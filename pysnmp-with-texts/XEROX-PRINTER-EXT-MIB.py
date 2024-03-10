"""SNMP MIB module (XEROX-PRINTER-EXT-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-PRINTER-EXT-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:19 2024
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

(prtOutputEntry,
 prtInterpreterEntry,
 prtConsoleLocalization,
 prtLocalizationCharacterSet,
 prtLocalizationLanguage,
 prtInterpreterIndex,
 prtLocalizationCountry,
 prtInputEntry,
 prtChannelEntry,
 PresentOnOff,
 prtGeneralEntry) = mibBuilder.importSymbols(
    "Printer-MIB",
    "prtOutputEntry",
    "prtInterpreterEntry",
    "prtConsoleLocalization",
    "prtLocalizationCharacterSet",
    "prtLocalizationLanguage",
    "prtInterpreterIndex",
    "prtLocalizationCountry",
    "prtInputEntry",
    "prtChannelEntry",
    "PresentOnOff",
    "prtGeneralEntry")

(ModuleCompliance,
 ObjectGroup,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "ObjectGroup",
    "NotificationGroup")

(ModuleIdentity,
 IpAddress,
 MibIdentifier,
 Bits,
 NotificationType,
 Integer32,
 TimeTicks,
 Counter32,
 Unsigned32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Counter64,
 ObjectIdentity,
 iso,
 Gauge32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "ModuleIdentity",
    "IpAddress",
    "MibIdentifier",
    "Bits",
    "NotificationType",
    "Integer32",
    "TimeTicks",
    "Counter32",
    "Unsigned32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Counter64",
    "ObjectIdentity",
    "iso",
    "Gauge32")

(RowStatus,
 TextualConvention,
 DisplayString,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "RowStatus",
    "TextualConvention",
    "DisplayString",
    "TruthValue")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(XcmGenRowPersistence,
 Cardinal32,
 XcmFixedLocaleDisplayString,
 Ordinal32) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "XcmGenRowPersistence",
    "Cardinal32",
    "XcmFixedLocaleDisplayString",
    "Ordinal32")

(XcmPrtHolePunchUnitType,
 XcmPrtIETFPrintMIBGroupSupport,
 XcmPrtMediumClassType,
 XcmPrtAsciiJobTicketType,
 XcmPrtPrintQuality,
 XcmPrtAccountingSystemType,
 XcmPrtGroupSupport,
 XcmPrtMediumSize,
 XcmPrtFinisherDFAType,
 XcmPrtAuthenticationModeType,
 XcmPrtOutputPunchPosition,
 XcmPrtInputTraysConfiguration,
 XcmPrtAuxSheetType,
 XcmPrtAuxSheetContent,
 XcmPrtPlex,
 XcmPrtFaxOutType,
 XcmPrtPageSizeErrorPolicy,
 XcmPrtHighCapacityFeederType,
 XcmPrtPCLFontSource,
 XcmPrtOutputOffsetStackingType,
 XcmPrtOutputStaplePosition,
 XcmPrtHoldForAuthenModeType,
 XcmPrtGeneralMonoPrintOpt,
 XcmPrtPrintScreen,
 XcmPrtPrintEngineType,
 XcmPrtTraySwitch,
 XcmPrtMediaTypeErrorPolicy,
 XcmPrtPhaserModuleType) = mibBuilder.importSymbols(
    "XEROX-PRINTER-EXT-TC",
    "XcmPrtHolePunchUnitType",
    "XcmPrtIETFPrintMIBGroupSupport",
    "XcmPrtMediumClassType",
    "XcmPrtAsciiJobTicketType",
    "XcmPrtPrintQuality",
    "XcmPrtAccountingSystemType",
    "XcmPrtGroupSupport",
    "XcmPrtMediumSize",
    "XcmPrtFinisherDFAType",
    "XcmPrtAuthenticationModeType",
    "XcmPrtOutputPunchPosition",
    "XcmPrtInputTraysConfiguration",
    "XcmPrtAuxSheetType",
    "XcmPrtAuxSheetContent",
    "XcmPrtPlex",
    "XcmPrtFaxOutType",
    "XcmPrtPageSizeErrorPolicy",
    "XcmPrtHighCapacityFeederType",
    "XcmPrtPCLFontSource",
    "XcmPrtOutputOffsetStackingType",
    "XcmPrtOutputStaplePosition",
    "XcmPrtHoldForAuthenModeType",
    "XcmPrtGeneralMonoPrintOpt",
    "XcmPrtPrintScreen",
    "XcmPrtPrintEngineType",
    "XcmPrtTraySwitch",
    "XcmPrtMediaTypeErrorPolicy",
    "XcmPrtPhaserModuleType")


# MODULE-IDENTITY

xcmPrintMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55)
)
xcmPrintMIB.setLastUpdated("1304020000Z")
if mibBuilder.loadTexts:
    xcmPrintMIB.setOrganization("""\
Xerox Common Management Interface Working Group
""")
xcmPrintMIB.setContactInfo("""\
 XCMI Editors E-Mail: coherence@crt.xerox.com -- --
""")
if mibBuilder.loadTexts:
    xcmPrintMIB.setDescription("""\
 Version: 6.006.pub Xerox XCMI Extension to IETF Printer MIB Module. This
Module provides extension to the IETF Printer MIB. Copyright (C) 1997-2013
Xerox Corporation. All Rights Reserved.
""")


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
if mibBuilder.loadTexts:
    xcmPrtBaseTable.setDescription("""\
A table of general counters and information for ease of use of the XCMI
Extension to IETF Printer MIB Module and the IETF Printer MIB on this host
system. Usage: The ONLY valid row in the 'xcmPrtBaseTable' shall ALWAYS have an
'xcmPrtBaseIndex' of one ('1').
""")
_XcmPrtBaseEntry_Object = MibTableRow
xcmPrtBaseEntry = _XcmPrtBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1)
)
xcmPrtBaseEntry.setIndexNames(
    (0, "XEROX-PRINTER-EXT-MIB", "xcmPrtBaseIndex"),
)
if mibBuilder.loadTexts:
    xcmPrtBaseEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtBaseEntry.setDescription("""\
An entry of general counters and information for ease of use of the XCMI
Extension to IETF Printer MIB Module and the IETF Printer MIB on this host
system. Usage: The ONLY valid row in the 'xcmPrtBaseTable' shall ALWAYS have an
'xcmPrtBaseIndex' of one ('1').
""")
_XcmPrtBaseIndex_Type = Ordinal32
_XcmPrtBaseIndex_Object = MibTableColumn
xcmPrtBaseIndex = _XcmPrtBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 1),
    _XcmPrtBaseIndex_Type()
)
xcmPrtBaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmPrtBaseIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtBaseIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmPrtBaseTable'. Usage: The ONLY valid row in the 'xcmPrtBaseTable' shall
ALWAYS have an 'xcmPrtBaseIndex' of one ('1').
""")
_XcmPrtBaseRowStatus_Type = RowStatus
_XcmPrtBaseRowStatus_Object = MibTableColumn
xcmPrtBaseRowStatus = _XcmPrtBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 2),
    _XcmPrtBaseRowStatus_Type()
)
xcmPrtBaseRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtBaseRowStatus.setDescription("""\
This object is used to display status of the ONLY valid conceptual row in the
'xcmPrtBaseTable'. Usage: 'xcmPrtBaseRowStatus' is 'read-only' because the ONLY
valid conceptual row shall NOT be deleted.
""")
_XcmPrtBaseGroupSupport_Type = XcmPrtGroupSupport
_XcmPrtBaseGroupSupport_Object = MibTableColumn
xcmPrtBaseGroupSupport = _XcmPrtBaseGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 3),
    _XcmPrtBaseGroupSupport_Type()
)
xcmPrtBaseGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtBaseGroupSupport.setDescription("""\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional module objects which are supported by this management agent
implementation (ie, version) on this host system, specified in a bit-mask.
""")
_XcmPrtBaseUpdateSupport_Type = XcmPrtGroupSupport
_XcmPrtBaseUpdateSupport_Object = MibTableColumn
xcmPrtBaseUpdateSupport = _XcmPrtBaseUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 4),
    _XcmPrtBaseUpdateSupport_Type()
)
xcmPrtBaseUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtBaseUpdateSupport.setDescription("""\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional module objects which are supported for existing row update (via SNMP
Set-Request PDUs) by this management agent implementation (ie, version) on this
host system, specified in a bit-mask.
""")
_XcmPrtBaseCreateSupport_Type = XcmPrtGroupSupport
_XcmPrtBaseCreateSupport_Object = MibTableColumn
xcmPrtBaseCreateSupport = _XcmPrtBaseCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 5),
    _XcmPrtBaseCreateSupport_Type()
)
xcmPrtBaseCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtBaseCreateSupport.setDescription("""\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional module objects which are supported for dynamic row creation (via
'...RowStatus') by this management agent implementation (ie, version) on this
host system, specified in a bit-mask.
""")


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
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBGroupSupport.setReference("""\
See: IETF Printer MIB
""")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBGroupSupport.setDescription("""\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional module objects in the IETF Printer MIB which are supported by this
management agent implementation (ie, version) on this host system, specified in
a bit-mask.
""")
_XcmPrtBaseIETFMIBUpdateSupport_Type = XcmPrtIETFPrintMIBGroupSupport
_XcmPrtBaseIETFMIBUpdateSupport_Object = MibTableColumn
xcmPrtBaseIETFMIBUpdateSupport = _XcmPrtBaseIETFMIBUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 7),
    _XcmPrtBaseIETFMIBUpdateSupport_Type()
)
xcmPrtBaseIETFMIBUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBUpdateSupport.setReference("""\
See: IETF Printer MIB
""")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBUpdateSupport.setDescription("""\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional module objects in the IETF Printer MIB supported for existing row
update (via SNMP Set-Request PDUs) by this management agent implementation (ie,
version) on this host system, specified in a bit-mask.
""")
_XcmPrtBaseIETFMIBCreateSupport_Type = XcmPrtIETFPrintMIBGroupSupport
_XcmPrtBaseIETFMIBCreateSupport_Object = MibTableColumn
xcmPrtBaseIETFMIBCreateSupport = _XcmPrtBaseIETFMIBCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 1, 2, 1, 8),
    _XcmPrtBaseIETFMIBCreateSupport_Type()
)
xcmPrtBaseIETFMIBCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBCreateSupport.setReference("""\
See: IETF Printer MIB
""")
if mibBuilder.loadTexts:
    xcmPrtBaseIETFMIBCreateSupport.setDescription("""\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional module objects in the IETF Printer MIB supported for dynamic row
creation (via '...RowStatus') by this management agent implementation (ie,
version) on this host system, specified in a bit-mask. Currently there are no
groups within the IETF Printer MIB which provide for dynamic row creation, and
this object shall always return '0'. Dynamic row creation is provided to these
groups through the XCMI Extension to IETF Printer MIB Module, but CreateSupport
should be reflected in xcmPrtBaseCreateSupport. This object is included for
completeness.
""")
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
if mibBuilder.loadTexts:
    xcmPrtGeneralTable.setDescription("""\
 A table of general information per printer. This table augments the
prtGeneralTable.
""")
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
if mibBuilder.loadTexts:
    xcmPrtGeneralEntry.setDescription("""\
 An entry exists in this table for each device entry in the hostmib device
table whose type is printer.
""")
_XcmPrtGeneralRowStatus_Type = RowStatus
_XcmPrtGeneralRowStatus_Object = MibTableColumn
xcmPrtGeneralRowStatus = _XcmPrtGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 1),
    _XcmPrtGeneralRowStatus_Type()
)
xcmPrtGeneralRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtGeneralRowStatus.setDescription("""\
 Manages the status of this conceptual row in the xcmPrtGeneralTable.
""")
_XcmPrtGeneralAuxSheetPackage_Type = Cardinal32
_XcmPrtGeneralAuxSheetPackage_Object = MibTableColumn
xcmPrtGeneralAuxSheetPackage = _XcmPrtGeneralAuxSheetPackage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 2),
    _XcmPrtGeneralAuxSheetPackage_Type()
)
xcmPrtGeneralAuxSheetPackage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralAuxSheetPackage.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtGeneralAuxSheetPackage.setReference("""\
 See: xcmPrtInterpAuxSheetPackage See: xcmPrtChannelAuxSheetPackage See:
xcmPrtGeneralAuxSheetGroup - xcmPrtGeneralStartupPage See:
xcmPrtGeneralAuxSheetGroup - xcmPrtGeneralBannerPage See:
xcmPrtGeneralAuxSheetGroup - xcmPrtGeneralEndBannerPage
""")
if mibBuilder.loadTexts:
    xcmPrtGeneralAuxSheetPackage.setDescription("""\
 This object is an index into the xcmPrtAuxPackageTable. This table is used to
enable or disable printing of auxiliary sheets at the printer box level. The
value zero shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralManualFeedTimeout.setReference("""\
 This object copied from the April 1996 Printer MIB prtInputManualFeedTimeout
object. This object is currently in the prtInputTable. The XCMI WG will push in
June 1996 to move this object the prtGeneralTable as done here.
""")
if mibBuilder.loadTexts:
    xcmPrtGeneralManualFeedTimeout.setDescription("""\
 The duration in seconds after which the printer shall either: (a) switch to
another input subunit, if the value of prtInputNextIndex is non-zero and
prtGeneralAutoSwitch is on or (b) abort any job waiting for manually fed input,
if the value value of prtInputNextIndex is zero or prtGeneralAutoSwitch is off
or notPresent. The event which causes the printer to enter the waiting state is
product specific. A value of (-1) implies 'other' or 'infinite' which
translates to 'this input subunit doesn't support manual feed'. A value of (-2)
implies 'unknown'.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralInputAutoSwitch.setReference("""\
 This object copied from the April 1996 Printer MIB prtInputAutoSwitch object.
This object is currently in the prtInputTable. The XCMI WG will push in June
1996, to move this object the prtGeneralTable as done here.
""")
if mibBuilder.loadTexts:
    xcmPrtGeneralInputAutoSwitch.setDescription("""\
 Indicates the state of the auto input switching feature. The value notPresent
indicates the feature is not currently supported. Exact behavior of this
feature is product specific.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralOutputAutoSwitch.setDescription("""\
 Indicates the state of the auto output tray switching feature. The value
notPresent indicates the feature is not currently supported. Exact behavior of
this feature is product specific.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralMediumClassDefault.setDescription("""\
 This object sets the default medium size class for the printer. This object
sets the medium size for printer management functions such as printing the
configuration sheet. It may affect any media related object, such as form
length.
""")
_XcmPrtGeneralDarknessLevels_Type = Cardinal32
_XcmPrtGeneralDarknessLevels_Object = MibTableColumn
xcmPrtGeneralDarknessLevels = _XcmPrtGeneralDarknessLevels_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 7),
    _XcmPrtGeneralDarknessLevels_Type()
)
xcmPrtGeneralDarknessLevels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralDarknessLevels.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtGeneralDarknessLevels.setDescription("""\
 This value indicates the maximum number of darkness levels supported by this
printer. The level settings range from 1 to xcmPrtGeneralDarknessLevels where 1
represents the lightest level and xcmPrtGeneralDarknessLevels represents the
darkest level. The value 1 implies no user settables. The value 0 means
unspecified. The selection of a darkness levels specifies that the printer
shall process the page images so that they appear either 'lighter' or 'darker'.
""")
_XcmPrtGeneralDarknessLevelNorm_Type = Cardinal32
_XcmPrtGeneralDarknessLevelNorm_Object = MibTableColumn
xcmPrtGeneralDarknessLevelNorm = _XcmPrtGeneralDarknessLevelNorm_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 1, 1, 8),
    _XcmPrtGeneralDarknessLevelNorm_Type()
)
xcmPrtGeneralDarknessLevelNorm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtGeneralDarknessLevelNorm.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtGeneralDarknessLevelNorm.setDescription("""\
 The normal setting for the darkness printing object. The value 0 means
unspecified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralDarknessLevelDflt.setReference("""\
 See: PJL Technical Reference Manual - DENSITY
""")
if mibBuilder.loadTexts:
    xcmPrtGeneralDarknessLevelDflt.setDescription("""\
 The default setting for the density printing option. The value (-2) indicates
unknown. The value (-4) indicates the auto setting.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralHexDumpEnable.setReference("""\
 See: Printer MIB prtInterpreterLangFamily - langDiagnostic(41)
""")
if mibBuilder.loadTexts:
    xcmPrtGeneralHexDumpEnable.setDescription("""\
 This object controls whether the printer is in a special diagnostic mode
wherein all received print data is printed in hexadecimal format. Whether a
reset or power-cycles turns xcmPrtGeneralHexDumpEnable to Off is product
dependent.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralStartupPage.setReference("""\
 This object copied directly from the April 1996 version of the Printer MIB's
prtGeneralStartupPage object.
""")
if mibBuilder.loadTexts:
    xcmPrtGeneralStartupPage.setDescription("""\
 Used to enable or disable printing a startup page. If enabled, a startup page
will be printed shortly after power-up, when the device is ready. Typical
startup pages include test patterns and/or printer configuration information.
Usage: Conforming management agents, which ALSO implement the the Printer MIB
v2, SHALL set 'xcmPrtGeneralStartupPage' to the SAME value as
'prtAuxiliarySheetStartupPage' (i.e., the values of these two objects SHALL be
interlocked).
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralBannerPage.setReference("""\
 This object copied directly from the April 1996 version of the Printer MIB's
prtGeneralBannerPage object.
""")
if mibBuilder.loadTexts:
    xcmPrtGeneralBannerPage.setDescription("""\
 Used to enable or disable printing banner pages at the beginning of jobs. This
is a master switch which applies to all jobs, regardless of interpreter. Usage:
Conforming management agents, which ALSO implement the the Printer MIB v2,
SHALL set 'xcmPrtGeneralBannerPage' to the SAME value as
'prtAuxiliarySheetBannerPage' (i.e., the values of these two objects SHALL be
interlocked).
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralTonerLowStop.setDescription("""\
 Indicates the action taken when a low toner condition exists. 'on' indicates
that the printer will stop printing when then toner is low 'off' indicates that
printing will continue when the toner is low 'notPresent' indicates that the
printer has no selectable option for action under a low toner condition.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralEndBannerPage.setDescription("""\
 Used to enable or disable printing banner pages at the end of jobs. This is a
master switch which applies to all jobs, regardless of interpreter.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralTrayLowWarning.setDescription("""\
 Indicates the action taken when a input tray paper condition 'on' indicates
that the printer will report the warning over the user interfaces: Control
Panel, CWIS, SNMP, etc. 'off' indicates that printing will not report the
warning 'notPresent' indicates that the printer has no selectable option for a
low paper condition.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralScanlineCompaction.setReference("""\
 See: xcmPrtInterpPageProtect See: DocuPrint 4517 Network Laser Printers User
Guide, Pg. D-12
""")
if mibBuilder.loadTexts:
    xcmPrtGeneralScanlineCompaction.setDescription("""\
 This object enables a printing mode wherein the printer compresses selected
scanlines of raster image data as they are received and holds them in
compressed form until they are to be printed. This allows particular jobs to be
processed with less memory, but often reduced performance as well. On some
Printers, turning this feature Off is referred to as 'PerformanceEnhancement'.
When xcmInterpPageProtect is set to Off, some complex jobs may not print
successfully with minimum memory. The ScanlineCompaction feature enables
printing some complex jobs without resorting to reserving additional memory by
turning on the PageProtect option or installing additional memory.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralMonoPrintOptimization.setReference("""\
 See: Phaser 7750 User Guide... for more information
""")
if mibBuilder.loadTexts:
    xcmPrtGeneralMonoPrintOptimization.setDescription("""\
 This object enables a printing mode wherein the printer can be set to either
one of two modes overall. Mode 1 is Optimized for Speed, Mode 2 is Optimized
for Economy. This setting affects the overall performance of the printer and
thus affects all print quality modes.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralInstalledFeeder.setDescription("""\
 This object uniquely specifies the currently installed Feeder hardware. Its
purpose is to allow clients to determine via a single MIB object the number and
type of input trays and feeding options available, based exclusively on the
feeder that is installed.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralInstalledFinisher.setDescription("""\
 This object uniquely specifies the currently installed Finisher hardware. Its
purpose is to allow clients to determine via a single MIB object the number and
type of output trays and finishing options available, based exclusively on the
finisher that is installed.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralInstalledAnalogFax.setDescription("""\
 This object uniquely specifies the currently installed analog fax card. Its
purpose is to allow clients to determine via a single MIB object whether an
analog fax card is installed, and the options that are available based on the
fax card that is installed.
""")
_XcmPrtGeneralConsoleLocalizationV1EventOID_ObjectIdentity = ObjectIdentity
xcmPrtGeneralConsoleLocalizationV1EventOID = _XcmPrtGeneralConsoleLocalizationV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 5, 2)
)
if mibBuilder.loadTexts:
    xcmPrtGeneralConsoleLocalizationV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtGeneralConsoleLocalizationV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever
'prtConsoleLocalization' in the industry standard printer mib is updated. See
SNMPv2 trap definition 'xcmPrtGeneralConsoleLocalizationV2Event' below.
""")
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
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptStapler.setDescription("""\
Object that indicates if a Stapler Unit is installed within the print device.
""")
_XcmPrtDrvrHwdOptDuplexUnit_Type = PresentOnOff
_XcmPrtDrvrHwdOptDuplexUnit_Object = MibScalar
xcmPrtDrvrHwdOptDuplexUnit = _XcmPrtDrvrHwdOptDuplexUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 2),
    _XcmPrtDrvrHwdOptDuplexUnit_Type()
)
xcmPrtDrvrHwdOptDuplexUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptDuplexUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptDuplexUnit.setDescription("""\
Object that indicates if a Duplex Unit is installed within the print device.
""")
_XcmPrtDrvrHwdOptPhaserBookletMaker_Type = PresentOnOff
_XcmPrtDrvrHwdOptPhaserBookletMaker_Object = MibScalar
xcmPrtDrvrHwdOptPhaserBookletMaker = _XcmPrtDrvrHwdOptPhaserBookletMaker_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 3),
    _XcmPrtDrvrHwdOptPhaserBookletMaker_Type()
)
xcmPrtDrvrHwdOptPhaserBookletMaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptPhaserBookletMaker.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptPhaserBookletMaker.setDescription("""\
Object that indicates if a Booklet Maker Module is installed within the Phaser
print device.
""")
_XcmPrtDrvrHwdOptEnvelopeTray_Type = PresentOnOff
_XcmPrtDrvrHwdOptEnvelopeTray_Object = MibScalar
xcmPrtDrvrHwdOptEnvelopeTray = _XcmPrtDrvrHwdOptEnvelopeTray_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 4),
    _XcmPrtDrvrHwdOptEnvelopeTray_Type()
)
xcmPrtDrvrHwdOptEnvelopeTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptEnvelopeTray.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptEnvelopeTray.setDescription("""\
Object that indicates if an Envelope Tray is installed within the print device.
""")
_XcmPrtDrvrHwdOptCoilPunchUnit_Type = PresentOnOff
_XcmPrtDrvrHwdOptCoilPunchUnit_Object = MibScalar
xcmPrtDrvrHwdOptCoilPunchUnit = _XcmPrtDrvrHwdOptCoilPunchUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 5),
    _XcmPrtDrvrHwdOptCoilPunchUnit_Type()
)
xcmPrtDrvrHwdOptCoilPunchUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptCoilPunchUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptCoilPunchUnit.setDescription("""\
Object that indicates if a Coil Punch Unit is installed within the print
device.
""")
_XcmPrtDrvrHwdOptFinisherDFA_Type = XcmPrtFinisherDFAType
_XcmPrtDrvrHwdOptFinisherDFA_Object = MibScalar
xcmPrtDrvrHwdOptFinisherDFA = _XcmPrtDrvrHwdOptFinisherDFA_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 6),
    _XcmPrtDrvrHwdOptFinisherDFA_Type()
)
xcmPrtDrvrHwdOptFinisherDFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptFinisherDFA.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptFinisherDFA.setDescription("""\
Object that indicates the type of Finisher DFA that is installed within the
print device.
""")
_XcmPrtDrvrHwdOptHighCapacityFeeder_Type = XcmPrtHighCapacityFeederType
_XcmPrtDrvrHwdOptHighCapacityFeeder_Object = MibScalar
xcmPrtDrvrHwdOptHighCapacityFeeder = _XcmPrtDrvrHwdOptHighCapacityFeeder_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 7),
    _XcmPrtDrvrHwdOptHighCapacityFeeder_Type()
)
xcmPrtDrvrHwdOptHighCapacityFeeder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptHighCapacityFeeder.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptHighCapacityFeeder.setDescription("""\
Object that indicates the type of High Capacity Feeder that is installed within
the print device.
""")


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
if mibBuilder.loadTexts:
    xcmPrtDriverOutputDeliveryUnit.setDescription("""\
Object used to indicate the type of Output Delivery Units that are installed
within the print device. The contents of this object shall expose a string of
valid Output Delivery Unit name which are seperated by a comma. Valid Output
Delivery Unit type include: 'notInstalled' 'installed' 'phStacker' 'phAdvanced'
'phProfessional' 'offsetCatchTray' 'simpleCatchTray' 'outputBin500Support'
'octMailbox' 'sctMailbox' 'octMailboxStapler' 'sctMailboxStapler'
'basicOfficeFinisher' 'officeFinisher' 'advancedOfficeFinisher'
'standardFinisher' 'professionalFinisher' 'dClassFinisher' 'dBookletMaker'
'dBookletMakerFold' 'd3ClassFinisher' 'd3ClassFinisherHcs' 'sbm' 'standardMff'
'professionalMff' 'bfm' 'ftm' 'bfmBfm' 'bfmBfmFtm' 'hcs' 'ehcs' 'hvf' 'hvfBm'
'bTypeFinisher' 'cTypeFinisher' 'cTypeFinisherBookletMaker' 'phProfessional2'
'dfaCompliant' 'hcss' 'dClassFinisherAdvanced' 'dClassFinisherProfessional'
'dClassFinisherProduction' 'cClassFinisherAdvanced'
'cClassFinisherProfessional' 'sbmFolder' 'standardFinisherMain'
'standardFinisherSb' 'dfaCompliantMain' 'dfaCompliantSb' 'dfaCompliantCustom'
'ehcs80' 'ehcss80' 'hcsDfa' 'hcsHcs' 'hcsHcsDfa' 'D3ClassFinisherHcsHcs' 'css'
'professionalPlusMff' 'bfmFtm' 'aTypeFinisher' 'typeSb' 'typeSbBookletMaker'
'professionalMffMohican' 'ftms' 'bfmFtms' 'ftmsFtms' 'bfmFtmsFtms' 'bfmBfmFtms'
'dFold' 'mainTray' An example: dClassFinisherProduction,dBookletMaker
""")
_XcmPrtDrvrHwdOptHardDrive_Type = PresentOnOff
_XcmPrtDrvrHwdOptHardDrive_Object = MibScalar
xcmPrtDrvrHwdOptHardDrive = _XcmPrtDrvrHwdOptHardDrive_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 9),
    _XcmPrtDrvrHwdOptHardDrive_Type()
)
xcmPrtDrvrHwdOptHardDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptHardDrive.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptHardDrive.setDescription("""\
Object that indicates if a Hard Drive is installed within the print device.
""")
_XcmPrtDrvrHwdOptHolePunchUnit_Type = XcmPrtHolePunchUnitType
_XcmPrtDrvrHwdOptHolePunchUnit_Object = MibScalar
xcmPrtDrvrHwdOptHolePunchUnit = _XcmPrtDrvrHwdOptHolePunchUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 10),
    _XcmPrtDrvrHwdOptHolePunchUnit_Type()
)
xcmPrtDrvrHwdOptHolePunchUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptHolePunchUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptHolePunchUnit.setDescription("""\
Object used to indicate the type of Hole Punch Unit that is installed within
the print device.
""")


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
if mibBuilder.loadTexts:
    xcmPrtDriverInputPaperTrays.setDescription("""\
Object used to indicate the type of Paper Trays that are installed within the
print device. The contents of this object shall expose a string of valid Paper
Tray names which are seperated by a comma. Valid paper tray types include:
'notInstalled' 'traysInstalled' '1Tray' '2Trays' '3Trays' '3TraysHighCapacity'
'4Trays' '4TraysHighCapacityTandemTray' '5Trays' '6Trays'
'extraTraysNotInstalled' '1ExtraTray' '2ExtraTrays' '3ExtraTrays' '4ExtraTrays'
'5TraysHighCapacityTandemTray' '6TraysHighCapacity'
'6TraysHighCapacityTandemTray' An example: 6Trays,2ExtraTrays
""")
_XcmPrtDrvrHwdOptInserterUnit_Type = PresentOnOff
_XcmPrtDrvrHwdOptInserterUnit_Object = MibScalar
xcmPrtDrvrHwdOptInserterUnit = _XcmPrtDrvrHwdOptInserterUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 12),
    _XcmPrtDrvrHwdOptInserterUnit_Type()
)
xcmPrtDrvrHwdOptInserterUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptInserterUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptInserterUnit.setDescription("""\
Object that indicates if an Inserter Unit is installed within the print device.
""")
_XcmPrtDrvrHwdOptJobAccountingFdi_Type = PresentOnOff
_XcmPrtDrvrHwdOptJobAccountingFdi_Object = MibScalar
xcmPrtDrvrHwdOptJobAccountingFdi = _XcmPrtDrvrHwdOptJobAccountingFdi_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 13),
    _XcmPrtDrvrHwdOptJobAccountingFdi_Type()
)
xcmPrtDrvrHwdOptJobAccountingFdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptJobAccountingFdi.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptJobAccountingFdi.setDescription("""\
Object that indicates if a Job Accounting FDI Unit is installedthe print
device.
""")
_XcmPrtDrvrHwdOptFaxOut_Type = XcmPrtFaxOutType
_XcmPrtDrvrHwdOptFaxOut_Object = MibScalar
xcmPrtDrvrHwdOptFaxOut = _XcmPrtDrvrHwdOptFaxOut_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 14),
    _XcmPrtDrvrHwdOptFaxOut_Type()
)
xcmPrtDrvrHwdOptFaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptFaxOut.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptFaxOut.setDescription("""\
Object that indicates if a Fax Out Unit is installed within the print device.
""")
_XcmPrtDrvrHwdOptMemoryInMBs_Type = Integer32
_XcmPrtDrvrHwdOptMemoryInMBs_Object = MibScalar
xcmPrtDrvrHwdOptMemoryInMBs = _XcmPrtDrvrHwdOptMemoryInMBs_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 15),
    _XcmPrtDrvrHwdOptMemoryInMBs_Type()
)
xcmPrtDrvrHwdOptMemoryInMBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptMemoryInMBs.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptMemoryInMBs.setDescription("""\
Object that indicates the size of physical memory in units of Megabytes
installed within the print device. A value of zero indicates that no memory is
installed.
""")
_XcmPrtDrvrHwdOptOutputBinSide_Type = PresentOnOff
_XcmPrtDrvrHwdOptOutputBinSide_Object = MibScalar
xcmPrtDrvrHwdOptOutputBinSide = _XcmPrtDrvrHwdOptOutputBinSide_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 16),
    _XcmPrtDrvrHwdOptOutputBinSide_Type()
)
xcmPrtDrvrHwdOptOutputBinSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptOutputBinSide.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptOutputBinSide.setDescription("""\
Object that indicates if a Side Output Bin is installed within the print
device.
""")
_XcmPrtDrvrHwdOptOutputBinCenter_Type = PresentOnOff
_XcmPrtDrvrHwdOptOutputBinCenter_Object = MibScalar
xcmPrtDrvrHwdOptOutputBinCenter = _XcmPrtDrvrHwdOptOutputBinCenter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 17),
    _XcmPrtDrvrHwdOptOutputBinCenter_Type()
)
xcmPrtDrvrHwdOptOutputBinCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptOutputBinCenter.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptOutputBinCenter.setDescription("""\
Object that indicates if a Center Output Bin is installed within the print
device.
""")
_XcmPrtDrvrHwdOptPhaserModule_Type = XcmPrtPhaserModuleType
_XcmPrtDrvrHwdOptPhaserModule_Object = MibScalar
xcmPrtDrvrHwdOptPhaserModule = _XcmPrtDrvrHwdOptPhaserModule_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 18),
    _XcmPrtDrvrHwdOptPhaserModule_Type()
)
xcmPrtDrvrHwdOptPhaserModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptPhaserModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptPhaserModule.setDescription("""\
Object that indentifies the configuration of the Phaser print device.
""")
_XcmPrtDrvrHwdOptPrintEngine_Type = XcmPrtPrintEngineType
_XcmPrtDrvrHwdOptPrintEngine_Object = MibScalar
xcmPrtDrvrHwdOptPrintEngine = _XcmPrtDrvrHwdOptPrintEngine_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 19),
    _XcmPrtDrvrHwdOptPrintEngine_Type()
)
xcmPrtDrvrHwdOptPrintEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptPrintEngine.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptPrintEngine.setDescription("""\
Object that indicates if the print device contains a single print engine or has
two print engines.
""")
_XcmPrtDrvrHwdOptSquareFoldTrimmer_Type = PresentOnOff
_XcmPrtDrvrHwdOptSquareFoldTrimmer_Object = MibScalar
xcmPrtDrvrHwdOptSquareFoldTrimmer = _XcmPrtDrvrHwdOptSquareFoldTrimmer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 20),
    _XcmPrtDrvrHwdOptSquareFoldTrimmer_Type()
)
xcmPrtDrvrHwdOptSquareFoldTrimmer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptSquareFoldTrimmer.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptSquareFoldTrimmer.setDescription("""\
Object that indicates if a Square Fold Trimmer Unit is installed within the
print device.
""")
_XcmPrtDrvrHwdOptTriFold_Type = PresentOnOff
_XcmPrtDrvrHwdOptTriFold_Object = MibScalar
xcmPrtDrvrHwdOptTriFold = _XcmPrtDrvrHwdOptTriFold_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 21),
    _XcmPrtDrvrHwdOptTriFold_Type()
)
xcmPrtDrvrHwdOptTriFold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptTriFold.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrHwdOptTriFold.setDescription("""\
Object that indicates if a Tri-Fold Unit is installed within the print device.
""")
_XcmPrtDrvrFntCollation_Type = PresentOnOff
_XcmPrtDrvrFntCollation_Object = MibScalar
xcmPrtDrvrFntCollation = _XcmPrtDrvrFntCollation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 50),
    _XcmPrtDrvrFntCollation_Type()
)
xcmPrtDrvrFntCollation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntCollation.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntCollation.setDescription("""\
Object that indicates if the Collation function is supported by the print
device.
""")
_XcmPrtDrvrFntAsciiJobTicket_Type = XcmPrtAsciiJobTicketType
_XcmPrtDrvrFntAsciiJobTicket_Object = MibScalar
xcmPrtDrvrFntAsciiJobTicket = _XcmPrtDrvrFntAsciiJobTicket_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 51),
    _XcmPrtDrvrFntAsciiJobTicket_Type()
)
xcmPrtDrvrFntAsciiJobTicket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntAsciiJobTicket.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntAsciiJobTicket.setDescription("""\
Object that indicates if an ACSII Job Ticket function is supported by the print
device.
""")
_XcmPrtDrvrFntAuthenticationMode_Type = XcmPrtAuthenticationModeType
_XcmPrtDrvrFntAuthenticationMode_Object = MibScalar
xcmPrtDrvrFntAuthenticationMode = _XcmPrtDrvrFntAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 52),
    _XcmPrtDrvrFntAuthenticationMode_Type()
)
xcmPrtDrvrFntAuthenticationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntAuthenticationMode.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntAuthenticationMode.setDescription("""\
Object that indicates the type of Authentication Mode function that is
supported by the print device.
""")
_XcmPrtDrvrFntHoldForAuthenMode_Type = XcmPrtHoldForAuthenModeType
_XcmPrtDrvrFntHoldForAuthenMode_Object = MibScalar
xcmPrtDrvrFntHoldForAuthenMode = _XcmPrtDrvrFntHoldForAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 53),
    _XcmPrtDrvrFntHoldForAuthenMode_Type()
)
xcmPrtDrvrFntHoldForAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntHoldForAuthenMode.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntHoldForAuthenMode.setDescription("""\
Object that indicates the type of Hold for Authentication Mode function that is
supported by the print device.
""")
_XcmPrtDrvrFntEnhancedImageQualityMode_Type = PresentOnOff
_XcmPrtDrvrFntEnhancedImageQualityMode_Object = MibScalar
xcmPrtDrvrFntEnhancedImageQualityMode = _XcmPrtDrvrFntEnhancedImageQualityMode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 54),
    _XcmPrtDrvrFntEnhancedImageQualityMode_Type()
)
xcmPrtDrvrFntEnhancedImageQualityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntEnhancedImageQualityMode.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntEnhancedImageQualityMode.setDescription("""\
Object that indicates if the Enhanced Image Quality function is supported by
the print device.
""")
_XcmPrtDrvrFntProductivityPack_Type = PresentOnOff
_XcmPrtDrvrFntProductivityPack_Object = MibScalar
xcmPrtDrvrFntProductivityPack = _XcmPrtDrvrFntProductivityPack_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 55),
    _XcmPrtDrvrFntProductivityPack_Type()
)
xcmPrtDrvrFntProductivityPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntProductivityPack.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntProductivityPack.setDescription("""\
Object that indicates if the Productivity Pack function is supported by the
print device.
""")
_XcmPrtDrvrFntJobStorage_Type = PresentOnOff
_XcmPrtDrvrFntJobStorage_Object = MibScalar
xcmPrtDrvrFntJobStorage = _XcmPrtDrvrFntJobStorage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 56),
    _XcmPrtDrvrFntJobStorage_Type()
)
xcmPrtDrvrFntJobStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntJobStorage.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntJobStorage.setDescription("""\
Object that indicates if the Job Storage software function is supported by the
print device.
""")
_XcmPrtDrvrFntJobAccountingSystem_Type = XcmPrtAccountingSystemType
_XcmPrtDrvrFntJobAccountingSystem_Object = MibScalar
xcmPrtDrvrFntJobAccountingSystem = _XcmPrtDrvrFntJobAccountingSystem_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 6, 57),
    _XcmPrtDrvrFntJobAccountingSystem_Type()
)
xcmPrtDrvrFntJobAccountingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntJobAccountingSystem.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtDrvrFntJobAccountingSystem.setDescription("""\
Object that indicates the type of Job Accounting System that is supported by
the print device.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInputTable.setDescription("""\
 This table logically augments the Printer MIB's prtInputTable.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInputEntry.setDescription("""\
 Entries may exist for each entry in the prtInputTable.
""")
_XcmPrtInputRowStatus_Type = RowStatus
_XcmPrtInputRowStatus_Object = MibTableColumn
xcmPrtInputRowStatus = _XcmPrtInputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 1),
    _XcmPrtInputRowStatus_Type()
)
xcmPrtInputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputRowStatus.setDescription("""\
 Manages the status of this conceptual row in the xcmPrtInputTable.
""")
_XcmPrtInputNextPrtInputIndex_Type = Integer32
_XcmPrtInputNextPrtInputIndex_Object = MibTableColumn
xcmPrtInputNextPrtInputIndex = _XcmPrtInputNextPrtInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 2),
    _XcmPrtInputNextPrtInputIndex_Type()
)
xcmPrtInputNextPrtInputIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputNextPrtInputIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputNextPrtInputIndex.setReference("""\
 See: xcmPrtInputAliasGroup See: xcmPrtInterpTraySwitch
""")
if mibBuilder.loadTexts:
    xcmPrtInputNextPrtInputIndex.setDescription("""\
 The value of prtInputIndex corresponding to the input subunit which will be
used when this input subunit is emptied. The value of zero indicates that auto
input switching will not occur when this input subunit is emptied. Two
different mechanisms for input tray switching, xcmPrtNextPrtInputIndex and
xcmPrtInputAliasGroup, are provided. A device agent may make use of one or the
other, none, or both. Use the model that fits best for the given application.
Usage: Conforming management agents, which ALSO implement the the Printer MIB
v2, SHALL set 'xcmPrtInputNextPrtInputIndex' to the SAME value as
'prtInputNextIndex' (i.e., the values of these two objects SHALL be
interlocked).
""")


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
if mibBuilder.loadTexts:
    xcmPrtInputUseCustomSize.setReference("""\
 See: xcmPrtInputCustDimFeedDirDecl See: xcmPrtInputCustDimXFeedDirDecl
""")
if mibBuilder.loadTexts:
    xcmPrtInputUseCustomSize.setDescription("""\
 Specifies how this input subunit determines the paper size to use. If the
value is 'Off' this input subunit uses the paper size automatically sensed by
the subunit. If the value is 'On' this input subunit uses the custom dimensions
provided by xcmPrtInputCustDimFeedDirDecl and xcmPrtInputCustDimXFeedDirDecl.
""")
_XcmPrtInputCustDimFeedDirDecl_Type = Integer32
_XcmPrtInputCustDimFeedDirDecl_Object = MibTableColumn
xcmPrtInputCustDimFeedDirDecl = _XcmPrtInputCustDimFeedDirDecl_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 4),
    _XcmPrtInputCustDimFeedDirDecl_Type()
)
xcmPrtInputCustDimFeedDirDecl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputCustDimFeedDirDecl.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputCustDimFeedDirDecl.setReference("""\
 See: xcmPrtInputUseCustomSize See: xcmPrtInputCustDimXFeedDirDecl
""")
if mibBuilder.loadTexts:
    xcmPrtInputCustDimFeedDirDecl.setDescription("""\
 Provides the dimension, in the feed direction, of the media in this input
subunit, when the value of xcmPrtInputUseCustomSize is set to 'On'. When
xcmPrtInputUseCustomSize is set to On, this value is copied to
prtInputMediaDimFeedDirDeclared and prtInputMediaDimFeedDirChosen.
""")
_XcmPrtInputCustDimXFeedDirDecl_Type = Integer32
_XcmPrtInputCustDimXFeedDirDecl_Object = MibTableColumn
xcmPrtInputCustDimXFeedDirDecl = _XcmPrtInputCustDimXFeedDirDecl_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 5),
    _XcmPrtInputCustDimXFeedDirDecl_Type()
)
xcmPrtInputCustDimXFeedDirDecl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputCustDimXFeedDirDecl.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputCustDimXFeedDirDecl.setReference("""\
 See: xcmPrtInputUseCustomSize See: xcmPrtInputCustDimFeedDirDecl
""")
if mibBuilder.loadTexts:
    xcmPrtInputCustDimXFeedDirDecl.setDescription("""\
 Provides the dimension, in the feed direction, of the media in this input
subunit, when the value of xcmPrtInputUseCustomSize is set to 'On'. When
xcmPrtInputUseCustomSize is set to 'On', this value is copied to
prtInputMediaDimFeedDirDeclared and prtInputMediaDimFeedDirChosen.
""")
_XcmPrtInputTrayPriority_Type = Integer32
_XcmPrtInputTrayPriority_Object = MibTableColumn
xcmPrtInputTrayPriority = _XcmPrtInputTrayPriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 1, 1, 6),
    _XcmPrtInputTrayPriority_Type()
)
xcmPrtInputTrayPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputTrayPriority.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputTrayPriority.setReference("""\
 See: xcmPrtNextPrtInputIndex See: xcmPrtInputAliasGroup
""")
if mibBuilder.loadTexts:
    xcmPrtInputTrayPriority.setDescription("""\
 The current priority of this tray. This value/mechanism is independent of
xcmPrtNextPrtInputIndex and xcmPrtInputAliasGroup. Usage: The priority of this
device, where '0' is unspecified (default), '1' is lowest, and '100' is
highest.
""")
_XcmPrtInputTrayTable_Object = MibTable
xcmPrtInputTrayTable = _XcmPrtInputTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 2)
)
if mibBuilder.loadTexts:
    xcmPrtInputTrayTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputTrayTable.setDescription("""\
 This table logically augments the Printer MIB's Input Group.
""")
_XcmPrtInputTrayEntry_Object = MibTableRow
xcmPrtInputTrayEntry = _XcmPrtInputTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 2, 1)
)
xcmPrtInputTrayEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmPrtInputTrayEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputTrayEntry.setDescription("""\
 Entries may exist for each unique hrDeviceIndex entry in the prtInputTable.
""")
_XcmPrtInputTraysRowStatus_Type = RowStatus
_XcmPrtInputTraysRowStatus_Object = MibTableColumn
xcmPrtInputTraysRowStatus = _XcmPrtInputTraysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 8, 2, 1, 1),
    _XcmPrtInputTraysRowStatus_Type()
)
xcmPrtInputTraysRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputTraysRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputTraysRowStatus.setDescription("""\
 Manages the status of this conceptual row in the xcmPrtInputTrayTable.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInputTraysInstalled.setDescription("""\
 The number of printer input trays installed on this device. This is read-only
on devices that are able to determine this value at The value is read-write on
devices that do not know how many inpu trays are installed on the device. The
value reported must match the number of rows in prtInputTable for each unique
hrDeviceIndex in that table. Input trays for finisher units are not reported by
this value.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInputTraysConfiguration.setDescription("""\
 This single object represents the input tray configuration for the entire
machine. The value exposed by this object will be utilized by Xerox print
driver software and the Microsoft OS.
""")
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
if mibBuilder.loadTexts:
    xcmPrtOutputTable.setDescription("""\
 This table logically augments the prtOutputTable in the Printer MIB.
""")
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
if mibBuilder.loadTexts:
    xcmPrtOutputEntry.setDescription("""\
 Entries may exist for each entry in the prtOutputTable.
""")
_XcmPrtOutputRowStatus_Type = RowStatus
_XcmPrtOutputRowStatus_Object = MibTableColumn
xcmPrtOutputRowStatus = _XcmPrtOutputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 1),
    _XcmPrtOutputRowStatus_Type()
)
xcmPrtOutputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtOutputRowStatus.setDescription("""\
 Manages the status of this conceptual row in the xcmPrtOutputTable.
""")
_XcmPrtOutputNextIndex_Type = Integer32
_XcmPrtOutputNextIndex_Object = MibTableColumn
xcmPrtOutputNextIndex = _XcmPrtOutputNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 2),
    _XcmPrtOutputNextIndex_Type()
)
xcmPrtOutputNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputNextIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtOutputNextIndex.setDescription("""\
 The value of prtOutputIndex corresponding to the output subunit which will be
used when this output subunit is filled. A value of zero(0) indicates that auto
output switching will not occur when this output subunit is filled.
""")


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
if mibBuilder.loadTexts:
    xcmPrtOutputPassword.setReference("""\
See: prtOutputSecurity.
""")
if mibBuilder.loadTexts:
    xcmPrtOutputPassword.setDescription("""\
 This object is used as the password for an Output Tray, e.g. an output
mailbox. It is the value that must be entered to open the output tray.
""")


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
if mibBuilder.loadTexts:
    xcmPrtOutputOffsetStackingType.setReference("""\
 See: prtOutputOffsetStacking See: xcmPrtInterpOffsetStackingType
""")
if mibBuilder.loadTexts:
    xcmPrtOutputOffsetStackingType.setDescription("""\
 This object further refines the type of offset stacking from that specified by
the object prtOutputOffsetStacking in the Printer MIB.
""")


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
if mibBuilder.loadTexts:
    xcmPrtOutputTrayTimeoutSupport.setReference("""\
See: xcmPrtOutputTrayTimeout
""")
if mibBuilder.loadTexts:
    xcmPrtOutputTrayTimeoutSupport.setDescription("""\
 Determines whether the printer should wait before sending the printed output
to another output destination when the selected or default destination is full.
'On' indicates that would should wait as specified by xcmPrtOutputTrayTimeout.
'Off' indicates this feature is off and should immediately seek to send the
printed output to another destination. The value 'other' shall mean not
specified.
""")
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
if mibBuilder.loadTexts:
    xcmPrtOutputTrayTimeout.setDescription("""\
 Determines how long the printer should wait before sending the printed output
to another output destination when the selected or default destination is full.
A value of (0) implies 'other' or 'infinite' which translates to this input
subunit does not support this feature.
""")


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
if mibBuilder.loadTexts:
    xcmPrtOutputStaple.setReference("""\
 See: 'xcmPrtOutputStapleDefault See: 'xcmPrtOutputStaplePosSupported' See:
'xcmPrtOutputStaplePosDefault'
""")
if mibBuilder.loadTexts:
    xcmPrtOutputStaple.setDescription("""\
 This object declares whether the printer has the ability to staple multi-page
documents delivered to the specified output destination, and whether this
ability is currently turned on. 'on' indicates stapling is supported to this
output destination, and that it is turned on. 'off' indicates this printer
supports stapling to this output destination, but that it is turned off. If a
job calls for a staple, none will be given. 'notPresent' indicates that this
printer does not support stapling to this output destination. The value 'other'
shall mean not specified.
""")
_XcmPrtOutputStaplePosSupported_Type = XcmPrtOutputStaplePosition
_XcmPrtOutputStaplePosSupported_Object = MibTableColumn
xcmPrtOutputStaplePosSupported = _XcmPrtOutputStaplePosSupported_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 101),
    _XcmPrtOutputStaplePosSupported_Type()
)
xcmPrtOutputStaplePosSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputStaplePosSupported.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtOutputStaplePosSupported.setReference("""\
 See: 'xcmPrtOutputStaple' See: 'xcmPrtOutputStapleDefault' See:
'xcmPrtOutputStaplePosDefault'
""")
if mibBuilder.loadTexts:
    xcmPrtOutputStaplePosSupported.setDescription("""\
 This object declares the stapling positions supported.
""")


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
if mibBuilder.loadTexts:
    xcmPrtOutputStapleDefault.setReference("""\
 See: 'xcmPrtOutputStaple See: 'xcmPrtOutputStaplePosSupported' See:
'xcmPrtOutputStaplePosDefault'
""")
if mibBuilder.loadTexts:
    xcmPrtOutputStapleDefault.setDescription("""\
 This object declares for the cases where the job-stream does not specify
whether to staple a particular job, whether the printer should apply the
default staple specified in xcmPrtOutputStaplePosDefault for this output
destination. 'on' indicates the staple default feature is supported for this
output destination, and that a job not specifying whether to staple should be
supplied a staple per the 'xcmPrtOutputStaplePosDefault' object. If stapling is
disabled, the document will not be stapled. 'off' indicates the staple default
feature is supported for this output destination, but that it is turned off.
Jobs not specifying whether to staple, will not be stapled. 'notPresent'
indicates the staple default feature is not supported. Jobs not specifying
whether to staple, will not be stapled. The value 'other' shall mean not
specified.
""")
_XcmPrtOutputStaplePosDefault_Type = XcmPrtOutputStaplePosition
_XcmPrtOutputStaplePosDefault_Object = MibTableColumn
xcmPrtOutputStaplePosDefault = _XcmPrtOutputStaplePosDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 103),
    _XcmPrtOutputStaplePosDefault_Type()
)
xcmPrtOutputStaplePosDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputStaplePosDefault.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtOutputStaplePosDefault.setReference("""\
 See: 'xcmPrtOutputStaple' See: 'xcmPrtOutputStapleDefault' See:
'xcmPrtOutputStaplePosSupported'
""")
if mibBuilder.loadTexts:
    xcmPrtOutputStaplePosDefault.setDescription("""\
 This object controls the default staple position to be used when stapling is
enabled, and the job-stream does not specify whether to staple the particular
job or the job-stream specifies to apply a staple, but does not specify where.
Only one staple position may be declared. The value of zero indicates a default
of not staple.
""")


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
if mibBuilder.loadTexts:
    xcmPrtOutputPunch.setDescription("""\
 This object declares whether the printer has the ability to punch holes in
documents delivered to the specified output destination, and whether this
ability is currently turned on. 'on' indicates hole punching is supported to
this output destination and that it is turned on 'off' indicates this printer
supports hole punching to this output destination, but that it is turned off.
If a job calls for punched output, no punching will occur. 'not Present'
indicates that this printer does not support hole punching.
""")


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
if mibBuilder.loadTexts:
    xcmPrtOutputPunchDefault.setDescription("""\
 This object declares whether the printer will punch the job when the print
stream does not specify a punch requirement. 'on' indicates hole punching is
supported to this output destination and that the job will be punched if the
data stream contains no job punch information 'off' indicates this printer
supports hole punching to this output destination, and that the job will not be
punched if the data stream contains no job punch information 'not Present'
indicates that this printer does not support hole punching.
""")
_XcmPrtOutputPunchPosSupported_Type = XcmPrtOutputPunchPosition
_XcmPrtOutputPunchPosSupported_Object = MibTableColumn
xcmPrtOutputPunchPosSupported = _XcmPrtOutputPunchPosSupported_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 9, 1, 1, 106),
    _XcmPrtOutputPunchPosSupported_Type()
)
xcmPrtOutputPunchPosSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtOutputPunchPosSupported.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtOutputPunchPosSupported.setReference("""\
 See: 'xcmPrtOutputPunch'
""")
if mibBuilder.loadTexts:
    xcmPrtOutputPunchPosSupported.setDescription("""\
 This object declares the punch positions supported.
""")


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
if mibBuilder.loadTexts:
    xcmPrtOutputBookletFoldStaple.setDescription("""\
 This object declares whether the device has the ability to fold and or staple
booklet documents delivered to the specifie output destination, and whether
this ability is currently turn on indicates booklet folding and/or stapling is
supported to output destination and that it is turned on. off indicates booklet
folding and/or stapling is supported to but that it is turned off. If a job
calls for a booklet folding and/or staple, none will be given. notPresent
indicates booklet folding and/or stapling is not supported. The value other
shall mean not specified.
""")
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
if mibBuilder.loadTexts:
    xcmPrtChannelTable.setDescription("""\
 This table logically augments Printer MIB's prtChannelTable.
""")
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
if mibBuilder.loadTexts:
    xcmPrtChannelEntry.setDescription("""\
 An entry exists corresponding to each entry in the prtChannelTable.
""")
_XcmPrtChannelRowStatus_Type = RowStatus
_XcmPrtChannelRowStatus_Object = MibTableColumn
xcmPrtChannelRowStatus = _XcmPrtChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 1),
    _XcmPrtChannelRowStatus_Type()
)
xcmPrtChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtChannelRowStatus.setDescription("""\
 Manages the status of this conceptual row in the xcmPrtChannelTable.
""")
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
if mibBuilder.loadTexts:
    xcmPrtChannelEOJTimeout.setDescription("""\
 Defines the number of seconds that the channel waits before timing out. For
example, this may be used for the parallel channel. The value zero means
infinite or no timeout on the channel.
""")
_XcmPrtChannelAuxSheetPackage_Type = Cardinal32
_XcmPrtChannelAuxSheetPackage_Object = MibTableColumn
xcmPrtChannelAuxSheetPackage = _XcmPrtChannelAuxSheetPackage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 14, 1, 1, 3),
    _XcmPrtChannelAuxSheetPackage_Type()
)
xcmPrtChannelAuxSheetPackage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtChannelAuxSheetPackage.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtChannelAuxSheetPackage.setReference("""\
 See: xcmPrtGeneralAuxSheetPackage See: xcmPrtInterpAuxSheetPackage
""")
if mibBuilder.loadTexts:
    xcmPrtChannelAuxSheetPackage.setDescription("""\
 This object is an index into the xcmPrtAuxPackageTable. This table is used to
enable or disable printing of auxiliary sheets by this channel. The value zero
shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtChannelSpoolingEnable.setReference("""\
 DocuPrint 4517 Network Laser Printers User Guide, pg. D-5.
""")
if mibBuilder.loadTexts:
    xcmPrtChannelSpoolingEnable.setDescription("""\
 This object controls spooling to a large data store such as a hard disk. When
set to On, data received and waiting to be processed from any port is spooled
onto the large data store and later retrieved for processing. This allows the
printer to receive the data more rapidly, thus freeing the data source sooner.
It may also increase throughput by having the next job's print data already
local for processing. When set to Off, the spooling feature is disabled. Data
received is not spooled to the large data store, and is accepted by the printer
only as needed for printing. You may want to disable this spooling feature if
spooling is already done outside the printer; having the spooling done on the
printer as well, may not add value, and may create error recovery and queue
monitoring difficulties. The value 'other' shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtChannelLangSensing.setReference("""\
 See: Printer MIB prtInterpreterLangFamily
""")
if mibBuilder.loadTexts:
    xcmPrtChannelLangSensing.setDescription("""\
 This object indicates whether the channel supports detection of the input PDL
language type, and if so, whether the feature is enabled. Currently, the
prtChannelDefaultPageDescLangIndex points to the Page Description Language
Interpreter for this channel. One of the PDL types enumerated in the
prtInterpreterLangFamily object is langAutomatic(37), to be used for automatic
PDL sensing; however, if the language sensing fails there is no fallback
language for the channel. Conforming implementations shall use
xcmPrtChannelLangSensing for each channel and deprecate use of the
langAutomatic(37) enum in favor of the literal default language in the
prtInterpreterLangFamily object. The value 'other' shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtChannelBinaryPostScript.setReference("""\
 See: Printer MIB prtInterpreterLangFamily See: xcmPrtChannelBinaryPostScriptZ
""")
if mibBuilder.loadTexts:
    xcmPrtChannelBinaryPostScript.setDescription("""\
 If 'On' PostScript received over this channel is processed as pure binary
data. If 'Off' PostScript is interpretted as ASCII or TBCP data. The value
'other' shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtChannelAutoJobEnd.setReference("""\
 See: xcmPrtChannelEOJTimeout See: Xerox 4517+ User Guide See: Xerox 4505 User
Guide
""")
if mibBuilder.loadTexts:
    xcmPrtChannelAutoJobEnd.setDescription("""\
 Controls automatic ending of a print job that does not finish printing. When
'On', after the current print job has paused long enough to exceed the
xcmPrtChannelEOJTimeout interval, the current print job will be stopped. When
'Off', the print job does not end after the timeout interval. Instead, the
printer waits to continue until another print job is received on any port. A
partial page will remain unprinted until the next print job is received. The
current job will then be stopped. The value 'other' shall indicate not
specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtChannelBinaryPostScriptZ.setReference("""\
 See: xcmPrtChannelBinaryPostScript See: Printer MIB prtInterpreterLangFamily
""")
if mibBuilder.loadTexts:
    xcmPrtChannelBinaryPostScriptZ.setDescription("""\
 If 'On' PostScript received over this channel is processed as pure binary
data. If 'Off' PostScript is interpretted as ASCII or TBCP data. The value
'other' shall mean not specified. Devices should NOT implement this object,
should instead implement the equivalent object xcmPrtChannelBinaryPostScript.
This xcmPrtChannelBinaryPostScriptZ object appears for backward compatibility
support only, since some few devices implemented the object at this OID.
Clients/managers wishing to support those devices should try to access both
objects (which generally can be done with a single SNMP message packet
combining requests for both object OIDs) and use whichever object is present in
the device.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInterpreterTable.setDescription("""\
 This table logically augments the Printer MIB's prtInterpreterTable.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInterpreterEntry.setDescription("""\
 An entry exists corresponding to each entry in the prtInterpreterTable.
""")
_XcmPrtInterpRowStatus_Type = RowStatus
_XcmPrtInterpRowStatus_Object = MibTableColumn
xcmPrtInterpRowStatus = _XcmPrtInterpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 1),
    _XcmPrtInterpRowStatus_Type()
)
xcmPrtInterpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpRowStatus.setDescription("""\
 Manages the status of this conceptual row in the xcmPrtInterpreterTable.
""")
_XcmPrtInterpAuxSheetPackage_Type = Cardinal32
_XcmPrtInterpAuxSheetPackage_Object = MibTableColumn
xcmPrtInterpAuxSheetPackage = _XcmPrtInterpAuxSheetPackage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 2),
    _XcmPrtInterpAuxSheetPackage_Type()
)
xcmPrtInterpAuxSheetPackage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpAuxSheetPackage.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpAuxSheetPackage.setReference("""\
 See: xcmPrtGeneralAuxSheetPackage See: xcmPrtChannelAuxSheetPackage
""")
if mibBuilder.loadTexts:
    xcmPrtInterpAuxSheetPackage.setDescription("""\
 This object is an index into the xcmPrtAuxPackageTable. This table is used to
enable or disable printing of auxiliary sheets by this interpreter. The value
zero shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpContextSaving.setReference("""\
 DocuPrint 4517 Network Laser Printers User Guide, Pg. D-16.
""")
if mibBuilder.loadTexts:
    xcmPrtInterpContextSaving.setDescription("""\
 Enables reserving memory for saving permanently downloaded fonts and macros,
when the printer switches between this and another interpreter. The effect is
to save the memory for a subsequent job using this interpreter. When set to
Off, all permanently downloaded fonts and macros are cleared from memory when
switching PDLs. They must be downloaded again when the printer switches back to
using the current PDL. When set to On, permanently downloaded fonts and macros
are stored in printer memory. You eliminate the time to download them again
when the printer switches back to the current PDL. In PCL, this is referred to
as Resource Savings. The value 'other' shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpEdgeEnhancement.setDescription("""\
 Specifies whether the printer should perform EdgeEnhancement of the image of
the printed document for this interpreter. The value 'other' shall mean not
specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpFontIndexDefault.setDescription("""\
 The value of xcmFontIndex corresponding to the xcmFontEntry which represents
the default font for this Interpreter. A value of (-1) means 'other'. A value
of (-2) means 'unknown'. A value of (-3) means 'notPresent'. A value of 'other'
(-3) should be used for those interpreters which have no default font (e.g.
PostScript). For agents that choose not to implement the Resources MIB, this
object specifies the ID of the default font. This use of this object is
significant only to the specific product.
""")
_XcmPrtInterpGrayLevels_Type = Cardinal32
_XcmPrtInterpGrayLevels_Object = MibTableColumn
xcmPrtInterpGrayLevels = _XcmPrtInterpGrayLevels_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 6),
    _XcmPrtInterpGrayLevels_Type()
)
xcmPrtInterpGrayLevels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpGrayLevels.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpGrayLevels.setDescription("""\
 This object describes the gray levels supported by this interpreter. This may
represent gray levels within a color plane. The value zero means not specified
for this interpreter.
""")
_XcmPrtInterpGrayLevelDefault_Type = Cardinal32
_XcmPrtInterpGrayLevelDefault_Object = MibTableColumn
xcmPrtInterpGrayLevelDefault = _XcmPrtInterpGrayLevelDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 7),
    _XcmPrtInterpGrayLevelDefault_Type()
)
xcmPrtInterpGrayLevelDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpGrayLevelDefault.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpGrayLevelDefault.setReference("""\
See: xcmPrtInterpGrayLevels
""")
if mibBuilder.loadTexts:
    xcmPrtInterpGrayLevelDefault.setDescription("""\
 This object controls the number of gray scales for this interpreter. The value
zero means not specified for this interpreter.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpJamRecovery.setReference("""\
 DocuPrint 4517 Network Laser Printers User Guide, Pg. D-9.
""")
if mibBuilder.loadTexts:
    xcmPrtInterpJamRecovery.setDescription("""\
 This object controls how the printer recovers from a paper jam. When set to
On, the printer reprints any pages in the printer at the time of the jam, after
the jam has been cleared. The printer does this by using a portion of memory to
store print data. This may slow throughput. When set to Off, some pages may be
lost after the jam has been cleared. The print job must be re-sent, specifying
those pages that did not print as a result of the paper jam. The value 'other'
shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpJobCopiesDefault.setReference("""\
 See: ISO/IEC 10175-1:1996(E) - Section 9.2.2.1: Results-profile job-copies
See: PJL Technical Reference Manual - COPIES See: PCL 5 Printer Language
Technical Reference Manual - Number of Copies Command
""")
if mibBuilder.loadTexts:
    xcmPrtInterpJobCopiesDefault.setDescription("""\
 This defines the default number of job copies to be printed by this
interpreter. If set incorrectly, this object may cause difficulties at customer
sites. Agent developers should consider making this object read-only,
permanently set to one copy.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpLineWrap.setReference("""\
 Adobe PostScript Language Reference Manual Supplement.
""")
if mibBuilder.loadTexts:
    xcmPrtInterpLineWrap.setDescription("""\
 This object controls whether long lines are wrapped or truncated. If On, long
lines wrap to the next line. If Off, long lines are truncated. Note the meaning
of 'long' depends on the orientation and the current page size. The value
'other' shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpMediumSizeDefault.setReference("""\
 See: PCL 5 Printer Language Technical Reference Manual See: PJL Technical
Reference Manual - PAPER See: xcmPrtGeneralMediumClassDefault
""")
if mibBuilder.loadTexts:
    xcmPrtInterpMediumSizeDefault.setDescription("""\
 This object specifies the default medium size for an interpreter. It is used
if no medium size is specified. For PCL, this object sets the General PJL
Environment variable 'Paper'. The xcmPrtInterpMediumSizeDefault object may be
affected by setting the xcmPrtGeneralMediumClassDefault object.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpPageProtect.setReference("""\
 DocuPrint 4517 Network Laser Printers User Guide, Pg. D-11.
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPageProtect.setDescription("""\
 This object enables reserving sufficient memory for printing complex pages,
thus avoiding Page Too Complex errors. The amount of memory reserved is
implementation specific. When this feature is turned on, printer performance
may be slowed. The value 'other' shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpPageProtectSize.setReference("""\
 See: Printer Job Language Technical Reference Manual - General PJL Environment
Variable 'PAGEPROTECT'
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPageProtectSize.setDescription("""\
 This object sets the PageSize to be used by this interpreter in reserving
sufficient memory for printing complex pages, thus avoiding Page Too Complex
Errors. The actual amount of memory to be reserved as a function of the
specified page size is implementation specific. When this feature is turned on,
printer performance may be slowed. In PCL, this object supports the General PJL
Environment Variable 'PAGEPROTECT'. This object the sets the page protection
configuration. The page protection feature reserves a block of printer memory
to prevent printer overrun errors when formatting very dense or complex images.
This variable may be set to any legal value at any time, regardless of the
current amount of free memory or the currently set resolution. When a job is
sent, if there is not enough memory to print correctly with the current
resolution and page protection configuration, the system temporarily overrides
the resolution and/or page protect values to run the job. When the page
protection status is changed, memory may be reconfigured, and all downloaded
fonts, PCL macros, and PostScript dictionaries may be lost. The value
notSpecified shall also mean Off.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpPageSizeErrorPolicy.setReference("""\
 See: xcmPrtInterpMediaTypeErrPolicy See: xcmPrtInterpErrorPolicyTimeout
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPageSizeErrorPolicy.setDescription("""\
 Controls interpreter behavior when the requested Page Size is not currently
available.
""")
_XcmPrtInterpPlexSupported_Type = XcmPrtPlex
_XcmPrtInterpPlexSupported_Object = MibTableColumn
xcmPrtInterpPlexSupported = _XcmPrtInterpPlexSupported_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 15),
    _XcmPrtInterpPlexSupported_Type()
)
xcmPrtInterpPlexSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPlexSupported.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpPlexSupported.setDescription("""\
 This object specifies the Plex modes supported by this interpreter. These Plex
modes specify the relative orientations between consecutive pages, and
capabilities of printing one-side, two-sided or both.
""")
_XcmPrtInterpPlexDefault_Type = XcmPrtPlex
_XcmPrtInterpPlexDefault_Object = MibTableColumn
xcmPrtInterpPlexDefault = _XcmPrtInterpPlexDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 16),
    _XcmPrtInterpPlexDefault_Type()
)
xcmPrtInterpPlexDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPlexDefault.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpPlexDefault.setReference("""\
See: xcmPrtInterpPlexSupported
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPlexDefault.setDescription("""\
 This object specifies the default plex for this interpreter. The device shall
set no more than one bit. The value zero shall indicate not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpPrintEdgeToEdge.setDescription("""\
 Enables edge to edge printing for interpreters that try to enforce a
coordinate system that is offset from the edge of the paper, e.g., PCL. When
On, jobs are printed to the edge of the paper. When Off, jobs are printed in
normal printable area of page. The value 'other' shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpPrintQuality.setDescription("""\
 Sets the default output quality of the printed document for this interpreter.
Some printers have programmatically controlled output quality.
""")
_XcmPrtInterpPrtInputIndexDflt_Type = Cardinal32
_XcmPrtInterpPrtInputIndexDflt_Object = MibTableColumn
xcmPrtInterpPrtInputIndexDflt = _XcmPrtInterpPrtInputIndexDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 19),
    _XcmPrtInterpPrtInputIndexDflt_Type()
)
xcmPrtInterpPrtInputIndexDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPrtInputIndexDflt.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpPrtInputIndexDflt.setDescription("""\
 Sets the default input source for the interpreter. It is the index to the
prtInputGroup. The value zero means not specified.
""")
_XcmPrtInterpPrtOutputIndexDflt_Type = Cardinal32
_XcmPrtInterpPrtOutputIndexDflt_Object = MibTableColumn
xcmPrtInterpPrtOutputIndexDflt = _XcmPrtInterpPrtOutputIndexDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 20),
    _XcmPrtInterpPrtOutputIndexDflt_Type()
)
xcmPrtInterpPrtOutputIndexDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPrtOutputIndexDflt.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpPrtOutputIndexDflt.setReference("""\
See: Printer MIB prtOutputDefaultIndex
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPrtOutputIndexDflt.setDescription("""\
 The value of the index of the default Output bin for this interpreter. If
specified, this object overrides the box level object prtOutputDefaultIndex.
The value zero means unspecified.
""")
_XcmPrtInterpResFeedDirDefault_Type = Cardinal32
_XcmPrtInterpResFeedDirDefault_Object = MibTableColumn
xcmPrtInterpResFeedDirDefault = _XcmPrtInterpResFeedDirDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 21),
    _XcmPrtInterpResFeedDirDefault_Type()
)
xcmPrtInterpResFeedDirDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpResFeedDirDefault.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpResFeedDirDefault.setReference("""\
See: Printer MIB prtInterpreterFeedAddressability
""")
if mibBuilder.loadTexts:
    xcmPrtInterpResFeedDirDefault.setDescription("""\
 This object specifies for this interpreter, the default resolution in the Feed
direction in 10000 units of measure specified by prtMarkerAddressabilityUnit
for this interpreter. A related object is the Printer MIB
prtInterpreterFeedAddressability object which describes the maximum interpreter
addressability in the feed direction. The value zero shall mean not specified.
If this object has a value other than unspecified, this object takes precedence
over xcmPrtInterpFeedResIndexDefault.
""")
_XcmPrtInterpResXFeedDirDefault_Type = Cardinal32
_XcmPrtInterpResXFeedDirDefault_Object = MibTableColumn
xcmPrtInterpResXFeedDirDefault = _XcmPrtInterpResXFeedDirDefault_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 22),
    _XcmPrtInterpResXFeedDirDefault_Type()
)
xcmPrtInterpResXFeedDirDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpResXFeedDirDefault.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpResXFeedDirDefault.setReference("""\
See: Printer MIB prtInterpreterXFeedAddressability
""")
if mibBuilder.loadTexts:
    xcmPrtInterpResXFeedDirDefault.setDescription("""\
 This object specifies for this interpreter, the default resolution in the
Cross Feed direction in 10000 units of measure specified by
prtMarkerAddressabilityUnit for this interpreter. A related object is the
Printer MIB prtInterpreterFeedAddressability object which describes the maximum
interpreter addressability in the cross feed direction. The value zero means
unspecified. If this object has a value other than unspecified, this object
takes precedence over xcmPrtInterpFeedResIndexDefault.
""")
_XcmPrtInterpResIPResIndex_Type = Cardinal32
_XcmPrtInterpResIPResIndex_Object = MibTableColumn
xcmPrtInterpResIPResIndex = _XcmPrtInterpResIPResIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 23),
    _XcmPrtInterpResIPResIndex_Type()
)
xcmPrtInterpResIPResIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpResIPResIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpResIPResIndex.setDescription("""\
 This object shall provide an index into the xcmIPResTable. The xcmIPResTable
shall be used to list available resolutions supported by this interpreter. Each
row includes objects for Feed Resolution (pixels per inch), XFeed Resolution
(pixels per inch), Bits Per Pixel Supported, and Number of Color Planes
Supported. The value zero means unspecified.
""")
_XcmPrtInterpResIPResIndexDflt_Type = Cardinal32
_XcmPrtInterpResIPResIndexDflt_Object = MibTableColumn
xcmPrtInterpResIPResIndexDflt = _XcmPrtInterpResIPResIndexDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 24),
    _XcmPrtInterpResIPResIndexDflt_Type()
)
xcmPrtInterpResIPResIndexDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpResIPResIndexDflt.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpResIPResIndexDflt.setDescription("""\
 This object which is a pointer into the xcmIPResTable sets the print
resolution for this interpreter. The value zero means unspecified.
""")
_XcmPrtInterpTextFormLength_Type = Cardinal32
_XcmPrtInterpTextFormLength_Object = MibTableColumn
xcmPrtInterpTextFormLength = _XcmPrtInterpTextFormLength_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 25),
    _XcmPrtInterpTextFormLength_Type()
)
xcmPrtInterpTextFormLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpTextFormLength.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpTextFormLength.setReference("""\
 See: PJL Technical Reference Manual - FORMLINES
""")
if mibBuilder.loadTexts:
    xcmPrtInterpTextFormLength.setDescription("""\
 This object sets the maximum number of lines per page for a text file that is
being printed using this interpreter. For PCL Interpreters, this object
provides the General PJL Environment Variable FORMLINES. This variable is tied
to both the PJL Environment Variables PAPER and ORIENTATION. If the value of
either of those variables is changed, then the FORMLINES variable automatically
is updated to maintain the same line spacing. The value zero means not
specified.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInterpTimeoutJob.setDescription("""\
 This object sets how long printer will wait for correct end of job from the
interpreter. This setting lets you adjust how long the printer will wait to
receive the data it needs to complete a job before terminating it prematurely.
The value zero means infinite.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInterpTimeoutPage.setDescription("""\
 This object sets how long printer will wait for correct end of page from the
interpreter. If, for example, a print job contains a page without the correct
end of page code, the job will stall. This setting lets you adjust how long the
printer will wait to receive the data it needs to complete a page before
terminating it prematurely. The value zero means infinite.
""")
_XcmPrtInterpInputAliasIndexDflt_Type = Cardinal32
_XcmPrtInterpInputAliasIndexDflt_Object = MibTableColumn
xcmPrtInterpInputAliasIndexDflt = _XcmPrtInterpInputAliasIndexDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 15, 1, 1, 28),
    _XcmPrtInterpInputAliasIndexDflt_Type()
)
xcmPrtInterpInputAliasIndexDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpInputAliasIndexDflt.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpInputAliasIndexDflt.setReference("""\
 See: xcmPrtInputAliasTable
""")
if mibBuilder.loadTexts:
    xcmPrtInterpInputAliasIndexDflt.setDescription("""\
 Sets the default input tray alias for this interpreter. It is the
xcmPrtInputAliasIndex to the xcmPrtInputAlias table. The value zero means 'not
specified'.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpTraySwitch.setReference("""\
 See: xcmPrtInputNextPrtInputIndex See: xcmPrtInputAliasGroup
""")
if mibBuilder.loadTexts:
    xcmPrtInterpTraySwitch.setDescription("""\
 This object declares for this interpreter the tray switching declaration
mechanism used. Note: The tray switching declaration mechanisms do not specify
how or when or whether a printer switches back to using an earlier emptied tray
after that tray is refilled. For example, assume a printer is set up to first
use Tray 1, then when emptied Tray 2, then Tray 3. If just after tray 1 becomes
empty and the printer switches to Tray 2, the operator refills Tray 1; the
printer may select which tray to pull the next sheet from using a variety of
algorithms: - The printer may switch back immediately to use tray 1. This may
be particularly appropriate if tray 1 is the high capacity feeder. - The
printer may pull sheets from tray 2 until it is empty and then switch back to
tray 1. - The printer may pull sheets from tray 2 until it is empty and then
continue to tray 3, before switching back to tray 1. Again, implementation of
how the input tray switching programs behave when empty trays are refilled is
considered printer specific.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpMediumTypeDefault.setDescription("""\
 Specifies the paper type used to print a page if no paper type is specified by
the software application Typical paper types could include Plain, Preprinted,
etc.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpMediaTypeErrPolicy.setReference("""\
 See: xcmPrtInterpPageSizeErrorPolicy See: xcmPrtInterpErrorPolicyTimeout
""")
if mibBuilder.loadTexts:
    xcmPrtInterpMediaTypeErrPolicy.setDescription("""\
 Controls interpreter behavior when the requested Media Type is not currently
available.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInterpErrorPolicyTimeout.setReference("""\
 See: xcmPrtInterpPageSizeErrorPolicy See: xcmPrtInterpMediaTypeErrPolicy
""")
if mibBuilder.loadTexts:
    xcmPrtInterpErrorPolicyTimeout.setDescription("""\
 Provides the timeout for ErrorPolicy enumerations requiring one, e.g.
'ignoreAfterTimeout' The value zero shall mean infinite or not supported.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpLineTerm.setDescription("""\
 Enables adding a Carriage Return after every Line Feed. The value 'On'
indicates that a Carriage Return will be added after every Line Feed. Usage
example: This is a useful feature when printing text jobs via PCL through a
standard queue in UNIX. The value 'other' shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpEnhancedResolution.setDescription("""\
 This value determines whether the value of prtMarkerAddressabilityFeedDir and
prtMarkerAddressabilityXFeedDir is generated directly or generated by enhancing
a lower resolution via interpolation techniques. The value 'other' shall mean
not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpAutoContinue.setReference("""\
 DocuPrint 4517 Network Laser Printers User Guide, Pg. D-3.
""")
if mibBuilder.loadTexts:
    xcmPrtInterpAutoContinue.setDescription("""\
 This object controls whether the printer resumes printing after a system error
occurs. When set to Off, the printer does not automatically resume. Manual
intervention must occur for the printer to resume. When set to On, the printer
automatically resumes operation after certain system errors. The On setting is
useful in a networked environment. The value 'other' shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpEnvFeederSize.setReference("""\
 DocuPrint 4517 Network Laser Printers User Guide, Pg. D-16.
""")
if mibBuilder.loadTexts:
    xcmPrtInterpEnvFeederSize.setDescription("""\
 This object informs the printer what size of envelope is currently loaded in
the envelope feeder. Because the input tray feeding envelopes may not have a
size sensor, this setting is required so that the printer is able to know when
the size of envelope requested for printing is different than that loaded. When
the sizes do not match, and xcmPrtInterpPageSizeErrorPolicy is set to Off, the
printer displays a message asking for a change of envelope size. The
XcmPrtPaperSize selected should be that of an envelope.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpManualFeedPgSize.setReference("""\
 DocuPrint 4517 Network Laser Printers User Guide, Pg. D-10.
""")
if mibBuilder.loadTexts:
    xcmPrtInterpManualFeedPgSize.setDescription("""\
 This object sets the default medium size of the manual input tray for this
interpreter.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpOffsetStackingType.setReference("""\
 See: prtOutputOffsetStacking. See: xcmPrtOutputOffsetStackingType
""")
if mibBuilder.loadTexts:
    xcmPrtInterpOffsetStackingType.setDescription("""\
 This object further refines the type of offset stacking from that specified by
the object prtOutputOffsetStacking in the Printer MIB. Printers who need to
specify OffsetStackingType by interpreter shall set this object to 'other'. To
specify OffsetStackingType by interpreter, use the object
xcmPrtOutputOffsetStackingType.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpProcessBarcodes.setDescription("""\
 Specifies whether the 'extra' barcode processing within the interpreter should
be used.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInputAliasTable.setDescription("""\
 This table defines one or more aliases for input sub-units defined in the
Input Group.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInputAliasEntry.setDescription("""\
 One or more entries may exist corresponding to each entry in the
prtInputTable.
""")
_XcmPrtInputAliasIndex_Type = Cardinal32
_XcmPrtInputAliasIndex_Object = MibTableColumn
xcmPrtInputAliasIndex = _XcmPrtInputAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 50, 1, 1, 1),
    _XcmPrtInputAliasIndex_Type()
)
xcmPrtInputAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmPrtInputAliasIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputAliasIndex.setDescription("""\
 A unique value used to identify this row in the xcmPrtInputAliasTable.
""")
_XcmPrtInputAliasRowStatus_Type = RowStatus
_XcmPrtInputAliasRowStatus_Object = MibTableColumn
xcmPrtInputAliasRowStatus = _XcmPrtInputAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 50, 1, 1, 2),
    _XcmPrtInputAliasRowStatus_Type()
)
xcmPrtInputAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInputAliasRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInputAliasRowStatus.setDescription("""\
 Manages the status of this conceptual row in the xcmPrtInputAliasTable.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInputAliasName.setDescription("""\
 Defines an alternate name for the input source. This is in addition to the
prtInputName from the Input Group. Typical usage is to map an interpreter
specific name to the sub-unit name in the Input Group, e.g., PCL's 'upper' to
the device input name 'main'.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInputAliasSwitchProgram.setDescription("""\
 The input tray switching program for this 'InputAliasName' presented in a '.'
separated list of prtInputIndex values. For example, the string '1.4.3'
indicates start with the input tray represented by prtInputIndex 1, if it
becomes empty switch to prtInputIndex 4, when it becomes empty switch to
prtInputIndex 3, if it becomes empty then wait for operator intervention. An
empty string shall indicate unspecified.
""")
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
if mibBuilder.loadTexts:
    xcmPrtAuxPackageTable.setDescription("""\
 This table lists Auxiliary Sheets enabled for this printer.
""")
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
if mibBuilder.loadTexts:
    xcmPrtAuxPackageEntry.setDescription("""\
 An entry exists corresponding to each entry in the xcmPrtAuxPackageTable.
""")
_XcmPrtAuxPackageIndex_Type = Cardinal32
_XcmPrtAuxPackageIndex_Object = MibTableColumn
xcmPrtAuxPackageIndex = _XcmPrtAuxPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 1),
    _XcmPrtAuxPackageIndex_Type()
)
xcmPrtAuxPackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageIndex.setDescription("""\
 A unique value used by the printer to identify this Auxiliary Sheet.
""")
_XcmPrtAuxPackageRowStatus_Type = RowStatus
_XcmPrtAuxPackageRowStatus_Object = MibTableColumn
xcmPrtAuxPackageRowStatus = _XcmPrtAuxPackageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 2),
    _XcmPrtAuxPackageRowStatus_Type()
)
xcmPrtAuxPackageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageRowStatus.setDescription("""\
 Manages the status of this conceptual row in the xcmPrtAuxPackageTable.
""")
_XcmPrtAuxPackageType_Type = XcmPrtAuxSheetType
_XcmPrtAuxPackageType_Object = MibTableColumn
xcmPrtAuxPackageType = _XcmPrtAuxPackageType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 3),
    _XcmPrtAuxPackageType_Type()
)
xcmPrtAuxPackageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageType.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageType.setDescription("""\
 Specifies the Auxiliary Sheet type associated with this row. Note: DEFVAL
commented out due to the negative enum definition in 15prtxtc being illegal in
strict SMIv1 (see section 3.2.1.1 of RFC 1155).
""")


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
if mibBuilder.loadTexts:
    xcmPrtAuxPackageContent.setDescription("""\
 Specifies the information content of this auxiliary sheet. The value zero
shall mean notSpecified.
""")
_XcmPrtAuxPackagePrtInputIndex_Type = Cardinal32
_XcmPrtAuxPackagePrtInputIndex_Object = MibTableColumn
xcmPrtAuxPackagePrtInputIndex = _XcmPrtAuxPackagePrtInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 5),
    _XcmPrtAuxPackagePrtInputIndex_Type()
)
xcmPrtAuxPackagePrtInputIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtAuxPackagePrtInputIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtAuxPackagePrtInputIndex.setDescription("""\
 Specifies the input tray the printer shall use in printing this auxiliary
sheet. The value zero shall mean notSpecified.
""")
_XcmPrtAuxPackageNext_Type = Cardinal32
_XcmPrtAuxPackageNext_Object = MibTableColumn
xcmPrtAuxPackageNext = _XcmPrtAuxPackageNext_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 60, 1, 1, 6),
    _XcmPrtAuxPackageNext_Type()
)
xcmPrtAuxPackageNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageNext.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtAuxPackageNext.setDescription("""\
 Provides the index of the next Auxiliary Sheet declared for this printer. This
provides a linking mechanism to group auxiliary pages. The last auxiliary page
to be declared will set this xcmPrtAuxPackageNext object to zero, meaning no
further sheets. The value zero shall mean notPresent.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInterpPCLTable.setDescription("""\
 This table is an extension to the prtInterpPCLTable.
""")
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
if mibBuilder.loadTexts:
    xcmPrtInterpPCLEntry.setDescription("""\
 An entry exists corresponding to each entry in the xcmPrtInterpPCLTable.
""")
_XcmPrtInterpPCLRowStatus_Type = RowStatus
_XcmPrtInterpPCLRowStatus_Object = MibTableColumn
xcmPrtInterpPCLRowStatus = _XcmPrtInterpPCLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 1),
    _XcmPrtInterpPCLRowStatus_Type()
)
xcmPrtInterpPCLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLRowStatus.setDescription("""\
 Manages the status of this conceptual row in the xcmPrtInterpPCLTable.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpPCLFontSourceDflt.setReference("""\
 See: PJL Technical Reference Manual- FONTSOURCE
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLFontSourceDflt.setDescription("""\
 This object provides the PCL-specific PJL variable 'FONTSOURCE'. 'FONTSOURCE'
specifies the device location of the default font in PCL.
""")
_XcmPrtInterpPCLFontNumberDflt_Type = Cardinal32
_XcmPrtInterpPCLFontNumberDflt_Object = MibTableColumn
xcmPrtInterpPCLFontNumberDflt = _XcmPrtInterpPCLFontNumberDflt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 3),
    _XcmPrtInterpPCLFontNumberDflt_Type()
)
xcmPrtInterpPCLFontNumberDflt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLFontNumberDflt.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLFontNumberDflt.setReference("""\
 See: PJL Technical Reference Manual - FONTNUMBER
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLFontNumberDflt.setDescription("""\
 This object provides the PCL-specific PJL variable 'FONTNUMBER'. In PCL,
'FONTNUMBER' specifies the ID of the default font within the default
FONTSOURCE.
""")
_XcmPrtInterpPCLPitchNumerator_Type = Cardinal32
_XcmPrtInterpPCLPitchNumerator_Object = MibTableColumn
xcmPrtInterpPCLPitchNumerator = _XcmPrtInterpPCLPitchNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 4),
    _XcmPrtInterpPCLPitchNumerator_Type()
)
xcmPrtInterpPCLPitchNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPitchNumerator.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPitchNumerator.setReference("""\
 See: PCL 5 Printer Language Technical Reference Manual See: PJL Technical
Reference Manual - PITCH See: xcmPrtInterpPCLPitchDenominator
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPitchNumerator.setDescription("""\
 This object along with xcmPrtInterpPCLPitchDenominator sets the default for
the PCL-specific PJL variable 'PITCH. These two object sets the default pitch
size for the PCL default font defined in xcmPrtInterpreterPCLFontNumberDflt.
This variable only applies when the default font specified is a scalable fixed
pitch font. A value of zero shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPitchDenominator.setReference("""\
 See: PCL 5 Printer Language Technical Reference Manual See: PJL Technical
Reference Manual - PITCH See: xcmPrtInterpPCLPitchNumerator
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPitchDenominator.setDescription("""\
 This object along with xcmPrtInterpPCLPitchNumerator sets the default for the
PCL-specific PJL variable 'PITCH'. These two object sets the default pitch size
for the PCL default font defined in xcmPrtInterpreterPCLFontNumberDflt. The
PITCH variable only applies when the default font specified is a scalable fixed
pitch font. A value of zero shall mean not specified. It is expected that a
typical application will set xcmPrtInterpPCLPitchDenominator to 100.
""")
_XcmPrtInterpPCLPtSizeNumerator_Type = Cardinal32
_XcmPrtInterpPCLPtSizeNumerator_Object = MibTableColumn
xcmPrtInterpPCLPtSizeNumerator = _XcmPrtInterpPCLPtSizeNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 70, 1, 1, 6),
    _XcmPrtInterpPCLPtSizeNumerator_Type()
)
xcmPrtInterpPCLPtSizeNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPtSizeNumerator.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPtSizeNumerator.setReference("""\
 See: PJL Technical Reference Manual - PTSIZE See: PCL 5 Printer Language
Technical Reference Manual See: xcmPrtInterpPCLPtSizeDenominatr
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPtSizeNumerator.setDescription("""\
 This object along with xcmPrtInterpPCLPtSizeDenominatr sets the default for
the PCL-specific PJL variable 'PTSIZE'. The PTSIZE variable only applies when
the FONTNUMBER setting specifies a scalable proportionally-spaced font. The
size is in units of printer's points, which units are here considered to be
exactly 1/72 of an inch. The value zero shall mean not specified.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPtSizeDenominatr.setReference("""\
 See: PCL 5 Printer Language Technical Reference Manual See: PJL Technical
Reference Manual - PTSIZE See: xcmPrtInterpPCLPtSizeNumerator
""")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPtSizeDenominatr.setDescription("""\
 This object along with xcmPrtInterpPCLPtSizeNumerator sets the default for the
PCL-specific PJL variable 'PTSIZE'. The PTSIZE variable only applies when the
FONTNUMBER setting specifies a scalable proportionally-spaced font. The value
zero shall mean not specified. It is expected that a typical application will
set this object to the value 4. For example, if the denominator is set to 4,
describe a PtSize of 8.5, xcmPrtInterpPCLPtSizeNominator must be set to 34.
""")


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
if mibBuilder.loadTexts:
    xcmPrtInterpPCLPrintScreen.setDescription("""\
 This object sets a special mode for 80 character screen dumps.
""")
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
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupTable.setDescription("""\
 A table of specific and general medium 'types' which are associated with this
host system.
""")
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
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupEntry.setDescription("""\
 An entry for a specific or general medium 'types' which is associated with
this host system.
""")
_XcmPrtMedmTypeSupIndex_Type = Ordinal32
_XcmPrtMedmTypeSupIndex_Object = MibTableColumn
xcmPrtMedmTypeSupIndex = _XcmPrtMedmTypeSupIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 1),
    _XcmPrtMedmTypeSupIndex_Type()
)
xcmPrtMedmTypeSupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupIndex.setDescription("""\
 A unique value used to identify this medium type supported.
""")
_XcmPrtMedmTypeSupRowStatus_Type = RowStatus
_XcmPrtMedmTypeSupRowStatus_Object = MibTableColumn
xcmPrtMedmTypeSupRowStatus = _XcmPrtMedmTypeSupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 75, 2, 1, 2),
    _XcmPrtMedmTypeSupRowStatus_Type()
)
xcmPrtMedmTypeSupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupRowStatus.setDescription("""\
 Manages the status of this conceptual row in the 'xcmPrtMedmTypeSupTable'.
""")


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
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupRowPersistence.setDescription("""\
 Indicates persistence of this row, from the given enumeration.
""")


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
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupName.setReference("""\
 See: prtInputMediaType
""")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupName.setDescription("""\
 Named 'type' of this medium instance. This can be the name of the media type
provided by a user.
""")


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
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupFuserTemp.setDescription("""\
 Indicates the relative fuser temperature for this medium type. The range is 1
- 100. A value to '50' indciates the 'normal' fuser temperature. Values higher
than 50 indicate higher fuser temperatures. Values lower than 50 indicate lower
fuser temperatures. The value to use is device specific.
""")


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
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupPaperType.setReference("""\
 See: prtInputMediaType
""")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupPaperType.setDescription("""\
 The paper type for this xcmPrtMedmTypeSupName.
""")


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
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupPDLString.setReference("""\
 See: prtInputMediaType
""")
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupPDLString.setDescription("""\
 The string used in the print stream for this xcmPrtMedmTypeSupName.
""")


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
if mibBuilder.loadTexts:
    xcmPrtMedmTypeSupFuserHide.setDescription("""\
 Indicates if the custom type has to be hidden in host drivers. True means the
media type is not displayed. False means the media type can be selected for a
print job
""")

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
if mibBuilder.loadTexts:
    xcmPrtBaseGroup.setDescription("""\
 The general printer group extension.
""")

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
if mibBuilder.loadTexts:
    xcmPrtGeneralGroup.setDescription("""\
 The general printer group extension.
""")

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
if mibBuilder.loadTexts:
    xcmPrtDriverOptionsGroup.setDescription("""\
 The printer driver options group extension.
""")

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
if mibBuilder.loadTexts:
    xcmPrtInputGroup.setDescription("""\
 The input group extension.
""")

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
if mibBuilder.loadTexts:
    xcmPrtOutputGroup.setDescription("""\
 The output group extension.
""")

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
if mibBuilder.loadTexts:
    xcmPrtChannelGroup.setDescription("""\
 The Channel group extension.
""")

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
if mibBuilder.loadTexts:
    xcmPrtInterpreterGroup.setDescription("""\
 The interpreter group extension.
""")

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
if mibBuilder.loadTexts:
    xcmPrtInputAliasGroup.setDescription("""\
 The Input Alias group.
""")

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
if mibBuilder.loadTexts:
    xcmPrtOutputFinishingGroup.setDescription("""\
 The Output Finishing group.
""")

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
if mibBuilder.loadTexts:
    xcmPrtGeneralAuxSheetGroup.setDescription("""\
 The General Auxiliary Sheet group.
""")

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
if mibBuilder.loadTexts:
    xcmPrtGeneralProdSpecificGroup.setDescription("""\
 The general printer product specific group.
""")

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
if mibBuilder.loadTexts:
    xcmPrtAuxPackageGroup.setDescription("""\
 The Auxiliary Package group.
""")

xcmPrtChannelProdSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 64)
)
xcmPrtChannelProdSpecificGroup.setObjects(
      *(("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelAutoJobEnd"),
        ("XEROX-PRINTER-EXT-MIB", "xcmPrtChannelBinaryPostScriptZ"))
)
if mibBuilder.loadTexts:
    xcmPrtChannelProdSpecificGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtChannelProdSpecificGroup.setDescription("""\
 The Channel group extension for prod specific objects.
""")

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
if mibBuilder.loadTexts:
    xcmPrtInterpProdSpecificGroup.setDescription("""\
 The interpreter group extension.
""")

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
if mibBuilder.loadTexts:
    xcmPrtInterpPCLGroup.setDescription("""\
 The Interpreter PCL group.
""")

xcmPrtInterpPCLProdSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 55, 2, 2, 71)
)
xcmPrtInterpPCLProdSpecificGroup.setObjects(
    ("XEROX-PRINTER-EXT-MIB", "xcmPrtInterpPCLPrintScreen")
)
if mibBuilder.loadTexts:
    xcmPrtInterpPCLProdSpecificGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmPrtInterpPCLProdSpecificGroup.setDescription("""\
 The Interpreter PCL Product Specific group.
""")

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
if mibBuilder.loadTexts:
    xcmPrtMediumTypeSupportedGroup.setDescription("""\
 The Medium Type Supported group.
""")


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
if mibBuilder.loadTexts:
    xcmPrtGeneralConsoleLocalizationV2Event.setDescription("""\
This trap is sent when the value for prtConsoleLocalization in the industry
standard printer MIB gets updated. Note: The variable-bindings of this trap
have been chosen to allow for updated prtConsoleLocalization information to be
provided while keeping trap messages reasonably concise (generally a few
hundred octets at most).
""")


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
if mibBuilder.loadTexts:
    xcmPrtMIBCompliance.setDescription("""\
 The compliance statement for agents that implement the printer MIB extension
module.
""")


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
