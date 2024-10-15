# SNMP MIB module (MERU-CONFIG-PORTPROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-PORTPROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:05 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlDataplaneMode,
 MwlEnableDisableOption,
 MwlIfAdministrativeState,
 MwlOnOffSwitch,
 MwlOperationalState) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlDataplaneMode",
    "MwlEnableDisableOption",
    "MwlIfAdministrativeState",
    "MwlOnOffSwitch",
    "MwlOperationalState")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigPortProfile = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwPortProfileTable_Object = MibTable
mwPortProfileTable = _MwPortProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1)
)
if mibBuilder.loadTexts:
    mwPortProfileTable.setStatus("current")
_MwPortProfileEntry_Object = MibTableRow
mwPortProfileEntry = _MwPortProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1, 1)
)
mwPortProfileEntry.setIndexNames(
    (0, "MERU-CONFIG-PORTPROFILE-MIB", "mwPortProfileTableIndex"),
)
if mibBuilder.loadTexts:
    mwPortProfileEntry.setStatus("current")
_MwPortProfileTableIndex_Type = Integer32
_MwPortProfileTableIndex_Object = MibTableColumn
mwPortProfileTableIndex = _MwPortProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1, 1, 1),
    _MwPortProfileTableIndex_Type()
)
mwPortProfileTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwPortProfileTableIndex.setStatus("current")


class _MwPortProfileName_Type(DisplayString):
    """Custom type mwPortProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwPortProfileName_Type.__name__ = "DisplayString"
_MwPortProfileName_Object = MibTableColumn
mwPortProfileName = _MwPortProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1, 1, 2),
    _MwPortProfileName_Type()
)
mwPortProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortProfileName.setStatus("current")
_MwPortProfileState_Type = MwlEnableDisableOption
_MwPortProfileState_Object = MibTableColumn
mwPortProfileState = _MwPortProfileState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1, 1, 3),
    _MwPortProfileState_Type()
)
mwPortProfileState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortProfileState.setStatus("current")
_MwPortProfileDataplaneMode_Type = MwlDataplaneMode
_MwPortProfileDataplaneMode_Object = MibTableColumn
mwPortProfileDataplaneMode = _MwPortProfileDataplaneMode_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1, 1, 4),
    _MwPortProfileDataplaneMode_Type()
)
mwPortProfileDataplaneMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortProfileDataplaneMode.setStatus("current")
_MwPortProfileApVlanTag_Type = Unsigned32
_MwPortProfileApVlanTag_Object = MibTableColumn
mwPortProfileApVlanTag = _MwPortProfileApVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1, 1, 5),
    _MwPortProfileApVlanTag_Type()
)
mwPortProfileApVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortProfileApVlanTag.setStatus("current")


class _MwPortProfileVlanName_Type(DisplayString):
    """Custom type mwPortProfileVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwPortProfileVlanName_Type.__name__ = "DisplayString"
_MwPortProfileVlanName_Object = MibTableColumn
mwPortProfileVlanName = _MwPortProfileVlanName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1, 1, 6),
    _MwPortProfileVlanName_Type()
)
mwPortProfileVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortProfileVlanName.setStatus("current")
_MwPortProfileAllowMulticast_Type = MwlOnOffSwitch
_MwPortProfileAllowMulticast_Object = MibTableColumn
mwPortProfileAllowMulticast = _MwPortProfileAllowMulticast_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1, 1, 7),
    _MwPortProfileAllowMulticast_Type()
)
mwPortProfileAllowMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortProfileAllowMulticast.setStatus("current")
_MwPortProfileRowStatus_Type = RowStatus
_MwPortProfileRowStatus_Object = MibTableColumn
mwPortProfileRowStatus = _MwPortProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 1, 1, 10),
    _MwPortProfileRowStatus_Type()
)
mwPortProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortProfileRowStatus.setStatus("current")
_MwPortApTable_Object = MibTable
mwPortApTable = _MwPortApTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2)
)
if mibBuilder.loadTexts:
    mwPortApTable.setStatus("current")
_MwPortApEntry_Object = MibTableRow
mwPortApEntry = _MwPortApEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1)
)
mwPortApEntry.setIndexNames(
    (0, "MERU-CONFIG-PORTPROFILE-MIB", "mwPortApTableIndex"),
)
if mibBuilder.loadTexts:
    mwPortApEntry.setStatus("current")
_MwPortApTableIndex_Type = Integer32
_MwPortApTableIndex_Object = MibTableColumn
mwPortApTableIndex = _MwPortApTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1, 1),
    _MwPortApTableIndex_Type()
)
mwPortApTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwPortApTableIndex.setStatus("current")


class _MwPortApName_Type(DisplayString):
    """Custom type mwPortApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwPortApName_Type.__name__ = "DisplayString"
_MwPortApName_Object = MibTableColumn
mwPortApName = _MwPortApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1, 2),
    _MwPortApName_Type()
)
mwPortApName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortApName.setStatus("current")
_MwPortApNodeId_Type = Unsigned32
_MwPortApNodeId_Object = MibTableColumn
mwPortApNodeId = _MwPortApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1, 3),
    _MwPortApNodeId_Type()
)
mwPortApNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortApNodeId.setStatus("current")
_MwPortApIfIndex_Type = Integer32
_MwPortApIfIndex_Object = MibTableColumn
mwPortApIfIndex = _MwPortApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1, 4),
    _MwPortApIfIndex_Type()
)
mwPortApIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortApIfIndex.setStatus("current")
_MwPortApApName_Type = DisplayString
_MwPortApApName_Object = MibTableColumn
mwPortApApName = _MwPortApApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1, 5),
    _MwPortApApName_Type()
)
mwPortApApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPortApApName.setStatus("current")
_MwPortApMacAddress_Type = MacAddress
_MwPortApMacAddress_Object = MibTableColumn
mwPortApMacAddress = _MwPortApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1, 6),
    _MwPortApMacAddress_Type()
)
mwPortApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPortApMacAddress.setStatus("current")
_MwPortApIfAdminStatus_Type = MwlIfAdministrativeState
_MwPortApIfAdminStatus_Object = MibTableColumn
mwPortApIfAdminStatus = _MwPortApIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1, 7),
    _MwPortApIfAdminStatus_Type()
)
mwPortApIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPortApIfAdminStatus.setStatus("current")
_MwPortApIfOperStatus_Type = MwlOperationalState
_MwPortApIfOperStatus_Object = MibTableColumn
mwPortApIfOperStatus = _MwPortApIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1, 8),
    _MwPortApIfOperStatus_Type()
)
mwPortApIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPortApIfOperStatus.setStatus("current")
_MwPortApRowStatus_Type = RowStatus
_MwPortApRowStatus_Object = MibTableColumn
mwPortApRowStatus = _MwPortApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 19, 2, 1, 9),
    _MwPortApRowStatus_Type()
)
mwPortApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwPortApRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-PORTPROFILE-MIB",
    **{"mwConfigPortProfile": mwConfigPortProfile,
       "mwPortProfileTable": mwPortProfileTable,
       "mwPortProfileEntry": mwPortProfileEntry,
       "mwPortProfileTableIndex": mwPortProfileTableIndex,
       "mwPortProfileName": mwPortProfileName,
       "mwPortProfileState": mwPortProfileState,
       "mwPortProfileDataplaneMode": mwPortProfileDataplaneMode,
       "mwPortProfileApVlanTag": mwPortProfileApVlanTag,
       "mwPortProfileVlanName": mwPortProfileVlanName,
       "mwPortProfileAllowMulticast": mwPortProfileAllowMulticast,
       "mwPortProfileRowStatus": mwPortProfileRowStatus,
       "mwPortApTable": mwPortApTable,
       "mwPortApEntry": mwPortApEntry,
       "mwPortApTableIndex": mwPortApTableIndex,
       "mwPortApName": mwPortApName,
       "mwPortApNodeId": mwPortApNodeId,
       "mwPortApIfIndex": mwPortApIfIndex,
       "mwPortApApName": mwPortApApName,
       "mwPortApMacAddress": mwPortApMacAddress,
       "mwPortApIfAdminStatus": mwPortApIfAdminStatus,
       "mwPortApIfOperStatus": mwPortApIfOperStatus,
       "mwPortApRowStatus": mwPortApRowStatus}
)
