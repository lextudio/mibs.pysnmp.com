# SNMP MIB module (DISMAN-SCRIPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DISMAN-SCRIPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:18 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

scriptMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 64)
)
scriptMIB.setRevisions(
        ("2001-08-21 00:00",
         "1999-02-22 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SmObjects_ObjectIdentity = ObjectIdentity
smObjects = _SmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 64, 1)
)
_SmLangTable_Object = MibTable
smLangTable = _SmLangTable_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 1)
)
if mibBuilder.loadTexts:
    smLangTable.setStatus("current")
_SmLangEntry_Object = MibTableRow
smLangEntry = _SmLangEntry_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 1, 1)
)
smLangEntry.setIndexNames(
    (0, "DISMAN-SCRIPT-MIB", "smLangIndex"),
)
if mibBuilder.loadTexts:
    smLangEntry.setStatus("current")


class _SmLangIndex_Type(Integer32):
    """Custom type smLangIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmLangIndex_Type.__name__ = "Integer32"
_SmLangIndex_Object = MibTableColumn
smLangIndex = _SmLangIndex_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 1),
    _SmLangIndex_Type()
)
smLangIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smLangIndex.setStatus("current")
_SmLangLanguage_Type = ObjectIdentifier
_SmLangLanguage_Object = MibTableColumn
smLangLanguage = _SmLangLanguage_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 2),
    _SmLangLanguage_Type()
)
smLangLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smLangLanguage.setStatus("current")


class _SmLangVersion_Type(SnmpAdminString):
    """Custom type smLangVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmLangVersion_Type.__name__ = "SnmpAdminString"
_SmLangVersion_Object = MibTableColumn
smLangVersion = _SmLangVersion_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 3),
    _SmLangVersion_Type()
)
smLangVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smLangVersion.setStatus("current")
_SmLangVendor_Type = ObjectIdentifier
_SmLangVendor_Object = MibTableColumn
smLangVendor = _SmLangVendor_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 4),
    _SmLangVendor_Type()
)
smLangVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smLangVendor.setStatus("current")


class _SmLangRevision_Type(SnmpAdminString):
    """Custom type smLangRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmLangRevision_Type.__name__ = "SnmpAdminString"
_SmLangRevision_Object = MibTableColumn
smLangRevision = _SmLangRevision_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 5),
    _SmLangRevision_Type()
)
smLangRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smLangRevision.setStatus("current")
_SmLangDescr_Type = SnmpAdminString
_SmLangDescr_Object = MibTableColumn
smLangDescr = _SmLangDescr_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 6),
    _SmLangDescr_Type()
)
smLangDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smLangDescr.setStatus("current")
_SmExtsnTable_Object = MibTable
smExtsnTable = _SmExtsnTable_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 2)
)
if mibBuilder.loadTexts:
    smExtsnTable.setStatus("current")
_SmExtsnEntry_Object = MibTableRow
smExtsnEntry = _SmExtsnEntry_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 2, 1)
)
smExtsnEntry.setIndexNames(
    (0, "DISMAN-SCRIPT-MIB", "smLangIndex"),
    (0, "DISMAN-SCRIPT-MIB", "smExtsnIndex"),
)
if mibBuilder.loadTexts:
    smExtsnEntry.setStatus("current")


class _SmExtsnIndex_Type(Integer32):
    """Custom type smExtsnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmExtsnIndex_Type.__name__ = "Integer32"
_SmExtsnIndex_Object = MibTableColumn
smExtsnIndex = _SmExtsnIndex_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 1),
    _SmExtsnIndex_Type()
)
smExtsnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smExtsnIndex.setStatus("current")
_SmExtsnExtension_Type = ObjectIdentifier
_SmExtsnExtension_Object = MibTableColumn
smExtsnExtension = _SmExtsnExtension_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 2),
    _SmExtsnExtension_Type()
)
smExtsnExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smExtsnExtension.setStatus("current")


class _SmExtsnVersion_Type(SnmpAdminString):
    """Custom type smExtsnVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmExtsnVersion_Type.__name__ = "SnmpAdminString"
_SmExtsnVersion_Object = MibTableColumn
smExtsnVersion = _SmExtsnVersion_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 3),
    _SmExtsnVersion_Type()
)
smExtsnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smExtsnVersion.setStatus("current")
_SmExtsnVendor_Type = ObjectIdentifier
_SmExtsnVendor_Object = MibTableColumn
smExtsnVendor = _SmExtsnVendor_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 4),
    _SmExtsnVendor_Type()
)
smExtsnVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smExtsnVendor.setStatus("current")


class _SmExtsnRevision_Type(SnmpAdminString):
    """Custom type smExtsnRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmExtsnRevision_Type.__name__ = "SnmpAdminString"
_SmExtsnRevision_Object = MibTableColumn
smExtsnRevision = _SmExtsnRevision_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 5),
    _SmExtsnRevision_Type()
)
smExtsnRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smExtsnRevision.setStatus("current")
_SmExtsnDescr_Type = SnmpAdminString
_SmExtsnDescr_Object = MibTableColumn
smExtsnDescr = _SmExtsnDescr_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 6),
    _SmExtsnDescr_Type()
)
smExtsnDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smExtsnDescr.setStatus("current")
_SmScriptObjects_ObjectIdentity = ObjectIdentity
smScriptObjects = _SmScriptObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 64, 1, 3)
)
_SmScriptTable_Object = MibTable
smScriptTable = _SmScriptTable_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1)
)
if mibBuilder.loadTexts:
    smScriptTable.setStatus("current")
_SmScriptEntry_Object = MibTableRow
smScriptEntry = _SmScriptEntry_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1)
)
smScriptEntry.setIndexNames(
    (0, "DISMAN-SCRIPT-MIB", "smScriptOwner"),
    (0, "DISMAN-SCRIPT-MIB", "smScriptName"),
)
if mibBuilder.loadTexts:
    smScriptEntry.setStatus("current")


class _SmScriptOwner_Type(SnmpAdminString):
    """Custom type smScriptOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmScriptOwner_Type.__name__ = "SnmpAdminString"
_SmScriptOwner_Object = MibTableColumn
smScriptOwner = _SmScriptOwner_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 1),
    _SmScriptOwner_Type()
)
smScriptOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smScriptOwner.setStatus("current")


class _SmScriptName_Type(SnmpAdminString):
    """Custom type smScriptName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SmScriptName_Type.__name__ = "SnmpAdminString"
_SmScriptName_Object = MibTableColumn
smScriptName = _SmScriptName_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 2),
    _SmScriptName_Type()
)
smScriptName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smScriptName.setStatus("current")
_SmScriptDescr_Type = SnmpAdminString
_SmScriptDescr_Object = MibTableColumn
smScriptDescr = _SmScriptDescr_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 3),
    _SmScriptDescr_Type()
)
smScriptDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smScriptDescr.setStatus("current")


class _SmScriptLanguage_Type(Integer32):
    """Custom type smScriptLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SmScriptLanguage_Type.__name__ = "Integer32"
_SmScriptLanguage_Object = MibTableColumn
smScriptLanguage = _SmScriptLanguage_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 4),
    _SmScriptLanguage_Type()
)
smScriptLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smScriptLanguage.setStatus("current")


class _SmScriptSource_Type(DisplayString):
    """Custom type smScriptSource based on DisplayString"""
    defaultHexValue = ""


_SmScriptSource_Object = MibTableColumn
smScriptSource = _SmScriptSource_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 5),
    _SmScriptSource_Type()
)
smScriptSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smScriptSource.setStatus("current")


class _SmScriptAdminStatus_Type(Integer32):
    """Custom type smScriptAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("editing", 3),
          ("enabled", 1))
    )


_SmScriptAdminStatus_Type.__name__ = "Integer32"
_SmScriptAdminStatus_Object = MibTableColumn
smScriptAdminStatus = _SmScriptAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 6),
    _SmScriptAdminStatus_Type()
)
smScriptAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smScriptAdminStatus.setStatus("current")


class _SmScriptOperStatus_Type(Integer32):
    """Custom type smScriptOperStatus based on Integer32"""
    defaultValue = 2

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
        *(("accessDenied", 7),
          ("compilationFailed", 10),
          ("compiling", 5),
          ("disabled", 2),
          ("editing", 3),
          ("enabled", 1),
          ("genericError", 14),
          ("noResourcesLeft", 11),
          ("noSuchScript", 6),
          ("protocolFailure", 13),
          ("retrieving", 4),
          ("unknownProtocol", 12),
          ("wrongLanguage", 8),
          ("wrongVersion", 9))
    )


_SmScriptOperStatus_Type.__name__ = "Integer32"
_SmScriptOperStatus_Object = MibTableColumn
smScriptOperStatus = _SmScriptOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 7),
    _SmScriptOperStatus_Type()
)
smScriptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smScriptOperStatus.setStatus("current")


class _SmScriptStorageType_Type(StorageType):
    """Custom type smScriptStorageType based on StorageType"""


_SmScriptStorageType_Object = MibTableColumn
smScriptStorageType = _SmScriptStorageType_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 8),
    _SmScriptStorageType_Type()
)
smScriptStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smScriptStorageType.setStatus("current")
_SmScriptRowStatus_Type = RowStatus
_SmScriptRowStatus_Object = MibTableColumn
smScriptRowStatus = _SmScriptRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 9),
    _SmScriptRowStatus_Type()
)
smScriptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smScriptRowStatus.setStatus("current")


class _SmScriptError_Type(SnmpAdminString):
    """Custom type smScriptError based on SnmpAdminString"""
    defaultHexValue = ""


_SmScriptError_Object = MibTableColumn
smScriptError = _SmScriptError_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 10),
    _SmScriptError_Type()
)
smScriptError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smScriptError.setStatus("current")


class _SmScriptLastChange_Type(DateAndTime):
    """Custom type smScriptLastChange based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SmScriptLastChange_Object = MibTableColumn
smScriptLastChange = _SmScriptLastChange_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 11),
    _SmScriptLastChange_Type()
)
smScriptLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smScriptLastChange.setStatus("current")
_SmCodeTable_Object = MibTable
smCodeTable = _SmCodeTable_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 2)
)
if mibBuilder.loadTexts:
    smCodeTable.setStatus("current")
_SmCodeEntry_Object = MibTableRow
smCodeEntry = _SmCodeEntry_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1)
)
smCodeEntry.setIndexNames(
    (0, "DISMAN-SCRIPT-MIB", "smScriptOwner"),
    (0, "DISMAN-SCRIPT-MIB", "smScriptName"),
    (0, "DISMAN-SCRIPT-MIB", "smCodeIndex"),
)
if mibBuilder.loadTexts:
    smCodeEntry.setStatus("current")


class _SmCodeIndex_Type(Unsigned32):
    """Custom type smCodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SmCodeIndex_Type.__name__ = "Unsigned32"
_SmCodeIndex_Object = MibTableColumn
smCodeIndex = _SmCodeIndex_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 1),
    _SmCodeIndex_Type()
)
smCodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smCodeIndex.setStatus("current")


class _SmCodeText_Type(OctetString):
    """Custom type smCodeText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_SmCodeText_Type.__name__ = "OctetString"
_SmCodeText_Object = MibTableColumn
smCodeText = _SmCodeText_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 2),
    _SmCodeText_Type()
)
smCodeText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smCodeText.setStatus("current")
_SmCodeRowStatus_Type = RowStatus
_SmCodeRowStatus_Object = MibTableColumn
smCodeRowStatus = _SmCodeRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 3),
    _SmCodeRowStatus_Type()
)
smCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smCodeRowStatus.setStatus("current")
_SmRunObjects_ObjectIdentity = ObjectIdentity
smRunObjects = _SmRunObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 64, 1, 4)
)
_SmLaunchTable_Object = MibTable
smLaunchTable = _SmLaunchTable_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1)
)
if mibBuilder.loadTexts:
    smLaunchTable.setStatus("current")
_SmLaunchEntry_Object = MibTableRow
smLaunchEntry = _SmLaunchEntry_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1)
)
smLaunchEntry.setIndexNames(
    (0, "DISMAN-SCRIPT-MIB", "smLaunchOwner"),
    (0, "DISMAN-SCRIPT-MIB", "smLaunchName"),
)
if mibBuilder.loadTexts:
    smLaunchEntry.setStatus("current")


class _SmLaunchOwner_Type(SnmpAdminString):
    """Custom type smLaunchOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmLaunchOwner_Type.__name__ = "SnmpAdminString"
_SmLaunchOwner_Object = MibTableColumn
smLaunchOwner = _SmLaunchOwner_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 1),
    _SmLaunchOwner_Type()
)
smLaunchOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smLaunchOwner.setStatus("current")


class _SmLaunchName_Type(SnmpAdminString):
    """Custom type smLaunchName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SmLaunchName_Type.__name__ = "SnmpAdminString"
_SmLaunchName_Object = MibTableColumn
smLaunchName = _SmLaunchName_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 2),
    _SmLaunchName_Type()
)
smLaunchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smLaunchName.setStatus("current")


class _SmLaunchScriptOwner_Type(SnmpAdminString):
    """Custom type smLaunchScriptOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmLaunchScriptOwner_Type.__name__ = "SnmpAdminString"
_SmLaunchScriptOwner_Object = MibTableColumn
smLaunchScriptOwner = _SmLaunchScriptOwner_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 3),
    _SmLaunchScriptOwner_Type()
)
smLaunchScriptOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchScriptOwner.setStatus("current")


class _SmLaunchScriptName_Type(SnmpAdminString):
    """Custom type smLaunchScriptName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmLaunchScriptName_Type.__name__ = "SnmpAdminString"
_SmLaunchScriptName_Object = MibTableColumn
smLaunchScriptName = _SmLaunchScriptName_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 4),
    _SmLaunchScriptName_Type()
)
smLaunchScriptName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchScriptName.setStatus("current")


class _SmLaunchArgument_Type(OctetString):
    """Custom type smLaunchArgument based on OctetString"""
    defaultHexValue = ""


_SmLaunchArgument_Object = MibTableColumn
smLaunchArgument = _SmLaunchArgument_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 5),
    _SmLaunchArgument_Type()
)
smLaunchArgument.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchArgument.setStatus("current")


class _SmLaunchMaxRunning_Type(Unsigned32):
    """Custom type smLaunchMaxRunning based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SmLaunchMaxRunning_Type.__name__ = "Unsigned32"
_SmLaunchMaxRunning_Object = MibTableColumn
smLaunchMaxRunning = _SmLaunchMaxRunning_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 6),
    _SmLaunchMaxRunning_Type()
)
smLaunchMaxRunning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchMaxRunning.setStatus("current")


class _SmLaunchMaxCompleted_Type(Unsigned32):
    """Custom type smLaunchMaxCompleted based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SmLaunchMaxCompleted_Type.__name__ = "Unsigned32"
_SmLaunchMaxCompleted_Object = MibTableColumn
smLaunchMaxCompleted = _SmLaunchMaxCompleted_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 7),
    _SmLaunchMaxCompleted_Type()
)
smLaunchMaxCompleted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchMaxCompleted.setStatus("current")


class _SmLaunchLifeTime_Type(TimeInterval):
    """Custom type smLaunchLifeTime based on TimeInterval"""
    defaultValue = 360000


_SmLaunchLifeTime_Object = MibTableColumn
smLaunchLifeTime = _SmLaunchLifeTime_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 8),
    _SmLaunchLifeTime_Type()
)
smLaunchLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    smLaunchLifeTime.setUnits("centi-seconds")


class _SmLaunchExpireTime_Type(TimeInterval):
    """Custom type smLaunchExpireTime based on TimeInterval"""
    defaultValue = 360000


_SmLaunchExpireTime_Object = MibTableColumn
smLaunchExpireTime = _SmLaunchExpireTime_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 9),
    _SmLaunchExpireTime_Type()
)
smLaunchExpireTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    smLaunchExpireTime.setUnits("centi-seconds")


class _SmLaunchStart_Type(Integer32):
    """Custom type smLaunchStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SmLaunchStart_Type.__name__ = "Integer32"
_SmLaunchStart_Object = MibTableColumn
smLaunchStart = _SmLaunchStart_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 10),
    _SmLaunchStart_Type()
)
smLaunchStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchStart.setStatus("current")


class _SmLaunchControl_Type(Integer32):
    """Custom type smLaunchControl based on Integer32"""
    defaultValue = 4

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
        *(("abort", 1),
          ("nop", 4),
          ("resume", 3),
          ("suspend", 2))
    )


_SmLaunchControl_Type.__name__ = "Integer32"
_SmLaunchControl_Object = MibTableColumn
smLaunchControl = _SmLaunchControl_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 11),
    _SmLaunchControl_Type()
)
smLaunchControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchControl.setStatus("current")


class _SmLaunchAdminStatus_Type(Integer32):
    """Custom type smLaunchAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autostart", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_SmLaunchAdminStatus_Type.__name__ = "Integer32"
_SmLaunchAdminStatus_Object = MibTableColumn
smLaunchAdminStatus = _SmLaunchAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 12),
    _SmLaunchAdminStatus_Type()
)
smLaunchAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchAdminStatus.setStatus("current")


class _SmLaunchOperStatus_Type(Integer32):
    """Custom type smLaunchOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("expired", 3))
    )


_SmLaunchOperStatus_Type.__name__ = "Integer32"
_SmLaunchOperStatus_Object = MibTableColumn
smLaunchOperStatus = _SmLaunchOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 13),
    _SmLaunchOperStatus_Type()
)
smLaunchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smLaunchOperStatus.setStatus("current")


class _SmLaunchRunIndexNext_Type(Integer32):
    """Custom type smLaunchRunIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmLaunchRunIndexNext_Type.__name__ = "Integer32"
_SmLaunchRunIndexNext_Object = MibTableColumn
smLaunchRunIndexNext = _SmLaunchRunIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 14),
    _SmLaunchRunIndexNext_Type()
)
smLaunchRunIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smLaunchRunIndexNext.setStatus("current")


class _SmLaunchStorageType_Type(StorageType):
    """Custom type smLaunchStorageType based on StorageType"""


_SmLaunchStorageType_Object = MibTableColumn
smLaunchStorageType = _SmLaunchStorageType_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 15),
    _SmLaunchStorageType_Type()
)
smLaunchStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchStorageType.setStatus("current")
_SmLaunchRowStatus_Type = RowStatus
_SmLaunchRowStatus_Object = MibTableColumn
smLaunchRowStatus = _SmLaunchRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 16),
    _SmLaunchRowStatus_Type()
)
smLaunchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchRowStatus.setStatus("current")


class _SmLaunchError_Type(SnmpAdminString):
    """Custom type smLaunchError based on SnmpAdminString"""
    defaultHexValue = ""


_SmLaunchError_Object = MibTableColumn
smLaunchError = _SmLaunchError_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 17),
    _SmLaunchError_Type()
)
smLaunchError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smLaunchError.setStatus("current")


class _SmLaunchLastChange_Type(DateAndTime):
    """Custom type smLaunchLastChange based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SmLaunchLastChange_Object = MibTableColumn
smLaunchLastChange = _SmLaunchLastChange_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 18),
    _SmLaunchLastChange_Type()
)
smLaunchLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smLaunchLastChange.setStatus("current")


class _SmLaunchRowExpireTime_Type(TimeInterval):
    """Custom type smLaunchRowExpireTime based on TimeInterval"""
    defaultValue = 2147483647


_SmLaunchRowExpireTime_Object = MibTableColumn
smLaunchRowExpireTime = _SmLaunchRowExpireTime_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 19),
    _SmLaunchRowExpireTime_Type()
)
smLaunchRowExpireTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smLaunchRowExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    smLaunchRowExpireTime.setUnits("centi-seconds")
_SmRunTable_Object = MibTable
smRunTable = _SmRunTable_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2)
)
if mibBuilder.loadTexts:
    smRunTable.setStatus("current")
_SmRunEntry_Object = MibTableRow
smRunEntry = _SmRunEntry_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1)
)
smRunEntry.setIndexNames(
    (0, "DISMAN-SCRIPT-MIB", "smLaunchOwner"),
    (0, "DISMAN-SCRIPT-MIB", "smLaunchName"),
    (0, "DISMAN-SCRIPT-MIB", "smRunIndex"),
)
if mibBuilder.loadTexts:
    smRunEntry.setStatus("current")


class _SmRunIndex_Type(Integer32):
    """Custom type smRunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmRunIndex_Type.__name__ = "Integer32"
_SmRunIndex_Object = MibTableColumn
smRunIndex = _SmRunIndex_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 1),
    _SmRunIndex_Type()
)
smRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smRunIndex.setStatus("current")


class _SmRunArgument_Type(OctetString):
    """Custom type smRunArgument based on OctetString"""
    defaultHexValue = ""


_SmRunArgument_Object = MibTableColumn
smRunArgument = _SmRunArgument_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 2),
    _SmRunArgument_Type()
)
smRunArgument.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smRunArgument.setStatus("current")


class _SmRunStartTime_Type(DateAndTime):
    """Custom type smRunStartTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SmRunStartTime_Object = MibTableColumn
smRunStartTime = _SmRunStartTime_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 3),
    _SmRunStartTime_Type()
)
smRunStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smRunStartTime.setStatus("current")


class _SmRunEndTime_Type(DateAndTime):
    """Custom type smRunEndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SmRunEndTime_Object = MibTableColumn
smRunEndTime = _SmRunEndTime_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 4),
    _SmRunEndTime_Type()
)
smRunEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smRunEndTime.setStatus("current")
_SmRunLifeTime_Type = TimeInterval
_SmRunLifeTime_Object = MibTableColumn
smRunLifeTime = _SmRunLifeTime_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 5),
    _SmRunLifeTime_Type()
)
smRunLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smRunLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    smRunLifeTime.setUnits("centi-seconds")
_SmRunExpireTime_Type = TimeInterval
_SmRunExpireTime_Object = MibTableColumn
smRunExpireTime = _SmRunExpireTime_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 6),
    _SmRunExpireTime_Type()
)
smRunExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smRunExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    smRunExpireTime.setUnits("centi-seconds")


class _SmRunExitCode_Type(Integer32):
    """Custom type smRunExitCode based on Integer32"""
    defaultValue = 1

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
        *(("genericError", 9),
          ("halted", 2),
          ("invalidArgument", 7),
          ("languageError", 5),
          ("lifeTimeExceeded", 3),
          ("noError", 1),
          ("noResourcesLeft", 4),
          ("runtimeError", 6),
          ("securityViolation", 8))
    )


_SmRunExitCode_Type.__name__ = "Integer32"
_SmRunExitCode_Object = MibTableColumn
smRunExitCode = _SmRunExitCode_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 7),
    _SmRunExitCode_Type()
)
smRunExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smRunExitCode.setStatus("current")


class _SmRunResult_Type(OctetString):
    """Custom type smRunResult based on OctetString"""
    defaultHexValue = ""


_SmRunResult_Object = MibTableColumn
smRunResult = _SmRunResult_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 8),
    _SmRunResult_Type()
)
smRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smRunResult.setStatus("current")


class _SmRunControl_Type(Integer32):
    """Custom type smRunControl based on Integer32"""
    defaultValue = 4

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
        *(("abort", 1),
          ("nop", 4),
          ("resume", 3),
          ("suspend", 2))
    )


_SmRunControl_Type.__name__ = "Integer32"
_SmRunControl_Object = MibTableColumn
smRunControl = _SmRunControl_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 9),
    _SmRunControl_Type()
)
smRunControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smRunControl.setStatus("current")


class _SmRunState_Type(Integer32):
    """Custom type smRunState based on Integer32"""
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
        *(("aborting", 6),
          ("executing", 2),
          ("initializing", 1),
          ("resuming", 5),
          ("suspended", 4),
          ("suspending", 3),
          ("terminated", 7))
    )


_SmRunState_Type.__name__ = "Integer32"
_SmRunState_Object = MibTableColumn
smRunState = _SmRunState_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 10),
    _SmRunState_Type()
)
smRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smRunState.setStatus("current")


class _SmRunError_Type(SnmpAdminString):
    """Custom type smRunError based on SnmpAdminString"""
    defaultHexValue = ""


_SmRunError_Object = MibTableColumn
smRunError = _SmRunError_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 11),
    _SmRunError_Type()
)
smRunError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smRunError.setStatus("current")


class _SmRunResultTime_Type(DateAndTime):
    """Custom type smRunResultTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SmRunResultTime_Object = MibTableColumn
smRunResultTime = _SmRunResultTime_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 12),
    _SmRunResultTime_Type()
)
smRunResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smRunResultTime.setStatus("current")


class _SmRunErrorTime_Type(DateAndTime):
    """Custom type smRunErrorTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SmRunErrorTime_Object = MibTableColumn
smRunErrorTime = _SmRunErrorTime_Object(
    (1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 13),
    _SmRunErrorTime_Type()
)
smRunErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smRunErrorTime.setStatus("current")
_SmNotifications_ObjectIdentity = ObjectIdentity
smNotifications = _SmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 64, 2)
)
_SmTraps_ObjectIdentity = ObjectIdentity
smTraps = _SmTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 64, 2, 0)
)
_SmConformance_ObjectIdentity = ObjectIdentity
smConformance = _SmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 64, 3)
)
_SmCompliances_ObjectIdentity = ObjectIdentity
smCompliances = _SmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 64, 3, 1)
)
_SmGroups_ObjectIdentity = ObjectIdentity
smGroups = _SmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 64, 3, 2)
)

# Managed Objects groups

smLanguageGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 1)
)
smLanguageGroup.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smLangLanguage"),
        ("DISMAN-SCRIPT-MIB", "smLangVersion"),
        ("DISMAN-SCRIPT-MIB", "smLangVendor"),
        ("DISMAN-SCRIPT-MIB", "smLangRevision"),
        ("DISMAN-SCRIPT-MIB", "smLangDescr"),
        ("DISMAN-SCRIPT-MIB", "smExtsnExtension"),
        ("DISMAN-SCRIPT-MIB", "smExtsnVersion"),
        ("DISMAN-SCRIPT-MIB", "smExtsnVendor"),
        ("DISMAN-SCRIPT-MIB", "smExtsnRevision"),
        ("DISMAN-SCRIPT-MIB", "smExtsnDescr"))
)
if mibBuilder.loadTexts:
    smLanguageGroup.setStatus("current")

smScriptGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 2)
)
smScriptGroup.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smScriptDescr"),
        ("DISMAN-SCRIPT-MIB", "smScriptLanguage"),
        ("DISMAN-SCRIPT-MIB", "smScriptSource"),
        ("DISMAN-SCRIPT-MIB", "smScriptAdminStatus"),
        ("DISMAN-SCRIPT-MIB", "smScriptOperStatus"),
        ("DISMAN-SCRIPT-MIB", "smScriptStorageType"),
        ("DISMAN-SCRIPT-MIB", "smScriptRowStatus"))
)
if mibBuilder.loadTexts:
    smScriptGroup.setStatus("deprecated")

smCodeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 3)
)
smCodeGroup.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smCodeText"),
        ("DISMAN-SCRIPT-MIB", "smCodeRowStatus"))
)
if mibBuilder.loadTexts:
    smCodeGroup.setStatus("current")

smLaunchGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 4)
)
smLaunchGroup.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smLaunchScriptOwner"),
        ("DISMAN-SCRIPT-MIB", "smLaunchScriptName"),
        ("DISMAN-SCRIPT-MIB", "smLaunchArgument"),
        ("DISMAN-SCRIPT-MIB", "smLaunchMaxRunning"),
        ("DISMAN-SCRIPT-MIB", "smLaunchMaxCompleted"),
        ("DISMAN-SCRIPT-MIB", "smLaunchLifeTime"),
        ("DISMAN-SCRIPT-MIB", "smLaunchExpireTime"),
        ("DISMAN-SCRIPT-MIB", "smLaunchStart"),
        ("DISMAN-SCRIPT-MIB", "smLaunchControl"),
        ("DISMAN-SCRIPT-MIB", "smLaunchAdminStatus"),
        ("DISMAN-SCRIPT-MIB", "smLaunchOperStatus"),
        ("DISMAN-SCRIPT-MIB", "smLaunchRunIndexNext"),
        ("DISMAN-SCRIPT-MIB", "smLaunchStorageType"),
        ("DISMAN-SCRIPT-MIB", "smLaunchRowStatus"))
)
if mibBuilder.loadTexts:
    smLaunchGroup.setStatus("deprecated")

smRunGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 5)
)
smRunGroup.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smRunArgument"),
        ("DISMAN-SCRIPT-MIB", "smRunStartTime"),
        ("DISMAN-SCRIPT-MIB", "smRunEndTime"),
        ("DISMAN-SCRIPT-MIB", "smRunLifeTime"),
        ("DISMAN-SCRIPT-MIB", "smRunExpireTime"),
        ("DISMAN-SCRIPT-MIB", "smRunExitCode"),
        ("DISMAN-SCRIPT-MIB", "smRunResult"),
        ("DISMAN-SCRIPT-MIB", "smRunState"),
        ("DISMAN-SCRIPT-MIB", "smRunControl"),
        ("DISMAN-SCRIPT-MIB", "smRunError"))
)
if mibBuilder.loadTexts:
    smRunGroup.setStatus("deprecated")

smScriptGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 7)
)
smScriptGroup2.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smScriptDescr"),
        ("DISMAN-SCRIPT-MIB", "smScriptLanguage"),
        ("DISMAN-SCRIPT-MIB", "smScriptSource"),
        ("DISMAN-SCRIPT-MIB", "smScriptAdminStatus"),
        ("DISMAN-SCRIPT-MIB", "smScriptOperStatus"),
        ("DISMAN-SCRIPT-MIB", "smScriptStorageType"),
        ("DISMAN-SCRIPT-MIB", "smScriptRowStatus"),
        ("DISMAN-SCRIPT-MIB", "smScriptError"),
        ("DISMAN-SCRIPT-MIB", "smScriptLastChange"))
)
if mibBuilder.loadTexts:
    smScriptGroup2.setStatus("current")

smLaunchGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 8)
)
smLaunchGroup2.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smLaunchScriptOwner"),
        ("DISMAN-SCRIPT-MIB", "smLaunchScriptName"),
        ("DISMAN-SCRIPT-MIB", "smLaunchArgument"),
        ("DISMAN-SCRIPT-MIB", "smLaunchMaxRunning"),
        ("DISMAN-SCRIPT-MIB", "smLaunchMaxCompleted"),
        ("DISMAN-SCRIPT-MIB", "smLaunchLifeTime"),
        ("DISMAN-SCRIPT-MIB", "smLaunchExpireTime"),
        ("DISMAN-SCRIPT-MIB", "smLaunchStart"),
        ("DISMAN-SCRIPT-MIB", "smLaunchControl"),
        ("DISMAN-SCRIPT-MIB", "smLaunchAdminStatus"),
        ("DISMAN-SCRIPT-MIB", "smLaunchOperStatus"),
        ("DISMAN-SCRIPT-MIB", "smLaunchRunIndexNext"),
        ("DISMAN-SCRIPT-MIB", "smLaunchStorageType"),
        ("DISMAN-SCRIPT-MIB", "smLaunchRowStatus"),
        ("DISMAN-SCRIPT-MIB", "smLaunchError"),
        ("DISMAN-SCRIPT-MIB", "smLaunchLastChange"),
        ("DISMAN-SCRIPT-MIB", "smLaunchRowExpireTime"))
)
if mibBuilder.loadTexts:
    smLaunchGroup2.setStatus("current")

smRunGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 9)
)
smRunGroup2.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smRunArgument"),
        ("DISMAN-SCRIPT-MIB", "smRunStartTime"),
        ("DISMAN-SCRIPT-MIB", "smRunEndTime"),
        ("DISMAN-SCRIPT-MIB", "smRunLifeTime"),
        ("DISMAN-SCRIPT-MIB", "smRunExpireTime"),
        ("DISMAN-SCRIPT-MIB", "smRunExitCode"),
        ("DISMAN-SCRIPT-MIB", "smRunResult"),
        ("DISMAN-SCRIPT-MIB", "smRunState"),
        ("DISMAN-SCRIPT-MIB", "smRunControl"),
        ("DISMAN-SCRIPT-MIB", "smRunError"),
        ("DISMAN-SCRIPT-MIB", "smRunResultTime"),
        ("DISMAN-SCRIPT-MIB", "smRunErrorTime"))
)
if mibBuilder.loadTexts:
    smRunGroup2.setStatus("current")


# Notification objects

smScriptAbort = NotificationType(
    (1, 3, 6, 1, 2, 1, 64, 2, 0, 1)
)
smScriptAbort.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smRunExitCode"),
        ("DISMAN-SCRIPT-MIB", "smRunEndTime"),
        ("DISMAN-SCRIPT-MIB", "smRunError"))
)
if mibBuilder.loadTexts:
    smScriptAbort.setStatus(
        "current"
    )

smScriptResult = NotificationType(
    (1, 3, 6, 1, 2, 1, 64, 2, 0, 2)
)
smScriptResult.setObjects(
    ("DISMAN-SCRIPT-MIB", "smRunResult")
)
if mibBuilder.loadTexts:
    smScriptResult.setStatus(
        "current"
    )

smScriptException = NotificationType(
    (1, 3, 6, 1, 2, 1, 64, 2, 0, 3)
)
smScriptException.setObjects(
    ("DISMAN-SCRIPT-MIB", "smRunError")
)
if mibBuilder.loadTexts:
    smScriptException.setStatus(
        "current"
    )


# Notifications groups

smNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 6)
)
smNotificationsGroup.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smScriptAbort"),
        ("DISMAN-SCRIPT-MIB", "smScriptResult"))
)
if mibBuilder.loadTexts:
    smNotificationsGroup.setStatus(
        "deprecated"
    )

smNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 64, 3, 2, 10)
)
smNotificationsGroup2.setObjects(
      *(("DISMAN-SCRIPT-MIB", "smScriptAbort"),
        ("DISMAN-SCRIPT-MIB", "smScriptResult"),
        ("DISMAN-SCRIPT-MIB", "smScriptException"))
)
if mibBuilder.loadTexts:
    smNotificationsGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

smCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 64, 3, 1, 1)
)
if mibBuilder.loadTexts:
    smCompliance.setStatus(
        "deprecated"
    )

smCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 64, 3, 1, 2)
)
if mibBuilder.loadTexts:
    smCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DISMAN-SCRIPT-MIB",
    **{"scriptMIB": scriptMIB,
       "smObjects": smObjects,
       "smLangTable": smLangTable,
       "smLangEntry": smLangEntry,
       "smLangIndex": smLangIndex,
       "smLangLanguage": smLangLanguage,
       "smLangVersion": smLangVersion,
       "smLangVendor": smLangVendor,
       "smLangRevision": smLangRevision,
       "smLangDescr": smLangDescr,
       "smExtsnTable": smExtsnTable,
       "smExtsnEntry": smExtsnEntry,
       "smExtsnIndex": smExtsnIndex,
       "smExtsnExtension": smExtsnExtension,
       "smExtsnVersion": smExtsnVersion,
       "smExtsnVendor": smExtsnVendor,
       "smExtsnRevision": smExtsnRevision,
       "smExtsnDescr": smExtsnDescr,
       "smScriptObjects": smScriptObjects,
       "smScriptTable": smScriptTable,
       "smScriptEntry": smScriptEntry,
       "smScriptOwner": smScriptOwner,
       "smScriptName": smScriptName,
       "smScriptDescr": smScriptDescr,
       "smScriptLanguage": smScriptLanguage,
       "smScriptSource": smScriptSource,
       "smScriptAdminStatus": smScriptAdminStatus,
       "smScriptOperStatus": smScriptOperStatus,
       "smScriptStorageType": smScriptStorageType,
       "smScriptRowStatus": smScriptRowStatus,
       "smScriptError": smScriptError,
       "smScriptLastChange": smScriptLastChange,
       "smCodeTable": smCodeTable,
       "smCodeEntry": smCodeEntry,
       "smCodeIndex": smCodeIndex,
       "smCodeText": smCodeText,
       "smCodeRowStatus": smCodeRowStatus,
       "smRunObjects": smRunObjects,
       "smLaunchTable": smLaunchTable,
       "smLaunchEntry": smLaunchEntry,
       "smLaunchOwner": smLaunchOwner,
       "smLaunchName": smLaunchName,
       "smLaunchScriptOwner": smLaunchScriptOwner,
       "smLaunchScriptName": smLaunchScriptName,
       "smLaunchArgument": smLaunchArgument,
       "smLaunchMaxRunning": smLaunchMaxRunning,
       "smLaunchMaxCompleted": smLaunchMaxCompleted,
       "smLaunchLifeTime": smLaunchLifeTime,
       "smLaunchExpireTime": smLaunchExpireTime,
       "smLaunchStart": smLaunchStart,
       "smLaunchControl": smLaunchControl,
       "smLaunchAdminStatus": smLaunchAdminStatus,
       "smLaunchOperStatus": smLaunchOperStatus,
       "smLaunchRunIndexNext": smLaunchRunIndexNext,
       "smLaunchStorageType": smLaunchStorageType,
       "smLaunchRowStatus": smLaunchRowStatus,
       "smLaunchError": smLaunchError,
       "smLaunchLastChange": smLaunchLastChange,
       "smLaunchRowExpireTime": smLaunchRowExpireTime,
       "smRunTable": smRunTable,
       "smRunEntry": smRunEntry,
       "smRunIndex": smRunIndex,
       "smRunArgument": smRunArgument,
       "smRunStartTime": smRunStartTime,
       "smRunEndTime": smRunEndTime,
       "smRunLifeTime": smRunLifeTime,
       "smRunExpireTime": smRunExpireTime,
       "smRunExitCode": smRunExitCode,
       "smRunResult": smRunResult,
       "smRunControl": smRunControl,
       "smRunState": smRunState,
       "smRunError": smRunError,
       "smRunResultTime": smRunResultTime,
       "smRunErrorTime": smRunErrorTime,
       "smNotifications": smNotifications,
       "smTraps": smTraps,
       "smScriptAbort": smScriptAbort,
       "smScriptResult": smScriptResult,
       "smScriptException": smScriptException,
       "smConformance": smConformance,
       "smCompliances": smCompliances,
       "smCompliance": smCompliance,
       "smCompliance2": smCompliance2,
       "smGroups": smGroups,
       "smLanguageGroup": smLanguageGroup,
       "smScriptGroup": smScriptGroup,
       "smCodeGroup": smCodeGroup,
       "smLaunchGroup": smLaunchGroup,
       "smRunGroup": smRunGroup,
       "smNotificationsGroup": smNotificationsGroup,
       "smScriptGroup2": smScriptGroup2,
       "smLaunchGroup2": smLaunchGroup2,
       "smRunGroup2": smRunGroup2,
       "smNotificationsGroup2": smNotificationsGroup2}
)
