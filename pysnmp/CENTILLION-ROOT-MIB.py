# SNMP MIB module (CENTILLION-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:05 2024
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

(Counter32,) = mibBuilder.importSymbols(
    "SNMPv2-SMI-v1",
    "Counter32")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class StatusIndicator(Integer32):
    """Custom type StatusIndicator based on Integer32"""
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





class SsBackplaneType(Integer32):
    """Custom type SsBackplaneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmBus", 2),
          ("other", 1))
    )





class SsChassisType(Integer32):
    """Custom type SsChassisType based on Integer32"""
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
        *(("other", 1),
          ("six-slot", 2),
          ("six-slotBH5005", 7),
          ("three-slotC50N", 5),
          ("three-slotC50T", 6),
          ("twelve-slot", 3),
          ("workgroup", 4))
    )





class SsModuleType(Integer32):
    """Custom type SsModuleType based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("mATM", 5),
          ("mATM1PMMFiber", 47),
          ("mATM1PVNR", 48),
          ("mATM2PC", 21),
          ("mATM2PCopper", 11),
          ("mATM2PSMFiber", 10),
          ("mATM4PC", 22),
          ("mATM4PCopper", 14),
          ("mATM4PMDA", 40),
          ("mATM4PMMFiber", 12),
          ("mATM4PSMFiber", 13),
          ("mATMMCP1PMMFiber", 46),
          ("mATMMCP1PSMFiber", 45),
          ("mATMMCP2PC", 23),
          ("mATMMCP2PCopper", 17),
          ("mATMMCP2PMMFiber", 16),
          ("mATMMCP2PSMFiber", 15),
          ("mATMMCP4PC", 24),
          ("mATMMCP4PCopper", 20),
          ("mATMMCP4PMDA", 41),
          ("mATMMCP4PMMFiber", 19),
          ("mATMMCP4PSMFiber", 18),
          ("mEther10P10BT100BT", 28),
          ("mEther10P10BT100BTMIX", 30),
          ("mEther12PBFL", 32),
          ("mEther14P10BT100BF", 26),
          ("mEther16P10BT100BTCopper", 25),
          ("mEther16P10BT100BTMixed", 29),
          ("mEther16P4x4", 33),
          ("mEther16PC10BT", 8),
          ("mEther24P100BFX", 50),
          ("mEther24P100BFx", 38),
          ("mEther24P10BT100BT", 37),
          ("mEther24P10BT100BTx", 49),
          ("mEther24PC", 36),
          ("mEther4P100BT", 42),
          ("mEther8P10BF", 27),
          ("mEtherMCP8PC10BT", 9),
          ("mTR16PC", 44),
          ("mTR24PC", 43),
          ("mTR4PC", 3),
          ("mTR8PC", 35),
          ("mTR8PFiber", 39),
          ("mTRFiber", 6),
          ("mTRMCP4PC", 4),
          ("mTRMCP8PC", 34),
          ("mTRMCPFiber", 7),
          ("other", 2))
    )





class SsMediaType(Integer32):
    """Custom type SsMediaType based on Integer32"""
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
        *(("mediaATM", 5),
          ("mediaEthernet", 4),
          ("mediaFDDI", 3),
          ("mediaTokenRing", 2),
          ("mediaUnkown", 1))
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class BitField(Integer32):
    """Custom type BitField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 2))
    )





class PortId(Integer32):
    """Custom type PortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class CardId(Integer32):
    """Custom type CardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )





class FailIndicator(Integer32):
    """Custom type FailIndicator based on Integer32"""
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





class EnableIndicator(Integer32):
    """Custom type EnableIndicator based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Centillion_ObjectIdentity = ObjectIdentity
centillion = _Centillion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930)
)
_CnProducts_ObjectIdentity = ObjectIdentity
cnProducts = _CnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 1)
)
_CnCentillion100_ObjectIdentity = ObjectIdentity
cnCentillion100 = _CnCentillion100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 1, 1)
)
_CnIBM8251_ObjectIdentity = ObjectIdentity
cnIBM8251 = _CnIBM8251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 1, 2)
)
_CnBayStack301_ObjectIdentity = ObjectIdentity
cnBayStack301 = _CnBayStack301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 1, 3)
)
_Cn5000BH_MCP_ObjectIdentity = ObjectIdentity
cn5000BH_MCP = _Cn5000BH_MCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 1, 4)
)
_CnCentillion50N_ObjectIdentity = ObjectIdentity
cnCentillion50N = _CnCentillion50N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 1, 5)
)
_CnCentillion50T_ObjectIdentity = ObjectIdentity
cnCentillion50T = _CnCentillion50T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 1, 6)
)
_Cn5005BH_MCP_ObjectIdentity = ObjectIdentity
cn5005BH_MCP = _Cn5005BH_MCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 1, 7)
)
_Proprietary_ObjectIdentity = ObjectIdentity
proprietary = _Proprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2)
)
_CnSystem_ObjectIdentity = ObjectIdentity
cnSystem = _CnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1)
)
_SysChassis_ObjectIdentity = ObjectIdentity
sysChassis = _SysChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1)
)
_ChassisType_Type = SsChassisType
_ChassisType_Object = MibScalar
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 1),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("mandatory")
_ChassisBkplType_Type = SsBackplaneType
_ChassisBkplType_Object = MibScalar
chassisBkplType = _ChassisBkplType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 2),
    _ChassisBkplType_Type()
)
chassisBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisBkplType.setStatus("mandatory")
_ChassisPs1FailStatus_Type = FailIndicator
_ChassisPs1FailStatus_Object = MibScalar
chassisPs1FailStatus = _ChassisPs1FailStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 3),
    _ChassisPs1FailStatus_Type()
)
chassisPs1FailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs1FailStatus.setStatus("mandatory")
_ChassisPs2FailStatus_Type = FailIndicator
_ChassisPs2FailStatus_Object = MibScalar
chassisPs2FailStatus = _ChassisPs2FailStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 4),
    _ChassisPs2FailStatus_Type()
)
chassisPs2FailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs2FailStatus.setStatus("mandatory")
_ChassisFanFailStatus_Type = FailIndicator
_ChassisFanFailStatus_Object = MibScalar
chassisFanFailStatus = _ChassisFanFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 5),
    _ChassisFanFailStatus_Type()
)
chassisFanFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanFailStatus.setStatus("mandatory")


class _ChassisSerialNumber_Type(OctetString):
    """Custom type chassisSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_ChassisSerialNumber_Type.__name__ = "OctetString"
_ChassisSerialNumber_Object = MibScalar
chassisSerialNumber = _ChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 6),
    _ChassisSerialNumber_Type()
)
chassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNumber.setStatus("mandatory")


class _ChassisPartNumber_Type(OctetString):
    """Custom type chassisPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ChassisPartNumber_Type.__name__ = "OctetString"
_ChassisPartNumber_Object = MibScalar
chassisPartNumber = _ChassisPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 7),
    _ChassisPartNumber_Type()
)
chassisPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPartNumber.setStatus("mandatory")
_SlotConfigTable_Object = MibTable
slotConfigTable = _SlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    slotConfigTable.setStatus("mandatory")
_SlotConfigEntry_Object = MibTableRow
slotConfigEntry = _SlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1)
)
slotConfigEntry.setIndexNames(
    (0, "CENTILLION-ROOT-MIB", "slotNumber"),
)
if mibBuilder.loadTexts:
    slotConfigEntry.setStatus("mandatory")
_SlotNumber_Type = Integer32
_SlotNumber_Object = MibTableColumn
slotNumber = _SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 1),
    _SlotNumber_Type()
)
slotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotNumber.setStatus("mandatory")
_SlotModuleType_Type = SsModuleType
_SlotModuleType_Object = MibTableColumn
slotModuleType = _SlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 2),
    _SlotModuleType_Type()
)
slotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleType.setStatus("deprecated")


class _SlotModuleHwVer_Type(OctetString):
    """Custom type slotModuleHwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SlotModuleHwVer_Type.__name__ = "OctetString"
_SlotModuleHwVer_Object = MibTableColumn
slotModuleHwVer = _SlotModuleHwVer_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 3),
    _SlotModuleHwVer_Type()
)
slotModuleHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleHwVer.setStatus("mandatory")


class _SlotModuleSerialNumber_Type(OctetString):
    """Custom type slotModuleSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SlotModuleSerialNumber_Type.__name__ = "OctetString"
_SlotModuleSerialNumber_Object = MibTableColumn
slotModuleSerialNumber = _SlotModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 4),
    _SlotModuleSerialNumber_Type()
)
slotModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleSerialNumber.setStatus("mandatory")
_SlotModuleSwVer_Type = DisplayString
_SlotModuleSwVer_Object = MibTableColumn
slotModuleSwVer = _SlotModuleSwVer_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 5),
    _SlotModuleSwVer_Type()
)
slotModuleSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleSwVer.setStatus("mandatory")


class _SlotModuleStatus_Type(Integer32):
    """Custom type slotModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_SlotModuleStatus_Type.__name__ = "Integer32"
_SlotModuleStatus_Object = MibTableColumn
slotModuleStatus = _SlotModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 6),
    _SlotModuleStatus_Type()
)
slotModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleStatus.setStatus("mandatory")
_SlotModuleLeds_Type = OctetString
_SlotModuleLeds_Object = MibTableColumn
slotModuleLeds = _SlotModuleLeds_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 7),
    _SlotModuleLeds_Type()
)
slotModuleLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleLeds.setStatus("mandatory")


class _SlotModuleReset_Type(Integer32):
    """Custom type slotModuleReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_SlotModuleReset_Type.__name__ = "Integer32"
_SlotModuleReset_Object = MibTableColumn
slotModuleReset = _SlotModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 8),
    _SlotModuleReset_Type()
)
slotModuleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotModuleReset.setStatus("mandatory")
_SlotConfigDelete_Type = Boolean
_SlotConfigDelete_Object = MibTableColumn
slotConfigDelete = _SlotConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 9),
    _SlotConfigDelete_Type()
)
slotConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigDelete.setStatus("mandatory")
_SlotConfigMediaType_Type = SsMediaType
_SlotConfigMediaType_Object = MibTableColumn
slotConfigMediaType = _SlotConfigMediaType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 10),
    _SlotConfigMediaType_Type()
)
slotConfigMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotConfigMediaType.setStatus("mandatory")
_SlotModuleMaxRAM_Type = Integer32
_SlotModuleMaxRAM_Object = MibTableColumn
slotModuleMaxRAM = _SlotModuleMaxRAM_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 11),
    _SlotModuleMaxRAM_Type()
)
slotModuleMaxRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleMaxRAM.setStatus("mandatory")
_SlotModuleInstalledRAM_Type = Integer32
_SlotModuleInstalledRAM_Object = MibTableColumn
slotModuleInstalledRAM = _SlotModuleInstalledRAM_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 12),
    _SlotModuleInstalledRAM_Type()
)
slotModuleInstalledRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleInstalledRAM.setStatus("mandatory")
_SlotModuleFlashSize_Type = Integer32
_SlotModuleFlashSize_Object = MibTableColumn
slotModuleFlashSize = _SlotModuleFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 13),
    _SlotModuleFlashSize_Type()
)
slotModuleFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleFlashSize.setStatus("mandatory")


class _SlotModuleProductImageId_Type(Integer32):
    """Custom type slotModuleProductImageId based on Integer32"""
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
        *(("fullAtmLanEmulation", 4),
          ("minAtmLanEmulation", 3),
          ("noAtmLanEmulation", 2),
          ("notApplicable", 1),
          ("pnnifullAtmLanEmulation", 5))
    )


_SlotModuleProductImageId_Type.__name__ = "Integer32"
_SlotModuleProductImageId_Object = MibTableColumn
slotModuleProductImageId = _SlotModuleProductImageId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 14),
    _SlotModuleProductImageId_Type()
)
slotModuleProductImageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleProductImageId.setStatus("mandatory")
_SlotModuleBaseMacAddress_Type = MacAddress
_SlotModuleBaseMacAddress_Object = MibTableColumn
slotModuleBaseMacAddress = _SlotModuleBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 15),
    _SlotModuleBaseMacAddress_Type()
)
slotModuleBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleBaseMacAddress.setStatus("mandatory")
_SlotLastResetEPC_Type = Counter32
_SlotLastResetEPC_Object = MibTableColumn
slotLastResetEPC = _SlotLastResetEPC_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 16),
    _SlotLastResetEPC_Type()
)
slotLastResetEPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotLastResetEPC.setStatus("mandatory")
_SlotLastResetVirtualAddress_Type = Counter32
_SlotLastResetVirtualAddress_Object = MibTableColumn
slotLastResetVirtualAddress = _SlotLastResetVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 17),
    _SlotLastResetVirtualAddress_Type()
)
slotLastResetVirtualAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotLastResetVirtualAddress.setStatus("mandatory")
_SlotLastResetCause_Type = Counter32
_SlotLastResetCause_Object = MibTableColumn
slotLastResetCause = _SlotLastResetCause_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 18),
    _SlotLastResetCause_Type()
)
slotLastResetCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotLastResetCause.setStatus("mandatory")
_SlotLastResetTimeStamp_Type = Counter32
_SlotLastResetTimeStamp_Object = MibTableColumn
slotLastResetTimeStamp = _SlotLastResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 19),
    _SlotLastResetTimeStamp_Type()
)
slotLastResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotLastResetTimeStamp.setStatus("mandatory")
_SlotConfigAdd_Type = Boolean
_SlotConfigAdd_Object = MibTableColumn
slotConfigAdd = _SlotConfigAdd_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 20),
    _SlotConfigAdd_Type()
)
slotConfigAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigAdd.setStatus("mandatory")


class _SlotConfigExtClockSource_Type(Integer32):
    """Custom type slotConfigExtClockSource based on Integer32"""
    defaultValue = 0


_SlotConfigExtClockSource_Object = MibTableColumn
slotConfigExtClockSource = _SlotConfigExtClockSource_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 21),
    _SlotConfigExtClockSource_Type()
)
slotConfigExtClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigExtClockSource.setStatus("mandatory")
_SlotConfigTrafficShapingRate_Type = Integer32
_SlotConfigTrafficShapingRate_Object = MibTableColumn
slotConfigTrafficShapingRate = _SlotConfigTrafficShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 22),
    _SlotConfigTrafficShapingRate_Type()
)
slotConfigTrafficShapingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConfigTrafficShapingRate.setStatus("mandatory")
_SysConfig_ObjectIdentity = ObjectIdentity
sysConfig = _SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2)
)
_SysMonitor_ObjectIdentity = ObjectIdentity
sysMonitor = _SysMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3)
)
_SysTrap_ObjectIdentity = ObjectIdentity
sysTrap = _SysTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 4)
)
_SysMcpRedundTrap_ObjectIdentity = ObjectIdentity
sysMcpRedundTrap = _SysMcpRedundTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 4, 1)
)
_CnPvcTraps_ObjectIdentity = ObjectIdentity
cnPvcTraps = _CnPvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 4, 2)
)
_SysEvtLogMgmt_ObjectIdentity = ObjectIdentity
sysEvtLogMgmt = _SysEvtLogMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5)
)
_CnATM_ObjectIdentity = ObjectIdentity
cnATM = _CnATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2)
)
_AtmConfig_ObjectIdentity = ObjectIdentity
atmConfig = _AtmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 1)
)
_AtmMonitor_ObjectIdentity = ObjectIdentity
atmMonitor = _AtmMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 2)
)
_AtmLane_ObjectIdentity = ObjectIdentity
atmLane = _AtmLane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3)
)
_AtmSonet_ObjectIdentity = ObjectIdentity
atmSonet = _AtmSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 4)
)
_Extensions_ObjectIdentity = ObjectIdentity
extensions = _Extensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3)
)
_CnTemporary_ObjectIdentity = ObjectIdentity
cnTemporary = _CnTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-ROOT-MIB",
    **{"StatusIndicator": StatusIndicator,
       "SsBackplaneType": SsBackplaneType,
       "SsChassisType": SsChassisType,
       "SsModuleType": SsModuleType,
       "SsMediaType": SsMediaType,
       "MacAddress": MacAddress,
       "Boolean": Boolean,
       "BitField": BitField,
       "PortId": PortId,
       "CardId": CardId,
       "FailIndicator": FailIndicator,
       "EnableIndicator": EnableIndicator,
       "centillion": centillion,
       "cnProducts": cnProducts,
       "cnCentillion100": cnCentillion100,
       "cnIBM8251": cnIBM8251,
       "cnBayStack301": cnBayStack301,
       "cn5000BH-MCP": cn5000BH_MCP,
       "cnCentillion50N": cnCentillion50N,
       "cnCentillion50T": cnCentillion50T,
       "cn5005BH-MCP": cn5005BH_MCP,
       "proprietary": proprietary,
       "cnSystem": cnSystem,
       "sysChassis": sysChassis,
       "chassisType": chassisType,
       "chassisBkplType": chassisBkplType,
       "chassisPs1FailStatus": chassisPs1FailStatus,
       "chassisPs2FailStatus": chassisPs2FailStatus,
       "chassisFanFailStatus": chassisFanFailStatus,
       "chassisSerialNumber": chassisSerialNumber,
       "chassisPartNumber": chassisPartNumber,
       "slotConfigTable": slotConfigTable,
       "slotConfigEntry": slotConfigEntry,
       "slotNumber": slotNumber,
       "slotModuleType": slotModuleType,
       "slotModuleHwVer": slotModuleHwVer,
       "slotModuleSerialNumber": slotModuleSerialNumber,
       "slotModuleSwVer": slotModuleSwVer,
       "slotModuleStatus": slotModuleStatus,
       "slotModuleLeds": slotModuleLeds,
       "slotModuleReset": slotModuleReset,
       "slotConfigDelete": slotConfigDelete,
       "slotConfigMediaType": slotConfigMediaType,
       "slotModuleMaxRAM": slotModuleMaxRAM,
       "slotModuleInstalledRAM": slotModuleInstalledRAM,
       "slotModuleFlashSize": slotModuleFlashSize,
       "slotModuleProductImageId": slotModuleProductImageId,
       "slotModuleBaseMacAddress": slotModuleBaseMacAddress,
       "slotLastResetEPC": slotLastResetEPC,
       "slotLastResetVirtualAddress": slotLastResetVirtualAddress,
       "slotLastResetCause": slotLastResetCause,
       "slotLastResetTimeStamp": slotLastResetTimeStamp,
       "slotConfigAdd": slotConfigAdd,
       "slotConfigExtClockSource": slotConfigExtClockSource,
       "slotConfigTrafficShapingRate": slotConfigTrafficShapingRate,
       "sysConfig": sysConfig,
       "sysMonitor": sysMonitor,
       "sysTrap": sysTrap,
       "sysMcpRedundTrap": sysMcpRedundTrap,
       "cnPvcTraps": cnPvcTraps,
       "sysEvtLogMgmt": sysEvtLogMgmt,
       "cnATM": cnATM,
       "atmConfig": atmConfig,
       "atmMonitor": atmMonitor,
       "atmLane": atmLane,
       "atmSonet": atmSonet,
       "extensions": extensions,
       "cnTemporary": cnTemporary}
)
