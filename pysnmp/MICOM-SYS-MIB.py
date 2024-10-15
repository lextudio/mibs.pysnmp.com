# SNMP MIB module (MICOM-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:36 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

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

_Micom_system_ObjectIdentity = ObjectIdentity
micom_system = _Micom_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1)
)
_Sys_configuration_ObjectIdentity = ObjectIdentity
sys_configuration = _Sys_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1)
)
_McmSysHWTypeGroup_ObjectIdentity = ObjectIdentity
mcmSysHWTypeGroup = _McmSysHWTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 1)
)


class _McmSysHWTypeModelType_Type(DisplayString):
    """Custom type mcmSysHWTypeModelType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_McmSysHWTypeModelType_Type.__name__ = "DisplayString"
_McmSysHWTypeModelType_Object = MibScalar
mcmSysHWTypeModelType = _McmSysHWTypeModelType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 1, 1),
    _McmSysHWTypeModelType_Type()
)
mcmSysHWTypeModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysHWTypeModelType.setStatus("deprecated")
_McmSysHWTypeRevisionLevel_Type = Integer32
_McmSysHWTypeRevisionLevel_Object = MibScalar
mcmSysHWTypeRevisionLevel = _McmSysHWTypeRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 1, 2),
    _McmSysHWTypeRevisionLevel_Type()
)
mcmSysHWTypeRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysHWTypeRevisionLevel.setStatus("mandatory")


class _McmSysHWTypeManufRevDate_Type(DisplayString):
    """Custom type mcmSysHWTypeManufRevDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_McmSysHWTypeManufRevDate_Type.__name__ = "DisplayString"
_McmSysHWTypeManufRevDate_Object = MibScalar
mcmSysHWTypeManufRevDate = _McmSysHWTypeManufRevDate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 1, 3),
    _McmSysHWTypeManufRevDate_Type()
)
mcmSysHWTypeManufRevDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysHWTypeManufRevDate.setStatus("mandatory")


class _McmSysHWTypeSerialNumber_Type(DisplayString):
    """Custom type mcmSysHWTypeSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_McmSysHWTypeSerialNumber_Type.__name__ = "DisplayString"
_McmSysHWTypeSerialNumber_Object = MibScalar
mcmSysHWTypeSerialNumber = _McmSysHWTypeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 1, 4),
    _McmSysHWTypeSerialNumber_Type()
)
mcmSysHWTypeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysHWTypeSerialNumber.setStatus("mandatory")
_McmSysHWTypeModuleID_Type = Integer32
_McmSysHWTypeModuleID_Object = MibScalar
mcmSysHWTypeModuleID = _McmSysHWTypeModuleID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 1, 5),
    _McmSysHWTypeModuleID_Type()
)
mcmSysHWTypeModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysHWTypeModuleID.setStatus("mandatory")


class _McmSysHWTypeMACAddress_Type(OctetString):
    """Custom type mcmSysHWTypeMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_McmSysHWTypeMACAddress_Type.__name__ = "OctetString"
_McmSysHWTypeMACAddress_Object = MibScalar
mcmSysHWTypeMACAddress = _McmSysHWTypeMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 1, 6),
    _McmSysHWTypeMACAddress_Type()
)
mcmSysHWTypeMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysHWTypeMACAddress.setStatus("mandatory")


class _McmSysHWTypeCPUType_Type(DisplayString):
    """Custom type mcmSysHWTypeCPUType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_McmSysHWTypeCPUType_Type.__name__ = "DisplayString"
_McmSysHWTypeCPUType_Object = MibScalar
mcmSysHWTypeCPUType = _McmSysHWTypeCPUType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 1, 7),
    _McmSysHWTypeCPUType_Type()
)
mcmSysHWTypeCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysHWTypeCPUType.setStatus("mandatory")


class _McmSysHWTypeGenCfgType_Type(Integer32):
    """Custom type mcmSysHWTypeGenCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passport4400", 2),
          ("reserved", 1))
    )


_McmSysHWTypeGenCfgType_Type.__name__ = "Integer32"
_McmSysHWTypeGenCfgType_Object = MibScalar
mcmSysHWTypeGenCfgType = _McmSysHWTypeGenCfgType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 1, 8),
    _McmSysHWTypeGenCfgType_Type()
)
mcmSysHWTypeGenCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysHWTypeGenCfgType.setStatus("mandatory")
_McmSysCfgGroup_ObjectIdentity = ObjectIdentity
mcmSysCfgGroup = _McmSysCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2)
)


class _McmSysCfgCPUConfiguration_Type(Integer32):
    """Custom type mcmSysCfgCPUConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("companion040", 2),
          ("companion060", 3))
    )


_McmSysCfgCPUConfiguration_Type.__name__ = "Integer32"
_McmSysCfgCPUConfiguration_Object = MibScalar
mcmSysCfgCPUConfiguration = _McmSysCfgCPUConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2, 1),
    _McmSysCfgCPUConfiguration_Type()
)
mcmSysCfgCPUConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCfgCPUConfiguration.setStatus("mandatory")


class _McmSysCfgPrimaryWANPort_Type(Integer32):
    """Custom type mcmSysCfgPrimaryWANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_McmSysCfgPrimaryWANPort_Type.__name__ = "Integer32"
_McmSysCfgPrimaryWANPort_Object = MibScalar
mcmSysCfgPrimaryWANPort = _McmSysCfgPrimaryWANPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2, 2),
    _McmSysCfgPrimaryWANPort_Type()
)
mcmSysCfgPrimaryWANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCfgPrimaryWANPort.setStatus("mandatory")


class _McmSysCfgPrimaryWANPortPhyMedia_Type(Integer32):
    """Custom type mcmSysCfgPrimaryWANPortPhyMedia based on Integer32"""
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
        *(("generalserial", 4),
          ("isdn", 6),
          ("link56k", 3),
          ("none", 1),
          ("t1e1", 5),
          ("unknown", 2))
    )


_McmSysCfgPrimaryWANPortPhyMedia_Type.__name__ = "Integer32"
_McmSysCfgPrimaryWANPortPhyMedia_Object = MibScalar
mcmSysCfgPrimaryWANPortPhyMedia = _McmSysCfgPrimaryWANPortPhyMedia_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2, 3),
    _McmSysCfgPrimaryWANPortPhyMedia_Type()
)
mcmSysCfgPrimaryWANPortPhyMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCfgPrimaryWANPortPhyMedia.setStatus("mandatory")


class _McmSysCfgDCESerialPortPhyMedia_Type(Integer32):
    """Custom type mcmSysCfgDCESerialPortPhyMedia based on Integer32"""
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
        *(("none", 1),
          ("rs232", 3),
          ("unknown", 2),
          ("v35", 4),
          ("v36", 5),
          ("x21", 6))
    )


_McmSysCfgDCESerialPortPhyMedia_Type.__name__ = "Integer32"
_McmSysCfgDCESerialPortPhyMedia_Object = MibScalar
mcmSysCfgDCESerialPortPhyMedia = _McmSysCfgDCESerialPortPhyMedia_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2, 4),
    _McmSysCfgDCESerialPortPhyMedia_Type()
)
mcmSysCfgDCESerialPortPhyMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCfgDCESerialPortPhyMedia.setStatus("mandatory")


class _McmSysCfgQUICCExpansionModule1_Type(Integer32):
    """Custom type mcmSysCfgQUICCExpansionModule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_McmSysCfgQUICCExpansionModule1_Type.__name__ = "Integer32"
_McmSysCfgQUICCExpansionModule1_Object = MibScalar
mcmSysCfgQUICCExpansionModule1 = _McmSysCfgQUICCExpansionModule1_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2, 5),
    _McmSysCfgQUICCExpansionModule1_Type()
)
mcmSysCfgQUICCExpansionModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCfgQUICCExpansionModule1.setStatus("mandatory")


class _McmSysCfgQUICCExpansionModule2_Type(Integer32):
    """Custom type mcmSysCfgQUICCExpansionModule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_McmSysCfgQUICCExpansionModule2_Type.__name__ = "Integer32"
_McmSysCfgQUICCExpansionModule2_Object = MibScalar
mcmSysCfgQUICCExpansionModule2 = _McmSysCfgQUICCExpansionModule2_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2, 6),
    _McmSysCfgQUICCExpansionModule2_Type()
)
mcmSysCfgQUICCExpansionModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCfgQUICCExpansionModule2.setStatus("mandatory")


class _McmSysCfgFeatureRTCBatteryStatus_Type(Integer32):
    """Custom type mcmSysCfgFeatureRTCBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("batteryLow", 2),
          ("batteryOK", 3),
          ("noBattery", 1))
    )


_McmSysCfgFeatureRTCBatteryStatus_Type.__name__ = "Integer32"
_McmSysCfgFeatureRTCBatteryStatus_Object = MibScalar
mcmSysCfgFeatureRTCBatteryStatus = _McmSysCfgFeatureRTCBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2, 7),
    _McmSysCfgFeatureRTCBatteryStatus_Type()
)
mcmSysCfgFeatureRTCBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCfgFeatureRTCBatteryStatus.setStatus("mandatory")


class _McmSysCfgDRAMSize_Type(Integer32):
    """Custom type mcmSysCfgDRAMSize based on Integer32"""
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
        *(("size16Mbytes", 3),
          ("size32Mbytes", 4),
          ("size4Mbytes", 1),
          ("size64Mbytes", 5),
          ("size8Mbytes", 2))
    )


_McmSysCfgDRAMSize_Type.__name__ = "Integer32"
_McmSysCfgDRAMSize_Object = MibScalar
mcmSysCfgDRAMSize = _McmSysCfgDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2, 8),
    _McmSysCfgDRAMSize_Type()
)
mcmSysCfgDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCfgDRAMSize.setStatus("mandatory")


class _McmSysCfgFlashMemorySize_Type(Integer32):
    """Custom type mcmSysCfgFlashMemorySize based on Integer32"""
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
        *(("size16Mbytes", 3),
          ("size32Mbytes", 4),
          ("size4Mbytes", 1),
          ("size64Mbytes", 5),
          ("size8Mbytes", 2))
    )


_McmSysCfgFlashMemorySize_Type.__name__ = "Integer32"
_McmSysCfgFlashMemorySize_Object = MibScalar
mcmSysCfgFlashMemorySize = _McmSysCfgFlashMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 2, 9),
    _McmSysCfgFlashMemorySize_Type()
)
mcmSysCfgFlashMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCfgFlashMemorySize.setStatus("mandatory")
_McmSysLimTable_Object = MibTable
mcmSysLimTable = _McmSysLimTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mcmSysLimTable.setStatus("mandatory")
_McmSysLimEntry_Object = MibTableRow
mcmSysLimEntry = _McmSysLimEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 3, 1)
)
mcmSysLimEntry.setIndexNames(
    (0, "MICOM-SYS-MIB", "mcmSysLimModuleAddress"),
)
if mibBuilder.loadTexts:
    mcmSysLimEntry.setStatus("mandatory")


class _McmSysLimModuleAddress_Type(Integer32):
    """Custom type mcmSysLimModuleAddress based on Integer32"""
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limA", 1),
          ("limB", 6),
          ("limC", 7),
          ("limD", 8),
          ("limE", 9))
    )


_McmSysLimModuleAddress_Type.__name__ = "Integer32"
_McmSysLimModuleAddress_Object = MibTableColumn
mcmSysLimModuleAddress = _McmSysLimModuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 3, 1, 1),
    _McmSysLimModuleAddress_Type()
)
mcmSysLimModuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLimModuleAddress.setStatus("mandatory")


class _McmSysLimModuleName_Type(DisplayString):
    """Custom type mcmSysLimModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_McmSysLimModuleName_Type.__name__ = "DisplayString"
_McmSysLimModuleName_Object = MibTableColumn
mcmSysLimModuleName = _McmSysLimModuleName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 3, 1, 2),
    _McmSysLimModuleName_Type()
)
mcmSysLimModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLimModuleName.setStatus("mandatory")


class _McmSysLimPcbPartNumber_Type(DisplayString):
    """Custom type mcmSysLimPcbPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_McmSysLimPcbPartNumber_Type.__name__ = "DisplayString"
_McmSysLimPcbPartNumber_Object = MibTableColumn
mcmSysLimPcbPartNumber = _McmSysLimPcbPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 3, 1, 3),
    _McmSysLimPcbPartNumber_Type()
)
mcmSysLimPcbPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLimPcbPartNumber.setStatus("mandatory")


class _McmSysLimPcbRelease_Type(DisplayString):
    """Custom type mcmSysLimPcbRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_McmSysLimPcbRelease_Type.__name__ = "DisplayString"
_McmSysLimPcbRelease_Object = MibTableColumn
mcmSysLimPcbRelease = _McmSysLimPcbRelease_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 3, 1, 4),
    _McmSysLimPcbRelease_Type()
)
mcmSysLimPcbRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLimPcbRelease.setStatus("mandatory")


class _McmSysLimSerialNumber_Type(DisplayString):
    """Custom type mcmSysLimSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_McmSysLimSerialNumber_Type.__name__ = "DisplayString"
_McmSysLimSerialNumber_Object = MibTableColumn
mcmSysLimSerialNumber = _McmSysLimSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 3, 1, 5),
    _McmSysLimSerialNumber_Type()
)
mcmSysLimSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLimSerialNumber.setStatus("mandatory")


class _McmSysLimMfgDate_Type(DisplayString):
    """Custom type mcmSysLimMfgDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_McmSysLimMfgDate_Type.__name__ = "DisplayString"
_McmSysLimMfgDate_Object = MibTableColumn
mcmSysLimMfgDate = _McmSysLimMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 3, 1, 6),
    _McmSysLimMfgDate_Type()
)
mcmSysLimMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLimMfgDate.setStatus("mandatory")
_McmSysChassisGroup_ObjectIdentity = ObjectIdentity
mcmSysChassisGroup = _McmSysChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 4)
)


class _McmSysChassisNumberOfModules_Type(Integer32):
    """Custom type mcmSysChassisNumberOfModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleFive", 2),
          ("moduleThree", 1))
    )


_McmSysChassisNumberOfModules_Type.__name__ = "Integer32"
_McmSysChassisNumberOfModules_Object = MibScalar
mcmSysChassisNumberOfModules = _McmSysChassisNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 4, 1),
    _McmSysChassisNumberOfModules_Type()
)
mcmSysChassisNumberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysChassisNumberOfModules.setStatus("mandatory")


class _McmSysChassisCoolingFan_Type(Integer32):
    """Custom type mcmSysChassisCoolingFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 2),
          ("running", 1))
    )


_McmSysChassisCoolingFan_Type.__name__ = "Integer32"
_McmSysChassisCoolingFan_Object = MibScalar
mcmSysChassisCoolingFan = _McmSysChassisCoolingFan_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 4, 2),
    _McmSysChassisCoolingFan_Type()
)
mcmSysChassisCoolingFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysChassisCoolingFan.setStatus("mandatory")


class _McmSysChassisPowerSupplyType_Type(Integer32):
    """Custom type mcmSysChassisPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type-A", 1),
          ("type-B", 2))
    )


_McmSysChassisPowerSupplyType_Type.__name__ = "Integer32"
_McmSysChassisPowerSupplyType_Object = MibScalar
mcmSysChassisPowerSupplyType = _McmSysChassisPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 4, 3),
    _McmSysChassisPowerSupplyType_Type()
)
mcmSysChassisPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysChassisPowerSupplyType.setStatus("mandatory")


class _McmSysChassisPowerSupplyStatus_Type(Integer32):
    """Custom type mcmSysChassisPowerSupplyStatus based on Integer32"""
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


_McmSysChassisPowerSupplyStatus_Type.__name__ = "Integer32"
_McmSysChassisPowerSupplyStatus_Object = MibScalar
mcmSysChassisPowerSupplyStatus = _McmSysChassisPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 4, 4),
    _McmSysChassisPowerSupplyStatus_Type()
)
mcmSysChassisPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysChassisPowerSupplyStatus.setStatus("mandatory")


class _McmSysChassisPowerSupplyModuleCount_Type(Integer32):
    """Custom type mcmSysChassisPowerSupplyModuleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmSysChassisPowerSupplyModuleCount_Type.__name__ = "Integer32"
_McmSysChassisPowerSupplyModuleCount_Object = MibScalar
mcmSysChassisPowerSupplyModuleCount = _McmSysChassisPowerSupplyModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 4, 5),
    _McmSysChassisPowerSupplyModuleCount_Type()
)
mcmSysChassisPowerSupplyModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysChassisPowerSupplyModuleCount.setStatus("mandatory")


class _McmSysChassisPowerSupplyRedundant_Type(Integer32):
    """Custom type mcmSysChassisPowerSupplyRedundant based on Integer32"""
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


_McmSysChassisPowerSupplyRedundant_Type.__name__ = "Integer32"
_McmSysChassisPowerSupplyRedundant_Object = MibScalar
mcmSysChassisPowerSupplyRedundant = _McmSysChassisPowerSupplyRedundant_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 4, 6),
    _McmSysChassisPowerSupplyRedundant_Type()
)
mcmSysChassisPowerSupplyRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysChassisPowerSupplyRedundant.setStatus("mandatory")
_McmSysTimeOfDayGroup_ObjectIdentity = ObjectIdentity
mcmSysTimeOfDayGroup = _McmSysTimeOfDayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5)
)
_McmSysTimeOfDay_ObjectIdentity = ObjectIdentity
mcmSysTimeOfDay = _McmSysTimeOfDay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5, 1)
)


class _McmSysTimeOfDaySec_Type(Integer32):
    """Custom type mcmSysTimeOfDaySec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_McmSysTimeOfDaySec_Type.__name__ = "Integer32"
_McmSysTimeOfDaySec_Object = MibScalar
mcmSysTimeOfDaySec = _McmSysTimeOfDaySec_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5, 1, 1),
    _McmSysTimeOfDaySec_Type()
)
mcmSysTimeOfDaySec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTimeOfDaySec.setStatus("mandatory")


class _McmSysTimeOfDayMin_Type(Integer32):
    """Custom type mcmSysTimeOfDayMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_McmSysTimeOfDayMin_Type.__name__ = "Integer32"
_McmSysTimeOfDayMin_Object = MibScalar
mcmSysTimeOfDayMin = _McmSysTimeOfDayMin_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5, 1, 2),
    _McmSysTimeOfDayMin_Type()
)
mcmSysTimeOfDayMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTimeOfDayMin.setStatus("mandatory")


class _McmSysTimeOfDayHour_Type(Integer32):
    """Custom type mcmSysTimeOfDayHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_McmSysTimeOfDayHour_Type.__name__ = "Integer32"
_McmSysTimeOfDayHour_Object = MibScalar
mcmSysTimeOfDayHour = _McmSysTimeOfDayHour_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5, 1, 3),
    _McmSysTimeOfDayHour_Type()
)
mcmSysTimeOfDayHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTimeOfDayHour.setStatus("mandatory")


class _McmSysTimeOfDayDay_Type(Integer32):
    """Custom type mcmSysTimeOfDayDay based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_McmSysTimeOfDayDay_Type.__name__ = "Integer32"
_McmSysTimeOfDayDay_Object = MibScalar
mcmSysTimeOfDayDay = _McmSysTimeOfDayDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5, 1, 4),
    _McmSysTimeOfDayDay_Type()
)
mcmSysTimeOfDayDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTimeOfDayDay.setStatus("mandatory")


class _McmSysTimeOfDayDate_Type(Integer32):
    """Custom type mcmSysTimeOfDayDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_McmSysTimeOfDayDate_Type.__name__ = "Integer32"
_McmSysTimeOfDayDate_Object = MibScalar
mcmSysTimeOfDayDate = _McmSysTimeOfDayDate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5, 1, 5),
    _McmSysTimeOfDayDate_Type()
)
mcmSysTimeOfDayDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTimeOfDayDate.setStatus("mandatory")


class _McmSysTimeOfDayMonth_Type(Integer32):
    """Custom type mcmSysTimeOfDayMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_McmSysTimeOfDayMonth_Type.__name__ = "Integer32"
_McmSysTimeOfDayMonth_Object = MibScalar
mcmSysTimeOfDayMonth = _McmSysTimeOfDayMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5, 1, 6),
    _McmSysTimeOfDayMonth_Type()
)
mcmSysTimeOfDayMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTimeOfDayMonth.setStatus("mandatory")


class _McmSysTimeOfDayYear_Type(Integer32):
    """Custom type mcmSysTimeOfDayYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1970, 2070),
    )


_McmSysTimeOfDayYear_Type.__name__ = "Integer32"
_McmSysTimeOfDayYear_Object = MibScalar
mcmSysTimeOfDayYear = _McmSysTimeOfDayYear_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5, 1, 7),
    _McmSysTimeOfDayYear_Type()
)
mcmSysTimeOfDayYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTimeOfDayYear.setStatus("mandatory")


class _McmSysAsciiTimeOfDay_Type(DisplayString):
    """Custom type mcmSysAsciiTimeOfDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 25),
    )


_McmSysAsciiTimeOfDay_Type.__name__ = "DisplayString"
_McmSysAsciiTimeOfDay_Object = MibScalar
mcmSysAsciiTimeOfDay = _McmSysAsciiTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 5, 2),
    _McmSysAsciiTimeOfDay_Type()
)
mcmSysAsciiTimeOfDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysAsciiTimeOfDay.setStatus("mandatory")
_McmSysFirmwareGroup_ObjectIdentity = ObjectIdentity
mcmSysFirmwareGroup = _McmSysFirmwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6)
)


class _McmSysOperationalType_Type(Integer32):
    """Custom type mcmSysOperationalType based on Integer32"""
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
        *(("accessRouter", 1),
          ("accessRouterAndNAS", 2),
          ("backboneRouter", 5),
          ("concentratingRouter", 4),
          ("nmCoreRouter", 3),
          ("other", 6))
    )


_McmSysOperationalType_Type.__name__ = "Integer32"
_McmSysOperationalType_Object = MibScalar
mcmSysOperationalType = _McmSysOperationalType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6, 1),
    _McmSysOperationalType_Type()
)
mcmSysOperationalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysOperationalType.setStatus("mandatory")


class _McmSysFirmwareConfigCommitBank_Type(Integer32):
    """Custom type mcmSysFirmwareConfigCommitBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bank3", 1),
          ("bank4", 2),
          ("none", 3))
    )


_McmSysFirmwareConfigCommitBank_Type.__name__ = "Integer32"
_McmSysFirmwareConfigCommitBank_Object = MibScalar
mcmSysFirmwareConfigCommitBank = _McmSysFirmwareConfigCommitBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6, 2),
    _McmSysFirmwareConfigCommitBank_Type()
)
mcmSysFirmwareConfigCommitBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysFirmwareConfigCommitBank.setStatus("mandatory")


class _McmSysFirmwareConfigSaveBank_Type(Integer32):
    """Custom type mcmSysFirmwareConfigSaveBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bank3", 1),
          ("bank4", 2))
    )


_McmSysFirmwareConfigSaveBank_Type.__name__ = "Integer32"
_McmSysFirmwareConfigSaveBank_Object = MibScalar
mcmSysFirmwareConfigSaveBank = _McmSysFirmwareConfigSaveBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6, 3),
    _McmSysFirmwareConfigSaveBank_Type()
)
mcmSysFirmwareConfigSaveBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysFirmwareConfigSaveBank.setStatus("mandatory")


class _McmSysFirmwareConfigActiveBank_Type(Integer32):
    """Custom type mcmSysFirmwareConfigActiveBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bank3", 1),
          ("bank4", 2),
          ("none", 3))
    )


_McmSysFirmwareConfigActiveBank_Type.__name__ = "Integer32"
_McmSysFirmwareConfigActiveBank_Object = MibScalar
mcmSysFirmwareConfigActiveBank = _McmSysFirmwareConfigActiveBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6, 4),
    _McmSysFirmwareConfigActiveBank_Type()
)
mcmSysFirmwareConfigActiveBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysFirmwareConfigActiveBank.setStatus("mandatory")


class _McmSysFirmwareConfigReadBank_Type(Integer32):
    """Custom type mcmSysFirmwareConfigReadBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bank3", 1),
          ("bank4", 2))
    )


_McmSysFirmwareConfigReadBank_Type.__name__ = "Integer32"
_McmSysFirmwareConfigReadBank_Object = MibScalar
mcmSysFirmwareConfigReadBank = _McmSysFirmwareConfigReadBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6, 5),
    _McmSysFirmwareConfigReadBank_Type()
)
mcmSysFirmwareConfigReadBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareConfigReadBank.setStatus("mandatory")


class _McmSysFirmwareCodeReadBank_Type(Integer32):
    """Custom type mcmSysFirmwareCodeReadBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bank1", 1),
          ("bank2", 2))
    )


_McmSysFirmwareCodeReadBank_Type.__name__ = "Integer32"
_McmSysFirmwareCodeReadBank_Object = MibScalar
mcmSysFirmwareCodeReadBank = _McmSysFirmwareCodeReadBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6, 6),
    _McmSysFirmwareCodeReadBank_Type()
)
mcmSysFirmwareCodeReadBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareCodeReadBank.setStatus("mandatory")


class _McmSysFirmwareCodeCommitBank_Type(Integer32):
    """Custom type mcmSysFirmwareCodeCommitBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bank1", 1),
          ("bank2", 2),
          ("none", 3))
    )


_McmSysFirmwareCodeCommitBank_Type.__name__ = "Integer32"
_McmSysFirmwareCodeCommitBank_Object = MibScalar
mcmSysFirmwareCodeCommitBank = _McmSysFirmwareCodeCommitBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6, 7),
    _McmSysFirmwareCodeCommitBank_Type()
)
mcmSysFirmwareCodeCommitBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysFirmwareCodeCommitBank.setStatus("mandatory")


class _McmSysFirmwareVersion_Type(DisplayString):
    """Custom type mcmSysFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_McmSysFirmwareVersion_Type.__name__ = "DisplayString"
_McmSysFirmwareVersion_Object = MibScalar
mcmSysFirmwareVersion = _McmSysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6, 8),
    _McmSysFirmwareVersion_Type()
)
mcmSysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareVersion.setStatus("mandatory")


class _McmSysFirmwareConfigVersion_Type(DisplayString):
    """Custom type mcmSysFirmwareConfigVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_McmSysFirmwareConfigVersion_Type.__name__ = "DisplayString"
_McmSysFirmwareConfigVersion_Object = MibScalar
mcmSysFirmwareConfigVersion = _McmSysFirmwareConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 6, 9),
    _McmSysFirmwareConfigVersion_Type()
)
mcmSysFirmwareConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareConfigVersion.setStatus("mandatory")
_McmSysFirmwareImageTable_Object = MibTable
mcmSysFirmwareImageTable = _McmSysFirmwareImageTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mcmSysFirmwareImageTable.setStatus("mandatory")
_McmSysFirmwareImageEntry_Object = MibTableRow
mcmSysFirmwareImageEntry = _McmSysFirmwareImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7, 1)
)
mcmSysFirmwareImageEntry.setIndexNames(
    (0, "MICOM-SYS-MIB", "mcmSysFirmwareImageIndex"),
)
if mibBuilder.loadTexts:
    mcmSysFirmwareImageEntry.setStatus("mandatory")
_McmSysFirmwareImageIndex_Type = Integer32
_McmSysFirmwareImageIndex_Object = MibTableColumn
mcmSysFirmwareImageIndex = _McmSysFirmwareImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7, 1, 1),
    _McmSysFirmwareImageIndex_Type()
)
mcmSysFirmwareImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareImageIndex.setStatus("mandatory")


class _McmSysFirmwareImageBank_Type(Integer32):
    """Custom type mcmSysFirmwareImageBank based on Integer32"""
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
        *(("bank0", 1),
          ("bank1", 2),
          ("bank2", 3),
          ("bank3", 4),
          ("bank4", 5))
    )


_McmSysFirmwareImageBank_Type.__name__ = "Integer32"
_McmSysFirmwareImageBank_Object = MibTableColumn
mcmSysFirmwareImageBank = _McmSysFirmwareImageBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7, 1, 2),
    _McmSysFirmwareImageBank_Type()
)
mcmSysFirmwareImageBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareImageBank.setStatus("mandatory")


class _McmSysFirmwareImageSoftware_Type(Integer32):
    """Custom type mcmSysFirmwareImageSoftware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("code", 2),
          ("config", 3))
    )


_McmSysFirmwareImageSoftware_Type.__name__ = "Integer32"
_McmSysFirmwareImageSoftware_Object = MibTableColumn
mcmSysFirmwareImageSoftware = _McmSysFirmwareImageSoftware_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7, 1, 3),
    _McmSysFirmwareImageSoftware_Type()
)
mcmSysFirmwareImageSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareImageSoftware.setStatus("mandatory")


class _McmSysFirmwareImageFilename_Type(DisplayString):
    """Custom type mcmSysFirmwareImageFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_McmSysFirmwareImageFilename_Type.__name__ = "DisplayString"
_McmSysFirmwareImageFilename_Object = MibTableColumn
mcmSysFirmwareImageFilename = _McmSysFirmwareImageFilename_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7, 1, 4),
    _McmSysFirmwareImageFilename_Type()
)
mcmSysFirmwareImageFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareImageFilename.setStatus("mandatory")


class _McmSysFirmwareImageRevision_Type(DisplayString):
    """Custom type mcmSysFirmwareImageRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_McmSysFirmwareImageRevision_Type.__name__ = "DisplayString"
_McmSysFirmwareImageRevision_Object = MibTableColumn
mcmSysFirmwareImageRevision = _McmSysFirmwareImageRevision_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7, 1, 5),
    _McmSysFirmwareImageRevision_Type()
)
mcmSysFirmwareImageRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareImageRevision.setStatus("mandatory")
_McmSysFirmwareImageSize_Type = Integer32
_McmSysFirmwareImageSize_Object = MibTableColumn
mcmSysFirmwareImageSize = _McmSysFirmwareImageSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7, 1, 6),
    _McmSysFirmwareImageSize_Type()
)
mcmSysFirmwareImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareImageSize.setStatus("mandatory")


class _McmSysFirmwareImageCommitStatus_Type(Integer32):
    """Custom type mcmSysFirmwareImageCommitStatus based on Integer32"""
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
        *(("committed", 1),
          ("committedAndActive", 3),
          ("committedAndNotActive", 4),
          ("notCommitted", 2))
    )


_McmSysFirmwareImageCommitStatus_Type.__name__ = "Integer32"
_McmSysFirmwareImageCommitStatus_Object = MibTableColumn
mcmSysFirmwareImageCommitStatus = _McmSysFirmwareImageCommitStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7, 1, 7),
    _McmSysFirmwareImageCommitStatus_Type()
)
mcmSysFirmwareImageCommitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareImageCommitStatus.setStatus("mandatory")
_McmSysFirmwareImageBurnCount_Type = Counter32
_McmSysFirmwareImageBurnCount_Object = MibTableColumn
mcmSysFirmwareImageBurnCount = _McmSysFirmwareImageBurnCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 7, 1, 8),
    _McmSysFirmwareImageBurnCount_Type()
)
mcmSysFirmwareImageBurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysFirmwareImageBurnCount.setStatus("mandatory")
_McmSysSmartCfgGroup_ObjectIdentity = ObjectIdentity
mcmSysSmartCfgGroup = _McmSysSmartCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 8)
)


class _McmSysSmartCfgAction_Type(Integer32):
    """Custom type mcmSysSmartCfgAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_McmSysSmartCfgAction_Type.__name__ = "Integer32"
_McmSysSmartCfgAction_Object = MibScalar
mcmSysSmartCfgAction = _McmSysSmartCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 8, 1),
    _McmSysSmartCfgAction_Type()
)
mcmSysSmartCfgAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmSysSmartCfgAction.setStatus("mandatory")


class _McmSysSmartCfgStatus_Type(Integer32):
    """Custom type mcmSysSmartCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_McmSysSmartCfgStatus_Type.__name__ = "Integer32"
_McmSysSmartCfgStatus_Object = MibScalar
mcmSysSmartCfgStatus = _McmSysSmartCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 8, 2),
    _McmSysSmartCfgStatus_Type()
)
mcmSysSmartCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysSmartCfgStatus.setStatus("mandatory")
_McmSysCommunityStringTable_Object = MibTable
mcmSysCommunityStringTable = _McmSysCommunityStringTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    mcmSysCommunityStringTable.setStatus("mandatory")
_McmSysCommunityStringEntry_Object = MibTableRow
mcmSysCommunityStringEntry = _McmSysCommunityStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 9, 1)
)
mcmSysCommunityStringEntry.setIndexNames(
    (0, "MICOM-SYS-MIB", "mcmSysCommunityStringIndex"),
)
if mibBuilder.loadTexts:
    mcmSysCommunityStringEntry.setStatus("mandatory")


class _McmSysCommunityStringIndex_Type(Integer32):
    """Custom type mcmSysCommunityStringIndex based on Integer32"""
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
        *(("customer-Configurator", 4),
          ("customer-Monitor", 6),
          ("customer-Operator", 5),
          ("nSP-Configurator", 1),
          ("nSP-Monitor", 3),
          ("nSP-Operator", 2))
    )


_McmSysCommunityStringIndex_Type.__name__ = "Integer32"
_McmSysCommunityStringIndex_Object = MibTableColumn
mcmSysCommunityStringIndex = _McmSysCommunityStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 9, 1, 1),
    _McmSysCommunityStringIndex_Type()
)
mcmSysCommunityStringIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysCommunityStringIndex.setStatus("mandatory")


class _McmSysCommunityStringCommunity_Type(DisplayString):
    """Custom type mcmSysCommunityStringCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_McmSysCommunityStringCommunity_Type.__name__ = "DisplayString"
_McmSysCommunityStringCommunity_Object = MibTableColumn
mcmSysCommunityStringCommunity = _McmSysCommunityStringCommunity_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 9, 1, 2),
    _McmSysCommunityStringCommunity_Type()
)
mcmSysCommunityStringCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysCommunityStringCommunity.setStatus("mandatory")
_McmSysValidateCommunityGroup_ObjectIdentity = ObjectIdentity
mcmSysValidateCommunityGroup = _McmSysValidateCommunityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 10)
)


class _McmSysValidateCommunity_Type(DisplayString):
    """Custom type mcmSysValidateCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_McmSysValidateCommunity_Type.__name__ = "DisplayString"
_McmSysValidateCommunity_Object = MibScalar
mcmSysValidateCommunity = _McmSysValidateCommunity_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 10, 1),
    _McmSysValidateCommunity_Type()
)
mcmSysValidateCommunity.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmSysValidateCommunity.setStatus("mandatory")


class _McmSysLastCommunityPriviledgeLevel_Type(Integer32):
    """Custom type mcmSysLastCommunityPriviledgeLevel based on Integer32"""
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
        *(("customerConfigurator", 4),
          ("customerMonitor", 6),
          ("customerOperator", 5),
          ("nspConfigurator", 1),
          ("nspMonitor", 3),
          ("nspOperator", 2))
    )


_McmSysLastCommunityPriviledgeLevel_Type.__name__ = "Integer32"
_McmSysLastCommunityPriviledgeLevel_Object = MibScalar
mcmSysLastCommunityPriviledgeLevel = _McmSysLastCommunityPriviledgeLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 10, 2),
    _McmSysLastCommunityPriviledgeLevel_Type()
)
mcmSysLastCommunityPriviledgeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLastCommunityPriviledgeLevel.setStatus("mandatory")
_McmSysConsolePortGroup_ObjectIdentity = ObjectIdentity
mcmSysConsolePortGroup = _McmSysConsolePortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 11)
)


class _McmSysConsolePortBaudRate_Type(Integer32):
    """Custom type mcmSysConsolePortBaudRate based on Integer32"""
    defaultValue = 3

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
        *(("bps19200", 4),
          ("bps2400", 1),
          ("bps38400", 5),
          ("bps4800", 2),
          ("bps9600", 3))
    )


_McmSysConsolePortBaudRate_Type.__name__ = "Integer32"
_McmSysConsolePortBaudRate_Object = MibScalar
mcmSysConsolePortBaudRate = _McmSysConsolePortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 11, 1),
    _McmSysConsolePortBaudRate_Type()
)
mcmSysConsolePortBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysConsolePortBaudRate.setStatus("mandatory")


class _McmSysConsolePortStopBits_Type(Integer32):
    """Custom type mcmSysConsolePortStopBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_McmSysConsolePortStopBits_Type.__name__ = "Integer32"
_McmSysConsolePortStopBits_Object = MibScalar
mcmSysConsolePortStopBits = _McmSysConsolePortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 11, 2),
    _McmSysConsolePortStopBits_Type()
)
mcmSysConsolePortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysConsolePortStopBits.setStatus("mandatory")


class _McmSysConsolePortDataBits_Type(Integer32):
    """Custom type mcmSysConsolePortDataBits based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_McmSysConsolePortDataBits_Type.__name__ = "Integer32"
_McmSysConsolePortDataBits_Object = MibScalar
mcmSysConsolePortDataBits = _McmSysConsolePortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 11, 3),
    _McmSysConsolePortDataBits_Type()
)
mcmSysConsolePortDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysConsolePortDataBits.setStatus("mandatory")


class _McmSysConsolePortParity_Type(Integer32):
    """Custom type mcmSysConsolePortParity based on Integer32"""
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
        *(("even", 2),
          ("odd", 3),
          ("off", 1))
    )


_McmSysConsolePortParity_Type.__name__ = "Integer32"
_McmSysConsolePortParity_Object = MibScalar
mcmSysConsolePortParity = _McmSysConsolePortParity_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 11, 4),
    _McmSysConsolePortParity_Type()
)
mcmSysConsolePortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysConsolePortParity.setStatus("mandatory")
_McmSysCommitTrackingGroup_ObjectIdentity = ObjectIdentity
mcmSysCommitTrackingGroup = _McmSysCommitTrackingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 12)
)
_McmSysCommitTrackingCounter_Type = Counter32
_McmSysCommitTrackingCounter_Object = MibScalar
mcmSysCommitTrackingCounter = _McmSysCommitTrackingCounter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 12, 1),
    _McmSysCommitTrackingCounter_Type()
)
mcmSysCommitTrackingCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCommitTrackingCounter.setStatus("mandatory")
_McmSysCommitTrackingSrcIPAddressOfLastCommit_Type = IpAddress
_McmSysCommitTrackingSrcIPAddressOfLastCommit_Object = MibScalar
mcmSysCommitTrackingSrcIPAddressOfLastCommit = _McmSysCommitTrackingSrcIPAddressOfLastCommit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 12, 2),
    _McmSysCommitTrackingSrcIPAddressOfLastCommit_Type()
)
mcmSysCommitTrackingSrcIPAddressOfLastCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCommitTrackingSrcIPAddressOfLastCommit.setStatus("mandatory")
_McmSysCommitTrackingCommunityOfLastCommit_Type = DisplayString
_McmSysCommitTrackingCommunityOfLastCommit_Object = MibScalar
mcmSysCommitTrackingCommunityOfLastCommit = _McmSysCommitTrackingCommunityOfLastCommit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 12, 3),
    _McmSysCommitTrackingCommunityOfLastCommit_Type()
)
mcmSysCommitTrackingCommunityOfLastCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCommitTrackingCommunityOfLastCommit.setStatus("mandatory")
_McmSysCommitTrackingTimeOfLastCommit_Type = TimeTicks
_McmSysCommitTrackingTimeOfLastCommit_Object = MibScalar
mcmSysCommitTrackingTimeOfLastCommit = _McmSysCommitTrackingTimeOfLastCommit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 12, 4),
    _McmSysCommitTrackingTimeOfLastCommit_Type()
)
mcmSysCommitTrackingTimeOfLastCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCommitTrackingTimeOfLastCommit.setStatus("mandatory")
_McmSysIfExtTable_Object = MibTable
mcmSysIfExtTable = _McmSysIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    mcmSysIfExtTable.setStatus("mandatory")
_McmSysIfExtEntry_Object = MibTableRow
mcmSysIfExtEntry = _McmSysIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1)
)
mcmSysIfExtEntry.setIndexNames(
    (0, "MICOM-SYS-MIB", "mcmSysIfExtIfIndex"),
)
if mibBuilder.loadTexts:
    mcmSysIfExtEntry.setStatus("mandatory")


class _McmSysIfExtIfIndex_Type(Integer32):
    """Custom type mcmSysIfExtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmSysIfExtIfIndex_Type.__name__ = "Integer32"
_McmSysIfExtIfIndex_Object = MibTableColumn
mcmSysIfExtIfIndex = _McmSysIfExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 1),
    _McmSysIfExtIfIndex_Type()
)
mcmSysIfExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtIfIndex.setStatus("mandatory")


class _McmSysIfExtName_Type(DisplayString):
    """Custom type mcmSysIfExtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_McmSysIfExtName_Type.__name__ = "DisplayString"
_McmSysIfExtName_Object = MibTableColumn
mcmSysIfExtName = _McmSysIfExtName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 2),
    _McmSysIfExtName_Type()
)
mcmSysIfExtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtName.setStatus("mandatory")


class _McmSysIfExtType_Type(Integer32):
    """Custom type mcmSysIfExtType based on Integer32"""
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
              31,
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
              50,
              51,
              52,
              53,
              54,
              63,
              75,
              76,
              77,
              81)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 49),
          ("arcnet", 35),
          ("arcnetPlus", 36),
          ("atm", 37),
          ("basicISDN", 20),
          ("ddnX25", 4),
          ("ds0", 81),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet3Mbit", 26),
          ("ethernetCsmacd", 6),
          ("fddi", 15),
          ("frameRelay", 32),
          ("frameRelayService", 44),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("isdn", 63),
          ("isdns", 75),
          ("isdnu", 76),
          ("iso88022llc", 41),
          ("iso88023Csmacd", 7),
          ("iso88024TokenBus", 8),
          ("iso88025TokenRing", 9),
          ("iso88026Man", 10),
          ("lapb", 16),
          ("lapd", 77),
          ("localTalk", 42),
          ("miox25", 38),
          ("modem", 48),
          ("nsip", 27),
          ("other", 1),
          ("para", 34),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propMultiplexor", 54),
          ("propPointToPointSerial", 22),
          ("propVirtual", 53),
          ("proteon10Mbit", 12),
          ("proteon80Mbit", 13),
          ("regular1822", 2),
          ("rfc877x25", 5),
          ("rs232", 33),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("smdsDxi", 43),
          ("smdsIcip", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonetPath", 50),
          ("sonetVT", 51),
          ("starLan", 11),
          ("ultra", 29),
          ("v35", 45),
          ("x25ple", 40))
    )


_McmSysIfExtType_Type.__name__ = "Integer32"
_McmSysIfExtType_Object = MibTableColumn
mcmSysIfExtType = _McmSysIfExtType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 3),
    _McmSysIfExtType_Type()
)
mcmSysIfExtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtType.setStatus("mandatory")


class _McmSysIfExtLinkUpDownTrapEnable_Type(Integer32):
    """Custom type mcmSysIfExtLinkUpDownTrapEnable based on Integer32"""
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


_McmSysIfExtLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_McmSysIfExtLinkUpDownTrapEnable_Object = MibTableColumn
mcmSysIfExtLinkUpDownTrapEnable = _McmSysIfExtLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 4),
    _McmSysIfExtLinkUpDownTrapEnable_Type()
)
mcmSysIfExtLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysIfExtLinkUpDownTrapEnable.setStatus("mandatory")


class _McmSysIfExtConnectorPresent_Type(Integer32):
    """Custom type mcmSysIfExtConnectorPresent based on Integer32"""
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


_McmSysIfExtConnectorPresent_Type.__name__ = "Integer32"
_McmSysIfExtConnectorPresent_Object = MibTableColumn
mcmSysIfExtConnectorPresent = _McmSysIfExtConnectorPresent_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 5),
    _McmSysIfExtConnectorPresent_Type()
)
mcmSysIfExtConnectorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtConnectorPresent.setStatus("mandatory")


class _McmSysIfExtPersistenceType_Type(Integer32):
    """Custom type mcmSysIfExtPersistenceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-volatile", 2),
          ("volatile", 1))
    )


_McmSysIfExtPersistenceType_Type.__name__ = "Integer32"
_McmSysIfExtPersistenceType_Object = MibTableColumn
mcmSysIfExtPersistenceType = _McmSysIfExtPersistenceType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 6),
    _McmSysIfExtPersistenceType_Type()
)
mcmSysIfExtPersistenceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtPersistenceType.setStatus("mandatory")


class _McmSysIfExtState_Type(Integer32):
    """Custom type mcmSysIfExtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("not-configured", 2))
    )


_McmSysIfExtState_Type.__name__ = "Integer32"
_McmSysIfExtState_Object = MibTableColumn
mcmSysIfExtState = _McmSysIfExtState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 7),
    _McmSysIfExtState_Type()
)
mcmSysIfExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtState.setStatus("mandatory")
_McmSysIfExtPPA_Type = Integer32
_McmSysIfExtPPA_Object = MibTableColumn
mcmSysIfExtPPA = _McmSysIfExtPPA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 8),
    _McmSysIfExtPPA_Type()
)
mcmSysIfExtPPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtPPA.setStatus("mandatory")


class _McmSysIfExtModule_Type(Integer32):
    """Custom type mcmSysIfExtModule based on Integer32"""
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limA", 1),
          ("limB", 6),
          ("limC", 7),
          ("limD", 8),
          ("limE", 9))
    )


_McmSysIfExtModule_Type.__name__ = "Integer32"
_McmSysIfExtModule_Object = MibTableColumn
mcmSysIfExtModule = _McmSysIfExtModule_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 9),
    _McmSysIfExtModule_Type()
)
mcmSysIfExtModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtModule.setStatus("mandatory")
_McmSysIfExtChannel_Type = Integer32
_McmSysIfExtChannel_Object = MibTableColumn
mcmSysIfExtChannel = _McmSysIfExtChannel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 10),
    _McmSysIfExtChannel_Type()
)
mcmSysIfExtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtChannel.setStatus("mandatory")


class _McmSysIfExtPPADeviceType_Type(Integer32):
    """Custom type mcmSysIfExtPPADeviceType based on Integer32"""
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
              31,
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
              46)
        )
    )
    namedValues = NamedValues(
        *(("csu-56k", 34),
          ("csu-e1", 37),
          ("csu-t1", 33),
          ("dataVP", 14),
          ("dce-Conn", 32),
          ("dvmCh", 28),
          ("e1DP1", 25),
          ("e1DP2", 26),
          ("e1Frac", 24),
          ("e1Loc", 23),
          ("e1Net", 22),
          ("ethDriver", 2),
          ("euvmCh", 19),
          ("frDevice-DCE", 29),
          ("frDevice-DTE", 6),
          ("isdn-B1-ch", 8),
          ("isdn-B2-ch", 9),
          ("isdn-BRI", 36),
          ("isdn-D-ch", 10),
          ("isdn-LAPD", 35),
          ("isdn-conn", 11),
          ("iuvmCh", 27),
          ("loopDriver", 3),
          ("nmVP", 13),
          ("noDevice", 5),
          ("nullDevice", 4),
          ("panlDCE", 38),
          ("panlDTE", 39),
          ("serialDevice", 18),
          ("standardFR", 40),
          ("t1DP1", 20),
          ("t1DP2", 21),
          ("t1Frac", 17),
          ("t1Loc", 16),
          ("t1Net", 15),
          ("voice-isdn-B1-ch", 45),
          ("voice-isdn-B2-ch", 46),
          ("voice-isdn-BRI", 42),
          ("voice-isdn-BRI-ch", 41),
          ("voice-isdn-D-ch", 44),
          ("voice-isdn-LAPD", 43),
          ("voiceVP", 12),
          ("wanConn", 7),
          ("wanDriver-FRDCE", 30),
          ("wanDriver-FRDTE", 1),
          ("wanDriver-FRTDS", 31))
    )


_McmSysIfExtPPADeviceType_Type.__name__ = "Integer32"
_McmSysIfExtPPADeviceType_Object = MibTableColumn
mcmSysIfExtPPADeviceType = _McmSysIfExtPPADeviceType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 13, 1, 11),
    _McmSysIfExtPPADeviceType_Type()
)
mcmSysIfExtPPADeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysIfExtPPADeviceType.setStatus("mandatory")
_McmSysRollbackGroup_ObjectIdentity = ObjectIdentity
mcmSysRollbackGroup = _McmSysRollbackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 14)
)


class _McmSysRollbackFeature_Type(Integer32):
    """Custom type mcmSysRollbackFeature based on Integer32"""
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


_McmSysRollbackFeature_Type.__name__ = "Integer32"
_McmSysRollbackFeature_Object = MibScalar
mcmSysRollbackFeature = _McmSysRollbackFeature_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 14, 1),
    _McmSysRollbackFeature_Type()
)
mcmSysRollbackFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysRollbackFeature.setStatus("mandatory")


class _McmSysRollbackStatus_Type(Integer32):
    """Custom type mcmSysRollbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("next-reset", 3),
          ("not-required", 2),
          ("required", 1))
    )


_McmSysRollbackStatus_Type.__name__ = "Integer32"
_McmSysRollbackStatus_Object = MibScalar
mcmSysRollbackStatus = _McmSysRollbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 14, 2),
    _McmSysRollbackStatus_Type()
)
mcmSysRollbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysRollbackStatus.setStatus("mandatory")


class _McmSysRollbackConfirm_Type(Integer32):
    """Custom type mcmSysRollbackConfirm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("confirm", 1)
    )


_McmSysRollbackConfirm_Type.__name__ = "Integer32"
_McmSysRollbackConfirm_Object = MibScalar
mcmSysRollbackConfirm = _McmSysRollbackConfirm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 14, 3),
    _McmSysRollbackConfirm_Type()
)
mcmSysRollbackConfirm.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmSysRollbackConfirm.setStatus("mandatory")
_NvmSysIfExtTable_Object = MibTable
nvmSysIfExtTable = _NvmSysIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15)
)
if mibBuilder.loadTexts:
    nvmSysIfExtTable.setStatus("mandatory")
_NvmSysIfExtEntry_Object = MibTableRow
nvmSysIfExtEntry = _NvmSysIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1)
)
nvmSysIfExtEntry.setIndexNames(
    (0, "MICOM-SYS-MIB", "nvmSysIfExtIfIndex"),
)
if mibBuilder.loadTexts:
    nvmSysIfExtEntry.setStatus("mandatory")


class _NvmSysIfExtIfIndex_Type(Integer32):
    """Custom type nvmSysIfExtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmSysIfExtIfIndex_Type.__name__ = "Integer32"
_NvmSysIfExtIfIndex_Object = MibTableColumn
nvmSysIfExtIfIndex = _NvmSysIfExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 1),
    _NvmSysIfExtIfIndex_Type()
)
nvmSysIfExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtIfIndex.setStatus("mandatory")


class _NvmSysIfExtName_Type(DisplayString):
    """Custom type nvmSysIfExtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_NvmSysIfExtName_Type.__name__ = "DisplayString"
_NvmSysIfExtName_Object = MibTableColumn
nvmSysIfExtName = _NvmSysIfExtName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 2),
    _NvmSysIfExtName_Type()
)
nvmSysIfExtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtName.setStatus("mandatory")


class _NvmSysIfExtType_Type(Integer32):
    """Custom type nvmSysIfExtType based on Integer32"""
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
              31,
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
              50,
              51,
              52,
              53,
              54,
              63,
              75,
              76,
              77,
              81)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 49),
          ("arcnet", 35),
          ("arcnetPlus", 36),
          ("atm", 37),
          ("basicISDN", 20),
          ("ddnX25", 4),
          ("ds0", 81),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet3Mbit", 26),
          ("ethernetCsmacd", 6),
          ("fddi", 15),
          ("frameRelay", 32),
          ("frameRelayService", 44),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("isdn", 63),
          ("isdns", 75),
          ("isdnu", 76),
          ("iso88022llc", 41),
          ("iso88023Csmacd", 7),
          ("iso88024TokenBus", 8),
          ("iso88025TokenRing", 9),
          ("iso88026Man", 10),
          ("lapb", 16),
          ("lapd", 77),
          ("localTalk", 42),
          ("miox25", 38),
          ("modem", 48),
          ("nsip", 27),
          ("other", 1),
          ("para", 34),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propMultiplexor", 54),
          ("propPointToPointSerial", 22),
          ("propVirtual", 53),
          ("proteon10Mbit", 12),
          ("proteon80Mbit", 13),
          ("regular1822", 2),
          ("rfc877x25", 5),
          ("rs232", 33),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("smdsDxi", 43),
          ("smdsIcip", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonetPath", 50),
          ("sonetVT", 51),
          ("starLan", 11),
          ("ultra", 29),
          ("v35", 45),
          ("x25ple", 40))
    )


_NvmSysIfExtType_Type.__name__ = "Integer32"
_NvmSysIfExtType_Object = MibTableColumn
nvmSysIfExtType = _NvmSysIfExtType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 3),
    _NvmSysIfExtType_Type()
)
nvmSysIfExtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtType.setStatus("mandatory")


class _NvmSysIfExtLinkUpDownTrapEnable_Type(Integer32):
    """Custom type nvmSysIfExtLinkUpDownTrapEnable based on Integer32"""
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


_NvmSysIfExtLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_NvmSysIfExtLinkUpDownTrapEnable_Object = MibTableColumn
nvmSysIfExtLinkUpDownTrapEnable = _NvmSysIfExtLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 4),
    _NvmSysIfExtLinkUpDownTrapEnable_Type()
)
nvmSysIfExtLinkUpDownTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtLinkUpDownTrapEnable.setStatus("mandatory")


class _NvmSysIfExtConnectorPresent_Type(Integer32):
    """Custom type nvmSysIfExtConnectorPresent based on Integer32"""
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


_NvmSysIfExtConnectorPresent_Type.__name__ = "Integer32"
_NvmSysIfExtConnectorPresent_Object = MibTableColumn
nvmSysIfExtConnectorPresent = _NvmSysIfExtConnectorPresent_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 5),
    _NvmSysIfExtConnectorPresent_Type()
)
nvmSysIfExtConnectorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtConnectorPresent.setStatus("mandatory")


class _NvmSysIfExtPersistenceType_Type(Integer32):
    """Custom type nvmSysIfExtPersistenceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-volatile", 2),
          ("volatile", 1))
    )


_NvmSysIfExtPersistenceType_Type.__name__ = "Integer32"
_NvmSysIfExtPersistenceType_Object = MibTableColumn
nvmSysIfExtPersistenceType = _NvmSysIfExtPersistenceType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 6),
    _NvmSysIfExtPersistenceType_Type()
)
nvmSysIfExtPersistenceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtPersistenceType.setStatus("mandatory")


class _NvmSysIfExtState_Type(Integer32):
    """Custom type nvmSysIfExtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("not-configured", 2))
    )


_NvmSysIfExtState_Type.__name__ = "Integer32"
_NvmSysIfExtState_Object = MibTableColumn
nvmSysIfExtState = _NvmSysIfExtState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 7),
    _NvmSysIfExtState_Type()
)
nvmSysIfExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtState.setStatus("mandatory")
_NvmSysIfExtPPA_Type = Integer32
_NvmSysIfExtPPA_Object = MibTableColumn
nvmSysIfExtPPA = _NvmSysIfExtPPA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 8),
    _NvmSysIfExtPPA_Type()
)
nvmSysIfExtPPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtPPA.setStatus("mandatory")


class _NvmSysIfExtModule_Type(Integer32):
    """Custom type nvmSysIfExtModule based on Integer32"""
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limA", 1),
          ("limB", 6),
          ("limC", 7),
          ("limD", 8),
          ("limE", 9))
    )


_NvmSysIfExtModule_Type.__name__ = "Integer32"
_NvmSysIfExtModule_Object = MibTableColumn
nvmSysIfExtModule = _NvmSysIfExtModule_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 9),
    _NvmSysIfExtModule_Type()
)
nvmSysIfExtModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtModule.setStatus("mandatory")
_NvmSysIfExtChannel_Type = Integer32
_NvmSysIfExtChannel_Object = MibTableColumn
nvmSysIfExtChannel = _NvmSysIfExtChannel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 10),
    _NvmSysIfExtChannel_Type()
)
nvmSysIfExtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtChannel.setStatus("mandatory")


class _NvmSysIfExtPPADeviceType_Type(Integer32):
    """Custom type nvmSysIfExtPPADeviceType based on Integer32"""
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
              31,
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
              46)
        )
    )
    namedValues = NamedValues(
        *(("csu-56k", 34),
          ("csu-e1", 37),
          ("csu-t1", 33),
          ("dataVP", 14),
          ("dce-Conn", 32),
          ("dvmCh", 28),
          ("e1DP1", 25),
          ("e1DP2", 26),
          ("e1Frac", 24),
          ("e1Loc", 23),
          ("e1Net", 22),
          ("ethDriver", 2),
          ("euvmCh", 19),
          ("frDevice-DCE", 29),
          ("frDevice-DTE", 6),
          ("isdn-B1-ch", 8),
          ("isdn-B2-ch", 9),
          ("isdn-BRI", 36),
          ("isdn-D-ch", 10),
          ("isdn-LAPD", 35),
          ("isdn-conn", 11),
          ("iuvmCh", 27),
          ("loopDriver", 3),
          ("nmVP", 13),
          ("noDevice", 5),
          ("nullDevice", 4),
          ("panlDCE", 38),
          ("panlDTE", 39),
          ("serialDevice", 18),
          ("standardFR", 40),
          ("t1DP1", 20),
          ("t1DP2", 21),
          ("t1Frac", 17),
          ("t1Loc", 16),
          ("t1Net", 15),
          ("voice-isdn-B1-ch", 45),
          ("voice-isdn-B2-ch", 46),
          ("voice-isdn-BRI", 42),
          ("voice-isdn-BRI-ch", 41),
          ("voice-isdn-D-ch", 44),
          ("voice-isdn-LAPD", 43),
          ("voiceVP", 12),
          ("wanConn", 7),
          ("wanDriver-FRDCE", 30),
          ("wanDriver-FRDTE", 1),
          ("wanDriver-FRTDS", 31))
    )


_NvmSysIfExtPPADeviceType_Type.__name__ = "Integer32"
_NvmSysIfExtPPADeviceType_Object = MibTableColumn
nvmSysIfExtPPADeviceType = _NvmSysIfExtPPADeviceType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 15, 1, 11),
    _NvmSysIfExtPPADeviceType_Type()
)
nvmSysIfExtPPADeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmSysIfExtPPADeviceType.setStatus("mandatory")
_McmSysPhysTable_Object = MibTable
mcmSysPhysTable = _McmSysPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 16)
)
if mibBuilder.loadTexts:
    mcmSysPhysTable.setStatus("mandatory")
_McmSysPhysEntry_Object = MibTableRow
mcmSysPhysEntry = _McmSysPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 16, 1)
)
mcmSysPhysEntry.setIndexNames(
    (0, "MICOM-SYS-MIB", "mcmSysPhysModuleAddress"),
)
if mibBuilder.loadTexts:
    mcmSysPhysEntry.setStatus("mandatory")


class _McmSysPhysModuleAddress_Type(Integer32):
    """Custom type mcmSysPhysModuleAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmSysPhysModuleAddress_Type.__name__ = "Integer32"
_McmSysPhysModuleAddress_Object = MibTableColumn
mcmSysPhysModuleAddress = _McmSysPhysModuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 16, 1, 1),
    _McmSysPhysModuleAddress_Type()
)
mcmSysPhysModuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysPhysModuleAddress.setStatus("mandatory")


class _McmSysLogModuleAddress_Type(Integer32):
    """Custom type mcmSysLogModuleAddress based on Integer32"""
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limA", 1),
          ("limB", 6),
          ("limC", 7),
          ("limD", 8),
          ("limE", 9),
          ("none", 10))
    )


_McmSysLogModuleAddress_Type.__name__ = "Integer32"
_McmSysLogModuleAddress_Object = MibTableColumn
mcmSysLogModuleAddress = _McmSysLogModuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 1, 16, 1, 2),
    _McmSysLogModuleAddress_Type()
)
mcmSysLogModuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLogModuleAddress.setStatus("mandatory")
_Sys_control_ObjectIdentity = ObjectIdentity
sys_control = _Sys_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 2)
)
_McmSysResetGroup_ObjectIdentity = ObjectIdentity
mcmSysResetGroup = _McmSysResetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 2, 1)
)


class _McmSysResetAction_Type(Integer32):
    """Custom type mcmSysResetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpu-only", 1),
          ("currentConfig", 2),
          ("factoryDefaults", 3))
    )


_McmSysResetAction_Type.__name__ = "Integer32"
_McmSysResetAction_Object = MibScalar
mcmSysResetAction = _McmSysResetAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 2, 1, 1),
    _McmSysResetAction_Type()
)
mcmSysResetAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmSysResetAction.setStatus("mandatory")


class _McmSysRestartReason_Type(Integer32):
    """Custom type mcmSysRestartReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              41,
              42,
              43,
              48,
              49,
              51,
              52,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("cliCurrentReset", 2),
          ("cliDefaultResetUnknownSWState", 52),
          ("cliResetToDefault", 42),
          ("configDefaultUnknownHWFault", 49),
          ("configDefaultUnknownSWHWState", 59),
          ("cpuResetWithCommittedCOnfig", 43),
          ("doubleBusFault", 6),
          ("hwButtonCurrentReset", 1),
          ("hwButtonDefaultUnknownSWState", 51),
          ("hwButtonOrCLICPUReset", 3),
          ("hwButtonResetToDefault", 41),
          ("noQUICCClock", 5),
          ("powerUp", 8),
          ("powerUpDefaultUnknownSWState", 58),
          ("powerUpWithDefaultedConfig", 48),
          ("switchCodeCLICurrReset", 22),
          ("switchCodeCPUReset", 23),
          ("switchCodeConfigCLICurrReset", 12),
          ("switchCodeConfigCPUReset", 13),
          ("switchCodeConfigHWButtonReset", 11),
          ("switchCodeConfigNoQUICCClock", 15),
          ("switchCodeConfigPowerUp", 18),
          ("switchCodeConfigRollbackTimer", 17),
          ("switchCodeConfigUnknownHWFault", 19),
          ("switchCodeConfigdoubleBusFault", 16),
          ("switchCodeConfigwatchdogTimer", 14),
          ("switchCodeHWButtonReset", 21),
          ("switchCodeNoQUICCClock", 25),
          ("switchCodePowerUp", 28),
          ("switchCodeRollbackTimer", 27),
          ("switchCodeUnknownHWFault", 29),
          ("switchCodedoubleBusFault", 26),
          ("switchCodewatchdogTimer", 24),
          ("switchConfigCLICurrReset", 32),
          ("switchConfigCPUReset", 33),
          ("switchConfigHWButtonReset", 31),
          ("switchConfigNoQUICCClock", 35),
          ("switchConfigPowerUp", 38),
          ("switchConfigRollbackTimer", 37),
          ("switchConfigUnknownHWFault", 39),
          ("switchConfigdoubleBusFault", 36),
          ("switchConfigwatchdogTimer", 34),
          ("unknownHardwareFault", 9),
          ("watchdogTimer", 4))
    )


_McmSysRestartReason_Type.__name__ = "Integer32"
_McmSysRestartReason_Object = MibScalar
mcmSysRestartReason = _McmSysRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 2, 1, 2),
    _McmSysRestartReason_Type()
)
mcmSysRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysRestartReason.setStatus("mandatory")


class _McmSysTimeOfLastReset_Type(DisplayString):
    """Custom type mcmSysTimeOfLastReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 25),
    )


_McmSysTimeOfLastReset_Type.__name__ = "DisplayString"
_McmSysTimeOfLastReset_Object = MibScalar
mcmSysTimeOfLastReset = _McmSysTimeOfLastReset_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 2, 1, 3),
    _McmSysTimeOfLastReset_Type()
)
mcmSysTimeOfLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysTimeOfLastReset.setStatus("mandatory")
_McmSysCfgLockGroup_ObjectIdentity = ObjectIdentity
mcmSysCfgLockGroup = _McmSysCfgLockGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 2, 2)
)


class _McmSysCfgLock_Type(DisplayString):
    """Custom type mcmSysCfgLock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_McmSysCfgLock_Type.__name__ = "DisplayString"
_McmSysCfgLock_Object = MibScalar
mcmSysCfgLock = _McmSysCfgLock_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 2, 2, 1),
    _McmSysCfgLock_Type()
)
mcmSysCfgLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysCfgLock.setStatus("mandatory")
_Sys_statistics_ObjectIdentity = ObjectIdentity
sys_statistics = _Sys_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 3)
)
_McmSysUtilGroup_ObjectIdentity = ObjectIdentity
mcmSysUtilGroup = _McmSysUtilGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 3, 1)
)
_McmSysCpuUtilization_Type = Gauge32
_McmSysCpuUtilization_Object = MibScalar
mcmSysCpuUtilization = _McmSysCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 3, 1, 1),
    _McmSysCpuUtilization_Type()
)
mcmSysCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysCpuUtilization.setStatus("mandatory")
_McmSysLinkTransmitBandwidthUtilization_Type = Gauge32
_McmSysLinkTransmitBandwidthUtilization_Object = MibScalar
mcmSysLinkTransmitBandwidthUtilization = _McmSysLinkTransmitBandwidthUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 3, 1, 2),
    _McmSysLinkTransmitBandwidthUtilization_Type()
)
mcmSysLinkTransmitBandwidthUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLinkTransmitBandwidthUtilization.setStatus("mandatory")
_McmSysInternalRAMUtilization_Type = Gauge32
_McmSysInternalRAMUtilization_Object = MibScalar
mcmSysInternalRAMUtilization = _McmSysInternalRAMUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 3, 1, 3),
    _McmSysInternalRAMUtilization_Type()
)
mcmSysInternalRAMUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysInternalRAMUtilization.setStatus("mandatory")
_McmSysLinkReceiveBandwidthUtilization_Type = Gauge32
_McmSysLinkReceiveBandwidthUtilization_Object = MibScalar
mcmSysLinkReceiveBandwidthUtilization = _McmSysLinkReceiveBandwidthUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 3, 1, 4),
    _McmSysLinkReceiveBandwidthUtilization_Type()
)
mcmSysLinkReceiveBandwidthUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmSysLinkReceiveBandwidthUtilization.setStatus("mandatory")
_Sys_trap_ObjectIdentity = ObjectIdentity
sys_trap = _Sys_trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4)
)
_McmSysTrapSubscriptionTable_Object = MibTable
mcmSysTrapSubscriptionTable = _McmSysTrapSubscriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mcmSysTrapSubscriptionTable.setStatus("mandatory")
_McmSysTrapSubscriptionEntry_Object = MibTableRow
mcmSysTrapSubscriptionEntry = _McmSysTrapSubscriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4, 1, 1)
)
mcmSysTrapSubscriptionEntry.setIndexNames(
    (0, "MICOM-SYS-MIB", "mcmSysTrapSubscriptionIPAddress"),
)
if mibBuilder.loadTexts:
    mcmSysTrapSubscriptionEntry.setStatus("mandatory")
_McmSysTrapSubscriptionIPAddress_Type = IpAddress
_McmSysTrapSubscriptionIPAddress_Object = MibTableColumn
mcmSysTrapSubscriptionIPAddress = _McmSysTrapSubscriptionIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4, 1, 1, 1),
    _McmSysTrapSubscriptionIPAddress_Type()
)
mcmSysTrapSubscriptionIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTrapSubscriptionIPAddress.setStatus("mandatory")
_McmSysTrapSubscriptionCommunityString_Type = DisplayString
_McmSysTrapSubscriptionCommunityString_Object = MibTableColumn
mcmSysTrapSubscriptionCommunityString = _McmSysTrapSubscriptionCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4, 1, 1, 2),
    _McmSysTrapSubscriptionCommunityString_Type()
)
mcmSysTrapSubscriptionCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTrapSubscriptionCommunityString.setStatus("mandatory")


class _McmSysTrapSubscriptionAction_Type(Integer32):
    """Custom type mcmSysTrapSubscriptionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("subscribe", 1))
    )


_McmSysTrapSubscriptionAction_Type.__name__ = "Integer32"
_McmSysTrapSubscriptionAction_Object = MibTableColumn
mcmSysTrapSubscriptionAction = _McmSysTrapSubscriptionAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4, 1, 1, 3),
    _McmSysTrapSubscriptionAction_Type()
)
mcmSysTrapSubscriptionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTrapSubscriptionAction.setStatus("mandatory")
_McmSysTrapThresholdGroup_ObjectIdentity = ObjectIdentity
mcmSysTrapThresholdGroup = _McmSysTrapThresholdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4, 2)
)


class _McmSysTrapCPUUtilThreshold_Type(Integer32):
    """Custom type mcmSysTrapCPUUtilThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_McmSysTrapCPUUtilThreshold_Type.__name__ = "Integer32"
_McmSysTrapCPUUtilThreshold_Object = MibScalar
mcmSysTrapCPUUtilThreshold = _McmSysTrapCPUUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4, 2, 1),
    _McmSysTrapCPUUtilThreshold_Type()
)
mcmSysTrapCPUUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTrapCPUUtilThreshold.setStatus("mandatory")


class _McmSysTrapBandwidthUtilThreshold_Type(Integer32):
    """Custom type mcmSysTrapBandwidthUtilThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_McmSysTrapBandwidthUtilThreshold_Type.__name__ = "Integer32"
_McmSysTrapBandwidthUtilThreshold_Object = MibScalar
mcmSysTrapBandwidthUtilThreshold = _McmSysTrapBandwidthUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4, 2, 2),
    _McmSysTrapBandwidthUtilThreshold_Type()
)
mcmSysTrapBandwidthUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTrapBandwidthUtilThreshold.setStatus("mandatory")


class _McmSysTrapRAMUtilThreshold_Type(Integer32):
    """Custom type mcmSysTrapRAMUtilThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_McmSysTrapRAMUtilThreshold_Type.__name__ = "Integer32"
_McmSysTrapRAMUtilThreshold_Object = MibScalar
mcmSysTrapRAMUtilThreshold = _McmSysTrapRAMUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 4, 2, 3),
    _McmSysTrapRAMUtilThreshold_Type()
)
mcmSysTrapRAMUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmSysTrapRAMUtilThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmSysMainPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 1)
)
mcmSysMainPowerSupplyFailure.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysMainPowerSupplyFailure.setStatus(
        ""
    )

mcmSysChassisFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 2)
)
mcmSysChassisFanFailure.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysChassisFanFailure.setStatus(
        ""
    )

mcmSysSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 3)
)
mcmSysSystemReset.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysSystemReset.setStatus(
        ""
    )

mcmSysBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 4)
)
mcmSysBatteryLow.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysBatteryLow.setStatus(
        ""
    )

mcmSysConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 5)
)
mcmSysConfigChanged.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysConfigChanged.setStatus(
        ""
    )

mcmSysCPUUtilExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 6)
)
mcmSysCPUUtilExceeded.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysCPUUtilExceeded.setStatus(
        ""
    )

mcmSysBandwidthUtilExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 7)
)
mcmSysBandwidthUtilExceeded.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysBandwidthUtilExceeded.setStatus(
        ""
    )

mcmSysRAMUtilExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 8)
)
mcmSysRAMUtilExceeded.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysRAMUtilExceeded.setStatus(
        ""
    )

mcmSysRollbackEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 9)
)
mcmSysRollbackEnabled.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysRollbackEnabled.setStatus(
        ""
    )

mcmSysRollbackDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 10)
)
mcmSysRollbackDisabled.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysRollbackDisabled.setStatus(
        ""
    )

mcmSysRollbackArmed = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 11)
)
mcmSysRollbackArmed.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysRollbackArmed.setStatus(
        ""
    )

mcmSysRollbackDisarmed = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 1, 0, 12)
)
mcmSysRollbackDisarmed.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmSysRollbackDisarmed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-SYS-MIB",
    **{"micom-system": micom_system,
       "mcmSysMainPowerSupplyFailure": mcmSysMainPowerSupplyFailure,
       "mcmSysChassisFanFailure": mcmSysChassisFanFailure,
       "mcmSysSystemReset": mcmSysSystemReset,
       "mcmSysBatteryLow": mcmSysBatteryLow,
       "mcmSysConfigChanged": mcmSysConfigChanged,
       "mcmSysCPUUtilExceeded": mcmSysCPUUtilExceeded,
       "mcmSysBandwidthUtilExceeded": mcmSysBandwidthUtilExceeded,
       "mcmSysRAMUtilExceeded": mcmSysRAMUtilExceeded,
       "mcmSysRollbackEnabled": mcmSysRollbackEnabled,
       "mcmSysRollbackDisabled": mcmSysRollbackDisabled,
       "mcmSysRollbackArmed": mcmSysRollbackArmed,
       "mcmSysRollbackDisarmed": mcmSysRollbackDisarmed,
       "sys-configuration": sys_configuration,
       "mcmSysHWTypeGroup": mcmSysHWTypeGroup,
       "mcmSysHWTypeModelType": mcmSysHWTypeModelType,
       "mcmSysHWTypeRevisionLevel": mcmSysHWTypeRevisionLevel,
       "mcmSysHWTypeManufRevDate": mcmSysHWTypeManufRevDate,
       "mcmSysHWTypeSerialNumber": mcmSysHWTypeSerialNumber,
       "mcmSysHWTypeModuleID": mcmSysHWTypeModuleID,
       "mcmSysHWTypeMACAddress": mcmSysHWTypeMACAddress,
       "mcmSysHWTypeCPUType": mcmSysHWTypeCPUType,
       "mcmSysHWTypeGenCfgType": mcmSysHWTypeGenCfgType,
       "mcmSysCfgGroup": mcmSysCfgGroup,
       "mcmSysCfgCPUConfiguration": mcmSysCfgCPUConfiguration,
       "mcmSysCfgPrimaryWANPort": mcmSysCfgPrimaryWANPort,
       "mcmSysCfgPrimaryWANPortPhyMedia": mcmSysCfgPrimaryWANPortPhyMedia,
       "mcmSysCfgDCESerialPortPhyMedia": mcmSysCfgDCESerialPortPhyMedia,
       "mcmSysCfgQUICCExpansionModule1": mcmSysCfgQUICCExpansionModule1,
       "mcmSysCfgQUICCExpansionModule2": mcmSysCfgQUICCExpansionModule2,
       "mcmSysCfgFeatureRTCBatteryStatus": mcmSysCfgFeatureRTCBatteryStatus,
       "mcmSysCfgDRAMSize": mcmSysCfgDRAMSize,
       "mcmSysCfgFlashMemorySize": mcmSysCfgFlashMemorySize,
       "mcmSysLimTable": mcmSysLimTable,
       "mcmSysLimEntry": mcmSysLimEntry,
       "mcmSysLimModuleAddress": mcmSysLimModuleAddress,
       "mcmSysLimModuleName": mcmSysLimModuleName,
       "mcmSysLimPcbPartNumber": mcmSysLimPcbPartNumber,
       "mcmSysLimPcbRelease": mcmSysLimPcbRelease,
       "mcmSysLimSerialNumber": mcmSysLimSerialNumber,
       "mcmSysLimMfgDate": mcmSysLimMfgDate,
       "mcmSysChassisGroup": mcmSysChassisGroup,
       "mcmSysChassisNumberOfModules": mcmSysChassisNumberOfModules,
       "mcmSysChassisCoolingFan": mcmSysChassisCoolingFan,
       "mcmSysChassisPowerSupplyType": mcmSysChassisPowerSupplyType,
       "mcmSysChassisPowerSupplyStatus": mcmSysChassisPowerSupplyStatus,
       "mcmSysChassisPowerSupplyModuleCount": mcmSysChassisPowerSupplyModuleCount,
       "mcmSysChassisPowerSupplyRedundant": mcmSysChassisPowerSupplyRedundant,
       "mcmSysTimeOfDayGroup": mcmSysTimeOfDayGroup,
       "mcmSysTimeOfDay": mcmSysTimeOfDay,
       "mcmSysTimeOfDaySec": mcmSysTimeOfDaySec,
       "mcmSysTimeOfDayMin": mcmSysTimeOfDayMin,
       "mcmSysTimeOfDayHour": mcmSysTimeOfDayHour,
       "mcmSysTimeOfDayDay": mcmSysTimeOfDayDay,
       "mcmSysTimeOfDayDate": mcmSysTimeOfDayDate,
       "mcmSysTimeOfDayMonth": mcmSysTimeOfDayMonth,
       "mcmSysTimeOfDayYear": mcmSysTimeOfDayYear,
       "mcmSysAsciiTimeOfDay": mcmSysAsciiTimeOfDay,
       "mcmSysFirmwareGroup": mcmSysFirmwareGroup,
       "mcmSysOperationalType": mcmSysOperationalType,
       "mcmSysFirmwareConfigCommitBank": mcmSysFirmwareConfigCommitBank,
       "mcmSysFirmwareConfigSaveBank": mcmSysFirmwareConfigSaveBank,
       "mcmSysFirmwareConfigActiveBank": mcmSysFirmwareConfigActiveBank,
       "mcmSysFirmwareConfigReadBank": mcmSysFirmwareConfigReadBank,
       "mcmSysFirmwareCodeReadBank": mcmSysFirmwareCodeReadBank,
       "mcmSysFirmwareCodeCommitBank": mcmSysFirmwareCodeCommitBank,
       "mcmSysFirmwareVersion": mcmSysFirmwareVersion,
       "mcmSysFirmwareConfigVersion": mcmSysFirmwareConfigVersion,
       "mcmSysFirmwareImageTable": mcmSysFirmwareImageTable,
       "mcmSysFirmwareImageEntry": mcmSysFirmwareImageEntry,
       "mcmSysFirmwareImageIndex": mcmSysFirmwareImageIndex,
       "mcmSysFirmwareImageBank": mcmSysFirmwareImageBank,
       "mcmSysFirmwareImageSoftware": mcmSysFirmwareImageSoftware,
       "mcmSysFirmwareImageFilename": mcmSysFirmwareImageFilename,
       "mcmSysFirmwareImageRevision": mcmSysFirmwareImageRevision,
       "mcmSysFirmwareImageSize": mcmSysFirmwareImageSize,
       "mcmSysFirmwareImageCommitStatus": mcmSysFirmwareImageCommitStatus,
       "mcmSysFirmwareImageBurnCount": mcmSysFirmwareImageBurnCount,
       "mcmSysSmartCfgGroup": mcmSysSmartCfgGroup,
       "mcmSysSmartCfgAction": mcmSysSmartCfgAction,
       "mcmSysSmartCfgStatus": mcmSysSmartCfgStatus,
       "mcmSysCommunityStringTable": mcmSysCommunityStringTable,
       "mcmSysCommunityStringEntry": mcmSysCommunityStringEntry,
       "mcmSysCommunityStringIndex": mcmSysCommunityStringIndex,
       "mcmSysCommunityStringCommunity": mcmSysCommunityStringCommunity,
       "mcmSysValidateCommunityGroup": mcmSysValidateCommunityGroup,
       "mcmSysValidateCommunity": mcmSysValidateCommunity,
       "mcmSysLastCommunityPriviledgeLevel": mcmSysLastCommunityPriviledgeLevel,
       "mcmSysConsolePortGroup": mcmSysConsolePortGroup,
       "mcmSysConsolePortBaudRate": mcmSysConsolePortBaudRate,
       "mcmSysConsolePortStopBits": mcmSysConsolePortStopBits,
       "mcmSysConsolePortDataBits": mcmSysConsolePortDataBits,
       "mcmSysConsolePortParity": mcmSysConsolePortParity,
       "mcmSysCommitTrackingGroup": mcmSysCommitTrackingGroup,
       "mcmSysCommitTrackingCounter": mcmSysCommitTrackingCounter,
       "mcmSysCommitTrackingSrcIPAddressOfLastCommit": mcmSysCommitTrackingSrcIPAddressOfLastCommit,
       "mcmSysCommitTrackingCommunityOfLastCommit": mcmSysCommitTrackingCommunityOfLastCommit,
       "mcmSysCommitTrackingTimeOfLastCommit": mcmSysCommitTrackingTimeOfLastCommit,
       "mcmSysIfExtTable": mcmSysIfExtTable,
       "mcmSysIfExtEntry": mcmSysIfExtEntry,
       "mcmSysIfExtIfIndex": mcmSysIfExtIfIndex,
       "mcmSysIfExtName": mcmSysIfExtName,
       "mcmSysIfExtType": mcmSysIfExtType,
       "mcmSysIfExtLinkUpDownTrapEnable": mcmSysIfExtLinkUpDownTrapEnable,
       "mcmSysIfExtConnectorPresent": mcmSysIfExtConnectorPresent,
       "mcmSysIfExtPersistenceType": mcmSysIfExtPersistenceType,
       "mcmSysIfExtState": mcmSysIfExtState,
       "mcmSysIfExtPPA": mcmSysIfExtPPA,
       "mcmSysIfExtModule": mcmSysIfExtModule,
       "mcmSysIfExtChannel": mcmSysIfExtChannel,
       "mcmSysIfExtPPADeviceType": mcmSysIfExtPPADeviceType,
       "mcmSysRollbackGroup": mcmSysRollbackGroup,
       "mcmSysRollbackFeature": mcmSysRollbackFeature,
       "mcmSysRollbackStatus": mcmSysRollbackStatus,
       "mcmSysRollbackConfirm": mcmSysRollbackConfirm,
       "nvmSysIfExtTable": nvmSysIfExtTable,
       "nvmSysIfExtEntry": nvmSysIfExtEntry,
       "nvmSysIfExtIfIndex": nvmSysIfExtIfIndex,
       "nvmSysIfExtName": nvmSysIfExtName,
       "nvmSysIfExtType": nvmSysIfExtType,
       "nvmSysIfExtLinkUpDownTrapEnable": nvmSysIfExtLinkUpDownTrapEnable,
       "nvmSysIfExtConnectorPresent": nvmSysIfExtConnectorPresent,
       "nvmSysIfExtPersistenceType": nvmSysIfExtPersistenceType,
       "nvmSysIfExtState": nvmSysIfExtState,
       "nvmSysIfExtPPA": nvmSysIfExtPPA,
       "nvmSysIfExtModule": nvmSysIfExtModule,
       "nvmSysIfExtChannel": nvmSysIfExtChannel,
       "nvmSysIfExtPPADeviceType": nvmSysIfExtPPADeviceType,
       "mcmSysPhysTable": mcmSysPhysTable,
       "mcmSysPhysEntry": mcmSysPhysEntry,
       "mcmSysPhysModuleAddress": mcmSysPhysModuleAddress,
       "mcmSysLogModuleAddress": mcmSysLogModuleAddress,
       "sys-control": sys_control,
       "mcmSysResetGroup": mcmSysResetGroup,
       "mcmSysResetAction": mcmSysResetAction,
       "mcmSysRestartReason": mcmSysRestartReason,
       "mcmSysTimeOfLastReset": mcmSysTimeOfLastReset,
       "mcmSysCfgLockGroup": mcmSysCfgLockGroup,
       "mcmSysCfgLock": mcmSysCfgLock,
       "sys-statistics": sys_statistics,
       "mcmSysUtilGroup": mcmSysUtilGroup,
       "mcmSysCpuUtilization": mcmSysCpuUtilization,
       "mcmSysLinkTransmitBandwidthUtilization": mcmSysLinkTransmitBandwidthUtilization,
       "mcmSysInternalRAMUtilization": mcmSysInternalRAMUtilization,
       "mcmSysLinkReceiveBandwidthUtilization": mcmSysLinkReceiveBandwidthUtilization,
       "sys-trap": sys_trap,
       "mcmSysTrapSubscriptionTable": mcmSysTrapSubscriptionTable,
       "mcmSysTrapSubscriptionEntry": mcmSysTrapSubscriptionEntry,
       "mcmSysTrapSubscriptionIPAddress": mcmSysTrapSubscriptionIPAddress,
       "mcmSysTrapSubscriptionCommunityString": mcmSysTrapSubscriptionCommunityString,
       "mcmSysTrapSubscriptionAction": mcmSysTrapSubscriptionAction,
       "mcmSysTrapThresholdGroup": mcmSysTrapThresholdGroup,
       "mcmSysTrapCPUUtilThreshold": mcmSysTrapCPUUtilThreshold,
       "mcmSysTrapBandwidthUtilThreshold": mcmSysTrapBandwidthUtilThreshold,
       "mcmSysTrapRAMUtilThreshold": mcmSysTrapRAMUtilThreshold}
)
