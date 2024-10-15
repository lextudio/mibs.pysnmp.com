# SNMP MIB module (IbmFaultMgmt-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IbmFaultMgmt-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:29 2024
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmArchitecture_ObjectIdentity = ObjectIdentity
ibmArchitecture = _IbmArchitecture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5)
)
_Alert_ObjectIdentity = ObjectIdentity
alert = _Alert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1)
)
_Product_Set_ID_ObjectIdentity = ObjectIdentity
product_Set_ID = _Product_Set_ID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3)
)
_HwProductInstallSpecificInfoTable_Object = MibTable
hwProductInstallSpecificInfoTable = _HwProductInstallSpecificInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwProductInstallSpecificInfoTable.setStatus("optional")
_HwProductEntry_Object = MibTableRow
hwProductEntry = _HwProductEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwProductEntry.setStatus("optional")


class _ProductClassificationHW_Type(Integer32):
    """Custom type productClassificationHW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("hwIBM", 1),
          ("hwIBM-NonIBM", 3),
          ("hwNonIBM", 9))
    )


_ProductClassificationHW_Type.__name__ = "Integer32"
_ProductClassificationHW_Object = MibTableColumn
productClassificationHW = _ProductClassificationHW_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1, 1),
    _ProductClassificationHW_Type()
)
productClassificationHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productClassificationHW.setStatus("optional")


class _FormatType_Type(Integer32):
    """Custom type formatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            17
        )
    )
    namedValues = NamedValues(
        ("form11", 17)
    )


_FormatType_Type.__name__ = "Integer32"
_FormatType_Object = MibTableColumn
formatType = _FormatType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1, 2),
    _FormatType_Type()
)
formatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    formatType.setStatus("optional")


class _MachineType_Type(DisplayString):
    """Custom type machineType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MachineType_Type.__name__ = "DisplayString"
_MachineType_Object = MibTableColumn
machineType = _MachineType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1, 3),
    _MachineType_Type()
)
machineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineType.setStatus("optional")


class _ModelNum_Type(DisplayString):
    """Custom type modelNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_ModelNum_Type.__name__ = "DisplayString"
_ModelNum_Object = MibTableColumn
modelNum = _ModelNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1, 4),
    _ModelNum_Type()
)
modelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelNum.setStatus("optional")


class _PlantOfManufacture_Type(DisplayString):
    """Custom type plantOfManufacture based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PlantOfManufacture_Type.__name__ = "DisplayString"
_PlantOfManufacture_Object = MibTableColumn
plantOfManufacture = _PlantOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1, 5),
    _PlantOfManufacture_Type()
)
plantOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plantOfManufacture.setStatus("optional")


class _SeqNum_Type(DisplayString):
    """Custom type seqNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SeqNum_Type.__name__ = "DisplayString"
_SeqNum_Object = MibTableColumn
seqNum = _SeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1, 6),
    _SeqNum_Type()
)
seqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seqNum.setStatus("optional")


class _MicrocodeECLevel_Type(DisplayString):
    """Custom type microcodeECLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MicrocodeECLevel_Type.__name__ = "DisplayString"
_MicrocodeECLevel_Object = MibTableColumn
microcodeECLevel = _MicrocodeECLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1, 7),
    _MicrocodeECLevel_Type()
)
microcodeECLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    microcodeECLevel.setStatus("optional")


class _HardwareProdCommonName_Type(DisplayString):
    """Custom type hardwareProdCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HardwareProdCommonName_Type.__name__ = "DisplayString"
_HardwareProdCommonName_Object = MibTableColumn
hardwareProdCommonName = _HardwareProdCommonName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1, 8),
    _HardwareProdCommonName_Type()
)
hardwareProdCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareProdCommonName.setStatus("optional")


class _VendorIDhw_Type(DisplayString):
    """Custom type vendorIDhw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VendorIDhw_Type.__name__ = "DisplayString"
_VendorIDhw_Object = MibTableColumn
vendorIDhw = _VendorIDhw_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 1, 1, 9),
    _VendorIDhw_Type()
)
vendorIDhw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorIDhw.setStatus("optional")
_SwProductInstallSpecificInfoTable_Object = MibTable
swProductInstallSpecificInfoTable = _SwProductInstallSpecificInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    swProductInstallSpecificInfoTable.setStatus("optional")
_SwProductEntry_Object = MibTableRow
swProductEntry = _SwProductEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    swProductEntry.setStatus("optional")


class _ProductClassificationSW_Type(Integer32):
    """Custom type productClassificationSW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("swIBM", 4),
          ("swIBM-NonIBM", 14),
          ("swNonIBM", 12))
    )


_ProductClassificationSW_Type.__name__ = "Integer32"
_ProductClassificationSW_Object = MibTableColumn
productClassificationSW = _ProductClassificationSW_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 2, 1, 1),
    _ProductClassificationSW_Type()
)
productClassificationSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productClassificationSW.setStatus("optional")


class _CommonVerID_Type(DisplayString):
    """Custom type commonVerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CommonVerID_Type.__name__ = "DisplayString"
_CommonVerID_Object = MibTableColumn
commonVerID = _CommonVerID_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 2, 1, 2),
    _CommonVerID_Type()
)
commonVerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonVerID.setStatus("optional")


class _CommonRelID_Type(DisplayString):
    """Custom type commonRelID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CommonRelID_Type.__name__ = "DisplayString"
_CommonRelID_Object = MibTableColumn
commonRelID = _CommonRelID_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 2, 1, 3),
    _CommonRelID_Type()
)
commonRelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonRelID.setStatus("optional")


class _CommonModID_Type(DisplayString):
    """Custom type commonModID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CommonModID_Type.__name__ = "DisplayString"
_CommonModID_Object = MibTableColumn
commonModID = _CommonModID_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 2, 1, 4),
    _CommonModID_Type()
)
commonModID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonModID.setStatus("optional")


class _SoftwareProdCommonName_Type(DisplayString):
    """Custom type softwareProdCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SoftwareProdCommonName_Type.__name__ = "DisplayString"
_SoftwareProdCommonName_Object = MibTableColumn
softwareProdCommonName = _SoftwareProdCommonName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 2, 1, 5),
    _SoftwareProdCommonName_Type()
)
softwareProdCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareProdCommonName.setStatus("optional")


class _SoftwareProdProgNmbr_Type(DisplayString):
    """Custom type softwareProdProgNmbr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SoftwareProdProgNmbr_Type.__name__ = "DisplayString"
_SoftwareProdProgNmbr_Object = MibTableColumn
softwareProdProgNmbr = _SoftwareProdProgNmbr_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 2, 1, 6),
    _SoftwareProdProgNmbr_Type()
)
softwareProdProgNmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareProdProgNmbr.setStatus("optional")


class _VendorIDsw_Type(DisplayString):
    """Custom type vendorIDsw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VendorIDsw_Type.__name__ = "DisplayString"
_VendorIDsw_Object = MibTableColumn
vendorIDsw = _VendorIDsw_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 3, 2, 1, 7),
    _VendorIDsw_Type()
)
vendorIDsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorIDsw.setStatus("optional")
_Supporting_Data_Correl_ObjectIdentity = ObjectIdentity
supporting_Data_Correl = _Supporting_Data_Correl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 7)
)
_DetailedDataSDTable_Object = MibTable
detailedDataSDTable = _DetailedDataSDTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 7, 2)
)
if mibBuilder.loadTexts:
    detailedDataSDTable.setStatus("optional")
_DetailedDataSDEntry_Object = MibTableRow
detailedDataSDEntry = _DetailedDataSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    detailedDataSDEntry.setStatus("optional")


class _ProductIDCodeSD_Type(Integer32):
    """Custom type productIDCodeSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              41,
              42,
              153,
              154)
        )
    )
    namedValues = NamedValues(
        *(("displayFirstHW", 41),
          ("displayFirstSW", 153),
          ("displayNone", 0),
          ("displaySecondHW", 42),
          ("displaySecondSW", 154))
    )


_ProductIDCodeSD_Type.__name__ = "Integer32"
_ProductIDCodeSD_Object = MibTableColumn
productIDCodeSD = _ProductIDCodeSD_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 7, 2, 1, 1),
    _ProductIDCodeSD_Type()
)
productIDCodeSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDCodeSD.setStatus("optional")


class _DataIDCodeSD_Type(Integer32):
    """Custom type dataIDCodeSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DataIDCodeSD_Type.__name__ = "Integer32"
_DataIDCodeSD_Object = MibTableColumn
dataIDCodeSD = _DataIDCodeSD_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 7, 2, 1, 2),
    _DataIDCodeSD_Type()
)
dataIDCodeSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataIDCodeSD.setStatus("optional")


class _DataEncodingSD_Type(Integer32):
    """Custom type dataEncodingSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 17),
          ("binary", 1),
          ("hex", 0))
    )


_DataEncodingSD_Type.__name__ = "Integer32"
_DataEncodingSD_Object = MibTableColumn
dataEncodingSD = _DataEncodingSD_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 7, 2, 1, 3),
    _DataEncodingSD_Type()
)
dataEncodingSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEncodingSD.setStatus("optional")


class _DataSD_Type(OctetString):
    """Custom type dataSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_DataSD_Type.__name__ = "OctetString"
_DataSD_Object = MibTableColumn
dataSD = _DataSD_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 7, 2, 1, 4),
    _DataSD_Type()
)
dataSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSD.setStatus("optional")
_Generic_Alert_Data_ObjectIdentity = ObjectIdentity
generic_Alert_Data = _Generic_Alert_Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 11)
)


class _Flags_Type(Integer32):
    """Custom type flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Flags_Type.__name__ = "Integer32"
_Flags_Object = MibScalar
flags = _Flags_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 11, 1),
    _Flags_Type()
)
flags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flags.setStatus("mandatory")


class _AlertType_Type(Integer32):
    """Custom type alertType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("pend", 17),
          ("perf", 3),
          ("perm", 1),
          ("temp", 2),
          ("unkn", 18))
    )


_AlertType_Type.__name__ = "Integer32"
_AlertType_Object = MibScalar
alertType = _AlertType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 11, 2),
    _AlertType_Type()
)
alertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertType.setStatus("mandatory")


class _AlertDescriptionCode_Type(Integer32):
    """Custom type alertDescriptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlertDescriptionCode_Type.__name__ = "Integer32"
_AlertDescriptionCode_Object = MibScalar
alertDescriptionCode = _AlertDescriptionCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 11, 3),
    _AlertDescriptionCode_Type()
)
alertDescriptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertDescriptionCode.setStatus("mandatory")
_Probable_Causes_ObjectIdentity = ObjectIdentity
probable_Causes = _Probable_Causes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 12)
)
_ProbableCausesTable_Object = MibTable
probableCausesTable = _ProbableCausesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 12, 1)
)
if mibBuilder.loadTexts:
    probableCausesTable.setStatus("mandatory")
_ProbableCausesEntry_Object = MibTableRow
probableCausesEntry = _ProbableCausesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    probableCausesEntry.setStatus("mandatory")
_ProbableCause_Type = Integer32
_ProbableCause_Object = MibTableColumn
probableCause = _ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 12, 1, 1, 1),
    _ProbableCause_Type()
)
probableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probableCause.setStatus("mandatory")
_User_Causes_ObjectIdentity = ObjectIdentity
user_Causes = _User_Causes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13)
)
_UserCausesTable_Object = MibTable
userCausesTable = _UserCausesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 1)
)
if mibBuilder.loadTexts:
    userCausesTable.setStatus("optional")
_UserCausesEntry_Object = MibTableRow
userCausesEntry = _UserCausesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    userCausesEntry.setStatus("optional")


class _UserCause_Type(Integer32):
    """Custom type userCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UserCause_Type.__name__ = "Integer32"
_UserCause_Object = MibTableColumn
userCause = _UserCause_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 1, 1, 1),
    _UserCause_Type()
)
userCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userCause.setStatus("optional")
_RecommendedActionsUCTable_Object = MibTable
recommendedActionsUCTable = _RecommendedActionsUCTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 2)
)
if mibBuilder.loadTexts:
    recommendedActionsUCTable.setStatus("optional")
_RecommendedActionsUCEntry_Object = MibTableRow
recommendedActionsUCEntry = _RecommendedActionsUCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    recommendedActionsUCEntry.setStatus("optional")


class _RecommendedActionUC_Type(Integer32):
    """Custom type recommendedActionUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RecommendedActionUC_Type.__name__ = "Integer32"
_RecommendedActionUC_Object = MibTableColumn
recommendedActionUC = _RecommendedActionUC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 2, 1, 1),
    _RecommendedActionUC_Type()
)
recommendedActionUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recommendedActionUC.setStatus("optional")
_DetailedDataUCTable_Object = MibTable
detailedDataUCTable = _DetailedDataUCTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 3)
)
if mibBuilder.loadTexts:
    detailedDataUCTable.setStatus("optional")
_DetailedDataUCEntry_Object = MibTableRow
detailedDataUCEntry = _DetailedDataUCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    detailedDataUCEntry.setStatus("optional")


class _ProductIDCodeUC_Type(Integer32):
    """Custom type productIDCodeUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              41,
              42,
              153,
              154)
        )
    )
    namedValues = NamedValues(
        *(("displayFirstHW", 41),
          ("displayFirstSW", 153),
          ("displayNone", 0),
          ("displaySecondHW", 42),
          ("displaySecondSW", 154))
    )


_ProductIDCodeUC_Type.__name__ = "Integer32"
_ProductIDCodeUC_Object = MibTableColumn
productIDCodeUC = _ProductIDCodeUC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 3, 1, 1),
    _ProductIDCodeUC_Type()
)
productIDCodeUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDCodeUC.setStatus("optional")


class _DataIDCodeUC_Type(Integer32):
    """Custom type dataIDCodeUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DataIDCodeUC_Type.__name__ = "Integer32"
_DataIDCodeUC_Object = MibTableColumn
dataIDCodeUC = _DataIDCodeUC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 3, 1, 2),
    _DataIDCodeUC_Type()
)
dataIDCodeUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataIDCodeUC.setStatus("optional")


class _DataEncodingUC_Type(Integer32):
    """Custom type dataEncodingUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 17),
          ("binary", 1),
          ("hex", 0))
    )


_DataEncodingUC_Type.__name__ = "Integer32"
_DataEncodingUC_Object = MibTableColumn
dataEncodingUC = _DataEncodingUC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 3, 1, 3),
    _DataEncodingUC_Type()
)
dataEncodingUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEncodingUC.setStatus("optional")


class _DataUC_Type(OctetString):
    """Custom type dataUC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_DataUC_Type.__name__ = "OctetString"
_DataUC_Object = MibTableColumn
dataUC = _DataUC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 3, 1, 4),
    _DataUC_Type()
)
dataUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataUC.setStatus("optional")
_ProductSetIDIndexUCTable_Object = MibTable
productSetIDIndexUCTable = _ProductSetIDIndexUCTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 4)
)
if mibBuilder.loadTexts:
    productSetIDIndexUCTable.setStatus("optional")
_ProductSetIDIndexUCEntry_Object = MibTableRow
productSetIDIndexUCEntry = _ProductSetIDIndexUCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 4, 1)
)
if mibBuilder.loadTexts:
    productSetIDIndexUCEntry.setStatus("optional")


class _ProductSetIDIndexUC_Type(Integer32):
    """Custom type productSetIDIndexUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(41,
              42,
              153,
              154)
        )
    )
    namedValues = NamedValues(
        *(("displayFirstHW", 41),
          ("displayFirstSW", 153),
          ("displaySecondHW", 42),
          ("displaySecondSW", 154))
    )


_ProductSetIDIndexUC_Type.__name__ = "Integer32"
_ProductSetIDIndexUC_Object = MibTableColumn
productSetIDIndexUC = _ProductSetIDIndexUC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 13, 4, 1, 1),
    _ProductSetIDIndexUC_Type()
)
productSetIDIndexUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSetIDIndexUC.setStatus("optional")
_Install_Causes_ObjectIdentity = ObjectIdentity
install_Causes = _Install_Causes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14)
)
_InstallCausesTable_Object = MibTable
installCausesTable = _InstallCausesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 1)
)
if mibBuilder.loadTexts:
    installCausesTable.setStatus("optional")
_InstallCausesEntry_Object = MibTableRow
installCausesEntry = _InstallCausesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    installCausesEntry.setStatus("optional")


class _InstallCause_Type(Integer32):
    """Custom type installCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InstallCause_Type.__name__ = "Integer32"
_InstallCause_Object = MibTableColumn
installCause = _InstallCause_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 1, 1, 1),
    _InstallCause_Type()
)
installCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installCause.setStatus("optional")
_RecommendedActionsICTable_Object = MibTable
recommendedActionsICTable = _RecommendedActionsICTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 2)
)
if mibBuilder.loadTexts:
    recommendedActionsICTable.setStatus("optional")
_RecommendedActionsICEntry_Object = MibTableRow
recommendedActionsICEntry = _RecommendedActionsICEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    recommendedActionsICEntry.setStatus("optional")


class _RecommendedActionIC_Type(Integer32):
    """Custom type recommendedActionIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RecommendedActionIC_Type.__name__ = "Integer32"
_RecommendedActionIC_Object = MibTableColumn
recommendedActionIC = _RecommendedActionIC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 2, 1, 1),
    _RecommendedActionIC_Type()
)
recommendedActionIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recommendedActionIC.setStatus("optional")
_DetailedDataICTable_Object = MibTable
detailedDataICTable = _DetailedDataICTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 3)
)
if mibBuilder.loadTexts:
    detailedDataICTable.setStatus("optional")
_DetailedDataICEntry_Object = MibTableRow
detailedDataICEntry = _DetailedDataICEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    detailedDataICEntry.setStatus("optional")


class _ProductIDCodeIC_Type(Integer32):
    """Custom type productIDCodeIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              41,
              42,
              153,
              154)
        )
    )
    namedValues = NamedValues(
        *(("displayFirstHW", 41),
          ("displayFirstSW", 153),
          ("displayNone", 0),
          ("displaySecondHW", 42),
          ("displaySecondSW", 154))
    )


_ProductIDCodeIC_Type.__name__ = "Integer32"
_ProductIDCodeIC_Object = MibTableColumn
productIDCodeIC = _ProductIDCodeIC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 3, 1, 1),
    _ProductIDCodeIC_Type()
)
productIDCodeIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDCodeIC.setStatus("optional")


class _DataIDCodeIC_Type(Integer32):
    """Custom type dataIDCodeIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DataIDCodeIC_Type.__name__ = "Integer32"
_DataIDCodeIC_Object = MibTableColumn
dataIDCodeIC = _DataIDCodeIC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 3, 1, 2),
    _DataIDCodeIC_Type()
)
dataIDCodeIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataIDCodeIC.setStatus("optional")


class _DataEncodingIC_Type(Integer32):
    """Custom type dataEncodingIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 17),
          ("binary", 1),
          ("hex", 0))
    )


_DataEncodingIC_Type.__name__ = "Integer32"
_DataEncodingIC_Object = MibTableColumn
dataEncodingIC = _DataEncodingIC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 3, 1, 3),
    _DataEncodingIC_Type()
)
dataEncodingIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEncodingIC.setStatus("optional")


class _DataIC_Type(OctetString):
    """Custom type dataIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_DataIC_Type.__name__ = "OctetString"
_DataIC_Object = MibTableColumn
dataIC = _DataIC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 3, 1, 4),
    _DataIC_Type()
)
dataIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataIC.setStatus("optional")
_ProductSetIDIndexICTable_Object = MibTable
productSetIDIndexICTable = _ProductSetIDIndexICTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 4)
)
if mibBuilder.loadTexts:
    productSetIDIndexICTable.setStatus("optional")
_ProductSetIDIndexICEntry_Object = MibTableRow
productSetIDIndexICEntry = _ProductSetIDIndexICEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 4, 1)
)
if mibBuilder.loadTexts:
    productSetIDIndexICEntry.setStatus("optional")


class _ProductSetIDIndexIC_Type(Integer32):
    """Custom type productSetIDIndexIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(41,
              42,
              153,
              154)
        )
    )
    namedValues = NamedValues(
        *(("displayFirstHW", 41),
          ("displayFirstSW", 153),
          ("displaySecondHW", 42),
          ("displaySecondSW", 154))
    )


_ProductSetIDIndexIC_Type.__name__ = "Integer32"
_ProductSetIDIndexIC_Object = MibTableColumn
productSetIDIndexIC = _ProductSetIDIndexIC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 14, 4, 1, 1),
    _ProductSetIDIndexIC_Type()
)
productSetIDIndexIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSetIDIndexIC.setStatus("optional")
_Failure_Causes_ObjectIdentity = ObjectIdentity
failure_Causes = _Failure_Causes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15)
)
_FailureCausesTable_Object = MibTable
failureCausesTable = _FailureCausesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 1)
)
if mibBuilder.loadTexts:
    failureCausesTable.setStatus("optional")
_FailureCausesEntry_Object = MibTableRow
failureCausesEntry = _FailureCausesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    failureCausesEntry.setStatus("optional")


class _FailureCause_Type(Integer32):
    """Custom type failureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FailureCause_Type.__name__ = "Integer32"
_FailureCause_Object = MibTableColumn
failureCause = _FailureCause_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 1, 1, 1),
    _FailureCause_Type()
)
failureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failureCause.setStatus("optional")
_RecommendedActionsFCTable_Object = MibTable
recommendedActionsFCTable = _RecommendedActionsFCTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 2)
)
if mibBuilder.loadTexts:
    recommendedActionsFCTable.setStatus("optional")
_RecommendedActionsFCEntry_Object = MibTableRow
recommendedActionsFCEntry = _RecommendedActionsFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    recommendedActionsFCEntry.setStatus("optional")


class _RecommendedActionFC_Type(Integer32):
    """Custom type recommendedActionFC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RecommendedActionFC_Type.__name__ = "Integer32"
_RecommendedActionFC_Object = MibTableColumn
recommendedActionFC = _RecommendedActionFC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 2, 1, 1),
    _RecommendedActionFC_Type()
)
recommendedActionFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recommendedActionFC.setStatus("optional")
_DetailedDataFCTable_Object = MibTable
detailedDataFCTable = _DetailedDataFCTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 3)
)
if mibBuilder.loadTexts:
    detailedDataFCTable.setStatus("optional")
_DetailedDataFCEntry_Object = MibTableRow
detailedDataFCEntry = _DetailedDataFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    detailedDataFCEntry.setStatus("optional")


class _ProductIDCodeFC_Type(Integer32):
    """Custom type productIDCodeFC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              41,
              42,
              153,
              154)
        )
    )
    namedValues = NamedValues(
        *(("displayFirstHW", 41),
          ("displayFirstSW", 153),
          ("displayNone", 0),
          ("displaySecondHW", 42),
          ("displaySecondSW", 154))
    )


_ProductIDCodeFC_Type.__name__ = "Integer32"
_ProductIDCodeFC_Object = MibTableColumn
productIDCodeFC = _ProductIDCodeFC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 3, 1, 1),
    _ProductIDCodeFC_Type()
)
productIDCodeFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDCodeFC.setStatus("optional")


class _DataIDCodeFC_Type(Integer32):
    """Custom type dataIDCodeFC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DataIDCodeFC_Type.__name__ = "Integer32"
_DataIDCodeFC_Object = MibTableColumn
dataIDCodeFC = _DataIDCodeFC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 3, 1, 2),
    _DataIDCodeFC_Type()
)
dataIDCodeFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataIDCodeFC.setStatus("optional")


class _DataEncodingFC_Type(Integer32):
    """Custom type dataEncodingFC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 17),
          ("binary", 1),
          ("hex", 0))
    )


_DataEncodingFC_Type.__name__ = "Integer32"
_DataEncodingFC_Object = MibTableColumn
dataEncodingFC = _DataEncodingFC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 3, 1, 3),
    _DataEncodingFC_Type()
)
dataEncodingFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEncodingFC.setStatus("optional")


class _DataFC_Type(OctetString):
    """Custom type dataFC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_DataFC_Type.__name__ = "OctetString"
_DataFC_Object = MibTableColumn
dataFC = _DataFC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 3, 1, 4),
    _DataFC_Type()
)
dataFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataFC.setStatus("optional")
_ProductSetIDIndexFCTable_Object = MibTable
productSetIDIndexFCTable = _ProductSetIDIndexFCTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 4)
)
if mibBuilder.loadTexts:
    productSetIDIndexFCTable.setStatus("optional")
_ProductSetIDIndexFCEntry_Object = MibTableRow
productSetIDIndexFCEntry = _ProductSetIDIndexFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 4, 1)
)
if mibBuilder.loadTexts:
    productSetIDIndexFCEntry.setStatus("optional")


class _ProductSetIDIndexFC_Type(Integer32):
    """Custom type productSetIDIndexFC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(41,
              42,
              153,
              154)
        )
    )
    namedValues = NamedValues(
        *(("displayFirstHW", 41),
          ("displayFirstSW", 153),
          ("displaySecondHW", 42),
          ("displaySecondSW", 154))
    )


_ProductSetIDIndexFC_Type.__name__ = "Integer32"
_ProductSetIDIndexFC_Object = MibTableColumn
productSetIDIndexFC = _ProductSetIDIndexFC_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 15, 4, 1, 1),
    _ProductSetIDIndexFC_Type()
)
productSetIDIndexFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSetIDIndexFC.setStatus("optional")
_Detailed_Data_SV_ObjectIdentity = ObjectIdentity
detailed_Data_SV = _Detailed_Data_SV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 17)
)
_DetailedDataDDTable_Object = MibTable
detailedDataDDTable = _DetailedDataDDTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 17, 1)
)
if mibBuilder.loadTexts:
    detailedDataDDTable.setStatus("optional")
_DetailedDataDDEntry_Object = MibTableRow
detailedDataDDEntry = _DetailedDataDDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 17, 1, 1)
)
if mibBuilder.loadTexts:
    detailedDataDDEntry.setStatus("optional")


class _ProductIDCodeDD_Type(Integer32):
    """Custom type productIDCodeDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              41,
              42,
              153,
              154)
        )
    )
    namedValues = NamedValues(
        *(("displayFirstHW", 41),
          ("displayFirstSW", 153),
          ("displayNone", 0),
          ("displaySecondHW", 42),
          ("displaySecondSW", 154))
    )


_ProductIDCodeDD_Type.__name__ = "Integer32"
_ProductIDCodeDD_Object = MibTableColumn
productIDCodeDD = _ProductIDCodeDD_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 17, 1, 1, 1),
    _ProductIDCodeDD_Type()
)
productIDCodeDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDCodeDD.setStatus("optional")


class _DataIDCodeDD_Type(Integer32):
    """Custom type dataIDCodeDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DataIDCodeDD_Type.__name__ = "Integer32"
_DataIDCodeDD_Object = MibTableColumn
dataIDCodeDD = _DataIDCodeDD_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 17, 1, 1, 2),
    _DataIDCodeDD_Type()
)
dataIDCodeDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataIDCodeDD.setStatus("optional")


class _DataEncodingDD_Type(Integer32):
    """Custom type dataEncodingDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 17),
          ("binary", 1),
          ("hex", 0))
    )


_DataEncodingDD_Type.__name__ = "Integer32"
_DataEncodingDD_Object = MibTableColumn
dataEncodingDD = _DataEncodingDD_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 17, 1, 1, 3),
    _DataEncodingDD_Type()
)
dataEncodingDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEncodingDD.setStatus("optional")


class _DataDD_Type(OctetString):
    """Custom type dataDD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_DataDD_Type.__name__ = "OctetString"
_DataDD_Object = MibTableColumn
dataDD = _DataDD_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 1, 17, 1, 1, 4),
    _DataDD_Type()
)
dataDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataDD.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IbmFaultMgmt-MIB",
    **{"ibm": ibm,
       "ibmArchitecture": ibmArchitecture,
       "alert": alert,
       "product-Set-ID": product_Set_ID,
       "hwProductInstallSpecificInfoTable": hwProductInstallSpecificInfoTable,
       "hwProductEntry": hwProductEntry,
       "productClassificationHW": productClassificationHW,
       "formatType": formatType,
       "machineType": machineType,
       "modelNum": modelNum,
       "plantOfManufacture": plantOfManufacture,
       "seqNum": seqNum,
       "microcodeECLevel": microcodeECLevel,
       "hardwareProdCommonName": hardwareProdCommonName,
       "vendorIDhw": vendorIDhw,
       "swProductInstallSpecificInfoTable": swProductInstallSpecificInfoTable,
       "swProductEntry": swProductEntry,
       "productClassificationSW": productClassificationSW,
       "commonVerID": commonVerID,
       "commonRelID": commonRelID,
       "commonModID": commonModID,
       "softwareProdCommonName": softwareProdCommonName,
       "softwareProdProgNmbr": softwareProdProgNmbr,
       "vendorIDsw": vendorIDsw,
       "supporting-Data-Correl": supporting_Data_Correl,
       "detailedDataSDTable": detailedDataSDTable,
       "detailedDataSDEntry": detailedDataSDEntry,
       "productIDCodeSD": productIDCodeSD,
       "dataIDCodeSD": dataIDCodeSD,
       "dataEncodingSD": dataEncodingSD,
       "dataSD": dataSD,
       "generic-Alert-Data": generic_Alert_Data,
       "flags": flags,
       "alertType": alertType,
       "alertDescriptionCode": alertDescriptionCode,
       "probable-Causes": probable_Causes,
       "probableCausesTable": probableCausesTable,
       "probableCausesEntry": probableCausesEntry,
       "probableCause": probableCause,
       "user-Causes": user_Causes,
       "userCausesTable": userCausesTable,
       "userCausesEntry": userCausesEntry,
       "userCause": userCause,
       "recommendedActionsUCTable": recommendedActionsUCTable,
       "recommendedActionsUCEntry": recommendedActionsUCEntry,
       "recommendedActionUC": recommendedActionUC,
       "detailedDataUCTable": detailedDataUCTable,
       "detailedDataUCEntry": detailedDataUCEntry,
       "productIDCodeUC": productIDCodeUC,
       "dataIDCodeUC": dataIDCodeUC,
       "dataEncodingUC": dataEncodingUC,
       "dataUC": dataUC,
       "productSetIDIndexUCTable": productSetIDIndexUCTable,
       "productSetIDIndexUCEntry": productSetIDIndexUCEntry,
       "productSetIDIndexUC": productSetIDIndexUC,
       "install-Causes": install_Causes,
       "installCausesTable": installCausesTable,
       "installCausesEntry": installCausesEntry,
       "installCause": installCause,
       "recommendedActionsICTable": recommendedActionsICTable,
       "recommendedActionsICEntry": recommendedActionsICEntry,
       "recommendedActionIC": recommendedActionIC,
       "detailedDataICTable": detailedDataICTable,
       "detailedDataICEntry": detailedDataICEntry,
       "productIDCodeIC": productIDCodeIC,
       "dataIDCodeIC": dataIDCodeIC,
       "dataEncodingIC": dataEncodingIC,
       "dataIC": dataIC,
       "productSetIDIndexICTable": productSetIDIndexICTable,
       "productSetIDIndexICEntry": productSetIDIndexICEntry,
       "productSetIDIndexIC": productSetIDIndexIC,
       "failure-Causes": failure_Causes,
       "failureCausesTable": failureCausesTable,
       "failureCausesEntry": failureCausesEntry,
       "failureCause": failureCause,
       "recommendedActionsFCTable": recommendedActionsFCTable,
       "recommendedActionsFCEntry": recommendedActionsFCEntry,
       "recommendedActionFC": recommendedActionFC,
       "detailedDataFCTable": detailedDataFCTable,
       "detailedDataFCEntry": detailedDataFCEntry,
       "productIDCodeFC": productIDCodeFC,
       "dataIDCodeFC": dataIDCodeFC,
       "dataEncodingFC": dataEncodingFC,
       "dataFC": dataFC,
       "productSetIDIndexFCTable": productSetIDIndexFCTable,
       "productSetIDIndexFCEntry": productSetIDIndexFCEntry,
       "productSetIDIndexFC": productSetIDIndexFC,
       "detailed-Data-SV": detailed_Data_SV,
       "detailedDataDDTable": detailedDataDDTable,
       "detailedDataDDEntry": detailedDataDDEntry,
       "productIDCodeDD": productIDCodeDD,
       "dataIDCodeDD": dataIDCodeDD,
       "dataEncodingDD": dataEncodingDD,
       "dataDD": dataDD}
)
