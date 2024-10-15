# SNMP MIB module (EMBEDDED-NGX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMBEDDED-NGX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:22 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sofaware_ObjectIdentity = ObjectIdentity
sofaware = _Sofaware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1)
)
_SwHardware_ObjectIdentity = ObjectIdentity
swHardware = _SwHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 1)
)
_SwHardwareVersion_Type = DisplayString
_SwHardwareVersion_Object = MibScalar
swHardwareVersion = _SwHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 1, 1),
    _SwHardwareVersion_Type()
)
swHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareVersion.setStatus("mandatory")
_SwHardwareType_Type = DisplayString
_SwHardwareType_Object = MibScalar
swHardwareType = _SwHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 1, 2),
    _SwHardwareType_Type()
)
swHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareType.setStatus("mandatory")
_SwStorage_ObjectIdentity = ObjectIdentity
swStorage = _SwStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2)
)
_SwStorageConfig_ObjectIdentity = ObjectIdentity
swStorageConfig = _SwStorageConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2, 1)
)
_SwStorageConfigTotal_Type = Integer32
_SwStorageConfigTotal_Object = MibScalar
swStorageConfigTotal = _SwStorageConfigTotal_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2, 1, 1),
    _SwStorageConfigTotal_Type()
)
swStorageConfigTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStorageConfigTotal.setStatus("mandatory")
_SwStorageConfigFree_Type = Integer32
_SwStorageConfigFree_Object = MibScalar
swStorageConfigFree = _SwStorageConfigFree_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2, 1, 2),
    _SwStorageConfigFree_Type()
)
swStorageConfigFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStorageConfigFree.setStatus("mandatory")
_SwStorageFirm_ObjectIdentity = ObjectIdentity
swStorageFirm = _SwStorageFirm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2, 2)
)
_SwStorageFirmTotal_Type = Integer32
_SwStorageFirmTotal_Object = MibScalar
swStorageFirmTotal = _SwStorageFirmTotal_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2, 2, 1),
    _SwStorageFirmTotal_Type()
)
swStorageFirmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStorageFirmTotal.setStatus("mandatory")
_SwStorageFirmFree_Type = Integer32
_SwStorageFirmFree_Object = MibScalar
swStorageFirmFree = _SwStorageFirmFree_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2, 2, 2),
    _SwStorageFirmFree_Type()
)
swStorageFirmFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStorageFirmFree.setStatus("mandatory")
_SwStorageCF_ObjectIdentity = ObjectIdentity
swStorageCF = _SwStorageCF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2, 3)
)
_SwStorageCFTotal_Type = Integer32
_SwStorageCFTotal_Object = MibScalar
swStorageCFTotal = _SwStorageCFTotal_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2, 3, 1),
    _SwStorageCFTotal_Type()
)
swStorageCFTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStorageCFTotal.setStatus("mandatory")
_SwStorageCFFree_Type = Integer32
_SwStorageCFFree_Object = MibScalar
swStorageCFFree = _SwStorageCFFree_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 2, 3, 2),
    _SwStorageCFFree_Type()
)
swStorageCFFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStorageCFFree.setStatus("mandatory")
_SwLicense_ObjectIdentity = ObjectIdentity
swLicense = _SwLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 3)
)
_SwLicenseMacAddress_Type = DisplayString
_SwLicenseMacAddress_Object = MibScalar
swLicenseMacAddress = _SwLicenseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 3, 1),
    _SwLicenseMacAddress_Type()
)
swLicenseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLicenseMacAddress.setStatus("mandatory")
_SwLicenseProductKey_Type = DisplayString
_SwLicenseProductKey_Object = MibScalar
swLicenseProductKey = _SwLicenseProductKey_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 3, 2),
    _SwLicenseProductKey_Type()
)
swLicenseProductKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLicenseProductKey.setStatus("mandatory")
_SwLicenseProductName_Type = DisplayString
_SwLicenseProductName_Object = MibScalar
swLicenseProductName = _SwLicenseProductName_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 3, 3),
    _SwLicenseProductName_Type()
)
swLicenseProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLicenseProductName.setStatus("mandatory")
_SwLicenseUsedNodes_Type = Integer32
_SwLicenseUsedNodes_Object = MibScalar
swLicenseUsedNodes = _SwLicenseUsedNodes_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 3, 4),
    _SwLicenseUsedNodes_Type()
)
swLicenseUsedNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLicenseUsedNodes.setStatus("mandatory")
_SwFirmware_ObjectIdentity = ObjectIdentity
swFirmware = _SwFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 4)
)
_SwFirmwareRunning_Type = DisplayString
_SwFirmwareRunning_Object = MibScalar
swFirmwareRunning = _SwFirmwareRunning_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 4, 1),
    _SwFirmwareRunning_Type()
)
swFirmwareRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareRunning.setStatus("mandatory")
_SwFirmwarePrimary_Type = DisplayString
_SwFirmwarePrimary_Object = MibScalar
swFirmwarePrimary = _SwFirmwarePrimary_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 4, 2),
    _SwFirmwarePrimary_Type()
)
swFirmwarePrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwarePrimary.setStatus("mandatory")
_SwFirmwareBackup_Type = DisplayString
_SwFirmwareBackup_Object = MibScalar
swFirmwareBackup = _SwFirmwareBackup_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 4, 3),
    _SwFirmwareBackup_Type()
)
swFirmwareBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareBackup.setStatus("mandatory")
_SwFirmwareBootcodeVersion_Type = Integer32
_SwFirmwareBootcodeVersion_Object = MibScalar
swFirmwareBootcodeVersion = _SwFirmwareBootcodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 4, 4),
    _SwFirmwareBootcodeVersion_Type()
)
swFirmwareBootcodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareBootcodeVersion.setStatus("mandatory")
_SwFirmwareDebugMode_Type = DisplayString
_SwFirmwareDebugMode_Object = MibScalar
swFirmwareDebugMode = _SwFirmwareDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 4, 5),
    _SwFirmwareDebugMode_Type()
)
swFirmwareDebugMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareDebugMode.setStatus("mandatory")
_SwMem_ObjectIdentity = ObjectIdentity
swMem = _SwMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5)
)
_SwMemRAM_ObjectIdentity = ObjectIdentity
swMemRAM = _SwMemRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 1)
)
_SwMemRamFree_Type = Integer32
_SwMemRamFree_Object = MibScalar
swMemRamFree = _SwMemRamFree_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 1, 1),
    _SwMemRamFree_Type()
)
swMemRamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemRamFree.setStatus("mandatory")
_SwMemRamTotal_Type = Integer32
_SwMemRamTotal_Object = MibScalar
swMemRamTotal = _SwMemRamTotal_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 1, 2),
    _SwMemRamTotal_Type()
)
swMemRamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemRamTotal.setStatus("mandatory")
_SwMemDFA_ObjectIdentity = ObjectIdentity
swMemDFA = _SwMemDFA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 2)
)
_SwMemDfaFree_Type = Integer32
_SwMemDfaFree_Object = MibScalar
swMemDfaFree = _SwMemDfaFree_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 2, 1),
    _SwMemDfaFree_Type()
)
swMemDfaFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemDfaFree.setStatus("mandatory")
_SwMemDfaTotal_Type = Integer32
_SwMemDfaTotal_Object = MibScalar
swMemDfaTotal = _SwMemDfaTotal_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 2, 2),
    _SwMemDfaTotal_Type()
)
swMemDfaTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemDfaTotal.setStatus("mandatory")
_SwMemDfaTest_Type = DisplayString
_SwMemDfaTest_Object = MibScalar
swMemDfaTest = _SwMemDfaTest_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 2, 3),
    _SwMemDfaTest_Type()
)
swMemDfaTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemDfaTest.setStatus("mandatory")
_SwUserMemFree_Type = Integer32
_SwUserMemFree_Object = MibScalar
swUserMemFree = _SwUserMemFree_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 3),
    _SwUserMemFree_Type()
)
swUserMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUserMemFree.setStatus("mandatory")
_SwKernelMemFree_Type = Integer32
_SwKernelMemFree_Object = MibScalar
swKernelMemFree = _SwKernelMemFree_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 4),
    _SwKernelMemFree_Type()
)
swKernelMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swKernelMemFree.setStatus("mandatory")
_SwFwMEMFree_Type = Integer32
_SwFwMEMFree_Object = MibScalar
swFwMEMFree = _SwFwMEMFree_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 5, 5),
    _SwFwMEMFree_Type()
)
swFwMEMFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwMEMFree.setStatus("mandatory")
_SwAV_ObjectIdentity = ObjectIdentity
swAV = _SwAV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 6)
)
_SwAvMain_Type = DisplayString
_SwAvMain_Object = MibScalar
swAvMain = _SwAvMain_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 6, 1),
    _SwAvMain_Type()
)
swAvMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvMain.setStatus("mandatory")
_SwAvDaily_Type = DisplayString
_SwAvDaily_Object = MibScalar
swAvDaily = _SwAvDaily_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 6, 2),
    _SwAvDaily_Type()
)
swAvDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvDaily.setStatus("mandatory")
_SwAvStatus_Type = DisplayString
_SwAvStatus_Object = MibScalar
swAvStatus = _SwAvStatus_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 6, 3),
    _SwAvStatus_Type()
)
swAvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvStatus.setStatus("mandatory")
_SwAvNextUpdate_Type = DisplayString
_SwAvNextUpdate_Object = MibScalar
swAvNextUpdate = _SwAvNextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 6, 4),
    _SwAvNextUpdate_Type()
)
swAvNextUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAvNextUpdate.setStatus("mandatory")
_SwFW_ObjectIdentity = ObjectIdentity
swFW = _SwFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7)
)
_SwFwActiveComputersTable_Object = MibTable
swFwActiveComputersTable = _SwFwActiveComputersTable_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1)
)
if mibBuilder.loadTexts:
    swFwActiveComputersTable.setStatus("mandatory")
_SwFwActiveComputerEntry_Object = MibTableRow
swFwActiveComputerEntry = _SwFwActiveComputerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1)
)
swFwActiveComputerEntry.setIndexNames(
    (0, "EMBEDDED-NGX-MIB", "swActCompNetwork"),
)
if mibBuilder.loadTexts:
    swFwActiveComputerEntry.setStatus("mandatory")
_SwActCompNetwork_Type = DisplayString
_SwActCompNetwork_Object = MibTableColumn
swActCompNetwork = _SwActCompNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 1),
    _SwActCompNetwork_Type()
)
swActCompNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActCompNetwork.setStatus("mandatory")
_SwActCompIpAddress_Type = DisplayString
_SwActCompIpAddress_Object = MibTableColumn
swActCompIpAddress = _SwActCompIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 2),
    _SwActCompIpAddress_Type()
)
swActCompIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActCompIpAddress.setStatus("mandatory")
_SwActCompMac_Type = DisplayString
_SwActCompMac_Object = MibTableColumn
swActCompMac = _SwActCompMac_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 3),
    _SwActCompMac_Type()
)
swActCompMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActCompMac.setStatus("mandatory")
_SwActCompType_Type = DisplayString
_SwActCompType_Object = MibTableColumn
swActCompType = _SwActCompType_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 4),
    _SwActCompType_Type()
)
swActCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActCompType.setStatus("mandatory")
_SwActCompName_Type = DisplayString
_SwActCompName_Object = MibTableColumn
swActCompName = _SwActCompName_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 5),
    _SwActCompName_Type()
)
swActCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActCompName.setStatus("mandatory")
_SwActCompLicense_Type = DisplayString
_SwActCompLicense_Object = MibTableColumn
swActCompLicense = _SwActCompLicense_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 6),
    _SwActCompLicense_Type()
)
swActCompLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActCompLicense.setStatus("mandatory")
_SwActCompAuthStatus_Type = DisplayString
_SwActCompAuthStatus_Object = MibTableColumn
swActCompAuthStatus = _SwActCompAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 7),
    _SwActCompAuthStatus_Type()
)
swActCompAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActCompAuthStatus.setStatus("mandatory")
_SwActCompAuthUsername_Type = DisplayString
_SwActCompAuthUsername_Object = MibTableColumn
swActCompAuthUsername = _SwActCompAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 8),
    _SwActCompAuthUsername_Type()
)
swActCompAuthUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActCompAuthUsername.setStatus("mandatory")
_SwActCompAuthSessionExpiresTime_Type = DisplayString
_SwActCompAuthSessionExpiresTime_Object = MibTableColumn
swActCompAuthSessionExpiresTime = _SwActCompAuthSessionExpiresTime_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 9),
    _SwActCompAuthSessionExpiresTime_Type()
)
swActCompAuthSessionExpiresTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swActCompAuthSessionExpiresTime.setStatus("mandatory")
_SwWireless_ObjectIdentity = ObjectIdentity
swWireless = _SwWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8)
)
_SwWirelessStationsTable_Object = MibTable
swWirelessStationsTable = _SwWirelessStationsTable_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1)
)
if mibBuilder.loadTexts:
    swWirelessStationsTable.setStatus("mandatory")
_SwWirelessStationEntry_Object = MibTableRow
swWirelessStationEntry = _SwWirelessStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1)
)
swWirelessStationEntry.setIndexNames(
    (0, "EMBEDDED-NGX-MIB", "swWStationMac"),
)
if mibBuilder.loadTexts:
    swWirelessStationEntry.setStatus("mandatory")
_SwWStationMac_Type = DisplayString
_SwWStationMac_Object = MibTableColumn
swWStationMac = _SwWStationMac_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 1),
    _SwWStationMac_Type()
)
swWStationMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationMac.setStatus("mandatory")
_SwWStationSignalDb_Type = Integer32
_SwWStationSignalDb_Object = MibTableColumn
swWStationSignalDb = _SwWStationSignalDb_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 2),
    _SwWStationSignalDb_Type()
)
swWStationSignalDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationSignalDb.setStatus("mandatory")
_SwWStationQos_Type = DisplayString
_SwWStationQos_Object = MibTableColumn
swWStationQos = _SwWStationQos_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 3),
    _SwWStationQos_Type()
)
swWStationQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationQos.setStatus("mandatory")
_SwWStationXr_Type = DisplayString
_SwWStationXr_Object = MibTableColumn
swWStationXr = _SwWStationXr_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 4),
    _SwWStationXr_Type()
)
swWStationXr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationXr.setStatus("mandatory")
_SwWStationRate_Type = DisplayString
_SwWStationRate_Object = MibTableColumn
swWStationRate = _SwWStationRate_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 5),
    _SwWStationRate_Type()
)
swWStationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationRate.setStatus("mandatory")
_SwWStationCipher_Type = DisplayString
_SwWStationCipher_Object = MibTableColumn
swWStationCipher = _SwWStationCipher_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 6),
    _SwWStationCipher_Type()
)
swWStationCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationCipher.setStatus("mandatory")
_SwWStationRxFramesOk_Type = Integer32
_SwWStationRxFramesOk_Object = MibTableColumn
swWStationRxFramesOk = _SwWStationRxFramesOk_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 7),
    _SwWStationRxFramesOk_Type()
)
swWStationRxFramesOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationRxFramesOk.setStatus("mandatory")
_SwWStationRxFramesManagement_Type = Integer32
_SwWStationRxFramesManagement_Object = MibTableColumn
swWStationRxFramesManagement = _SwWStationRxFramesManagement_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 8),
    _SwWStationRxFramesManagement_Type()
)
swWStationRxFramesManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationRxFramesManagement.setStatus("mandatory")
_SwWStationRxFramesControl_Type = Integer32
_SwWStationRxFramesControl_Object = MibTableColumn
swWStationRxFramesControl = _SwWStationRxFramesControl_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 9),
    _SwWStationRxFramesControl_Type()
)
swWStationRxFramesControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationRxFramesControl.setStatus("mandatory")
_SwWStationRxFramesErrorFrame_Type = Integer32
_SwWStationRxFramesErrorFrame_Object = MibTableColumn
swWStationRxFramesErrorFrame = _SwWStationRxFramesErrorFrame_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 10),
    _SwWStationRxFramesErrorFrame_Type()
)
swWStationRxFramesErrorFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationRxFramesErrorFrame.setStatus("mandatory")
_SwWStationRxRetryRation_Type = Integer32
_SwWStationRxRetryRation_Object = MibTableColumn
swWStationRxRetryRation = _SwWStationRxRetryRation_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 11),
    _SwWStationRxRetryRation_Type()
)
swWStationRxRetryRation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationRxRetryRation.setStatus("mandatory")
_SwWStationRxDupRatio_Type = Integer32
_SwWStationRxDupRatio_Object = MibTableColumn
swWStationRxDupRatio = _SwWStationRxDupRatio_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 12),
    _SwWStationRxDupRatio_Type()
)
swWStationRxDupRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationRxDupRatio.setStatus("mandatory")
_SwWStationTxFramesOk_Type = Integer32
_SwWStationTxFramesOk_Object = MibTableColumn
swWStationTxFramesOk = _SwWStationTxFramesOk_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 13),
    _SwWStationTxFramesOk_Type()
)
swWStationTxFramesOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationTxFramesOk.setStatus("mandatory")
_SwWStationTxFramesManagement_Type = Integer32
_SwWStationTxFramesManagement_Object = MibTableColumn
swWStationTxFramesManagement = _SwWStationTxFramesManagement_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 14),
    _SwWStationTxFramesManagement_Type()
)
swWStationTxFramesManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationTxFramesManagement.setStatus("mandatory")
_SwWStationTxFramesError_Type = Integer32
_SwWStationTxFramesError_Object = MibTableColumn
swWStationTxFramesError = _SwWStationTxFramesError_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 15),
    _SwWStationTxFramesError_Type()
)
swWStationTxFramesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationTxFramesError.setStatus("mandatory")
_SwWStationTxFailRatio_Type = Integer32
_SwWStationTxFailRatio_Object = MibTableColumn
swWStationTxFailRatio = _SwWStationTxFailRatio_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 16),
    _SwWStationTxFailRatio_Type()
)
swWStationTxFailRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationTxFailRatio.setStatus("mandatory")
_SwWStationTxPacketErrorRatio_Type = Integer32
_SwWStationTxPacketErrorRatio_Object = MibTableColumn
swWStationTxPacketErrorRatio = _SwWStationTxPacketErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 17),
    _SwWStationTxPacketErrorRatio_Type()
)
swWStationTxPacketErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWStationTxPacketErrorRatio.setStatus("mandatory")
_SwHA_ObjectIdentity = ObjectIdentity
swHA = _SwHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 9)
)
_SwVirtualIpTable_Object = MibTable
swVirtualIpTable = _SwVirtualIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 9, 1)
)
if mibBuilder.loadTexts:
    swVirtualIpTable.setStatus("mandatory")
_SwVirtualIpEntry_Object = MibTableRow
swVirtualIpEntry = _SwVirtualIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 9, 1, 1)
)
swVirtualIpEntry.setIndexNames(
    (0, "EMBEDDED-NGX-MIB", "swVirtualIpAddr"),
)
if mibBuilder.loadTexts:
    swVirtualIpEntry.setStatus("mandatory")
_SwVirtualIpAddr_Type = DisplayString
_SwVirtualIpAddr_Object = MibTableColumn
swVirtualIpAddr = _SwVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 9, 1, 1, 1),
    _SwVirtualIpAddr_Type()
)
swVirtualIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVirtualIpAddr.setStatus("mandatory")
_SwVirtualIpStatus_Type = DisplayString
_SwVirtualIpStatus_Object = MibTableColumn
swVirtualIpStatus = _SwVirtualIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6983, 1, 9, 1, 1, 2),
    _SwVirtualIpStatus_Type()
)
swVirtualIpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVirtualIpStatus.setStatus("mandatory")
_SwGWType_ObjectIdentity = ObjectIdentity
swGWType = _SwGWType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10)
)
_SafeAtOffice205_ObjectIdentity = ObjectIdentity
SafeAtOffice205 = _SafeAtOffice205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 7)
)
_SafeAtOffice210_ObjectIdentity = ObjectIdentity
SafeAtOffice210 = _SafeAtOffice210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 9)
)
_SafeAtOffice225_ObjectIdentity = ObjectIdentity
SafeAtOffice225 = _SafeAtOffice225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 11)
)
_UTM1EdgeX_ObjectIdentity = ObjectIdentity
UTM1EdgeX = _UTM1EdgeX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 15)
)
_SafeAtOffice405_ObjectIdentity = ObjectIdentity
SafeAtOffice405 = _SafeAtOffice405_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 16)
)
_SafeAtOffice410_ObjectIdentity = ObjectIdentity
SafeAtOffice410 = _SafeAtOffice410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 17)
)
_SafeAtOffice425_ObjectIdentity = ObjectIdentity
SafeAtOffice425 = _SafeAtOffice425_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 18)
)
_UTM1EdgeW_ObjectIdentity = ObjectIdentity
UTM1EdgeW = _UTM1EdgeW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 20)
)
_SafeAtOffice500_ObjectIdentity = ObjectIdentity
SafeAtOffice500 = _SafeAtOffice500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 21)
)
_SafeAtOffice500P_ObjectIdentity = ObjectIdentity
SafeAtOffice500P = _SafeAtOffice500P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 22)
)
_UTM_1X300_ObjectIdentity = ObjectIdentity
UTM_1X300 = _UTM_1X300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 23)
)
_UTM_1X400_ObjectIdentity = ObjectIdentity
UTM_1X400 = _UTM_1X400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 24)
)
_UTM_1X1000_ObjectIdentity = ObjectIdentity
UTM_1X1000 = _UTM_1X1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6983, 1, 10, 25)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMBEDDED-NGX-MIB",
    **{"DisplayString": DisplayString,
       "sofaware": sofaware,
       "products": products,
       "swHardware": swHardware,
       "swHardwareVersion": swHardwareVersion,
       "swHardwareType": swHardwareType,
       "swStorage": swStorage,
       "swStorageConfig": swStorageConfig,
       "swStorageConfigTotal": swStorageConfigTotal,
       "swStorageConfigFree": swStorageConfigFree,
       "swStorageFirm": swStorageFirm,
       "swStorageFirmTotal": swStorageFirmTotal,
       "swStorageFirmFree": swStorageFirmFree,
       "swStorageCF": swStorageCF,
       "swStorageCFTotal": swStorageCFTotal,
       "swStorageCFFree": swStorageCFFree,
       "swLicense": swLicense,
       "swLicenseMacAddress": swLicenseMacAddress,
       "swLicenseProductKey": swLicenseProductKey,
       "swLicenseProductName": swLicenseProductName,
       "swLicenseUsedNodes": swLicenseUsedNodes,
       "swFirmware": swFirmware,
       "swFirmwareRunning": swFirmwareRunning,
       "swFirmwarePrimary": swFirmwarePrimary,
       "swFirmwareBackup": swFirmwareBackup,
       "swFirmwareBootcodeVersion": swFirmwareBootcodeVersion,
       "swFirmwareDebugMode": swFirmwareDebugMode,
       "swMem": swMem,
       "swMemRAM": swMemRAM,
       "swMemRamFree": swMemRamFree,
       "swMemRamTotal": swMemRamTotal,
       "swMemDFA": swMemDFA,
       "swMemDfaFree": swMemDfaFree,
       "swMemDfaTotal": swMemDfaTotal,
       "swMemDfaTest": swMemDfaTest,
       "swUserMemFree": swUserMemFree,
       "swKernelMemFree": swKernelMemFree,
       "swFwMEMFree": swFwMEMFree,
       "swAV": swAV,
       "swAvMain": swAvMain,
       "swAvDaily": swAvDaily,
       "swAvStatus": swAvStatus,
       "swAvNextUpdate": swAvNextUpdate,
       "swFW": swFW,
       "swFwActiveComputersTable": swFwActiveComputersTable,
       "swFwActiveComputerEntry": swFwActiveComputerEntry,
       "swActCompNetwork": swActCompNetwork,
       "swActCompIpAddress": swActCompIpAddress,
       "swActCompMac": swActCompMac,
       "swActCompType": swActCompType,
       "swActCompName": swActCompName,
       "swActCompLicense": swActCompLicense,
       "swActCompAuthStatus": swActCompAuthStatus,
       "swActCompAuthUsername": swActCompAuthUsername,
       "swActCompAuthSessionExpiresTime": swActCompAuthSessionExpiresTime,
       "swWireless": swWireless,
       "swWirelessStationsTable": swWirelessStationsTable,
       "swWirelessStationEntry": swWirelessStationEntry,
       "swWStationMac": swWStationMac,
       "swWStationSignalDb": swWStationSignalDb,
       "swWStationQos": swWStationQos,
       "swWStationXr": swWStationXr,
       "swWStationRate": swWStationRate,
       "swWStationCipher": swWStationCipher,
       "swWStationRxFramesOk": swWStationRxFramesOk,
       "swWStationRxFramesManagement": swWStationRxFramesManagement,
       "swWStationRxFramesControl": swWStationRxFramesControl,
       "swWStationRxFramesErrorFrame": swWStationRxFramesErrorFrame,
       "swWStationRxRetryRation": swWStationRxRetryRation,
       "swWStationRxDupRatio": swWStationRxDupRatio,
       "swWStationTxFramesOk": swWStationTxFramesOk,
       "swWStationTxFramesManagement": swWStationTxFramesManagement,
       "swWStationTxFramesError": swWStationTxFramesError,
       "swWStationTxFailRatio": swWStationTxFailRatio,
       "swWStationTxPacketErrorRatio": swWStationTxPacketErrorRatio,
       "swHA": swHA,
       "swVirtualIpTable": swVirtualIpTable,
       "swVirtualIpEntry": swVirtualIpEntry,
       "swVirtualIpAddr": swVirtualIpAddr,
       "swVirtualIpStatus": swVirtualIpStatus,
       "swGWType": swGWType,
       "SafeAtOffice205": SafeAtOffice205,
       "SafeAtOffice210": SafeAtOffice210,
       "SafeAtOffice225": SafeAtOffice225,
       "UTM1EdgeX": UTM1EdgeX,
       "SafeAtOffice405": SafeAtOffice405,
       "SafeAtOffice410": SafeAtOffice410,
       "SafeAtOffice425": SafeAtOffice425,
       "UTM1EdgeW": UTM1EdgeW,
       "SafeAtOffice500": SafeAtOffice500,
       "SafeAtOffice500P": SafeAtOffice500P,
       "UTM-1X300": UTM_1X300,
       "UTM-1X400": UTM_1X400,
       "UTM-1X1000": UTM_1X1000}
)
