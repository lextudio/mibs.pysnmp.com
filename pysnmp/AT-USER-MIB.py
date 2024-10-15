# SNMP MIB module (AT-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-USER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:36 2024
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

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "sysinfo")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

user = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20)
)
user.setRevisions(
        ("2012-09-21 00:00",
         "2010-09-07 00:00",
         "2010-06-15 00:15",
         "2010-06-08 00:00",
         "2008-10-16 12:00",
         "2008-08-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UserInfoTable_Object = MibTable
userInfoTable = _UserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1)
)
if mibBuilder.loadTexts:
    userInfoTable.setStatus("current")
_UserInfoEntry_Object = MibTableRow
userInfoEntry = _UserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1)
)
userInfoEntry.setIndexNames(
    (0, "AT-USER-MIB", "userInfoType"),
    (0, "AT-USER-MIB", "userInfoIndex"),
)
if mibBuilder.loadTexts:
    userInfoEntry.setStatus("current")


class _UserInfoType_Type(Integer32):
    """Custom type userInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aux", 2),
          ("console", 1),
          ("script", 4),
          ("stack", 5),
          ("telnet", 3))
    )


_UserInfoType_Type.__name__ = "Integer32"
_UserInfoType_Object = MibTableColumn
userInfoType = _UserInfoType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 1),
    _UserInfoType_Type()
)
userInfoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userInfoType.setStatus("current")


class _UserInfoIndex_Type(Unsigned32):
    """Custom type userInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_UserInfoIndex_Type.__name__ = "Unsigned32"
_UserInfoIndex_Object = MibTableColumn
userInfoIndex = _UserInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 2),
    _UserInfoIndex_Type()
)
userInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userInfoIndex.setStatus("current")
_UserInfoUserName_Type = DisplayString
_UserInfoUserName_Object = MibTableColumn
userInfoUserName = _UserInfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 3),
    _UserInfoUserName_Type()
)
userInfoUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoUserName.setStatus("current")


class _UserInfoPrivilegeLevel_Type(Unsigned32):
    """Custom type userInfoPrivilegeLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_UserInfoPrivilegeLevel_Type.__name__ = "Unsigned32"
_UserInfoPrivilegeLevel_Object = MibTableColumn
userInfoPrivilegeLevel = _UserInfoPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 4),
    _UserInfoPrivilegeLevel_Type()
)
userInfoPrivilegeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoPrivilegeLevel.setStatus("current")
_UserInfoIdleTime_Type = DisplayString
_UserInfoIdleTime_Object = MibTableColumn
userInfoIdleTime = _UserInfoIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 5),
    _UserInfoIdleTime_Type()
)
userInfoIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoIdleTime.setStatus("current")
_UserInfoLocation_Type = DisplayString
_UserInfoLocation_Object = MibTableColumn
userInfoLocation = _UserInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 6),
    _UserInfoLocation_Type()
)
userInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoLocation.setStatus("current")
_UserInfoPasswordLifetime_Type = DisplayString
_UserInfoPasswordLifetime_Object = MibTableColumn
userInfoPasswordLifetime = _UserInfoPasswordLifetime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 7),
    _UserInfoPasswordLifetime_Type()
)
userInfoPasswordLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoPasswordLifetime.setStatus("current")
_UserInfoPasswordLastChange_Type = DisplayString
_UserInfoPasswordLastChange_Object = MibTableColumn
userInfoPasswordLastChange = _UserInfoPasswordLastChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 8),
    _UserInfoPasswordLastChange_Type()
)
userInfoPasswordLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userInfoPasswordLastChange.setStatus("current")
_UserConfigTable_Object = MibTable
userConfigTable = _UserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2)
)
if mibBuilder.loadTexts:
    userConfigTable.setStatus("current")
_UserConfigEntry_Object = MibTableRow
userConfigEntry = _UserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1)
)
userConfigEntry.setIndexNames(
    (0, "AT-USER-MIB", "userConfigIndex"),
)
if mibBuilder.loadTexts:
    userConfigEntry.setStatus("current")
_UserConfigIndex_Type = Unsigned32
_UserConfigIndex_Object = MibTableColumn
userConfigIndex = _UserConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 1),
    _UserConfigIndex_Type()
)
userConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userConfigIndex.setStatus("current")
_UserConfigUsername_Type = DisplayString
_UserConfigUsername_Object = MibTableColumn
userConfigUsername = _UserConfigUsername_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 2),
    _UserConfigUsername_Type()
)
userConfigUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userConfigUsername.setStatus("current")


class _UserConfigPrivilegeLevel_Type(Unsigned32):
    """Custom type userConfigPrivilegeLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_UserConfigPrivilegeLevel_Type.__name__ = "Unsigned32"
_UserConfigPrivilegeLevel_Object = MibTableColumn
userConfigPrivilegeLevel = _UserConfigPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 3),
    _UserConfigPrivilegeLevel_Type()
)
userConfigPrivilegeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userConfigPrivilegeLevel.setStatus("current")
_UserSecurityPasswordRules_ObjectIdentity = ObjectIdentity
userSecurityPasswordRules = _UserSecurityPasswordRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3)
)
_UserSecurityPasswordHistory_Type = DisplayString
_UserSecurityPasswordHistory_Object = MibScalar
userSecurityPasswordHistory = _UserSecurityPasswordHistory_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 1),
    _UserSecurityPasswordHistory_Type()
)
userSecurityPasswordHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityPasswordHistory.setStatus("current")
_UserSecurityPasswordLifetime_Type = DisplayString
_UserSecurityPasswordLifetime_Object = MibScalar
userSecurityPasswordLifetime = _UserSecurityPasswordLifetime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 2),
    _UserSecurityPasswordLifetime_Type()
)
userSecurityPasswordLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityPasswordLifetime.setStatus("current")
_UserSecurityPasswordWarning_Type = DisplayString
_UserSecurityPasswordWarning_Object = MibScalar
userSecurityPasswordWarning = _UserSecurityPasswordWarning_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 3),
    _UserSecurityPasswordWarning_Type()
)
userSecurityPasswordWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityPasswordWarning.setStatus("current")


class _UserSecurityPasswordMinLength_Type(Unsigned32):
    """Custom type userSecurityPasswordMinLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_UserSecurityPasswordMinLength_Type.__name__ = "Unsigned32"
_UserSecurityPasswordMinLength_Object = MibScalar
userSecurityPasswordMinLength = _UserSecurityPasswordMinLength_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 4),
    _UserSecurityPasswordMinLength_Type()
)
userSecurityPasswordMinLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityPasswordMinLength.setStatus("current")


class _UserSecurityPasswordMinCategory_Type(Unsigned32):
    """Custom type userSecurityPasswordMinCategory based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UserSecurityPasswordMinCategory_Type.__name__ = "Unsigned32"
_UserSecurityPasswordMinCategory_Object = MibScalar
userSecurityPasswordMinCategory = _UserSecurityPasswordMinCategory_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 5),
    _UserSecurityPasswordMinCategory_Type()
)
userSecurityPasswordMinCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityPasswordMinCategory.setStatus("current")


class _UserSecurityPasswordForced_Type(Integer32):
    """Custom type userSecurityPasswordForced based on Integer32"""
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


_UserSecurityPasswordForced_Type.__name__ = "Integer32"
_UserSecurityPasswordForced_Object = MibScalar
userSecurityPasswordForced = _UserSecurityPasswordForced_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 6),
    _UserSecurityPasswordForced_Type()
)
userSecurityPasswordForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityPasswordForced.setStatus("current")


class _UserSecurityPasswordReject_Type(Integer32):
    """Custom type userSecurityPasswordReject based on Integer32"""
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


_UserSecurityPasswordReject_Type.__name__ = "Integer32"
_UserSecurityPasswordReject_Object = MibScalar
userSecurityPasswordReject = _UserSecurityPasswordReject_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 7),
    _UserSecurityPasswordReject_Type()
)
userSecurityPasswordReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityPasswordReject.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-USER-MIB",
    **{"user": user,
       "userInfoTable": userInfoTable,
       "userInfoEntry": userInfoEntry,
       "userInfoType": userInfoType,
       "userInfoIndex": userInfoIndex,
       "userInfoUserName": userInfoUserName,
       "userInfoPrivilegeLevel": userInfoPrivilegeLevel,
       "userInfoIdleTime": userInfoIdleTime,
       "userInfoLocation": userInfoLocation,
       "userInfoPasswordLifetime": userInfoPasswordLifetime,
       "userInfoPasswordLastChange": userInfoPasswordLastChange,
       "userConfigTable": userConfigTable,
       "userConfigEntry": userConfigEntry,
       "userConfigIndex": userConfigIndex,
       "userConfigUsername": userConfigUsername,
       "userConfigPrivilegeLevel": userConfigPrivilegeLevel,
       "userSecurityPasswordRules": userSecurityPasswordRules,
       "userSecurityPasswordHistory": userSecurityPasswordHistory,
       "userSecurityPasswordLifetime": userSecurityPasswordLifetime,
       "userSecurityPasswordWarning": userSecurityPasswordWarning,
       "userSecurityPasswordMinLength": userSecurityPasswordMinLength,
       "userSecurityPasswordMinCategory": userSecurityPasswordMinCategory,
       "userSecurityPasswordForced": userSecurityPasswordForced,
       "userSecurityPasswordReject": userSecurityPasswordReject}
)
