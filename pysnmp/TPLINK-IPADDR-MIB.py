# SNMP MIB module (TPLINK-IPADDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-IPADDR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:10 2024
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

tplinkIpAddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6)
)
tplinkIpAddrMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TpInterfaceMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 3),
          ("dhcp", 2),
          ("manual", 1),
          ("none", 0))
    )



class TpInterfaceMode2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("none", 0))
    )



class TpPortLinkMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 0),
          ("route", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TplinkIpAddrMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIpAddrMIBObjects = _TplinkIpAddrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1)
)
_TpInterfaceConfig_ObjectIdentity = ObjectIdentity
tpInterfaceConfig = _TpInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1)
)
_TpVlanInterfaceTable_Object = MibTable
tpVlanInterfaceTable = _TpVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpVlanInterfaceTable.setStatus("current")
_TpVlanInterfaceConfigEntry_Object = MibTableRow
tpVlanInterfaceConfigEntry = _TpVlanInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 1, 1)
)
tpVlanInterfaceConfigEntry.setIndexNames(
    (0, "TPLINK-IPADDR-MIB", "tpVlanInterfaceVlanId"),
    (0, "TPLINK-IPADDR-MIB", "tpVlanInterfaceIp"),
    (0, "TPLINK-IPADDR-MIB", "tpVlanInterfaceSecondary"),
)
if mibBuilder.loadTexts:
    tpVlanInterfaceConfigEntry.setStatus("current")
_TpVlanInterfaceVlanId_Type = Integer32
_TpVlanInterfaceVlanId_Object = MibTableColumn
tpVlanInterfaceVlanId = _TpVlanInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 1, 1, 1),
    _TpVlanInterfaceVlanId_Type()
)
tpVlanInterfaceVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVlanInterfaceVlanId.setStatus("current")
_TpVlanInterfaceSecondary_Type = Integer32
_TpVlanInterfaceSecondary_Object = MibTableColumn
tpVlanInterfaceSecondary = _TpVlanInterfaceSecondary_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 1, 1, 2),
    _TpVlanInterfaceSecondary_Type()
)
tpVlanInterfaceSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVlanInterfaceSecondary.setStatus("current")
_TpVlanInterfaceMode_Type = TpInterfaceMode
_TpVlanInterfaceMode_Object = MibTableColumn
tpVlanInterfaceMode = _TpVlanInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 1, 1, 3),
    _TpVlanInterfaceMode_Type()
)
tpVlanInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVlanInterfaceMode.setStatus("current")
_TpVlanInterfaceIp_Type = IpAddress
_TpVlanInterfaceIp_Object = MibTableColumn
tpVlanInterfaceIp = _TpVlanInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 1, 1, 4),
    _TpVlanInterfaceIp_Type()
)
tpVlanInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVlanInterfaceIp.setStatus("current")
_TpVlanInterfaceMsk_Type = IpAddress
_TpVlanInterfaceMsk_Object = MibTableColumn
tpVlanInterfaceMsk = _TpVlanInterfaceMsk_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 1, 1, 5),
    _TpVlanInterfaceMsk_Type()
)
tpVlanInterfaceMsk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVlanInterfaceMsk.setStatus("current")


class _TpVlanInterfaceName_Type(OctetString):
    """Custom type tpVlanInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TpVlanInterfaceName_Type.__name__ = "OctetString"
_TpVlanInterfaceName_Object = MibTableColumn
tpVlanInterfaceName = _TpVlanInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 1, 1, 6),
    _TpVlanInterfaceName_Type()
)
tpVlanInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVlanInterfaceName.setStatus("current")
_TpVlanInterfaceStatus_Type = TPRowStatus
_TpVlanInterfaceStatus_Object = MibTableColumn
tpVlanInterfaceStatus = _TpVlanInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 1, 1, 7),
    _TpVlanInterfaceStatus_Type()
)
tpVlanInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVlanInterfaceStatus.setStatus("current")
_TpLoopbackInterfaceTable_Object = MibTable
tpLoopbackInterfaceTable = _TpLoopbackInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tpLoopbackInterfaceTable.setStatus("current")
_TpLoopbackInterfaceConfigEntry_Object = MibTableRow
tpLoopbackInterfaceConfigEntry = _TpLoopbackInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 2, 1)
)
tpLoopbackInterfaceConfigEntry.setIndexNames(
    (0, "TPLINK-IPADDR-MIB", "tpLoopbackInterfaceId"),
    (0, "TPLINK-IPADDR-MIB", "tpLoopbackInterfaceIp"),
    (0, "TPLINK-IPADDR-MIB", "tpLoopbackInterfaceSecondary"),
)
if mibBuilder.loadTexts:
    tpLoopbackInterfaceConfigEntry.setStatus("current")
_TpLoopbackInterfaceId_Type = Integer32
_TpLoopbackInterfaceId_Object = MibTableColumn
tpLoopbackInterfaceId = _TpLoopbackInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 2, 1, 1),
    _TpLoopbackInterfaceId_Type()
)
tpLoopbackInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLoopbackInterfaceId.setStatus("current")
_TpLoopbackInterfaceSecondary_Type = Integer32
_TpLoopbackInterfaceSecondary_Object = MibTableColumn
tpLoopbackInterfaceSecondary = _TpLoopbackInterfaceSecondary_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 2, 1, 2),
    _TpLoopbackInterfaceSecondary_Type()
)
tpLoopbackInterfaceSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLoopbackInterfaceSecondary.setStatus("current")
_TpLoopbackInterfaceMode_Type = TpInterfaceMode2
_TpLoopbackInterfaceMode_Object = MibTableColumn
tpLoopbackInterfaceMode = _TpLoopbackInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 2, 1, 3),
    _TpLoopbackInterfaceMode_Type()
)
tpLoopbackInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpLoopbackInterfaceMode.setStatus("current")
_TpLoopbackInterfaceIp_Type = IpAddress
_TpLoopbackInterfaceIp_Object = MibTableColumn
tpLoopbackInterfaceIp = _TpLoopbackInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 2, 1, 4),
    _TpLoopbackInterfaceIp_Type()
)
tpLoopbackInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLoopbackInterfaceIp.setStatus("current")
_TpLoopbackInterfaceMsk_Type = IpAddress
_TpLoopbackInterfaceMsk_Object = MibTableColumn
tpLoopbackInterfaceMsk = _TpLoopbackInterfaceMsk_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 2, 1, 5),
    _TpLoopbackInterfaceMsk_Type()
)
tpLoopbackInterfaceMsk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpLoopbackInterfaceMsk.setStatus("current")


class _TpLoopbackInterfaceName_Type(OctetString):
    """Custom type tpLoopbackInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TpLoopbackInterfaceName_Type.__name__ = "OctetString"
_TpLoopbackInterfaceName_Object = MibTableColumn
tpLoopbackInterfaceName = _TpLoopbackInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 2, 1, 6),
    _TpLoopbackInterfaceName_Type()
)
tpLoopbackInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpLoopbackInterfaceName.setStatus("current")
_TpLoopbackInterfaceStatus_Type = TPRowStatus
_TpLoopbackInterfaceStatus_Object = MibTableColumn
tpLoopbackInterfaceStatus = _TpLoopbackInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 2, 1, 7),
    _TpLoopbackInterfaceStatus_Type()
)
tpLoopbackInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpLoopbackInterfaceStatus.setStatus("current")
_TpRoutedPortTable_Object = MibTable
tpRoutedPortTable = _TpRoutedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tpRoutedPortTable.setStatus("current")
_TpRoutedPortConfigEntry_Object = MibTableRow
tpRoutedPortConfigEntry = _TpRoutedPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 3, 1)
)
tpRoutedPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TPLINK-IPADDR-MIB", "tpRoutedPortIp"),
    (0, "TPLINK-IPADDR-MIB", "tpRoutedPortSecondary"),
)
if mibBuilder.loadTexts:
    tpRoutedPortConfigEntry.setStatus("current")


class _TpRoutedPortId_Type(OctetString):
    """Custom type tpRoutedPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpRoutedPortId_Type.__name__ = "OctetString"
_TpRoutedPortId_Object = MibTableColumn
tpRoutedPortId = _TpRoutedPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 3, 1, 1),
    _TpRoutedPortId_Type()
)
tpRoutedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRoutedPortId.setStatus("current")
_TpRoutedPortSecondary_Type = Integer32
_TpRoutedPortSecondary_Object = MibTableColumn
tpRoutedPortSecondary = _TpRoutedPortSecondary_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 3, 1, 2),
    _TpRoutedPortSecondary_Type()
)
tpRoutedPortSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRoutedPortSecondary.setStatus("current")
_TpRoutedPortMode_Type = TpInterfaceMode
_TpRoutedPortMode_Object = MibTableColumn
tpRoutedPortMode = _TpRoutedPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 3, 1, 3),
    _TpRoutedPortMode_Type()
)
tpRoutedPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpRoutedPortMode.setStatus("current")
_TpRoutedPortIp_Type = IpAddress
_TpRoutedPortIp_Object = MibTableColumn
tpRoutedPortIp = _TpRoutedPortIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 3, 1, 4),
    _TpRoutedPortIp_Type()
)
tpRoutedPortIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRoutedPortIp.setStatus("current")
_TpRoutedPortMsk_Type = IpAddress
_TpRoutedPortMsk_Object = MibTableColumn
tpRoutedPortMsk = _TpRoutedPortMsk_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 3, 1, 5),
    _TpRoutedPortMsk_Type()
)
tpRoutedPortMsk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpRoutedPortMsk.setStatus("current")


class _TpRoutedPortName_Type(OctetString):
    """Custom type tpRoutedPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TpRoutedPortName_Type.__name__ = "OctetString"
_TpRoutedPortName_Object = MibTableColumn
tpRoutedPortName = _TpRoutedPortName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 3, 1, 6),
    _TpRoutedPortName_Type()
)
tpRoutedPortName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpRoutedPortName.setStatus("current")
_TpRoutedPortStatus_Type = TPRowStatus
_TpRoutedPortStatus_Object = MibTableColumn
tpRoutedPortStatus = _TpRoutedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 3, 1, 7),
    _TpRoutedPortStatus_Type()
)
tpRoutedPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpRoutedPortStatus.setStatus("current")
_TpPortChannelTable_Object = MibTable
tpPortChannelTable = _TpPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tpPortChannelTable.setStatus("current")
_TpPortChannelConfigEntry_Object = MibTableRow
tpPortChannelConfigEntry = _TpPortChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 4, 1)
)
tpPortChannelConfigEntry.setIndexNames(
    (0, "TPLINK-IPADDR-MIB", "tpPortChannelId"),
    (0, "TPLINK-IPADDR-MIB", "tpPortChannelIp"),
    (0, "TPLINK-IPADDR-MIB", "tpPortChannelSecondary"),
)
if mibBuilder.loadTexts:
    tpPortChannelConfigEntry.setStatus("current")
_TpPortChannelId_Type = Integer32
_TpPortChannelId_Object = MibTableColumn
tpPortChannelId = _TpPortChannelId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 4, 1, 1),
    _TpPortChannelId_Type()
)
tpPortChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortChannelId.setStatus("current")
_TpPortChannelSecondary_Type = Integer32
_TpPortChannelSecondary_Object = MibTableColumn
tpPortChannelSecondary = _TpPortChannelSecondary_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 4, 1, 2),
    _TpPortChannelSecondary_Type()
)
tpPortChannelSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortChannelSecondary.setStatus("current")
_TpPortChannelMode_Type = TpInterfaceMode
_TpPortChannelMode_Object = MibTableColumn
tpPortChannelMode = _TpPortChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 4, 1, 3),
    _TpPortChannelMode_Type()
)
tpPortChannelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPortChannelMode.setStatus("current")
_TpPortChannelIp_Type = IpAddress
_TpPortChannelIp_Object = MibTableColumn
tpPortChannelIp = _TpPortChannelIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 4, 1, 4),
    _TpPortChannelIp_Type()
)
tpPortChannelIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortChannelIp.setStatus("current")
_TpPortChannelMsk_Type = IpAddress
_TpPortChannelMsk_Object = MibTableColumn
tpPortChannelMsk = _TpPortChannelMsk_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 4, 1, 5),
    _TpPortChannelMsk_Type()
)
tpPortChannelMsk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPortChannelMsk.setStatus("current")


class _TpPortChannelName_Type(OctetString):
    """Custom type tpPortChannelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TpPortChannelName_Type.__name__ = "OctetString"
_TpPortChannelName_Object = MibTableColumn
tpPortChannelName = _TpPortChannelName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 4, 1, 6),
    _TpPortChannelName_Type()
)
tpPortChannelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPortChannelName.setStatus("current")
_TpPortChannelStatus_Type = TPRowStatus
_TpPortChannelStatus_Object = MibTableColumn
tpPortChannelStatus = _TpPortChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 1, 1, 4, 1, 7),
    _TpPortChannelStatus_Type()
)
tpPortChannelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpPortChannelStatus.setStatus("current")
_TplinkIpAddrNotifications_ObjectIdentity = ObjectIdentity
tplinkIpAddrNotifications = _TplinkIpAddrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 6, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IPADDR-MIB",
    **{"TpInterfaceMode": TpInterfaceMode,
       "TpInterfaceMode2": TpInterfaceMode2,
       "TpPortLinkMode": TpPortLinkMode,
       "tplinkIpAddrMIB": tplinkIpAddrMIB,
       "tplinkIpAddrMIBObjects": tplinkIpAddrMIBObjects,
       "tpInterfaceConfig": tpInterfaceConfig,
       "tpVlanInterfaceTable": tpVlanInterfaceTable,
       "tpVlanInterfaceConfigEntry": tpVlanInterfaceConfigEntry,
       "tpVlanInterfaceVlanId": tpVlanInterfaceVlanId,
       "tpVlanInterfaceSecondary": tpVlanInterfaceSecondary,
       "tpVlanInterfaceMode": tpVlanInterfaceMode,
       "tpVlanInterfaceIp": tpVlanInterfaceIp,
       "tpVlanInterfaceMsk": tpVlanInterfaceMsk,
       "tpVlanInterfaceName": tpVlanInterfaceName,
       "tpVlanInterfaceStatus": tpVlanInterfaceStatus,
       "tpLoopbackInterfaceTable": tpLoopbackInterfaceTable,
       "tpLoopbackInterfaceConfigEntry": tpLoopbackInterfaceConfigEntry,
       "tpLoopbackInterfaceId": tpLoopbackInterfaceId,
       "tpLoopbackInterfaceSecondary": tpLoopbackInterfaceSecondary,
       "tpLoopbackInterfaceMode": tpLoopbackInterfaceMode,
       "tpLoopbackInterfaceIp": tpLoopbackInterfaceIp,
       "tpLoopbackInterfaceMsk": tpLoopbackInterfaceMsk,
       "tpLoopbackInterfaceName": tpLoopbackInterfaceName,
       "tpLoopbackInterfaceStatus": tpLoopbackInterfaceStatus,
       "tpRoutedPortTable": tpRoutedPortTable,
       "tpRoutedPortConfigEntry": tpRoutedPortConfigEntry,
       "tpRoutedPortId": tpRoutedPortId,
       "tpRoutedPortSecondary": tpRoutedPortSecondary,
       "tpRoutedPortMode": tpRoutedPortMode,
       "tpRoutedPortIp": tpRoutedPortIp,
       "tpRoutedPortMsk": tpRoutedPortMsk,
       "tpRoutedPortName": tpRoutedPortName,
       "tpRoutedPortStatus": tpRoutedPortStatus,
       "tpPortChannelTable": tpPortChannelTable,
       "tpPortChannelConfigEntry": tpPortChannelConfigEntry,
       "tpPortChannelId": tpPortChannelId,
       "tpPortChannelSecondary": tpPortChannelSecondary,
       "tpPortChannelMode": tpPortChannelMode,
       "tpPortChannelIp": tpPortChannelIp,
       "tpPortChannelMsk": tpPortChannelMsk,
       "tpPortChannelName": tpPortChannelName,
       "tpPortChannelStatus": tpPortChannelStatus,
       "tplinkIpAddrNotifications": tplinkIpAddrNotifications}
)
