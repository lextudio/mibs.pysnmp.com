# SNMP MIB module (ZYXEL-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-DHCP-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:33 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelDhcpRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDhcpRelaySetup_ObjectIdentity = ObjectIdentity
zyxelDhcpRelaySetup = _ZyxelDhcpRelaySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1)
)
_ZyxelDhcpRelayGlobalRelay_ObjectIdentity = ObjectIdentity
zyxelDhcpRelayGlobalRelay = _ZyxelDhcpRelayGlobalRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1)
)
_ZyDhcpRelayGlobalRelayState_Type = EnabledStatus
_ZyDhcpRelayGlobalRelayState_Object = MibScalar
zyDhcpRelayGlobalRelayState = _ZyDhcpRelayGlobalRelayState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 1),
    _ZyDhcpRelayGlobalRelayState_Type()
)
zyDhcpRelayGlobalRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpRelayGlobalRelayState.setStatus("current")
_ZyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers_Type = Integer32
_ZyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers_Object = MibScalar
zyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers = _ZyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 2),
    _ZyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers_Type()
)
zyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers.setStatus("current")
_ZyxelDhcpRelayGlobalRelayRemoteServerTable_Object = MibTable
zyxelDhcpRelayGlobalRelayRemoteServerTable = _ZyxelDhcpRelayGlobalRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayGlobalRelayRemoteServerTable.setStatus("current")
_ZyxelDhcpRelayGlobalRelayRemoteServerEntry_Object = MibTableRow
zyxelDhcpRelayGlobalRelayRemoteServerEntry = _ZyxelDhcpRelayGlobalRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 3, 1)
)
zyxelDhcpRelayGlobalRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayGlobalRelayRemoteServerIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayGlobalRelayRemoteServerEntry.setStatus("current")
_ZyDhcpRelayGlobalRelayRemoteServerIpAddress_Type = IpAddress
_ZyDhcpRelayGlobalRelayRemoteServerIpAddress_Object = MibTableColumn
zyDhcpRelayGlobalRelayRemoteServerIpAddress = _ZyDhcpRelayGlobalRelayRemoteServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 3, 1, 1),
    _ZyDhcpRelayGlobalRelayRemoteServerIpAddress_Type()
)
zyDhcpRelayGlobalRelayRemoteServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDhcpRelayGlobalRelayRemoteServerIpAddress.setStatus("current")
_ZyDhcpRelayGlobalRelayRemoteServerRowStatus_Type = RowStatus
_ZyDhcpRelayGlobalRelayRemoteServerRowStatus_Object = MibTableColumn
zyDhcpRelayGlobalRelayRemoteServerRowStatus = _ZyDhcpRelayGlobalRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 3, 1, 2),
    _ZyDhcpRelayGlobalRelayRemoteServerRowStatus_Type()
)
zyDhcpRelayGlobalRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyDhcpRelayGlobalRelayRemoteServerRowStatus.setStatus("current")
_ZyDhcpRelayGlobalRelayOption82Profile_Type = DisplayString
_ZyDhcpRelayGlobalRelayOption82Profile_Object = MibScalar
zyDhcpRelayGlobalRelayOption82Profile = _ZyDhcpRelayGlobalRelayOption82Profile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 4),
    _ZyDhcpRelayGlobalRelayOption82Profile_Type()
)
zyDhcpRelayGlobalRelayOption82Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpRelayGlobalRelayOption82Profile.setStatus("current")
_ZyDhcpRelayGlobalRelayMaxNumberOfOption82Port_Type = Integer32
_ZyDhcpRelayGlobalRelayMaxNumberOfOption82Port_Object = MibScalar
zyDhcpRelayGlobalRelayMaxNumberOfOption82Port = _ZyDhcpRelayGlobalRelayMaxNumberOfOption82Port_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 5),
    _ZyDhcpRelayGlobalRelayMaxNumberOfOption82Port_Type()
)
zyDhcpRelayGlobalRelayMaxNumberOfOption82Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpRelayGlobalRelayMaxNumberOfOption82Port.setStatus("current")
_ZyxelDhcpRelayGlobalRelayOption82PortTable_Object = MibTable
zyxelDhcpRelayGlobalRelayOption82PortTable = _ZyxelDhcpRelayGlobalRelayOption82PortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayGlobalRelayOption82PortTable.setStatus("current")
_ZyxelDhcpRelayGlobalRelayOption82PortEntry_Object = MibTableRow
zyxelDhcpRelayGlobalRelayOption82PortEntry = _ZyxelDhcpRelayGlobalRelayOption82PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 6, 1)
)
zyxelDhcpRelayGlobalRelayOption82PortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayGlobalRelayOption82PortEntry.setStatus("current")
_ZyDhcpRelayGlobalRelayOption82PortProfile_Type = DisplayString
_ZyDhcpRelayGlobalRelayOption82PortProfile_Object = MibTableColumn
zyDhcpRelayGlobalRelayOption82PortProfile = _ZyDhcpRelayGlobalRelayOption82PortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 6, 1, 1),
    _ZyDhcpRelayGlobalRelayOption82PortProfile_Type()
)
zyDhcpRelayGlobalRelayOption82PortProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyDhcpRelayGlobalRelayOption82PortProfile.setStatus("current")
_ZyxelDhcpRelayVlanRelay_ObjectIdentity = ObjectIdentity
zyxelDhcpRelayVlanRelay = _ZyxelDhcpRelayVlanRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2)
)
_ZyDhcpRelayVlanRelayMaxNumberOfRelays_Type = Integer32
_ZyDhcpRelayVlanRelayMaxNumberOfRelays_Object = MibScalar
zyDhcpRelayVlanRelayMaxNumberOfRelays = _ZyDhcpRelayVlanRelayMaxNumberOfRelays_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 1),
    _ZyDhcpRelayVlanRelayMaxNumberOfRelays_Type()
)
zyDhcpRelayVlanRelayMaxNumberOfRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpRelayVlanRelayMaxNumberOfRelays.setStatus("current")
_ZyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers_Type = Integer32
_ZyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers_Object = MibScalar
zyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers = _ZyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 2),
    _ZyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers_Type()
)
zyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers.setStatus("current")
_ZyxelDhcpRelayVlanRelayRemoteServerTable_Object = MibTable
zyxelDhcpRelayVlanRelayRemoteServerTable = _ZyxelDhcpRelayVlanRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayVlanRelayRemoteServerTable.setStatus("current")
_ZyxelDhcpRelayVlanRelayRemoteServerEntry_Object = MibTableRow
zyxelDhcpRelayVlanRelayRemoteServerEntry = _ZyxelDhcpRelayVlanRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3, 1)
)
zyxelDhcpRelayVlanRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayVlanRelayRemoteServerServeVid"),
    (0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayVlanRelayRemoteServerIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayVlanRelayRemoteServerEntry.setStatus("current")
_ZyDhcpRelayVlanRelayRemoteServerServeVid_Type = Integer32
_ZyDhcpRelayVlanRelayRemoteServerServeVid_Object = MibTableColumn
zyDhcpRelayVlanRelayRemoteServerServeVid = _ZyDhcpRelayVlanRelayRemoteServerServeVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3, 1, 1),
    _ZyDhcpRelayVlanRelayRemoteServerServeVid_Type()
)
zyDhcpRelayVlanRelayRemoteServerServeVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDhcpRelayVlanRelayRemoteServerServeVid.setStatus("current")
_ZyDhcpRelayVlanRelayRemoteServerIpAddress_Type = IpAddress
_ZyDhcpRelayVlanRelayRemoteServerIpAddress_Object = MibTableColumn
zyDhcpRelayVlanRelayRemoteServerIpAddress = _ZyDhcpRelayVlanRelayRemoteServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3, 1, 2),
    _ZyDhcpRelayVlanRelayRemoteServerIpAddress_Type()
)
zyDhcpRelayVlanRelayRemoteServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDhcpRelayVlanRelayRemoteServerIpAddress.setStatus("current")
_ZyDhcpRelayVlanRelayRemoteServerRowStatus_Type = RowStatus
_ZyDhcpRelayVlanRelayRemoteServerRowStatus_Object = MibTableColumn
zyDhcpRelayVlanRelayRemoteServerRowStatus = _ZyDhcpRelayVlanRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3, 1, 3),
    _ZyDhcpRelayVlanRelayRemoteServerRowStatus_Type()
)
zyDhcpRelayVlanRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyDhcpRelayVlanRelayRemoteServerRowStatus.setStatus("current")
_ZyxelDhcpRelayVlanRelayTable_Object = MibTable
zyxelDhcpRelayVlanRelayTable = _ZyxelDhcpRelayVlanRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayVlanRelayTable.setStatus("current")
_ZyxelDhcpRelayVlanRelayEntry_Object = MibTableRow
zyxelDhcpRelayVlanRelayEntry = _ZyxelDhcpRelayVlanRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 4, 1)
)
zyxelDhcpRelayVlanRelayEntry.setIndexNames(
    (0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayVlanRelayRemoteServerServeVid"),
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayVlanRelayEntry.setStatus("current")
_ZyDhcpRelayVlanRelayOption82Profile_Type = DisplayString
_ZyDhcpRelayVlanRelayOption82Profile_Object = MibTableColumn
zyDhcpRelayVlanRelayOption82Profile = _ZyDhcpRelayVlanRelayOption82Profile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 4, 1, 1),
    _ZyDhcpRelayVlanRelayOption82Profile_Type()
)
zyDhcpRelayVlanRelayOption82Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpRelayVlanRelayOption82Profile.setStatus("current")
_ZyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort_Type = Integer32
_ZyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort_Object = MibScalar
zyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort = _ZyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 5),
    _ZyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort_Type()
)
zyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort.setStatus("current")
_ZyxelDhcpRelayVlanRelayOption82VlanPortTable_Object = MibTable
zyxelDhcpRelayVlanRelayOption82VlanPortTable = _ZyxelDhcpRelayVlanRelayOption82VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 6)
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayVlanRelayOption82VlanPortTable.setStatus("current")
_ZyxelDhcpRelayVlanRelayOption82VlanPortEntry_Object = MibTableRow
zyxelDhcpRelayVlanRelayOption82VlanPortEntry = _ZyxelDhcpRelayVlanRelayOption82VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 6, 1)
)
zyxelDhcpRelayVlanRelayOption82VlanPortEntry.setIndexNames(
    (0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayVlanRelayRemoteServerServeVid"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelDhcpRelayVlanRelayOption82VlanPortEntry.setStatus("current")
_ZyDhcpRelayVlanRelayOption82VlanPortProfile_Type = DisplayString
_ZyDhcpRelayVlanRelayOption82VlanPortProfile_Object = MibTableColumn
zyDhcpRelayVlanRelayOption82VlanPortProfile = _ZyDhcpRelayVlanRelayOption82VlanPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 6, 1, 1),
    _ZyDhcpRelayVlanRelayOption82VlanPortProfile_Type()
)
zyDhcpRelayVlanRelayOption82VlanPortProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyDhcpRelayVlanRelayOption82VlanPortProfile.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DHCP-RELAY-MIB",
    **{"zyxelDhcpRelay": zyxelDhcpRelay,
       "zyxelDhcpRelaySetup": zyxelDhcpRelaySetup,
       "zyxelDhcpRelayGlobalRelay": zyxelDhcpRelayGlobalRelay,
       "zyDhcpRelayGlobalRelayState": zyDhcpRelayGlobalRelayState,
       "zyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers": zyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers,
       "zyxelDhcpRelayGlobalRelayRemoteServerTable": zyxelDhcpRelayGlobalRelayRemoteServerTable,
       "zyxelDhcpRelayGlobalRelayRemoteServerEntry": zyxelDhcpRelayGlobalRelayRemoteServerEntry,
       "zyDhcpRelayGlobalRelayRemoteServerIpAddress": zyDhcpRelayGlobalRelayRemoteServerIpAddress,
       "zyDhcpRelayGlobalRelayRemoteServerRowStatus": zyDhcpRelayGlobalRelayRemoteServerRowStatus,
       "zyDhcpRelayGlobalRelayOption82Profile": zyDhcpRelayGlobalRelayOption82Profile,
       "zyDhcpRelayGlobalRelayMaxNumberOfOption82Port": zyDhcpRelayGlobalRelayMaxNumberOfOption82Port,
       "zyxelDhcpRelayGlobalRelayOption82PortTable": zyxelDhcpRelayGlobalRelayOption82PortTable,
       "zyxelDhcpRelayGlobalRelayOption82PortEntry": zyxelDhcpRelayGlobalRelayOption82PortEntry,
       "zyDhcpRelayGlobalRelayOption82PortProfile": zyDhcpRelayGlobalRelayOption82PortProfile,
       "zyxelDhcpRelayVlanRelay": zyxelDhcpRelayVlanRelay,
       "zyDhcpRelayVlanRelayMaxNumberOfRelays": zyDhcpRelayVlanRelayMaxNumberOfRelays,
       "zyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers": zyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers,
       "zyxelDhcpRelayVlanRelayRemoteServerTable": zyxelDhcpRelayVlanRelayRemoteServerTable,
       "zyxelDhcpRelayVlanRelayRemoteServerEntry": zyxelDhcpRelayVlanRelayRemoteServerEntry,
       "zyDhcpRelayVlanRelayRemoteServerServeVid": zyDhcpRelayVlanRelayRemoteServerServeVid,
       "zyDhcpRelayVlanRelayRemoteServerIpAddress": zyDhcpRelayVlanRelayRemoteServerIpAddress,
       "zyDhcpRelayVlanRelayRemoteServerRowStatus": zyDhcpRelayVlanRelayRemoteServerRowStatus,
       "zyxelDhcpRelayVlanRelayTable": zyxelDhcpRelayVlanRelayTable,
       "zyxelDhcpRelayVlanRelayEntry": zyxelDhcpRelayVlanRelayEntry,
       "zyDhcpRelayVlanRelayOption82Profile": zyDhcpRelayVlanRelayOption82Profile,
       "zyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort": zyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort,
       "zyxelDhcpRelayVlanRelayOption82VlanPortTable": zyxelDhcpRelayVlanRelayOption82VlanPortTable,
       "zyxelDhcpRelayVlanRelayOption82VlanPortEntry": zyxelDhcpRelayVlanRelayOption82VlanPortEntry,
       "zyDhcpRelayVlanRelayOption82VlanPortProfile": zyDhcpRelayVlanRelayOption82VlanPortProfile}
)
