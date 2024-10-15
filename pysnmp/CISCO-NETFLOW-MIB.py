# SNMP MIB module (CISCO-NETFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NETFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:06 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetPortNumber")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoNetflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387)
)
ciscoNetflowMIB.setRevisions(
        ("2006-04-27 00:00",
         "2006-04-20 00:00",
         "2005-08-30 00:00",
         "2005-03-27 00:00",
         "2004-05-18 00:00",
         "2004-01-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NfInterfaceDirectionTypes(Integer32, TextualConvention):
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
        *(("interfaceDirBoth", 3),
          ("interfaceDirEgress", 2),
          ("interfaceDirIngress", 1),
          ("interfaceDirNone", 0))
    )



class NfCacheTypes(Integer32, TextualConvention):
    status = "current"
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              23)
        )
    )
    namedValues = NamedValues(
        *(("as", 1),
          ("asTos", 9),
          ("bgpNexthopTos", 15),
          ("destinationOnly", 6),
          ("destinationPrefix", 4),
          ("destinationPrefixTos", 12),
          ("expBgpPrefix", 23),
          ("fullFlow", 8),
          ("main", 0),
          ("prefix", 5),
          ("prefixPort", 14),
          ("prefixTos", 13),
          ("protocolPort", 2),
          ("protocolPortTos", 10),
          ("sourceDestination", 7),
          ("sourcePrefix", 3),
          ("sourcePrefixTos", 11))
    )



class NfProtocolTypes(Integer32, TextualConvention):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("all", 22),
          ("gre", 20),
          ("icmp", 16),
          ("igmp", 17),
          ("ipInIp", 18),
          ("ipOther", 21),
          ("ipv6InIp", 19),
          ("tcpBgp", 7),
          ("tcpFrag", 9),
          ("tcpFtp", 2),
          ("tcpFtpd", 3),
          ("tcpNntp", 8),
          ("tcpOther", 10),
          ("tcpSmtp", 5),
          ("tcpTelnet", 1),
          ("tcpWww", 4),
          ("tcpX", 6),
          ("udpDns", 11),
          ("udpFrag", 14),
          ("udpNtp", 12),
          ("udpOther", 15),
          ("udpTftp", 13))
    )



class NfTemplateTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optionTemplate", 2),
          ("template", 1))
    )



class NfTopFlowsSortTypes(Integer32, TextualConvention):
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
        *(("byBytes", 3),
          ("byPackets", 2),
          ("noSort", 1))
    )



class NfFlowDirectionTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowDirEgress", 2),
          ("flowDirIngress", 1),
          ("flowDirNone", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoNetflowMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNetflowMIBNotifs = _CiscoNetflowMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 0)
)
_CiscoNetflowMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNetflowMIBObjects = _CiscoNetflowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1)
)
_CnfCacheInfo_ObjectIdentity = ObjectIdentity
cnfCacheInfo = _CnfCacheInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1)
)
_CnfCIInterfaceTable_Object = MibTable
cnfCIInterfaceTable = _CnfCIInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cnfCIInterfaceTable.setStatus("current")
_CnfCIInterfaceEntry_Object = MibTableRow
cnfCIInterfaceEntry = _CnfCIInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 1, 1)
)
cnfCIInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnfCIInterfaceEntry.setStatus("current")
_CnfCINetflowEnable_Type = NfInterfaceDirectionTypes
_CnfCINetflowEnable_Object = MibTableColumn
cnfCINetflowEnable = _CnfCINetflowEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 1, 1, 1),
    _CnfCINetflowEnable_Type()
)
cnfCINetflowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCINetflowEnable.setStatus("current")
_CnfCIMcastNetflowEnable_Type = NfInterfaceDirectionTypes
_CnfCIMcastNetflowEnable_Object = MibTableColumn
cnfCIMcastNetflowEnable = _CnfCIMcastNetflowEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 1, 1, 2),
    _CnfCIMcastNetflowEnable_Type()
)
cnfCIMcastNetflowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCIMcastNetflowEnable.setStatus("current")
_CnfCICacheTable_Object = MibTable
cnfCICacheTable = _CnfCICacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cnfCICacheTable.setStatus("current")
_CnfCICacheEntry_Object = MibTableRow
cnfCICacheEntry = _CnfCICacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1)
)
cnfCICacheEntry.setIndexNames(
    (0, "CISCO-NETFLOW-MIB", "cnfCICacheType"),
)
if mibBuilder.loadTexts:
    cnfCICacheEntry.setStatus("current")
_CnfCICacheType_Type = NfCacheTypes
_CnfCICacheType_Object = MibTableColumn
cnfCICacheType = _CnfCICacheType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1, 1),
    _CnfCICacheType_Type()
)
cnfCICacheType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnfCICacheType.setStatus("current")
_CnfCICacheEnable_Type = TruthValue
_CnfCICacheEnable_Object = MibTableColumn
cnfCICacheEnable = _CnfCICacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1, 2),
    _CnfCICacheEnable_Type()
)
cnfCICacheEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCICacheEnable.setStatus("current")
_CnfCICacheEntries_Type = Unsigned32
_CnfCICacheEntries_Object = MibTableColumn
cnfCICacheEntries = _CnfCICacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1, 3),
    _CnfCICacheEntries_Type()
)
cnfCICacheEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCICacheEntries.setStatus("current")
_CnfCIActiveFlows_Type = Unsigned32
_CnfCIActiveFlows_Object = MibTableColumn
cnfCIActiveFlows = _CnfCIActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1, 4),
    _CnfCIActiveFlows_Type()
)
cnfCIActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfCIActiveFlows.setStatus("current")
_CnfCIInactiveFlows_Type = Unsigned32
_CnfCIInactiveFlows_Object = MibTableColumn
cnfCIInactiveFlows = _CnfCIInactiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1, 5),
    _CnfCIInactiveFlows_Type()
)
cnfCIInactiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfCIInactiveFlows.setStatus("current")
_CnfCIActiveTimeOut_Type = Unsigned32
_CnfCIActiveTimeOut_Object = MibTableColumn
cnfCIActiveTimeOut = _CnfCIActiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1, 6),
    _CnfCIActiveTimeOut_Type()
)
cnfCIActiveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCIActiveTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cnfCIActiveTimeOut.setUnits("minutes")
_CnfCIInactiveTimeOut_Type = Unsigned32
_CnfCIInactiveTimeOut_Object = MibTableColumn
cnfCIInactiveTimeOut = _CnfCIInactiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1, 7),
    _CnfCIInactiveTimeOut_Type()
)
cnfCIInactiveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCIInactiveTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cnfCIInactiveTimeOut.setUnits("seconds")
_CnfCIMinSourceMask_Type = InetAddressPrefixLength
_CnfCIMinSourceMask_Object = MibTableColumn
cnfCIMinSourceMask = _CnfCIMinSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1, 8),
    _CnfCIMinSourceMask_Type()
)
cnfCIMinSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCIMinSourceMask.setStatus("current")
_CnfCIMinDestinationMask_Type = InetAddressPrefixLength
_CnfCIMinDestinationMask_Object = MibTableColumn
cnfCIMinDestinationMask = _CnfCIMinDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 2, 1, 9),
    _CnfCIMinDestinationMask_Type()
)
cnfCIMinDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCIMinDestinationMask.setStatus("current")
_CnfCIBridgedFlowStatsCtrlTable_Object = MibTable
cnfCIBridgedFlowStatsCtrlTable = _CnfCIBridgedFlowStatsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cnfCIBridgedFlowStatsCtrlTable.setStatus("current")
_CnfCIBridgedFlowStatsCtrlEntry_Object = MibTableRow
cnfCIBridgedFlowStatsCtrlEntry = _CnfCIBridgedFlowStatsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 3, 1)
)
cnfCIBridgedFlowStatsCtrlEntry.setIndexNames(
    (0, "CISCO-NETFLOW-MIB", "cnfCIBridgedFlowVlan"),
)
if mibBuilder.loadTexts:
    cnfCIBridgedFlowStatsCtrlEntry.setStatus("current")
_CnfCIBridgedFlowVlan_Type = VlanIndex
_CnfCIBridgedFlowVlan_Object = MibTableColumn
cnfCIBridgedFlowVlan = _CnfCIBridgedFlowVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 3, 1, 1),
    _CnfCIBridgedFlowVlan_Type()
)
cnfCIBridgedFlowVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnfCIBridgedFlowVlan.setStatus("current")
_CnfCIBridgedFlowStatsCrtEnable_Type = TruthValue
_CnfCIBridgedFlowStatsCrtEnable_Object = MibTableColumn
cnfCIBridgedFlowStatsCrtEnable = _CnfCIBridgedFlowStatsCrtEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 3, 1, 2),
    _CnfCIBridgedFlowStatsCrtEnable_Type()
)
cnfCIBridgedFlowStatsCrtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCIBridgedFlowStatsCrtEnable.setStatus("current")
_CnfCIBridgedFlowStatsExpEnable_Type = TruthValue
_CnfCIBridgedFlowStatsExpEnable_Object = MibTableColumn
cnfCIBridgedFlowStatsExpEnable = _CnfCIBridgedFlowStatsExpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 3, 1, 3),
    _CnfCIBridgedFlowStatsExpEnable_Type()
)
cnfCIBridgedFlowStatsExpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCIBridgedFlowStatsExpEnable.setStatus("current")
_CnfCIMcastNetflowRPFFailedEnable_Type = TruthValue
_CnfCIMcastNetflowRPFFailedEnable_Object = MibScalar
cnfCIMcastNetflowRPFFailedEnable = _CnfCIMcastNetflowRPFFailedEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 1, 4),
    _CnfCIMcastNetflowRPFFailedEnable_Type()
)
cnfCIMcastNetflowRPFFailedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfCIMcastNetflowRPFFailedEnable.setStatus("current")
_CnfExportInfo_ObjectIdentity = ObjectIdentity
cnfExportInfo = _CnfExportInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2)
)
_CnfEIExportInfoTable_Object = MibTable
cnfEIExportInfoTable = _CnfEIExportInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cnfEIExportInfoTable.setStatus("current")
_CnfEIExportInfoEntry_Object = MibTableRow
cnfEIExportInfoEntry = _CnfEIExportInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 1, 1)
)
cnfEIExportInfoEntry.setIndexNames(
    (0, "CISCO-NETFLOW-MIB", "cnfCICacheType"),
)
if mibBuilder.loadTexts:
    cnfEIExportInfoEntry.setStatus("current")
_CnfEIExportVersion_Type = Unsigned32
_CnfEIExportVersion_Object = MibTableColumn
cnfEIExportVersion = _CnfEIExportVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 1, 1, 1),
    _CnfEIExportVersion_Type()
)
cnfEIExportVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfEIExportVersion.setStatus("current")
_CnfEIPeerAS_Type = TruthValue
_CnfEIPeerAS_Object = MibTableColumn
cnfEIPeerAS = _CnfEIPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 1, 1, 2),
    _CnfEIPeerAS_Type()
)
cnfEIPeerAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfEIPeerAS.setStatus("current")
_CnfEIOriginAS_Type = TruthValue
_CnfEIOriginAS_Object = MibTableColumn
cnfEIOriginAS = _CnfEIOriginAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 1, 1, 3),
    _CnfEIOriginAS_Type()
)
cnfEIOriginAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfEIOriginAS.setStatus("current")
_CnfEIBgpNextHop_Type = TruthValue
_CnfEIBgpNextHop_Object = MibTableColumn
cnfEIBgpNextHop = _CnfEIBgpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 1, 1, 4),
    _CnfEIBgpNextHop_Type()
)
cnfEIBgpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfEIBgpNextHop.setStatus("current")
_CnfEIMaxCollectors_Type = Unsigned32
_CnfEIMaxCollectors_Object = MibScalar
cnfEIMaxCollectors = _CnfEIMaxCollectors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 2),
    _CnfEIMaxCollectors_Type()
)
cnfEIMaxCollectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfEIMaxCollectors.setStatus("current")
_CnfEICollectorTable_Object = MibTable
cnfEICollectorTable = _CnfEICollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cnfEICollectorTable.setStatus("current")
_CnfEICollectorEntry_Object = MibTableRow
cnfEICollectorEntry = _CnfEICollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 3, 1)
)
cnfEICollectorEntry.setIndexNames(
    (0, "CISCO-NETFLOW-MIB", "cnfCICacheType"),
    (0, "CISCO-NETFLOW-MIB", "cnfEICollectorAddressType"),
    (0, "CISCO-NETFLOW-MIB", "cnfEICollectorAddress"),
    (0, "CISCO-NETFLOW-MIB", "cnfEICollectorPort"),
)
if mibBuilder.loadTexts:
    cnfEICollectorEntry.setStatus("current")
_CnfEICollectorAddressType_Type = InetAddressType
_CnfEICollectorAddressType_Object = MibTableColumn
cnfEICollectorAddressType = _CnfEICollectorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 3, 1, 1),
    _CnfEICollectorAddressType_Type()
)
cnfEICollectorAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnfEICollectorAddressType.setStatus("current")
_CnfEICollectorAddress_Type = InetAddress
_CnfEICollectorAddress_Object = MibTableColumn
cnfEICollectorAddress = _CnfEICollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 3, 1, 2),
    _CnfEICollectorAddress_Type()
)
cnfEICollectorAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnfEICollectorAddress.setStatus("current")
_CnfEICollectorPort_Type = InetPortNumber
_CnfEICollectorPort_Object = MibTableColumn
cnfEICollectorPort = _CnfEICollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 3, 1, 3),
    _CnfEICollectorPort_Type()
)
cnfEICollectorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnfEICollectorPort.setStatus("current")
_CnfEICollectorStatus_Type = RowStatus
_CnfEICollectorStatus_Object = MibTableColumn
cnfEICollectorStatus = _CnfEICollectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 2, 3, 1, 4),
    _CnfEICollectorStatus_Type()
)
cnfEICollectorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnfEICollectorStatus.setStatus("current")
_CnfExportStatistics_ObjectIdentity = ObjectIdentity
cnfExportStatistics = _CnfExportStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 4)
)
_CnfESSampledPacket_Type = Counter32
_CnfESSampledPacket_Object = MibScalar
cnfESSampledPacket = _CnfESSampledPacket_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 4, 1),
    _CnfESSampledPacket_Type()
)
cnfESSampledPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfESSampledPacket.setStatus("current")
_CnfESExportRate_Type = Counter32
_CnfESExportRate_Object = MibScalar
cnfESExportRate = _CnfESExportRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 4, 2),
    _CnfESExportRate_Type()
)
cnfESExportRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfESExportRate.setStatus("current")
if mibBuilder.loadTexts:
    cnfESExportRate.setUnits("bytes per second")
_CnfESRecordsExported_Type = Counter32
_CnfESRecordsExported_Object = MibScalar
cnfESRecordsExported = _CnfESRecordsExported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 4, 3),
    _CnfESRecordsExported_Type()
)
cnfESRecordsExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfESRecordsExported.setStatus("current")
_CnfESPktsExported_Type = Counter32
_CnfESPktsExported_Object = MibScalar
cnfESPktsExported = _CnfESPktsExported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 4, 4),
    _CnfESPktsExported_Type()
)
cnfESPktsExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfESPktsExported.setStatus("current")
_CnfESPktsFailed_Type = Counter32
_CnfESPktsFailed_Object = MibScalar
cnfESPktsFailed = _CnfESPktsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 4, 5),
    _CnfESPktsFailed_Type()
)
cnfESPktsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfESPktsFailed.setStatus("current")
_CnfESPktsDropped_Type = Counter32
_CnfESPktsDropped_Object = MibScalar
cnfESPktsDropped = _CnfESPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 4, 6),
    _CnfESPktsDropped_Type()
)
cnfESPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfESPktsDropped.setStatus("current")
_CnfProtocolStatistics_ObjectIdentity = ObjectIdentity
cnfProtocolStatistics = _CnfProtocolStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5)
)


class _CnfPSPacketSizeDistribution_Type(OctetString):
    """Custom type cnfPSPacketSizeDistribution based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(52, 52),
    )


_CnfPSPacketSizeDistribution_Type.__name__ = "OctetString"
_CnfPSPacketSizeDistribution_Object = MibScalar
cnfPSPacketSizeDistribution = _CnfPSPacketSizeDistribution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 1),
    _CnfPSPacketSizeDistribution_Type()
)
cnfPSPacketSizeDistribution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfPSPacketSizeDistribution.setStatus("current")
_CnfPSLastClearElapsedTime_Type = Gauge32
_CnfPSLastClearElapsedTime_Object = MibScalar
cnfPSLastClearElapsedTime = _CnfPSLastClearElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 2),
    _CnfPSLastClearElapsedTime_Type()
)
cnfPSLastClearElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfPSLastClearElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    cnfPSLastClearElapsedTime.setUnits("milliseconds")
_CnfPSProtocolStatTable_Object = MibTable
cnfPSProtocolStatTable = _CnfPSProtocolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cnfPSProtocolStatTable.setStatus("current")
_CnfPSProtocolStatEntry_Object = MibTableRow
cnfPSProtocolStatEntry = _CnfPSProtocolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 3, 1)
)
cnfPSProtocolStatEntry.setIndexNames(
    (0, "CISCO-NETFLOW-MIB", "cnfPSProtocolType"),
)
if mibBuilder.loadTexts:
    cnfPSProtocolStatEntry.setStatus("current")
_CnfPSProtocolType_Type = NfProtocolTypes
_CnfPSProtocolType_Object = MibTableColumn
cnfPSProtocolType = _CnfPSProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 3, 1, 1),
    _CnfPSProtocolType_Type()
)
cnfPSProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnfPSProtocolType.setStatus("current")
_CnfPSExpiredFlows_Type = Counter64
_CnfPSExpiredFlows_Object = MibTableColumn
cnfPSExpiredFlows = _CnfPSExpiredFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 3, 1, 2),
    _CnfPSExpiredFlows_Type()
)
cnfPSExpiredFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfPSExpiredFlows.setStatus("current")
_CnfPSPackets_Type = Counter64
_CnfPSPackets_Object = MibTableColumn
cnfPSPackets = _CnfPSPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 3, 1, 3),
    _CnfPSPackets_Type()
)
cnfPSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfPSPackets.setStatus("current")
_CnfPSBytes_Type = Counter64
_CnfPSBytes_Object = MibTableColumn
cnfPSBytes = _CnfPSBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 3, 1, 4),
    _CnfPSBytes_Type()
)
cnfPSBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfPSBytes.setStatus("current")
_CnfPSActive_Type = Counter64
_CnfPSActive_Object = MibTableColumn
cnfPSActive = _CnfPSActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 3, 1, 5),
    _CnfPSActive_Type()
)
cnfPSActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfPSActive.setStatus("current")
if mibBuilder.loadTexts:
    cnfPSActive.setUnits("milliseconds")
_CnfPSInactive_Type = Counter64
_CnfPSInactive_Object = MibTableColumn
cnfPSInactive = _CnfPSInactive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 5, 3, 1, 6),
    _CnfPSInactive_Type()
)
cnfPSInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfPSInactive.setStatus("current")
if mibBuilder.loadTexts:
    cnfPSInactive.setUnits("milliseconds")
_CnfExportTemplate_ObjectIdentity = ObjectIdentity
cnfExportTemplate = _CnfExportTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6)
)
_CnfTemplateOptionsFlag_Type = Unsigned32
_CnfTemplateOptionsFlag_Object = MibScalar
cnfTemplateOptionsFlag = _CnfTemplateOptionsFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 1),
    _CnfTemplateOptionsFlag_Type()
)
cnfTemplateOptionsFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTemplateOptionsFlag.setStatus("current")
_CnfTemplateTable_Object = MibTable
cnfTemplateTable = _CnfTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cnfTemplateTable.setStatus("current")
_CnfTemplateEntry_Object = MibTableRow
cnfTemplateEntry = _CnfTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 2, 1)
)
cnfTemplateEntry.setIndexNames(
    (0, "CISCO-NETFLOW-MIB", "cnfTemplateType"),
)
if mibBuilder.loadTexts:
    cnfTemplateEntry.setStatus("current")
_CnfTemplateType_Type = NfTemplateTypes
_CnfTemplateType_Object = MibTableColumn
cnfTemplateType = _CnfTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 2, 1, 1),
    _CnfTemplateType_Type()
)
cnfTemplateType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnfTemplateType.setStatus("current")
_CnfTemplateAdded_Type = Unsigned32
_CnfTemplateAdded_Object = MibTableColumn
cnfTemplateAdded = _CnfTemplateAdded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 2, 1, 2),
    _CnfTemplateAdded_Type()
)
cnfTemplateAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTemplateAdded.setStatus("current")
_CnfTemplateActive_Type = Unsigned32
_CnfTemplateActive_Object = MibTableColumn
cnfTemplateActive = _CnfTemplateActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 2, 1, 3),
    _CnfTemplateActive_Type()
)
cnfTemplateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTemplateActive.setStatus("current")
_CnfTemplateAgerPolls_Type = Unsigned32
_CnfTemplateAgerPolls_Object = MibTableColumn
cnfTemplateAgerPolls = _CnfTemplateAgerPolls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 2, 1, 4),
    _CnfTemplateAgerPolls_Type()
)
cnfTemplateAgerPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTemplateAgerPolls.setStatus("current")
_CnfTemplateExportInfoTable_Object = MibTable
cnfTemplateExportInfoTable = _CnfTemplateExportInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cnfTemplateExportInfoTable.setStatus("current")
_CnfTemplateExportInfoEntry_Object = MibTableRow
cnfTemplateExportInfoEntry = _CnfTemplateExportInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 3, 1)
)
cnfTemplateExportInfoEntry.setIndexNames(
    (0, "CISCO-NETFLOW-MIB", "cnfCICacheType"),
)
if mibBuilder.loadTexts:
    cnfTemplateExportInfoEntry.setStatus("current")
_CnfTemplateExportVer9Enable_Type = TruthValue
_CnfTemplateExportVer9Enable_Object = MibTableColumn
cnfTemplateExportVer9Enable = _CnfTemplateExportVer9Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 3, 1, 1),
    _CnfTemplateExportVer9Enable_Type()
)
cnfTemplateExportVer9Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTemplateExportVer9Enable.setStatus("current")
_CnfTemplateExportVer9TplTimeout_Type = Unsigned32
_CnfTemplateExportVer9TplTimeout_Object = MibTableColumn
cnfTemplateExportVer9TplTimeout = _CnfTemplateExportVer9TplTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 3, 1, 2),
    _CnfTemplateExportVer9TplTimeout_Type()
)
cnfTemplateExportVer9TplTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTemplateExportVer9TplTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cnfTemplateExportVer9TplTimeout.setUnits("minutes")
_CnfTemplateExportVer9OptTimeout_Type = Unsigned32
_CnfTemplateExportVer9OptTimeout_Object = MibTableColumn
cnfTemplateExportVer9OptTimeout = _CnfTemplateExportVer9OptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 3, 1, 3),
    _CnfTemplateExportVer9OptTimeout_Type()
)
cnfTemplateExportVer9OptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTemplateExportVer9OptTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cnfTemplateExportVer9OptTimeout.setUnits("minutes")
_CnfTemplateExportVer9TplRefreshRate_Type = Unsigned32
_CnfTemplateExportVer9TplRefreshRate_Object = MibTableColumn
cnfTemplateExportVer9TplRefreshRate = _CnfTemplateExportVer9TplRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 3, 1, 4),
    _CnfTemplateExportVer9TplRefreshRate_Type()
)
cnfTemplateExportVer9TplRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTemplateExportVer9TplRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    cnfTemplateExportVer9TplRefreshRate.setUnits("packets")
_CnfTemplateExportVer9OptRefreshRate_Type = Unsigned32
_CnfTemplateExportVer9OptRefreshRate_Object = MibTableColumn
cnfTemplateExportVer9OptRefreshRate = _CnfTemplateExportVer9OptRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 6, 3, 1, 5),
    _CnfTemplateExportVer9OptRefreshRate_Type()
)
cnfTemplateExportVer9OptRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTemplateExportVer9OptRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    cnfTemplateExportVer9OptRefreshRate.setUnits("packets")
_CnfTopFlows_ObjectIdentity = ObjectIdentity
cnfTopFlows = _CnfTopFlows_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7)
)
_CnfTopFlowsTimeStamp_Type = TimeStamp
_CnfTopFlowsTimeStamp_Object = MibScalar
cnfTopFlowsTimeStamp = _CnfTopFlowsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 1),
    _CnfTopFlowsTimeStamp_Type()
)
cnfTopFlowsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsTimeStamp.setStatus("current")
_CnfTopFlowsTopN_Type = Unsigned32
_CnfTopFlowsTopN_Object = MibScalar
cnfTopFlowsTopN = _CnfTopFlowsTopN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 2),
    _CnfTopFlowsTopN_Type()
)
cnfTopFlowsTopN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsTopN.setStatus("current")
_CnfTopFlowsAvailableFlows_Type = Unsigned32
_CnfTopFlowsAvailableFlows_Object = MibScalar
cnfTopFlowsAvailableFlows = _CnfTopFlowsAvailableFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 3),
    _CnfTopFlowsAvailableFlows_Type()
)
cnfTopFlowsAvailableFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsAvailableFlows.setStatus("current")
_CnfTopFlowsMatchingFlows_Type = Unsigned32
_CnfTopFlowsMatchingFlows_Object = MibScalar
cnfTopFlowsMatchingFlows = _CnfTopFlowsMatchingFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 4),
    _CnfTopFlowsMatchingFlows_Type()
)
cnfTopFlowsMatchingFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchingFlows.setStatus("current")
_CnfTopFlowsTotalFlows_Type = Unsigned32
_CnfTopFlowsTotalFlows_Object = MibScalar
cnfTopFlowsTotalFlows = _CnfTopFlowsTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 5),
    _CnfTopFlowsTotalFlows_Type()
)
cnfTopFlowsTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsTotalFlows.setStatus("current")
_CnfTopFlowsSortBy_Type = NfTopFlowsSortTypes
_CnfTopFlowsSortBy_Object = MibScalar
cnfTopFlowsSortBy = _CnfTopFlowsSortBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 6),
    _CnfTopFlowsSortBy_Type()
)
cnfTopFlowsSortBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsSortBy.setStatus("current")
_CnfTopFlowsCacheTimeout_Type = Unsigned32
_CnfTopFlowsCacheTimeout_Object = MibScalar
cnfTopFlowsCacheTimeout = _CnfTopFlowsCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 7),
    _CnfTopFlowsCacheTimeout_Type()
)
cnfTopFlowsCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsCacheTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cnfTopFlowsCacheTimeout.setUnits("milliseconds")
_CnfTopFlowsTable_Object = MibTable
cnfTopFlowsTable = _CnfTopFlowsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8)
)
if mibBuilder.loadTexts:
    cnfTopFlowsTable.setStatus("current")
_CnfTopFlowsTableEntry_Object = MibTableRow
cnfTopFlowsTableEntry = _CnfTopFlowsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1)
)
cnfTopFlowsTableEntry.setIndexNames(
    (0, "CISCO-NETFLOW-MIB", "cnfTopFlowsIndex"),
)
if mibBuilder.loadTexts:
    cnfTopFlowsTableEntry.setStatus("current")
_CnfTopFlowsIndex_Type = Unsigned32
_CnfTopFlowsIndex_Object = MibTableColumn
cnfTopFlowsIndex = _CnfTopFlowsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 1),
    _CnfTopFlowsIndex_Type()
)
cnfTopFlowsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnfTopFlowsIndex.setStatus("current")
_CnfTopFlowsSrcAddressType_Type = InetAddressType
_CnfTopFlowsSrcAddressType_Object = MibTableColumn
cnfTopFlowsSrcAddressType = _CnfTopFlowsSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 2),
    _CnfTopFlowsSrcAddressType_Type()
)
cnfTopFlowsSrcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsSrcAddressType.setStatus("current")
_CnfTopFlowsSrcAddress_Type = InetAddress
_CnfTopFlowsSrcAddress_Object = MibTableColumn
cnfTopFlowsSrcAddress = _CnfTopFlowsSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 3),
    _CnfTopFlowsSrcAddress_Type()
)
cnfTopFlowsSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsSrcAddress.setStatus("current")
_CnfTopFlowsSrcAddressMask_Type = InetAddressPrefixLength
_CnfTopFlowsSrcAddressMask_Object = MibTableColumn
cnfTopFlowsSrcAddressMask = _CnfTopFlowsSrcAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 4),
    _CnfTopFlowsSrcAddressMask_Type()
)
cnfTopFlowsSrcAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsSrcAddressMask.setStatus("current")
_CnfTopFlowsDstAddressType_Type = InetAddressType
_CnfTopFlowsDstAddressType_Object = MibTableColumn
cnfTopFlowsDstAddressType = _CnfTopFlowsDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 5),
    _CnfTopFlowsDstAddressType_Type()
)
cnfTopFlowsDstAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsDstAddressType.setStatus("current")
_CnfTopFlowsDstAddress_Type = InetAddress
_CnfTopFlowsDstAddress_Object = MibTableColumn
cnfTopFlowsDstAddress = _CnfTopFlowsDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 6),
    _CnfTopFlowsDstAddress_Type()
)
cnfTopFlowsDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsDstAddress.setStatus("current")
_CnfTopFlowsDstAddressMask_Type = InetAddressPrefixLength
_CnfTopFlowsDstAddressMask_Object = MibTableColumn
cnfTopFlowsDstAddressMask = _CnfTopFlowsDstAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 7),
    _CnfTopFlowsDstAddressMask_Type()
)
cnfTopFlowsDstAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsDstAddressMask.setStatus("current")
_CnfTopFlowsNhAddressType_Type = InetAddressType
_CnfTopFlowsNhAddressType_Object = MibTableColumn
cnfTopFlowsNhAddressType = _CnfTopFlowsNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 8),
    _CnfTopFlowsNhAddressType_Type()
)
cnfTopFlowsNhAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsNhAddressType.setStatus("current")
_CnfTopFlowsNhAddress_Type = InetAddress
_CnfTopFlowsNhAddress_Object = MibTableColumn
cnfTopFlowsNhAddress = _CnfTopFlowsNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 9),
    _CnfTopFlowsNhAddress_Type()
)
cnfTopFlowsNhAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsNhAddress.setStatus("current")
_CnfTopFlowsSrcPort_Type = InetPortNumber
_CnfTopFlowsSrcPort_Object = MibTableColumn
cnfTopFlowsSrcPort = _CnfTopFlowsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 10),
    _CnfTopFlowsSrcPort_Type()
)
cnfTopFlowsSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsSrcPort.setStatus("current")
_CnfTopFlowsDstPort_Type = InetPortNumber
_CnfTopFlowsDstPort_Object = MibTableColumn
cnfTopFlowsDstPort = _CnfTopFlowsDstPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 11),
    _CnfTopFlowsDstPort_Type()
)
cnfTopFlowsDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsDstPort.setStatus("current")
_CnfTopFlowsSrcAS_Type = InetAutonomousSystemNumber
_CnfTopFlowsSrcAS_Object = MibTableColumn
cnfTopFlowsSrcAS = _CnfTopFlowsSrcAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 12),
    _CnfTopFlowsSrcAS_Type()
)
cnfTopFlowsSrcAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsSrcAS.setStatus("current")
_CnfTopFlowsDstAS_Type = InetAutonomousSystemNumber
_CnfTopFlowsDstAS_Object = MibTableColumn
cnfTopFlowsDstAS = _CnfTopFlowsDstAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 13),
    _CnfTopFlowsDstAS_Type()
)
cnfTopFlowsDstAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsDstAS.setStatus("current")
_CnfTopFlowsInputIfIndex_Type = InterfaceIndex
_CnfTopFlowsInputIfIndex_Object = MibTableColumn
cnfTopFlowsInputIfIndex = _CnfTopFlowsInputIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 14),
    _CnfTopFlowsInputIfIndex_Type()
)
cnfTopFlowsInputIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsInputIfIndex.setStatus("current")
_CnfTopFlowsOutputIfIndex_Type = InterfaceIndex
_CnfTopFlowsOutputIfIndex_Object = MibTableColumn
cnfTopFlowsOutputIfIndex = _CnfTopFlowsOutputIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 15),
    _CnfTopFlowsOutputIfIndex_Type()
)
cnfTopFlowsOutputIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsOutputIfIndex.setStatus("current")
_CnfTopFlowsFirstSwitched_Type = TimeStamp
_CnfTopFlowsFirstSwitched_Object = MibTableColumn
cnfTopFlowsFirstSwitched = _CnfTopFlowsFirstSwitched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 16),
    _CnfTopFlowsFirstSwitched_Type()
)
cnfTopFlowsFirstSwitched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsFirstSwitched.setStatus("current")
_CnfTopFlowsLastSwitched_Type = TimeStamp
_CnfTopFlowsLastSwitched_Object = MibTableColumn
cnfTopFlowsLastSwitched = _CnfTopFlowsLastSwitched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 17),
    _CnfTopFlowsLastSwitched_Type()
)
cnfTopFlowsLastSwitched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsLastSwitched.setStatus("current")
_CnfTopFlowsTOS_Type = Unsigned32
_CnfTopFlowsTOS_Object = MibTableColumn
cnfTopFlowsTOS = _CnfTopFlowsTOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 18),
    _CnfTopFlowsTOS_Type()
)
cnfTopFlowsTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsTOS.setStatus("current")
_CnfTopFlowsProtocol_Type = Unsigned32
_CnfTopFlowsProtocol_Object = MibTableColumn
cnfTopFlowsProtocol = _CnfTopFlowsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 19),
    _CnfTopFlowsProtocol_Type()
)
cnfTopFlowsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsProtocol.setStatus("current")
_CnfTopFlowsTCPFlags_Type = Unsigned32
_CnfTopFlowsTCPFlags_Object = MibTableColumn
cnfTopFlowsTCPFlags = _CnfTopFlowsTCPFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 20),
    _CnfTopFlowsTCPFlags_Type()
)
cnfTopFlowsTCPFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsTCPFlags.setStatus("current")
_CnfTopFlowsSamplerID_Type = Unsigned32
_CnfTopFlowsSamplerID_Object = MibTableColumn
cnfTopFlowsSamplerID = _CnfTopFlowsSamplerID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 21),
    _CnfTopFlowsSamplerID_Type()
)
cnfTopFlowsSamplerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsSamplerID.setStatus("current")
_CnfTopFlowsClassID_Type = Unsigned32
_CnfTopFlowsClassID_Object = MibTableColumn
cnfTopFlowsClassID = _CnfTopFlowsClassID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 22),
    _CnfTopFlowsClassID_Type()
)
cnfTopFlowsClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsClassID.setStatus("current")
_CnfTopFlowsFlags_Type = Unsigned32
_CnfTopFlowsFlags_Object = MibTableColumn
cnfTopFlowsFlags = _CnfTopFlowsFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 23),
    _CnfTopFlowsFlags_Type()
)
cnfTopFlowsFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsFlags.setStatus("current")
_CnfTopFlowsBytes_Type = Unsigned32
_CnfTopFlowsBytes_Object = MibTableColumn
cnfTopFlowsBytes = _CnfTopFlowsBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 24),
    _CnfTopFlowsBytes_Type()
)
cnfTopFlowsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsBytes.setStatus("current")
_CnfTopFlowsPackets_Type = Unsigned32
_CnfTopFlowsPackets_Object = MibTableColumn
cnfTopFlowsPackets = _CnfTopFlowsPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 25),
    _CnfTopFlowsPackets_Type()
)
cnfTopFlowsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsPackets.setStatus("current")
_CnfTopFlowsVlan_Type = VlanIndex
_CnfTopFlowsVlan_Object = MibTableColumn
cnfTopFlowsVlan = _CnfTopFlowsVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 8, 1, 26),
    _CnfTopFlowsVlan_Type()
)
cnfTopFlowsVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsVlan.setStatus("current")
_CnfTopFlowsMatchSrcAddressType_Type = InetAddressType
_CnfTopFlowsMatchSrcAddressType_Object = MibScalar
cnfTopFlowsMatchSrcAddressType = _CnfTopFlowsMatchSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 9),
    _CnfTopFlowsMatchSrcAddressType_Type()
)
cnfTopFlowsMatchSrcAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchSrcAddressType.setStatus("current")
_CnfTopFlowsMatchSrcAddress_Type = InetAddress
_CnfTopFlowsMatchSrcAddress_Object = MibScalar
cnfTopFlowsMatchSrcAddress = _CnfTopFlowsMatchSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 10),
    _CnfTopFlowsMatchSrcAddress_Type()
)
cnfTopFlowsMatchSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchSrcAddress.setStatus("current")
_CnfTopFlowsMatchSrcAddressMask_Type = InetAddressPrefixLength
_CnfTopFlowsMatchSrcAddressMask_Object = MibScalar
cnfTopFlowsMatchSrcAddressMask = _CnfTopFlowsMatchSrcAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 11),
    _CnfTopFlowsMatchSrcAddressMask_Type()
)
cnfTopFlowsMatchSrcAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchSrcAddressMask.setStatus("current")
_CnfTopFlowsMatchDstAddressType_Type = InetAddressType
_CnfTopFlowsMatchDstAddressType_Object = MibScalar
cnfTopFlowsMatchDstAddressType = _CnfTopFlowsMatchDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 12),
    _CnfTopFlowsMatchDstAddressType_Type()
)
cnfTopFlowsMatchDstAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchDstAddressType.setStatus("current")
_CnfTopFlowsMatchDstAddress_Type = InetAddress
_CnfTopFlowsMatchDstAddress_Object = MibScalar
cnfTopFlowsMatchDstAddress = _CnfTopFlowsMatchDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 13),
    _CnfTopFlowsMatchDstAddress_Type()
)
cnfTopFlowsMatchDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchDstAddress.setStatus("current")
_CnfTopFlowsMatchDstAddressMask_Type = InetAddressPrefixLength
_CnfTopFlowsMatchDstAddressMask_Object = MibScalar
cnfTopFlowsMatchDstAddressMask = _CnfTopFlowsMatchDstAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 14),
    _CnfTopFlowsMatchDstAddressMask_Type()
)
cnfTopFlowsMatchDstAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchDstAddressMask.setStatus("current")
_CnfTopFlowsMatchNhAddressType_Type = InetAddressType
_CnfTopFlowsMatchNhAddressType_Object = MibScalar
cnfTopFlowsMatchNhAddressType = _CnfTopFlowsMatchNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 15),
    _CnfTopFlowsMatchNhAddressType_Type()
)
cnfTopFlowsMatchNhAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchNhAddressType.setStatus("current")
_CnfTopFlowsMatchNhAddress_Type = InetAddress
_CnfTopFlowsMatchNhAddress_Object = MibScalar
cnfTopFlowsMatchNhAddress = _CnfTopFlowsMatchNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 16),
    _CnfTopFlowsMatchNhAddress_Type()
)
cnfTopFlowsMatchNhAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchNhAddress.setStatus("current")
_CnfTopFlowsMatchNhAddressMask_Type = InetAddressPrefixLength
_CnfTopFlowsMatchNhAddressMask_Object = MibScalar
cnfTopFlowsMatchNhAddressMask = _CnfTopFlowsMatchNhAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 17),
    _CnfTopFlowsMatchNhAddressMask_Type()
)
cnfTopFlowsMatchNhAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchNhAddressMask.setStatus("current")


class _CnfTopFlowsMatchSrcPortLo_Type(Integer32):
    """Custom type cnfTopFlowsMatchSrcPortLo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_CnfTopFlowsMatchSrcPortLo_Type.__name__ = "Integer32"
_CnfTopFlowsMatchSrcPortLo_Object = MibScalar
cnfTopFlowsMatchSrcPortLo = _CnfTopFlowsMatchSrcPortLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 18),
    _CnfTopFlowsMatchSrcPortLo_Type()
)
cnfTopFlowsMatchSrcPortLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchSrcPortLo.setStatus("current")


class _CnfTopFlowsMatchSrcPortHi_Type(Integer32):
    """Custom type cnfTopFlowsMatchSrcPortHi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_CnfTopFlowsMatchSrcPortHi_Type.__name__ = "Integer32"
_CnfTopFlowsMatchSrcPortHi_Object = MibScalar
cnfTopFlowsMatchSrcPortHi = _CnfTopFlowsMatchSrcPortHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 19),
    _CnfTopFlowsMatchSrcPortHi_Type()
)
cnfTopFlowsMatchSrcPortHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchSrcPortHi.setStatus("current")


class _CnfTopFlowsMatchDstPortLo_Type(Integer32):
    """Custom type cnfTopFlowsMatchDstPortLo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_CnfTopFlowsMatchDstPortLo_Type.__name__ = "Integer32"
_CnfTopFlowsMatchDstPortLo_Object = MibScalar
cnfTopFlowsMatchDstPortLo = _CnfTopFlowsMatchDstPortLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 20),
    _CnfTopFlowsMatchDstPortLo_Type()
)
cnfTopFlowsMatchDstPortLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchDstPortLo.setStatus("current")


class _CnfTopFlowsMatchDstPortHi_Type(Integer32):
    """Custom type cnfTopFlowsMatchDstPortHi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_CnfTopFlowsMatchDstPortHi_Type.__name__ = "Integer32"
_CnfTopFlowsMatchDstPortHi_Object = MibScalar
cnfTopFlowsMatchDstPortHi = _CnfTopFlowsMatchDstPortHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 21),
    _CnfTopFlowsMatchDstPortHi_Type()
)
cnfTopFlowsMatchDstPortHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchDstPortHi.setStatus("current")
_CnfTopFlowsMatchSrcAS_Type = Integer32
_CnfTopFlowsMatchSrcAS_Object = MibScalar
cnfTopFlowsMatchSrcAS = _CnfTopFlowsMatchSrcAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 22),
    _CnfTopFlowsMatchSrcAS_Type()
)
cnfTopFlowsMatchSrcAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchSrcAS.setStatus("current")
_CnfTopFlowsMatchDstAS_Type = Integer32
_CnfTopFlowsMatchDstAS_Object = MibScalar
cnfTopFlowsMatchDstAS = _CnfTopFlowsMatchDstAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 23),
    _CnfTopFlowsMatchDstAS_Type()
)
cnfTopFlowsMatchDstAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchDstAS.setStatus("current")
_CnfTopFlowsMatchInputIf_Type = InterfaceIndexOrZero
_CnfTopFlowsMatchInputIf_Object = MibScalar
cnfTopFlowsMatchInputIf = _CnfTopFlowsMatchInputIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 24),
    _CnfTopFlowsMatchInputIf_Type()
)
cnfTopFlowsMatchInputIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchInputIf.setStatus("current")
_CnfTopFlowsMatchOutputIf_Type = InterfaceIndexOrZero
_CnfTopFlowsMatchOutputIf_Object = MibScalar
cnfTopFlowsMatchOutputIf = _CnfTopFlowsMatchOutputIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 25),
    _CnfTopFlowsMatchOutputIf_Type()
)
cnfTopFlowsMatchOutputIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchOutputIf.setStatus("current")
_CnfTopFlowsMatchTOSByte_Type = Integer32
_CnfTopFlowsMatchTOSByte_Object = MibScalar
cnfTopFlowsMatchTOSByte = _CnfTopFlowsMatchTOSByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 26),
    _CnfTopFlowsMatchTOSByte_Type()
)
cnfTopFlowsMatchTOSByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchTOSByte.setStatus("current")
_CnfTopFlowsMatchProtocol_Type = Integer32
_CnfTopFlowsMatchProtocol_Object = MibScalar
cnfTopFlowsMatchProtocol = _CnfTopFlowsMatchProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 27),
    _CnfTopFlowsMatchProtocol_Type()
)
cnfTopFlowsMatchProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchProtocol.setStatus("current")
_CnfTopFlowsMatchSampler_Type = DisplayString
_CnfTopFlowsMatchSampler_Object = MibScalar
cnfTopFlowsMatchSampler = _CnfTopFlowsMatchSampler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 28),
    _CnfTopFlowsMatchSampler_Type()
)
cnfTopFlowsMatchSampler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchSampler.setStatus("current")
_CnfTopFlowsMatchClass_Type = DisplayString
_CnfTopFlowsMatchClass_Object = MibScalar
cnfTopFlowsMatchClass = _CnfTopFlowsMatchClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 29),
    _CnfTopFlowsMatchClass_Type()
)
cnfTopFlowsMatchClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchClass.setStatus("current")
_CnfTopFlowsMatchMinPackets_Type = Unsigned32
_CnfTopFlowsMatchMinPackets_Object = MibScalar
cnfTopFlowsMatchMinPackets = _CnfTopFlowsMatchMinPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 30),
    _CnfTopFlowsMatchMinPackets_Type()
)
cnfTopFlowsMatchMinPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchMinPackets.setStatus("current")
_CnfTopFlowsMatchMaxPackets_Type = Unsigned32
_CnfTopFlowsMatchMaxPackets_Object = MibScalar
cnfTopFlowsMatchMaxPackets = _CnfTopFlowsMatchMaxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 31),
    _CnfTopFlowsMatchMaxPackets_Type()
)
cnfTopFlowsMatchMaxPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchMaxPackets.setStatus("current")
_CnfTopFlowsMatchMinBytes_Type = Unsigned32
_CnfTopFlowsMatchMinBytes_Object = MibScalar
cnfTopFlowsMatchMinBytes = _CnfTopFlowsMatchMinBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 32),
    _CnfTopFlowsMatchMinBytes_Type()
)
cnfTopFlowsMatchMinBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchMinBytes.setStatus("current")
_CnfTopFlowsMatchMaxBytes_Type = Unsigned32
_CnfTopFlowsMatchMaxBytes_Object = MibScalar
cnfTopFlowsMatchMaxBytes = _CnfTopFlowsMatchMaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 33),
    _CnfTopFlowsMatchMaxBytes_Type()
)
cnfTopFlowsMatchMaxBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchMaxBytes.setStatus("current")
_CnfTopFlowsMatchDirection_Type = NfFlowDirectionTypes
_CnfTopFlowsMatchDirection_Object = MibScalar
cnfTopFlowsMatchDirection = _CnfTopFlowsMatchDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 34),
    _CnfTopFlowsMatchDirection_Type()
)
cnfTopFlowsMatchDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsMatchDirection.setStatus("current")
_CnfTopFlowsGenerate_Type = TruthValue
_CnfTopFlowsGenerate_Object = MibScalar
cnfTopFlowsGenerate = _CnfTopFlowsGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 35),
    _CnfTopFlowsGenerate_Type()
)
cnfTopFlowsGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfTopFlowsGenerate.setStatus("current")
_CnfTopFlowsReportAvailable_Type = TruthValue
_CnfTopFlowsReportAvailable_Object = MibScalar
cnfTopFlowsReportAvailable = _CnfTopFlowsReportAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 36),
    _CnfTopFlowsReportAvailable_Type()
)
cnfTopFlowsReportAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsReportAvailable.setStatus("current")


class _CnfTopFlowsNextGenActionEffect_Type(Integer32):
    """Custom type cnfTopFlowsNextGenActionEffect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generate", 2),
          ("noOp", 1))
    )


_CnfTopFlowsNextGenActionEffect_Type.__name__ = "Integer32"
_CnfTopFlowsNextGenActionEffect_Object = MibScalar
cnfTopFlowsNextGenActionEffect = _CnfTopFlowsNextGenActionEffect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 37),
    _CnfTopFlowsNextGenActionEffect_Type()
)
cnfTopFlowsNextGenActionEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsNextGenActionEffect.setStatus("current")


class _CnfTopFlowsReportSource_Type(Integer32):
    """Custom type cnfTopFlowsReportSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("hardware", 2),
          ("other", 1),
          ("software", 3))
    )


_CnfTopFlowsReportSource_Type.__name__ = "Integer32"
_CnfTopFlowsReportSource_Object = MibScalar
cnfTopFlowsReportSource = _CnfTopFlowsReportSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 1, 7, 38),
    _CnfTopFlowsReportSource_Type()
)
cnfTopFlowsReportSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfTopFlowsReportSource.setStatus("current")
_CiscoNetflowMIBConform_ObjectIdentity = ObjectIdentity
ciscoNetflowMIBConform = _CiscoNetflowMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2)
)
_CnfMIBCompliances_ObjectIdentity = ObjectIdentity
cnfMIBCompliances = _CnfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 1)
)
_CnfMIBGroups_ObjectIdentity = ObjectIdentity
cnfMIBGroups = _CnfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2)
)

# Managed Objects groups

cnfCacheInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 1)
)
cnfCacheInfoGroup.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfCINetflowEnable"),
        ("CISCO-NETFLOW-MIB", "cnfCICacheEnable"),
        ("CISCO-NETFLOW-MIB", "cnfCICacheEntries"),
        ("CISCO-NETFLOW-MIB", "cnfCIActiveFlows"),
        ("CISCO-NETFLOW-MIB", "cnfCIInactiveFlows"),
        ("CISCO-NETFLOW-MIB", "cnfCIActiveTimeOut"),
        ("CISCO-NETFLOW-MIB", "cnfCIInactiveTimeOut"),
        ("CISCO-NETFLOW-MIB", "cnfCIMinSourceMask"),
        ("CISCO-NETFLOW-MIB", "cnfCIMinDestinationMask"))
)
if mibBuilder.loadTexts:
    cnfCacheInfoGroup.setStatus("current")

cnfProtocolStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 2)
)
cnfProtocolStatGroup.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfPSPacketSizeDistribution"),
        ("CISCO-NETFLOW-MIB", "cnfPSLastClearElapsedTime"),
        ("CISCO-NETFLOW-MIB", "cnfPSExpiredFlows"),
        ("CISCO-NETFLOW-MIB", "cnfPSPackets"),
        ("CISCO-NETFLOW-MIB", "cnfPSBytes"),
        ("CISCO-NETFLOW-MIB", "cnfPSActive"),
        ("CISCO-NETFLOW-MIB", "cnfPSInactive"))
)
if mibBuilder.loadTexts:
    cnfProtocolStatGroup.setStatus("current")

cnfExportInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 3)
)
cnfExportInfoGroup.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfEIExportVersion"),
        ("CISCO-NETFLOW-MIB", "cnfEIPeerAS"),
        ("CISCO-NETFLOW-MIB", "cnfEIOriginAS"),
        ("CISCO-NETFLOW-MIB", "cnfEIBgpNextHop"),
        ("CISCO-NETFLOW-MIB", "cnfEIMaxCollectors"),
        ("CISCO-NETFLOW-MIB", "cnfEICollectorStatus"))
)
if mibBuilder.loadTexts:
    cnfExportInfoGroup.setStatus("current")

cnfExportStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 5)
)
cnfExportStatisticsGroup.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfESSampledPacket"),
        ("CISCO-NETFLOW-MIB", "cnfESExportRate"),
        ("CISCO-NETFLOW-MIB", "cnfESRecordsExported"),
        ("CISCO-NETFLOW-MIB", "cnfESPktsExported"),
        ("CISCO-NETFLOW-MIB", "cnfESPktsFailed"),
        ("CISCO-NETFLOW-MIB", "cnfESPktsDropped"))
)
if mibBuilder.loadTexts:
    cnfExportStatisticsGroup.setStatus("current")

cnfExportTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 6)
)
cnfExportTemplateGroup.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfTemplateOptionsFlag"),
        ("CISCO-NETFLOW-MIB", "cnfTemplateAdded"),
        ("CISCO-NETFLOW-MIB", "cnfTemplateActive"),
        ("CISCO-NETFLOW-MIB", "cnfTemplateAgerPolls"),
        ("CISCO-NETFLOW-MIB", "cnfTemplateExportVer9Enable"),
        ("CISCO-NETFLOW-MIB", "cnfTemplateExportVer9TplTimeout"),
        ("CISCO-NETFLOW-MIB", "cnfTemplateExportVer9OptTimeout"),
        ("CISCO-NETFLOW-MIB", "cnfTemplateExportVer9TplRefreshRate"),
        ("CISCO-NETFLOW-MIB", "cnfTemplateExportVer9OptRefreshRate"))
)
if mibBuilder.loadTexts:
    cnfExportTemplateGroup.setStatus("current")

cnfTopFlowsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 7)
)
cnfTopFlowsGroup.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfTopFlowsTimeStamp"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsTopN"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsAvailableFlows"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchingFlows"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsTotalFlows"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSortBy"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsCacheTimeout"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsNhAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsNhAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcPort"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstPort"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcAS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstAS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsInputIfIndex"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsOutputIfIndex"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsFirstSwitched"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsLastSwitched"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsTOS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsProtocol"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsTCPFlags"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSamplerID"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsClassID"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsFlags"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsBytes"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsPackets"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchNhAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchNhAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchNhAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcPortLo"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcPortHi"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstPortLo"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstPortHi"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcAS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstAS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchInputIf"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchOutputIf"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchTOSByte"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchProtocol"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSampler"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchClass"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchMinPackets"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchMaxPackets"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchMinBytes"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchMaxBytes"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDirection"))
)
if mibBuilder.loadTexts:
    cnfTopFlowsGroup.setStatus("deprecated")

cnfTopFlowsDataGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 8)
)
cnfTopFlowsDataGroup1.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfTopFlowsTimeStamp"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsTopN"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsAvailableFlows"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsTotalFlows"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSortBy"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcPort"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstPort"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsProtocol"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsBytes"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsPackets"))
)
if mibBuilder.loadTexts:
    cnfTopFlowsDataGroup1.setStatus("current")

cnfTopFlowsDataGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 9)
)
cnfTopFlowsDataGroup2.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfTopFlowsCacheTimeout"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsNhAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsNhAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSrcAS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsDstAS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsInputIfIndex"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsOutputIfIndex"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsFirstSwitched"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsLastSwitched"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsTOS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsTCPFlags"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsSamplerID"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsClassID"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsFlags"))
)
if mibBuilder.loadTexts:
    cnfTopFlowsDataGroup2.setStatus("current")

cnfTopFlowsVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 10)
)
cnfTopFlowsVlanGroup.setObjects(
    ("CISCO-NETFLOW-MIB", "cnfTopFlowsVlan")
)
if mibBuilder.loadTexts:
    cnfTopFlowsVlanGroup.setStatus("current")

cnfTopFlowsControlGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 11)
)
cnfTopFlowsControlGroup1.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchingFlows"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchNhAddressType"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchNhAddress"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchNhAddressMask"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcPortLo"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcPortHi"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstPortLo"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstPortHi"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSrcAS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDstAS"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchInputIf"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchOutputIf"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchTOSByte"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchProtocol"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchSampler"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchClass"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchMinPackets"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchMaxPackets"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchMinBytes"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchMaxBytes"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsMatchDirection"))
)
if mibBuilder.loadTexts:
    cnfTopFlowsControlGroup1.setStatus("current")

cnfTopFlowsControlGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 12)
)
cnfTopFlowsControlGroup2.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfTopFlowsGenerate"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsReportAvailable"))
)
if mibBuilder.loadTexts:
    cnfTopFlowsControlGroup2.setStatus("current")

cnfMcastNetflowControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 13)
)
cnfMcastNetflowControlGroup.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfCIMcastNetflowEnable"),
        ("CISCO-NETFLOW-MIB", "cnfCIMcastNetflowRPFFailedEnable"))
)
if mibBuilder.loadTexts:
    cnfMcastNetflowControlGroup.setStatus("current")

cnfBridgedFlowStatsCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 14)
)
cnfBridgedFlowStatsCtrlGroup.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfCIBridgedFlowStatsCrtEnable"),
        ("CISCO-NETFLOW-MIB", "cnfCIBridgedFlowStatsExpEnable"))
)
if mibBuilder.loadTexts:
    cnfBridgedFlowStatsCtrlGroup.setStatus("current")

cnfTopFlowsReportGenerateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 2, 15)
)
cnfTopFlowsReportGenerateGroup.setObjects(
      *(("CISCO-NETFLOW-MIB", "cnfTopFlowsNextGenActionEffect"),
        ("CISCO-NETFLOW-MIB", "cnfTopFlowsReportSource"))
)
if mibBuilder.loadTexts:
    cnfTopFlowsReportGenerateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cnfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cnfMIBCompliance.setStatus(
        "deprecated"
    )

cnfMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cnfMIBCompliance1.setStatus(
        "deprecated"
    )

cnfMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cnfMIBCompliance2.setStatus(
        "deprecated"
    )

cnfMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 387, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cnfMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NETFLOW-MIB",
    **{"NfInterfaceDirectionTypes": NfInterfaceDirectionTypes,
       "NfCacheTypes": NfCacheTypes,
       "NfProtocolTypes": NfProtocolTypes,
       "NfTemplateTypes": NfTemplateTypes,
       "NfTopFlowsSortTypes": NfTopFlowsSortTypes,
       "NfFlowDirectionTypes": NfFlowDirectionTypes,
       "ciscoNetflowMIB": ciscoNetflowMIB,
       "ciscoNetflowMIBNotifs": ciscoNetflowMIBNotifs,
       "ciscoNetflowMIBObjects": ciscoNetflowMIBObjects,
       "cnfCacheInfo": cnfCacheInfo,
       "cnfCIInterfaceTable": cnfCIInterfaceTable,
       "cnfCIInterfaceEntry": cnfCIInterfaceEntry,
       "cnfCINetflowEnable": cnfCINetflowEnable,
       "cnfCIMcastNetflowEnable": cnfCIMcastNetflowEnable,
       "cnfCICacheTable": cnfCICacheTable,
       "cnfCICacheEntry": cnfCICacheEntry,
       "cnfCICacheType": cnfCICacheType,
       "cnfCICacheEnable": cnfCICacheEnable,
       "cnfCICacheEntries": cnfCICacheEntries,
       "cnfCIActiveFlows": cnfCIActiveFlows,
       "cnfCIInactiveFlows": cnfCIInactiveFlows,
       "cnfCIActiveTimeOut": cnfCIActiveTimeOut,
       "cnfCIInactiveTimeOut": cnfCIInactiveTimeOut,
       "cnfCIMinSourceMask": cnfCIMinSourceMask,
       "cnfCIMinDestinationMask": cnfCIMinDestinationMask,
       "cnfCIBridgedFlowStatsCtrlTable": cnfCIBridgedFlowStatsCtrlTable,
       "cnfCIBridgedFlowStatsCtrlEntry": cnfCIBridgedFlowStatsCtrlEntry,
       "cnfCIBridgedFlowVlan": cnfCIBridgedFlowVlan,
       "cnfCIBridgedFlowStatsCrtEnable": cnfCIBridgedFlowStatsCrtEnable,
       "cnfCIBridgedFlowStatsExpEnable": cnfCIBridgedFlowStatsExpEnable,
       "cnfCIMcastNetflowRPFFailedEnable": cnfCIMcastNetflowRPFFailedEnable,
       "cnfExportInfo": cnfExportInfo,
       "cnfEIExportInfoTable": cnfEIExportInfoTable,
       "cnfEIExportInfoEntry": cnfEIExportInfoEntry,
       "cnfEIExportVersion": cnfEIExportVersion,
       "cnfEIPeerAS": cnfEIPeerAS,
       "cnfEIOriginAS": cnfEIOriginAS,
       "cnfEIBgpNextHop": cnfEIBgpNextHop,
       "cnfEIMaxCollectors": cnfEIMaxCollectors,
       "cnfEICollectorTable": cnfEICollectorTable,
       "cnfEICollectorEntry": cnfEICollectorEntry,
       "cnfEICollectorAddressType": cnfEICollectorAddressType,
       "cnfEICollectorAddress": cnfEICollectorAddress,
       "cnfEICollectorPort": cnfEICollectorPort,
       "cnfEICollectorStatus": cnfEICollectorStatus,
       "cnfExportStatistics": cnfExportStatistics,
       "cnfESSampledPacket": cnfESSampledPacket,
       "cnfESExportRate": cnfESExportRate,
       "cnfESRecordsExported": cnfESRecordsExported,
       "cnfESPktsExported": cnfESPktsExported,
       "cnfESPktsFailed": cnfESPktsFailed,
       "cnfESPktsDropped": cnfESPktsDropped,
       "cnfProtocolStatistics": cnfProtocolStatistics,
       "cnfPSPacketSizeDistribution": cnfPSPacketSizeDistribution,
       "cnfPSLastClearElapsedTime": cnfPSLastClearElapsedTime,
       "cnfPSProtocolStatTable": cnfPSProtocolStatTable,
       "cnfPSProtocolStatEntry": cnfPSProtocolStatEntry,
       "cnfPSProtocolType": cnfPSProtocolType,
       "cnfPSExpiredFlows": cnfPSExpiredFlows,
       "cnfPSPackets": cnfPSPackets,
       "cnfPSBytes": cnfPSBytes,
       "cnfPSActive": cnfPSActive,
       "cnfPSInactive": cnfPSInactive,
       "cnfExportTemplate": cnfExportTemplate,
       "cnfTemplateOptionsFlag": cnfTemplateOptionsFlag,
       "cnfTemplateTable": cnfTemplateTable,
       "cnfTemplateEntry": cnfTemplateEntry,
       "cnfTemplateType": cnfTemplateType,
       "cnfTemplateAdded": cnfTemplateAdded,
       "cnfTemplateActive": cnfTemplateActive,
       "cnfTemplateAgerPolls": cnfTemplateAgerPolls,
       "cnfTemplateExportInfoTable": cnfTemplateExportInfoTable,
       "cnfTemplateExportInfoEntry": cnfTemplateExportInfoEntry,
       "cnfTemplateExportVer9Enable": cnfTemplateExportVer9Enable,
       "cnfTemplateExportVer9TplTimeout": cnfTemplateExportVer9TplTimeout,
       "cnfTemplateExportVer9OptTimeout": cnfTemplateExportVer9OptTimeout,
       "cnfTemplateExportVer9TplRefreshRate": cnfTemplateExportVer9TplRefreshRate,
       "cnfTemplateExportVer9OptRefreshRate": cnfTemplateExportVer9OptRefreshRate,
       "cnfTopFlows": cnfTopFlows,
       "cnfTopFlowsTimeStamp": cnfTopFlowsTimeStamp,
       "cnfTopFlowsTopN": cnfTopFlowsTopN,
       "cnfTopFlowsAvailableFlows": cnfTopFlowsAvailableFlows,
       "cnfTopFlowsMatchingFlows": cnfTopFlowsMatchingFlows,
       "cnfTopFlowsTotalFlows": cnfTopFlowsTotalFlows,
       "cnfTopFlowsSortBy": cnfTopFlowsSortBy,
       "cnfTopFlowsCacheTimeout": cnfTopFlowsCacheTimeout,
       "cnfTopFlowsTable": cnfTopFlowsTable,
       "cnfTopFlowsTableEntry": cnfTopFlowsTableEntry,
       "cnfTopFlowsIndex": cnfTopFlowsIndex,
       "cnfTopFlowsSrcAddressType": cnfTopFlowsSrcAddressType,
       "cnfTopFlowsSrcAddress": cnfTopFlowsSrcAddress,
       "cnfTopFlowsSrcAddressMask": cnfTopFlowsSrcAddressMask,
       "cnfTopFlowsDstAddressType": cnfTopFlowsDstAddressType,
       "cnfTopFlowsDstAddress": cnfTopFlowsDstAddress,
       "cnfTopFlowsDstAddressMask": cnfTopFlowsDstAddressMask,
       "cnfTopFlowsNhAddressType": cnfTopFlowsNhAddressType,
       "cnfTopFlowsNhAddress": cnfTopFlowsNhAddress,
       "cnfTopFlowsSrcPort": cnfTopFlowsSrcPort,
       "cnfTopFlowsDstPort": cnfTopFlowsDstPort,
       "cnfTopFlowsSrcAS": cnfTopFlowsSrcAS,
       "cnfTopFlowsDstAS": cnfTopFlowsDstAS,
       "cnfTopFlowsInputIfIndex": cnfTopFlowsInputIfIndex,
       "cnfTopFlowsOutputIfIndex": cnfTopFlowsOutputIfIndex,
       "cnfTopFlowsFirstSwitched": cnfTopFlowsFirstSwitched,
       "cnfTopFlowsLastSwitched": cnfTopFlowsLastSwitched,
       "cnfTopFlowsTOS": cnfTopFlowsTOS,
       "cnfTopFlowsProtocol": cnfTopFlowsProtocol,
       "cnfTopFlowsTCPFlags": cnfTopFlowsTCPFlags,
       "cnfTopFlowsSamplerID": cnfTopFlowsSamplerID,
       "cnfTopFlowsClassID": cnfTopFlowsClassID,
       "cnfTopFlowsFlags": cnfTopFlowsFlags,
       "cnfTopFlowsBytes": cnfTopFlowsBytes,
       "cnfTopFlowsPackets": cnfTopFlowsPackets,
       "cnfTopFlowsVlan": cnfTopFlowsVlan,
       "cnfTopFlowsMatchSrcAddressType": cnfTopFlowsMatchSrcAddressType,
       "cnfTopFlowsMatchSrcAddress": cnfTopFlowsMatchSrcAddress,
       "cnfTopFlowsMatchSrcAddressMask": cnfTopFlowsMatchSrcAddressMask,
       "cnfTopFlowsMatchDstAddressType": cnfTopFlowsMatchDstAddressType,
       "cnfTopFlowsMatchDstAddress": cnfTopFlowsMatchDstAddress,
       "cnfTopFlowsMatchDstAddressMask": cnfTopFlowsMatchDstAddressMask,
       "cnfTopFlowsMatchNhAddressType": cnfTopFlowsMatchNhAddressType,
       "cnfTopFlowsMatchNhAddress": cnfTopFlowsMatchNhAddress,
       "cnfTopFlowsMatchNhAddressMask": cnfTopFlowsMatchNhAddressMask,
       "cnfTopFlowsMatchSrcPortLo": cnfTopFlowsMatchSrcPortLo,
       "cnfTopFlowsMatchSrcPortHi": cnfTopFlowsMatchSrcPortHi,
       "cnfTopFlowsMatchDstPortLo": cnfTopFlowsMatchDstPortLo,
       "cnfTopFlowsMatchDstPortHi": cnfTopFlowsMatchDstPortHi,
       "cnfTopFlowsMatchSrcAS": cnfTopFlowsMatchSrcAS,
       "cnfTopFlowsMatchDstAS": cnfTopFlowsMatchDstAS,
       "cnfTopFlowsMatchInputIf": cnfTopFlowsMatchInputIf,
       "cnfTopFlowsMatchOutputIf": cnfTopFlowsMatchOutputIf,
       "cnfTopFlowsMatchTOSByte": cnfTopFlowsMatchTOSByte,
       "cnfTopFlowsMatchProtocol": cnfTopFlowsMatchProtocol,
       "cnfTopFlowsMatchSampler": cnfTopFlowsMatchSampler,
       "cnfTopFlowsMatchClass": cnfTopFlowsMatchClass,
       "cnfTopFlowsMatchMinPackets": cnfTopFlowsMatchMinPackets,
       "cnfTopFlowsMatchMaxPackets": cnfTopFlowsMatchMaxPackets,
       "cnfTopFlowsMatchMinBytes": cnfTopFlowsMatchMinBytes,
       "cnfTopFlowsMatchMaxBytes": cnfTopFlowsMatchMaxBytes,
       "cnfTopFlowsMatchDirection": cnfTopFlowsMatchDirection,
       "cnfTopFlowsGenerate": cnfTopFlowsGenerate,
       "cnfTopFlowsReportAvailable": cnfTopFlowsReportAvailable,
       "cnfTopFlowsNextGenActionEffect": cnfTopFlowsNextGenActionEffect,
       "cnfTopFlowsReportSource": cnfTopFlowsReportSource,
       "ciscoNetflowMIBConform": ciscoNetflowMIBConform,
       "cnfMIBCompliances": cnfMIBCompliances,
       "cnfMIBCompliance": cnfMIBCompliance,
       "cnfMIBCompliance1": cnfMIBCompliance1,
       "cnfMIBCompliance2": cnfMIBCompliance2,
       "cnfMIBCompliance3": cnfMIBCompliance3,
       "cnfMIBGroups": cnfMIBGroups,
       "cnfCacheInfoGroup": cnfCacheInfoGroup,
       "cnfProtocolStatGroup": cnfProtocolStatGroup,
       "cnfExportInfoGroup": cnfExportInfoGroup,
       "cnfExportStatisticsGroup": cnfExportStatisticsGroup,
       "cnfExportTemplateGroup": cnfExportTemplateGroup,
       "cnfTopFlowsGroup": cnfTopFlowsGroup,
       "cnfTopFlowsDataGroup1": cnfTopFlowsDataGroup1,
       "cnfTopFlowsDataGroup2": cnfTopFlowsDataGroup2,
       "cnfTopFlowsVlanGroup": cnfTopFlowsVlanGroup,
       "cnfTopFlowsControlGroup1": cnfTopFlowsControlGroup1,
       "cnfTopFlowsControlGroup2": cnfTopFlowsControlGroup2,
       "cnfMcastNetflowControlGroup": cnfMcastNetflowControlGroup,
       "cnfBridgedFlowStatsCtrlGroup": cnfBridgedFlowStatsCtrlGroup,
       "cnfTopFlowsReportGenerateGroup": cnfTopFlowsReportGenerateGroup}
)
