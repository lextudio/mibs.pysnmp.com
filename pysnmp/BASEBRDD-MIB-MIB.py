# SNMP MIB module (BASEBRDD-MIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BASEBRDD-MIB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:38 2024
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

(DmiDate,
 DmiInteger64,
 dmiCompId,
 dmiEventAssociatedGroup,
 dmiEventDateTime,
 dmiEventSeverity,
 dmiEventStateKey,
 dmiEventSubSystem,
 dmiEventSystem) = mibBuilder.importSymbols(
    "DMTF-DMI-MIB",
    "DmiDate",
    "DmiInteger64",
    "dmiCompId",
    "dmiEventAssociatedGroup",
    "dmiEventDateTime",
    "dmiEventSeverity",
    "dmiEventStateKey",
    "dmiEventSubSystem",
    "dmiEventSystem")

(InternationalDisplayString,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString")

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
    "NotificationType",
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



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiCounter64(Counter64):
    """Custom type DmiCounter64 based on Counter64"""




class DmiGauge(Gauge32):
    """Custom type DmiGauge based on Gauge32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiCompId(Integer32):
    """Custom type DmiCompId based on Integer32"""




class DmiGroupId(Integer32):
    """Custom type DmiGroupId based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dmtf_ObjectIdentity = ObjectIdentity
dmtf = _Dmtf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412)
)
_DmtfStdMifs_ObjectIdentity = ObjectIdentity
dmtfStdMifs = _DmtfStdMifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2)
)
_DmtfServiceLayerMIF_ObjectIdentity = ObjectIdentity
dmtfServiceLayerMIF = _DmtfServiceLayerMIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2, 1)
)
_DMTFComponentIDTable_Object = MibTable
dMTFComponentIDTable = _DMTFComponentIDTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dMTFComponentIDTable.setStatus("mandatory")
_DMTFComponentIDEntry_Object = MibTableRow
dMTFComponentIDEntry = _DMTFComponentIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1)
)
dMTFComponentIDEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dMTFComponentIDEntry.setStatus("mandatory")
_ManufacturerAtt1_Type = DmiDisplaystring
_ManufacturerAtt1_Object = MibTableColumn
manufacturerAtt1 = _ManufacturerAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 1),
    _ManufacturerAtt1_Type()
)
manufacturerAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturerAtt1.setStatus("mandatory")
_ProductAtt2_Type = DmiDisplaystring
_ProductAtt2_Object = MibTableColumn
productAtt2 = _ProductAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 2),
    _ProductAtt2_Type()
)
productAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productAtt2.setStatus("mandatory")
_VersionAtt3_Type = DmiDisplaystring
_VersionAtt3_Object = MibTableColumn
versionAtt3 = _VersionAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 3),
    _VersionAtt3_Type()
)
versionAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionAtt3.setStatus("mandatory")
_SerialNumberAtt4_Type = DmiDisplaystring
_SerialNumberAtt4_Object = MibTableColumn
serialNumberAtt4 = _SerialNumberAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 4),
    _SerialNumberAtt4_Type()
)
serialNumberAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumberAtt4.setStatus("mandatory")
_InstallationAtt5_Type = DmiDate
_InstallationAtt5_Object = MibTableColumn
installationAtt5 = _InstallationAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 5),
    _InstallationAtt5_Type()
)
installationAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installationAtt5.setStatus("mandatory")


class _VerifyAtt6_Type(Integer32):
    """Custom type verifyAtt6 based on Integer32"""
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
        *(("anErrorOccurredCheckStatusCode", 0),
          ("reserved", 3),
          ("thisComponentDoesNotExist", 1),
          ("thisComponentExistsAndIsFunctioningCorrectly", 7),
          ("thisComponentExistsAndIsNotFunctioningCorrectly", 6),
          ("thisComponentExistsButTheFunctionalityIsUnknown", 5),
          ("thisComponentExistsButTheFunctionalityIsUntested", 4),
          ("verificationIsNotSupported", 2))
    )


_VerifyAtt6_Type.__name__ = "Integer32"
_VerifyAtt6_Object = MibTableColumn
verifyAtt6 = _VerifyAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 6),
    _VerifyAtt6_Type()
)
verifyAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verifyAtt6.setStatus("mandatory")
_DmtfSystemsMIF_ObjectIdentity = ObjectIdentity
dmtfSystemsMIF = _DmtfSystemsMIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2, 4)
)
_DMTFGeneralInformationTable_Object = MibTable
dMTFGeneralInformationTable = _DMTFGeneralInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dMTFGeneralInformationTable.setStatus("mandatory")
_DMTFGeneralInformationEntry_Object = MibTableRow
dMTFGeneralInformationEntry = _DMTFGeneralInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 1, 1)
)
dMTFGeneralInformationEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dMTFGeneralInformationEntry.setStatus("mandatory")
_SystemNameAtt1_Type = DmiDisplaystring
_SystemNameAtt1_Object = MibTableColumn
systemNameAtt1 = _SystemNameAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 1, 1, 1),
    _SystemNameAtt1_Type()
)
systemNameAtt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNameAtt1.setStatus("mandatory")
_SystemLocationAtt2_Type = DmiDisplaystring
_SystemLocationAtt2_Object = MibTableColumn
systemLocationAtt2 = _SystemLocationAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 1, 1, 2),
    _SystemLocationAtt2_Type()
)
systemLocationAtt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocationAtt2.setStatus("mandatory")
_SystemPrimaryUserNameAtt3_Type = DmiDisplaystring
_SystemPrimaryUserNameAtt3_Object = MibTableColumn
systemPrimaryUserNameAtt3 = _SystemPrimaryUserNameAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 1, 1, 3),
    _SystemPrimaryUserNameAtt3_Type()
)
systemPrimaryUserNameAtt3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPrimaryUserNameAtt3.setStatus("mandatory")
_SystemPrimaryUserPhoneAtt4_Type = DmiDisplaystring
_SystemPrimaryUserPhoneAtt4_Object = MibTableColumn
systemPrimaryUserPhoneAtt4 = _SystemPrimaryUserPhoneAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 1, 1, 4),
    _SystemPrimaryUserPhoneAtt4_Type()
)
systemPrimaryUserPhoneAtt4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPrimaryUserPhoneAtt4.setStatus("mandatory")
_SystemBootupTimeAtt5_Type = DmiDate
_SystemBootupTimeAtt5_Object = MibTableColumn
systemBootupTimeAtt5 = _SystemBootupTimeAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 1, 1, 5),
    _SystemBootupTimeAtt5_Type()
)
systemBootupTimeAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBootupTimeAtt5.setStatus("mandatory")
_SystemDateTimeAtt6_Type = DmiDate
_SystemDateTimeAtt6_Object = MibTableColumn
systemDateTimeAtt6 = _SystemDateTimeAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 1, 1, 6),
    _SystemDateTimeAtt6_Type()
)
systemDateTimeAtt6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDateTimeAtt6.setStatus("mandatory")
_DMTFOperatingSystemTable_Object = MibTable
dMTFOperatingSystemTable = _DMTFOperatingSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dMTFOperatingSystemTable.setStatus("mandatory")
_DMTFOperatingSystemEntry_Object = MibTableRow
dMTFOperatingSystemEntry = _DMTFOperatingSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1)
)
dMTFOperatingSystemEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "operatingSystemIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFOperatingSystemEntry.setStatus("mandatory")


class _DMTFOperatingSystemState_Type(Integer32):
    """Custom type dMTFOperatingSystemState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFOperatingSystemState_Type.__name__ = "Integer32"
_DMTFOperatingSystemState_Object = MibTableColumn
dMTFOperatingSystemState = _DMTFOperatingSystemState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1, 0),
    _DMTFOperatingSystemState_Type()
)
dMTFOperatingSystemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFOperatingSystemState.setStatus("mandatory")
_OperatingSystemIndexAtt1_Type = DmiInteger
_OperatingSystemIndexAtt1_Object = MibTableColumn
operatingSystemIndexAtt1 = _OperatingSystemIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1, 1),
    _OperatingSystemIndexAtt1_Type()
)
operatingSystemIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemIndexAtt1.setStatus("mandatory")
_OperatingSystemNameAtt2_Type = DmiDisplaystring
_OperatingSystemNameAtt2_Object = MibTableColumn
operatingSystemNameAtt2 = _OperatingSystemNameAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1, 2),
    _OperatingSystemNameAtt2_Type()
)
operatingSystemNameAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemNameAtt2.setStatus("mandatory")
_OperatingSystemVersionAtt3_Type = DmiDisplaystring
_OperatingSystemVersionAtt3_Object = MibTableColumn
operatingSystemVersionAtt3 = _OperatingSystemVersionAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1, 3),
    _OperatingSystemVersionAtt3_Type()
)
operatingSystemVersionAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemVersionAtt3.setStatus("mandatory")


class _PrimaryOperatingSystemAtt4_Type(Integer32):
    """Custom type primaryOperatingSystemAtt4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PrimaryOperatingSystemAtt4_Type.__name__ = "Integer32"
_PrimaryOperatingSystemAtt4_Object = MibTableColumn
primaryOperatingSystemAtt4 = _PrimaryOperatingSystemAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1, 4),
    _PrimaryOperatingSystemAtt4_Type()
)
primaryOperatingSystemAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryOperatingSystemAtt4.setStatus("mandatory")


class _OperatingSystemBootDeviceStorageTypeAtt5_Type(Integer32):
    """Custom type operatingSystemBootDeviceStorageTypeAtt5 based on Integer32"""
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
        *(("bernoulli", 10),
          ("compactDisk", 8),
          ("flashDisk", 9),
          ("floppyDisk", 4),
          ("hardDisk", 3),
          ("opticalFloppyDisk", 11),
          ("opticalROM", 5),
          ("opticalRW", 7),
          ("opticalWORM", 6),
          ("other", 1),
          ("unknown", 2))
    )


_OperatingSystemBootDeviceStorageTypeAtt5_Type.__name__ = "Integer32"
_OperatingSystemBootDeviceStorageTypeAtt5_Object = MibTableColumn
operatingSystemBootDeviceStorageTypeAtt5 = _OperatingSystemBootDeviceStorageTypeAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1, 5),
    _OperatingSystemBootDeviceStorageTypeAtt5_Type()
)
operatingSystemBootDeviceStorageTypeAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemBootDeviceStorageTypeAtt5.setStatus("mandatory")
_OperatingSystemBootDeviceIndexAtt6_Type = DmiInteger
_OperatingSystemBootDeviceIndexAtt6_Object = MibTableColumn
operatingSystemBootDeviceIndexAtt6 = _OperatingSystemBootDeviceIndexAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1, 6),
    _OperatingSystemBootDeviceIndexAtt6_Type()
)
operatingSystemBootDeviceIndexAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemBootDeviceIndexAtt6.setStatus("mandatory")
_OperatingSystemBootPartitionIndexAtt7_Type = DmiInteger
_OperatingSystemBootPartitionIndexAtt7_Object = MibTableColumn
operatingSystemBootPartitionIndexAtt7 = _OperatingSystemBootPartitionIndexAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1, 7),
    _OperatingSystemBootPartitionIndexAtt7_Type()
)
operatingSystemBootPartitionIndexAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemBootPartitionIndexAtt7.setStatus("mandatory")
_OperatingSystemDescriptionAtt8_Type = DmiDisplaystring
_OperatingSystemDescriptionAtt8_Object = MibTableColumn
operatingSystemDescriptionAtt8 = _OperatingSystemDescriptionAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 2, 1, 8),
    _OperatingSystemDescriptionAtt8_Type()
)
operatingSystemDescriptionAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemDescriptionAtt8.setStatus("mandatory")
_DMTFSystemBIOSTable_Object = MibTable
dMTFSystemBIOSTable = _DMTFSystemBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3)
)
if mibBuilder.loadTexts:
    dMTFSystemBIOSTable.setStatus("mandatory")
_DMTFSystemBIOSEntry_Object = MibTableRow
dMTFSystemBIOSEntry = _DMTFSystemBIOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1)
)
dMTFSystemBIOSEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "bIOSIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSystemBIOSEntry.setStatus("mandatory")


class _DMTFSystemBIOSState_Type(Integer32):
    """Custom type dMTFSystemBIOSState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSystemBIOSState_Type.__name__ = "Integer32"
_DMTFSystemBIOSState_Object = MibTableColumn
dMTFSystemBIOSState = _DMTFSystemBIOSState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 0),
    _DMTFSystemBIOSState_Type()
)
dMTFSystemBIOSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSystemBIOSState.setStatus("mandatory")
_BIOSIndexAtt1_Type = DmiInteger
_BIOSIndexAtt1_Object = MibTableColumn
bIOSIndexAtt1 = _BIOSIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 1),
    _BIOSIndexAtt1_Type()
)
bIOSIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIOSIndexAtt1.setStatus("mandatory")
_BIOSManufacturerAtt2_Type = DmiDisplaystring
_BIOSManufacturerAtt2_Object = MibTableColumn
bIOSManufacturerAtt2 = _BIOSManufacturerAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 2),
    _BIOSManufacturerAtt2_Type()
)
bIOSManufacturerAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIOSManufacturerAtt2.setStatus("mandatory")
_BIOSVersionAtt3_Type = DmiDisplaystring
_BIOSVersionAtt3_Object = MibTableColumn
bIOSVersionAtt3 = _BIOSVersionAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 3),
    _BIOSVersionAtt3_Type()
)
bIOSVersionAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIOSVersionAtt3.setStatus("mandatory")
_BIOSROMSizeAtt4_Type = DmiInteger
_BIOSROMSizeAtt4_Object = MibTableColumn
bIOSROMSizeAtt4 = _BIOSROMSizeAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 4),
    _BIOSROMSizeAtt4_Type()
)
bIOSROMSizeAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIOSROMSizeAtt4.setStatus("mandatory")
_BIOSStartingAddressAtt5_Type = DmiInteger64
_BIOSStartingAddressAtt5_Object = MibTableColumn
bIOSStartingAddressAtt5 = _BIOSStartingAddressAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 5),
    _BIOSStartingAddressAtt5_Type()
)
bIOSStartingAddressAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIOSStartingAddressAtt5.setStatus("mandatory")
_BIOSEndingAddressAtt6_Type = DmiInteger64
_BIOSEndingAddressAtt6_Object = MibTableColumn
bIOSEndingAddressAtt6 = _BIOSEndingAddressAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 6),
    _BIOSEndingAddressAtt6_Type()
)
bIOSEndingAddressAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIOSEndingAddressAtt6.setStatus("mandatory")
_BIOSLoaderVersionAtt7_Type = DmiDisplaystring
_BIOSLoaderVersionAtt7_Object = MibTableColumn
bIOSLoaderVersionAtt7 = _BIOSLoaderVersionAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 7),
    _BIOSLoaderVersionAtt7_Type()
)
bIOSLoaderVersionAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIOSLoaderVersionAtt7.setStatus("mandatory")
_BIOSReleaseDateAtt8_Type = DmiDate
_BIOSReleaseDateAtt8_Object = MibTableColumn
bIOSReleaseDateAtt8 = _BIOSReleaseDateAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 8),
    _BIOSReleaseDateAtt8_Type()
)
bIOSReleaseDateAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIOSReleaseDateAtt8.setStatus("mandatory")


class _PrimaryBIOSAtt9_Type(Integer32):
    """Custom type primaryBIOSAtt9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PrimaryBIOSAtt9_Type.__name__ = "Integer32"
_PrimaryBIOSAtt9_Object = MibTableColumn
primaryBIOSAtt9 = _PrimaryBIOSAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 3, 1, 9),
    _PrimaryBIOSAtt9_Type()
)
primaryBIOSAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryBIOSAtt9.setStatus("mandatory")
_DMTFProcessorTable_Object = MibTable
dMTFProcessorTable = _DMTFProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5)
)
if mibBuilder.loadTexts:
    dMTFProcessorTable.setStatus("mandatory")
_DMTFProcessorEntry_Object = MibTableRow
dMTFProcessorEntry = _DMTFProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1)
)
dMTFProcessorEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "processorIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFProcessorEntry.setStatus("mandatory")


class _DMTFProcessorState_Type(Integer32):
    """Custom type dMTFProcessorState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFProcessorState_Type.__name__ = "Integer32"
_DMTFProcessorState_Object = MibTableColumn
dMTFProcessorState = _DMTFProcessorState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 0),
    _DMTFProcessorState_Type()
)
dMTFProcessorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFProcessorState.setStatus("mandatory")
_ProcessorIndexAtt1_Type = DmiInteger
_ProcessorIndexAtt1_Object = MibTableColumn
processorIndexAtt1 = _ProcessorIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 1),
    _ProcessorIndexAtt1_Type()
)
processorIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorIndexAtt1.setStatus("mandatory")


class _ProcessorTypeAtt2_Type(Integer32):
    """Custom type processorTypeAtt2 based on Integer32"""
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
        *(("centralProcessor", 3),
          ("dSPProcessor", 5),
          ("mathProcessor", 4),
          ("other", 1),
          ("unknown", 2),
          ("videoProcessor", 6))
    )


_ProcessorTypeAtt2_Type.__name__ = "Integer32"
_ProcessorTypeAtt2_Object = MibTableColumn
processorTypeAtt2 = _ProcessorTypeAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 2),
    _ProcessorTypeAtt2_Type()
)
processorTypeAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorTypeAtt2.setStatus("mandatory")


class _ProcessorFamilyAtt3_Type(Integer32):
    """Custom type processorFamilyAtt3 based on Integer32"""
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
              18,
              19,
              25,
              26,
              32,
              33,
              34,
              35,
              36,
              48,
              64,
              80,
              96,
              97,
              98,
              99,
              100,
              101,
              112,
              128,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("alphaFamily", 48),
          ("celeron", 15),
          ("hobbitFamily", 112),
          ("k5Family", 25),
          ("k6Family", 26),
          ("m1Family", 18),
          ("m2Family", 19),
          ("mIPSFamily", 64),
          ("other", 1),
          ("pARISCFamily", 144),
          ("pentiumFamily", 11),
          ("pentiumII", 13),
          ("pentiumMMX", 14),
          ("pentiumPro", 12),
          ("powerPC601", 33),
          ("powerPC603", 34),
          ("powerPC603-1", 35),
          ("powerPC604", 36),
          ("powerPCFamily", 32),
          ("sPARCFamily", 80),
          ("unknown", 2),
          ("v30Family", 160),
          ("weitek", 128),
          ("x68000", 98),
          ("x68010", 99),
          ("x68020", 100),
          ("x68030", 101),
          ("x68040", 96),
          ("x68xxxFamily", 97),
          ("x80286", 4),
          ("x80287", 8),
          ("x80386", 5),
          ("x80387", 9),
          ("x80486", 6),
          ("x80487", 10),
          ("x8086", 3),
          ("x8087", 7),
          ("xeon", 16))
    )


_ProcessorFamilyAtt3_Type.__name__ = "Integer32"
_ProcessorFamilyAtt3_Object = MibTableColumn
processorFamilyAtt3 = _ProcessorFamilyAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 3),
    _ProcessorFamilyAtt3_Type()
)
processorFamilyAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorFamilyAtt3.setStatus("mandatory")
_ProcessorVersionInformationAtt4_Type = DmiDisplaystring
_ProcessorVersionInformationAtt4_Object = MibTableColumn
processorVersionInformationAtt4 = _ProcessorVersionInformationAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 4),
    _ProcessorVersionInformationAtt4_Type()
)
processorVersionInformationAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorVersionInformationAtt4.setStatus("mandatory")
_MaximumSpeedAtt5_Type = DmiInteger
_MaximumSpeedAtt5_Object = MibTableColumn
maximumSpeedAtt5 = _MaximumSpeedAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 5),
    _MaximumSpeedAtt5_Type()
)
maximumSpeedAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumSpeedAtt5.setStatus("mandatory")
_CurrentSpeedAtt6_Type = DmiInteger
_CurrentSpeedAtt6_Object = MibTableColumn
currentSpeedAtt6 = _CurrentSpeedAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 6),
    _CurrentSpeedAtt6_Type()
)
currentSpeedAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSpeedAtt6.setStatus("mandatory")


class _ProcessorUpgradeAtt7_Type(Integer32):
    """Custom type processorUpgradeAtt7 based on Integer32"""
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
        *(("daughterBoard", 3),
          ("lIFSocket", 7),
          ("none", 6),
          ("other", 1),
          ("replacementPiggyBack", 5),
          ("slot1", 8),
          ("slot2", 9),
          ("unknown", 2),
          ("zIFSocket", 4))
    )


_ProcessorUpgradeAtt7_Type.__name__ = "Integer32"
_ProcessorUpgradeAtt7_Object = MibTableColumn
processorUpgradeAtt7 = _ProcessorUpgradeAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 7),
    _ProcessorUpgradeAtt7_Type()
)
processorUpgradeAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorUpgradeAtt7.setStatus("mandatory")
_FRUGroupIndexAtt8_Type = DmiInteger
_FRUGroupIndexAtt8_Object = MibTableColumn
fRUGroupIndexAtt8 = _FRUGroupIndexAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 8),
    _FRUGroupIndexAtt8_Type()
)
fRUGroupIndexAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt8.setStatus("mandatory")
_OperationalGroupIndexAtt9_Type = DmiInteger
_OperationalGroupIndexAtt9_Object = MibTableColumn
operationalGroupIndexAtt9 = _OperationalGroupIndexAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 9),
    _OperationalGroupIndexAtt9_Type()
)
operationalGroupIndexAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt9.setStatus("mandatory")
_Level1CacheIndexAtt10_Type = DmiInteger
_Level1CacheIndexAtt10_Object = MibTableColumn
level1CacheIndexAtt10 = _Level1CacheIndexAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 10),
    _Level1CacheIndexAtt10_Type()
)
level1CacheIndexAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    level1CacheIndexAtt10.setStatus("mandatory")
_Level2CacheIndexAtt11_Type = DmiInteger
_Level2CacheIndexAtt11_Object = MibTableColumn
level2CacheIndexAtt11 = _Level2CacheIndexAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 11),
    _Level2CacheIndexAtt11_Type()
)
level2CacheIndexAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    level2CacheIndexAtt11.setStatus("mandatory")
_Level3CacheIndexAtt12_Type = DmiInteger
_Level3CacheIndexAtt12_Object = MibTableColumn
level3CacheIndexAtt12 = _Level3CacheIndexAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 5, 1, 12),
    _Level3CacheIndexAtt12_Type()
)
level3CacheIndexAtt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    level3CacheIndexAtt12.setStatus("mandatory")
_DMTFSystemCacheTable_Object = MibTable
dMTFSystemCacheTable = _DMTFSystemCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9)
)
if mibBuilder.loadTexts:
    dMTFSystemCacheTable.setStatus("mandatory")
_DMTFSystemCacheEntry_Object = MibTableRow
dMTFSystemCacheEntry = _DMTFSystemCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1)
)
dMTFSystemCacheEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "systemCacheIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSystemCacheEntry.setStatus("mandatory")


class _DMTFSystemCacheState_Type(Integer32):
    """Custom type dMTFSystemCacheState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSystemCacheState_Type.__name__ = "Integer32"
_DMTFSystemCacheState_Object = MibTableColumn
dMTFSystemCacheState = _DMTFSystemCacheState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 0),
    _DMTFSystemCacheState_Type()
)
dMTFSystemCacheState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSystemCacheState.setStatus("mandatory")
_SystemCacheIndexAtt1_Type = DmiInteger
_SystemCacheIndexAtt1_Object = MibTableColumn
systemCacheIndexAtt1 = _SystemCacheIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 1),
    _SystemCacheIndexAtt1_Type()
)
systemCacheIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCacheIndexAtt1.setStatus("mandatory")


class _SystemCacheLevelAtt2_Type(Integer32):
    """Custom type systemCacheLevelAtt2 based on Integer32"""
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
        *(("other", 1),
          ("primary", 3),
          ("secondary", 4),
          ("tertiary", 5),
          ("unknown", 2))
    )


_SystemCacheLevelAtt2_Type.__name__ = "Integer32"
_SystemCacheLevelAtt2_Object = MibTableColumn
systemCacheLevelAtt2 = _SystemCacheLevelAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 2),
    _SystemCacheLevelAtt2_Type()
)
systemCacheLevelAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCacheLevelAtt2.setStatus("mandatory")
_SystemCacheSpeedAtt3_Type = DmiInteger
_SystemCacheSpeedAtt3_Object = MibTableColumn
systemCacheSpeedAtt3 = _SystemCacheSpeedAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 3),
    _SystemCacheSpeedAtt3_Type()
)
systemCacheSpeedAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCacheSpeedAtt3.setStatus("mandatory")
_SystemCacheSizeAtt4_Type = DmiInteger
_SystemCacheSizeAtt4_Object = MibTableColumn
systemCacheSizeAtt4 = _SystemCacheSizeAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 4),
    _SystemCacheSizeAtt4_Type()
)
systemCacheSizeAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCacheSizeAtt4.setStatus("mandatory")


class _SystemCacheWritePolicyAtt5_Type(Integer32):
    """Custom type systemCacheWritePolicyAtt5 based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("variesWithAddress", 5),
          ("writeBack", 3),
          ("writeThrough", 4))
    )


_SystemCacheWritePolicyAtt5_Type.__name__ = "Integer32"
_SystemCacheWritePolicyAtt5_Object = MibTableColumn
systemCacheWritePolicyAtt5 = _SystemCacheWritePolicyAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 5),
    _SystemCacheWritePolicyAtt5_Type()
)
systemCacheWritePolicyAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCacheWritePolicyAtt5.setStatus("mandatory")


class _SystemCacheErrorCorrectionAtt6_Type(Integer32):
    """Custom type systemCacheErrorCorrectionAtt6 based on Integer32"""
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
        *(("multiBitECC", 6),
          ("none", 3),
          ("other", 1),
          ("parity", 4),
          ("singleBitECC", 5),
          ("unknown", 2))
    )


_SystemCacheErrorCorrectionAtt6_Type.__name__ = "Integer32"
_SystemCacheErrorCorrectionAtt6_Object = MibTableColumn
systemCacheErrorCorrectionAtt6 = _SystemCacheErrorCorrectionAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 6),
    _SystemCacheErrorCorrectionAtt6_Type()
)
systemCacheErrorCorrectionAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCacheErrorCorrectionAtt6.setStatus("mandatory")
_FRUGroupIndexAtt7_1_Type = DmiInteger
_FRUGroupIndexAtt7_1_Object = MibScalar
fRUGroupIndexAtt7_1 = _FRUGroupIndexAtt7_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 7),
    _FRUGroupIndexAtt7_1_Type()
)
fRUGroupIndexAtt7_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt7_1.setStatus("mandatory")
_OperationalGroupIndexAtt8_2_Type = DmiInteger
_OperationalGroupIndexAtt8_2_Object = MibScalar
operationalGroupIndexAtt8_2 = _OperationalGroupIndexAtt8_2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 8),
    _OperationalGroupIndexAtt8_2_Type()
)
operationalGroupIndexAtt8_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt8_2.setStatus("mandatory")


class _SystemCacheTypeAtt9_Type(Integer32):
    """Custom type systemCacheTypeAtt9 based on Integer32"""
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
        *(("data", 4),
          ("instruction", 3),
          ("other", 1),
          ("unified", 5),
          ("unknown", 2))
    )


_SystemCacheTypeAtt9_Type.__name__ = "Integer32"
_SystemCacheTypeAtt9_Object = MibTableColumn
systemCacheTypeAtt9 = _SystemCacheTypeAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 9),
    _SystemCacheTypeAtt9_Type()
)
systemCacheTypeAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCacheTypeAtt9.setStatus("mandatory")
_LineSizeAtt10_Type = DmiInteger
_LineSizeAtt10_Object = MibTableColumn
lineSizeAtt10 = _LineSizeAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 10),
    _LineSizeAtt10_Type()
)
lineSizeAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSizeAtt10.setStatus("mandatory")


class _VolatilityAtt11_Type(Integer32):
    """Custom type volatilityAtt11 based on Integer32"""
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
          ("permanentNonVolatile", 5),
          ("temporaryNonVolatile", 6),
          ("temporaryVolatile", 3),
          ("uPSNonVolatile", 7),
          ("unknown", 2),
          ("volatile", 4))
    )


_VolatilityAtt11_Type.__name__ = "Integer32"
_VolatilityAtt11_Object = MibTableColumn
volatilityAtt11 = _VolatilityAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 11),
    _VolatilityAtt11_Type()
)
volatilityAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volatilityAtt11.setStatus("mandatory")


class _ReplacementPolicyAtt12_Type(Integer32):
    """Custom type replacementPolicyAtt12 based on Integer32"""
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
        *(("firstInFirstOutFIFO", 4),
          ("lastInFirstOutLIFO", 5),
          ("leastFrequentlyUsedLFU", 6),
          ("leastRecentlyUsedLRU", 3),
          ("mostFrequentlyUsedMFU", 7),
          ("other", 1),
          ("unknown", 2))
    )


_ReplacementPolicyAtt12_Type.__name__ = "Integer32"
_ReplacementPolicyAtt12_Object = MibTableColumn
replacementPolicyAtt12 = _ReplacementPolicyAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 12),
    _ReplacementPolicyAtt12_Type()
)
replacementPolicyAtt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replacementPolicyAtt12.setStatus("mandatory")


class _ReadPolicyAtt13_Type(Integer32):
    """Custom type readPolicyAtt13 based on Integer32"""
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
        *(("other", 1),
          ("read", 3),
          ("readAhead", 4),
          ("readAndReadAhead", 5),
          ("unknown", 2))
    )


_ReadPolicyAtt13_Type.__name__ = "Integer32"
_ReadPolicyAtt13_Object = MibTableColumn
readPolicyAtt13 = _ReadPolicyAtt13_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 13),
    _ReadPolicyAtt13_Type()
)
readPolicyAtt13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readPolicyAtt13.setStatus("mandatory")
_FlushTimerAtt14_Type = DmiInteger
_FlushTimerAtt14_Object = MibTableColumn
flushTimerAtt14 = _FlushTimerAtt14_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 14),
    _FlushTimerAtt14_Type()
)
flushTimerAtt14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flushTimerAtt14.setStatus("mandatory")


class _AssociativityAtt15_Type(Integer32):
    """Custom type associativityAtt15 based on Integer32"""
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
        *(("directMapped", 3),
          ("fullyAssociative", 6),
          ("other", 1),
          ("unknown", 2),
          ("x2WaySetAssociative", 4),
          ("x4WaySetAssociative", 5))
    )


_AssociativityAtt15_Type.__name__ = "Integer32"
_AssociativityAtt15_Object = MibTableColumn
associativityAtt15 = _AssociativityAtt15_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 9, 1, 15),
    _AssociativityAtt15_Type()
)
associativityAtt15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associativityAtt15.setStatus("mandatory")
_DMTFParallelPortsTable_Object = MibTable
dMTFParallelPortsTable = _DMTFParallelPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10)
)
if mibBuilder.loadTexts:
    dMTFParallelPortsTable.setStatus("mandatory")
_DMTFParallelPortsEntry_Object = MibTableRow
dMTFParallelPortsEntry = _DMTFParallelPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1)
)
dMTFParallelPortsEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "parallelPortIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFParallelPortsEntry.setStatus("mandatory")


class _DMTFParallelPortsState_Type(Integer32):
    """Custom type dMTFParallelPortsState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFParallelPortsState_Type.__name__ = "Integer32"
_DMTFParallelPortsState_Object = MibTableColumn
dMTFParallelPortsState = _DMTFParallelPortsState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 0),
    _DMTFParallelPortsState_Type()
)
dMTFParallelPortsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFParallelPortsState.setStatus("mandatory")
_ParallelPortIndexAtt1_Type = DmiInteger
_ParallelPortIndexAtt1_Object = MibTableColumn
parallelPortIndexAtt1 = _ParallelPortIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 1),
    _ParallelPortIndexAtt1_Type()
)
parallelPortIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortIndexAtt1.setStatus("mandatory")
_ParallelBaseIOAddressAtt2_Type = DmiInteger64
_ParallelBaseIOAddressAtt2_Object = MibTableColumn
parallelBaseIOAddressAtt2 = _ParallelBaseIOAddressAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 2),
    _ParallelBaseIOAddressAtt2_Type()
)
parallelBaseIOAddressAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelBaseIOAddressAtt2.setStatus("mandatory")
_IRQUsedAtt3_1_Type = DmiInteger
_IRQUsedAtt3_1_Object = MibScalar
iRQUsedAtt3_1 = _IRQUsedAtt3_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 3),
    _IRQUsedAtt3_1_Type()
)
iRQUsedAtt3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRQUsedAtt3_1.setStatus("mandatory")
_LogicalNameAtt4_1_Type = DmiDisplaystring
_LogicalNameAtt4_1_Object = MibScalar
logicalNameAtt4_1 = _LogicalNameAtt4_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 4),
    _LogicalNameAtt4_1_Type()
)
logicalNameAtt4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalNameAtt4_1.setStatus("mandatory")


class _ConnectorTypeAtt5_1_Type(Integer32):
    """Custom type connectorTypeAtt5_1 based on Integer32"""
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
              160,
              161,
              162)
        )
    )
    namedValues = NamedValues(
        *(("centronics", 5),
          ("centronics14", 160),
          ("dB25Female", 3),
          ("dB25Male", 4),
          ("dB36Female", 161),
          ("miniCentronics", 6),
          ("miniCentronics20", 162),
          ("other", 1),
          ("proprietary", 7),
          ("unknown", 2))
    )


_ConnectorTypeAtt5_1_Type.__name__ = "Integer32"
_ConnectorTypeAtt5_1_Object = MibScalar
connectorTypeAtt5_1 = _ConnectorTypeAtt5_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 5),
    _ConnectorTypeAtt5_1_Type()
)
connectorTypeAtt5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectorTypeAtt5_1.setStatus("mandatory")


class _ConnectorPinoutAtt6_Type(Integer32):
    """Custom type connectorPinoutAtt6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              160,
              161,
              162,
              163,
              164)
        )
    )
    namedValues = NamedValues(
        *(("iEEE1284", 5),
          ("other", 1),
          ("pC98", 160),
          ("pC98Full", 164),
          ("pC98Hireso", 161),
          ("pC98Note", 163),
          ("pCH98", 162),
          ("pS2", 4),
          ("proprietary", 6),
          ("unknown", 2),
          ("xTAT", 3))
    )


_ConnectorPinoutAtt6_Type.__name__ = "Integer32"
_ConnectorPinoutAtt6_Object = MibTableColumn
connectorPinoutAtt6 = _ConnectorPinoutAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 6),
    _ConnectorPinoutAtt6_Type()
)
connectorPinoutAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectorPinoutAtt6.setStatus("mandatory")


class _DMASupportAtt7_Type(Integer32):
    """Custom type dMASupportAtt7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DMASupportAtt7_Type.__name__ = "Integer32"
_DMASupportAtt7_Object = MibTableColumn
dMASupportAtt7 = _DMASupportAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 7),
    _DMASupportAtt7_Type()
)
dMASupportAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMASupportAtt7.setStatus("mandatory")
_ParallelPortCapabilitiesAtt8_Type = DmiInteger
_ParallelPortCapabilitiesAtt8_Object = MibTableColumn
parallelPortCapabilitiesAtt8 = _ParallelPortCapabilitiesAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 8),
    _ParallelPortCapabilitiesAtt8_Type()
)
parallelPortCapabilitiesAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortCapabilitiesAtt8.setStatus("mandatory")
_OperationalGroupIndexAtt9_1_Type = DmiInteger
_OperationalGroupIndexAtt9_1_Object = MibScalar
operationalGroupIndexAtt9_1 = _OperationalGroupIndexAtt9_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 9),
    _OperationalGroupIndexAtt9_1_Type()
)
operationalGroupIndexAtt9_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt9_1.setStatus("mandatory")


class _ParallelPortSecuritySettingsAtt10_Type(Integer32):
    """Custom type parallelPortSecuritySettingsAtt10 based on Integer32"""
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
        *(("bootBypass", 6),
          ("externalInterfaceEnabled", 5),
          ("externalInterfaceLockedOut", 4),
          ("none", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ParallelPortSecuritySettingsAtt10_Type.__name__ = "Integer32"
_ParallelPortSecuritySettingsAtt10_Object = MibTableColumn
parallelPortSecuritySettingsAtt10 = _ParallelPortSecuritySettingsAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 10, 1, 10),
    _ParallelPortSecuritySettingsAtt10_Type()
)
parallelPortSecuritySettingsAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortSecuritySettingsAtt10.setStatus("mandatory")
_DMTFSerialPortsTable_Object = MibTable
dMTFSerialPortsTable = _DMTFSerialPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11)
)
if mibBuilder.loadTexts:
    dMTFSerialPortsTable.setStatus("mandatory")
_DMTFSerialPortsEntry_Object = MibTableRow
dMTFSerialPortsEntry = _DMTFSerialPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1)
)
dMTFSerialPortsEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "serialPortIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSerialPortsEntry.setStatus("mandatory")


class _DMTFSerialPortsState_Type(Integer32):
    """Custom type dMTFSerialPortsState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSerialPortsState_Type.__name__ = "Integer32"
_DMTFSerialPortsState_Object = MibTableColumn
dMTFSerialPortsState = _DMTFSerialPortsState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 0),
    _DMTFSerialPortsState_Type()
)
dMTFSerialPortsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSerialPortsState.setStatus("mandatory")
_SerialPortIndexAtt1_Type = DmiInteger
_SerialPortIndexAtt1_Object = MibTableColumn
serialPortIndexAtt1 = _SerialPortIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 1),
    _SerialPortIndexAtt1_Type()
)
serialPortIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortIndexAtt1.setStatus("mandatory")
_SerialBaseIOAddressAtt2_Type = DmiInteger64
_SerialBaseIOAddressAtt2_Object = MibTableColumn
serialBaseIOAddressAtt2 = _SerialBaseIOAddressAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 2),
    _SerialBaseIOAddressAtt2_Type()
)
serialBaseIOAddressAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialBaseIOAddressAtt2.setStatus("mandatory")
_IRQUsedAtt3_Type = DmiInteger
_IRQUsedAtt3_Object = MibTableColumn
iRQUsedAtt3 = _IRQUsedAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 3),
    _IRQUsedAtt3_Type()
)
iRQUsedAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRQUsedAtt3.setStatus("mandatory")
_LogicalNameAtt4_Type = DmiDisplaystring
_LogicalNameAtt4_Object = MibTableColumn
logicalNameAtt4 = _LogicalNameAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 4),
    _LogicalNameAtt4_Type()
)
logicalNameAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalNameAtt4.setStatus("mandatory")


class _ConnectorTypeAtt5_Type(Integer32):
    """Custom type connectorTypeAtt5 based on Integer32"""
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
              160,
              161)
        )
    )
    namedValues = NamedValues(
        *(("circularDIN8Female", 11),
          ("circularDIN8Male", 10),
          ("dB25PinFemale", 6),
          ("dB25PinMale", 5),
          ("dB9PinFemale", 4),
          ("dB9PinMale", 3),
          ("miniCentronicsType14", 160),
          ("miniCentronicsType26", 161),
          ("other", 1),
          ("proprietary", 9),
          ("rJ11", 7),
          ("rJ45", 8),
          ("unknown", 2))
    )


_ConnectorTypeAtt5_Type.__name__ = "Integer32"
_ConnectorTypeAtt5_Object = MibTableColumn
connectorTypeAtt5 = _ConnectorTypeAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 5),
    _ConnectorTypeAtt5_Type()
)
connectorTypeAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectorTypeAtt5.setStatus("mandatory")
_MaximumSpeedAtt6_Type = DmiInteger
_MaximumSpeedAtt6_Object = MibTableColumn
maximumSpeedAtt6 = _MaximumSpeedAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 6),
    _MaximumSpeedAtt6_Type()
)
maximumSpeedAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumSpeedAtt6.setStatus("mandatory")


class _SerialPortCapabilitiesAtt7_Type(Integer32):
    """Custom type serialPortCapabilitiesAtt7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              160,
              161)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("x16450Compatible", 4),
          ("x16550ACompatible", 6),
          ("x16550Compatible", 5),
          ("x8251Compatible", 160),
          ("x8251FIFOCompatible", 161),
          ("xTATCompatible", 3))
    )


_SerialPortCapabilitiesAtt7_Type.__name__ = "Integer32"
_SerialPortCapabilitiesAtt7_Object = MibTableColumn
serialPortCapabilitiesAtt7 = _SerialPortCapabilitiesAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 7),
    _SerialPortCapabilitiesAtt7_Type()
)
serialPortCapabilitiesAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortCapabilitiesAtt7.setStatus("mandatory")
_OperationalGroupIndexAtt8_1_Type = DmiInteger
_OperationalGroupIndexAtt8_1_Object = MibScalar
operationalGroupIndexAtt8_1 = _OperationalGroupIndexAtt8_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 8),
    _OperationalGroupIndexAtt8_1_Type()
)
operationalGroupIndexAtt8_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt8_1.setStatus("mandatory")


class _SerialPortSecuritySettingsAtt9_Type(Integer32):
    """Custom type serialPortSecuritySettingsAtt9 based on Integer32"""
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
        *(("bootBypass", 6),
          ("externalInterfaceEnabled", 5),
          ("externalInterfaceLockedOut", 4),
          ("none", 3),
          ("other", 1),
          ("unknown", 2))
    )


_SerialPortSecuritySettingsAtt9_Type.__name__ = "Integer32"
_SerialPortSecuritySettingsAtt9_Object = MibTableColumn
serialPortSecuritySettingsAtt9 = _SerialPortSecuritySettingsAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 11, 1, 9),
    _SerialPortSecuritySettingsAtt9_Type()
)
serialPortSecuritySettingsAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortSecuritySettingsAtt9.setStatus("mandatory")
_DMTFPowerSupplyTable_Object = MibTable
dMTFPowerSupplyTable = _DMTFPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16)
)
if mibBuilder.loadTexts:
    dMTFPowerSupplyTable.setStatus("mandatory")
_DMTFPowerSupplyEntry_Object = MibTableRow
dMTFPowerSupplyEntry = _DMTFPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1)
)
dMTFPowerSupplyEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "powerSupplyIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFPowerSupplyEntry.setStatus("mandatory")


class _DMTFPowerSupplyState_Type(Integer32):
    """Custom type dMTFPowerSupplyState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFPowerSupplyState_Type.__name__ = "Integer32"
_DMTFPowerSupplyState_Object = MibTableColumn
dMTFPowerSupplyState = _DMTFPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 0),
    _DMTFPowerSupplyState_Type()
)
dMTFPowerSupplyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFPowerSupplyState.setStatus("mandatory")
_PowerSupplyIndexAtt1_Type = DmiInteger
_PowerSupplyIndexAtt1_Object = MibTableColumn
powerSupplyIndexAtt1 = _PowerSupplyIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 1),
    _PowerSupplyIndexAtt1_Type()
)
powerSupplyIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndexAtt1.setStatus("mandatory")
_FRUGroupIndexAtt2_1_Type = DmiInteger
_FRUGroupIndexAtt2_1_Object = MibScalar
fRUGroupIndexAtt2_1 = _FRUGroupIndexAtt2_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 2),
    _FRUGroupIndexAtt2_1_Type()
)
fRUGroupIndexAtt2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt2_1.setStatus("mandatory")
_OperationalGroupIndexAtt3_1_Type = DmiInteger
_OperationalGroupIndexAtt3_1_Object = MibScalar
operationalGroupIndexAtt3_1 = _OperationalGroupIndexAtt3_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 3),
    _OperationalGroupIndexAtt3_1_Type()
)
operationalGroupIndexAtt3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt3_1.setStatus("mandatory")
_PowerUnitIndexAtt4_Type = DmiInteger
_PowerUnitIndexAtt4_Object = MibTableColumn
powerUnitIndexAtt4 = _PowerUnitIndexAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 4),
    _PowerUnitIndexAtt4_Type()
)
powerUnitIndexAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitIndexAtt4.setStatus("mandatory")


class _PowerSupplyTypeAtt5_Type(Integer32):
    """Custom type powerSupplyTypeAtt5 based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("battery", 5),
          ("converter", 7),
          ("linear", 3),
          ("other", 1),
          ("regulator", 8),
          ("switching", 4),
          ("uPS", 6),
          ("unknown", 2))
    )


_PowerSupplyTypeAtt5_Type.__name__ = "Integer32"
_PowerSupplyTypeAtt5_Object = MibTableColumn
powerSupplyTypeAtt5 = _PowerSupplyTypeAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 5),
    _PowerSupplyTypeAtt5_Type()
)
powerSupplyTypeAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyTypeAtt5.setStatus("mandatory")
_InputVoltageCapabilityDescriptionAtt6_Type = DmiDisplaystring
_InputVoltageCapabilityDescriptionAtt6_Object = MibTableColumn
inputVoltageCapabilityDescriptionAtt6 = _InputVoltageCapabilityDescriptionAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 6),
    _InputVoltageCapabilityDescriptionAtt6_Type()
)
inputVoltageCapabilityDescriptionAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltageCapabilityDescriptionAtt6.setStatus("mandatory")
_Range1InputVoltageLowAtt7_Type = DmiInteger
_Range1InputVoltageLowAtt7_Object = MibTableColumn
range1InputVoltageLowAtt7 = _Range1InputVoltageLowAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 7),
    _Range1InputVoltageLowAtt7_Type()
)
range1InputVoltageLowAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range1InputVoltageLowAtt7.setStatus("mandatory")
_Range1InputVoltageHighAtt8_Type = DmiInteger
_Range1InputVoltageHighAtt8_Object = MibTableColumn
range1InputVoltageHighAtt8 = _Range1InputVoltageHighAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 8),
    _Range1InputVoltageHighAtt8_Type()
)
range1InputVoltageHighAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range1InputVoltageHighAtt8.setStatus("mandatory")
_Range1VoltageProbeIndexAtt9_Type = DmiInteger
_Range1VoltageProbeIndexAtt9_Object = MibTableColumn
range1VoltageProbeIndexAtt9 = _Range1VoltageProbeIndexAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 9),
    _Range1VoltageProbeIndexAtt9_Type()
)
range1VoltageProbeIndexAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range1VoltageProbeIndexAtt9.setStatus("mandatory")
_Range1ElectricalCurrentProbeIndexAtt10_Type = DmiInteger
_Range1ElectricalCurrentProbeIndexAtt10_Object = MibTableColumn
range1ElectricalCurrentProbeIndexAtt10 = _Range1ElectricalCurrentProbeIndexAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 10),
    _Range1ElectricalCurrentProbeIndexAtt10_Type()
)
range1ElectricalCurrentProbeIndexAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range1ElectricalCurrentProbeIndexAtt10.setStatus("mandatory")
_Range2InputVoltageLowAtt11_Type = DmiInteger
_Range2InputVoltageLowAtt11_Object = MibTableColumn
range2InputVoltageLowAtt11 = _Range2InputVoltageLowAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 11),
    _Range2InputVoltageLowAtt11_Type()
)
range2InputVoltageLowAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range2InputVoltageLowAtt11.setStatus("mandatory")
_Range2InputVoltageHighAtt12_Type = DmiInteger
_Range2InputVoltageHighAtt12_Object = MibTableColumn
range2InputVoltageHighAtt12 = _Range2InputVoltageHighAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 12),
    _Range2InputVoltageHighAtt12_Type()
)
range2InputVoltageHighAtt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range2InputVoltageHighAtt12.setStatus("mandatory")
_Range2VoltageProbeIndexAtt13_Type = DmiInteger
_Range2VoltageProbeIndexAtt13_Object = MibTableColumn
range2VoltageProbeIndexAtt13 = _Range2VoltageProbeIndexAtt13_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 13),
    _Range2VoltageProbeIndexAtt13_Type()
)
range2VoltageProbeIndexAtt13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range2VoltageProbeIndexAtt13.setStatus("mandatory")
_Range2CurrentProbeIndexAtt14_Type = DmiInteger
_Range2CurrentProbeIndexAtt14_Object = MibTableColumn
range2CurrentProbeIndexAtt14 = _Range2CurrentProbeIndexAtt14_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 14),
    _Range2CurrentProbeIndexAtt14_Type()
)
range2CurrentProbeIndexAtt14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range2CurrentProbeIndexAtt14.setStatus("mandatory")


class _ActiveInputVoltageRangeAtt15_Type(Integer32):
    """Custom type activeInputVoltageRangeAtt15 based on Integer32"""
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
        *(("both", 5),
          ("other", 1),
          ("range1", 3),
          ("range2", 4),
          ("unknown", 2))
    )


_ActiveInputVoltageRangeAtt15_Type.__name__ = "Integer32"
_ActiveInputVoltageRangeAtt15_Object = MibTableColumn
activeInputVoltageRangeAtt15 = _ActiveInputVoltageRangeAtt15_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 15),
    _ActiveInputVoltageRangeAtt15_Type()
)
activeInputVoltageRangeAtt15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeInputVoltageRangeAtt15.setStatus("mandatory")


class _InputVoltageRangeSwitchingAtt16_Type(Integer32):
    """Custom type inputVoltageRangeSwitchingAtt16 based on Integer32"""
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
        *(("autoswitch", 4),
          ("manual", 3),
          ("notApplicable", 6),
          ("other", 1),
          ("unknown", 2),
          ("wideRange", 5))
    )


_InputVoltageRangeSwitchingAtt16_Type.__name__ = "Integer32"
_InputVoltageRangeSwitchingAtt16_Object = MibTableColumn
inputVoltageRangeSwitchingAtt16 = _InputVoltageRangeSwitchingAtt16_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 16),
    _InputVoltageRangeSwitchingAtt16_Type()
)
inputVoltageRangeSwitchingAtt16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltageRangeSwitchingAtt16.setStatus("mandatory")
_Range1InputFrequencyLowAtt17_Type = DmiInteger
_Range1InputFrequencyLowAtt17_Object = MibTableColumn
range1InputFrequencyLowAtt17 = _Range1InputFrequencyLowAtt17_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 17),
    _Range1InputFrequencyLowAtt17_Type()
)
range1InputFrequencyLowAtt17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range1InputFrequencyLowAtt17.setStatus("mandatory")
_Range1InputFrequencyHighAtt18_Type = DmiInteger
_Range1InputFrequencyHighAtt18_Object = MibTableColumn
range1InputFrequencyHighAtt18 = _Range1InputFrequencyHighAtt18_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 18),
    _Range1InputFrequencyHighAtt18_Type()
)
range1InputFrequencyHighAtt18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range1InputFrequencyHighAtt18.setStatus("mandatory")
_Range2InputFrequencyLowAtt19_Type = DmiInteger
_Range2InputFrequencyLowAtt19_Object = MibTableColumn
range2InputFrequencyLowAtt19 = _Range2InputFrequencyLowAtt19_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 19),
    _Range2InputFrequencyLowAtt19_Type()
)
range2InputFrequencyLowAtt19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range2InputFrequencyLowAtt19.setStatus("mandatory")
_Range2InputFrequencyHighAtt20_Type = DmiInteger
_Range2InputFrequencyHighAtt20_Object = MibTableColumn
range2InputFrequencyHighAtt20 = _Range2InputFrequencyHighAtt20_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 20),
    _Range2InputFrequencyHighAtt20_Type()
)
range2InputFrequencyHighAtt20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range2InputFrequencyHighAtt20.setStatus("mandatory")
_TotalOutputPowerAtt21_Type = DmiInteger
_TotalOutputPowerAtt21_Object = MibTableColumn
totalOutputPowerAtt21 = _TotalOutputPowerAtt21_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 1, 21),
    _TotalOutputPowerAtt21_Type()
)
totalOutputPowerAtt21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutputPowerAtt21.setStatus("mandatory")


class _DMTFPowerSupplyEvSys_Type(Integer32):
    """Custom type dMTFPowerSupplyEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFPowerSupplyEvSys_Type.__name__ = "Integer32"
_DMTFPowerSupplyEvSys_Object = MibScalar
dMTFPowerSupplyEvSys = _DMTFPowerSupplyEvSys_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 6),
    _DMTFPowerSupplyEvSys_Type()
)
dMTFPowerSupplyEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFPowerSupplyEvSys.setStatus("mandatory")


class _DMTFPowerSupplyEvSub_Type(Integer32):
    """Custom type dMTFPowerSupplyEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFPowerSupplyEvSub_Type.__name__ = "Integer32"
_DMTFPowerSupplyEvSub_Object = MibScalar
dMTFPowerSupplyEvSub = _DMTFPowerSupplyEvSub_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 7),
    _DMTFPowerSupplyEvSub_Type()
)
dMTFPowerSupplyEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFPowerSupplyEvSub.setStatus("mandatory")
_DMTFCoolingDeviceTable_Object = MibTable
dMTFCoolingDeviceTable = _DMTFCoolingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17)
)
if mibBuilder.loadTexts:
    dMTFCoolingDeviceTable.setStatus("mandatory")
_DMTFCoolingDeviceEntry_Object = MibTableRow
dMTFCoolingDeviceEntry = _DMTFCoolingDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 1)
)
dMTFCoolingDeviceEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "coolingDeviceTableIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFCoolingDeviceEntry.setStatus("mandatory")


class _DMTFCoolingDeviceState_Type(Integer32):
    """Custom type dMTFCoolingDeviceState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFCoolingDeviceState_Type.__name__ = "Integer32"
_DMTFCoolingDeviceState_Object = MibTableColumn
dMTFCoolingDeviceState = _DMTFCoolingDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 1, 0),
    _DMTFCoolingDeviceState_Type()
)
dMTFCoolingDeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFCoolingDeviceState.setStatus("mandatory")
_CoolingDeviceTableIndexAtt1_Type = DmiInteger
_CoolingDeviceTableIndexAtt1_Object = MibTableColumn
coolingDeviceTableIndexAtt1 = _CoolingDeviceTableIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 1, 1),
    _CoolingDeviceTableIndexAtt1_Type()
)
coolingDeviceTableIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceTableIndexAtt1.setStatus("mandatory")
_FRUGroupIndexAtt2_Type = DmiInteger
_FRUGroupIndexAtt2_Object = MibTableColumn
fRUGroupIndexAtt2 = _FRUGroupIndexAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 1, 2),
    _FRUGroupIndexAtt2_Type()
)
fRUGroupIndexAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt2.setStatus("mandatory")
_OperationalGroupIndexAtt3_Type = DmiInteger
_OperationalGroupIndexAtt3_Object = MibTableColumn
operationalGroupIndexAtt3 = _OperationalGroupIndexAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 1, 3),
    _OperationalGroupIndexAtt3_Type()
)
operationalGroupIndexAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt3.setStatus("mandatory")
_CoolingUnitIndexAtt4_Type = DmiInteger
_CoolingUnitIndexAtt4_Object = MibTableColumn
coolingUnitIndexAtt4 = _CoolingUnitIndexAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 1, 4),
    _CoolingUnitIndexAtt4_Type()
)
coolingUnitIndexAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitIndexAtt4.setStatus("mandatory")


class _CoolingDeviceTypeAtt5_Type(Integer32):
    """Custom type coolingDeviceTypeAtt5 based on Integer32"""
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
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("activeCooling", 32),
          ("cabinetFan", 6),
          ("centrifugalBlower", 4),
          ("chipFan", 5),
          ("fan", 3),
          ("heatPipe", 8),
          ("integratedRefrigeration", 9),
          ("other", 1),
          ("passiveCooling", 33),
          ("powerSupplyFan", 7),
          ("unknown", 2))
    )


_CoolingDeviceTypeAtt5_Type.__name__ = "Integer32"
_CoolingDeviceTypeAtt5_Object = MibTableColumn
coolingDeviceTypeAtt5 = _CoolingDeviceTypeAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 1, 5),
    _CoolingDeviceTypeAtt5_Type()
)
coolingDeviceTypeAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceTypeAtt5.setStatus("mandatory")
_TemperatureProbeIndexAtt6_Type = DmiInteger
_TemperatureProbeIndexAtt6_Object = MibTableColumn
temperatureProbeIndexAtt6 = _TemperatureProbeIndexAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 1, 6),
    _TemperatureProbeIndexAtt6_Type()
)
temperatureProbeIndexAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeIndexAtt6.setStatus("mandatory")


class _DMTFCoolingDeviceEvSys_Type(Integer32):
    """Custom type dMTFCoolingDeviceEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFCoolingDeviceEvSys_Type.__name__ = "Integer32"
_DMTFCoolingDeviceEvSys_Object = MibScalar
dMTFCoolingDeviceEvSys = _DMTFCoolingDeviceEvSys_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 6),
    _DMTFCoolingDeviceEvSys_Type()
)
dMTFCoolingDeviceEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFCoolingDeviceEvSys.setStatus("mandatory")


class _DMTFCoolingDeviceEvSub_Type(Integer32):
    """Custom type dMTFCoolingDeviceEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFCoolingDeviceEvSub_Type.__name__ = "Integer32"
_DMTFCoolingDeviceEvSub_Object = MibScalar
dMTFCoolingDeviceEvSub = _DMTFCoolingDeviceEvSub_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 7),
    _DMTFCoolingDeviceEvSub_Type()
)
dMTFCoolingDeviceEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFCoolingDeviceEvSub.setStatus("mandatory")
_DMTFSystemSlotsTable_Object = MibTable
dMTFSystemSlotsTable = _DMTFSystemSlotsTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18)
)
if mibBuilder.loadTexts:
    dMTFSystemSlotsTable.setStatus("mandatory")
_DMTFSystemSlotsEntry_Object = MibTableRow
dMTFSystemSlotsEntry = _DMTFSystemSlotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1)
)
dMTFSystemSlotsEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "slotIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSystemSlotsEntry.setStatus("mandatory")


class _DMTFSystemSlotsState_Type(Integer32):
    """Custom type dMTFSystemSlotsState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSystemSlotsState_Type.__name__ = "Integer32"
_DMTFSystemSlotsState_Object = MibTableColumn
dMTFSystemSlotsState = _DMTFSystemSlotsState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1, 0),
    _DMTFSystemSlotsState_Type()
)
dMTFSystemSlotsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSystemSlotsState.setStatus("mandatory")
_SlotIndexAtt1_Type = DmiInteger
_SlotIndexAtt1_Object = MibTableColumn
slotIndexAtt1 = _SlotIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1, 1),
    _SlotIndexAtt1_Type()
)
slotIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndexAtt1.setStatus("mandatory")
_SlotTypeAtt2_Type = DmiInteger64
_SlotTypeAtt2_Object = MibTableColumn
slotTypeAtt2 = _SlotTypeAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1, 2),
    _SlotTypeAtt2_Type()
)
slotTypeAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotTypeAtt2.setStatus("mandatory")


class _SlotWidthAtt3_Type(Integer32):
    """Custom type slotWidthAtt3 based on Integer32"""
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
          ("unknown", 2),
          ("x128BitCard", 7),
          ("x16BitCard", 4),
          ("x32BitCard", 5),
          ("x64BitCard", 6),
          ("x8BitCard", 3))
    )


_SlotWidthAtt3_Type.__name__ = "Integer32"
_SlotWidthAtt3_Object = MibTableColumn
slotWidthAtt3 = _SlotWidthAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1, 3),
    _SlotWidthAtt3_Type()
)
slotWidthAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotWidthAtt3.setStatus("mandatory")


class _CurrentUsageAtt4_Type(Integer32):
    """Custom type currentUsageAtt4 based on Integer32"""
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
        *(("available", 3),
          ("inUse", 4),
          ("other", 1),
          ("unknown", 2))
    )


_CurrentUsageAtt4_Type.__name__ = "Integer32"
_CurrentUsageAtt4_Object = MibTableColumn
currentUsageAtt4 = _CurrentUsageAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1, 4),
    _CurrentUsageAtt4_Type()
)
currentUsageAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentUsageAtt4.setStatus("mandatory")
_SlotDescriptionAtt5_Type = DmiDisplaystring
_SlotDescriptionAtt5_Object = MibTableColumn
slotDescriptionAtt5 = _SlotDescriptionAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1, 5),
    _SlotDescriptionAtt5_Type()
)
slotDescriptionAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotDescriptionAtt5.setStatus("mandatory")


class _SlotCategoryAtt6_Type(Integer32):
    """Custom type slotCategoryAtt6 based on Integer32"""
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
        *(("busConnector", 3),
          ("motherboard", 5),
          ("other", 1),
          ("pCMCIASlot", 4),
          ("unknown", 2))
    )


_SlotCategoryAtt6_Type.__name__ = "Integer32"
_SlotCategoryAtt6_Object = MibTableColumn
slotCategoryAtt6 = _SlotCategoryAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1, 6),
    _SlotCategoryAtt6_Type()
)
slotCategoryAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotCategoryAtt6.setStatus("mandatory")


class _VirtualSlotAtt7_Type(Integer32):
    """Custom type virtualSlotAtt7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_VirtualSlotAtt7_Type.__name__ = "Integer32"
_VirtualSlotAtt7_Object = MibTableColumn
virtualSlotAtt7 = _VirtualSlotAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1, 7),
    _VirtualSlotAtt7_Type()
)
virtualSlotAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualSlotAtt7.setStatus("mandatory")
_ResourceUserIDAtt8_Type = DmiInteger
_ResourceUserIDAtt8_Object = MibTableColumn
resourceUserIDAtt8 = _ResourceUserIDAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 18, 1, 8),
    _ResourceUserIDAtt8_Type()
)
resourceUserIDAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceUserIDAtt8.setStatus("mandatory")
_DMTFFRUTable_Object = MibTable
dMTFFRUTable = _DMTFFRUTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29)
)
if mibBuilder.loadTexts:
    dMTFFRUTable.setStatus("mandatory")
_DMTFFRUEntry_Object = MibTableRow
dMTFFRUEntry = _DMTFFRUEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1)
)
dMTFFRUEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "fRUIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFFRUEntry.setStatus("mandatory")


class _DMTFFRUState_Type(Integer32):
    """Custom type dMTFFRUState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFFRUState_Type.__name__ = "Integer32"
_DMTFFRUState_Object = MibTableColumn
dMTFFRUState = _DMTFFRUState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 0),
    _DMTFFRUState_Type()
)
dMTFFRUState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFFRUState.setStatus("mandatory")
_FRUIndexAtt1_Type = DmiInteger
_FRUIndexAtt1_Object = MibTableColumn
fRUIndexAtt1 = _FRUIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 1),
    _FRUIndexAtt1_Type()
)
fRUIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUIndexAtt1.setStatus("mandatory")
_DeviceGroupIndexAtt2_Type = DmiInteger
_DeviceGroupIndexAtt2_Object = MibTableColumn
deviceGroupIndexAtt2 = _DeviceGroupIndexAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 2),
    _DeviceGroupIndexAtt2_Type()
)
deviceGroupIndexAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceGroupIndexAtt2.setStatus("mandatory")
_DescriptionAtt3_Type = DmiDisplaystring
_DescriptionAtt3_Object = MibTableColumn
descriptionAtt3 = _DescriptionAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 3),
    _DescriptionAtt3_Type()
)
descriptionAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    descriptionAtt3.setStatus("mandatory")
_ManufacturerAtt4_Type = DmiDisplaystring
_ManufacturerAtt4_Object = MibTableColumn
manufacturerAtt4 = _ManufacturerAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 4),
    _ManufacturerAtt4_Type()
)
manufacturerAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturerAtt4.setStatus("mandatory")
_ModelAtt5_Type = DmiDisplaystring
_ModelAtt5_Object = MibTableColumn
modelAtt5 = _ModelAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 5),
    _ModelAtt5_Type()
)
modelAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelAtt5.setStatus("mandatory")
_PartNumberAtt6_Type = DmiDisplaystring
_PartNumberAtt6_Object = MibTableColumn
partNumberAtt6 = _PartNumberAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 6),
    _PartNumberAtt6_Type()
)
partNumberAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partNumberAtt6.setStatus("mandatory")
_FRUSerialNumberAtt7_Type = DmiDisplaystring
_FRUSerialNumberAtt7_Object = MibTableColumn
fRUSerialNumberAtt7 = _FRUSerialNumberAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 7),
    _FRUSerialNumberAtt7_Type()
)
fRUSerialNumberAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUSerialNumberAtt7.setStatus("mandatory")
_RevisionLevelAtt8_Type = DmiDisplaystring
_RevisionLevelAtt8_Object = MibTableColumn
revisionLevelAtt8 = _RevisionLevelAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 8),
    _RevisionLevelAtt8_Type()
)
revisionLevelAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revisionLevelAtt8.setStatus("mandatory")
_WarrantyStartDateAtt9_Type = DmiDate
_WarrantyStartDateAtt9_Object = MibTableColumn
warrantyStartDateAtt9 = _WarrantyStartDateAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 9),
    _WarrantyStartDateAtt9_Type()
)
warrantyStartDateAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warrantyStartDateAtt9.setStatus("mandatory")
_WarrantyDurationAtt10_Type = DmiInteger
_WarrantyDurationAtt10_Object = MibTableColumn
warrantyDurationAtt10 = _WarrantyDurationAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 10),
    _WarrantyDurationAtt10_Type()
)
warrantyDurationAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warrantyDurationAtt10.setStatus("mandatory")
_SupportPhoneNumberAtt11_Type = DmiDisplaystring
_SupportPhoneNumberAtt11_Object = MibTableColumn
supportPhoneNumberAtt11 = _SupportPhoneNumberAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 11),
    _SupportPhoneNumberAtt11_Type()
)
supportPhoneNumberAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportPhoneNumberAtt11.setStatus("mandatory")
_FRUInternetUniformResourceLocatorAtt12_Type = DmiDisplaystring
_FRUInternetUniformResourceLocatorAtt12_Object = MibTableColumn
fRUInternetUniformResourceLocatorAtt12 = _FRUInternetUniformResourceLocatorAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 29, 1, 12),
    _FRUInternetUniformResourceLocatorAtt12_Type()
)
fRUInternetUniformResourceLocatorAtt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUInternetUniformResourceLocatorAtt12.setStatus("mandatory")
_DMTFOperationalStateTable_Object = MibTable
dMTFOperationalStateTable = _DMTFOperationalStateTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30)
)
if mibBuilder.loadTexts:
    dMTFOperationalStateTable.setStatus("mandatory")
_DMTFOperationalStateEntry_Object = MibTableRow
dMTFOperationalStateEntry = _DMTFOperationalStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1)
)
dMTFOperationalStateEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "operationalStateInstanceIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFOperationalStateEntry.setStatus("mandatory")


class _DMTFOperationalStateState_Type(Integer32):
    """Custom type dMTFOperationalStateState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFOperationalStateState_Type.__name__ = "Integer32"
_DMTFOperationalStateState_Object = MibTableColumn
dMTFOperationalStateState = _DMTFOperationalStateState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 0),
    _DMTFOperationalStateState_Type()
)
dMTFOperationalStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFOperationalStateState.setStatus("mandatory")
_OperationalStateInstanceIndexAtt1_Type = DmiInteger
_OperationalStateInstanceIndexAtt1_Object = MibTableColumn
operationalStateInstanceIndexAtt1 = _OperationalStateInstanceIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 1),
    _OperationalStateInstanceIndexAtt1_Type()
)
operationalStateInstanceIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalStateInstanceIndexAtt1.setStatus("mandatory")
_DeviceGroupIndexAtt2_1_Type = DmiInteger
_DeviceGroupIndexAtt2_1_Object = MibScalar
deviceGroupIndexAtt2_1 = _DeviceGroupIndexAtt2_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 2),
    _DeviceGroupIndexAtt2_1_Type()
)
deviceGroupIndexAtt2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceGroupIndexAtt2_1.setStatus("mandatory")


class _OperationalStatusAtt3_Type(Integer32):
    """Custom type operationalStatusAtt3 based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("notApplicable", 5),
          ("other", 1),
          ("unknown", 2))
    )


_OperationalStatusAtt3_Type.__name__ = "Integer32"
_OperationalStatusAtt3_Object = MibTableColumn
operationalStatusAtt3 = _OperationalStatusAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 3),
    _OperationalStatusAtt3_Type()
)
operationalStatusAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalStatusAtt3.setStatus("mandatory")


class _UsageStateAtt4_Type(Integer32):
    """Custom type usageStateAtt4 based on Integer32"""
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
        *(("active", 4),
          ("busy", 5),
          ("idle", 3),
          ("notApplicable", 6),
          ("other", 1),
          ("unknown", 2))
    )


_UsageStateAtt4_Type.__name__ = "Integer32"
_UsageStateAtt4_Object = MibTableColumn
usageStateAtt4 = _UsageStateAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 4),
    _UsageStateAtt4_Type()
)
usageStateAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStateAtt4.setStatus("mandatory")


class _AvailabilityStatusAtt5_Type(Integer32):
    """Custom type availabilityStatusAtt5 based on Integer32"""
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
        *(("degraded", 10),
          ("inTest", 5),
          ("installError", 12),
          ("notApplicable", 6),
          ("notInstalled", 11),
          ("offDuty", 9),
          ("offLine", 8),
          ("other", 1),
          ("powerOff", 7),
          ("powerSave", 13),
          ("running", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_AvailabilityStatusAtt5_Type.__name__ = "Integer32"
_AvailabilityStatusAtt5_Object = MibTableColumn
availabilityStatusAtt5 = _AvailabilityStatusAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 5),
    _AvailabilityStatusAtt5_Type()
)
availabilityStatusAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availabilityStatusAtt5.setStatus("mandatory")


class _AdministrativeStateAtt6_Type(Integer32):
    """Custom type administrativeStateAtt6 based on Integer32"""
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
        *(("locked", 3),
          ("notApplicable", 5),
          ("other", 1),
          ("shuttingDown", 6),
          ("unknown", 2),
          ("unlocked", 4))
    )


_AdministrativeStateAtt6_Type.__name__ = "Integer32"
_AdministrativeStateAtt6_Object = MibTableColumn
administrativeStateAtt6 = _AdministrativeStateAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 6),
    _AdministrativeStateAtt6_Type()
)
administrativeStateAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    administrativeStateAtt6.setStatus("mandatory")
_FatalErrorCountAtt7_Type = DmiCounter
_FatalErrorCountAtt7_Object = MibTableColumn
fatalErrorCountAtt7 = _FatalErrorCountAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 7),
    _FatalErrorCountAtt7_Type()
)
fatalErrorCountAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fatalErrorCountAtt7.setStatus("mandatory")
_MajorErrorCountAtt8_Type = DmiCounter
_MajorErrorCountAtt8_Object = MibTableColumn
majorErrorCountAtt8 = _MajorErrorCountAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 8),
    _MajorErrorCountAtt8_Type()
)
majorErrorCountAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorErrorCountAtt8.setStatus("mandatory")
_WarningErrorCountAtt9_Type = DmiCounter
_WarningErrorCountAtt9_Object = MibTableColumn
warningErrorCountAtt9 = _WarningErrorCountAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 9),
    _WarningErrorCountAtt9_Type()
)
warningErrorCountAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningErrorCountAtt9.setStatus("mandatory")


class _CurrentErrorStatusAtt10_Type(Integer32):
    """Custom type currentErrorStatusAtt10 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_CurrentErrorStatusAtt10_Type.__name__ = "Integer32"
_CurrentErrorStatusAtt10_Object = MibTableColumn
currentErrorStatusAtt10 = _CurrentErrorStatusAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 10),
    _CurrentErrorStatusAtt10_Type()
)
currentErrorStatusAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentErrorStatusAtt10.setStatus("mandatory")


class _DevicePredictedFailureStatusAtt11_Type(Integer32):
    """Custom type devicePredictedFailureStatusAtt11 based on Integer32"""
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
        *(("deviceFailurePredictedByTheDevice", 5),
          ("mediaFailurePredictedByTheDevice", 6),
          ("noFailurePredictedByTheDevice", 4),
          ("notSupportedByThisDevice", 3),
          ("other", 1),
          ("unknown", 2))
    )


_DevicePredictedFailureStatusAtt11_Type.__name__ = "Integer32"
_DevicePredictedFailureStatusAtt11_Object = MibTableColumn
devicePredictedFailureStatusAtt11 = _DevicePredictedFailureStatusAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 30, 1, 11),
    _DevicePredictedFailureStatusAtt11_Type()
)
devicePredictedFailureStatusAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePredictedFailureStatusAtt11.setStatus("mandatory")
_DMTFPhysicalMemoryArrayTable_Object = MibTable
dMTFPhysicalMemoryArrayTable = _DMTFPhysicalMemoryArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33)
)
if mibBuilder.loadTexts:
    dMTFPhysicalMemoryArrayTable.setStatus("mandatory")
_DMTFPhysicalMemoryArrayEntry_Object = MibTableRow
dMTFPhysicalMemoryArrayEntry = _DMTFPhysicalMemoryArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1)
)
dMTFPhysicalMemoryArrayEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "memoryArrayTableIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFPhysicalMemoryArrayEntry.setStatus("mandatory")


class _DMTFPhysicalMemoryArrayState_Type(Integer32):
    """Custom type dMTFPhysicalMemoryArrayState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFPhysicalMemoryArrayState_Type.__name__ = "Integer32"
_DMTFPhysicalMemoryArrayState_Object = MibTableColumn
dMTFPhysicalMemoryArrayState = _DMTFPhysicalMemoryArrayState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 0),
    _DMTFPhysicalMemoryArrayState_Type()
)
dMTFPhysicalMemoryArrayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFPhysicalMemoryArrayState.setStatus("mandatory")
_MemoryArrayTableIndexAtt1_Type = DmiInteger
_MemoryArrayTableIndexAtt1_Object = MibTableColumn
memoryArrayTableIndexAtt1 = _MemoryArrayTableIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 1),
    _MemoryArrayTableIndexAtt1_Type()
)
memoryArrayTableIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryArrayTableIndexAtt1.setStatus("mandatory")


class _MemoryArrayLocationAtt2_Type(Integer32):
    """Custom type memoryArrayLocationAtt2 based on Integer32"""
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
              16,
              160,
              161,
              162,
              163,
              164)
        )
    )
    namedValues = NamedValues(
        *(("eISAAddOnCard", 5),
          ("iSAAddOnCard", 4),
          ("mCAAddOnCard", 7),
          ("nuBus", 16),
          ("other", 1),
          ("pC98C20AddOnCard", 160),
          ("pC98C24AddOnCard", 161),
          ("pC98CardSlotAddOnCard", 164),
          ("pC98EAddOnCard", 162),
          ("pC98LocalBusAddOnCard", 163),
          ("pCIAddOnCard", 6),
          ("pCMCIAAddOnCard", 8),
          ("proprietaryAddOnCard", 9),
          ("systemBoardOrMotherboard", 3),
          ("unknown", 2))
    )


_MemoryArrayLocationAtt2_Type.__name__ = "Integer32"
_MemoryArrayLocationAtt2_Object = MibTableColumn
memoryArrayLocationAtt2 = _MemoryArrayLocationAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 2),
    _MemoryArrayLocationAtt2_Type()
)
memoryArrayLocationAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryArrayLocationAtt2.setStatus("mandatory")


class _MemoryArrayUseAtt3_Type(Integer32):
    """Custom type memoryArrayUseAtt3 based on Integer32"""
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
        *(("cacheMemory", 7),
          ("flashMemory", 5),
          ("nonVolatileRAM", 6),
          ("other", 1),
          ("systemMemory", 3),
          ("unknown", 2),
          ("videoMemory", 4))
    )


_MemoryArrayUseAtt3_Type.__name__ = "Integer32"
_MemoryArrayUseAtt3_Object = MibTableColumn
memoryArrayUseAtt3 = _MemoryArrayUseAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 3),
    _MemoryArrayUseAtt3_Type()
)
memoryArrayUseAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryArrayUseAtt3.setStatus("mandatory")
_MaximumMemoryCapacityAtt4_Type = DmiInteger
_MaximumMemoryCapacityAtt4_Object = MibTableColumn
maximumMemoryCapacityAtt4 = _MaximumMemoryCapacityAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 4),
    _MaximumMemoryCapacityAtt4_Type()
)
maximumMemoryCapacityAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumMemoryCapacityAtt4.setStatus("mandatory")
_NumberOfMemoryDeviceSocketsAtt5_Type = DmiInteger
_NumberOfMemoryDeviceSocketsAtt5_Object = MibTableColumn
numberOfMemoryDeviceSocketsAtt5 = _NumberOfMemoryDeviceSocketsAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 5),
    _NumberOfMemoryDeviceSocketsAtt5_Type()
)
numberOfMemoryDeviceSocketsAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfMemoryDeviceSocketsAtt5.setStatus("mandatory")
_NumberOfMemoryDeviceSocketsUsedAtt6_Type = DmiInteger
_NumberOfMemoryDeviceSocketsUsedAtt6_Object = MibTableColumn
numberOfMemoryDeviceSocketsUsedAtt6 = _NumberOfMemoryDeviceSocketsUsedAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 6),
    _NumberOfMemoryDeviceSocketsUsedAtt6_Type()
)
numberOfMemoryDeviceSocketsUsedAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfMemoryDeviceSocketsUsedAtt6.setStatus("mandatory")


class _MemoryErrorCorrectionAtt7_Type(Integer32):
    """Custom type memoryErrorCorrectionAtt7 based on Integer32"""
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
        *(("cRC", 7),
          ("multiBitECC", 6),
          ("none", 3),
          ("other", 1),
          ("parity", 4),
          ("singleBitECC", 5),
          ("unknown", 2))
    )


_MemoryErrorCorrectionAtt7_Type.__name__ = "Integer32"
_MemoryErrorCorrectionAtt7_Object = MibTableColumn
memoryErrorCorrectionAtt7 = _MemoryErrorCorrectionAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 7),
    _MemoryErrorCorrectionAtt7_Type()
)
memoryErrorCorrectionAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryErrorCorrectionAtt7.setStatus("mandatory")


class _ArrayErrorTypeAtt8_Type(Integer32):
    """Custom type arrayErrorTypeAtt8 based on Integer32"""
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
        *(("badRead", 4),
          ("cRCError", 11),
          ("checksumError", 10),
          ("correctedError", 13),
          ("correctedSingleBitError", 12),
          ("doubleBitError", 7),
          ("multiBitError", 8),
          ("nibbleError", 9),
          ("oK", 3),
          ("other", 1),
          ("parityError", 5),
          ("singleBitError", 6),
          ("uncorrectableError", 14),
          ("unknown", 2))
    )


_ArrayErrorTypeAtt8_Type.__name__ = "Integer32"
_ArrayErrorTypeAtt8_Object = MibTableColumn
arrayErrorTypeAtt8 = _ArrayErrorTypeAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 8),
    _ArrayErrorTypeAtt8_Type()
)
arrayErrorTypeAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayErrorTypeAtt8.setStatus("mandatory")


class _LastErrorUpdateAtt9_Type(Integer32):
    """Custom type lastErrorUpdateAtt9 based on Integer32"""
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
        *(("noUpdateSinceLastInstrumentationStart", 3),
          ("other", 1),
          ("unknown", 2),
          ("updatedDuringInstrumentationRunTime", 5),
          ("updatedFromInformationObtainedPriorToInstrumentati", 4))
    )


_LastErrorUpdateAtt9_Type.__name__ = "Integer32"
_LastErrorUpdateAtt9_Object = MibTableColumn
lastErrorUpdateAtt9 = _LastErrorUpdateAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 9),
    _LastErrorUpdateAtt9_Type()
)
lastErrorUpdateAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastErrorUpdateAtt9.setStatus("mandatory")


class _ErrorOperationAtt10_Type(Integer32):
    """Custom type errorOperationAtt10 based on Integer32"""
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
        *(("other", 1),
          ("partialWrite", 5),
          ("read", 3),
          ("unknown", 2),
          ("write", 4))
    )


_ErrorOperationAtt10_Type.__name__ = "Integer32"
_ErrorOperationAtt10_Object = MibTableColumn
errorOperationAtt10 = _ErrorOperationAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 10),
    _ErrorOperationAtt10_Type()
)
errorOperationAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorOperationAtt10.setStatus("mandatory")
_ErrorDataSizeAtt11_Type = DmiInteger
_ErrorDataSizeAtt11_Object = MibTableColumn
errorDataSizeAtt11 = _ErrorDataSizeAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 11),
    _ErrorDataSizeAtt11_Type()
)
errorDataSizeAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorDataSizeAtt11.setStatus("mandatory")
_ErrorDataAtt12_Type = DmiOctetstring
_ErrorDataAtt12_Object = MibTableColumn
errorDataAtt12 = _ErrorDataAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 12),
    _ErrorDataAtt12_Type()
)
errorDataAtt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorDataAtt12.setStatus("mandatory")
_VendorSyndromeAtt13_Type = DmiOctetstring
_VendorSyndromeAtt13_Object = MibTableColumn
vendorSyndromeAtt13 = _VendorSyndromeAtt13_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 13),
    _VendorSyndromeAtt13_Type()
)
vendorSyndromeAtt13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorSyndromeAtt13.setStatus("mandatory")
_ErrorAddressAtt14_Type = DmiInteger64
_ErrorAddressAtt14_Object = MibTableColumn
errorAddressAtt14 = _ErrorAddressAtt14_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 14),
    _ErrorAddressAtt14_Type()
)
errorAddressAtt14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorAddressAtt14.setStatus("mandatory")
_ErrorResolutionAtt15_Type = DmiInteger
_ErrorResolutionAtt15_Object = MibTableColumn
errorResolutionAtt15 = _ErrorResolutionAtt15_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 15),
    _ErrorResolutionAtt15_Type()
)
errorResolutionAtt15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorResolutionAtt15.setStatus("mandatory")
_FRUGroupIndexAtt16_Type = DmiInteger
_FRUGroupIndexAtt16_Object = MibTableColumn
fRUGroupIndexAtt16 = _FRUGroupIndexAtt16_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 16),
    _FRUGroupIndexAtt16_Type()
)
fRUGroupIndexAtt16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt16.setStatus("mandatory")
_OperationalGroupIndexAtt17_Type = DmiInteger
_OperationalGroupIndexAtt17_Object = MibTableColumn
operationalGroupIndexAtt17 = _OperationalGroupIndexAtt17_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 1, 17),
    _OperationalGroupIndexAtt17_Type()
)
operationalGroupIndexAtt17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt17.setStatus("mandatory")


class _DMTFPhysicalMemoryArrayEvSys_Type(Integer32):
    """Custom type dMTFPhysicalMemoryArrayEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFPhysicalMemoryArrayEvSys_Type.__name__ = "Integer32"
_DMTFPhysicalMemoryArrayEvSys_Object = MibScalar
dMTFPhysicalMemoryArrayEvSys = _DMTFPhysicalMemoryArrayEvSys_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 6),
    _DMTFPhysicalMemoryArrayEvSys_Type()
)
dMTFPhysicalMemoryArrayEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFPhysicalMemoryArrayEvSys.setStatus("mandatory")


class _DMTFPhysicalMemoryArrayEvSub_Type(Integer32):
    """Custom type dMTFPhysicalMemoryArrayEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFPhysicalMemoryArrayEvSub_Type.__name__ = "Integer32"
_DMTFPhysicalMemoryArrayEvSub_Object = MibScalar
dMTFPhysicalMemoryArrayEvSub = _DMTFPhysicalMemoryArrayEvSub_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 7),
    _DMTFPhysicalMemoryArrayEvSub_Type()
)
dMTFPhysicalMemoryArrayEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFPhysicalMemoryArrayEvSub.setStatus("mandatory")
_DMTFMemoryArrayMappedAddressesTable_Object = MibTable
dMTFMemoryArrayMappedAddressesTable = _DMTFMemoryArrayMappedAddressesTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34)
)
if mibBuilder.loadTexts:
    dMTFMemoryArrayMappedAddressesTable.setStatus("mandatory")
_DMTFMemoryArrayMappedAddressesEntry_Object = MibTableRow
dMTFMemoryArrayMappedAddressesEntry = _DMTFMemoryArrayMappedAddressesEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34, 1)
)
dMTFMemoryArrayMappedAddressesEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "memoryArrayMappedAddressesTableIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFMemoryArrayMappedAddressesEntry.setStatus("mandatory")


class _DMTFMemoryArrayMappedAddressesState_Type(Integer32):
    """Custom type dMTFMemoryArrayMappedAddressesState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFMemoryArrayMappedAddressesState_Type.__name__ = "Integer32"
_DMTFMemoryArrayMappedAddressesState_Object = MibTableColumn
dMTFMemoryArrayMappedAddressesState = _DMTFMemoryArrayMappedAddressesState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34, 1, 0),
    _DMTFMemoryArrayMappedAddressesState_Type()
)
dMTFMemoryArrayMappedAddressesState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFMemoryArrayMappedAddressesState.setStatus("mandatory")
_MemoryArrayMappedAddressesTableIndexAtt1_Type = DmiInteger
_MemoryArrayMappedAddressesTableIndexAtt1_Object = MibTableColumn
memoryArrayMappedAddressesTableIndexAtt1 = _MemoryArrayMappedAddressesTableIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34, 1, 1),
    _MemoryArrayMappedAddressesTableIndexAtt1_Type()
)
memoryArrayMappedAddressesTableIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryArrayMappedAddressesTableIndexAtt1.setStatus("mandatory")
_MemoryArrayIndexAtt2_Type = DmiInteger
_MemoryArrayIndexAtt2_Object = MibTableColumn
memoryArrayIndexAtt2 = _MemoryArrayIndexAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34, 1, 2),
    _MemoryArrayIndexAtt2_Type()
)
memoryArrayIndexAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryArrayIndexAtt2.setStatus("mandatory")
_MappedRangeStartingAddressAtt3_Type = DmiInteger
_MappedRangeStartingAddressAtt3_Object = MibTableColumn
mappedRangeStartingAddressAtt3 = _MappedRangeStartingAddressAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34, 1, 3),
    _MappedRangeStartingAddressAtt3_Type()
)
mappedRangeStartingAddressAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappedRangeStartingAddressAtt3.setStatus("mandatory")
_MappedRangeEndingAddressAtt4_Type = DmiInteger
_MappedRangeEndingAddressAtt4_Object = MibTableColumn
mappedRangeEndingAddressAtt4 = _MappedRangeEndingAddressAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34, 1, 4),
    _MappedRangeEndingAddressAtt4_Type()
)
mappedRangeEndingAddressAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappedRangeEndingAddressAtt4.setStatus("mandatory")
_PartitionIDAtt5_Type = DmiInteger
_PartitionIDAtt5_Object = MibTableColumn
partitionIDAtt5 = _PartitionIDAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34, 1, 5),
    _PartitionIDAtt5_Type()
)
partitionIDAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionIDAtt5.setStatus("mandatory")
_PartitionWidthAtt6_Type = DmiInteger
_PartitionWidthAtt6_Object = MibTableColumn
partitionWidthAtt6 = _PartitionWidthAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34, 1, 6),
    _PartitionWidthAtt6_Type()
)
partitionWidthAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionWidthAtt6.setStatus("mandatory")
_OperationalGroupIndexAtt7_Type = DmiInteger
_OperationalGroupIndexAtt7_Object = MibTableColumn
operationalGroupIndexAtt7 = _OperationalGroupIndexAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 34, 1, 7),
    _OperationalGroupIndexAtt7_Type()
)
operationalGroupIndexAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt7.setStatus("mandatory")
_DMTFMemoryDeviceTable_Object = MibTable
dMTFMemoryDeviceTable = _DMTFMemoryDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35)
)
if mibBuilder.loadTexts:
    dMTFMemoryDeviceTable.setStatus("mandatory")
_DMTFMemoryDeviceEntry_Object = MibTableRow
dMTFMemoryDeviceEntry = _DMTFMemoryDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1)
)
dMTFMemoryDeviceEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "memoryDeviceTableIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFMemoryDeviceEntry.setStatus("mandatory")


class _DMTFMemoryDeviceState_Type(Integer32):
    """Custom type dMTFMemoryDeviceState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFMemoryDeviceState_Type.__name__ = "Integer32"
_DMTFMemoryDeviceState_Object = MibTableColumn
dMTFMemoryDeviceState = _DMTFMemoryDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 0),
    _DMTFMemoryDeviceState_Type()
)
dMTFMemoryDeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFMemoryDeviceState.setStatus("mandatory")
_MemoryDeviceTableIndexAtt1_Type = DmiInteger
_MemoryDeviceTableIndexAtt1_Object = MibTableColumn
memoryDeviceTableIndexAtt1 = _MemoryDeviceTableIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 1),
    _MemoryDeviceTableIndexAtt1_Type()
)
memoryDeviceTableIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceTableIndexAtt1.setStatus("mandatory")
_MemoryArrayIndexAtt2_1_Type = DmiInteger
_MemoryArrayIndexAtt2_1_Object = MibScalar
memoryArrayIndexAtt2_1 = _MemoryArrayIndexAtt2_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 2),
    _MemoryArrayIndexAtt2_1_Type()
)
memoryArrayIndexAtt2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryArrayIndexAtt2_1.setStatus("mandatory")
_DeviceLocatorAtt3_Type = DmiDisplaystring
_DeviceLocatorAtt3_Object = MibTableColumn
deviceLocatorAtt3 = _DeviceLocatorAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 3),
    _DeviceLocatorAtt3_Type()
)
deviceLocatorAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLocatorAtt3.setStatus("mandatory")
_BankLocatorAtt4_Type = DmiDisplaystring
_BankLocatorAtt4_Object = MibTableColumn
bankLocatorAtt4 = _BankLocatorAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 4),
    _BankLocatorAtt4_Type()
)
bankLocatorAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bankLocatorAtt4.setStatus("mandatory")
_SizeAtt5_Type = DmiInteger
_SizeAtt5_Object = MibTableColumn
sizeAtt5 = _SizeAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 5),
    _SizeAtt5_Type()
)
sizeAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeAtt5.setStatus("mandatory")


class _FormFactorAtt6_Type(Integer32):
    """Custom type formFactorAtt6 based on Integer32"""
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
        *(("chip", 5),
          ("dIMM", 9),
          ("dIP", 6),
          ("other", 1),
          ("proprietaryCard", 8),
          ("rowOfChips", 11),
          ("sIMM", 3),
          ("sIP", 4),
          ("tSOP", 10),
          ("unknown", 2),
          ("zIP", 7))
    )


_FormFactorAtt6_Type.__name__ = "Integer32"
_FormFactorAtt6_Object = MibTableColumn
formFactorAtt6 = _FormFactorAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 6),
    _FormFactorAtt6_Type()
)
formFactorAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    formFactorAtt6.setStatus("mandatory")
_TotalWidthAtt7_Type = DmiInteger
_TotalWidthAtt7_Object = MibTableColumn
totalWidthAtt7 = _TotalWidthAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 7),
    _TotalWidthAtt7_Type()
)
totalWidthAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalWidthAtt7.setStatus("mandatory")
_DataWidthAtt8_Type = DmiInteger
_DataWidthAtt8_Object = MibTableColumn
dataWidthAtt8 = _DataWidthAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 8),
    _DataWidthAtt8_Type()
)
dataWidthAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataWidthAtt8.setStatus("mandatory")


class _MemoryTypeAtt9_Type(Integer32):
    """Custom type memoryTypeAtt9 based on Integer32"""
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
        *(("dRAM", 3),
          ("eDRAM", 4),
          ("eEPROM", 10),
          ("ePROM", 12),
          ("fEPROM", 11),
          ("fLASH", 9),
          ("other", 1),
          ("rAM", 7),
          ("rOM", 8),
          ("sRAM", 6),
          ("unknown", 2),
          ("vRAM", 5))
    )


_MemoryTypeAtt9_Type.__name__ = "Integer32"
_MemoryTypeAtt9_Object = MibTableColumn
memoryTypeAtt9 = _MemoryTypeAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 9),
    _MemoryTypeAtt9_Type()
)
memoryTypeAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTypeAtt9.setStatus("mandatory")


class _TypeDetailAtt10_Type(Integer32):
    """Custom type typeDetailAtt10 based on Integer32"""
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
        *(("cMOS", 8),
          ("cacheDRAM", 11),
          ("eDO", 9),
          ("fastPaged", 3),
          ("nonVolatile", 12),
          ("other", 1),
          ("pseudoStatic", 5),
          ("rAMBUS", 6),
          ("staticColumn", 4),
          ("synchronous", 7),
          ("unknown", 2),
          ("windowDRAM", 10))
    )


_TypeDetailAtt10_Type.__name__ = "Integer32"
_TypeDetailAtt10_Object = MibTableColumn
typeDetailAtt10 = _TypeDetailAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 10),
    _TypeDetailAtt10_Type()
)
typeDetailAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    typeDetailAtt10.setStatus("mandatory")
_DeviceSetAtt11_Type = DmiInteger
_DeviceSetAtt11_Object = MibTableColumn
deviceSetAtt11 = _DeviceSetAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 11),
    _DeviceSetAtt11_Type()
)
deviceSetAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSetAtt11.setStatus("mandatory")


class _DeviceErrorTypeAtt12_Type(Integer32):
    """Custom type deviceErrorTypeAtt12 based on Integer32"""
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
        *(("badRead", 4),
          ("cRCError", 11),
          ("checksumError", 10),
          ("correctedError", 13),
          ("correctedSingleBitError", 12),
          ("doubleBitError", 7),
          ("multiBitError", 8),
          ("nibbleError", 9),
          ("oK", 3),
          ("other", 1),
          ("parityError", 5),
          ("singleBitError", 6),
          ("uncorrectableError", 14),
          ("unknown", 2))
    )


_DeviceErrorTypeAtt12_Type.__name__ = "Integer32"
_DeviceErrorTypeAtt12_Object = MibTableColumn
deviceErrorTypeAtt12 = _DeviceErrorTypeAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 12),
    _DeviceErrorTypeAtt12_Type()
)
deviceErrorTypeAtt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceErrorTypeAtt12.setStatus("mandatory")


class _ErrorGranularityAtt13_Type(Integer32):
    """Custom type errorGranularityAtt13 based on Integer32"""
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
        *(("deviceLevel", 3),
          ("memoryPartitionLevel", 4),
          ("other", 1),
          ("unknown", 2))
    )


_ErrorGranularityAtt13_Type.__name__ = "Integer32"
_ErrorGranularityAtt13_Object = MibTableColumn
errorGranularityAtt13 = _ErrorGranularityAtt13_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 13),
    _ErrorGranularityAtt13_Type()
)
errorGranularityAtt13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorGranularityAtt13.setStatus("mandatory")


class _LastErrorUpdateAtt14_Type(Integer32):
    """Custom type lastErrorUpdateAtt14 based on Integer32"""
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
        *(("noUpdateSinceLastInstrumentationStart", 3),
          ("other", 1),
          ("unknown", 2),
          ("updatedDuringInstrumentationRunTime", 5),
          ("updatedFromInformationObtainedPriorToInstrumentati", 4))
    )


_LastErrorUpdateAtt14_Type.__name__ = "Integer32"
_LastErrorUpdateAtt14_Object = MibTableColumn
lastErrorUpdateAtt14 = _LastErrorUpdateAtt14_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 14),
    _LastErrorUpdateAtt14_Type()
)
lastErrorUpdateAtt14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastErrorUpdateAtt14.setStatus("mandatory")


class _ErrorOperationAtt15_Type(Integer32):
    """Custom type errorOperationAtt15 based on Integer32"""
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
        *(("other", 1),
          ("partialWrite", 5),
          ("read", 3),
          ("unknown", 2),
          ("write", 4))
    )


_ErrorOperationAtt15_Type.__name__ = "Integer32"
_ErrorOperationAtt15_Object = MibTableColumn
errorOperationAtt15 = _ErrorOperationAtt15_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 15),
    _ErrorOperationAtt15_Type()
)
errorOperationAtt15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorOperationAtt15.setStatus("mandatory")
_ErrorDataSizeAtt16_Type = DmiInteger
_ErrorDataSizeAtt16_Object = MibTableColumn
errorDataSizeAtt16 = _ErrorDataSizeAtt16_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 16),
    _ErrorDataSizeAtt16_Type()
)
errorDataSizeAtt16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorDataSizeAtt16.setStatus("mandatory")
_ErrorDataAtt17_Type = DmiOctetstring
_ErrorDataAtt17_Object = MibTableColumn
errorDataAtt17 = _ErrorDataAtt17_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 17),
    _ErrorDataAtt17_Type()
)
errorDataAtt17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorDataAtt17.setStatus("mandatory")
_VendorSyndromeAtt18_Type = DmiOctetstring
_VendorSyndromeAtt18_Object = MibTableColumn
vendorSyndromeAtt18 = _VendorSyndromeAtt18_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 18),
    _VendorSyndromeAtt18_Type()
)
vendorSyndromeAtt18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorSyndromeAtt18.setStatus("mandatory")
_DeviceErrorAddressAtt19_Type = DmiInteger
_DeviceErrorAddressAtt19_Object = MibTableColumn
deviceErrorAddressAtt19 = _DeviceErrorAddressAtt19_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 19),
    _DeviceErrorAddressAtt19_Type()
)
deviceErrorAddressAtt19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceErrorAddressAtt19.setStatus("mandatory")
_ArrayErrorAddressAtt20_Type = DmiInteger
_ArrayErrorAddressAtt20_Object = MibTableColumn
arrayErrorAddressAtt20 = _ArrayErrorAddressAtt20_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 20),
    _ArrayErrorAddressAtt20_Type()
)
arrayErrorAddressAtt20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayErrorAddressAtt20.setStatus("mandatory")
_ErrorResolutionAtt21_Type = DmiInteger
_ErrorResolutionAtt21_Object = MibTableColumn
errorResolutionAtt21 = _ErrorResolutionAtt21_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 21),
    _ErrorResolutionAtt21_Type()
)
errorResolutionAtt21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorResolutionAtt21.setStatus("mandatory")
_FRUGroupIndexAtt22_Type = DmiInteger
_FRUGroupIndexAtt22_Object = MibTableColumn
fRUGroupIndexAtt22 = _FRUGroupIndexAtt22_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 22),
    _FRUGroupIndexAtt22_Type()
)
fRUGroupIndexAtt22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt22.setStatus("mandatory")
_OperationalGroupIndexAtt23_Type = DmiInteger
_OperationalGroupIndexAtt23_Object = MibTableColumn
operationalGroupIndexAtt23 = _OperationalGroupIndexAtt23_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 35, 1, 23),
    _OperationalGroupIndexAtt23_Type()
)
operationalGroupIndexAtt23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt23.setStatus("mandatory")
_DMTFMemoryDeviceMappedAddressesTable_Object = MibTable
dMTFMemoryDeviceMappedAddressesTable = _DMTFMemoryDeviceMappedAddressesTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36)
)
if mibBuilder.loadTexts:
    dMTFMemoryDeviceMappedAddressesTable.setStatus("mandatory")
_DMTFMemoryDeviceMappedAddressesEntry_Object = MibTableRow
dMTFMemoryDeviceMappedAddressesEntry = _DMTFMemoryDeviceMappedAddressesEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1)
)
dMTFMemoryDeviceMappedAddressesEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "memoryDeviceMappedAddressesTableIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFMemoryDeviceMappedAddressesEntry.setStatus("mandatory")


class _DMTFMemoryDeviceMappedAddressesState_Type(Integer32):
    """Custom type dMTFMemoryDeviceMappedAddressesState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFMemoryDeviceMappedAddressesState_Type.__name__ = "Integer32"
_DMTFMemoryDeviceMappedAddressesState_Object = MibTableColumn
dMTFMemoryDeviceMappedAddressesState = _DMTFMemoryDeviceMappedAddressesState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1, 0),
    _DMTFMemoryDeviceMappedAddressesState_Type()
)
dMTFMemoryDeviceMappedAddressesState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFMemoryDeviceMappedAddressesState.setStatus("mandatory")
_MemoryDeviceMappedAddressesTableIndexAtt1_Type = DmiInteger
_MemoryDeviceMappedAddressesTableIndexAtt1_Object = MibTableColumn
memoryDeviceMappedAddressesTableIndexAtt1 = _MemoryDeviceMappedAddressesTableIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1, 1),
    _MemoryDeviceMappedAddressesTableIndexAtt1_Type()
)
memoryDeviceMappedAddressesTableIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressesTableIndexAtt1.setStatus("mandatory")
_MemoryDeviceSetIDAtt2_Type = DmiInteger
_MemoryDeviceSetIDAtt2_Object = MibTableColumn
memoryDeviceSetIDAtt2 = _MemoryDeviceSetIDAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1, 2),
    _MemoryDeviceSetIDAtt2_Type()
)
memoryDeviceSetIDAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSetIDAtt2.setStatus("mandatory")
_PartitionAtt3_Type = DmiInteger
_PartitionAtt3_Object = MibTableColumn
partitionAtt3 = _PartitionAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1, 3),
    _PartitionAtt3_Type()
)
partitionAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionAtt3.setStatus("mandatory")
_MappedRangeStartingAddressAtt4_Type = DmiInteger
_MappedRangeStartingAddressAtt4_Object = MibTableColumn
mappedRangeStartingAddressAtt4 = _MappedRangeStartingAddressAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1, 4),
    _MappedRangeStartingAddressAtt4_Type()
)
mappedRangeStartingAddressAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappedRangeStartingAddressAtt4.setStatus("mandatory")
_MappedRangeEndingAddressAtt5_Type = DmiInteger
_MappedRangeEndingAddressAtt5_Object = MibTableColumn
mappedRangeEndingAddressAtt5 = _MappedRangeEndingAddressAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1, 5),
    _MappedRangeEndingAddressAtt5_Type()
)
mappedRangeEndingAddressAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappedRangeEndingAddressAtt5.setStatus("mandatory")
_PartitionRowPositionAtt6_Type = DmiInteger
_PartitionRowPositionAtt6_Object = MibTableColumn
partitionRowPositionAtt6 = _PartitionRowPositionAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1, 6),
    _PartitionRowPositionAtt6_Type()
)
partitionRowPositionAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionRowPositionAtt6.setStatus("mandatory")
_InterleavePositionAtt7_Type = DmiInteger
_InterleavePositionAtt7_Object = MibTableColumn
interleavePositionAtt7 = _InterleavePositionAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1, 7),
    _InterleavePositionAtt7_Type()
)
interleavePositionAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interleavePositionAtt7.setStatus("mandatory")
_DataDepthAtt8_Type = DmiInteger
_DataDepthAtt8_Object = MibTableColumn
dataDepthAtt8 = _DataDepthAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 36, 1, 8),
    _DataDepthAtt8_Type()
)
dataDepthAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataDepthAtt8.setStatus("mandatory")
_DMTFSystemResources2Table_Object = MibTable
dMTFSystemResources2Table = _DMTFSystemResources2Table_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37)
)
if mibBuilder.loadTexts:
    dMTFSystemResources2Table.setStatus("mandatory")
_DMTFSystemResources2Entry_Object = MibTableRow
dMTFSystemResources2Entry = _DMTFSystemResources2Entry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1)
)
dMTFSystemResources2Entry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "systemResourcesIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSystemResources2Entry.setStatus("mandatory")


class _DMTFSystemResources2State_Type(Integer32):
    """Custom type dMTFSystemResources2State based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSystemResources2State_Type.__name__ = "Integer32"
_DMTFSystemResources2State_Object = MibTableColumn
dMTFSystemResources2State = _DMTFSystemResources2State_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 0),
    _DMTFSystemResources2State_Type()
)
dMTFSystemResources2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSystemResources2State.setStatus("mandatory")
_SystemResourcesIndexAtt1_Type = DmiInteger
_SystemResourcesIndexAtt1_Object = MibTableColumn
systemResourcesIndexAtt1 = _SystemResourcesIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 1),
    _SystemResourcesIndexAtt1_Type()
)
systemResourcesIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourcesIndexAtt1.setStatus("mandatory")
_ResourceUserAtt2_Type = DmiInteger
_ResourceUserAtt2_Object = MibTableColumn
resourceUserAtt2 = _ResourceUserAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 2),
    _ResourceUserAtt2_Type()
)
resourceUserAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceUserAtt2.setStatus("mandatory")
_ResourceSetAtt3_Type = DmiInteger
_ResourceSetAtt3_Object = MibTableColumn
resourceSetAtt3 = _ResourceSetAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 3),
    _ResourceSetAtt3_Type()
)
resourceSetAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceSetAtt3.setStatus("mandatory")


class _ResourceAssignmentAtt4_Type(Integer32):
    """Custom type resourceAssignmentAtt4 based on Integer32"""
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
        *(("allocated", 3),
          ("assignable", 4),
          ("other", 1),
          ("temporaryAssignment", 5),
          ("unknown", 2))
    )


_ResourceAssignmentAtt4_Type.__name__ = "Integer32"
_ResourceAssignmentAtt4_Object = MibTableColumn
resourceAssignmentAtt4 = _ResourceAssignmentAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 4),
    _ResourceAssignmentAtt4_Type()
)
resourceAssignmentAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAssignmentAtt4.setStatus("mandatory")


class _ResourceTypeAtt5_Type(Integer32):
    """Custom type resourceTypeAtt5 based on Integer32"""
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
        *(("dMA", 6),
          ("iO", 4),
          ("iRQ", 5),
          ("memory", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ResourceTypeAtt5_Type.__name__ = "Integer32"
_ResourceTypeAtt5_Object = MibTableColumn
resourceTypeAtt5 = _ResourceTypeAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 5),
    _ResourceTypeAtt5_Type()
)
resourceTypeAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceTypeAtt5.setStatus("mandatory")
_ResourceNumberAtt6_Type = DmiInteger
_ResourceNumberAtt6_Object = MibTableColumn
resourceNumberAtt6 = _ResourceNumberAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 6),
    _ResourceNumberAtt6_Type()
)
resourceNumberAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNumberAtt6.setStatus("mandatory")
_ResourceInfoIDAtt7_Type = DmiInteger
_ResourceInfoIDAtt7_Object = MibTableColumn
resourceInfoIDAtt7 = _ResourceInfoIDAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 7),
    _ResourceInfoIDAtt7_Type()
)
resourceInfoIDAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceInfoIDAtt7.setStatus("mandatory")
_StartAddressAtt8_Type = DmiInteger64
_StartAddressAtt8_Object = MibTableColumn
startAddressAtt8 = _StartAddressAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 8),
    _StartAddressAtt8_Type()
)
startAddressAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startAddressAtt8.setStatus("mandatory")
_EndAddressAtt9_Type = DmiInteger64
_EndAddressAtt9_Object = MibTableColumn
endAddressAtt9 = _EndAddressAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 9),
    _EndAddressAtt9_Type()
)
endAddressAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endAddressAtt9.setStatus("mandatory")
_ResourceSizeAtt10_Type = DmiInteger
_ResourceSizeAtt10_Object = MibTableColumn
resourceSizeAtt10 = _ResourceSizeAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 10),
    _ResourceSizeAtt10_Type()
)
resourceSizeAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceSizeAtt10.setStatus("mandatory")
_BaseAlignmentAtt11_Type = DmiInteger
_BaseAlignmentAtt11_Object = MibTableColumn
baseAlignmentAtt11 = _BaseAlignmentAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 11),
    _BaseAlignmentAtt11_Type()
)
baseAlignmentAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseAlignmentAtt11.setStatus("mandatory")


class _ShareableAtt12_Type(Integer32):
    """Custom type shareableAtt12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_ShareableAtt12_Type.__name__ = "Integer32"
_ShareableAtt12_Object = MibTableColumn
shareableAtt12 = _ShareableAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 12),
    _ShareableAtt12_Type()
)
shareableAtt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shareableAtt12.setStatus("mandatory")


class _SharedAtt13_Type(Integer32):
    """Custom type sharedAtt13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_SharedAtt13_Type.__name__ = "Integer32"
_SharedAtt13_Object = MibTableColumn
sharedAtt13 = _SharedAtt13_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 37, 1, 13),
    _SharedAtt13_Type()
)
sharedAtt13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedAtt13.setStatus("mandatory")
_DMTFSystemResourceDeviceInfoTable_Object = MibTable
dMTFSystemResourceDeviceInfoTable = _DMTFSystemResourceDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38)
)
if mibBuilder.loadTexts:
    dMTFSystemResourceDeviceInfoTable.setStatus("mandatory")
_DMTFSystemResourceDeviceInfoEntry_Object = MibTableRow
dMTFSystemResourceDeviceInfoEntry = _DMTFSystemResourceDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1)
)
dMTFSystemResourceDeviceInfoEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "resourceUserAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSystemResourceDeviceInfoEntry.setStatus("mandatory")


class _DMTFSystemResourceDeviceInfoState_Type(Integer32):
    """Custom type dMTFSystemResourceDeviceInfoState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSystemResourceDeviceInfoState_Type.__name__ = "Integer32"
_DMTFSystemResourceDeviceInfoState_Object = MibTableColumn
dMTFSystemResourceDeviceInfoState = _DMTFSystemResourceDeviceInfoState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 0),
    _DMTFSystemResourceDeviceInfoState_Type()
)
dMTFSystemResourceDeviceInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSystemResourceDeviceInfoState.setStatus("mandatory")
_ResourceUserAtt1_Type = DmiInteger
_ResourceUserAtt1_Object = MibTableColumn
resourceUserAtt1 = _ResourceUserAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 1),
    _ResourceUserAtt1_Type()
)
resourceUserAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceUserAtt1.setStatus("mandatory")
_DeviceIDAtt2_Type = DmiInteger
_DeviceIDAtt2_Object = MibTableColumn
deviceIDAtt2 = _DeviceIDAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 2),
    _DeviceIDAtt2_Type()
)
deviceIDAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIDAtt2.setStatus("mandatory")
_DeviceSerialNumberAtt3_Type = DmiInteger
_DeviceSerialNumberAtt3_Object = MibTableColumn
deviceSerialNumberAtt3 = _DeviceSerialNumberAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 3),
    _DeviceSerialNumberAtt3_Type()
)
deviceSerialNumberAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumberAtt3.setStatus("mandatory")
_LogicalDeviceIDClassCodeAtt4_Type = DmiInteger
_LogicalDeviceIDClassCodeAtt4_Object = MibTableColumn
logicalDeviceIDClassCodeAtt4 = _LogicalDeviceIDClassCodeAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 4),
    _LogicalDeviceIDClassCodeAtt4_Type()
)
logicalDeviceIDClassCodeAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceIDClassCodeAtt4.setStatus("mandatory")
_DeviceFlagsAtt5_Type = DmiInteger
_DeviceFlagsAtt5_Object = MibTableColumn
deviceFlagsAtt5 = _DeviceFlagsAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 5),
    _DeviceFlagsAtt5_Type()
)
deviceFlagsAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFlagsAtt5.setStatus("mandatory")
_DeviceNumberAtt6_Type = DmiInteger
_DeviceNumberAtt6_Object = MibTableColumn
deviceNumberAtt6 = _DeviceNumberAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 6),
    _DeviceNumberAtt6_Type()
)
deviceNumberAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceNumberAtt6.setStatus("mandatory")
_FunctionNumberAtt7_Type = DmiInteger
_FunctionNumberAtt7_Object = MibTableColumn
functionNumberAtt7 = _FunctionNumberAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 7),
    _FunctionNumberAtt7_Type()
)
functionNumberAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    functionNumberAtt7.setStatus("mandatory")
_BusTypeAtt8_Type = DmiInteger
_BusTypeAtt8_Object = MibTableColumn
busTypeAtt8 = _BusTypeAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 8),
    _BusTypeAtt8_Type()
)
busTypeAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busTypeAtt8.setStatus("mandatory")
_CMReservedAtt9_Type = DmiInteger
_CMReservedAtt9_Object = MibTableColumn
cMReservedAtt9 = _CMReservedAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 38, 1, 9),
    _CMReservedAtt9_Type()
)
cMReservedAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMReservedAtt9.setStatus("mandatory")
_DMTFSystemResourceMemoryInfoTable_Object = MibTable
dMTFSystemResourceMemoryInfoTable = _DMTFSystemResourceMemoryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39)
)
if mibBuilder.loadTexts:
    dMTFSystemResourceMemoryInfoTable.setStatus("mandatory")
_DMTFSystemResourceMemoryInfoEntry_Object = MibTableRow
dMTFSystemResourceMemoryInfoEntry = _DMTFSystemResourceMemoryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39, 1)
)
dMTFSystemResourceMemoryInfoEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "systemResourceMemoryInfoIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSystemResourceMemoryInfoEntry.setStatus("mandatory")


class _DMTFSystemResourceMemoryInfoState_Type(Integer32):
    """Custom type dMTFSystemResourceMemoryInfoState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSystemResourceMemoryInfoState_Type.__name__ = "Integer32"
_DMTFSystemResourceMemoryInfoState_Object = MibTableColumn
dMTFSystemResourceMemoryInfoState = _DMTFSystemResourceMemoryInfoState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39, 1, 0),
    _DMTFSystemResourceMemoryInfoState_Type()
)
dMTFSystemResourceMemoryInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSystemResourceMemoryInfoState.setStatus("mandatory")
_SystemResourceMemoryInfoIndexAtt1_Type = DmiInteger
_SystemResourceMemoryInfoIndexAtt1_Object = MibTableColumn
systemResourceMemoryInfoIndexAtt1 = _SystemResourceMemoryInfoIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39, 1, 1),
    _SystemResourceMemoryInfoIndexAtt1_Type()
)
systemResourceMemoryInfoIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryInfoIndexAtt1.setStatus("mandatory")


class _ISAPCMCIARangeDescriptorAtt2_Type(Integer32):
    """Custom type iSAPCMCIARangeDescriptorAtt2 based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("x16BitMemoryOnly", 4),
          ("x32BitMemoryOnly", 6),
          ("x8And16BitMemorySupported", 5),
          ("x8BitMemoryOnly", 3))
    )


_ISAPCMCIARangeDescriptorAtt2_Type.__name__ = "Integer32"
_ISAPCMCIARangeDescriptorAtt2_Object = MibTableColumn
iSAPCMCIARangeDescriptorAtt2 = _ISAPCMCIARangeDescriptorAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39, 1, 2),
    _ISAPCMCIARangeDescriptorAtt2_Type()
)
iSAPCMCIARangeDescriptorAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSAPCMCIARangeDescriptorAtt2.setStatus("mandatory")


class _EISARangeDescriptorAtt3_Type(Integer32):
    """Custom type eISARangeDescriptorAtt3 based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("x16BitMemoryOnly", 4),
          ("x32BitMemoryOnly", 6),
          ("x8And16BitMemorySupported", 5),
          ("x8BitMemoryOnly", 3))
    )


_EISARangeDescriptorAtt3_Type.__name__ = "Integer32"
_EISARangeDescriptorAtt3_Object = MibTableColumn
eISARangeDescriptorAtt3 = _EISARangeDescriptorAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39, 1, 3),
    _EISARangeDescriptorAtt3_Type()
)
eISARangeDescriptorAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eISARangeDescriptorAtt3.setStatus("mandatory")


class _DecodeSupportAtt4_Type(Integer32):
    """Custom type decodeSupportAtt4 based on Integer32"""
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
        *(("decodeSupportsHighAddress", 3),
          ("decodeSupportsRangeLength", 4),
          ("other", 1),
          ("unknown", 2))
    )


_DecodeSupportAtt4_Type.__name__ = "Integer32"
_DecodeSupportAtt4_Object = MibTableColumn
decodeSupportAtt4 = _DecodeSupportAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39, 1, 4),
    _DecodeSupportAtt4_Type()
)
decodeSupportAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decodeSupportAtt4.setStatus("mandatory")


class _CacheableAtt5_Type(Integer32):
    """Custom type cacheableAtt5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_CacheableAtt5_Type.__name__ = "Integer32"
_CacheableAtt5_Object = MibTableColumn
cacheableAtt5 = _CacheableAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39, 1, 5),
    _CacheableAtt5_Type()
)
cacheableAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheableAtt5.setStatus("mandatory")


class _CacheTypeAtt6_Type(Integer32):
    """Custom type cacheTypeAtt6 based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("writeBack-1", 3),
          ("writeThrough-1", 4))
    )


_CacheTypeAtt6_Type.__name__ = "Integer32"
_CacheTypeAtt6_Object = MibTableColumn
cacheTypeAtt6 = _CacheTypeAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39, 1, 6),
    _CacheTypeAtt6_Type()
)
cacheTypeAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTypeAtt6.setStatus("mandatory")


class _ReadWriteAtt7_Type(Integer32):
    """Custom type readWriteAtt7 based on Integer32"""
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
        *(("other", 1),
          ("rAMReadwrite", 4),
          ("rOMReadOnly", 3),
          ("unknown", 2))
    )


_ReadWriteAtt7_Type.__name__ = "Integer32"
_ReadWriteAtt7_Object = MibTableColumn
readWriteAtt7 = _ReadWriteAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 39, 1, 7),
    _ReadWriteAtt7_Type()
)
readWriteAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readWriteAtt7.setStatus("mandatory")
_DMTFSystemResourceIOInfoTable_Object = MibTable
dMTFSystemResourceIOInfoTable = _DMTFSystemResourceIOInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 40)
)
if mibBuilder.loadTexts:
    dMTFSystemResourceIOInfoTable.setStatus("mandatory")
_DMTFSystemResourceIOInfoEntry_Object = MibTableRow
dMTFSystemResourceIOInfoEntry = _DMTFSystemResourceIOInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 40, 1)
)
dMTFSystemResourceIOInfoEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "systemResourceIOInfoIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSystemResourceIOInfoEntry.setStatus("mandatory")


class _DMTFSystemResourceIOInfoState_Type(Integer32):
    """Custom type dMTFSystemResourceIOInfoState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSystemResourceIOInfoState_Type.__name__ = "Integer32"
_DMTFSystemResourceIOInfoState_Object = MibTableColumn
dMTFSystemResourceIOInfoState = _DMTFSystemResourceIOInfoState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 40, 1, 0),
    _DMTFSystemResourceIOInfoState_Type()
)
dMTFSystemResourceIOInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSystemResourceIOInfoState.setStatus("mandatory")
_SystemResourceIOInfoIndexAtt1_Type = DmiInteger
_SystemResourceIOInfoIndexAtt1_Object = MibTableColumn
systemResourceIOInfoIndexAtt1 = _SystemResourceIOInfoIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 40, 1, 1),
    _SystemResourceIOInfoIndexAtt1_Type()
)
systemResourceIOInfoIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOInfoIndexAtt1.setStatus("mandatory")


class _IODecodeAtt2_Type(Integer32):
    """Custom type iODecodeAtt2 based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("x10Bits", 3),
          ("x16Bits", 4))
    )


_IODecodeAtt2_Type.__name__ = "Integer32"
_IODecodeAtt2_Object = MibTableColumn
iODecodeAtt2 = _IODecodeAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 40, 1, 2),
    _IODecodeAtt2_Type()
)
iODecodeAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iODecodeAtt2.setStatus("mandatory")
_DMTFSystemResourceIRQInfoTable_Object = MibTable
dMTFSystemResourceIRQInfoTable = _DMTFSystemResourceIRQInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 41)
)
if mibBuilder.loadTexts:
    dMTFSystemResourceIRQInfoTable.setStatus("mandatory")
_DMTFSystemResourceIRQInfoEntry_Object = MibTableRow
dMTFSystemResourceIRQInfoEntry = _DMTFSystemResourceIRQInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 41, 1)
)
dMTFSystemResourceIRQInfoEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "systemResourceIRQInfoIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSystemResourceIRQInfoEntry.setStatus("mandatory")


class _DMTFSystemResourceIRQInfoState_Type(Integer32):
    """Custom type dMTFSystemResourceIRQInfoState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSystemResourceIRQInfoState_Type.__name__ = "Integer32"
_DMTFSystemResourceIRQInfoState_Object = MibTableColumn
dMTFSystemResourceIRQInfoState = _DMTFSystemResourceIRQInfoState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 41, 1, 0),
    _DMTFSystemResourceIRQInfoState_Type()
)
dMTFSystemResourceIRQInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSystemResourceIRQInfoState.setStatus("mandatory")
_SystemResourceIRQInfoIndexAtt1_Type = DmiInteger
_SystemResourceIRQInfoIndexAtt1_Object = MibTableColumn
systemResourceIRQInfoIndexAtt1 = _SystemResourceIRQInfoIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 41, 1, 1),
    _SystemResourceIRQInfoIndexAtt1_Type()
)
systemResourceIRQInfoIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIRQInfoIndexAtt1.setStatus("mandatory")


class _TriggerTypeAtt2_Type(Integer32):
    """Custom type triggerTypeAtt2 based on Integer32"""
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
        *(("edge", 4),
          ("level", 3),
          ("other", 1),
          ("unknown", 2))
    )


_TriggerTypeAtt2_Type.__name__ = "Integer32"
_TriggerTypeAtt2_Object = MibTableColumn
triggerTypeAtt2 = _TriggerTypeAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 41, 1, 2),
    _TriggerTypeAtt2_Type()
)
triggerTypeAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerTypeAtt2.setStatus("mandatory")


class _TriggerLevelAtt3_Type(Integer32):
    """Custom type triggerLevelAtt3 based on Integer32"""
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
        *(("activeHigh", 4),
          ("activeLow", 3),
          ("other", 1),
          ("unknown", 2))
    )


_TriggerLevelAtt3_Type.__name__ = "Integer32"
_TriggerLevelAtt3_Object = MibTableColumn
triggerLevelAtt3 = _TriggerLevelAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 41, 1, 3),
    _TriggerLevelAtt3_Type()
)
triggerLevelAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerLevelAtt3.setStatus("mandatory")
_DMTFSystemResourceDMAInfoTable_Object = MibTable
dMTFSystemResourceDMAInfoTable = _DMTFSystemResourceDMAInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42)
)
if mibBuilder.loadTexts:
    dMTFSystemResourceDMAInfoTable.setStatus("mandatory")
_DMTFSystemResourceDMAInfoEntry_Object = MibTableRow
dMTFSystemResourceDMAInfoEntry = _DMTFSystemResourceDMAInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1)
)
dMTFSystemResourceDMAInfoEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "systemResourceDMAInfoIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFSystemResourceDMAInfoEntry.setStatus("mandatory")


class _DMTFSystemResourceDMAInfoState_Type(Integer32):
    """Custom type dMTFSystemResourceDMAInfoState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFSystemResourceDMAInfoState_Type.__name__ = "Integer32"
_DMTFSystemResourceDMAInfoState_Object = MibTableColumn
dMTFSystemResourceDMAInfoState = _DMTFSystemResourceDMAInfoState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 0),
    _DMTFSystemResourceDMAInfoState_Type()
)
dMTFSystemResourceDMAInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFSystemResourceDMAInfoState.setStatus("mandatory")
_SystemResourceDMAInfoIndexAtt1_Type = DmiInteger
_SystemResourceDMAInfoIndexAtt1_Object = MibTableColumn
systemResourceDMAInfoIndexAtt1 = _SystemResourceDMAInfoIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 1),
    _SystemResourceDMAInfoIndexAtt1_Type()
)
systemResourceDMAInfoIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAInfoIndexAtt1.setStatus("mandatory")


class _DMATransferWidthAtt2_Type(Integer32):
    """Custom type dMATransferWidthAtt2 based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("x128Bit", 8),
          ("x16Bit", 5),
          ("x32Bit", 6),
          ("x64Bit", 7),
          ("x8And16Bit", 4),
          ("x8Bit", 3))
    )


_DMATransferWidthAtt2_Type.__name__ = "Integer32"
_DMATransferWidthAtt2_Object = MibTableColumn
dMATransferWidthAtt2 = _DMATransferWidthAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 2),
    _DMATransferWidthAtt2_Type()
)
dMATransferWidthAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMATransferWidthAtt2.setStatus("mandatory")


class _DMAAddressSizeAtt3_Type(Integer32):
    """Custom type dMAAddressSizeAtt3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("x16Bit", 5),
          ("x32Bit", 6),
          ("x64Bit", 7),
          ("x8Bit", 3))
    )


_DMAAddressSizeAtt3_Type.__name__ = "Integer32"
_DMAAddressSizeAtt3_Object = MibTableColumn
dMAAddressSizeAtt3 = _DMAAddressSizeAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 3),
    _DMAAddressSizeAtt3_Type()
)
dMAAddressSizeAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMAAddressSizeAtt3.setStatus("mandatory")
_DMAMaximumTransferSizeAtt4_Type = DmiInteger
_DMAMaximumTransferSizeAtt4_Object = MibTableColumn
dMAMaximumTransferSizeAtt4 = _DMAMaximumTransferSizeAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 4),
    _DMAMaximumTransferSizeAtt4_Type()
)
dMAMaximumTransferSizeAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMAMaximumTransferSizeAtt4.setStatus("mandatory")


class _DMATransferPreferenceAtt5_Type(Integer32):
    """Custom type dMATransferPreferenceAtt5 based on Integer32"""
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
          ("unknown", 2),
          ("x16Bit", 5),
          ("x32Bit", 6),
          ("x64Bit", 7),
          ("x8And16Bit", 4),
          ("x8Bit", 3))
    )


_DMATransferPreferenceAtt5_Type.__name__ = "Integer32"
_DMATransferPreferenceAtt5_Object = MibTableColumn
dMATransferPreferenceAtt5 = _DMATransferPreferenceAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 5),
    _DMATransferPreferenceAtt5_Type()
)
dMATransferPreferenceAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMATransferPreferenceAtt5.setStatus("mandatory")


class _BusMasterAtt6_Type(Integer32):
    """Custom type busMasterAtt6 based on Integer32"""
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
        *(("logicalDeviceIsABusMaster", 4),
          ("logicalDeviceIsNotABusMaster", 3),
          ("other", 1),
          ("unknown", 2))
    )


_BusMasterAtt6_Type.__name__ = "Integer32"
_BusMasterAtt6_Object = MibTableColumn
busMasterAtt6 = _BusMasterAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 6),
    _BusMasterAtt6_Type()
)
busMasterAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busMasterAtt6.setStatus("mandatory")


class _ByteModeAtt7_Type(Integer32):
    """Custom type byteModeAtt7 based on Integer32"""
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
        *(("dMAMayExecuteInCountByByteMode", 4),
          ("dMAMayNotExecuteInCountByByteMode", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ByteModeAtt7_Type.__name__ = "Integer32"
_ByteModeAtt7_Object = MibTableColumn
byteModeAtt7 = _ByteModeAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 7),
    _ByteModeAtt7_Type()
)
byteModeAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    byteModeAtt7.setStatus("mandatory")


class _WordModeAtt8_Type(Integer32):
    """Custom type wordModeAtt8 based on Integer32"""
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
        *(("dMAMayExecuteInCountByWordMode", 4),
          ("dMAMayNotExecuteInCountByWordMode", 3),
          ("other", 1),
          ("unknown", 2))
    )


_WordModeAtt8_Type.__name__ = "Integer32"
_WordModeAtt8_Object = MibTableColumn
wordModeAtt8 = _WordModeAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 8),
    _WordModeAtt8_Type()
)
wordModeAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wordModeAtt8.setStatus("mandatory")


class _ChannelTimingAtt9_Type(Integer32):
    """Custom type channelTimingAtt9 based on Integer32"""
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
        *(("iSACompatible", 3),
          ("other", 1),
          ("typeA", 4),
          ("typeB", 5),
          ("typeF", 6),
          ("unknown", 2))
    )


_ChannelTimingAtt9_Type.__name__ = "Integer32"
_ChannelTimingAtt9_Object = MibTableColumn
channelTimingAtt9 = _ChannelTimingAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 9),
    _ChannelTimingAtt9_Type()
)
channelTimingAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelTimingAtt9.setStatus("mandatory")


class _TypeCTimingAtt10_Type(Integer32):
    """Custom type typeCTimingAtt10 based on Integer32"""
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
        *(("cTypeTimingIsNotSupported", 4),
          ("cTypeTimingIsSupported", 5),
          ("iSACompatible", 3),
          ("other", 1),
          ("unknown", 2))
    )


_TypeCTimingAtt10_Type.__name__ = "Integer32"
_TypeCTimingAtt10_Object = MibTableColumn
typeCTimingAtt10 = _TypeCTimingAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 42, 1, 10),
    _TypeCTimingAtt10_Type()
)
typeCTimingAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    typeCTimingAtt10.setStatus("mandatory")
_DMTFSystemHardwareSecurityTable_Object = MibTable
dMTFSystemHardwareSecurityTable = _DMTFSystemHardwareSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 49)
)
if mibBuilder.loadTexts:
    dMTFSystemHardwareSecurityTable.setStatus("mandatory")
_DMTFSystemHardwareSecurityEntry_Object = MibTableRow
dMTFSystemHardwareSecurityEntry = _DMTFSystemHardwareSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 49, 1)
)
dMTFSystemHardwareSecurityEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dMTFSystemHardwareSecurityEntry.setStatus("mandatory")


class _PowerOnPasswordStatusAtt1_Type(Integer32):
    """Custom type powerOnPasswordStatusAtt1 based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 4),
          ("notImplemented", 5),
          ("other", 1),
          ("unknown", 2))
    )


_PowerOnPasswordStatusAtt1_Type.__name__ = "Integer32"
_PowerOnPasswordStatusAtt1_Object = MibTableColumn
powerOnPasswordStatusAtt1 = _PowerOnPasswordStatusAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 49, 1, 1),
    _PowerOnPasswordStatusAtt1_Type()
)
powerOnPasswordStatusAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnPasswordStatusAtt1.setStatus("mandatory")


class _KeyboardPasswordStatusAtt2_Type(Integer32):
    """Custom type keyboardPasswordStatusAtt2 based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 4),
          ("notImplemented", 5),
          ("other", 1),
          ("unknown", 2))
    )


_KeyboardPasswordStatusAtt2_Type.__name__ = "Integer32"
_KeyboardPasswordStatusAtt2_Object = MibTableColumn
keyboardPasswordStatusAtt2 = _KeyboardPasswordStatusAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 49, 1, 2),
    _KeyboardPasswordStatusAtt2_Type()
)
keyboardPasswordStatusAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPasswordStatusAtt2.setStatus("mandatory")


class _AdministratorPasswordStatisAtt3_Type(Integer32):
    """Custom type administratorPasswordStatisAtt3 based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 4),
          ("notImplemented", 5),
          ("other", 1),
          ("unknown", 2))
    )


_AdministratorPasswordStatisAtt3_Type.__name__ = "Integer32"
_AdministratorPasswordStatisAtt3_Object = MibTableColumn
administratorPasswordStatisAtt3 = _AdministratorPasswordStatisAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 49, 1, 3),
    _AdministratorPasswordStatisAtt3_Type()
)
administratorPasswordStatisAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    administratorPasswordStatisAtt3.setStatus("mandatory")


class _FrontPanelResetStatusAtt4_Type(Integer32):
    """Custom type frontPanelResetStatusAtt4 based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 4),
          ("notImplemented", 5),
          ("other", 1),
          ("unknown", 2))
    )


_FrontPanelResetStatusAtt4_Type.__name__ = "Integer32"
_FrontPanelResetStatusAtt4_Object = MibTableColumn
frontPanelResetStatusAtt4 = _FrontPanelResetStatusAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 49, 1, 4),
    _FrontPanelResetStatusAtt4_Type()
)
frontPanelResetStatusAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frontPanelResetStatusAtt4.setStatus("mandatory")
_DMTFSystemPowerControlsTable_Object = MibTable
dMTFSystemPowerControlsTable = _DMTFSystemPowerControlsTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 51)
)
if mibBuilder.loadTexts:
    dMTFSystemPowerControlsTable.setStatus("mandatory")
_DMTFSystemPowerControlsEntry_Object = MibTableRow
dMTFSystemPowerControlsEntry = _DMTFSystemPowerControlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 51, 1)
)
dMTFSystemPowerControlsEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dMTFSystemPowerControlsEntry.setStatus("mandatory")


class _PowerControlRequestAtt1_Type(Integer32):
    """Custom type powerControlRequestAtt1 based on Integer32"""
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
        *(("enterHibernationMode", 7),
          ("enterStandbyMode", 5),
          ("enterSuspendMode", 6),
          ("other", 1),
          ("powerOff", 3),
          ("powerOffThenOnAgain", 4),
          ("unknown", 2))
    )


_PowerControlRequestAtt1_Type.__name__ = "Integer32"
_PowerControlRequestAtt1_Object = MibTableColumn
powerControlRequestAtt1 = _PowerControlRequestAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 51, 1, 1),
    _PowerControlRequestAtt1_Type()
)
powerControlRequestAtt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerControlRequestAtt1.setStatus("mandatory")


class _TimedPowerOnAvailableAtt2_Type(Integer32):
    """Custom type timedPowerOnAvailableAtt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_TimedPowerOnAvailableAtt2_Type.__name__ = "Integer32"
_TimedPowerOnAvailableAtt2_Object = MibTableColumn
timedPowerOnAvailableAtt2 = _TimedPowerOnAvailableAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 51, 1, 2),
    _TimedPowerOnAvailableAtt2_Type()
)
timedPowerOnAvailableAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timedPowerOnAvailableAtt2.setStatus("mandatory")
_TimeToNextScheduledPowerOnAtt3_Type = DmiInteger
_TimeToNextScheduledPowerOnAtt3_Object = MibTableColumn
timeToNextScheduledPowerOnAtt3 = _TimeToNextScheduledPowerOnAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 51, 1, 3),
    _TimeToNextScheduledPowerOnAtt3_Type()
)
timeToNextScheduledPowerOnAtt3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeToNextScheduledPowerOnAtt3.setStatus("mandatory")
_DMTFVoltageProbeTable_Object = MibTable
dMTFVoltageProbeTable = _DMTFVoltageProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53)
)
if mibBuilder.loadTexts:
    dMTFVoltageProbeTable.setStatus("mandatory")
_DMTFVoltageProbeEntry_Object = MibTableRow
dMTFVoltageProbeEntry = _DMTFVoltageProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1)
)
dMTFVoltageProbeEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "voltageProbeIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFVoltageProbeEntry.setStatus("mandatory")


class _DMTFVoltageProbeState_Type(Integer32):
    """Custom type dMTFVoltageProbeState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFVoltageProbeState_Type.__name__ = "Integer32"
_DMTFVoltageProbeState_Object = MibTableColumn
dMTFVoltageProbeState = _DMTFVoltageProbeState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 0),
    _DMTFVoltageProbeState_Type()
)
dMTFVoltageProbeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFVoltageProbeState.setStatus("mandatory")
_VoltageProbeIndexAtt1_Type = DmiInteger
_VoltageProbeIndexAtt1_Object = MibTableColumn
voltageProbeIndexAtt1 = _VoltageProbeIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 1),
    _VoltageProbeIndexAtt1_Type()
)
voltageProbeIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeIndexAtt1.setStatus("mandatory")


class _VoltageProbeLocationAtt2_Type(Integer32):
    """Custom type voltageProbeLocationAtt2 based on Integer32"""
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
        *(("addInCard", 11),
          ("disk", 4),
          ("memoryModule", 8),
          ("motherboard", 7),
          ("other", 1),
          ("peripheralBay", 5),
          ("powerUnit", 10),
          ("processor", 3),
          ("processorModule", 9),
          ("systemManagementModule", 6),
          ("unknown", 2))
    )


_VoltageProbeLocationAtt2_Type.__name__ = "Integer32"
_VoltageProbeLocationAtt2_Object = MibTableColumn
voltageProbeLocationAtt2 = _VoltageProbeLocationAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 2),
    _VoltageProbeLocationAtt2_Type()
)
voltageProbeLocationAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLocationAtt2.setStatus("mandatory")
_VoltageProbeDescriptionAtt3_Type = DmiDisplaystring
_VoltageProbeDescriptionAtt3_Object = MibTableColumn
voltageProbeDescriptionAtt3 = _VoltageProbeDescriptionAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 3),
    _VoltageProbeDescriptionAtt3_Type()
)
voltageProbeDescriptionAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeDescriptionAtt3.setStatus("mandatory")


class _VoltageStatusAtt4_Type(Integer32):
    """Custom type voltageStatusAtt4 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_VoltageStatusAtt4_Type.__name__ = "Integer32"
_VoltageStatusAtt4_Object = MibTableColumn
voltageStatusAtt4 = _VoltageStatusAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 4),
    _VoltageStatusAtt4_Type()
)
voltageStatusAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageStatusAtt4.setStatus("mandatory")
_VoltageProbeVoltageLevelAtt5_Type = DmiInteger
_VoltageProbeVoltageLevelAtt5_Object = MibTableColumn
voltageProbeVoltageLevelAtt5 = _VoltageProbeVoltageLevelAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 5),
    _VoltageProbeVoltageLevelAtt5_Type()
)
voltageProbeVoltageLevelAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeVoltageLevelAtt5.setStatus("mandatory")
_MonitoredVoltageNominalLevelAtt6_Type = DmiInteger
_MonitoredVoltageNominalLevelAtt6_Object = MibTableColumn
monitoredVoltageNominalLevelAtt6 = _MonitoredVoltageNominalLevelAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 6),
    _MonitoredVoltageNominalLevelAtt6_Type()
)
monitoredVoltageNominalLevelAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoredVoltageNominalLevelAtt6.setStatus("mandatory")
_MonitoredVoltageNormalMaximumAtt7_Type = DmiInteger
_MonitoredVoltageNormalMaximumAtt7_Object = MibTableColumn
monitoredVoltageNormalMaximumAtt7 = _MonitoredVoltageNormalMaximumAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 7),
    _MonitoredVoltageNormalMaximumAtt7_Type()
)
monitoredVoltageNormalMaximumAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoredVoltageNormalMaximumAtt7.setStatus("mandatory")
_MonitoredVoltageNormalMinimumAtt8_Type = DmiInteger
_MonitoredVoltageNormalMinimumAtt8_Object = MibTableColumn
monitoredVoltageNormalMinimumAtt8 = _MonitoredVoltageNormalMinimumAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 8),
    _MonitoredVoltageNormalMinimumAtt8_Type()
)
monitoredVoltageNormalMinimumAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoredVoltageNormalMinimumAtt8.setStatus("mandatory")
_VoltageProbeMaximumAtt9_Type = DmiInteger
_VoltageProbeMaximumAtt9_Object = MibTableColumn
voltageProbeMaximumAtt9 = _VoltageProbeMaximumAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 9),
    _VoltageProbeMaximumAtt9_Type()
)
voltageProbeMaximumAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeMaximumAtt9.setStatus("mandatory")
_VoltageProbeMinimumAtt10_Type = DmiInteger
_VoltageProbeMinimumAtt10_Object = MibTableColumn
voltageProbeMinimumAtt10 = _VoltageProbeMinimumAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 10),
    _VoltageProbeMinimumAtt10_Type()
)
voltageProbeMinimumAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeMinimumAtt10.setStatus("mandatory")
_VoltageLevelLowerThresholdNonCriticalAtt11_Type = DmiInteger
_VoltageLevelLowerThresholdNonCriticalAtt11_Object = MibTableColumn
voltageLevelLowerThresholdNonCriticalAtt11 = _VoltageLevelLowerThresholdNonCriticalAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 11),
    _VoltageLevelLowerThresholdNonCriticalAtt11_Type()
)
voltageLevelLowerThresholdNonCriticalAtt11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageLevelLowerThresholdNonCriticalAtt11.setStatus("mandatory")
_VoltageLevelUpperThresholdNonCriticalAtt12_Type = DmiInteger
_VoltageLevelUpperThresholdNonCriticalAtt12_Object = MibTableColumn
voltageLevelUpperThresholdNonCriticalAtt12 = _VoltageLevelUpperThresholdNonCriticalAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 12),
    _VoltageLevelUpperThresholdNonCriticalAtt12_Type()
)
voltageLevelUpperThresholdNonCriticalAtt12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageLevelUpperThresholdNonCriticalAtt12.setStatus("mandatory")
_VoltageLevelLowerThresholdCriticalAtt13_Type = DmiInteger
_VoltageLevelLowerThresholdCriticalAtt13_Object = MibTableColumn
voltageLevelLowerThresholdCriticalAtt13 = _VoltageLevelLowerThresholdCriticalAtt13_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 13),
    _VoltageLevelLowerThresholdCriticalAtt13_Type()
)
voltageLevelLowerThresholdCriticalAtt13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageLevelLowerThresholdCriticalAtt13.setStatus("mandatory")
_VoltageLevelUpperThresholdCriticalAtt14_Type = DmiInteger
_VoltageLevelUpperThresholdCriticalAtt14_Object = MibTableColumn
voltageLevelUpperThresholdCriticalAtt14 = _VoltageLevelUpperThresholdCriticalAtt14_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 14),
    _VoltageLevelUpperThresholdCriticalAtt14_Type()
)
voltageLevelUpperThresholdCriticalAtt14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageLevelUpperThresholdCriticalAtt14.setStatus("mandatory")
_VoltageLevelLowerThresholdNonRecoverableAtt15_Type = DmiInteger
_VoltageLevelLowerThresholdNonRecoverableAtt15_Object = MibTableColumn
voltageLevelLowerThresholdNonRecoverableAtt15 = _VoltageLevelLowerThresholdNonRecoverableAtt15_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 15),
    _VoltageLevelLowerThresholdNonRecoverableAtt15_Type()
)
voltageLevelLowerThresholdNonRecoverableAtt15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageLevelLowerThresholdNonRecoverableAtt15.setStatus("mandatory")
_VoltageLevelUpperThresholdNonRecoverableAtt16_Type = DmiInteger
_VoltageLevelUpperThresholdNonRecoverableAtt16_Object = MibTableColumn
voltageLevelUpperThresholdNonRecoverableAtt16 = _VoltageLevelUpperThresholdNonRecoverableAtt16_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 16),
    _VoltageLevelUpperThresholdNonRecoverableAtt16_Type()
)
voltageLevelUpperThresholdNonRecoverableAtt16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageLevelUpperThresholdNonRecoverableAtt16.setStatus("mandatory")
_VoltageProbeResolutionAtt17_Type = DmiInteger
_VoltageProbeResolutionAtt17_Object = MibTableColumn
voltageProbeResolutionAtt17 = _VoltageProbeResolutionAtt17_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 17),
    _VoltageProbeResolutionAtt17_Type()
)
voltageProbeResolutionAtt17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageProbeResolutionAtt17.setStatus("mandatory")
_VoltageProbeToleranceAtt18_Type = DmiInteger
_VoltageProbeToleranceAtt18_Object = MibTableColumn
voltageProbeToleranceAtt18 = _VoltageProbeToleranceAtt18_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 18),
    _VoltageProbeToleranceAtt18_Type()
)
voltageProbeToleranceAtt18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageProbeToleranceAtt18.setStatus("mandatory")
_VoltageProbeAccuracyAtt19_Type = DmiInteger
_VoltageProbeAccuracyAtt19_Object = MibTableColumn
voltageProbeAccuracyAtt19 = _VoltageProbeAccuracyAtt19_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 19),
    _VoltageProbeAccuracyAtt19_Type()
)
voltageProbeAccuracyAtt19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageProbeAccuracyAtt19.setStatus("mandatory")
_FRUGroupIndexAtt20_2_Type = DmiInteger
_FRUGroupIndexAtt20_2_Object = MibScalar
fRUGroupIndexAtt20_2 = _FRUGroupIndexAtt20_2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 20),
    _FRUGroupIndexAtt20_2_Type()
)
fRUGroupIndexAtt20_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt20_2.setStatus("mandatory")
_OperationalGroupIndexAtt21_2_Type = DmiInteger
_OperationalGroupIndexAtt21_2_Object = MibScalar
operationalGroupIndexAtt21_2 = _OperationalGroupIndexAtt21_2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 1, 21),
    _OperationalGroupIndexAtt21_2_Type()
)
operationalGroupIndexAtt21_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt21_2.setStatus("mandatory")


class _DMTFVoltageProbeEvSys_Type(Integer32):
    """Custom type dMTFVoltageProbeEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFVoltageProbeEvSys_Type.__name__ = "Integer32"
_DMTFVoltageProbeEvSys_Object = MibScalar
dMTFVoltageProbeEvSys = _DMTFVoltageProbeEvSys_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 6),
    _DMTFVoltageProbeEvSys_Type()
)
dMTFVoltageProbeEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFVoltageProbeEvSys.setStatus("mandatory")


class _DMTFVoltageProbeEvSub_Type(Integer32):
    """Custom type dMTFVoltageProbeEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFVoltageProbeEvSub_Type.__name__ = "Integer32"
_DMTFVoltageProbeEvSub_Object = MibScalar
dMTFVoltageProbeEvSub = _DMTFVoltageProbeEvSub_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 7),
    _DMTFVoltageProbeEvSub_Type()
)
dMTFVoltageProbeEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFVoltageProbeEvSub.setStatus("mandatory")
_DMTFTemperatureProbeTable_Object = MibTable
dMTFTemperatureProbeTable = _DMTFTemperatureProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54)
)
if mibBuilder.loadTexts:
    dMTFTemperatureProbeTable.setStatus("mandatory")
_DMTFTemperatureProbeEntry_Object = MibTableRow
dMTFTemperatureProbeEntry = _DMTFTemperatureProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1)
)
dMTFTemperatureProbeEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "temperatureProbeTableIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFTemperatureProbeEntry.setStatus("mandatory")


class _DMTFTemperatureProbeState_Type(Integer32):
    """Custom type dMTFTemperatureProbeState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFTemperatureProbeState_Type.__name__ = "Integer32"
_DMTFTemperatureProbeState_Object = MibTableColumn
dMTFTemperatureProbeState = _DMTFTemperatureProbeState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 0),
    _DMTFTemperatureProbeState_Type()
)
dMTFTemperatureProbeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFTemperatureProbeState.setStatus("mandatory")
_TemperatureProbeTableIndexAtt1_Type = DmiInteger
_TemperatureProbeTableIndexAtt1_Object = MibTableColumn
temperatureProbeTableIndexAtt1 = _TemperatureProbeTableIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 1),
    _TemperatureProbeTableIndexAtt1_Type()
)
temperatureProbeTableIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeTableIndexAtt1.setStatus("mandatory")


class _TemperatureProbeLocationAtt2_Type(Integer32):
    """Custom type temperatureProbeLocationAtt2 based on Integer32"""
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
        *(("addInCard", 11),
          ("disk", 4),
          ("memoryModule", 8),
          ("motherboard", 7),
          ("other", 1),
          ("peripheralBay", 5),
          ("powerUnit", 10),
          ("processor", 3),
          ("processorModule", 9),
          ("sMBMaster", 6),
          ("unknown", 2))
    )


_TemperatureProbeLocationAtt2_Type.__name__ = "Integer32"
_TemperatureProbeLocationAtt2_Object = MibTableColumn
temperatureProbeLocationAtt2 = _TemperatureProbeLocationAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 2),
    _TemperatureProbeLocationAtt2_Type()
)
temperatureProbeLocationAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLocationAtt2.setStatus("mandatory")
_TemperatureProbeDescriptionAtt3_Type = DmiDisplaystring
_TemperatureProbeDescriptionAtt3_Object = MibTableColumn
temperatureProbeDescriptionAtt3 = _TemperatureProbeDescriptionAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 3),
    _TemperatureProbeDescriptionAtt3_Type()
)
temperatureProbeDescriptionAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeDescriptionAtt3.setStatus("mandatory")


class _TemperatureStatusAtt4_Type(Integer32):
    """Custom type temperatureStatusAtt4 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_TemperatureStatusAtt4_Type.__name__ = "Integer32"
_TemperatureStatusAtt4_Object = MibTableColumn
temperatureStatusAtt4 = _TemperatureStatusAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 4),
    _TemperatureStatusAtt4_Type()
)
temperatureStatusAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureStatusAtt4.setStatus("mandatory")
_TemperatureProbeTemperatureReadingAtt5_Type = DmiInteger
_TemperatureProbeTemperatureReadingAtt5_Object = MibTableColumn
temperatureProbeTemperatureReadingAtt5 = _TemperatureProbeTemperatureReadingAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 5),
    _TemperatureProbeTemperatureReadingAtt5_Type()
)
temperatureProbeTemperatureReadingAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeTemperatureReadingAtt5.setStatus("mandatory")
_MonitoredTemperatureNominalReadingAtt6_Type = DmiInteger
_MonitoredTemperatureNominalReadingAtt6_Object = MibTableColumn
monitoredTemperatureNominalReadingAtt6 = _MonitoredTemperatureNominalReadingAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 6),
    _MonitoredTemperatureNominalReadingAtt6_Type()
)
monitoredTemperatureNominalReadingAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoredTemperatureNominalReadingAtt6.setStatus("mandatory")
_MonitoredTemperatureNormalMaximumAtt7_Type = DmiInteger
_MonitoredTemperatureNormalMaximumAtt7_Object = MibTableColumn
monitoredTemperatureNormalMaximumAtt7 = _MonitoredTemperatureNormalMaximumAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 7),
    _MonitoredTemperatureNormalMaximumAtt7_Type()
)
monitoredTemperatureNormalMaximumAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoredTemperatureNormalMaximumAtt7.setStatus("mandatory")
_MonitoredTemperatureNormalMinimumAtt8_Type = DmiInteger
_MonitoredTemperatureNormalMinimumAtt8_Object = MibTableColumn
monitoredTemperatureNormalMinimumAtt8 = _MonitoredTemperatureNormalMinimumAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 8),
    _MonitoredTemperatureNormalMinimumAtt8_Type()
)
monitoredTemperatureNormalMinimumAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoredTemperatureNormalMinimumAtt8.setStatus("mandatory")
_TemperatureProbeMaximumAtt9_Type = DmiInteger
_TemperatureProbeMaximumAtt9_Object = MibTableColumn
temperatureProbeMaximumAtt9 = _TemperatureProbeMaximumAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 9),
    _TemperatureProbeMaximumAtt9_Type()
)
temperatureProbeMaximumAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMaximumAtt9.setStatus("mandatory")
_TemperatureProbeMinimumAtt10_Type = DmiInteger
_TemperatureProbeMinimumAtt10_Object = MibTableColumn
temperatureProbeMinimumAtt10 = _TemperatureProbeMinimumAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 10),
    _TemperatureProbeMinimumAtt10_Type()
)
temperatureProbeMinimumAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeMinimumAtt10.setStatus("mandatory")
_TemperatureReadingLowerThresholdNonCriticalAtt11_Type = DmiInteger
_TemperatureReadingLowerThresholdNonCriticalAtt11_Object = MibTableColumn
temperatureReadingLowerThresholdNonCriticalAtt11 = _TemperatureReadingLowerThresholdNonCriticalAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 11),
    _TemperatureReadingLowerThresholdNonCriticalAtt11_Type()
)
temperatureReadingLowerThresholdNonCriticalAtt11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureReadingLowerThresholdNonCriticalAtt11.setStatus("mandatory")
_TemperatureReadingUpperThresholdNonCriticalAtt12_Type = DmiInteger
_TemperatureReadingUpperThresholdNonCriticalAtt12_Object = MibTableColumn
temperatureReadingUpperThresholdNonCriticalAtt12 = _TemperatureReadingUpperThresholdNonCriticalAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 12),
    _TemperatureReadingUpperThresholdNonCriticalAtt12_Type()
)
temperatureReadingUpperThresholdNonCriticalAtt12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureReadingUpperThresholdNonCriticalAtt12.setStatus("mandatory")
_TemperatureReadingLowerThresholdCriticalAtt13_Type = DmiInteger
_TemperatureReadingLowerThresholdCriticalAtt13_Object = MibTableColumn
temperatureReadingLowerThresholdCriticalAtt13 = _TemperatureReadingLowerThresholdCriticalAtt13_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 13),
    _TemperatureReadingLowerThresholdCriticalAtt13_Type()
)
temperatureReadingLowerThresholdCriticalAtt13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureReadingLowerThresholdCriticalAtt13.setStatus("mandatory")
_TemperatureReadingUpperThresholdCriticalAtt14_Type = DmiInteger
_TemperatureReadingUpperThresholdCriticalAtt14_Object = MibTableColumn
temperatureReadingUpperThresholdCriticalAtt14 = _TemperatureReadingUpperThresholdCriticalAtt14_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 14),
    _TemperatureReadingUpperThresholdCriticalAtt14_Type()
)
temperatureReadingUpperThresholdCriticalAtt14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureReadingUpperThresholdCriticalAtt14.setStatus("mandatory")
_TemperatureReadingLowerThresholdNonRecoverableAtt15_Type = DmiInteger
_TemperatureReadingLowerThresholdNonRecoverableAtt15_Object = MibTableColumn
temperatureReadingLowerThresholdNonRecoverableAtt15 = _TemperatureReadingLowerThresholdNonRecoverableAtt15_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 15),
    _TemperatureReadingLowerThresholdNonRecoverableAtt15_Type()
)
temperatureReadingLowerThresholdNonRecoverableAtt15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureReadingLowerThresholdNonRecoverableAtt15.setStatus("mandatory")
_TemperatureReadingUpperThresholdNonRecoverableAtt16_Type = DmiInteger
_TemperatureReadingUpperThresholdNonRecoverableAtt16_Object = MibTableColumn
temperatureReadingUpperThresholdNonRecoverableAtt16 = _TemperatureReadingUpperThresholdNonRecoverableAtt16_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 16),
    _TemperatureReadingUpperThresholdNonRecoverableAtt16_Type()
)
temperatureReadingUpperThresholdNonRecoverableAtt16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureReadingUpperThresholdNonRecoverableAtt16.setStatus("mandatory")
_TemperatureProbeResolutionAtt17_Type = DmiInteger
_TemperatureProbeResolutionAtt17_Object = MibTableColumn
temperatureProbeResolutionAtt17 = _TemperatureProbeResolutionAtt17_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 17),
    _TemperatureProbeResolutionAtt17_Type()
)
temperatureProbeResolutionAtt17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureProbeResolutionAtt17.setStatus("mandatory")
_TemperatureProbeToleranceAtt18_Type = DmiInteger
_TemperatureProbeToleranceAtt18_Object = MibTableColumn
temperatureProbeToleranceAtt18 = _TemperatureProbeToleranceAtt18_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 18),
    _TemperatureProbeToleranceAtt18_Type()
)
temperatureProbeToleranceAtt18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureProbeToleranceAtt18.setStatus("mandatory")
_TemperatureProbeAccuracyAtt19_Type = DmiInteger
_TemperatureProbeAccuracyAtt19_Object = MibTableColumn
temperatureProbeAccuracyAtt19 = _TemperatureProbeAccuracyAtt19_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 19),
    _TemperatureProbeAccuracyAtt19_Type()
)
temperatureProbeAccuracyAtt19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureProbeAccuracyAtt19.setStatus("mandatory")
_FRUGroupIndexAtt20_1_Type = DmiInteger
_FRUGroupIndexAtt20_1_Object = MibScalar
fRUGroupIndexAtt20_1 = _FRUGroupIndexAtt20_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 20),
    _FRUGroupIndexAtt20_1_Type()
)
fRUGroupIndexAtt20_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt20_1.setStatus("mandatory")
_OperationalGroupIndexAtt21_1_Type = DmiInteger
_OperationalGroupIndexAtt21_1_Object = MibScalar
operationalGroupIndexAtt21_1 = _OperationalGroupIndexAtt21_1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 1, 21),
    _OperationalGroupIndexAtt21_1_Type()
)
operationalGroupIndexAtt21_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt21_1.setStatus("mandatory")


class _DMTFTemperatureProbeEvSys_Type(Integer32):
    """Custom type dMTFTemperatureProbeEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFTemperatureProbeEvSys_Type.__name__ = "Integer32"
_DMTFTemperatureProbeEvSys_Object = MibScalar
dMTFTemperatureProbeEvSys = _DMTFTemperatureProbeEvSys_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 6),
    _DMTFTemperatureProbeEvSys_Type()
)
dMTFTemperatureProbeEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFTemperatureProbeEvSys.setStatus("mandatory")


class _DMTFTemperatureProbeEvSub_Type(Integer32):
    """Custom type dMTFTemperatureProbeEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFTemperatureProbeEvSub_Type.__name__ = "Integer32"
_DMTFTemperatureProbeEvSub_Object = MibScalar
dMTFTemperatureProbeEvSub = _DMTFTemperatureProbeEvSub_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 7),
    _DMTFTemperatureProbeEvSub_Type()
)
dMTFTemperatureProbeEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFTemperatureProbeEvSub.setStatus("mandatory")
_DMTFElectricalCurrentProbeTable_Object = MibTable
dMTFElectricalCurrentProbeTable = _DMTFElectricalCurrentProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55)
)
if mibBuilder.loadTexts:
    dMTFElectricalCurrentProbeTable.setStatus("mandatory")
_DMTFElectricalCurrentProbeEntry_Object = MibTableRow
dMTFElectricalCurrentProbeEntry = _DMTFElectricalCurrentProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1)
)
dMTFElectricalCurrentProbeEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "electricalCurrentProbeTableIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFElectricalCurrentProbeEntry.setStatus("mandatory")


class _DMTFElectricalCurrentProbeState_Type(Integer32):
    """Custom type dMTFElectricalCurrentProbeState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFElectricalCurrentProbeState_Type.__name__ = "Integer32"
_DMTFElectricalCurrentProbeState_Object = MibTableColumn
dMTFElectricalCurrentProbeState = _DMTFElectricalCurrentProbeState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 0),
    _DMTFElectricalCurrentProbeState_Type()
)
dMTFElectricalCurrentProbeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFElectricalCurrentProbeState.setStatus("mandatory")
_ElectricalCurrentProbeTableIndexAtt1_Type = DmiInteger
_ElectricalCurrentProbeTableIndexAtt1_Object = MibTableColumn
electricalCurrentProbeTableIndexAtt1 = _ElectricalCurrentProbeTableIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 1),
    _ElectricalCurrentProbeTableIndexAtt1_Type()
)
electricalCurrentProbeTableIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    electricalCurrentProbeTableIndexAtt1.setStatus("mandatory")


class _ElectricalCurrentProbeLocationAtt2_Type(Integer32):
    """Custom type electricalCurrentProbeLocationAtt2 based on Integer32"""
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
        *(("addInCard", 11),
          ("disk", 4),
          ("memoryModule", 8),
          ("motherboard", 7),
          ("other", 1),
          ("peripheralBay", 5),
          ("powerUnit", 10),
          ("processor", 3),
          ("processorModule", 9),
          ("sMBMaster", 6),
          ("unknown", 2))
    )


_ElectricalCurrentProbeLocationAtt2_Type.__name__ = "Integer32"
_ElectricalCurrentProbeLocationAtt2_Object = MibTableColumn
electricalCurrentProbeLocationAtt2 = _ElectricalCurrentProbeLocationAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 2),
    _ElectricalCurrentProbeLocationAtt2_Type()
)
electricalCurrentProbeLocationAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    electricalCurrentProbeLocationAtt2.setStatus("mandatory")
_ElectricalCurrentProbeDescriptionAtt3_Type = DmiDisplaystring
_ElectricalCurrentProbeDescriptionAtt3_Object = MibTableColumn
electricalCurrentProbeDescriptionAtt3 = _ElectricalCurrentProbeDescriptionAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 3),
    _ElectricalCurrentProbeDescriptionAtt3_Type()
)
electricalCurrentProbeDescriptionAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    electricalCurrentProbeDescriptionAtt3.setStatus("mandatory")


class _ElectricalCurrentStatusAtt4_Type(Integer32):
    """Custom type electricalCurrentStatusAtt4 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ElectricalCurrentStatusAtt4_Type.__name__ = "Integer32"
_ElectricalCurrentStatusAtt4_Object = MibTableColumn
electricalCurrentStatusAtt4 = _ElectricalCurrentStatusAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 4),
    _ElectricalCurrentStatusAtt4_Type()
)
electricalCurrentStatusAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    electricalCurrentStatusAtt4.setStatus("mandatory")
_ElectricalCurrentProbeReadingAtt5_Type = DmiInteger
_ElectricalCurrentProbeReadingAtt5_Object = MibTableColumn
electricalCurrentProbeReadingAtt5 = _ElectricalCurrentProbeReadingAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 5),
    _ElectricalCurrentProbeReadingAtt5_Type()
)
electricalCurrentProbeReadingAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    electricalCurrentProbeReadingAtt5.setStatus("mandatory")
_MonitoredElectricalCurrentNominalReadingAtt6_Type = DmiInteger
_MonitoredElectricalCurrentNominalReadingAtt6_Object = MibTableColumn
monitoredElectricalCurrentNominalReadingAtt6 = _MonitoredElectricalCurrentNominalReadingAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 6),
    _MonitoredElectricalCurrentNominalReadingAtt6_Type()
)
monitoredElectricalCurrentNominalReadingAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoredElectricalCurrentNominalReadingAtt6.setStatus("mandatory")
_MonitoredElectricalCurrentNormalMaximumAtt7_Type = DmiInteger
_MonitoredElectricalCurrentNormalMaximumAtt7_Object = MibTableColumn
monitoredElectricalCurrentNormalMaximumAtt7 = _MonitoredElectricalCurrentNormalMaximumAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 7),
    _MonitoredElectricalCurrentNormalMaximumAtt7_Type()
)
monitoredElectricalCurrentNormalMaximumAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoredElectricalCurrentNormalMaximumAtt7.setStatus("mandatory")
_MonitoredElectricalCurrentNormalMinimumAtt8_Type = DmiInteger
_MonitoredElectricalCurrentNormalMinimumAtt8_Object = MibTableColumn
monitoredElectricalCurrentNormalMinimumAtt8 = _MonitoredElectricalCurrentNormalMinimumAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 8),
    _MonitoredElectricalCurrentNormalMinimumAtt8_Type()
)
monitoredElectricalCurrentNormalMinimumAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitoredElectricalCurrentNormalMinimumAtt8.setStatus("mandatory")
_ElectricalCurrentProbeMaximumAtt9_Type = DmiInteger
_ElectricalCurrentProbeMaximumAtt9_Object = MibTableColumn
electricalCurrentProbeMaximumAtt9 = _ElectricalCurrentProbeMaximumAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 9),
    _ElectricalCurrentProbeMaximumAtt9_Type()
)
electricalCurrentProbeMaximumAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    electricalCurrentProbeMaximumAtt9.setStatus("mandatory")
_ElectricalCurrentProbeMinimumAtt10_Type = DmiInteger
_ElectricalCurrentProbeMinimumAtt10_Object = MibTableColumn
electricalCurrentProbeMinimumAtt10 = _ElectricalCurrentProbeMinimumAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 10),
    _ElectricalCurrentProbeMinimumAtt10_Type()
)
electricalCurrentProbeMinimumAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    electricalCurrentProbeMinimumAtt10.setStatus("mandatory")
_ElectricalCurrentReadingLowerThresholdNonCriticalAtt11_Type = DmiInteger
_ElectricalCurrentReadingLowerThresholdNonCriticalAtt11_Object = MibTableColumn
electricalCurrentReadingLowerThresholdNonCriticalAtt11 = _ElectricalCurrentReadingLowerThresholdNonCriticalAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 11),
    _ElectricalCurrentReadingLowerThresholdNonCriticalAtt11_Type()
)
electricalCurrentReadingLowerThresholdNonCriticalAtt11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalCurrentReadingLowerThresholdNonCriticalAtt11.setStatus("mandatory")
_ElectricalCurrentReadingUpperThresholdNonCriticalAtt12_Type = DmiInteger
_ElectricalCurrentReadingUpperThresholdNonCriticalAtt12_Object = MibTableColumn
electricalCurrentReadingUpperThresholdNonCriticalAtt12 = _ElectricalCurrentReadingUpperThresholdNonCriticalAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 12),
    _ElectricalCurrentReadingUpperThresholdNonCriticalAtt12_Type()
)
electricalCurrentReadingUpperThresholdNonCriticalAtt12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalCurrentReadingUpperThresholdNonCriticalAtt12.setStatus("mandatory")
_ElectricalCurrentReadingLowerThresholdCriticalAtt13_Type = DmiInteger
_ElectricalCurrentReadingLowerThresholdCriticalAtt13_Object = MibTableColumn
electricalCurrentReadingLowerThresholdCriticalAtt13 = _ElectricalCurrentReadingLowerThresholdCriticalAtt13_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 13),
    _ElectricalCurrentReadingLowerThresholdCriticalAtt13_Type()
)
electricalCurrentReadingLowerThresholdCriticalAtt13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalCurrentReadingLowerThresholdCriticalAtt13.setStatus("mandatory")
_CurrentReadingUpperThresholdCriticalAtt14_Type = DmiInteger
_CurrentReadingUpperThresholdCriticalAtt14_Object = MibTableColumn
currentReadingUpperThresholdCriticalAtt14 = _CurrentReadingUpperThresholdCriticalAtt14_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 14),
    _CurrentReadingUpperThresholdCriticalAtt14_Type()
)
currentReadingUpperThresholdCriticalAtt14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentReadingUpperThresholdCriticalAtt14.setStatus("mandatory")
_ElectricalCurrentReadingLowerThresholdNonRecoverabAtt15_Type = DmiInteger
_ElectricalCurrentReadingLowerThresholdNonRecoverabAtt15_Object = MibTableColumn
electricalCurrentReadingLowerThresholdNonRecoverabAtt15 = _ElectricalCurrentReadingLowerThresholdNonRecoverabAtt15_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 15),
    _ElectricalCurrentReadingLowerThresholdNonRecoverabAtt15_Type()
)
electricalCurrentReadingLowerThresholdNonRecoverabAtt15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalCurrentReadingLowerThresholdNonRecoverabAtt15.setStatus("mandatory")
_ElectricalCurrentReadingUpperThresholdNonRecoverabAtt16_Type = DmiInteger
_ElectricalCurrentReadingUpperThresholdNonRecoverabAtt16_Object = MibTableColumn
electricalCurrentReadingUpperThresholdNonRecoverabAtt16 = _ElectricalCurrentReadingUpperThresholdNonRecoverabAtt16_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 16),
    _ElectricalCurrentReadingUpperThresholdNonRecoverabAtt16_Type()
)
electricalCurrentReadingUpperThresholdNonRecoverabAtt16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalCurrentReadingUpperThresholdNonRecoverabAtt16.setStatus("mandatory")
_ElectricalCurrentProbeResolutionAtt17_Type = DmiInteger
_ElectricalCurrentProbeResolutionAtt17_Object = MibTableColumn
electricalCurrentProbeResolutionAtt17 = _ElectricalCurrentProbeResolutionAtt17_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 17),
    _ElectricalCurrentProbeResolutionAtt17_Type()
)
electricalCurrentProbeResolutionAtt17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalCurrentProbeResolutionAtt17.setStatus("mandatory")
_ElectricalCurrentProbeToleranceAtt18_Type = DmiInteger
_ElectricalCurrentProbeToleranceAtt18_Object = MibTableColumn
electricalCurrentProbeToleranceAtt18 = _ElectricalCurrentProbeToleranceAtt18_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 18),
    _ElectricalCurrentProbeToleranceAtt18_Type()
)
electricalCurrentProbeToleranceAtt18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalCurrentProbeToleranceAtt18.setStatus("mandatory")
_ElectricalCurrentProbeAccuracyAtt19_Type = DmiInteger
_ElectricalCurrentProbeAccuracyAtt19_Object = MibTableColumn
electricalCurrentProbeAccuracyAtt19 = _ElectricalCurrentProbeAccuracyAtt19_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 19),
    _ElectricalCurrentProbeAccuracyAtt19_Type()
)
electricalCurrentProbeAccuracyAtt19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    electricalCurrentProbeAccuracyAtt19.setStatus("mandatory")
_FRUGroupIndexAtt20_Type = DmiInteger
_FRUGroupIndexAtt20_Object = MibScalar
fRUGroupIndexAtt20 = _FRUGroupIndexAtt20_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 20),
    _FRUGroupIndexAtt20_Type()
)
fRUGroupIndexAtt20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt20.setStatus("mandatory")
_OperationalGroupIndexAtt21_Type = DmiInteger
_OperationalGroupIndexAtt21_Object = MibScalar
operationalGroupIndexAtt21 = _OperationalGroupIndexAtt21_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 1, 21),
    _OperationalGroupIndexAtt21_Type()
)
operationalGroupIndexAtt21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt21.setStatus("mandatory")


class _DMTFElectricalCurrentProbeEvSys_Type(Integer32):
    """Custom type dMTFElectricalCurrentProbeEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFElectricalCurrentProbeEvSys_Type.__name__ = "Integer32"
_DMTFElectricalCurrentProbeEvSys_Object = MibScalar
dMTFElectricalCurrentProbeEvSys = _DMTFElectricalCurrentProbeEvSys_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 6),
    _DMTFElectricalCurrentProbeEvSys_Type()
)
dMTFElectricalCurrentProbeEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFElectricalCurrentProbeEvSys.setStatus("mandatory")


class _DMTFElectricalCurrentProbeEvSub_Type(Integer32):
    """Custom type dMTFElectricalCurrentProbeEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFElectricalCurrentProbeEvSub_Type.__name__ = "Integer32"
_DMTFElectricalCurrentProbeEvSub_Object = MibScalar
dMTFElectricalCurrentProbeEvSub = _DMTFElectricalCurrentProbeEvSub_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 7),
    _DMTFElectricalCurrentProbeEvSub_Type()
)
dMTFElectricalCurrentProbeEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFElectricalCurrentProbeEvSub.setStatus("mandatory")
_DMTFPhysicalContainerGlobalTableTable_Object = MibTable
dMTFPhysicalContainerGlobalTableTable = _DMTFPhysicalContainerGlobalTableTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63)
)
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableTable.setStatus("mandatory")
_DMTFPhysicalContainerGlobalTableEntry_Object = MibTableRow
dMTFPhysicalContainerGlobalTableEntry = _DMTFPhysicalContainerGlobalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1)
)
dMTFPhysicalContainerGlobalTableEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "containerIndexAtt9"),
)
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEntry.setStatus("mandatory")


class _DMTFPhysicalContainerGlobalTableState_Type(Integer32):
    """Custom type dMTFPhysicalContainerGlobalTableState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFPhysicalContainerGlobalTableState_Type.__name__ = "Integer32"
_DMTFPhysicalContainerGlobalTableState_Object = MibTableColumn
dMTFPhysicalContainerGlobalTableState = _DMTFPhysicalContainerGlobalTableState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 0),
    _DMTFPhysicalContainerGlobalTableState_Type()
)
dMTFPhysicalContainerGlobalTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableState.setStatus("mandatory")


class _ContainerOrChassisTypeAtt1_Type(Integer32):
    """Custom type containerOrChassisTypeAtt1 based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("allInOne", 13),
          ("busExpansionChassis", 20),
          ("desktop", 3),
          ("dockingStation", 12),
          ("expansionChassis", 18),
          ("handHeld", 11),
          ("lapTop", 9),
          ("lowProfileDesktop", 4),
          ("lunchBox", 16),
          ("mainSystemChassis", 17),
          ("miniTower", 6),
          ("notebook", 10),
          ("other", 1),
          ("peripheralChassis", 21),
          ("pizzaBox", 5),
          ("portable", 8),
          ("rAIDChassis", 22),
          ("rackMountChassis", 23),
          ("sealedCasePC", 24),
          ("spaceSaving", 15),
          ("subChassis", 19),
          ("subNotebook", 14),
          ("tower", 7),
          ("unknown", 2))
    )


_ContainerOrChassisTypeAtt1_Type.__name__ = "Integer32"
_ContainerOrChassisTypeAtt1_Object = MibTableColumn
containerOrChassisTypeAtt1 = _ContainerOrChassisTypeAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 1),
    _ContainerOrChassisTypeAtt1_Type()
)
containerOrChassisTypeAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    containerOrChassisTypeAtt1.setStatus("mandatory")
_AssetTagAtt2_Type = DmiDisplaystring
_AssetTagAtt2_Object = MibTableColumn
assetTagAtt2 = _AssetTagAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 2),
    _AssetTagAtt2_Type()
)
assetTagAtt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assetTagAtt2.setStatus("mandatory")


class _ChassisLockPresentAtt3_Type(Integer32):
    """Custom type chassisLockPresentAtt3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ChassisLockPresentAtt3_Type.__name__ = "Integer32"
_ChassisLockPresentAtt3_Object = MibTableColumn
chassisLockPresentAtt3 = _ChassisLockPresentAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 3),
    _ChassisLockPresentAtt3_Type()
)
chassisLockPresentAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLockPresentAtt3.setStatus("mandatory")


class _BootupStateAtt4_Type(Integer32):
    """Custom type bootupStateAtt4 based on Integer32"""
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
        *(("critical", 5),
          ("nonRecoverable-1", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2),
          ("warning", 4))
    )


_BootupStateAtt4_Type.__name__ = "Integer32"
_BootupStateAtt4_Object = MibTableColumn
bootupStateAtt4 = _BootupStateAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 4),
    _BootupStateAtt4_Type()
)
bootupStateAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootupStateAtt4.setStatus("mandatory")


class _PowerStateAtt5_Type(Integer32):
    """Custom type powerStateAtt5 based on Integer32"""
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
        *(("critical", 5),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2),
          ("warning", 4))
    )


_PowerStateAtt5_Type.__name__ = "Integer32"
_PowerStateAtt5_Object = MibTableColumn
powerStateAtt5 = _PowerStateAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 5),
    _PowerStateAtt5_Type()
)
powerStateAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStateAtt5.setStatus("mandatory")


class _ThermalStateAtt6_Type(Integer32):
    """Custom type thermalStateAtt6 based on Integer32"""
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
        *(("critical", 5),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2),
          ("warning", 4))
    )


_ThermalStateAtt6_Type.__name__ = "Integer32"
_ThermalStateAtt6_Object = MibTableColumn
thermalStateAtt6 = _ThermalStateAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 6),
    _ThermalStateAtt6_Type()
)
thermalStateAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thermalStateAtt6.setStatus("mandatory")
_FRUGroupIndexAtt7_Type = DmiInteger
_FRUGroupIndexAtt7_Object = MibTableColumn
fRUGroupIndexAtt7 = _FRUGroupIndexAtt7_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 7),
    _FRUGroupIndexAtt7_Type()
)
fRUGroupIndexAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndexAtt7.setStatus("mandatory")
_OperationalGroupIndexAtt8_Type = DmiInteger
_OperationalGroupIndexAtt8_Object = MibTableColumn
operationalGroupIndexAtt8 = _OperationalGroupIndexAtt8_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 8),
    _OperationalGroupIndexAtt8_Type()
)
operationalGroupIndexAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndexAtt8.setStatus("mandatory")
_ContainerIndexAtt9_Type = DmiInteger
_ContainerIndexAtt9_Object = MibTableColumn
containerIndexAtt9 = _ContainerIndexAtt9_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 9),
    _ContainerIndexAtt9_Type()
)
containerIndexAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    containerIndexAtt9.setStatus("mandatory")
_ContainerNameAtt10_Type = DmiDisplaystring
_ContainerNameAtt10_Object = MibTableColumn
containerNameAtt10 = _ContainerNameAtt10_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 10),
    _ContainerNameAtt10_Type()
)
containerNameAtt10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    containerNameAtt10.setStatus("mandatory")
_ContainerLocationAtt11_Type = DmiDisplaystring
_ContainerLocationAtt11_Object = MibTableColumn
containerLocationAtt11 = _ContainerLocationAtt11_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 11),
    _ContainerLocationAtt11_Type()
)
containerLocationAtt11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    containerLocationAtt11.setStatus("mandatory")


class _ContainerSecurityStatusAtt12_Type(Integer32):
    """Custom type containerSecurityStatusAtt12 based on Integer32"""
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
        *(("containerSecurityBreachAttempted", 4),
          ("containerSecurityBreached", 5),
          ("noSecurityBreachDetected", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ContainerSecurityStatusAtt12_Type.__name__ = "Integer32"
_ContainerSecurityStatusAtt12_Object = MibTableColumn
containerSecurityStatusAtt12 = _ContainerSecurityStatusAtt12_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 1, 12),
    _ContainerSecurityStatusAtt12_Type()
)
containerSecurityStatusAtt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    containerSecurityStatusAtt12.setStatus("mandatory")


class _DMTFPhysicalContainerGlobalTableEvSys_Type(Integer32):
    """Custom type dMTFPhysicalContainerGlobalTableEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFPhysicalContainerGlobalTableEvSys_Type.__name__ = "Integer32"
_DMTFPhysicalContainerGlobalTableEvSys_Object = MibScalar
dMTFPhysicalContainerGlobalTableEvSys = _DMTFPhysicalContainerGlobalTableEvSys_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 6),
    _DMTFPhysicalContainerGlobalTableEvSys_Type()
)
dMTFPhysicalContainerGlobalTableEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEvSys.setStatus("mandatory")


class _DMTFPhysicalContainerGlobalTableEvSub_Type(Integer32):
    """Custom type dMTFPhysicalContainerGlobalTableEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DMTFPhysicalContainerGlobalTableEvSub_Type.__name__ = "Integer32"
_DMTFPhysicalContainerGlobalTableEvSub_Object = MibScalar
dMTFPhysicalContainerGlobalTableEvSub = _DMTFPhysicalContainerGlobalTableEvSub_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 7),
    _DMTFPhysicalContainerGlobalTableEvSub_Type()
)
dMTFPhysicalContainerGlobalTableEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEvSub.setStatus("mandatory")
_DMTFPowerUnitGlobalTableTable_Object = MibTable
dMTFPowerUnitGlobalTableTable = _DMTFPowerUnitGlobalTableTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 66)
)
if mibBuilder.loadTexts:
    dMTFPowerUnitGlobalTableTable.setStatus("mandatory")
_DMTFPowerUnitGlobalTableEntry_Object = MibTableRow
dMTFPowerUnitGlobalTableEntry = _DMTFPowerUnitGlobalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 66, 1)
)
dMTFPowerUnitGlobalTableEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "powerUnitIndexAtt1"),
)
if mibBuilder.loadTexts:
    dMTFPowerUnitGlobalTableEntry.setStatus("mandatory")


class _DMTFPowerUnitGlobalTableState_Type(Integer32):
    """Custom type dMTFPowerUnitGlobalTableState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DMTFPowerUnitGlobalTableState_Type.__name__ = "Integer32"
_DMTFPowerUnitGlobalTableState_Object = MibTableColumn
dMTFPowerUnitGlobalTableState = _DMTFPowerUnitGlobalTableState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 66, 1, 0),
    _DMTFPowerUnitGlobalTableState_Type()
)
dMTFPowerUnitGlobalTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMTFPowerUnitGlobalTableState.setStatus("mandatory")
_PowerUnitIndexAtt1_Type = DmiInteger
_PowerUnitIndexAtt1_Object = MibTableColumn
powerUnitIndexAtt1 = _PowerUnitIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 66, 1, 1),
    _PowerUnitIndexAtt1_Type()
)
powerUnitIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitIndexAtt1.setStatus("mandatory")


class _PowerUnitRedundancyStatusAtt2_Type(Integer32):
    """Custom type powerUnitRedundancyStatusAtt2 based on Integer32"""
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
        *(("degradedRedundancy", 6),
          ("fullyRedundant-1", 5),
          ("notApplicableUnitNotRedundant-1", 3),
          ("offline", 4),
          ("other", 1),
          ("redundancyLost", 7),
          ("unknown", 2))
    )


_PowerUnitRedundancyStatusAtt2_Type.__name__ = "Integer32"
_PowerUnitRedundancyStatusAtt2_Object = MibTableColumn
powerUnitRedundancyStatusAtt2 = _PowerUnitRedundancyStatusAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 66, 1, 2),
    _PowerUnitRedundancyStatusAtt2_Type()
)
powerUnitRedundancyStatusAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitRedundancyStatusAtt2.setStatus("mandatory")
_DmtfDynOids_ObjectIdentity = ObjectIdentity
dmtfDynOids = _DmtfDynOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3)
)
_DmiDynOid386845712_ObjectIdentity = ObjectIdentity
dmiDynOid386845712 = _DmiDynOid386845712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3, 386845712)
)
_DmiDynOid73111109_ObjectIdentity = ObjectIdentity
dmiDynOid73111109 = _DmiDynOid73111109_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3, 386845712, 73111109)
)
_DmiDynOid3922453424_ObjectIdentity = ObjectIdentity
dmiDynOid3922453424 = _DmiDynOid3922453424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3, 386845712, 73111109, 3922453424)
)
_INTELMIFTOMIBTable_Object = MibTable
iNTELMIFTOMIBTable = _INTELMIFTOMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 3, 386845712, 73111109, 3922453424, 1737102472)
)
if mibBuilder.loadTexts:
    iNTELMIFTOMIBTable.setStatus("mandatory")
_INTELMIFTOMIBEntry_Object = MibTableRow
iNTELMIFTOMIBEntry = _INTELMIFTOMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 3, 386845712, 73111109, 3922453424, 1737102472, 1)
)
iNTELMIFTOMIBEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    iNTELMIFTOMIBEntry.setStatus("mandatory")
_DellBaseBoardMIBAtt1_Type = DmiDisplaystring
_DellBaseBoardMIBAtt1_Object = MibTableColumn
dellBaseBoardMIBAtt1 = _DellBaseBoardMIBAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 3, 386845712, 73111109, 3922453424, 1737102472, 1, 1),
    _DellBaseBoardMIBAtt1_Type()
)
dellBaseBoardMIBAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellBaseBoardMIBAtt1.setStatus("mandatory")
_MIBOIDAtt2_Type = DmiDisplaystring
_MIBOIDAtt2_Object = MibTableColumn
mIBOIDAtt2 = _MIBOIDAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 3, 386845712, 73111109, 3922453424, 1737102472, 1, 2),
    _MIBOIDAtt2_Type()
)
mIBOIDAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIBOIDAtt2.setStatus("mandatory")
_DisableTrapsAtt3_Type = DmiInteger
_DisableTrapsAtt3_Object = MibTableColumn
disableTrapsAtt3 = _DisableTrapsAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 3, 386845712, 73111109, 3922453424, 1737102472, 1, 3),
    _DisableTrapsAtt3_Type()
)
disableTrapsAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disableTrapsAtt3.setStatus("mandatory")
_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server2_ObjectIdentity = ObjectIdentity
server2 = _Server2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10891)
)
_DellTemperatureProbeTable_Object = MibTable
dellTemperatureProbeTable = _DellTemperatureProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300)
)
if mibBuilder.loadTexts:
    dellTemperatureProbeTable.setStatus("mandatory")
_DellTemperatureProbeEntry_Object = MibTableRow
dellTemperatureProbeEntry = _DellTemperatureProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1)
)
dellTemperatureProbeEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "tempParentIndexAtt1"),
    (0, "BASEBRDD-MIB-MIB", "tempIndexAtt2"),
)
if mibBuilder.loadTexts:
    dellTemperatureProbeEntry.setStatus("mandatory")


class _DellTemperatureProbeState_Type(Integer32):
    """Custom type dellTemperatureProbeState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellTemperatureProbeState_Type.__name__ = "Integer32"
_DellTemperatureProbeState_Object = MibTableColumn
dellTemperatureProbeState = _DellTemperatureProbeState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 0),
    _DellTemperatureProbeState_Type()
)
dellTemperatureProbeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellTemperatureProbeState.setStatus("mandatory")
_TempParentIndexAtt1_Type = DmiInteger
_TempParentIndexAtt1_Object = MibTableColumn
tempParentIndexAtt1 = _TempParentIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 1),
    _TempParentIndexAtt1_Type()
)
tempParentIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempParentIndexAtt1.setStatus("mandatory")
_TempIndexAtt2_Type = DmiInteger
_TempIndexAtt2_Object = MibTableColumn
tempIndexAtt2 = _TempIndexAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 2),
    _TempIndexAtt2_Type()
)
tempIndexAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndexAtt2.setStatus("mandatory")


class _TempTypeAtt3_Type(Integer32):
    """Custom type tempTypeAtt3 based on Integer32"""
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
        *(("backplane", 6),
          ("eSM", 5),
          ("harrierBackplane", 7),
          ("other", 1),
          ("tMC", 3),
          ("tVM", 4),
          ("unknown", 2))
    )


_TempTypeAtt3_Type.__name__ = "Integer32"
_TempTypeAtt3_Object = MibTableColumn
tempTypeAtt3 = _TempTypeAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 3),
    _TempTypeAtt3_Type()
)
tempTypeAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempTypeAtt3.setStatus("mandatory")


class _TempStatusAtt4_Type(Integer32):
    """Custom type tempStatusAtt4 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_TempStatusAtt4_Type.__name__ = "Integer32"
_TempStatusAtt4_Object = MibTableColumn
tempStatusAtt4 = _TempStatusAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 4),
    _TempStatusAtt4_Type()
)
tempStatusAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempStatusAtt4.setStatus("mandatory")
_TempReadingAtt5_Type = DmiInteger
_TempReadingAtt5_Object = MibTableColumn
tempReadingAtt5 = _TempReadingAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 5),
    _TempReadingAtt5_Type()
)
tempReadingAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempReadingAtt5.setStatus("mandatory")
_TempMinWarnAtt6_Type = DmiDisplaystring
_TempMinWarnAtt6_Object = MibTableColumn
tempMinWarnAtt6 = _TempMinWarnAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 6),
    _TempMinWarnAtt6_Type()
)
tempMinWarnAtt6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempMinWarnAtt6.setStatus("mandatory")
_TempMaxWarnAtt7_Type = DmiDisplaystring
_TempMaxWarnAtt7_Object = MibTableColumn
tempMaxWarnAtt7 = _TempMaxWarnAtt7_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 7),
    _TempMaxWarnAtt7_Type()
)
tempMaxWarnAtt7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempMaxWarnAtt7.setStatus("mandatory")
_TempMinFailAtt8_Type = DmiInteger
_TempMinFailAtt8_Object = MibTableColumn
tempMinFailAtt8 = _TempMinFailAtt8_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 8),
    _TempMinFailAtt8_Type()
)
tempMinFailAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinFailAtt8.setStatus("mandatory")
_TempMaxFailAtt9_Type = DmiInteger
_TempMaxFailAtt9_Object = MibTableColumn
tempMaxFailAtt9 = _TempMaxFailAtt9_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 9),
    _TempMaxFailAtt9_Type()
)
tempMaxFailAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaxFailAtt9.setStatus("mandatory")
_TempLocationAtt10_Type = DmiDisplaystring
_TempLocationAtt10_Object = MibTableColumn
tempLocationAtt10 = _TempLocationAtt10_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 1, 10),
    _TempLocationAtt10_Type()
)
tempLocationAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempLocationAtt10.setStatus("mandatory")


class _DellTemperatureProbeEvSys_Type(Integer32):
    """Custom type dellTemperatureProbeEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellTemperatureProbeEvSys_Type.__name__ = "Integer32"
_DellTemperatureProbeEvSys_Object = MibScalar
dellTemperatureProbeEvSys = _DellTemperatureProbeEvSys_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 6),
    _DellTemperatureProbeEvSys_Type()
)
dellTemperatureProbeEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellTemperatureProbeEvSys.setStatus("mandatory")


class _DellTemperatureProbeEvSub_Type(Integer32):
    """Custom type dellTemperatureProbeEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellTemperatureProbeEvSub_Type.__name__ = "Integer32"
_DellTemperatureProbeEvSub_Object = MibScalar
dellTemperatureProbeEvSub = _DellTemperatureProbeEvSub_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 7),
    _DellTemperatureProbeEvSub_Type()
)
dellTemperatureProbeEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellTemperatureProbeEvSub.setStatus("mandatory")


class _DellTemperatureProbeEvSol_Type(Integer32):
    """Custom type dellTemperatureProbeEvSol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2))
    )


_DellTemperatureProbeEvSol_Type.__name__ = "Integer32"
_DellTemperatureProbeEvSol_Object = MibScalar
dellTemperatureProbeEvSol = _DellTemperatureProbeEvSol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 8),
    _DellTemperatureProbeEvSol_Type()
)
dellTemperatureProbeEvSol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellTemperatureProbeEvSol.setStatus("mandatory")
_DellFanSensorTable_Object = MibTable
dellFanSensorTable = _DellFanSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301)
)
if mibBuilder.loadTexts:
    dellFanSensorTable.setStatus("mandatory")
_DellFanSensorEntry_Object = MibTableRow
dellFanSensorEntry = _DellFanSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1)
)
dellFanSensorEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "fansParentIndexAtt1"),
    (0, "BASEBRDD-MIB-MIB", "fansIndexAtt2"),
)
if mibBuilder.loadTexts:
    dellFanSensorEntry.setStatus("mandatory")


class _DellFanSensorState_Type(Integer32):
    """Custom type dellFanSensorState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellFanSensorState_Type.__name__ = "Integer32"
_DellFanSensorState_Object = MibTableColumn
dellFanSensorState = _DellFanSensorState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 0),
    _DellFanSensorState_Type()
)
dellFanSensorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellFanSensorState.setStatus("mandatory")
_FansParentIndexAtt1_Type = DmiInteger
_FansParentIndexAtt1_Object = MibTableColumn
fansParentIndexAtt1 = _FansParentIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 1),
    _FansParentIndexAtt1_Type()
)
fansParentIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansParentIndexAtt1.setStatus("mandatory")
_FansIndexAtt2_Type = DmiInteger
_FansIndexAtt2_Object = MibTableColumn
fansIndexAtt2 = _FansIndexAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 2),
    _FansIndexAtt2_Type()
)
fansIndexAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansIndexAtt2.setStatus("mandatory")


class _FansTypeAtt3_Type(Integer32):
    """Custom type fansTypeAtt3 based on Integer32"""
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
        *(("boolean", 3),
          ("other", 1),
          ("rPM", 4),
          ("unknown", 2))
    )


_FansTypeAtt3_Type.__name__ = "Integer32"
_FansTypeAtt3_Object = MibTableColumn
fansTypeAtt3 = _FansTypeAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 3),
    _FansTypeAtt3_Type()
)
fansTypeAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansTypeAtt3.setStatus("mandatory")


class _FansStatusAtt4_Type(Integer32):
    """Custom type fansStatusAtt4 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_FansStatusAtt4_Type.__name__ = "Integer32"
_FansStatusAtt4_Object = MibTableColumn
fansStatusAtt4 = _FansStatusAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 4),
    _FansStatusAtt4_Type()
)
fansStatusAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansStatusAtt4.setStatus("mandatory")
_FansReadingAtt5_Type = DmiInteger
_FansReadingAtt5_Object = MibTableColumn
fansReadingAtt5 = _FansReadingAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 5),
    _FansReadingAtt5_Type()
)
fansReadingAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansReadingAtt5.setStatus("mandatory")
_FansWarningMinAtt6_Type = DmiDisplaystring
_FansWarningMinAtt6_Object = MibTableColumn
fansWarningMinAtt6 = _FansWarningMinAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 6),
    _FansWarningMinAtt6_Type()
)
fansWarningMinAtt6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fansWarningMinAtt6.setStatus("mandatory")
_FansMaxWarnAtt7_Type = DmiDisplaystring
_FansMaxWarnAtt7_Object = MibTableColumn
fansMaxWarnAtt7 = _FansMaxWarnAtt7_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 7),
    _FansMaxWarnAtt7_Type()
)
fansMaxWarnAtt7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fansMaxWarnAtt7.setStatus("mandatory")
_FansMinFailAtt8_Type = DmiInteger
_FansMinFailAtt8_Object = MibTableColumn
fansMinFailAtt8 = _FansMinFailAtt8_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 8),
    _FansMinFailAtt8_Type()
)
fansMinFailAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansMinFailAtt8.setStatus("mandatory")
_FansMaxFailAtt9_Type = DmiInteger
_FansMaxFailAtt9_Object = MibTableColumn
fansMaxFailAtt9 = _FansMaxFailAtt9_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 9),
    _FansMaxFailAtt9_Type()
)
fansMaxFailAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansMaxFailAtt9.setStatus("mandatory")
_FansLocationAtt10_Type = DmiDisplaystring
_FansLocationAtt10_Object = MibTableColumn
fansLocationAtt10 = _FansLocationAtt10_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 1, 10),
    _FansLocationAtt10_Type()
)
fansLocationAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fansLocationAtt10.setStatus("mandatory")


class _DellFanSensorEvSys_Type(Integer32):
    """Custom type dellFanSensorEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellFanSensorEvSys_Type.__name__ = "Integer32"
_DellFanSensorEvSys_Object = MibScalar
dellFanSensorEvSys = _DellFanSensorEvSys_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 6),
    _DellFanSensorEvSys_Type()
)
dellFanSensorEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellFanSensorEvSys.setStatus("mandatory")


class _DellFanSensorEvSub_Type(Integer32):
    """Custom type dellFanSensorEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellFanSensorEvSub_Type.__name__ = "Integer32"
_DellFanSensorEvSub_Object = MibScalar
dellFanSensorEvSub = _DellFanSensorEvSub_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 7),
    _DellFanSensorEvSub_Type()
)
dellFanSensorEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellFanSensorEvSub.setStatus("mandatory")


class _DellFanSensorEvSol_Type(Integer32):
    """Custom type dellFanSensorEvSol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2))
    )


_DellFanSensorEvSol_Type.__name__ = "Integer32"
_DellFanSensorEvSol_Object = MibScalar
dellFanSensorEvSol = _DellFanSensorEvSol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 8),
    _DellFanSensorEvSol_Type()
)
dellFanSensorEvSol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellFanSensorEvSol.setStatus("mandatory")
_DellVoltageProbeTable_Object = MibTable
dellVoltageProbeTable = _DellVoltageProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302)
)
if mibBuilder.loadTexts:
    dellVoltageProbeTable.setStatus("mandatory")
_DellVoltageProbeEntry_Object = MibTableRow
dellVoltageProbeEntry = _DellVoltageProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1)
)
dellVoltageProbeEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "voltParentIndexAtt1"),
    (0, "BASEBRDD-MIB-MIB", "voltIndexAtt2"),
)
if mibBuilder.loadTexts:
    dellVoltageProbeEntry.setStatus("mandatory")


class _DellVoltageProbeState_Type(Integer32):
    """Custom type dellVoltageProbeState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellVoltageProbeState_Type.__name__ = "Integer32"
_DellVoltageProbeState_Object = MibTableColumn
dellVoltageProbeState = _DellVoltageProbeState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 0),
    _DellVoltageProbeState_Type()
)
dellVoltageProbeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellVoltageProbeState.setStatus("mandatory")
_VoltParentIndexAtt1_Type = DmiInteger
_VoltParentIndexAtt1_Object = MibTableColumn
voltParentIndexAtt1 = _VoltParentIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 1),
    _VoltParentIndexAtt1_Type()
)
voltParentIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltParentIndexAtt1.setStatus("mandatory")
_VoltIndexAtt2_Type = DmiInteger
_VoltIndexAtt2_Object = MibTableColumn
voltIndexAtt2 = _VoltIndexAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 2),
    _VoltIndexAtt2_Type()
)
voltIndexAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltIndexAtt2.setStatus("mandatory")


class _VoltTypeAtt3_Type(Integer32):
    """Custom type voltTypeAtt3 based on Integer32"""
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
        *(("core", 10),
          ("other", 1),
          ("unknown", 2),
          ("v12", 7),
          ("v12-1", 8),
          ("v15", 9),
          ("v33", 3),
          ("v33-1", 4),
          ("v5", 5),
          ("v5-1", 6))
    )


_VoltTypeAtt3_Type.__name__ = "Integer32"
_VoltTypeAtt3_Object = MibTableColumn
voltTypeAtt3 = _VoltTypeAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 3),
    _VoltTypeAtt3_Type()
)
voltTypeAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltTypeAtt3.setStatus("mandatory")


class _VoltStatusAtt4_Type(Integer32):
    """Custom type voltStatusAtt4 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_VoltStatusAtt4_Type.__name__ = "Integer32"
_VoltStatusAtt4_Object = MibTableColumn
voltStatusAtt4 = _VoltStatusAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 4),
    _VoltStatusAtt4_Type()
)
voltStatusAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltStatusAtt4.setStatus("mandatory")
_VoltReadingAtt5_Type = DmiInteger
_VoltReadingAtt5_Object = MibTableColumn
voltReadingAtt5 = _VoltReadingAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 5),
    _VoltReadingAtt5_Type()
)
voltReadingAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltReadingAtt5.setStatus("mandatory")
_VoltMinWarnAtt6_Type = DmiDisplaystring
_VoltMinWarnAtt6_Object = MibTableColumn
voltMinWarnAtt6 = _VoltMinWarnAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 6),
    _VoltMinWarnAtt6_Type()
)
voltMinWarnAtt6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltMinWarnAtt6.setStatus("mandatory")
_VoltMaxWarnAtt7_Type = DmiDisplaystring
_VoltMaxWarnAtt7_Object = MibTableColumn
voltMaxWarnAtt7 = _VoltMaxWarnAtt7_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 7),
    _VoltMaxWarnAtt7_Type()
)
voltMaxWarnAtt7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltMaxWarnAtt7.setStatus("mandatory")
_VoltMinFailAtt8_Type = DmiInteger
_VoltMinFailAtt8_Object = MibTableColumn
voltMinFailAtt8 = _VoltMinFailAtt8_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 8),
    _VoltMinFailAtt8_Type()
)
voltMinFailAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltMinFailAtt8.setStatus("mandatory")
_VoltMaxFailAtt9_Type = DmiInteger
_VoltMaxFailAtt9_Object = MibTableColumn
voltMaxFailAtt9 = _VoltMaxFailAtt9_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 9),
    _VoltMaxFailAtt9_Type()
)
voltMaxFailAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltMaxFailAtt9.setStatus("mandatory")
_VoltLocationAtt10_Type = DmiDisplaystring
_VoltLocationAtt10_Object = MibTableColumn
voltLocationAtt10 = _VoltLocationAtt10_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 1, 10),
    _VoltLocationAtt10_Type()
)
voltLocationAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltLocationAtt10.setStatus("mandatory")


class _DellVoltageProbeEvSys_Type(Integer32):
    """Custom type dellVoltageProbeEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellVoltageProbeEvSys_Type.__name__ = "Integer32"
_DellVoltageProbeEvSys_Object = MibScalar
dellVoltageProbeEvSys = _DellVoltageProbeEvSys_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 6),
    _DellVoltageProbeEvSys_Type()
)
dellVoltageProbeEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellVoltageProbeEvSys.setStatus("mandatory")


class _DellVoltageProbeEvSub_Type(Integer32):
    """Custom type dellVoltageProbeEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellVoltageProbeEvSub_Type.__name__ = "Integer32"
_DellVoltageProbeEvSub_Object = MibScalar
dellVoltageProbeEvSub = _DellVoltageProbeEvSub_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 7),
    _DellVoltageProbeEvSub_Type()
)
dellVoltageProbeEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellVoltageProbeEvSub.setStatus("mandatory")


class _DellVoltageProbeEvSol_Type(Integer32):
    """Custom type dellVoltageProbeEvSol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2))
    )


_DellVoltageProbeEvSol_Type.__name__ = "Integer32"
_DellVoltageProbeEvSol_Object = MibScalar
dellVoltageProbeEvSol = _DellVoltageProbeEvSol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 8),
    _DellVoltageProbeEvSol_Type()
)
dellVoltageProbeEvSol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellVoltageProbeEvSol.setStatus("mandatory")
_DellCurrentProbeTable_Object = MibTable
dellCurrentProbeTable = _DellCurrentProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303)
)
if mibBuilder.loadTexts:
    dellCurrentProbeTable.setStatus("mandatory")
_DellCurrentProbeEntry_Object = MibTableRow
dellCurrentProbeEntry = _DellCurrentProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1)
)
dellCurrentProbeEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "ampParentIndexAtt1"),
    (0, "BASEBRDD-MIB-MIB", "ampIndexAtt2"),
)
if mibBuilder.loadTexts:
    dellCurrentProbeEntry.setStatus("mandatory")


class _DellCurrentProbeState_Type(Integer32):
    """Custom type dellCurrentProbeState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellCurrentProbeState_Type.__name__ = "Integer32"
_DellCurrentProbeState_Object = MibTableColumn
dellCurrentProbeState = _DellCurrentProbeState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 0),
    _DellCurrentProbeState_Type()
)
dellCurrentProbeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellCurrentProbeState.setStatus("mandatory")
_AmpParentIndexAtt1_Type = DmiInteger
_AmpParentIndexAtt1_Object = MibTableColumn
ampParentIndexAtt1 = _AmpParentIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 1),
    _AmpParentIndexAtt1_Type()
)
ampParentIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampParentIndexAtt1.setStatus("mandatory")
_AmpIndexAtt2_Type = DmiInteger
_AmpIndexAtt2_Object = MibTableColumn
ampIndexAtt2 = _AmpIndexAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 2),
    _AmpIndexAtt2_Type()
)
ampIndexAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampIndexAtt2.setStatus("mandatory")


class _AmpTypeAtt3_Type(Integer32):
    """Custom type ampTypeAtt3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("v12", 8),
          ("v33", 4),
          ("v5", 6))
    )


_AmpTypeAtt3_Type.__name__ = "Integer32"
_AmpTypeAtt3_Object = MibTableColumn
ampTypeAtt3 = _AmpTypeAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 3),
    _AmpTypeAtt3_Type()
)
ampTypeAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampTypeAtt3.setStatus("mandatory")


class _AmpStatusAtt4_Type(Integer32):
    """Custom type ampStatusAtt4 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_AmpStatusAtt4_Type.__name__ = "Integer32"
_AmpStatusAtt4_Object = MibTableColumn
ampStatusAtt4 = _AmpStatusAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 4),
    _AmpStatusAtt4_Type()
)
ampStatusAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampStatusAtt4.setStatus("mandatory")
_AmpReadingAtt5_Type = DmiInteger
_AmpReadingAtt5_Object = MibTableColumn
ampReadingAtt5 = _AmpReadingAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 5),
    _AmpReadingAtt5_Type()
)
ampReadingAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampReadingAtt5.setStatus("mandatory")
_AmpMinWarnAtt6_Type = DmiDisplaystring
_AmpMinWarnAtt6_Object = MibTableColumn
ampMinWarnAtt6 = _AmpMinWarnAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 6),
    _AmpMinWarnAtt6_Type()
)
ampMinWarnAtt6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ampMinWarnAtt6.setStatus("mandatory")
_AmpMaxWarnAtt7_Type = DmiDisplaystring
_AmpMaxWarnAtt7_Object = MibTableColumn
ampMaxWarnAtt7 = _AmpMaxWarnAtt7_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 7),
    _AmpMaxWarnAtt7_Type()
)
ampMaxWarnAtt7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ampMaxWarnAtt7.setStatus("mandatory")
_AmpMinFailAtt8_Type = DmiInteger
_AmpMinFailAtt8_Object = MibTableColumn
ampMinFailAtt8 = _AmpMinFailAtt8_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 8),
    _AmpMinFailAtt8_Type()
)
ampMinFailAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampMinFailAtt8.setStatus("mandatory")
_AmpMaxFailAtt9_Type = DmiInteger
_AmpMaxFailAtt9_Object = MibTableColumn
ampMaxFailAtt9 = _AmpMaxFailAtt9_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 9),
    _AmpMaxFailAtt9_Type()
)
ampMaxFailAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampMaxFailAtt9.setStatus("mandatory")
_AmpLocationAtt10_Type = DmiDisplaystring
_AmpLocationAtt10_Object = MibTableColumn
ampLocationAtt10 = _AmpLocationAtt10_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 1, 10),
    _AmpLocationAtt10_Type()
)
ampLocationAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampLocationAtt10.setStatus("mandatory")


class _DellCurrentProbeEvSys_Type(Integer32):
    """Custom type dellCurrentProbeEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellCurrentProbeEvSys_Type.__name__ = "Integer32"
_DellCurrentProbeEvSys_Object = MibScalar
dellCurrentProbeEvSys = _DellCurrentProbeEvSys_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 6),
    _DellCurrentProbeEvSys_Type()
)
dellCurrentProbeEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellCurrentProbeEvSys.setStatus("mandatory")


class _DellCurrentProbeEvSub_Type(Integer32):
    """Custom type dellCurrentProbeEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellCurrentProbeEvSub_Type.__name__ = "Integer32"
_DellCurrentProbeEvSub_Object = MibScalar
dellCurrentProbeEvSub = _DellCurrentProbeEvSub_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 7),
    _DellCurrentProbeEvSub_Type()
)
dellCurrentProbeEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellCurrentProbeEvSub.setStatus("mandatory")


class _DellCurrentProbeEvSol_Type(Integer32):
    """Custom type dellCurrentProbeEvSol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2))
    )


_DellCurrentProbeEvSol_Type.__name__ = "Integer32"
_DellCurrentProbeEvSol_Object = MibScalar
dellCurrentProbeEvSol = _DellCurrentProbeEvSol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 8),
    _DellCurrentProbeEvSol_Type()
)
dellCurrentProbeEvSol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellCurrentProbeEvSol.setStatus("mandatory")
_DellRedundantPowerSupplyTable_Object = MibTable
dellRedundantPowerSupplyTable = _DellRedundantPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 304)
)
if mibBuilder.loadTexts:
    dellRedundantPowerSupplyTable.setStatus("mandatory")
_DellRedundantPowerSupplyEntry_Object = MibTableRow
dellRedundantPowerSupplyEntry = _DellRedundantPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 304, 1)
)
dellRedundantPowerSupplyEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "pwrSupplyParentIndexAtt1"),
    (0, "BASEBRDD-MIB-MIB", "pwrSupplyIndexAtt2"),
)
if mibBuilder.loadTexts:
    dellRedundantPowerSupplyEntry.setStatus("mandatory")


class _DellRedundantPowerSupplyState_Type(Integer32):
    """Custom type dellRedundantPowerSupplyState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellRedundantPowerSupplyState_Type.__name__ = "Integer32"
_DellRedundantPowerSupplyState_Object = MibTableColumn
dellRedundantPowerSupplyState = _DellRedundantPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 304, 1, 0),
    _DellRedundantPowerSupplyState_Type()
)
dellRedundantPowerSupplyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellRedundantPowerSupplyState.setStatus("mandatory")
_PwrSupplyParentIndexAtt1_Type = DmiInteger
_PwrSupplyParentIndexAtt1_Object = MibTableColumn
pwrSupplyParentIndexAtt1 = _PwrSupplyParentIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 304, 1, 1),
    _PwrSupplyParentIndexAtt1_Type()
)
pwrSupplyParentIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyParentIndexAtt1.setStatus("mandatory")
_PwrSupplyIndexAtt2_Type = DmiInteger
_PwrSupplyIndexAtt2_Object = MibTableColumn
pwrSupplyIndexAtt2 = _PwrSupplyIndexAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 304, 1, 2),
    _PwrSupplyIndexAtt2_Type()
)
pwrSupplyIndexAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyIndexAtt2.setStatus("mandatory")


class _PwrSupplyTypeAtt3_Type(Integer32):
    """Custom type pwrSupplyTypeAtt3 based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("pSPB", 3),
          ("unknown", 2),
          ("x230W", 4),
          ("x275W", 8),
          ("x320W", 7),
          ("x500W", 5),
          ("x700W", 6))
    )


_PwrSupplyTypeAtt3_Type.__name__ = "Integer32"
_PwrSupplyTypeAtt3_Object = MibTableColumn
pwrSupplyTypeAtt3 = _PwrSupplyTypeAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 304, 1, 3),
    _PwrSupplyTypeAtt3_Type()
)
pwrSupplyTypeAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyTypeAtt3.setStatus("mandatory")


class _PwrSupplyStatusAtt4_Type(Integer32):
    """Custom type pwrSupplyStatusAtt4 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_PwrSupplyStatusAtt4_Type.__name__ = "Integer32"
_PwrSupplyStatusAtt4_Object = MibTableColumn
pwrSupplyStatusAtt4 = _PwrSupplyStatusAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 304, 1, 4),
    _PwrSupplyStatusAtt4_Type()
)
pwrSupplyStatusAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyStatusAtt4.setStatus("mandatory")
_PwrSupplyOnlineAtt5_Type = DmiDisplaystring
_PwrSupplyOnlineAtt5_Object = MibTableColumn
pwrSupplyOnlineAtt5 = _PwrSupplyOnlineAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 304, 1, 5),
    _PwrSupplyOnlineAtt5_Type()
)
pwrSupplyOnlineAtt5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrSupplyOnlineAtt5.setStatus("mandatory")
_PwrLocationAtt6_Type = DmiDisplaystring
_PwrLocationAtt6_Object = MibTableColumn
pwrLocationAtt6 = _PwrLocationAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 304, 1, 6),
    _PwrLocationAtt6_Type()
)
pwrLocationAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrLocationAtt6.setStatus("mandatory")
_DellGlobalPowerUnitTable_Object = MibTable
dellGlobalPowerUnitTable = _DellGlobalPowerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305)
)
if mibBuilder.loadTexts:
    dellGlobalPowerUnitTable.setStatus("mandatory")
_DellGlobalPowerUnitEntry_Object = MibTableRow
dellGlobalPowerUnitEntry = _DellGlobalPowerUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1)
)
dellGlobalPowerUnitEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "pwrUnitIndexAtt11"),
)
if mibBuilder.loadTexts:
    dellGlobalPowerUnitEntry.setStatus("mandatory")


class _DellGlobalPowerUnitState_Type(Integer32):
    """Custom type dellGlobalPowerUnitState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellGlobalPowerUnitState_Type.__name__ = "Integer32"
_DellGlobalPowerUnitState_Object = MibTableColumn
dellGlobalPowerUnitState = _DellGlobalPowerUnitState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 0),
    _DellGlobalPowerUnitState_Type()
)
dellGlobalPowerUnitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellGlobalPowerUnitState.setStatus("mandatory")


class _PwrUnitStatusAtt1_Type(Integer32):
    """Custom type pwrUnitStatusAtt1 based on Integer32"""
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
        *(("degradedRedundancy", 6),
          ("fullyRedundant", 5),
          ("notApplicableUnitNotRedundant", 3),
          ("offline", 4),
          ("other", 1),
          ("redundancyLost", 7),
          ("unknown", 2))
    )


_PwrUnitStatusAtt1_Type.__name__ = "Integer32"
_PwrUnitStatusAtt1_Object = MibTableColumn
pwrUnitStatusAtt1 = _PwrUnitStatusAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 1),
    _PwrUnitStatusAtt1_Type()
)
pwrUnitStatusAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrUnitStatusAtt1.setStatus("mandatory")
_PwrUnitGlobalLevelAtt2_Type = DmiInteger
_PwrUnitGlobalLevelAtt2_Object = MibTableColumn
pwrUnitGlobalLevelAtt2 = _PwrUnitGlobalLevelAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 2),
    _PwrUnitGlobalLevelAtt2_Type()
)
pwrUnitGlobalLevelAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrUnitGlobalLevelAtt2.setStatus("mandatory")
_PwrUnitGlobalMaxWarnAtt3_Type = DmiDisplaystring
_PwrUnitGlobalMaxWarnAtt3_Object = MibTableColumn
pwrUnitGlobalMaxWarnAtt3 = _PwrUnitGlobalMaxWarnAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 3),
    _PwrUnitGlobalMaxWarnAtt3_Type()
)
pwrUnitGlobalMaxWarnAtt3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrUnitGlobalMaxWarnAtt3.setStatus("mandatory")
_PwrUnitLevel33vAtt4_Type = DmiInteger
_PwrUnitLevel33vAtt4_Object = MibTableColumn
pwrUnitLevel33vAtt4 = _PwrUnitLevel33vAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 4),
    _PwrUnitLevel33vAtt4_Type()
)
pwrUnitLevel33vAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrUnitLevel33vAtt4.setStatus("mandatory")
_PwrUnitMaxWarn33vAtt5_Type = DmiDisplaystring
_PwrUnitMaxWarn33vAtt5_Object = MibTableColumn
pwrUnitMaxWarn33vAtt5 = _PwrUnitMaxWarn33vAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 5),
    _PwrUnitMaxWarn33vAtt5_Type()
)
pwrUnitMaxWarn33vAtt5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrUnitMaxWarn33vAtt5.setStatus("mandatory")
_PwrUnitLevel5vAtt6_Type = DmiInteger
_PwrUnitLevel5vAtt6_Object = MibTableColumn
pwrUnitLevel5vAtt6 = _PwrUnitLevel5vAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 6),
    _PwrUnitLevel5vAtt6_Type()
)
pwrUnitLevel5vAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrUnitLevel5vAtt6.setStatus("mandatory")
_PwrUnitMaxWarn5vAtt7_Type = DmiDisplaystring
_PwrUnitMaxWarn5vAtt7_Object = MibTableColumn
pwrUnitMaxWarn5vAtt7 = _PwrUnitMaxWarn5vAtt7_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 7),
    _PwrUnitMaxWarn5vAtt7_Type()
)
pwrUnitMaxWarn5vAtt7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrUnitMaxWarn5vAtt7.setStatus("mandatory")
_PwrUnitLevel12vAtt8_Type = DmiInteger
_PwrUnitLevel12vAtt8_Object = MibTableColumn
pwrUnitLevel12vAtt8 = _PwrUnitLevel12vAtt8_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 8),
    _PwrUnitLevel12vAtt8_Type()
)
pwrUnitLevel12vAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrUnitLevel12vAtt8.setStatus("mandatory")
_PwrUnitMaxWarn12vAtt9_Type = DmiDisplaystring
_PwrUnitMaxWarn12vAtt9_Object = MibTableColumn
pwrUnitMaxWarn12vAtt9 = _PwrUnitMaxWarn12vAtt9_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 9),
    _PwrUnitMaxWarn12vAtt9_Type()
)
pwrUnitMaxWarn12vAtt9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrUnitMaxWarn12vAtt9.setStatus("mandatory")
_PwrUnitUidAtt10_Type = DmiDisplaystring
_PwrUnitUidAtt10_Object = MibTableColumn
pwrUnitUidAtt10 = _PwrUnitUidAtt10_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 10),
    _PwrUnitUidAtt10_Type()
)
pwrUnitUidAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrUnitUidAtt10.setStatus("mandatory")
_PwrUnitIndexAtt11_Type = DmiInteger
_PwrUnitIndexAtt11_Object = MibTableColumn
pwrUnitIndexAtt11 = _PwrUnitIndexAtt11_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 1, 11),
    _PwrUnitIndexAtt11_Type()
)
pwrUnitIndexAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrUnitIndexAtt11.setStatus("mandatory")


class _DellGlobalPowerUnitEvSys_Type(Integer32):
    """Custom type dellGlobalPowerUnitEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellGlobalPowerUnitEvSys_Type.__name__ = "Integer32"
_DellGlobalPowerUnitEvSys_Object = MibScalar
dellGlobalPowerUnitEvSys = _DellGlobalPowerUnitEvSys_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 6),
    _DellGlobalPowerUnitEvSys_Type()
)
dellGlobalPowerUnitEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellGlobalPowerUnitEvSys.setStatus("mandatory")


class _DellGlobalPowerUnitEvSub_Type(Integer32):
    """Custom type dellGlobalPowerUnitEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellGlobalPowerUnitEvSub_Type.__name__ = "Integer32"
_DellGlobalPowerUnitEvSub_Object = MibScalar
dellGlobalPowerUnitEvSub = _DellGlobalPowerUnitEvSub_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 7),
    _DellGlobalPowerUnitEvSub_Type()
)
dellGlobalPowerUnitEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellGlobalPowerUnitEvSub.setStatus("mandatory")


class _DellGlobalPowerUnitEvSol_Type(Integer32):
    """Custom type dellGlobalPowerUnitEvSol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2))
    )


_DellGlobalPowerUnitEvSol_Type.__name__ = "Integer32"
_DellGlobalPowerUnitEvSol_Object = MibScalar
dellGlobalPowerUnitEvSol = _DellGlobalPowerUnitEvSol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 8),
    _DellGlobalPowerUnitEvSol_Type()
)
dellGlobalPowerUnitEvSol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellGlobalPowerUnitEvSol.setStatus("mandatory")
_DellSystemChassisExtensionTable_Object = MibTable
dellSystemChassisExtensionTable = _DellSystemChassisExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306)
)
if mibBuilder.loadTexts:
    dellSystemChassisExtensionTable.setStatus("mandatory")
_DellSystemChassisExtensionEntry_Object = MibTableRow
dellSystemChassisExtensionEntry = _DellSystemChassisExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1)
)
dellSystemChassisExtensionEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "chassIndexAtt1"),
)
if mibBuilder.loadTexts:
    dellSystemChassisExtensionEntry.setStatus("mandatory")


class _DellSystemChassisExtensionState_Type(Integer32):
    """Custom type dellSystemChassisExtensionState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellSystemChassisExtensionState_Type.__name__ = "Integer32"
_DellSystemChassisExtensionState_Object = MibTableColumn
dellSystemChassisExtensionState = _DellSystemChassisExtensionState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 0),
    _DellSystemChassisExtensionState_Type()
)
dellSystemChassisExtensionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellSystemChassisExtensionState.setStatus("mandatory")
_ChassIndexAtt1_Type = DmiInteger
_ChassIndexAtt1_Object = MibTableColumn
chassIndexAtt1 = _ChassIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 1),
    _ChassIndexAtt1_Type()
)
chassIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassIndexAtt1.setStatus("mandatory")


class _ChassGlobStatusAtt2_Type(Integer32):
    """Custom type chassGlobStatusAtt2 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ChassGlobStatusAtt2_Type.__name__ = "Integer32"
_ChassGlobStatusAtt2_Object = MibTableColumn
chassGlobStatusAtt2 = _ChassGlobStatusAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 2),
    _ChassGlobStatusAtt2_Type()
)
chassGlobStatusAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassGlobStatusAtt2.setStatus("mandatory")


class _ChassTempStatusAtt3_Type(Integer32):
    """Custom type chassTempStatusAtt3 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ChassTempStatusAtt3_Type.__name__ = "Integer32"
_ChassTempStatusAtt3_Object = MibTableColumn
chassTempStatusAtt3 = _ChassTempStatusAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 3),
    _ChassTempStatusAtt3_Type()
)
chassTempStatusAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassTempStatusAtt3.setStatus("mandatory")
_ChassTempProbesAtt4_Type = DmiOctetstring
_ChassTempProbesAtt4_Object = MibTableColumn
chassTempProbesAtt4 = _ChassTempProbesAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 4),
    _ChassTempProbesAtt4_Type()
)
chassTempProbesAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassTempProbesAtt4.setStatus("mandatory")


class _ChassFansStatusAtt5_Type(Integer32):
    """Custom type chassFansStatusAtt5 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ChassFansStatusAtt5_Type.__name__ = "Integer32"
_ChassFansStatusAtt5_Object = MibTableColumn
chassFansStatusAtt5 = _ChassFansStatusAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 5),
    _ChassFansStatusAtt5_Type()
)
chassFansStatusAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassFansStatusAtt5.setStatus("mandatory")
_ChassFansProbesAtt6_Type = DmiOctetstring
_ChassFansProbesAtt6_Object = MibTableColumn
chassFansProbesAtt6 = _ChassFansProbesAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 6),
    _ChassFansProbesAtt6_Type()
)
chassFansProbesAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassFansProbesAtt6.setStatus("mandatory")


class _ChassVoltStatusAtt7_Type(Integer32):
    """Custom type chassVoltStatusAtt7 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ChassVoltStatusAtt7_Type.__name__ = "Integer32"
_ChassVoltStatusAtt7_Object = MibTableColumn
chassVoltStatusAtt7 = _ChassVoltStatusAtt7_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 7),
    _ChassVoltStatusAtt7_Type()
)
chassVoltStatusAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassVoltStatusAtt7.setStatus("mandatory")
_ChassVoltProbesAtt8_Type = DmiOctetstring
_ChassVoltProbesAtt8_Object = MibTableColumn
chassVoltProbesAtt8 = _ChassVoltProbesAtt8_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 8),
    _ChassVoltProbesAtt8_Type()
)
chassVoltProbesAtt8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassVoltProbesAtt8.setStatus("mandatory")


class _ChassAmpStatusAtt9_Type(Integer32):
    """Custom type chassAmpStatusAtt9 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ChassAmpStatusAtt9_Type.__name__ = "Integer32"
_ChassAmpStatusAtt9_Object = MibTableColumn
chassAmpStatusAtt9 = _ChassAmpStatusAtt9_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 9),
    _ChassAmpStatusAtt9_Type()
)
chassAmpStatusAtt9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassAmpStatusAtt9.setStatus("mandatory")
_ChassAmpProbesAtt10_Type = DmiOctetstring
_ChassAmpProbesAtt10_Object = MibTableColumn
chassAmpProbesAtt10 = _ChassAmpProbesAtt10_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 10),
    _ChassAmpProbesAtt10_Type()
)
chassAmpProbesAtt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassAmpProbesAtt10.setStatus("mandatory")


class _ChassPsStatusAtt11_Type(Integer32):
    """Custom type chassPsStatusAtt11 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ChassPsStatusAtt11_Type.__name__ = "Integer32"
_ChassPsStatusAtt11_Object = MibTableColumn
chassPsStatusAtt11 = _ChassPsStatusAtt11_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 11),
    _ChassPsStatusAtt11_Type()
)
chassPsStatusAtt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassPsStatusAtt11.setStatus("mandatory")
_ChassPwrSuppliesAtt12_Type = DmiOctetstring
_ChassPwrSuppliesAtt12_Object = MibTableColumn
chassPwrSuppliesAtt12 = _ChassPwrSuppliesAtt12_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 12),
    _ChassPwrSuppliesAtt12_Type()
)
chassPwrSuppliesAtt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassPwrSuppliesAtt12.setStatus("mandatory")
_ChassServiceTagAtt13_Type = DmiDisplaystring
_ChassServiceTagAtt13_Object = MibTableColumn
chassServiceTagAtt13 = _ChassServiceTagAtt13_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 13),
    _ChassServiceTagAtt13_Type()
)
chassServiceTagAtt13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassServiceTagAtt13.setStatus("mandatory")
_ChassUidAtt14_Type = DmiDisplaystring
_ChassUidAtt14_Object = MibTableColumn
chassUidAtt14 = _ChassUidAtt14_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 14),
    _ChassUidAtt14_Type()
)
chassUidAtt14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassUidAtt14.setStatus("mandatory")
_ChassBackPlaneUidAtt15_Type = DmiDisplaystring
_ChassBackPlaneUidAtt15_Object = MibTableColumn
chassBackPlaneUidAtt15 = _ChassBackPlaneUidAtt15_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 15),
    _ChassBackPlaneUidAtt15_Type()
)
chassBackPlaneUidAtt15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassBackPlaneUidAtt15.setStatus("mandatory")
_ChassIdentifyAtt16_Type = DmiDisplaystring
_ChassIdentifyAtt16_Object = MibTableColumn
chassIdentifyAtt16 = _ChassIdentifyAtt16_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 16),
    _ChassIdentifyAtt16_Type()
)
chassIdentifyAtt16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassIdentifyAtt16.setStatus("mandatory")
_ChassFanControlAtt17_Type = DmiDisplaystring
_ChassFanControlAtt17_Object = MibTableColumn
chassFanControlAtt17 = _ChassFanControlAtt17_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 17),
    _ChassFanControlAtt17_Type()
)
chassFanControlAtt17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassFanControlAtt17.setStatus("mandatory")
_ChassLEDConfigAtt18_Type = DmiDisplaystring
_ChassLEDConfigAtt18_Object = MibTableColumn
chassLEDConfigAtt18 = _ChassLEDConfigAtt18_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 18),
    _ChassLEDConfigAtt18_Type()
)
chassLEDConfigAtt18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassLEDConfigAtt18.setStatus("mandatory")
_ChassFaultClearAtt19_Type = DmiDisplaystring
_ChassFaultClearAtt19_Object = MibTableColumn
chassFaultClearAtt19 = _ChassFaultClearAtt19_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 19),
    _ChassFaultClearAtt19_Type()
)
chassFaultClearAtt19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassFaultClearAtt19.setStatus("mandatory")
_ChassThermalShutdownAtt20_Type = DmiDisplaystring
_ChassThermalShutdownAtt20_Object = MibTableColumn
chassThermalShutdownAtt20 = _ChassThermalShutdownAtt20_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 20),
    _ChassThermalShutdownAtt20_Type()
)
chassThermalShutdownAtt20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassThermalShutdownAtt20.setStatus("mandatory")


class _ChassMemStatusAtt21_Type(Integer32):
    """Custom type chassMemStatusAtt21 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ChassMemStatusAtt21_Type.__name__ = "Integer32"
_ChassMemStatusAtt21_Object = MibTableColumn
chassMemStatusAtt21 = _ChassMemStatusAtt21_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 21),
    _ChassMemStatusAtt21_Type()
)
chassMemStatusAtt21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassMemStatusAtt21.setStatus("mandatory")
_ChassMemDevicesAtt22_Type = DmiOctetstring
_ChassMemDevicesAtt22_Object = MibTableColumn
chassMemDevicesAtt22 = _ChassMemDevicesAtt22_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 1, 22),
    _ChassMemDevicesAtt22_Type()
)
chassMemDevicesAtt22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassMemDevicesAtt22.setStatus("mandatory")


class _DellSystemChassisExtensionEvSys_Type(Integer32):
    """Custom type dellSystemChassisExtensionEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellSystemChassisExtensionEvSys_Type.__name__ = "Integer32"
_DellSystemChassisExtensionEvSys_Object = MibScalar
dellSystemChassisExtensionEvSys = _DellSystemChassisExtensionEvSys_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 6),
    _DellSystemChassisExtensionEvSys_Type()
)
dellSystemChassisExtensionEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellSystemChassisExtensionEvSys.setStatus("mandatory")


class _DellSystemChassisExtensionEvSub_Type(Integer32):
    """Custom type dellSystemChassisExtensionEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellSystemChassisExtensionEvSub_Type.__name__ = "Integer32"
_DellSystemChassisExtensionEvSub_Object = MibScalar
dellSystemChassisExtensionEvSub = _DellSystemChassisExtensionEvSub_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 7),
    _DellSystemChassisExtensionEvSub_Type()
)
dellSystemChassisExtensionEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellSystemChassisExtensionEvSub.setStatus("mandatory")


class _DellSystemChassisExtensionEvSol_Type(Integer32):
    """Custom type dellSystemChassisExtensionEvSol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2))
    )


_DellSystemChassisExtensionEvSol_Type.__name__ = "Integer32"
_DellSystemChassisExtensionEvSol_Object = MibScalar
dellSystemChassisExtensionEvSol = _DellSystemChassisExtensionEvSol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 8),
    _DellSystemChassisExtensionEvSol_Type()
)
dellSystemChassisExtensionEvSol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellSystemChassisExtensionEvSol.setStatus("mandatory")
_DellEsmLogTable_Object = MibTable
dellEsmLogTable = _DellEsmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 307)
)
if mibBuilder.loadTexts:
    dellEsmLogTable.setStatus("mandatory")
_DellEsmLogEntry_Object = MibTableRow
dellEsmLogEntry = _DellEsmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 307, 1)
)
dellEsmLogEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "esmLogIndexAtt1"),
)
if mibBuilder.loadTexts:
    dellEsmLogEntry.setStatus("mandatory")


class _DellEsmLogState_Type(Integer32):
    """Custom type dellEsmLogState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellEsmLogState_Type.__name__ = "Integer32"
_DellEsmLogState_Object = MibTableColumn
dellEsmLogState = _DellEsmLogState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 307, 1, 0),
    _DellEsmLogState_Type()
)
dellEsmLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellEsmLogState.setStatus("mandatory")
_EsmLogIndexAtt1_Type = DmiInteger
_EsmLogIndexAtt1_Object = MibTableColumn
esmLogIndexAtt1 = _EsmLogIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 307, 1, 1),
    _EsmLogIndexAtt1_Type()
)
esmLogIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmLogIndexAtt1.setStatus("mandatory")
_EsmLogDataAtt2_Type = DmiDisplaystring
_EsmLogDataAtt2_Object = MibTableColumn
esmLogDataAtt2 = _EsmLogDataAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 307, 1, 2),
    _EsmLogDataAtt2_Type()
)
esmLogDataAtt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmLogDataAtt2.setStatus("mandatory")
_DellPOSTLogTable_Object = MibTable
dellPOSTLogTable = _DellPOSTLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 308)
)
if mibBuilder.loadTexts:
    dellPOSTLogTable.setStatus("mandatory")
_DellPOSTLogEntry_Object = MibTableRow
dellPOSTLogEntry = _DellPOSTLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 308, 1)
)
dellPOSTLogEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "postLogIndexAtt1"),
)
if mibBuilder.loadTexts:
    dellPOSTLogEntry.setStatus("mandatory")


class _DellPOSTLogState_Type(Integer32):
    """Custom type dellPOSTLogState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellPOSTLogState_Type.__name__ = "Integer32"
_DellPOSTLogState_Object = MibTableColumn
dellPOSTLogState = _DellPOSTLogState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 308, 1, 0),
    _DellPOSTLogState_Type()
)
dellPOSTLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellPOSTLogState.setStatus("mandatory")
_PostLogIndexAtt1_Type = DmiInteger
_PostLogIndexAtt1_Object = MibTableColumn
postLogIndexAtt1 = _PostLogIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 308, 1, 1),
    _PostLogIndexAtt1_Type()
)
postLogIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogIndexAtt1.setStatus("mandatory")
_PostLogDataAtt2_Type = DmiOctetstring
_PostLogDataAtt2_Object = MibTableColumn
postLogDataAtt2 = _PostLogDataAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 308, 1, 2),
    _PostLogDataAtt2_Type()
)
postLogDataAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogDataAtt2.setStatus("mandatory")
_DellSecurityTable_Object = MibTable
dellSecurityTable = _DellSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 309)
)
if mibBuilder.loadTexts:
    dellSecurityTable.setStatus("mandatory")
_DellSecurityEntry_Object = MibTableRow
dellSecurityEntry = _DellSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 309, 1)
)
dellSecurityEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "userIndexAtt1"),
)
if mibBuilder.loadTexts:
    dellSecurityEntry.setStatus("mandatory")


class _DellSecurityState_Type(Integer32):
    """Custom type dellSecurityState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellSecurityState_Type.__name__ = "Integer32"
_DellSecurityState_Object = MibTableColumn
dellSecurityState = _DellSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 309, 1, 0),
    _DellSecurityState_Type()
)
dellSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellSecurityState.setStatus("mandatory")
_UserIndexAtt1_Type = DmiInteger
_UserIndexAtt1_Object = MibTableColumn
userIndexAtt1 = _UserIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 309, 1, 1),
    _UserIndexAtt1_Type()
)
userIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userIndexAtt1.setStatus("mandatory")
_UserNameAtt2_Type = DmiDisplaystring
_UserNameAtt2_Object = MibTableColumn
userNameAtt2 = _UserNameAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 309, 1, 2),
    _UserNameAtt2_Type()
)
userNameAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userNameAtt2.setStatus("mandatory")
_UserControlAtt3_Type = DmiDisplaystring
_UserControlAtt3_Object = MibTableColumn
userControlAtt3 = _UserControlAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 309, 1, 3),
    _UserControlAtt3_Type()
)
userControlAtt3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userControlAtt3.setStatus("mandatory")
_RequestAtt4_Type = DmiDisplaystring
_RequestAtt4_Object = MibTableColumn
requestAtt4 = _RequestAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 309, 1, 4),
    _RequestAtt4_Type()
)
requestAtt4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    requestAtt4.setStatus("mandatory")
_DellDialupTable_Object = MibTable
dellDialupTable = _DellDialupTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 310)
)
if mibBuilder.loadTexts:
    dellDialupTable.setStatus("mandatory")
_DellDialupEntry_Object = MibTableRow
dellDialupEntry = _DellDialupEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 310, 1)
)
dellDialupEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dellDialupEntry.setStatus("mandatory")


class _DialupCapabilityAtt1_Type(Integer32):
    """Custom type dialupCapabilityAtt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DialupCapabilityAtt1_Type.__name__ = "Integer32"
_DialupCapabilityAtt1_Object = MibTableColumn
dialupCapabilityAtt1 = _DialupCapabilityAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 310, 1, 1),
    _DialupCapabilityAtt1_Type()
)
dialupCapabilityAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialupCapabilityAtt1.setStatus("mandatory")
_CallbackNumberAtt2_Type = DmiDisplaystring
_CallbackNumberAtt2_Object = MibTableColumn
callbackNumberAtt2 = _CallbackNumberAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 310, 1, 2),
    _CallbackNumberAtt2_Type()
)
callbackNumberAtt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callbackNumberAtt2.setStatus("mandatory")
_DellFirmwareTable_Object = MibTable
dellFirmwareTable = _DellFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 311)
)
if mibBuilder.loadTexts:
    dellFirmwareTable.setStatus("mandatory")
_DellFirmwareEntry_Object = MibTableRow
dellFirmwareEntry = _DellFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 311, 1)
)
dellFirmwareEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "firmwareChassisIndexAtt1"),
    (0, "BASEBRDD-MIB-MIB", "firmwareIndexAtt2"),
)
if mibBuilder.loadTexts:
    dellFirmwareEntry.setStatus("mandatory")


class _DellFirmwareState_Type(Integer32):
    """Custom type dellFirmwareState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellFirmwareState_Type.__name__ = "Integer32"
_DellFirmwareState_Object = MibTableColumn
dellFirmwareState = _DellFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 311, 1, 0),
    _DellFirmwareState_Type()
)
dellFirmwareState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellFirmwareState.setStatus("mandatory")
_FirmwareChassisIndexAtt1_Type = DmiInteger
_FirmwareChassisIndexAtt1_Object = MibTableColumn
firmwareChassisIndexAtt1 = _FirmwareChassisIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 311, 1, 1),
    _FirmwareChassisIndexAtt1_Type()
)
firmwareChassisIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareChassisIndexAtt1.setStatus("mandatory")
_FirmwareIndexAtt2_Type = DmiInteger
_FirmwareIndexAtt2_Object = MibTableColumn
firmwareIndexAtt2 = _FirmwareIndexAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 311, 1, 2),
    _FirmwareIndexAtt2_Type()
)
firmwareIndexAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareIndexAtt2.setStatus("mandatory")


class _FirmwareTypeAtt3_Type(Integer32):
    """Custom type firmwareTypeAtt3 based on Integer32"""
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
        *(("bIOS", 3),
          ("backplane", 6),
          ("eSM", 4),
          ("other", 1),
          ("pSPB", 5),
          ("unknown", 2))
    )


_FirmwareTypeAtt3_Type.__name__ = "Integer32"
_FirmwareTypeAtt3_Object = MibTableColumn
firmwareTypeAtt3 = _FirmwareTypeAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 311, 1, 3),
    _FirmwareTypeAtt3_Type()
)
firmwareTypeAtt3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareTypeAtt3.setStatus("mandatory")
_FirmwareVersionAtt4_Type = DmiDisplaystring
_FirmwareVersionAtt4_Object = MibTableColumn
firmwareVersionAtt4 = _FirmwareVersionAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 311, 1, 4),
    _FirmwareVersionAtt4_Type()
)
firmwareVersionAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersionAtt4.setStatus("mandatory")


class _FirmwareStatusAtt5_Type(Integer32):
    """Custom type firmwareStatusAtt5 based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("oK", 3),
          ("other", 1),
          ("unknown", 2))
    )


_FirmwareStatusAtt5_Type.__name__ = "Integer32"
_FirmwareStatusAtt5_Object = MibTableColumn
firmwareStatusAtt5 = _FirmwareStatusAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 311, 1, 5),
    _FirmwareStatusAtt5_Type()
)
firmwareStatusAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStatusAtt5.setStatus("mandatory")
_DellSystemResetTable_Object = MibTable
dellSystemResetTable = _DellSystemResetTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312)
)
if mibBuilder.loadTexts:
    dellSystemResetTable.setStatus("mandatory")
_DellSystemResetEntry_Object = MibTableRow
dellSystemResetEntry = _DellSystemResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 1)
)
dellSystemResetEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dellSystemResetEntry.setStatus("mandatory")
_AutomaticCapabilitiesAtt1_Type = DmiInteger
_AutomaticCapabilitiesAtt1_Object = MibTableColumn
automaticCapabilitiesAtt1 = _AutomaticCapabilitiesAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 1, 1),
    _AutomaticCapabilitiesAtt1_Type()
)
automaticCapabilitiesAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automaticCapabilitiesAtt1.setStatus("mandatory")
_AutomaticSettingsAtt2_Type = DmiDisplaystring
_AutomaticSettingsAtt2_Object = MibTableColumn
automaticSettingsAtt2 = _AutomaticSettingsAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 1, 2),
    _AutomaticSettingsAtt2_Type()
)
automaticSettingsAtt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automaticSettingsAtt2.setStatus("mandatory")
_NotificationNumberAtt3_Type = DmiDisplaystring
_NotificationNumberAtt3_Object = MibTableColumn
notificationNumberAtt3 = _NotificationNumberAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 1, 3),
    _NotificationNumberAtt3_Type()
)
notificationNumberAtt3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    notificationNumberAtt3.setStatus("mandatory")
_ManualCapabilitiesAtt4_Type = DmiInteger
_ManualCapabilitiesAtt4_Object = MibTableColumn
manualCapabilitiesAtt4 = _ManualCapabilitiesAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 1, 4),
    _ManualCapabilitiesAtt4_Type()
)
manualCapabilitiesAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manualCapabilitiesAtt4.setStatus("mandatory")
_ManualControlAtt5_Type = DmiDisplaystring
_ManualControlAtt5_Object = MibTableColumn
manualControlAtt5 = _ManualControlAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 1, 5),
    _ManualControlAtt5_Type()
)
manualControlAtt5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manualControlAtt5.setStatus("mandatory")
_AutomaticSystemResetTimerAtt6_Type = DmiDisplaystring
_AutomaticSystemResetTimerAtt6_Object = MibTableColumn
automaticSystemResetTimerAtt6 = _AutomaticSystemResetTimerAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 1, 6),
    _AutomaticSystemResetTimerAtt6_Type()
)
automaticSystemResetTimerAtt6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automaticSystemResetTimerAtt6.setStatus("mandatory")


class _DellSystemResetEvSys_Type(Integer32):
    """Custom type dellSystemResetEvSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellSystemResetEvSys_Type.__name__ = "Integer32"
_DellSystemResetEvSys_Object = MibScalar
dellSystemResetEvSys = _DellSystemResetEvSys_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 6),
    _DellSystemResetEvSys_Type()
)
dellSystemResetEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellSystemResetEvSys.setStatus("mandatory")


class _DellSystemResetEvSub_Type(Integer32):
    """Custom type dellSystemResetEvSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 1))
    )


_DellSystemResetEvSub_Type.__name__ = "Integer32"
_DellSystemResetEvSub_Object = MibScalar
dellSystemResetEvSub = _DellSystemResetEvSub_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 7),
    _DellSystemResetEvSub_Type()
)
dellSystemResetEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellSystemResetEvSub.setStatus("mandatory")


class _DellSystemResetEvSol_Type(Integer32):
    """Custom type dellSystemResetEvSol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2))
    )


_DellSystemResetEvSol_Type.__name__ = "Integer32"
_DellSystemResetEvSol_Object = MibScalar
dellSystemResetEvSol = _DellSystemResetEvSol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 8),
    _DellSystemResetEvSol_Type()
)
dellSystemResetEvSol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellSystemResetEvSol.setStatus("mandatory")
_DELLSystemsManagementSoftwareTable_Object = MibTable
dELLSystemsManagementSoftwareTable = _DELLSystemsManagementSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400)
)
if mibBuilder.loadTexts:
    dELLSystemsManagementSoftwareTable.setStatus("mandatory")
_DELLSystemsManagementSoftwareEntry_Object = MibTableRow
dELLSystemsManagementSoftwareEntry = _DELLSystemsManagementSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1)
)
dELLSystemsManagementSoftwareEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dELLSystemsManagementSoftwareEntry.setStatus("mandatory")
_ProductAtt1_Type = DmiDisplaystring
_ProductAtt1_Object = MibTableColumn
productAtt1 = _ProductAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 1),
    _ProductAtt1_Type()
)
productAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productAtt1.setStatus("mandatory")
_VersionAtt2_Type = DmiDisplaystring
_VersionAtt2_Object = MibTableColumn
versionAtt2 = _VersionAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 2),
    _VersionAtt2_Type()
)
versionAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionAtt2.setStatus("mandatory")
_BuildNumberAtt3_Type = DmiInteger
_BuildNumberAtt3_Object = MibTableColumn
buildNumberAtt3 = _BuildNumberAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 3),
    _BuildNumberAtt3_Type()
)
buildNumberAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildNumberAtt3.setStatus("mandatory")
_DescriptionAtt4_Type = DmiDisplaystring
_DescriptionAtt4_Object = MibTableColumn
descriptionAtt4 = _DescriptionAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 4),
    _DescriptionAtt4_Type()
)
descriptionAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    descriptionAtt4.setStatus("mandatory")
_SupportedProtocolsAtt5_Type = DmiInteger
_SupportedProtocolsAtt5_Object = MibTableColumn
supportedProtocolsAtt5 = _SupportedProtocolsAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 5),
    _SupportedProtocolsAtt5_Type()
)
supportedProtocolsAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportedProtocolsAtt5.setStatus("mandatory")


class _PreferredProtocolAtt6_Type(Integer32):
    """Custom type preferredProtocolAtt6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cIMOM", 4),
          ("dMIRPC", 2),
          ("sNMP", 1))
    )


_PreferredProtocolAtt6_Type.__name__ = "Integer32"
_PreferredProtocolAtt6_Object = MibTableColumn
preferredProtocolAtt6 = _PreferredProtocolAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 6),
    _PreferredProtocolAtt6_Type()
)
preferredProtocolAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preferredProtocolAtt6.setStatus("mandatory")
_DMIRPCTypesAtt7_Type = DmiDisplaystring
_DMIRPCTypesAtt7_Object = MibTableColumn
dMIRPCTypesAtt7 = _DMIRPCTypesAtt7_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 7),
    _DMIRPCTypesAtt7_Type()
)
dMIRPCTypesAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMIRPCTypesAtt7.setStatus("mandatory")
_DELLSystemsSummaryInformationTable_Object = MibTable
dELLSystemsSummaryInformationTable = _DELLSystemsSummaryInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 402)
)
if mibBuilder.loadTexts:
    dELLSystemsSummaryInformationTable.setStatus("mandatory")
_DELLSystemsSummaryInformationEntry_Object = MibTableRow
dELLSystemsSummaryInformationEntry = _DELLSystemsSummaryInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 402, 1)
)
dELLSystemsSummaryInformationEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dELLSystemsSummaryInformationEntry.setStatus("mandatory")


class _OperatingSystemAtt1_Type(Integer32):
    """Custom type operatingSystemAtt1 based on Integer32"""
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
        *(("iBMOS2", 5),
          ("netware", 7),
          ("other", 1),
          ("sCOUNIX", 6),
          ("unknown", 2),
          ("windows9x", 4),
          ("windowsNT", 3))
    )


_OperatingSystemAtt1_Type.__name__ = "Integer32"
_OperatingSystemAtt1_Object = MibTableColumn
operatingSystemAtt1 = _OperatingSystemAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 402, 1, 1),
    _OperatingSystemAtt1_Type()
)
operatingSystemAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemAtt1.setStatus("mandatory")


class _SystemClassAtt2_Type(Integer32):
    """Custom type systemClassAtt2 based on Integer32"""
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
        *(("desktop", 5),
          ("netPC", 7),
          ("other", 1),
          ("portable", 6),
          ("server", 4),
          ("unknown", 2),
          ("workstation", 3))
    )


_SystemClassAtt2_Type.__name__ = "Integer32"
_SystemClassAtt2_Object = MibTableColumn
systemClassAtt2 = _SystemClassAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 402, 1, 2),
    _SystemClassAtt2_Type()
)
systemClassAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemClassAtt2.setStatus("mandatory")
_DellMemoryPrefailureTable_Object = MibTable
dellMemoryPrefailureTable = _DellMemoryPrefailureTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 403)
)
if mibBuilder.loadTexts:
    dellMemoryPrefailureTable.setStatus("mandatory")
_DellMemoryPrefailureEntry_Object = MibTableRow
dellMemoryPrefailureEntry = _DellMemoryPrefailureEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 403, 1)
)
dellMemoryPrefailureEntry.setIndexNames(
    (0, "BASEBRDD-MIB-MIB", "DmiCompId"),
    (0, "BASEBRDD-MIB-MIB", "DmiGroupId"),
    (0, "BASEBRDD-MIB-MIB", "memoryDeviceIndexAtt1"),
)
if mibBuilder.loadTexts:
    dellMemoryPrefailureEntry.setStatus("mandatory")


class _DellMemoryPrefailureState_Type(Integer32):
    """Custom type dellMemoryPrefailureState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DellMemoryPrefailureState_Type.__name__ = "Integer32"
_DellMemoryPrefailureState_Object = MibTableColumn
dellMemoryPrefailureState = _DellMemoryPrefailureState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 403, 1, 0),
    _DellMemoryPrefailureState_Type()
)
dellMemoryPrefailureState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellMemoryPrefailureState.setStatus("mandatory")
_MemoryDeviceIndexAtt1_Type = DmiInteger
_MemoryDeviceIndexAtt1_Object = MibTableColumn
memoryDeviceIndexAtt1 = _MemoryDeviceIndexAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 403, 1, 1),
    _MemoryDeviceIndexAtt1_Type()
)
memoryDeviceIndexAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceIndexAtt1.setStatus("mandatory")
_ResetMemoryDeviceErrorCountAndPrefailureStatusAtt2_Type = DmiInteger
_ResetMemoryDeviceErrorCountAndPrefailureStatusAtt2_Object = MibTableColumn
resetMemoryDeviceErrorCountAndPrefailureStatusAtt2 = _ResetMemoryDeviceErrorCountAndPrefailureStatusAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 403, 1, 2),
    _ResetMemoryDeviceErrorCountAndPrefailureStatusAtt2_Type()
)
resetMemoryDeviceErrorCountAndPrefailureStatusAtt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetMemoryDeviceErrorCountAndPrefailureStatusAtt2.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dMTFPowerSupplyEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 0, 1)
)
dMTFPowerSupplyEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPowerSupplyEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPowerSupplyEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPowerSupplyEvt1.setStatus(
        ""
    )

dMTFPowerSupplyEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 16, 0, 2)
)
dMTFPowerSupplyEvt2.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPowerSupplyEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPowerSupplyEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPowerSupplyEvt2.setStatus(
        ""
    )

dMTFCoolingDeviceEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 0, 1)
)
dMTFCoolingDeviceEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFCoolingDeviceEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFCoolingDeviceEvSub"))
)
if mibBuilder.loadTexts:
    dMTFCoolingDeviceEvt1.setStatus(
        ""
    )

dMTFCoolingDeviceEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 17, 0, 2)
)
dMTFCoolingDeviceEvt2.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFCoolingDeviceEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFCoolingDeviceEvSub"))
)
if mibBuilder.loadTexts:
    dMTFCoolingDeviceEvt2.setStatus(
        ""
    )

dMTFPhysicalMemoryArrayEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 0, 1)
)
dMTFPhysicalMemoryArrayEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalMemoryArrayEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalMemoryArrayEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPhysicalMemoryArrayEvt1.setStatus(
        ""
    )

dMTFPhysicalMemoryArrayEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 33, 0, 2)
)
dMTFPhysicalMemoryArrayEvt2.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalMemoryArrayEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalMemoryArrayEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPhysicalMemoryArrayEvt2.setStatus(
        ""
    )

dMTFVoltageProbeEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 53, 0, 1)
)
dMTFVoltageProbeEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFVoltageProbeEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFVoltageProbeEvSub"))
)
if mibBuilder.loadTexts:
    dMTFVoltageProbeEvt1.setStatus(
        ""
    )

dMTFTemperatureProbeEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 54, 0, 1)
)
dMTFTemperatureProbeEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFTemperatureProbeEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFTemperatureProbeEvSub"))
)
if mibBuilder.loadTexts:
    dMTFTemperatureProbeEvt1.setStatus(
        ""
    )

dMTFElectricalCurrentProbeEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 0, 1)
)
dMTFElectricalCurrentProbeEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFElectricalCurrentProbeEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFElectricalCurrentProbeEvSub"))
)
if mibBuilder.loadTexts:
    dMTFElectricalCurrentProbeEvt1.setStatus(
        ""
    )

dMTFElectricalCurrentProbeEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 55, 0, 2)
)
dMTFElectricalCurrentProbeEvt2.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFElectricalCurrentProbeEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFElectricalCurrentProbeEvSub"))
)
if mibBuilder.loadTexts:
    dMTFElectricalCurrentProbeEvt2.setStatus(
        ""
    )

dMTFPhysicalContainerGlobalTableEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 0, 1)
)
dMTFPhysicalContainerGlobalTableEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEvt1.setStatus(
        ""
    )

dMTFPhysicalContainerGlobalTableEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 0, 2)
)
dMTFPhysicalContainerGlobalTableEvt2.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEvt2.setStatus(
        ""
    )

dMTFPhysicalContainerGlobalTableEvt3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 0, 3)
)
dMTFPhysicalContainerGlobalTableEvt3.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEvt3.setStatus(
        ""
    )

dMTFPhysicalContainerGlobalTableEvt4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 0, 4)
)
dMTFPhysicalContainerGlobalTableEvt4.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEvt4.setStatus(
        ""
    )

dMTFPhysicalContainerGlobalTableEvt5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 0, 5)
)
dMTFPhysicalContainerGlobalTableEvt5.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEvt5.setStatus(
        ""
    )

dMTFPhysicalContainerGlobalTableEvt6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 0, 6)
)
dMTFPhysicalContainerGlobalTableEvt6.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEvt6.setStatus(
        ""
    )

dMTFPhysicalContainerGlobalTableEvt7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 4, 63, 0, 7)
)
dMTFPhysicalContainerGlobalTableEvt7.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSys"),
        ("BASEBRDD-MIB-MIB", "dMTFPhysicalContainerGlobalTableEvSub"))
)
if mibBuilder.loadTexts:
    dMTFPhysicalContainerGlobalTableEvt7.setStatus(
        ""
    )

dellTemperatureProbeEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10891, 300, 0, 1)
)
dellTemperatureProbeEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dellTemperatureProbeEvSys"),
        ("BASEBRDD-MIB-MIB", "dellTemperatureProbeEvSub"),
        ("BASEBRDD-MIB-MIB", "dellTemperatureProbeEvSol"))
)
if mibBuilder.loadTexts:
    dellTemperatureProbeEvt1.setStatus(
        ""
    )

dellFanSensorEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10891, 301, 0, 1)
)
dellFanSensorEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dellFanSensorEvSys"),
        ("BASEBRDD-MIB-MIB", "dellFanSensorEvSub"),
        ("BASEBRDD-MIB-MIB", "dellFanSensorEvSol"))
)
if mibBuilder.loadTexts:
    dellFanSensorEvt1.setStatus(
        ""
    )

dellVoltageProbeEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10891, 302, 0, 1)
)
dellVoltageProbeEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dellVoltageProbeEvSys"),
        ("BASEBRDD-MIB-MIB", "dellVoltageProbeEvSub"),
        ("BASEBRDD-MIB-MIB", "dellVoltageProbeEvSol"))
)
if mibBuilder.loadTexts:
    dellVoltageProbeEvt1.setStatus(
        ""
    )

dellCurrentProbeEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10891, 303, 0, 1)
)
dellCurrentProbeEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dellCurrentProbeEvSys"),
        ("BASEBRDD-MIB-MIB", "dellCurrentProbeEvSub"),
        ("BASEBRDD-MIB-MIB", "dellCurrentProbeEvSol"))
)
if mibBuilder.loadTexts:
    dellCurrentProbeEvt1.setStatus(
        ""
    )

dellGlobalPowerUnitEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 0, 1)
)
dellGlobalPowerUnitEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dellGlobalPowerUnitEvSys"),
        ("BASEBRDD-MIB-MIB", "dellGlobalPowerUnitEvSub"),
        ("BASEBRDD-MIB-MIB", "dellGlobalPowerUnitEvSol"))
)
if mibBuilder.loadTexts:
    dellGlobalPowerUnitEvt1.setStatus(
        ""
    )

dellGlobalPowerUnitEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10891, 305, 0, 2)
)
dellGlobalPowerUnitEvt2.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dellGlobalPowerUnitEvSys"),
        ("BASEBRDD-MIB-MIB", "dellGlobalPowerUnitEvSub"),
        ("BASEBRDD-MIB-MIB", "dellGlobalPowerUnitEvSol"))
)
if mibBuilder.loadTexts:
    dellGlobalPowerUnitEvt2.setStatus(
        ""
    )

dellSystemChassisExtensionEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10891, 306, 0, 1)
)
dellSystemChassisExtensionEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dellSystemChassisExtensionEvSys"),
        ("BASEBRDD-MIB-MIB", "dellSystemChassisExtensionEvSub"),
        ("BASEBRDD-MIB-MIB", "dellSystemChassisExtensionEvSol"))
)
if mibBuilder.loadTexts:
    dellSystemChassisExtensionEvt1.setStatus(
        ""
    )

dellSystemResetEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10891, 312, 0, 1)
)
dellSystemResetEvt1.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("BASEBRDD-MIB-MIB", "dellSystemResetEvSys"),
        ("BASEBRDD-MIB-MIB", "dellSystemResetEvSub"),
        ("BASEBRDD-MIB-MIB", "dellSystemResetEvSol"))
)
if mibBuilder.loadTexts:
    dellSystemResetEvt1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BASEBRDD-MIB-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiCounter64": DmiCounter64,
       "DmiGauge": DmiGauge,
       "DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiCompId": DmiCompId,
       "DmiGroupId": DmiGroupId,
       "dmtf": dmtf,
       "dmtfStdMifs": dmtfStdMifs,
       "dmtfServiceLayerMIF": dmtfServiceLayerMIF,
       "dMTFComponentIDTable": dMTFComponentIDTable,
       "dMTFComponentIDEntry": dMTFComponentIDEntry,
       "manufacturerAtt1": manufacturerAtt1,
       "productAtt2": productAtt2,
       "versionAtt3": versionAtt3,
       "serialNumberAtt4": serialNumberAtt4,
       "installationAtt5": installationAtt5,
       "verifyAtt6": verifyAtt6,
       "dmtfSystemsMIF": dmtfSystemsMIF,
       "dMTFGeneralInformationTable": dMTFGeneralInformationTable,
       "dMTFGeneralInformationEntry": dMTFGeneralInformationEntry,
       "systemNameAtt1": systemNameAtt1,
       "systemLocationAtt2": systemLocationAtt2,
       "systemPrimaryUserNameAtt3": systemPrimaryUserNameAtt3,
       "systemPrimaryUserPhoneAtt4": systemPrimaryUserPhoneAtt4,
       "systemBootupTimeAtt5": systemBootupTimeAtt5,
       "systemDateTimeAtt6": systemDateTimeAtt6,
       "dMTFOperatingSystemTable": dMTFOperatingSystemTable,
       "dMTFOperatingSystemEntry": dMTFOperatingSystemEntry,
       "dMTFOperatingSystemState": dMTFOperatingSystemState,
       "operatingSystemIndexAtt1": operatingSystemIndexAtt1,
       "operatingSystemNameAtt2": operatingSystemNameAtt2,
       "operatingSystemVersionAtt3": operatingSystemVersionAtt3,
       "primaryOperatingSystemAtt4": primaryOperatingSystemAtt4,
       "operatingSystemBootDeviceStorageTypeAtt5": operatingSystemBootDeviceStorageTypeAtt5,
       "operatingSystemBootDeviceIndexAtt6": operatingSystemBootDeviceIndexAtt6,
       "operatingSystemBootPartitionIndexAtt7": operatingSystemBootPartitionIndexAtt7,
       "operatingSystemDescriptionAtt8": operatingSystemDescriptionAtt8,
       "dMTFSystemBIOSTable": dMTFSystemBIOSTable,
       "dMTFSystemBIOSEntry": dMTFSystemBIOSEntry,
       "dMTFSystemBIOSState": dMTFSystemBIOSState,
       "bIOSIndexAtt1": bIOSIndexAtt1,
       "bIOSManufacturerAtt2": bIOSManufacturerAtt2,
       "bIOSVersionAtt3": bIOSVersionAtt3,
       "bIOSROMSizeAtt4": bIOSROMSizeAtt4,
       "bIOSStartingAddressAtt5": bIOSStartingAddressAtt5,
       "bIOSEndingAddressAtt6": bIOSEndingAddressAtt6,
       "bIOSLoaderVersionAtt7": bIOSLoaderVersionAtt7,
       "bIOSReleaseDateAtt8": bIOSReleaseDateAtt8,
       "primaryBIOSAtt9": primaryBIOSAtt9,
       "dMTFProcessorTable": dMTFProcessorTable,
       "dMTFProcessorEntry": dMTFProcessorEntry,
       "dMTFProcessorState": dMTFProcessorState,
       "processorIndexAtt1": processorIndexAtt1,
       "processorTypeAtt2": processorTypeAtt2,
       "processorFamilyAtt3": processorFamilyAtt3,
       "processorVersionInformationAtt4": processorVersionInformationAtt4,
       "maximumSpeedAtt5": maximumSpeedAtt5,
       "currentSpeedAtt6": currentSpeedAtt6,
       "processorUpgradeAtt7": processorUpgradeAtt7,
       "fRUGroupIndexAtt8": fRUGroupIndexAtt8,
       "operationalGroupIndexAtt9": operationalGroupIndexAtt9,
       "level1CacheIndexAtt10": level1CacheIndexAtt10,
       "level2CacheIndexAtt11": level2CacheIndexAtt11,
       "level3CacheIndexAtt12": level3CacheIndexAtt12,
       "dMTFSystemCacheTable": dMTFSystemCacheTable,
       "dMTFSystemCacheEntry": dMTFSystemCacheEntry,
       "dMTFSystemCacheState": dMTFSystemCacheState,
       "systemCacheIndexAtt1": systemCacheIndexAtt1,
       "systemCacheLevelAtt2": systemCacheLevelAtt2,
       "systemCacheSpeedAtt3": systemCacheSpeedAtt3,
       "systemCacheSizeAtt4": systemCacheSizeAtt4,
       "systemCacheWritePolicyAtt5": systemCacheWritePolicyAtt5,
       "systemCacheErrorCorrectionAtt6": systemCacheErrorCorrectionAtt6,
       "fRUGroupIndexAtt7-1": fRUGroupIndexAtt7_1,
       "operationalGroupIndexAtt8-2": operationalGroupIndexAtt8_2,
       "systemCacheTypeAtt9": systemCacheTypeAtt9,
       "lineSizeAtt10": lineSizeAtt10,
       "volatilityAtt11": volatilityAtt11,
       "replacementPolicyAtt12": replacementPolicyAtt12,
       "readPolicyAtt13": readPolicyAtt13,
       "flushTimerAtt14": flushTimerAtt14,
       "associativityAtt15": associativityAtt15,
       "dMTFParallelPortsTable": dMTFParallelPortsTable,
       "dMTFParallelPortsEntry": dMTFParallelPortsEntry,
       "dMTFParallelPortsState": dMTFParallelPortsState,
       "parallelPortIndexAtt1": parallelPortIndexAtt1,
       "parallelBaseIOAddressAtt2": parallelBaseIOAddressAtt2,
       "iRQUsedAtt3-1": iRQUsedAtt3_1,
       "logicalNameAtt4-1": logicalNameAtt4_1,
       "connectorTypeAtt5-1": connectorTypeAtt5_1,
       "connectorPinoutAtt6": connectorPinoutAtt6,
       "dMASupportAtt7": dMASupportAtt7,
       "parallelPortCapabilitiesAtt8": parallelPortCapabilitiesAtt8,
       "operationalGroupIndexAtt9-1": operationalGroupIndexAtt9_1,
       "parallelPortSecuritySettingsAtt10": parallelPortSecuritySettingsAtt10,
       "dMTFSerialPortsTable": dMTFSerialPortsTable,
       "dMTFSerialPortsEntry": dMTFSerialPortsEntry,
       "dMTFSerialPortsState": dMTFSerialPortsState,
       "serialPortIndexAtt1": serialPortIndexAtt1,
       "serialBaseIOAddressAtt2": serialBaseIOAddressAtt2,
       "iRQUsedAtt3": iRQUsedAtt3,
       "logicalNameAtt4": logicalNameAtt4,
       "connectorTypeAtt5": connectorTypeAtt5,
       "maximumSpeedAtt6": maximumSpeedAtt6,
       "serialPortCapabilitiesAtt7": serialPortCapabilitiesAtt7,
       "operationalGroupIndexAtt8-1": operationalGroupIndexAtt8_1,
       "serialPortSecuritySettingsAtt9": serialPortSecuritySettingsAtt9,
       "dMTFPowerSupplyTable": dMTFPowerSupplyTable,
       "dMTFPowerSupplyEvt1": dMTFPowerSupplyEvt1,
       "dMTFPowerSupplyEvt2": dMTFPowerSupplyEvt2,
       "dMTFPowerSupplyEntry": dMTFPowerSupplyEntry,
       "dMTFPowerSupplyState": dMTFPowerSupplyState,
       "powerSupplyIndexAtt1": powerSupplyIndexAtt1,
       "fRUGroupIndexAtt2-1": fRUGroupIndexAtt2_1,
       "operationalGroupIndexAtt3-1": operationalGroupIndexAtt3_1,
       "powerUnitIndexAtt4": powerUnitIndexAtt4,
       "powerSupplyTypeAtt5": powerSupplyTypeAtt5,
       "inputVoltageCapabilityDescriptionAtt6": inputVoltageCapabilityDescriptionAtt6,
       "range1InputVoltageLowAtt7": range1InputVoltageLowAtt7,
       "range1InputVoltageHighAtt8": range1InputVoltageHighAtt8,
       "range1VoltageProbeIndexAtt9": range1VoltageProbeIndexAtt9,
       "range1ElectricalCurrentProbeIndexAtt10": range1ElectricalCurrentProbeIndexAtt10,
       "range2InputVoltageLowAtt11": range2InputVoltageLowAtt11,
       "range2InputVoltageHighAtt12": range2InputVoltageHighAtt12,
       "range2VoltageProbeIndexAtt13": range2VoltageProbeIndexAtt13,
       "range2CurrentProbeIndexAtt14": range2CurrentProbeIndexAtt14,
       "activeInputVoltageRangeAtt15": activeInputVoltageRangeAtt15,
       "inputVoltageRangeSwitchingAtt16": inputVoltageRangeSwitchingAtt16,
       "range1InputFrequencyLowAtt17": range1InputFrequencyLowAtt17,
       "range1InputFrequencyHighAtt18": range1InputFrequencyHighAtt18,
       "range2InputFrequencyLowAtt19": range2InputFrequencyLowAtt19,
       "range2InputFrequencyHighAtt20": range2InputFrequencyHighAtt20,
       "totalOutputPowerAtt21": totalOutputPowerAtt21,
       "dMTFPowerSupplyEvSys": dMTFPowerSupplyEvSys,
       "dMTFPowerSupplyEvSub": dMTFPowerSupplyEvSub,
       "dMTFCoolingDeviceTable": dMTFCoolingDeviceTable,
       "dMTFCoolingDeviceEvt1": dMTFCoolingDeviceEvt1,
       "dMTFCoolingDeviceEvt2": dMTFCoolingDeviceEvt2,
       "dMTFCoolingDeviceEntry": dMTFCoolingDeviceEntry,
       "dMTFCoolingDeviceState": dMTFCoolingDeviceState,
       "coolingDeviceTableIndexAtt1": coolingDeviceTableIndexAtt1,
       "fRUGroupIndexAtt2": fRUGroupIndexAtt2,
       "operationalGroupIndexAtt3": operationalGroupIndexAtt3,
       "coolingUnitIndexAtt4": coolingUnitIndexAtt4,
       "coolingDeviceTypeAtt5": coolingDeviceTypeAtt5,
       "temperatureProbeIndexAtt6": temperatureProbeIndexAtt6,
       "dMTFCoolingDeviceEvSys": dMTFCoolingDeviceEvSys,
       "dMTFCoolingDeviceEvSub": dMTFCoolingDeviceEvSub,
       "dMTFSystemSlotsTable": dMTFSystemSlotsTable,
       "dMTFSystemSlotsEntry": dMTFSystemSlotsEntry,
       "dMTFSystemSlotsState": dMTFSystemSlotsState,
       "slotIndexAtt1": slotIndexAtt1,
       "slotTypeAtt2": slotTypeAtt2,
       "slotWidthAtt3": slotWidthAtt3,
       "currentUsageAtt4": currentUsageAtt4,
       "slotDescriptionAtt5": slotDescriptionAtt5,
       "slotCategoryAtt6": slotCategoryAtt6,
       "virtualSlotAtt7": virtualSlotAtt7,
       "resourceUserIDAtt8": resourceUserIDAtt8,
       "dMTFFRUTable": dMTFFRUTable,
       "dMTFFRUEntry": dMTFFRUEntry,
       "dMTFFRUState": dMTFFRUState,
       "fRUIndexAtt1": fRUIndexAtt1,
       "deviceGroupIndexAtt2": deviceGroupIndexAtt2,
       "descriptionAtt3": descriptionAtt3,
       "manufacturerAtt4": manufacturerAtt4,
       "modelAtt5": modelAtt5,
       "partNumberAtt6": partNumberAtt6,
       "fRUSerialNumberAtt7": fRUSerialNumberAtt7,
       "revisionLevelAtt8": revisionLevelAtt8,
       "warrantyStartDateAtt9": warrantyStartDateAtt9,
       "warrantyDurationAtt10": warrantyDurationAtt10,
       "supportPhoneNumberAtt11": supportPhoneNumberAtt11,
       "fRUInternetUniformResourceLocatorAtt12": fRUInternetUniformResourceLocatorAtt12,
       "dMTFOperationalStateTable": dMTFOperationalStateTable,
       "dMTFOperationalStateEntry": dMTFOperationalStateEntry,
       "dMTFOperationalStateState": dMTFOperationalStateState,
       "operationalStateInstanceIndexAtt1": operationalStateInstanceIndexAtt1,
       "deviceGroupIndexAtt2-1": deviceGroupIndexAtt2_1,
       "operationalStatusAtt3": operationalStatusAtt3,
       "usageStateAtt4": usageStateAtt4,
       "availabilityStatusAtt5": availabilityStatusAtt5,
       "administrativeStateAtt6": administrativeStateAtt6,
       "fatalErrorCountAtt7": fatalErrorCountAtt7,
       "majorErrorCountAtt8": majorErrorCountAtt8,
       "warningErrorCountAtt9": warningErrorCountAtt9,
       "currentErrorStatusAtt10": currentErrorStatusAtt10,
       "devicePredictedFailureStatusAtt11": devicePredictedFailureStatusAtt11,
       "dMTFPhysicalMemoryArrayTable": dMTFPhysicalMemoryArrayTable,
       "dMTFPhysicalMemoryArrayEvt1": dMTFPhysicalMemoryArrayEvt1,
       "dMTFPhysicalMemoryArrayEvt2": dMTFPhysicalMemoryArrayEvt2,
       "dMTFPhysicalMemoryArrayEntry": dMTFPhysicalMemoryArrayEntry,
       "dMTFPhysicalMemoryArrayState": dMTFPhysicalMemoryArrayState,
       "memoryArrayTableIndexAtt1": memoryArrayTableIndexAtt1,
       "memoryArrayLocationAtt2": memoryArrayLocationAtt2,
       "memoryArrayUseAtt3": memoryArrayUseAtt3,
       "maximumMemoryCapacityAtt4": maximumMemoryCapacityAtt4,
       "numberOfMemoryDeviceSocketsAtt5": numberOfMemoryDeviceSocketsAtt5,
       "numberOfMemoryDeviceSocketsUsedAtt6": numberOfMemoryDeviceSocketsUsedAtt6,
       "memoryErrorCorrectionAtt7": memoryErrorCorrectionAtt7,
       "arrayErrorTypeAtt8": arrayErrorTypeAtt8,
       "lastErrorUpdateAtt9": lastErrorUpdateAtt9,
       "errorOperationAtt10": errorOperationAtt10,
       "errorDataSizeAtt11": errorDataSizeAtt11,
       "errorDataAtt12": errorDataAtt12,
       "vendorSyndromeAtt13": vendorSyndromeAtt13,
       "errorAddressAtt14": errorAddressAtt14,
       "errorResolutionAtt15": errorResolutionAtt15,
       "fRUGroupIndexAtt16": fRUGroupIndexAtt16,
       "operationalGroupIndexAtt17": operationalGroupIndexAtt17,
       "dMTFPhysicalMemoryArrayEvSys": dMTFPhysicalMemoryArrayEvSys,
       "dMTFPhysicalMemoryArrayEvSub": dMTFPhysicalMemoryArrayEvSub,
       "dMTFMemoryArrayMappedAddressesTable": dMTFMemoryArrayMappedAddressesTable,
       "dMTFMemoryArrayMappedAddressesEntry": dMTFMemoryArrayMappedAddressesEntry,
       "dMTFMemoryArrayMappedAddressesState": dMTFMemoryArrayMappedAddressesState,
       "memoryArrayMappedAddressesTableIndexAtt1": memoryArrayMappedAddressesTableIndexAtt1,
       "memoryArrayIndexAtt2": memoryArrayIndexAtt2,
       "mappedRangeStartingAddressAtt3": mappedRangeStartingAddressAtt3,
       "mappedRangeEndingAddressAtt4": mappedRangeEndingAddressAtt4,
       "partitionIDAtt5": partitionIDAtt5,
       "partitionWidthAtt6": partitionWidthAtt6,
       "operationalGroupIndexAtt7": operationalGroupIndexAtt7,
       "dMTFMemoryDeviceTable": dMTFMemoryDeviceTable,
       "dMTFMemoryDeviceEntry": dMTFMemoryDeviceEntry,
       "dMTFMemoryDeviceState": dMTFMemoryDeviceState,
       "memoryDeviceTableIndexAtt1": memoryDeviceTableIndexAtt1,
       "memoryArrayIndexAtt2-1": memoryArrayIndexAtt2_1,
       "deviceLocatorAtt3": deviceLocatorAtt3,
       "bankLocatorAtt4": bankLocatorAtt4,
       "sizeAtt5": sizeAtt5,
       "formFactorAtt6": formFactorAtt6,
       "totalWidthAtt7": totalWidthAtt7,
       "dataWidthAtt8": dataWidthAtt8,
       "memoryTypeAtt9": memoryTypeAtt9,
       "typeDetailAtt10": typeDetailAtt10,
       "deviceSetAtt11": deviceSetAtt11,
       "deviceErrorTypeAtt12": deviceErrorTypeAtt12,
       "errorGranularityAtt13": errorGranularityAtt13,
       "lastErrorUpdateAtt14": lastErrorUpdateAtt14,
       "errorOperationAtt15": errorOperationAtt15,
       "errorDataSizeAtt16": errorDataSizeAtt16,
       "errorDataAtt17": errorDataAtt17,
       "vendorSyndromeAtt18": vendorSyndromeAtt18,
       "deviceErrorAddressAtt19": deviceErrorAddressAtt19,
       "arrayErrorAddressAtt20": arrayErrorAddressAtt20,
       "errorResolutionAtt21": errorResolutionAtt21,
       "fRUGroupIndexAtt22": fRUGroupIndexAtt22,
       "operationalGroupIndexAtt23": operationalGroupIndexAtt23,
       "dMTFMemoryDeviceMappedAddressesTable": dMTFMemoryDeviceMappedAddressesTable,
       "dMTFMemoryDeviceMappedAddressesEntry": dMTFMemoryDeviceMappedAddressesEntry,
       "dMTFMemoryDeviceMappedAddressesState": dMTFMemoryDeviceMappedAddressesState,
       "memoryDeviceMappedAddressesTableIndexAtt1": memoryDeviceMappedAddressesTableIndexAtt1,
       "memoryDeviceSetIDAtt2": memoryDeviceSetIDAtt2,
       "partitionAtt3": partitionAtt3,
       "mappedRangeStartingAddressAtt4": mappedRangeStartingAddressAtt4,
       "mappedRangeEndingAddressAtt5": mappedRangeEndingAddressAtt5,
       "partitionRowPositionAtt6": partitionRowPositionAtt6,
       "interleavePositionAtt7": interleavePositionAtt7,
       "dataDepthAtt8": dataDepthAtt8,
       "dMTFSystemResources2Table": dMTFSystemResources2Table,
       "dMTFSystemResources2Entry": dMTFSystemResources2Entry,
       "dMTFSystemResources2State": dMTFSystemResources2State,
       "systemResourcesIndexAtt1": systemResourcesIndexAtt1,
       "resourceUserAtt2": resourceUserAtt2,
       "resourceSetAtt3": resourceSetAtt3,
       "resourceAssignmentAtt4": resourceAssignmentAtt4,
       "resourceTypeAtt5": resourceTypeAtt5,
       "resourceNumberAtt6": resourceNumberAtt6,
       "resourceInfoIDAtt7": resourceInfoIDAtt7,
       "startAddressAtt8": startAddressAtt8,
       "endAddressAtt9": endAddressAtt9,
       "resourceSizeAtt10": resourceSizeAtt10,
       "baseAlignmentAtt11": baseAlignmentAtt11,
       "shareableAtt12": shareableAtt12,
       "sharedAtt13": sharedAtt13,
       "dMTFSystemResourceDeviceInfoTable": dMTFSystemResourceDeviceInfoTable,
       "dMTFSystemResourceDeviceInfoEntry": dMTFSystemResourceDeviceInfoEntry,
       "dMTFSystemResourceDeviceInfoState": dMTFSystemResourceDeviceInfoState,
       "resourceUserAtt1": resourceUserAtt1,
       "deviceIDAtt2": deviceIDAtt2,
       "deviceSerialNumberAtt3": deviceSerialNumberAtt3,
       "logicalDeviceIDClassCodeAtt4": logicalDeviceIDClassCodeAtt4,
       "deviceFlagsAtt5": deviceFlagsAtt5,
       "deviceNumberAtt6": deviceNumberAtt6,
       "functionNumberAtt7": functionNumberAtt7,
       "busTypeAtt8": busTypeAtt8,
       "cMReservedAtt9": cMReservedAtt9,
       "dMTFSystemResourceMemoryInfoTable": dMTFSystemResourceMemoryInfoTable,
       "dMTFSystemResourceMemoryInfoEntry": dMTFSystemResourceMemoryInfoEntry,
       "dMTFSystemResourceMemoryInfoState": dMTFSystemResourceMemoryInfoState,
       "systemResourceMemoryInfoIndexAtt1": systemResourceMemoryInfoIndexAtt1,
       "iSAPCMCIARangeDescriptorAtt2": iSAPCMCIARangeDescriptorAtt2,
       "eISARangeDescriptorAtt3": eISARangeDescriptorAtt3,
       "decodeSupportAtt4": decodeSupportAtt4,
       "cacheableAtt5": cacheableAtt5,
       "cacheTypeAtt6": cacheTypeAtt6,
       "readWriteAtt7": readWriteAtt7,
       "dMTFSystemResourceIOInfoTable": dMTFSystemResourceIOInfoTable,
       "dMTFSystemResourceIOInfoEntry": dMTFSystemResourceIOInfoEntry,
       "dMTFSystemResourceIOInfoState": dMTFSystemResourceIOInfoState,
       "systemResourceIOInfoIndexAtt1": systemResourceIOInfoIndexAtt1,
       "iODecodeAtt2": iODecodeAtt2,
       "dMTFSystemResourceIRQInfoTable": dMTFSystemResourceIRQInfoTable,
       "dMTFSystemResourceIRQInfoEntry": dMTFSystemResourceIRQInfoEntry,
       "dMTFSystemResourceIRQInfoState": dMTFSystemResourceIRQInfoState,
       "systemResourceIRQInfoIndexAtt1": systemResourceIRQInfoIndexAtt1,
       "triggerTypeAtt2": triggerTypeAtt2,
       "triggerLevelAtt3": triggerLevelAtt3,
       "dMTFSystemResourceDMAInfoTable": dMTFSystemResourceDMAInfoTable,
       "dMTFSystemResourceDMAInfoEntry": dMTFSystemResourceDMAInfoEntry,
       "dMTFSystemResourceDMAInfoState": dMTFSystemResourceDMAInfoState,
       "systemResourceDMAInfoIndexAtt1": systemResourceDMAInfoIndexAtt1,
       "dMATransferWidthAtt2": dMATransferWidthAtt2,
       "dMAAddressSizeAtt3": dMAAddressSizeAtt3,
       "dMAMaximumTransferSizeAtt4": dMAMaximumTransferSizeAtt4,
       "dMATransferPreferenceAtt5": dMATransferPreferenceAtt5,
       "busMasterAtt6": busMasterAtt6,
       "byteModeAtt7": byteModeAtt7,
       "wordModeAtt8": wordModeAtt8,
       "channelTimingAtt9": channelTimingAtt9,
       "typeCTimingAtt10": typeCTimingAtt10,
       "dMTFSystemHardwareSecurityTable": dMTFSystemHardwareSecurityTable,
       "dMTFSystemHardwareSecurityEntry": dMTFSystemHardwareSecurityEntry,
       "powerOnPasswordStatusAtt1": powerOnPasswordStatusAtt1,
       "keyboardPasswordStatusAtt2": keyboardPasswordStatusAtt2,
       "administratorPasswordStatisAtt3": administratorPasswordStatisAtt3,
       "frontPanelResetStatusAtt4": frontPanelResetStatusAtt4,
       "dMTFSystemPowerControlsTable": dMTFSystemPowerControlsTable,
       "dMTFSystemPowerControlsEntry": dMTFSystemPowerControlsEntry,
       "powerControlRequestAtt1": powerControlRequestAtt1,
       "timedPowerOnAvailableAtt2": timedPowerOnAvailableAtt2,
       "timeToNextScheduledPowerOnAtt3": timeToNextScheduledPowerOnAtt3,
       "dMTFVoltageProbeTable": dMTFVoltageProbeTable,
       "dMTFVoltageProbeEvt1": dMTFVoltageProbeEvt1,
       "dMTFVoltageProbeEntry": dMTFVoltageProbeEntry,
       "dMTFVoltageProbeState": dMTFVoltageProbeState,
       "voltageProbeIndexAtt1": voltageProbeIndexAtt1,
       "voltageProbeLocationAtt2": voltageProbeLocationAtt2,
       "voltageProbeDescriptionAtt3": voltageProbeDescriptionAtt3,
       "voltageStatusAtt4": voltageStatusAtt4,
       "voltageProbeVoltageLevelAtt5": voltageProbeVoltageLevelAtt5,
       "monitoredVoltageNominalLevelAtt6": monitoredVoltageNominalLevelAtt6,
       "monitoredVoltageNormalMaximumAtt7": monitoredVoltageNormalMaximumAtt7,
       "monitoredVoltageNormalMinimumAtt8": monitoredVoltageNormalMinimumAtt8,
       "voltageProbeMaximumAtt9": voltageProbeMaximumAtt9,
       "voltageProbeMinimumAtt10": voltageProbeMinimumAtt10,
       "voltageLevelLowerThresholdNonCriticalAtt11": voltageLevelLowerThresholdNonCriticalAtt11,
       "voltageLevelUpperThresholdNonCriticalAtt12": voltageLevelUpperThresholdNonCriticalAtt12,
       "voltageLevelLowerThresholdCriticalAtt13": voltageLevelLowerThresholdCriticalAtt13,
       "voltageLevelUpperThresholdCriticalAtt14": voltageLevelUpperThresholdCriticalAtt14,
       "voltageLevelLowerThresholdNonRecoverableAtt15": voltageLevelLowerThresholdNonRecoverableAtt15,
       "voltageLevelUpperThresholdNonRecoverableAtt16": voltageLevelUpperThresholdNonRecoverableAtt16,
       "voltageProbeResolutionAtt17": voltageProbeResolutionAtt17,
       "voltageProbeToleranceAtt18": voltageProbeToleranceAtt18,
       "voltageProbeAccuracyAtt19": voltageProbeAccuracyAtt19,
       "fRUGroupIndexAtt20-2": fRUGroupIndexAtt20_2,
       "operationalGroupIndexAtt21-2": operationalGroupIndexAtt21_2,
       "dMTFVoltageProbeEvSys": dMTFVoltageProbeEvSys,
       "dMTFVoltageProbeEvSub": dMTFVoltageProbeEvSub,
       "dMTFTemperatureProbeTable": dMTFTemperatureProbeTable,
       "dMTFTemperatureProbeEvt1": dMTFTemperatureProbeEvt1,
       "dMTFTemperatureProbeEntry": dMTFTemperatureProbeEntry,
       "dMTFTemperatureProbeState": dMTFTemperatureProbeState,
       "temperatureProbeTableIndexAtt1": temperatureProbeTableIndexAtt1,
       "temperatureProbeLocationAtt2": temperatureProbeLocationAtt2,
       "temperatureProbeDescriptionAtt3": temperatureProbeDescriptionAtt3,
       "temperatureStatusAtt4": temperatureStatusAtt4,
       "temperatureProbeTemperatureReadingAtt5": temperatureProbeTemperatureReadingAtt5,
       "monitoredTemperatureNominalReadingAtt6": monitoredTemperatureNominalReadingAtt6,
       "monitoredTemperatureNormalMaximumAtt7": monitoredTemperatureNormalMaximumAtt7,
       "monitoredTemperatureNormalMinimumAtt8": monitoredTemperatureNormalMinimumAtt8,
       "temperatureProbeMaximumAtt9": temperatureProbeMaximumAtt9,
       "temperatureProbeMinimumAtt10": temperatureProbeMinimumAtt10,
       "temperatureReadingLowerThresholdNonCriticalAtt11": temperatureReadingLowerThresholdNonCriticalAtt11,
       "temperatureReadingUpperThresholdNonCriticalAtt12": temperatureReadingUpperThresholdNonCriticalAtt12,
       "temperatureReadingLowerThresholdCriticalAtt13": temperatureReadingLowerThresholdCriticalAtt13,
       "temperatureReadingUpperThresholdCriticalAtt14": temperatureReadingUpperThresholdCriticalAtt14,
       "temperatureReadingLowerThresholdNonRecoverableAtt15": temperatureReadingLowerThresholdNonRecoverableAtt15,
       "temperatureReadingUpperThresholdNonRecoverableAtt16": temperatureReadingUpperThresholdNonRecoverableAtt16,
       "temperatureProbeResolutionAtt17": temperatureProbeResolutionAtt17,
       "temperatureProbeToleranceAtt18": temperatureProbeToleranceAtt18,
       "temperatureProbeAccuracyAtt19": temperatureProbeAccuracyAtt19,
       "fRUGroupIndexAtt20-1": fRUGroupIndexAtt20_1,
       "operationalGroupIndexAtt21-1": operationalGroupIndexAtt21_1,
       "dMTFTemperatureProbeEvSys": dMTFTemperatureProbeEvSys,
       "dMTFTemperatureProbeEvSub": dMTFTemperatureProbeEvSub,
       "dMTFElectricalCurrentProbeTable": dMTFElectricalCurrentProbeTable,
       "dMTFElectricalCurrentProbeEvt1": dMTFElectricalCurrentProbeEvt1,
       "dMTFElectricalCurrentProbeEvt2": dMTFElectricalCurrentProbeEvt2,
       "dMTFElectricalCurrentProbeEntry": dMTFElectricalCurrentProbeEntry,
       "dMTFElectricalCurrentProbeState": dMTFElectricalCurrentProbeState,
       "electricalCurrentProbeTableIndexAtt1": electricalCurrentProbeTableIndexAtt1,
       "electricalCurrentProbeLocationAtt2": electricalCurrentProbeLocationAtt2,
       "electricalCurrentProbeDescriptionAtt3": electricalCurrentProbeDescriptionAtt3,
       "electricalCurrentStatusAtt4": electricalCurrentStatusAtt4,
       "electricalCurrentProbeReadingAtt5": electricalCurrentProbeReadingAtt5,
       "monitoredElectricalCurrentNominalReadingAtt6": monitoredElectricalCurrentNominalReadingAtt6,
       "monitoredElectricalCurrentNormalMaximumAtt7": monitoredElectricalCurrentNormalMaximumAtt7,
       "monitoredElectricalCurrentNormalMinimumAtt8": monitoredElectricalCurrentNormalMinimumAtt8,
       "electricalCurrentProbeMaximumAtt9": electricalCurrentProbeMaximumAtt9,
       "electricalCurrentProbeMinimumAtt10": electricalCurrentProbeMinimumAtt10,
       "electricalCurrentReadingLowerThresholdNonCriticalAtt11": electricalCurrentReadingLowerThresholdNonCriticalAtt11,
       "electricalCurrentReadingUpperThresholdNonCriticalAtt12": electricalCurrentReadingUpperThresholdNonCriticalAtt12,
       "electricalCurrentReadingLowerThresholdCriticalAtt13": electricalCurrentReadingLowerThresholdCriticalAtt13,
       "currentReadingUpperThresholdCriticalAtt14": currentReadingUpperThresholdCriticalAtt14,
       "electricalCurrentReadingLowerThresholdNonRecoverabAtt15": electricalCurrentReadingLowerThresholdNonRecoverabAtt15,
       "electricalCurrentReadingUpperThresholdNonRecoverabAtt16": electricalCurrentReadingUpperThresholdNonRecoverabAtt16,
       "electricalCurrentProbeResolutionAtt17": electricalCurrentProbeResolutionAtt17,
       "electricalCurrentProbeToleranceAtt18": electricalCurrentProbeToleranceAtt18,
       "electricalCurrentProbeAccuracyAtt19": electricalCurrentProbeAccuracyAtt19,
       "fRUGroupIndexAtt20": fRUGroupIndexAtt20,
       "operationalGroupIndexAtt21": operationalGroupIndexAtt21,
       "dMTFElectricalCurrentProbeEvSys": dMTFElectricalCurrentProbeEvSys,
       "dMTFElectricalCurrentProbeEvSub": dMTFElectricalCurrentProbeEvSub,
       "dMTFPhysicalContainerGlobalTableTable": dMTFPhysicalContainerGlobalTableTable,
       "dMTFPhysicalContainerGlobalTableEvt1": dMTFPhysicalContainerGlobalTableEvt1,
       "dMTFPhysicalContainerGlobalTableEvt2": dMTFPhysicalContainerGlobalTableEvt2,
       "dMTFPhysicalContainerGlobalTableEvt3": dMTFPhysicalContainerGlobalTableEvt3,
       "dMTFPhysicalContainerGlobalTableEvt4": dMTFPhysicalContainerGlobalTableEvt4,
       "dMTFPhysicalContainerGlobalTableEvt5": dMTFPhysicalContainerGlobalTableEvt5,
       "dMTFPhysicalContainerGlobalTableEvt6": dMTFPhysicalContainerGlobalTableEvt6,
       "dMTFPhysicalContainerGlobalTableEvt7": dMTFPhysicalContainerGlobalTableEvt7,
       "dMTFPhysicalContainerGlobalTableEntry": dMTFPhysicalContainerGlobalTableEntry,
       "dMTFPhysicalContainerGlobalTableState": dMTFPhysicalContainerGlobalTableState,
       "containerOrChassisTypeAtt1": containerOrChassisTypeAtt1,
       "assetTagAtt2": assetTagAtt2,
       "chassisLockPresentAtt3": chassisLockPresentAtt3,
       "bootupStateAtt4": bootupStateAtt4,
       "powerStateAtt5": powerStateAtt5,
       "thermalStateAtt6": thermalStateAtt6,
       "fRUGroupIndexAtt7": fRUGroupIndexAtt7,
       "operationalGroupIndexAtt8": operationalGroupIndexAtt8,
       "containerIndexAtt9": containerIndexAtt9,
       "containerNameAtt10": containerNameAtt10,
       "containerLocationAtt11": containerLocationAtt11,
       "containerSecurityStatusAtt12": containerSecurityStatusAtt12,
       "dMTFPhysicalContainerGlobalTableEvSys": dMTFPhysicalContainerGlobalTableEvSys,
       "dMTFPhysicalContainerGlobalTableEvSub": dMTFPhysicalContainerGlobalTableEvSub,
       "dMTFPowerUnitGlobalTableTable": dMTFPowerUnitGlobalTableTable,
       "dMTFPowerUnitGlobalTableEntry": dMTFPowerUnitGlobalTableEntry,
       "dMTFPowerUnitGlobalTableState": dMTFPowerUnitGlobalTableState,
       "powerUnitIndexAtt1": powerUnitIndexAtt1,
       "powerUnitRedundancyStatusAtt2": powerUnitRedundancyStatusAtt2,
       "dmtfDynOids": dmtfDynOids,
       "dmiDynOid386845712": dmiDynOid386845712,
       "dmiDynOid73111109": dmiDynOid73111109,
       "dmiDynOid3922453424": dmiDynOid3922453424,
       "iNTELMIFTOMIBTable": iNTELMIFTOMIBTable,
       "iNTELMIFTOMIBEntry": iNTELMIFTOMIBEntry,
       "dellBaseBoardMIBAtt1": dellBaseBoardMIBAtt1,
       "mIBOIDAtt2": mIBOIDAtt2,
       "disableTrapsAtt3": disableTrapsAtt3,
       "dell": dell,
       "server2": server2,
       "dellTemperatureProbeTable": dellTemperatureProbeTable,
       "dellTemperatureProbeEvt1": dellTemperatureProbeEvt1,
       "dellTemperatureProbeEntry": dellTemperatureProbeEntry,
       "dellTemperatureProbeState": dellTemperatureProbeState,
       "tempParentIndexAtt1": tempParentIndexAtt1,
       "tempIndexAtt2": tempIndexAtt2,
       "tempTypeAtt3": tempTypeAtt3,
       "tempStatusAtt4": tempStatusAtt4,
       "tempReadingAtt5": tempReadingAtt5,
       "tempMinWarnAtt6": tempMinWarnAtt6,
       "tempMaxWarnAtt7": tempMaxWarnAtt7,
       "tempMinFailAtt8": tempMinFailAtt8,
       "tempMaxFailAtt9": tempMaxFailAtt9,
       "tempLocationAtt10": tempLocationAtt10,
       "dellTemperatureProbeEvSys": dellTemperatureProbeEvSys,
       "dellTemperatureProbeEvSub": dellTemperatureProbeEvSub,
       "dellTemperatureProbeEvSol": dellTemperatureProbeEvSol,
       "dellFanSensorTable": dellFanSensorTable,
       "dellFanSensorEvt1": dellFanSensorEvt1,
       "dellFanSensorEntry": dellFanSensorEntry,
       "dellFanSensorState": dellFanSensorState,
       "fansParentIndexAtt1": fansParentIndexAtt1,
       "fansIndexAtt2": fansIndexAtt2,
       "fansTypeAtt3": fansTypeAtt3,
       "fansStatusAtt4": fansStatusAtt4,
       "fansReadingAtt5": fansReadingAtt5,
       "fansWarningMinAtt6": fansWarningMinAtt6,
       "fansMaxWarnAtt7": fansMaxWarnAtt7,
       "fansMinFailAtt8": fansMinFailAtt8,
       "fansMaxFailAtt9": fansMaxFailAtt9,
       "fansLocationAtt10": fansLocationAtt10,
       "dellFanSensorEvSys": dellFanSensorEvSys,
       "dellFanSensorEvSub": dellFanSensorEvSub,
       "dellFanSensorEvSol": dellFanSensorEvSol,
       "dellVoltageProbeTable": dellVoltageProbeTable,
       "dellVoltageProbeEvt1": dellVoltageProbeEvt1,
       "dellVoltageProbeEntry": dellVoltageProbeEntry,
       "dellVoltageProbeState": dellVoltageProbeState,
       "voltParentIndexAtt1": voltParentIndexAtt1,
       "voltIndexAtt2": voltIndexAtt2,
       "voltTypeAtt3": voltTypeAtt3,
       "voltStatusAtt4": voltStatusAtt4,
       "voltReadingAtt5": voltReadingAtt5,
       "voltMinWarnAtt6": voltMinWarnAtt6,
       "voltMaxWarnAtt7": voltMaxWarnAtt7,
       "voltMinFailAtt8": voltMinFailAtt8,
       "voltMaxFailAtt9": voltMaxFailAtt9,
       "voltLocationAtt10": voltLocationAtt10,
       "dellVoltageProbeEvSys": dellVoltageProbeEvSys,
       "dellVoltageProbeEvSub": dellVoltageProbeEvSub,
       "dellVoltageProbeEvSol": dellVoltageProbeEvSol,
       "dellCurrentProbeTable": dellCurrentProbeTable,
       "dellCurrentProbeEvt1": dellCurrentProbeEvt1,
       "dellCurrentProbeEntry": dellCurrentProbeEntry,
       "dellCurrentProbeState": dellCurrentProbeState,
       "ampParentIndexAtt1": ampParentIndexAtt1,
       "ampIndexAtt2": ampIndexAtt2,
       "ampTypeAtt3": ampTypeAtt3,
       "ampStatusAtt4": ampStatusAtt4,
       "ampReadingAtt5": ampReadingAtt5,
       "ampMinWarnAtt6": ampMinWarnAtt6,
       "ampMaxWarnAtt7": ampMaxWarnAtt7,
       "ampMinFailAtt8": ampMinFailAtt8,
       "ampMaxFailAtt9": ampMaxFailAtt9,
       "ampLocationAtt10": ampLocationAtt10,
       "dellCurrentProbeEvSys": dellCurrentProbeEvSys,
       "dellCurrentProbeEvSub": dellCurrentProbeEvSub,
       "dellCurrentProbeEvSol": dellCurrentProbeEvSol,
       "dellRedundantPowerSupplyTable": dellRedundantPowerSupplyTable,
       "dellRedundantPowerSupplyEntry": dellRedundantPowerSupplyEntry,
       "dellRedundantPowerSupplyState": dellRedundantPowerSupplyState,
       "pwrSupplyParentIndexAtt1": pwrSupplyParentIndexAtt1,
       "pwrSupplyIndexAtt2": pwrSupplyIndexAtt2,
       "pwrSupplyTypeAtt3": pwrSupplyTypeAtt3,
       "pwrSupplyStatusAtt4": pwrSupplyStatusAtt4,
       "pwrSupplyOnlineAtt5": pwrSupplyOnlineAtt5,
       "pwrLocationAtt6": pwrLocationAtt6,
       "dellGlobalPowerUnitTable": dellGlobalPowerUnitTable,
       "dellGlobalPowerUnitEvt1": dellGlobalPowerUnitEvt1,
       "dellGlobalPowerUnitEvt2": dellGlobalPowerUnitEvt2,
       "dellGlobalPowerUnitEntry": dellGlobalPowerUnitEntry,
       "dellGlobalPowerUnitState": dellGlobalPowerUnitState,
       "pwrUnitStatusAtt1": pwrUnitStatusAtt1,
       "pwrUnitGlobalLevelAtt2": pwrUnitGlobalLevelAtt2,
       "pwrUnitGlobalMaxWarnAtt3": pwrUnitGlobalMaxWarnAtt3,
       "pwrUnitLevel33vAtt4": pwrUnitLevel33vAtt4,
       "pwrUnitMaxWarn33vAtt5": pwrUnitMaxWarn33vAtt5,
       "pwrUnitLevel5vAtt6": pwrUnitLevel5vAtt6,
       "pwrUnitMaxWarn5vAtt7": pwrUnitMaxWarn5vAtt7,
       "pwrUnitLevel12vAtt8": pwrUnitLevel12vAtt8,
       "pwrUnitMaxWarn12vAtt9": pwrUnitMaxWarn12vAtt9,
       "pwrUnitUidAtt10": pwrUnitUidAtt10,
       "pwrUnitIndexAtt11": pwrUnitIndexAtt11,
       "dellGlobalPowerUnitEvSys": dellGlobalPowerUnitEvSys,
       "dellGlobalPowerUnitEvSub": dellGlobalPowerUnitEvSub,
       "dellGlobalPowerUnitEvSol": dellGlobalPowerUnitEvSol,
       "dellSystemChassisExtensionTable": dellSystemChassisExtensionTable,
       "dellSystemChassisExtensionEvt1": dellSystemChassisExtensionEvt1,
       "dellSystemChassisExtensionEntry": dellSystemChassisExtensionEntry,
       "dellSystemChassisExtensionState": dellSystemChassisExtensionState,
       "chassIndexAtt1": chassIndexAtt1,
       "chassGlobStatusAtt2": chassGlobStatusAtt2,
       "chassTempStatusAtt3": chassTempStatusAtt3,
       "chassTempProbesAtt4": chassTempProbesAtt4,
       "chassFansStatusAtt5": chassFansStatusAtt5,
       "chassFansProbesAtt6": chassFansProbesAtt6,
       "chassVoltStatusAtt7": chassVoltStatusAtt7,
       "chassVoltProbesAtt8": chassVoltProbesAtt8,
       "chassAmpStatusAtt9": chassAmpStatusAtt9,
       "chassAmpProbesAtt10": chassAmpProbesAtt10,
       "chassPsStatusAtt11": chassPsStatusAtt11,
       "chassPwrSuppliesAtt12": chassPwrSuppliesAtt12,
       "chassServiceTagAtt13": chassServiceTagAtt13,
       "chassUidAtt14": chassUidAtt14,
       "chassBackPlaneUidAtt15": chassBackPlaneUidAtt15,
       "chassIdentifyAtt16": chassIdentifyAtt16,
       "chassFanControlAtt17": chassFanControlAtt17,
       "chassLEDConfigAtt18": chassLEDConfigAtt18,
       "chassFaultClearAtt19": chassFaultClearAtt19,
       "chassThermalShutdownAtt20": chassThermalShutdownAtt20,
       "chassMemStatusAtt21": chassMemStatusAtt21,
       "chassMemDevicesAtt22": chassMemDevicesAtt22,
       "dellSystemChassisExtensionEvSys": dellSystemChassisExtensionEvSys,
       "dellSystemChassisExtensionEvSub": dellSystemChassisExtensionEvSub,
       "dellSystemChassisExtensionEvSol": dellSystemChassisExtensionEvSol,
       "dellEsmLogTable": dellEsmLogTable,
       "dellEsmLogEntry": dellEsmLogEntry,
       "dellEsmLogState": dellEsmLogState,
       "esmLogIndexAtt1": esmLogIndexAtt1,
       "esmLogDataAtt2": esmLogDataAtt2,
       "dellPOSTLogTable": dellPOSTLogTable,
       "dellPOSTLogEntry": dellPOSTLogEntry,
       "dellPOSTLogState": dellPOSTLogState,
       "postLogIndexAtt1": postLogIndexAtt1,
       "postLogDataAtt2": postLogDataAtt2,
       "dellSecurityTable": dellSecurityTable,
       "dellSecurityEntry": dellSecurityEntry,
       "dellSecurityState": dellSecurityState,
       "userIndexAtt1": userIndexAtt1,
       "userNameAtt2": userNameAtt2,
       "userControlAtt3": userControlAtt3,
       "requestAtt4": requestAtt4,
       "dellDialupTable": dellDialupTable,
       "dellDialupEntry": dellDialupEntry,
       "dialupCapabilityAtt1": dialupCapabilityAtt1,
       "callbackNumberAtt2": callbackNumberAtt2,
       "dellFirmwareTable": dellFirmwareTable,
       "dellFirmwareEntry": dellFirmwareEntry,
       "dellFirmwareState": dellFirmwareState,
       "firmwareChassisIndexAtt1": firmwareChassisIndexAtt1,
       "firmwareIndexAtt2": firmwareIndexAtt2,
       "firmwareTypeAtt3": firmwareTypeAtt3,
       "firmwareVersionAtt4": firmwareVersionAtt4,
       "firmwareStatusAtt5": firmwareStatusAtt5,
       "dellSystemResetTable": dellSystemResetTable,
       "dellSystemResetEvt1": dellSystemResetEvt1,
       "dellSystemResetEntry": dellSystemResetEntry,
       "automaticCapabilitiesAtt1": automaticCapabilitiesAtt1,
       "automaticSettingsAtt2": automaticSettingsAtt2,
       "notificationNumberAtt3": notificationNumberAtt3,
       "manualCapabilitiesAtt4": manualCapabilitiesAtt4,
       "manualControlAtt5": manualControlAtt5,
       "automaticSystemResetTimerAtt6": automaticSystemResetTimerAtt6,
       "dellSystemResetEvSys": dellSystemResetEvSys,
       "dellSystemResetEvSub": dellSystemResetEvSub,
       "dellSystemResetEvSol": dellSystemResetEvSol,
       "dELLSystemsManagementSoftwareTable": dELLSystemsManagementSoftwareTable,
       "dELLSystemsManagementSoftwareEntry": dELLSystemsManagementSoftwareEntry,
       "productAtt1": productAtt1,
       "versionAtt2": versionAtt2,
       "buildNumberAtt3": buildNumberAtt3,
       "descriptionAtt4": descriptionAtt4,
       "supportedProtocolsAtt5": supportedProtocolsAtt5,
       "preferredProtocolAtt6": preferredProtocolAtt6,
       "dMIRPCTypesAtt7": dMIRPCTypesAtt7,
       "dELLSystemsSummaryInformationTable": dELLSystemsSummaryInformationTable,
       "dELLSystemsSummaryInformationEntry": dELLSystemsSummaryInformationEntry,
       "operatingSystemAtt1": operatingSystemAtt1,
       "systemClassAtt2": systemClassAtt2,
       "dellMemoryPrefailureTable": dellMemoryPrefailureTable,
       "dellMemoryPrefailureEntry": dellMemoryPrefailureEntry,
       "dellMemoryPrefailureState": dellMemoryPrefailureState,
       "memoryDeviceIndexAtt1": memoryDeviceIndexAtt1,
       "resetMemoryDeviceErrorCountAndPrefailureStatusAtt2": resetMemoryDeviceErrorCountAndPrefailureStatusAtt2}
)
