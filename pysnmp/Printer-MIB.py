# SNMP MIB module (Printer-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Printer-MIB
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

(hrDeviceIndex,
 hrStorageIndex) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex",
    "hrStorageIndex")

(IANACharset,) = mibBuilder.importSymbols(
    "IANA-CHARSET-MIB",
    "IANACharset")

(PrtAlertCodeTC,
 PrtAlertGroupTC,
 PrtAlertTrainingLevelTC,
 PrtChannelTypeTC,
 PrtConsoleColorTC,
 PrtConsoleDisableTC,
 PrtCoverStatusTC,
 PrtGeneralResetTC,
 PrtInputTypeTC,
 PrtInterpreterLangFamilyTC,
 PrtMarkerMarkTechTC,
 PrtMarkerSuppliesTypeTC,
 PrtMediaPathTypeTC,
 PrtOutputTypeTC) = mibBuilder.importSymbols(
    "IANA-PRINTER-MIB",
    "PrtAlertCodeTC",
    "PrtAlertGroupTC",
    "PrtAlertTrainingLevelTC",
    "PrtChannelTypeTC",
    "PrtConsoleColorTC",
    "PrtConsoleDisableTC",
    "PrtCoverStatusTC",
    "PrtGeneralResetTC",
    "PrtInputTypeTC",
    "PrtInterpreterLangFamilyTC",
    "PrtMarkerMarkTechTC",
    "PrtMarkerSuppliesTypeTC",
    "PrtMediaPathTypeTC",
    "PrtOutputTypeTC")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

printmib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 43)
)
printmib.setRevisions(
        ("2004-06-02 00:00",
         "1994-11-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PrtMediaUnitTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("micrometers", 4),
          ("tenThousandthsOfInches", 3))
    )



class MediaUnit(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("micrometers", 4),
          ("tenThousandthsOfInches", 3))
    )



class PrtCapacityUnitTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("feet", 16),
          ("items", 18),
          ("meters", 17),
          ("micrometers", 4),
          ("other", 1),
          ("percent", 19),
          ("sheets", 8),
          ("tenThousandthsOfInches", 3),
          ("unknown", 2))
    )



class CapacityUnit(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              8,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("feet", 16),
          ("meters", 17),
          ("micrometers", 4),
          ("sheets", 8),
          ("tenThousandthsOfInches", 3))
    )



class PrtPrintOrientationTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("landscape", 4),
          ("other", 1),
          ("portrait", 3))
    )



class PrtSubUnitStatusTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )



class SubUnitStatus(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )



class PresentOnOff(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 5),
          ("off", 4),
          ("on", 3),
          ("other", 1))
    )



class PrtLocalizedDescriptionStringTC(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class PrtConsoleDescriptionStringTC(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CodedCharSet(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("other", 1)
    )



class PrtChannelStateTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noDataAccepted", 4),
          ("other", 1),
          ("printDataAccepted", 3))
    )



class PrtOutputStackingOrderTC(Integer32, TextualConvention):
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
        *(("firstToLast", 3),
          ("lastToFirst", 4),
          ("unknown", 2))
    )



class PrtOutputPageDeliveryOrientationTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("faceDown", 4),
          ("faceUp", 3))
    )



class PrtMarkerCounterUnitTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              11,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("characters", 5),
          ("dotRow", 9),
          ("feet", 16),
          ("hours", 11),
          ("impressions", 7),
          ("lines", 6),
          ("meters", 17),
          ("micrometers", 4),
          ("sheets", 8),
          ("tenThousandthsOfInches", 3))
    )



class PrtMarkerSuppliesSupplyUnitTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("feet", 16),
          ("hours", 11),
          ("hundrethsOfFluidOunces", 14),
          ("impressions", 7),
          ("items", 18),
          ("meters", 17),
          ("micrometers", 4),
          ("other", 1),
          ("percent", 19),
          ("sheets", 8),
          ("tenThousandthsOfInches", 3),
          ("tenthsOfGrams", 13),
          ("tenthsOfMilliliters", 15),
          ("thousandthsOfOunces", 12),
          ("unknown", 2))
    )



class PrtMarkerSuppliesClassTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("receptacleThatIsFilled", 4),
          ("supplyThatIsConsumed", 3))
    )



class PrtMarkerColorantRoleTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("process", 3),
          ("spot", 4))
    )



class PrtMarkerAddressabilityUnitTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("micrometers", 4),
          ("tenThousandthsOfInches", 3))
    )



class PrtMediaPathMaxSpeedPrintUnitTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("charactersPerHour", 5),
          ("dotRowPerHour", 9),
          ("feetPerHour", 16),
          ("impressionsPerHour", 7),
          ("linesPerHour", 6),
          ("metersPerHour", 17),
          ("micrometersPerHour", 4),
          ("sheetsPerHour", 8),
          ("tenThousandthsOfInchesPerHour", 3))
    )



class PrtInterpreterTwoWayTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no", 4),
          ("yes", 3))
    )



class PrtAlertSeverityLevelTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("other", 1),
          ("warning", 4),
          ("warningBinaryChangeEvent", 5))
    )



# MIB Managed Objects in the order of their OIDs

_PrtMIBConformance_ObjectIdentity = ObjectIdentity
prtMIBConformance = _PrtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 2)
)
_PrtMIBGroups_ObjectIdentity = ObjectIdentity
prtMIBGroups = _PrtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 2, 2)
)
_PrtMIB2Groups_ObjectIdentity = ObjectIdentity
prtMIB2Groups = _PrtMIB2Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 2, 4)
)
_PrtGeneral_ObjectIdentity = ObjectIdentity
prtGeneral = _PrtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 5)
)
_PrtGeneralTable_Object = MibTable
prtGeneralTable = _PrtGeneralTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1)
)
if mibBuilder.loadTexts:
    prtGeneralTable.setStatus("current")
_PrtGeneralEntry_Object = MibTableRow
prtGeneralEntry = _PrtGeneralEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1)
)
prtGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    prtGeneralEntry.setStatus("current")
_PrtGeneralConfigChanges_Type = Counter32
_PrtGeneralConfigChanges_Object = MibTableColumn
prtGeneralConfigChanges = _PrtGeneralConfigChanges_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 1),
    _PrtGeneralConfigChanges_Type()
)
prtGeneralConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGeneralConfigChanges.setStatus("current")


class _PrtGeneralCurrentLocalization_Type(Integer32):
    """Custom type prtGeneralCurrentLocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtGeneralCurrentLocalization_Type.__name__ = "Integer32"
_PrtGeneralCurrentLocalization_Object = MibTableColumn
prtGeneralCurrentLocalization = _PrtGeneralCurrentLocalization_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 2),
    _PrtGeneralCurrentLocalization_Type()
)
prtGeneralCurrentLocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralCurrentLocalization.setStatus("current")
_PrtGeneralReset_Type = PrtGeneralResetTC
_PrtGeneralReset_Object = MibTableColumn
prtGeneralReset = _PrtGeneralReset_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 3),
    _PrtGeneralReset_Type()
)
prtGeneralReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralReset.setStatus("current")


class _PrtGeneralCurrentOperator_Type(OctetString):
    """Custom type prtGeneralCurrentOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PrtGeneralCurrentOperator_Type.__name__ = "OctetString"
_PrtGeneralCurrentOperator_Object = MibTableColumn
prtGeneralCurrentOperator = _PrtGeneralCurrentOperator_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 4),
    _PrtGeneralCurrentOperator_Type()
)
prtGeneralCurrentOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralCurrentOperator.setStatus("current")


class _PrtGeneralServicePerson_Type(OctetString):
    """Custom type prtGeneralServicePerson based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PrtGeneralServicePerson_Type.__name__ = "OctetString"
_PrtGeneralServicePerson_Object = MibTableColumn
prtGeneralServicePerson = _PrtGeneralServicePerson_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 5),
    _PrtGeneralServicePerson_Type()
)
prtGeneralServicePerson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralServicePerson.setStatus("current")


class _PrtInputDefaultIndex_Type(Integer32):
    """Custom type prtInputDefaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtInputDefaultIndex_Type.__name__ = "Integer32"
_PrtInputDefaultIndex_Object = MibTableColumn
prtInputDefaultIndex = _PrtInputDefaultIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 6),
    _PrtInputDefaultIndex_Type()
)
prtInputDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputDefaultIndex.setStatus("current")


class _PrtOutputDefaultIndex_Type(Integer32):
    """Custom type prtOutputDefaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtOutputDefaultIndex_Type.__name__ = "Integer32"
_PrtOutputDefaultIndex_Object = MibTableColumn
prtOutputDefaultIndex = _PrtOutputDefaultIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 7),
    _PrtOutputDefaultIndex_Type()
)
prtOutputDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputDefaultIndex.setStatus("current")


class _PrtMarkerDefaultIndex_Type(Integer32):
    """Custom type prtMarkerDefaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtMarkerDefaultIndex_Type.__name__ = "Integer32"
_PrtMarkerDefaultIndex_Object = MibTableColumn
prtMarkerDefaultIndex = _PrtMarkerDefaultIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 8),
    _PrtMarkerDefaultIndex_Type()
)
prtMarkerDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMarkerDefaultIndex.setStatus("current")


class _PrtMediaPathDefaultIndex_Type(Integer32):
    """Custom type prtMediaPathDefaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtMediaPathDefaultIndex_Type.__name__ = "Integer32"
_PrtMediaPathDefaultIndex_Object = MibTableColumn
prtMediaPathDefaultIndex = _PrtMediaPathDefaultIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 9),
    _PrtMediaPathDefaultIndex_Type()
)
prtMediaPathDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMediaPathDefaultIndex.setStatus("current")


class _PrtConsoleLocalization_Type(Integer32):
    """Custom type prtConsoleLocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtConsoleLocalization_Type.__name__ = "Integer32"
_PrtConsoleLocalization_Object = MibTableColumn
prtConsoleLocalization = _PrtConsoleLocalization_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 10),
    _PrtConsoleLocalization_Type()
)
prtConsoleLocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtConsoleLocalization.setStatus("current")


class _PrtConsoleNumberOfDisplayLines_Type(Integer32):
    """Custom type prtConsoleNumberOfDisplayLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtConsoleNumberOfDisplayLines_Type.__name__ = "Integer32"
_PrtConsoleNumberOfDisplayLines_Object = MibTableColumn
prtConsoleNumberOfDisplayLines = _PrtConsoleNumberOfDisplayLines_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 11),
    _PrtConsoleNumberOfDisplayLines_Type()
)
prtConsoleNumberOfDisplayLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtConsoleNumberOfDisplayLines.setStatus("current")


class _PrtConsoleNumberOfDisplayChars_Type(Integer32):
    """Custom type prtConsoleNumberOfDisplayChars based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtConsoleNumberOfDisplayChars_Type.__name__ = "Integer32"
_PrtConsoleNumberOfDisplayChars_Object = MibTableColumn
prtConsoleNumberOfDisplayChars = _PrtConsoleNumberOfDisplayChars_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 12),
    _PrtConsoleNumberOfDisplayChars_Type()
)
prtConsoleNumberOfDisplayChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtConsoleNumberOfDisplayChars.setStatus("current")
_PrtConsoleDisable_Type = PrtConsoleDisableTC
_PrtConsoleDisable_Object = MibTableColumn
prtConsoleDisable = _PrtConsoleDisable_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 13),
    _PrtConsoleDisable_Type()
)
prtConsoleDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtConsoleDisable.setStatus("current")
_PrtAuxiliarySheetStartupPage_Type = PresentOnOff
_PrtAuxiliarySheetStartupPage_Object = MibTableColumn
prtAuxiliarySheetStartupPage = _PrtAuxiliarySheetStartupPage_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 14),
    _PrtAuxiliarySheetStartupPage_Type()
)
prtAuxiliarySheetStartupPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtAuxiliarySheetStartupPage.setStatus("current")
_PrtAuxiliarySheetBannerPage_Type = PresentOnOff
_PrtAuxiliarySheetBannerPage_Object = MibTableColumn
prtAuxiliarySheetBannerPage = _PrtAuxiliarySheetBannerPage_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 15),
    _PrtAuxiliarySheetBannerPage_Type()
)
prtAuxiliarySheetBannerPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtAuxiliarySheetBannerPage.setStatus("current")


class _PrtGeneralPrinterName_Type(OctetString):
    """Custom type prtGeneralPrinterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PrtGeneralPrinterName_Type.__name__ = "OctetString"
_PrtGeneralPrinterName_Object = MibTableColumn
prtGeneralPrinterName = _PrtGeneralPrinterName_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 16),
    _PrtGeneralPrinterName_Type()
)
prtGeneralPrinterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralPrinterName.setStatus("current")


class _PrtGeneralSerialNumber_Type(OctetString):
    """Custom type prtGeneralSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtGeneralSerialNumber_Type.__name__ = "OctetString"
_PrtGeneralSerialNumber_Object = MibTableColumn
prtGeneralSerialNumber = _PrtGeneralSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 17),
    _PrtGeneralSerialNumber_Type()
)
prtGeneralSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralSerialNumber.setStatus("current")
_PrtAlertCriticalEvents_Type = Counter32
_PrtAlertCriticalEvents_Object = MibTableColumn
prtAlertCriticalEvents = _PrtAlertCriticalEvents_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 18),
    _PrtAlertCriticalEvents_Type()
)
prtAlertCriticalEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertCriticalEvents.setStatus("current")
_PrtAlertAllEvents_Type = Counter32
_PrtAlertAllEvents_Object = MibTableColumn
prtAlertAllEvents = _PrtAlertAllEvents_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 19),
    _PrtAlertAllEvents_Type()
)
prtAlertAllEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertAllEvents.setStatus("current")
_PrtStorageRefTable_Object = MibTable
prtStorageRefTable = _PrtStorageRefTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 2)
)
if mibBuilder.loadTexts:
    prtStorageRefTable.setStatus("current")
_PrtStorageRefEntry_Object = MibTableRow
prtStorageRefEntry = _PrtStorageRefEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 2, 1)
)
prtStorageRefEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrStorageIndex"),
    (0, "Printer-MIB", "prtStorageRefSeqNumber"),
)
if mibBuilder.loadTexts:
    prtStorageRefEntry.setStatus("current")


class _PrtStorageRefSeqNumber_Type(Integer32):
    """Custom type prtStorageRefSeqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtStorageRefSeqNumber_Type.__name__ = "Integer32"
_PrtStorageRefSeqNumber_Object = MibTableColumn
prtStorageRefSeqNumber = _PrtStorageRefSeqNumber_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 2, 1, 1),
    _PrtStorageRefSeqNumber_Type()
)
prtStorageRefSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtStorageRefSeqNumber.setStatus("current")


class _PrtStorageRefIndex_Type(Integer32):
    """Custom type prtStorageRefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrtStorageRefIndex_Type.__name__ = "Integer32"
_PrtStorageRefIndex_Object = MibTableColumn
prtStorageRefIndex = _PrtStorageRefIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 2, 1, 2),
    _PrtStorageRefIndex_Type()
)
prtStorageRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtStorageRefIndex.setStatus("current")
_PrtDeviceRefTable_Object = MibTable
prtDeviceRefTable = _PrtDeviceRefTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 3)
)
if mibBuilder.loadTexts:
    prtDeviceRefTable.setStatus("current")
_PrtDeviceRefEntry_Object = MibTableRow
prtDeviceRefEntry = _PrtDeviceRefEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 3, 1)
)
prtDeviceRefEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtDeviceRefSeqNumber"),
)
if mibBuilder.loadTexts:
    prtDeviceRefEntry.setStatus("current")


class _PrtDeviceRefSeqNumber_Type(Integer32):
    """Custom type prtDeviceRefSeqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtDeviceRefSeqNumber_Type.__name__ = "Integer32"
_PrtDeviceRefSeqNumber_Object = MibTableColumn
prtDeviceRefSeqNumber = _PrtDeviceRefSeqNumber_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 3, 1, 1),
    _PrtDeviceRefSeqNumber_Type()
)
prtDeviceRefSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtDeviceRefSeqNumber.setStatus("current")


class _PrtDeviceRefIndex_Type(Integer32):
    """Custom type prtDeviceRefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrtDeviceRefIndex_Type.__name__ = "Integer32"
_PrtDeviceRefIndex_Object = MibTableColumn
prtDeviceRefIndex = _PrtDeviceRefIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 3, 1, 2),
    _PrtDeviceRefIndex_Type()
)
prtDeviceRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDeviceRefIndex.setStatus("current")
_PrtCover_ObjectIdentity = ObjectIdentity
prtCover = _PrtCover_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 6)
)
_PrtCoverTable_Object = MibTable
prtCoverTable = _PrtCoverTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 6, 1)
)
if mibBuilder.loadTexts:
    prtCoverTable.setStatus("current")
_PrtCoverEntry_Object = MibTableRow
prtCoverEntry = _PrtCoverEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 6, 1, 1)
)
prtCoverEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtCoverIndex"),
)
if mibBuilder.loadTexts:
    prtCoverEntry.setStatus("current")


class _PrtCoverIndex_Type(Integer32):
    """Custom type prtCoverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtCoverIndex_Type.__name__ = "Integer32"
_PrtCoverIndex_Object = MibTableColumn
prtCoverIndex = _PrtCoverIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 6, 1, 1, 1),
    _PrtCoverIndex_Type()
)
prtCoverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtCoverIndex.setStatus("current")
_PrtCoverDescription_Type = PrtLocalizedDescriptionStringTC
_PrtCoverDescription_Object = MibTableColumn
prtCoverDescription = _PrtCoverDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 6, 1, 1, 2),
    _PrtCoverDescription_Type()
)
prtCoverDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCoverDescription.setStatus("current")
_PrtCoverStatus_Type = PrtCoverStatusTC
_PrtCoverStatus_Object = MibTableColumn
prtCoverStatus = _PrtCoverStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 6, 1, 1, 3),
    _PrtCoverStatus_Type()
)
prtCoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCoverStatus.setStatus("current")
_PrtLocalization_ObjectIdentity = ObjectIdentity
prtLocalization = _PrtLocalization_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 7)
)
_PrtLocalizationTable_Object = MibTable
prtLocalizationTable = _PrtLocalizationTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 7, 1)
)
if mibBuilder.loadTexts:
    prtLocalizationTable.setStatus("current")
_PrtLocalizationEntry_Object = MibTableRow
prtLocalizationEntry = _PrtLocalizationEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 7, 1, 1)
)
prtLocalizationEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtLocalizationIndex"),
)
if mibBuilder.loadTexts:
    prtLocalizationEntry.setStatus("current")


class _PrtLocalizationIndex_Type(Integer32):
    """Custom type prtLocalizationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtLocalizationIndex_Type.__name__ = "Integer32"
_PrtLocalizationIndex_Object = MibTableColumn
prtLocalizationIndex = _PrtLocalizationIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 7, 1, 1, 1),
    _PrtLocalizationIndex_Type()
)
prtLocalizationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtLocalizationIndex.setStatus("current")


class _PrtLocalizationLanguage_Type(OctetString):
    """Custom type prtLocalizationLanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PrtLocalizationLanguage_Type.__name__ = "OctetString"
_PrtLocalizationLanguage_Object = MibTableColumn
prtLocalizationLanguage = _PrtLocalizationLanguage_Object(
    (1, 3, 6, 1, 2, 1, 43, 7, 1, 1, 2),
    _PrtLocalizationLanguage_Type()
)
prtLocalizationLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtLocalizationLanguage.setStatus("current")


class _PrtLocalizationCountry_Type(OctetString):
    """Custom type prtLocalizationCountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PrtLocalizationCountry_Type.__name__ = "OctetString"
_PrtLocalizationCountry_Object = MibTableColumn
prtLocalizationCountry = _PrtLocalizationCountry_Object(
    (1, 3, 6, 1, 2, 1, 43, 7, 1, 1, 3),
    _PrtLocalizationCountry_Type()
)
prtLocalizationCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtLocalizationCountry.setStatus("current")
_PrtLocalizationCharacterSet_Type = IANACharset
_PrtLocalizationCharacterSet_Object = MibTableColumn
prtLocalizationCharacterSet = _PrtLocalizationCharacterSet_Object(
    (1, 3, 6, 1, 2, 1, 43, 7, 1, 1, 4),
    _PrtLocalizationCharacterSet_Type()
)
prtLocalizationCharacterSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtLocalizationCharacterSet.setStatus("current")
_PrtInput_ObjectIdentity = ObjectIdentity
prtInput = _PrtInput_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 8)
)
_PrtInputTable_Object = MibTable
prtInputTable = _PrtInputTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2)
)
if mibBuilder.loadTexts:
    prtInputTable.setStatus("current")
_PrtInputEntry_Object = MibTableRow
prtInputEntry = _PrtInputEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1)
)
prtInputEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtInputIndex"),
)
if mibBuilder.loadTexts:
    prtInputEntry.setStatus("current")


class _PrtInputIndex_Type(Integer32):
    """Custom type prtInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtInputIndex_Type.__name__ = "Integer32"
_PrtInputIndex_Object = MibTableColumn
prtInputIndex = _PrtInputIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 1),
    _PrtInputIndex_Type()
)
prtInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtInputIndex.setStatus("current")
_PrtInputType_Type = PrtInputTypeTC
_PrtInputType_Object = MibTableColumn
prtInputType = _PrtInputType_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 2),
    _PrtInputType_Type()
)
prtInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputType.setStatus("current")
_PrtInputDimUnit_Type = PrtMediaUnitTC
_PrtInputDimUnit_Object = MibTableColumn
prtInputDimUnit = _PrtInputDimUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 3),
    _PrtInputDimUnit_Type()
)
prtInputDimUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputDimUnit.setStatus("current")


class _PrtInputMediaDimFeedDirDeclared_Type(Integer32):
    """Custom type prtInputMediaDimFeedDirDeclared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaDimFeedDirDeclared_Type.__name__ = "Integer32"
_PrtInputMediaDimFeedDirDeclared_Object = MibTableColumn
prtInputMediaDimFeedDirDeclared = _PrtInputMediaDimFeedDirDeclared_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 4),
    _PrtInputMediaDimFeedDirDeclared_Type()
)
prtInputMediaDimFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaDimFeedDirDeclared.setStatus("current")


class _PrtInputMediaDimXFeedDirDeclared_Type(Integer32):
    """Custom type prtInputMediaDimXFeedDirDeclared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaDimXFeedDirDeclared_Type.__name__ = "Integer32"
_PrtInputMediaDimXFeedDirDeclared_Object = MibTableColumn
prtInputMediaDimXFeedDirDeclared = _PrtInputMediaDimXFeedDirDeclared_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 5),
    _PrtInputMediaDimXFeedDirDeclared_Type()
)
prtInputMediaDimXFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaDimXFeedDirDeclared.setStatus("current")


class _PrtInputMediaDimFeedDirChosen_Type(Integer32):
    """Custom type prtInputMediaDimFeedDirChosen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaDimFeedDirChosen_Type.__name__ = "Integer32"
_PrtInputMediaDimFeedDirChosen_Object = MibTableColumn
prtInputMediaDimFeedDirChosen = _PrtInputMediaDimFeedDirChosen_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 6),
    _PrtInputMediaDimFeedDirChosen_Type()
)
prtInputMediaDimFeedDirChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputMediaDimFeedDirChosen.setStatus("current")


class _PrtInputMediaDimXFeedDirChosen_Type(Integer32):
    """Custom type prtInputMediaDimXFeedDirChosen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaDimXFeedDirChosen_Type.__name__ = "Integer32"
_PrtInputMediaDimXFeedDirChosen_Object = MibTableColumn
prtInputMediaDimXFeedDirChosen = _PrtInputMediaDimXFeedDirChosen_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 7),
    _PrtInputMediaDimXFeedDirChosen_Type()
)
prtInputMediaDimXFeedDirChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputMediaDimXFeedDirChosen.setStatus("current")
_PrtInputCapacityUnit_Type = PrtCapacityUnitTC
_PrtInputCapacityUnit_Object = MibTableColumn
prtInputCapacityUnit = _PrtInputCapacityUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 8),
    _PrtInputCapacityUnit_Type()
)
prtInputCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputCapacityUnit.setStatus("current")


class _PrtInputMaxCapacity_Type(Integer32):
    """Custom type prtInputMaxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMaxCapacity_Type.__name__ = "Integer32"
_PrtInputMaxCapacity_Object = MibTableColumn
prtInputMaxCapacity = _PrtInputMaxCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 9),
    _PrtInputMaxCapacity_Type()
)
prtInputMaxCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMaxCapacity.setStatus("current")


class _PrtInputCurrentLevel_Type(Integer32):
    """Custom type prtInputCurrentLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 2147483647),
    )


_PrtInputCurrentLevel_Type.__name__ = "Integer32"
_PrtInputCurrentLevel_Object = MibTableColumn
prtInputCurrentLevel = _PrtInputCurrentLevel_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 10),
    _PrtInputCurrentLevel_Type()
)
prtInputCurrentLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputCurrentLevel.setStatus("current")
_PrtInputStatus_Type = PrtSubUnitStatusTC
_PrtInputStatus_Object = MibTableColumn
prtInputStatus = _PrtInputStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 11),
    _PrtInputStatus_Type()
)
prtInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputStatus.setStatus("current")


class _PrtInputMediaName_Type(OctetString):
    """Custom type prtInputMediaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputMediaName_Type.__name__ = "OctetString"
_PrtInputMediaName_Object = MibTableColumn
prtInputMediaName = _PrtInputMediaName_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 12),
    _PrtInputMediaName_Type()
)
prtInputMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaName.setStatus("current")


class _PrtInputName_Type(OctetString):
    """Custom type prtInputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputName_Type.__name__ = "OctetString"
_PrtInputName_Object = MibTableColumn
prtInputName = _PrtInputName_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 13),
    _PrtInputName_Type()
)
prtInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputName.setStatus("current")


class _PrtInputVendorName_Type(OctetString):
    """Custom type prtInputVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputVendorName_Type.__name__ = "OctetString"
_PrtInputVendorName_Object = MibTableColumn
prtInputVendorName = _PrtInputVendorName_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 14),
    _PrtInputVendorName_Type()
)
prtInputVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputVendorName.setStatus("current")


class _PrtInputModel_Type(OctetString):
    """Custom type prtInputModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputModel_Type.__name__ = "OctetString"
_PrtInputModel_Object = MibTableColumn
prtInputModel = _PrtInputModel_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 15),
    _PrtInputModel_Type()
)
prtInputModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputModel.setStatus("current")


class _PrtInputVersion_Type(OctetString):
    """Custom type prtInputVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputVersion_Type.__name__ = "OctetString"
_PrtInputVersion_Object = MibTableColumn
prtInputVersion = _PrtInputVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 16),
    _PrtInputVersion_Type()
)
prtInputVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputVersion.setStatus("current")


class _PrtInputSerialNumber_Type(OctetString):
    """Custom type prtInputSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrtInputSerialNumber_Type.__name__ = "OctetString"
_PrtInputSerialNumber_Object = MibTableColumn
prtInputSerialNumber = _PrtInputSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 17),
    _PrtInputSerialNumber_Type()
)
prtInputSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputSerialNumber.setStatus("current")
_PrtInputDescription_Type = PrtLocalizedDescriptionStringTC
_PrtInputDescription_Object = MibTableColumn
prtInputDescription = _PrtInputDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 18),
    _PrtInputDescription_Type()
)
prtInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputDescription.setStatus("current")
_PrtInputSecurity_Type = PresentOnOff
_PrtInputSecurity_Object = MibTableColumn
prtInputSecurity = _PrtInputSecurity_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 19),
    _PrtInputSecurity_Type()
)
prtInputSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputSecurity.setStatus("current")


class _PrtInputMediaWeight_Type(Integer32):
    """Custom type prtInputMediaWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaWeight_Type.__name__ = "Integer32"
_PrtInputMediaWeight_Object = MibTableColumn
prtInputMediaWeight = _PrtInputMediaWeight_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 20),
    _PrtInputMediaWeight_Type()
)
prtInputMediaWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaWeight.setStatus("current")


class _PrtInputMediaType_Type(OctetString):
    """Custom type prtInputMediaType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputMediaType_Type.__name__ = "OctetString"
_PrtInputMediaType_Object = MibTableColumn
prtInputMediaType = _PrtInputMediaType_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 21),
    _PrtInputMediaType_Type()
)
prtInputMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaType.setStatus("current")


class _PrtInputMediaColor_Type(OctetString):
    """Custom type prtInputMediaColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputMediaColor_Type.__name__ = "OctetString"
_PrtInputMediaColor_Object = MibTableColumn
prtInputMediaColor = _PrtInputMediaColor_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 22),
    _PrtInputMediaColor_Type()
)
prtInputMediaColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaColor.setStatus("current")


class _PrtInputMediaFormParts_Type(Integer32):
    """Custom type prtInputMediaFormParts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaFormParts_Type.__name__ = "Integer32"
_PrtInputMediaFormParts_Object = MibTableColumn
prtInputMediaFormParts = _PrtInputMediaFormParts_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 23),
    _PrtInputMediaFormParts_Type()
)
prtInputMediaFormParts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaFormParts.setStatus("current")


class _PrtInputMediaLoadTimeout_Type(Integer32):
    """Custom type prtInputMediaLoadTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaLoadTimeout_Type.__name__ = "Integer32"
_PrtInputMediaLoadTimeout_Object = MibTableColumn
prtInputMediaLoadTimeout = _PrtInputMediaLoadTimeout_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 24),
    _PrtInputMediaLoadTimeout_Type()
)
prtInputMediaLoadTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaLoadTimeout.setStatus("current")


class _PrtInputNextIndex_Type(Integer32):
    """Custom type prtInputNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 2147483647),
    )


_PrtInputNextIndex_Type.__name__ = "Integer32"
_PrtInputNextIndex_Object = MibTableColumn
prtInputNextIndex = _PrtInputNextIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 25),
    _PrtInputNextIndex_Type()
)
prtInputNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputNextIndex.setStatus("current")
_PrtOutput_ObjectIdentity = ObjectIdentity
prtOutput = _PrtOutput_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 9)
)
_PrtOutputTable_Object = MibTable
prtOutputTable = _PrtOutputTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2)
)
if mibBuilder.loadTexts:
    prtOutputTable.setStatus("current")
_PrtOutputEntry_Object = MibTableRow
prtOutputEntry = _PrtOutputEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1)
)
prtOutputEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtOutputIndex"),
)
if mibBuilder.loadTexts:
    prtOutputEntry.setStatus("current")


class _PrtOutputIndex_Type(Integer32):
    """Custom type prtOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtOutputIndex_Type.__name__ = "Integer32"
_PrtOutputIndex_Object = MibTableColumn
prtOutputIndex = _PrtOutputIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 1),
    _PrtOutputIndex_Type()
)
prtOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtOutputIndex.setStatus("current")
_PrtOutputType_Type = PrtOutputTypeTC
_PrtOutputType_Object = MibTableColumn
prtOutputType = _PrtOutputType_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 2),
    _PrtOutputType_Type()
)
prtOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputType.setStatus("current")
_PrtOutputCapacityUnit_Type = PrtCapacityUnitTC
_PrtOutputCapacityUnit_Object = MibTableColumn
prtOutputCapacityUnit = _PrtOutputCapacityUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 3),
    _PrtOutputCapacityUnit_Type()
)
prtOutputCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputCapacityUnit.setStatus("current")


class _PrtOutputMaxCapacity_Type(Integer32):
    """Custom type prtOutputMaxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMaxCapacity_Type.__name__ = "Integer32"
_PrtOutputMaxCapacity_Object = MibTableColumn
prtOutputMaxCapacity = _PrtOutputMaxCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 4),
    _PrtOutputMaxCapacity_Type()
)
prtOutputMaxCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMaxCapacity.setStatus("current")


class _PrtOutputRemainingCapacity_Type(Integer32):
    """Custom type prtOutputRemainingCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 2147483647),
    )


_PrtOutputRemainingCapacity_Type.__name__ = "Integer32"
_PrtOutputRemainingCapacity_Object = MibTableColumn
prtOutputRemainingCapacity = _PrtOutputRemainingCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 5),
    _PrtOutputRemainingCapacity_Type()
)
prtOutputRemainingCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputRemainingCapacity.setStatus("current")
_PrtOutputStatus_Type = PrtSubUnitStatusTC
_PrtOutputStatus_Object = MibTableColumn
prtOutputStatus = _PrtOutputStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 6),
    _PrtOutputStatus_Type()
)
prtOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputStatus.setStatus("current")


class _PrtOutputName_Type(OctetString):
    """Custom type prtOutputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputName_Type.__name__ = "OctetString"
_PrtOutputName_Object = MibTableColumn
prtOutputName = _PrtOutputName_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 7),
    _PrtOutputName_Type()
)
prtOutputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputName.setStatus("current")


class _PrtOutputVendorName_Type(OctetString):
    """Custom type prtOutputVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputVendorName_Type.__name__ = "OctetString"
_PrtOutputVendorName_Object = MibTableColumn
prtOutputVendorName = _PrtOutputVendorName_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 8),
    _PrtOutputVendorName_Type()
)
prtOutputVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputVendorName.setStatus("current")


class _PrtOutputModel_Type(OctetString):
    """Custom type prtOutputModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputModel_Type.__name__ = "OctetString"
_PrtOutputModel_Object = MibTableColumn
prtOutputModel = _PrtOutputModel_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 9),
    _PrtOutputModel_Type()
)
prtOutputModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputModel.setStatus("current")


class _PrtOutputVersion_Type(OctetString):
    """Custom type prtOutputVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputVersion_Type.__name__ = "OctetString"
_PrtOutputVersion_Object = MibTableColumn
prtOutputVersion = _PrtOutputVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 10),
    _PrtOutputVersion_Type()
)
prtOutputVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputVersion.setStatus("current")


class _PrtOutputSerialNumber_Type(OctetString):
    """Custom type prtOutputSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputSerialNumber_Type.__name__ = "OctetString"
_PrtOutputSerialNumber_Object = MibTableColumn
prtOutputSerialNumber = _PrtOutputSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 11),
    _PrtOutputSerialNumber_Type()
)
prtOutputSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputSerialNumber.setStatus("current")
_PrtOutputDescription_Type = PrtLocalizedDescriptionStringTC
_PrtOutputDescription_Object = MibTableColumn
prtOutputDescription = _PrtOutputDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 12),
    _PrtOutputDescription_Type()
)
prtOutputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputDescription.setStatus("current")
_PrtOutputSecurity_Type = PresentOnOff
_PrtOutputSecurity_Object = MibTableColumn
prtOutputSecurity = _PrtOutputSecurity_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 13),
    _PrtOutputSecurity_Type()
)
prtOutputSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputSecurity.setStatus("current")
_PrtOutputDimUnit_Type = PrtMediaUnitTC
_PrtOutputDimUnit_Object = MibTableColumn
prtOutputDimUnit = _PrtOutputDimUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 14),
    _PrtOutputDimUnit_Type()
)
prtOutputDimUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputDimUnit.setStatus("current")


class _PrtOutputMaxDimFeedDir_Type(Integer32):
    """Custom type prtOutputMaxDimFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMaxDimFeedDir_Type.__name__ = "Integer32"
_PrtOutputMaxDimFeedDir_Object = MibTableColumn
prtOutputMaxDimFeedDir = _PrtOutputMaxDimFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 15),
    _PrtOutputMaxDimFeedDir_Type()
)
prtOutputMaxDimFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMaxDimFeedDir.setStatus("current")


class _PrtOutputMaxDimXFeedDir_Type(Integer32):
    """Custom type prtOutputMaxDimXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMaxDimXFeedDir_Type.__name__ = "Integer32"
_PrtOutputMaxDimXFeedDir_Object = MibTableColumn
prtOutputMaxDimXFeedDir = _PrtOutputMaxDimXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 16),
    _PrtOutputMaxDimXFeedDir_Type()
)
prtOutputMaxDimXFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMaxDimXFeedDir.setStatus("current")


class _PrtOutputMinDimFeedDir_Type(Integer32):
    """Custom type prtOutputMinDimFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMinDimFeedDir_Type.__name__ = "Integer32"
_PrtOutputMinDimFeedDir_Object = MibTableColumn
prtOutputMinDimFeedDir = _PrtOutputMinDimFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 17),
    _PrtOutputMinDimFeedDir_Type()
)
prtOutputMinDimFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMinDimFeedDir.setStatus("current")


class _PrtOutputMinDimXFeedDir_Type(Integer32):
    """Custom type prtOutputMinDimXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMinDimXFeedDir_Type.__name__ = "Integer32"
_PrtOutputMinDimXFeedDir_Object = MibTableColumn
prtOutputMinDimXFeedDir = _PrtOutputMinDimXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 18),
    _PrtOutputMinDimXFeedDir_Type()
)
prtOutputMinDimXFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMinDimXFeedDir.setStatus("current")
_PrtOutputStackingOrder_Type = PrtOutputStackingOrderTC
_PrtOutputStackingOrder_Object = MibTableColumn
prtOutputStackingOrder = _PrtOutputStackingOrder_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 19),
    _PrtOutputStackingOrder_Type()
)
prtOutputStackingOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputStackingOrder.setStatus("current")
_PrtOutputPageDeliveryOrientation_Type = PrtOutputPageDeliveryOrientationTC
_PrtOutputPageDeliveryOrientation_Object = MibTableColumn
prtOutputPageDeliveryOrientation = _PrtOutputPageDeliveryOrientation_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 20),
    _PrtOutputPageDeliveryOrientation_Type()
)
prtOutputPageDeliveryOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputPageDeliveryOrientation.setStatus("current")
_PrtOutputBursting_Type = PresentOnOff
_PrtOutputBursting_Object = MibTableColumn
prtOutputBursting = _PrtOutputBursting_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 21),
    _PrtOutputBursting_Type()
)
prtOutputBursting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputBursting.setStatus("current")
_PrtOutputDecollating_Type = PresentOnOff
_PrtOutputDecollating_Object = MibTableColumn
prtOutputDecollating = _PrtOutputDecollating_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 22),
    _PrtOutputDecollating_Type()
)
prtOutputDecollating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputDecollating.setStatus("current")
_PrtOutputPageCollated_Type = PresentOnOff
_PrtOutputPageCollated_Object = MibTableColumn
prtOutputPageCollated = _PrtOutputPageCollated_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 23),
    _PrtOutputPageCollated_Type()
)
prtOutputPageCollated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputPageCollated.setStatus("current")
_PrtOutputOffsetStacking_Type = PresentOnOff
_PrtOutputOffsetStacking_Object = MibTableColumn
prtOutputOffsetStacking = _PrtOutputOffsetStacking_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 24),
    _PrtOutputOffsetStacking_Type()
)
prtOutputOffsetStacking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputOffsetStacking.setStatus("current")
_PrtMarker_ObjectIdentity = ObjectIdentity
prtMarker = _PrtMarker_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 10)
)
_PrtMarkerTable_Object = MibTable
prtMarkerTable = _PrtMarkerTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2)
)
if mibBuilder.loadTexts:
    prtMarkerTable.setStatus("current")
_PrtMarkerEntry_Object = MibTableRow
prtMarkerEntry = _PrtMarkerEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1)
)
prtMarkerEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtMarkerIndex"),
)
if mibBuilder.loadTexts:
    prtMarkerEntry.setStatus("current")


class _PrtMarkerIndex_Type(Integer32):
    """Custom type prtMarkerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtMarkerIndex_Type.__name__ = "Integer32"
_PrtMarkerIndex_Object = MibTableColumn
prtMarkerIndex = _PrtMarkerIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 1),
    _PrtMarkerIndex_Type()
)
prtMarkerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtMarkerIndex.setStatus("current")
_PrtMarkerMarkTech_Type = PrtMarkerMarkTechTC
_PrtMarkerMarkTech_Object = MibTableColumn
prtMarkerMarkTech = _PrtMarkerMarkTech_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 2),
    _PrtMarkerMarkTech_Type()
)
prtMarkerMarkTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerMarkTech.setStatus("current")
_PrtMarkerCounterUnit_Type = PrtMarkerCounterUnitTC
_PrtMarkerCounterUnit_Object = MibTableColumn
prtMarkerCounterUnit = _PrtMarkerCounterUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 3),
    _PrtMarkerCounterUnit_Type()
)
prtMarkerCounterUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerCounterUnit.setStatus("current")
_PrtMarkerLifeCount_Type = Counter32
_PrtMarkerLifeCount_Object = MibTableColumn
prtMarkerLifeCount = _PrtMarkerLifeCount_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 4),
    _PrtMarkerLifeCount_Type()
)
prtMarkerLifeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerLifeCount.setStatus("current")
_PrtMarkerPowerOnCount_Type = Counter32
_PrtMarkerPowerOnCount_Object = MibTableColumn
prtMarkerPowerOnCount = _PrtMarkerPowerOnCount_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 5),
    _PrtMarkerPowerOnCount_Type()
)
prtMarkerPowerOnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerPowerOnCount.setStatus("current")


class _PrtMarkerProcessColorants_Type(Integer32):
    """Custom type prtMarkerProcessColorants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerProcessColorants_Type.__name__ = "Integer32"
_PrtMarkerProcessColorants_Object = MibTableColumn
prtMarkerProcessColorants = _PrtMarkerProcessColorants_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 6),
    _PrtMarkerProcessColorants_Type()
)
prtMarkerProcessColorants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerProcessColorants.setStatus("current")


class _PrtMarkerSpotColorants_Type(Integer32):
    """Custom type prtMarkerSpotColorants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerSpotColorants_Type.__name__ = "Integer32"
_PrtMarkerSpotColorants_Object = MibTableColumn
prtMarkerSpotColorants = _PrtMarkerSpotColorants_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 7),
    _PrtMarkerSpotColorants_Type()
)
prtMarkerSpotColorants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSpotColorants.setStatus("current")
_PrtMarkerAddressabilityUnit_Type = PrtMarkerAddressabilityUnitTC
_PrtMarkerAddressabilityUnit_Object = MibTableColumn
prtMarkerAddressabilityUnit = _PrtMarkerAddressabilityUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 8),
    _PrtMarkerAddressabilityUnit_Type()
)
prtMarkerAddressabilityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerAddressabilityUnit.setStatus("current")


class _PrtMarkerAddressabilityFeedDir_Type(Integer32):
    """Custom type prtMarkerAddressabilityFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerAddressabilityFeedDir_Type.__name__ = "Integer32"
_PrtMarkerAddressabilityFeedDir_Object = MibTableColumn
prtMarkerAddressabilityFeedDir = _PrtMarkerAddressabilityFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 9),
    _PrtMarkerAddressabilityFeedDir_Type()
)
prtMarkerAddressabilityFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerAddressabilityFeedDir.setStatus("current")


class _PrtMarkerAddressabilityXFeedDir_Type(Integer32):
    """Custom type prtMarkerAddressabilityXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerAddressabilityXFeedDir_Type.__name__ = "Integer32"
_PrtMarkerAddressabilityXFeedDir_Object = MibTableColumn
prtMarkerAddressabilityXFeedDir = _PrtMarkerAddressabilityXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 10),
    _PrtMarkerAddressabilityXFeedDir_Type()
)
prtMarkerAddressabilityXFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerAddressabilityXFeedDir.setStatus("current")


class _PrtMarkerNorthMargin_Type(Integer32):
    """Custom type prtMarkerNorthMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerNorthMargin_Type.__name__ = "Integer32"
_PrtMarkerNorthMargin_Object = MibTableColumn
prtMarkerNorthMargin = _PrtMarkerNorthMargin_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 11),
    _PrtMarkerNorthMargin_Type()
)
prtMarkerNorthMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerNorthMargin.setStatus("current")


class _PrtMarkerSouthMargin_Type(Integer32):
    """Custom type prtMarkerSouthMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerSouthMargin_Type.__name__ = "Integer32"
_PrtMarkerSouthMargin_Object = MibTableColumn
prtMarkerSouthMargin = _PrtMarkerSouthMargin_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 12),
    _PrtMarkerSouthMargin_Type()
)
prtMarkerSouthMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSouthMargin.setStatus("current")


class _PrtMarkerWestMargin_Type(Integer32):
    """Custom type prtMarkerWestMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerWestMargin_Type.__name__ = "Integer32"
_PrtMarkerWestMargin_Object = MibTableColumn
prtMarkerWestMargin = _PrtMarkerWestMargin_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 13),
    _PrtMarkerWestMargin_Type()
)
prtMarkerWestMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerWestMargin.setStatus("current")


class _PrtMarkerEastMargin_Type(Integer32):
    """Custom type prtMarkerEastMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerEastMargin_Type.__name__ = "Integer32"
_PrtMarkerEastMargin_Object = MibTableColumn
prtMarkerEastMargin = _PrtMarkerEastMargin_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 14),
    _PrtMarkerEastMargin_Type()
)
prtMarkerEastMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerEastMargin.setStatus("current")
_PrtMarkerStatus_Type = PrtSubUnitStatusTC
_PrtMarkerStatus_Object = MibTableColumn
prtMarkerStatus = _PrtMarkerStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 15),
    _PrtMarkerStatus_Type()
)
prtMarkerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerStatus.setStatus("current")
_PrtMarkerSupplies_ObjectIdentity = ObjectIdentity
prtMarkerSupplies = _PrtMarkerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 11)
)
_PrtMarkerSuppliesTable_Object = MibTable
prtMarkerSuppliesTable = _PrtMarkerSuppliesTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1)
)
if mibBuilder.loadTexts:
    prtMarkerSuppliesTable.setStatus("current")
_PrtMarkerSuppliesEntry_Object = MibTableRow
prtMarkerSuppliesEntry = _PrtMarkerSuppliesEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1)
)
prtMarkerSuppliesEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtMarkerSuppliesIndex"),
)
if mibBuilder.loadTexts:
    prtMarkerSuppliesEntry.setStatus("current")


class _PrtMarkerSuppliesIndex_Type(Integer32):
    """Custom type prtMarkerSuppliesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtMarkerSuppliesIndex_Type.__name__ = "Integer32"
_PrtMarkerSuppliesIndex_Object = MibTableColumn
prtMarkerSuppliesIndex = _PrtMarkerSuppliesIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 1),
    _PrtMarkerSuppliesIndex_Type()
)
prtMarkerSuppliesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtMarkerSuppliesIndex.setStatus("current")


class _PrtMarkerSuppliesMarkerIndex_Type(Integer32):
    """Custom type prtMarkerSuppliesMarkerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerSuppliesMarkerIndex_Type.__name__ = "Integer32"
_PrtMarkerSuppliesMarkerIndex_Object = MibTableColumn
prtMarkerSuppliesMarkerIndex = _PrtMarkerSuppliesMarkerIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 2),
    _PrtMarkerSuppliesMarkerIndex_Type()
)
prtMarkerSuppliesMarkerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesMarkerIndex.setStatus("current")


class _PrtMarkerSuppliesColorantIndex_Type(Integer32):
    """Custom type prtMarkerSuppliesColorantIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerSuppliesColorantIndex_Type.__name__ = "Integer32"
_PrtMarkerSuppliesColorantIndex_Object = MibTableColumn
prtMarkerSuppliesColorantIndex = _PrtMarkerSuppliesColorantIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 3),
    _PrtMarkerSuppliesColorantIndex_Type()
)
prtMarkerSuppliesColorantIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesColorantIndex.setStatus("current")
_PrtMarkerSuppliesClass_Type = PrtMarkerSuppliesClassTC
_PrtMarkerSuppliesClass_Object = MibTableColumn
prtMarkerSuppliesClass = _PrtMarkerSuppliesClass_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 4),
    _PrtMarkerSuppliesClass_Type()
)
prtMarkerSuppliesClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesClass.setStatus("current")
_PrtMarkerSuppliesType_Type = PrtMarkerSuppliesTypeTC
_PrtMarkerSuppliesType_Object = MibTableColumn
prtMarkerSuppliesType = _PrtMarkerSuppliesType_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 5),
    _PrtMarkerSuppliesType_Type()
)
prtMarkerSuppliesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesType.setStatus("current")
_PrtMarkerSuppliesDescription_Type = PrtLocalizedDescriptionStringTC
_PrtMarkerSuppliesDescription_Object = MibTableColumn
prtMarkerSuppliesDescription = _PrtMarkerSuppliesDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 6),
    _PrtMarkerSuppliesDescription_Type()
)
prtMarkerSuppliesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesDescription.setStatus("current")
_PrtMarkerSuppliesSupplyUnit_Type = PrtMarkerSuppliesSupplyUnitTC
_PrtMarkerSuppliesSupplyUnit_Object = MibTableColumn
prtMarkerSuppliesSupplyUnit = _PrtMarkerSuppliesSupplyUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 7),
    _PrtMarkerSuppliesSupplyUnit_Type()
)
prtMarkerSuppliesSupplyUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesSupplyUnit.setStatus("current")


class _PrtMarkerSuppliesMaxCapacity_Type(Integer32):
    """Custom type prtMarkerSuppliesMaxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerSuppliesMaxCapacity_Type.__name__ = "Integer32"
_PrtMarkerSuppliesMaxCapacity_Object = MibTableColumn
prtMarkerSuppliesMaxCapacity = _PrtMarkerSuppliesMaxCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 8),
    _PrtMarkerSuppliesMaxCapacity_Type()
)
prtMarkerSuppliesMaxCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMarkerSuppliesMaxCapacity.setStatus("current")


class _PrtMarkerSuppliesLevel_Type(Integer32):
    """Custom type prtMarkerSuppliesLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 2147483647),
    )


_PrtMarkerSuppliesLevel_Type.__name__ = "Integer32"
_PrtMarkerSuppliesLevel_Object = MibTableColumn
prtMarkerSuppliesLevel = _PrtMarkerSuppliesLevel_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 9),
    _PrtMarkerSuppliesLevel_Type()
)
prtMarkerSuppliesLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMarkerSuppliesLevel.setStatus("current")
_PrtMarkerColorant_ObjectIdentity = ObjectIdentity
prtMarkerColorant = _PrtMarkerColorant_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 12)
)
_PrtMarkerColorantTable_Object = MibTable
prtMarkerColorantTable = _PrtMarkerColorantTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1)
)
if mibBuilder.loadTexts:
    prtMarkerColorantTable.setStatus("current")
_PrtMarkerColorantEntry_Object = MibTableRow
prtMarkerColorantEntry = _PrtMarkerColorantEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1)
)
prtMarkerColorantEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtMarkerColorantIndex"),
)
if mibBuilder.loadTexts:
    prtMarkerColorantEntry.setStatus("current")


class _PrtMarkerColorantIndex_Type(Integer32):
    """Custom type prtMarkerColorantIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtMarkerColorantIndex_Type.__name__ = "Integer32"
_PrtMarkerColorantIndex_Object = MibTableColumn
prtMarkerColorantIndex = _PrtMarkerColorantIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1, 1),
    _PrtMarkerColorantIndex_Type()
)
prtMarkerColorantIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtMarkerColorantIndex.setStatus("current")


class _PrtMarkerColorantMarkerIndex_Type(Integer32):
    """Custom type prtMarkerColorantMarkerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerColorantMarkerIndex_Type.__name__ = "Integer32"
_PrtMarkerColorantMarkerIndex_Object = MibTableColumn
prtMarkerColorantMarkerIndex = _PrtMarkerColorantMarkerIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1, 2),
    _PrtMarkerColorantMarkerIndex_Type()
)
prtMarkerColorantMarkerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerColorantMarkerIndex.setStatus("current")
_PrtMarkerColorantRole_Type = PrtMarkerColorantRoleTC
_PrtMarkerColorantRole_Object = MibTableColumn
prtMarkerColorantRole = _PrtMarkerColorantRole_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1, 3),
    _PrtMarkerColorantRole_Type()
)
prtMarkerColorantRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerColorantRole.setStatus("current")


class _PrtMarkerColorantValue_Type(OctetString):
    """Custom type prtMarkerColorantValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtMarkerColorantValue_Type.__name__ = "OctetString"
_PrtMarkerColorantValue_Object = MibTableColumn
prtMarkerColorantValue = _PrtMarkerColorantValue_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1, 4),
    _PrtMarkerColorantValue_Type()
)
prtMarkerColorantValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerColorantValue.setStatus("current")


class _PrtMarkerColorantTonality_Type(Integer32):
    """Custom type prtMarkerColorantTonality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2147483647),
    )


_PrtMarkerColorantTonality_Type.__name__ = "Integer32"
_PrtMarkerColorantTonality_Object = MibTableColumn
prtMarkerColorantTonality = _PrtMarkerColorantTonality_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1, 5),
    _PrtMarkerColorantTonality_Type()
)
prtMarkerColorantTonality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerColorantTonality.setStatus("current")
_PrtMediaPath_ObjectIdentity = ObjectIdentity
prtMediaPath = _PrtMediaPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 13)
)
_PrtMediaPathTable_Object = MibTable
prtMediaPathTable = _PrtMediaPathTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4)
)
if mibBuilder.loadTexts:
    prtMediaPathTable.setStatus("current")
_PrtMediaPathEntry_Object = MibTableRow
prtMediaPathEntry = _PrtMediaPathEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1)
)
prtMediaPathEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtMediaPathIndex"),
)
if mibBuilder.loadTexts:
    prtMediaPathEntry.setStatus("current")


class _PrtMediaPathIndex_Type(Integer32):
    """Custom type prtMediaPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtMediaPathIndex_Type.__name__ = "Integer32"
_PrtMediaPathIndex_Object = MibTableColumn
prtMediaPathIndex = _PrtMediaPathIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 1),
    _PrtMediaPathIndex_Type()
)
prtMediaPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtMediaPathIndex.setStatus("current")
_PrtMediaPathMaxSpeedPrintUnit_Type = PrtMediaPathMaxSpeedPrintUnitTC
_PrtMediaPathMaxSpeedPrintUnit_Object = MibTableColumn
prtMediaPathMaxSpeedPrintUnit = _PrtMediaPathMaxSpeedPrintUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 2),
    _PrtMediaPathMaxSpeedPrintUnit_Type()
)
prtMediaPathMaxSpeedPrintUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMaxSpeedPrintUnit.setStatus("current")
_PrtMediaPathMediaSizeUnit_Type = PrtMediaUnitTC
_PrtMediaPathMediaSizeUnit_Object = MibTableColumn
prtMediaPathMediaSizeUnit = _PrtMediaPathMediaSizeUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 3),
    _PrtMediaPathMediaSizeUnit_Type()
)
prtMediaPathMediaSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMediaSizeUnit.setStatus("current")


class _PrtMediaPathMaxSpeed_Type(Integer32):
    """Custom type prtMediaPathMaxSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMaxSpeed_Type.__name__ = "Integer32"
_PrtMediaPathMaxSpeed_Object = MibTableColumn
prtMediaPathMaxSpeed = _PrtMediaPathMaxSpeed_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 4),
    _PrtMediaPathMaxSpeed_Type()
)
prtMediaPathMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMaxSpeed.setStatus("current")


class _PrtMediaPathMaxMediaFeedDir_Type(Integer32):
    """Custom type prtMediaPathMaxMediaFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMaxMediaFeedDir_Type.__name__ = "Integer32"
_PrtMediaPathMaxMediaFeedDir_Object = MibTableColumn
prtMediaPathMaxMediaFeedDir = _PrtMediaPathMaxMediaFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 5),
    _PrtMediaPathMaxMediaFeedDir_Type()
)
prtMediaPathMaxMediaFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMaxMediaFeedDir.setStatus("current")


class _PrtMediaPathMaxMediaXFeedDir_Type(Integer32):
    """Custom type prtMediaPathMaxMediaXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMaxMediaXFeedDir_Type.__name__ = "Integer32"
_PrtMediaPathMaxMediaXFeedDir_Object = MibTableColumn
prtMediaPathMaxMediaXFeedDir = _PrtMediaPathMaxMediaXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 6),
    _PrtMediaPathMaxMediaXFeedDir_Type()
)
prtMediaPathMaxMediaXFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMaxMediaXFeedDir.setStatus("current")


class _PrtMediaPathMinMediaFeedDir_Type(Integer32):
    """Custom type prtMediaPathMinMediaFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMinMediaFeedDir_Type.__name__ = "Integer32"
_PrtMediaPathMinMediaFeedDir_Object = MibTableColumn
prtMediaPathMinMediaFeedDir = _PrtMediaPathMinMediaFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 7),
    _PrtMediaPathMinMediaFeedDir_Type()
)
prtMediaPathMinMediaFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMinMediaFeedDir.setStatus("current")


class _PrtMediaPathMinMediaXFeedDir_Type(Integer32):
    """Custom type prtMediaPathMinMediaXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMinMediaXFeedDir_Type.__name__ = "Integer32"
_PrtMediaPathMinMediaXFeedDir_Object = MibTableColumn
prtMediaPathMinMediaXFeedDir = _PrtMediaPathMinMediaXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 8),
    _PrtMediaPathMinMediaXFeedDir_Type()
)
prtMediaPathMinMediaXFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMinMediaXFeedDir.setStatus("current")
_PrtMediaPathType_Type = PrtMediaPathTypeTC
_PrtMediaPathType_Object = MibTableColumn
prtMediaPathType = _PrtMediaPathType_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 9),
    _PrtMediaPathType_Type()
)
prtMediaPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathType.setStatus("current")
_PrtMediaPathDescription_Type = PrtLocalizedDescriptionStringTC
_PrtMediaPathDescription_Object = MibTableColumn
prtMediaPathDescription = _PrtMediaPathDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 10),
    _PrtMediaPathDescription_Type()
)
prtMediaPathDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathDescription.setStatus("current")
_PrtMediaPathStatus_Type = PrtSubUnitStatusTC
_PrtMediaPathStatus_Object = MibTableColumn
prtMediaPathStatus = _PrtMediaPathStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 11),
    _PrtMediaPathStatus_Type()
)
prtMediaPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathStatus.setStatus("current")
_PrtChannel_ObjectIdentity = ObjectIdentity
prtChannel = _PrtChannel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 14)
)
_PrtChannelTable_Object = MibTable
prtChannelTable = _PrtChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1)
)
if mibBuilder.loadTexts:
    prtChannelTable.setStatus("current")
_PrtChannelEntry_Object = MibTableRow
prtChannelEntry = _PrtChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1)
)
prtChannelEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtChannelIndex"),
)
if mibBuilder.loadTexts:
    prtChannelEntry.setStatus("current")


class _PrtChannelIndex_Type(Integer32):
    """Custom type prtChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtChannelIndex_Type.__name__ = "Integer32"
_PrtChannelIndex_Object = MibTableColumn
prtChannelIndex = _PrtChannelIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 1),
    _PrtChannelIndex_Type()
)
prtChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtChannelIndex.setStatus("current")
_PrtChannelType_Type = PrtChannelTypeTC
_PrtChannelType_Object = MibTableColumn
prtChannelType = _PrtChannelType_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 2),
    _PrtChannelType_Type()
)
prtChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtChannelType.setStatus("current")


class _PrtChannelProtocolVersion_Type(OctetString):
    """Custom type prtChannelProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtChannelProtocolVersion_Type.__name__ = "OctetString"
_PrtChannelProtocolVersion_Object = MibTableColumn
prtChannelProtocolVersion = _PrtChannelProtocolVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 3),
    _PrtChannelProtocolVersion_Type()
)
prtChannelProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtChannelProtocolVersion.setStatus("current")


class _PrtChannelCurrentJobCntlLangIndex_Type(Integer32):
    """Custom type prtChannelCurrentJobCntlLangIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtChannelCurrentJobCntlLangIndex_Type.__name__ = "Integer32"
_PrtChannelCurrentJobCntlLangIndex_Object = MibTableColumn
prtChannelCurrentJobCntlLangIndex = _PrtChannelCurrentJobCntlLangIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 4),
    _PrtChannelCurrentJobCntlLangIndex_Type()
)
prtChannelCurrentJobCntlLangIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtChannelCurrentJobCntlLangIndex.setStatus("current")


class _PrtChannelDefaultPageDescLangIndex_Type(Integer32):
    """Custom type prtChannelDefaultPageDescLangIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtChannelDefaultPageDescLangIndex_Type.__name__ = "Integer32"
_PrtChannelDefaultPageDescLangIndex_Object = MibTableColumn
prtChannelDefaultPageDescLangIndex = _PrtChannelDefaultPageDescLangIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 5),
    _PrtChannelDefaultPageDescLangIndex_Type()
)
prtChannelDefaultPageDescLangIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtChannelDefaultPageDescLangIndex.setStatus("current")
_PrtChannelState_Type = PrtChannelStateTC
_PrtChannelState_Object = MibTableColumn
prtChannelState = _PrtChannelState_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 6),
    _PrtChannelState_Type()
)
prtChannelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtChannelState.setStatus("current")
_PrtChannelIfIndex_Type = InterfaceIndexOrZero
_PrtChannelIfIndex_Object = MibTableColumn
prtChannelIfIndex = _PrtChannelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 7),
    _PrtChannelIfIndex_Type()
)
prtChannelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtChannelIfIndex.setStatus("current")
_PrtChannelStatus_Type = PrtSubUnitStatusTC
_PrtChannelStatus_Object = MibTableColumn
prtChannelStatus = _PrtChannelStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 8),
    _PrtChannelStatus_Type()
)
prtChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtChannelStatus.setStatus("current")


class _PrtChannelInformation_Type(OctetString):
    """Custom type prtChannelInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtChannelInformation_Type.__name__ = "OctetString"
_PrtChannelInformation_Object = MibTableColumn
prtChannelInformation = _PrtChannelInformation_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 9),
    _PrtChannelInformation_Type()
)
prtChannelInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtChannelInformation.setStatus("current")
_PrtInterpreter_ObjectIdentity = ObjectIdentity
prtInterpreter = _PrtInterpreter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 15)
)
_PrtInterpreterTable_Object = MibTable
prtInterpreterTable = _PrtInterpreterTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1)
)
if mibBuilder.loadTexts:
    prtInterpreterTable.setStatus("current")
_PrtInterpreterEntry_Object = MibTableRow
prtInterpreterEntry = _PrtInterpreterEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1)
)
prtInterpreterEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtInterpreterIndex"),
)
if mibBuilder.loadTexts:
    prtInterpreterEntry.setStatus("current")


class _PrtInterpreterIndex_Type(Integer32):
    """Custom type prtInterpreterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtInterpreterIndex_Type.__name__ = "Integer32"
_PrtInterpreterIndex_Object = MibTableColumn
prtInterpreterIndex = _PrtInterpreterIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 1),
    _PrtInterpreterIndex_Type()
)
prtInterpreterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtInterpreterIndex.setStatus("current")
_PrtInterpreterLangFamily_Type = PrtInterpreterLangFamilyTC
_PrtInterpreterLangFamily_Object = MibTableColumn
prtInterpreterLangFamily = _PrtInterpreterLangFamily_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 2),
    _PrtInterpreterLangFamily_Type()
)
prtInterpreterLangFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterLangFamily.setStatus("current")


class _PrtInterpreterLangLevel_Type(OctetString):
    """Custom type prtInterpreterLangLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PrtInterpreterLangLevel_Type.__name__ = "OctetString"
_PrtInterpreterLangLevel_Object = MibTableColumn
prtInterpreterLangLevel = _PrtInterpreterLangLevel_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 3),
    _PrtInterpreterLangLevel_Type()
)
prtInterpreterLangLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterLangLevel.setStatus("current")


class _PrtInterpreterLangVersion_Type(OctetString):
    """Custom type prtInterpreterLangVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PrtInterpreterLangVersion_Type.__name__ = "OctetString"
_PrtInterpreterLangVersion_Object = MibTableColumn
prtInterpreterLangVersion = _PrtInterpreterLangVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 4),
    _PrtInterpreterLangVersion_Type()
)
prtInterpreterLangVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterLangVersion.setStatus("current")
_PrtInterpreterDescription_Type = PrtLocalizedDescriptionStringTC
_PrtInterpreterDescription_Object = MibTableColumn
prtInterpreterDescription = _PrtInterpreterDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 5),
    _PrtInterpreterDescription_Type()
)
prtInterpreterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterDescription.setStatus("current")


class _PrtInterpreterVersion_Type(OctetString):
    """Custom type prtInterpreterVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PrtInterpreterVersion_Type.__name__ = "OctetString"
_PrtInterpreterVersion_Object = MibTableColumn
prtInterpreterVersion = _PrtInterpreterVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 6),
    _PrtInterpreterVersion_Type()
)
prtInterpreterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterVersion.setStatus("current")
_PrtInterpreterDefaultOrientation_Type = PrtPrintOrientationTC
_PrtInterpreterDefaultOrientation_Object = MibTableColumn
prtInterpreterDefaultOrientation = _PrtInterpreterDefaultOrientation_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 7),
    _PrtInterpreterDefaultOrientation_Type()
)
prtInterpreterDefaultOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInterpreterDefaultOrientation.setStatus("current")


class _PrtInterpreterFeedAddressability_Type(Integer32):
    """Custom type prtInterpreterFeedAddressability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInterpreterFeedAddressability_Type.__name__ = "Integer32"
_PrtInterpreterFeedAddressability_Object = MibTableColumn
prtInterpreterFeedAddressability = _PrtInterpreterFeedAddressability_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 8),
    _PrtInterpreterFeedAddressability_Type()
)
prtInterpreterFeedAddressability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterFeedAddressability.setStatus("current")


class _PrtInterpreterXFeedAddressability_Type(Integer32):
    """Custom type prtInterpreterXFeedAddressability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInterpreterXFeedAddressability_Type.__name__ = "Integer32"
_PrtInterpreterXFeedAddressability_Object = MibTableColumn
prtInterpreterXFeedAddressability = _PrtInterpreterXFeedAddressability_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 9),
    _PrtInterpreterXFeedAddressability_Type()
)
prtInterpreterXFeedAddressability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterXFeedAddressability.setStatus("current")
_PrtInterpreterDefaultCharSetIn_Type = IANACharset
_PrtInterpreterDefaultCharSetIn_Object = MibTableColumn
prtInterpreterDefaultCharSetIn = _PrtInterpreterDefaultCharSetIn_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 10),
    _PrtInterpreterDefaultCharSetIn_Type()
)
prtInterpreterDefaultCharSetIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInterpreterDefaultCharSetIn.setStatus("current")
_PrtInterpreterDefaultCharSetOut_Type = IANACharset
_PrtInterpreterDefaultCharSetOut_Object = MibTableColumn
prtInterpreterDefaultCharSetOut = _PrtInterpreterDefaultCharSetOut_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 11),
    _PrtInterpreterDefaultCharSetOut_Type()
)
prtInterpreterDefaultCharSetOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInterpreterDefaultCharSetOut.setStatus("current")
_PrtInterpreterTwoWay_Type = PrtInterpreterTwoWayTC
_PrtInterpreterTwoWay_Object = MibTableColumn
prtInterpreterTwoWay = _PrtInterpreterTwoWay_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 12),
    _PrtInterpreterTwoWay_Type()
)
prtInterpreterTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterTwoWay.setStatus("current")
_PrtConsoleDisplayBuffer_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBuffer = _PrtConsoleDisplayBuffer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 16)
)
_PrtConsoleDisplayBufferTable_Object = MibTable
prtConsoleDisplayBufferTable = _PrtConsoleDisplayBufferTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 16, 5)
)
if mibBuilder.loadTexts:
    prtConsoleDisplayBufferTable.setStatus("current")
_PrtConsoleDisplayBufferEntry_Object = MibTableRow
prtConsoleDisplayBufferEntry = _PrtConsoleDisplayBufferEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 16, 5, 1)
)
prtConsoleDisplayBufferEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtConsoleDisplayBufferIndex"),
)
if mibBuilder.loadTexts:
    prtConsoleDisplayBufferEntry.setStatus("current")


class _PrtConsoleDisplayBufferIndex_Type(Integer32):
    """Custom type prtConsoleDisplayBufferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtConsoleDisplayBufferIndex_Type.__name__ = "Integer32"
_PrtConsoleDisplayBufferIndex_Object = MibTableColumn
prtConsoleDisplayBufferIndex = _PrtConsoleDisplayBufferIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 16, 5, 1, 1),
    _PrtConsoleDisplayBufferIndex_Type()
)
prtConsoleDisplayBufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtConsoleDisplayBufferIndex.setStatus("current")
_PrtConsoleDisplayBufferText_Type = PrtConsoleDescriptionStringTC
_PrtConsoleDisplayBufferText_Object = MibTableColumn
prtConsoleDisplayBufferText = _PrtConsoleDisplayBufferText_Object(
    (1, 3, 6, 1, 2, 1, 43, 16, 5, 1, 2),
    _PrtConsoleDisplayBufferText_Type()
)
prtConsoleDisplayBufferText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtConsoleDisplayBufferText.setStatus("current")
_PrtConsoleLights_ObjectIdentity = ObjectIdentity
prtConsoleLights = _PrtConsoleLights_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 17)
)
_PrtConsoleLightTable_Object = MibTable
prtConsoleLightTable = _PrtConsoleLightTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 17, 6)
)
if mibBuilder.loadTexts:
    prtConsoleLightTable.setStatus("current")
_PrtConsoleLightEntry_Object = MibTableRow
prtConsoleLightEntry = _PrtConsoleLightEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 17, 6, 1)
)
prtConsoleLightEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtConsoleLightIndex"),
)
if mibBuilder.loadTexts:
    prtConsoleLightEntry.setStatus("current")


class _PrtConsoleLightIndex_Type(Integer32):
    """Custom type prtConsoleLightIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtConsoleLightIndex_Type.__name__ = "Integer32"
_PrtConsoleLightIndex_Object = MibTableColumn
prtConsoleLightIndex = _PrtConsoleLightIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 17, 6, 1, 1),
    _PrtConsoleLightIndex_Type()
)
prtConsoleLightIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtConsoleLightIndex.setStatus("current")


class _PrtConsoleOnTime_Type(Integer32):
    """Custom type prtConsoleOnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrtConsoleOnTime_Type.__name__ = "Integer32"
_PrtConsoleOnTime_Object = MibTableColumn
prtConsoleOnTime = _PrtConsoleOnTime_Object(
    (1, 3, 6, 1, 2, 1, 43, 17, 6, 1, 2),
    _PrtConsoleOnTime_Type()
)
prtConsoleOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtConsoleOnTime.setStatus("current")


class _PrtConsoleOffTime_Type(Integer32):
    """Custom type prtConsoleOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrtConsoleOffTime_Type.__name__ = "Integer32"
_PrtConsoleOffTime_Object = MibTableColumn
prtConsoleOffTime = _PrtConsoleOffTime_Object(
    (1, 3, 6, 1, 2, 1, 43, 17, 6, 1, 3),
    _PrtConsoleOffTime_Type()
)
prtConsoleOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtConsoleOffTime.setStatus("current")
_PrtConsoleColor_Type = PrtConsoleColorTC
_PrtConsoleColor_Object = MibTableColumn
prtConsoleColor = _PrtConsoleColor_Object(
    (1, 3, 6, 1, 2, 1, 43, 17, 6, 1, 4),
    _PrtConsoleColor_Type()
)
prtConsoleColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtConsoleColor.setStatus("current")
_PrtConsoleDescription_Type = PrtConsoleDescriptionStringTC
_PrtConsoleDescription_Object = MibTableColumn
prtConsoleDescription = _PrtConsoleDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 17, 6, 1, 5),
    _PrtConsoleDescription_Type()
)
prtConsoleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtConsoleDescription.setStatus("current")
_PrtAlert_ObjectIdentity = ObjectIdentity
prtAlert = _PrtAlert_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 18)
)
_PrtAlertTable_Object = MibTable
prtAlertTable = _PrtAlertTable_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1)
)
if mibBuilder.loadTexts:
    prtAlertTable.setStatus("current")
_PrtAlertEntry_Object = MibTableRow
prtAlertEntry = _PrtAlertEntry_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1)
)
prtAlertEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtAlertIndex"),
)
if mibBuilder.loadTexts:
    prtAlertEntry.setStatus("current")


class _PrtAlertIndex_Type(Integer32):
    """Custom type prtAlertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PrtAlertIndex_Type.__name__ = "Integer32"
_PrtAlertIndex_Object = MibTableColumn
prtAlertIndex = _PrtAlertIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1, 1),
    _PrtAlertIndex_Type()
)
prtAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertIndex.setStatus("current")
_PrtAlertSeverityLevel_Type = PrtAlertSeverityLevelTC
_PrtAlertSeverityLevel_Object = MibTableColumn
prtAlertSeverityLevel = _PrtAlertSeverityLevel_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1, 2),
    _PrtAlertSeverityLevel_Type()
)
prtAlertSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertSeverityLevel.setStatus("current")
_PrtAlertTrainingLevel_Type = PrtAlertTrainingLevelTC
_PrtAlertTrainingLevel_Object = MibTableColumn
prtAlertTrainingLevel = _PrtAlertTrainingLevel_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1, 3),
    _PrtAlertTrainingLevel_Type()
)
prtAlertTrainingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertTrainingLevel.setStatus("current")
_PrtAlertGroup_Type = PrtAlertGroupTC
_PrtAlertGroup_Object = MibTableColumn
prtAlertGroup = _PrtAlertGroup_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1, 4),
    _PrtAlertGroup_Type()
)
prtAlertGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertGroup.setStatus("current")


class _PrtAlertGroupIndex_Type(Integer32):
    """Custom type prtAlertGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_PrtAlertGroupIndex_Type.__name__ = "Integer32"
_PrtAlertGroupIndex_Object = MibTableColumn
prtAlertGroupIndex = _PrtAlertGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1, 5),
    _PrtAlertGroupIndex_Type()
)
prtAlertGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertGroupIndex.setStatus("current")


class _PrtAlertLocation_Type(Integer32):
    """Custom type prtAlertLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtAlertLocation_Type.__name__ = "Integer32"
_PrtAlertLocation_Object = MibTableColumn
prtAlertLocation = _PrtAlertLocation_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1, 6),
    _PrtAlertLocation_Type()
)
prtAlertLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertLocation.setStatus("current")
_PrtAlertCode_Type = PrtAlertCodeTC
_PrtAlertCode_Object = MibTableColumn
prtAlertCode = _PrtAlertCode_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1, 7),
    _PrtAlertCode_Type()
)
prtAlertCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertCode.setStatus("current")
_PrtAlertDescription_Type = PrtLocalizedDescriptionStringTC
_PrtAlertDescription_Object = MibTableColumn
prtAlertDescription = _PrtAlertDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1, 8),
    _PrtAlertDescription_Type()
)
prtAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertDescription.setStatus("current")
_PrtAlertTime_Type = TimeTicks
_PrtAlertTime_Object = MibTableColumn
prtAlertTime = _PrtAlertTime_Object(
    (1, 3, 6, 1, 2, 1, 43, 18, 1, 1, 9),
    _PrtAlertTime_Type()
)
prtAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlertTime.setStatus("current")
_PrinterV1Alert_ObjectIdentity = ObjectIdentity
printerV1Alert = _PrinterV1Alert_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 18, 2)
)
if mibBuilder.loadTexts:
    printerV1Alert.setStatus("current")
_PrinterV2AlertPrefix_ObjectIdentity = ObjectIdentity
printerV2AlertPrefix = _PrinterV2AlertPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 18, 2, 0)
)

# Managed Objects groups

prtGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 1)
)
prtGeneralGroup.setObjects(
      *(("Printer-MIB", "prtGeneralConfigChanges"),
        ("Printer-MIB", "prtGeneralCurrentLocalization"),
        ("Printer-MIB", "prtGeneralReset"),
        ("Printer-MIB", "prtCoverDescription"),
        ("Printer-MIB", "prtCoverStatus"),
        ("Printer-MIB", "prtLocalizationLanguage"),
        ("Printer-MIB", "prtLocalizationCountry"),
        ("Printer-MIB", "prtLocalizationCharacterSet"),
        ("Printer-MIB", "prtStorageRefIndex"),
        ("Printer-MIB", "prtDeviceRefIndex"))
)
if mibBuilder.loadTexts:
    prtGeneralGroup.setStatus("current")

prtResponsiblePartyGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 2)
)
prtResponsiblePartyGroup.setObjects(
      *(("Printer-MIB", "prtGeneralCurrentOperator"),
        ("Printer-MIB", "prtGeneralServicePerson"))
)
if mibBuilder.loadTexts:
    prtResponsiblePartyGroup.setStatus("current")

prtInputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 3)
)
prtInputGroup.setObjects(
      *(("Printer-MIB", "prtInputDefaultIndex"),
        ("Printer-MIB", "prtInputType"),
        ("Printer-MIB", "prtInputDimUnit"),
        ("Printer-MIB", "prtInputMediaDimFeedDirDeclared"),
        ("Printer-MIB", "prtInputMediaDimXFeedDirDeclared"),
        ("Printer-MIB", "prtInputMediaDimFeedDirChosen"),
        ("Printer-MIB", "prtInputMediaDimXFeedDirChosen"),
        ("Printer-MIB", "prtInputCapacityUnit"),
        ("Printer-MIB", "prtInputMaxCapacity"),
        ("Printer-MIB", "prtInputCurrentLevel"),
        ("Printer-MIB", "prtInputStatus"),
        ("Printer-MIB", "prtInputMediaName"))
)
if mibBuilder.loadTexts:
    prtInputGroup.setStatus("current")

prtExtendedInputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 4)
)
prtExtendedInputGroup.setObjects(
      *(("Printer-MIB", "prtInputName"),
        ("Printer-MIB", "prtInputVendorName"),
        ("Printer-MIB", "prtInputModel"),
        ("Printer-MIB", "prtInputVersion"),
        ("Printer-MIB", "prtInputSerialNumber"),
        ("Printer-MIB", "prtInputDescription"),
        ("Printer-MIB", "prtInputSecurity"))
)
if mibBuilder.loadTexts:
    prtExtendedInputGroup.setStatus("current")

prtInputMediaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 5)
)
prtInputMediaGroup.setObjects(
      *(("Printer-MIB", "prtInputMediaWeight"),
        ("Printer-MIB", "prtInputMediaType"),
        ("Printer-MIB", "prtInputMediaColor"),
        ("Printer-MIB", "prtInputMediaFormParts"))
)
if mibBuilder.loadTexts:
    prtInputMediaGroup.setStatus("current")

prtOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 6)
)
prtOutputGroup.setObjects(
      *(("Printer-MIB", "prtOutputDefaultIndex"),
        ("Printer-MIB", "prtOutputType"),
        ("Printer-MIB", "prtOutputCapacityUnit"),
        ("Printer-MIB", "prtOutputMaxCapacity"),
        ("Printer-MIB", "prtOutputRemainingCapacity"),
        ("Printer-MIB", "prtOutputStatus"))
)
if mibBuilder.loadTexts:
    prtOutputGroup.setStatus("current")

prtExtendedOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 7)
)
prtExtendedOutputGroup.setObjects(
      *(("Printer-MIB", "prtOutputName"),
        ("Printer-MIB", "prtOutputVendorName"),
        ("Printer-MIB", "prtOutputModel"),
        ("Printer-MIB", "prtOutputVersion"),
        ("Printer-MIB", "prtOutputSerialNumber"),
        ("Printer-MIB", "prtOutputDescription"),
        ("Printer-MIB", "prtOutputSecurity"))
)
if mibBuilder.loadTexts:
    prtExtendedOutputGroup.setStatus("current")

prtOutputDimensionsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 8)
)
prtOutputDimensionsGroup.setObjects(
      *(("Printer-MIB", "prtOutputDimUnit"),
        ("Printer-MIB", "prtOutputMaxDimFeedDir"),
        ("Printer-MIB", "prtOutputMaxDimXFeedDir"),
        ("Printer-MIB", "prtOutputMinDimFeedDir"),
        ("Printer-MIB", "prtOutputMinDimXFeedDir"))
)
if mibBuilder.loadTexts:
    prtOutputDimensionsGroup.setStatus("current")

prtOutputFeaturesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 9)
)
prtOutputFeaturesGroup.setObjects(
      *(("Printer-MIB", "prtOutputStackingOrder"),
        ("Printer-MIB", "prtOutputPageDeliveryOrientation"),
        ("Printer-MIB", "prtOutputBursting"),
        ("Printer-MIB", "prtOutputDecollating"),
        ("Printer-MIB", "prtOutputPageCollated"),
        ("Printer-MIB", "prtOutputOffsetStacking"))
)
if mibBuilder.loadTexts:
    prtOutputFeaturesGroup.setStatus("current")

prtMarkerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 10)
)
prtMarkerGroup.setObjects(
      *(("Printer-MIB", "prtMarkerDefaultIndex"),
        ("Printer-MIB", "prtMarkerMarkTech"),
        ("Printer-MIB", "prtMarkerCounterUnit"),
        ("Printer-MIB", "prtMarkerLifeCount"),
        ("Printer-MIB", "prtMarkerPowerOnCount"),
        ("Printer-MIB", "prtMarkerProcessColorants"),
        ("Printer-MIB", "prtMarkerSpotColorants"),
        ("Printer-MIB", "prtMarkerAddressabilityUnit"),
        ("Printer-MIB", "prtMarkerAddressabilityFeedDir"),
        ("Printer-MIB", "prtMarkerAddressabilityXFeedDir"),
        ("Printer-MIB", "prtMarkerNorthMargin"),
        ("Printer-MIB", "prtMarkerSouthMargin"),
        ("Printer-MIB", "prtMarkerWestMargin"),
        ("Printer-MIB", "prtMarkerEastMargin"),
        ("Printer-MIB", "prtMarkerStatus"))
)
if mibBuilder.loadTexts:
    prtMarkerGroup.setStatus("current")

prtMarkerSuppliesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 11)
)
prtMarkerSuppliesGroup.setObjects(
      *(("Printer-MIB", "prtMarkerSuppliesMarkerIndex"),
        ("Printer-MIB", "prtMarkerSuppliesColorantIndex"),
        ("Printer-MIB", "prtMarkerSuppliesClass"),
        ("Printer-MIB", "prtMarkerSuppliesType"),
        ("Printer-MIB", "prtMarkerSuppliesDescription"),
        ("Printer-MIB", "prtMarkerSuppliesSupplyUnit"),
        ("Printer-MIB", "prtMarkerSuppliesMaxCapacity"),
        ("Printer-MIB", "prtMarkerSuppliesLevel"))
)
if mibBuilder.loadTexts:
    prtMarkerSuppliesGroup.setStatus("current")

prtMarkerColorantGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 12)
)
prtMarkerColorantGroup.setObjects(
      *(("Printer-MIB", "prtMarkerColorantMarkerIndex"),
        ("Printer-MIB", "prtMarkerColorantRole"),
        ("Printer-MIB", "prtMarkerColorantValue"),
        ("Printer-MIB", "prtMarkerColorantTonality"))
)
if mibBuilder.loadTexts:
    prtMarkerColorantGroup.setStatus("current")

prtMediaPathGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 13)
)
prtMediaPathGroup.setObjects(
      *(("Printer-MIB", "prtMediaPathDefaultIndex"),
        ("Printer-MIB", "prtMediaPathMaxSpeedPrintUnit"),
        ("Printer-MIB", "prtMediaPathMediaSizeUnit"),
        ("Printer-MIB", "prtMediaPathMaxSpeed"),
        ("Printer-MIB", "prtMediaPathMaxMediaFeedDir"),
        ("Printer-MIB", "prtMediaPathMaxMediaXFeedDir"),
        ("Printer-MIB", "prtMediaPathMinMediaFeedDir"),
        ("Printer-MIB", "prtMediaPathMinMediaXFeedDir"),
        ("Printer-MIB", "prtMediaPathType"),
        ("Printer-MIB", "prtMediaPathDescription"),
        ("Printer-MIB", "prtMediaPathStatus"))
)
if mibBuilder.loadTexts:
    prtMediaPathGroup.setStatus("current")

prtChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 14)
)
prtChannelGroup.setObjects(
      *(("Printer-MIB", "prtChannelType"),
        ("Printer-MIB", "prtChannelProtocolVersion"),
        ("Printer-MIB", "prtChannelCurrentJobCntlLangIndex"),
        ("Printer-MIB", "prtChannelDefaultPageDescLangIndex"),
        ("Printer-MIB", "prtChannelState"),
        ("Printer-MIB", "prtChannelIfIndex"),
        ("Printer-MIB", "prtChannelStatus"))
)
if mibBuilder.loadTexts:
    prtChannelGroup.setStatus("current")

prtInterpreterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 15)
)
prtInterpreterGroup.setObjects(
      *(("Printer-MIB", "prtInterpreterLangFamily"),
        ("Printer-MIB", "prtInterpreterLangLevel"),
        ("Printer-MIB", "prtInterpreterLangVersion"),
        ("Printer-MIB", "prtInterpreterDescription"),
        ("Printer-MIB", "prtInterpreterVersion"),
        ("Printer-MIB", "prtInterpreterDefaultOrientation"),
        ("Printer-MIB", "prtInterpreterFeedAddressability"),
        ("Printer-MIB", "prtInterpreterXFeedAddressability"),
        ("Printer-MIB", "prtInterpreterDefaultCharSetIn"),
        ("Printer-MIB", "prtInterpreterDefaultCharSetOut"),
        ("Printer-MIB", "prtInterpreterTwoWay"))
)
if mibBuilder.loadTexts:
    prtInterpreterGroup.setStatus("current")

prtConsoleGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 16)
)
prtConsoleGroup.setObjects(
      *(("Printer-MIB", "prtConsoleLocalization"),
        ("Printer-MIB", "prtConsoleNumberOfDisplayLines"),
        ("Printer-MIB", "prtConsoleNumberOfDisplayChars"),
        ("Printer-MIB", "prtConsoleDisable"),
        ("Printer-MIB", "prtConsoleDisplayBufferText"),
        ("Printer-MIB", "prtConsoleOnTime"),
        ("Printer-MIB", "prtConsoleOffTime"),
        ("Printer-MIB", "prtConsoleColor"),
        ("Printer-MIB", "prtConsoleDescription"))
)
if mibBuilder.loadTexts:
    prtConsoleGroup.setStatus("current")

prtAlertTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 17)
)
prtAlertTableGroup.setObjects(
      *(("Printer-MIB", "prtAlertSeverityLevel"),
        ("Printer-MIB", "prtAlertTrainingLevel"),
        ("Printer-MIB", "prtAlertGroup"),
        ("Printer-MIB", "prtAlertGroupIndex"),
        ("Printer-MIB", "prtAlertLocation"),
        ("Printer-MIB", "prtAlertCode"),
        ("Printer-MIB", "prtAlertDescription"))
)
if mibBuilder.loadTexts:
    prtAlertTableGroup.setStatus("current")

prtAlertTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 18)
)
prtAlertTimeGroup.setObjects(
    ("Printer-MIB", "prtAlertTime")
)
if mibBuilder.loadTexts:
    prtAlertTimeGroup.setStatus("current")

prtAuxiliarySheetGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 19)
)
prtAuxiliarySheetGroup.setObjects(
      *(("Printer-MIB", "prtAuxiliarySheetStartupPage"),
        ("Printer-MIB", "prtAuxiliarySheetBannerPage"))
)
if mibBuilder.loadTexts:
    prtAuxiliarySheetGroup.setStatus("current")

prtInputSwitchingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 20)
)
prtInputSwitchingGroup.setObjects(
      *(("Printer-MIB", "prtInputMediaLoadTimeout"),
        ("Printer-MIB", "prtInputNextIndex"))
)
if mibBuilder.loadTexts:
    prtInputSwitchingGroup.setStatus("current")

prtGeneralV2Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 21)
)
prtGeneralV2Group.setObjects(
      *(("Printer-MIB", "prtGeneralPrinterName"),
        ("Printer-MIB", "prtGeneralSerialNumber"))
)
if mibBuilder.loadTexts:
    prtGeneralV2Group.setStatus("current")

prtAlertTableV2Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 22)
)
prtAlertTableV2Group.setObjects(
      *(("Printer-MIB", "prtAlertIndex"),
        ("Printer-MIB", "prtAlertCriticalEvents"),
        ("Printer-MIB", "prtAlertAllEvents"))
)
if mibBuilder.loadTexts:
    prtAlertTableV2Group.setStatus("current")

prtChannelV2Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 23)
)
prtChannelV2Group.setObjects(
    ("Printer-MIB", "prtChannelInformation")
)
if mibBuilder.loadTexts:
    prtChannelV2Group.setStatus("current")


# Notification objects

printerV2Alert = NotificationType(
    (1, 3, 6, 1, 2, 1, 43, 18, 2, 0, 1)
)
printerV2Alert.setObjects(
      *(("Printer-MIB", "prtAlertIndex"),
        ("Printer-MIB", "prtAlertSeverityLevel"),
        ("Printer-MIB", "prtAlertGroup"),
        ("Printer-MIB", "prtAlertGroupIndex"),
        ("Printer-MIB", "prtAlertLocation"),
        ("Printer-MIB", "prtAlertCode"))
)
if mibBuilder.loadTexts:
    printerV2Alert.setStatus(
        "current"
    )


# Notifications groups

prtAlertTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 43, 2, 2, 24)
)
prtAlertTrapGroup.setObjects(
    ("Printer-MIB", "printerV2Alert")
)
if mibBuilder.loadTexts:
    prtAlertTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 43, 2, 1)
)
if mibBuilder.loadTexts:
    prtMIBCompliance.setStatus(
        "current"
    )

prtMIB2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 43, 2, 3)
)
if mibBuilder.loadTexts:
    prtMIB2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Printer-MIB",
    **{"PrtMediaUnitTC": PrtMediaUnitTC,
       "MediaUnit": MediaUnit,
       "PrtCapacityUnitTC": PrtCapacityUnitTC,
       "CapacityUnit": CapacityUnit,
       "PrtPrintOrientationTC": PrtPrintOrientationTC,
       "PrtSubUnitStatusTC": PrtSubUnitStatusTC,
       "SubUnitStatus": SubUnitStatus,
       "PresentOnOff": PresentOnOff,
       "PrtLocalizedDescriptionStringTC": PrtLocalizedDescriptionStringTC,
       "PrtConsoleDescriptionStringTC": PrtConsoleDescriptionStringTC,
       "CodedCharSet": CodedCharSet,
       "PrtChannelStateTC": PrtChannelStateTC,
       "PrtOutputStackingOrderTC": PrtOutputStackingOrderTC,
       "PrtOutputPageDeliveryOrientationTC": PrtOutputPageDeliveryOrientationTC,
       "PrtMarkerCounterUnitTC": PrtMarkerCounterUnitTC,
       "PrtMarkerSuppliesSupplyUnitTC": PrtMarkerSuppliesSupplyUnitTC,
       "PrtMarkerSuppliesClassTC": PrtMarkerSuppliesClassTC,
       "PrtMarkerColorantRoleTC": PrtMarkerColorantRoleTC,
       "PrtMarkerAddressabilityUnitTC": PrtMarkerAddressabilityUnitTC,
       "PrtMediaPathMaxSpeedPrintUnitTC": PrtMediaPathMaxSpeedPrintUnitTC,
       "PrtInterpreterTwoWayTC": PrtInterpreterTwoWayTC,
       "PrtAlertSeverityLevelTC": PrtAlertSeverityLevelTC,
       "printmib": printmib,
       "prtMIBConformance": prtMIBConformance,
       "prtMIBCompliance": prtMIBCompliance,
       "prtMIBGroups": prtMIBGroups,
       "prtGeneralGroup": prtGeneralGroup,
       "prtResponsiblePartyGroup": prtResponsiblePartyGroup,
       "prtInputGroup": prtInputGroup,
       "prtExtendedInputGroup": prtExtendedInputGroup,
       "prtInputMediaGroup": prtInputMediaGroup,
       "prtOutputGroup": prtOutputGroup,
       "prtExtendedOutputGroup": prtExtendedOutputGroup,
       "prtOutputDimensionsGroup": prtOutputDimensionsGroup,
       "prtOutputFeaturesGroup": prtOutputFeaturesGroup,
       "prtMarkerGroup": prtMarkerGroup,
       "prtMarkerSuppliesGroup": prtMarkerSuppliesGroup,
       "prtMarkerColorantGroup": prtMarkerColorantGroup,
       "prtMediaPathGroup": prtMediaPathGroup,
       "prtChannelGroup": prtChannelGroup,
       "prtInterpreterGroup": prtInterpreterGroup,
       "prtConsoleGroup": prtConsoleGroup,
       "prtAlertTableGroup": prtAlertTableGroup,
       "prtAlertTimeGroup": prtAlertTimeGroup,
       "prtAuxiliarySheetGroup": prtAuxiliarySheetGroup,
       "prtInputSwitchingGroup": prtInputSwitchingGroup,
       "prtGeneralV2Group": prtGeneralV2Group,
       "prtAlertTableV2Group": prtAlertTableV2Group,
       "prtChannelV2Group": prtChannelV2Group,
       "prtAlertTrapGroup": prtAlertTrapGroup,
       "prtMIB2Compliance": prtMIB2Compliance,
       "prtMIB2Groups": prtMIB2Groups,
       "prtGeneral": prtGeneral,
       "prtGeneralTable": prtGeneralTable,
       "prtGeneralEntry": prtGeneralEntry,
       "prtGeneralConfigChanges": prtGeneralConfigChanges,
       "prtGeneralCurrentLocalization": prtGeneralCurrentLocalization,
       "prtGeneralReset": prtGeneralReset,
       "prtGeneralCurrentOperator": prtGeneralCurrentOperator,
       "prtGeneralServicePerson": prtGeneralServicePerson,
       "prtInputDefaultIndex": prtInputDefaultIndex,
       "prtOutputDefaultIndex": prtOutputDefaultIndex,
       "prtMarkerDefaultIndex": prtMarkerDefaultIndex,
       "prtMediaPathDefaultIndex": prtMediaPathDefaultIndex,
       "prtConsoleLocalization": prtConsoleLocalization,
       "prtConsoleNumberOfDisplayLines": prtConsoleNumberOfDisplayLines,
       "prtConsoleNumberOfDisplayChars": prtConsoleNumberOfDisplayChars,
       "prtConsoleDisable": prtConsoleDisable,
       "prtAuxiliarySheetStartupPage": prtAuxiliarySheetStartupPage,
       "prtAuxiliarySheetBannerPage": prtAuxiliarySheetBannerPage,
       "prtGeneralPrinterName": prtGeneralPrinterName,
       "prtGeneralSerialNumber": prtGeneralSerialNumber,
       "prtAlertCriticalEvents": prtAlertCriticalEvents,
       "prtAlertAllEvents": prtAlertAllEvents,
       "prtStorageRefTable": prtStorageRefTable,
       "prtStorageRefEntry": prtStorageRefEntry,
       "prtStorageRefSeqNumber": prtStorageRefSeqNumber,
       "prtStorageRefIndex": prtStorageRefIndex,
       "prtDeviceRefTable": prtDeviceRefTable,
       "prtDeviceRefEntry": prtDeviceRefEntry,
       "prtDeviceRefSeqNumber": prtDeviceRefSeqNumber,
       "prtDeviceRefIndex": prtDeviceRefIndex,
       "prtCover": prtCover,
       "prtCoverTable": prtCoverTable,
       "prtCoverEntry": prtCoverEntry,
       "prtCoverIndex": prtCoverIndex,
       "prtCoverDescription": prtCoverDescription,
       "prtCoverStatus": prtCoverStatus,
       "prtLocalization": prtLocalization,
       "prtLocalizationTable": prtLocalizationTable,
       "prtLocalizationEntry": prtLocalizationEntry,
       "prtLocalizationIndex": prtLocalizationIndex,
       "prtLocalizationLanguage": prtLocalizationLanguage,
       "prtLocalizationCountry": prtLocalizationCountry,
       "prtLocalizationCharacterSet": prtLocalizationCharacterSet,
       "prtInput": prtInput,
       "prtInputTable": prtInputTable,
       "prtInputEntry": prtInputEntry,
       "prtInputIndex": prtInputIndex,
       "prtInputType": prtInputType,
       "prtInputDimUnit": prtInputDimUnit,
       "prtInputMediaDimFeedDirDeclared": prtInputMediaDimFeedDirDeclared,
       "prtInputMediaDimXFeedDirDeclared": prtInputMediaDimXFeedDirDeclared,
       "prtInputMediaDimFeedDirChosen": prtInputMediaDimFeedDirChosen,
       "prtInputMediaDimXFeedDirChosen": prtInputMediaDimXFeedDirChosen,
       "prtInputCapacityUnit": prtInputCapacityUnit,
       "prtInputMaxCapacity": prtInputMaxCapacity,
       "prtInputCurrentLevel": prtInputCurrentLevel,
       "prtInputStatus": prtInputStatus,
       "prtInputMediaName": prtInputMediaName,
       "prtInputName": prtInputName,
       "prtInputVendorName": prtInputVendorName,
       "prtInputModel": prtInputModel,
       "prtInputVersion": prtInputVersion,
       "prtInputSerialNumber": prtInputSerialNumber,
       "prtInputDescription": prtInputDescription,
       "prtInputSecurity": prtInputSecurity,
       "prtInputMediaWeight": prtInputMediaWeight,
       "prtInputMediaType": prtInputMediaType,
       "prtInputMediaColor": prtInputMediaColor,
       "prtInputMediaFormParts": prtInputMediaFormParts,
       "prtInputMediaLoadTimeout": prtInputMediaLoadTimeout,
       "prtInputNextIndex": prtInputNextIndex,
       "prtOutput": prtOutput,
       "prtOutputTable": prtOutputTable,
       "prtOutputEntry": prtOutputEntry,
       "prtOutputIndex": prtOutputIndex,
       "prtOutputType": prtOutputType,
       "prtOutputCapacityUnit": prtOutputCapacityUnit,
       "prtOutputMaxCapacity": prtOutputMaxCapacity,
       "prtOutputRemainingCapacity": prtOutputRemainingCapacity,
       "prtOutputStatus": prtOutputStatus,
       "prtOutputName": prtOutputName,
       "prtOutputVendorName": prtOutputVendorName,
       "prtOutputModel": prtOutputModel,
       "prtOutputVersion": prtOutputVersion,
       "prtOutputSerialNumber": prtOutputSerialNumber,
       "prtOutputDescription": prtOutputDescription,
       "prtOutputSecurity": prtOutputSecurity,
       "prtOutputDimUnit": prtOutputDimUnit,
       "prtOutputMaxDimFeedDir": prtOutputMaxDimFeedDir,
       "prtOutputMaxDimXFeedDir": prtOutputMaxDimXFeedDir,
       "prtOutputMinDimFeedDir": prtOutputMinDimFeedDir,
       "prtOutputMinDimXFeedDir": prtOutputMinDimXFeedDir,
       "prtOutputStackingOrder": prtOutputStackingOrder,
       "prtOutputPageDeliveryOrientation": prtOutputPageDeliveryOrientation,
       "prtOutputBursting": prtOutputBursting,
       "prtOutputDecollating": prtOutputDecollating,
       "prtOutputPageCollated": prtOutputPageCollated,
       "prtOutputOffsetStacking": prtOutputOffsetStacking,
       "prtMarker": prtMarker,
       "prtMarkerTable": prtMarkerTable,
       "prtMarkerEntry": prtMarkerEntry,
       "prtMarkerIndex": prtMarkerIndex,
       "prtMarkerMarkTech": prtMarkerMarkTech,
       "prtMarkerCounterUnit": prtMarkerCounterUnit,
       "prtMarkerLifeCount": prtMarkerLifeCount,
       "prtMarkerPowerOnCount": prtMarkerPowerOnCount,
       "prtMarkerProcessColorants": prtMarkerProcessColorants,
       "prtMarkerSpotColorants": prtMarkerSpotColorants,
       "prtMarkerAddressabilityUnit": prtMarkerAddressabilityUnit,
       "prtMarkerAddressabilityFeedDir": prtMarkerAddressabilityFeedDir,
       "prtMarkerAddressabilityXFeedDir": prtMarkerAddressabilityXFeedDir,
       "prtMarkerNorthMargin": prtMarkerNorthMargin,
       "prtMarkerSouthMargin": prtMarkerSouthMargin,
       "prtMarkerWestMargin": prtMarkerWestMargin,
       "prtMarkerEastMargin": prtMarkerEastMargin,
       "prtMarkerStatus": prtMarkerStatus,
       "prtMarkerSupplies": prtMarkerSupplies,
       "prtMarkerSuppliesTable": prtMarkerSuppliesTable,
       "prtMarkerSuppliesEntry": prtMarkerSuppliesEntry,
       "prtMarkerSuppliesIndex": prtMarkerSuppliesIndex,
       "prtMarkerSuppliesMarkerIndex": prtMarkerSuppliesMarkerIndex,
       "prtMarkerSuppliesColorantIndex": prtMarkerSuppliesColorantIndex,
       "prtMarkerSuppliesClass": prtMarkerSuppliesClass,
       "prtMarkerSuppliesType": prtMarkerSuppliesType,
       "prtMarkerSuppliesDescription": prtMarkerSuppliesDescription,
       "prtMarkerSuppliesSupplyUnit": prtMarkerSuppliesSupplyUnit,
       "prtMarkerSuppliesMaxCapacity": prtMarkerSuppliesMaxCapacity,
       "prtMarkerSuppliesLevel": prtMarkerSuppliesLevel,
       "prtMarkerColorant": prtMarkerColorant,
       "prtMarkerColorantTable": prtMarkerColorantTable,
       "prtMarkerColorantEntry": prtMarkerColorantEntry,
       "prtMarkerColorantIndex": prtMarkerColorantIndex,
       "prtMarkerColorantMarkerIndex": prtMarkerColorantMarkerIndex,
       "prtMarkerColorantRole": prtMarkerColorantRole,
       "prtMarkerColorantValue": prtMarkerColorantValue,
       "prtMarkerColorantTonality": prtMarkerColorantTonality,
       "prtMediaPath": prtMediaPath,
       "prtMediaPathTable": prtMediaPathTable,
       "prtMediaPathEntry": prtMediaPathEntry,
       "prtMediaPathIndex": prtMediaPathIndex,
       "prtMediaPathMaxSpeedPrintUnit": prtMediaPathMaxSpeedPrintUnit,
       "prtMediaPathMediaSizeUnit": prtMediaPathMediaSizeUnit,
       "prtMediaPathMaxSpeed": prtMediaPathMaxSpeed,
       "prtMediaPathMaxMediaFeedDir": prtMediaPathMaxMediaFeedDir,
       "prtMediaPathMaxMediaXFeedDir": prtMediaPathMaxMediaXFeedDir,
       "prtMediaPathMinMediaFeedDir": prtMediaPathMinMediaFeedDir,
       "prtMediaPathMinMediaXFeedDir": prtMediaPathMinMediaXFeedDir,
       "prtMediaPathType": prtMediaPathType,
       "prtMediaPathDescription": prtMediaPathDescription,
       "prtMediaPathStatus": prtMediaPathStatus,
       "prtChannel": prtChannel,
       "prtChannelTable": prtChannelTable,
       "prtChannelEntry": prtChannelEntry,
       "prtChannelIndex": prtChannelIndex,
       "prtChannelType": prtChannelType,
       "prtChannelProtocolVersion": prtChannelProtocolVersion,
       "prtChannelCurrentJobCntlLangIndex": prtChannelCurrentJobCntlLangIndex,
       "prtChannelDefaultPageDescLangIndex": prtChannelDefaultPageDescLangIndex,
       "prtChannelState": prtChannelState,
       "prtChannelIfIndex": prtChannelIfIndex,
       "prtChannelStatus": prtChannelStatus,
       "prtChannelInformation": prtChannelInformation,
       "prtInterpreter": prtInterpreter,
       "prtInterpreterTable": prtInterpreterTable,
       "prtInterpreterEntry": prtInterpreterEntry,
       "prtInterpreterIndex": prtInterpreterIndex,
       "prtInterpreterLangFamily": prtInterpreterLangFamily,
       "prtInterpreterLangLevel": prtInterpreterLangLevel,
       "prtInterpreterLangVersion": prtInterpreterLangVersion,
       "prtInterpreterDescription": prtInterpreterDescription,
       "prtInterpreterVersion": prtInterpreterVersion,
       "prtInterpreterDefaultOrientation": prtInterpreterDefaultOrientation,
       "prtInterpreterFeedAddressability": prtInterpreterFeedAddressability,
       "prtInterpreterXFeedAddressability": prtInterpreterXFeedAddressability,
       "prtInterpreterDefaultCharSetIn": prtInterpreterDefaultCharSetIn,
       "prtInterpreterDefaultCharSetOut": prtInterpreterDefaultCharSetOut,
       "prtInterpreterTwoWay": prtInterpreterTwoWay,
       "prtConsoleDisplayBuffer": prtConsoleDisplayBuffer,
       "prtConsoleDisplayBufferTable": prtConsoleDisplayBufferTable,
       "prtConsoleDisplayBufferEntry": prtConsoleDisplayBufferEntry,
       "prtConsoleDisplayBufferIndex": prtConsoleDisplayBufferIndex,
       "prtConsoleDisplayBufferText": prtConsoleDisplayBufferText,
       "prtConsoleLights": prtConsoleLights,
       "prtConsoleLightTable": prtConsoleLightTable,
       "prtConsoleLightEntry": prtConsoleLightEntry,
       "prtConsoleLightIndex": prtConsoleLightIndex,
       "prtConsoleOnTime": prtConsoleOnTime,
       "prtConsoleOffTime": prtConsoleOffTime,
       "prtConsoleColor": prtConsoleColor,
       "prtConsoleDescription": prtConsoleDescription,
       "prtAlert": prtAlert,
       "prtAlertTable": prtAlertTable,
       "prtAlertEntry": prtAlertEntry,
       "prtAlertIndex": prtAlertIndex,
       "prtAlertSeverityLevel": prtAlertSeverityLevel,
       "prtAlertTrainingLevel": prtAlertTrainingLevel,
       "prtAlertGroup": prtAlertGroup,
       "prtAlertGroupIndex": prtAlertGroupIndex,
       "prtAlertLocation": prtAlertLocation,
       "prtAlertCode": prtAlertCode,
       "prtAlertDescription": prtAlertDescription,
       "prtAlertTime": prtAlertTime,
       "printerV1Alert": printerV1Alert,
       "printerV2AlertPrefix": printerV2AlertPrefix,
       "printerV2Alert": printerV2Alert}
)
