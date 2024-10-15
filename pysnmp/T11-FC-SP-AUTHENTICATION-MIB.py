# SNMP MIB module (T11-FC-SP-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-SP-AUTHENTICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:34 2024
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

(FcNameIdOrZero,
 fcmInstanceIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcNameIdOrZero",
    "fcmInstanceIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(t11FamLocalSwitchWwn,) = mibBuilder.importSymbols(
    "T11-FC-FABRIC-ADDR-MGR-MIB",
    "t11FamLocalSwitchWwn")

(T11FcSpAuthRejReasonCodeExp,
 T11FcSpAuthRejectReasonCode,
 T11FcSpDhGroups,
 T11FcSpHashFunctions,
 T11FcSpLifetimeLeft,
 T11FcSpLifetimeLeftUnits,
 T11FcSpSignFunctions) = mibBuilder.importSymbols(
    "T11-FC-SP-TC-MIB",
    "T11FcSpAuthRejReasonCodeExp",
    "T11FcSpAuthRejectReasonCode",
    "T11FcSpDhGroups",
    "T11FcSpHashFunctions",
    "T11FcSpLifetimeLeft",
    "T11FcSpLifetimeLeftUnits",
    "T11FcSpSignFunctions")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcSpAuthenticationMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 176)
)
t11FcSpAuthenticationMIB.setRevisions(
        ("2008-08-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_T11FcSpAuMIBNotifications_ObjectIdentity = ObjectIdentity
t11FcSpAuMIBNotifications = _T11FcSpAuMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 176, 0)
)
_T11FcSpAuMIBObjects_ObjectIdentity = ObjectIdentity
t11FcSpAuMIBObjects = _T11FcSpAuMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 176, 1)
)
_T11FcSpAuEntityTable_Object = MibTable
t11FcSpAuEntityTable = _T11FcSpAuEntityTable_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpAuEntityTable.setStatus("current")
_T11FcSpAuEntityEntry_Object = MibTableRow
t11FcSpAuEntityEntry = _T11FcSpAuEntityEntry_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1)
)
t11FcSpAuEntityEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName"),
    (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpAuEntityEntry.setStatus("current")


class _T11FcSpAuEntityName_Type(FcNameIdOrZero):
    """Custom type t11FcSpAuEntityName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpAuEntityName_Type.__name__ = "FcNameIdOrZero"
_T11FcSpAuEntityName_Object = MibTableColumn
t11FcSpAuEntityName = _T11FcSpAuEntityName_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 1),
    _T11FcSpAuEntityName_Type()
)
t11FcSpAuEntityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpAuEntityName.setStatus("current")
_T11FcSpAuFabricIndex_Type = T11FabricIndex
_T11FcSpAuFabricIndex_Object = MibTableColumn
t11FcSpAuFabricIndex = _T11FcSpAuFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 2),
    _T11FcSpAuFabricIndex_Type()
)
t11FcSpAuFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpAuFabricIndex.setStatus("current")
_T11FcSpAuServerProtocol_Type = AutonomousType
_T11FcSpAuServerProtocol_Object = MibTableColumn
t11FcSpAuServerProtocol = _T11FcSpAuServerProtocol_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 3),
    _T11FcSpAuServerProtocol_Type()
)
t11FcSpAuServerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuServerProtocol.setStatus("current")
_T11FcSpAuStorageType_Type = StorageType
_T11FcSpAuStorageType_Object = MibTableColumn
t11FcSpAuStorageType = _T11FcSpAuStorageType_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 4),
    _T11FcSpAuStorageType_Type()
)
t11FcSpAuStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpAuStorageType.setStatus("current")


class _T11FcSpAuSendRejNotifyEnable_Type(TruthValue):
    """Custom type t11FcSpAuSendRejNotifyEnable based on TruthValue"""


_T11FcSpAuSendRejNotifyEnable_Object = MibTableColumn
t11FcSpAuSendRejNotifyEnable = _T11FcSpAuSendRejNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 5),
    _T11FcSpAuSendRejNotifyEnable_Type()
)
t11FcSpAuSendRejNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpAuSendRejNotifyEnable.setStatus("current")


class _T11FcSpAuRcvRejNotifyEnable_Type(TruthValue):
    """Custom type t11FcSpAuRcvRejNotifyEnable based on TruthValue"""


_T11FcSpAuRcvRejNotifyEnable_Object = MibTableColumn
t11FcSpAuRcvRejNotifyEnable = _T11FcSpAuRcvRejNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 6),
    _T11FcSpAuRcvRejNotifyEnable_Type()
)
t11FcSpAuRcvRejNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpAuRcvRejNotifyEnable.setStatus("current")


class _T11FcSpAuDefaultLifetime_Type(T11FcSpLifetimeLeft):
    """Custom type t11FcSpAuDefaultLifetime based on T11FcSpLifetimeLeft"""
    defaultValue = 28800


_T11FcSpAuDefaultLifetime_Object = MibTableColumn
t11FcSpAuDefaultLifetime = _T11FcSpAuDefaultLifetime_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 7),
    _T11FcSpAuDefaultLifetime_Type()
)
t11FcSpAuDefaultLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpAuDefaultLifetime.setStatus("current")


class _T11FcSpAuDefaultLifetimeUnits_Type(T11FcSpLifetimeLeftUnits):
    """Custom type t11FcSpAuDefaultLifetimeUnits based on T11FcSpLifetimeLeftUnits"""


_T11FcSpAuDefaultLifetimeUnits_Object = MibTableColumn
t11FcSpAuDefaultLifetimeUnits = _T11FcSpAuDefaultLifetimeUnits_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 8),
    _T11FcSpAuDefaultLifetimeUnits_Type()
)
t11FcSpAuDefaultLifetimeUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpAuDefaultLifetimeUnits.setStatus("current")


class _T11FcSpAuRejectMaxRows_Type(Unsigned32):
    """Custom type t11FcSpAuRejectMaxRows based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_T11FcSpAuRejectMaxRows_Type.__name__ = "Unsigned32"
_T11FcSpAuRejectMaxRows_Object = MibTableColumn
t11FcSpAuRejectMaxRows = _T11FcSpAuRejectMaxRows_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 9),
    _T11FcSpAuRejectMaxRows_Type()
)
t11FcSpAuRejectMaxRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpAuRejectMaxRows.setStatus("current")
_T11FcSpAuDhChapHashFunctions_Type = T11FcSpHashFunctions
_T11FcSpAuDhChapHashFunctions_Object = MibTableColumn
t11FcSpAuDhChapHashFunctions = _T11FcSpAuDhChapHashFunctions_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 10),
    _T11FcSpAuDhChapHashFunctions_Type()
)
t11FcSpAuDhChapHashFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuDhChapHashFunctions.setStatus("current")
_T11FcSpAuDhChapDhGroups_Type = T11FcSpDhGroups
_T11FcSpAuDhChapDhGroups_Object = MibTableColumn
t11FcSpAuDhChapDhGroups = _T11FcSpAuDhChapDhGroups_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 11),
    _T11FcSpAuDhChapDhGroups_Type()
)
t11FcSpAuDhChapDhGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuDhChapDhGroups.setStatus("current")
_T11FcSpAuFcapHashFunctions_Type = T11FcSpHashFunctions
_T11FcSpAuFcapHashFunctions_Object = MibTableColumn
t11FcSpAuFcapHashFunctions = _T11FcSpAuFcapHashFunctions_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 12),
    _T11FcSpAuFcapHashFunctions_Type()
)
t11FcSpAuFcapHashFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuFcapHashFunctions.setStatus("current")
_T11FcSpAuFcapCertsSignFunctions_Type = T11FcSpSignFunctions
_T11FcSpAuFcapCertsSignFunctions_Object = MibTableColumn
t11FcSpAuFcapCertsSignFunctions = _T11FcSpAuFcapCertsSignFunctions_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 13),
    _T11FcSpAuFcapCertsSignFunctions_Type()
)
t11FcSpAuFcapCertsSignFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuFcapCertsSignFunctions.setStatus("current")
_T11FcSpAuFcapDhGroups_Type = T11FcSpDhGroups
_T11FcSpAuFcapDhGroups_Object = MibTableColumn
t11FcSpAuFcapDhGroups = _T11FcSpAuFcapDhGroups_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 14),
    _T11FcSpAuFcapDhGroups_Type()
)
t11FcSpAuFcapDhGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuFcapDhGroups.setStatus("current")
_T11FcSpAuFcpapHashFunctions_Type = T11FcSpHashFunctions
_T11FcSpAuFcpapHashFunctions_Object = MibTableColumn
t11FcSpAuFcpapHashFunctions = _T11FcSpAuFcpapHashFunctions_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 15),
    _T11FcSpAuFcpapHashFunctions_Type()
)
t11FcSpAuFcpapHashFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuFcpapHashFunctions.setStatus("current")
_T11FcSpAuFcpapDhGroups_Type = T11FcSpDhGroups
_T11FcSpAuFcpapDhGroups_Object = MibTableColumn
t11FcSpAuFcpapDhGroups = _T11FcSpAuFcpapDhGroups_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 16),
    _T11FcSpAuFcpapDhGroups_Type()
)
t11FcSpAuFcpapDhGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuFcpapDhGroups.setStatus("current")
_T11FcSpAuIfStatTable_Object = MibTable
t11FcSpAuIfStatTable = _T11FcSpAuIfStatTable_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2)
)
if mibBuilder.loadTexts:
    t11FcSpAuIfStatTable.setStatus("current")
_T11FcSpAuIfStatEntry_Object = MibTableRow
t11FcSpAuIfStatEntry = _T11FcSpAuIfStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1)
)
t11FcSpAuIfStatEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName"),
    (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatInterfaceIndex"),
    (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpAuIfStatEntry.setStatus("current")
_T11FcSpAuIfStatInterfaceIndex_Type = InterfaceIndex
_T11FcSpAuIfStatInterfaceIndex_Object = MibTableColumn
t11FcSpAuIfStatInterfaceIndex = _T11FcSpAuIfStatInterfaceIndex_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 1),
    _T11FcSpAuIfStatInterfaceIndex_Type()
)
t11FcSpAuIfStatInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpAuIfStatInterfaceIndex.setStatus("current")
_T11FcSpAuIfStatFabricIndex_Type = T11FabricIndex
_T11FcSpAuIfStatFabricIndex_Object = MibTableColumn
t11FcSpAuIfStatFabricIndex = _T11FcSpAuIfStatFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 2),
    _T11FcSpAuIfStatFabricIndex_Type()
)
t11FcSpAuIfStatFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpAuIfStatFabricIndex.setStatus("current")
_T11FcSpAuIfStatTimeouts_Type = Counter32
_T11FcSpAuIfStatTimeouts_Object = MibTableColumn
t11FcSpAuIfStatTimeouts = _T11FcSpAuIfStatTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 3),
    _T11FcSpAuIfStatTimeouts_Type()
)
t11FcSpAuIfStatTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuIfStatTimeouts.setStatus("current")
_T11FcSpAuIfStatInAcceptedMsgs_Type = Counter32
_T11FcSpAuIfStatInAcceptedMsgs_Object = MibTableColumn
t11FcSpAuIfStatInAcceptedMsgs = _T11FcSpAuIfStatInAcceptedMsgs_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 4),
    _T11FcSpAuIfStatInAcceptedMsgs_Type()
)
t11FcSpAuIfStatInAcceptedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuIfStatInAcceptedMsgs.setStatus("current")
_T11FcSpAuIfStatInLsSwRejectedMsgs_Type = Counter32
_T11FcSpAuIfStatInLsSwRejectedMsgs_Object = MibTableColumn
t11FcSpAuIfStatInLsSwRejectedMsgs = _T11FcSpAuIfStatInLsSwRejectedMsgs_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 5),
    _T11FcSpAuIfStatInLsSwRejectedMsgs_Type()
)
t11FcSpAuIfStatInLsSwRejectedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuIfStatInLsSwRejectedMsgs.setStatus("current")
_T11FcSpAuIfStatInAuthRejectedMsgs_Type = Counter32
_T11FcSpAuIfStatInAuthRejectedMsgs_Object = MibTableColumn
t11FcSpAuIfStatInAuthRejectedMsgs = _T11FcSpAuIfStatInAuthRejectedMsgs_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 6),
    _T11FcSpAuIfStatInAuthRejectedMsgs_Type()
)
t11FcSpAuIfStatInAuthRejectedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuIfStatInAuthRejectedMsgs.setStatus("current")
_T11FcSpAuIfStatOutAcceptedMsgs_Type = Counter32
_T11FcSpAuIfStatOutAcceptedMsgs_Object = MibTableColumn
t11FcSpAuIfStatOutAcceptedMsgs = _T11FcSpAuIfStatOutAcceptedMsgs_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 7),
    _T11FcSpAuIfStatOutAcceptedMsgs_Type()
)
t11FcSpAuIfStatOutAcceptedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuIfStatOutAcceptedMsgs.setStatus("current")
_T11FcSpAuIfStatOutLsSwRejectedMsgs_Type = Counter32
_T11FcSpAuIfStatOutLsSwRejectedMsgs_Object = MibTableColumn
t11FcSpAuIfStatOutLsSwRejectedMsgs = _T11FcSpAuIfStatOutLsSwRejectedMsgs_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 8),
    _T11FcSpAuIfStatOutLsSwRejectedMsgs_Type()
)
t11FcSpAuIfStatOutLsSwRejectedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuIfStatOutLsSwRejectedMsgs.setStatus("current")
_T11FcSpAuIfStatOutAuthRejectedMsgs_Type = Counter32
_T11FcSpAuIfStatOutAuthRejectedMsgs_Object = MibTableColumn
t11FcSpAuIfStatOutAuthRejectedMsgs = _T11FcSpAuIfStatOutAuthRejectedMsgs_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 9),
    _T11FcSpAuIfStatOutAuthRejectedMsgs_Type()
)
t11FcSpAuIfStatOutAuthRejectedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuIfStatOutAuthRejectedMsgs.setStatus("current")
_T11FcSpAuRejectTable_Object = MibTable
t11FcSpAuRejectTable = _T11FcSpAuRejectTable_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3)
)
if mibBuilder.loadTexts:
    t11FcSpAuRejectTable.setStatus("current")
_T11FcSpAuRejectEntry_Object = MibTableRow
t11FcSpAuRejectEntry = _T11FcSpAuRejectEntry_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3, 1)
)
t11FcSpAuRejectEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName"),
    (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejInterfaceIndex"),
    (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejFabricIndex"),
    (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejTimestamp"),
)
if mibBuilder.loadTexts:
    t11FcSpAuRejectEntry.setStatus("current")
_T11FcSpAuRejInterfaceIndex_Type = InterfaceIndex
_T11FcSpAuRejInterfaceIndex_Object = MibTableColumn
t11FcSpAuRejInterfaceIndex = _T11FcSpAuRejInterfaceIndex_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 1),
    _T11FcSpAuRejInterfaceIndex_Type()
)
t11FcSpAuRejInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpAuRejInterfaceIndex.setStatus("current")
_T11FcSpAuRejFabricIndex_Type = T11FabricIndex
_T11FcSpAuRejFabricIndex_Object = MibTableColumn
t11FcSpAuRejFabricIndex = _T11FcSpAuRejFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 2),
    _T11FcSpAuRejFabricIndex_Type()
)
t11FcSpAuRejFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpAuRejFabricIndex.setStatus("current")
_T11FcSpAuRejTimestamp_Type = TimeStamp
_T11FcSpAuRejTimestamp_Object = MibTableColumn
t11FcSpAuRejTimestamp = _T11FcSpAuRejTimestamp_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 3),
    _T11FcSpAuRejTimestamp_Type()
)
t11FcSpAuRejTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpAuRejTimestamp.setStatus("current")


class _T11FcSpAuRejDirection_Type(Integer32):
    """Custom type t11FcSpAuRejDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("received", 2),
          ("sent", 1))
    )


_T11FcSpAuRejDirection_Type.__name__ = "Integer32"
_T11FcSpAuRejDirection_Object = MibTableColumn
t11FcSpAuRejDirection = _T11FcSpAuRejDirection_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 4),
    _T11FcSpAuRejDirection_Type()
)
t11FcSpAuRejDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuRejDirection.setStatus("current")


class _T11FcSpAuRejType_Type(Integer32):
    """Custom type t11FcSpAuRejType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authReject", 1),
          ("lsRjt", 3),
          ("swRjt", 2))
    )


_T11FcSpAuRejType_Type.__name__ = "Integer32"
_T11FcSpAuRejType_Object = MibTableColumn
t11FcSpAuRejType = _T11FcSpAuRejType_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 5),
    _T11FcSpAuRejType_Type()
)
t11FcSpAuRejType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuRejType.setStatus("current")


class _T11FcSpAuRejAuthMsgString_Type(OctetString):
    """Custom type t11FcSpAuRejAuthMsgString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11FcSpAuRejAuthMsgString_Type.__name__ = "OctetString"
_T11FcSpAuRejAuthMsgString_Object = MibTableColumn
t11FcSpAuRejAuthMsgString = _T11FcSpAuRejAuthMsgString_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 6),
    _T11FcSpAuRejAuthMsgString_Type()
)
t11FcSpAuRejAuthMsgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuRejAuthMsgString.setStatus("current")
_T11FcSpAuRejReasonCode_Type = T11FcSpAuthRejectReasonCode
_T11FcSpAuRejReasonCode_Object = MibTableColumn
t11FcSpAuRejReasonCode = _T11FcSpAuRejReasonCode_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 7),
    _T11FcSpAuRejReasonCode_Type()
)
t11FcSpAuRejReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuRejReasonCode.setStatus("current")
_T11FcSpAuRejReasonCodeExp_Type = T11FcSpAuthRejReasonCodeExp
_T11FcSpAuRejReasonCodeExp_Object = MibTableColumn
t11FcSpAuRejReasonCodeExp = _T11FcSpAuRejReasonCodeExp_Object(
    (1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 8),
    _T11FcSpAuRejReasonCodeExp_Type()
)
t11FcSpAuRejReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpAuRejReasonCodeExp.setStatus("current")
_T11FcSpAuMIBConformance_ObjectIdentity = ObjectIdentity
t11FcSpAuMIBConformance = _T11FcSpAuMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 176, 2)
)
_T11FcSpAuMIBCompliances_ObjectIdentity = ObjectIdentity
t11FcSpAuMIBCompliances = _T11FcSpAuMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 176, 2, 1)
)
_T11FcSpAuMIBGroups_ObjectIdentity = ObjectIdentity
t11FcSpAuMIBGroups = _T11FcSpAuMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 176, 2, 2)
)
_T11FcSpAuMIBIdentities_ObjectIdentity = ObjectIdentity
t11FcSpAuMIBIdentities = _T11FcSpAuMIBIdentities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 176, 3)
)
_T11FcSpAuServerProtocolRadius_ObjectIdentity = ObjectIdentity
t11FcSpAuServerProtocolRadius = _T11FcSpAuServerProtocolRadius_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 176, 3, 1)
)
if mibBuilder.loadTexts:
    t11FcSpAuServerProtocolRadius.setStatus("current")
_T11FcSpAuServerProtocolDiameter_ObjectIdentity = ObjectIdentity
t11FcSpAuServerProtocolDiameter = _T11FcSpAuServerProtocolDiameter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 176, 3, 2)
)
if mibBuilder.loadTexts:
    t11FcSpAuServerProtocolDiameter.setStatus("current")
_T11FcSpAuServerProtocolTacacs_ObjectIdentity = ObjectIdentity
t11FcSpAuServerProtocolTacacs = _T11FcSpAuServerProtocolTacacs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 176, 3, 3)
)
if mibBuilder.loadTexts:
    t11FcSpAuServerProtocolTacacs.setStatus("current")

# Managed Objects groups

t11FcSpAuGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 176, 2, 2, 1)
)
t11FcSpAuGeneralGroup.setObjects(
      *(("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuServerProtocol"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuStorageType"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuSendRejNotifyEnable"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRcvRejNotifyEnable"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuDefaultLifetime"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuDefaultLifetimeUnits"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejectMaxRows"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuDhChapHashFunctions"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuDhChapDhGroups"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcapHashFunctions"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcapCertsSignFunctions"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcapDhGroups"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcpapHashFunctions"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcpapDhGroups"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatTimeouts"))
)
if mibBuilder.loadTexts:
    t11FcSpAuGeneralGroup.setStatus("current")

t11FcSpAuIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 176, 2, 2, 2)
)
t11FcSpAuIfStatsGroup.setObjects(
      *(("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatInAcceptedMsgs"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatInLsSwRejectedMsgs"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatInAuthRejectedMsgs"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatOutAcceptedMsgs"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatOutLsSwRejectedMsgs"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatOutAuthRejectedMsgs"))
)
if mibBuilder.loadTexts:
    t11FcSpAuIfStatsGroup.setStatus("current")

t11FcSpAuRejectedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 176, 2, 2, 3)
)
t11FcSpAuRejectedGroup.setObjects(
      *(("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejDirection"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejType"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejAuthMsgString"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCode"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCodeExp"))
)
if mibBuilder.loadTexts:
    t11FcSpAuRejectedGroup.setStatus("current")


# Notification objects

t11FcSpAuRejectSentNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 176, 0, 1)
)
t11FcSpAuRejectSentNotify.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejAuthMsgString"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejType"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCode"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCodeExp"))
)
if mibBuilder.loadTexts:
    t11FcSpAuRejectSentNotify.setStatus(
        "current"
    )

t11FcSpAuRejectReceivedNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 176, 0, 2)
)
t11FcSpAuRejectReceivedNotify.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejAuthMsgString"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejType"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCode"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCodeExp"))
)
if mibBuilder.loadTexts:
    t11FcSpAuRejectReceivedNotify.setStatus(
        "current"
    )


# Notifications groups

t11FcSpAuNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 176, 2, 2, 4)
)
t11FcSpAuNotificationGroup.setObjects(
      *(("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejectSentNotify"),
        ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejectReceivedNotify"))
)
if mibBuilder.loadTexts:
    t11FcSpAuNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11FcSpAuMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 176, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpAuMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-SP-AUTHENTICATION-MIB",
    **{"t11FcSpAuthenticationMIB": t11FcSpAuthenticationMIB,
       "t11FcSpAuMIBNotifications": t11FcSpAuMIBNotifications,
       "t11FcSpAuRejectSentNotify": t11FcSpAuRejectSentNotify,
       "t11FcSpAuRejectReceivedNotify": t11FcSpAuRejectReceivedNotify,
       "t11FcSpAuMIBObjects": t11FcSpAuMIBObjects,
       "t11FcSpAuEntityTable": t11FcSpAuEntityTable,
       "t11FcSpAuEntityEntry": t11FcSpAuEntityEntry,
       "t11FcSpAuEntityName": t11FcSpAuEntityName,
       "t11FcSpAuFabricIndex": t11FcSpAuFabricIndex,
       "t11FcSpAuServerProtocol": t11FcSpAuServerProtocol,
       "t11FcSpAuStorageType": t11FcSpAuStorageType,
       "t11FcSpAuSendRejNotifyEnable": t11FcSpAuSendRejNotifyEnable,
       "t11FcSpAuRcvRejNotifyEnable": t11FcSpAuRcvRejNotifyEnable,
       "t11FcSpAuDefaultLifetime": t11FcSpAuDefaultLifetime,
       "t11FcSpAuDefaultLifetimeUnits": t11FcSpAuDefaultLifetimeUnits,
       "t11FcSpAuRejectMaxRows": t11FcSpAuRejectMaxRows,
       "t11FcSpAuDhChapHashFunctions": t11FcSpAuDhChapHashFunctions,
       "t11FcSpAuDhChapDhGroups": t11FcSpAuDhChapDhGroups,
       "t11FcSpAuFcapHashFunctions": t11FcSpAuFcapHashFunctions,
       "t11FcSpAuFcapCertsSignFunctions": t11FcSpAuFcapCertsSignFunctions,
       "t11FcSpAuFcapDhGroups": t11FcSpAuFcapDhGroups,
       "t11FcSpAuFcpapHashFunctions": t11FcSpAuFcpapHashFunctions,
       "t11FcSpAuFcpapDhGroups": t11FcSpAuFcpapDhGroups,
       "t11FcSpAuIfStatTable": t11FcSpAuIfStatTable,
       "t11FcSpAuIfStatEntry": t11FcSpAuIfStatEntry,
       "t11FcSpAuIfStatInterfaceIndex": t11FcSpAuIfStatInterfaceIndex,
       "t11FcSpAuIfStatFabricIndex": t11FcSpAuIfStatFabricIndex,
       "t11FcSpAuIfStatTimeouts": t11FcSpAuIfStatTimeouts,
       "t11FcSpAuIfStatInAcceptedMsgs": t11FcSpAuIfStatInAcceptedMsgs,
       "t11FcSpAuIfStatInLsSwRejectedMsgs": t11FcSpAuIfStatInLsSwRejectedMsgs,
       "t11FcSpAuIfStatInAuthRejectedMsgs": t11FcSpAuIfStatInAuthRejectedMsgs,
       "t11FcSpAuIfStatOutAcceptedMsgs": t11FcSpAuIfStatOutAcceptedMsgs,
       "t11FcSpAuIfStatOutLsSwRejectedMsgs": t11FcSpAuIfStatOutLsSwRejectedMsgs,
       "t11FcSpAuIfStatOutAuthRejectedMsgs": t11FcSpAuIfStatOutAuthRejectedMsgs,
       "t11FcSpAuRejectTable": t11FcSpAuRejectTable,
       "t11FcSpAuRejectEntry": t11FcSpAuRejectEntry,
       "t11FcSpAuRejInterfaceIndex": t11FcSpAuRejInterfaceIndex,
       "t11FcSpAuRejFabricIndex": t11FcSpAuRejFabricIndex,
       "t11FcSpAuRejTimestamp": t11FcSpAuRejTimestamp,
       "t11FcSpAuRejDirection": t11FcSpAuRejDirection,
       "t11FcSpAuRejType": t11FcSpAuRejType,
       "t11FcSpAuRejAuthMsgString": t11FcSpAuRejAuthMsgString,
       "t11FcSpAuRejReasonCode": t11FcSpAuRejReasonCode,
       "t11FcSpAuRejReasonCodeExp": t11FcSpAuRejReasonCodeExp,
       "t11FcSpAuMIBConformance": t11FcSpAuMIBConformance,
       "t11FcSpAuMIBCompliances": t11FcSpAuMIBCompliances,
       "t11FcSpAuMIBCompliance": t11FcSpAuMIBCompliance,
       "t11FcSpAuMIBGroups": t11FcSpAuMIBGroups,
       "t11FcSpAuGeneralGroup": t11FcSpAuGeneralGroup,
       "t11FcSpAuIfStatsGroup": t11FcSpAuIfStatsGroup,
       "t11FcSpAuRejectedGroup": t11FcSpAuRejectedGroup,
       "t11FcSpAuNotificationGroup": t11FcSpAuNotificationGroup,
       "t11FcSpAuMIBIdentities": t11FcSpAuMIBIdentities,
       "t11FcSpAuServerProtocolRadius": t11FcSpAuServerProtocolRadius,
       "t11FcSpAuServerProtocolDiameter": t11FcSpAuServerProtocolDiameter,
       "t11FcSpAuServerProtocolTacacs": t11FcSpAuServerProtocolTacacs}
)
