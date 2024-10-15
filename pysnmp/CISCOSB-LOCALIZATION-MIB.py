# SNMP MIB module (CISCOSB-LOCALIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-LOCALIZATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:32 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlLocalization = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103)
)
rlLocalization.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlLocalizationActivelanguage_Type(DisplayString):
    """Custom type rlLocalizationActivelanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RlLocalizationActivelanguage_Type.__name__ = "DisplayString"
_RlLocalizationActivelanguage_Object = MibScalar
rlLocalizationActivelanguage = _RlLocalizationActivelanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 8),
    _RlLocalizationActivelanguage_Type()
)
rlLocalizationActivelanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLocalizationActivelanguage.setStatus("current")
_RlLocalizationLoginlanguage_Type = DisplayString
_RlLocalizationLoginlanguage_Object = MibScalar
rlLocalizationLoginlanguage = _RlLocalizationLoginlanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 9),
    _RlLocalizationLoginlanguage_Type()
)
rlLocalizationLoginlanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationLoginlanguage.setStatus("current")
_RlLocalizationLanguagesTable_Object = MibTable
rlLocalizationLanguagesTable = _RlLocalizationLanguagesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10)
)
if mibBuilder.loadTexts:
    rlLocalizationLanguagesTable.setStatus("current")
_RlLocalizationLanguagesEntry_Object = MibTableRow
rlLocalizationLanguagesEntry = _RlLocalizationLanguagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1)
)
rlLocalizationLanguagesEntry.setIndexNames(
    (1, "CISCOSB-LOCALIZATION-MIB", "rlLocalizationLanguagesName"),
)
if mibBuilder.loadTexts:
    rlLocalizationLanguagesEntry.setStatus("current")


class _RlLocalizationLanguagesName_Type(DisplayString):
    """Custom type rlLocalizationLanguagesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_RlLocalizationLanguagesName_Type.__name__ = "DisplayString"
_RlLocalizationLanguagesName_Object = MibTableColumn
rlLocalizationLanguagesName = _RlLocalizationLanguagesName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 1),
    _RlLocalizationLanguagesName_Type()
)
rlLocalizationLanguagesName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLocalizationLanguagesName.setStatus("current")


class _RlLocalizationLanguagesUnicodeName_Type(SnmpAdminString):
    """Custom type rlLocalizationLanguagesUnicodeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlLocalizationLanguagesUnicodeName_Type.__name__ = "SnmpAdminString"
_RlLocalizationLanguagesUnicodeName_Object = MibTableColumn
rlLocalizationLanguagesUnicodeName = _RlLocalizationLanguagesUnicodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 2),
    _RlLocalizationLanguagesUnicodeName_Type()
)
rlLocalizationLanguagesUnicodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationLanguagesUnicodeName.setStatus("current")
_RlLocalizationLanguagesUrlDir_Type = DisplayString
_RlLocalizationLanguagesUrlDir_Object = MibTableColumn
rlLocalizationLanguagesUrlDir = _RlLocalizationLanguagesUrlDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 3),
    _RlLocalizationLanguagesUrlDir_Type()
)
rlLocalizationLanguagesUrlDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationLanguagesUrlDir.setStatus("current")
_RlLocalizationLanguagesUrlHelpDir_Type = DisplayString
_RlLocalizationLanguagesUrlHelpDir_Object = MibTableColumn
rlLocalizationLanguagesUrlHelpDir = _RlLocalizationLanguagesUrlHelpDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 4),
    _RlLocalizationLanguagesUrlHelpDir_Type()
)
rlLocalizationLanguagesUrlHelpDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationLanguagesUrlHelpDir.setStatus("current")
_RlLocalizationLanguageCode_Type = DisplayString
_RlLocalizationLanguageCode_Object = MibTableColumn
rlLocalizationLanguageCode = _RlLocalizationLanguageCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 5),
    _RlLocalizationLanguageCode_Type()
)
rlLocalizationLanguageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationLanguageCode.setStatus("current")


class _RlLocalizationNumOfSections_Type(Integer32):
    """Custom type rlLocalizationNumOfSections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlLocalizationNumOfSections_Type.__name__ = "Integer32"
_RlLocalizationNumOfSections_Object = MibTableColumn
rlLocalizationNumOfSections = _RlLocalizationNumOfSections_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 6),
    _RlLocalizationNumOfSections_Type()
)
rlLocalizationNumOfSections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationNumOfSections.setStatus("current")


class _RlLocalizationNumOfEmbSections_Type(Integer32):
    """Custom type rlLocalizationNumOfEmbSections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlLocalizationNumOfEmbSections_Type.__name__ = "Integer32"
_RlLocalizationNumOfEmbSections_Object = MibTableColumn
rlLocalizationNumOfEmbSections = _RlLocalizationNumOfEmbSections_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 7),
    _RlLocalizationNumOfEmbSections_Type()
)
rlLocalizationNumOfEmbSections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationNumOfEmbSections.setStatus("current")


class _RlLocalizationVersion_Type(DisplayString):
    """Custom type rlLocalizationVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RlLocalizationVersion_Type.__name__ = "DisplayString"
_RlLocalizationVersion_Object = MibTableColumn
rlLocalizationVersion = _RlLocalizationVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 8),
    _RlLocalizationVersion_Type()
)
rlLocalizationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationVersion.setStatus("current")
_RlLocalizationMd5ChksumFile_Type = DisplayString
_RlLocalizationMd5ChksumFile_Object = MibTableColumn
rlLocalizationMd5ChksumFile = _RlLocalizationMd5ChksumFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 9),
    _RlLocalizationMd5ChksumFile_Type()
)
rlLocalizationMd5ChksumFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLocalizationMd5ChksumFile.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-LOCALIZATION-MIB",
    **{"rlLocalization": rlLocalization,
       "rlLocalizationActivelanguage": rlLocalizationActivelanguage,
       "rlLocalizationLoginlanguage": rlLocalizationLoginlanguage,
       "rlLocalizationLanguagesTable": rlLocalizationLanguagesTable,
       "rlLocalizationLanguagesEntry": rlLocalizationLanguagesEntry,
       "rlLocalizationLanguagesName": rlLocalizationLanguagesName,
       "rlLocalizationLanguagesUnicodeName": rlLocalizationLanguagesUnicodeName,
       "rlLocalizationLanguagesUrlDir": rlLocalizationLanguagesUrlDir,
       "rlLocalizationLanguagesUrlHelpDir": rlLocalizationLanguagesUrlHelpDir,
       "rlLocalizationLanguageCode": rlLocalizationLanguageCode,
       "rlLocalizationNumOfSections": rlLocalizationNumOfSections,
       "rlLocalizationNumOfEmbSections": rlLocalizationNumOfEmbSections,
       "rlLocalizationVersion": rlLocalizationVersion,
       "rlLocalizationMd5ChksumFile": rlLocalizationMd5ChksumFile}
)
