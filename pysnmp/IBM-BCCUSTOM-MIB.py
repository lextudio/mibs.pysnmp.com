# SNMP MIB module (IBM-BCCUSTOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-BCCUSTOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:24 2024
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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

bcCustom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215)
)
bcCustom.setRevisions(
        ("2013-10-15 17:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_BcCustomMibVersion_ObjectIdentity = ObjectIdentity
bcCustomMibVersion = _BcCustomMibVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 1)
)
if mibBuilder.loadTexts:
    bcCustomMibVersion.setStatus("current")
_MibCustomVersion_ObjectIdentity = ObjectIdentity
mibCustomVersion = _MibCustomVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 1, 1)
)
_MibMajorMinor_Type = Integer32
_MibMajorMinor_Object = MibScalar
mibMajorMinor = _MibMajorMinor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 1, 1, 1),
    _MibMajorMinor_Type()
)
mibMajorMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibMajorMinor.setStatus("current")
_IomGlobal_ObjectIdentity = ObjectIdentity
iomGlobal = _IomGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 1, 2)
)


class _IomCapability_Type(Integer32):
    """Custom type iomCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IomCapability_Type.__name__ = "Integer32"
_IomCapability_Object = MibScalar
iomCapability = _IomCapability_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 1, 2, 1),
    _IomCapability_Type()
)
iomCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iomCapability.setStatus("current")


class _IomMode_Type(Integer32):
    """Custom type iomMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("managedSwitchMode", 1),
          ("passthruEnhanceMode", 3),
          ("passthruNativeMode", 2))
    )


_IomMode_Type.__name__ = "Integer32"
_IomMode_Object = MibScalar
iomMode = _IomMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 1, 2, 2),
    _IomMode_Type()
)
iomMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iomMode.setStatus("current")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2)
)
if mibBuilder.loadTexts:
    ports.setStatus("current")
_PortInformation_ObjectIdentity = ObjectIdentity
portInformation = _PortInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1)
)
_PortInformationTable_Object = MibTable
portInformationTable = _PortInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1)
)
if mibBuilder.loadTexts:
    portInformationTable.setStatus("current")
_PortInformationEntry_Object = MibTableRow
portInformationEntry = _PortInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1)
)
portInformationEntry.setIndexNames(
    (0, "IBM-BCCUSTOM-MIB", "portModuleIndex"),
    (0, "IBM-BCCUSTOM-MIB", "portModuleType"),
)
if mibBuilder.loadTexts:
    portInformationEntry.setStatus("current")


class _PortModuleIndex_Type(Integer32):
    """Custom type portModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortModuleIndex_Type.__name__ = "Integer32"
_PortModuleIndex_Object = MibTableColumn
portModuleIndex = _PortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 1),
    _PortModuleIndex_Type()
)
portModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleIndex.setStatus("current")


class _PortModuleType_Type(Integer32):
    """Custom type portModuleType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("bladePort", 4),
          ("externalDualPort", 3),
          ("externalManagementPort", 2),
          ("externalPort", 1),
          ("interModuleDualPort", 9),
          ("interModuleExternalBridgePort", 10),
          ("interModuleInternalBridgePort", 11),
          ("interModuleManagementPort", 8),
          ("interModulePort", 7),
          ("mmManagementPort", 5),
          ("unUsed", 0),
          ("uplinkPort", 6))
    )


_PortModuleType_Type.__name__ = "Integer32"
_PortModuleType_Object = MibTableColumn
portModuleType = _PortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 2),
    _PortModuleType_Type()
)
portModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleType.setStatus("current")


class _PortModuleLinkState_Type(Integer32):
    """Custom type portModuleLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("initialized", 2),
          ("up", 1))
    )


_PortModuleLinkState_Type.__name__ = "Integer32"
_PortModuleLinkState_Object = MibTableColumn
portModuleLinkState = _PortModuleLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 3),
    _PortModuleLinkState_Type()
)
portModuleLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portModuleLinkState.setStatus("current")


class _PortModuleLabel_Type(OctetString):
    """Custom type portModuleLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortModuleLabel_Type.__name__ = "OctetString"
_PortModuleLabel_Object = MibTableColumn
portModuleLabel = _PortModuleLabel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 4),
    _PortModuleLabel_Type()
)
portModuleLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portModuleLabel.setStatus("current")


class _PortModuleSpeed_Type(Integer32):
    """Custom type portModuleSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10,
              20,
              40,
              60,
              80,
              100,
              140,
              160,
              200,
              400,
              560,
              600,
              800,
              1000,
              1120,
              1680)
        )
    )
    namedValues = NamedValues(
        *(("autoduplex", 0),
          ("eight-Gbpsfullduplex", 80),
          ("eighty-Gbpsfullduplex", 800),
          ("fivtysix-Gbpsfullduplex", 560),
          ("four-Gbpsfullduplex", 40),
          ("fourteen-Gbpsfullduplex", 140),
          ("fourty-Gbpsfullduplex", 400),
          ("hundred-Gbpsfullduplex", 1000),
          ("hundred-Mbpsfullduplex", 1),
          ("hundredandsixtyeight-Gbpsfullduplex", 1680),
          ("hundredandtwelve-Gbpsfullduplex", 1120),
          ("one-Gbpsfullduplex", 10),
          ("six-Gbpsfullduplex", 60),
          ("sixteen-Gbpsfullduplex", 160),
          ("sixty-Gbpsfullduplex", 600),
          ("ten-Gbpsfullduplex", 100),
          ("twenty-Gbpsfullduplex", 200),
          ("two-Gbpsfullduplex", 20))
    )


_PortModuleSpeed_Type.__name__ = "Integer32"
_PortModuleSpeed_Object = MibTableColumn
portModuleSpeed = _PortModuleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 5),
    _PortModuleSpeed_Type()
)
portModuleSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portModuleSpeed.setStatus("current")


class _PortModuleMedia_Type(Integer32):
    """Custom type portModuleMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              32,
              40,
              48,
              255)
        )
    )
    namedValues = NamedValues(
        *(("copper", 0),
          ("opticalInterHaul", 40),
          ("opticalLongHaul", 48),
          ("opticalShortHaul", 32),
          ("other", 255),
          ("serdes", 1))
    )


_PortModuleMedia_Type.__name__ = "Integer32"
_PortModuleMedia_Object = MibTableColumn
portModuleMedia = _PortModuleMedia_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 6),
    _PortModuleMedia_Type()
)
portModuleMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleMedia.setStatus("current")


class _PortModuleProtocol_Type(Integer32):
    """Custom type portModuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              112,
              120)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 16),
          ("fibreChannel", 32),
          ("infiniband", 64),
          ("myrinet", 112),
          ("pciExpress", 80),
          ("scalability", 48),
          ("serial", 120))
    )


_PortModuleProtocol_Type.__name__ = "Integer32"
_PortModuleProtocol_Object = MibTableColumn
portModuleProtocol = _PortModuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 7),
    _PortModuleProtocol_Type()
)
portModuleProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleProtocol.setStatus("current")


class _PortModuleTotal_Type(Integer32):
    """Custom type portModuleTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortModuleTotal_Type.__name__ = "Integer32"
_PortModuleTotal_Object = MibTableColumn
portModuleTotal = _PortModuleTotal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 8),
    _PortModuleTotal_Type()
)
portModuleTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleTotal.setStatus("current")


class _PortModuleSpeedList_Type(OctetString):
    """Custom type portModuleSpeedList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortModuleSpeedList_Type.__name__ = "OctetString"
_PortModuleSpeedList_Object = MibTableColumn
portModuleSpeedList = _PortModuleSpeedList_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 9),
    _PortModuleSpeedList_Type()
)
portModuleSpeedList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleSpeedList.setStatus("current")


class _PortModuleReal_Type(Integer32):
    """Custom type portModuleReal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortModuleReal_Type.__name__ = "Integer32"
_PortModuleReal_Object = MibTableColumn
portModuleReal = _PortModuleReal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 10),
    _PortModuleReal_Type()
)
portModuleReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleReal.setStatus("current")


class _PortModuleRelative_Type(Integer32):
    """Custom type portModuleRelative based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortModuleRelative_Type.__name__ = "Integer32"
_PortModuleRelative_Object = MibTableColumn
portModuleRelative = _PortModuleRelative_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 11),
    _PortModuleRelative_Type()
)
portModuleRelative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleRelative.setStatus("current")


class _PortModuleLaneCount_Type(Integer32):
    """Custom type portModuleLaneCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              12,
              16)
        )
    )
    namedValues = NamedValues(
        *(("eightx", 8),
          ("fourx", 4),
          ("onex", 1),
          ("sixteenx", 16),
          ("twelvex", 12),
          ("twox", 2))
    )


_PortModuleLaneCount_Type.__name__ = "Integer32"
_PortModuleLaneCount_Object = MibTableColumn
portModuleLaneCount = _PortModuleLaneCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 12),
    _PortModuleLaneCount_Type()
)
portModuleLaneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleLaneCount.setStatus("current")


class _PortModuleCableLength_Type(Integer32):
    """Custom type portModuleCableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortModuleCableLength_Type.__name__ = "Integer32"
_PortModuleCableLength_Object = MibTableColumn
portModuleCableLength = _PortModuleCableLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 13),
    _PortModuleCableLength_Type()
)
portModuleCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleCableLength.setStatus("current")


class _PortModuleCableManufacturer_Type(OctetString):
    """Custom type portModuleCableManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortModuleCableManufacturer_Type.__name__ = "OctetString"
_PortModuleCableManufacturer_Object = MibTableColumn
portModuleCableManufacturer = _PortModuleCableManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 14),
    _PortModuleCableManufacturer_Type()
)
portModuleCableManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleCableManufacturer.setStatus("current")


class _PortModuleCableCompatiblity_Type(Integer32):
    """Custom type portModuleCableCompatiblity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 1),
          ("compatibleButNotRecommnded", 2),
          ("incompatible", 0))
    )


_PortModuleCableCompatiblity_Type.__name__ = "Integer32"
_PortModuleCableCompatiblity_Object = MibTableColumn
portModuleCableCompatiblity = _PortModuleCableCompatiblity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 15),
    _PortModuleCableCompatiblity_Type()
)
portModuleCableCompatiblity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleCableCompatiblity.setStatus("current")


class _PortModuleCableType_Type(OctetString):
    """Custom type portModuleCableType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortModuleCableType_Type.__name__ = "OctetString"
_PortModuleCableType_Object = MibTableColumn
portModuleCableType = _PortModuleCableType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 16),
    _PortModuleCableType_Type()
)
portModuleCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleCableType.setStatus("current")


class _PortModuleDataRate_Type(Integer32):
    """Custom type portModuleDataRate based on Integer32"""
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
        *(("ddr", 1),
          ("edr", 3),
          ("fdr", 4),
          ("qdr", 2),
          ("sdr", 0))
    )


_PortModuleDataRate_Type.__name__ = "Integer32"
_PortModuleDataRate_Object = MibTableColumn
portModuleDataRate = _PortModuleDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 17),
    _PortModuleDataRate_Type()
)
portModuleDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleDataRate.setStatus("current")


class _PortModuleLicensedState_Type(Integer32):
    """Custom type portModuleLicensedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licensed", 2),
          ("notApplicable", 0),
          ("notLicensed", 1))
    )


_PortModuleLicensedState_Type.__name__ = "Integer32"
_PortModuleLicensedState_Object = MibTableColumn
portModuleLicensedState = _PortModuleLicensedState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 2, 1, 1, 1, 18),
    _PortModuleLicensedState_Type()
)
portModuleLicensedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleLicensedState.setStatus("current")
_Firmware_ObjectIdentity = ObjectIdentity
firmware = _Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3)
)
if mibBuilder.loadTexts:
    firmware.setStatus("current")
_FirmwareOps_ObjectIdentity = ObjectIdentity
firmwareOps = _FirmwareOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1)
)
_FwInformationTable_Object = MibTable
fwInformationTable = _FwInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fwInformationTable.setStatus("current")
_FwInformationEntry_Object = MibTableRow
fwInformationEntry = _FwInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 1, 1)
)
fwInformationEntry.setIndexNames(
    (0, "IBM-BCCUSTOM-MIB", "fwImageIndex"),
)
if mibBuilder.loadTexts:
    fwInformationEntry.setStatus("current")


class _FwImageIndex_Type(Integer32):
    """Custom type fwImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FwImageIndex_Type.__name__ = "Integer32"
_FwImageIndex_Object = MibTableColumn
fwImageIndex = _FwImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 1, 1, 1),
    _FwImageIndex_Type()
)
fwImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwImageIndex.setStatus("current")


class _FwImageInformation_Type(OctetString):
    """Custom type fwImageInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_FwImageInformation_Type.__name__ = "OctetString"
_FwImageInformation_Object = MibTableColumn
fwImageInformation = _FwImageInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 1, 1, 2),
    _FwImageInformation_Type()
)
fwImageInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwImageInformation.setStatus("current")


class _FwImageFileLocation_Type(Integer32):
    """Custom type fwImageFileLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("externalServerRequired", 1),
          ("mmServer", 0))
    )


_FwImageFileLocation_Type.__name__ = "Integer32"
_FwImageFileLocation_Object = MibTableColumn
fwImageFileLocation = _FwImageFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 1, 1, 3),
    _FwImageFileLocation_Type()
)
fwImageFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwImageFileLocation.setStatus("current")


class _FwImageProtocols_Type(OctetString):
    """Custom type fwImageProtocols based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FwImageProtocols_Type.__name__ = "OctetString"
_FwImageProtocols_Object = MibTableColumn
fwImageProtocols = _FwImageProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 1, 1, 4),
    _FwImageProtocols_Type()
)
fwImageProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwImageProtocols.setStatus("current")


class _FwImageIsUpdateable_Type(Integer32):
    """Custom type fwImageIsUpdateable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notupdateable", 1),
          ("updateable", 0))
    )


_FwImageIsUpdateable_Type.__name__ = "Integer32"
_FwImageIsUpdateable_Object = MibTableColumn
fwImageIsUpdateable = _FwImageIsUpdateable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 1, 1, 5),
    _FwImageIsUpdateable_Type()
)
fwImageIsUpdateable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwImageIsUpdateable.setStatus("current")
_FirmwareCmd_ObjectIdentity = ObjectIdentity
firmwareCmd = _FirmwareCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 2)
)


class _FirmwareImageCnt_Type(Integer32):
    """Custom type firmwareImageCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FirmwareImageCnt_Type.__name__ = "Integer32"
_FirmwareImageCnt_Object = MibScalar
firmwareImageCnt = _FirmwareImageCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 2, 1),
    _FirmwareImageCnt_Type()
)
firmwareImageCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareImageCnt.setStatus("current")


class _FirmwareImageNum_Type(Integer32):
    """Custom type firmwareImageNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FirmwareImageNum_Type.__name__ = "Integer32"
_FirmwareImageNum_Object = MibScalar
firmwareImageNum = _FirmwareImageNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 2, 2),
    _FirmwareImageNum_Type()
)
firmwareImageNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareImageNum.setStatus("current")


class _FirmwareAction_Type(Integer32):
    """Custom type firmwareAction based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("rsvd10", 10),
          ("rsvd2", 2),
          ("rsvd3", 3),
          ("rsvd4", 4),
          ("rsvd5", 5),
          ("rsvd6", 6),
          ("rsvd7", 7),
          ("rsvd8", 8),
          ("rsvd9", 9),
          ("unknown", 0))
    )


_FirmwareAction_Type.__name__ = "Integer32"
_FirmwareAction_Object = MibScalar
firmwareAction = _FirmwareAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 2, 3),
    _FirmwareAction_Type()
)
firmwareAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareAction.setStatus("current")


class _FwUpdateOperationStatus_Type(Integer32):
    """Custom type fwUpdateOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              101,
              201)
        )
    )
    namedValues = NamedValues(
        *(("failure", 201),
          ("noOperation", 0),
          ("success", 101))
    )


_FwUpdateOperationStatus_Type.__name__ = "Integer32"
_FwUpdateOperationStatus_Object = MibScalar
fwUpdateOperationStatus = _FwUpdateOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 2, 4),
    _FwUpdateOperationStatus_Type()
)
fwUpdateOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwUpdateOperationStatus.setStatus("current")


class _FirmwareServer_Type(OctetString):
    """Custom type firmwareServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FirmwareServer_Type.__name__ = "OctetString"
_FirmwareServer_Object = MibScalar
firmwareServer = _FirmwareServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 2, 5),
    _FirmwareServer_Type()
)
firmwareServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareServer.setStatus("current")


class _FwUpdateImageActivation_Type(Integer32):
    """Custom type fwUpdateImageActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FwUpdateImageActivation_Type.__name__ = "Integer32"
_FwUpdateImageActivation_Object = MibScalar
fwUpdateImageActivation = _FwUpdateImageActivation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 2, 6),
    _FwUpdateImageActivation_Type()
)
fwUpdateImageActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwUpdateImageActivation.setStatus("current")


class _FwUpdateImageUri_Type(OctetString):
    """Custom type fwUpdateImageUri based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FwUpdateImageUri_Type.__name__ = "OctetString"
_FwUpdateImageUri_Object = MibScalar
fwUpdateImageUri = _FwUpdateImageUri_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 2, 7),
    _FwUpdateImageUri_Type()
)
fwUpdateImageUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwUpdateImageUri.setStatus("current")


class _FwUpdateImageSftpRsaKey_Type(OctetString):
    """Custom type fwUpdateImageSftpRsaKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_FwUpdateImageSftpRsaKey_Type.__name__ = "OctetString"
_FwUpdateImageSftpRsaKey_Object = MibScalar
fwUpdateImageSftpRsaKey = _FwUpdateImageSftpRsaKey_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 3, 1, 2, 8),
    _FwUpdateImageSftpRsaKey_Type()
)
fwUpdateImageSftpRsaKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwUpdateImageSftpRsaKey.setStatus("deprecated")
_Files_ObjectIdentity = ObjectIdentity
files = _Files_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4)
)
if mibBuilder.loadTexts:
    files.setStatus("current")
_SystemFile_ObjectIdentity = ObjectIdentity
systemFile = _SystemFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 1)
)
_SystemFileInformationTable_Object = MibTable
systemFileInformationTable = _SystemFileInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 1, 1)
)
if mibBuilder.loadTexts:
    systemFileInformationTable.setStatus("current")
_SystemFileInformationEntry_Object = MibTableRow
systemFileInformationEntry = _SystemFileInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 1, 1, 1)
)
systemFileInformationEntry.setIndexNames(
    (0, "IBM-BCCUSTOM-MIB", "systemFileIndex"),
)
if mibBuilder.loadTexts:
    systemFileInformationEntry.setStatus("current")


class _SystemFileIndex_Type(Integer32):
    """Custom type systemFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemFileIndex_Type.__name__ = "Integer32"
_SystemFileIndex_Object = MibTableColumn
systemFileIndex = _SystemFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 1, 1, 1, 1),
    _SystemFileIndex_Type()
)
systemFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileIndex.setStatus("current")


class _SystemFileInformation_Type(OctetString):
    """Custom type systemFileInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemFileInformation_Type.__name__ = "OctetString"
_SystemFileInformation_Object = MibTableColumn
systemFileInformation = _SystemFileInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 1, 1, 1, 2),
    _SystemFileInformation_Type()
)
systemFileInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileInformation.setStatus("current")


class _SystemFileInformationProtocols_Type(OctetString):
    """Custom type systemFileInformationProtocols based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemFileInformationProtocols_Type.__name__ = "OctetString"
_SystemFileInformationProtocols_Object = MibTableColumn
systemFileInformationProtocols = _SystemFileInformationProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 1, 1, 1, 3),
    _SystemFileInformationProtocols_Type()
)
systemFileInformationProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileInformationProtocols.setStatus("current")
_SystemFileCmd_ObjectIdentity = ObjectIdentity
systemFileCmd = _SystemFileCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2)
)


class _SystemFileCmdCnt_Type(Integer32):
    """Custom type systemFileCmdCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemFileCmdCnt_Type.__name__ = "Integer32"
_SystemFileCmdCnt_Object = MibScalar
systemFileCmdCnt = _SystemFileCmdCnt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2, 1),
    _SystemFileCmdCnt_Type()
)
systemFileCmdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileCmdCnt.setStatus("current")


class _SystemFileCmdFilename_Type(OctetString):
    """Custom type systemFileCmdFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemFileCmdFilename_Type.__name__ = "OctetString"
_SystemFileCmdFilename_Object = MibScalar
systemFileCmdFilename = _SystemFileCmdFilename_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2, 2),
    _SystemFileCmdFilename_Type()
)
systemFileCmdFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFileCmdFilename.setStatus("deprecated")


class _SystemFileCmdMaxSize_Type(Integer32):
    """Custom type systemFileCmdMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SystemFileCmdMaxSize_Type.__name__ = "Integer32"
_SystemFileCmdMaxSize_Object = MibScalar
systemFileCmdMaxSize = _SystemFileCmdMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2, 3),
    _SystemFileCmdMaxSize_Type()
)
systemFileCmdMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFileCmdMaxSize.setStatus("current")


class _SystemFileCmdUri_Type(OctetString):
    """Custom type systemFileCmdUri based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SystemFileCmdUri_Type.__name__ = "OctetString"
_SystemFileCmdUri_Object = MibScalar
systemFileCmdUri = _SystemFileCmdUri_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2, 4),
    _SystemFileCmdUri_Type()
)
systemFileCmdUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFileCmdUri.setStatus("current")


class _SystemFileCmdSftpRsaKey_Type(OctetString):
    """Custom type systemFileCmdSftpRsaKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SystemFileCmdSftpRsaKey_Type.__name__ = "OctetString"
_SystemFileCmdSftpRsaKey_Object = MibScalar
systemFileCmdSftpRsaKey = _SystemFileCmdSftpRsaKey_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2, 5),
    _SystemFileCmdSftpRsaKey_Type()
)
systemFileCmdSftpRsaKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFileCmdSftpRsaKey.setStatus("deprecated")


class _SystemFileCmdExecuteOp_Type(Integer32):
    """Custom type systemFileCmdExecuteOp based on Integer32"""
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
        *(("cfgget", 2),
          ("cfgput", 3),
          ("ssget", 1),
          ("unknown", 0))
    )


_SystemFileCmdExecuteOp_Type.__name__ = "Integer32"
_SystemFileCmdExecuteOp_Object = MibScalar
systemFileCmdExecuteOp = _SystemFileCmdExecuteOp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2, 6),
    _SystemFileCmdExecuteOp_Type()
)
systemFileCmdExecuteOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFileCmdExecuteOp.setStatus("current")


class _SystemFileOperationStatus_Type(Integer32):
    """Custom type systemFileOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50,
              51,
              101,
              201)
        )
    )
    namedValues = NamedValues(
        *(("failed", 201),
          ("generationcompleted", 50),
          ("initiated", 1),
          ("noOperation", 0),
          ("success", 101),
          ("transfer", 51))
    )


_SystemFileOperationStatus_Type.__name__ = "Integer32"
_SystemFileOperationStatus_Object = MibScalar
systemFileOperationStatus = _SystemFileOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2, 7),
    _SystemFileOperationStatus_Type()
)
systemFileOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileOperationStatus.setStatus("current")


class _SystemFileOpStatusString_Type(OctetString):
    """Custom type systemFileOpStatusString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemFileOpStatusString_Type.__name__ = "OctetString"
_SystemFileOpStatusString_Object = MibScalar
systemFileOpStatusString = _SystemFileOpStatusString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2, 8),
    _SystemFileOpStatusString_Type()
)
systemFileOpStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileOpStatusString.setStatus("current")


class _SystemFileActivation_Type(Integer32):
    """Custom type systemFileActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("noOp", 0))
    )


_SystemFileActivation_Type.__name__ = "Integer32"
_SystemFileActivation_Object = MibScalar
systemFileActivation = _SystemFileActivation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 4, 2, 9),
    _SystemFileActivation_Type()
)
systemFileActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFileActivation.setStatus("current")
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 5)
)
if mibBuilder.loadTexts:
    protocols.setStatus("current")
_NtpConfig_ObjectIdentity = ObjectIdentity
ntpConfig = _NtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 5, 1)
)


class _NtpEnable_Type(Integer32):
    """Custom type ntpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NtpEnable_Type.__name__ = "Integer32"
_NtpEnable_Object = MibScalar
ntpEnable = _NtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 5, 1, 1),
    _NtpEnable_Type()
)
ntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpEnable.setStatus("current")


class _NtpSrvIpv6Address_Type(OctetString):
    """Custom type ntpSrvIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtpSrvIpv6Address_Type.__name__ = "OctetString"
_NtpSrvIpv6Address_Object = MibScalar
ntpSrvIpv6Address = _NtpSrvIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 5, 1, 2),
    _NtpSrvIpv6Address_Type()
)
ntpSrvIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpSrvIpv6Address.setStatus("current")
_NtpSrvIpv4Address_Type = IpAddress
_NtpSrvIpv4Address_Object = MibScalar
ntpSrvIpv4Address = _NtpSrvIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 5, 1, 3),
    _NtpSrvIpv4Address_Type()
)
ntpSrvIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpSrvIpv4Address.setStatus("current")


class _NtpUpdateFrequency_Type(Integer32):
    """Custom type ntpUpdateFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtpUpdateFrequency_Type.__name__ = "Integer32"
_NtpUpdateFrequency_Object = MibScalar
ntpUpdateFrequency = _NtpUpdateFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 5, 1, 4),
    _NtpUpdateFrequency_Type()
)
ntpUpdateFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpUpdateFrequency.setStatus("current")


class _Ntpv3AuthConfig_Type(OctetString):
    """Custom type ntpv3AuthConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Ntpv3AuthConfig_Type.__name__ = "OctetString"
_Ntpv3AuthConfig_Object = MibScalar
ntpv3AuthConfig = _Ntpv3AuthConfig_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 5, 1, 5),
    _Ntpv3AuthConfig_Type()
)
ntpv3AuthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpv3AuthConfig.setStatus("current")


class _Ntpv3AuthEnable_Type(Integer32):
    """Custom type ntpv3AuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Ntpv3AuthEnable_Type.__name__ = "Integer32"
_Ntpv3AuthEnable_Object = MibScalar
ntpv3AuthEnable = _Ntpv3AuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 5, 1, 6),
    _Ntpv3AuthEnable_Type()
)
ntpv3AuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpv3AuthEnable.setStatus("current")
_Snmpuser_ObjectIdentity = ObjectIdentity
snmpuser = _Snmpuser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6)
)
if mibBuilder.loadTexts:
    snmpuser.setStatus("current")
_IomSnmpv3Cfg_ObjectIdentity = ObjectIdentity
iomSnmpv3Cfg = _IomSnmpv3Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1)
)


class _IomSnmpv3UserName_Type(OctetString):
    """Custom type iomSnmpv3UserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IomSnmpv3UserName_Type.__name__ = "OctetString"
_IomSnmpv3UserName_Object = MibScalar
iomSnmpv3UserName = _IomSnmpv3UserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 1),
    _IomSnmpv3UserName_Type()
)
iomSnmpv3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3UserName.setStatus("current")


class _IomSnmpv3UserAuthProtocol_Type(Integer32):
    """Custom type iomSnmpv3UserAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sha", 1)
    )


_IomSnmpv3UserAuthProtocol_Type.__name__ = "Integer32"
_IomSnmpv3UserAuthProtocol_Object = MibScalar
iomSnmpv3UserAuthProtocol = _IomSnmpv3UserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 2),
    _IomSnmpv3UserAuthProtocol_Type()
)
iomSnmpv3UserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3UserAuthProtocol.setStatus("current")


class _IomSnmpv3UserAuthPassword_Type(OctetString):
    """Custom type iomSnmpv3UserAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IomSnmpv3UserAuthPassword_Type.__name__ = "OctetString"
_IomSnmpv3UserAuthPassword_Object = MibScalar
iomSnmpv3UserAuthPassword = _IomSnmpv3UserAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 3),
    _IomSnmpv3UserAuthPassword_Type()
)
iomSnmpv3UserAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3UserAuthPassword.setStatus("current")


class _IomSnmpv3UserPrivacyProtocol_Type(Integer32):
    """Custom type iomSnmpv3UserPrivacyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("aes", 1)
    )


_IomSnmpv3UserPrivacyProtocol_Type.__name__ = "Integer32"
_IomSnmpv3UserPrivacyProtocol_Object = MibScalar
iomSnmpv3UserPrivacyProtocol = _IomSnmpv3UserPrivacyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 4),
    _IomSnmpv3UserPrivacyProtocol_Type()
)
iomSnmpv3UserPrivacyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3UserPrivacyProtocol.setStatus("current")


class _IomSnmpv3UserPrivacyPassword_Type(OctetString):
    """Custom type iomSnmpv3UserPrivacyPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IomSnmpv3UserPrivacyPassword_Type.__name__ = "OctetString"
_IomSnmpv3UserPrivacyPassword_Object = MibScalar
iomSnmpv3UserPrivacyPassword = _IomSnmpv3UserPrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 5),
    _IomSnmpv3UserPrivacyPassword_Type()
)
iomSnmpv3UserPrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3UserPrivacyPassword.setStatus("current")


class _IomSnmpv3UserAccessType_Type(Integer32):
    """Custom type iomSnmpv3UserAccessType based on Integer32"""
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
        *(("get-set-traps", 2),
          ("get-traps", 1),
          ("no-access", 0),
          ("traps-only", 3))
    )


_IomSnmpv3UserAccessType_Type.__name__ = "Integer32"
_IomSnmpv3UserAccessType_Object = MibScalar
iomSnmpv3UserAccessType = _IomSnmpv3UserAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 6),
    _IomSnmpv3UserAccessType_Type()
)
iomSnmpv3UserAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3UserAccessType.setStatus("current")


class _IomSnmpv3UserIPv6TrapAddress_Type(OctetString):
    """Custom type iomSnmpv3UserIPv6TrapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IomSnmpv3UserIPv6TrapAddress_Type.__name__ = "OctetString"
_IomSnmpv3UserIPv6TrapAddress_Object = MibScalar
iomSnmpv3UserIPv6TrapAddress = _IomSnmpv3UserIPv6TrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 7),
    _IomSnmpv3UserIPv6TrapAddress_Type()
)
iomSnmpv3UserIPv6TrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3UserIPv6TrapAddress.setStatus("current")
_IomSnmpv3UserIPv4TrapAddress_Type = IpAddress
_IomSnmpv3UserIPv4TrapAddress_Object = MibScalar
iomSnmpv3UserIPv4TrapAddress = _IomSnmpv3UserIPv4TrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 8),
    _IomSnmpv3UserIPv4TrapAddress_Type()
)
iomSnmpv3UserIPv4TrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3UserIPv4TrapAddress.setStatus("current")


class _IomSnmpv3UserState_Type(Integer32):
    """Custom type iomSnmpv3UserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IomSnmpv3UserState_Type.__name__ = "Integer32"
_IomSnmpv3UserState_Object = MibScalar
iomSnmpv3UserState = _IomSnmpv3UserState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 9),
    _IomSnmpv3UserState_Type()
)
iomSnmpv3UserState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3UserState.setStatus("current")


class _IomSnmpv3UserStateStatusString_Type(OctetString):
    """Custom type iomSnmpv3UserStateStatusString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IomSnmpv3UserStateStatusString_Type.__name__ = "OctetString"
_IomSnmpv3UserStateStatusString_Object = MibScalar
iomSnmpv3UserStateStatusString = _IomSnmpv3UserStateStatusString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 10),
    _IomSnmpv3UserStateStatusString_Type()
)
iomSnmpv3UserStateStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iomSnmpv3UserStateStatusString.setStatus("current")


class _IomSnmpv3TestTrap_Type(Integer32):
    """Custom type iomSnmpv3TestTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("traptest", 1)
    )


_IomSnmpv3TestTrap_Type.__name__ = "Integer32"
_IomSnmpv3TestTrap_Object = MibScalar
iomSnmpv3TestTrap = _IomSnmpv3TestTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 11),
    _IomSnmpv3TestTrap_Type()
)
iomSnmpv3TestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3TestTrap.setStatus("current")


class _IomSnmpv3tResetUser_Type(Integer32):
    """Custom type iomSnmpv3tResetUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_IomSnmpv3tResetUser_Type.__name__ = "Integer32"
_IomSnmpv3tResetUser_Object = MibScalar
iomSnmpv3tResetUser = _IomSnmpv3tResetUser_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 6, 1, 12),
    _IomSnmpv3tResetUser_Type()
)
iomSnmpv3tResetUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iomSnmpv3tResetUser.setStatus("current")
_License_ObjectIdentity = ObjectIdentity
license = _License_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 7)
)
if mibBuilder.loadTexts:
    license.setStatus("current")
_LicenseKeyInformationTable_Object = MibTable
licenseKeyInformationTable = _LicenseKeyInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 7, 1)
)
if mibBuilder.loadTexts:
    licenseKeyInformationTable.setStatus("current")
_LicenseKeyInformationEntry_Object = MibTableRow
licenseKeyInformationEntry = _LicenseKeyInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 7, 1, 1)
)
licenseKeyInformationEntry.setIndexNames(
    (0, "IBM-BCCUSTOM-MIB", "licenseKeyIndex"),
)
if mibBuilder.loadTexts:
    licenseKeyInformationEntry.setStatus("current")


class _LicenseKeyIndex_Type(Integer32):
    """Custom type licenseKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LicenseKeyIndex_Type.__name__ = "Integer32"
_LicenseKeyIndex_Object = MibTableColumn
licenseKeyIndex = _LicenseKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 7, 1, 1, 1),
    _LicenseKeyIndex_Type()
)
licenseKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyIndex.setStatus("current")


class _LicenseKeyDescStringInformation_Type(OctetString):
    """Custom type licenseKeyDescStringInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_LicenseKeyDescStringInformation_Type.__name__ = "OctetString"
_LicenseKeyDescStringInformation_Object = MibTableColumn
licenseKeyDescStringInformation = _LicenseKeyDescStringInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 7, 1, 1, 2),
    _LicenseKeyDescStringInformation_Type()
)
licenseKeyDescStringInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyDescStringInformation.setStatus("current")


class _LicenseKeyCurrentState_Type(Integer32):
    """Custom type licenseKeyCurrentState based on Integer32"""
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
        *(("expired", 3),
          ("notValid", 2),
          ("unknown", 0),
          ("usageExceeded", 4),
          ("valid", 1))
    )


_LicenseKeyCurrentState_Type.__name__ = "Integer32"
_LicenseKeyCurrentState_Object = MibTableColumn
licenseKeyCurrentState = _LicenseKeyCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 215, 7, 1, 1, 3),
    _LicenseKeyCurrentState_Type()
)
licenseKeyCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyCurrentState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-BCCUSTOM-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "bcCustom": bcCustom,
       "bcCustomMibVersion": bcCustomMibVersion,
       "mibCustomVersion": mibCustomVersion,
       "mibMajorMinor": mibMajorMinor,
       "iomGlobal": iomGlobal,
       "iomCapability": iomCapability,
       "iomMode": iomMode,
       "ports": ports,
       "portInformation": portInformation,
       "portInformationTable": portInformationTable,
       "portInformationEntry": portInformationEntry,
       "portModuleIndex": portModuleIndex,
       "portModuleType": portModuleType,
       "portModuleLinkState": portModuleLinkState,
       "portModuleLabel": portModuleLabel,
       "portModuleSpeed": portModuleSpeed,
       "portModuleMedia": portModuleMedia,
       "portModuleProtocol": portModuleProtocol,
       "portModuleTotal": portModuleTotal,
       "portModuleSpeedList": portModuleSpeedList,
       "portModuleReal": portModuleReal,
       "portModuleRelative": portModuleRelative,
       "portModuleLaneCount": portModuleLaneCount,
       "portModuleCableLength": portModuleCableLength,
       "portModuleCableManufacturer": portModuleCableManufacturer,
       "portModuleCableCompatiblity": portModuleCableCompatiblity,
       "portModuleCableType": portModuleCableType,
       "portModuleDataRate": portModuleDataRate,
       "portModuleLicensedState": portModuleLicensedState,
       "firmware": firmware,
       "firmwareOps": firmwareOps,
       "fwInformationTable": fwInformationTable,
       "fwInformationEntry": fwInformationEntry,
       "fwImageIndex": fwImageIndex,
       "fwImageInformation": fwImageInformation,
       "fwImageFileLocation": fwImageFileLocation,
       "fwImageProtocols": fwImageProtocols,
       "fwImageIsUpdateable": fwImageIsUpdateable,
       "firmwareCmd": firmwareCmd,
       "firmwareImageCnt": firmwareImageCnt,
       "firmwareImageNum": firmwareImageNum,
       "firmwareAction": firmwareAction,
       "fwUpdateOperationStatus": fwUpdateOperationStatus,
       "firmwareServer": firmwareServer,
       "fwUpdateImageActivation": fwUpdateImageActivation,
       "fwUpdateImageUri": fwUpdateImageUri,
       "fwUpdateImageSftpRsaKey": fwUpdateImageSftpRsaKey,
       "files": files,
       "systemFile": systemFile,
       "systemFileInformationTable": systemFileInformationTable,
       "systemFileInformationEntry": systemFileInformationEntry,
       "systemFileIndex": systemFileIndex,
       "systemFileInformation": systemFileInformation,
       "systemFileInformationProtocols": systemFileInformationProtocols,
       "systemFileCmd": systemFileCmd,
       "systemFileCmdCnt": systemFileCmdCnt,
       "systemFileCmdFilename": systemFileCmdFilename,
       "systemFileCmdMaxSize": systemFileCmdMaxSize,
       "systemFileCmdUri": systemFileCmdUri,
       "systemFileCmdSftpRsaKey": systemFileCmdSftpRsaKey,
       "systemFileCmdExecuteOp": systemFileCmdExecuteOp,
       "systemFileOperationStatus": systemFileOperationStatus,
       "systemFileOpStatusString": systemFileOpStatusString,
       "systemFileActivation": systemFileActivation,
       "protocols": protocols,
       "ntpConfig": ntpConfig,
       "ntpEnable": ntpEnable,
       "ntpSrvIpv6Address": ntpSrvIpv6Address,
       "ntpSrvIpv4Address": ntpSrvIpv4Address,
       "ntpUpdateFrequency": ntpUpdateFrequency,
       "ntpv3AuthConfig": ntpv3AuthConfig,
       "ntpv3AuthEnable": ntpv3AuthEnable,
       "snmpuser": snmpuser,
       "iomSnmpv3Cfg": iomSnmpv3Cfg,
       "iomSnmpv3UserName": iomSnmpv3UserName,
       "iomSnmpv3UserAuthProtocol": iomSnmpv3UserAuthProtocol,
       "iomSnmpv3UserAuthPassword": iomSnmpv3UserAuthPassword,
       "iomSnmpv3UserPrivacyProtocol": iomSnmpv3UserPrivacyProtocol,
       "iomSnmpv3UserPrivacyPassword": iomSnmpv3UserPrivacyPassword,
       "iomSnmpv3UserAccessType": iomSnmpv3UserAccessType,
       "iomSnmpv3UserIPv6TrapAddress": iomSnmpv3UserIPv6TrapAddress,
       "iomSnmpv3UserIPv4TrapAddress": iomSnmpv3UserIPv4TrapAddress,
       "iomSnmpv3UserState": iomSnmpv3UserState,
       "iomSnmpv3UserStateStatusString": iomSnmpv3UserStateStatusString,
       "iomSnmpv3TestTrap": iomSnmpv3TestTrap,
       "iomSnmpv3tResetUser": iomSnmpv3tResetUser,
       "license": license,
       "licenseKeyInformationTable": licenseKeyInformationTable,
       "licenseKeyInformationEntry": licenseKeyInformationEntry,
       "licenseKeyIndex": licenseKeyIndex,
       "licenseKeyDescStringInformation": licenseKeyDescStringInformation,
       "licenseKeyCurrentState": licenseKeyCurrentState}
)
