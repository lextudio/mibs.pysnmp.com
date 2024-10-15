# SNMP MIB module (DESKSNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DESKSNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:02 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniExtensions_ObjectIdentity = ObjectIdentity
sniExtensions = _SniExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10)
)
_SniDesktopMgmt_ObjectIdentity = ObjectIdentity
sniDesktopMgmt = _SniDesktopMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3)
)
_SniDeskInfo_ObjectIdentity = ObjectIdentity
sniDeskInfo = _SniDeskInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1)
)
_SniPCInformation_ObjectIdentity = ObjectIdentity
sniPCInformation = _SniPCInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2)
)
_SniPCManufacturer_Type = DisplayString
_SniPCManufacturer_Object = MibScalar
sniPCManufacturer = _SniPCManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2, 1),
    _SniPCManufacturer_Type()
)
sniPCManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCManufacturer.setStatus("mandatory")
_SniPCName_Type = DisplayString
_SniPCName_Object = MibScalar
sniPCName = _SniPCName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2, 2),
    _SniPCName_Type()
)
sniPCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCName.setStatus("mandatory")
_SniProductVersion_Type = DisplayString
_SniProductVersion_Object = MibScalar
sniProductVersion = _SniProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2, 3),
    _SniProductVersion_Type()
)
sniProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProductVersion.setStatus("mandatory")
_SniPCSerialNumber_Type = DisplayString
_SniPCSerialNumber_Object = MibScalar
sniPCSerialNumber = _SniPCSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2, 4),
    _SniPCSerialNumber_Type()
)
sniPCSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCSerialNumber.setStatus("mandatory")


class _SniChassisType_Type(Integer32):
    """Custom type sniChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("e-all-in-one", 13),
          ("e-bus-expansion-chassis", 20),
          ("e-desktop", 3),
          ("e-docking-station", 12),
          ("e-expansion-chassis", 18),
          ("e-handheld", 11),
          ("e-laptop", 9),
          ("e-low-profile-desktop", 4),
          ("e-lunch-box", 16),
          ("e-mainserver", 17),
          ("e-mini-tower", 6),
          ("e-notebook", 10),
          ("e-peripheral-chassis", 21),
          ("e-pizza-box", 5),
          ("e-portable", 8),
          ("e-rack-mount-chassis", 23),
          ("e-raid-chassis", 22),
          ("e-space-saving", 15),
          ("e-sub-chassis", 19),
          ("e-sub-notebook", 14),
          ("e-tower", 7),
          ("e-unknown", 0))
    )


_SniChassisType_Type.__name__ = "Integer32"
_SniChassisType_Object = MibScalar
sniChassisType = _SniChassisType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2, 5),
    _SniChassisType_Type()
)
sniChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniChassisType.setStatus("mandatory")
_SniChassisColor_Type = Integer32
_SniChassisColor_Object = MibScalar
sniChassisColor = _SniChassisColor_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2, 6),
    _SniChassisColor_Type()
)
sniChassisColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniChassisColor.setStatus("mandatory")
_SniHousingGeometry_Type = DisplayString
_SniHousingGeometry_Object = MibScalar
sniHousingGeometry = _SniHousingGeometry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2, 7),
    _SniHousingGeometry_Type()
)
sniHousingGeometry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniHousingGeometry.setStatus("mandatory")
_SniCustomerSpecificSerialNumber_Type = DisplayString
_SniCustomerSpecificSerialNumber_Object = MibScalar
sniCustomerSpecificSerialNumber = _SniCustomerSpecificSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2, 8),
    _SniCustomerSpecificSerialNumber_Type()
)
sniCustomerSpecificSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCustomerSpecificSerialNumber.setStatus("mandatory")
_SniUUID_Type = DisplayString
_SniUUID_Object = MibScalar
sniUUID = _SniUUID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 2, 9),
    _SniUUID_Type()
)
sniUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniUUID.setStatus("mandatory")
_SniBios_ObjectIdentity = ObjectIdentity
sniBios = _SniBios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3)
)
_SniBiosManufacturer_Type = DisplayString
_SniBiosManufacturer_Object = MibScalar
sniBiosManufacturer = _SniBiosManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 1),
    _SniBiosManufacturer_Type()
)
sniBiosManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBiosManufacturer.setStatus("mandatory")
_SniAdaptions_Type = DisplayString
_SniAdaptions_Object = MibScalar
sniAdaptions = _SniAdaptions_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 2),
    _SniAdaptions_Type()
)
sniAdaptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAdaptions.setStatus("mandatory")
_SniFeatures_Type = DisplayString
_SniFeatures_Object = MibScalar
sniFeatures = _SniFeatures_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 3),
    _SniFeatures_Type()
)
sniFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniFeatures.setStatus("mandatory")
_SniBiosVersion_Type = DisplayString
_SniBiosVersion_Object = MibScalar
sniBiosVersion = _SniBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 4),
    _SniBiosVersion_Type()
)
sniBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBiosVersion.setStatus("mandatory")
_SniLoaderVersion_Type = DisplayString
_SniLoaderVersion_Object = MibScalar
sniLoaderVersion = _SniLoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 5),
    _SniLoaderVersion_Type()
)
sniLoaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLoaderVersion.setStatus("mandatory")
_SniRomSizekB_Type = Integer32
_SniRomSizekB_Object = MibScalar
sniRomSizekB = _SniRomSizekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 6),
    _SniRomSizekB_Type()
)
sniRomSizekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniRomSizekB.setStatus("mandatory")
_SniBiosDate_Type = DisplayString
_SniBiosDate_Object = MibScalar
sniBiosDate = _SniBiosDate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 7),
    _SniBiosDate_Type()
)
sniBiosDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBiosDate.setStatus("mandatory")
_SniStatus_Type = Integer32
_SniStatus_Object = MibScalar
sniStatus = _SniStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 10),
    _SniStatus_Type()
)
sniStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniStatus.setStatus("mandatory")
_SniStartaddress_Type = DisplayString
_SniStartaddress_Object = MibScalar
sniStartaddress = _SniStartaddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 11),
    _SniStartaddress_Type()
)
sniStartaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniStartaddress.setStatus("mandatory")
_SniEndaddress_Type = DisplayString
_SniEndaddress_Object = MibScalar
sniEndaddress = _SniEndaddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 13),
    _SniEndaddress_Type()
)
sniEndaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEndaddress.setStatus("mandatory")


class _SniISABus_Type(Integer32):
    """Custom type sniISABus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniISABus_Type.__name__ = "Integer32"
_SniISABus_Object = MibScalar
sniISABus = _SniISABus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 15),
    _SniISABus_Type()
)
sniISABus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniISABus.setStatus("mandatory")


class _SniMCABus_Type(Integer32):
    """Custom type sniMCABus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniMCABus_Type.__name__ = "Integer32"
_SniMCABus_Object = MibScalar
sniMCABus = _SniMCABus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 16),
    _SniMCABus_Type()
)
sniMCABus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMCABus.setStatus("mandatory")


class _SniEISABus_Type(Integer32):
    """Custom type sniEISABus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniEISABus_Type.__name__ = "Integer32"
_SniEISABus_Object = MibScalar
sniEISABus = _SniEISABus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 17),
    _SniEISABus_Type()
)
sniEISABus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEISABus.setStatus("mandatory")


class _SniPCIBus_Type(Integer32):
    """Custom type sniPCIBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPCIBus_Type.__name__ = "Integer32"
_SniPCIBus_Object = MibScalar
sniPCIBus = _SniPCIBus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 18),
    _SniPCIBus_Type()
)
sniPCIBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIBus.setStatus("mandatory")


class _SniPCMCIAInterface_Type(Integer32):
    """Custom type sniPCMCIAInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPCMCIAInterface_Type.__name__ = "Integer32"
_SniPCMCIAInterface_Object = MibScalar
sniPCMCIAInterface = _SniPCMCIAInterface_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 19),
    _SniPCMCIAInterface_Type()
)
sniPCMCIAInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCMCIAInterface.setStatus("mandatory")


class _SniPlugandPlayPnP_Type(Integer32):
    """Custom type sniPlugandPlayPnP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPlugandPlayPnP_Type.__name__ = "Integer32"
_SniPlugandPlayPnP_Object = MibScalar
sniPlugandPlayPnP = _SniPlugandPlayPnP_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 20),
    _SniPlugandPlayPnP_Type()
)
sniPlugandPlayPnP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPlugandPlayPnP.setStatus("mandatory")


class _SniAdvPowerManagemAPM_Type(Integer32):
    """Custom type sniAdvPowerManagemAPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniAdvPowerManagemAPM_Type.__name__ = "Integer32"
_SniAdvPowerManagemAPM_Object = MibScalar
sniAdvPowerManagemAPM = _SniAdvPowerManagemAPM_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 21),
    _SniAdvPowerManagemAPM_Type()
)
sniAdvPowerManagemAPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAdvPowerManagemAPM.setStatus("mandatory")


class _SniVLBus_Type(Integer32):
    """Custom type sniVLBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniVLBus_Type.__name__ = "Integer32"
_SniVLBus_Object = MibScalar
sniVLBus = _SniVLBus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 22),
    _SniVLBus_Type()
)
sniVLBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniVLBus.setStatus("mandatory")


class _SniESCDBus_Type(Integer32):
    """Custom type sniESCDBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniESCDBus_Type.__name__ = "Integer32"
_SniESCDBus_Object = MibScalar
sniESCDBus = _SniESCDBus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 23),
    _SniESCDBus_Type()
)
sniESCDBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniESCDBus.setStatus("mandatory")


class _SniIRDABus_Type(Integer32):
    """Custom type sniIRDABus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniIRDABus_Type.__name__ = "Integer32"
_SniIRDABus_Object = MibScalar
sniIRDABus = _SniIRDABus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 24),
    _SniIRDABus_Type()
)
sniIRDABus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIRDABus.setStatus("mandatory")


class _SniBootfromCDROM_Type(Integer32):
    """Custom type sniBootfromCDROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniBootfromCDROM_Type.__name__ = "Integer32"
_SniBootfromCDROM_Object = MibScalar
sniBootfromCDROM = _SniBootfromCDROM_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 25),
    _SniBootfromCDROM_Type()
)
sniBootfromCDROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBootfromCDROM.setStatus("mandatory")


class _SniBootfromPCMCIA_Type(Integer32):
    """Custom type sniBootfromPCMCIA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniBootfromPCMCIA_Type.__name__ = "Integer32"
_SniBootfromPCMCIA_Object = MibScalar
sniBootfromPCMCIA = _SniBootfromPCMCIA_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 26),
    _SniBootfromPCMCIA_Type()
)
sniBootfromPCMCIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBootfromPCMCIA.setStatus("mandatory")


class _SniBiosShadowing_Type(Integer32):
    """Custom type sniBiosShadowing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniBiosShadowing_Type.__name__ = "Integer32"
_SniBiosShadowing_Object = MibScalar
sniBiosShadowing = _SniBiosShadowing_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 27),
    _SniBiosShadowing_Type()
)
sniBiosShadowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBiosShadowing.setStatus("mandatory")


class _SniSavetoDiskStd_Type(Integer32):
    """Custom type sniSavetoDiskStd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniSavetoDiskStd_Type.__name__ = "Integer32"
_SniSavetoDiskStd_Object = MibScalar
sniSavetoDiskStd = _SniSavetoDiskStd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 28),
    _SniSavetoDiskStd_Type()
)
sniSavetoDiskStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSavetoDiskStd.setStatus("mandatory")


class _SniSecurity_Type(Integer32):
    """Custom type sniSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniSecurity_Type.__name__ = "Integer32"
_SniSecurity_Object = MibScalar
sniSecurity = _SniSecurity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 29),
    _SniSecurity_Type()
)
sniSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSecurity.setStatus("mandatory")


class _SniUSB_Type(Integer32):
    """Custom type sniUSB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniUSB_Type.__name__ = "Integer32"
_SniUSB_Object = MibScalar
sniUSB = _SniUSB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 30),
    _SniUSB_Type()
)
sniUSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniUSB.setStatus("mandatory")


class _SniSoftwarePowerOff_Type(Integer32):
    """Custom type sniSoftwarePowerOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniSoftwarePowerOff_Type.__name__ = "Integer32"
_SniSoftwarePowerOff_Object = MibScalar
sniSoftwarePowerOff = _SniSoftwarePowerOff_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 31),
    _SniSoftwarePowerOff_Type()
)
sniSoftwarePowerOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSoftwarePowerOff.setStatus("mandatory")


class _SniRemoteOn_Type(Integer32):
    """Custom type sniRemoteOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniRemoteOn_Type.__name__ = "Integer32"
_SniRemoteOn_Object = MibScalar
sniRemoteOn = _SniRemoteOn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 32),
    _SniRemoteOn_Type()
)
sniRemoteOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniRemoteOn.setStatus("mandatory")
_SniAPMSpecificVersion_Type = DisplayString
_SniAPMSpecificVersion_Object = MibScalar
sniAPMSpecificVersion = _SniAPMSpecificVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 33),
    _SniAPMSpecificVersion_Type()
)
sniAPMSpecificVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAPMSpecificVersion.setStatus("mandatory")
_SniPNPSpecificVersion_Type = DisplayString
_SniPNPSpecificVersion_Object = MibScalar
sniPNPSpecificVersion = _SniPNPSpecificVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 35),
    _SniPNPSpecificVersion_Type()
)
sniPNPSpecificVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPNPSpecificVersion.setStatus("mandatory")


class _SniFlashBIOS_Type(Integer32):
    """Custom type sniFlashBIOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniFlashBIOS_Type.__name__ = "Integer32"
_SniFlashBIOS_Object = MibScalar
sniFlashBIOS = _SniFlashBIOS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 37),
    _SniFlashBIOS_Type()
)
sniFlashBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniFlashBIOS.setStatus("mandatory")


class _SniPC98_Type(Integer32):
    """Custom type sniPC98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPC98_Type.__name__ = "Integer32"
_SniPC98_Object = MibScalar
sniPC98 = _SniPC98_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 38),
    _SniPC98_Type()
)
sniPC98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPC98.setStatus("mandatory")


class _SniBootDeviceSelectable_Type(Integer32):
    """Custom type sniBootDeviceSelectable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniBootDeviceSelectable_Type.__name__ = "Integer32"
_SniBootDeviceSelectable_Object = MibScalar
sniBootDeviceSelectable = _SniBootDeviceSelectable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 39),
    _SniBootDeviceSelectable_Type()
)
sniBootDeviceSelectable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBootDeviceSelectable.setStatus("mandatory")


class _SniBIOSRomSocketed_Type(Integer32):
    """Custom type sniBIOSRomSocketed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniBIOSRomSocketed_Type.__name__ = "Integer32"
_SniBIOSRomSocketed_Object = MibScalar
sniBIOSRomSocketed = _SniBIOSRomSocketed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 40),
    _SniBIOSRomSocketed_Type()
)
sniBIOSRomSocketed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBIOSRomSocketed.setStatus("mandatory")


class _SniEnhancedDiskDriveEDD_Type(Integer32):
    """Custom type sniEnhancedDiskDriveEDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniEnhancedDiskDriveEDD_Type.__name__ = "Integer32"
_SniEnhancedDiskDriveEDD_Object = MibScalar
sniEnhancedDiskDriveEDD = _SniEnhancedDiskDriveEDD_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 41),
    _SniEnhancedDiskDriveEDD_Type()
)
sniEnhancedDiskDriveEDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEnhancedDiskDriveEDD.setStatus("mandatory")


class _SniNEC9800FloppySupport_Type(Integer32):
    """Custom type sniNEC9800FloppySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniNEC9800FloppySupport_Type.__name__ = "Integer32"
_SniNEC9800FloppySupport_Object = MibScalar
sniNEC9800FloppySupport = _SniNEC9800FloppySupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 42),
    _SniNEC9800FloppySupport_Type()
)
sniNEC9800FloppySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNEC9800FloppySupport.setStatus("mandatory")


class _SniToshibaFloppySupport_Type(Integer32):
    """Custom type sniToshibaFloppySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniToshibaFloppySupport_Type.__name__ = "Integer32"
_SniToshibaFloppySupport_Object = MibScalar
sniToshibaFloppySupport = _SniToshibaFloppySupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 43),
    _SniToshibaFloppySupport_Type()
)
sniToshibaFloppySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniToshibaFloppySupport.setStatus("mandatory")


class _Sni360kBFloppySupport_Type(Integer32):
    """Custom type sni360kBFloppySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_Sni360kBFloppySupport_Type.__name__ = "Integer32"
_Sni360kBFloppySupport_Object = MibScalar
sni360kBFloppySupport = _Sni360kBFloppySupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 44),
    _Sni360kBFloppySupport_Type()
)
sni360kBFloppySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sni360kBFloppySupport.setStatus("mandatory")


class _Sni720kBFloppySupport_Type(Integer32):
    """Custom type sni720kBFloppySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_Sni720kBFloppySupport_Type.__name__ = "Integer32"
_Sni720kBFloppySupport_Object = MibScalar
sni720kBFloppySupport = _Sni720kBFloppySupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 45),
    _Sni720kBFloppySupport_Type()
)
sni720kBFloppySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sni720kBFloppySupport.setStatus("mandatory")


class _Sni1MB2FloppySupport_Type(Integer32):
    """Custom type sni1MB2FloppySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_Sni1MB2FloppySupport_Type.__name__ = "Integer32"
_Sni1MB2FloppySupport_Object = MibScalar
sni1MB2FloppySupport = _Sni1MB2FloppySupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 46),
    _Sni1MB2FloppySupport_Type()
)
sni1MB2FloppySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sni1MB2FloppySupport.setStatus("mandatory")


class _Sni2MB88FloppySupport_Type(Integer32):
    """Custom type sni2MB88FloppySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_Sni2MB88FloppySupport_Type.__name__ = "Integer32"
_Sni2MB88FloppySupport_Object = MibScalar
sni2MB88FloppySupport = _Sni2MB88FloppySupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 47),
    _Sni2MB88FloppySupport_Type()
)
sni2MB88FloppySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sni2MB88FloppySupport.setStatus("mandatory")


class _SniInt5PrintScreenService_Type(Integer32):
    """Custom type sniInt5PrintScreenService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniInt5PrintScreenService_Type.__name__ = "Integer32"
_SniInt5PrintScreenService_Object = MibScalar
sniInt5PrintScreenService = _SniInt5PrintScreenService_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 48),
    _SniInt5PrintScreenService_Type()
)
sniInt5PrintScreenService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInt5PrintScreenService.setStatus("mandatory")


class _SniInt9Keyboard8042Supp_Type(Integer32):
    """Custom type sniInt9Keyboard8042Supp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniInt9Keyboard8042Supp_Type.__name__ = "Integer32"
_SniInt9Keyboard8042Supp_Object = MibScalar
sniInt9Keyboard8042Supp = _SniInt9Keyboard8042Supp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 49),
    _SniInt9Keyboard8042Supp_Type()
)
sniInt9Keyboard8042Supp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInt9Keyboard8042Supp.setStatus("mandatory")


class _SniSoftwarePowerOn_Type(Integer32):
    """Custom type sniSoftwarePowerOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniSoftwarePowerOn_Type.__name__ = "Integer32"
_SniSoftwarePowerOn_Object = MibScalar
sniSoftwarePowerOn = _SniSoftwarePowerOn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 50),
    _SniSoftwarePowerOn_Type()
)
sniSoftwarePowerOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSoftwarePowerOn.setStatus("mandatory")


class _SniISAMemoryGapSupport_Type(Integer32):
    """Custom type sniISAMemoryGapSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniISAMemoryGapSupport_Type.__name__ = "Integer32"
_SniISAMemoryGapSupport_Object = MibScalar
sniISAMemoryGapSupport = _SniISAMemoryGapSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 51),
    _SniISAMemoryGapSupport_Type()
)
sniISAMemoryGapSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniISAMemoryGapSupport.setStatus("mandatory")


class _SniIEEE1394Support_Type(Integer32):
    """Custom type sniIEEE1394Support based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniIEEE1394Support_Type.__name__ = "Integer32"
_SniIEEE1394Support_Object = MibScalar
sniIEEE1394Support = _SniIEEE1394Support_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 52),
    _SniIEEE1394Support_Type()
)
sniIEEE1394Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIEEE1394Support.setStatus("mandatory")


class _SniDMISupport_Type(Integer32):
    """Custom type sniDMISupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniDMISupport_Type.__name__ = "Integer32"
_SniDMISupport_Object = MibScalar
sniDMISupport = _SniDMISupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 53),
    _SniDMISupport_Type()
)
sniDMISupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDMISupport.setStatus("mandatory")


class _SniACPISupport_Type(Integer32):
    """Custom type sniACPISupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniACPISupport_Type.__name__ = "Integer32"
_SniACPISupport_Object = MibScalar
sniACPISupport = _SniACPISupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 54),
    _SniACPISupport_Type()
)
sniACPISupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniACPISupport.setStatus("mandatory")


class _SniSystemMonitoring_Type(Integer32):
    """Custom type sniSystemMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniSystemMonitoring_Type.__name__ = "Integer32"
_SniSystemMonitoring_Object = MibScalar
sniSystemMonitoring = _SniSystemMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 55),
    _SniSystemMonitoring_Type()
)
sniSystemMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSystemMonitoring.setStatus("mandatory")


class _SniInt14SerialServices_Type(Integer32):
    """Custom type sniInt14SerialServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniInt14SerialServices_Type.__name__ = "Integer32"
_SniInt14SerialServices_Object = MibScalar
sniInt14SerialServices = _SniInt14SerialServices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 56),
    _SniInt14SerialServices_Type()
)
sniInt14SerialServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInt14SerialServices.setStatus("mandatory")


class _SniInt17PrinterServices_Type(Integer32):
    """Custom type sniInt17PrinterServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniInt17PrinterServices_Type.__name__ = "Integer32"
_SniInt17PrinterServices_Object = MibScalar
sniInt17PrinterServices = _SniInt17PrinterServices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 57),
    _SniInt17PrinterServices_Type()
)
sniInt17PrinterServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInt17PrinterServices.setStatus("mandatory")


class _SniInt10CGAVideoServices_Type(Integer32):
    """Custom type sniInt10CGAVideoServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniInt10CGAVideoServices_Type.__name__ = "Integer32"
_SniInt10CGAVideoServices_Object = MibScalar
sniInt10CGAVideoServices = _SniInt10CGAVideoServices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 58),
    _SniInt10CGAVideoServices_Type()
)
sniInt10CGAVideoServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInt10CGAVideoServices.setStatus("mandatory")


class _SniAGPSupport_Type(Integer32):
    """Custom type sniAGPSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniAGPSupport_Type.__name__ = "Integer32"
_SniAGPSupport_Object = MibScalar
sniAGPSupport = _SniAGPSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 59),
    _SniAGPSupport_Type()
)
sniAGPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAGPSupport.setStatus("mandatory")


class _SniI2OBootSupport_Type(Integer32):
    """Custom type sniI2OBootSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniI2OBootSupport_Type.__name__ = "Integer32"
_SniI2OBootSupport_Object = MibScalar
sniI2OBootSupport = _SniI2OBootSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 60),
    _SniI2OBootSupport_Type()
)
sniI2OBootSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniI2OBootSupport.setStatus("mandatory")


class _SniLS120BootSupport_Type(Integer32):
    """Custom type sniLS120BootSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniLS120BootSupport_Type.__name__ = "Integer32"
_SniLS120BootSupport_Object = MibScalar
sniLS120BootSupport = _SniLS120BootSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 61),
    _SniLS120BootSupport_Type()
)
sniLS120BootSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLS120BootSupport.setStatus("mandatory")


class _SniAtapiZIPDriveBootSupport_Type(Integer32):
    """Custom type sniAtapiZIPDriveBootSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniAtapiZIPDriveBootSupport_Type.__name__ = "Integer32"
_SniAtapiZIPDriveBootSupport_Object = MibScalar
sniAtapiZIPDriveBootSupport = _SniAtapiZIPDriveBootSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 62),
    _SniAtapiZIPDriveBootSupport_Type()
)
sniAtapiZIPDriveBootSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAtapiZIPDriveBootSupport.setStatus("mandatory")


class _SniSMARTBatterieSupport_Type(Integer32):
    """Custom type sniSMARTBatterieSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniSMARTBatterieSupport_Type.__name__ = "Integer32"
_SniSMARTBatterieSupport_Object = MibScalar
sniSMARTBatterieSupport = _SniSMARTBatterieSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 3, 63),
    _SniSMARTBatterieSupport_Type()
)
sniSMARTBatterieSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSMARTBatterieSupport.setStatus("mandatory")
_SniMemory_ObjectIdentity = ObjectIdentity
sniMemory = _SniMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4)
)
_SniPhysicalMemoryMB_Type = Integer32
_SniPhysicalMemoryMB_Object = MibScalar
sniPhysicalMemoryMB = _SniPhysicalMemoryMB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 1),
    _SniPhysicalMemoryMB_Type()
)
sniPhysicalMemoryMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalMemoryMB.setStatus("mandatory")
_SniBaseMemorykB_Type = Integer32
_SniBaseMemorykB_Object = MibScalar
sniBaseMemorykB = _SniBaseMemorykB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 2),
    _SniBaseMemorykB_Type()
)
sniBaseMemorykB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBaseMemorykB.setStatus("mandatory")
_SniFreePhysicalMemorykB_Type = Integer32
_SniFreePhysicalMemorykB_Object = MibScalar
sniFreePhysicalMemorykB = _SniFreePhysicalMemorykB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 3),
    _SniFreePhysicalMemorykB_Type()
)
sniFreePhysicalMemorykB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniFreePhysicalMemorykB.setStatus("mandatory")
_SniFreeUserResourcesPercentage_Type = Integer32
_SniFreeUserResourcesPercentage_Object = MibScalar
sniFreeUserResourcesPercentage = _SniFreeUserResourcesPercentage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 4),
    _SniFreeUserResourcesPercentage_Type()
)
sniFreeUserResourcesPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniFreeUserResourcesPercentage.setStatus("mandatory")
_SniFreeGDIResourcesPercentage_Type = Integer32
_SniFreeGDIResourcesPercentage_Object = MibScalar
sniFreeGDIResourcesPercentage = _SniFreeGDIResourcesPercentage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 5),
    _SniFreeGDIResourcesPercentage_Type()
)
sniFreeGDIResourcesPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniFreeGDIResourcesPercentage.setStatus("mandatory")


class _SniVirtualMemoryType_Type(Integer32):
    """Custom type sniVirtualMemoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e-dos-paging", 2),
          ("e-no-paging", 1),
          ("e-protected-paging", 3),
          ("e-unknown", 0))
    )


_SniVirtualMemoryType_Type.__name__ = "Integer32"
_SniVirtualMemoryType_Object = MibScalar
sniVirtualMemoryType = _SniVirtualMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 6),
    _SniVirtualMemoryType_Type()
)
sniVirtualMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniVirtualMemoryType.setStatus("mandatory")
_SniSwapFileName_Type = DisplayString
_SniSwapFileName_Object = MibScalar
sniSwapFileName = _SniSwapFileName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 7),
    _SniSwapFileName_Type()
)
sniSwapFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSwapFileName.setStatus("mandatory")
_SniSwapFileSizekB_Type = Integer32
_SniSwapFileSizekB_Object = MibScalar
sniSwapFileSizekB = _SniSwapFileSizekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 8),
    _SniSwapFileSizekB_Type()
)
sniSwapFileSizekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSwapFileSizekB.setStatus("mandatory")
_SniSwapFileUsedPercentage_Type = Integer32
_SniSwapFileUsedPercentage_Object = MibScalar
sniSwapFileUsedPercentage = _SniSwapFileUsedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 9),
    _SniSwapFileUsedPercentage_Type()
)
sniSwapFileUsedPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSwapFileUsedPercentage.setStatus("mandatory")
_SniEMMSizekB_Type = Integer32
_SniEMMSizekB_Object = MibScalar
sniEMMSizekB = _SniEMMSizekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 10),
    _SniEMMSizekB_Type()
)
sniEMMSizekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEMMSizekB.setStatus("mandatory")
_SniEMMFreekB_Type = Integer32
_SniEMMFreekB_Object = MibScalar
sniEMMFreekB = _SniEMMFreekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 11),
    _SniEMMFreekB_Type()
)
sniEMMFreekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEMMFreekB.setStatus("mandatory")
_SniEMMDriverVersion_Type = DisplayString
_SniEMMDriverVersion_Object = MibScalar
sniEMMDriverVersion = _SniEMMDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 12),
    _SniEMMDriverVersion_Type()
)
sniEMMDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEMMDriverVersion.setStatus("mandatory")
_SniEMMDriverName_Type = DisplayString
_SniEMMDriverName_Object = MibScalar
sniEMMDriverName = _SniEMMDriverName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 13),
    _SniEMMDriverName_Type()
)
sniEMMDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEMMDriverName.setStatus("mandatory")
_SniXMSSizekB_Type = Integer32
_SniXMSSizekB_Object = MibScalar
sniXMSSizekB = _SniXMSSizekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 14),
    _SniXMSSizekB_Type()
)
sniXMSSizekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniXMSSizekB.setStatus("mandatory")
_SniXMSFreeMemorykB_Type = Integer32
_SniXMSFreeMemorykB_Object = MibScalar
sniXMSFreeMemorykB = _SniXMSFreeMemorykB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 15),
    _SniXMSFreeMemorykB_Type()
)
sniXMSFreeMemorykB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniXMSFreeMemorykB.setStatus("mandatory")
_SniXMSDriverVersion_Type = DisplayString
_SniXMSDriverVersion_Object = MibScalar
sniXMSDriverVersion = _SniXMSDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 16),
    _SniXMSDriverVersion_Type()
)
sniXMSDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniXMSDriverVersion.setStatus("mandatory")
_SniXMSDriverName_Type = DisplayString
_SniXMSDriverName_Object = MibScalar
sniXMSDriverName = _SniXMSDriverName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 4, 17),
    _SniXMSDriverName_Type()
)
sniXMSDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniXMSDriverName.setStatus("mandatory")
_SniGraphic_ObjectIdentity = ObjectIdentity
sniGraphic = _SniGraphic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5)
)
_SniGraphicCardManufacturer_Type = DisplayString
_SniGraphicCardManufacturer_Object = MibScalar
sniGraphicCardManufacturer = _SniGraphicCardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 1),
    _SniGraphicCardManufacturer_Type()
)
sniGraphicCardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGraphicCardManufacturer.setStatus("mandatory")
_SniGraphicController_Type = DisplayString
_SniGraphicController_Object = MibScalar
sniGraphicController = _SniGraphicController_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 2),
    _SniGraphicController_Type()
)
sniGraphicController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGraphicController.setStatus("mandatory")
_SniGraphicCardDate_Type = DisplayString
_SniGraphicCardDate_Object = MibScalar
sniGraphicCardDate = _SniGraphicCardDate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 3),
    _SniGraphicCardDate_Type()
)
sniGraphicCardDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGraphicCardDate.setStatus("mandatory")


class _SniShadowed_Type(Integer32):
    """Custom type sniShadowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniShadowed_Type.__name__ = "Integer32"
_SniShadowed_Object = MibScalar
sniShadowed = _SniShadowed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 4),
    _SniShadowed_Type()
)
sniShadowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniShadowed.setStatus("mandatory")


class _SniGraphicType_Type(Integer32):
    """Custom type sniGraphicType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("e-8514a", 10),
          ("e-cga", 3),
          ("e-ega", 4),
          ("e-frame-buffer", 12),
          ("e-hgc", 8),
          ("e-mcga", 9),
          ("e-mda", 7),
          ("e-svga", 6),
          ("e-unknown", 0),
          ("e-vga", 5),
          ("e-xga", 11))
    )


_SniGraphicType_Type.__name__ = "Integer32"
_SniGraphicType_Object = MibScalar
sniGraphicType = _SniGraphicType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 5),
    _SniGraphicType_Type()
)
sniGraphicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGraphicType.setStatus("mandatory")
_SniDriver_Type = DisplayString
_SniDriver_Object = MibScalar
sniDriver = _SniDriver_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 6),
    _SniDriver_Type()
)
sniDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDriver.setStatus("mandatory")
_SniGraphicmode_Type = Integer32
_SniGraphicmode_Object = MibScalar
sniGraphicmode = _SniGraphicmode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 7),
    _SniGraphicmode_Type()
)
sniGraphicmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGraphicmode.setStatus("mandatory")
_SnivertResolutionPixel_Type = Integer32
_SnivertResolutionPixel_Object = MibScalar
snivertResolutionPixel = _SnivertResolutionPixel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 8),
    _SnivertResolutionPixel_Type()
)
snivertResolutionPixel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snivertResolutionPixel.setStatus("mandatory")
_SnihorResolutionPixel_Type = Integer32
_SnihorResolutionPixel_Object = MibScalar
snihorResolutionPixel = _SnihorResolutionPixel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 9),
    _SnihorResolutionPixel_Type()
)
snihorResolutionPixel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snihorResolutionPixel.setStatus("mandatory")
_SniColorResolution_Type = Integer32
_SniColorResolution_Object = MibScalar
sniColorResolution = _SniColorResolution_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 10),
    _SniColorResolution_Type()
)
sniColorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniColorResolution.setStatus("mandatory")
_SniRefreshrateHz_Type = Integer32
_SniRefreshrateHz_Object = MibScalar
sniRefreshrateHz = _SniRefreshrateHz_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 11),
    _SniRefreshrateHz_Type()
)
sniRefreshrateHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniRefreshrateHz.setStatus("mandatory")


class _SniScanMode_Type(Integer32):
    """Custom type sniScanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-interlaced", 3),
          ("e-non-interlaced", 4),
          ("e-unknown", 0))
    )


_SniScanMode_Type.__name__ = "Integer32"
_SniScanMode_Object = MibScalar
sniScanMode = _SniScanMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 12),
    _SniScanMode_Type()
)
sniScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniScanMode.setStatus("mandatory")
_SniMinRefreshrateHz_Type = Integer32
_SniMinRefreshrateHz_Object = MibScalar
sniMinRefreshrateHz = _SniMinRefreshrateHz_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 13),
    _SniMinRefreshrateHz_Type()
)
sniMinRefreshrateHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMinRefreshrateHz.setStatus("mandatory")
_SniMaxRefreshrateHz_Type = Integer32
_SniMaxRefreshrateHz_Object = MibScalar
sniMaxRefreshrateHz = _SniMaxRefreshrateHz_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 14),
    _SniMaxRefreshrateHz_Type()
)
sniMaxRefreshrateHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaxRefreshrateHz.setStatus("mandatory")
_SniMemorySizeKB_Type = Integer32
_SniMemorySizeKB_Object = MibScalar
sniMemorySizeKB = _SniMemorySizeKB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 15),
    _SniMemorySizeKB_Type()
)
sniMemorySizeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemorySizeKB.setStatus("mandatory")


class _SniMemoryType_Type(Integer32):
    """Custom type sniMemoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e-dram", 4),
          ("e-sram", 5),
          ("e-unknown", 0),
          ("e-vram", 3))
    )


_SniMemoryType_Type.__name__ = "Integer32"
_SniMemoryType_Object = MibScalar
sniMemoryType = _SniMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 16),
    _SniMemoryType_Type()
)
sniMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryType.setStatus("mandatory")


class _SniGraphicCardLocation_Type(Integer32):
    """Custom type sniGraphicCardLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-add-on", 4),
          ("e-integrated", 3),
          ("e-unknown", 0))
    )


_SniGraphicCardLocation_Type.__name__ = "Integer32"
_SniGraphicCardLocation_Object = MibScalar
sniGraphicCardLocation = _SniGraphicCardLocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 17),
    _SniGraphicCardLocation_Type()
)
sniGraphicCardLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGraphicCardLocation.setStatus("mandatory")


class _SniStandardBios_Type(Integer32):
    """Custom type sniStandardBios based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniStandardBios_Type.__name__ = "Integer32"
_SniStandardBios_Object = MibScalar
sniStandardBios = _SniStandardBios_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 18),
    _SniStandardBios_Type()
)
sniStandardBios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniStandardBios.setStatus("mandatory")


class _SniVESAExtensions_Type(Integer32):
    """Custom type sniVESAExtensions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniVESAExtensions_Type.__name__ = "Integer32"
_SniVESAExtensions_Object = MibScalar
sniVESAExtensions = _SniVESAExtensions_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 19),
    _SniVESAExtensions_Type()
)
sniVESAExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniVESAExtensions.setStatus("mandatory")


class _SniDPMS_Type(Integer32):
    """Custom type sniDPMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniDPMS_Type.__name__ = "Integer32"
_SniDPMS_Object = MibScalar
sniDPMS = _SniDPMS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 20),
    _SniDPMS_Type()
)
sniDPMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDPMS.setStatus("mandatory")


class _SniDDC_Type(Integer32):
    """Custom type sniDDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniDDC_Type.__name__ = "Integer32"
_SniDDC_Object = MibScalar
sniDDC = _SniDDC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 21),
    _SniDDC_Type()
)
sniDDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDDC.setStatus("mandatory")


class _SniShadowing_Type(Integer32):
    """Custom type sniShadowing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniShadowing_Type.__name__ = "Integer32"
_SniShadowing_Object = MibScalar
sniShadowing = _SniShadowing_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 22),
    _SniShadowing_Type()
)
sniShadowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniShadowing.setStatus("mandatory")


class _SniUpgradable_Type(Integer32):
    """Custom type sniUpgradable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniUpgradable_Type.__name__ = "Integer32"
_SniUpgradable_Object = MibScalar
sniUpgradable = _SniUpgradable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 5, 23),
    _SniUpgradable_Type()
)
sniUpgradable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniUpgradable.setStatus("mandatory")
_SniMonitor_ObjectIdentity = ObjectIdentity
sniMonitor = _SniMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6)
)
_SniMonitorName_Type = DisplayString
_SniMonitorName_Object = MibScalar
sniMonitorName = _SniMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 1),
    _SniMonitorName_Type()
)
sniMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMonitorName.setStatus("mandatory")
_SniSizeInch_Type = Integer32
_SniSizeInch_Object = MibScalar
sniSizeInch = _SniSizeInch_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 2),
    _SniSizeInch_Type()
)
sniSizeInch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSizeInch.setStatus("mandatory")


class _SniDDCSupport_Type(Integer32):
    """Custom type sniDDCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniDDCSupport_Type.__name__ = "Integer32"
_SniDDCSupport_Object = MibScalar
sniDDCSupport = _SniDDCSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 3),
    _SniDDCSupport_Type()
)
sniDDCSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDDCSupport.setStatus("mandatory")


class _SniDPMSSupport_Type(Integer32):
    """Custom type sniDPMSSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniDPMSSupport_Type.__name__ = "Integer32"
_SniDPMSSupport_Object = MibScalar
sniDPMSSupport = _SniDPMSSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 4),
    _SniDPMSSupport_Type()
)
sniDPMSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDPMSSupport.setStatus("mandatory")
_SniMaxhorizResolution_Type = Integer32
_SniMaxhorizResolution_Object = MibScalar
sniMaxhorizResolution = _SniMaxhorizResolution_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 5),
    _SniMaxhorizResolution_Type()
)
sniMaxhorizResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaxhorizResolution.setStatus("mandatory")
_SniMaxverticalResolution_Type = Integer32
_SniMaxverticalResolution_Object = MibScalar
sniMaxverticalResolution = _SniMaxverticalResolution_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 6),
    _SniMaxverticalResolution_Type()
)
sniMaxverticalResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaxverticalResolution.setStatus("mandatory")
_SniMaxhorizontalFrequency_Type = Integer32
_SniMaxhorizontalFrequency_Object = MibScalar
sniMaxhorizontalFrequency = _SniMaxhorizontalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 7),
    _SniMaxhorizontalFrequency_Type()
)
sniMaxhorizontalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaxhorizontalFrequency.setStatus("mandatory")
_SniMinhorizontalFrequency_Type = Integer32
_SniMinhorizontalFrequency_Object = MibScalar
sniMinhorizontalFrequency = _SniMinhorizontalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 8),
    _SniMinhorizontalFrequency_Type()
)
sniMinhorizontalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMinhorizontalFrequency.setStatus("mandatory")
_SniMaximumRefreshrate_Type = Integer32
_SniMaximumRefreshrate_Object = MibScalar
sniMaximumRefreshrate = _SniMaximumRefreshrate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 9),
    _SniMaximumRefreshrate_Type()
)
sniMaximumRefreshrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaximumRefreshrate.setStatus("mandatory")
_SniMinimumRefreshrate_Type = Integer32
_SniMinimumRefreshrate_Object = MibScalar
sniMinimumRefreshrate = _SniMinimumRefreshrate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 10),
    _SniMinimumRefreshrate_Type()
)
sniMinimumRefreshrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMinimumRefreshrate.setStatus("mandatory")
_SniSerialNumber_Type = DisplayString
_SniSerialNumber_Object = MibScalar
sniSerialNumber = _SniSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 11),
    _SniSerialNumber_Type()
)
sniSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSerialNumber.setStatus("mandatory")
_SniWeekofManufacture_Type = Integer32
_SniWeekofManufacture_Object = MibScalar
sniWeekofManufacture = _SniWeekofManufacture_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 12),
    _SniWeekofManufacture_Type()
)
sniWeekofManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWeekofManufacture.setStatus("mandatory")
_SniYearofManufacture_Type = Integer32
_SniYearofManufacture_Object = MibScalar
sniYearofManufacture = _SniYearofManufacture_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 6, 13),
    _SniYearofManufacture_Type()
)
sniYearofManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniYearofManufacture.setStatus("mandatory")
_SniOperatingSystem_ObjectIdentity = ObjectIdentity
sniOperatingSystem = _SniOperatingSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7)
)
_SniOSName_Type = DisplayString
_SniOSName_Object = MibScalar
sniOSName = _SniOSName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 1),
    _SniOSName_Type()
)
sniOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOSName.setStatus("mandatory")
_SniOSVersion_Type = DisplayString
_SniOSVersion_Object = MibScalar
sniOSVersion = _SniOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 2),
    _SniOSVersion_Type()
)
sniOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOSVersion.setStatus("mandatory")
_SniOSLanguage_Type = DisplayString
_SniOSLanguage_Object = MibScalar
sniOSLanguage = _SniOSLanguage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 3),
    _SniOSLanguage_Type()
)
sniOSLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOSLanguage.setStatus("mandatory")
_SniOSInstallationDirectory_Type = DisplayString
_SniOSInstallationDirectory_Object = MibScalar
sniOSInstallationDirectory = _SniOSInstallationDirectory_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 4),
    _SniOSInstallationDirectory_Type()
)
sniOSInstallationDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOSInstallationDirectory.setStatus("mandatory")
_SniOSNameSecondary_Type = DisplayString
_SniOSNameSecondary_Object = MibScalar
sniOSNameSecondary = _SniOSNameSecondary_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 5),
    _SniOSNameSecondary_Type()
)
sniOSNameSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOSNameSecondary.setStatus("mandatory")
_SniOSVersionSecondary_Type = DisplayString
_SniOSVersionSecondary_Object = MibScalar
sniOSVersionSecondary = _SniOSVersionSecondary_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 6),
    _SniOSVersionSecondary_Type()
)
sniOSVersionSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOSVersionSecondary.setStatus("mandatory")
_SniOSLanguageSecondary_Type = DisplayString
_SniOSLanguageSecondary_Object = MibScalar
sniOSLanguageSecondary = _SniOSLanguageSecondary_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 7),
    _SniOSLanguageSecondary_Type()
)
sniOSLanguageSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOSLanguageSecondary.setStatus("mandatory")
_SniOSInstallDirSec_Type = DisplayString
_SniOSInstallDirSec_Object = MibScalar
sniOSInstallDirSec = _SniOSInstallDirSec_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 8),
    _SniOSInstallDirSec_Type()
)
sniOSInstallDirSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOSInstallDirSec.setStatus("mandatory")
_SniPreInstallationVersion_Type = DisplayString
_SniPreInstallationVersion_Object = MibScalar
sniPreInstallationVersion = _SniPreInstallationVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 9),
    _SniPreInstallationVersion_Type()
)
sniPreInstallationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPreInstallationVersion.setStatus("mandatory")
_SniPreInstallationLanguage_Type = DisplayString
_SniPreInstallationLanguage_Object = MibScalar
sniPreInstallationLanguage = _SniPreInstallationLanguage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 7, 10),
    _SniPreInstallationLanguage_Type()
)
sniPreInstallationLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPreInstallationLanguage.setStatus("mandatory")
_SniSoftware_Object = MibTable
sniSoftware = _SniSoftware_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 8)
)
if mibBuilder.loadTexts:
    sniSoftware.setStatus("mandatory")
_SniSoftwareEntry_Object = MibTableRow
sniSoftwareEntry = _SniSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 8, 1)
)
sniSoftwareEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniSoftwareIndex"),
)
if mibBuilder.loadTexts:
    sniSoftwareEntry.setStatus("mandatory")
_SniSoftwareIndex_Type = Integer32
_SniSoftwareIndex_Object = MibTableColumn
sniSoftwareIndex = _SniSoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 8, 1, 1),
    _SniSoftwareIndex_Type()
)
sniSoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSoftwareIndex.setStatus("mandatory")
_SniSoftwareName_Type = DisplayString
_SniSoftwareName_Object = MibTableColumn
sniSoftwareName = _SniSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 8, 1, 2),
    _SniSoftwareName_Type()
)
sniSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSoftwareName.setStatus("mandatory")
_SniSoftwareVersion_Type = DisplayString
_SniSoftwareVersion_Object = MibTableColumn
sniSoftwareVersion = _SniSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 8, 1, 3),
    _SniSoftwareVersion_Type()
)
sniSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSoftwareVersion.setStatus("mandatory")
_SniInstallationDirectory_Type = DisplayString
_SniInstallationDirectory_Object = MibTableColumn
sniInstallationDirectory = _SniInstallationDirectory_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 8, 1, 4),
    _SniInstallationDirectory_Type()
)
sniInstallationDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInstallationDirectory.setStatus("mandatory")


class _SniAtPreInstallTime_Type(Integer32):
    """Custom type sniAtPreInstallTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniAtPreInstallTime_Type.__name__ = "Integer32"
_SniAtPreInstallTime_Object = MibTableColumn
sniAtPreInstallTime = _SniAtPreInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 8, 1, 5),
    _SniAtPreInstallTime_Type()
)
sniAtPreInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAtPreInstallTime.setStatus("mandatory")
_SniVersion_Type = DisplayString
_SniVersion_Object = MibTableColumn
sniVersion = _SniVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 8, 1, 6),
    _SniVersion_Type()
)
sniVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniVersion.setStatus("mandatory")
_SniHardware_Object = MibTable
sniHardware = _SniHardware_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 10)
)
if mibBuilder.loadTexts:
    sniHardware.setStatus("mandatory")
_SniHardwareEntry_Object = MibTableRow
sniHardwareEntry = _SniHardwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 10, 1)
)
sniHardwareEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniHardwareIndex"),
)
if mibBuilder.loadTexts:
    sniHardwareEntry.setStatus("mandatory")
_SniHardwareIndex_Type = Integer32
_SniHardwareIndex_Object = MibTableColumn
sniHardwareIndex = _SniHardwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 10, 1, 1),
    _SniHardwareIndex_Type()
)
sniHardwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniHardwareIndex.setStatus("mandatory")
_SniHardwareName_Type = DisplayString
_SniHardwareName_Object = MibTableColumn
sniHardwareName = _SniHardwareName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 10, 1, 2),
    _SniHardwareName_Type()
)
sniHardwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniHardwareName.setStatus("mandatory")
_SniDriverDirectory_Type = DisplayString
_SniDriverDirectory_Object = MibTableColumn
sniDriverDirectory = _SniDriverDirectory_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 10, 1, 3),
    _SniDriverDirectory_Type()
)
sniDriverDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDriverDirectory.setStatus("mandatory")
_SniLogicalDrives_Object = MibTable
sniLogicalDrives = _SniLogicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12)
)
if mibBuilder.loadTexts:
    sniLogicalDrives.setStatus("mandatory")
_SniLogicalDrivesEntry_Object = MibTableRow
sniLogicalDrivesEntry = _SniLogicalDrivesEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1)
)
sniLogicalDrivesEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniDriveletter"),
)
if mibBuilder.loadTexts:
    sniLogicalDrivesEntry.setStatus("mandatory")
_SniDriveletter_Type = DisplayString
_SniDriveletter_Object = MibTableColumn
sniDriveletter = _SniDriveletter_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 1),
    _SniDriveletter_Type()
)
sniDriveletter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDriveletter.setStatus("mandatory")


class _SniLogicalDriveType_Type(Integer32):
    """Custom type sniLogicalDriveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("e-cd-rom", 6),
          ("e-disk-array", 9),
          ("e-floppy-disk", 7),
          ("e-harddisk", 3),
          ("e-ramdrive", 8),
          ("e-remote", 5),
          ("e-removable-disk", 4),
          ("e-unknown", 0))
    )


_SniLogicalDriveType_Type.__name__ = "Integer32"
_SniLogicalDriveType_Object = MibTableColumn
sniLogicalDriveType = _SniLogicalDriveType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 2),
    _SniLogicalDriveType_Type()
)
sniLogicalDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDriveType.setStatus("mandatory")
_SniVolumename_Type = DisplayString
_SniVolumename_Object = MibTableColumn
sniVolumename = _SniVolumename_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 3),
    _SniVolumename_Type()
)
sniVolumename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniVolumename.setStatus("mandatory")
_SniLogicalDriveSizekB_Type = Integer32
_SniLogicalDriveSizekB_Object = MibTableColumn
sniLogicalDriveSizekB = _SniLogicalDriveSizekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 4),
    _SniLogicalDriveSizekB_Type()
)
sniLogicalDriveSizekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDriveSizekB.setStatus("mandatory")
_SniLogicalDriveFreeSpacekB_Type = Integer32
_SniLogicalDriveFreeSpacekB_Object = MibTableColumn
sniLogicalDriveFreeSpacekB = _SniLogicalDriveFreeSpacekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 5),
    _SniLogicalDriveFreeSpacekB_Type()
)
sniLogicalDriveFreeSpacekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDriveFreeSpacekB.setStatus("mandatory")
_SniLogicalDriveSectorSizeByte_Type = Integer32
_SniLogicalDriveSectorSizeByte_Object = MibTableColumn
sniLogicalDriveSectorSizeByte = _SniLogicalDriveSectorSizeByte_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 6),
    _SniLogicalDriveSectorSizeByte_Type()
)
sniLogicalDriveSectorSizeByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDriveSectorSizeByte.setStatus("mandatory")
_SniClusterSizeByte_Type = Integer32
_SniClusterSizeByte_Object = MibTableColumn
sniClusterSizeByte = _SniClusterSizeByte_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 7),
    _SniClusterSizeByte_Type()
)
sniClusterSizeByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniClusterSizeByte.setStatus("mandatory")
_SniSectorsPerCluster_Type = Integer32
_SniSectorsPerCluster_Object = MibTableColumn
sniSectorsPerCluster = _SniSectorsPerCluster_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 8),
    _SniSectorsPerCluster_Type()
)
sniSectorsPerCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSectorsPerCluster.setStatus("mandatory")
_SniClusters_Type = Integer32
_SniClusters_Object = MibTableColumn
sniClusters = _SniClusters_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 9),
    _SniClusters_Type()
)
sniClusters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniClusters.setStatus("mandatory")
_SniSectors_Type = Integer32
_SniSectors_Object = MibTableColumn
sniSectors = _SniSectors_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 10),
    _SniSectors_Type()
)
sniSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSectors.setStatus("mandatory")
_SniNetworkpath_Type = DisplayString
_SniNetworkpath_Object = MibTableColumn
sniNetworkpath = _SniNetworkpath_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 11),
    _SniNetworkpath_Type()
)
sniNetworkpath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNetworkpath.setStatus("mandatory")
_SniLogicalDrivePartitionName_Type = DisplayString
_SniLogicalDrivePartitionName_Object = MibTableColumn
sniLogicalDrivePartitionName = _SniLogicalDrivePartitionName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 12),
    _SniLogicalDrivePartitionName_Type()
)
sniLogicalDrivePartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDrivePartitionName.setStatus("mandatory")
_SniLogicalDrivePartitionSizekB_Type = Integer32
_SniLogicalDrivePartitionSizekB_Object = MibTableColumn
sniLogicalDrivePartitionSizekB = _SniLogicalDrivePartitionSizekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 13),
    _SniLogicalDrivePartitionSizekB_Type()
)
sniLogicalDrivePartitionSizekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDrivePartitionSizekB.setStatus("mandatory")
_SniLogicalDrivePartitionFreeSpacekB_Type = Integer32
_SniLogicalDrivePartitionFreeSpacekB_Object = MibTableColumn
sniLogicalDrivePartitionFreeSpacekB = _SniLogicalDrivePartitionFreeSpacekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 14),
    _SniLogicalDrivePartitionFreeSpacekB_Type()
)
sniLogicalDrivePartitionFreeSpacekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDrivePartitionFreeSpacekB.setStatus("mandatory")
_SniLogicalDrivePartitionLabel_Type = DisplayString
_SniLogicalDrivePartitionLabel_Object = MibTableColumn
sniLogicalDrivePartitionLabel = _SniLogicalDrivePartitionLabel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 15),
    _SniLogicalDrivePartitionLabel_Type()
)
sniLogicalDrivePartitionLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDrivePartitionLabel.setStatus("mandatory")


class _SniLogicalDrivePartitionFilesystem_Type(Integer32):
    """Custom type sniLogicalDrivePartitionFilesystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("e-cdfs", 17),
          ("e-fat", 3),
          ("e-fat32", 18),
          ("e-ffs", 14),
          ("e-hfs", 8),
          ("e-hpfs", 4),
          ("e-mfs", 7),
          ("e-netware286", 15),
          ("e-netware386", 16),
          ("e-ntfs", 5),
          ("e-ofs", 6),
          ("e-s5", 11),
          ("e-s52k", 12),
          ("e-sfs", 10),
          ("e-ufs", 13),
          ("e-unknown", 0),
          ("e-vxfs", 9))
    )


_SniLogicalDrivePartitionFilesystem_Type.__name__ = "Integer32"
_SniLogicalDrivePartitionFilesystem_Object = MibTableColumn
sniLogicalDrivePartitionFilesystem = _SniLogicalDrivePartitionFilesystem_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 16),
    _SniLogicalDrivePartitionFilesystem_Type()
)
sniLogicalDrivePartitionFilesystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDrivePartitionFilesystem.setStatus("mandatory")


class _SniLogicalDrivePartitionCompressed_Type(Integer32):
    """Custom type sniLogicalDrivePartitionCompressed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniLogicalDrivePartitionCompressed_Type.__name__ = "Integer32"
_SniLogicalDrivePartitionCompressed_Object = MibTableColumn
sniLogicalDrivePartitionCompressed = _SniLogicalDrivePartitionCompressed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 17),
    _SniLogicalDrivePartitionCompressed_Type()
)
sniLogicalDrivePartitionCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDrivePartitionCompressed.setStatus("mandatory")


class _SniLogicalDrivePartitionEncrypted_Type(Integer32):
    """Custom type sniLogicalDrivePartitionEncrypted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniLogicalDrivePartitionEncrypted_Type.__name__ = "Integer32"
_SniLogicalDrivePartitionEncrypted_Object = MibTableColumn
sniLogicalDrivePartitionEncrypted = _SniLogicalDrivePartitionEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 18),
    _SniLogicalDrivePartitionEncrypted_Type()
)
sniLogicalDrivePartitionEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDrivePartitionEncrypted.setStatus("mandatory")


class _SniLogicalDrivePartitionActive_Type(Integer32):
    """Custom type sniLogicalDrivePartitionActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniLogicalDrivePartitionActive_Type.__name__ = "Integer32"
_SniLogicalDrivePartitionActive_Object = MibTableColumn
sniLogicalDrivePartitionActive = _SniLogicalDrivePartitionActive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 19),
    _SniLogicalDrivePartitionActive_Type()
)
sniLogicalDrivePartitionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDrivePartitionActive.setStatus("mandatory")


class _SniLogicalDrivePartitionBootable_Type(Integer32):
    """Custom type sniLogicalDrivePartitionBootable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniLogicalDrivePartitionBootable_Type.__name__ = "Integer32"
_SniLogicalDrivePartitionBootable_Object = MibTableColumn
sniLogicalDrivePartitionBootable = _SniLogicalDrivePartitionBootable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 12, 1, 20),
    _SniLogicalDrivePartitionBootable_Type()
)
sniLogicalDrivePartitionBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLogicalDrivePartitionBootable.setStatus("mandatory")
_SniPhysicalDrives_Object = MibTable
sniPhysicalDrives = _SniPhysicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14)
)
if mibBuilder.loadTexts:
    sniPhysicalDrives.setStatus("mandatory")
_SniPhysicalDrivesEntry_Object = MibTableRow
sniPhysicalDrivesEntry = _SniPhysicalDrivesEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1)
)
sniPhysicalDrivesEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniPhysicalDrive"),
)
if mibBuilder.loadTexts:
    sniPhysicalDrivesEntry.setStatus("mandatory")
_SniPhysicalDrive_Type = Integer32
_SniPhysicalDrive_Object = MibTableColumn
sniPhysicalDrive = _SniPhysicalDrive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 1),
    _SniPhysicalDrive_Type()
)
sniPhysicalDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalDrive.setStatus("mandatory")
_SniPhysicalDriveName_Type = DisplayString
_SniPhysicalDriveName_Object = MibTableColumn
sniPhysicalDriveName = _SniPhysicalDriveName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 2),
    _SniPhysicalDriveName_Type()
)
sniPhysicalDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalDriveName.setStatus("mandatory")


class _SniPhysicalDriveType_Type(Integer32):
    """Custom type sniPhysicalDriveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("e-bernoulli-disk", 10),
          ("e-cd", 8),
          ("e-flash-disk", 9),
          ("e-floppydisk", 4),
          ("e-harddisk", 3),
          ("e-optical-fd", 11),
          ("e-optical-rom", 5),
          ("e-optical-rw", 7),
          ("e-optical-worm", 6),
          ("e-other", 1),
          ("e-unknown", 0))
    )


_SniPhysicalDriveType_Type.__name__ = "Integer32"
_SniPhysicalDriveType_Object = MibTableColumn
sniPhysicalDriveType = _SniPhysicalDriveType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 3),
    _SniPhysicalDriveType_Type()
)
sniPhysicalDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalDriveType.setStatus("mandatory")


class _SniInterface_Type(Integer32):
    """Custom type sniInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("e-atapi", 17),
          ("e-cmd", 6),
          ("e-dssi", 9),
          ("e-eide", 15),
          ("e-esdi", 4),
          ("e-fd", 13),
          ("e-hippi", 11),
          ("e-ide", 5),
          ("e-ide-eide", 16),
          ("e-ipi", 7),
          ("e-parallel", 10),
          ("e-pcmcia", 14),
          ("e-qic2", 12),
          ("e-scsi", 3),
          ("e-st506", 8),
          ("e-unknown", 0),
          ("e-usb", 18))
    )


_SniInterface_Type.__name__ = "Integer32"
_SniInterface_Object = MibTableColumn
sniInterface = _SniInterface_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 4),
    _SniInterface_Type()
)
sniInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInterface.setStatus("mandatory")


class _SniMediaLoaded_Type(Integer32):
    """Custom type sniMediaLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniMediaLoaded_Type.__name__ = "Integer32"
_SniMediaLoaded_Object = MibTableColumn
sniMediaLoaded = _SniMediaLoaded_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 5),
    _SniMediaLoaded_Type()
)
sniMediaLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMediaLoaded.setStatus("mandatory")


class _SniRemovableDrive_Type(Integer32):
    """Custom type sniRemovableDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniRemovableDrive_Type.__name__ = "Integer32"
_SniRemovableDrive_Object = MibTableColumn
sniRemovableDrive = _SniRemovableDrive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 6),
    _SniRemovableDrive_Type()
)
sniRemovableDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniRemovableDrive.setStatus("mandatory")


class _SniRemovableMedia_Type(Integer32):
    """Custom type sniRemovableMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniRemovableMedia_Type.__name__ = "Integer32"
_SniRemovableMedia_Object = MibTableColumn
sniRemovableMedia = _SniRemovableMedia_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 7),
    _SniRemovableMedia_Type()
)
sniRemovableMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniRemovableMedia.setStatus("mandatory")
_SniSCSIID_Type = Integer32
_SniSCSIID_Object = MibTableColumn
sniSCSIID = _SniSCSIID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 8),
    _SniSCSIID_Type()
)
sniSCSIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSCSIID.setStatus("mandatory")
_SniSCSILUN_Type = Integer32
_SniSCSILUN_Object = MibTableColumn
sniSCSILUN = _SniSCSILUN_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 9),
    _SniSCSILUN_Type()
)
sniSCSILUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSCSILUN.setStatus("mandatory")
_SniPhysicalDriveTotalSpacekB_Type = Integer32
_SniPhysicalDriveTotalSpacekB_Object = MibTableColumn
sniPhysicalDriveTotalSpacekB = _SniPhysicalDriveTotalSpacekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 10),
    _SniPhysicalDriveTotalSpacekB_Type()
)
sniPhysicalDriveTotalSpacekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalDriveTotalSpacekB.setStatus("mandatory")
_SniTracks_Type = Integer32
_SniTracks_Object = MibTableColumn
sniTracks = _SniTracks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 11),
    _SniTracks_Type()
)
sniTracks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTracks.setStatus("mandatory")
_SniSectorsPerTrack_Type = Integer32
_SniSectorsPerTrack_Object = MibTableColumn
sniSectorsPerTrack = _SniSectorsPerTrack_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 12),
    _SniSectorsPerTrack_Type()
)
sniSectorsPerTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSectorsPerTrack.setStatus("mandatory")
_SniHeads_Type = Integer32
_SniHeads_Object = MibTableColumn
sniHeads = _SniHeads_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 13),
    _SniHeads_Type()
)
sniHeads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniHeads.setStatus("mandatory")
_SniWritePreComp_Type = Integer32
_SniWritePreComp_Object = MibTableColumn
sniWritePreComp = _SniWritePreComp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 14),
    _SniWritePreComp_Type()
)
sniWritePreComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWritePreComp.setStatus("mandatory")
_SniLandingZone_Type = Integer32
_SniLandingZone_Object = MibTableColumn
sniLandingZone = _SniLandingZone_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 15),
    _SniLandingZone_Type()
)
sniLandingZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLandingZone.setStatus("mandatory")
_SniPhysicalDriveSectorSizeByte_Type = Integer32
_SniPhysicalDriveSectorSizeByte_Object = MibTableColumn
sniPhysicalDriveSectorSizeByte = _SniPhysicalDriveSectorSizeByte_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 16),
    _SniPhysicalDriveSectorSizeByte_Type()
)
sniPhysicalDriveSectorSizeByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalDriveSectorSizeByte.setStatus("mandatory")
_SniBadBlocks_Type = Integer32
_SniBadBlocks_Object = MibTableColumn
sniBadBlocks = _SniBadBlocks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 17),
    _SniBadBlocks_Type()
)
sniBadBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBadBlocks.setStatus("mandatory")
_SniPhysicalDrivePartitions_Type = Integer32
_SniPhysicalDrivePartitions_Object = MibTableColumn
sniPhysicalDrivePartitions = _SniPhysicalDrivePartitions_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 18),
    _SniPhysicalDrivePartitions_Type()
)
sniPhysicalDrivePartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalDrivePartitions.setStatus("mandatory")


class _SniPhysicalDriveLocation_Type(Integer32):
    """Custom type sniPhysicalDriveLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-external", 4),
          ("e-internal", 3),
          ("e-unknown", 0))
    )


_SniPhysicalDriveLocation_Type.__name__ = "Integer32"
_SniPhysicalDriveLocation_Object = MibTableColumn
sniPhysicalDriveLocation = _SniPhysicalDriveLocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 19),
    _SniPhysicalDriveLocation_Type()
)
sniPhysicalDriveLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalDriveLocation.setStatus("mandatory")


class _SniSMART_Type(Integer32):
    """Custom type sniSMART based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e-critical", 5),
          ("e-ok", 3),
          ("e-unknown", 0),
          ("e-warning", 4))
    )


_SniSMART_Type.__name__ = "Integer32"
_SniSMART_Object = MibTableColumn
sniSMART = _SniSMART_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 20),
    _SniSMART_Type()
)
sniSMART.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSMART.setStatus("mandatory")
_SniSMARTCrossreference_Type = Integer32
_SniSMARTCrossreference_Object = MibTableColumn
sniSMARTCrossreference = _SniSMARTCrossreference_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 14, 1, 21),
    _SniSMARTCrossreference_Type()
)
sniSMARTCrossreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSMARTCrossreference.setStatus("mandatory")
_SniPartitions_Object = MibTable
sniPartitions = _SniPartitions_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16)
)
if mibBuilder.loadTexts:
    sniPartitions.setStatus("mandatory")
_SniPartitionsEntry_Object = MibTableRow
sniPartitionsEntry = _SniPartitionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1)
)
sniPartitionsEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniPhysicalDriveIndex"),
    (0, "DESKSNMP-MIB", "sniPartitionIndex"),
)
if mibBuilder.loadTexts:
    sniPartitionsEntry.setStatus("mandatory")
_SniPhysicalDriveIndex_Type = Integer32
_SniPhysicalDriveIndex_Object = MibTableColumn
sniPhysicalDriveIndex = _SniPhysicalDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 1),
    _SniPhysicalDriveIndex_Type()
)
sniPhysicalDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalDriveIndex.setStatus("mandatory")
_SniPartitionIndex_Type = Integer32
_SniPartitionIndex_Object = MibTableColumn
sniPartitionIndex = _SniPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 2),
    _SniPartitionIndex_Type()
)
sniPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPartitionIndex.setStatus("mandatory")
_SniPartitionName_Type = DisplayString
_SniPartitionName_Object = MibTableColumn
sniPartitionName = _SniPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 3),
    _SniPartitionName_Type()
)
sniPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPartitionName.setStatus("mandatory")
_SniPartitionSizekB_Type = Integer32
_SniPartitionSizekB_Object = MibTableColumn
sniPartitionSizekB = _SniPartitionSizekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 4),
    _SniPartitionSizekB_Type()
)
sniPartitionSizekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPartitionSizekB.setStatus("mandatory")
_SniPartitionFreeSpacekB_Type = Integer32
_SniPartitionFreeSpacekB_Object = MibTableColumn
sniPartitionFreeSpacekB = _SniPartitionFreeSpacekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 5),
    _SniPartitionFreeSpacekB_Type()
)
sniPartitionFreeSpacekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPartitionFreeSpacekB.setStatus("mandatory")
_SniLabel_Type = DisplayString
_SniLabel_Object = MibTableColumn
sniLabel = _SniLabel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 6),
    _SniLabel_Type()
)
sniLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLabel.setStatus("mandatory")


class _SniPartitionFilesystem_Type(Integer32):
    """Custom type sniPartitionFilesystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("e-cdfs", 17),
          ("e-fat", 3),
          ("e-fat32", 18),
          ("e-ffs", 14),
          ("e-hfs", 8),
          ("e-hpfs", 4),
          ("e-mfs", 7),
          ("e-netware286", 15),
          ("e-netware386", 16),
          ("e-ntfs", 5),
          ("e-ofs", 6),
          ("e-s5", 11),
          ("e-s52k", 12),
          ("e-sfs", 10),
          ("e-ufs", 13),
          ("e-unknown", 0),
          ("e-vxfs", 9))
    )


_SniPartitionFilesystem_Type.__name__ = "Integer32"
_SniPartitionFilesystem_Object = MibTableColumn
sniPartitionFilesystem = _SniPartitionFilesystem_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 7),
    _SniPartitionFilesystem_Type()
)
sniPartitionFilesystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPartitionFilesystem.setStatus("mandatory")


class _SniPartitionCompressed_Type(Integer32):
    """Custom type sniPartitionCompressed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPartitionCompressed_Type.__name__ = "Integer32"
_SniPartitionCompressed_Object = MibTableColumn
sniPartitionCompressed = _SniPartitionCompressed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 8),
    _SniPartitionCompressed_Type()
)
sniPartitionCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPartitionCompressed.setStatus("mandatory")


class _SniPartitionEncrypted_Type(Integer32):
    """Custom type sniPartitionEncrypted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPartitionEncrypted_Type.__name__ = "Integer32"
_SniPartitionEncrypted_Object = MibTableColumn
sniPartitionEncrypted = _SniPartitionEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 9),
    _SniPartitionEncrypted_Type()
)
sniPartitionEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPartitionEncrypted.setStatus("mandatory")


class _SniPartitionActive_Type(Integer32):
    """Custom type sniPartitionActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPartitionActive_Type.__name__ = "Integer32"
_SniPartitionActive_Object = MibTableColumn
sniPartitionActive = _SniPartitionActive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 10),
    _SniPartitionActive_Type()
)
sniPartitionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPartitionActive.setStatus("mandatory")


class _SniPartitionBootable_Type(Integer32):
    """Custom type sniPartitionBootable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPartitionBootable_Type.__name__ = "Integer32"
_SniPartitionBootable_Object = MibTableColumn
sniPartitionBootable = _SniPartitionBootable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 16, 1, 11),
    _SniPartitionBootable_Type()
)
sniPartitionBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPartitionBootable.setStatus("mandatory")
_SniMainboard_ObjectIdentity = ObjectIdentity
sniMainboard = _SniMainboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18)
)
_SniMainboardManufacturer_Type = DisplayString
_SniMainboardManufacturer_Object = MibScalar
sniMainboardManufacturer = _SniMainboardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 1),
    _SniMainboardManufacturer_Type()
)
sniMainboardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMainboardManufacturer.setStatus("mandatory")
_SniMainboardName_Type = DisplayString
_SniMainboardName_Object = MibScalar
sniMainboardName = _SniMainboardName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 2),
    _SniMainboardName_Type()
)
sniMainboardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMainboardName.setStatus("mandatory")
_SniMainboardVersion_Type = DisplayString
_SniMainboardVersion_Object = MibScalar
sniMainboardVersion = _SniMainboardVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 3),
    _SniMainboardVersion_Type()
)
sniMainboardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMainboardVersion.setStatus("mandatory")
_SniProductID_Type = DisplayString
_SniProductID_Object = MibScalar
sniProductID = _SniProductID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 4),
    _SniProductID_Type()
)
sniProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProductID.setStatus("mandatory")
_SniProductType_Type = DisplayString
_SniProductType_Object = MibScalar
sniProductType = _SniProductType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 5),
    _SniProductType_Type()
)
sniProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProductType.setStatus("mandatory")
_SniMaxMemoryMB_Type = Integer32
_SniMaxMemoryMB_Object = MibScalar
sniMaxMemoryMB = _SniMaxMemoryMB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 6),
    _SniMaxMemoryMB_Type()
)
sniMaxMemoryMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaxMemoryMB.setStatus("mandatory")
_SniUsedMemorySlots_Type = Integer32
_SniUsedMemorySlots_Object = MibScalar
sniUsedMemorySlots = _SniUsedMemorySlots_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 7),
    _SniUsedMemorySlots_Type()
)
sniUsedMemorySlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniUsedMemorySlots.setStatus("mandatory")
_SniNumberMemorySlots_Type = Integer32
_SniNumberMemorySlots_Object = MibScalar
sniNumberMemorySlots = _SniNumberMemorySlots_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 8),
    _SniNumberMemorySlots_Type()
)
sniNumberMemorySlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNumberMemorySlots.setStatus("mandatory")


class _SniOnBoardMouse_Type(Integer32):
    """Custom type sniOnBoardMouse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniOnBoardMouse_Type.__name__ = "Integer32"
_SniOnBoardMouse_Object = MibScalar
sniOnBoardMouse = _SniOnBoardMouse_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 9),
    _SniOnBoardMouse_Type()
)
sniOnBoardMouse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOnBoardMouse.setStatus("mandatory")


class _SniHarddiskAccelerator_Type(Integer32):
    """Custom type sniHarddiskAccelerator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniHarddiskAccelerator_Type.__name__ = "Integer32"
_SniHarddiskAccelerator_Object = MibScalar
sniHarddiskAccelerator = _SniHarddiskAccelerator_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 10),
    _SniHarddiskAccelerator_Type()
)
sniHarddiskAccelerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniHarddiskAccelerator.setStatus("mandatory")
_SniMainboardGSNumber_Type = DisplayString
_SniMainboardGSNumber_Object = MibScalar
sniMainboardGSNumber = _SniMainboardGSNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 11),
    _SniMainboardGSNumber_Type()
)
sniMainboardGSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMainboardGSNumber.setStatus("mandatory")
_SniMainboardVariant_Type = DisplayString
_SniMainboardVariant_Object = MibScalar
sniMainboardVariant = _SniMainboardVariant_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 18, 12),
    _SniMainboardVariant_Type()
)
sniMainboardVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMainboardVariant.setStatus("mandatory")
_SniMainboardProcessors_Object = MibTable
sniMainboardProcessors = _SniMainboardProcessors_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 19)
)
if mibBuilder.loadTexts:
    sniMainboardProcessors.setStatus("mandatory")
_SniMainboardProcessorsEntry_Object = MibTableRow
sniMainboardProcessorsEntry = _SniMainboardProcessorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 19, 1)
)
sniMainboardProcessorsEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniProcessorIndex"),
)
if mibBuilder.loadTexts:
    sniMainboardProcessorsEntry.setStatus("mandatory")
_SniProcessorIndex_Type = Integer32
_SniProcessorIndex_Object = MibTableColumn
sniProcessorIndex = _SniProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 19, 1, 1),
    _SniProcessorIndex_Type()
)
sniProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProcessorIndex.setStatus("mandatory")


class _SniProcessorType_Type(Integer32):
    """Custom type sniProcessorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("e-co-processor", 4),
          ("e-cpu", 3),
          ("e-graphic-processor", 6),
          ("e-sound-processor", 5),
          ("e-unknown", 0))
    )


_SniProcessorType_Type.__name__ = "Integer32"
_SniProcessorType_Object = MibTableColumn
sniProcessorType = _SniProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 19, 1, 2),
    _SniProcessorType_Type()
)
sniProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProcessorType.setStatus("mandatory")
_SniFamily_Type = DisplayString
_SniFamily_Object = MibTableColumn
sniFamily = _SniFamily_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 19, 1, 3),
    _SniFamily_Type()
)
sniFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniFamily.setStatus("mandatory")
_SniProcessorVersion_Type = DisplayString
_SniProcessorVersion_Object = MibTableColumn
sniProcessorVersion = _SniProcessorVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 19, 1, 4),
    _SniProcessorVersion_Type()
)
sniProcessorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProcessorVersion.setStatus("mandatory")
_SniCurrentProcSpeedMHz_Type = Integer32
_SniCurrentProcSpeedMHz_Object = MibTableColumn
sniCurrentProcSpeedMHz = _SniCurrentProcSpeedMHz_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 19, 1, 5),
    _SniCurrentProcSpeedMHz_Type()
)
sniCurrentProcSpeedMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCurrentProcSpeedMHz.setStatus("mandatory")
_SniMaxBoardSpeedMHz_Type = Integer32
_SniMaxBoardSpeedMHz_Object = MibTableColumn
sniMaxBoardSpeedMHz = _SniMaxBoardSpeedMHz_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 19, 1, 6),
    _SniMaxBoardSpeedMHz_Type()
)
sniMaxBoardSpeedMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaxBoardSpeedMHz.setStatus("mandatory")
_SniProcessorSerialnumber_Type = DisplayString
_SniProcessorSerialnumber_Object = MibTableColumn
sniProcessorSerialnumber = _SniProcessorSerialnumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 19, 1, 7),
    _SniProcessorSerialnumber_Type()
)
sniProcessorSerialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProcessorSerialnumber.setStatus("mandatory")
_SniMainboardCache_Object = MibTable
sniMainboardCache = _SniMainboardCache_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21)
)
if mibBuilder.loadTexts:
    sniMainboardCache.setStatus("mandatory")
_SniMainboardCacheEntry_Object = MibTableRow
sniMainboardCacheEntry = _SniMainboardCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1)
)
sniMainboardCacheEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniCacheIndex"),
)
if mibBuilder.loadTexts:
    sniMainboardCacheEntry.setStatus("mandatory")
_SniCacheIndex_Type = Integer32
_SniCacheIndex_Object = MibTableColumn
sniCacheIndex = _SniCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 1),
    _SniCacheIndex_Type()
)
sniCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCacheIndex.setStatus("mandatory")


class _SniCacheActive_Type(Integer32):
    """Custom type sniCacheActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniCacheActive_Type.__name__ = "Integer32"
_SniCacheActive_Object = MibTableColumn
sniCacheActive = _SniCacheActive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 2),
    _SniCacheActive_Type()
)
sniCacheActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCacheActive.setStatus("mandatory")
_SniCacheSizekB_Type = Integer32
_SniCacheSizekB_Object = MibTableColumn
sniCacheSizekB = _SniCacheSizekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 3),
    _SniCacheSizekB_Type()
)
sniCacheSizekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCacheSizekB.setStatus("mandatory")
_SniMaximumSizekB_Type = Integer32
_SniMaximumSizekB_Object = MibTableColumn
sniMaximumSizekB = _SniMaximumSizekB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 4),
    _SniMaximumSizekB_Type()
)
sniMaximumSizekB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaximumSizekB.setStatus("mandatory")
_SniLevel_Type = Integer32
_SniLevel_Object = MibTableColumn
sniLevel = _SniLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 5),
    _SniLevel_Type()
)
sniLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLevel.setStatus("mandatory")


class _SniCacheBurstType_Type(Integer32):
    """Custom type sniCacheBurstType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("e-burst", 2),
          ("e-burst-nonburst", 3),
          ("e-burst-nonburst-pipelinedburst", 7),
          ("e-burst-pipelinedburst", 6),
          ("e-non-burst", 1),
          ("e-nonburst-pipelinedburst", 5),
          ("e-pipelinedburst", 4),
          ("e-unknown", 0))
    )


_SniCacheBurstType_Type.__name__ = "Integer32"
_SniCacheBurstType_Object = MibTableColumn
sniCacheBurstType = _SniCacheBurstType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 6),
    _SniCacheBurstType_Type()
)
sniCacheBurstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCacheBurstType.setStatus("mandatory")


class _SniCacheSynchron_Type(Integer32):
    """Custom type sniCacheSynchron based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 2),
          ("e-unknown", 0),
          ("e-yes", 1))
    )


_SniCacheSynchron_Type.__name__ = "Integer32"
_SniCacheSynchron_Object = MibTableColumn
sniCacheSynchron = _SniCacheSynchron_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 7),
    _SniCacheSynchron_Type()
)
sniCacheSynchron.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCacheSynchron.setStatus("mandatory")


class _SniCacheSRAM_Type(Integer32):
    """Custom type sniCacheSRAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 128))
    )


_SniCacheSRAM_Type.__name__ = "Integer32"
_SniCacheSRAM_Object = MibTableColumn
sniCacheSRAM = _SniCacheSRAM_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 8),
    _SniCacheSRAM_Type()
)
sniCacheSRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCacheSRAM.setStatus("mandatory")


class _SniBurstTypeSupport_Type(Integer32):
    """Custom type sniBurstTypeSupport based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("e-burst", 2),
          ("e-burst-nonburst", 3),
          ("e-burst-nonburst-pipelinedburst", 7),
          ("e-burst-pipelinedburst", 6),
          ("e-non-burst", 1),
          ("e-nonburst-pipelinedburst", 5),
          ("e-pipelinedburst", 4),
          ("e-unknown", 0))
    )


_SniBurstTypeSupport_Type.__name__ = "Integer32"
_SniBurstTypeSupport_Object = MibTableColumn
sniBurstTypeSupport = _SniBurstTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 9),
    _SniBurstTypeSupport_Type()
)
sniBurstTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBurstTypeSupport.setStatus("mandatory")


class _SniSynchronSupport_Type(Integer32):
    """Custom type sniSynchronSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e-asynchron", 2),
          ("e-synchron", 1),
          ("e-synchron-asynchron", 3),
          ("e-unknown", 0))
    )


_SniSynchronSupport_Type.__name__ = "Integer32"
_SniSynchronSupport_Object = MibTableColumn
sniSynchronSupport = _SniSynchronSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 10),
    _SniSynchronSupport_Type()
)
sniSynchronSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSynchronSupport.setStatus("mandatory")


class _SniSRAMSupport_Type(Integer32):
    """Custom type sniSRAMSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 128))
    )


_SniSRAMSupport_Type.__name__ = "Integer32"
_SniSRAMSupport_Object = MibTableColumn
sniSRAMSupport = _SniSRAMSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 11),
    _SniSRAMSupport_Type()
)
sniSRAMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSRAMSupport.setStatus("mandatory")


class _SniWriteThrough_Type(Integer32):
    """Custom type sniWriteThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniWriteThrough_Type.__name__ = "Integer32"
_SniWriteThrough_Object = MibTableColumn
sniWriteThrough = _SniWriteThrough_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 12),
    _SniWriteThrough_Type()
)
sniWriteThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWriteThrough.setStatus("mandatory")


class _SniWriteBack_Type(Integer32):
    """Custom type sniWriteBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniWriteBack_Type.__name__ = "Integer32"
_SniWriteBack_Object = MibTableColumn
sniWriteBack = _SniWriteBack_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 13),
    _SniWriteBack_Type()
)
sniWriteBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWriteBack.setStatus("mandatory")


class _SniDataCache_Type(Integer32):
    """Custom type sniDataCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniDataCache_Type.__name__ = "Integer32"
_SniDataCache_Object = MibTableColumn
sniDataCache = _SniDataCache_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 14),
    _SniDataCache_Type()
)
sniDataCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDataCache.setStatus("mandatory")


class _SniInstructionCache_Type(Integer32):
    """Custom type sniInstructionCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniInstructionCache_Type.__name__ = "Integer32"
_SniInstructionCache_Object = MibTableColumn
sniInstructionCache = _SniInstructionCache_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 15),
    _SniInstructionCache_Type()
)
sniInstructionCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInstructionCache.setStatus("mandatory")


class _SniInternal_Type(Integer32):
    """Custom type sniInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniInternal_Type.__name__ = "Integer32"
_SniInternal_Object = MibTableColumn
sniInternal = _SniInternal_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 16),
    _SniInternal_Type()
)
sniInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInternal.setStatus("mandatory")


class _SniInSocket_Type(Integer32):
    """Custom type sniInSocket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniInSocket_Type.__name__ = "Integer32"
_SniInSocket_Object = MibTableColumn
sniInSocket = _SniInSocket_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 21, 1, 17),
    _SniInSocket_Type()
)
sniInSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInSocket.setStatus("mandatory")
_SniMainboardPorts_Object = MibTable
sniMainboardPorts = _SniMainboardPorts_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 23)
)
if mibBuilder.loadTexts:
    sniMainboardPorts.setStatus("mandatory")
_SniMainboardPortsEntry_Object = MibTableRow
sniMainboardPortsEntry = _SniMainboardPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 23, 1)
)
sniMainboardPortsEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniPortIndex"),
)
if mibBuilder.loadTexts:
    sniMainboardPortsEntry.setStatus("mandatory")
_SniPortIndex_Type = Integer32
_SniPortIndex_Object = MibTableColumn
sniPortIndex = _SniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 23, 1, 1),
    _SniPortIndex_Type()
)
sniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPortIndex.setStatus("mandatory")
_SniPortName_Type = DisplayString
_SniPortName_Object = MibTableColumn
sniPortName = _SniPortName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 23, 1, 2),
    _SniPortName_Type()
)
sniPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPortName.setStatus("mandatory")


class _SniPortType_Type(Integer32):
    """Custom type sniPortType based on Integer32"""
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
              255,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("e-access-bus", 18),
          ("e-cd-rom-sound", 28),
          ("e-centronics", 2),
          ("e-centronics14", 29),
          ("e-centronics26", 30),
          ("e-circ-din8-female", 21),
          ("e-circ-din8-male", 20),
          ("e-db15-female", 7),
          ("e-db15-male", 6),
          ("e-db25-female", 5),
          ("e-db25-male", 4),
          ("e-db9-female", 9),
          ("e-db9-male", 8),
          ("e-dil25", 25),
          ("e-dil50", 26),
          ("e-dil68", 27),
          ("e-dil9", 24),
          ("e-fd", 23),
          ("e-firewire", 38),
          ("e-hp-hil", 17),
          ("e-ide", 22),
          ("e-infra-red", 16),
          ("e-micro-din", 14),
          ("e-mini-centronics", 3),
          ("e-mini-din", 13),
          ("e-mini-jack", 37),
          ("e-mini-scsi", 12),
          ("e-no-interface", 0),
          ("e-other", 2147483647),
          ("e-pc98", 31),
          ("e-pc98-hireso", 32),
          ("e-pc98full", 35),
          ("e-pc98note", 34),
          ("e-pch98", 33),
          ("e-proprietary", 1),
          ("e-ps2", 15),
          ("e-rj11", 10),
          ("e-rj45", 11),
          ("e-ssa-scsi", 19),
          ("e-unknown", 255),
          ("e-usb", 36))
    )


_SniPortType_Type.__name__ = "Integer32"
_SniPortType_Object = MibTableColumn
sniPortType = _SniPortType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 23, 1, 3),
    _SniPortType_Type()
)
sniPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPortType.setStatus("mandatory")
_SniIOBaseAddress_Type = Integer32
_SniIOBaseAddress_Object = MibTableColumn
sniIOBaseAddress = _SniIOBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 23, 1, 4),
    _SniIOBaseAddress_Type()
)
sniIOBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIOBaseAddress.setStatus("mandatory")
_SniPortIRQ_Type = Integer32
_SniPortIRQ_Object = MibTableColumn
sniPortIRQ = _SniPortIRQ_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 23, 1, 5),
    _SniPortIRQ_Type()
)
sniPortIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPortIRQ.setStatus("mandatory")


class _SniPortDMA_Type(Integer32):
    """Custom type sniPortDMA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPortDMA_Type.__name__ = "Integer32"
_SniPortDMA_Object = MibTableColumn
sniPortDMA = _SniPortDMA_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 23, 1, 6),
    _SniPortDMA_Type()
)
sniPortDMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPortDMA.setStatus("mandatory")
_SniMainboardSystemSlots_Object = MibTable
sniMainboardSystemSlots = _SniMainboardSystemSlots_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25)
)
if mibBuilder.loadTexts:
    sniMainboardSystemSlots.setStatus("mandatory")
_SniMainboardSystemSlotsEntry_Object = MibTableRow
sniMainboardSystemSlotsEntry = _SniMainboardSystemSlotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25, 1)
)
sniMainboardSystemSlotsEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniSystemSlotIndex"),
)
if mibBuilder.loadTexts:
    sniMainboardSystemSlotsEntry.setStatus("mandatory")
_SniSystemSlotIndex_Type = Integer32
_SniSystemSlotIndex_Object = MibTableColumn
sniSystemSlotIndex = _SniSystemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25, 1, 1),
    _SniSystemSlotIndex_Type()
)
sniSystemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSystemSlotIndex.setStatus("mandatory")
_SniSystemSlotName_Type = DisplayString
_SniSystemSlotName_Object = MibTableColumn
sniSystemSlotName = _SniSystemSlotName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25, 1, 2),
    _SniSystemSlotName_Type()
)
sniSystemSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSystemSlotName.setStatus("mandatory")


class _SniSystemSlotType_Type(Integer32):
    """Custom type sniSystemSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("e-agp", 20),
          ("e-agp2x", 21),
          ("e-agp4x", 22),
          ("e-eisa", 5),
          ("e-isa", 3),
          ("e-mca", 4),
          ("e-memory-card", 11),
          ("e-nubus", 13),
          ("e-pc98-card", 19),
          ("e-pc98-localbus", 18),
          ("e-pc98c20", 15),
          ("e-pc98c24", 16),
          ("e-pc98e", 17),
          ("e-pci", 6),
          ("e-pci66", 14),
          ("e-pcmcia", 7),
          ("e-processor-card", 10),
          ("e-proprietary", 9),
          ("e-riser-card", 12),
          ("e-unknown", 0),
          ("e-vlb", 8))
    )


_SniSystemSlotType_Type.__name__ = "Integer32"
_SniSystemSlotType_Object = MibTableColumn
sniSystemSlotType = _SniSystemSlotType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25, 1, 3),
    _SniSystemSlotType_Type()
)
sniSystemSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSystemSlotType.setStatus("mandatory")
_SniNumber_Type = Integer32
_SniNumber_Object = MibTableColumn
sniNumber = _SniNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25, 1, 4),
    _SniNumber_Type()
)
sniNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNumber.setStatus("mandatory")


class _SniInUse_Type(Integer32):
    """Custom type sniInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniInUse_Type.__name__ = "Integer32"
_SniInUse_Object = MibTableColumn
sniInUse = _SniInUse_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25, 1, 5),
    _SniInUse_Type()
)
sniInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInUse.setStatus("mandatory")


class _SniBusWidth_Type(Integer32):
    """Custom type sniBusWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("e-128", 7),
          ("e-16", 4),
          ("e-32", 5),
          ("e-64", 6),
          ("e-8", 3),
          ("e-unknown", 0))
    )


_SniBusWidth_Type.__name__ = "Integer32"
_SniBusWidth_Object = MibTableColumn
sniBusWidth = _SniBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25, 1, 6),
    _SniBusWidth_Type()
)
sniBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBusWidth.setStatus("mandatory")


class _SniSlotLength_Type(Integer32):
    """Custom type sniSlotLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-full", 3),
          ("e-half", 4),
          ("e-unknown", 0))
    )


_SniSlotLength_Type.__name__ = "Integer32"
_SniSlotLength_Object = MibTableColumn
sniSlotLength = _SniSlotLength_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25, 1, 7),
    _SniSlotLength_Type()
)
sniSlotLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSlotLength.setStatus("mandatory")


class _SniSharedSlot_Type(Integer32):
    """Custom type sniSharedSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniSharedSlot_Type.__name__ = "Integer32"
_SniSharedSlot_Object = MibTableColumn
sniSharedSlot = _SniSharedSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 25, 1, 8),
    _SniSharedSlot_Type()
)
sniSharedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSharedSlot.setStatus("mandatory")
_SniMainboardOnboardDevices_Object = MibTable
sniMainboardOnboardDevices = _SniMainboardOnboardDevices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 27)
)
if mibBuilder.loadTexts:
    sniMainboardOnboardDevices.setStatus("mandatory")
_SniMainboardOnboardDevicesEntry_Object = MibTableRow
sniMainboardOnboardDevicesEntry = _SniMainboardOnboardDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 27, 1)
)
sniMainboardOnboardDevicesEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniOnboardDeviceIndex"),
)
if mibBuilder.loadTexts:
    sniMainboardOnboardDevicesEntry.setStatus("mandatory")
_SniOnboardDeviceIndex_Type = Integer32
_SniOnboardDeviceIndex_Object = MibTableColumn
sniOnboardDeviceIndex = _SniOnboardDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 27, 1, 1),
    _SniOnboardDeviceIndex_Type()
)
sniOnboardDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOnboardDeviceIndex.setStatus("mandatory")
_SniOnboardDeviceName_Type = DisplayString
_SniOnboardDeviceName_Object = MibTableColumn
sniOnboardDeviceName = _SniOnboardDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 27, 1, 2),
    _SniOnboardDeviceName_Type()
)
sniOnboardDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOnboardDeviceName.setStatus("mandatory")


class _SniOnboardDeviceType_Type(Integer32):
    """Custom type sniOnboardDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("e-ethernet-card", 5),
          ("e-graphic-card", 3),
          ("e-hd-accelerator", 9),
          ("e-mouse", 8),
          ("e-other", 1),
          ("e-scsi", 4),
          ("e-sni-chip", 10),
          ("e-sound-card", 7),
          ("e-tokenring-card", 6),
          ("e-unknown", 0))
    )


_SniOnboardDeviceType_Type.__name__ = "Integer32"
_SniOnboardDeviceType_Object = MibTableColumn
sniOnboardDeviceType = _SniOnboardDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 27, 1, 3),
    _SniOnboardDeviceType_Type()
)
sniOnboardDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOnboardDeviceType.setStatus("mandatory")


class _SniOnboardDeviceActive_Type(Integer32):
    """Custom type sniOnboardDeviceActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniOnboardDeviceActive_Type.__name__ = "Integer32"
_SniOnboardDeviceActive_Object = MibTableColumn
sniOnboardDeviceActive = _SniOnboardDeviceActive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 27, 1, 4),
    _SniOnboardDeviceActive_Type()
)
sniOnboardDeviceActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOnboardDeviceActive.setStatus("mandatory")
_SniMainboardMemory_Object = MibTable
sniMainboardMemory = _SniMainboardMemory_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29)
)
if mibBuilder.loadTexts:
    sniMainboardMemory.setStatus("mandatory")
_SniMainboardMemoryEntry_Object = MibTableRow
sniMainboardMemoryEntry = _SniMainboardMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1)
)
sniMainboardMemoryEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniMemoryControllerIndex"),
)
if mibBuilder.loadTexts:
    sniMainboardMemoryEntry.setStatus("mandatory")
_SniMemoryControllerIndex_Type = Integer32
_SniMemoryControllerIndex_Object = MibTableColumn
sniMemoryControllerIndex = _SniMemoryControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 1),
    _SniMemoryControllerIndex_Type()
)
sniMemoryControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryControllerIndex.setStatus("mandatory")
_SniNumberOfMemoryModules_Type = Integer32
_SniNumberOfMemoryModules_Object = MibTableColumn
sniNumberOfMemoryModules = _SniNumberOfMemoryModules_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 2),
    _SniNumberOfMemoryModules_Type()
)
sniNumberOfMemoryModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNumberOfMemoryModules.setStatus("mandatory")
_SniMaxNumberofModules_Type = Integer32
_SniMaxNumberofModules_Object = MibTableColumn
sniMaxNumberofModules = _SniMaxNumberofModules_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 3),
    _SniMaxNumberofModules_Type()
)
sniMaxNumberofModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaxNumberofModules.setStatus("mandatory")
_SniMaximumModuleSizeMB_Type = Integer32
_SniMaximumModuleSizeMB_Object = MibTableColumn
sniMaximumModuleSizeMB = _SniMaximumModuleSizeMB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 4),
    _SniMaximumModuleSizeMB_Type()
)
sniMaximumModuleSizeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaximumModuleSizeMB.setStatus("mandatory")


class _SniSupportedSpeeds_Type(Integer32):
    """Custom type sniSupportedSpeeds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("e-50-ns", 16),
          ("e-60-ns", 8),
          ("e-70-ns", 4),
          ("e-other", 0),
          ("e-unknown", 2))
    )


_SniSupportedSpeeds_Type.__name__ = "Integer32"
_SniSupportedSpeeds_Object = MibTableColumn
sniSupportedSpeeds = _SniSupportedSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 5),
    _SniSupportedSpeeds_Type()
)
sniSupportedSpeeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSupportedSpeeds.setStatus("mandatory")


class _SniErrorCorrectionECC_Type(Integer32):
    """Custom type sniErrorCorrectionECC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("e-double-bit", 5),
          ("e-no", 3),
          ("e-other", 8),
          ("e-scrubbing", 6),
          ("e-single-bit", 4),
          ("e-unknown", 0))
    )


_SniErrorCorrectionECC_Type.__name__ = "Integer32"
_SniErrorCorrectionECC_Object = MibTableColumn
sniErrorCorrectionECC = _SniErrorCorrectionECC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 6),
    _SniErrorCorrectionECC_Type()
)
sniErrorCorrectionECC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorCorrectionECC.setStatus("mandatory")


class _SniStandardSupport_Type(Integer32):
    """Custom type sniStandardSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 4))
    )


_SniStandardSupport_Type.__name__ = "Integer32"
_SniStandardSupport_Object = MibTableColumn
sniStandardSupport = _SniStandardSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 7),
    _SniStandardSupport_Type()
)
sniStandardSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniStandardSupport.setStatus("mandatory")


class _SniFastPageModeSupport_Type(Integer32):
    """Custom type sniFastPageModeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 8))
    )


_SniFastPageModeSupport_Type.__name__ = "Integer32"
_SniFastPageModeSupport_Object = MibTableColumn
sniFastPageModeSupport = _SniFastPageModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 8),
    _SniFastPageModeSupport_Type()
)
sniFastPageModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniFastPageModeSupport.setStatus("mandatory")


class _SniEDOSupport_Type(Integer32):
    """Custom type sniEDOSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 16))
    )


_SniEDOSupport_Type.__name__ = "Integer32"
_SniEDOSupport_Object = MibTableColumn
sniEDOSupport = _SniEDOSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 9),
    _SniEDOSupport_Type()
)
sniEDOSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEDOSupport.setStatus("mandatory")


class _SniParitySupport_Type(Integer32):
    """Custom type sniParitySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              32)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 32))
    )


_SniParitySupport_Type.__name__ = "Integer32"
_SniParitySupport_Object = MibTableColumn
sniParitySupport = _SniParitySupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 10),
    _SniParitySupport_Type()
)
sniParitySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniParitySupport.setStatus("mandatory")


class _SniECCSupport_Type(Integer32):
    """Custom type sniECCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              64)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 64))
    )


_SniECCSupport_Type.__name__ = "Integer32"
_SniECCSupport_Object = MibTableColumn
sniECCSupport = _SniECCSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 11),
    _SniECCSupport_Type()
)
sniECCSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniECCSupport.setStatus("mandatory")


class _SniSIMMSupport_Type(Integer32):
    """Custom type sniSIMMSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 128))
    )


_SniSIMMSupport_Type.__name__ = "Integer32"
_SniSIMMSupport_Object = MibTableColumn
sniSIMMSupport = _SniSIMMSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 12),
    _SniSIMMSupport_Type()
)
sniSIMMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSIMMSupport.setStatus("mandatory")


class _SniDIMMSupport_Type(Integer32):
    """Custom type sniDIMMSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              256)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 256))
    )


_SniDIMMSupport_Type.__name__ = "Integer32"
_SniDIMMSupport_Object = MibTableColumn
sniDIMMSupport = _SniDIMMSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 13),
    _SniDIMMSupport_Type()
)
sniDIMMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDIMMSupport.setStatus("mandatory")


class _SniRIMMSupport_Type(Integer32):
    """Custom type sniRIMMSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              512)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 512))
    )


_SniRIMMSupport_Type.__name__ = "Integer32"
_SniRIMMSupport_Object = MibTableColumn
sniRIMMSupport = _SniRIMMSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 14),
    _SniRIMMSupport_Type()
)
sniRIMMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniRIMMSupport.setStatus("mandatory")
_SniMaximumNumberOfLowLevelDevices_Type = Integer32
_SniMaximumNumberOfLowLevelDevices_Object = MibTableColumn
sniMaximumNumberOfLowLevelDevices = _SniMaximumNumberOfLowLevelDevices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 15),
    _SniMaximumNumberOfLowLevelDevices_Type()
)
sniMaximumNumberOfLowLevelDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaximumNumberOfLowLevelDevices.setStatus("mandatory")
_SniTotalNumberOfLowLevelDevices_Type = Integer32
_SniTotalNumberOfLowLevelDevices_Object = MibTableColumn
sniTotalNumberOfLowLevelDevices = _SniTotalNumberOfLowLevelDevices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 29, 1, 16),
    _SniTotalNumberOfLowLevelDevices_Type()
)
sniTotalNumberOfLowLevelDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTotalNumberOfLowLevelDevices.setStatus("mandatory")
_SniMainboardMemoryModules_Object = MibTable
sniMainboardMemoryModules = _SniMainboardMemoryModules_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31)
)
if mibBuilder.loadTexts:
    sniMainboardMemoryModules.setStatus("mandatory")
_SniMainboardMemoryModulesEntry_Object = MibTableRow
sniMainboardMemoryModulesEntry = _SniMainboardMemoryModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1)
)
sniMainboardMemoryModulesEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniMemoryController"),
    (0, "DESKSNMP-MIB", "sniMemoryModule"),
)
if mibBuilder.loadTexts:
    sniMainboardMemoryModulesEntry.setStatus("mandatory")
_SniMemoryController_Type = Integer32
_SniMemoryController_Object = MibTableColumn
sniMemoryController = _SniMemoryController_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 1),
    _SniMemoryController_Type()
)
sniMemoryController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryController.setStatus("mandatory")
_SniMemoryModule_Type = Integer32
_SniMemoryModule_Object = MibTableColumn
sniMemoryModule = _SniMemoryModule_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 2),
    _SniMemoryModule_Type()
)
sniMemoryModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryModule.setStatus("mandatory")
_SniMemoryModuleName_Type = DisplayString
_SniMemoryModuleName_Object = MibTableColumn
sniMemoryModuleName = _SniMemoryModuleName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 3),
    _SniMemoryModuleName_Type()
)
sniMemoryModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryModuleName.setStatus("mandatory")
_SniModuleSizeMB_Type = Integer32
_SniModuleSizeMB_Object = MibTableColumn
sniModuleSizeMB = _SniModuleSizeMB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 4),
    _SniModuleSizeMB_Type()
)
sniModuleSizeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniModuleSizeMB.setStatus("mandatory")
_SniSpeedns_Type = Integer32
_SniSpeedns_Object = MibTableColumn
sniSpeedns = _SniSpeedns_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 5),
    _SniSpeedns_Type()
)
sniSpeedns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSpeedns.setStatus("mandatory")


class _SniStandardMemoryModule_Type(Integer32):
    """Custom type sniStandardMemoryModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 4))
    )


_SniStandardMemoryModule_Type.__name__ = "Integer32"
_SniStandardMemoryModule_Object = MibTableColumn
sniStandardMemoryModule = _SniStandardMemoryModule_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 6),
    _SniStandardMemoryModule_Type()
)
sniStandardMemoryModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniStandardMemoryModule.setStatus("mandatory")


class _SniEDO_Type(Integer32):
    """Custom type sniEDO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 16))
    )


_SniEDO_Type.__name__ = "Integer32"
_SniEDO_Object = MibTableColumn
sniEDO = _SniEDO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 7),
    _SniEDO_Type()
)
sniEDO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEDO.setStatus("mandatory")


class _SniSIMM_Type(Integer32):
    """Custom type sniSIMM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 128))
    )


_SniSIMM_Type.__name__ = "Integer32"
_SniSIMM_Object = MibTableColumn
sniSIMM = _SniSIMM_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 8),
    _SniSIMM_Type()
)
sniSIMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSIMM.setStatus("mandatory")


class _SniDIMM_Type(Integer32):
    """Custom type sniDIMM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              256)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 256))
    )


_SniDIMM_Type.__name__ = "Integer32"
_SniDIMM_Object = MibTableColumn
sniDIMM = _SniDIMM_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 9),
    _SniDIMM_Type()
)
sniDIMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDIMM.setStatus("mandatory")


class _SniFastPageMode_Type(Integer32):
    """Custom type sniFastPageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 8))
    )


_SniFastPageMode_Type.__name__ = "Integer32"
_SniFastPageMode_Object = MibTableColumn
sniFastPageMode = _SniFastPageMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 10),
    _SniFastPageMode_Type()
)
sniFastPageMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniFastPageMode.setStatus("mandatory")


class _SniParity_Type(Integer32):
    """Custom type sniParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              32)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 32))
    )


_SniParity_Type.__name__ = "Integer32"
_SniParity_Object = MibTableColumn
sniParity = _SniParity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 11),
    _SniParity_Type()
)
sniParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniParity.setStatus("mandatory")


class _SniECC_Type(Integer32):
    """Custom type sniECC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              64)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 64))
    )


_SniECC_Type.__name__ = "Integer32"
_SniECC_Object = MibTableColumn
sniECC = _SniECC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 12),
    _SniECC_Type()
)
sniECC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniECC.setStatus("mandatory")
_SniMemoryBank_Type = Integer32
_SniMemoryBank_Object = MibTableColumn
sniMemoryBank = _SniMemoryBank_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 13),
    _SniMemoryBank_Type()
)
sniMemoryBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryBank.setStatus("mandatory")
_SniAttachedMemoryBank_Type = Integer32
_SniAttachedMemoryBank_Object = MibTableColumn
sniAttachedMemoryBank = _SniAttachedMemoryBank_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 14),
    _SniAttachedMemoryBank_Type()
)
sniAttachedMemoryBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAttachedMemoryBank.setStatus("mandatory")


class _SniRIMM_Type(Integer32):
    """Custom type sniRIMM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              512)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 512))
    )


_SniRIMM_Type.__name__ = "Integer32"
_SniRIMM_Object = MibTableColumn
sniRIMM = _SniRIMM_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 31, 1, 15),
    _SniRIMM_Type()
)
sniRIMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniRIMM.setStatus("mandatory")
_SniStateOfSupplySystemData_ObjectIdentity = ObjectIdentity
sniStateOfSupplySystemData = _SniStateOfSupplySystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 33)
)
_SniSystemName_Type = DisplayString
_SniSystemName_Object = MibScalar
sniSystemName = _SniSystemName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 33, 1),
    _SniSystemName_Type()
)
sniSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSystemName.setStatus("mandatory")
_SniIdentNumber_Type = DisplayString
_SniIdentNumber_Object = MibScalar
sniIdentNumber = _SniIdentNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 33, 2),
    _SniIdentNumber_Type()
)
sniIdentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIdentNumber.setStatus("mandatory")
_SniSystemSerialNumber_Type = DisplayString
_SniSystemSerialNumber_Object = MibScalar
sniSystemSerialNumber = _SniSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 33, 3),
    _SniSystemSerialNumber_Type()
)
sniSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSystemSerialNumber.setStatus("mandatory")
_SniProductionMonth_Type = DisplayString
_SniProductionMonth_Object = MibScalar
sniProductionMonth = _SniProductionMonth_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 33, 4),
    _SniProductionMonth_Type()
)
sniProductionMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProductionMonth.setStatus("mandatory")
_SniStateOfSupplyMainboard_ObjectIdentity = ObjectIdentity
sniStateOfSupplyMainboard = _SniStateOfSupplyMainboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 34)
)
_SniProductName_Type = DisplayString
_SniProductName_Object = MibScalar
sniProductName = _SniProductName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 34, 1),
    _SniProductName_Type()
)
sniProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProductName.setStatus("mandatory")
_SniGSNumber_Type = DisplayString
_SniGSNumber_Object = MibScalar
sniGSNumber = _SniGSNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 34, 2),
    _SniGSNumber_Type()
)
sniGSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGSNumber.setStatus("mandatory")
_SniMainboardSerialNumber_Type = DisplayString
_SniMainboardSerialNumber_Object = MibScalar
sniMainboardSerialNumber = _SniMainboardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 34, 3),
    _SniMainboardSerialNumber_Type()
)
sniMainboardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMainboardSerialNumber.setStatus("mandatory")
_SniBIOSVersion_Type = DisplayString
_SniBIOSVersion_Object = MibScalar
sniBIOSVersion = _SniBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 34, 4),
    _SniBIOSVersion_Type()
)
sniBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBIOSVersion.setStatus("mandatory")
_SniStateOfSupplyInternalDevices_Object = MibTable
sniStateOfSupplyInternalDevices = _SniStateOfSupplyInternalDevices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 35)
)
if mibBuilder.loadTexts:
    sniStateOfSupplyInternalDevices.setStatus("mandatory")
_SniStateOfSupplyInternalDevicesEntry_Object = MibTableRow
sniStateOfSupplyInternalDevicesEntry = _SniStateOfSupplyInternalDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 35, 1)
)
sniStateOfSupplyInternalDevicesEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniDeviceIndex"),
)
if mibBuilder.loadTexts:
    sniStateOfSupplyInternalDevicesEntry.setStatus("mandatory")
_SniDeviceIndex_Type = Integer32
_SniDeviceIndex_Object = MibTableColumn
sniDeviceIndex = _SniDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 35, 1, 1),
    _SniDeviceIndex_Type()
)
sniDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDeviceIndex.setStatus("mandatory")
_SniDeviceName_Type = DisplayString
_SniDeviceName_Object = MibTableColumn
sniDeviceName = _SniDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 35, 1, 2),
    _SniDeviceName_Type()
)
sniDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDeviceName.setStatus("mandatory")


class _SniDeviceType_Type(Integer32):
    """Custom type sniDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("e-cd-rom", 6),
          ("e-chipcard-reader", 10),
          ("e-floppydisk", 5),
          ("e-floptical-disk", 9),
          ("e-harddisk", 4),
          ("e-magneto-optical-disk", 7),
          ("e-other", 1),
          ("e-power-supply", 3),
          ("e-streamer", 8),
          ("e-unknown", 0))
    )


_SniDeviceType_Type.__name__ = "Integer32"
_SniDeviceType_Object = MibTableColumn
sniDeviceType = _SniDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 35, 1, 3),
    _SniDeviceType_Type()
)
sniDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDeviceType.setStatus("mandatory")
_SniDeviceSerialnumber_Type = DisplayString
_SniDeviceSerialnumber_Object = MibTableColumn
sniDeviceSerialnumber = _SniDeviceSerialnumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 35, 1, 4),
    _SniDeviceSerialnumber_Type()
)
sniDeviceSerialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDeviceSerialnumber.setStatus("mandatory")
_SniNumberofDevices_Type = Integer32
_SniNumberofDevices_Object = MibTableColumn
sniNumberofDevices = _SniNumberofDevices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 35, 1, 5),
    _SniNumberofDevices_Type()
)
sniNumberofDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNumberofDevices.setStatus("mandatory")
_SniStateOfSupplyAddOnModules_Object = MibTable
sniStateOfSupplyAddOnModules = _SniStateOfSupplyAddOnModules_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 37)
)
if mibBuilder.loadTexts:
    sniStateOfSupplyAddOnModules.setStatus("mandatory")
_SniStateOfSupplyAddOnModulesEntry_Object = MibTableRow
sniStateOfSupplyAddOnModulesEntry = _SniStateOfSupplyAddOnModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 37, 1)
)
sniStateOfSupplyAddOnModulesEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniModuleIndex"),
)
if mibBuilder.loadTexts:
    sniStateOfSupplyAddOnModulesEntry.setStatus("mandatory")
_SniModuleIndex_Type = Integer32
_SniModuleIndex_Object = MibTableColumn
sniModuleIndex = _SniModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 37, 1, 1),
    _SniModuleIndex_Type()
)
sniModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniModuleIndex.setStatus("mandatory")
_SniModuleName_Type = DisplayString
_SniModuleName_Object = MibTableColumn
sniModuleName = _SniModuleName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 37, 1, 2),
    _SniModuleName_Type()
)
sniModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniModuleName.setStatus("mandatory")


class _SniModuleType_Type(Integer32):
    """Custom type sniModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e-cache", 3),
          ("e-dram", 4),
          ("e-other", 1),
          ("e-unknown", 0),
          ("e-video-memory", 5))
    )


_SniModuleType_Type.__name__ = "Integer32"
_SniModuleType_Object = MibTableColumn
sniModuleType = _SniModuleType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 37, 1, 3),
    _SniModuleType_Type()
)
sniModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniModuleType.setStatus("mandatory")
_SniModuleSerialnumber_Type = DisplayString
_SniModuleSerialnumber_Object = MibTableColumn
sniModuleSerialnumber = _SniModuleSerialnumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 37, 1, 4),
    _SniModuleSerialnumber_Type()
)
sniModuleSerialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniModuleSerialnumber.setStatus("mandatory")
_SniNumberofModules_Type = Integer32
_SniNumberofModules_Object = MibTableColumn
sniNumberofModules = _SniNumberofModules_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 37, 1, 5),
    _SniNumberofModules_Type()
)
sniNumberofModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNumberofModules.setStatus("mandatory")
_SniStateOfSupplyAddOnBoards_Object = MibTable
sniStateOfSupplyAddOnBoards = _SniStateOfSupplyAddOnBoards_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39)
)
if mibBuilder.loadTexts:
    sniStateOfSupplyAddOnBoards.setStatus("mandatory")
_SniStateOfSupplyAddOnBoardsEntry_Object = MibTableRow
sniStateOfSupplyAddOnBoardsEntry = _SniStateOfSupplyAddOnBoardsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1)
)
sniStateOfSupplyAddOnBoardsEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniBoardIndex"),
)
if mibBuilder.loadTexts:
    sniStateOfSupplyAddOnBoardsEntry.setStatus("mandatory")
_SniBoardIndex_Type = Integer32
_SniBoardIndex_Object = MibTableColumn
sniBoardIndex = _SniBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 1),
    _SniBoardIndex_Type()
)
sniBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBoardIndex.setStatus("mandatory")
_SniBoardName_Type = DisplayString
_SniBoardName_Object = MibTableColumn
sniBoardName = _SniBoardName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 2),
    _SniBoardName_Type()
)
sniBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBoardName.setStatus("mandatory")


class _SniBoardType_Type(Integer32):
    """Custom type sniBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("e-audio", 6),
          ("e-fax", 7),
          ("e-modem", 8),
          ("e-mpeg", 10),
          ("e-net", 4),
          ("e-other", 1),
          ("e-scsi", 5),
          ("e-tv", 9),
          ("e-unknown", 0),
          ("e-video", 3))
    )


_SniBoardType_Type.__name__ = "Integer32"
_SniBoardType_Object = MibTableColumn
sniBoardType = _SniBoardType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 3),
    _SniBoardType_Type()
)
sniBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBoardType.setStatus("mandatory")
_SniBoardSerialnumber_Type = DisplayString
_SniBoardSerialnumber_Object = MibTableColumn
sniBoardSerialnumber = _SniBoardSerialnumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 4),
    _SniBoardSerialnumber_Type()
)
sniBoardSerialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBoardSerialnumber.setStatus("mandatory")
_SniNumberofBoards_Type = Integer32
_SniNumberofBoards_Object = MibTableColumn
sniNumberofBoards = _SniNumberofBoards_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 5),
    _SniNumberofBoards_Type()
)
sniNumberofBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNumberofBoards.setStatus("mandatory")
_SniVendorID_Type = DisplayString
_SniVendorID_Object = MibTableColumn
sniVendorID = _SniVendorID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 6),
    _SniVendorID_Type()
)
sniVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniVendorID.setStatus("mandatory")
_SniBoardIRQ_Type = DisplayString
_SniBoardIRQ_Object = MibTableColumn
sniBoardIRQ = _SniBoardIRQ_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 7),
    _SniBoardIRQ_Type()
)
sniBoardIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBoardIRQ.setStatus("mandatory")
_SniBoardDMA_Type = DisplayString
_SniBoardDMA_Object = MibTableColumn
sniBoardDMA = _SniBoardDMA_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 8),
    _SniBoardDMA_Type()
)
sniBoardDMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBoardDMA.setStatus("mandatory")
_SniIOAddress_Type = DisplayString
_SniIOAddress_Object = MibTableColumn
sniIOAddress = _SniIOAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 9),
    _SniIOAddress_Type()
)
sniIOAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIOAddress.setStatus("mandatory")
_SniMemoryMapping_Type = DisplayString
_SniMemoryMapping_Object = MibTableColumn
sniMemoryMapping = _SniMemoryMapping_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 39, 1, 10),
    _SniMemoryMapping_Type()
)
sniMemoryMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryMapping.setStatus("mandatory")
_SniStateOfSupplySCSIDevices_Object = MibTable
sniStateOfSupplySCSIDevices = _SniStateOfSupplySCSIDevices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41)
)
if mibBuilder.loadTexts:
    sniStateOfSupplySCSIDevices.setStatus("mandatory")
_SniStateOfSupplySCSIDevicesEntry_Object = MibTableRow
sniStateOfSupplySCSIDevicesEntry = _SniStateOfSupplySCSIDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1)
)
sniStateOfSupplySCSIDevicesEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniSCSIDeviceIndex"),
)
if mibBuilder.loadTexts:
    sniStateOfSupplySCSIDevicesEntry.setStatus("mandatory")
_SniSCSIDeviceIndex_Type = Integer32
_SniSCSIDeviceIndex_Object = MibTableColumn
sniSCSIDeviceIndex = _SniSCSIDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1, 1),
    _SniSCSIDeviceIndex_Type()
)
sniSCSIDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSCSIDeviceIndex.setStatus("mandatory")
_SniSCSIDeviceName_Type = DisplayString
_SniSCSIDeviceName_Object = MibTableColumn
sniSCSIDeviceName = _SniSCSIDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1, 2),
    _SniSCSIDeviceName_Type()
)
sniSCSIDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSCSIDeviceName.setStatus("mandatory")


class _SniSCSIDeviceType_Type(Integer32):
    """Custom type sniSCSIDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("e-ascit8-defined", 12),
          ("e-cdrom", 7),
          ("e-communication", 11),
          ("e-jukebox", 10),
          ("e-optical-disk", 9),
          ("e-other", 1),
          ("e-printer", 4),
          ("e-processor", 5),
          ("e-scanner", 8),
          ("e-tape", 3),
          ("e-unknown", 0),
          ("e-worm", 6))
    )


_SniSCSIDeviceType_Type.__name__ = "Integer32"
_SniSCSIDeviceType_Object = MibTableColumn
sniSCSIDeviceType = _SniSCSIDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1, 3),
    _SniSCSIDeviceType_Type()
)
sniSCSIDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSCSIDeviceType.setStatus("mandatory")
_SniTargetID_Type = Integer32
_SniTargetID_Object = MibTableColumn
sniTargetID = _SniTargetID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1, 4),
    _SniTargetID_Type()
)
sniTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTargetID.setStatus("mandatory")
_SniHostAdapterID_Type = Integer32
_SniHostAdapterID_Object = MibTableColumn
sniHostAdapterID = _SniHostAdapterID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1, 5),
    _SniHostAdapterID_Type()
)
sniHostAdapterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniHostAdapterID.setStatus("mandatory")
_SniCapacity_Type = DisplayString
_SniCapacity_Object = MibTableColumn
sniCapacity = _SniCapacity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1, 6),
    _SniCapacity_Type()
)
sniCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCapacity.setStatus("mandatory")
_SniSCSIDeviceSerialnumber_Type = DisplayString
_SniSCSIDeviceSerialnumber_Object = MibTableColumn
sniSCSIDeviceSerialnumber = _SniSCSIDeviceSerialnumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1, 7),
    _SniSCSIDeviceSerialnumber_Type()
)
sniSCSIDeviceSerialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSCSIDeviceSerialnumber.setStatus("mandatory")
_SniInfo_Type = DisplayString
_SniInfo_Object = MibTableColumn
sniInfo = _SniInfo_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1, 8),
    _SniInfo_Type()
)
sniInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInfo.setStatus("mandatory")
_SniNumberOfSCSIDevices_Type = Integer32
_SniNumberOfSCSIDevices_Object = MibTableColumn
sniNumberOfSCSIDevices = _SniNumberOfSCSIDevices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 41, 1, 9),
    _SniNumberOfSCSIDevices_Type()
)
sniNumberOfSCSIDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNumberOfSCSIDevices.setStatus("mandatory")
_SniAntiVirus_Object = MibTable
sniAntiVirus = _SniAntiVirus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43)
)
if mibBuilder.loadTexts:
    sniAntiVirus.setStatus("mandatory")
_SniAntiVirusEntry_Object = MibTableRow
sniAntiVirusEntry = _SniAntiVirusEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1)
)
sniAntiVirusEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniAntiVirusProgramIndex"),
)
if mibBuilder.loadTexts:
    sniAntiVirusEntry.setStatus("mandatory")
_SniAntiVirusProgramIndex_Type = Integer32
_SniAntiVirusProgramIndex_Object = MibTableColumn
sniAntiVirusProgramIndex = _SniAntiVirusProgramIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 1),
    _SniAntiVirusProgramIndex_Type()
)
sniAntiVirusProgramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAntiVirusProgramIndex.setStatus("mandatory")
_SniAntiVirusLogfile_Type = DisplayString
_SniAntiVirusLogfile_Object = MibTableColumn
sniAntiVirusLogfile = _SniAntiVirusLogfile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 2),
    _SniAntiVirusLogfile_Type()
)
sniAntiVirusLogfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAntiVirusLogfile.setStatus("mandatory")
_SniScannerName_Type = DisplayString
_SniScannerName_Object = MibTableColumn
sniScannerName = _SniScannerName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 3),
    _SniScannerName_Type()
)
sniScannerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniScannerName.setStatus("mandatory")
_SniErrorKeyword1_Type = DisplayString
_SniErrorKeyword1_Object = MibTableColumn
sniErrorKeyword1 = _SniErrorKeyword1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 4),
    _SniErrorKeyword1_Type()
)
sniErrorKeyword1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword1.setStatus("mandatory")
_SniErrorKeyword2_Type = DisplayString
_SniErrorKeyword2_Object = MibTableColumn
sniErrorKeyword2 = _SniErrorKeyword2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 5),
    _SniErrorKeyword2_Type()
)
sniErrorKeyword2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword2.setStatus("mandatory")
_SniErrorKeyword3_Type = DisplayString
_SniErrorKeyword3_Object = MibTableColumn
sniErrorKeyword3 = _SniErrorKeyword3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 6),
    _SniErrorKeyword3_Type()
)
sniErrorKeyword3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword3.setStatus("mandatory")
_SniErrorKeyword4_Type = DisplayString
_SniErrorKeyword4_Object = MibTableColumn
sniErrorKeyword4 = _SniErrorKeyword4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 7),
    _SniErrorKeyword4_Type()
)
sniErrorKeyword4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword4.setStatus("mandatory")
_SniErrorKeyword5_Type = DisplayString
_SniErrorKeyword5_Object = MibTableColumn
sniErrorKeyword5 = _SniErrorKeyword5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 8),
    _SniErrorKeyword5_Type()
)
sniErrorKeyword5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword5.setStatus("mandatory")
_SniErrorKeyword6_Type = DisplayString
_SniErrorKeyword6_Object = MibTableColumn
sniErrorKeyword6 = _SniErrorKeyword6_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 9),
    _SniErrorKeyword6_Type()
)
sniErrorKeyword6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword6.setStatus("mandatory")
_SniErrorKeyword7_Type = DisplayString
_SniErrorKeyword7_Object = MibTableColumn
sniErrorKeyword7 = _SniErrorKeyword7_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 10),
    _SniErrorKeyword7_Type()
)
sniErrorKeyword7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword7.setStatus("mandatory")
_SniErrorKeyword8_Type = DisplayString
_SniErrorKeyword8_Object = MibTableColumn
sniErrorKeyword8 = _SniErrorKeyword8_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 11),
    _SniErrorKeyword8_Type()
)
sniErrorKeyword8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword8.setStatus("mandatory")
_SniErrorKeyword9_Type = DisplayString
_SniErrorKeyword9_Object = MibTableColumn
sniErrorKeyword9 = _SniErrorKeyword9_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 12),
    _SniErrorKeyword9_Type()
)
sniErrorKeyword9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword9.setStatus("mandatory")
_SniErrorKeyword10_Type = DisplayString
_SniErrorKeyword10_Object = MibTableColumn
sniErrorKeyword10 = _SniErrorKeyword10_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 13),
    _SniErrorKeyword10_Type()
)
sniErrorKeyword10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniErrorKeyword10.setStatus("mandatory")
_SniWarningKeyword1_Type = DisplayString
_SniWarningKeyword1_Object = MibTableColumn
sniWarningKeyword1 = _SniWarningKeyword1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 14),
    _SniWarningKeyword1_Type()
)
sniWarningKeyword1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword1.setStatus("mandatory")
_SniWarningKeyword2_Type = DisplayString
_SniWarningKeyword2_Object = MibTableColumn
sniWarningKeyword2 = _SniWarningKeyword2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 15),
    _SniWarningKeyword2_Type()
)
sniWarningKeyword2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword2.setStatus("mandatory")
_SniWarningKeyword3_Type = DisplayString
_SniWarningKeyword3_Object = MibTableColumn
sniWarningKeyword3 = _SniWarningKeyword3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 16),
    _SniWarningKeyword3_Type()
)
sniWarningKeyword3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword3.setStatus("mandatory")
_SniWarningKeyword4_Type = DisplayString
_SniWarningKeyword4_Object = MibTableColumn
sniWarningKeyword4 = _SniWarningKeyword4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 17),
    _SniWarningKeyword4_Type()
)
sniWarningKeyword4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword4.setStatus("mandatory")
_SniWarningKeyword5_Type = DisplayString
_SniWarningKeyword5_Object = MibTableColumn
sniWarningKeyword5 = _SniWarningKeyword5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 18),
    _SniWarningKeyword5_Type()
)
sniWarningKeyword5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword5.setStatus("mandatory")
_SniWarningKeyword6_Type = DisplayString
_SniWarningKeyword6_Object = MibTableColumn
sniWarningKeyword6 = _SniWarningKeyword6_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 19),
    _SniWarningKeyword6_Type()
)
sniWarningKeyword6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword6.setStatus("mandatory")
_SniWarningKeyword7_Type = DisplayString
_SniWarningKeyword7_Object = MibTableColumn
sniWarningKeyword7 = _SniWarningKeyword7_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 20),
    _SniWarningKeyword7_Type()
)
sniWarningKeyword7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword7.setStatus("mandatory")
_SniWarningKeyword8_Type = DisplayString
_SniWarningKeyword8_Object = MibTableColumn
sniWarningKeyword8 = _SniWarningKeyword8_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 21),
    _SniWarningKeyword8_Type()
)
sniWarningKeyword8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword8.setStatus("mandatory")
_SniWarningKeyword9_Type = DisplayString
_SniWarningKeyword9_Object = MibTableColumn
sniWarningKeyword9 = _SniWarningKeyword9_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 22),
    _SniWarningKeyword9_Type()
)
sniWarningKeyword9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword9.setStatus("mandatory")
_SniWarningKeyword10_Type = DisplayString
_SniWarningKeyword10_Object = MibTableColumn
sniWarningKeyword10 = _SniWarningKeyword10_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 23),
    _SniWarningKeyword10_Type()
)
sniWarningKeyword10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWarningKeyword10.setStatus("mandatory")


class _SniDistinguishWarningError_Type(Integer32):
    """Custom type sniDistinguishWarningError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniDistinguishWarningError_Type.__name__ = "Integer32"
_SniDistinguishWarningError_Object = MibTableColumn
sniDistinguishWarningError = _SniDistinguishWarningError_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 43, 1, 24),
    _SniDistinguishWarningError_Type()
)
sniDistinguishWarningError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDistinguishWarningError.setStatus("mandatory")
_SniMouse_ObjectIdentity = ObjectIdentity
sniMouse = _SniMouse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45)
)
_SniMouseManufacturer_Type = DisplayString
_SniMouseManufacturer_Object = MibScalar
sniMouseManufacturer = _SniMouseManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 1),
    _SniMouseManufacturer_Type()
)
sniMouseManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMouseManufacturer.setStatus("mandatory")
_SniMouseDriverName_Type = DisplayString
_SniMouseDriverName_Object = MibScalar
sniMouseDriverName = _SniMouseDriverName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 2),
    _SniMouseDriverName_Type()
)
sniMouseDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMouseDriverName.setStatus("mandatory")
_SniDriverVersion_Type = DisplayString
_SniDriverVersion_Object = MibScalar
sniDriverVersion = _SniDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 3),
    _SniDriverVersion_Type()
)
sniDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDriverVersion.setStatus("mandatory")


class _SniMouseInterface_Type(Integer32):
    """Custom type sniMouseInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("e-bus", 6),
          ("e-infra-red", 5),
          ("e-ps-2", 4),
          ("e-serial", 3),
          ("e-unknown", 0),
          ("e-usb", 7))
    )


_SniMouseInterface_Type.__name__ = "Integer32"
_SniMouseInterface_Object = MibScalar
sniMouseInterface = _SniMouseInterface_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 4),
    _SniMouseInterface_Type()
)
sniMouseInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMouseInterface.setStatus("mandatory")
_SniMouseIRQ_Type = Integer32
_SniMouseIRQ_Object = MibScalar
sniMouseIRQ = _SniMouseIRQ_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 5),
    _SniMouseIRQ_Type()
)
sniMouseIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMouseIRQ.setStatus("mandatory")
_SniMousePort_Type = DisplayString
_SniMousePort_Object = MibScalar
sniMousePort = _SniMousePort_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 6),
    _SniMousePort_Type()
)
sniMousePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMousePort.setStatus("mandatory")
_SniSupportedButtons_Type = Integer32
_SniSupportedButtons_Object = MibScalar
sniSupportedButtons = _SniSupportedButtons_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 7),
    _SniSupportedButtons_Type()
)
sniSupportedButtons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSupportedButtons.setStatus("mandatory")


class _SniButtonsExchanged_Type(Integer32):
    """Custom type sniButtonsExchanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniButtonsExchanged_Type.__name__ = "Integer32"
_SniButtonsExchanged_Object = MibScalar
sniButtonsExchanged = _SniButtonsExchanged_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 8),
    _SniButtonsExchanged_Type()
)
sniButtonsExchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniButtonsExchanged.setStatus("mandatory")
_SniSpeedPercentage_Type = Integer32
_SniSpeedPercentage_Object = MibScalar
sniSpeedPercentage = _SniSpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 9),
    _SniSpeedPercentage_Type()
)
sniSpeedPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSpeedPercentage.setStatus("mandatory")


class _SniShowMouseTrails_Type(Integer32):
    """Custom type sniShowMouseTrails based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniShowMouseTrails_Type.__name__ = "Integer32"
_SniShowMouseTrails_Object = MibScalar
sniShowMouseTrails = _SniShowMouseTrails_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 45, 10),
    _SniShowMouseTrails_Type()
)
sniShowMouseTrails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniShowMouseTrails.setStatus("mandatory")
_SniKeyboard_ObjectIdentity = ObjectIdentity
sniKeyboard = _SniKeyboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 46)
)
_SniKeyboardType_Type = DisplayString
_SniKeyboardType_Object = MibScalar
sniKeyboardType = _SniKeyboardType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 46, 1),
    _SniKeyboardType_Type()
)
sniKeyboardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniKeyboardType.setStatus("mandatory")
_SniLayout_Type = DisplayString
_SniLayout_Object = MibScalar
sniLayout = _SniLayout_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 46, 2),
    _SniLayout_Type()
)
sniLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLayout.setStatus("mandatory")


class _SniInterfaceType_Type(Integer32):
    """Custom type sniInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("e-access-bus", 9),
          ("e-db-9", 8),
          ("e-hp-hil", 7),
          ("e-infra-red", 6),
          ("e-micro-din", 4),
          ("e-mini-din", 3),
          ("e-ps-2", 5),
          ("e-unknown", 0),
          ("e-usb", 10))
    )


_SniInterfaceType_Type.__name__ = "Integer32"
_SniInterfaceType_Object = MibScalar
sniInterfaceType = _SniInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 46, 3),
    _SniInterfaceType_Type()
)
sniInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInterfaceType.setStatus("mandatory")
_SniCodepage_Type = Integer32
_SniCodepage_Object = MibScalar
sniCodepage = _SniCodepage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 46, 4),
    _SniCodepage_Type()
)
sniCodepage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCodepage.setStatus("mandatory")
_SniWindowsDriver_Type = DisplayString
_SniWindowsDriver_Object = MibScalar
sniWindowsDriver = _SniWindowsDriver_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 46, 5),
    _SniWindowsDriver_Type()
)
sniWindowsDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniWindowsDriver.setStatus("mandatory")
_SniDOSDriver_Type = DisplayString
_SniDOSDriver_Object = MibScalar
sniDOSDriver = _SniDOSDriver_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 46, 6),
    _SniDOSDriver_Type()
)
sniDOSDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDOSDriver.setStatus("mandatory")
_SniDeskViewVersion_ObjectIdentity = ObjectIdentity
sniDeskViewVersion = _SniDeskViewVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 47)
)
_SniSysInf32Version_Type = DisplayString
_SniSysInf32Version_Object = MibScalar
sniSysInf32Version = _SniSysInf32Version_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 47, 1),
    _SniSysInf32Version_Type()
)
sniSysInf32Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSysInf32Version.setStatus("mandatory")
_SniSysInf16Version_Type = DisplayString
_SniSysInf16Version_Object = MibScalar
sniSysInf16Version = _SniSysInf16Version_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 47, 2),
    _SniSysInf16Version_Type()
)
sniSysInf16Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSysInf16Version.setStatus("mandatory")
_SniDeskInfoAgentVersion_Type = DisplayString
_SniDeskInfoAgentVersion_Object = MibScalar
sniDeskInfoAgentVersion = _SniDeskInfoAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 47, 3),
    _SniDeskInfoAgentVersion_Type()
)
sniDeskInfoAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDeskInfoAgentVersion.setStatus("mandatory")
_SniDINetVersion_Type = DisplayString
_SniDINetVersion_Object = MibScalar
sniDINetVersion = _SniDINetVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 47, 4),
    _SniDINetVersion_Type()
)
sniDINetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDINetVersion.setStatus("mandatory")
_SniDNAgentVersion_Type = DisplayString
_SniDNAgentVersion_Object = MibScalar
sniDNAgentVersion = _SniDNAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 47, 5),
    _SniDNAgentVersion_Type()
)
sniDNAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDNAgentVersion.setStatus("mandatory")
_SniDNBrowserVersion_Type = DisplayString
_SniDNBrowserVersion_Object = MibScalar
sniDNBrowserVersion = _SniDNBrowserVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 47, 6),
    _SniDNBrowserVersion_Type()
)
sniDNBrowserVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDNBrowserVersion.setStatus("mandatory")
_SniSMARTValues_Object = MibTable
sniSMARTValues = _SniSMARTValues_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48)
)
if mibBuilder.loadTexts:
    sniSMARTValues.setStatus("mandatory")
_SniSMARTValuesEntry_Object = MibTableRow
sniSMARTValuesEntry = _SniSMARTValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48, 1)
)
sniSMARTValuesEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniSMARTIndex"),
)
if mibBuilder.loadTexts:
    sniSMARTValuesEntry.setStatus("mandatory")
_SniSMARTIndex_Type = Integer32
_SniSMARTIndex_Object = MibTableColumn
sniSMARTIndex = _SniSMARTIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48, 1, 1),
    _SniSMARTIndex_Type()
)
sniSMARTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSMARTIndex.setStatus("mandatory")
_SniPhysicalDriveCrossreference_Type = Integer32
_SniPhysicalDriveCrossreference_Object = MibTableColumn
sniPhysicalDriveCrossreference = _SniPhysicalDriveCrossreference_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48, 1, 2),
    _SniPhysicalDriveCrossreference_Type()
)
sniPhysicalDriveCrossreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhysicalDriveCrossreference.setStatus("mandatory")
_SniSMARTID_Type = Integer32
_SniSMARTID_Object = MibTableColumn
sniSMARTID = _SniSMARTID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48, 1, 3),
    _SniSMARTID_Type()
)
sniSMARTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSMARTID.setStatus("mandatory")
_SniSMARTName_Type = DisplayString
_SniSMARTName_Object = MibTableColumn
sniSMARTName = _SniSMARTName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48, 1, 4),
    _SniSMARTName_Type()
)
sniSMARTName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSMARTName.setStatus("mandatory")
_SniSMARTErrorThreshold_Type = Integer32
_SniSMARTErrorThreshold_Object = MibTableColumn
sniSMARTErrorThreshold = _SniSMARTErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48, 1, 5),
    _SniSMARTErrorThreshold_Type()
)
sniSMARTErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSMARTErrorThreshold.setStatus("mandatory")
_SniSMARTWarningThreshold_Type = Integer32
_SniSMARTWarningThreshold_Object = MibTableColumn
sniSMARTWarningThreshold = _SniSMARTWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48, 1, 6),
    _SniSMARTWarningThreshold_Type()
)
sniSMARTWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSMARTWarningThreshold.setStatus("mandatory")
_SniCurrentSMARTValue_Type = Integer32
_SniCurrentSMARTValue_Object = MibTableColumn
sniCurrentSMARTValue = _SniCurrentSMARTValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48, 1, 7),
    _SniCurrentSMARTValue_Type()
)
sniCurrentSMARTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCurrentSMARTValue.setStatus("mandatory")


class _SniSMARTState_Type(Integer32):
    """Custom type sniSMARTState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e-critical", 5),
          ("e-ok", 3),
          ("e-unknown", 0),
          ("e-warning", 4))
    )


_SniSMARTState_Type.__name__ = "Integer32"
_SniSMARTState_Object = MibTableColumn
sniSMARTState = _SniSMARTState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 48, 1, 8),
    _SniSMARTState_Type()
)
sniSMARTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSMARTState.setStatus("mandatory")
_SniHardwarePowersupply_Object = MibTable
sniHardwarePowersupply = _SniHardwarePowersupply_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50)
)
if mibBuilder.loadTexts:
    sniHardwarePowersupply.setStatus("mandatory")
_SniHardwarePowersupplyEntry_Object = MibTableRow
sniHardwarePowersupplyEntry = _SniHardwarePowersupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1)
)
sniHardwarePowersupplyEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniPowersupplyIndex"),
)
if mibBuilder.loadTexts:
    sniHardwarePowersupplyEntry.setStatus("mandatory")
_SniPowersupplyIndex_Type = Integer32
_SniPowersupplyIndex_Object = MibTableColumn
sniPowersupplyIndex = _SniPowersupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 1),
    _SniPowersupplyIndex_Type()
)
sniPowersupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPowersupplyIndex.setStatus("mandatory")
_SniPowersupplySerialNumber_Type = DisplayString
_SniPowersupplySerialNumber_Object = MibTableColumn
sniPowersupplySerialNumber = _SniPowersupplySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 2),
    _SniPowersupplySerialNumber_Type()
)
sniPowersupplySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPowersupplySerialNumber.setStatus("mandatory")
_SniPowersupplyGSLevel_Type = DisplayString
_SniPowersupplyGSLevel_Object = MibTableColumn
sniPowersupplyGSLevel = _SniPowersupplyGSLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 3),
    _SniPowersupplyGSLevel_Type()
)
sniPowersupplyGSLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPowersupplyGSLevel.setStatus("mandatory")
_SniPowersupplyRevision_Type = DisplayString
_SniPowersupplyRevision_Object = MibTableColumn
sniPowersupplyRevision = _SniPowersupplyRevision_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 4),
    _SniPowersupplyRevision_Type()
)
sniPowersupplyRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPowersupplyRevision.setStatus("mandatory")
_SniPowersupplyManufacturingDate_Type = DisplayString
_SniPowersupplyManufacturingDate_Object = MibTableColumn
sniPowersupplyManufacturingDate = _SniPowersupplyManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 5),
    _SniPowersupplyManufacturingDate_Type()
)
sniPowersupplyManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPowersupplyManufacturingDate.setStatus("mandatory")
_SniOutputPowerW_Type = DisplayString
_SniOutputPowerW_Object = MibTableColumn
sniOutputPowerW = _SniOutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 6),
    _SniOutputPowerW_Type()
)
sniOutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOutputPowerW.setStatus("mandatory")


class _SniMonitorOutletSupported_Type(Integer32):
    """Custom type sniMonitorOutletSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniMonitorOutletSupported_Type.__name__ = "Integer32"
_SniMonitorOutletSupported_Object = MibTableColumn
sniMonitorOutletSupported = _SniMonitorOutletSupported_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 7),
    _SniMonitorOutletSupported_Type()
)
sniMonitorOutletSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMonitorOutletSupported.setStatus("mandatory")


class _SniMonitorOutlet_Type(Integer32):
    """Custom type sniMonitorOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-off", 3),
          ("e-on", 4),
          ("e-other", 1),
          ("e-unknown", 0))
    )


_SniMonitorOutlet_Type.__name__ = "Integer32"
_SniMonitorOutlet_Object = MibTableColumn
sniMonitorOutlet = _SniMonitorOutlet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 8),
    _SniMonitorOutlet_Type()
)
sniMonitorOutlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMonitorOutlet.setStatus("mandatory")
_SniVoltage5V_Type = DisplayString
_SniVoltage5V_Object = MibTableColumn
sniVoltage5V = _SniVoltage5V_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 9),
    _SniVoltage5V_Type()
)
sniVoltage5V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniVoltage5V.setStatus("mandatory")
_SniVoltage12V_Type = DisplayString
_SniVoltage12V_Object = MibTableColumn
sniVoltage12V = _SniVoltage12V_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 10),
    _SniVoltage12V_Type()
)
sniVoltage12V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniVoltage12V.setStatus("mandatory")
_SniMin5VCurrentA_Type = DisplayString
_SniMin5VCurrentA_Object = MibTableColumn
sniMin5VCurrentA = _SniMin5VCurrentA_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 11),
    _SniMin5VCurrentA_Type()
)
sniMin5VCurrentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMin5VCurrentA.setStatus("mandatory")
_SniOutputCurrentmA_Type = DisplayString
_SniOutputCurrentmA_Object = MibTableColumn
sniOutputCurrentmA = _SniOutputCurrentmA_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 12),
    _SniOutputCurrentmA_Type()
)
sniOutputCurrentmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOutputCurrentmA.setStatus("mandatory")
_SniPulsPerRevolution_Type = Integer32
_SniPulsPerRevolution_Object = MibTableColumn
sniPulsPerRevolution = _SniPulsPerRevolution_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 13),
    _SniPulsPerRevolution_Type()
)
sniPulsPerRevolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPulsPerRevolution.setStatus("mandatory")


class _SniPowersFanControlSupp_Type(Integer32):
    """Custom type sniPowersFanControlSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPowersFanControlSupp_Type.__name__ = "Integer32"
_SniPowersFanControlSupp_Object = MibTableColumn
sniPowersFanControlSupp = _SniPowersFanControlSupp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 14),
    _SniPowersFanControlSupp_Type()
)
sniPowersFanControlSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPowersFanControlSupp.setStatus("mandatory")


class _SniPowersupplyFanSpeed_Type(Integer32):
    """Custom type sniPowersupplyFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-controlled", 3),
          ("e-full-speed", 4),
          ("e-other", 1),
          ("e-unknown", 0))
    )


_SniPowersupplyFanSpeed_Type.__name__ = "Integer32"
_SniPowersupplyFanSpeed_Object = MibTableColumn
sniPowersupplyFanSpeed = _SniPowersupplyFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 15),
    _SniPowersupplyFanSpeed_Type()
)
sniPowersupplyFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPowersupplyFanSpeed.setStatus("mandatory")


class _SniPowersupplyFanControl_Type(Integer32):
    """Custom type sniPowersupplyFanControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e-full-controlled", 5),
          ("e-not-controlled", 3),
          ("e-on-off", 4),
          ("e-other", 1),
          ("e-unknown", 0))
    )


_SniPowersupplyFanControl_Type.__name__ = "Integer32"
_SniPowersupplyFanControl_Object = MibTableColumn
sniPowersupplyFanControl = _SniPowersupplyFanControl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 50, 1, 16),
    _SniPowersupplyFanControl_Type()
)
sniPowersupplyFanControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPowersupplyFanControl.setStatus("mandatory")
_SniHardwareDriveBays_Object = MibTable
sniHardwareDriveBays = _SniHardwareDriveBays_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 52)
)
if mibBuilder.loadTexts:
    sniHardwareDriveBays.setStatus("mandatory")
_SniHardwareDriveBaysEntry_Object = MibTableRow
sniHardwareDriveBaysEntry = _SniHardwareDriveBaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 52, 1)
)
sniHardwareDriveBaysEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniDriveBayIndex"),
)
if mibBuilder.loadTexts:
    sniHardwareDriveBaysEntry.setStatus("mandatory")
_SniDriveBayIndex_Type = Integer32
_SniDriveBayIndex_Object = MibTableColumn
sniDriveBayIndex = _SniDriveBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 52, 1, 1),
    _SniDriveBayIndex_Type()
)
sniDriveBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDriveBayIndex.setStatus("mandatory")


class _SniDriveBayType_Type(Integer32):
    """Custom type sniDriveBayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-3-5-inch", 3),
          ("e-5-25-inch", 4),
          ("e-other", 1),
          ("e-unknown", 0))
    )


_SniDriveBayType_Type.__name__ = "Integer32"
_SniDriveBayType_Object = MibTableColumn
sniDriveBayType = _SniDriveBayType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 52, 1, 2),
    _SniDriveBayType_Type()
)
sniDriveBayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDriveBayType.setStatus("mandatory")
_SniNumberOfDriveBays_Type = Integer32
_SniNumberOfDriveBays_Object = MibTableColumn
sniNumberOfDriveBays = _SniNumberOfDriveBays_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 52, 1, 3),
    _SniNumberOfDriveBays_Type()
)
sniNumberOfDriveBays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNumberOfDriveBays.setStatus("mandatory")


class _SniAccessible_Type(Integer32):
    """Custom type sniAccessible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniAccessible_Type.__name__ = "Integer32"
_SniAccessible_Object = MibTableColumn
sniAccessible = _SniAccessible_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 52, 1, 4),
    _SniAccessible_Type()
)
sniAccessible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAccessible.setStatus("mandatory")
_SniMainboardResourceUsage_Object = MibTable
sniMainboardResourceUsage = _SniMainboardResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 54)
)
if mibBuilder.loadTexts:
    sniMainboardResourceUsage.setStatus("mandatory")
_SniMainboardResourceUsageEntry_Object = MibTableRow
sniMainboardResourceUsageEntry = _SniMainboardResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 54, 1)
)
sniMainboardResourceUsageEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniResourceUsageIndex"),
)
if mibBuilder.loadTexts:
    sniMainboardResourceUsageEntry.setStatus("mandatory")
_SniResourceUsageIndex_Type = Integer32
_SniResourceUsageIndex_Object = MibTableColumn
sniResourceUsageIndex = _SniResourceUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 54, 1, 1),
    _SniResourceUsageIndex_Type()
)
sniResourceUsageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniResourceUsageIndex.setStatus("mandatory")


class _SniBusType_Type(Integer32):
    """Custom type sniBusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e-other", 1),
          ("e-pci", 3),
          ("e-unknown", 0))
    )


_SniBusType_Type.__name__ = "Integer32"
_SniBusType_Object = MibTableColumn
sniBusType = _SniBusType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 54, 1, 2),
    _SniBusType_Type()
)
sniBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBusType.setStatus("mandatory")
_SniBusLoad_Type = DisplayString
_SniBusLoad_Object = MibTableColumn
sniBusLoad = _SniBusLoad_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 54, 1, 3),
    _SniBusLoad_Type()
)
sniBusLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBusLoad.setStatus("mandatory")
_SniHardwarePCIBaseAddress_Object = MibTable
sniHardwarePCIBaseAddress = _SniHardwarePCIBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 56)
)
if mibBuilder.loadTexts:
    sniHardwarePCIBaseAddress.setStatus("mandatory")
_SniHardwarePCIBaseAddressEntry_Object = MibTableRow
sniHardwarePCIBaseAddressEntry = _SniHardwarePCIBaseAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 56, 1)
)
sniHardwarePCIBaseAddressEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniPCIBaseAddressIndex"),
)
if mibBuilder.loadTexts:
    sniHardwarePCIBaseAddressEntry.setStatus("mandatory")
_SniPCIBaseAddressIndex_Type = Integer32
_SniPCIBaseAddressIndex_Object = MibTableColumn
sniPCIBaseAddressIndex = _SniPCIBaseAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 56, 1, 1),
    _SniPCIBaseAddressIndex_Type()
)
sniPCIBaseAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIBaseAddressIndex.setStatus("mandatory")
_SniPCIIndex1_Type = Integer32
_SniPCIIndex1_Object = MibTableColumn
sniPCIIndex1 = _SniPCIIndex1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 56, 1, 2),
    _SniPCIIndex1_Type()
)
sniPCIIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIIndex1.setStatus("mandatory")


class _SniMemoryIOSpace_Type(Integer32):
    """Custom type sniMemoryIOSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-io-space", 4),
          ("e-memory-space", 3),
          ("e-unknown", 0))
    )


_SniMemoryIOSpace_Type.__name__ = "Integer32"
_SniMemoryIOSpace_Object = MibTableColumn
sniMemoryIOSpace = _SniMemoryIOSpace_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 56, 1, 3),
    _SniMemoryIOSpace_Type()
)
sniMemoryIOSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryIOSpace.setStatus("mandatory")


class _SniPrefetchable_Type(Integer32):
    """Custom type sniPrefetchable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniPrefetchable_Type.__name__ = "Integer32"
_SniPrefetchable_Object = MibTableColumn
sniPrefetchable = _SniPrefetchable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 56, 1, 4),
    _SniPrefetchable_Type()
)
sniPrefetchable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPrefetchable.setStatus("mandatory")


class _SniPCIMemoryMapping_Type(Integer32):
    """Custom type sniPCIMemoryMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e-below-1-mbyte", 4),
          ("e-in-32bit-space", 3),
          ("e-in-64bit-space", 5),
          ("e-unknown", 0))
    )


_SniPCIMemoryMapping_Type.__name__ = "Integer32"
_SniPCIMemoryMapping_Object = MibTableColumn
sniPCIMemoryMapping = _SniPCIMemoryMapping_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 56, 1, 5),
    _SniPCIMemoryMapping_Type()
)
sniPCIMemoryMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIMemoryMapping.setStatus("mandatory")
_SniBaseAddress_Type = DisplayString
_SniBaseAddress_Object = MibTableColumn
sniBaseAddress = _SniBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 56, 1, 6),
    _SniBaseAddress_Type()
)
sniBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBaseAddress.setStatus("mandatory")
_SniHardwarePCICharacteristics_Object = MibTable
sniHardwarePCICharacteristics = _SniHardwarePCICharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 58)
)
if mibBuilder.loadTexts:
    sniHardwarePCICharacteristics.setStatus("mandatory")
_SniHardwarePCICharacteristicsEntry_Object = MibTableRow
sniHardwarePCICharacteristicsEntry = _SniHardwarePCICharacteristicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 58, 1)
)
sniHardwarePCICharacteristicsEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniPCICharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    sniHardwarePCICharacteristicsEntry.setStatus("mandatory")
_SniPCICharacteristicsIndex_Type = Integer32
_SniPCICharacteristicsIndex_Object = MibTableColumn
sniPCICharacteristicsIndex = _SniPCICharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 58, 1, 1),
    _SniPCICharacteristicsIndex_Type()
)
sniPCICharacteristicsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCICharacteristicsIndex.setStatus("mandatory")
_SniPCIIndex2_Type = Integer32
_SniPCIIndex2_Object = MibTableColumn
sniPCIIndex2 = _SniPCIIndex2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 58, 1, 2),
    _SniPCIIndex2_Type()
)
sniPCIIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIIndex2.setStatus("mandatory")
_SniCharacteristicNumber_Type = Integer32
_SniCharacteristicNumber_Object = MibTableColumn
sniCharacteristicNumber = _SniCharacteristicNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 58, 1, 3),
    _SniCharacteristicNumber_Type()
)
sniCharacteristicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCharacteristicNumber.setStatus("mandatory")
_SniCharacteristicInfo_Type = DisplayString
_SniCharacteristicInfo_Object = MibTableColumn
sniCharacteristicInfo = _SniCharacteristicInfo_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 58, 1, 4),
    _SniCharacteristicInfo_Type()
)
sniCharacteristicInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCharacteristicInfo.setStatus("mandatory")
_SniModeNumber_Type = Integer32
_SniModeNumber_Object = MibTableColumn
sniModeNumber = _SniModeNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 58, 1, 5),
    _SniModeNumber_Type()
)
sniModeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniModeNumber.setStatus("mandatory")
_SniModeInfo_Type = DisplayString
_SniModeInfo_Object = MibTableColumn
sniModeInfo = _SniModeInfo_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 58, 1, 6),
    _SniModeInfo_Type()
)
sniModeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniModeInfo.setStatus("mandatory")
_SniHardwarePCIInfo_Object = MibTable
sniHardwarePCIInfo = _SniHardwarePCIInfo_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60)
)
if mibBuilder.loadTexts:
    sniHardwarePCIInfo.setStatus("mandatory")
_SniHardwarePCIInfoEntry_Object = MibTableRow
sniHardwarePCIInfoEntry = _SniHardwarePCIInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1)
)
sniHardwarePCIInfoEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniPCIInfoIndex"),
)
if mibBuilder.loadTexts:
    sniHardwarePCIInfoEntry.setStatus("mandatory")
_SniPCIInfoIndex_Type = Integer32
_SniPCIInfoIndex_Object = MibTableColumn
sniPCIInfoIndex = _SniPCIInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 1),
    _SniPCIInfoIndex_Type()
)
sniPCIInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIInfoIndex.setStatus("mandatory")
_SniPCIIndex3_Type = Integer32
_SniPCIIndex3_Object = MibTableColumn
sniPCIIndex3 = _SniPCIIndex3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 2),
    _SniPCIIndex3_Type()
)
sniPCIIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIIndex3.setStatus("mandatory")
_SniDeviceID_Type = Integer32
_SniDeviceID_Object = MibTableColumn
sniDeviceID = _SniDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 3),
    _SniDeviceID_Type()
)
sniDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDeviceID.setStatus("mandatory")
_SniPCIDeviceType_Type = DisplayString
_SniPCIDeviceType_Object = MibTableColumn
sniPCIDeviceType = _SniPCIDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 4),
    _SniPCIDeviceType_Type()
)
sniPCIDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIDeviceType.setStatus("mandatory")
_SniPCIDeviceName_Type = DisplayString
_SniPCIDeviceName_Object = MibTableColumn
sniPCIDeviceName = _SniPCIDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 5),
    _SniPCIDeviceName_Type()
)
sniPCIDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIDeviceName.setStatus("mandatory")
_SniRevisionID_Type = Integer32
_SniRevisionID_Object = MibTableColumn
sniRevisionID = _SniRevisionID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 6),
    _SniRevisionID_Type()
)
sniRevisionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniRevisionID.setStatus("mandatory")
_SniPCIBusNumber_Type = Integer32
_SniPCIBusNumber_Object = MibTableColumn
sniPCIBusNumber = _SniPCIBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 7),
    _SniPCIBusNumber_Type()
)
sniPCIBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIBusNumber.setStatus("mandatory")
_SniPCISlotNumber_Type = Integer32
_SniPCISlotNumber_Object = MibTableColumn
sniPCISlotNumber = _SniPCISlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 8),
    _SniPCISlotNumber_Type()
)
sniPCISlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCISlotNumber.setStatus("mandatory")
_SniPCIVendorID_Type = Integer32
_SniPCIVendorID_Object = MibTableColumn
sniPCIVendorID = _SniPCIVendorID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 9),
    _SniPCIVendorID_Type()
)
sniPCIVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPCIVendorID.setStatus("mandatory")
_SniVendorName_Type = DisplayString
_SniVendorName_Object = MibTableColumn
sniVendorName = _SniVendorName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 10),
    _SniVendorName_Type()
)
sniVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniVendorName.setStatus("mandatory")
_SniBaseClassID_Type = Integer32
_SniBaseClassID_Object = MibTableColumn
sniBaseClassID = _SniBaseClassID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 11),
    _SniBaseClassID_Type()
)
sniBaseClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBaseClassID.setStatus("mandatory")
_SniSubClassID_Type = Integer32
_SniSubClassID_Object = MibTableColumn
sniSubClassID = _SniSubClassID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 12),
    _SniSubClassID_Type()
)
sniSubClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSubClassID.setStatus("mandatory")
_SniProgrammingInterfaceID_Type = Integer32
_SniProgrammingInterfaceID_Object = MibTableColumn
sniProgrammingInterfaceID = _SniProgrammingInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 13),
    _SniProgrammingInterfaceID_Type()
)
sniProgrammingInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniProgrammingInterfaceID.setStatus("mandatory")
_SniBaseClassDescription_Type = DisplayString
_SniBaseClassDescription_Object = MibTableColumn
sniBaseClassDescription = _SniBaseClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 14),
    _SniBaseClassDescription_Type()
)
sniBaseClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBaseClassDescription.setStatus("mandatory")
_SniSubClassDescription_Type = DisplayString
_SniSubClassDescription_Object = MibTableColumn
sniSubClassDescription = _SniSubClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 15),
    _SniSubClassDescription_Type()
)
sniSubClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSubClassDescription.setStatus("mandatory")


class _SniSingleMultiFunction_Type(Integer32):
    """Custom type sniSingleMultiFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e-multi", 4),
          ("e-single", 3),
          ("e-unknown", 0))
    )


_SniSingleMultiFunction_Type.__name__ = "Integer32"
_SniSingleMultiFunction_Object = MibTableColumn
sniSingleMultiFunction = _SniSingleMultiFunction_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 16),
    _SniSingleMultiFunction_Type()
)
sniSingleMultiFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSingleMultiFunction.setStatus("mandatory")
_SniDeviceCommand_Type = Integer32
_SniDeviceCommand_Object = MibTableColumn
sniDeviceCommand = _SniDeviceCommand_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 17),
    _SniDeviceCommand_Type()
)
sniDeviceCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDeviceCommand.setStatus("mandatory")
_SniDeviceStatus_Type = Integer32
_SniDeviceStatus_Object = MibTableColumn
sniDeviceStatus = _SniDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 18),
    _SniDeviceStatus_Type()
)
sniDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDeviceStatus.setStatus("mandatory")
_SniCacheLineSize_Type = Integer32
_SniCacheLineSize_Object = MibTableColumn
sniCacheLineSize = _SniCacheLineSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 19),
    _SniCacheLineSize_Type()
)
sniCacheLineSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCacheLineSize.setStatus("mandatory")
_SniLatencyTimer_Type = Integer32
_SniLatencyTimer_Object = MibTableColumn
sniLatencyTimer = _SniLatencyTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 20),
    _SniLatencyTimer_Type()
)
sniLatencyTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLatencyTimer.setStatus("mandatory")
_SniCompletionCode_Type = Integer32
_SniCompletionCode_Object = MibTableColumn
sniCompletionCode = _SniCompletionCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 21),
    _SniCompletionCode_Type()
)
sniCompletionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCompletionCode.setStatus("mandatory")


class _SniBuildinSelfTestSupport_Type(Integer32):
    """Custom type sniBuildinSelfTestSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniBuildinSelfTestSupport_Type.__name__ = "Integer32"
_SniBuildinSelfTestSupport_Object = MibTableColumn
sniBuildinSelfTestSupport = _SniBuildinSelfTestSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 22),
    _SniBuildinSelfTestSupport_Type()
)
sniBuildinSelfTestSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniBuildinSelfTestSupport.setStatus("mandatory")
_SniInterruptLine_Type = Integer32
_SniInterruptLine_Object = MibTableColumn
sniInterruptLine = _SniInterruptLine_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 23),
    _SniInterruptLine_Type()
)
sniInterruptLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInterruptLine.setStatus("mandatory")


class _SniInterruptPin_Type(Integer32):
    """Custom type sniInterruptPin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("e-inta", 4),
          ("e-intb", 5),
          ("e-intc", 6),
          ("e-intd", 7),
          ("e-none", 3),
          ("e-unknown", 0))
    )


_SniInterruptPin_Type.__name__ = "Integer32"
_SniInterruptPin_Object = MibTableColumn
sniInterruptPin = _SniInterruptPin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 24),
    _SniInterruptPin_Type()
)
sniInterruptPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniInterruptPin.setStatus("mandatory")
_SniMinimumGrant_Type = Integer32
_SniMinimumGrant_Object = MibTableColumn
sniMinimumGrant = _SniMinimumGrant_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 25),
    _SniMinimumGrant_Type()
)
sniMinimumGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMinimumGrant.setStatus("mandatory")
_SniMaximumLatencyTime_Type = Integer32
_SniMaximumLatencyTime_Object = MibTableColumn
sniMaximumLatencyTime = _SniMaximumLatencyTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 26),
    _SniMaximumLatencyTime_Type()
)
sniMaximumLatencyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMaximumLatencyTime.setStatus("mandatory")
_SniSubVendorID_Type = Integer32
_SniSubVendorID_Object = MibTableColumn
sniSubVendorID = _SniSubVendorID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 27),
    _SniSubVendorID_Type()
)
sniSubVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSubVendorID.setStatus("mandatory")
_SniSubSystemID_Type = Integer32
_SniSubSystemID_Object = MibTableColumn
sniSubSystemID = _SniSubSystemID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 28),
    _SniSubSystemID_Type()
)
sniSubSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSubSystemID.setStatus("mandatory")
_SniCIS_Type = DisplayString
_SniCIS_Object = MibTableColumn
sniCIS = _SniCIS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 29),
    _SniCIS_Type()
)
sniCIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniCIS.setStatus("mandatory")
_SniExpROMBaseAddressReg_Type = DisplayString
_SniExpROMBaseAddressReg_Object = MibTableColumn
sniExpROMBaseAddressReg = _SniExpROMBaseAddressReg_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 30),
    _SniExpROMBaseAddressReg_Type()
)
sniExpROMBaseAddressReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniExpROMBaseAddressReg.setStatus("mandatory")
_SniExpansionROMBaseAddress_Type = DisplayString
_SniExpansionROMBaseAddress_Object = MibTableColumn
sniExpansionROMBaseAddress = _SniExpansionROMBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 31),
    _SniExpansionROMBaseAddress_Type()
)
sniExpansionROMBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniExpansionROMBaseAddress.setStatus("mandatory")


class _SniDecodeenabled_Type(Integer32):
    """Custom type sniDecodeenabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e-no", 0),
          ("e-unknown", 2),
          ("e-yes", 1))
    )


_SniDecodeenabled_Type.__name__ = "Integer32"
_SniDecodeenabled_Object = MibTableColumn
sniDecodeenabled = _SniDecodeenabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 32),
    _SniDecodeenabled_Type()
)
sniDecodeenabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDecodeenabled.setStatus("mandatory")
_SniFunctionnumber_Type = Integer32
_SniFunctionnumber_Object = MibTableColumn
sniFunctionnumber = _SniFunctionnumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 33),
    _SniFunctionnumber_Type()
)
sniFunctionnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniFunctionnumber.setStatus("mandatory")
_SniDevicenumber_Type = Integer32
_SniDevicenumber_Object = MibTableColumn
sniDevicenumber = _SniDevicenumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 60, 1, 34),
    _SniDevicenumber_Type()
)
sniDevicenumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDevicenumber.setStatus("mandatory")
_SniMainboardMemoryModulesEx_Object = MibTable
sniMainboardMemoryModulesEx = _SniMainboardMemoryModulesEx_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62)
)
if mibBuilder.loadTexts:
    sniMainboardMemoryModulesEx.setStatus("mandatory")
_SniMainboardMemoryModulesExEntry_Object = MibTableRow
sniMainboardMemoryModulesExEntry = _SniMainboardMemoryModulesExEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1)
)
sniMainboardMemoryModulesExEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniMemoryController2"),
    (0, "DESKSNMP-MIB", "sniMemoryModule2"),
)
if mibBuilder.loadTexts:
    sniMainboardMemoryModulesExEntry.setStatus("mandatory")
_SniMemoryController2_Type = Integer32
_SniMemoryController2_Object = MibTableColumn
sniMemoryController2 = _SniMemoryController2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1, 1),
    _SniMemoryController2_Type()
)
sniMemoryController2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryController2.setStatus("mandatory")
_SniMemoryModule2_Type = Integer32
_SniMemoryModule2_Object = MibTableColumn
sniMemoryModule2 = _SniMemoryModule2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1, 2),
    _SniMemoryModule2_Type()
)
sniMemoryModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryModule2.setStatus("mandatory")
_SniMemoryModuleSerialnumber_Type = DisplayString
_SniMemoryModuleSerialnumber_Object = MibTableColumn
sniMemoryModuleSerialnumber = _SniMemoryModuleSerialnumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1, 3),
    _SniMemoryModuleSerialnumber_Type()
)
sniMemoryModuleSerialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryModuleSerialnumber.setStatus("mandatory")
_SniMemoryModuleManufacturer_Type = DisplayString
_SniMemoryModuleManufacturer_Object = MibTableColumn
sniMemoryModuleManufacturer = _SniMemoryModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1, 4),
    _SniMemoryModuleManufacturer_Type()
)
sniMemoryModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryModuleManufacturer.setStatus("mandatory")
_SniLocationMemoryBank_Type = DisplayString
_SniLocationMemoryBank_Object = MibTableColumn
sniLocationMemoryBank = _SniLocationMemoryBank_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1, 5),
    _SniLocationMemoryBank_Type()
)
sniLocationMemoryBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLocationMemoryBank.setStatus("mandatory")
_SniNumberOfLowLevelDevices_Type = Integer32
_SniNumberOfLowLevelDevices_Object = MibTableColumn
sniNumberOfLowLevelDevices = _SniNumberOfLowLevelDevices_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1, 6),
    _SniNumberOfLowLevelDevices_Type()
)
sniNumberOfLowLevelDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNumberOfLowLevelDevices.setStatus("mandatory")
_SniSpeedMHz_Type = Integer32
_SniSpeedMHz_Object = MibTableColumn
sniSpeedMHz = _SniSpeedMHz_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1, 7),
    _SniSpeedMHz_Type()
)
sniSpeedMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSpeedMHz.setStatus("mandatory")


class _SniMemoryTypeEx_Type(Integer32):
    """Custom type sniMemoryTypeEx based on Integer32"""
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
        *(("e-3dram", 14),
          ("e-cdram", 13),
          ("e-dram", 3),
          ("e-edram", 4),
          ("e-eeprom", 10),
          ("e-eprom", 12),
          ("e-feprom", 11),
          ("e-flash", 9),
          ("e-other", 1),
          ("e-ram", 7),
          ("e-rdram", 17),
          ("e-rom", 8),
          ("e-sdram", 15),
          ("e-sgram", 16),
          ("e-sram", 6),
          ("e-unknown", 2),
          ("e-vram", 5))
    )


_SniMemoryTypeEx_Type.__name__ = "Integer32"
_SniMemoryTypeEx_Object = MibTableColumn
sniMemoryTypeEx = _SniMemoryTypeEx_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1, 8),
    _SniMemoryTypeEx_Type()
)
sniMemoryTypeEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemoryTypeEx.setStatus("mandatory")
_SniMemorymoduleFormfactorandType_Type = DisplayString
_SniMemorymoduleFormfactorandType_Object = MibTableColumn
sniMemorymoduleFormfactorandType = _SniMemorymoduleFormfactorandType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 62, 1, 9),
    _SniMemorymoduleFormfactorandType_Type()
)
sniMemorymoduleFormfactorandType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMemorymoduleFormfactorandType.setStatus("mandatory")
_SniUSER_ObjectIdentity = ObjectIdentity
sniUSER = _SniUSER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64)
)
_SniUsername_Type = DisplayString
_SniUsername_Object = MibScalar
sniUsername = _SniUsername_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 1),
    _SniUsername_Type()
)
sniUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniUsername.setStatus("mandatory")
_SniPhonenumber_Type = DisplayString
_SniPhonenumber_Object = MibScalar
sniPhonenumber = _SniPhonenumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 2),
    _SniPhonenumber_Type()
)
sniPhonenumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPhonenumber.setStatus("mandatory")
_SniPlace_Type = DisplayString
_SniPlace_Object = MibScalar
sniPlace = _SniPlace_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 3),
    _SniPlace_Type()
)
sniPlace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPlace.setStatus("mandatory")
_SniDepartment_Type = DisplayString
_SniDepartment_Object = MibScalar
sniDepartment = _SniDepartment_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 4),
    _SniDepartment_Type()
)
sniDepartment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDepartment.setStatus("mandatory")
_SniJobTitle_Type = DisplayString
_SniJobTitle_Object = MibScalar
sniJobTitle = _SniJobTitle_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 5),
    _SniJobTitle_Type()
)
sniJobTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniJobTitle.setStatus("mandatory")
_SniContact_Type = DisplayString
_SniContact_Object = MibScalar
sniContact = _SniContact_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 6),
    _SniContact_Type()
)
sniContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniContact.setStatus("mandatory")
_SniAdditionalUserInformation_Type = DisplayString
_SniAdditionalUserInformation_Object = MibScalar
sniAdditionalUserInformation = _SniAdditionalUserInformation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 7),
    _SniAdditionalUserInformation_Type()
)
sniAdditionalUserInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAdditionalUserInformation.setStatus("mandatory")
_SniServicePartner_Type = DisplayString
_SniServicePartner_Object = MibScalar
sniServicePartner = _SniServicePartner_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 8),
    _SniServicePartner_Type()
)
sniServicePartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniServicePartner.setStatus("mandatory")
_SniServiceContact_Type = DisplayString
_SniServiceContact_Object = MibScalar
sniServiceContact = _SniServiceContact_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 9),
    _SniServiceContact_Type()
)
sniServiceContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniServiceContact.setStatus("mandatory")
_SniEndOfContract_Type = DisplayString
_SniEndOfContract_Object = MibScalar
sniEndOfContract = _SniEndOfContract_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 10),
    _SniEndOfContract_Type()
)
sniEndOfContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniEndOfContract.setStatus("mandatory")
_SniAdditionalServiceInformation_Type = DisplayString
_SniAdditionalServiceInformation_Object = MibScalar
sniAdditionalServiceInformation = _SniAdditionalServiceInformation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 11),
    _SniAdditionalServiceInformation_Type()
)
sniAdditionalServiceInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAdditionalServiceInformation.setStatus("mandatory")
_SniGeneralInformation_Type = DisplayString
_SniGeneralInformation_Object = MibScalar
sniGeneralInformation = _SniGeneralInformation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 64, 12),
    _SniGeneralInformation_Type()
)
sniGeneralInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGeneralInformation.setStatus("mandatory")
_SniNetwork_Object = MibTable
sniNetwork = _SniNetwork_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65)
)
if mibBuilder.loadTexts:
    sniNetwork.setStatus("mandatory")
_SniNetworkEntry_Object = MibTableRow
sniNetworkEntry = _SniNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1)
)
sniNetworkEntry.setIndexNames(
    (0, "DESKSNMP-MIB", "sniNetworkAdapterIndex"),
)
if mibBuilder.loadTexts:
    sniNetworkEntry.setStatus("mandatory")
_SniNetworkAdapterIndex_Type = Integer32
_SniNetworkAdapterIndex_Object = MibTableColumn
sniNetworkAdapterIndex = _SniNetworkAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 1),
    _SniNetworkAdapterIndex_Type()
)
sniNetworkAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNetworkAdapterIndex.setStatus("mandatory")
_SniNetworkAdapter_Type = DisplayString
_SniNetworkAdapter_Object = MibTableColumn
sniNetworkAdapter = _SniNetworkAdapter_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 2),
    _SniNetworkAdapter_Type()
)
sniNetworkAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniNetworkAdapter.setStatus("mandatory")
_SniMACAddress_Type = DisplayString
_SniMACAddress_Object = MibTableColumn
sniMACAddress = _SniMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 3),
    _SniMACAddress_Type()
)
sniMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMACAddress.setStatus("mandatory")
_SniComputerName_Type = DisplayString
_SniComputerName_Object = MibTableColumn
sniComputerName = _SniComputerName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 4),
    _SniComputerName_Type()
)
sniComputerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniComputerName.setStatus("mandatory")
_SniDHCPServer_Type = DisplayString
_SniDHCPServer_Object = MibTableColumn
sniDHCPServer = _SniDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 5),
    _SniDHCPServer_Type()
)
sniDHCPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDHCPServer.setStatus("mandatory")
_SniDNSHostname_Type = DisplayString
_SniDNSHostname_Object = MibTableColumn
sniDNSHostname = _SniDNSHostname_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 6),
    _SniDNSHostname_Type()
)
sniDNSHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDNSHostname.setStatus("mandatory")
_SniDNSDomainname_Type = DisplayString
_SniDNSDomainname_Object = MibTableColumn
sniDNSDomainname = _SniDNSDomainname_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 7),
    _SniDNSDomainname_Type()
)
sniDNSDomainname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDNSDomainname.setStatus("mandatory")
_SniDNSServer1_Type = DisplayString
_SniDNSServer1_Object = MibTableColumn
sniDNSServer1 = _SniDNSServer1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 8),
    _SniDNSServer1_Type()
)
sniDNSServer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDNSServer1.setStatus("mandatory")
_SniDNSServer2_Type = DisplayString
_SniDNSServer2_Object = MibTableColumn
sniDNSServer2 = _SniDNSServer2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 9),
    _SniDNSServer2_Type()
)
sniDNSServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDNSServer2.setStatus("mandatory")
_SniDNSServer3_Type = DisplayString
_SniDNSServer3_Object = MibTableColumn
sniDNSServer3 = _SniDNSServer3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 10),
    _SniDNSServer3_Type()
)
sniDNSServer3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDNSServer3.setStatus("mandatory")
_SniDNSServer4_Type = DisplayString
_SniDNSServer4_Object = MibTableColumn
sniDNSServer4 = _SniDNSServer4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 11),
    _SniDNSServer4_Type()
)
sniDNSServer4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDNSServer4.setStatus("mandatory")
_SniDNSServer5_Type = DisplayString
_SniDNSServer5_Object = MibTableColumn
sniDNSServer5 = _SniDNSServer5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 12),
    _SniDNSServer5_Type()
)
sniDNSServer5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniDNSServer5.setStatus("mandatory")
_SniIPAddress1_Type = DisplayString
_SniIPAddress1_Object = MibTableColumn
sniIPAddress1 = _SniIPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 13),
    _SniIPAddress1_Type()
)
sniIPAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIPAddress1.setStatus("mandatory")
_SniIPAddress2_Type = DisplayString
_SniIPAddress2_Object = MibTableColumn
sniIPAddress2 = _SniIPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 14),
    _SniIPAddress2_Type()
)
sniIPAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIPAddress2.setStatus("mandatory")
_SniIPAddress3_Type = DisplayString
_SniIPAddress3_Object = MibTableColumn
sniIPAddress3 = _SniIPAddress3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 15),
    _SniIPAddress3_Type()
)
sniIPAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIPAddress3.setStatus("mandatory")
_SniIPAddress4_Type = DisplayString
_SniIPAddress4_Object = MibTableColumn
sniIPAddress4 = _SniIPAddress4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 16),
    _SniIPAddress4_Type()
)
sniIPAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIPAddress4.setStatus("mandatory")
_SniIPAddress5_Type = DisplayString
_SniIPAddress5_Object = MibTableColumn
sniIPAddress5 = _SniIPAddress5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 17),
    _SniIPAddress5_Type()
)
sniIPAddress5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniIPAddress5.setStatus("mandatory")
_SniSubnetMask1_Type = DisplayString
_SniSubnetMask1_Object = MibTableColumn
sniSubnetMask1 = _SniSubnetMask1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 18),
    _SniSubnetMask1_Type()
)
sniSubnetMask1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSubnetMask1.setStatus("mandatory")
_SniSubnetMask2_Type = DisplayString
_SniSubnetMask2_Object = MibTableColumn
sniSubnetMask2 = _SniSubnetMask2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 19),
    _SniSubnetMask2_Type()
)
sniSubnetMask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSubnetMask2.setStatus("mandatory")
_SniSubnetMask3_Type = DisplayString
_SniSubnetMask3_Object = MibTableColumn
sniSubnetMask3 = _SniSubnetMask3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 20),
    _SniSubnetMask3_Type()
)
sniSubnetMask3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSubnetMask3.setStatus("mandatory")
_SniSubnetMask4_Type = DisplayString
_SniSubnetMask4_Object = MibTableColumn
sniSubnetMask4 = _SniSubnetMask4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 21),
    _SniSubnetMask4_Type()
)
sniSubnetMask4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSubnetMask4.setStatus("mandatory")
_SniSubnetMask5_Type = DisplayString
_SniSubnetMask5_Object = MibTableColumn
sniSubnetMask5 = _SniSubnetMask5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 22),
    _SniSubnetMask5_Type()
)
sniSubnetMask5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniSubnetMask5.setStatus("mandatory")
_SniGateway1_Type = DisplayString
_SniGateway1_Object = MibTableColumn
sniGateway1 = _SniGateway1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 23),
    _SniGateway1_Type()
)
sniGateway1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGateway1.setStatus("mandatory")
_SniGateway2_Type = DisplayString
_SniGateway2_Object = MibTableColumn
sniGateway2 = _SniGateway2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 24),
    _SniGateway2_Type()
)
sniGateway2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGateway2.setStatus("mandatory")
_SniGateway3_Type = DisplayString
_SniGateway3_Object = MibTableColumn
sniGateway3 = _SniGateway3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 25),
    _SniGateway3_Type()
)
sniGateway3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGateway3.setStatus("mandatory")
_SniGateway4_Type = DisplayString
_SniGateway4_Object = MibTableColumn
sniGateway4 = _SniGateway4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 26),
    _SniGateway4_Type()
)
sniGateway4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGateway4.setStatus("mandatory")
_SniGateway5_Type = DisplayString
_SniGateway5_Object = MibTableColumn
sniGateway5 = _SniGateway5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 1, 65, 1, 27),
    _SniGateway5_Type()
)
sniGateway5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniGateway5.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DESKSNMP-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniExtensions": sniExtensions,
       "sniDesktopMgmt": sniDesktopMgmt,
       "sniDeskInfo": sniDeskInfo,
       "sniPCInformation": sniPCInformation,
       "sniPCManufacturer": sniPCManufacturer,
       "sniPCName": sniPCName,
       "sniProductVersion": sniProductVersion,
       "sniPCSerialNumber": sniPCSerialNumber,
       "sniChassisType": sniChassisType,
       "sniChassisColor": sniChassisColor,
       "sniHousingGeometry": sniHousingGeometry,
       "sniCustomerSpecificSerialNumber": sniCustomerSpecificSerialNumber,
       "sniUUID": sniUUID,
       "sniBios": sniBios,
       "sniBiosManufacturer": sniBiosManufacturer,
       "sniAdaptions": sniAdaptions,
       "sniFeatures": sniFeatures,
       "sniBiosVersion": sniBiosVersion,
       "sniLoaderVersion": sniLoaderVersion,
       "sniRomSizekB": sniRomSizekB,
       "sniBiosDate": sniBiosDate,
       "sniStatus": sniStatus,
       "sniStartaddress": sniStartaddress,
       "sniEndaddress": sniEndaddress,
       "sniISABus": sniISABus,
       "sniMCABus": sniMCABus,
       "sniEISABus": sniEISABus,
       "sniPCIBus": sniPCIBus,
       "sniPCMCIAInterface": sniPCMCIAInterface,
       "sniPlugandPlayPnP": sniPlugandPlayPnP,
       "sniAdvPowerManagemAPM": sniAdvPowerManagemAPM,
       "sniVLBus": sniVLBus,
       "sniESCDBus": sniESCDBus,
       "sniIRDABus": sniIRDABus,
       "sniBootfromCDROM": sniBootfromCDROM,
       "sniBootfromPCMCIA": sniBootfromPCMCIA,
       "sniBiosShadowing": sniBiosShadowing,
       "sniSavetoDiskStd": sniSavetoDiskStd,
       "sniSecurity": sniSecurity,
       "sniUSB": sniUSB,
       "sniSoftwarePowerOff": sniSoftwarePowerOff,
       "sniRemoteOn": sniRemoteOn,
       "sniAPMSpecificVersion": sniAPMSpecificVersion,
       "sniPNPSpecificVersion": sniPNPSpecificVersion,
       "sniFlashBIOS": sniFlashBIOS,
       "sniPC98": sniPC98,
       "sniBootDeviceSelectable": sniBootDeviceSelectable,
       "sniBIOSRomSocketed": sniBIOSRomSocketed,
       "sniEnhancedDiskDriveEDD": sniEnhancedDiskDriveEDD,
       "sniNEC9800FloppySupport": sniNEC9800FloppySupport,
       "sniToshibaFloppySupport": sniToshibaFloppySupport,
       "sni360kBFloppySupport": sni360kBFloppySupport,
       "sni720kBFloppySupport": sni720kBFloppySupport,
       "sni1MB2FloppySupport": sni1MB2FloppySupport,
       "sni2MB88FloppySupport": sni2MB88FloppySupport,
       "sniInt5PrintScreenService": sniInt5PrintScreenService,
       "sniInt9Keyboard8042Supp": sniInt9Keyboard8042Supp,
       "sniSoftwarePowerOn": sniSoftwarePowerOn,
       "sniISAMemoryGapSupport": sniISAMemoryGapSupport,
       "sniIEEE1394Support": sniIEEE1394Support,
       "sniDMISupport": sniDMISupport,
       "sniACPISupport": sniACPISupport,
       "sniSystemMonitoring": sniSystemMonitoring,
       "sniInt14SerialServices": sniInt14SerialServices,
       "sniInt17PrinterServices": sniInt17PrinterServices,
       "sniInt10CGAVideoServices": sniInt10CGAVideoServices,
       "sniAGPSupport": sniAGPSupport,
       "sniI2OBootSupport": sniI2OBootSupport,
       "sniLS120BootSupport": sniLS120BootSupport,
       "sniAtapiZIPDriveBootSupport": sniAtapiZIPDriveBootSupport,
       "sniSMARTBatterieSupport": sniSMARTBatterieSupport,
       "sniMemory": sniMemory,
       "sniPhysicalMemoryMB": sniPhysicalMemoryMB,
       "sniBaseMemorykB": sniBaseMemorykB,
       "sniFreePhysicalMemorykB": sniFreePhysicalMemorykB,
       "sniFreeUserResourcesPercentage": sniFreeUserResourcesPercentage,
       "sniFreeGDIResourcesPercentage": sniFreeGDIResourcesPercentage,
       "sniVirtualMemoryType": sniVirtualMemoryType,
       "sniSwapFileName": sniSwapFileName,
       "sniSwapFileSizekB": sniSwapFileSizekB,
       "sniSwapFileUsedPercentage": sniSwapFileUsedPercentage,
       "sniEMMSizekB": sniEMMSizekB,
       "sniEMMFreekB": sniEMMFreekB,
       "sniEMMDriverVersion": sniEMMDriverVersion,
       "sniEMMDriverName": sniEMMDriverName,
       "sniXMSSizekB": sniXMSSizekB,
       "sniXMSFreeMemorykB": sniXMSFreeMemorykB,
       "sniXMSDriverVersion": sniXMSDriverVersion,
       "sniXMSDriverName": sniXMSDriverName,
       "sniGraphic": sniGraphic,
       "sniGraphicCardManufacturer": sniGraphicCardManufacturer,
       "sniGraphicController": sniGraphicController,
       "sniGraphicCardDate": sniGraphicCardDate,
       "sniShadowed": sniShadowed,
       "sniGraphicType": sniGraphicType,
       "sniDriver": sniDriver,
       "sniGraphicmode": sniGraphicmode,
       "snivertResolutionPixel": snivertResolutionPixel,
       "snihorResolutionPixel": snihorResolutionPixel,
       "sniColorResolution": sniColorResolution,
       "sniRefreshrateHz": sniRefreshrateHz,
       "sniScanMode": sniScanMode,
       "sniMinRefreshrateHz": sniMinRefreshrateHz,
       "sniMaxRefreshrateHz": sniMaxRefreshrateHz,
       "sniMemorySizeKB": sniMemorySizeKB,
       "sniMemoryType": sniMemoryType,
       "sniGraphicCardLocation": sniGraphicCardLocation,
       "sniStandardBios": sniStandardBios,
       "sniVESAExtensions": sniVESAExtensions,
       "sniDPMS": sniDPMS,
       "sniDDC": sniDDC,
       "sniShadowing": sniShadowing,
       "sniUpgradable": sniUpgradable,
       "sniMonitor": sniMonitor,
       "sniMonitorName": sniMonitorName,
       "sniSizeInch": sniSizeInch,
       "sniDDCSupport": sniDDCSupport,
       "sniDPMSSupport": sniDPMSSupport,
       "sniMaxhorizResolution": sniMaxhorizResolution,
       "sniMaxverticalResolution": sniMaxverticalResolution,
       "sniMaxhorizontalFrequency": sniMaxhorizontalFrequency,
       "sniMinhorizontalFrequency": sniMinhorizontalFrequency,
       "sniMaximumRefreshrate": sniMaximumRefreshrate,
       "sniMinimumRefreshrate": sniMinimumRefreshrate,
       "sniSerialNumber": sniSerialNumber,
       "sniWeekofManufacture": sniWeekofManufacture,
       "sniYearofManufacture": sniYearofManufacture,
       "sniOperatingSystem": sniOperatingSystem,
       "sniOSName": sniOSName,
       "sniOSVersion": sniOSVersion,
       "sniOSLanguage": sniOSLanguage,
       "sniOSInstallationDirectory": sniOSInstallationDirectory,
       "sniOSNameSecondary": sniOSNameSecondary,
       "sniOSVersionSecondary": sniOSVersionSecondary,
       "sniOSLanguageSecondary": sniOSLanguageSecondary,
       "sniOSInstallDirSec": sniOSInstallDirSec,
       "sniPreInstallationVersion": sniPreInstallationVersion,
       "sniPreInstallationLanguage": sniPreInstallationLanguage,
       "sniSoftware": sniSoftware,
       "sniSoftwareEntry": sniSoftwareEntry,
       "sniSoftwareIndex": sniSoftwareIndex,
       "sniSoftwareName": sniSoftwareName,
       "sniSoftwareVersion": sniSoftwareVersion,
       "sniInstallationDirectory": sniInstallationDirectory,
       "sniAtPreInstallTime": sniAtPreInstallTime,
       "sniVersion": sniVersion,
       "sniHardware": sniHardware,
       "sniHardwareEntry": sniHardwareEntry,
       "sniHardwareIndex": sniHardwareIndex,
       "sniHardwareName": sniHardwareName,
       "sniDriverDirectory": sniDriverDirectory,
       "sniLogicalDrives": sniLogicalDrives,
       "sniLogicalDrivesEntry": sniLogicalDrivesEntry,
       "sniDriveletter": sniDriveletter,
       "sniLogicalDriveType": sniLogicalDriveType,
       "sniVolumename": sniVolumename,
       "sniLogicalDriveSizekB": sniLogicalDriveSizekB,
       "sniLogicalDriveFreeSpacekB": sniLogicalDriveFreeSpacekB,
       "sniLogicalDriveSectorSizeByte": sniLogicalDriveSectorSizeByte,
       "sniClusterSizeByte": sniClusterSizeByte,
       "sniSectorsPerCluster": sniSectorsPerCluster,
       "sniClusters": sniClusters,
       "sniSectors": sniSectors,
       "sniNetworkpath": sniNetworkpath,
       "sniLogicalDrivePartitionName": sniLogicalDrivePartitionName,
       "sniLogicalDrivePartitionSizekB": sniLogicalDrivePartitionSizekB,
       "sniLogicalDrivePartitionFreeSpacekB": sniLogicalDrivePartitionFreeSpacekB,
       "sniLogicalDrivePartitionLabel": sniLogicalDrivePartitionLabel,
       "sniLogicalDrivePartitionFilesystem": sniLogicalDrivePartitionFilesystem,
       "sniLogicalDrivePartitionCompressed": sniLogicalDrivePartitionCompressed,
       "sniLogicalDrivePartitionEncrypted": sniLogicalDrivePartitionEncrypted,
       "sniLogicalDrivePartitionActive": sniLogicalDrivePartitionActive,
       "sniLogicalDrivePartitionBootable": sniLogicalDrivePartitionBootable,
       "sniPhysicalDrives": sniPhysicalDrives,
       "sniPhysicalDrivesEntry": sniPhysicalDrivesEntry,
       "sniPhysicalDrive": sniPhysicalDrive,
       "sniPhysicalDriveName": sniPhysicalDriveName,
       "sniPhysicalDriveType": sniPhysicalDriveType,
       "sniInterface": sniInterface,
       "sniMediaLoaded": sniMediaLoaded,
       "sniRemovableDrive": sniRemovableDrive,
       "sniRemovableMedia": sniRemovableMedia,
       "sniSCSIID": sniSCSIID,
       "sniSCSILUN": sniSCSILUN,
       "sniPhysicalDriveTotalSpacekB": sniPhysicalDriveTotalSpacekB,
       "sniTracks": sniTracks,
       "sniSectorsPerTrack": sniSectorsPerTrack,
       "sniHeads": sniHeads,
       "sniWritePreComp": sniWritePreComp,
       "sniLandingZone": sniLandingZone,
       "sniPhysicalDriveSectorSizeByte": sniPhysicalDriveSectorSizeByte,
       "sniBadBlocks": sniBadBlocks,
       "sniPhysicalDrivePartitions": sniPhysicalDrivePartitions,
       "sniPhysicalDriveLocation": sniPhysicalDriveLocation,
       "sniSMART": sniSMART,
       "sniSMARTCrossreference": sniSMARTCrossreference,
       "sniPartitions": sniPartitions,
       "sniPartitionsEntry": sniPartitionsEntry,
       "sniPhysicalDriveIndex": sniPhysicalDriveIndex,
       "sniPartitionIndex": sniPartitionIndex,
       "sniPartitionName": sniPartitionName,
       "sniPartitionSizekB": sniPartitionSizekB,
       "sniPartitionFreeSpacekB": sniPartitionFreeSpacekB,
       "sniLabel": sniLabel,
       "sniPartitionFilesystem": sniPartitionFilesystem,
       "sniPartitionCompressed": sniPartitionCompressed,
       "sniPartitionEncrypted": sniPartitionEncrypted,
       "sniPartitionActive": sniPartitionActive,
       "sniPartitionBootable": sniPartitionBootable,
       "sniMainboard": sniMainboard,
       "sniMainboardManufacturer": sniMainboardManufacturer,
       "sniMainboardName": sniMainboardName,
       "sniMainboardVersion": sniMainboardVersion,
       "sniProductID": sniProductID,
       "sniProductType": sniProductType,
       "sniMaxMemoryMB": sniMaxMemoryMB,
       "sniUsedMemorySlots": sniUsedMemorySlots,
       "sniNumberMemorySlots": sniNumberMemorySlots,
       "sniOnBoardMouse": sniOnBoardMouse,
       "sniHarddiskAccelerator": sniHarddiskAccelerator,
       "sniMainboardGSNumber": sniMainboardGSNumber,
       "sniMainboardVariant": sniMainboardVariant,
       "sniMainboardProcessors": sniMainboardProcessors,
       "sniMainboardProcessorsEntry": sniMainboardProcessorsEntry,
       "sniProcessorIndex": sniProcessorIndex,
       "sniProcessorType": sniProcessorType,
       "sniFamily": sniFamily,
       "sniProcessorVersion": sniProcessorVersion,
       "sniCurrentProcSpeedMHz": sniCurrentProcSpeedMHz,
       "sniMaxBoardSpeedMHz": sniMaxBoardSpeedMHz,
       "sniProcessorSerialnumber": sniProcessorSerialnumber,
       "sniMainboardCache": sniMainboardCache,
       "sniMainboardCacheEntry": sniMainboardCacheEntry,
       "sniCacheIndex": sniCacheIndex,
       "sniCacheActive": sniCacheActive,
       "sniCacheSizekB": sniCacheSizekB,
       "sniMaximumSizekB": sniMaximumSizekB,
       "sniLevel": sniLevel,
       "sniCacheBurstType": sniCacheBurstType,
       "sniCacheSynchron": sniCacheSynchron,
       "sniCacheSRAM": sniCacheSRAM,
       "sniBurstTypeSupport": sniBurstTypeSupport,
       "sniSynchronSupport": sniSynchronSupport,
       "sniSRAMSupport": sniSRAMSupport,
       "sniWriteThrough": sniWriteThrough,
       "sniWriteBack": sniWriteBack,
       "sniDataCache": sniDataCache,
       "sniInstructionCache": sniInstructionCache,
       "sniInternal": sniInternal,
       "sniInSocket": sniInSocket,
       "sniMainboardPorts": sniMainboardPorts,
       "sniMainboardPortsEntry": sniMainboardPortsEntry,
       "sniPortIndex": sniPortIndex,
       "sniPortName": sniPortName,
       "sniPortType": sniPortType,
       "sniIOBaseAddress": sniIOBaseAddress,
       "sniPortIRQ": sniPortIRQ,
       "sniPortDMA": sniPortDMA,
       "sniMainboardSystemSlots": sniMainboardSystemSlots,
       "sniMainboardSystemSlotsEntry": sniMainboardSystemSlotsEntry,
       "sniSystemSlotIndex": sniSystemSlotIndex,
       "sniSystemSlotName": sniSystemSlotName,
       "sniSystemSlotType": sniSystemSlotType,
       "sniNumber": sniNumber,
       "sniInUse": sniInUse,
       "sniBusWidth": sniBusWidth,
       "sniSlotLength": sniSlotLength,
       "sniSharedSlot": sniSharedSlot,
       "sniMainboardOnboardDevices": sniMainboardOnboardDevices,
       "sniMainboardOnboardDevicesEntry": sniMainboardOnboardDevicesEntry,
       "sniOnboardDeviceIndex": sniOnboardDeviceIndex,
       "sniOnboardDeviceName": sniOnboardDeviceName,
       "sniOnboardDeviceType": sniOnboardDeviceType,
       "sniOnboardDeviceActive": sniOnboardDeviceActive,
       "sniMainboardMemory": sniMainboardMemory,
       "sniMainboardMemoryEntry": sniMainboardMemoryEntry,
       "sniMemoryControllerIndex": sniMemoryControllerIndex,
       "sniNumberOfMemoryModules": sniNumberOfMemoryModules,
       "sniMaxNumberofModules": sniMaxNumberofModules,
       "sniMaximumModuleSizeMB": sniMaximumModuleSizeMB,
       "sniSupportedSpeeds": sniSupportedSpeeds,
       "sniErrorCorrectionECC": sniErrorCorrectionECC,
       "sniStandardSupport": sniStandardSupport,
       "sniFastPageModeSupport": sniFastPageModeSupport,
       "sniEDOSupport": sniEDOSupport,
       "sniParitySupport": sniParitySupport,
       "sniECCSupport": sniECCSupport,
       "sniSIMMSupport": sniSIMMSupport,
       "sniDIMMSupport": sniDIMMSupport,
       "sniRIMMSupport": sniRIMMSupport,
       "sniMaximumNumberOfLowLevelDevices": sniMaximumNumberOfLowLevelDevices,
       "sniTotalNumberOfLowLevelDevices": sniTotalNumberOfLowLevelDevices,
       "sniMainboardMemoryModules": sniMainboardMemoryModules,
       "sniMainboardMemoryModulesEntry": sniMainboardMemoryModulesEntry,
       "sniMemoryController": sniMemoryController,
       "sniMemoryModule": sniMemoryModule,
       "sniMemoryModuleName": sniMemoryModuleName,
       "sniModuleSizeMB": sniModuleSizeMB,
       "sniSpeedns": sniSpeedns,
       "sniStandardMemoryModule": sniStandardMemoryModule,
       "sniEDO": sniEDO,
       "sniSIMM": sniSIMM,
       "sniDIMM": sniDIMM,
       "sniFastPageMode": sniFastPageMode,
       "sniParity": sniParity,
       "sniECC": sniECC,
       "sniMemoryBank": sniMemoryBank,
       "sniAttachedMemoryBank": sniAttachedMemoryBank,
       "sniRIMM": sniRIMM,
       "sniStateOfSupplySystemData": sniStateOfSupplySystemData,
       "sniSystemName": sniSystemName,
       "sniIdentNumber": sniIdentNumber,
       "sniSystemSerialNumber": sniSystemSerialNumber,
       "sniProductionMonth": sniProductionMonth,
       "sniStateOfSupplyMainboard": sniStateOfSupplyMainboard,
       "sniProductName": sniProductName,
       "sniGSNumber": sniGSNumber,
       "sniMainboardSerialNumber": sniMainboardSerialNumber,
       "sniBIOSVersion": sniBIOSVersion,
       "sniStateOfSupplyInternalDevices": sniStateOfSupplyInternalDevices,
       "sniStateOfSupplyInternalDevicesEntry": sniStateOfSupplyInternalDevicesEntry,
       "sniDeviceIndex": sniDeviceIndex,
       "sniDeviceName": sniDeviceName,
       "sniDeviceType": sniDeviceType,
       "sniDeviceSerialnumber": sniDeviceSerialnumber,
       "sniNumberofDevices": sniNumberofDevices,
       "sniStateOfSupplyAddOnModules": sniStateOfSupplyAddOnModules,
       "sniStateOfSupplyAddOnModulesEntry": sniStateOfSupplyAddOnModulesEntry,
       "sniModuleIndex": sniModuleIndex,
       "sniModuleName": sniModuleName,
       "sniModuleType": sniModuleType,
       "sniModuleSerialnumber": sniModuleSerialnumber,
       "sniNumberofModules": sniNumberofModules,
       "sniStateOfSupplyAddOnBoards": sniStateOfSupplyAddOnBoards,
       "sniStateOfSupplyAddOnBoardsEntry": sniStateOfSupplyAddOnBoardsEntry,
       "sniBoardIndex": sniBoardIndex,
       "sniBoardName": sniBoardName,
       "sniBoardType": sniBoardType,
       "sniBoardSerialnumber": sniBoardSerialnumber,
       "sniNumberofBoards": sniNumberofBoards,
       "sniVendorID": sniVendorID,
       "sniBoardIRQ": sniBoardIRQ,
       "sniBoardDMA": sniBoardDMA,
       "sniIOAddress": sniIOAddress,
       "sniMemoryMapping": sniMemoryMapping,
       "sniStateOfSupplySCSIDevices": sniStateOfSupplySCSIDevices,
       "sniStateOfSupplySCSIDevicesEntry": sniStateOfSupplySCSIDevicesEntry,
       "sniSCSIDeviceIndex": sniSCSIDeviceIndex,
       "sniSCSIDeviceName": sniSCSIDeviceName,
       "sniSCSIDeviceType": sniSCSIDeviceType,
       "sniTargetID": sniTargetID,
       "sniHostAdapterID": sniHostAdapterID,
       "sniCapacity": sniCapacity,
       "sniSCSIDeviceSerialnumber": sniSCSIDeviceSerialnumber,
       "sniInfo": sniInfo,
       "sniNumberOfSCSIDevices": sniNumberOfSCSIDevices,
       "sniAntiVirus": sniAntiVirus,
       "sniAntiVirusEntry": sniAntiVirusEntry,
       "sniAntiVirusProgramIndex": sniAntiVirusProgramIndex,
       "sniAntiVirusLogfile": sniAntiVirusLogfile,
       "sniScannerName": sniScannerName,
       "sniErrorKeyword1": sniErrorKeyword1,
       "sniErrorKeyword2": sniErrorKeyword2,
       "sniErrorKeyword3": sniErrorKeyword3,
       "sniErrorKeyword4": sniErrorKeyword4,
       "sniErrorKeyword5": sniErrorKeyword5,
       "sniErrorKeyword6": sniErrorKeyword6,
       "sniErrorKeyword7": sniErrorKeyword7,
       "sniErrorKeyword8": sniErrorKeyword8,
       "sniErrorKeyword9": sniErrorKeyword9,
       "sniErrorKeyword10": sniErrorKeyword10,
       "sniWarningKeyword1": sniWarningKeyword1,
       "sniWarningKeyword2": sniWarningKeyword2,
       "sniWarningKeyword3": sniWarningKeyword3,
       "sniWarningKeyword4": sniWarningKeyword4,
       "sniWarningKeyword5": sniWarningKeyword5,
       "sniWarningKeyword6": sniWarningKeyword6,
       "sniWarningKeyword7": sniWarningKeyword7,
       "sniWarningKeyword8": sniWarningKeyword8,
       "sniWarningKeyword9": sniWarningKeyword9,
       "sniWarningKeyword10": sniWarningKeyword10,
       "sniDistinguishWarningError": sniDistinguishWarningError,
       "sniMouse": sniMouse,
       "sniMouseManufacturer": sniMouseManufacturer,
       "sniMouseDriverName": sniMouseDriverName,
       "sniDriverVersion": sniDriverVersion,
       "sniMouseInterface": sniMouseInterface,
       "sniMouseIRQ": sniMouseIRQ,
       "sniMousePort": sniMousePort,
       "sniSupportedButtons": sniSupportedButtons,
       "sniButtonsExchanged": sniButtonsExchanged,
       "sniSpeedPercentage": sniSpeedPercentage,
       "sniShowMouseTrails": sniShowMouseTrails,
       "sniKeyboard": sniKeyboard,
       "sniKeyboardType": sniKeyboardType,
       "sniLayout": sniLayout,
       "sniInterfaceType": sniInterfaceType,
       "sniCodepage": sniCodepage,
       "sniWindowsDriver": sniWindowsDriver,
       "sniDOSDriver": sniDOSDriver,
       "sniDeskViewVersion": sniDeskViewVersion,
       "sniSysInf32Version": sniSysInf32Version,
       "sniSysInf16Version": sniSysInf16Version,
       "sniDeskInfoAgentVersion": sniDeskInfoAgentVersion,
       "sniDINetVersion": sniDINetVersion,
       "sniDNAgentVersion": sniDNAgentVersion,
       "sniDNBrowserVersion": sniDNBrowserVersion,
       "sniSMARTValues": sniSMARTValues,
       "sniSMARTValuesEntry": sniSMARTValuesEntry,
       "sniSMARTIndex": sniSMARTIndex,
       "sniPhysicalDriveCrossreference": sniPhysicalDriveCrossreference,
       "sniSMARTID": sniSMARTID,
       "sniSMARTName": sniSMARTName,
       "sniSMARTErrorThreshold": sniSMARTErrorThreshold,
       "sniSMARTWarningThreshold": sniSMARTWarningThreshold,
       "sniCurrentSMARTValue": sniCurrentSMARTValue,
       "sniSMARTState": sniSMARTState,
       "sniHardwarePowersupply": sniHardwarePowersupply,
       "sniHardwarePowersupplyEntry": sniHardwarePowersupplyEntry,
       "sniPowersupplyIndex": sniPowersupplyIndex,
       "sniPowersupplySerialNumber": sniPowersupplySerialNumber,
       "sniPowersupplyGSLevel": sniPowersupplyGSLevel,
       "sniPowersupplyRevision": sniPowersupplyRevision,
       "sniPowersupplyManufacturingDate": sniPowersupplyManufacturingDate,
       "sniOutputPowerW": sniOutputPowerW,
       "sniMonitorOutletSupported": sniMonitorOutletSupported,
       "sniMonitorOutlet": sniMonitorOutlet,
       "sniVoltage5V": sniVoltage5V,
       "sniVoltage12V": sniVoltage12V,
       "sniMin5VCurrentA": sniMin5VCurrentA,
       "sniOutputCurrentmA": sniOutputCurrentmA,
       "sniPulsPerRevolution": sniPulsPerRevolution,
       "sniPowersFanControlSupp": sniPowersFanControlSupp,
       "sniPowersupplyFanSpeed": sniPowersupplyFanSpeed,
       "sniPowersupplyFanControl": sniPowersupplyFanControl,
       "sniHardwareDriveBays": sniHardwareDriveBays,
       "sniHardwareDriveBaysEntry": sniHardwareDriveBaysEntry,
       "sniDriveBayIndex": sniDriveBayIndex,
       "sniDriveBayType": sniDriveBayType,
       "sniNumberOfDriveBays": sniNumberOfDriveBays,
       "sniAccessible": sniAccessible,
       "sniMainboardResourceUsage": sniMainboardResourceUsage,
       "sniMainboardResourceUsageEntry": sniMainboardResourceUsageEntry,
       "sniResourceUsageIndex": sniResourceUsageIndex,
       "sniBusType": sniBusType,
       "sniBusLoad": sniBusLoad,
       "sniHardwarePCIBaseAddress": sniHardwarePCIBaseAddress,
       "sniHardwarePCIBaseAddressEntry": sniHardwarePCIBaseAddressEntry,
       "sniPCIBaseAddressIndex": sniPCIBaseAddressIndex,
       "sniPCIIndex1": sniPCIIndex1,
       "sniMemoryIOSpace": sniMemoryIOSpace,
       "sniPrefetchable": sniPrefetchable,
       "sniPCIMemoryMapping": sniPCIMemoryMapping,
       "sniBaseAddress": sniBaseAddress,
       "sniHardwarePCICharacteristics": sniHardwarePCICharacteristics,
       "sniHardwarePCICharacteristicsEntry": sniHardwarePCICharacteristicsEntry,
       "sniPCICharacteristicsIndex": sniPCICharacteristicsIndex,
       "sniPCIIndex2": sniPCIIndex2,
       "sniCharacteristicNumber": sniCharacteristicNumber,
       "sniCharacteristicInfo": sniCharacteristicInfo,
       "sniModeNumber": sniModeNumber,
       "sniModeInfo": sniModeInfo,
       "sniHardwarePCIInfo": sniHardwarePCIInfo,
       "sniHardwarePCIInfoEntry": sniHardwarePCIInfoEntry,
       "sniPCIInfoIndex": sniPCIInfoIndex,
       "sniPCIIndex3": sniPCIIndex3,
       "sniDeviceID": sniDeviceID,
       "sniPCIDeviceType": sniPCIDeviceType,
       "sniPCIDeviceName": sniPCIDeviceName,
       "sniRevisionID": sniRevisionID,
       "sniPCIBusNumber": sniPCIBusNumber,
       "sniPCISlotNumber": sniPCISlotNumber,
       "sniPCIVendorID": sniPCIVendorID,
       "sniVendorName": sniVendorName,
       "sniBaseClassID": sniBaseClassID,
       "sniSubClassID": sniSubClassID,
       "sniProgrammingInterfaceID": sniProgrammingInterfaceID,
       "sniBaseClassDescription": sniBaseClassDescription,
       "sniSubClassDescription": sniSubClassDescription,
       "sniSingleMultiFunction": sniSingleMultiFunction,
       "sniDeviceCommand": sniDeviceCommand,
       "sniDeviceStatus": sniDeviceStatus,
       "sniCacheLineSize": sniCacheLineSize,
       "sniLatencyTimer": sniLatencyTimer,
       "sniCompletionCode": sniCompletionCode,
       "sniBuildinSelfTestSupport": sniBuildinSelfTestSupport,
       "sniInterruptLine": sniInterruptLine,
       "sniInterruptPin": sniInterruptPin,
       "sniMinimumGrant": sniMinimumGrant,
       "sniMaximumLatencyTime": sniMaximumLatencyTime,
       "sniSubVendorID": sniSubVendorID,
       "sniSubSystemID": sniSubSystemID,
       "sniCIS": sniCIS,
       "sniExpROMBaseAddressReg": sniExpROMBaseAddressReg,
       "sniExpansionROMBaseAddress": sniExpansionROMBaseAddress,
       "sniDecodeenabled": sniDecodeenabled,
       "sniFunctionnumber": sniFunctionnumber,
       "sniDevicenumber": sniDevicenumber,
       "sniMainboardMemoryModulesEx": sniMainboardMemoryModulesEx,
       "sniMainboardMemoryModulesExEntry": sniMainboardMemoryModulesExEntry,
       "sniMemoryController2": sniMemoryController2,
       "sniMemoryModule2": sniMemoryModule2,
       "sniMemoryModuleSerialnumber": sniMemoryModuleSerialnumber,
       "sniMemoryModuleManufacturer": sniMemoryModuleManufacturer,
       "sniLocationMemoryBank": sniLocationMemoryBank,
       "sniNumberOfLowLevelDevices": sniNumberOfLowLevelDevices,
       "sniSpeedMHz": sniSpeedMHz,
       "sniMemoryTypeEx": sniMemoryTypeEx,
       "sniMemorymoduleFormfactorandType": sniMemorymoduleFormfactorandType,
       "sniUSER": sniUSER,
       "sniUsername": sniUsername,
       "sniPhonenumber": sniPhonenumber,
       "sniPlace": sniPlace,
       "sniDepartment": sniDepartment,
       "sniJobTitle": sniJobTitle,
       "sniContact": sniContact,
       "sniAdditionalUserInformation": sniAdditionalUserInformation,
       "sniServicePartner": sniServicePartner,
       "sniServiceContact": sniServiceContact,
       "sniEndOfContract": sniEndOfContract,
       "sniAdditionalServiceInformation": sniAdditionalServiceInformation,
       "sniGeneralInformation": sniGeneralInformation,
       "sniNetwork": sniNetwork,
       "sniNetworkEntry": sniNetworkEntry,
       "sniNetworkAdapterIndex": sniNetworkAdapterIndex,
       "sniNetworkAdapter": sniNetworkAdapter,
       "sniMACAddress": sniMACAddress,
       "sniComputerName": sniComputerName,
       "sniDHCPServer": sniDHCPServer,
       "sniDNSHostname": sniDNSHostname,
       "sniDNSDomainname": sniDNSDomainname,
       "sniDNSServer1": sniDNSServer1,
       "sniDNSServer2": sniDNSServer2,
       "sniDNSServer3": sniDNSServer3,
       "sniDNSServer4": sniDNSServer4,
       "sniDNSServer5": sniDNSServer5,
       "sniIPAddress1": sniIPAddress1,
       "sniIPAddress2": sniIPAddress2,
       "sniIPAddress3": sniIPAddress3,
       "sniIPAddress4": sniIPAddress4,
       "sniIPAddress5": sniIPAddress5,
       "sniSubnetMask1": sniSubnetMask1,
       "sniSubnetMask2": sniSubnetMask2,
       "sniSubnetMask3": sniSubnetMask3,
       "sniSubnetMask4": sniSubnetMask4,
       "sniSubnetMask5": sniSubnetMask5,
       "sniGateway1": sniGateway1,
       "sniGateway2": sniGateway2,
       "sniGateway3": sniGateway3,
       "sniGateway4": sniGateway4,
       "sniGateway5": sniGateway5}
)
