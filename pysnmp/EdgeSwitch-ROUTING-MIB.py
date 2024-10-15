# SNMP MIB module (EdgeSwitch-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-ROUTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:05 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "EdgeSwitch-REF-MIB",
    "fastPath")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(RouterID,
 ospfAreaEntry,
 ospfIfEntry,
 ospfVirtIfEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "RouterID",
    "ospfAreaEntry",
    "ospfIfEntry",
    "ospfVirtIfEntry")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfEntry")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(vrrpOperVrId,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperVrId")


# MODULE-IDENTITY

fastPathRouting = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2)
)
fastPathRouting.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00",
         "2003-11-21 00:00",
         "2003-04-02 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SpfTimerRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class AutoCostRefBw(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967),
    )



# MIB Managed Objects in the order of their OIDs

_AgentSwitchArpGroup_ObjectIdentity = ObjectIdentity
agentSwitchArpGroup = _AgentSwitchArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1)
)


class _AgentSwitchArpAgeoutTime_Type(Integer32):
    """Custom type agentSwitchArpAgeoutTime based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 21600),
    )


_AgentSwitchArpAgeoutTime_Type.__name__ = "Integer32"
_AgentSwitchArpAgeoutTime_Object = MibScalar
agentSwitchArpAgeoutTime = _AgentSwitchArpAgeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 1),
    _AgentSwitchArpAgeoutTime_Type()
)
agentSwitchArpAgeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpAgeoutTime.setStatus("current")


class _AgentSwitchArpResponseTime_Type(Integer32):
    """Custom type agentSwitchArpResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentSwitchArpResponseTime_Type.__name__ = "Integer32"
_AgentSwitchArpResponseTime_Object = MibScalar
agentSwitchArpResponseTime = _AgentSwitchArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 2),
    _AgentSwitchArpResponseTime_Type()
)
agentSwitchArpResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpResponseTime.setStatus("current")


class _AgentSwitchArpMaxRetries_Type(Integer32):
    """Custom type agentSwitchArpMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AgentSwitchArpMaxRetries_Type.__name__ = "Integer32"
_AgentSwitchArpMaxRetries_Object = MibScalar
agentSwitchArpMaxRetries = _AgentSwitchArpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 3),
    _AgentSwitchArpMaxRetries_Type()
)
agentSwitchArpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpMaxRetries.setStatus("current")
_AgentSwitchArpCacheSize_Type = Integer32
_AgentSwitchArpCacheSize_Object = MibScalar
agentSwitchArpCacheSize = _AgentSwitchArpCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 4),
    _AgentSwitchArpCacheSize_Type()
)
agentSwitchArpCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpCacheSize.setStatus("current")


class _AgentSwitchArpDynamicRenew_Type(Integer32):
    """Custom type agentSwitchArpDynamicRenew based on Integer32"""
    defaultValue = 1

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


_AgentSwitchArpDynamicRenew_Type.__name__ = "Integer32"
_AgentSwitchArpDynamicRenew_Object = MibScalar
agentSwitchArpDynamicRenew = _AgentSwitchArpDynamicRenew_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 5),
    _AgentSwitchArpDynamicRenew_Type()
)
agentSwitchArpDynamicRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpDynamicRenew.setStatus("current")
_AgentSwitchArpTotalEntryCountCurrent_Type = Gauge32
_AgentSwitchArpTotalEntryCountCurrent_Object = MibScalar
agentSwitchArpTotalEntryCountCurrent = _AgentSwitchArpTotalEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 6),
    _AgentSwitchArpTotalEntryCountCurrent_Type()
)
agentSwitchArpTotalEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpTotalEntryCountCurrent.setStatus("current")
_AgentSwitchArpTotalEntryCountPeak_Type = Gauge32
_AgentSwitchArpTotalEntryCountPeak_Object = MibScalar
agentSwitchArpTotalEntryCountPeak = _AgentSwitchArpTotalEntryCountPeak_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 7),
    _AgentSwitchArpTotalEntryCountPeak_Type()
)
agentSwitchArpTotalEntryCountPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpTotalEntryCountPeak.setStatus("current")
_AgentSwitchArpStaticEntryCountCurrent_Type = Gauge32
_AgentSwitchArpStaticEntryCountCurrent_Object = MibScalar
agentSwitchArpStaticEntryCountCurrent = _AgentSwitchArpStaticEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 8),
    _AgentSwitchArpStaticEntryCountCurrent_Type()
)
agentSwitchArpStaticEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpStaticEntryCountCurrent.setStatus("current")
_AgentSwitchArpStaticEntryCountMax_Type = Integer32
_AgentSwitchArpStaticEntryCountMax_Object = MibScalar
agentSwitchArpStaticEntryCountMax = _AgentSwitchArpStaticEntryCountMax_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 9),
    _AgentSwitchArpStaticEntryCountMax_Type()
)
agentSwitchArpStaticEntryCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpStaticEntryCountMax.setStatus("current")
_AgentSwitchArpTable_Object = MibTable
agentSwitchArpTable = _AgentSwitchArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    agentSwitchArpTable.setStatus("obsolete")
_AgentSwitchArpEntry_Object = MibTableRow
agentSwitchArpEntry = _AgentSwitchArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 10, 1)
)
agentSwitchArpEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchArpIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchArpEntry.setStatus("obsolete")
_AgentSwitchArpAge_Type = TimeTicks
_AgentSwitchArpAge_Object = MibTableColumn
agentSwitchArpAge = _AgentSwitchArpAge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 10, 1, 1),
    _AgentSwitchArpAge_Type()
)
agentSwitchArpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpAge.setStatus("obsolete")
_AgentSwitchArpIpAddress_Type = IpAddress
_AgentSwitchArpIpAddress_Object = MibTableColumn
agentSwitchArpIpAddress = _AgentSwitchArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 10, 1, 2),
    _AgentSwitchArpIpAddress_Type()
)
agentSwitchArpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpIpAddress.setStatus("obsolete")
_AgentSwitchArpMacAddress_Type = PhysAddress
_AgentSwitchArpMacAddress_Object = MibTableColumn
agentSwitchArpMacAddress = _AgentSwitchArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 10, 1, 3),
    _AgentSwitchArpMacAddress_Type()
)
agentSwitchArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchArpMacAddress.setStatus("obsolete")
_AgentSwitchArpInterface_Type = Integer32
_AgentSwitchArpInterface_Object = MibTableColumn
agentSwitchArpInterface = _AgentSwitchArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 10, 1, 4),
    _AgentSwitchArpInterface_Type()
)
agentSwitchArpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchArpInterface.setStatus("obsolete")


class _AgentSwitchArpType_Type(Integer32):
    """Custom type agentSwitchArpType based on Integer32"""
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
        *(("dynamic", 4),
          ("gateway", 2),
          ("local", 1),
          ("static", 3))
    )


_AgentSwitchArpType_Type.__name__ = "Integer32"
_AgentSwitchArpType_Object = MibTableColumn
agentSwitchArpType = _AgentSwitchArpType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 10, 1, 5),
    _AgentSwitchArpType_Type()
)
agentSwitchArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpType.setStatus("obsolete")
_AgentSwitchArpStatus_Type = RowStatus
_AgentSwitchArpStatus_Object = MibTableColumn
agentSwitchArpStatus = _AgentSwitchArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 10, 1, 6),
    _AgentSwitchArpStatus_Type()
)
agentSwitchArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpStatus.setStatus("obsolete")
_AgentSwitchLocalProxyArpTable_Object = MibTable
agentSwitchLocalProxyArpTable = _AgentSwitchLocalProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    agentSwitchLocalProxyArpTable.setStatus("current")
_AgentSwitchLocalProxyArpEntry_Object = MibTableRow
agentSwitchLocalProxyArpEntry = _AgentSwitchLocalProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 11, 1)
)
agentSwitchLocalProxyArpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchLocalProxyArpEntry.setStatus("current")


class _AgentSwitchLocalProxyArpMode_Type(Integer32):
    """Custom type agentSwitchLocalProxyArpMode based on Integer32"""
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


_AgentSwitchLocalProxyArpMode_Type.__name__ = "Integer32"
_AgentSwitchLocalProxyArpMode_Object = MibTableColumn
agentSwitchLocalProxyArpMode = _AgentSwitchLocalProxyArpMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 11, 1, 1),
    _AgentSwitchLocalProxyArpMode_Type()
)
agentSwitchLocalProxyArpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchLocalProxyArpMode.setStatus("current")
_AgentSwitchIntfArpTable_Object = MibTable
agentSwitchIntfArpTable = _AgentSwitchIntfArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 12)
)
if mibBuilder.loadTexts:
    agentSwitchIntfArpTable.setStatus("current")
_AgentSwitchIntfArpEntry_Object = MibTableRow
agentSwitchIntfArpEntry = _AgentSwitchIntfArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 12, 1)
)
agentSwitchIntfArpEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIntfArpIpAddress"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIntfArpIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchIntfArpEntry.setStatus("current")
_AgentSwitchIntfArpIpAddress_Type = IpAddress
_AgentSwitchIntfArpIpAddress_Object = MibTableColumn
agentSwitchIntfArpIpAddress = _AgentSwitchIntfArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 12, 1, 1),
    _AgentSwitchIntfArpIpAddress_Type()
)
agentSwitchIntfArpIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchIntfArpIpAddress.setStatus("current")
_AgentSwitchIntfArpIfIndex_Type = InterfaceIndex
_AgentSwitchIntfArpIfIndex_Object = MibTableColumn
agentSwitchIntfArpIfIndex = _AgentSwitchIntfArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 12, 1, 2),
    _AgentSwitchIntfArpIfIndex_Type()
)
agentSwitchIntfArpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchIntfArpIfIndex.setStatus("current")
_AgentSwitchIntfArpAge_Type = TimeTicks
_AgentSwitchIntfArpAge_Object = MibTableColumn
agentSwitchIntfArpAge = _AgentSwitchIntfArpAge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 12, 1, 3),
    _AgentSwitchIntfArpAge_Type()
)
agentSwitchIntfArpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIntfArpAge.setStatus("current")
_AgentSwitchIntfArpMacAddress_Type = PhysAddress
_AgentSwitchIntfArpMacAddress_Object = MibTableColumn
agentSwitchIntfArpMacAddress = _AgentSwitchIntfArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 12, 1, 4),
    _AgentSwitchIntfArpMacAddress_Type()
)
agentSwitchIntfArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIntfArpMacAddress.setStatus("current")


class _AgentSwitchIntfArpType_Type(Integer32):
    """Custom type agentSwitchIntfArpType based on Integer32"""
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
        *(("dynamic", 4),
          ("gateway", 2),
          ("local", 1),
          ("static", 3))
    )


_AgentSwitchIntfArpType_Type.__name__ = "Integer32"
_AgentSwitchIntfArpType_Object = MibTableColumn
agentSwitchIntfArpType = _AgentSwitchIntfArpType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 12, 1, 5),
    _AgentSwitchIntfArpType_Type()
)
agentSwitchIntfArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIntfArpType.setStatus("current")
_AgentSwitchIntfArpStatus_Type = RowStatus
_AgentSwitchIntfArpStatus_Object = MibTableColumn
agentSwitchIntfArpStatus = _AgentSwitchIntfArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 1, 12, 1, 6),
    _AgentSwitchIntfArpStatus_Type()
)
agentSwitchIntfArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIntfArpStatus.setStatus("current")
_AgentSwitchIpGroup_ObjectIdentity = ObjectIdentity
agentSwitchIpGroup = _AgentSwitchIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2)
)


class _AgentSwitchIpRoutingMode_Type(Integer32):
    """Custom type agentSwitchIpRoutingMode based on Integer32"""
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


_AgentSwitchIpRoutingMode_Type.__name__ = "Integer32"
_AgentSwitchIpRoutingMode_Object = MibScalar
agentSwitchIpRoutingMode = _AgentSwitchIpRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 1),
    _AgentSwitchIpRoutingMode_Type()
)
agentSwitchIpRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRoutingMode.setStatus("current")
_AgentSwitchIpDefaultGateway_Type = IpAddress
_AgentSwitchIpDefaultGateway_Object = MibScalar
agentSwitchIpDefaultGateway = _AgentSwitchIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 2),
    _AgentSwitchIpDefaultGateway_Type()
)
agentSwitchIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpDefaultGateway.setStatus("current")
_AgentSwitchIpInterfaceTable_Object = MibTable
agentSwitchIpInterfaceTable = _AgentSwitchIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceTable.setStatus("current")
_AgentSwitchIpInterfaceEntry_Object = MibTableRow
agentSwitchIpInterfaceEntry = _AgentSwitchIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1)
)
agentSwitchIpInterfaceEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceEntry.setStatus("current")


class _AgentSwitchIpInterfaceIfIndex_Type(Integer32):
    """Custom type agentSwitchIpInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchIpInterfaceIfIndex_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceIfIndex_Object = MibTableColumn
agentSwitchIpInterfaceIfIndex = _AgentSwitchIpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 1),
    _AgentSwitchIpInterfaceIfIndex_Type()
)
agentSwitchIpInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIfIndex.setStatus("current")


class _AgentSwitchIPAddressConfigMethod_Type(Integer32):
    """Custom type agentSwitchIPAddressConfigMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("manual", 1),
          ("none", 0))
    )


_AgentSwitchIPAddressConfigMethod_Type.__name__ = "Integer32"
_AgentSwitchIPAddressConfigMethod_Object = MibTableColumn
agentSwitchIPAddressConfigMethod = _AgentSwitchIPAddressConfigMethod_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 2),
    _AgentSwitchIPAddressConfigMethod_Type()
)
agentSwitchIPAddressConfigMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIPAddressConfigMethod.setStatus("current")
_AgentSwitchIpInterfaceIpAddress_Type = IpAddress
_AgentSwitchIpInterfaceIpAddress_Object = MibTableColumn
agentSwitchIpInterfaceIpAddress = _AgentSwitchIpInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 3),
    _AgentSwitchIpInterfaceIpAddress_Type()
)
agentSwitchIpInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIpAddress.setStatus("current")
_AgentSwitchIpInterfaceNetMask_Type = IpAddress
_AgentSwitchIpInterfaceNetMask_Object = MibTableColumn
agentSwitchIpInterfaceNetMask = _AgentSwitchIpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 4),
    _AgentSwitchIpInterfaceNetMask_Type()
)
agentSwitchIpInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceNetMask.setStatus("current")


class _AgentSwitchIpInterfaceClearIp_Type(Integer32):
    """Custom type agentSwitchIpInterfaceClearIp based on Integer32"""
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


_AgentSwitchIpInterfaceClearIp_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceClearIp_Object = MibTableColumn
agentSwitchIpInterfaceClearIp = _AgentSwitchIpInterfaceClearIp_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 5),
    _AgentSwitchIpInterfaceClearIp_Type()
)
agentSwitchIpInterfaceClearIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceClearIp.setStatus("current")


class _AgentSwitchIpInterfaceRoutingMode_Type(Integer32):
    """Custom type agentSwitchIpInterfaceRoutingMode based on Integer32"""
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


_AgentSwitchIpInterfaceRoutingMode_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceRoutingMode_Object = MibTableColumn
agentSwitchIpInterfaceRoutingMode = _AgentSwitchIpInterfaceRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 6),
    _AgentSwitchIpInterfaceRoutingMode_Type()
)
agentSwitchIpInterfaceRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceRoutingMode.setStatus("current")


class _AgentSwitchIpInterfaceProxyARPMode_Type(Integer32):
    """Custom type agentSwitchIpInterfaceProxyARPMode based on Integer32"""
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


_AgentSwitchIpInterfaceProxyARPMode_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceProxyARPMode_Object = MibTableColumn
agentSwitchIpInterfaceProxyARPMode = _AgentSwitchIpInterfaceProxyARPMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 7),
    _AgentSwitchIpInterfaceProxyARPMode_Type()
)
agentSwitchIpInterfaceProxyARPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceProxyARPMode.setStatus("current")


class _AgentSwitchIpInterfaceMtuValue_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceMtuValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(68, 9198),
    )


_AgentSwitchIpInterfaceMtuValue_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceMtuValue_Object = MibTableColumn
agentSwitchIpInterfaceMtuValue = _AgentSwitchIpInterfaceMtuValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 8),
    _AgentSwitchIpInterfaceMtuValue_Type()
)
agentSwitchIpInterfaceMtuValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceMtuValue.setStatus("current")


class _AgentSwitchIpInterfaceBandwidth_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000000),
    )


_AgentSwitchIpInterfaceBandwidth_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceBandwidth_Object = MibTableColumn
agentSwitchIpInterfaceBandwidth = _AgentSwitchIpInterfaceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 9),
    _AgentSwitchIpInterfaceBandwidth_Type()
)
agentSwitchIpInterfaceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceBandwidth.setStatus("current")
_AgentSwitchIpInterfaceUnnumberedIfIndex_Type = InterfaceIndexOrZero
_AgentSwitchIpInterfaceUnnumberedIfIndex_Object = MibTableColumn
agentSwitchIpInterfaceUnnumberedIfIndex = _AgentSwitchIpInterfaceUnnumberedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 10),
    _AgentSwitchIpInterfaceUnnumberedIfIndex_Type()
)
agentSwitchIpInterfaceUnnumberedIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceUnnumberedIfIndex.setStatus("current")


class _AgentSwitchIpInterfaceIcmpUnreachables_Type(Integer32):
    """Custom type agentSwitchIpInterfaceIcmpUnreachables based on Integer32"""
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


_AgentSwitchIpInterfaceIcmpUnreachables_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceIcmpUnreachables_Object = MibTableColumn
agentSwitchIpInterfaceIcmpUnreachables = _AgentSwitchIpInterfaceIcmpUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 11),
    _AgentSwitchIpInterfaceIcmpUnreachables_Type()
)
agentSwitchIpInterfaceIcmpUnreachables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIcmpUnreachables.setStatus("current")


class _AgentSwitchIpInterfaceIcmpRedirects_Type(Integer32):
    """Custom type agentSwitchIpInterfaceIcmpRedirects based on Integer32"""
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


_AgentSwitchIpInterfaceIcmpRedirects_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceIcmpRedirects_Object = MibTableColumn
agentSwitchIpInterfaceIcmpRedirects = _AgentSwitchIpInterfaceIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 12),
    _AgentSwitchIpInterfaceIcmpRedirects_Type()
)
agentSwitchIpInterfaceIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIcmpRedirects.setStatus("current")


class _AgentSwitchDhcpOperation_Type(Integer32):
    """Custom type agentSwitchDhcpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("release", 2),
          ("renew", 1))
    )


_AgentSwitchDhcpOperation_Type.__name__ = "Integer32"
_AgentSwitchDhcpOperation_Object = MibTableColumn
agentSwitchDhcpOperation = _AgentSwitchDhcpOperation_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 13),
    _AgentSwitchDhcpOperation_Type()
)
agentSwitchDhcpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDhcpOperation.setStatus("current")


class _AgentSwitchIpInterfaceSuppressed_Type(Integer32):
    """Custom type agentSwitchIpInterfaceSuppressed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("suppressed", 1),
          ("unsuppressed", 0))
    )


_AgentSwitchIpInterfaceSuppressed_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceSuppressed_Object = MibTableColumn
agentSwitchIpInterfaceSuppressed = _AgentSwitchIpInterfaceSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 14),
    _AgentSwitchIpInterfaceSuppressed_Type()
)
agentSwitchIpInterfaceSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceSuppressed.setStatus("current")


class _AgentSwitchIpInterfaceNumberOfFlaps_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceNumberOfFlaps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AgentSwitchIpInterfaceNumberOfFlaps_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceNumberOfFlaps_Object = MibTableColumn
agentSwitchIpInterfaceNumberOfFlaps = _AgentSwitchIpInterfaceNumberOfFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 15),
    _AgentSwitchIpInterfaceNumberOfFlaps_Type()
)
agentSwitchIpInterfaceNumberOfFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceNumberOfFlaps.setStatus("current")


class _AgentSwitchIpInterfaceCurrentPenalty_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceCurrentPenalty based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_AgentSwitchIpInterfaceCurrentPenalty_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceCurrentPenalty_Object = MibTableColumn
agentSwitchIpInterfaceCurrentPenalty = _AgentSwitchIpInterfaceCurrentPenalty_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 16),
    _AgentSwitchIpInterfaceCurrentPenalty_Type()
)
agentSwitchIpInterfaceCurrentPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceCurrentPenalty.setStatus("current")


class _AgentSwitchIpInterfaceReUseTime_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceReUseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentSwitchIpInterfaceReUseTime_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceReUseTime_Object = MibTableColumn
agentSwitchIpInterfaceReUseTime = _AgentSwitchIpInterfaceReUseTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 3, 1, 17),
    _AgentSwitchIpInterfaceReUseTime_Type()
)
agentSwitchIpInterfaceReUseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceReUseTime.setStatus("current")
_AgentSwitchIpRouterDiscoveryTable_Object = MibTable
agentSwitchIpRouterDiscoveryTable = _AgentSwitchIpRouterDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryTable.setStatus("current")
_AgentSwitchIpRouterDiscoveryEntry_Object = MibTableRow
agentSwitchIpRouterDiscoveryEntry = _AgentSwitchIpRouterDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 4, 1)
)
agentSwitchIpRouterDiscoveryEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIpRouterDiscoveryIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryEntry.setStatus("current")


class _AgentSwitchIpRouterDiscoveryIfIndex_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchIpRouterDiscoveryIfIndex_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryIfIndex_Object = MibTableColumn
agentSwitchIpRouterDiscoveryIfIndex = _AgentSwitchIpRouterDiscoveryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 4, 1, 1),
    _AgentSwitchIpRouterDiscoveryIfIndex_Type()
)
agentSwitchIpRouterDiscoveryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryIfIndex.setStatus("current")


class _AgentSwitchIpRouterDiscoveryAdvertiseMode_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryAdvertiseMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchIpRouterDiscoveryAdvertiseMode_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryAdvertiseMode_Object = MibTableColumn
agentSwitchIpRouterDiscoveryAdvertiseMode = _AgentSwitchIpRouterDiscoveryAdvertiseMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 4, 1, 2),
    _AgentSwitchIpRouterDiscoveryAdvertiseMode_Type()
)
agentSwitchIpRouterDiscoveryAdvertiseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryAdvertiseMode.setStatus("current")


class _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryMaxAdvertisementInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object = MibTableColumn
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval = _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 4, 1, 3),
    _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type()
)
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setStatus("current")


class _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryMinAdvertisementInterval based on Integer32"""
    defaultValue = 450

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object = MibTableColumn
agentSwitchIpRouterDiscoveryMinAdvertisementInterval = _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 4, 1, 4),
    _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type()
)
agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setStatus("current")


class _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryAdvertisementLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object = MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementLifetime = _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 4, 1, 5),
    _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type()
)
agentSwitchIpRouterDiscoveryAdvertisementLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryAdvertisementLifetime.setStatus("current")


class _AgentSwitchIpRouterDiscoveryPreferenceLevel_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryPreferenceLevel based on Integer32"""
    defaultValue = 0


_AgentSwitchIpRouterDiscoveryPreferenceLevel_Object = MibTableColumn
agentSwitchIpRouterDiscoveryPreferenceLevel = _AgentSwitchIpRouterDiscoveryPreferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 4, 1, 6),
    _AgentSwitchIpRouterDiscoveryPreferenceLevel_Type()
)
agentSwitchIpRouterDiscoveryPreferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryPreferenceLevel.setStatus("current")


class _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):
    """Custom type agentSwitchIpRouterDiscoveryAdvertisementAddress based on IpAddress"""
    defaultHexValue = "E0000001"


_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object = MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementAddress = _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 4, 1, 7),
    _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type()
)
agentSwitchIpRouterDiscoveryAdvertisementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryAdvertisementAddress.setStatus("current")
_AgentSwitchIpVlanTable_Object = MibTable
agentSwitchIpVlanTable = _AgentSwitchIpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    agentSwitchIpVlanTable.setStatus("current")
_AgentSwitchIpVlanEntry_Object = MibTableRow
agentSwitchIpVlanEntry = _AgentSwitchIpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 5, 1)
)
agentSwitchIpVlanEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIpVlanId"),
)
if mibBuilder.loadTexts:
    agentSwitchIpVlanEntry.setStatus("current")


class _AgentSwitchIpVlanId_Type(Integer32):
    """Custom type agentSwitchIpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchIpVlanId_Type.__name__ = "Integer32"
_AgentSwitchIpVlanId_Object = MibTableColumn
agentSwitchIpVlanId = _AgentSwitchIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 5, 1, 1),
    _AgentSwitchIpVlanId_Type()
)
agentSwitchIpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpVlanId.setStatus("current")
_AgentSwitchIpVlanIfIndex_Type = Integer32
_AgentSwitchIpVlanIfIndex_Object = MibTableColumn
agentSwitchIpVlanIfIndex = _AgentSwitchIpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 5, 1, 2),
    _AgentSwitchIpVlanIfIndex_Type()
)
agentSwitchIpVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpVlanIfIndex.setStatus("current")
_AgentSwitchIpVlanRoutingStatus_Type = RowStatus
_AgentSwitchIpVlanRoutingStatus_Object = MibTableColumn
agentSwitchIpVlanRoutingStatus = _AgentSwitchIpVlanRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 5, 1, 3),
    _AgentSwitchIpVlanRoutingStatus_Type()
)
agentSwitchIpVlanRoutingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIpVlanRoutingStatus.setStatus("current")
_AgentSwitchSecondaryAddressTable_Object = MibTable
agentSwitchSecondaryAddressTable = _AgentSwitchSecondaryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    agentSwitchSecondaryAddressTable.setStatus("current")
_AgentSwitchSecondaryAddressEntry_Object = MibTableRow
agentSwitchSecondaryAddressEntry = _AgentSwitchSecondaryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 6, 1)
)
agentSwitchSecondaryAddressEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchSecondaryIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchSecondaryAddressEntry.setStatus("current")
_AgentSwitchSecondaryIpAddress_Type = IpAddress
_AgentSwitchSecondaryIpAddress_Object = MibTableColumn
agentSwitchSecondaryIpAddress = _AgentSwitchSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 6, 1, 1),
    _AgentSwitchSecondaryIpAddress_Type()
)
agentSwitchSecondaryIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSecondaryIpAddress.setStatus("current")
_AgentSwitchSecondaryNetMask_Type = IpAddress
_AgentSwitchSecondaryNetMask_Object = MibTableColumn
agentSwitchSecondaryNetMask = _AgentSwitchSecondaryNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 6, 1, 2),
    _AgentSwitchSecondaryNetMask_Type()
)
agentSwitchSecondaryNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchSecondaryNetMask.setStatus("current")
_AgentSwitchSecondaryStatus_Type = RowStatus
_AgentSwitchSecondaryStatus_Object = MibTableColumn
agentSwitchSecondaryStatus = _AgentSwitchSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 6, 1, 3),
    _AgentSwitchSecondaryStatus_Type()
)
agentSwitchSecondaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchSecondaryStatus.setStatus("current")
_AgentSwitchHelperAddressTable_Object = MibTable
agentSwitchHelperAddressTable = _AgentSwitchHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    agentSwitchHelperAddressTable.setStatus("obsolete")
_AgentSwitchHelperAddressEntry_Object = MibTableRow
agentSwitchHelperAddressEntry = _AgentSwitchHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 7, 1)
)
agentSwitchHelperAddressEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchHelperIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchHelperAddressEntry.setStatus("obsolete")
_AgentSwitchHelperIpAddress_Type = IpAddress
_AgentSwitchHelperIpAddress_Object = MibTableColumn
agentSwitchHelperIpAddress = _AgentSwitchHelperIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 7, 1, 1),
    _AgentSwitchHelperIpAddress_Type()
)
agentSwitchHelperIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchHelperIpAddress.setStatus("obsolete")
_AgentSwitchHelperStatus_Type = RowStatus
_AgentSwitchHelperStatus_Object = MibTableColumn
agentSwitchHelperStatus = _AgentSwitchHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 7, 1, 2),
    _AgentSwitchHelperStatus_Type()
)
agentSwitchHelperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchHelperStatus.setStatus("obsolete")
_AgentSwitchIpIcmpControlGroup_ObjectIdentity = ObjectIdentity
agentSwitchIpIcmpControlGroup = _AgentSwitchIpIcmpControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 8)
)


class _AgentSwitchIpIcmpEchoReplyMode_Type(Integer32):
    """Custom type agentSwitchIpIcmpEchoReplyMode based on Integer32"""
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


_AgentSwitchIpIcmpEchoReplyMode_Type.__name__ = "Integer32"
_AgentSwitchIpIcmpEchoReplyMode_Object = MibScalar
agentSwitchIpIcmpEchoReplyMode = _AgentSwitchIpIcmpEchoReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 8, 1),
    _AgentSwitchIpIcmpEchoReplyMode_Type()
)
agentSwitchIpIcmpEchoReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpIcmpEchoReplyMode.setStatus("current")


class _AgentSwitchIpIcmpRedirectsMode_Type(Integer32):
    """Custom type agentSwitchIpIcmpRedirectsMode based on Integer32"""
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


_AgentSwitchIpIcmpRedirectsMode_Type.__name__ = "Integer32"
_AgentSwitchIpIcmpRedirectsMode_Object = MibScalar
agentSwitchIpIcmpRedirectsMode = _AgentSwitchIpIcmpRedirectsMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 8, 2),
    _AgentSwitchIpIcmpRedirectsMode_Type()
)
agentSwitchIpIcmpRedirectsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpIcmpRedirectsMode.setStatus("current")


class _AgentSwitchIpIcmpRateLimitInterval_Type(Integer32):
    """Custom type agentSwitchIpIcmpRateLimitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchIpIcmpRateLimitInterval_Type.__name__ = "Integer32"
_AgentSwitchIpIcmpRateLimitInterval_Object = MibScalar
agentSwitchIpIcmpRateLimitInterval = _AgentSwitchIpIcmpRateLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 8, 3),
    _AgentSwitchIpIcmpRateLimitInterval_Type()
)
agentSwitchIpIcmpRateLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpIcmpRateLimitInterval.setStatus("current")


class _AgentSwitchIpIcmpRateLimitBurstSize_Type(Integer32):
    """Custom type agentSwitchIpIcmpRateLimitBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AgentSwitchIpIcmpRateLimitBurstSize_Type.__name__ = "Integer32"
_AgentSwitchIpIcmpRateLimitBurstSize_Object = MibScalar
agentSwitchIpIcmpRateLimitBurstSize = _AgentSwitchIpIcmpRateLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 8, 4),
    _AgentSwitchIpIcmpRateLimitBurstSize_Type()
)
agentSwitchIpIcmpRateLimitBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpIcmpRateLimitBurstSize.setStatus("current")
_AgentSwitchIntfIpHelperAddressTable_Object = MibTable
agentSwitchIntfIpHelperAddressTable = _AgentSwitchIntfIpHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperAddressTable.setStatus("current")
_AgentSwitchIntfIpHelperAddressEntry_Object = MibTableRow
agentSwitchIntfIpHelperAddressEntry = _AgentSwitchIntfIpHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 10, 1)
)
agentSwitchIntfIpHelperAddressEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIntfIpHelperUdpPort"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIntfIpHelperIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperAddressEntry.setStatus("current")
_AgentSwitchIntfIpHelperIpAddress_Type = IpAddress
_AgentSwitchIntfIpHelperIpAddress_Object = MibTableColumn
agentSwitchIntfIpHelperIpAddress = _AgentSwitchIntfIpHelperIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 10, 1, 1),
    _AgentSwitchIntfIpHelperIpAddress_Type()
)
agentSwitchIntfIpHelperIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperIpAddress.setStatus("current")


class _AgentSwitchIntfIpHelperUdpPort_Type(Unsigned32):
    """Custom type agentSwitchIntfIpHelperUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentSwitchIntfIpHelperUdpPort_Type.__name__ = "Unsigned32"
_AgentSwitchIntfIpHelperUdpPort_Object = MibTableColumn
agentSwitchIntfIpHelperUdpPort = _AgentSwitchIntfIpHelperUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 10, 1, 2),
    _AgentSwitchIntfIpHelperUdpPort_Type()
)
agentSwitchIntfIpHelperUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperUdpPort.setStatus("current")
_AgentSwitchIntfIpHelperDiscard_Type = TruthValue
_AgentSwitchIntfIpHelperDiscard_Object = MibTableColumn
agentSwitchIntfIpHelperDiscard = _AgentSwitchIntfIpHelperDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 10, 1, 3),
    _AgentSwitchIntfIpHelperDiscard_Type()
)
agentSwitchIntfIpHelperDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperDiscard.setStatus("obsolete")
_AgentSwitchIntfIpHelperHitCount_Type = Unsigned32
_AgentSwitchIntfIpHelperHitCount_Object = MibTableColumn
agentSwitchIntfIpHelperHitCount = _AgentSwitchIntfIpHelperHitCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 10, 1, 4),
    _AgentSwitchIntfIpHelperHitCount_Type()
)
agentSwitchIntfIpHelperHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperHitCount.setStatus("current")
_AgentSwitchIntfIpHelperStatus_Type = RowStatus
_AgentSwitchIntfIpHelperStatus_Object = MibTableColumn
agentSwitchIntfIpHelperStatus = _AgentSwitchIntfIpHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 10, 1, 5),
    _AgentSwitchIntfIpHelperStatus_Type()
)
agentSwitchIntfIpHelperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperStatus.setStatus("current")


class _AgentSwitchClearIpDefaultGateway_Type(Integer32):
    """Custom type agentSwitchClearIpDefaultGateway based on Integer32"""
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


_AgentSwitchClearIpDefaultGateway_Type.__name__ = "Integer32"
_AgentSwitchClearIpDefaultGateway_Object = MibScalar
agentSwitchClearIpDefaultGateway = _AgentSwitchClearIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 2, 11),
    _AgentSwitchClearIpDefaultGateway_Type()
)
agentSwitchClearIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchClearIpDefaultGateway.setStatus("current")
_AgentRouterRipConfigGroup_ObjectIdentity = ObjectIdentity
agentRouterRipConfigGroup = _AgentRouterRipConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3)
)


class _AgentRouterRipAdminState_Type(Integer32):
    """Custom type agentRouterRipAdminState based on Integer32"""
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


_AgentRouterRipAdminState_Type.__name__ = "Integer32"
_AgentRouterRipAdminState_Object = MibScalar
agentRouterRipAdminState = _AgentRouterRipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 1),
    _AgentRouterRipAdminState_Type()
)
agentRouterRipAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipAdminState.setStatus("current")


class _AgentRouterRipSplitHorizonMode_Type(Integer32):
    """Custom type agentRouterRipSplitHorizonMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("poisonReverse", 3),
          ("simple", 2))
    )


_AgentRouterRipSplitHorizonMode_Type.__name__ = "Integer32"
_AgentRouterRipSplitHorizonMode_Object = MibScalar
agentRouterRipSplitHorizonMode = _AgentRouterRipSplitHorizonMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 2),
    _AgentRouterRipSplitHorizonMode_Type()
)
agentRouterRipSplitHorizonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipSplitHorizonMode.setStatus("current")


class _AgentRouterRipAutoSummaryMode_Type(Integer32):
    """Custom type agentRouterRipAutoSummaryMode based on Integer32"""
    defaultValue = 1

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


_AgentRouterRipAutoSummaryMode_Type.__name__ = "Integer32"
_AgentRouterRipAutoSummaryMode_Object = MibScalar
agentRouterRipAutoSummaryMode = _AgentRouterRipAutoSummaryMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 3),
    _AgentRouterRipAutoSummaryMode_Type()
)
agentRouterRipAutoSummaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipAutoSummaryMode.setStatus("current")


class _AgentRouterRipHostRoutesAcceptMode_Type(Integer32):
    """Custom type agentRouterRipHostRoutesAcceptMode based on Integer32"""
    defaultValue = 1

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


_AgentRouterRipHostRoutesAcceptMode_Type.__name__ = "Integer32"
_AgentRouterRipHostRoutesAcceptMode_Object = MibScalar
agentRouterRipHostRoutesAcceptMode = _AgentRouterRipHostRoutesAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 4),
    _AgentRouterRipHostRoutesAcceptMode_Type()
)
agentRouterRipHostRoutesAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipHostRoutesAcceptMode.setStatus("current")


class _AgentRouterRipDefaultMetric_Type(Integer32):
    """Custom type agentRouterRipDefaultMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_AgentRouterRipDefaultMetric_Type.__name__ = "Integer32"
_AgentRouterRipDefaultMetric_Object = MibScalar
agentRouterRipDefaultMetric = _AgentRouterRipDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 5),
    _AgentRouterRipDefaultMetric_Type()
)
agentRouterRipDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipDefaultMetric.setStatus("current")


class _AgentRouterRipDefaultMetricConfigured_Type(TruthValue):
    """Custom type agentRouterRipDefaultMetricConfigured based on TruthValue"""


_AgentRouterRipDefaultMetricConfigured_Object = MibScalar
agentRouterRipDefaultMetricConfigured = _AgentRouterRipDefaultMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 6),
    _AgentRouterRipDefaultMetricConfigured_Type()
)
agentRouterRipDefaultMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipDefaultMetricConfigured.setStatus("current")


class _AgentRouterRipDefaultInfoOriginate_Type(TruthValue):
    """Custom type agentRouterRipDefaultInfoOriginate based on TruthValue"""


_AgentRouterRipDefaultInfoOriginate_Object = MibScalar
agentRouterRipDefaultInfoOriginate = _AgentRouterRipDefaultInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 7),
    _AgentRouterRipDefaultInfoOriginate_Type()
)
agentRouterRipDefaultInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipDefaultInfoOriginate.setStatus("current")
_AgentRipRouteRedistTable_Object = MibTable
agentRipRouteRedistTable = _AgentRipRouteRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    agentRipRouteRedistTable.setStatus("current")
_AgentRipRouteRedistEntry_Object = MibTableRow
agentRipRouteRedistEntry = _AgentRipRouteRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1)
)
agentRipRouteRedistEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentRipRouteRedistSource"),
)
if mibBuilder.loadTexts:
    agentRipRouteRedistEntry.setStatus("current")


class _AgentRipRouteRedistSource_Type(Integer32):
    """Custom type agentRipRouteRedistSource based on Integer32"""
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
        *(("bgp", 4),
          ("connected", 1),
          ("ospf", 3),
          ("static", 2))
    )


_AgentRipRouteRedistSource_Type.__name__ = "Integer32"
_AgentRipRouteRedistSource_Object = MibTableColumn
agentRipRouteRedistSource = _AgentRipRouteRedistSource_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 1),
    _AgentRipRouteRedistSource_Type()
)
agentRipRouteRedistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRipRouteRedistSource.setStatus("current")


class _AgentRipRouteRedistMode_Type(Integer32):
    """Custom type agentRipRouteRedistMode based on Integer32"""
    defaultValue = 2

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


_AgentRipRouteRedistMode_Type.__name__ = "Integer32"
_AgentRipRouteRedistMode_Object = MibTableColumn
agentRipRouteRedistMode = _AgentRipRouteRedistMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 2),
    _AgentRipRouteRedistMode_Type()
)
agentRipRouteRedistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMode.setStatus("current")


class _AgentRipRouteRedistMetric_Type(Integer32):
    """Custom type agentRipRouteRedistMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_AgentRipRouteRedistMetric_Type.__name__ = "Integer32"
_AgentRipRouteRedistMetric_Object = MibTableColumn
agentRipRouteRedistMetric = _AgentRipRouteRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 3),
    _AgentRipRouteRedistMetric_Type()
)
agentRipRouteRedistMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMetric.setStatus("current")


class _AgentRipRouteRedistMetricConfigured_Type(TruthValue):
    """Custom type agentRipRouteRedistMetricConfigured based on TruthValue"""


_AgentRipRouteRedistMetricConfigured_Object = MibTableColumn
agentRipRouteRedistMetricConfigured = _AgentRipRouteRedistMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 4),
    _AgentRipRouteRedistMetricConfigured_Type()
)
agentRipRouteRedistMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMetricConfigured.setStatus("current")


class _AgentRipRouteRedistMatchInternal_Type(Integer32):
    """Custom type agentRipRouteRedistMatchInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("not-applicable", 3),
          ("true", 1))
    )


_AgentRipRouteRedistMatchInternal_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchInternal_Object = MibTableColumn
agentRipRouteRedistMatchInternal = _AgentRipRouteRedistMatchInternal_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 5),
    _AgentRipRouteRedistMatchInternal_Type()
)
agentRipRouteRedistMatchInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchInternal.setStatus("current")


class _AgentRipRouteRedistMatchExternal1_Type(Integer32):
    """Custom type agentRipRouteRedistMatchExternal1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("not-applicable", 3),
          ("true", 1))
    )


_AgentRipRouteRedistMatchExternal1_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchExternal1_Object = MibTableColumn
agentRipRouteRedistMatchExternal1 = _AgentRipRouteRedistMatchExternal1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 6),
    _AgentRipRouteRedistMatchExternal1_Type()
)
agentRipRouteRedistMatchExternal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchExternal1.setStatus("current")


class _AgentRipRouteRedistMatchExternal2_Type(Integer32):
    """Custom type agentRipRouteRedistMatchExternal2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("not-applicable", 3),
          ("true", 1))
    )


_AgentRipRouteRedistMatchExternal2_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchExternal2_Object = MibTableColumn
agentRipRouteRedistMatchExternal2 = _AgentRipRouteRedistMatchExternal2_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 7),
    _AgentRipRouteRedistMatchExternal2_Type()
)
agentRipRouteRedistMatchExternal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchExternal2.setStatus("current")


class _AgentRipRouteRedistMatchNSSAExternal1_Type(Integer32):
    """Custom type agentRipRouteRedistMatchNSSAExternal1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("not-applicable", 3),
          ("true", 1))
    )


_AgentRipRouteRedistMatchNSSAExternal1_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchNSSAExternal1_Object = MibTableColumn
agentRipRouteRedistMatchNSSAExternal1 = _AgentRipRouteRedistMatchNSSAExternal1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 8),
    _AgentRipRouteRedistMatchNSSAExternal1_Type()
)
agentRipRouteRedistMatchNSSAExternal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchNSSAExternal1.setStatus("current")


class _AgentRipRouteRedistMatchNSSAExternal2_Type(Integer32):
    """Custom type agentRipRouteRedistMatchNSSAExternal2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("not-applicable", 3),
          ("true", 1))
    )


_AgentRipRouteRedistMatchNSSAExternal2_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchNSSAExternal2_Object = MibTableColumn
agentRipRouteRedistMatchNSSAExternal2 = _AgentRipRouteRedistMatchNSSAExternal2_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 9),
    _AgentRipRouteRedistMatchNSSAExternal2_Type()
)
agentRipRouteRedistMatchNSSAExternal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchNSSAExternal2.setStatus("current")


class _AgentRipRouteRedistDistList_Type(Unsigned32):
    """Custom type agentRipRouteRedistDistList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_AgentRipRouteRedistDistList_Type.__name__ = "Unsigned32"
_AgentRipRouteRedistDistList_Object = MibTableColumn
agentRipRouteRedistDistList = _AgentRipRouteRedistDistList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 10),
    _AgentRipRouteRedistDistList_Type()
)
agentRipRouteRedistDistList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistDistList.setStatus("current")
_AgentRipRouteRedistDistListConfigured_Type = TruthValue
_AgentRipRouteRedistDistListConfigured_Object = MibTableColumn
agentRipRouteRedistDistListConfigured = _AgentRipRouteRedistDistListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 8, 1, 11),
    _AgentRipRouteRedistDistListConfigured_Type()
)
agentRipRouteRedistDistListConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistDistListConfigured.setStatus("current")
_AgentRip2IfConfTable_Object = MibTable
agentRip2IfConfTable = _AgentRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    agentRip2IfConfTable.setStatus("current")
_AgentRip2IfConfEntry_Object = MibTableRow
agentRip2IfConfEntry = _AgentRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    agentRip2IfConfEntry.setStatus("current")


class _AgentRip2IfConfAuthKeyId_Type(Integer32):
    """Custom type agentRip2IfConfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentRip2IfConfAuthKeyId_Type.__name__ = "Integer32"
_AgentRip2IfConfAuthKeyId_Object = MibTableColumn
agentRip2IfConfAuthKeyId = _AgentRip2IfConfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 9, 1, 1),
    _AgentRip2IfConfAuthKeyId_Type()
)
agentRip2IfConfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRip2IfConfAuthKeyId.setStatus("current")


class _AgentRouterRipRoutePref_Type(Integer32):
    """Custom type agentRouterRipRoutePref based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentRouterRipRoutePref_Type.__name__ = "Integer32"
_AgentRouterRipRoutePref_Object = MibScalar
agentRouterRipRoutePref = _AgentRouterRipRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 3, 10),
    _AgentRouterRipRoutePref_Type()
)
agentRouterRipRoutePref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRouterRipRoutePref.setStatus("current")
_AgentRouterOspfConfigGroup_ObjectIdentity = ObjectIdentity
agentRouterOspfConfigGroup = _AgentRouterOspfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4)
)


class _AgentOspfDefaultMetric_Type(Integer32):
    """Custom type agentOspfDefaultMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777214),
    )


_AgentOspfDefaultMetric_Type.__name__ = "Integer32"
_AgentOspfDefaultMetric_Object = MibScalar
agentOspfDefaultMetric = _AgentOspfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 1),
    _AgentOspfDefaultMetric_Type()
)
agentOspfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultMetric.setStatus("current")


class _AgentOspfDefaultMetricConfigured_Type(TruthValue):
    """Custom type agentOspfDefaultMetricConfigured based on TruthValue"""


_AgentOspfDefaultMetricConfigured_Object = MibScalar
agentOspfDefaultMetricConfigured = _AgentOspfDefaultMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 2),
    _AgentOspfDefaultMetricConfigured_Type()
)
agentOspfDefaultMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultMetricConfigured.setStatus("current")


class _AgentOspfDefaultInfoOriginate_Type(TruthValue):
    """Custom type agentOspfDefaultInfoOriginate based on TruthValue"""


_AgentOspfDefaultInfoOriginate_Object = MibScalar
agentOspfDefaultInfoOriginate = _AgentOspfDefaultInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 3),
    _AgentOspfDefaultInfoOriginate_Type()
)
agentOspfDefaultInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginate.setStatus("current")


class _AgentOspfDefaultInfoOriginateAlways_Type(TruthValue):
    """Custom type agentOspfDefaultInfoOriginateAlways based on TruthValue"""


_AgentOspfDefaultInfoOriginateAlways_Object = MibScalar
agentOspfDefaultInfoOriginateAlways = _AgentOspfDefaultInfoOriginateAlways_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 4),
    _AgentOspfDefaultInfoOriginateAlways_Type()
)
agentOspfDefaultInfoOriginateAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginateAlways.setStatus("current")


class _AgentOspfDefaultInfoOriginateMetric_Type(Integer32):
    """Custom type agentOspfDefaultInfoOriginateMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777214),
    )


_AgentOspfDefaultInfoOriginateMetric_Type.__name__ = "Integer32"
_AgentOspfDefaultInfoOriginateMetric_Object = MibScalar
agentOspfDefaultInfoOriginateMetric = _AgentOspfDefaultInfoOriginateMetric_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 5),
    _AgentOspfDefaultInfoOriginateMetric_Type()
)
agentOspfDefaultInfoOriginateMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginateMetric.setStatus("current")
_AgentOspfDefaultInfoOriginateMetricConfigured_Type = TruthValue
_AgentOspfDefaultInfoOriginateMetricConfigured_Object = MibScalar
agentOspfDefaultInfoOriginateMetricConfigured = _AgentOspfDefaultInfoOriginateMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 6),
    _AgentOspfDefaultInfoOriginateMetricConfigured_Type()
)
agentOspfDefaultInfoOriginateMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginateMetricConfigured.setStatus("current")


class _AgentOspfDefaultInfoOriginateMetricType_Type(Integer32):
    """Custom type agentOspfDefaultInfoOriginateMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalType1", 1),
          ("externalType2", 2))
    )


_AgentOspfDefaultInfoOriginateMetricType_Type.__name__ = "Integer32"
_AgentOspfDefaultInfoOriginateMetricType_Object = MibScalar
agentOspfDefaultInfoOriginateMetricType = _AgentOspfDefaultInfoOriginateMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 7),
    _AgentOspfDefaultInfoOriginateMetricType_Type()
)
agentOspfDefaultInfoOriginateMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginateMetricType.setStatus("current")
_AgentOspfRouteRedistTable_Object = MibTable
agentOspfRouteRedistTable = _AgentOspfRouteRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8)
)
if mibBuilder.loadTexts:
    agentOspfRouteRedistTable.setStatus("current")
_AgentOspfRouteRedistEntry_Object = MibTableRow
agentOspfRouteRedistEntry = _AgentOspfRouteRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1)
)
agentOspfRouteRedistEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfRouteRedistSource"),
)
if mibBuilder.loadTexts:
    agentOspfRouteRedistEntry.setStatus("current")


class _AgentOspfRouteRedistSource_Type(Integer32):
    """Custom type agentOspfRouteRedistSource based on Integer32"""
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
        *(("bgp", 4),
          ("connected", 1),
          ("rip", 3),
          ("static", 2))
    )


_AgentOspfRouteRedistSource_Type.__name__ = "Integer32"
_AgentOspfRouteRedistSource_Object = MibTableColumn
agentOspfRouteRedistSource = _AgentOspfRouteRedistSource_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1, 1),
    _AgentOspfRouteRedistSource_Type()
)
agentOspfRouteRedistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfRouteRedistSource.setStatus("current")


class _AgentOspfRouteRedistMode_Type(Integer32):
    """Custom type agentOspfRouteRedistMode based on Integer32"""
    defaultValue = 2

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


_AgentOspfRouteRedistMode_Type.__name__ = "Integer32"
_AgentOspfRouteRedistMode_Object = MibTableColumn
agentOspfRouteRedistMode = _AgentOspfRouteRedistMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1, 2),
    _AgentOspfRouteRedistMode_Type()
)
agentOspfRouteRedistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistMode.setStatus("current")


class _AgentOspfRouteRedistMetric_Type(Integer32):
    """Custom type agentOspfRouteRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_AgentOspfRouteRedistMetric_Type.__name__ = "Integer32"
_AgentOspfRouteRedistMetric_Object = MibTableColumn
agentOspfRouteRedistMetric = _AgentOspfRouteRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1, 3),
    _AgentOspfRouteRedistMetric_Type()
)
agentOspfRouteRedistMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistMetric.setStatus("current")
_AgentOspfRouteRedistMetricConfigured_Type = TruthValue
_AgentOspfRouteRedistMetricConfigured_Object = MibTableColumn
agentOspfRouteRedistMetricConfigured = _AgentOspfRouteRedistMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1, 4),
    _AgentOspfRouteRedistMetricConfigured_Type()
)
agentOspfRouteRedistMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistMetricConfigured.setStatus("current")


class _AgentOspfRouteRedistMetricType_Type(Integer32):
    """Custom type agentOspfRouteRedistMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalType1", 1),
          ("externalType2", 2))
    )


_AgentOspfRouteRedistMetricType_Type.__name__ = "Integer32"
_AgentOspfRouteRedistMetricType_Object = MibTableColumn
agentOspfRouteRedistMetricType = _AgentOspfRouteRedistMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1, 5),
    _AgentOspfRouteRedistMetricType_Type()
)
agentOspfRouteRedistMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistMetricType.setStatus("current")
_AgentOspfRouteRedistTag_Type = Unsigned32
_AgentOspfRouteRedistTag_Object = MibTableColumn
agentOspfRouteRedistTag = _AgentOspfRouteRedistTag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1, 6),
    _AgentOspfRouteRedistTag_Type()
)
agentOspfRouteRedistTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistTag.setStatus("current")


class _AgentOspfRouteRedistSubnets_Type(TruthValue):
    """Custom type agentOspfRouteRedistSubnets based on TruthValue"""


_AgentOspfRouteRedistSubnets_Object = MibTableColumn
agentOspfRouteRedistSubnets = _AgentOspfRouteRedistSubnets_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1, 7),
    _AgentOspfRouteRedistSubnets_Type()
)
agentOspfRouteRedistSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistSubnets.setStatus("current")


class _AgentOspfRouteRedistDistList_Type(Unsigned32):
    """Custom type agentOspfRouteRedistDistList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_AgentOspfRouteRedistDistList_Type.__name__ = "Unsigned32"
_AgentOspfRouteRedistDistList_Object = MibTableColumn
agentOspfRouteRedistDistList = _AgentOspfRouteRedistDistList_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1, 8),
    _AgentOspfRouteRedistDistList_Type()
)
agentOspfRouteRedistDistList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistDistList.setStatus("current")
_AgentOspfRouteRedistDistListConfigured_Type = TruthValue
_AgentOspfRouteRedistDistListConfigured_Object = MibTableColumn
agentOspfRouteRedistDistListConfigured = _AgentOspfRouteRedistDistListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 8, 1, 9),
    _AgentOspfRouteRedistDistListConfigured_Type()
)
agentOspfRouteRedistDistListConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistDistListConfigured.setStatus("current")
_AgentOspfIfTable_Object = MibTable
agentOspfIfTable = _AgentOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 9)
)
if mibBuilder.loadTexts:
    agentOspfIfTable.setStatus("current")
_AgentOspfIfEntry_Object = MibTableRow
agentOspfIfEntry = _AgentOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 9, 1)
)
if mibBuilder.loadTexts:
    agentOspfIfEntry.setStatus("current")


class _AgentOspfIfAuthKeyId_Type(Integer32):
    """Custom type agentOspfIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOspfIfAuthKeyId_Type.__name__ = "Integer32"
_AgentOspfIfAuthKeyId_Object = MibTableColumn
agentOspfIfAuthKeyId = _AgentOspfIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 9, 1, 1),
    _AgentOspfIfAuthKeyId_Type()
)
agentOspfIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOspfIfAuthKeyId.setStatus("current")


class _AgentOspfIfIpMtuIgnoreFlag_Type(Integer32):
    """Custom type agentOspfIfIpMtuIgnoreFlag based on Integer32"""
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


_AgentOspfIfIpMtuIgnoreFlag_Type.__name__ = "Integer32"
_AgentOspfIfIpMtuIgnoreFlag_Object = MibTableColumn
agentOspfIfIpMtuIgnoreFlag = _AgentOspfIfIpMtuIgnoreFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 9, 1, 2),
    _AgentOspfIfIpMtuIgnoreFlag_Type()
)
agentOspfIfIpMtuIgnoreFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfIfIpMtuIgnoreFlag.setStatus("current")


class _AgentOspfIfPassiveMode_Type(TruthValue):
    """Custom type agentOspfIfPassiveMode based on TruthValue"""


_AgentOspfIfPassiveMode_Object = MibTableColumn
agentOspfIfPassiveMode = _AgentOspfIfPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 9, 1, 3),
    _AgentOspfIfPassiveMode_Type()
)
agentOspfIfPassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfIfPassiveMode.setStatus("current")


class _AgentOspfIfAdvertiseSecondaries_Type(Integer32):
    """Custom type agentOspfIfAdvertiseSecondaries based on Integer32"""
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


_AgentOspfIfAdvertiseSecondaries_Type.__name__ = "Integer32"
_AgentOspfIfAdvertiseSecondaries_Object = MibTableColumn
agentOspfIfAdvertiseSecondaries = _AgentOspfIfAdvertiseSecondaries_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 9, 1, 4),
    _AgentOspfIfAdvertiseSecondaries_Type()
)
agentOspfIfAdvertiseSecondaries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfIfAdvertiseSecondaries.setStatus("current")
_AgentOspfVirtIfTable_Object = MibTable
agentOspfVirtIfTable = _AgentOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 10)
)
if mibBuilder.loadTexts:
    agentOspfVirtIfTable.setStatus("current")
_AgentOspfVirtIfEntry_Object = MibTableRow
agentOspfVirtIfEntry = _AgentOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 10, 1)
)
if mibBuilder.loadTexts:
    agentOspfVirtIfEntry.setStatus("current")


class _AgentOspfVirtIfAuthKeyId_Type(Integer32):
    """Custom type agentOspfVirtIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOspfVirtIfAuthKeyId_Type.__name__ = "Integer32"
_AgentOspfVirtIfAuthKeyId_Object = MibTableColumn
agentOspfVirtIfAuthKeyId = _AgentOspfVirtIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 10, 1, 1),
    _AgentOspfVirtIfAuthKeyId_Type()
)
agentOspfVirtIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOspfVirtIfAuthKeyId.setStatus("current")


class _AgentRouterOspfRFC1583CompatibilityMode_Type(Integer32):
    """Custom type agentRouterOspfRFC1583CompatibilityMode based on Integer32"""
    defaultValue = 1

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


_AgentRouterOspfRFC1583CompatibilityMode_Type.__name__ = "Integer32"
_AgentRouterOspfRFC1583CompatibilityMode_Object = MibScalar
agentRouterOspfRFC1583CompatibilityMode = _AgentRouterOspfRFC1583CompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 11),
    _AgentRouterOspfRFC1583CompatibilityMode_Type()
)
agentRouterOspfRFC1583CompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterOspfRFC1583CompatibilityMode.setStatus("current")


class _AgentOspfSpfDelayTime_Type(SpfTimerRange):
    """Custom type agentOspfSpfDelayTime based on SpfTimerRange"""
    defaultValue = 5


_AgentOspfSpfDelayTime_Object = MibScalar
agentOspfSpfDelayTime = _AgentOspfSpfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 12),
    _AgentOspfSpfDelayTime_Type()
)
agentOspfSpfDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfSpfDelayTime.setStatus("current")


class _AgentOspfSpfHoldTime_Type(SpfTimerRange):
    """Custom type agentOspfSpfHoldTime based on SpfTimerRange"""
    defaultValue = 10


_AgentOspfSpfHoldTime_Object = MibScalar
agentOspfSpfHoldTime = _AgentOspfSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 13),
    _AgentOspfSpfHoldTime_Type()
)
agentOspfSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfSpfHoldTime.setStatus("current")


class _AgentOspfAutoCostRefBw_Type(AutoCostRefBw):
    """Custom type agentOspfAutoCostRefBw based on AutoCostRefBw"""
    defaultValue = 100


_AgentOspfAutoCostRefBw_Object = MibScalar
agentOspfAutoCostRefBw = _AgentOspfAutoCostRefBw_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 14),
    _AgentOspfAutoCostRefBw_Type()
)
agentOspfAutoCostRefBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfAutoCostRefBw.setStatus("current")
_AgentOspfOpaqueLsaSupport_Type = TruthValue
_AgentOspfOpaqueLsaSupport_Object = MibScalar
agentOspfOpaqueLsaSupport = _AgentOspfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 15),
    _AgentOspfOpaqueLsaSupport_Type()
)
agentOspfOpaqueLsaSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfOpaqueLsaSupport.setStatus("current")
_AgentOspfAreaOpaqueLsdbTable_Object = MibTable
agentOspfAreaOpaqueLsdbTable = _AgentOspfAreaOpaqueLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16)
)
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbTable.setStatus("current")
_AgentOspfAreaOpaqueLsdbEntry_Object = MibTableRow
agentOspfAreaOpaqueLsdbEntry = _AgentOspfAreaOpaqueLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16, 1)
)
agentOspfAreaOpaqueLsdbEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfAreaOpaqueLsdbAreaId"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfAreaOpaqueLsdbType"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfAreaOpaqueLsdbLsid"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfAreaOpaqueLsdbRouterId"),
)
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbEntry.setStatus("current")
_AgentOspfAreaOpaqueLsdbAreaId_Type = IpAddress
_AgentOspfAreaOpaqueLsdbAreaId_Object = MibTableColumn
agentOspfAreaOpaqueLsdbAreaId = _AgentOspfAreaOpaqueLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16, 1, 1),
    _AgentOspfAreaOpaqueLsdbAreaId_Type()
)
agentOspfAreaOpaqueLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbAreaId.setStatus("current")


class _AgentOspfAreaOpaqueLsdbType_Type(Integer32):
    """Custom type agentOspfAreaOpaqueLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("areaOpaqueLink", 10)
    )


_AgentOspfAreaOpaqueLsdbType_Type.__name__ = "Integer32"
_AgentOspfAreaOpaqueLsdbType_Object = MibTableColumn
agentOspfAreaOpaqueLsdbType = _AgentOspfAreaOpaqueLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16, 1, 2),
    _AgentOspfAreaOpaqueLsdbType_Type()
)
agentOspfAreaOpaqueLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbType.setStatus("current")
_AgentOspfAreaOpaqueLsdbLsid_Type = IpAddress
_AgentOspfAreaOpaqueLsdbLsid_Object = MibTableColumn
agentOspfAreaOpaqueLsdbLsid = _AgentOspfAreaOpaqueLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16, 1, 3),
    _AgentOspfAreaOpaqueLsdbLsid_Type()
)
agentOspfAreaOpaqueLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbLsid.setStatus("current")
_AgentOspfAreaOpaqueLsdbRouterId_Type = IpAddress
_AgentOspfAreaOpaqueLsdbRouterId_Object = MibTableColumn
agentOspfAreaOpaqueLsdbRouterId = _AgentOspfAreaOpaqueLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16, 1, 4),
    _AgentOspfAreaOpaqueLsdbRouterId_Type()
)
agentOspfAreaOpaqueLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbRouterId.setStatus("current")
_AgentOspfAreaOpaqueLsdbSequence_Type = Integer32
_AgentOspfAreaOpaqueLsdbSequence_Object = MibTableColumn
agentOspfAreaOpaqueLsdbSequence = _AgentOspfAreaOpaqueLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16, 1, 5),
    _AgentOspfAreaOpaqueLsdbSequence_Type()
)
agentOspfAreaOpaqueLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbSequence.setStatus("current")
_AgentOspfAreaOpaqueLsdbAge_Type = Integer32
_AgentOspfAreaOpaqueLsdbAge_Object = MibTableColumn
agentOspfAreaOpaqueLsdbAge = _AgentOspfAreaOpaqueLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16, 1, 6),
    _AgentOspfAreaOpaqueLsdbAge_Type()
)
agentOspfAreaOpaqueLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbAge.setUnits("seconds")
_AgentOspfAreaOpaqueLsdbChecksum_Type = Integer32
_AgentOspfAreaOpaqueLsdbChecksum_Object = MibTableColumn
agentOspfAreaOpaqueLsdbChecksum = _AgentOspfAreaOpaqueLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16, 1, 7),
    _AgentOspfAreaOpaqueLsdbChecksum_Type()
)
agentOspfAreaOpaqueLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbChecksum.setStatus("current")


class _AgentOspfAreaOpaqueLsdbAdvertisement_Type(OctetString):
    """Custom type agentOspfAreaOpaqueLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_AgentOspfAreaOpaqueLsdbAdvertisement_Type.__name__ = "OctetString"
_AgentOspfAreaOpaqueLsdbAdvertisement_Object = MibTableColumn
agentOspfAreaOpaqueLsdbAdvertisement = _AgentOspfAreaOpaqueLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 16, 1, 8),
    _AgentOspfAreaOpaqueLsdbAdvertisement_Type()
)
agentOspfAreaOpaqueLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAreaOpaqueLsdbAdvertisement.setStatus("current")
_AgentOspfLocalLsdbTable_Object = MibTable
agentOspfLocalLsdbTable = _AgentOspfLocalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17)
)
if mibBuilder.loadTexts:
    agentOspfLocalLsdbTable.setStatus("current")
_AgentOspfLocalLsdbEntry_Object = MibTableRow
agentOspfLocalLsdbEntry = _AgentOspfLocalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1)
)
agentOspfLocalLsdbEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfLocalLsdbIpAddress"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfLocalLsdbAddressLessIf"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfLocalLsdbType"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfLocalLsdbLsid"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    agentOspfLocalLsdbEntry.setStatus("current")
_AgentOspfLocalLsdbIpAddress_Type = IpAddress
_AgentOspfLocalLsdbIpAddress_Object = MibTableColumn
agentOspfLocalLsdbIpAddress = _AgentOspfLocalLsdbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1, 1),
    _AgentOspfLocalLsdbIpAddress_Type()
)
agentOspfLocalLsdbIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbIpAddress.setStatus("current")
_AgentOspfLocalLsdbAddressLessIf_Type = InterfaceIndexOrZero
_AgentOspfLocalLsdbAddressLessIf_Object = MibTableColumn
agentOspfLocalLsdbAddressLessIf = _AgentOspfLocalLsdbAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1, 2),
    _AgentOspfLocalLsdbAddressLessIf_Type()
)
agentOspfLocalLsdbAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbAddressLessIf.setStatus("current")


class _AgentOspfLocalLsdbType_Type(Integer32):
    """Custom type agentOspfLocalLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("localOpaqueLink", 9)
    )


_AgentOspfLocalLsdbType_Type.__name__ = "Integer32"
_AgentOspfLocalLsdbType_Object = MibTableColumn
agentOspfLocalLsdbType = _AgentOspfLocalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1, 3),
    _AgentOspfLocalLsdbType_Type()
)
agentOspfLocalLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbType.setStatus("current")
_AgentOspfLocalLsdbLsid_Type = IpAddress
_AgentOspfLocalLsdbLsid_Object = MibTableColumn
agentOspfLocalLsdbLsid = _AgentOspfLocalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1, 4),
    _AgentOspfLocalLsdbLsid_Type()
)
agentOspfLocalLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbLsid.setStatus("current")
_AgentOspfLocalLsdbRouterId_Type = RouterID
_AgentOspfLocalLsdbRouterId_Object = MibTableColumn
agentOspfLocalLsdbRouterId = _AgentOspfLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1, 5),
    _AgentOspfLocalLsdbRouterId_Type()
)
agentOspfLocalLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbRouterId.setStatus("current")
_AgentOspfLocalLsdbSequence_Type = Integer32
_AgentOspfLocalLsdbSequence_Object = MibTableColumn
agentOspfLocalLsdbSequence = _AgentOspfLocalLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1, 6),
    _AgentOspfLocalLsdbSequence_Type()
)
agentOspfLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbSequence.setStatus("current")
_AgentOspfLocalLsdbAge_Type = Integer32
_AgentOspfLocalLsdbAge_Object = MibTableColumn
agentOspfLocalLsdbAge = _AgentOspfLocalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1, 7),
    _AgentOspfLocalLsdbAge_Type()
)
agentOspfLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbAge.setUnits("seconds")
_AgentOspfLocalLsdbChecksum_Type = Integer32
_AgentOspfLocalLsdbChecksum_Object = MibTableColumn
agentOspfLocalLsdbChecksum = _AgentOspfLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1, 8),
    _AgentOspfLocalLsdbChecksum_Type()
)
agentOspfLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbChecksum.setStatus("current")


class _AgentOspfLocalLsdbAdvertisement_Type(OctetString):
    """Custom type agentOspfLocalLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_AgentOspfLocalLsdbAdvertisement_Type.__name__ = "OctetString"
_AgentOspfLocalLsdbAdvertisement_Object = MibTableColumn
agentOspfLocalLsdbAdvertisement = _AgentOspfLocalLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 17, 1, 9),
    _AgentOspfLocalLsdbAdvertisement_Type()
)
agentOspfLocalLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLocalLsdbAdvertisement.setStatus("current")
_AgentOspfAsLsdbTable_Object = MibTable
agentOspfAsLsdbTable = _AgentOspfAsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 18)
)
if mibBuilder.loadTexts:
    agentOspfAsLsdbTable.setStatus("current")
_AgentOspfAsLsdbEntry_Object = MibTableRow
agentOspfAsLsdbEntry = _AgentOspfAsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 18, 1)
)
agentOspfAsLsdbEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfAsLsdbType"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfAsLsdbLsid"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfAsLsdbRouterId"),
)
if mibBuilder.loadTexts:
    agentOspfAsLsdbEntry.setStatus("current")


class _AgentOspfAsLsdbType_Type(Integer32):
    """Custom type agentOspfAsLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            11
        )
    )
    namedValues = NamedValues(
        ("asOpaqueLink", 11)
    )


_AgentOspfAsLsdbType_Type.__name__ = "Integer32"
_AgentOspfAsLsdbType_Object = MibTableColumn
agentOspfAsLsdbType = _AgentOspfAsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 18, 1, 1),
    _AgentOspfAsLsdbType_Type()
)
agentOspfAsLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAsLsdbType.setStatus("current")
_AgentOspfAsLsdbLsid_Type = IpAddress
_AgentOspfAsLsdbLsid_Object = MibTableColumn
agentOspfAsLsdbLsid = _AgentOspfAsLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 18, 1, 2),
    _AgentOspfAsLsdbLsid_Type()
)
agentOspfAsLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAsLsdbLsid.setStatus("current")
_AgentOspfAsLsdbRouterId_Type = RouterID
_AgentOspfAsLsdbRouterId_Object = MibTableColumn
agentOspfAsLsdbRouterId = _AgentOspfAsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 18, 1, 3),
    _AgentOspfAsLsdbRouterId_Type()
)
agentOspfAsLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAsLsdbRouterId.setStatus("current")
_AgentOspfAsLsdbSequence_Type = Integer32
_AgentOspfAsLsdbSequence_Object = MibTableColumn
agentOspfAsLsdbSequence = _AgentOspfAsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 18, 1, 4),
    _AgentOspfAsLsdbSequence_Type()
)
agentOspfAsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAsLsdbSequence.setStatus("current")
_AgentOspfAsLsdbAge_Type = Integer32
_AgentOspfAsLsdbAge_Object = MibTableColumn
agentOspfAsLsdbAge = _AgentOspfAsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 18, 1, 5),
    _AgentOspfAsLsdbAge_Type()
)
agentOspfAsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAsLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    agentOspfAsLsdbAge.setUnits("seconds")
_AgentOspfAsLsdbChecksum_Type = Integer32
_AgentOspfAsLsdbChecksum_Object = MibTableColumn
agentOspfAsLsdbChecksum = _AgentOspfAsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 18, 1, 6),
    _AgentOspfAsLsdbChecksum_Type()
)
agentOspfAsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAsLsdbChecksum.setStatus("current")


class _AgentOspfAsLsdbAdvertisement_Type(OctetString):
    """Custom type agentOspfAsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_AgentOspfAsLsdbAdvertisement_Type.__name__ = "OctetString"
_AgentOspfAsLsdbAdvertisement_Object = MibTableColumn
agentOspfAsLsdbAdvertisement = _AgentOspfAsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 18, 1, 7),
    _AgentOspfAsLsdbAdvertisement_Type()
)
agentOspfAsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfAsLsdbAdvertisement.setStatus("current")


class _AgentOspfDefaultPassiveMode_Type(TruthValue):
    """Custom type agentOspfDefaultPassiveMode based on TruthValue"""


_AgentOspfDefaultPassiveMode_Object = MibScalar
agentOspfDefaultPassiveMode = _AgentOspfDefaultPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 19),
    _AgentOspfDefaultPassiveMode_Type()
)
agentOspfDefaultPassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultPassiveMode.setStatus("current")


class _AgentOspfRoutePrefIntraArea_Type(Integer32):
    """Custom type agentOspfRoutePrefIntraArea based on Integer32"""
    defaultValue = 110

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentOspfRoutePrefIntraArea_Type.__name__ = "Integer32"
_AgentOspfRoutePrefIntraArea_Object = MibScalar
agentOspfRoutePrefIntraArea = _AgentOspfRoutePrefIntraArea_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 20),
    _AgentOspfRoutePrefIntraArea_Type()
)
agentOspfRoutePrefIntraArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRoutePrefIntraArea.setStatus("current")


class _AgentOspfRoutePrefInterArea_Type(Integer32):
    """Custom type agentOspfRoutePrefInterArea based on Integer32"""
    defaultValue = 110

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentOspfRoutePrefInterArea_Type.__name__ = "Integer32"
_AgentOspfRoutePrefInterArea_Object = MibScalar
agentOspfRoutePrefInterArea = _AgentOspfRoutePrefInterArea_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 21),
    _AgentOspfRoutePrefInterArea_Type()
)
agentOspfRoutePrefInterArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRoutePrefInterArea.setStatus("current")


class _AgentOspfRoutePrefExternal_Type(Integer32):
    """Custom type agentOspfRoutePrefExternal based on Integer32"""
    defaultValue = 110

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentOspfRoutePrefExternal_Type.__name__ = "Integer32"
_AgentOspfRoutePrefExternal_Object = MibScalar
agentOspfRoutePrefExternal = _AgentOspfRoutePrefExternal_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 4, 22),
    _AgentOspfRoutePrefExternal_Type()
)
agentOspfRoutePrefExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRoutePrefExternal.setStatus("current")
_AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity = ObjectIdentity
agentSnmpTrapFlagsConfigGroupLayer3 = _AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 5)
)


class _AgentSnmpVRRPNewMasterTrapFlag_Type(Integer32):
    """Custom type agentSnmpVRRPNewMasterTrapFlag based on Integer32"""
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


_AgentSnmpVRRPNewMasterTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpVRRPNewMasterTrapFlag_Object = MibScalar
agentSnmpVRRPNewMasterTrapFlag = _AgentSnmpVRRPNewMasterTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 5, 1),
    _AgentSnmpVRRPNewMasterTrapFlag_Type()
)
agentSnmpVRRPNewMasterTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpVRRPNewMasterTrapFlag.setStatus("current")


class _AgentSnmpVRRPAuthFailureTrapFlag_Type(Integer32):
    """Custom type agentSnmpVRRPAuthFailureTrapFlag based on Integer32"""
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


_AgentSnmpVRRPAuthFailureTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpVRRPAuthFailureTrapFlag_Object = MibScalar
agentSnmpVRRPAuthFailureTrapFlag = _AgentSnmpVRRPAuthFailureTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 5, 2),
    _AgentSnmpVRRPAuthFailureTrapFlag_Type()
)
agentSnmpVRRPAuthFailureTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpVRRPAuthFailureTrapFlag.setStatus("current")
_AgentBootpDhcpRelayGroup_ObjectIdentity = ObjectIdentity
agentBootpDhcpRelayGroup = _AgentBootpDhcpRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 6)
)


class _AgentBootpDhcpRelayMaxHopCount_Type(Integer32):
    """Custom type agentBootpDhcpRelayMaxHopCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AgentBootpDhcpRelayMaxHopCount_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayMaxHopCount_Object = MibScalar
agentBootpDhcpRelayMaxHopCount = _AgentBootpDhcpRelayMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 6, 1),
    _AgentBootpDhcpRelayMaxHopCount_Type()
)
agentBootpDhcpRelayMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayMaxHopCount.setStatus("current")
_AgentBootpDhcpRelayForwardingIp_Type = IpAddress
_AgentBootpDhcpRelayForwardingIp_Object = MibScalar
agentBootpDhcpRelayForwardingIp = _AgentBootpDhcpRelayForwardingIp_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 6, 2),
    _AgentBootpDhcpRelayForwardingIp_Type()
)
agentBootpDhcpRelayForwardingIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayForwardingIp.setStatus("obsolete")


class _AgentBootpDhcpRelayForwardMode_Type(Integer32):
    """Custom type agentBootpDhcpRelayForwardMode based on Integer32"""
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


_AgentBootpDhcpRelayForwardMode_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayForwardMode_Object = MibScalar
agentBootpDhcpRelayForwardMode = _AgentBootpDhcpRelayForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 6, 3),
    _AgentBootpDhcpRelayForwardMode_Type()
)
agentBootpDhcpRelayForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayForwardMode.setStatus("obsolete")


class _AgentBootpDhcpRelayMinWaitTime_Type(Integer32):
    """Custom type agentBootpDhcpRelayMinWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentBootpDhcpRelayMinWaitTime_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayMinWaitTime_Object = MibScalar
agentBootpDhcpRelayMinWaitTime = _AgentBootpDhcpRelayMinWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 6, 4),
    _AgentBootpDhcpRelayMinWaitTime_Type()
)
agentBootpDhcpRelayMinWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayMinWaitTime.setStatus("current")


class _AgentBootpDhcpRelayCircuitIdOptionMode_Type(Integer32):
    """Custom type agentBootpDhcpRelayCircuitIdOptionMode based on Integer32"""
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


_AgentBootpDhcpRelayCircuitIdOptionMode_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayCircuitIdOptionMode_Object = MibScalar
agentBootpDhcpRelayCircuitIdOptionMode = _AgentBootpDhcpRelayCircuitIdOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 6, 5),
    _AgentBootpDhcpRelayCircuitIdOptionMode_Type()
)
agentBootpDhcpRelayCircuitIdOptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayCircuitIdOptionMode.setStatus("current")
_AgentBootpDhcpRelayNumOfRequestsReceived_Type = Integer32
_AgentBootpDhcpRelayNumOfRequestsReceived_Object = MibScalar
agentBootpDhcpRelayNumOfRequestsReceived = _AgentBootpDhcpRelayNumOfRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 6, 6),
    _AgentBootpDhcpRelayNumOfRequestsReceived_Type()
)
agentBootpDhcpRelayNumOfRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayNumOfRequestsReceived.setStatus("obsolete")
_AgentBootpDhcpRelayNumOfRequestsForwarded_Type = Integer32
_AgentBootpDhcpRelayNumOfRequestsForwarded_Object = MibScalar
agentBootpDhcpRelayNumOfRequestsForwarded = _AgentBootpDhcpRelayNumOfRequestsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 6, 7),
    _AgentBootpDhcpRelayNumOfRequestsForwarded_Type()
)
agentBootpDhcpRelayNumOfRequestsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayNumOfRequestsForwarded.setStatus("obsolete")
_AgentBootpDhcpRelayNumOfDiscards_Type = Integer32
_AgentBootpDhcpRelayNumOfDiscards_Object = MibScalar
agentBootpDhcpRelayNumOfDiscards = _AgentBootpDhcpRelayNumOfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 6, 8),
    _AgentBootpDhcpRelayNumOfDiscards_Type()
)
agentBootpDhcpRelayNumOfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayNumOfDiscards.setStatus("obsolete")
_AgentECMPGroup_ObjectIdentity = ObjectIdentity
agentECMPGroup = _AgentECMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 7)
)


class _AgentECMPOspfMaxPaths_Type(Integer32):
    """Custom type agentECMPOspfMaxPaths based on Integer32"""
    defaultValue = 4


_AgentECMPOspfMaxPaths_Object = MibScalar
agentECMPOspfMaxPaths = _AgentECMPOspfMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 7, 1),
    _AgentECMPOspfMaxPaths_Type()
)
agentECMPOspfMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentECMPOspfMaxPaths.setStatus("current")
_AgentRouterVrrpConfigGroup_ObjectIdentity = ObjectIdentity
agentRouterVrrpConfigGroup = _AgentRouterVrrpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 8)
)


class _AgentRouterVrrpAdminState_Type(Integer32):
    """Custom type agentRouterVrrpAdminState based on Integer32"""
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


_AgentRouterVrrpAdminState_Type.__name__ = "Integer32"
_AgentRouterVrrpAdminState_Object = MibScalar
agentRouterVrrpAdminState = _AgentRouterVrrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 8, 1),
    _AgentRouterVrrpAdminState_Type()
)
agentRouterVrrpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterVrrpAdminState.setStatus("current")
_AgentRouterVrrpConfiguredTable_Object = MibTable
agentRouterVrrpConfiguredTable = _AgentRouterVrrpConfiguredTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    agentRouterVrrpConfiguredTable.setStatus("current")
_AgentRouterVrrpConfiguredEntry_Object = MibTableRow
agentRouterVrrpConfiguredEntry = _AgentRouterVrrpConfiguredEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 8, 2, 1)
)
agentRouterVrrpConfiguredEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    agentRouterVrrpConfiguredEntry.setStatus("current")


class _AgentRouterVrrpConfiguredPriority_Type(Integer32):
    """Custom type agentRouterVrrpConfiguredPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AgentRouterVrrpConfiguredPriority_Type.__name__ = "Integer32"
_AgentRouterVrrpConfiguredPriority_Object = MibTableColumn
agentRouterVrrpConfiguredPriority = _AgentRouterVrrpConfiguredPriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 8, 2, 1, 1),
    _AgentRouterVrrpConfiguredPriority_Type()
)
agentRouterVrrpConfiguredPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouterVrrpConfiguredPriority.setStatus("current")
_AgentVrrpOperations_ObjectIdentity = ObjectIdentity
agentVrrpOperations = _AgentVrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 9)
)
_AgentRouterVrrpOperTable_Object = MibTable
agentRouterVrrpOperTable = _AgentRouterVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    agentRouterVrrpOperTable.setStatus("obsolete")
_AgentRouterVrrpOperEntry_Object = MibTableRow
agentRouterVrrpOperEntry = _AgentRouterVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 9, 1, 1)
)
agentRouterVrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    agentRouterVrrpOperEntry.setStatus("obsolete")


class _AgentRouterVrrpOperPriority_Type(Integer32):
    """Custom type agentRouterVrrpOperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentRouterVrrpOperPriority_Type.__name__ = "Integer32"
_AgentRouterVrrpOperPriority_Object = MibTableColumn
agentRouterVrrpOperPriority = _AgentRouterVrrpOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 9, 1, 1, 1),
    _AgentRouterVrrpOperPriority_Type()
)
agentRouterVrrpOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouterVrrpOperPriority.setStatus("obsolete")
_AgentRouterVrrpTrackGroup_ObjectIdentity = ObjectIdentity
agentRouterVrrpTrackGroup = _AgentRouterVrrpTrackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10)
)
_AgentRouterVrrpTrackIntfTable_Object = MibTable
agentRouterVrrpTrackIntfTable = _AgentRouterVrrpTrackIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    agentRouterVrrpTrackIntfTable.setStatus("current")
_AgentRouterVrrpTrackIntfEntry_Object = MibTableRow
agentRouterVrrpTrackIntfEntry = _AgentRouterVrrpTrackIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 1, 1)
)
agentRouterVrrpTrackIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentRouterVrrpTrackIntf"),
)
if mibBuilder.loadTexts:
    agentRouterVrrpTrackIntfEntry.setStatus("current")
_AgentRouterVrrpTrackIntf_Type = InterfaceIndex
_AgentRouterVrrpTrackIntf_Object = MibTableColumn
agentRouterVrrpTrackIntf = _AgentRouterVrrpTrackIntf_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 1, 1, 1),
    _AgentRouterVrrpTrackIntf_Type()
)
agentRouterVrrpTrackIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRouterVrrpTrackIntf.setStatus("current")


class _AgentRouterVrrpTrackIfPrioDec_Type(Integer32):
    """Custom type agentRouterVrrpTrackIfPrioDec based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AgentRouterVrrpTrackIfPrioDec_Type.__name__ = "Integer32"
_AgentRouterVrrpTrackIfPrioDec_Object = MibTableColumn
agentRouterVrrpTrackIfPrioDec = _AgentRouterVrrpTrackIfPrioDec_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 1, 1, 2),
    _AgentRouterVrrpTrackIfPrioDec_Type()
)
agentRouterVrrpTrackIfPrioDec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRouterVrrpTrackIfPrioDec.setStatus("current")
_AgentRouterVrrpTrackIfState_Type = TruthValue
_AgentRouterVrrpTrackIfState_Object = MibTableColumn
agentRouterVrrpTrackIfState = _AgentRouterVrrpTrackIfState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 1, 1, 3),
    _AgentRouterVrrpTrackIfState_Type()
)
agentRouterVrrpTrackIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouterVrrpTrackIfState.setStatus("current")
_AgentRouterVrrpTrackIfStatus_Type = RowStatus
_AgentRouterVrrpTrackIfStatus_Object = MibTableColumn
agentRouterVrrpTrackIfStatus = _AgentRouterVrrpTrackIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 1, 1, 4),
    _AgentRouterVrrpTrackIfStatus_Type()
)
agentRouterVrrpTrackIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRouterVrrpTrackIfStatus.setStatus("current")
_AgentRouterVrrpTrackRouteTable_Object = MibTable
agentRouterVrrpTrackRouteTable = _AgentRouterVrrpTrackRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    agentRouterVrrpTrackRouteTable.setStatus("current")
_AgentRouterVrrpTrackRouteEntry_Object = MibTableRow
agentRouterVrrpTrackRouteEntry = _AgentRouterVrrpTrackRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 2, 1)
)
agentRouterVrrpTrackRouteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentRouterVrrpTrackRtPfx"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentRouterVrrpTrackRtPfxLen"),
)
if mibBuilder.loadTexts:
    agentRouterVrrpTrackRouteEntry.setStatus("current")
_AgentRouterVrrpTrackRtPfx_Type = IpAddress
_AgentRouterVrrpTrackRtPfx_Object = MibTableColumn
agentRouterVrrpTrackRtPfx = _AgentRouterVrrpTrackRtPfx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 2, 1, 1),
    _AgentRouterVrrpTrackRtPfx_Type()
)
agentRouterVrrpTrackRtPfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRouterVrrpTrackRtPfx.setStatus("current")


class _AgentRouterVrrpTrackRtPfxLen_Type(Integer32):
    """Custom type agentRouterVrrpTrackRtPfxLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AgentRouterVrrpTrackRtPfxLen_Type.__name__ = "Integer32"
_AgentRouterVrrpTrackRtPfxLen_Object = MibTableColumn
agentRouterVrrpTrackRtPfxLen = _AgentRouterVrrpTrackRtPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 2, 1, 2),
    _AgentRouterVrrpTrackRtPfxLen_Type()
)
agentRouterVrrpTrackRtPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRouterVrrpTrackRtPfxLen.setStatus("current")


class _AgentRouterVrrpTrackRtPrioDec_Type(Integer32):
    """Custom type agentRouterVrrpTrackRtPrioDec based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AgentRouterVrrpTrackRtPrioDec_Type.__name__ = "Integer32"
_AgentRouterVrrpTrackRtPrioDec_Object = MibTableColumn
agentRouterVrrpTrackRtPrioDec = _AgentRouterVrrpTrackRtPrioDec_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 2, 1, 3),
    _AgentRouterVrrpTrackRtPrioDec_Type()
)
agentRouterVrrpTrackRtPrioDec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRouterVrrpTrackRtPrioDec.setStatus("current")
_AgentRouterVrrpTrackRtReachable_Type = TruthValue
_AgentRouterVrrpTrackRtReachable_Object = MibTableColumn
agentRouterVrrpTrackRtReachable = _AgentRouterVrrpTrackRtReachable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 2, 1, 4),
    _AgentRouterVrrpTrackRtReachable_Type()
)
agentRouterVrrpTrackRtReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouterVrrpTrackRtReachable.setStatus("current")
_AgentRouterVrrpTrackRtStatus_Type = RowStatus
_AgentRouterVrrpTrackRtStatus_Object = MibTableColumn
agentRouterVrrpTrackRtStatus = _AgentRouterVrrpTrackRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 10, 2, 1, 5),
    _AgentRouterVrrpTrackRtStatus_Type()
)
agentRouterVrrpTrackRtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRouterVrrpTrackRtStatus.setStatus("current")
_AgentIpHelperGroup_ObjectIdentity = ObjectIdentity
agentIpHelperGroup = _AgentIpHelperGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11)
)


class _AgentIpHelperAdminMode_Type(Integer32):
    """Custom type agentIpHelperAdminMode based on Integer32"""
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


_AgentIpHelperAdminMode_Type.__name__ = "Integer32"
_AgentIpHelperAdminMode_Object = MibScalar
agentIpHelperAdminMode = _AgentIpHelperAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 1),
    _AgentIpHelperAdminMode_Type()
)
agentIpHelperAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpHelperAdminMode.setStatus("current")
_AgentDhcpClientMsgsReceived_Type = Counter32
_AgentDhcpClientMsgsReceived_Object = MibScalar
agentDhcpClientMsgsReceived = _AgentDhcpClientMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 2),
    _AgentDhcpClientMsgsReceived_Type()
)
agentDhcpClientMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpClientMsgsReceived.setStatus("current")
_AgentDhcpClientMsgsRelayed_Type = Counter32
_AgentDhcpClientMsgsRelayed_Object = MibScalar
agentDhcpClientMsgsRelayed = _AgentDhcpClientMsgsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 3),
    _AgentDhcpClientMsgsRelayed_Type()
)
agentDhcpClientMsgsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpClientMsgsRelayed.setStatus("current")
_AgentDhcpServerMsgsReceived_Type = Counter32
_AgentDhcpServerMsgsReceived_Object = MibScalar
agentDhcpServerMsgsReceived = _AgentDhcpServerMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 4),
    _AgentDhcpServerMsgsReceived_Type()
)
agentDhcpServerMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerMsgsReceived.setStatus("current")
_AgentDhcpServerMsgsRelayed_Type = Counter32
_AgentDhcpServerMsgsRelayed_Object = MibScalar
agentDhcpServerMsgsRelayed = _AgentDhcpServerMsgsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 5),
    _AgentDhcpServerMsgsRelayed_Type()
)
agentDhcpServerMsgsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerMsgsRelayed.setStatus("current")
_AgentUdpClientMsgsReceived_Type = Counter32
_AgentUdpClientMsgsReceived_Object = MibScalar
agentUdpClientMsgsReceived = _AgentUdpClientMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 6),
    _AgentUdpClientMsgsReceived_Type()
)
agentUdpClientMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUdpClientMsgsReceived.setStatus("current")
_AgentUdpClientMsgsRelayed_Type = Counter32
_AgentUdpClientMsgsRelayed_Object = MibScalar
agentUdpClientMsgsRelayed = _AgentUdpClientMsgsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 7),
    _AgentUdpClientMsgsRelayed_Type()
)
agentUdpClientMsgsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUdpClientMsgsRelayed.setStatus("current")
_AgentSwitchIpHelperAddressTable_Object = MibTable
agentSwitchIpHelperAddressTable = _AgentSwitchIpHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 8)
)
if mibBuilder.loadTexts:
    agentSwitchIpHelperAddressTable.setStatus("current")
_AgentSwitchIpHelperAddressEntry_Object = MibTableRow
agentSwitchIpHelperAddressEntry = _AgentSwitchIpHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 8, 1)
)
agentSwitchIpHelperAddressEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIpHelperAddress"),
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchIpHelperUdpPort"),
)
if mibBuilder.loadTexts:
    agentSwitchIpHelperAddressEntry.setStatus("current")
_AgentSwitchIpHelperAddress_Type = IpAddress
_AgentSwitchIpHelperAddress_Object = MibTableColumn
agentSwitchIpHelperAddress = _AgentSwitchIpHelperAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 8, 1, 1),
    _AgentSwitchIpHelperAddress_Type()
)
agentSwitchIpHelperAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpHelperAddress.setStatus("current")


class _AgentSwitchIpHelperUdpPort_Type(Unsigned32):
    """Custom type agentSwitchIpHelperUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentSwitchIpHelperUdpPort_Type.__name__ = "Unsigned32"
_AgentSwitchIpHelperUdpPort_Object = MibTableColumn
agentSwitchIpHelperUdpPort = _AgentSwitchIpHelperUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 8, 1, 2),
    _AgentSwitchIpHelperUdpPort_Type()
)
agentSwitchIpHelperUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpHelperUdpPort.setStatus("current")
_AgentSwitchIpHelperHitCount_Type = Unsigned32
_AgentSwitchIpHelperHitCount_Object = MibTableColumn
agentSwitchIpHelperHitCount = _AgentSwitchIpHelperHitCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 8, 1, 3),
    _AgentSwitchIpHelperHitCount_Type()
)
agentSwitchIpHelperHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpHelperHitCount.setStatus("current")
_AgentSwitchIpHelperStatus_Type = RowStatus
_AgentSwitchIpHelperStatus_Object = MibTableColumn
agentSwitchIpHelperStatus = _AgentSwitchIpHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 8, 1, 4),
    _AgentSwitchIpHelperStatus_Type()
)
agentSwitchIpHelperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIpHelperStatus.setStatus("current")
_AgentUdpClientMsgsTtlExpired_Type = Counter32
_AgentUdpClientMsgsTtlExpired_Object = MibScalar
agentUdpClientMsgsTtlExpired = _AgentUdpClientMsgsTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 9),
    _AgentUdpClientMsgsTtlExpired_Type()
)
agentUdpClientMsgsTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUdpClientMsgsTtlExpired.setStatus("current")
_AgentUdpClientMsgsDiscarded_Type = Counter32
_AgentUdpClientMsgsDiscarded_Object = MibScalar
agentUdpClientMsgsDiscarded = _AgentUdpClientMsgsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 11, 10),
    _AgentUdpClientMsgsDiscarded_Type()
)
agentUdpClientMsgsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUdpClientMsgsDiscarded.setStatus("current")
_AgentInternalVlanGroup_ObjectIdentity = ObjectIdentity
agentInternalVlanGroup = _AgentInternalVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 12)
)


class _AgentInternalVlanBase_Type(Integer32):
    """Custom type agentInternalVlanBase based on Integer32"""
    defaultValue = 4093


_AgentInternalVlanBase_Object = MibScalar
agentInternalVlanBase = _AgentInternalVlanBase_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 12, 1),
    _AgentInternalVlanBase_Type()
)
agentInternalVlanBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInternalVlanBase.setStatus("current")


class _AgentInternalVlanPolicy_Type(Integer32):
    """Custom type agentInternalVlanPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 0),
          ("descending", 1))
    )


_AgentInternalVlanPolicy_Type.__name__ = "Integer32"
_AgentInternalVlanPolicy_Object = MibScalar
agentInternalVlanPolicy = _AgentInternalVlanPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 12, 2),
    _AgentInternalVlanPolicy_Type()
)
agentInternalVlanPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInternalVlanPolicy.setStatus("current")
_AgentSwitchInternalVlanTable_Object = MibTable
agentSwitchInternalVlanTable = _AgentSwitchInternalVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 12, 3)
)
if mibBuilder.loadTexts:
    agentSwitchInternalVlanTable.setStatus("current")
_AgentSwitchInternalVlanEntry_Object = MibTableRow
agentSwitchInternalVlanEntry = _AgentSwitchInternalVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 12, 3, 1)
)
agentSwitchInternalVlanEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentSwitchInternalVlanId"),
)
if mibBuilder.loadTexts:
    agentSwitchInternalVlanEntry.setStatus("current")


class _AgentSwitchInternalVlanId_Type(Integer32):
    """Custom type agentSwitchInternalVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchInternalVlanId_Type.__name__ = "Integer32"
_AgentSwitchInternalVlanId_Object = MibTableColumn
agentSwitchInternalVlanId = _AgentSwitchInternalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 12, 3, 1, 1),
    _AgentSwitchInternalVlanId_Type()
)
agentSwitchInternalVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchInternalVlanId.setStatus("current")
_AgentSwitchInternalVlanIfIndex_Type = Integer32
_AgentSwitchInternalVlanIfIndex_Object = MibTableColumn
agentSwitchInternalVlanIfIndex = _AgentSwitchInternalVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 12, 3, 1, 2),
    _AgentSwitchInternalVlanIfIndex_Type()
)
agentSwitchInternalVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchInternalVlanIfIndex.setStatus("current")
_AgentOspfQueueGroup_ObjectIdentity = ObjectIdentity
agentOspfQueueGroup = _AgentOspfQueueGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 13)
)
_AgentOspfQueueTable_Object = MibTable
agentOspfQueueTable = _AgentOspfQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    agentOspfQueueTable.setStatus("current")
_AgentOspfQueueEntry_Object = MibTableRow
agentOspfQueueEntry = _AgentOspfQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 13, 1, 1)
)
agentOspfQueueEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfQueueIndex"),
)
if mibBuilder.loadTexts:
    agentOspfQueueEntry.setStatus("current")
_AgentOspfQueueIndex_Type = Unsigned32
_AgentOspfQueueIndex_Object = MibTableColumn
agentOspfQueueIndex = _AgentOspfQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 13, 1, 1, 1),
    _AgentOspfQueueIndex_Type()
)
agentOspfQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentOspfQueueIndex.setStatus("current")
_AgentOspfQueueName_Type = DisplayString
_AgentOspfQueueName_Object = MibTableColumn
agentOspfQueueName = _AgentOspfQueueName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 13, 1, 1, 2),
    _AgentOspfQueueName_Type()
)
agentOspfQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfQueueName.setStatus("current")
_AgentOspfQueueLength_Type = Gauge32
_AgentOspfQueueLength_Object = MibTableColumn
agentOspfQueueLength = _AgentOspfQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 13, 1, 1, 3),
    _AgentOspfQueueLength_Type()
)
agentOspfQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfQueueLength.setStatus("current")
_AgentOspfQueueHigh_Type = Gauge32
_AgentOspfQueueHigh_Object = MibTableColumn
agentOspfQueueHigh = _AgentOspfQueueHigh_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 13, 1, 1, 4),
    _AgentOspfQueueHigh_Type()
)
agentOspfQueueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfQueueHigh.setStatus("current")
_AgentOspfQueueDrops_Type = Counter32
_AgentOspfQueueDrops_Object = MibTableColumn
agentOspfQueueDrops = _AgentOspfQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 13, 1, 1, 5),
    _AgentOspfQueueDrops_Type()
)
agentOspfQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfQueueDrops.setStatus("current")
_AgentOspfQueueLimit_Type = Unsigned32
_AgentOspfQueueLimit_Object = MibTableColumn
agentOspfQueueLimit = _AgentOspfQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 13, 1, 1, 6),
    _AgentOspfQueueLimit_Type()
)
agentOspfQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfQueueLimit.setStatus("current")
_AgentOspfPacketStatsGroup_ObjectIdentity = ObjectIdentity
agentOspfPacketStatsGroup = _AgentOspfPacketStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14)
)
_AgentOspfCountersCleared_Type = Unsigned32
_AgentOspfCountersCleared_Object = MibScalar
agentOspfCountersCleared = _AgentOspfCountersCleared_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 1),
    _AgentOspfCountersCleared_Type()
)
agentOspfCountersCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfCountersCleared.setStatus("current")
_AgentOspfLsaRetxCount_Type = Counter32
_AgentOspfLsaRetxCount_Object = MibScalar
agentOspfLsaRetxCount = _AgentOspfLsaRetxCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 2),
    _AgentOspfLsaRetxCount_Type()
)
agentOspfLsaRetxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLsaRetxCount.setStatus("current")
_AgentOspfHellosRx_Type = Counter32
_AgentOspfHellosRx_Object = MibScalar
agentOspfHellosRx = _AgentOspfHellosRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 3),
    _AgentOspfHellosRx_Type()
)
agentOspfHellosRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfHellosRx.setStatus("current")
_AgentOspfHellosTx_Type = Counter32
_AgentOspfHellosTx_Object = MibScalar
agentOspfHellosTx = _AgentOspfHellosTx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 4),
    _AgentOspfHellosTx_Type()
)
agentOspfHellosTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfHellosTx.setStatus("current")
_AgentOspfDdRx_Type = Counter32
_AgentOspfDdRx_Object = MibScalar
agentOspfDdRx = _AgentOspfDdRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 5),
    _AgentOspfDdRx_Type()
)
agentOspfDdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfDdRx.setStatus("current")
_AgentOspfDdTx_Type = Counter32
_AgentOspfDdTx_Object = MibScalar
agentOspfDdTx = _AgentOspfDdTx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 6),
    _AgentOspfDdTx_Type()
)
agentOspfDdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfDdTx.setStatus("current")
_AgentOspfLsReqRx_Type = Counter32
_AgentOspfLsReqRx_Object = MibScalar
agentOspfLsReqRx = _AgentOspfLsReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 7),
    _AgentOspfLsReqRx_Type()
)
agentOspfLsReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLsReqRx.setStatus("current")
_AgentOspfLsReqTx_Type = Counter32
_AgentOspfLsReqTx_Object = MibScalar
agentOspfLsReqTx = _AgentOspfLsReqTx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 8),
    _AgentOspfLsReqTx_Type()
)
agentOspfLsReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLsReqTx.setStatus("current")
_AgentOspfLsUpdatesRx_Type = Counter32
_AgentOspfLsUpdatesRx_Object = MibScalar
agentOspfLsUpdatesRx = _AgentOspfLsUpdatesRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 9),
    _AgentOspfLsUpdatesRx_Type()
)
agentOspfLsUpdatesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLsUpdatesRx.setStatus("current")
_AgentOspfLsUpdatesTx_Type = Counter32
_AgentOspfLsUpdatesTx_Object = MibScalar
agentOspfLsUpdatesTx = _AgentOspfLsUpdatesTx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 10),
    _AgentOspfLsUpdatesTx_Type()
)
agentOspfLsUpdatesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLsUpdatesTx.setStatus("current")
_AgentOspfLsAckRx_Type = Counter32
_AgentOspfLsAckRx_Object = MibScalar
agentOspfLsAckRx = _AgentOspfLsAckRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 11),
    _AgentOspfLsAckRx_Type()
)
agentOspfLsAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLsAckRx.setStatus("current")
_AgentOspfLsAckTx_Type = Counter32
_AgentOspfLsAckTx_Object = MibScalar
agentOspfLsAckTx = _AgentOspfLsAckTx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 12),
    _AgentOspfLsAckTx_Type()
)
agentOspfLsAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLsAckTx.setStatus("current")
_AgentOspfLsUpdatesRxMax_Type = Gauge32
_AgentOspfLsUpdatesRxMax_Object = MibScalar
agentOspfLsUpdatesRxMax = _AgentOspfLsUpdatesRxMax_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 13),
    _AgentOspfLsUpdatesRxMax_Type()
)
agentOspfLsUpdatesRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLsUpdatesRxMax.setStatus("current")
_AgentOspfLsUpdatesTxMax_Type = Gauge32
_AgentOspfLsUpdatesTxMax_Object = MibScalar
agentOspfLsUpdatesTxMax = _AgentOspfLsUpdatesTxMax_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 14),
    _AgentOspfLsUpdatesTxMax_Type()
)
agentOspfLsUpdatesTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfLsUpdatesTxMax.setStatus("current")
_AgentOspfType1LsasRx_Type = Counter32
_AgentOspfType1LsasRx_Object = MibScalar
agentOspfType1LsasRx = _AgentOspfType1LsasRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 15),
    _AgentOspfType1LsasRx_Type()
)
agentOspfType1LsasRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfType1LsasRx.setStatus("current")
_AgentOspfType2LsasRx_Type = Counter32
_AgentOspfType2LsasRx_Object = MibScalar
agentOspfType2LsasRx = _AgentOspfType2LsasRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 16),
    _AgentOspfType2LsasRx_Type()
)
agentOspfType2LsasRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfType2LsasRx.setStatus("current")
_AgentOspfType3LsasRx_Type = Counter32
_AgentOspfType3LsasRx_Object = MibScalar
agentOspfType3LsasRx = _AgentOspfType3LsasRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 17),
    _AgentOspfType3LsasRx_Type()
)
agentOspfType3LsasRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfType3LsasRx.setStatus("current")
_AgentOspfType4LsasRx_Type = Counter32
_AgentOspfType4LsasRx_Object = MibScalar
agentOspfType4LsasRx = _AgentOspfType4LsasRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 18),
    _AgentOspfType4LsasRx_Type()
)
agentOspfType4LsasRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfType4LsasRx.setStatus("current")
_AgentOspfType5LsasRx_Type = Counter32
_AgentOspfType5LsasRx_Object = MibScalar
agentOspfType5LsasRx = _AgentOspfType5LsasRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 19),
    _AgentOspfType5LsasRx_Type()
)
agentOspfType5LsasRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfType5LsasRx.setStatus("current")
_AgentOspfType7LsasRx_Type = Counter32
_AgentOspfType7LsasRx_Object = MibScalar
agentOspfType7LsasRx = _AgentOspfType7LsasRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 20),
    _AgentOspfType7LsasRx_Type()
)
agentOspfType7LsasRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfType7LsasRx.setStatus("current")
_AgentOspfType9LsasRx_Type = Counter32
_AgentOspfType9LsasRx_Object = MibScalar
agentOspfType9LsasRx = _AgentOspfType9LsasRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 21),
    _AgentOspfType9LsasRx_Type()
)
agentOspfType9LsasRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfType9LsasRx.setStatus("current")
_AgentOspfType10LsasRx_Type = Counter32
_AgentOspfType10LsasRx_Object = MibScalar
agentOspfType10LsasRx = _AgentOspfType10LsasRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 22),
    _AgentOspfType10LsasRx_Type()
)
agentOspfType10LsasRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfType10LsasRx.setStatus("current")
_AgentOspfType11LsasRx_Type = Counter32
_AgentOspfType11LsasRx_Object = MibScalar
agentOspfType11LsasRx = _AgentOspfType11LsasRx_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 14, 23),
    _AgentOspfType11LsasRx_Type()
)
agentOspfType11LsasRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfType11LsasRx.setStatus("current")
_AgentOspfSpfStatsTable_Object = MibTable
agentOspfSpfStatsTable = _AgentOspfSpfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    agentOspfSpfStatsTable.setStatus("current")
_AgentOspfSpfStatsEntry_Object = MibTableRow
agentOspfSpfStatsEntry = _AgentOspfSpfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15, 1)
)
agentOspfSpfStatsEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentOspfSpfIndex"),
)
if mibBuilder.loadTexts:
    agentOspfSpfStatsEntry.setStatus("current")
_AgentOspfSpfIndex_Type = Counter32
_AgentOspfSpfIndex_Object = MibTableColumn
agentOspfSpfIndex = _AgentOspfSpfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15, 1, 1),
    _AgentOspfSpfIndex_Type()
)
agentOspfSpfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentOspfSpfIndex.setStatus("current")
_AgentOspfSpfStatsDeltaT_Type = Unsigned32
_AgentOspfSpfStatsDeltaT_Object = MibTableColumn
agentOspfSpfStatsDeltaT = _AgentOspfSpfStatsDeltaT_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15, 1, 2),
    _AgentOspfSpfStatsDeltaT_Type()
)
agentOspfSpfStatsDeltaT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfSpfStatsDeltaT.setStatus("current")
_AgentOspfSpfStatsIntra_Type = Gauge32
_AgentOspfSpfStatsIntra_Object = MibTableColumn
agentOspfSpfStatsIntra = _AgentOspfSpfStatsIntra_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15, 1, 3),
    _AgentOspfSpfStatsIntra_Type()
)
agentOspfSpfStatsIntra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfSpfStatsIntra.setStatus("current")
_AgentOspfSpfStatsSumm_Type = Gauge32
_AgentOspfSpfStatsSumm_Object = MibTableColumn
agentOspfSpfStatsSumm = _AgentOspfSpfStatsSumm_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15, 1, 4),
    _AgentOspfSpfStatsSumm_Type()
)
agentOspfSpfStatsSumm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfSpfStatsSumm.setStatus("current")
_AgentOspfSpfStatsExt_Type = Gauge32
_AgentOspfSpfStatsExt_Object = MibTableColumn
agentOspfSpfStatsExt = _AgentOspfSpfStatsExt_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15, 1, 5),
    _AgentOspfSpfStatsExt_Type()
)
agentOspfSpfStatsExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfSpfStatsExt.setStatus("current")
_AgentOspfSpfStatsSpfTotal_Type = Gauge32
_AgentOspfSpfStatsSpfTotal_Object = MibTableColumn
agentOspfSpfStatsSpfTotal = _AgentOspfSpfStatsSpfTotal_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15, 1, 6),
    _AgentOspfSpfStatsSpfTotal_Type()
)
agentOspfSpfStatsSpfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfSpfStatsSpfTotal.setStatus("current")
_AgentOspfSpfStatsRibUpdate_Type = Gauge32
_AgentOspfSpfStatsRibUpdate_Object = MibTableColumn
agentOspfSpfStatsRibUpdate = _AgentOspfSpfStatsRibUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15, 1, 7),
    _AgentOspfSpfStatsRibUpdate_Type()
)
agentOspfSpfStatsRibUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfSpfStatsRibUpdate.setStatus("current")
_AgentOspfSpfStatsReason_Type = DisplayString
_AgentOspfSpfStatsReason_Object = MibTableColumn
agentOspfSpfStatsReason = _AgentOspfSpfStatsReason_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 15, 1, 8),
    _AgentOspfSpfStatsReason_Type()
)
agentOspfSpfStatsReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfSpfStatsReason.setStatus("current")
_AgentRoutingHeapGroup_ObjectIdentity = ObjectIdentity
agentRoutingHeapGroup = _AgentRoutingHeapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 16)
)
_AgentRoutingHeapSize_Type = Unsigned32
_AgentRoutingHeapSize_Object = MibScalar
agentRoutingHeapSize = _AgentRoutingHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 16, 1),
    _AgentRoutingHeapSize_Type()
)
agentRoutingHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRoutingHeapSize.setStatus("current")
_AgentRoutingHeapInUse_Type = Gauge32
_AgentRoutingHeapInUse_Object = MibScalar
agentRoutingHeapInUse = _AgentRoutingHeapInUse_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 16, 2),
    _AgentRoutingHeapInUse_Type()
)
agentRoutingHeapInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRoutingHeapInUse.setStatus("current")
_AgentRoutingHeapHigh_Type = Gauge32
_AgentRoutingHeapHigh_Object = MibScalar
agentRoutingHeapHigh = _AgentRoutingHeapHigh_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 16, 3),
    _AgentRoutingHeapHigh_Type()
)
agentRoutingHeapHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRoutingHeapHigh.setStatus("current")
_AgentRoutingTableSummaryGroup_ObjectIdentity = ObjectIdentity
agentRoutingTableSummaryGroup = _AgentRoutingTableSummaryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17)
)
_AgentConnectedRoutes_Type = Gauge32
_AgentConnectedRoutes_Object = MibScalar
agentConnectedRoutes = _AgentConnectedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 1),
    _AgentConnectedRoutes_Type()
)
agentConnectedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentConnectedRoutes.setStatus("current")
_AgentStaticRoutes_Type = Gauge32
_AgentStaticRoutes_Object = MibScalar
agentStaticRoutes = _AgentStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 2),
    _AgentStaticRoutes_Type()
)
agentStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStaticRoutes.setStatus("current")
_AgentRipRoutes_Type = Gauge32
_AgentRipRoutes_Object = MibScalar
agentRipRoutes = _AgentRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 3),
    _AgentRipRoutes_Type()
)
agentRipRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRipRoutes.setStatus("current")
_AgentOspfRoutes_Type = Gauge32
_AgentOspfRoutes_Object = MibScalar
agentOspfRoutes = _AgentOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 4),
    _AgentOspfRoutes_Type()
)
agentOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfRoutes.setStatus("current")
_AgentOspfIntraRoutes_Type = Gauge32
_AgentOspfIntraRoutes_Object = MibScalar
agentOspfIntraRoutes = _AgentOspfIntraRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 5),
    _AgentOspfIntraRoutes_Type()
)
agentOspfIntraRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfIntraRoutes.setStatus("current")
_AgentOspfInterRoutes_Type = Gauge32
_AgentOspfInterRoutes_Object = MibScalar
agentOspfInterRoutes = _AgentOspfInterRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 6),
    _AgentOspfInterRoutes_Type()
)
agentOspfInterRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfInterRoutes.setStatus("current")
_AgentOspfExt1Routes_Type = Gauge32
_AgentOspfExt1Routes_Object = MibScalar
agentOspfExt1Routes = _AgentOspfExt1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 7),
    _AgentOspfExt1Routes_Type()
)
agentOspfExt1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfExt1Routes.setStatus("current")
_AgentOspfExt2Routes_Type = Gauge32
_AgentOspfExt2Routes_Object = MibScalar
agentOspfExt2Routes = _AgentOspfExt2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 8),
    _AgentOspfExt2Routes_Type()
)
agentOspfExt2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfExt2Routes.setStatus("current")
_AgentBgpRoutes_Type = Gauge32
_AgentBgpRoutes_Object = MibScalar
agentBgpRoutes = _AgentBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 9),
    _AgentBgpRoutes_Type()
)
agentBgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBgpRoutes.setStatus("current")
_AgentEbgpRoutes_Type = Gauge32
_AgentEbgpRoutes_Object = MibScalar
agentEbgpRoutes = _AgentEbgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 10),
    _AgentEbgpRoutes_Type()
)
agentEbgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEbgpRoutes.setStatus("current")
_AgentIbgpRoutes_Type = Gauge32
_AgentIbgpRoutes_Object = MibScalar
agentIbgpRoutes = _AgentIbgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 11),
    _AgentIbgpRoutes_Type()
)
agentIbgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIbgpRoutes.setStatus("current")
_AgentLocalBgpRoutes_Type = Gauge32
_AgentLocalBgpRoutes_Object = MibScalar
agentLocalBgpRoutes = _AgentLocalBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 12),
    _AgentLocalBgpRoutes_Type()
)
agentLocalBgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLocalBgpRoutes.setStatus("current")
_AgentRejectRoutes_Type = Gauge32
_AgentRejectRoutes_Object = MibScalar
agentRejectRoutes = _AgentRejectRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 13),
    _AgentRejectRoutes_Type()
)
agentRejectRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRejectRoutes.setStatus("current")
_AgentTotalRoutes_Type = Gauge32
_AgentTotalRoutes_Object = MibScalar
agentTotalRoutes = _AgentTotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 14),
    _AgentTotalRoutes_Type()
)
agentTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTotalRoutes.setStatus("current")
_AgentBestRoutes_Type = Gauge32
_AgentBestRoutes_Object = MibScalar
agentBestRoutes = _AgentBestRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 15),
    _AgentBestRoutes_Type()
)
agentBestRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBestRoutes.setStatus("current")
_AgentBestRoutesHigh_Type = Gauge32
_AgentBestRoutesHigh_Object = MibScalar
agentBestRoutesHigh = _AgentBestRoutesHigh_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 16),
    _AgentBestRoutesHigh_Type()
)
agentBestRoutesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBestRoutesHigh.setStatus("current")
_AgentAlternateRoutes_Type = Gauge32
_AgentAlternateRoutes_Object = MibScalar
agentAlternateRoutes = _AgentAlternateRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 17),
    _AgentAlternateRoutes_Type()
)
agentAlternateRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAlternateRoutes.setStatus("current")
_AgentRouteAdds_Type = Counter32
_AgentRouteAdds_Object = MibScalar
agentRouteAdds = _AgentRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 18),
    _AgentRouteAdds_Type()
)
agentRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouteAdds.setStatus("current")
_AgentRouteModifies_Type = Counter32
_AgentRouteModifies_Object = MibScalar
agentRouteModifies = _AgentRouteModifies_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 19),
    _AgentRouteModifies_Type()
)
agentRouteModifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouteModifies.setStatus("current")
_AgentRouteDeletes_Type = Counter32
_AgentRouteDeletes_Object = MibScalar
agentRouteDeletes = _AgentRouteDeletes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 20),
    _AgentRouteDeletes_Type()
)
agentRouteDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouteDeletes.setStatus("current")
_AgentUnresolvedRouteAdds_Type = Counter32
_AgentUnresolvedRouteAdds_Object = MibScalar
agentUnresolvedRouteAdds = _AgentUnresolvedRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 21),
    _AgentUnresolvedRouteAdds_Type()
)
agentUnresolvedRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUnresolvedRouteAdds.setStatus("current")
_AgentInvalidRouteAdds_Type = Counter32
_AgentInvalidRouteAdds_Object = MibScalar
agentInvalidRouteAdds = _AgentInvalidRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 22),
    _AgentInvalidRouteAdds_Type()
)
agentInvalidRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInvalidRouteAdds.setStatus("current")
_AgentFailedRouteAdds_Type = Counter32
_AgentFailedRouteAdds_Object = MibScalar
agentFailedRouteAdds = _AgentFailedRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 23),
    _AgentFailedRouteAdds_Type()
)
agentFailedRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFailedRouteAdds.setStatus("current")
_AgentReservedLocals_Type = Gauge32
_AgentReservedLocals_Object = MibScalar
agentReservedLocals = _AgentReservedLocals_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 24),
    _AgentReservedLocals_Type()
)
agentReservedLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentReservedLocals.setStatus("current")
_AgentUniqueNextHops_Type = Gauge32
_AgentUniqueNextHops_Object = MibScalar
agentUniqueNextHops = _AgentUniqueNextHops_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 25),
    _AgentUniqueNextHops_Type()
)
agentUniqueNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUniqueNextHops.setStatus("current")
_AgentUniqueNextHopsHigh_Type = Gauge32
_AgentUniqueNextHopsHigh_Object = MibScalar
agentUniqueNextHopsHigh = _AgentUniqueNextHopsHigh_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 26),
    _AgentUniqueNextHopsHigh_Type()
)
agentUniqueNextHopsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUniqueNextHopsHigh.setStatus("current")
_AgentNextHopGroups_Type = Gauge32
_AgentNextHopGroups_Object = MibScalar
agentNextHopGroups = _AgentNextHopGroups_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 27),
    _AgentNextHopGroups_Type()
)
agentNextHopGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNextHopGroups.setStatus("current")
_AgentNextHopGroupsHigh_Type = Gauge32
_AgentNextHopGroupsHigh_Object = MibScalar
agentNextHopGroupsHigh = _AgentNextHopGroupsHigh_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 28),
    _AgentNextHopGroupsHigh_Type()
)
agentNextHopGroupsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNextHopGroupsHigh.setStatus("current")
_AgentEcmpGroups_Type = Gauge32
_AgentEcmpGroups_Object = MibScalar
agentEcmpGroups = _AgentEcmpGroups_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 29),
    _AgentEcmpGroups_Type()
)
agentEcmpGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpGroups.setStatus("current")
_AgentEcmpGroupsHigh_Type = Gauge32
_AgentEcmpGroupsHigh_Object = MibScalar
agentEcmpGroupsHigh = _AgentEcmpGroupsHigh_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 30),
    _AgentEcmpGroupsHigh_Type()
)
agentEcmpGroupsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpGroupsHigh.setStatus("current")
_AgentEcmpRoutes_Type = Gauge32
_AgentEcmpRoutes_Object = MibScalar
agentEcmpRoutes = _AgentEcmpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 31),
    _AgentEcmpRoutes_Type()
)
agentEcmpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpRoutes.setStatus("current")
_AgentTruncEcmpRoutes_Type = Gauge32
_AgentTruncEcmpRoutes_Object = MibScalar
agentTruncEcmpRoutes = _AgentTruncEcmpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 32),
    _AgentTruncEcmpRoutes_Type()
)
agentTruncEcmpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTruncEcmpRoutes.setStatus("current")
_AgentEcmpRetries_Type = Counter32
_AgentEcmpRetries_Object = MibScalar
agentEcmpRetries = _AgentEcmpRetries_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 17, 33),
    _AgentEcmpRetries_Type()
)
agentEcmpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpRetries.setStatus("current")
_AgentEcmpCountTable_Object = MibTable
agentEcmpCountTable = _AgentEcmpCountTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 18)
)
if mibBuilder.loadTexts:
    agentEcmpCountTable.setStatus("current")
_AgentEcmpCountEntry_Object = MibTableRow
agentEcmpCountEntry = _AgentEcmpCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 18, 1)
)
agentEcmpCountEntry.setIndexNames(
    (0, "EdgeSwitch-ROUTING-MIB", "agentEcmpNextHopCount"),
)
if mibBuilder.loadTexts:
    agentEcmpCountEntry.setStatus("current")


class _AgentEcmpNextHopCount_Type(Unsigned32):
    """Custom type agentEcmpNextHopCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentEcmpNextHopCount_Type.__name__ = "Unsigned32"
_AgentEcmpNextHopCount_Object = MibTableColumn
agentEcmpNextHopCount = _AgentEcmpNextHopCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 18, 1, 1),
    _AgentEcmpNextHopCount_Type()
)
agentEcmpNextHopCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentEcmpNextHopCount.setStatus("current")
_AgentEcmpRouteCount_Type = Gauge32
_AgentEcmpRouteCount_Object = MibTableColumn
agentEcmpRouteCount = _AgentEcmpRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 18, 1, 2),
    _AgentEcmpRouteCount_Type()
)
agentEcmpRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpRouteCount.setStatus("current")
_AgentOspfStubRouterGroup_ObjectIdentity = ObjectIdentity
agentOspfStubRouterGroup = _AgentOspfStubRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 19)
)


class _OspfStubRouterAdvertisement_Type(Integer32):
    """Custom type ospfStubRouterAdvertisement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("doNotAdvertise", 1))
    )


_OspfStubRouterAdvertisement_Type.__name__ = "Integer32"
_OspfStubRouterAdvertisement_Object = MibScalar
ospfStubRouterAdvertisement = _OspfStubRouterAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 19, 1),
    _OspfStubRouterAdvertisement_Type()
)
ospfStubRouterAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStubRouterAdvertisement.setStatus("current")


class _AgentOspfStubRouterReason_Type(Integer32):
    """Custom type agentOspfStubRouterReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 0),
          ("resource-limitation", 2),
          ("startup", 1))
    )


_AgentOspfStubRouterReason_Type.__name__ = "Integer32"
_AgentOspfStubRouterReason_Object = MibScalar
agentOspfStubRouterReason = _AgentOspfStubRouterReason_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 19, 2),
    _AgentOspfStubRouterReason_Type()
)
agentOspfStubRouterReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfStubRouterReason.setStatus("current")
_AgentOspfStubRouterStartupTimeRemaining_Type = Unsigned32
_AgentOspfStubRouterStartupTimeRemaining_Object = MibScalar
agentOspfStubRouterStartupTimeRemaining = _AgentOspfStubRouterStartupTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 19, 3),
    _AgentOspfStubRouterStartupTimeRemaining_Type()
)
agentOspfStubRouterStartupTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfStubRouterStartupTimeRemaining.setStatus("current")
_AgentOspfStubRouterDuration_Type = Unsigned32
_AgentOspfStubRouterDuration_Object = MibScalar
agentOspfStubRouterDuration = _AgentOspfStubRouterDuration_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 2, 19, 4),
    _AgentOspfStubRouterDuration_Type()
)
agentOspfStubRouterDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfStubRouterDuration.setStatus("current")
rip2IfConfEntry.registerAugmentions(
    ("EdgeSwitch-ROUTING-MIB",
     "agentRip2IfConfEntry")
)
agentRip2IfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("EdgeSwitch-ROUTING-MIB",
     "agentOspfIfEntry")
)
agentOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("EdgeSwitch-ROUTING-MIB",
     "agentOspfVirtIfEntry")
)
agentOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-ROUTING-MIB",
    **{"SpfTimerRange": SpfTimerRange,
       "AutoCostRefBw": AutoCostRefBw,
       "fastPathRouting": fastPathRouting,
       "agentSwitchArpGroup": agentSwitchArpGroup,
       "agentSwitchArpAgeoutTime": agentSwitchArpAgeoutTime,
       "agentSwitchArpResponseTime": agentSwitchArpResponseTime,
       "agentSwitchArpMaxRetries": agentSwitchArpMaxRetries,
       "agentSwitchArpCacheSize": agentSwitchArpCacheSize,
       "agentSwitchArpDynamicRenew": agentSwitchArpDynamicRenew,
       "agentSwitchArpTotalEntryCountCurrent": agentSwitchArpTotalEntryCountCurrent,
       "agentSwitchArpTotalEntryCountPeak": agentSwitchArpTotalEntryCountPeak,
       "agentSwitchArpStaticEntryCountCurrent": agentSwitchArpStaticEntryCountCurrent,
       "agentSwitchArpStaticEntryCountMax": agentSwitchArpStaticEntryCountMax,
       "agentSwitchArpTable": agentSwitchArpTable,
       "agentSwitchArpEntry": agentSwitchArpEntry,
       "agentSwitchArpAge": agentSwitchArpAge,
       "agentSwitchArpIpAddress": agentSwitchArpIpAddress,
       "agentSwitchArpMacAddress": agentSwitchArpMacAddress,
       "agentSwitchArpInterface": agentSwitchArpInterface,
       "agentSwitchArpType": agentSwitchArpType,
       "agentSwitchArpStatus": agentSwitchArpStatus,
       "agentSwitchLocalProxyArpTable": agentSwitchLocalProxyArpTable,
       "agentSwitchLocalProxyArpEntry": agentSwitchLocalProxyArpEntry,
       "agentSwitchLocalProxyArpMode": agentSwitchLocalProxyArpMode,
       "agentSwitchIntfArpTable": agentSwitchIntfArpTable,
       "agentSwitchIntfArpEntry": agentSwitchIntfArpEntry,
       "agentSwitchIntfArpIpAddress": agentSwitchIntfArpIpAddress,
       "agentSwitchIntfArpIfIndex": agentSwitchIntfArpIfIndex,
       "agentSwitchIntfArpAge": agentSwitchIntfArpAge,
       "agentSwitchIntfArpMacAddress": agentSwitchIntfArpMacAddress,
       "agentSwitchIntfArpType": agentSwitchIntfArpType,
       "agentSwitchIntfArpStatus": agentSwitchIntfArpStatus,
       "agentSwitchIpGroup": agentSwitchIpGroup,
       "agentSwitchIpRoutingMode": agentSwitchIpRoutingMode,
       "agentSwitchIpDefaultGateway": agentSwitchIpDefaultGateway,
       "agentSwitchIpInterfaceTable": agentSwitchIpInterfaceTable,
       "agentSwitchIpInterfaceEntry": agentSwitchIpInterfaceEntry,
       "agentSwitchIpInterfaceIfIndex": agentSwitchIpInterfaceIfIndex,
       "agentSwitchIPAddressConfigMethod": agentSwitchIPAddressConfigMethod,
       "agentSwitchIpInterfaceIpAddress": agentSwitchIpInterfaceIpAddress,
       "agentSwitchIpInterfaceNetMask": agentSwitchIpInterfaceNetMask,
       "agentSwitchIpInterfaceClearIp": agentSwitchIpInterfaceClearIp,
       "agentSwitchIpInterfaceRoutingMode": agentSwitchIpInterfaceRoutingMode,
       "agentSwitchIpInterfaceProxyARPMode": agentSwitchIpInterfaceProxyARPMode,
       "agentSwitchIpInterfaceMtuValue": agentSwitchIpInterfaceMtuValue,
       "agentSwitchIpInterfaceBandwidth": agentSwitchIpInterfaceBandwidth,
       "agentSwitchIpInterfaceUnnumberedIfIndex": agentSwitchIpInterfaceUnnumberedIfIndex,
       "agentSwitchIpInterfaceIcmpUnreachables": agentSwitchIpInterfaceIcmpUnreachables,
       "agentSwitchIpInterfaceIcmpRedirects": agentSwitchIpInterfaceIcmpRedirects,
       "agentSwitchDhcpOperation": agentSwitchDhcpOperation,
       "agentSwitchIpInterfaceSuppressed": agentSwitchIpInterfaceSuppressed,
       "agentSwitchIpInterfaceNumberOfFlaps": agentSwitchIpInterfaceNumberOfFlaps,
       "agentSwitchIpInterfaceCurrentPenalty": agentSwitchIpInterfaceCurrentPenalty,
       "agentSwitchIpInterfaceReUseTime": agentSwitchIpInterfaceReUseTime,
       "agentSwitchIpRouterDiscoveryTable": agentSwitchIpRouterDiscoveryTable,
       "agentSwitchIpRouterDiscoveryEntry": agentSwitchIpRouterDiscoveryEntry,
       "agentSwitchIpRouterDiscoveryIfIndex": agentSwitchIpRouterDiscoveryIfIndex,
       "agentSwitchIpRouterDiscoveryAdvertiseMode": agentSwitchIpRouterDiscoveryAdvertiseMode,
       "agentSwitchIpRouterDiscoveryMaxAdvertisementInterval": agentSwitchIpRouterDiscoveryMaxAdvertisementInterval,
       "agentSwitchIpRouterDiscoveryMinAdvertisementInterval": agentSwitchIpRouterDiscoveryMinAdvertisementInterval,
       "agentSwitchIpRouterDiscoveryAdvertisementLifetime": agentSwitchIpRouterDiscoveryAdvertisementLifetime,
       "agentSwitchIpRouterDiscoveryPreferenceLevel": agentSwitchIpRouterDiscoveryPreferenceLevel,
       "agentSwitchIpRouterDiscoveryAdvertisementAddress": agentSwitchIpRouterDiscoveryAdvertisementAddress,
       "agentSwitchIpVlanTable": agentSwitchIpVlanTable,
       "agentSwitchIpVlanEntry": agentSwitchIpVlanEntry,
       "agentSwitchIpVlanId": agentSwitchIpVlanId,
       "agentSwitchIpVlanIfIndex": agentSwitchIpVlanIfIndex,
       "agentSwitchIpVlanRoutingStatus": agentSwitchIpVlanRoutingStatus,
       "agentSwitchSecondaryAddressTable": agentSwitchSecondaryAddressTable,
       "agentSwitchSecondaryAddressEntry": agentSwitchSecondaryAddressEntry,
       "agentSwitchSecondaryIpAddress": agentSwitchSecondaryIpAddress,
       "agentSwitchSecondaryNetMask": agentSwitchSecondaryNetMask,
       "agentSwitchSecondaryStatus": agentSwitchSecondaryStatus,
       "agentSwitchHelperAddressTable": agentSwitchHelperAddressTable,
       "agentSwitchHelperAddressEntry": agentSwitchHelperAddressEntry,
       "agentSwitchHelperIpAddress": agentSwitchHelperIpAddress,
       "agentSwitchHelperStatus": agentSwitchHelperStatus,
       "agentSwitchIpIcmpControlGroup": agentSwitchIpIcmpControlGroup,
       "agentSwitchIpIcmpEchoReplyMode": agentSwitchIpIcmpEchoReplyMode,
       "agentSwitchIpIcmpRedirectsMode": agentSwitchIpIcmpRedirectsMode,
       "agentSwitchIpIcmpRateLimitInterval": agentSwitchIpIcmpRateLimitInterval,
       "agentSwitchIpIcmpRateLimitBurstSize": agentSwitchIpIcmpRateLimitBurstSize,
       "agentSwitchIntfIpHelperAddressTable": agentSwitchIntfIpHelperAddressTable,
       "agentSwitchIntfIpHelperAddressEntry": agentSwitchIntfIpHelperAddressEntry,
       "agentSwitchIntfIpHelperIpAddress": agentSwitchIntfIpHelperIpAddress,
       "agentSwitchIntfIpHelperUdpPort": agentSwitchIntfIpHelperUdpPort,
       "agentSwitchIntfIpHelperDiscard": agentSwitchIntfIpHelperDiscard,
       "agentSwitchIntfIpHelperHitCount": agentSwitchIntfIpHelperHitCount,
       "agentSwitchIntfIpHelperStatus": agentSwitchIntfIpHelperStatus,
       "agentSwitchClearIpDefaultGateway": agentSwitchClearIpDefaultGateway,
       "agentRouterRipConfigGroup": agentRouterRipConfigGroup,
       "agentRouterRipAdminState": agentRouterRipAdminState,
       "agentRouterRipSplitHorizonMode": agentRouterRipSplitHorizonMode,
       "agentRouterRipAutoSummaryMode": agentRouterRipAutoSummaryMode,
       "agentRouterRipHostRoutesAcceptMode": agentRouterRipHostRoutesAcceptMode,
       "agentRouterRipDefaultMetric": agentRouterRipDefaultMetric,
       "agentRouterRipDefaultMetricConfigured": agentRouterRipDefaultMetricConfigured,
       "agentRouterRipDefaultInfoOriginate": agentRouterRipDefaultInfoOriginate,
       "agentRipRouteRedistTable": agentRipRouteRedistTable,
       "agentRipRouteRedistEntry": agentRipRouteRedistEntry,
       "agentRipRouteRedistSource": agentRipRouteRedistSource,
       "agentRipRouteRedistMode": agentRipRouteRedistMode,
       "agentRipRouteRedistMetric": agentRipRouteRedistMetric,
       "agentRipRouteRedistMetricConfigured": agentRipRouteRedistMetricConfigured,
       "agentRipRouteRedistMatchInternal": agentRipRouteRedistMatchInternal,
       "agentRipRouteRedistMatchExternal1": agentRipRouteRedistMatchExternal1,
       "agentRipRouteRedistMatchExternal2": agentRipRouteRedistMatchExternal2,
       "agentRipRouteRedistMatchNSSAExternal1": agentRipRouteRedistMatchNSSAExternal1,
       "agentRipRouteRedistMatchNSSAExternal2": agentRipRouteRedistMatchNSSAExternal2,
       "agentRipRouteRedistDistList": agentRipRouteRedistDistList,
       "agentRipRouteRedistDistListConfigured": agentRipRouteRedistDistListConfigured,
       "agentRip2IfConfTable": agentRip2IfConfTable,
       "agentRip2IfConfEntry": agentRip2IfConfEntry,
       "agentRip2IfConfAuthKeyId": agentRip2IfConfAuthKeyId,
       "agentRouterRipRoutePref": agentRouterRipRoutePref,
       "agentRouterOspfConfigGroup": agentRouterOspfConfigGroup,
       "agentOspfDefaultMetric": agentOspfDefaultMetric,
       "agentOspfDefaultMetricConfigured": agentOspfDefaultMetricConfigured,
       "agentOspfDefaultInfoOriginate": agentOspfDefaultInfoOriginate,
       "agentOspfDefaultInfoOriginateAlways": agentOspfDefaultInfoOriginateAlways,
       "agentOspfDefaultInfoOriginateMetric": agentOspfDefaultInfoOriginateMetric,
       "agentOspfDefaultInfoOriginateMetricConfigured": agentOspfDefaultInfoOriginateMetricConfigured,
       "agentOspfDefaultInfoOriginateMetricType": agentOspfDefaultInfoOriginateMetricType,
       "agentOspfRouteRedistTable": agentOspfRouteRedistTable,
       "agentOspfRouteRedistEntry": agentOspfRouteRedistEntry,
       "agentOspfRouteRedistSource": agentOspfRouteRedistSource,
       "agentOspfRouteRedistMode": agentOspfRouteRedistMode,
       "agentOspfRouteRedistMetric": agentOspfRouteRedistMetric,
       "agentOspfRouteRedistMetricConfigured": agentOspfRouteRedistMetricConfigured,
       "agentOspfRouteRedistMetricType": agentOspfRouteRedistMetricType,
       "agentOspfRouteRedistTag": agentOspfRouteRedistTag,
       "agentOspfRouteRedistSubnets": agentOspfRouteRedistSubnets,
       "agentOspfRouteRedistDistList": agentOspfRouteRedistDistList,
       "agentOspfRouteRedistDistListConfigured": agentOspfRouteRedistDistListConfigured,
       "agentOspfIfTable": agentOspfIfTable,
       "agentOspfIfEntry": agentOspfIfEntry,
       "agentOspfIfAuthKeyId": agentOspfIfAuthKeyId,
       "agentOspfIfIpMtuIgnoreFlag": agentOspfIfIpMtuIgnoreFlag,
       "agentOspfIfPassiveMode": agentOspfIfPassiveMode,
       "agentOspfIfAdvertiseSecondaries": agentOspfIfAdvertiseSecondaries,
       "agentOspfVirtIfTable": agentOspfVirtIfTable,
       "agentOspfVirtIfEntry": agentOspfVirtIfEntry,
       "agentOspfVirtIfAuthKeyId": agentOspfVirtIfAuthKeyId,
       "agentRouterOspfRFC1583CompatibilityMode": agentRouterOspfRFC1583CompatibilityMode,
       "agentOspfSpfDelayTime": agentOspfSpfDelayTime,
       "agentOspfSpfHoldTime": agentOspfSpfHoldTime,
       "agentOspfAutoCostRefBw": agentOspfAutoCostRefBw,
       "agentOspfOpaqueLsaSupport": agentOspfOpaqueLsaSupport,
       "agentOspfAreaOpaqueLsdbTable": agentOspfAreaOpaqueLsdbTable,
       "agentOspfAreaOpaqueLsdbEntry": agentOspfAreaOpaqueLsdbEntry,
       "agentOspfAreaOpaqueLsdbAreaId": agentOspfAreaOpaqueLsdbAreaId,
       "agentOspfAreaOpaqueLsdbType": agentOspfAreaOpaqueLsdbType,
       "agentOspfAreaOpaqueLsdbLsid": agentOspfAreaOpaqueLsdbLsid,
       "agentOspfAreaOpaqueLsdbRouterId": agentOspfAreaOpaqueLsdbRouterId,
       "agentOspfAreaOpaqueLsdbSequence": agentOspfAreaOpaqueLsdbSequence,
       "agentOspfAreaOpaqueLsdbAge": agentOspfAreaOpaqueLsdbAge,
       "agentOspfAreaOpaqueLsdbChecksum": agentOspfAreaOpaqueLsdbChecksum,
       "agentOspfAreaOpaqueLsdbAdvertisement": agentOspfAreaOpaqueLsdbAdvertisement,
       "agentOspfLocalLsdbTable": agentOspfLocalLsdbTable,
       "agentOspfLocalLsdbEntry": agentOspfLocalLsdbEntry,
       "agentOspfLocalLsdbIpAddress": agentOspfLocalLsdbIpAddress,
       "agentOspfLocalLsdbAddressLessIf": agentOspfLocalLsdbAddressLessIf,
       "agentOspfLocalLsdbType": agentOspfLocalLsdbType,
       "agentOspfLocalLsdbLsid": agentOspfLocalLsdbLsid,
       "agentOspfLocalLsdbRouterId": agentOspfLocalLsdbRouterId,
       "agentOspfLocalLsdbSequence": agentOspfLocalLsdbSequence,
       "agentOspfLocalLsdbAge": agentOspfLocalLsdbAge,
       "agentOspfLocalLsdbChecksum": agentOspfLocalLsdbChecksum,
       "agentOspfLocalLsdbAdvertisement": agentOspfLocalLsdbAdvertisement,
       "agentOspfAsLsdbTable": agentOspfAsLsdbTable,
       "agentOspfAsLsdbEntry": agentOspfAsLsdbEntry,
       "agentOspfAsLsdbType": agentOspfAsLsdbType,
       "agentOspfAsLsdbLsid": agentOspfAsLsdbLsid,
       "agentOspfAsLsdbRouterId": agentOspfAsLsdbRouterId,
       "agentOspfAsLsdbSequence": agentOspfAsLsdbSequence,
       "agentOspfAsLsdbAge": agentOspfAsLsdbAge,
       "agentOspfAsLsdbChecksum": agentOspfAsLsdbChecksum,
       "agentOspfAsLsdbAdvertisement": agentOspfAsLsdbAdvertisement,
       "agentOspfDefaultPassiveMode": agentOspfDefaultPassiveMode,
       "agentOspfRoutePrefIntraArea": agentOspfRoutePrefIntraArea,
       "agentOspfRoutePrefInterArea": agentOspfRoutePrefInterArea,
       "agentOspfRoutePrefExternal": agentOspfRoutePrefExternal,
       "agentSnmpTrapFlagsConfigGroupLayer3": agentSnmpTrapFlagsConfigGroupLayer3,
       "agentSnmpVRRPNewMasterTrapFlag": agentSnmpVRRPNewMasterTrapFlag,
       "agentSnmpVRRPAuthFailureTrapFlag": agentSnmpVRRPAuthFailureTrapFlag,
       "agentBootpDhcpRelayGroup": agentBootpDhcpRelayGroup,
       "agentBootpDhcpRelayMaxHopCount": agentBootpDhcpRelayMaxHopCount,
       "agentBootpDhcpRelayForwardingIp": agentBootpDhcpRelayForwardingIp,
       "agentBootpDhcpRelayForwardMode": agentBootpDhcpRelayForwardMode,
       "agentBootpDhcpRelayMinWaitTime": agentBootpDhcpRelayMinWaitTime,
       "agentBootpDhcpRelayCircuitIdOptionMode": agentBootpDhcpRelayCircuitIdOptionMode,
       "agentBootpDhcpRelayNumOfRequestsReceived": agentBootpDhcpRelayNumOfRequestsReceived,
       "agentBootpDhcpRelayNumOfRequestsForwarded": agentBootpDhcpRelayNumOfRequestsForwarded,
       "agentBootpDhcpRelayNumOfDiscards": agentBootpDhcpRelayNumOfDiscards,
       "agentECMPGroup": agentECMPGroup,
       "agentECMPOspfMaxPaths": agentECMPOspfMaxPaths,
       "agentRouterVrrpConfigGroup": agentRouterVrrpConfigGroup,
       "agentRouterVrrpAdminState": agentRouterVrrpAdminState,
       "agentRouterVrrpConfiguredTable": agentRouterVrrpConfiguredTable,
       "agentRouterVrrpConfiguredEntry": agentRouterVrrpConfiguredEntry,
       "agentRouterVrrpConfiguredPriority": agentRouterVrrpConfiguredPriority,
       "agentVrrpOperations": agentVrrpOperations,
       "agentRouterVrrpOperTable": agentRouterVrrpOperTable,
       "agentRouterVrrpOperEntry": agentRouterVrrpOperEntry,
       "agentRouterVrrpOperPriority": agentRouterVrrpOperPriority,
       "agentRouterVrrpTrackGroup": agentRouterVrrpTrackGroup,
       "agentRouterVrrpTrackIntfTable": agentRouterVrrpTrackIntfTable,
       "agentRouterVrrpTrackIntfEntry": agentRouterVrrpTrackIntfEntry,
       "agentRouterVrrpTrackIntf": agentRouterVrrpTrackIntf,
       "agentRouterVrrpTrackIfPrioDec": agentRouterVrrpTrackIfPrioDec,
       "agentRouterVrrpTrackIfState": agentRouterVrrpTrackIfState,
       "agentRouterVrrpTrackIfStatus": agentRouterVrrpTrackIfStatus,
       "agentRouterVrrpTrackRouteTable": agentRouterVrrpTrackRouteTable,
       "agentRouterVrrpTrackRouteEntry": agentRouterVrrpTrackRouteEntry,
       "agentRouterVrrpTrackRtPfx": agentRouterVrrpTrackRtPfx,
       "agentRouterVrrpTrackRtPfxLen": agentRouterVrrpTrackRtPfxLen,
       "agentRouterVrrpTrackRtPrioDec": agentRouterVrrpTrackRtPrioDec,
       "agentRouterVrrpTrackRtReachable": agentRouterVrrpTrackRtReachable,
       "agentRouterVrrpTrackRtStatus": agentRouterVrrpTrackRtStatus,
       "agentIpHelperGroup": agentIpHelperGroup,
       "agentIpHelperAdminMode": agentIpHelperAdminMode,
       "agentDhcpClientMsgsReceived": agentDhcpClientMsgsReceived,
       "agentDhcpClientMsgsRelayed": agentDhcpClientMsgsRelayed,
       "agentDhcpServerMsgsReceived": agentDhcpServerMsgsReceived,
       "agentDhcpServerMsgsRelayed": agentDhcpServerMsgsRelayed,
       "agentUdpClientMsgsReceived": agentUdpClientMsgsReceived,
       "agentUdpClientMsgsRelayed": agentUdpClientMsgsRelayed,
       "agentSwitchIpHelperAddressTable": agentSwitchIpHelperAddressTable,
       "agentSwitchIpHelperAddressEntry": agentSwitchIpHelperAddressEntry,
       "agentSwitchIpHelperAddress": agentSwitchIpHelperAddress,
       "agentSwitchIpHelperUdpPort": agentSwitchIpHelperUdpPort,
       "agentSwitchIpHelperHitCount": agentSwitchIpHelperHitCount,
       "agentSwitchIpHelperStatus": agentSwitchIpHelperStatus,
       "agentUdpClientMsgsTtlExpired": agentUdpClientMsgsTtlExpired,
       "agentUdpClientMsgsDiscarded": agentUdpClientMsgsDiscarded,
       "agentInternalVlanGroup": agentInternalVlanGroup,
       "agentInternalVlanBase": agentInternalVlanBase,
       "agentInternalVlanPolicy": agentInternalVlanPolicy,
       "agentSwitchInternalVlanTable": agentSwitchInternalVlanTable,
       "agentSwitchInternalVlanEntry": agentSwitchInternalVlanEntry,
       "agentSwitchInternalVlanId": agentSwitchInternalVlanId,
       "agentSwitchInternalVlanIfIndex": agentSwitchInternalVlanIfIndex,
       "agentOspfQueueGroup": agentOspfQueueGroup,
       "agentOspfQueueTable": agentOspfQueueTable,
       "agentOspfQueueEntry": agentOspfQueueEntry,
       "agentOspfQueueIndex": agentOspfQueueIndex,
       "agentOspfQueueName": agentOspfQueueName,
       "agentOspfQueueLength": agentOspfQueueLength,
       "agentOspfQueueHigh": agentOspfQueueHigh,
       "agentOspfQueueDrops": agentOspfQueueDrops,
       "agentOspfQueueLimit": agentOspfQueueLimit,
       "agentOspfPacketStatsGroup": agentOspfPacketStatsGroup,
       "agentOspfCountersCleared": agentOspfCountersCleared,
       "agentOspfLsaRetxCount": agentOspfLsaRetxCount,
       "agentOspfHellosRx": agentOspfHellosRx,
       "agentOspfHellosTx": agentOspfHellosTx,
       "agentOspfDdRx": agentOspfDdRx,
       "agentOspfDdTx": agentOspfDdTx,
       "agentOspfLsReqRx": agentOspfLsReqRx,
       "agentOspfLsReqTx": agentOspfLsReqTx,
       "agentOspfLsUpdatesRx": agentOspfLsUpdatesRx,
       "agentOspfLsUpdatesTx": agentOspfLsUpdatesTx,
       "agentOspfLsAckRx": agentOspfLsAckRx,
       "agentOspfLsAckTx": agentOspfLsAckTx,
       "agentOspfLsUpdatesRxMax": agentOspfLsUpdatesRxMax,
       "agentOspfLsUpdatesTxMax": agentOspfLsUpdatesTxMax,
       "agentOspfType1LsasRx": agentOspfType1LsasRx,
       "agentOspfType2LsasRx": agentOspfType2LsasRx,
       "agentOspfType3LsasRx": agentOspfType3LsasRx,
       "agentOspfType4LsasRx": agentOspfType4LsasRx,
       "agentOspfType5LsasRx": agentOspfType5LsasRx,
       "agentOspfType7LsasRx": agentOspfType7LsasRx,
       "agentOspfType9LsasRx": agentOspfType9LsasRx,
       "agentOspfType10LsasRx": agentOspfType10LsasRx,
       "agentOspfType11LsasRx": agentOspfType11LsasRx,
       "agentOspfSpfStatsTable": agentOspfSpfStatsTable,
       "agentOspfSpfStatsEntry": agentOspfSpfStatsEntry,
       "agentOspfSpfIndex": agentOspfSpfIndex,
       "agentOspfSpfStatsDeltaT": agentOspfSpfStatsDeltaT,
       "agentOspfSpfStatsIntra": agentOspfSpfStatsIntra,
       "agentOspfSpfStatsSumm": agentOspfSpfStatsSumm,
       "agentOspfSpfStatsExt": agentOspfSpfStatsExt,
       "agentOspfSpfStatsSpfTotal": agentOspfSpfStatsSpfTotal,
       "agentOspfSpfStatsRibUpdate": agentOspfSpfStatsRibUpdate,
       "agentOspfSpfStatsReason": agentOspfSpfStatsReason,
       "agentRoutingHeapGroup": agentRoutingHeapGroup,
       "agentRoutingHeapSize": agentRoutingHeapSize,
       "agentRoutingHeapInUse": agentRoutingHeapInUse,
       "agentRoutingHeapHigh": agentRoutingHeapHigh,
       "agentRoutingTableSummaryGroup": agentRoutingTableSummaryGroup,
       "agentConnectedRoutes": agentConnectedRoutes,
       "agentStaticRoutes": agentStaticRoutes,
       "agentRipRoutes": agentRipRoutes,
       "agentOspfRoutes": agentOspfRoutes,
       "agentOspfIntraRoutes": agentOspfIntraRoutes,
       "agentOspfInterRoutes": agentOspfInterRoutes,
       "agentOspfExt1Routes": agentOspfExt1Routes,
       "agentOspfExt2Routes": agentOspfExt2Routes,
       "agentBgpRoutes": agentBgpRoutes,
       "agentEbgpRoutes": agentEbgpRoutes,
       "agentIbgpRoutes": agentIbgpRoutes,
       "agentLocalBgpRoutes": agentLocalBgpRoutes,
       "agentRejectRoutes": agentRejectRoutes,
       "agentTotalRoutes": agentTotalRoutes,
       "agentBestRoutes": agentBestRoutes,
       "agentBestRoutesHigh": agentBestRoutesHigh,
       "agentAlternateRoutes": agentAlternateRoutes,
       "agentRouteAdds": agentRouteAdds,
       "agentRouteModifies": agentRouteModifies,
       "agentRouteDeletes": agentRouteDeletes,
       "agentUnresolvedRouteAdds": agentUnresolvedRouteAdds,
       "agentInvalidRouteAdds": agentInvalidRouteAdds,
       "agentFailedRouteAdds": agentFailedRouteAdds,
       "agentReservedLocals": agentReservedLocals,
       "agentUniqueNextHops": agentUniqueNextHops,
       "agentUniqueNextHopsHigh": agentUniqueNextHopsHigh,
       "agentNextHopGroups": agentNextHopGroups,
       "agentNextHopGroupsHigh": agentNextHopGroupsHigh,
       "agentEcmpGroups": agentEcmpGroups,
       "agentEcmpGroupsHigh": agentEcmpGroupsHigh,
       "agentEcmpRoutes": agentEcmpRoutes,
       "agentTruncEcmpRoutes": agentTruncEcmpRoutes,
       "agentEcmpRetries": agentEcmpRetries,
       "agentEcmpCountTable": agentEcmpCountTable,
       "agentEcmpCountEntry": agentEcmpCountEntry,
       "agentEcmpNextHopCount": agentEcmpNextHopCount,
       "agentEcmpRouteCount": agentEcmpRouteCount,
       "agentOspfStubRouterGroup": agentOspfStubRouterGroup,
       "ospfStubRouterAdvertisement": ospfStubRouterAdvertisement,
       "agentOspfStubRouterReason": agentOspfStubRouterReason,
       "agentOspfStubRouterStartupTimeRemaining": agentOspfStubRouterStartupTimeRemaining,
       "agentOspfStubRouterDuration": agentOspfStubRouterDuration}
)
