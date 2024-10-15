# SNMP MIB module (COLUBRIS-PUBLIC-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-PUBLIC-ACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:21 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisNotificationEnable,
 ColubrisPriorityQueue,
 ColubrisProfileIndexOrZero,
 ColubrisSSIDOrNone,
 ColubrisSecurity,
 ColubrisUsersAuthenticationMode,
 ColubrisUsersAuthenticationType) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable",
    "ColubrisPriorityQueue",
    "ColubrisProfileIndexOrZero",
    "ColubrisSSIDOrNone",
    "ColubrisSecurity",
    "ColubrisUsersAuthenticationMode",
    "ColubrisUsersAuthenticationType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

colubrisPublicAccessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisPublicAccessMIBObjects_ObjectIdentity = ObjectIdentity
colubrisPublicAccessMIBObjects = _ColubrisPublicAccessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1)
)
_PublicAccessGroup_ObjectIdentity = ObjectIdentity
publicAccessGroup = _PublicAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 1)
)


class _PublicAccessStatus_Type(Integer32):
    """Custom type publicAccessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PublicAccessStatus_Type.__name__ = "Integer32"
_PublicAccessStatus_Object = MibScalar
publicAccessStatus = _PublicAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 1, 1),
    _PublicAccessStatus_Type()
)
publicAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessStatus.setStatus("current")


class _PublicAccessStatusChangedCause_Type(OctetString):
    """Custom type publicAccessStatusChangedCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_PublicAccessStatusChangedCause_Type.__name__ = "OctetString"
_PublicAccessStatusChangedCause_Object = MibScalar
publicAccessStatusChangedCause = _PublicAccessStatusChangedCause_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 1, 2),
    _PublicAccessStatusChangedCause_Type()
)
publicAccessStatusChangedCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessStatusChangedCause.setStatus("current")
_PublicAccessDeviceGroup_ObjectIdentity = ObjectIdentity
publicAccessDeviceGroup = _PublicAccessDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2)
)


class _PublicAccessDeviceUserName_Type(OctetString):
    """Custom type publicAccessDeviceUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_PublicAccessDeviceUserName_Type.__name__ = "OctetString"
_PublicAccessDeviceUserName_Object = MibScalar
publicAccessDeviceUserName = _PublicAccessDeviceUserName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 1),
    _PublicAccessDeviceUserName_Type()
)
publicAccessDeviceUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessDeviceUserName.setStatus("current")


class _PublicAccessDeviceUserPassword_Type(OctetString):
    """Custom type publicAccessDeviceUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 230),
    )


_PublicAccessDeviceUserPassword_Type.__name__ = "OctetString"
_PublicAccessDeviceUserPassword_Object = MibScalar
publicAccessDeviceUserPassword = _PublicAccessDeviceUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 2),
    _PublicAccessDeviceUserPassword_Type()
)
publicAccessDeviceUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessDeviceUserPassword.setStatus("current")


class _PublicAccessDeviceSessionTimeoutAdminStatus_Type(Unsigned32):
    """Custom type publicAccessDeviceSessionTimeoutAdminStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_PublicAccessDeviceSessionTimeoutAdminStatus_Type.__name__ = "Unsigned32"
_PublicAccessDeviceSessionTimeoutAdminStatus_Object = MibScalar
publicAccessDeviceSessionTimeoutAdminStatus = _PublicAccessDeviceSessionTimeoutAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 3),
    _PublicAccessDeviceSessionTimeoutAdminStatus_Type()
)
publicAccessDeviceSessionTimeoutAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessDeviceSessionTimeoutAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    publicAccessDeviceSessionTimeoutAdminStatus.setUnits("minutes")
_PublicAccessDeviceSessionTimeoutOperStatus_Type = Unsigned32
_PublicAccessDeviceSessionTimeoutOperStatus_Object = MibScalar
publicAccessDeviceSessionTimeoutOperStatus = _PublicAccessDeviceSessionTimeoutOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 4),
    _PublicAccessDeviceSessionTimeoutOperStatus_Type()
)
publicAccessDeviceSessionTimeoutOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessDeviceSessionTimeoutOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    publicAccessDeviceSessionTimeoutOperStatus.setUnits("seconds")
_PublicAccessDeviceConfigMode_Type = ColubrisUsersAuthenticationMode
_PublicAccessDeviceConfigMode_Object = MibScalar
publicAccessDeviceConfigMode = _PublicAccessDeviceConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 5),
    _PublicAccessDeviceConfigMode_Type()
)
publicAccessDeviceConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessDeviceConfigMode.setStatus("current")
_PublicAccessDeviceAuthenProfileIndex_Type = ColubrisProfileIndexOrZero
_PublicAccessDeviceAuthenProfileIndex_Object = MibScalar
publicAccessDeviceAuthenProfileIndex = _PublicAccessDeviceAuthenProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 6),
    _PublicAccessDeviceAuthenProfileIndex_Type()
)
publicAccessDeviceAuthenProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessDeviceAuthenProfileIndex.setStatus("current")


class _PublicAccessDeviceAccountingEnabled_Type(Integer32):
    """Custom type publicAccessDeviceAccountingEnabled based on Integer32"""
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


_PublicAccessDeviceAccountingEnabled_Type.__name__ = "Integer32"
_PublicAccessDeviceAccountingEnabled_Object = MibScalar
publicAccessDeviceAccountingEnabled = _PublicAccessDeviceAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 7),
    _PublicAccessDeviceAccountingEnabled_Type()
)
publicAccessDeviceAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessDeviceAccountingEnabled.setStatus("current")
_PublicAccessDeviceAccountingProfileIndex_Type = ColubrisProfileIndexOrZero
_PublicAccessDeviceAccountingProfileIndex_Object = MibScalar
publicAccessDeviceAccountingProfileIndex = _PublicAccessDeviceAccountingProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 8),
    _PublicAccessDeviceAccountingProfileIndex_Type()
)
publicAccessDeviceAccountingProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessDeviceAccountingProfileIndex.setStatus("current")


class _PublicAccessDeviceForceReconfiguration_Type(Integer32):
    """Custom type publicAccessDeviceForceReconfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forceReconfiguration", 1),
          ("idle", 0))
    )


_PublicAccessDeviceForceReconfiguration_Type.__name__ = "Integer32"
_PublicAccessDeviceForceReconfiguration_Object = MibScalar
publicAccessDeviceForceReconfiguration = _PublicAccessDeviceForceReconfiguration_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 9),
    _PublicAccessDeviceForceReconfiguration_Type()
)
publicAccessDeviceForceReconfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessDeviceForceReconfiguration.setStatus("current")
_PublicAccessUsersGroup_ObjectIdentity = ObjectIdentity
publicAccessUsersGroup = _PublicAccessUsersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3)
)
_PublicAccessUsersMaxCount_Type = Unsigned32
_PublicAccessUsersMaxCount_Object = MibScalar
publicAccessUsersMaxCount = _PublicAccessUsersMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 1),
    _PublicAccessUsersMaxCount_Type()
)
publicAccessUsersMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersMaxCount.setStatus("current")
_PublicAccessUsersCount_Type = Gauge32
_PublicAccessUsersCount_Object = MibScalar
publicAccessUsersCount = _PublicAccessUsersCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 2),
    _PublicAccessUsersCount_Type()
)
publicAccessUsersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersCount.setStatus("current")
_PublicAccessUsersThreshold_Type = Unsigned32
_PublicAccessUsersThreshold_Object = MibScalar
publicAccessUsersThreshold = _PublicAccessUsersThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 3),
    _PublicAccessUsersThreshold_Type()
)
publicAccessUsersThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessUsersThreshold.setStatus("current")


class _PublicAccessUsersSessionTrapEnabled_Type(ColubrisNotificationEnable):
    """Custom type publicAccessUsersSessionTrapEnabled based on ColubrisNotificationEnable"""


_PublicAccessUsersSessionTrapEnabled_Object = MibScalar
publicAccessUsersSessionTrapEnabled = _PublicAccessUsersSessionTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 4),
    _PublicAccessUsersSessionTrapEnabled_Type()
)
publicAccessUsersSessionTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessUsersSessionTrapEnabled.setStatus("current")
_PublicAccessUsersConfigTable_Object = MibTable
publicAccessUsersConfigTable = _PublicAccessUsersConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    publicAccessUsersConfigTable.setStatus("current")
_PublicAccessUsersConfigEntry_Object = MibTableRow
publicAccessUsersConfigEntry = _PublicAccessUsersConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1)
)
publicAccessUsersConfigEntry.setIndexNames(
    (0, "COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigIndex"),
)
if mibBuilder.loadTexts:
    publicAccessUsersConfigEntry.setStatus("current")


class _PublicAccessUsersConfigIndex_Type(Integer32):
    """Custom type publicAccessUsersConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PublicAccessUsersConfigIndex_Type.__name__ = "Integer32"
_PublicAccessUsersConfigIndex_Object = MibTableColumn
publicAccessUsersConfigIndex = _PublicAccessUsersConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 1),
    _PublicAccessUsersConfigIndex_Type()
)
publicAccessUsersConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    publicAccessUsersConfigIndex.setStatus("current")
_PublicAccessUsersConfigAuthenType_Type = ColubrisUsersAuthenticationType
_PublicAccessUsersConfigAuthenType_Object = MibTableColumn
publicAccessUsersConfigAuthenType = _PublicAccessUsersConfigAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 2),
    _PublicAccessUsersConfigAuthenType_Type()
)
publicAccessUsersConfigAuthenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersConfigAuthenType.setStatus("current")
_PublicAccessUsersConfigAuthenMode_Type = ColubrisUsersAuthenticationMode
_PublicAccessUsersConfigAuthenMode_Object = MibTableColumn
publicAccessUsersConfigAuthenMode = _PublicAccessUsersConfigAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 3),
    _PublicAccessUsersConfigAuthenMode_Type()
)
publicAccessUsersConfigAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersConfigAuthenMode.setStatus("current")
_PublicAccessUsersConfigAuthenProfileIndex_Type = ColubrisProfileIndexOrZero
_PublicAccessUsersConfigAuthenProfileIndex_Object = MibTableColumn
publicAccessUsersConfigAuthenProfileIndex = _PublicAccessUsersConfigAuthenProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 4),
    _PublicAccessUsersConfigAuthenProfileIndex_Type()
)
publicAccessUsersConfigAuthenProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersConfigAuthenProfileIndex.setStatus("current")


class _PublicAccessUsersConfigAuthenTimeout_Type(Unsigned32):
    """Custom type publicAccessUsersConfigAuthenTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PublicAccessUsersConfigAuthenTimeout_Type.__name__ = "Unsigned32"
_PublicAccessUsersConfigAuthenTimeout_Object = MibTableColumn
publicAccessUsersConfigAuthenTimeout = _PublicAccessUsersConfigAuthenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 5),
    _PublicAccessUsersConfigAuthenTimeout_Type()
)
publicAccessUsersConfigAuthenTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersConfigAuthenTimeout.setStatus("current")
if mibBuilder.loadTexts:
    publicAccessUsersConfigAuthenTimeout.setUnits("seconds")


class _PublicAccessUsersConfigAccountingEnabled_Type(Integer32):
    """Custom type publicAccessUsersConfigAccountingEnabled based on Integer32"""
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


_PublicAccessUsersConfigAccountingEnabled_Type.__name__ = "Integer32"
_PublicAccessUsersConfigAccountingEnabled_Object = MibTableColumn
publicAccessUsersConfigAccountingEnabled = _PublicAccessUsersConfigAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 6),
    _PublicAccessUsersConfigAccountingEnabled_Type()
)
publicAccessUsersConfigAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersConfigAccountingEnabled.setStatus("current")
_PublicAccessUsersConfigAccountingProfileIndex_Type = ColubrisProfileIndexOrZero
_PublicAccessUsersConfigAccountingProfileIndex_Object = MibTableColumn
publicAccessUsersConfigAccountingProfileIndex = _PublicAccessUsersConfigAccountingProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 7),
    _PublicAccessUsersConfigAccountingProfileIndex_Type()
)
publicAccessUsersConfigAccountingProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersConfigAccountingProfileIndex.setStatus("current")
_PublicAccessUsersConfigInterfaceIndex_Type = InterfaceIndex
_PublicAccessUsersConfigInterfaceIndex_Object = MibTableColumn
publicAccessUsersConfigInterfaceIndex = _PublicAccessUsersConfigInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 8),
    _PublicAccessUsersConfigInterfaceIndex_Type()
)
publicAccessUsersConfigInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersConfigInterfaceIndex.setStatus("current")


class _PublicAccessUsersConfigVirtualApProfileIndex_Type(Integer32):
    """Custom type publicAccessUsersConfigVirtualApProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PublicAccessUsersConfigVirtualApProfileIndex_Type.__name__ = "Integer32"
_PublicAccessUsersConfigVirtualApProfileIndex_Object = MibTableColumn
publicAccessUsersConfigVirtualApProfileIndex = _PublicAccessUsersConfigVirtualApProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 9),
    _PublicAccessUsersConfigVirtualApProfileIndex_Type()
)
publicAccessUsersConfigVirtualApProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUsersConfigVirtualApProfileIndex.setStatus("current")
_PublicAccessUserTable_Object = MibTable
publicAccessUserTable = _PublicAccessUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    publicAccessUserTable.setStatus("current")
_PublicAccessUserEntry_Object = MibTableRow
publicAccessUserEntry = _PublicAccessUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1)
)
publicAccessUserEntry.setIndexNames(
    (0, "COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserIndex"),
)
if mibBuilder.loadTexts:
    publicAccessUserEntry.setStatus("current")


class _PublicAccessUserIndex_Type(Integer32):
    """Custom type publicAccessUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PublicAccessUserIndex_Type.__name__ = "Integer32"
_PublicAccessUserIndex_Object = MibTableColumn
publicAccessUserIndex = _PublicAccessUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 1),
    _PublicAccessUserIndex_Type()
)
publicAccessUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    publicAccessUserIndex.setStatus("current")
_PublicAccessUserAuthenType_Type = ColubrisUsersAuthenticationType
_PublicAccessUserAuthenType_Object = MibTableColumn
publicAccessUserAuthenType = _PublicAccessUserAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 2),
    _PublicAccessUserAuthenType_Type()
)
publicAccessUserAuthenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserAuthenType.setStatus("current")
_PublicAccessUserAuthenMode_Type = ColubrisUsersAuthenticationMode
_PublicAccessUserAuthenMode_Object = MibTableColumn
publicAccessUserAuthenMode = _PublicAccessUserAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 3),
    _PublicAccessUserAuthenMode_Type()
)
publicAccessUserAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserAuthenMode.setStatus("current")


class _PublicAccessUserState_Type(Integer32):
    """Custom type publicAccessUserState based on Integer32"""
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
        *(("connected", 2),
          ("connecting", 1),
          ("disconnected", 5),
          ("disconnectedAdministrative", 7),
          ("disconnecting", 4),
          ("disconnectingAdministrative", 6),
          ("reconnecting", 3),
          ("unassigned", 0))
    )


_PublicAccessUserState_Type.__name__ = "Integer32"
_PublicAccessUserState_Object = MibTableColumn
publicAccessUserState = _PublicAccessUserState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 4),
    _PublicAccessUserState_Type()
)
publicAccessUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserState.setStatus("current")
_PublicAccessUserStationIpAddress_Type = IpAddress
_PublicAccessUserStationIpAddress_Object = MibTableColumn
publicAccessUserStationIpAddress = _PublicAccessUserStationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 5),
    _PublicAccessUserStationIpAddress_Type()
)
publicAccessUserStationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserStationIpAddress.setStatus("current")


class _PublicAccessUserName_Type(OctetString):
    """Custom type publicAccessUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_PublicAccessUserName_Type.__name__ = "OctetString"
_PublicAccessUserName_Object = MibTableColumn
publicAccessUserName = _PublicAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 6),
    _PublicAccessUserName_Type()
)
publicAccessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserName.setStatus("current")
_PublicAccessUserSessionStartTime_Type = DateAndTime
_PublicAccessUserSessionStartTime_Object = MibTableColumn
publicAccessUserSessionStartTime = _PublicAccessUserSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 7),
    _PublicAccessUserSessionStartTime_Type()
)
publicAccessUserSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserSessionStartTime.setStatus("current")
_PublicAccessUserSessionDuration_Type = Counter32
_PublicAccessUserSessionDuration_Object = MibTableColumn
publicAccessUserSessionDuration = _PublicAccessUserSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 8),
    _PublicAccessUserSessionDuration_Type()
)
publicAccessUserSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    publicAccessUserSessionDuration.setUnits("seconds")
_PublicAccessUserIdleTime_Type = Counter32
_PublicAccessUserIdleTime_Object = MibTableColumn
publicAccessUserIdleTime = _PublicAccessUserIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 9),
    _PublicAccessUserIdleTime_Type()
)
publicAccessUserIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    publicAccessUserIdleTime.setUnits("seconds")
_PublicAccessUserBytesSent_Type = Counter64
_PublicAccessUserBytesSent_Object = MibTableColumn
publicAccessUserBytesSent = _PublicAccessUserBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 10),
    _PublicAccessUserBytesSent_Type()
)
publicAccessUserBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserBytesSent.setStatus("current")
_PublicAccessUserBytesReceived_Type = Counter64
_PublicAccessUserBytesReceived_Object = MibTableColumn
publicAccessUserBytesReceived = _PublicAccessUserBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 11),
    _PublicAccessUserBytesReceived_Type()
)
publicAccessUserBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserBytesReceived.setStatus("current")
_PublicAccessUserPacketsSent_Type = Counter32
_PublicAccessUserPacketsSent_Object = MibTableColumn
publicAccessUserPacketsSent = _PublicAccessUserPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 12),
    _PublicAccessUserPacketsSent_Type()
)
publicAccessUserPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserPacketsSent.setStatus("current")
_PublicAccessUserPacketsReceived_Type = Counter32
_PublicAccessUserPacketsReceived_Object = MibTableColumn
publicAccessUserPacketsReceived = _PublicAccessUserPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 13),
    _PublicAccessUserPacketsReceived_Type()
)
publicAccessUserPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserPacketsReceived.setStatus("current")


class _PublicAccessUserForceDisconnection_Type(Integer32):
    """Custom type publicAccessUserForceDisconnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adminReset", 1),
          ("idle", 0))
    )


_PublicAccessUserForceDisconnection_Type.__name__ = "Integer32"
_PublicAccessUserForceDisconnection_Object = MibTableColumn
publicAccessUserForceDisconnection = _PublicAccessUserForceDisconnection_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 14),
    _PublicAccessUserForceDisconnection_Type()
)
publicAccessUserForceDisconnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessUserForceDisconnection.setStatus("current")
_PublicAccessUserStationMacAddress_Type = MacAddress
_PublicAccessUserStationMacAddress_Object = MibTableColumn
publicAccessUserStationMacAddress = _PublicAccessUserStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 15),
    _PublicAccessUserStationMacAddress_Type()
)
publicAccessUserStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserStationMacAddress.setStatus("current")
_PublicAccessUserApMacAddress_Type = MacAddress
_PublicAccessUserApMacAddress_Object = MibTableColumn
publicAccessUserApMacAddress = _PublicAccessUserApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 16),
    _PublicAccessUserApMacAddress_Type()
)
publicAccessUserApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserApMacAddress.setStatus("current")


class _PublicAccessUserGroupName_Type(OctetString):
    """Custom type publicAccessUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PublicAccessUserGroupName_Type.__name__ = "OctetString"
_PublicAccessUserGroupName_Object = MibTableColumn
publicAccessUserGroupName = _PublicAccessUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 17),
    _PublicAccessUserGroupName_Type()
)
publicAccessUserGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserGroupName.setStatus("current")
_PublicAccessUserSSID_Type = ColubrisSSIDOrNone
_PublicAccessUserSSID_Object = MibTableColumn
publicAccessUserSSID = _PublicAccessUserSSID_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 18),
    _PublicAccessUserSSID_Type()
)
publicAccessUserSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserSSID.setStatus("current")
_PublicAccessUserSecurity_Type = ColubrisSecurity
_PublicAccessUserSecurity_Object = MibTableColumn
publicAccessUserSecurity = _PublicAccessUserSecurity_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 19),
    _PublicAccessUserSecurity_Type()
)
publicAccessUserSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserSecurity.setStatus("current")


class _PublicAccessUserPHYType_Type(Integer32):
    """Custom type publicAccessUserPHYType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11g", 3),
          ("ieee802dot11n", 4),
          ("unknown", 0))
    )


_PublicAccessUserPHYType_Type.__name__ = "Integer32"
_PublicAccessUserPHYType_Object = MibTableColumn
publicAccessUserPHYType = _PublicAccessUserPHYType_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 20),
    _PublicAccessUserPHYType_Type()
)
publicAccessUserPHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserPHYType.setStatus("current")


class _PublicAccessUserVLAN_Type(Integer32):
    """Custom type publicAccessUserVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PublicAccessUserVLAN_Type.__name__ = "Integer32"
_PublicAccessUserVLAN_Object = MibTableColumn
publicAccessUserVLAN = _PublicAccessUserVLAN_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 21),
    _PublicAccessUserVLAN_Type()
)
publicAccessUserVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserVLAN.setStatus("current")


class _PublicAccessUserApRadioIndex_Type(Integer32):
    """Custom type publicAccessUserApRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PublicAccessUserApRadioIndex_Type.__name__ = "Integer32"
_PublicAccessUserApRadioIndex_Object = MibTableColumn
publicAccessUserApRadioIndex = _PublicAccessUserApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 22),
    _PublicAccessUserApRadioIndex_Type()
)
publicAccessUserApRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserApRadioIndex.setStatus("current")


class _PublicAccessUserConfigIndex_Type(Integer32):
    """Custom type publicAccessUserConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PublicAccessUserConfigIndex_Type.__name__ = "Integer32"
_PublicAccessUserConfigIndex_Object = MibTableColumn
publicAccessUserConfigIndex = _PublicAccessUserConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 23),
    _PublicAccessUserConfigIndex_Type()
)
publicAccessUserConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserConfigIndex.setStatus("current")


class _PublicAccessUserConnectedInterface_Type(OctetString):
    """Custom type publicAccessUserConnectedInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PublicAccessUserConnectedInterface_Type.__name__ = "OctetString"
_PublicAccessUserConnectedInterface_Object = MibTableColumn
publicAccessUserConnectedInterface = _PublicAccessUserConnectedInterface_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 24),
    _PublicAccessUserConnectedInterface_Type()
)
publicAccessUserConnectedInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    publicAccessUserConnectedInterface.setStatus("current")
_PublicAccessUserBytesSentDropped_Type = Counter64
_PublicAccessUserBytesSentDropped_Object = MibTableColumn
publicAccessUserBytesSentDropped = _PublicAccessUserBytesSentDropped_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 25),
    _PublicAccessUserBytesSentDropped_Type()
)
publicAccessUserBytesSentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserBytesSentDropped.setStatus("current")
_PublicAccessUserBytesReceivedDropped_Type = Counter64
_PublicAccessUserBytesReceivedDropped_Object = MibTableColumn
publicAccessUserBytesReceivedDropped = _PublicAccessUserBytesReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 26),
    _PublicAccessUserBytesReceivedDropped_Type()
)
publicAccessUserBytesReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserBytesReceivedDropped.setStatus("current")
_PublicAccessUserPacketsSentDropped_Type = Counter32
_PublicAccessUserPacketsSentDropped_Object = MibTableColumn
publicAccessUserPacketsSentDropped = _PublicAccessUserPacketsSentDropped_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 27),
    _PublicAccessUserPacketsSentDropped_Type()
)
publicAccessUserPacketsSentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserPacketsSentDropped.setStatus("current")
_PublicAccessUserPacketsReceivedDropped_Type = Counter32
_PublicAccessUserPacketsReceivedDropped_Object = MibTableColumn
publicAccessUserPacketsReceivedDropped = _PublicAccessUserPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 28),
    _PublicAccessUserPacketsReceivedDropped_Type()
)
publicAccessUserPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserPacketsReceivedDropped.setStatus("current")
_PublicAccessUserRateLimitationEnabled_Type = TruthValue
_PublicAccessUserRateLimitationEnabled_Object = MibTableColumn
publicAccessUserRateLimitationEnabled = _PublicAccessUserRateLimitationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 29),
    _PublicAccessUserRateLimitationEnabled_Type()
)
publicAccessUserRateLimitationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserRateLimitationEnabled.setStatus("current")


class _PublicAccessUserMaxTransmitRate_Type(Integer32):
    """Custom type publicAccessUserMaxTransmitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_PublicAccessUserMaxTransmitRate_Type.__name__ = "Integer32"
_PublicAccessUserMaxTransmitRate_Object = MibTableColumn
publicAccessUserMaxTransmitRate = _PublicAccessUserMaxTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 30),
    _PublicAccessUserMaxTransmitRate_Type()
)
publicAccessUserMaxTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserMaxTransmitRate.setStatus("current")


class _PublicAccessUserMaxReceiveRate_Type(Integer32):
    """Custom type publicAccessUserMaxReceiveRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_PublicAccessUserMaxReceiveRate_Type.__name__ = "Integer32"
_PublicAccessUserMaxReceiveRate_Object = MibTableColumn
publicAccessUserMaxReceiveRate = _PublicAccessUserMaxReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 31),
    _PublicAccessUserMaxReceiveRate_Type()
)
publicAccessUserMaxReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserMaxReceiveRate.setStatus("current")
_PublicAccessUserBandwidthControlLevel_Type = ColubrisPriorityQueue
_PublicAccessUserBandwidthControlLevel_Object = MibTableColumn
publicAccessUserBandwidthControlLevel = _PublicAccessUserBandwidthControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 32),
    _PublicAccessUserBandwidthControlLevel_Type()
)
publicAccessUserBandwidthControlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserBandwidthControlLevel.setStatus("current")
_PublicAccessUserNASPort_Type = Unsigned32
_PublicAccessUserNASPort_Object = MibTableColumn
publicAccessUserNASPort = _PublicAccessUserNASPort_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 33),
    _PublicAccessUserNASPort_Type()
)
publicAccessUserNASPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessUserNASPort.setStatus("current")


class _PublicAccessUsersLoggedInTrapEnabled_Type(ColubrisNotificationEnable):
    """Custom type publicAccessUsersLoggedInTrapEnabled based on ColubrisNotificationEnable"""


_PublicAccessUsersLoggedInTrapEnabled_Object = MibScalar
publicAccessUsersLoggedInTrapEnabled = _PublicAccessUsersLoggedInTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 7),
    _PublicAccessUsersLoggedInTrapEnabled_Type()
)
publicAccessUsersLoggedInTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessUsersLoggedInTrapEnabled.setStatus("current")


class _PublicAccessUsersLoggedInTrapInterval_Type(Unsigned32):
    """Custom type publicAccessUsersLoggedInTrapInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_PublicAccessUsersLoggedInTrapInterval_Type.__name__ = "Unsigned32"
_PublicAccessUsersLoggedInTrapInterval_Object = MibScalar
publicAccessUsersLoggedInTrapInterval = _PublicAccessUsersLoggedInTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 8),
    _PublicAccessUsersLoggedInTrapInterval_Type()
)
publicAccessUsersLoggedInTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessUsersLoggedInTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    publicAccessUsersLoggedInTrapInterval.setUnits("minutes")
_PublicAccessNASPortsGroup_ObjectIdentity = ObjectIdentity
publicAccessNASPortsGroup = _PublicAccessNASPortsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4)
)
_PublicAccessNASPortCount_Type = Gauge32
_PublicAccessNASPortCount_Object = MibScalar
publicAccessNASPortCount = _PublicAccessNASPortCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 1),
    _PublicAccessNASPortCount_Type()
)
publicAccessNASPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessNASPortCount.setStatus("current")
_PublicAccessNASPortTable_Object = MibTable
publicAccessNASPortTable = _PublicAccessNASPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    publicAccessNASPortTable.setStatus("current")
_PublicAccessNASPortEntry_Object = MibTableRow
publicAccessNASPortEntry = _PublicAccessNASPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 2, 1)
)
publicAccessNASPortEntry.setIndexNames(
    (0, "COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessNASPortIndex"),
)
if mibBuilder.loadTexts:
    publicAccessNASPortEntry.setStatus("current")


class _PublicAccessNASPortIndex_Type(Integer32):
    """Custom type publicAccessNASPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PublicAccessNASPortIndex_Type.__name__ = "Integer32"
_PublicAccessNASPortIndex_Object = MibTableColumn
publicAccessNASPortIndex = _PublicAccessNASPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 2, 1, 1),
    _PublicAccessNASPortIndex_Type()
)
publicAccessNASPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    publicAccessNASPortIndex.setStatus("current")


class _PublicAccessNASPortUserName_Type(OctetString):
    """Custom type publicAccessNASPortUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_PublicAccessNASPortUserName_Type.__name__ = "OctetString"
_PublicAccessNASPortUserName_Object = MibTableColumn
publicAccessNASPortUserName = _PublicAccessNASPortUserName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 2, 1, 2),
    _PublicAccessNASPortUserName_Type()
)
publicAccessNASPortUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessNASPortUserName.setStatus("current")
_PublicAccessMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
publicAccessMIBNotificationPrefix = _PublicAccessMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 2)
)
_PublicAccessMIBNotifications_ObjectIdentity = ObjectIdentity
publicAccessMIBNotifications = _PublicAccessMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0)
)
_ColubrisPublicAccessMIBConformance_ObjectIdentity = ObjectIdentity
colubrisPublicAccessMIBConformance = _ColubrisPublicAccessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 3)
)
_ColubrisPublicAccessMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisPublicAccessMIBCompliances = _ColubrisPublicAccessMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 1)
)
_ColubrisPublicAccessMIBGroups_ObjectIdentity = ObjectIdentity
colubrisPublicAccessMIBGroups = _ColubrisPublicAccessMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2)
)

# Managed Objects groups

colubrisPublicAccessMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 1)
)
colubrisPublicAccessMIBGroup.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatus"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatusChangedCause"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceUserName"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceUserPassword"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceSessionTimeoutAdminStatus"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceSessionTimeoutOperStatus"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceConfigMode"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceAuthenProfileIndex"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceAccountingEnabled"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceAccountingProfileIndex"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceForceReconfiguration"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersMaxCount"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersCount"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersThreshold"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersSessionTrapEnabled"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersLoggedInTrapEnabled"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersLoggedInTrapInterval"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessNASPortCount"))
)
if mibBuilder.loadTexts:
    colubrisPublicAccessMIBGroup.setStatus("current")

colubrisPublicAccessUserMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 2)
)
colubrisPublicAccessUserMIBGroup.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserAuthenType"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserAuthenMode"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserState"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserStationIpAddress"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSessionStartTime"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSessionDuration"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserIdleTime"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesSent"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesReceived"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPacketsSent"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPacketsReceived"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserForceDisconnection"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserStationMacAddress"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserApMacAddress"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserGroupName"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSSID"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSecurity"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPHYType"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserVLAN"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserApRadioIndex"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserConfigIndex"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserConnectedInterface"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesSentDropped"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesReceivedDropped"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPacketsSentDropped"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPacketsReceivedDropped"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserRateLimitationEnabled"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserMaxTransmitRate"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserMaxReceiveRate"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBandwidthControlLevel"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserNASPort"))
)
if mibBuilder.loadTexts:
    colubrisPublicAccessUserMIBGroup.setStatus("current")

colubrisPublicAccessUserConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 3)
)
colubrisPublicAccessUserConfigMIBGroup.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAuthenType"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAuthenMode"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAuthenProfileIndex"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAuthenTimeout"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAccountingEnabled"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAccountingProfileIndex"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigInterfaceIndex"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigVirtualApProfileIndex"))
)
if mibBuilder.loadTexts:
    colubrisPublicAccessUserConfigMIBGroup.setStatus("current")

colubrisPublicAccessNASPortsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 5)
)
colubrisPublicAccessNASPortsMIBGroup.setObjects(
    ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessNASPortUserName")
)
if mibBuilder.loadTexts:
    colubrisPublicAccessNASPortsMIBGroup.setStatus("current")


# Notification objects

publicAccessStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 1)
)
publicAccessStatusChangedTrap.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatus"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatusChangedCause"))
)
if mibBuilder.loadTexts:
    publicAccessStatusChangedTrap.setStatus(
        "current"
    )

publicAccessUsersThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 2)
)
publicAccessUsersThresholdTrap.setObjects(
    ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersCount")
)
if mibBuilder.loadTexts:
    publicAccessUsersThresholdTrap.setStatus(
        "current"
    )

publicAccessUsersSessionStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 3)
)
publicAccessUsersSessionStartTrap.setObjects(
    ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName")
)
if mibBuilder.loadTexts:
    publicAccessUsersSessionStartTrap.setStatus(
        "current"
    )

publicAccessUsersSessionStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 4)
)
publicAccessUsersSessionStopTrap.setObjects(
    ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName")
)
if mibBuilder.loadTexts:
    publicAccessUsersSessionStopTrap.setStatus(
        "current"
    )

publicAccessUsersSessionFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 5)
)
publicAccessUsersSessionFailTrap.setObjects(
    ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName")
)
if mibBuilder.loadTexts:
    publicAccessUsersSessionFailTrap.setStatus(
        "current"
    )

publicAccessUsersLoggedInTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 6)
)
publicAccessUsersLoggedInTrap.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersCount"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserStationIpAddress"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserStationMacAddress"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserApMacAddress"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserConnectedInterface"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSessionDuration"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesReceived"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesSent"))
)
if mibBuilder.loadTexts:
    publicAccessUsersLoggedInTrap.setStatus(
        "current"
    )


# Notifications groups

colubrisPublicAccessNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 4)
)
colubrisPublicAccessNotificationGroup.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatusChangedTrap"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersThresholdTrap"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersSessionStartTrap"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersSessionStopTrap"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersSessionFailTrap"),
        ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersLoggedInTrap"))
)
if mibBuilder.loadTexts:
    colubrisPublicAccessNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisPublicAccessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisPublicAccessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-PUBLIC-ACCESS-MIB",
    **{"colubrisPublicAccessMIB": colubrisPublicAccessMIB,
       "colubrisPublicAccessMIBObjects": colubrisPublicAccessMIBObjects,
       "publicAccessGroup": publicAccessGroup,
       "publicAccessStatus": publicAccessStatus,
       "publicAccessStatusChangedCause": publicAccessStatusChangedCause,
       "publicAccessDeviceGroup": publicAccessDeviceGroup,
       "publicAccessDeviceUserName": publicAccessDeviceUserName,
       "publicAccessDeviceUserPassword": publicAccessDeviceUserPassword,
       "publicAccessDeviceSessionTimeoutAdminStatus": publicAccessDeviceSessionTimeoutAdminStatus,
       "publicAccessDeviceSessionTimeoutOperStatus": publicAccessDeviceSessionTimeoutOperStatus,
       "publicAccessDeviceConfigMode": publicAccessDeviceConfigMode,
       "publicAccessDeviceAuthenProfileIndex": publicAccessDeviceAuthenProfileIndex,
       "publicAccessDeviceAccountingEnabled": publicAccessDeviceAccountingEnabled,
       "publicAccessDeviceAccountingProfileIndex": publicAccessDeviceAccountingProfileIndex,
       "publicAccessDeviceForceReconfiguration": publicAccessDeviceForceReconfiguration,
       "publicAccessUsersGroup": publicAccessUsersGroup,
       "publicAccessUsersMaxCount": publicAccessUsersMaxCount,
       "publicAccessUsersCount": publicAccessUsersCount,
       "publicAccessUsersThreshold": publicAccessUsersThreshold,
       "publicAccessUsersSessionTrapEnabled": publicAccessUsersSessionTrapEnabled,
       "publicAccessUsersConfigTable": publicAccessUsersConfigTable,
       "publicAccessUsersConfigEntry": publicAccessUsersConfigEntry,
       "publicAccessUsersConfigIndex": publicAccessUsersConfigIndex,
       "publicAccessUsersConfigAuthenType": publicAccessUsersConfigAuthenType,
       "publicAccessUsersConfigAuthenMode": publicAccessUsersConfigAuthenMode,
       "publicAccessUsersConfigAuthenProfileIndex": publicAccessUsersConfigAuthenProfileIndex,
       "publicAccessUsersConfigAuthenTimeout": publicAccessUsersConfigAuthenTimeout,
       "publicAccessUsersConfigAccountingEnabled": publicAccessUsersConfigAccountingEnabled,
       "publicAccessUsersConfigAccountingProfileIndex": publicAccessUsersConfigAccountingProfileIndex,
       "publicAccessUsersConfigInterfaceIndex": publicAccessUsersConfigInterfaceIndex,
       "publicAccessUsersConfigVirtualApProfileIndex": publicAccessUsersConfigVirtualApProfileIndex,
       "publicAccessUserTable": publicAccessUserTable,
       "publicAccessUserEntry": publicAccessUserEntry,
       "publicAccessUserIndex": publicAccessUserIndex,
       "publicAccessUserAuthenType": publicAccessUserAuthenType,
       "publicAccessUserAuthenMode": publicAccessUserAuthenMode,
       "publicAccessUserState": publicAccessUserState,
       "publicAccessUserStationIpAddress": publicAccessUserStationIpAddress,
       "publicAccessUserName": publicAccessUserName,
       "publicAccessUserSessionStartTime": publicAccessUserSessionStartTime,
       "publicAccessUserSessionDuration": publicAccessUserSessionDuration,
       "publicAccessUserIdleTime": publicAccessUserIdleTime,
       "publicAccessUserBytesSent": publicAccessUserBytesSent,
       "publicAccessUserBytesReceived": publicAccessUserBytesReceived,
       "publicAccessUserPacketsSent": publicAccessUserPacketsSent,
       "publicAccessUserPacketsReceived": publicAccessUserPacketsReceived,
       "publicAccessUserForceDisconnection": publicAccessUserForceDisconnection,
       "publicAccessUserStationMacAddress": publicAccessUserStationMacAddress,
       "publicAccessUserApMacAddress": publicAccessUserApMacAddress,
       "publicAccessUserGroupName": publicAccessUserGroupName,
       "publicAccessUserSSID": publicAccessUserSSID,
       "publicAccessUserSecurity": publicAccessUserSecurity,
       "publicAccessUserPHYType": publicAccessUserPHYType,
       "publicAccessUserVLAN": publicAccessUserVLAN,
       "publicAccessUserApRadioIndex": publicAccessUserApRadioIndex,
       "publicAccessUserConfigIndex": publicAccessUserConfigIndex,
       "publicAccessUserConnectedInterface": publicAccessUserConnectedInterface,
       "publicAccessUserBytesSentDropped": publicAccessUserBytesSentDropped,
       "publicAccessUserBytesReceivedDropped": publicAccessUserBytesReceivedDropped,
       "publicAccessUserPacketsSentDropped": publicAccessUserPacketsSentDropped,
       "publicAccessUserPacketsReceivedDropped": publicAccessUserPacketsReceivedDropped,
       "publicAccessUserRateLimitationEnabled": publicAccessUserRateLimitationEnabled,
       "publicAccessUserMaxTransmitRate": publicAccessUserMaxTransmitRate,
       "publicAccessUserMaxReceiveRate": publicAccessUserMaxReceiveRate,
       "publicAccessUserBandwidthControlLevel": publicAccessUserBandwidthControlLevel,
       "publicAccessUserNASPort": publicAccessUserNASPort,
       "publicAccessUsersLoggedInTrapEnabled": publicAccessUsersLoggedInTrapEnabled,
       "publicAccessUsersLoggedInTrapInterval": publicAccessUsersLoggedInTrapInterval,
       "publicAccessNASPortsGroup": publicAccessNASPortsGroup,
       "publicAccessNASPortCount": publicAccessNASPortCount,
       "publicAccessNASPortTable": publicAccessNASPortTable,
       "publicAccessNASPortEntry": publicAccessNASPortEntry,
       "publicAccessNASPortIndex": publicAccessNASPortIndex,
       "publicAccessNASPortUserName": publicAccessNASPortUserName,
       "publicAccessMIBNotificationPrefix": publicAccessMIBNotificationPrefix,
       "publicAccessMIBNotifications": publicAccessMIBNotifications,
       "publicAccessStatusChangedTrap": publicAccessStatusChangedTrap,
       "publicAccessUsersThresholdTrap": publicAccessUsersThresholdTrap,
       "publicAccessUsersSessionStartTrap": publicAccessUsersSessionStartTrap,
       "publicAccessUsersSessionStopTrap": publicAccessUsersSessionStopTrap,
       "publicAccessUsersSessionFailTrap": publicAccessUsersSessionFailTrap,
       "publicAccessUsersLoggedInTrap": publicAccessUsersLoggedInTrap,
       "colubrisPublicAccessMIBConformance": colubrisPublicAccessMIBConformance,
       "colubrisPublicAccessMIBCompliances": colubrisPublicAccessMIBCompliances,
       "colubrisPublicAccessMIBCompliance": colubrisPublicAccessMIBCompliance,
       "colubrisPublicAccessMIBGroups": colubrisPublicAccessMIBGroups,
       "colubrisPublicAccessMIBGroup": colubrisPublicAccessMIBGroup,
       "colubrisPublicAccessUserMIBGroup": colubrisPublicAccessUserMIBGroup,
       "colubrisPublicAccessUserConfigMIBGroup": colubrisPublicAccessUserConfigMIBGroup,
       "colubrisPublicAccessNotificationGroup": colubrisPublicAccessNotificationGroup,
       "colubrisPublicAccessNASPortsMIBGroup": colubrisPublicAccessNASPortsMIBGroup}
)
