# SNMP MIB module (ALCATEL-IND1-SESSION-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-SESSION-MGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:04 2024
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

(softentIND1Sesmgr,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Sesmgr")

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


# MODULE-IDENTITY

alcatelIND1SessionMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1)
)
alcatelIND1SessionMgrMIB.setRevisions(
        ("2010-05-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1SessionMgrMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1SessionMgrMIBNotifications = _AlcatelIND1SessionMgrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1SessionMgrMIBNotifications.setStatus("current")
_AlcatelIND1SessionMgrMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1SessionMgrMIBObjects = _AlcatelIND1SessionMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SessionMgrMIBObjects.setStatus("current")
_SessionMgr_ObjectIdentity = ObjectIdentity
sessionMgr = _SessionMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1)
)
_SessionConfigTable_Object = MibTable
sessionConfigTable = _SessionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sessionConfigTable.setStatus("current")
_SessionConfigEntry_Object = MibTableRow
sessionConfigEntry = _SessionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 1, 1)
)
sessionConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-SESSION-MGR-MIB", "sessionType"),
)
if mibBuilder.loadTexts:
    sessionConfigEntry.setStatus("current")


class _SessionType_Type(Integer32):
    """Custom type sessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cli", 1),
          ("ftp", 3),
          ("http", 2))
    )


_SessionType_Type.__name__ = "Integer32"
_SessionType_Object = MibTableColumn
sessionType = _SessionType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 1, 1, 1),
    _SessionType_Type()
)
sessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionType.setStatus("current")


class _SessionBannerFileName_Type(SnmpAdminString):
    """Custom type sessionBannerFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SessionBannerFileName_Type.__name__ = "SnmpAdminString"
_SessionBannerFileName_Object = MibTableColumn
sessionBannerFileName = _SessionBannerFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 1, 1, 2),
    _SessionBannerFileName_Type()
)
sessionBannerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionBannerFileName.setStatus("current")


class _SessionInactivityTimerValue_Type(Integer32):
    """Custom type sessionInactivityTimerValue based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 596523),
    )


_SessionInactivityTimerValue_Type.__name__ = "Integer32"
_SessionInactivityTimerValue_Object = MibTableColumn
sessionInactivityTimerValue = _SessionInactivityTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 1, 1, 3),
    _SessionInactivityTimerValue_Type()
)
sessionInactivityTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionInactivityTimerValue.setStatus("current")


class _SessionDefaultPromptString_Type(SnmpAdminString):
    """Custom type sessionDefaultPromptString based on SnmpAdminString"""
    defaultValue = OctetString("-> ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SessionDefaultPromptString_Type.__name__ = "SnmpAdminString"
_SessionDefaultPromptString_Object = MibTableColumn
sessionDefaultPromptString = _SessionDefaultPromptString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 1, 1, 4),
    _SessionDefaultPromptString_Type()
)
sessionDefaultPromptString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionDefaultPromptString.setStatus("current")
_SessionActiveTable_Object = MibTable
sessionActiveTable = _SessionActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sessionActiveTable.setStatus("current")
_SessionActiveEntry_Object = MibTableRow
sessionActiveEntry = _SessionActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1)
)
sessionActiveEntry.setIndexNames(
    (0, "ALCATEL-IND1-SESSION-MGR-MIB", "sessionIndex"),
)
if mibBuilder.loadTexts:
    sessionActiveEntry.setStatus("current")


class _SessionIndex_Type(Integer32):
    """Custom type sessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SessionIndex_Type.__name__ = "Integer32"
_SessionIndex_Object = MibTableColumn
sessionIndex = _SessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1, 1),
    _SessionIndex_Type()
)
sessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionIndex.setStatus("current")


class _SessionAccessType_Type(Integer32):
    """Custom type sessionAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("ftp", 3),
          ("http", 4),
          ("https", 6),
          ("ssh", 5),
          ("telnet", 2))
    )


_SessionAccessType_Type.__name__ = "Integer32"
_SessionAccessType_Object = MibTableColumn
sessionAccessType = _SessionAccessType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1, 2),
    _SessionAccessType_Type()
)
sessionAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionAccessType.setStatus("current")


class _SessionPhysicalPort_Type(Integer32):
    """Custom type sessionPhysicalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ether", 2),
          ("local", 1),
          ("notSignificant", 0))
    )


_SessionPhysicalPort_Type.__name__ = "Integer32"
_SessionPhysicalPort_Object = MibTableColumn
sessionPhysicalPort = _SessionPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1, 3),
    _SessionPhysicalPort_Type()
)
sessionPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionPhysicalPort.setStatus("current")


class _SessionUserName_Type(SnmpAdminString):
    """Custom type sessionUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SessionUserName_Type.__name__ = "SnmpAdminString"
_SessionUserName_Object = MibTableColumn
sessionUserName = _SessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1, 4),
    _SessionUserName_Type()
)
sessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionUserName.setStatus("current")


class _SessionUserReadPrivileges_Type(OctetString):
    """Custom type sessionUserReadPrivileges based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SessionUserReadPrivileges_Type.__name__ = "OctetString"
_SessionUserReadPrivileges_Object = MibTableColumn
sessionUserReadPrivileges = _SessionUserReadPrivileges_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1, 5),
    _SessionUserReadPrivileges_Type()
)
sessionUserReadPrivileges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionUserReadPrivileges.setStatus("current")


class _SessionUserWritePrivileges_Type(OctetString):
    """Custom type sessionUserWritePrivileges based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SessionUserWritePrivileges_Type.__name__ = "OctetString"
_SessionUserWritePrivileges_Object = MibTableColumn
sessionUserWritePrivileges = _SessionUserWritePrivileges_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1, 6),
    _SessionUserWritePrivileges_Type()
)
sessionUserWritePrivileges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionUserWritePrivileges.setStatus("current")


class _SessionUserProfileName_Type(SnmpAdminString):
    """Custom type sessionUserProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SessionUserProfileName_Type.__name__ = "SnmpAdminString"
_SessionUserProfileName_Object = MibTableColumn
sessionUserProfileName = _SessionUserProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1, 7),
    _SessionUserProfileName_Type()
)
sessionUserProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionUserProfileName.setStatus("obsolete")
_SessionUserIpAddress_Type = IpAddress
_SessionUserIpAddress_Object = MibTableColumn
sessionUserIpAddress = _SessionUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1, 8),
    _SessionUserIpAddress_Type()
)
sessionUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionUserIpAddress.setStatus("current")
_SessionRowStatus_Type = RowStatus
_SessionRowStatus_Object = MibTableColumn
sessionRowStatus = _SessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 2, 1, 9),
    _SessionRowStatus_Type()
)
sessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sessionRowStatus.setStatus("current")


class _SessionLoginTimeout_Type(Integer32):
    """Custom type sessionLoginTimeout based on Integer32"""
    defaultValue = 55

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_SessionLoginTimeout_Type.__name__ = "Integer32"
_SessionLoginTimeout_Object = MibScalar
sessionLoginTimeout = _SessionLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 3),
    _SessionLoginTimeout_Type()
)
sessionLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLoginTimeout.setStatus("current")


class _SessionLoginAttempt_Type(Integer32):
    """Custom type sessionLoginAttempt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SessionLoginAttempt_Type.__name__ = "Integer32"
_SessionLoginAttempt_Object = MibScalar
sessionLoginAttempt = _SessionLoginAttempt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 4),
    _SessionLoginAttempt_Type()
)
sessionLoginAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLoginAttempt.setStatus("current")


class _SessionCliCommandLogEnable_Type(Integer32):
    """Custom type sessionCliCommandLogEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SessionCliCommandLogEnable_Type.__name__ = "Integer32"
_SessionCliCommandLogEnable_Object = MibScalar
sessionCliCommandLogEnable = _SessionCliCommandLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 5),
    _SessionCliCommandLogEnable_Type()
)
sessionCliCommandLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionCliCommandLogEnable.setStatus("current")


class _SessionXonXoffEnable_Type(Integer32):
    """Custom type sessionXonXoffEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SessionXonXoffEnable_Type.__name__ = "Integer32"
_SessionXonXoffEnable_Object = MibScalar
sessionXonXoffEnable = _SessionXonXoffEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 6),
    _SessionXonXoffEnable_Type()
)
sessionXonXoffEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionXonXoffEnable.setStatus("current")
_SwitchMgtTrapsObj_ObjectIdentity = ObjectIdentity
switchMgtTrapsObj = _SwitchMgtTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 7)
)


class _SessionAuthFailure_Type(Integer32):
    """Custom type sessionAuthFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unknownUser", 1)
    )


_SessionAuthFailure_Type.__name__ = "Integer32"
_SessionAuthFailure_Object = MibScalar
sessionAuthFailure = _SessionAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 1, 1, 7, 1),
    _SessionAuthFailure_Type()
)
sessionAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionAuthFailure.setStatus("current")
_AlcatelIND1SessionMgrMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1SessionMgrMIBConformance = _AlcatelIND1SessionMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SessionMgrMIBConformance.setStatus("current")
_AlcatelIND1SessionMgrMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1SessionMgrMIBGroups = _AlcatelIND1SessionMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SessionMgrMIBGroups.setStatus("current")
_AlcatelIND1SessionMgrMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1SessionMgrMIBCompliances = _AlcatelIND1SessionMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SessionMgrMIBCompliances.setStatus("current")

# Managed Objects groups

sessionConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 2, 1, 1)
)
sessionConfigGroup.setObjects(
      *(("ALCATEL-IND1-SESSION-MGR-MIB", "sessionType"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionBannerFileName"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionInactivityTimerValue"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionDefaultPromptString"))
)
if mibBuilder.loadTexts:
    sessionConfigGroup.setStatus("current")

sessionActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 2, 1, 2)
)
sessionActiveGroup.setObjects(
      *(("ALCATEL-IND1-SESSION-MGR-MIB", "sessionIndex"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionAccessType"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionPhysicalPort"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionUserName"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionUserReadPrivileges"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionUserWritePrivileges"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionUserProfileName"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionUserIpAddress"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionRowStatus"))
)
if mibBuilder.loadTexts:
    sessionActiveGroup.setStatus("current")

sessionObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 2, 1, 4)
)
sessionObjectGroup.setObjects(
      *(("ALCATEL-IND1-SESSION-MGR-MIB", "sessionLoginTimeout"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionLoginAttempt"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionCliCommandLogEnable"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionXonXoffEnable"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionAuthFailure"))
)
if mibBuilder.loadTexts:
    sessionObjectGroup.setStatus("current")


# Notification objects

sessionAuthenticationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 0, 1)
)
sessionAuthenticationTrap.setObjects(
      *(("ALCATEL-IND1-SESSION-MGR-MIB", "sessionAccessType"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionUserName"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionUserIpAddress"),
        ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionAuthFailure"))
)
if mibBuilder.loadTexts:
    sessionAuthenticationTrap.setStatus(
        "current"
    )


# Notifications groups

sessionTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 2, 1, 3)
)
sessionTrapsGroup.setObjects(
    ("ALCATEL-IND1-SESSION-MGR-MIB", "sessionAuthenticationTrap")
)
if mibBuilder.loadTexts:
    sessionTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1SessionMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SessionMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-SESSION-MGR-MIB",
    **{"alcatelIND1SessionMgrMIB": alcatelIND1SessionMgrMIB,
       "alcatelIND1SessionMgrMIBNotifications": alcatelIND1SessionMgrMIBNotifications,
       "sessionAuthenticationTrap": sessionAuthenticationTrap,
       "alcatelIND1SessionMgrMIBObjects": alcatelIND1SessionMgrMIBObjects,
       "sessionMgr": sessionMgr,
       "sessionConfigTable": sessionConfigTable,
       "sessionConfigEntry": sessionConfigEntry,
       "sessionType": sessionType,
       "sessionBannerFileName": sessionBannerFileName,
       "sessionInactivityTimerValue": sessionInactivityTimerValue,
       "sessionDefaultPromptString": sessionDefaultPromptString,
       "sessionActiveTable": sessionActiveTable,
       "sessionActiveEntry": sessionActiveEntry,
       "sessionIndex": sessionIndex,
       "sessionAccessType": sessionAccessType,
       "sessionPhysicalPort": sessionPhysicalPort,
       "sessionUserName": sessionUserName,
       "sessionUserReadPrivileges": sessionUserReadPrivileges,
       "sessionUserWritePrivileges": sessionUserWritePrivileges,
       "sessionUserProfileName": sessionUserProfileName,
       "sessionUserIpAddress": sessionUserIpAddress,
       "sessionRowStatus": sessionRowStatus,
       "sessionLoginTimeout": sessionLoginTimeout,
       "sessionLoginAttempt": sessionLoginAttempt,
       "sessionCliCommandLogEnable": sessionCliCommandLogEnable,
       "sessionXonXoffEnable": sessionXonXoffEnable,
       "switchMgtTrapsObj": switchMgtTrapsObj,
       "sessionAuthFailure": sessionAuthFailure,
       "alcatelIND1SessionMgrMIBConformance": alcatelIND1SessionMgrMIBConformance,
       "alcatelIND1SessionMgrMIBGroups": alcatelIND1SessionMgrMIBGroups,
       "sessionConfigGroup": sessionConfigGroup,
       "sessionActiveGroup": sessionActiveGroup,
       "sessionTrapsGroup": sessionTrapsGroup,
       "sessionObjectGroup": sessionObjectGroup,
       "alcatelIND1SessionMgrMIBCompliances": alcatelIND1SessionMgrMIBCompliances,
       "alcatelIND1SessionMgrMIBCompliance": alcatelIND1SessionMgrMIBCompliance}
)
