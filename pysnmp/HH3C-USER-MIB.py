# SNMP MIB module (HH3C-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-USER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:12 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cUser = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12)
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

_Hh3cUserObjects_ObjectIdentity = ObjectIdentity
hh3cUserObjects = _Hh3cUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1)
)
_Hh3cUserInfoTable_Object = MibTable
hh3cUserInfoTable = _Hh3cUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cUserInfoTable.setStatus("current")
_Hh3cUserInfoEntry_Object = MibTableRow
hh3cUserInfoEntry = _Hh3cUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1)
)
hh3cUserInfoEntry.setIndexNames(
    (0, "HH3C-USER-MIB", "hh3cUserIndex"),
)
if mibBuilder.loadTexts:
    hh3cUserInfoEntry.setStatus("current")
_Hh3cUserName_Type = DisplayString
_Hh3cUserName_Object = MibTableColumn
hh3cUserName = _Hh3cUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 1),
    _Hh3cUserName_Type()
)
hh3cUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cUserName.setStatus("current")
_Hh3cUserPassword_Type = DisplayString
_Hh3cUserPassword_Object = MibTableColumn
hh3cUserPassword = _Hh3cUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 2),
    _Hh3cUserPassword_Type()
)
hh3cUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cUserPassword.setStatus("current")
_Hh3cAuthMode_Type = Integer32
_Hh3cAuthMode_Object = MibTableColumn
hh3cAuthMode = _Hh3cAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 3),
    _Hh3cAuthMode_Type()
)
hh3cAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAuthMode.setStatus("current")
_Hh3cUserLevel_Type = Integer32
_Hh3cUserLevel_Object = MibTableColumn
hh3cUserLevel = _Hh3cUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 4),
    _Hh3cUserLevel_Type()
)
hh3cUserLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cUserLevel.setStatus("current")


class _Hh3cUserState_Type(Integer32):
    """Custom type hh3cUserState based on Integer32"""
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


_Hh3cUserState_Type.__name__ = "Integer32"
_Hh3cUserState_Object = MibTableColumn
hh3cUserState = _Hh3cUserState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 5),
    _Hh3cUserState_Type()
)
hh3cUserState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cUserState.setStatus("current")
_Hh3cUserInfoRowStatus_Type = RowStatus
_Hh3cUserInfoRowStatus_Object = MibTableColumn
hh3cUserInfoRowStatus = _Hh3cUserInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 6),
    _Hh3cUserInfoRowStatus_Type()
)
hh3cUserInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cUserInfoRowStatus.setStatus("current")
_Hh3cUserIndex_Type = Integer32
_Hh3cUserIndex_Object = MibTableColumn
hh3cUserIndex = _Hh3cUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 7),
    _Hh3cUserIndex_Type()
)
hh3cUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cUserIndex.setStatus("current")
_Hh3cUserAttributeTable_Object = MibTable
hh3cUserAttributeTable = _Hh3cUserAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cUserAttributeTable.setStatus("current")
_Hh3cUserAttributeEntry_Object = MibTableRow
hh3cUserAttributeEntry = _Hh3cUserAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1)
)
hh3cUserAttributeEntry.setIndexNames(
    (0, "HH3C-USER-MIB", "hh3cUserIndex"),
)
if mibBuilder.loadTexts:
    hh3cUserAttributeEntry.setStatus("current")
_Hh3cAccessLimit_Type = Integer32
_Hh3cAccessLimit_Object = MibTableColumn
hh3cAccessLimit = _Hh3cAccessLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 1),
    _Hh3cAccessLimit_Type()
)
hh3cAccessLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAccessLimit.setStatus("current")
_Hh3cIdleCut_Type = Integer32
_Hh3cIdleCut_Object = MibTableColumn
hh3cIdleCut = _Hh3cIdleCut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 2),
    _Hh3cIdleCut_Type()
)
hh3cIdleCut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIdleCut.setStatus("current")
_Hh3cIPAddress_Type = IpAddress
_Hh3cIPAddress_Object = MibTableColumn
hh3cIPAddress = _Hh3cIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 3),
    _Hh3cIPAddress_Type()
)
hh3cIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIPAddress.setStatus("current")
_Hh3cNasIPAddress_Type = IpAddress
_Hh3cNasIPAddress_Object = MibTableColumn
hh3cNasIPAddress = _Hh3cNasIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 4),
    _Hh3cNasIPAddress_Type()
)
hh3cNasIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNasIPAddress.setStatus("current")
_Hh3cSlotNum_Type = Integer32
_Hh3cSlotNum_Object = MibTableColumn
hh3cSlotNum = _Hh3cSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 5),
    _Hh3cSlotNum_Type()
)
hh3cSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSlotNum.setStatus("current")
_Hh3cSubSlotNum_Type = Integer32
_Hh3cSubSlotNum_Object = MibTableColumn
hh3cSubSlotNum = _Hh3cSubSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 6),
    _Hh3cSubSlotNum_Type()
)
hh3cSubSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSubSlotNum.setStatus("current")
_Hh3cPortNum_Type = Integer32
_Hh3cPortNum_Object = MibTableColumn
hh3cPortNum = _Hh3cPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 7),
    _Hh3cPortNum_Type()
)
hh3cPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortNum.setStatus("current")
_Hh3cMacAddress_Type = MacAddress
_Hh3cMacAddress_Object = MibTableColumn
hh3cMacAddress = _Hh3cMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 8),
    _Hh3cMacAddress_Type()
)
hh3cMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMacAddress.setStatus("current")


class _Hh3cVlan_Type(Integer32):
    """Custom type hh3cVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cVlan_Type.__name__ = "Integer32"
_Hh3cVlan_Object = MibTableColumn
hh3cVlan = _Hh3cVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 9),
    _Hh3cVlan_Type()
)
hh3cVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVlan.setStatus("current")
_Hh3cFtpService_Type = ServiceType
_Hh3cFtpService_Object = MibTableColumn
hh3cFtpService = _Hh3cFtpService_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 10),
    _Hh3cFtpService_Type()
)
hh3cFtpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFtpService.setStatus("current")
_Hh3cFtpDirectory_Type = OctetString
_Hh3cFtpDirectory_Object = MibTableColumn
hh3cFtpDirectory = _Hh3cFtpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 11),
    _Hh3cFtpDirectory_Type()
)
hh3cFtpDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFtpDirectory.setStatus("current")
_Hh3cLanAccessService_Type = ServiceType
_Hh3cLanAccessService_Object = MibTableColumn
hh3cLanAccessService = _Hh3cLanAccessService_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 12),
    _Hh3cLanAccessService_Type()
)
hh3cLanAccessService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLanAccessService.setStatus("current")
_Hh3cSshService_Type = ServiceType
_Hh3cSshService_Object = MibTableColumn
hh3cSshService = _Hh3cSshService_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 13),
    _Hh3cSshService_Type()
)
hh3cSshService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSshService.setStatus("current")
_Hh3cTelnetService_Type = ServiceType
_Hh3cTelnetService_Object = MibTableColumn
hh3cTelnetService = _Hh3cTelnetService_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 14),
    _Hh3cTelnetService_Type()
)
hh3cTelnetService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTelnetService.setStatus("current")
_Hh3cTerminalService_Type = ServiceType
_Hh3cTerminalService_Object = MibTableColumn
hh3cTerminalService = _Hh3cTerminalService_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 15),
    _Hh3cTerminalService_Type()
)
hh3cTerminalService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTerminalService.setStatus("current")


class _Hh3cExpirationDate_Type(DateAndTime):
    """Custom type hh3cExpirationDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hh3cExpirationDate_Type.__name__ = "DateAndTime"
_Hh3cExpirationDate_Object = MibTableColumn
hh3cExpirationDate = _Hh3cExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 16),
    _Hh3cExpirationDate_Type()
)
hh3cExpirationDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExpirationDate.setStatus("current")
_Hh3cUserGroup_Type = DisplayString
_Hh3cUserGroup_Object = MibTableColumn
hh3cUserGroup = _Hh3cUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 17),
    _Hh3cUserGroup_Type()
)
hh3cUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserGroup.setStatus("current")
_Hh3cPortalService_Type = ServiceType
_Hh3cPortalService_Object = MibTableColumn
hh3cPortalService = _Hh3cPortalService_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 18),
    _Hh3cPortalService_Type()
)
hh3cPortalService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalService.setStatus("current")
_Hh3cUserMaxNum_Type = Integer32
_Hh3cUserMaxNum_Object = MibScalar
hh3cUserMaxNum = _Hh3cUserMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 3),
    _Hh3cUserMaxNum_Type()
)
hh3cUserMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserMaxNum.setStatus("current")
_Hh3cUserCurrNum_Type = Integer32
_Hh3cUserCurrNum_Object = MibScalar
hh3cUserCurrNum = _Hh3cUserCurrNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 4),
    _Hh3cUserCurrNum_Type()
)
hh3cUserCurrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserCurrNum.setStatus("current")
_Hh3cUserIndexIndicator_Type = Integer32
_Hh3cUserIndexIndicator_Object = MibScalar
hh3cUserIndexIndicator = _Hh3cUserIndexIndicator_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 5),
    _Hh3cUserIndexIndicator_Type()
)
hh3cUserIndexIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserIndexIndicator.setStatus("current")
_Hh3cUserGroupObjects_ObjectIdentity = ObjectIdentity
hh3cUserGroupObjects = _Hh3cUserGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 2)
)
_Hh3cUserGroupInfoTable_Object = MibTable
hh3cUserGroupInfoTable = _Hh3cUserGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cUserGroupInfoTable.setStatus("current")
_Hh3cUserGroupInfoEntry_Object = MibTableRow
hh3cUserGroupInfoEntry = _Hh3cUserGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 2, 1, 1)
)
hh3cUserGroupInfoEntry.setIndexNames(
    (0, "HH3C-USER-MIB", "hh3cUserGroupName"),
)
if mibBuilder.loadTexts:
    hh3cUserGroupInfoEntry.setStatus("current")


class _Hh3cUserGroupName_Type(DisplayString):
    """Custom type hh3cUserGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Hh3cUserGroupName_Type.__name__ = "DisplayString"
_Hh3cUserGroupName_Object = MibTableColumn
hh3cUserGroupName = _Hh3cUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 2, 1, 1, 1),
    _Hh3cUserGroupName_Type()
)
hh3cUserGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cUserGroupName.setStatus("current")
_Hh3cUserGroupInfoRowStatus_Type = RowStatus
_Hh3cUserGroupInfoRowStatus_Object = MibTableColumn
hh3cUserGroupInfoRowStatus = _Hh3cUserGroupInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12, 2, 1, 1, 2),
    _Hh3cUserGroupInfoRowStatus_Type()
)
hh3cUserGroupInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cUserGroupInfoRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-USER-MIB",
    **{"DisplayString": DisplayString,
       "ServiceType": ServiceType,
       "hh3cUser": hh3cUser,
       "hh3cUserObjects": hh3cUserObjects,
       "hh3cUserInfoTable": hh3cUserInfoTable,
       "hh3cUserInfoEntry": hh3cUserInfoEntry,
       "hh3cUserName": hh3cUserName,
       "hh3cUserPassword": hh3cUserPassword,
       "hh3cAuthMode": hh3cAuthMode,
       "hh3cUserLevel": hh3cUserLevel,
       "hh3cUserState": hh3cUserState,
       "hh3cUserInfoRowStatus": hh3cUserInfoRowStatus,
       "hh3cUserIndex": hh3cUserIndex,
       "hh3cUserAttributeTable": hh3cUserAttributeTable,
       "hh3cUserAttributeEntry": hh3cUserAttributeEntry,
       "hh3cAccessLimit": hh3cAccessLimit,
       "hh3cIdleCut": hh3cIdleCut,
       "hh3cIPAddress": hh3cIPAddress,
       "hh3cNasIPAddress": hh3cNasIPAddress,
       "hh3cSlotNum": hh3cSlotNum,
       "hh3cSubSlotNum": hh3cSubSlotNum,
       "hh3cPortNum": hh3cPortNum,
       "hh3cMacAddress": hh3cMacAddress,
       "hh3cVlan": hh3cVlan,
       "hh3cFtpService": hh3cFtpService,
       "hh3cFtpDirectory": hh3cFtpDirectory,
       "hh3cLanAccessService": hh3cLanAccessService,
       "hh3cSshService": hh3cSshService,
       "hh3cTelnetService": hh3cTelnetService,
       "hh3cTerminalService": hh3cTerminalService,
       "hh3cExpirationDate": hh3cExpirationDate,
       "hh3cUserGroup": hh3cUserGroup,
       "hh3cPortalService": hh3cPortalService,
       "hh3cUserMaxNum": hh3cUserMaxNum,
       "hh3cUserCurrNum": hh3cUserCurrNum,
       "hh3cUserIndexIndicator": hh3cUserIndexIndicator,
       "hh3cUserGroupObjects": hh3cUserGroupObjects,
       "hh3cUserGroupInfoTable": hh3cUserGroupInfoTable,
       "hh3cUserGroupInfoEntry": hh3cUserGroupInfoEntry,
       "hh3cUserGroupName": hh3cUserGroupName,
       "hh3cUserGroupInfoRowStatus": hh3cUserGroupInfoRowStatus}
)
