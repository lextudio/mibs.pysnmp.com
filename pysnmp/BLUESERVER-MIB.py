# SNMP MIB module (BLUESERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUESERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:24 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

blueSocket = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9967)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BlueIpAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )



class BlueMacAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:1x:1x:1x:1x:1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )



class LocalDateAndTime(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



# MIB Managed Objects in the order of their OIDs

_BlueServer_ObjectIdentity = ObjectIdentity
blueServer = _BlueServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1)
)
_Users_ObjectIdentity = ObjectIdentity
users = _Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1)
)
_NativeUsers_ObjectIdentity = ObjectIdentity
nativeUsers = _NativeUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1)
)
_NativeUserTable_Object = MibTable
nativeUserTable = _NativeUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nativeUserTable.setStatus("current")
_NativeUserEntry_Object = MibTableRow
nativeUserEntry = _NativeUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1)
)
nativeUserEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "nativeUserId"),
)
if mibBuilder.loadTexts:
    nativeUserEntry.setStatus("current")


class _NativeUserId_Type(Integer32):
    """Custom type nativeUserId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NativeUserId_Type.__name__ = "Integer32"
_NativeUserId_Object = MibTableColumn
nativeUserId = _NativeUserId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 1),
    _NativeUserId_Type()
)
nativeUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nativeUserId.setStatus("current")


class _NativeUserAccess_Type(Integer32):
    """Custom type nativeUserAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NativeUserAccess_Type.__name__ = "Integer32"
_NativeUserAccess_Object = MibTableColumn
nativeUserAccess = _NativeUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 2),
    _NativeUserAccess_Type()
)
nativeUserAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nativeUserAccess.setStatus("current")
_NativeUserName_Type = DisplayString
_NativeUserName_Object = MibTableColumn
nativeUserName = _NativeUserName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 3),
    _NativeUserName_Type()
)
nativeUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nativeUserName.setStatus("current")
_NativeUserRoleId_Type = Integer32
_NativeUserRoleId_Object = MibTableColumn
nativeUserRoleId = _NativeUserRoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 4),
    _NativeUserRoleId_Type()
)
nativeUserRoleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nativeUserRoleId.setStatus("current")
_NativeUserEmailId_Type = DisplayString
_NativeUserEmailId_Object = MibTableColumn
nativeUserEmailId = _NativeUserEmailId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 5),
    _NativeUserEmailId_Type()
)
nativeUserEmailId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nativeUserEmailId.setStatus("current")
_NativeUserFixedIpAddr_Type = BlueIpAddress
_NativeUserFixedIpAddr_Object = MibTableColumn
nativeUserFixedIpAddr = _NativeUserFixedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 6),
    _NativeUserFixedIpAddr_Type()
)
nativeUserFixedIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nativeUserFixedIpAddr.setStatus("current")
_NativeUserPassword_Type = DisplayString
_NativeUserPassword_Object = MibTableColumn
nativeUserPassword = _NativeUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 7),
    _NativeUserPassword_Type()
)
nativeUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nativeUserPassword.setStatus("current")
_NativeUserNotes_Type = DisplayString
_NativeUserNotes_Object = MibTableColumn
nativeUserNotes = _NativeUserNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 8),
    _NativeUserNotes_Type()
)
nativeUserNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nativeUserNotes.setStatus("current")
_NativeUserRowStatus_Type = RowStatus
_NativeUserRowStatus_Object = MibTableColumn
nativeUserRowStatus = _NativeUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 9),
    _NativeUserRowStatus_Type()
)
nativeUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nativeUserRowStatus.setStatus("current")
_NativeUserRadAcctServId_Type = Integer32
_NativeUserRadAcctServId_Object = MibTableColumn
nativeUserRadAcctServId = _NativeUserRadAcctServId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 1, 1, 1, 10),
    _NativeUserRadAcctServId_Type()
)
nativeUserRadAcctServId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nativeUserRadAcctServId.setStatus("current")
_AdminUsers_ObjectIdentity = ObjectIdentity
adminUsers = _AdminUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2)
)
_AdminUserTable_Object = MibTable
adminUserTable = _AdminUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adminUserTable.setStatus("current")
_AdminUserEntry_Object = MibTableRow
adminUserEntry = _AdminUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1, 1)
)
adminUserEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "adminUserId"),
)
if mibBuilder.loadTexts:
    adminUserEntry.setStatus("current")


class _AdminUserId_Type(Integer32):
    """Custom type adminUserId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdminUserId_Type.__name__ = "Integer32"
_AdminUserId_Object = MibTableColumn
adminUserId = _AdminUserId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1, 1, 1),
    _AdminUserId_Type()
)
adminUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminUserId.setStatus("current")


class _AdminUserStatus_Type(Integer32):
    """Custom type adminUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdminUserStatus_Type.__name__ = "Integer32"
_AdminUserStatus_Object = MibTableColumn
adminUserStatus = _AdminUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1, 1, 2),
    _AdminUserStatus_Type()
)
adminUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adminUserStatus.setStatus("current")
_AdminUserName_Type = DisplayString
_AdminUserName_Object = MibTableColumn
adminUserName = _AdminUserName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1, 1, 3),
    _AdminUserName_Type()
)
adminUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adminUserName.setStatus("current")


class _AdminUserAccess_Type(Integer32):
    """Custom type adminUserAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("intermediate", 2),
          ("readOnly", 3))
    )


_AdminUserAccess_Type.__name__ = "Integer32"
_AdminUserAccess_Object = MibTableColumn
adminUserAccess = _AdminUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1, 1, 4),
    _AdminUserAccess_Type()
)
adminUserAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adminUserAccess.setStatus("current")
_AdminUserEmailId_Type = DisplayString
_AdminUserEmailId_Object = MibTableColumn
adminUserEmailId = _AdminUserEmailId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1, 1, 5),
    _AdminUserEmailId_Type()
)
adminUserEmailId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adminUserEmailId.setStatus("current")
_AdminUserPassword_Type = DisplayString
_AdminUserPassword_Object = MibTableColumn
adminUserPassword = _AdminUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1, 1, 6),
    _AdminUserPassword_Type()
)
adminUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adminUserPassword.setStatus("current")
_AdminUserNotes_Type = DisplayString
_AdminUserNotes_Object = MibTableColumn
adminUserNotes = _AdminUserNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1, 1, 7),
    _AdminUserNotes_Type()
)
adminUserNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adminUserNotes.setStatus("current")
_AdminUserRowStatus_Type = RowStatus
_AdminUserRowStatus_Object = MibTableColumn
adminUserRowStatus = _AdminUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 2, 1, 1, 9),
    _AdminUserRowStatus_Type()
)
adminUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adminUserRowStatus.setStatus("current")
_AdUsrAccessTable_Object = MibTable
adUsrAccessTable = _AdUsrAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adUsrAccessTable.setStatus("current")
_AdUsrAccessEntry_Object = MibTableRow
adUsrAccessEntry = _AdUsrAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1)
)
adUsrAccessEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "adminUserId"),
)
if mibBuilder.loadTexts:
    adUsrAccessEntry.setStatus("current")


class _AdUsrAccessAdminUser_Type(Integer32):
    """Custom type adUsrAccessAdminUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessAdminUser_Type.__name__ = "Integer32"
_AdUsrAccessAdminUser_Object = MibTableColumn
adUsrAccessAdminUser = _AdUsrAccessAdminUser_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 1),
    _AdUsrAccessAdminUser_Type()
)
adUsrAccessAdminUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessAdminUser.setStatus("current")


class _AdUsrAccessNativeUser_Type(Integer32):
    """Custom type adUsrAccessNativeUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessNativeUser_Type.__name__ = "Integer32"
_AdUsrAccessNativeUser_Object = MibTableColumn
adUsrAccessNativeUser = _AdUsrAccessNativeUser_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 2),
    _AdUsrAccessNativeUser_Type()
)
adUsrAccessNativeUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessNativeUser.setStatus("current")


class _AdUsrAccessExServer_Type(Integer32):
    """Custom type adUsrAccessExServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessExServer_Type.__name__ = "Integer32"
_AdUsrAccessExServer_Object = MibTableColumn
adUsrAccessExServer = _AdUsrAccessExServer_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 3),
    _AdUsrAccessExServer_Type()
)
adUsrAccessExServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessExServer.setStatus("current")


class _AdUsrAccessAccounting_Type(Integer32):
    """Custom type adUsrAccessAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessAccounting_Type.__name__ = "Integer32"
_AdUsrAccessAccounting_Object = MibTableColumn
adUsrAccessAccounting = _AdUsrAccessAccounting_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 4),
    _AdUsrAccessAccounting_Type()
)
adUsrAccessAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessAccounting.setStatus("current")


class _AdUsrAccessRoles_Type(Integer32):
    """Custom type adUsrAccessRoles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessRoles_Type.__name__ = "Integer32"
_AdUsrAccessRoles_Object = MibTableColumn
adUsrAccessRoles = _AdUsrAccessRoles_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 5),
    _AdUsrAccessRoles_Type()
)
adUsrAccessRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessRoles.setStatus("current")


class _AdUsrAccessDestination_Type(Integer32):
    """Custom type adUsrAccessDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessDestination_Type.__name__ = "Integer32"
_AdUsrAccessDestination_Object = MibTableColumn
adUsrAccessDestination = _AdUsrAccessDestination_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 6),
    _AdUsrAccessDestination_Type()
)
adUsrAccessDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessDestination.setStatus("current")


class _AdUsrAccessServices_Type(Integer32):
    """Custom type adUsrAccessServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessServices_Type.__name__ = "Integer32"
_AdUsrAccessServices_Object = MibTableColumn
adUsrAccessServices = _AdUsrAccessServices_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 7),
    _AdUsrAccessServices_Type()
)
adUsrAccessServices.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessServices.setStatus("current")


class _AdUsrAccessVpn_Type(Integer32):
    """Custom type adUsrAccessVpn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessVpn_Type.__name__ = "Integer32"
_AdUsrAccessVpn_Object = MibTableColumn
adUsrAccessVpn = _AdUsrAccessVpn_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 8),
    _AdUsrAccessVpn_Type()
)
adUsrAccessVpn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessVpn.setStatus("current")


class _AdUsrAccessConfiguration_Type(Integer32):
    """Custom type adUsrAccessConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessConfiguration_Type.__name__ = "Integer32"
_AdUsrAccessConfiguration_Object = MibTableColumn
adUsrAccessConfiguration = _AdUsrAccessConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 9),
    _AdUsrAccessConfiguration_Type()
)
adUsrAccessConfiguration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessConfiguration.setStatus("current")


class _AdUsrAccessNetwork_Type(Integer32):
    """Custom type adUsrAccessNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessNetwork_Type.__name__ = "Integer32"
_AdUsrAccessNetwork_Object = MibTableColumn
adUsrAccessNetwork = _AdUsrAccessNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 10),
    _AdUsrAccessNetwork_Type()
)
adUsrAccessNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessNetwork.setStatus("current")


class _AdUsrAccessReplication_Type(Integer32):
    """Custom type adUsrAccessReplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessReplication_Type.__name__ = "Integer32"
_AdUsrAccessReplication_Object = MibTableColumn
adUsrAccessReplication = _AdUsrAccessReplication_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 11),
    _AdUsrAccessReplication_Type()
)
adUsrAccessReplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessReplication.setStatus("current")


class _AdUsrAccessMaintance_Type(Integer32):
    """Custom type adUsrAccessMaintance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessMaintance_Type.__name__ = "Integer32"
_AdUsrAccessMaintance_Object = MibTableColumn
adUsrAccessMaintance = _AdUsrAccessMaintance_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 12),
    _AdUsrAccessMaintance_Type()
)
adUsrAccessMaintance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessMaintance.setStatus("current")


class _AdUsrAccessStatus_Type(Integer32):
    """Custom type adUsrAccessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessStatus_Type.__name__ = "Integer32"
_AdUsrAccessStatus_Object = MibTableColumn
adUsrAccessStatus = _AdUsrAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 13),
    _AdUsrAccessStatus_Type()
)
adUsrAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessStatus.setStatus("current")


class _AdUsrAccessVlans_Type(Integer32):
    """Custom type adUsrAccessVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessVlans_Type.__name__ = "Integer32"
_AdUsrAccessVlans_Object = MibTableColumn
adUsrAccessVlans = _AdUsrAccessVlans_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 14),
    _AdUsrAccessVlans_Type()
)
adUsrAccessVlans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessVlans.setStatus("current")


class _AdUsrAccessSchedules_Type(Integer32):
    """Custom type adUsrAccessSchedules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessSchedules_Type.__name__ = "Integer32"
_AdUsrAccessSchedules_Object = MibTableColumn
adUsrAccessSchedules = _AdUsrAccessSchedules_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 15),
    _AdUsrAccessSchedules_Type()
)
adUsrAccessSchedules.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessSchedules.setStatus("current")


class _AdUsrAccessMacDev_Type(Integer32):
    """Custom type adUsrAccessMacDev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdUsrAccessMacDev_Type.__name__ = "Integer32"
_AdUsrAccessMacDev_Object = MibTableColumn
adUsrAccessMacDev = _AdUsrAccessMacDev_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 1, 3, 1, 16),
    _AdUsrAccessMacDev_Type()
)
adUsrAccessMacDev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adUsrAccessMacDev.setStatus("current")
_Destination_ObjectIdentity = ObjectIdentity
destination = _Destination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3)
)
_HostTable_Object = MibTable
hostTable = _HostTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hostTable.setStatus("current")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1, 1)
)
hostEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "hostId"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("current")


class _HostId_Type(Integer32):
    """Custom type hostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HostId_Type.__name__ = "Integer32"
_HostId_Object = MibTableColumn
hostId = _HostId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1, 1, 1),
    _HostId_Type()
)
hostId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostId.setStatus("current")


class _HostName_Type(OctetString):
    """Custom type hostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_HostName_Type.__name__ = "OctetString"
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_HostAddress_Type = BlueIpAddress
_HostAddress_Object = MibTableColumn
hostAddress = _HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1, 1, 3),
    _HostAddress_Type()
)
hostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostAddress.setStatus("current")
_HostNetmask_Type = BlueIpAddress
_HostNetmask_Object = MibTableColumn
hostNetmask = _HostNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1, 1, 4),
    _HostNetmask_Type()
)
hostNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostNetmask.setStatus("current")


class _HostInvertDest_Type(OctetString):
    """Custom type hostInvertDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HostInvertDest_Type.__name__ = "OctetString"
_HostInvertDest_Object = MibTableColumn
hostInvertDest = _HostInvertDest_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1, 1, 5),
    _HostInvertDest_Type()
)
hostInvertDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostInvertDest.setStatus("current")


class _HostType_Type(OctetString):
    """Custom type hostType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HostType_Type.__name__ = "OctetString"
_HostType_Object = MibTableColumn
hostType = _HostType_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1, 1, 6),
    _HostType_Type()
)
hostType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostType.setStatus("current")
_HostNotes_Type = DisplayString
_HostNotes_Object = MibTableColumn
hostNotes = _HostNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1, 1, 7),
    _HostNotes_Type()
)
hostNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostNotes.setStatus("current")
_HostRowStatus_Type = RowStatus
_HostRowStatus_Object = MibTableColumn
hostRowStatus = _HostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 1, 1, 8),
    _HostRowStatus_Type()
)
hostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostRowStatus.setStatus("current")
_HostGrpTable_Object = MibTable
hostGrpTable = _HostGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hostGrpTable.setStatus("current")
_HostGrpEntry_Object = MibTableRow
hostGrpEntry = _HostGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 2, 1)
)
hostGrpEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "hostGrpId"),
)
if mibBuilder.loadTexts:
    hostGrpEntry.setStatus("current")


class _HostGrpId_Type(Integer32):
    """Custom type hostGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HostGrpId_Type.__name__ = "Integer32"
_HostGrpId_Object = MibTableColumn
hostGrpId = _HostGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 2, 1, 1),
    _HostGrpId_Type()
)
hostGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostGrpId.setStatus("current")


class _HostGrpName_Type(OctetString):
    """Custom type hostGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_HostGrpName_Type.__name__ = "OctetString"
_HostGrpName_Object = MibTableColumn
hostGrpName = _HostGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 2, 1, 2),
    _HostGrpName_Type()
)
hostGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostGrpName.setStatus("current")
_HostGrpRowStatus_Type = RowStatus
_HostGrpRowStatus_Object = MibTableColumn
hostGrpRowStatus = _HostGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 2, 1, 3),
    _HostGrpRowStatus_Type()
)
hostGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostGrpRowStatus.setStatus("current")
_HostGrpMemTable_Object = MibTable
hostGrpMemTable = _HostGrpMemTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hostGrpMemTable.setStatus("current")
_HostGrpMemEntry_Object = MibTableRow
hostGrpMemEntry = _HostGrpMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 3, 1)
)
hostGrpMemEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "hostGrpId"),
    (0, "BLUESERVER-MIB", "hostGrpMemId"),
)
if mibBuilder.loadTexts:
    hostGrpMemEntry.setStatus("current")


class _HostGrpMemId_Type(Integer32):
    """Custom type hostGrpMemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HostGrpMemId_Type.__name__ = "Integer32"
_HostGrpMemId_Object = MibTableColumn
hostGrpMemId = _HostGrpMemId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 3, 1, 1),
    _HostGrpMemId_Type()
)
hostGrpMemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostGrpMemId.setStatus("current")
_HostGrpMemRowStatus_Type = RowStatus
_HostGrpMemRowStatus_Object = MibTableColumn
hostGrpMemRowStatus = _HostGrpMemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 3, 3, 1, 2),
    _HostGrpMemRowStatus_Type()
)
hostGrpMemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostGrpMemRowStatus.setStatus("current")
_Service_ObjectIdentity = ObjectIdentity
service = _Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4)
)
_ServiceTable_Object = MibTable
serviceTable = _ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1)
)
if mibBuilder.loadTexts:
    serviceTable.setStatus("current")
_ServiceEntry_Object = MibTableRow
serviceEntry = _ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1)
)
serviceEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "serviceId"),
)
if mibBuilder.loadTexts:
    serviceEntry.setStatus("current")


class _ServiceId_Type(Integer32):
    """Custom type serviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ServiceId_Type.__name__ = "Integer32"
_ServiceId_Object = MibTableColumn
serviceId = _ServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 1),
    _ServiceId_Type()
)
serviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceId.setStatus("current")


class _ServiceName_Type(OctetString):
    """Custom type serviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ServiceName_Type.__name__ = "OctetString"
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 2),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceName.setStatus("current")
_ServicePort_Type = Integer32
_ServicePort_Object = MibTableColumn
servicePort = _ServicePort_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 3),
    _ServicePort_Type()
)
servicePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    servicePort.setStatus("current")


class _ServiceProtocol_Type(OctetString):
    """Custom type serviceProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ServiceProtocol_Type.__name__ = "OctetString"
_ServiceProtocol_Object = MibTableColumn
serviceProtocol = _ServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 4),
    _ServiceProtocol_Type()
)
serviceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceProtocol.setStatus("current")
_ServiceCosPriorityIn_Type = Integer32
_ServiceCosPriorityIn_Object = MibTableColumn
serviceCosPriorityIn = _ServiceCosPriorityIn_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 7),
    _ServiceCosPriorityIn_Type()
)
serviceCosPriorityIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceCosPriorityIn.setStatus("current")
_ServiceCosPriorityOut_Type = Integer32
_ServiceCosPriorityOut_Object = MibTableColumn
serviceCosPriorityOut = _ServiceCosPriorityOut_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 8),
    _ServiceCosPriorityOut_Type()
)
serviceCosPriorityOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceCosPriorityOut.setStatus("current")
_ServiceCosDscpIn_Type = Integer32
_ServiceCosDscpIn_Object = MibTableColumn
serviceCosDscpIn = _ServiceCosDscpIn_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 9),
    _ServiceCosDscpIn_Type()
)
serviceCosDscpIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceCosDscpIn.setStatus("current")
_ServiceCosDscpOut_Type = Integer32
_ServiceCosDscpOut_Object = MibTableColumn
serviceCosDscpOut = _ServiceCosDscpOut_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 10),
    _ServiceCosDscpOut_Type()
)
serviceCosDscpOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceCosDscpOut.setStatus("current")
_ServiceNotes_Type = DisplayString
_ServiceNotes_Object = MibTableColumn
serviceNotes = _ServiceNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 11),
    _ServiceNotes_Type()
)
serviceNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceNotes.setStatus("current")
_ServiceRowStatus_Type = RowStatus
_ServiceRowStatus_Object = MibTableColumn
serviceRowStatus = _ServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 1, 1, 12),
    _ServiceRowStatus_Type()
)
serviceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceRowStatus.setStatus("current")
_ServiceGrpTable_Object = MibTable
serviceGrpTable = _ServiceGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 2)
)
if mibBuilder.loadTexts:
    serviceGrpTable.setStatus("current")
_ServiceGrpEntry_Object = MibTableRow
serviceGrpEntry = _ServiceGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 2, 1)
)
serviceGrpEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "serviceGrpId"),
)
if mibBuilder.loadTexts:
    serviceGrpEntry.setStatus("current")


class _ServiceGrpId_Type(Integer32):
    """Custom type serviceGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ServiceGrpId_Type.__name__ = "Integer32"
_ServiceGrpId_Object = MibTableColumn
serviceGrpId = _ServiceGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 2, 1, 1),
    _ServiceGrpId_Type()
)
serviceGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceGrpId.setStatus("current")


class _ServiceGrpName_Type(OctetString):
    """Custom type serviceGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ServiceGrpName_Type.__name__ = "OctetString"
_ServiceGrpName_Object = MibTableColumn
serviceGrpName = _ServiceGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 2, 1, 2),
    _ServiceGrpName_Type()
)
serviceGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceGrpName.setStatus("current")
_ServiceGrpRowStatus_Type = RowStatus
_ServiceGrpRowStatus_Object = MibTableColumn
serviceGrpRowStatus = _ServiceGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 2, 1, 3),
    _ServiceGrpRowStatus_Type()
)
serviceGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceGrpRowStatus.setStatus("current")
_ServiceGrpMemTable_Object = MibTable
serviceGrpMemTable = _ServiceGrpMemTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 3)
)
if mibBuilder.loadTexts:
    serviceGrpMemTable.setStatus("current")
_ServiceGrpMemEntry_Object = MibTableRow
serviceGrpMemEntry = _ServiceGrpMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 3, 1)
)
serviceGrpMemEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "serviceGrpId"),
    (0, "BLUESERVER-MIB", "serviceGrpMemId"),
)
if mibBuilder.loadTexts:
    serviceGrpMemEntry.setStatus("current")


class _ServiceGrpMemId_Type(Integer32):
    """Custom type serviceGrpMemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ServiceGrpMemId_Type.__name__ = "Integer32"
_ServiceGrpMemId_Object = MibTableColumn
serviceGrpMemId = _ServiceGrpMemId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 3, 1, 1),
    _ServiceGrpMemId_Type()
)
serviceGrpMemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceGrpMemId.setStatus("current")
_ServiceGrpMemRowStatus_Type = RowStatus
_ServiceGrpMemRowStatus_Object = MibTableColumn
serviceGrpMemRowStatus = _ServiceGrpMemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 4, 3, 1, 2),
    _ServiceGrpMemRowStatus_Type()
)
serviceGrpMemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceGrpMemRowStatus.setStatus("current")
_Policy_ObjectIdentity = ObjectIdentity
policy = _Policy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5)
)
_PolicyTable_Object = MibTable
policyTable = _PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1)
)
if mibBuilder.loadTexts:
    policyTable.setStatus("current")
_PolicyEntry_Object = MibTableRow
policyEntry = _PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1)
)
policyEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "roleId"),
    (0, "BLUESERVER-MIB", "policyId"),
)
if mibBuilder.loadTexts:
    policyEntry.setStatus("current")


class _PolicyId_Type(Integer32):
    """Custom type policyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PolicyId_Type.__name__ = "Integer32"
_PolicyId_Object = MibTableColumn
policyId = _PolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1, 1),
    _PolicyId_Type()
)
policyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyId.setStatus("current")
_PolicyServiceId_Type = Integer32
_PolicyServiceId_Object = MibTableColumn
policyServiceId = _PolicyServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1, 2),
    _PolicyServiceId_Type()
)
policyServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyServiceId.setStatus("current")
_PolicyHostId_Type = Integer32
_PolicyHostId_Object = MibTableColumn
policyHostId = _PolicyHostId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1, 3),
    _PolicyHostId_Type()
)
policyHostId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyHostId.setStatus("current")


class _PolicyAction_Type(OctetString):
    """Custom type policyAction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PolicyAction_Type.__name__ = "OctetString"
_PolicyAction_Object = MibTableColumn
policyAction = _PolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1, 4),
    _PolicyAction_Type()
)
policyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyAction.setStatus("current")


class _PolicyDirection_Type(OctetString):
    """Custom type policyDirection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PolicyDirection_Type.__name__ = "OctetString"
_PolicyDirection_Object = MibTableColumn
policyDirection = _PolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1, 5),
    _PolicyDirection_Type()
)
policyDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyDirection.setStatus("current")
_PolicySeqId_Type = Integer32
_PolicySeqId_Object = MibTableColumn
policySeqId = _PolicySeqId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1, 6),
    _PolicySeqId_Type()
)
policySeqId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policySeqId.setStatus("current")
_PolicyVlanId_Type = Integer32
_PolicyVlanId_Object = MibTableColumn
policyVlanId = _PolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1, 8),
    _PolicyVlanId_Type()
)
policyVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyVlanId.setStatus("current")
_PolicyScheduleId_Type = Integer32
_PolicyScheduleId_Object = MibTableColumn
policyScheduleId = _PolicyScheduleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1, 9),
    _PolicyScheduleId_Type()
)
policyScheduleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyScheduleId.setStatus("current")
_PolicyRowStatus_Type = RowStatus
_PolicyRowStatus_Object = MibTableColumn
policyRowStatus = _PolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 5, 1, 1, 10),
    _PolicyRowStatus_Type()
)
policyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyRowStatus.setStatus("current")
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6)
)
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1)
)


class _ExchangeMode_Type(Integer32):
    """Custom type exchangeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 1),
          ("main", 2))
    )


_ExchangeMode_Type.__name__ = "Integer32"
_ExchangeMode_Object = MibScalar
exchangeMode = _ExchangeMode_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 1),
    _ExchangeMode_Type()
)
exchangeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exchangeMode.setStatus("current")


class _AuthenticationMethod_Type(Integer32):
    """Custom type authenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("certificates", 1),
          ("sharedKeys", 2))
    )


_AuthenticationMethod_Type.__name__ = "Integer32"
_AuthenticationMethod_Object = MibScalar
authenticationMethod = _AuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 2),
    _AuthenticationMethod_Type()
)
authenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationMethod.setStatus("current")
_IdleTimeout_Type = Integer32
_IdleTimeout_Object = MibScalar
idleTimeout = _IdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 3),
    _IdleTimeout_Type()
)
idleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleTimeout.setStatus("current")
_MaxLifeTimeInSecs_Type = Integer32
_MaxLifeTimeInSecs_Object = MibScalar
maxLifeTimeInSecs = _MaxLifeTimeInSecs_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 4),
    _MaxLifeTimeInSecs_Type()
)
maxLifeTimeInSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxLifeTimeInSecs.setStatus("current")
_MaxLifeTimeInKbs_Type = Integer32
_MaxLifeTimeInKbs_Object = MibScalar
maxLifeTimeInKbs = _MaxLifeTimeInKbs_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 5),
    _MaxLifeTimeInKbs_Type()
)
maxLifeTimeInKbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxLifeTimeInKbs.setStatus("current")
_RefreshThresholdInSecs_Type = Integer32
_RefreshThresholdInSecs_Object = MibScalar
refreshThresholdInSecs = _RefreshThresholdInSecs_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 6),
    _RefreshThresholdInSecs_Type()
)
refreshThresholdInSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refreshThresholdInSecs.setStatus("current")
_RefreshThresholdInKbs_Type = Integer32
_RefreshThresholdInKbs_Object = MibScalar
refreshThresholdInKbs = _RefreshThresholdInKbs_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 7),
    _RefreshThresholdInKbs_Type()
)
refreshThresholdInKbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refreshThresholdInKbs.setStatus("current")
_MinLifeTimeInSecs_Type = Integer32
_MinLifeTimeInSecs_Object = MibScalar
minLifeTimeInSecs = _MinLifeTimeInSecs_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 8),
    _MinLifeTimeInSecs_Type()
)
minLifeTimeInSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minLifeTimeInSecs.setStatus("current")
_MinLifeTimeInKbs_Type = Integer32
_MinLifeTimeInKbs_Object = MibScalar
minLifeTimeInKbs = _MinLifeTimeInKbs_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 9),
    _MinLifeTimeInKbs_Type()
)
minLifeTimeInKbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minLifeTimeInKbs.setStatus("current")


class _ExModeAggressive_Type(Integer32):
    """Custom type exModeAggressive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ExModeAggressive_Type.__name__ = "Integer32"
_ExModeAggressive_Object = MibScalar
exModeAggressive = _ExModeAggressive_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 10),
    _ExModeAggressive_Type()
)
exModeAggressive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exModeAggressive.setStatus("current")


class _ExModeMain_Type(Integer32):
    """Custom type exModeMain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ExModeMain_Type.__name__ = "Integer32"
_ExModeMain_Object = MibScalar
exModeMain = _ExModeMain_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 11),
    _ExModeMain_Type()
)
exModeMain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exModeMain.setStatus("current")


class _AuthMethodCertificates_Type(Integer32):
    """Custom type authMethodCertificates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AuthMethodCertificates_Type.__name__ = "Integer32"
_AuthMethodCertificates_Object = MibScalar
authMethodCertificates = _AuthMethodCertificates_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 12),
    _AuthMethodCertificates_Type()
)
authMethodCertificates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMethodCertificates.setStatus("current")


class _AuthMethodPreSharedKeys_Type(Integer32):
    """Custom type authMethodPreSharedKeys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AuthMethodPreSharedKeys_Type.__name__ = "Integer32"
_AuthMethodPreSharedKeys_Object = MibScalar
authMethodPreSharedKeys = _AuthMethodPreSharedKeys_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 13),
    _AuthMethodPreSharedKeys_Type()
)
authMethodPreSharedKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMethodPreSharedKeys.setStatus("current")
_IpsecConfTable_Object = MibTable
ipsecConfTable = _IpsecConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14)
)
if mibBuilder.loadTexts:
    ipsecConfTable.setStatus("current")
_IpsecConfEntry_Object = MibTableRow
ipsecConfEntry = _IpsecConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1)
)
ipsecConfEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "ipsecConfId"),
)
if mibBuilder.loadTexts:
    ipsecConfEntry.setStatus("current")


class _IpsecConfId_Type(Integer32):
    """Custom type ipsecConfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsecConfId_Type.__name__ = "Integer32"
_IpsecConfId_Object = MibTableColumn
ipsecConfId = _IpsecConfId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 1),
    _IpsecConfId_Type()
)
ipsecConfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecConfId.setStatus("current")


class _IpsecConfEnableConfiguration_Type(Integer32):
    """Custom type ipsecConfEnableConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_IpsecConfEnableConfiguration_Type.__name__ = "Integer32"
_IpsecConfEnableConfiguration_Object = MibTableColumn
ipsecConfEnableConfiguration = _IpsecConfEnableConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 2),
    _IpsecConfEnableConfiguration_Type()
)
ipsecConfEnableConfiguration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEnableConfiguration.setStatus("current")
_IpsecConfName_Type = DisplayString
_IpsecConfName_Object = MibTableColumn
ipsecConfName = _IpsecConfName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 3),
    _IpsecConfName_Type()
)
ipsecConfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfName.setStatus("current")


class _IpsecConfLocalAuth_Type(Integer32):
    """Custom type ipsecConfLocalAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfLocalAuth_Type.__name__ = "Integer32"
_IpsecConfLocalAuth_Object = MibTableColumn
ipsecConfLocalAuth = _IpsecConfLocalAuth_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 4),
    _IpsecConfLocalAuth_Type()
)
ipsecConfLocalAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfLocalAuth.setStatus("current")


class _IpsecConfEspTripleDESWithSHA1_Type(Integer32):
    """Custom type ipsecConfEspTripleDESWithSHA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEspTripleDESWithSHA1_Type.__name__ = "Integer32"
_IpsecConfEspTripleDESWithSHA1_Object = MibTableColumn
ipsecConfEspTripleDESWithSHA1 = _IpsecConfEspTripleDESWithSHA1_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 5),
    _IpsecConfEspTripleDESWithSHA1_Type()
)
ipsecConfEspTripleDESWithSHA1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEspTripleDESWithSHA1.setStatus("current")


class _IpsecConfEspTripleDESWithMD5_Type(Integer32):
    """Custom type ipsecConfEspTripleDESWithMD5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEspTripleDESWithMD5_Type.__name__ = "Integer32"
_IpsecConfEspTripleDESWithMD5_Object = MibTableColumn
ipsecConfEspTripleDESWithMD5 = _IpsecConfEspTripleDESWithMD5_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 6),
    _IpsecConfEspTripleDESWithMD5_Type()
)
ipsecConfEspTripleDESWithMD5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEspTripleDESWithMD5.setStatus("current")


class _IpsecConfEsp56BitDESWithMD5_Type(Integer32):
    """Custom type ipsecConfEsp56BitDESWithMD5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEsp56BitDESWithMD5_Type.__name__ = "Integer32"
_IpsecConfEsp56BitDESWithMD5_Object = MibTableColumn
ipsecConfEsp56BitDESWithMD5 = _IpsecConfEsp56BitDESWithMD5_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 7),
    _IpsecConfEsp56BitDESWithMD5_Type()
)
ipsecConfEsp56BitDESWithMD5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEsp56BitDESWithMD5.setStatus("current")


class _IpsecConfEsp56BitDESWithSHA1_Type(Integer32):
    """Custom type ipsecConfEsp56BitDESWithSHA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEsp56BitDESWithSHA1_Type.__name__ = "Integer32"
_IpsecConfEsp56BitDESWithSHA1_Object = MibTableColumn
ipsecConfEsp56BitDESWithSHA1 = _IpsecConfEsp56BitDESWithSHA1_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 8),
    _IpsecConfEsp56BitDESWithSHA1_Type()
)
ipsecConfEsp56BitDESWithSHA1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEsp56BitDESWithSHA1.setStatus("current")


class _IpsecConfEsp128BitAESWithMD5_Type(Integer32):
    """Custom type ipsecConfEsp128BitAESWithMD5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEsp128BitAESWithMD5_Type.__name__ = "Integer32"
_IpsecConfEsp128BitAESWithMD5_Object = MibTableColumn
ipsecConfEsp128BitAESWithMD5 = _IpsecConfEsp128BitAESWithMD5_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 9),
    _IpsecConfEsp128BitAESWithMD5_Type()
)
ipsecConfEsp128BitAESWithMD5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEsp128BitAESWithMD5.setStatus("current")


class _IpsecConfEsp128BitAESWithSHA1_Type(Integer32):
    """Custom type ipsecConfEsp128BitAESWithSHA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEsp128BitAESWithSHA1_Type.__name__ = "Integer32"
_IpsecConfEsp128BitAESWithSHA1_Object = MibTableColumn
ipsecConfEsp128BitAESWithSHA1 = _IpsecConfEsp128BitAESWithSHA1_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 10),
    _IpsecConfEsp128BitAESWithSHA1_Type()
)
ipsecConfEsp128BitAESWithSHA1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEsp128BitAESWithSHA1.setStatus("current")


class _IpsecConfEsp192BitAESWithMD5_Type(Integer32):
    """Custom type ipsecConfEsp192BitAESWithMD5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEsp192BitAESWithMD5_Type.__name__ = "Integer32"
_IpsecConfEsp192BitAESWithMD5_Object = MibTableColumn
ipsecConfEsp192BitAESWithMD5 = _IpsecConfEsp192BitAESWithMD5_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 11),
    _IpsecConfEsp192BitAESWithMD5_Type()
)
ipsecConfEsp192BitAESWithMD5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEsp192BitAESWithMD5.setStatus("current")


class _IpsecConfEsp192BitAESWithSHA1_Type(Integer32):
    """Custom type ipsecConfEsp192BitAESWithSHA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEsp192BitAESWithSHA1_Type.__name__ = "Integer32"
_IpsecConfEsp192BitAESWithSHA1_Object = MibTableColumn
ipsecConfEsp192BitAESWithSHA1 = _IpsecConfEsp192BitAESWithSHA1_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 12),
    _IpsecConfEsp192BitAESWithSHA1_Type()
)
ipsecConfEsp192BitAESWithSHA1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEsp192BitAESWithSHA1.setStatus("current")


class _IpsecConfEsp256BitAESWithMD5_Type(Integer32):
    """Custom type ipsecConfEsp256BitAESWithMD5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEsp256BitAESWithMD5_Type.__name__ = "Integer32"
_IpsecConfEsp256BitAESWithMD5_Object = MibTableColumn
ipsecConfEsp256BitAESWithMD5 = _IpsecConfEsp256BitAESWithMD5_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 13),
    _IpsecConfEsp256BitAESWithMD5_Type()
)
ipsecConfEsp256BitAESWithMD5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEsp256BitAESWithMD5.setStatus("current")


class _IpsecConfEsp256BitAESWithSHA1_Type(Integer32):
    """Custom type ipsecConfEsp256BitAESWithSHA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfEsp256BitAESWithSHA1_Type.__name__ = "Integer32"
_IpsecConfEsp256BitAESWithSHA1_Object = MibTableColumn
ipsecConfEsp256BitAESWithSHA1 = _IpsecConfEsp256BitAESWithSHA1_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 14),
    _IpsecConfEsp256BitAESWithSHA1_Type()
)
ipsecConfEsp256BitAESWithSHA1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfEsp256BitAESWithSHA1.setStatus("current")


class _IpsecConfDiffieHellmanGrp1_Type(Integer32):
    """Custom type ipsecConfDiffieHellmanGrp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfDiffieHellmanGrp1_Type.__name__ = "Integer32"
_IpsecConfDiffieHellmanGrp1_Object = MibTableColumn
ipsecConfDiffieHellmanGrp1 = _IpsecConfDiffieHellmanGrp1_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 15),
    _IpsecConfDiffieHellmanGrp1_Type()
)
ipsecConfDiffieHellmanGrp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfDiffieHellmanGrp1.setStatus("current")


class _IpsecConfDiffieHellmanGrp2_Type(Integer32):
    """Custom type ipsecConfDiffieHellmanGrp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfDiffieHellmanGrp2_Type.__name__ = "Integer32"
_IpsecConfDiffieHellmanGrp2_Object = MibTableColumn
ipsecConfDiffieHellmanGrp2 = _IpsecConfDiffieHellmanGrp2_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 16),
    _IpsecConfDiffieHellmanGrp2_Type()
)
ipsecConfDiffieHellmanGrp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfDiffieHellmanGrp2.setStatus("current")


class _IpsecConfDiffieHellmanGrp5_Type(Integer32):
    """Custom type ipsecConfDiffieHellmanGrp5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfDiffieHellmanGrp5_Type.__name__ = "Integer32"
_IpsecConfDiffieHellmanGrp5_Object = MibTableColumn
ipsecConfDiffieHellmanGrp5 = _IpsecConfDiffieHellmanGrp5_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 17),
    _IpsecConfDiffieHellmanGrp5_Type()
)
ipsecConfDiffieHellmanGrp5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfDiffieHellmanGrp5.setStatus("current")


class _IpsecConfPsfMode_Type(Integer32):
    """Custom type ipsecConfPsfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfPsfMode_Type.__name__ = "Integer32"
_IpsecConfPsfMode_Object = MibTableColumn
ipsecConfPsfMode = _IpsecConfPsfMode_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 18),
    _IpsecConfPsfMode_Type()
)
ipsecConfPsfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfPsfMode.setStatus("current")


class _IpsecConfCompressionDeflate_Type(Integer32):
    """Custom type ipsecConfCompressionDeflate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfCompressionDeflate_Type.__name__ = "Integer32"
_IpsecConfCompressionDeflate_Object = MibTableColumn
ipsecConfCompressionDeflate = _IpsecConfCompressionDeflate_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 19),
    _IpsecConfCompressionDeflate_Type()
)
ipsecConfCompressionDeflate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfCompressionDeflate.setStatus("current")


class _IpsecConfCompressionLZS_Type(Integer32):
    """Custom type ipsecConfCompressionLZS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpsecConfCompressionLZS_Type.__name__ = "Integer32"
_IpsecConfCompressionLZS_Object = MibTableColumn
ipsecConfCompressionLZS = _IpsecConfCompressionLZS_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 20),
    _IpsecConfCompressionLZS_Type()
)
ipsecConfCompressionLZS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfCompressionLZS.setStatus("current")
_IpsecConfRowStatus_Type = RowStatus
_IpsecConfRowStatus_Object = MibTableColumn
ipsecConfRowStatus = _IpsecConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 1, 14, 1, 21),
    _IpsecConfRowStatus_Type()
)
ipsecConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsecConfRowStatus.setStatus("current")
_Pptp_ObjectIdentity = ObjectIdentity
pptp = _Pptp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2)
)


class _PptpEnable_Type(Integer32):
    """Custom type pptpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_PptpEnable_Type.__name__ = "Integer32"
_PptpEnable_Object = MibScalar
pptpEnable = _PptpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2, 1),
    _PptpEnable_Type()
)
pptpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpEnable.setStatus("current")
_PptpRemoteIpStartAddr_Type = BlueIpAddress
_PptpRemoteIpStartAddr_Object = MibScalar
pptpRemoteIpStartAddr = _PptpRemoteIpStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2, 2),
    _PptpRemoteIpStartAddr_Type()
)
pptpRemoteIpStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpRemoteIpStartAddr.setStatus("current")
_PptpRemoteIpEndAddr_Type = BlueIpAddress
_PptpRemoteIpEndAddr_Object = MibScalar
pptpRemoteIpEndAddr = _PptpRemoteIpEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2, 3),
    _PptpRemoteIpEndAddr_Type()
)
pptpRemoteIpEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpRemoteIpEndAddr.setStatus("current")
_PptpLocalIpAddr_Type = BlueIpAddress
_PptpLocalIpAddr_Object = MibScalar
pptpLocalIpAddr = _PptpLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2, 4),
    _PptpLocalIpAddr_Type()
)
pptpLocalIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpLocalIpAddr.setStatus("current")


class _PptpEncryption40Bit_Type(Integer32):
    """Custom type pptpEncryption40Bit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PptpEncryption40Bit_Type.__name__ = "Integer32"
_PptpEncryption40Bit_Object = MibScalar
pptpEncryption40Bit = _PptpEncryption40Bit_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2, 5),
    _PptpEncryption40Bit_Type()
)
pptpEncryption40Bit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpEncryption40Bit.setStatus("current")


class _PptpEncryption128Bit_Type(Integer32):
    """Custom type pptpEncryption128Bit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PptpEncryption128Bit_Type.__name__ = "Integer32"
_PptpEncryption128Bit_Object = MibScalar
pptpEncryption128Bit = _PptpEncryption128Bit_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2, 6),
    _PptpEncryption128Bit_Type()
)
pptpEncryption128Bit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpEncryption128Bit.setStatus("current")
_PptpIdleTimeout_Type = Integer32
_PptpIdleTimeout_Object = MibScalar
pptpIdleTimeout = _PptpIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2, 7),
    _PptpIdleTimeout_Type()
)
pptpIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpIdleTimeout.setStatus("current")
_PptpLdapPwdAttrName_Type = DisplayString
_PptpLdapPwdAttrName_Object = MibScalar
pptpLdapPwdAttrName = _PptpLdapPwdAttrName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2, 8),
    _PptpLdapPwdAttrName_Type()
)
pptpLdapPwdAttrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpLdapPwdAttrName.setStatus("current")
_PptpRoleId_Type = Integer32
_PptpRoleId_Object = MibScalar
pptpRoleId = _PptpRoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 2, 9),
    _PptpRoleId_Type()
)
pptpRoleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpRoleId.setStatus("current")
_SubnetVpn_ObjectIdentity = ObjectIdentity
subnetVpn = _SubnetVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 3)
)


class _SubnetVpnMode_Type(Integer32):
    """Custom type subnetVpnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SubnetVpnMode_Type.__name__ = "Integer32"
_SubnetVpnMode_Object = MibScalar
subnetVpnMode = _SubnetVpnMode_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 3, 1),
    _SubnetVpnMode_Type()
)
subnetVpnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetVpnMode.setStatus("current")
_SubnetVpnRtFirstIp_Type = BlueIpAddress
_SubnetVpnRtFirstIp_Object = MibScalar
subnetVpnRtFirstIp = _SubnetVpnRtFirstIp_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 3, 2),
    _SubnetVpnRtFirstIp_Type()
)
subnetVpnRtFirstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetVpnRtFirstIp.setStatus("current")
_SubnetVpnRtLastIp_Type = BlueIpAddress
_SubnetVpnRtLastIp_Object = MibScalar
subnetVpnRtLastIp = _SubnetVpnRtLastIp_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 3, 3),
    _SubnetVpnRtLastIp_Type()
)
subnetVpnRtLastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetVpnRtLastIp.setStatus("current")
_SubnetVpnSharedSec_Type = DisplayString
_SubnetVpnSharedSec_Object = MibScalar
subnetVpnSharedSec = _SubnetVpnSharedSec_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 3, 4),
    _SubnetVpnSharedSec_Type()
)
subnetVpnSharedSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetVpnSharedSec.setStatus("current")
_SubnetIpConfIdInUse_Type = Integer32
_SubnetIpConfIdInUse_Object = MibScalar
subnetIpConfIdInUse = _SubnetIpConfIdInUse_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 3, 5),
    _SubnetIpConfIdInUse_Type()
)
subnetIpConfIdInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetIpConfIdInUse.setStatus("current")
_Certificate_ObjectIdentity = ObjectIdentity
certificate = _Certificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4)
)
_CertTable_Object = MibTable
certTable = _CertTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    certTable.setStatus("current")
_CertEntry_Object = MibTableRow
certEntry = _CertEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1)
)
certEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "certId"),
)
if mibBuilder.loadTexts:
    certEntry.setStatus("current")


class _CertId_Type(Integer32):
    """Custom type certId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CertId_Type.__name__ = "Integer32"
_CertId_Object = MibTableColumn
certId = _CertId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 1),
    _CertId_Type()
)
certId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    certId.setStatus("current")
_CertType_Type = DisplayString
_CertType_Object = MibTableColumn
certType = _CertType_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 2),
    _CertType_Type()
)
certType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certType.setStatus("current")
_CertSubject_Type = DisplayString
_CertSubject_Object = MibTableColumn
certSubject = _CertSubject_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 3),
    _CertSubject_Type()
)
certSubject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certSubject.setStatus("current")
_CertStartDate_Type = DisplayString
_CertStartDate_Object = MibTableColumn
certStartDate = _CertStartDate_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 4),
    _CertStartDate_Type()
)
certStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certStartDate.setStatus("current")
_CertEndDate_Type = DisplayString
_CertEndDate_Object = MibTableColumn
certEndDate = _CertEndDate_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 5),
    _CertEndDate_Type()
)
certEndDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certEndDate.setStatus("current")
_CertIssuer_Type = DisplayString
_CertIssuer_Object = MibTableColumn
certIssuer = _CertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 6),
    _CertIssuer_Type()
)
certIssuer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certIssuer.setStatus("current")
_CertName_Type = DisplayString
_CertName_Object = MibTableColumn
certName = _CertName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 7),
    _CertName_Type()
)
certName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certName.setStatus("current")
_CertOrg_Type = DisplayString
_CertOrg_Object = MibTableColumn
certOrg = _CertOrg_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 8),
    _CertOrg_Type()
)
certOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certOrg.setStatus("current")


class _CertContent_Type(OctetString):
    """Custom type certContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_CertContent_Type.__name__ = "OctetString"
_CertContent_Object = MibTableColumn
certContent = _CertContent_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 9),
    _CertContent_Type()
)
certContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certContent.setStatus("current")
_CertPkey_Type = DisplayString
_CertPkey_Object = MibTableColumn
certPkey = _CertPkey_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 10),
    _CertPkey_Type()
)
certPkey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certPkey.setStatus("current")
_CertPkeyAlgo_Type = DisplayString
_CertPkeyAlgo_Object = MibTableColumn
certPkeyAlgo = _CertPkeyAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 11),
    _CertPkeyAlgo_Type()
)
certPkeyAlgo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certPkeyAlgo.setStatus("current")
_CertPkeySize_Type = Integer32
_CertPkeySize_Object = MibTableColumn
certPkeySize = _CertPkeySize_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 12),
    _CertPkeySize_Type()
)
certPkeySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certPkeySize.setStatus("current")
_CertSerial_Type = DisplayString
_CertSerial_Object = MibTableColumn
certSerial = _CertSerial_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 13),
    _CertSerial_Type()
)
certSerial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certSerial.setStatus("current")
_CertSignAlgo_Type = DisplayString
_CertSignAlgo_Object = MibTableColumn
certSignAlgo = _CertSignAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 14),
    _CertSignAlgo_Type()
)
certSignAlgo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certSignAlgo.setStatus("current")
_CertVersion_Type = Integer32
_CertVersion_Object = MibTableColumn
certVersion = _CertVersion_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 15),
    _CertVersion_Type()
)
certVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certVersion.setStatus("current")
_CertRowStatus_Type = RowStatus
_CertRowStatus_Object = MibTableColumn
certRowStatus = _CertRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 4, 1, 1, 16),
    _CertRowStatus_Type()
)
certRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    certRowStatus.setStatus("current")
_L2tp_ObjectIdentity = ObjectIdentity
l2tp = _L2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 5)
)


class _L2tpEnable_Type(Integer32):
    """Custom type l2tpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_L2tpEnable_Type.__name__ = "Integer32"
_L2tpEnable_Object = MibScalar
l2tpEnable = _L2tpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 5, 1),
    _L2tpEnable_Type()
)
l2tpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpEnable.setStatus("current")
_L2tpRemoteIpStartAddr_Type = BlueIpAddress
_L2tpRemoteIpStartAddr_Object = MibScalar
l2tpRemoteIpStartAddr = _L2tpRemoteIpStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 5, 2),
    _L2tpRemoteIpStartAddr_Type()
)
l2tpRemoteIpStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpRemoteIpStartAddr.setStatus("current")
_L2tpRemoteIpEndAddr_Type = BlueIpAddress
_L2tpRemoteIpEndAddr_Object = MibScalar
l2tpRemoteIpEndAddr = _L2tpRemoteIpEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 5, 3),
    _L2tpRemoteIpEndAddr_Type()
)
l2tpRemoteIpEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpRemoteIpEndAddr.setStatus("current")
_L2tpLocalIpAddr_Type = BlueIpAddress
_L2tpLocalIpAddr_Object = MibScalar
l2tpLocalIpAddr = _L2tpLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 5, 4),
    _L2tpLocalIpAddr_Type()
)
l2tpLocalIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpLocalIpAddr.setStatus("current")
_L2tpIdleTimeout_Type = Integer32
_L2tpIdleTimeout_Object = MibScalar
l2tpIdleTimeout = _L2tpIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 5, 5),
    _L2tpIdleTimeout_Type()
)
l2tpIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpIdleTimeout.setStatus("current")
_L2tpLdapPwdAttrName_Type = DisplayString
_L2tpLdapPwdAttrName_Object = MibScalar
l2tpLdapPwdAttrName = _L2tpLdapPwdAttrName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 5, 6),
    _L2tpLdapPwdAttrName_Type()
)
l2tpLdapPwdAttrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpLdapPwdAttrName.setStatus("current")
_L2tpRoleId_Type = Integer32
_L2tpRoleId_Object = MibScalar
l2tpRoleId = _L2tpRoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 6, 5, 7),
    _L2tpRoleId_Type()
)
l2tpRoleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpRoleId.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7)
)
_Http_ObjectIdentity = ObjectIdentity
http = _Http_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1)
)
_HttpPort_Type = DisplayString
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 1),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")
_HttpRedirect_Type = Integer32
_HttpRedirect_Object = MibScalar
httpRedirect = _HttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 2),
    _HttpRedirect_Type()
)
httpRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpRedirect.setStatus("current")


class _HttpAutoRedirectStatus_Type(Integer32):
    """Custom type httpAutoRedirectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpAutoRedirectStatus_Type.__name__ = "Integer32"
_HttpAutoRedirectStatus_Object = MibScalar
httpAutoRedirectStatus = _HttpAutoRedirectStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 3),
    _HttpAutoRedirectStatus_Type()
)
httpAutoRedirectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpAutoRedirectStatus.setStatus("current")
_HttpAutoPause_Type = Integer32
_HttpAutoPause_Object = MibScalar
httpAutoPause = _HttpAutoPause_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 4),
    _HttpAutoPause_Type()
)
httpAutoPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpAutoPause.setStatus("current")


class _HttpDefaultUrl_Type(OctetString):
    """Custom type httpDefaultUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HttpDefaultUrl_Type.__name__ = "OctetString"
_HttpDefaultUrl_Object = MibScalar
httpDefaultUrl = _HttpDefaultUrl_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 5),
    _HttpDefaultUrl_Type()
)
httpDefaultUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpDefaultUrl.setStatus("current")


class _HttpLogoutPopup_Type(Integer32):
    """Custom type httpLogoutPopup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpLogoutPopup_Type.__name__ = "Integer32"
_HttpLogoutPopup_Object = MibScalar
httpLogoutPopup = _HttpLogoutPopup_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 6),
    _HttpLogoutPopup_Type()
)
httpLogoutPopup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpLogoutPopup.setStatus("current")
_HttpRootCaUrl_Type = DisplayString
_HttpRootCaUrl_Object = MibScalar
httpRootCaUrl = _HttpRootCaUrl_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 7),
    _HttpRootCaUrl_Type()
)
httpRootCaUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpRootCaUrl.setStatus("current")


class _HttpExServerChoice_Type(Integer32):
    """Custom type httpExServerChoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpExServerChoice_Type.__name__ = "Integer32"
_HttpExServerChoice_Object = MibScalar
httpExServerChoice = _HttpExServerChoice_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 8),
    _HttpExServerChoice_Type()
)
httpExServerChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpExServerChoice.setStatus("current")


class _HttpPasswdChangeChoice_Type(Integer32):
    """Custom type httpPasswdChangeChoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpPasswdChangeChoice_Type.__name__ = "Integer32"
_HttpPasswdChangeChoice_Object = MibScalar
httpPasswdChangeChoice = _HttpPasswdChangeChoice_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 9),
    _HttpPasswdChangeChoice_Type()
)
httpPasswdChangeChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPasswdChangeChoice.setStatus("current")


class _HttpLangChangeChoice_Type(Integer32):
    """Custom type httpLangChangeChoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpLangChangeChoice_Type.__name__ = "Integer32"
_HttpLangChangeChoice_Object = MibScalar
httpLangChangeChoice = _HttpLangChangeChoice_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 10),
    _HttpLangChangeChoice_Type()
)
httpLangChangeChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpLangChangeChoice.setStatus("current")


class _HttpLoginHelpButton_Type(Integer32):
    """Custom type httpLoginHelpButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpLoginHelpButton_Type.__name__ = "Integer32"
_HttpLoginHelpButton_Object = MibScalar
httpLoginHelpButton = _HttpLoginHelpButton_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 11),
    _HttpLoginHelpButton_Type()
)
httpLoginHelpButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpLoginHelpButton.setStatus("current")
_HttpAttemptWait_Type = Integer32
_HttpAttemptWait_Object = MibScalar
httpAttemptWait = _HttpAttemptWait_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 12),
    _HttpAttemptWait_Type()
)
httpAttemptWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpAttemptWait.setStatus("current")
_HttpMaxNumOfActiveSess_Type = Integer32
_HttpMaxNumOfActiveSess_Object = MibScalar
httpMaxNumOfActiveSess = _HttpMaxNumOfActiveSess_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 13),
    _HttpMaxNumOfActiveSess_Type()
)
httpMaxNumOfActiveSess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpMaxNumOfActiveSess.setStatus("current")
_HttpAdminACL_Type = DisplayString
_HttpAdminACL_Object = MibScalar
httpAdminACL = _HttpAdminACL_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 14),
    _HttpAdminACL_Type()
)
httpAdminACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpAdminACL.setStatus("current")


class _HttpRedirectToHostName_Type(Integer32):
    """Custom type httpRedirectToHostName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpRedirectToHostName_Type.__name__ = "Integer32"
_HttpRedirectToHostName_Object = MibScalar
httpRedirectToHostName = _HttpRedirectToHostName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 15),
    _HttpRedirectToHostName_Type()
)
httpRedirectToHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpRedirectToHostName.setStatus("current")
_HttpLoginAttempts_Type = Integer32
_HttpLoginAttempts_Object = MibScalar
httpLoginAttempts = _HttpLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 16),
    _HttpLoginAttempts_Type()
)
httpLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpLoginAttempts.setStatus("current")


class _HttpChainCertChangeChoice_Type(Integer32):
    """Custom type httpChainCertChangeChoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpChainCertChangeChoice_Type.__name__ = "Integer32"
_HttpChainCertChangeChoice_Object = MibScalar
httpChainCertChangeChoice = _HttpChainCertChangeChoice_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 1, 17),
    _HttpChainCertChangeChoice_Type()
)
httpChainCertChangeChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpChainCertChangeChoice.setStatus("current")
_Misc_ObjectIdentity = ObjectIdentity
misc = _Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 2)
)
_StatusUpTime_Type = Integer32
_StatusUpTime_Object = MibScalar
statusUpTime = _StatusUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 2, 1),
    _StatusUpTime_Type()
)
statusUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusUpTime.setStatus("current")
_ConnectionCheckTime_Type = Integer32
_ConnectionCheckTime_Object = MibScalar
connectionCheckTime = _ConnectionCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 2, 2),
    _ConnectionCheckTime_Type()
)
connectionCheckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionCheckTime.setStatus("current")
_ApCheckTime_Type = Integer32
_ApCheckTime_Object = MibScalar
apCheckTime = _ApCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 2, 3),
    _ApCheckTime_Type()
)
apCheckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCheckTime.setStatus("current")
_StatusRefreshTime_Type = Integer32
_StatusRefreshTime_Object = MibScalar
statusRefreshTime = _StatusRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 2, 4),
    _StatusRefreshTime_Type()
)
statusRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusRefreshTime.setStatus("current")
_ApSnmpCommunity_Type = DisplayString
_ApSnmpCommunity_Object = MibScalar
apSnmpCommunity = _ApSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 2, 5),
    _ApSnmpCommunity_Type()
)
apSnmpCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpCommunity.setStatus("current")
_AutoBackup_ObjectIdentity = ObjectIdentity
autoBackup = _AutoBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 3)
)


class _AutoBkupRate_Type(OctetString):
    """Custom type autoBkupRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 7),
    )


_AutoBkupRate_Type.__name__ = "OctetString"
_AutoBkupRate_Object = MibScalar
autoBkupRate = _AutoBkupRate_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 3, 1),
    _AutoBkupRate_Type()
)
autoBkupRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBkupRate.setStatus("current")
_AutoBkupFtpServName_Type = DisplayString
_AutoBkupFtpServName_Object = MibScalar
autoBkupFtpServName = _AutoBkupFtpServName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 3, 2),
    _AutoBkupFtpServName_Type()
)
autoBkupFtpServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBkupFtpServName.setStatus("current")
_AutoBkupFtpDestDir_Type = DisplayString
_AutoBkupFtpDestDir_Object = MibScalar
autoBkupFtpDestDir = _AutoBkupFtpDestDir_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 3, 3),
    _AutoBkupFtpDestDir_Type()
)
autoBkupFtpDestDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBkupFtpDestDir.setStatus("current")
_AutoBkupFtpServUser_Type = DisplayString
_AutoBkupFtpServUser_Object = MibScalar
autoBkupFtpServUser = _AutoBkupFtpServUser_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 3, 4),
    _AutoBkupFtpServUser_Type()
)
autoBkupFtpServUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBkupFtpServUser.setStatus("current")
_AutoBkupFtpServPasswd_Type = DisplayString
_AutoBkupFtpServPasswd_Object = MibScalar
autoBkupFtpServPasswd = _AutoBkupFtpServPasswd_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 3, 5),
    _AutoBkupFtpServPasswd_Type()
)
autoBkupFtpServPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoBkupFtpServPasswd.setStatus("current")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4)
)
_TZone_Type = DisplayString
_TZone_Object = MibScalar
tZone = _TZone_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4, 1),
    _TZone_Type()
)
tZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tZone.setStatus("current")


class _TMonth_Type(Integer32):
    """Custom type tMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TMonth_Type.__name__ = "Integer32"
_TMonth_Object = MibScalar
tMonth = _TMonth_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4, 2),
    _TMonth_Type()
)
tMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMonth.setStatus("current")


class _TDay_Type(Integer32):
    """Custom type tDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TDay_Type.__name__ = "Integer32"
_TDay_Object = MibScalar
tDay = _TDay_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4, 3),
    _TDay_Type()
)
tDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDay.setStatus("current")


class _TYear_Type(Integer32):
    """Custom type tYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TYear_Type.__name__ = "Integer32"
_TYear_Object = MibScalar
tYear = _TYear_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4, 4),
    _TYear_Type()
)
tYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tYear.setStatus("current")


class _THours_Type(Integer32):
    """Custom type tHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_THours_Type.__name__ = "Integer32"
_THours_Object = MibScalar
tHours = _THours_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4, 5),
    _THours_Type()
)
tHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tHours.setStatus("current")


class _TMinutes_Type(Integer32):
    """Custom type tMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TMinutes_Type.__name__ = "Integer32"
_TMinutes_Object = MibScalar
tMinutes = _TMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4, 6),
    _TMinutes_Type()
)
tMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMinutes.setStatus("current")


class _TSeconds_Type(Integer32):
    """Custom type tSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TSeconds_Type.__name__ = "Integer32"
_TSeconds_Object = MibScalar
tSeconds = _TSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4, 7),
    _TSeconds_Type()
)
tSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSeconds.setStatus("current")
_TNtpSync_Type = DisplayString
_TNtpSync_Object = MibScalar
tNtpSync = _TNtpSync_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4, 8),
    _TNtpSync_Type()
)
tNtpSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNtpSync.setStatus("current")
_TNtpServers_Type = DisplayString
_TNtpServers_Object = MibScalar
tNtpServers = _TNtpServers_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 4, 9),
    _TNtpServers_Type()
)
tNtpServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNtpServers.setStatus("current")
_Mobility_ObjectIdentity = ObjectIdentity
mobility = _Mobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 5)
)


class _MobilityMode_Type(Integer32):
    """Custom type mobilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MobilityMode_Type.__name__ = "Integer32"
_MobilityMode_Object = MibScalar
mobilityMode = _MobilityMode_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 5, 1),
    _MobilityMode_Type()
)
mobilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilityMode.setStatus("current")
_MobilityMeshKey_Type = DisplayString
_MobilityMeshKey_Object = MibScalar
mobilityMeshKey = _MobilityMeshKey_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 5, 2),
    _MobilityMeshKey_Type()
)
mobilityMeshKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobilityMeshKey.setStatus("current")
_PublicAccess_ObjectIdentity = ObjectIdentity
publicAccess = _PublicAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 6)
)


class _PaFixedIpClientAccess_Type(Integer32):
    """Custom type paFixedIpClientAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PaFixedIpClientAccess_Type.__name__ = "Integer32"
_PaFixedIpClientAccess_Object = MibScalar
paFixedIpClientAccess = _PaFixedIpClientAccess_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 6, 1),
    _PaFixedIpClientAccess_Type()
)
paFixedIpClientAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paFixedIpClientAccess.setStatus("current")
_PaSMTPServerIp_Type = DisplayString
_PaSMTPServerIp_Object = MibScalar
paSMTPServerIp = _PaSMTPServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 6, 2),
    _PaSMTPServerIp_Type()
)
paSMTPServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paSMTPServerIp.setStatus("current")
_ConfLog_ObjectIdentity = ObjectIdentity
confLog = _ConfLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7)
)
_ConfLogGroup_ObjectIdentity = ObjectIdentity
confLogGroup = _ConfLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 1)
)
_LogMaxLogEntries_Type = Integer32
_LogMaxLogEntries_Object = MibScalar
logMaxLogEntries = _LogMaxLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 1, 1),
    _LogMaxLogEntries_Type()
)
logMaxLogEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMaxLogEntries.setStatus("current")
_LogNoOfDelLogEntries_Type = Integer32
_LogNoOfDelLogEntries_Object = MibScalar
logNoOfDelLogEntries = _LogNoOfDelLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 1, 2),
    _LogNoOfDelLogEntries_Type()
)
logNoOfDelLogEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logNoOfDelLogEntries.setStatus("current")


class _LogStorage_Type(Integer32):
    """Custom type logStorage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("local", 0),
          ("remote", 1))
    )


_LogStorage_Type.__name__ = "Integer32"
_LogStorage_Object = MibScalar
logStorage = _LogStorage_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 1, 3),
    _LogStorage_Type()
)
logStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logStorage.setStatus("current")
_RemoteLog_Type = DisplayString
_RemoteLog_Object = MibScalar
remoteLog = _RemoteLog_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 1, 4),
    _RemoteLog_Type()
)
remoteLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLog.setStatus("current")
_SysLogFacility_Type = DisplayString
_SysLogFacility_Object = MibScalar
sysLogFacility = _SysLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 1, 5),
    _SysLogFacility_Type()
)
sysLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFacility.setStatus("current")


class _LogMaxRemSysLogLevel_Type(Integer32):
    """Custom type logMaxRemSysLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LogMaxRemSysLogLevel_Type.__name__ = "Integer32"
_LogMaxRemSysLogLevel_Object = MibScalar
logMaxRemSysLogLevel = _LogMaxRemSysLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 1, 6),
    _LogMaxRemSysLogLevel_Type()
)
logMaxRemSysLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMaxRemSysLogLevel.setStatus("current")
_AppLogLevTable_Object = MibTable
appLogLevTable = _AppLogLevTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 3)
)
if mibBuilder.loadTexts:
    appLogLevTable.setStatus("current")
_AppLogLevEntry_Object = MibTableRow
appLogLevEntry = _AppLogLevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 3, 1)
)
appLogLevEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "appLogLevId"),
)
if mibBuilder.loadTexts:
    appLogLevEntry.setStatus("current")


class _AppLogLevId_Type(Integer32):
    """Custom type appLogLevId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AppLogLevId_Type.__name__ = "Integer32"
_AppLogLevId_Object = MibTableColumn
appLogLevId = _AppLogLevId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 3, 1, 1),
    _AppLogLevId_Type()
)
appLogLevId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLogLevId.setStatus("current")
_AppLogLevName_Type = DisplayString
_AppLogLevName_Object = MibTableColumn
appLogLevName = _AppLogLevName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 3, 1, 2),
    _AppLogLevName_Type()
)
appLogLevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogLevName.setStatus("current")


class _AppLogLevLevel_Type(Integer32):
    """Custom type appLogLevLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_AppLogLevLevel_Type.__name__ = "Integer32"
_AppLogLevLevel_Object = MibTableColumn
appLogLevLevel = _AppLogLevLevel_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 7, 3, 1, 3),
    _AppLogLevLevel_Type()
)
appLogLevLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appLogLevLevel.setStatus("current")
_SnmpConf_ObjectIdentity = ObjectIdentity
snmpConf = _SnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8)
)
_SnmpTrapConf_ObjectIdentity = ObjectIdentity
snmpTrapConf = _SnmpTrapConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1)
)
_SnmpTrapMgmtTable_Object = MibTable
snmpTrapMgmtTable = _SnmpTrapMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 1)
)
if mibBuilder.loadTexts:
    snmpTrapMgmtTable.setStatus("current")
_SnmpTrapMgmtEntry_Object = MibTableRow
snmpTrapMgmtEntry = _SnmpTrapMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 1, 1)
)
snmpTrapMgmtEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "snmpTrapMgmtId"),
)
if mibBuilder.loadTexts:
    snmpTrapMgmtEntry.setStatus("current")


class _SnmpTrapMgmtId_Type(Integer32):
    """Custom type snmpTrapMgmtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnmpTrapMgmtId_Type.__name__ = "Integer32"
_SnmpTrapMgmtId_Object = MibTableColumn
snmpTrapMgmtId = _SnmpTrapMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 1, 1, 1),
    _SnmpTrapMgmtId_Type()
)
snmpTrapMgmtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTrapMgmtId.setStatus("current")
_SnmpTrapMgmtIpAddress_Type = BlueIpAddress
_SnmpTrapMgmtIpAddress_Object = MibTableColumn
snmpTrapMgmtIpAddress = _SnmpTrapMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 1, 1, 2),
    _SnmpTrapMgmtIpAddress_Type()
)
snmpTrapMgmtIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapMgmtIpAddress.setStatus("current")
_SnmpTrapMgmtCommunity_Type = DisplayString
_SnmpTrapMgmtCommunity_Object = MibTableColumn
snmpTrapMgmtCommunity = _SnmpTrapMgmtCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 1, 1, 3),
    _SnmpTrapMgmtCommunity_Type()
)
snmpTrapMgmtCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapMgmtCommunity.setStatus("current")
_SnmpTrapMgmtRowStatus_Type = RowStatus
_SnmpTrapMgmtRowStatus_Object = MibTableColumn
snmpTrapMgmtRowStatus = _SnmpTrapMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 1, 1, 4),
    _SnmpTrapMgmtRowStatus_Type()
)
snmpTrapMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapMgmtRowStatus.setStatus("current")
_BlueEventTable_Object = MibTable
blueEventTable = _BlueEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 2)
)
if mibBuilder.loadTexts:
    blueEventTable.setStatus("current")
_BlueEventEntry_Object = MibTableRow
blueEventEntry = _BlueEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 2, 1)
)
blueEventEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "btId"),
)
if mibBuilder.loadTexts:
    blueEventEntry.setStatus("current")


class _BtId_Type(Integer32):
    """Custom type btId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BtId_Type.__name__ = "Integer32"
_BtId_Object = MibTableColumn
btId = _BtId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 2, 1, 1),
    _BtId_Type()
)
btId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btId.setStatus("current")
_BtName_Type = DisplayString
_BtName_Object = MibTableColumn
btName = _BtName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 2, 1, 2),
    _BtName_Type()
)
btName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btName.setStatus("current")


class _BtEventOptStatus_Type(Integer32):
    """Custom type btEventOptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BtEventOptStatus_Type.__name__ = "Integer32"
_BtEventOptStatus_Object = MibTableColumn
btEventOptStatus = _BtEventOptStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 8, 1, 2, 1, 3),
    _BtEventOptStatus_Type()
)
btEventOptStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btEventOptStatus.setStatus("current")
_SystemTracker_ObjectIdentity = ObjectIdentity
systemTracker = _SystemTracker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 9)
)
_StThresholdTable_Object = MibTable
stThresholdTable = _StThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 9, 1)
)
if mibBuilder.loadTexts:
    stThresholdTable.setStatus("current")
_StThresholdEntry_Object = MibTableRow
stThresholdEntry = _StThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 9, 1, 1)
)
stThresholdEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "stThresholdId"),
)
if mibBuilder.loadTexts:
    stThresholdEntry.setStatus("current")


class _StThresholdId_Type(Integer32):
    """Custom type stThresholdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StThresholdId_Type.__name__ = "Integer32"
_StThresholdId_Object = MibTableColumn
stThresholdId = _StThresholdId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 9, 1, 1, 1),
    _StThresholdId_Type()
)
stThresholdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stThresholdId.setStatus("current")
_StThresholdAttrName_Type = DisplayString
_StThresholdAttrName_Object = MibTableColumn
stThresholdAttrName = _StThresholdAttrName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 9, 1, 1, 2),
    _StThresholdAttrName_Type()
)
stThresholdAttrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stThresholdAttrName.setStatus("current")
_StThresholdToLogMessage_Type = Integer32
_StThresholdToLogMessage_Object = MibTableColumn
stThresholdToLogMessage = _StThresholdToLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 9, 1, 1, 3),
    _StThresholdToLogMessage_Type()
)
stThresholdToLogMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stThresholdToLogMessage.setStatus("current")
_StThresholdToSendTrap_Type = Integer32
_StThresholdToSendTrap_Object = MibTableColumn
stThresholdToSendTrap = _StThresholdToSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 9, 1, 1, 4),
    _StThresholdToSendTrap_Type()
)
stThresholdToSendTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stThresholdToSendTrap.setStatus("current")
_StThresholdToFailover_Type = Integer32
_StThresholdToFailover_Object = MibTableColumn
stThresholdToFailover = _StThresholdToFailover_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 9, 1, 1, 5),
    _StThresholdToFailover_Type()
)
stThresholdToFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stThresholdToFailover.setStatus("current")
_Authentication_ObjectIdentity = ObjectIdentity
authentication = _Authentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10)
)
_ExAuthServer_ObjectIdentity = ObjectIdentity
exAuthServer = _ExAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1)
)
_ExRdAuthServTable_Object = MibTable
exRdAuthServTable = _ExRdAuthServTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2)
)
if mibBuilder.loadTexts:
    exRdAuthServTable.setStatus("current")
_ExRdAuthServEntry_Object = MibTableRow
exRdAuthServEntry = _ExRdAuthServEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1)
)
exRdAuthServEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "exRdAuthServId"),
)
if mibBuilder.loadTexts:
    exRdAuthServEntry.setStatus("current")


class _ExRdAuthServId_Type(Integer32):
    """Custom type exRdAuthServId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExRdAuthServId_Type.__name__ = "Integer32"
_ExRdAuthServId_Object = MibTableColumn
exRdAuthServId = _ExRdAuthServId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 1),
    _ExRdAuthServId_Type()
)
exRdAuthServId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exRdAuthServId.setStatus("current")


class _ExRdAuthServState_Type(Integer32):
    """Custom type exRdAuthServState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ExRdAuthServState_Type.__name__ = "Integer32"
_ExRdAuthServState_Object = MibTableColumn
exRdAuthServState = _ExRdAuthServState_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 2),
    _ExRdAuthServState_Type()
)
exRdAuthServState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServState.setStatus("current")
_ExRdAuthServName_Type = DisplayString
_ExRdAuthServName_Object = MibTableColumn
exRdAuthServName = _ExRdAuthServName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 3),
    _ExRdAuthServName_Type()
)
exRdAuthServName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServName.setStatus("current")
_ExRdAuthServDefRoleId_Type = Integer32
_ExRdAuthServDefRoleId_Object = MibTableColumn
exRdAuthServDefRoleId = _ExRdAuthServDefRoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 4),
    _ExRdAuthServDefRoleId_Type()
)
exRdAuthServDefRoleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServDefRoleId.setStatus("current")
_ExRdAuthServRdAccId_Type = Integer32
_ExRdAuthServRdAccId_Object = MibTableColumn
exRdAuthServRdAccId = _ExRdAuthServRdAccId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 6),
    _ExRdAuthServRdAccId_Type()
)
exRdAuthServRdAccId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServRdAccId.setStatus("current")
_ExRdAuthServAddr_Type = DisplayString
_ExRdAuthServAddr_Object = MibTableColumn
exRdAuthServAddr = _ExRdAuthServAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 7),
    _ExRdAuthServAddr_Type()
)
exRdAuthServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServAddr.setStatus("current")
_ExRdAuthServPort_Type = Integer32
_ExRdAuthServPort_Object = MibTableColumn
exRdAuthServPort = _ExRdAuthServPort_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 8),
    _ExRdAuthServPort_Type()
)
exRdAuthServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServPort.setStatus("current")
_ExRdAuthServSecret_Type = DisplayString
_ExRdAuthServSecret_Object = MibTableColumn
exRdAuthServSecret = _ExRdAuthServSecret_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 9),
    _ExRdAuthServSecret_Type()
)
exRdAuthServSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServSecret.setStatus("current")
_ExRdAuthServPrecedence_Type = Integer32
_ExRdAuthServPrecedence_Object = MibTableColumn
exRdAuthServPrecedence = _ExRdAuthServPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 10),
    _ExRdAuthServPrecedence_Type()
)
exRdAuthServPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServPrecedence.setStatus("current")
_ExRdAuthServNotes_Type = DisplayString
_ExRdAuthServNotes_Object = MibTableColumn
exRdAuthServNotes = _ExRdAuthServNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 11),
    _ExRdAuthServNotes_Type()
)
exRdAuthServNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServNotes.setStatus("current")
_ExRdAuthServRowStatus_Type = RowStatus
_ExRdAuthServRowStatus_Object = MibTableColumn
exRdAuthServRowStatus = _ExRdAuthServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 2, 1, 12),
    _ExRdAuthServRowStatus_Type()
)
exRdAuthServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAuthServRowStatus.setStatus("current")
_ExLdapServTable_Object = MibTable
exLdapServTable = _ExLdapServTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3)
)
if mibBuilder.loadTexts:
    exLdapServTable.setStatus("current")
_ExLdapServEntry_Object = MibTableRow
exLdapServEntry = _ExLdapServEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1)
)
exLdapServEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "exLdapServId"),
)
if mibBuilder.loadTexts:
    exLdapServEntry.setStatus("current")


class _ExLdapServId_Type(Integer32):
    """Custom type exLdapServId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExLdapServId_Type.__name__ = "Integer32"
_ExLdapServId_Object = MibTableColumn
exLdapServId = _ExLdapServId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 1),
    _ExLdapServId_Type()
)
exLdapServId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exLdapServId.setStatus("current")


class _ExLdapServState_Type(Integer32):
    """Custom type exLdapServState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ExLdapServState_Type.__name__ = "Integer32"
_ExLdapServState_Object = MibTableColumn
exLdapServState = _ExLdapServState_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 2),
    _ExLdapServState_Type()
)
exLdapServState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServState.setStatus("current")
_ExLdapServName_Type = DisplayString
_ExLdapServName_Object = MibTableColumn
exLdapServName = _ExLdapServName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 3),
    _ExLdapServName_Type()
)
exLdapServName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServName.setStatus("current")
_ExLdapServDefRoleId_Type = Integer32
_ExLdapServDefRoleId_Object = MibTableColumn
exLdapServDefRoleId = _ExLdapServDefRoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 4),
    _ExLdapServDefRoleId_Type()
)
exLdapServDefRoleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServDefRoleId.setStatus("current")


class _ExLdapServRdAccState_Type(Integer32):
    """Custom type exLdapServRdAccState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ExLdapServRdAccState_Type.__name__ = "Integer32"
_ExLdapServRdAccState_Object = MibTableColumn
exLdapServRdAccState = _ExLdapServRdAccState_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 5),
    _ExLdapServRdAccState_Type()
)
exLdapServRdAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServRdAccState.setStatus("current")
_ExLdapServRdAccId_Type = Integer32
_ExLdapServRdAccId_Object = MibTableColumn
exLdapServRdAccId = _ExLdapServRdAccId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 6),
    _ExLdapServRdAccId_Type()
)
exLdapServRdAccId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServRdAccId.setStatus("current")
_ExLdapServAddr_Type = DisplayString
_ExLdapServAddr_Object = MibTableColumn
exLdapServAddr = _ExLdapServAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 7),
    _ExLdapServAddr_Type()
)
exLdapServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServAddr.setStatus("current")
_ExLdapServPort_Type = Integer32
_ExLdapServPort_Object = MibTableColumn
exLdapServPort = _ExLdapServPort_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 8),
    _ExLdapServPort_Type()
)
exLdapServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServPort.setStatus("current")
_ExLdapServBase_Type = DisplayString
_ExLdapServBase_Object = MibTableColumn
exLdapServBase = _ExLdapServBase_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 9),
    _ExLdapServBase_Type()
)
exLdapServBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServBase.setStatus("current")
_ExLdapServUniqueId_Type = DisplayString
_ExLdapServUniqueId_Object = MibTableColumn
exLdapServUniqueId = _ExLdapServUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 10),
    _ExLdapServUniqueId_Type()
)
exLdapServUniqueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServUniqueId.setStatus("current")
_ExLdapServAccount_Type = DisplayString
_ExLdapServAccount_Object = MibTableColumn
exLdapServAccount = _ExLdapServAccount_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 11),
    _ExLdapServAccount_Type()
)
exLdapServAccount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServAccount.setStatus("current")
_ExLdapServFilters_Type = DisplayString
_ExLdapServFilters_Object = MibTableColumn
exLdapServFilters = _ExLdapServFilters_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 12),
    _ExLdapServFilters_Type()
)
exLdapServFilters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServFilters.setStatus("current")
_ExLdapServSecret_Type = DisplayString
_ExLdapServSecret_Object = MibTableColumn
exLdapServSecret = _ExLdapServSecret_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 13),
    _ExLdapServSecret_Type()
)
exLdapServSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServSecret.setStatus("current")
_ExLdapServPrecedence_Type = Integer32
_ExLdapServPrecedence_Object = MibTableColumn
exLdapServPrecedence = _ExLdapServPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 14),
    _ExLdapServPrecedence_Type()
)
exLdapServPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServPrecedence.setStatus("current")
_ExLdapServNotes_Type = DisplayString
_ExLdapServNotes_Object = MibTableColumn
exLdapServNotes = _ExLdapServNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 15),
    _ExLdapServNotes_Type()
)
exLdapServNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServNotes.setStatus("current")


class _ExLdapServSsl_Type(OctetString):
    """Custom type exLdapServSsl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExLdapServSsl_Type.__name__ = "OctetString"
_ExLdapServSsl_Object = MibTableColumn
exLdapServSsl = _ExLdapServSsl_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 17),
    _ExLdapServSsl_Type()
)
exLdapServSsl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServSsl.setStatus("current")
_ExLdapServSslServer_Type = Integer32
_ExLdapServSslServer_Object = MibTableColumn
exLdapServSslServer = _ExLdapServSslServer_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 18),
    _ExLdapServSslServer_Type()
)
exLdapServSslServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServSslServer.setStatus("current")
_ExLdapServSslClient_Type = Integer32
_ExLdapServSslClient_Object = MibTableColumn
exLdapServSslClient = _ExLdapServSslClient_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 19),
    _ExLdapServSslClient_Type()
)
exLdapServSslClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServSslClient.setStatus("current")
_ExLdapServRowStatus_Type = RowStatus
_ExLdapServRowStatus_Object = MibTableColumn
exLdapServRowStatus = _ExLdapServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 3, 1, 20),
    _ExLdapServRowStatus_Type()
)
exLdapServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exLdapServRowStatus.setStatus("current")
_ExNtlmServTable_Object = MibTable
exNtlmServTable = _ExNtlmServTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4)
)
if mibBuilder.loadTexts:
    exNtlmServTable.setStatus("current")
_ExNtlmServEntry_Object = MibTableRow
exNtlmServEntry = _ExNtlmServEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1)
)
exNtlmServEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "exNtlmServId"),
)
if mibBuilder.loadTexts:
    exNtlmServEntry.setStatus("current")


class _ExNtlmServId_Type(Integer32):
    """Custom type exNtlmServId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExNtlmServId_Type.__name__ = "Integer32"
_ExNtlmServId_Object = MibTableColumn
exNtlmServId = _ExNtlmServId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 1),
    _ExNtlmServId_Type()
)
exNtlmServId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exNtlmServId.setStatus("current")


class _ExNtlmServState_Type(Integer32):
    """Custom type exNtlmServState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ExNtlmServState_Type.__name__ = "Integer32"
_ExNtlmServState_Object = MibTableColumn
exNtlmServState = _ExNtlmServState_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 2),
    _ExNtlmServState_Type()
)
exNtlmServState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServState.setStatus("current")
_ExNtlmServName_Type = DisplayString
_ExNtlmServName_Object = MibTableColumn
exNtlmServName = _ExNtlmServName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 3),
    _ExNtlmServName_Type()
)
exNtlmServName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServName.setStatus("current")


class _ExNtlmServRdAccState_Type(Integer32):
    """Custom type exNtlmServRdAccState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ExNtlmServRdAccState_Type.__name__ = "Integer32"
_ExNtlmServRdAccState_Object = MibTableColumn
exNtlmServRdAccState = _ExNtlmServRdAccState_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 4),
    _ExNtlmServRdAccState_Type()
)
exNtlmServRdAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServRdAccState.setStatus("current")
_ExNtlmServRdAccId_Type = Integer32
_ExNtlmServRdAccId_Object = MibTableColumn
exNtlmServRdAccId = _ExNtlmServRdAccId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 5),
    _ExNtlmServRdAccId_Type()
)
exNtlmServRdAccId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServRdAccId.setStatus("current")
_ExNtlmServDefRoleId_Type = Integer32
_ExNtlmServDefRoleId_Object = MibTableColumn
exNtlmServDefRoleId = _ExNtlmServDefRoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 6),
    _ExNtlmServDefRoleId_Type()
)
exNtlmServDefRoleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServDefRoleId.setStatus("current")
_ExNtlmServDomainName_Type = DisplayString
_ExNtlmServDomainName_Object = MibTableColumn
exNtlmServDomainName = _ExNtlmServDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 7),
    _ExNtlmServDomainName_Type()
)
exNtlmServDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServDomainName.setStatus("current")
_ExNtlmServMsdc_Type = DisplayString
_ExNtlmServMsdc_Object = MibTableColumn
exNtlmServMsdc = _ExNtlmServMsdc_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 8),
    _ExNtlmServMsdc_Type()
)
exNtlmServMsdc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServMsdc.setStatus("current")
_ExNtlmServMsrpc_Type = DisplayString
_ExNtlmServMsrpc_Object = MibTableColumn
exNtlmServMsrpc = _ExNtlmServMsrpc_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 9),
    _ExNtlmServMsrpc_Type()
)
exNtlmServMsrpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServMsrpc.setStatus("current")
_ExNtlmServMsad_Type = Integer32
_ExNtlmServMsad_Object = MibTableColumn
exNtlmServMsad = _ExNtlmServMsad_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 10),
    _ExNtlmServMsad_Type()
)
exNtlmServMsad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServMsad.setStatus("current")
_ExNtlmServNotes_Type = DisplayString
_ExNtlmServNotes_Object = MibTableColumn
exNtlmServNotes = _ExNtlmServNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 11),
    _ExNtlmServNotes_Type()
)
exNtlmServNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServNotes.setStatus("current")
_ExNtlmServRowStatus_Type = RowStatus
_ExNtlmServRowStatus_Object = MibTableColumn
exNtlmServRowStatus = _ExNtlmServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 4, 1, 12),
    _ExNtlmServRowStatus_Type()
)
exNtlmServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exNtlmServRowStatus.setStatus("current")
_ExUserRuleTable_Object = MibTable
exUserRuleTable = _ExUserRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5)
)
if mibBuilder.loadTexts:
    exUserRuleTable.setStatus("current")
_ExUserRuleEntry_Object = MibTableRow
exUserRuleEntry = _ExUserRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5, 1)
)
exUserRuleEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "exServId"),
    (0, "BLUESERVER-MIB", "exUserRuleId"),
)
if mibBuilder.loadTexts:
    exUserRuleEntry.setStatus("current")


class _ExServId_Type(Integer32):
    """Custom type exServId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExServId_Type.__name__ = "Integer32"
_ExServId_Object = MibTableColumn
exServId = _ExServId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5, 1, 1),
    _ExServId_Type()
)
exServId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exServId.setStatus("current")


class _ExUserRuleId_Type(Integer32):
    """Custom type exUserRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExUserRuleId_Type.__name__ = "Integer32"
_ExUserRuleId_Object = MibTableColumn
exUserRuleId = _ExUserRuleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5, 1, 2),
    _ExUserRuleId_Type()
)
exUserRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exUserRuleId.setStatus("current")


class _ExUserRuleAttribute_Type(OctetString):
    """Custom type exUserRuleAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ExUserRuleAttribute_Type.__name__ = "OctetString"
_ExUserRuleAttribute_Object = MibTableColumn
exUserRuleAttribute = _ExUserRuleAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5, 1, 3),
    _ExUserRuleAttribute_Type()
)
exUserRuleAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exUserRuleAttribute.setStatus("current")


class _ExUserRuleOperator_Type(OctetString):
    """Custom type exUserRuleOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_ExUserRuleOperator_Type.__name__ = "OctetString"
_ExUserRuleOperator_Object = MibTableColumn
exUserRuleOperator = _ExUserRuleOperator_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5, 1, 4),
    _ExUserRuleOperator_Type()
)
exUserRuleOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exUserRuleOperator.setStatus("current")


class _ExUserRuleValue_Type(OctetString):
    """Custom type exUserRuleValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ExUserRuleValue_Type.__name__ = "OctetString"
_ExUserRuleValue_Object = MibTableColumn
exUserRuleValue = _ExUserRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5, 1, 5),
    _ExUserRuleValue_Type()
)
exUserRuleValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exUserRuleValue.setStatus("current")
_ExUserRuleRoleId_Type = Integer32
_ExUserRuleRoleId_Object = MibTableColumn
exUserRuleRoleId = _ExUserRuleRoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5, 1, 6),
    _ExUserRuleRoleId_Type()
)
exUserRuleRoleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exUserRuleRoleId.setStatus("current")
_ExUserRuleSeqId_Type = Integer32
_ExUserRuleSeqId_Object = MibTableColumn
exUserRuleSeqId = _ExUserRuleSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5, 1, 7),
    _ExUserRuleSeqId_Type()
)
exUserRuleSeqId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exUserRuleSeqId.setStatus("current")
_ExUserRuleRowStatus_Type = RowStatus
_ExUserRuleRowStatus_Object = MibTableColumn
exUserRuleRowStatus = _ExUserRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 5, 1, 8),
    _ExUserRuleRowStatus_Type()
)
exUserRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exUserRuleRowStatus.setStatus("current")
_ExRdAccServTable_Object = MibTable
exRdAccServTable = _ExRdAccServTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6)
)
if mibBuilder.loadTexts:
    exRdAccServTable.setStatus("current")
_ExRdAccServEntry_Object = MibTableRow
exRdAccServEntry = _ExRdAccServEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6, 1)
)
exRdAccServEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "exRdAccServId"),
)
if mibBuilder.loadTexts:
    exRdAccServEntry.setStatus("current")


class _ExRdAccServId_Type(Integer32):
    """Custom type exRdAccServId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExRdAccServId_Type.__name__ = "Integer32"
_ExRdAccServId_Object = MibTableColumn
exRdAccServId = _ExRdAccServId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6, 1, 1),
    _ExRdAccServId_Type()
)
exRdAccServId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exRdAccServId.setStatus("current")


class _ExRdAccServState_Type(Integer32):
    """Custom type exRdAccServState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ExRdAccServState_Type.__name__ = "Integer32"
_ExRdAccServState_Object = MibTableColumn
exRdAccServState = _ExRdAccServState_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6, 1, 2),
    _ExRdAccServState_Type()
)
exRdAccServState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAccServState.setStatus("current")
_ExRdAccServName_Type = DisplayString
_ExRdAccServName_Object = MibTableColumn
exRdAccServName = _ExRdAccServName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6, 1, 3),
    _ExRdAccServName_Type()
)
exRdAccServName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAccServName.setStatus("current")
_ExRdAccServAddr_Type = DisplayString
_ExRdAccServAddr_Object = MibTableColumn
exRdAccServAddr = _ExRdAccServAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6, 1, 4),
    _ExRdAccServAddr_Type()
)
exRdAccServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAccServAddr.setStatus("current")
_ExRdAccServPort_Type = Integer32
_ExRdAccServPort_Object = MibTableColumn
exRdAccServPort = _ExRdAccServPort_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6, 1, 5),
    _ExRdAccServPort_Type()
)
exRdAccServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAccServPort.setStatus("current")
_ExRdAccServSecret_Type = DisplayString
_ExRdAccServSecret_Object = MibTableColumn
exRdAccServSecret = _ExRdAccServSecret_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6, 1, 6),
    _ExRdAccServSecret_Type()
)
exRdAccServSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAccServSecret.setStatus("current")
_ExRdAccServNotes_Type = DisplayString
_ExRdAccServNotes_Object = MibTableColumn
exRdAccServNotes = _ExRdAccServNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6, 1, 7),
    _ExRdAccServNotes_Type()
)
exRdAccServNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAccServNotes.setStatus("current")
_ExRdAccServRowStatus_Type = RowStatus
_ExRdAccServRowStatus_Object = MibTableColumn
exRdAccServRowStatus = _ExRdAccServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 6, 1, 8),
    _ExRdAccServRowStatus_Type()
)
exRdAccServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    exRdAccServRowStatus.setStatus("current")
_Ex802AuthServTable_Object = MibTable
ex802AuthServTable = _Ex802AuthServTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7)
)
if mibBuilder.loadTexts:
    ex802AuthServTable.setStatus("current")
_Ex802AuthServEntry_Object = MibTableRow
ex802AuthServEntry = _Ex802AuthServEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7, 1)
)
ex802AuthServEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "ex802AuthServId"),
)
if mibBuilder.loadTexts:
    ex802AuthServEntry.setStatus("current")


class _Ex802AuthServId_Type(Integer32):
    """Custom type ex802AuthServId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ex802AuthServId_Type.__name__ = "Integer32"
_Ex802AuthServId_Object = MibTableColumn
ex802AuthServId = _Ex802AuthServId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7, 1, 1),
    _Ex802AuthServId_Type()
)
ex802AuthServId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ex802AuthServId.setStatus("current")


class _Ex802AuthServState_Type(Integer32):
    """Custom type ex802AuthServState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ex802AuthServState_Type.__name__ = "Integer32"
_Ex802AuthServState_Object = MibTableColumn
ex802AuthServState = _Ex802AuthServState_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7, 1, 2),
    _Ex802AuthServState_Type()
)
ex802AuthServState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ex802AuthServState.setStatus("current")
_Ex802AuthServName_Type = DisplayString
_Ex802AuthServName_Object = MibTableColumn
ex802AuthServName = _Ex802AuthServName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7, 1, 3),
    _Ex802AuthServName_Type()
)
ex802AuthServName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ex802AuthServName.setStatus("current")
_Ex802AuthServAddr_Type = DisplayString
_Ex802AuthServAddr_Object = MibTableColumn
ex802AuthServAddr = _Ex802AuthServAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7, 1, 4),
    _Ex802AuthServAddr_Type()
)
ex802AuthServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ex802AuthServAddr.setStatus("current")
_Ex802AuthServPort_Type = Integer32
_Ex802AuthServPort_Object = MibTableColumn
ex802AuthServPort = _Ex802AuthServPort_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7, 1, 5),
    _Ex802AuthServPort_Type()
)
ex802AuthServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ex802AuthServPort.setStatus("current")
_Ex802AuthServDefaultRole_Type = Integer32
_Ex802AuthServDefaultRole_Object = MibTableColumn
ex802AuthServDefaultRole = _Ex802AuthServDefaultRole_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7, 1, 6),
    _Ex802AuthServDefaultRole_Type()
)
ex802AuthServDefaultRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ex802AuthServDefaultRole.setStatus("current")
_Ex802AuthServNotes_Type = DisplayString
_Ex802AuthServNotes_Object = MibTableColumn
ex802AuthServNotes = _Ex802AuthServNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7, 1, 7),
    _Ex802AuthServNotes_Type()
)
ex802AuthServNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ex802AuthServNotes.setStatus("current")
_Ex802AuthServRowStatus_Type = RowStatus
_Ex802AuthServRowStatus_Object = MibTableColumn
ex802AuthServRowStatus = _Ex802AuthServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 1, 7, 1, 8),
    _Ex802AuthServRowStatus_Type()
)
ex802AuthServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ex802AuthServRowStatus.setStatus("current")
_MacDevAuthTable_Object = MibTable
macDevAuthTable = _MacDevAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 2)
)
if mibBuilder.loadTexts:
    macDevAuthTable.setStatus("current")
_MacDevAuthEntry_Object = MibTableRow
macDevAuthEntry = _MacDevAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 2, 1)
)
macDevAuthEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "macDevAuthId"),
)
if mibBuilder.loadTexts:
    macDevAuthEntry.setStatus("current")


class _MacDevAuthId_Type(Integer32):
    """Custom type macDevAuthId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MacDevAuthId_Type.__name__ = "Integer32"
_MacDevAuthId_Object = MibTableColumn
macDevAuthId = _MacDevAuthId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 2, 1, 1),
    _MacDevAuthId_Type()
)
macDevAuthId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macDevAuthId.setStatus("current")


class _MacDevAuthState_Type(Integer32):
    """Custom type macDevAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MacDevAuthState_Type.__name__ = "Integer32"
_MacDevAuthState_Object = MibTableColumn
macDevAuthState = _MacDevAuthState_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 2, 1, 2),
    _MacDevAuthState_Type()
)
macDevAuthState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macDevAuthState.setStatus("current")
_MacDevAuthName_Type = DisplayString
_MacDevAuthName_Object = MibTableColumn
macDevAuthName = _MacDevAuthName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 2, 1, 3),
    _MacDevAuthName_Type()
)
macDevAuthName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macDevAuthName.setStatus("current")
_MacDevAuthMac_Type = DisplayString
_MacDevAuthMac_Object = MibTableColumn
macDevAuthMac = _MacDevAuthMac_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 2, 1, 4),
    _MacDevAuthMac_Type()
)
macDevAuthMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macDevAuthMac.setStatus("current")
_MacDevAuthDefaultRole_Type = Integer32
_MacDevAuthDefaultRole_Object = MibTableColumn
macDevAuthDefaultRole = _MacDevAuthDefaultRole_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 2, 1, 5),
    _MacDevAuthDefaultRole_Type()
)
macDevAuthDefaultRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macDevAuthDefaultRole.setStatus("current")
_MacDevAuthNotes_Type = DisplayString
_MacDevAuthNotes_Object = MibTableColumn
macDevAuthNotes = _MacDevAuthNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 2, 1, 6),
    _MacDevAuthNotes_Type()
)
macDevAuthNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macDevAuthNotes.setStatus("current")
_MacDevAuthRowStatus_Type = RowStatus
_MacDevAuthRowStatus_Object = MibTableColumn
macDevAuthRowStatus = _MacDevAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 7, 10, 2, 1, 7),
    _MacDevAuthRowStatus_Type()
)
macDevAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macDevAuthRowStatus.setStatus("current")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8)
)
_Failover_ObjectIdentity = ObjectIdentity
failover = _Failover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 3)
)
_HeartBeatInterval_Type = Integer32
_HeartBeatInterval_Object = MibScalar
heartBeatInterval = _HeartBeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 3, 1),
    _HeartBeatInterval_Type()
)
heartBeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heartBeatInterval.setStatus("current")
_NoOfFailedBeats_Type = Integer32
_NoOfFailedBeats_Object = MibScalar
noOfFailedBeats = _NoOfFailedBeats_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 3, 2),
    _NoOfFailedBeats_Type()
)
noOfFailedBeats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noOfFailedBeats.setStatus("current")
_Managed_ObjectIdentity = ObjectIdentity
managed = _Managed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4)
)
_MIntTable_Object = MibTable
mIntTable = _MIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    mIntTable.setStatus("current")
_MIntEntry_Object = MibTableRow
mIntEntry = _MIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1)
)
mIntEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "mIntId"),
)
if mibBuilder.loadTexts:
    mIntEntry.setStatus("current")


class _MIntId_Type(Integer32):
    """Custom type mIntId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MIntId_Type.__name__ = "Integer32"
_MIntId_Object = MibTableColumn
mIntId = _MIntId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 1),
    _MIntId_Type()
)
mIntId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mIntId.setStatus("current")
_MIntName_Type = DisplayString
_MIntName_Object = MibTableColumn
mIntName = _MIntName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 2),
    _MIntName_Type()
)
mIntName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntName.setStatus("current")


class _MIntEnableDhcpRelay_Type(Integer32):
    """Custom type mIntEnableDhcpRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MIntEnableDhcpRelay_Type.__name__ = "Integer32"
_MIntEnableDhcpRelay_Object = MibTableColumn
mIntEnableDhcpRelay = _MIntEnableDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 3),
    _MIntEnableDhcpRelay_Type()
)
mIntEnableDhcpRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntEnableDhcpRelay.setStatus("current")
_MIntIpAddress_Type = BlueIpAddress
_MIntIpAddress_Object = MibTableColumn
mIntIpAddress = _MIntIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 4),
    _MIntIpAddress_Type()
)
mIntIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntIpAddress.setStatus("current")
_MIntNetmask_Type = BlueIpAddress
_MIntNetmask_Object = MibTableColumn
mIntNetmask = _MIntNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 5),
    _MIntNetmask_Type()
)
mIntNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntNetmask.setStatus("current")


class _MIntDhcpServerOpt_Type(Integer32):
    """Custom type mIntDhcpServerOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 0))
    )


_MIntDhcpServerOpt_Type.__name__ = "Integer32"
_MIntDhcpServerOpt_Object = MibTableColumn
mIntDhcpServerOpt = _MIntDhcpServerOpt_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 6),
    _MIntDhcpServerOpt_Type()
)
mIntDhcpServerOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntDhcpServerOpt.setStatus("current")


class _MIntNatAddresses_Type(Integer32):
    """Custom type mIntNatAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MIntNatAddresses_Type.__name__ = "Integer32"
_MIntNatAddresses_Object = MibTableColumn
mIntNatAddresses = _MIntNatAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 7),
    _MIntNatAddresses_Type()
)
mIntNatAddresses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntNatAddresses.setStatus("current")


class _MIntMulticastOpt_Type(Integer32):
    """Custom type mIntMulticastOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MIntMulticastOpt_Type.__name__ = "Integer32"
_MIntMulticastOpt_Object = MibTableColumn
mIntMulticastOpt = _MIntMulticastOpt_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 8),
    _MIntMulticastOpt_Type()
)
mIntMulticastOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntMulticastOpt.setStatus("current")
_MIntDhcpStartIpAddr_Type = BlueIpAddress
_MIntDhcpStartIpAddr_Object = MibTableColumn
mIntDhcpStartIpAddr = _MIntDhcpStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 9),
    _MIntDhcpStartIpAddr_Type()
)
mIntDhcpStartIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mIntDhcpStartIpAddr.setStatus("current")
_MIntDhcpEndIpAddr_Type = BlueIpAddress
_MIntDhcpEndIpAddr_Object = MibTableColumn
mIntDhcpEndIpAddr = _MIntDhcpEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 10),
    _MIntDhcpEndIpAddr_Type()
)
mIntDhcpEndIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntDhcpEndIpAddr.setStatus("current")
_MIntNetbiosNameServ_Type = BlueIpAddress
_MIntNetbiosNameServ_Object = MibTableColumn
mIntNetbiosNameServ = _MIntNetbiosNameServ_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 11),
    _MIntNetbiosNameServ_Type()
)
mIntNetbiosNameServ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntNetbiosNameServ.setStatus("current")


class _MIntDnsDomainName_Type(OctetString):
    """Custom type mIntDnsDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_MIntDnsDomainName_Type.__name__ = "OctetString"
_MIntDnsDomainName_Object = MibTableColumn
mIntDnsDomainName = _MIntDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 12),
    _MIntDnsDomainName_Type()
)
mIntDnsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntDnsDomainName.setStatus("current")
_MIntDefaultLease_Type = Integer32
_MIntDefaultLease_Object = MibTableColumn
mIntDefaultLease = _MIntDefaultLease_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 13),
    _MIntDefaultLease_Type()
)
mIntDefaultLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntDefaultLease.setStatus("current")
_MIntMaximumLease_Type = Integer32
_MIntMaximumLease_Object = MibTableColumn
mIntMaximumLease = _MIntMaximumLease_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 14),
    _MIntMaximumLease_Type()
)
mIntMaximumLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntMaximumLease.setStatus("current")


class _MIntDynamicDNS_Type(Integer32):
    """Custom type mIntDynamicDNS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adHoc", 2),
          ("disabled", 1),
          ("interim", 3))
    )


_MIntDynamicDNS_Type.__name__ = "Integer32"
_MIntDynamicDNS_Object = MibTableColumn
mIntDynamicDNS = _MIntDynamicDNS_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 15),
    _MIntDynamicDNS_Type()
)
mIntDynamicDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntDynamicDNS.setStatus("current")
_MIntVlanId_Type = Integer32
_MIntVlanId_Object = MibTableColumn
mIntVlanId = _MIntVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 16),
    _MIntVlanId_Type()
)
mIntVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mIntVlanId.setStatus("current")
_MIntVlanInterface_Type = Integer32
_MIntVlanInterface_Object = MibTableColumn
mIntVlanInterface = _MIntVlanInterface_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 17),
    _MIntVlanInterface_Type()
)
mIntVlanInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntVlanInterface.setStatus("current")


class _MIntProxyArpStatus_Type(Integer32):
    """Custom type mIntProxyArpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MIntProxyArpStatus_Type.__name__ = "Integer32"
_MIntProxyArpStatus_Object = MibTableColumn
mIntProxyArpStatus = _MIntProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 18),
    _MIntProxyArpStatus_Type()
)
mIntProxyArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntProxyArpStatus.setStatus("current")
_MIntRowStatus_Type = RowStatus
_MIntRowStatus_Object = MibTableColumn
mIntRowStatus = _MIntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 1, 1, 19),
    _MIntRowStatus_Type()
)
mIntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mIntRowStatus.setStatus("current")
_FixedIpAddrTable_Object = MibTable
fixedIpAddrTable = _FixedIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 2)
)
if mibBuilder.loadTexts:
    fixedIpAddrTable.setStatus("current")
_FixedIpAddrEntry_Object = MibTableRow
fixedIpAddrEntry = _FixedIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 2, 1)
)
fixedIpAddrEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "mIntId"),
    (0, "BLUESERVER-MIB", "fixedIpAddrId"),
)
if mibBuilder.loadTexts:
    fixedIpAddrEntry.setStatus("current")


class _FixedIpAddrId_Type(Integer32):
    """Custom type fixedIpAddrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FixedIpAddrId_Type.__name__ = "Integer32"
_FixedIpAddrId_Object = MibTableColumn
fixedIpAddrId = _FixedIpAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 2, 1, 1),
    _FixedIpAddrId_Type()
)
fixedIpAddrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fixedIpAddrId.setStatus("current")


class _FixedIpAddrMac_Type(OctetString):
    """Custom type fixedIpAddrMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_FixedIpAddrMac_Type.__name__ = "OctetString"
_FixedIpAddrMac_Object = MibTableColumn
fixedIpAddrMac = _FixedIpAddrMac_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 2, 1, 2),
    _FixedIpAddrMac_Type()
)
fixedIpAddrMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fixedIpAddrMac.setStatus("current")
_FixedIpAddrAddress_Type = BlueIpAddress
_FixedIpAddrAddress_Object = MibTableColumn
fixedIpAddrAddress = _FixedIpAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 2, 1, 3),
    _FixedIpAddrAddress_Type()
)
fixedIpAddrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fixedIpAddrAddress.setStatus("current")
_FixedIpAddrHost_Type = BlueIpAddress
_FixedIpAddrHost_Object = MibTableColumn
fixedIpAddrHost = _FixedIpAddrHost_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 2, 1, 4),
    _FixedIpAddrHost_Type()
)
fixedIpAddrHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fixedIpAddrHost.setStatus("current")
_FixedIpAddrRoleId_Type = Integer32
_FixedIpAddrRoleId_Object = MibTableColumn
fixedIpAddrRoleId = _FixedIpAddrRoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 2, 1, 5),
    _FixedIpAddrRoleId_Type()
)
fixedIpAddrRoleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fixedIpAddrRoleId.setStatus("current")
_FixedIpAddrRowStatus_Type = RowStatus
_FixedIpAddrRowStatus_Object = MibTableColumn
fixedIpAddrRowStatus = _FixedIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 2, 1, 6),
    _FixedIpAddrRowStatus_Type()
)
fixedIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fixedIpAddrRowStatus.setStatus("current")
_NatTable_Object = MibTable
natTable = _NatTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 3)
)
if mibBuilder.loadTexts:
    natTable.setStatus("current")
_NatEntry_Object = MibTableRow
natEntry = _NatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 3, 1)
)
natEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "mIntId"),
    (0, "BLUESERVER-MIB", "natId"),
)
if mibBuilder.loadTexts:
    natEntry.setStatus("current")


class _NatId_Type(Integer32):
    """Custom type natId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NatId_Type.__name__ = "Integer32"
_NatId_Object = MibTableColumn
natId = _NatId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 3, 1, 1),
    _NatId_Type()
)
natId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natId.setStatus("current")
_NatProtectedIp_Type = BlueIpAddress
_NatProtectedIp_Object = MibTableColumn
natProtectedIp = _NatProtectedIp_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 3, 1, 2),
    _NatProtectedIp_Type()
)
natProtectedIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natProtectedIp.setStatus("current")
_NatManagedIp_Type = BlueIpAddress
_NatManagedIp_Object = MibTableColumn
natManagedIp = _NatManagedIp_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 3, 1, 3),
    _NatManagedIp_Type()
)
natManagedIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natManagedIp.setStatus("current")
_NatRowStatus_Type = RowStatus
_NatRowStatus_Object = MibTableColumn
natRowStatus = _NatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 4, 3, 1, 4),
    _NatRowStatus_Type()
)
natRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natRowStatus.setStatus("current")
_Protected_ObjectIdentity = ObjectIdentity
protected = _Protected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5)
)
_PIntTable_Object = MibTable
pIntTable = _PIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1)
)
if mibBuilder.loadTexts:
    pIntTable.setStatus("current")
_PIntEntry_Object = MibTableRow
pIntEntry = _PIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1)
)
pIntEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "pIntId"),
)
if mibBuilder.loadTexts:
    pIntEntry.setStatus("current")


class _PIntId_Type(Integer32):
    """Custom type pIntId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PIntId_Type.__name__ = "Integer32"
_PIntId_Object = MibTableColumn
pIntId = _PIntId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 1),
    _PIntId_Type()
)
pIntId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pIntId.setStatus("current")
_PIntName_Type = DisplayString
_PIntName_Object = MibTableColumn
pIntName = _PIntName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 2),
    _PIntName_Type()
)
pIntName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntName.setStatus("current")


class _PIntGetIpFromDhcp_Type(Integer32):
    """Custom type pIntGetIpFromDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PIntGetIpFromDhcp_Type.__name__ = "Integer32"
_PIntGetIpFromDhcp_Object = MibTableColumn
pIntGetIpFromDhcp = _PIntGetIpFromDhcp_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 3),
    _PIntGetIpFromDhcp_Type()
)
pIntGetIpFromDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntGetIpFromDhcp.setStatus("current")
_PIntDhcpTimeout_Type = Integer32
_PIntDhcpTimeout_Object = MibTableColumn
pIntDhcpTimeout = _PIntDhcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 4),
    _PIntDhcpTimeout_Type()
)
pIntDhcpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntDhcpTimeout.setStatus("current")
_PIntIpAddress_Type = BlueIpAddress
_PIntIpAddress_Object = MibTableColumn
pIntIpAddress = _PIntIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 5),
    _PIntIpAddress_Type()
)
pIntIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntIpAddress.setStatus("current")
_PIntNetmask_Type = BlueIpAddress
_PIntNetmask_Object = MibTableColumn
pIntNetmask = _PIntNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 6),
    _PIntNetmask_Type()
)
pIntNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntNetmask.setStatus("current")
_PIntGateway_Type = BlueIpAddress
_PIntGateway_Object = MibTableColumn
pIntGateway = _PIntGateway_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 7),
    _PIntGateway_Type()
)
pIntGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntGateway.setStatus("current")
_PIntPrimaryDNS_Type = BlueIpAddress
_PIntPrimaryDNS_Object = MibTableColumn
pIntPrimaryDNS = _PIntPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 8),
    _PIntPrimaryDNS_Type()
)
pIntPrimaryDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntPrimaryDNS.setStatus("current")
_PIntSecondaryDNS_Type = BlueIpAddress
_PIntSecondaryDNS_Object = MibTableColumn
pIntSecondaryDNS = _PIntSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 9),
    _PIntSecondaryDNS_Type()
)
pIntSecondaryDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntSecondaryDNS.setStatus("current")


class _PIntDefaultDomain_Type(OctetString):
    """Custom type pIntDefaultDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_PIntDefaultDomain_Type.__name__ = "OctetString"
_PIntDefaultDomain_Object = MibTableColumn
pIntDefaultDomain = _PIntDefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 10),
    _PIntDefaultDomain_Type()
)
pIntDefaultDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntDefaultDomain.setStatus("current")
_PIntHostName_Type = DisplayString
_PIntHostName_Object = MibTableColumn
pIntHostName = _PIntHostName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 11),
    _PIntHostName_Type()
)
pIntHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntHostName.setStatus("current")


class _PIntEnableMulticast_Type(Integer32):
    """Custom type pIntEnableMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PIntEnableMulticast_Type.__name__ = "Integer32"
_PIntEnableMulticast_Object = MibTableColumn
pIntEnableMulticast = _PIntEnableMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 12),
    _PIntEnableMulticast_Type()
)
pIntEnableMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntEnableMulticast.setStatus("current")
_PIntVlanId_Type = Integer32
_PIntVlanId_Object = MibTableColumn
pIntVlanId = _PIntVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 13),
    _PIntVlanId_Type()
)
pIntVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntVlanId.setStatus("current")
_PIntVlanInterface_Type = Integer32
_PIntVlanInterface_Object = MibTableColumn
pIntVlanInterface = _PIntVlanInterface_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 14),
    _PIntVlanInterface_Type()
)
pIntVlanInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntVlanInterface.setStatus("current")


class _PIntProxyArpStatus_Type(Integer32):
    """Custom type pIntProxyArpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PIntProxyArpStatus_Type.__name__ = "Integer32"
_PIntProxyArpStatus_Object = MibTableColumn
pIntProxyArpStatus = _PIntProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 15),
    _PIntProxyArpStatus_Type()
)
pIntProxyArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntProxyArpStatus.setStatus("current")
_PIntRowStatus_Type = RowStatus
_PIntRowStatus_Object = MibTableColumn
pIntRowStatus = _PIntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 8, 5, 1, 1, 16),
    _PIntRowStatus_Type()
)
pIntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pIntRowStatus.setStatus("current")
_Replication_ObjectIdentity = ObjectIdentity
replication = _Replication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9)
)


class _MachineRole_Type(Integer32):
    """Custom type machineRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_MachineRole_Type.__name__ = "Integer32"
_MachineRole_Object = MibScalar
machineRole = _MachineRole_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 1),
    _MachineRole_Type()
)
machineRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    machineRole.setStatus("current")


class _GenSnapshot_Type(Integer32):
    """Custom type genSnapshot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_GenSnapshot_Type.__name__ = "Integer32"
_GenSnapshot_Object = MibScalar
genSnapshot = _GenSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 2),
    _GenSnapshot_Type()
)
genSnapshot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSnapshot.setStatus("current")
_SlaveTable_Object = MibTable
slaveTable = _SlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 3)
)
if mibBuilder.loadTexts:
    slaveTable.setStatus("current")
_SlaveEntry_Object = MibTableRow
slaveEntry = _SlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 3, 1)
)
slaveEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "slaveId"),
)
if mibBuilder.loadTexts:
    slaveEntry.setStatus("current")


class _SlaveId_Type(Integer32):
    """Custom type slaveId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlaveId_Type.__name__ = "Integer32"
_SlaveId_Object = MibTableColumn
slaveId = _SlaveId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 3, 1, 1),
    _SlaveId_Type()
)
slaveId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slaveId.setStatus("current")


class _SlaveEnabled_Type(Integer32):
    """Custom type slaveEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SlaveEnabled_Type.__name__ = "Integer32"
_SlaveEnabled_Object = MibTableColumn
slaveEnabled = _SlaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 3, 1, 2),
    _SlaveEnabled_Type()
)
slaveEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaveEnabled.setStatus("current")


class _SlaveAddress_Type(OctetString):
    """Custom type slaveAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_SlaveAddress_Type.__name__ = "OctetString"
_SlaveAddress_Object = MibTableColumn
slaveAddress = _SlaveAddress_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 3, 1, 3),
    _SlaveAddress_Type()
)
slaveAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaveAddress.setStatus("current")
_SlaveNotes_Type = DisplayString
_SlaveNotes_Object = MibTableColumn
slaveNotes = _SlaveNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 3, 1, 4),
    _SlaveNotes_Type()
)
slaveNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaveNotes.setStatus("current")
_SlaveRowStatus_Type = RowStatus
_SlaveRowStatus_Object = MibTableColumn
slaveRowStatus = _SlaveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 3, 1, 5),
    _SlaveRowStatus_Type()
)
slaveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaveRowStatus.setStatus("current")


class _SlaveMobility_Type(Integer32):
    """Custom type slaveMobility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SlaveMobility_Type.__name__ = "Integer32"
_SlaveMobility_Object = MibTableColumn
slaveMobility = _SlaveMobility_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 9, 3, 1, 6),
    _SlaveMobility_Type()
)
slaveMobility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaveMobility.setStatus("current")
_Connection_ObjectIdentity = ObjectIdentity
connection = _Connection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10)
)
_ConnectionTable_Object = MibTable
connectionTable = _ConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1)
)
if mibBuilder.loadTexts:
    connectionTable.setStatus("current")
_ConnectionEntry_Object = MibTableRow
connectionEntry = _ConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1)
)
connectionEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "connectionId"),
)
if mibBuilder.loadTexts:
    connectionEntry.setStatus("current")


class _ConnectionId_Type(Integer32):
    """Custom type connectionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConnectionId_Type.__name__ = "Integer32"
_ConnectionId_Object = MibTableColumn
connectionId = _ConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 1),
    _ConnectionId_Type()
)
connectionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connectionId.setStatus("current")
_ConnectionName_Type = DisplayString
_ConnectionName_Object = MibTableColumn
connectionName = _ConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 2),
    _ConnectionName_Type()
)
connectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionName.setStatus("current")
_ConnectionIp_Type = BlueIpAddress
_ConnectionIp_Object = MibTableColumn
connectionIp = _ConnectionIp_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 3),
    _ConnectionIp_Type()
)
connectionIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionIp.setStatus("current")


class _ConnectionMac_Type(OctetString):
    """Custom type connectionMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_ConnectionMac_Type.__name__ = "OctetString"
_ConnectionMac_Object = MibTableColumn
connectionMac = _ConnectionMac_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 4),
    _ConnectionMac_Type()
)
connectionMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionMac.setStatus("current")
_ConnectionRoleId_Type = Integer32
_ConnectionRoleId_Object = MibTableColumn
connectionRoleId = _ConnectionRoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 5),
    _ConnectionRoleId_Type()
)
connectionRoleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionRoleId.setStatus("current")
_ConnectionUserId_Type = Integer32
_ConnectionUserId_Object = MibTableColumn
connectionUserId = _ConnectionUserId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 6),
    _ConnectionUserId_Type()
)
connectionUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionUserId.setStatus("current")
_ConnectionLoginTime_Type = DateAndTime
_ConnectionLoginTime_Object = MibTableColumn
connectionLoginTime = _ConnectionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 7),
    _ConnectionLoginTime_Type()
)
connectionLoginTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionLoginTime.setStatus("current")
_ConnectionChecked_Type = TimeTicks
_ConnectionChecked_Object = MibTableColumn
connectionChecked = _ConnectionChecked_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 8),
    _ConnectionChecked_Type()
)
connectionChecked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionChecked.setStatus("current")
_ConnectionBytes_Type = Integer32
_ConnectionBytes_Object = MibTableColumn
connectionBytes = _ConnectionBytes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 9),
    _ConnectionBytes_Type()
)
connectionBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionBytes.setStatus("current")
_ConnectionCurRate_Type = Integer32
_ConnectionCurRate_Object = MibTableColumn
connectionCurRate = _ConnectionCurRate_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 10),
    _ConnectionCurRate_Type()
)
connectionCurRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionCurRate.setStatus("current")
_ConnectionExpiry_Type = Integer32
_ConnectionExpiry_Object = MibTableColumn
connectionExpiry = _ConnectionExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 11),
    _ConnectionExpiry_Type()
)
connectionExpiry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionExpiry.setStatus("current")


class _ConnectionDev_Type(OctetString):
    """Custom type connectionDev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_ConnectionDev_Type.__name__ = "OctetString"
_ConnectionDev_Object = MibTableColumn
connectionDev = _ConnectionDev_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 12),
    _ConnectionDev_Type()
)
connectionDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionDev.setStatus("current")
_ConnectionHost_Type = DisplayString
_ConnectionHost_Object = MibTableColumn
connectionHost = _ConnectionHost_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 13),
    _ConnectionHost_Type()
)
connectionHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionHost.setStatus("current")
_ConnectionUnReg_Type = Integer32
_ConnectionUnReg_Object = MibTableColumn
connectionUnReg = _ConnectionUnReg_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 14),
    _ConnectionUnReg_Type()
)
connectionUnReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionUnReg.setStatus("current")


class _ConnectionAP_Type(OctetString):
    """Custom type connectionAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ConnectionAP_Type.__name__ = "OctetString"
_ConnectionAP_Object = MibTableColumn
connectionAP = _ConnectionAP_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 15),
    _ConnectionAP_Type()
)
connectionAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionAP.setStatus("current")
_ConnectionLoginAttempt_Type = Integer32
_ConnectionLoginAttempt_Object = MibTableColumn
connectionLoginAttempt = _ConnectionLoginAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 16),
    _ConnectionLoginAttempt_Type()
)
connectionLoginAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionLoginAttempt.setStatus("current")
_ConnectionLoginAttemptCnt_Type = Integer32
_ConnectionLoginAttemptCnt_Object = MibTableColumn
connectionLoginAttemptCnt = _ConnectionLoginAttemptCnt_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 17),
    _ConnectionLoginAttemptCnt_Type()
)
connectionLoginAttemptCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionLoginAttemptCnt.setStatus("current")


class _ConnectionRoamMac_Type(OctetString):
    """Custom type connectionRoamMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_ConnectionRoamMac_Type.__name__ = "OctetString"
_ConnectionRoamMac_Object = MibTableColumn
connectionRoamMac = _ConnectionRoamMac_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 10, 1, 1, 18),
    _ConnectionRoamMac_Type()
)
connectionRoamMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionRoamMac.setStatus("current")
_Roles_ObjectIdentity = ObjectIdentity
roles = _Roles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11)
)
_RoleTable_Object = MibTable
roleTable = _RoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1)
)
if mibBuilder.loadTexts:
    roleTable.setStatus("current")
_RoleEntry_Object = MibTableRow
roleEntry = _RoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1)
)
roleEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "roleId"),
)
if mibBuilder.loadTexts:
    roleEntry.setStatus("current")


class _RoleId_Type(Integer32):
    """Custom type roleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RoleId_Type.__name__ = "Integer32"
_RoleId_Object = MibTableColumn
roleId = _RoleId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 1),
    _RoleId_Type()
)
roleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    roleId.setStatus("current")


class _RoleName_Type(OctetString):
    """Custom type roleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_RoleName_Type.__name__ = "OctetString"
_RoleName_Object = MibTableColumn
roleName = _RoleName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 2),
    _RoleName_Type()
)
roleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleName.setStatus("current")


class _RoleType_Type(OctetString):
    """Custom type roleType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_RoleType_Type.__name__ = "OctetString"
_RoleType_Object = MibTableColumn
roleType = _RoleType_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 3),
    _RoleType_Type()
)
roleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleType.setStatus("current")


class _RoleQosRate_Type(OctetString):
    """Custom type roleQosRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_RoleQosRate_Type.__name__ = "OctetString"
_RoleQosRate_Object = MibTableColumn
roleQosRate = _RoleQosRate_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 4),
    _RoleQosRate_Type()
)
roleQosRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosRate.setStatus("current")
_RoleQosQnt_Type = Integer32
_RoleQosQnt_Object = MibTableColumn
roleQosQnt = _RoleQosQnt_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 5),
    _RoleQosQnt_Type()
)
roleQosQnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosQnt.setStatus("current")


class _RoleVpn_Type(Integer32):
    """Custom type roleVpn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modarate", 3),
          ("none", 1),
          ("pptp", 2))
    )


_RoleVpn_Type.__name__ = "Integer32"
_RoleVpn_Object = MibTableColumn
roleVpn = _RoleVpn_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 6),
    _RoleVpn_Type()
)
roleVpn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleVpn.setStatus("current")
_RoleInherit_Type = Integer32
_RoleInherit_Object = MibTableColumn
roleInherit = _RoleInherit_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 7),
    _RoleInherit_Type()
)
roleInherit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleInherit.setStatus("current")
_RoleUnGuestLogin_Type = Integer32
_RoleUnGuestLogin_Object = MibTableColumn
roleUnGuestLogin = _RoleUnGuestLogin_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 8),
    _RoleUnGuestLogin_Type()
)
roleUnGuestLogin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleUnGuestLogin.setStatus("current")
_RoleUnUserLogin_Type = Integer32
_RoleUnUserLogin_Object = MibTableColumn
roleUnUserLogin = _RoleUnUserLogin_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 9),
    _RoleUnUserLogin_Type()
)
roleUnUserLogin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleUnUserLogin.setStatus("current")
_RoleNotes_Type = DisplayString
_RoleNotes_Object = MibTableColumn
roleNotes = _RoleNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 10),
    _RoleNotes_Type()
)
roleNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleNotes.setStatus("current")
_RoleQosUserIn_Type = Integer32
_RoleQosUserIn_Object = MibTableColumn
roleQosUserIn = _RoleQosUserIn_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 12),
    _RoleQosUserIn_Type()
)
roleQosUserIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosUserIn.setStatus("current")
_RoleQosUserOut_Type = Integer32
_RoleQosUserOut_Object = MibTableColumn
roleQosUserOut = _RoleQosUserOut_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 13),
    _RoleQosUserOut_Type()
)
roleQosUserOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosUserOut.setStatus("current")
_RoleQosPriorityIn_Type = Integer32
_RoleQosPriorityIn_Object = MibTableColumn
roleQosPriorityIn = _RoleQosPriorityIn_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 14),
    _RoleQosPriorityIn_Type()
)
roleQosPriorityIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosPriorityIn.setStatus("current")
_RoleQosPriorityOut_Type = Integer32
_RoleQosPriorityOut_Object = MibTableColumn
roleQosPriorityOut = _RoleQosPriorityOut_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 15),
    _RoleQosPriorityOut_Type()
)
roleQosPriorityOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosPriorityOut.setStatus("current")


class _RoleQosPriInOverride_Type(OctetString):
    """Custom type roleQosPriInOverride based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RoleQosPriInOverride_Type.__name__ = "OctetString"
_RoleQosPriInOverride_Object = MibTableColumn
roleQosPriInOverride = _RoleQosPriInOverride_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 16),
    _RoleQosPriInOverride_Type()
)
roleQosPriInOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosPriInOverride.setStatus("current")


class _RoleQosPriOutOverride_Type(OctetString):
    """Custom type roleQosPriOutOverride based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RoleQosPriOutOverride_Type.__name__ = "OctetString"
_RoleQosPriOutOverride_Object = MibTableColumn
roleQosPriOutOverride = _RoleQosPriOutOverride_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 17),
    _RoleQosPriOutOverride_Type()
)
roleQosPriOutOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosPriOutOverride.setStatus("current")
_RoleQosDscpIn_Type = Integer32
_RoleQosDscpIn_Object = MibTableColumn
roleQosDscpIn = _RoleQosDscpIn_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 18),
    _RoleQosDscpIn_Type()
)
roleQosDscpIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosDscpIn.setStatus("current")
_RoleQosDscpOut_Type = Integer32
_RoleQosDscpOut_Object = MibTableColumn
roleQosDscpOut = _RoleQosDscpOut_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 19),
    _RoleQosDscpOut_Type()
)
roleQosDscpOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosDscpOut.setStatus("current")


class _RoleQosDscpInOverride_Type(OctetString):
    """Custom type roleQosDscpInOverride based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RoleQosDscpInOverride_Type.__name__ = "OctetString"
_RoleQosDscpInOverride_Object = MibTableColumn
roleQosDscpInOverride = _RoleQosDscpInOverride_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 20),
    _RoleQosDscpInOverride_Type()
)
roleQosDscpInOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosDscpInOverride.setStatus("current")


class _RoleQosDscpOutOverride_Type(OctetString):
    """Custom type roleQosDscpOutOverride based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RoleQosDscpOutOverride_Type.__name__ = "OctetString"
_RoleQosDscpOutOverride_Object = MibTableColumn
roleQosDscpOutOverride = _RoleQosDscpOutOverride_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 21),
    _RoleQosDscpOutOverride_Type()
)
roleQosDscpOutOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosDscpOutOverride.setStatus("current")
_RoleQosRateOut_Type = Integer32
_RoleQosRateOut_Object = MibTableColumn
roleQosRateOut = _RoleQosRateOut_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 22),
    _RoleQosRateOut_Type()
)
roleQosRateOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosRateOut.setStatus("current")


class _RoleQosRateQntOut_Type(OctetString):
    """Custom type roleQosRateQntOut based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_RoleQosRateQntOut_Type.__name__ = "OctetString"
_RoleQosRateQntOut_Object = MibTableColumn
roleQosRateQntOut = _RoleQosRateQntOut_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 23),
    _RoleQosRateQntOut_Type()
)
roleQosRateQntOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleQosRateQntOut.setStatus("current")
_RoleVlanId_Type = Integer32
_RoleVlanId_Object = MibTableColumn
roleVlanId = _RoleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 24),
    _RoleVlanId_Type()
)
roleVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleVlanId.setStatus("current")


class _RoleRedirect_Type(OctetString):
    """Custom type roleRedirect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_RoleRedirect_Type.__name__ = "OctetString"
_RoleRedirect_Object = MibTableColumn
roleRedirect = _RoleRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 25),
    _RoleRedirect_Type()
)
roleRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleRedirect.setStatus("current")
_RoleRowStatus_Type = RowStatus
_RoleRowStatus_Object = MibTableColumn
roleRowStatus = _RoleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 11, 1, 1, 26),
    _RoleRowStatus_Type()
)
roleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    roleRowStatus.setStatus("current")
_ServiceMgmt_ObjectIdentity = ObjectIdentity
serviceMgmt = _ServiceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 12)
)
_ServiceMgmtTable_Object = MibTable
serviceMgmtTable = _ServiceMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 12, 1)
)
if mibBuilder.loadTexts:
    serviceMgmtTable.setStatus("current")
_ServiceMgmtEntry_Object = MibTableRow
serviceMgmtEntry = _ServiceMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 12, 1, 1)
)
serviceMgmtEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "serviceMgmtId"),
)
if mibBuilder.loadTexts:
    serviceMgmtEntry.setStatus("current")


class _ServiceMgmtId_Type(Integer32):
    """Custom type serviceMgmtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ServiceMgmtId_Type.__name__ = "Integer32"
_ServiceMgmtId_Object = MibTableColumn
serviceMgmtId = _ServiceMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 12, 1, 1, 1),
    _ServiceMgmtId_Type()
)
serviceMgmtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceMgmtId.setStatus("current")
_ServiceMgmtName_Type = DisplayString
_ServiceMgmtName_Object = MibTableColumn
serviceMgmtName = _ServiceMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 12, 1, 1, 2),
    _ServiceMgmtName_Type()
)
serviceMgmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceMgmtName.setStatus("current")


class _ServiceMgmtOptStatus_Type(Integer32):
    """Custom type serviceMgmtOptStatus based on Integer32"""
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
        *(("noopt", 4),
          ("restart", 3),
          ("start", 1),
          ("stop", 2))
    )


_ServiceMgmtOptStatus_Type.__name__ = "Integer32"
_ServiceMgmtOptStatus_Object = MibTableColumn
serviceMgmtOptStatus = _ServiceMgmtOptStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 12, 1, 1, 3),
    _ServiceMgmtOptStatus_Type()
)
serviceMgmtOptStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceMgmtOptStatus.setStatus("current")
_ServiceMgmtDesr_Type = DisplayString
_ServiceMgmtDesr_Object = MibTableColumn
serviceMgmtDesr = _ServiceMgmtDesr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 12, 1, 1, 4),
    _ServiceMgmtDesr_Type()
)
serviceMgmtDesr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceMgmtDesr.setStatus("current")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13)
)
_UserSummary_ObjectIdentity = ObjectIdentity
userSummary = _UserSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 1)
)
_UserSumNoOfUsr_Type = Integer32
_UserSumNoOfUsr_Object = MibScalar
userSumNoOfUsr = _UserSumNoOfUsr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 1, 1),
    _UserSumNoOfUsr_Type()
)
userSumNoOfUsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSumNoOfUsr.setStatus("current")
_UserSumNoOfLogdInUsr_Type = Integer32
_UserSumNoOfLogdInUsr_Object = MibScalar
userSumNoOfLogdInUsr = _UserSumNoOfLogdInUsr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 1, 2),
    _UserSumNoOfLogdInUsr_Type()
)
userSumNoOfLogdInUsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSumNoOfLogdInUsr.setStatus("current")
_UserSumNoOfLogdVPNUsr_Type = Integer32
_UserSumNoOfLogdVPNUsr_Object = MibScalar
userSumNoOfLogdVPNUsr = _UserSumNoOfLogdVPNUsr_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 1, 3),
    _UserSumNoOfLogdVPNUsr_Type()
)
userSumNoOfLogdVPNUsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSumNoOfLogdVPNUsr.setStatus("current")
_UsmSumTtlBandWthInUse_Type = Integer32
_UsmSumTtlBandWthInUse_Object = MibScalar
usmSumTtlBandWthInUse = _UsmSumTtlBandWthInUse_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 1, 4),
    _UsmSumTtlBandWthInUse_Type()
)
usmSumTtlBandWthInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmSumTtlBandWthInUse.setStatus("current")
_SystemStats_ObjectIdentity = ObjectIdentity
systemStats = _SystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 2)
)
_SysStatCpuUtil_Type = Integer32
_SysStatCpuUtil_Object = MibScalar
sysStatCpuUtil = _SysStatCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 2, 1),
    _SysStatCpuUtil_Type()
)
sysStatCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatCpuUtil.setStatus("current")
_SysStatMemUtil_Type = Integer32
_SysStatMemUtil_Object = MibScalar
sysStatMemUtil = _SysStatMemUtil_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 2, 2),
    _SysStatMemUtil_Type()
)
sysStatMemUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatMemUtil.setStatus("current")
_SysStatTotalDiskSpace_Type = Integer32
_SysStatTotalDiskSpace_Object = MibScalar
sysStatTotalDiskSpace = _SysStatTotalDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 2, 3),
    _SysStatTotalDiskSpace_Type()
)
sysStatTotalDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatTotalDiskSpace.setStatus("current")
_SysStatDiskSpaceUsed_Type = Integer32
_SysStatDiskSpaceUsed_Object = MibScalar
sysStatDiskSpaceUsed = _SysStatDiskSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 2, 4),
    _SysStatDiskSpaceUsed_Type()
)
sysStatDiskSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatDiskSpaceUsed.setStatus("current")
_SysStatDiskSpaceFree_Type = Integer32
_SysStatDiskSpaceFree_Object = MibScalar
sysStatDiskSpaceFree = _SysStatDiskSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 2, 5),
    _SysStatDiskSpaceFree_Type()
)
sysStatDiskSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatDiskSpaceFree.setStatus("current")
_SysStatLOgSpaceUsed_Type = Integer32
_SysStatLOgSpaceUsed_Object = MibScalar
sysStatLOgSpaceUsed = _SysStatLOgSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 2, 6),
    _SysStatLOgSpaceUsed_Type()
)
sysStatLOgSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatLOgSpaceUsed.setStatus("current")


class _SysStatNeedRestart_Type(Integer32):
    """Custom type sysStatNeedRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SysStatNeedRestart_Type.__name__ = "Integer32"
_SysStatNeedRestart_Object = MibScalar
sysStatNeedRestart = _SysStatNeedRestart_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 13, 2, 7),
    _SysStatNeedRestart_Type()
)
sysStatNeedRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatNeedRestart.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "vlanRowId"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")


class _VlanRowId_Type(Integer32):
    """Custom type vlanRowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VlanRowId_Type.__name__ = "Integer32"
_VlanRowId_Object = MibTableColumn
vlanRowId = _VlanRowId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 1, 1, 1),
    _VlanRowId_Type()
)
vlanRowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanRowId.setStatus("current")


class _VlanName_Type(OctetString):
    """Custom type vlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_VlanName_Type.__name__ = "OctetString"
_VlanName_Object = MibTableColumn
vlanName = _VlanName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 1, 1, 2),
    _VlanName_Type()
)
vlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanName.setStatus("current")
_VlanId_Type = Integer32
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 1, 1, 3),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_VlanNotes_Type = DisplayString
_VlanNotes_Object = MibTableColumn
vlanNotes = _VlanNotes_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 1, 1, 4),
    _VlanNotes_Type()
)
vlanNotes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNotes.setStatus("current")
_VlanRowStatus_Type = RowStatus
_VlanRowStatus_Object = MibTableColumn
vlanRowStatus = _VlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 1, 1, 5),
    _VlanRowStatus_Type()
)
vlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanRowStatus.setStatus("current")
_VlanGrpTable_Object = MibTable
vlanGrpTable = _VlanGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 2)
)
if mibBuilder.loadTexts:
    vlanGrpTable.setStatus("current")
_VlanGrpEntry_Object = MibTableRow
vlanGrpEntry = _VlanGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 2, 1)
)
vlanGrpEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "vlanGrpId"),
)
if mibBuilder.loadTexts:
    vlanGrpEntry.setStatus("current")


class _VlanGrpId_Type(Integer32):
    """Custom type vlanGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VlanGrpId_Type.__name__ = "Integer32"
_VlanGrpId_Object = MibTableColumn
vlanGrpId = _VlanGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 2, 1, 1),
    _VlanGrpId_Type()
)
vlanGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanGrpId.setStatus("current")


class _VlanGrpName_Type(OctetString):
    """Custom type vlanGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_VlanGrpName_Type.__name__ = "OctetString"
_VlanGrpName_Object = MibTableColumn
vlanGrpName = _VlanGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 2, 1, 2),
    _VlanGrpName_Type()
)
vlanGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanGrpName.setStatus("current")
_VlanGrpRowStatus_Type = RowStatus
_VlanGrpRowStatus_Object = MibTableColumn
vlanGrpRowStatus = _VlanGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 2, 1, 3),
    _VlanGrpRowStatus_Type()
)
vlanGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanGrpRowStatus.setStatus("current")
_VlanGrpMemTable_Object = MibTable
vlanGrpMemTable = _VlanGrpMemTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 3)
)
if mibBuilder.loadTexts:
    vlanGrpMemTable.setStatus("current")
_VlanGrpMemEntry_Object = MibTableRow
vlanGrpMemEntry = _VlanGrpMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 3, 1)
)
vlanGrpMemEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "vlanGrpId"),
    (0, "BLUESERVER-MIB", "vlanGrpMemId"),
)
if mibBuilder.loadTexts:
    vlanGrpMemEntry.setStatus("current")


class _VlanGrpMemId_Type(Integer32):
    """Custom type vlanGrpMemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VlanGrpMemId_Type.__name__ = "Integer32"
_VlanGrpMemId_Object = MibTableColumn
vlanGrpMemId = _VlanGrpMemId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 3, 1, 1),
    _VlanGrpMemId_Type()
)
vlanGrpMemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanGrpMemId.setStatus("current")
_VlanGrpMemRowStatus_Type = RowStatus
_VlanGrpMemRowStatus_Object = MibTableColumn
vlanGrpMemRowStatus = _VlanGrpMemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 14, 3, 1, 2),
    _VlanGrpMemRowStatus_Type()
)
vlanGrpMemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanGrpMemRowStatus.setStatus("current")
_Schedule_ObjectIdentity = ObjectIdentity
schedule = _Schedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15)
)
_SchedTable_Object = MibTable
schedTable = _SchedTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1)
)
if mibBuilder.loadTexts:
    schedTable.setStatus("current")
_SchedEntry_Object = MibTableRow
schedEntry = _SchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1)
)
schedEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "schedRowId"),
)
if mibBuilder.loadTexts:
    schedEntry.setStatus("current")


class _SchedRowId_Type(Integer32):
    """Custom type schedRowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SchedRowId_Type.__name__ = "Integer32"
_SchedRowId_Object = MibTableColumn
schedRowId = _SchedRowId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 1),
    _SchedRowId_Type()
)
schedRowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schedRowId.setStatus("current")


class _SchedName_Type(OctetString):
    """Custom type schedName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_SchedName_Type.__name__ = "OctetString"
_SchedName_Object = MibTableColumn
schedName = _SchedName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 2),
    _SchedName_Type()
)
schedName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedName.setStatus("current")


class _SchedAllDay_Type(Integer32):
    """Custom type schedAllDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SchedAllDay_Type.__name__ = "Integer32"
_SchedAllDay_Object = MibTableColumn
schedAllDay = _SchedAllDay_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 3),
    _SchedAllDay_Type()
)
schedAllDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedAllDay.setStatus("current")


class _SchedEveryDay_Type(Integer32):
    """Custom type schedEveryDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SchedEveryDay_Type.__name__ = "Integer32"
_SchedEveryDay_Object = MibTableColumn
schedEveryDay = _SchedEveryDay_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 4),
    _SchedEveryDay_Type()
)
schedEveryDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedEveryDay.setStatus("current")
_SchedStartDateAndTime_Type = LocalDateAndTime
_SchedStartDateAndTime_Object = MibTableColumn
schedStartDateAndTime = _SchedStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 5),
    _SchedStartDateAndTime_Type()
)
schedStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedStartDateAndTime.setStatus("current")
_SchedEndDateAndTime_Type = LocalDateAndTime
_SchedEndDateAndTime_Object = MibTableColumn
schedEndDateAndTime = _SchedEndDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 6),
    _SchedEndDateAndTime_Type()
)
schedEndDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedEndDateAndTime.setStatus("current")


class _SchedMonth_Type(Integer32):
    """Custom type schedMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_SchedMonth_Type.__name__ = "Integer32"
_SchedMonth_Object = MibTableColumn
schedMonth = _SchedMonth_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 7),
    _SchedMonth_Type()
)
schedMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedMonth.setStatus("current")


class _SchedWeekDay_Type(Integer32):
    """Custom type schedWeekDay based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_SchedWeekDay_Type.__name__ = "Integer32"
_SchedWeekDay_Object = MibTableColumn
schedWeekDay = _SchedWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 8),
    _SchedWeekDay_Type()
)
schedWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedWeekDay.setStatus("current")
_SchedDayOfMonth_Type = Integer32
_SchedDayOfMonth_Object = MibTableColumn
schedDayOfMonth = _SchedDayOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 9),
    _SchedDayOfMonth_Type()
)
schedDayOfMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedDayOfMonth.setStatus("current")
_SchedRowStatus_Type = RowStatus
_SchedRowStatus_Object = MibTableColumn
schedRowStatus = _SchedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 1, 1, 10),
    _SchedRowStatus_Type()
)
schedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedRowStatus.setStatus("current")
_SchedGrpTable_Object = MibTable
schedGrpTable = _SchedGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 2)
)
if mibBuilder.loadTexts:
    schedGrpTable.setStatus("current")
_SchedGrpEntry_Object = MibTableRow
schedGrpEntry = _SchedGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 2, 1)
)
schedGrpEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "schedGrpId"),
)
if mibBuilder.loadTexts:
    schedGrpEntry.setStatus("current")


class _SchedGrpId_Type(Integer32):
    """Custom type schedGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SchedGrpId_Type.__name__ = "Integer32"
_SchedGrpId_Object = MibTableColumn
schedGrpId = _SchedGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 2, 1, 1),
    _SchedGrpId_Type()
)
schedGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schedGrpId.setStatus("current")


class _SchedGrpName_Type(OctetString):
    """Custom type schedGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_SchedGrpName_Type.__name__ = "OctetString"
_SchedGrpName_Object = MibTableColumn
schedGrpName = _SchedGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 2, 1, 2),
    _SchedGrpName_Type()
)
schedGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedGrpName.setStatus("current")
_SchedGrpRowStatus_Type = RowStatus
_SchedGrpRowStatus_Object = MibTableColumn
schedGrpRowStatus = _SchedGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 2, 1, 3),
    _SchedGrpRowStatus_Type()
)
schedGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedGrpRowStatus.setStatus("current")
_SchedGrpMemTable_Object = MibTable
schedGrpMemTable = _SchedGrpMemTable_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 3)
)
if mibBuilder.loadTexts:
    schedGrpMemTable.setStatus("current")
_SchedGrpMemEntry_Object = MibTableRow
schedGrpMemEntry = _SchedGrpMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 3, 1)
)
schedGrpMemEntry.setIndexNames(
    (0, "BLUESERVER-MIB", "schedGrpId"),
    (0, "BLUESERVER-MIB", "schedGrpMemId"),
)
if mibBuilder.loadTexts:
    schedGrpMemEntry.setStatus("current")


class _SchedGrpMemId_Type(Integer32):
    """Custom type schedGrpMemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SchedGrpMemId_Type.__name__ = "Integer32"
_SchedGrpMemId_Object = MibTableColumn
schedGrpMemId = _SchedGrpMemId_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 3, 1, 1),
    _SchedGrpMemId_Type()
)
schedGrpMemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schedGrpMemId.setStatus("current")
_SchedGrpMemRowStatus_Type = RowStatus
_SchedGrpMemRowStatus_Object = MibTableColumn
schedGrpMemRowStatus = _SchedGrpMemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9967, 1, 15, 3, 1, 2),
    _SchedGrpMemRowStatus_Type()
)
schedGrpMemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedGrpMemRowStatus.setStatus("current")
_BlueNotification_ObjectIdentity = ObjectIdentity
blueNotification = _BlueNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2)
)
_NotifyObjects_ObjectIdentity = ObjectIdentity
notifyObjects = _NotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1)
)


class _NtyobjLevel_Type(OctetString):
    """Custom type ntyobjLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_NtyobjLevel_Type.__name__ = "OctetString"
_NtyobjLevel_Object = MibScalar
ntyobjLevel = _NtyobjLevel_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 1),
    _NtyobjLevel_Type()
)
ntyobjLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjLevel.setStatus("current")


class _NtyobjName_Type(OctetString):
    """Custom type ntyobjName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NtyobjName_Type.__name__ = "OctetString"
_NtyobjName_Object = MibScalar
ntyobjName = _NtyobjName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 2),
    _NtyobjName_Type()
)
ntyobjName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjName.setStatus("current")


class _NtyobjDesc_Type(OctetString):
    """Custom type ntyobjDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_NtyobjDesc_Type.__name__ = "OctetString"
_NtyobjDesc_Object = MibScalar
ntyobjDesc = _NtyobjDesc_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 3),
    _NtyobjDesc_Type()
)
ntyobjDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjDesc.setStatus("current")
_NtyobjOID_Type = ObjectIdentifier
_NtyobjOID_Object = MibScalar
ntyobjOID = _NtyobjOID_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 4),
    _NtyobjOID_Type()
)
ntyobjOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjOID.setStatus("current")


class _NtyobjValue_Type(OctetString):
    """Custom type ntyobjValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtyobjValue_Type.__name__ = "OctetString"
_NtyobjValue_Object = MibScalar
ntyobjValue = _NtyobjValue_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 5),
    _NtyobjValue_Type()
)
ntyobjValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjValue.setStatus("current")
_BlueTraps_ObjectIdentity = ObjectIdentity
blueTraps = _BlueTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2)
)
_BlueConfigTraps_ObjectIdentity = ObjectIdentity
blueConfigTraps = _BlueConfigTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1)
)
_BlueConfigTraps0_ObjectIdentity = ObjectIdentity
blueConfigTraps0 = _BlueConfigTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0)
)
_BlueFailureTraps_ObjectIdentity = ObjectIdentity
blueFailureTraps = _BlueFailureTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2)
)
_BlueFailureTraps0_ObjectIdentity = ObjectIdentity
blueFailureTraps0 = _BlueFailureTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0)
)
_BlueThresholdTraps_ObjectIdentity = ObjectIdentity
blueThresholdTraps = _BlueThresholdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3)
)
_BlueThresholdTraps0_ObjectIdentity = ObjectIdentity
blueThresholdTraps0 = _BlueThresholdTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0)
)
_BlueGeneralTraps_ObjectIdentity = ObjectIdentity
blueGeneralTraps = _BlueGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4)
)
_BlueGeneralTraps0_ObjectIdentity = ObjectIdentity
blueGeneralTraps0 = _BlueGeneralTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4, 0)
)

# Managed Objects groups


# Notification objects

cctSystemConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 1)
)
cctSystemConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctSystemConfChange.setStatus(
        "current"
    )

cctUserConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 2)
)
cctUserConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctUserConfChange.setStatus(
        "current"
    )

cctExternalServConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 3)
)
cctExternalServConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctExternalServConfChange.setStatus(
        "current"
    )

cctRoleConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 4)
)
cctRoleConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctRoleConfChange.setStatus(
        "current"
    )

cctDestinationConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 5)
)
cctDestinationConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctDestinationConfChange.setStatus(
        "current"
    )

cctServiceConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 6)
)
cctServiceConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctServiceConfChange.setStatus(
        "current"
    )

cctNetworkConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 7)
)
cctNetworkConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctNetworkConfChange.setStatus(
        "current"
    )

cctVpnConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 8)
)
cctVpnConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctVpnConfChange.setStatus(
        "current"
    )

cctMobilityConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 9)
)
cctMobilityConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctMobilityConfChange.setStatus(
        "current"
    )

cctProcessConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 10)
)
cctProcessConfChange.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctProcessConfChange.setStatus(
        "current"
    )

btSysGeneralFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 1)
)
btSysGeneralFailure.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btSysGeneralFailure.setStatus(
        "current"
    )

btUserLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 2)
)
btUserLoginFailure.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btUserLoginFailure.setStatus(
        "current"
    )

btProcessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 3)
)
btProcessFailure.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btProcessFailure.setStatus(
        "current"
    )

btAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 4)
)
btAuthFailure.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btAuthFailure.setStatus(
        "current"
    )

btSystemFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 5)
)
btSystemFailover.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btSystemFailover.setStatus(
        "current"
    )

btConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0, 1)
)
btConditionalEvent.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjOID"),
        ("BLUESERVER-MIB", "ntyobjValue"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btConditionalEvent.setStatus(
        "current"
    )

btCpuLoadEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0, 2)
)
btCpuLoadEvent.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjOID"),
        ("BLUESERVER-MIB", "ntyobjValue"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btCpuLoadEvent.setStatus(
        "current"
    )

btMemSwapUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0, 3)
)
btMemSwapUsageEvent.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjOID"),
        ("BLUESERVER-MIB", "ntyobjValue"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btMemSwapUsageEvent.setStatus(
        "current"
    )

btDiskUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0, 4)
)
btDiskUsageEvent.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjOID"),
        ("BLUESERVER-MIB", "ntyobjValue"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btDiskUsageEvent.setStatus(
        "current"
    )

btLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4, 0, 1)
)
btLinkUp.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btLinkUp.setStatus(
        "current"
    )

btLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4, 0, 2)
)
btLinkDown.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btLinkDown.setStatus(
        "current"
    )

btSystemGeneralTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4, 0, 3)
)
btSystemGeneralTrap.setObjects(
      *(("BLUESERVER-MIB", "ntyobjLevel"),
        ("BLUESERVER-MIB", "ntyobjName"),
        ("BLUESERVER-MIB", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btSystemGeneralTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUESERVER-MIB",
    **{"BlueIpAddress": BlueIpAddress,
       "BlueMacAddress": BlueMacAddress,
       "LocalDateAndTime": LocalDateAndTime,
       "blueSocket": blueSocket,
       "blueServer": blueServer,
       "users": users,
       "nativeUsers": nativeUsers,
       "nativeUserTable": nativeUserTable,
       "nativeUserEntry": nativeUserEntry,
       "nativeUserId": nativeUserId,
       "nativeUserAccess": nativeUserAccess,
       "nativeUserName": nativeUserName,
       "nativeUserRoleId": nativeUserRoleId,
       "nativeUserEmailId": nativeUserEmailId,
       "nativeUserFixedIpAddr": nativeUserFixedIpAddr,
       "nativeUserPassword": nativeUserPassword,
       "nativeUserNotes": nativeUserNotes,
       "nativeUserRowStatus": nativeUserRowStatus,
       "nativeUserRadAcctServId": nativeUserRadAcctServId,
       "adminUsers": adminUsers,
       "adminUserTable": adminUserTable,
       "adminUserEntry": adminUserEntry,
       "adminUserId": adminUserId,
       "adminUserStatus": adminUserStatus,
       "adminUserName": adminUserName,
       "adminUserAccess": adminUserAccess,
       "adminUserEmailId": adminUserEmailId,
       "adminUserPassword": adminUserPassword,
       "adminUserNotes": adminUserNotes,
       "adminUserRowStatus": adminUserRowStatus,
       "adUsrAccessTable": adUsrAccessTable,
       "adUsrAccessEntry": adUsrAccessEntry,
       "adUsrAccessAdminUser": adUsrAccessAdminUser,
       "adUsrAccessNativeUser": adUsrAccessNativeUser,
       "adUsrAccessExServer": adUsrAccessExServer,
       "adUsrAccessAccounting": adUsrAccessAccounting,
       "adUsrAccessRoles": adUsrAccessRoles,
       "adUsrAccessDestination": adUsrAccessDestination,
       "adUsrAccessServices": adUsrAccessServices,
       "adUsrAccessVpn": adUsrAccessVpn,
       "adUsrAccessConfiguration": adUsrAccessConfiguration,
       "adUsrAccessNetwork": adUsrAccessNetwork,
       "adUsrAccessReplication": adUsrAccessReplication,
       "adUsrAccessMaintance": adUsrAccessMaintance,
       "adUsrAccessStatus": adUsrAccessStatus,
       "adUsrAccessVlans": adUsrAccessVlans,
       "adUsrAccessSchedules": adUsrAccessSchedules,
       "adUsrAccessMacDev": adUsrAccessMacDev,
       "destination": destination,
       "hostTable": hostTable,
       "hostEntry": hostEntry,
       "hostId": hostId,
       "hostName": hostName,
       "hostAddress": hostAddress,
       "hostNetmask": hostNetmask,
       "hostInvertDest": hostInvertDest,
       "hostType": hostType,
       "hostNotes": hostNotes,
       "hostRowStatus": hostRowStatus,
       "hostGrpTable": hostGrpTable,
       "hostGrpEntry": hostGrpEntry,
       "hostGrpId": hostGrpId,
       "hostGrpName": hostGrpName,
       "hostGrpRowStatus": hostGrpRowStatus,
       "hostGrpMemTable": hostGrpMemTable,
       "hostGrpMemEntry": hostGrpMemEntry,
       "hostGrpMemId": hostGrpMemId,
       "hostGrpMemRowStatus": hostGrpMemRowStatus,
       "service": service,
       "serviceTable": serviceTable,
       "serviceEntry": serviceEntry,
       "serviceId": serviceId,
       "serviceName": serviceName,
       "servicePort": servicePort,
       "serviceProtocol": serviceProtocol,
       "serviceCosPriorityIn": serviceCosPriorityIn,
       "serviceCosPriorityOut": serviceCosPriorityOut,
       "serviceCosDscpIn": serviceCosDscpIn,
       "serviceCosDscpOut": serviceCosDscpOut,
       "serviceNotes": serviceNotes,
       "serviceRowStatus": serviceRowStatus,
       "serviceGrpTable": serviceGrpTable,
       "serviceGrpEntry": serviceGrpEntry,
       "serviceGrpId": serviceGrpId,
       "serviceGrpName": serviceGrpName,
       "serviceGrpRowStatus": serviceGrpRowStatus,
       "serviceGrpMemTable": serviceGrpMemTable,
       "serviceGrpMemEntry": serviceGrpMemEntry,
       "serviceGrpMemId": serviceGrpMemId,
       "serviceGrpMemRowStatus": serviceGrpMemRowStatus,
       "policy": policy,
       "policyTable": policyTable,
       "policyEntry": policyEntry,
       "policyId": policyId,
       "policyServiceId": policyServiceId,
       "policyHostId": policyHostId,
       "policyAction": policyAction,
       "policyDirection": policyDirection,
       "policySeqId": policySeqId,
       "policyVlanId": policyVlanId,
       "policyScheduleId": policyScheduleId,
       "policyRowStatus": policyRowStatus,
       "vpn": vpn,
       "ipsec": ipsec,
       "exchangeMode": exchangeMode,
       "authenticationMethod": authenticationMethod,
       "idleTimeout": idleTimeout,
       "maxLifeTimeInSecs": maxLifeTimeInSecs,
       "maxLifeTimeInKbs": maxLifeTimeInKbs,
       "refreshThresholdInSecs": refreshThresholdInSecs,
       "refreshThresholdInKbs": refreshThresholdInKbs,
       "minLifeTimeInSecs": minLifeTimeInSecs,
       "minLifeTimeInKbs": minLifeTimeInKbs,
       "exModeAggressive": exModeAggressive,
       "exModeMain": exModeMain,
       "authMethodCertificates": authMethodCertificates,
       "authMethodPreSharedKeys": authMethodPreSharedKeys,
       "ipsecConfTable": ipsecConfTable,
       "ipsecConfEntry": ipsecConfEntry,
       "ipsecConfId": ipsecConfId,
       "ipsecConfEnableConfiguration": ipsecConfEnableConfiguration,
       "ipsecConfName": ipsecConfName,
       "ipsecConfLocalAuth": ipsecConfLocalAuth,
       "ipsecConfEspTripleDESWithSHA1": ipsecConfEspTripleDESWithSHA1,
       "ipsecConfEspTripleDESWithMD5": ipsecConfEspTripleDESWithMD5,
       "ipsecConfEsp56BitDESWithMD5": ipsecConfEsp56BitDESWithMD5,
       "ipsecConfEsp56BitDESWithSHA1": ipsecConfEsp56BitDESWithSHA1,
       "ipsecConfEsp128BitAESWithMD5": ipsecConfEsp128BitAESWithMD5,
       "ipsecConfEsp128BitAESWithSHA1": ipsecConfEsp128BitAESWithSHA1,
       "ipsecConfEsp192BitAESWithMD5": ipsecConfEsp192BitAESWithMD5,
       "ipsecConfEsp192BitAESWithSHA1": ipsecConfEsp192BitAESWithSHA1,
       "ipsecConfEsp256BitAESWithMD5": ipsecConfEsp256BitAESWithMD5,
       "ipsecConfEsp256BitAESWithSHA1": ipsecConfEsp256BitAESWithSHA1,
       "ipsecConfDiffieHellmanGrp1": ipsecConfDiffieHellmanGrp1,
       "ipsecConfDiffieHellmanGrp2": ipsecConfDiffieHellmanGrp2,
       "ipsecConfDiffieHellmanGrp5": ipsecConfDiffieHellmanGrp5,
       "ipsecConfPsfMode": ipsecConfPsfMode,
       "ipsecConfCompressionDeflate": ipsecConfCompressionDeflate,
       "ipsecConfCompressionLZS": ipsecConfCompressionLZS,
       "ipsecConfRowStatus": ipsecConfRowStatus,
       "pptp": pptp,
       "pptpEnable": pptpEnable,
       "pptpRemoteIpStartAddr": pptpRemoteIpStartAddr,
       "pptpRemoteIpEndAddr": pptpRemoteIpEndAddr,
       "pptpLocalIpAddr": pptpLocalIpAddr,
       "pptpEncryption40Bit": pptpEncryption40Bit,
       "pptpEncryption128Bit": pptpEncryption128Bit,
       "pptpIdleTimeout": pptpIdleTimeout,
       "pptpLdapPwdAttrName": pptpLdapPwdAttrName,
       "pptpRoleId": pptpRoleId,
       "subnetVpn": subnetVpn,
       "subnetVpnMode": subnetVpnMode,
       "subnetVpnRtFirstIp": subnetVpnRtFirstIp,
       "subnetVpnRtLastIp": subnetVpnRtLastIp,
       "subnetVpnSharedSec": subnetVpnSharedSec,
       "subnetIpConfIdInUse": subnetIpConfIdInUse,
       "certificate": certificate,
       "certTable": certTable,
       "certEntry": certEntry,
       "certId": certId,
       "certType": certType,
       "certSubject": certSubject,
       "certStartDate": certStartDate,
       "certEndDate": certEndDate,
       "certIssuer": certIssuer,
       "certName": certName,
       "certOrg": certOrg,
       "certContent": certContent,
       "certPkey": certPkey,
       "certPkeyAlgo": certPkeyAlgo,
       "certPkeySize": certPkeySize,
       "certSerial": certSerial,
       "certSignAlgo": certSignAlgo,
       "certVersion": certVersion,
       "certRowStatus": certRowStatus,
       "l2tp": l2tp,
       "l2tpEnable": l2tpEnable,
       "l2tpRemoteIpStartAddr": l2tpRemoteIpStartAddr,
       "l2tpRemoteIpEndAddr": l2tpRemoteIpEndAddr,
       "l2tpLocalIpAddr": l2tpLocalIpAddr,
       "l2tpIdleTimeout": l2tpIdleTimeout,
       "l2tpLdapPwdAttrName": l2tpLdapPwdAttrName,
       "l2tpRoleId": l2tpRoleId,
       "configuration": configuration,
       "http": http,
       "httpPort": httpPort,
       "httpRedirect": httpRedirect,
       "httpAutoRedirectStatus": httpAutoRedirectStatus,
       "httpAutoPause": httpAutoPause,
       "httpDefaultUrl": httpDefaultUrl,
       "httpLogoutPopup": httpLogoutPopup,
       "httpRootCaUrl": httpRootCaUrl,
       "httpExServerChoice": httpExServerChoice,
       "httpPasswdChangeChoice": httpPasswdChangeChoice,
       "httpLangChangeChoice": httpLangChangeChoice,
       "httpLoginHelpButton": httpLoginHelpButton,
       "httpAttemptWait": httpAttemptWait,
       "httpMaxNumOfActiveSess": httpMaxNumOfActiveSess,
       "httpAdminACL": httpAdminACL,
       "httpRedirectToHostName": httpRedirectToHostName,
       "httpLoginAttempts": httpLoginAttempts,
       "httpChainCertChangeChoice": httpChainCertChangeChoice,
       "misc": misc,
       "statusUpTime": statusUpTime,
       "connectionCheckTime": connectionCheckTime,
       "apCheckTime": apCheckTime,
       "statusRefreshTime": statusRefreshTime,
       "apSnmpCommunity": apSnmpCommunity,
       "autoBackup": autoBackup,
       "autoBkupRate": autoBkupRate,
       "autoBkupFtpServName": autoBkupFtpServName,
       "autoBkupFtpDestDir": autoBkupFtpDestDir,
       "autoBkupFtpServUser": autoBkupFtpServUser,
       "autoBkupFtpServPasswd": autoBkupFtpServPasswd,
       "time": time,
       "tZone": tZone,
       "tMonth": tMonth,
       "tDay": tDay,
       "tYear": tYear,
       "tHours": tHours,
       "tMinutes": tMinutes,
       "tSeconds": tSeconds,
       "tNtpSync": tNtpSync,
       "tNtpServers": tNtpServers,
       "mobility": mobility,
       "mobilityMode": mobilityMode,
       "mobilityMeshKey": mobilityMeshKey,
       "publicAccess": publicAccess,
       "paFixedIpClientAccess": paFixedIpClientAccess,
       "paSMTPServerIp": paSMTPServerIp,
       "confLog": confLog,
       "confLogGroup": confLogGroup,
       "logMaxLogEntries": logMaxLogEntries,
       "logNoOfDelLogEntries": logNoOfDelLogEntries,
       "logStorage": logStorage,
       "remoteLog": remoteLog,
       "sysLogFacility": sysLogFacility,
       "logMaxRemSysLogLevel": logMaxRemSysLogLevel,
       "appLogLevTable": appLogLevTable,
       "appLogLevEntry": appLogLevEntry,
       "appLogLevId": appLogLevId,
       "appLogLevName": appLogLevName,
       "appLogLevLevel": appLogLevLevel,
       "snmpConf": snmpConf,
       "snmpTrapConf": snmpTrapConf,
       "snmpTrapMgmtTable": snmpTrapMgmtTable,
       "snmpTrapMgmtEntry": snmpTrapMgmtEntry,
       "snmpTrapMgmtId": snmpTrapMgmtId,
       "snmpTrapMgmtIpAddress": snmpTrapMgmtIpAddress,
       "snmpTrapMgmtCommunity": snmpTrapMgmtCommunity,
       "snmpTrapMgmtRowStatus": snmpTrapMgmtRowStatus,
       "blueEventTable": blueEventTable,
       "blueEventEntry": blueEventEntry,
       "btId": btId,
       "btName": btName,
       "btEventOptStatus": btEventOptStatus,
       "systemTracker": systemTracker,
       "stThresholdTable": stThresholdTable,
       "stThresholdEntry": stThresholdEntry,
       "stThresholdId": stThresholdId,
       "stThresholdAttrName": stThresholdAttrName,
       "stThresholdToLogMessage": stThresholdToLogMessage,
       "stThresholdToSendTrap": stThresholdToSendTrap,
       "stThresholdToFailover": stThresholdToFailover,
       "authentication": authentication,
       "exAuthServer": exAuthServer,
       "exRdAuthServTable": exRdAuthServTable,
       "exRdAuthServEntry": exRdAuthServEntry,
       "exRdAuthServId": exRdAuthServId,
       "exRdAuthServState": exRdAuthServState,
       "exRdAuthServName": exRdAuthServName,
       "exRdAuthServDefRoleId": exRdAuthServDefRoleId,
       "exRdAuthServRdAccId": exRdAuthServRdAccId,
       "exRdAuthServAddr": exRdAuthServAddr,
       "exRdAuthServPort": exRdAuthServPort,
       "exRdAuthServSecret": exRdAuthServSecret,
       "exRdAuthServPrecedence": exRdAuthServPrecedence,
       "exRdAuthServNotes": exRdAuthServNotes,
       "exRdAuthServRowStatus": exRdAuthServRowStatus,
       "exLdapServTable": exLdapServTable,
       "exLdapServEntry": exLdapServEntry,
       "exLdapServId": exLdapServId,
       "exLdapServState": exLdapServState,
       "exLdapServName": exLdapServName,
       "exLdapServDefRoleId": exLdapServDefRoleId,
       "exLdapServRdAccState": exLdapServRdAccState,
       "exLdapServRdAccId": exLdapServRdAccId,
       "exLdapServAddr": exLdapServAddr,
       "exLdapServPort": exLdapServPort,
       "exLdapServBase": exLdapServBase,
       "exLdapServUniqueId": exLdapServUniqueId,
       "exLdapServAccount": exLdapServAccount,
       "exLdapServFilters": exLdapServFilters,
       "exLdapServSecret": exLdapServSecret,
       "exLdapServPrecedence": exLdapServPrecedence,
       "exLdapServNotes": exLdapServNotes,
       "exLdapServSsl": exLdapServSsl,
       "exLdapServSslServer": exLdapServSslServer,
       "exLdapServSslClient": exLdapServSslClient,
       "exLdapServRowStatus": exLdapServRowStatus,
       "exNtlmServTable": exNtlmServTable,
       "exNtlmServEntry": exNtlmServEntry,
       "exNtlmServId": exNtlmServId,
       "exNtlmServState": exNtlmServState,
       "exNtlmServName": exNtlmServName,
       "exNtlmServRdAccState": exNtlmServRdAccState,
       "exNtlmServRdAccId": exNtlmServRdAccId,
       "exNtlmServDefRoleId": exNtlmServDefRoleId,
       "exNtlmServDomainName": exNtlmServDomainName,
       "exNtlmServMsdc": exNtlmServMsdc,
       "exNtlmServMsrpc": exNtlmServMsrpc,
       "exNtlmServMsad": exNtlmServMsad,
       "exNtlmServNotes": exNtlmServNotes,
       "exNtlmServRowStatus": exNtlmServRowStatus,
       "exUserRuleTable": exUserRuleTable,
       "exUserRuleEntry": exUserRuleEntry,
       "exServId": exServId,
       "exUserRuleId": exUserRuleId,
       "exUserRuleAttribute": exUserRuleAttribute,
       "exUserRuleOperator": exUserRuleOperator,
       "exUserRuleValue": exUserRuleValue,
       "exUserRuleRoleId": exUserRuleRoleId,
       "exUserRuleSeqId": exUserRuleSeqId,
       "exUserRuleRowStatus": exUserRuleRowStatus,
       "exRdAccServTable": exRdAccServTable,
       "exRdAccServEntry": exRdAccServEntry,
       "exRdAccServId": exRdAccServId,
       "exRdAccServState": exRdAccServState,
       "exRdAccServName": exRdAccServName,
       "exRdAccServAddr": exRdAccServAddr,
       "exRdAccServPort": exRdAccServPort,
       "exRdAccServSecret": exRdAccServSecret,
       "exRdAccServNotes": exRdAccServNotes,
       "exRdAccServRowStatus": exRdAccServRowStatus,
       "ex802AuthServTable": ex802AuthServTable,
       "ex802AuthServEntry": ex802AuthServEntry,
       "ex802AuthServId": ex802AuthServId,
       "ex802AuthServState": ex802AuthServState,
       "ex802AuthServName": ex802AuthServName,
       "ex802AuthServAddr": ex802AuthServAddr,
       "ex802AuthServPort": ex802AuthServPort,
       "ex802AuthServDefaultRole": ex802AuthServDefaultRole,
       "ex802AuthServNotes": ex802AuthServNotes,
       "ex802AuthServRowStatus": ex802AuthServRowStatus,
       "macDevAuthTable": macDevAuthTable,
       "macDevAuthEntry": macDevAuthEntry,
       "macDevAuthId": macDevAuthId,
       "macDevAuthState": macDevAuthState,
       "macDevAuthName": macDevAuthName,
       "macDevAuthMac": macDevAuthMac,
       "macDevAuthDefaultRole": macDevAuthDefaultRole,
       "macDevAuthNotes": macDevAuthNotes,
       "macDevAuthRowStatus": macDevAuthRowStatus,
       "interface": interface,
       "failover": failover,
       "heartBeatInterval": heartBeatInterval,
       "noOfFailedBeats": noOfFailedBeats,
       "managed": managed,
       "mIntTable": mIntTable,
       "mIntEntry": mIntEntry,
       "mIntId": mIntId,
       "mIntName": mIntName,
       "mIntEnableDhcpRelay": mIntEnableDhcpRelay,
       "mIntIpAddress": mIntIpAddress,
       "mIntNetmask": mIntNetmask,
       "mIntDhcpServerOpt": mIntDhcpServerOpt,
       "mIntNatAddresses": mIntNatAddresses,
       "mIntMulticastOpt": mIntMulticastOpt,
       "mIntDhcpStartIpAddr": mIntDhcpStartIpAddr,
       "mIntDhcpEndIpAddr": mIntDhcpEndIpAddr,
       "mIntNetbiosNameServ": mIntNetbiosNameServ,
       "mIntDnsDomainName": mIntDnsDomainName,
       "mIntDefaultLease": mIntDefaultLease,
       "mIntMaximumLease": mIntMaximumLease,
       "mIntDynamicDNS": mIntDynamicDNS,
       "mIntVlanId": mIntVlanId,
       "mIntVlanInterface": mIntVlanInterface,
       "mIntProxyArpStatus": mIntProxyArpStatus,
       "mIntRowStatus": mIntRowStatus,
       "fixedIpAddrTable": fixedIpAddrTable,
       "fixedIpAddrEntry": fixedIpAddrEntry,
       "fixedIpAddrId": fixedIpAddrId,
       "fixedIpAddrMac": fixedIpAddrMac,
       "fixedIpAddrAddress": fixedIpAddrAddress,
       "fixedIpAddrHost": fixedIpAddrHost,
       "fixedIpAddrRoleId": fixedIpAddrRoleId,
       "fixedIpAddrRowStatus": fixedIpAddrRowStatus,
       "natTable": natTable,
       "natEntry": natEntry,
       "natId": natId,
       "natProtectedIp": natProtectedIp,
       "natManagedIp": natManagedIp,
       "natRowStatus": natRowStatus,
       "protected": protected,
       "pIntTable": pIntTable,
       "pIntEntry": pIntEntry,
       "pIntId": pIntId,
       "pIntName": pIntName,
       "pIntGetIpFromDhcp": pIntGetIpFromDhcp,
       "pIntDhcpTimeout": pIntDhcpTimeout,
       "pIntIpAddress": pIntIpAddress,
       "pIntNetmask": pIntNetmask,
       "pIntGateway": pIntGateway,
       "pIntPrimaryDNS": pIntPrimaryDNS,
       "pIntSecondaryDNS": pIntSecondaryDNS,
       "pIntDefaultDomain": pIntDefaultDomain,
       "pIntHostName": pIntHostName,
       "pIntEnableMulticast": pIntEnableMulticast,
       "pIntVlanId": pIntVlanId,
       "pIntVlanInterface": pIntVlanInterface,
       "pIntProxyArpStatus": pIntProxyArpStatus,
       "pIntRowStatus": pIntRowStatus,
       "replication": replication,
       "machineRole": machineRole,
       "genSnapshot": genSnapshot,
       "slaveTable": slaveTable,
       "slaveEntry": slaveEntry,
       "slaveId": slaveId,
       "slaveEnabled": slaveEnabled,
       "slaveAddress": slaveAddress,
       "slaveNotes": slaveNotes,
       "slaveRowStatus": slaveRowStatus,
       "slaveMobility": slaveMobility,
       "connection": connection,
       "connectionTable": connectionTable,
       "connectionEntry": connectionEntry,
       "connectionId": connectionId,
       "connectionName": connectionName,
       "connectionIp": connectionIp,
       "connectionMac": connectionMac,
       "connectionRoleId": connectionRoleId,
       "connectionUserId": connectionUserId,
       "connectionLoginTime": connectionLoginTime,
       "connectionChecked": connectionChecked,
       "connectionBytes": connectionBytes,
       "connectionCurRate": connectionCurRate,
       "connectionExpiry": connectionExpiry,
       "connectionDev": connectionDev,
       "connectionHost": connectionHost,
       "connectionUnReg": connectionUnReg,
       "connectionAP": connectionAP,
       "connectionLoginAttempt": connectionLoginAttempt,
       "connectionLoginAttemptCnt": connectionLoginAttemptCnt,
       "connectionRoamMac": connectionRoamMac,
       "roles": roles,
       "roleTable": roleTable,
       "roleEntry": roleEntry,
       "roleId": roleId,
       "roleName": roleName,
       "roleType": roleType,
       "roleQosRate": roleQosRate,
       "roleQosQnt": roleQosQnt,
       "roleVpn": roleVpn,
       "roleInherit": roleInherit,
       "roleUnGuestLogin": roleUnGuestLogin,
       "roleUnUserLogin": roleUnUserLogin,
       "roleNotes": roleNotes,
       "roleQosUserIn": roleQosUserIn,
       "roleQosUserOut": roleQosUserOut,
       "roleQosPriorityIn": roleQosPriorityIn,
       "roleQosPriorityOut": roleQosPriorityOut,
       "roleQosPriInOverride": roleQosPriInOverride,
       "roleQosPriOutOverride": roleQosPriOutOverride,
       "roleQosDscpIn": roleQosDscpIn,
       "roleQosDscpOut": roleQosDscpOut,
       "roleQosDscpInOverride": roleQosDscpInOverride,
       "roleQosDscpOutOverride": roleQosDscpOutOverride,
       "roleQosRateOut": roleQosRateOut,
       "roleQosRateQntOut": roleQosRateQntOut,
       "roleVlanId": roleVlanId,
       "roleRedirect": roleRedirect,
       "roleRowStatus": roleRowStatus,
       "serviceMgmt": serviceMgmt,
       "serviceMgmtTable": serviceMgmtTable,
       "serviceMgmtEntry": serviceMgmtEntry,
       "serviceMgmtId": serviceMgmtId,
       "serviceMgmtName": serviceMgmtName,
       "serviceMgmtOptStatus": serviceMgmtOptStatus,
       "serviceMgmtDesr": serviceMgmtDesr,
       "statistics": statistics,
       "userSummary": userSummary,
       "userSumNoOfUsr": userSumNoOfUsr,
       "userSumNoOfLogdInUsr": userSumNoOfLogdInUsr,
       "userSumNoOfLogdVPNUsr": userSumNoOfLogdVPNUsr,
       "usmSumTtlBandWthInUse": usmSumTtlBandWthInUse,
       "systemStats": systemStats,
       "sysStatCpuUtil": sysStatCpuUtil,
       "sysStatMemUtil": sysStatMemUtil,
       "sysStatTotalDiskSpace": sysStatTotalDiskSpace,
       "sysStatDiskSpaceUsed": sysStatDiskSpaceUsed,
       "sysStatDiskSpaceFree": sysStatDiskSpaceFree,
       "sysStatLOgSpaceUsed": sysStatLOgSpaceUsed,
       "sysStatNeedRestart": sysStatNeedRestart,
       "vlan": vlan,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanRowId": vlanRowId,
       "vlanName": vlanName,
       "vlanId": vlanId,
       "vlanNotes": vlanNotes,
       "vlanRowStatus": vlanRowStatus,
       "vlanGrpTable": vlanGrpTable,
       "vlanGrpEntry": vlanGrpEntry,
       "vlanGrpId": vlanGrpId,
       "vlanGrpName": vlanGrpName,
       "vlanGrpRowStatus": vlanGrpRowStatus,
       "vlanGrpMemTable": vlanGrpMemTable,
       "vlanGrpMemEntry": vlanGrpMemEntry,
       "vlanGrpMemId": vlanGrpMemId,
       "vlanGrpMemRowStatus": vlanGrpMemRowStatus,
       "schedule": schedule,
       "schedTable": schedTable,
       "schedEntry": schedEntry,
       "schedRowId": schedRowId,
       "schedName": schedName,
       "schedAllDay": schedAllDay,
       "schedEveryDay": schedEveryDay,
       "schedStartDateAndTime": schedStartDateAndTime,
       "schedEndDateAndTime": schedEndDateAndTime,
       "schedMonth": schedMonth,
       "schedWeekDay": schedWeekDay,
       "schedDayOfMonth": schedDayOfMonth,
       "schedRowStatus": schedRowStatus,
       "schedGrpTable": schedGrpTable,
       "schedGrpEntry": schedGrpEntry,
       "schedGrpId": schedGrpId,
       "schedGrpName": schedGrpName,
       "schedGrpRowStatus": schedGrpRowStatus,
       "schedGrpMemTable": schedGrpMemTable,
       "schedGrpMemEntry": schedGrpMemEntry,
       "schedGrpMemId": schedGrpMemId,
       "schedGrpMemRowStatus": schedGrpMemRowStatus,
       "blueNotification": blueNotification,
       "notifyObjects": notifyObjects,
       "ntyobjLevel": ntyobjLevel,
       "ntyobjName": ntyobjName,
       "ntyobjDesc": ntyobjDesc,
       "ntyobjOID": ntyobjOID,
       "ntyobjValue": ntyobjValue,
       "blueTraps": blueTraps,
       "blueConfigTraps": blueConfigTraps,
       "blueConfigTraps0": blueConfigTraps0,
       "cctSystemConfChange": cctSystemConfChange,
       "cctUserConfChange": cctUserConfChange,
       "cctExternalServConfChange": cctExternalServConfChange,
       "cctRoleConfChange": cctRoleConfChange,
       "cctDestinationConfChange": cctDestinationConfChange,
       "cctServiceConfChange": cctServiceConfChange,
       "cctNetworkConfChange": cctNetworkConfChange,
       "cctVpnConfChange": cctVpnConfChange,
       "cctMobilityConfChange": cctMobilityConfChange,
       "cctProcessConfChange": cctProcessConfChange,
       "blueFailureTraps": blueFailureTraps,
       "blueFailureTraps0": blueFailureTraps0,
       "btSysGeneralFailure": btSysGeneralFailure,
       "btUserLoginFailure": btUserLoginFailure,
       "btProcessFailure": btProcessFailure,
       "btAuthFailure": btAuthFailure,
       "btSystemFailover": btSystemFailover,
       "blueThresholdTraps": blueThresholdTraps,
       "blueThresholdTraps0": blueThresholdTraps0,
       "btConditionalEvent": btConditionalEvent,
       "btCpuLoadEvent": btCpuLoadEvent,
       "btMemSwapUsageEvent": btMemSwapUsageEvent,
       "btDiskUsageEvent": btDiskUsageEvent,
       "blueGeneralTraps": blueGeneralTraps,
       "blueGeneralTraps0": blueGeneralTraps0,
       "btLinkUp": btLinkUp,
       "btLinkDown": btLinkDown,
       "btSystemGeneralTrap": btSystemGeneralTrap}
)
