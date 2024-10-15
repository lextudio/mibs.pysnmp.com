# SNMP MIB module (SNIA-SML-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNIA-SML-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:50 2024
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



class UShortReal(Integer32):
    """Custom type UShortReal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class CimDateTime(OctetString):
    """Custom type CimDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )





class UINT64(OctetString):
    """Custom type UINT64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class UINT32(Integer32):
    """Custom type UINT32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class UINT16(Integer32):
    """Custom type UINT16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Snia_ObjectIdentity = ObjectIdentity
snia = _Snia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 2)
)
_Libraries_ObjectIdentity = ObjectIdentity
libraries = _Libraries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3)
)
_SmlRoot_ObjectIdentity = ObjectIdentity
smlRoot = _SmlRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1)
)


class _SmlMibVersion_Type(DisplayString):
    """Custom type smlMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SmlMibVersion_Type.__name__ = "DisplayString"
_SmlMibVersion_Object = MibScalar
smlMibVersion = _SmlMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 1),
    _SmlMibVersion_Type()
)
smlMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smlMibVersion.setStatus("mandatory")


class _SmlCimVersion_Type(DisplayString):
    """Custom type smlCimVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SmlCimVersion_Type.__name__ = "DisplayString"
_SmlCimVersion_Object = MibScalar
smlCimVersion = _SmlCimVersion_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 2),
    _SmlCimVersion_Type()
)
smlCimVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smlCimVersion.setStatus("mandatory")
_ProductGroup_ObjectIdentity = ObjectIdentity
productGroup = _ProductGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 3)
)


class _Product_Name_Type(DisplayString):
    """Custom type product_Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_Name_Type.__name__ = "DisplayString"
_Product_Name_Object = MibScalar
product_Name = _Product_Name_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 3, 1),
    _Product_Name_Type()
)
product_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product_Name.setStatus("mandatory")


class _Product_IdentifyingNumber_Type(DisplayString):
    """Custom type product_IdentifyingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_IdentifyingNumber_Type.__name__ = "DisplayString"
_Product_IdentifyingNumber_Object = MibScalar
product_IdentifyingNumber = _Product_IdentifyingNumber_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 3, 2),
    _Product_IdentifyingNumber_Type()
)
product_IdentifyingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product_IdentifyingNumber.setStatus("mandatory")


class _Product_Vendor_Type(DisplayString):
    """Custom type product_Vendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_Vendor_Type.__name__ = "DisplayString"
_Product_Vendor_Object = MibScalar
product_Vendor = _Product_Vendor_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 3, 3),
    _Product_Vendor_Type()
)
product_Vendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product_Vendor.setStatus("mandatory")


class _Product_Version_Type(DisplayString):
    """Custom type product_Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_Version_Type.__name__ = "DisplayString"
_Product_Version_Object = MibScalar
product_Version = _Product_Version_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 3, 4),
    _Product_Version_Type()
)
product_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product_Version.setStatus("mandatory")


class _Product_ElementName_Type(DisplayString):
    """Custom type product_ElementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_ElementName_Type.__name__ = "DisplayString"
_Product_ElementName_Object = MibScalar
product_ElementName = _Product_ElementName_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 3, 5),
    _Product_ElementName_Type()
)
product_ElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product_ElementName.setStatus("mandatory")
_ChassisGroup_ObjectIdentity = ObjectIdentity
chassisGroup = _ChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4)
)


class _Chassis_Manufacturer_Type(DisplayString):
    """Custom type chassis_Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chassis_Manufacturer_Type.__name__ = "DisplayString"
_Chassis_Manufacturer_Object = MibScalar
chassis_Manufacturer = _Chassis_Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 1),
    _Chassis_Manufacturer_Type()
)
chassis_Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_Manufacturer.setStatus("mandatory")


class _Chassis_Model_Type(DisplayString):
    """Custom type chassis_Model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Chassis_Model_Type.__name__ = "DisplayString"
_Chassis_Model_Object = MibScalar
chassis_Model = _Chassis_Model_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 2),
    _Chassis_Model_Type()
)
chassis_Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_Model.setStatus("mandatory")


class _Chassis_SerialNumber_Type(DisplayString):
    """Custom type chassis_SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Chassis_SerialNumber_Type.__name__ = "DisplayString"
_Chassis_SerialNumber_Object = MibScalar
chassis_SerialNumber = _Chassis_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 3),
    _Chassis_SerialNumber_Type()
)
chassis_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_SerialNumber.setStatus("mandatory")


class _Chassis_LockPresent_Type(Integer32):
    """Custom type chassis_LockPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_Chassis_LockPresent_Type.__name__ = "Integer32"
_Chassis_LockPresent_Object = MibScalar
chassis_LockPresent = _Chassis_LockPresent_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 4),
    _Chassis_LockPresent_Type()
)
chassis_LockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_LockPresent.setStatus("mandatory")


class _Chassis_SecurityBreach_Type(Integer32):
    """Custom type chassis_SecurityBreach based on Integer32"""
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
        *(("breachAttempted", 4),
          ("breachSuccessful", 5),
          ("noBreach", 3),
          ("other", 2),
          ("unknown", 1))
    )


_Chassis_SecurityBreach_Type.__name__ = "Integer32"
_Chassis_SecurityBreach_Object = MibScalar
chassis_SecurityBreach = _Chassis_SecurityBreach_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 5),
    _Chassis_SecurityBreach_Type()
)
chassis_SecurityBreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_SecurityBreach.setStatus("mandatory")


class _Chassis_IsLocked_Type(Integer32):
    """Custom type chassis_IsLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_Chassis_IsLocked_Type.__name__ = "Integer32"
_Chassis_IsLocked_Object = MibScalar
chassis_IsLocked = _Chassis_IsLocked_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 6),
    _Chassis_IsLocked_Type()
)
chassis_IsLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_IsLocked.setStatus("mandatory")


class _Chassis_Tag_Type(DisplayString):
    """Custom type chassis_Tag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chassis_Tag_Type.__name__ = "DisplayString"
_Chassis_Tag_Object = MibScalar
chassis_Tag = _Chassis_Tag_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 7),
    _Chassis_Tag_Type()
)
chassis_Tag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_Tag.setStatus("mandatory")


class _Chassis_ElementName_Type(DisplayString):
    """Custom type chassis_ElementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chassis_ElementName_Type.__name__ = "DisplayString"
_Chassis_ElementName_Object = MibScalar
chassis_ElementName = _Chassis_ElementName_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 8),
    _Chassis_ElementName_Type()
)
chassis_ElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis_ElementName.setStatus("mandatory")
_NumberOfsubChassis_Type = Integer32
_NumberOfsubChassis_Object = MibScalar
numberOfsubChassis = _NumberOfsubChassis_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 9),
    _NumberOfsubChassis_Type()
)
numberOfsubChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfsubChassis.setStatus("mandatory")
_SubChassisTable_Object = MibTable
subChassisTable = _SubChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10)
)
if mibBuilder.loadTexts:
    subChassisTable.setStatus("mandatory")
_SubChassisEntry_Object = MibTableRow
subChassisEntry = _SubChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1)
)
subChassisEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "subChassisIndex"),
)
if mibBuilder.loadTexts:
    subChassisEntry.setStatus("mandatory")
_SubChassisIndex_Type = UINT32
_SubChassisIndex_Object = MibTableColumn
subChassisIndex = _SubChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 1),
    _SubChassisIndex_Type()
)
subChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassisIndex.setStatus("mandatory")


class _SubChassis_Manufacturer_Type(DisplayString):
    """Custom type subChassis_Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SubChassis_Manufacturer_Type.__name__ = "DisplayString"
_SubChassis_Manufacturer_Object = MibScalar
subChassis_Manufacturer = _SubChassis_Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 2),
    _SubChassis_Manufacturer_Type()
)
subChassis_Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_Manufacturer.setStatus("mandatory")


class _SubChassis_Model_Type(DisplayString):
    """Custom type subChassis_Model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SubChassis_Model_Type.__name__ = "DisplayString"
_SubChassis_Model_Object = MibScalar
subChassis_Model = _SubChassis_Model_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 3),
    _SubChassis_Model_Type()
)
subChassis_Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_Model.setStatus("mandatory")


class _SubChassis_SerialNumber_Type(DisplayString):
    """Custom type subChassis_SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SubChassis_SerialNumber_Type.__name__ = "DisplayString"
_SubChassis_SerialNumber_Object = MibScalar
subChassis_SerialNumber = _SubChassis_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 4),
    _SubChassis_SerialNumber_Type()
)
subChassis_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_SerialNumber.setStatus("mandatory")


class _SubChassis_LockPresent_Type(Integer32):
    """Custom type subChassis_LockPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_SubChassis_LockPresent_Type.__name__ = "Integer32"
_SubChassis_LockPresent_Object = MibScalar
subChassis_LockPresent = _SubChassis_LockPresent_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 5),
    _SubChassis_LockPresent_Type()
)
subChassis_LockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_LockPresent.setStatus("mandatory")


class _SubChassis_SecurityBreach_Type(Integer32):
    """Custom type subChassis_SecurityBreach based on Integer32"""
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
        *(("breachAttempted", 4),
          ("breachSuccessful", 5),
          ("noBreach", 3),
          ("other", 2),
          ("unknown", 1))
    )


_SubChassis_SecurityBreach_Type.__name__ = "Integer32"
_SubChassis_SecurityBreach_Object = MibScalar
subChassis_SecurityBreach = _SubChassis_SecurityBreach_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 6),
    _SubChassis_SecurityBreach_Type()
)
subChassis_SecurityBreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_SecurityBreach.setStatus("mandatory")


class _SubChassis_IsLocked_Type(Integer32):
    """Custom type subChassis_IsLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_SubChassis_IsLocked_Type.__name__ = "Integer32"
_SubChassis_IsLocked_Object = MibScalar
subChassis_IsLocked = _SubChassis_IsLocked_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 7),
    _SubChassis_IsLocked_Type()
)
subChassis_IsLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_IsLocked.setStatus("mandatory")


class _SubChassis_Tag_Type(DisplayString):
    """Custom type subChassis_Tag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SubChassis_Tag_Type.__name__ = "DisplayString"
_SubChassis_Tag_Object = MibScalar
subChassis_Tag = _SubChassis_Tag_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 8),
    _SubChassis_Tag_Type()
)
subChassis_Tag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_Tag.setStatus("mandatory")


class _SubChassis_ElementName_Type(DisplayString):
    """Custom type subChassis_ElementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SubChassis_ElementName_Type.__name__ = "DisplayString"
_SubChassis_ElementName_Object = MibScalar
subChassis_ElementName = _SubChassis_ElementName_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 9),
    _SubChassis_ElementName_Type()
)
subChassis_ElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_ElementName.setStatus("mandatory")


class _SubChassis_OperationalStatus_Type(Integer32):
    """Custom type subChassis_OperationalStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("completed", 17),
          ("dMTFReserved", 19),
          ("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("inService", 11),
          ("lostCommunication", 13),
          ("noContact", 12),
          ("non-RecoverableError", 7),
          ("ok", 2),
          ("other", 1),
          ("powerMode", 18),
          ("predictiveFailure", 5),
          ("starting", 8),
          ("stopped", 10),
          ("stopping", 9),
          ("stressed", 4),
          ("supportingEntityInError", 16),
          ("unknown", 0),
          ("vendorReserved", 32768))
    )


_SubChassis_OperationalStatus_Type.__name__ = "Integer32"
_SubChassis_OperationalStatus_Object = MibScalar
subChassis_OperationalStatus = _SubChassis_OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 10),
    _SubChassis_OperationalStatus_Type()
)
subChassis_OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_OperationalStatus.setStatus("mandatory")


class _SubChassis_PackageType_Type(Integer32):
    """Custom type subChassis_PackageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              17,
              18,
              19,
              32769)
        )
    )
    namedValues = NamedValues(
        *(("expansionChassis", 18),
          ("mainSystemChassis", 17),
          ("serviceBay", 32769),
          ("subChassis", 19),
          ("unknown", 0))
    )


_SubChassis_PackageType_Type.__name__ = "Integer32"
_SubChassis_PackageType_Object = MibScalar
subChassis_PackageType = _SubChassis_PackageType_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 4, 10, 1, 11),
    _SubChassis_PackageType_Type()
)
subChassis_PackageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subChassis_PackageType.setStatus("mandatory")
_StorageLibraryGroup_ObjectIdentity = ObjectIdentity
storageLibraryGroup = _StorageLibraryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 5)
)


class _StorageLibrary_Name_Type(DisplayString):
    """Custom type storageLibrary_Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StorageLibrary_Name_Type.__name__ = "DisplayString"
_StorageLibrary_Name_Object = MibScalar
storageLibrary_Name = _StorageLibrary_Name_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 5, 1),
    _StorageLibrary_Name_Type()
)
storageLibrary_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_Name.setStatus("deprecated")


class _StorageLibrary_Description_Type(DisplayString):
    """Custom type storageLibrary_Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StorageLibrary_Description_Type.__name__ = "DisplayString"
_StorageLibrary_Description_Object = MibScalar
storageLibrary_Description = _StorageLibrary_Description_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 5, 2),
    _StorageLibrary_Description_Type()
)
storageLibrary_Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_Description.setStatus("deprecated")


class _StorageLibrary_Caption_Type(DisplayString):
    """Custom type storageLibrary_Caption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StorageLibrary_Caption_Type.__name__ = "DisplayString"
_StorageLibrary_Caption_Object = MibScalar
storageLibrary_Caption = _StorageLibrary_Caption_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 5, 3),
    _StorageLibrary_Caption_Type()
)
storageLibrary_Caption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_Caption.setStatus("deprecated")


class _StorageLibrary_Status_Type(DisplayString):
    """Custom type storageLibrary_Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_StorageLibrary_Status_Type.__name__ = "DisplayString"
_StorageLibrary_Status_Object = MibScalar
storageLibrary_Status = _StorageLibrary_Status_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 5, 4),
    _StorageLibrary_Status_Type()
)
storageLibrary_Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_Status.setStatus("deprecated")
_StorageLibrary_InstallDate_Type = CimDateTime
_StorageLibrary_InstallDate_Object = MibScalar
storageLibrary_InstallDate = _StorageLibrary_InstallDate_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 5, 5),
    _StorageLibrary_InstallDate_Type()
)
storageLibrary_InstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageLibrary_InstallDate.setStatus("deprecated")
_MediaAccessDeviceGroup_ObjectIdentity = ObjectIdentity
mediaAccessDeviceGroup = _MediaAccessDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6)
)
_NumberOfMediaAccessDevices_Type = Integer32
_NumberOfMediaAccessDevices_Object = MibScalar
numberOfMediaAccessDevices = _NumberOfMediaAccessDevices_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 1),
    _NumberOfMediaAccessDevices_Type()
)
numberOfMediaAccessDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfMediaAccessDevices.setStatus("mandatory")
_MediaAccessDeviceTable_Object = MibTable
mediaAccessDeviceTable = _MediaAccessDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    mediaAccessDeviceTable.setStatus("mandatory")
_MediaAccessDeviceEntry_Object = MibTableRow
mediaAccessDeviceEntry = _MediaAccessDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1)
)
mediaAccessDeviceEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "mediaAccessDeviceIndex"),
)
if mibBuilder.loadTexts:
    mediaAccessDeviceEntry.setStatus("mandatory")
_MediaAccessDeviceIndex_Type = UINT32
_MediaAccessDeviceIndex_Object = MibTableColumn
mediaAccessDeviceIndex = _MediaAccessDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 1),
    _MediaAccessDeviceIndex_Type()
)
mediaAccessDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDeviceIndex.setStatus("mandatory")


class _MediaAccessDeviceObjectType_Type(Integer32):
    """Custom type mediaAccessDeviceObjectType based on Integer32"""
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
        *(("cdromDrive", 5),
          ("dvdDrive", 4),
          ("magnetoOpticalDrive", 2),
          ("tapeDrive", 3),
          ("unknown", 0),
          ("wormDrive", 1))
    )


_MediaAccessDeviceObjectType_Type.__name__ = "Integer32"
_MediaAccessDeviceObjectType_Object = MibTableColumn
mediaAccessDeviceObjectType = _MediaAccessDeviceObjectType_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 2),
    _MediaAccessDeviceObjectType_Type()
)
mediaAccessDeviceObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDeviceObjectType.setStatus("mandatory")


class _MediaAccessDevice_Name_Type(DisplayString):
    """Custom type mediaAccessDevice_Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MediaAccessDevice_Name_Type.__name__ = "DisplayString"
_MediaAccessDevice_Name_Object = MibScalar
mediaAccessDevice_Name = _MediaAccessDevice_Name_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 3),
    _MediaAccessDevice_Name_Type()
)
mediaAccessDevice_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_Name.setStatus("deprecated")


class _MediaAccessDevice_Status_Type(DisplayString):
    """Custom type mediaAccessDevice_Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MediaAccessDevice_Status_Type.__name__ = "DisplayString"
_MediaAccessDevice_Status_Object = MibScalar
mediaAccessDevice_Status = _MediaAccessDevice_Status_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 4),
    _MediaAccessDevice_Status_Type()
)
mediaAccessDevice_Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_Status.setStatus("deprecated")


class _MediaAccessDevice_Availability_Type(Integer32):
    """Custom type mediaAccessDevice_Availability based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 10),
          ("inTest", 5),
          ("installError", 12),
          ("notApplicable", 6),
          ("notConfigured", 20),
          ("notInstalled", 11),
          ("notReady", 19),
          ("offDuty", 9),
          ("offLine", 8),
          ("other", 1),
          ("paused", 18),
          ("powerCycle", 16),
          ("powerOff", 7),
          ("powerSaveLowPowerMode", 14),
          ("powerSaveStandby", 15),
          ("powerSaveUnknown", 13),
          ("powerSaveWarning", 17),
          ("quiesced", 21),
          ("runningFullPower", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_MediaAccessDevice_Availability_Type.__name__ = "Integer32"
_MediaAccessDevice_Availability_Object = MibScalar
mediaAccessDevice_Availability = _MediaAccessDevice_Availability_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 5),
    _MediaAccessDevice_Availability_Type()
)
mediaAccessDevice_Availability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_Availability.setStatus("mandatory")


class _MediaAccessDevice_NeedsCleaning_Type(Integer32):
    """Custom type mediaAccessDevice_NeedsCleaning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_MediaAccessDevice_NeedsCleaning_Type.__name__ = "Integer32"
_MediaAccessDevice_NeedsCleaning_Object = MibScalar
mediaAccessDevice_NeedsCleaning = _MediaAccessDevice_NeedsCleaning_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 6),
    _MediaAccessDevice_NeedsCleaning_Type()
)
mediaAccessDevice_NeedsCleaning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_NeedsCleaning.setStatus("mandatory")
_MediaAccessDevice_MountCount_Type = UINT64
_MediaAccessDevice_MountCount_Object = MibScalar
mediaAccessDevice_MountCount = _MediaAccessDevice_MountCount_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 7),
    _MediaAccessDevice_MountCount_Type()
)
mediaAccessDevice_MountCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_MountCount.setStatus("mandatory")


class _MediaAccessDevice_DeviceID_Type(DisplayString):
    """Custom type mediaAccessDevice_DeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MediaAccessDevice_DeviceID_Type.__name__ = "DisplayString"
_MediaAccessDevice_DeviceID_Object = MibScalar
mediaAccessDevice_DeviceID = _MediaAccessDevice_DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 8),
    _MediaAccessDevice_DeviceID_Type()
)
mediaAccessDevice_DeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_DeviceID.setStatus("mandatory")
_MediaAccessDevice_PowerOnHours_Type = UINT64
_MediaAccessDevice_PowerOnHours_Object = MibScalar
mediaAccessDevice_PowerOnHours = _MediaAccessDevice_PowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 9),
    _MediaAccessDevice_PowerOnHours_Type()
)
mediaAccessDevice_PowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_PowerOnHours.setStatus("mandatory")
_MediaAccessDevice_TotalPowerOnHours_Type = UINT64
_MediaAccessDevice_TotalPowerOnHours_Object = MibScalar
mediaAccessDevice_TotalPowerOnHours = _MediaAccessDevice_TotalPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 10),
    _MediaAccessDevice_TotalPowerOnHours_Type()
)
mediaAccessDevice_TotalPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_TotalPowerOnHours.setStatus("mandatory")


class _MediaAccessDevice_OperationalStatus_Type(Integer32):
    """Custom type mediaAccessDevice_OperationalStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("completed", 17),
          ("dMTFReserved", 19),
          ("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("inService", 11),
          ("lostCommunication", 13),
          ("noContact", 12),
          ("non-RecoverableError", 7),
          ("ok", 2),
          ("other", 1),
          ("powerMode", 18),
          ("predictiveFailure", 5),
          ("starting", 8),
          ("stopped", 10),
          ("stopping", 9),
          ("stressed", 4),
          ("supportingEntityInError", 16),
          ("unknown", 0),
          ("vendorReserved", 32768))
    )


_MediaAccessDevice_OperationalStatus_Type.__name__ = "Integer32"
_MediaAccessDevice_OperationalStatus_Object = MibScalar
mediaAccessDevice_OperationalStatus = _MediaAccessDevice_OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 11),
    _MediaAccessDevice_OperationalStatus_Type()
)
mediaAccessDevice_OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_OperationalStatus.setStatus("mandatory")
_MediaAccessDevice_Realizes_StorageLocationIndex_Type = UINT32
_MediaAccessDevice_Realizes_StorageLocationIndex_Object = MibScalar
mediaAccessDevice_Realizes_StorageLocationIndex = _MediaAccessDevice_Realizes_StorageLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 12),
    _MediaAccessDevice_Realizes_StorageLocationIndex_Type()
)
mediaAccessDevice_Realizes_StorageLocationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_Realizes_StorageLocationIndex.setStatus("mandatory")
_MediaAccessDevice_Realizes_softwareElementIndex_Type = UINT32
_MediaAccessDevice_Realizes_softwareElementIndex_Object = MibScalar
mediaAccessDevice_Realizes_softwareElementIndex = _MediaAccessDevice_Realizes_softwareElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 6, 2, 1, 13),
    _MediaAccessDevice_Realizes_softwareElementIndex_Type()
)
mediaAccessDevice_Realizes_softwareElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaAccessDevice_Realizes_softwareElementIndex.setStatus("mandatory")
_PhysicalPackageGroup_ObjectIdentity = ObjectIdentity
physicalPackageGroup = _PhysicalPackageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8)
)
_NumberOfPhysicalPackages_Type = Integer32
_NumberOfPhysicalPackages_Object = MibScalar
numberOfPhysicalPackages = _NumberOfPhysicalPackages_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8, 1),
    _NumberOfPhysicalPackages_Type()
)
numberOfPhysicalPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPhysicalPackages.setStatus("mandatory")
_PhysicalPackageTable_Object = MibTable
physicalPackageTable = _PhysicalPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    physicalPackageTable.setStatus("mandatory")
_PhysicalPackageEntry_Object = MibTableRow
physicalPackageEntry = _PhysicalPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8, 2, 1)
)
physicalPackageEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "physicalPackageIndex"),
)
if mibBuilder.loadTexts:
    physicalPackageEntry.setStatus("mandatory")
_PhysicalPackageIndex_Type = UINT32
_PhysicalPackageIndex_Object = MibTableColumn
physicalPackageIndex = _PhysicalPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8, 2, 1, 1),
    _PhysicalPackageIndex_Type()
)
physicalPackageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackageIndex.setStatus("mandatory")


class _PhysicalPackage_Manufacturer_Type(DisplayString):
    """Custom type physicalPackage_Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PhysicalPackage_Manufacturer_Type.__name__ = "DisplayString"
_PhysicalPackage_Manufacturer_Object = MibScalar
physicalPackage_Manufacturer = _PhysicalPackage_Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8, 2, 1, 2),
    _PhysicalPackage_Manufacturer_Type()
)
physicalPackage_Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackage_Manufacturer.setStatus("mandatory")


class _PhysicalPackage_Model_Type(DisplayString):
    """Custom type physicalPackage_Model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PhysicalPackage_Model_Type.__name__ = "DisplayString"
_PhysicalPackage_Model_Object = MibScalar
physicalPackage_Model = _PhysicalPackage_Model_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8, 2, 1, 3),
    _PhysicalPackage_Model_Type()
)
physicalPackage_Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackage_Model.setStatus("mandatory")


class _PhysicalPackage_SerialNumber_Type(DisplayString):
    """Custom type physicalPackage_SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PhysicalPackage_SerialNumber_Type.__name__ = "DisplayString"
_PhysicalPackage_SerialNumber_Object = MibScalar
physicalPackage_SerialNumber = _PhysicalPackage_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8, 2, 1, 4),
    _PhysicalPackage_SerialNumber_Type()
)
physicalPackage_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackage_SerialNumber.setStatus("mandatory")
_PhysicalPackage_Realizes_MediaAccessDeviceIndex_Type = Integer32
_PhysicalPackage_Realizes_MediaAccessDeviceIndex_Object = MibScalar
physicalPackage_Realizes_MediaAccessDeviceIndex = _PhysicalPackage_Realizes_MediaAccessDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8, 2, 1, 5),
    _PhysicalPackage_Realizes_MediaAccessDeviceIndex_Type()
)
physicalPackage_Realizes_MediaAccessDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackage_Realizes_MediaAccessDeviceIndex.setStatus("mandatory")


class _PhysicalPackage_Tag_Type(DisplayString):
    """Custom type physicalPackage_Tag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PhysicalPackage_Tag_Type.__name__ = "DisplayString"
_PhysicalPackage_Tag_Object = MibScalar
physicalPackage_Tag = _PhysicalPackage_Tag_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 8, 2, 1, 6),
    _PhysicalPackage_Tag_Type()
)
physicalPackage_Tag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPackage_Tag.setStatus("mandatory")
_SoftwareElementGroup_ObjectIdentity = ObjectIdentity
softwareElementGroup = _SoftwareElementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9)
)
_NumberOfSoftwareElements_Type = Integer32
_NumberOfSoftwareElements_Object = MibScalar
numberOfSoftwareElements = _NumberOfSoftwareElements_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 1),
    _NumberOfSoftwareElements_Type()
)
numberOfSoftwareElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfSoftwareElements.setStatus("mandatory")
_SoftwareElementTable_Object = MibTable
softwareElementTable = _SoftwareElementTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2)
)
if mibBuilder.loadTexts:
    softwareElementTable.setStatus("mandatory")
_SoftwareElementEntry_Object = MibTableRow
softwareElementEntry = _SoftwareElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1)
)
softwareElementEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "softwareElementIndex"),
)
if mibBuilder.loadTexts:
    softwareElementEntry.setStatus("mandatory")
_SoftwareElementIndex_Type = UINT32
_SoftwareElementIndex_Object = MibTableColumn
softwareElementIndex = _SoftwareElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 1),
    _SoftwareElementIndex_Type()
)
softwareElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElementIndex.setStatus("mandatory")


class _SoftwareElement_Name_Type(DisplayString):
    """Custom type softwareElement_Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareElement_Name_Type.__name__ = "DisplayString"
_SoftwareElement_Name_Object = MibScalar
softwareElement_Name = _SoftwareElement_Name_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 2),
    _SoftwareElement_Name_Type()
)
softwareElement_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_Name.setStatus("deprecated")


class _SoftwareElement_Version_Type(DisplayString):
    """Custom type softwareElement_Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareElement_Version_Type.__name__ = "DisplayString"
_SoftwareElement_Version_Object = MibScalar
softwareElement_Version = _SoftwareElement_Version_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 3),
    _SoftwareElement_Version_Type()
)
softwareElement_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_Version.setStatus("mandatory")


class _SoftwareElement_SoftwareElementID_Type(DisplayString):
    """Custom type softwareElement_SoftwareElementID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareElement_SoftwareElementID_Type.__name__ = "DisplayString"
_SoftwareElement_SoftwareElementID_Object = MibScalar
softwareElement_SoftwareElementID = _SoftwareElement_SoftwareElementID_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 4),
    _SoftwareElement_SoftwareElementID_Type()
)
softwareElement_SoftwareElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_SoftwareElementID.setStatus("mandatory")


class _SoftwareElement_Manufacturer_Type(DisplayString):
    """Custom type softwareElement_Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_Manufacturer_Type.__name__ = "DisplayString"
_SoftwareElement_Manufacturer_Object = MibScalar
softwareElement_Manufacturer = _SoftwareElement_Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 5),
    _SoftwareElement_Manufacturer_Type()
)
softwareElement_Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_Manufacturer.setStatus("mandatory")


class _SoftwareElement_BuildNumber_Type(DisplayString):
    """Custom type softwareElement_BuildNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_BuildNumber_Type.__name__ = "DisplayString"
_SoftwareElement_BuildNumber_Object = MibScalar
softwareElement_BuildNumber = _SoftwareElement_BuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 6),
    _SoftwareElement_BuildNumber_Type()
)
softwareElement_BuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_BuildNumber.setStatus("mandatory")


class _SoftwareElement_SerialNumber_Type(DisplayString):
    """Custom type softwareElement_SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_SerialNumber_Type.__name__ = "DisplayString"
_SoftwareElement_SerialNumber_Object = MibScalar
softwareElement_SerialNumber = _SoftwareElement_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 7),
    _SoftwareElement_SerialNumber_Type()
)
softwareElement_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_SerialNumber.setStatus("mandatory")


class _SoftwareElement_CodeSet_Type(DisplayString):
    """Custom type softwareElement_CodeSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_CodeSet_Type.__name__ = "DisplayString"
_SoftwareElement_CodeSet_Object = MibScalar
softwareElement_CodeSet = _SoftwareElement_CodeSet_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 8),
    _SoftwareElement_CodeSet_Type()
)
softwareElement_CodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_CodeSet.setStatus("deprecated")


class _SoftwareElement_IdentificationCode_Type(DisplayString):
    """Custom type softwareElement_IdentificationCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareElement_IdentificationCode_Type.__name__ = "DisplayString"
_SoftwareElement_IdentificationCode_Object = MibScalar
softwareElement_IdentificationCode = _SoftwareElement_IdentificationCode_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 9),
    _SoftwareElement_IdentificationCode_Type()
)
softwareElement_IdentificationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_IdentificationCode.setStatus("deprecated")


class _SoftwareElement_LanguageEdition_Type(DisplayString):
    """Custom type softwareElement_LanguageEdition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SoftwareElement_LanguageEdition_Type.__name__ = "DisplayString"
_SoftwareElement_LanguageEdition_Object = MibScalar
softwareElement_LanguageEdition = _SoftwareElement_LanguageEdition_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 10),
    _SoftwareElement_LanguageEdition_Type()
)
softwareElement_LanguageEdition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_LanguageEdition.setStatus("deprecated")


class _SoftwareElement_InstanceID_Type(DisplayString):
    """Custom type softwareElement_InstanceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareElement_InstanceID_Type.__name__ = "DisplayString"
_SoftwareElement_InstanceID_Object = MibScalar
softwareElement_InstanceID = _SoftwareElement_InstanceID_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 9, 2, 1, 11),
    _SoftwareElement_InstanceID_Type()
)
softwareElement_InstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElement_InstanceID.setStatus("mandatory")
_ComputerSystemGroup_ObjectIdentity = ObjectIdentity
computerSystemGroup = _ComputerSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10)
)


class _ComputerSystem_ElementName_Type(DisplayString):
    """Custom type computerSystem_ElementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ComputerSystem_ElementName_Type.__name__ = "DisplayString"
_ComputerSystem_ElementName_Object = MibScalar
computerSystem_ElementName = _ComputerSystem_ElementName_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 1),
    _ComputerSystem_ElementName_Type()
)
computerSystem_ElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_ElementName.setStatus("mandatory")


class _ComputerSystem_OperationalStatus_Type(Integer32):
    """Custom type computerSystem_OperationalStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("completed", 17),
          ("dMTFReserved", 19),
          ("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("inService", 11),
          ("lostCommunication", 13),
          ("noContact", 12),
          ("non-RecoverableError", 7),
          ("ok", 2),
          ("other", 1),
          ("powerMode", 18),
          ("predictiveFailure", 5),
          ("starting", 8),
          ("stopped", 10),
          ("stopping", 9),
          ("stressed", 4),
          ("supportingEntityInError", 16),
          ("unknown", 0),
          ("vendorReserved", 32768))
    )


_ComputerSystem_OperationalStatus_Type.__name__ = "Integer32"
_ComputerSystem_OperationalStatus_Object = MibScalar
computerSystem_OperationalStatus = _ComputerSystem_OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 2),
    _ComputerSystem_OperationalStatus_Type()
)
computerSystem_OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_OperationalStatus.setStatus("mandatory")


class _ComputerSystem_Name_Type(DisplayString):
    """Custom type computerSystem_Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ComputerSystem_Name_Type.__name__ = "DisplayString"
_ComputerSystem_Name_Object = MibScalar
computerSystem_Name = _ComputerSystem_Name_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 3),
    _ComputerSystem_Name_Type()
)
computerSystem_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_Name.setStatus("mandatory")


class _ComputerSystem_NameFormat_Type(DisplayString):
    """Custom type computerSystem_NameFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ComputerSystem_NameFormat_Type.__name__ = "DisplayString"
_ComputerSystem_NameFormat_Object = MibScalar
computerSystem_NameFormat = _ComputerSystem_NameFormat_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 4),
    _ComputerSystem_NameFormat_Type()
)
computerSystem_NameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_NameFormat.setStatus("mandatory")


class _ComputerSystem_Dedicated_Type(Integer32):
    """Custom type computerSystem_Dedicated based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("accessServer", 9),
          ("blockServer", 15),
          ("bridgeExtender", 19),
          ("centralOfficeSwitch", 7),
          ("fileServer", 16),
          ("firewall", 10),
          ("gateway", 20),
          ("hub", 8),
          ("io", 12),
          ("layer3switch", 6),
          ("management", 14),
          ("mobileUserDevice", 17),
          ("notDedicated", 0),
          ("other", 2),
          ("print", 11),
          ("repeater", 18),
          ("router", 4),
          ("storage", 3),
          ("switch", 5),
          ("unknown", 1),
          ("webCaching", 13))
    )


_ComputerSystem_Dedicated_Type.__name__ = "Integer32"
_ComputerSystem_Dedicated_Object = MibScalar
computerSystem_Dedicated = _ComputerSystem_Dedicated_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 5),
    _ComputerSystem_Dedicated_Type()
)
computerSystem_Dedicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_Dedicated.setStatus("mandatory")


class _ComputerSystem_PrimaryOwnerContact_Type(DisplayString):
    """Custom type computerSystem_PrimaryOwnerContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ComputerSystem_PrimaryOwnerContact_Type.__name__ = "DisplayString"
_ComputerSystem_PrimaryOwnerContact_Object = MibScalar
computerSystem_PrimaryOwnerContact = _ComputerSystem_PrimaryOwnerContact_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 6),
    _ComputerSystem_PrimaryOwnerContact_Type()
)
computerSystem_PrimaryOwnerContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_PrimaryOwnerContact.setStatus("mandatory")


class _ComputerSystem_PrimaryOwnerName_Type(DisplayString):
    """Custom type computerSystem_PrimaryOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ComputerSystem_PrimaryOwnerName_Type.__name__ = "DisplayString"
_ComputerSystem_PrimaryOwnerName_Object = MibScalar
computerSystem_PrimaryOwnerName = _ComputerSystem_PrimaryOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 7),
    _ComputerSystem_PrimaryOwnerName_Type()
)
computerSystem_PrimaryOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_PrimaryOwnerName.setStatus("mandatory")


class _ComputerSystem_Description_Type(DisplayString):
    """Custom type computerSystem_Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ComputerSystem_Description_Type.__name__ = "DisplayString"
_ComputerSystem_Description_Object = MibScalar
computerSystem_Description = _ComputerSystem_Description_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 8),
    _ComputerSystem_Description_Type()
)
computerSystem_Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_Description.setStatus("mandatory")


class _ComputerSystem_Caption_Type(DisplayString):
    """Custom type computerSystem_Caption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ComputerSystem_Caption_Type.__name__ = "DisplayString"
_ComputerSystem_Caption_Object = MibScalar
computerSystem_Caption = _ComputerSystem_Caption_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 9),
    _ComputerSystem_Caption_Type()
)
computerSystem_Caption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_Caption.setStatus("mandatory")
_ComputerSystem_Realizes_softwareElementIndex_Type = UINT32
_ComputerSystem_Realizes_softwareElementIndex_Object = MibScalar
computerSystem_Realizes_softwareElementIndex = _ComputerSystem_Realizes_softwareElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 10, 10),
    _ComputerSystem_Realizes_softwareElementIndex_Type()
)
computerSystem_Realizes_softwareElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystem_Realizes_softwareElementIndex.setStatus("mandatory")
_ChangerDeviceGroup_ObjectIdentity = ObjectIdentity
changerDeviceGroup = _ChangerDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11)
)
_NumberOfChangerDevices_Type = Integer32
_NumberOfChangerDevices_Object = MibScalar
numberOfChangerDevices = _NumberOfChangerDevices_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 1),
    _NumberOfChangerDevices_Type()
)
numberOfChangerDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfChangerDevices.setStatus("mandatory")
_ChangerDeviceTable_Object = MibTable
changerDeviceTable = _ChangerDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2)
)
if mibBuilder.loadTexts:
    changerDeviceTable.setStatus("mandatory")
_ChangerDeviceEntry_Object = MibTableRow
changerDeviceEntry = _ChangerDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1)
)
changerDeviceEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "changerDeviceIndex"),
)
if mibBuilder.loadTexts:
    changerDeviceEntry.setStatus("mandatory")
_ChangerDeviceIndex_Type = UINT32
_ChangerDeviceIndex_Object = MibTableColumn
changerDeviceIndex = _ChangerDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1, 1),
    _ChangerDeviceIndex_Type()
)
changerDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changerDeviceIndex.setStatus("mandatory")


class _ChangerDevice_DeviceID_Type(DisplayString):
    """Custom type changerDevice_DeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ChangerDevice_DeviceID_Type.__name__ = "DisplayString"
_ChangerDevice_DeviceID_Object = MibScalar
changerDevice_DeviceID = _ChangerDevice_DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1, 2),
    _ChangerDevice_DeviceID_Type()
)
changerDevice_DeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changerDevice_DeviceID.setStatus("mandatory")


class _ChangerDevice_MediaFlipSupported_Type(Integer32):
    """Custom type changerDevice_MediaFlipSupported based on Integer32"""
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


_ChangerDevice_MediaFlipSupported_Type.__name__ = "Integer32"
_ChangerDevice_MediaFlipSupported_Object = MibScalar
changerDevice_MediaFlipSupported = _ChangerDevice_MediaFlipSupported_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1, 3),
    _ChangerDevice_MediaFlipSupported_Type()
)
changerDevice_MediaFlipSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changerDevice_MediaFlipSupported.setStatus("mandatory")


class _ChangerDevice_ElementName_Type(DisplayString):
    """Custom type changerDevice_ElementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChangerDevice_ElementName_Type.__name__ = "DisplayString"
_ChangerDevice_ElementName_Object = MibScalar
changerDevice_ElementName = _ChangerDevice_ElementName_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1, 4),
    _ChangerDevice_ElementName_Type()
)
changerDevice_ElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changerDevice_ElementName.setStatus("mandatory")


class _ChangerDevice_Caption_Type(DisplayString):
    """Custom type changerDevice_Caption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ChangerDevice_Caption_Type.__name__ = "DisplayString"
_ChangerDevice_Caption_Object = MibScalar
changerDevice_Caption = _ChangerDevice_Caption_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1, 5),
    _ChangerDevice_Caption_Type()
)
changerDevice_Caption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changerDevice_Caption.setStatus("mandatory")


class _ChangerDevice_Description_Type(DisplayString):
    """Custom type changerDevice_Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChangerDevice_Description_Type.__name__ = "DisplayString"
_ChangerDevice_Description_Object = MibScalar
changerDevice_Description = _ChangerDevice_Description_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1, 6),
    _ChangerDevice_Description_Type()
)
changerDevice_Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changerDevice_Description.setStatus("mandatory")


class _ChangerDevice_Availability_Type(Integer32):
    """Custom type changerDevice_Availability based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 10),
          ("inTest", 5),
          ("installError", 12),
          ("notApplicable", 6),
          ("notConfigured", 20),
          ("notInstalled", 11),
          ("notReady", 19),
          ("offDuty", 9),
          ("offLine", 8),
          ("other", 1),
          ("paused", 18),
          ("powerCycle", 16),
          ("powerOff", 7),
          ("powerSaveLowPowerMode", 14),
          ("powerSaveStandby", 15),
          ("powerSaveUnknown", 13),
          ("powerSaveWarning", 17),
          ("quiesced", 21),
          ("runningFullPower", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_ChangerDevice_Availability_Type.__name__ = "Integer32"
_ChangerDevice_Availability_Object = MibScalar
changerDevice_Availability = _ChangerDevice_Availability_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1, 8),
    _ChangerDevice_Availability_Type()
)
changerDevice_Availability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changerDevice_Availability.setStatus("mandatory")


class _ChangerDevice_OperationalStatus_Type(Integer32):
    """Custom type changerDevice_OperationalStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("completed", 17),
          ("dMTFReserved", 19),
          ("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("inService", 11),
          ("lostCommunication", 13),
          ("noContact", 12),
          ("non-RecoverableError", 7),
          ("ok", 2),
          ("other", 1),
          ("powerMode", 18),
          ("predictiveFailure", 5),
          ("starting", 8),
          ("stopped", 10),
          ("stopping", 9),
          ("stressed", 4),
          ("supportingEntityInError", 16),
          ("unknown", 0),
          ("vendorReserved", 32768))
    )


_ChangerDevice_OperationalStatus_Type.__name__ = "Integer32"
_ChangerDevice_OperationalStatus_Object = MibScalar
changerDevice_OperationalStatus = _ChangerDevice_OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1, 9),
    _ChangerDevice_OperationalStatus_Type()
)
changerDevice_OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changerDevice_OperationalStatus.setStatus("mandatory")
_ChangerDevice_Realizes_StorageLocationIndex_Type = UINT32
_ChangerDevice_Realizes_StorageLocationIndex_Object = MibScalar
changerDevice_Realizes_StorageLocationIndex = _ChangerDevice_Realizes_StorageLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 11, 2, 1, 10),
    _ChangerDevice_Realizes_StorageLocationIndex_Type()
)
changerDevice_Realizes_StorageLocationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changerDevice_Realizes_StorageLocationIndex.setStatus("mandatory")
_ScsiProtocolControllerGroup_ObjectIdentity = ObjectIdentity
scsiProtocolControllerGroup = _ScsiProtocolControllerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12)
)
_NumberOfSCSIProtocolControllers_Type = Integer32
_NumberOfSCSIProtocolControllers_Object = MibScalar
numberOfSCSIProtocolControllers = _NumberOfSCSIProtocolControllers_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 1),
    _NumberOfSCSIProtocolControllers_Type()
)
numberOfSCSIProtocolControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfSCSIProtocolControllers.setStatus("mandatory")
_ScsiProtocolControllerTable_Object = MibTable
scsiProtocolControllerTable = _ScsiProtocolControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2)
)
if mibBuilder.loadTexts:
    scsiProtocolControllerTable.setStatus("mandatory")
_ScsiProtocolControllerEntry_Object = MibTableRow
scsiProtocolControllerEntry = _ScsiProtocolControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2, 1)
)
scsiProtocolControllerEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "scsiProtocolControllerIndex"),
)
if mibBuilder.loadTexts:
    scsiProtocolControllerEntry.setStatus("mandatory")
_ScsiProtocolControllerIndex_Type = UINT32
_ScsiProtocolControllerIndex_Object = MibTableColumn
scsiProtocolControllerIndex = _ScsiProtocolControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2, 1, 1),
    _ScsiProtocolControllerIndex_Type()
)
scsiProtocolControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiProtocolControllerIndex.setStatus("mandatory")


class _ScsiProtocolController_DeviceID_Type(DisplayString):
    """Custom type scsiProtocolController_DeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ScsiProtocolController_DeviceID_Type.__name__ = "DisplayString"
_ScsiProtocolController_DeviceID_Object = MibScalar
scsiProtocolController_DeviceID = _ScsiProtocolController_DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2, 1, 2),
    _ScsiProtocolController_DeviceID_Type()
)
scsiProtocolController_DeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiProtocolController_DeviceID.setStatus("mandatory")


class _ScsiProtocolController_ElementName_Type(DisplayString):
    """Custom type scsiProtocolController_ElementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ScsiProtocolController_ElementName_Type.__name__ = "DisplayString"
_ScsiProtocolController_ElementName_Object = MibScalar
scsiProtocolController_ElementName = _ScsiProtocolController_ElementName_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2, 1, 3),
    _ScsiProtocolController_ElementName_Type()
)
scsiProtocolController_ElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiProtocolController_ElementName.setStatus("mandatory")


class _ScsiProtocolController_OperationalStatus_Type(Integer32):
    """Custom type scsiProtocolController_OperationalStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("completed", 17),
          ("dMTFReserved", 19),
          ("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("inService", 11),
          ("lostCommunication", 13),
          ("noContact", 12),
          ("non-RecoverableError", 7),
          ("ok", 2),
          ("other", 1),
          ("powerMode", 18),
          ("predictiveFailure", 5),
          ("starting", 8),
          ("stopped", 10),
          ("stopping", 9),
          ("stressed", 4),
          ("supportingEntityInError", 16),
          ("unknown", 0),
          ("vendorReserved", 32768))
    )


_ScsiProtocolController_OperationalStatus_Type.__name__ = "Integer32"
_ScsiProtocolController_OperationalStatus_Object = MibScalar
scsiProtocolController_OperationalStatus = _ScsiProtocolController_OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2, 1, 4),
    _ScsiProtocolController_OperationalStatus_Type()
)
scsiProtocolController_OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiProtocolController_OperationalStatus.setStatus("mandatory")


class _ScsiProtocolController_Description_Type(DisplayString):
    """Custom type scsiProtocolController_Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ScsiProtocolController_Description_Type.__name__ = "DisplayString"
_ScsiProtocolController_Description_Object = MibScalar
scsiProtocolController_Description = _ScsiProtocolController_Description_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2, 1, 5),
    _ScsiProtocolController_Description_Type()
)
scsiProtocolController_Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiProtocolController_Description.setStatus("mandatory")


class _ScsiProtocolController_Availability_Type(Integer32):
    """Custom type scsiProtocolController_Availability based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 10),
          ("inTest", 5),
          ("installError", 12),
          ("notApplicable", 6),
          ("notConfigured", 20),
          ("notInstalled", 11),
          ("notReady", 19),
          ("offDuty", 9),
          ("offLine", 8),
          ("other", 1),
          ("paused", 18),
          ("powerCycle", 16),
          ("powerOff", 7),
          ("powerSaveLowPowerMode", 14),
          ("powerSaveStandby", 15),
          ("powerSaveUnknown", 13),
          ("powerSaveWarning", 17),
          ("quiesced", 21),
          ("runningFullPower", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_ScsiProtocolController_Availability_Type.__name__ = "Integer32"
_ScsiProtocolController_Availability_Object = MibScalar
scsiProtocolController_Availability = _ScsiProtocolController_Availability_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2, 1, 6),
    _ScsiProtocolController_Availability_Type()
)
scsiProtocolController_Availability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiProtocolController_Availability.setStatus("mandatory")
_ScsiProtocolController_Realizes_ChangerDeviceIndex_Type = UINT32
_ScsiProtocolController_Realizes_ChangerDeviceIndex_Object = MibScalar
scsiProtocolController_Realizes_ChangerDeviceIndex = _ScsiProtocolController_Realizes_ChangerDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2, 1, 7),
    _ScsiProtocolController_Realizes_ChangerDeviceIndex_Type()
)
scsiProtocolController_Realizes_ChangerDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiProtocolController_Realizes_ChangerDeviceIndex.setStatus("mandatory")
_ScsiProtocolController_Realizes_MediaAccessDeviceIndex_Type = UINT32
_ScsiProtocolController_Realizes_MediaAccessDeviceIndex_Object = MibScalar
scsiProtocolController_Realizes_MediaAccessDeviceIndex = _ScsiProtocolController_Realizes_MediaAccessDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 12, 2, 1, 8),
    _ScsiProtocolController_Realizes_MediaAccessDeviceIndex_Type()
)
scsiProtocolController_Realizes_MediaAccessDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiProtocolController_Realizes_MediaAccessDeviceIndex.setStatus("mandatory")
_StorageMediaLocationGroup_ObjectIdentity = ObjectIdentity
storageMediaLocationGroup = _StorageMediaLocationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13)
)
_NumberOfStorageMediaLocations_Type = Integer32
_NumberOfStorageMediaLocations_Object = MibScalar
numberOfStorageMediaLocations = _NumberOfStorageMediaLocations_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 1),
    _NumberOfStorageMediaLocations_Type()
)
numberOfStorageMediaLocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfStorageMediaLocations.setStatus("mandatory")
_NumberOfPhysicalMedias_Type = Integer32
_NumberOfPhysicalMedias_Object = MibScalar
numberOfPhysicalMedias = _NumberOfPhysicalMedias_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 2),
    _NumberOfPhysicalMedias_Type()
)
numberOfPhysicalMedias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPhysicalMedias.setStatus("mandatory")
_StorageMediaLocationTable_Object = MibTable
storageMediaLocationTable = _StorageMediaLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3)
)
if mibBuilder.loadTexts:
    storageMediaLocationTable.setStatus("mandatory")
_StorageMediaLocationEntry_Object = MibTableRow
storageMediaLocationEntry = _StorageMediaLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1)
)
storageMediaLocationEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "storageMediaLocationIndex"),
)
if mibBuilder.loadTexts:
    storageMediaLocationEntry.setStatus("mandatory")
_StorageMediaLocationIndex_Type = UINT32
_StorageMediaLocationIndex_Object = MibTableColumn
storageMediaLocationIndex = _StorageMediaLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 1),
    _StorageMediaLocationIndex_Type()
)
storageMediaLocationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocationIndex.setStatus("mandatory")


class _StorageMediaLocation_Tag_Type(DisplayString):
    """Custom type storageMediaLocation_Tag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StorageMediaLocation_Tag_Type.__name__ = "DisplayString"
_StorageMediaLocation_Tag_Object = MibScalar
storageMediaLocation_Tag = _StorageMediaLocation_Tag_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 2),
    _StorageMediaLocation_Tag_Type()
)
storageMediaLocation_Tag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_Tag.setStatus("mandatory")


class _StorageMediaLocation_LocationType_Type(Integer32):
    """Custom type storageMediaLocation_LocationType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("door", 7),
          ("interLibraryPort", 5),
          ("limitedAccessPort", 6),
          ("magazine", 3),
          ("mediaAccessDevice", 4),
          ("other", 1),
          ("shelf", 8),
          ("slot", 2),
          ("unknown", 0),
          ("vault", 9))
    )


_StorageMediaLocation_LocationType_Type.__name__ = "Integer32"
_StorageMediaLocation_LocationType_Object = MibScalar
storageMediaLocation_LocationType = _StorageMediaLocation_LocationType_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 3),
    _StorageMediaLocation_LocationType_Type()
)
storageMediaLocation_LocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_LocationType.setStatus("mandatory")


class _StorageMediaLocation_LocationCoordinates_Type(DisplayString):
    """Custom type storageMediaLocation_LocationCoordinates based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StorageMediaLocation_LocationCoordinates_Type.__name__ = "DisplayString"
_StorageMediaLocation_LocationCoordinates_Object = MibScalar
storageMediaLocation_LocationCoordinates = _StorageMediaLocation_LocationCoordinates_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 4),
    _StorageMediaLocation_LocationCoordinates_Type()
)
storageMediaLocation_LocationCoordinates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_LocationCoordinates.setStatus("mandatory")


class _StorageMediaLocation_MediaTypesSupported_Type(Integer32):
    """Custom type storageMediaLocation_MediaTypesSupported based on Integer32"""
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
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66)
        )
    )
    namedValues = NamedValues(
        *(("ablativeWriteOnce", 49),
          ("ait", 4),
          ("catridgeDisk", 11),
          ("cdDA", 34),
          ("cdI", 18),
          ("cdPlus", 35),
          ("cdRW", 33),
          ("cdRecordable", 19),
          ("cdRom", 16),
          ("cdRomXA", 17),
          ("clikDisk", 32),
          ("d2Tape", 63),
          ("dat", 6),
          ("divx", 27),
          ("dlt", 9),
          ("dstLarge", 66),
          ("dstMedium", 65),
          ("dstSmall", 64),
          ("dtf", 5),
          ("dvd", 22),
          ("dvd10", 41),
          ("dvd18", 42),
          ("dvd5", 39),
          ("dvd9", 40),
          ("dvdAudio", 38),
          ("dvdRAM", 24),
          ("dvdROM", 25),
          ("dvdRW", 37),
          ("dvdRWPlus", 23),
          ("dvdRecordable", 36),
          ("dvdVideo", 26),
          ("eightmmAdvanced", 54),
          ("eightmmMetal", 53),
          ("eightmmTape", 7),
          ("floppyDiskette", 28),
          ("halfInchMO", 10),
          ("hardCopy", 31),
          ("hardDisk", 29),
          ("jazDisk", 12),
          ("ltoAccelis", 57),
          ("ltoUltrium", 56),
          ("magneto-Optical", 21),
          ("magstar3590", 61),
          ("magstarMP", 62),
          ("memoryCard", 30),
          ("miniQic", 51),
          ("moLIMDOW", 45),
          ("moRewriteable", 43),
          ("moWriteOnce", 44),
          ("nctp", 55),
          ("nearField", 50),
          ("nineteenmmTape", 8),
          ("other", 1),
          ("phaseChangeDualRewriteable", 48),
          ("phaseChangeRewriteable", 47),
          ("phaseChangeWO", 46),
          ("qic", 3),
          ("syQuestDisk", 14),
          ("tape", 2),
          ("tape18Track", 59),
          ("tape36Track", 60),
          ("tape9Track", 58),
          ("travan", 52),
          ("unknown", 0),
          ("wORM", 20),
          ("winchesterDisk", 15),
          ("zipDisk", 13))
    )


_StorageMediaLocation_MediaTypesSupported_Type.__name__ = "Integer32"
_StorageMediaLocation_MediaTypesSupported_Object = MibScalar
storageMediaLocation_MediaTypesSupported = _StorageMediaLocation_MediaTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 5),
    _StorageMediaLocation_MediaTypesSupported_Type()
)
storageMediaLocation_MediaTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_MediaTypesSupported.setStatus("mandatory")
_StorageMediaLocation_MediaCapacity_Type = UINT32
_StorageMediaLocation_MediaCapacity_Object = MibScalar
storageMediaLocation_MediaCapacity = _StorageMediaLocation_MediaCapacity_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 6),
    _StorageMediaLocation_MediaCapacity_Type()
)
storageMediaLocation_MediaCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_MediaCapacity.setStatus("mandatory")
_StorageMediaLocation_Association_ChangerDeviceIndex_Type = UINT32
_StorageMediaLocation_Association_ChangerDeviceIndex_Object = MibScalar
storageMediaLocation_Association_ChangerDeviceIndex = _StorageMediaLocation_Association_ChangerDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 7),
    _StorageMediaLocation_Association_ChangerDeviceIndex_Type()
)
storageMediaLocation_Association_ChangerDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_Association_ChangerDeviceIndex.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMediaPresent_Type(Integer32):
    """Custom type storageMediaLocation_PhysicalMediaPresent based on Integer32"""
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


_StorageMediaLocation_PhysicalMediaPresent_Type.__name__ = "Integer32"
_StorageMediaLocation_PhysicalMediaPresent_Object = MibScalar
storageMediaLocation_PhysicalMediaPresent = _StorageMediaLocation_PhysicalMediaPresent_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 10),
    _StorageMediaLocation_PhysicalMediaPresent_Type()
)
storageMediaLocation_PhysicalMediaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMediaPresent.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMedia_Removable_Type(Integer32):
    """Custom type storageMediaLocation_PhysicalMedia_Removable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_StorageMediaLocation_PhysicalMedia_Removable_Type.__name__ = "Integer32"
_StorageMediaLocation_PhysicalMedia_Removable_Object = MibScalar
storageMediaLocation_PhysicalMedia_Removable = _StorageMediaLocation_PhysicalMedia_Removable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 11),
    _StorageMediaLocation_PhysicalMedia_Removable_Type()
)
storageMediaLocation_PhysicalMedia_Removable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_Removable.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMedia_Replaceable_Type(Integer32):
    """Custom type storageMediaLocation_PhysicalMedia_Replaceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_StorageMediaLocation_PhysicalMedia_Replaceable_Type.__name__ = "Integer32"
_StorageMediaLocation_PhysicalMedia_Replaceable_Object = MibScalar
storageMediaLocation_PhysicalMedia_Replaceable = _StorageMediaLocation_PhysicalMedia_Replaceable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 12),
    _StorageMediaLocation_PhysicalMedia_Replaceable_Type()
)
storageMediaLocation_PhysicalMedia_Replaceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_Replaceable.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMedia_HotSwappable_Type(Integer32):
    """Custom type storageMediaLocation_PhysicalMedia_HotSwappable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_StorageMediaLocation_PhysicalMedia_HotSwappable_Type.__name__ = "Integer32"
_StorageMediaLocation_PhysicalMedia_HotSwappable_Object = MibScalar
storageMediaLocation_PhysicalMedia_HotSwappable = _StorageMediaLocation_PhysicalMedia_HotSwappable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 13),
    _StorageMediaLocation_PhysicalMedia_HotSwappable_Type()
)
storageMediaLocation_PhysicalMedia_HotSwappable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_HotSwappable.setStatus("mandatory")
_StorageMediaLocation_PhysicalMedia_Capacity_Type = UINT64
_StorageMediaLocation_PhysicalMedia_Capacity_Object = MibScalar
storageMediaLocation_PhysicalMedia_Capacity = _StorageMediaLocation_PhysicalMedia_Capacity_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 14),
    _StorageMediaLocation_PhysicalMedia_Capacity_Type()
)
storageMediaLocation_PhysicalMedia_Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_Capacity.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMedia_MediaType_Type(Integer32):
    """Custom type storageMediaLocation_PhysicalMedia_MediaType based on Integer32"""
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
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66)
        )
    )
    namedValues = NamedValues(
        *(("ablativeWriteOnce", 49),
          ("ait", 4),
          ("catridgeDisk", 11),
          ("cdDA", 34),
          ("cdI", 18),
          ("cdPlus", 35),
          ("cdRW", 33),
          ("cdRecordable", 19),
          ("cdRom", 16),
          ("cdRomXA", 17),
          ("clikDisk", 32),
          ("d2Tape", 63),
          ("dat", 6),
          ("divx", 27),
          ("dlt", 9),
          ("dstLarge", 66),
          ("dstMedium", 65),
          ("dstSmall", 64),
          ("dtf", 5),
          ("dvd", 22),
          ("dvd10", 41),
          ("dvd18", 42),
          ("dvd5", 39),
          ("dvd9", 40),
          ("dvdAudio", 38),
          ("dvdRAM", 24),
          ("dvdROM", 25),
          ("dvdRW", 37),
          ("dvdRWPlus", 23),
          ("dvdRecordable", 36),
          ("dvdVideo", 26),
          ("eightmmAdvanced", 54),
          ("eightmmMetal", 53),
          ("eightmmTape", 7),
          ("floppyDiskette", 28),
          ("halfInchMO", 10),
          ("hardCopy", 31),
          ("hardDisk", 29),
          ("jazDisk", 12),
          ("ltoAccelis", 57),
          ("ltoUltrium", 56),
          ("magneto-Optical", 21),
          ("magstar3590", 61),
          ("magstarMP", 62),
          ("memoryCard", 30),
          ("miniQic", 51),
          ("moLIMDOW", 45),
          ("moRewriteable", 43),
          ("moWriteOnce", 44),
          ("nctp", 55),
          ("nearField", 50),
          ("nineteenmmTape", 8),
          ("other", 1),
          ("phaseChangeDualRewriteable", 48),
          ("phaseChangeRewriteable", 47),
          ("phaseChangeWO", 46),
          ("qic", 3),
          ("syQuestDisk", 14),
          ("tape", 2),
          ("tape18Track", 59),
          ("tape36Track", 60),
          ("tape9Track", 58),
          ("travan", 52),
          ("unknown", 0),
          ("wORM", 20),
          ("winchesterDisk", 15),
          ("zipDisk", 13))
    )


_StorageMediaLocation_PhysicalMedia_MediaType_Type.__name__ = "Integer32"
_StorageMediaLocation_PhysicalMedia_MediaType_Object = MibScalar
storageMediaLocation_PhysicalMedia_MediaType = _StorageMediaLocation_PhysicalMedia_MediaType_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 15),
    _StorageMediaLocation_PhysicalMedia_MediaType_Type()
)
storageMediaLocation_PhysicalMedia_MediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_MediaType.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMedia_MediaDescription_Type(DisplayString):
    """Custom type storageMediaLocation_PhysicalMedia_MediaDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StorageMediaLocation_PhysicalMedia_MediaDescription_Type.__name__ = "DisplayString"
_StorageMediaLocation_PhysicalMedia_MediaDescription_Object = MibScalar
storageMediaLocation_PhysicalMedia_MediaDescription = _StorageMediaLocation_PhysicalMedia_MediaDescription_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 16),
    _StorageMediaLocation_PhysicalMedia_MediaDescription_Type()
)
storageMediaLocation_PhysicalMedia_MediaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_MediaDescription.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMedia_CleanerMedia_Type(Integer32):
    """Custom type storageMediaLocation_PhysicalMedia_CleanerMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_StorageMediaLocation_PhysicalMedia_CleanerMedia_Type.__name__ = "Integer32"
_StorageMediaLocation_PhysicalMedia_CleanerMedia_Object = MibScalar
storageMediaLocation_PhysicalMedia_CleanerMedia = _StorageMediaLocation_PhysicalMedia_CleanerMedia_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 17),
    _StorageMediaLocation_PhysicalMedia_CleanerMedia_Type()
)
storageMediaLocation_PhysicalMedia_CleanerMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_CleanerMedia.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMedia_DualSided_Type(Integer32):
    """Custom type storageMediaLocation_PhysicalMedia_DualSided based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )


_StorageMediaLocation_PhysicalMedia_DualSided_Type.__name__ = "Integer32"
_StorageMediaLocation_PhysicalMedia_DualSided_Object = MibScalar
storageMediaLocation_PhysicalMedia_DualSided = _StorageMediaLocation_PhysicalMedia_DualSided_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 18),
    _StorageMediaLocation_PhysicalMedia_DualSided_Type()
)
storageMediaLocation_PhysicalMedia_DualSided.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_DualSided.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMedia_PhysicalLabel_Type(DisplayString):
    """Custom type storageMediaLocation_PhysicalMedia_PhysicalLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StorageMediaLocation_PhysicalMedia_PhysicalLabel_Type.__name__ = "DisplayString"
_StorageMediaLocation_PhysicalMedia_PhysicalLabel_Object = MibScalar
storageMediaLocation_PhysicalMedia_PhysicalLabel = _StorageMediaLocation_PhysicalMedia_PhysicalLabel_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 19),
    _StorageMediaLocation_PhysicalMedia_PhysicalLabel_Type()
)
storageMediaLocation_PhysicalMedia_PhysicalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_PhysicalLabel.setStatus("mandatory")


class _StorageMediaLocation_PhysicalMedia_Tag_Type(DisplayString):
    """Custom type storageMediaLocation_PhysicalMedia_Tag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StorageMediaLocation_PhysicalMedia_Tag_Type.__name__ = "DisplayString"
_StorageMediaLocation_PhysicalMedia_Tag_Object = MibScalar
storageMediaLocation_PhysicalMedia_Tag = _StorageMediaLocation_PhysicalMedia_Tag_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 13, 3, 1, 20),
    _StorageMediaLocation_PhysicalMedia_Tag_Type()
)
storageMediaLocation_PhysicalMedia_Tag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageMediaLocation_PhysicalMedia_Tag.setStatus("mandatory")
_LimitedAccessPortGroup_ObjectIdentity = ObjectIdentity
limitedAccessPortGroup = _LimitedAccessPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14)
)
_NumberOflimitedAccessPorts_Type = Integer32
_NumberOflimitedAccessPorts_Object = MibScalar
numberOflimitedAccessPorts = _NumberOflimitedAccessPorts_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 1),
    _NumberOflimitedAccessPorts_Type()
)
numberOflimitedAccessPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOflimitedAccessPorts.setStatus("mandatory")
_LimitedAccessPortTable_Object = MibTable
limitedAccessPortTable = _LimitedAccessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 2)
)
if mibBuilder.loadTexts:
    limitedAccessPortTable.setStatus("mandatory")
_LimitedAccessPortEntry_Object = MibTableRow
limitedAccessPortEntry = _LimitedAccessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 2, 1)
)
limitedAccessPortEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "limitedAccessPortIndex"),
)
if mibBuilder.loadTexts:
    limitedAccessPortEntry.setStatus("mandatory")
_LimitedAccessPortIndex_Type = UINT32
_LimitedAccessPortIndex_Object = MibTableColumn
limitedAccessPortIndex = _LimitedAccessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 2, 1, 1),
    _LimitedAccessPortIndex_Type()
)
limitedAccessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitedAccessPortIndex.setStatus("mandatory")


class _LimitedAccessPort_DeviceID_Type(DisplayString):
    """Custom type limitedAccessPort_DeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LimitedAccessPort_DeviceID_Type.__name__ = "DisplayString"
_LimitedAccessPort_DeviceID_Object = MibScalar
limitedAccessPort_DeviceID = _LimitedAccessPort_DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 2, 1, 2),
    _LimitedAccessPort_DeviceID_Type()
)
limitedAccessPort_DeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitedAccessPort_DeviceID.setStatus("mandatory")


class _LimitedAccessPort_Extended_Type(Integer32):
    """Custom type limitedAccessPort_Extended based on Integer32"""
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


_LimitedAccessPort_Extended_Type.__name__ = "Integer32"
_LimitedAccessPort_Extended_Object = MibScalar
limitedAccessPort_Extended = _LimitedAccessPort_Extended_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 2, 1, 3),
    _LimitedAccessPort_Extended_Type()
)
limitedAccessPort_Extended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitedAccessPort_Extended.setStatus("mandatory")


class _LimitedAccessPort_ElementName_Type(DisplayString):
    """Custom type limitedAccessPort_ElementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LimitedAccessPort_ElementName_Type.__name__ = "DisplayString"
_LimitedAccessPort_ElementName_Object = MibScalar
limitedAccessPort_ElementName = _LimitedAccessPort_ElementName_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 2, 1, 4),
    _LimitedAccessPort_ElementName_Type()
)
limitedAccessPort_ElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitedAccessPort_ElementName.setStatus("mandatory")


class _LimitedAccessPort_Caption_Type(DisplayString):
    """Custom type limitedAccessPort_Caption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LimitedAccessPort_Caption_Type.__name__ = "DisplayString"
_LimitedAccessPort_Caption_Object = MibScalar
limitedAccessPort_Caption = _LimitedAccessPort_Caption_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 2, 1, 5),
    _LimitedAccessPort_Caption_Type()
)
limitedAccessPort_Caption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitedAccessPort_Caption.setStatus("mandatory")


class _LimitedAccessPort_Description_Type(DisplayString):
    """Custom type limitedAccessPort_Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LimitedAccessPort_Description_Type.__name__ = "DisplayString"
_LimitedAccessPort_Description_Object = MibScalar
limitedAccessPort_Description = _LimitedAccessPort_Description_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 2, 1, 6),
    _LimitedAccessPort_Description_Type()
)
limitedAccessPort_Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitedAccessPort_Description.setStatus("mandatory")
_LimitedAccessPort_Realizes_StorageLocationIndex_Type = UINT32
_LimitedAccessPort_Realizes_StorageLocationIndex_Object = MibScalar
limitedAccessPort_Realizes_StorageLocationIndex = _LimitedAccessPort_Realizes_StorageLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 14, 2, 1, 7),
    _LimitedAccessPort_Realizes_StorageLocationIndex_Type()
)
limitedAccessPort_Realizes_StorageLocationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitedAccessPort_Realizes_StorageLocationIndex.setStatus("mandatory")
_FCPortGroup_ObjectIdentity = ObjectIdentity
fCPortGroup = _FCPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15)
)
_NumberOffCPorts_Type = Integer32
_NumberOffCPorts_Object = MibScalar
numberOffCPorts = _NumberOffCPorts_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 1),
    _NumberOffCPorts_Type()
)
numberOffCPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOffCPorts.setStatus("mandatory")
_FCPortTable_Object = MibTable
fCPortTable = _FCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2)
)
if mibBuilder.loadTexts:
    fCPortTable.setStatus("mandatory")
_FCPortEntry_Object = MibTableRow
fCPortEntry = _FCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2, 1)
)
fCPortEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "fCPortIndex"),
)
if mibBuilder.loadTexts:
    fCPortEntry.setStatus("mandatory")
_FCPortIndex_Type = UINT32
_FCPortIndex_Object = MibTableColumn
fCPortIndex = _FCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2, 1, 1),
    _FCPortIndex_Type()
)
fCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCPortIndex.setStatus("mandatory")


class _FCPort_DeviceID_Type(DisplayString):
    """Custom type fCPort_DeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FCPort_DeviceID_Type.__name__ = "DisplayString"
_FCPort_DeviceID_Object = MibScalar
fCPort_DeviceID = _FCPort_DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2, 1, 2),
    _FCPort_DeviceID_Type()
)
fCPort_DeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCPort_DeviceID.setStatus("mandatory")


class _FCPort_ElementName_Type(DisplayString):
    """Custom type fCPort_ElementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FCPort_ElementName_Type.__name__ = "DisplayString"
_FCPort_ElementName_Object = MibScalar
fCPort_ElementName = _FCPort_ElementName_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2, 1, 3),
    _FCPort_ElementName_Type()
)
fCPort_ElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCPort_ElementName.setStatus("mandatory")


class _FCPort_Caption_Type(DisplayString):
    """Custom type fCPort_Caption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FCPort_Caption_Type.__name__ = "DisplayString"
_FCPort_Caption_Object = MibScalar
fCPort_Caption = _FCPort_Caption_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2, 1, 4),
    _FCPort_Caption_Type()
)
fCPort_Caption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCPort_Caption.setStatus("mandatory")


class _FCPort_Description_Type(DisplayString):
    """Custom type fCPort_Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FCPort_Description_Type.__name__ = "DisplayString"
_FCPort_Description_Object = MibScalar
fCPort_Description = _FCPort_Description_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2, 1, 5),
    _FCPort_Description_Type()
)
fCPort_Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCPort_Description.setStatus("mandatory")


class _FCPortController_OperationalStatus_Type(Integer32):
    """Custom type fCPortController_OperationalStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("completed", 17),
          ("dMTFReserved", 19),
          ("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("inService", 11),
          ("lostCommunication", 13),
          ("noContact", 12),
          ("non-RecoverableError", 7),
          ("ok", 2),
          ("other", 1),
          ("powerMode", 18),
          ("predictiveFailure", 5),
          ("starting", 8),
          ("stopped", 10),
          ("stopping", 9),
          ("stressed", 4),
          ("supportingEntityInError", 16),
          ("unknown", 0),
          ("vendorReserved", 32768))
    )


_FCPortController_OperationalStatus_Type.__name__ = "Integer32"
_FCPortController_OperationalStatus_Object = MibScalar
fCPortController_OperationalStatus = _FCPortController_OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2, 1, 6),
    _FCPortController_OperationalStatus_Type()
)
fCPortController_OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCPortController_OperationalStatus.setStatus("mandatory")


class _FCPort_PermanentAddress_Type(DisplayString):
    """Custom type fCPort_PermanentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FCPort_PermanentAddress_Type.__name__ = "DisplayString"
_FCPort_PermanentAddress_Object = MibScalar
fCPort_PermanentAddress = _FCPort_PermanentAddress_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2, 1, 7),
    _FCPort_PermanentAddress_Type()
)
fCPort_PermanentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCPort_PermanentAddress.setStatus("mandatory")
_FCPort_Realizes_scsiProtocolControllerIndex_Type = UINT32
_FCPort_Realizes_scsiProtocolControllerIndex_Object = MibScalar
fCPort_Realizes_scsiProtocolControllerIndex = _FCPort_Realizes_scsiProtocolControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 15, 2, 1, 8),
    _FCPort_Realizes_scsiProtocolControllerIndex_Type()
)
fCPort_Realizes_scsiProtocolControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCPort_Realizes_scsiProtocolControllerIndex.setStatus("mandatory")
_TrapGroup_ObjectIdentity = ObjectIdentity
trapGroup = _TrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16)
)


class _TrapsEnabled_Type(Integer32):
    """Custom type trapsEnabled based on Integer32"""
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


_TrapsEnabled_Type.__name__ = "Integer32"
_TrapsEnabled_Object = MibScalar
trapsEnabled = _TrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 1),
    _TrapsEnabled_Type()
)
trapsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsEnabled.setStatus("mandatory")


class _TrapDriveAlertSummary_Type(Integer32):
    """Custom type trapDriveAlertSummary based on Integer32"""
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
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60)
        )
    )
    namedValues = NamedValues(
        *(("automationInterfaceFailure", 57),
          ("cleanNow", 20),
          ("cleanPeriodic", 21),
          ("cleaningMedia", 11),
          ("coolingFanError", 26),
          ("diagnosticsRequired", 39),
          ("directoryCorruptedOnLoad", 18),
          ("downloadFailure", 34),
          ("driveHumidity", 35),
          ("driveMaintenance", 29),
          ("driveTemperature", 36),
          ("driveVoltage", 37),
          ("dualPortInterfaceError", 25),
          ("ejectMedia", 33),
          ("expiredCleaningMedia", 22),
          ("firmwareFailure", 58),
          ("forcedEject", 16),
          ("hardError", 3),
          ("hardwareA", 30),
          ("hardwareB", 31),
          ("interface", 32),
          ("invalidCleaningMedia", 23),
          ("loadingFailure", 55),
          ("lostStatistics", 50),
          ("media", 4),
          ("mediaDirectoryInvalidAtUnload", 51),
          ("mediaLife", 7),
          ("mediaSystemAreaReadFailure", 53),
          ("mediaSystemAreaWriteFailure", 52),
          ("memoryChipInCartridgeFailure", 15),
          ("nearingMediaLife", 19),
          ("noRemoval", 10),
          ("noStartOfData", 54),
          ("notDataGrade", 8),
          ("powerConsumption", 28),
          ("powerSupplyFailure", 27),
          ("predictiveFailure", 38),
          ("readFailure", 5),
          ("readOnlyFormat", 17),
          ("readWarning", 1),
          ("recoverableSnappedTape", 13),
          ("retentionRequested", 24),
          ("unrecoverableSnappedTape", 14),
          ("unrecoverableUnloadFailure", 56),
          ("unsupportedFormat", 12),
          ("wormMediumIntegrityCheckFailed", 59),
          ("wormMediumOverwriteAttempted", 60),
          ("writeFailure", 6),
          ("writeProtect", 9),
          ("writeWarning", 2))
    )


_TrapDriveAlertSummary_Type.__name__ = "Integer32"
_TrapDriveAlertSummary_Object = MibScalar
trapDriveAlertSummary = _TrapDriveAlertSummary_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 2),
    _TrapDriveAlertSummary_Type()
)
trapDriveAlertSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDriveAlertSummary.setStatus("mandatory")
_Trap_Association_MediaAccessDeviceIndex_Type = UINT32
_Trap_Association_MediaAccessDeviceIndex_Object = MibScalar
trap_Association_MediaAccessDeviceIndex = _Trap_Association_MediaAccessDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 3),
    _Trap_Association_MediaAccessDeviceIndex_Type()
)
trap_Association_MediaAccessDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_Association_MediaAccessDeviceIndex.setStatus("mandatory")


class _TrapChangerAlertSummary_Type(Integer32):
    """Custom type trapChangerAlertSummary based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("cartridgeInPassThroughMechanism", 31),
          ("coolingFanFailure", 27),
          ("dualPortInterfaceError", 26),
          ("failurePrediction", 7),
          ("libraryDiagnosticsRequired", 5),
          ("libraryDoor", 16),
          ("libraryDriveOffline", 22),
          ("libraryHardwareA", 1),
          ("libraryHardwareB", 2),
          ("libraryHardwareC", 3),
          ("libraryHardwareD", 4),
          ("libraryHumidityLimits", 9),
          ("libraryIllegalOperation", 25),
          ("libraryInterface", 6),
          ("libraryInventory", 24),
          ("libraryLoadRetry", 15),
          ("libraryMagazine", 18),
          ("libraryMailslot", 17),
          ("libraryMaintenance", 8),
          ("libraryOffline", 21),
          ("libraryPickRetry", 13),
          ("libraryPlaceRetry", 14),
          ("libraryScanRetry", 23),
          ("librarySecurity", 19),
          ("librarySecurityMode", 20),
          ("libraryStrayMedia", 12),
          ("libraryTemperatureLimits", 10),
          ("libraryVoltageLimits", 11),
          ("passThroughMechanismFailure", 30),
          ("powerConsumption", 29),
          ("powerSupply", 28),
          ("unreadableBarCodeLabels", 32))
    )


_TrapChangerAlertSummary_Type.__name__ = "Integer32"
_TrapChangerAlertSummary_Object = MibScalar
trapChangerAlertSummary = _TrapChangerAlertSummary_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 4),
    _TrapChangerAlertSummary_Type()
)
trapChangerAlertSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangerAlertSummary.setStatus("mandatory")
_Trap_Association_ChangerDeviceIndex_Type = UINT32
_Trap_Association_ChangerDeviceIndex_Object = MibScalar
trap_Association_ChangerDeviceIndex = _Trap_Association_ChangerDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 5),
    _Trap_Association_ChangerDeviceIndex_Type()
)
trap_Association_ChangerDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_Association_ChangerDeviceIndex.setStatus("mandatory")


class _TrapPerceivedSeverity_Type(Integer32):
    """Custom type trapPerceivedSeverity based on Integer32"""
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
        *(("critical", 6),
          ("degradedWarning", 3),
          ("fatalNonRecoverable", 7),
          ("information", 2),
          ("major", 5),
          ("minor", 4),
          ("other", 1),
          ("unknown", 0))
    )


_TrapPerceivedSeverity_Type.__name__ = "Integer32"
_TrapPerceivedSeverity_Object = MibScalar
trapPerceivedSeverity = _TrapPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 6),
    _TrapPerceivedSeverity_Type()
)
trapPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPerceivedSeverity.setStatus("mandatory")
_TrapDestinationTable_Object = MibTable
trapDestinationTable = _TrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 7)
)
if mibBuilder.loadTexts:
    trapDestinationTable.setStatus("mandatory")
_TrapDestinationEntry_Object = MibTableRow
trapDestinationEntry = _TrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 7, 1)
)
trapDestinationEntry.setIndexNames(
    (0, "SNIA-SML-MIB", "numberOfTrapDestinations"),
)
if mibBuilder.loadTexts:
    trapDestinationEntry.setStatus("mandatory")
_NumberOfTrapDestinations_Type = Integer32
_NumberOfTrapDestinations_Object = MibTableColumn
numberOfTrapDestinations = _NumberOfTrapDestinations_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 7, 1, 1),
    _NumberOfTrapDestinations_Type()
)
numberOfTrapDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfTrapDestinations.setStatus("mandatory")


class _TrapDestinationHostType_Type(Integer32):
    """Custom type trapDestinationHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 1),
          ("iPv6", 2))
    )


_TrapDestinationHostType_Type.__name__ = "Integer32"
_TrapDestinationHostType_Object = MibTableColumn
trapDestinationHostType = _TrapDestinationHostType_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 7, 1, 2),
    _TrapDestinationHostType_Type()
)
trapDestinationHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestinationHostType.setStatus("mandatory")
_TrapDestinationHostAddr_Type = DisplayString
_TrapDestinationHostAddr_Object = MibTableColumn
trapDestinationHostAddr = _TrapDestinationHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 7, 1, 3),
    _TrapDestinationHostAddr_Type()
)
trapDestinationHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestinationHostAddr.setStatus("mandatory")


class _TrapDestinationPort_Type(Integer32):
    """Custom type trapDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapDestinationPort_Type.__name__ = "Integer32"
_TrapDestinationPort_Object = MibTableColumn
trapDestinationPort = _TrapDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 7, 1, 4),
    _TrapDestinationPort_Type()
)
trapDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestinationPort.setStatus("mandatory")
_TrapObjects_ObjectIdentity = ObjectIdentity
trapObjects = _TrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 8)
)


class _CurrentOperationalStatus_Type(Integer32):
    """Custom type currentOperationalStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("completed", 17),
          ("dMTFReserved", 19),
          ("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("inService", 11),
          ("lostCommunication", 13),
          ("noContact", 12),
          ("non-RecoverableError", 7),
          ("ok", 2),
          ("other", 1),
          ("powerMode", 18),
          ("predictiveFailure", 5),
          ("starting", 8),
          ("stopped", 10),
          ("stopping", 9),
          ("stressed", 4),
          ("supportingEntityInError", 16),
          ("unknown", 0),
          ("vendorReserved", 32768))
    )


_CurrentOperationalStatus_Type.__name__ = "Integer32"
_CurrentOperationalStatus_Object = MibScalar
currentOperationalStatus = _CurrentOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 8, 1),
    _CurrentOperationalStatus_Type()
)
currentOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentOperationalStatus.setStatus("mandatory")


class _OldOperationalStatus_Type(Integer32):
    """Custom type oldOperationalStatus based on Integer32"""
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
              32768)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("completed", 17),
          ("dMTFReserved", 19),
          ("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("inService", 11),
          ("lostCommunication", 13),
          ("noContact", 12),
          ("non-RecoverableError", 7),
          ("ok", 2),
          ("other", 1),
          ("powerMode", 18),
          ("predictiveFailure", 5),
          ("starting", 8),
          ("stopped", 10),
          ("stopping", 9),
          ("stressed", 4),
          ("supportingEntityInError", 16),
          ("unknown", 0),
          ("vendorReserved", 32768))
    )


_OldOperationalStatus_Type.__name__ = "Integer32"
_OldOperationalStatus_Object = MibScalar
oldOperationalStatus = _OldOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 8, 2),
    _OldOperationalStatus_Type()
)
oldOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oldOperationalStatus.setStatus("mandatory")
_EndOfSmlMib_Type = ObjectIdentifier
_EndOfSmlMib_Object = MibScalar
endOfSmlMib = _EndOfSmlMib_Object(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 17),
    _EndOfSmlMib_Type()
)
endOfSmlMib.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    endOfSmlMib.setStatus("mandatory")

# Managed Objects groups


# Notification objects

driveAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 0, 0)
)
driveAlert.setObjects(
      *(("SNIA-SML-MIB", "trapDriveAlertSummary"),
        ("SNIA-SML-MIB", "trap_Association_MediaAccessDeviceIndex"),
        ("SNIA-SML-MIB", "trapPerceivedSeverity"))
)
if mibBuilder.loadTexts:
    driveAlert.setStatus(
        ""
    )

changerAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 0, 1)
)
changerAlert.setObjects(
      *(("SNIA-SML-MIB", "trapChangerAlertSummary"),
        ("SNIA-SML-MIB", "trap_Association_ChangerDeviceIndex"),
        ("SNIA-SML-MIB", "trapPerceivedSeverity"))
)
if mibBuilder.loadTexts:
    changerAlert.setStatus(
        ""
    )

libraryAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 3)
)
libraryAddedTrap.setObjects(
    ("SNIA-SML-MIB", "storageLibrary_Name")
)
if mibBuilder.loadTexts:
    libraryAddedTrap.setStatus(
        ""
    )

libraryDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 4)
)
libraryDeletedTrap.setObjects(
    ("SNIA-SML-MIB", "storageLibrary_Name")
)
if mibBuilder.loadTexts:
    libraryDeletedTrap.setStatus(
        ""
    )

libraryOpStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 5)
)
libraryOpStatusChangedTrap.setObjects(
      *(("SNIA-SML-MIB", "storageLibrary_Name"),
        ("SNIA-SML-MIB", "currentOperationalStatus"),
        ("SNIA-SML-MIB", "oldOperationalStatus"))
)
if mibBuilder.loadTexts:
    libraryOpStatusChangedTrap.setStatus(
        ""
    )

driveAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 6)
)
driveAddedTrap.setObjects(
      *(("SNIA-SML-MIB", "storageLibrary_Name"),
        ("SNIA-SML-MIB", "mediaAccessDevice_DeviceID"))
)
if mibBuilder.loadTexts:
    driveAddedTrap.setStatus(
        ""
    )

driveDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 7)
)
driveDeletedTrap.setObjects(
      *(("SNIA-SML-MIB", "storageLibrary_Name"),
        ("SNIA-SML-MIB", "mediaAccessDevice_DeviceID"))
)
if mibBuilder.loadTexts:
    driveDeletedTrap.setStatus(
        ""
    )

driveOpStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 8)
)
driveOpStatusChangedTrap.setObjects(
      *(("SNIA-SML-MIB", "storageLibrary_Name"),
        ("SNIA-SML-MIB", "mediaAccessDevice_DeviceID"),
        ("SNIA-SML-MIB", "currentOperationalStatus"),
        ("SNIA-SML-MIB", "oldOperationalStatus"))
)
if mibBuilder.loadTexts:
    driveOpStatusChangedTrap.setStatus(
        ""
    )

changerAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 9)
)
changerAddedTrap.setObjects(
      *(("SNIA-SML-MIB", "storageLibrary_Name"),
        ("SNIA-SML-MIB", "changerDevice_DeviceID"))
)
if mibBuilder.loadTexts:
    changerAddedTrap.setStatus(
        ""
    )

changerDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 10)
)
changerDeletedTrap.setObjects(
      *(("SNIA-SML-MIB", "storageLibrary_Name"),
        ("SNIA-SML-MIB", "changerDevice_DeviceID"))
)
if mibBuilder.loadTexts:
    changerDeletedTrap.setStatus(
        ""
    )

changerOpStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 11)
)
changerOpStatusChangedTrap.setObjects(
      *(("SNIA-SML-MIB", "storageLibrary_Name"),
        ("SNIA-SML-MIB", "changerDevice_DeviceID"),
        ("SNIA-SML-MIB", "currentOperationalStatus"),
        ("SNIA-SML-MIB", "oldOperationalStatus"))
)
if mibBuilder.loadTexts:
    changerOpStatusChangedTrap.setStatus(
        ""
    )

physicalMediaAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 12)
)
physicalMediaAddedTrap.setObjects(
    ("SNIA-SML-MIB", "storageMediaLocation_PhysicalMedia_Tag")
)
if mibBuilder.loadTexts:
    physicalMediaAddedTrap.setStatus(
        ""
    )

physicalMediaDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14851, 3, 1, 16, 0, 13)
)
physicalMediaDeletedTrap.setObjects(
    ("SNIA-SML-MIB", "storageMediaLocation_PhysicalMedia_Tag")
)
if mibBuilder.loadTexts:
    physicalMediaDeletedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNIA-SML-MIB",
    **{"UShortReal": UShortReal,
       "CimDateTime": CimDateTime,
       "UINT64": UINT64,
       "UINT32": UINT32,
       "UINT16": UINT16,
       "snia": snia,
       "experimental": experimental,
       "common": common,
       "libraries": libraries,
       "smlRoot": smlRoot,
       "driveAlert": driveAlert,
       "changerAlert": changerAlert,
       "smlMibVersion": smlMibVersion,
       "smlCimVersion": smlCimVersion,
       "productGroup": productGroup,
       "product-Name": product_Name,
       "product-IdentifyingNumber": product_IdentifyingNumber,
       "product-Vendor": product_Vendor,
       "product-Version": product_Version,
       "product-ElementName": product_ElementName,
       "chassisGroup": chassisGroup,
       "chassis-Manufacturer": chassis_Manufacturer,
       "chassis-Model": chassis_Model,
       "chassis-SerialNumber": chassis_SerialNumber,
       "chassis-LockPresent": chassis_LockPresent,
       "chassis-SecurityBreach": chassis_SecurityBreach,
       "chassis-IsLocked": chassis_IsLocked,
       "chassis-Tag": chassis_Tag,
       "chassis-ElementName": chassis_ElementName,
       "numberOfsubChassis": numberOfsubChassis,
       "subChassisTable": subChassisTable,
       "subChassisEntry": subChassisEntry,
       "subChassisIndex": subChassisIndex,
       "subChassis-Manufacturer": subChassis_Manufacturer,
       "subChassis-Model": subChassis_Model,
       "subChassis-SerialNumber": subChassis_SerialNumber,
       "subChassis-LockPresent": subChassis_LockPresent,
       "subChassis-SecurityBreach": subChassis_SecurityBreach,
       "subChassis-IsLocked": subChassis_IsLocked,
       "subChassis-Tag": subChassis_Tag,
       "subChassis-ElementName": subChassis_ElementName,
       "subChassis-OperationalStatus": subChassis_OperationalStatus,
       "subChassis-PackageType": subChassis_PackageType,
       "storageLibraryGroup": storageLibraryGroup,
       "storageLibrary-Name": storageLibrary_Name,
       "storageLibrary-Description": storageLibrary_Description,
       "storageLibrary-Caption": storageLibrary_Caption,
       "storageLibrary-Status": storageLibrary_Status,
       "storageLibrary-InstallDate": storageLibrary_InstallDate,
       "mediaAccessDeviceGroup": mediaAccessDeviceGroup,
       "numberOfMediaAccessDevices": numberOfMediaAccessDevices,
       "mediaAccessDeviceTable": mediaAccessDeviceTable,
       "mediaAccessDeviceEntry": mediaAccessDeviceEntry,
       "mediaAccessDeviceIndex": mediaAccessDeviceIndex,
       "mediaAccessDeviceObjectType": mediaAccessDeviceObjectType,
       "mediaAccessDevice-Name": mediaAccessDevice_Name,
       "mediaAccessDevice-Status": mediaAccessDevice_Status,
       "mediaAccessDevice-Availability": mediaAccessDevice_Availability,
       "mediaAccessDevice-NeedsCleaning": mediaAccessDevice_NeedsCleaning,
       "mediaAccessDevice-MountCount": mediaAccessDevice_MountCount,
       "mediaAccessDevice-DeviceID": mediaAccessDevice_DeviceID,
       "mediaAccessDevice-PowerOnHours": mediaAccessDevice_PowerOnHours,
       "mediaAccessDevice-TotalPowerOnHours": mediaAccessDevice_TotalPowerOnHours,
       "mediaAccessDevice-OperationalStatus": mediaAccessDevice_OperationalStatus,
       "mediaAccessDevice-Realizes-StorageLocationIndex": mediaAccessDevice_Realizes_StorageLocationIndex,
       "mediaAccessDevice-Realizes-softwareElementIndex": mediaAccessDevice_Realizes_softwareElementIndex,
       "physicalPackageGroup": physicalPackageGroup,
       "numberOfPhysicalPackages": numberOfPhysicalPackages,
       "physicalPackageTable": physicalPackageTable,
       "physicalPackageEntry": physicalPackageEntry,
       "physicalPackageIndex": physicalPackageIndex,
       "physicalPackage-Manufacturer": physicalPackage_Manufacturer,
       "physicalPackage-Model": physicalPackage_Model,
       "physicalPackage-SerialNumber": physicalPackage_SerialNumber,
       "physicalPackage-Realizes-MediaAccessDeviceIndex": physicalPackage_Realizes_MediaAccessDeviceIndex,
       "physicalPackage-Tag": physicalPackage_Tag,
       "softwareElementGroup": softwareElementGroup,
       "numberOfSoftwareElements": numberOfSoftwareElements,
       "softwareElementTable": softwareElementTable,
       "softwareElementEntry": softwareElementEntry,
       "softwareElementIndex": softwareElementIndex,
       "softwareElement-Name": softwareElement_Name,
       "softwareElement-Version": softwareElement_Version,
       "softwareElement-SoftwareElementID": softwareElement_SoftwareElementID,
       "softwareElement-Manufacturer": softwareElement_Manufacturer,
       "softwareElement-BuildNumber": softwareElement_BuildNumber,
       "softwareElement-SerialNumber": softwareElement_SerialNumber,
       "softwareElement-CodeSet": softwareElement_CodeSet,
       "softwareElement-IdentificationCode": softwareElement_IdentificationCode,
       "softwareElement-LanguageEdition": softwareElement_LanguageEdition,
       "softwareElement-InstanceID": softwareElement_InstanceID,
       "computerSystemGroup": computerSystemGroup,
       "computerSystem-ElementName": computerSystem_ElementName,
       "computerSystem-OperationalStatus": computerSystem_OperationalStatus,
       "computerSystem-Name": computerSystem_Name,
       "computerSystem-NameFormat": computerSystem_NameFormat,
       "computerSystem-Dedicated": computerSystem_Dedicated,
       "computerSystem-PrimaryOwnerContact": computerSystem_PrimaryOwnerContact,
       "computerSystem-PrimaryOwnerName": computerSystem_PrimaryOwnerName,
       "computerSystem-Description": computerSystem_Description,
       "computerSystem-Caption": computerSystem_Caption,
       "computerSystem-Realizes-softwareElementIndex": computerSystem_Realizes_softwareElementIndex,
       "changerDeviceGroup": changerDeviceGroup,
       "numberOfChangerDevices": numberOfChangerDevices,
       "changerDeviceTable": changerDeviceTable,
       "changerDeviceEntry": changerDeviceEntry,
       "changerDeviceIndex": changerDeviceIndex,
       "changerDevice-DeviceID": changerDevice_DeviceID,
       "changerDevice-MediaFlipSupported": changerDevice_MediaFlipSupported,
       "changerDevice-ElementName": changerDevice_ElementName,
       "changerDevice-Caption": changerDevice_Caption,
       "changerDevice-Description": changerDevice_Description,
       "changerDevice-Availability": changerDevice_Availability,
       "changerDevice-OperationalStatus": changerDevice_OperationalStatus,
       "changerDevice-Realizes-StorageLocationIndex": changerDevice_Realizes_StorageLocationIndex,
       "scsiProtocolControllerGroup": scsiProtocolControllerGroup,
       "numberOfSCSIProtocolControllers": numberOfSCSIProtocolControllers,
       "scsiProtocolControllerTable": scsiProtocolControllerTable,
       "scsiProtocolControllerEntry": scsiProtocolControllerEntry,
       "scsiProtocolControllerIndex": scsiProtocolControllerIndex,
       "scsiProtocolController-DeviceID": scsiProtocolController_DeviceID,
       "scsiProtocolController-ElementName": scsiProtocolController_ElementName,
       "scsiProtocolController-OperationalStatus": scsiProtocolController_OperationalStatus,
       "scsiProtocolController-Description": scsiProtocolController_Description,
       "scsiProtocolController-Availability": scsiProtocolController_Availability,
       "scsiProtocolController-Realizes-ChangerDeviceIndex": scsiProtocolController_Realizes_ChangerDeviceIndex,
       "scsiProtocolController-Realizes-MediaAccessDeviceIndex": scsiProtocolController_Realizes_MediaAccessDeviceIndex,
       "storageMediaLocationGroup": storageMediaLocationGroup,
       "numberOfStorageMediaLocations": numberOfStorageMediaLocations,
       "numberOfPhysicalMedias": numberOfPhysicalMedias,
       "storageMediaLocationTable": storageMediaLocationTable,
       "storageMediaLocationEntry": storageMediaLocationEntry,
       "storageMediaLocationIndex": storageMediaLocationIndex,
       "storageMediaLocation-Tag": storageMediaLocation_Tag,
       "storageMediaLocation-LocationType": storageMediaLocation_LocationType,
       "storageMediaLocation-LocationCoordinates": storageMediaLocation_LocationCoordinates,
       "storageMediaLocation-MediaTypesSupported": storageMediaLocation_MediaTypesSupported,
       "storageMediaLocation-MediaCapacity": storageMediaLocation_MediaCapacity,
       "storageMediaLocation-Association-ChangerDeviceIndex": storageMediaLocation_Association_ChangerDeviceIndex,
       "storageMediaLocation-PhysicalMediaPresent": storageMediaLocation_PhysicalMediaPresent,
       "storageMediaLocation-PhysicalMedia-Removable": storageMediaLocation_PhysicalMedia_Removable,
       "storageMediaLocation-PhysicalMedia-Replaceable": storageMediaLocation_PhysicalMedia_Replaceable,
       "storageMediaLocation-PhysicalMedia-HotSwappable": storageMediaLocation_PhysicalMedia_HotSwappable,
       "storageMediaLocation-PhysicalMedia-Capacity": storageMediaLocation_PhysicalMedia_Capacity,
       "storageMediaLocation-PhysicalMedia-MediaType": storageMediaLocation_PhysicalMedia_MediaType,
       "storageMediaLocation-PhysicalMedia-MediaDescription": storageMediaLocation_PhysicalMedia_MediaDescription,
       "storageMediaLocation-PhysicalMedia-CleanerMedia": storageMediaLocation_PhysicalMedia_CleanerMedia,
       "storageMediaLocation-PhysicalMedia-DualSided": storageMediaLocation_PhysicalMedia_DualSided,
       "storageMediaLocation-PhysicalMedia-PhysicalLabel": storageMediaLocation_PhysicalMedia_PhysicalLabel,
       "storageMediaLocation-PhysicalMedia-Tag": storageMediaLocation_PhysicalMedia_Tag,
       "limitedAccessPortGroup": limitedAccessPortGroup,
       "numberOflimitedAccessPorts": numberOflimitedAccessPorts,
       "limitedAccessPortTable": limitedAccessPortTable,
       "limitedAccessPortEntry": limitedAccessPortEntry,
       "limitedAccessPortIndex": limitedAccessPortIndex,
       "limitedAccessPort-DeviceID": limitedAccessPort_DeviceID,
       "limitedAccessPort-Extended": limitedAccessPort_Extended,
       "limitedAccessPort-ElementName": limitedAccessPort_ElementName,
       "limitedAccessPort-Caption": limitedAccessPort_Caption,
       "limitedAccessPort-Description": limitedAccessPort_Description,
       "limitedAccessPort-Realizes-StorageLocationIndex": limitedAccessPort_Realizes_StorageLocationIndex,
       "fCPortGroup": fCPortGroup,
       "numberOffCPorts": numberOffCPorts,
       "fCPortTable": fCPortTable,
       "fCPortEntry": fCPortEntry,
       "fCPortIndex": fCPortIndex,
       "fCPort-DeviceID": fCPort_DeviceID,
       "fCPort-ElementName": fCPort_ElementName,
       "fCPort-Caption": fCPort_Caption,
       "fCPort-Description": fCPort_Description,
       "fCPortController-OperationalStatus": fCPortController_OperationalStatus,
       "fCPort-PermanentAddress": fCPort_PermanentAddress,
       "fCPort-Realizes-scsiProtocolControllerIndex": fCPort_Realizes_scsiProtocolControllerIndex,
       "trapGroup": trapGroup,
       "libraryAddedTrap": libraryAddedTrap,
       "libraryDeletedTrap": libraryDeletedTrap,
       "libraryOpStatusChangedTrap": libraryOpStatusChangedTrap,
       "driveAddedTrap": driveAddedTrap,
       "driveDeletedTrap": driveDeletedTrap,
       "driveOpStatusChangedTrap": driveOpStatusChangedTrap,
       "changerAddedTrap": changerAddedTrap,
       "changerDeletedTrap": changerDeletedTrap,
       "changerOpStatusChangedTrap": changerOpStatusChangedTrap,
       "physicalMediaAddedTrap": physicalMediaAddedTrap,
       "physicalMediaDeletedTrap": physicalMediaDeletedTrap,
       "trapsEnabled": trapsEnabled,
       "trapDriveAlertSummary": trapDriveAlertSummary,
       "trap-Association-MediaAccessDeviceIndex": trap_Association_MediaAccessDeviceIndex,
       "trapChangerAlertSummary": trapChangerAlertSummary,
       "trap-Association-ChangerDeviceIndex": trap_Association_ChangerDeviceIndex,
       "trapPerceivedSeverity": trapPerceivedSeverity,
       "trapDestinationTable": trapDestinationTable,
       "trapDestinationEntry": trapDestinationEntry,
       "numberOfTrapDestinations": numberOfTrapDestinations,
       "trapDestinationHostType": trapDestinationHostType,
       "trapDestinationHostAddr": trapDestinationHostAddr,
       "trapDestinationPort": trapDestinationPort,
       "trapObjects": trapObjects,
       "currentOperationalStatus": currentOperationalStatus,
       "oldOperationalStatus": oldOperationalStatus,
       "endOfSmlMib": endOfSmlMib}
)
