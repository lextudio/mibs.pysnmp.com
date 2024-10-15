# SNMP MIB module (H3C-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-USER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:38 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cUser = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



class ServiceType(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_H3cUserObjects_ObjectIdentity = ObjectIdentity
h3cUserObjects = _H3cUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1)
)
_H3cUserInfoTable_Object = MibTable
h3cUserInfoTable = _H3cUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1)
)
if mibBuilder.loadTexts:
    h3cUserInfoTable.setStatus("current")
_H3cUserInfoEntry_Object = MibTableRow
h3cUserInfoEntry = _H3cUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1)
)
h3cUserInfoEntry.setIndexNames(
    (0, "H3C-USER-MIB", "h3cUserIndex"),
)
if mibBuilder.loadTexts:
    h3cUserInfoEntry.setStatus("current")
_H3cUserName_Type = DisplayString
_H3cUserName_Object = MibTableColumn
h3cUserName = _H3cUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 1),
    _H3cUserName_Type()
)
h3cUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cUserName.setStatus("current")
_H3cUserPassword_Type = DisplayString
_H3cUserPassword_Object = MibTableColumn
h3cUserPassword = _H3cUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 2),
    _H3cUserPassword_Type()
)
h3cUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cUserPassword.setStatus("current")
_H3cAuthMode_Type = Integer32
_H3cAuthMode_Object = MibTableColumn
h3cAuthMode = _H3cAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 3),
    _H3cAuthMode_Type()
)
h3cAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAuthMode.setStatus("current")
_H3cUserLevel_Type = Integer32
_H3cUserLevel_Object = MibTableColumn
h3cUserLevel = _H3cUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 4),
    _H3cUserLevel_Type()
)
h3cUserLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cUserLevel.setStatus("current")


class _H3cUserState_Type(Integer32):
    """Custom type h3cUserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("block", 1))
    )


_H3cUserState_Type.__name__ = "Integer32"
_H3cUserState_Object = MibTableColumn
h3cUserState = _H3cUserState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 5),
    _H3cUserState_Type()
)
h3cUserState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cUserState.setStatus("current")
_H3cUserInfoRowStatus_Type = RowStatus
_H3cUserInfoRowStatus_Object = MibTableColumn
h3cUserInfoRowStatus = _H3cUserInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 6),
    _H3cUserInfoRowStatus_Type()
)
h3cUserInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cUserInfoRowStatus.setStatus("current")


class _H3cUserIndex_Type(Integer32):
    """Custom type h3cUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483646),
    )


_H3cUserIndex_Type.__name__ = "Integer32"
_H3cUserIndex_Object = MibTableColumn
h3cUserIndex = _H3cUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 1, 1, 7),
    _H3cUserIndex_Type()
)
h3cUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cUserIndex.setStatus("current")
_H3cUserAttributeTable_Object = MibTable
h3cUserAttributeTable = _H3cUserAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2)
)
if mibBuilder.loadTexts:
    h3cUserAttributeTable.setStatus("current")
_H3cUserAttributeEntry_Object = MibTableRow
h3cUserAttributeEntry = _H3cUserAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1)
)
h3cUserAttributeEntry.setIndexNames(
    (0, "H3C-USER-MIB", "h3cUserIndex"),
)
if mibBuilder.loadTexts:
    h3cUserAttributeEntry.setStatus("current")
_H3cAccessLimit_Type = Integer32
_H3cAccessLimit_Object = MibTableColumn
h3cAccessLimit = _H3cAccessLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 1),
    _H3cAccessLimit_Type()
)
h3cAccessLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cAccessLimit.setStatus("current")
_H3cIdleCut_Type = Integer32
_H3cIdleCut_Object = MibTableColumn
h3cIdleCut = _H3cIdleCut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 2),
    _H3cIdleCut_Type()
)
h3cIdleCut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIdleCut.setStatus("current")
_H3cIPAddress_Type = IpAddress
_H3cIPAddress_Object = MibTableColumn
h3cIPAddress = _H3cIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 3),
    _H3cIPAddress_Type()
)
h3cIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPAddress.setStatus("current")
_H3cNasIPAddress_Type = IpAddress
_H3cNasIPAddress_Object = MibTableColumn
h3cNasIPAddress = _H3cNasIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 4),
    _H3cNasIPAddress_Type()
)
h3cNasIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNasIPAddress.setStatus("current")
_H3cSlotNum_Type = Integer32
_H3cSlotNum_Object = MibTableColumn
h3cSlotNum = _H3cSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 5),
    _H3cSlotNum_Type()
)
h3cSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSlotNum.setStatus("current")
_H3cSubSlotNum_Type = Integer32
_H3cSubSlotNum_Object = MibTableColumn
h3cSubSlotNum = _H3cSubSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 6),
    _H3cSubSlotNum_Type()
)
h3cSubSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSubSlotNum.setStatus("current")
_H3cPortNum_Type = Integer32
_H3cPortNum_Object = MibTableColumn
h3cPortNum = _H3cPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 7),
    _H3cPortNum_Type()
)
h3cPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPortNum.setStatus("current")
_H3cMacAddress_Type = MacAddress
_H3cMacAddress_Object = MibTableColumn
h3cMacAddress = _H3cMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 8),
    _H3cMacAddress_Type()
)
h3cMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMacAddress.setStatus("current")


class _H3cVlan_Type(Integer32):
    """Custom type h3cVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cVlan_Type.__name__ = "Integer32"
_H3cVlan_Object = MibTableColumn
h3cVlan = _H3cVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 9),
    _H3cVlan_Type()
)
h3cVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVlan.setStatus("current")
_H3cFtpService_Type = ServiceType
_H3cFtpService_Object = MibTableColumn
h3cFtpService = _H3cFtpService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 10),
    _H3cFtpService_Type()
)
h3cFtpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFtpService.setStatus("current")
_H3cFtpDirectory_Type = OctetString
_H3cFtpDirectory_Object = MibTableColumn
h3cFtpDirectory = _H3cFtpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 11),
    _H3cFtpDirectory_Type()
)
h3cFtpDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFtpDirectory.setStatus("current")
_H3cLanAccessService_Type = ServiceType
_H3cLanAccessService_Object = MibTableColumn
h3cLanAccessService = _H3cLanAccessService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 12),
    _H3cLanAccessService_Type()
)
h3cLanAccessService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLanAccessService.setStatus("current")
_H3cSshService_Type = ServiceType
_H3cSshService_Object = MibTableColumn
h3cSshService = _H3cSshService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 13),
    _H3cSshService_Type()
)
h3cSshService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSshService.setStatus("current")
_H3cTelnetService_Type = ServiceType
_H3cTelnetService_Object = MibTableColumn
h3cTelnetService = _H3cTelnetService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 14),
    _H3cTelnetService_Type()
)
h3cTelnetService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTelnetService.setStatus("current")
_H3cTerminalService_Type = ServiceType
_H3cTerminalService_Object = MibTableColumn
h3cTerminalService = _H3cTerminalService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 15),
    _H3cTerminalService_Type()
)
h3cTerminalService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTerminalService.setStatus("current")


class _H3cExpirationDate_Type(DateAndTime):
    """Custom type h3cExpirationDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_H3cExpirationDate_Type.__name__ = "DateAndTime"
_H3cExpirationDate_Object = MibTableColumn
h3cExpirationDate = _H3cExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 16),
    _H3cExpirationDate_Type()
)
h3cExpirationDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cExpirationDate.setStatus("current")
_H3cUserGroup_Type = DisplayString
_H3cUserGroup_Object = MibTableColumn
h3cUserGroup = _H3cUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 17),
    _H3cUserGroup_Type()
)
h3cUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cUserGroup.setStatus("current")
_H3cPortalService_Type = ServiceType
_H3cPortalService_Object = MibTableColumn
h3cPortalService = _H3cPortalService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 18),
    _H3cPortalService_Type()
)
h3cPortalService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPortalService.setStatus("current")
_H3cPPPService_Type = ServiceType
_H3cPPPService_Object = MibTableColumn
h3cPPPService = _H3cPPPService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 19),
    _H3cPPPService_Type()
)
h3cPPPService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPPPService.setStatus("current")
_H3cHttpService_Type = ServiceType
_H3cHttpService_Object = MibTableColumn
h3cHttpService = _H3cHttpService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 20),
    _H3cHttpService_Type()
)
h3cHttpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHttpService.setStatus("current")
_H3cHttpsService_Type = ServiceType
_H3cHttpsService_Object = MibTableColumn
h3cHttpsService = _H3cHttpsService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 2, 1, 21),
    _H3cHttpsService_Type()
)
h3cHttpsService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHttpsService.setStatus("current")
_H3cUserMaxNum_Type = Integer32
_H3cUserMaxNum_Object = MibScalar
h3cUserMaxNum = _H3cUserMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 3),
    _H3cUserMaxNum_Type()
)
h3cUserMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUserMaxNum.setStatus("current")
_H3cUserCurrNum_Type = Integer32
_H3cUserCurrNum_Object = MibScalar
h3cUserCurrNum = _H3cUserCurrNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 4),
    _H3cUserCurrNum_Type()
)
h3cUserCurrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUserCurrNum.setStatus("current")
_H3cUserIndexIndicator_Type = Integer32
_H3cUserIndexIndicator_Object = MibScalar
h3cUserIndexIndicator = _H3cUserIndexIndicator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 5),
    _H3cUserIndexIndicator_Type()
)
h3cUserIndexIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUserIndexIndicator.setStatus("current")
_H3cUserRoleTable_Object = MibTable
h3cUserRoleTable = _H3cUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 6)
)
if mibBuilder.loadTexts:
    h3cUserRoleTable.setStatus("current")
_H3cUserRoleEntry_Object = MibTableRow
h3cUserRoleEntry = _H3cUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 6, 1)
)
h3cUserRoleEntry.setIndexNames(
    (0, "H3C-USER-MIB", "h3cUserIndex"),
    (0, "H3C-USER-MIB", "h3cUserRole"),
)
if mibBuilder.loadTexts:
    h3cUserRoleEntry.setStatus("current")


class _H3cUserRole_Type(DisplayString):
    """Custom type h3cUserRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cUserRole_Type.__name__ = "DisplayString"
_H3cUserRole_Object = MibTableColumn
h3cUserRole = _H3cUserRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 6, 1, 1),
    _H3cUserRole_Type()
)
h3cUserRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cUserRole.setStatus("current")
_H3cUserRoleStatus_Type = RowStatus
_H3cUserRoleStatus_Object = MibTableColumn
h3cUserRoleStatus = _H3cUserRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 1, 6, 1, 2),
    _H3cUserRoleStatus_Type()
)
h3cUserRoleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cUserRoleStatus.setStatus("current")
_H3cUserGroupObjects_ObjectIdentity = ObjectIdentity
h3cUserGroupObjects = _H3cUserGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2)
)
_H3cUserGroupInfoTable_Object = MibTable
h3cUserGroupInfoTable = _H3cUserGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    h3cUserGroupInfoTable.setStatus("current")
_H3cUserGroupInfoEntry_Object = MibTableRow
h3cUserGroupInfoEntry = _H3cUserGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2, 1, 1)
)
h3cUserGroupInfoEntry.setIndexNames(
    (0, "H3C-USER-MIB", "h3cUserGroupName"),
)
if mibBuilder.loadTexts:
    h3cUserGroupInfoEntry.setStatus("current")


class _H3cUserGroupName_Type(DisplayString):
    """Custom type h3cUserGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_H3cUserGroupName_Type.__name__ = "DisplayString"
_H3cUserGroupName_Object = MibTableColumn
h3cUserGroupName = _H3cUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2, 1, 1, 1),
    _H3cUserGroupName_Type()
)
h3cUserGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cUserGroupName.setStatus("current")
_H3cUserGroupInfoRowStatus_Type = RowStatus
_H3cUserGroupInfoRowStatus_Object = MibTableColumn
h3cUserGroupInfoRowStatus = _H3cUserGroupInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 12, 2, 1, 1, 2),
    _H3cUserGroupInfoRowStatus_Type()
)
h3cUserGroupInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cUserGroupInfoRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-USER-MIB",
    **{"DisplayString": DisplayString,
       "ServiceType": ServiceType,
       "h3cUser": h3cUser,
       "h3cUserObjects": h3cUserObjects,
       "h3cUserInfoTable": h3cUserInfoTable,
       "h3cUserInfoEntry": h3cUserInfoEntry,
       "h3cUserName": h3cUserName,
       "h3cUserPassword": h3cUserPassword,
       "h3cAuthMode": h3cAuthMode,
       "h3cUserLevel": h3cUserLevel,
       "h3cUserState": h3cUserState,
       "h3cUserInfoRowStatus": h3cUserInfoRowStatus,
       "h3cUserIndex": h3cUserIndex,
       "h3cUserAttributeTable": h3cUserAttributeTable,
       "h3cUserAttributeEntry": h3cUserAttributeEntry,
       "h3cAccessLimit": h3cAccessLimit,
       "h3cIdleCut": h3cIdleCut,
       "h3cIPAddress": h3cIPAddress,
       "h3cNasIPAddress": h3cNasIPAddress,
       "h3cSlotNum": h3cSlotNum,
       "h3cSubSlotNum": h3cSubSlotNum,
       "h3cPortNum": h3cPortNum,
       "h3cMacAddress": h3cMacAddress,
       "h3cVlan": h3cVlan,
       "h3cFtpService": h3cFtpService,
       "h3cFtpDirectory": h3cFtpDirectory,
       "h3cLanAccessService": h3cLanAccessService,
       "h3cSshService": h3cSshService,
       "h3cTelnetService": h3cTelnetService,
       "h3cTerminalService": h3cTerminalService,
       "h3cExpirationDate": h3cExpirationDate,
       "h3cUserGroup": h3cUserGroup,
       "h3cPortalService": h3cPortalService,
       "h3cPPPService": h3cPPPService,
       "h3cHttpService": h3cHttpService,
       "h3cHttpsService": h3cHttpsService,
       "h3cUserMaxNum": h3cUserMaxNum,
       "h3cUserCurrNum": h3cUserCurrNum,
       "h3cUserIndexIndicator": h3cUserIndexIndicator,
       "h3cUserRoleTable": h3cUserRoleTable,
       "h3cUserRoleEntry": h3cUserRoleEntry,
       "h3cUserRole": h3cUserRole,
       "h3cUserRoleStatus": h3cUserRoleStatus,
       "h3cUserGroupObjects": h3cUserGroupObjects,
       "h3cUserGroupInfoTable": h3cUserGroupInfoTable,
       "h3cUserGroupInfoEntry": h3cUserGroupInfoEntry,
       "h3cUserGroupName": h3cUserGroupName,
       "h3cUserGroupInfoRowStatus": h3cUserGroupInfoRowStatus}
)
