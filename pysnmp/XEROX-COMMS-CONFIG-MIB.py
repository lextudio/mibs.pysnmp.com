# SNMP MIB module (XEROX-COMMS-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-COMMS-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:14 2024
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

(XcmCommsConfigGroupSupport,
 XcmCommsDirAttributeType,
 XcmCommsDirRecordType) = mibBuilder.importSymbols(
    "XEROX-COMMS-CONFIG-TC",
    "XcmCommsConfigGroupSupport",
    "XcmCommsDirAttributeType",
    "XcmCommsDirRecordType")

(XcmCommsStackExtProtocol,) = mibBuilder.importSymbols(
    "XEROX-COMMS-ENGINE-TC",
    "XcmCommsStackExtProtocol")

(Cardinal32,
 Ordinal32,
 XcmFixedLocaleUtf8String,
 XcmGenOptionValueSyntax,
 zeroDotZero) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Cardinal32",
    "Ordinal32",
    "XcmFixedLocaleUtf8String",
    "XcmGenOptionValueSyntax",
    "zeroDotZero")


# MODULE-IDENTITY

xcmCommsConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmCommsConfigZeroDummy_ObjectIdentity = ObjectIdentity
xcmCommsConfigZeroDummy = _XcmCommsConfigZeroDummy_ObjectIdentity(
    (0, 0, 64)
)
_XcmCommsConfigMIBConformance_ObjectIdentity = ObjectIdentity
xcmCommsConfigMIBConformance = _XcmCommsConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2)
)
_XcmCommsConfigMIBGroups_ObjectIdentity = ObjectIdentity
xcmCommsConfigMIBGroups = _XcmCommsConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2)
)
_XcmCommsConfig_ObjectIdentity = ObjectIdentity
xcmCommsConfig = _XcmCommsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3)
)
_XcmCommsConfigTable_Object = MibTable
xcmCommsConfigTable = _XcmCommsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2)
)
if mibBuilder.loadTexts:
    xcmCommsConfigTable.setStatus("current")
_XcmCommsConfigEntry_Object = MibTableRow
xcmCommsConfigEntry = _XcmCommsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1)
)
xcmCommsConfigEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsConfigEntry.setStatus("current")
_XcmCommsConfigRowStatus_Type = RowStatus
_XcmCommsConfigRowStatus_Object = MibTableColumn
xcmCommsConfigRowStatus = _XcmCommsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 1),
    _XcmCommsConfigRowStatus_Type()
)
xcmCommsConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigRowStatus.setStatus("current")


class _XcmCommsConfigActiveOptionFirst_Type(Cardinal32):
    """Custom type xcmCommsConfigActiveOptionFirst based on Cardinal32"""
    defaultValue = 0


_XcmCommsConfigActiveOptionFirst_Object = MibTableColumn
xcmCommsConfigActiveOptionFirst = _XcmCommsConfigActiveOptionFirst_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 2),
    _XcmCommsConfigActiveOptionFirst_Type()
)
xcmCommsConfigActiveOptionFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigActiveOptionFirst.setStatus("current")


class _XcmCommsConfigActiveOptionLast_Type(Cardinal32):
    """Custom type xcmCommsConfigActiveOptionLast based on Cardinal32"""
    defaultValue = 0


_XcmCommsConfigActiveOptionLast_Object = MibTableColumn
xcmCommsConfigActiveOptionLast = _XcmCommsConfigActiveOptionLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 3),
    _XcmCommsConfigActiveOptionLast_Type()
)
xcmCommsConfigActiveOptionLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigActiveOptionLast.setStatus("current")


class _XcmCommsConfigGroupSupport_Type(XcmCommsConfigGroupSupport):
    """Custom type xcmCommsConfigGroupSupport based on XcmCommsConfigGroupSupport"""
    defaultValue = 1


_XcmCommsConfigGroupSupport_Object = MibTableColumn
xcmCommsConfigGroupSupport = _XcmCommsConfigGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 4),
    _XcmCommsConfigGroupSupport_Type()
)
xcmCommsConfigGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigGroupSupport.setStatus("current")


class _XcmCommsConfigCreateSupport_Type(XcmCommsConfigGroupSupport):
    """Custom type xcmCommsConfigCreateSupport based on XcmCommsConfigGroupSupport"""
    defaultValue = 0


_XcmCommsConfigCreateSupport_Object = MibTableColumn
xcmCommsConfigCreateSupport = _XcmCommsConfigCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 5),
    _XcmCommsConfigCreateSupport_Type()
)
xcmCommsConfigCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigCreateSupport.setStatus("current")


class _XcmCommsConfigUpdateSupport_Type(XcmCommsConfigGroupSupport):
    """Custom type xcmCommsConfigUpdateSupport based on XcmCommsConfigGroupSupport"""
    defaultValue = 0


_XcmCommsConfigUpdateSupport_Object = MibTableColumn
xcmCommsConfigUpdateSupport = _XcmCommsConfigUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 6),
    _XcmCommsConfigUpdateSupport_Type()
)
xcmCommsConfigUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigUpdateSupport.setStatus("current")
_XcmCommsOption_ObjectIdentity = ObjectIdentity
xcmCommsOption = _XcmCommsOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4)
)
_XcmCommsOptionTable_Object = MibTable
xcmCommsOptionTable = _XcmCommsOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2)
)
if mibBuilder.loadTexts:
    xcmCommsOptionTable.setStatus("current")
_XcmCommsOptionEntry_Object = MibTableRow
xcmCommsOptionEntry = _XcmCommsOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1)
)
xcmCommsOptionEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsOptionEntry.setStatus("current")
_XcmCommsOptionIndex_Type = Ordinal32
_XcmCommsOptionIndex_Object = MibTableColumn
xcmCommsOptionIndex = _XcmCommsOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 1),
    _XcmCommsOptionIndex_Type()
)
xcmCommsOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsOptionIndex.setStatus("current")
_XcmCommsOptionRowStatus_Type = RowStatus
_XcmCommsOptionRowStatus_Object = MibTableColumn
xcmCommsOptionRowStatus = _XcmCommsOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 2),
    _XcmCommsOptionRowStatus_Type()
)
xcmCommsOptionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionRowStatus.setStatus("current")


class _XcmCommsOptionTypeOID_Type(ObjectIdentifier):
    """Custom type xcmCommsOptionTypeOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmCommsOptionTypeOID_Object = MibTableColumn
xcmCommsOptionTypeOID = _XcmCommsOptionTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 3),
    _XcmCommsOptionTypeOID_Type()
)
xcmCommsOptionTypeOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionTypeOID.setStatus("current")


class _XcmCommsOptionValueSyntax_Type(XcmGenOptionValueSyntax):
    """Custom type xcmCommsOptionValueSyntax based on XcmGenOptionValueSyntax"""


_XcmCommsOptionValueSyntax_Object = MibTableColumn
xcmCommsOptionValueSyntax = _XcmCommsOptionValueSyntax_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 4),
    _XcmCommsOptionValueSyntax_Type()
)
xcmCommsOptionValueSyntax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueSyntax.setStatus("current")


class _XcmCommsOptionValueInteger_Type(Integer32):
    """Custom type xcmCommsOptionValueInteger based on Integer32"""
    defaultValue = 0


_XcmCommsOptionValueInteger_Object = MibTableColumn
xcmCommsOptionValueInteger = _XcmCommsOptionValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 5),
    _XcmCommsOptionValueInteger_Type()
)
xcmCommsOptionValueInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueInteger.setStatus("current")


class _XcmCommsOptionValueOID_Type(ObjectIdentifier):
    """Custom type xcmCommsOptionValueOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmCommsOptionValueOID_Object = MibTableColumn
xcmCommsOptionValueOID = _XcmCommsOptionValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 6),
    _XcmCommsOptionValueOID_Type()
)
xcmCommsOptionValueOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueOID.setStatus("current")


class _XcmCommsOptionValueString_Type(OctetString):
    """Custom type xcmCommsOptionValueString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsOptionValueString_Type.__name__ = "OctetString"
_XcmCommsOptionValueString_Object = MibTableColumn
xcmCommsOptionValueString = _XcmCommsOptionValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 7),
    _XcmCommsOptionValueString_Type()
)
xcmCommsOptionValueString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueString.setStatus("current")


class _XcmCommsOptionValueLocalization_Type(Cardinal32):
    """Custom type xcmCommsOptionValueLocalization based on Cardinal32"""
    defaultValue = 0


_XcmCommsOptionValueLocalization_Object = MibTableColumn
xcmCommsOptionValueLocalization = _XcmCommsOptionValueLocalization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 8),
    _XcmCommsOptionValueLocalization_Type()
)
xcmCommsOptionValueLocalization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueLocalization.setStatus("current")


class _XcmCommsOptionValueCodedCharSet_Type(IANACharset):
    """Custom type xcmCommsOptionValueCodedCharSet based on IANACharset"""


_XcmCommsOptionValueCodedCharSet_Object = MibTableColumn
xcmCommsOptionValueCodedCharSet = _XcmCommsOptionValueCodedCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 9),
    _XcmCommsOptionValueCodedCharSet_Type()
)
xcmCommsOptionValueCodedCharSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueCodedCharSet.setStatus("current")


class _XcmCommsOptionNextIndex_Type(Cardinal32):
    """Custom type xcmCommsOptionNextIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsOptionNextIndex_Object = MibTableColumn
xcmCommsOptionNextIndex = _XcmCommsOptionNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 10),
    _XcmCommsOptionNextIndex_Type()
)
xcmCommsOptionNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionNextIndex.setStatus("current")


class _XcmCommsOptionPreviousIndex_Type(Cardinal32):
    """Custom type xcmCommsOptionPreviousIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsOptionPreviousIndex_Object = MibTableColumn
xcmCommsOptionPreviousIndex = _XcmCommsOptionPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 11),
    _XcmCommsOptionPreviousIndex_Type()
)
xcmCommsOptionPreviousIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionPreviousIndex.setStatus("current")


class _XcmCommsOptionFamilyIndex_Type(Cardinal32):
    """Custom type xcmCommsOptionFamilyIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsOptionFamilyIndex_Object = MibTableColumn
xcmCommsOptionFamilyIndex = _XcmCommsOptionFamilyIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 12),
    _XcmCommsOptionFamilyIndex_Type()
)
xcmCommsOptionFamilyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionFamilyIndex.setStatus("current")
_XcmCommsDirRecord_ObjectIdentity = ObjectIdentity
xcmCommsDirRecord = _XcmCommsDirRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5)
)
_XcmCommsDirRecordTable_Object = MibTable
xcmCommsDirRecordTable = _XcmCommsDirRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2)
)
if mibBuilder.loadTexts:
    xcmCommsDirRecordTable.setStatus("current")
_XcmCommsDirRecordEntry_Object = MibTableRow
xcmCommsDirRecordEntry = _XcmCommsDirRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1)
)
xcmCommsDirRecordEntry.setIndexNames(
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsDirRecordEntry.setStatus("current")
_XcmCommsDirRecordType_Type = XcmCommsDirRecordType
_XcmCommsDirRecordType_Object = MibTableColumn
xcmCommsDirRecordType = _XcmCommsDirRecordType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 1),
    _XcmCommsDirRecordType_Type()
)
xcmCommsDirRecordType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsDirRecordType.setStatus("current")
_XcmCommsDirRecordIndex_Type = Ordinal32
_XcmCommsDirRecordIndex_Object = MibTableColumn
xcmCommsDirRecordIndex = _XcmCommsDirRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 2),
    _XcmCommsDirRecordIndex_Type()
)
xcmCommsDirRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsDirRecordIndex.setStatus("current")
_XcmCommsDirRecordRowStatus_Type = RowStatus
_XcmCommsDirRecordRowStatus_Object = MibTableColumn
xcmCommsDirRecordRowStatus = _XcmCommsDirRecordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 3),
    _XcmCommsDirRecordRowStatus_Type()
)
xcmCommsDirRecordRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordRowStatus.setStatus("current")


class _XcmCommsDirRecordKeyType_Type(XcmCommsDirAttributeType):
    """Custom type xcmCommsDirRecordKeyType based on XcmCommsDirAttributeType"""


_XcmCommsDirRecordKeyType_Object = MibTableColumn
xcmCommsDirRecordKeyType = _XcmCommsDirRecordKeyType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 4),
    _XcmCommsDirRecordKeyType_Type()
)
xcmCommsDirRecordKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyType.setStatus("current")


class _XcmCommsDirRecordKeyInteger_Type(Integer32):
    """Custom type xcmCommsDirRecordKeyInteger based on Integer32"""
    defaultValue = 0


_XcmCommsDirRecordKeyInteger_Object = MibTableColumn
xcmCommsDirRecordKeyInteger = _XcmCommsDirRecordKeyInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 5),
    _XcmCommsDirRecordKeyInteger_Type()
)
xcmCommsDirRecordKeyInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyInteger.setStatus("current")


class _XcmCommsDirRecordKeyString_Type(XcmFixedLocaleUtf8String):
    """Custom type xcmCommsDirRecordKeyString based on XcmFixedLocaleUtf8String"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsDirRecordKeyString_Type.__name__ = "XcmFixedLocaleUtf8String"
_XcmCommsDirRecordKeyString_Object = MibTableColumn
xcmCommsDirRecordKeyString = _XcmCommsDirRecordKeyString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 6),
    _XcmCommsDirRecordKeyString_Type()
)
xcmCommsDirRecordKeyString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyString.setStatus("current")


class _XcmCommsDirRecordParentType_Type(XcmCommsDirRecordType):
    """Custom type xcmCommsDirRecordParentType based on XcmCommsDirRecordType"""


_XcmCommsDirRecordParentType_Object = MibTableColumn
xcmCommsDirRecordParentType = _XcmCommsDirRecordParentType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 7),
    _XcmCommsDirRecordParentType_Type()
)
xcmCommsDirRecordParentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordParentType.setStatus("current")


class _XcmCommsDirRecordParentIndex_Type(Cardinal32):
    """Custom type xcmCommsDirRecordParentIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsDirRecordParentIndex_Object = MibTableColumn
xcmCommsDirRecordParentIndex = _XcmCommsDirRecordParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 8),
    _XcmCommsDirRecordParentIndex_Type()
)
xcmCommsDirRecordParentIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordParentIndex.setStatus("current")
_XcmCommsDirAttribute_ObjectIdentity = ObjectIdentity
xcmCommsDirAttribute = _XcmCommsDirAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6)
)
_XcmCommsDirAttributeTable_Object = MibTable
xcmCommsDirAttributeTable = _XcmCommsDirAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2)
)
if mibBuilder.loadTexts:
    xcmCommsDirAttributeTable.setStatus("current")
_XcmCommsDirAttributeEntry_Object = MibTableRow
xcmCommsDirAttributeEntry = _XcmCommsDirAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1)
)
xcmCommsDirAttributeEntry.setIndexNames(
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordIndex"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsDirAttributeEntry.setStatus("current")
_XcmCommsDirAttributeType_Type = XcmCommsDirAttributeType
_XcmCommsDirAttributeType_Object = MibTableColumn
xcmCommsDirAttributeType = _XcmCommsDirAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1, 1),
    _XcmCommsDirAttributeType_Type()
)
xcmCommsDirAttributeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeType.setStatus("current")
_XcmCommsDirAttributeIndex_Type = Ordinal32
_XcmCommsDirAttributeIndex_Object = MibTableColumn
xcmCommsDirAttributeIndex = _XcmCommsDirAttributeIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1, 2),
    _XcmCommsDirAttributeIndex_Type()
)
xcmCommsDirAttributeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeIndex.setStatus("current")
_XcmCommsDirAttributeRowStatus_Type = RowStatus
_XcmCommsDirAttributeRowStatus_Object = MibTableColumn
xcmCommsDirAttributeRowStatus = _XcmCommsDirAttributeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1, 3),
    _XcmCommsDirAttributeRowStatus_Type()
)
xcmCommsDirAttributeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeRowStatus.setStatus("current")


class _XcmCommsDirAttributeValue_Type(Integer32):
    """Custom type xcmCommsDirAttributeValue based on Integer32"""
    defaultValue = 0


_XcmCommsDirAttributeValue_Object = MibTableColumn
xcmCommsDirAttributeValue = _XcmCommsDirAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1, 4),
    _XcmCommsDirAttributeValue_Type()
)
xcmCommsDirAttributeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeValue.setStatus("current")
_XcmCommsDirString_ObjectIdentity = ObjectIdentity
xcmCommsDirString = _XcmCommsDirString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7)
)
_XcmCommsDirStringTable_Object = MibTable
xcmCommsDirStringTable = _XcmCommsDirStringTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7, 2)
)
if mibBuilder.loadTexts:
    xcmCommsDirStringTable.setStatus("current")
_XcmCommsDirStringEntry_Object = MibTableRow
xcmCommsDirStringEntry = _XcmCommsDirStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7, 2, 1)
)
xcmCommsDirStringEntry.setIndexNames(
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordIndex"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsDirStringEntry.setStatus("current")
_XcmCommsDirStringRowStatus_Type = RowStatus
_XcmCommsDirStringRowStatus_Object = MibTableColumn
xcmCommsDirStringRowStatus = _XcmCommsDirStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7, 2, 1, 1),
    _XcmCommsDirStringRowStatus_Type()
)
xcmCommsDirStringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirStringRowStatus.setStatus("current")


class _XcmCommsDirStringValue_Type(XcmFixedLocaleUtf8String):
    """Custom type xcmCommsDirStringValue based on XcmFixedLocaleUtf8String"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsDirStringValue_Type.__name__ = "XcmFixedLocaleUtf8String"
_XcmCommsDirStringValue_Object = MibTableColumn
xcmCommsDirStringValue = _XcmCommsDirStringValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7, 2, 1, 2),
    _XcmCommsDirStringValue_Type()
)
xcmCommsDirStringValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirStringValue.setStatus("current")
_XcmCommsProtocol_ObjectIdentity = ObjectIdentity
xcmCommsProtocol = _XcmCommsProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8)
)
_XcmCommsProtocolTable_Object = MibTable
xcmCommsProtocolTable = _XcmCommsProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8, 2)
)
if mibBuilder.loadTexts:
    xcmCommsProtocolTable.setStatus("current")
_XcmCommsProtocolEntry_Object = MibTableRow
xcmCommsProtocolEntry = _XcmCommsProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8, 2, 1)
)
xcmCommsProtocolEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsProtocolType"),
)
if mibBuilder.loadTexts:
    xcmCommsProtocolEntry.setStatus("current")
_XcmCommsProtocolType_Type = XcmCommsStackExtProtocol
_XcmCommsProtocolType_Object = MibTableColumn
xcmCommsProtocolType = _XcmCommsProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8, 2, 1, 1),
    _XcmCommsProtocolType_Type()
)
xcmCommsProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsProtocolType.setStatus("current")
_XcmCommsProtocolRowStatus_Type = RowStatus
_XcmCommsProtocolRowStatus_Object = MibTableColumn
xcmCommsProtocolRowStatus = _XcmCommsProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8, 2, 1, 2),
    _XcmCommsProtocolRowStatus_Type()
)
xcmCommsProtocolRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsProtocolRowStatus.setStatus("current")

# Managed Objects groups

xcmCommsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 3)
)
xcmCommsConfigGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigActiveOptionFirst"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigActiveOptionLast"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigGroupSupport"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigCreateSupport"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmCommsConfigGroup.setStatus("current")

xcmCommsOptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 4)
)
xcmCommsOptionGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionTypeOID"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueSyntax"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueInteger"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueOID"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueString"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueLocalization"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueCodedCharSet"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionNextIndex"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionPreviousIndex"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionFamilyIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsOptionGroup.setStatus("current")

xcmCommsDirRecordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 5)
)
xcmCommsDirRecordGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordKeyType"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordKeyInteger"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordKeyString"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordParentType"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordParentIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsDirRecordGroup.setStatus("current")

xcmCommsDirAttributeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 6)
)
xcmCommsDirAttributeGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeValue"))
)
if mibBuilder.loadTexts:
    xcmCommsDirAttributeGroup.setStatus("current")

xcmCommsDirStringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 7)
)
xcmCommsDirStringGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirStringRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirStringValue"))
)
if mibBuilder.loadTexts:
    xcmCommsDirStringGroup.setStatus("current")

xcmCommsProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 8)
)
xcmCommsProtocolGroup.setObjects(
    ("XEROX-COMMS-CONFIG-MIB", "xcmCommsProtocolRowStatus")
)
if mibBuilder.loadTexts:
    xcmCommsProtocolGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xcmCommsConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 3)
)
if mibBuilder.loadTexts:
    xcmCommsConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-COMMS-CONFIG-MIB",
    **{"xcmCommsConfigZeroDummy": xcmCommsConfigZeroDummy,
       "xcmCommsConfigMIB": xcmCommsConfigMIB,
       "xcmCommsConfigMIBConformance": xcmCommsConfigMIBConformance,
       "xcmCommsConfigMIBGroups": xcmCommsConfigMIBGroups,
       "xcmCommsConfigGroup": xcmCommsConfigGroup,
       "xcmCommsOptionGroup": xcmCommsOptionGroup,
       "xcmCommsDirRecordGroup": xcmCommsDirRecordGroup,
       "xcmCommsDirAttributeGroup": xcmCommsDirAttributeGroup,
       "xcmCommsDirStringGroup": xcmCommsDirStringGroup,
       "xcmCommsProtocolGroup": xcmCommsProtocolGroup,
       "xcmCommsConfigMIBCompliance": xcmCommsConfigMIBCompliance,
       "xcmCommsConfig": xcmCommsConfig,
       "xcmCommsConfigTable": xcmCommsConfigTable,
       "xcmCommsConfigEntry": xcmCommsConfigEntry,
       "xcmCommsConfigRowStatus": xcmCommsConfigRowStatus,
       "xcmCommsConfigActiveOptionFirst": xcmCommsConfigActiveOptionFirst,
       "xcmCommsConfigActiveOptionLast": xcmCommsConfigActiveOptionLast,
       "xcmCommsConfigGroupSupport": xcmCommsConfigGroupSupport,
       "xcmCommsConfigCreateSupport": xcmCommsConfigCreateSupport,
       "xcmCommsConfigUpdateSupport": xcmCommsConfigUpdateSupport,
       "xcmCommsOption": xcmCommsOption,
       "xcmCommsOptionTable": xcmCommsOptionTable,
       "xcmCommsOptionEntry": xcmCommsOptionEntry,
       "xcmCommsOptionIndex": xcmCommsOptionIndex,
       "xcmCommsOptionRowStatus": xcmCommsOptionRowStatus,
       "xcmCommsOptionTypeOID": xcmCommsOptionTypeOID,
       "xcmCommsOptionValueSyntax": xcmCommsOptionValueSyntax,
       "xcmCommsOptionValueInteger": xcmCommsOptionValueInteger,
       "xcmCommsOptionValueOID": xcmCommsOptionValueOID,
       "xcmCommsOptionValueString": xcmCommsOptionValueString,
       "xcmCommsOptionValueLocalization": xcmCommsOptionValueLocalization,
       "xcmCommsOptionValueCodedCharSet": xcmCommsOptionValueCodedCharSet,
       "xcmCommsOptionNextIndex": xcmCommsOptionNextIndex,
       "xcmCommsOptionPreviousIndex": xcmCommsOptionPreviousIndex,
       "xcmCommsOptionFamilyIndex": xcmCommsOptionFamilyIndex,
       "xcmCommsDirRecord": xcmCommsDirRecord,
       "xcmCommsDirRecordTable": xcmCommsDirRecordTable,
       "xcmCommsDirRecordEntry": xcmCommsDirRecordEntry,
       "xcmCommsDirRecordType": xcmCommsDirRecordType,
       "xcmCommsDirRecordIndex": xcmCommsDirRecordIndex,
       "xcmCommsDirRecordRowStatus": xcmCommsDirRecordRowStatus,
       "xcmCommsDirRecordKeyType": xcmCommsDirRecordKeyType,
       "xcmCommsDirRecordKeyInteger": xcmCommsDirRecordKeyInteger,
       "xcmCommsDirRecordKeyString": xcmCommsDirRecordKeyString,
       "xcmCommsDirRecordParentType": xcmCommsDirRecordParentType,
       "xcmCommsDirRecordParentIndex": xcmCommsDirRecordParentIndex,
       "xcmCommsDirAttribute": xcmCommsDirAttribute,
       "xcmCommsDirAttributeTable": xcmCommsDirAttributeTable,
       "xcmCommsDirAttributeEntry": xcmCommsDirAttributeEntry,
       "xcmCommsDirAttributeType": xcmCommsDirAttributeType,
       "xcmCommsDirAttributeIndex": xcmCommsDirAttributeIndex,
       "xcmCommsDirAttributeRowStatus": xcmCommsDirAttributeRowStatus,
       "xcmCommsDirAttributeValue": xcmCommsDirAttributeValue,
       "xcmCommsDirString": xcmCommsDirString,
       "xcmCommsDirStringTable": xcmCommsDirStringTable,
       "xcmCommsDirStringEntry": xcmCommsDirStringEntry,
       "xcmCommsDirStringRowStatus": xcmCommsDirStringRowStatus,
       "xcmCommsDirStringValue": xcmCommsDirStringValue,
       "xcmCommsProtocol": xcmCommsProtocol,
       "xcmCommsProtocolTable": xcmCommsProtocolTable,
       "xcmCommsProtocolEntry": xcmCommsProtocolEntry,
       "xcmCommsProtocolType": xcmCommsProtocolType,
       "xcmCommsProtocolRowStatus": xcmCommsProtocolRowStatus}
)
