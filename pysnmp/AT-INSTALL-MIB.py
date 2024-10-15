# SNMP MIB module (AT-INSTALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-INSTALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:18 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

install = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49)
)
install.setRevisions(
        ("2006-06-28 12:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InstallTrap_ObjectIdentity = ObjectIdentity
installTrap = _InstallTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 0)
)
_InstallTable_Object = MibTable
installTable = _InstallTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1)
)
if mibBuilder.loadTexts:
    installTable.setStatus("current")
_InstallEntry_Object = MibTableRow
installEntry = _InstallEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1)
)
installEntry.setIndexNames(
    (0, "AT-INSTALL-MIB", "instIndex"),
)
if mibBuilder.loadTexts:
    installEntry.setStatus("current")


class _InstIndex_Type(Integer32):
    """Custom type instIndex based on Integer32"""
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
        *(("current", 4),
          ("default", 3),
          ("preferred", 2),
          ("temporary", 1))
    )


_InstIndex_Type.__name__ = "Integer32"
_InstIndex_Object = MibTableColumn
instIndex = _InstIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 1),
    _InstIndex_Type()
)
instIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instIndex.setStatus("current")


class _InstRelDevice_Type(Integer32):
    """Custom type instRelDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eprom", 2),
          ("flash", 3),
          ("none", 1))
    )


_InstRelDevice_Type.__name__ = "Integer32"
_InstRelDevice_Object = MibTableColumn
instRelDevice = _InstRelDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 2),
    _InstRelDevice_Type()
)
instRelDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelDevice.setStatus("current")
_InstRelName_Type = DisplayString
_InstRelName_Object = MibTableColumn
instRelName = _InstRelName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 3),
    _InstRelName_Type()
)
instRelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelName.setStatus("current")
_InstRelMajor_Type = Integer32
_InstRelMajor_Object = MibTableColumn
instRelMajor = _InstRelMajor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 4),
    _InstRelMajor_Type()
)
instRelMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelMajor.setStatus("current")
_InstRelMinor_Type = Integer32
_InstRelMinor_Object = MibTableColumn
instRelMinor = _InstRelMinor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 5),
    _InstRelMinor_Type()
)
instRelMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelMinor.setStatus("current")


class _InstPatDevice_Type(Integer32):
    """Custom type instPatDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("none", 1),
          ("nvs", 4))
    )


_InstPatDevice_Type.__name__ = "Integer32"
_InstPatDevice_Object = MibTableColumn
instPatDevice = _InstPatDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 6),
    _InstPatDevice_Type()
)
instPatDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instPatDevice.setStatus("current")
_InstPatName_Type = DisplayString
_InstPatName_Object = MibTableColumn
instPatName = _InstPatName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 7),
    _InstPatName_Type()
)
instPatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instPatName.setStatus("current")
_InstRelInterim_Type = Integer32
_InstRelInterim_Object = MibTableColumn
instRelInterim = _InstRelInterim_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 8),
    _InstRelInterim_Type()
)
instRelInterim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelInterim.setStatus("current")


class _InstRelExists_Type(Integer32):
    """Custom type instRelExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_InstRelExists_Type.__name__ = "Integer32"
_InstRelExists_Object = MibTableColumn
instRelExists = _InstRelExists_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 9),
    _InstRelExists_Type()
)
instRelExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instRelExists.setStatus("current")


class _InstPatExists_Type(Integer32):
    """Custom type instPatExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_InstPatExists_Type.__name__ = "Integer32"
_InstPatExists_Object = MibTableColumn
instPatExists = _InstPatExists_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 10),
    _InstPatExists_Type()
)
instPatExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instPatExists.setStatus("current")
_InstallHistoryTable_Object = MibTable
installHistoryTable = _InstallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2)
)
if mibBuilder.loadTexts:
    installHistoryTable.setStatus("current")
_InstallHistoryEntry_Object = MibTableRow
installHistoryEntry = _InstallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2, 1)
)
installHistoryEntry.setIndexNames(
    (0, "AT-INSTALL-MIB", "instHistIndex"),
)
if mibBuilder.loadTexts:
    installHistoryEntry.setStatus("current")
_InstHistIndex_Type = Integer32
_InstHistIndex_Object = MibTableColumn
instHistIndex = _InstHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2, 1, 1),
    _InstHistIndex_Type()
)
instHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instHistIndex.setStatus("current")
_InstHistLine_Type = DisplayString
_InstHistLine_Object = MibTableColumn
instHistLine = _InstHistLine_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2, 1, 2),
    _InstHistLine_Type()
)
instHistLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instHistLine.setStatus("current")
_ConfigFile_Type = DisplayString
_ConfigFile_Object = MibScalar
configFile = _ConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 3),
    _ConfigFile_Type()
)
configFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFile.setStatus("current")
_LicenceTable_Object = MibTable
licenceTable = _LicenceTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4)
)
if mibBuilder.loadTexts:
    licenceTable.setStatus("current")
_LicenceEntry_Object = MibTableRow
licenceEntry = _LicenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1)
)
licenceEntry.setIndexNames(
    (0, "AT-INSTALL-MIB", "licenceIndex"),
)
if mibBuilder.loadTexts:
    licenceEntry.setStatus("current")
_LicenceIndex_Type = Integer32
_LicenceIndex_Object = MibTableColumn
licenceIndex = _LicenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 1),
    _LicenceIndex_Type()
)
licenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceIndex.setStatus("current")


class _LicenceStatus_Type(Integer32):
    """Custom type licenceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleting", 2),
          ("ok", 1))
    )


_LicenceStatus_Type.__name__ = "Integer32"
_LicenceStatus_Object = MibTableColumn
licenceStatus = _LicenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 2),
    _LicenceStatus_Type()
)
licenceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceStatus.setStatus("current")
_LicenceRelease_Type = DisplayString
_LicenceRelease_Object = MibTableColumn
licenceRelease = _LicenceRelease_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 3),
    _LicenceRelease_Type()
)
licenceRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceRelease.setStatus("current")
_LicenceMajor_Type = Integer32
_LicenceMajor_Object = MibTableColumn
licenceMajor = _LicenceMajor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 4),
    _LicenceMajor_Type()
)
licenceMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceMajor.setStatus("current")
_LicenceMinor_Type = Integer32
_LicenceMinor_Object = MibTableColumn
licenceMinor = _LicenceMinor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 5),
    _LicenceMinor_Type()
)
licenceMinor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceMinor.setStatus("current")


class _LicencePassword_Type(DisplayStringUnsized):
    """Custom type licencePassword based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_LicencePassword_Type.__name__ = "DisplayStringUnsized"
_LicencePassword_Object = MibTableColumn
licencePassword = _LicencePassword_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 6),
    _LicencePassword_Type()
)
licencePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licencePassword.setStatus("current")
_LicenceExpiry_Type = DisplayString
_LicenceExpiry_Object = MibTableColumn
licenceExpiry = _LicenceExpiry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 7),
    _LicenceExpiry_Type()
)
licenceExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceExpiry.setStatus("current")
_LicenceInterim_Type = Integer32
_LicenceInterim_Object = MibTableColumn
licenceInterim = _LicenceInterim_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 8),
    _LicenceInterim_Type()
)
licenceInterim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenceInterim.setStatus("current")
_CreateConfigFile_Type = DisplayString
_CreateConfigFile_Object = MibScalar
createConfigFile = _CreateConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 5),
    _CreateConfigFile_Type()
)
createConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    createConfigFile.setStatus("current")


class _ConfigFileExist_Type(Integer32):
    """Custom type configFileExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ConfigFileExist_Type.__name__ = "Integer32"
_ConfigFileExist_Object = MibScalar
configFileExist = _ConfigFileExist_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 6),
    _ConfigFileExist_Type()
)
configFileExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFileExist.setStatus("current")
_CurrentConfigFile_Type = DisplayString
_CurrentConfigFile_Object = MibScalar
currentConfigFile = _CurrentConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 7),
    _CurrentConfigFile_Type()
)
currentConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentConfigFile.setStatus("current")

# Managed Objects groups


# Notification objects

configFileExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 0, 1)
)
configFileExistTrap.setObjects(
    ("AT-INSTALL-MIB", "configFileExist")
)
if mibBuilder.loadTexts:
    configFileExistTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-INSTALL-MIB",
    **{"install": install,
       "installTrap": installTrap,
       "configFileExistTrap": configFileExistTrap,
       "installTable": installTable,
       "installEntry": installEntry,
       "instIndex": instIndex,
       "instRelDevice": instRelDevice,
       "instRelName": instRelName,
       "instRelMajor": instRelMajor,
       "instRelMinor": instRelMinor,
       "instPatDevice": instPatDevice,
       "instPatName": instPatName,
       "instRelInterim": instRelInterim,
       "instRelExists": instRelExists,
       "instPatExists": instPatExists,
       "installHistoryTable": installHistoryTable,
       "installHistoryEntry": installHistoryEntry,
       "instHistIndex": instHistIndex,
       "instHistLine": instHistLine,
       "configFile": configFile,
       "licenceTable": licenceTable,
       "licenceEntry": licenceEntry,
       "licenceIndex": licenceIndex,
       "licenceStatus": licenceStatus,
       "licenceRelease": licenceRelease,
       "licenceMajor": licenceMajor,
       "licenceMinor": licenceMinor,
       "licencePassword": licencePassword,
       "licenceExpiry": licenceExpiry,
       "licenceInterim": licenceInterim,
       "createConfigFile": createConfigFile,
       "configFileExist": configFileExist,
       "currentConfigFile": currentConfigFile}
)
