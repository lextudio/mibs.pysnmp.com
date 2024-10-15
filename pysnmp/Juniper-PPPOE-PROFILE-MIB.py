# SNMP MIB module (Juniper-PPPOE-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PPPOE-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:01 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,
 JuniSetMap) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniSetMap")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

juniPppoeProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46)
)
juniPppoeProfileMIB.setRevisions(
        ("2008-06-18 10:29",
         "2005-07-13 11:40",
         "2004-06-10 19:25",
         "2003-03-11 21:58",
         "2002-09-16 21:44",
         "2002-08-15 20:34",
         "2002-08-15 19:07",
         "2001-03-21 18:32")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniPppoeProfileObjects_ObjectIdentity = ObjectIdentity
juniPppoeProfileObjects = _JuniPppoeProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1)
)
_JuniPppoeProfile_ObjectIdentity = ObjectIdentity
juniPppoeProfile = _JuniPppoeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1)
)
_JuniPppoeProfileTable_Object = MibTable
juniPppoeProfileTable = _JuniPppoeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniPppoeProfileTable.setStatus("current")
_JuniPppoeProfileEntry_Object = MibTableRow
juniPppoeProfileEntry = _JuniPppoeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1)
)
juniPppoeProfileEntry.setIndexNames(
    (0, "Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileId"),
)
if mibBuilder.loadTexts:
    juniPppoeProfileEntry.setStatus("current")
_JuniPppoeProfileId_Type = Unsigned32
_JuniPppoeProfileId_Object = MibTableColumn
juniPppoeProfileId = _JuniPppoeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 1),
    _JuniPppoeProfileId_Type()
)
juniPppoeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppoeProfileId.setStatus("current")
_JuniPppoeProfileSetMap_Type = JuniSetMap
_JuniPppoeProfileSetMap_Object = MibTableColumn
juniPppoeProfileSetMap = _JuniPppoeProfileSetMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 2),
    _JuniPppoeProfileSetMap_Type()
)
juniPppoeProfileSetMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfileSetMap.setStatus("current")


class _JuniPppoeProfileMaxNumSessions_Type(Integer32):
    """Custom type juniPppoeProfileMaxNumSessions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniPppoeProfileMaxNumSessions_Type.__name__ = "Integer32"
_JuniPppoeProfileMaxNumSessions_Object = MibTableColumn
juniPppoeProfileMaxNumSessions = _JuniPppoeProfileMaxNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 3),
    _JuniPppoeProfileMaxNumSessions_Type()
)
juniPppoeProfileMaxNumSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfileMaxNumSessions.setStatus("current")


class _JuniPppoeProfileSubMotm_Type(DisplayString):
    """Custom type juniPppoeProfileSubMotm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JuniPppoeProfileSubMotm_Type.__name__ = "DisplayString"
_JuniPppoeProfileSubMotm_Object = MibTableColumn
juniPppoeProfileSubMotm = _JuniPppoeProfileSubMotm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 4),
    _JuniPppoeProfileSubMotm_Type()
)
juniPppoeProfileSubMotm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfileSubMotm.setStatus("current")


class _JuniPppoeProfileSubUrl_Type(DisplayString):
    """Custom type juniPppoeProfileSubUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JuniPppoeProfileSubUrl_Type.__name__ = "DisplayString"
_JuniPppoeProfileSubUrl_Object = MibTableColumn
juniPppoeProfileSubUrl = _JuniPppoeProfileSubUrl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 5),
    _JuniPppoeProfileSubUrl_Type()
)
juniPppoeProfileSubUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfileSubUrl.setStatus("current")


class _JuniPppoeProfileDupProtect_Type(JuniEnable):
    """Custom type juniPppoeProfileDupProtect based on JuniEnable"""


_JuniPppoeProfileDupProtect_Object = MibTableColumn
juniPppoeProfileDupProtect = _JuniPppoeProfileDupProtect_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 6),
    _JuniPppoeProfileDupProtect_Type()
)
juniPppoeProfileDupProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfileDupProtect.setStatus("current")


class _JuniPppoeProfileAcName_Type(DisplayString):
    """Custom type juniPppoeProfileAcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniPppoeProfileAcName_Type.__name__ = "DisplayString"
_JuniPppoeProfileAcName_Object = MibTableColumn
juniPppoeProfileAcName = _JuniPppoeProfileAcName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 7),
    _JuniPppoeProfileAcName_Type()
)
juniPppoeProfileAcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfileAcName.setStatus("current")


class _JuniPppoeProfilePadiFlag_Type(JuniEnable):
    """Custom type juniPppoeProfilePadiFlag based on JuniEnable"""


_JuniPppoeProfilePadiFlag_Object = MibTableColumn
juniPppoeProfilePadiFlag = _JuniPppoeProfilePadiFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 8),
    _JuniPppoeProfilePadiFlag_Type()
)
juniPppoeProfilePadiFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfilePadiFlag.setStatus("current")


class _JuniPppoeProfilePacketTrace_Type(JuniEnable):
    """Custom type juniPppoeProfilePacketTrace based on JuniEnable"""


_JuniPppoeProfilePacketTrace_Object = MibTableColumn
juniPppoeProfilePacketTrace = _JuniPppoeProfilePacketTrace_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 9),
    _JuniPppoeProfilePacketTrace_Type()
)
juniPppoeProfilePacketTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfilePacketTrace.setStatus("current")


class _JuniPppoeProfileServiceNameTableName_Type(DisplayString):
    """Custom type juniPppoeProfileServiceNameTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JuniPppoeProfileServiceNameTableName_Type.__name__ = "DisplayString"
_JuniPppoeProfileServiceNameTableName_Object = MibTableColumn
juniPppoeProfileServiceNameTableName = _JuniPppoeProfileServiceNameTableName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 10),
    _JuniPppoeProfileServiceNameTableName_Type()
)
juniPppoeProfileServiceNameTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfileServiceNameTableName.setStatus("current")


class _JuniPppoeProfilePadrRemoteCircuitIdCapture_Type(JuniEnable):
    """Custom type juniPppoeProfilePadrRemoteCircuitIdCapture based on JuniEnable"""


_JuniPppoeProfilePadrRemoteCircuitIdCapture_Object = MibTableColumn
juniPppoeProfilePadrRemoteCircuitIdCapture = _JuniPppoeProfilePadrRemoteCircuitIdCapture_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 11),
    _JuniPppoeProfilePadrRemoteCircuitIdCapture_Type()
)
juniPppoeProfilePadrRemoteCircuitIdCapture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfilePadrRemoteCircuitIdCapture.setStatus("current")


class _JuniPppoeProfileMtu_Type(Integer32):
    """Custom type juniPppoeProfileMtu based on Integer32"""
    defaultValue = 1494

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(66, 65535),
    )


_JuniPppoeProfileMtu_Type.__name__ = "Integer32"
_JuniPppoeProfileMtu_Object = MibTableColumn
juniPppoeProfileMtu = _JuniPppoeProfileMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 12),
    _JuniPppoeProfileMtu_Type()
)
juniPppoeProfileMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfileMtu.setStatus("current")


class _JuniPppoeProfileMaxSessionOverride_Type(Integer32):
    """Custom type juniPppoeProfileMaxSessionOverride based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("override", 1))
    )


_JuniPppoeProfileMaxSessionOverride_Type.__name__ = "Integer32"
_JuniPppoeProfileMaxSessionOverride_Object = MibTableColumn
juniPppoeProfileMaxSessionOverride = _JuniPppoeProfileMaxSessionOverride_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 13),
    _JuniPppoeProfileMaxSessionOverride_Type()
)
juniPppoeProfileMaxSessionOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppoeProfileMaxSessionOverride.setStatus("current")
_JuniPppoeProfileConformance_ObjectIdentity = ObjectIdentity
juniPppoeProfileConformance = _JuniPppoeProfileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4)
)
_JuniPppoeProfileCompliances_ObjectIdentity = ObjectIdentity
juniPppoeProfileCompliances = _JuniPppoeProfileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1)
)
_JuniPppoeProfileGroups_ObjectIdentity = ObjectIdentity
juniPppoeProfileGroups = _JuniPppoeProfileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2)
)

# Managed Objects groups

juniPppoeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 1)
)
juniPppoeProfileGroup.setObjects(
      *(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"))
)
if mibBuilder.loadTexts:
    juniPppoeProfileGroup.setStatus("obsolete")

juniPppoeProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 2)
)
juniPppoeProfileGroup2.setObjects(
      *(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"))
)
if mibBuilder.loadTexts:
    juniPppoeProfileGroup2.setStatus("obsolete")

juniPppoeProfileGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 3)
)
juniPppoeProfileGroup3.setObjects(
      *(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"))
)
if mibBuilder.loadTexts:
    juniPppoeProfileGroup3.setStatus("obsolete")

juniPppoeProfileGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 4)
)
juniPppoeProfileGroup4.setObjects(
      *(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"))
)
if mibBuilder.loadTexts:
    juniPppoeProfileGroup4.setStatus("obsolete")

juniPppoeProfileGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 5)
)
juniPppoeProfileGroup5.setObjects(
      *(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadrRemoteCircuitIdCapture"))
)
if mibBuilder.loadTexts:
    juniPppoeProfileGroup5.setStatus("obsolete")

juniPppoeProfileGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 6)
)
juniPppoeProfileGroup6.setObjects(
      *(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadrRemoteCircuitIdCapture"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMtu"))
)
if mibBuilder.loadTexts:
    juniPppoeProfileGroup6.setStatus("obsolete")

juniPppoeProfileGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 7)
)
juniPppoeProfileGroup7.setObjects(
      *(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadrRemoteCircuitIdCapture"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMtu"),
        ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxSessionOverride"))
)
if mibBuilder.loadTexts:
    juniPppoeProfileGroup7.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniPppoeProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniPppoeProfileCompliance.setStatus(
        "obsolete"
    )

juniPppoeCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniPppoeCompliance2.setStatus(
        "obsolete"
    )

juniPppoeCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniPppoeCompliance3.setStatus(
        "obsolete"
    )

juniPppoeCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniPppoeCompliance4.setStatus(
        "obsolete"
    )

juniPppoeCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniPppoeCompliance5.setStatus(
        "obsolete"
    )

juniPppoeCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniPppoeCompliance6.setStatus(
        "obsolete"
    )

juniPppoeCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 7)
)
if mibBuilder.loadTexts:
    juniPppoeCompliance7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PPPOE-PROFILE-MIB",
    **{"juniPppoeProfileMIB": juniPppoeProfileMIB,
       "juniPppoeProfileObjects": juniPppoeProfileObjects,
       "juniPppoeProfile": juniPppoeProfile,
       "juniPppoeProfileTable": juniPppoeProfileTable,
       "juniPppoeProfileEntry": juniPppoeProfileEntry,
       "juniPppoeProfileId": juniPppoeProfileId,
       "juniPppoeProfileSetMap": juniPppoeProfileSetMap,
       "juniPppoeProfileMaxNumSessions": juniPppoeProfileMaxNumSessions,
       "juniPppoeProfileSubMotm": juniPppoeProfileSubMotm,
       "juniPppoeProfileSubUrl": juniPppoeProfileSubUrl,
       "juniPppoeProfileDupProtect": juniPppoeProfileDupProtect,
       "juniPppoeProfileAcName": juniPppoeProfileAcName,
       "juniPppoeProfilePadiFlag": juniPppoeProfilePadiFlag,
       "juniPppoeProfilePacketTrace": juniPppoeProfilePacketTrace,
       "juniPppoeProfileServiceNameTableName": juniPppoeProfileServiceNameTableName,
       "juniPppoeProfilePadrRemoteCircuitIdCapture": juniPppoeProfilePadrRemoteCircuitIdCapture,
       "juniPppoeProfileMtu": juniPppoeProfileMtu,
       "juniPppoeProfileMaxSessionOverride": juniPppoeProfileMaxSessionOverride,
       "juniPppoeProfileConformance": juniPppoeProfileConformance,
       "juniPppoeProfileCompliances": juniPppoeProfileCompliances,
       "juniPppoeProfileCompliance": juniPppoeProfileCompliance,
       "juniPppoeCompliance2": juniPppoeCompliance2,
       "juniPppoeCompliance3": juniPppoeCompliance3,
       "juniPppoeCompliance4": juniPppoeCompliance4,
       "juniPppoeCompliance5": juniPppoeCompliance5,
       "juniPppoeCompliance6": juniPppoeCompliance6,
       "juniPppoeCompliance7": juniPppoeCompliance7,
       "juniPppoeProfileGroups": juniPppoeProfileGroups,
       "juniPppoeProfileGroup": juniPppoeProfileGroup,
       "juniPppoeProfileGroup2": juniPppoeProfileGroup2,
       "juniPppoeProfileGroup3": juniPppoeProfileGroup3,
       "juniPppoeProfileGroup4": juniPppoeProfileGroup4,
       "juniPppoeProfileGroup5": juniPppoeProfileGroup5,
       "juniPppoeProfileGroup6": juniPppoeProfileGroup6,
       "juniPppoeProfileGroup7": juniPppoeProfileGroup7}
)
