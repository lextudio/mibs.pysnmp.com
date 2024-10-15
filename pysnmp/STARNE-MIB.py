# SNMP MIB module (STARNE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STARNE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:54 2024
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

_Samsung_ObjectIdentity = ObjectIdentity
samsung = _Samsung_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236)
)
_StarNeMib_ObjectIdentity = ObjectIdentity
starNeMib = _StarNeMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5)
)
_StarSystem_ObjectIdentity = ObjectIdentity
starSystem = _StarSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 1)
)
_StarSysGeneric_ObjectIdentity = ObjectIdentity
starSysGeneric = _StarSysGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1)
)


class _StarNeId_Type(Integer32):
    """Custom type starNeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_StarNeId_Type.__name__ = "Integer32"
_StarNeId_Object = MibScalar
starNeId = _StarNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 1),
    _StarNeId_Type()
)
starNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeId.setStatus("mandatory")
_StarNeDescr_Type = DisplayString
_StarNeDescr_Object = MibScalar
starNeDescr = _StarNeDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 2),
    _StarNeDescr_Type()
)
starNeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeDescr.setStatus("mandatory")
_StarNeMipAddress_Type = IpAddress
_StarNeMipAddress_Object = MibScalar
starNeMipAddress = _StarNeMipAddress_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 3),
    _StarNeMipAddress_Type()
)
starNeMipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeMipAddress.setStatus("mandatory")
_StarNeTimeofDay_Type = TimeTicks
_StarNeTimeofDay_Object = MibScalar
starNeTimeofDay = _StarNeTimeofDay_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 4),
    _StarNeTimeofDay_Type()
)
starNeTimeofDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starNeTimeofDay.setStatus("mandatory")
_StarNeOperStatus_Type = Integer32
_StarNeOperStatus_Object = MibScalar
starNeOperStatus = _StarNeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 5),
    _StarNeOperStatus_Type()
)
starNeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeOperStatus.setStatus("mandatory")


class _StarNeReset_Type(Integer32):
    """Custom type starNeReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 1),
          ("reset", 2))
    )


_StarNeReset_Type.__name__ = "Integer32"
_StarNeReset_Object = MibScalar
starNeReset = _StarNeReset_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 6),
    _StarNeReset_Type()
)
starNeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starNeReset.setStatus("mandatory")
_StarNeSlotReset_Type = Integer32
_StarNeSlotReset_Object = MibScalar
starNeSlotReset = _StarNeSlotReset_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 7),
    _StarNeSlotReset_Type()
)
starNeSlotReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    starNeSlotReset.setStatus("mandatory")
_StarNeSwDownload_Type = DisplayString
_StarNeSwDownload_Object = MibScalar
starNeSwDownload = _StarNeSwDownload_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 8),
    _StarNeSwDownload_Type()
)
starNeSwDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starNeSwDownload.setStatus("mandatory")
_StarNeHwVersion_Type = Integer32
_StarNeHwVersion_Object = MibScalar
starNeHwVersion = _StarNeHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 9),
    _StarNeHwVersion_Type()
)
starNeHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeHwVersion.setStatus("mandatory")
_StarNeBootSwVersion_Type = Integer32
_StarNeBootSwVersion_Object = MibScalar
starNeBootSwVersion = _StarNeBootSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 10),
    _StarNeBootSwVersion_Type()
)
starNeBootSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeBootSwVersion.setStatus("mandatory")
_StarNeSwVersion_Type = Integer32
_StarNeSwVersion_Object = MibScalar
starNeSwVersion = _StarNeSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 11),
    _StarNeSwVersion_Type()
)
starNeSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeSwVersion.setStatus("mandatory")
_StarNeXCoordinate_Type = Integer32
_StarNeXCoordinate_Object = MibScalar
starNeXCoordinate = _StarNeXCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 12),
    _StarNeXCoordinate_Type()
)
starNeXCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starNeXCoordinate.setStatus("mandatory")
_StarNeYCoordinate_Type = Integer32
_StarNeYCoordinate_Object = MibScalar
starNeYCoordinate = _StarNeYCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 13),
    _StarNeYCoordinate_Type()
)
starNeYCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starNeYCoordinate.setStatus("mandatory")
_StarNeNodeManagerIP_Type = IpAddress
_StarNeNodeManagerIP_Object = MibScalar
starNeNodeManagerIP = _StarNeNodeManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 14),
    _StarNeNodeManagerIP_Type()
)
starNeNodeManagerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeNodeManagerIP.setStatus("mandatory")
_StarNeMasterManagerIP_Type = IpAddress
_StarNeMasterManagerIP_Object = MibScalar
starNeMasterManagerIP = _StarNeMasterManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 15),
    _StarNeMasterManagerIP_Type()
)
starNeMasterManagerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeMasterManagerIP.setStatus("mandatory")
_StarNeStandbyMasterManagerIP_Type = IpAddress
_StarNeStandbyMasterManagerIP_Object = MibScalar
starNeStandbyMasterManagerIP = _StarNeStandbyMasterManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 16),
    _StarNeStandbyMasterManagerIP_Type()
)
starNeStandbyMasterManagerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeStandbyMasterManagerIP.setStatus("mandatory")


class _StarNeAlive_Type(Integer32):
    """Custom type starNeAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onespu", 1),
          ("twospu", 2))
    )


_StarNeAlive_Type.__name__ = "Integer32"
_StarNeAlive_Object = MibScalar
starNeAlive = _StarNeAlive_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 17),
    _StarNeAlive_Type()
)
starNeAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeAlive.setStatus("mandatory")
_StarMibRegister_Type = Integer32
_StarMibRegister_Object = MibScalar
starMibRegister = _StarMibRegister_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 18),
    _StarMibRegister_Type()
)
starMibRegister.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    starMibRegister.setStatus("mandatory")
_StarNeCurrentAlarmTftp_Type = Integer32
_StarNeCurrentAlarmTftp_Object = MibScalar
starNeCurrentAlarmTftp = _StarNeCurrentAlarmTftp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 19),
    _StarNeCurrentAlarmTftp_Type()
)
starNeCurrentAlarmTftp.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    starNeCurrentAlarmTftp.setStatus("mandatory")
_StarNeCurrentTimeDescr_Type = DisplayString
_StarNeCurrentTimeDescr_Object = MibScalar
starNeCurrentTimeDescr = _StarNeCurrentTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 20),
    _StarNeCurrentTimeDescr_Type()
)
starNeCurrentTimeDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starNeCurrentTimeDescr.setStatus("mandatory")
_StarNeSoftwareVersion_Type = DisplayString
_StarNeSoftwareVersion_Object = MibScalar
starNeSoftwareVersion = _StarNeSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 22),
    _StarNeSoftwareVersion_Type()
)
starNeSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeSoftwareVersion.setStatus("mandatory")


class _StarNeSoftwareType_Type(Integer32):
    """Custom type starNeSoftwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("star1", 1)
    )


_StarNeSoftwareType_Type.__name__ = "Integer32"
_StarNeSoftwareType_Object = MibScalar
starNeSoftwareType = _StarNeSoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 23),
    _StarNeSoftwareType_Type()
)
starNeSoftwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeSoftwareType.setStatus("mandatory")
_StarNeSwUpgradeDownload_Type = Integer32
_StarNeSwUpgradeDownload_Object = MibScalar
starNeSwUpgradeDownload = _StarNeSwUpgradeDownload_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 24),
    _StarNeSwUpgradeDownload_Type()
)
starNeSwUpgradeDownload.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    starNeSwUpgradeDownload.setStatus("mandatory")
_StarNeSwUpgradeCancel_Type = Integer32
_StarNeSwUpgradeCancel_Object = MibScalar
starNeSwUpgradeCancel = _StarNeSwUpgradeCancel_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 25),
    _StarNeSwUpgradeCancel_Type()
)
starNeSwUpgradeCancel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    starNeSwUpgradeCancel.setStatus("mandatory")
_StarNeSwUpgradeActionTrigger_Type = Integer32
_StarNeSwUpgradeActionTrigger_Object = MibScalar
starNeSwUpgradeActionTrigger = _StarNeSwUpgradeActionTrigger_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 26),
    _StarNeSwUpgradeActionTrigger_Type()
)
starNeSwUpgradeActionTrigger.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    starNeSwUpgradeActionTrigger.setStatus("mandatory")
_StarNeSwUpgradedFiles_Type = Integer32
_StarNeSwUpgradedFiles_Object = MibScalar
starNeSwUpgradedFiles = _StarNeSwUpgradedFiles_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 27),
    _StarNeSwUpgradedFiles_Type()
)
starNeSwUpgradedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeSwUpgradedFiles.setStatus("mandatory")
_StarNeSwUpgradeCurrentFile_Type = Integer32
_StarNeSwUpgradeCurrentFile_Object = MibScalar
starNeSwUpgradeCurrentFile = _StarNeSwUpgradeCurrentFile_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 28),
    _StarNeSwUpgradeCurrentFile_Type()
)
starNeSwUpgradeCurrentFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeSwUpgradeCurrentFile.setStatus("mandatory")
_StarNeSwUpgradeStatus_Type = Integer32
_StarNeSwUpgradeStatus_Object = MibScalar
starNeSwUpgradeStatus = _StarNeSwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 1, 29),
    _StarNeSwUpgradeStatus_Type()
)
starNeSwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starNeSwUpgradeStatus.setStatus("mandatory")
_StarSysSlotRedundencyInfo_ObjectIdentity = ObjectIdentity
starSysSlotRedundencyInfo = _StarSysSlotRedundencyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 2)
)
_StarActiveSPUSlotNo_Type = Integer32
_StarActiveSPUSlotNo_Object = MibScalar
starActiveSPUSlotNo = _StarActiveSPUSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 2, 1),
    _StarActiveSPUSlotNo_Type()
)
starActiveSPUSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starActiveSPUSlotNo.setStatus("mandatory")
_StarStandbySPUSlotNo_Type = Integer32
_StarStandbySPUSlotNo_Object = MibScalar
starStandbySPUSlotNo = _StarStandbySPUSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 2, 2),
    _StarStandbySPUSlotNo_Type()
)
starStandbySPUSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starStandbySPUSlotNo.setStatus("mandatory")
_StarActiveSCUSlotNo_Type = Integer32
_StarActiveSCUSlotNo_Object = MibScalar
starActiveSCUSlotNo = _StarActiveSCUSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 2, 3),
    _StarActiveSCUSlotNo_Type()
)
starActiveSCUSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starActiveSCUSlotNo.setStatus("mandatory")
_StarStandbySCUSlotNo_Type = Integer32
_StarStandbySCUSlotNo_Object = MibScalar
starStandbySCUSlotNo = _StarStandbySCUSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 2, 4),
    _StarStandbySCUSlotNo_Type()
)
starStandbySCUSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starStandbySCUSlotNo.setStatus("mandatory")
_StarActiveSSUSlotNo_Type = Integer32
_StarActiveSSUSlotNo_Object = MibScalar
starActiveSSUSlotNo = _StarActiveSSUSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 2, 5),
    _StarActiveSSUSlotNo_Type()
)
starActiveSSUSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starActiveSSUSlotNo.setStatus("mandatory")
_StarStandbySSUSlotNo_Type = Integer32
_StarStandbySSUSlotNo_Object = MibScalar
starStandbySSUSlotNo = _StarStandbySSUSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 2, 6),
    _StarStandbySSUSlotNo_Type()
)
starStandbySSUSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starStandbySSUSlotNo.setStatus("mandatory")
_StarConfigManager_ObjectIdentity = ObjectIdentity
starConfigManager = _StarConfigManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3)
)


class _StarCfAllChanged_Type(Integer32):
    """Custom type starCfAllChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 2),
          ("notchanged", 1))
    )


_StarCfAllChanged_Type.__name__ = "Integer32"
_StarCfAllChanged_Object = MibScalar
starCfAllChanged = _StarCfAllChanged_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 1),
    _StarCfAllChanged_Type()
)
starCfAllChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCfAllChanged.setStatus("mandatory")
_StarCfFileChanged_Type = DisplayString
_StarCfFileChanged_Object = MibScalar
starCfFileChanged = _StarCfFileChanged_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 2),
    _StarCfFileChanged_Type()
)
starCfFileChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCfFileChanged.setStatus("mandatory")
_StarCfBootFileName_Type = DisplayString
_StarCfBootFileName_Object = MibScalar
starCfBootFileName = _StarCfBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 3),
    _StarCfBootFileName_Type()
)
starCfBootFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfBootFileName.setStatus("mandatory")


class _StarCfShelf_Type(Integer32):
    """Custom type starCfShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )


_StarCfShelf_Type.__name__ = "Integer32"
_StarCfShelf_Object = MibScalar
starCfShelf = _StarCfShelf_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 4),
    _StarCfShelf_Type()
)
starCfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCfShelf.setStatus("mandatory")


class _StarCfMaxSlots_Type(Integer32):
    """Custom type starCfMaxSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_StarCfMaxSlots_Type.__name__ = "Integer32"
_StarCfMaxSlots_Object = MibScalar
starCfMaxSlots = _StarCfMaxSlots_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 5),
    _StarCfMaxSlots_Type()
)
starCfMaxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfMaxSlots.setStatus("mandatory")


class _StarCfBootSwitch_Type(Integer32):
    """Custom type starCfBootSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("mastermgr", 3),
          ("nodemgr", 2))
    )


_StarCfBootSwitch_Type.__name__ = "Integer32"
_StarCfBootSwitch_Object = MibScalar
starCfBootSwitch = _StarCfBootSwitch_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 6),
    _StarCfBootSwitch_Type()
)
starCfBootSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCfBootSwitch.setStatus("mandatory")


class _StarCfInvalidateFlash_Type(Integer32):
    """Custom type starCfInvalidateFlash based on Integer32"""
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


_StarCfInvalidateFlash_Type.__name__ = "Integer32"
_StarCfInvalidateFlash_Object = MibScalar
starCfInvalidateFlash = _StarCfInvalidateFlash_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 7),
    _StarCfInvalidateFlash_Type()
)
starCfInvalidateFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCfInvalidateFlash.setStatus("mandatory")


class _StarCfActivePSUNo_Type(Integer32):
    """Custom type starCfActivePSUNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_StarCfActivePSUNo_Type.__name__ = "Integer32"
_StarCfActivePSUNo_Object = MibScalar
starCfActivePSUNo = _StarCfActivePSUNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 8),
    _StarCfActivePSUNo_Type()
)
starCfActivePSUNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfActivePSUNo.setStatus("mandatory")


class _StarCfPSUOperStatus_Type(Integer32):
    """Custom type starCfPSUOperStatus based on Integer32"""
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
        *(("psu1installed", 2),
          ("psu1on", 1),
          ("psu2installed", 8),
          ("psu2on", 4),
          ("psu3installed", 32),
          ("psu3on", 16),
          ("psu4installed", 128),
          ("psu4on", 64))
    )


_StarCfPSUOperStatus_Type.__name__ = "Integer32"
_StarCfPSUOperStatus_Object = MibScalar
starCfPSUOperStatus = _StarCfPSUOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 9),
    _StarCfPSUOperStatus_Type()
)
starCfPSUOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfPSUOperStatus.setStatus("mandatory")


class _StarCfFanStatus_Type(Integer32):
    """Custom type starCfFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fan1on", 1),
          ("fan2on", 2),
          ("fan3on", 4),
          ("fan4on", 8))
    )


_StarCfFanStatus_Type.__name__ = "Integer32"
_StarCfFanStatus_Object = MibScalar
starCfFanStatus = _StarCfFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 10),
    _StarCfFanStatus_Type()
)
starCfFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfFanStatus.setStatus("mandatory")


class _StarCfAluLedStatus_Type(Integer32):
    """Custom type starCfAluLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("aco", 16),
          ("buzzer", 64),
          ("critical", 1),
          ("fanfail", 32),
          ("history", 8),
          ("major", 2),
          ("minor", 4))
    )


_StarCfAluLedStatus_Type.__name__ = "Integer32"
_StarCfAluLedStatus_Object = MibScalar
starCfAluLedStatus = _StarCfAluLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 11),
    _StarCfAluLedStatus_Type()
)
starCfAluLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfAluLedStatus.setStatus("mandatory")
_StarCfAluCharacterDisplay_Type = DisplayString
_StarCfAluCharacterDisplay_Object = MibScalar
starCfAluCharacterDisplay = _StarCfAluCharacterDisplay_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 12),
    _StarCfAluCharacterDisplay_Type()
)
starCfAluCharacterDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfAluCharacterDisplay.setStatus("mandatory")


class _StarCfAluBrightness_Type(Integer32):
    """Custom type starCfAluBrightness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_StarCfAluBrightness_Type.__name__ = "Integer32"
_StarCfAluBrightness_Object = MibScalar
starCfAluBrightness = _StarCfAluBrightness_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 13),
    _StarCfAluBrightness_Type()
)
starCfAluBrightness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCfAluBrightness.setStatus("mandatory")


class _StarCfSlotInstalled_Type(Integer32):
    """Custom type starCfSlotInstalled based on Integer32"""
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
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384)
        )
    )
    namedValues = NamedValues(
        *(("slot10installed", 512),
          ("slot11installed", 1024),
          ("slot12installed", 2048),
          ("slot13installed", 4096),
          ("slot14installed", 8192),
          ("slot15installed", 16384),
          ("slot1installed", 1),
          ("slot2installed", 2),
          ("slot3installed", 4),
          ("slot4installed", 8),
          ("slot5installed", 16),
          ("slot6installed", 32),
          ("slot7installed", 64),
          ("slot8installed", 128),
          ("slot9installed", 256))
    )


_StarCfSlotInstalled_Type.__name__ = "Integer32"
_StarCfSlotInstalled_Object = MibScalar
starCfSlotInstalled = _StarCfSlotInstalled_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 3, 14),
    _StarCfSlotInstalled_Type()
)
starCfSlotInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfSlotInstalled.setStatus("mandatory")
_StarAccountManager_ObjectIdentity = ObjectIdentity
starAccountManager = _StarAccountManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 4)
)
_StarAmCDRFileGetCompleted_Type = Integer32
_StarAmCDRFileGetCompleted_Object = MibScalar
starAmCDRFileGetCompleted = _StarAmCDRFileGetCompleted_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 4, 1),
    _StarAmCDRFileGetCompleted_Type()
)
starAmCDRFileGetCompleted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starAmCDRFileGetCompleted.setStatus("mandatory")
_StarAmCDRThresholdCount_Type = Integer32
_StarAmCDRThresholdCount_Object = MibScalar
starAmCDRThresholdCount = _StarAmCDRThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 4, 2),
    _StarAmCDRThresholdCount_Type()
)
starAmCDRThresholdCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starAmCDRThresholdCount.setStatus("mandatory")
_StarAmCDRThresholdTime_Type = Integer32
_StarAmCDRThresholdTime_Object = MibScalar
starAmCDRThresholdTime = _StarAmCDRThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 4, 3),
    _StarAmCDRThresholdTime_Type()
)
starAmCDRThresholdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starAmCDRThresholdTime.setStatus("mandatory")
_StarAmCDRFileGetRequest_Type = Integer32
_StarAmCDRFileGetRequest_Object = MibScalar
starAmCDRFileGetRequest = _StarAmCDRFileGetRequest_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 4, 4),
    _StarAmCDRFileGetRequest_Type()
)
starAmCDRFileGetRequest.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    starAmCDRFileGetRequest.setStatus("mandatory")
_StarAmCDRFileCount_Type = Integer32
_StarAmCDRFileCount_Object = MibScalar
starAmCDRFileCount = _StarAmCDRFileCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 4, 5),
    _StarAmCDRFileCount_Type()
)
starAmCDRFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAmCDRFileCount.setStatus("mandatory")
_StarAmCDRMaxCount_Type = Integer32
_StarAmCDRMaxCount_Object = MibScalar
starAmCDRMaxCount = _StarAmCDRMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 4, 6),
    _StarAmCDRMaxCount_Type()
)
starAmCDRMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starAmCDRMaxCount.setStatus("mandatory")
_StarAmCacheTimer_Type = Integer32
_StarAmCacheTimer_Object = MibScalar
starAmCacheTimer = _StarAmCacheTimer_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 4, 7),
    _StarAmCacheTimer_Type()
)
starAmCacheTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starAmCacheTimer.setStatus("mandatory")
_StarAmCacheCounter_Type = Integer32
_StarAmCacheCounter_Object = MibScalar
starAmCacheCounter = _StarAmCacheCounter_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 4, 8),
    _StarAmCacheCounter_Type()
)
starAmCacheCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starAmCacheCounter.setStatus("mandatory")
_StarFaultManager_ObjectIdentity = ObjectIdentity
starFaultManager = _StarFaultManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 5)
)


class _StarFmSendTrapThreshold_Type(Integer32):
    """Custom type starFmSendTrapThreshold based on Integer32"""
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
        *(("all", 5),
          ("cleared", 4),
          ("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_StarFmSendTrapThreshold_Type.__name__ = "Integer32"
_StarFmSendTrapThreshold_Object = MibScalar
starFmSendTrapThreshold = _StarFmSendTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 5, 1),
    _StarFmSendTrapThreshold_Type()
)
starFmSendTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starFmSendTrapThreshold.setStatus("mandatory")
_StarFmLogNotify_Type = Integer32
_StarFmLogNotify_Object = MibScalar
starFmLogNotify = _StarFmLogNotify_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 5, 2),
    _StarFmLogNotify_Type()
)
starFmLogNotify.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    starFmLogNotify.setStatus("mandatory")
_StarFmLogFileInterval_Type = Integer32
_StarFmLogFileInterval_Object = MibScalar
starFmLogFileInterval = _StarFmLogFileInterval_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 5, 3),
    _StarFmLogFileInterval_Type()
)
starFmLogFileInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starFmLogFileInterval.setStatus("mandatory")
_StarSysSlotStatusTable_Object = MibTable
starSysSlotStatusTable = _StarSysSlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6)
)
if mibBuilder.loadTexts:
    starSysSlotStatusTable.setStatus("mandatory")
_StarSysSlotStatusEntry_Object = MibTableRow
starSysSlotStatusEntry = _StarSysSlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1)
)
starSysSlotStatusEntry.setIndexNames(
    (0, "STARNE-MIB", "starSSDIndex"),
)
if mibBuilder.loadTexts:
    starSysSlotStatusEntry.setStatus("mandatory")


class _StarSSDIndex_Type(Integer32):
    """Custom type starSSDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_StarSSDIndex_Type.__name__ = "Integer32"
_StarSSDIndex_Object = MibTableColumn
starSSDIndex = _StarSSDIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 1),
    _StarSSDIndex_Type()
)
starSSDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSDIndex.setStatus("mandatory")


class _StarSSDBdEquipStatus_Type(Integer32):
    """Custom type starSSDBdEquipStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equip", 2),
          ("noEquip", 1))
    )


_StarSSDBdEquipStatus_Type.__name__ = "Integer32"
_StarSSDBdEquipStatus_Object = MibTableColumn
starSSDBdEquipStatus = _StarSSDBdEquipStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 2),
    _StarSSDBdEquipStatus_Type()
)
starSSDBdEquipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSDBdEquipStatus.setStatus("mandatory")
_StarSSDModuleType_Type = Integer32
_StarSSDModuleType_Object = MibTableColumn
starSSDModuleType = _StarSSDModuleType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 3),
    _StarSSDModuleType_Type()
)
starSSDModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSDModuleType.setStatus("mandatory")
_StarSSDInterfaceType_Type = Integer32
_StarSSDInterfaceType_Object = MibTableColumn
starSSDInterfaceType = _StarSSDInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 4),
    _StarSSDInterfaceType_Type()
)
starSSDInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSDInterfaceType.setStatus("mandatory")


class _StarSSDOperStatus_Type(Integer32):
    """Custom type starSSDOperStatus based on Integer32"""
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
        *(("active", 3),
          ("deactive", 4),
          ("delete", 1),
          ("install", 2))
    )


_StarSSDOperStatus_Type.__name__ = "Integer32"
_StarSSDOperStatus_Object = MibTableColumn
starSSDOperStatus = _StarSSDOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 5),
    _StarSSDOperStatus_Type()
)
starSSDOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSDOperStatus.setStatus("mandatory")


class _StarSSDCpuFailStatus_Type(Integer32):
    """Custom type starSSDCpuFailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("normal", 2))
    )


_StarSSDCpuFailStatus_Type.__name__ = "Integer32"
_StarSSDCpuFailStatus_Object = MibTableColumn
starSSDCpuFailStatus = _StarSSDCpuFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 6),
    _StarSSDCpuFailStatus_Type()
)
starSSDCpuFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSDCpuFailStatus.setStatus("mandatory")


class _StarSSDPwrFailStatus_Type(Integer32):
    """Custom type starSSDPwrFailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("normal", 2))
    )


_StarSSDPwrFailStatus_Type.__name__ = "Integer32"
_StarSSDPwrFailStatus_Object = MibTableColumn
starSSDPwrFailStatus = _StarSSDPwrFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 7),
    _StarSSDPwrFailStatus_Type()
)
starSSDPwrFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSDPwrFailStatus.setStatus("mandatory")
_StarSSDRealStatus_Type = Integer32
_StarSSDRealStatus_Object = MibTableColumn
starSSDRealStatus = _StarSSDRealStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 8),
    _StarSSDRealStatus_Type()
)
starSSDRealStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSDRealStatus.setStatus("mandatory")


class _StarSiuRednConfigStatus_Type(Integer32):
    """Custom type starSiuRednConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("maxRedund", 4),
          ("primary", 1),
          ("secondary", 2),
          ("standalone", 0),
          ("undefined", 3))
    )


_StarSiuRednConfigStatus_Type.__name__ = "Integer32"
_StarSiuRednConfigStatus_Object = MibTableColumn
starSiuRednConfigStatus = _StarSiuRednConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 9),
    _StarSiuRednConfigStatus_Type()
)
starSiuRednConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSiuRednConfigStatus.setStatus("mandatory")


class _StarSiuRednOperStatus_Type(Integer32):
    """Custom type starSiuRednOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failedRole", 4),
          ("maxRedund", 5),
          ("standalone", 0),
          ("standby", 2),
          ("unknown", 3))
    )


_StarSiuRednOperStatus_Type.__name__ = "Integer32"
_StarSiuRednOperStatus_Object = MibTableColumn
starSiuRednOperStatus = _StarSiuRednOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 10),
    _StarSiuRednOperStatus_Type()
)
starSiuRednOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSiuRednOperStatus.setStatus("mandatory")
_StarSiuRednSwitchOver_Type = Integer32
_StarSiuRednSwitchOver_Object = MibTableColumn
starSiuRednSwitchOver = _StarSiuRednSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 6, 1, 11),
    _StarSiuRednSwitchOver_Type()
)
starSiuRednSwitchOver.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    starSiuRednSwitchOver.setStatus("mandatory")
_StarFaultControlTable_Object = MibTable
starFaultControlTable = _StarFaultControlTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 7)
)
if mibBuilder.loadTexts:
    starFaultControlTable.setStatus("mandatory")
_StarFaultControlEntry_Object = MibTableRow
starFaultControlEntry = _StarFaultControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 7, 1)
)
starFaultControlEntry.setIndexNames(
    (0, "STARNE-MIB", "starFaultSlotId"),
    (0, "STARNE-MIB", "starFaultGroupId"),
    (0, "STARNE-MIB", "starFaultSubId"),
)
if mibBuilder.loadTexts:
    starFaultControlEntry.setStatus("mandatory")
_StarFaultSlotId_Type = Integer32
_StarFaultSlotId_Object = MibTableColumn
starFaultSlotId = _StarFaultSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 7, 1, 1),
    _StarFaultSlotId_Type()
)
starFaultSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFaultSlotId.setStatus("mandatory")
_StarFaultGroupId_Type = Integer32
_StarFaultGroupId_Object = MibTableColumn
starFaultGroupId = _StarFaultGroupId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 7, 1, 2),
    _StarFaultGroupId_Type()
)
starFaultGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFaultGroupId.setStatus("mandatory")
_StarFaultSubId_Type = Integer32
_StarFaultSubId_Object = MibTableColumn
starFaultSubId = _StarFaultSubId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 7, 1, 3),
    _StarFaultSubId_Type()
)
starFaultSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFaultSubId.setStatus("mandatory")
_StarSeverity_Type = Integer32
_StarSeverity_Object = MibTableColumn
starSeverity = _StarSeverity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 7, 1, 4),
    _StarSeverity_Type()
)
starSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSeverity.setStatus("mandatory")
_StarFaultThresholdType_Type = Integer32
_StarFaultThresholdType_Object = MibTableColumn
starFaultThresholdType = _StarFaultThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 7, 1, 5),
    _StarFaultThresholdType_Type()
)
starFaultThresholdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starFaultThresholdType.setStatus("mandatory")
_StarFaultHappenValue_Type = Integer32
_StarFaultHappenValue_Object = MibTableColumn
starFaultHappenValue = _StarFaultHappenValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 7, 1, 6),
    _StarFaultHappenValue_Type()
)
starFaultHappenValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starFaultHappenValue.setStatus("mandatory")
_StarFaultClearValue_Type = Integer32
_StarFaultClearValue_Object = MibTableColumn
starFaultClearValue = _StarFaultClearValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 7, 1, 7),
    _StarFaultClearValue_Type()
)
starFaultClearValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starFaultClearValue.setStatus("mandatory")
_StarTrapControlTable_Object = MibTable
starTrapControlTable = _StarTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 8)
)
if mibBuilder.loadTexts:
    starTrapControlTable.setStatus("mandatory")
_StarTrapControlEntry_Object = MibTableRow
starTrapControlEntry = _StarTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 8, 1)
)
starTrapControlEntry.setIndexNames(
    (0, "STARNE-MIB", "starTrapGroupId"),
    (0, "STARNE-MIB", "starTrapSubId"),
)
if mibBuilder.loadTexts:
    starTrapControlEntry.setStatus("mandatory")
_StarTrapGroupId_Type = Integer32
_StarTrapGroupId_Object = MibTableColumn
starTrapGroupId = _StarTrapGroupId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 8, 1, 1),
    _StarTrapGroupId_Type()
)
starTrapGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starTrapGroupId.setStatus("mandatory")
_StarTrapSubId_Type = Integer32
_StarTrapSubId_Object = MibTableColumn
starTrapSubId = _StarTrapSubId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 8, 1, 2),
    _StarTrapSubId_Type()
)
starTrapSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starTrapSubId.setStatus("mandatory")
_StarTrapSendCondition_Type = Integer32
_StarTrapSendCondition_Object = MibTableColumn
starTrapSendCondition = _StarTrapSendCondition_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 8, 1, 3),
    _StarTrapSendCondition_Type()
)
starTrapSendCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starTrapSendCondition.setStatus("mandatory")
_StarMipRouteTable_Object = MibTable
starMipRouteTable = _StarMipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 9)
)
if mibBuilder.loadTexts:
    starMipRouteTable.setStatus("mandatory")
_StarMipRouteEntry_Object = MibTableRow
starMipRouteEntry = _StarMipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 9, 1)
)
starMipRouteEntry.setIndexNames(
    (0, "STARNE-MIB", "starMipDestNeId"),
)
if mibBuilder.loadTexts:
    starMipRouteEntry.setStatus("mandatory")
_StarMipDestNeId_Type = Integer32
_StarMipDestNeId_Object = MibTableColumn
starMipDestNeId = _StarMipDestNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 9, 1, 1),
    _StarMipDestNeId_Type()
)
starMipDestNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starMipDestNeId.setStatus("mandatory")
_StarMipSourceSlot_Type = Integer32
_StarMipSourceSlot_Object = MibTableColumn
starMipSourceSlot = _StarMipSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 9, 1, 2),
    _StarMipSourceSlot_Type()
)
starMipSourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starMipSourceSlot.setStatus("mandatory")
_StarMipSourcePort_Type = Integer32
_StarMipSourcePort_Object = MibTableColumn
starMipSourcePort = _StarMipSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 9, 1, 3),
    _StarMipSourcePort_Type()
)
starMipSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starMipSourcePort.setStatus("mandatory")
_StarSvcAts_ObjectIdentity = ObjectIdentity
starSvcAts = _StarSvcAts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10)
)
_StarSvcAtsValue_ObjectIdentity = ObjectIdentity
starSvcAtsValue = _StarSvcAtsValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 1)
)
_StarSvcAtsRxReqCount_Type = Integer32
_StarSvcAtsRxReqCount_Object = MibScalar
starSvcAtsRxReqCount = _StarSvcAtsRxReqCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 1, 1),
    _StarSvcAtsRxReqCount_Type()
)
starSvcAtsRxReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcAtsRxReqCount.setStatus("mandatory")
_StarSvcAtsRxValidResponseCount_Type = Integer32
_StarSvcAtsRxValidResponseCount_Object = MibScalar
starSvcAtsRxValidResponseCount = _StarSvcAtsRxValidResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 1, 2),
    _StarSvcAtsRxValidResponseCount_Type()
)
starSvcAtsRxValidResponseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcAtsRxValidResponseCount.setStatus("mandatory")
_StarSvcAtsRxInvalidResponseCount_Type = Integer32
_StarSvcAtsRxInvalidResponseCount_Object = MibScalar
starSvcAtsRxInvalidResponseCount = _StarSvcAtsRxInvalidResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 1, 3),
    _StarSvcAtsRxInvalidResponseCount_Type()
)
starSvcAtsRxInvalidResponseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcAtsRxInvalidResponseCount.setStatus("mandatory")
_StarSvcAtsNotCacheCount_Type = Integer32
_StarSvcAtsNotCacheCount_Object = MibScalar
starSvcAtsNotCacheCount = _StarSvcAtsNotCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 1, 4),
    _StarSvcAtsNotCacheCount_Type()
)
starSvcAtsNotCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcAtsNotCacheCount.setStatus("mandatory")
_StarSvcAtsCachedReqCount_Type = Integer32
_StarSvcAtsCachedReqCount_Object = MibScalar
starSvcAtsCachedReqCount = _StarSvcAtsCachedReqCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 1, 5),
    _StarSvcAtsCachedReqCount_Type()
)
starSvcAtsCachedReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcAtsCachedReqCount.setStatus("mandatory")
_StarSvcAtsTCPConnTrialCount_Type = Integer32
_StarSvcAtsTCPConnTrialCount_Object = MibScalar
starSvcAtsTCPConnTrialCount = _StarSvcAtsTCPConnTrialCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 1, 6),
    _StarSvcAtsTCPConnTrialCount_Type()
)
starSvcAtsTCPConnTrialCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcAtsTCPConnTrialCount.setStatus("mandatory")
_StarSvcAtsStatusTable_Object = MibTable
starSvcAtsStatusTable = _StarSvcAtsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 2)
)
if mibBuilder.loadTexts:
    starSvcAtsStatusTable.setStatus("mandatory")
_StarSvcAtsStatusEntry_Object = MibTableRow
starSvcAtsStatusEntry = _StarSvcAtsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 2, 1)
)
starSvcAtsStatusEntry.setIndexNames(
    (0, "STARNE-MIB", "starSvcAtsIndex"),
)
if mibBuilder.loadTexts:
    starSvcAtsStatusEntry.setStatus("mandatory")
_StarSvcAtsIndex_Type = Integer32
_StarSvcAtsIndex_Object = MibTableColumn
starSvcAtsIndex = _StarSvcAtsIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 2, 1, 1),
    _StarSvcAtsIndex_Type()
)
starSvcAtsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcAtsIndex.setStatus("mandatory")
_StarSvcAtsServerStatus_Type = Integer32
_StarSvcAtsServerStatus_Object = MibTableColumn
starSvcAtsServerStatus = _StarSvcAtsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 10, 2, 1, 2),
    _StarSvcAtsServerStatus_Type()
)
starSvcAtsServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSvcAtsServerStatus.setStatus("mandatory")
_StarPerformanceManager_ObjectIdentity = ObjectIdentity
starPerformanceManager = _StarPerformanceManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 11)
)
_StarPmReportInterval_Type = Integer32
_StarPmReportInterval_Object = MibScalar
starPmReportInterval = _StarPmReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 11, 1),
    _StarPmReportInterval_Type()
)
starPmReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmReportInterval.setStatus("mandatory")
_StarPmCollectInterval_Type = Integer32
_StarPmCollectInterval_Object = MibScalar
starPmCollectInterval = _StarPmCollectInterval_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 11, 2),
    _StarPmCollectInterval_Type()
)
starPmCollectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCollectInterval.setStatus("mandatory")
_StarPmStatsChangeTable_Object = MibTable
starPmStatsChangeTable = _StarPmStatsChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 11, 3)
)
if mibBuilder.loadTexts:
    starPmStatsChangeTable.setStatus("mandatory")
_StarPmStatsChangeEntry_Object = MibTableRow
starPmStatsChangeEntry = _StarPmStatsChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 11, 3, 1)
)
starPmStatsChangeEntry.setIndexNames(
    (0, "STARNE-MIB", "starPmIndex"),
)
if mibBuilder.loadTexts:
    starPmStatsChangeEntry.setStatus("mandatory")
_StarPmIndex_Type = Integer32
_StarPmIndex_Object = MibTableColumn
starPmIndex = _StarPmIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 11, 3, 1, 1),
    _StarPmIndex_Type()
)
starPmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPmIndex.setStatus("mandatory")
_StarPmPortStatusChange_Type = OctetString
_StarPmPortStatusChange_Object = MibTableColumn
starPmPortStatusChange = _StarPmPortStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 11, 3, 1, 2),
    _StarPmPortStatusChange_Type()
)
starPmPortStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmPortStatusChange.setStatus("mandatory")
_StarPmConnStatusChange_Type = OctetString
_StarPmConnStatusChange_Object = MibTableColumn
starPmConnStatusChange = _StarPmConnStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 1, 11, 3, 1, 3),
    _StarPmConnStatusChange_Type()
)
starPmConnStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmConnStatusChange.setStatus("mandatory")
_StarSlot_ObjectIdentity = ObjectIdentity
starSlot = _StarSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2)
)
_StarSlotTable_Object = MibTable
starSlotTable = _StarSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1)
)
if mibBuilder.loadTexts:
    starSlotTable.setStatus("mandatory")
_StarSlotEntry_Object = MibTableRow
starSlotEntry = _StarSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1)
)
starSlotEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
)
if mibBuilder.loadTexts:
    starSlotEntry.setStatus("mandatory")


class _StarSlotIndex_Type(Integer32):
    """Custom type starSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_StarSlotIndex_Type.__name__ = "Integer32"
_StarSlotIndex_Object = MibTableColumn
starSlotIndex = _StarSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 1),
    _StarSlotIndex_Type()
)
starSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotIndex.setStatus("mandatory")
_StarSlotModuleType_Type = Integer32
_StarSlotModuleType_Object = MibTableColumn
starSlotModuleType = _StarSlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 2),
    _StarSlotModuleType_Type()
)
starSlotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotModuleType.setStatus("mandatory")
_StarSlotInterfaceType_Type = Integer32
_StarSlotInterfaceType_Object = MibTableColumn
starSlotInterfaceType = _StarSlotInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 3),
    _StarSlotInterfaceType_Type()
)
starSlotInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotInterfaceType.setStatus("mandatory")
_StarSlotModuleDescr_Type = DisplayString
_StarSlotModuleDescr_Object = MibTableColumn
starSlotModuleDescr = _StarSlotModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 4),
    _StarSlotModuleDescr_Type()
)
starSlotModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotModuleDescr.setStatus("mandatory")
_StarSlotMaxPortNo_Type = Integer32
_StarSlotMaxPortNo_Object = MibTableColumn
starSlotMaxPortNo = _StarSlotMaxPortNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 5),
    _StarSlotMaxPortNo_Type()
)
starSlotMaxPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotMaxPortNo.setStatus("mandatory")


class _StarSlotModuleCpuUtilization_Type(Integer32):
    """Custom type starSlotModuleCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StarSlotModuleCpuUtilization_Type.__name__ = "Integer32"
_StarSlotModuleCpuUtilization_Object = MibTableColumn
starSlotModuleCpuUtilization = _StarSlotModuleCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 6),
    _StarSlotModuleCpuUtilization_Type()
)
starSlotModuleCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotModuleCpuUtilization.setStatus("mandatory")
_StarSlotModuleHwVersion_Type = Integer32
_StarSlotModuleHwVersion_Object = MibTableColumn
starSlotModuleHwVersion = _StarSlotModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 7),
    _StarSlotModuleHwVersion_Type()
)
starSlotModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotModuleHwVersion.setStatus("mandatory")
_StarSlotModuleSwVersion_Type = DisplayString
_StarSlotModuleSwVersion_Object = MibTableColumn
starSlotModuleSwVersion = _StarSlotModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 8),
    _StarSlotModuleSwVersion_Type()
)
starSlotModuleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotModuleSwVersion.setStatus("mandatory")
_StarSlotLastInstalledTime_Type = TimeTicks
_StarSlotLastInstalledTime_Object = MibTableColumn
starSlotLastInstalledTime = _StarSlotLastInstalledTime_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 9),
    _StarSlotLastInstalledTime_Type()
)
starSlotLastInstalledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotLastInstalledTime.setStatus("mandatory")
_StarSlotSSBStatus_Type = Integer32
_StarSlotSSBStatus_Object = MibTableColumn
starSlotSSBStatus = _StarSlotSSBStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 10),
    _StarSlotSSBStatus_Type()
)
starSlotSSBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotSSBStatus.setStatus("mandatory")
_StarSlotCellPathStatus_Type = Integer32
_StarSlotCellPathStatus_Object = MibTableColumn
starSlotCellPathStatus = _StarSlotCellPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 11),
    _StarSlotCellPathStatus_Type()
)
starSlotCellPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotCellPathStatus.setStatus("mandatory")
_StarSlotLineClkSource_Type = Integer32
_StarSlotLineClkSource_Object = MibTableColumn
starSlotLineClkSource = _StarSlotLineClkSource_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 12),
    _StarSlotLineClkSource_Type()
)
starSlotLineClkSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotLineClkSource.setStatus("mandatory")
_StarSlotVpiVciRange_Type = Integer32
_StarSlotVpiVciRange_Object = MibTableColumn
starSlotVpiVciRange = _StarSlotVpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 1, 1, 13),
    _StarSlotVpiVciRange_Type()
)
starSlotVpiVciRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSlotVpiVciRange.setStatus("mandatory")
_StarSlotSSUInfo_ObjectIdentity = ObjectIdentity
starSlotSSUInfo = _StarSlotSSUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4)
)
_StarSSULoadInfoTbl_Object = MibTable
starSSULoadInfoTbl = _StarSSULoadInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    starSSULoadInfoTbl.setStatus("mandatory")
_StarSSULoadInfoEntry_Object = MibTableRow
starSSULoadInfoEntry = _StarSSULoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1)
)
starSSULoadInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSSULoadInfoSlotId"),
)
if mibBuilder.loadTexts:
    starSSULoadInfoEntry.setStatus("mandatory")
_StarSSULoadInfoSlotId_Type = Integer32
_StarSSULoadInfoSlotId_Object = MibTableColumn
starSSULoadInfoSlotId = _StarSSULoadInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 1),
    _StarSSULoadInfoSlotId_Type()
)
starSSULoadInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadInfoSlotId.setStatus("mandatory")
_StarSSULoadTotalConnections_Type = Integer32
_StarSSULoadTotalConnections_Object = MibTableColumn
starSSULoadTotalConnections = _StarSSULoadTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 2),
    _StarSSULoadTotalConnections_Type()
)
starSSULoadTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadTotalConnections.setStatus("mandatory")
_StarSSULoadNumMcConnections_Type = Integer32
_StarSSULoadNumMcConnections_Object = MibTableColumn
starSSULoadNumMcConnections = _StarSSULoadNumMcConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 3),
    _StarSSULoadNumMcConnections_Type()
)
starSSULoadNumMcConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadNumMcConnections.setStatus("mandatory")
_StarSSULoadHighMarkVbrIn_Type = Integer32
_StarSSULoadHighMarkVbrIn_Object = MibTableColumn
starSSULoadHighMarkVbrIn = _StarSSULoadHighMarkVbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 4),
    _StarSSULoadHighMarkVbrIn_Type()
)
starSSULoadHighMarkVbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadHighMarkVbrIn.setStatus("mandatory")
_StarSSULoadTotalVbrIn_Type = Integer32
_StarSSULoadTotalVbrIn_Object = MibTableColumn
starSSULoadTotalVbrIn = _StarSSULoadTotalVbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 5),
    _StarSSULoadTotalVbrIn_Type()
)
starSSULoadTotalVbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadTotalVbrIn.setStatus("mandatory")
_StarSSULoadLowMarkVbrIn_Type = Integer32
_StarSSULoadLowMarkVbrIn_Object = MibTableColumn
starSSULoadLowMarkVbrIn = _StarSSULoadLowMarkVbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 6),
    _StarSSULoadLowMarkVbrIn_Type()
)
starSSULoadLowMarkVbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadLowMarkVbrIn.setStatus("mandatory")
_StarSSULoadHighMarkVbrOut_Type = Integer32
_StarSSULoadHighMarkVbrOut_Object = MibTableColumn
starSSULoadHighMarkVbrOut = _StarSSULoadHighMarkVbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 7),
    _StarSSULoadHighMarkVbrOut_Type()
)
starSSULoadHighMarkVbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadHighMarkVbrOut.setStatus("mandatory")
_StarSSULoadTotalVbrOut_Type = Integer32
_StarSSULoadTotalVbrOut_Object = MibTableColumn
starSSULoadTotalVbrOut = _StarSSULoadTotalVbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 8),
    _StarSSULoadTotalVbrOut_Type()
)
starSSULoadTotalVbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadTotalVbrOut.setStatus("mandatory")
_StarSSULoadLowMarkVbrOut_Type = Integer32
_StarSSULoadLowMarkVbrOut_Object = MibTableColumn
starSSULoadLowMarkVbrOut = _StarSSULoadLowMarkVbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 9),
    _StarSSULoadLowMarkVbrOut_Type()
)
starSSULoadLowMarkVbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadLowMarkVbrOut.setStatus("mandatory")
_StarSSULoadHighMarkFbrIn_Type = Integer32
_StarSSULoadHighMarkFbrIn_Object = MibTableColumn
starSSULoadHighMarkFbrIn = _StarSSULoadHighMarkFbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 10),
    _StarSSULoadHighMarkFbrIn_Type()
)
starSSULoadHighMarkFbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadHighMarkFbrIn.setStatus("mandatory")
_StarSSULoadTotalFbrIn_Type = Integer32
_StarSSULoadTotalFbrIn_Object = MibTableColumn
starSSULoadTotalFbrIn = _StarSSULoadTotalFbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 11),
    _StarSSULoadTotalFbrIn_Type()
)
starSSULoadTotalFbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadTotalFbrIn.setStatus("mandatory")
_StarSSULoadLowMarkFbrIn_Type = Integer32
_StarSSULoadLowMarkFbrIn_Object = MibTableColumn
starSSULoadLowMarkFbrIn = _StarSSULoadLowMarkFbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 12),
    _StarSSULoadLowMarkFbrIn_Type()
)
starSSULoadLowMarkFbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadLowMarkFbrIn.setStatus("mandatory")
_StarSSULoadHighMarkFbrOut_Type = Integer32
_StarSSULoadHighMarkFbrOut_Object = MibTableColumn
starSSULoadHighMarkFbrOut = _StarSSULoadHighMarkFbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 13),
    _StarSSULoadHighMarkFbrOut_Type()
)
starSSULoadHighMarkFbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadHighMarkFbrOut.setStatus("mandatory")
_StarSSULoadTotalFbrOut_Type = Integer32
_StarSSULoadTotalFbrOut_Object = MibTableColumn
starSSULoadTotalFbrOut = _StarSSULoadTotalFbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 14),
    _StarSSULoadTotalFbrOut_Type()
)
starSSULoadTotalFbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadTotalFbrOut.setStatus("mandatory")
_StarSSULoadLowMarkFbrOut_Type = Integer32
_StarSSULoadLowMarkFbrOut_Object = MibTableColumn
starSSULoadLowMarkFbrOut = _StarSSULoadLowMarkFbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 1, 1, 15),
    _StarSSULoadLowMarkFbrOut_Type()
)
starSSULoadLowMarkFbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULoadLowMarkFbrOut.setStatus("mandatory")
_StarSSUSiuLoadInfoTbl_Object = MibTable
starSSUSiuLoadInfoTbl = _StarSSUSiuLoadInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2)
)
if mibBuilder.loadTexts:
    starSSUSiuLoadInfoTbl.setStatus("mandatory")
_StarSSUSiuLoadInfoEntry_Object = MibTableRow
starSSUSiuLoadInfoEntry = _StarSSUSiuLoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2, 1)
)
starSSUSiuLoadInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIdSiuLoadInfo"),
    (0, "STARNE-MIB", "starSiuIdSiuLoadInfo"),
)
if mibBuilder.loadTexts:
    starSSUSiuLoadInfoEntry.setStatus("mandatory")
_StarSlotIdSiuLoadInfo_Type = Integer32
_StarSlotIdSiuLoadInfo_Object = MibTableColumn
starSlotIdSiuLoadInfo = _StarSlotIdSiuLoadInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2, 1, 1),
    _StarSlotIdSiuLoadInfo_Type()
)
starSlotIdSiuLoadInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotIdSiuLoadInfo.setStatus("mandatory")
_StarSiuIdSiuLoadInfo_Type = Integer32
_StarSiuIdSiuLoadInfo_Object = MibTableColumn
starSiuIdSiuLoadInfo = _StarSiuIdSiuLoadInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2, 1, 2),
    _StarSiuIdSiuLoadInfo_Type()
)
starSiuIdSiuLoadInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSiuIdSiuLoadInfo.setStatus("mandatory")
_StarSSUSiuTotalConnections_Type = Integer32
_StarSSUSiuTotalConnections_Object = MibTableColumn
starSSUSiuTotalConnections = _StarSSUSiuTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2, 1, 3),
    _StarSSUSiuTotalConnections_Type()
)
starSSUSiuTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuTotalConnections.setStatus("mandatory")
_StarSSUSiuNumMcConnections_Type = Integer32
_StarSSUSiuNumMcConnections_Object = MibTableColumn
starSSUSiuNumMcConnections = _StarSSUSiuNumMcConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2, 1, 4),
    _StarSSUSiuNumMcConnections_Type()
)
starSSUSiuNumMcConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuNumMcConnections.setStatus("mandatory")
_StarSSUSiuTotalVbrIn_Type = Integer32
_StarSSUSiuTotalVbrIn_Object = MibTableColumn
starSSUSiuTotalVbrIn = _StarSSUSiuTotalVbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2, 1, 5),
    _StarSSUSiuTotalVbrIn_Type()
)
starSSUSiuTotalVbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuTotalVbrIn.setStatus("mandatory")
_StarSSUSiuTotalVbrOut_Type = Integer32
_StarSSUSiuTotalVbrOut_Object = MibTableColumn
starSSUSiuTotalVbrOut = _StarSSUSiuTotalVbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2, 1, 6),
    _StarSSUSiuTotalVbrOut_Type()
)
starSSUSiuTotalVbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuTotalVbrOut.setStatus("mandatory")
_StarSSUSiuTotalFbrIn_Type = Integer32
_StarSSUSiuTotalFbrIn_Object = MibTableColumn
starSSUSiuTotalFbrIn = _StarSSUSiuTotalFbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2, 1, 7),
    _StarSSUSiuTotalFbrIn_Type()
)
starSSUSiuTotalFbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuTotalFbrIn.setStatus("mandatory")
_StarSSUSiuTotalFbrOut_Type = Integer32
_StarSSUSiuTotalFbrOut_Object = MibTableColumn
starSSUSiuTotalFbrOut = _StarSSUSiuTotalFbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 2, 1, 8),
    _StarSSUSiuTotalFbrOut_Type()
)
starSSUSiuTotalFbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuTotalFbrOut.setStatus("mandatory")
_StarSSUSiuPortLoadInfoTbl_Object = MibTable
starSSUSiuPortLoadInfoTbl = _StarSSUSiuPortLoadInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3)
)
if mibBuilder.loadTexts:
    starSSUSiuPortLoadInfoTbl.setStatus("mandatory")
_StarSSUSiuPortLoadInfoEntry_Object = MibTableRow
starSSUSiuPortLoadInfoEntry = _StarSSUSiuPortLoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1)
)
starSSUSiuPortLoadInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIdPortLoadInfo"),
    (0, "STARNE-MIB", "starSiuIdPortLoadInfo"),
    (0, "STARNE-MIB", "starSiuPortIdPortLoadInfo"),
)
if mibBuilder.loadTexts:
    starSSUSiuPortLoadInfoEntry.setStatus("mandatory")
_StarSlotIdPortLoadInfo_Type = Integer32
_StarSlotIdPortLoadInfo_Object = MibTableColumn
starSlotIdPortLoadInfo = _StarSlotIdPortLoadInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1, 1),
    _StarSlotIdPortLoadInfo_Type()
)
starSlotIdPortLoadInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotIdPortLoadInfo.setStatus("mandatory")
_StarSiuIdPortLoadInfo_Type = Integer32
_StarSiuIdPortLoadInfo_Object = MibTableColumn
starSiuIdPortLoadInfo = _StarSiuIdPortLoadInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1, 2),
    _StarSiuIdPortLoadInfo_Type()
)
starSiuIdPortLoadInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSiuIdPortLoadInfo.setStatus("mandatory")
_StarSiuPortIdPortLoadInfo_Type = Integer32
_StarSiuPortIdPortLoadInfo_Object = MibTableColumn
starSiuPortIdPortLoadInfo = _StarSiuPortIdPortLoadInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1, 3),
    _StarSiuPortIdPortLoadInfo_Type()
)
starSiuPortIdPortLoadInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSiuPortIdPortLoadInfo.setStatus("mandatory")
_StarSSUSiuPortTotalConnections_Type = Integer32
_StarSSUSiuPortTotalConnections_Object = MibTableColumn
starSSUSiuPortTotalConnections = _StarSSUSiuPortTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1, 4),
    _StarSSUSiuPortTotalConnections_Type()
)
starSSUSiuPortTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuPortTotalConnections.setStatus("mandatory")
_StarSSUSiuPortNumMcConnections_Type = Integer32
_StarSSUSiuPortNumMcConnections_Object = MibTableColumn
starSSUSiuPortNumMcConnections = _StarSSUSiuPortNumMcConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1, 5),
    _StarSSUSiuPortNumMcConnections_Type()
)
starSSUSiuPortNumMcConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuPortNumMcConnections.setStatus("mandatory")
_StarSSUSiuPortTotalVbrIn_Type = Integer32
_StarSSUSiuPortTotalVbrIn_Object = MibTableColumn
starSSUSiuPortTotalVbrIn = _StarSSUSiuPortTotalVbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1, 6),
    _StarSSUSiuPortTotalVbrIn_Type()
)
starSSUSiuPortTotalVbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuPortTotalVbrIn.setStatus("mandatory")
_StarSSUSiuPortTotalVbrOut_Type = Integer32
_StarSSUSiuPortTotalVbrOut_Object = MibTableColumn
starSSUSiuPortTotalVbrOut = _StarSSUSiuPortTotalVbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1, 7),
    _StarSSUSiuPortTotalVbrOut_Type()
)
starSSUSiuPortTotalVbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuPortTotalVbrOut.setStatus("mandatory")
_StarSSUSiuPortTotalFbrIn_Type = Integer32
_StarSSUSiuPortTotalFbrIn_Object = MibTableColumn
starSSUSiuPortTotalFbrIn = _StarSSUSiuPortTotalFbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1, 8),
    _StarSSUSiuPortTotalFbrIn_Type()
)
starSSUSiuPortTotalFbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuPortTotalFbrIn.setStatus("mandatory")
_StarSSUSiuPortTotalFbrOut_Type = Integer32
_StarSSUSiuPortTotalFbrOut_Object = MibTableColumn
starSSUSiuPortTotalFbrOut = _StarSSUSiuPortTotalFbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 3, 1, 9),
    _StarSSUSiuPortTotalFbrOut_Type()
)
starSSUSiuPortTotalFbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuPortTotalFbrOut.setStatus("mandatory")
_StarSSUConfigInfoTbl_Object = MibTable
starSSUConfigInfoTbl = _StarSSUConfigInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 4)
)
if mibBuilder.loadTexts:
    starSSUConfigInfoTbl.setStatus("mandatory")
_StarSSUConfigInfoEntry_Object = MibTableRow
starSSUConfigInfoEntry = _StarSSUConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 4, 1)
)
starSSUConfigInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSSUConfigInfoSlotId"),
)
if mibBuilder.loadTexts:
    starSSUConfigInfoEntry.setStatus("mandatory")
_StarSSUConfigInfoSlotId_Type = Integer32
_StarSSUConfigInfoSlotId_Object = MibTableColumn
starSSUConfigInfoSlotId = _StarSSUConfigInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 4, 1, 1),
    _StarSSUConfigInfoSlotId_Type()
)
starSSUConfigInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUConfigInfoSlotId.setStatus("mandatory")
_StarSSUSwitchLinkMaxCapacity_Type = Integer32
_StarSSUSwitchLinkMaxCapacity_Object = MibTableColumn
starSSUSwitchLinkMaxCapacity = _StarSSUSwitchLinkMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 4, 1, 2),
    _StarSSUSwitchLinkMaxCapacity_Type()
)
starSSUSwitchLinkMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSwitchLinkMaxCapacity.setStatus("mandatory")
_StarSSUSwitchLinkMaxVbr_Type = Integer32
_StarSSUSwitchLinkMaxVbr_Object = MibTableColumn
starSSUSwitchLinkMaxVbr = _StarSSUSwitchLinkMaxVbr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 4, 1, 3),
    _StarSSUSwitchLinkMaxVbr_Type()
)
starSSUSwitchLinkMaxVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSwitchLinkMaxVbr.setStatus("mandatory")
_StarSSUPercentVbrToLoad_Type = Integer32
_StarSSUPercentVbrToLoad_Object = MibTableColumn
starSSUPercentVbrToLoad = _StarSSUPercentVbrToLoad_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 4, 1, 4),
    _StarSSUPercentVbrToLoad_Type()
)
starSSUPercentVbrToLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUPercentVbrToLoad.setStatus("mandatory")
_StarSSUSiuInvalidationTimeout_Type = Integer32
_StarSSUSiuInvalidationTimeout_Object = MibTableColumn
starSSUSiuInvalidationTimeout = _StarSSUSiuInvalidationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 4, 1, 5),
    _StarSSUSiuInvalidationTimeout_Type()
)
starSSUSiuInvalidationTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUSiuInvalidationTimeout.setStatus("mandatory")
_StarSSUMulticastInfoTbl_Object = MibTable
starSSUMulticastInfoTbl = _StarSSUMulticastInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5)
)
if mibBuilder.loadTexts:
    starSSUMulticastInfoTbl.setStatus("mandatory")
_StarSSUMulticastInfoEntry_Object = MibTableRow
starSSUMulticastInfoEntry = _StarSSUMulticastInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1)
)
starSSUMulticastInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSSUMulticastSlotId"),
    (0, "STARNE-MIB", "starSSUMulticastGroup"),
)
if mibBuilder.loadTexts:
    starSSUMulticastInfoEntry.setStatus("mandatory")
_StarSSUMulticastSlotId_Type = Integer32
_StarSSUMulticastSlotId_Object = MibTableColumn
starSSUMulticastSlotId = _StarSSUMulticastSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1, 1),
    _StarSSUMulticastSlotId_Type()
)
starSSUMulticastSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUMulticastSlotId.setStatus("mandatory")
_StarSSUMulticastGroup_Type = Integer32
_StarSSUMulticastGroup_Object = MibTableColumn
starSSUMulticastGroup = _StarSSUMulticastGroup_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1, 2),
    _StarSSUMulticastGroup_Type()
)
starSSUMulticastGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUMulticastGroup.setStatus("mandatory")
_StarSSUNumberMcLeaves_Type = Integer32
_StarSSUNumberMcLeaves_Object = MibTableColumn
starSSUNumberMcLeaves = _StarSSUNumberMcLeaves_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1, 3),
    _StarSSUNumberMcLeaves_Type()
)
starSSUNumberMcLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUNumberMcLeaves.setStatus("mandatory")
_StarSSUMcSourceSiu_Type = Integer32
_StarSSUMcSourceSiu_Object = MibTableColumn
starSSUMcSourceSiu = _StarSSUMcSourceSiu_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1, 4),
    _StarSSUMcSourceSiu_Type()
)
starSSUMcSourceSiu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUMcSourceSiu.setStatus("mandatory")
_StarSSUMcSourcePort_Type = Integer32
_StarSSUMcSourcePort_Object = MibTableColumn
starSSUMcSourcePort = _StarSSUMcSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1, 5),
    _StarSSUMcSourcePort_Type()
)
starSSUMcSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUMcSourcePort.setStatus("mandatory")
_StarSSUMcInputFbr_Type = Integer32
_StarSSUMcInputFbr_Object = MibTableColumn
starSSUMcInputFbr = _StarSSUMcInputFbr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1, 6),
    _StarSSUMcInputFbr_Type()
)
starSSUMcInputFbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUMcInputFbr.setStatus("mandatory")
_StarSSUMcInputVbr_Type = Integer32
_StarSSUMcInputVbr_Object = MibTableColumn
starSSUMcInputVbr = _StarSSUMcInputVbr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1, 7),
    _StarSSUMcInputVbr_Type()
)
starSSUMcInputVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUMcInputVbr.setStatus("mandatory")
_StarSSUMcOutputFbr_Type = Integer32
_StarSSUMcOutputFbr_Object = MibTableColumn
starSSUMcOutputFbr = _StarSSUMcOutputFbr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1, 8),
    _StarSSUMcOutputFbr_Type()
)
starSSUMcOutputFbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUMcOutputFbr.setStatus("mandatory")
_StarSSUMcOutputVbr_Type = Integer32
_StarSSUMcOutputVbr_Object = MibTableColumn
starSSUMcOutputVbr = _StarSSUMcOutputVbr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 5, 1, 9),
    _StarSSUMcOutputVbr_Type()
)
starSSUMcOutputVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUMcOutputVbr.setStatus("mandatory")
_StarSSULinkConfigInfoTbl_Object = MibTable
starSSULinkConfigInfoTbl = _StarSSULinkConfigInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 6)
)
if mibBuilder.loadTexts:
    starSSULinkConfigInfoTbl.setStatus("mandatory")
_StarSSULinkConfigInfoEntry_Object = MibTableRow
starSSULinkConfigInfoEntry = _StarSSULinkConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 6, 1)
)
starSSULinkConfigInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSSULinkConfigSlotId"),
    (0, "STARNE-MIB", "starSSULinkConfigSwitchLevel"),
    (0, "STARNE-MIB", "starSSUConfigSwitchLink"),
)
if mibBuilder.loadTexts:
    starSSULinkConfigInfoEntry.setStatus("mandatory")
_StarSSULinkConfigSlotId_Type = Integer32
_StarSSULinkConfigSlotId_Object = MibTableColumn
starSSULinkConfigSlotId = _StarSSULinkConfigSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 6, 1, 1),
    _StarSSULinkConfigSlotId_Type()
)
starSSULinkConfigSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULinkConfigSlotId.setStatus("mandatory")
_StarSSULinkConfigSwitchLevel_Type = Integer32
_StarSSULinkConfigSwitchLevel_Object = MibTableColumn
starSSULinkConfigSwitchLevel = _StarSSULinkConfigSwitchLevel_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 6, 1, 2),
    _StarSSULinkConfigSwitchLevel_Type()
)
starSSULinkConfigSwitchLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSULinkConfigSwitchLevel.setStatus("mandatory")
_StarSSUConfigSwitchLink_Type = Integer32
_StarSSUConfigSwitchLink_Object = MibTableColumn
starSSUConfigSwitchLink = _StarSSUConfigSwitchLink_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 6, 1, 3),
    _StarSSUConfigSwitchLink_Type()
)
starSSUConfigSwitchLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUConfigSwitchLink.setStatus("mandatory")
_StarSSULinkMaxCapacity_Type = Integer32
_StarSSULinkMaxCapacity_Object = MibTableColumn
starSSULinkMaxCapacity = _StarSSULinkMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 6, 1, 4),
    _StarSSULinkMaxCapacity_Type()
)
starSSULinkMaxCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSULinkMaxCapacity.setStatus("mandatory")
_StarSSULinkMaxVbr_Type = Integer32
_StarSSULinkMaxVbr_Object = MibTableColumn
starSSULinkMaxVbr = _StarSSULinkMaxVbr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 6, 1, 5),
    _StarSSULinkMaxVbr_Type()
)
starSSULinkMaxVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSULinkMaxVbr.setStatus("mandatory")
_StarSSUPmThresholdInfoTbl_Object = MibTable
starSSUPmThresholdInfoTbl = _StarSSUPmThresholdInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7)
)
if mibBuilder.loadTexts:
    starSSUPmThresholdInfoTbl.setStatus("mandatory")
_StarSSUPmThresholdInfoEntry_Object = MibTableRow
starSSUPmThresholdInfoEntry = _StarSSUPmThresholdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1)
)
starSSUPmThresholdInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSSUPmThresholdSlotId"),
)
if mibBuilder.loadTexts:
    starSSUPmThresholdInfoEntry.setStatus("mandatory")
_StarSSUPmThresholdSlotId_Type = Integer32
_StarSSUPmThresholdSlotId_Object = MibTableColumn
starSSUPmThresholdSlotId = _StarSSUPmThresholdSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1, 1),
    _StarSSUPmThresholdSlotId_Type()
)
starSSUPmThresholdSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSSUPmThresholdSlotId.setStatus("mandatory")
_StarSSUSwitchMcGroupThreshold_Type = Integer32
_StarSSUSwitchMcGroupThreshold_Object = MibTableColumn
starSSUSwitchMcGroupThreshold = _StarSSUSwitchMcGroupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1, 2),
    _StarSSUSwitchMcGroupThreshold_Type()
)
starSSUSwitchMcGroupThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSUSwitchMcGroupThreshold.setStatus("mandatory")
_StarSSUSwitchMcBitsPerMcgThreshold_Type = Integer32
_StarSSUSwitchMcBitsPerMcgThreshold_Object = MibTableColumn
starSSUSwitchMcBitsPerMcgThreshold = _StarSSUSwitchMcBitsPerMcgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1, 3),
    _StarSSUSwitchMcBitsPerMcgThreshold_Type()
)
starSSUSwitchMcBitsPerMcgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSUSwitchMcBitsPerMcgThreshold.setStatus("mandatory")
_StarSSUSwitchTotalMcBitsThreshold_Type = Integer32
_StarSSUSwitchTotalMcBitsThreshold_Object = MibTableColumn
starSSUSwitchTotalMcBitsThreshold = _StarSSUSwitchTotalMcBitsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1, 4),
    _StarSSUSwitchTotalMcBitsThreshold_Type()
)
starSSUSwitchTotalMcBitsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSUSwitchTotalMcBitsThreshold.setStatus("mandatory")
_StarSSUCrsrReqFailedThreshold_Type = Integer32
_StarSSUCrsrReqFailedThreshold_Object = MibTableColumn
starSSUCrsrReqFailedThreshold = _StarSSUCrsrReqFailedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1, 5),
    _StarSSUCrsrReqFailedThreshold_Type()
)
starSSUCrsrReqFailedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSUCrsrReqFailedThreshold.setStatus("mandatory")
_StarSSUCrsrReqNumThreshold_Type = Integer32
_StarSSUCrsrReqNumThreshold_Object = MibTableColumn
starSSUCrsrReqNumThreshold = _StarSSUCrsrReqNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1, 6),
    _StarSSUCrsrReqNumThreshold_Type()
)
starSSUCrsrReqNumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSUCrsrReqNumThreshold.setStatus("mandatory")
_StarSSUCrsrReqFailedMcgExceededThreshold_Type = Integer32
_StarSSUCrsrReqFailedMcgExceededThreshold_Object = MibTableColumn
starSSUCrsrReqFailedMcgExceededThreshold = _StarSSUCrsrReqFailedMcgExceededThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1, 7),
    _StarSSUCrsrReqFailedMcgExceededThreshold_Type()
)
starSSUCrsrReqFailedMcgExceededThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSUCrsrReqFailedMcgExceededThreshold.setStatus("mandatory")
_StarSSUCrsrReconcileFailThreshold_Type = Integer32
_StarSSUCrsrReconcileFailThreshold_Object = MibTableColumn
starSSUCrsrReconcileFailThreshold = _StarSSUCrsrReconcileFailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1, 8),
    _StarSSUCrsrReconcileFailThreshold_Type()
)
starSSUCrsrReconcileFailThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSUCrsrReconcileFailThreshold.setStatus("mandatory")
_StarSSUSiuLoadCapacityThreshold_Type = Integer32
_StarSSUSiuLoadCapacityThreshold_Object = MibTableColumn
starSSUSiuLoadCapacityThreshold = _StarSSUSiuLoadCapacityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 4, 7, 1, 9),
    _StarSSUSiuLoadCapacityThreshold_Type()
)
starSSUSiuLoadCapacityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starSSUSiuLoadCapacityThreshold.setStatus("mandatory")
_StarSysClockInfo_ObjectIdentity = ObjectIdentity
starSysClockInfo = _StarSysClockInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5)
)
_StarSysClockTbl_Object = MibTable
starSysClockTbl = _StarSysClockTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1)
)
if mibBuilder.loadTexts:
    starSysClockTbl.setStatus("mandatory")
_StarSysClockInfoEntry_Object = MibTableRow
starSysClockInfoEntry = _StarSysClockInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1)
)
starSysClockInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starScuInfoSlotId"),
)
if mibBuilder.loadTexts:
    starSysClockInfoEntry.setStatus("mandatory")
_StarScuInfoSlotId_Type = Integer32
_StarScuInfoSlotId_Object = MibTableColumn
starScuInfoSlotId = _StarScuInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1, 1),
    _StarScuInfoSlotId_Type()
)
starScuInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starScuInfoSlotId.setStatus("mandatory")


class _StarClkSource_Type(Integer32):
    """Custom type starClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bits", 1),
          ("extline", 2),
          ("freerun", 4),
          ("holdover", 3),
          ("init", 0))
    )


_StarClkSource_Type.__name__ = "Integer32"
_StarClkSource_Object = MibTableColumn
starClkSource = _StarClkSource_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1, 2),
    _StarClkSource_Type()
)
starClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starClkSource.setStatus("mandatory")


class _StarClkPrevSource_Type(Integer32):
    """Custom type starClkPrevSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bits", 1),
          ("extline", 2),
          ("freerun", 4),
          ("holdover", 3),
          ("init", 0))
    )


_StarClkPrevSource_Type.__name__ = "Integer32"
_StarClkPrevSource_Object = MibTableColumn
starClkPrevSource = _StarClkPrevSource_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1, 3),
    _StarClkPrevSource_Type()
)
starClkPrevSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkPrevSource.setStatus("mandatory")
_StarClkSourceLine_Type = Integer32
_StarClkSourceLine_Object = MibTableColumn
starClkSourceLine = _StarClkSourceLine_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1, 4),
    _StarClkSourceLine_Type()
)
starClkSourceLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starClkSourceLine.setStatus("mandatory")
_StarClkPrevSourceLine_Type = Integer32
_StarClkPrevSourceLine_Object = MibTableColumn
starClkPrevSourceLine = _StarClkPrevSourceLine_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1, 5),
    _StarClkPrevSourceLine_Type()
)
starClkPrevSourceLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkPrevSourceLine.setStatus("mandatory")


class _StarClkStatus_Type(Integer32):
    """Custom type starClkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1))
    )


_StarClkStatus_Type.__name__ = "Integer32"
_StarClkStatus_Object = MibTableColumn
starClkStatus = _StarClkStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1, 6),
    _StarClkStatus_Type()
)
starClkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkStatus.setStatus("mandatory")


class _StarClkPLLMode_Type(Integer32):
    """Custom type starClkPLLMode based on Integer32"""
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
        *(("fast", 1),
          ("freerun", 5),
          ("holdover", 4),
          ("mid", 2),
          ("normal", 3))
    )


_StarClkPLLMode_Type.__name__ = "Integer32"
_StarClkPLLMode_Object = MibTableColumn
starClkPLLMode = _StarClkPLLMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1, 7),
    _StarClkPLLMode_Type()
)
starClkPLLMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkPLLMode.setStatus("mandatory")


class _StarClkMasterStatus_Type(Integer32):
    """Custom type starClkMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_StarClkMasterStatus_Type.__name__ = "Integer32"
_StarClkMasterStatus_Object = MibTableColumn
starClkMasterStatus = _StarClkMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1, 8),
    _StarClkMasterStatus_Type()
)
starClkMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkMasterStatus.setStatus("mandatory")
_StarClkPriority_Type = Integer32
_StarClkPriority_Object = MibTableColumn
starClkPriority = _StarClkPriority_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 1, 1, 9),
    _StarClkPriority_Type()
)
starClkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkPriority.setStatus("mandatory")
_StarClkCurStatusLineTbl_Object = MibTable
starClkCurStatusLineTbl = _StarClkCurStatusLineTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2)
)
if mibBuilder.loadTexts:
    starClkCurStatusLineTbl.setStatus("mandatory")
_StarClkCurStatusLineEntry_Object = MibTableRow
starClkCurStatusLineEntry = _StarClkCurStatusLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1)
)
starClkCurStatusLineEntry.setIndexNames(
    (0, "STARNE-MIB", "starClkStatusSlotId"),
)
if mibBuilder.loadTexts:
    starClkCurStatusLineEntry.setStatus("mandatory")
_StarClkStatusSlotId_Type = Integer32
_StarClkStatusSlotId_Object = MibTableColumn
starClkStatusSlotId = _StarClkStatusSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 1),
    _StarClkStatusSlotId_Type()
)
starClkStatusSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkStatusSlotId.setStatus("mandatory")


class _StarClkCurStatusSiu1_Type(Integer32):
    """Custom type starClkCurStatusSiu1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("notready", 3))
    )


_StarClkCurStatusSiu1_Type.__name__ = "Integer32"
_StarClkCurStatusSiu1_Object = MibTableColumn
starClkCurStatusSiu1 = _StarClkCurStatusSiu1_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 2),
    _StarClkCurStatusSiu1_Type()
)
starClkCurStatusSiu1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkCurStatusSiu1.setStatus("mandatory")


class _StarClkCurStatusSiu2_Type(Integer32):
    """Custom type starClkCurStatusSiu2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("notready", 3))
    )


_StarClkCurStatusSiu2_Type.__name__ = "Integer32"
_StarClkCurStatusSiu2_Object = MibTableColumn
starClkCurStatusSiu2 = _StarClkCurStatusSiu2_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 3),
    _StarClkCurStatusSiu2_Type()
)
starClkCurStatusSiu2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkCurStatusSiu2.setStatus("mandatory")


class _StarClkCurStatusSiu3_Type(Integer32):
    """Custom type starClkCurStatusSiu3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("notready", 3))
    )


_StarClkCurStatusSiu3_Type.__name__ = "Integer32"
_StarClkCurStatusSiu3_Object = MibTableColumn
starClkCurStatusSiu3 = _StarClkCurStatusSiu3_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 4),
    _StarClkCurStatusSiu3_Type()
)
starClkCurStatusSiu3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkCurStatusSiu3.setStatus("mandatory")


class _StarClkCurStatusSiu4_Type(Integer32):
    """Custom type starClkCurStatusSiu4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("notready", 3))
    )


_StarClkCurStatusSiu4_Type.__name__ = "Integer32"
_StarClkCurStatusSiu4_Object = MibTableColumn
starClkCurStatusSiu4 = _StarClkCurStatusSiu4_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 5),
    _StarClkCurStatusSiu4_Type()
)
starClkCurStatusSiu4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkCurStatusSiu4.setStatus("mandatory")


class _StarClkCurStatusSiu5_Type(Integer32):
    """Custom type starClkCurStatusSiu5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("notready", 3))
    )


_StarClkCurStatusSiu5_Type.__name__ = "Integer32"
_StarClkCurStatusSiu5_Object = MibTableColumn
starClkCurStatusSiu5 = _StarClkCurStatusSiu5_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 6),
    _StarClkCurStatusSiu5_Type()
)
starClkCurStatusSiu5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkCurStatusSiu5.setStatus("mandatory")


class _StarClkCurStatusSiu6_Type(Integer32):
    """Custom type starClkCurStatusSiu6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("notready", 3))
    )


_StarClkCurStatusSiu6_Type.__name__ = "Integer32"
_StarClkCurStatusSiu6_Object = MibTableColumn
starClkCurStatusSiu6 = _StarClkCurStatusSiu6_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 7),
    _StarClkCurStatusSiu6_Type()
)
starClkCurStatusSiu6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkCurStatusSiu6.setStatus("mandatory")


class _StarClkCurStatusSiu7_Type(Integer32):
    """Custom type starClkCurStatusSiu7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("notready", 3))
    )


_StarClkCurStatusSiu7_Type.__name__ = "Integer32"
_StarClkCurStatusSiu7_Object = MibTableColumn
starClkCurStatusSiu7 = _StarClkCurStatusSiu7_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 8),
    _StarClkCurStatusSiu7_Type()
)
starClkCurStatusSiu7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkCurStatusSiu7.setStatus("mandatory")


class _StarClkCurStatusSiu8_Type(Integer32):
    """Custom type starClkCurStatusSiu8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("notready", 3))
    )


_StarClkCurStatusSiu8_Type.__name__ = "Integer32"
_StarClkCurStatusSiu8_Object = MibTableColumn
starClkCurStatusSiu8 = _StarClkCurStatusSiu8_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 9),
    _StarClkCurStatusSiu8_Type()
)
starClkCurStatusSiu8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkCurStatusSiu8.setStatus("mandatory")


class _StarClkCurStatusSiu9_Type(Integer32):
    """Custom type starClkCurStatusSiu9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("notready", 3))
    )


_StarClkCurStatusSiu9_Type.__name__ = "Integer32"
_StarClkCurStatusSiu9_Object = MibTableColumn
starClkCurStatusSiu9 = _StarClkCurStatusSiu9_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 2, 1, 10),
    _StarClkCurStatusSiu9_Type()
)
starClkCurStatusSiu9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkCurStatusSiu9.setStatus("mandatory")
_StarClkDistribStatusTbl_Object = MibTable
starClkDistribStatusTbl = _StarClkDistribStatusTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3)
)
if mibBuilder.loadTexts:
    starClkDistribStatusTbl.setStatus("mandatory")
_StarClkDistribStatusEntry_Object = MibTableRow
starClkDistribStatusEntry = _StarClkDistribStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1)
)
starClkDistribStatusEntry.setIndexNames(
    (0, "STARNE-MIB", "starClkDistribSlotId"),
)
if mibBuilder.loadTexts:
    starClkDistribStatusEntry.setStatus("mandatory")
_StarClkDistribSlotId_Type = Integer32
_StarClkDistribSlotId_Object = MibTableColumn
starClkDistribSlotId = _StarClkDistribSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 1),
    _StarClkDistribSlotId_Type()
)
starClkDistribSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribSlotId.setStatus("mandatory")


class _StarClkDistribStatusSiu1_Type(Integer32):
    """Custom type starClkDistribStatusSiu1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKHZ", 1),
          ("nintennMHZ", 2))
    )


_StarClkDistribStatusSiu1_Type.__name__ = "Integer32"
_StarClkDistribStatusSiu1_Object = MibTableColumn
starClkDistribStatusSiu1 = _StarClkDistribStatusSiu1_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 2),
    _StarClkDistribStatusSiu1_Type()
)
starClkDistribStatusSiu1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribStatusSiu1.setStatus("mandatory")


class _StarClkDistribStatusSiu2_Type(Integer32):
    """Custom type starClkDistribStatusSiu2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKHZ", 1),
          ("nintennMHZ", 2))
    )


_StarClkDistribStatusSiu2_Type.__name__ = "Integer32"
_StarClkDistribStatusSiu2_Object = MibTableColumn
starClkDistribStatusSiu2 = _StarClkDistribStatusSiu2_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 3),
    _StarClkDistribStatusSiu2_Type()
)
starClkDistribStatusSiu2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribStatusSiu2.setStatus("mandatory")


class _StarClkDistribStatusSiu3_Type(Integer32):
    """Custom type starClkDistribStatusSiu3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKHZ", 1),
          ("nintennMHZ", 2))
    )


_StarClkDistribStatusSiu3_Type.__name__ = "Integer32"
_StarClkDistribStatusSiu3_Object = MibTableColumn
starClkDistribStatusSiu3 = _StarClkDistribStatusSiu3_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 4),
    _StarClkDistribStatusSiu3_Type()
)
starClkDistribStatusSiu3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribStatusSiu3.setStatus("mandatory")


class _StarClkDistribStatusSiu4_Type(Integer32):
    """Custom type starClkDistribStatusSiu4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKHZ", 1),
          ("nintennMHZ", 2))
    )


_StarClkDistribStatusSiu4_Type.__name__ = "Integer32"
_StarClkDistribStatusSiu4_Object = MibTableColumn
starClkDistribStatusSiu4 = _StarClkDistribStatusSiu4_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 5),
    _StarClkDistribStatusSiu4_Type()
)
starClkDistribStatusSiu4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribStatusSiu4.setStatus("mandatory")


class _StarClkDistribStatusSiu5_Type(Integer32):
    """Custom type starClkDistribStatusSiu5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKHZ", 1),
          ("nintennMHZ", 2))
    )


_StarClkDistribStatusSiu5_Type.__name__ = "Integer32"
_StarClkDistribStatusSiu5_Object = MibTableColumn
starClkDistribStatusSiu5 = _StarClkDistribStatusSiu5_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 6),
    _StarClkDistribStatusSiu5_Type()
)
starClkDistribStatusSiu5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribStatusSiu5.setStatus("mandatory")


class _StarClkDistribStatusSiu6_Type(Integer32):
    """Custom type starClkDistribStatusSiu6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKHZ", 1),
          ("nintennMHZ", 2))
    )


_StarClkDistribStatusSiu6_Type.__name__ = "Integer32"
_StarClkDistribStatusSiu6_Object = MibTableColumn
starClkDistribStatusSiu6 = _StarClkDistribStatusSiu6_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 7),
    _StarClkDistribStatusSiu6_Type()
)
starClkDistribStatusSiu6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribStatusSiu6.setStatus("mandatory")


class _StarClkDistribStatusSiu7_Type(Integer32):
    """Custom type starClkDistribStatusSiu7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKHZ", 1),
          ("nintennMHZ", 2))
    )


_StarClkDistribStatusSiu7_Type.__name__ = "Integer32"
_StarClkDistribStatusSiu7_Object = MibTableColumn
starClkDistribStatusSiu7 = _StarClkDistribStatusSiu7_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 8),
    _StarClkDistribStatusSiu7_Type()
)
starClkDistribStatusSiu7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribStatusSiu7.setStatus("mandatory")


class _StarClkDistribStatusSiu8_Type(Integer32):
    """Custom type starClkDistribStatusSiu8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKHZ", 1),
          ("nintennMHZ", 2))
    )


_StarClkDistribStatusSiu8_Type.__name__ = "Integer32"
_StarClkDistribStatusSiu8_Object = MibTableColumn
starClkDistribStatusSiu8 = _StarClkDistribStatusSiu8_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 9),
    _StarClkDistribStatusSiu8_Type()
)
starClkDistribStatusSiu8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribStatusSiu8.setStatus("mandatory")


class _StarClkDistribStatusSiu9_Type(Integer32):
    """Custom type starClkDistribStatusSiu9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightKHZ", 1),
          ("nintennMHZ", 2))
    )


_StarClkDistribStatusSiu9_Type.__name__ = "Integer32"
_StarClkDistribStatusSiu9_Object = MibTableColumn
starClkDistribStatusSiu9 = _StarClkDistribStatusSiu9_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 5, 3, 1, 10),
    _StarClkDistribStatusSiu9_Type()
)
starClkDistribStatusSiu9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starClkDistribStatusSiu9.setStatus("mandatory")
_StarSwitch88Info_ObjectIdentity = ObjectIdentity
starSwitch88Info = _StarSwitch88Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6)
)
_StarSwitchInfoTbl_Object = MibTable
starSwitchInfoTbl = _StarSwitchInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1)
)
if mibBuilder.loadTexts:
    starSwitchInfoTbl.setStatus("mandatory")
_StarSwitchInfoEntry_Object = MibTableRow
starSwitchInfoEntry = _StarSwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1)
)
starSwitchInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSwitchInfoSlotId"),
    (0, "STARNE-MIB", "starSwitchFabricRow"),
    (0, "STARNE-MIB", "starSwitchFabricColumn"),
)
if mibBuilder.loadTexts:
    starSwitchInfoEntry.setStatus("mandatory")
_StarSwitchInfoSlotId_Type = Integer32
_StarSwitchInfoSlotId_Object = MibTableColumn
starSwitchInfoSlotId = _StarSwitchInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 1),
    _StarSwitchInfoSlotId_Type()
)
starSwitchInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchInfoSlotId.setStatus("mandatory")
_StarSwitchFabricRow_Type = Integer32
_StarSwitchFabricRow_Object = MibTableColumn
starSwitchFabricRow = _StarSwitchFabricRow_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 2),
    _StarSwitchFabricRow_Type()
)
starSwitchFabricRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchFabricRow.setStatus("mandatory")
_StarSwitchFabricColumn_Type = Integer32
_StarSwitchFabricColumn_Object = MibTableColumn
starSwitchFabricColumn = _StarSwitchFabricColumn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 3),
    _StarSwitchFabricColumn_Type()
)
starSwitchFabricColumn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchFabricColumn.setStatus("mandatory")


class _StarSwitchCurrentState_Type(Integer32):
    """Custom type starSwitchCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("operational", 2))
    )


_StarSwitchCurrentState_Type.__name__ = "Integer32"
_StarSwitchCurrentState_Object = MibTableColumn
starSwitchCurrentState = _StarSwitchCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 4),
    _StarSwitchCurrentState_Type()
)
starSwitchCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchCurrentState.setStatus("mandatory")
_StarSwitchChipVersion_Type = Integer32
_StarSwitchChipVersion_Object = MibTableColumn
starSwitchChipVersion = _StarSwitchChipVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 5),
    _StarSwitchChipVersion_Type()
)
starSwitchChipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchChipVersion.setStatus("mandatory")
_StarSwitchFabricLevel_Type = Integer32
_StarSwitchFabricLevel_Object = MibTableColumn
starSwitchFabricLevel = _StarSwitchFabricLevel_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 6),
    _StarSwitchFabricLevel_Type()
)
starSwitchFabricLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchFabricLevel.setStatus("mandatory")


class _StarSwitchBckPressureDly_Type(Integer32):
    """Custom type starSwitchBckPressureDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clk2Delay", 2),
          ("clk4Delay", 3),
          ("noDelay", 1))
    )


_StarSwitchBckPressureDly_Type.__name__ = "Integer32"
_StarSwitchBckPressureDly_Object = MibTableColumn
starSwitchBckPressureDly = _StarSwitchBckPressureDly_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 7),
    _StarSwitchBckPressureDly_Type()
)
starSwitchBckPressureDly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchBckPressureDly.setStatus("mandatory")
_StarSwitchAggrIp_Type = Integer32
_StarSwitchAggrIp_Object = MibTableColumn
starSwitchAggrIp = _StarSwitchAggrIp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 8),
    _StarSwitchAggrIp_Type()
)
starSwitchAggrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchAggrIp.setStatus("mandatory")
_StarSwitchAggrOp_Type = Integer32
_StarSwitchAggrOp_Object = MibTableColumn
starSwitchAggrOp = _StarSwitchAggrOp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 9),
    _StarSwitchAggrOp_Type()
)
starSwitchAggrOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchAggrOp.setStatus("mandatory")
_StarSwitchStrictPriority_Type = Integer32
_StarSwitchStrictPriority_Object = MibTableColumn
starSwitchStrictPriority = _StarSwitchStrictPriority_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 10),
    _StarSwitchStrictPriority_Type()
)
starSwitchStrictPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchStrictPriority.setStatus("mandatory")
_StarSwitchInMarkedCellCnt_Type = Counter32
_StarSwitchInMarkedCellCnt_Object = MibTableColumn
starSwitchInMarkedCellCnt = _StarSwitchInMarkedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 11),
    _StarSwitchInMarkedCellCnt_Type()
)
starSwitchInMarkedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchInMarkedCellCnt.setStatus("mandatory")
_StarSwitchOutMarkedCellCnt_Type = Counter32
_StarSwitchOutMarkedCellCnt_Object = MibTableColumn
starSwitchOutMarkedCellCnt = _StarSwitchOutMarkedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 12),
    _StarSwitchOutMarkedCellCnt_Type()
)
starSwitchOutMarkedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchOutMarkedCellCnt.setStatus("mandatory")
_StarSwitchRatioAOrder1_Type = Integer32
_StarSwitchRatioAOrder1_Object = MibTableColumn
starSwitchRatioAOrder1 = _StarSwitchRatioAOrder1_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 13),
    _StarSwitchRatioAOrder1_Type()
)
starSwitchRatioAOrder1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchRatioAOrder1.setStatus("mandatory")
_StarSwitchRatioAOrder2_Type = Integer32
_StarSwitchRatioAOrder2_Object = MibTableColumn
starSwitchRatioAOrder2 = _StarSwitchRatioAOrder2_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 14),
    _StarSwitchRatioAOrder2_Type()
)
starSwitchRatioAOrder2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchRatioAOrder2.setStatus("mandatory")
_StarSwitchRatioBOrder1_Type = Integer32
_StarSwitchRatioBOrder1_Object = MibTableColumn
starSwitchRatioBOrder1 = _StarSwitchRatioBOrder1_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 15),
    _StarSwitchRatioBOrder1_Type()
)
starSwitchRatioBOrder1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchRatioBOrder1.setStatus("mandatory")
_StarSwitchRatioBOrder2_Type = Integer32
_StarSwitchRatioBOrder2_Object = MibTableColumn
starSwitchRatioBOrder2 = _StarSwitchRatioBOrder2_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 1, 1, 16),
    _StarSwitchRatioBOrder2_Type()
)
starSwitchRatioBOrder2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchRatioBOrder2.setStatus("mandatory")
_StarSwitchMulticastInfoTbl_Object = MibTable
starSwitchMulticastInfoTbl = _StarSwitchMulticastInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 2)
)
if mibBuilder.loadTexts:
    starSwitchMulticastInfoTbl.setStatus("mandatory")
_StarSwitchMulticastInfoEntry_Object = MibTableRow
starSwitchMulticastInfoEntry = _StarSwitchMulticastInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 2, 1)
)
starSwitchMulticastInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIdSwitchMcInfo"),
    (0, "STARNE-MIB", "starMcSwitchFabricRow"),
    (0, "STARNE-MIB", "starMcSwitchFabricColumn"),
    (0, "STARNE-MIB", "starSwitchMulticastNo"),
)
if mibBuilder.loadTexts:
    starSwitchMulticastInfoEntry.setStatus("mandatory")
_StarSlotIdSwitchMcInfo_Type = Integer32
_StarSlotIdSwitchMcInfo_Object = MibTableColumn
starSlotIdSwitchMcInfo = _StarSlotIdSwitchMcInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 2, 1, 1),
    _StarSlotIdSwitchMcInfo_Type()
)
starSlotIdSwitchMcInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotIdSwitchMcInfo.setStatus("mandatory")
_StarMcSwitchFabricRow_Type = Integer32
_StarMcSwitchFabricRow_Object = MibTableColumn
starMcSwitchFabricRow = _StarMcSwitchFabricRow_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 2, 1, 2),
    _StarMcSwitchFabricRow_Type()
)
starMcSwitchFabricRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starMcSwitchFabricRow.setStatus("mandatory")
_StarMcSwitchFabricColumn_Type = Integer32
_StarMcSwitchFabricColumn_Object = MibTableColumn
starMcSwitchFabricColumn = _StarMcSwitchFabricColumn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 2, 1, 3),
    _StarMcSwitchFabricColumn_Type()
)
starMcSwitchFabricColumn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starMcSwitchFabricColumn.setStatus("mandatory")
_StarSwitchMulticastNo_Type = Integer32
_StarSwitchMulticastNo_Object = MibTableColumn
starSwitchMulticastNo = _StarSwitchMulticastNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 2, 1, 4),
    _StarSwitchMulticastNo_Type()
)
starSwitchMulticastNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchMulticastNo.setStatus("mandatory")
_StarSwitchMulticastPorts_Type = Integer32
_StarSwitchMulticastPorts_Object = MibTableColumn
starSwitchMulticastPorts = _StarSwitchMulticastPorts_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 2, 1, 5),
    _StarSwitchMulticastPorts_Type()
)
starSwitchMulticastPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchMulticastPorts.setStatus("mandatory")
_StarSwitchLinkLoadTbl_Object = MibTable
starSwitchLinkLoadTbl = _StarSwitchLinkLoadTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3)
)
if mibBuilder.loadTexts:
    starSwitchLinkLoadTbl.setStatus("mandatory")
_StarSwitchLinkLoadEntry_Object = MibTableRow
starSwitchLinkLoadEntry = _StarSwitchLinkLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3, 1)
)
starSwitchLinkLoadEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIdSwitchLoadInfo"),
    (0, "STARNE-MIB", "starLinkLoadSwitchFabricRow"),
    (0, "STARNE-MIB", "starLinkLoadSwitchFabricColumn"),
    (0, "STARNE-MIB", "starSwitchLinkId"),
)
if mibBuilder.loadTexts:
    starSwitchLinkLoadEntry.setStatus("mandatory")
_StarSlotIdSwitchLoadInfo_Type = Integer32
_StarSlotIdSwitchLoadInfo_Object = MibTableColumn
starSlotIdSwitchLoadInfo = _StarSlotIdSwitchLoadInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3, 1, 1),
    _StarSlotIdSwitchLoadInfo_Type()
)
starSlotIdSwitchLoadInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotIdSwitchLoadInfo.setStatus("mandatory")
_StarLinkLoadSwitchFabricRow_Type = Integer32
_StarLinkLoadSwitchFabricRow_Object = MibTableColumn
starLinkLoadSwitchFabricRow = _StarLinkLoadSwitchFabricRow_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3, 1, 2),
    _StarLinkLoadSwitchFabricRow_Type()
)
starLinkLoadSwitchFabricRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLinkLoadSwitchFabricRow.setStatus("mandatory")
_StarLinkLoadSwitchFabricColumn_Type = Integer32
_StarLinkLoadSwitchFabricColumn_Object = MibTableColumn
starLinkLoadSwitchFabricColumn = _StarLinkLoadSwitchFabricColumn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3, 1, 3),
    _StarLinkLoadSwitchFabricColumn_Type()
)
starLinkLoadSwitchFabricColumn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLinkLoadSwitchFabricColumn.setStatus("mandatory")
_StarSwitchLinkId_Type = Integer32
_StarSwitchLinkId_Object = MibTableColumn
starSwitchLinkId = _StarSwitchLinkId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3, 1, 4),
    _StarSwitchLinkId_Type()
)
starSwitchLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchLinkId.setStatus("mandatory")
_StarSwitchLinkVbrIn_Type = Integer32
_StarSwitchLinkVbrIn_Object = MibTableColumn
starSwitchLinkVbrIn = _StarSwitchLinkVbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3, 1, 5),
    _StarSwitchLinkVbrIn_Type()
)
starSwitchLinkVbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchLinkVbrIn.setStatus("mandatory")
_StarSwitchLinkVbrOut_Type = Integer32
_StarSwitchLinkVbrOut_Object = MibTableColumn
starSwitchLinkVbrOut = _StarSwitchLinkVbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3, 1, 6),
    _StarSwitchLinkVbrOut_Type()
)
starSwitchLinkVbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchLinkVbrOut.setStatus("mandatory")
_StarSwitchLinkFbrIn_Type = Integer32
_StarSwitchLinkFbrIn_Object = MibTableColumn
starSwitchLinkFbrIn = _StarSwitchLinkFbrIn_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3, 1, 7),
    _StarSwitchLinkFbrIn_Type()
)
starSwitchLinkFbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchLinkFbrIn.setStatus("mandatory")
_StarSwitchLinkFbrOut_Type = Integer32
_StarSwitchLinkFbrOut_Object = MibTableColumn
starSwitchLinkFbrOut = _StarSwitchLinkFbrOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 6, 3, 1, 8),
    _StarSwitchLinkFbrOut_Type()
)
starSwitchLinkFbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchLinkFbrOut.setStatus("mandatory")
_StarCellMuxInfoTbl_Object = MibTable
starCellMuxInfoTbl = _StarCellMuxInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7)
)
if mibBuilder.loadTexts:
    starCellMuxInfoTbl.setStatus("mandatory")
_StarCellMuxInfoEntry_Object = MibTableRow
starCellMuxInfoEntry = _StarCellMuxInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1)
)
starCellMuxInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIdCellMuxInfo"),
    (0, "STARNE-MIB", "starCellMuxChipId"),
)
if mibBuilder.loadTexts:
    starCellMuxInfoEntry.setStatus("mandatory")
_StarSlotIdCellMuxInfo_Type = Integer32
_StarSlotIdCellMuxInfo_Object = MibTableColumn
starSlotIdCellMuxInfo = _StarSlotIdCellMuxInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 1),
    _StarSlotIdCellMuxInfo_Type()
)
starSlotIdCellMuxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotIdCellMuxInfo.setStatus("mandatory")
_StarCellMuxChipId_Type = Integer32
_StarCellMuxChipId_Object = MibTableColumn
starCellMuxChipId = _StarCellMuxChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 2),
    _StarCellMuxChipId_Type()
)
starCellMuxChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCellMuxChipId.setStatus("mandatory")


class _StarCellMuxCurrentState_Type(Integer32):
    """Custom type starCellMuxCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("operational", 2))
    )


_StarCellMuxCurrentState_Type.__name__ = "Integer32"
_StarCellMuxCurrentState_Object = MibTableColumn
starCellMuxCurrentState = _StarCellMuxCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 3),
    _StarCellMuxCurrentState_Type()
)
starCellMuxCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCellMuxCurrentState.setStatus("mandatory")
_StarCellMuxChipVersion_Type = Integer32
_StarCellMuxChipVersion_Object = MibTableColumn
starCellMuxChipVersion = _StarCellMuxChipVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 4),
    _StarCellMuxChipVersion_Type()
)
starCellMuxChipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCellMuxChipVersion.setStatus("mandatory")
_StarCellMuxWatchDogTimer_Type = Integer32
_StarCellMuxWatchDogTimer_Object = MibTableColumn
starCellMuxWatchDogTimer = _StarCellMuxWatchDogTimer_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 5),
    _StarCellMuxWatchDogTimer_Type()
)
starCellMuxWatchDogTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCellMuxWatchDogTimer.setStatus("mandatory")
_StarCellMuxUsedHighBufCnt_Type = Counter32
_StarCellMuxUsedHighBufCnt_Object = MibTableColumn
starCellMuxUsedHighBufCnt = _StarCellMuxUsedHighBufCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 6),
    _StarCellMuxUsedHighBufCnt_Type()
)
starCellMuxUsedHighBufCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCellMuxUsedHighBufCnt.setStatus("mandatory")
_StarCellMuxUsedMedBufCnt_Type = Counter32
_StarCellMuxUsedMedBufCnt_Object = MibTableColumn
starCellMuxUsedMedBufCnt = _StarCellMuxUsedMedBufCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 7),
    _StarCellMuxUsedMedBufCnt_Type()
)
starCellMuxUsedMedBufCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCellMuxUsedMedBufCnt.setStatus("mandatory")
_StarCellMuxUsedLowBufCnt_Type = Counter32
_StarCellMuxUsedLowBufCnt_Object = MibTableColumn
starCellMuxUsedLowBufCnt = _StarCellMuxUsedLowBufCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 8),
    _StarCellMuxUsedLowBufCnt_Type()
)
starCellMuxUsedLowBufCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCellMuxUsedLowBufCnt.setStatus("mandatory")
_StarCellMuxFreeHighBufCnt_Type = Counter32
_StarCellMuxFreeHighBufCnt_Object = MibTableColumn
starCellMuxFreeHighBufCnt = _StarCellMuxFreeHighBufCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 9),
    _StarCellMuxFreeHighBufCnt_Type()
)
starCellMuxFreeHighBufCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCellMuxFreeHighBufCnt.setStatus("mandatory")
_StarCellMuxFreeMedBufCnt_Type = Counter32
_StarCellMuxFreeMedBufCnt_Object = MibTableColumn
starCellMuxFreeMedBufCnt = _StarCellMuxFreeMedBufCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 10),
    _StarCellMuxFreeMedBufCnt_Type()
)
starCellMuxFreeMedBufCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCellMuxFreeMedBufCnt.setStatus("mandatory")
_StarCellMuxFreeLowBufCnt_Type = Counter32
_StarCellMuxFreeLowBufCnt_Object = MibTableColumn
starCellMuxFreeLowBufCnt = _StarCellMuxFreeLowBufCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 7, 1, 11),
    _StarCellMuxFreeLowBufCnt_Type()
)
starCellMuxFreeLowBufCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCellMuxFreeLowBufCnt.setStatus("mandatory")
_StarSlotRoute88Table_Object = MibTable
starSlotRoute88Table = _StarSlotRoute88Table_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8)
)
if mibBuilder.loadTexts:
    starSlotRoute88Table.setStatus("mandatory")
_StarSlotRoute88Entry_Object = MibTableRow
starSlotRoute88Entry = _StarSlotRoute88Entry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8, 1)
)
starSlotRoute88Entry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starSlotRoute88Index"),
)
if mibBuilder.loadTexts:
    starSlotRoute88Entry.setStatus("mandatory")
_StarSlotRoute88Index_Type = Integer32
_StarSlotRoute88Index_Object = MibTableColumn
starSlotRoute88Index = _StarSlotRoute88Index_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8, 1, 1),
    _StarSlotRoute88Index_Type()
)
starSlotRoute88Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotRoute88Index.setStatus("mandatory")
_StarSlotRoute88Revision_Type = Integer32
_StarSlotRoute88Revision_Object = MibTableColumn
starSlotRoute88Revision = _StarSlotRoute88Revision_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8, 1, 2),
    _StarSlotRoute88Revision_Type()
)
starSlotRoute88Revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotRoute88Revision.setStatus("mandatory")
_StarSlotRoute88TxParityFailCount_Type = Counter32
_StarSlotRoute88TxParityFailCount_Object = MibTableColumn
starSlotRoute88TxParityFailCount = _StarSlotRoute88TxParityFailCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8, 1, 3),
    _StarSlotRoute88TxParityFailCount_Type()
)
starSlotRoute88TxParityFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotRoute88TxParityFailCount.setStatus("mandatory")
_StarSlotRoute88BPIgnoredCount_Type = Counter32
_StarSlotRoute88BPIgnoredCount_Object = MibTableColumn
starSlotRoute88BPIgnoredCount = _StarSlotRoute88BPIgnoredCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8, 1, 4),
    _StarSlotRoute88BPIgnoredCount_Type()
)
starSlotRoute88BPIgnoredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotRoute88BPIgnoredCount.setStatus("mandatory")
_StarSlotRoute88BPLiveFailCount_Type = Counter32
_StarSlotRoute88BPLiveFailCount_Object = MibTableColumn
starSlotRoute88BPLiveFailCount = _StarSlotRoute88BPLiveFailCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8, 1, 5),
    _StarSlotRoute88BPLiveFailCount_Type()
)
starSlotRoute88BPLiveFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotRoute88BPLiveFailCount.setStatus("mandatory")
_StarSlotRoute88WDFailCount_Type = Counter32
_StarSlotRoute88WDFailCount_Object = MibTableColumn
starSlotRoute88WDFailCount = _StarSlotRoute88WDFailCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8, 1, 6),
    _StarSlotRoute88WDFailCount_Type()
)
starSlotRoute88WDFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotRoute88WDFailCount.setStatus("mandatory")
_StarSlotRoute88TxMarkedCells_Type = Counter32
_StarSlotRoute88TxMarkedCells_Object = MibTableColumn
starSlotRoute88TxMarkedCells = _StarSlotRoute88TxMarkedCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8, 1, 7),
    _StarSlotRoute88TxMarkedCells_Type()
)
starSlotRoute88TxMarkedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotRoute88TxMarkedCells.setStatus("mandatory")
_StarSlotRoute88RxMarkedCells_Type = Counter32
_StarSlotRoute88RxMarkedCells_Object = MibTableColumn
starSlotRoute88RxMarkedCells = _StarSlotRoute88RxMarkedCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 8, 1, 8),
    _StarSlotRoute88RxMarkedCells_Type()
)
starSlotRoute88RxMarkedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotRoute88RxMarkedCells.setStatus("mandatory")
_StarSlotAal1SarTable_Object = MibTable
starSlotAal1SarTable = _StarSlotAal1SarTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9)
)
if mibBuilder.loadTexts:
    starSlotAal1SarTable.setStatus("mandatory")
_StarAal1SarInfoEntry_Object = MibTableRow
starAal1SarInfoEntry = _StarAal1SarInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1)
)
starAal1SarInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starAal1SarSlotId"),
    (0, "STARNE-MIB", "starAal1SarPortId"),
    (0, "STARNE-MIB", "starAal1SarChannelId"),
)
if mibBuilder.loadTexts:
    starAal1SarInfoEntry.setStatus("mandatory")
_StarAal1SarSlotId_Type = Integer32
_StarAal1SarSlotId_Object = MibTableColumn
starAal1SarSlotId = _StarAal1SarSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 1),
    _StarAal1SarSlotId_Type()
)
starAal1SarSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarSlotId.setStatus("mandatory")
_StarAal1SarPortId_Type = Integer32
_StarAal1SarPortId_Object = MibTableColumn
starAal1SarPortId = _StarAal1SarPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 2),
    _StarAal1SarPortId_Type()
)
starAal1SarPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarPortId.setStatus("mandatory")
_StarAal1SarChannelId_Type = Integer32
_StarAal1SarChannelId_Object = MibTableColumn
starAal1SarChannelId = _StarAal1SarChannelId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 3),
    _StarAal1SarChannelId_Type()
)
starAal1SarChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarChannelId.setStatus("mandatory")
_StarAal1SarInvalidSnCnt_Type = Integer32
_StarAal1SarInvalidSnCnt_Object = MibTableColumn
starAal1SarInvalidSnCnt = _StarAal1SarInvalidSnCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 4),
    _StarAal1SarInvalidSnCnt_Type()
)
starAal1SarInvalidSnCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarInvalidSnCnt.setStatus("mandatory")
_StarAal1SarIncorrectSnpCnt_Type = Integer32
_StarAal1SarIncorrectSnpCnt_Object = MibTableColumn
starAal1SarIncorrectSnpCnt = _StarAal1SarIncorrectSnpCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 5),
    _StarAal1SarIncorrectSnpCnt_Type()
)
starAal1SarIncorrectSnpCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarIncorrectSnpCnt.setStatus("mandatory")
_StarAal1SarRxOAMCellCnt_Type = Integer32
_StarAal1SarRxOAMCellCnt_Object = MibTableColumn
starAal1SarRxOAMCellCnt = _StarAal1SarRxOAMCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 6),
    _StarAal1SarRxOAMCellCnt_Type()
)
starAal1SarRxOAMCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarRxOAMCellCnt.setStatus("mandatory")
_StarAal1SarRxCellLossStatus_Type = Integer32
_StarAal1SarRxCellLossStatus_Object = MibTableColumn
starAal1SarRxCellLossStatus = _StarAal1SarRxCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 7),
    _StarAal1SarRxCellLossStatus_Type()
)
starAal1SarRxCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarRxCellLossStatus.setStatus("mandatory")
_StarAal1SarLostCellCnt_Type = Integer32
_StarAal1SarLostCellCnt_Object = MibTableColumn
starAal1SarLostCellCnt = _StarAal1SarLostCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 8),
    _StarAal1SarLostCellCnt_Type()
)
starAal1SarLostCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarLostCellCnt.setStatus("mandatory")
_StarAal1SarTxCellCnt_Type = Integer32
_StarAal1SarTxCellCnt_Object = MibTableColumn
starAal1SarTxCellCnt = _StarAal1SarTxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 9),
    _StarAal1SarTxCellCnt_Type()
)
starAal1SarTxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarTxCellCnt.setStatus("mandatory")
_StarAal1SarRxCellCnt_Type = Integer32
_StarAal1SarRxCellCnt_Object = MibTableColumn
starAal1SarRxCellCnt = _StarAal1SarRxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 10),
    _StarAal1SarRxCellCnt_Type()
)
starAal1SarRxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarRxCellCnt.setStatus("mandatory")
_StarAal1SarRxUnderrun_Type = Integer32
_StarAal1SarRxUnderrun_Object = MibTableColumn
starAal1SarRxUnderrun = _StarAal1SarRxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 11),
    _StarAal1SarRxUnderrun_Type()
)
starAal1SarRxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarRxUnderrun.setStatus("mandatory")
_StarAal1SarRxOverrun_Type = Integer32
_StarAal1SarRxOverrun_Object = MibTableColumn
starAal1SarRxOverrun = _StarAal1SarRxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 12),
    _StarAal1SarRxOverrun_Type()
)
starAal1SarRxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarRxOverrun.setStatus("mandatory")
_StarAal1SarPtrMismatch_Type = Integer32
_StarAal1SarPtrMismatch_Object = MibTableColumn
starAal1SarPtrMismatch = _StarAal1SarPtrMismatch_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 9, 1, 13),
    _StarAal1SarPtrMismatch_Type()
)
starAal1SarPtrMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal1SarPtrMismatch.setStatus("mandatory")
_StarSlotLsgnStatusTable_Object = MibTable
starSlotLsgnStatusTable = _StarSlotLsgnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 10)
)
if mibBuilder.loadTexts:
    starSlotLsgnStatusTable.setStatus("mandatory")
_StarLsgnEntry_Object = MibTableRow
starLsgnEntry = _StarLsgnEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 10, 1)
)
starLsgnEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starLsgnEntry.setStatus("mandatory")
_StarLsgnDownCt_Type = Integer32
_StarLsgnDownCt_Object = MibTableColumn
starLsgnDownCt = _StarLsgnDownCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 10, 1, 1),
    _StarLsgnDownCt_Type()
)
starLsgnDownCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLsgnDownCt.setStatus("mandatory")
_StarLsgnUpCt_Type = Integer32
_StarLsgnUpCt_Object = MibTableColumn
starLsgnUpCt = _StarLsgnUpCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 10, 1, 2),
    _StarLsgnUpCt_Type()
)
starLsgnUpCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLsgnUpCt.setStatus("mandatory")
_StarLsgnTrafficLoadChangedCt_Type = Integer32
_StarLsgnTrafficLoadChangedCt_Object = MibTableColumn
starLsgnTrafficLoadChangedCt = _StarLsgnTrafficLoadChangedCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 10, 1, 3),
    _StarLsgnTrafficLoadChangedCt_Type()
)
starLsgnTrafficLoadChangedCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLsgnTrafficLoadChangedCt.setStatus("mandatory")
_StarLsgnPeriodMsgCt_Type = Integer32
_StarLsgnPeriodMsgCt_Object = MibTableColumn
starLsgnPeriodMsgCt = _StarLsgnPeriodMsgCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 10, 1, 4),
    _StarLsgnPeriodMsgCt_Type()
)
starLsgnPeriodMsgCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLsgnPeriodMsgCt.setStatus("mandatory")
_StarLsgnLinkOperStatus_Type = Integer32
_StarLsgnLinkOperStatus_Object = MibTableColumn
starLsgnLinkOperStatus = _StarLsgnLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 10, 1, 5),
    _StarLsgnLinkOperStatus_Type()
)
starLsgnLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLsgnLinkOperStatus.setStatus("mandatory")
_StarSlotRlspStatusTable_Object = MibTable
starSlotRlspStatusTable = _StarSlotRlspStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 11)
)
if mibBuilder.loadTexts:
    starSlotRlspStatusTable.setStatus("mandatory")
_StarRlspEntry_Object = MibTableRow
starRlspEntry = _StarRlspEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 11, 1)
)
starRlspEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
)
if mibBuilder.loadTexts:
    starRlspEntry.setStatus("mandatory")
_StarRlspForwardedCt_Type = Integer32
_StarRlspForwardedCt_Object = MibTableColumn
starRlspForwardedCt = _StarRlspForwardedCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 11, 1, 1),
    _StarRlspForwardedCt_Type()
)
starRlspForwardedCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRlspForwardedCt.setStatus("mandatory")
_StarRlspDiscardedCt_Type = Integer32
_StarRlspDiscardedCt_Object = MibTableColumn
starRlspDiscardedCt = _StarRlspDiscardedCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 11, 1, 2),
    _StarRlspDiscardedCt_Type()
)
starRlspDiscardedCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRlspDiscardedCt.setStatus("mandatory")
_StarRlspInvalidCt_Type = Integer32
_StarRlspInvalidCt_Object = MibTableColumn
starRlspInvalidCt = _StarRlspInvalidCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 11, 1, 3),
    _StarRlspInvalidCt_Type()
)
starRlspInvalidCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRlspInvalidCt.setStatus("mandatory")
_StarRlspMismatchCt_Type = Integer32
_StarRlspMismatchCt_Object = MibTableColumn
starRlspMismatchCt = _StarRlspMismatchCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 11, 1, 4),
    _StarRlspMismatchCt_Type()
)
starRlspMismatchCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRlspMismatchCt.setStatus("mandatory")
_StarRlspNoRoutesCt_Type = Integer32
_StarRlspNoRoutesCt_Object = MibTableColumn
starRlspNoRoutesCt = _StarRlspNoRoutesCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 11, 1, 5),
    _StarRlspNoRoutesCt_Type()
)
starRlspNoRoutesCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRlspNoRoutesCt.setStatus("mandatory")
_StarSlotBbcpStatusTable_Object = MibTable
starSlotBbcpStatusTable = _StarSlotBbcpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12)
)
if mibBuilder.loadTexts:
    starSlotBbcpStatusTable.setStatus("mandatory")
_StarBbcpEntry_Object = MibTableRow
starBbcpEntry = _StarBbcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1)
)
starBbcpEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starBbcpEntry.setStatus("mandatory")
_StarBbcpPtoPInConnections_Type = Integer32
_StarBbcpPtoPInConnections_Object = MibTableColumn
starBbcpPtoPInConnections = _StarBbcpPtoPInConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 1),
    _StarBbcpPtoPInConnections_Type()
)
starBbcpPtoPInConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpPtoPInConnections.setStatus("mandatory")
_StarBbcpPtoPOutConnections_Type = Integer32
_StarBbcpPtoPOutConnections_Object = MibTableColumn
starBbcpPtoPOutConnections = _StarBbcpPtoPOutConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 2),
    _StarBbcpPtoPOutConnections_Type()
)
starBbcpPtoPOutConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpPtoPOutConnections.setStatus("mandatory")
_StarBbcpPtoMInConnections_Type = Integer32
_StarBbcpPtoMInConnections_Object = MibTableColumn
starBbcpPtoMInConnections = _StarBbcpPtoMInConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 3),
    _StarBbcpPtoMInConnections_Type()
)
starBbcpPtoMInConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpPtoMInConnections.setStatus("mandatory")
_StarBbcpPtoMOutConnections_Type = Integer32
_StarBbcpPtoMOutConnections_Object = MibTableColumn
starBbcpPtoMOutConnections = _StarBbcpPtoMOutConnections_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 4),
    _StarBbcpPtoMOutConnections_Type()
)
starBbcpPtoMOutConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpPtoMOutConnections.setStatus("mandatory")
_StarBbcpInConnectionLinkFailCt_Type = Integer32
_StarBbcpInConnectionLinkFailCt_Object = MibTableColumn
starBbcpInConnectionLinkFailCt = _StarBbcpInConnectionLinkFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 5),
    _StarBbcpInConnectionLinkFailCt_Type()
)
starBbcpInConnectionLinkFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionLinkFailCt.setStatus("mandatory")
_StarBbcpInConnectionVcciFailCt_Type = Integer32
_StarBbcpInConnectionVcciFailCt_Object = MibTableColumn
starBbcpInConnectionVcciFailCt = _StarBbcpInConnectionVcciFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 6),
    _StarBbcpInConnectionVcciFailCt_Type()
)
starBbcpInConnectionVcciFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionVcciFailCt.setStatus("mandatory")
_StarBbcpInConnectionNoSwitchCapacityCt_Type = Integer32
_StarBbcpInConnectionNoSwitchCapacityCt_Object = MibTableColumn
starBbcpInConnectionNoSwitchCapacityCt = _StarBbcpInConnectionNoSwitchCapacityCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 7),
    _StarBbcpInConnectionNoSwitchCapacityCt_Type()
)
starBbcpInConnectionNoSwitchCapacityCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionNoSwitchCapacityCt.setStatus("mandatory")
_StarBbcpInConnectionNoBBCapacityCt_Type = Integer32
_StarBbcpInConnectionNoBBCapacityCt_Object = MibTableColumn
starBbcpInConnectionNoBBCapacityCt = _StarBbcpInConnectionNoBBCapacityCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 8),
    _StarBbcpInConnectionNoBBCapacityCt_Type()
)
starBbcpInConnectionNoBBCapacityCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionNoBBCapacityCt.setStatus("mandatory")
_StarBbcpInConnectionTimeoutCt_Type = Integer32
_StarBbcpInConnectionTimeoutCt_Object = MibTableColumn
starBbcpInConnectionTimeoutCt = _StarBbcpInConnectionTimeoutCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 9),
    _StarBbcpInConnectionTimeoutCt_Type()
)
starBbcpInConnectionTimeoutCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionTimeoutCt.setStatus("mandatory")
_StarBbcpInConnectionChipErrorCt_Type = Integer32
_StarBbcpInConnectionChipErrorCt_Object = MibTableColumn
starBbcpInConnectionChipErrorCt = _StarBbcpInConnectionChipErrorCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 10),
    _StarBbcpInConnectionChipErrorCt_Type()
)
starBbcpInConnectionChipErrorCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionChipErrorCt.setStatus("mandatory")
_StarBbcpInConnectionPreemptFailCt_Type = Integer32
_StarBbcpInConnectionPreemptFailCt_Object = MibTableColumn
starBbcpInConnectionPreemptFailCt = _StarBbcpInConnectionPreemptFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 11),
    _StarBbcpInConnectionPreemptFailCt_Type()
)
starBbcpInConnectionPreemptFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionPreemptFailCt.setStatus("mandatory")
_StarBbcpInConnectionModuleFailCt_Type = Integer32
_StarBbcpInConnectionModuleFailCt_Object = MibTableColumn
starBbcpInConnectionModuleFailCt = _StarBbcpInConnectionModuleFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 12),
    _StarBbcpInConnectionModuleFailCt_Type()
)
starBbcpInConnectionModuleFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionModuleFailCt.setStatus("mandatory")
_StarBbcpInConnectionVcciCollisionFailCt_Type = Integer32
_StarBbcpInConnectionVcciCollisionFailCt_Object = MibTableColumn
starBbcpInConnectionVcciCollisionFailCt = _StarBbcpInConnectionVcciCollisionFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 13),
    _StarBbcpInConnectionVcciCollisionFailCt_Type()
)
starBbcpInConnectionVcciCollisionFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionVcciCollisionFailCt.setStatus("mandatory")
_StarBbcpOutConnectionLinkFailCt_Type = Integer32
_StarBbcpOutConnectionLinkFailCt_Object = MibTableColumn
starBbcpOutConnectionLinkFailCt = _StarBbcpOutConnectionLinkFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 14),
    _StarBbcpOutConnectionLinkFailCt_Type()
)
starBbcpOutConnectionLinkFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionLinkFailCt.setStatus("mandatory")
_StarBbcpOutConnectionVcciInvalidCt_Type = Integer32
_StarBbcpOutConnectionVcciInvalidCt_Object = MibTableColumn
starBbcpOutConnectionVcciInvalidCt = _StarBbcpOutConnectionVcciInvalidCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 15),
    _StarBbcpOutConnectionVcciInvalidCt_Type()
)
starBbcpOutConnectionVcciInvalidCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionVcciInvalidCt.setStatus("mandatory")
_StarBbcpOutConnectionNoSwitchCapacityCt_Type = Integer32
_StarBbcpOutConnectionNoSwitchCapacityCt_Object = MibTableColumn
starBbcpOutConnectionNoSwitchCapacityCt = _StarBbcpOutConnectionNoSwitchCapacityCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 16),
    _StarBbcpOutConnectionNoSwitchCapacityCt_Type()
)
starBbcpOutConnectionNoSwitchCapacityCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionNoSwitchCapacityCt.setStatus("mandatory")
_StarBbcpOutConnectionNoBBCapacityCt_Type = Integer32
_StarBbcpOutConnectionNoBBCapacityCt_Object = MibTableColumn
starBbcpOutConnectionNoBBCapacityCt = _StarBbcpOutConnectionNoBBCapacityCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 17),
    _StarBbcpOutConnectionNoBBCapacityCt_Type()
)
starBbcpOutConnectionNoBBCapacityCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionNoBBCapacityCt.setStatus("mandatory")
_StarBbcpOutConnectionTimeoutCt_Type = Integer32
_StarBbcpOutConnectionTimeoutCt_Object = MibTableColumn
starBbcpOutConnectionTimeoutCt = _StarBbcpOutConnectionTimeoutCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 18),
    _StarBbcpOutConnectionTimeoutCt_Type()
)
starBbcpOutConnectionTimeoutCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionTimeoutCt.setStatus("mandatory")
_StarBbcpOutConnectionChipErrorCt_Type = Integer32
_StarBbcpOutConnectionChipErrorCt_Object = MibTableColumn
starBbcpOutConnectionChipErrorCt = _StarBbcpOutConnectionChipErrorCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 19),
    _StarBbcpOutConnectionChipErrorCt_Type()
)
starBbcpOutConnectionChipErrorCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionChipErrorCt.setStatus("mandatory")
_StarBbcpOutConnectionPreemptFailCt_Type = Integer32
_StarBbcpOutConnectionPreemptFailCt_Object = MibTableColumn
starBbcpOutConnectionPreemptFailCt = _StarBbcpOutConnectionPreemptFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 20),
    _StarBbcpOutConnectionPreemptFailCt_Type()
)
starBbcpOutConnectionPreemptFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionPreemptFailCt.setStatus("mandatory")
_StarBbcpOutConnectionModuleFailCt_Type = Integer32
_StarBbcpOutConnectionModuleFailCt_Object = MibTableColumn
starBbcpOutConnectionModuleFailCt = _StarBbcpOutConnectionModuleFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 21),
    _StarBbcpOutConnectionModuleFailCt_Type()
)
starBbcpOutConnectionModuleFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionModuleFailCt.setStatus("mandatory")
_StarBbcpOutConnectionVcciCollisionFailCt_Type = Integer32
_StarBbcpOutConnectionVcciCollisionFailCt_Object = MibTableColumn
starBbcpOutConnectionVcciCollisionFailCt = _StarBbcpOutConnectionVcciCollisionFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 22),
    _StarBbcpOutConnectionVcciCollisionFailCt_Type()
)
starBbcpOutConnectionVcciCollisionFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionVcciCollisionFailCt.setStatus("mandatory")
_StarBbcpInConnectionClearLinkFailCt_Type = Integer32
_StarBbcpInConnectionClearLinkFailCt_Object = MibTableColumn
starBbcpInConnectionClearLinkFailCt = _StarBbcpInConnectionClearLinkFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 23),
    _StarBbcpInConnectionClearLinkFailCt_Type()
)
starBbcpInConnectionClearLinkFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionClearLinkFailCt.setStatus("mandatory")
_StarBbcpInConnectionClearPreemptionCt_Type = Integer32
_StarBbcpInConnectionClearPreemptionCt_Object = MibTableColumn
starBbcpInConnectionClearPreemptionCt = _StarBbcpInConnectionClearPreemptionCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 24),
    _StarBbcpInConnectionClearPreemptionCt_Type()
)
starBbcpInConnectionClearPreemptionCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionClearPreemptionCt.setStatus("mandatory")
_StarBbcpInConnectionClearModuleFailCt_Type = Integer32
_StarBbcpInConnectionClearModuleFailCt_Object = MibTableColumn
starBbcpInConnectionClearModuleFailCt = _StarBbcpInConnectionClearModuleFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 25),
    _StarBbcpInConnectionClearModuleFailCt_Type()
)
starBbcpInConnectionClearModuleFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionClearModuleFailCt.setStatus("mandatory")
_StarBbcpInConnectionClearNormalCt_Type = Integer32
_StarBbcpInConnectionClearNormalCt_Object = MibTableColumn
starBbcpInConnectionClearNormalCt = _StarBbcpInConnectionClearNormalCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 26),
    _StarBbcpInConnectionClearNormalCt_Type()
)
starBbcpInConnectionClearNormalCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInConnectionClearNormalCt.setStatus("mandatory")
_StarBbcpOutConnectionClearLinkFailCt_Type = Integer32
_StarBbcpOutConnectionClearLinkFailCt_Object = MibTableColumn
starBbcpOutConnectionClearLinkFailCt = _StarBbcpOutConnectionClearLinkFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 27),
    _StarBbcpOutConnectionClearLinkFailCt_Type()
)
starBbcpOutConnectionClearLinkFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionClearLinkFailCt.setStatus("mandatory")
_StarBbcpOutConnectionClearPreemptionCt_Type = Integer32
_StarBbcpOutConnectionClearPreemptionCt_Object = MibTableColumn
starBbcpOutConnectionClearPreemptionCt = _StarBbcpOutConnectionClearPreemptionCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 28),
    _StarBbcpOutConnectionClearPreemptionCt_Type()
)
starBbcpOutConnectionClearPreemptionCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionClearPreemptionCt.setStatus("mandatory")
_StarBbcpOutConnectionClearModuleFailCt_Type = Integer32
_StarBbcpOutConnectionClearModuleFailCt_Object = MibTableColumn
starBbcpOutConnectionClearModuleFailCt = _StarBbcpOutConnectionClearModuleFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 29),
    _StarBbcpOutConnectionClearModuleFailCt_Type()
)
starBbcpOutConnectionClearModuleFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionClearModuleFailCt.setStatus("mandatory")
_StarBbcpOutConnectionClearNormalCt_Type = Integer32
_StarBbcpOutConnectionClearNormalCt_Object = MibTableColumn
starBbcpOutConnectionClearNormalCt = _StarBbcpOutConnectionClearNormalCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 30),
    _StarBbcpOutConnectionClearNormalCt_Type()
)
starBbcpOutConnectionClearNormalCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpOutConnectionClearNormalCt.setStatus("mandatory")
_StarBbcpInvalidMsgCt_Type = Integer32
_StarBbcpInvalidMsgCt_Object = MibTableColumn
starBbcpInvalidMsgCt = _StarBbcpInvalidMsgCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 31),
    _StarBbcpInvalidMsgCt_Type()
)
starBbcpInvalidMsgCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInvalidMsgCt.setStatus("mandatory")
_StarBbcpTimerExpiredCt_Type = Integer32
_StarBbcpTimerExpiredCt_Object = MibTableColumn
starBbcpTimerExpiredCt = _StarBbcpTimerExpiredCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 32),
    _StarBbcpTimerExpiredCt_Type()
)
starBbcpTimerExpiredCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpTimerExpiredCt.setStatus("mandatory")
_StarBbcpInvalidEventCt_Type = Integer32
_StarBbcpInvalidEventCt_Object = MibTableColumn
starBbcpInvalidEventCt = _StarBbcpInvalidEventCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 33),
    _StarBbcpInvalidEventCt_Type()
)
starBbcpInvalidEventCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpInvalidEventCt.setStatus("mandatory")
_StarBbcpAvailableFixedCapacity_Type = Integer32
_StarBbcpAvailableFixedCapacity_Object = MibTableColumn
starBbcpAvailableFixedCapacity = _StarBbcpAvailableFixedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 34),
    _StarBbcpAvailableFixedCapacity_Type()
)
starBbcpAvailableFixedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpAvailableFixedCapacity.setStatus("mandatory")
_StarBbcpAvailableVariableCapacity_Type = Integer32
_StarBbcpAvailableVariableCapacity_Object = MibTableColumn
starBbcpAvailableVariableCapacity = _StarBbcpAvailableVariableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 12, 1, 35),
    _StarBbcpAvailableVariableCapacity_Type()
)
starBbcpAvailableVariableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpAvailableVariableCapacity.setStatus("mandatory")
_StarSlotBbcpXConnectTable_Object = MibTable
starSlotBbcpXConnectTable = _StarSlotBbcpXConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13)
)
if mibBuilder.loadTexts:
    starSlotBbcpXConnectTable.setStatus("mandatory")
_StarBbcpXConnectEntry_Object = MibTableRow
starBbcpXConnectEntry = _StarBbcpXConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1)
)
starBbcpXConnectEntry.setIndexNames(
    (0, "STARNE-MIB", "starBbcpSlotIndex"),
    (0, "STARNE-MIB", "starBbcpPortIndex"),
    (0, "STARNE-MIB", "starBbcpGCIDNeId"),
    (0, "STARNE-MIB", "starBbcpGCIDSlotId"),
    (0, "STARNE-MIB", "starBbcpGCIDPortId"),
    (0, "STARNE-MIB", "starBbcpGCIDIfType"),
    (0, "STARNE-MIB", "starBbcpGCIDConnId"),
    (0, "STARNE-MIB", "starBbcpGCIDLeafId"),
)
if mibBuilder.loadTexts:
    starBbcpXConnectEntry.setStatus("mandatory")
_StarBbcpSlotIndex_Type = Integer32
_StarBbcpSlotIndex_Object = MibTableColumn
starBbcpSlotIndex = _StarBbcpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 1),
    _StarBbcpSlotIndex_Type()
)
starBbcpSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpSlotIndex.setStatus("mandatory")
_StarBbcpPortIndex_Type = Integer32
_StarBbcpPortIndex_Object = MibTableColumn
starBbcpPortIndex = _StarBbcpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 2),
    _StarBbcpPortIndex_Type()
)
starBbcpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpPortIndex.setStatus("mandatory")
_StarBbcpGCIDNeId_Type = Integer32
_StarBbcpGCIDNeId_Object = MibTableColumn
starBbcpGCIDNeId = _StarBbcpGCIDNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 3),
    _StarBbcpGCIDNeId_Type()
)
starBbcpGCIDNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpGCIDNeId.setStatus("mandatory")
_StarBbcpGCIDSlotId_Type = Integer32
_StarBbcpGCIDSlotId_Object = MibTableColumn
starBbcpGCIDSlotId = _StarBbcpGCIDSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 4),
    _StarBbcpGCIDSlotId_Type()
)
starBbcpGCIDSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpGCIDSlotId.setStatus("mandatory")
_StarBbcpGCIDPortId_Type = Integer32
_StarBbcpGCIDPortId_Object = MibTableColumn
starBbcpGCIDPortId = _StarBbcpGCIDPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 5),
    _StarBbcpGCIDPortId_Type()
)
starBbcpGCIDPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpGCIDPortId.setStatus("mandatory")
_StarBbcpGCIDIfType_Type = Integer32
_StarBbcpGCIDIfType_Object = MibTableColumn
starBbcpGCIDIfType = _StarBbcpGCIDIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 6),
    _StarBbcpGCIDIfType_Type()
)
starBbcpGCIDIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpGCIDIfType.setStatus("mandatory")
_StarBbcpGCIDConnId_Type = Integer32
_StarBbcpGCIDConnId_Object = MibTableColumn
starBbcpGCIDConnId = _StarBbcpGCIDConnId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 7),
    _StarBbcpGCIDConnId_Type()
)
starBbcpGCIDConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpGCIDConnId.setStatus("mandatory")
_StarBbcpGCIDLeafId_Type = Integer32
_StarBbcpGCIDLeafId_Object = MibTableColumn
starBbcpGCIDLeafId = _StarBbcpGCIDLeafId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 8),
    _StarBbcpGCIDLeafId_Type()
)
starBbcpGCIDLeafId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpGCIDLeafId.setStatus("mandatory")
_StarBbcpXConnOperStatus_Type = Integer32
_StarBbcpXConnOperStatus_Object = MibTableColumn
starBbcpXConnOperStatus = _StarBbcpXConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 9),
    _StarBbcpXConnOperStatus_Type()
)
starBbcpXConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpXConnOperStatus.setStatus("mandatory")
_StarBbcpXConnAdjacentSlotId_Type = Integer32
_StarBbcpXConnAdjacentSlotId_Object = MibTableColumn
starBbcpXConnAdjacentSlotId = _StarBbcpXConnAdjacentSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 10),
    _StarBbcpXConnAdjacentSlotId_Type()
)
starBbcpXConnAdjacentSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpXConnAdjacentSlotId.setStatus("mandatory")
_StarBbcpXConnAdjacentPortId_Type = Integer32
_StarBbcpXConnAdjacentPortId_Object = MibTableColumn
starBbcpXConnAdjacentPortId = _StarBbcpXConnAdjacentPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 11),
    _StarBbcpXConnAdjacentPortId_Type()
)
starBbcpXConnAdjacentPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpXConnAdjacentPortId.setStatus("mandatory")
_StarBbcpXConnAdjacentVpi_Type = Integer32
_StarBbcpXConnAdjacentVpi_Object = MibTableColumn
starBbcpXConnAdjacentVpi = _StarBbcpXConnAdjacentVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 12),
    _StarBbcpXConnAdjacentVpi_Type()
)
starBbcpXConnAdjacentVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpXConnAdjacentVpi.setStatus("mandatory")
_StarBbcpXConnAdjacentVci_Type = Integer32
_StarBbcpXConnAdjacentVci_Object = MibTableColumn
starBbcpXConnAdjacentVci = _StarBbcpXConnAdjacentVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 13, 1, 13),
    _StarBbcpXConnAdjacentVci_Type()
)
starBbcpXConnAdjacentVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBbcpXConnAdjacentVci.setStatus("mandatory")
_StarPvcmStatusTable_Object = MibTable
starPvcmStatusTable = _StarPvcmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14)
)
if mibBuilder.loadTexts:
    starPvcmStatusTable.setStatus("mandatory")
_StarPvcmEntry_Object = MibTableRow
starPvcmEntry = _StarPvcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1)
)
starPvcmEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starPvcmEntry.setStatus("mandatory")
_StarPvcmPtoPOrgConnectionNumber_Type = Integer32
_StarPvcmPtoPOrgConnectionNumber_Object = MibTableColumn
starPvcmPtoPOrgConnectionNumber = _StarPvcmPtoPOrgConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 1),
    _StarPvcmPtoPOrgConnectionNumber_Type()
)
starPvcmPtoPOrgConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmPtoPOrgConnectionNumber.setStatus("mandatory")
_StarPvcmPtoPTermConnectionNumber_Type = Integer32
_StarPvcmPtoPTermConnectionNumber_Object = MibTableColumn
starPvcmPtoPTermConnectionNumber = _StarPvcmPtoPTermConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 2),
    _StarPvcmPtoPTermConnectionNumber_Type()
)
starPvcmPtoPTermConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmPtoPTermConnectionNumber.setStatus("mandatory")
_StarPvcmPtoMOrgConnectionNumber_Type = Integer32
_StarPvcmPtoMOrgConnectionNumber_Object = MibTableColumn
starPvcmPtoMOrgConnectionNumber = _StarPvcmPtoMOrgConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 3),
    _StarPvcmPtoMOrgConnectionNumber_Type()
)
starPvcmPtoMOrgConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmPtoMOrgConnectionNumber.setStatus("mandatory")
_StarPvcmPtoMTermConnectionNumber_Type = Integer32
_StarPvcmPtoMTermConnectionNumber_Object = MibTableColumn
starPvcmPtoMTermConnectionNumber = _StarPvcmPtoMTermConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 4),
    _StarPvcmPtoMTermConnectionNumber_Type()
)
starPvcmPtoMTermConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmPtoMTermConnectionNumber.setStatus("mandatory")
_StarPvcmOutOfServiceConnectionNumber_Type = Integer32
_StarPvcmOutOfServiceConnectionNumber_Object = MibTableColumn
starPvcmOutOfServiceConnectionNumber = _StarPvcmOutOfServiceConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 5),
    _StarPvcmOutOfServiceConnectionNumber_Type()
)
starPvcmOutOfServiceConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmOutOfServiceConnectionNumber.setStatus("mandatory")
_StarPvcmOptimizedConnectionNumber_Type = Integer32
_StarPvcmOptimizedConnectionNumber_Object = MibTableColumn
starPvcmOptimizedConnectionNumber = _StarPvcmOptimizedConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 6),
    _StarPvcmOptimizedConnectionNumber_Type()
)
starPvcmOptimizedConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmOptimizedConnectionNumber.setStatus("mandatory")
_StarPvcmRouteFailCt_Type = Integer32
_StarPvcmRouteFailCt_Object = MibTableColumn
starPvcmRouteFailCt = _StarPvcmRouteFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 7),
    _StarPvcmRouteFailCt_Type()
)
starPvcmRouteFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmRouteFailCt.setStatus("mandatory")
_StarPvcmConnectReqFailCt_Type = Integer32
_StarPvcmConnectReqFailCt_Object = MibTableColumn
starPvcmConnectReqFailCt = _StarPvcmConnectReqFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 8),
    _StarPvcmConnectReqFailCt_Type()
)
starPvcmConnectReqFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmConnectReqFailCt.setStatus("mandatory")
_StarPvcmOrgConnectedFailCt_Type = Integer32
_StarPvcmOrgConnectedFailCt_Object = MibTableColumn
starPvcmOrgConnectedFailCt = _StarPvcmOrgConnectedFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 9),
    _StarPvcmOrgConnectedFailCt_Type()
)
starPvcmOrgConnectedFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmOrgConnectedFailCt.setStatus("mandatory")
_StarPvcmTermConnectedFailCt_Type = Integer32
_StarPvcmTermConnectedFailCt_Object = MibTableColumn
starPvcmTermConnectedFailCt = _StarPvcmTermConnectedFailCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 10),
    _StarPvcmTermConnectedFailCt_Type()
)
starPvcmTermConnectedFailCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmTermConnectedFailCt.setStatus("mandatory")
_StarPvcmActiveConnectionNumber_Type = Integer32
_StarPvcmActiveConnectionNumber_Object = MibTableColumn
starPvcmActiveConnectionNumber = _StarPvcmActiveConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 11),
    _StarPvcmActiveConnectionNumber_Type()
)
starPvcmActiveConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmActiveConnectionNumber.setStatus("mandatory")
_StarPvcmDeletedConnectionNumber_Type = Integer32
_StarPvcmDeletedConnectionNumber_Object = MibTableColumn
starPvcmDeletedConnectionNumber = _StarPvcmDeletedConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 12),
    _StarPvcmDeletedConnectionNumber_Type()
)
starPvcmDeletedConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmDeletedConnectionNumber.setStatus("mandatory")
_StarPvcmAddedConnectionNumber_Type = Integer32
_StarPvcmAddedConnectionNumber_Object = MibTableColumn
starPvcmAddedConnectionNumber = _StarPvcmAddedConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 13),
    _StarPvcmAddedConnectionNumber_Type()
)
starPvcmAddedConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmAddedConnectionNumber.setStatus("mandatory")
_StarPvcmFailedConnectionNumber_Type = Integer32
_StarPvcmFailedConnectionNumber_Object = MibTableColumn
starPvcmFailedConnectionNumber = _StarPvcmFailedConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 14),
    _StarPvcmFailedConnectionNumber_Type()
)
starPvcmFailedConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmFailedConnectionNumber.setStatus("mandatory")
_StarPvcmChangedConnectionNumber_Type = Integer32
_StarPvcmChangedConnectionNumber_Object = MibTableColumn
starPvcmChangedConnectionNumber = _StarPvcmChangedConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 15),
    _StarPvcmChangedConnectionNumber_Type()
)
starPvcmChangedConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmChangedConnectionNumber.setStatus("mandatory")
_StarPvcmOrgHoldingConnectionNumber_Type = Integer32
_StarPvcmOrgHoldingConnectionNumber_Object = MibTableColumn
starPvcmOrgHoldingConnectionNumber = _StarPvcmOrgHoldingConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 16),
    _StarPvcmOrgHoldingConnectionNumber_Type()
)
starPvcmOrgHoldingConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmOrgHoldingConnectionNumber.setStatus("mandatory")
_StarPvcmTermHoldingConnectionNumber_Type = Integer32
_StarPvcmTermHoldingConnectionNumber_Object = MibTableColumn
starPvcmTermHoldingConnectionNumber = _StarPvcmTermHoldingConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 17),
    _StarPvcmTermHoldingConnectionNumber_Type()
)
starPvcmTermHoldingConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmTermHoldingConnectionNumber.setStatus("mandatory")
_StarPvcmInvalidMsgNumber_Type = Integer32
_StarPvcmInvalidMsgNumber_Object = MibTableColumn
starPvcmInvalidMsgNumber = _StarPvcmInvalidMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 18),
    _StarPvcmInvalidMsgNumber_Type()
)
starPvcmInvalidMsgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmInvalidMsgNumber.setStatus("mandatory")
_StarPvcmTimerExpiredCnt_Type = Integer32
_StarPvcmTimerExpiredCnt_Object = MibTableColumn
starPvcmTimerExpiredCnt = _StarPvcmTimerExpiredCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 14, 1, 19),
    _StarPvcmTimerExpiredCnt_Type()
)
starPvcmTimerExpiredCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmTimerExpiredCnt.setStatus("mandatory")
_StarPvcConnectionTable_Object = MibTable
starPvcConnectionTable = _StarPvcConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15)
)
if mibBuilder.loadTexts:
    starPvcConnectionTable.setStatus("mandatory")
_StarPvcConnectionEntry_Object = MibTableRow
starPvcConnectionEntry = _StarPvcConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1)
)
starPvcConnectionEntry.setIndexNames(
    (0, "STARNE-MIB", "starPvcSrcSlotId"),
    (0, "STARNE-MIB", "starPvcSrcPortId"),
    (0, "STARNE-MIB", "starPvcSrcIfType"),
    (0, "STARNE-MIB", "starPvcSrcVpi"),
    (0, "STARNE-MIB", "starPvcSrcVci"),
    (0, "STARNE-MIB", "starPvcSrcLeaf"),
    (0, "STARNE-MIB", "starPvcSrcDlci"),
    (0, "STARNE-MIB", "starPvcSrcTimeslot"),
)
if mibBuilder.loadTexts:
    starPvcConnectionEntry.setStatus("mandatory")
_StarPvcSrcSlotId_Type = Integer32
_StarPvcSrcSlotId_Object = MibTableColumn
starPvcSrcSlotId = _StarPvcSrcSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 1),
    _StarPvcSrcSlotId_Type()
)
starPvcSrcSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcSrcSlotId.setStatus("mandatory")
_StarPvcSrcPortId_Type = Integer32
_StarPvcSrcPortId_Object = MibTableColumn
starPvcSrcPortId = _StarPvcSrcPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 2),
    _StarPvcSrcPortId_Type()
)
starPvcSrcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcSrcPortId.setStatus("mandatory")
_StarPvcSrcIfType_Type = Integer32
_StarPvcSrcIfType_Object = MibTableColumn
starPvcSrcIfType = _StarPvcSrcIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 3),
    _StarPvcSrcIfType_Type()
)
starPvcSrcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcSrcIfType.setStatus("mandatory")
_StarPvcSrcVpi_Type = Integer32
_StarPvcSrcVpi_Object = MibTableColumn
starPvcSrcVpi = _StarPvcSrcVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 4),
    _StarPvcSrcVpi_Type()
)
starPvcSrcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcSrcVpi.setStatus("mandatory")
_StarPvcSrcVci_Type = Integer32
_StarPvcSrcVci_Object = MibTableColumn
starPvcSrcVci = _StarPvcSrcVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 5),
    _StarPvcSrcVci_Type()
)
starPvcSrcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcSrcVci.setStatus("mandatory")
_StarPvcSrcLeaf_Type = Integer32
_StarPvcSrcLeaf_Object = MibTableColumn
starPvcSrcLeaf = _StarPvcSrcLeaf_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 6),
    _StarPvcSrcLeaf_Type()
)
starPvcSrcLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcSrcLeaf.setStatus("mandatory")
_StarPvcSrcDlci_Type = Integer32
_StarPvcSrcDlci_Object = MibTableColumn
starPvcSrcDlci = _StarPvcSrcDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 7),
    _StarPvcSrcDlci_Type()
)
starPvcSrcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcSrcDlci.setStatus("mandatory")
_StarPvcSrcTimeslot_Type = Integer32
_StarPvcSrcTimeslot_Object = MibTableColumn
starPvcSrcTimeslot = _StarPvcSrcTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 8),
    _StarPvcSrcTimeslot_Type()
)
starPvcSrcTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcSrcTimeslot.setStatus("mandatory")
_StarPvcDestNodeId_Type = Integer32
_StarPvcDestNodeId_Object = MibTableColumn
starPvcDestNodeId = _StarPvcDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 9),
    _StarPvcDestNodeId_Type()
)
starPvcDestNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcDestNodeId.setStatus("mandatory")
_StarPvcDestSlotId_Type = Integer32
_StarPvcDestSlotId_Object = MibTableColumn
starPvcDestSlotId = _StarPvcDestSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 10),
    _StarPvcDestSlotId_Type()
)
starPvcDestSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcDestSlotId.setStatus("mandatory")
_StarPvcDestPortId_Type = Integer32
_StarPvcDestPortId_Object = MibTableColumn
starPvcDestPortId = _StarPvcDestPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 11),
    _StarPvcDestPortId_Type()
)
starPvcDestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcDestPortId.setStatus("mandatory")
_StarPvcDestIfType_Type = Integer32
_StarPvcDestIfType_Object = MibTableColumn
starPvcDestIfType = _StarPvcDestIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 12),
    _StarPvcDestIfType_Type()
)
starPvcDestIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcDestIfType.setStatus("mandatory")
_StarPvcDestVpi_Type = Integer32
_StarPvcDestVpi_Object = MibTableColumn
starPvcDestVpi = _StarPvcDestVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 13),
    _StarPvcDestVpi_Type()
)
starPvcDestVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcDestVpi.setStatus("mandatory")
_StarPvcDestVci_Type = Integer32
_StarPvcDestVci_Object = MibTableColumn
starPvcDestVci = _StarPvcDestVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 14),
    _StarPvcDestVci_Type()
)
starPvcDestVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcDestVci.setStatus("mandatory")
_StarPvcDestDlci_Type = Integer32
_StarPvcDestDlci_Object = MibTableColumn
starPvcDestDlci = _StarPvcDestDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 15),
    _StarPvcDestDlci_Type()
)
starPvcDestDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcDestDlci.setStatus("mandatory")
_StarPvcDestTimeslot_Type = Integer32
_StarPvcDestTimeslot_Object = MibTableColumn
starPvcDestTimeslot = _StarPvcDestTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 16),
    _StarPvcDestTimeslot_Type()
)
starPvcDestTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcDestTimeslot.setStatus("mandatory")
_StarPvcConnectionOperStatus_Type = Integer32
_StarPvcConnectionOperStatus_Object = MibTableColumn
starPvcConnectionOperStatus = _StarPvcConnectionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 17),
    _StarPvcConnectionOperStatus_Type()
)
starPvcConnectionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcConnectionOperStatus.setStatus("mandatory")
_StarPvcConnectionType_Type = Integer32
_StarPvcConnectionType_Object = MibTableColumn
starPvcConnectionType = _StarPvcConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 18),
    _StarPvcConnectionType_Type()
)
starPvcConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcConnectionType.setStatus("mandatory")
_StarPvcConnectionCOS_Type = Integer32
_StarPvcConnectionCOS_Object = MibTableColumn
starPvcConnectionCOS = _StarPvcConnectionCOS_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 19),
    _StarPvcConnectionCOS_Type()
)
starPvcConnectionCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcConnectionCOS.setStatus("mandatory")
_StarPvcConnectionStatusLastChangedDate_Type = Integer32
_StarPvcConnectionStatusLastChangedDate_Object = MibTableColumn
starPvcConnectionStatusLastChangedDate = _StarPvcConnectionStatusLastChangedDate_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 20),
    _StarPvcConnectionStatusLastChangedDate_Type()
)
starPvcConnectionStatusLastChangedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcConnectionStatusLastChangedDate.setStatus("mandatory")
_StarPvcConnectionStatusLastChangedTime_Type = Integer32
_StarPvcConnectionStatusLastChangedTime_Object = MibTableColumn
starPvcConnectionStatusLastChangedTime = _StarPvcConnectionStatusLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 21),
    _StarPvcConnectionStatusLastChangedTime_Type()
)
starPvcConnectionStatusLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcConnectionStatusLastChangedTime.setStatus("mandatory")
_StarPvcConnectionCauseValue_Type = Integer32
_StarPvcConnectionCauseValue_Object = MibTableColumn
starPvcConnectionCauseValue = _StarPvcConnectionCauseValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 15, 1, 22),
    _StarPvcConnectionCauseValue_Type()
)
starPvcConnectionCauseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcConnectionCauseValue.setStatus("mandatory")
_StarFiuModuleInfo_ObjectIdentity = ObjectIdentity
starFiuModuleInfo = _StarFiuModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16)
)
_StarFrlExtnModuleInfo_ObjectIdentity = ObjectIdentity
starFrlExtnModuleInfo = _StarFrlExtnModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1)
)
_FrlPortInfoTbl_Object = MibTable
frlPortInfoTbl = _FrlPortInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    frlPortInfoTbl.setStatus("mandatory")
_FrlPortInfoEntry_Object = MibTableRow
frlPortInfoEntry = _FrlPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 1, 1)
)
frlPortInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "frlPortInfoSlotId"),
    (0, "STARNE-MIB", "frlPortInfoPortId"),
)
if mibBuilder.loadTexts:
    frlPortInfoEntry.setStatus("mandatory")
_FrlPortInfoSlotId_Type = Integer32
_FrlPortInfoSlotId_Object = MibTableColumn
frlPortInfoSlotId = _FrlPortInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 1, 1, 1),
    _FrlPortInfoSlotId_Type()
)
frlPortInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frlPortInfoSlotId.setStatus("mandatory")
_FrlPortInfoPortId_Type = Integer32
_FrlPortInfoPortId_Object = MibTableColumn
frlPortInfoPortId = _FrlPortInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 1, 1, 2),
    _FrlPortInfoPortId_Type()
)
frlPortInfoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frlPortInfoPortId.setStatus("mandatory")


class _FrlPortSigMode_Type(Integer32):
    """Custom type frlPortSigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FrlPortSigMode_Type.__name__ = "Integer32"
_FrlPortSigMode_Object = MibTableColumn
frlPortSigMode = _FrlPortSigMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 1, 1, 3),
    _FrlPortSigMode_Type()
)
frlPortSigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frlPortSigMode.setStatus("mandatory")
_FrlPortActiveDlci_Type = Integer32
_FrlPortActiveDlci_Object = MibTableColumn
frlPortActiveDlci = _FrlPortActiveDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 1, 1, 4),
    _FrlPortActiveDlci_Type()
)
frlPortActiveDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frlPortActiveDlci.setStatus("mandatory")
_FrlPvcEndptInfoTbl_Object = MibTable
frlPvcEndptInfoTbl = _FrlPvcEndptInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2)
)
if mibBuilder.loadTexts:
    frlPvcEndptInfoTbl.setStatus("mandatory")
_FrlPvcEndptInfoEntry_Object = MibTableRow
frlPvcEndptInfoEntry = _FrlPvcEndptInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1)
)
frlPvcEndptInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "frlPvcEndptInfoSlotId"),
    (0, "STARNE-MIB", "frlPvcEndptInfoPortId"),
    (0, "STARNE-MIB", "frlPvcEndptInfoDlci"),
)
if mibBuilder.loadTexts:
    frlPvcEndptInfoEntry.setStatus("mandatory")
_FrlPvcEndptInfoSlotId_Type = Integer32
_FrlPvcEndptInfoSlotId_Object = MibTableColumn
frlPvcEndptInfoSlotId = _FrlPvcEndptInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 1),
    _FrlPvcEndptInfoSlotId_Type()
)
frlPvcEndptInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frlPvcEndptInfoSlotId.setStatus("mandatory")
_FrlPvcEndptInfoPortId_Type = Integer32
_FrlPvcEndptInfoPortId_Object = MibTableColumn
frlPvcEndptInfoPortId = _FrlPvcEndptInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 2),
    _FrlPvcEndptInfoPortId_Type()
)
frlPvcEndptInfoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frlPvcEndptInfoPortId.setStatus("mandatory")
_FrlPvcEndptInfoDlci_Type = Integer32
_FrlPvcEndptInfoDlci_Object = MibTableColumn
frlPvcEndptInfoDlci = _FrlPvcEndptInfoDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 3),
    _FrlPvcEndptInfoDlci_Type()
)
frlPvcEndptInfoDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frlPvcEndptInfoDlci.setStatus("mandatory")
_FrPvcEndptInfoTimeStamp_Type = Integer32
_FrPvcEndptInfoTimeStamp_Object = MibTableColumn
frPvcEndptInfoTimeStamp = _FrPvcEndptInfoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 4),
    _FrPvcEndptInfoTimeStamp_Type()
)
frPvcEndptInfoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptInfoTimeStamp.setStatus("mandatory")
_FrPvcMarkedDe_Type = Integer32
_FrPvcMarkedDe_Object = MibTableColumn
frPvcMarkedDe = _FrPvcMarkedDe_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 5),
    _FrPvcMarkedDe_Type()
)
frPvcMarkedDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcMarkedDe.setStatus("mandatory")
_FrPvcEndptOperStatus_Type = Integer32
_FrPvcEndptOperStatus_Object = MibTableColumn
frPvcEndptOperStatus = _FrPvcEndptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 6),
    _FrPvcEndptOperStatus_Type()
)
frPvcEndptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptOperStatus.setStatus("mandatory")
_FrPvcEndptNoRecvFECN_Type = Integer32
_FrPvcEndptNoRecvFECN_Object = MibTableColumn
frPvcEndptNoRecvFECN = _FrPvcEndptNoRecvFECN_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 7),
    _FrPvcEndptNoRecvFECN_Type()
)
frPvcEndptNoRecvFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptNoRecvFECN.setStatus("mandatory")
_FrPvcEndptNoTxFECN_Type = Integer32
_FrPvcEndptNoTxFECN_Object = MibTableColumn
frPvcEndptNoTxFECN = _FrPvcEndptNoTxFECN_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 8),
    _FrPvcEndptNoTxFECN_Type()
)
frPvcEndptNoTxFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptNoTxFECN.setStatus("mandatory")
_FrPvcEndptNoRecvBECN_Type = Integer32
_FrPvcEndptNoRecvBECN_Object = MibTableColumn
frPvcEndptNoRecvBECN = _FrPvcEndptNoRecvBECN_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 9),
    _FrPvcEndptNoRecvBECN_Type()
)
frPvcEndptNoRecvBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptNoRecvBECN.setStatus("mandatory")
_FrPvcEndptNoTxBECN_Type = Integer32
_FrPvcEndptNoTxBECN_Object = MibTableColumn
frPvcEndptNoTxBECN = _FrPvcEndptNoTxBECN_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 10),
    _FrPvcEndptNoTxBECN_Type()
)
frPvcEndptNoTxBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptNoTxBECN.setStatus("mandatory")
_FrPvcEndptNoTxDE_Type = Integer32
_FrPvcEndptNoTxDE_Object = MibTableColumn
frPvcEndptNoTxDE = _FrPvcEndptNoTxDE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 11),
    _FrPvcEndptNoTxDE_Type()
)
frPvcEndptNoTxDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptNoTxDE.setStatus("mandatory")
_FrPvcEndptNoDiscardWithDE_Type = Integer32
_FrPvcEndptNoDiscardWithDE_Object = MibTableColumn
frPvcEndptNoDiscardWithDE = _FrPvcEndptNoDiscardWithDE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 12),
    _FrPvcEndptNoDiscardWithDE_Type()
)
frPvcEndptNoDiscardWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptNoDiscardWithDE.setStatus("mandatory")
_FrPvcEndptNoDiscardWoutDE_Type = Integer32
_FrPvcEndptNoDiscardWoutDE_Object = MibTableColumn
frPvcEndptNoDiscardWoutDE = _FrPvcEndptNoDiscardWoutDE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 13),
    _FrPvcEndptNoDiscardWoutDE_Type()
)
frPvcEndptNoDiscardWoutDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptNoDiscardWoutDE.setStatus("mandatory")
_FrPvcEndptInDEFrames_Type = Integer32
_FrPvcEndptInDEFrames_Object = MibTableColumn
frPvcEndptInDEFrames = _FrPvcEndptInDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 2, 1, 14),
    _FrPvcEndptInDEFrames_Type()
)
frPvcEndptInDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcEndptInDEFrames.setStatus("mandatory")
_StarfrPVCEndptPerfTbl_Object = MibTable
starfrPVCEndptPerfTbl = _StarfrPVCEndptPerfTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3)
)
if mibBuilder.loadTexts:
    starfrPVCEndptPerfTbl.setStatus("mandatory")
_StarfrPVCEndptPerfTblEntry_Object = MibTableRow
starfrPVCEndptPerfTblEntry = _StarfrPVCEndptPerfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1)
)
starfrPVCEndptPerfTblEntry.setIndexNames(
    (0, "STARNE-MIB", "starfrPVCEndptPerfSlotId"),
    (0, "STARNE-MIB", "starfrPVCEndptPerfPortId"),
    (0, "STARNE-MIB", "starfrPVCEndptPerfDLCIIndex"),
)
if mibBuilder.loadTexts:
    starfrPVCEndptPerfTblEntry.setStatus("mandatory")
_StarfrPVCEndptPerfSlotId_Type = Integer32
_StarfrPVCEndptPerfSlotId_Object = MibTableColumn
starfrPVCEndptPerfSlotId = _StarfrPVCEndptPerfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 1),
    _StarfrPVCEndptPerfSlotId_Type()
)
starfrPVCEndptPerfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfSlotId.setStatus("mandatory")
_StarfrPVCEndptPerfPortId_Type = Integer32
_StarfrPVCEndptPerfPortId_Object = MibTableColumn
starfrPVCEndptPerfPortId = _StarfrPVCEndptPerfPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 2),
    _StarfrPVCEndptPerfPortId_Type()
)
starfrPVCEndptPerfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfPortId.setStatus("mandatory")
_StarfrPVCEndptPerfDLCIIndex_Type = Integer32
_StarfrPVCEndptPerfDLCIIndex_Object = MibTableColumn
starfrPVCEndptPerfDLCIIndex = _StarfrPVCEndptPerfDLCIIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 3),
    _StarfrPVCEndptPerfDLCIIndex_Type()
)
starfrPVCEndptPerfDLCIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfDLCIIndex.setStatus("mandatory")
_StarfrPVCEndptPerfTmStp_Type = Integer32
_StarfrPVCEndptPerfTmStp_Object = MibTableColumn
starfrPVCEndptPerfTmStp = _StarfrPVCEndptPerfTmStp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 4),
    _StarfrPVCEndptPerfTmStp_Type()
)
starfrPVCEndptPerfTmStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfTmStp.setStatus("mandatory")
_StarfrPVCEndptPerfRxPktSz_Type = Integer32
_StarfrPVCEndptPerfRxPktSz_Object = MibTableColumn
starfrPVCEndptPerfRxPktSz = _StarfrPVCEndptPerfRxPktSz_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 5),
    _StarfrPVCEndptPerfRxPktSz_Type()
)
starfrPVCEndptPerfRxPktSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfRxPktSz.setStatus("mandatory")
_StarfrPVCEndptPerfTxpktSz_Type = Integer32
_StarfrPVCEndptPerfTxpktSz_Object = MibTableColumn
starfrPVCEndptPerfTxpktSz = _StarfrPVCEndptPerfTxpktSz_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 6),
    _StarfrPVCEndptPerfTxpktSz_Type()
)
starfrPVCEndptPerfTxpktSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfTxpktSz.setStatus("mandatory")
_StarfrPVCEndptPerfRxFrPs_Type = Integer32
_StarfrPVCEndptPerfRxFrPs_Object = MibTableColumn
starfrPVCEndptPerfRxFrPs = _StarfrPVCEndptPerfRxFrPs_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 7),
    _StarfrPVCEndptPerfRxFrPs_Type()
)
starfrPVCEndptPerfRxFrPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfRxFrPs.setStatus("mandatory")
_StarfrPVCEndptPerfTxFrPs_Type = Integer32
_StarfrPVCEndptPerfTxFrPs_Object = MibTableColumn
starfrPVCEndptPerfTxFrPs = _StarfrPVCEndptPerfTxFrPs_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 8),
    _StarfrPVCEndptPerfTxFrPs_Type()
)
starfrPVCEndptPerfTxFrPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfTxFrPs.setStatus("mandatory")
_StarfrPVCEndptPerfRxKbps_Type = Integer32
_StarfrPVCEndptPerfRxKbps_Object = MibTableColumn
starfrPVCEndptPerfRxKbps = _StarfrPVCEndptPerfRxKbps_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 9),
    _StarfrPVCEndptPerfRxKbps_Type()
)
starfrPVCEndptPerfRxKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfRxKbps.setStatus("mandatory")
_StarfrPVCEndptPerfTxKbps_Type = Integer32
_StarfrPVCEndptPerfTxKbps_Object = MibTableColumn
starfrPVCEndptPerfTxKbps = _StarfrPVCEndptPerfTxKbps_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 10),
    _StarfrPVCEndptPerfTxKbps_Type()
)
starfrPVCEndptPerfTxKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfTxKbps.setStatus("mandatory")
_StarfrPVCEndptPerfRxUt_Type = Integer32
_StarfrPVCEndptPerfRxUt_Object = MibTableColumn
starfrPVCEndptPerfRxUt = _StarfrPVCEndptPerfRxUt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 11),
    _StarfrPVCEndptPerfRxUt_Type()
)
starfrPVCEndptPerfRxUt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfRxUt.setStatus("mandatory")
_StarfrPVCEndptPerfTxUt_Type = Integer32
_StarfrPVCEndptPerfTxUt_Object = MibTableColumn
starfrPVCEndptPerfTxUt = _StarfrPVCEndptPerfTxUt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 1, 3, 1, 12),
    _StarfrPVCEndptPerfTxUt_Type()
)
starfrPVCEndptPerfTxUt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starfrPVCEndptPerfTxUt.setStatus("mandatory")
_StarFiuSscsInfo_ObjectIdentity = ObjectIdentity
starFiuSscsInfo = _StarFiuSscsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2)
)
_StarFiuSscsIfInfoTbl_Object = MibTable
starFiuSscsIfInfoTbl = _StarFiuSscsIfInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1)
)
if mibBuilder.loadTexts:
    starFiuSscsIfInfoTbl.setStatus("mandatory")
_StarFiuSscsIfInfoEntry_Object = MibTableRow
starFiuSscsIfInfoEntry = _StarFiuSscsIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1)
)
starFiuSscsIfInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starFiuIfInfoSlotId"),
    (0, "STARNE-MIB", "starFiuIfInfoPortId"),
)
if mibBuilder.loadTexts:
    starFiuSscsIfInfoEntry.setStatus("mandatory")
_StarFiuIfInfoSlotId_Type = Integer32
_StarFiuIfInfoSlotId_Object = MibTableColumn
starFiuIfInfoSlotId = _StarFiuIfInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 1),
    _StarFiuIfInfoSlotId_Type()
)
starFiuIfInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuIfInfoSlotId.setStatus("mandatory")
_StarFiuIfInfoPortId_Type = Integer32
_StarFiuIfInfoPortId_Object = MibTableColumn
starFiuIfInfoPortId = _StarFiuIfInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 2),
    _StarFiuIfInfoPortId_Type()
)
starFiuIfInfoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuIfInfoPortId.setStatus("mandatory")


class _StarFiuFrcsIfAdminStatus_Type(Integer32):
    """Custom type starFiuFrcsIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defined", 1),
          ("out-of-service", 3),
          ("undefined", 2))
    )


_StarFiuFrcsIfAdminStatus_Type.__name__ = "Integer32"
_StarFiuFrcsIfAdminStatus_Object = MibTableColumn
starFiuFrcsIfAdminStatus = _StarFiuFrcsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 3),
    _StarFiuFrcsIfAdminStatus_Type()
)
starFiuFrcsIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfAdminStatus.setStatus("mandatory")


class _StarFiuFrcsIfOperStatus_Type(Integer32):
    """Custom type starFiuFrcsIfOperStatus based on Integer32"""
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


_StarFiuFrcsIfOperStatus_Type.__name__ = "Integer32"
_StarFiuFrcsIfOperStatus_Object = MibTableColumn
starFiuFrcsIfOperStatus = _StarFiuFrcsIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 4),
    _StarFiuFrcsIfOperStatus_Type()
)
starFiuFrcsIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfOperStatus.setStatus("mandatory")
_StarFiuFrcsIfLastChange_Type = Integer32
_StarFiuFrcsIfLastChange_Object = MibTableColumn
starFiuFrcsIfLastChange = _StarFiuFrcsIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 5),
    _StarFiuFrcsIfLastChange_Type()
)
starFiuFrcsIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfLastChange.setStatus("mandatory")
_StarFiuFrcsIfInOctets_Type = Integer32
_StarFiuFrcsIfInOctets_Object = MibTableColumn
starFiuFrcsIfInOctets = _StarFiuFrcsIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 6),
    _StarFiuFrcsIfInOctets_Type()
)
starFiuFrcsIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfInOctets.setStatus("mandatory")
_StarFiuFrcsIfInUcastPkts_Type = Integer32
_StarFiuFrcsIfInUcastPkts_Object = MibTableColumn
starFiuFrcsIfInUcastPkts = _StarFiuFrcsIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 7),
    _StarFiuFrcsIfInUcastPkts_Type()
)
starFiuFrcsIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfInUcastPkts.setStatus("mandatory")
_StarFiuFrcsIfInDiscards_Type = Integer32
_StarFiuFrcsIfInDiscards_Object = MibTableColumn
starFiuFrcsIfInDiscards = _StarFiuFrcsIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 8),
    _StarFiuFrcsIfInDiscards_Type()
)
starFiuFrcsIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfInDiscards.setStatus("mandatory")
_StarFiuFrcsIfInErrors_Type = Integer32
_StarFiuFrcsIfInErrors_Object = MibTableColumn
starFiuFrcsIfInErrors = _StarFiuFrcsIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 9),
    _StarFiuFrcsIfInErrors_Type()
)
starFiuFrcsIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfInErrors.setStatus("mandatory")
_StarFiuFrcsIfOutOctets_Type = Integer32
_StarFiuFrcsIfOutOctets_Object = MibTableColumn
starFiuFrcsIfOutOctets = _StarFiuFrcsIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 10),
    _StarFiuFrcsIfOutOctets_Type()
)
starFiuFrcsIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfOutOctets.setStatus("mandatory")
_StarFiuFrcsIfOutUcastPkts_Type = Integer32
_StarFiuFrcsIfOutUcastPkts_Object = MibTableColumn
starFiuFrcsIfOutUcastPkts = _StarFiuFrcsIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 11),
    _StarFiuFrcsIfOutUcastPkts_Type()
)
starFiuFrcsIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfOutUcastPkts.setStatus("mandatory")
_StarFiuFrcsIfOutDiscards_Type = Integer32
_StarFiuFrcsIfOutDiscards_Object = MibTableColumn
starFiuFrcsIfOutDiscards = _StarFiuFrcsIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 12),
    _StarFiuFrcsIfOutDiscards_Type()
)
starFiuFrcsIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfOutDiscards.setStatus("mandatory")
_StarFiuFrcsIfOutErrors_Type = Integer32
_StarFiuFrcsIfOutErrors_Object = MibTableColumn
starFiuFrcsIfOutErrors = _StarFiuFrcsIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 1, 1, 13),
    _StarFiuFrcsIfOutErrors_Type()
)
starFiuFrcsIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsIfOutErrors.setStatus("mandatory")
_StarFiuSscsPvcInfoTbl_Object = MibTable
starFiuSscsPvcInfoTbl = _StarFiuSscsPvcInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2)
)
if mibBuilder.loadTexts:
    starFiuSscsPvcInfoTbl.setStatus("mandatory")
_StarFiuSscsPvcInfoEntry_Object = MibTableRow
starFiuSscsPvcInfoEntry = _StarFiuSscsPvcInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1)
)
starFiuSscsPvcInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starFiuPvcInfoSlotId"),
    (0, "STARNE-MIB", "starFiuPvcInfoPortId"),
    (0, "STARNE-MIB", "starFiuPvcInfoDlci"),
)
if mibBuilder.loadTexts:
    starFiuSscsPvcInfoEntry.setStatus("mandatory")
_StarFiuPvcInfoSlotId_Type = Integer32
_StarFiuPvcInfoSlotId_Object = MibTableColumn
starFiuPvcInfoSlotId = _StarFiuPvcInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 1),
    _StarFiuPvcInfoSlotId_Type()
)
starFiuPvcInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuPvcInfoSlotId.setStatus("mandatory")
_StarFiuPvcInfoPortId_Type = Integer32
_StarFiuPvcInfoPortId_Object = MibTableColumn
starFiuPvcInfoPortId = _StarFiuPvcInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 2),
    _StarFiuPvcInfoPortId_Type()
)
starFiuPvcInfoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuPvcInfoPortId.setStatus("mandatory")
_StarFiuPvcInfoDlci_Type = Integer32
_StarFiuPvcInfoDlci_Object = MibTableColumn
starFiuPvcInfoDlci = _StarFiuPvcInfoDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 3),
    _StarFiuPvcInfoDlci_Type()
)
starFiuPvcInfoDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuPvcInfoDlci.setStatus("mandatory")
_StarFiuFrcsPvcEndptInFrames_Type = Integer32
_StarFiuFrcsPvcEndptInFrames_Object = MibTableColumn
starFiuFrcsPvcEndptInFrames = _StarFiuFrcsPvcEndptInFrames_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 4),
    _StarFiuFrcsPvcEndptInFrames_Type()
)
starFiuFrcsPvcEndptInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptInFrames.setStatus("mandatory")
_StarFiuFrcsPvcEndptOutFrames_Type = Integer32
_StarFiuFrcsPvcEndptOutFrames_Object = MibTableColumn
starFiuFrcsPvcEndptOutFrames = _StarFiuFrcsPvcEndptOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 5),
    _StarFiuFrcsPvcEndptOutFrames_Type()
)
starFiuFrcsPvcEndptOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptOutFrames.setStatus("mandatory")
_StarFiuFrcsPvcEndptInOctets_Type = Integer32
_StarFiuFrcsPvcEndptInOctets_Object = MibTableColumn
starFiuFrcsPvcEndptInOctets = _StarFiuFrcsPvcEndptInOctets_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 6),
    _StarFiuFrcsPvcEndptInOctets_Type()
)
starFiuFrcsPvcEndptInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptInOctets.setStatus("mandatory")
_StarFiuFrcsPvcEndptOutOctets_Type = Integer32
_StarFiuFrcsPvcEndptOutOctets_Object = MibTableColumn
starFiuFrcsPvcEndptOutOctets = _StarFiuFrcsPvcEndptOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 7),
    _StarFiuFrcsPvcEndptOutOctets_Type()
)
starFiuFrcsPvcEndptOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptOutOctets.setStatus("mandatory")


class _StarFiuFrcsPvcConnectAdminStatus_Type(Integer32):
    """Custom type starFiuFrcsPvcConnectAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defined", 1),
          ("out-of-service", 3),
          ("undefined", 2))
    )


_StarFiuFrcsPvcConnectAdminStatus_Type.__name__ = "Integer32"
_StarFiuFrcsPvcConnectAdminStatus_Object = MibTableColumn
starFiuFrcsPvcConnectAdminStatus = _StarFiuFrcsPvcConnectAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 8),
    _StarFiuFrcsPvcConnectAdminStatus_Type()
)
starFiuFrcsPvcConnectAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcConnectAdminStatus.setStatus("mandatory")


class _StarFiuFrcsPvcEndptOperStatus_Type(Integer32):
    """Custom type starFiuFrcsPvcEndptOperStatus based on Integer32"""
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


_StarFiuFrcsPvcEndptOperStatus_Type.__name__ = "Integer32"
_StarFiuFrcsPvcEndptOperStatus_Object = MibTableColumn
starFiuFrcsPvcEndptOperStatus = _StarFiuFrcsPvcEndptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 9),
    _StarFiuFrcsPvcEndptOperStatus_Type()
)
starFiuFrcsPvcEndptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptOperStatus.setStatus("mandatory")
_StarFiuFrcsPvcEndptLastChange_Type = Integer32
_StarFiuFrcsPvcEndptLastChange_Object = MibTableColumn
starFiuFrcsPvcEndptLastChange = _StarFiuFrcsPvcEndptLastChange_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 10),
    _StarFiuFrcsPvcEndptLastChange_Type()
)
starFiuFrcsPvcEndptLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptLastChange.setStatus("mandatory")
_StarFiuFrcsPvcTxVp_Type = Integer32
_StarFiuFrcsPvcTxVp_Object = MibTableColumn
starFiuFrcsPvcTxVp = _StarFiuFrcsPvcTxVp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 11),
    _StarFiuFrcsPvcTxVp_Type()
)
starFiuFrcsPvcTxVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcTxVp.setStatus("mandatory")
_StarFiuFrcsPvcTxVc_Type = Integer32
_StarFiuFrcsPvcTxVc_Object = MibTableColumn
starFiuFrcsPvcTxVc = _StarFiuFrcsPvcTxVc_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 12),
    _StarFiuFrcsPvcTxVc_Type()
)
starFiuFrcsPvcTxVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcTxVc.setStatus("mandatory")
_StarFiuFrcsPvcRxVp_Type = Integer32
_StarFiuFrcsPvcRxVp_Object = MibTableColumn
starFiuFrcsPvcRxVp = _StarFiuFrcsPvcRxVp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 13),
    _StarFiuFrcsPvcRxVp_Type()
)
starFiuFrcsPvcRxVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcRxVp.setStatus("mandatory")
_StarFiuFrcsPvcRxVc_Type = Integer32
_StarFiuFrcsPvcRxVc_Object = MibTableColumn
starFiuFrcsPvcRxVc = _StarFiuFrcsPvcRxVc_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 14),
    _StarFiuFrcsPvcRxVc_Type()
)
starFiuFrcsPvcRxVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcRxVc.setStatus("mandatory")
_StarFiuFrcsPvcEndptOutOamCells_Type = Integer32
_StarFiuFrcsPvcEndptOutOamCells_Object = MibTableColumn
starFiuFrcsPvcEndptOutOamCells = _StarFiuFrcsPvcEndptOutOamCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 15),
    _StarFiuFrcsPvcEndptOutOamCells_Type()
)
starFiuFrcsPvcEndptOutOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptOutOamCells.setStatus("mandatory")
_StarFiuFrcsPvcEndptInOamCells_Type = Integer32
_StarFiuFrcsPvcEndptInOamCells_Object = MibTableColumn
starFiuFrcsPvcEndptInOamCells = _StarFiuFrcsPvcEndptInOamCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 16),
    _StarFiuFrcsPvcEndptInOamCells_Type()
)
starFiuFrcsPvcEndptInOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptInOamCells.setStatus("mandatory")
_StarFiuFrcsPvcEndptOutRawCells_Type = Integer32
_StarFiuFrcsPvcEndptOutRawCells_Object = MibTableColumn
starFiuFrcsPvcEndptOutRawCells = _StarFiuFrcsPvcEndptOutRawCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 17),
    _StarFiuFrcsPvcEndptOutRawCells_Type()
)
starFiuFrcsPvcEndptOutRawCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptOutRawCells.setStatus("mandatory")
_StarFiuFrcsPvcEndptInRawCells_Type = Integer32
_StarFiuFrcsPvcEndptInRawCells_Object = MibTableColumn
starFiuFrcsPvcEndptInRawCells = _StarFiuFrcsPvcEndptInRawCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 2, 1, 18),
    _StarFiuFrcsPvcEndptInRawCells_Type()
)
starFiuFrcsPvcEndptInRawCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuFrcsPvcEndptInRawCells.setStatus("mandatory")
_StarFiuSscsIfPerfTbl_Object = MibTable
starFiuSscsIfPerfTbl = _StarFiuSscsIfPerfTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3)
)
if mibBuilder.loadTexts:
    starFiuSscsIfPerfTbl.setStatus("mandatory")
_StarFiuSscsIfPerfTblEntry_Object = MibTableRow
starFiuSscsIfPerfTblEntry = _StarFiuSscsIfPerfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1)
)
starFiuSscsIfPerfTblEntry.setIndexNames(
    (0, "STARNE-MIB", "starFiuSscsIfPerfSlotId"),
    (0, "STARNE-MIB", "starFiuSscsIfPerfPortId"),
)
if mibBuilder.loadTexts:
    starFiuSscsIfPerfTblEntry.setStatus("mandatory")
_StarFiuSscsIfPerfSlotId_Type = Integer32
_StarFiuSscsIfPerfSlotId_Object = MibTableColumn
starFiuSscsIfPerfSlotId = _StarFiuSscsIfPerfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 1),
    _StarFiuSscsIfPerfSlotId_Type()
)
starFiuSscsIfPerfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfSlotId.setStatus("mandatory")
_StarFiuSscsIfPerfPortId_Type = Integer32
_StarFiuSscsIfPerfPortId_Object = MibTableColumn
starFiuSscsIfPerfPortId = _StarFiuSscsIfPerfPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 2),
    _StarFiuSscsIfPerfPortId_Type()
)
starFiuSscsIfPerfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfPortId.setStatus("mandatory")
_StarFiuSscsIfPerfTmStp_Type = Integer32
_StarFiuSscsIfPerfTmStp_Object = MibTableColumn
starFiuSscsIfPerfTmStp = _StarFiuSscsIfPerfTmStp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 3),
    _StarFiuSscsIfPerfTmStp_Type()
)
starFiuSscsIfPerfTmStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfTmStp.setStatus("mandatory")
_StarFiuSscsIfPerfRxPktSz_Type = Integer32
_StarFiuSscsIfPerfRxPktSz_Object = MibTableColumn
starFiuSscsIfPerfRxPktSz = _StarFiuSscsIfPerfRxPktSz_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 4),
    _StarFiuSscsIfPerfRxPktSz_Type()
)
starFiuSscsIfPerfRxPktSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfRxPktSz.setStatus("mandatory")
_StarFiuSscsIfPerfTxpktSz_Type = Integer32
_StarFiuSscsIfPerfTxpktSz_Object = MibTableColumn
starFiuSscsIfPerfTxpktSz = _StarFiuSscsIfPerfTxpktSz_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 5),
    _StarFiuSscsIfPerfTxpktSz_Type()
)
starFiuSscsIfPerfTxpktSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfTxpktSz.setStatus("mandatory")
_StarFiuSscsIfPerfRxFrPs_Type = Integer32
_StarFiuSscsIfPerfRxFrPs_Object = MibTableColumn
starFiuSscsIfPerfRxFrPs = _StarFiuSscsIfPerfRxFrPs_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 6),
    _StarFiuSscsIfPerfRxFrPs_Type()
)
starFiuSscsIfPerfRxFrPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfRxFrPs.setStatus("mandatory")
_StarFiuSscsIfPerfTxFrPs_Type = Integer32
_StarFiuSscsIfPerfTxFrPs_Object = MibTableColumn
starFiuSscsIfPerfTxFrPs = _StarFiuSscsIfPerfTxFrPs_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 7),
    _StarFiuSscsIfPerfTxFrPs_Type()
)
starFiuSscsIfPerfTxFrPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfTxFrPs.setStatus("mandatory")
_StarFiuSscsIfPerfRxKbps_Type = Integer32
_StarFiuSscsIfPerfRxKbps_Object = MibTableColumn
starFiuSscsIfPerfRxKbps = _StarFiuSscsIfPerfRxKbps_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 8),
    _StarFiuSscsIfPerfRxKbps_Type()
)
starFiuSscsIfPerfRxKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfRxKbps.setStatus("mandatory")
_StarFiuSscsIfPerfTxKbps_Type = Integer32
_StarFiuSscsIfPerfTxKbps_Object = MibTableColumn
starFiuSscsIfPerfTxKbps = _StarFiuSscsIfPerfTxKbps_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 9),
    _StarFiuSscsIfPerfTxKbps_Type()
)
starFiuSscsIfPerfTxKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfTxKbps.setStatus("mandatory")
_StarFiuSscsIfPerfRxUt_Type = Integer32
_StarFiuSscsIfPerfRxUt_Object = MibTableColumn
starFiuSscsIfPerfRxUt = _StarFiuSscsIfPerfRxUt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 10),
    _StarFiuSscsIfPerfRxUt_Type()
)
starFiuSscsIfPerfRxUt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfRxUt.setStatus("mandatory")
_StarFiuSscsIfPerfTxUt_Type = Integer32
_StarFiuSscsIfPerfTxUt_Object = MibTableColumn
starFiuSscsIfPerfTxUt = _StarFiuSscsIfPerfTxUt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 2, 3, 1, 11),
    _StarFiuSscsIfPerfTxUt_Type()
)
starFiuSscsIfPerfTxUt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuSscsIfPerfTxUt.setStatus("mandatory")
_StarFrMgmtStatisticInfoTbl_Object = MibTable
starFrMgmtStatisticInfoTbl = _StarFrMgmtStatisticInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3)
)
if mibBuilder.loadTexts:
    starFrMgmtStatisticInfoTbl.setStatus("mandatory")
_StarFrMgmtStatisticInfoEntry_Object = MibTableRow
starFrMgmtStatisticInfoEntry = _StarFrMgmtStatisticInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1)
)
starFrMgmtStatisticInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starFrMgmtStatisticSlotId"),
    (0, "STARNE-MIB", "starFrMgmtStatisticPortId"),
)
if mibBuilder.loadTexts:
    starFrMgmtStatisticInfoEntry.setStatus("mandatory")
_StarFrMgmtStatisticSlotId_Type = Integer32
_StarFrMgmtStatisticSlotId_Object = MibTableColumn
starFrMgmtStatisticSlotId = _StarFrMgmtStatisticSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 1),
    _StarFrMgmtStatisticSlotId_Type()
)
starFrMgmtStatisticSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrMgmtStatisticSlotId.setStatus("mandatory")
_StarFrMgmtStatisticPortId_Type = Integer32
_StarFrMgmtStatisticPortId_Object = MibTableColumn
starFrMgmtStatisticPortId = _StarFrMgmtStatisticPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 2),
    _StarFrMgmtStatisticPortId_Type()
)
starFrMgmtStatisticPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrMgmtStatisticPortId.setStatus("mandatory")
_StarFrlMgtInKeepalive_Type = Integer32
_StarFrlMgtInKeepalive_Object = MibTableColumn
starFrlMgtInKeepalive = _StarFrlMgtInKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 3),
    _StarFrlMgtInKeepalive_Type()
)
starFrlMgtInKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtInKeepalive.setStatus("mandatory")
_StarFrlMgtOutKeepalive_Type = Integer32
_StarFrlMgtOutKeepalive_Object = MibTableColumn
starFrlMgtOutKeepalive = _StarFrlMgtOutKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 4),
    _StarFrlMgtOutKeepalive_Type()
)
starFrlMgtOutKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtOutKeepalive.setStatus("mandatory")
_StarFrlMgtInStatus_Type = Integer32
_StarFrlMgtInStatus_Object = MibTableColumn
starFrlMgtInStatus = _StarFrlMgtInStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 5),
    _StarFrlMgtInStatus_Type()
)
starFrlMgtInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtInStatus.setStatus("mandatory")
_StarFrlMgtOutStatus_Type = Integer32
_StarFrlMgtOutStatus_Object = MibTableColumn
starFrlMgtOutStatus = _StarFrlMgtOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 6),
    _StarFrlMgtOutStatus_Type()
)
starFrlMgtOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtOutStatus.setStatus("mandatory")
_StarFrlMgtInStatusReply_Type = Integer32
_StarFrlMgtInStatusReply_Object = MibTableColumn
starFrlMgtInStatusReply = _StarFrlMgtInStatusReply_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 7),
    _StarFrlMgtInStatusReply_Type()
)
starFrlMgtInStatusReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtInStatusReply.setStatus("mandatory")
_StarFrlMgtOutStatusReply_Type = Integer32
_StarFrlMgtOutStatusReply_Object = MibTableColumn
starFrlMgtOutStatusReply = _StarFrlMgtOutStatusReply_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 8),
    _StarFrlMgtOutStatusReply_Type()
)
starFrlMgtOutStatusReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtOutStatusReply.setStatus("mandatory")
_StarFrlMgtInAsyncUpdates_Type = Integer32
_StarFrlMgtInAsyncUpdates_Object = MibTableColumn
starFrlMgtInAsyncUpdates = _StarFrlMgtInAsyncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 9),
    _StarFrlMgtInAsyncUpdates_Type()
)
starFrlMgtInAsyncUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtInAsyncUpdates.setStatus("mandatory")
_StarFrlMgtOutAsyncUpdates_Type = Integer32
_StarFrlMgtOutAsyncUpdates_Object = MibTableColumn
starFrlMgtOutAsyncUpdates = _StarFrlMgtOutAsyncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 10),
    _StarFrlMgtOutAsyncUpdates_Type()
)
starFrlMgtOutAsyncUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtOutAsyncUpdates.setStatus("mandatory")
_StarFrlMgtNoMismatchSeqNo_Type = Integer32
_StarFrlMgtNoMismatchSeqNo_Object = MibTableColumn
starFrlMgtNoMismatchSeqNo = _StarFrlMgtNoMismatchSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 11),
    _StarFrlMgtNoMismatchSeqNo_Type()
)
starFrlMgtNoMismatchSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtNoMismatchSeqNo.setStatus("mandatory")
_StarFrlMgtNoT392TimeOut_Type = Integer32
_StarFrlMgtNoT392TimeOut_Object = MibTableColumn
starFrlMgtNoT392TimeOut = _StarFrlMgtNoT392TimeOut_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 12),
    _StarFrlMgtNoT392TimeOut_Type()
)
starFrlMgtNoT392TimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtNoT392TimeOut.setStatus("mandatory")
_StarFrlMgtNoRecvErDlci_Type = Integer32
_StarFrlMgtNoRecvErDlci_Object = MibTableColumn
starFrlMgtNoRecvErDlci = _StarFrlMgtNoRecvErDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 13),
    _StarFrlMgtNoRecvErDlci_Type()
)
starFrlMgtNoRecvErDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtNoRecvErDlci.setStatus("mandatory")
_StarFrlMgtLastRecvErDlci_Type = Integer32
_StarFrlMgtLastRecvErDlci_Object = MibTableColumn
starFrlMgtLastRecvErDlci = _StarFrlMgtLastRecvErDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 3, 1, 14),
    _StarFrlMgtLastRecvErDlci_Type()
)
starFrlMgtLastRecvErDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrlMgtLastRecvErDlci.setStatus("mandatory")
_StarFiuPmInfo_ObjectIdentity = ObjectIdentity
starFiuPmInfo = _StarFiuPmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 4)
)
_StarFrHdlcPmInfoTbl_Object = MibTable
starFrHdlcPmInfoTbl = _StarFrHdlcPmInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 4, 1)
)
if mibBuilder.loadTexts:
    starFrHdlcPmInfoTbl.setStatus("mandatory")
_StarFrHdlcPmInfoEntry_Object = MibTableRow
starFrHdlcPmInfoEntry = _StarFrHdlcPmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 4, 1, 1)
)
starFrHdlcPmInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starFrHdlcPmSlotId"),
    (0, "STARNE-MIB", "starFrHdlcPmPortId"),
)
if mibBuilder.loadTexts:
    starFrHdlcPmInfoEntry.setStatus("mandatory")
_StarFrHdlcPmSlotId_Type = Integer32
_StarFrHdlcPmSlotId_Object = MibTableColumn
starFrHdlcPmSlotId = _StarFrHdlcPmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 4, 1, 1, 1),
    _StarFrHdlcPmSlotId_Type()
)
starFrHdlcPmSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrHdlcPmSlotId.setStatus("mandatory")
_StarFrHdlcPmPortId_Type = Integer32
_StarFrHdlcPmPortId_Object = MibTableColumn
starFrHdlcPmPortId = _StarFrHdlcPmPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 4, 1, 1, 2),
    _StarFrHdlcPmPortId_Type()
)
starFrHdlcPmPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrHdlcPmPortId.setStatus("mandatory")
_StarFrHdlcRxOverrunCount_Type = Integer32
_StarFrHdlcRxOverrunCount_Object = MibTableColumn
starFrHdlcRxOverrunCount = _StarFrHdlcRxOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 4, 1, 1, 3),
    _StarFrHdlcRxOverrunCount_Type()
)
starFrHdlcRxOverrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrHdlcRxOverrunCount.setStatus("mandatory")
_StarFrHdlcTxUnderrunCount_Type = Integer32
_StarFrHdlcTxUnderrunCount_Object = MibTableColumn
starFrHdlcTxUnderrunCount = _StarFrHdlcTxUnderrunCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 4, 1, 1, 4),
    _StarFrHdlcTxUnderrunCount_Type()
)
starFrHdlcTxUnderrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrHdlcTxUnderrunCount.setStatus("mandatory")
_StarFrCongStatInfoTbl_Object = MibTable
starFrCongStatInfoTbl = _StarFrCongStatInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5)
)
if mibBuilder.loadTexts:
    starFrCongStatInfoTbl.setStatus("mandatory")
_StarFrCongStatInfoEntry_Object = MibTableRow
starFrCongStatInfoEntry = _StarFrCongStatInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1)
)
starFrCongStatInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starFrCongStatSlotId"),
    (0, "STARNE-MIB", "starFrCongStatPortId"),
)
if mibBuilder.loadTexts:
    starFrCongStatInfoEntry.setStatus("mandatory")
_StarFrCongStatSlotId_Type = Integer32
_StarFrCongStatSlotId_Object = MibTableColumn
starFrCongStatSlotId = _StarFrCongStatSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 1),
    _StarFrCongStatSlotId_Type()
)
starFrCongStatSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongStatSlotId.setStatus("mandatory")
_StarFrCongStatPortId_Type = Integer32
_StarFrCongStatPortId_Object = MibTableColumn
starFrCongStatPortId = _StarFrCongStatPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 2),
    _StarFrCongStatPortId_Type()
)
starFrCongStatPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongStatPortId.setStatus("mandatory")
_StarFrCongStatTimeStamp_Type = Integer32
_StarFrCongStatTimeStamp_Object = MibTableColumn
starFrCongStatTimeStamp = _StarFrCongStatTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 3),
    _StarFrCongStatTimeStamp_Type()
)
starFrCongStatTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongStatTimeStamp.setStatus("mandatory")
_StarFrCongNoRecvFECN_Type = Integer32
_StarFrCongNoRecvFECN_Object = MibTableColumn
starFrCongNoRecvFECN = _StarFrCongNoRecvFECN_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 4),
    _StarFrCongNoRecvFECN_Type()
)
starFrCongNoRecvFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongNoRecvFECN.setStatus("mandatory")
_StarFrCongNoTxFECN_Type = Integer32
_StarFrCongNoTxFECN_Object = MibTableColumn
starFrCongNoTxFECN = _StarFrCongNoTxFECN_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 5),
    _StarFrCongNoTxFECN_Type()
)
starFrCongNoTxFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongNoTxFECN.setStatus("mandatory")
_StarFrCongNoRecvBECN_Type = Integer32
_StarFrCongNoRecvBECN_Object = MibTableColumn
starFrCongNoRecvBECN = _StarFrCongNoRecvBECN_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 6),
    _StarFrCongNoRecvBECN_Type()
)
starFrCongNoRecvBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongNoRecvBECN.setStatus("mandatory")
_StarFrCongNoTxBECN_Type = Integer32
_StarFrCongNoTxBECN_Object = MibTableColumn
starFrCongNoTxBECN = _StarFrCongNoTxBECN_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 7),
    _StarFrCongNoTxBECN_Type()
)
starFrCongNoTxBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongNoTxBECN.setStatus("mandatory")
_StarFrCongNoRecvDE_Type = Integer32
_StarFrCongNoRecvDE_Object = MibTableColumn
starFrCongNoRecvDE = _StarFrCongNoRecvDE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 8),
    _StarFrCongNoRecvDE_Type()
)
starFrCongNoRecvDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongNoRecvDE.setStatus("mandatory")
_StarFrCongNoTxDE_Type = Integer32
_StarFrCongNoTxDE_Object = MibTableColumn
starFrCongNoTxDE = _StarFrCongNoTxDE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 9),
    _StarFrCongNoTxDE_Type()
)
starFrCongNoTxDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongNoTxDE.setStatus("mandatory")
_StarFrCongNoMarkDE_Type = Integer32
_StarFrCongNoMarkDE_Object = MibTableColumn
starFrCongNoMarkDE = _StarFrCongNoMarkDE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 10),
    _StarFrCongNoMarkDE_Type()
)
starFrCongNoMarkDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongNoMarkDE.setStatus("mandatory")
_StarFrCongNoDiscardWithDE_Type = Integer32
_StarFrCongNoDiscardWithDE_Object = MibTableColumn
starFrCongNoDiscardWithDE = _StarFrCongNoDiscardWithDE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 11),
    _StarFrCongNoDiscardWithDE_Type()
)
starFrCongNoDiscardWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongNoDiscardWithDE.setStatus("mandatory")
_StarFrCongNoDiscardWoutDE_Type = Integer32
_StarFrCongNoDiscardWoutDE_Object = MibTableColumn
starFrCongNoDiscardWoutDE = _StarFrCongNoDiscardWoutDE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 16, 5, 1, 12),
    _StarFrCongNoDiscardWoutDE_Type()
)
starFrCongNoDiscardWoutDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrCongNoDiscardWoutDE.setStatus("mandatory")
_StarAal5Info_ObjectIdentity = ObjectIdentity
starAal5Info = _StarAal5Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17)
)
_StarAal5ChannelStatisticsTbl_Object = MibTable
starAal5ChannelStatisticsTbl = _StarAal5ChannelStatisticsTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1)
)
if mibBuilder.loadTexts:
    starAal5ChannelStatisticsTbl.setStatus("mandatory")
_StarAal5ChannelStatisticsInfoEntry_Object = MibTableRow
starAal5ChannelStatisticsInfoEntry = _StarAal5ChannelStatisticsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1)
)
starAal5ChannelStatisticsInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starAal5ChannelStatisticsSlotIdInfo"),
    (0, "STARNE-MIB", "starAal5ChannelStatisticsChipId"),
)
if mibBuilder.loadTexts:
    starAal5ChannelStatisticsInfoEntry.setStatus("mandatory")
_StarAal5ChannelStatisticsSlotIdInfo_Type = Integer32
_StarAal5ChannelStatisticsSlotIdInfo_Object = MibTableColumn
starAal5ChannelStatisticsSlotIdInfo = _StarAal5ChannelStatisticsSlotIdInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 1),
    _StarAal5ChannelStatisticsSlotIdInfo_Type()
)
starAal5ChannelStatisticsSlotIdInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ChannelStatisticsSlotIdInfo.setStatus("mandatory")
_StarAal5ChannelStatisticsChipId_Type = Integer32
_StarAal5ChannelStatisticsChipId_Object = MibTableColumn
starAal5ChannelStatisticsChipId = _StarAal5ChannelStatisticsChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 2),
    _StarAal5ChannelStatisticsChipId_Type()
)
starAal5ChannelStatisticsChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ChannelStatisticsChipId.setStatus("mandatory")
_StarAal5NumPktsTransmitted_Type = Integer32
_StarAal5NumPktsTransmitted_Object = MibTableColumn
starAal5NumPktsTransmitted = _StarAal5NumPktsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 3),
    _StarAal5NumPktsTransmitted_Type()
)
starAal5NumPktsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumPktsTransmitted.setStatus("mandatory")
_StarAal5NumPktsReceived_Type = Integer32
_StarAal5NumPktsReceived_Object = MibTableColumn
starAal5NumPktsReceived = _StarAal5NumPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 4),
    _StarAal5NumPktsReceived_Type()
)
starAal5NumPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumPktsReceived.setStatus("mandatory")
_StarAal5NumTimesTxQueUnderrun_Type = Integer32
_StarAal5NumTimesTxQueUnderrun_Object = MibTableColumn
starAal5NumTimesTxQueUnderrun = _StarAal5NumTimesTxQueUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 5),
    _StarAal5NumTimesTxQueUnderrun_Type()
)
starAal5NumTimesTxQueUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumTimesTxQueUnderrun.setStatus("mandatory")
_StarAal5NumTimesRxQueUnderrun_Type = Integer32
_StarAal5NumTimesRxQueUnderrun_Object = MibTableColumn
starAal5NumTimesRxQueUnderrun = _StarAal5NumTimesRxQueUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 6),
    _StarAal5NumTimesRxQueUnderrun_Type()
)
starAal5NumTimesRxQueUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumTimesRxQueUnderrun.setStatus("mandatory")
_StarAal5NumTimesPktDropped_Type = Integer32
_StarAal5NumTimesPktDropped_Object = MibTableColumn
starAal5NumTimesPktDropped = _StarAal5NumTimesPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 7),
    _StarAal5NumTimesPktDropped_Type()
)
starAal5NumTimesPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumTimesPktDropped.setStatus("mandatory")
_StarAal5NumTimesInvalidCPI_Type = Integer32
_StarAal5NumTimesInvalidCPI_Object = MibTableColumn
starAal5NumTimesInvalidCPI = _StarAal5NumTimesInvalidCPI_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 8),
    _StarAal5NumTimesInvalidCPI_Type()
)
starAal5NumTimesInvalidCPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumTimesInvalidCPI.setStatus("mandatory")
_StarAal5NumTimesLengthViolation_Type = Integer32
_StarAal5NumTimesLengthViolation_Object = MibTableColumn
starAal5NumTimesLengthViolation = _StarAal5NumTimesLengthViolation_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 9),
    _StarAal5NumTimesLengthViolation_Type()
)
starAal5NumTimesLengthViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumTimesLengthViolation.setStatus("mandatory")
_StarAal5NumTimesOverRxDataUnit_Type = Integer32
_StarAal5NumTimesOverRxDataUnit_Object = MibTableColumn
starAal5NumTimesOverRxDataUnit = _StarAal5NumTimesOverRxDataUnit_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 10),
    _StarAal5NumTimesOverRxDataUnit_Type()
)
starAal5NumTimesOverRxDataUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumTimesOverRxDataUnit.setStatus("mandatory")
_StarAal5NumTimesCRCViolation_Type = Integer32
_StarAal5NumTimesCRCViolation_Object = MibTableColumn
starAal5NumTimesCRCViolation = _StarAal5NumTimesCRCViolation_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 11),
    _StarAal5NumTimesCRCViolation_Type()
)
starAal5NumTimesCRCViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumTimesCRCViolation.setStatus("mandatory")
_StarAal5NumTimesTimerExpire_Type = Integer32
_StarAal5NumTimesTimerExpire_Object = MibTableColumn
starAal5NumTimesTimerExpire = _StarAal5NumTimesTimerExpire_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 1, 1, 12),
    _StarAal5NumTimesTimerExpire_Type()
)
starAal5NumTimesTimerExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumTimesTimerExpire.setStatus("mandatory")
_StarAal5StatusTbl_Object = MibTable
starAal5StatusTbl = _StarAal5StatusTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 2)
)
if mibBuilder.loadTexts:
    starAal5StatusTbl.setStatus("mandatory")
_StarAal5StatusInfoEntry_Object = MibTableRow
starAal5StatusInfoEntry = _StarAal5StatusInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 2, 1)
)
starAal5StatusInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starAal5ChannelStatusSlotIdInfo"),
    (0, "STARNE-MIB", "starAal5ChannelStatusChipId"),
)
if mibBuilder.loadTexts:
    starAal5StatusInfoEntry.setStatus("mandatory")
_StarAal5ChannelStatusSlotIdInfo_Type = Integer32
_StarAal5ChannelStatusSlotIdInfo_Object = MibTableColumn
starAal5ChannelStatusSlotIdInfo = _StarAal5ChannelStatusSlotIdInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 2, 1, 1),
    _StarAal5ChannelStatusSlotIdInfo_Type()
)
starAal5ChannelStatusSlotIdInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ChannelStatusSlotIdInfo.setStatus("mandatory")
_StarAal5ChannelStatusChipId_Type = Integer32
_StarAal5ChannelStatusChipId_Object = MibTableColumn
starAal5ChannelStatusChipId = _StarAal5ChannelStatusChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 2, 1, 2),
    _StarAal5ChannelStatusChipId_Type()
)
starAal5ChannelStatusChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ChannelStatusChipId.setStatus("mandatory")
_StarAal5NumPktsQuedToTransmit_Type = Integer32
_StarAal5NumPktsQuedToTransmit_Object = MibTableColumn
starAal5NumPktsQuedToTransmit = _StarAal5NumPktsQuedToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 2, 1, 3),
    _StarAal5NumPktsQuedToTransmit_Type()
)
starAal5NumPktsQuedToTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumPktsQuedToTransmit.setStatus("mandatory")
_StarAal5NumTxChannelsOpened_Type = Integer32
_StarAal5NumTxChannelsOpened_Object = MibTableColumn
starAal5NumTxChannelsOpened = _StarAal5NumTxChannelsOpened_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 2, 1, 4),
    _StarAal5NumTxChannelsOpened_Type()
)
starAal5NumTxChannelsOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumTxChannelsOpened.setStatus("mandatory")
_StarAal5NumRxChannelsOpened_Type = Integer32
_StarAal5NumRxChannelsOpened_Object = MibTableColumn
starAal5NumRxChannelsOpened = _StarAal5NumRxChannelsOpened_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 2, 1, 5),
    _StarAal5NumRxChannelsOpened_Type()
)
starAal5NumRxChannelsOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumRxChannelsOpened.setStatus("mandatory")
_StarAal5ConfigTxVCTbl_Object = MibTable
starAal5ConfigTxVCTbl = _StarAal5ConfigTxVCTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3)
)
if mibBuilder.loadTexts:
    starAal5ConfigTxVCTbl.setStatus("mandatory")
_StarAal5ConfigTxVCInfoEntry_Object = MibTableRow
starAal5ConfigTxVCInfoEntry = _StarAal5ConfigTxVCInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1)
)
starAal5ConfigTxVCInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starAal5ConfigTxVCSlotIdInfo"),
    (0, "STARNE-MIB", "starAal5ConfigTxVCChipId"),
    (0, "STARNE-MIB", "starAal5ConfigTxVPIndex"),
    (0, "STARNE-MIB", "starAal5ConfigTxVCIndex"),
)
if mibBuilder.loadTexts:
    starAal5ConfigTxVCInfoEntry.setStatus("mandatory")
_StarAal5ConfigTxVCSlotIdInfo_Type = Integer32
_StarAal5ConfigTxVCSlotIdInfo_Object = MibTableColumn
starAal5ConfigTxVCSlotIdInfo = _StarAal5ConfigTxVCSlotIdInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 1),
    _StarAal5ConfigTxVCSlotIdInfo_Type()
)
starAal5ConfigTxVCSlotIdInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ConfigTxVCSlotIdInfo.setStatus("mandatory")
_StarAal5ConfigTxVCChipId_Type = Integer32
_StarAal5ConfigTxVCChipId_Object = MibTableColumn
starAal5ConfigTxVCChipId = _StarAal5ConfigTxVCChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 2),
    _StarAal5ConfigTxVCChipId_Type()
)
starAal5ConfigTxVCChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ConfigTxVCChipId.setStatus("mandatory")
_StarAal5ConfigTxVPIndex_Type = Integer32
_StarAal5ConfigTxVPIndex_Object = MibTableColumn
starAal5ConfigTxVPIndex = _StarAal5ConfigTxVPIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 3),
    _StarAal5ConfigTxVPIndex_Type()
)
starAal5ConfigTxVPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ConfigTxVPIndex.setStatus("mandatory")
_StarAal5ConfigTxVCIndex_Type = Integer32
_StarAal5ConfigTxVCIndex_Object = MibTableColumn
starAal5ConfigTxVCIndex = _StarAal5ConfigTxVCIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 4),
    _StarAal5ConfigTxVCIndex_Type()
)
starAal5ConfigTxVCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ConfigTxVCIndex.setStatus("mandatory")
_StarAal5TxVCChannelType_Type = Integer32
_StarAal5TxVCChannelType_Object = MibTableColumn
starAal5TxVCChannelType = _StarAal5TxVCChannelType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 5),
    _StarAal5TxVCChannelType_Type()
)
starAal5TxVCChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5TxVCChannelType.setStatus("mandatory")
_StarAal5CpcsUU_Type = Integer32
_StarAal5CpcsUU_Object = MibTableColumn
starAal5CpcsUU = _StarAal5CpcsUU_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 6),
    _StarAal5CpcsUU_Type()
)
starAal5CpcsUU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5CpcsUU.setStatus("mandatory")
_StarAal5AvgI_Type = Integer32
_StarAal5AvgI_Object = MibTableColumn
starAal5AvgI = _StarAal5AvgI_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 7),
    _StarAal5AvgI_Type()
)
starAal5AvgI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5AvgI.setStatus("mandatory")
_StarAal5AvgM_Type = Integer32
_StarAal5AvgM_Object = MibTableColumn
starAal5AvgM = _StarAal5AvgM_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 8),
    _StarAal5AvgM_Type()
)
starAal5AvgM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5AvgM.setStatus("mandatory")
_StarAal5PeakRate_Type = Integer32
_StarAal5PeakRate_Object = MibTableColumn
starAal5PeakRate = _StarAal5PeakRate_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 9),
    _StarAal5PeakRate_Type()
)
starAal5PeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5PeakRate.setStatus("mandatory")
_StarAal5MaxBurst_Type = Integer32
_StarAal5MaxBurst_Object = MibTableColumn
starAal5MaxBurst = _StarAal5MaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 10),
    _StarAal5MaxBurst_Type()
)
starAal5MaxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5MaxBurst.setStatus("mandatory")
_StarAal5Priority_Type = Integer32
_StarAal5Priority_Object = MibTableColumn
starAal5Priority = _StarAal5Priority_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 3, 1, 11),
    _StarAal5Priority_Type()
)
starAal5Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5Priority.setStatus("mandatory")
_StarAal5ConfigRxVCTbl_Object = MibTable
starAal5ConfigRxVCTbl = _StarAal5ConfigRxVCTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4)
)
if mibBuilder.loadTexts:
    starAal5ConfigRxVCTbl.setStatus("mandatory")
_StarAal5ConfigRxVCInfoEntry_Object = MibTableRow
starAal5ConfigRxVCInfoEntry = _StarAal5ConfigRxVCInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4, 1)
)
starAal5ConfigRxVCInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starAal5ConfigRxVCSlotIdInfo"),
    (0, "STARNE-MIB", "starAal5ConfigRxVCChipId"),
    (0, "STARNE-MIB", "starAal5ConfigRxVPIndex"),
    (0, "STARNE-MIB", "starAal5ConfigRxVCIndex"),
)
if mibBuilder.loadTexts:
    starAal5ConfigRxVCInfoEntry.setStatus("mandatory")
_StarAal5ConfigRxVCSlotIdInfo_Type = Integer32
_StarAal5ConfigRxVCSlotIdInfo_Object = MibTableColumn
starAal5ConfigRxVCSlotIdInfo = _StarAal5ConfigRxVCSlotIdInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4, 1, 1),
    _StarAal5ConfigRxVCSlotIdInfo_Type()
)
starAal5ConfigRxVCSlotIdInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ConfigRxVCSlotIdInfo.setStatus("mandatory")
_StarAal5ConfigRxVCChipId_Type = Integer32
_StarAal5ConfigRxVCChipId_Object = MibTableColumn
starAal5ConfigRxVCChipId = _StarAal5ConfigRxVCChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4, 1, 2),
    _StarAal5ConfigRxVCChipId_Type()
)
starAal5ConfigRxVCChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ConfigRxVCChipId.setStatus("mandatory")
_StarAal5ConfigRxVPIndex_Type = Integer32
_StarAal5ConfigRxVPIndex_Object = MibTableColumn
starAal5ConfigRxVPIndex = _StarAal5ConfigRxVPIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4, 1, 3),
    _StarAal5ConfigRxVPIndex_Type()
)
starAal5ConfigRxVPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ConfigRxVPIndex.setStatus("mandatory")
_StarAal5ConfigRxVCIndex_Type = Integer32
_StarAal5ConfigRxVCIndex_Object = MibTableColumn
starAal5ConfigRxVCIndex = _StarAal5ConfigRxVCIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4, 1, 4),
    _StarAal5ConfigRxVCIndex_Type()
)
starAal5ConfigRxVCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5ConfigRxVCIndex.setStatus("mandatory")
_StarAal5PoolNum_Type = Integer32
_StarAal5PoolNum_Object = MibTableColumn
starAal5PoolNum = _StarAal5PoolNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4, 1, 5),
    _StarAal5PoolNum_Type()
)
starAal5PoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5PoolNum.setStatus("mandatory")
_StarAal5NumOAMDrops_Type = Integer32
_StarAal5NumOAMDrops_Object = MibTableColumn
starAal5NumOAMDrops = _StarAal5NumOAMDrops_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4, 1, 6),
    _StarAal5NumOAMDrops_Type()
)
starAal5NumOAMDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5NumOAMDrops.setStatus("mandatory")
_StarAal5RxVCChannelType_Type = Integer32
_StarAal5RxVCChannelType_Object = MibTableColumn
starAal5RxVCChannelType = _StarAal5RxVCChannelType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4, 1, 7),
    _StarAal5RxVCChannelType_Type()
)
starAal5RxVCChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5RxVCChannelType.setStatus("mandatory")
_StarAal5MaxNumSegments_Type = Integer32
_StarAal5MaxNumSegments_Object = MibTableColumn
starAal5MaxNumSegments = _StarAal5MaxNumSegments_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 17, 4, 1, 8),
    _StarAal5MaxNumSegments_Type()
)
starAal5MaxNumSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAal5MaxNumSegments.setStatus("mandatory")
_StarRout88Info_ObjectIdentity = ObjectIdentity
starRout88Info = _StarRout88Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18)
)
_StarRoutInfoTbl_Object = MibTable
starRoutInfoTbl = _StarRoutInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1)
)
if mibBuilder.loadTexts:
    starRoutInfoTbl.setStatus("mandatory")
_StarRoutInfoEntry_Object = MibTableRow
starRoutInfoEntry = _StarRoutInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1)
)
starRoutInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIdRoutInfo"),
    (0, "STARNE-MIB", "starRoutChipId"),
)
if mibBuilder.loadTexts:
    starRoutInfoEntry.setStatus("mandatory")
_StarSlotIdRoutInfo_Type = Integer32
_StarSlotIdRoutInfo_Object = MibTableColumn
starSlotIdRoutInfo = _StarSlotIdRoutInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 1),
    _StarSlotIdRoutInfo_Type()
)
starSlotIdRoutInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotIdRoutInfo.setStatus("mandatory")
_StarRoutChipId_Type = Integer32
_StarRoutChipId_Object = MibTableColumn
starRoutChipId = _StarRoutChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 2),
    _StarRoutChipId_Type()
)
starRoutChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutChipId.setStatus("mandatory")


class _StarRoutCurrentState_Type(Integer32):
    """Custom type starRoutCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("operational", 2))
    )


_StarRoutCurrentState_Type.__name__ = "Integer32"
_StarRoutCurrentState_Object = MibTableColumn
starRoutCurrentState = _StarRoutCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 3),
    _StarRoutCurrentState_Type()
)
starRoutCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutCurrentState.setStatus("mandatory")
_StarRoutChipVersion_Type = Integer32
_StarRoutChipVersion_Object = MibTableColumn
starRoutChipVersion = _StarRoutChipVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 4),
    _StarRoutChipVersion_Type()
)
starRoutChipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutChipVersion.setStatus("mandatory")


class _StarRoutSramConfig_Type(Integer32):
    """Custom type starRoutSramConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ram2x128x8", 2),
          ("ram2x32x8", 1),
          ("ram4x128x8", 3))
    )


_StarRoutSramConfig_Type.__name__ = "Integer32"
_StarRoutSramConfig_Object = MibTableColumn
starRoutSramConfig = _StarRoutSramConfig_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 5),
    _StarRoutSramConfig_Type()
)
starRoutSramConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutSramConfig.setStatus("mandatory")


class _StarRoutBckPressureDly_Type(Integer32):
    """Custom type starRoutBckPressureDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clk2Delay", 2),
          ("clk4Delay", 3),
          ("noDelay", 1))
    )


_StarRoutBckPressureDly_Type.__name__ = "Integer32"
_StarRoutBckPressureDly_Object = MibTableColumn
starRoutBckPressureDly = _StarRoutBckPressureDly_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 6),
    _StarRoutBckPressureDly_Type()
)
starRoutBckPressureDly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutBckPressureDly.setStatus("mandatory")
_StarRoutNumVpi_Type = Integer32
_StarRoutNumVpi_Object = MibTableColumn
starRoutNumVpi = _StarRoutNumVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 7),
    _StarRoutNumVpi_Type()
)
starRoutNumVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutNumVpi.setStatus("mandatory")


class _StarRoutConnectToSar_Type(Integer32):
    """Custom type starRoutConnectToSar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectPHY", 1),
          ("connectSAR", 2))
    )


_StarRoutConnectToSar_Type.__name__ = "Integer32"
_StarRoutConnectToSar_Object = MibTableColumn
starRoutConnectToSar = _StarRoutConnectToSar_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 8),
    _StarRoutConnectToSar_Type()
)
starRoutConnectToSar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutConnectToSar.setStatus("mandatory")
_StarRoutWatchDogConfig_Type = Integer32
_StarRoutWatchDogConfig_Object = MibTableColumn
starRoutWatchDogConfig = _StarRoutWatchDogConfig_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 9),
    _StarRoutWatchDogConfig_Type()
)
starRoutWatchDogConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutWatchDogConfig.setStatus("mandatory")


class _StarRoutEmptyQstate_Type(Integer32):
    """Custom type starRoutEmptyQstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inCongestion", 1),
          ("notInCongestion", 2))
    )


_StarRoutEmptyQstate_Type.__name__ = "Integer32"
_StarRoutEmptyQstate_Object = MibTableColumn
starRoutEmptyQstate = _StarRoutEmptyQstate_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 10),
    _StarRoutEmptyQstate_Type()
)
starRoutEmptyQstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutEmptyQstate.setStatus("mandatory")
_StarRoutTxMarkedCellCnt_Type = Counter32
_StarRoutTxMarkedCellCnt_Object = MibTableColumn
starRoutTxMarkedCellCnt = _StarRoutTxMarkedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 11),
    _StarRoutTxMarkedCellCnt_Type()
)
starRoutTxMarkedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutTxMarkedCellCnt.setStatus("mandatory")
_StarRoutRxMarkedCellCnt_Type = Counter32
_StarRoutRxMarkedCellCnt_Object = MibTableColumn
starRoutRxMarkedCellCnt = _StarRoutRxMarkedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 12),
    _StarRoutRxMarkedCellCnt_Type()
)
starRoutRxMarkedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutRxMarkedCellCnt.setStatus("mandatory")
_StarRoutTxParityFailCnt_Type = Counter32
_StarRoutTxParityFailCnt_Object = MibTableColumn
starRoutTxParityFailCnt = _StarRoutTxParityFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 13),
    _StarRoutTxParityFailCnt_Type()
)
starRoutTxParityFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutTxParityFailCnt.setStatus("mandatory")
_StarRoutBpIgnoredCnt_Type = Counter32
_StarRoutBpIgnoredCnt_Object = MibTableColumn
starRoutBpIgnoredCnt = _StarRoutBpIgnoredCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 14),
    _StarRoutBpIgnoredCnt_Type()
)
starRoutBpIgnoredCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutBpIgnoredCnt.setStatus("mandatory")
_StarRoutLiveFailCnt_Type = Counter32
_StarRoutLiveFailCnt_Object = MibTableColumn
starRoutLiveFailCnt = _StarRoutLiveFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 15),
    _StarRoutLiveFailCnt_Type()
)
starRoutLiveFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutLiveFailCnt.setStatus("mandatory")
_StarRoutWdFailCnt_Type = Counter32
_StarRoutWdFailCnt_Object = MibTableColumn
starRoutWdFailCnt = _StarRoutWdFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 16),
    _StarRoutWdFailCnt_Type()
)
starRoutWdFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutWdFailCnt.setStatus("mandatory")
_StarRoutEmptyQCongQd_Type = Integer32
_StarRoutEmptyQCongQd_Object = MibTableColumn
starRoutEmptyQCongQd = _StarRoutEmptyQCongQd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 17),
    _StarRoutEmptyQCongQd_Type()
)
starRoutEmptyQCongQd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutEmptyQCongQd.setStatus("mandatory")
_StarRoutEmptyQCurQd_Type = Integer32
_StarRoutEmptyQCurQd_Object = MibTableColumn
starRoutEmptyQCurQd = _StarRoutEmptyQCurQd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 18),
    _StarRoutEmptyQCurQd_Type()
)
starRoutEmptyQCurQd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutEmptyQCurQd.setStatus("mandatory")
_StarRoutRatioAOrder1_Type = Integer32
_StarRoutRatioAOrder1_Object = MibTableColumn
starRoutRatioAOrder1 = _StarRoutRatioAOrder1_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 19),
    _StarRoutRatioAOrder1_Type()
)
starRoutRatioAOrder1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutRatioAOrder1.setStatus("mandatory")
_StarRoutRatioBOrder1_Type = Integer32
_StarRoutRatioBOrder1_Object = MibTableColumn
starRoutRatioBOrder1 = _StarRoutRatioBOrder1_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 20),
    _StarRoutRatioBOrder1_Type()
)
starRoutRatioBOrder1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutRatioBOrder1.setStatus("mandatory")
_StarRoutRatioAOrder2_Type = Integer32
_StarRoutRatioAOrder2_Object = MibTableColumn
starRoutRatioAOrder2 = _StarRoutRatioAOrder2_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 21),
    _StarRoutRatioAOrder2_Type()
)
starRoutRatioAOrder2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutRatioAOrder2.setStatus("mandatory")
_StarRoutRatioBOrder2_Type = Integer32
_StarRoutRatioBOrder2_Object = MibTableColumn
starRoutRatioBOrder2 = _StarRoutRatioBOrder2_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 1, 1, 22),
    _StarRoutRatioBOrder2_Type()
)
starRoutRatioBOrder2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutRatioBOrder2.setStatus("mandatory")
_StarRoutPrioQInfoTbl_Object = MibTable
starRoutPrioQInfoTbl = _StarRoutPrioQInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2)
)
if mibBuilder.loadTexts:
    starRoutPrioQInfoTbl.setStatus("mandatory")
_StarRoutPrioQInfoEntry_Object = MibTableRow
starRoutPrioQInfoEntry = _StarRoutPrioQInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2, 1)
)
starRoutPrioQInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIdPrioQInfo"),
    (0, "STARNE-MIB", "starPrioQRoutChipId"),
    (0, "STARNE-MIB", "starRoutPrioQType"),
)
if mibBuilder.loadTexts:
    starRoutPrioQInfoEntry.setStatus("mandatory")
_StarSlotIdPrioQInfo_Type = Integer32
_StarSlotIdPrioQInfo_Object = MibTableColumn
starSlotIdPrioQInfo = _StarSlotIdPrioQInfo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2, 1, 1),
    _StarSlotIdPrioQInfo_Type()
)
starSlotIdPrioQInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSlotIdPrioQInfo.setStatus("mandatory")
_StarPrioQRoutChipId_Type = Integer32
_StarPrioQRoutChipId_Object = MibTableColumn
starPrioQRoutChipId = _StarPrioQRoutChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2, 1, 2),
    _StarPrioQRoutChipId_Type()
)
starPrioQRoutChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPrioQRoutChipId.setStatus("mandatory")


class _StarRoutPrioQType_Type(Integer32):
    """Custom type starRoutPrioQType based on Integer32"""
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
        *(("highPriorityA", 1),
          ("highPriorityB", 6),
          ("multicastQueue", 2),
          ("oamReceiveQ", 7),
          ("pba", 3),
          ("pbb", 4),
          ("pbc", 5))
    )


_StarRoutPrioQType_Type.__name__ = "Integer32"
_StarRoutPrioQType_Object = MibTableColumn
starRoutPrioQType = _StarRoutPrioQType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2, 1, 3),
    _StarRoutPrioQType_Type()
)
starRoutPrioQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutPrioQType.setStatus("mandatory")
_StarRoutPerPrioMaximumQd_Type = Integer32
_StarRoutPerPrioMaximumQd_Object = MibTableColumn
starRoutPerPrioMaximumQd = _StarRoutPerPrioMaximumQd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2, 1, 4),
    _StarRoutPerPrioMaximumQd_Type()
)
starRoutPerPrioMaximumQd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutPerPrioMaximumQd.setStatus("mandatory")
_StarRoutPerPrioCongestionQd_Type = Integer32
_StarRoutPerPrioCongestionQd_Object = MibTableColumn
starRoutPerPrioCongestionQd = _StarRoutPerPrioCongestionQd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2, 1, 5),
    _StarRoutPerPrioCongestionQd_Type()
)
starRoutPerPrioCongestionQd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutPerPrioCongestionQd.setStatus("mandatory")
_StarRoutPerPrioCurrentQd_Type = Integer32
_StarRoutPerPrioCurrentQd_Object = MibTableColumn
starRoutPerPrioCurrentQd = _StarRoutPerPrioCurrentQd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2, 1, 6),
    _StarRoutPerPrioCurrentQd_Type()
)
starRoutPerPrioCurrentQd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutPerPrioCurrentQd.setStatus("mandatory")


class _StarRoutIsQCongested_Type(Integer32):
    """Custom type starRoutIsQCongested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qCongested", 1),
          ("qNotCongested", 2))
    )


_StarRoutIsQCongested_Type.__name__ = "Integer32"
_StarRoutIsQCongested_Object = MibTableColumn
starRoutIsQCongested = _StarRoutIsQCongested_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2, 1, 7),
    _StarRoutIsQCongested_Type()
)
starRoutIsQCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutIsQCongested.setStatus("mandatory")


class _StarRoutIsCellInQueue_Type(Integer32):
    """Custom type starRoutIsCellInQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cellNotPresent", 2),
          ("cellPresent", 1))
    )


_StarRoutIsCellInQueue_Type.__name__ = "Integer32"
_StarRoutIsCellInQueue_Object = MibTableColumn
starRoutIsCellInQueue = _StarRoutIsCellInQueue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 2, 1, 8),
    _StarRoutIsCellInQueue_Type()
)
starRoutIsCellInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutIsCellInQueue.setStatus("mandatory")
_StarRoutCcbInfoTbl_Object = MibTable
starRoutCcbInfoTbl = _StarRoutCcbInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3)
)
if mibBuilder.loadTexts:
    starRoutCcbInfoTbl.setStatus("mandatory")
_StarRoutCcbInfoEntry_Object = MibTableRow
starRoutCcbInfoEntry = _StarRoutCcbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1)
)
starRoutCcbInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starCcbInfoSlotId"),
    (0, "STARNE-MIB", "starCcbRoutChipId"),
    (0, "STARNE-MIB", "starRoutVp"),
    (0, "STARNE-MIB", "starRoutVc"),
)
if mibBuilder.loadTexts:
    starRoutCcbInfoEntry.setStatus("mandatory")
_StarCcbInfoSlotId_Type = Integer32
_StarCcbInfoSlotId_Object = MibTableColumn
starCcbInfoSlotId = _StarCcbInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 1),
    _StarCcbInfoSlotId_Type()
)
starCcbInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCcbInfoSlotId.setStatus("mandatory")
_StarCcbRoutChipId_Type = Integer32
_StarCcbRoutChipId_Object = MibTableColumn
starCcbRoutChipId = _StarCcbRoutChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 2),
    _StarCcbRoutChipId_Type()
)
starCcbRoutChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCcbRoutChipId.setStatus("mandatory")
_StarRoutVp_Type = Integer32
_StarRoutVp_Object = MibTableColumn
starRoutVp = _StarRoutVp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 3),
    _StarRoutVp_Type()
)
starRoutVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutVp.setStatus("mandatory")
_StarRoutVc_Type = Integer32
_StarRoutVc_Object = MibTableColumn
starRoutVc = _StarRoutVc_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 4),
    _StarRoutVc_Type()
)
starRoutVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutVc.setStatus("mandatory")


class _StarRoutEnClpDrop_Type(Integer32):
    """Custom type starRoutEnClpDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disablesClpDrop", 2),
          ("enablesClpDrop", 1))
    )


_StarRoutEnClpDrop_Type.__name__ = "Integer32"
_StarRoutEnClpDrop_Object = MibTableColumn
starRoutEnClpDrop = _StarRoutEnClpDrop_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 5),
    _StarRoutEnClpDrop_Type()
)
starRoutEnClpDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRoutEnClpDrop.setStatus("mandatory")


class _StarRoutEnAal5Epd_Type(Integer32):
    """Custom type starRoutEnAal5Epd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disablesAal5Discard", 2),
          ("enablesAal5Discard", 1))
    )


_StarRoutEnAal5Epd_Type.__name__ = "Integer32"
_StarRoutEnAal5Epd_Object = MibTableColumn
starRoutEnAal5Epd = _StarRoutEnAal5Epd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 6),
    _StarRoutEnAal5Epd_Type()
)
starRoutEnAal5Epd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRoutEnAal5Epd.setStatus("mandatory")


class _StarRoutEnEfciMark_Type(Integer32):
    """Custom type starRoutEnEfciMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disablesEfciMarking", 2),
          ("enablesEfciMarking", 1))
    )


_StarRoutEnEfciMark_Type.__name__ = "Integer32"
_StarRoutEnEfciMark_Object = MibTableColumn
starRoutEnEfciMark = _StarRoutEnEfciMark_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 7),
    _StarRoutEnEfciMark_Type()
)
starRoutEnEfciMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRoutEnEfciMark.setStatus("mandatory")


class _StarRoutEnExtDrop_Type(Integer32):
    """Custom type starRoutEnExtDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disablesExtDrop", 2),
          ("enablesExtDrop", 1))
    )


_StarRoutEnExtDrop_Type.__name__ = "Integer32"
_StarRoutEnExtDrop_Object = MibTableColumn
starRoutEnExtDrop = _StarRoutEnExtDrop_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 8),
    _StarRoutEnExtDrop_Type()
)
starRoutEnExtDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRoutEnExtDrop.setStatus("mandatory")


class _StarRoutPti7_Type(Integer32):
    """Custom type starRoutPti7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passPti", 2),
          ("putPti", 1))
    )


_StarRoutPti7_Type.__name__ = "Integer32"
_StarRoutPti7_Object = MibTableColumn
starRoutPti7 = _StarRoutPti7_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 9),
    _StarRoutPti7_Type()
)
starRoutPti7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRoutPti7.setStatus("mandatory")


class _StarRoutPti6_Type(Integer32):
    """Custom type starRoutPti6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passPti", 2),
          ("putPti", 1))
    )


_StarRoutPti6_Type.__name__ = "Integer32"
_StarRoutPti6_Object = MibTableColumn
starRoutPti6 = _StarRoutPti6_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 10),
    _StarRoutPti6_Type()
)
starRoutPti6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRoutPti6.setStatus("mandatory")


class _StarRoutPti5_Type(Integer32):
    """Custom type starRoutPti5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passPti", 2),
          ("putPti", 1))
    )


_StarRoutPti5_Type.__name__ = "Integer32"
_StarRoutPti5_Object = MibTableColumn
starRoutPti5 = _StarRoutPti5_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 11),
    _StarRoutPti5_Type()
)
starRoutPti5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRoutPti5.setStatus("mandatory")


class _StarRoutPti4_Type(Integer32):
    """Custom type starRoutPti4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passPti", 2),
          ("putPti", 1))
    )


_StarRoutPti4_Type.__name__ = "Integer32"
_StarRoutPti4_Object = MibTableColumn
starRoutPti4 = _StarRoutPti4_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 12),
    _StarRoutPti4_Type()
)
starRoutPti4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRoutPti4.setStatus("mandatory")


class _StarRoutCcbQueue_Type(Integer32):
    """Custom type starRoutCcbQueue based on Integer32"""
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
        *(("highPriorityA", 1),
          ("highPriorityB", 6),
          ("multicastQueue", 2),
          ("oamReceiveQ", 7),
          ("pbA", 3),
          ("pbB", 4),
          ("pbC", 5))
    )


_StarRoutCcbQueue_Type.__name__ = "Integer32"
_StarRoutCcbQueue_Object = MibTableColumn
starRoutCcbQueue = _StarRoutCcbQueue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 13),
    _StarRoutCcbQueue_Type()
)
starRoutCcbQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutCcbQueue.setStatus("mandatory")
_StarRoutMaxPerVcQd_Type = Integer32
_StarRoutMaxPerVcQd_Object = MibTableColumn
starRoutMaxPerVcQd = _StarRoutMaxPerVcQd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 14),
    _StarRoutMaxPerVcQd_Type()
)
starRoutMaxPerVcQd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutMaxPerVcQd.setStatus("mandatory")
_StarRoutCongPerVcQd_Type = Integer32
_StarRoutCongPerVcQd_Object = MibTableColumn
starRoutCongPerVcQd = _StarRoutCongPerVcQd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 15),
    _StarRoutCongPerVcQd_Type()
)
starRoutCongPerVcQd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutCongPerVcQd.setStatus("mandatory")
_StarRoutCurPerVcQd_Type = Integer32
_StarRoutCurPerVcQd_Object = MibTableColumn
starRoutCurPerVcQd = _StarRoutCurPerVcQd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 16),
    _StarRoutCurPerVcQd_Type()
)
starRoutCurPerVcQd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutCurPerVcQd.setStatus("mandatory")


class _StarRoutTags_Type(OctetString):
    """Custom type starRoutTags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_StarRoutTags_Type.__name__ = "OctetString"
_StarRoutTags_Object = MibTableColumn
starRoutTags = _StarRoutTags_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 17),
    _StarRoutTags_Type()
)
starRoutTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutTags.setStatus("mandatory")


class _StarRoutIsVpTranslated_Type(Integer32):
    """Custom type starRoutIsVpTranslated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotTranslateVP", 2),
          ("translateVP", 1))
    )


_StarRoutIsVpTranslated_Type.__name__ = "Integer32"
_StarRoutIsVpTranslated_Object = MibTableColumn
starRoutIsVpTranslated = _StarRoutIsVpTranslated_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 18),
    _StarRoutIsVpTranslated_Type()
)
starRoutIsVpTranslated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutIsVpTranslated.setStatus("mandatory")


class _StarRoutIsVcTranslated_Type(Integer32):
    """Custom type starRoutIsVcTranslated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotTranslateVC", 2),
          ("translateVC", 1))
    )


_StarRoutIsVcTranslated_Type.__name__ = "Integer32"
_StarRoutIsVcTranslated_Object = MibTableColumn
starRoutIsVcTranslated = _StarRoutIsVcTranslated_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 19),
    _StarRoutIsVcTranslated_Type()
)
starRoutIsVcTranslated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutIsVcTranslated.setStatus("mandatory")
_StarRoutNewVp_Type = Integer32
_StarRoutNewVp_Object = MibTableColumn
starRoutNewVp = _StarRoutNewVp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 20),
    _StarRoutNewVp_Type()
)
starRoutNewVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutNewVp.setStatus("mandatory")
_StarRoutNewVc_Type = Integer32
_StarRoutNewVc_Object = MibTableColumn
starRoutNewVc = _StarRoutNewVc_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 21),
    _StarRoutNewVc_Type()
)
starRoutNewVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutNewVc.setStatus("mandatory")
_StarRoutCellRxCnt_Type = Counter32
_StarRoutCellRxCnt_Object = MibTableColumn
starRoutCellRxCnt = _StarRoutCellRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 22),
    _StarRoutCellRxCnt_Type()
)
starRoutCellRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutCellRxCnt.setStatus("mandatory")
_StarRoutCellsDrpdCnt_Type = Counter32
_StarRoutCellsDrpdCnt_Object = MibTableColumn
starRoutCellsDrpdCnt = _StarRoutCellsDrpdCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 23),
    _StarRoutCellsDrpdCnt_Type()
)
starRoutCellsDrpdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutCellsDrpdCnt.setStatus("mandatory")
_StarRoutCongCellCnt_Type = Counter32
_StarRoutCongCellCnt_Object = MibTableColumn
starRoutCongCellCnt = _StarRoutCongCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 18, 3, 1, 24),
    _StarRoutCongCellCnt_Type()
)
starRoutCongCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRoutCongCellCnt.setStatus("mandatory")
_StarHdlcControllerInfo_ObjectIdentity = ObjectIdentity
starHdlcControllerInfo = _StarHdlcControllerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19)
)
_StarFiuHdlcStatusTbl_Object = MibTable
starFiuHdlcStatusTbl = _StarFiuHdlcStatusTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1)
)
if mibBuilder.loadTexts:
    starFiuHdlcStatusTbl.setStatus("mandatory")
_StarFiuHdlcStatusInfoEntry_Object = MibTableRow
starFiuHdlcStatusInfoEntry = _StarFiuHdlcStatusInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1)
)
starFiuHdlcStatusInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starFiuHdlcStatusSlotId"),
    (0, "STARNE-MIB", "starFiuHdlcStatusChipId"),
)
if mibBuilder.loadTexts:
    starFiuHdlcStatusInfoEntry.setStatus("mandatory")
_StarFiuHdlcStatusSlotId_Type = Integer32
_StarFiuHdlcStatusSlotId_Object = MibTableColumn
starFiuHdlcStatusSlotId = _StarFiuHdlcStatusSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 1),
    _StarFiuHdlcStatusSlotId_Type()
)
starFiuHdlcStatusSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcStatusSlotId.setStatus("mandatory")
_StarFiuHdlcStatusChipId_Type = Integer32
_StarFiuHdlcStatusChipId_Object = MibTableColumn
starFiuHdlcStatusChipId = _StarFiuHdlcStatusChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 2),
    _StarFiuHdlcStatusChipId_Type()
)
starFiuHdlcStatusChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcStatusChipId.setStatus("mandatory")
_StarFiuHdlcRxBuffOverFlow_Type = Integer32
_StarFiuHdlcRxBuffOverFlow_Object = MibTableColumn
starFiuHdlcRxBuffOverFlow = _StarFiuHdlcRxBuffOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 3),
    _StarFiuHdlcRxBuffOverFlow_Type()
)
starFiuHdlcRxBuffOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcRxBuffOverFlow.setStatus("mandatory")
_StarFiuHdlcRxCountOverflow_Type = Integer32
_StarFiuHdlcRxCountOverflow_Object = MibTableColumn
starFiuHdlcRxCountOverflow = _StarFiuHdlcRxCountOverflow_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 4),
    _StarFiuHdlcRxCountOverflow_Type()
)
starFiuHdlcRxCountOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcRxCountOverflow.setStatus("mandatory")
_StarFiuHdlcRxShort_Type = Integer32
_StarFiuHdlcRxShort_Object = MibTableColumn
starFiuHdlcRxShort = _StarFiuHdlcRxShort_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 5),
    _StarFiuHdlcRxShort_Type()
)
starFiuHdlcRxShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcRxShort.setStatus("mandatory")
_StarFiuHdlcRxAbort_Type = Integer32
_StarFiuHdlcRxAbort_Object = MibTableColumn
starFiuHdlcRxAbort = _StarFiuHdlcRxAbort_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 6),
    _StarFiuHdlcRxAbort_Type()
)
starFiuHdlcRxAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcRxAbort.setStatus("mandatory")
_StarFiuHdlcRxOverrun_Type = Integer32
_StarFiuHdlcRxOverrun_Object = MibTableColumn
starFiuHdlcRxOverrun = _StarFiuHdlcRxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 7),
    _StarFiuHdlcRxOverrun_Type()
)
starFiuHdlcRxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcRxOverrun.setStatus("mandatory")
_StarFiuHdlcRxCrc_Type = Integer32
_StarFiuHdlcRxCrc_Object = MibTableColumn
starFiuHdlcRxCrc = _StarFiuHdlcRxCrc_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 8),
    _StarFiuHdlcRxCrc_Type()
)
starFiuHdlcRxCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcRxCrc.setStatus("mandatory")
_StarFiuHdlcRxPduCount_Type = Integer32
_StarFiuHdlcRxPduCount_Object = MibTableColumn
starFiuHdlcRxPduCount = _StarFiuHdlcRxPduCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 9),
    _StarFiuHdlcRxPduCount_Type()
)
starFiuHdlcRxPduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcRxPduCount.setStatus("mandatory")
_StarFiuHdlcRxByteCount_Type = Integer32
_StarFiuHdlcRxByteCount_Object = MibTableColumn
starFiuHdlcRxByteCount = _StarFiuHdlcRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 10),
    _StarFiuHdlcRxByteCount_Type()
)
starFiuHdlcRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcRxByteCount.setStatus("mandatory")
_StarFiuHdlcTxUnderrun_Type = Integer32
_StarFiuHdlcTxUnderrun_Object = MibTableColumn
starFiuHdlcTxUnderrun = _StarFiuHdlcTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 11),
    _StarFiuHdlcTxUnderrun_Type()
)
starFiuHdlcTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcTxUnderrun.setStatus("mandatory")
_StarFiuHdlcTxPduCount_Type = Integer32
_StarFiuHdlcTxPduCount_Object = MibTableColumn
starFiuHdlcTxPduCount = _StarFiuHdlcTxPduCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 12),
    _StarFiuHdlcTxPduCount_Type()
)
starFiuHdlcTxPduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcTxPduCount.setStatus("mandatory")
_StarFiuHdlcTxByteCount_Type = Integer32
_StarFiuHdlcTxByteCount_Object = MibTableColumn
starFiuHdlcTxByteCount = _StarFiuHdlcTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 13),
    _StarFiuHdlcTxByteCount_Type()
)
starFiuHdlcTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcTxByteCount.setStatus("mandatory")
_StarFiuHdlcLinkstatus_Type = Integer32
_StarFiuHdlcLinkstatus_Object = MibTableColumn
starFiuHdlcLinkstatus = _StarFiuHdlcLinkstatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 14),
    _StarFiuHdlcLinkstatus_Type()
)
starFiuHdlcLinkstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcLinkstatus.setStatus("mandatory")
_StarFiuHdlcTxBuffOverFlow_Type = Integer32
_StarFiuHdlcTxBuffOverFlow_Object = MibTableColumn
starFiuHdlcTxBuffOverFlow = _StarFiuHdlcTxBuffOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 15),
    _StarFiuHdlcTxBuffOverFlow_Type()
)
starFiuHdlcTxBuffOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcTxBuffOverFlow.setStatus("mandatory")
_StarFiuHdlcTxCountOverflow_Type = Integer32
_StarFiuHdlcTxCountOverflow_Object = MibTableColumn
starFiuHdlcTxCountOverflow = _StarFiuHdlcTxCountOverflow_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 19, 1, 1, 16),
    _StarFiuHdlcTxCountOverflow_Type()
)
starFiuHdlcTxCountOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFiuHdlcTxCountOverflow.setStatus("mandatory")
_StarRclInfo_ObjectIdentity = ObjectIdentity
starRclInfo = _StarRclInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20)
)
_StarRclInfoTbl_Object = MibTable
starRclInfoTbl = _StarRclInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1)
)
if mibBuilder.loadTexts:
    starRclInfoTbl.setStatus("mandatory")
_StarRclInfoEntry_Object = MibTableRow
starRclInfoEntry = _StarRclInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1)
)
starRclInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starRclInfoSlotId"),
)
if mibBuilder.loadTexts:
    starRclInfoEntry.setStatus("mandatory")
_StarRclInfoSlotId_Type = Integer32
_StarRclInfoSlotId_Object = MibTableColumn
starRclInfoSlotId = _StarRclInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 1),
    _StarRclInfoSlotId_Type()
)
starRclInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclInfoSlotId.setStatus("mandatory")
_StarRclNumRegAppl_Type = Integer32
_StarRclNumRegAppl_Object = MibTableColumn
starRclNumRegAppl = _StarRclNumRegAppl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 2),
    _StarRclNumRegAppl_Type()
)
starRclNumRegAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclNumRegAppl.setStatus("mandatory")
_StarRclNumSwitchovers_Type = Integer32
_StarRclNumSwitchovers_Object = MibTableColumn
starRclNumSwitchovers = _StarRclNumSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 3),
    _StarRclNumSwitchovers_Type()
)
starRclNumSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclNumSwitchovers.setStatus("mandatory")
_StarRclSwitchoverThreshold_Type = Integer32
_StarRclSwitchoverThreshold_Object = MibTableColumn
starRclSwitchoverThreshold = _StarRclSwitchoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 4),
    _StarRclSwitchoverThreshold_Type()
)
starRclSwitchoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRclSwitchoverThreshold.setStatus("mandatory")
_StarRclSwitchoverTimeLimit_Type = Integer32
_StarRclSwitchoverTimeLimit_Object = MibTableColumn
starRclSwitchoverTimeLimit = _StarRclSwitchoverTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 5),
    _StarRclSwitchoverTimeLimit_Type()
)
starRclSwitchoverTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRclSwitchoverTimeLimit.setStatus("mandatory")
_StarRclSwitchoverResetTime_Type = Integer32
_StarRclSwitchoverResetTime_Object = MibTableColumn
starRclSwitchoverResetTime = _StarRclSwitchoverResetTime_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 6),
    _StarRclSwitchoverResetTime_Type()
)
starRclSwitchoverResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRclSwitchoverResetTime.setStatus("mandatory")


class _StarRclLockoutFlag_Type(Integer32):
    """Custom type starRclLockoutFlag based on Integer32"""
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


_StarRclLockoutFlag_Type.__name__ = "Integer32"
_StarRclLockoutFlag_Object = MibTableColumn
starRclLockoutFlag = _StarRclLockoutFlag_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 7),
    _StarRclLockoutFlag_Type()
)
starRclLockoutFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRclLockoutFlag.setStatus("mandatory")


class _StarRclHmcTestStatus_Type(Integer32):
    """Custom type starRclHmcTestStatus based on Integer32"""
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
        *(("idle", 1),
          ("initiateTest", 4),
          ("testInProgress", 2),
          ("testInitiatedByOtherModule", 3))
    )


_StarRclHmcTestStatus_Type.__name__ = "Integer32"
_StarRclHmcTestStatus_Object = MibTableColumn
starRclHmcTestStatus = _StarRclHmcTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 8),
    _StarRclHmcTestStatus_Type()
)
starRclHmcTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRclHmcTestStatus.setStatus("mandatory")


class _StarRclHmcTestResult_Type(Integer32):
    """Custom type starRclHmcTestResult based on Integer32"""
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
        *(("testCancelDueToStateChange", 2),
          ("testCancelDueToTimeout", 3),
          ("testFail", 4),
          ("testSuccess", 1))
    )


_StarRclHmcTestResult_Type.__name__ = "Integer32"
_StarRclHmcTestResult_Object = MibTableColumn
starRclHmcTestResult = _StarRclHmcTestResult_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 9),
    _StarRclHmcTestResult_Type()
)
starRclHmcTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclHmcTestResult.setStatus("mandatory")


class _StarRclModuleStatus_Type(Integer32):
    """Custom type starRclModuleStatus based on Integer32"""
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
        *(("active", 2),
          ("init", 1),
          ("standalone", 4),
          ("standby", 3))
    )


_StarRclModuleStatus_Type.__name__ = "Integer32"
_StarRclModuleStatus_Object = MibTableColumn
starRclModuleStatus = _StarRclModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 10),
    _StarRclModuleStatus_Type()
)
starRclModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starRclModuleStatus.setStatus("mandatory")


class _StarRclSwitchoverReason_Type(Integer32):
    """Custom type starRclSwitchoverReason based on Integer32"""
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
        *(("cpuFail", 3),
          ("eject", 1),
          ("hmcRegisterFail", 10),
          ("hmcdTestFail", 9),
          ("powerFail", 2),
          ("rcldHealthCheckFail", 8),
          ("redundantModuleUp", 5),
          ("requestFromNms", 7),
          ("requestFromRednModule", 6),
          ("reset", 4))
    )


_StarRclSwitchoverReason_Type.__name__ = "Integer32"
_StarRclSwitchoverReason_Object = MibTableColumn
starRclSwitchoverReason = _StarRclSwitchoverReason_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 11),
    _StarRclSwitchoverReason_Type()
)
starRclSwitchoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclSwitchoverReason.setStatus("mandatory")
_StarRclSwitchoverTime_Type = Integer32
_StarRclSwitchoverTime_Object = MibTableColumn
starRclSwitchoverTime = _StarRclSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 1, 1, 12),
    _StarRclSwitchoverTime_Type()
)
starRclSwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclSwitchoverTime.setStatus("mandatory")
_StarRclRegInfoTbl_Object = MibTable
starRclRegInfoTbl = _StarRclRegInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 2)
)
if mibBuilder.loadTexts:
    starRclRegInfoTbl.setStatus("mandatory")
_StarRclRegInfoEntry_Object = MibTableRow
starRclRegInfoEntry = _StarRclRegInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 2, 1)
)
starRclRegInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starRclRegInfoSlotId"),
    (0, "STARNE-MIB", "starRclRegKey"),
)
if mibBuilder.loadTexts:
    starRclRegInfoEntry.setStatus("mandatory")
_StarRclRegInfoSlotId_Type = Integer32
_StarRclRegInfoSlotId_Object = MibTableColumn
starRclRegInfoSlotId = _StarRclRegInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 2, 1, 1),
    _StarRclRegInfoSlotId_Type()
)
starRclRegInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclRegInfoSlotId.setStatus("mandatory")
_StarRclRegKey_Type = Integer32
_StarRclRegKey_Object = MibTableColumn
starRclRegKey = _StarRclRegKey_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 2, 1, 2),
    _StarRclRegKey_Type()
)
starRclRegKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclRegKey.setStatus("mandatory")


class _StarRclRegTaskName_Type(OctetString):
    """Custom type starRclRegTaskName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_StarRclRegTaskName_Type.__name__ = "OctetString"
_StarRclRegTaskName_Object = MibTableColumn
starRclRegTaskName = _StarRclRegTaskName_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 2, 1, 3),
    _StarRclRegTaskName_Type()
)
starRclRegTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclRegTaskName.setStatus("mandatory")


class _StarRclRegQueueName_Type(OctetString):
    """Custom type starRclRegQueueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_StarRclRegQueueName_Type.__name__ = "OctetString"
_StarRclRegQueueName_Object = MibTableColumn
starRclRegQueueName = _StarRclRegQueueName_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 20, 2, 1, 4),
    _StarRclRegQueueName_Type()
)
starRclRegQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRclRegQueueName.setStatus("mandatory")
_StarCasInfo_ObjectIdentity = ObjectIdentity
starCasInfo = _StarCasInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21)
)
_StarCasStatusInfoTbl_Object = MibTable
starCasStatusInfoTbl = _StarCasStatusInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 1)
)
if mibBuilder.loadTexts:
    starCasStatusInfoTbl.setStatus("mandatory")
_StarCasStatusInfoEntry_Object = MibTableRow
starCasStatusInfoEntry = _StarCasStatusInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 1, 1)
)
starCasStatusInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starCasStatusSlotId"),
    (0, "STARNE-MIB", "starCasStatusPortId"),
    (0, "STARNE-MIB", "starCasStatusChannelId"),
)
if mibBuilder.loadTexts:
    starCasStatusInfoEntry.setStatus("mandatory")
_StarCasStatusSlotId_Type = Integer32
_StarCasStatusSlotId_Object = MibTableColumn
starCasStatusSlotId = _StarCasStatusSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 1, 1, 1),
    _StarCasStatusSlotId_Type()
)
starCasStatusSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusSlotId.setStatus("mandatory")
_StarCasStatusPortId_Type = Integer32
_StarCasStatusPortId_Object = MibTableColumn
starCasStatusPortId = _StarCasStatusPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 1, 1, 2),
    _StarCasStatusPortId_Type()
)
starCasStatusPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusPortId.setStatus("mandatory")
_StarCasStatusChannelId_Type = Integer32
_StarCasStatusChannelId_Object = MibTableColumn
starCasStatusChannelId = _StarCasStatusChannelId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 1, 1, 3),
    _StarCasStatusChannelId_Type()
)
starCasStatusChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusChannelId.setStatus("mandatory")
_StarCasStatusConfigured_Type = Integer32
_StarCasStatusConfigured_Object = MibTableColumn
starCasStatusConfigured = _StarCasStatusConfigured_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 1, 1, 4),
    _StarCasStatusConfigured_Type()
)
starCasStatusConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusConfigured.setStatus("mandatory")
_StarCasStatusCurrentStatus_Type = Integer32
_StarCasStatusCurrentStatus_Object = MibTableColumn
starCasStatusCurrentStatus = _StarCasStatusCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 1, 1, 5),
    _StarCasStatusCurrentStatus_Type()
)
starCasStatusCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusCurrentStatus.setStatus("mandatory")
_StarCasStatusStatusChange_Type = Integer32
_StarCasStatusStatusChange_Object = MibTableColumn
starCasStatusStatusChange = _StarCasStatusStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 1, 1, 6),
    _StarCasStatusStatusChange_Type()
)
starCasStatusStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusStatusChange.setStatus("mandatory")
_StarCasStatusNewStatusSampleNum_Type = Integer32
_StarCasStatusNewStatusSampleNum_Object = MibTableColumn
starCasStatusNewStatusSampleNum = _StarCasStatusNewStatusSampleNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 1, 1, 7),
    _StarCasStatusNewStatusSampleNum_Type()
)
starCasStatusNewStatusSampleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusNewStatusSampleNum.setStatus("mandatory")
_StarCasStatusPortInfoTbl_Object = MibTable
starCasStatusPortInfoTbl = _StarCasStatusPortInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 2)
)
if mibBuilder.loadTexts:
    starCasStatusPortInfoTbl.setStatus("mandatory")
_StarCasStatusPortInfoEntry_Object = MibTableRow
starCasStatusPortInfoEntry = _StarCasStatusPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 2, 1)
)
starCasStatusPortInfoEntry.setIndexNames(
    (0, "STARNE-MIB", "starCasStatusPortSlotId"),
    (0, "STARNE-MIB", "starCasStatusPortPortId"),
)
if mibBuilder.loadTexts:
    starCasStatusPortInfoEntry.setStatus("mandatory")
_StarCasStatusPortSlotId_Type = Integer32
_StarCasStatusPortSlotId_Object = MibTableColumn
starCasStatusPortSlotId = _StarCasStatusPortSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 2, 1, 1),
    _StarCasStatusPortSlotId_Type()
)
starCasStatusPortSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusPortSlotId.setStatus("mandatory")
_StarCasStatusPortPortId_Type = Integer32
_StarCasStatusPortPortId_Object = MibTableColumn
starCasStatusPortPortId = _StarCasStatusPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 2, 1, 2),
    _StarCasStatusPortPortId_Type()
)
starCasStatusPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusPortPortId.setStatus("mandatory")
_StarCasStatusPortConfigured_Type = Integer32
_StarCasStatusPortConfigured_Object = MibTableColumn
starCasStatusPortConfigured = _StarCasStatusPortConfigured_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 2, 1, 3),
    _StarCasStatusPortConfigured_Type()
)
starCasStatusPortConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusPortConfigured.setStatus("mandatory")
_StarCasStatusPortCasSamplePeriod_Type = Integer32
_StarCasStatusPortCasSamplePeriod_Object = MibTableColumn
starCasStatusPortCasSamplePeriod = _StarCasStatusPortCasSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 2, 1, 4),
    _StarCasStatusPortCasSamplePeriod_Type()
)
starCasStatusPortCasSamplePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusPortCasSamplePeriod.setStatus("mandatory")
_StarCasStatusPortCasSampleNum_Type = Integer32
_StarCasStatusPortCasSampleNum_Object = MibTableColumn
starCasStatusPortCasSampleNum = _StarCasStatusPortCasSampleNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 21, 2, 1, 5),
    _StarCasStatusPortCasSampleNum_Type()
)
starCasStatusPortCasSampleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCasStatusPortCasSampleNum.setStatus("mandatory")
_StarCesInfo_ObjectIdentity = ObjectIdentity
starCesInfo = _StarCesInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23)
)
_StarDS1E1CESConfTable_Object = MibTable
starDS1E1CESConfTable = _StarDS1E1CESConfTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1)
)
if mibBuilder.loadTexts:
    starDS1E1CESConfTable.setStatus("mandatory")
_StarDS1E1CESConfEntry_Object = MibTableRow
starDS1E1CESConfEntry = _StarDS1E1CESConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1)
)
starDS1E1CESConfEntry.setIndexNames(
    (0, "STARNE-MIB", "starDS1E1CESSlotId"),
    (0, "STARNE-MIB", "starDS1E1CESPortId"),
    (0, "STARNE-MIB", "starDS1E1CESChannelId"),
)
if mibBuilder.loadTexts:
    starDS1E1CESConfEntry.setStatus("mandatory")
_StarDS1E1CESSlotId_Type = Integer32
_StarDS1E1CESSlotId_Object = MibTableColumn
starDS1E1CESSlotId = _StarDS1E1CESSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 1),
    _StarDS1E1CESSlotId_Type()
)
starDS1E1CESSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESSlotId.setStatus("mandatory")
_StarDS1E1CESPortId_Type = Integer32
_StarDS1E1CESPortId_Object = MibTableColumn
starDS1E1CESPortId = _StarDS1E1CESPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 2),
    _StarDS1E1CESPortId_Type()
)
starDS1E1CESPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESPortId.setStatus("mandatory")
_StarDS1E1CESChannelId_Type = Integer32
_StarDS1E1CESChannelId_Object = MibTableColumn
starDS1E1CESChannelId = _StarDS1E1CESChannelId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 3),
    _StarDS1E1CESChannelId_Type()
)
starDS1E1CESChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESChannelId.setStatus("mandatory")
_StarDS1E1CESMapATMIndex_Type = Integer32
_StarDS1E1CESMapATMIndex_Object = MibTableColumn
starDS1E1CESMapATMIndex = _StarDS1E1CESMapATMIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 4),
    _StarDS1E1CESMapATMIndex_Type()
)
starDS1E1CESMapATMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESMapATMIndex.setStatus("mandatory")
_StarDS1E1CESMapVPI_Type = Integer32
_StarDS1E1CESMapVPI_Object = MibTableColumn
starDS1E1CESMapVPI = _StarDS1E1CESMapVPI_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 5),
    _StarDS1E1CESMapVPI_Type()
)
starDS1E1CESMapVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESMapVPI.setStatus("mandatory")
_StarDS1E1CESMapVCI_Type = Integer32
_StarDS1E1CESMapVCI_Object = MibTableColumn
starDS1E1CESMapVCI = _StarDS1E1CESMapVCI_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 6),
    _StarDS1E1CESMapVCI_Type()
)
starDS1E1CESMapVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESMapVCI.setStatus("mandatory")


class _StarDS1E1CESCBRService_Type(Integer32):
    """Custom type starDS1E1CESCBRService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("structured", 2),
          ("unstructured", 1))
    )


_StarDS1E1CESCBRService_Type.__name__ = "Integer32"
_StarDS1E1CESCBRService_Object = MibTableColumn
starDS1E1CESCBRService = _StarDS1E1CESCBRService_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 7),
    _StarDS1E1CESCBRService_Type()
)
starDS1E1CESCBRService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starDS1E1CESCBRService.setStatus("mandatory")


class _StarDS1E1CESCBRClockMode_Type(Integer32):
    """Custom type starDS1E1CESCBRClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("srts", 2),
          ("synchronous", 1))
    )


_StarDS1E1CESCBRClockMode_Type.__name__ = "Integer32"
_StarDS1E1CESCBRClockMode_Object = MibTableColumn
starDS1E1CESCBRClockMode = _StarDS1E1CESCBRClockMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 8),
    _StarDS1E1CESCBRClockMode_Type()
)
starDS1E1CESCBRClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starDS1E1CESCBRClockMode.setStatus("mandatory")


class _StarDS1E1CESCas_Type(Integer32):
    """Custom type starDS1E1CESCas based on Integer32"""
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
        *(("basic", 1),
          ("ds1EsfCas", 4),
          ("ds1SfCas", 3),
          ("e1Cas", 2))
    )


_StarDS1E1CESCas_Type.__name__ = "Integer32"
_StarDS1E1CESCas_Object = MibTableColumn
starDS1E1CESCas = _StarDS1E1CESCas_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 9),
    _StarDS1E1CESCas_Type()
)
starDS1E1CESCas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starDS1E1CESCas.setStatus("mandatory")


class _StarDS1E1CESPartialFill_Type(Integer32):
    """Custom type starDS1E1CESPartialFill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_StarDS1E1CESPartialFill_Type.__name__ = "Integer32"
_StarDS1E1CESPartialFill_Object = MibTableColumn
starDS1E1CESPartialFill = _StarDS1E1CESPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 10),
    _StarDS1E1CESPartialFill_Type()
)
starDS1E1CESPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starDS1E1CESPartialFill.setStatus("mandatory")


class _StarDS1E1CESBufMaxSize_Type(Integer32):
    """Custom type starDS1E1CESBufMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_StarDS1E1CESBufMaxSize_Type.__name__ = "Integer32"
_StarDS1E1CESBufMaxSize_Object = MibTableColumn
starDS1E1CESBufMaxSize = _StarDS1E1CESBufMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 11),
    _StarDS1E1CESBufMaxSize_Type()
)
starDS1E1CESBufMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starDS1E1CESBufMaxSize.setStatus("mandatory")


class _StarDS1E1CESCDVRxT_Type(Integer32):
    """Custom type starDS1E1CESCDVRxT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StarDS1E1CESCDVRxT_Type.__name__ = "Integer32"
_StarDS1E1CESCDVRxT_Object = MibTableColumn
starDS1E1CESCDVRxT = _StarDS1E1CESCDVRxT_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 12),
    _StarDS1E1CESCDVRxT_Type()
)
starDS1E1CESCDVRxT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starDS1E1CESCDVRxT.setStatus("mandatory")


class _StarDS1E1CESCellLossIntegPrd_Type(Integer32):
    """Custom type starDS1E1CESCellLossIntegPrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_StarDS1E1CESCellLossIntegPrd_Type.__name__ = "Integer32"
_StarDS1E1CESCellLossIntegPrd_Object = MibTableColumn
starDS1E1CESCellLossIntegPrd = _StarDS1E1CESCellLossIntegPrd_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 1, 1, 13),
    _StarDS1E1CESCellLossIntegPrd_Type()
)
starDS1E1CESCellLossIntegPrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starDS1E1CESCellLossIntegPrd.setStatus("mandatory")
_StarDS1E1CESStatsTable_Object = MibTable
starDS1E1CESStatsTable = _StarDS1E1CESStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2)
)
if mibBuilder.loadTexts:
    starDS1E1CESStatsTable.setStatus("mandatory")
_StarDS1E1CESStatsEntry_Object = MibTableRow
starDS1E1CESStatsEntry = _StarDS1E1CESStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1)
)
starDS1E1CESStatsEntry.setIndexNames(
    (0, "STARNE-MIB", "starDS1E1CESStatSlotId"),
    (0, "STARNE-MIB", "starDS1E1CESStatDeviceId"),
    (0, "STARNE-MIB", "starDS1E1CESStatPortId"),
    (0, "STARNE-MIB", "starDS1E1CESStatChannelId"),
)
if mibBuilder.loadTexts:
    starDS1E1CESStatsEntry.setStatus("mandatory")
_StarDS1E1CESStatSlotId_Type = Integer32
_StarDS1E1CESStatSlotId_Object = MibTableColumn
starDS1E1CESStatSlotId = _StarDS1E1CESStatSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 1),
    _StarDS1E1CESStatSlotId_Type()
)
starDS1E1CESStatSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESStatSlotId.setStatus("mandatory")
_StarDS1E1CESStatDeviceId_Type = Integer32
_StarDS1E1CESStatDeviceId_Object = MibTableColumn
starDS1E1CESStatDeviceId = _StarDS1E1CESStatDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 2),
    _StarDS1E1CESStatDeviceId_Type()
)
starDS1E1CESStatDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESStatDeviceId.setStatus("mandatory")
_StarDS1E1CESStatPortId_Type = Integer32
_StarDS1E1CESStatPortId_Object = MibTableColumn
starDS1E1CESStatPortId = _StarDS1E1CESStatPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 3),
    _StarDS1E1CESStatPortId_Type()
)
starDS1E1CESStatPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESStatPortId.setStatus("mandatory")
_StarDS1E1CESStatChannelId_Type = Integer32
_StarDS1E1CESStatChannelId_Object = MibTableColumn
starDS1E1CESStatChannelId = _StarDS1E1CESStatChannelId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 4),
    _StarDS1E1CESStatChannelId_Type()
)
starDS1E1CESStatChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESStatChannelId.setStatus("mandatory")
_StarDS1E1CESReassCells_Type = Integer32
_StarDS1E1CESReassCells_Object = MibTableColumn
starDS1E1CESReassCells = _StarDS1E1CESReassCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 5),
    _StarDS1E1CESReassCells_Type()
)
starDS1E1CESReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESReassCells.setStatus("mandatory")
_StarDS1E1CESHdrErrors_Type = Integer32
_StarDS1E1CESHdrErrors_Object = MibTableColumn
starDS1E1CESHdrErrors = _StarDS1E1CESHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 6),
    _StarDS1E1CESHdrErrors_Type()
)
starDS1E1CESHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESHdrErrors.setStatus("mandatory")
_StarDS1E1CESPointerReframes_Type = Integer32
_StarDS1E1CESPointerReframes_Object = MibTableColumn
starDS1E1CESPointerReframes = _StarDS1E1CESPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 7),
    _StarDS1E1CESPointerReframes_Type()
)
starDS1E1CESPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESPointerReframes.setStatus("mandatory")
_StarDS1E1CESLostCells_Type = Integer32
_StarDS1E1CESLostCells_Object = MibTableColumn
starDS1E1CESLostCells = _StarDS1E1CESLostCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 8),
    _StarDS1E1CESLostCells_Type()
)
starDS1E1CESLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESLostCells.setStatus("mandatory")
_StarDS1E1CESBufUnderflows_Type = Integer32
_StarDS1E1CESBufUnderflows_Object = MibTableColumn
starDS1E1CESBufUnderflows = _StarDS1E1CESBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 9),
    _StarDS1E1CESBufUnderflows_Type()
)
starDS1E1CESBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESBufUnderflows.setStatus("mandatory")
_StarDS1E1CESBufOverflows_Type = Integer32
_StarDS1E1CESBufOverflows_Object = MibTableColumn
starDS1E1CESBufOverflows = _StarDS1E1CESBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 10),
    _StarDS1E1CESBufOverflows_Type()
)
starDS1E1CESBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESBufOverflows.setStatus("mandatory")


class _StarDS1E1CESCellLossStatus_Type(Integer32):
    """Custom type starDS1E1CESCellLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 2),
          ("noLoss", 1))
    )


_StarDS1E1CESCellLossStatus_Type.__name__ = "Integer32"
_StarDS1E1CESCellLossStatus_Object = MibTableColumn
starDS1E1CESCellLossStatus = _StarDS1E1CESCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 2, 23, 2, 1, 11),
    _StarDS1E1CESCellLossStatus_Type()
)
starDS1E1CESCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1E1CESCellLossStatus.setStatus("mandatory")
_StarPort_ObjectIdentity = ObjectIdentity
starPort = _StarPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 3)
)
_StarPortTable_Object = MibTable
starPortTable = _StarPortTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1)
)
if mibBuilder.loadTexts:
    starPortTable.setStatus("mandatory")
_StarPortEntry_Object = MibTableRow
starPortEntry = _StarPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1)
)
starPortEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starPortEntry.setStatus("mandatory")
_StarPortIndex_Type = Integer32
_StarPortIndex_Object = MibTableColumn
starPortIndex = _StarPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 1),
    _StarPortIndex_Type()
)
starPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortIndex.setStatus("mandatory")
_StarPortIfIndex_Type = Integer32
_StarPortIfIndex_Object = MibTableColumn
starPortIfIndex = _StarPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 2),
    _StarPortIfIndex_Type()
)
starPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortIfIndex.setStatus("mandatory")
_StarPortType_Type = Integer32
_StarPortType_Object = MibTableColumn
starPortType = _StarPortType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 3),
    _StarPortType_Type()
)
starPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortType.setStatus("mandatory")
_StarPortConfig_Type = Integer32
_StarPortConfig_Object = MibTableColumn
starPortConfig = _StarPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 4),
    _StarPortConfig_Type()
)
starPortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortConfig.setStatus("mandatory")
_StarPortDescr_Type = DisplayString
_StarPortDescr_Object = MibTableColumn
starPortDescr = _StarPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 5),
    _StarPortDescr_Type()
)
starPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDescr.setStatus("mandatory")
_StarPortAdminStatus_Type = Integer32
_StarPortAdminStatus_Object = MibTableColumn
starPortAdminStatus = _StarPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 6),
    _StarPortAdminStatus_Type()
)
starPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortAdminStatus.setStatus("mandatory")
_StarPortAtmAddress_Type = OctetString
_StarPortAtmAddress_Object = MibTableColumn
starPortAtmAddress = _StarPortAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 7),
    _StarPortAtmAddress_Type()
)
starPortAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortAtmAddress.setStatus("mandatory")
_StarPortLastChanged_Type = TimeTicks
_StarPortLastChanged_Object = MibTableColumn
starPortLastChanged = _StarPortLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 8),
    _StarPortLastChanged_Type()
)
starPortLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortLastChanged.setStatus("mandatory")
_StarPortAlarmStatus_Type = Integer32
_StarPortAlarmStatus_Object = MibTableColumn
starPortAlarmStatus = _StarPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 9),
    _StarPortAlarmStatus_Type()
)
starPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortAlarmStatus.setStatus("mandatory")
_StarPortRemoteAtmAddress_Type = OctetString
_StarPortRemoteAtmAddress_Object = MibTableColumn
starPortRemoteAtmAddress = _StarPortRemoteAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 10),
    _StarPortRemoteAtmAddress_Type()
)
starPortRemoteAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortRemoteAtmAddress.setStatus("mandatory")


class _StarPortOperStatus_Type(Integer32):
    """Custom type starPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-of-service", 2))
    )


_StarPortOperStatus_Type.__name__ = "Integer32"
_StarPortOperStatus_Object = MibTableColumn
starPortOperStatus = _StarPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 11),
    _StarPortOperStatus_Type()
)
starPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortOperStatus.setStatus("mandatory")
_StarPortIFType_Type = Integer32
_StarPortIFType_Object = MibTableColumn
starPortIFType = _StarPortIFType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 12),
    _StarPortIFType_Type()
)
starPortIFType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortIFType.setStatus("mandatory")
_StarPortMaxVPINumber_Type = Integer32
_StarPortMaxVPINumber_Object = MibTableColumn
starPortMaxVPINumber = _StarPortMaxVPINumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 13),
    _StarPortMaxVPINumber_Type()
)
starPortMaxVPINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortMaxVPINumber.setStatus("mandatory")
_StarPortUsedVPINumber_Type = Integer32
_StarPortUsedVPINumber_Object = MibTableColumn
starPortUsedVPINumber = _StarPortUsedVPINumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 14),
    _StarPortUsedVPINumber_Type()
)
starPortUsedVPINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUsedVPINumber.setStatus("mandatory")
_StarPortMaxVCINumber_Type = Integer32
_StarPortMaxVCINumber_Object = MibTableColumn
starPortMaxVCINumber = _StarPortMaxVCINumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 15),
    _StarPortMaxVCINumber_Type()
)
starPortMaxVCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortMaxVCINumber.setStatus("mandatory")
_StarPortUsedVCINumber_Type = Integer32
_StarPortUsedVCINumber_Object = MibTableColumn
starPortUsedVCINumber = _StarPortUsedVCINumber_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 16),
    _StarPortUsedVCINumber_Type()
)
starPortUsedVCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUsedVCINumber.setStatus("mandatory")
_StarPortMaxFixedCapacity_Type = Integer32
_StarPortMaxFixedCapacity_Object = MibTableColumn
starPortMaxFixedCapacity = _StarPortMaxFixedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 17),
    _StarPortMaxFixedCapacity_Type()
)
starPortMaxFixedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortMaxFixedCapacity.setStatus("mandatory")
_StarPortMaxVariableCapacity_Type = Integer32
_StarPortMaxVariableCapacity_Object = MibTableColumn
starPortMaxVariableCapacity = _StarPortMaxVariableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 18),
    _StarPortMaxVariableCapacity_Type()
)
starPortMaxVariableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortMaxVariableCapacity.setStatus("mandatory")
_StarPortUsedFwdFixedCapacity_Type = Integer32
_StarPortUsedFwdFixedCapacity_Object = MibTableColumn
starPortUsedFwdFixedCapacity = _StarPortUsedFwdFixedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 19),
    _StarPortUsedFwdFixedCapacity_Type()
)
starPortUsedFwdFixedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUsedFwdFixedCapacity.setStatus("mandatory")
_StarPortUsedFwdVariableCapacity_Type = Integer32
_StarPortUsedFwdVariableCapacity_Object = MibTableColumn
starPortUsedFwdVariableCapacity = _StarPortUsedFwdVariableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 20),
    _StarPortUsedFwdVariableCapacity_Type()
)
starPortUsedFwdVariableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUsedFwdVariableCapacity.setStatus("mandatory")
_StarPortUsedBwdFixedCapacity_Type = Integer32
_StarPortUsedBwdFixedCapacity_Object = MibTableColumn
starPortUsedBwdFixedCapacity = _StarPortUsedBwdFixedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 21),
    _StarPortUsedBwdFixedCapacity_Type()
)
starPortUsedBwdFixedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUsedBwdFixedCapacity.setStatus("mandatory")
_StarPortUsedBwdVariableCapacity_Type = Integer32
_StarPortUsedBwdVariableCapacity_Object = MibTableColumn
starPortUsedBwdVariableCapacity = _StarPortUsedBwdVariableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 22),
    _StarPortUsedBwdVariableCapacity_Type()
)
starPortUsedBwdVariableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUsedBwdVariableCapacity.setStatus("mandatory")
_StarPortAvailableVpi_Type = Integer32
_StarPortAvailableVpi_Object = MibTableColumn
starPortAvailableVpi = _StarPortAvailableVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 1, 1, 23),
    _StarPortAvailableVpi_Type()
)
starPortAvailableVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortAvailableVpi.setStatus("mandatory")
_StarPortDS1FramerTable_Object = MibTable
starPortDS1FramerTable = _StarPortDS1FramerTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2)
)
if mibBuilder.loadTexts:
    starPortDS1FramerTable.setStatus("mandatory")
_StarPortDS1FramerEntry_Object = MibTableRow
starPortDS1FramerEntry = _StarPortDS1FramerEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2, 1)
)
starPortDS1FramerEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortDS1FramerIndex"),
)
if mibBuilder.loadTexts:
    starPortDS1FramerEntry.setStatus("mandatory")
_StarPortDS1FramerIndex_Type = Integer32
_StarPortDS1FramerIndex_Object = MibTableColumn
starPortDS1FramerIndex = _StarPortDS1FramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2, 1, 1),
    _StarPortDS1FramerIndex_Type()
)
starPortDS1FramerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1FramerIndex.setStatus("mandatory")
_StarPortDS1FramerRevision_Type = Integer32
_StarPortDS1FramerRevision_Object = MibTableColumn
starPortDS1FramerRevision = _StarPortDS1FramerRevision_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2, 1, 2),
    _StarPortDS1FramerRevision_Type()
)
starPortDS1FramerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1FramerRevision.setStatus("mandatory")


class _StarPortDS1FramerFrameMode_Type(Integer32):
    """Custom type starPortDS1FramerFrameMode based on Integer32"""
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
        *(("esfnormal", 3),
          ("esfzbtis", 4),
          ("sfnormal", 1),
          ("sft1dm", 2))
    )


_StarPortDS1FramerFrameMode_Type.__name__ = "Integer32"
_StarPortDS1FramerFrameMode_Object = MibTableColumn
starPortDS1FramerFrameMode = _StarPortDS1FramerFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2, 1, 3),
    _StarPortDS1FramerFrameMode_Type()
)
starPortDS1FramerFrameMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1FramerFrameMode.setStatus("mandatory")


class _StarPortDS1FramerLineCoding_Type(Integer32):
    """Custom type starPortDS1FramerLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zstxrx", 3),
          ("mbzs", 2))
    )


_StarPortDS1FramerLineCoding_Type.__name__ = "Integer32"
_StarPortDS1FramerLineCoding_Object = MibTableColumn
starPortDS1FramerLineCoding = _StarPortDS1FramerLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2, 1, 4),
    _StarPortDS1FramerLineCoding_Type()
)
starPortDS1FramerLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1FramerLineCoding.setStatus("mandatory")
_StarPortDS1FramerBPVCounter_Type = Integer32
_StarPortDS1FramerBPVCounter_Object = MibTableColumn
starPortDS1FramerBPVCounter = _StarPortDS1FramerBPVCounter_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2, 1, 5),
    _StarPortDS1FramerBPVCounter_Type()
)
starPortDS1FramerBPVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1FramerBPVCounter.setStatus("mandatory")
_StarPortDS1FramerFBErrorCounter_Type = Integer32
_StarPortDS1FramerFBErrorCounter_Object = MibTableColumn
starPortDS1FramerFBErrorCounter = _StarPortDS1FramerFBErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2, 1, 6),
    _StarPortDS1FramerFBErrorCounter_Type()
)
starPortDS1FramerFBErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1FramerFBErrorCounter.setStatus("mandatory")
_StarPortDS1FramerCRCErrorCounter_Type = Integer32
_StarPortDS1FramerCRCErrorCounter_Object = MibTableColumn
starPortDS1FramerCRCErrorCounter = _StarPortDS1FramerCRCErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2, 1, 7),
    _StarPortDS1FramerCRCErrorCounter_Type()
)
starPortDS1FramerCRCErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1FramerCRCErrorCounter.setStatus("mandatory")
_StarPortDS1FramerCOFACounter_Type = Integer32
_StarPortDS1FramerCOFACounter_Object = MibTableColumn
starPortDS1FramerCOFACounter = _StarPortDS1FramerCOFACounter_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 2, 1, 8),
    _StarPortDS1FramerCOFACounter_Type()
)
starPortDS1FramerCOFACounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1FramerCOFACounter.setStatus("mandatory")
_StarPortE1FramerTable_Object = MibTable
starPortE1FramerTable = _StarPortE1FramerTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 3)
)
if mibBuilder.loadTexts:
    starPortE1FramerTable.setStatus("mandatory")
_StarPortE1FramerEntry_Object = MibTableRow
starPortE1FramerEntry = _StarPortE1FramerEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 3, 1)
)
starPortE1FramerEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortE1FramerIndex"),
)
if mibBuilder.loadTexts:
    starPortE1FramerEntry.setStatus("mandatory")
_StarPortE1FramerIndex_Type = Integer32
_StarPortE1FramerIndex_Object = MibTableColumn
starPortE1FramerIndex = _StarPortE1FramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 3, 1, 1),
    _StarPortE1FramerIndex_Type()
)
starPortE1FramerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortE1FramerIndex.setStatus("mandatory")
_StarPortE1FramerRevision_Type = Integer32
_StarPortE1FramerRevision_Object = MibTableColumn
starPortE1FramerRevision = _StarPortE1FramerRevision_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 3, 1, 2),
    _StarPortE1FramerRevision_Type()
)
starPortE1FramerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortE1FramerRevision.setStatus("mandatory")


class _StarPortE1FramerLineCoding_Type(Integer32):
    """Custom type starPortE1FramerLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("hdb3", 2))
    )


_StarPortE1FramerLineCoding_Type.__name__ = "Integer32"
_StarPortE1FramerLineCoding_Object = MibTableColumn
starPortE1FramerLineCoding = _StarPortE1FramerLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 3, 1, 3),
    _StarPortE1FramerLineCoding_Type()
)
starPortE1FramerLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortE1FramerLineCoding.setStatus("mandatory")


class _StarPortE1FramerSignalMode_Type(Integer32):
    """Custom type starPortE1FramerSignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cas", 2),
          ("ccs", 1),
          ("lapd", 3))
    )


_StarPortE1FramerSignalMode_Type.__name__ = "Integer32"
_StarPortE1FramerSignalMode_Object = MibTableColumn
starPortE1FramerSignalMode = _StarPortE1FramerSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 3, 1, 4),
    _StarPortE1FramerSignalMode_Type()
)
starPortE1FramerSignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortE1FramerSignalMode.setStatus("mandatory")
_StarPortE1FramerCRCErrorCounter_Type = Integer32
_StarPortE1FramerCRCErrorCounter_Object = MibTableColumn
starPortE1FramerCRCErrorCounter = _StarPortE1FramerCRCErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 3, 1, 5),
    _StarPortE1FramerCRCErrorCounter_Type()
)
starPortE1FramerCRCErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortE1FramerCRCErrorCounter.setStatus("mandatory")
_StarPortE1FramerLCVErrorCounter_Type = Integer32
_StarPortE1FramerLCVErrorCounter_Object = MibTableColumn
starPortE1FramerLCVErrorCounter = _StarPortE1FramerLCVErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 3, 1, 6),
    _StarPortE1FramerLCVErrorCounter_Type()
)
starPortE1FramerLCVErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortE1FramerLCVErrorCounter.setStatus("mandatory")
_StarPortE1FramerFASErrorCounter_Type = Integer32
_StarPortE1FramerFASErrorCounter_Object = MibTableColumn
starPortE1FramerFASErrorCounter = _StarPortE1FramerFASErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 3, 1, 7),
    _StarPortE1FramerFASErrorCounter_Type()
)
starPortE1FramerFASErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortE1FramerFASErrorCounter.setStatus("mandatory")
_StarPortDS3FramerTable_Object = MibTable
starPortDS3FramerTable = _StarPortDS3FramerTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 4)
)
if mibBuilder.loadTexts:
    starPortDS3FramerTable.setStatus("mandatory")
_StarPortDS3FramerEntry_Object = MibTableRow
starPortDS3FramerEntry = _StarPortDS3FramerEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 4, 1)
)
starPortDS3FramerEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortDS3FramerIndex"),
)
if mibBuilder.loadTexts:
    starPortDS3FramerEntry.setStatus("mandatory")
_StarPortDS3FramerIndex_Type = Integer32
_StarPortDS3FramerIndex_Object = MibTableColumn
starPortDS3FramerIndex = _StarPortDS3FramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 4, 1, 1),
    _StarPortDS3FramerIndex_Type()
)
starPortDS3FramerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS3FramerIndex.setStatus("mandatory")
_StarPortDS3FramerRevision_Type = Integer32
_StarPortDS3FramerRevision_Object = MibTableColumn
starPortDS3FramerRevision = _StarPortDS3FramerRevision_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 4, 1, 2),
    _StarPortDS3FramerRevision_Type()
)
starPortDS3FramerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS3FramerRevision.setStatus("mandatory")


class _StarPortDS3FramerFramingMode_Type(Integer32):
    """Custom type starPortDS3FramerFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("c-bit", 2),
          ("m13", 1))
    )


_StarPortDS3FramerFramingMode_Type.__name__ = "Integer32"
_StarPortDS3FramerFramingMode_Object = MibTableColumn
starPortDS3FramerFramingMode = _StarPortDS3FramerFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 4, 1, 3),
    _StarPortDS3FramerFramingMode_Type()
)
starPortDS3FramerFramingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS3FramerFramingMode.setStatus("mandatory")
_StarPortSonetUniTable_Object = MibTable
starPortSonetUniTable = _StarPortSonetUniTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 5)
)
if mibBuilder.loadTexts:
    starPortSonetUniTable.setStatus("mandatory")
_StarPortSonetUniEntry_Object = MibTableRow
starPortSonetUniEntry = _StarPortSonetUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 5, 1)
)
starPortSonetUniEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortSonetUniIndex"),
)
if mibBuilder.loadTexts:
    starPortSonetUniEntry.setStatus("mandatory")
_StarPortSonetUniIndex_Type = Integer32
_StarPortSonetUniIndex_Object = MibTableColumn
starPortSonetUniIndex = _StarPortSonetUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 5, 1, 1),
    _StarPortSonetUniIndex_Type()
)
starPortSonetUniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortSonetUniIndex.setStatus("mandatory")
_StarPortSonetUniMsgTxCt_Type = Integer32
_StarPortSonetUniMsgTxCt_Object = MibTableColumn
starPortSonetUniMsgTxCt = _StarPortSonetUniMsgTxCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 5, 1, 2),
    _StarPortSonetUniMsgTxCt_Type()
)
starPortSonetUniMsgTxCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortSonetUniMsgTxCt.setStatus("mandatory")
_StarPortSonetUniMsgRxCt_Type = Integer32
_StarPortSonetUniMsgRxCt_Object = MibTableColumn
starPortSonetUniMsgRxCt = _StarPortSonetUniMsgRxCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 5, 1, 3),
    _StarPortSonetUniMsgRxCt_Type()
)
starPortSonetUniMsgRxCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortSonetUniMsgRxCt.setStatus("mandatory")
_StarPortSonetUniHECErrorCt_Type = Integer32
_StarPortSonetUniHECErrorCt_Object = MibTableColumn
starPortSonetUniHECErrorCt = _StarPortSonetUniHECErrorCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 5, 1, 4),
    _StarPortSonetUniHECErrorCt_Type()
)
starPortSonetUniHECErrorCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortSonetUniHECErrorCt.setStatus("mandatory")
_StarPortDs3UniTable_Object = MibTable
starPortDs3UniTable = _StarPortDs3UniTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6)
)
if mibBuilder.loadTexts:
    starPortDs3UniTable.setStatus("mandatory")
_StarPortDs3UniEntry_Object = MibTableRow
starPortDs3UniEntry = _StarPortDs3UniEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1)
)
starPortDs3UniEntry.setIndexNames(
    (0, "STARNE-MIB", "starDsx3CurrentIndex"),
)
if mibBuilder.loadTexts:
    starPortDs3UniEntry.setStatus("mandatory")


class _StarDsx3CurrentIndex_Type(Integer32):
    """Custom type starDsx3CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StarDsx3CurrentIndex_Type.__name__ = "Integer32"
_StarDsx3CurrentIndex_Object = MibTableColumn
starDsx3CurrentIndex = _StarDsx3CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 1),
    _StarDsx3CurrentIndex_Type()
)
starDsx3CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDsx3CurrentIndex.setStatus("mandatory")
_StarPortDs3TxFEBEcount_Type = Gauge32
_StarPortDs3TxFEBEcount_Object = MibTableColumn
starPortDs3TxFEBEcount = _StarPortDs3TxFEBEcount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 2),
    _StarPortDs3TxFEBEcount_Type()
)
starPortDs3TxFEBEcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDs3TxFEBEcount.setStatus("mandatory")
_StarPortDs3RxFEBEcount_Type = Gauge32
_StarPortDs3RxFEBEcount_Object = MibTableColumn
starPortDs3RxFEBEcount = _StarPortDs3RxFEBEcount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 3),
    _StarPortDs3RxFEBEcount_Type()
)
starPortDs3RxFEBEcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDs3RxFEBEcount.setStatus("mandatory")
_StarPortPlcpTxFEBEcount_Type = Gauge32
_StarPortPlcpTxFEBEcount_Object = MibTableColumn
starPortPlcpTxFEBEcount = _StarPortPlcpTxFEBEcount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 4),
    _StarPortPlcpTxFEBEcount_Type()
)
starPortPlcpTxFEBEcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPlcpTxFEBEcount.setStatus("mandatory")
_StarPortPlcpRxFEBEcount_Type = Gauge32
_StarPortPlcpRxFEBEcount_Object = MibTableColumn
starPortPlcpRxFEBEcount = _StarPortPlcpRxFEBEcount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 5),
    _StarPortPlcpRxFEBEcount_Type()
)
starPortPlcpRxFEBEcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPlcpRxFEBEcount.setStatus("mandatory")
_StarPortRAIstatus_Type = Integer32
_StarPortRAIstatus_Object = MibTableColumn
starPortRAIstatus = _StarPortRAIstatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 6),
    _StarPortRAIstatus_Type()
)
starPortRAIstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortRAIstatus.setStatus("mandatory")
_StarPortPlcpCVcount_Type = Gauge32
_StarPortPlcpCVcount_Object = MibTableColumn
starPortPlcpCVcount = _StarPortPlcpCVcount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 7),
    _StarPortPlcpCVcount_Type()
)
starPortPlcpCVcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPlcpCVcount.setStatus("mandatory")
_StarPortPlcpEScount_Type = Gauge32
_StarPortPlcpEScount_Object = MibTableColumn
starPortPlcpEScount = _StarPortPlcpEScount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 8),
    _StarPortPlcpEScount_Type()
)
starPortPlcpEScount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPlcpEScount.setStatus("mandatory")
_StarPortPlcpSEScount_Type = Gauge32
_StarPortPlcpSEScount_Object = MibTableColumn
starPortPlcpSEScount = _StarPortPlcpSEScount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 9),
    _StarPortPlcpSEScount_Type()
)
starPortPlcpSEScount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPlcpSEScount.setStatus("mandatory")
_StarPortPlcpEFScount_Type = Gauge32
_StarPortPlcpEFScount_Object = MibTableColumn
starPortPlcpEFScount = _StarPortPlcpEFScount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 10),
    _StarPortPlcpEFScount_Type()
)
starPortPlcpEFScount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPlcpEFScount.setStatus("mandatory")
_StarPortPlcpSEFScount_Type = Gauge32
_StarPortPlcpSEFScount_Object = MibTableColumn
starPortPlcpSEFScount = _StarPortPlcpSEFScount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 11),
    _StarPortPlcpSEFScount_Type()
)
starPortPlcpSEFScount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPlcpSEFScount.setStatus("mandatory")
_StarPortPlcpUAScount_Type = Gauge32
_StarPortPlcpUAScount_Object = MibTableColumn
starPortPlcpUAScount = _StarPortPlcpUAScount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 12),
    _StarPortPlcpUAScount_Type()
)
starPortPlcpUAScount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPlcpUAScount.setStatus("mandatory")
_StarPortDs3LSEScount_Type = Gauge32
_StarPortDs3LSEScount_Object = MibTableColumn
starPortDs3LSEScount = _StarPortDs3LSEScount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 13),
    _StarPortDs3LSEScount_Type()
)
starPortDs3LSEScount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDs3LSEScount.setStatus("mandatory")
_StarPortDs3AISScount_Type = Gauge32
_StarPortDs3AISScount_Object = MibTableColumn
starPortDs3AISScount = _StarPortDs3AISScount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 14),
    _StarPortDs3AISScount_Type()
)
starPortDs3AISScount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDs3AISScount.setStatus("mandatory")
_StarPortDs3EFScount_Type = Gauge32
_StarPortDs3EFScount_Object = MibTableColumn
starPortDs3EFScount = _StarPortDs3EFScount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 6, 1, 15),
    _StarPortDs3EFScount_Type()
)
starPortDs3EFScount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDs3EFScount.setStatus("mandatory")
_StarPortPdhUniTable_Object = MibTable
starPortPdhUniTable = _StarPortPdhUniTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 7)
)
if mibBuilder.loadTexts:
    starPortPdhUniTable.setStatus("mandatory")
_StarPortPdhUniEntry_Object = MibTableRow
starPortPdhUniEntry = _StarPortPdhUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 7, 1)
)
starPortPdhUniEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortPdhUniIndex"),
)
if mibBuilder.loadTexts:
    starPortPdhUniEntry.setStatus("mandatory")
_StarPortPdhUniIndex_Type = Integer32
_StarPortPdhUniIndex_Object = MibTableColumn
starPortPdhUniIndex = _StarPortPdhUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 7, 1, 1),
    _StarPortPdhUniIndex_Type()
)
starPortPdhUniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPdhUniIndex.setStatus("mandatory")
_StarPortPdhUniMsgTxCt_Type = Integer32
_StarPortPdhUniMsgTxCt_Object = MibTableColumn
starPortPdhUniMsgTxCt = _StarPortPdhUniMsgTxCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 7, 1, 2),
    _StarPortPdhUniMsgTxCt_Type()
)
starPortPdhUniMsgTxCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPdhUniMsgTxCt.setStatus("mandatory")
_StarPortPdhUniMsgRxCt_Type = Integer32
_StarPortPdhUniMsgRxCt_Object = MibTableColumn
starPortPdhUniMsgRxCt = _StarPortPdhUniMsgRxCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 7, 1, 3),
    _StarPortPdhUniMsgRxCt_Type()
)
starPortPdhUniMsgRxCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPdhUniMsgRxCt.setStatus("mandatory")
_StarPortPdhUniHECErrCt_Type = Integer32
_StarPortPdhUniHECErrCt_Object = MibTableColumn
starPortPdhUniHECErrCt = _StarPortPdhUniHECErrCt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 7, 1, 4),
    _StarPortPdhUniHECErrCt_Type()
)
starPortPdhUniHECErrCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortPdhUniHECErrCt.setStatus("mandatory")
_StarPortDS1ATMTable_Object = MibTable
starPortDS1ATMTable = _StarPortDS1ATMTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 9)
)
if mibBuilder.loadTexts:
    starPortDS1ATMTable.setStatus("mandatory")
_StarPortDS1ATMEntry_Object = MibTableRow
starPortDS1ATMEntry = _StarPortDS1ATMEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 9, 1)
)
starPortDS1ATMEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortDS1ATMIndex"),
)
if mibBuilder.loadTexts:
    starPortDS1ATMEntry.setStatus("mandatory")
_StarPortDS1ATMIndex_Type = Integer32
_StarPortDS1ATMIndex_Object = MibTableColumn
starPortDS1ATMIndex = _StarPortDS1ATMIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 9, 1, 1),
    _StarPortDS1ATMIndex_Type()
)
starPortDS1ATMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1ATMIndex.setStatus("mandatory")
_StarPortDS1ATMHecCnt_Type = Integer32
_StarPortDS1ATMHecCnt_Object = MibTableColumn
starPortDS1ATMHecCnt = _StarPortDS1ATMHecCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 9, 1, 2),
    _StarPortDS1ATMHecCnt_Type()
)
starPortDS1ATMHecCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1ATMHecCnt.setStatus("mandatory")
_StarPortDS1ATMDiscardCellCnt_Type = Integer32
_StarPortDS1ATMDiscardCellCnt_Object = MibTableColumn
starPortDS1ATMDiscardCellCnt = _StarPortDS1ATMDiscardCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 9, 1, 3),
    _StarPortDS1ATMDiscardCellCnt_Type()
)
starPortDS1ATMDiscardCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1ATMDiscardCellCnt.setStatus("mandatory")
_StarPortDS1ATMErrCorrectCellCnt_Type = Integer32
_StarPortDS1ATMErrCorrectCellCnt_Object = MibTableColumn
starPortDS1ATMErrCorrectCellCnt = _StarPortDS1ATMErrCorrectCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 9, 1, 4),
    _StarPortDS1ATMErrCorrectCellCnt_Type()
)
starPortDS1ATMErrCorrectCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1ATMErrCorrectCellCnt.setStatus("mandatory")
_StarPortDS1ATMRxBusyCellCnt_Type = Integer32
_StarPortDS1ATMRxBusyCellCnt_Object = MibTableColumn
starPortDS1ATMRxBusyCellCnt = _StarPortDS1ATMRxBusyCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 9, 1, 5),
    _StarPortDS1ATMRxBusyCellCnt_Type()
)
starPortDS1ATMRxBusyCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1ATMRxBusyCellCnt.setStatus("mandatory")
_StarPortDS1ATMTxBusyCellCnt_Type = Integer32
_StarPortDS1ATMTxBusyCellCnt_Object = MibTableColumn
starPortDS1ATMTxBusyCellCnt = _StarPortDS1ATMTxBusyCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 9, 1, 6),
    _StarPortDS1ATMTxBusyCellCnt_Type()
)
starPortDS1ATMTxBusyCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortDS1ATMTxBusyCellCnt.setStatus("mandatory")
_StarPortM32Table_Object = MibTable
starPortM32Table = _StarPortM32Table_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10)
)
if mibBuilder.loadTexts:
    starPortM32Table.setStatus("mandatory")
_StarPortM32Entry_Object = MibTableRow
starPortM32Entry = _StarPortM32Entry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1)
)
starPortM32Entry.setIndexNames(
    (0, "STARNE-MIB", "starPortM32SlotId"),
    (0, "STARNE-MIB", "starPortM32ChipId"),
)
if mibBuilder.loadTexts:
    starPortM32Entry.setStatus("mandatory")
_StarPortM32SlotId_Type = Integer32
_StarPortM32SlotId_Object = MibTableColumn
starPortM32SlotId = _StarPortM32SlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 1),
    _StarPortM32SlotId_Type()
)
starPortM32SlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32SlotId.setStatus("mandatory")
_StarPortM32ChipId_Type = Integer32
_StarPortM32ChipId_Object = MibTableColumn
starPortM32ChipId = _StarPortM32ChipId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 2),
    _StarPortM32ChipId_Type()
)
starPortM32ChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32ChipId.setStatus("mandatory")
_StarPortM32RxCrcErrorCount_Type = Integer32
_StarPortM32RxCrcErrorCount_Object = MibTableColumn
starPortM32RxCrcErrorCount = _StarPortM32RxCrcErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 3),
    _StarPortM32RxCrcErrorCount_Type()
)
starPortM32RxCrcErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32RxCrcErrorCount.setStatus("mandatory")
_StarPortM32RxNobErrorCount_Type = Integer32
_StarPortM32RxNobErrorCount_Object = MibTableColumn
starPortM32RxNobErrorCount = _StarPortM32RxNobErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 4),
    _StarPortM32RxNobErrorCount_Type()
)
starPortM32RxNobErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32RxNobErrorCount.setStatus("mandatory")
_StarPortM32RxLfdErrorCount_Type = Integer32
_StarPortM32RxLfdErrorCount_Object = MibTableColumn
starPortM32RxLfdErrorCount = _StarPortM32RxLfdErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 5),
    _StarPortM32RxLfdErrorCount_Type()
)
starPortM32RxLfdErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32RxLfdErrorCount.setStatus("mandatory")
_StarPortM32RxIntBufOverFlwCount_Type = Integer32
_StarPortM32RxIntBufOverFlwCount_Object = MibTableColumn
starPortM32RxIntBufOverFlwCount = _StarPortM32RxIntBufOverFlwCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 6),
    _StarPortM32RxIntBufOverFlwCount_Type()
)
starPortM32RxIntBufOverFlwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32RxIntBufOverFlwCount.setStatus("mandatory")
_StarPortM32RxAbortCount_Type = Integer32
_StarPortM32RxAbortCount_Object = MibTableColumn
starPortM32RxAbortCount = _StarPortM32RxAbortCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 7),
    _StarPortM32RxAbortCount_Type()
)
starPortM32RxAbortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32RxAbortCount.setStatus("mandatory")
_StarPortM32RxShortFrameCount_Type = Integer32
_StarPortM32RxShortFrameCount_Object = MibTableColumn
starPortM32RxShortFrameCount = _StarPortM32RxShortFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 8),
    _StarPortM32RxShortFrameCount_Type()
)
starPortM32RxShortFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32RxShortFrameCount.setStatus("mandatory")
_StarPortM32RxDiscardFrameCount_Type = Integer32
_StarPortM32RxDiscardFrameCount_Object = MibTableColumn
starPortM32RxDiscardFrameCount = _StarPortM32RxDiscardFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 9),
    _StarPortM32RxDiscardFrameCount_Type()
)
starPortM32RxDiscardFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32RxDiscardFrameCount.setStatus("mandatory")
_StarPortM32RxPduCount_Type = Integer32
_StarPortM32RxPduCount_Object = MibTableColumn
starPortM32RxPduCount = _StarPortM32RxPduCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 10),
    _StarPortM32RxPduCount_Type()
)
starPortM32RxPduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32RxPduCount.setStatus("mandatory")
_StarPortM32RxByteCount_Type = Integer32
_StarPortM32RxByteCount_Object = MibTableColumn
starPortM32RxByteCount = _StarPortM32RxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 11),
    _StarPortM32RxByteCount_Type()
)
starPortM32RxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32RxByteCount.setStatus("mandatory")
_StarPortM32TxErrorCount_Type = Integer32
_StarPortM32TxErrorCount_Object = MibTableColumn
starPortM32TxErrorCount = _StarPortM32TxErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 12),
    _StarPortM32TxErrorCount_Type()
)
starPortM32TxErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32TxErrorCount.setStatus("mandatory")
_StarPortM32TxPduCount_Type = Integer32
_StarPortM32TxPduCount_Object = MibTableColumn
starPortM32TxPduCount = _StarPortM32TxPduCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 13),
    _StarPortM32TxPduCount_Type()
)
starPortM32TxPduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32TxPduCount.setStatus("mandatory")
_StarPortM32TxByteCount_Type = Integer32
_StarPortM32TxByteCount_Object = MibTableColumn
starPortM32TxByteCount = _StarPortM32TxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 10, 1, 14),
    _StarPortM32TxByteCount_Type()
)
starPortM32TxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortM32TxByteCount.setStatus("mandatory")
_StarPortHdlcConfigTable_Object = MibTable
starPortHdlcConfigTable = _StarPortHdlcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 11)
)
if mibBuilder.loadTexts:
    starPortHdlcConfigTable.setStatus("mandatory")
_StarPortHdlcConfigEntry_Object = MibTableRow
starPortHdlcConfigEntry = _StarPortHdlcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 11, 1)
)
starPortHdlcConfigEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortHdlcIndex"),
)
if mibBuilder.loadTexts:
    starPortHdlcConfigEntry.setStatus("mandatory")
_StarPortHdlcIndex_Type = Integer32
_StarPortHdlcIndex_Object = MibTableColumn
starPortHdlcIndex = _StarPortHdlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 11, 1, 1),
    _StarPortHdlcIndex_Type()
)
starPortHdlcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortHdlcIndex.setStatus("mandatory")


class _StarPortHdlcLineSpeed_Type(Integer32):
    """Custom type starPortHdlcLineSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("t1", 1)
    )


_StarPortHdlcLineSpeed_Type.__name__ = "Integer32"
_StarPortHdlcLineSpeed_Object = MibTableColumn
starPortHdlcLineSpeed = _StarPortHdlcLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 11, 1, 2),
    _StarPortHdlcLineSpeed_Type()
)
starPortHdlcLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortHdlcLineSpeed.setStatus("mandatory")


class _StarPortHdlcLineEncoding_Type(Integer32):
    """Custom type starPortHdlcLineEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi", 2))
    )


_StarPortHdlcLineEncoding_Type.__name__ = "Integer32"
_StarPortHdlcLineEncoding_Object = MibTableColumn
starPortHdlcLineEncoding = _StarPortHdlcLineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 11, 1, 3),
    _StarPortHdlcLineEncoding_Type()
)
starPortHdlcLineEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortHdlcLineEncoding.setStatus("mandatory")


class _StarPortHdlcCrcMode_Type(Integer32):
    """Custom type starPortHdlcCrcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crcccitt", 2))
    )


_StarPortHdlcCrcMode_Type.__name__ = "Integer32"
_StarPortHdlcCrcMode_Object = MibTableColumn
starPortHdlcCrcMode = _StarPortHdlcCrcMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 11, 1, 4),
    _StarPortHdlcCrcMode_Type()
)
starPortHdlcCrcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortHdlcCrcMode.setStatus("mandatory")


class _StarPortHdlcDteDce_Type(Integer32):
    """Custom type starPortHdlcDteDce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_StarPortHdlcDteDce_Type.__name__ = "Integer32"
_StarPortHdlcDteDce_Object = MibTableColumn
starPortHdlcDteDce = _StarPortHdlcDteDce_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 11, 1, 5),
    _StarPortHdlcDteDce_Type()
)
starPortHdlcDteDce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortHdlcDteDce.setStatus("mandatory")


class _StarPortHdlcClockMode_Type(Integer32):
    """Custom type starPortHdlcClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_StarPortHdlcClockMode_Type.__name__ = "Integer32"
_StarPortHdlcClockMode_Object = MibTableColumn
starPortHdlcClockMode = _StarPortHdlcClockMode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 11, 1, 6),
    _StarPortHdlcClockMode_Type()
)
starPortHdlcClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortHdlcClockMode.setStatus("mandatory")
_StarSvcmStatusTable_Object = MibTable
starSvcmStatusTable = _StarSvcmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12)
)
if mibBuilder.loadTexts:
    starSvcmStatusTable.setStatus("mandatory")
_StarSvcmStatusEntry_Object = MibTableRow
starSvcmStatusEntry = _StarSvcmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1)
)
starSvcmStatusEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starSvcmStatusEntry.setStatus("mandatory")
_StarSvcmActiveCallCnt_Type = Integer32
_StarSvcmActiveCallCnt_Object = MibTableColumn
starSvcmActiveCallCnt = _StarSvcmActiveCallCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 1),
    _StarSvcmActiveCallCnt_Type()
)
starSvcmActiveCallCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmActiveCallCnt.setStatus("mandatory")
_StarSvcmLastTxCause_Type = Integer32
_StarSvcmLastTxCause_Object = MibTableColumn
starSvcmLastTxCause = _StarSvcmLastTxCause_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 2),
    _StarSvcmLastTxCause_Type()
)
starSvcmLastTxCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmLastTxCause.setStatus("mandatory")
_StarSvcmPtoPOrgActiveConnectionCnt_Type = Integer32
_StarSvcmPtoPOrgActiveConnectionCnt_Object = MibTableColumn
starSvcmPtoPOrgActiveConnectionCnt = _StarSvcmPtoPOrgActiveConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 3),
    _StarSvcmPtoPOrgActiveConnectionCnt_Type()
)
starSvcmPtoPOrgActiveConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmPtoPOrgActiveConnectionCnt.setStatus("mandatory")
_StarSvcmPtoPTermActiveConnectionCnt_Type = Integer32
_StarSvcmPtoPTermActiveConnectionCnt_Object = MibTableColumn
starSvcmPtoPTermActiveConnectionCnt = _StarSvcmPtoPTermActiveConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 4),
    _StarSvcmPtoPTermActiveConnectionCnt_Type()
)
starSvcmPtoPTermActiveConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmPtoPTermActiveConnectionCnt.setStatus("mandatory")
_StarSvcmPtoMPOrgActiveConnectionCnt_Type = Integer32
_StarSvcmPtoMPOrgActiveConnectionCnt_Object = MibTableColumn
starSvcmPtoMPOrgActiveConnectionCnt = _StarSvcmPtoMPOrgActiveConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 5),
    _StarSvcmPtoMPOrgActiveConnectionCnt_Type()
)
starSvcmPtoMPOrgActiveConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmPtoMPOrgActiveConnectionCnt.setStatus("mandatory")
_StarSvcmPtoMPTermActiveConnectionCnt_Type = Integer32
_StarSvcmPtoMPTermActiveConnectionCnt_Object = MibTableColumn
starSvcmPtoMPTermActiveConnectionCnt = _StarSvcmPtoMPTermActiveConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 6),
    _StarSvcmPtoMPTermActiveConnectionCnt_Type()
)
starSvcmPtoMPTermActiveConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmPtoMPTermActiveConnectionCnt.setStatus("mandatory")
_StarSvcmConnectionSetupFailCnt_Type = Integer32
_StarSvcmConnectionSetupFailCnt_Object = MibTableColumn
starSvcmConnectionSetupFailCnt = _StarSvcmConnectionSetupFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 7),
    _StarSvcmConnectionSetupFailCnt_Type()
)
starSvcmConnectionSetupFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmConnectionSetupFailCnt.setStatus("mandatory")
_StarSvcmTxCallProceedingMsgCnt_Type = Integer32
_StarSvcmTxCallProceedingMsgCnt_Object = MibTableColumn
starSvcmTxCallProceedingMsgCnt = _StarSvcmTxCallProceedingMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 8),
    _StarSvcmTxCallProceedingMsgCnt_Type()
)
starSvcmTxCallProceedingMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmTxCallProceedingMsgCnt.setStatus("mandatory")
_StarSvcmRxCallProceedingMsgCnt_Type = Integer32
_StarSvcmRxCallProceedingMsgCnt_Object = MibTableColumn
starSvcmRxCallProceedingMsgCnt = _StarSvcmRxCallProceedingMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 9),
    _StarSvcmRxCallProceedingMsgCnt_Type()
)
starSvcmRxCallProceedingMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmRxCallProceedingMsgCnt.setStatus("mandatory")
_StarSvcmTxConnectMsgCnt_Type = Integer32
_StarSvcmTxConnectMsgCnt_Object = MibTableColumn
starSvcmTxConnectMsgCnt = _StarSvcmTxConnectMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 10),
    _StarSvcmTxConnectMsgCnt_Type()
)
starSvcmTxConnectMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmTxConnectMsgCnt.setStatus("mandatory")
_StarSvcmRxConnectMsgCnt_Type = Integer32
_StarSvcmRxConnectMsgCnt_Object = MibTableColumn
starSvcmRxConnectMsgCnt = _StarSvcmRxConnectMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 11),
    _StarSvcmRxConnectMsgCnt_Type()
)
starSvcmRxConnectMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmRxConnectMsgCnt.setStatus("mandatory")
_StarSvcmTxSetupMsgCnt_Type = Integer32
_StarSvcmTxSetupMsgCnt_Object = MibTableColumn
starSvcmTxSetupMsgCnt = _StarSvcmTxSetupMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 12),
    _StarSvcmTxSetupMsgCnt_Type()
)
starSvcmTxSetupMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmTxSetupMsgCnt.setStatus("mandatory")
_StarSvcmRxSetupMsgCnt_Type = Integer32
_StarSvcmRxSetupMsgCnt_Object = MibTableColumn
starSvcmRxSetupMsgCnt = _StarSvcmRxSetupMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 13),
    _StarSvcmRxSetupMsgCnt_Type()
)
starSvcmRxSetupMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmRxSetupMsgCnt.setStatus("mandatory")
_StarSvcmTxReleaseMsgCnt_Type = Integer32
_StarSvcmTxReleaseMsgCnt_Object = MibTableColumn
starSvcmTxReleaseMsgCnt = _StarSvcmTxReleaseMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 14),
    _StarSvcmTxReleaseMsgCnt_Type()
)
starSvcmTxReleaseMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmTxReleaseMsgCnt.setStatus("mandatory")
_StarSvcmRxReleaseMsgCnt_Type = Integer32
_StarSvcmRxReleaseMsgCnt_Object = MibTableColumn
starSvcmRxReleaseMsgCnt = _StarSvcmRxReleaseMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 15),
    _StarSvcmRxReleaseMsgCnt_Type()
)
starSvcmRxReleaseMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmRxReleaseMsgCnt.setStatus("mandatory")
_StarSvcmTxReleaseCompleteMsgCnt_Type = Integer32
_StarSvcmTxReleaseCompleteMsgCnt_Object = MibTableColumn
starSvcmTxReleaseCompleteMsgCnt = _StarSvcmTxReleaseCompleteMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 16),
    _StarSvcmTxReleaseCompleteMsgCnt_Type()
)
starSvcmTxReleaseCompleteMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmTxReleaseCompleteMsgCnt.setStatus("mandatory")
_StarSvcmRxReleaseCompleteMsgCnt_Type = Integer32
_StarSvcmRxReleaseCompleteMsgCnt_Object = MibTableColumn
starSvcmRxReleaseCompleteMsgCnt = _StarSvcmRxReleaseCompleteMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 17),
    _StarSvcmRxReleaseCompleteMsgCnt_Type()
)
starSvcmRxReleaseCompleteMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmRxReleaseCompleteMsgCnt.setStatus("mandatory")
_StarSvcmTxRestartMsgCnt_Type = Integer32
_StarSvcmTxRestartMsgCnt_Object = MibTableColumn
starSvcmTxRestartMsgCnt = _StarSvcmTxRestartMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 18),
    _StarSvcmTxRestartMsgCnt_Type()
)
starSvcmTxRestartMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmTxRestartMsgCnt.setStatus("mandatory")
_StarSvcmRxRestartMsgCnt_Type = Integer32
_StarSvcmRxRestartMsgCnt_Object = MibTableColumn
starSvcmRxRestartMsgCnt = _StarSvcmRxRestartMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 19),
    _StarSvcmRxRestartMsgCnt_Type()
)
starSvcmRxRestartMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmRxRestartMsgCnt.setStatus("mandatory")
_StarSvcmTxRestartAckMsgCnt_Type = Integer32
_StarSvcmTxRestartAckMsgCnt_Object = MibTableColumn
starSvcmTxRestartAckMsgCnt = _StarSvcmTxRestartAckMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 20),
    _StarSvcmTxRestartAckMsgCnt_Type()
)
starSvcmTxRestartAckMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmTxRestartAckMsgCnt.setStatus("mandatory")
_StarSvcmRxRestartAckMsgCnt_Type = Integer32
_StarSvcmRxRestartAckMsgCnt_Object = MibTableColumn
starSvcmRxRestartAckMsgCnt = _StarSvcmRxRestartAckMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 21),
    _StarSvcmRxRestartAckMsgCnt_Type()
)
starSvcmRxRestartAckMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmRxRestartAckMsgCnt.setStatus("mandatory")
_StarSvcmTxStatusMsgCnt_Type = Integer32
_StarSvcmTxStatusMsgCnt_Object = MibTableColumn
starSvcmTxStatusMsgCnt = _StarSvcmTxStatusMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 22),
    _StarSvcmTxStatusMsgCnt_Type()
)
starSvcmTxStatusMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmTxStatusMsgCnt.setStatus("mandatory")
_StarSvcmRxStatusMsgCnt_Type = Integer32
_StarSvcmRxStatusMsgCnt_Object = MibTableColumn
starSvcmRxStatusMsgCnt = _StarSvcmRxStatusMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 23),
    _StarSvcmRxStatusMsgCnt_Type()
)
starSvcmRxStatusMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmRxStatusMsgCnt.setStatus("mandatory")
_StarSvcmTxStatusEnquiryMsgCnt_Type = Integer32
_StarSvcmTxStatusEnquiryMsgCnt_Object = MibTableColumn
starSvcmTxStatusEnquiryMsgCnt = _StarSvcmTxStatusEnquiryMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 24),
    _StarSvcmTxStatusEnquiryMsgCnt_Type()
)
starSvcmTxStatusEnquiryMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmTxStatusEnquiryMsgCnt.setStatus("mandatory")
_StarSvcmRxStatusEnquiryMsgCnt_Type = Integer32
_StarSvcmRxStatusEnquiryMsgCnt_Object = MibTableColumn
starSvcmRxStatusEnquiryMsgCnt = _StarSvcmRxStatusEnquiryMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 12, 1, 25),
    _StarSvcmRxStatusEnquiryMsgCnt_Type()
)
starSvcmRxStatusEnquiryMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmRxStatusEnquiryMsgCnt.setStatus("mandatory")
_StarSvcmAiuStatsTable_Object = MibTable
starSvcmAiuStatsTable = _StarSvcmAiuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13)
)
if mibBuilder.loadTexts:
    starSvcmAiuStatsTable.setStatus("mandatory")
_StarSvcmAiuStatsEntry_Object = MibTableRow
starSvcmAiuStatsEntry = _StarSvcmAiuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1)
)
starSvcmAiuStatsEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starSvcmAiuStatsEntry.setStatus("mandatory")
_StarSvcmAiuTxSSCOPDiscardedCells_Type = Integer32
_StarSvcmAiuTxSSCOPDiscardedCells_Object = MibTableColumn
starSvcmAiuTxSSCOPDiscardedCells = _StarSvcmAiuTxSSCOPDiscardedCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 1),
    _StarSvcmAiuTxSSCOPDiscardedCells_Type()
)
starSvcmAiuTxSSCOPDiscardedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuTxSSCOPDiscardedCells.setStatus("mandatory")
_StarSvcmAiuRxBGNCells_Type = Integer32
_StarSvcmAiuRxBGNCells_Object = MibTableColumn
starSvcmAiuRxBGNCells = _StarSvcmAiuRxBGNCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 2),
    _StarSvcmAiuRxBGNCells_Type()
)
starSvcmAiuRxBGNCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxBGNCells.setStatus("mandatory")
_StarSvcmAiuRxBGAKCells_Type = Integer32
_StarSvcmAiuRxBGAKCells_Object = MibTableColumn
starSvcmAiuRxBGAKCells = _StarSvcmAiuRxBGAKCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 3),
    _StarSvcmAiuRxBGAKCells_Type()
)
starSvcmAiuRxBGAKCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxBGAKCells.setStatus("mandatory")
_StarSvcmAiuRxENDCells_Type = Integer32
_StarSvcmAiuRxENDCells_Object = MibTableColumn
starSvcmAiuRxENDCells = _StarSvcmAiuRxENDCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 4),
    _StarSvcmAiuRxENDCells_Type()
)
starSvcmAiuRxENDCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxENDCells.setStatus("mandatory")
_StarSvcmAiuRxRSCells_Type = Integer32
_StarSvcmAiuRxRSCells_Object = MibTableColumn
starSvcmAiuRxRSCells = _StarSvcmAiuRxRSCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 5),
    _StarSvcmAiuRxRSCells_Type()
)
starSvcmAiuRxRSCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxRSCells.setStatus("mandatory")
_StarSvcmAiuRxRSAKCells_Type = Integer32
_StarSvcmAiuRxRSAKCells_Object = MibTableColumn
starSvcmAiuRxRSAKCells = _StarSvcmAiuRxRSAKCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 6),
    _StarSvcmAiuRxRSAKCells_Type()
)
starSvcmAiuRxRSAKCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxRSAKCells.setStatus("mandatory")
_StarSvcmAiuRxSDCells_Type = Integer32
_StarSvcmAiuRxSDCells_Object = MibTableColumn
starSvcmAiuRxSDCells = _StarSvcmAiuRxSDCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 7),
    _StarSvcmAiuRxSDCells_Type()
)
starSvcmAiuRxSDCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxSDCells.setStatus("mandatory")
_StarSvcmAiuRxSDPCCells_Type = Integer32
_StarSvcmAiuRxSDPCCells_Object = MibTableColumn
starSvcmAiuRxSDPCCells = _StarSvcmAiuRxSDPCCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 8),
    _StarSvcmAiuRxSDPCCells_Type()
)
starSvcmAiuRxSDPCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxSDPCCells.setStatus("mandatory")
_StarSvcmAiuRxPOLLCells_Type = Integer32
_StarSvcmAiuRxPOLLCells_Object = MibTableColumn
starSvcmAiuRxPOLLCells = _StarSvcmAiuRxPOLLCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 9),
    _StarSvcmAiuRxPOLLCells_Type()
)
starSvcmAiuRxPOLLCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxPOLLCells.setStatus("mandatory")
_StarSvcmAiuRxSTATCells_Type = Integer32
_StarSvcmAiuRxSTATCells_Object = MibTableColumn
starSvcmAiuRxSTATCells = _StarSvcmAiuRxSTATCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 10),
    _StarSvcmAiuRxSTATCells_Type()
)
starSvcmAiuRxSTATCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxSTATCells.setStatus("mandatory")
_StarSvcmAiuRxUSTATCells_Type = Integer32
_StarSvcmAiuRxUSTATCells_Object = MibTableColumn
starSvcmAiuRxUSTATCells = _StarSvcmAiuRxUSTATCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 11),
    _StarSvcmAiuRxUSTATCells_Type()
)
starSvcmAiuRxUSTATCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxUSTATCells.setStatus("mandatory")
_StarSvcmAiuRxUDCells_Type = Integer32
_StarSvcmAiuRxUDCells_Object = MibTableColumn
starSvcmAiuRxUDCells = _StarSvcmAiuRxUDCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 12),
    _StarSvcmAiuRxUDCells_Type()
)
starSvcmAiuRxUDCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxUDCells.setStatus("mandatory")
_StarSvcmAiuRxMDCells_Type = Integer32
_StarSvcmAiuRxMDCells_Object = MibTableColumn
starSvcmAiuRxMDCells = _StarSvcmAiuRxMDCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 13),
    _StarSvcmAiuRxMDCells_Type()
)
starSvcmAiuRxMDCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxMDCells.setStatus("mandatory")
_StarSvcmAiuTxAddPartyMsgCnt_Type = Integer32
_StarSvcmAiuTxAddPartyMsgCnt_Object = MibTableColumn
starSvcmAiuTxAddPartyMsgCnt = _StarSvcmAiuTxAddPartyMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 14),
    _StarSvcmAiuTxAddPartyMsgCnt_Type()
)
starSvcmAiuTxAddPartyMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuTxAddPartyMsgCnt.setStatus("mandatory")
_StarSvcmAiuRxAddPartyMsgCnt_Type = Integer32
_StarSvcmAiuRxAddPartyMsgCnt_Object = MibTableColumn
starSvcmAiuRxAddPartyMsgCnt = _StarSvcmAiuRxAddPartyMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 15),
    _StarSvcmAiuRxAddPartyMsgCnt_Type()
)
starSvcmAiuRxAddPartyMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxAddPartyMsgCnt.setStatus("mandatory")
_StarSvcmAiuTxAddPartyRejMsgCnt_Type = Integer32
_StarSvcmAiuTxAddPartyRejMsgCnt_Object = MibTableColumn
starSvcmAiuTxAddPartyRejMsgCnt = _StarSvcmAiuTxAddPartyRejMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 16),
    _StarSvcmAiuTxAddPartyRejMsgCnt_Type()
)
starSvcmAiuTxAddPartyRejMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuTxAddPartyRejMsgCnt.setStatus("mandatory")
_StarSvcmAiuRxAddPartyRejMsgCnt_Type = Integer32
_StarSvcmAiuRxAddPartyRejMsgCnt_Object = MibTableColumn
starSvcmAiuRxAddPartyRejMsgCnt = _StarSvcmAiuRxAddPartyRejMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 17),
    _StarSvcmAiuRxAddPartyRejMsgCnt_Type()
)
starSvcmAiuRxAddPartyRejMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxAddPartyRejMsgCnt.setStatus("mandatory")
_StarSvcmAiuTxAddPartyAckMsgCnt_Type = Integer32
_StarSvcmAiuTxAddPartyAckMsgCnt_Object = MibTableColumn
starSvcmAiuTxAddPartyAckMsgCnt = _StarSvcmAiuTxAddPartyAckMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 18),
    _StarSvcmAiuTxAddPartyAckMsgCnt_Type()
)
starSvcmAiuTxAddPartyAckMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuTxAddPartyAckMsgCnt.setStatus("mandatory")
_StarSvcmAiuRxAddPartyAckMsgCnt_Type = Integer32
_StarSvcmAiuRxAddPartyAckMsgCnt_Object = MibTableColumn
starSvcmAiuRxAddPartyAckMsgCnt = _StarSvcmAiuRxAddPartyAckMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 19),
    _StarSvcmAiuRxAddPartyAckMsgCnt_Type()
)
starSvcmAiuRxAddPartyAckMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxAddPartyAckMsgCnt.setStatus("mandatory")
_StarSvcmAiuTxDropPartyMsgCnt_Type = Integer32
_StarSvcmAiuTxDropPartyMsgCnt_Object = MibTableColumn
starSvcmAiuTxDropPartyMsgCnt = _StarSvcmAiuTxDropPartyMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 20),
    _StarSvcmAiuTxDropPartyMsgCnt_Type()
)
starSvcmAiuTxDropPartyMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuTxDropPartyMsgCnt.setStatus("mandatory")
_StarSvcmAiuRxDropPartyMsgCnt_Type = Integer32
_StarSvcmAiuRxDropPartyMsgCnt_Object = MibTableColumn
starSvcmAiuRxDropPartyMsgCnt = _StarSvcmAiuRxDropPartyMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 21),
    _StarSvcmAiuRxDropPartyMsgCnt_Type()
)
starSvcmAiuRxDropPartyMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxDropPartyMsgCnt.setStatus("mandatory")
_StarSvcmAiuTxDropPartyAckMsgCnt_Type = Integer32
_StarSvcmAiuTxDropPartyAckMsgCnt_Object = MibTableColumn
starSvcmAiuTxDropPartyAckMsgCnt = _StarSvcmAiuTxDropPartyAckMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 22),
    _StarSvcmAiuTxDropPartyAckMsgCnt_Type()
)
starSvcmAiuTxDropPartyAckMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuTxDropPartyAckMsgCnt.setStatus("mandatory")
_StarSvcmAiuRxDropPartyAckMsgCnt_Type = Integer32
_StarSvcmAiuRxDropPartyAckMsgCnt_Object = MibTableColumn
starSvcmAiuRxDropPartyAckMsgCnt = _StarSvcmAiuRxDropPartyAckMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 13, 1, 23),
    _StarSvcmAiuRxDropPartyAckMsgCnt_Type()
)
starSvcmAiuRxDropPartyAckMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmAiuRxDropPartyAckMsgCnt.setStatus("mandatory")
_StarSvcmFiuStatsTable_Object = MibTable
starSvcmFiuStatsTable = _StarSvcmFiuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 14)
)
if mibBuilder.loadTexts:
    starSvcmFiuStatsTable.setStatus("mandatory")
_StarSvcmFiuStatsEntry_Object = MibTableRow
starSvcmFiuStatsEntry = _StarSvcmFiuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 14, 1)
)
starSvcmFiuStatsEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starSvcmFiuStatsEntry.setStatus("mandatory")
_StarSvcmFiuQ933TimerExpiryCnt_Type = Integer32
_StarSvcmFiuQ933TimerExpiryCnt_Object = MibTableColumn
starSvcmFiuQ933TimerExpiryCnt = _StarSvcmFiuQ933TimerExpiryCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 14, 1, 1),
    _StarSvcmFiuQ933TimerExpiryCnt_Type()
)
starSvcmFiuQ933TimerExpiryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmFiuQ933TimerExpiryCnt.setStatus("mandatory")
_StarSvcmFiuQ933IllegalMsgCnt_Type = Integer32
_StarSvcmFiuQ933IllegalMsgCnt_Object = MibTableColumn
starSvcmFiuQ933IllegalMsgCnt = _StarSvcmFiuQ933IllegalMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 14, 1, 2),
    _StarSvcmFiuQ933IllegalMsgCnt_Type()
)
starSvcmFiuQ933IllegalMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmFiuQ933IllegalMsgCnt.setStatus("mandatory")
_StarSvcmFiuQ922TimerExpiryCnt_Type = Integer32
_StarSvcmFiuQ922TimerExpiryCnt_Object = MibTableColumn
starSvcmFiuQ922TimerExpiryCnt = _StarSvcmFiuQ922TimerExpiryCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 14, 1, 3),
    _StarSvcmFiuQ922TimerExpiryCnt_Type()
)
starSvcmFiuQ922TimerExpiryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmFiuQ922TimerExpiryCnt.setStatus("mandatory")
_StarSvcmFiuQ922LinkFailIndicationCnt_Type = Integer32
_StarSvcmFiuQ922LinkFailIndicationCnt_Object = MibTableColumn
starSvcmFiuQ922LinkFailIndicationCnt = _StarSvcmFiuQ922LinkFailIndicationCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 14, 1, 4),
    _StarSvcmFiuQ922LinkFailIndicationCnt_Type()
)
starSvcmFiuQ922LinkFailIndicationCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmFiuQ922LinkFailIndicationCnt.setStatus("mandatory")
_StarSvcmFiuQ922UnackedMsgCnt_Type = Integer32
_StarSvcmFiuQ922UnackedMsgCnt_Object = MibTableColumn
starSvcmFiuQ922UnackedMsgCnt = _StarSvcmFiuQ922UnackedMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 14, 1, 5),
    _StarSvcmFiuQ922UnackedMsgCnt_Type()
)
starSvcmFiuQ922UnackedMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmFiuQ922UnackedMsgCnt.setStatus("mandatory")
_StarPortTrunkTable_Object = MibTable
starPortTrunkTable = _StarPortTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15)
)
if mibBuilder.loadTexts:
    starPortTrunkTable.setStatus("mandatory")
_StarPortTrunkEntry_Object = MibTableRow
starPortTrunkEntry = _StarPortTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1)
)
starPortTrunkEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starPortTrunkEntry.setStatus("mandatory")
_StarTotalInFixedCapa_Type = Integer32
_StarTotalInFixedCapa_Object = MibTableColumn
starTotalInFixedCapa = _StarTotalInFixedCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 1),
    _StarTotalInFixedCapa_Type()
)
starTotalInFixedCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starTotalInFixedCapa.setStatus("mandatory")
_StarTotalOutFixedCapa_Type = Integer32
_StarTotalOutFixedCapa_Object = MibTableColumn
starTotalOutFixedCapa = _StarTotalOutFixedCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 2),
    _StarTotalOutFixedCapa_Type()
)
starTotalOutFixedCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starTotalOutFixedCapa.setStatus("mandatory")
_StarTotalInVariableCapa_Type = Integer32
_StarTotalInVariableCapa_Object = MibTableColumn
starTotalInVariableCapa = _StarTotalInVariableCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 3),
    _StarTotalInVariableCapa_Type()
)
starTotalInVariableCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starTotalInVariableCapa.setStatus("mandatory")
_StarTotalOutVariableCapa_Type = Integer32
_StarTotalOutVariableCapa_Object = MibTableColumn
starTotalOutVariableCapa = _StarTotalOutVariableCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 4),
    _StarTotalOutVariableCapa_Type()
)
starTotalOutVariableCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starTotalOutVariableCapa.setStatus("mandatory")
_StarPvcInFixedCapa_Type = Integer32
_StarPvcInFixedCapa_Object = MibTableColumn
starPvcInFixedCapa = _StarPvcInFixedCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 5),
    _StarPvcInFixedCapa_Type()
)
starPvcInFixedCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcInFixedCapa.setStatus("mandatory")
_StarPvcOutFixedCapa_Type = Integer32
_StarPvcOutFixedCapa_Object = MibTableColumn
starPvcOutFixedCapa = _StarPvcOutFixedCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 6),
    _StarPvcOutFixedCapa_Type()
)
starPvcOutFixedCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcOutFixedCapa.setStatus("mandatory")
_StarPvcInVariableCapa_Type = Integer32
_StarPvcInVariableCapa_Object = MibTableColumn
starPvcInVariableCapa = _StarPvcInVariableCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 7),
    _StarPvcInVariableCapa_Type()
)
starPvcInVariableCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcInVariableCapa.setStatus("mandatory")
_StarPvcOutVariableCapa_Type = Integer32
_StarPvcOutVariableCapa_Object = MibTableColumn
starPvcOutVariableCapa = _StarPvcOutVariableCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 8),
    _StarPvcOutVariableCapa_Type()
)
starPvcOutVariableCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcOutVariableCapa.setStatus("mandatory")
_StarSvcInFixedCapa_Type = Integer32
_StarSvcInFixedCapa_Object = MibTableColumn
starSvcInFixedCapa = _StarSvcInFixedCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 9),
    _StarSvcInFixedCapa_Type()
)
starSvcInFixedCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcInFixedCapa.setStatus("mandatory")
_StarSvcOutFixedCapa_Type = Integer32
_StarSvcOutFixedCapa_Object = MibTableColumn
starSvcOutFixedCapa = _StarSvcOutFixedCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 10),
    _StarSvcOutFixedCapa_Type()
)
starSvcOutFixedCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcOutFixedCapa.setStatus("mandatory")
_StarSvcInVariableCapa_Type = Integer32
_StarSvcInVariableCapa_Object = MibTableColumn
starSvcInVariableCapa = _StarSvcInVariableCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 11),
    _StarSvcInVariableCapa_Type()
)
starSvcInVariableCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcInVariableCapa.setStatus("mandatory")
_StarSvcOutVariableCapa_Type = Integer32
_StarSvcOutVariableCapa_Object = MibTableColumn
starSvcOutVariableCapa = _StarSvcOutVariableCapa_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 15, 1, 12),
    _StarSvcOutVariableCapa_Type()
)
starSvcOutVariableCapa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcOutVariableCapa.setStatus("mandatory")
_StarPortRealStatusTable_Object = MibTable
starPortRealStatusTable = _StarPortRealStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 16)
)
if mibBuilder.loadTexts:
    starPortRealStatusTable.setStatus("mandatory")
_StarPortRealStatusEntry_Object = MibTableRow
starPortRealStatusEntry = _StarPortRealStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 16, 1)
)
starPortRealStatusEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
)
if mibBuilder.loadTexts:
    starPortRealStatusEntry.setStatus("mandatory")
_StarPortConfigRealStatus_Type = Integer32
_StarPortConfigRealStatus_Object = MibTableColumn
starPortConfigRealStatus = _StarPortConfigRealStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 16, 1, 1),
    _StarPortConfigRealStatus_Type()
)
starPortConfigRealStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortConfigRealStatus.setStatus("mandatory")
_StarPortAlarmRealStatus_Type = Integer32
_StarPortAlarmRealStatus_Object = MibTableColumn
starPortAlarmRealStatus = _StarPortAlarmRealStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 16, 1, 2),
    _StarPortAlarmRealStatus_Type()
)
starPortAlarmRealStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortAlarmRealStatus.setStatus("mandatory")
_StarPortOperRealStatus_Type = Integer32
_StarPortOperRealStatus_Object = MibTableColumn
starPortOperRealStatus = _StarPortOperRealStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 16, 1, 3),
    _StarPortOperRealStatus_Type()
)
starPortOperRealStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortOperRealStatus.setStatus("mandatory")
_StarPortRealStatusDescr_Type = OctetString
_StarPortRealStatusDescr_Object = MibTableColumn
starPortRealStatusDescr = _StarPortRealStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 16, 1, 4),
    _StarPortRealStatusDescr_Type()
)
starPortRealStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortRealStatusDescr.setStatus("mandatory")
_StarPortPmThresholdTable_Object = MibTable
starPortPmThresholdTable = _StarPortPmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17)
)
if mibBuilder.loadTexts:
    starPortPmThresholdTable.setStatus("mandatory")
_StarPortPmThresholdEntry_Object = MibTableRow
starPortPmThresholdEntry = _StarPortPmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17, 1)
)
starPortPmThresholdEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
    (0, "STARNE-MIB", "starPortPmThreshIdx"),
)
if mibBuilder.loadTexts:
    starPortPmThresholdEntry.setStatus("mandatory")
_StarPortPmThreshIdx_Type = Integer32
_StarPortPmThreshIdx_Object = MibTableColumn
starPortPmThreshIdx = _StarPortPmThreshIdx_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17, 1, 1),
    _StarPortPmThreshIdx_Type()
)
starPortPmThreshIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortPmThreshIdx.setStatus("mandatory")
_StarPortPmTrigger_Type = Integer32
_StarPortPmTrigger_Object = MibTableColumn
starPortPmTrigger = _StarPortPmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17, 1, 2),
    _StarPortPmTrigger_Type()
)
starPortPmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortPmTrigger.setStatus("mandatory")
_StarPortPmFlag_Type = Integer32
_StarPortPmFlag_Object = MibTableColumn
starPortPmFlag = _StarPortPmFlag_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17, 1, 3),
    _StarPortPmFlag_Type()
)
starPortPmFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortPmFlag.setStatus("mandatory")
_StarPortPmThreshValue_Type = Integer32
_StarPortPmThreshValue_Object = MibTableColumn
starPortPmThreshValue = _StarPortPmThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17, 1, 4),
    _StarPortPmThreshValue_Type()
)
starPortPmThreshValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortPmThreshValue.setStatus("mandatory")
_StarPortPmRearmValue_Type = Integer32
_StarPortPmRearmValue_Object = MibTableColumn
starPortPmRearmValue = _StarPortPmRearmValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17, 1, 5),
    _StarPortPmRearmValue_Type()
)
starPortPmRearmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortPmRearmValue.setStatus("mandatory")
_StarPortPmPriority_Type = Integer32
_StarPortPmPriority_Object = MibTableColumn
starPortPmPriority = _StarPortPmPriority_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17, 1, 6),
    _StarPortPmPriority_Type()
)
starPortPmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortPmPriority.setStatus("mandatory")
_StarPortPmInterval_Type = Integer32
_StarPortPmInterval_Object = MibTableColumn
starPortPmInterval = _StarPortPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17, 1, 7),
    _StarPortPmInterval_Type()
)
starPortPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortPmInterval.setStatus("mandatory")
_StarPortPmCnt_Type = Integer32
_StarPortPmCnt_Object = MibTableColumn
starPortPmCnt = _StarPortPmCnt_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 17, 1, 8),
    _StarPortPmCnt_Type()
)
starPortPmCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPortPmCnt.setStatus("mandatory")
_StarPortLMIStatsTable_Object = MibTable
starPortLMIStatsTable = _StarPortLMIStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 18)
)
if mibBuilder.loadTexts:
    starPortLMIStatsTable.setStatus("mandatory")
_StarPortLMIStatsEntry_Object = MibTableRow
starPortLMIStatsEntry = _StarPortLMIStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 18, 1)
)
starPortLMIStatsEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starPortLMIStatsEntry.setStatus("mandatory")
_StarPortLMILinkStats_Type = Integer32
_StarPortLMILinkStats_Object = MibTableColumn
starPortLMILinkStats = _StarPortLMILinkStats_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 18, 1, 1),
    _StarPortLMILinkStats_Type()
)
starPortLMILinkStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortLMILinkStats.setStatus("mandatory")
_StarPortFiu12Ds1Table_Object = MibTable
starPortFiu12Ds1Table = _StarPortFiu12Ds1Table_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19)
)
if mibBuilder.loadTexts:
    starPortFiu12Ds1Table.setStatus("mandatory")
_StarPortFiu12Ds1Entry_Object = MibTableRow
starPortFiu12Ds1Entry = _StarPortFiu12Ds1Entry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1)
)
starPortFiu12Ds1Entry.setIndexNames(
    (0, "STARNE-MIB", "starPortFiu12Index"),
)
if mibBuilder.loadTexts:
    starPortFiu12Ds1Entry.setStatus("mandatory")
_StarPortFiu12Index_Type = Integer32
_StarPortFiu12Index_Object = MibTableColumn
starPortFiu12Index = _StarPortFiu12Index_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1, 1),
    _StarPortFiu12Index_Type()
)
starPortFiu12Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Index.setStatus("mandatory")
_StarPortFiu12Ds1LCV_Type = Integer32
_StarPortFiu12Ds1LCV_Object = MibTableColumn
starPortFiu12Ds1LCV = _StarPortFiu12Ds1LCV_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1, 2),
    _StarPortFiu12Ds1LCV_Type()
)
starPortFiu12Ds1LCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds1LCV.setStatus("mandatory")
_StarPortFiu12Ds1BEE_Type = Integer32
_StarPortFiu12Ds1BEE_Object = MibTableColumn
starPortFiu12Ds1BEE = _StarPortFiu12Ds1BEE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1, 3),
    _StarPortFiu12Ds1BEE_Type()
)
starPortFiu12Ds1BEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds1BEE.setStatus("mandatory")
_StarPortFiu12Ds1FER_Type = Integer32
_StarPortFiu12Ds1FER_Object = MibTableColumn
starPortFiu12Ds1FER = _StarPortFiu12Ds1FER_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1, 4),
    _StarPortFiu12Ds1FER_Type()
)
starPortFiu12Ds1FER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds1FER.setStatus("mandatory")
_StarPortFiu12Ds1OOF_Type = Integer32
_StarPortFiu12Ds1OOF_Object = MibTableColumn
starPortFiu12Ds1OOF = _StarPortFiu12Ds1OOF_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1, 5),
    _StarPortFiu12Ds1OOF_Type()
)
starPortFiu12Ds1OOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds1OOF.setStatus("mandatory")
_StarPortFiu12E1FER_Type = Integer32
_StarPortFiu12E1FER_Object = MibTableColumn
starPortFiu12E1FER = _StarPortFiu12E1FER_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1, 6),
    _StarPortFiu12E1FER_Type()
)
starPortFiu12E1FER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12E1FER.setStatus("mandatory")
_StarPortFiu12E1FEBE_Type = Integer32
_StarPortFiu12E1FEBE_Object = MibTableColumn
starPortFiu12E1FEBE = _StarPortFiu12E1FEBE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1, 7),
    _StarPortFiu12E1FEBE_Type()
)
starPortFiu12E1FEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12E1FEBE.setStatus("mandatory")
_StarPortFiu12E1CRC_Type = Integer32
_StarPortFiu12E1CRC_Object = MibTableColumn
starPortFiu12E1CRC = _StarPortFiu12E1CRC_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1, 8),
    _StarPortFiu12E1CRC_Type()
)
starPortFiu12E1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12E1CRC.setStatus("mandatory")
_StarPortFiu12E1LCV_Type = Integer32
_StarPortFiu12E1LCV_Object = MibTableColumn
starPortFiu12E1LCV = _StarPortFiu12E1LCV_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 19, 1, 9),
    _StarPortFiu12E1LCV_Type()
)
starPortFiu12E1LCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12E1LCV.setStatus("mandatory")
_StarPortFiu12Ds3FramerTable_Object = MibTable
starPortFiu12Ds3FramerTable = _StarPortFiu12Ds3FramerTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 20)
)
if mibBuilder.loadTexts:
    starPortFiu12Ds3FramerTable.setStatus("mandatory")
_StarPortFiu12Ds3FramerEntry_Object = MibTableRow
starPortFiu12Ds3FramerEntry = _StarPortFiu12Ds3FramerEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 20, 1)
)
starPortFiu12Ds3FramerEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortFiu12Ds3FramerIndex"),
)
if mibBuilder.loadTexts:
    starPortFiu12Ds3FramerEntry.setStatus("mandatory")
_StarPortFiu12Ds3FramerIndex_Type = Integer32
_StarPortFiu12Ds3FramerIndex_Object = MibTableColumn
starPortFiu12Ds3FramerIndex = _StarPortFiu12Ds3FramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 20, 1, 1),
    _StarPortFiu12Ds3FramerIndex_Type()
)
starPortFiu12Ds3FramerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds3FramerIndex.setStatus("mandatory")
_StarPortFiu12Ds3FramerLCV_Type = Integer32
_StarPortFiu12Ds3FramerLCV_Object = MibTableColumn
starPortFiu12Ds3FramerLCV = _StarPortFiu12Ds3FramerLCV_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 20, 1, 2),
    _StarPortFiu12Ds3FramerLCV_Type()
)
starPortFiu12Ds3FramerLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds3FramerLCV.setStatus("mandatory")
_StarPortFiu12Ds3FramerFERR_Type = Integer32
_StarPortFiu12Ds3FramerFERR_Object = MibTableColumn
starPortFiu12Ds3FramerFERR = _StarPortFiu12Ds3FramerFERR_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 20, 1, 3),
    _StarPortFiu12Ds3FramerFERR_Type()
)
starPortFiu12Ds3FramerFERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds3FramerFERR.setStatus("mandatory")
_StarPortFiu12Ds3FramerDXZS_Type = Integer32
_StarPortFiu12Ds3FramerDXZS_Object = MibTableColumn
starPortFiu12Ds3FramerDXZS = _StarPortFiu12Ds3FramerDXZS_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 20, 1, 4),
    _StarPortFiu12Ds3FramerDXZS_Type()
)
starPortFiu12Ds3FramerDXZS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds3FramerDXZS.setStatus("mandatory")
_StarPortFiu12Ds3FramerPERR_Type = Integer32
_StarPortFiu12Ds3FramerPERR_Object = MibTableColumn
starPortFiu12Ds3FramerPERR = _StarPortFiu12Ds3FramerPERR_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 20, 1, 5),
    _StarPortFiu12Ds3FramerPERR_Type()
)
starPortFiu12Ds3FramerPERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds3FramerPERR.setStatus("mandatory")
_StarPortFiu12Ds3FramerCPERR_Type = Integer32
_StarPortFiu12Ds3FramerCPERR_Object = MibTableColumn
starPortFiu12Ds3FramerCPERR = _StarPortFiu12Ds3FramerCPERR_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 20, 1, 6),
    _StarPortFiu12Ds3FramerCPERR_Type()
)
starPortFiu12Ds3FramerCPERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds3FramerCPERR.setStatus("mandatory")
_StarPortFiu12Ds3FramerFEBE_Type = Integer32
_StarPortFiu12Ds3FramerFEBE_Object = MibTableColumn
starPortFiu12Ds3FramerFEBE = _StarPortFiu12Ds3FramerFEBE_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 20, 1, 7),
    _StarPortFiu12Ds3FramerFEBE_Type()
)
starPortFiu12Ds3FramerFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortFiu12Ds3FramerFEBE.setStatus("mandatory")
_StarPhysicalLoopbackTable_Object = MibTable
starPhysicalLoopbackTable = _StarPhysicalLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 21)
)
if mibBuilder.loadTexts:
    starPhysicalLoopbackTable.setStatus("mandatory")
_StarPhysicalLoopbackEntry_Object = MibTableRow
starPhysicalLoopbackEntry = _StarPhysicalLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 21, 1)
)
starPhysicalLoopbackEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
    (0, "STARNE-MIB", "starPhysicalLoopbackDs1Port"),
    (0, "STARNE-MIB", "starPhysicalLoopbackMethod"),
    (0, "STARNE-MIB", "starPhysicalLoopbackCtrl"),
)
if mibBuilder.loadTexts:
    starPhysicalLoopbackEntry.setStatus("mandatory")
_StarPhysicalLoopbackDs1Port_Type = Integer32
_StarPhysicalLoopbackDs1Port_Object = MibTableColumn
starPhysicalLoopbackDs1Port = _StarPhysicalLoopbackDs1Port_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 21, 1, 1),
    _StarPhysicalLoopbackDs1Port_Type()
)
starPhysicalLoopbackDs1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPhysicalLoopbackDs1Port.setStatus("mandatory")
_StarPhysicalLoopbackMethod_Type = Integer32
_StarPhysicalLoopbackMethod_Object = MibTableColumn
starPhysicalLoopbackMethod = _StarPhysicalLoopbackMethod_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 21, 1, 2),
    _StarPhysicalLoopbackMethod_Type()
)
starPhysicalLoopbackMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPhysicalLoopbackMethod.setStatus("mandatory")


class _StarPhysicalLoopbackCtrl_Type(Integer32):
    """Custom type starPhysicalLoopbackCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("release", 2),
          ("set", 1))
    )


_StarPhysicalLoopbackCtrl_Type.__name__ = "Integer32"
_StarPhysicalLoopbackCtrl_Object = MibTableColumn
starPhysicalLoopbackCtrl = _StarPhysicalLoopbackCtrl_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 21, 1, 3),
    _StarPhysicalLoopbackCtrl_Type()
)
starPhysicalLoopbackCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPhysicalLoopbackCtrl.setStatus("mandatory")
_StarPhysicalLoopbackStatus_Type = Integer32
_StarPhysicalLoopbackStatus_Object = MibTableColumn
starPhysicalLoopbackStatus = _StarPhysicalLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 21, 1, 4),
    _StarPhysicalLoopbackStatus_Type()
)
starPhysicalLoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPhysicalLoopbackStatus.setStatus("mandatory")
_StarPhysicalLoopbackDescr_Type = OctetString
_StarPhysicalLoopbackDescr_Object = MibTableColumn
starPhysicalLoopbackDescr = _StarPhysicalLoopbackDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 21, 1, 5),
    _StarPhysicalLoopbackDescr_Type()
)
starPhysicalLoopbackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPhysicalLoopbackDescr.setStatus("mandatory")
_StarPPP_ObjectIdentity = ObjectIdentity
starPPP = _StarPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22)
)
_StarPPPLinkStatusTable_Object = MibTable
starPPPLinkStatusTable = _StarPPPLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1)
)
if mibBuilder.loadTexts:
    starPPPLinkStatusTable.setStatus("mandatory")
_StarPPPLinkStatusEntry_Object = MibTableRow
starPPPLinkStatusEntry = _StarPPPLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1)
)
starPPPLinkStatusEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starPPPLinkStatusEntry.setStatus("mandatory")


class _StarPPPLinkStatusPhysicalIndex_Type(Integer32):
    """Custom type starPPPLinkStatusPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StarPPPLinkStatusPhysicalIndex_Type.__name__ = "Integer32"
_StarPPPLinkStatusPhysicalIndex_Object = MibTableColumn
starPPPLinkStatusPhysicalIndex = _StarPPPLinkStatusPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 1),
    _StarPPPLinkStatusPhysicalIndex_Type()
)
starPPPLinkStatusPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusPhysicalIndex.setStatus("mandatory")
_StarPPPLinkStatusBadAddresses_Type = Counter32
_StarPPPLinkStatusBadAddresses_Object = MibTableColumn
starPPPLinkStatusBadAddresses = _StarPPPLinkStatusBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 2),
    _StarPPPLinkStatusBadAddresses_Type()
)
starPPPLinkStatusBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusBadAddresses.setStatus("mandatory")
_StarPPPLinkStatusBadControls_Type = Counter32
_StarPPPLinkStatusBadControls_Object = MibTableColumn
starPPPLinkStatusBadControls = _StarPPPLinkStatusBadControls_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 3),
    _StarPPPLinkStatusBadControls_Type()
)
starPPPLinkStatusBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusBadControls.setStatus("mandatory")
_StarPPPLinkStatusPacketTooLongs_Type = Counter32
_StarPPPLinkStatusPacketTooLongs_Object = MibTableColumn
starPPPLinkStatusPacketTooLongs = _StarPPPLinkStatusPacketTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 4),
    _StarPPPLinkStatusPacketTooLongs_Type()
)
starPPPLinkStatusPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusPacketTooLongs.setStatus("mandatory")
_StarPPPLinkStatusBadFCSs_Type = Counter32
_StarPPPLinkStatusBadFCSs_Object = MibTableColumn
starPPPLinkStatusBadFCSs = _StarPPPLinkStatusBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 5),
    _StarPPPLinkStatusBadFCSs_Type()
)
starPPPLinkStatusBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusBadFCSs.setStatus("mandatory")


class _StarPPPLinkStatusLocalMRU_Type(Integer32):
    """Custom type starPPPLinkStatusLocalMRU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StarPPPLinkStatusLocalMRU_Type.__name__ = "Integer32"
_StarPPPLinkStatusLocalMRU_Object = MibTableColumn
starPPPLinkStatusLocalMRU = _StarPPPLinkStatusLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 6),
    _StarPPPLinkStatusLocalMRU_Type()
)
starPPPLinkStatusLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusLocalMRU.setStatus("mandatory")


class _StarPPPLinkStatusRemoteMRU_Type(Integer32):
    """Custom type starPPPLinkStatusRemoteMRU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StarPPPLinkStatusRemoteMRU_Type.__name__ = "Integer32"
_StarPPPLinkStatusRemoteMRU_Object = MibTableColumn
starPPPLinkStatusRemoteMRU = _StarPPPLinkStatusRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 7),
    _StarPPPLinkStatusRemoteMRU_Type()
)
starPPPLinkStatusRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusRemoteMRU.setStatus("mandatory")


class _StarPPPLinkStatusLocalToPeerACCMap_Type(OctetString):
    """Custom type starPPPLinkStatusLocalToPeerACCMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_StarPPPLinkStatusLocalToPeerACCMap_Type.__name__ = "OctetString"
_StarPPPLinkStatusLocalToPeerACCMap_Object = MibTableColumn
starPPPLinkStatusLocalToPeerACCMap = _StarPPPLinkStatusLocalToPeerACCMap_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 8),
    _StarPPPLinkStatusLocalToPeerACCMap_Type()
)
starPPPLinkStatusLocalToPeerACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusLocalToPeerACCMap.setStatus("mandatory")


class _StarPPPLinkStatusPeerToLocalACCMap_Type(OctetString):
    """Custom type starPPPLinkStatusPeerToLocalACCMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_StarPPPLinkStatusPeerToLocalACCMap_Type.__name__ = "OctetString"
_StarPPPLinkStatusPeerToLocalACCMap_Object = MibTableColumn
starPPPLinkStatusPeerToLocalACCMap = _StarPPPLinkStatusPeerToLocalACCMap_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 9),
    _StarPPPLinkStatusPeerToLocalACCMap_Type()
)
starPPPLinkStatusPeerToLocalACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusPeerToLocalACCMap.setStatus("mandatory")


class _StarPPPLinkStatusLocalToRemotePC_Type(Integer32):
    """Custom type starPPPLinkStatusLocalToRemotePC based on Integer32"""
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


_StarPPPLinkStatusLocalToRemotePC_Type.__name__ = "Integer32"
_StarPPPLinkStatusLocalToRemotePC_Object = MibTableColumn
starPPPLinkStatusLocalToRemotePC = _StarPPPLinkStatusLocalToRemotePC_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 10),
    _StarPPPLinkStatusLocalToRemotePC_Type()
)
starPPPLinkStatusLocalToRemotePC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusLocalToRemotePC.setStatus("mandatory")


class _StarPPPLinkStatusRemoteToLocalPC_Type(Integer32):
    """Custom type starPPPLinkStatusRemoteToLocalPC based on Integer32"""
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


_StarPPPLinkStatusRemoteToLocalPC_Type.__name__ = "Integer32"
_StarPPPLinkStatusRemoteToLocalPC_Object = MibTableColumn
starPPPLinkStatusRemoteToLocalPC = _StarPPPLinkStatusRemoteToLocalPC_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 11),
    _StarPPPLinkStatusRemoteToLocalPC_Type()
)
starPPPLinkStatusRemoteToLocalPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusRemoteToLocalPC.setStatus("mandatory")


class _StarPPPLinkStatusLocalToRemoteACFC_Type(Integer32):
    """Custom type starPPPLinkStatusLocalToRemoteACFC based on Integer32"""
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


_StarPPPLinkStatusLocalToRemoteACFC_Type.__name__ = "Integer32"
_StarPPPLinkStatusLocalToRemoteACFC_Object = MibTableColumn
starPPPLinkStatusLocalToRemoteACFC = _StarPPPLinkStatusLocalToRemoteACFC_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 12),
    _StarPPPLinkStatusLocalToRemoteACFC_Type()
)
starPPPLinkStatusLocalToRemoteACFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusLocalToRemoteACFC.setStatus("mandatory")


class _StarPPPLinkStatusRemoteToLocalACFC_Type(Integer32):
    """Custom type starPPPLinkStatusRemoteToLocalACFC based on Integer32"""
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


_StarPPPLinkStatusRemoteToLocalACFC_Type.__name__ = "Integer32"
_StarPPPLinkStatusRemoteToLocalACFC_Object = MibTableColumn
starPPPLinkStatusRemoteToLocalACFC = _StarPPPLinkStatusRemoteToLocalACFC_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 13),
    _StarPPPLinkStatusRemoteToLocalACFC_Type()
)
starPPPLinkStatusRemoteToLocalACFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusRemoteToLocalACFC.setStatus("mandatory")


class _StarPPPLinkStatusTransmitFcsSize_Type(Integer32):
    """Custom type starPPPLinkStatusTransmitFcsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_StarPPPLinkStatusTransmitFcsSize_Type.__name__ = "Integer32"
_StarPPPLinkStatusTransmitFcsSize_Object = MibTableColumn
starPPPLinkStatusTransmitFcsSize = _StarPPPLinkStatusTransmitFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 14),
    _StarPPPLinkStatusTransmitFcsSize_Type()
)
starPPPLinkStatusTransmitFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusTransmitFcsSize.setStatus("mandatory")


class _StarPPPLinkStatusReceiveFcsSize_Type(Integer32):
    """Custom type starPPPLinkStatusReceiveFcsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_StarPPPLinkStatusReceiveFcsSize_Type.__name__ = "Integer32"
_StarPPPLinkStatusReceiveFcsSize_Object = MibTableColumn
starPPPLinkStatusReceiveFcsSize = _StarPPPLinkStatusReceiveFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 1, 1, 15),
    _StarPPPLinkStatusReceiveFcsSize_Type()
)
starPPPLinkStatusReceiveFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLinkStatusReceiveFcsSize.setStatus("mandatory")
_StarPPPLqrTable_Object = MibTable
starPPPLqrTable = _StarPPPLqrTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 2)
)
if mibBuilder.loadTexts:
    starPPPLqrTable.setStatus("mandatory")
_StarPPPLqrEntry_Object = MibTableRow
starPPPLqrEntry = _StarPPPLqrEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 2, 1)
)
starPPPLqrEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starPPPLqrEntry.setStatus("mandatory")


class _StarPPPLqrQuality_Type(Integer32):
    """Custom type starPPPLqrQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1),
          ("not-determined", 3))
    )


_StarPPPLqrQuality_Type.__name__ = "Integer32"
_StarPPPLqrQuality_Object = MibTableColumn
starPPPLqrQuality = _StarPPPLqrQuality_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 2, 1, 1),
    _StarPPPLqrQuality_Type()
)
starPPPLqrQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLqrQuality.setStatus("mandatory")
_StarPPPLqrInGoodOctets_Type = Counter32
_StarPPPLqrInGoodOctets_Object = MibTableColumn
starPPPLqrInGoodOctets = _StarPPPLqrInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 2, 1, 2),
    _StarPPPLqrInGoodOctets_Type()
)
starPPPLqrInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLqrInGoodOctets.setStatus("mandatory")


class _StarPPPLqrLocalPeriod_Type(Integer32):
    """Custom type starPPPLqrLocalPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StarPPPLqrLocalPeriod_Type.__name__ = "Integer32"
_StarPPPLqrLocalPeriod_Object = MibTableColumn
starPPPLqrLocalPeriod = _StarPPPLqrLocalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 2, 1, 3),
    _StarPPPLqrLocalPeriod_Type()
)
starPPPLqrLocalPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLqrLocalPeriod.setStatus("mandatory")


class _StarPPPLqrRemotePeriod_Type(Integer32):
    """Custom type starPPPLqrRemotePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StarPPPLqrRemotePeriod_Type.__name__ = "Integer32"
_StarPPPLqrRemotePeriod_Object = MibTableColumn
starPPPLqrRemotePeriod = _StarPPPLqrRemotePeriod_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 2, 1, 4),
    _StarPPPLqrRemotePeriod_Type()
)
starPPPLqrRemotePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLqrRemotePeriod.setStatus("mandatory")
_StarPPPLqrOutLQRs_Type = Counter32
_StarPPPLqrOutLQRs_Object = MibTableColumn
starPPPLqrOutLQRs = _StarPPPLqrOutLQRs_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 2, 1, 5),
    _StarPPPLqrOutLQRs_Type()
)
starPPPLqrOutLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLqrOutLQRs.setStatus("mandatory")
_StarPPPLqrInLQRs_Type = Counter32
_StarPPPLqrInLQRs_Object = MibTableColumn
starPPPLqrInLQRs = _StarPPPLqrInLQRs_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 2, 1, 6),
    _StarPPPLqrInLQRs_Type()
)
starPPPLqrInLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPLqrInLQRs.setStatus("mandatory")
_StarPPPIpTable_Object = MibTable
starPPPIpTable = _StarPPPIpTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 3)
)
if mibBuilder.loadTexts:
    starPPPIpTable.setStatus("mandatory")
_StarPPPIpEntry_Object = MibTableRow
starPPPIpEntry = _StarPPPIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 3, 1)
)
starPPPIpEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starPPPIpEntry.setStatus("mandatory")


class _StarPPPIpOperStatus_Type(Integer32):
    """Custom type starPPPIpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_StarPPPIpOperStatus_Type.__name__ = "Integer32"
_StarPPPIpOperStatus_Object = MibTableColumn
starPPPIpOperStatus = _StarPPPIpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 3, 1, 1),
    _StarPPPIpOperStatus_Type()
)
starPPPIpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPIpOperStatus.setStatus("mandatory")


class _StarPPPIpLocalToRemoteCP_Type(Integer32):
    """Custom type starPPPIpLocalToRemoteCP based on Integer32"""
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


_StarPPPIpLocalToRemoteCP_Type.__name__ = "Integer32"
_StarPPPIpLocalToRemoteCP_Object = MibTableColumn
starPPPIpLocalToRemoteCP = _StarPPPIpLocalToRemoteCP_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 3, 1, 2),
    _StarPPPIpLocalToRemoteCP_Type()
)
starPPPIpLocalToRemoteCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPIpLocalToRemoteCP.setStatus("mandatory")


class _StarPPPIpRemoteToLocalCP_Type(Integer32):
    """Custom type starPPPIpRemoteToLocalCP based on Integer32"""
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


_StarPPPIpRemoteToLocalCP_Type.__name__ = "Integer32"
_StarPPPIpRemoteToLocalCP_Object = MibTableColumn
starPPPIpRemoteToLocalCP = _StarPPPIpRemoteToLocalCP_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 3, 1, 3),
    _StarPPPIpRemoteToLocalCP_Type()
)
starPPPIpRemoteToLocalCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPIpRemoteToLocalCP.setStatus("mandatory")


class _StarPPPIpRemoteMaxSlotId_Type(Integer32):
    """Custom type starPPPIpRemoteMaxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StarPPPIpRemoteMaxSlotId_Type.__name__ = "Integer32"
_StarPPPIpRemoteMaxSlotId_Object = MibTableColumn
starPPPIpRemoteMaxSlotId = _StarPPPIpRemoteMaxSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 3, 1, 4),
    _StarPPPIpRemoteMaxSlotId_Type()
)
starPPPIpRemoteMaxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPIpRemoteMaxSlotId.setStatus("mandatory")


class _StarPPPIpLocalMaxSlotId_Type(Integer32):
    """Custom type starPPPIpLocalMaxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StarPPPIpLocalMaxSlotId_Type.__name__ = "Integer32"
_StarPPPIpLocalMaxSlotId_Object = MibTableColumn
starPPPIpLocalMaxSlotId = _StarPPPIpLocalMaxSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 3, 22, 3, 1, 5),
    _StarPPPIpLocalMaxSlotId_Type()
)
starPPPIpLocalMaxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPPPIpLocalMaxSlotId.setStatus("mandatory")
_StarConn_ObjectIdentity = ObjectIdentity
starConn = _StarConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 4)
)
_StarVplStatsTable_Object = MibTable
starVplStatsTable = _StarVplStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1)
)
if mibBuilder.loadTexts:
    starVplStatsTable.setStatus("mandatory")
_StarVplStatsEntry_Object = MibTableRow
starVplStatsEntry = _StarVplStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1)
)
starVplStatsEntry.setIndexNames(
    (0, "STARNE-MIB", "starVplSlotIndex"),
    (0, "STARNE-MIB", "starVplPortIndex"),
    (0, "STARNE-MIB", "starVplConnRole"),
    (0, "STARNE-MIB", "starVplSourceNode"),
    (0, "STARNE-MIB", "starVplSourceSlot"),
    (0, "STARNE-MIB", "starVplSourcePort"),
    (0, "STARNE-MIB", "starVplSourceVpi"),
    (0, "STARNE-MIB", "starVplSourceVci"),
)
if mibBuilder.loadTexts:
    starVplStatsEntry.setStatus("mandatory")
_StarVplSlotIndex_Type = Integer32
_StarVplSlotIndex_Object = MibTableColumn
starVplSlotIndex = _StarVplSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 1),
    _StarVplSlotIndex_Type()
)
starVplSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplSlotIndex.setStatus("mandatory")
_StarVplPortIndex_Type = Integer32
_StarVplPortIndex_Object = MibTableColumn
starVplPortIndex = _StarVplPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 2),
    _StarVplPortIndex_Type()
)
starVplPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplPortIndex.setStatus("mandatory")
_StarVplSourceNode_Type = Integer32
_StarVplSourceNode_Object = MibTableColumn
starVplSourceNode = _StarVplSourceNode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 3),
    _StarVplSourceNode_Type()
)
starVplSourceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplSourceNode.setStatus("mandatory")
_StarVplSourceSlot_Type = Integer32
_StarVplSourceSlot_Object = MibTableColumn
starVplSourceSlot = _StarVplSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 4),
    _StarVplSourceSlot_Type()
)
starVplSourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplSourceSlot.setStatus("mandatory")
_StarVplSourcePort_Type = Integer32
_StarVplSourcePort_Object = MibTableColumn
starVplSourcePort = _StarVplSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 5),
    _StarVplSourcePort_Type()
)
starVplSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplSourcePort.setStatus("mandatory")
_StarVplSourceVpi_Type = Integer32
_StarVplSourceVpi_Object = MibTableColumn
starVplSourceVpi = _StarVplSourceVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 6),
    _StarVplSourceVpi_Type()
)
starVplSourceVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplSourceVpi.setStatus("mandatory")
_StarVplSourceVci_Type = Integer32
_StarVplSourceVci_Object = MibTableColumn
starVplSourceVci = _StarVplSourceVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 7),
    _StarVplSourceVci_Type()
)
starVplSourceVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplSourceVci.setStatus("mandatory")
_StarVplConnRole_Type = Integer32
_StarVplConnRole_Object = MibTableColumn
starVplConnRole = _StarVplConnRole_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 8),
    _StarVplConnRole_Type()
)
starVplConnRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplConnRole.setStatus("mandatory")
_StarVplStatsTimeStamp_Type = Counter32
_StarVplStatsTimeStamp_Object = MibTableColumn
starVplStatsTimeStamp = _StarVplStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 9),
    _StarVplStatsTimeStamp_Type()
)
starVplStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplStatsTimeStamp.setStatus("mandatory")
_StarVplNumOAMInvalidCRC_Type = Counter32
_StarVplNumOAMInvalidCRC_Object = MibTableColumn
starVplNumOAMInvalidCRC = _StarVplNumOAMInvalidCRC_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 10),
    _StarVplNumOAMInvalidCRC_Type()
)
starVplNumOAMInvalidCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplNumOAMInvalidCRC.setStatus("mandatory")


class _StarVplRtCongestedState_Type(Integer32):
    """Custom type starVplRtCongestedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congested", 1),
          ("notcongested", 2))
    )


_StarVplRtCongestedState_Type.__name__ = "Integer32"
_StarVplRtCongestedState_Object = MibTableColumn
starVplRtCongestedState = _StarVplRtCongestedState_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 11),
    _StarVplRtCongestedState_Type()
)
starVplRtCongestedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplRtCongestedState.setStatus("mandatory")
_StarVplRtNewVpi_Type = Counter32
_StarVplRtNewVpi_Object = MibTableColumn
starVplRtNewVpi = _StarVplRtNewVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 12),
    _StarVplRtNewVpi_Type()
)
starVplRtNewVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplRtNewVpi.setStatus("mandatory")
_StarVplRtCellsRxCount_Type = Counter32
_StarVplRtCellsRxCount_Object = MibTableColumn
starVplRtCellsRxCount = _StarVplRtCellsRxCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 13),
    _StarVplRtCellsRxCount_Type()
)
starVplRtCellsRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplRtCellsRxCount.setStatus("mandatory")
_StarVplRtCellsDroppedCount_Type = Counter32
_StarVplRtCellsDroppedCount_Object = MibTableColumn
starVplRtCellsDroppedCount = _StarVplRtCellsDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 14),
    _StarVplRtCellsDroppedCount_Type()
)
starVplRtCellsDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplRtCellsDroppedCount.setStatus("mandatory")
_StarVplRtCellsCongCount_Type = Counter32
_StarVplRtCellsCongCount_Object = MibTableColumn
starVplRtCellsCongCount = _StarVplRtCellsCongCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 15),
    _StarVplRtCellsCongCount_Type()
)
starVplRtCellsCongCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplRtCellsCongCount.setStatus("mandatory")
_StarVplUpcGcra0ViolCount_Type = Counter32
_StarVplUpcGcra0ViolCount_Object = MibTableColumn
starVplUpcGcra0ViolCount = _StarVplUpcGcra0ViolCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 16),
    _StarVplUpcGcra0ViolCount_Type()
)
starVplUpcGcra0ViolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplUpcGcra0ViolCount.setStatus("mandatory")
_StarVplUpcGcra1ViolCount_Type = Counter32
_StarVplUpcGcra1ViolCount_Object = MibTableColumn
starVplUpcGcra1ViolCount = _StarVplUpcGcra1ViolCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 17),
    _StarVplUpcGcra1ViolCount_Type()
)
starVplUpcGcra1ViolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplUpcGcra1ViolCount.setStatus("mandatory")
_StarVplUpcCellsCLP0_Type = Counter32
_StarVplUpcCellsCLP0_Object = MibTableColumn
starVplUpcCellsCLP0 = _StarVplUpcCellsCLP0_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 18),
    _StarVplUpcCellsCLP0_Type()
)
starVplUpcCellsCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplUpcCellsCLP0.setStatus("mandatory")
_StarVplUpcTotalCells_Type = Counter32
_StarVplUpcTotalCells_Object = MibTableColumn
starVplUpcTotalCells = _StarVplUpcTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 19),
    _StarVplUpcTotalCells_Type()
)
starVplUpcTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplUpcTotalCells.setStatus("mandatory")
_StarVplUpcTotalOAMCells_Type = Counter32
_StarVplUpcTotalOAMCells_Object = MibTableColumn
starVplUpcTotalOAMCells = _StarVplUpcTotalOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 1, 1, 20),
    _StarVplUpcTotalOAMCells_Type()
)
starVplUpcTotalOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVplUpcTotalOAMCells.setStatus("mandatory")
_StarVclStatsTable_Object = MibTable
starVclStatsTable = _StarVclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2)
)
if mibBuilder.loadTexts:
    starVclStatsTable.setStatus("mandatory")
_StarVclStatsEntry_Object = MibTableRow
starVclStatsEntry = _StarVclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1)
)
starVclStatsEntry.setIndexNames(
    (0, "STARNE-MIB", "starVclSlotIndex"),
    (0, "STARNE-MIB", "starVclPortIndex"),
    (0, "STARNE-MIB", "starVclConnRole"),
    (0, "STARNE-MIB", "starVclSourceNode"),
    (0, "STARNE-MIB", "starVclSourceSlot"),
    (0, "STARNE-MIB", "starVclSourcePort"),
    (0, "STARNE-MIB", "starVclSourceVpi"),
    (0, "STARNE-MIB", "starVclSourceVci"),
    (0, "STARNE-MIB", "starVclSourceDlci"),
    (0, "STARNE-MIB", "starVclSourceTimeslot"),
    (0, "STARNE-MIB", "starVclSourceIftype"),
    (0, "STARNE-MIB", "starVclSourceLeafno"),
)
if mibBuilder.loadTexts:
    starVclStatsEntry.setStatus("mandatory")
_StarVclSlotIndex_Type = Integer32
_StarVclSlotIndex_Object = MibTableColumn
starVclSlotIndex = _StarVclSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 1),
    _StarVclSlotIndex_Type()
)
starVclSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSlotIndex.setStatus("mandatory")
_StarVclPortIndex_Type = Integer32
_StarVclPortIndex_Object = MibTableColumn
starVclPortIndex = _StarVclPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 2),
    _StarVclPortIndex_Type()
)
starVclPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclPortIndex.setStatus("mandatory")
_StarVclSourceNode_Type = Integer32
_StarVclSourceNode_Object = MibTableColumn
starVclSourceNode = _StarVclSourceNode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 3),
    _StarVclSourceNode_Type()
)
starVclSourceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSourceNode.setStatus("mandatory")
_StarVclSourceSlot_Type = Integer32
_StarVclSourceSlot_Object = MibTableColumn
starVclSourceSlot = _StarVclSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 4),
    _StarVclSourceSlot_Type()
)
starVclSourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSourceSlot.setStatus("mandatory")
_StarVclSourcePort_Type = Integer32
_StarVclSourcePort_Object = MibTableColumn
starVclSourcePort = _StarVclSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 5),
    _StarVclSourcePort_Type()
)
starVclSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSourcePort.setStatus("mandatory")
_StarVclSourceVpi_Type = Integer32
_StarVclSourceVpi_Object = MibTableColumn
starVclSourceVpi = _StarVclSourceVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 6),
    _StarVclSourceVpi_Type()
)
starVclSourceVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSourceVpi.setStatus("mandatory")
_StarVclSourceVci_Type = Integer32
_StarVclSourceVci_Object = MibTableColumn
starVclSourceVci = _StarVclSourceVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 7),
    _StarVclSourceVci_Type()
)
starVclSourceVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSourceVci.setStatus("mandatory")
_StarVclConnRole_Type = Integer32
_StarVclConnRole_Object = MibTableColumn
starVclConnRole = _StarVclConnRole_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 8),
    _StarVclConnRole_Type()
)
starVclConnRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclConnRole.setStatus("mandatory")
_StarVclStatsTimeStamp_Type = Counter32
_StarVclStatsTimeStamp_Object = MibTableColumn
starVclStatsTimeStamp = _StarVclStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 9),
    _StarVclStatsTimeStamp_Type()
)
starVclStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclStatsTimeStamp.setStatus("mandatory")
_StarVclNumOAMInvalidCRC_Type = Counter32
_StarVclNumOAMInvalidCRC_Object = MibTableColumn
starVclNumOAMInvalidCRC = _StarVclNumOAMInvalidCRC_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 10),
    _StarVclNumOAMInvalidCRC_Type()
)
starVclNumOAMInvalidCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclNumOAMInvalidCRC.setStatus("mandatory")


class _StarVclRtCongestedState_Type(Integer32):
    """Custom type starVclRtCongestedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congested", 2),
          ("notcongested", 1))
    )


_StarVclRtCongestedState_Type.__name__ = "Integer32"
_StarVclRtCongestedState_Object = MibTableColumn
starVclRtCongestedState = _StarVclRtCongestedState_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 11),
    _StarVclRtCongestedState_Type()
)
starVclRtCongestedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclRtCongestedState.setStatus("mandatory")
_StarVclRtLastAal5State_Type = Counter32
_StarVclRtLastAal5State_Object = MibTableColumn
starVclRtLastAal5State = _StarVclRtLastAal5State_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 12),
    _StarVclRtLastAal5State_Type()
)
starVclRtLastAal5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclRtLastAal5State.setStatus("mandatory")
_StarVclRtNewVpi_Type = Counter32
_StarVclRtNewVpi_Object = MibTableColumn
starVclRtNewVpi = _StarVclRtNewVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 13),
    _StarVclRtNewVpi_Type()
)
starVclRtNewVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclRtNewVpi.setStatus("mandatory")
_StarVclRtNewVci_Type = Counter32
_StarVclRtNewVci_Object = MibTableColumn
starVclRtNewVci = _StarVclRtNewVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 14),
    _StarVclRtNewVci_Type()
)
starVclRtNewVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclRtNewVci.setStatus("mandatory")
_StarVclRtCellsRxCount_Type = Counter32
_StarVclRtCellsRxCount_Object = MibTableColumn
starVclRtCellsRxCount = _StarVclRtCellsRxCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 15),
    _StarVclRtCellsRxCount_Type()
)
starVclRtCellsRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclRtCellsRxCount.setStatus("mandatory")
_StarVclRtCellsDroppedCount_Type = Counter32
_StarVclRtCellsDroppedCount_Object = MibTableColumn
starVclRtCellsDroppedCount = _StarVclRtCellsDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 16),
    _StarVclRtCellsDroppedCount_Type()
)
starVclRtCellsDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclRtCellsDroppedCount.setStatus("mandatory")
_StarVclRtCellsCongCount_Type = Counter32
_StarVclRtCellsCongCount_Object = MibTableColumn
starVclRtCellsCongCount = _StarVclRtCellsCongCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 17),
    _StarVclRtCellsCongCount_Type()
)
starVclRtCellsCongCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclRtCellsCongCount.setStatus("mandatory")
_StarVclUpcGcra0ViolCount_Type = Counter32
_StarVclUpcGcra0ViolCount_Object = MibTableColumn
starVclUpcGcra0ViolCount = _StarVclUpcGcra0ViolCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 18),
    _StarVclUpcGcra0ViolCount_Type()
)
starVclUpcGcra0ViolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclUpcGcra0ViolCount.setStatus("mandatory")
_StarVclUpcGcra1ViolCount_Type = Counter32
_StarVclUpcGcra1ViolCount_Object = MibTableColumn
starVclUpcGcra1ViolCount = _StarVclUpcGcra1ViolCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 19),
    _StarVclUpcGcra1ViolCount_Type()
)
starVclUpcGcra1ViolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclUpcGcra1ViolCount.setStatus("mandatory")
_StarVclUpcCellsCLP0_Type = Counter32
_StarVclUpcCellsCLP0_Object = MibTableColumn
starVclUpcCellsCLP0 = _StarVclUpcCellsCLP0_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 20),
    _StarVclUpcCellsCLP0_Type()
)
starVclUpcCellsCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclUpcCellsCLP0.setStatus("mandatory")
_StarVclUpcTotalCells_Type = Counter32
_StarVclUpcTotalCells_Object = MibTableColumn
starVclUpcTotalCells = _StarVclUpcTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 21),
    _StarVclUpcTotalCells_Type()
)
starVclUpcTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclUpcTotalCells.setStatus("mandatory")
_StarVclUpcTotalOAMCells_Type = Counter32
_StarVclUpcTotalOAMCells_Object = MibTableColumn
starVclUpcTotalOAMCells = _StarVclUpcTotalOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 22),
    _StarVclUpcTotalOAMCells_Type()
)
starVclUpcTotalOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclUpcTotalOAMCells.setStatus("mandatory")
_StarVclSourceDlci_Type = Integer32
_StarVclSourceDlci_Object = MibTableColumn
starVclSourceDlci = _StarVclSourceDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 23),
    _StarVclSourceDlci_Type()
)
starVclSourceDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSourceDlci.setStatus("mandatory")
_StarVclSourceTimeslot_Type = Integer32
_StarVclSourceTimeslot_Object = MibTableColumn
starVclSourceTimeslot = _StarVclSourceTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 24),
    _StarVclSourceTimeslot_Type()
)
starVclSourceTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSourceTimeslot.setStatus("mandatory")
_StarVclSourceIftype_Type = Integer32
_StarVclSourceIftype_Object = MibTableColumn
starVclSourceIftype = _StarVclSourceIftype_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 25),
    _StarVclSourceIftype_Type()
)
starVclSourceIftype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSourceIftype.setStatus("mandatory")
_StarVclSourceLeafno_Type = Integer32
_StarVclSourceLeafno_Object = MibTableColumn
starVclSourceLeafno = _StarVclSourceLeafno_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 2, 1, 26),
    _StarVclSourceLeafno_Type()
)
starVclSourceLeafno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVclSourceLeafno.setStatus("mandatory")
_StarVpiRangeTable_Object = MibTable
starVpiRangeTable = _StarVpiRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 3)
)
if mibBuilder.loadTexts:
    starVpiRangeTable.setStatus("mandatory")
_StarVpiRangeEntry_Object = MibTableRow
starVpiRangeEntry = _StarVpiRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 3, 1)
)
starVpiRangeEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
    (0, "STARNE-MIB", "starVpiIndex"),
)
if mibBuilder.loadTexts:
    starVpiRangeEntry.setStatus("mandatory")
_StarVpiIndex_Type = Integer32
_StarVpiIndex_Object = MibTableColumn
starVpiIndex = _StarVpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 3, 1, 1),
    _StarVpiIndex_Type()
)
starVpiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVpiIndex.setStatus("mandatory")
_StarVpiVciBitRangeClass_Type = Integer32
_StarVpiVciBitRangeClass_Object = MibTableColumn
starVpiVciBitRangeClass = _StarVpiVciBitRangeClass_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 3, 1, 2),
    _StarVpiVciBitRangeClass_Type()
)
starVpiVciBitRangeClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starVpiVciBitRangeClass.setStatus("mandatory")
_StarVpiBitRangeValue_Type = Integer32
_StarVpiBitRangeValue_Object = MibTableColumn
starVpiBitRangeValue = _StarVpiBitRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 3, 1, 3),
    _StarVpiBitRangeValue_Type()
)
starVpiBitRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVpiBitRangeValue.setStatus("mandatory")
_StarVciBitRangeValue_Type = Integer32
_StarVciBitRangeValue_Object = MibTableColumn
starVciBitRangeValue = _StarVciBitRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 3, 1, 4),
    _StarVciBitRangeValue_Type()
)
starVciBitRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starVciBitRangeValue.setStatus("mandatory")
_StarAvailableVpiValue_Type = Integer32
_StarAvailableVpiValue_Object = MibTableColumn
starAvailableVpiValue = _StarAvailableVpiValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 3, 1, 5),
    _StarAvailableVpiValue_Type()
)
starAvailableVpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starAvailableVpiValue.setStatus("mandatory")
_StarLoopbackCtrTable_Object = MibTable
starLoopbackCtrTable = _StarLoopbackCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5)
)
if mibBuilder.loadTexts:
    starLoopbackCtrTable.setStatus("mandatory")
_StarLoopbackCtrEntry_Object = MibTableRow
starLoopbackCtrEntry = _StarLoopbackCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1)
)
starLoopbackCtrEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
)
if mibBuilder.loadTexts:
    starLoopbackCtrEntry.setStatus("mandatory")
_StarLoopbackCtrPortIndex_Type = Integer32
_StarLoopbackCtrPortIndex_Object = MibTableColumn
starLoopbackCtrPortIndex = _StarLoopbackCtrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 1),
    _StarLoopbackCtrPortIndex_Type()
)
starLoopbackCtrPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrPortIndex.setStatus("mandatory")
_StarLoopbackCtrVpi_Type = Integer32
_StarLoopbackCtrVpi_Object = MibTableColumn
starLoopbackCtrVpi = _StarLoopbackCtrVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 2),
    _StarLoopbackCtrVpi_Type()
)
starLoopbackCtrVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrVpi.setStatus("mandatory")
_StarLoopbackCtrVci_Type = Integer32
_StarLoopbackCtrVci_Object = MibTableColumn
starLoopbackCtrVci = _StarLoopbackCtrVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 3),
    _StarLoopbackCtrVci_Type()
)
starLoopbackCtrVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrVci.setStatus("mandatory")
_StarLoopbackCtrDeviceId_Type = Integer32
_StarLoopbackCtrDeviceId_Object = MibTableColumn
starLoopbackCtrDeviceId = _StarLoopbackCtrDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 4),
    _StarLoopbackCtrDeviceId_Type()
)
starLoopbackCtrDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrDeviceId.setStatus("mandatory")


class _StarLoopbackCtrType_Type(Integer32):
    """Custom type starLoopbackCtrType based on Integer32"""
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
        *(("oam-f4", 1),
          ("oam-f5", 2),
          ("phyline", 3),
          ("physsu", 4))
    )


_StarLoopbackCtrType_Type.__name__ = "Integer32"
_StarLoopbackCtrType_Object = MibTableColumn
starLoopbackCtrType = _StarLoopbackCtrType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 5),
    _StarLoopbackCtrType_Type()
)
starLoopbackCtrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrType.setStatus("mandatory")


class _StarLoopbackCtrEndType_Type(Integer32):
    """Custom type starLoopbackCtrEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connection-end", 2),
          ("intermediate", 3),
          ("segment", 1))
    )


_StarLoopbackCtrEndType_Type.__name__ = "Integer32"
_StarLoopbackCtrEndType_Object = MibTableColumn
starLoopbackCtrEndType = _StarLoopbackCtrEndType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 6),
    _StarLoopbackCtrEndType_Type()
)
starLoopbackCtrEndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrEndType.setStatus("mandatory")
_StarLoopbackCtrTxCellNo_Type = Integer32
_StarLoopbackCtrTxCellNo_Object = MibTableColumn
starLoopbackCtrTxCellNo = _StarLoopbackCtrTxCellNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 7),
    _StarLoopbackCtrTxCellNo_Type()
)
starLoopbackCtrTxCellNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrTxCellNo.setStatus("mandatory")
_StarLoopbackCtrTimetoWait_Type = Integer32
_StarLoopbackCtrTimetoWait_Object = MibTableColumn
starLoopbackCtrTimetoWait = _StarLoopbackCtrTimetoWait_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 8),
    _StarLoopbackCtrTimetoWait_Type()
)
starLoopbackCtrTimetoWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrTimetoWait.setStatus("mandatory")


class _StarLoopbackCtrSetup_Type(Integer32):
    """Custom type starLoopbackCtrSetup based on Integer32"""
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
        *(("finishreceiver", 4),
          ("finishsender", 5),
          ("initrcvatm", 2),
          ("initrcvphy", 1),
          ("initsender", 3))
    )


_StarLoopbackCtrSetup_Type.__name__ = "Integer32"
_StarLoopbackCtrSetup_Object = MibTableColumn
starLoopbackCtrSetup = _StarLoopbackCtrSetup_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 9),
    _StarLoopbackCtrSetup_Type()
)
starLoopbackCtrSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrSetup.setStatus("mandatory")
_StarLoopbackCtrMethod_Type = Integer32
_StarLoopbackCtrMethod_Object = MibTableColumn
starLoopbackCtrMethod = _StarLoopbackCtrMethod_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 10),
    _StarLoopbackCtrMethod_Type()
)
starLoopbackCtrMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrMethod.setStatus("mandatory")
_StarLoopbackCtrGeneration_Type = Integer32
_StarLoopbackCtrGeneration_Object = MibTableColumn
starLoopbackCtrGeneration = _StarLoopbackCtrGeneration_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 11),
    _StarLoopbackCtrGeneration_Type()
)
starLoopbackCtrGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGeneration.setStatus("mandatory")


class _StarLoopbackCtrInputType_Type(Integer32):
    """Custom type starLoopbackCtrInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gcid", 1),
          ("vcci", 2))
    )


_StarLoopbackCtrInputType_Type.__name__ = "Integer32"
_StarLoopbackCtrInputType_Object = MibTableColumn
starLoopbackCtrInputType = _StarLoopbackCtrInputType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 12),
    _StarLoopbackCtrInputType_Type()
)
starLoopbackCtrInputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrInputType.setStatus("mandatory")
_StarLoopbackCtrPdhNum_Type = Integer32
_StarLoopbackCtrPdhNum_Object = MibTableColumn
starLoopbackCtrPdhNum = _StarLoopbackCtrPdhNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 13),
    _StarLoopbackCtrPdhNum_Type()
)
starLoopbackCtrPdhNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrPdhNum.setStatus("mandatory")
_StarLoopbackCtrCellSpeed_Type = Integer32
_StarLoopbackCtrCellSpeed_Object = MibTableColumn
starLoopbackCtrCellSpeed = _StarLoopbackCtrCellSpeed_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 14),
    _StarLoopbackCtrCellSpeed_Type()
)
starLoopbackCtrCellSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrCellSpeed.setStatus("mandatory")
_StarLoopbackCtrGCIDNeId_Type = Integer32
_StarLoopbackCtrGCIDNeId_Object = MibTableColumn
starLoopbackCtrGCIDNeId = _StarLoopbackCtrGCIDNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 15),
    _StarLoopbackCtrGCIDNeId_Type()
)
starLoopbackCtrGCIDNeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGCIDNeId.setStatus("mandatory")
_StarLoopbackCtrGCIDSlotIndex_Type = Integer32
_StarLoopbackCtrGCIDSlotIndex_Object = MibTableColumn
starLoopbackCtrGCIDSlotIndex = _StarLoopbackCtrGCIDSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 16),
    _StarLoopbackCtrGCIDSlotIndex_Type()
)
starLoopbackCtrGCIDSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGCIDSlotIndex.setStatus("mandatory")
_StarLoopbackCtrGCIDPortIndex_Type = Integer32
_StarLoopbackCtrGCIDPortIndex_Object = MibTableColumn
starLoopbackCtrGCIDPortIndex = _StarLoopbackCtrGCIDPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 17),
    _StarLoopbackCtrGCIDPortIndex_Type()
)
starLoopbackCtrGCIDPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGCIDPortIndex.setStatus("mandatory")
_StarLoopbackCtrGCIDModuleIfType_Type = Integer32
_StarLoopbackCtrGCIDModuleIfType_Object = MibTableColumn
starLoopbackCtrGCIDModuleIfType = _StarLoopbackCtrGCIDModuleIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 18),
    _StarLoopbackCtrGCIDModuleIfType_Type()
)
starLoopbackCtrGCIDModuleIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGCIDModuleIfType.setStatus("mandatory")
_StarLoopbackCtrGCIDVpi_Type = Integer32
_StarLoopbackCtrGCIDVpi_Object = MibTableColumn
starLoopbackCtrGCIDVpi = _StarLoopbackCtrGCIDVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 19),
    _StarLoopbackCtrGCIDVpi_Type()
)
starLoopbackCtrGCIDVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGCIDVpi.setStatus("mandatory")
_StarLoopbackCtrGCIDVci_Type = Integer32
_StarLoopbackCtrGCIDVci_Object = MibTableColumn
starLoopbackCtrGCIDVci = _StarLoopbackCtrGCIDVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 20),
    _StarLoopbackCtrGCIDVci_Type()
)
starLoopbackCtrGCIDVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGCIDVci.setStatus("mandatory")
_StarLoopbackCtrGCIDDlci_Type = Integer32
_StarLoopbackCtrGCIDDlci_Object = MibTableColumn
starLoopbackCtrGCIDDlci = _StarLoopbackCtrGCIDDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 21),
    _StarLoopbackCtrGCIDDlci_Type()
)
starLoopbackCtrGCIDDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGCIDDlci.setStatus("mandatory")
_StarLoopbackCtrGCIDTimeSlot_Type = Integer32
_StarLoopbackCtrGCIDTimeSlot_Object = MibTableColumn
starLoopbackCtrGCIDTimeSlot = _StarLoopbackCtrGCIDTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 22),
    _StarLoopbackCtrGCIDTimeSlot_Type()
)
starLoopbackCtrGCIDTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGCIDTimeSlot.setStatus("mandatory")
_StarLoopbackCtrGCIDLeafNum_Type = Integer32
_StarLoopbackCtrGCIDLeafNum_Object = MibTableColumn
starLoopbackCtrGCIDLeafNum = _StarLoopbackCtrGCIDLeafNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 23),
    _StarLoopbackCtrGCIDLeafNum_Type()
)
starLoopbackCtrGCIDLeafNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGCIDLeafNum.setStatus("mandatory")
_StarLoopbackCtrAssignedSessionNo_Type = Integer32
_StarLoopbackCtrAssignedSessionNo_Object = MibTableColumn
starLoopbackCtrAssignedSessionNo = _StarLoopbackCtrAssignedSessionNo_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 24),
    _StarLoopbackCtrAssignedSessionNo_Type()
)
starLoopbackCtrAssignedSessionNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrAssignedSessionNo.setStatus("mandatory")


class _StarLoopbackCtrArea_Type(Integer32):
    """Custom type starLoopbackCtrArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interloop", 2),
          ("intraloop", 1),
          ("remoteloop", 3))
    )


_StarLoopbackCtrArea_Type.__name__ = "Integer32"
_StarLoopbackCtrArea_Object = MibTableColumn
starLoopbackCtrArea = _StarLoopbackCtrArea_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 25),
    _StarLoopbackCtrArea_Type()
)
starLoopbackCtrArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrArea.setStatus("mandatory")


class _StarLoopbackCtrChannelType_Type(Integer32):
    """Custom type starLoopbackCtrChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("looptestchan", 2),
          ("userchan", 1))
    )


_StarLoopbackCtrChannelType_Type.__name__ = "Integer32"
_StarLoopbackCtrChannelType_Object = MibTableColumn
starLoopbackCtrChannelType = _StarLoopbackCtrChannelType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 26),
    _StarLoopbackCtrChannelType_Type()
)
starLoopbackCtrChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrChannelType.setStatus("mandatory")


class _StarLoopbackCtrLastSetupResult_Type(Integer32):
    """Custom type starLoopbackCtrLastSetupResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("success", 1))
    )


_StarLoopbackCtrLastSetupResult_Type.__name__ = "Integer32"
_StarLoopbackCtrLastSetupResult_Object = MibTableColumn
starLoopbackCtrLastSetupResult = _StarLoopbackCtrLastSetupResult_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 27),
    _StarLoopbackCtrLastSetupResult_Type()
)
starLoopbackCtrLastSetupResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLoopbackCtrLastSetupResult.setStatus("mandatory")
_StarLoopbackCtrPortNum_Type = Integer32
_StarLoopbackCtrPortNum_Object = MibTableColumn
starLoopbackCtrPortNum = _StarLoopbackCtrPortNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 28),
    _StarLoopbackCtrPortNum_Type()
)
starLoopbackCtrPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrPortNum.setStatus("mandatory")


class _StarLoopbackCtrGenCellType_Type(Integer32):
    """Custom type starLoopbackCtrGenCellType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connection-end", 2),
          ("segment", 1))
    )


_StarLoopbackCtrGenCellType_Type.__name__ = "Integer32"
_StarLoopbackCtrGenCellType_Object = MibTableColumn
starLoopbackCtrGenCellType = _StarLoopbackCtrGenCellType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 5, 1, 29),
    _StarLoopbackCtrGenCellType_Type()
)
starLoopbackCtrGenCellType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starLoopbackCtrGenCellType.setStatus("mandatory")
_StarLoopbackResultTable_Object = MibTable
starLoopbackResultTable = _StarLoopbackResultTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 6)
)
if mibBuilder.loadTexts:
    starLoopbackResultTable.setStatus("mandatory")
_StarLoopbackResultEntry_Object = MibTableRow
starLoopbackResultEntry = _StarLoopbackResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 6, 1)
)
starLoopbackResultEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
)
if mibBuilder.loadTexts:
    starLoopbackResultEntry.setStatus("mandatory")
_StarLoopbackResultGeneratedCells_Type = Integer32
_StarLoopbackResultGeneratedCells_Object = MibTableColumn
starLoopbackResultGeneratedCells = _StarLoopbackResultGeneratedCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 6, 1, 1),
    _StarLoopbackResultGeneratedCells_Type()
)
starLoopbackResultGeneratedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLoopbackResultGeneratedCells.setStatus("mandatory")
_StarLoopbackResultReturnedCells_Type = Integer32
_StarLoopbackResultReturnedCells_Object = MibTableColumn
starLoopbackResultReturnedCells = _StarLoopbackResultReturnedCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 6, 1, 2),
    _StarLoopbackResultReturnedCells_Type()
)
starLoopbackResultReturnedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starLoopbackResultReturnedCells.setStatus("mandatory")
_StarPmCtrTable_Object = MibTable
starPmCtrTable = _StarPmCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7)
)
if mibBuilder.loadTexts:
    starPmCtrTable.setStatus("mandatory")
_StarPmCtrEntry_Object = MibTableRow
starPmCtrEntry = _StarPmCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1)
)
starPmCtrEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
)
if mibBuilder.loadTexts:
    starPmCtrEntry.setStatus("mandatory")
_StarPmCtrUpcId_Type = Integer32
_StarPmCtrUpcId_Object = MibTableColumn
starPmCtrUpcId = _StarPmCtrUpcId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 1),
    _StarPmCtrUpcId_Type()
)
starPmCtrUpcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrUpcId.setStatus("mandatory")
_StarPmCtrVpi_Type = Integer32
_StarPmCtrVpi_Object = MibTableColumn
starPmCtrVpi = _StarPmCtrVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 2),
    _StarPmCtrVpi_Type()
)
starPmCtrVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrVpi.setStatus("mandatory")
_StarPmCtrVci_Type = Integer32
_StarPmCtrVci_Object = MibTableColumn
starPmCtrVci = _StarPmCtrVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 3),
    _StarPmCtrVci_Type()
)
starPmCtrVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrVci.setStatus("mandatory")


class _StarPmCtrSegmentType_Type(Integer32):
    """Custom type starPmCtrSegmentType based on Integer32"""
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
        *(("end-to-endvcc", 4),
          ("end-to-endvpc", 2),
          ("segmentvcc", 3),
          ("segmentvpc", 1))
    )


_StarPmCtrSegmentType_Type.__name__ = "Integer32"
_StarPmCtrSegmentType_Object = MibTableColumn
starPmCtrSegmentType = _StarPmCtrSegmentType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 4),
    _StarPmCtrSegmentType_Type()
)
starPmCtrSegmentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrSegmentType.setStatus("mandatory")


class _StarPmCtrNodeType_Type(Integer32):
    """Custom type starPmCtrNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("orignode", 1),
          ("termnode", 2))
    )


_StarPmCtrNodeType_Type.__name__ = "Integer32"
_StarPmCtrNodeType_Object = MibTableColumn
starPmCtrNodeType = _StarPmCtrNodeType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 5),
    _StarPmCtrNodeType_Type()
)
starPmCtrNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrNodeType.setStatus("mandatory")
_StarPmCtrBlockSize_Type = Integer32
_StarPmCtrBlockSize_Object = MibTableColumn
starPmCtrBlockSize = _StarPmCtrBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 6),
    _StarPmCtrBlockSize_Type()
)
starPmCtrBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrBlockSize.setStatus("mandatory")


class _StarPmCtrPmCellClp_Type(Integer32):
    """Custom type starPmCtrPmCellClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clp0", 0),
          ("clp1", 1))
    )


_StarPmCtrPmCellClp_Type.__name__ = "Integer32"
_StarPmCtrPmCellClp_Object = MibTableColumn
starPmCtrPmCellClp = _StarPmCtrPmCellClp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 7),
    _StarPmCtrPmCellClp_Type()
)
starPmCtrPmCellClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrPmCellClp.setStatus("mandatory")


class _StarPmCtrBackRptGen_Type(Integer32):
    """Custom type starPmCtrBackRptGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bwgrGen", 1),
          ("nobwgr", 0))
    )


_StarPmCtrBackRptGen_Type.__name__ = "Integer32"
_StarPmCtrBackRptGen_Object = MibTableColumn
starPmCtrBackRptGen = _StarPmCtrBackRptGen_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 8),
    _StarPmCtrBackRptGen_Type()
)
starPmCtrBackRptGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrBackRptGen.setStatus("mandatory")


class _StarPmCtrActivate_Type(Integer32):
    """Custom type starPmCtrActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2))
    )


_StarPmCtrActivate_Type.__name__ = "Integer32"
_StarPmCtrActivate_Object = MibTableColumn
starPmCtrActivate = _StarPmCtrActivate_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 9),
    _StarPmCtrActivate_Type()
)
starPmCtrActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrActivate.setStatus("mandatory")


class _StarPmCtrStart_Type(Integer32):
    """Custom type starPmCtrStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_StarPmCtrStart_Type.__name__ = "Integer32"
_StarPmCtrStart_Object = MibTableColumn
starPmCtrStart = _StarPmCtrStart_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 10),
    _StarPmCtrStart_Type()
)
starPmCtrStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starPmCtrStart.setStatus("mandatory")
_StarPmCtrLastAssignedSession_Type = Integer32
_StarPmCtrLastAssignedSession_Object = MibTableColumn
starPmCtrLastAssignedSession = _StarPmCtrLastAssignedSession_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 7, 1, 11),
    _StarPmCtrLastAssignedSession_Type()
)
starPmCtrLastAssignedSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPmCtrLastAssignedSession.setStatus("mandatory")
_StarPmTable_Object = MibTable
starPmTable = _StarPmTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 8)
)
if mibBuilder.loadTexts:
    starPmTable.setStatus("mandatory")
_StarPmEntry_Object = MibTableRow
starPmEntry = _StarPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 8, 1)
)
starPmEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPmCtrUpcId"),
    (0, "STARNE-MIB", "starPmCtrLastAssignedSession"),
)
if mibBuilder.loadTexts:
    starPmEntry.setStatus("mandatory")
_StarPmTotalCellClp0Count_Type = Integer32
_StarPmTotalCellClp0Count_Object = MibTableColumn
starPmTotalCellClp0Count = _StarPmTotalCellClp0Count_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 8, 1, 1),
    _StarPmTotalCellClp0Count_Type()
)
starPmTotalCellClp0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPmTotalCellClp0Count.setStatus("mandatory")
_StarPmTotalCellClp01Count_Type = Integer32
_StarPmTotalCellClp01Count_Object = MibTableColumn
starPmTotalCellClp01Count = _StarPmTotalCellClp01Count_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 8, 1, 2),
    _StarPmTotalCellClp01Count_Type()
)
starPmTotalCellClp01Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPmTotalCellClp01Count.setStatus("mandatory")
_StarPmLostCellClp0Count_Type = Integer32
_StarPmLostCellClp0Count_Object = MibTableColumn
starPmLostCellClp0Count = _StarPmLostCellClp0Count_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 8, 1, 3),
    _StarPmLostCellClp0Count_Type()
)
starPmLostCellClp0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPmLostCellClp0Count.setStatus("mandatory")
_StarPmLostCellClp01Count_Type = Integer32
_StarPmLostCellClp01Count_Object = MibTableColumn
starPmLostCellClp01Count = _StarPmLostCellClp01Count_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 8, 1, 4),
    _StarPmLostCellClp01Count_Type()
)
starPmLostCellClp01Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPmLostCellClp01Count.setStatus("mandatory")
_StarPmErroredCellCount_Type = Integer32
_StarPmErroredCellCount_Object = MibTableColumn
starPmErroredCellCount = _StarPmErroredCellCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 8, 1, 5),
    _StarPmErroredCellCount_Type()
)
starPmErroredCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPmErroredCellCount.setStatus("mandatory")
_StarPmMisinsertedCellCount_Type = Integer32
_StarPmMisinsertedCellCount_Object = MibTableColumn
starPmMisinsertedCellCount = _StarPmMisinsertedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 8, 1, 6),
    _StarPmMisinsertedCellCount_Type()
)
starPmMisinsertedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPmMisinsertedCellCount.setStatus("mandatory")
_StarPmSeverelyErroredBlockCount_Type = Integer32
_StarPmSeverelyErroredBlockCount_Object = MibTableColumn
starPmSeverelyErroredBlockCount = _StarPmSeverelyErroredBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 8, 1, 7),
    _StarPmSeverelyErroredBlockCount_Type()
)
starPmSeverelyErroredBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPmSeverelyErroredBlockCount.setStatus("mandatory")
_StarPvcRouteTable_Object = MibTable
starPvcRouteTable = _StarPvcRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9)
)
if mibBuilder.loadTexts:
    starPvcRouteTable.setStatus("mandatory")
_StarPvcRouteEntry_Object = MibTableRow
starPvcRouteEntry = _StarPvcRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1)
)
starPvcRouteEntry.setIndexNames(
    (0, "STARNE-MIB", "starPvcRouteGCIDSlotId"),
    (0, "STARNE-MIB", "starPvcRouteGCIDPortId"),
    (0, "STARNE-MIB", "starPvcRouteGCIDIfType"),
    (0, "STARNE-MIB", "starPvcRouteGCIDConnId"),
    (0, "STARNE-MIB", "starPvcRouteGCIDLeafId"),
    (0, "STARNE-MIB", "starPvcRouteHopIndex"),
)
if mibBuilder.loadTexts:
    starPvcRouteEntry.setStatus("mandatory")
_StarPvcRouteGCIDSlotId_Type = Integer32
_StarPvcRouteGCIDSlotId_Object = MibTableColumn
starPvcRouteGCIDSlotId = _StarPvcRouteGCIDSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 1),
    _StarPvcRouteGCIDSlotId_Type()
)
starPvcRouteGCIDSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteGCIDSlotId.setStatus("mandatory")
_StarPvcRouteGCIDPortId_Type = Integer32
_StarPvcRouteGCIDPortId_Object = MibTableColumn
starPvcRouteGCIDPortId = _StarPvcRouteGCIDPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 2),
    _StarPvcRouteGCIDPortId_Type()
)
starPvcRouteGCIDPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteGCIDPortId.setStatus("mandatory")
_StarPvcRouteGCIDIfType_Type = Integer32
_StarPvcRouteGCIDIfType_Object = MibTableColumn
starPvcRouteGCIDIfType = _StarPvcRouteGCIDIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 3),
    _StarPvcRouteGCIDIfType_Type()
)
starPvcRouteGCIDIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteGCIDIfType.setStatus("mandatory")
_StarPvcRouteGCIDConnId_Type = Integer32
_StarPvcRouteGCIDConnId_Object = MibTableColumn
starPvcRouteGCIDConnId = _StarPvcRouteGCIDConnId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 4),
    _StarPvcRouteGCIDConnId_Type()
)
starPvcRouteGCIDConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteGCIDConnId.setStatus("mandatory")
_StarPvcRouteGCIDLeafId_Type = Integer32
_StarPvcRouteGCIDLeafId_Object = MibTableColumn
starPvcRouteGCIDLeafId = _StarPvcRouteGCIDLeafId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 5),
    _StarPvcRouteGCIDLeafId_Type()
)
starPvcRouteGCIDLeafId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteGCIDLeafId.setStatus("mandatory")
_StarPvcRouteHopIndex_Type = Integer32
_StarPvcRouteHopIndex_Object = MibTableColumn
starPvcRouteHopIndex = _StarPvcRouteHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 6),
    _StarPvcRouteHopIndex_Type()
)
starPvcRouteHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteHopIndex.setStatus("mandatory")
_StarPvcRouteOutgoingNeId_Type = Integer32
_StarPvcRouteOutgoingNeId_Object = MibTableColumn
starPvcRouteOutgoingNeId = _StarPvcRouteOutgoingNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 7),
    _StarPvcRouteOutgoingNeId_Type()
)
starPvcRouteOutgoingNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteOutgoingNeId.setStatus("mandatory")


class _StarPvcRouteOutgoingNodeType_Type(Integer32):
    """Custom type starPvcRouteOutgoingNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dest", 3),
          ("source", 1),
          ("transit", 2))
    )


_StarPvcRouteOutgoingNodeType_Type.__name__ = "Integer32"
_StarPvcRouteOutgoingNodeType_Object = MibTableColumn
starPvcRouteOutgoingNodeType = _StarPvcRouteOutgoingNodeType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 8),
    _StarPvcRouteOutgoingNodeType_Type()
)
starPvcRouteOutgoingNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteOutgoingNodeType.setStatus("mandatory")
_StarPvcRouteOutgoingModuleId_Type = Integer32
_StarPvcRouteOutgoingModuleId_Object = MibTableColumn
starPvcRouteOutgoingModuleId = _StarPvcRouteOutgoingModuleId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 9),
    _StarPvcRouteOutgoingModuleId_Type()
)
starPvcRouteOutgoingModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteOutgoingModuleId.setStatus("mandatory")
_StarPvcRouteOutgoingPortId_Type = Integer32
_StarPvcRouteOutgoingPortId_Object = MibTableColumn
starPvcRouteOutgoingPortId = _StarPvcRouteOutgoingPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 9, 1, 10),
    _StarPvcRouteOutgoingPortId_Type()
)
starPvcRouteOutgoingPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteOutgoingPortId.setStatus("mandatory")
_StarCcCtrTable_Object = MibTable
starCcCtrTable = _StarCcCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10)
)
if mibBuilder.loadTexts:
    starCcCtrTable.setStatus("mandatory")
_StarCcCtrEntry_Object = MibTableRow
starCcCtrEntry = _StarCcCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1)
)
starCcCtrEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
)
if mibBuilder.loadTexts:
    starCcCtrEntry.setStatus("mandatory")
_StarCcCtrPortIndex_Type = Integer32
_StarCcCtrPortIndex_Object = MibTableColumn
starCcCtrPortIndex = _StarCcCtrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 1),
    _StarCcCtrPortIndex_Type()
)
starCcCtrPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrPortIndex.setStatus("mandatory")
_StarCcCtrVpi_Type = Integer32
_StarCcCtrVpi_Object = MibTableColumn
starCcCtrVpi = _StarCcCtrVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 2),
    _StarCcCtrVpi_Type()
)
starCcCtrVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrVpi.setStatus("mandatory")
_StarCcCtrVci_Type = Integer32
_StarCcCtrVci_Object = MibTableColumn
starCcCtrVci = _StarCcCtrVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 3),
    _StarCcCtrVci_Type()
)
starCcCtrVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrVci.setStatus("mandatory")


class _StarCcCtrType_Type(Integer32):
    """Custom type starCcCtrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oam-f4", 1),
          ("oam-f5", 2))
    )


_StarCcCtrType_Type.__name__ = "Integer32"
_StarCcCtrType_Object = MibTableColumn
starCcCtrType = _StarCcCtrType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 4),
    _StarCcCtrType_Type()
)
starCcCtrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrType.setStatus("mandatory")


class _StarCcCtrEndType_Type(Integer32):
    """Custom type starCcCtrEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connection-end", 2),
          ("segment", 1))
    )


_StarCcCtrEndType_Type.__name__ = "Integer32"
_StarCcCtrEndType_Object = MibTableColumn
starCcCtrEndType = _StarCcCtrEndType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 5),
    _StarCcCtrEndType_Type()
)
starCcCtrEndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrEndType.setStatus("mandatory")


class _StarCcCtrSetup_Type(Integer32):
    """Custom type starCcCtrSetup based on Integer32"""
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
        *(("finishccreceiver", 3),
          ("finishccsender", 4),
          ("initccreceiver", 2),
          ("initccsender", 1))
    )


_StarCcCtrSetup_Type.__name__ = "Integer32"
_StarCcCtrSetup_Object = MibTableColumn
starCcCtrSetup = _StarCcCtrSetup_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 6),
    _StarCcCtrSetup_Type()
)
starCcCtrSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrSetup.setStatus("mandatory")


class _StarCcCtrInputType_Type(Integer32):
    """Custom type starCcCtrInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gcid", 1),
          ("vcci", 2))
    )


_StarCcCtrInputType_Type.__name__ = "Integer32"
_StarCcCtrInputType_Object = MibTableColumn
starCcCtrInputType = _StarCcCtrInputType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 7),
    _StarCcCtrInputType_Type()
)
starCcCtrInputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrInputType.setStatus("mandatory")
_StarCcCtrGCIDNeId_Type = Integer32
_StarCcCtrGCIDNeId_Object = MibTableColumn
starCcCtrGCIDNeId = _StarCcCtrGCIDNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 8),
    _StarCcCtrGCIDNeId_Type()
)
starCcCtrGCIDNeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrGCIDNeId.setStatus("mandatory")
_StarCcCtrGCIDSlotIndex_Type = Integer32
_StarCcCtrGCIDSlotIndex_Object = MibTableColumn
starCcCtrGCIDSlotIndex = _StarCcCtrGCIDSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 9),
    _StarCcCtrGCIDSlotIndex_Type()
)
starCcCtrGCIDSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrGCIDSlotIndex.setStatus("mandatory")
_StarCcCtrGCIDPortIndex_Type = Integer32
_StarCcCtrGCIDPortIndex_Object = MibTableColumn
starCcCtrGCIDPortIndex = _StarCcCtrGCIDPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 10),
    _StarCcCtrGCIDPortIndex_Type()
)
starCcCtrGCIDPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrGCIDPortIndex.setStatus("mandatory")
_StarCcCtrGCIDModuleIfType_Type = Integer32
_StarCcCtrGCIDModuleIfType_Object = MibTableColumn
starCcCtrGCIDModuleIfType = _StarCcCtrGCIDModuleIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 11),
    _StarCcCtrGCIDModuleIfType_Type()
)
starCcCtrGCIDModuleIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrGCIDModuleIfType.setStatus("mandatory")
_StarCcCtrGCIDVpi_Type = Integer32
_StarCcCtrGCIDVpi_Object = MibTableColumn
starCcCtrGCIDVpi = _StarCcCtrGCIDVpi_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 12),
    _StarCcCtrGCIDVpi_Type()
)
starCcCtrGCIDVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrGCIDVpi.setStatus("mandatory")
_StarCcCtrGCIDVci_Type = Integer32
_StarCcCtrGCIDVci_Object = MibTableColumn
starCcCtrGCIDVci = _StarCcCtrGCIDVci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 13),
    _StarCcCtrGCIDVci_Type()
)
starCcCtrGCIDVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrGCIDVci.setStatus("mandatory")
_StarCcCtrGCIDDlci_Type = Integer32
_StarCcCtrGCIDDlci_Object = MibTableColumn
starCcCtrGCIDDlci = _StarCcCtrGCIDDlci_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 14),
    _StarCcCtrGCIDDlci_Type()
)
starCcCtrGCIDDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrGCIDDlci.setStatus("mandatory")
_StarCcCtrGCIDTimeSlot_Type = Integer32
_StarCcCtrGCIDTimeSlot_Object = MibTableColumn
starCcCtrGCIDTimeSlot = _StarCcCtrGCIDTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 15),
    _StarCcCtrGCIDTimeSlot_Type()
)
starCcCtrGCIDTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrGCIDTimeSlot.setStatus("mandatory")
_StarCcCtrGCIDLeafNum_Type = Integer32
_StarCcCtrGCIDLeafNum_Object = MibTableColumn
starCcCtrGCIDLeafNum = _StarCcCtrGCIDLeafNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 10, 1, 16),
    _StarCcCtrGCIDLeafNum_Type()
)
starCcCtrGCIDLeafNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starCcCtrGCIDLeafNum.setStatus("mandatory")
_StarPortCellStatsTable_Object = MibTable
starPortCellStatsTable = _StarPortCellStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11)
)
if mibBuilder.loadTexts:
    starPortCellStatsTable.setStatus("mandatory")
_StarPortCellStatsEntry_Object = MibTableRow
starPortCellStatsEntry = _StarPortCellStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1)
)
starPortCellStatsEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starPortCellStatsEntry.setStatus("mandatory")
_StarPortTimeStamp_Type = Counter32
_StarPortTimeStamp_Object = MibTableColumn
starPortTimeStamp = _StarPortTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1, 1),
    _StarPortTimeStamp_Type()
)
starPortTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortTimeStamp.setStatus("mandatory")
_StarPortRtCellsRxCount_Type = Counter32
_StarPortRtCellsRxCount_Object = MibTableColumn
starPortRtCellsRxCount = _StarPortRtCellsRxCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1, 2),
    _StarPortRtCellsRxCount_Type()
)
starPortRtCellsRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortRtCellsRxCount.setStatus("mandatory")
_StarPortRtCellsDroppedCount_Type = Counter32
_StarPortRtCellsDroppedCount_Object = MibTableColumn
starPortRtCellsDroppedCount = _StarPortRtCellsDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1, 3),
    _StarPortRtCellsDroppedCount_Type()
)
starPortRtCellsDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortRtCellsDroppedCount.setStatus("mandatory")
_StarPortRtCellsCongCount_Type = Counter32
_StarPortRtCellsCongCount_Object = MibTableColumn
starPortRtCellsCongCount = _StarPortRtCellsCongCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1, 4),
    _StarPortRtCellsCongCount_Type()
)
starPortRtCellsCongCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortRtCellsCongCount.setStatus("mandatory")
_StarPortUpcCellsCLP0_Type = Counter32
_StarPortUpcCellsCLP0_Object = MibTableColumn
starPortUpcCellsCLP0 = _StarPortUpcCellsCLP0_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1, 5),
    _StarPortUpcCellsCLP0_Type()
)
starPortUpcCellsCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUpcCellsCLP0.setStatus("mandatory")
_StarPortUpcTotalCells_Type = Counter32
_StarPortUpcTotalCells_Object = MibTableColumn
starPortUpcTotalCells = _StarPortUpcTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1, 6),
    _StarPortUpcTotalCells_Type()
)
starPortUpcTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUpcTotalCells.setStatus("mandatory")
_StarPortUpcGcra0ViolCount_Type = Counter32
_StarPortUpcGcra0ViolCount_Object = MibTableColumn
starPortUpcGcra0ViolCount = _StarPortUpcGcra0ViolCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1, 7),
    _StarPortUpcGcra0ViolCount_Type()
)
starPortUpcGcra0ViolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUpcGcra0ViolCount.setStatus("mandatory")
_StarPortUpcGcra1ViolCount_Type = Counter32
_StarPortUpcGcra1ViolCount_Object = MibTableColumn
starPortUpcGcra1ViolCount = _StarPortUpcGcra1ViolCount_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1, 8),
    _StarPortUpcGcra1ViolCount_Type()
)
starPortUpcGcra1ViolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUpcGcra1ViolCount.setStatus("mandatory")
_StarPortUpcTotalOAMCells_Type = Counter32
_StarPortUpcTotalOAMCells_Object = MibTableColumn
starPortUpcTotalOAMCells = _StarPortUpcTotalOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 11, 1, 9),
    _StarPortUpcTotalOAMCells_Type()
)
starPortUpcTotalOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPortUpcTotalOAMCells.setStatus("mandatory")
_StarAtmPointTable_Object = MibTable
starAtmPointTable = _StarAtmPointTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 13)
)
if mibBuilder.loadTexts:
    starAtmPointTable.setStatus("mandatory")
_StarAtmPointEntry_Object = MibTableRow
starAtmPointEntry = _StarAtmPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 13, 1)
)
starAtmPointEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
    (0, "STARNE-MIB", "starLoopbackCtrGCIDNeId"),
    (0, "STARNE-MIB", "starLoopbackCtrGCIDSlotIndex"),
    (0, "STARNE-MIB", "starLoopbackCtrGCIDPortIndex"),
    (0, "STARNE-MIB", "starLoopbackCtrGCIDModuleIfType"),
    (0, "STARNE-MIB", "starLoopbackCtrGCIDVpi"),
    (0, "STARNE-MIB", "starLoopbackCtrGCIDVci"),
    (0, "STARNE-MIB", "starLoopbackCtrGCIDDlci"),
    (0, "STARNE-MIB", "starLoopbackCtrGCIDTimeSlot"),
    (0, "STARNE-MIB", "starLoopbackCtrGCIDLeafNum"),
)
if mibBuilder.loadTexts:
    starAtmPointEntry.setStatus("mandatory")


class _StarAtmPointPointType_Type(Integer32):
    """Custom type starAtmPointPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connectionend", 2),
          ("intermediate", 3),
          ("segmentend", 1))
    )


_StarAtmPointPointType_Type.__name__ = "Integer32"
_StarAtmPointPointType_Object = MibTableColumn
starAtmPointPointType = _StarAtmPointPointType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 13, 1, 1),
    _StarAtmPointPointType_Type()
)
starAtmPointPointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starAtmPointPointType.setStatus("mandatory")
_StarSvcRouteTable_Object = MibTable
starSvcRouteTable = _StarSvcRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14)
)
if mibBuilder.loadTexts:
    starSvcRouteTable.setStatus("mandatory")
_StarSvcRouteEntry_Object = MibTableRow
starSvcRouteEntry = _StarSvcRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1)
)
starSvcRouteEntry.setIndexNames(
    (0, "STARNE-MIB", "starSvcRouteGCIDSlotId"),
    (0, "STARNE-MIB", "starSvcRouteGCIDPortId"),
    (0, "STARNE-MIB", "starSvcRouteGCIDIfType"),
    (0, "STARNE-MIB", "starSvcRouteGCIDConnId"),
    (0, "STARNE-MIB", "starSvcRouteGCIDLeafId"),
    (0, "STARNE-MIB", "starSvcRouteHopIndex"),
)
if mibBuilder.loadTexts:
    starSvcRouteEntry.setStatus("mandatory")
_StarSvcRouteGCIDSlotId_Type = Integer32
_StarSvcRouteGCIDSlotId_Object = MibTableColumn
starSvcRouteGCIDSlotId = _StarSvcRouteGCIDSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 1),
    _StarSvcRouteGCIDSlotId_Type()
)
starSvcRouteGCIDSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteGCIDSlotId.setStatus("mandatory")
_StarSvcRouteGCIDPortId_Type = Integer32
_StarSvcRouteGCIDPortId_Object = MibTableColumn
starSvcRouteGCIDPortId = _StarSvcRouteGCIDPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 2),
    _StarSvcRouteGCIDPortId_Type()
)
starSvcRouteGCIDPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteGCIDPortId.setStatus("mandatory")
_StarSvcRouteGCIDIfType_Type = Integer32
_StarSvcRouteGCIDIfType_Object = MibTableColumn
starSvcRouteGCIDIfType = _StarSvcRouteGCIDIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 3),
    _StarSvcRouteGCIDIfType_Type()
)
starSvcRouteGCIDIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteGCIDIfType.setStatus("mandatory")
_StarSvcRouteGCIDConnId_Type = Integer32
_StarSvcRouteGCIDConnId_Object = MibTableColumn
starSvcRouteGCIDConnId = _StarSvcRouteGCIDConnId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 4),
    _StarSvcRouteGCIDConnId_Type()
)
starSvcRouteGCIDConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteGCIDConnId.setStatus("mandatory")
_StarSvcRouteGCIDLeafId_Type = Integer32
_StarSvcRouteGCIDLeafId_Object = MibTableColumn
starSvcRouteGCIDLeafId = _StarSvcRouteGCIDLeafId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 5),
    _StarSvcRouteGCIDLeafId_Type()
)
starSvcRouteGCIDLeafId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteGCIDLeafId.setStatus("mandatory")
_StarSvcRouteHopIndex_Type = Integer32
_StarSvcRouteHopIndex_Object = MibTableColumn
starSvcRouteHopIndex = _StarSvcRouteHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 6),
    _StarSvcRouteHopIndex_Type()
)
starSvcRouteHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteHopIndex.setStatus("mandatory")
_StarSvcRouteOutgoingNeId_Type = Integer32
_StarSvcRouteOutgoingNeId_Object = MibTableColumn
starSvcRouteOutgoingNeId = _StarSvcRouteOutgoingNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 7),
    _StarSvcRouteOutgoingNeId_Type()
)
starSvcRouteOutgoingNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteOutgoingNeId.setStatus("mandatory")


class _StarSvcRouteOutgoingNodeType_Type(Integer32):
    """Custom type starSvcRouteOutgoingNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dest", 3),
          ("source", 1),
          ("transit", 2))
    )


_StarSvcRouteOutgoingNodeType_Type.__name__ = "Integer32"
_StarSvcRouteOutgoingNodeType_Object = MibTableColumn
starSvcRouteOutgoingNodeType = _StarSvcRouteOutgoingNodeType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 8),
    _StarSvcRouteOutgoingNodeType_Type()
)
starSvcRouteOutgoingNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteOutgoingNodeType.setStatus("mandatory")
_StarSvcRouteOutgoingModuleId_Type = Integer32
_StarSvcRouteOutgoingModuleId_Object = MibTableColumn
starSvcRouteOutgoingModuleId = _StarSvcRouteOutgoingModuleId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 9),
    _StarSvcRouteOutgoingModuleId_Type()
)
starSvcRouteOutgoingModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteOutgoingModuleId.setStatus("mandatory")
_StarSvcRouteOutgoingPortId_Type = Integer32
_StarSvcRouteOutgoingPortId_Object = MibTableColumn
starSvcRouteOutgoingPortId = _StarSvcRouteOutgoingPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 14, 1, 10),
    _StarSvcRouteOutgoingPortId_Type()
)
starSvcRouteOutgoingPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcRouteOutgoingPortId.setStatus("mandatory")
_StarPVCRouteTable_Object = MibTable
starPVCRouteTable = _StarPVCRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15)
)
if mibBuilder.loadTexts:
    starPVCRouteTable.setStatus("mandatory")
_StarPVCRouteEntry_Object = MibTableRow
starPVCRouteEntry = _StarPVCRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1)
)
starPVCRouteEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
    (0, "STARNE-MIB", "starPvcRouteAdjacentNodeType"),
    (0, "STARNE-MIB", "starPvcRouteSrcGCIDNeId"),
    (0, "STARNE-MIB", "starPvcRouteSrcGCIDSlotId"),
    (0, "STARNE-MIB", "starPvcRouteSrcGCIDPortId"),
    (0, "STARNE-MIB", "starPvcRouteSrcGCIDIfType"),
    (0, "STARNE-MIB", "starPvcRouteSrcGCIDConnId"),
    (0, "STARNE-MIB", "starPvcRouteSrcGCIDLeafId"),
)
if mibBuilder.loadTexts:
    starPVCRouteEntry.setStatus("mandatory")
_StarPvcRouteSrcGCIDNeId_Type = Integer32
_StarPvcRouteSrcGCIDNeId_Object = MibTableColumn
starPvcRouteSrcGCIDNeId = _StarPvcRouteSrcGCIDNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 1),
    _StarPvcRouteSrcGCIDNeId_Type()
)
starPvcRouteSrcGCIDNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteSrcGCIDNeId.setStatus("mandatory")
_StarPvcRouteSrcGCIDSlotId_Type = Integer32
_StarPvcRouteSrcGCIDSlotId_Object = MibTableColumn
starPvcRouteSrcGCIDSlotId = _StarPvcRouteSrcGCIDSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 2),
    _StarPvcRouteSrcGCIDSlotId_Type()
)
starPvcRouteSrcGCIDSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteSrcGCIDSlotId.setStatus("mandatory")
_StarPvcRouteSrcGCIDPortId_Type = Integer32
_StarPvcRouteSrcGCIDPortId_Object = MibTableColumn
starPvcRouteSrcGCIDPortId = _StarPvcRouteSrcGCIDPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 3),
    _StarPvcRouteSrcGCIDPortId_Type()
)
starPvcRouteSrcGCIDPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteSrcGCIDPortId.setStatus("mandatory")
_StarPvcRouteSrcGCIDIfType_Type = Integer32
_StarPvcRouteSrcGCIDIfType_Object = MibTableColumn
starPvcRouteSrcGCIDIfType = _StarPvcRouteSrcGCIDIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 4),
    _StarPvcRouteSrcGCIDIfType_Type()
)
starPvcRouteSrcGCIDIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteSrcGCIDIfType.setStatus("mandatory")
_StarPvcRouteSrcGCIDConnId_Type = Integer32
_StarPvcRouteSrcGCIDConnId_Object = MibTableColumn
starPvcRouteSrcGCIDConnId = _StarPvcRouteSrcGCIDConnId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 5),
    _StarPvcRouteSrcGCIDConnId_Type()
)
starPvcRouteSrcGCIDConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteSrcGCIDConnId.setStatus("mandatory")
_StarPvcRouteSrcGCIDLeafId_Type = Integer32
_StarPvcRouteSrcGCIDLeafId_Object = MibTableColumn
starPvcRouteSrcGCIDLeafId = _StarPvcRouteSrcGCIDLeafId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 6),
    _StarPvcRouteSrcGCIDLeafId_Type()
)
starPvcRouteSrcGCIDLeafId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteSrcGCIDLeafId.setStatus("mandatory")
_StarPvcRouteAdjacentNeId_Type = Integer32
_StarPvcRouteAdjacentNeId_Object = MibTableColumn
starPvcRouteAdjacentNeId = _StarPvcRouteAdjacentNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 7),
    _StarPvcRouteAdjacentNeId_Type()
)
starPvcRouteAdjacentNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteAdjacentNeId.setStatus("mandatory")
_StarPvcRouteAdjacentSlotId_Type = Integer32
_StarPvcRouteAdjacentSlotId_Object = MibTableColumn
starPvcRouteAdjacentSlotId = _StarPvcRouteAdjacentSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 8),
    _StarPvcRouteAdjacentSlotId_Type()
)
starPvcRouteAdjacentSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteAdjacentSlotId.setStatus("mandatory")
_StarPvcRouteAdjacentPortId_Type = Integer32
_StarPvcRouteAdjacentPortId_Object = MibTableColumn
starPvcRouteAdjacentPortId = _StarPvcRouteAdjacentPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 9),
    _StarPvcRouteAdjacentPortId_Type()
)
starPvcRouteAdjacentPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteAdjacentPortId.setStatus("mandatory")


class _StarPvcRouteAdjacentNodeType_Type(Integer32):
    """Custom type starPvcRouteAdjacentNodeType based on Integer32"""
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
        *(("dest", 4),
          ("incoming", 2),
          ("outgoing", 3),
          ("source", 1))
    )


_StarPvcRouteAdjacentNodeType_Type.__name__ = "Integer32"
_StarPvcRouteAdjacentNodeType_Object = MibTableColumn
starPvcRouteAdjacentNodeType = _StarPvcRouteAdjacentNodeType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 10),
    _StarPvcRouteAdjacentNodeType_Type()
)
starPvcRouteAdjacentNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteAdjacentNodeType.setStatus("mandatory")


class _StarPvcRouteLocalNodeType_Type(Integer32):
    """Custom type starPvcRouteLocalNodeType based on Integer32"""
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
        *(("dest", 4),
          ("incoming", 2),
          ("outgoing", 3),
          ("source", 1))
    )


_StarPvcRouteLocalNodeType_Type.__name__ = "Integer32"
_StarPvcRouteLocalNodeType_Object = MibTableColumn
starPvcRouteLocalNodeType = _StarPvcRouteLocalNodeType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 11),
    _StarPvcRouteLocalNodeType_Type()
)
starPvcRouteLocalNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteLocalNodeType.setStatus("mandatory")
_StarPvcRouteLocalIfType_Type = Integer32
_StarPvcRouteLocalIfType_Object = MibTableColumn
starPvcRouteLocalIfType = _StarPvcRouteLocalIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 12),
    _StarPvcRouteLocalIfType_Type()
)
starPvcRouteLocalIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteLocalIfType.setStatus("mandatory")
_StarPvcRouteLocalConnId_Type = Integer32
_StarPvcRouteLocalConnId_Object = MibTableColumn
starPvcRouteLocalConnId = _StarPvcRouteLocalConnId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 13),
    _StarPvcRouteLocalConnId_Type()
)
starPvcRouteLocalConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteLocalConnId.setStatus("mandatory")
_StarPvcRouteLocalLeafId_Type = Integer32
_StarPvcRouteLocalLeafId_Object = MibTableColumn
starPvcRouteLocalLeafId = _StarPvcRouteLocalLeafId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 14),
    _StarPvcRouteLocalLeafId_Type()
)
starPvcRouteLocalLeafId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteLocalLeafId.setStatus("mandatory")
_StarPvcRouteQueryDescr_Type = OctetString
_StarPvcRouteQueryDescr_Object = MibTableColumn
starPvcRouteQueryDescr = _StarPvcRouteQueryDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 4, 15, 1, 15),
    _StarPvcRouteQueryDescr_Type()
)
starPvcRouteQueryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcRouteQueryDescr.setStatus("mandatory")
_StarBackbone_ObjectIdentity = ObjectIdentity
starBackbone = _StarBackbone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 5)
)
_StarBackboneLinkTable_Object = MibTable
starBackboneLinkTable = _StarBackboneLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 5, 1)
)
if mibBuilder.loadTexts:
    starBackboneLinkTable.setStatus("mandatory")
_StarBackboneLinkEntry_Object = MibTableRow
starBackboneLinkEntry = _StarBackboneLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 5, 1, 1)
)
starBackboneLinkEntry.setIndexNames(
    (0, "STARNE-MIB", "starSlotIndex"),
    (0, "STARNE-MIB", "starPortIndex"),
)
if mibBuilder.loadTexts:
    starBackboneLinkEntry.setStatus("mandatory")
_StarBackboneLinkStatus_Type = Integer32
_StarBackboneLinkStatus_Object = MibTableColumn
starBackboneLinkStatus = _StarBackboneLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 5, 1, 1, 1),
    _StarBackboneLinkStatus_Type()
)
starBackboneLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBackboneLinkStatus.setStatus("mandatory")
_StarBackboneLinkDestNodeId_Type = Integer32
_StarBackboneLinkDestNodeId_Object = MibTableColumn
starBackboneLinkDestNodeId = _StarBackboneLinkDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 5, 1, 1, 2),
    _StarBackboneLinkDestNodeId_Type()
)
starBackboneLinkDestNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBackboneLinkDestNodeId.setStatus("mandatory")
_StarBackboneLinkDestSlotId_Type = Integer32
_StarBackboneLinkDestSlotId_Object = MibTableColumn
starBackboneLinkDestSlotId = _StarBackboneLinkDestSlotId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 5, 1, 1, 3),
    _StarBackboneLinkDestSlotId_Type()
)
starBackboneLinkDestSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBackboneLinkDestSlotId.setStatus("mandatory")
_StarBackboneLinkDestPortId_Type = Integer32
_StarBackboneLinkDestPortId_Object = MibTableColumn
starBackboneLinkDestPortId = _StarBackboneLinkDestPortId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 5, 1, 1, 4),
    _StarBackboneLinkDestPortId_Type()
)
starBackboneLinkDestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBackboneLinkDestPortId.setStatus("mandatory")
_StarBackboneLinkIfType_Type = Integer32
_StarBackboneLinkIfType_Object = MibTableColumn
starBackboneLinkIfType = _StarBackboneLinkIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 5, 1, 1, 5),
    _StarBackboneLinkIfType_Type()
)
starBackboneLinkIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBackboneLinkIfType.setStatus("mandatory")
_StarBackboneLinkConnStatus_Type = Integer32
_StarBackboneLinkConnStatus_Object = MibTableColumn
starBackboneLinkConnStatus = _StarBackboneLinkConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 5, 1, 1, 6),
    _StarBackboneLinkConnStatus_Type()
)
starBackboneLinkConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBackboneLinkConnStatus.setStatus("mandatory")
_StarTrap_ObjectIdentity = ObjectIdentity
starTrap = _StarTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 5, 6)
)
_StarTrapPriority_Type = Integer32
_StarTrapPriority_Object = MibScalar
starTrapPriority = _StarTrapPriority_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 1),
    _StarTrapPriority_Type()
)
starTrapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starTrapPriority.setStatus("mandatory")
_StarReturnedErrorCode_Type = Integer32
_StarReturnedErrorCode_Object = MibScalar
starReturnedErrorCode = _StarReturnedErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 2),
    _StarReturnedErrorCode_Type()
)
starReturnedErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starReturnedErrorCode.setStatus("mandatory")
_StarCfPSUNum_Type = Integer32
_StarCfPSUNum_Object = MibScalar
starCfPSUNum = _StarCfPSUNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 3),
    _StarCfPSUNum_Type()
)
starCfPSUNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfPSUNum.setStatus("mandatory")
_StarCfFANNum_Type = Integer32
_StarCfFANNum_Object = MibScalar
starCfFANNum = _StarCfFANNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 4),
    _StarCfFANNum_Type()
)
starCfFANNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfFANNum.setStatus("mandatory")
_StarCfSlotActualBoardType_Type = Integer32
_StarCfSlotActualBoardType_Object = MibScalar
starCfSlotActualBoardType = _StarCfSlotActualBoardType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 5),
    _StarCfSlotActualBoardType_Type()
)
starCfSlotActualBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfSlotActualBoardType.setStatus("mandatory")
_StarCfConfiguredBoardType_Type = Integer32
_StarCfConfiguredBoardType_Object = MibScalar
starCfConfiguredBoardType = _StarCfConfiguredBoardType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 6),
    _StarCfConfiguredBoardType_Type()
)
starCfConfiguredBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfConfiguredBoardType.setStatus("mandatory")
_StarCfActualFileVersion_Type = Integer32
_StarCfActualFileVersion_Object = MibScalar
starCfActualFileVersion = _StarCfActualFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 7),
    _StarCfActualFileVersion_Type()
)
starCfActualFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfActualFileVersion.setStatus("mandatory")
_StarCfConfiguredFileVersion_Type = Integer32
_StarCfConfiguredFileVersion_Object = MibScalar
starCfConfiguredFileVersion = _StarCfConfiguredFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 8),
    _StarCfConfiguredFileVersion_Type()
)
starCfConfiguredFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCfConfiguredFileVersion.setStatus("mandatory")
_StarTaskName_Type = DisplayString
_StarTaskName_Object = MibScalar
starTaskName = _StarTaskName_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 9),
    _StarTaskName_Type()
)
starTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starTaskName.setStatus("mandatory")
_StarQueueName_Type = DisplayString
_StarQueueName_Object = MibScalar
starQueueName = _StarQueueName_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 10),
    _StarQueueName_Type()
)
starQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starQueueName.setStatus("mandatory")
_StarMsgSize_Type = Integer32
_StarMsgSize_Object = MibScalar
starMsgSize = _StarMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 11),
    _StarMsgSize_Type()
)
starMsgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starMsgSize.setStatus("mandatory")
_StarFileName_Type = DisplayString
_StarFileName_Object = MibScalar
starFileName = _StarFileName_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 12),
    _StarFileName_Type()
)
starFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFileName.setStatus("mandatory")
_StarDeviceType_Type = Integer32
_StarDeviceType_Object = MibScalar
starDeviceType = _StarDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 13),
    _StarDeviceType_Type()
)
starDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDeviceType.setStatus("mandatory")
_StarModuleIfType_Type = Integer32
_StarModuleIfType_Object = MibScalar
starModuleIfType = _StarModuleIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 14),
    _StarModuleIfType_Type()
)
starModuleIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starModuleIfType.setStatus("mandatory")
_StarRefClkIndex_Type = Integer32
_StarRefClkIndex_Object = MibScalar
starRefClkIndex = _StarRefClkIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 15),
    _StarRefClkIndex_Type()
)
starRefClkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRefClkIndex.setStatus("mandatory")


class _StarEthernetType_Type(Integer32):
    """Custom type starEthernetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipc1", 2),
          ("ipc2", 3),
          ("nms", 1))
    )


_StarEthernetType_Type.__name__ = "Integer32"
_StarEthernetType_Object = MibScalar
starEthernetType = _StarEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 16),
    _StarEthernetType_Type()
)
starEthernetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starEthernetType.setStatus("mandatory")
_StarDS1ChanIndex_Type = Integer32
_StarDS1ChanIndex_Object = MibScalar
starDS1ChanIndex = _StarDS1ChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 17),
    _StarDS1ChanIndex_Type()
)
starDS1ChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS1ChanIndex.setStatus("mandatory")
_StarDS2ChanIndex_Type = Integer32
_StarDS2ChanIndex_Object = MibScalar
starDS2ChanIndex = _StarDS2ChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 18),
    _StarDS2ChanIndex_Type()
)
starDS2ChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDS2ChanIndex.setStatus("mandatory")
_StarDeviceId_Type = Integer32
_StarDeviceId_Object = MibScalar
starDeviceId = _StarDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 19),
    _StarDeviceId_Type()
)
starDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starDeviceId.setStatus("mandatory")
_StarRcvdMsgType_Type = Integer32
_StarRcvdMsgType_Object = MibScalar
starRcvdMsgType = _StarRcvdMsgType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 20),
    _StarRcvdMsgType_Type()
)
starRcvdMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRcvdMsgType.setStatus("mandatory")
_StarReturnedSlotIndex_Type = Integer32
_StarReturnedSlotIndex_Object = MibScalar
starReturnedSlotIndex = _StarReturnedSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 21),
    _StarReturnedSlotIndex_Type()
)
starReturnedSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starReturnedSlotIndex.setStatus("mandatory")
_StarRcvdSrcSlotIndex_Type = Integer32
_StarRcvdSrcSlotIndex_Object = MibScalar
starRcvdSrcSlotIndex = _StarRcvdSrcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 22),
    _StarRcvdSrcSlotIndex_Type()
)
starRcvdSrcSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRcvdSrcSlotIndex.setStatus("mandatory")
_StarRcvdModuleIfType_Type = Integer32
_StarRcvdModuleIfType_Object = MibScalar
starRcvdModuleIfType = _StarRcvdModuleIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 23),
    _StarRcvdModuleIfType_Type()
)
starRcvdModuleIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRcvdModuleIfType.setStatus("mandatory")
_StarFileId_Type = Integer32
_StarFileId_Object = MibScalar
starFileId = _StarFileId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 24),
    _StarFileId_Type()
)
starFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFileId.setStatus("mandatory")
_StarCOSId_Type = Integer32
_StarCOSId_Object = MibScalar
starCOSId = _StarCOSId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 25),
    _StarCOSId_Type()
)
starCOSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCOSId.setStatus("mandatory")
_StarRcvdModuleType_Type = Integer32
_StarRcvdModuleType_Object = MibScalar
starRcvdModuleType = _StarRcvdModuleType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 26),
    _StarRcvdModuleType_Type()
)
starRcvdModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRcvdModuleType.setStatus("mandatory")
_StarRcvdGroupId_Type = Integer32
_StarRcvdGroupId_Object = MibScalar
starRcvdGroupId = _StarRcvdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 27),
    _StarRcvdGroupId_Type()
)
starRcvdGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRcvdGroupId.setStatus("mandatory")
_StarRcvdSubId_Type = Integer32
_StarRcvdSubId_Object = MibScalar
starRcvdSubId = _StarRcvdSubId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 28),
    _StarRcvdSubId_Type()
)
starRcvdSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRcvdSubId.setStatus("mandatory")
_StarGcidNeId_Type = Integer32
_StarGcidNeId_Object = MibScalar
starGcidNeId = _StarGcidNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 29),
    _StarGcidNeId_Type()
)
starGcidNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starGcidNeId.setStatus("mandatory")
_StarGcidSlotIndex_Type = Integer32
_StarGcidSlotIndex_Object = MibScalar
starGcidSlotIndex = _StarGcidSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 30),
    _StarGcidSlotIndex_Type()
)
starGcidSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starGcidSlotIndex.setStatus("mandatory")
_StarGcidPortIndex_Type = Integer32
_StarGcidPortIndex_Object = MibScalar
starGcidPortIndex = _StarGcidPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 31),
    _StarGcidPortIndex_Type()
)
starGcidPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starGcidPortIndex.setStatus("mandatory")
_StarGcidModuleIfType_Type = Integer32
_StarGcidModuleIfType_Object = MibScalar
starGcidModuleIfType = _StarGcidModuleIfType_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 32),
    _StarGcidModuleIfType_Type()
)
starGcidModuleIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starGcidModuleIfType.setStatus("mandatory")
_StarGcidLeafNum_Type = Integer32
_StarGcidLeafNum_Object = MibScalar
starGcidLeafNum = _StarGcidLeafNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 33),
    _StarGcidLeafNum_Type()
)
starGcidLeafNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starGcidLeafNum.setStatus("mandatory")
_StarGcidConnectionNum_Type = Integer32
_StarGcidConnectionNum_Object = MibScalar
starGcidConnectionNum = _StarGcidConnectionNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 34),
    _StarGcidConnectionNum_Type()
)
starGcidConnectionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starGcidConnectionNum.setStatus("mandatory")
_StarCRSRResultedErrorCode_Type = Integer32
_StarCRSRResultedErrorCode_Object = MibScalar
starCRSRResultedErrorCode = _StarCRSRResultedErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 35),
    _StarCRSRResultedErrorCode_Type()
)
starCRSRResultedErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCRSRResultedErrorCode.setStatus("mandatory")
_StarCRSRFailedSlotIndex_Type = Integer32
_StarCRSRFailedSlotIndex_Object = MibScalar
starCRSRFailedSlotIndex = _StarCRSRFailedSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 36),
    _StarCRSRFailedSlotIndex_Type()
)
starCRSRFailedSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCRSRFailedSlotIndex.setStatus("mandatory")
_StarCRSRFailedPortIndex_Type = Integer32
_StarCRSRFailedPortIndex_Object = MibScalar
starCRSRFailedPortIndex = _StarCRSRFailedPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 37),
    _StarCRSRFailedPortIndex_Type()
)
starCRSRFailedPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCRSRFailedPortIndex.setStatus("mandatory")
_StarCRSRDescriptionCode_Type = Integer32
_StarCRSRDescriptionCode_Object = MibScalar
starCRSRDescriptionCode = _StarCRSRDescriptionCode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 38),
    _StarCRSRDescriptionCode_Type()
)
starCRSRDescriptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCRSRDescriptionCode.setStatus("mandatory")
_StarSwitchReason_Type = Integer32
_StarSwitchReason_Object = MibScalar
starSwitchReason = _StarSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 39),
    _StarSwitchReason_Type()
)
starSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSwitchReason.setStatus("mandatory")
_StarBoardFailReason_Type = Integer32
_StarBoardFailReason_Object = MibScalar
starBoardFailReason = _StarBoardFailReason_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 40),
    _StarBoardFailReason_Type()
)
starBoardFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starBoardFailReason.setStatus("mandatory")
_StarCDRGetReason_Type = Integer32
_StarCDRGetReason_Object = MibScalar
starCDRGetReason = _StarCDRGetReason_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 41),
    _StarCDRGetReason_Type()
)
starCDRGetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCDRGetReason.setStatus("mandatory")
_StarCDRFileSplitNum_Type = Integer32
_StarCDRFileSplitNum_Object = MibScalar
starCDRFileSplitNum = _StarCDRFileSplitNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 42),
    _StarCDRFileSplitNum_Type()
)
starCDRFileSplitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starCDRFileSplitNum.setStatus("mandatory")
_StarPvcmConfFaultCause_Type = Integer32
_StarPvcmConfFaultCause_Object = MibScalar
starPvcmConfFaultCause = _StarPvcmConfFaultCause_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 43),
    _StarPvcmConfFaultCause_Type()
)
starPvcmConfFaultCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starPvcmConfFaultCause.setStatus("mandatory")
_StarConnClearCause_Type = Integer32
_StarConnClearCause_Object = MibScalar
starConnClearCause = _StarConnClearCause_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 44),
    _StarConnClearCause_Type()
)
starConnClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starConnClearCause.setStatus("mandatory")
_StarRemoteNeId_Type = Integer32
_StarRemoteNeId_Object = MibScalar
starRemoteNeId = _StarRemoteNeId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 45),
    _StarRemoteNeId_Type()
)
starRemoteNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRemoteNeId.setStatus("mandatory")
_StarRemoteModuleNum_Type = Integer32
_StarRemoteModuleNum_Object = MibScalar
starRemoteModuleNum = _StarRemoteModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 46),
    _StarRemoteModuleNum_Type()
)
starRemoteModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRemoteModuleNum.setStatus("mandatory")
_StarRemotePortIndex_Type = Integer32
_StarRemotePortIndex_Object = MibScalar
starRemotePortIndex = _StarRemotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 47),
    _StarRemotePortIndex_Type()
)
starRemotePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRemotePortIndex.setStatus("mandatory")
_StarFrLmiPortIndex_Type = Integer32
_StarFrLmiPortIndex_Object = MibScalar
starFrLmiPortIndex = _StarFrLmiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 48),
    _StarFrLmiPortIndex_Type()
)
starFrLmiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFrLmiPortIndex.setStatus("mandatory")
_StarQueuePoolId_Type = Integer32
_StarQueuePoolId_Object = MibScalar
starQueuePoolId = _StarQueuePoolId_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 49),
    _StarQueuePoolId_Type()
)
starQueuePoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starQueuePoolId.setStatus("mandatory")
_StarRipAddress0_Type = Integer32
_StarRipAddress0_Object = MibScalar
starRipAddress0 = _StarRipAddress0_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 50),
    _StarRipAddress0_Type()
)
starRipAddress0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRipAddress0.setStatus("mandatory")
_StarRipAddress1_Type = Integer32
_StarRipAddress1_Object = MibScalar
starRipAddress1 = _StarRipAddress1_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 51),
    _StarRipAddress1_Type()
)
starRipAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRipAddress1.setStatus("mandatory")
_StarRipAddress2_Type = Integer32
_StarRipAddress2_Object = MibScalar
starRipAddress2 = _StarRipAddress2_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 52),
    _StarRipAddress2_Type()
)
starRipAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRipAddress2.setStatus("mandatory")
_StarRipAddress3_Type = Integer32
_StarRipAddress3_Object = MibScalar
starRipAddress3 = _StarRipAddress3_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 53),
    _StarRipAddress3_Type()
)
starRipAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRipAddress3.setStatus("mandatory")
_StarRipAddress4_Type = Integer32
_StarRipAddress4_Object = MibScalar
starRipAddress4 = _StarRipAddress4_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 54),
    _StarRipAddress4_Type()
)
starRipAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starRipAddress4.setStatus("mandatory")
_StarFatalErrorCode_Type = Integer32
_StarFatalErrorCode_Object = MibScalar
starFatalErrorCode = _StarFatalErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 55),
    _StarFatalErrorCode_Type()
)
starFatalErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starFatalErrorCode.setStatus("mandatory")
_StarSvcmCacThreshold_Type = Integer32
_StarSvcmCacThreshold_Object = MibScalar
starSvcmCacThreshold = _StarSvcmCacThreshold_Object(
    (1, 3, 6, 1, 4, 1, 236, 5, 6, 56),
    _StarSvcmCacThreshold_Type()
)
starSvcmCacThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    starSvcmCacThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STARNE-MIB",
    **{"samsung": samsung,
       "starNeMib": starNeMib,
       "starSystem": starSystem,
       "starSysGeneric": starSysGeneric,
       "starNeId": starNeId,
       "starNeDescr": starNeDescr,
       "starNeMipAddress": starNeMipAddress,
       "starNeTimeofDay": starNeTimeofDay,
       "starNeOperStatus": starNeOperStatus,
       "starNeReset": starNeReset,
       "starNeSlotReset": starNeSlotReset,
       "starNeSwDownload": starNeSwDownload,
       "starNeHwVersion": starNeHwVersion,
       "starNeBootSwVersion": starNeBootSwVersion,
       "starNeSwVersion": starNeSwVersion,
       "starNeXCoordinate": starNeXCoordinate,
       "starNeYCoordinate": starNeYCoordinate,
       "starNeNodeManagerIP": starNeNodeManagerIP,
       "starNeMasterManagerIP": starNeMasterManagerIP,
       "starNeStandbyMasterManagerIP": starNeStandbyMasterManagerIP,
       "starNeAlive": starNeAlive,
       "starMibRegister": starMibRegister,
       "starNeCurrentAlarmTftp": starNeCurrentAlarmTftp,
       "starNeCurrentTimeDescr": starNeCurrentTimeDescr,
       "starNeSoftwareVersion": starNeSoftwareVersion,
       "starNeSoftwareType": starNeSoftwareType,
       "starNeSwUpgradeDownload": starNeSwUpgradeDownload,
       "starNeSwUpgradeCancel": starNeSwUpgradeCancel,
       "starNeSwUpgradeActionTrigger": starNeSwUpgradeActionTrigger,
       "starNeSwUpgradedFiles": starNeSwUpgradedFiles,
       "starNeSwUpgradeCurrentFile": starNeSwUpgradeCurrentFile,
       "starNeSwUpgradeStatus": starNeSwUpgradeStatus,
       "starSysSlotRedundencyInfo": starSysSlotRedundencyInfo,
       "starActiveSPUSlotNo": starActiveSPUSlotNo,
       "starStandbySPUSlotNo": starStandbySPUSlotNo,
       "starActiveSCUSlotNo": starActiveSCUSlotNo,
       "starStandbySCUSlotNo": starStandbySCUSlotNo,
       "starActiveSSUSlotNo": starActiveSSUSlotNo,
       "starStandbySSUSlotNo": starStandbySSUSlotNo,
       "starConfigManager": starConfigManager,
       "starCfAllChanged": starCfAllChanged,
       "starCfFileChanged": starCfFileChanged,
       "starCfBootFileName": starCfBootFileName,
       "starCfShelf": starCfShelf,
       "starCfMaxSlots": starCfMaxSlots,
       "starCfBootSwitch": starCfBootSwitch,
       "starCfInvalidateFlash": starCfInvalidateFlash,
       "starCfActivePSUNo": starCfActivePSUNo,
       "starCfPSUOperStatus": starCfPSUOperStatus,
       "starCfFanStatus": starCfFanStatus,
       "starCfAluLedStatus": starCfAluLedStatus,
       "starCfAluCharacterDisplay": starCfAluCharacterDisplay,
       "starCfAluBrightness": starCfAluBrightness,
       "starCfSlotInstalled": starCfSlotInstalled,
       "starAccountManager": starAccountManager,
       "starAmCDRFileGetCompleted": starAmCDRFileGetCompleted,
       "starAmCDRThresholdCount": starAmCDRThresholdCount,
       "starAmCDRThresholdTime": starAmCDRThresholdTime,
       "starAmCDRFileGetRequest": starAmCDRFileGetRequest,
       "starAmCDRFileCount": starAmCDRFileCount,
       "starAmCDRMaxCount": starAmCDRMaxCount,
       "starAmCacheTimer": starAmCacheTimer,
       "starAmCacheCounter": starAmCacheCounter,
       "starFaultManager": starFaultManager,
       "starFmSendTrapThreshold": starFmSendTrapThreshold,
       "starFmLogNotify": starFmLogNotify,
       "starFmLogFileInterval": starFmLogFileInterval,
       "starSysSlotStatusTable": starSysSlotStatusTable,
       "starSysSlotStatusEntry": starSysSlotStatusEntry,
       "starSSDIndex": starSSDIndex,
       "starSSDBdEquipStatus": starSSDBdEquipStatus,
       "starSSDModuleType": starSSDModuleType,
       "starSSDInterfaceType": starSSDInterfaceType,
       "starSSDOperStatus": starSSDOperStatus,
       "starSSDCpuFailStatus": starSSDCpuFailStatus,
       "starSSDPwrFailStatus": starSSDPwrFailStatus,
       "starSSDRealStatus": starSSDRealStatus,
       "starSiuRednConfigStatus": starSiuRednConfigStatus,
       "starSiuRednOperStatus": starSiuRednOperStatus,
       "starSiuRednSwitchOver": starSiuRednSwitchOver,
       "starFaultControlTable": starFaultControlTable,
       "starFaultControlEntry": starFaultControlEntry,
       "starFaultSlotId": starFaultSlotId,
       "starFaultGroupId": starFaultGroupId,
       "starFaultSubId": starFaultSubId,
       "starSeverity": starSeverity,
       "starFaultThresholdType": starFaultThresholdType,
       "starFaultHappenValue": starFaultHappenValue,
       "starFaultClearValue": starFaultClearValue,
       "starTrapControlTable": starTrapControlTable,
       "starTrapControlEntry": starTrapControlEntry,
       "starTrapGroupId": starTrapGroupId,
       "starTrapSubId": starTrapSubId,
       "starTrapSendCondition": starTrapSendCondition,
       "starMipRouteTable": starMipRouteTable,
       "starMipRouteEntry": starMipRouteEntry,
       "starMipDestNeId": starMipDestNeId,
       "starMipSourceSlot": starMipSourceSlot,
       "starMipSourcePort": starMipSourcePort,
       "starSvcAts": starSvcAts,
       "starSvcAtsValue": starSvcAtsValue,
       "starSvcAtsRxReqCount": starSvcAtsRxReqCount,
       "starSvcAtsRxValidResponseCount": starSvcAtsRxValidResponseCount,
       "starSvcAtsRxInvalidResponseCount": starSvcAtsRxInvalidResponseCount,
       "starSvcAtsNotCacheCount": starSvcAtsNotCacheCount,
       "starSvcAtsCachedReqCount": starSvcAtsCachedReqCount,
       "starSvcAtsTCPConnTrialCount": starSvcAtsTCPConnTrialCount,
       "starSvcAtsStatusTable": starSvcAtsStatusTable,
       "starSvcAtsStatusEntry": starSvcAtsStatusEntry,
       "starSvcAtsIndex": starSvcAtsIndex,
       "starSvcAtsServerStatus": starSvcAtsServerStatus,
       "starPerformanceManager": starPerformanceManager,
       "starPmReportInterval": starPmReportInterval,
       "starPmCollectInterval": starPmCollectInterval,
       "starPmStatsChangeTable": starPmStatsChangeTable,
       "starPmStatsChangeEntry": starPmStatsChangeEntry,
       "starPmIndex": starPmIndex,
       "starPmPortStatusChange": starPmPortStatusChange,
       "starPmConnStatusChange": starPmConnStatusChange,
       "starSlot": starSlot,
       "starSlotTable": starSlotTable,
       "starSlotEntry": starSlotEntry,
       "starSlotIndex": starSlotIndex,
       "starSlotModuleType": starSlotModuleType,
       "starSlotInterfaceType": starSlotInterfaceType,
       "starSlotModuleDescr": starSlotModuleDescr,
       "starSlotMaxPortNo": starSlotMaxPortNo,
       "starSlotModuleCpuUtilization": starSlotModuleCpuUtilization,
       "starSlotModuleHwVersion": starSlotModuleHwVersion,
       "starSlotModuleSwVersion": starSlotModuleSwVersion,
       "starSlotLastInstalledTime": starSlotLastInstalledTime,
       "starSlotSSBStatus": starSlotSSBStatus,
       "starSlotCellPathStatus": starSlotCellPathStatus,
       "starSlotLineClkSource": starSlotLineClkSource,
       "starSlotVpiVciRange": starSlotVpiVciRange,
       "starSlotSSUInfo": starSlotSSUInfo,
       "starSSULoadInfoTbl": starSSULoadInfoTbl,
       "starSSULoadInfoEntry": starSSULoadInfoEntry,
       "starSSULoadInfoSlotId": starSSULoadInfoSlotId,
       "starSSULoadTotalConnections": starSSULoadTotalConnections,
       "starSSULoadNumMcConnections": starSSULoadNumMcConnections,
       "starSSULoadHighMarkVbrIn": starSSULoadHighMarkVbrIn,
       "starSSULoadTotalVbrIn": starSSULoadTotalVbrIn,
       "starSSULoadLowMarkVbrIn": starSSULoadLowMarkVbrIn,
       "starSSULoadHighMarkVbrOut": starSSULoadHighMarkVbrOut,
       "starSSULoadTotalVbrOut": starSSULoadTotalVbrOut,
       "starSSULoadLowMarkVbrOut": starSSULoadLowMarkVbrOut,
       "starSSULoadHighMarkFbrIn": starSSULoadHighMarkFbrIn,
       "starSSULoadTotalFbrIn": starSSULoadTotalFbrIn,
       "starSSULoadLowMarkFbrIn": starSSULoadLowMarkFbrIn,
       "starSSULoadHighMarkFbrOut": starSSULoadHighMarkFbrOut,
       "starSSULoadTotalFbrOut": starSSULoadTotalFbrOut,
       "starSSULoadLowMarkFbrOut": starSSULoadLowMarkFbrOut,
       "starSSUSiuLoadInfoTbl": starSSUSiuLoadInfoTbl,
       "starSSUSiuLoadInfoEntry": starSSUSiuLoadInfoEntry,
       "starSlotIdSiuLoadInfo": starSlotIdSiuLoadInfo,
       "starSiuIdSiuLoadInfo": starSiuIdSiuLoadInfo,
       "starSSUSiuTotalConnections": starSSUSiuTotalConnections,
       "starSSUSiuNumMcConnections": starSSUSiuNumMcConnections,
       "starSSUSiuTotalVbrIn": starSSUSiuTotalVbrIn,
       "starSSUSiuTotalVbrOut": starSSUSiuTotalVbrOut,
       "starSSUSiuTotalFbrIn": starSSUSiuTotalFbrIn,
       "starSSUSiuTotalFbrOut": starSSUSiuTotalFbrOut,
       "starSSUSiuPortLoadInfoTbl": starSSUSiuPortLoadInfoTbl,
       "starSSUSiuPortLoadInfoEntry": starSSUSiuPortLoadInfoEntry,
       "starSlotIdPortLoadInfo": starSlotIdPortLoadInfo,
       "starSiuIdPortLoadInfo": starSiuIdPortLoadInfo,
       "starSiuPortIdPortLoadInfo": starSiuPortIdPortLoadInfo,
       "starSSUSiuPortTotalConnections": starSSUSiuPortTotalConnections,
       "starSSUSiuPortNumMcConnections": starSSUSiuPortNumMcConnections,
       "starSSUSiuPortTotalVbrIn": starSSUSiuPortTotalVbrIn,
       "starSSUSiuPortTotalVbrOut": starSSUSiuPortTotalVbrOut,
       "starSSUSiuPortTotalFbrIn": starSSUSiuPortTotalFbrIn,
       "starSSUSiuPortTotalFbrOut": starSSUSiuPortTotalFbrOut,
       "starSSUConfigInfoTbl": starSSUConfigInfoTbl,
       "starSSUConfigInfoEntry": starSSUConfigInfoEntry,
       "starSSUConfigInfoSlotId": starSSUConfigInfoSlotId,
       "starSSUSwitchLinkMaxCapacity": starSSUSwitchLinkMaxCapacity,
       "starSSUSwitchLinkMaxVbr": starSSUSwitchLinkMaxVbr,
       "starSSUPercentVbrToLoad": starSSUPercentVbrToLoad,
       "starSSUSiuInvalidationTimeout": starSSUSiuInvalidationTimeout,
       "starSSUMulticastInfoTbl": starSSUMulticastInfoTbl,
       "starSSUMulticastInfoEntry": starSSUMulticastInfoEntry,
       "starSSUMulticastSlotId": starSSUMulticastSlotId,
       "starSSUMulticastGroup": starSSUMulticastGroup,
       "starSSUNumberMcLeaves": starSSUNumberMcLeaves,
       "starSSUMcSourceSiu": starSSUMcSourceSiu,
       "starSSUMcSourcePort": starSSUMcSourcePort,
       "starSSUMcInputFbr": starSSUMcInputFbr,
       "starSSUMcInputVbr": starSSUMcInputVbr,
       "starSSUMcOutputFbr": starSSUMcOutputFbr,
       "starSSUMcOutputVbr": starSSUMcOutputVbr,
       "starSSULinkConfigInfoTbl": starSSULinkConfigInfoTbl,
       "starSSULinkConfigInfoEntry": starSSULinkConfigInfoEntry,
       "starSSULinkConfigSlotId": starSSULinkConfigSlotId,
       "starSSULinkConfigSwitchLevel": starSSULinkConfigSwitchLevel,
       "starSSUConfigSwitchLink": starSSUConfigSwitchLink,
       "starSSULinkMaxCapacity": starSSULinkMaxCapacity,
       "starSSULinkMaxVbr": starSSULinkMaxVbr,
       "starSSUPmThresholdInfoTbl": starSSUPmThresholdInfoTbl,
       "starSSUPmThresholdInfoEntry": starSSUPmThresholdInfoEntry,
       "starSSUPmThresholdSlotId": starSSUPmThresholdSlotId,
       "starSSUSwitchMcGroupThreshold": starSSUSwitchMcGroupThreshold,
       "starSSUSwitchMcBitsPerMcgThreshold": starSSUSwitchMcBitsPerMcgThreshold,
       "starSSUSwitchTotalMcBitsThreshold": starSSUSwitchTotalMcBitsThreshold,
       "starSSUCrsrReqFailedThreshold": starSSUCrsrReqFailedThreshold,
       "starSSUCrsrReqNumThreshold": starSSUCrsrReqNumThreshold,
       "starSSUCrsrReqFailedMcgExceededThreshold": starSSUCrsrReqFailedMcgExceededThreshold,
       "starSSUCrsrReconcileFailThreshold": starSSUCrsrReconcileFailThreshold,
       "starSSUSiuLoadCapacityThreshold": starSSUSiuLoadCapacityThreshold,
       "starSysClockInfo": starSysClockInfo,
       "starSysClockTbl": starSysClockTbl,
       "starSysClockInfoEntry": starSysClockInfoEntry,
       "starScuInfoSlotId": starScuInfoSlotId,
       "starClkSource": starClkSource,
       "starClkPrevSource": starClkPrevSource,
       "starClkSourceLine": starClkSourceLine,
       "starClkPrevSourceLine": starClkPrevSourceLine,
       "starClkStatus": starClkStatus,
       "starClkPLLMode": starClkPLLMode,
       "starClkMasterStatus": starClkMasterStatus,
       "starClkPriority": starClkPriority,
       "starClkCurStatusLineTbl": starClkCurStatusLineTbl,
       "starClkCurStatusLineEntry": starClkCurStatusLineEntry,
       "starClkStatusSlotId": starClkStatusSlotId,
       "starClkCurStatusSiu1": starClkCurStatusSiu1,
       "starClkCurStatusSiu2": starClkCurStatusSiu2,
       "starClkCurStatusSiu3": starClkCurStatusSiu3,
       "starClkCurStatusSiu4": starClkCurStatusSiu4,
       "starClkCurStatusSiu5": starClkCurStatusSiu5,
       "starClkCurStatusSiu6": starClkCurStatusSiu6,
       "starClkCurStatusSiu7": starClkCurStatusSiu7,
       "starClkCurStatusSiu8": starClkCurStatusSiu8,
       "starClkCurStatusSiu9": starClkCurStatusSiu9,
       "starClkDistribStatusTbl": starClkDistribStatusTbl,
       "starClkDistribStatusEntry": starClkDistribStatusEntry,
       "starClkDistribSlotId": starClkDistribSlotId,
       "starClkDistribStatusSiu1": starClkDistribStatusSiu1,
       "starClkDistribStatusSiu2": starClkDistribStatusSiu2,
       "starClkDistribStatusSiu3": starClkDistribStatusSiu3,
       "starClkDistribStatusSiu4": starClkDistribStatusSiu4,
       "starClkDistribStatusSiu5": starClkDistribStatusSiu5,
       "starClkDistribStatusSiu6": starClkDistribStatusSiu6,
       "starClkDistribStatusSiu7": starClkDistribStatusSiu7,
       "starClkDistribStatusSiu8": starClkDistribStatusSiu8,
       "starClkDistribStatusSiu9": starClkDistribStatusSiu9,
       "starSwitch88Info": starSwitch88Info,
       "starSwitchInfoTbl": starSwitchInfoTbl,
       "starSwitchInfoEntry": starSwitchInfoEntry,
       "starSwitchInfoSlotId": starSwitchInfoSlotId,
       "starSwitchFabricRow": starSwitchFabricRow,
       "starSwitchFabricColumn": starSwitchFabricColumn,
       "starSwitchCurrentState": starSwitchCurrentState,
       "starSwitchChipVersion": starSwitchChipVersion,
       "starSwitchFabricLevel": starSwitchFabricLevel,
       "starSwitchBckPressureDly": starSwitchBckPressureDly,
       "starSwitchAggrIp": starSwitchAggrIp,
       "starSwitchAggrOp": starSwitchAggrOp,
       "starSwitchStrictPriority": starSwitchStrictPriority,
       "starSwitchInMarkedCellCnt": starSwitchInMarkedCellCnt,
       "starSwitchOutMarkedCellCnt": starSwitchOutMarkedCellCnt,
       "starSwitchRatioAOrder1": starSwitchRatioAOrder1,
       "starSwitchRatioAOrder2": starSwitchRatioAOrder2,
       "starSwitchRatioBOrder1": starSwitchRatioBOrder1,
       "starSwitchRatioBOrder2": starSwitchRatioBOrder2,
       "starSwitchMulticastInfoTbl": starSwitchMulticastInfoTbl,
       "starSwitchMulticastInfoEntry": starSwitchMulticastInfoEntry,
       "starSlotIdSwitchMcInfo": starSlotIdSwitchMcInfo,
       "starMcSwitchFabricRow": starMcSwitchFabricRow,
       "starMcSwitchFabricColumn": starMcSwitchFabricColumn,
       "starSwitchMulticastNo": starSwitchMulticastNo,
       "starSwitchMulticastPorts": starSwitchMulticastPorts,
       "starSwitchLinkLoadTbl": starSwitchLinkLoadTbl,
       "starSwitchLinkLoadEntry": starSwitchLinkLoadEntry,
       "starSlotIdSwitchLoadInfo": starSlotIdSwitchLoadInfo,
       "starLinkLoadSwitchFabricRow": starLinkLoadSwitchFabricRow,
       "starLinkLoadSwitchFabricColumn": starLinkLoadSwitchFabricColumn,
       "starSwitchLinkId": starSwitchLinkId,
       "starSwitchLinkVbrIn": starSwitchLinkVbrIn,
       "starSwitchLinkVbrOut": starSwitchLinkVbrOut,
       "starSwitchLinkFbrIn": starSwitchLinkFbrIn,
       "starSwitchLinkFbrOut": starSwitchLinkFbrOut,
       "starCellMuxInfoTbl": starCellMuxInfoTbl,
       "starCellMuxInfoEntry": starCellMuxInfoEntry,
       "starSlotIdCellMuxInfo": starSlotIdCellMuxInfo,
       "starCellMuxChipId": starCellMuxChipId,
       "starCellMuxCurrentState": starCellMuxCurrentState,
       "starCellMuxChipVersion": starCellMuxChipVersion,
       "starCellMuxWatchDogTimer": starCellMuxWatchDogTimer,
       "starCellMuxUsedHighBufCnt": starCellMuxUsedHighBufCnt,
       "starCellMuxUsedMedBufCnt": starCellMuxUsedMedBufCnt,
       "starCellMuxUsedLowBufCnt": starCellMuxUsedLowBufCnt,
       "starCellMuxFreeHighBufCnt": starCellMuxFreeHighBufCnt,
       "starCellMuxFreeMedBufCnt": starCellMuxFreeMedBufCnt,
       "starCellMuxFreeLowBufCnt": starCellMuxFreeLowBufCnt,
       "starSlotRoute88Table": starSlotRoute88Table,
       "starSlotRoute88Entry": starSlotRoute88Entry,
       "starSlotRoute88Index": starSlotRoute88Index,
       "starSlotRoute88Revision": starSlotRoute88Revision,
       "starSlotRoute88TxParityFailCount": starSlotRoute88TxParityFailCount,
       "starSlotRoute88BPIgnoredCount": starSlotRoute88BPIgnoredCount,
       "starSlotRoute88BPLiveFailCount": starSlotRoute88BPLiveFailCount,
       "starSlotRoute88WDFailCount": starSlotRoute88WDFailCount,
       "starSlotRoute88TxMarkedCells": starSlotRoute88TxMarkedCells,
       "starSlotRoute88RxMarkedCells": starSlotRoute88RxMarkedCells,
       "starSlotAal1SarTable": starSlotAal1SarTable,
       "starAal1SarInfoEntry": starAal1SarInfoEntry,
       "starAal1SarSlotId": starAal1SarSlotId,
       "starAal1SarPortId": starAal1SarPortId,
       "starAal1SarChannelId": starAal1SarChannelId,
       "starAal1SarInvalidSnCnt": starAal1SarInvalidSnCnt,
       "starAal1SarIncorrectSnpCnt": starAal1SarIncorrectSnpCnt,
       "starAal1SarRxOAMCellCnt": starAal1SarRxOAMCellCnt,
       "starAal1SarRxCellLossStatus": starAal1SarRxCellLossStatus,
       "starAal1SarLostCellCnt": starAal1SarLostCellCnt,
       "starAal1SarTxCellCnt": starAal1SarTxCellCnt,
       "starAal1SarRxCellCnt": starAal1SarRxCellCnt,
       "starAal1SarRxUnderrun": starAal1SarRxUnderrun,
       "starAal1SarRxOverrun": starAal1SarRxOverrun,
       "starAal1SarPtrMismatch": starAal1SarPtrMismatch,
       "starSlotLsgnStatusTable": starSlotLsgnStatusTable,
       "starLsgnEntry": starLsgnEntry,
       "starLsgnDownCt": starLsgnDownCt,
       "starLsgnUpCt": starLsgnUpCt,
       "starLsgnTrafficLoadChangedCt": starLsgnTrafficLoadChangedCt,
       "starLsgnPeriodMsgCt": starLsgnPeriodMsgCt,
       "starLsgnLinkOperStatus": starLsgnLinkOperStatus,
       "starSlotRlspStatusTable": starSlotRlspStatusTable,
       "starRlspEntry": starRlspEntry,
       "starRlspForwardedCt": starRlspForwardedCt,
       "starRlspDiscardedCt": starRlspDiscardedCt,
       "starRlspInvalidCt": starRlspInvalidCt,
       "starRlspMismatchCt": starRlspMismatchCt,
       "starRlspNoRoutesCt": starRlspNoRoutesCt,
       "starSlotBbcpStatusTable": starSlotBbcpStatusTable,
       "starBbcpEntry": starBbcpEntry,
       "starBbcpPtoPInConnections": starBbcpPtoPInConnections,
       "starBbcpPtoPOutConnections": starBbcpPtoPOutConnections,
       "starBbcpPtoMInConnections": starBbcpPtoMInConnections,
       "starBbcpPtoMOutConnections": starBbcpPtoMOutConnections,
       "starBbcpInConnectionLinkFailCt": starBbcpInConnectionLinkFailCt,
       "starBbcpInConnectionVcciFailCt": starBbcpInConnectionVcciFailCt,
       "starBbcpInConnectionNoSwitchCapacityCt": starBbcpInConnectionNoSwitchCapacityCt,
       "starBbcpInConnectionNoBBCapacityCt": starBbcpInConnectionNoBBCapacityCt,
       "starBbcpInConnectionTimeoutCt": starBbcpInConnectionTimeoutCt,
       "starBbcpInConnectionChipErrorCt": starBbcpInConnectionChipErrorCt,
       "starBbcpInConnectionPreemptFailCt": starBbcpInConnectionPreemptFailCt,
       "starBbcpInConnectionModuleFailCt": starBbcpInConnectionModuleFailCt,
       "starBbcpInConnectionVcciCollisionFailCt": starBbcpInConnectionVcciCollisionFailCt,
       "starBbcpOutConnectionLinkFailCt": starBbcpOutConnectionLinkFailCt,
       "starBbcpOutConnectionVcciInvalidCt": starBbcpOutConnectionVcciInvalidCt,
       "starBbcpOutConnectionNoSwitchCapacityCt": starBbcpOutConnectionNoSwitchCapacityCt,
       "starBbcpOutConnectionNoBBCapacityCt": starBbcpOutConnectionNoBBCapacityCt,
       "starBbcpOutConnectionTimeoutCt": starBbcpOutConnectionTimeoutCt,
       "starBbcpOutConnectionChipErrorCt": starBbcpOutConnectionChipErrorCt,
       "starBbcpOutConnectionPreemptFailCt": starBbcpOutConnectionPreemptFailCt,
       "starBbcpOutConnectionModuleFailCt": starBbcpOutConnectionModuleFailCt,
       "starBbcpOutConnectionVcciCollisionFailCt": starBbcpOutConnectionVcciCollisionFailCt,
       "starBbcpInConnectionClearLinkFailCt": starBbcpInConnectionClearLinkFailCt,
       "starBbcpInConnectionClearPreemptionCt": starBbcpInConnectionClearPreemptionCt,
       "starBbcpInConnectionClearModuleFailCt": starBbcpInConnectionClearModuleFailCt,
       "starBbcpInConnectionClearNormalCt": starBbcpInConnectionClearNormalCt,
       "starBbcpOutConnectionClearLinkFailCt": starBbcpOutConnectionClearLinkFailCt,
       "starBbcpOutConnectionClearPreemptionCt": starBbcpOutConnectionClearPreemptionCt,
       "starBbcpOutConnectionClearModuleFailCt": starBbcpOutConnectionClearModuleFailCt,
       "starBbcpOutConnectionClearNormalCt": starBbcpOutConnectionClearNormalCt,
       "starBbcpInvalidMsgCt": starBbcpInvalidMsgCt,
       "starBbcpTimerExpiredCt": starBbcpTimerExpiredCt,
       "starBbcpInvalidEventCt": starBbcpInvalidEventCt,
       "starBbcpAvailableFixedCapacity": starBbcpAvailableFixedCapacity,
       "starBbcpAvailableVariableCapacity": starBbcpAvailableVariableCapacity,
       "starSlotBbcpXConnectTable": starSlotBbcpXConnectTable,
       "starBbcpXConnectEntry": starBbcpXConnectEntry,
       "starBbcpSlotIndex": starBbcpSlotIndex,
       "starBbcpPortIndex": starBbcpPortIndex,
       "starBbcpGCIDNeId": starBbcpGCIDNeId,
       "starBbcpGCIDSlotId": starBbcpGCIDSlotId,
       "starBbcpGCIDPortId": starBbcpGCIDPortId,
       "starBbcpGCIDIfType": starBbcpGCIDIfType,
       "starBbcpGCIDConnId": starBbcpGCIDConnId,
       "starBbcpGCIDLeafId": starBbcpGCIDLeafId,
       "starBbcpXConnOperStatus": starBbcpXConnOperStatus,
       "starBbcpXConnAdjacentSlotId": starBbcpXConnAdjacentSlotId,
       "starBbcpXConnAdjacentPortId": starBbcpXConnAdjacentPortId,
       "starBbcpXConnAdjacentVpi": starBbcpXConnAdjacentVpi,
       "starBbcpXConnAdjacentVci": starBbcpXConnAdjacentVci,
       "starPvcmStatusTable": starPvcmStatusTable,
       "starPvcmEntry": starPvcmEntry,
       "starPvcmPtoPOrgConnectionNumber": starPvcmPtoPOrgConnectionNumber,
       "starPvcmPtoPTermConnectionNumber": starPvcmPtoPTermConnectionNumber,
       "starPvcmPtoMOrgConnectionNumber": starPvcmPtoMOrgConnectionNumber,
       "starPvcmPtoMTermConnectionNumber": starPvcmPtoMTermConnectionNumber,
       "starPvcmOutOfServiceConnectionNumber": starPvcmOutOfServiceConnectionNumber,
       "starPvcmOptimizedConnectionNumber": starPvcmOptimizedConnectionNumber,
       "starPvcmRouteFailCt": starPvcmRouteFailCt,
       "starPvcmConnectReqFailCt": starPvcmConnectReqFailCt,
       "starPvcmOrgConnectedFailCt": starPvcmOrgConnectedFailCt,
       "starPvcmTermConnectedFailCt": starPvcmTermConnectedFailCt,
       "starPvcmActiveConnectionNumber": starPvcmActiveConnectionNumber,
       "starPvcmDeletedConnectionNumber": starPvcmDeletedConnectionNumber,
       "starPvcmAddedConnectionNumber": starPvcmAddedConnectionNumber,
       "starPvcmFailedConnectionNumber": starPvcmFailedConnectionNumber,
       "starPvcmChangedConnectionNumber": starPvcmChangedConnectionNumber,
       "starPvcmOrgHoldingConnectionNumber": starPvcmOrgHoldingConnectionNumber,
       "starPvcmTermHoldingConnectionNumber": starPvcmTermHoldingConnectionNumber,
       "starPvcmInvalidMsgNumber": starPvcmInvalidMsgNumber,
       "starPvcmTimerExpiredCnt": starPvcmTimerExpiredCnt,
       "starPvcConnectionTable": starPvcConnectionTable,
       "starPvcConnectionEntry": starPvcConnectionEntry,
       "starPvcSrcSlotId": starPvcSrcSlotId,
       "starPvcSrcPortId": starPvcSrcPortId,
       "starPvcSrcIfType": starPvcSrcIfType,
       "starPvcSrcVpi": starPvcSrcVpi,
       "starPvcSrcVci": starPvcSrcVci,
       "starPvcSrcLeaf": starPvcSrcLeaf,
       "starPvcSrcDlci": starPvcSrcDlci,
       "starPvcSrcTimeslot": starPvcSrcTimeslot,
       "starPvcDestNodeId": starPvcDestNodeId,
       "starPvcDestSlotId": starPvcDestSlotId,
       "starPvcDestPortId": starPvcDestPortId,
       "starPvcDestIfType": starPvcDestIfType,
       "starPvcDestVpi": starPvcDestVpi,
       "starPvcDestVci": starPvcDestVci,
       "starPvcDestDlci": starPvcDestDlci,
       "starPvcDestTimeslot": starPvcDestTimeslot,
       "starPvcConnectionOperStatus": starPvcConnectionOperStatus,
       "starPvcConnectionType": starPvcConnectionType,
       "starPvcConnectionCOS": starPvcConnectionCOS,
       "starPvcConnectionStatusLastChangedDate": starPvcConnectionStatusLastChangedDate,
       "starPvcConnectionStatusLastChangedTime": starPvcConnectionStatusLastChangedTime,
       "starPvcConnectionCauseValue": starPvcConnectionCauseValue,
       "starFiuModuleInfo": starFiuModuleInfo,
       "starFrlExtnModuleInfo": starFrlExtnModuleInfo,
       "frlPortInfoTbl": frlPortInfoTbl,
       "frlPortInfoEntry": frlPortInfoEntry,
       "frlPortInfoSlotId": frlPortInfoSlotId,
       "frlPortInfoPortId": frlPortInfoPortId,
       "frlPortSigMode": frlPortSigMode,
       "frlPortActiveDlci": frlPortActiveDlci,
       "frlPvcEndptInfoTbl": frlPvcEndptInfoTbl,
       "frlPvcEndptInfoEntry": frlPvcEndptInfoEntry,
       "frlPvcEndptInfoSlotId": frlPvcEndptInfoSlotId,
       "frlPvcEndptInfoPortId": frlPvcEndptInfoPortId,
       "frlPvcEndptInfoDlci": frlPvcEndptInfoDlci,
       "frPvcEndptInfoTimeStamp": frPvcEndptInfoTimeStamp,
       "frPvcMarkedDe": frPvcMarkedDe,
       "frPvcEndptOperStatus": frPvcEndptOperStatus,
       "frPvcEndptNoRecvFECN": frPvcEndptNoRecvFECN,
       "frPvcEndptNoTxFECN": frPvcEndptNoTxFECN,
       "frPvcEndptNoRecvBECN": frPvcEndptNoRecvBECN,
       "frPvcEndptNoTxBECN": frPvcEndptNoTxBECN,
       "frPvcEndptNoTxDE": frPvcEndptNoTxDE,
       "frPvcEndptNoDiscardWithDE": frPvcEndptNoDiscardWithDE,
       "frPvcEndptNoDiscardWoutDE": frPvcEndptNoDiscardWoutDE,
       "frPvcEndptInDEFrames": frPvcEndptInDEFrames,
       "starfrPVCEndptPerfTbl": starfrPVCEndptPerfTbl,
       "starfrPVCEndptPerfTblEntry": starfrPVCEndptPerfTblEntry,
       "starfrPVCEndptPerfSlotId": starfrPVCEndptPerfSlotId,
       "starfrPVCEndptPerfPortId": starfrPVCEndptPerfPortId,
       "starfrPVCEndptPerfDLCIIndex": starfrPVCEndptPerfDLCIIndex,
       "starfrPVCEndptPerfTmStp": starfrPVCEndptPerfTmStp,
       "starfrPVCEndptPerfRxPktSz": starfrPVCEndptPerfRxPktSz,
       "starfrPVCEndptPerfTxpktSz": starfrPVCEndptPerfTxpktSz,
       "starfrPVCEndptPerfRxFrPs": starfrPVCEndptPerfRxFrPs,
       "starfrPVCEndptPerfTxFrPs": starfrPVCEndptPerfTxFrPs,
       "starfrPVCEndptPerfRxKbps": starfrPVCEndptPerfRxKbps,
       "starfrPVCEndptPerfTxKbps": starfrPVCEndptPerfTxKbps,
       "starfrPVCEndptPerfRxUt": starfrPVCEndptPerfRxUt,
       "starfrPVCEndptPerfTxUt": starfrPVCEndptPerfTxUt,
       "starFiuSscsInfo": starFiuSscsInfo,
       "starFiuSscsIfInfoTbl": starFiuSscsIfInfoTbl,
       "starFiuSscsIfInfoEntry": starFiuSscsIfInfoEntry,
       "starFiuIfInfoSlotId": starFiuIfInfoSlotId,
       "starFiuIfInfoPortId": starFiuIfInfoPortId,
       "starFiuFrcsIfAdminStatus": starFiuFrcsIfAdminStatus,
       "starFiuFrcsIfOperStatus": starFiuFrcsIfOperStatus,
       "starFiuFrcsIfLastChange": starFiuFrcsIfLastChange,
       "starFiuFrcsIfInOctets": starFiuFrcsIfInOctets,
       "starFiuFrcsIfInUcastPkts": starFiuFrcsIfInUcastPkts,
       "starFiuFrcsIfInDiscards": starFiuFrcsIfInDiscards,
       "starFiuFrcsIfInErrors": starFiuFrcsIfInErrors,
       "starFiuFrcsIfOutOctets": starFiuFrcsIfOutOctets,
       "starFiuFrcsIfOutUcastPkts": starFiuFrcsIfOutUcastPkts,
       "starFiuFrcsIfOutDiscards": starFiuFrcsIfOutDiscards,
       "starFiuFrcsIfOutErrors": starFiuFrcsIfOutErrors,
       "starFiuSscsPvcInfoTbl": starFiuSscsPvcInfoTbl,
       "starFiuSscsPvcInfoEntry": starFiuSscsPvcInfoEntry,
       "starFiuPvcInfoSlotId": starFiuPvcInfoSlotId,
       "starFiuPvcInfoPortId": starFiuPvcInfoPortId,
       "starFiuPvcInfoDlci": starFiuPvcInfoDlci,
       "starFiuFrcsPvcEndptInFrames": starFiuFrcsPvcEndptInFrames,
       "starFiuFrcsPvcEndptOutFrames": starFiuFrcsPvcEndptOutFrames,
       "starFiuFrcsPvcEndptInOctets": starFiuFrcsPvcEndptInOctets,
       "starFiuFrcsPvcEndptOutOctets": starFiuFrcsPvcEndptOutOctets,
       "starFiuFrcsPvcConnectAdminStatus": starFiuFrcsPvcConnectAdminStatus,
       "starFiuFrcsPvcEndptOperStatus": starFiuFrcsPvcEndptOperStatus,
       "starFiuFrcsPvcEndptLastChange": starFiuFrcsPvcEndptLastChange,
       "starFiuFrcsPvcTxVp": starFiuFrcsPvcTxVp,
       "starFiuFrcsPvcTxVc": starFiuFrcsPvcTxVc,
       "starFiuFrcsPvcRxVp": starFiuFrcsPvcRxVp,
       "starFiuFrcsPvcRxVc": starFiuFrcsPvcRxVc,
       "starFiuFrcsPvcEndptOutOamCells": starFiuFrcsPvcEndptOutOamCells,
       "starFiuFrcsPvcEndptInOamCells": starFiuFrcsPvcEndptInOamCells,
       "starFiuFrcsPvcEndptOutRawCells": starFiuFrcsPvcEndptOutRawCells,
       "starFiuFrcsPvcEndptInRawCells": starFiuFrcsPvcEndptInRawCells,
       "starFiuSscsIfPerfTbl": starFiuSscsIfPerfTbl,
       "starFiuSscsIfPerfTblEntry": starFiuSscsIfPerfTblEntry,
       "starFiuSscsIfPerfSlotId": starFiuSscsIfPerfSlotId,
       "starFiuSscsIfPerfPortId": starFiuSscsIfPerfPortId,
       "starFiuSscsIfPerfTmStp": starFiuSscsIfPerfTmStp,
       "starFiuSscsIfPerfRxPktSz": starFiuSscsIfPerfRxPktSz,
       "starFiuSscsIfPerfTxpktSz": starFiuSscsIfPerfTxpktSz,
       "starFiuSscsIfPerfRxFrPs": starFiuSscsIfPerfRxFrPs,
       "starFiuSscsIfPerfTxFrPs": starFiuSscsIfPerfTxFrPs,
       "starFiuSscsIfPerfRxKbps": starFiuSscsIfPerfRxKbps,
       "starFiuSscsIfPerfTxKbps": starFiuSscsIfPerfTxKbps,
       "starFiuSscsIfPerfRxUt": starFiuSscsIfPerfRxUt,
       "starFiuSscsIfPerfTxUt": starFiuSscsIfPerfTxUt,
       "starFrMgmtStatisticInfoTbl": starFrMgmtStatisticInfoTbl,
       "starFrMgmtStatisticInfoEntry": starFrMgmtStatisticInfoEntry,
       "starFrMgmtStatisticSlotId": starFrMgmtStatisticSlotId,
       "starFrMgmtStatisticPortId": starFrMgmtStatisticPortId,
       "starFrlMgtInKeepalive": starFrlMgtInKeepalive,
       "starFrlMgtOutKeepalive": starFrlMgtOutKeepalive,
       "starFrlMgtInStatus": starFrlMgtInStatus,
       "starFrlMgtOutStatus": starFrlMgtOutStatus,
       "starFrlMgtInStatusReply": starFrlMgtInStatusReply,
       "starFrlMgtOutStatusReply": starFrlMgtOutStatusReply,
       "starFrlMgtInAsyncUpdates": starFrlMgtInAsyncUpdates,
       "starFrlMgtOutAsyncUpdates": starFrlMgtOutAsyncUpdates,
       "starFrlMgtNoMismatchSeqNo": starFrlMgtNoMismatchSeqNo,
       "starFrlMgtNoT392TimeOut": starFrlMgtNoT392TimeOut,
       "starFrlMgtNoRecvErDlci": starFrlMgtNoRecvErDlci,
       "starFrlMgtLastRecvErDlci": starFrlMgtLastRecvErDlci,
       "starFiuPmInfo": starFiuPmInfo,
       "starFrHdlcPmInfoTbl": starFrHdlcPmInfoTbl,
       "starFrHdlcPmInfoEntry": starFrHdlcPmInfoEntry,
       "starFrHdlcPmSlotId": starFrHdlcPmSlotId,
       "starFrHdlcPmPortId": starFrHdlcPmPortId,
       "starFrHdlcRxOverrunCount": starFrHdlcRxOverrunCount,
       "starFrHdlcTxUnderrunCount": starFrHdlcTxUnderrunCount,
       "starFrCongStatInfoTbl": starFrCongStatInfoTbl,
       "starFrCongStatInfoEntry": starFrCongStatInfoEntry,
       "starFrCongStatSlotId": starFrCongStatSlotId,
       "starFrCongStatPortId": starFrCongStatPortId,
       "starFrCongStatTimeStamp": starFrCongStatTimeStamp,
       "starFrCongNoRecvFECN": starFrCongNoRecvFECN,
       "starFrCongNoTxFECN": starFrCongNoTxFECN,
       "starFrCongNoRecvBECN": starFrCongNoRecvBECN,
       "starFrCongNoTxBECN": starFrCongNoTxBECN,
       "starFrCongNoRecvDE": starFrCongNoRecvDE,
       "starFrCongNoTxDE": starFrCongNoTxDE,
       "starFrCongNoMarkDE": starFrCongNoMarkDE,
       "starFrCongNoDiscardWithDE": starFrCongNoDiscardWithDE,
       "starFrCongNoDiscardWoutDE": starFrCongNoDiscardWoutDE,
       "starAal5Info": starAal5Info,
       "starAal5ChannelStatisticsTbl": starAal5ChannelStatisticsTbl,
       "starAal5ChannelStatisticsInfoEntry": starAal5ChannelStatisticsInfoEntry,
       "starAal5ChannelStatisticsSlotIdInfo": starAal5ChannelStatisticsSlotIdInfo,
       "starAal5ChannelStatisticsChipId": starAal5ChannelStatisticsChipId,
       "starAal5NumPktsTransmitted": starAal5NumPktsTransmitted,
       "starAal5NumPktsReceived": starAal5NumPktsReceived,
       "starAal5NumTimesTxQueUnderrun": starAal5NumTimesTxQueUnderrun,
       "starAal5NumTimesRxQueUnderrun": starAal5NumTimesRxQueUnderrun,
       "starAal5NumTimesPktDropped": starAal5NumTimesPktDropped,
       "starAal5NumTimesInvalidCPI": starAal5NumTimesInvalidCPI,
       "starAal5NumTimesLengthViolation": starAal5NumTimesLengthViolation,
       "starAal5NumTimesOverRxDataUnit": starAal5NumTimesOverRxDataUnit,
       "starAal5NumTimesCRCViolation": starAal5NumTimesCRCViolation,
       "starAal5NumTimesTimerExpire": starAal5NumTimesTimerExpire,
       "starAal5StatusTbl": starAal5StatusTbl,
       "starAal5StatusInfoEntry": starAal5StatusInfoEntry,
       "starAal5ChannelStatusSlotIdInfo": starAal5ChannelStatusSlotIdInfo,
       "starAal5ChannelStatusChipId": starAal5ChannelStatusChipId,
       "starAal5NumPktsQuedToTransmit": starAal5NumPktsQuedToTransmit,
       "starAal5NumTxChannelsOpened": starAal5NumTxChannelsOpened,
       "starAal5NumRxChannelsOpened": starAal5NumRxChannelsOpened,
       "starAal5ConfigTxVCTbl": starAal5ConfigTxVCTbl,
       "starAal5ConfigTxVCInfoEntry": starAal5ConfigTxVCInfoEntry,
       "starAal5ConfigTxVCSlotIdInfo": starAal5ConfigTxVCSlotIdInfo,
       "starAal5ConfigTxVCChipId": starAal5ConfigTxVCChipId,
       "starAal5ConfigTxVPIndex": starAal5ConfigTxVPIndex,
       "starAal5ConfigTxVCIndex": starAal5ConfigTxVCIndex,
       "starAal5TxVCChannelType": starAal5TxVCChannelType,
       "starAal5CpcsUU": starAal5CpcsUU,
       "starAal5AvgI": starAal5AvgI,
       "starAal5AvgM": starAal5AvgM,
       "starAal5PeakRate": starAal5PeakRate,
       "starAal5MaxBurst": starAal5MaxBurst,
       "starAal5Priority": starAal5Priority,
       "starAal5ConfigRxVCTbl": starAal5ConfigRxVCTbl,
       "starAal5ConfigRxVCInfoEntry": starAal5ConfigRxVCInfoEntry,
       "starAal5ConfigRxVCSlotIdInfo": starAal5ConfigRxVCSlotIdInfo,
       "starAal5ConfigRxVCChipId": starAal5ConfigRxVCChipId,
       "starAal5ConfigRxVPIndex": starAal5ConfigRxVPIndex,
       "starAal5ConfigRxVCIndex": starAal5ConfigRxVCIndex,
       "starAal5PoolNum": starAal5PoolNum,
       "starAal5NumOAMDrops": starAal5NumOAMDrops,
       "starAal5RxVCChannelType": starAal5RxVCChannelType,
       "starAal5MaxNumSegments": starAal5MaxNumSegments,
       "starRout88Info": starRout88Info,
       "starRoutInfoTbl": starRoutInfoTbl,
       "starRoutInfoEntry": starRoutInfoEntry,
       "starSlotIdRoutInfo": starSlotIdRoutInfo,
       "starRoutChipId": starRoutChipId,
       "starRoutCurrentState": starRoutCurrentState,
       "starRoutChipVersion": starRoutChipVersion,
       "starRoutSramConfig": starRoutSramConfig,
       "starRoutBckPressureDly": starRoutBckPressureDly,
       "starRoutNumVpi": starRoutNumVpi,
       "starRoutConnectToSar": starRoutConnectToSar,
       "starRoutWatchDogConfig": starRoutWatchDogConfig,
       "starRoutEmptyQstate": starRoutEmptyQstate,
       "starRoutTxMarkedCellCnt": starRoutTxMarkedCellCnt,
       "starRoutRxMarkedCellCnt": starRoutRxMarkedCellCnt,
       "starRoutTxParityFailCnt": starRoutTxParityFailCnt,
       "starRoutBpIgnoredCnt": starRoutBpIgnoredCnt,
       "starRoutLiveFailCnt": starRoutLiveFailCnt,
       "starRoutWdFailCnt": starRoutWdFailCnt,
       "starRoutEmptyQCongQd": starRoutEmptyQCongQd,
       "starRoutEmptyQCurQd": starRoutEmptyQCurQd,
       "starRoutRatioAOrder1": starRoutRatioAOrder1,
       "starRoutRatioBOrder1": starRoutRatioBOrder1,
       "starRoutRatioAOrder2": starRoutRatioAOrder2,
       "starRoutRatioBOrder2": starRoutRatioBOrder2,
       "starRoutPrioQInfoTbl": starRoutPrioQInfoTbl,
       "starRoutPrioQInfoEntry": starRoutPrioQInfoEntry,
       "starSlotIdPrioQInfo": starSlotIdPrioQInfo,
       "starPrioQRoutChipId": starPrioQRoutChipId,
       "starRoutPrioQType": starRoutPrioQType,
       "starRoutPerPrioMaximumQd": starRoutPerPrioMaximumQd,
       "starRoutPerPrioCongestionQd": starRoutPerPrioCongestionQd,
       "starRoutPerPrioCurrentQd": starRoutPerPrioCurrentQd,
       "starRoutIsQCongested": starRoutIsQCongested,
       "starRoutIsCellInQueue": starRoutIsCellInQueue,
       "starRoutCcbInfoTbl": starRoutCcbInfoTbl,
       "starRoutCcbInfoEntry": starRoutCcbInfoEntry,
       "starCcbInfoSlotId": starCcbInfoSlotId,
       "starCcbRoutChipId": starCcbRoutChipId,
       "starRoutVp": starRoutVp,
       "starRoutVc": starRoutVc,
       "starRoutEnClpDrop": starRoutEnClpDrop,
       "starRoutEnAal5Epd": starRoutEnAal5Epd,
       "starRoutEnEfciMark": starRoutEnEfciMark,
       "starRoutEnExtDrop": starRoutEnExtDrop,
       "starRoutPti7": starRoutPti7,
       "starRoutPti6": starRoutPti6,
       "starRoutPti5": starRoutPti5,
       "starRoutPti4": starRoutPti4,
       "starRoutCcbQueue": starRoutCcbQueue,
       "starRoutMaxPerVcQd": starRoutMaxPerVcQd,
       "starRoutCongPerVcQd": starRoutCongPerVcQd,
       "starRoutCurPerVcQd": starRoutCurPerVcQd,
       "starRoutTags": starRoutTags,
       "starRoutIsVpTranslated": starRoutIsVpTranslated,
       "starRoutIsVcTranslated": starRoutIsVcTranslated,
       "starRoutNewVp": starRoutNewVp,
       "starRoutNewVc": starRoutNewVc,
       "starRoutCellRxCnt": starRoutCellRxCnt,
       "starRoutCellsDrpdCnt": starRoutCellsDrpdCnt,
       "starRoutCongCellCnt": starRoutCongCellCnt,
       "starHdlcControllerInfo": starHdlcControllerInfo,
       "starFiuHdlcStatusTbl": starFiuHdlcStatusTbl,
       "starFiuHdlcStatusInfoEntry": starFiuHdlcStatusInfoEntry,
       "starFiuHdlcStatusSlotId": starFiuHdlcStatusSlotId,
       "starFiuHdlcStatusChipId": starFiuHdlcStatusChipId,
       "starFiuHdlcRxBuffOverFlow": starFiuHdlcRxBuffOverFlow,
       "starFiuHdlcRxCountOverflow": starFiuHdlcRxCountOverflow,
       "starFiuHdlcRxShort": starFiuHdlcRxShort,
       "starFiuHdlcRxAbort": starFiuHdlcRxAbort,
       "starFiuHdlcRxOverrun": starFiuHdlcRxOverrun,
       "starFiuHdlcRxCrc": starFiuHdlcRxCrc,
       "starFiuHdlcRxPduCount": starFiuHdlcRxPduCount,
       "starFiuHdlcRxByteCount": starFiuHdlcRxByteCount,
       "starFiuHdlcTxUnderrun": starFiuHdlcTxUnderrun,
       "starFiuHdlcTxPduCount": starFiuHdlcTxPduCount,
       "starFiuHdlcTxByteCount": starFiuHdlcTxByteCount,
       "starFiuHdlcLinkstatus": starFiuHdlcLinkstatus,
       "starFiuHdlcTxBuffOverFlow": starFiuHdlcTxBuffOverFlow,
       "starFiuHdlcTxCountOverflow": starFiuHdlcTxCountOverflow,
       "starRclInfo": starRclInfo,
       "starRclInfoTbl": starRclInfoTbl,
       "starRclInfoEntry": starRclInfoEntry,
       "starRclInfoSlotId": starRclInfoSlotId,
       "starRclNumRegAppl": starRclNumRegAppl,
       "starRclNumSwitchovers": starRclNumSwitchovers,
       "starRclSwitchoverThreshold": starRclSwitchoverThreshold,
       "starRclSwitchoverTimeLimit": starRclSwitchoverTimeLimit,
       "starRclSwitchoverResetTime": starRclSwitchoverResetTime,
       "starRclLockoutFlag": starRclLockoutFlag,
       "starRclHmcTestStatus": starRclHmcTestStatus,
       "starRclHmcTestResult": starRclHmcTestResult,
       "starRclModuleStatus": starRclModuleStatus,
       "starRclSwitchoverReason": starRclSwitchoverReason,
       "starRclSwitchoverTime": starRclSwitchoverTime,
       "starRclRegInfoTbl": starRclRegInfoTbl,
       "starRclRegInfoEntry": starRclRegInfoEntry,
       "starRclRegInfoSlotId": starRclRegInfoSlotId,
       "starRclRegKey": starRclRegKey,
       "starRclRegTaskName": starRclRegTaskName,
       "starRclRegQueueName": starRclRegQueueName,
       "starCasInfo": starCasInfo,
       "starCasStatusInfoTbl": starCasStatusInfoTbl,
       "starCasStatusInfoEntry": starCasStatusInfoEntry,
       "starCasStatusSlotId": starCasStatusSlotId,
       "starCasStatusPortId": starCasStatusPortId,
       "starCasStatusChannelId": starCasStatusChannelId,
       "starCasStatusConfigured": starCasStatusConfigured,
       "starCasStatusCurrentStatus": starCasStatusCurrentStatus,
       "starCasStatusStatusChange": starCasStatusStatusChange,
       "starCasStatusNewStatusSampleNum": starCasStatusNewStatusSampleNum,
       "starCasStatusPortInfoTbl": starCasStatusPortInfoTbl,
       "starCasStatusPortInfoEntry": starCasStatusPortInfoEntry,
       "starCasStatusPortSlotId": starCasStatusPortSlotId,
       "starCasStatusPortPortId": starCasStatusPortPortId,
       "starCasStatusPortConfigured": starCasStatusPortConfigured,
       "starCasStatusPortCasSamplePeriod": starCasStatusPortCasSamplePeriod,
       "starCasStatusPortCasSampleNum": starCasStatusPortCasSampleNum,
       "starCesInfo": starCesInfo,
       "starDS1E1CESConfTable": starDS1E1CESConfTable,
       "starDS1E1CESConfEntry": starDS1E1CESConfEntry,
       "starDS1E1CESSlotId": starDS1E1CESSlotId,
       "starDS1E1CESPortId": starDS1E1CESPortId,
       "starDS1E1CESChannelId": starDS1E1CESChannelId,
       "starDS1E1CESMapATMIndex": starDS1E1CESMapATMIndex,
       "starDS1E1CESMapVPI": starDS1E1CESMapVPI,
       "starDS1E1CESMapVCI": starDS1E1CESMapVCI,
       "starDS1E1CESCBRService": starDS1E1CESCBRService,
       "starDS1E1CESCBRClockMode": starDS1E1CESCBRClockMode,
       "starDS1E1CESCas": starDS1E1CESCas,
       "starDS1E1CESPartialFill": starDS1E1CESPartialFill,
       "starDS1E1CESBufMaxSize": starDS1E1CESBufMaxSize,
       "starDS1E1CESCDVRxT": starDS1E1CESCDVRxT,
       "starDS1E1CESCellLossIntegPrd": starDS1E1CESCellLossIntegPrd,
       "starDS1E1CESStatsTable": starDS1E1CESStatsTable,
       "starDS1E1CESStatsEntry": starDS1E1CESStatsEntry,
       "starDS1E1CESStatSlotId": starDS1E1CESStatSlotId,
       "starDS1E1CESStatDeviceId": starDS1E1CESStatDeviceId,
       "starDS1E1CESStatPortId": starDS1E1CESStatPortId,
       "starDS1E1CESStatChannelId": starDS1E1CESStatChannelId,
       "starDS1E1CESReassCells": starDS1E1CESReassCells,
       "starDS1E1CESHdrErrors": starDS1E1CESHdrErrors,
       "starDS1E1CESPointerReframes": starDS1E1CESPointerReframes,
       "starDS1E1CESLostCells": starDS1E1CESLostCells,
       "starDS1E1CESBufUnderflows": starDS1E1CESBufUnderflows,
       "starDS1E1CESBufOverflows": starDS1E1CESBufOverflows,
       "starDS1E1CESCellLossStatus": starDS1E1CESCellLossStatus,
       "starPort": starPort,
       "starPortTable": starPortTable,
       "starPortEntry": starPortEntry,
       "starPortIndex": starPortIndex,
       "starPortIfIndex": starPortIfIndex,
       "starPortType": starPortType,
       "starPortConfig": starPortConfig,
       "starPortDescr": starPortDescr,
       "starPortAdminStatus": starPortAdminStatus,
       "starPortAtmAddress": starPortAtmAddress,
       "starPortLastChanged": starPortLastChanged,
       "starPortAlarmStatus": starPortAlarmStatus,
       "starPortRemoteAtmAddress": starPortRemoteAtmAddress,
       "starPortOperStatus": starPortOperStatus,
       "starPortIFType": starPortIFType,
       "starPortMaxVPINumber": starPortMaxVPINumber,
       "starPortUsedVPINumber": starPortUsedVPINumber,
       "starPortMaxVCINumber": starPortMaxVCINumber,
       "starPortUsedVCINumber": starPortUsedVCINumber,
       "starPortMaxFixedCapacity": starPortMaxFixedCapacity,
       "starPortMaxVariableCapacity": starPortMaxVariableCapacity,
       "starPortUsedFwdFixedCapacity": starPortUsedFwdFixedCapacity,
       "starPortUsedFwdVariableCapacity": starPortUsedFwdVariableCapacity,
       "starPortUsedBwdFixedCapacity": starPortUsedBwdFixedCapacity,
       "starPortUsedBwdVariableCapacity": starPortUsedBwdVariableCapacity,
       "starPortAvailableVpi": starPortAvailableVpi,
       "starPortDS1FramerTable": starPortDS1FramerTable,
       "starPortDS1FramerEntry": starPortDS1FramerEntry,
       "starPortDS1FramerIndex": starPortDS1FramerIndex,
       "starPortDS1FramerRevision": starPortDS1FramerRevision,
       "starPortDS1FramerFrameMode": starPortDS1FramerFrameMode,
       "starPortDS1FramerLineCoding": starPortDS1FramerLineCoding,
       "starPortDS1FramerBPVCounter": starPortDS1FramerBPVCounter,
       "starPortDS1FramerFBErrorCounter": starPortDS1FramerFBErrorCounter,
       "starPortDS1FramerCRCErrorCounter": starPortDS1FramerCRCErrorCounter,
       "starPortDS1FramerCOFACounter": starPortDS1FramerCOFACounter,
       "starPortE1FramerTable": starPortE1FramerTable,
       "starPortE1FramerEntry": starPortE1FramerEntry,
       "starPortE1FramerIndex": starPortE1FramerIndex,
       "starPortE1FramerRevision": starPortE1FramerRevision,
       "starPortE1FramerLineCoding": starPortE1FramerLineCoding,
       "starPortE1FramerSignalMode": starPortE1FramerSignalMode,
       "starPortE1FramerCRCErrorCounter": starPortE1FramerCRCErrorCounter,
       "starPortE1FramerLCVErrorCounter": starPortE1FramerLCVErrorCounter,
       "starPortE1FramerFASErrorCounter": starPortE1FramerFASErrorCounter,
       "starPortDS3FramerTable": starPortDS3FramerTable,
       "starPortDS3FramerEntry": starPortDS3FramerEntry,
       "starPortDS3FramerIndex": starPortDS3FramerIndex,
       "starPortDS3FramerRevision": starPortDS3FramerRevision,
       "starPortDS3FramerFramingMode": starPortDS3FramerFramingMode,
       "starPortSonetUniTable": starPortSonetUniTable,
       "starPortSonetUniEntry": starPortSonetUniEntry,
       "starPortSonetUniIndex": starPortSonetUniIndex,
       "starPortSonetUniMsgTxCt": starPortSonetUniMsgTxCt,
       "starPortSonetUniMsgRxCt": starPortSonetUniMsgRxCt,
       "starPortSonetUniHECErrorCt": starPortSonetUniHECErrorCt,
       "starPortDs3UniTable": starPortDs3UniTable,
       "starPortDs3UniEntry": starPortDs3UniEntry,
       "starDsx3CurrentIndex": starDsx3CurrentIndex,
       "starPortDs3TxFEBEcount": starPortDs3TxFEBEcount,
       "starPortDs3RxFEBEcount": starPortDs3RxFEBEcount,
       "starPortPlcpTxFEBEcount": starPortPlcpTxFEBEcount,
       "starPortPlcpRxFEBEcount": starPortPlcpRxFEBEcount,
       "starPortRAIstatus": starPortRAIstatus,
       "starPortPlcpCVcount": starPortPlcpCVcount,
       "starPortPlcpEScount": starPortPlcpEScount,
       "starPortPlcpSEScount": starPortPlcpSEScount,
       "starPortPlcpEFScount": starPortPlcpEFScount,
       "starPortPlcpSEFScount": starPortPlcpSEFScount,
       "starPortPlcpUAScount": starPortPlcpUAScount,
       "starPortDs3LSEScount": starPortDs3LSEScount,
       "starPortDs3AISScount": starPortDs3AISScount,
       "starPortDs3EFScount": starPortDs3EFScount,
       "starPortPdhUniTable": starPortPdhUniTable,
       "starPortPdhUniEntry": starPortPdhUniEntry,
       "starPortPdhUniIndex": starPortPdhUniIndex,
       "starPortPdhUniMsgTxCt": starPortPdhUniMsgTxCt,
       "starPortPdhUniMsgRxCt": starPortPdhUniMsgRxCt,
       "starPortPdhUniHECErrCt": starPortPdhUniHECErrCt,
       "starPortDS1ATMTable": starPortDS1ATMTable,
       "starPortDS1ATMEntry": starPortDS1ATMEntry,
       "starPortDS1ATMIndex": starPortDS1ATMIndex,
       "starPortDS1ATMHecCnt": starPortDS1ATMHecCnt,
       "starPortDS1ATMDiscardCellCnt": starPortDS1ATMDiscardCellCnt,
       "starPortDS1ATMErrCorrectCellCnt": starPortDS1ATMErrCorrectCellCnt,
       "starPortDS1ATMRxBusyCellCnt": starPortDS1ATMRxBusyCellCnt,
       "starPortDS1ATMTxBusyCellCnt": starPortDS1ATMTxBusyCellCnt,
       "starPortM32Table": starPortM32Table,
       "starPortM32Entry": starPortM32Entry,
       "starPortM32SlotId": starPortM32SlotId,
       "starPortM32ChipId": starPortM32ChipId,
       "starPortM32RxCrcErrorCount": starPortM32RxCrcErrorCount,
       "starPortM32RxNobErrorCount": starPortM32RxNobErrorCount,
       "starPortM32RxLfdErrorCount": starPortM32RxLfdErrorCount,
       "starPortM32RxIntBufOverFlwCount": starPortM32RxIntBufOverFlwCount,
       "starPortM32RxAbortCount": starPortM32RxAbortCount,
       "starPortM32RxShortFrameCount": starPortM32RxShortFrameCount,
       "starPortM32RxDiscardFrameCount": starPortM32RxDiscardFrameCount,
       "starPortM32RxPduCount": starPortM32RxPduCount,
       "starPortM32RxByteCount": starPortM32RxByteCount,
       "starPortM32TxErrorCount": starPortM32TxErrorCount,
       "starPortM32TxPduCount": starPortM32TxPduCount,
       "starPortM32TxByteCount": starPortM32TxByteCount,
       "starPortHdlcConfigTable": starPortHdlcConfigTable,
       "starPortHdlcConfigEntry": starPortHdlcConfigEntry,
       "starPortHdlcIndex": starPortHdlcIndex,
       "starPortHdlcLineSpeed": starPortHdlcLineSpeed,
       "starPortHdlcLineEncoding": starPortHdlcLineEncoding,
       "starPortHdlcCrcMode": starPortHdlcCrcMode,
       "starPortHdlcDteDce": starPortHdlcDteDce,
       "starPortHdlcClockMode": starPortHdlcClockMode,
       "starSvcmStatusTable": starSvcmStatusTable,
       "starSvcmStatusEntry": starSvcmStatusEntry,
       "starSvcmActiveCallCnt": starSvcmActiveCallCnt,
       "starSvcmLastTxCause": starSvcmLastTxCause,
       "starSvcmPtoPOrgActiveConnectionCnt": starSvcmPtoPOrgActiveConnectionCnt,
       "starSvcmPtoPTermActiveConnectionCnt": starSvcmPtoPTermActiveConnectionCnt,
       "starSvcmPtoMPOrgActiveConnectionCnt": starSvcmPtoMPOrgActiveConnectionCnt,
       "starSvcmPtoMPTermActiveConnectionCnt": starSvcmPtoMPTermActiveConnectionCnt,
       "starSvcmConnectionSetupFailCnt": starSvcmConnectionSetupFailCnt,
       "starSvcmTxCallProceedingMsgCnt": starSvcmTxCallProceedingMsgCnt,
       "starSvcmRxCallProceedingMsgCnt": starSvcmRxCallProceedingMsgCnt,
       "starSvcmTxConnectMsgCnt": starSvcmTxConnectMsgCnt,
       "starSvcmRxConnectMsgCnt": starSvcmRxConnectMsgCnt,
       "starSvcmTxSetupMsgCnt": starSvcmTxSetupMsgCnt,
       "starSvcmRxSetupMsgCnt": starSvcmRxSetupMsgCnt,
       "starSvcmTxReleaseMsgCnt": starSvcmTxReleaseMsgCnt,
       "starSvcmRxReleaseMsgCnt": starSvcmRxReleaseMsgCnt,
       "starSvcmTxReleaseCompleteMsgCnt": starSvcmTxReleaseCompleteMsgCnt,
       "starSvcmRxReleaseCompleteMsgCnt": starSvcmRxReleaseCompleteMsgCnt,
       "starSvcmTxRestartMsgCnt": starSvcmTxRestartMsgCnt,
       "starSvcmRxRestartMsgCnt": starSvcmRxRestartMsgCnt,
       "starSvcmTxRestartAckMsgCnt": starSvcmTxRestartAckMsgCnt,
       "starSvcmRxRestartAckMsgCnt": starSvcmRxRestartAckMsgCnt,
       "starSvcmTxStatusMsgCnt": starSvcmTxStatusMsgCnt,
       "starSvcmRxStatusMsgCnt": starSvcmRxStatusMsgCnt,
       "starSvcmTxStatusEnquiryMsgCnt": starSvcmTxStatusEnquiryMsgCnt,
       "starSvcmRxStatusEnquiryMsgCnt": starSvcmRxStatusEnquiryMsgCnt,
       "starSvcmAiuStatsTable": starSvcmAiuStatsTable,
       "starSvcmAiuStatsEntry": starSvcmAiuStatsEntry,
       "starSvcmAiuTxSSCOPDiscardedCells": starSvcmAiuTxSSCOPDiscardedCells,
       "starSvcmAiuRxBGNCells": starSvcmAiuRxBGNCells,
       "starSvcmAiuRxBGAKCells": starSvcmAiuRxBGAKCells,
       "starSvcmAiuRxENDCells": starSvcmAiuRxENDCells,
       "starSvcmAiuRxRSCells": starSvcmAiuRxRSCells,
       "starSvcmAiuRxRSAKCells": starSvcmAiuRxRSAKCells,
       "starSvcmAiuRxSDCells": starSvcmAiuRxSDCells,
       "starSvcmAiuRxSDPCCells": starSvcmAiuRxSDPCCells,
       "starSvcmAiuRxPOLLCells": starSvcmAiuRxPOLLCells,
       "starSvcmAiuRxSTATCells": starSvcmAiuRxSTATCells,
       "starSvcmAiuRxUSTATCells": starSvcmAiuRxUSTATCells,
       "starSvcmAiuRxUDCells": starSvcmAiuRxUDCells,
       "starSvcmAiuRxMDCells": starSvcmAiuRxMDCells,
       "starSvcmAiuTxAddPartyMsgCnt": starSvcmAiuTxAddPartyMsgCnt,
       "starSvcmAiuRxAddPartyMsgCnt": starSvcmAiuRxAddPartyMsgCnt,
       "starSvcmAiuTxAddPartyRejMsgCnt": starSvcmAiuTxAddPartyRejMsgCnt,
       "starSvcmAiuRxAddPartyRejMsgCnt": starSvcmAiuRxAddPartyRejMsgCnt,
       "starSvcmAiuTxAddPartyAckMsgCnt": starSvcmAiuTxAddPartyAckMsgCnt,
       "starSvcmAiuRxAddPartyAckMsgCnt": starSvcmAiuRxAddPartyAckMsgCnt,
       "starSvcmAiuTxDropPartyMsgCnt": starSvcmAiuTxDropPartyMsgCnt,
       "starSvcmAiuRxDropPartyMsgCnt": starSvcmAiuRxDropPartyMsgCnt,
       "starSvcmAiuTxDropPartyAckMsgCnt": starSvcmAiuTxDropPartyAckMsgCnt,
       "starSvcmAiuRxDropPartyAckMsgCnt": starSvcmAiuRxDropPartyAckMsgCnt,
       "starSvcmFiuStatsTable": starSvcmFiuStatsTable,
       "starSvcmFiuStatsEntry": starSvcmFiuStatsEntry,
       "starSvcmFiuQ933TimerExpiryCnt": starSvcmFiuQ933TimerExpiryCnt,
       "starSvcmFiuQ933IllegalMsgCnt": starSvcmFiuQ933IllegalMsgCnt,
       "starSvcmFiuQ922TimerExpiryCnt": starSvcmFiuQ922TimerExpiryCnt,
       "starSvcmFiuQ922LinkFailIndicationCnt": starSvcmFiuQ922LinkFailIndicationCnt,
       "starSvcmFiuQ922UnackedMsgCnt": starSvcmFiuQ922UnackedMsgCnt,
       "starPortTrunkTable": starPortTrunkTable,
       "starPortTrunkEntry": starPortTrunkEntry,
       "starTotalInFixedCapa": starTotalInFixedCapa,
       "starTotalOutFixedCapa": starTotalOutFixedCapa,
       "starTotalInVariableCapa": starTotalInVariableCapa,
       "starTotalOutVariableCapa": starTotalOutVariableCapa,
       "starPvcInFixedCapa": starPvcInFixedCapa,
       "starPvcOutFixedCapa": starPvcOutFixedCapa,
       "starPvcInVariableCapa": starPvcInVariableCapa,
       "starPvcOutVariableCapa": starPvcOutVariableCapa,
       "starSvcInFixedCapa": starSvcInFixedCapa,
       "starSvcOutFixedCapa": starSvcOutFixedCapa,
       "starSvcInVariableCapa": starSvcInVariableCapa,
       "starSvcOutVariableCapa": starSvcOutVariableCapa,
       "starPortRealStatusTable": starPortRealStatusTable,
       "starPortRealStatusEntry": starPortRealStatusEntry,
       "starPortConfigRealStatus": starPortConfigRealStatus,
       "starPortAlarmRealStatus": starPortAlarmRealStatus,
       "starPortOperRealStatus": starPortOperRealStatus,
       "starPortRealStatusDescr": starPortRealStatusDescr,
       "starPortPmThresholdTable": starPortPmThresholdTable,
       "starPortPmThresholdEntry": starPortPmThresholdEntry,
       "starPortPmThreshIdx": starPortPmThreshIdx,
       "starPortPmTrigger": starPortPmTrigger,
       "starPortPmFlag": starPortPmFlag,
       "starPortPmThreshValue": starPortPmThreshValue,
       "starPortPmRearmValue": starPortPmRearmValue,
       "starPortPmPriority": starPortPmPriority,
       "starPortPmInterval": starPortPmInterval,
       "starPortPmCnt": starPortPmCnt,
       "starPortLMIStatsTable": starPortLMIStatsTable,
       "starPortLMIStatsEntry": starPortLMIStatsEntry,
       "starPortLMILinkStats": starPortLMILinkStats,
       "starPortFiu12Ds1Table": starPortFiu12Ds1Table,
       "starPortFiu12Ds1Entry": starPortFiu12Ds1Entry,
       "starPortFiu12Index": starPortFiu12Index,
       "starPortFiu12Ds1LCV": starPortFiu12Ds1LCV,
       "starPortFiu12Ds1BEE": starPortFiu12Ds1BEE,
       "starPortFiu12Ds1FER": starPortFiu12Ds1FER,
       "starPortFiu12Ds1OOF": starPortFiu12Ds1OOF,
       "starPortFiu12E1FER": starPortFiu12E1FER,
       "starPortFiu12E1FEBE": starPortFiu12E1FEBE,
       "starPortFiu12E1CRC": starPortFiu12E1CRC,
       "starPortFiu12E1LCV": starPortFiu12E1LCV,
       "starPortFiu12Ds3FramerTable": starPortFiu12Ds3FramerTable,
       "starPortFiu12Ds3FramerEntry": starPortFiu12Ds3FramerEntry,
       "starPortFiu12Ds3FramerIndex": starPortFiu12Ds3FramerIndex,
       "starPortFiu12Ds3FramerLCV": starPortFiu12Ds3FramerLCV,
       "starPortFiu12Ds3FramerFERR": starPortFiu12Ds3FramerFERR,
       "starPortFiu12Ds3FramerDXZS": starPortFiu12Ds3FramerDXZS,
       "starPortFiu12Ds3FramerPERR": starPortFiu12Ds3FramerPERR,
       "starPortFiu12Ds3FramerCPERR": starPortFiu12Ds3FramerCPERR,
       "starPortFiu12Ds3FramerFEBE": starPortFiu12Ds3FramerFEBE,
       "starPhysicalLoopbackTable": starPhysicalLoopbackTable,
       "starPhysicalLoopbackEntry": starPhysicalLoopbackEntry,
       "starPhysicalLoopbackDs1Port": starPhysicalLoopbackDs1Port,
       "starPhysicalLoopbackMethod": starPhysicalLoopbackMethod,
       "starPhysicalLoopbackCtrl": starPhysicalLoopbackCtrl,
       "starPhysicalLoopbackStatus": starPhysicalLoopbackStatus,
       "starPhysicalLoopbackDescr": starPhysicalLoopbackDescr,
       "starPPP": starPPP,
       "starPPPLinkStatusTable": starPPPLinkStatusTable,
       "starPPPLinkStatusEntry": starPPPLinkStatusEntry,
       "starPPPLinkStatusPhysicalIndex": starPPPLinkStatusPhysicalIndex,
       "starPPPLinkStatusBadAddresses": starPPPLinkStatusBadAddresses,
       "starPPPLinkStatusBadControls": starPPPLinkStatusBadControls,
       "starPPPLinkStatusPacketTooLongs": starPPPLinkStatusPacketTooLongs,
       "starPPPLinkStatusBadFCSs": starPPPLinkStatusBadFCSs,
       "starPPPLinkStatusLocalMRU": starPPPLinkStatusLocalMRU,
       "starPPPLinkStatusRemoteMRU": starPPPLinkStatusRemoteMRU,
       "starPPPLinkStatusLocalToPeerACCMap": starPPPLinkStatusLocalToPeerACCMap,
       "starPPPLinkStatusPeerToLocalACCMap": starPPPLinkStatusPeerToLocalACCMap,
       "starPPPLinkStatusLocalToRemotePC": starPPPLinkStatusLocalToRemotePC,
       "starPPPLinkStatusRemoteToLocalPC": starPPPLinkStatusRemoteToLocalPC,
       "starPPPLinkStatusLocalToRemoteACFC": starPPPLinkStatusLocalToRemoteACFC,
       "starPPPLinkStatusRemoteToLocalACFC": starPPPLinkStatusRemoteToLocalACFC,
       "starPPPLinkStatusTransmitFcsSize": starPPPLinkStatusTransmitFcsSize,
       "starPPPLinkStatusReceiveFcsSize": starPPPLinkStatusReceiveFcsSize,
       "starPPPLqrTable": starPPPLqrTable,
       "starPPPLqrEntry": starPPPLqrEntry,
       "starPPPLqrQuality": starPPPLqrQuality,
       "starPPPLqrInGoodOctets": starPPPLqrInGoodOctets,
       "starPPPLqrLocalPeriod": starPPPLqrLocalPeriod,
       "starPPPLqrRemotePeriod": starPPPLqrRemotePeriod,
       "starPPPLqrOutLQRs": starPPPLqrOutLQRs,
       "starPPPLqrInLQRs": starPPPLqrInLQRs,
       "starPPPIpTable": starPPPIpTable,
       "starPPPIpEntry": starPPPIpEntry,
       "starPPPIpOperStatus": starPPPIpOperStatus,
       "starPPPIpLocalToRemoteCP": starPPPIpLocalToRemoteCP,
       "starPPPIpRemoteToLocalCP": starPPPIpRemoteToLocalCP,
       "starPPPIpRemoteMaxSlotId": starPPPIpRemoteMaxSlotId,
       "starPPPIpLocalMaxSlotId": starPPPIpLocalMaxSlotId,
       "starConn": starConn,
       "starVplStatsTable": starVplStatsTable,
       "starVplStatsEntry": starVplStatsEntry,
       "starVplSlotIndex": starVplSlotIndex,
       "starVplPortIndex": starVplPortIndex,
       "starVplSourceNode": starVplSourceNode,
       "starVplSourceSlot": starVplSourceSlot,
       "starVplSourcePort": starVplSourcePort,
       "starVplSourceVpi": starVplSourceVpi,
       "starVplSourceVci": starVplSourceVci,
       "starVplConnRole": starVplConnRole,
       "starVplStatsTimeStamp": starVplStatsTimeStamp,
       "starVplNumOAMInvalidCRC": starVplNumOAMInvalidCRC,
       "starVplRtCongestedState": starVplRtCongestedState,
       "starVplRtNewVpi": starVplRtNewVpi,
       "starVplRtCellsRxCount": starVplRtCellsRxCount,
       "starVplRtCellsDroppedCount": starVplRtCellsDroppedCount,
       "starVplRtCellsCongCount": starVplRtCellsCongCount,
       "starVplUpcGcra0ViolCount": starVplUpcGcra0ViolCount,
       "starVplUpcGcra1ViolCount": starVplUpcGcra1ViolCount,
       "starVplUpcCellsCLP0": starVplUpcCellsCLP0,
       "starVplUpcTotalCells": starVplUpcTotalCells,
       "starVplUpcTotalOAMCells": starVplUpcTotalOAMCells,
       "starVclStatsTable": starVclStatsTable,
       "starVclStatsEntry": starVclStatsEntry,
       "starVclSlotIndex": starVclSlotIndex,
       "starVclPortIndex": starVclPortIndex,
       "starVclSourceNode": starVclSourceNode,
       "starVclSourceSlot": starVclSourceSlot,
       "starVclSourcePort": starVclSourcePort,
       "starVclSourceVpi": starVclSourceVpi,
       "starVclSourceVci": starVclSourceVci,
       "starVclConnRole": starVclConnRole,
       "starVclStatsTimeStamp": starVclStatsTimeStamp,
       "starVclNumOAMInvalidCRC": starVclNumOAMInvalidCRC,
       "starVclRtCongestedState": starVclRtCongestedState,
       "starVclRtLastAal5State": starVclRtLastAal5State,
       "starVclRtNewVpi": starVclRtNewVpi,
       "starVclRtNewVci": starVclRtNewVci,
       "starVclRtCellsRxCount": starVclRtCellsRxCount,
       "starVclRtCellsDroppedCount": starVclRtCellsDroppedCount,
       "starVclRtCellsCongCount": starVclRtCellsCongCount,
       "starVclUpcGcra0ViolCount": starVclUpcGcra0ViolCount,
       "starVclUpcGcra1ViolCount": starVclUpcGcra1ViolCount,
       "starVclUpcCellsCLP0": starVclUpcCellsCLP0,
       "starVclUpcTotalCells": starVclUpcTotalCells,
       "starVclUpcTotalOAMCells": starVclUpcTotalOAMCells,
       "starVclSourceDlci": starVclSourceDlci,
       "starVclSourceTimeslot": starVclSourceTimeslot,
       "starVclSourceIftype": starVclSourceIftype,
       "starVclSourceLeafno": starVclSourceLeafno,
       "starVpiRangeTable": starVpiRangeTable,
       "starVpiRangeEntry": starVpiRangeEntry,
       "starVpiIndex": starVpiIndex,
       "starVpiVciBitRangeClass": starVpiVciBitRangeClass,
       "starVpiBitRangeValue": starVpiBitRangeValue,
       "starVciBitRangeValue": starVciBitRangeValue,
       "starAvailableVpiValue": starAvailableVpiValue,
       "starLoopbackCtrTable": starLoopbackCtrTable,
       "starLoopbackCtrEntry": starLoopbackCtrEntry,
       "starLoopbackCtrPortIndex": starLoopbackCtrPortIndex,
       "starLoopbackCtrVpi": starLoopbackCtrVpi,
       "starLoopbackCtrVci": starLoopbackCtrVci,
       "starLoopbackCtrDeviceId": starLoopbackCtrDeviceId,
       "starLoopbackCtrType": starLoopbackCtrType,
       "starLoopbackCtrEndType": starLoopbackCtrEndType,
       "starLoopbackCtrTxCellNo": starLoopbackCtrTxCellNo,
       "starLoopbackCtrTimetoWait": starLoopbackCtrTimetoWait,
       "starLoopbackCtrSetup": starLoopbackCtrSetup,
       "starLoopbackCtrMethod": starLoopbackCtrMethod,
       "starLoopbackCtrGeneration": starLoopbackCtrGeneration,
       "starLoopbackCtrInputType": starLoopbackCtrInputType,
       "starLoopbackCtrPdhNum": starLoopbackCtrPdhNum,
       "starLoopbackCtrCellSpeed": starLoopbackCtrCellSpeed,
       "starLoopbackCtrGCIDNeId": starLoopbackCtrGCIDNeId,
       "starLoopbackCtrGCIDSlotIndex": starLoopbackCtrGCIDSlotIndex,
       "starLoopbackCtrGCIDPortIndex": starLoopbackCtrGCIDPortIndex,
       "starLoopbackCtrGCIDModuleIfType": starLoopbackCtrGCIDModuleIfType,
       "starLoopbackCtrGCIDVpi": starLoopbackCtrGCIDVpi,
       "starLoopbackCtrGCIDVci": starLoopbackCtrGCIDVci,
       "starLoopbackCtrGCIDDlci": starLoopbackCtrGCIDDlci,
       "starLoopbackCtrGCIDTimeSlot": starLoopbackCtrGCIDTimeSlot,
       "starLoopbackCtrGCIDLeafNum": starLoopbackCtrGCIDLeafNum,
       "starLoopbackCtrAssignedSessionNo": starLoopbackCtrAssignedSessionNo,
       "starLoopbackCtrArea": starLoopbackCtrArea,
       "starLoopbackCtrChannelType": starLoopbackCtrChannelType,
       "starLoopbackCtrLastSetupResult": starLoopbackCtrLastSetupResult,
       "starLoopbackCtrPortNum": starLoopbackCtrPortNum,
       "starLoopbackCtrGenCellType": starLoopbackCtrGenCellType,
       "starLoopbackResultTable": starLoopbackResultTable,
       "starLoopbackResultEntry": starLoopbackResultEntry,
       "starLoopbackResultGeneratedCells": starLoopbackResultGeneratedCells,
       "starLoopbackResultReturnedCells": starLoopbackResultReturnedCells,
       "starPmCtrTable": starPmCtrTable,
       "starPmCtrEntry": starPmCtrEntry,
       "starPmCtrUpcId": starPmCtrUpcId,
       "starPmCtrVpi": starPmCtrVpi,
       "starPmCtrVci": starPmCtrVci,
       "starPmCtrSegmentType": starPmCtrSegmentType,
       "starPmCtrNodeType": starPmCtrNodeType,
       "starPmCtrBlockSize": starPmCtrBlockSize,
       "starPmCtrPmCellClp": starPmCtrPmCellClp,
       "starPmCtrBackRptGen": starPmCtrBackRptGen,
       "starPmCtrActivate": starPmCtrActivate,
       "starPmCtrStart": starPmCtrStart,
       "starPmCtrLastAssignedSession": starPmCtrLastAssignedSession,
       "starPmTable": starPmTable,
       "starPmEntry": starPmEntry,
       "starPmTotalCellClp0Count": starPmTotalCellClp0Count,
       "starPmTotalCellClp01Count": starPmTotalCellClp01Count,
       "starPmLostCellClp0Count": starPmLostCellClp0Count,
       "starPmLostCellClp01Count": starPmLostCellClp01Count,
       "starPmErroredCellCount": starPmErroredCellCount,
       "starPmMisinsertedCellCount": starPmMisinsertedCellCount,
       "starPmSeverelyErroredBlockCount": starPmSeverelyErroredBlockCount,
       "starPvcRouteTable": starPvcRouteTable,
       "starPvcRouteEntry": starPvcRouteEntry,
       "starPvcRouteGCIDSlotId": starPvcRouteGCIDSlotId,
       "starPvcRouteGCIDPortId": starPvcRouteGCIDPortId,
       "starPvcRouteGCIDIfType": starPvcRouteGCIDIfType,
       "starPvcRouteGCIDConnId": starPvcRouteGCIDConnId,
       "starPvcRouteGCIDLeafId": starPvcRouteGCIDLeafId,
       "starPvcRouteHopIndex": starPvcRouteHopIndex,
       "starPvcRouteOutgoingNeId": starPvcRouteOutgoingNeId,
       "starPvcRouteOutgoingNodeType": starPvcRouteOutgoingNodeType,
       "starPvcRouteOutgoingModuleId": starPvcRouteOutgoingModuleId,
       "starPvcRouteOutgoingPortId": starPvcRouteOutgoingPortId,
       "starCcCtrTable": starCcCtrTable,
       "starCcCtrEntry": starCcCtrEntry,
       "starCcCtrPortIndex": starCcCtrPortIndex,
       "starCcCtrVpi": starCcCtrVpi,
       "starCcCtrVci": starCcCtrVci,
       "starCcCtrType": starCcCtrType,
       "starCcCtrEndType": starCcCtrEndType,
       "starCcCtrSetup": starCcCtrSetup,
       "starCcCtrInputType": starCcCtrInputType,
       "starCcCtrGCIDNeId": starCcCtrGCIDNeId,
       "starCcCtrGCIDSlotIndex": starCcCtrGCIDSlotIndex,
       "starCcCtrGCIDPortIndex": starCcCtrGCIDPortIndex,
       "starCcCtrGCIDModuleIfType": starCcCtrGCIDModuleIfType,
       "starCcCtrGCIDVpi": starCcCtrGCIDVpi,
       "starCcCtrGCIDVci": starCcCtrGCIDVci,
       "starCcCtrGCIDDlci": starCcCtrGCIDDlci,
       "starCcCtrGCIDTimeSlot": starCcCtrGCIDTimeSlot,
       "starCcCtrGCIDLeafNum": starCcCtrGCIDLeafNum,
       "starPortCellStatsTable": starPortCellStatsTable,
       "starPortCellStatsEntry": starPortCellStatsEntry,
       "starPortTimeStamp": starPortTimeStamp,
       "starPortRtCellsRxCount": starPortRtCellsRxCount,
       "starPortRtCellsDroppedCount": starPortRtCellsDroppedCount,
       "starPortRtCellsCongCount": starPortRtCellsCongCount,
       "starPortUpcCellsCLP0": starPortUpcCellsCLP0,
       "starPortUpcTotalCells": starPortUpcTotalCells,
       "starPortUpcGcra0ViolCount": starPortUpcGcra0ViolCount,
       "starPortUpcGcra1ViolCount": starPortUpcGcra1ViolCount,
       "starPortUpcTotalOAMCells": starPortUpcTotalOAMCells,
       "starAtmPointTable": starAtmPointTable,
       "starAtmPointEntry": starAtmPointEntry,
       "starAtmPointPointType": starAtmPointPointType,
       "starSvcRouteTable": starSvcRouteTable,
       "starSvcRouteEntry": starSvcRouteEntry,
       "starSvcRouteGCIDSlotId": starSvcRouteGCIDSlotId,
       "starSvcRouteGCIDPortId": starSvcRouteGCIDPortId,
       "starSvcRouteGCIDIfType": starSvcRouteGCIDIfType,
       "starSvcRouteGCIDConnId": starSvcRouteGCIDConnId,
       "starSvcRouteGCIDLeafId": starSvcRouteGCIDLeafId,
       "starSvcRouteHopIndex": starSvcRouteHopIndex,
       "starSvcRouteOutgoingNeId": starSvcRouteOutgoingNeId,
       "starSvcRouteOutgoingNodeType": starSvcRouteOutgoingNodeType,
       "starSvcRouteOutgoingModuleId": starSvcRouteOutgoingModuleId,
       "starSvcRouteOutgoingPortId": starSvcRouteOutgoingPortId,
       "starPVCRouteTable": starPVCRouteTable,
       "starPVCRouteEntry": starPVCRouteEntry,
       "starPvcRouteSrcGCIDNeId": starPvcRouteSrcGCIDNeId,
       "starPvcRouteSrcGCIDSlotId": starPvcRouteSrcGCIDSlotId,
       "starPvcRouteSrcGCIDPortId": starPvcRouteSrcGCIDPortId,
       "starPvcRouteSrcGCIDIfType": starPvcRouteSrcGCIDIfType,
       "starPvcRouteSrcGCIDConnId": starPvcRouteSrcGCIDConnId,
       "starPvcRouteSrcGCIDLeafId": starPvcRouteSrcGCIDLeafId,
       "starPvcRouteAdjacentNeId": starPvcRouteAdjacentNeId,
       "starPvcRouteAdjacentSlotId": starPvcRouteAdjacentSlotId,
       "starPvcRouteAdjacentPortId": starPvcRouteAdjacentPortId,
       "starPvcRouteAdjacentNodeType": starPvcRouteAdjacentNodeType,
       "starPvcRouteLocalNodeType": starPvcRouteLocalNodeType,
       "starPvcRouteLocalIfType": starPvcRouteLocalIfType,
       "starPvcRouteLocalConnId": starPvcRouteLocalConnId,
       "starPvcRouteLocalLeafId": starPvcRouteLocalLeafId,
       "starPvcRouteQueryDescr": starPvcRouteQueryDescr,
       "starBackbone": starBackbone,
       "starBackboneLinkTable": starBackboneLinkTable,
       "starBackboneLinkEntry": starBackboneLinkEntry,
       "starBackboneLinkStatus": starBackboneLinkStatus,
       "starBackboneLinkDestNodeId": starBackboneLinkDestNodeId,
       "starBackboneLinkDestSlotId": starBackboneLinkDestSlotId,
       "starBackboneLinkDestPortId": starBackboneLinkDestPortId,
       "starBackboneLinkIfType": starBackboneLinkIfType,
       "starBackboneLinkConnStatus": starBackboneLinkConnStatus,
       "starTrap": starTrap,
       "starTrapPriority": starTrapPriority,
       "starReturnedErrorCode": starReturnedErrorCode,
       "starCfPSUNum": starCfPSUNum,
       "starCfFANNum": starCfFANNum,
       "starCfSlotActualBoardType": starCfSlotActualBoardType,
       "starCfConfiguredBoardType": starCfConfiguredBoardType,
       "starCfActualFileVersion": starCfActualFileVersion,
       "starCfConfiguredFileVersion": starCfConfiguredFileVersion,
       "starTaskName": starTaskName,
       "starQueueName": starQueueName,
       "starMsgSize": starMsgSize,
       "starFileName": starFileName,
       "starDeviceType": starDeviceType,
       "starModuleIfType": starModuleIfType,
       "starRefClkIndex": starRefClkIndex,
       "starEthernetType": starEthernetType,
       "starDS1ChanIndex": starDS1ChanIndex,
       "starDS2ChanIndex": starDS2ChanIndex,
       "starDeviceId": starDeviceId,
       "starRcvdMsgType": starRcvdMsgType,
       "starReturnedSlotIndex": starReturnedSlotIndex,
       "starRcvdSrcSlotIndex": starRcvdSrcSlotIndex,
       "starRcvdModuleIfType": starRcvdModuleIfType,
       "starFileId": starFileId,
       "starCOSId": starCOSId,
       "starRcvdModuleType": starRcvdModuleType,
       "starRcvdGroupId": starRcvdGroupId,
       "starRcvdSubId": starRcvdSubId,
       "starGcidNeId": starGcidNeId,
       "starGcidSlotIndex": starGcidSlotIndex,
       "starGcidPortIndex": starGcidPortIndex,
       "starGcidModuleIfType": starGcidModuleIfType,
       "starGcidLeafNum": starGcidLeafNum,
       "starGcidConnectionNum": starGcidConnectionNum,
       "starCRSRResultedErrorCode": starCRSRResultedErrorCode,
       "starCRSRFailedSlotIndex": starCRSRFailedSlotIndex,
       "starCRSRFailedPortIndex": starCRSRFailedPortIndex,
       "starCRSRDescriptionCode": starCRSRDescriptionCode,
       "starSwitchReason": starSwitchReason,
       "starBoardFailReason": starBoardFailReason,
       "starCDRGetReason": starCDRGetReason,
       "starCDRFileSplitNum": starCDRFileSplitNum,
       "starPvcmConfFaultCause": starPvcmConfFaultCause,
       "starConnClearCause": starConnClearCause,
       "starRemoteNeId": starRemoteNeId,
       "starRemoteModuleNum": starRemoteModuleNum,
       "starRemotePortIndex": starRemotePortIndex,
       "starFrLmiPortIndex": starFrLmiPortIndex,
       "starQueuePoolId": starQueuePoolId,
       "starRipAddress0": starRipAddress0,
       "starRipAddress1": starRipAddress1,
       "starRipAddress2": starRipAddress2,
       "starRipAddress3": starRipAddress3,
       "starRipAddress4": starRipAddress4,
       "starFatalErrorCode": starFatalErrorCode,
       "starSvcmCacThreshold": starSvcmCacThreshold}
)
