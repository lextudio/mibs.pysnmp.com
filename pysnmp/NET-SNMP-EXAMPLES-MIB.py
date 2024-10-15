# SNMP MIB module (NET-SNMP-EXAMPLES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NET-SNMP-EXAMPLES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:22 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(netSnmp,) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmp")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

netSnmpExamples = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 2)
)
netSnmpExamples.setRevisions(
        ("2004-06-15 00:00",
         "2002-02-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetSnmpExampleScalars_ObjectIdentity = ObjectIdentity
netSnmpExampleScalars = _NetSnmpExampleScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 2, 1)
)


class _NetSnmpExampleInteger_Type(Integer32):
    """Custom type netSnmpExampleInteger based on Integer32"""
    defaultValue = 42


_NetSnmpExampleInteger_Object = MibScalar
netSnmpExampleInteger = _NetSnmpExampleInteger_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 1, 1),
    _NetSnmpExampleInteger_Type()
)
netSnmpExampleInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSnmpExampleInteger.setStatus("current")


class _NetSnmpExampleSleeper_Type(Integer32):
    """Custom type netSnmpExampleSleeper based on Integer32"""
    defaultValue = 1


_NetSnmpExampleSleeper_Object = MibScalar
netSnmpExampleSleeper = _NetSnmpExampleSleeper_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 1, 2),
    _NetSnmpExampleSleeper_Type()
)
netSnmpExampleSleeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSnmpExampleSleeper.setStatus("current")


class _NetSnmpExampleString_Type(SnmpAdminString):
    """Custom type netSnmpExampleString based on SnmpAdminString"""
    defaultValue = OctetString("So long, and thanks for all the fish!")


_NetSnmpExampleString_Object = MibScalar
netSnmpExampleString = _NetSnmpExampleString_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 1, 3),
    _NetSnmpExampleString_Type()
)
netSnmpExampleString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSnmpExampleString.setStatus("current")
_NetSnmpExampleTables_ObjectIdentity = ObjectIdentity
netSnmpExampleTables = _NetSnmpExampleTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2)
)
_NetSnmpIETFWGTable_Object = MibTable
netSnmpIETFWGTable = _NetSnmpIETFWGTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 1)
)
if mibBuilder.loadTexts:
    netSnmpIETFWGTable.setStatus("current")
_NetSnmpIETFWGEntry_Object = MibTableRow
netSnmpIETFWGEntry = _NetSnmpIETFWGEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1)
)
netSnmpIETFWGEntry.setIndexNames(
    (0, "NET-SNMP-EXAMPLES-MIB", "nsIETFWGName"),
)
if mibBuilder.loadTexts:
    netSnmpIETFWGEntry.setStatus("current")


class _NsIETFWGName_Type(OctetString):
    """Custom type nsIETFWGName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NsIETFWGName_Type.__name__ = "OctetString"
_NsIETFWGName_Object = MibTableColumn
nsIETFWGName = _NsIETFWGName_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1, 1),
    _NsIETFWGName_Type()
)
nsIETFWGName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsIETFWGName.setStatus("current")
_NsIETFWGChair1_Type = OctetString
_NsIETFWGChair1_Object = MibTableColumn
nsIETFWGChair1 = _NsIETFWGChair1_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1, 2),
    _NsIETFWGChair1_Type()
)
nsIETFWGChair1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsIETFWGChair1.setStatus("current")
_NsIETFWGChair2_Type = OctetString
_NsIETFWGChair2_Object = MibTableColumn
nsIETFWGChair2 = _NsIETFWGChair2_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1, 3),
    _NsIETFWGChair2_Type()
)
nsIETFWGChair2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsIETFWGChair2.setStatus("current")
_NetSnmpHostsTable_Object = MibTable
netSnmpHostsTable = _NetSnmpHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 2)
)
if mibBuilder.loadTexts:
    netSnmpHostsTable.setStatus("current")
_NetSnmpHostsEntry_Object = MibTableRow
netSnmpHostsEntry = _NetSnmpHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1)
)
netSnmpHostsEntry.setIndexNames(
    (0, "NET-SNMP-EXAMPLES-MIB", "netSnmpHostName"),
)
if mibBuilder.loadTexts:
    netSnmpHostsEntry.setStatus("current")


class _NetSnmpHostName_Type(OctetString):
    """Custom type netSnmpHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NetSnmpHostName_Type.__name__ = "OctetString"
_NetSnmpHostName_Object = MibTableColumn
netSnmpHostName = _NetSnmpHostName_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 1),
    _NetSnmpHostName_Type()
)
netSnmpHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netSnmpHostName.setStatus("current")
_NetSnmpHostAddressType_Type = InetAddressType
_NetSnmpHostAddressType_Object = MibTableColumn
netSnmpHostAddressType = _NetSnmpHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 2),
    _NetSnmpHostAddressType_Type()
)
netSnmpHostAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netSnmpHostAddressType.setStatus("current")
_NetSnmpHostAddress_Type = InetAddress
_NetSnmpHostAddress_Object = MibTableColumn
netSnmpHostAddress = _NetSnmpHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 3),
    _NetSnmpHostAddress_Type()
)
netSnmpHostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netSnmpHostAddress.setStatus("current")


class _NetSnmpHostStorage_Type(StorageType):
    """Custom type netSnmpHostStorage based on StorageType"""


_NetSnmpHostStorage_Object = MibTableColumn
netSnmpHostStorage = _NetSnmpHostStorage_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 4),
    _NetSnmpHostStorage_Type()
)
netSnmpHostStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netSnmpHostStorage.setStatus("current")
_NetSnmpHostRowStatus_Type = RowStatus
_NetSnmpHostRowStatus_Object = MibTableColumn
netSnmpHostRowStatus = _NetSnmpHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 5),
    _NetSnmpHostRowStatus_Type()
)
netSnmpHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netSnmpHostRowStatus.setStatus("current")
_NetSnmpExampleNotifications_ObjectIdentity = ObjectIdentity
netSnmpExampleNotifications = _NetSnmpExampleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 2, 3)
)
_NetSnmpExampleNotificationPrefix_ObjectIdentity = ObjectIdentity
netSnmpExampleNotificationPrefix = _NetSnmpExampleNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 2, 3, 0)
)
_NetSnmpExampleNotification_Type = SnmpAdminString
_NetSnmpExampleNotification_Object = MibScalar
netSnmpExampleNotification = _NetSnmpExampleNotification_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 3, 1),
    _NetSnmpExampleNotification_Type()
)
netSnmpExampleNotification.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    netSnmpExampleNotification.setStatus("obsolete")
_NetSnmpExampleNotificationObjects_ObjectIdentity = ObjectIdentity
netSnmpExampleNotificationObjects = _NetSnmpExampleNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 2, 3, 2)
)
_NetSnmpExampleHeartbeatRate_Type = Integer32
_NetSnmpExampleHeartbeatRate_Object = MibScalar
netSnmpExampleHeartbeatRate = _NetSnmpExampleHeartbeatRate_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 3, 2, 1),
    _NetSnmpExampleHeartbeatRate_Type()
)
netSnmpExampleHeartbeatRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    netSnmpExampleHeartbeatRate.setStatus("current")
_NetSnmpExampleHeartbeatName_Type = SnmpAdminString
_NetSnmpExampleHeartbeatName_Object = MibScalar
netSnmpExampleHeartbeatName = _NetSnmpExampleHeartbeatName_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 3, 2, 2),
    _NetSnmpExampleHeartbeatName_Type()
)
netSnmpExampleHeartbeatName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    netSnmpExampleHeartbeatName.setStatus("current")

# Managed Objects groups


# Notification objects

netSnmpExampleHeartbeatNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8072, 2, 3, 0, 1)
)
netSnmpExampleHeartbeatNotification.setObjects(
    ("NET-SNMP-EXAMPLES-MIB", "netSnmpExampleHeartbeatRate")
)
if mibBuilder.loadTexts:
    netSnmpExampleHeartbeatNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-EXAMPLES-MIB",
    **{"netSnmpExamples": netSnmpExamples,
       "netSnmpExampleScalars": netSnmpExampleScalars,
       "netSnmpExampleInteger": netSnmpExampleInteger,
       "netSnmpExampleSleeper": netSnmpExampleSleeper,
       "netSnmpExampleString": netSnmpExampleString,
       "netSnmpExampleTables": netSnmpExampleTables,
       "netSnmpIETFWGTable": netSnmpIETFWGTable,
       "netSnmpIETFWGEntry": netSnmpIETFWGEntry,
       "nsIETFWGName": nsIETFWGName,
       "nsIETFWGChair1": nsIETFWGChair1,
       "nsIETFWGChair2": nsIETFWGChair2,
       "netSnmpHostsTable": netSnmpHostsTable,
       "netSnmpHostsEntry": netSnmpHostsEntry,
       "netSnmpHostName": netSnmpHostName,
       "netSnmpHostAddressType": netSnmpHostAddressType,
       "netSnmpHostAddress": netSnmpHostAddress,
       "netSnmpHostStorage": netSnmpHostStorage,
       "netSnmpHostRowStatus": netSnmpHostRowStatus,
       "netSnmpExampleNotifications": netSnmpExampleNotifications,
       "netSnmpExampleNotificationPrefix": netSnmpExampleNotificationPrefix,
       "netSnmpExampleHeartbeatNotification": netSnmpExampleHeartbeatNotification,
       "netSnmpExampleNotification": netSnmpExampleNotification,
       "netSnmpExampleNotificationObjects": netSnmpExampleNotificationObjects,
       "netSnmpExampleHeartbeatRate": netSnmpExampleHeartbeatRate,
       "netSnmpExampleHeartbeatName": netSnmpExampleHeartbeatName}
)
