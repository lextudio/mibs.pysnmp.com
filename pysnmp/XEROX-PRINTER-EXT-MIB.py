"""SNMP MIB module (XEROX-PRINTER-EXT-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-PRINTER-EXT-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 06:00:37 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(prtChannelEntry,
 PresentOnOff,
 prtLocalizationLanguage,
 prtInterpreterIndex,
 prtLocalizationCountry,
 prtLocalizationCharacterSet,
 prtGeneralEntry,
 prtConsoleLocalization,
 prtOutputEntry,
 prtInputEntry,
 prtInterpreterEntry) = mibBuilder.importSymbols(
    "Printer-MIB",
    "prtChannelEntry",
    "PresentOnOff",
    "prtLocalizationLanguage",
    "prtInterpreterIndex",
    "prtLocalizationCountry",
    "prtLocalizationCharacterSet",
    "prtGeneralEntry",
    "prtConsoleLocalization",
    "prtOutputEntry",
    "prtInputEntry",
    "prtInterpreterEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(ModuleIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Counter64,
 IpAddress,
 Integer32,
 TimeTicks,
 MibIdentifier,
 NotificationType,
 Bits,
 Unsigned32,
 ObjectIdentity,
 Counter32,
 Gauge32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "ModuleIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Counter64",
    "IpAddress",
    "Integer32",
    "TimeTicks",
    "MibIdentifier",
    "NotificationType",
    "Bits",
    "Unsigned32",
    "ObjectIdentity",
    "Counter32",
    "Gauge32",
    "iso")

(DisplayString,
 TextualConvention,
 RowStatus,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "RowStatus",
    "TruthValue")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(XcmFixedLocaleDisplayString,
 Cardinal32,
 Ordinal32,
 XcmGenRowPersistence) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "XcmFixedLocaleDisplayString",
    "Cardinal32",
    "Ordinal32",
    "XcmGenRowPersistence")

(XcmPrtGeneralMonoPrintOpt,
 XcmPrtAccountingSystemType,
 XcmPrtAuxSheetType,
 XcmPrtFinisherDFAType,
 XcmPrtMediaTypeErrorPolicy,
 XcmPrtPCLFontSource,
 XcmPrtIETFPrintMIBGroupSupport,
 XcmPrtMediumSize,
 XcmPrtPhaserModuleType,
 XcmPrtAuthenticationModeType,
 XcmPrtInputTraysConfiguration,
 XcmPrtOutputPunchPosition,
 XcmPrtGroupSupport,
 XcmPrtPrintEngineType,
 XcmPrtFaxOutType,
 XcmPrtHighCapacityFeederType,
 XcmPrtHoldForAuthenModeType,
 XcmPrtAuxSheetContent,
 XcmPrtPrintScreen,
 XcmPrtHolePunchUnitType,
 XcmPrtMediumClassType,
 XcmPrtOutputOffsetStackingType,
 XcmPrtPageSizeErrorPolicy,
 XcmPrtTraySwitch,
 XcmPrtPlex,
 XcmPrtAsciiJobTicketType,
 XcmPrtOutputStaplePosition,
 XcmPrtPrintQuality) = mibBuilder.importSymbols(
    "XEROX-PRINTER-EXT-TC",
    "XcmPrtGeneralMonoPrintOpt",
    "XcmPrtAccountingSystemType",
    "XcmPrtAuxSheetType",
    "XcmPrtFinisherDFAType",
    "XcmPrtMediaTypeErrorPolicy",
    "XcmPrtPCLFontSource",
    "XcmPrtIETFPrintMIBGroupSupport",
    "XcmPrtMediumSize",
    "XcmPrtPhaserModuleType",
    "XcmPrtAuthenticationModeType",
    "XcmPrtInputTraysConfiguration",
    "XcmPrtOutputPunchPosition",
    "XcmPrtGroupSupport",
    "XcmPrtPrintEngineType",
    "XcmPrtFaxOutType",
    "XcmPrtHighCapacityFeederType",
    "XcmPrtHoldForAuthenModeType",
    "XcmPrtAuxSheetContent",
    "XcmPrtPrintScreen",
    "XcmPrtHolePunchUnitType",
    "XcmPrtMediumClassType",
    "XcmPrtOutputOffsetStackingType",
    "XcmPrtPageSizeErrorPolicy",
    "XcmPrtTraySwitch",
    "XcmPrtPlex",
    "XcmPrtAsciiJobTicketType",
    "XcmPrtOutputStaplePosition",
    "XcmPrtPrintQuality")


# MODULE-IDENTITY

xcmPrintMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmPrtBase_ObjectIdentity = ObjectIdentity
xcmPrtBase = _XcmPrtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1)
)
_XcmPrtBaseTable_Object = MibTable
xcmPrtBaseTable = _XcmPrtBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2)
)
if mibBuilder.loadTexts:
    xcmPrtBaseTable.setStatus("current")
_XcmPrtBaseEntry_Object = MibTableRow
xcmPrtBaseEntry = _XcmPrtBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1)
)
xcmPrtBaseEntry.setIndexNames(
    (0, "XEROX-PRINTER-EXT-MIB", "xcmPrtBaseIndex"),
)
if mibBuilder.loadTexts:
    xcmPrtBaseEntry.setStatus("current")
_XcmPrtBaseIndex_Type = Ordinal32
_XcmPrtBaseIndex_Object = MibTableColumn
xcmPrtBaseIndex = _XcmPrtBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 1),
    _XcmPrtBaseIndex_Type()
)
xcmPrtBaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmPrtBaseIndex.setStatus("current")
_XcmPrtBaseRowStatus_Type = RowStatus
_XcmPrtBaseRowStatus_Object = MibTableColumn
xcmPrtBaseRowStatus = _XcmPrtBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 2),
    _XcmPrtBaseRowStatus_Type()
)
xcmPrtBaseRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseRowStatus.setStatus("current")
_XcmPrtBaseGroupSupport_Type = XcmPrtGroupSupport
_XcmPrtBaseGroupSupport_Object = MibTableColumn
xcmPrtBaseGroupSupport = _XcmPrtBaseGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 3),
    _XcmPrtBaseGroupSupport_Type()
)
xcmPrtBaseGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseGroupSupport.setStatus("current")
_XcmPrtBaseUpdateSupport_Type = XcmPrtGroupSupport
_XcmPrtBaseUpdateSupport_Object = MibTableColumn
xcmPrtBaseUpdateSupport = _XcmPrtBaseUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 4),
    _XcmPrtBaseUpdateSupport_Type()
)
xcmPrtBaseUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseUpdateSupport.setStatus("current")
_XcmPrtBaseCreateSupport_Type = XcmPrtGroupSupport
_XcmPrtBaseCreateSupport_Object = MibTableColumn
xcmPrtBaseCreateSupport = _XcmPrtBaseCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 5),
    _XcmPrtBaseCreateSupport_Type()
)
xcmPrtBaseCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseCreateSupport.setStatus("current")


class _XcmPrtBaseIETFMIBGroupSupport_Type(XcmPrtIETFPrintMIBGroupSupport):
    """Custom type xcmPrtBaseIETFMIBGroupSupport based on XcmPrtIETFPrintMIBGroupSupport"""
    defaultValue = 127525


_XcmPrtBaseIETFMIBGroupSupport_Object = MibTableColumn
xcmPrtBaseIETFMIBGroupSupport = _XcmPrtBaseIETFMIBGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 6),
    _XcmPrtBaseIETFMIBGroupSupport_Type()
)
xcmPrtBaseIETFMIBGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBGroupSupport.setStatus("current")
_XcmPrtBaseIETFMIBUpdateSupport_Type = XcmPrtIETFPrintMIBGroupSupport
_XcmPrtBaseIETFMIBUpdateSupport_Object = MibTableColumn
xcmPrtBaseIETFMIBUpdateSupport = _XcmPrtBaseIETFMIBUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 7),
    _XcmPrtBaseIETFMIBUpdateSupport_Type()
)
xcmPrtBaseIETFMIBUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBUpdateSupport.setStatus("current")
_XcmPrtBaseIETFMIBCreateSupport_Type = XcmPrtIETFPrintMIBGroupSupport
_XcmPrtBaseIETFMIBCreateSupport_Object = MibTableColumn
xcmPrtBaseIETFMIBCreateSupport = _XcmPrtBaseIETFMIBCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 8),
    _XcmPrtBaseIETFMIBCreateSupport_Type()
)
xcmPrtBaseIETFMIBCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBCreateSupport.setStatus("current")
_XcmPrtMIBConformance_ObjectIdentity = ObjectIdentity
xcmPrtMIBConformance = _XcmPrtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2)
)
_XcmPrtMIBGroups_ObjectIdentity = ObjectIdentity
xcmPrtMIBGroups = _XcmPrtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2)
)
_XcmPrtGeneral_ObjectIdentity = ObjectIdentity
xcmPrtGeneral = _XcmPrtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5)
)
_XcmPrtGeneralTable_Object = MibTable
xcmPrtGeneralTable = _XcmPrtGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1)
)
if mibBuilder.loadTexts:
    xcmPrtGeneralTable.setStatus("current")
_XcmPrtGeneralEntry_Object = MibTableRow
xcmPrtGeneralEntry = _XcmPrtGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1)
)
prtGeneralEntry.registerAugmentions(
    ("XEROX-PRINTER-EXT-MIB",
     "xcmPrtGeneralEntry")
)
xcmPrtGeneralEntry.setIndexNames(*prtGeneralEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmPrtGeneralEntry.setStatus("current")
_XcmPrtGeneralRowStatus_Type = RowStatus
_XcmPrtGeneralRowStatus_Object = MibTableColumn
xcmPrtGeneralRowStatus = _XcmPrtGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 1),
    _XcmPrtGeneralRowStatus_Type()
)
xcmPrtGeneralRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralRowStatus.setStatus("current")
_XcmPrtGeneralAuxSheetPackage_Type = Cardinal32
_XcmPrtGeneralAuxSheetPackage_Object = MibTableColumn
xcmPrtGeneralAuxSheetPackage = _XcmPrtGeneralAuxSheetPackage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 2),
    _XcmPrtGeneralAuxSheetPackage_Type()
)
xcmPrtGeneralAuxSheetPackage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralAuxSheetPackage.setStatus("current")


class _XcmPrtGeneralManualFeedTimeout_Type(Integer32):
    """Custom type xcmPrtGeneralManualFeedTimeout based on Integer32"""
    defaultValue = -1


_XcmPrtGeneralManualFeedTimeout_Object = MibTableColumn
xcmPrtGeneralManualFeedTimeout = _XcmPrtGeneralManualFeedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 3),
    _XcmPrtGeneralManualFeedTimeout_Type()
)
xcmPrtGeneralManualFeedTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralManualFeedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtGeneralManualFeedTimeout.setUnits("Seconds")


class _XcmPrtGeneralInputAutoSwitch_Type(PresentOnOff):
    """Custom type xcmPrtGeneralInputAutoSwitch based on PresentOnOff"""


_XcmPrtGeneralInputAutoSwitch_Object = MibTableColumn
xcmPrtGeneralInputAutoSwitch = _XcmPrtGeneralInputAutoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 4),
    _XcmPrtGeneralInputAutoSwitch_Type()
)
xcmPrtGeneralInputAutoSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralInputAutoSwitch.setStatus("current")


class _XcmPrtGeneralOutputAutoSwitch_Type(PresentOnOff):
    """Custom type xcmPrtGeneralOutputAutoSwitch based on PresentOnOff"""


_XcmPrtGeneralOutputAutoSwitch_Object = MibTableColumn
xcmPrtGeneralOutputAutoSwitch = _XcmPrtGeneralOutputAutoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 5),
    _XcmPrtGeneralOutputAutoSwitch_Type()
)
xcmPrtGeneralOutputAutoSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralOutputAutoSwitch.setStatus("current")


class _XcmPrtGeneralMediumClassDefault_Type(XcmPrtMediumClassType):
    """Custom type xcmPrtGeneralMediumClassDefault based on XcmPrtMediumClassType"""


_XcmPrtGeneralMediumClassDefault_Object = MibTableColumn
xcmPrtGeneralMediumClassDefault = _XcmPrtGeneralMediumClassDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 6),
    _XcmPrtGeneralMediumClassDefault_Type()
)
xcmPrtGeneralMediumClassDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralMediumClassDefault.setStatus("current")
_XcmPrtGeneralDarknessLevels_Type = Cardinal32
_XcmPrtGeneralDarknessLevels_Object = MibTableColumn
xcmPrtGeneralDarknessLevels = _XcmPrtGeneralDarknessLevels_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 7),
    _XcmPrtGeneralDarknessLevels_Type()
)
xcmPrtGeneralDarknessLevels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralDarknessLevels.setStatus("current")
_XcmPrtGeneralDarknessLevelNorm_Type = Cardinal32
_XcmPrtGeneralDarknessLevelNorm_Object = MibTableColumn
xcmPrtGeneralDarknessLevelNorm = _XcmPrtGeneralDarknessLevelNorm_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 8),
    _XcmPrtGeneralDarknessLevelNorm_Type()
)
xcmPrtGeneralDarknessLevelNorm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralDarknessLevelNorm.setStatus("current")


class _XcmPrtGeneralDarknessLevelDflt_Type(Integer32):
    """Custom type xcmPrtGeneralDarknessLevelDflt based on Integer32"""
    defaultValue = -2


_XcmPrtGeneralDarknessLevelDflt_Object = MibTableColumn
xcmPrtGeneralDarknessLevelDflt = _XcmPrtGeneralDarknessLevelDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 9),
    _XcmPrtGeneralDarknessLevelDflt_Type()
)
xcmPrtGeneralDarknessLevelDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralDarknessLevelDflt.setStatus("current")


class _XcmPrtGeneralHexDumpEnable_Type(PresentOnOff):
    """Custom type xcmPrtGeneralHexDumpEnable based on PresentOnOff"""


_XcmPrtGeneralHexDumpEnable_Object = MibTableColumn
xcmPrtGeneralHexDumpEnable = _XcmPrtGeneralHexDumpEnable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 10),
    _XcmPrtGeneralHexDumpEnable_Type()
)
xcmPrtGeneralHexDumpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralHexDumpEnable.setStatus("current")


class _XcmPrtGeneralStartupPage_Type(PresentOnOff):
    """Custom type xcmPrtGeneralStartupPage based on PresentOnOff"""


_XcmPrtGeneralStartupPage_Object = MibTableColumn
xcmPrtGeneralStartupPage = _XcmPrtGeneralStartupPage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 11),
    _XcmPrtGeneralStartupPage_Type()
)
xcmPrtGeneralStartupPage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralStartupPage.setStatus("current")


class _XcmPrtGeneralBannerPage_Type(PresentOnOff):
    """Custom type xcmPrtGeneralBannerPage based on PresentOnOff"""


_XcmPrtGeneralBannerPage_Object = MibTableColumn
xcmPrtGeneralBannerPage = _XcmPrtGeneralBannerPage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 12),
    _XcmPrtGeneralBannerPage_Type()
)
xcmPrtGeneralBannerPage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralBannerPage.setStatus("current")


class _XcmPrtGeneralTonerLowStop_Type(PresentOnOff):
    """Custom type xcmPrtGeneralTonerLowStop based on PresentOnOff"""


_XcmPrtGeneralTonerLowStop_Object = MibTableColumn
xcmPrtGeneralTonerLowStop = _XcmPrtGeneralTonerLowStop_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 13),
    _XcmPrtGeneralTonerLowStop_Type()
)
xcmPrtGeneralTonerLowStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralTonerLowStop.setStatus("current")


class _XcmPrtGeneralEndBannerPage_Type(PresentOnOff):
    """Custom type xcmPrtGeneralEndBannerPage based on PresentOnOff"""


_XcmPrtGeneralEndBannerPage_Object = MibTableColumn
xcmPrtGeneralEndBannerPage = _XcmPrtGeneralEndBannerPage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 14),
    _XcmPrtGeneralEndBannerPage_Type()
)
xcmPrtGeneralEndBannerPage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralEndBannerPage.setStatus("current")


class _XcmPrtGeneralTrayLowWarning_Type(PresentOnOff):
    """Custom type xcmPrtGeneralTrayLowWarning based on PresentOnOff"""


_XcmPrtGeneralTrayLowWarning_Object = MibTableColumn
xcmPrtGeneralTrayLowWarning = _XcmPrtGeneralTrayLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 15),
    _XcmPrtGeneralTrayLowWarning_Type()
)
xcmPrtGeneralTrayLowWarning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralTrayLowWarning.setStatus("current")


class _XcmPrtGeneralScanlineCompaction_Type(PresentOnOff):
    """Custom type xcmPrtGeneralScanlineCompaction based on PresentOnOff"""


_XcmPrtGeneralScanlineCompaction_Object = MibTableColumn
xcmPrtGeneralScanlineCompaction = _XcmPrtGeneralScanlineCompaction_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 50),
    _XcmPrtGeneralScanlineCompaction_Type()
)
xcmPrtGeneralScanlineCompaction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralScanlineCompaction.setStatus("current")


class _XcmPrtGeneralMonoPrintOptimization_Type(XcmPrtGeneralMonoPrintOpt):
    """Custom type xcmPrtGeneralMonoPrintOptimization based on XcmPrtGeneralMonoPrintOpt"""


_XcmPrtGeneralMonoPrintOptimization_Object = MibTableColumn
xcmPrtGeneralMonoPrintOptimization = _XcmPrtGeneralMonoPrintOptimization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 51),
    _XcmPrtGeneralMonoPrintOptimization_Type()
)
xcmPrtGeneralMonoPrintOptimization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralMonoPrintOptimization.setStatus("current")


class _XcmPrtGeneralInstalledFeeder_Type(OctetString):
    """Custom type xcmPrtGeneralInstalledFeeder based on OctetString"""
    defaultValue = OctetString("none")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtGeneralInstalledFeeder_Type.__name__ = "OctetString"
_XcmPrtGeneralInstalledFeeder_Object = MibTableColumn
xcmPrtGeneralInstalledFeeder = _XcmPrtGeneralInstalledFeeder_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 70),
    _XcmPrtGeneralInstalledFeeder_Type()
)
xcmPrtGeneralInstalledFeeder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtGeneralInstalledFeeder.setStatus("current")


class _XcmPrtGeneralInstalledFinisher_Type(OctetString):
    """Custom type xcmPrtGeneralInstalledFinisher based on OctetString"""
    defaultValue = OctetString("none")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtGeneralInstalledFinisher_Type.__name__ = "OctetString"
_XcmPrtGeneralInstalledFinisher_Object = MibTableColumn
xcmPrtGeneralInstalledFinisher = _XcmPrtGeneralInstalledFinisher_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 71),
    _XcmPrtGeneralInstalledFinisher_Type()
)
xcmPrtGeneralInstalledFinisher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtGeneralInstalledFinisher.setStatus("current")


class _XcmPrtGeneralInstalledAnalogFax_Type(OctetString):
    """Custom type xcmPrtGeneralInstalledAnalogFax based on OctetString"""
    defaultValue = OctetString("none")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtGeneralInstalledAnalogFax_Type.__name__ = "OctetString"
_XcmPrtGeneralInstalledAnalogFax_Object = MibTableColumn
xcmPrtGeneralInstalledAnalogFax = _XcmPrtGeneralInstalledAnalogFax_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 72),
    _XcmPrtGeneralInstalledAnalogFax_Type()
)
xcmPrtGeneralInstalledAnalogFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtGeneralInstalledAnalogFax.setStatus("current")
_XcmPrtGeneralConsoleLocalizationV1EventOID_ObjectIdentity = ObjectIdentity
xcmPrtGeneralConsoleLocalizationV1EventOID = _XcmPrtGeneralConsoleLocalizationV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 2)
)
if mibBuilder.loadTexts:
    xcmPrtGeneralConsoleLocalizationV1EventOID.setStatus("current")
_XcmPrtGeneralConsoleLocalizationV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmPrtGeneralConsoleLocalizationV2EventPrefix = _XcmPrtGeneralConsoleLocalizationV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 2, 0)
)
_XcmPrtDriverOptions_ObjectIdentity = ObjectIdentity
xcmPrtDriverOptions = _XcmPrtDriverOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6)
)
_XcmPrtDrvrHwdOptStapler_Type = PresentOnOff
_XcmPrtDrvrHwdOptStapler_Object = MibScalar
xcmPrtDrvrHwdOptStapler = _XcmPrtDrvrHwdOptStapler_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 1),
    _XcmPrtDrvrHwdOptStapler_Type()
)
xcmPrtDrvrHwdOptStapler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptStapler.setStatus("current")
_XcmPrtDrvrHwdOptDuplexUnit_Type = PresentOnOff
_XcmPrtDrvrHwdOptDuplexUnit_Object = MibScalar
xcmPrtDrvrHwdOptDuplexUnit = _XcmPrtDrvrHwdOptDuplexUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 2),
    _XcmPrtDrvrHwdOptDuplexUnit_Type()
)
xcmPrtDrvrHwdOptDuplexUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptDuplexUnit.setStatus("current")
_XcmPrtDrvrHwdOptPhaserBookletMaker_Type = PresentOnOff
_XcmPrtDrvrHwdOptPhaserBookletMaker_Object = MibScalar
xcmPrtDrvrHwdOptPhaserBookletMaker = _XcmPrtDrvrHwdOptPhaserBookletMaker_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 3),
    _XcmPrtDrvrHwdOptPhaserBookletMaker_Type()
)
xcmPrtDrvrHwdOptPhaserBookletMaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptPhaserBookletMaker.setStatus("current")
_XcmPrtDrvrHwdOptEnvelopeTray_Type = PresentOnOff
_XcmPrtDrvrHwdOptEnvelopeTray_Object = MibScalar
xcmPrtDrvrHwdOptEnvelopeTray = _XcmPrtDrvrHwdOptEnvelopeTray_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 4),
    _XcmPrtDrvrHwdOptEnvelopeTray_Type()
)
xcmPrtDrvrHwdOptEnvelopeTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptEnvelopeTray.setStatus("current")
_XcmPrtDrvrHwdOptCoilPunchUnit_Type = PresentOnOff
_XcmPrtDrvrHwdOptCoilPunchUnit_Object = MibScalar
xcmPrtDrvrHwdOptCoilPunchUnit = _XcmPrtDrvrHwdOptCoilPunchUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 5),
    _XcmPrtDrvrHwdOptCoilPunchUnit_Type()
)
xcmPrtDrvrHwdOptCoilPunchUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptCoilPunchUnit.setStatus("current")
_XcmPrtDrvrHwdOptFinisherDFA_Type = XcmPrtFinisherDFAType
_XcmPrtDrvrHwdOptFinisherDFA_Object = MibScalar
xcmPrtDrvrHwdOptFinisherDFA = _XcmPrtDrvrHwdOptFinisherDFA_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 6),
    _XcmPrtDrvrHwdOptFinisherDFA_Type()
)
xcmPrtDrvrHwdOptFinisherDFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptFinisherDFA.setStatus("current")
_XcmPrtDrvrHwdOptHighCapacityFeeder_Type = XcmPrtHighCapacityFeederType
_XcmPrtDrvrHwdOptHighCapacityFeeder_Object = MibScalar
xcmPrtDrvrHwdOptHighCapacityFeeder = _XcmPrtDrvrHwdOptHighCapacityFeeder_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 7),
    _XcmPrtDrvrHwdOptHighCapacityFeeder_Type()
)
xcmPrtDrvrHwdOptHighCapacityFeeder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptHighCapacityFeeder.setStatus("current")


class _XcmPrtDriverOutputDeliveryUnit_Type(OctetString):
    """Custom type xcmPrtDriverOutputDeliveryUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtDriverOutputDeliveryUnit_Type.__name__ = "OctetString"
_XcmPrtDriverOutputDeliveryUnit_Object = MibScalar
xcmPrtDriverOutputDeliveryUnit = _XcmPrtDriverOutputDeliveryUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 8),
    _XcmPrtDriverOutputDeliveryUnit_Type()
)
xcmPrtDriverOutputDeliveryUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDriverOutputDeliveryUnit.setStatus("current")
_XcmPrtDrvrHwdOptHardDrive_Type = PresentOnOff
_XcmPrtDrvrHwdOptHardDrive_Object = MibScalar
xcmPrtDrvrHwdOptHardDrive = _XcmPrtDrvrHwdOptHardDrive_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 9),
    _XcmPrtDrvrHwdOptHardDrive_Type()
)
xcmPrtDrvrHwdOptHardDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptHardDrive.setStatus("current")
_XcmPrtDrvrHwdOptHolePunchUnit_Type = XcmPrtHolePunchUnitType
_XcmPrtDrvrHwdOptHolePunchUnit_Object = MibScalar
xcmPrtDrvrHwdOptHolePunchUnit = _XcmPrtDrvrHwdOptHolePunchUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 10),
    _XcmPrtDrvrHwdOptHolePunchUnit_Type()
)
xcmPrtDrvrHwdOptHolePunchUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptHolePunchUnit.setStatus("current")


class _XcmPrtDriverInputPaperTrays_Type(OctetString):
    """Custom type xcmPrtDriverInputPaperTrays based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtDriverInputPaperTrays_Type.__name__ = "OctetString"
_XcmPrtDriverInputPaperTrays_Object = MibScalar
xcmPrtDriverInputPaperTrays = _XcmPrtDriverInputPaperTrays_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 11),
    _XcmPrtDriverInputPaperTrays_Type()
)
xcmPrtDriverInputPaperTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDriverInputPaperTrays.setStatus("current")
_XcmPrtDrvrHwdOptInserterUnit_Type = PresentOnOff
_XcmPrtDrvrHwdOptInserterUnit_Object = MibScalar
xcmPrtDrvrHwdOptInserterUnit = _XcmPrtDrvrHwdOptInserterUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 12),
    _XcmPrtDrvrHwdOptInserterUnit_Type()
)
xcmPrtDrvrHwdOptInserterUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptInserterUnit.setStatus("current")
_XcmPrtDrvrHwdOptJobAccountingFdi_Type = PresentOnOff
_XcmPrtDrvrHwdOptJobAccountingFdi_Object = MibScalar
xcmPrtDrvrHwdOptJobAccountingFdi = _XcmPrtDrvrHwdOptJobAccountingFdi_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 13),
    _XcmPrtDrvrHwdOptJobAccountingFdi_Type()
)
xcmPrtDrvrHwdOptJobAccountingFdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptJobAccountingFdi.setStatus("current")
_XcmPrtDrvrHwdOptFaxOut_Type = XcmPrtFaxOutType
_XcmPrtDrvrHwdOptFaxOut_Object = MibScalar
xcmPrtDrvrHwdOptFaxOut = _XcmPrtDrvrHwdOptFaxOut_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 14),
    _XcmPrtDrvrHwdOptFaxOut_Type()
)
xcmPrtDrvrHwdOptFaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptFaxOut.setStatus("current")
_XcmPrtDrvrHwdOptMemoryInMBs_Type = Integer32
_XcmPrtDrvrHwdOptMemoryInMBs_Object = MibScalar
xcmPrtDrvrHwdOptMemoryInMBs = _XcmPrtDrvrHwdOptMemoryInMBs_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 15),
    _XcmPrtDrvrHwdOptMemoryInMBs_Type()
)
xcmPrtDrvrHwdOptMemoryInMBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptMemoryInMBs.setStatus("current")
_XcmPrtDrvrHwdOptOutputBinSide_Type = PresentOnOff
_XcmPrtDrvrHwdOptOutputBinSide_Object = MibScalar
xcmPrtDrvrHwdOptOutputBinSide = _XcmPrtDrvrHwdOptOutputBinSide_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 16),
    _XcmPrtDrvrHwdOptOutputBinSide_Type()
)
xcmPrtDrvrHwdOptOutputBinSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptOutputBinSide.setStatus("current")
_XcmPrtDrvrHwdOptOutputBinCenter_Type = PresentOnOff
_XcmPrtDrvrHwdOptOutputBinCenter_Object = MibScalar
xcmPrtDrvrHwdOptOutputBinCenter = _XcmPrtDrvrHwdOptOutputBinCenter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 17),
    _XcmPrtDrvrHwdOptOutputBinCenter_Type()
)
xcmPrtDrvrHwdOptOutputBinCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptOutputBinCenter.setStatus("current")
_XcmPrtDrvrHwdOptPhaserModule_Type = XcmPrtPhaserModuleType
_XcmPrtDrvrHwdOptPhaserModule_Object = MibScalar
xcmPrtDrvrHwdOptPhaserModule = _XcmPrtDrvrHwdOptPhaserModule_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 18),
    _XcmPrtDrvrHwdOptPhaserModule_Type()
)
xcmPrtDrvrHwdOptPhaserModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptPhaserModule.setStatus("current")
_XcmPrtDrvrHwdOptPrintEngine_Type = XcmPrtPrintEngineType
_XcmPrtDrvrHwdOptPrintEngine_Object = MibScalar
xcmPrtDrvrHwdOptPrintEngine = _XcmPrtDrvrHwdOptPrintEngine_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 19),
    _XcmPrtDrvrHwdOptPrintEngine_Type()
)
xcmPrtDrvrHwdOptPrintEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptPrintEngine.setStatus("current")
_XcmPrtDrvrHwdOptSquareFoldTrimmer_Type = PresentOnOff
_XcmPrtDrvrHwdOptSquareFoldTrimmer_Object = MibScalar
xcmPrtDrvrHwdOptSquareFoldTrimmer = _XcmPrtDrvrHwdOptSquareFoldTrimmer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 20),
    _XcmPrtDrvrHwdOptSquareFoldTrimmer_Type()
)
xcmPrtDrvrHwdOptSquareFoldTrimmer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptSquareFoldTrimmer.setStatus("current")
_XcmPrtDrvrHwdOptTriFold_Type = PresentOnOff
_XcmPrtDrvrHwdOptTriFold_Object = MibScalar
xcmPrtDrvrHwdOptTriFold = _XcmPrtDrvrHwdOptTriFold_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 21),
    _XcmPrtDrvrHwdOptTriFold_Type()
)
xcmPrtDrvrHwdOptTriFold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptTriFold.setStatus("current")
_XcmPrtDrvrFntCollation_Type = PresentOnOff
_XcmPrtDrvrFntCollation_Object = MibScalar
xcmPrtDrvrFntCollation = _XcmPrtDrvrFntCollation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 50),
    _XcmPrtDrvrFntCollation_Type()
)
xcmPrtDrvrFntCollation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntCollation.setStatus("current")
_XcmPrtDrvrFntAsciiJobTicket_Type = XcmPrtAsciiJobTicketType
_XcmPrtDrvrFntAsciiJobTicket_Object = MibScalar
xcmPrtDrvrFntAsciiJobTicket = _XcmPrtDrvrFntAsciiJobTicket_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 51),
    _XcmPrtDrvrFntAsciiJobTicket_Type()
)
xcmPrtDrvrFntAsciiJobTicket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntAsciiJobTicket.setStatus("current")
_XcmPrtDrvrFntAuthenticationMode_Type = XcmPrtAuthenticationModeType
_XcmPrtDrvrFntAuthenticationMode_Object = MibScalar
xcmPrtDrvrFntAuthenticationMode = _XcmPrtDrvrFntAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 52),
    _XcmPrtDrvrFntAuthenticationMode_Type()
)
xcmPrtDrvrFntAuthenticationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntAuthenticationMode.setStatus("current")
_XcmPrtDrvrFntHoldForAuthenMode_Type = XcmPrtHoldForAuthenModeType
_XcmPrtDrvrFntHoldForAuthenMode_Object = MibScalar
xcmPrtDrvrFntHoldForAuthenMode = _XcmPrtDrvrFntHoldForAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 53),
    _XcmPrtDrvrFntHoldForAuthenMode_Type()
)
xcmPrtDrvrFntHoldForAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntHoldForAuthenMode.setStatus("current")
_XcmPrtDrvrFntEnhancedImageQualityMode_Type = PresentOnOff
_XcmPrtDrvrFntEnhancedImageQualityMode_Object = MibScalar
xcmPrtDrvrFntEnhancedImageQualityMode = _XcmPrtDrvrFntEnhancedImageQualityMode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 54),
    _XcmPrtDrvrFntEnhancedImageQualityMode_Type()
)
xcmPrtDrvrFntEnhancedImageQualityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntEnhancedImageQualityMode.setStatus("current")
_XcmPrtDrvrFntProductivityPack_Type = PresentOnOff
_XcmPrtDrvrFntProductivityPack_Object = MibScalar
xcmPrtDrvrFntProductivityPack = _XcmPrtDrvrFntProductivityPack_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 55),
    _XcmPrtDrvrFntProductivityPack_Type()
)
xcmPrtDrvrFntProductivityPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntProductivityPack.setStatus("current")
_XcmPrtDrvrFntJobStorage_Type = PresentOnOff
_XcmPrtDrvrFntJobStorage_Object = MibScalar
xcmPrtDrvrFntJobStorage = _XcmPrtDrvrFntJobStorage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 56),
    _XcmPrtDrvrFntJobStorage_Type()
)
xcmPrtDrvrFntJobStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntJobStorage.setStatus("current")
_XcmPrtDrvrFntJobAccountingSystem_Type = XcmPrtAccountingSystemType
_XcmPrtDrvrFntJobAccountingSystem_Object = MibScalar
xcmPrtDrvrFntJobAccountingSystem = _XcmPrtDrvrFntJobAccountingSystem_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 57),
    _XcmPrtDrvrFntJobAccountingSystem_Type()
)
xcmPrtDrvrFntJobAccountingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntJobAccountingSystem.setStatus("current")
_XcmPrtInput_ObjectIdentity = ObjectIdentity
xcmPrtInput = _XcmPrtInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8)
)
_XcmPrtInputTable_Object = MibTable
xcmPrtInputTable = _XcmPrtInputTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1)
)
if mibBuilder.loadTexts:
    xcmPrtInputTable.setStatus("current")
_XcmPrtInputEntry_Object = MibTableRow
xcmPrtInputEntry = _XcmPrtInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1)
)
prtInputEntry.registerAugmentions(
    ("XEROX-PRINTER-EXT-MIB",
     "xcmPrtInputEntry")
)
xcmPrtInputEntry.setIndexNames(*prtInputEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmPrtInputEntry.setStatus("current")
_XcmPrtInputRowStatus_Type = RowStatus
_XcmPrtInputRowStatus_Object = MibTableColumn
xcmPrtInputRowStatus = _XcmPrtInputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 1),
    _XcmPrtInputRowStatus_Type()
)
xcmPrtInputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputRowStatus.setStatus("current")
_XcmPrtInputNextPrtInputIndex_Type = Integer32
_XcmPrtInputNextPrtInputIndex_Object = MibTableColumn
xcmPrtInputNextPrtInputIndex = _XcmPrtInputNextPrtInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 2),
    _XcmPrtInputNextPrtInputIndex_Type()
)
xcmPrtInputNextPrtInputIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputNextPrtInputIndex.setStatus("current")


class _XcmPrtInputUseCustomSize_Type(PresentOnOff):
    """Custom type xcmPrtInputUseCustomSize based on PresentOnOff"""


_XcmPrtInputUseCustomSize_Object = MibTableColumn
xcmPrtInputUseCustomSize = _XcmPrtInputUseCustomSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 3),
    _XcmPrtInputUseCustomSize_Type()
)
xcmPrtInputUseCustomSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputUseCustomSize.setStatus("current")
_XcmPrtInputCustDimFeedDirDecl_Type = Integer32
_XcmPrtInputCustDimFeedDirDecl_Object = MibTableColumn
xcmPrtInputCustDimFeedDirDecl = _XcmPrtInputCustDimFeedDirDecl_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 4),
    _XcmPrtInputCustDimFeedDirDecl_Type()
)
xcmPrtInputCustDimFeedDirDecl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputCustDimFeedDirDecl.setStatus("current")
_XcmPrtInputCustDimXFeedDirDecl_Type = Integer32
_XcmPrtInputCustDimXFeedDirDecl_Object = MibTableColumn
xcmPrtInputCustDimXFeedDirDecl = _XcmPrtInputCustDimXFeedDirDecl_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 5),
    _XcmPrtInputCustDimXFeedDirDecl_Type()
)
xcmPrtInputCustDimXFeedDirDecl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputCustDimXFeedDirDecl.setStatus("current")
_XcmPrtInputTrayPriority_Type = Integer32
_XcmPrtInputTrayPriority_Object = MibTableColumn
xcmPrtInputTrayPriority = _XcmPrtInputTrayPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 6),
    _XcmPrtInputTrayPriority_Type()
)
xcmPrtInputTrayPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputTrayPriority.setStatus("current")
_XcmPrtInputTrayTable_Object = MibTable
xcmPrtInputTrayTable = _XcmPrtInputTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 2)
)
if mibBuilder.loadTexts:
    xcmPrtInputTrayTable.setStatus("current")
_XcmPrtInputTrayEntry_Object = MibTableRow
xcmPrtInputTrayEntry = _XcmPrtInputTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 2, 1)
)
xcmPrtInputTrayEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmPrtInputTrayEntry.setStatus("current")
_XcmPrtInputTraysRowStatus_Type = RowStatus
_XcmPrtInputTraysRowStatus_Object = MibTableColumn
xcmPrtInputTraysRowStatus = _XcmPrtInputTraysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 2, 1, 1),
    _XcmPrtInputTraysRowStatus_Type()
)
xcmPrtInputTraysRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputTraysRowStatus.setStatus("current")


class _XcmPrtInputTraysInstalled_Type(Integer32):
    """Custom type xcmPrtInputTraysInstalled based on Integer32"""
    defaultValue = 1


_XcmPrtInputTraysInstalled_Object = MibTableColumn
xcmPrtInputTraysInstalled = _XcmPrtInputTraysInstalled_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 2, 1, 2),
    _XcmPrtInputTraysInstalled_Type()
)
xcmPrtInputTraysInstalled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputTraysInstalled.setStatus("current")


class _XcmPrtInputTraysConfiguration_Type(XcmPrtInputTraysConfiguration):
    """Custom type xcmPrtInputTraysConfiguration based on XcmPrtInputTraysConfiguration"""


_XcmPrtInputTraysConfiguration_Object = MibTableColumn
xcmPrtInputTraysConfiguration = _XcmPrtInputTraysConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 2, 1, 3),
    _XcmPrtInputTraysConfiguration_Type()
)
xcmPrtInputTraysConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtInputTraysConfiguration.setStatus("current")
_XcmPrtOutput_ObjectIdentity = ObjectIdentity
xcmPrtOutput = _XcmPrtOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9)
)
_XcmPrtOutputTable_Object = MibTable
xcmPrtOutputTable = _XcmPrtOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1)
)
if mibBuilder.loadTexts:
    xcmPrtOutputTable.setStatus("current")
_XcmPrtOutputEntry_Object = MibTableRow
xcmPrtOutputEntry = _XcmPrtOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1)
)
prtOutputEntry.registerAugmentions(
    ("XEROX-PRINTER-EXT-MIB",
     "xcmPrtOutputEntry")
)
xcmPrtOutputEntry.setIndexNames(*prtOutputEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmPrtOutputEntry.setStatus("current")
_XcmPrtOutputRowStatus_Type = RowStatus
_XcmPrtOutputRowStatus_Object = MibTableColumn
xcmPrtOutputRowStatus = _XcmPrtOutputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 1),
    _XcmPrtOutputRowStatus_Type()
)
xcmPrtOutputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputRowStatus.setStatus("current")
_XcmPrtOutputNextIndex_Type = Integer32
_XcmPrtOutputNextIndex_Object = MibTableColumn
xcmPrtOutputNextIndex = _XcmPrtOutputNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 2),
    _XcmPrtOutputNextIndex_Type()
)
xcmPrtOutputNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputNextIndex.setStatus("current")


class _XcmPrtOutputPassword_Type(OctetString):
    """Custom type xcmPrtOutputPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtOutputPassword_Type.__name__ = "OctetString"
_XcmPrtOutputPassword_Object = MibTableColumn
xcmPrtOutputPassword = _XcmPrtOutputPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 3),
    _XcmPrtOutputPassword_Type()
)
xcmPrtOutputPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputPassword.setStatus("current")


class _XcmPrtOutputOffsetStackingType_Type(XcmPrtOutputOffsetStackingType):
    """Custom type xcmPrtOutputOffsetStackingType based on XcmPrtOutputOffsetStackingType"""


_XcmPrtOutputOffsetStackingType_Object = MibTableColumn
xcmPrtOutputOffsetStackingType = _XcmPrtOutputOffsetStackingType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 4),
    _XcmPrtOutputOffsetStackingType_Type()
)
xcmPrtOutputOffsetStackingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputOffsetStackingType.setStatus("current")


class _XcmPrtOutputTrayTimeoutSupport_Type(PresentOnOff):
    """Custom type xcmPrtOutputTrayTimeoutSupport based on PresentOnOff"""


_XcmPrtOutputTrayTimeoutSupport_Object = MibTableColumn
xcmPrtOutputTrayTimeoutSupport = _XcmPrtOutputTrayTimeoutSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 5),
    _XcmPrtOutputTrayTimeoutSupport_Type()
)
xcmPrtOutputTrayTimeoutSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputTrayTimeoutSupport.setStatus("current")
_XcmPrtOutputTrayTimeout_Type = Cardinal32
_XcmPrtOutputTrayTimeout_Object = MibTableColumn
xcmPrtOutputTrayTimeout = _XcmPrtOutputTrayTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 6),
    _XcmPrtOutputTrayTimeout_Type()
)
xcmPrtOutputTrayTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputTrayTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtOutputTrayTimeout.setUnits("Seconds")


class _XcmPrtOutputStaple_Type(PresentOnOff):
    """Custom type xcmPrtOutputStaple based on PresentOnOff"""


_XcmPrtOutputStaple_Object = MibTableColumn
xcmPrtOutputStaple = _XcmPrtOutputStaple_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 100),
    _XcmPrtOutputStaple_Type()
)
xcmPrtOutputStaple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputStaple.setStatus("current")
_XcmPrtOutputStaplePosSupported_Type = XcmPrtOutputStaplePosition
_XcmPrtOutputStaplePosSupported_Object = MibTableColumn
xcmPrtOutputStaplePosSupported = _XcmPrtOutputStaplePosSupported_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 101),
    _XcmPrtOutputStaplePosSupported_Type()
)
xcmPrtOutputStaplePosSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputStaplePosSupported.setStatus("current")


class _XcmPrtOutputStapleDefault_Type(PresentOnOff):
    """Custom type xcmPrtOutputStapleDefault based on PresentOnOff"""


_XcmPrtOutputStapleDefault_Object = MibTableColumn
xcmPrtOutputStapleDefault = _XcmPrtOutputStapleDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 102),
    _XcmPrtOutputStapleDefault_Type()
)
xcmPrtOutputStapleDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputStapleDefault.setStatus("current")
_XcmPrtOutputStaplePosDefault_Type = XcmPrtOutputStaplePosition
_XcmPrtOutputStaplePosDefault_Object = MibTableColumn
xcmPrtOutputStaplePosDefault = _XcmPrtOutputStaplePosDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 103),
    _XcmPrtOutputStaplePosDefault_Type()
)
xcmPrtOutputStaplePosDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputStaplePosDefault.setStatus("current")


class _XcmPrtOutputPunch_Type(PresentOnOff):
    """Custom type xcmPrtOutputPunch based on PresentOnOff"""


_XcmPrtOutputPunch_Object = MibTableColumn
xcmPrtOutputPunch = _XcmPrtOutputPunch_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 104),
    _XcmPrtOutputPunch_Type()
)
xcmPrtOutputPunch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputPunch.setStatus("current")


class _XcmPrtOutputPunchDefault_Type(PresentOnOff):
    """Custom type xcmPrtOutputPunchDefault based on PresentOnOff"""


_XcmPrtOutputPunchDefault_Object = MibTableColumn
xcmPrtOutputPunchDefault = _XcmPrtOutputPunchDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 105),
    _XcmPrtOutputPunchDefault_Type()
)
xcmPrtOutputPunchDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputPunchDefault.setStatus("current")
_XcmPrtOutputPunchPosSupported_Type = XcmPrtOutputPunchPosition
_XcmPrtOutputPunchPosSupported_Object = MibTableColumn
xcmPrtOutputPunchPosSupported = _XcmPrtOutputPunchPosSupported_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 106),
    _XcmPrtOutputPunchPosSupported_Type()
)
xcmPrtOutputPunchPosSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputPunchPosSupported.setStatus("current")


class _XcmPrtOutputBookletFoldStaple_Type(PresentOnOff):
    """Custom type xcmPrtOutputBookletFoldStaple based on PresentOnOff"""


_XcmPrtOutputBookletFoldStaple_Object = MibTableColumn
xcmPrtOutputBookletFoldStaple = _XcmPrtOutputBookletFoldStaple_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 107),
    _XcmPrtOutputBookletFoldStaple_Type()
)
xcmPrtOutputBookletFoldStaple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputBookletFoldStaple.setStatus("current")
_XcmPrtChannel_ObjectIdentity = ObjectIdentity
xcmPrtChannel = _XcmPrtChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14)
)
_XcmPrtChannelTable_Object = MibTable
xcmPrtChannelTable = _XcmPrtChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1)
)
if mibBuilder.loadTexts:
    xcmPrtChannelTable.setStatus("current")
_XcmPrtChannelEntry_Object = MibTableRow
xcmPrtChannelEntry = _XcmPrtChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1)
)
prtChannelEntry.registerAugmentions(
    ("XEROX-PRINTER-EXT-MIB",
     "xcmPrtChannelEntry")
)
xcmPrtChannelEntry.setIndexNames(*prtChannelEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmPrtChannelEntry.setStatus("current")
_XcmPrtChannelRowStatus_Type = RowStatus
_XcmPrtChannelRowStatus_Object = MibTableColumn
xcmPrtChannelRowStatus = _XcmPrtChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 1),
    _XcmPrtChannelRowStatus_Type()
)
xcmPrtChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelRowStatus.setStatus("current")
_XcmPrtChannelEOJTimeout_Type = Cardinal32
_XcmPrtChannelEOJTimeout_Object = MibTableColumn
xcmPrtChannelEOJTimeout = _XcmPrtChannelEOJTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 2),
    _XcmPrtChannelEOJTimeout_Type()
)
xcmPrtChannelEOJTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelEOJTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtChannelEOJTimeout.setUnits("Seconds")
_XcmPrtChannelAuxSheetPackage_Type = Cardinal32
_XcmPrtChannelAuxSheetPackage_Object = MibTableColumn
xcmPrtChannelAuxSheetPackage = _XcmPrtChannelAuxSheetPackage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 3),
    _XcmPrtChannelAuxSheetPackage_Type()
)
xcmPrtChannelAuxSheetPackage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelAuxSheetPackage.setStatus("current")


class _XcmPrtChannelSpoolingEnable_Type(PresentOnOff):
    """Custom type xcmPrtChannelSpoolingEnable based on PresentOnOff"""


_XcmPrtChannelSpoolingEnable_Object = MibTableColumn
xcmPrtChannelSpoolingEnable = _XcmPrtChannelSpoolingEnable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 4),
    _XcmPrtChannelSpoolingEnable_Type()
)
xcmPrtChannelSpoolingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelSpoolingEnable.setStatus("current")


class _XcmPrtChannelLangSensing_Type(PresentOnOff):
    """Custom type xcmPrtChannelLangSensing based on PresentOnOff"""


_XcmPrtChannelLangSensing_Object = MibTableColumn
xcmPrtChannelLangSensing = _XcmPrtChannelLangSensing_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 5),
    _XcmPrtChannelLangSensing_Type()
)
xcmPrtChannelLangSensing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelLangSensing.setStatus("current")


class _XcmPrtChannelBinaryPostScript_Type(PresentOnOff):
    """Custom type xcmPrtChannelBinaryPostScript based on PresentOnOff"""


_XcmPrtChannelBinaryPostScript_Object = MibTableColumn
xcmPrtChannelBinaryPostScript = _XcmPrtChannelBinaryPostScript_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 6),
    _XcmPrtChannelBinaryPostScript_Type()
)
xcmPrtChannelBinaryPostScript.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelBinaryPostScript.setStatus("current")


class _XcmPrtChannelAutoJobEnd_Type(PresentOnOff):
    """Custom type xcmPrtChannelAutoJobEnd based on PresentOnOff"""


_XcmPrtChannelAutoJobEnd_Object = MibTableColumn
xcmPrtChannelAutoJobEnd = _XcmPrtChannelAutoJobEnd_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 80),
    _XcmPrtChannelAutoJobEnd_Type()
)
xcmPrtChannelAutoJobEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelAutoJobEnd.setStatus("current")


class _XcmPrtChannelBinaryPostScriptZ_Type(PresentOnOff):
    """Custom type xcmPrtChannelBinaryPostScriptZ based on PresentOnOff"""


_XcmPrtChannelBinaryPostScriptZ_Object = MibTableColumn
xcmPrtChannelBinaryPostScriptZ = _XcmPrtChannelBinaryPostScriptZ_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 81),
    _XcmPrtChannelBinaryPostScriptZ_Type()
)
xcmPrtChannelBinaryPostScriptZ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelBinaryPostScriptZ.setStatus("current")
_XcmPrtInterpreter_ObjectIdentity = ObjectIdentity
xcmPrtInterpreter = _XcmPrtInterpreter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15)
)
_XcmPrtInterpreterTable_Object = MibTable
xcmPrtInterpreterTable = _XcmPrtInterpreterTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1)
)
if mibBuilder.loadTexts:
    xcmPrtInterpreterTable.setStatus("current")
_XcmPrtInterpreterEntry_Object = MibTableRow
xcmPrtInterpreterEntry = _XcmPrtInterpreterEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1)
)
prtInterpreterEntry.registerAugmentions(
    ("XEROX-PRINTER-EXT-MIB",
     "xcmPrtInterpreterEntry")
)
xcmPrtInterpreterEntry.setIndexNames(*prtInterpreterEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmPrtInterpreterEntry.setStatus("current")
_XcmPrtInterpRowStatus_Type = RowStatus
_XcmPrtInterpRowStatus_Object = MibTableColumn
xcmPrtInterpRowStatus = _XcmPrtInterpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 1),
    _XcmPrtInterpRowStatus_Type()
)
xcmPrtInterpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpRowStatus.setStatus("current")
_XcmPrtInterpAuxSheetPackage_Type = Cardinal32
_XcmPrtInterpAuxSheetPackage_Object = MibTableColumn
xcmPrtInterpAuxSheetPackage = _XcmPrtInterpAuxSheetPackage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 2),
    _XcmPrtInterpAuxSheetPackage_Type()
)
xcmPrtInterpAuxSheetPackage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpAuxSheetPackage.setStatus("current")


class _XcmPrtInterpContextSaving_Type(PresentOnOff):
    """Custom type xcmPrtInterpContextSaving based on PresentOnOff"""


_XcmPrtInterpContextSaving_Object = MibTableColumn
xcmPrtInterpContextSaving = _XcmPrtInterpContextSaving_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 3),
    _XcmPrtInterpContextSaving_Type()
)
xcmPrtInterpContextSaving.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpContextSaving.setStatus("current")


class _XcmPrtInterpEdgeEnhancement_Type(PresentOnOff):
    """Custom type xcmPrtInterpEdgeEnhancement based on PresentOnOff"""


_XcmPrtInterpEdgeEnhancement_Object = MibTableColumn
xcmPrtInterpEdgeEnhancement = _XcmPrtInterpEdgeEnhancement_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 4),
    _XcmPrtInterpEdgeEnhancement_Type()
)
xcmPrtInterpEdgeEnhancement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpEdgeEnhancement.setStatus("current")


class _XcmPrtInterpFontIndexDefault_Type(Integer32):
    """Custom type xcmPrtInterpFontIndexDefault based on Integer32"""
    defaultValue = -2


_XcmPrtInterpFontIndexDefault_Object = MibTableColumn
xcmPrtInterpFontIndexDefault = _XcmPrtInterpFontIndexDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 5),
    _XcmPrtInterpFontIndexDefault_Type()
)
xcmPrtInterpFontIndexDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpFontIndexDefault.setStatus("current")
_XcmPrtInterpGrayLevels_Type = Cardinal32
_XcmPrtInterpGrayLevels_Object = MibTableColumn
xcmPrtInterpGrayLevels = _XcmPrtInterpGrayLevels_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 6),
    _XcmPrtInterpGrayLevels_Type()
)
xcmPrtInterpGrayLevels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpGrayLevels.setStatus("current")
_XcmPrtInterpGrayLevelDefault_Type = Cardinal32
_XcmPrtInterpGrayLevelDefault_Object = MibTableColumn
xcmPrtInterpGrayLevelDefault = _XcmPrtInterpGrayLevelDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 7),
    _XcmPrtInterpGrayLevelDefault_Type()
)
xcmPrtInterpGrayLevelDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpGrayLevelDefault.setStatus("current")


class _XcmPrtInterpJamRecovery_Type(PresentOnOff):
    """Custom type xcmPrtInterpJamRecovery based on PresentOnOff"""


_XcmPrtInterpJamRecovery_Object = MibTableColumn
xcmPrtInterpJamRecovery = _XcmPrtInterpJamRecovery_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 8),
    _XcmPrtInterpJamRecovery_Type()
)
xcmPrtInterpJamRecovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpJamRecovery.setStatus("current")


class _XcmPrtInterpJobCopiesDefault_Type(Ordinal32):
    """Custom type xcmPrtInterpJobCopiesDefault based on Ordinal32"""
    defaultValue = 1


_XcmPrtInterpJobCopiesDefault_Object = MibTableColumn
xcmPrtInterpJobCopiesDefault = _XcmPrtInterpJobCopiesDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 9),
    _XcmPrtInterpJobCopiesDefault_Type()
)
xcmPrtInterpJobCopiesDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpJobCopiesDefault.setStatus("current")


class _XcmPrtInterpLineWrap_Type(PresentOnOff):
    """Custom type xcmPrtInterpLineWrap based on PresentOnOff"""


_XcmPrtInterpLineWrap_Object = MibTableColumn
xcmPrtInterpLineWrap = _XcmPrtInterpLineWrap_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 10),
    _XcmPrtInterpLineWrap_Type()
)
xcmPrtInterpLineWrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpLineWrap.setStatus("current")


class _XcmPrtInterpMediumSizeDefault_Type(XcmPrtMediumSize):
    """Custom type xcmPrtInterpMediumSizeDefault based on XcmPrtMediumSize"""


_XcmPrtInterpMediumSizeDefault_Object = MibTableColumn
xcmPrtInterpMediumSizeDefault = _XcmPrtInterpMediumSizeDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 11),
    _XcmPrtInterpMediumSizeDefault_Type()
)
xcmPrtInterpMediumSizeDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpMediumSizeDefault.setStatus("current")


class _XcmPrtInterpPageProtect_Type(PresentOnOff):
    """Custom type xcmPrtInterpPageProtect based on PresentOnOff"""


_XcmPrtInterpPageProtect_Object = MibTableColumn
xcmPrtInterpPageProtect = _XcmPrtInterpPageProtect_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 12),
    _XcmPrtInterpPageProtect_Type()
)
xcmPrtInterpPageProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPageProtect.setStatus("current")


class _XcmPrtInterpPageProtectSize_Type(XcmPrtMediumSize):
    """Custom type xcmPrtInterpPageProtectSize based on XcmPrtMediumSize"""


_XcmPrtInterpPageProtectSize_Object = MibTableColumn
xcmPrtInterpPageProtectSize = _XcmPrtInterpPageProtectSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 13),
    _XcmPrtInterpPageProtectSize_Type()
)
xcmPrtInterpPageProtectSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPageProtectSize.setStatus("current")


class _XcmPrtInterpPageSizeErrorPolicy_Type(XcmPrtPageSizeErrorPolicy):
    """Custom type xcmPrtInterpPageSizeErrorPolicy based on XcmPrtPageSizeErrorPolicy"""


_XcmPrtInterpPageSizeErrorPolicy_Object = MibTableColumn
xcmPrtInterpPageSizeErrorPolicy = _XcmPrtInterpPageSizeErrorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 14),
    _XcmPrtInterpPageSizeErrorPolicy_Type()
)
xcmPrtInterpPageSizeErrorPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPageSizeErrorPolicy.setStatus("current")
_XcmPrtInterpPlexSupported_Type = XcmPrtPlex
_XcmPrtInterpPlexSupported_Object = MibTableColumn
xcmPrtInterpPlexSupported = _XcmPrtInterpPlexSupported_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 15),
    _XcmPrtInterpPlexSupported_Type()
)
xcmPrtInterpPlexSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPlexSupported.setStatus("current")
_XcmPrtInterpPlexDefault_Type = XcmPrtPlex
_XcmPrtInterpPlexDefault_Object = MibTableColumn
xcmPrtInterpPlexDefault = _XcmPrtInterpPlexDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 16),
    _XcmPrtInterpPlexDefault_Type()
)
xcmPrtInterpPlexDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPlexDefault.setStatus("current")


class _XcmPrtInterpPrintEdgeToEdge_Type(PresentOnOff):
    """Custom type xcmPrtInterpPrintEdgeToEdge based on PresentOnOff"""


_XcmPrtInterpPrintEdgeToEdge_Object = MibTableColumn
xcmPrtInterpPrintEdgeToEdge = _XcmPrtInterpPrintEdgeToEdge_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 17),
    _XcmPrtInterpPrintEdgeToEdge_Type()
)
xcmPrtInterpPrintEdgeToEdge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPrintEdgeToEdge.setStatus("current")


class _XcmPrtInterpPrintQuality_Type(XcmPrtPrintQuality):
    """Custom type xcmPrtInterpPrintQuality based on XcmPrtPrintQuality"""


_XcmPrtInterpPrintQuality_Object = MibTableColumn
xcmPrtInterpPrintQuality = _XcmPrtInterpPrintQuality_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 18),
    _XcmPrtInterpPrintQuality_Type()
)
xcmPrtInterpPrintQuality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPrintQuality.setStatus("current")
_XcmPrtInterpPrtInputIndexDflt_Type = Cardinal32
_XcmPrtInterpPrtInputIndexDflt_Object = MibTableColumn
xcmPrtInterpPrtInputIndexDflt = _XcmPrtInterpPrtInputIndexDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 19),
    _XcmPrtInterpPrtInputIndexDflt_Type()
)
xcmPrtInterpPrtInputIndexDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPrtInputIndexDflt.setStatus("current")
_XcmPrtInterpPrtOutputIndexDflt_Type = Cardinal32
_XcmPrtInterpPrtOutputIndexDflt_Object = MibTableColumn
xcmPrtInterpPrtOutputIndexDflt = _XcmPrtInterpPrtOutputIndexDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 20),
    _XcmPrtInterpPrtOutputIndexDflt_Type()
)
xcmPrtInterpPrtOutputIndexDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPrtOutputIndexDflt.setStatus("current")
_XcmPrtInterpResFeedDirDefault_Type = Cardinal32
_XcmPrtInterpResFeedDirDefault_Object = MibTableColumn
xcmPrtInterpResFeedDirDefault = _XcmPrtInterpResFeedDirDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 21),
    _XcmPrtInterpResFeedDirDefault_Type()
)
xcmPrtInterpResFeedDirDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpResFeedDirDefault.setStatus("current")
_XcmPrtInterpResXFeedDirDefault_Type = Cardinal32
_XcmPrtInterpResXFeedDirDefault_Object = MibTableColumn
xcmPrtInterpResXFeedDirDefault = _XcmPrtInterpResXFeedDirDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 22),
    _XcmPrtInterpResXFeedDirDefault_Type()
)
xcmPrtInterpResXFeedDirDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpResXFeedDirDefault.setStatus("current")
_XcmPrtInterpResIPResIndex_Type = Cardinal32
_XcmPrtInterpResIPResIndex_Object = MibTableColumn
xcmPrtInterpResIPResIndex = _XcmPrtInterpResIPResIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 23),
    _XcmPrtInterpResIPResIndex_Type()
)
xcmPrtInterpResIPResIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpResIPResIndex.setStatus("current")
_XcmPrtInterpResIPResIndexDflt_Type = Cardinal32
_XcmPrtInterpResIPResIndexDflt_Object = MibTableColumn
xcmPrtInterpResIPResIndexDflt = _XcmPrtInterpResIPResIndexDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 24),
    _XcmPrtInterpResIPResIndexDflt_Type()
)
xcmPrtInterpResIPResIndexDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpResIPResIndexDflt.setStatus("current")
_XcmPrtInterpTextFormLength_Type = Cardinal32
_XcmPrtInterpTextFormLength_Object = MibTableColumn
xcmPrtInterpTextFormLength = _XcmPrtInterpTextFormLength_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 25),
    _XcmPrtInterpTextFormLength_Type()
)
xcmPrtInterpTextFormLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpTextFormLength.setStatus("current")
_XcmPrtInterpTimeoutJob_Type = Cardinal32
_XcmPrtInterpTimeoutJob_Object = MibTableColumn
xcmPrtInterpTimeoutJob = _XcmPrtInterpTimeoutJob_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 26),
    _XcmPrtInterpTimeoutJob_Type()
)
xcmPrtInterpTimeoutJob.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpTimeoutJob.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpTimeoutJob.setUnits("Seconds")
_XcmPrtInterpTimeoutPage_Type = Cardinal32
_XcmPrtInterpTimeoutPage_Object = MibTableColumn
xcmPrtInterpTimeoutPage = _XcmPrtInterpTimeoutPage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 27),
    _XcmPrtInterpTimeoutPage_Type()
)
xcmPrtInterpTimeoutPage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpTimeoutPage.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpTimeoutPage.setUnits("Seconds")
_XcmPrtInterpInputAliasIndexDflt_Type = Cardinal32
_XcmPrtInterpInputAliasIndexDflt_Object = MibTableColumn
xcmPrtInterpInputAliasIndexDflt = _XcmPrtInterpInputAliasIndexDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 28),
    _XcmPrtInterpInputAliasIndexDflt_Type()
)
xcmPrtInterpInputAliasIndexDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpInputAliasIndexDflt.setStatus("current")


class _XcmPrtInterpTraySwitch_Type(XcmPrtTraySwitch):
    """Custom type xcmPrtInterpTraySwitch based on XcmPrtTraySwitch"""


_XcmPrtInterpTraySwitch_Object = MibTableColumn
xcmPrtInterpTraySwitch = _XcmPrtInterpTraySwitch_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 29),
    _XcmPrtInterpTraySwitch_Type()
)
xcmPrtInterpTraySwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpTraySwitch.setStatus("current")


class _XcmPrtInterpMediumTypeDefault_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmPrtInterpMediumTypeDefault based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtInterpMediumTypeDefault_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmPrtInterpMediumTypeDefault_Object = MibTableColumn
xcmPrtInterpMediumTypeDefault = _XcmPrtInterpMediumTypeDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 30),
    _XcmPrtInterpMediumTypeDefault_Type()
)
xcmPrtInterpMediumTypeDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpMediumTypeDefault.setStatus("current")


class _XcmPrtInterpMediaTypeErrPolicy_Type(XcmPrtMediaTypeErrorPolicy):
    """Custom type xcmPrtInterpMediaTypeErrPolicy based on XcmPrtMediaTypeErrorPolicy"""


_XcmPrtInterpMediaTypeErrPolicy_Object = MibTableColumn
xcmPrtInterpMediaTypeErrPolicy = _XcmPrtInterpMediaTypeErrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 31),
    _XcmPrtInterpMediaTypeErrPolicy_Type()
)
xcmPrtInterpMediaTypeErrPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpMediaTypeErrPolicy.setStatus("current")
_XcmPrtInterpErrorPolicyTimeout_Type = Cardinal32
_XcmPrtInterpErrorPolicyTimeout_Object = MibTableColumn
xcmPrtInterpErrorPolicyTimeout = _XcmPrtInterpErrorPolicyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 32),
    _XcmPrtInterpErrorPolicyTimeout_Type()
)
xcmPrtInterpErrorPolicyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpErrorPolicyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpErrorPolicyTimeout.setUnits("Seconds")


class _XcmPrtInterpLineTerm_Type(PresentOnOff):
    """Custom type xcmPrtInterpLineTerm based on PresentOnOff"""


_XcmPrtInterpLineTerm_Object = MibTableColumn
xcmPrtInterpLineTerm = _XcmPrtInterpLineTerm_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 33),
    _XcmPrtInterpLineTerm_Type()
)
xcmPrtInterpLineTerm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpLineTerm.setStatus("current")


class _XcmPrtInterpEnhancedResolution_Type(PresentOnOff):
    """Custom type xcmPrtInterpEnhancedResolution based on PresentOnOff"""


_XcmPrtInterpEnhancedResolution_Object = MibTableColumn
xcmPrtInterpEnhancedResolution = _XcmPrtInterpEnhancedResolution_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 34),
    _XcmPrtInterpEnhancedResolution_Type()
)
xcmPrtInterpEnhancedResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpEnhancedResolution.setStatus("current")


class _XcmPrtInterpAutoContinue_Type(PresentOnOff):
    """Custom type xcmPrtInterpAutoContinue based on PresentOnOff"""


_XcmPrtInterpAutoContinue_Object = MibTableColumn
xcmPrtInterpAutoContinue = _XcmPrtInterpAutoContinue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 50),
    _XcmPrtInterpAutoContinue_Type()
)
xcmPrtInterpAutoContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpAutoContinue.setStatus("current")


class _XcmPrtInterpEnvFeederSize_Type(XcmPrtMediumSize):
    """Custom type xcmPrtInterpEnvFeederSize based on XcmPrtMediumSize"""


_XcmPrtInterpEnvFeederSize_Object = MibTableColumn
xcmPrtInterpEnvFeederSize = _XcmPrtInterpEnvFeederSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 51),
    _XcmPrtInterpEnvFeederSize_Type()
)
xcmPrtInterpEnvFeederSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpEnvFeederSize.setStatus("current")


class _XcmPrtInterpManualFeedPgSize_Type(XcmPrtMediumSize):
    """Custom type xcmPrtInterpManualFeedPgSize based on XcmPrtMediumSize"""


_XcmPrtInterpManualFeedPgSize_Object = MibTableColumn
xcmPrtInterpManualFeedPgSize = _XcmPrtInterpManualFeedPgSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 52),
    _XcmPrtInterpManualFeedPgSize_Type()
)
xcmPrtInterpManualFeedPgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpManualFeedPgSize.setStatus("current")


class _XcmPrtInterpOffsetStackingType_Type(XcmPrtOutputOffsetStackingType):
    """Custom type xcmPrtInterpOffsetStackingType based on XcmPrtOutputOffsetStackingType"""


_XcmPrtInterpOffsetStackingType_Object = MibTableColumn
xcmPrtInterpOffsetStackingType = _XcmPrtInterpOffsetStackingType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 53),
    _XcmPrtInterpOffsetStackingType_Type()
)
xcmPrtInterpOffsetStackingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpOffsetStackingType.setStatus("current")


class _XcmPrtInterpProcessBarcodes_Type(PresentOnOff):
    """Custom type xcmPrtInterpProcessBarcodes based on PresentOnOff"""


_XcmPrtInterpProcessBarcodes_Object = MibTableColumn
xcmPrtInterpProcessBarcodes = _XcmPrtInterpProcessBarcodes_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 54),
    _XcmPrtInterpProcessBarcodes_Type()
)
xcmPrtInterpProcessBarcodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpProcessBarcodes.setStatus("current")
_XcmPrtInputAlias_ObjectIdentity = ObjectIdentity
xcmPrtInputAlias = _XcmPrtInputAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 50)
)
_XcmPrtInputAliasTable_Object = MibTable
xcmPrtInputAliasTable = _XcmPrtInputAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 50, 1)
)
if mibBuilder.loadTexts:
    xcmPrtInputAliasTable.setStatus("current")
_XcmPrtInputAliasEntry_Object = MibTableRow
xcmPrtInputAliasEntry = _XcmPrtInputAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 50, 1, 1)
)
xcmPrtInputAliasEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtInterpreterIndex"),
    (0, "XEROX-PRINTER-EXT-MIB", "xcmPrtInputAliasIndex"),
)
if mibBuilder.loadTexts:
    xcmPrtInputAliasEntry.setStatus("current")
_XcmPrtInputAliasIndex_Type = Cardinal32
_XcmPrtInputAliasIndex_Object = MibTableColumn
xcmPrtInputAliasIndex = _XcmPrtInputAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 50, 1, 1, 1),
    _XcmPrtInputAliasIndex_Type()
)
xcmPrtInputAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmPrtInputAliasIndex.setStatus("current")
_XcmPrtInputAliasRowStatus_Type = RowStatus
_XcmPrtInputAliasRowStatus_Object = MibTableColumn
xcmPrtInputAliasRowStatus = _XcmPrtInputAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 50, 1, 1, 2),
    _XcmPrtInputAliasRowStatus_Type()
)
xcmPrtInputAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputAliasRowStatus.setStatus("current")


class _XcmPrtInputAliasName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmPrtInputAliasName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XcmPrtInputAliasName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmPrtInputAliasName_Object = MibTableColumn
xcmPrtInputAliasName = _XcmPrtInputAliasName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 50, 1, 1, 3),
    _XcmPrtInputAliasName_Type()
)
xcmPrtInputAliasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputAliasName.setStatus("current")


class _XcmPrtInputAliasSwitchProgram_Type(DisplayString):
    """Custom type xcmPrtInputAliasSwitchProgram based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtInputAliasSwitchProgram_Type.__name__ = "DisplayString"
_XcmPrtInputAliasSwitchProgram_Object = MibTableColumn
xcmPrtInputAliasSwitchProgram = _XcmPrtInputAliasSwitchProgram_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 50, 1, 1, 4),
    _XcmPrtInputAliasSwitchProgram_Type()
)
xcmPrtInputAliasSwitchProgram.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputAliasSwitchProgram.setStatus("current")
_XcmPrtAuxSheet_ObjectIdentity = ObjectIdentity
xcmPrtAuxSheet = _XcmPrtAuxSheet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 52)
)
_XcmPrtAuxPackage_ObjectIdentity = ObjectIdentity
xcmPrtAuxPackage = _XcmPrtAuxPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60)
)
_XcmPrtAuxPackageTable_Object = MibTable
xcmPrtAuxPackageTable = _XcmPrtAuxPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1)
)
if mibBuilder.loadTexts:
    xcmPrtAuxPackageTable.setStatus("current")
_XcmPrtAuxPackageEntry_Object = MibTableRow
xcmPrtAuxPackageEntry = _XcmPrtAuxPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1)
)
xcmPrtAuxPackageEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-PRINTER-EXT-MIB", "xcmPrtAuxPackageIndex"),
)
if mibBuilder.loadTexts:
    xcmPrtAuxPackageEntry.setStatus("current")
_XcmPrtAuxPackageIndex_Type = Cardinal32
_XcmPrtAuxPackageIndex_Object = MibTableColumn
xcmPrtAuxPackageIndex = _XcmPrtAuxPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 1),
    _XcmPrtAuxPackageIndex_Type()
)
xcmPrtAuxPackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageIndex.setStatus("current")
_XcmPrtAuxPackageRowStatus_Type = RowStatus
_XcmPrtAuxPackageRowStatus_Object = MibTableColumn
xcmPrtAuxPackageRowStatus = _XcmPrtAuxPackageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 2),
    _XcmPrtAuxPackageRowStatus_Type()
)
xcmPrtAuxPackageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageRowStatus.setStatus("current")
_XcmPrtAuxPackageType_Type = XcmPrtAuxSheetType
_XcmPrtAuxPackageType_Object = MibTableColumn
xcmPrtAuxPackageType = _XcmPrtAuxPackageType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 3),
    _XcmPrtAuxPackageType_Type()
)
xcmPrtAuxPackageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageType.setStatus("current")


class _XcmPrtAuxPackageContent_Type(XcmPrtAuxSheetContent):
    """Custom type xcmPrtAuxPackageContent based on XcmPrtAuxSheetContent"""


_XcmPrtAuxPackageContent_Object = MibTableColumn
xcmPrtAuxPackageContent = _XcmPrtAuxPackageContent_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 4),
    _XcmPrtAuxPackageContent_Type()
)
xcmPrtAuxPackageContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageContent.setStatus("current")
_XcmPrtAuxPackagePrtInputIndex_Type = Cardinal32
_XcmPrtAuxPackagePrtInputIndex_Object = MibTableColumn
xcmPrtAuxPackagePrtInputIndex = _XcmPrtAuxPackagePrtInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 5),
    _XcmPrtAuxPackagePrtInputIndex_Type()
)
xcmPrtAuxPackagePrtInputIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtAuxPackagePrtInputIndex.setStatus("current")
_XcmPrtAuxPackageNext_Type = Cardinal32
_XcmPrtAuxPackageNext_Object = MibTableColumn
xcmPrtAuxPackageNext = _XcmPrtAuxPackageNext_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 6),
    _XcmPrtAuxPackageNext_Type()
)
xcmPrtAuxPackageNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageNext.setStatus("current")
_XcmPrtInterpPCL_ObjectIdentity = ObjectIdentity
xcmPrtInterpPCL = _XcmPrtInterpPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70)
)
_XcmPrtInterpPCLTable_Object = MibTable
xcmPrtInterpPCLTable = _XcmPrtInterpPCLTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1)
)
if mibBuilder.loadTexts:
    xcmPrtInterpPCLTable.setStatus("current")
_XcmPrtInterpPCLEntry_Object = MibTableRow
xcmPrtInterpPCLEntry = _XcmPrtInterpPCLEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1)
)
xcmPrtInterpPCLEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtInterpreterIndex"),
)
if mibBuilder.loadTexts:
    xcmPrtInterpPCLEntry.setStatus("current")
_XcmPrtInterpPCLRowStatus_Type = RowStatus
_XcmPrtInterpPCLRowStatus_Object = MibTableColumn
xcmPrtInterpPCLRowStatus = _XcmPrtInterpPCLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 1),
    _XcmPrtInterpPCLRowStatus_Type()
)
xcmPrtInterpPCLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLRowStatus.setStatus("current")


class _XcmPrtInterpPCLFontSourceDflt_Type(XcmPrtPCLFontSource):
    """Custom type xcmPrtInterpPCLFontSourceDflt based on XcmPrtPCLFontSource"""


_XcmPrtInterpPCLFontSourceDflt_Object = MibTableColumn
xcmPrtInterpPCLFontSourceDflt = _XcmPrtInterpPCLFontSourceDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 2),
    _XcmPrtInterpPCLFontSourceDflt_Type()
)
xcmPrtInterpPCLFontSourceDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLFontSourceDflt.setStatus("current")
_XcmPrtInterpPCLFontNumberDflt_Type = Cardinal32
_XcmPrtInterpPCLFontNumberDflt_Object = MibTableColumn
xcmPrtInterpPCLFontNumberDflt = _XcmPrtInterpPCLFontNumberDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 3),
    _XcmPrtInterpPCLFontNumberDflt_Type()
)
xcmPrtInterpPCLFontNumberDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLFontNumberDflt.setStatus("current")
_XcmPrtInterpPCLPitchNumerator_Type = Cardinal32
_XcmPrtInterpPCLPitchNumerator_Object = MibTableColumn
xcmPrtInterpPCLPitchNumerator = _XcmPrtInterpPCLPitchNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 4),
    _XcmPrtInterpPCLPitchNumerator_Type()
)
xcmPrtInterpPCLPitchNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPitchNumerator.setStatus("current")


class _XcmPrtInterpPCLPitchDenominator_Type(Cardinal32):
    """Custom type xcmPrtInterpPCLPitchDenominator based on Cardinal32"""
    defaultValue = 100


_XcmPrtInterpPCLPitchDenominator_Object = MibTableColumn
xcmPrtInterpPCLPitchDenominator = _XcmPrtInterpPCLPitchDenominator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 5),
    _XcmPrtInterpPCLPitchDenominator_Type()
)
xcmPrtInterpPCLPitchDenominator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPitchDenominator.setStatus("current")
_XcmPrtInterpPCLPtSizeNumerator_Type = Cardinal32
_XcmPrtInterpPCLPtSizeNumerator_Object = MibTableColumn
xcmPrtInterpPCLPtSizeNumerator = _XcmPrtInterpPCLPtSizeNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 6),
    _XcmPrtInterpPCLPtSizeNumerator_Type()
)
xcmPrtInterpPCLPtSizeNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPtSizeNumerator.setStatus("current")


class _XcmPrtInterpPCLPtSizeDenominatr_Type(Cardinal32):
    """Custom type xcmPrtInterpPCLPtSizeDenominatr based on Cardinal32"""
    defaultValue = 4


_XcmPrtInterpPCLPtSizeDenominatr_Object = MibTableColumn
xcmPrtInterpPCLPtSizeDenominatr = _XcmPrtInterpPCLPtSizeDenominatr_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 7),
    _XcmPrtInterpPCLPtSizeDenominatr_Type()
)
xcmPrtInterpPCLPtSizeDenominatr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPtSizeDenominatr.setStatus("current")


class _XcmPrtInterpPCLPrintScreen_Type(XcmPrtPrintScreen):
    """Custom type xcmPrtInterpPCLPrintScreen based on XcmPrtPrintScreen"""


_XcmPrtInterpPCLPrintScreen_Object = MibTableColumn
xcmPrtInterpPCLPrintScreen = _XcmPrtInterpPCLPrintScreen_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 50),
    _XcmPrtInterpPCLPrintScreen_Type()
)
xcmPrtInterpPCLPrintScreen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPrintScreen.setStatus("current")
_XcmPrtMediumTypeSupported_ObjectIdentity = ObjectIdentity
xcmPrtMediumTypeSupported = _XcmPrtMediumTypeSupported_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75)
)
_XcmPrtMedmTypeSupTable_Object = MibTable
xcmPrtMedmTypeSupTable = _XcmPrtMedmTypeSupTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2)
)
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupTable.setStatus("current")
_XcmPrtMedmTypeSupEntry_Object = MibTableRow
xcmPrtMedmTypeSupEntry = _XcmPrtMedmTypeSupEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1)
)
xcmPrtMedmTypeSupEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-PRINTER-EXT-MIB", "xcmPrtMedmTypeSupIndex"),
)
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupEntry.setStatus("current")
_XcmPrtMedmTypeSupIndex_Type = Ordinal32
_XcmPrtMedmTypeSupIndex_Object = MibTableColumn
xcmPrtMedmTypeSupIndex = _XcmPrtMedmTypeSupIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 1),
    _XcmPrtMedmTypeSupIndex_Type()
)
xcmPrtMedmTypeSupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupIndex.setStatus("current")
_XcmPrtMedmTypeSupRowStatus_Type = RowStatus
_XcmPrtMedmTypeSupRowStatus_Object = MibTableColumn
xcmPrtMedmTypeSupRowStatus = _XcmPrtMedmTypeSupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 2),
    _XcmPrtMedmTypeSupRowStatus_Type()
)
xcmPrtMedmTypeSupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupRowStatus.setStatus("current")


class _XcmPrtMedmTypeSupRowPersistence_Type(XcmGenRowPersistence):
    """Custom type xcmPrtMedmTypeSupRowPersistence based on XcmGenRowPersistence"""


_XcmPrtMedmTypeSupRowPersistence_Object = MibTableColumn
xcmPrtMedmTypeSupRowPersistence = _XcmPrtMedmTypeSupRowPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 3),
    _XcmPrtMedmTypeSupRowPersistence_Type()
)
xcmPrtMedmTypeSupRowPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupRowPersistence.setStatus("current")


class _XcmPrtMedmTypeSupName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmPrtMedmTypeSupName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtMedmTypeSupName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmPrtMedmTypeSupName_Object = MibTableColumn
xcmPrtMedmTypeSupName = _XcmPrtMedmTypeSupName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 4),
    _XcmPrtMedmTypeSupName_Type()
)
xcmPrtMedmTypeSupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupName.setStatus("current")


class _XcmPrtMedmTypeSupFuserTemp_Type(Integer32):
    """Custom type xcmPrtMedmTypeSupFuserTemp based on Integer32"""
    defaultValue = 50


_XcmPrtMedmTypeSupFuserTemp_Object = MibTableColumn
xcmPrtMedmTypeSupFuserTemp = _XcmPrtMedmTypeSupFuserTemp_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 5),
    _XcmPrtMedmTypeSupFuserTemp_Type()
)
xcmPrtMedmTypeSupFuserTemp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupFuserTemp.setStatus("current")


class _XcmPrtMedmTypeSupPaperType_Type(OctetString):
    """Custom type xcmPrtMedmTypeSupPaperType based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtMedmTypeSupPaperType_Type.__name__ = "OctetString"
_XcmPrtMedmTypeSupPaperType_Object = MibTableColumn
xcmPrtMedmTypeSupPaperType = _XcmPrtMedmTypeSupPaperType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 6),
    _XcmPrtMedmTypeSupPaperType_Type()
)
xcmPrtMedmTypeSupPaperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupPaperType.setStatus("current")


class _XcmPrtMedmTypeSupPDLString_Type(OctetString):
    """Custom type xcmPrtMedmTypeSupPDLString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmPrtMedmTypeSupPDLString_Type.__name__ = "OctetString"
_XcmPrtMedmTypeSupPDLString_Object = MibTableColumn
xcmPrtMedmTypeSupPDLString = _XcmPrtMedmTypeSupPDLString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 7),
    _XcmPrtMedmTypeSupPDLString_Type()
)
xcmPrtMedmTypeSupPDLString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupPDLString.setStatus("current")


class _XcmPrtMedmTypeSupFuserHide_Type(TruthValue):
    """Custom type xcmPrtMedmTypeSupFuserHide based on TruthValue"""


_XcmPrtMedmTypeSupFuserHide_Object = MibTableColumn
xcmPrtMedmTypeSupFuserHide = _XcmPrtMedmTypeSupFuserHide_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 8),
    _XcmPrtMedmTypeSupFuserHide_Type()
)
xcmPrtMedmTypeSupFuserHide.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupFuserHide.setStatus("current")

# Managed Objects groups

xcmPrtBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 1)
)
xcmPrtBaseGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtBaseRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtBaseGroupSupport"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtBaseUpdateSupport"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtBaseCreateSupport"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtBaseIETFMIBGroupSupport"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtBaseIETFMIBUpdateSupport"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtBaseIETFMIBCreateSupport"))
)
if mibBuilder.loadTexts:
    xcmPrtBaseGroup.setStatus("current")

xcmPrtGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 5)
)
xcmPrtGeneralGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralAuxSheetPackage"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralManualFeedTimeout"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralInputAutoSwitch"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralOutputAutoSwitch"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralMediumClassDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralDarknessLevels"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralDarknessLevelNorm"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralDarknessLevelDflt"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralHexDumpEnable"))
)
if mibBuilder.loadTexts:
    xcmPrtGeneralGroup.setStatus("current")

xcmPrtDriverOptionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 6)
)
xcmPrtDriverOptionsGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptStapler"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptDuplexUnit"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptPhaserBookletMaker"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptEnvelopeTray"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptCoilPunchUnit"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptFinisherDFA"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptHighCapacityFeeder"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDriverOutputDeliveryUnit"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptHardDrive"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptHolePunchUnit"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDriverInputPaperTrays"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptInserterUnit"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptJobAccountingFdi"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptFaxOut"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptMemoryInMBs"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptOutputBinSide"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptOutputBinCenter"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptPhaserModule"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptPrintEngine"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptSquareFoldTrimmer"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrHwdOptTriFold"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrFntCollation"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrFntAsciiJobTicket"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrFntAuthenticationMode"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrFntHoldForAuthenMode"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrFntEnhancedImageQualityMode"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrFntProductivityPack"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrFntJobStorage"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtDrvrFntJobAccountingSystem"))
)
if mibBuilder.loadTexts:
    xcmPrtDriverOptionsGroup.setStatus("current")

xcmPrtInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 8)
)
xcmPrtInputGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtInputRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInputNextPrtInputIndex"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInputUseCustomSize"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInputCustDimFeedDirDecl"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInputCustDimXFeedDirDecl"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInputTrayPriority"))
)
if mibBuilder.loadTexts:
    xcmPrtInputGroup.setStatus("current")

xcmPrtOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 9)
)
xcmPrtOutputGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputNextIndex"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputPassword"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputOffsetStackingType"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputTrayTimeoutSupport"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputTrayTimeout"))
)
if mibBuilder.loadTexts:
    xcmPrtOutputGroup.setStatus("current")

xcmPrtChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 14)
)
xcmPrtChannelGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelEOJTimeout"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelAuxSheetPackage"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelSpoolingEnable"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelLangSensing"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelBinaryPostScript"))
)
if mibBuilder.loadTexts:
    xcmPrtChannelGroup.setStatus("current")

xcmPrtInterpreterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 15)
)
xcmPrtInterpreterGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpAuxSheetPackage"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpContextSaving"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpEdgeEnhancement"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpFontIndexDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpGrayLevels"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpGrayLevelDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpJamRecovery"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpJobCopiesDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpLineWrap"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpMediumSizeDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPageProtect"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPageProtectSize"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPageSizeErrorPolicy"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPlexSupported"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPlexDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPrintEdgeToEdge"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPrintQuality"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPrtInputIndexDflt"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPrtOutputIndexDflt"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpResFeedDirDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpResXFeedDirDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpResIPResIndex"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpResIPResIndexDflt"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpTextFormLength"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpTimeoutJob"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpTimeoutPage"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpInputAliasIndexDflt"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpTraySwitch"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpMediumTypeDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpMediaTypeErrPolicy"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpErrorPolicyTimeout"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpLineTerm"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpEnhancedResolution"))
)
if mibBuilder.loadTexts:
    xcmPrtInterpreterGroup.setStatus("current")

xcmPrtInputAliasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 50)
)
xcmPrtInputAliasGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtInputAliasRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInputAliasName"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInputAliasSwitchProgram"))
)
if mibBuilder.loadTexts:
    xcmPrtInputAliasGroup.setStatus("current")

xcmPrtOutputFinishingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 51)
)
xcmPrtOutputFinishingGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputStaple"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputStaplePosSupported"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputStapleDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputStaplePosDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputPunch"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputPunchDefault"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputPunchPosSupported"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtOutputBookletFoldStaple"))
)
if mibBuilder.loadTexts:
    xcmPrtOutputFinishingGroup.setStatus("current")

xcmPrtGeneralAuxSheetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 52)
)
xcmPrtGeneralAuxSheetGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralStartupPage"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralBannerPage"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralEndBannerPage"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralTrayLowWarning"))
)
if mibBuilder.loadTexts:
    xcmPrtGeneralAuxSheetGroup.setStatus("current")

xcmPrtGeneralProdSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 55)
)
xcmPrtGeneralProdSpecificGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralScanlineCompaction"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralTonerLowStop"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtGeneralMonoPrintOptimization"))
)
if mibBuilder.loadTexts:
    xcmPrtGeneralProdSpecificGroup.setStatus("current")

xcmPrtAuxPackageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 60)
)
xcmPrtAuxPackageGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtAuxPackageRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtAuxPackageType"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtAuxPackageContent"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtAuxPackagePrtInputIndex"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtAuxPackageNext"))
)
if mibBuilder.loadTexts:
    xcmPrtAuxPackageGroup.setStatus("current")

xcmPrtChannelProdSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 64)
)
xcmPrtChannelProdSpecificGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelAutoJobEnd"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelBinaryPostScriptZ"))
)
if mibBuilder.loadTexts:
    xcmPrtChannelProdSpecificGroup.setStatus("current")

xcmPrtInterpProdSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 65)
)
xcmPrtInterpProdSpecificGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpAutoContinue"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpOffsetStackingType"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpEnvFeederSize"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpManualFeedPgSize"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpProcessBarcodes"))
)
if mibBuilder.loadTexts:
    xcmPrtInterpProdSpecificGroup.setStatus("current")

xcmPrtInterpPCLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 70)
)
xcmPrtInterpPCLGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPCLRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPCLFontSourceDflt"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPCLFontNumberDflt"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPCLPitchNumerator"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPCLPitchDenominator"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPCLPtSizeNumerator"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPCLPtSizeDenominatr"))
)
if mibBuilder.loadTexts:
    xcmPrtInterpPCLGroup.setStatus("current")

xcmPrtInterpPCLProdSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 71)
)
xcmPrtInterpPCLProdSpecificGroup.setObjects(
    ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPCLPrintScreen")
)
if mibBuilder.loadTexts:
    xcmPrtInterpPCLProdSpecificGroup.setStatus("current")

xcmPrtMediumTypeSupportedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 75)
)
xcmPrtMediumTypeSupportedGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtMedmTypeSupRowStatus"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtMedmTypeSupRowPersistence"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtMedmTypeSupName"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtMedmTypeSupFuserTemp"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtMedmTypeSupPaperType"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtMedmTypeSupPDLString"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtMedmTypeSupFuserHide"))
)
if mibBuilder.loadTexts:
    xcmPrtMediumTypeSupportedGroup.setStatus("current")


# Notification objects

xcmPrtGeneralConsoleLocalizationV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 2, 0, 1)
)
xcmPrtGeneralConsoleLocalizationV2Event.setObjects(
      *(("Printer-MIB", "prtConsoleLocalization"),
        ("Printer-MIB", "prtLocalizationLanguage"),
        ("Printer-MIB", "prtLocalizationCountry"),
        ("Printer-MIB", "prtLocalizationCharacterSet"))
)
if mibBuilder.loadTexts:
    xcmPrtGeneralConsoleLocalizationV2Event.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

xcmPrtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 1)
)
if mibBuilder.loadTexts:
    xcmPrtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-PRINTER-EXT-MIB",
    **{"xcmPrintMIB": xcmPrintMIB,
       "xcmPrtBase": xcmPrtBase,
       "xcmPrtBaseTable": xcmPrtBaseTable,
       "xcmPrtBaseEntry": xcmPrtBaseEntry,
       "xcmPrtBaseIndex": xcmPrtBaseIndex,
       "xcmPrtBaseRowStatus": xcmPrtBaseRowStatus,
       "xcmPrtBaseGroupSupport": xcmPrtBaseGroupSupport,
       "xcmPrtBaseUpdateSupport": xcmPrtBaseUpdateSupport,
       "xcmPrtBaseCreateSupport": xcmPrtBaseCreateSupport,
       "xcmPrtBaseIETFMIBGroupSupport": xcmPrtBaseIETFMIBGroupSupport,
       "xcmPrtBaseIETFMIBUpdateSupport": xcmPrtBaseIETFMIBUpdateSupport,
       "xcmPrtBaseIETFMIBCreateSupport": xcmPrtBaseIETFMIBCreateSupport,
       "xcmPrtMIBConformance": xcmPrtMIBConformance,
       "xcmPrtMIBCompliance": xcmPrtMIBCompliance,
       "xcmPrtMIBGroups": xcmPrtMIBGroups,
       "xcmPrtBaseGroup": xcmPrtBaseGroup,
       "xcmPrtGeneralGroup": xcmPrtGeneralGroup,
       "xcmPrtDriverOptionsGroup": xcmPrtDriverOptionsGroup,
       "xcmPrtInputGroup": xcmPrtInputGroup,
       "xcmPrtOutputGroup": xcmPrtOutputGroup,
       "xcmPrtChannelGroup": xcmPrtChannelGroup,
       "xcmPrtInterpreterGroup": xcmPrtInterpreterGroup,
       "xcmPrtInputAliasGroup": xcmPrtInputAliasGroup,
       "xcmPrtOutputFinishingGroup": xcmPrtOutputFinishingGroup,
       "xcmPrtGeneralAuxSheetGroup": xcmPrtGeneralAuxSheetGroup,
       "xcmPrtGeneralProdSpecificGroup": xcmPrtGeneralProdSpecificGroup,
       "xcmPrtAuxPackageGroup": xcmPrtAuxPackageGroup,
       "xcmPrtChannelProdSpecificGroup": xcmPrtChannelProdSpecificGroup,
       "xcmPrtInterpProdSpecificGroup": xcmPrtInterpProdSpecificGroup,
       "xcmPrtInterpPCLGroup": xcmPrtInterpPCLGroup,
       "xcmPrtInterpPCLProdSpecificGroup": xcmPrtInterpPCLProdSpecificGroup,
       "xcmPrtMediumTypeSupportedGroup": xcmPrtMediumTypeSupportedGroup,
       "xcmPrtGeneral": xcmPrtGeneral,
       "xcmPrtGeneralTable": xcmPrtGeneralTable,
       "xcmPrtGeneralEntry": xcmPrtGeneralEntry,
       "xcmPrtGeneralRowStatus": xcmPrtGeneralRowStatus,
       "xcmPrtGeneralAuxSheetPackage": xcmPrtGeneralAuxSheetPackage,
       "xcmPrtGeneralManualFeedTimeout": xcmPrtGeneralManualFeedTimeout,
       "xcmPrtGeneralInputAutoSwitch": xcmPrtGeneralInputAutoSwitch,
       "xcmPrtGeneralOutputAutoSwitch": xcmPrtGeneralOutputAutoSwitch,
       "xcmPrtGeneralMediumClassDefault": xcmPrtGeneralMediumClassDefault,
       "xcmPrtGeneralDarknessLevels": xcmPrtGeneralDarknessLevels,
       "xcmPrtGeneralDarknessLevelNorm": xcmPrtGeneralDarknessLevelNorm,
       "xcmPrtGeneralDarknessLevelDflt": xcmPrtGeneralDarknessLevelDflt,
       "xcmPrtGeneralHexDumpEnable": xcmPrtGeneralHexDumpEnable,
       "xcmPrtGeneralStartupPage": xcmPrtGeneralStartupPage,
       "xcmPrtGeneralBannerPage": xcmPrtGeneralBannerPage,
       "xcmPrtGeneralTonerLowStop": xcmPrtGeneralTonerLowStop,
       "xcmPrtGeneralEndBannerPage": xcmPrtGeneralEndBannerPage,
       "xcmPrtGeneralTrayLowWarning": xcmPrtGeneralTrayLowWarning,
       "xcmPrtGeneralScanlineCompaction": xcmPrtGeneralScanlineCompaction,
       "xcmPrtGeneralMonoPrintOptimization": xcmPrtGeneralMonoPrintOptimization,
       "xcmPrtGeneralInstalledFeeder": xcmPrtGeneralInstalledFeeder,
       "xcmPrtGeneralInstalledFinisher": xcmPrtGeneralInstalledFinisher,
       "xcmPrtGeneralInstalledAnalogFax": xcmPrtGeneralInstalledAnalogFax,
       "xcmPrtGeneralConsoleLocalizationV1EventOID": xcmPrtGeneralConsoleLocalizationV1EventOID,
       "xcmPrtGeneralConsoleLocalizationV2EventPrefix": xcmPrtGeneralConsoleLocalizationV2EventPrefix,
       "xcmPrtGeneralConsoleLocalizationV2Event": xcmPrtGeneralConsoleLocalizationV2Event,
       "xcmPrtDriverOptions": xcmPrtDriverOptions,
       "xcmPrtDrvrHwdOptStapler": xcmPrtDrvrHwdOptStapler,
       "xcmPrtDrvrHwdOptDuplexUnit": xcmPrtDrvrHwdOptDuplexUnit,
       "xcmPrtDrvrHwdOptPhaserBookletMaker": xcmPrtDrvrHwdOptPhaserBookletMaker,
       "xcmPrtDrvrHwdOptEnvelopeTray": xcmPrtDrvrHwdOptEnvelopeTray,
       "xcmPrtDrvrHwdOptCoilPunchUnit": xcmPrtDrvrHwdOptCoilPunchUnit,
       "xcmPrtDrvrHwdOptFinisherDFA": xcmPrtDrvrHwdOptFinisherDFA,
       "xcmPrtDrvrHwdOptHighCapacityFeeder": xcmPrtDrvrHwdOptHighCapacityFeeder,
       "xcmPrtDriverOutputDeliveryUnit": xcmPrtDriverOutputDeliveryUnit,
       "xcmPrtDrvrHwdOptHardDrive": xcmPrtDrvrHwdOptHardDrive,
       "xcmPrtDrvrHwdOptHolePunchUnit": xcmPrtDrvrHwdOptHolePunchUnit,
       "xcmPrtDriverInputPaperTrays": xcmPrtDriverInputPaperTrays,
       "xcmPrtDrvrHwdOptInserterUnit": xcmPrtDrvrHwdOptInserterUnit,
       "xcmPrtDrvrHwdOptJobAccountingFdi": xcmPrtDrvrHwdOptJobAccountingFdi,
       "xcmPrtDrvrHwdOptFaxOut": xcmPrtDrvrHwdOptFaxOut,
       "xcmPrtDrvrHwdOptMemoryInMBs": xcmPrtDrvrHwdOptMemoryInMBs,
       "xcmPrtDrvrHwdOptOutputBinSide": xcmPrtDrvrHwdOptOutputBinSide,
       "xcmPrtDrvrHwdOptOutputBinCenter": xcmPrtDrvrHwdOptOutputBinCenter,
       "xcmPrtDrvrHwdOptPhaserModule": xcmPrtDrvrHwdOptPhaserModule,
       "xcmPrtDrvrHwdOptPrintEngine": xcmPrtDrvrHwdOptPrintEngine,
       "xcmPrtDrvrHwdOptSquareFoldTrimmer": xcmPrtDrvrHwdOptSquareFoldTrimmer,
       "xcmPrtDrvrHwdOptTriFold": xcmPrtDrvrHwdOptTriFold,
       "xcmPrtDrvrFntCollation": xcmPrtDrvrFntCollation,
       "xcmPrtDrvrFntAsciiJobTicket": xcmPrtDrvrFntAsciiJobTicket,
       "xcmPrtDrvrFntAuthenticationMode": xcmPrtDrvrFntAuthenticationMode,
       "xcmPrtDrvrFntHoldForAuthenMode": xcmPrtDrvrFntHoldForAuthenMode,
       "xcmPrtDrvrFntEnhancedImageQualityMode": xcmPrtDrvrFntEnhancedImageQualityMode,
       "xcmPrtDrvrFntProductivityPack": xcmPrtDrvrFntProductivityPack,
       "xcmPrtDrvrFntJobStorage": xcmPrtDrvrFntJobStorage,
       "xcmPrtDrvrFntJobAccountingSystem": xcmPrtDrvrFntJobAccountingSystem,
       "xcmPrtInput": xcmPrtInput,
       "xcmPrtInputTable": xcmPrtInputTable,
       "xcmPrtInputEntry": xcmPrtInputEntry,
       "xcmPrtInputRowStatus": xcmPrtInputRowStatus,
       "xcmPrtInputNextPrtInputIndex": xcmPrtInputNextPrtInputIndex,
       "xcmPrtInputUseCustomSize": xcmPrtInputUseCustomSize,
       "xcmPrtInputCustDimFeedDirDecl": xcmPrtInputCustDimFeedDirDecl,
       "xcmPrtInputCustDimXFeedDirDecl": xcmPrtInputCustDimXFeedDirDecl,
       "xcmPrtInputTrayPriority": xcmPrtInputTrayPriority,
       "xcmPrtInputTrayTable": xcmPrtInputTrayTable,
       "xcmPrtInputTrayEntry": xcmPrtInputTrayEntry,
       "xcmPrtInputTraysRowStatus": xcmPrtInputTraysRowStatus,
       "xcmPrtInputTraysInstalled": xcmPrtInputTraysInstalled,
       "xcmPrtInputTraysConfiguration": xcmPrtInputTraysConfiguration,
       "xcmPrtOutput": xcmPrtOutput,
       "xcmPrtOutputTable": xcmPrtOutputTable,
       "xcmPrtOutputEntry": xcmPrtOutputEntry,
       "xcmPrtOutputRowStatus": xcmPrtOutputRowStatus,
       "xcmPrtOutputNextIndex": xcmPrtOutputNextIndex,
       "xcmPrtOutputPassword": xcmPrtOutputPassword,
       "xcmPrtOutputOffsetStackingType": xcmPrtOutputOffsetStackingType,
       "xcmPrtOutputTrayTimeoutSupport": xcmPrtOutputTrayTimeoutSupport,
       "xcmPrtOutputTrayTimeout": xcmPrtOutputTrayTimeout,
       "xcmPrtOutputStaple": xcmPrtOutputStaple,
       "xcmPrtOutputStaplePosSupported": xcmPrtOutputStaplePosSupported,
       "xcmPrtOutputStapleDefault": xcmPrtOutputStapleDefault,
       "xcmPrtOutputStaplePosDefault": xcmPrtOutputStaplePosDefault,
       "xcmPrtOutputPunch": xcmPrtOutputPunch,
       "xcmPrtOutputPunchDefault": xcmPrtOutputPunchDefault,
       "xcmPrtOutputPunchPosSupported": xcmPrtOutputPunchPosSupported,
       "xcmPrtOutputBookletFoldStaple": xcmPrtOutputBookletFoldStaple,
       "xcmPrtChannel": xcmPrtChannel,
       "xcmPrtChannelTable": xcmPrtChannelTable,
       "xcmPrtChannelEntry": xcmPrtChannelEntry,
       "xcmPrtChannelRowStatus": xcmPrtChannelRowStatus,
       "xcmPrtChannelEOJTimeout": xcmPrtChannelEOJTimeout,
       "xcmPrtChannelAuxSheetPackage": xcmPrtChannelAuxSheetPackage,
       "xcmPrtChannelSpoolingEnable": xcmPrtChannelSpoolingEnable,
       "xcmPrtChannelLangSensing": xcmPrtChannelLangSensing,
       "xcmPrtChannelBinaryPostScript": xcmPrtChannelBinaryPostScript,
       "xcmPrtChannelAutoJobEnd": xcmPrtChannelAutoJobEnd,
       "xcmPrtChannelBinaryPostScriptZ": xcmPrtChannelBinaryPostScriptZ,
       "xcmPrtInterpreter": xcmPrtInterpreter,
       "xcmPrtInterpreterTable": xcmPrtInterpreterTable,
       "xcmPrtInterpreterEntry": xcmPrtInterpreterEntry,
       "xcmPrtInterpRowStatus": xcmPrtInterpRowStatus,
       "xcmPrtInterpAuxSheetPackage": xcmPrtInterpAuxSheetPackage,
       "xcmPrtInterpContextSaving": xcmPrtInterpContextSaving,
       "xcmPrtInterpEdgeEnhancement": xcmPrtInterpEdgeEnhancement,
       "xcmPrtInterpFontIndexDefault": xcmPrtInterpFontIndexDefault,
       "xcmPrtInterpGrayLevels": xcmPrtInterpGrayLevels,
       "xcmPrtInterpGrayLevelDefault": xcmPrtInterpGrayLevelDefault,
       "xcmPrtInterpJamRecovery": xcmPrtInterpJamRecovery,
       "xcmPrtInterpJobCopiesDefault": xcmPrtInterpJobCopiesDefault,
       "xcmPrtInterpLineWrap": xcmPrtInterpLineWrap,
       "xcmPrtInterpMediumSizeDefault": xcmPrtInterpMediumSizeDefault,
       "xcmPrtInterpPageProtect": xcmPrtInterpPageProtect,
       "xcmPrtInterpPageProtectSize": xcmPrtInterpPageProtectSize,
       "xcmPrtInterpPageSizeErrorPolicy": xcmPrtInterpPageSizeErrorPolicy,
       "xcmPrtInterpPlexSupported": xcmPrtInterpPlexSupported,
       "xcmPrtInterpPlexDefault": xcmPrtInterpPlexDefault,
       "xcmPrtInterpPrintEdgeToEdge": xcmPrtInterpPrintEdgeToEdge,
       "xcmPrtInterpPrintQuality": xcmPrtInterpPrintQuality,
       "xcmPrtInterpPrtInputIndexDflt": xcmPrtInterpPrtInputIndexDflt,
       "xcmPrtInterpPrtOutputIndexDflt": xcmPrtInterpPrtOutputIndexDflt,
       "xcmPrtInterpResFeedDirDefault": xcmPrtInterpResFeedDirDefault,
       "xcmPrtInterpResXFeedDirDefault": xcmPrtInterpResXFeedDirDefault,
       "xcmPrtInterpResIPResIndex": xcmPrtInterpResIPResIndex,
       "xcmPrtInterpResIPResIndexDflt": xcmPrtInterpResIPResIndexDflt,
       "xcmPrtInterpTextFormLength": xcmPrtInterpTextFormLength,
       "xcmPrtInterpTimeoutJob": xcmPrtInterpTimeoutJob,
       "xcmPrtInterpTimeoutPage": xcmPrtInterpTimeoutPage,
       "xcmPrtInterpInputAliasIndexDflt": xcmPrtInterpInputAliasIndexDflt,
       "xcmPrtInterpTraySwitch": xcmPrtInterpTraySwitch,
       "xcmPrtInterpMediumTypeDefault": xcmPrtInterpMediumTypeDefault,
       "xcmPrtInterpMediaTypeErrPolicy": xcmPrtInterpMediaTypeErrPolicy,
       "xcmPrtInterpErrorPolicyTimeout": xcmPrtInterpErrorPolicyTimeout,
       "xcmPrtInterpLineTerm": xcmPrtInterpLineTerm,
       "xcmPrtInterpEnhancedResolution": xcmPrtInterpEnhancedResolution,
       "xcmPrtInterpAutoContinue": xcmPrtInterpAutoContinue,
       "xcmPrtInterpEnvFeederSize": xcmPrtInterpEnvFeederSize,
       "xcmPrtInterpManualFeedPgSize": xcmPrtInterpManualFeedPgSize,
       "xcmPrtInterpOffsetStackingType": xcmPrtInterpOffsetStackingType,
       "xcmPrtInterpProcessBarcodes": xcmPrtInterpProcessBarcodes,
       "xcmPrtInputAlias": xcmPrtInputAlias,
       "xcmPrtInputAliasTable": xcmPrtInputAliasTable,
       "xcmPrtInputAliasEntry": xcmPrtInputAliasEntry,
       "xcmPrtInputAliasIndex": xcmPrtInputAliasIndex,
       "xcmPrtInputAliasRowStatus": xcmPrtInputAliasRowStatus,
       "xcmPrtInputAliasName": xcmPrtInputAliasName,
       "xcmPrtInputAliasSwitchProgram": xcmPrtInputAliasSwitchProgram,
       "xcmPrtAuxSheet": xcmPrtAuxSheet,
       "xcmPrtAuxPackage": xcmPrtAuxPackage,
       "xcmPrtAuxPackageTable": xcmPrtAuxPackageTable,
       "xcmPrtAuxPackageEntry": xcmPrtAuxPackageEntry,
       "xcmPrtAuxPackageIndex": xcmPrtAuxPackageIndex,
       "xcmPrtAuxPackageRowStatus": xcmPrtAuxPackageRowStatus,
       "xcmPrtAuxPackageType": xcmPrtAuxPackageType,
       "xcmPrtAuxPackageContent": xcmPrtAuxPackageContent,
       "xcmPrtAuxPackagePrtInputIndex": xcmPrtAuxPackagePrtInputIndex,
       "xcmPrtAuxPackageNext": xcmPrtAuxPackageNext,
       "xcmPrtInterpPCL": xcmPrtInterpPCL,
       "xcmPrtInterpPCLTable": xcmPrtInterpPCLTable,
       "xcmPrtInterpPCLEntry": xcmPrtInterpPCLEntry,
       "xcmPrtInterpPCLRowStatus": xcmPrtInterpPCLRowStatus,
       "xcmPrtInterpPCLFontSourceDflt": xcmPrtInterpPCLFontSourceDflt,
       "xcmPrtInterpPCLFontNumberDflt": xcmPrtInterpPCLFontNumberDflt,
       "xcmPrtInterpPCLPitchNumerator": xcmPrtInterpPCLPitchNumerator,
       "xcmPrtInterpPCLPitchDenominator": xcmPrtInterpPCLPitchDenominator,
       "xcmPrtInterpPCLPtSizeNumerator": xcmPrtInterpPCLPtSizeNumerator,
       "xcmPrtInterpPCLPtSizeDenominatr": xcmPrtInterpPCLPtSizeDenominatr,
       "xcmPrtInterpPCLPrintScreen": xcmPrtInterpPCLPrintScreen,
       "xcmPrtMediumTypeSupported": xcmPrtMediumTypeSupported,
       "xcmPrtMedmTypeSupTable": xcmPrtMedmTypeSupTable,
       "xcmPrtMedmTypeSupEntry": xcmPrtMedmTypeSupEntry,
       "xcmPrtMedmTypeSupIndex": xcmPrtMedmTypeSupIndex,
       "xcmPrtMedmTypeSupRowStatus": xcmPrtMedmTypeSupRowStatus,
       "xcmPrtMedmTypeSupRowPersistence": xcmPrtMedmTypeSupRowPersistence,
       "xcmPrtMedmTypeSupName": xcmPrtMedmTypeSupName,
       "xcmPrtMedmTypeSupFuserTemp": xcmPrtMedmTypeSupFuserTemp,
       "xcmPrtMedmTypeSupPaperType": xcmPrtMedmTypeSupPaperType,
       "xcmPrtMedmTypeSupPDLString": xcmPrtMedmTypeSupPDLString,
       "xcmPrtMedmTypeSupFuserHide": xcmPrtMedmTypeSupFuserHide}
)
