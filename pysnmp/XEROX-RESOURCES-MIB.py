# SNMP MIB module (XEROX-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:32 2024
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

(IANACharset,) = mibBuilder.importSymbols(
    "IANA-CHARSET-MIB",
    "IANACharset")

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
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(Cardinal32,
 CodeIndexedStringIndex,
 Integer64High,
 Integer64Low,
 Ordinal32) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Cardinal32",
    "CodeIndexedStringIndex",
    "Integer64High",
    "Integer64Low",
    "Ordinal32")

(XcmPrtInterpreterLangFamily,) = mibBuilder.importSymbols(
    "XEROX-PRINTER-EXT-TC",
    "XcmPrtInterpreterLangFamily")

(XcmFontPCLStrokeWeight,
 XcmFontPCLStyle,
 XcmFontSpacing,
 XcmFontType,
 XcmRsrcGroupSupport,
 XcmRsrcPersistence,
 XcmRsrcType) = mibBuilder.importSymbols(
    "XEROX-RESOURCES-TC",
    "XcmFontPCLStrokeWeight",
    "XcmFontPCLStyle",
    "XcmFontSpacing",
    "XcmFontType",
    "XcmRsrcGroupSupport",
    "XcmRsrcPersistence",
    "XcmRsrcType")


# MODULE-IDENTITY

xcmRsrcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmRsrcGeneral_ObjectIdentity = ObjectIdentity
xcmRsrcGeneral = _XcmRsrcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1)
)
_XcmRsrcGeneralTable_Object = MibTable
xcmRsrcGeneralTable = _XcmRsrcGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1)
)
if mibBuilder.loadTexts:
    xcmRsrcGeneralTable.setStatus("current")
_XcmRsrcGeneralEntry_Object = MibTableRow
xcmRsrcGeneralEntry = _XcmRsrcGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1)
)
xcmRsrcGeneralEntry.setIndexNames(
    (0, "XEROX-RESOURCES-MIB", "xcmRsrcGeneralIndex"),
)
if mibBuilder.loadTexts:
    xcmRsrcGeneralEntry.setStatus("current")
_XcmRsrcGeneralIndex_Type = Ordinal32
_XcmRsrcGeneralIndex_Object = MibTableColumn
xcmRsrcGeneralIndex = _XcmRsrcGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 1),
    _XcmRsrcGeneralIndex_Type()
)
xcmRsrcGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmRsrcGeneralIndex.setStatus("current")
_XcmRsrcGeneralRowStatus_Type = RowStatus
_XcmRsrcGeneralRowStatus_Object = MibTableColumn
xcmRsrcGeneralRowStatus = _XcmRsrcGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 2),
    _XcmRsrcGeneralRowStatus_Type()
)
xcmRsrcGeneralRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRowStatus.setStatus("current")


class _XcmRsrcGeneralGroupSupport_Type(XcmRsrcGroupSupport):
    """Custom type xcmRsrcGeneralGroupSupport based on XcmRsrcGroupSupport"""
    defaultValue = 2


_XcmRsrcGeneralGroupSupport_Object = MibTableColumn
xcmRsrcGeneralGroupSupport = _XcmRsrcGeneralGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 3),
    _XcmRsrcGeneralGroupSupport_Type()
)
xcmRsrcGeneralGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralGroupSupport.setStatus("current")


class _XcmRsrcGeneralCreateSupport_Type(XcmRsrcGroupSupport):
    """Custom type xcmRsrcGeneralCreateSupport based on XcmRsrcGroupSupport"""
    defaultValue = 0


_XcmRsrcGeneralCreateSupport_Object = MibTableColumn
xcmRsrcGeneralCreateSupport = _XcmRsrcGeneralCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 4),
    _XcmRsrcGeneralCreateSupport_Type()
)
xcmRsrcGeneralCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralCreateSupport.setStatus("current")


class _XcmRsrcGeneralUpdateSupport_Type(XcmRsrcGroupSupport):
    """Custom type xcmRsrcGeneralUpdateSupport based on XcmRsrcGroupSupport"""
    defaultValue = 0


_XcmRsrcGeneralUpdateSupport_Object = MibTableColumn
xcmRsrcGeneralUpdateSupport = _XcmRsrcGeneralUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 5),
    _XcmRsrcGeneralUpdateSupport_Type()
)
xcmRsrcGeneralUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralUpdateSupport.setStatus("current")


class _XcmRsrcGeneralRsrcTypeAccept_Type(OctetString):
    """Custom type xcmRsrcGeneralRsrcTypeAccept based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XcmRsrcGeneralRsrcTypeAccept_Type.__name__ = "OctetString"
_XcmRsrcGeneralRsrcTypeAccept_Object = MibTableColumn
xcmRsrcGeneralRsrcTypeAccept = _XcmRsrcGeneralRsrcTypeAccept_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 6),
    _XcmRsrcGeneralRsrcTypeAccept_Type()
)
xcmRsrcGeneralRsrcTypeAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRsrcTypeAccept.setStatus("current")


class _XcmRsrcGeneralFontTypeAccept_Type(OctetString):
    """Custom type xcmRsrcGeneralFontTypeAccept based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmRsrcGeneralFontTypeAccept_Type.__name__ = "OctetString"
_XcmRsrcGeneralFontTypeAccept_Object = MibTableColumn
xcmRsrcGeneralFontTypeAccept = _XcmRsrcGeneralFontTypeAccept_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 7),
    _XcmRsrcGeneralFontTypeAccept_Type()
)
xcmRsrcGeneralFontTypeAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralFontTypeAccept.setStatus("current")


class _XcmRsrcGeneralRsrcTypeSupport_Type(OctetString):
    """Custom type xcmRsrcGeneralRsrcTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XcmRsrcGeneralRsrcTypeSupport_Type.__name__ = "OctetString"
_XcmRsrcGeneralRsrcTypeSupport_Object = MibTableColumn
xcmRsrcGeneralRsrcTypeSupport = _XcmRsrcGeneralRsrcTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 8),
    _XcmRsrcGeneralRsrcTypeSupport_Type()
)
xcmRsrcGeneralRsrcTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRsrcTypeSupport.setStatus("current")


class _XcmRsrcGeneralFontTypeSupport_Type(OctetString):
    """Custom type xcmRsrcGeneralFontTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmRsrcGeneralFontTypeSupport_Type.__name__ = "OctetString"
_XcmRsrcGeneralFontTypeSupport_Object = MibTableColumn
xcmRsrcGeneralFontTypeSupport = _XcmRsrcGeneralFontTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 9),
    _XcmRsrcGeneralFontTypeSupport_Type()
)
xcmRsrcGeneralFontTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralFontTypeSupport.setStatus("current")
_XcmRsrcMIBConformance_ObjectIdentity = ObjectIdentity
xcmRsrcMIBConformance = _XcmRsrcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2)
)
_XcmRsrcMIBGroups_ObjectIdentity = ObjectIdentity
xcmRsrcMIBGroups = _XcmRsrcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2)
)
_XcmRsrcInfo_ObjectIdentity = ObjectIdentity
xcmRsrcInfo = _XcmRsrcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3)
)
_XcmRsrcTable_Object = MibTable
xcmRsrcTable = _XcmRsrcTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1)
)
if mibBuilder.loadTexts:
    xcmRsrcTable.setStatus("current")
_XcmRsrcEntry_Object = MibTableRow
xcmRsrcEntry = _XcmRsrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1)
)
xcmRsrcEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-RESOURCES-MIB", "xcmRsrcIndex"),
)
if mibBuilder.loadTexts:
    xcmRsrcEntry.setStatus("current")
_XcmRsrcIndex_Type = Ordinal32
_XcmRsrcIndex_Object = MibTableColumn
xcmRsrcIndex = _XcmRsrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 1),
    _XcmRsrcIndex_Type()
)
xcmRsrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmRsrcIndex.setStatus("current")
_XcmRsrcRowStatus_Type = RowStatus
_XcmRsrcRowStatus_Object = MibTableColumn
xcmRsrcRowStatus = _XcmRsrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 2),
    _XcmRsrcRowStatus_Type()
)
xcmRsrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcRowStatus.setStatus("current")


class _XcmRsrcType_Type(XcmRsrcType):
    """Custom type xcmRsrcType based on XcmRsrcType"""


_XcmRsrcType_Object = MibTableColumn
xcmRsrcType = _XcmRsrcType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 3),
    _XcmRsrcType_Type()
)
xcmRsrcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcType.setStatus("current")


class _XcmRsrcInterpreterLangFamily_Type(XcmPrtInterpreterLangFamily):
    """Custom type xcmRsrcInterpreterLangFamily based on XcmPrtInterpreterLangFamily"""


_XcmRsrcInterpreterLangFamily_Object = MibTableColumn
xcmRsrcInterpreterLangFamily = _XcmRsrcInterpreterLangFamily_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 4),
    _XcmRsrcInterpreterLangFamily_Type()
)
xcmRsrcInterpreterLangFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcInterpreterLangFamily.setStatus("current")


class _XcmRsrcName_Type(CodeIndexedStringIndex):
    """Custom type xcmRsrcName based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmRsrcName_Object = MibTableColumn
xcmRsrcName = _XcmRsrcName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 5),
    _XcmRsrcName_Type()
)
xcmRsrcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcName.setStatus("current")


class _XcmRsrcDescription_Type(CodeIndexedStringIndex):
    """Custom type xcmRsrcDescription based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmRsrcDescription_Object = MibTableColumn
xcmRsrcDescription = _XcmRsrcDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 6),
    _XcmRsrcDescription_Type()
)
xcmRsrcDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcDescription.setStatus("current")


class _XcmRsrcCopyright_Type(CodeIndexedStringIndex):
    """Custom type xcmRsrcCopyright based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmRsrcCopyright_Object = MibTableColumn
xcmRsrcCopyright = _XcmRsrcCopyright_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 7),
    _XcmRsrcCopyright_Type()
)
xcmRsrcCopyright.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcCopyright.setStatus("current")


class _XcmRsrcPersistence_Type(XcmRsrcPersistence):
    """Custom type xcmRsrcPersistence based on XcmRsrcPersistence"""


_XcmRsrcPersistence_Object = MibTableColumn
xcmRsrcPersistence = _XcmRsrcPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 8),
    _XcmRsrcPersistence_Type()
)
xcmRsrcPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcPersistence.setStatus("current")


class _XcmRsrcHrStorageIndex_Type(Cardinal32):
    """Custom type xcmRsrcHrStorageIndex based on Cardinal32"""
    defaultValue = 0


_XcmRsrcHrStorageIndex_Object = MibTableColumn
xcmRsrcHrStorageIndex = _XcmRsrcHrStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 9),
    _XcmRsrcHrStorageIndex_Type()
)
xcmRsrcHrStorageIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcHrStorageIndex.setStatus("current")


class _XcmRsrcSizeHigh_Type(Integer64High):
    """Custom type xcmRsrcSizeHigh based on Integer64High"""
    defaultValue = -1


_XcmRsrcSizeHigh_Object = MibTableColumn
xcmRsrcSizeHigh = _XcmRsrcSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 10),
    _XcmRsrcSizeHigh_Type()
)
xcmRsrcSizeHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcSizeHigh.setStatus("current")


class _XcmRsrcSizeLow_Type(Integer64Low):
    """Custom type xcmRsrcSizeLow based on Integer64Low"""
    defaultValue = 0


_XcmRsrcSizeLow_Object = MibTableColumn
xcmRsrcSizeLow = _XcmRsrcSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 11),
    _XcmRsrcSizeLow_Type()
)
xcmRsrcSizeLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcSizeLow.setStatus("current")


class _XcmRsrcID_Type(CodeIndexedStringIndex):
    """Custom type xcmRsrcID based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmRsrcID_Object = MibTableColumn
xcmRsrcID = _XcmRsrcID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 12),
    _XcmRsrcID_Type()
)
xcmRsrcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcID.setStatus("current")


class _XcmRsrcVersion_Type(CodeIndexedStringIndex):
    """Custom type xcmRsrcVersion based on CodeIndexedStringIndex"""
    defaultValue = 0


_XcmRsrcVersion_Object = MibTableColumn
xcmRsrcVersion = _XcmRsrcVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 13),
    _XcmRsrcVersion_Type()
)
xcmRsrcVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcVersion.setStatus("current")
_XcmRsrcV1EventOID_ObjectIdentity = ObjectIdentity
xcmRsrcV1EventOID = _XcmRsrcV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 2)
)
if mibBuilder.loadTexts:
    xcmRsrcV1EventOID.setStatus("current")
_XcmRsrcV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmRsrcV2EventPrefix = _XcmRsrcV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 2, 0)
)
_XcmFontInfo_ObjectIdentity = ObjectIdentity
xcmFontInfo = _XcmFontInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4)
)
_XcmFontTable_Object = MibTable
xcmFontTable = _XcmFontTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1)
)
if mibBuilder.loadTexts:
    xcmFontTable.setStatus("current")
_XcmFontEntry_Object = MibTableRow
xcmFontEntry = _XcmFontEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1)
)
xcmFontEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-RESOURCES-MIB", "xcmRsrcIndex"),
)
if mibBuilder.loadTexts:
    xcmFontEntry.setStatus("current")
_XcmFontRowStatus_Type = RowStatus
_XcmFontRowStatus_Object = MibTableColumn
xcmFontRowStatus = _XcmFontRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 1),
    _XcmFontRowStatus_Type()
)
xcmFontRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontRowStatus.setStatus("current")


class _XcmFontType_Type(XcmFontType):
    """Custom type xcmFontType based on XcmFontType"""


_XcmFontType_Object = MibTableColumn
xcmFontType = _XcmFontType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 2),
    _XcmFontType_Type()
)
xcmFontType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontType.setStatus("current")


class _XcmFontPointsMinNumerator_Type(Integer32):
    """Custom type xcmFontPointsMinNumerator based on Integer32"""
    defaultValue = -2


_XcmFontPointsMinNumerator_Object = MibTableColumn
xcmFontPointsMinNumerator = _XcmFontPointsMinNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 3),
    _XcmFontPointsMinNumerator_Type()
)
xcmFontPointsMinNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPointsMinNumerator.setStatus("current")


class _XcmFontPointsMaxNumerator_Type(Integer32):
    """Custom type xcmFontPointsMaxNumerator based on Integer32"""
    defaultValue = -2


_XcmFontPointsMaxNumerator_Object = MibTableColumn
xcmFontPointsMaxNumerator = _XcmFontPointsMaxNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 4),
    _XcmFontPointsMaxNumerator_Type()
)
xcmFontPointsMaxNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPointsMaxNumerator.setStatus("current")


class _XcmFontPointsDenominator_Type(Integer32):
    """Custom type xcmFontPointsDenominator based on Integer32"""
    defaultValue = -2


_XcmFontPointsDenominator_Object = MibTableColumn
xcmFontPointsDenominator = _XcmFontPointsDenominator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 5),
    _XcmFontPointsDenominator_Type()
)
xcmFontPointsDenominator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPointsDenominator.setStatus("current")


class _XcmFontSpacing_Type(XcmFontSpacing):
    """Custom type xcmFontSpacing based on XcmFontSpacing"""


_XcmFontSpacing_Object = MibTableColumn
xcmFontSpacing = _XcmFontSpacing_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 6),
    _XcmFontSpacing_Type()
)
xcmFontSpacing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontSpacing.setStatus("current")


class _XcmFontCharSet_Type(IANACharset):
    """Custom type xcmFontCharSet based on IANACharset"""


_XcmFontCharSet_Object = MibTableColumn
xcmFontCharSet = _XcmFontCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 7),
    _XcmFontCharSet_Type()
)
xcmFontCharSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontCharSet.setStatus("current")
_XcmFontPCLInfo_ObjectIdentity = ObjectIdentity
xcmFontPCLInfo = _XcmFontPCLInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5)
)
_XcmFontPCLTable_Object = MibTable
xcmFontPCLTable = _XcmFontPCLTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1)
)
if mibBuilder.loadTexts:
    xcmFontPCLTable.setStatus("current")
_XcmFontPCLEntry_Object = MibTableRow
xcmFontPCLEntry = _XcmFontPCLEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1)
)
xcmFontPCLEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-RESOURCES-MIB", "xcmRsrcIndex"),
)
if mibBuilder.loadTexts:
    xcmFontPCLEntry.setStatus("current")
_XcmFontPCLRowStatus_Type = RowStatus
_XcmFontPCLRowStatus_Object = MibTableColumn
xcmFontPCLRowStatus = _XcmFontPCLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 1),
    _XcmFontPCLRowStatus_Type()
)
xcmFontPCLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLRowStatus.setStatus("current")


class _XcmFontPCLTypefaceValue_Type(Integer32):
    """Custom type xcmFontPCLTypefaceValue based on Integer32"""
    defaultValue = -1


_XcmFontPCLTypefaceValue_Object = MibTableColumn
xcmFontPCLTypefaceValue = _XcmFontPCLTypefaceValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 2),
    _XcmFontPCLTypefaceValue_Type()
)
xcmFontPCLTypefaceValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLTypefaceValue.setStatus("current")


class _XcmFontPCLSymbolSetValue_Type(Integer32):
    """Custom type xcmFontPCLSymbolSetValue based on Integer32"""
    defaultValue = -1


_XcmFontPCLSymbolSetValue_Object = MibTableColumn
xcmFontPCLSymbolSetValue = _XcmFontPCLSymbolSetValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 3),
    _XcmFontPCLSymbolSetValue_Type()
)
xcmFontPCLSymbolSetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLSymbolSetValue.setStatus("current")


class _XcmFontPCLStyle_Type(XcmFontPCLStyle):
    """Custom type xcmFontPCLStyle based on XcmFontPCLStyle"""


_XcmFontPCLStyle_Object = MibTableColumn
xcmFontPCLStyle = _XcmFontPCLStyle_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 4),
    _XcmFontPCLStyle_Type()
)
xcmFontPCLStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLStyle.setStatus("current")


class _XcmFontPCLPitchMinNumerator_Type(Integer32):
    """Custom type xcmFontPCLPitchMinNumerator based on Integer32"""
    defaultValue = -2


_XcmFontPCLPitchMinNumerator_Object = MibTableColumn
xcmFontPCLPitchMinNumerator = _XcmFontPCLPitchMinNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 5),
    _XcmFontPCLPitchMinNumerator_Type()
)
xcmFontPCLPitchMinNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLPitchMinNumerator.setStatus("current")


class _XcmFontPCLPitchMaxNumerator_Type(Integer32):
    """Custom type xcmFontPCLPitchMaxNumerator based on Integer32"""
    defaultValue = -2


_XcmFontPCLPitchMaxNumerator_Object = MibTableColumn
xcmFontPCLPitchMaxNumerator = _XcmFontPCLPitchMaxNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 6),
    _XcmFontPCLPitchMaxNumerator_Type()
)
xcmFontPCLPitchMaxNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLPitchMaxNumerator.setStatus("current")


class _XcmFontPCLPitchDenominator_Type(Integer32):
    """Custom type xcmFontPCLPitchDenominator based on Integer32"""
    defaultValue = -2


_XcmFontPCLPitchDenominator_Object = MibTableColumn
xcmFontPCLPitchDenominator = _XcmFontPCLPitchDenominator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 7),
    _XcmFontPCLPitchDenominator_Type()
)
xcmFontPCLPitchDenominator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLPitchDenominator.setStatus("current")


class _XcmFontPCLStrokeWeight_Type(XcmFontPCLStrokeWeight):
    """Custom type xcmFontPCLStrokeWeight based on XcmFontPCLStrokeWeight"""


_XcmFontPCLStrokeWeight_Object = MibTableColumn
xcmFontPCLStrokeWeight = _XcmFontPCLStrokeWeight_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 8),
    _XcmFontPCLStrokeWeight_Type()
)
xcmFontPCLStrokeWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLStrokeWeight.setStatus("current")

# Managed Objects groups

xcmRsrcGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2, 1)
)
xcmRsrcGeneralGroup.setObjects(
      *(("XEROX-RESOURCES-MIB", "xcmRsrcGeneralRowStatus"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralGroupSupport"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralCreateSupport"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralUpdateSupport"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralRsrcTypeAccept"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralFontTypeAccept"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralRsrcTypeSupport"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralFontTypeSupport"))
)
if mibBuilder.loadTexts:
    xcmRsrcGeneralGroup.setStatus("current")

xcmRsrcInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2, 3)
)
xcmRsrcInfoGroup.setObjects(
      *(("XEROX-RESOURCES-MIB", "xcmRsrcRowStatus"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcType"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcInterpreterLangFamily"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcName"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcDescription"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcCopyright"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcPersistence"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcHrStorageIndex"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcSizeHigh"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcSizeLow"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcID"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcVersion"))
)
if mibBuilder.loadTexts:
    xcmRsrcInfoGroup.setStatus("current")

xcmFontInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2, 4)
)
xcmFontInfoGroup.setObjects(
      *(("XEROX-RESOURCES-MIB", "xcmFontRowStatus"),
        ("XEROX-RESOURCES-MIB", "xcmFontType"),
        ("XEROX-RESOURCES-MIB", "xcmFontPointsMinNumerator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPointsMaxNumerator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPointsDenominator"),
        ("XEROX-RESOURCES-MIB", "xcmFontSpacing"),
        ("XEROX-RESOURCES-MIB", "xcmFontCharSet"))
)
if mibBuilder.loadTexts:
    xcmFontInfoGroup.setStatus("current")

xcmFontPCLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2, 5)
)
xcmFontPCLGroup.setObjects(
      *(("XEROX-RESOURCES-MIB", "xcmFontPCLRowStatus"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLTypefaceValue"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLSymbolSetValue"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLStyle"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLPitchMinNumerator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLPitchMaxNumerator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLPitchDenominator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLStrokeWeight"))
)
if mibBuilder.loadTexts:
    xcmFontPCLGroup.setStatus("current")


# Notification objects

xcmRsrcV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 2, 0, 1)
)
xcmRsrcV2Event.setObjects(
    ("XEROX-RESOURCES-MIB", "xcmRsrcRowStatus")
)
if mibBuilder.loadTexts:
    xcmRsrcV2Event.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

xcmRsrcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 1)
)
if mibBuilder.loadTexts:
    xcmRsrcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-RESOURCES-MIB",
    **{"xcmRsrcMIB": xcmRsrcMIB,
       "xcmRsrcGeneral": xcmRsrcGeneral,
       "xcmRsrcGeneralTable": xcmRsrcGeneralTable,
       "xcmRsrcGeneralEntry": xcmRsrcGeneralEntry,
       "xcmRsrcGeneralIndex": xcmRsrcGeneralIndex,
       "xcmRsrcGeneralRowStatus": xcmRsrcGeneralRowStatus,
       "xcmRsrcGeneralGroupSupport": xcmRsrcGeneralGroupSupport,
       "xcmRsrcGeneralCreateSupport": xcmRsrcGeneralCreateSupport,
       "xcmRsrcGeneralUpdateSupport": xcmRsrcGeneralUpdateSupport,
       "xcmRsrcGeneralRsrcTypeAccept": xcmRsrcGeneralRsrcTypeAccept,
       "xcmRsrcGeneralFontTypeAccept": xcmRsrcGeneralFontTypeAccept,
       "xcmRsrcGeneralRsrcTypeSupport": xcmRsrcGeneralRsrcTypeSupport,
       "xcmRsrcGeneralFontTypeSupport": xcmRsrcGeneralFontTypeSupport,
       "xcmRsrcMIBConformance": xcmRsrcMIBConformance,
       "xcmRsrcMIBCompliance": xcmRsrcMIBCompliance,
       "xcmRsrcMIBGroups": xcmRsrcMIBGroups,
       "xcmRsrcGeneralGroup": xcmRsrcGeneralGroup,
       "xcmRsrcInfoGroup": xcmRsrcInfoGroup,
       "xcmFontInfoGroup": xcmFontInfoGroup,
       "xcmFontPCLGroup": xcmFontPCLGroup,
       "xcmRsrcInfo": xcmRsrcInfo,
       "xcmRsrcTable": xcmRsrcTable,
       "xcmRsrcEntry": xcmRsrcEntry,
       "xcmRsrcIndex": xcmRsrcIndex,
       "xcmRsrcRowStatus": xcmRsrcRowStatus,
       "xcmRsrcType": xcmRsrcType,
       "xcmRsrcInterpreterLangFamily": xcmRsrcInterpreterLangFamily,
       "xcmRsrcName": xcmRsrcName,
       "xcmRsrcDescription": xcmRsrcDescription,
       "xcmRsrcCopyright": xcmRsrcCopyright,
       "xcmRsrcPersistence": xcmRsrcPersistence,
       "xcmRsrcHrStorageIndex": xcmRsrcHrStorageIndex,
       "xcmRsrcSizeHigh": xcmRsrcSizeHigh,
       "xcmRsrcSizeLow": xcmRsrcSizeLow,
       "xcmRsrcID": xcmRsrcID,
       "xcmRsrcVersion": xcmRsrcVersion,
       "xcmRsrcV1EventOID": xcmRsrcV1EventOID,
       "xcmRsrcV2EventPrefix": xcmRsrcV2EventPrefix,
       "xcmRsrcV2Event": xcmRsrcV2Event,
       "xcmFontInfo": xcmFontInfo,
       "xcmFontTable": xcmFontTable,
       "xcmFontEntry": xcmFontEntry,
       "xcmFontRowStatus": xcmFontRowStatus,
       "xcmFontType": xcmFontType,
       "xcmFontPointsMinNumerator": xcmFontPointsMinNumerator,
       "xcmFontPointsMaxNumerator": xcmFontPointsMaxNumerator,
       "xcmFontPointsDenominator": xcmFontPointsDenominator,
       "xcmFontSpacing": xcmFontSpacing,
       "xcmFontCharSet": xcmFontCharSet,
       "xcmFontPCLInfo": xcmFontPCLInfo,
       "xcmFontPCLTable": xcmFontPCLTable,
       "xcmFontPCLEntry": xcmFontPCLEntry,
       "xcmFontPCLRowStatus": xcmFontPCLRowStatus,
       "xcmFontPCLTypefaceValue": xcmFontPCLTypefaceValue,
       "xcmFontPCLSymbolSetValue": xcmFontPCLSymbolSetValue,
       "xcmFontPCLStyle": xcmFontPCLStyle,
       "xcmFontPCLPitchMinNumerator": xcmFontPCLPitchMinNumerator,
       "xcmFontPCLPitchMaxNumerator": xcmFontPCLPitchMaxNumerator,
       "xcmFontPCLPitchDenominator": xcmFontPCLPitchDenominator,
       "xcmFontPCLStrokeWeight": xcmFontPCLStrokeWeight}
)
