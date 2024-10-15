# SNMP MIB module (Unisphere-Data-PPPOE-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-PPPOE-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:21 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,
 UsdSetMap) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable",
    "UsdSetMap")


# MODULE-IDENTITY

usdPppoeProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46)
)
usdPppoeProfileMIB.setRevisions(
        ("2002-08-15 20:34",
         "2002-08-15 19:07",
         "2001-03-21 18:32")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdPppoeProfileObjects_ObjectIdentity = ObjectIdentity
usdPppoeProfileObjects = _UsdPppoeProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1)
)
_UsdPppoeProfile_ObjectIdentity = ObjectIdentity
usdPppoeProfile = _UsdPppoeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1)
)
_UsdPppoeProfileTable_Object = MibTable
usdPppoeProfileTable = _UsdPppoeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdPppoeProfileTable.setStatus("current")
_UsdPppoeProfileEntry_Object = MibTableRow
usdPppoeProfileEntry = _UsdPppoeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1)
)
usdPppoeProfileEntry.setIndexNames(
    (0, "Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileId"),
)
if mibBuilder.loadTexts:
    usdPppoeProfileEntry.setStatus("current")
_UsdPppoeProfileId_Type = Unsigned32
_UsdPppoeProfileId_Object = MibTableColumn
usdPppoeProfileId = _UsdPppoeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 1),
    _UsdPppoeProfileId_Type()
)
usdPppoeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPppoeProfileId.setStatus("current")
_UsdPppoeProfileSetMap_Type = UsdSetMap
_UsdPppoeProfileSetMap_Object = MibTableColumn
usdPppoeProfileSetMap = _UsdPppoeProfileSetMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 2),
    _UsdPppoeProfileSetMap_Type()
)
usdPppoeProfileSetMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppoeProfileSetMap.setStatus("current")


class _UsdPppoeProfileMaxNumSessions_Type(Integer32):
    """Custom type usdPppoeProfileMaxNumSessions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdPppoeProfileMaxNumSessions_Type.__name__ = "Integer32"
_UsdPppoeProfileMaxNumSessions_Object = MibTableColumn
usdPppoeProfileMaxNumSessions = _UsdPppoeProfileMaxNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 3),
    _UsdPppoeProfileMaxNumSessions_Type()
)
usdPppoeProfileMaxNumSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppoeProfileMaxNumSessions.setStatus("current")


class _UsdPppoeProfileSubMotm_Type(DisplayString):
    """Custom type usdPppoeProfileSubMotm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UsdPppoeProfileSubMotm_Type.__name__ = "DisplayString"
_UsdPppoeProfileSubMotm_Object = MibTableColumn
usdPppoeProfileSubMotm = _UsdPppoeProfileSubMotm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 4),
    _UsdPppoeProfileSubMotm_Type()
)
usdPppoeProfileSubMotm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppoeProfileSubMotm.setStatus("current")


class _UsdPppoeProfileSubUrl_Type(DisplayString):
    """Custom type usdPppoeProfileSubUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UsdPppoeProfileSubUrl_Type.__name__ = "DisplayString"
_UsdPppoeProfileSubUrl_Object = MibTableColumn
usdPppoeProfileSubUrl = _UsdPppoeProfileSubUrl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 5),
    _UsdPppoeProfileSubUrl_Type()
)
usdPppoeProfileSubUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppoeProfileSubUrl.setStatus("current")


class _UsdPppoeProfileDupProtect_Type(UsdEnable):
    """Custom type usdPppoeProfileDupProtect based on UsdEnable"""


_UsdPppoeProfileDupProtect_Object = MibTableColumn
usdPppoeProfileDupProtect = _UsdPppoeProfileDupProtect_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 6),
    _UsdPppoeProfileDupProtect_Type()
)
usdPppoeProfileDupProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppoeProfileDupProtect.setStatus("current")


class _UsdPppoeProfileAcName_Type(DisplayString):
    """Custom type usdPppoeProfileAcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UsdPppoeProfileAcName_Type.__name__ = "DisplayString"
_UsdPppoeProfileAcName_Object = MibTableColumn
usdPppoeProfileAcName = _UsdPppoeProfileAcName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 7),
    _UsdPppoeProfileAcName_Type()
)
usdPppoeProfileAcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppoeProfileAcName.setStatus("current")


class _UsdPppoeProfilePadiFlag_Type(UsdEnable):
    """Custom type usdPppoeProfilePadiFlag based on UsdEnable"""


_UsdPppoeProfilePadiFlag_Object = MibTableColumn
usdPppoeProfilePadiFlag = _UsdPppoeProfilePadiFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 8),
    _UsdPppoeProfilePadiFlag_Type()
)
usdPppoeProfilePadiFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppoeProfilePadiFlag.setStatus("current")


class _UsdPppoeProfilePacketTrace_Type(UsdEnable):
    """Custom type usdPppoeProfilePacketTrace based on UsdEnable"""


_UsdPppoeProfilePacketTrace_Object = MibTableColumn
usdPppoeProfilePacketTrace = _UsdPppoeProfilePacketTrace_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 9),
    _UsdPppoeProfilePacketTrace_Type()
)
usdPppoeProfilePacketTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppoeProfilePacketTrace.setStatus("current")
_UsdPppoeProfileConformance_ObjectIdentity = ObjectIdentity
usdPppoeProfileConformance = _UsdPppoeProfileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4)
)
_UsdPppoeProfileCompliances_ObjectIdentity = ObjectIdentity
usdPppoeProfileCompliances = _UsdPppoeProfileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1)
)
_UsdPppoeProfileGroups_ObjectIdentity = ObjectIdentity
usdPppoeProfileGroups = _UsdPppoeProfileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2)
)

# Managed Objects groups

usdPppoeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 1)
)
usdPppoeProfileGroup.setObjects(
      *(("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSetMap"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileMaxNumSessions"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubMotm"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubUrl"))
)
if mibBuilder.loadTexts:
    usdPppoeProfileGroup.setStatus("obsolete")

usdPppoeProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 2)
)
usdPppoeProfileGroup2.setObjects(
      *(("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSetMap"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileMaxNumSessions"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubMotm"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubUrl"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileDupProtect"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileAcName"))
)
if mibBuilder.loadTexts:
    usdPppoeProfileGroup2.setStatus("obsolete")

usdPppoeProfileGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 3)
)
usdPppoeProfileGroup3.setObjects(
      *(("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSetMap"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileMaxNumSessions"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubMotm"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubUrl"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileDupProtect"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileAcName"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfilePadiFlag"),
        ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfilePacketTrace"))
)
if mibBuilder.loadTexts:
    usdPppoeProfileGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdPppoeProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdPppoeProfileCompliance.setStatus(
        "obsolete"
    )

usdPppoeCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdPppoeCompliance2.setStatus(
        "obsolete"
    )

usdPppoeCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdPppoeCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-PPPOE-PROFILE-MIB",
    **{"usdPppoeProfileMIB": usdPppoeProfileMIB,
       "usdPppoeProfileObjects": usdPppoeProfileObjects,
       "usdPppoeProfile": usdPppoeProfile,
       "usdPppoeProfileTable": usdPppoeProfileTable,
       "usdPppoeProfileEntry": usdPppoeProfileEntry,
       "usdPppoeProfileId": usdPppoeProfileId,
       "usdPppoeProfileSetMap": usdPppoeProfileSetMap,
       "usdPppoeProfileMaxNumSessions": usdPppoeProfileMaxNumSessions,
       "usdPppoeProfileSubMotm": usdPppoeProfileSubMotm,
       "usdPppoeProfileSubUrl": usdPppoeProfileSubUrl,
       "usdPppoeProfileDupProtect": usdPppoeProfileDupProtect,
       "usdPppoeProfileAcName": usdPppoeProfileAcName,
       "usdPppoeProfilePadiFlag": usdPppoeProfilePadiFlag,
       "usdPppoeProfilePacketTrace": usdPppoeProfilePacketTrace,
       "usdPppoeProfileConformance": usdPppoeProfileConformance,
       "usdPppoeProfileCompliances": usdPppoeProfileCompliances,
       "usdPppoeProfileCompliance": usdPppoeProfileCompliance,
       "usdPppoeCompliance2": usdPppoeCompliance2,
       "usdPppoeCompliance3": usdPppoeCompliance3,
       "usdPppoeProfileGroups": usdPppoeProfileGroups,
       "usdPppoeProfileGroup": usdPppoeProfileGroup,
       "usdPppoeProfileGroup2": usdPppoeProfileGroup2,
       "usdPppoeProfileGroup3": usdPppoeProfileGroup3}
)
