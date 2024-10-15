# SNMP MIB module (HP-AUTZ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-AUTZ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:55 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpSwitchAuthorizationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32)
)
hpSwitchAuthorizationMIB.setRevisions(
        ("2017-03-16 00:00",
         "2016-10-20 00:00",
         "2016-05-09 00:00",
         "2016-01-07 00:00",
         "2014-08-04 00:00",
         "2011-02-07 00:00",
         "2007-08-29 00:00",
         "2005-10-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpAutzUserRoleName(OctetString, TextualConvention):
    status = "current"
    displayHint = "63a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



# MIB Managed Objects in the order of their OIDs

_HpicfSwitchAuthorizationNotifications_ObjectIdentity = ObjectIdentity
hpicfSwitchAuthorizationNotifications = _HpicfSwitchAuthorizationNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 0)
)
_HpSwitchAuthorizationConfig_ObjectIdentity = ObjectIdentity
hpSwitchAuthorizationConfig = _HpSwitchAuthorizationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1)
)
_HpSwitchAutzServiceTable_Object = MibTable
hpSwitchAutzServiceTable = _HpSwitchAutzServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchAutzServiceTable.setStatus("current")
_HpSwitchAutzServiceEntry_Object = MibTableRow
hpSwitchAutzServiceEntry = _HpSwitchAutzServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1)
)
hpSwitchAutzServiceEntry.setIndexNames(
    (0, "HP-AUTZ-MIB", "hpSwitchAutzServiceType"),
)
if mibBuilder.loadTexts:
    hpSwitchAutzServiceEntry.setStatus("current")


class _HpSwitchAutzServiceType_Type(Integer32):
    """Custom type hpSwitchAutzServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commands", 1),
          ("exec", 2),
          ("network", 3))
    )


_HpSwitchAutzServiceType_Type.__name__ = "Integer32"
_HpSwitchAutzServiceType_Object = MibTableColumn
hpSwitchAutzServiceType = _HpSwitchAutzServiceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 1),
    _HpSwitchAutzServiceType_Type()
)
hpSwitchAutzServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAutzServiceType.setStatus("current")


class _HpSwitchAutzServicePrimaryMethod_Type(Integer32):
    """Custom type hpSwitchAutzServicePrimaryMethod based on Integer32"""
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
        *(("auto", 5),
          ("local", 1),
          ("none", 4),
          ("radius", 3),
          ("tacacs", 2))
    )


_HpSwitchAutzServicePrimaryMethod_Type.__name__ = "Integer32"
_HpSwitchAutzServicePrimaryMethod_Object = MibTableColumn
hpSwitchAutzServicePrimaryMethod = _HpSwitchAutzServicePrimaryMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 2),
    _HpSwitchAutzServicePrimaryMethod_Type()
)
hpSwitchAutzServicePrimaryMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAutzServicePrimaryMethod.setStatus("current")


class _HpSwitchAutzServiceSecondaryMethod_Type(Integer32):
    """Custom type hpSwitchAutzServiceSecondaryMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("none", 2))
    )


_HpSwitchAutzServiceSecondaryMethod_Type.__name__ = "Integer32"
_HpSwitchAutzServiceSecondaryMethod_Object = MibTableColumn
hpSwitchAutzServiceSecondaryMethod = _HpSwitchAutzServiceSecondaryMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 3),
    _HpSwitchAutzServiceSecondaryMethod_Type()
)
hpSwitchAutzServiceSecondaryMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAutzServiceSecondaryMethod.setStatus("current")


class _HpSwitchAutzServiceCommandsLevel_Type(Integer32):
    """Custom type hpSwitchAutzServiceCommandsLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("managerlevelonly", 2))
    )


_HpSwitchAutzServiceCommandsLevel_Type.__name__ = "Integer32"
_HpSwitchAutzServiceCommandsLevel_Object = MibTableColumn
hpSwitchAutzServiceCommandsLevel = _HpSwitchAutzServiceCommandsLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 4),
    _HpSwitchAutzServiceCommandsLevel_Type()
)
hpSwitchAutzServiceCommandsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAutzServiceCommandsLevel.setStatus("current")
_HpicfSwitchAuthObjects_ObjectIdentity = ObjectIdentity
hpicfSwitchAuthObjects = _HpicfSwitchAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2)
)


class _HpicfSwitchAuthServerType_Type(Integer32):
    """Custom type hpicfSwitchAuthServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 9),
          ("radius", 1),
          ("tacacs", 2))
    )


_HpicfSwitchAuthServerType_Type.__name__ = "Integer32"
_HpicfSwitchAuthServerType_Object = MibScalar
hpicfSwitchAuthServerType = _HpicfSwitchAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2, 1),
    _HpicfSwitchAuthServerType_Type()
)
hpicfSwitchAuthServerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfSwitchAuthServerType.setStatus("current")
_HpicfSwitchAuthServerIPType_Type = InetAddressType
_HpicfSwitchAuthServerIPType_Object = MibScalar
hpicfSwitchAuthServerIPType = _HpicfSwitchAuthServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2, 2),
    _HpicfSwitchAuthServerIPType_Type()
)
hpicfSwitchAuthServerIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfSwitchAuthServerIPType.setStatus("current")
_HpicfSwitchAuthServerIP_Type = InetAddress
_HpicfSwitchAuthServerIP_Object = MibScalar
hpicfSwitchAuthServerIP = _HpicfSwitchAuthServerIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2, 3),
    _HpicfSwitchAuthServerIP_Type()
)
hpicfSwitchAuthServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfSwitchAuthServerIP.setStatus("current")
_HpSwitchAuthConfigObjects_ObjectIdentity = ObjectIdentity
hpSwitchAuthConfigObjects = _HpSwitchAuthConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 3)
)


class _HpicfSwitchAuthServerNotifyEnable_Type(Integer32):
    """Custom type hpicfSwitchAuthServerNotifyEnable based on Integer32"""
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


_HpicfSwitchAuthServerNotifyEnable_Type.__name__ = "Integer32"
_HpicfSwitchAuthServerNotifyEnable_Object = MibScalar
hpicfSwitchAuthServerNotifyEnable = _HpicfSwitchAuthServerNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 3, 1),
    _HpicfSwitchAuthServerNotifyEnable_Type()
)
hpicfSwitchAuthServerNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSwitchAuthServerNotifyEnable.setStatus("current")
_HpSwitchAuthLocalPrivConfigObjects_ObjectIdentity = ObjectIdentity
hpSwitchAuthLocalPrivConfigObjects = _HpSwitchAuthLocalPrivConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4)
)
_HpSwitchLocalMgmtPrivGroupsTable_Object = MibTable
hpSwitchLocalMgmtPrivGroupsTable = _HpSwitchLocalMgmtPrivGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivGroupsTable.setStatus("current")
_HpSwitchLocalMgmtPrivGroupsEntry_Object = MibTableRow
hpSwitchLocalMgmtPrivGroupsEntry = _HpSwitchLocalMgmtPrivGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1)
)
hpSwitchLocalMgmtPrivGroupsEntry.setIndexNames(
    (0, "HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivGroupsEntry.setStatus("current")


class _HpSwitchLocalMgmtPrivGroupIndex_Type(Integer32):
    """Custom type hpSwitchLocalMgmtPrivGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSwitchLocalMgmtPrivGroupIndex_Type.__name__ = "Integer32"
_HpSwitchLocalMgmtPrivGroupIndex_Object = MibTableColumn
hpSwitchLocalMgmtPrivGroupIndex = _HpSwitchLocalMgmtPrivGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1, 1),
    _HpSwitchLocalMgmtPrivGroupIndex_Type()
)
hpSwitchLocalMgmtPrivGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivGroupIndex.setStatus("current")


class _HpSwitchLocalMgmtPrivGroupName_Type(OctetString):
    """Custom type hpSwitchLocalMgmtPrivGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpSwitchLocalMgmtPrivGroupName_Type.__name__ = "OctetString"
_HpSwitchLocalMgmtPrivGroupName_Object = MibTableColumn
hpSwitchLocalMgmtPrivGroupName = _HpSwitchLocalMgmtPrivGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1, 2),
    _HpSwitchLocalMgmtPrivGroupName_Type()
)
hpSwitchLocalMgmtPrivGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivGroupName.setStatus("current")
_HpSwitchLocalMgmtPrivGroupStatus_Type = RowStatus
_HpSwitchLocalMgmtPrivGroupStatus_Object = MibTableColumn
hpSwitchLocalMgmtPrivGroupStatus = _HpSwitchLocalMgmtPrivGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1, 3),
    _HpSwitchLocalMgmtPrivGroupStatus_Type()
)
hpSwitchLocalMgmtPrivGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivGroupStatus.setStatus("current")
_HpSwitchLocalMgmtPrivCommandsTable_Object = MibTable
hpSwitchLocalMgmtPrivCommandsTable = _HpSwitchLocalMgmtPrivCommandsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivCommandsTable.setStatus("current")
_HpSwitchLocalMgmtPrivCommandsEntry_Object = MibTableRow
hpSwitchLocalMgmtPrivCommandsEntry = _HpSwitchLocalMgmtPrivCommandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1)
)
hpSwitchLocalMgmtPrivCommandsEntry.setIndexNames(
    (0, "HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupIndex"),
    (0, "HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdSequenceIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivCommandsEntry.setStatus("current")


class _HpSwitchLocalMgmtPrivCmdSequenceIndex_Type(Integer32):
    """Custom type hpSwitchLocalMgmtPrivCmdSequenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSwitchLocalMgmtPrivCmdSequenceIndex_Type.__name__ = "Integer32"
_HpSwitchLocalMgmtPrivCmdSequenceIndex_Object = MibTableColumn
hpSwitchLocalMgmtPrivCmdSequenceIndex = _HpSwitchLocalMgmtPrivCmdSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 1),
    _HpSwitchLocalMgmtPrivCmdSequenceIndex_Type()
)
hpSwitchLocalMgmtPrivCmdSequenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivCmdSequenceIndex.setStatus("current")


class _HpSwitchLocalMgmtPrivCmdMatchStr_Type(OctetString):
    """Custom type hpSwitchLocalMgmtPrivCmdMatchStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_HpSwitchLocalMgmtPrivCmdMatchStr_Type.__name__ = "OctetString"
_HpSwitchLocalMgmtPrivCmdMatchStr_Object = MibTableColumn
hpSwitchLocalMgmtPrivCmdMatchStr = _HpSwitchLocalMgmtPrivCmdMatchStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 2),
    _HpSwitchLocalMgmtPrivCmdMatchStr_Type()
)
hpSwitchLocalMgmtPrivCmdMatchStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivCmdMatchStr.setStatus("current")


class _HpSwitchLocalMgmtPrivCmdPriv_Type(Integer32):
    """Custom type hpSwitchLocalMgmtPrivCmdPriv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HpSwitchLocalMgmtPrivCmdPriv_Type.__name__ = "Integer32"
_HpSwitchLocalMgmtPrivCmdPriv_Object = MibTableColumn
hpSwitchLocalMgmtPrivCmdPriv = _HpSwitchLocalMgmtPrivCmdPriv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 3),
    _HpSwitchLocalMgmtPrivCmdPriv_Type()
)
hpSwitchLocalMgmtPrivCmdPriv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivCmdPriv.setStatus("current")


class _HpSwitchLocalMgmtPrivCmdSendLog_Type(Integer32):
    """Custom type hpSwitchLocalMgmtPrivCmdSendLog based on Integer32"""
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


_HpSwitchLocalMgmtPrivCmdSendLog_Type.__name__ = "Integer32"
_HpSwitchLocalMgmtPrivCmdSendLog_Object = MibTableColumn
hpSwitchLocalMgmtPrivCmdSendLog = _HpSwitchLocalMgmtPrivCmdSendLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 4),
    _HpSwitchLocalMgmtPrivCmdSendLog_Type()
)
hpSwitchLocalMgmtPrivCmdSendLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivCmdSendLog.setStatus("current")
_HpSwitchLocalMgmtPrivCmdStatus_Type = RowStatus
_HpSwitchLocalMgmtPrivCmdStatus_Object = MibTableColumn
hpSwitchLocalMgmtPrivCmdStatus = _HpSwitchLocalMgmtPrivCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 5),
    _HpSwitchLocalMgmtPrivCmdStatus_Type()
)
hpSwitchLocalMgmtPrivCmdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivCmdStatus.setStatus("current")
_HpSwitchAutzUserRole_ObjectIdentity = ObjectIdentity
hpSwitchAutzUserRole = _HpSwitchAutzUserRole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5)
)


class _HpSwitchAutzUserRoleEnabled_Type(TruthValue):
    """Custom type hpSwitchAutzUserRoleEnabled based on TruthValue"""


_HpSwitchAutzUserRoleEnabled_Object = MibScalar
hpSwitchAutzUserRoleEnabled = _HpSwitchAutzUserRoleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 1),
    _HpSwitchAutzUserRoleEnabled_Type()
)
hpSwitchAutzUserRoleEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleEnabled.setStatus("current")
_HpSwitchAutzUserRoleInitialRoleName_Type = HpAutzUserRoleName
_HpSwitchAutzUserRoleInitialRoleName_Object = MibScalar
hpSwitchAutzUserRoleInitialRoleName = _HpSwitchAutzUserRoleInitialRoleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 2),
    _HpSwitchAutzUserRoleInitialRoleName_Type()
)
hpSwitchAutzUserRoleInitialRoleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleInitialRoleName.setStatus("current")
_HpSwitchAutzUserRoleTable_Object = MibTable
hpSwitchAutzUserRoleTable = _HpSwitchAutzUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleTable.setStatus("current")
_HpSwitchAutzUserRoleEntry_Object = MibTableRow
hpSwitchAutzUserRoleEntry = _HpSwitchAutzUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1)
)
hpSwitchAutzUserRoleEntry.setIndexNames(
    (0, "HP-AUTZ-MIB", "hpSwitchAutzUserRoleName"),
)
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleEntry.setStatus("current")
_HpSwitchAutzUserRoleName_Type = HpAutzUserRoleName
_HpSwitchAutzUserRoleName_Object = MibTableColumn
hpSwitchAutzUserRoleName = _HpSwitchAutzUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 1),
    _HpSwitchAutzUserRoleName_Type()
)
hpSwitchAutzUserRoleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleName.setStatus("current")
_HpSwitchAutzUserRoleRowStatus_Type = RowStatus
_HpSwitchAutzUserRoleRowStatus_Object = MibTableColumn
hpSwitchAutzUserRoleRowStatus = _HpSwitchAutzUserRoleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 2),
    _HpSwitchAutzUserRoleRowStatus_Type()
)
hpSwitchAutzUserRoleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleRowStatus.setStatus("current")


class _HpSwitchAutzUserRoleType_Type(Integer32):
    """Custom type hpSwitchAutzUserRoleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloaded", 3),
          ("local", 2),
          ("predefined", 1))
    )


_HpSwitchAutzUserRoleType_Type.__name__ = "Integer32"
_HpSwitchAutzUserRoleType_Object = MibTableColumn
hpSwitchAutzUserRoleType = _HpSwitchAutzUserRoleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 3),
    _HpSwitchAutzUserRoleType_Type()
)
hpSwitchAutzUserRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleType.setStatus("current")


class _HpSwitchAutzUserRoleCaptivePortalProfileName_Type(OctetString):
    """Custom type hpSwitchAutzUserRoleCaptivePortalProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpSwitchAutzUserRoleCaptivePortalProfileName_Type.__name__ = "OctetString"
_HpSwitchAutzUserRoleCaptivePortalProfileName_Object = MibTableColumn
hpSwitchAutzUserRoleCaptivePortalProfileName = _HpSwitchAutzUserRoleCaptivePortalProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 4),
    _HpSwitchAutzUserRoleCaptivePortalProfileName_Type()
)
hpSwitchAutzUserRoleCaptivePortalProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleCaptivePortalProfileName.setStatus("current")


class _HpSwitchAutzUserRoleIngressUserPolicyName_Type(OctetString):
    """Custom type hpSwitchAutzUserRoleIngressUserPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpSwitchAutzUserRoleIngressUserPolicyName_Type.__name__ = "OctetString"
_HpSwitchAutzUserRoleIngressUserPolicyName_Object = MibTableColumn
hpSwitchAutzUserRoleIngressUserPolicyName = _HpSwitchAutzUserRoleIngressUserPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 5),
    _HpSwitchAutzUserRoleIngressUserPolicyName_Type()
)
hpSwitchAutzUserRoleIngressUserPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleIngressUserPolicyName.setStatus("current")


class _HpSwitchAutzUserRoleReauthPeriod_Type(Integer32):
    """Custom type hpSwitchAutzUserRoleReauthPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_HpSwitchAutzUserRoleReauthPeriod_Type.__name__ = "Integer32"
_HpSwitchAutzUserRoleReauthPeriod_Object = MibTableColumn
hpSwitchAutzUserRoleReauthPeriod = _HpSwitchAutzUserRoleReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 6),
    _HpSwitchAutzUserRoleReauthPeriod_Type()
)
hpSwitchAutzUserRoleReauthPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleReauthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleReauthPeriod.setUnits("seconds")
_HpSwitchAutzUserRoleVlanId_Type = VlanIndex
_HpSwitchAutzUserRoleVlanId_Object = MibTableColumn
hpSwitchAutzUserRoleVlanId = _HpSwitchAutzUserRoleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 7),
    _HpSwitchAutzUserRoleVlanId_Type()
)
hpSwitchAutzUserRoleVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleVlanId.setStatus("current")


class _HpSwitchAutzUserRoleVlanName_Type(SnmpAdminString):
    """Custom type hpSwitchAutzUserRoleVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpSwitchAutzUserRoleVlanName_Type.__name__ = "SnmpAdminString"
_HpSwitchAutzUserRoleVlanName_Object = MibTableColumn
hpSwitchAutzUserRoleVlanName = _HpSwitchAutzUserRoleVlanName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 8),
    _HpSwitchAutzUserRoleVlanName_Type()
)
hpSwitchAutzUserRoleVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleVlanName.setStatus("current")


class _HpSwitchAutzUserRoleTunneledNodeServerRedirect_Type(Integer32):
    """Custom type hpSwitchAutzUserRoleTunneledNodeServerRedirect based on Integer32"""
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


_HpSwitchAutzUserRoleTunneledNodeServerRedirect_Type.__name__ = "Integer32"
_HpSwitchAutzUserRoleTunneledNodeServerRedirect_Object = MibTableColumn
hpSwitchAutzUserRoleTunneledNodeServerRedirect = _HpSwitchAutzUserRoleTunneledNodeServerRedirect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 9),
    _HpSwitchAutzUserRoleTunneledNodeServerRedirect_Type()
)
hpSwitchAutzUserRoleTunneledNodeServerRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleTunneledNodeServerRedirect.setStatus("current")


class _HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Type(OctetString):
    """Custom type hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Type.__name__ = "OctetString"
_HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Object = MibTableColumn
hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole = _HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 10),
    _HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Type()
)
hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole.setStatus("current")
_HpSwitchAutzUserRoleTaggedVlanId_Type = VlanIndex
_HpSwitchAutzUserRoleTaggedVlanId_Object = MibTableColumn
hpSwitchAutzUserRoleTaggedVlanId = _HpSwitchAutzUserRoleTaggedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 11),
    _HpSwitchAutzUserRoleTaggedVlanId_Type()
)
hpSwitchAutzUserRoleTaggedVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleTaggedVlanId.setStatus("current")


class _HpSwitchAutzUserRoleTaggedVlanName_Type(SnmpAdminString):
    """Custom type hpSwitchAutzUserRoleTaggedVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpSwitchAutzUserRoleTaggedVlanName_Type.__name__ = "SnmpAdminString"
_HpSwitchAutzUserRoleTaggedVlanName_Object = MibTableColumn
hpSwitchAutzUserRoleTaggedVlanName = _HpSwitchAutzUserRoleTaggedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 12),
    _HpSwitchAutzUserRoleTaggedVlanName_Type()
)
hpSwitchAutzUserRoleTaggedVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleTaggedVlanName.setStatus("current")


class _HpSwitchAutzUserRoleDownloadedEnabled_Type(TruthValue):
    """Custom type hpSwitchAutzUserRoleDownloadedEnabled based on TruthValue"""


_HpSwitchAutzUserRoleDownloadedEnabled_Object = MibScalar
hpSwitchAutzUserRoleDownloadedEnabled = _HpSwitchAutzUserRoleDownloadedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 4),
    _HpSwitchAutzUserRoleDownloadedEnabled_Type()
)
hpSwitchAutzUserRoleDownloadedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleDownloadedEnabled.setStatus("current")
_HpSwitchAuthorizationConformance_ObjectIdentity = ObjectIdentity
hpSwitchAuthorizationConformance = _HpSwitchAuthorizationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2)
)
_HpSwitchAuthorizationMIBCompliances_ObjectIdentity = ObjectIdentity
hpSwitchAuthorizationMIBCompliances = _HpSwitchAuthorizationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1)
)
_HpSwitchAuthorizationMIBGroups_ObjectIdentity = ObjectIdentity
hpSwitchAuthorizationMIBGroups = _HpSwitchAuthorizationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2)
)

# Managed Objects groups

hpSwitchAuthorizationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 1)
)
hpSwitchAuthorizationConfigGroup.setObjects(
      *(("HP-AUTZ-MIB", "hpSwitchAutzServicePrimaryMethod"),
        ("HP-AUTZ-MIB", "hpSwitchAutzServiceSecondaryMethod"),
        ("HP-AUTZ-MIB", "hpSwitchAutzServiceCommandsLevel"),
        ("HP-AUTZ-MIB", "hpicfSwitchAuthServerNotifyEnable"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthorizationConfigGroup.setStatus("current")

hpicfSwitchAuthorizationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 3)
)
hpicfSwitchAuthorizationObjectsGroup.setObjects(
      *(("HP-AUTZ-MIB", "hpicfSwitchAuthServerType"),
        ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIPType"),
        ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIP"))
)
if mibBuilder.loadTexts:
    hpicfSwitchAuthorizationObjectsGroup.setStatus("current")

hpSwitchAutzLocalMgmtPrivGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 4)
)
hpSwitchAutzLocalMgmtPrivGroup.setObjects(
      *(("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupName"),
        ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdMatchStr"),
        ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdPriv"),
        ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdSendLog"))
)
if mibBuilder.loadTexts:
    hpSwitchAutzLocalMgmtPrivGroup.setStatus("current")

hpSwitchAutzLocalMgmtPrivGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 5)
)
hpSwitchAutzLocalMgmtPrivGroup1.setObjects(
      *(("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdStatus"),
        ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchAutzLocalMgmtPrivGroup1.setStatus("current")

hpSwitchAutzUserRoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 6)
)
hpSwitchAutzUserRoleGroup.setObjects(
      *(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"))
)
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleGroup.setStatus("deprecated")

hpSwitchAutzUserRoleGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 7)
)
hpSwitchAutzUserRoleGroup1.setObjects(
      *(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"))
)
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleGroup1.setStatus("deprecated")

hpSwitchAutzUserRoleGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 8)
)
hpSwitchAutzUserRoleGroup2.setObjects(
      *(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanId"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanName"))
)
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleGroup2.setStatus("deprecated")

hpSwitchAutzUserRoleGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 9)
)
hpSwitchAutzUserRoleGroup3.setObjects(
      *(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanId"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanName"),
        ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleDownloadedEnabled"))
)
if mibBuilder.loadTexts:
    hpSwitchAutzUserRoleGroup3.setStatus("current")


# Notification objects

hpicfSwitchAuthServerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 0, 1)
)
hpicfSwitchAuthServerFail.setObjects(
      *(("HP-AUTZ-MIB", "hpicfSwitchAuthServerType"),
        ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIPType"),
        ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIP"))
)
if mibBuilder.loadTexts:
    hpicfSwitchAuthServerFail.setStatus(
        "current"
    )


# Notifications groups

hpicfSwitchAuthorizationNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 2)
)
hpicfSwitchAuthorizationNotificationGroup.setObjects(
    ("HP-AUTZ-MIB", "hpicfSwitchAuthServerFail")
)
if mibBuilder.loadTexts:
    hpicfSwitchAuthorizationNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpSwitchAuthorizationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchAuthorizationMIBCompliance.setStatus(
        "current"
    )

hpSwitchLocalMgmtPrivGrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivGrpMIBCompliance.setStatus(
        "current"
    )

hpSwitchLocalMgmtPrivGrpMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivGrpMIBCompliance1.setStatus(
        "current"
    )

hpSwitchAuthorizationObjectsGrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpSwitchAuthorizationObjectsGrpMIBCompliance.setStatus(
        "current"
    )

hpSwitchAuthorizationNotificationGrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hpSwitchAuthorizationNotificationGrpMIBCompliance.setStatus(
        "current"
    )

hpSwitchAutzRoleGrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hpSwitchAutzRoleGrpCompliance.setStatus(
        "deprecated"
    )

hpSwitchAutzRoleGrpCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hpSwitchAutzRoleGrpCompliance1.setStatus(
        "deprecated"
    )

hpSwitchAutzRoleGrpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hpSwitchAutzRoleGrpCompliance2.setStatus(
        "deprecated"
    )

hpSwitchAutzRoleGrpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hpSwitchAutzRoleGrpCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-AUTZ-MIB",
    **{"HpAutzUserRoleName": HpAutzUserRoleName,
       "hpSwitchAuthorizationMIB": hpSwitchAuthorizationMIB,
       "hpicfSwitchAuthorizationNotifications": hpicfSwitchAuthorizationNotifications,
       "hpicfSwitchAuthServerFail": hpicfSwitchAuthServerFail,
       "hpSwitchAuthorizationConfig": hpSwitchAuthorizationConfig,
       "hpSwitchAutzServiceTable": hpSwitchAutzServiceTable,
       "hpSwitchAutzServiceEntry": hpSwitchAutzServiceEntry,
       "hpSwitchAutzServiceType": hpSwitchAutzServiceType,
       "hpSwitchAutzServicePrimaryMethod": hpSwitchAutzServicePrimaryMethod,
       "hpSwitchAutzServiceSecondaryMethod": hpSwitchAutzServiceSecondaryMethod,
       "hpSwitchAutzServiceCommandsLevel": hpSwitchAutzServiceCommandsLevel,
       "hpicfSwitchAuthObjects": hpicfSwitchAuthObjects,
       "hpicfSwitchAuthServerType": hpicfSwitchAuthServerType,
       "hpicfSwitchAuthServerIPType": hpicfSwitchAuthServerIPType,
       "hpicfSwitchAuthServerIP": hpicfSwitchAuthServerIP,
       "hpSwitchAuthConfigObjects": hpSwitchAuthConfigObjects,
       "hpicfSwitchAuthServerNotifyEnable": hpicfSwitchAuthServerNotifyEnable,
       "hpSwitchAuthLocalPrivConfigObjects": hpSwitchAuthLocalPrivConfigObjects,
       "hpSwitchLocalMgmtPrivGroupsTable": hpSwitchLocalMgmtPrivGroupsTable,
       "hpSwitchLocalMgmtPrivGroupsEntry": hpSwitchLocalMgmtPrivGroupsEntry,
       "hpSwitchLocalMgmtPrivGroupIndex": hpSwitchLocalMgmtPrivGroupIndex,
       "hpSwitchLocalMgmtPrivGroupName": hpSwitchLocalMgmtPrivGroupName,
       "hpSwitchLocalMgmtPrivGroupStatus": hpSwitchLocalMgmtPrivGroupStatus,
       "hpSwitchLocalMgmtPrivCommandsTable": hpSwitchLocalMgmtPrivCommandsTable,
       "hpSwitchLocalMgmtPrivCommandsEntry": hpSwitchLocalMgmtPrivCommandsEntry,
       "hpSwitchLocalMgmtPrivCmdSequenceIndex": hpSwitchLocalMgmtPrivCmdSequenceIndex,
       "hpSwitchLocalMgmtPrivCmdMatchStr": hpSwitchLocalMgmtPrivCmdMatchStr,
       "hpSwitchLocalMgmtPrivCmdPriv": hpSwitchLocalMgmtPrivCmdPriv,
       "hpSwitchLocalMgmtPrivCmdSendLog": hpSwitchLocalMgmtPrivCmdSendLog,
       "hpSwitchLocalMgmtPrivCmdStatus": hpSwitchLocalMgmtPrivCmdStatus,
       "hpSwitchAutzUserRole": hpSwitchAutzUserRole,
       "hpSwitchAutzUserRoleEnabled": hpSwitchAutzUserRoleEnabled,
       "hpSwitchAutzUserRoleInitialRoleName": hpSwitchAutzUserRoleInitialRoleName,
       "hpSwitchAutzUserRoleTable": hpSwitchAutzUserRoleTable,
       "hpSwitchAutzUserRoleEntry": hpSwitchAutzUserRoleEntry,
       "hpSwitchAutzUserRoleName": hpSwitchAutzUserRoleName,
       "hpSwitchAutzUserRoleRowStatus": hpSwitchAutzUserRoleRowStatus,
       "hpSwitchAutzUserRoleType": hpSwitchAutzUserRoleType,
       "hpSwitchAutzUserRoleCaptivePortalProfileName": hpSwitchAutzUserRoleCaptivePortalProfileName,
       "hpSwitchAutzUserRoleIngressUserPolicyName": hpSwitchAutzUserRoleIngressUserPolicyName,
       "hpSwitchAutzUserRoleReauthPeriod": hpSwitchAutzUserRoleReauthPeriod,
       "hpSwitchAutzUserRoleVlanId": hpSwitchAutzUserRoleVlanId,
       "hpSwitchAutzUserRoleVlanName": hpSwitchAutzUserRoleVlanName,
       "hpSwitchAutzUserRoleTunneledNodeServerRedirect": hpSwitchAutzUserRoleTunneledNodeServerRedirect,
       "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole": hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole,
       "hpSwitchAutzUserRoleTaggedVlanId": hpSwitchAutzUserRoleTaggedVlanId,
       "hpSwitchAutzUserRoleTaggedVlanName": hpSwitchAutzUserRoleTaggedVlanName,
       "hpSwitchAutzUserRoleDownloadedEnabled": hpSwitchAutzUserRoleDownloadedEnabled,
       "hpSwitchAuthorizationConformance": hpSwitchAuthorizationConformance,
       "hpSwitchAuthorizationMIBCompliances": hpSwitchAuthorizationMIBCompliances,
       "hpSwitchAuthorizationMIBCompliance": hpSwitchAuthorizationMIBCompliance,
       "hpSwitchLocalMgmtPrivGrpMIBCompliance": hpSwitchLocalMgmtPrivGrpMIBCompliance,
       "hpSwitchLocalMgmtPrivGrpMIBCompliance1": hpSwitchLocalMgmtPrivGrpMIBCompliance1,
       "hpSwitchAuthorizationObjectsGrpMIBCompliance": hpSwitchAuthorizationObjectsGrpMIBCompliance,
       "hpSwitchAuthorizationNotificationGrpMIBCompliance": hpSwitchAuthorizationNotificationGrpMIBCompliance,
       "hpSwitchAutzRoleGrpCompliance": hpSwitchAutzRoleGrpCompliance,
       "hpSwitchAutzRoleGrpCompliance1": hpSwitchAutzRoleGrpCompliance1,
       "hpSwitchAutzRoleGrpCompliance2": hpSwitchAutzRoleGrpCompliance2,
       "hpSwitchAutzRoleGrpCompliance3": hpSwitchAutzRoleGrpCompliance3,
       "hpSwitchAuthorizationMIBGroups": hpSwitchAuthorizationMIBGroups,
       "hpSwitchAuthorizationConfigGroup": hpSwitchAuthorizationConfigGroup,
       "hpicfSwitchAuthorizationNotificationGroup": hpicfSwitchAuthorizationNotificationGroup,
       "hpicfSwitchAuthorizationObjectsGroup": hpicfSwitchAuthorizationObjectsGroup,
       "hpSwitchAutzLocalMgmtPrivGroup": hpSwitchAutzLocalMgmtPrivGroup,
       "hpSwitchAutzLocalMgmtPrivGroup1": hpSwitchAutzLocalMgmtPrivGroup1,
       "hpSwitchAutzUserRoleGroup": hpSwitchAutzUserRoleGroup,
       "hpSwitchAutzUserRoleGroup1": hpSwitchAutzUserRoleGroup1,
       "hpSwitchAutzUserRoleGroup2": hpSwitchAutzUserRoleGroup2,
       "hpSwitchAutzUserRoleGroup3": hpSwitchAutzUserRoleGroup3}
)
