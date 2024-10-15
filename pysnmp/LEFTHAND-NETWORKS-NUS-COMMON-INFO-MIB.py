# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:42 2024
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

(lhnNusCommonInfo,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    "lhnNusCommonInfo")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lhnNusCommonInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InfoSerialNumber_Type = OctetString
_InfoSerialNumber_Object = MibScalar
infoSerialNumber = _InfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 1),
    _InfoSerialNumber_Type()
)
infoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSerialNumber.setStatus("current")
_InfoModel_Type = OctetString
_InfoModel_Object = MibScalar
infoModel = _InfoModel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 2),
    _InfoModel_Type()
)
infoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModel.setStatus("current")
_InfoSoftwareVersion_Type = OctetString
_InfoSoftwareVersion_Object = MibScalar
infoSoftwareVersion = _InfoSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 3),
    _InfoSoftwareVersion_Type()
)
infoSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareVersion.setStatus("current")
_InfoDSPFirmwareVersion_Type = OctetString
_InfoDSPFirmwareVersion_Object = MibScalar
infoDSPFirmwareVersion = _InfoDSPFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 4),
    _InfoDSPFirmwareVersion_Type()
)
infoDSPFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDSPFirmwareVersion.setStatus("current")
_InfoMotherboardTemperature_Type = Integer32
_InfoMotherboardTemperature_Object = MibScalar
infoMotherboardTemperature = _InfoMotherboardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 5),
    _InfoMotherboardTemperature_Type()
)
infoMotherboardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoMotherboardTemperature.setStatus("current")
if mibBuilder.loadTexts:
    infoMotherboardTemperature.setUnits("Celsius")
_InfoCPUTemperature_Type = Integer32
_InfoCPUTemperature_Object = MibScalar
infoCPUTemperature = _InfoCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 6),
    _InfoCPUTemperature_Type()
)
infoCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCPUTemperature.setStatus("current")
if mibBuilder.loadTexts:
    infoCPUTemperature.setUnits("Celsius")
_InfoCPUFanSpeed_Type = Integer32
_InfoCPUFanSpeed_Object = MibScalar
infoCPUFanSpeed = _InfoCPUFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 7),
    _InfoCPUFanSpeed_Type()
)
infoCPUFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCPUFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    infoCPUFanSpeed.setUnits("RPM")
_InfoPowerSupplyCount_Type = Integer32
_InfoPowerSupplyCount_Object = MibScalar
infoPowerSupplyCount = _InfoPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 8),
    _InfoPowerSupplyCount_Type()
)
infoPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerSupplyCount.setStatus("current")
_InfoPowerSupplyTable_Object = MibTable
infoPowerSupplyTable = _InfoPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    infoPowerSupplyTable.setStatus("current")
_InfoPowerSupplyEntry_Object = MibTableRow
infoPowerSupplyEntry = _InfoPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 9, 1)
)
infoPowerSupplyEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-INFO-MIB", "infoPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    infoPowerSupplyEntry.setStatus("current")
_InfoPowerSupplyIndex_Type = Integer32
_InfoPowerSupplyIndex_Object = MibTableColumn
infoPowerSupplyIndex = _InfoPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 9, 1, 1),
    _InfoPowerSupplyIndex_Type()
)
infoPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerSupplyIndex.setStatus("current")


class _InfoPowerSupplyStatus_Type(Integer32):
    """Custom type infoPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("marginal", 3))
    )


_InfoPowerSupplyStatus_Type.__name__ = "Integer32"
_InfoPowerSupplyStatus_Object = MibTableColumn
infoPowerSupplyStatus = _InfoPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 9, 1, 2),
    _InfoPowerSupplyStatus_Type()
)
infoPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerSupplyStatus.setStatus("current")
_InfoSFDSCount_Type = Integer32
_InfoSFDSCount_Object = MibScalar
infoSFDSCount = _InfoSFDSCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 10),
    _InfoSFDSCount_Type()
)
infoSFDSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSFDSCount.setStatus("current")
_InfoSFDSTable_Object = MibTable
infoSFDSTable = _InfoSFDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    infoSFDSTable.setStatus("current")
_InfoSFDSEntry_Object = MibTableRow
infoSFDSEntry = _InfoSFDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 11, 1)
)
infoSFDSEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-INFO-MIB", "infoSFDSIndex"),
)
if mibBuilder.loadTexts:
    infoSFDSEntry.setStatus("current")
_InfoSFDSIndex_Type = Integer32
_InfoSFDSIndex_Object = MibTableColumn
infoSFDSIndex = _InfoSFDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 11, 1, 1),
    _InfoSFDSIndex_Type()
)
infoSFDSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSFDSIndex.setStatus("current")
_InfoSFDSHardwareVersion_Type = OctetString
_InfoSFDSHardwareVersion_Object = MibTableColumn
infoSFDSHardwareVersion = _InfoSFDSHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 11, 1, 2),
    _InfoSFDSHardwareVersion_Type()
)
infoSFDSHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSFDSHardwareVersion.setStatus("current")
_InfoSFDSFirmwareVersion_Type = OctetString
_InfoSFDSFirmwareVersion_Object = MibTableColumn
infoSFDSFirmwareVersion = _InfoSFDSFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 11, 1, 3),
    _InfoSFDSFirmwareVersion_Type()
)
infoSFDSFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSFDSFirmwareVersion.setStatus("current")
_InfoSFDSDriverVersion_Type = OctetString
_InfoSFDSDriverVersion_Object = MibTableColumn
infoSFDSDriverVersion = _InfoSFDSDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 11, 1, 4),
    _InfoSFDSDriverVersion_Type()
)
infoSFDSDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSFDSDriverVersion.setStatus("current")
_InfoSFDSMemorySize_Type = Counter32
_InfoSFDSMemorySize_Object = MibTableColumn
infoSFDSMemorySize = _InfoSFDSMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 11, 1, 5),
    _InfoSFDSMemorySize_Type()
)
infoSFDSMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSFDSMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    infoSFDSMemorySize.setUnits("KBytes")
_InfoSFDSStatus_Type = OctetString
_InfoSFDSStatus_Object = MibTableColumn
infoSFDSStatus = _InfoSFDSStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 11, 1, 6),
    _InfoSFDSStatus_Type()
)
infoSFDSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSFDSStatus.setStatus("current")
_InfoDriveCardCount_Type = Integer32
_InfoDriveCardCount_Object = MibScalar
infoDriveCardCount = _InfoDriveCardCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 12),
    _InfoDriveCardCount_Type()
)
infoDriveCardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDriveCardCount.setStatus("current")
_InfoDriveCardTable_Object = MibTable
infoDriveCardTable = _InfoDriveCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 13)
)
if mibBuilder.loadTexts:
    infoDriveCardTable.setStatus("current")
_InfoDriveCardEntry_Object = MibTableRow
infoDriveCardEntry = _InfoDriveCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 13, 1)
)
infoDriveCardEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-INFO-MIB", "infoDriveCardIndex"),
)
if mibBuilder.loadTexts:
    infoDriveCardEntry.setStatus("current")
_InfoDriveCardIndex_Type = Integer32
_InfoDriveCardIndex_Object = MibTableColumn
infoDriveCardIndex = _InfoDriveCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 13, 1, 1),
    _InfoDriveCardIndex_Type()
)
infoDriveCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDriveCardIndex.setStatus("current")
_InfoDriveCardModel_Type = OctetString
_InfoDriveCardModel_Object = MibTableColumn
infoDriveCardModel = _InfoDriveCardModel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 13, 1, 2),
    _InfoDriveCardModel_Type()
)
infoDriveCardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDriveCardModel.setStatus("current")
_InfoDriveCardBiosVersion_Type = OctetString
_InfoDriveCardBiosVersion_Object = MibTableColumn
infoDriveCardBiosVersion = _InfoDriveCardBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 13, 1, 3),
    _InfoDriveCardBiosVersion_Type()
)
infoDriveCardBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDriveCardBiosVersion.setStatus("current")
_InfoDriveCardFirmwareVersion_Type = OctetString
_InfoDriveCardFirmwareVersion_Object = MibTableColumn
infoDriveCardFirmwareVersion = _InfoDriveCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 13, 1, 4),
    _InfoDriveCardFirmwareVersion_Type()
)
infoDriveCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDriveCardFirmwareVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-INFO-MIB",
    **{"lhnNusCommonInfoModule": lhnNusCommonInfoModule,
       "infoSerialNumber": infoSerialNumber,
       "infoModel": infoModel,
       "infoSoftwareVersion": infoSoftwareVersion,
       "infoDSPFirmwareVersion": infoDSPFirmwareVersion,
       "infoMotherboardTemperature": infoMotherboardTemperature,
       "infoCPUTemperature": infoCPUTemperature,
       "infoCPUFanSpeed": infoCPUFanSpeed,
       "infoPowerSupplyCount": infoPowerSupplyCount,
       "infoPowerSupplyTable": infoPowerSupplyTable,
       "infoPowerSupplyEntry": infoPowerSupplyEntry,
       "infoPowerSupplyIndex": infoPowerSupplyIndex,
       "infoPowerSupplyStatus": infoPowerSupplyStatus,
       "infoSFDSCount": infoSFDSCount,
       "infoSFDSTable": infoSFDSTable,
       "infoSFDSEntry": infoSFDSEntry,
       "infoSFDSIndex": infoSFDSIndex,
       "infoSFDSHardwareVersion": infoSFDSHardwareVersion,
       "infoSFDSFirmwareVersion": infoSFDSFirmwareVersion,
       "infoSFDSDriverVersion": infoSFDSDriverVersion,
       "infoSFDSMemorySize": infoSFDSMemorySize,
       "infoSFDSStatus": infoSFDSStatus,
       "infoDriveCardCount": infoDriveCardCount,
       "infoDriveCardTable": infoDriveCardTable,
       "infoDriveCardEntry": infoDriveCardEntry,
       "infoDriveCardIndex": infoDriveCardIndex,
       "infoDriveCardModel": infoDriveCardModel,
       "infoDriveCardBiosVersion": infoDriveCardBiosVersion,
       "infoDriveCardFirmwareVersion": infoDriveCardFirmwareVersion}
)
