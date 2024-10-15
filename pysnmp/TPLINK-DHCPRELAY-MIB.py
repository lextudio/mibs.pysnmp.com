# SNMP MIB module (TPLINK-DHCPRELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-DHCPRELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:55 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkDhcpRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39)
)
tplinkDhcpRelayMIB.setRevisions(
        ("2012-12-17 11:21",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcpRelayMIBObjects = _TplinkDhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1)
)
_DhcpRelayGlobalConfig_ObjectIdentity = ObjectIdentity
dhcpRelayGlobalConfig = _DhcpRelayGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1)
)


class _DhcpRelayEnableState_Type(Integer32):
    """Custom type dhcpRelayEnableState based on Integer32"""
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


_DhcpRelayEnableState_Type.__name__ = "Integer32"
_DhcpRelayEnableState_Object = MibScalar
dhcpRelayEnableState = _DhcpRelayEnableState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1, 1),
    _DhcpRelayEnableState_Type()
)
dhcpRelayEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayEnableState.setStatus("current")


class _DhcpRelayOption82Support_Type(Integer32):
    """Custom type dhcpRelayOption82Support based on Integer32"""
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


_DhcpRelayOption82Support_Type.__name__ = "Integer32"
_DhcpRelayOption82Support_Object = MibScalar
dhcpRelayOption82Support = _DhcpRelayOption82Support_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1, 2),
    _DhcpRelayOption82Support_Type()
)
dhcpRelayOption82Support.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Support.setStatus("current")


class _DhcpRelayExistedOption82Field_Type(Integer32):
    """Custom type dhcpRelayExistedOption82Field based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("keep", 0),
          ("replace", 1))
    )


_DhcpRelayExistedOption82Field_Type.__name__ = "Integer32"
_DhcpRelayExistedOption82Field_Object = MibScalar
dhcpRelayExistedOption82Field = _DhcpRelayExistedOption82Field_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1, 3),
    _DhcpRelayExistedOption82Field_Type()
)
dhcpRelayExistedOption82Field.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayExistedOption82Field.setStatus("current")


class _DhcpRelayOption82Customization_Type(Integer32):
    """Custom type dhcpRelayOption82Customization based on Integer32"""
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


_DhcpRelayOption82Customization_Type.__name__ = "Integer32"
_DhcpRelayOption82Customization_Object = MibScalar
dhcpRelayOption82Customization = _DhcpRelayOption82Customization_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1, 4),
    _DhcpRelayOption82Customization_Type()
)
dhcpRelayOption82Customization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Customization.setStatus("current")


class _DhcpRelayOption82CircuitID_Type(OctetString):
    """Custom type dhcpRelayOption82CircuitID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DhcpRelayOption82CircuitID_Type.__name__ = "OctetString"
_DhcpRelayOption82CircuitID_Object = MibScalar
dhcpRelayOption82CircuitID = _DhcpRelayOption82CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1, 5),
    _DhcpRelayOption82CircuitID_Type()
)
dhcpRelayOption82CircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82CircuitID.setStatus("current")


class _DhcpRelayOption82RemoteID_Type(OctetString):
    """Custom type dhcpRelayOption82RemoteID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DhcpRelayOption82RemoteID_Type.__name__ = "OctetString"
_DhcpRelayOption82RemoteID_Object = MibScalar
dhcpRelayOption82RemoteID = _DhcpRelayOption82RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1, 6),
    _DhcpRelayOption82RemoteID_Type()
)
dhcpRelayOption82RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82RemoteID.setStatus("current")
_DhcpRelayServerConfig_ObjectIdentity = ObjectIdentity
dhcpRelayServerConfig = _DhcpRelayServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2)
)
_DhcpRelayServerVlanInterfaceTable_Object = MibTable
dhcpRelayServerVlanInterfaceTable = _DhcpRelayServerVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpRelayServerVlanInterfaceTable.setStatus("current")
_DhcpRelayServerVlanInterfaceEntry_Object = MibTableRow
dhcpRelayServerVlanInterfaceEntry = _DhcpRelayServerVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1, 1)
)
dhcpRelayServerVlanInterfaceEntry.setIndexNames(
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerVlanId"),
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerVlanInterfaceIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerVlanInterfaceEntry.setStatus("current")
_DhcpRelayServerVlanId_Type = Integer32
_DhcpRelayServerVlanId_Object = MibTableColumn
dhcpRelayServerVlanId = _DhcpRelayServerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1, 1, 1),
    _DhcpRelayServerVlanId_Type()
)
dhcpRelayServerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerVlanId.setStatus("current")
_DhcpRelayServerVlanInterfaceIp_Type = IpAddress
_DhcpRelayServerVlanInterfaceIp_Object = MibTableColumn
dhcpRelayServerVlanInterfaceIp = _DhcpRelayServerVlanInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1, 1, 2),
    _DhcpRelayServerVlanInterfaceIp_Type()
)
dhcpRelayServerVlanInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerVlanInterfaceIp.setStatus("current")
_DhcpRelayServerVlanInterfaceStatus_Type = TPRowStatus
_DhcpRelayServerVlanInterfaceStatus_Object = MibTableColumn
dhcpRelayServerVlanInterfaceStatus = _DhcpRelayServerVlanInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1, 1, 3),
    _DhcpRelayServerVlanInterfaceStatus_Type()
)
dhcpRelayServerVlanInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayServerVlanInterfaceStatus.setStatus("current")
_DhcpRelayServerLoopbackInterfaceTable_Object = MibTable
dhcpRelayServerLoopbackInterfaceTable = _DhcpRelayServerLoopbackInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dhcpRelayServerLoopbackInterfaceTable.setStatus("current")
_DhcpRelayServerLoopbackInterfaceEntry_Object = MibTableRow
dhcpRelayServerLoopbackInterfaceEntry = _DhcpRelayServerLoopbackInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 2, 1)
)
dhcpRelayServerLoopbackInterfaceEntry.setIndexNames(
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerLoopbackId"),
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerLoopbackInterfaceIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerLoopbackInterfaceEntry.setStatus("current")
_DhcpRelayServerLoopbackId_Type = Integer32
_DhcpRelayServerLoopbackId_Object = MibTableColumn
dhcpRelayServerLoopbackId = _DhcpRelayServerLoopbackId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 2, 1, 1),
    _DhcpRelayServerLoopbackId_Type()
)
dhcpRelayServerLoopbackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerLoopbackId.setStatus("current")
_DhcpRelayServerLoopbackInterfaceIp_Type = IpAddress
_DhcpRelayServerLoopbackInterfaceIp_Object = MibTableColumn
dhcpRelayServerLoopbackInterfaceIp = _DhcpRelayServerLoopbackInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 2, 1, 2),
    _DhcpRelayServerLoopbackInterfaceIp_Type()
)
dhcpRelayServerLoopbackInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerLoopbackInterfaceIp.setStatus("current")
_DhcpRelayServerLoopbackInterfaceStatus_Type = TPRowStatus
_DhcpRelayServerLoopbackInterfaceStatus_Object = MibTableColumn
dhcpRelayServerLoopbackInterfaceStatus = _DhcpRelayServerLoopbackInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 2, 1, 3),
    _DhcpRelayServerLoopbackInterfaceStatus_Type()
)
dhcpRelayServerLoopbackInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayServerLoopbackInterfaceStatus.setStatus("current")
_DhcpRelayServerRoutedPortInterfaceTable_Object = MibTable
dhcpRelayServerRoutedPortInterfaceTable = _DhcpRelayServerRoutedPortInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortInterfaceTable.setStatus("current")
_DhcpRelayServerRoutedPortInterfaceEntry_Object = MibTableRow
dhcpRelayServerRoutedPortInterfaceEntry = _DhcpRelayServerRoutedPortInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3, 1)
)
dhcpRelayServerRoutedPortInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerRoutedPortInterfaceIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortInterfaceEntry.setStatus("current")


class _DhcpRelayServerRoutedPortPortId_Type(OctetString):
    """Custom type dhcpRelayServerRoutedPortPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DhcpRelayServerRoutedPortPortId_Type.__name__ = "OctetString"
_DhcpRelayServerRoutedPortPortId_Object = MibTableColumn
dhcpRelayServerRoutedPortPortId = _DhcpRelayServerRoutedPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3, 1, 1),
    _DhcpRelayServerRoutedPortPortId_Type()
)
dhcpRelayServerRoutedPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortPortId.setStatus("current")
_DhcpRelayServerRoutedPortInterfaceIp_Type = IpAddress
_DhcpRelayServerRoutedPortInterfaceIp_Object = MibTableColumn
dhcpRelayServerRoutedPortInterfaceIp = _DhcpRelayServerRoutedPortInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3, 1, 2),
    _DhcpRelayServerRoutedPortInterfaceIp_Type()
)
dhcpRelayServerRoutedPortInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortInterfaceIp.setStatus("current")
_DhcpRelayServerRoutedPortInterfaceStatus_Type = TPRowStatus
_DhcpRelayServerRoutedPortInterfaceStatus_Object = MibTableColumn
dhcpRelayServerRoutedPortInterfaceStatus = _DhcpRelayServerRoutedPortInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3, 1, 3),
    _DhcpRelayServerRoutedPortInterfaceStatus_Type()
)
dhcpRelayServerRoutedPortInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortInterfaceStatus.setStatus("current")
_DhcpRelayServerPortChannelInterfaceTable_Object = MibTable
dhcpRelayServerPortChannelInterfaceTable = _DhcpRelayServerPortChannelInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelInterfaceTable.setStatus("current")
_DhcpRelayServerPortChannelInterfaceEntry_Object = MibTableRow
dhcpRelayServerPortChannelInterfaceEntry = _DhcpRelayServerPortChannelInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4, 1)
)
dhcpRelayServerPortChannelInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerPortChannelInterfaceIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelInterfaceEntry.setStatus("current")
_DhcpRelayServerPortChannelPortId_Type = Integer32
_DhcpRelayServerPortChannelPortId_Object = MibTableColumn
dhcpRelayServerPortChannelPortId = _DhcpRelayServerPortChannelPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4, 1, 1),
    _DhcpRelayServerPortChannelPortId_Type()
)
dhcpRelayServerPortChannelPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelPortId.setStatus("current")
_DhcpRelayServerPortChannelInterfaceIp_Type = IpAddress
_DhcpRelayServerPortChannelInterfaceIp_Object = MibTableColumn
dhcpRelayServerPortChannelInterfaceIp = _DhcpRelayServerPortChannelInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4, 1, 2),
    _DhcpRelayServerPortChannelInterfaceIp_Type()
)
dhcpRelayServerPortChannelInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelInterfaceIp.setStatus("current")
_DhcpRelayServerPortChannelInterfaceStatus_Type = TPRowStatus
_DhcpRelayServerPortChannelInterfaceStatus_Object = MibTableColumn
dhcpRelayServerPortChannelInterfaceStatus = _DhcpRelayServerPortChannelInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4, 1, 3),
    _DhcpRelayServerPortChannelInterfaceStatus_Type()
)
dhcpRelayServerPortChannelInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelInterfaceStatus.setStatus("current")
_TplinkDhcpRelayNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcpRelayNotifications = _TplinkDhcpRelayNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCPRELAY-MIB",
    **{"tplinkDhcpRelayMIB": tplinkDhcpRelayMIB,
       "tplinkDhcpRelayMIBObjects": tplinkDhcpRelayMIBObjects,
       "dhcpRelayGlobalConfig": dhcpRelayGlobalConfig,
       "dhcpRelayEnableState": dhcpRelayEnableState,
       "dhcpRelayOption82Support": dhcpRelayOption82Support,
       "dhcpRelayExistedOption82Field": dhcpRelayExistedOption82Field,
       "dhcpRelayOption82Customization": dhcpRelayOption82Customization,
       "dhcpRelayOption82CircuitID": dhcpRelayOption82CircuitID,
       "dhcpRelayOption82RemoteID": dhcpRelayOption82RemoteID,
       "dhcpRelayServerConfig": dhcpRelayServerConfig,
       "dhcpRelayServerVlanInterfaceTable": dhcpRelayServerVlanInterfaceTable,
       "dhcpRelayServerVlanInterfaceEntry": dhcpRelayServerVlanInterfaceEntry,
       "dhcpRelayServerVlanId": dhcpRelayServerVlanId,
       "dhcpRelayServerVlanInterfaceIp": dhcpRelayServerVlanInterfaceIp,
       "dhcpRelayServerVlanInterfaceStatus": dhcpRelayServerVlanInterfaceStatus,
       "dhcpRelayServerLoopbackInterfaceTable": dhcpRelayServerLoopbackInterfaceTable,
       "dhcpRelayServerLoopbackInterfaceEntry": dhcpRelayServerLoopbackInterfaceEntry,
       "dhcpRelayServerLoopbackId": dhcpRelayServerLoopbackId,
       "dhcpRelayServerLoopbackInterfaceIp": dhcpRelayServerLoopbackInterfaceIp,
       "dhcpRelayServerLoopbackInterfaceStatus": dhcpRelayServerLoopbackInterfaceStatus,
       "dhcpRelayServerRoutedPortInterfaceTable": dhcpRelayServerRoutedPortInterfaceTable,
       "dhcpRelayServerRoutedPortInterfaceEntry": dhcpRelayServerRoutedPortInterfaceEntry,
       "dhcpRelayServerRoutedPortPortId": dhcpRelayServerRoutedPortPortId,
       "dhcpRelayServerRoutedPortInterfaceIp": dhcpRelayServerRoutedPortInterfaceIp,
       "dhcpRelayServerRoutedPortInterfaceStatus": dhcpRelayServerRoutedPortInterfaceStatus,
       "dhcpRelayServerPortChannelInterfaceTable": dhcpRelayServerPortChannelInterfaceTable,
       "dhcpRelayServerPortChannelInterfaceEntry": dhcpRelayServerPortChannelInterfaceEntry,
       "dhcpRelayServerPortChannelPortId": dhcpRelayServerPortChannelPortId,
       "dhcpRelayServerPortChannelInterfaceIp": dhcpRelayServerPortChannelInterfaceIp,
       "dhcpRelayServerPortChannelInterfaceStatus": dhcpRelayServerPortChannelInterfaceStatus,
       "tplinkDhcpRelayNotifications": tplinkDhcpRelayNotifications}
)
