# SNMP MIB module (ZHNFIREWALL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNFIREWALL
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:58 2024
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

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(lanDeviceIndex,
 lanEthernetIndex) = mibBuilder.importSymbols(
    "ZHNLANDEVICE",
    "lanDeviceIndex",
    "lanEthernetIndex")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhnFirewall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45)
)
zhnFirewall.setRevisions(
        ("2012-04-18 12:00",
         "2012-02-03 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FirewallMgmtAccessServiceValues(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("https", 2),
          ("ping", 3),
          ("snmp", 4),
          ("snmpTrap", 5),
          ("ssh", 6),
          ("telnet", 7))
    )



class FirewallMgmtAccessServiceActions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("undefined", 3))
    )



class FirewallPortTypeValues(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dmz", 3),
          ("portRange", 1),
          ("portRemap", 2))
    )



class FirewallPortProtocolValues(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 4),
          ("icmpv4", 5),
          ("none", 6),
          ("tcp", 1),
          ("tcpOrUdp", 3),
          ("udp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ZhnFirewallObjects_ObjectIdentity = ObjectIdentity
zhnFirewallObjects = _ZhnFirewallObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1)
)
_FirewallMgmtAccessTable_Object = MibTable
firewallMgmtAccessTable = _FirewallMgmtAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1)
)
if mibBuilder.loadTexts:
    firewallMgmtAccessTable.setStatus("current")
_FirewallMgmtAccessEntry_Object = MibTableRow
firewallMgmtAccessEntry = _FirewallMgmtAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1)
)
firewallMgmtAccessEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "lanEthernetIndex"),
    (0, "ZHNFIREWALL", "firewallMgmtServiceIndex"),
)
if mibBuilder.loadTexts:
    firewallMgmtAccessEntry.setStatus("current")
_FirewallMgmtServiceIndex_Type = FirewallMgmtAccessServiceValues
_FirewallMgmtServiceIndex_Object = MibTableColumn
firewallMgmtServiceIndex = _FirewallMgmtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1, 1),
    _FirewallMgmtServiceIndex_Type()
)
firewallMgmtServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    firewallMgmtServiceIndex.setStatus("current")
_FirewallMgmtService_Type = OctetString
_FirewallMgmtService_Object = MibTableColumn
firewallMgmtService = _FirewallMgmtService_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1, 2),
    _FirewallMgmtService_Type()
)
firewallMgmtService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallMgmtService.setStatus("current")
_FirewallMgmtAction_Type = FirewallMgmtAccessServiceActions
_FirewallMgmtAction_Object = MibTableColumn
firewallMgmtAction = _FirewallMgmtAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1, 3),
    _FirewallMgmtAction_Type()
)
firewallMgmtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallMgmtAction.setStatus("current")
_FirewallPortForwardingTable_Object = MibTable
firewallPortForwardingTable = _FirewallPortForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2)
)
if mibBuilder.loadTexts:
    firewallPortForwardingTable.setStatus("current")
_FirewallPortForwardingEntry_Object = MibTableRow
firewallPortForwardingEntry = _FirewallPortForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1)
)
firewallPortForwardingEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "lanEthernetIndex"),
    (0, "ZHNFIREWALL", "firewallPortForwardingIndex"),
)
if mibBuilder.loadTexts:
    firewallPortForwardingEntry.setStatus("current")
_FirewallPortForwardingIndex_Type = Unsigned32
_FirewallPortForwardingIndex_Object = MibTableColumn
firewallPortForwardingIndex = _FirewallPortForwardingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 1),
    _FirewallPortForwardingIndex_Type()
)
firewallPortForwardingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    firewallPortForwardingIndex.setStatus("current")
_FirewallPortForwardingName_Type = OctetString
_FirewallPortForwardingName_Object = MibTableColumn
firewallPortForwardingName = _FirewallPortForwardingName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 2),
    _FirewallPortForwardingName_Type()
)
firewallPortForwardingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallPortForwardingName.setStatus("current")
_FirewallPortType_Type = FirewallPortTypeValues
_FirewallPortType_Object = MibTableColumn
firewallPortType = _FirewallPortType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 3),
    _FirewallPortType_Type()
)
firewallPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallPortType.setStatus("current")
_FirewallPortProtocol_Type = FirewallPortProtocolValues
_FirewallPortProtocol_Object = MibTableColumn
firewallPortProtocol = _FirewallPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 4),
    _FirewallPortProtocol_Type()
)
firewallPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallPortProtocol.setStatus("current")
_FirewallPortPublicPortStart_Type = Unsigned32
_FirewallPortPublicPortStart_Object = MibTableColumn
firewallPortPublicPortStart = _FirewallPortPublicPortStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 5),
    _FirewallPortPublicPortStart_Type()
)
firewallPortPublicPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallPortPublicPortStart.setStatus("current")
_FirewallPortPublicPortEnd_Type = Unsigned32
_FirewallPortPublicPortEnd_Object = MibTableColumn
firewallPortPublicPortEnd = _FirewallPortPublicPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 6),
    _FirewallPortPublicPortEnd_Type()
)
firewallPortPublicPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallPortPublicPortEnd.setStatus("current")
_FirewallPortPrivatePort_Type = Unsigned32
_FirewallPortPrivatePort_Object = MibTableColumn
firewallPortPrivatePort = _FirewallPortPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 7),
    _FirewallPortPrivatePort_Type()
)
firewallPortPrivatePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallPortPrivatePort.setStatus("current")
_FirewallPortPrivateIPAddress_Type = IpAddress
_FirewallPortPrivateIPAddress_Object = MibTableColumn
firewallPortPrivateIPAddress = _FirewallPortPrivateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 8),
    _FirewallPortPrivateIPAddress_Type()
)
firewallPortPrivateIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallPortPrivateIPAddress.setStatus("current")
_FirewallPortForwardingRowStatus_Type = ZhoneRowStatus
_FirewallPortForwardingRowStatus_Object = MibTableColumn
firewallPortForwardingRowStatus = _FirewallPortForwardingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 9),
    _FirewallPortForwardingRowStatus_Type()
)
firewallPortForwardingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallPortForwardingRowStatus.setStatus("current")
_ZhnFirewallConformance_ObjectIdentity = ObjectIdentity
zhnFirewallConformance = _ZhnFirewallConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3)
)
_ZhnFirewallGroups_ObjectIdentity = ObjectIdentity
zhnFirewallGroups = _ZhnFirewallGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 1)
)
_ZhnFirewallCompliances_ObjectIdentity = ObjectIdentity
zhnFirewallCompliances = _ZhnFirewallCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 2)
)

# Managed Objects groups

zhnFirewallMgmtAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 1, 1)
)
zhnFirewallMgmtAccessGroup.setObjects(
      *(("ZHNFIREWALL", "firewallMgmtService"),
        ("ZHNFIREWALL", "firewallMgmtAction"))
)
if mibBuilder.loadTexts:
    zhnFirewallMgmtAccessGroup.setStatus("current")

zhnFirewallPortForwardingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 1, 2)
)
zhnFirewallPortForwardingGroup.setObjects(
      *(("ZHNFIREWALL", "firewallPortForwardingName"),
        ("ZHNFIREWALL", "firewallPortType"),
        ("ZHNFIREWALL", "firewallPortProtocol"),
        ("ZHNFIREWALL", "firewallPortPublicPortStart"),
        ("ZHNFIREWALL", "firewallPortPublicPortEnd"),
        ("ZHNFIREWALL", "firewallPortPrivatePort"),
        ("ZHNFIREWALL", "firewallPortPrivateIPAddress"),
        ("ZHNFIREWALL", "firewallPortForwardingRowStatus"))
)
if mibBuilder.loadTexts:
    zhnFirewallPortForwardingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnFirewallCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 2, 1)
)
if mibBuilder.loadTexts:
    zhnFirewallCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNFIREWALL",
    **{"FirewallMgmtAccessServiceValues": FirewallMgmtAccessServiceValues,
       "FirewallMgmtAccessServiceActions": FirewallMgmtAccessServiceActions,
       "FirewallPortTypeValues": FirewallPortTypeValues,
       "FirewallPortProtocolValues": FirewallPortProtocolValues,
       "zhnFirewall": zhnFirewall,
       "zhnFirewallObjects": zhnFirewallObjects,
       "firewallMgmtAccessTable": firewallMgmtAccessTable,
       "firewallMgmtAccessEntry": firewallMgmtAccessEntry,
       "firewallMgmtServiceIndex": firewallMgmtServiceIndex,
       "firewallMgmtService": firewallMgmtService,
       "firewallMgmtAction": firewallMgmtAction,
       "firewallPortForwardingTable": firewallPortForwardingTable,
       "firewallPortForwardingEntry": firewallPortForwardingEntry,
       "firewallPortForwardingIndex": firewallPortForwardingIndex,
       "firewallPortForwardingName": firewallPortForwardingName,
       "firewallPortType": firewallPortType,
       "firewallPortProtocol": firewallPortProtocol,
       "firewallPortPublicPortStart": firewallPortPublicPortStart,
       "firewallPortPublicPortEnd": firewallPortPublicPortEnd,
       "firewallPortPrivatePort": firewallPortPrivatePort,
       "firewallPortPrivateIPAddress": firewallPortPrivateIPAddress,
       "firewallPortForwardingRowStatus": firewallPortForwardingRowStatus,
       "zhnFirewallConformance": zhnFirewallConformance,
       "zhnFirewallGroups": zhnFirewallGroups,
       "zhnFirewallMgmtAccessGroup": zhnFirewallMgmtAccessGroup,
       "zhnFirewallPortForwardingGroup": zhnFirewallPortForwardingGroup,
       "zhnFirewallCompliances": zhnFirewallCompliances,
       "zhnFirewallCompliance": zhnFirewallCompliance}
)
