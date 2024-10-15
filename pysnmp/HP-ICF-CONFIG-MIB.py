# SNMP MIB module (HP-ICF-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:11 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpicfConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136)
)
hpicfConfig.setRevisions(
        ("2017-10-07 00:00",
         "2017-04-19 00:00",
         "2017-03-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfConfigNotifications_ObjectIdentity = ObjectIdentity
hpicfConfigNotifications = _HpicfConfigNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 0)
)
_HpicfConfigScalar_ObjectIdentity = ObjectIdentity
hpicfConfigScalar = _HpicfConfigScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 1)
)
_HpicfConfigGlobals_ObjectIdentity = ObjectIdentity
hpicfConfigGlobals = _HpicfConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 2)
)
_HpicfConfigConformance_ObjectIdentity = ObjectIdentity
hpicfConfigConformance = _HpicfConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 3)
)
_HpicfConfigGroups_ObjectIdentity = ObjectIdentity
hpicfConfigGroups = _HpicfConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 3, 1)
)
_HpicfConfigMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfConfigMIBCompliances = _HpicfConfigMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 3, 2)
)
_HpicfConfigConfig_ObjectIdentity = ObjectIdentity
hpicfConfigConfig = _HpicfConfigConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4)
)
_HpicfConfigObjects_ObjectIdentity = ObjectIdentity
hpicfConfigObjects = _HpicfConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 1)
)


class _HpicfConfigRestoreFileName_Type(OctetString):
    """Custom type hpicfConfigRestoreFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfConfigRestoreFileName_Type.__name__ = "OctetString"
_HpicfConfigRestoreFileName_Object = MibScalar
hpicfConfigRestoreFileName = _HpicfConfigRestoreFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 1, 1),
    _HpicfConfigRestoreFileName_Type()
)
hpicfConfigRestoreFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfConfigRestoreFileName.setStatus("current")


class _HpicfConfigRunningConfigSHA_Type(OctetString):
    """Custom type hpicfConfigRunningConfigSHA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfConfigRunningConfigSHA_Type.__name__ = "OctetString"
_HpicfConfigRunningConfigSHA_Object = MibScalar
hpicfConfigRunningConfigSHA = _HpicfConfigRunningConfigSHA_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 1, 2),
    _HpicfConfigRunningConfigSHA_Type()
)
hpicfConfigRunningConfigSHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfConfigRunningConfigSHA.setStatus("current")


class _HpicfConfigStartupConfigSHA_Type(OctetString):
    """Custom type hpicfConfigStartupConfigSHA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfConfigStartupConfigSHA_Type.__name__ = "OctetString"
_HpicfConfigStartupConfigSHA_Object = MibScalar
hpicfConfigStartupConfigSHA = _HpicfConfigStartupConfigSHA_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 1, 3),
    _HpicfConfigStartupConfigSHA_Type()
)
hpicfConfigStartupConfigSHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfConfigStartupConfigSHA.setStatus("current")


class _HpicfConfigRestoreStatus_Type(Integer32):
    """Custom type hpicfConfigRestoreStatus based on Integer32"""
    defaultValue = 1

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
        *(("failed", 4),
          ("inProgress", 2),
          ("notYetRun", 1),
          ("success", 3))
    )


_HpicfConfigRestoreStatus_Type.__name__ = "Integer32"
_HpicfConfigRestoreStatus_Object = MibScalar
hpicfConfigRestoreStatus = _HpicfConfigRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 1, 4),
    _HpicfConfigRestoreStatus_Type()
)
hpicfConfigRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfConfigRestoreStatus.setStatus("current")


class _HpicfConfigRecoveryMode_Type(Integer32):
    """Custom type hpicfConfigRecoveryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfConfigRecoveryMode_Type.__name__ = "Integer32"
_HpicfConfigRecoveryMode_Object = MibScalar
hpicfConfigRecoveryMode = _HpicfConfigRecoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 1, 5),
    _HpicfConfigRecoveryMode_Type()
)
hpicfConfigRecoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfConfigRecoveryMode.setStatus("current")
_HpicfConfigFilesObjects_ObjectIdentity = ObjectIdentity
hpicfConfigFilesObjects = _HpicfConfigFilesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 2)
)
_HpicfConfigFilesTable_Object = MibTable
hpicfConfigFilesTable = _HpicfConfigFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfConfigFilesTable.setStatus("current")
_HpicfConfigFilesEntry_Object = MibTableRow
hpicfConfigFilesEntry = _HpicfConfigFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 2, 1, 1)
)
hpicfConfigFilesEntry.setIndexNames(
    (0, "HP-ICF-CONFIG-MIB", "hpicfConfigFilePos"),
)
if mibBuilder.loadTexts:
    hpicfConfigFilesEntry.setStatus("current")
_HpicfConfigFilePos_Type = Unsigned32
_HpicfConfigFilePos_Object = MibTableColumn
hpicfConfigFilePos = _HpicfConfigFilePos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 2, 1, 1, 1),
    _HpicfConfigFilePos_Type()
)
hpicfConfigFilePos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfConfigFilePos.setStatus("current")


class _HpicfConfigFileName_Type(OctetString):
    """Custom type hpicfConfigFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfConfigFileName_Type.__name__ = "OctetString"
_HpicfConfigFileName_Object = MibTableColumn
hpicfConfigFileName = _HpicfConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 2, 1, 1, 2),
    _HpicfConfigFileName_Type()
)
hpicfConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfConfigFileName.setStatus("current")
_HpicfConfigTimestamp_Type = DateAndTime
_HpicfConfigTimestamp_Object = MibTableColumn
hpicfConfigTimestamp = _HpicfConfigTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 4, 2, 1, 1, 3),
    _HpicfConfigTimestamp_Type()
)
hpicfConfigTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfConfigTimestamp.setStatus("current")

# Managed Objects groups

hpicfConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 3, 1, 1)
)
hpicfConfigScalarsGroup.setObjects(
      *(("HP-ICF-CONFIG-MIB", "hpicfConfigRestoreFileName"),
        ("HP-ICF-CONFIG-MIB", "hpicfConfigRunningConfigSHA"),
        ("HP-ICF-CONFIG-MIB", "hpicfConfigStartupConfigSHA"),
        ("HP-ICF-CONFIG-MIB", "hpicfConfigRestoreStatus"),
        ("HP-ICF-CONFIG-MIB", "hpicfConfigRecoveryMode"))
)
if mibBuilder.loadTexts:
    hpicfConfigScalarsGroup.setStatus("current")

hpicfConfigFilesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 3, 1, 2)
)
hpicfConfigFilesGroup.setObjects(
      *(("HP-ICF-CONFIG-MIB", "hpicfConfigFileName"),
        ("HP-ICF-CONFIG-MIB", "hpicfConfigTimestamp"))
)
if mibBuilder.loadTexts:
    hpicfConfigFilesGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-CONFIG-MIB",
    **{"hpicfConfig": hpicfConfig,
       "hpicfConfigNotifications": hpicfConfigNotifications,
       "hpicfConfigScalar": hpicfConfigScalar,
       "hpicfConfigGlobals": hpicfConfigGlobals,
       "hpicfConfigConformance": hpicfConfigConformance,
       "hpicfConfigGroups": hpicfConfigGroups,
       "hpicfConfigScalarsGroup": hpicfConfigScalarsGroup,
       "hpicfConfigFilesGroup": hpicfConfigFilesGroup,
       "hpicfConfigMIBCompliances": hpicfConfigMIBCompliances,
       "hpicfConfigMIBCompliance": hpicfConfigMIBCompliance,
       "hpicfConfigConfig": hpicfConfigConfig,
       "hpicfConfigObjects": hpicfConfigObjects,
       "hpicfConfigRestoreFileName": hpicfConfigRestoreFileName,
       "hpicfConfigRunningConfigSHA": hpicfConfigRunningConfigSHA,
       "hpicfConfigStartupConfigSHA": hpicfConfigStartupConfigSHA,
       "hpicfConfigRestoreStatus": hpicfConfigRestoreStatus,
       "hpicfConfigRecoveryMode": hpicfConfigRecoveryMode,
       "hpicfConfigFilesObjects": hpicfConfigFilesObjects,
       "hpicfConfigFilesTable": hpicfConfigFilesTable,
       "hpicfConfigFilesEntry": hpicfConfigFilesEntry,
       "hpicfConfigFilePos": hpicfConfigFilePos,
       "hpicfConfigFileName": hpicfConfigFileName,
       "hpicfConfigTimestamp": hpicfConfigTimestamp}
)
