# SNMP MIB module (HPN-ICF-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-USER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:06 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfUser = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12)
)


# Types definitions


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

_HpnicfUserObjects_ObjectIdentity = ObjectIdentity
hpnicfUserObjects = _HpnicfUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1)
)
_HpnicfUserInfoTable_Object = MibTable
hpnicfUserInfoTable = _HpnicfUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfUserInfoTable.setStatus("current")
_HpnicfUserInfoEntry_Object = MibTableRow
hpnicfUserInfoEntry = _HpnicfUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1)
)
hpnicfUserInfoEntry.setIndexNames(
    (0, "HPN-ICF-USER-MIB", "hpnicfUserIndex"),
)
if mibBuilder.loadTexts:
    hpnicfUserInfoEntry.setStatus("current")
_HpnicfUserName_Type = DisplayString
_HpnicfUserName_Object = MibTableColumn
hpnicfUserName = _HpnicfUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 1),
    _HpnicfUserName_Type()
)
hpnicfUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfUserName.setStatus("current")
_HpnicfUserPassword_Type = DisplayString
_HpnicfUserPassword_Object = MibTableColumn
hpnicfUserPassword = _HpnicfUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 2),
    _HpnicfUserPassword_Type()
)
hpnicfUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfUserPassword.setStatus("current")
_HpnicfAuthMode_Type = Integer32
_HpnicfAuthMode_Object = MibTableColumn
hpnicfAuthMode = _HpnicfAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 3),
    _HpnicfAuthMode_Type()
)
hpnicfAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAuthMode.setStatus("current")
_HpnicfUserLevel_Type = Integer32
_HpnicfUserLevel_Object = MibTableColumn
hpnicfUserLevel = _HpnicfUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 4),
    _HpnicfUserLevel_Type()
)
hpnicfUserLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfUserLevel.setStatus("current")


class _HpnicfUserState_Type(Integer32):
    """Custom type hpnicfUserState based on Integer32"""
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


_HpnicfUserState_Type.__name__ = "Integer32"
_HpnicfUserState_Object = MibTableColumn
hpnicfUserState = _HpnicfUserState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 5),
    _HpnicfUserState_Type()
)
hpnicfUserState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfUserState.setStatus("current")
_HpnicfUserInfoRowStatus_Type = RowStatus
_HpnicfUserInfoRowStatus_Object = MibTableColumn
hpnicfUserInfoRowStatus = _HpnicfUserInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 6),
    _HpnicfUserInfoRowStatus_Type()
)
hpnicfUserInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfUserInfoRowStatus.setStatus("current")


class _HpnicfUserIndex_Type(Integer32):
    """Custom type hpnicfUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483646),
    )


_HpnicfUserIndex_Type.__name__ = "Integer32"
_HpnicfUserIndex_Object = MibTableColumn
hpnicfUserIndex = _HpnicfUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 1, 1, 7),
    _HpnicfUserIndex_Type()
)
hpnicfUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfUserIndex.setStatus("current")
_HpnicfUserAttributeTable_Object = MibTable
hpnicfUserAttributeTable = _HpnicfUserAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfUserAttributeTable.setStatus("current")
_HpnicfUserAttributeEntry_Object = MibTableRow
hpnicfUserAttributeEntry = _HpnicfUserAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1)
)
hpnicfUserAttributeEntry.setIndexNames(
    (0, "HPN-ICF-USER-MIB", "hpnicfUserIndex"),
)
if mibBuilder.loadTexts:
    hpnicfUserAttributeEntry.setStatus("current")
_HpnicfAccessLimit_Type = Integer32
_HpnicfAccessLimit_Object = MibTableColumn
hpnicfAccessLimit = _HpnicfAccessLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 1),
    _HpnicfAccessLimit_Type()
)
hpnicfAccessLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAccessLimit.setStatus("current")
_HpnicfIdleCut_Type = Integer32
_HpnicfIdleCut_Object = MibTableColumn
hpnicfIdleCut = _HpnicfIdleCut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 2),
    _HpnicfIdleCut_Type()
)
hpnicfIdleCut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIdleCut.setStatus("current")
_HpnicfIPAddress_Type = IpAddress
_HpnicfIPAddress_Object = MibTableColumn
hpnicfIPAddress = _HpnicfIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 3),
    _HpnicfIPAddress_Type()
)
hpnicfIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIPAddress.setStatus("current")
_HpnicfNasIPAddress_Type = IpAddress
_HpnicfNasIPAddress_Object = MibTableColumn
hpnicfNasIPAddress = _HpnicfNasIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 4),
    _HpnicfNasIPAddress_Type()
)
hpnicfNasIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNasIPAddress.setStatus("current")
_HpnicfSlotNum_Type = Integer32
_HpnicfSlotNum_Object = MibTableColumn
hpnicfSlotNum = _HpnicfSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 5),
    _HpnicfSlotNum_Type()
)
hpnicfSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSlotNum.setStatus("current")
_HpnicfSubSlotNum_Type = Integer32
_HpnicfSubSlotNum_Object = MibTableColumn
hpnicfSubSlotNum = _HpnicfSubSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 6),
    _HpnicfSubSlotNum_Type()
)
hpnicfSubSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSubSlotNum.setStatus("current")
_HpnicfPortNum_Type = Integer32
_HpnicfPortNum_Object = MibTableColumn
hpnicfPortNum = _HpnicfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 7),
    _HpnicfPortNum_Type()
)
hpnicfPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortNum.setStatus("current")
_HpnicfMacAddress_Type = MacAddress
_HpnicfMacAddress_Object = MibTableColumn
hpnicfMacAddress = _HpnicfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 8),
    _HpnicfMacAddress_Type()
)
hpnicfMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMacAddress.setStatus("current")


class _HpnicfVlan_Type(Integer32):
    """Custom type hpnicfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfVlan_Type.__name__ = "Integer32"
_HpnicfVlan_Object = MibTableColumn
hpnicfVlan = _HpnicfVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 9),
    _HpnicfVlan_Type()
)
hpnicfVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVlan.setStatus("current")
_HpnicfFtpService_Type = ServiceType
_HpnicfFtpService_Object = MibTableColumn
hpnicfFtpService = _HpnicfFtpService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 10),
    _HpnicfFtpService_Type()
)
hpnicfFtpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFtpService.setStatus("current")
_HpnicfFtpDirectory_Type = OctetString
_HpnicfFtpDirectory_Object = MibTableColumn
hpnicfFtpDirectory = _HpnicfFtpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 11),
    _HpnicfFtpDirectory_Type()
)
hpnicfFtpDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFtpDirectory.setStatus("current")
_HpnicfLanAccessService_Type = ServiceType
_HpnicfLanAccessService_Object = MibTableColumn
hpnicfLanAccessService = _HpnicfLanAccessService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 12),
    _HpnicfLanAccessService_Type()
)
hpnicfLanAccessService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLanAccessService.setStatus("current")
_HpnicfSshService_Type = ServiceType
_HpnicfSshService_Object = MibTableColumn
hpnicfSshService = _HpnicfSshService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 13),
    _HpnicfSshService_Type()
)
hpnicfSshService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSshService.setStatus("current")
_HpnicfTelnetService_Type = ServiceType
_HpnicfTelnetService_Object = MibTableColumn
hpnicfTelnetService = _HpnicfTelnetService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 14),
    _HpnicfTelnetService_Type()
)
hpnicfTelnetService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTelnetService.setStatus("current")
_HpnicfTerminalService_Type = ServiceType
_HpnicfTerminalService_Object = MibTableColumn
hpnicfTerminalService = _HpnicfTerminalService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 15),
    _HpnicfTerminalService_Type()
)
hpnicfTerminalService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTerminalService.setStatus("current")


class _HpnicfExpirationDate_Type(DateAndTime):
    """Custom type hpnicfExpirationDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpnicfExpirationDate_Type.__name__ = "DateAndTime"
_HpnicfExpirationDate_Object = MibTableColumn
hpnicfExpirationDate = _HpnicfExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 16),
    _HpnicfExpirationDate_Type()
)
hpnicfExpirationDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfExpirationDate.setStatus("current")
_HpnicfUserGroup_Type = DisplayString
_HpnicfUserGroup_Object = MibTableColumn
hpnicfUserGroup = _HpnicfUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 17),
    _HpnicfUserGroup_Type()
)
hpnicfUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserGroup.setStatus("current")
_HpnicfPortalService_Type = ServiceType
_HpnicfPortalService_Object = MibTableColumn
hpnicfPortalService = _HpnicfPortalService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 18),
    _HpnicfPortalService_Type()
)
hpnicfPortalService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortalService.setStatus("current")
_HpnicfPPPService_Type = ServiceType
_HpnicfPPPService_Object = MibTableColumn
hpnicfPPPService = _HpnicfPPPService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 19),
    _HpnicfPPPService_Type()
)
hpnicfPPPService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPPPService.setStatus("current")
_HpnicfHttpService_Type = ServiceType
_HpnicfHttpService_Object = MibTableColumn
hpnicfHttpService = _HpnicfHttpService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 20),
    _HpnicfHttpService_Type()
)
hpnicfHttpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfHttpService.setStatus("current")
_HpnicfHttpsService_Type = ServiceType
_HpnicfHttpsService_Object = MibTableColumn
hpnicfHttpsService = _HpnicfHttpsService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 21),
    _HpnicfHttpsService_Type()
)
hpnicfHttpsService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfHttpsService.setStatus("current")
_HpnicfUserIfIndex_Type = Integer32
_HpnicfUserIfIndex_Object = MibTableColumn
hpnicfUserIfIndex = _HpnicfUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 2, 1, 22),
    _HpnicfUserIfIndex_Type()
)
hpnicfUserIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserIfIndex.setStatus("current")
_HpnicfUserMaxNum_Type = Integer32
_HpnicfUserMaxNum_Object = MibScalar
hpnicfUserMaxNum = _HpnicfUserMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 3),
    _HpnicfUserMaxNum_Type()
)
hpnicfUserMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserMaxNum.setStatus("current")
_HpnicfUserCurrNum_Type = Integer32
_HpnicfUserCurrNum_Object = MibScalar
hpnicfUserCurrNum = _HpnicfUserCurrNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 4),
    _HpnicfUserCurrNum_Type()
)
hpnicfUserCurrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserCurrNum.setStatus("current")
_HpnicfUserIndexIndicator_Type = Integer32
_HpnicfUserIndexIndicator_Object = MibScalar
hpnicfUserIndexIndicator = _HpnicfUserIndexIndicator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 5),
    _HpnicfUserIndexIndicator_Type()
)
hpnicfUserIndexIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserIndexIndicator.setStatus("current")
_HpnicfUserRoleTable_Object = MibTable
hpnicfUserRoleTable = _HpnicfUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfUserRoleTable.setStatus("current")
_HpnicfUserRoleEntry_Object = MibTableRow
hpnicfUserRoleEntry = _HpnicfUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 6, 1)
)
hpnicfUserRoleEntry.setIndexNames(
    (0, "HPN-ICF-USER-MIB", "hpnicfUserIndex"),
    (0, "HPN-ICF-USER-MIB", "hpnicfUserRole"),
)
if mibBuilder.loadTexts:
    hpnicfUserRoleEntry.setStatus("current")


class _HpnicfUserRole_Type(DisplayString):
    """Custom type hpnicfUserRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfUserRole_Type.__name__ = "DisplayString"
_HpnicfUserRole_Object = MibTableColumn
hpnicfUserRole = _HpnicfUserRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 6, 1, 1),
    _HpnicfUserRole_Type()
)
hpnicfUserRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfUserRole.setStatus("current")
_HpnicfUserRoleStatus_Type = RowStatus
_HpnicfUserRoleStatus_Object = MibTableColumn
hpnicfUserRoleStatus = _HpnicfUserRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 1, 6, 1, 2),
    _HpnicfUserRoleStatus_Type()
)
hpnicfUserRoleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfUserRoleStatus.setStatus("current")
_HpnicfUserGroupObjects_ObjectIdentity = ObjectIdentity
hpnicfUserGroupObjects = _HpnicfUserGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2)
)
_HpnicfUserGroupInfoTable_Object = MibTable
hpnicfUserGroupInfoTable = _HpnicfUserGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfUserGroupInfoTable.setStatus("current")
_HpnicfUserGroupInfoEntry_Object = MibTableRow
hpnicfUserGroupInfoEntry = _HpnicfUserGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2, 1, 1)
)
hpnicfUserGroupInfoEntry.setIndexNames(
    (0, "HPN-ICF-USER-MIB", "hpnicfUserGroupName"),
)
if mibBuilder.loadTexts:
    hpnicfUserGroupInfoEntry.setStatus("current")


class _HpnicfUserGroupName_Type(DisplayString):
    """Custom type hpnicfUserGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_HpnicfUserGroupName_Type.__name__ = "DisplayString"
_HpnicfUserGroupName_Object = MibTableColumn
hpnicfUserGroupName = _HpnicfUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2, 1, 1, 1),
    _HpnicfUserGroupName_Type()
)
hpnicfUserGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfUserGroupName.setStatus("current")
_HpnicfUserGroupInfoRowStatus_Type = RowStatus
_HpnicfUserGroupInfoRowStatus_Object = MibTableColumn
hpnicfUserGroupInfoRowStatus = _HpnicfUserGroupInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12, 2, 1, 1, 2),
    _HpnicfUserGroupInfoRowStatus_Type()
)
hpnicfUserGroupInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfUserGroupInfoRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-USER-MIB",
    **{"ServiceType": ServiceType,
       "hpnicfUser": hpnicfUser,
       "hpnicfUserObjects": hpnicfUserObjects,
       "hpnicfUserInfoTable": hpnicfUserInfoTable,
       "hpnicfUserInfoEntry": hpnicfUserInfoEntry,
       "hpnicfUserName": hpnicfUserName,
       "hpnicfUserPassword": hpnicfUserPassword,
       "hpnicfAuthMode": hpnicfAuthMode,
       "hpnicfUserLevel": hpnicfUserLevel,
       "hpnicfUserState": hpnicfUserState,
       "hpnicfUserInfoRowStatus": hpnicfUserInfoRowStatus,
       "hpnicfUserIndex": hpnicfUserIndex,
       "hpnicfUserAttributeTable": hpnicfUserAttributeTable,
       "hpnicfUserAttributeEntry": hpnicfUserAttributeEntry,
       "hpnicfAccessLimit": hpnicfAccessLimit,
       "hpnicfIdleCut": hpnicfIdleCut,
       "hpnicfIPAddress": hpnicfIPAddress,
       "hpnicfNasIPAddress": hpnicfNasIPAddress,
       "hpnicfSlotNum": hpnicfSlotNum,
       "hpnicfSubSlotNum": hpnicfSubSlotNum,
       "hpnicfPortNum": hpnicfPortNum,
       "hpnicfMacAddress": hpnicfMacAddress,
       "hpnicfVlan": hpnicfVlan,
       "hpnicfFtpService": hpnicfFtpService,
       "hpnicfFtpDirectory": hpnicfFtpDirectory,
       "hpnicfLanAccessService": hpnicfLanAccessService,
       "hpnicfSshService": hpnicfSshService,
       "hpnicfTelnetService": hpnicfTelnetService,
       "hpnicfTerminalService": hpnicfTerminalService,
       "hpnicfExpirationDate": hpnicfExpirationDate,
       "hpnicfUserGroup": hpnicfUserGroup,
       "hpnicfPortalService": hpnicfPortalService,
       "hpnicfPPPService": hpnicfPPPService,
       "hpnicfHttpService": hpnicfHttpService,
       "hpnicfHttpsService": hpnicfHttpsService,
       "hpnicfUserIfIndex": hpnicfUserIfIndex,
       "hpnicfUserMaxNum": hpnicfUserMaxNum,
       "hpnicfUserCurrNum": hpnicfUserCurrNum,
       "hpnicfUserIndexIndicator": hpnicfUserIndexIndicator,
       "hpnicfUserRoleTable": hpnicfUserRoleTable,
       "hpnicfUserRoleEntry": hpnicfUserRoleEntry,
       "hpnicfUserRole": hpnicfUserRole,
       "hpnicfUserRoleStatus": hpnicfUserRoleStatus,
       "hpnicfUserGroupObjects": hpnicfUserGroupObjects,
       "hpnicfUserGroupInfoTable": hpnicfUserGroupInfoTable,
       "hpnicfUserGroupInfoEntry": hpnicfUserGroupInfoEntry,
       "hpnicfUserGroupName": hpnicfUserGroupName,
       "hpnicfUserGroupInfoRowStatus": hpnicfUserGroupInfoRowStatus}
)
