# SNMP MIB module (Finisher-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Finisher-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:48 2024
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(PresentOnOff,
 PrtCapacityUnitTC,
 PrtInputTypeTC,
 PrtMarkerSuppliesClassTC,
 PrtMarkerSuppliesSupplyUnitTC,
 PrtMarkerSuppliesTypeTC,
 PrtMediaUnitTC,
 PrtSubUnitStatusTC,
 printmib,
 prtMIBConformance) = mibBuilder.importSymbols(
    "Printer-MIB",
    "PresentOnOff",
    "PrtCapacityUnitTC",
    "PrtInputTypeTC",
    "PrtMarkerSuppliesClassTC",
    "PrtMarkerSuppliesSupplyUnitTC",
    "PrtMarkerSuppliesTypeTC",
    "PrtMediaUnitTC",
    "PrtSubUnitStatusTC",
    "printmib",
    "prtMIBConformance")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 experimental,
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
    "experimental",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

finisherMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FinDeviceTypeTC(Integer32, TextualConvention):
    status = "current"
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
        *(("bander", 14),
          ("binder", 5),
          ("dieCutter", 7),
          ("folder", 4),
          ("imprinter", 12),
          ("makeEnvelope", 15),
          ("other", 1),
          ("perforater", 9),
          ("puncher", 8),
          ("separationCutter", 11),
          ("sheetRotator", 17),
          ("slitter", 10),
          ("stacker", 16),
          ("stitcher", 3),
          ("trimmer", 6),
          ("unknown", 2),
          ("wrapper", 13))
    )



class FinAttributeTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              30,
              31,
              40,
              50,
              80,
              81,
              82,
              83,
              100,
              130,
              160,
              161,
              162)
        )
    )
    namedValues = NamedValues(
        *(("bindingType", 50),
          ("deviceModel", 5),
          ("deviceName", 3),
          ("deviceSerialNumber", 7),
          ("deviceVendorName", 4),
          ("deviceVersion", 6),
          ("finAxisOffset", 11),
          ("finHeadLocation", 13),
          ("finJogEdge", 12),
          ("finMediaTypeRestriction", 17),
          ("finNextFinishingOperation", 20),
          ("finNumberOfPositions", 15),
          ("finOperationRestrictions", 14),
          ("finPreviousFinishingOperation", 19),
          ("finPrinterInputTraySupported", 18),
          ("finProcessOffsetUnits", 9),
          ("finReferenceEdge", 10),
          ("foldingType", 40),
          ("maximumSheets", 8),
          ("namedConfiguration", 16),
          ("other", 1),
          ("punchHoleSizeLongDim", 81),
          ("punchHoleSizeShortDim", 82),
          ("punchHoleType", 80),
          ("punchPattern", 83),
          ("slittingType", 100),
          ("stackOffset", 161),
          ("stackOutputType", 160),
          ("stackRotation", 162),
          ("stitchingDirection", 31),
          ("stitchingType", 30),
          ("wrappingType", 130))
    )



class FinEdgeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bottomEdge", 4),
          ("leftEdge", 5),
          ("rightEdge", 6),
          ("topEdge", 3))
    )



class FinStitchingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
        *(("edgeStitch", 9),
          ("other", 1),
          ("saddleStitch", 8),
          ("stapleBottomLeft", 5),
          ("stapleBottomRight", 7),
          ("stapleDual", 10),
          ("stapleTopLeft", 4),
          ("stapleTopRight", 6),
          ("unknown", 2))
    )



class StitchingDirTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bottomUp", 4),
          ("topDown", 3),
          ("unknown", 2))
    )



class StitchingAngleTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 3),
          ("slanted", 5),
          ("unknown", 2),
          ("vertical", 4))
    )



class FinFoldingTypeTC(Integer32, TextualConvention):
    status = "current"
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
        *(("halfFold", 4),
          ("letterFold", 5),
          ("other", 1),
          ("unknown", 2),
          ("zFold", 3))
    )



class FinBindingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
        *(("adhesive", 9),
          ("comb", 10),
          ("other", 1),
          ("padding", 11),
          ("perfect", 7),
          ("plastic", 5),
          ("spiral", 8),
          ("tape", 4),
          ("unknown", 2),
          ("velo", 6))
    )



class FinPunchHoleTypeTC(Integer32, TextualConvention):
    status = "current"
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
        *(("oblong", 4),
          ("other", 1),
          ("rectangular", 6),
          ("round", 3),
          ("square", 5),
          ("star", 7),
          ("unknown", 2))
    )



class FinPunchPatternTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
        *(("fiveHoleUS", 13),
          ("fourHoleDIN", 7),
          ("metric26Hole", 17),
          ("metric30Hole", 18),
          ("mixed7H4S", 15),
          ("nineteenHoleUS", 9),
          ("norweg6Hole", 16),
          ("other", 1),
          ("sevenHoleUS", 14),
          ("swedish4Hole", 11),
          ("threeHoleUS", 5),
          ("twentyTwoHoleUS", 8),
          ("twoHoleDIN", 6),
          ("twoHoleMetric", 10),
          ("twoHoleUSSide", 12),
          ("twoHoleUSTop", 4),
          ("unknown", 2))
    )



class FinSlittingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("slitAndMerge", 5),
          ("slitAndSeparate", 4),
          ("unknown", 2))
    )



class FinWrappingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("paperWrap", 5),
          ("shrinkWrap", 4),
          ("unknown", 2))
    )



class FinStackOutputTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("crissCross", 6),
          ("offset", 5),
          ("other", 1),
          ("straight", 4),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FinMIBGroups_ObjectIdentity = ObjectIdentity
finMIBGroups = _FinMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 2, 4)
)
_FinDevice_ObjectIdentity = ObjectIdentity
finDevice = _FinDevice_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 30)
)
_FinDeviceTable_Object = MibTable
finDeviceTable = _FinDeviceTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1)
)
if mibBuilder.loadTexts:
    finDeviceTable.setStatus("current")
_FinDeviceEntry_Object = MibTableRow
finDeviceEntry = _FinDeviceEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1)
)
finDeviceEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Finisher-MIB", "finDeviceIndex"),
)
if mibBuilder.loadTexts:
    finDeviceEntry.setStatus("current")


class _FinDeviceIndex_Type(Integer32):
    """Custom type finDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FinDeviceIndex_Type.__name__ = "Integer32"
_FinDeviceIndex_Object = MibTableColumn
finDeviceIndex = _FinDeviceIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 1),
    _FinDeviceIndex_Type()
)
finDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    finDeviceIndex.setStatus("current")
_FinDeviceType_Type = FinDeviceTypeTC
_FinDeviceType_Object = MibTableColumn
finDeviceType = _FinDeviceType_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 2),
    _FinDeviceType_Type()
)
finDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finDeviceType.setStatus("current")


class _FinDevicePresentOnOff_Type(PresentOnOff):
    """Custom type finDevicePresentOnOff based on PresentOnOff"""


_FinDevicePresentOnOff_Object = MibTableColumn
finDevicePresentOnOff = _FinDevicePresentOnOff_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 3),
    _FinDevicePresentOnOff_Type()
)
finDevicePresentOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finDevicePresentOnOff.setStatus("current")
_FinDeviceCapacityUnit_Type = PrtCapacityUnitTC
_FinDeviceCapacityUnit_Object = MibTableColumn
finDeviceCapacityUnit = _FinDeviceCapacityUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 4),
    _FinDeviceCapacityUnit_Type()
)
finDeviceCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finDeviceCapacityUnit.setStatus("current")


class _FinDeviceMaxCapacity_Type(Integer32):
    """Custom type finDeviceMaxCapacity based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_FinDeviceMaxCapacity_Type.__name__ = "Integer32"
_FinDeviceMaxCapacity_Object = MibTableColumn
finDeviceMaxCapacity = _FinDeviceMaxCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 5),
    _FinDeviceMaxCapacity_Type()
)
finDeviceMaxCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finDeviceMaxCapacity.setStatus("current")


class _FinDeviceCurrentCapacity_Type(Integer32):
    """Custom type finDeviceCurrentCapacity based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_FinDeviceCurrentCapacity_Type.__name__ = "Integer32"
_FinDeviceCurrentCapacity_Object = MibTableColumn
finDeviceCurrentCapacity = _FinDeviceCurrentCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 6),
    _FinDeviceCurrentCapacity_Type()
)
finDeviceCurrentCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finDeviceCurrentCapacity.setStatus("current")
_FinDeviceAssociatedMediaPaths_Type = OctetString
_FinDeviceAssociatedMediaPaths_Object = MibTableColumn
finDeviceAssociatedMediaPaths = _FinDeviceAssociatedMediaPaths_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 7),
    _FinDeviceAssociatedMediaPaths_Type()
)
finDeviceAssociatedMediaPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finDeviceAssociatedMediaPaths.setStatus("current")
_FinDeviceAssociatedOutputs_Type = OctetString
_FinDeviceAssociatedOutputs_Object = MibTableColumn
finDeviceAssociatedOutputs = _FinDeviceAssociatedOutputs_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 8),
    _FinDeviceAssociatedOutputs_Type()
)
finDeviceAssociatedOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finDeviceAssociatedOutputs.setStatus("current")


class _FinDeviceStatus_Type(PrtSubUnitStatusTC):
    """Custom type finDeviceStatus based on PrtSubUnitStatusTC"""
    defaultValue = 5


_FinDeviceStatus_Object = MibTableColumn
finDeviceStatus = _FinDeviceStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 9),
    _FinDeviceStatus_Type()
)
finDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finDeviceStatus.setStatus("current")


class _FinDeviceDescription_Type(OctetString):
    """Custom type finDeviceDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FinDeviceDescription_Type.__name__ = "OctetString"
_FinDeviceDescription_Object = MibTableColumn
finDeviceDescription = _FinDeviceDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 10),
    _FinDeviceDescription_Type()
)
finDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finDeviceDescription.setStatus("current")
_FinSupply_ObjectIdentity = ObjectIdentity
finSupply = _FinSupply_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 31)
)
_FinSupplyTable_Object = MibTable
finSupplyTable = _FinSupplyTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1)
)
if mibBuilder.loadTexts:
    finSupplyTable.setStatus("current")
_FinSupplyEntry_Object = MibTableRow
finSupplyEntry = _FinSupplyEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1)
)
finSupplyEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Finisher-MIB", "finSupplyIndex"),
)
if mibBuilder.loadTexts:
    finSupplyEntry.setStatus("current")


class _FinSupplyIndex_Type(Integer32):
    """Custom type finSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FinSupplyIndex_Type.__name__ = "Integer32"
_FinSupplyIndex_Object = MibTableColumn
finSupplyIndex = _FinSupplyIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 1),
    _FinSupplyIndex_Type()
)
finSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    finSupplyIndex.setStatus("current")


class _FinSupplyDeviceIndex_Type(Integer32):
    """Custom type finSupplyDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FinSupplyDeviceIndex_Type.__name__ = "Integer32"
_FinSupplyDeviceIndex_Object = MibTableColumn
finSupplyDeviceIndex = _FinSupplyDeviceIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 2),
    _FinSupplyDeviceIndex_Type()
)
finSupplyDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyDeviceIndex.setStatus("current")
_FinSupplyClass_Type = PrtMarkerSuppliesClassTC
_FinSupplyClass_Object = MibTableColumn
finSupplyClass = _FinSupplyClass_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 3),
    _FinSupplyClass_Type()
)
finSupplyClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyClass.setStatus("current")
_FinSupplyType_Type = PrtMarkerSuppliesTypeTC
_FinSupplyType_Object = MibTableColumn
finSupplyType = _FinSupplyType_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 4),
    _FinSupplyType_Type()
)
finSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyType.setStatus("current")


class _FinSupplyDescription_Type(OctetString):
    """Custom type finSupplyDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FinSupplyDescription_Type.__name__ = "OctetString"
_FinSupplyDescription_Object = MibTableColumn
finSupplyDescription = _FinSupplyDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 5),
    _FinSupplyDescription_Type()
)
finSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyDescription.setStatus("current")
_FinSupplyUnit_Type = PrtMarkerSuppliesSupplyUnitTC
_FinSupplyUnit_Object = MibTableColumn
finSupplyUnit = _FinSupplyUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 6),
    _FinSupplyUnit_Type()
)
finSupplyUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyUnit.setStatus("current")


class _FinSupplyMaxCapacity_Type(Integer32):
    """Custom type finSupplyMaxCapacity based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_FinSupplyMaxCapacity_Type.__name__ = "Integer32"
_FinSupplyMaxCapacity_Object = MibTableColumn
finSupplyMaxCapacity = _FinSupplyMaxCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 7),
    _FinSupplyMaxCapacity_Type()
)
finSupplyMaxCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyMaxCapacity.setStatus("current")


class _FinSupplyCurrentLevel_Type(Integer32):
    """Custom type finSupplyCurrentLevel based on Integer32"""
    defaultValue = -2


_FinSupplyCurrentLevel_Object = MibTableColumn
finSupplyCurrentLevel = _FinSupplyCurrentLevel_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 8),
    _FinSupplyCurrentLevel_Type()
)
finSupplyCurrentLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyCurrentLevel.setStatus("current")


class _FinSupplyColorName_Type(OctetString):
    """Custom type finSupplyColorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FinSupplyColorName_Type.__name__ = "OctetString"
_FinSupplyColorName_Object = MibTableColumn
finSupplyColorName = _FinSupplyColorName_Object(
    (1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 9),
    _FinSupplyColorName_Type()
)
finSupplyColorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyColorName.setStatus("current")
_FinSupplyMediaInput_ObjectIdentity = ObjectIdentity
finSupplyMediaInput = _FinSupplyMediaInput_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 32)
)
_FinSupplyMediaInputTable_Object = MibTable
finSupplyMediaInputTable = _FinSupplyMediaInputTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1)
)
if mibBuilder.loadTexts:
    finSupplyMediaInputTable.setStatus("current")
_FinSupplyMediaInputEntry_Object = MibTableRow
finSupplyMediaInputEntry = _FinSupplyMediaInputEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1)
)
finSupplyMediaInputEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Finisher-MIB", "finSupplyMediaInputIndex"),
)
if mibBuilder.loadTexts:
    finSupplyMediaInputEntry.setStatus("current")


class _FinSupplyMediaInputIndex_Type(Integer32):
    """Custom type finSupplyMediaInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FinSupplyMediaInputIndex_Type.__name__ = "Integer32"
_FinSupplyMediaInputIndex_Object = MibTableColumn
finSupplyMediaInputIndex = _FinSupplyMediaInputIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 1),
    _FinSupplyMediaInputIndex_Type()
)
finSupplyMediaInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    finSupplyMediaInputIndex.setStatus("current")


class _FinSupplyMediaInputDeviceIndex_Type(Integer32):
    """Custom type finSupplyMediaInputDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FinSupplyMediaInputDeviceIndex_Type.__name__ = "Integer32"
_FinSupplyMediaInputDeviceIndex_Object = MibTableColumn
finSupplyMediaInputDeviceIndex = _FinSupplyMediaInputDeviceIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 2),
    _FinSupplyMediaInputDeviceIndex_Type()
)
finSupplyMediaInputDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyMediaInputDeviceIndex.setStatus("current")


class _FinSupplyMediaInputSupplyIndex_Type(Integer32):
    """Custom type finSupplyMediaInputSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FinSupplyMediaInputSupplyIndex_Type.__name__ = "Integer32"
_FinSupplyMediaInputSupplyIndex_Object = MibTableColumn
finSupplyMediaInputSupplyIndex = _FinSupplyMediaInputSupplyIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 3),
    _FinSupplyMediaInputSupplyIndex_Type()
)
finSupplyMediaInputSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyMediaInputSupplyIndex.setStatus("current")
_FinSupplyMediaInputType_Type = PrtInputTypeTC
_FinSupplyMediaInputType_Object = MibTableColumn
finSupplyMediaInputType = _FinSupplyMediaInputType_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 4),
    _FinSupplyMediaInputType_Type()
)
finSupplyMediaInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyMediaInputType.setStatus("current")
_FinSupplyMediaInputDimUnit_Type = PrtMediaUnitTC
_FinSupplyMediaInputDimUnit_Object = MibTableColumn
finSupplyMediaInputDimUnit = _FinSupplyMediaInputDimUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 5),
    _FinSupplyMediaInputDimUnit_Type()
)
finSupplyMediaInputDimUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyMediaInputDimUnit.setStatus("current")


class _FinSupplyMediaInputMediaDimFeedDir_Type(Integer32):
    """Custom type finSupplyMediaInputMediaDimFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_FinSupplyMediaInputMediaDimFeedDir_Type.__name__ = "Integer32"
_FinSupplyMediaInputMediaDimFeedDir_Object = MibTableColumn
finSupplyMediaInputMediaDimFeedDir = _FinSupplyMediaInputMediaDimFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 6),
    _FinSupplyMediaInputMediaDimFeedDir_Type()
)
finSupplyMediaInputMediaDimFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyMediaInputMediaDimFeedDir.setStatus("current")


class _FinSupplyMediaInputMediaDimXFeedDir_Type(Integer32):
    """Custom type finSupplyMediaInputMediaDimXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_FinSupplyMediaInputMediaDimXFeedDir_Type.__name__ = "Integer32"
_FinSupplyMediaInputMediaDimXFeedDir_Object = MibTableColumn
finSupplyMediaInputMediaDimXFeedDir = _FinSupplyMediaInputMediaDimXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 7),
    _FinSupplyMediaInputMediaDimXFeedDir_Type()
)
finSupplyMediaInputMediaDimXFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyMediaInputMediaDimXFeedDir.setStatus("current")


class _FinSupplyMediaInputStatus_Type(PrtSubUnitStatusTC):
    """Custom type finSupplyMediaInputStatus based on PrtSubUnitStatusTC"""
    defaultValue = 5


_FinSupplyMediaInputStatus_Object = MibTableColumn
finSupplyMediaInputStatus = _FinSupplyMediaInputStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 8),
    _FinSupplyMediaInputStatus_Type()
)
finSupplyMediaInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyMediaInputStatus.setStatus("current")


class _FinSupplyMediaInputMediaName_Type(OctetString):
    """Custom type finSupplyMediaInputMediaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FinSupplyMediaInputMediaName_Type.__name__ = "OctetString"
_FinSupplyMediaInputMediaName_Object = MibTableColumn
finSupplyMediaInputMediaName = _FinSupplyMediaInputMediaName_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 9),
    _FinSupplyMediaInputMediaName_Type()
)
finSupplyMediaInputMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyMediaInputMediaName.setStatus("current")


class _FinSupplyMediaInputName_Type(OctetString):
    """Custom type finSupplyMediaInputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FinSupplyMediaInputName_Type.__name__ = "OctetString"
_FinSupplyMediaInputName_Object = MibTableColumn
finSupplyMediaInputName = _FinSupplyMediaInputName_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 10),
    _FinSupplyMediaInputName_Type()
)
finSupplyMediaInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyMediaInputName.setStatus("current")


class _FinSupplyMediaInputDescription_Type(OctetString):
    """Custom type finSupplyMediaInputDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FinSupplyMediaInputDescription_Type.__name__ = "OctetString"
_FinSupplyMediaInputDescription_Object = MibTableColumn
finSupplyMediaInputDescription = _FinSupplyMediaInputDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 11),
    _FinSupplyMediaInputDescription_Type()
)
finSupplyMediaInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finSupplyMediaInputDescription.setStatus("current")
_FinSupplyMediaInputSecurity_Type = PresentOnOff
_FinSupplyMediaInputSecurity_Object = MibTableColumn
finSupplyMediaInputSecurity = _FinSupplyMediaInputSecurity_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 12),
    _FinSupplyMediaInputSecurity_Type()
)
finSupplyMediaInputSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyMediaInputSecurity.setStatus("current")
_FinSupplyMediaInputMediaWeight_Type = Integer32
_FinSupplyMediaInputMediaWeight_Object = MibTableColumn
finSupplyMediaInputMediaWeight = _FinSupplyMediaInputMediaWeight_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 13),
    _FinSupplyMediaInputMediaWeight_Type()
)
finSupplyMediaInputMediaWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyMediaInputMediaWeight.setStatus("current")


class _FinSupplyMediaInputMediaThickness_Type(Integer32):
    """Custom type finSupplyMediaInputMediaThickness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_FinSupplyMediaInputMediaThickness_Type.__name__ = "Integer32"
_FinSupplyMediaInputMediaThickness_Object = MibTableColumn
finSupplyMediaInputMediaThickness = _FinSupplyMediaInputMediaThickness_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 14),
    _FinSupplyMediaInputMediaThickness_Type()
)
finSupplyMediaInputMediaThickness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyMediaInputMediaThickness.setStatus("current")


class _FinSupplyMediaInputMediaType_Type(OctetString):
    """Custom type finSupplyMediaInputMediaType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FinSupplyMediaInputMediaType_Type.__name__ = "OctetString"
_FinSupplyMediaInputMediaType_Object = MibTableColumn
finSupplyMediaInputMediaType = _FinSupplyMediaInputMediaType_Object(
    (1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 15),
    _FinSupplyMediaInputMediaType_Type()
)
finSupplyMediaInputMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finSupplyMediaInputMediaType.setStatus("current")
_FinDeviceAttribute_ObjectIdentity = ObjectIdentity
finDeviceAttribute = _FinDeviceAttribute_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 33)
)
_FinDeviceAttributeTable_Object = MibTable
finDeviceAttributeTable = _FinDeviceAttributeTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 33, 1)
)
if mibBuilder.loadTexts:
    finDeviceAttributeTable.setStatus("current")
_FinDeviceAttributeEntry_Object = MibTableRow
finDeviceAttributeEntry = _FinDeviceAttributeEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 33, 1, 1)
)
finDeviceAttributeEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Finisher-MIB", "finDeviceIndex"),
    (0, "Finisher-MIB", "finDeviceAttributeTypeIndex"),
    (0, "Finisher-MIB", "finDeviceAttributeInstanceIndex"),
)
if mibBuilder.loadTexts:
    finDeviceAttributeEntry.setStatus("current")
_FinDeviceAttributeTypeIndex_Type = FinAttributeTypeTC
_FinDeviceAttributeTypeIndex_Object = MibTableColumn
finDeviceAttributeTypeIndex = _FinDeviceAttributeTypeIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 1),
    _FinDeviceAttributeTypeIndex_Type()
)
finDeviceAttributeTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    finDeviceAttributeTypeIndex.setStatus("current")


class _FinDeviceAttributeInstanceIndex_Type(Integer32):
    """Custom type finDeviceAttributeInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FinDeviceAttributeInstanceIndex_Type.__name__ = "Integer32"
_FinDeviceAttributeInstanceIndex_Object = MibTableColumn
finDeviceAttributeInstanceIndex = _FinDeviceAttributeInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 2),
    _FinDeviceAttributeInstanceIndex_Type()
)
finDeviceAttributeInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    finDeviceAttributeInstanceIndex.setStatus("current")


class _FinDeviceAttributeValueAsInteger_Type(Integer32):
    """Custom type finDeviceAttributeValueAsInteger based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_FinDeviceAttributeValueAsInteger_Type.__name__ = "Integer32"
_FinDeviceAttributeValueAsInteger_Object = MibTableColumn
finDeviceAttributeValueAsInteger = _FinDeviceAttributeValueAsInteger_Object(
    (1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 3),
    _FinDeviceAttributeValueAsInteger_Type()
)
finDeviceAttributeValueAsInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finDeviceAttributeValueAsInteger.setStatus("current")


class _FinDeviceAttributeValueAsOctets_Type(OctetString):
    """Custom type finDeviceAttributeValueAsOctets based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FinDeviceAttributeValueAsOctets_Type.__name__ = "OctetString"
_FinDeviceAttributeValueAsOctets_Object = MibTableColumn
finDeviceAttributeValueAsOctets = _FinDeviceAttributeValueAsOctets_Object(
    (1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 4),
    _FinDeviceAttributeValueAsOctets_Type()
)
finDeviceAttributeValueAsOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    finDeviceAttributeValueAsOctets.setStatus("current")

# Managed Objects groups

finDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 4, 1)
)
finDeviceGroup.setObjects(
      *(("Finisher-MIB", "finDeviceType"),
        ("Finisher-MIB", "finDevicePresentOnOff"),
        ("Finisher-MIB", "finDeviceCapacityUnit"),
        ("Finisher-MIB", "finDeviceMaxCapacity"),
        ("Finisher-MIB", "finDeviceCurrentCapacity"),
        ("Finisher-MIB", "finDeviceAssociatedMediaPaths"),
        ("Finisher-MIB", "finDeviceAssociatedOutputs"),
        ("Finisher-MIB", "finDeviceStatus"),
        ("Finisher-MIB", "finDeviceDescription"))
)
if mibBuilder.loadTexts:
    finDeviceGroup.setStatus("current")

finSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 4, 2)
)
finSupplyGroup.setObjects(
      *(("Finisher-MIB", "finSupplyDeviceIndex"),
        ("Finisher-MIB", "finSupplyClass"),
        ("Finisher-MIB", "finSupplyType"),
        ("Finisher-MIB", "finSupplyDescription"),
        ("Finisher-MIB", "finSupplyUnit"),
        ("Finisher-MIB", "finSupplyMaxCapacity"),
        ("Finisher-MIB", "finSupplyCurrentLevel"),
        ("Finisher-MIB", "finSupplyColorName"))
)
if mibBuilder.loadTexts:
    finSupplyGroup.setStatus("current")

finSupplyMediaInputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 4, 3)
)
finSupplyMediaInputGroup.setObjects(
      *(("Finisher-MIB", "finSupplyMediaInputDeviceIndex"),
        ("Finisher-MIB", "finSupplyMediaInputSupplyIndex"),
        ("Finisher-MIB", "finSupplyMediaInputType"),
        ("Finisher-MIB", "finSupplyMediaInputDimUnit"),
        ("Finisher-MIB", "finSupplyMediaInputMediaDimFeedDir"),
        ("Finisher-MIB", "finSupplyMediaInputMediaDimXFeedDir"),
        ("Finisher-MIB", "finSupplyMediaInputStatus"),
        ("Finisher-MIB", "finSupplyMediaInputMediaName"),
        ("Finisher-MIB", "finSupplyMediaInputName"),
        ("Finisher-MIB", "finSupplyMediaInputDescription"),
        ("Finisher-MIB", "finSupplyMediaInputSecurity"),
        ("Finisher-MIB", "finSupplyMediaInputMediaWeight"),
        ("Finisher-MIB", "finSupplyMediaInputMediaThickness"),
        ("Finisher-MIB", "finSupplyMediaInputMediaType"))
)
if mibBuilder.loadTexts:
    finSupplyMediaInputGroup.setStatus("current")

finDeviceAttributeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 4, 4)
)
finDeviceAttributeGroup.setObjects(
      *(("Finisher-MIB", "finDeviceAttributeValueAsInteger"),
        ("Finisher-MIB", "finDeviceAttributeValueAsOctets"))
)
if mibBuilder.loadTexts:
    finDeviceAttributeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

finMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 43, 2, 3)
)
if mibBuilder.loadTexts:
    finMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Finisher-MIB",
    **{"FinDeviceTypeTC": FinDeviceTypeTC,
       "FinAttributeTypeTC": FinAttributeTypeTC,
       "FinEdgeTC": FinEdgeTC,
       "FinStitchingTypeTC": FinStitchingTypeTC,
       "StitchingDirTypeTC": StitchingDirTypeTC,
       "StitchingAngleTypeTC": StitchingAngleTypeTC,
       "FinFoldingTypeTC": FinFoldingTypeTC,
       "FinBindingTypeTC": FinBindingTypeTC,
       "FinPunchHoleTypeTC": FinPunchHoleTypeTC,
       "FinPunchPatternTC": FinPunchPatternTC,
       "FinSlittingTypeTC": FinSlittingTypeTC,
       "FinWrappingTypeTC": FinWrappingTypeTC,
       "FinStackOutputTypeTC": FinStackOutputTypeTC,
       "finMIBCompliance": finMIBCompliance,
       "finMIBGroups": finMIBGroups,
       "finDeviceGroup": finDeviceGroup,
       "finSupplyGroup": finSupplyGroup,
       "finSupplyMediaInputGroup": finSupplyMediaInputGroup,
       "finDeviceAttributeGroup": finDeviceAttributeGroup,
       "finDevice": finDevice,
       "finDeviceTable": finDeviceTable,
       "finDeviceEntry": finDeviceEntry,
       "finDeviceIndex": finDeviceIndex,
       "finDeviceType": finDeviceType,
       "finDevicePresentOnOff": finDevicePresentOnOff,
       "finDeviceCapacityUnit": finDeviceCapacityUnit,
       "finDeviceMaxCapacity": finDeviceMaxCapacity,
       "finDeviceCurrentCapacity": finDeviceCurrentCapacity,
       "finDeviceAssociatedMediaPaths": finDeviceAssociatedMediaPaths,
       "finDeviceAssociatedOutputs": finDeviceAssociatedOutputs,
       "finDeviceStatus": finDeviceStatus,
       "finDeviceDescription": finDeviceDescription,
       "finSupply": finSupply,
       "finSupplyTable": finSupplyTable,
       "finSupplyEntry": finSupplyEntry,
       "finSupplyIndex": finSupplyIndex,
       "finSupplyDeviceIndex": finSupplyDeviceIndex,
       "finSupplyClass": finSupplyClass,
       "finSupplyType": finSupplyType,
       "finSupplyDescription": finSupplyDescription,
       "finSupplyUnit": finSupplyUnit,
       "finSupplyMaxCapacity": finSupplyMaxCapacity,
       "finSupplyCurrentLevel": finSupplyCurrentLevel,
       "finSupplyColorName": finSupplyColorName,
       "finSupplyMediaInput": finSupplyMediaInput,
       "finSupplyMediaInputTable": finSupplyMediaInputTable,
       "finSupplyMediaInputEntry": finSupplyMediaInputEntry,
       "finSupplyMediaInputIndex": finSupplyMediaInputIndex,
       "finSupplyMediaInputDeviceIndex": finSupplyMediaInputDeviceIndex,
       "finSupplyMediaInputSupplyIndex": finSupplyMediaInputSupplyIndex,
       "finSupplyMediaInputType": finSupplyMediaInputType,
       "finSupplyMediaInputDimUnit": finSupplyMediaInputDimUnit,
       "finSupplyMediaInputMediaDimFeedDir": finSupplyMediaInputMediaDimFeedDir,
       "finSupplyMediaInputMediaDimXFeedDir": finSupplyMediaInputMediaDimXFeedDir,
       "finSupplyMediaInputStatus": finSupplyMediaInputStatus,
       "finSupplyMediaInputMediaName": finSupplyMediaInputMediaName,
       "finSupplyMediaInputName": finSupplyMediaInputName,
       "finSupplyMediaInputDescription": finSupplyMediaInputDescription,
       "finSupplyMediaInputSecurity": finSupplyMediaInputSecurity,
       "finSupplyMediaInputMediaWeight": finSupplyMediaInputMediaWeight,
       "finSupplyMediaInputMediaThickness": finSupplyMediaInputMediaThickness,
       "finSupplyMediaInputMediaType": finSupplyMediaInputMediaType,
       "finDeviceAttribute": finDeviceAttribute,
       "finDeviceAttributeTable": finDeviceAttributeTable,
       "finDeviceAttributeEntry": finDeviceAttributeEntry,
       "finDeviceAttributeTypeIndex": finDeviceAttributeTypeIndex,
       "finDeviceAttributeInstanceIndex": finDeviceAttributeInstanceIndex,
       "finDeviceAttributeValueAsInteger": finDeviceAttributeValueAsInteger,
       "finDeviceAttributeValueAsOctets": finDeviceAttributeValueAsOctets,
       "finisherMIB": finisherMIB}
)
