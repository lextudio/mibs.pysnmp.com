# SNMP MIB module (XEROX-GENERAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-GENERAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:19 2024
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

(InternationalDisplayString,
 ProductID,
 hrDeviceIndex) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString",
    "ProductID",
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(Cardinal32,
 CodeIndexedStringIndex,
 CodedCountry,
 CodedLanguage,
 Ordinal16,
 Ordinal32,
 XcmFixedLocaleDisplayString,
 XcmGenGroupSupport,
 XcmGenMessageMapStringLabel,
 XcmGenNotifyDetailType,
 XcmGenNotifySchemeSupport,
 XcmGenNotifySeverityFilter,
 XcmGenNotifyTrainingFilter,
 XcmGenOptionValueSyntax,
 XcmGenReconfOptionState,
 XcmGenRowPersistence,
 XcmGenSNMPDomain,
 XcmGenSNMPVersion,
 XcmGenSNMPv2ErrorStatus,
 XcmGlobalUniqueID,
 XcmNamedLocaleUtf8String,
 zeroDotZero) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Cardinal32",
    "CodeIndexedStringIndex",
    "CodedCountry",
    "CodedLanguage",
    "Ordinal16",
    "Ordinal32",
    "XcmFixedLocaleDisplayString",
    "XcmGenGroupSupport",
    "XcmGenMessageMapStringLabel",
    "XcmGenNotifyDetailType",
    "XcmGenNotifySchemeSupport",
    "XcmGenNotifySeverityFilter",
    "XcmGenNotifyTrainingFilter",
    "XcmGenOptionValueSyntax",
    "XcmGenReconfOptionState",
    "XcmGenRowPersistence",
    "XcmGenSNMPDomain",
    "XcmGenSNMPVersion",
    "XcmGenSNMPv2ErrorStatus",
    "XcmGlobalUniqueID",
    "XcmNamedLocaleUtf8String",
    "zeroDotZero")


# MODULE-IDENTITY

xcmGeneralMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmGenZeroDummy_ObjectIdentity = ObjectIdentity
xcmGenZeroDummy = _XcmGenZeroDummy_ObjectIdentity(
    (0, 0, 51)
)
_XcmGenBase_ObjectIdentity = ObjectIdentity
xcmGenBase = _XcmGenBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1)
)
_XcmGenBaseTable_Object = MibTable
xcmGenBaseTable = _XcmGenBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2)
)
if mibBuilder.loadTexts:
    xcmGenBaseTable.setStatus("current")
_XcmGenBaseEntry_Object = MibTableRow
xcmGenBaseEntry = _XcmGenBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1)
)
xcmGenBaseEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenBaseIndex"),
)
if mibBuilder.loadTexts:
    xcmGenBaseEntry.setStatus("current")
_XcmGenBaseIndex_Type = Ordinal32
_XcmGenBaseIndex_Object = MibTableColumn
xcmGenBaseIndex = _XcmGenBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 1),
    _XcmGenBaseIndex_Type()
)
xcmGenBaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenBaseIndex.setStatus("current")
_XcmGenBaseRowStatus_Type = RowStatus
_XcmGenBaseRowStatus_Object = MibTableColumn
xcmGenBaseRowStatus = _XcmGenBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 2),
    _XcmGenBaseRowStatus_Type()
)
xcmGenBaseRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseRowStatus.setStatus("current")


class _XcmGenBaseSystemHrDeviceIndex_Type(Cardinal32):
    """Custom type xcmGenBaseSystemHrDeviceIndex based on Cardinal32"""
    defaultValue = 0


_XcmGenBaseSystemHrDeviceIndex_Object = MibTableColumn
xcmGenBaseSystemHrDeviceIndex = _XcmGenBaseSystemHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 3),
    _XcmGenBaseSystemHrDeviceIndex_Type()
)
xcmGenBaseSystemHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSystemHrDeviceIndex.setStatus("current")


class _XcmGenBaseGroupSupport_Type(XcmGenGroupSupport):
    """Custom type xcmGenBaseGroupSupport based on XcmGenGroupSupport"""
    defaultValue = 3584


_XcmGenBaseGroupSupport_Object = MibTableColumn
xcmGenBaseGroupSupport = _XcmGenBaseGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 4),
    _XcmGenBaseGroupSupport_Type()
)
xcmGenBaseGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseGroupSupport.setStatus("current")


class _XcmGenBaseGroupCreateSupport_Type(XcmGenGroupSupport):
    """Custom type xcmGenBaseGroupCreateSupport based on XcmGenGroupSupport"""
    defaultValue = 1536


_XcmGenBaseGroupCreateSupport_Object = MibTableColumn
xcmGenBaseGroupCreateSupport = _XcmGenBaseGroupCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 5),
    _XcmGenBaseGroupCreateSupport_Type()
)
xcmGenBaseGroupCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseGroupCreateSupport.setStatus("current")


class _XcmGenBaseGroupUpdateSupport_Type(XcmGenGroupSupport):
    """Custom type xcmGenBaseGroupUpdateSupport based on XcmGenGroupSupport"""
    defaultValue = 3584


_XcmGenBaseGroupUpdateSupport_Object = MibTableColumn
xcmGenBaseGroupUpdateSupport = _XcmGenBaseGroupUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 6),
    _XcmGenBaseGroupUpdateSupport_Type()
)
xcmGenBaseGroupUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseGroupUpdateSupport.setStatus("current")


class _XcmGenBaseClientDataMaxSupport_Type(Cardinal32):
    """Custom type xcmGenBaseClientDataMaxSupport based on Cardinal32"""
    defaultValue = 0


_XcmGenBaseClientDataMaxSupport_Object = MibTableColumn
xcmGenBaseClientDataMaxSupport = _XcmGenBaseClientDataMaxSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 7),
    _XcmGenBaseClientDataMaxSupport_Type()
)
xcmGenBaseClientDataMaxSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseClientDataMaxSupport.setStatus("current")


class _XcmGenBaseOptionSyntaxSupport_Type(Cardinal32):
    """Custom type xcmGenBaseOptionSyntaxSupport based on Cardinal32"""
    defaultValue = 0


_XcmGenBaseOptionSyntaxSupport_Object = MibTableColumn
xcmGenBaseOptionSyntaxSupport = _XcmGenBaseOptionSyntaxSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 8),
    _XcmGenBaseOptionSyntaxSupport_Type()
)
xcmGenBaseOptionSyntaxSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseOptionSyntaxSupport.setStatus("current")


class _XcmGenBaseReconfStateSupport_Type(Cardinal32):
    """Custom type xcmGenBaseReconfStateSupport based on Cardinal32"""
    defaultValue = 0


_XcmGenBaseReconfStateSupport_Object = MibTableColumn
xcmGenBaseReconfStateSupport = _XcmGenBaseReconfStateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 9),
    _XcmGenBaseReconfStateSupport_Type()
)
xcmGenBaseReconfStateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseReconfStateSupport.setStatus("current")
_XcmGenBaseSNMPDomainSupport_Type = Cardinal32
_XcmGenBaseSNMPDomainSupport_Object = MibTableColumn
xcmGenBaseSNMPDomainSupport = _XcmGenBaseSNMPDomainSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 10),
    _XcmGenBaseSNMPDomainSupport_Type()
)
xcmGenBaseSNMPDomainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPDomainSupport.setStatus("current")
_XcmGenBaseSNMPTrapSupport_Type = TruthValue
_XcmGenBaseSNMPTrapSupport_Object = MibTableColumn
xcmGenBaseSNMPTrapSupport = _XcmGenBaseSNMPTrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 11),
    _XcmGenBaseSNMPTrapSupport_Type()
)
xcmGenBaseSNMPTrapSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPTrapSupport.setStatus("current")
_XcmGenBaseSNMPVersionSupport_Type = Cardinal32
_XcmGenBaseSNMPVersionSupport_Object = MibTableColumn
xcmGenBaseSNMPVersionSupport = _XcmGenBaseSNMPVersionSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 12),
    _XcmGenBaseSNMPVersionSupport_Type()
)
xcmGenBaseSNMPVersionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPVersionSupport.setStatus("current")


class _XcmGenBaseSNMPReadCommunity_Type(OctetString):
    """Custom type xcmGenBaseSNMPReadCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmGenBaseSNMPReadCommunity_Type.__name__ = "OctetString"
_XcmGenBaseSNMPReadCommunity_Object = MibTableColumn
xcmGenBaseSNMPReadCommunity = _XcmGenBaseSNMPReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 13),
    _XcmGenBaseSNMPReadCommunity_Type()
)
xcmGenBaseSNMPReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPReadCommunity.setStatus("current")


class _XcmGenBaseSNMPWriteCommunity_Type(OctetString):
    """Custom type xcmGenBaseSNMPWriteCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmGenBaseSNMPWriteCommunity_Type.__name__ = "OctetString"
_XcmGenBaseSNMPWriteCommunity_Object = MibTableColumn
xcmGenBaseSNMPWriteCommunity = _XcmGenBaseSNMPWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 14),
    _XcmGenBaseSNMPWriteCommunity_Type()
)
xcmGenBaseSNMPWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPWriteCommunity.setStatus("current")


class _XcmGenBaseSNMPTrapCommunity_Type(OctetString):
    """Custom type xcmGenBaseSNMPTrapCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmGenBaseSNMPTrapCommunity_Type.__name__ = "OctetString"
_XcmGenBaseSNMPTrapCommunity_Object = MibTableColumn
xcmGenBaseSNMPTrapCommunity = _XcmGenBaseSNMPTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 15),
    _XcmGenBaseSNMPTrapCommunity_Type()
)
xcmGenBaseSNMPTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPTrapCommunity.setStatus("current")


class _XcmGenBaseGroupWalkHidden_Type(XcmGenGroupSupport):
    """Custom type xcmGenBaseGroupWalkHidden based on XcmGenGroupSupport"""
    defaultValue = 12288


_XcmGenBaseGroupWalkHidden_Object = MibTableColumn
xcmGenBaseGroupWalkHidden = _XcmGenBaseGroupWalkHidden_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 16),
    _XcmGenBaseGroupWalkHidden_Type()
)
xcmGenBaseGroupWalkHidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseGroupWalkHidden.setStatus("current")


class _XcmGenBaseNotifySchemeSupport_Type(XcmGenNotifySchemeSupport):
    """Custom type xcmGenBaseNotifySchemeSupport based on XcmGenNotifySchemeSupport"""
    defaultValue = 1


_XcmGenBaseNotifySchemeSupport_Object = MibTableColumn
xcmGenBaseNotifySchemeSupport = _XcmGenBaseNotifySchemeSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 17),
    _XcmGenBaseNotifySchemeSupport_Type()
)
xcmGenBaseNotifySchemeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseNotifySchemeSupport.setStatus("current")


class _XcmGenBaseNotifySeveritySupport_Type(XcmGenNotifySeverityFilter):
    """Custom type xcmGenBaseNotifySeveritySupport based on XcmGenNotifySeverityFilter"""
    defaultValue = 15


_XcmGenBaseNotifySeveritySupport_Object = MibTableColumn
xcmGenBaseNotifySeveritySupport = _XcmGenBaseNotifySeveritySupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 18),
    _XcmGenBaseNotifySeveritySupport_Type()
)
xcmGenBaseNotifySeveritySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseNotifySeveritySupport.setStatus("current")


class _XcmGenBaseNotifyTrainingSupport_Type(XcmGenNotifyTrainingFilter):
    """Custom type xcmGenBaseNotifyTrainingSupport based on XcmGenNotifyTrainingFilter"""
    defaultValue = 60


_XcmGenBaseNotifyTrainingSupport_Object = MibTableColumn
xcmGenBaseNotifyTrainingSupport = _XcmGenBaseNotifyTrainingSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 19),
    _XcmGenBaseNotifyTrainingSupport_Type()
)
xcmGenBaseNotifyTrainingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseNotifyTrainingSupport.setStatus("current")


class _XcmGenBaseSystem1284DeviceId_Type(DisplayString):
    """Custom type xcmGenBaseSystem1284DeviceId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenBaseSystem1284DeviceId_Type.__name__ = "DisplayString"
_XcmGenBaseSystem1284DeviceId_Object = MibTableColumn
xcmGenBaseSystem1284DeviceId = _XcmGenBaseSystem1284DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 20),
    _XcmGenBaseSystem1284DeviceId_Type()
)
xcmGenBaseSystem1284DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSystem1284DeviceId.setStatus("current")


class _XcmGenBaseSNMPWarningTrapSupport_Type(TruthValue):
    """Custom type xcmGenBaseSNMPWarningTrapSupport based on TruthValue"""


_XcmGenBaseSNMPWarningTrapSupport_Object = MibTableColumn
xcmGenBaseSNMPWarningTrapSupport = _XcmGenBaseSNMPWarningTrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 21),
    _XcmGenBaseSNMPWarningTrapSupport_Type()
)
xcmGenBaseSNMPWarningTrapSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPWarningTrapSupport.setStatus("current")
_XcmGeneralMIBConformance_ObjectIdentity = ObjectIdentity
xcmGeneralMIBConformance = _XcmGeneralMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2)
)
_XcmGeneralMIBGroups_ObjectIdentity = ObjectIdentity
xcmGeneralMIBGroups = _XcmGeneralMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2)
)
_XcmGenCurrentLocalization_ObjectIdentity = ObjectIdentity
xcmGenCurrentLocalization = _XcmGenCurrentLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3)
)
_XcmGenCurrentLocalizationTable_Object = MibTable
xcmGenCurrentLocalizationTable = _XcmGenCurrentLocalizationTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3, 1)
)
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationTable.setStatus("current")
_XcmGenCurrentLocalizationEntry_Object = MibTableRow
xcmGenCurrentLocalizationEntry = _XcmGenCurrentLocalizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3, 1, 1)
)
xcmGenCurrentLocalizationEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationEntry.setStatus("current")
_XcmGenCurrentLocalizationIndex_Type = Ordinal16
_XcmGenCurrentLocalizationIndex_Object = MibTableColumn
xcmGenCurrentLocalizationIndex = _XcmGenCurrentLocalizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3, 1, 1, 1),
    _XcmGenCurrentLocalizationIndex_Type()
)
xcmGenCurrentLocalizationIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationIndex.setStatus("current")
_XcmGenCurrLocalizationRowStatus_Type = RowStatus
_XcmGenCurrLocalizationRowStatus_Object = MibTableColumn
xcmGenCurrLocalizationRowStatus = _XcmGenCurrLocalizationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3, 1, 1, 2),
    _XcmGenCurrLocalizationRowStatus_Type()
)
xcmGenCurrLocalizationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCurrLocalizationRowStatus.setStatus("current")
_XcmGenLocalization_ObjectIdentity = ObjectIdentity
xcmGenLocalization = _XcmGenLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4)
)
_XcmGenLocalizationTable_Object = MibTable
xcmGenLocalizationTable = _XcmGenLocalizationTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1)
)
if mibBuilder.loadTexts:
    xcmGenLocalizationTable.setStatus("current")
_XcmGenLocalizationEntry_Object = MibTableRow
xcmGenLocalizationEntry = _XcmGenLocalizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1)
)
xcmGenLocalizationEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenLocalizationIndex"),
)
if mibBuilder.loadTexts:
    xcmGenLocalizationEntry.setStatus("current")
_XcmGenLocalizationIndex_Type = Ordinal16
_XcmGenLocalizationIndex_Object = MibTableColumn
xcmGenLocalizationIndex = _XcmGenLocalizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 1),
    _XcmGenLocalizationIndex_Type()
)
xcmGenLocalizationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenLocalizationIndex.setStatus("current")
_XcmGenLocalizationRowStatus_Type = RowStatus
_XcmGenLocalizationRowStatus_Object = MibTableColumn
xcmGenLocalizationRowStatus = _XcmGenLocalizationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 2),
    _XcmGenLocalizationRowStatus_Type()
)
xcmGenLocalizationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationRowStatus.setStatus("current")


class _XcmGenLocalizationASCIIName_Type(DisplayString):
    """Custom type xcmGenLocalizationASCIIName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenLocalizationASCIIName_Type.__name__ = "DisplayString"
_XcmGenLocalizationASCIIName_Object = MibTableColumn
xcmGenLocalizationASCIIName = _XcmGenLocalizationASCIIName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 3),
    _XcmGenLocalizationASCIIName_Type()
)
xcmGenLocalizationASCIIName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationASCIIName.setStatus("current")


class _XcmGenLocalizationName_Type(InternationalDisplayString):
    """Custom type xcmGenLocalizationName based on InternationalDisplayString"""
    defaultHexValue = ""

    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenLocalizationName_Type.__name__ = "InternationalDisplayString"
_XcmGenLocalizationName_Object = MibTableColumn
xcmGenLocalizationName = _XcmGenLocalizationName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 4),
    _XcmGenLocalizationName_Type()
)
xcmGenLocalizationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationName.setStatus("current")


class _XcmGenLocalizationLanguage_Type(CodedLanguage):
    """Custom type xcmGenLocalizationLanguage based on CodedLanguage"""
    defaultHexValue = ""


_XcmGenLocalizationLanguage_Object = MibTableColumn
xcmGenLocalizationLanguage = _XcmGenLocalizationLanguage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 5),
    _XcmGenLocalizationLanguage_Type()
)
xcmGenLocalizationLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationLanguage.setStatus("current")


class _XcmGenLocalizationCountry_Type(CodedCountry):
    """Custom type xcmGenLocalizationCountry based on CodedCountry"""
    defaultHexValue = ""


_XcmGenLocalizationCountry_Object = MibTableColumn
xcmGenLocalizationCountry = _XcmGenLocalizationCountry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 6),
    _XcmGenLocalizationCountry_Type()
)
xcmGenLocalizationCountry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationCountry.setStatus("current")


class _XcmGenLocalizationCharSet_Type(IANACharset):
    """Custom type xcmGenLocalizationCharSet based on IANACharset"""


_XcmGenLocalizationCharSet_Object = MibTableColumn
xcmGenLocalizationCharSet = _XcmGenLocalizationCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 7),
    _XcmGenLocalizationCharSet_Type()
)
xcmGenLocalizationCharSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationCharSet.setStatus("current")
_XcmGenCodeIndexedString_ObjectIdentity = ObjectIdentity
xcmGenCodeIndexedString = _XcmGenCodeIndexedString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5)
)
_XcmGenCodeIndexedStringTable_Object = MibTable
xcmGenCodeIndexedStringTable = _XcmGenCodeIndexedStringTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1)
)
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringTable.setStatus("current")
_XcmGenCodeIndexedStringEntry_Object = MibTableRow
xcmGenCodeIndexedStringEntry = _XcmGenCodeIndexedStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1)
)
xcmGenCodeIndexedStringEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenCodeIndexedStringIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenCodeIndexedStringCharSet"),
)
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringEntry.setStatus("current")


class _XcmGenCodeIndexedStringIndex_Type(CodeIndexedStringIndex):
    """Custom type xcmGenCodeIndexedStringIndex based on CodeIndexedStringIndex"""
    subtypeSpec = CodeIndexedStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XcmGenCodeIndexedStringIndex_Type.__name__ = "CodeIndexedStringIndex"
_XcmGenCodeIndexedStringIndex_Object = MibTableColumn
xcmGenCodeIndexedStringIndex = _XcmGenCodeIndexedStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1, 1),
    _XcmGenCodeIndexedStringIndex_Type()
)
xcmGenCodeIndexedStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringIndex.setStatus("current")
_XcmGenCodeIndexedStringCharSet_Type = IANACharset
_XcmGenCodeIndexedStringCharSet_Object = MibTableColumn
xcmGenCodeIndexedStringCharSet = _XcmGenCodeIndexedStringCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1, 2),
    _XcmGenCodeIndexedStringCharSet_Type()
)
xcmGenCodeIndexedStringCharSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringCharSet.setStatus("current")
_XcmGenCodeIndexedStringRowStat_Type = RowStatus
_XcmGenCodeIndexedStringRowStat_Object = MibTableColumn
xcmGenCodeIndexedStringRowStat = _XcmGenCodeIndexedStringRowStat_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1, 3),
    _XcmGenCodeIndexedStringRowStat_Type()
)
xcmGenCodeIndexedStringRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringRowStat.setStatus("current")


class _XcmGenCodeIndexedStringData_Type(OctetString):
    """Custom type xcmGenCodeIndexedStringData based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenCodeIndexedStringData_Type.__name__ = "OctetString"
_XcmGenCodeIndexedStringData_Object = MibTableColumn
xcmGenCodeIndexedStringData = _XcmGenCodeIndexedStringData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1, 4),
    _XcmGenCodeIndexedStringData_Type()
)
xcmGenCodeIndexedStringData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringData.setStatus("current")
_XcmGenCodedCharSet_ObjectIdentity = ObjectIdentity
xcmGenCodedCharSet = _XcmGenCodedCharSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6)
)
_XcmGenCodedCharSetTable_Object = MibTable
xcmGenCodedCharSetTable = _XcmGenCodedCharSetTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1)
)
if mibBuilder.loadTexts:
    xcmGenCodedCharSetTable.setStatus("current")
_XcmGenCodedCharSetEntry_Object = MibTableRow
xcmGenCodedCharSetEntry = _XcmGenCodedCharSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1, 1)
)
xcmGenCodedCharSetEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenCodedCharSetCharSet"),
)
if mibBuilder.loadTexts:
    xcmGenCodedCharSetEntry.setStatus("current")
_XcmGenCodedCharSetCharSet_Type = IANACharset
_XcmGenCodedCharSetCharSet_Object = MibTableColumn
xcmGenCodedCharSetCharSet = _XcmGenCodedCharSetCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1, 1, 1),
    _XcmGenCodedCharSetCharSet_Type()
)
xcmGenCodedCharSetCharSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetCharSet.setStatus("current")
_XcmGenCodedCharSetRowStatus_Type = RowStatus
_XcmGenCodedCharSetRowStatus_Object = MibTableColumn
xcmGenCodedCharSetRowStatus = _XcmGenCodedCharSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1, 1, 2),
    _XcmGenCodedCharSetRowStatus_Type()
)
xcmGenCodedCharSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetRowStatus.setStatus("current")


class _XcmGenCodedCharSetASCIIName_Type(DisplayString):
    """Custom type xcmGenCodedCharSetASCIIName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenCodedCharSetASCIIName_Type.__name__ = "DisplayString"
_XcmGenCodedCharSetASCIIName_Object = MibTableColumn
xcmGenCodedCharSetASCIIName = _XcmGenCodedCharSetASCIIName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1, 1, 3),
    _XcmGenCodedCharSetASCIIName_Type()
)
xcmGenCodedCharSetASCIIName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetASCIIName.setStatus("current")
_XcmGenFixedLocalization_ObjectIdentity = ObjectIdentity
xcmGenFixedLocalization = _XcmGenFixedLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7)
)
_XcmGenFixedLocalizationTable_Object = MibTable
xcmGenFixedLocalizationTable = _XcmGenFixedLocalizationTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7, 1)
)
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationTable.setStatus("current")
_XcmGenFixedLocalizationEntry_Object = MibTableRow
xcmGenFixedLocalizationEntry = _XcmGenFixedLocalizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7, 1, 1)
)
xcmGenFixedLocalizationEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationEntry.setStatus("current")
_XcmGenFixedLocalizationIndex_Type = Ordinal16
_XcmGenFixedLocalizationIndex_Object = MibTableColumn
xcmGenFixedLocalizationIndex = _XcmGenFixedLocalizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7, 1, 1, 1),
    _XcmGenFixedLocalizationIndex_Type()
)
xcmGenFixedLocalizationIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationIndex.setStatus("current")
_XcmGenFixedLocalizationRowStat_Type = RowStatus
_XcmGenFixedLocalizationRowStat_Object = MibTableColumn
xcmGenFixedLocalizationRowStat = _XcmGenFixedLocalizationRowStat_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7, 1, 1, 2),
    _XcmGenFixedLocalizationRowStat_Type()
)
xcmGenFixedLocalizationRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationRowStat.setStatus("current")
_XcmGenLock_ObjectIdentity = ObjectIdentity
xcmGenLock = _XcmGenLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8)
)
_XcmGenLockSimple_ObjectIdentity = ObjectIdentity
xcmGenLockSimple = _XcmGenLockSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1)
)
if mibBuilder.loadTexts:
    xcmGenLockSimple.setStatus("current")


class _XcmGenLockSupportMaxTimer_Type(Cardinal32):
    """Custom type xcmGenLockSupportMaxTimer based on Cardinal32"""
    defaultValue = 0


_XcmGenLockSupportMaxTimer_Object = MibScalar
xcmGenLockSupportMaxTimer = _XcmGenLockSupportMaxTimer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 1),
    _XcmGenLockSupportMaxTimer_Type()
)
xcmGenLockSupportMaxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxTimer.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxTimer.setUnits("seconds")


class _XcmGenLockCurrentMaxTimer_Type(Cardinal32):
    """Custom type xcmGenLockCurrentMaxTimer based on Cardinal32"""
    defaultValue = 0


_XcmGenLockCurrentMaxTimer_Object = MibScalar
xcmGenLockCurrentMaxTimer = _XcmGenLockCurrentMaxTimer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 2),
    _XcmGenLockCurrentMaxTimer_Type()
)
xcmGenLockCurrentMaxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockCurrentMaxTimer.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockCurrentMaxTimer.setUnits("seconds")


class _XcmGenLockCurrentLockCount_Type(Cardinal32):
    """Custom type xcmGenLockCurrentLockCount based on Cardinal32"""
    defaultValue = 0


_XcmGenLockCurrentLockCount_Object = MibScalar
xcmGenLockCurrentLockCount = _XcmGenLockCurrentLockCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 3),
    _XcmGenLockCurrentLockCount_Type()
)
xcmGenLockCurrentLockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockCurrentLockCount.setStatus("current")


class _XcmGenLockHighestLockIndex_Type(Cardinal32):
    """Custom type xcmGenLockHighestLockIndex based on Cardinal32"""
    defaultValue = 0


_XcmGenLockHighestLockIndex_Object = MibScalar
xcmGenLockHighestLockIndex = _XcmGenLockHighestLockIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 4),
    _XcmGenLockHighestLockIndex_Type()
)
xcmGenLockHighestLockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockHighestLockIndex.setStatus("current")


class _XcmGenLockSupportMaxCount_Type(Cardinal32):
    """Custom type xcmGenLockSupportMaxCount based on Cardinal32"""
    defaultValue = 0


_XcmGenLockSupportMaxCount_Object = MibScalar
xcmGenLockSupportMaxCount = _XcmGenLockSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 5),
    _XcmGenLockSupportMaxCount_Type()
)
xcmGenLockSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxCount.setStatus("current")
_XcmGenLockTable_Object = MibTable
xcmGenLockTable = _XcmGenLockTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2)
)
if mibBuilder.loadTexts:
    xcmGenLockTable.setStatus("current")
_XcmGenLockEntry_Object = MibTableRow
xcmGenLockEntry = _XcmGenLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1)
)
xcmGenLockEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenLockIndex"),
)
if mibBuilder.loadTexts:
    xcmGenLockEntry.setStatus("current")
_XcmGenLockIndex_Type = Ordinal32
_XcmGenLockIndex_Object = MibTableColumn
xcmGenLockIndex = _XcmGenLockIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 1),
    _XcmGenLockIndex_Type()
)
xcmGenLockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenLockIndex.setStatus("current")
_XcmGenLockRowStatus_Type = RowStatus
_XcmGenLockRowStatus_Object = MibTableColumn
xcmGenLockRowStatus = _XcmGenLockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 2),
    _XcmGenLockRowStatus_Type()
)
xcmGenLockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLockRowStatus.setStatus("current")


class _XcmGenLockOwnerString_Type(OctetString):
    """Custom type xcmGenLockOwnerString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenLockOwnerString_Type.__name__ = "OctetString"
_XcmGenLockOwnerString_Object = MibTableColumn
xcmGenLockOwnerString = _XcmGenLockOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 3),
    _XcmGenLockOwnerString_Type()
)
xcmGenLockOwnerString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLockOwnerString.setStatus("current")


class _XcmGenLockOwnerSubtree_Type(ObjectIdentifier):
    """Custom type xcmGenLockOwnerSubtree based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmGenLockOwnerSubtree_Object = MibTableColumn
xcmGenLockOwnerSubtree = _XcmGenLockOwnerSubtree_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 4),
    _XcmGenLockOwnerSubtree_Type()
)
xcmGenLockOwnerSubtree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLockOwnerSubtree.setStatus("current")
_XcmGenLockOwnerTimer_Type = Cardinal32
_XcmGenLockOwnerTimer_Object = MibTableColumn
xcmGenLockOwnerTimer = _XcmGenLockOwnerTimer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 5),
    _XcmGenLockOwnerTimer_Type()
)
xcmGenLockOwnerTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLockOwnerTimer.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockOwnerTimer.setUnits("seconds")
_XcmGenReconf_ObjectIdentity = ObjectIdentity
xcmGenReconf = _XcmGenReconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9)
)
_XcmGenReconfSimple_ObjectIdentity = ObjectIdentity
xcmGenReconfSimple = _XcmGenReconfSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 1)
)
if mibBuilder.loadTexts:
    xcmGenReconfSimple.setStatus("current")
_XcmGenReconfActivations_Type = Counter32
_XcmGenReconfActivations_Object = MibScalar
xcmGenReconfActivations = _XcmGenReconfActivations_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 1, 1),
    _XcmGenReconfActivations_Type()
)
xcmGenReconfActivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfActivations.setStatus("current")
_XcmGenReconfEntryCount_Type = Counter32
_XcmGenReconfEntryCount_Object = MibScalar
xcmGenReconfEntryCount = _XcmGenReconfEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 1, 2),
    _XcmGenReconfEntryCount_Type()
)
xcmGenReconfEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfEntryCount.setStatus("current")


class _XcmGenReconfSupportMaxCount_Type(Cardinal32):
    """Custom type xcmGenReconfSupportMaxCount based on Cardinal32"""
    defaultValue = 0


_XcmGenReconfSupportMaxCount_Object = MibScalar
xcmGenReconfSupportMaxCount = _XcmGenReconfSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 1, 3),
    _XcmGenReconfSupportMaxCount_Type()
)
xcmGenReconfSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfSupportMaxCount.setStatus("current")
_XcmGenReconfTable_Object = MibTable
xcmGenReconfTable = _XcmGenReconfTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2)
)
if mibBuilder.loadTexts:
    xcmGenReconfTable.setStatus("current")
_XcmGenReconfEntry_Object = MibTableRow
xcmGenReconfEntry = _XcmGenReconfEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1)
)
xcmGenReconfEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenReconfIndex"),
)
if mibBuilder.loadTexts:
    xcmGenReconfEntry.setStatus("current")
_XcmGenReconfIndex_Type = Ordinal32
_XcmGenReconfIndex_Object = MibTableColumn
xcmGenReconfIndex = _XcmGenReconfIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 1),
    _XcmGenReconfIndex_Type()
)
xcmGenReconfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenReconfIndex.setStatus("current")
_XcmGenReconfRowStatus_Type = RowStatus
_XcmGenReconfRowStatus_Object = MibTableColumn
xcmGenReconfRowStatus = _XcmGenReconfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 2),
    _XcmGenReconfRowStatus_Type()
)
xcmGenReconfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenReconfRowStatus.setStatus("current")


class _XcmGenReconfOptionIndex_Type(Cardinal32):
    """Custom type xcmGenReconfOptionIndex based on Cardinal32"""
    defaultValue = 0


_XcmGenReconfOptionIndex_Object = MibTableColumn
xcmGenReconfOptionIndex = _XcmGenReconfOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 3),
    _XcmGenReconfOptionIndex_Type()
)
xcmGenReconfOptionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenReconfOptionIndex.setStatus("current")


class _XcmGenReconfOptionState_Type(XcmGenReconfOptionState):
    """Custom type xcmGenReconfOptionState based on XcmGenReconfOptionState"""


_XcmGenReconfOptionState_Object = MibTableColumn
xcmGenReconfOptionState = _XcmGenReconfOptionState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 4),
    _XcmGenReconfOptionState_Type()
)
xcmGenReconfOptionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenReconfOptionState.setStatus("current")


class _XcmGenReconfErrorIndex_Type(Cardinal32):
    """Custom type xcmGenReconfErrorIndex based on Cardinal32"""
    defaultValue = 0


_XcmGenReconfErrorIndex_Object = MibTableColumn
xcmGenReconfErrorIndex = _XcmGenReconfErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 5),
    _XcmGenReconfErrorIndex_Type()
)
xcmGenReconfErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfErrorIndex.setStatus("current")
_XcmGenReconfErrorStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmGenReconfErrorStatus_Object = MibTableColumn
xcmGenReconfErrorStatus = _XcmGenReconfErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 6),
    _XcmGenReconfErrorStatus_Type()
)
xcmGenReconfErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfErrorStatus.setStatus("current")
_XcmGenOption_ObjectIdentity = ObjectIdentity
xcmGenOption = _XcmGenOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10)
)
_XcmGenOptionSimple_ObjectIdentity = ObjectIdentity
xcmGenOptionSimple = _XcmGenOptionSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1)
)
if mibBuilder.loadTexts:
    xcmGenOptionSimple.setStatus("current")
_XcmGenOptionOperation_ObjectIdentity = ObjectIdentity
xcmGenOptionOperation = _XcmGenOptionOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 1)
)
_XcmGenOptionOperationInsert_ObjectIdentity = ObjectIdentity
xcmGenOptionOperationInsert = _XcmGenOptionOperationInsert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 1, 1)
)
_XcmGenOptionOperationDelete_ObjectIdentity = ObjectIdentity
xcmGenOptionOperationDelete = _XcmGenOptionOperationDelete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 1, 2)
)
_XcmGenOptionOperationReplace_ObjectIdentity = ObjectIdentity
xcmGenOptionOperationReplace = _XcmGenOptionOperationReplace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 1, 3)
)
_XcmGenOptionEntryCount_Type = Counter32
_XcmGenOptionEntryCount_Object = MibScalar
xcmGenOptionEntryCount = _XcmGenOptionEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 2),
    _XcmGenOptionEntryCount_Type()
)
xcmGenOptionEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenOptionEntryCount.setStatus("current")


class _XcmGenOptionSupportMaxCount_Type(Cardinal32):
    """Custom type xcmGenOptionSupportMaxCount based on Cardinal32"""
    defaultValue = 0


_XcmGenOptionSupportMaxCount_Object = MibScalar
xcmGenOptionSupportMaxCount = _XcmGenOptionSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 3),
    _XcmGenOptionSupportMaxCount_Type()
)
xcmGenOptionSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenOptionSupportMaxCount.setStatus("current")
_XcmGenOptionTable_Object = MibTable
xcmGenOptionTable = _XcmGenOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2)
)
if mibBuilder.loadTexts:
    xcmGenOptionTable.setStatus("current")
_XcmGenOptionEntry_Object = MibTableRow
xcmGenOptionEntry = _XcmGenOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1)
)
xcmGenOptionEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenOptionIndex"),
)
if mibBuilder.loadTexts:
    xcmGenOptionEntry.setStatus("current")
_XcmGenOptionIndex_Type = Ordinal32
_XcmGenOptionIndex_Object = MibTableColumn
xcmGenOptionIndex = _XcmGenOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 1),
    _XcmGenOptionIndex_Type()
)
xcmGenOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenOptionIndex.setStatus("current")
_XcmGenOptionRowStatus_Type = RowStatus
_XcmGenOptionRowStatus_Object = MibTableColumn
xcmGenOptionRowStatus = _XcmGenOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 2),
    _XcmGenOptionRowStatus_Type()
)
xcmGenOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionRowStatus.setStatus("current")


class _XcmGenOptionTypeOID_Type(ObjectIdentifier):
    """Custom type xcmGenOptionTypeOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmGenOptionTypeOID_Object = MibTableColumn
xcmGenOptionTypeOID = _XcmGenOptionTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 3),
    _XcmGenOptionTypeOID_Type()
)
xcmGenOptionTypeOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionTypeOID.setStatus("current")


class _XcmGenOptionValueSyntax_Type(XcmGenOptionValueSyntax):
    """Custom type xcmGenOptionValueSyntax based on XcmGenOptionValueSyntax"""


_XcmGenOptionValueSyntax_Object = MibTableColumn
xcmGenOptionValueSyntax = _XcmGenOptionValueSyntax_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 4),
    _XcmGenOptionValueSyntax_Type()
)
xcmGenOptionValueSyntax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueSyntax.setStatus("current")


class _XcmGenOptionValueInteger_Type(Integer32):
    """Custom type xcmGenOptionValueInteger based on Integer32"""
    defaultValue = 0


_XcmGenOptionValueInteger_Object = MibTableColumn
xcmGenOptionValueInteger = _XcmGenOptionValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 5),
    _XcmGenOptionValueInteger_Type()
)
xcmGenOptionValueInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueInteger.setStatus("current")


class _XcmGenOptionValueOID_Type(ObjectIdentifier):
    """Custom type xcmGenOptionValueOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmGenOptionValueOID_Object = MibTableColumn
xcmGenOptionValueOID = _XcmGenOptionValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 6),
    _XcmGenOptionValueOID_Type()
)
xcmGenOptionValueOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueOID.setStatus("current")


class _XcmGenOptionValueString_Type(OctetString):
    """Custom type xcmGenOptionValueString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenOptionValueString_Type.__name__ = "OctetString"
_XcmGenOptionValueString_Object = MibTableColumn
xcmGenOptionValueString = _XcmGenOptionValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 7),
    _XcmGenOptionValueString_Type()
)
xcmGenOptionValueString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueString.setStatus("current")


class _XcmGenOptionValueLocalization_Type(Cardinal32):
    """Custom type xcmGenOptionValueLocalization based on Cardinal32"""
    defaultValue = 0


_XcmGenOptionValueLocalization_Object = MibTableColumn
xcmGenOptionValueLocalization = _XcmGenOptionValueLocalization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 8),
    _XcmGenOptionValueLocalization_Type()
)
xcmGenOptionValueLocalization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueLocalization.setStatus("current")


class _XcmGenOptionValueCodedCharSet_Type(IANACharset):
    """Custom type xcmGenOptionValueCodedCharSet based on IANACharset"""


_XcmGenOptionValueCodedCharSet_Object = MibTableColumn
xcmGenOptionValueCodedCharSet = _XcmGenOptionValueCodedCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 9),
    _XcmGenOptionValueCodedCharSet_Type()
)
xcmGenOptionValueCodedCharSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueCodedCharSet.setStatus("current")


class _XcmGenOptionNextIndex_Type(Cardinal32):
    """Custom type xcmGenOptionNextIndex based on Cardinal32"""
    defaultValue = 0


_XcmGenOptionNextIndex_Object = MibTableColumn
xcmGenOptionNextIndex = _XcmGenOptionNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 10),
    _XcmGenOptionNextIndex_Type()
)
xcmGenOptionNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionNextIndex.setStatus("current")


class _XcmGenOptionPreviousIndex_Type(Cardinal32):
    """Custom type xcmGenOptionPreviousIndex based on Cardinal32"""
    defaultValue = 0


_XcmGenOptionPreviousIndex_Object = MibTableColumn
xcmGenOptionPreviousIndex = _XcmGenOptionPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 11),
    _XcmGenOptionPreviousIndex_Type()
)
xcmGenOptionPreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionPreviousIndex.setStatus("current")


class _XcmGenOptionFamilyIndex_Type(Cardinal32):
    """Custom type xcmGenOptionFamilyIndex based on Cardinal32"""
    defaultValue = 0


_XcmGenOptionFamilyIndex_Object = MibTableColumn
xcmGenOptionFamilyIndex = _XcmGenOptionFamilyIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 12),
    _XcmGenOptionFamilyIndex_Type()
)
xcmGenOptionFamilyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionFamilyIndex.setStatus("current")
_XcmGenClientData_ObjectIdentity = ObjectIdentity
xcmGenClientData = _XcmGenClientData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11)
)
_XcmGenClientDataSimple_ObjectIdentity = ObjectIdentity
xcmGenClientDataSimple = _XcmGenClientDataSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 1)
)
if mibBuilder.loadTexts:
    xcmGenClientDataSimple.setStatus("current")
_XcmGenClientDataEntryCount_Type = Counter32
_XcmGenClientDataEntryCount_Object = MibScalar
xcmGenClientDataEntryCount = _XcmGenClientDataEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 1, 1),
    _XcmGenClientDataEntryCount_Type()
)
xcmGenClientDataEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenClientDataEntryCount.setStatus("current")
_XcmGenClientDataLastIndex_Type = Cardinal32
_XcmGenClientDataLastIndex_Object = MibScalar
xcmGenClientDataLastIndex = _XcmGenClientDataLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 1, 2),
    _XcmGenClientDataLastIndex_Type()
)
xcmGenClientDataLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenClientDataLastIndex.setStatus("current")


class _XcmGenClientDataSupportMaxCount_Type(Cardinal32):
    """Custom type xcmGenClientDataSupportMaxCount based on Cardinal32"""
    defaultValue = 0


_XcmGenClientDataSupportMaxCount_Object = MibScalar
xcmGenClientDataSupportMaxCount = _XcmGenClientDataSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 1, 3),
    _XcmGenClientDataSupportMaxCount_Type()
)
xcmGenClientDataSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenClientDataSupportMaxCount.setStatus("current")
_XcmGenClientDataTable_Object = MibTable
xcmGenClientDataTable = _XcmGenClientDataTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2)
)
if mibBuilder.loadTexts:
    xcmGenClientDataTable.setStatus("current")
_XcmGenClientDataEntry_Object = MibTableRow
xcmGenClientDataEntry = _XcmGenClientDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1)
)
xcmGenClientDataEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenClientDataIndex"),
)
if mibBuilder.loadTexts:
    xcmGenClientDataEntry.setStatus("current")
_XcmGenClientDataIndex_Type = Ordinal32
_XcmGenClientDataIndex_Object = MibTableColumn
xcmGenClientDataIndex = _XcmGenClientDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 1),
    _XcmGenClientDataIndex_Type()
)
xcmGenClientDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenClientDataIndex.setStatus("current")
_XcmGenClientDataRowStatus_Type = RowStatus
_XcmGenClientDataRowStatus_Object = MibTableColumn
xcmGenClientDataRowStatus = _XcmGenClientDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 2),
    _XcmGenClientDataRowStatus_Type()
)
xcmGenClientDataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataRowStatus.setStatus("current")


class _XcmGenClientDataRequestDate_Type(DateAndTime):
    """Custom type xcmGenClientDataRequestDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmGenClientDataRequestDate_Object = MibTableColumn
xcmGenClientDataRequestDate = _XcmGenClientDataRequestDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 3),
    _XcmGenClientDataRequestDate_Type()
)
xcmGenClientDataRequestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenClientDataRequestDate.setStatus("current")


class _XcmGenClientDataRequestID_Type(XcmGlobalUniqueID):
    """Custom type xcmGenClientDataRequestID based on XcmGlobalUniqueID"""
    defaultHexValue = ""


_XcmGenClientDataRequestID_Object = MibTableColumn
xcmGenClientDataRequestID = _XcmGenClientDataRequestID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 4),
    _XcmGenClientDataRequestID_Type()
)
xcmGenClientDataRequestID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataRequestID.setStatus("current")


class _XcmGenClientDataProductID_Type(ProductID):
    """Custom type xcmGenClientDataProductID based on ProductID"""
    defaultValue = (0, 0)


_XcmGenClientDataProductID_Object = MibTableColumn
xcmGenClientDataProductID = _XcmGenClientDataProductID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 5),
    _XcmGenClientDataProductID_Type()
)
xcmGenClientDataProductID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataProductID.setStatus("current")


class _XcmGenClientDataLength_Type(Cardinal32):
    """Custom type xcmGenClientDataLength based on Cardinal32"""
    defaultValue = 0


_XcmGenClientDataLength_Object = MibTableColumn
xcmGenClientDataLength = _XcmGenClientDataLength_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 6),
    _XcmGenClientDataLength_Type()
)
xcmGenClientDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataLength.setStatus("current")


class _XcmGenClientDataString_Type(OctetString):
    """Custom type xcmGenClientDataString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenClientDataString_Type.__name__ = "OctetString"
_XcmGenClientDataString_Object = MibTableColumn
xcmGenClientDataString = _XcmGenClientDataString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 7),
    _XcmGenClientDataString_Type()
)
xcmGenClientDataString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataString.setStatus("current")
_XcmGenTrapClient_ObjectIdentity = ObjectIdentity
xcmGenTrapClient = _XcmGenTrapClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13)
)
_XcmGenTrapClientSimple_ObjectIdentity = ObjectIdentity
xcmGenTrapClientSimple = _XcmGenTrapClientSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 1)
)
if mibBuilder.loadTexts:
    xcmGenTrapClientSimple.setStatus("current")
_XcmGenTrapClientEntryCount_Type = Counter32
_XcmGenTrapClientEntryCount_Object = MibScalar
xcmGenTrapClientEntryCount = _XcmGenTrapClientEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 1, 1),
    _XcmGenTrapClientEntryCount_Type()
)
xcmGenTrapClientEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapClientEntryCount.setStatus("current")


class _XcmGenTrapClientSupportMaxCount_Type(Cardinal32):
    """Custom type xcmGenTrapClientSupportMaxCount based on Cardinal32"""
    defaultValue = 0


_XcmGenTrapClientSupportMaxCount_Object = MibScalar
xcmGenTrapClientSupportMaxCount = _XcmGenTrapClientSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 1, 2),
    _XcmGenTrapClientSupportMaxCount_Type()
)
xcmGenTrapClientSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapClientSupportMaxCount.setStatus("current")
_XcmGenTrapClientTable_Object = MibTable
xcmGenTrapClientTable = _XcmGenTrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2)
)
if mibBuilder.loadTexts:
    xcmGenTrapClientTable.setStatus("current")
_XcmGenTrapClientEntry_Object = MibTableRow
xcmGenTrapClientEntry = _XcmGenTrapClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1)
)
xcmGenTrapClientEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenTrapClientSNMPDomain"),
    (0, "XEROX-GENERAL-MIB", "xcmGenTrapClientSNMPAddress"),
)
if mibBuilder.loadTexts:
    xcmGenTrapClientEntry.setStatus("current")
_XcmGenTrapClientSNMPDomain_Type = XcmGenSNMPDomain
_XcmGenTrapClientSNMPDomain_Object = MibTableColumn
xcmGenTrapClientSNMPDomain = _XcmGenTrapClientSNMPDomain_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 1),
    _XcmGenTrapClientSNMPDomain_Type()
)
xcmGenTrapClientSNMPDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPDomain.setStatus("current")


class _XcmGenTrapClientSNMPAddress_Type(OctetString):
    """Custom type xcmGenTrapClientSNMPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenTrapClientSNMPAddress_Type.__name__ = "OctetString"
_XcmGenTrapClientSNMPAddress_Object = MibTableColumn
xcmGenTrapClientSNMPAddress = _XcmGenTrapClientSNMPAddress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 2),
    _XcmGenTrapClientSNMPAddress_Type()
)
xcmGenTrapClientSNMPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPAddress.setStatus("current")
_XcmGenTrapClientRowStatus_Type = RowStatus
_XcmGenTrapClientRowStatus_Object = MibTableColumn
xcmGenTrapClientRowStatus = _XcmGenTrapClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 3),
    _XcmGenTrapClientRowStatus_Type()
)
xcmGenTrapClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapClientRowStatus.setStatus("current")
_XcmGenTrapClientIndex_Type = Ordinal32
_XcmGenTrapClientIndex_Object = MibTableColumn
xcmGenTrapClientIndex = _XcmGenTrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 4),
    _XcmGenTrapClientIndex_Type()
)
xcmGenTrapClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapClientIndex.setStatus("current")


class _XcmGenTrapClientRowPersistence_Type(XcmGenRowPersistence):
    """Custom type xcmGenTrapClientRowPersistence based on XcmGenRowPersistence"""


_XcmGenTrapClientRowPersistence_Object = MibTableColumn
xcmGenTrapClientRowPersistence = _XcmGenTrapClientRowPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 5),
    _XcmGenTrapClientRowPersistence_Type()
)
xcmGenTrapClientRowPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapClientRowPersistence.setStatus("current")


class _XcmGenTrapClientSNMPVersion_Type(XcmGenSNMPVersion):
    """Custom type xcmGenTrapClientSNMPVersion based on XcmGenSNMPVersion"""


_XcmGenTrapClientSNMPVersion_Object = MibTableColumn
xcmGenTrapClientSNMPVersion = _XcmGenTrapClientSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 6),
    _XcmGenTrapClientSNMPVersion_Type()
)
xcmGenTrapClientSNMPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPVersion.setStatus("current")


class _XcmGenTrapClientSNMPCommunity_Type(OctetString):
    """Custom type xcmGenTrapClientSNMPCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmGenTrapClientSNMPCommunity_Type.__name__ = "OctetString"
_XcmGenTrapClientSNMPCommunity_Object = MibTableColumn
xcmGenTrapClientSNMPCommunity = _XcmGenTrapClientSNMPCommunity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 7),
    _XcmGenTrapClientSNMPCommunity_Type()
)
xcmGenTrapClientSNMPCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPCommunity.setStatus("current")
_XcmGenTrapView_ObjectIdentity = ObjectIdentity
xcmGenTrapView = _XcmGenTrapView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14)
)
_XcmGenTrapViewSimple_ObjectIdentity = ObjectIdentity
xcmGenTrapViewSimple = _XcmGenTrapViewSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 1)
)
if mibBuilder.loadTexts:
    xcmGenTrapViewSimple.setStatus("current")
_XcmGenTrapViewEntryCount_Type = Counter32
_XcmGenTrapViewEntryCount_Object = MibScalar
xcmGenTrapViewEntryCount = _XcmGenTrapViewEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 1, 1),
    _XcmGenTrapViewEntryCount_Type()
)
xcmGenTrapViewEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapViewEntryCount.setStatus("current")


class _XcmGenTrapViewSupportMaxCount_Type(Cardinal32):
    """Custom type xcmGenTrapViewSupportMaxCount based on Cardinal32"""
    defaultValue = 0


_XcmGenTrapViewSupportMaxCount_Object = MibScalar
xcmGenTrapViewSupportMaxCount = _XcmGenTrapViewSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 1, 2),
    _XcmGenTrapViewSupportMaxCount_Type()
)
xcmGenTrapViewSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapViewSupportMaxCount.setStatus("current")
_XcmGenTrapViewTable_Object = MibTable
xcmGenTrapViewTable = _XcmGenTrapViewTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2)
)
if mibBuilder.loadTexts:
    xcmGenTrapViewTable.setStatus("current")
_XcmGenTrapViewEntry_Object = MibTableRow
xcmGenTrapViewEntry = _XcmGenTrapViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1)
)
xcmGenTrapViewEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenTrapClientIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenTrapViewObjectSubtree"),
)
if mibBuilder.loadTexts:
    xcmGenTrapViewEntry.setStatus("current")
_XcmGenTrapViewObjectSubtree_Type = ObjectIdentifier
_XcmGenTrapViewObjectSubtree_Object = MibTableColumn
xcmGenTrapViewObjectSubtree = _XcmGenTrapViewObjectSubtree_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1, 1),
    _XcmGenTrapViewObjectSubtree_Type()
)
xcmGenTrapViewObjectSubtree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenTrapViewObjectSubtree.setStatus("current")
_XcmGenTrapViewRowStatus_Type = RowStatus
_XcmGenTrapViewRowStatus_Object = MibTableColumn
xcmGenTrapViewRowStatus = _XcmGenTrapViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1, 2),
    _XcmGenTrapViewRowStatus_Type()
)
xcmGenTrapViewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapViewRowStatus.setStatus("current")


class _XcmGenTrapViewNotifySeverity_Type(XcmGenNotifySeverityFilter):
    """Custom type xcmGenTrapViewNotifySeverity based on XcmGenNotifySeverityFilter"""
    defaultValue = 15


_XcmGenTrapViewNotifySeverity_Object = MibTableColumn
xcmGenTrapViewNotifySeverity = _XcmGenTrapViewNotifySeverity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1, 3),
    _XcmGenTrapViewNotifySeverity_Type()
)
xcmGenTrapViewNotifySeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapViewNotifySeverity.setStatus("current")


class _XcmGenTrapViewNotifyTraining_Type(XcmGenNotifyTrainingFilter):
    """Custom type xcmGenTrapViewNotifyTraining based on XcmGenNotifyTrainingFilter"""
    defaultValue = 60


_XcmGenTrapViewNotifyTraining_Object = MibTableColumn
xcmGenTrapViewNotifyTraining = _XcmGenTrapViewNotifyTraining_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1, 4),
    _XcmGenTrapViewNotifyTraining_Type()
)
xcmGenTrapViewNotifyTraining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapViewNotifyTraining.setStatus("current")
_XcmGenMessageMap_ObjectIdentity = ObjectIdentity
xcmGenMessageMap = _XcmGenMessageMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15)
)
_XcmGenMessageMapTable_Object = MibTable
xcmGenMessageMapTable = _XcmGenMessageMapTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15, 2)
)
if mibBuilder.loadTexts:
    xcmGenMessageMapTable.setStatus("current")
_XcmGenMessageMapEntry_Object = MibTableRow
xcmGenMessageMapEntry = _XcmGenMessageMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15, 2, 1)
)
xcmGenMessageMapEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenMessageMapStringIndexOID"),
)
if mibBuilder.loadTexts:
    xcmGenMessageMapEntry.setStatus("current")
_XcmGenMessageMapStringIndexOID_Type = ObjectIdentifier
_XcmGenMessageMapStringIndexOID_Object = MibTableColumn
xcmGenMessageMapStringIndexOID = _XcmGenMessageMapStringIndexOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15, 2, 1, 1),
    _XcmGenMessageMapStringIndexOID_Type()
)
xcmGenMessageMapStringIndexOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenMessageMapStringIndexOID.setStatus("current")
_XcmGenMessageMapStringLabel_Type = XcmGenMessageMapStringLabel
_XcmGenMessageMapStringLabel_Object = MibTableColumn
xcmGenMessageMapStringLabel = _XcmGenMessageMapStringLabel_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15, 2, 1, 2),
    _XcmGenMessageMapStringLabel_Type()
)
xcmGenMessageMapStringLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenMessageMapStringLabel.setStatus("current")
_XcmGenMessageText_ObjectIdentity = ObjectIdentity
xcmGenMessageText = _XcmGenMessageText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16)
)
_XcmGenMessageTextTable_Object = MibTable
xcmGenMessageTextTable = _XcmGenMessageTextTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2)
)
if mibBuilder.loadTexts:
    xcmGenMessageTextTable.setStatus("current")
_XcmGenMessageTextEntry_Object = MibTableRow
xcmGenMessageTextEntry = _XcmGenMessageTextEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2, 1)
)
xcmGenMessageTextEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenMessageTextStringIndexOID"),
    (0, "XEROX-GENERAL-MIB", "xcmGenMessageTextTargetLocale"),
)
if mibBuilder.loadTexts:
    xcmGenMessageTextEntry.setStatus("current")
_XcmGenMessageTextStringIndexOID_Type = ObjectIdentifier
_XcmGenMessageTextStringIndexOID_Object = MibTableColumn
xcmGenMessageTextStringIndexOID = _XcmGenMessageTextStringIndexOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2, 1, 1),
    _XcmGenMessageTextStringIndexOID_Type()
)
xcmGenMessageTextStringIndexOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenMessageTextStringIndexOID.setStatus("current")
_XcmGenMessageTextTargetLocale_Type = Ordinal32
_XcmGenMessageTextTargetLocale_Object = MibTableColumn
xcmGenMessageTextTargetLocale = _XcmGenMessageTextTargetLocale_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2, 1, 2),
    _XcmGenMessageTextTargetLocale_Type()
)
xcmGenMessageTextTargetLocale.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenMessageTextTargetLocale.setStatus("current")


class _XcmGenMessageTextTargetString_Type(XcmNamedLocaleUtf8String):
    """Custom type xcmGenMessageTextTargetString based on XcmNamedLocaleUtf8String"""
    subtypeSpec = XcmNamedLocaleUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenMessageTextTargetString_Type.__name__ = "XcmNamedLocaleUtf8String"
_XcmGenMessageTextTargetString_Object = MibTableColumn
xcmGenMessageTextTargetString = _XcmGenMessageTextTargetString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2, 1, 3),
    _XcmGenMessageTextTargetString_Type()
)
xcmGenMessageTextTargetString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenMessageTextTargetString.setStatus("current")
_XcmGenNotifyRule_ObjectIdentity = ObjectIdentity
xcmGenNotifyRule = _XcmGenNotifyRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17)
)
_XcmGenNotifyRuleSimple_ObjectIdentity = ObjectIdentity
xcmGenNotifyRuleSimple = _XcmGenNotifyRuleSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 1)
)
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSimple.setStatus("current")
_XcmGenNotifyRuleEntryCount_Type = Counter32
_XcmGenNotifyRuleEntryCount_Object = MibScalar
xcmGenNotifyRuleEntryCount = _XcmGenNotifyRuleEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 1, 1),
    _XcmGenNotifyRuleEntryCount_Type()
)
xcmGenNotifyRuleEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEntryCount.setStatus("current")


class _XcmGenNotifyRuleSupportMaxCount_Type(Cardinal32):
    """Custom type xcmGenNotifyRuleSupportMaxCount based on Cardinal32"""
    defaultValue = 0


_XcmGenNotifyRuleSupportMaxCount_Object = MibScalar
xcmGenNotifyRuleSupportMaxCount = _XcmGenNotifyRuleSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 1, 2),
    _XcmGenNotifyRuleSupportMaxCount_Type()
)
xcmGenNotifyRuleSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSupportMaxCount.setStatus("current")
_XcmGenNotifyRuleTable_Object = MibTable
xcmGenNotifyRuleTable = _XcmGenNotifyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2)
)
if mibBuilder.loadTexts:
    xcmGenNotifyRuleTable.setStatus("current")
_XcmGenNotifyRuleEntry_Object = MibTableRow
xcmGenNotifyRuleEntry = _XcmGenNotifyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1)
)
xcmGenNotifyRuleEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenNotifyRuleIndex"),
)
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEntry.setStatus("current")
_XcmGenNotifyRuleIndex_Type = Ordinal32
_XcmGenNotifyRuleIndex_Object = MibTableColumn
xcmGenNotifyRuleIndex = _XcmGenNotifyRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 1),
    _XcmGenNotifyRuleIndex_Type()
)
xcmGenNotifyRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleIndex.setStatus("current")
_XcmGenNotifyRuleRowStatus_Type = RowStatus
_XcmGenNotifyRuleRowStatus_Object = MibTableColumn
xcmGenNotifyRuleRowStatus = _XcmGenNotifyRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 2),
    _XcmGenNotifyRuleRowStatus_Type()
)
xcmGenNotifyRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRowStatus.setStatus("current")


class _XcmGenNotifyRuleRowPersistence_Type(XcmGenRowPersistence):
    """Custom type xcmGenNotifyRuleRowPersistence based on XcmGenRowPersistence"""


_XcmGenNotifyRuleRowPersistence_Object = MibTableColumn
xcmGenNotifyRuleRowPersistence = _XcmGenNotifyRuleRowPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 3),
    _XcmGenNotifyRuleRowPersistence_Type()
)
xcmGenNotifyRuleRowPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRowPersistence.setStatus("current")


class _XcmGenNotifyRuleRecipientURI_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmGenNotifyRuleRecipientURI based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenNotifyRuleRecipientURI_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmGenNotifyRuleRecipientURI_Object = MibTableColumn
xcmGenNotifyRuleRecipientURI = _XcmGenNotifyRuleRecipientURI_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 4),
    _XcmGenNotifyRuleRecipientURI_Type()
)
xcmGenNotifyRuleRecipientURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRecipientURI.setStatus("current")


class _XcmGenNotifyRuleEventNames_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmGenNotifyRuleEventNames based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenNotifyRuleEventNames_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmGenNotifyRuleEventNames_Object = MibTableColumn
xcmGenNotifyRuleEventNames = _XcmGenNotifyRuleEventNames_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 5),
    _XcmGenNotifyRuleEventNames_Type()
)
xcmGenNotifyRuleEventNames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEventNames.setStatus("current")


class _XcmGenNotifyRuleEventDelay_Type(Cardinal32):
    """Custom type xcmGenNotifyRuleEventDelay based on Cardinal32"""
    defaultValue = 0


_XcmGenNotifyRuleEventDelay_Object = MibTableColumn
xcmGenNotifyRuleEventDelay = _XcmGenNotifyRuleEventDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 6),
    _XcmGenNotifyRuleEventDelay_Type()
)
xcmGenNotifyRuleEventDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEventDelay.setStatus("current")


class _XcmGenNotifyRuleSeverityFilter_Type(XcmGenNotifySeverityFilter):
    """Custom type xcmGenNotifyRuleSeverityFilter based on XcmGenNotifySeverityFilter"""
    defaultValue = 15


_XcmGenNotifyRuleSeverityFilter_Object = MibTableColumn
xcmGenNotifyRuleSeverityFilter = _XcmGenNotifyRuleSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 7),
    _XcmGenNotifyRuleSeverityFilter_Type()
)
xcmGenNotifyRuleSeverityFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSeverityFilter.setStatus("current")


class _XcmGenNotifyRuleTrainingFilter_Type(XcmGenNotifyTrainingFilter):
    """Custom type xcmGenNotifyRuleTrainingFilter based on XcmGenNotifyTrainingFilter"""
    defaultValue = 60


_XcmGenNotifyRuleTrainingFilter_Object = MibTableColumn
xcmGenNotifyRuleTrainingFilter = _XcmGenNotifyRuleTrainingFilter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 8),
    _XcmGenNotifyRuleTrainingFilter_Type()
)
xcmGenNotifyRuleTrainingFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleTrainingFilter.setStatus("current")


class _XcmGenNotifyRuleCharset_Type(IANACharset):
    """Custom type xcmGenNotifyRuleCharset based on IANACharset"""


_XcmGenNotifyRuleCharset_Object = MibTableColumn
xcmGenNotifyRuleCharset = _XcmGenNotifyRuleCharset_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 9),
    _XcmGenNotifyRuleCharset_Type()
)
xcmGenNotifyRuleCharset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleCharset.setStatus("current")


class _XcmGenNotifyRuleNaturalLanguage_Type(DisplayString):
    """Custom type xcmGenNotifyRuleNaturalLanguage based on DisplayString"""
    defaultHexValue = ""


_XcmGenNotifyRuleNaturalLanguage_Object = MibTableColumn
xcmGenNotifyRuleNaturalLanguage = _XcmGenNotifyRuleNaturalLanguage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 10),
    _XcmGenNotifyRuleNaturalLanguage_Type()
)
xcmGenNotifyRuleNaturalLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleNaturalLanguage.setStatus("current")


class _XcmGenNotifyRuleSequenceNumber_Type(Cardinal32):
    """Custom type xcmGenNotifyRuleSequenceNumber based on Cardinal32"""
    defaultValue = 0


_XcmGenNotifyRuleSequenceNumber_Object = MibTableColumn
xcmGenNotifyRuleSequenceNumber = _XcmGenNotifyRuleSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 11),
    _XcmGenNotifyRuleSequenceNumber_Type()
)
xcmGenNotifyRuleSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSequenceNumber.setStatus("current")
_XcmGenNotifyDetail_ObjectIdentity = ObjectIdentity
xcmGenNotifyDetail = _XcmGenNotifyDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18)
)
_XcmGenNotifyDetailSimple_ObjectIdentity = ObjectIdentity
xcmGenNotifyDetailSimple = _XcmGenNotifyDetailSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 1)
)
if mibBuilder.loadTexts:
    xcmGenNotifyDetailSimple.setStatus("current")
_XcmGenNotifyDetailEntryCount_Type = Counter32
_XcmGenNotifyDetailEntryCount_Object = MibScalar
xcmGenNotifyDetailEntryCount = _XcmGenNotifyDetailEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 1, 1),
    _XcmGenNotifyDetailEntryCount_Type()
)
xcmGenNotifyDetailEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailEntryCount.setStatus("current")


class _XcmGenNotifyDetailSupportMax_Type(Cardinal32):
    """Custom type xcmGenNotifyDetailSupportMax based on Cardinal32"""
    defaultValue = 0


_XcmGenNotifyDetailSupportMax_Object = MibScalar
xcmGenNotifyDetailSupportMax = _XcmGenNotifyDetailSupportMax_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 1, 2),
    _XcmGenNotifyDetailSupportMax_Type()
)
xcmGenNotifyDetailSupportMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailSupportMax.setStatus("current")
_XcmGenNotifyDetailTable_Object = MibTable
xcmGenNotifyDetailTable = _XcmGenNotifyDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2)
)
if mibBuilder.loadTexts:
    xcmGenNotifyDetailTable.setStatus("current")
_XcmGenNotifyDetailEntry_Object = MibTableRow
xcmGenNotifyDetailEntry = _XcmGenNotifyDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1)
)
xcmGenNotifyDetailEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenNotifyRuleIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenNotifyDetailType"),
    (0, "XEROX-GENERAL-MIB", "xcmGenNotifyDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmGenNotifyDetailEntry.setStatus("current")
_XcmGenNotifyDetailType_Type = XcmGenNotifyDetailType
_XcmGenNotifyDetailType_Object = MibTableColumn
xcmGenNotifyDetailType = _XcmGenNotifyDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1, 1),
    _XcmGenNotifyDetailType_Type()
)
xcmGenNotifyDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailType.setStatus("current")
_XcmGenNotifyDetailIndex_Type = Ordinal32
_XcmGenNotifyDetailIndex_Object = MibTableColumn
xcmGenNotifyDetailIndex = _XcmGenNotifyDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1, 2),
    _XcmGenNotifyDetailIndex_Type()
)
xcmGenNotifyDetailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailIndex.setStatus("current")
_XcmGenNotifyDetailRowStatus_Type = RowStatus
_XcmGenNotifyDetailRowStatus_Object = MibTableColumn
xcmGenNotifyDetailRowStatus = _XcmGenNotifyDetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1, 3),
    _XcmGenNotifyDetailRowStatus_Type()
)
xcmGenNotifyDetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailRowStatus.setStatus("current")


class _XcmGenNotifyDetailString_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmGenNotifyDetailString based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenNotifyDetailString_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmGenNotifyDetailString_Object = MibTableColumn
xcmGenNotifyDetailString = _XcmGenNotifyDetailString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1, 4),
    _XcmGenNotifyDetailString_Type()
)
xcmGenNotifyDetailString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailString.setStatus("current")

# Managed Objects groups

xcmGenBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 1)
)
xcmGenBaseGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenBaseRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSystemHrDeviceIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseGroupSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseGroupCreateSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseGroupUpdateSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseClientDataMaxSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseOptionSyntaxSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseReconfStateSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPDomainSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPTrapSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPVersionSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPReadCommunity"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPWriteCommunity"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPTrapCommunity"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseGroupWalkHidden"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseNotifySchemeSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseNotifySeveritySupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseNotifyTrainingSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSystem1284DeviceId"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPWarningTrapSupport"))
)
if mibBuilder.loadTexts:
    xcmGenBaseGroup.setStatus("current")

xcmGenCurrentLocalizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 3)
)
xcmGenCurrentLocalizationGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenCurrentLocalizationIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenCurrLocalizationRowStatus"))
)
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationGroup.setStatus("current")

xcmGenLocalizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 4)
)
xcmGenLocalizationGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenLocalizationRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationASCIIName"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationName"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationLanguage"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationCountry"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationCharSet"))
)
if mibBuilder.loadTexts:
    xcmGenLocalizationGroup.setStatus("current")

xcmGenCodeIndexedStringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 5)
)
xcmGenCodeIndexedStringGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenCodeIndexedStringRowStat"),
        ("XEROX-GENERAL-MIB", "xcmGenCodeIndexedStringData"))
)
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringGroup.setStatus("current")

xcmGenCodedCharSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 6)
)
xcmGenCodedCharSetGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenCodedCharSetRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenCodedCharSetASCIIName"))
)
if mibBuilder.loadTexts:
    xcmGenCodedCharSetGroup.setStatus("current")

xcmGenFixedLocalizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 7)
)
xcmGenFixedLocalizationGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenFixedLocalizationIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenFixedLocalizationRowStat"))
)
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationGroup.setStatus("current")

xcmGenLockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 8)
)
xcmGenLockGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenLockSupportMaxTimer"),
        ("XEROX-GENERAL-MIB", "xcmGenLockCurrentMaxTimer"),
        ("XEROX-GENERAL-MIB", "xcmGenLockCurrentLockCount"),
        ("XEROX-GENERAL-MIB", "xcmGenLockHighestLockIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenLockSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenLockRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenLockOwnerString"),
        ("XEROX-GENERAL-MIB", "xcmGenLockOwnerSubtree"),
        ("XEROX-GENERAL-MIB", "xcmGenLockOwnerTimer"))
)
if mibBuilder.loadTexts:
    xcmGenLockGroup.setStatus("current")

xcmGenReconfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 9)
)
xcmGenReconfGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenReconfActivations"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfOptionIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfOptionState"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfErrorIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfErrorStatus"))
)
if mibBuilder.loadTexts:
    xcmGenReconfGroup.setStatus("current")

xcmGenOptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 10)
)
xcmGenOptionGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenOptionEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionTypeOID"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueSyntax"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueInteger"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueOID"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueString"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueLocalization"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueCodedCharSet"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionNextIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionPreviousIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionFamilyIndex"))
)
if mibBuilder.loadTexts:
    xcmGenOptionGroup.setStatus("current")

xcmGenClientDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 11)
)
xcmGenClientDataGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenClientDataEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataLastIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataRequestDate"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataRequestID"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataProductID"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataLength"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataString"))
)
if mibBuilder.loadTexts:
    xcmGenClientDataGroup.setStatus("current")

xcmGenTrapClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 13)
)
xcmGenTrapClientGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenTrapClientEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientRowPersistence"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientSNMPVersion"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientSNMPCommunity"))
)
if mibBuilder.loadTexts:
    xcmGenTrapClientGroup.setStatus("current")

xcmGenTrapViewGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 14)
)
xcmGenTrapViewGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenTrapViewEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapViewSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapViewRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapViewNotifySeverity"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapViewNotifyTraining"))
)
if mibBuilder.loadTexts:
    xcmGenTrapViewGroup.setStatus("current")

xcmGenMessageMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 15)
)
xcmGenMessageMapGroup.setObjects(
    ("XEROX-GENERAL-MIB", "xcmGenMessageMapStringLabel")
)
if mibBuilder.loadTexts:
    xcmGenMessageMapGroup.setStatus("current")

xcmGenMessageTextGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 16)
)
xcmGenMessageTextGroup.setObjects(
    ("XEROX-GENERAL-MIB", "xcmGenMessageTextTargetString")
)
if mibBuilder.loadTexts:
    xcmGenMessageTextGroup.setStatus("current")

xcmGenNotifyRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 17)
)
xcmGenNotifyRuleGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenNotifyRuleEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleRowPersistence"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleRecipientURI"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleEventNames"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleEventDelay"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleSeverityFilter"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleTrainingFilter"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleCharset"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleNaturalLanguage"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleSequenceNumber"))
)
if mibBuilder.loadTexts:
    xcmGenNotifyRuleGroup.setStatus("current")

xcmGenNotifyDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 18)
)
xcmGenNotifyDetailGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenNotifyDetailEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyDetailSupportMax"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyDetailRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyDetailString"))
)
if mibBuilder.loadTexts:
    xcmGenNotifyDetailGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xcmGeneralMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 3)
)
if mibBuilder.loadTexts:
    xcmGeneralMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-GENERAL-MIB",
    **{"xcmGenZeroDummy": xcmGenZeroDummy,
       "xcmGeneralMIB": xcmGeneralMIB,
       "xcmGenBase": xcmGenBase,
       "xcmGenBaseTable": xcmGenBaseTable,
       "xcmGenBaseEntry": xcmGenBaseEntry,
       "xcmGenBaseIndex": xcmGenBaseIndex,
       "xcmGenBaseRowStatus": xcmGenBaseRowStatus,
       "xcmGenBaseSystemHrDeviceIndex": xcmGenBaseSystemHrDeviceIndex,
       "xcmGenBaseGroupSupport": xcmGenBaseGroupSupport,
       "xcmGenBaseGroupCreateSupport": xcmGenBaseGroupCreateSupport,
       "xcmGenBaseGroupUpdateSupport": xcmGenBaseGroupUpdateSupport,
       "xcmGenBaseClientDataMaxSupport": xcmGenBaseClientDataMaxSupport,
       "xcmGenBaseOptionSyntaxSupport": xcmGenBaseOptionSyntaxSupport,
       "xcmGenBaseReconfStateSupport": xcmGenBaseReconfStateSupport,
       "xcmGenBaseSNMPDomainSupport": xcmGenBaseSNMPDomainSupport,
       "xcmGenBaseSNMPTrapSupport": xcmGenBaseSNMPTrapSupport,
       "xcmGenBaseSNMPVersionSupport": xcmGenBaseSNMPVersionSupport,
       "xcmGenBaseSNMPReadCommunity": xcmGenBaseSNMPReadCommunity,
       "xcmGenBaseSNMPWriteCommunity": xcmGenBaseSNMPWriteCommunity,
       "xcmGenBaseSNMPTrapCommunity": xcmGenBaseSNMPTrapCommunity,
       "xcmGenBaseGroupWalkHidden": xcmGenBaseGroupWalkHidden,
       "xcmGenBaseNotifySchemeSupport": xcmGenBaseNotifySchemeSupport,
       "xcmGenBaseNotifySeveritySupport": xcmGenBaseNotifySeveritySupport,
       "xcmGenBaseNotifyTrainingSupport": xcmGenBaseNotifyTrainingSupport,
       "xcmGenBaseSystem1284DeviceId": xcmGenBaseSystem1284DeviceId,
       "xcmGenBaseSNMPWarningTrapSupport": xcmGenBaseSNMPWarningTrapSupport,
       "xcmGeneralMIBConformance": xcmGeneralMIBConformance,
       "xcmGeneralMIBGroups": xcmGeneralMIBGroups,
       "xcmGenBaseGroup": xcmGenBaseGroup,
       "xcmGenCurrentLocalizationGroup": xcmGenCurrentLocalizationGroup,
       "xcmGenLocalizationGroup": xcmGenLocalizationGroup,
       "xcmGenCodeIndexedStringGroup": xcmGenCodeIndexedStringGroup,
       "xcmGenCodedCharSetGroup": xcmGenCodedCharSetGroup,
       "xcmGenFixedLocalizationGroup": xcmGenFixedLocalizationGroup,
       "xcmGenLockGroup": xcmGenLockGroup,
       "xcmGenReconfGroup": xcmGenReconfGroup,
       "xcmGenOptionGroup": xcmGenOptionGroup,
       "xcmGenClientDataGroup": xcmGenClientDataGroup,
       "xcmGenTrapClientGroup": xcmGenTrapClientGroup,
       "xcmGenTrapViewGroup": xcmGenTrapViewGroup,
       "xcmGenMessageMapGroup": xcmGenMessageMapGroup,
       "xcmGenMessageTextGroup": xcmGenMessageTextGroup,
       "xcmGenNotifyRuleGroup": xcmGenNotifyRuleGroup,
       "xcmGenNotifyDetailGroup": xcmGenNotifyDetailGroup,
       "xcmGeneralMIBCompliance": xcmGeneralMIBCompliance,
       "xcmGenCurrentLocalization": xcmGenCurrentLocalization,
       "xcmGenCurrentLocalizationTable": xcmGenCurrentLocalizationTable,
       "xcmGenCurrentLocalizationEntry": xcmGenCurrentLocalizationEntry,
       "xcmGenCurrentLocalizationIndex": xcmGenCurrentLocalizationIndex,
       "xcmGenCurrLocalizationRowStatus": xcmGenCurrLocalizationRowStatus,
       "xcmGenLocalization": xcmGenLocalization,
       "xcmGenLocalizationTable": xcmGenLocalizationTable,
       "xcmGenLocalizationEntry": xcmGenLocalizationEntry,
       "xcmGenLocalizationIndex": xcmGenLocalizationIndex,
       "xcmGenLocalizationRowStatus": xcmGenLocalizationRowStatus,
       "xcmGenLocalizationASCIIName": xcmGenLocalizationASCIIName,
       "xcmGenLocalizationName": xcmGenLocalizationName,
       "xcmGenLocalizationLanguage": xcmGenLocalizationLanguage,
       "xcmGenLocalizationCountry": xcmGenLocalizationCountry,
       "xcmGenLocalizationCharSet": xcmGenLocalizationCharSet,
       "xcmGenCodeIndexedString": xcmGenCodeIndexedString,
       "xcmGenCodeIndexedStringTable": xcmGenCodeIndexedStringTable,
       "xcmGenCodeIndexedStringEntry": xcmGenCodeIndexedStringEntry,
       "xcmGenCodeIndexedStringIndex": xcmGenCodeIndexedStringIndex,
       "xcmGenCodeIndexedStringCharSet": xcmGenCodeIndexedStringCharSet,
       "xcmGenCodeIndexedStringRowStat": xcmGenCodeIndexedStringRowStat,
       "xcmGenCodeIndexedStringData": xcmGenCodeIndexedStringData,
       "xcmGenCodedCharSet": xcmGenCodedCharSet,
       "xcmGenCodedCharSetTable": xcmGenCodedCharSetTable,
       "xcmGenCodedCharSetEntry": xcmGenCodedCharSetEntry,
       "xcmGenCodedCharSetCharSet": xcmGenCodedCharSetCharSet,
       "xcmGenCodedCharSetRowStatus": xcmGenCodedCharSetRowStatus,
       "xcmGenCodedCharSetASCIIName": xcmGenCodedCharSetASCIIName,
       "xcmGenFixedLocalization": xcmGenFixedLocalization,
       "xcmGenFixedLocalizationTable": xcmGenFixedLocalizationTable,
       "xcmGenFixedLocalizationEntry": xcmGenFixedLocalizationEntry,
       "xcmGenFixedLocalizationIndex": xcmGenFixedLocalizationIndex,
       "xcmGenFixedLocalizationRowStat": xcmGenFixedLocalizationRowStat,
       "xcmGenLock": xcmGenLock,
       "xcmGenLockSimple": xcmGenLockSimple,
       "xcmGenLockSupportMaxTimer": xcmGenLockSupportMaxTimer,
       "xcmGenLockCurrentMaxTimer": xcmGenLockCurrentMaxTimer,
       "xcmGenLockCurrentLockCount": xcmGenLockCurrentLockCount,
       "xcmGenLockHighestLockIndex": xcmGenLockHighestLockIndex,
       "xcmGenLockSupportMaxCount": xcmGenLockSupportMaxCount,
       "xcmGenLockTable": xcmGenLockTable,
       "xcmGenLockEntry": xcmGenLockEntry,
       "xcmGenLockIndex": xcmGenLockIndex,
       "xcmGenLockRowStatus": xcmGenLockRowStatus,
       "xcmGenLockOwnerString": xcmGenLockOwnerString,
       "xcmGenLockOwnerSubtree": xcmGenLockOwnerSubtree,
       "xcmGenLockOwnerTimer": xcmGenLockOwnerTimer,
       "xcmGenReconf": xcmGenReconf,
       "xcmGenReconfSimple": xcmGenReconfSimple,
       "xcmGenReconfActivations": xcmGenReconfActivations,
       "xcmGenReconfEntryCount": xcmGenReconfEntryCount,
       "xcmGenReconfSupportMaxCount": xcmGenReconfSupportMaxCount,
       "xcmGenReconfTable": xcmGenReconfTable,
       "xcmGenReconfEntry": xcmGenReconfEntry,
       "xcmGenReconfIndex": xcmGenReconfIndex,
       "xcmGenReconfRowStatus": xcmGenReconfRowStatus,
       "xcmGenReconfOptionIndex": xcmGenReconfOptionIndex,
       "xcmGenReconfOptionState": xcmGenReconfOptionState,
       "xcmGenReconfErrorIndex": xcmGenReconfErrorIndex,
       "xcmGenReconfErrorStatus": xcmGenReconfErrorStatus,
       "xcmGenOption": xcmGenOption,
       "xcmGenOptionSimple": xcmGenOptionSimple,
       "xcmGenOptionOperation": xcmGenOptionOperation,
       "xcmGenOptionOperationInsert": xcmGenOptionOperationInsert,
       "xcmGenOptionOperationDelete": xcmGenOptionOperationDelete,
       "xcmGenOptionOperationReplace": xcmGenOptionOperationReplace,
       "xcmGenOptionEntryCount": xcmGenOptionEntryCount,
       "xcmGenOptionSupportMaxCount": xcmGenOptionSupportMaxCount,
       "xcmGenOptionTable": xcmGenOptionTable,
       "xcmGenOptionEntry": xcmGenOptionEntry,
       "xcmGenOptionIndex": xcmGenOptionIndex,
       "xcmGenOptionRowStatus": xcmGenOptionRowStatus,
       "xcmGenOptionTypeOID": xcmGenOptionTypeOID,
       "xcmGenOptionValueSyntax": xcmGenOptionValueSyntax,
       "xcmGenOptionValueInteger": xcmGenOptionValueInteger,
       "xcmGenOptionValueOID": xcmGenOptionValueOID,
       "xcmGenOptionValueString": xcmGenOptionValueString,
       "xcmGenOptionValueLocalization": xcmGenOptionValueLocalization,
       "xcmGenOptionValueCodedCharSet": xcmGenOptionValueCodedCharSet,
       "xcmGenOptionNextIndex": xcmGenOptionNextIndex,
       "xcmGenOptionPreviousIndex": xcmGenOptionPreviousIndex,
       "xcmGenOptionFamilyIndex": xcmGenOptionFamilyIndex,
       "xcmGenClientData": xcmGenClientData,
       "xcmGenClientDataSimple": xcmGenClientDataSimple,
       "xcmGenClientDataEntryCount": xcmGenClientDataEntryCount,
       "xcmGenClientDataLastIndex": xcmGenClientDataLastIndex,
       "xcmGenClientDataSupportMaxCount": xcmGenClientDataSupportMaxCount,
       "xcmGenClientDataTable": xcmGenClientDataTable,
       "xcmGenClientDataEntry": xcmGenClientDataEntry,
       "xcmGenClientDataIndex": xcmGenClientDataIndex,
       "xcmGenClientDataRowStatus": xcmGenClientDataRowStatus,
       "xcmGenClientDataRequestDate": xcmGenClientDataRequestDate,
       "xcmGenClientDataRequestID": xcmGenClientDataRequestID,
       "xcmGenClientDataProductID": xcmGenClientDataProductID,
       "xcmGenClientDataLength": xcmGenClientDataLength,
       "xcmGenClientDataString": xcmGenClientDataString,
       "xcmGenTrapClient": xcmGenTrapClient,
       "xcmGenTrapClientSimple": xcmGenTrapClientSimple,
       "xcmGenTrapClientEntryCount": xcmGenTrapClientEntryCount,
       "xcmGenTrapClientSupportMaxCount": xcmGenTrapClientSupportMaxCount,
       "xcmGenTrapClientTable": xcmGenTrapClientTable,
       "xcmGenTrapClientEntry": xcmGenTrapClientEntry,
       "xcmGenTrapClientSNMPDomain": xcmGenTrapClientSNMPDomain,
       "xcmGenTrapClientSNMPAddress": xcmGenTrapClientSNMPAddress,
       "xcmGenTrapClientRowStatus": xcmGenTrapClientRowStatus,
       "xcmGenTrapClientIndex": xcmGenTrapClientIndex,
       "xcmGenTrapClientRowPersistence": xcmGenTrapClientRowPersistence,
       "xcmGenTrapClientSNMPVersion": xcmGenTrapClientSNMPVersion,
       "xcmGenTrapClientSNMPCommunity": xcmGenTrapClientSNMPCommunity,
       "xcmGenTrapView": xcmGenTrapView,
       "xcmGenTrapViewSimple": xcmGenTrapViewSimple,
       "xcmGenTrapViewEntryCount": xcmGenTrapViewEntryCount,
       "xcmGenTrapViewSupportMaxCount": xcmGenTrapViewSupportMaxCount,
       "xcmGenTrapViewTable": xcmGenTrapViewTable,
       "xcmGenTrapViewEntry": xcmGenTrapViewEntry,
       "xcmGenTrapViewObjectSubtree": xcmGenTrapViewObjectSubtree,
       "xcmGenTrapViewRowStatus": xcmGenTrapViewRowStatus,
       "xcmGenTrapViewNotifySeverity": xcmGenTrapViewNotifySeverity,
       "xcmGenTrapViewNotifyTraining": xcmGenTrapViewNotifyTraining,
       "xcmGenMessageMap": xcmGenMessageMap,
       "xcmGenMessageMapTable": xcmGenMessageMapTable,
       "xcmGenMessageMapEntry": xcmGenMessageMapEntry,
       "xcmGenMessageMapStringIndexOID": xcmGenMessageMapStringIndexOID,
       "xcmGenMessageMapStringLabel": xcmGenMessageMapStringLabel,
       "xcmGenMessageText": xcmGenMessageText,
       "xcmGenMessageTextTable": xcmGenMessageTextTable,
       "xcmGenMessageTextEntry": xcmGenMessageTextEntry,
       "xcmGenMessageTextStringIndexOID": xcmGenMessageTextStringIndexOID,
       "xcmGenMessageTextTargetLocale": xcmGenMessageTextTargetLocale,
       "xcmGenMessageTextTargetString": xcmGenMessageTextTargetString,
       "xcmGenNotifyRule": xcmGenNotifyRule,
       "xcmGenNotifyRuleSimple": xcmGenNotifyRuleSimple,
       "xcmGenNotifyRuleEntryCount": xcmGenNotifyRuleEntryCount,
       "xcmGenNotifyRuleSupportMaxCount": xcmGenNotifyRuleSupportMaxCount,
       "xcmGenNotifyRuleTable": xcmGenNotifyRuleTable,
       "xcmGenNotifyRuleEntry": xcmGenNotifyRuleEntry,
       "xcmGenNotifyRuleIndex": xcmGenNotifyRuleIndex,
       "xcmGenNotifyRuleRowStatus": xcmGenNotifyRuleRowStatus,
       "xcmGenNotifyRuleRowPersistence": xcmGenNotifyRuleRowPersistence,
       "xcmGenNotifyRuleRecipientURI": xcmGenNotifyRuleRecipientURI,
       "xcmGenNotifyRuleEventNames": xcmGenNotifyRuleEventNames,
       "xcmGenNotifyRuleEventDelay": xcmGenNotifyRuleEventDelay,
       "xcmGenNotifyRuleSeverityFilter": xcmGenNotifyRuleSeverityFilter,
       "xcmGenNotifyRuleTrainingFilter": xcmGenNotifyRuleTrainingFilter,
       "xcmGenNotifyRuleCharset": xcmGenNotifyRuleCharset,
       "xcmGenNotifyRuleNaturalLanguage": xcmGenNotifyRuleNaturalLanguage,
       "xcmGenNotifyRuleSequenceNumber": xcmGenNotifyRuleSequenceNumber,
       "xcmGenNotifyDetail": xcmGenNotifyDetail,
       "xcmGenNotifyDetailSimple": xcmGenNotifyDetailSimple,
       "xcmGenNotifyDetailEntryCount": xcmGenNotifyDetailEntryCount,
       "xcmGenNotifyDetailSupportMax": xcmGenNotifyDetailSupportMax,
       "xcmGenNotifyDetailTable": xcmGenNotifyDetailTable,
       "xcmGenNotifyDetailEntry": xcmGenNotifyDetailEntry,
       "xcmGenNotifyDetailType": xcmGenNotifyDetailType,
       "xcmGenNotifyDetailIndex": xcmGenNotifyDetailIndex,
       "xcmGenNotifyDetailRowStatus": xcmGenNotifyDetailRowStatus,
       "xcmGenNotifyDetailString": xcmGenNotifyDetailString}
)
