# SNMP MIB module (HM2-USERMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-USERMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:31 2024
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

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

hm2UserMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24)
)
hm2UserMgmtMib.setRevisions(
        ("2011-03-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2UserAccessRoles(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              6,
              7,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 15),
          ("auditor", 2),
          ("custom1", 5),
          ("custom2", 6),
          ("custom3", 7),
          ("guest", 1),
          ("operator", 13),
          ("unauthorized", 0))
    )



class Hm2UserAuthList(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              7,
              9,
              10,
              248,
              300)
        )
    )
    namedValues = NamedValues(
        *(("cam", 9),
          ("ias", 7),
          ("ldap", 10),
          ("local", 3),
          ("none", 300),
          ("radius", 5),
          ("reject", 248))
    )



class Hm2UserCustomAccessRoles(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("custom1", 5),
          ("custom2", 6),
          ("custom3", 7))
    )



class Hm2UserCliExecModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("all-modes", 10),
          ("global-config-exec-mode", 3),
          ("interface-exec-mode", 5),
          ("priv-exec-mode", 2),
          ("user-exec-mode", 1),
          ("vlan-database-exec-mode", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2UserMgmtMibNotifications_ObjectIdentity = ObjectIdentity
hm2UserMgmtMibNotifications = _Hm2UserMgmtMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 0)
)
_Hm2UserMgmtMibObjects_ObjectIdentity = ObjectIdentity
hm2UserMgmtMibObjects = _Hm2UserMgmtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1)
)
_Hm2UserConfigGroup_ObjectIdentity = ObjectIdentity
hm2UserConfigGroup = _Hm2UserConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1)
)
_Hm2UserConfigTable_Object = MibTable
hm2UserConfigTable = _Hm2UserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hm2UserConfigTable.setStatus("current")
_Hm2UserConfigEntry_Object = MibTableRow
hm2UserConfigEntry = _Hm2UserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1)
)
hm2UserConfigEntry.setIndexNames(
    (1, "HM2-USERMGMT-MIB", "hm2UserName"),
)
if mibBuilder.loadTexts:
    hm2UserConfigEntry.setStatus("current")


class _Hm2UserName_Type(SnmpAdminString):
    """Custom type hm2UserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2UserName_Type.__name__ = "SnmpAdminString"
_Hm2UserName_Object = MibTableColumn
hm2UserName = _Hm2UserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 1),
    _Hm2UserName_Type()
)
hm2UserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2UserName.setStatus("current")


class _Hm2UserPassword_Type(DisplayString):
    """Custom type hm2UserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2UserPassword_Type.__name__ = "DisplayString"
_Hm2UserPassword_Object = MibTableColumn
hm2UserPassword = _Hm2UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 2),
    _Hm2UserPassword_Type()
)
hm2UserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserPassword.setStatus("current")


class _Hm2UserAccessRole_Type(Hm2UserAccessRoles):
    """Custom type hm2UserAccessRole based on Hm2UserAccessRoles"""


_Hm2UserAccessRole_Object = MibTableColumn
hm2UserAccessRole = _Hm2UserAccessRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 3),
    _Hm2UserAccessRole_Type()
)
hm2UserAccessRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserAccessRole.setStatus("current")


class _Hm2UserLockoutStatus_Type(TruthValue):
    """Custom type hm2UserLockoutStatus based on TruthValue"""


_Hm2UserLockoutStatus_Object = MibTableColumn
hm2UserLockoutStatus = _Hm2UserLockoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 4),
    _Hm2UserLockoutStatus_Type()
)
hm2UserLockoutStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserLockoutStatus.setStatus("current")


class _Hm2UserPwdChangePerm_Type(TruthValue):
    """Custom type hm2UserPwdChangePerm based on TruthValue"""


_Hm2UserPwdChangePerm_Object = MibTableColumn
hm2UserPwdChangePerm = _Hm2UserPwdChangePerm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 5),
    _Hm2UserPwdChangePerm_Type()
)
hm2UserPwdChangePerm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserPwdChangePerm.setStatus("current")


class _Hm2UserPwdPolicyChk_Type(HmEnabledStatus):
    """Custom type hm2UserPwdPolicyChk based on HmEnabledStatus"""


_Hm2UserPwdPolicyChk_Object = MibTableColumn
hm2UserPwdPolicyChk = _Hm2UserPwdPolicyChk_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 6),
    _Hm2UserPwdPolicyChk_Type()
)
hm2UserPwdPolicyChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserPwdPolicyChk.setStatus("current")


class _Hm2UserSnmpAuthType_Type(Integer32):
    """Custom type hm2UserSnmpAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacmd5", 1),
          ("hmacsha", 2))
    )


_Hm2UserSnmpAuthType_Type.__name__ = "Integer32"
_Hm2UserSnmpAuthType_Object = MibTableColumn
hm2UserSnmpAuthType = _Hm2UserSnmpAuthType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 7),
    _Hm2UserSnmpAuthType_Type()
)
hm2UserSnmpAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserSnmpAuthType.setStatus("current")


class _Hm2UserSnmpEncType_Type(Integer32):
    """Custom type hm2UserSnmpEncType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aesCfb128", 2),
          ("des", 1),
          ("none", 0))
    )


_Hm2UserSnmpEncType_Type.__name__ = "Integer32"
_Hm2UserSnmpEncType_Object = MibTableColumn
hm2UserSnmpEncType = _Hm2UserSnmpEncType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 8),
    _Hm2UserSnmpEncType_Type()
)
hm2UserSnmpEncType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserSnmpEncType.setStatus("current")
_Hm2UserStatus_Type = RowStatus
_Hm2UserStatus_Object = MibTableColumn
hm2UserStatus = _Hm2UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 9),
    _Hm2UserStatus_Type()
)
hm2UserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserStatus.setStatus("current")
_Hm2UserStatusGroup_ObjectIdentity = ObjectIdentity
hm2UserStatusGroup = _Hm2UserStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 10)
)


class _Hm2UserLastUserCreated_Type(SnmpAdminString):
    """Custom type hm2UserLastUserCreated based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_Hm2UserLastUserCreated_Type.__name__ = "SnmpAdminString"
_Hm2UserLastUserCreated_Object = MibScalar
hm2UserLastUserCreated = _Hm2UserLastUserCreated_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 10, 1),
    _Hm2UserLastUserCreated_Type()
)
hm2UserLastUserCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2UserLastUserCreated.setStatus("current")


class _Hm2UserLastUserDeleted_Type(SnmpAdminString):
    """Custom type hm2UserLastUserDeleted based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_Hm2UserLastUserDeleted_Type.__name__ = "SnmpAdminString"
_Hm2UserLastUserDeleted_Object = MibScalar
hm2UserLastUserDeleted = _Hm2UserLastUserDeleted_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 10, 2),
    _Hm2UserLastUserDeleted_Type()
)
hm2UserLastUserDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2UserLastUserDeleted.setStatus("current")
_Hm2UserCustomGroup_ObjectIdentity = ObjectIdentity
hm2UserCustomGroup = _Hm2UserCustomGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20)
)
_Hm2UserCustomAccessRole2NameTable_Object = MibTable
hm2UserCustomAccessRole2NameTable = _Hm2UserCustomAccessRole2NameTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    hm2UserCustomAccessRole2NameTable.setStatus("current")
_Hm2UserCustomAccessRole2NameEntry_Object = MibTableRow
hm2UserCustomAccessRole2NameEntry = _Hm2UserCustomAccessRole2NameEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1, 1)
)
hm2UserCustomAccessRole2NameEntry.setIndexNames(
    (0, "HM2-USERMGMT-MIB", "hm2UserCustomAccessRole"),
)
if mibBuilder.loadTexts:
    hm2UserCustomAccessRole2NameEntry.setStatus("current")
_Hm2UserCustomAccessRole_Type = Hm2UserCustomAccessRoles
_Hm2UserCustomAccessRole_Object = MibTableColumn
hm2UserCustomAccessRole = _Hm2UserCustomAccessRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1, 1, 1),
    _Hm2UserCustomAccessRole_Type()
)
hm2UserCustomAccessRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2UserCustomAccessRole.setStatus("current")


class _Hm2UserCustomAccessRoleName_Type(SnmpAdminString):
    """Custom type hm2UserCustomAccessRoleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2UserCustomAccessRoleName_Type.__name__ = "SnmpAdminString"
_Hm2UserCustomAccessRoleName_Object = MibTableColumn
hm2UserCustomAccessRoleName = _Hm2UserCustomAccessRoleName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1, 1, 2),
    _Hm2UserCustomAccessRoleName_Type()
)
hm2UserCustomAccessRoleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2UserCustomAccessRoleName.setStatus("current")
_Hm2UserCustomAccessRoleStatus_Type = RowStatus
_Hm2UserCustomAccessRoleStatus_Object = MibTableColumn
hm2UserCustomAccessRoleStatus = _Hm2UserCustomAccessRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1, 1, 3),
    _Hm2UserCustomAccessRoleStatus_Type()
)
hm2UserCustomAccessRoleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserCustomAccessRoleStatus.setStatus("current")
_Hm2UserCustomCliCmdInheritTable_Object = MibTable
hm2UserCustomCliCmdInheritTable = _Hm2UserCustomCliCmdInheritTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    hm2UserCustomCliCmdInheritTable.setStatus("current")
_Hm2UserCustomCliCmdInheritEntry_Object = MibTableRow
hm2UserCustomCliCmdInheritEntry = _Hm2UserCustomCliCmdInheritEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 2, 1)
)
hm2UserCustomCliCmdInheritEntry.setIndexNames(
    (0, "HM2-USERMGMT-MIB", "hm2UserCustomAccessRole"),
)
if mibBuilder.loadTexts:
    hm2UserCustomCliCmdInheritEntry.setStatus("current")


class _Hm2UserCustomCliBaseAccessRole_Type(Hm2UserAccessRoles):
    """Custom type hm2UserCustomCliBaseAccessRole based on Hm2UserAccessRoles"""


_Hm2UserCustomCliBaseAccessRole_Object = MibTableColumn
hm2UserCustomCliBaseAccessRole = _Hm2UserCustomCliBaseAccessRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 2, 1, 1),
    _Hm2UserCustomCliBaseAccessRole_Type()
)
hm2UserCustomCliBaseAccessRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserCustomCliBaseAccessRole.setStatus("current")
_Hm2UserCustomCliBaseAccessRoleStatus_Type = RowStatus
_Hm2UserCustomCliBaseAccessRoleStatus_Object = MibTableColumn
hm2UserCustomCliBaseAccessRoleStatus = _Hm2UserCustomCliBaseAccessRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 2, 1, 2),
    _Hm2UserCustomCliBaseAccessRoleStatus_Type()
)
hm2UserCustomCliBaseAccessRoleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserCustomCliBaseAccessRoleStatus.setStatus("current")
_Hm2UserCustomCliCmdTable_Object = MibTable
hm2UserCustomCliCmdTable = _Hm2UserCustomCliCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3)
)
if mibBuilder.loadTexts:
    hm2UserCustomCliCmdTable.setStatus("current")
_Hm2UserCustomCliCmdEntry_Object = MibTableRow
hm2UserCustomCliCmdEntry = _Hm2UserCustomCliCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1)
)
hm2UserCustomCliCmdEntry.setIndexNames(
    (0, "HM2-USERMGMT-MIB", "hm2UserCustomAccessRole"),
    (0, "HM2-USERMGMT-MIB", "hm2UserCustomCliExecMode"),
    (0, "HM2-USERMGMT-MIB", "hm2UserCustomCliIndex"),
)
if mibBuilder.loadTexts:
    hm2UserCustomCliCmdEntry.setStatus("current")
_Hm2UserCustomCliExecMode_Type = Hm2UserCliExecModes
_Hm2UserCustomCliExecMode_Object = MibTableColumn
hm2UserCustomCliExecMode = _Hm2UserCustomCliExecMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 1),
    _Hm2UserCustomCliExecMode_Type()
)
hm2UserCustomCliExecMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2UserCustomCliExecMode.setStatus("current")


class _Hm2UserCustomCliIndex_Type(Integer32):
    """Custom type hm2UserCustomCliIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hm2UserCustomCliIndex_Type.__name__ = "Integer32"
_Hm2UserCustomCliIndex_Object = MibTableColumn
hm2UserCustomCliIndex = _Hm2UserCustomCliIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 2),
    _Hm2UserCustomCliIndex_Type()
)
hm2UserCustomCliIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2UserCustomCliIndex.setStatus("current")
_Hm2UserCustomCliCommand_Type = SnmpAdminString
_Hm2UserCustomCliCommand_Object = MibTableColumn
hm2UserCustomCliCommand = _Hm2UserCustomCliCommand_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 3),
    _Hm2UserCustomCliCommand_Type()
)
hm2UserCustomCliCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserCustomCliCommand.setStatus("current")


class _Hm2UserCustomCliType_Type(Integer32):
    """Custom type hm2UserCustomCliType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_Hm2UserCustomCliType_Type.__name__ = "Integer32"
_Hm2UserCustomCliType_Object = MibTableColumn
hm2UserCustomCliType = _Hm2UserCustomCliType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 4),
    _Hm2UserCustomCliType_Type()
)
hm2UserCustomCliType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserCustomCliType.setStatus("current")
_Hm2UserCustomCliStatus_Type = RowStatus
_Hm2UserCustomCliStatus_Object = MibTableColumn
hm2UserCustomCliStatus = _Hm2UserCustomCliStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 5),
    _Hm2UserCustomCliStatus_Type()
)
hm2UserCustomCliStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserCustomCliStatus.setStatus("current")
_Hm2PwdMgmtGroup_ObjectIdentity = ObjectIdentity
hm2PwdMgmtGroup = _Hm2PwdMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2)
)


class _Hm2PwdMgmtMinLength_Type(Integer32):
    """Custom type hm2PwdMgmtMinLength based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hm2PwdMgmtMinLength_Type.__name__ = "Integer32"
_Hm2PwdMgmtMinLength_Object = MibScalar
hm2PwdMgmtMinLength = _Hm2PwdMgmtMinLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 1),
    _Hm2PwdMgmtMinLength_Type()
)
hm2PwdMgmtMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PwdMgmtMinLength.setStatus("current")


class _Hm2PwdMgmtLoginAttempts_Type(Integer32):
    """Custom type hm2PwdMgmtLoginAttempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Hm2PwdMgmtLoginAttempts_Type.__name__ = "Integer32"
_Hm2PwdMgmtLoginAttempts_Object = MibScalar
hm2PwdMgmtLoginAttempts = _Hm2PwdMgmtLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 2),
    _Hm2PwdMgmtLoginAttempts_Type()
)
hm2PwdMgmtLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PwdMgmtLoginAttempts.setStatus("current")


class _Hm2PwdMgmtMinUpperCase_Type(Integer32):
    """Custom type hm2PwdMgmtMinUpperCase based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Hm2PwdMgmtMinUpperCase_Type.__name__ = "Integer32"
_Hm2PwdMgmtMinUpperCase_Object = MibScalar
hm2PwdMgmtMinUpperCase = _Hm2PwdMgmtMinUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 3),
    _Hm2PwdMgmtMinUpperCase_Type()
)
hm2PwdMgmtMinUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PwdMgmtMinUpperCase.setStatus("current")


class _Hm2PwdMgmtMinLowerCase_Type(Integer32):
    """Custom type hm2PwdMgmtMinLowerCase based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Hm2PwdMgmtMinLowerCase_Type.__name__ = "Integer32"
_Hm2PwdMgmtMinLowerCase_Object = MibScalar
hm2PwdMgmtMinLowerCase = _Hm2PwdMgmtMinLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 4),
    _Hm2PwdMgmtMinLowerCase_Type()
)
hm2PwdMgmtMinLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PwdMgmtMinLowerCase.setStatus("current")


class _Hm2PwdMgmtMinNumericNumbers_Type(Integer32):
    """Custom type hm2PwdMgmtMinNumericNumbers based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Hm2PwdMgmtMinNumericNumbers_Type.__name__ = "Integer32"
_Hm2PwdMgmtMinNumericNumbers_Object = MibScalar
hm2PwdMgmtMinNumericNumbers = _Hm2PwdMgmtMinNumericNumbers_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 5),
    _Hm2PwdMgmtMinNumericNumbers_Type()
)
hm2PwdMgmtMinNumericNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PwdMgmtMinNumericNumbers.setStatus("current")


class _Hm2PwdMgmtMinSpecialCharacters_Type(Integer32):
    """Custom type hm2PwdMgmtMinSpecialCharacters based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Hm2PwdMgmtMinSpecialCharacters_Type.__name__ = "Integer32"
_Hm2PwdMgmtMinSpecialCharacters_Object = MibScalar
hm2PwdMgmtMinSpecialCharacters = _Hm2PwdMgmtMinSpecialCharacters_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 6),
    _Hm2PwdMgmtMinSpecialCharacters_Type()
)
hm2PwdMgmtMinSpecialCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PwdMgmtMinSpecialCharacters.setStatus("current")
_Hm2PwdMgmtDefaultPwdStatusGroup_ObjectIdentity = ObjectIdentity
hm2PwdMgmtDefaultPwdStatusGroup = _Hm2PwdMgmtDefaultPwdStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100)
)
_Hm2PwdMgmtDefaultPwdActive_Type = TruthValue
_Hm2PwdMgmtDefaultPwdActive_Object = MibScalar
hm2PwdMgmtDefaultPwdActive = _Hm2PwdMgmtDefaultPwdActive_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 1),
    _Hm2PwdMgmtDefaultPwdActive_Type()
)
hm2PwdMgmtDefaultPwdActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PwdMgmtDefaultPwdActive.setStatus("current")
_Hm2PwdMgmtDefaultPwdStatusTable_Object = MibTable
hm2PwdMgmtDefaultPwdStatusTable = _Hm2PwdMgmtDefaultPwdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 100)
)
if mibBuilder.loadTexts:
    hm2PwdMgmtDefaultPwdStatusTable.setStatus("current")
_Hm2PwdMgmtDefaultPwdStatusEntry_Object = MibTableRow
hm2PwdMgmtDefaultPwdStatusEntry = _Hm2PwdMgmtDefaultPwdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 100, 1)
)
hm2PwdMgmtDefaultPwdStatusEntry.setIndexNames(
    (0, "HM2-USERMGMT-MIB", "hm2PwdMgmtDefaultPwdStatusIndex"),
)
if mibBuilder.loadTexts:
    hm2PwdMgmtDefaultPwdStatusEntry.setStatus("current")
_Hm2PwdMgmtDefaultPwdStatusIndex_Type = Integer32
_Hm2PwdMgmtDefaultPwdStatusIndex_Object = MibTableColumn
hm2PwdMgmtDefaultPwdStatusIndex = _Hm2PwdMgmtDefaultPwdStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 100, 1, 1),
    _Hm2PwdMgmtDefaultPwdStatusIndex_Type()
)
hm2PwdMgmtDefaultPwdStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2PwdMgmtDefaultPwdStatusIndex.setStatus("current")
_Hm2PwdMgmtDefaultPwdStatusUserName_Type = SnmpAdminString
_Hm2PwdMgmtDefaultPwdStatusUserName_Object = MibTableColumn
hm2PwdMgmtDefaultPwdStatusUserName = _Hm2PwdMgmtDefaultPwdStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 100, 1, 2),
    _Hm2PwdMgmtDefaultPwdStatusUserName_Type()
)
hm2PwdMgmtDefaultPwdStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PwdMgmtDefaultPwdStatusUserName.setStatus("current")
_Hm2UserApplicationListGroup_ObjectIdentity = ObjectIdentity
hm2UserApplicationListGroup = _Hm2UserApplicationListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3)
)
_Hm2UserApplicationListTable_Object = MibTable
hm2UserApplicationListTable = _Hm2UserApplicationListTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hm2UserApplicationListTable.setStatus("current")
_Hm2UserApplicationListEntry_Object = MibTableRow
hm2UserApplicationListEntry = _Hm2UserApplicationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1, 1)
)
hm2UserApplicationListEntry.setIndexNames(
    (1, "HM2-USERMGMT-MIB", "hm2UserApplicationListName"),
)
if mibBuilder.loadTexts:
    hm2UserApplicationListEntry.setStatus("current")


class _Hm2UserApplicationListName_Type(SnmpAdminString):
    """Custom type hm2UserApplicationListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2UserApplicationListName_Type.__name__ = "SnmpAdminString"
_Hm2UserApplicationListName_Object = MibTableColumn
hm2UserApplicationListName = _Hm2UserApplicationListName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1, 1, 1),
    _Hm2UserApplicationListName_Type()
)
hm2UserApplicationListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2UserApplicationListName.setStatus("current")


class _Hm2UserApplicationListAuthListName_Type(SnmpAdminString):
    """Custom type hm2UserApplicationListAuthListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2UserApplicationListAuthListName_Type.__name__ = "SnmpAdminString"
_Hm2UserApplicationListAuthListName_Object = MibTableColumn
hm2UserApplicationListAuthListName = _Hm2UserApplicationListAuthListName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1, 1, 6),
    _Hm2UserApplicationListAuthListName_Type()
)
hm2UserApplicationListAuthListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserApplicationListAuthListName.setStatus("current")
_Hm2UserApplicationListStatus_Type = RowStatus
_Hm2UserApplicationListStatus_Object = MibTableColumn
hm2UserApplicationListStatus = _Hm2UserApplicationListStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1, 1, 7),
    _Hm2UserApplicationListStatus_Type()
)
hm2UserApplicationListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserApplicationListStatus.setStatus("current")
_Hm2UserAuthListGroup_ObjectIdentity = ObjectIdentity
hm2UserAuthListGroup = _Hm2UserAuthListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4)
)
_Hm2UserAuthListTable_Object = MibTable
hm2UserAuthListTable = _Hm2UserAuthListTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hm2UserAuthListTable.setStatus("current")
_Hm2UserAuthListEntry_Object = MibTableRow
hm2UserAuthListEntry = _Hm2UserAuthListEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1)
)
hm2UserAuthListEntry.setIndexNames(
    (1, "HM2-USERMGMT-MIB", "hm2UserAuthListName"),
)
if mibBuilder.loadTexts:
    hm2UserAuthListEntry.setStatus("current")


class _Hm2UserAuthListName_Type(SnmpAdminString):
    """Custom type hm2UserAuthListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2UserAuthListName_Type.__name__ = "SnmpAdminString"
_Hm2UserAuthListName_Object = MibTableColumn
hm2UserAuthListName = _Hm2UserAuthListName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 1),
    _Hm2UserAuthListName_Type()
)
hm2UserAuthListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2UserAuthListName.setStatus("current")


class _Hm2UserAuthListPolicy1_Type(Hm2UserAuthList):
    """Custom type hm2UserAuthListPolicy1 based on Hm2UserAuthList"""


_Hm2UserAuthListPolicy1_Object = MibTableColumn
hm2UserAuthListPolicy1 = _Hm2UserAuthListPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 2),
    _Hm2UserAuthListPolicy1_Type()
)
hm2UserAuthListPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserAuthListPolicy1.setStatus("current")


class _Hm2UserAuthListPolicy2_Type(Hm2UserAuthList):
    """Custom type hm2UserAuthListPolicy2 based on Hm2UserAuthList"""


_Hm2UserAuthListPolicy2_Object = MibTableColumn
hm2UserAuthListPolicy2 = _Hm2UserAuthListPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 3),
    _Hm2UserAuthListPolicy2_Type()
)
hm2UserAuthListPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserAuthListPolicy2.setStatus("current")


class _Hm2UserAuthListPolicy3_Type(Hm2UserAuthList):
    """Custom type hm2UserAuthListPolicy3 based on Hm2UserAuthList"""


_Hm2UserAuthListPolicy3_Object = MibTableColumn
hm2UserAuthListPolicy3 = _Hm2UserAuthListPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 4),
    _Hm2UserAuthListPolicy3_Type()
)
hm2UserAuthListPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserAuthListPolicy3.setStatus("current")


class _Hm2UserAuthListPolicy4_Type(Hm2UserAuthList):
    """Custom type hm2UserAuthListPolicy4 based on Hm2UserAuthList"""


_Hm2UserAuthListPolicy4_Object = MibTableColumn
hm2UserAuthListPolicy4 = _Hm2UserAuthListPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 5),
    _Hm2UserAuthListPolicy4_Type()
)
hm2UserAuthListPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserAuthListPolicy4.setStatus("current")


class _Hm2UserAuthListPolicy5_Type(Hm2UserAuthList):
    """Custom type hm2UserAuthListPolicy5 based on Hm2UserAuthList"""


_Hm2UserAuthListPolicy5_Object = MibTableColumn
hm2UserAuthListPolicy5 = _Hm2UserAuthListPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 6),
    _Hm2UserAuthListPolicy5_Type()
)
hm2UserAuthListPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserAuthListPolicy5.setStatus("current")
_Hm2UserAuthListStatus_Type = RowStatus
_Hm2UserAuthListStatus_Object = MibTableColumn
hm2UserAuthListStatus = _Hm2UserAuthListStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 7),
    _Hm2UserAuthListStatus_Type()
)
hm2UserAuthListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserAuthListStatus.setStatus("current")
_Hm2UserIasGroup_ObjectIdentity = ObjectIdentity
hm2UserIasGroup = _Hm2UserIasGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5)
)
_Hm2UserIasTable_Object = MibTable
hm2UserIasTable = _Hm2UserIasTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hm2UserIasTable.setStatus("current")
_Hm2UserIasEntry_Object = MibTableRow
hm2UserIasEntry = _Hm2UserIasEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1, 1)
)
hm2UserIasEntry.setIndexNames(
    (1, "HM2-USERMGMT-MIB", "hm2UserIasUserName"),
)
if mibBuilder.loadTexts:
    hm2UserIasEntry.setStatus("current")


class _Hm2UserIasUserName_Type(SnmpAdminString):
    """Custom type hm2UserIasUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2UserIasUserName_Type.__name__ = "SnmpAdminString"
_Hm2UserIasUserName_Object = MibTableColumn
hm2UserIasUserName = _Hm2UserIasUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1, 1, 1),
    _Hm2UserIasUserName_Type()
)
hm2UserIasUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2UserIasUserName.setStatus("current")


class _Hm2UserIasUserPassword_Type(DisplayString):
    """Custom type hm2UserIasUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2UserIasUserPassword_Type.__name__ = "DisplayString"
_Hm2UserIasUserPassword_Object = MibTableColumn
hm2UserIasUserPassword = _Hm2UserIasUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1, 1, 2),
    _Hm2UserIasUserPassword_Type()
)
hm2UserIasUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserIasUserPassword.setStatus("current")
_Hm2UserIasUserStatus_Type = RowStatus
_Hm2UserIasUserStatus_Object = MibTableColumn
hm2UserIasUserStatus = _Hm2UserIasUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1, 1, 3),
    _Hm2UserIasUserStatus_Type()
)
hm2UserIasUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2UserIasUserStatus.setStatus("current")
_Hm2UserMgmtMibSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2UserMgmtMibSNMPExtensionGroup = _Hm2UserMgmtMibSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3)
)
_Hm2UserMgmtGlobalSESGroup_ObjectIdentity = ObjectIdentity
hm2UserMgmtGlobalSESGroup = _Hm2UserMgmtGlobalSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 1)
)
_Hm2UserMgmtGlobalSESLenCharset_ObjectIdentity = ObjectIdentity
hm2UserMgmtGlobalSESLenCharset = _Hm2UserMgmtGlobalSESLenCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hm2UserMgmtGlobalSESLenCharset.setStatus("current")
_Hm2UserMgmtGlobalSESPwdLenCharset_ObjectIdentity = ObjectIdentity
hm2UserMgmtGlobalSESPwdLenCharset = _Hm2UserMgmtGlobalSESPwdLenCharset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hm2UserMgmtGlobalSESPwdLenCharset.setStatus("current")
_Hm2UserMgmtUserSESGroup_ObjectIdentity = ObjectIdentity
hm2UserMgmtUserSESGroup = _Hm2UserMgmtUserSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 2)
)
_Hm2UserMgmtUserSESActivate_ObjectIdentity = ObjectIdentity
hm2UserMgmtUserSESActivate = _Hm2UserMgmtUserSESActivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm2UserMgmtUserSESActivate.setStatus("current")
_Hm2UserMgmtUserSESDeactivate_ObjectIdentity = ObjectIdentity
hm2UserMgmtUserSESDeactivate = _Hm2UserMgmtUserSESDeactivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hm2UserMgmtUserSESDeactivate.setStatus("current")
_Hm2UserMgmtApplSESGroup_ObjectIdentity = ObjectIdentity
hm2UserMgmtApplSESGroup = _Hm2UserMgmtApplSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 3)
)
_Hm2UserMgmtApplSESAddDel_ObjectIdentity = ObjectIdentity
hm2UserMgmtApplSESAddDel = _Hm2UserMgmtApplSESAddDel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hm2UserMgmtApplSESAddDel.setStatus("current")
_Hm2UserMgmtApplSESDeactivate_ObjectIdentity = ObjectIdentity
hm2UserMgmtApplSESDeactivate = _Hm2UserMgmtApplSESDeactivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hm2UserMgmtApplSESDeactivate.setStatus("current")
_Hm2UserMgmtAuthSESGroup_ObjectIdentity = ObjectIdentity
hm2UserMgmtAuthSESGroup = _Hm2UserMgmtAuthSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 4)
)
_Hm2UserMgmtAuthSESDuplPolicy_ObjectIdentity = ObjectIdentity
hm2UserMgmtAuthSESDuplPolicy = _Hm2UserMgmtAuthSESDuplPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 4, 1)
)
if mibBuilder.loadTexts:
    hm2UserMgmtAuthSESDuplPolicy.setStatus("current")
_Hm2UserMgmtAuthSESDeactivate_ObjectIdentity = ObjectIdentity
hm2UserMgmtAuthSESDeactivate = _Hm2UserMgmtAuthSESDeactivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 4, 2)
)
if mibBuilder.loadTexts:
    hm2UserMgmtAuthSESDeactivate.setStatus("current")

# Managed Objects groups


# Notification objects

hm2UserCreatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 1)
)
hm2UserCreatedTrap.setObjects(
    ("HM2-USERMGMT-MIB", "hm2UserLastUserCreated")
)
if mibBuilder.loadTexts:
    hm2UserCreatedTrap.setStatus(
        "current"
    )

hm2UserDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 2)
)
hm2UserDeletedTrap.setObjects(
    ("HM2-USERMGMT-MIB", "hm2UserLastUserDeleted")
)
if mibBuilder.loadTexts:
    hm2UserDeletedTrap.setStatus(
        "current"
    )

hm2UserLockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 3)
)
hm2UserLockedTrap.setObjects(
      *(("HM2-USERMGMT-MIB", "hm2UserName"),
        ("HM2-USERMGMT-MIB", "hm2UserLockoutStatus"))
)
if mibBuilder.loadTexts:
    hm2UserLockedTrap.setStatus(
        "current"
    )

hm2UserPwdChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 4)
)
hm2UserPwdChangedTrap.setObjects(
    ("HM2-USERMGMT-MIB", "hm2UserName")
)
if mibBuilder.loadTexts:
    hm2UserPwdChangedTrap.setStatus(
        "current"
    )

hm2UserPwdPolicyChkChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 5)
)
hm2UserPwdPolicyChkChangedTrap.setObjects(
      *(("HM2-USERMGMT-MIB", "hm2UserName"),
        ("HM2-USERMGMT-MIB", "hm2UserPwdPolicyChk"))
)
if mibBuilder.loadTexts:
    hm2UserPwdPolicyChkChangedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-USERMGMT-MIB",
    **{"Hm2UserAccessRoles": Hm2UserAccessRoles,
       "Hm2UserAuthList": Hm2UserAuthList,
       "Hm2UserCustomAccessRoles": Hm2UserCustomAccessRoles,
       "Hm2UserCliExecModes": Hm2UserCliExecModes,
       "hm2UserMgmtMib": hm2UserMgmtMib,
       "hm2UserMgmtMibNotifications": hm2UserMgmtMibNotifications,
       "hm2UserCreatedTrap": hm2UserCreatedTrap,
       "hm2UserDeletedTrap": hm2UserDeletedTrap,
       "hm2UserLockedTrap": hm2UserLockedTrap,
       "hm2UserPwdChangedTrap": hm2UserPwdChangedTrap,
       "hm2UserPwdPolicyChkChangedTrap": hm2UserPwdPolicyChkChangedTrap,
       "hm2UserMgmtMibObjects": hm2UserMgmtMibObjects,
       "hm2UserConfigGroup": hm2UserConfigGroup,
       "hm2UserConfigTable": hm2UserConfigTable,
       "hm2UserConfigEntry": hm2UserConfigEntry,
       "hm2UserName": hm2UserName,
       "hm2UserPassword": hm2UserPassword,
       "hm2UserAccessRole": hm2UserAccessRole,
       "hm2UserLockoutStatus": hm2UserLockoutStatus,
       "hm2UserPwdChangePerm": hm2UserPwdChangePerm,
       "hm2UserPwdPolicyChk": hm2UserPwdPolicyChk,
       "hm2UserSnmpAuthType": hm2UserSnmpAuthType,
       "hm2UserSnmpEncType": hm2UserSnmpEncType,
       "hm2UserStatus": hm2UserStatus,
       "hm2UserStatusGroup": hm2UserStatusGroup,
       "hm2UserLastUserCreated": hm2UserLastUserCreated,
       "hm2UserLastUserDeleted": hm2UserLastUserDeleted,
       "hm2UserCustomGroup": hm2UserCustomGroup,
       "hm2UserCustomAccessRole2NameTable": hm2UserCustomAccessRole2NameTable,
       "hm2UserCustomAccessRole2NameEntry": hm2UserCustomAccessRole2NameEntry,
       "hm2UserCustomAccessRole": hm2UserCustomAccessRole,
       "hm2UserCustomAccessRoleName": hm2UserCustomAccessRoleName,
       "hm2UserCustomAccessRoleStatus": hm2UserCustomAccessRoleStatus,
       "hm2UserCustomCliCmdInheritTable": hm2UserCustomCliCmdInheritTable,
       "hm2UserCustomCliCmdInheritEntry": hm2UserCustomCliCmdInheritEntry,
       "hm2UserCustomCliBaseAccessRole": hm2UserCustomCliBaseAccessRole,
       "hm2UserCustomCliBaseAccessRoleStatus": hm2UserCustomCliBaseAccessRoleStatus,
       "hm2UserCustomCliCmdTable": hm2UserCustomCliCmdTable,
       "hm2UserCustomCliCmdEntry": hm2UserCustomCliCmdEntry,
       "hm2UserCustomCliExecMode": hm2UserCustomCliExecMode,
       "hm2UserCustomCliIndex": hm2UserCustomCliIndex,
       "hm2UserCustomCliCommand": hm2UserCustomCliCommand,
       "hm2UserCustomCliType": hm2UserCustomCliType,
       "hm2UserCustomCliStatus": hm2UserCustomCliStatus,
       "hm2PwdMgmtGroup": hm2PwdMgmtGroup,
       "hm2PwdMgmtMinLength": hm2PwdMgmtMinLength,
       "hm2PwdMgmtLoginAttempts": hm2PwdMgmtLoginAttempts,
       "hm2PwdMgmtMinUpperCase": hm2PwdMgmtMinUpperCase,
       "hm2PwdMgmtMinLowerCase": hm2PwdMgmtMinLowerCase,
       "hm2PwdMgmtMinNumericNumbers": hm2PwdMgmtMinNumericNumbers,
       "hm2PwdMgmtMinSpecialCharacters": hm2PwdMgmtMinSpecialCharacters,
       "hm2PwdMgmtDefaultPwdStatusGroup": hm2PwdMgmtDefaultPwdStatusGroup,
       "hm2PwdMgmtDefaultPwdActive": hm2PwdMgmtDefaultPwdActive,
       "hm2PwdMgmtDefaultPwdStatusTable": hm2PwdMgmtDefaultPwdStatusTable,
       "hm2PwdMgmtDefaultPwdStatusEntry": hm2PwdMgmtDefaultPwdStatusEntry,
       "hm2PwdMgmtDefaultPwdStatusIndex": hm2PwdMgmtDefaultPwdStatusIndex,
       "hm2PwdMgmtDefaultPwdStatusUserName": hm2PwdMgmtDefaultPwdStatusUserName,
       "hm2UserApplicationListGroup": hm2UserApplicationListGroup,
       "hm2UserApplicationListTable": hm2UserApplicationListTable,
       "hm2UserApplicationListEntry": hm2UserApplicationListEntry,
       "hm2UserApplicationListName": hm2UserApplicationListName,
       "hm2UserApplicationListAuthListName": hm2UserApplicationListAuthListName,
       "hm2UserApplicationListStatus": hm2UserApplicationListStatus,
       "hm2UserAuthListGroup": hm2UserAuthListGroup,
       "hm2UserAuthListTable": hm2UserAuthListTable,
       "hm2UserAuthListEntry": hm2UserAuthListEntry,
       "hm2UserAuthListName": hm2UserAuthListName,
       "hm2UserAuthListPolicy1": hm2UserAuthListPolicy1,
       "hm2UserAuthListPolicy2": hm2UserAuthListPolicy2,
       "hm2UserAuthListPolicy3": hm2UserAuthListPolicy3,
       "hm2UserAuthListPolicy4": hm2UserAuthListPolicy4,
       "hm2UserAuthListPolicy5": hm2UserAuthListPolicy5,
       "hm2UserAuthListStatus": hm2UserAuthListStatus,
       "hm2UserIasGroup": hm2UserIasGroup,
       "hm2UserIasTable": hm2UserIasTable,
       "hm2UserIasEntry": hm2UserIasEntry,
       "hm2UserIasUserName": hm2UserIasUserName,
       "hm2UserIasUserPassword": hm2UserIasUserPassword,
       "hm2UserIasUserStatus": hm2UserIasUserStatus,
       "hm2UserMgmtMibSNMPExtensionGroup": hm2UserMgmtMibSNMPExtensionGroup,
       "hm2UserMgmtGlobalSESGroup": hm2UserMgmtGlobalSESGroup,
       "hm2UserMgmtGlobalSESLenCharset": hm2UserMgmtGlobalSESLenCharset,
       "hm2UserMgmtGlobalSESPwdLenCharset": hm2UserMgmtGlobalSESPwdLenCharset,
       "hm2UserMgmtUserSESGroup": hm2UserMgmtUserSESGroup,
       "hm2UserMgmtUserSESActivate": hm2UserMgmtUserSESActivate,
       "hm2UserMgmtUserSESDeactivate": hm2UserMgmtUserSESDeactivate,
       "hm2UserMgmtApplSESGroup": hm2UserMgmtApplSESGroup,
       "hm2UserMgmtApplSESAddDel": hm2UserMgmtApplSESAddDel,
       "hm2UserMgmtApplSESDeactivate": hm2UserMgmtApplSESDeactivate,
       "hm2UserMgmtAuthSESGroup": hm2UserMgmtAuthSESGroup,
       "hm2UserMgmtAuthSESDuplPolicy": hm2UserMgmtAuthSESDuplPolicy,
       "hm2UserMgmtAuthSESDeactivate": hm2UserMgmtAuthSESDeactivate}
)
