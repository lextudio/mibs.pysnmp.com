# SNMP MIB module (HIRSCHMANN-MMP4-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIRSCHMANN-MMP4-ROUTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:43 2024
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

(hmPlatform4,) = mibBuilder.importSymbols(
    "HIRSCHMANN-MMP4-BASICL2-MIB",
    "hmPlatform4")

(ospfIfEntry,
 ospfVirtIfEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
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


# MODULE-IDENTITY

hmPlatform4Routing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2)
)
hmPlatform4Routing.setRevisions(
        ("2005-08-18 12:00",
         "2003-04-02 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmAgentSwitchArpGroup_ObjectIdentity = ObjectIdentity
hmAgentSwitchArpGroup = _HmAgentSwitchArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1)
)


class _HmAgentSwitchArpAgeoutTime_Type(Integer32):
    """Custom type hmAgentSwitchArpAgeoutTime based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 21600),
    )


_HmAgentSwitchArpAgeoutTime_Type.__name__ = "Integer32"
_HmAgentSwitchArpAgeoutTime_Object = MibScalar
hmAgentSwitchArpAgeoutTime = _HmAgentSwitchArpAgeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 1),
    _HmAgentSwitchArpAgeoutTime_Type()
)
hmAgentSwitchArpAgeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchArpAgeoutTime.setStatus("current")


class _HmAgentSwitchArpResponseTime_Type(Integer32):
    """Custom type hmAgentSwitchArpResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HmAgentSwitchArpResponseTime_Type.__name__ = "Integer32"
_HmAgentSwitchArpResponseTime_Object = MibScalar
hmAgentSwitchArpResponseTime = _HmAgentSwitchArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 2),
    _HmAgentSwitchArpResponseTime_Type()
)
hmAgentSwitchArpResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchArpResponseTime.setStatus("current")


class _HmAgentSwitchArpMaxRetries_Type(Integer32):
    """Custom type hmAgentSwitchArpMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HmAgentSwitchArpMaxRetries_Type.__name__ = "Integer32"
_HmAgentSwitchArpMaxRetries_Object = MibScalar
hmAgentSwitchArpMaxRetries = _HmAgentSwitchArpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 3),
    _HmAgentSwitchArpMaxRetries_Type()
)
hmAgentSwitchArpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchArpMaxRetries.setStatus("current")
_HmAgentSwitchArpCacheSize_Type = Integer32
_HmAgentSwitchArpCacheSize_Object = MibScalar
hmAgentSwitchArpCacheSize = _HmAgentSwitchArpCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 4),
    _HmAgentSwitchArpCacheSize_Type()
)
hmAgentSwitchArpCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchArpCacheSize.setStatus("current")


class _HmAgentSwitchArpDynamicRenew_Type(Integer32):
    """Custom type hmAgentSwitchArpDynamicRenew based on Integer32"""
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


_HmAgentSwitchArpDynamicRenew_Type.__name__ = "Integer32"
_HmAgentSwitchArpDynamicRenew_Object = MibScalar
hmAgentSwitchArpDynamicRenew = _HmAgentSwitchArpDynamicRenew_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 5),
    _HmAgentSwitchArpDynamicRenew_Type()
)
hmAgentSwitchArpDynamicRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchArpDynamicRenew.setStatus("current")
_HmAgentSwitchArpTotalEntryCountCurrent_Type = Gauge32
_HmAgentSwitchArpTotalEntryCountCurrent_Object = MibScalar
hmAgentSwitchArpTotalEntryCountCurrent = _HmAgentSwitchArpTotalEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 6),
    _HmAgentSwitchArpTotalEntryCountCurrent_Type()
)
hmAgentSwitchArpTotalEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchArpTotalEntryCountCurrent.setStatus("current")
_HmAgentSwitchArpTotalEntryCountPeak_Type = Gauge32
_HmAgentSwitchArpTotalEntryCountPeak_Object = MibScalar
hmAgentSwitchArpTotalEntryCountPeak = _HmAgentSwitchArpTotalEntryCountPeak_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 7),
    _HmAgentSwitchArpTotalEntryCountPeak_Type()
)
hmAgentSwitchArpTotalEntryCountPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchArpTotalEntryCountPeak.setStatus("current")
_HmAgentSwitchArpStaticEntryCountCurrent_Type = Gauge32
_HmAgentSwitchArpStaticEntryCountCurrent_Object = MibScalar
hmAgentSwitchArpStaticEntryCountCurrent = _HmAgentSwitchArpStaticEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 8),
    _HmAgentSwitchArpStaticEntryCountCurrent_Type()
)
hmAgentSwitchArpStaticEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchArpStaticEntryCountCurrent.setStatus("current")
_HmAgentSwitchArpStaticEntryCountMax_Type = Integer32
_HmAgentSwitchArpStaticEntryCountMax_Object = MibScalar
hmAgentSwitchArpStaticEntryCountMax = _HmAgentSwitchArpStaticEntryCountMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 9),
    _HmAgentSwitchArpStaticEntryCountMax_Type()
)
hmAgentSwitchArpStaticEntryCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchArpStaticEntryCountMax.setStatus("current")
_HmAgentSwitchArpTable_Object = MibTable
hmAgentSwitchArpTable = _HmAgentSwitchArpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hmAgentSwitchArpTable.setStatus("current")
_HmAgentSwitchArpEntry_Object = MibTableRow
hmAgentSwitchArpEntry = _HmAgentSwitchArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 10, 1)
)
hmAgentSwitchArpEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchArpIpAddress"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchArpEntry.setStatus("current")
_HmAgentSwitchArpAge_Type = TimeTicks
_HmAgentSwitchArpAge_Object = MibTableColumn
hmAgentSwitchArpAge = _HmAgentSwitchArpAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 10, 1, 1),
    _HmAgentSwitchArpAge_Type()
)
hmAgentSwitchArpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchArpAge.setStatus("current")
_HmAgentSwitchArpIpAddress_Type = IpAddress
_HmAgentSwitchArpIpAddress_Object = MibTableColumn
hmAgentSwitchArpIpAddress = _HmAgentSwitchArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 10, 1, 2),
    _HmAgentSwitchArpIpAddress_Type()
)
hmAgentSwitchArpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchArpIpAddress.setStatus("current")
_HmAgentSwitchArpMacAddress_Type = MacAddress
_HmAgentSwitchArpMacAddress_Object = MibTableColumn
hmAgentSwitchArpMacAddress = _HmAgentSwitchArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 10, 1, 3),
    _HmAgentSwitchArpMacAddress_Type()
)
hmAgentSwitchArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentSwitchArpMacAddress.setStatus("current")
_HmAgentSwitchArpInterface_Type = Integer32
_HmAgentSwitchArpInterface_Object = MibTableColumn
hmAgentSwitchArpInterface = _HmAgentSwitchArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 10, 1, 4),
    _HmAgentSwitchArpInterface_Type()
)
hmAgentSwitchArpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchArpInterface.setStatus("current")


class _HmAgentSwitchArpType_Type(Integer32):
    """Custom type hmAgentSwitchArpType based on Integer32"""
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


_HmAgentSwitchArpType_Type.__name__ = "Integer32"
_HmAgentSwitchArpType_Object = MibTableColumn
hmAgentSwitchArpType = _HmAgentSwitchArpType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 10, 1, 5),
    _HmAgentSwitchArpType_Type()
)
hmAgentSwitchArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchArpType.setStatus("current")
_HmAgentSwitchArpStatus_Type = RowStatus
_HmAgentSwitchArpStatus_Object = MibTableColumn
hmAgentSwitchArpStatus = _HmAgentSwitchArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 10, 1, 6),
    _HmAgentSwitchArpStatus_Type()
)
hmAgentSwitchArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchArpStatus.setStatus("current")


class _HmAgentSwitchArpSparseLearn_Type(Integer32):
    """Custom type hmAgentSwitchArpSparseLearn based on Integer32"""
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


_HmAgentSwitchArpSparseLearn_Type.__name__ = "Integer32"
_HmAgentSwitchArpSparseLearn_Object = MibScalar
hmAgentSwitchArpSparseLearn = _HmAgentSwitchArpSparseLearn_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 1, 11),
    _HmAgentSwitchArpSparseLearn_Type()
)
hmAgentSwitchArpSparseLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchArpSparseLearn.setStatus("current")
_HmAgentSwitchIpGroup_ObjectIdentity = ObjectIdentity
hmAgentSwitchIpGroup = _HmAgentSwitchIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2)
)


class _HmAgentSwitchIpRoutingMode_Type(Integer32):
    """Custom type hmAgentSwitchIpRoutingMode based on Integer32"""
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


_HmAgentSwitchIpRoutingMode_Type.__name__ = "Integer32"
_HmAgentSwitchIpRoutingMode_Object = MibScalar
hmAgentSwitchIpRoutingMode = _HmAgentSwitchIpRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 1),
    _HmAgentSwitchIpRoutingMode_Type()
)
hmAgentSwitchIpRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRoutingMode.setStatus("current")


class _HmAgentSwitchIpVRRPMode_Type(Integer32):
    """Custom type hmAgentSwitchIpVRRPMode based on Integer32"""
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


_HmAgentSwitchIpVRRPMode_Type.__name__ = "Integer32"
_HmAgentSwitchIpVRRPMode_Object = MibScalar
hmAgentSwitchIpVRRPMode = _HmAgentSwitchIpVRRPMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 2),
    _HmAgentSwitchIpVRRPMode_Type()
)
hmAgentSwitchIpVRRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpVRRPMode.setStatus("current")
_HmAgentSwitchIpInterfaceTable_Object = MibTable
hmAgentSwitchIpInterfaceTable = _HmAgentSwitchIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceTable.setStatus("current")
_HmAgentSwitchIpInterfaceEntry_Object = MibTableRow
hmAgentSwitchIpInterfaceEntry = _HmAgentSwitchIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1)
)
hmAgentSwitchIpInterfaceEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchIpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceEntry.setStatus("current")
_HmAgentSwitchIpInterfaceIfIndex_Type = Integer32
_HmAgentSwitchIpInterfaceIfIndex_Object = MibTableColumn
hmAgentSwitchIpInterfaceIfIndex = _HmAgentSwitchIpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 1),
    _HmAgentSwitchIpInterfaceIfIndex_Type()
)
hmAgentSwitchIpInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceIfIndex.setStatus("current")
_HmAgentSwitchIpInterfaceIpAddress_Type = IpAddress
_HmAgentSwitchIpInterfaceIpAddress_Object = MibTableColumn
hmAgentSwitchIpInterfaceIpAddress = _HmAgentSwitchIpInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 2),
    _HmAgentSwitchIpInterfaceIpAddress_Type()
)
hmAgentSwitchIpInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceIpAddress.setStatus("current")
_HmAgentSwitchIpInterfaceNetMask_Type = IpAddress
_HmAgentSwitchIpInterfaceNetMask_Object = MibTableColumn
hmAgentSwitchIpInterfaceNetMask = _HmAgentSwitchIpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 3),
    _HmAgentSwitchIpInterfaceNetMask_Type()
)
hmAgentSwitchIpInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceNetMask.setStatus("current")


class _HmAgentSwitchIpInterfaceClearIp_Type(Integer32):
    """Custom type hmAgentSwitchIpInterfaceClearIp based on Integer32"""
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


_HmAgentSwitchIpInterfaceClearIp_Type.__name__ = "Integer32"
_HmAgentSwitchIpInterfaceClearIp_Object = MibTableColumn
hmAgentSwitchIpInterfaceClearIp = _HmAgentSwitchIpInterfaceClearIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 4),
    _HmAgentSwitchIpInterfaceClearIp_Type()
)
hmAgentSwitchIpInterfaceClearIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceClearIp.setStatus("current")


class _HmAgentSwitchIpInterfaceRoutingMode_Type(Integer32):
    """Custom type hmAgentSwitchIpInterfaceRoutingMode based on Integer32"""
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


_HmAgentSwitchIpInterfaceRoutingMode_Type.__name__ = "Integer32"
_HmAgentSwitchIpInterfaceRoutingMode_Object = MibTableColumn
hmAgentSwitchIpInterfaceRoutingMode = _HmAgentSwitchIpInterfaceRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 5),
    _HmAgentSwitchIpInterfaceRoutingMode_Type()
)
hmAgentSwitchIpInterfaceRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceRoutingMode.setStatus("current")


class _HmAgentSwitchIpInterfaceProxyARPMode_Type(Integer32):
    """Custom type hmAgentSwitchIpInterfaceProxyARPMode based on Integer32"""
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


_HmAgentSwitchIpInterfaceProxyARPMode_Type.__name__ = "Integer32"
_HmAgentSwitchIpInterfaceProxyARPMode_Object = MibTableColumn
hmAgentSwitchIpInterfaceProxyARPMode = _HmAgentSwitchIpInterfaceProxyARPMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 6),
    _HmAgentSwitchIpInterfaceProxyARPMode_Type()
)
hmAgentSwitchIpInterfaceProxyARPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceProxyARPMode.setStatus("current")


class _HmAgentSwitchIpInterfaceMtuValue_Type(Unsigned32):
    """Custom type hmAgentSwitchIpInterfaceMtuValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(68, 9000),
    )


_HmAgentSwitchIpInterfaceMtuValue_Type.__name__ = "Unsigned32"
_HmAgentSwitchIpInterfaceMtuValue_Object = MibTableColumn
hmAgentSwitchIpInterfaceMtuValue = _HmAgentSwitchIpInterfaceMtuValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 7),
    _HmAgentSwitchIpInterfaceMtuValue_Type()
)
hmAgentSwitchIpInterfaceMtuValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceMtuValue.setStatus("current")
_HmAgentSwitchIpInterfaceSlotNum_Type = Integer32
_HmAgentSwitchIpInterfaceSlotNum_Object = MibTableColumn
hmAgentSwitchIpInterfaceSlotNum = _HmAgentSwitchIpInterfaceSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 8),
    _HmAgentSwitchIpInterfaceSlotNum_Type()
)
hmAgentSwitchIpInterfaceSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceSlotNum.setStatus("current")
_HmAgentSwitchIpInterfacePortNum_Type = Integer32
_HmAgentSwitchIpInterfacePortNum_Object = MibTableColumn
hmAgentSwitchIpInterfacePortNum = _HmAgentSwitchIpInterfacePortNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 9),
    _HmAgentSwitchIpInterfacePortNum_Type()
)
hmAgentSwitchIpInterfacePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfacePortNum.setStatus("current")


class _HmAgentSwitchIpInterfaceNetdirectedBCMode_Type(Integer32):
    """Custom type hmAgentSwitchIpInterfaceNetdirectedBCMode based on Integer32"""
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


_HmAgentSwitchIpInterfaceNetdirectedBCMode_Type.__name__ = "Integer32"
_HmAgentSwitchIpInterfaceNetdirectedBCMode_Object = MibTableColumn
hmAgentSwitchIpInterfaceNetdirectedBCMode = _HmAgentSwitchIpInterfaceNetdirectedBCMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 3, 1, 10),
    _HmAgentSwitchIpInterfaceNetdirectedBCMode_Type()
)
hmAgentSwitchIpInterfaceNetdirectedBCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpInterfaceNetdirectedBCMode.setStatus("current")
_HmAgentSwitchIpRouterDiscoveryTable_Object = MibTable
hmAgentSwitchIpRouterDiscoveryTable = _HmAgentSwitchIpRouterDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouterDiscoveryTable.setStatus("current")
_HmAgentSwitchIpRouterDiscoveryEntry_Object = MibTableRow
hmAgentSwitchIpRouterDiscoveryEntry = _HmAgentSwitchIpRouterDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 4, 1)
)
hmAgentSwitchIpRouterDiscoveryEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchIpRouterDiscoveryIfIndex"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouterDiscoveryEntry.setStatus("current")
_HmAgentSwitchIpRouterDiscoveryIfIndex_Type = Integer32
_HmAgentSwitchIpRouterDiscoveryIfIndex_Object = MibTableColumn
hmAgentSwitchIpRouterDiscoveryIfIndex = _HmAgentSwitchIpRouterDiscoveryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 4, 1, 1),
    _HmAgentSwitchIpRouterDiscoveryIfIndex_Type()
)
hmAgentSwitchIpRouterDiscoveryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouterDiscoveryIfIndex.setStatus("current")


class _HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Type(Integer32):
    """Custom type hmAgentSwitchIpRouterDiscoveryAdvertiseMode based on Integer32"""
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


_HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Type.__name__ = "Integer32"
_HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Object = MibTableColumn
hmAgentSwitchIpRouterDiscoveryAdvertiseMode = _HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 4, 1, 2),
    _HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Type()
)
hmAgentSwitchIpRouterDiscoveryAdvertiseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouterDiscoveryAdvertiseMode.setStatus("current")


class _HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):
    """Custom type hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__ = "Integer32"
_HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object = MibTableColumn
hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval = _HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 4, 1, 3),
    _HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type()
)
hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setStatus("current")


class _HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):
    """Custom type hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval based on Integer32"""
    defaultValue = 450

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type.__name__ = "Integer32"
_HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object = MibTableColumn
hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval = _HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 4, 1, 4),
    _HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type()
)
hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval.setStatus("current")


class _HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):
    """Custom type hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type.__name__ = "Integer32"
_HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object = MibTableColumn
hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime = _HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 4, 1, 5),
    _HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type()
)
hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime.setStatus("current")


class _HmAgentSwitchIpRouterDiscoveryPreferenceLevel_Type(Integer32):
    """Custom type hmAgentSwitchIpRouterDiscoveryPreferenceLevel based on Integer32"""
    defaultValue = 0


_HmAgentSwitchIpRouterDiscoveryPreferenceLevel_Object = MibTableColumn
hmAgentSwitchIpRouterDiscoveryPreferenceLevel = _HmAgentSwitchIpRouterDiscoveryPreferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 4, 1, 6),
    _HmAgentSwitchIpRouterDiscoveryPreferenceLevel_Type()
)
hmAgentSwitchIpRouterDiscoveryPreferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouterDiscoveryPreferenceLevel.setStatus("current")


class _HmAgentSwitchIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):
    """Custom type hmAgentSwitchIpRouterDiscoveryAdvertisementAddress based on IpAddress"""
    defaultHexValue = "E0000001"


_HmAgentSwitchIpRouterDiscoveryAdvertisementAddress_Object = MibTableColumn
hmAgentSwitchIpRouterDiscoveryAdvertisementAddress = _HmAgentSwitchIpRouterDiscoveryAdvertisementAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 4, 1, 7),
    _HmAgentSwitchIpRouterDiscoveryAdvertisementAddress_Type()
)
hmAgentSwitchIpRouterDiscoveryAdvertisementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouterDiscoveryAdvertisementAddress.setStatus("current")
_HmAgentSwitchIpVlanTable_Object = MibTable
hmAgentSwitchIpVlanTable = _HmAgentSwitchIpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpVlanTable.setStatus("current")
_HmAgentSwitchIpVlanEntry_Object = MibTableRow
hmAgentSwitchIpVlanEntry = _HmAgentSwitchIpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 5, 1)
)
hmAgentSwitchIpVlanEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchIpVlanId"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpVlanEntry.setStatus("current")
_HmAgentSwitchIpVlanId_Type = Integer32
_HmAgentSwitchIpVlanId_Object = MibTableColumn
hmAgentSwitchIpVlanId = _HmAgentSwitchIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 5, 1, 1),
    _HmAgentSwitchIpVlanId_Type()
)
hmAgentSwitchIpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpVlanId.setStatus("current")
_HmAgentSwitchIpVlanIfIndex_Type = Integer32
_HmAgentSwitchIpVlanIfIndex_Object = MibTableColumn
hmAgentSwitchIpVlanIfIndex = _HmAgentSwitchIpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 5, 1, 2),
    _HmAgentSwitchIpVlanIfIndex_Type()
)
hmAgentSwitchIpVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpVlanIfIndex.setStatus("current")
_HmAgentSwitchIpVlanRoutingStatus_Type = RowStatus
_HmAgentSwitchIpVlanRoutingStatus_Object = MibTableColumn
hmAgentSwitchIpVlanRoutingStatus = _HmAgentSwitchIpVlanRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 5, 1, 3),
    _HmAgentSwitchIpVlanRoutingStatus_Type()
)
hmAgentSwitchIpVlanRoutingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentSwitchIpVlanRoutingStatus.setStatus("current")
_HmAgentSwitchSecondaryAddressTable_Object = MibTable
hmAgentSwitchSecondaryAddressTable = _HmAgentSwitchSecondaryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hmAgentSwitchSecondaryAddressTable.setStatus("current")
_HmAgentSwitchSecondaryAddressEntry_Object = MibTableRow
hmAgentSwitchSecondaryAddressEntry = _HmAgentSwitchSecondaryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 6, 1)
)
hmAgentSwitchSecondaryAddressEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchIpInterfaceIfIndex"),
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchSecondaryIpAddress"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchSecondaryAddressEntry.setStatus("current")
_HmAgentSwitchSecondaryIpAddress_Type = IpAddress
_HmAgentSwitchSecondaryIpAddress_Object = MibTableColumn
hmAgentSwitchSecondaryIpAddress = _HmAgentSwitchSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 6, 1, 1),
    _HmAgentSwitchSecondaryIpAddress_Type()
)
hmAgentSwitchSecondaryIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentSwitchSecondaryIpAddress.setStatus("current")
_HmAgentSwitchSecondaryNetMask_Type = IpAddress
_HmAgentSwitchSecondaryNetMask_Object = MibTableColumn
hmAgentSwitchSecondaryNetMask = _HmAgentSwitchSecondaryNetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 6, 1, 2),
    _HmAgentSwitchSecondaryNetMask_Type()
)
hmAgentSwitchSecondaryNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentSwitchSecondaryNetMask.setStatus("current")
_HmAgentSwitchSecondaryStatus_Type = RowStatus
_HmAgentSwitchSecondaryStatus_Object = MibTableColumn
hmAgentSwitchSecondaryStatus = _HmAgentSwitchSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 6, 1, 3),
    _HmAgentSwitchSecondaryStatus_Type()
)
hmAgentSwitchSecondaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentSwitchSecondaryStatus.setStatus("current")
_HmAgentSwitchIpRoutePreferenceTable_Object = MibTable
hmAgentSwitchIpRoutePreferenceTable = _HmAgentSwitchIpRoutePreferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpRoutePreferenceTable.setStatus("current")
_HmAgentSwitchIpRoutePreferenceEntry_Object = MibTableRow
hmAgentSwitchIpRoutePreferenceEntry = _HmAgentSwitchIpRoutePreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 7, 1)
)
hmAgentSwitchIpRoutePreferenceEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchIpRoutePreferenceSource"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpRoutePreferenceEntry.setStatus("current")


class _HmAgentSwitchIpRoutePreferenceSource_Type(Integer32):
    """Custom type hmAgentSwitchIpRoutePreferenceSource based on Integer32"""
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
        *(("connected", 1),
          ("ospf-ext-t1", 5),
          ("ospf-ext-t2", 6),
          ("ospf-inter", 4),
          ("ospf-intra", 3),
          ("rip", 7),
          ("static", 2))
    )


_HmAgentSwitchIpRoutePreferenceSource_Type.__name__ = "Integer32"
_HmAgentSwitchIpRoutePreferenceSource_Object = MibTableColumn
hmAgentSwitchIpRoutePreferenceSource = _HmAgentSwitchIpRoutePreferenceSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 7, 1, 1),
    _HmAgentSwitchIpRoutePreferenceSource_Type()
)
hmAgentSwitchIpRoutePreferenceSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRoutePreferenceSource.setStatus("current")


class _HmAgentSwitchIpRoutePreferenceValue_Type(Integer32):
    """Custom type hmAgentSwitchIpRoutePreferenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmAgentSwitchIpRoutePreferenceValue_Type.__name__ = "Integer32"
_HmAgentSwitchIpRoutePreferenceValue_Object = MibTableColumn
hmAgentSwitchIpRoutePreferenceValue = _HmAgentSwitchIpRoutePreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 7, 1, 2),
    _HmAgentSwitchIpRoutePreferenceValue_Type()
)
hmAgentSwitchIpRoutePreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRoutePreferenceValue.setStatus("current")
_HmAgentSwitchIpRouteStaticTable_Object = MibTable
hmAgentSwitchIpRouteStaticTable = _HmAgentSwitchIpRouteStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouteStaticTable.setStatus("current")
_HmAgentSwitchIpRouteStaticEntry_Object = MibTableRow
hmAgentSwitchIpRouteStaticEntry = _HmAgentSwitchIpRouteStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 8, 1)
)
hmAgentSwitchIpRouteStaticEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchIpRouteStaticDestination"),
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchIpRouteStaticDestinationMask"),
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentSwitchIpRouteStaticNextHop"),
)
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouteStaticEntry.setStatus("current")
_HmAgentSwitchIpRouteStaticDestination_Type = IpAddress
_HmAgentSwitchIpRouteStaticDestination_Object = MibTableColumn
hmAgentSwitchIpRouteStaticDestination = _HmAgentSwitchIpRouteStaticDestination_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 8, 1, 1),
    _HmAgentSwitchIpRouteStaticDestination_Type()
)
hmAgentSwitchIpRouteStaticDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouteStaticDestination.setStatus("current")
_HmAgentSwitchIpRouteStaticDestinationMask_Type = IpAddress
_HmAgentSwitchIpRouteStaticDestinationMask_Object = MibTableColumn
hmAgentSwitchIpRouteStaticDestinationMask = _HmAgentSwitchIpRouteStaticDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 8, 1, 2),
    _HmAgentSwitchIpRouteStaticDestinationMask_Type()
)
hmAgentSwitchIpRouteStaticDestinationMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouteStaticDestinationMask.setStatus("current")
_HmAgentSwitchIpRouteStaticNextHop_Type = IpAddress
_HmAgentSwitchIpRouteStaticNextHop_Object = MibTableColumn
hmAgentSwitchIpRouteStaticNextHop = _HmAgentSwitchIpRouteStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 8, 1, 3),
    _HmAgentSwitchIpRouteStaticNextHop_Type()
)
hmAgentSwitchIpRouteStaticNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouteStaticNextHop.setStatus("current")


class _HmAgentSwitchIpRouteStaticPreference_Type(Integer32):
    """Custom type hmAgentSwitchIpRouteStaticPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmAgentSwitchIpRouteStaticPreference_Type.__name__ = "Integer32"
_HmAgentSwitchIpRouteStaticPreference_Object = MibTableColumn
hmAgentSwitchIpRouteStaticPreference = _HmAgentSwitchIpRouteStaticPreference_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 8, 1, 4),
    _HmAgentSwitchIpRouteStaticPreference_Type()
)
hmAgentSwitchIpRouteStaticPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouteStaticPreference.setStatus("current")
_HmAgentSwitchIpRouteStaticStatus_Type = RowStatus
_HmAgentSwitchIpRouteStaticStatus_Object = MibTableColumn
hmAgentSwitchIpRouteStaticStatus = _HmAgentSwitchIpRouteStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 8, 1, 5),
    _HmAgentSwitchIpRouteStaticStatus_Type()
)
hmAgentSwitchIpRouteStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouteStaticStatus.setStatus("current")


class _HmAgentSwitchIpRouteStaticTrackId_Type(Integer32):
    """Custom type hmAgentSwitchIpRouteStaticTrackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmAgentSwitchIpRouteStaticTrackId_Type.__name__ = "Integer32"
_HmAgentSwitchIpRouteStaticTrackId_Object = MibTableColumn
hmAgentSwitchIpRouteStaticTrackId = _HmAgentSwitchIpRouteStaticTrackId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 8, 1, 6),
    _HmAgentSwitchIpRouteStaticTrackId_Type()
)
hmAgentSwitchIpRouteStaticTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpRouteStaticTrackId.setStatus("current")


class _HmAgentSwitchIpVlanSingleMacMode_Type(Integer32):
    """Custom type hmAgentSwitchIpVlanSingleMacMode based on Integer32"""
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


_HmAgentSwitchIpVlanSingleMacMode_Type.__name__ = "Integer32"
_HmAgentSwitchIpVlanSingleMacMode_Object = MibScalar
hmAgentSwitchIpVlanSingleMacMode = _HmAgentSwitchIpVlanSingleMacMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 100),
    _HmAgentSwitchIpVlanSingleMacMode_Type()
)
hmAgentSwitchIpVlanSingleMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpVlanSingleMacMode.setStatus("current")
_HmAgentSwitchIpTableSizesGroup_ObjectIdentity = ObjectIdentity
hmAgentSwitchIpTableSizesGroup = _HmAgentSwitchIpTableSizesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 101)
)


class _HmAgentSwitchIpTableSizeArp_Type(Integer32):
    """Custom type hmAgentSwitchIpTableSizeArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 4096),
    )


_HmAgentSwitchIpTableSizeArp_Type.__name__ = "Integer32"
_HmAgentSwitchIpTableSizeArp_Object = MibScalar
hmAgentSwitchIpTableSizeArp = _HmAgentSwitchIpTableSizeArp_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 101, 1),
    _HmAgentSwitchIpTableSizeArp_Type()
)
hmAgentSwitchIpTableSizeArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpTableSizeArp.setStatus("current")


class _HmAgentSwitchIpTableSizeUCRoutes_Type(Integer32):
    """Custom type hmAgentSwitchIpTableSizeUCRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 4096),
    )


_HmAgentSwitchIpTableSizeUCRoutes_Type.__name__ = "Integer32"
_HmAgentSwitchIpTableSizeUCRoutes_Object = MibScalar
hmAgentSwitchIpTableSizeUCRoutes = _HmAgentSwitchIpTableSizeUCRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 101, 2),
    _HmAgentSwitchIpTableSizeUCRoutes_Type()
)
hmAgentSwitchIpTableSizeUCRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpTableSizeUCRoutes.setStatus("current")


class _HmAgentSwitchIpTableSizeMCRoutes_Type(Integer32):
    """Custom type hmAgentSwitchIpTableSizeMCRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_HmAgentSwitchIpTableSizeMCRoutes_Type.__name__ = "Integer32"
_HmAgentSwitchIpTableSizeMCRoutes_Object = MibScalar
hmAgentSwitchIpTableSizeMCRoutes = _HmAgentSwitchIpTableSizeMCRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 101, 3),
    _HmAgentSwitchIpTableSizeMCRoutes_Type()
)
hmAgentSwitchIpTableSizeMCRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSwitchIpTableSizeMCRoutes.setStatus("current")


class _HmAgentSwitchIpCurrentTableSizeArp_Type(Integer32):
    """Custom type hmAgentSwitchIpCurrentTableSizeArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 4096),
    )


_HmAgentSwitchIpCurrentTableSizeArp_Type.__name__ = "Integer32"
_HmAgentSwitchIpCurrentTableSizeArp_Object = MibScalar
hmAgentSwitchIpCurrentTableSizeArp = _HmAgentSwitchIpCurrentTableSizeArp_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 101, 4),
    _HmAgentSwitchIpCurrentTableSizeArp_Type()
)
hmAgentSwitchIpCurrentTableSizeArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpCurrentTableSizeArp.setStatus("current")


class _HmAgentSwitchIpCurrentTableSizeUCRoutes_Type(Integer32):
    """Custom type hmAgentSwitchIpCurrentTableSizeUCRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 4096),
    )


_HmAgentSwitchIpCurrentTableSizeUCRoutes_Type.__name__ = "Integer32"
_HmAgentSwitchIpCurrentTableSizeUCRoutes_Object = MibScalar
hmAgentSwitchIpCurrentTableSizeUCRoutes = _HmAgentSwitchIpCurrentTableSizeUCRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 101, 5),
    _HmAgentSwitchIpCurrentTableSizeUCRoutes_Type()
)
hmAgentSwitchIpCurrentTableSizeUCRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpCurrentTableSizeUCRoutes.setStatus("current")


class _HmAgentSwitchIpCurrentTableSizeMCRoutes_Type(Integer32):
    """Custom type hmAgentSwitchIpCurrentTableSizeMCRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_HmAgentSwitchIpCurrentTableSizeMCRoutes_Type.__name__ = "Integer32"
_HmAgentSwitchIpCurrentTableSizeMCRoutes_Object = MibScalar
hmAgentSwitchIpCurrentTableSizeMCRoutes = _HmAgentSwitchIpCurrentTableSizeMCRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 2, 101, 6),
    _HmAgentSwitchIpCurrentTableSizeMCRoutes_Type()
)
hmAgentSwitchIpCurrentTableSizeMCRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSwitchIpCurrentTableSizeMCRoutes.setStatus("current")
_HmAgentRouterRipConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentRouterRipConfigGroup = _HmAgentRouterRipConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3)
)


class _HmAgentRouterRipAdminState_Type(Integer32):
    """Custom type hmAgentRouterRipAdminState based on Integer32"""
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


_HmAgentRouterRipAdminState_Type.__name__ = "Integer32"
_HmAgentRouterRipAdminState_Object = MibScalar
hmAgentRouterRipAdminState = _HmAgentRouterRipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 1),
    _HmAgentRouterRipAdminState_Type()
)
hmAgentRouterRipAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterRipAdminState.setStatus("current")


class _HmAgentRouterRipSplitHorizonMode_Type(Integer32):
    """Custom type hmAgentRouterRipSplitHorizonMode based on Integer32"""
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


_HmAgentRouterRipSplitHorizonMode_Type.__name__ = "Integer32"
_HmAgentRouterRipSplitHorizonMode_Object = MibScalar
hmAgentRouterRipSplitHorizonMode = _HmAgentRouterRipSplitHorizonMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 2),
    _HmAgentRouterRipSplitHorizonMode_Type()
)
hmAgentRouterRipSplitHorizonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterRipSplitHorizonMode.setStatus("current")


class _HmAgentRouterRipAutoSummaryMode_Type(Integer32):
    """Custom type hmAgentRouterRipAutoSummaryMode based on Integer32"""
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


_HmAgentRouterRipAutoSummaryMode_Type.__name__ = "Integer32"
_HmAgentRouterRipAutoSummaryMode_Object = MibScalar
hmAgentRouterRipAutoSummaryMode = _HmAgentRouterRipAutoSummaryMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 3),
    _HmAgentRouterRipAutoSummaryMode_Type()
)
hmAgentRouterRipAutoSummaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterRipAutoSummaryMode.setStatus("current")


class _HmAgentRouterRipHostRoutesAcceptMode_Type(Integer32):
    """Custom type hmAgentRouterRipHostRoutesAcceptMode based on Integer32"""
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


_HmAgentRouterRipHostRoutesAcceptMode_Type.__name__ = "Integer32"
_HmAgentRouterRipHostRoutesAcceptMode_Object = MibScalar
hmAgentRouterRipHostRoutesAcceptMode = _HmAgentRouterRipHostRoutesAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 4),
    _HmAgentRouterRipHostRoutesAcceptMode_Type()
)
hmAgentRouterRipHostRoutesAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterRipHostRoutesAcceptMode.setStatus("current")


class _HmAgentRouterRipDefaultMetric_Type(Integer32):
    """Custom type hmAgentRouterRipDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HmAgentRouterRipDefaultMetric_Type.__name__ = "Integer32"
_HmAgentRouterRipDefaultMetric_Object = MibScalar
hmAgentRouterRipDefaultMetric = _HmAgentRouterRipDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 5),
    _HmAgentRouterRipDefaultMetric_Type()
)
hmAgentRouterRipDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterRipDefaultMetric.setStatus("current")
_HmAgentRouterRipDefaultMetricConfigured_Type = TruthValue
_HmAgentRouterRipDefaultMetricConfigured_Object = MibScalar
hmAgentRouterRipDefaultMetricConfigured = _HmAgentRouterRipDefaultMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 6),
    _HmAgentRouterRipDefaultMetricConfigured_Type()
)
hmAgentRouterRipDefaultMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterRipDefaultMetricConfigured.setStatus("current")


class _HmAgentRouterRipDefaultInfoOriginate_Type(TruthValue):
    """Custom type hmAgentRouterRipDefaultInfoOriginate based on TruthValue"""


_HmAgentRouterRipDefaultInfoOriginate_Object = MibScalar
hmAgentRouterRipDefaultInfoOriginate = _HmAgentRouterRipDefaultInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 7),
    _HmAgentRouterRipDefaultInfoOriginate_Type()
)
hmAgentRouterRipDefaultInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterRipDefaultInfoOriginate.setStatus("current")
_HmAgentRipRouteRedistTable_Object = MibTable
hmAgentRipRouteRedistTable = _HmAgentRipRouteRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8)
)
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistTable.setStatus("current")
_HmAgentRipRouteRedistEntry_Object = MibTableRow
hmAgentRipRouteRedistEntry = _HmAgentRipRouteRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1)
)
hmAgentRipRouteRedistEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentRipRouteRedistSource"),
)
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistEntry.setStatus("current")


class _HmAgentRipRouteRedistSource_Type(Integer32):
    """Custom type hmAgentRipRouteRedistSource based on Integer32"""
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


_HmAgentRipRouteRedistSource_Type.__name__ = "Integer32"
_HmAgentRipRouteRedistSource_Object = MibTableColumn
hmAgentRipRouteRedistSource = _HmAgentRipRouteRedistSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 1),
    _HmAgentRipRouteRedistSource_Type()
)
hmAgentRipRouteRedistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistSource.setStatus("current")


class _HmAgentRipRouteRedistMode_Type(Integer32):
    """Custom type hmAgentRipRouteRedistMode based on Integer32"""
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


_HmAgentRipRouteRedistMode_Type.__name__ = "Integer32"
_HmAgentRipRouteRedistMode_Object = MibTableColumn
hmAgentRipRouteRedistMode = _HmAgentRipRouteRedistMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 2),
    _HmAgentRipRouteRedistMode_Type()
)
hmAgentRipRouteRedistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistMode.setStatus("current")


class _HmAgentRipRouteRedistMetric_Type(Integer32):
    """Custom type hmAgentRipRouteRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HmAgentRipRouteRedistMetric_Type.__name__ = "Integer32"
_HmAgentRipRouteRedistMetric_Object = MibTableColumn
hmAgentRipRouteRedistMetric = _HmAgentRipRouteRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 3),
    _HmAgentRipRouteRedistMetric_Type()
)
hmAgentRipRouteRedistMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistMetric.setStatus("current")
_HmAgentRipRouteRedistMetricConfigured_Type = TruthValue
_HmAgentRipRouteRedistMetricConfigured_Object = MibTableColumn
hmAgentRipRouteRedistMetricConfigured = _HmAgentRipRouteRedistMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 4),
    _HmAgentRipRouteRedistMetricConfigured_Type()
)
hmAgentRipRouteRedistMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistMetricConfigured.setStatus("current")


class _HmAgentRipRouteRedistMatchInternal_Type(Integer32):
    """Custom type hmAgentRipRouteRedistMatchInternal based on Integer32"""
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


_HmAgentRipRouteRedistMatchInternal_Type.__name__ = "Integer32"
_HmAgentRipRouteRedistMatchInternal_Object = MibTableColumn
hmAgentRipRouteRedistMatchInternal = _HmAgentRipRouteRedistMatchInternal_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 5),
    _HmAgentRipRouteRedistMatchInternal_Type()
)
hmAgentRipRouteRedistMatchInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistMatchInternal.setStatus("current")


class _HmAgentRipRouteRedistMatchExternal1_Type(Integer32):
    """Custom type hmAgentRipRouteRedistMatchExternal1 based on Integer32"""
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


_HmAgentRipRouteRedistMatchExternal1_Type.__name__ = "Integer32"
_HmAgentRipRouteRedistMatchExternal1_Object = MibTableColumn
hmAgentRipRouteRedistMatchExternal1 = _HmAgentRipRouteRedistMatchExternal1_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 6),
    _HmAgentRipRouteRedistMatchExternal1_Type()
)
hmAgentRipRouteRedistMatchExternal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistMatchExternal1.setStatus("current")


class _HmAgentRipRouteRedistMatchExternal2_Type(Integer32):
    """Custom type hmAgentRipRouteRedistMatchExternal2 based on Integer32"""
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


_HmAgentRipRouteRedistMatchExternal2_Type.__name__ = "Integer32"
_HmAgentRipRouteRedistMatchExternal2_Object = MibTableColumn
hmAgentRipRouteRedistMatchExternal2 = _HmAgentRipRouteRedistMatchExternal2_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 7),
    _HmAgentRipRouteRedistMatchExternal2_Type()
)
hmAgentRipRouteRedistMatchExternal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistMatchExternal2.setStatus("current")


class _HmAgentRipRouteRedistMatchNSSAExternal1_Type(Integer32):
    """Custom type hmAgentRipRouteRedistMatchNSSAExternal1 based on Integer32"""
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


_HmAgentRipRouteRedistMatchNSSAExternal1_Type.__name__ = "Integer32"
_HmAgentRipRouteRedistMatchNSSAExternal1_Object = MibTableColumn
hmAgentRipRouteRedistMatchNSSAExternal1 = _HmAgentRipRouteRedistMatchNSSAExternal1_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 8),
    _HmAgentRipRouteRedistMatchNSSAExternal1_Type()
)
hmAgentRipRouteRedistMatchNSSAExternal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistMatchNSSAExternal1.setStatus("current")


class _HmAgentRipRouteRedistMatchNSSAExternal2_Type(Integer32):
    """Custom type hmAgentRipRouteRedistMatchNSSAExternal2 based on Integer32"""
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


_HmAgentRipRouteRedistMatchNSSAExternal2_Type.__name__ = "Integer32"
_HmAgentRipRouteRedistMatchNSSAExternal2_Object = MibTableColumn
hmAgentRipRouteRedistMatchNSSAExternal2 = _HmAgentRipRouteRedistMatchNSSAExternal2_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 9),
    _HmAgentRipRouteRedistMatchNSSAExternal2_Type()
)
hmAgentRipRouteRedistMatchNSSAExternal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistMatchNSSAExternal2.setStatus("current")


class _HmAgentRipRouteRedistDistList_Type(Unsigned32):
    """Custom type hmAgentRipRouteRedistDistList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_HmAgentRipRouteRedistDistList_Type.__name__ = "Unsigned32"
_HmAgentRipRouteRedistDistList_Object = MibTableColumn
hmAgentRipRouteRedistDistList = _HmAgentRipRouteRedistDistList_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 10),
    _HmAgentRipRouteRedistDistList_Type()
)
hmAgentRipRouteRedistDistList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistDistList.setStatus("current")
_HmAgentRipRouteRedistDistListConfigured_Type = TruthValue
_HmAgentRipRouteRedistDistListConfigured_Object = MibTableColumn
hmAgentRipRouteRedistDistListConfigured = _HmAgentRipRouteRedistDistListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 8, 1, 11),
    _HmAgentRipRouteRedistDistListConfigured_Type()
)
hmAgentRipRouteRedistDistListConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRipRouteRedistDistListConfigured.setStatus("current")
_HmAgentRip2IfConfTable_Object = MibTable
hmAgentRip2IfConfTable = _HmAgentRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 9)
)
if mibBuilder.loadTexts:
    hmAgentRip2IfConfTable.setStatus("current")
_HmAgentRip2IfConfEntry_Object = MibTableRow
hmAgentRip2IfConfEntry = _HmAgentRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    hmAgentRip2IfConfEntry.setStatus("current")


class _HmAgentRip2IfConfAuthKeyId_Type(Integer32):
    """Custom type hmAgentRip2IfConfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmAgentRip2IfConfAuthKeyId_Type.__name__ = "Integer32"
_HmAgentRip2IfConfAuthKeyId_Object = MibTableColumn
hmAgentRip2IfConfAuthKeyId = _HmAgentRip2IfConfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 9, 1, 1),
    _HmAgentRip2IfConfAuthKeyId_Type()
)
hmAgentRip2IfConfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentRip2IfConfAuthKeyId.setStatus("current")
_HmAgentRip2InterfaceTable_Object = MibTable
hmAgentRip2InterfaceTable = _HmAgentRip2InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10)
)
if mibBuilder.loadTexts:
    hmAgentRip2InterfaceTable.setStatus("current")
_HmAgentRip2InterfaceEntry_Object = MibTableRow
hmAgentRip2InterfaceEntry = _HmAgentRip2InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1)
)
hmAgentRip2InterfaceEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentRip2InterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hmAgentRip2InterfaceEntry.setStatus("current")
_HmAgentRip2InterfaceIfIndex_Type = Integer32
_HmAgentRip2InterfaceIfIndex_Object = MibTableColumn
hmAgentRip2InterfaceIfIndex = _HmAgentRip2InterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 1),
    _HmAgentRip2InterfaceIfIndex_Type()
)
hmAgentRip2InterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentRip2InterfaceIfIndex.setStatus("current")


class _HmAgentRip2InterfaceAuthType_Type(Integer32):
    """Custom type hmAgentRip2InterfaceAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("noAuthentication", 1),
          ("simplePassword", 2))
    )


_HmAgentRip2InterfaceAuthType_Type.__name__ = "Integer32"
_HmAgentRip2InterfaceAuthType_Object = MibTableColumn
hmAgentRip2InterfaceAuthType = _HmAgentRip2InterfaceAuthType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 2),
    _HmAgentRip2InterfaceAuthType_Type()
)
hmAgentRip2InterfaceAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRip2InterfaceAuthType.setStatus("current")


class _HmAgentRip2InterfaceAuthKey_Type(OctetString):
    """Custom type hmAgentRip2InterfaceAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HmAgentRip2InterfaceAuthKey_Type.__name__ = "OctetString"
_HmAgentRip2InterfaceAuthKey_Object = MibTableColumn
hmAgentRip2InterfaceAuthKey = _HmAgentRip2InterfaceAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 3),
    _HmAgentRip2InterfaceAuthKey_Type()
)
hmAgentRip2InterfaceAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRip2InterfaceAuthKey.setStatus("current")


class _HmAgentRip2InterfaceAuthKeyId_Type(Integer32):
    """Custom type hmAgentRip2InterfaceAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmAgentRip2InterfaceAuthKeyId_Type.__name__ = "Integer32"
_HmAgentRip2InterfaceAuthKeyId_Object = MibTableColumn
hmAgentRip2InterfaceAuthKeyId = _HmAgentRip2InterfaceAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 4),
    _HmAgentRip2InterfaceAuthKeyId_Type()
)
hmAgentRip2InterfaceAuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRip2InterfaceAuthKeyId.setStatus("current")


class _HmAgentRip2InterfaceSendVersion_Type(Integer32):
    """Custom type hmAgentRip2InterfaceSendVersion based on Integer32"""
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
        *(("doNotSend", 1),
          ("rip1Compatible", 3),
          ("ripVersion1", 2),
          ("ripVersion2", 4))
    )


_HmAgentRip2InterfaceSendVersion_Type.__name__ = "Integer32"
_HmAgentRip2InterfaceSendVersion_Object = MibTableColumn
hmAgentRip2InterfaceSendVersion = _HmAgentRip2InterfaceSendVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 5),
    _HmAgentRip2InterfaceSendVersion_Type()
)
hmAgentRip2InterfaceSendVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRip2InterfaceSendVersion.setStatus("current")


class _HmAgentRip2InterfaceReceiveVersion_Type(Integer32):
    """Custom type hmAgentRip2InterfaceReceiveVersion based on Integer32"""
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
        *(("doNotReceive", 4),
          ("rip1", 1),
          ("rip1OrRip2", 3),
          ("rip2", 2))
    )


_HmAgentRip2InterfaceReceiveVersion_Type.__name__ = "Integer32"
_HmAgentRip2InterfaceReceiveVersion_Object = MibTableColumn
hmAgentRip2InterfaceReceiveVersion = _HmAgentRip2InterfaceReceiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 6),
    _HmAgentRip2InterfaceReceiveVersion_Type()
)
hmAgentRip2InterfaceReceiveVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRip2InterfaceReceiveVersion.setStatus("current")


class _HmAgentRip2InterfaceAdminState_Type(Integer32):
    """Custom type hmAgentRip2InterfaceAdminState based on Integer32"""
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


_HmAgentRip2InterfaceAdminState_Type.__name__ = "Integer32"
_HmAgentRip2InterfaceAdminState_Object = MibTableColumn
hmAgentRip2InterfaceAdminState = _HmAgentRip2InterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 7),
    _HmAgentRip2InterfaceAdminState_Type()
)
hmAgentRip2InterfaceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRip2InterfaceAdminState.setStatus("current")
_HmAgentRip2RcvBadPackets_Type = Counter32
_HmAgentRip2RcvBadPackets_Object = MibTableColumn
hmAgentRip2RcvBadPackets = _HmAgentRip2RcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 8),
    _HmAgentRip2RcvBadPackets_Type()
)
hmAgentRip2RcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentRip2RcvBadPackets.setStatus("current")
_HmAgentRip2RcvBadRoutes_Type = Counter32
_HmAgentRip2RcvBadRoutes_Object = MibTableColumn
hmAgentRip2RcvBadRoutes = _HmAgentRip2RcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 9),
    _HmAgentRip2RcvBadRoutes_Type()
)
hmAgentRip2RcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentRip2RcvBadRoutes.setStatus("current")
_HmAgentRip2SentUpdates_Type = Counter32
_HmAgentRip2SentUpdates_Object = MibTableColumn
hmAgentRip2SentUpdates = _HmAgentRip2SentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 10, 1, 10),
    _HmAgentRip2SentUpdates_Type()
)
hmAgentRip2SentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentRip2SentUpdates.setStatus("current")


class _HmAgentRouterRipUpdateTimerInterval_Type(Integer32):
    """Custom type hmAgentRouterRipUpdateTimerInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HmAgentRouterRipUpdateTimerInterval_Type.__name__ = "Integer32"
_HmAgentRouterRipUpdateTimerInterval_Object = MibScalar
hmAgentRouterRipUpdateTimerInterval = _HmAgentRouterRipUpdateTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 3, 50),
    _HmAgentRouterRipUpdateTimerInterval_Type()
)
hmAgentRouterRipUpdateTimerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterRipUpdateTimerInterval.setStatus("current")
_HmAgentRouterOspfConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentRouterOspfConfigGroup = _HmAgentRouterOspfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4)
)


class _HmAgentOspfDefaultMetric_Type(Integer32):
    """Custom type hmAgentOspfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HmAgentOspfDefaultMetric_Type.__name__ = "Integer32"
_HmAgentOspfDefaultMetric_Object = MibScalar
hmAgentOspfDefaultMetric = _HmAgentOspfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 1),
    _HmAgentOspfDefaultMetric_Type()
)
hmAgentOspfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfDefaultMetric.setStatus("current")
_HmAgentOspfDefaultMetricConfigured_Type = TruthValue
_HmAgentOspfDefaultMetricConfigured_Object = MibScalar
hmAgentOspfDefaultMetricConfigured = _HmAgentOspfDefaultMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 2),
    _HmAgentOspfDefaultMetricConfigured_Type()
)
hmAgentOspfDefaultMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfDefaultMetricConfigured.setStatus("current")


class _HmAgentOspfDefaultInfoOriginate_Type(TruthValue):
    """Custom type hmAgentOspfDefaultInfoOriginate based on TruthValue"""


_HmAgentOspfDefaultInfoOriginate_Object = MibScalar
hmAgentOspfDefaultInfoOriginate = _HmAgentOspfDefaultInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 3),
    _HmAgentOspfDefaultInfoOriginate_Type()
)
hmAgentOspfDefaultInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfDefaultInfoOriginate.setStatus("current")


class _HmAgentOspfDefaultInfoOriginateAlways_Type(TruthValue):
    """Custom type hmAgentOspfDefaultInfoOriginateAlways based on TruthValue"""


_HmAgentOspfDefaultInfoOriginateAlways_Object = MibScalar
hmAgentOspfDefaultInfoOriginateAlways = _HmAgentOspfDefaultInfoOriginateAlways_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 4),
    _HmAgentOspfDefaultInfoOriginateAlways_Type()
)
hmAgentOspfDefaultInfoOriginateAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfDefaultInfoOriginateAlways.setStatus("current")


class _HmAgentOspfDefaultInfoOriginateMetric_Type(Integer32):
    """Custom type hmAgentOspfDefaultInfoOriginateMetric based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HmAgentOspfDefaultInfoOriginateMetric_Type.__name__ = "Integer32"
_HmAgentOspfDefaultInfoOriginateMetric_Object = MibScalar
hmAgentOspfDefaultInfoOriginateMetric = _HmAgentOspfDefaultInfoOriginateMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 5),
    _HmAgentOspfDefaultInfoOriginateMetric_Type()
)
hmAgentOspfDefaultInfoOriginateMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfDefaultInfoOriginateMetric.setStatus("current")
_HmAgentOspfDefaultInfoOriginateMetricConfigured_Type = TruthValue
_HmAgentOspfDefaultInfoOriginateMetricConfigured_Object = MibScalar
hmAgentOspfDefaultInfoOriginateMetricConfigured = _HmAgentOspfDefaultInfoOriginateMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 6),
    _HmAgentOspfDefaultInfoOriginateMetricConfigured_Type()
)
hmAgentOspfDefaultInfoOriginateMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfDefaultInfoOriginateMetricConfigured.setStatus("current")


class _HmAgentOspfDefaultInfoOriginateMetricType_Type(Integer32):
    """Custom type hmAgentOspfDefaultInfoOriginateMetricType based on Integer32"""
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


_HmAgentOspfDefaultInfoOriginateMetricType_Type.__name__ = "Integer32"
_HmAgentOspfDefaultInfoOriginateMetricType_Object = MibScalar
hmAgentOspfDefaultInfoOriginateMetricType = _HmAgentOspfDefaultInfoOriginateMetricType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 7),
    _HmAgentOspfDefaultInfoOriginateMetricType_Type()
)
hmAgentOspfDefaultInfoOriginateMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfDefaultInfoOriginateMetricType.setStatus("current")
_HmAgentOspfRouteRedistTable_Object = MibTable
hmAgentOspfRouteRedistTable = _HmAgentOspfRouteRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8)
)
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistTable.setStatus("current")
_HmAgentOspfRouteRedistEntry_Object = MibTableRow
hmAgentOspfRouteRedistEntry = _HmAgentOspfRouteRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1)
)
hmAgentOspfRouteRedistEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmAgentOspfRouteRedistSource"),
)
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistEntry.setStatus("current")


class _HmAgentOspfRouteRedistSource_Type(Integer32):
    """Custom type hmAgentOspfRouteRedistSource based on Integer32"""
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


_HmAgentOspfRouteRedistSource_Type.__name__ = "Integer32"
_HmAgentOspfRouteRedistSource_Object = MibTableColumn
hmAgentOspfRouteRedistSource = _HmAgentOspfRouteRedistSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1, 1),
    _HmAgentOspfRouteRedistSource_Type()
)
hmAgentOspfRouteRedistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistSource.setStatus("current")


class _HmAgentOspfRouteRedistMode_Type(Integer32):
    """Custom type hmAgentOspfRouteRedistMode based on Integer32"""
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


_HmAgentOspfRouteRedistMode_Type.__name__ = "Integer32"
_HmAgentOspfRouteRedistMode_Object = MibTableColumn
hmAgentOspfRouteRedistMode = _HmAgentOspfRouteRedistMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1, 2),
    _HmAgentOspfRouteRedistMode_Type()
)
hmAgentOspfRouteRedistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistMode.setStatus("current")


class _HmAgentOspfRouteRedistMetric_Type(Integer32):
    """Custom type hmAgentOspfRouteRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HmAgentOspfRouteRedistMetric_Type.__name__ = "Integer32"
_HmAgentOspfRouteRedistMetric_Object = MibTableColumn
hmAgentOspfRouteRedistMetric = _HmAgentOspfRouteRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1, 3),
    _HmAgentOspfRouteRedistMetric_Type()
)
hmAgentOspfRouteRedistMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistMetric.setStatus("current")
_HmAgentOspfRouteRedistMetricConfigured_Type = TruthValue
_HmAgentOspfRouteRedistMetricConfigured_Object = MibTableColumn
hmAgentOspfRouteRedistMetricConfigured = _HmAgentOspfRouteRedistMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1, 4),
    _HmAgentOspfRouteRedistMetricConfigured_Type()
)
hmAgentOspfRouteRedistMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistMetricConfigured.setStatus("current")


class _HmAgentOspfRouteRedistMetricType_Type(Integer32):
    """Custom type hmAgentOspfRouteRedistMetricType based on Integer32"""
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


_HmAgentOspfRouteRedistMetricType_Type.__name__ = "Integer32"
_HmAgentOspfRouteRedistMetricType_Object = MibTableColumn
hmAgentOspfRouteRedistMetricType = _HmAgentOspfRouteRedistMetricType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1, 5),
    _HmAgentOspfRouteRedistMetricType_Type()
)
hmAgentOspfRouteRedistMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistMetricType.setStatus("current")


class _HmAgentOspfRouteRedistTag_Type(Unsigned32):
    """Custom type hmAgentOspfRouteRedistTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HmAgentOspfRouteRedistTag_Type.__name__ = "Unsigned32"
_HmAgentOspfRouteRedistTag_Object = MibTableColumn
hmAgentOspfRouteRedistTag = _HmAgentOspfRouteRedistTag_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1, 6),
    _HmAgentOspfRouteRedistTag_Type()
)
hmAgentOspfRouteRedistTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistTag.setStatus("current")


class _HmAgentOspfRouteRedistSubnets_Type(TruthValue):
    """Custom type hmAgentOspfRouteRedistSubnets based on TruthValue"""


_HmAgentOspfRouteRedistSubnets_Object = MibTableColumn
hmAgentOspfRouteRedistSubnets = _HmAgentOspfRouteRedistSubnets_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1, 7),
    _HmAgentOspfRouteRedistSubnets_Type()
)
hmAgentOspfRouteRedistSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistSubnets.setStatus("current")


class _HmAgentOspfRouteRedistDistList_Type(Unsigned32):
    """Custom type hmAgentOspfRouteRedistDistList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_HmAgentOspfRouteRedistDistList_Type.__name__ = "Unsigned32"
_HmAgentOspfRouteRedistDistList_Object = MibTableColumn
hmAgentOspfRouteRedistDistList = _HmAgentOspfRouteRedistDistList_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1, 8),
    _HmAgentOspfRouteRedistDistList_Type()
)
hmAgentOspfRouteRedistDistList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistDistList.setStatus("current")
_HmAgentOspfRouteRedistDistListConfigured_Type = TruthValue
_HmAgentOspfRouteRedistDistListConfigured_Object = MibTableColumn
hmAgentOspfRouteRedistDistListConfigured = _HmAgentOspfRouteRedistDistListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 8, 1, 9),
    _HmAgentOspfRouteRedistDistListConfigured_Type()
)
hmAgentOspfRouteRedistDistListConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfRouteRedistDistListConfigured.setStatus("current")
_HmAgentOspfIfTable_Object = MibTable
hmAgentOspfIfTable = _HmAgentOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 9)
)
if mibBuilder.loadTexts:
    hmAgentOspfIfTable.setStatus("current")
_HmAgentOspfIfEntry_Object = MibTableRow
hmAgentOspfIfEntry = _HmAgentOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 9, 1)
)
if mibBuilder.loadTexts:
    hmAgentOspfIfEntry.setStatus("current")


class _HmAgentOspfIfAuthKeyId_Type(Integer32):
    """Custom type hmAgentOspfIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmAgentOspfIfAuthKeyId_Type.__name__ = "Integer32"
_HmAgentOspfIfAuthKeyId_Object = MibTableColumn
hmAgentOspfIfAuthKeyId = _HmAgentOspfIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 9, 1, 1),
    _HmAgentOspfIfAuthKeyId_Type()
)
hmAgentOspfIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentOspfIfAuthKeyId.setStatus("current")


class _HmAgentOspfIfIpMtuIgnoreFlag_Type(Integer32):
    """Custom type hmAgentOspfIfIpMtuIgnoreFlag based on Integer32"""
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


_HmAgentOspfIfIpMtuIgnoreFlag_Type.__name__ = "Integer32"
_HmAgentOspfIfIpMtuIgnoreFlag_Object = MibTableColumn
hmAgentOspfIfIpMtuIgnoreFlag = _HmAgentOspfIfIpMtuIgnoreFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 9, 1, 2),
    _HmAgentOspfIfIpMtuIgnoreFlag_Type()
)
hmAgentOspfIfIpMtuIgnoreFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentOspfIfIpMtuIgnoreFlag.setStatus("current")
_HmAgentOspfVirtIfTable_Object = MibTable
hmAgentOspfVirtIfTable = _HmAgentOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 10)
)
if mibBuilder.loadTexts:
    hmAgentOspfVirtIfTable.setStatus("current")
_HmAgentOspfVirtIfEntry_Object = MibTableRow
hmAgentOspfVirtIfEntry = _HmAgentOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 10, 1)
)
if mibBuilder.loadTexts:
    hmAgentOspfVirtIfEntry.setStatus("current")


class _HmAgentOspfVirtIfAuthKeyId_Type(Integer32):
    """Custom type hmAgentOspfVirtIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmAgentOspfVirtIfAuthKeyId_Type.__name__ = "Integer32"
_HmAgentOspfVirtIfAuthKeyId_Object = MibTableColumn
hmAgentOspfVirtIfAuthKeyId = _HmAgentOspfVirtIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 10, 1, 1),
    _HmAgentOspfVirtIfAuthKeyId_Type()
)
hmAgentOspfVirtIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmAgentOspfVirtIfAuthKeyId.setStatus("current")


class _HmAgentRouterOspfRFC1583CompatibilityMode_Type(Integer32):
    """Custom type hmAgentRouterOspfRFC1583CompatibilityMode based on Integer32"""
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


_HmAgentRouterOspfRFC1583CompatibilityMode_Type.__name__ = "Integer32"
_HmAgentRouterOspfRFC1583CompatibilityMode_Object = MibScalar
hmAgentRouterOspfRFC1583CompatibilityMode = _HmAgentRouterOspfRFC1583CompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 4, 11),
    _HmAgentRouterOspfRFC1583CompatibilityMode_Type()
)
hmAgentRouterOspfRFC1583CompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterOspfRFC1583CompatibilityMode.setStatus("current")
_HmAgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity = ObjectIdentity
hmAgentSnmpTrapFlagsConfigGroupLayer3 = _HmAgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 5)
)


class _HmAgentSnmpVRRPNewMasterTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpVRRPNewMasterTrapFlag based on Integer32"""
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


_HmAgentSnmpVRRPNewMasterTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpVRRPNewMasterTrapFlag_Object = MibScalar
hmAgentSnmpVRRPNewMasterTrapFlag = _HmAgentSnmpVRRPNewMasterTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 5, 1),
    _HmAgentSnmpVRRPNewMasterTrapFlag_Type()
)
hmAgentSnmpVRRPNewMasterTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpVRRPNewMasterTrapFlag.setStatus("current")


class _HmAgentSnmpVRRPAuthFailureTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpVRRPAuthFailureTrapFlag based on Integer32"""
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


_HmAgentSnmpVRRPAuthFailureTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpVRRPAuthFailureTrapFlag_Object = MibScalar
hmAgentSnmpVRRPAuthFailureTrapFlag = _HmAgentSnmpVRRPAuthFailureTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 5, 2),
    _HmAgentSnmpVRRPAuthFailureTrapFlag_Type()
)
hmAgentSnmpVRRPAuthFailureTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpVRRPAuthFailureTrapFlag.setStatus("current")
_HmAgentECMPGroup_ObjectIdentity = ObjectIdentity
hmAgentECMPGroup = _HmAgentECMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 7)
)


class _HmAgentECMPOspfMaxPaths_Type(Integer32):
    """Custom type hmAgentECMPOspfMaxPaths based on Integer32"""
    defaultValue = 4


_HmAgentECMPOspfMaxPaths_Object = MibScalar
hmAgentECMPOspfMaxPaths = _HmAgentECMPOspfMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 7, 1),
    _HmAgentECMPOspfMaxPaths_Type()
)
hmAgentECMPOspfMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentECMPOspfMaxPaths.setStatus("current")
_HmAgentRouterVrrpConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentRouterVrrpConfigGroup = _HmAgentRouterVrrpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 8)
)


class _HmAgentRouterVrrpAdminState_Type(Integer32):
    """Custom type hmAgentRouterVrrpAdminState based on Integer32"""
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


_HmAgentRouterVrrpAdminState_Type.__name__ = "Integer32"
_HmAgentRouterVrrpAdminState_Object = MibScalar
hmAgentRouterVrrpAdminState = _HmAgentRouterVrrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 8, 1),
    _HmAgentRouterVrrpAdminState_Type()
)
hmAgentRouterVrrpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentRouterVrrpAdminState.setStatus("current")
_HmVrrpExtGroup_ObjectIdentity = ObjectIdentity
hmVrrpExtGroup = _HmVrrpExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9)
)
_HmVrrpTrackingTable_Object = MibTable
hmVrrpTrackingTable = _HmVrrpTrackingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 1)
)
if mibBuilder.loadTexts:
    hmVrrpTrackingTable.setStatus("current")
_HmVrrpTrackingEntry_Object = MibTableRow
hmVrrpTrackingEntry = _HmVrrpTrackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 1, 1)
)
hmVrrpTrackingEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmVrrpTrackIfIndex"),
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmVrrpTrackVrid"),
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmVrrpTrackId"),
)
if mibBuilder.loadTexts:
    hmVrrpTrackingEntry.setStatus("current")
_HmVrrpTrackIfIndex_Type = Integer32
_HmVrrpTrackIfIndex_Object = MibTableColumn
hmVrrpTrackIfIndex = _HmVrrpTrackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 1, 1, 1),
    _HmVrrpTrackIfIndex_Type()
)
hmVrrpTrackIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmVrrpTrackIfIndex.setStatus("current")


class _HmVrrpTrackVrid_Type(Integer32):
    """Custom type hmVrrpTrackVrid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmVrrpTrackVrid_Type.__name__ = "Integer32"
_HmVrrpTrackVrid_Object = MibTableColumn
hmVrrpTrackVrid = _HmVrrpTrackVrid_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 1, 1, 2),
    _HmVrrpTrackVrid_Type()
)
hmVrrpTrackVrid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmVrrpTrackVrid.setStatus("current")
_HmVrrpTrackId_Type = Integer32
_HmVrrpTrackId_Object = MibTableColumn
hmVrrpTrackId = _HmVrrpTrackId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 1, 1, 3),
    _HmVrrpTrackId_Type()
)
hmVrrpTrackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmVrrpTrackId.setStatus("current")


class _HmVrrpTrackDecrement_Type(Integer32):
    """Custom type hmVrrpTrackDecrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 253),
    )


_HmVrrpTrackDecrement_Type.__name__ = "Integer32"
_HmVrrpTrackDecrement_Object = MibTableColumn
hmVrrpTrackDecrement = _HmVrrpTrackDecrement_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 1, 1, 4),
    _HmVrrpTrackDecrement_Type()
)
hmVrrpTrackDecrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmVrrpTrackDecrement.setStatus("current")


class _HmVrrpTrackOperStatus_Type(Integer32):
    """Custom type hmVrrpTrackOperStatus based on Integer32"""
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


_HmVrrpTrackOperStatus_Type.__name__ = "Integer32"
_HmVrrpTrackOperStatus_Object = MibTableColumn
hmVrrpTrackOperStatus = _HmVrrpTrackOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 1, 1, 5),
    _HmVrrpTrackOperStatus_Type()
)
hmVrrpTrackOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmVrrpTrackOperStatus.setStatus("current")
_HmVrrpTrackRowStatus_Type = RowStatus
_HmVrrpTrackRowStatus_Object = MibTableColumn
hmVrrpTrackRowStatus = _HmVrrpTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 1, 1, 6),
    _HmVrrpTrackRowStatus_Type()
)
hmVrrpTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmVrrpTrackRowStatus.setStatus("current")
_HmVrrpExtTable_Object = MibTable
hmVrrpExtTable = _HmVrrpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2)
)
if mibBuilder.loadTexts:
    hmVrrpExtTable.setStatus("current")
_HmVrrpExtEntry_Object = MibTableRow
hmVrrpExtEntry = _HmVrrpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1)
)
hmVrrpExtEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmVrrpExtIfIndex"),
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmVrrpExtVrid"),
)
if mibBuilder.loadTexts:
    hmVrrpExtEntry.setStatus("current")
_HmVrrpExtIfIndex_Type = Integer32
_HmVrrpExtIfIndex_Object = MibTableColumn
hmVrrpExtIfIndex = _HmVrrpExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 1),
    _HmVrrpExtIfIndex_Type()
)
hmVrrpExtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmVrrpExtIfIndex.setStatus("current")


class _HmVrrpExtVrid_Type(Integer32):
    """Custom type hmVrrpExtVrid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmVrrpExtVrid_Type.__name__ = "Integer32"
_HmVrrpExtVrid_Object = MibTableColumn
hmVrrpExtVrid = _HmVrrpExtVrid_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 2),
    _HmVrrpExtVrid_Type()
)
hmVrrpExtVrid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmVrrpExtVrid.setStatus("current")


class _HmVrrpExtDomainId_Type(Integer32):
    """Custom type hmVrrpExtDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HmVrrpExtDomainId_Type.__name__ = "Integer32"
_HmVrrpExtDomainId_Object = MibTableColumn
hmVrrpExtDomainId = _HmVrrpExtDomainId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 3),
    _HmVrrpExtDomainId_Type()
)
hmVrrpExtDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmVrrpExtDomainId.setStatus("current")


class _HmVrrpExtDomainRole_Type(Integer32):
    """Custom type hmVrrpExtDomainRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("member", 2),
          ("none", 1),
          ("supervisor", 3))
    )


_HmVrrpExtDomainRole_Type.__name__ = "Integer32"
_HmVrrpExtDomainRole_Object = MibTableColumn
hmVrrpExtDomainRole = _HmVrrpExtDomainRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 4),
    _HmVrrpExtDomainRole_Type()
)
hmVrrpExtDomainRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmVrrpExtDomainRole.setStatus("current")


class _HmVrrpExtDomainStatus_Type(Integer32):
    """Custom type hmVrrpExtDomainStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("noSupervisor", 2),
          ("supervisorDown", 3))
    )


_HmVrrpExtDomainStatus_Type.__name__ = "Integer32"
_HmVrrpExtDomainStatus_Object = MibTableColumn
hmVrrpExtDomainStatus = _HmVrrpExtDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 5),
    _HmVrrpExtDomainStatus_Type()
)
hmVrrpExtDomainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmVrrpExtDomainStatus.setStatus("current")
_HmVrrpExtAdvertAddress_Type = IpAddress
_HmVrrpExtAdvertAddress_Object = MibTableColumn
hmVrrpExtAdvertAddress = _HmVrrpExtAdvertAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 6),
    _HmVrrpExtAdvertAddress_Type()
)
hmVrrpExtAdvertAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmVrrpExtAdvertAddress.setStatus("current")


class _HmVrrpExtAdvertTimer_Type(Integer32):
    """Custom type hmVrrpExtAdvertTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 255000),
    )


_HmVrrpExtAdvertTimer_Type.__name__ = "Integer32"
_HmVrrpExtAdvertTimer_Object = MibTableColumn
hmVrrpExtAdvertTimer = _HmVrrpExtAdvertTimer_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 7),
    _HmVrrpExtAdvertTimer_Type()
)
hmVrrpExtAdvertTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmVrrpExtAdvertTimer.setStatus("current")
if mibBuilder.loadTexts:
    hmVrrpExtAdvertTimer.setUnits("milliseconds")


class _HmVrrpExtOperPriority_Type(Integer32):
    """Custom type hmVrrpExtOperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmVrrpExtOperPriority_Type.__name__ = "Integer32"
_HmVrrpExtOperPriority_Object = MibTableColumn
hmVrrpExtOperPriority = _HmVrrpExtOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 8),
    _HmVrrpExtOperPriority_Type()
)
hmVrrpExtOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmVrrpExtOperPriority.setStatus("current")
_HmVrrpExtNotifyAddress_Type = IpAddress
_HmVrrpExtNotifyAddress_Object = MibTableColumn
hmVrrpExtNotifyAddress = _HmVrrpExtNotifyAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 9),
    _HmVrrpExtNotifyAddress_Type()
)
hmVrrpExtNotifyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmVrrpExtNotifyAddress.setStatus("current")


class _HmVrrpExtNotifyLinkdown_Type(Integer32):
    """Custom type hmVrrpExtNotifyLinkdown based on Integer32"""
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


_HmVrrpExtNotifyLinkdown_Type.__name__ = "Integer32"
_HmVrrpExtNotifyLinkdown_Object = MibTableColumn
hmVrrpExtNotifyLinkdown = _HmVrrpExtNotifyLinkdown_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 10),
    _HmVrrpExtNotifyLinkdown_Type()
)
hmVrrpExtNotifyLinkdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmVrrpExtNotifyLinkdown.setStatus("current")


class _HmVrrpExtPreemptionDelay_Type(Integer32):
    """Custom type hmVrrpExtPreemptionDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmVrrpExtPreemptionDelay_Type.__name__ = "Integer32"
_HmVrrpExtPreemptionDelay_Object = MibTableColumn
hmVrrpExtPreemptionDelay = _HmVrrpExtPreemptionDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 2, 1, 11),
    _HmVrrpExtPreemptionDelay_Type()
)
hmVrrpExtPreemptionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmVrrpExtPreemptionDelay.setStatus("current")
_HmVrrpDomainTable_Object = MibTable
hmVrrpDomainTable = _HmVrrpDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 3)
)
if mibBuilder.loadTexts:
    hmVrrpDomainTable.setStatus("current")
_HmVrrpDomainEntry_Object = MibTableRow
hmVrrpDomainEntry = _HmVrrpDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 3, 1)
)
hmVrrpDomainEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-ROUTING-MIB", "hmVrrpDomainId"),
)
if mibBuilder.loadTexts:
    hmVrrpDomainEntry.setStatus("current")


class _HmVrrpDomainId_Type(Integer32):
    """Custom type hmVrrpDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HmVrrpDomainId_Type.__name__ = "Integer32"
_HmVrrpDomainId_Object = MibTableColumn
hmVrrpDomainId = _HmVrrpDomainId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 3, 1, 1),
    _HmVrrpDomainId_Type()
)
hmVrrpDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmVrrpDomainId.setStatus("current")


class _HmVrrpDomainMemberSendAdv_Type(Integer32):
    """Custom type hmVrrpDomainMemberSendAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HmVrrpDomainMemberSendAdv_Type.__name__ = "Integer32"
_HmVrrpDomainMemberSendAdv_Object = MibTableColumn
hmVrrpDomainMemberSendAdv = _HmVrrpDomainMemberSendAdv_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 3, 1, 2),
    _HmVrrpDomainMemberSendAdv_Type()
)
hmVrrpDomainMemberSendAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmVrrpDomainMemberSendAdv.setStatus("current")


class _HmVrrpDomainStatus_Type(Integer32):
    """Custom type hmVrrpDomainStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("noSupervisor", 2),
          ("supervisorDown", 3))
    )


_HmVrrpDomainStatus_Type.__name__ = "Integer32"
_HmVrrpDomainStatus_Object = MibTableColumn
hmVrrpDomainStatus = _HmVrrpDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 3, 1, 3),
    _HmVrrpDomainStatus_Type()
)
hmVrrpDomainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmVrrpDomainStatus.setStatus("current")
_HmVrrpDomainSupervisorIfIndex_Type = Integer32
_HmVrrpDomainSupervisorIfIndex_Object = MibTableColumn
hmVrrpDomainSupervisorIfIndex = _HmVrrpDomainSupervisorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 3, 1, 4),
    _HmVrrpDomainSupervisorIfIndex_Type()
)
hmVrrpDomainSupervisorIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmVrrpDomainSupervisorIfIndex.setStatus("current")


class _HmVrrpDomainSupervisorVrid_Type(Integer32):
    """Custom type hmVrrpDomainSupervisorVrid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmVrrpDomainSupervisorVrid_Type.__name__ = "Integer32"
_HmVrrpDomainSupervisorVrid_Object = MibTableColumn
hmVrrpDomainSupervisorVrid = _HmVrrpDomainSupervisorVrid_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 3, 1, 5),
    _HmVrrpDomainSupervisorVrid_Type()
)
hmVrrpDomainSupervisorVrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmVrrpDomainSupervisorVrid.setStatus("current")


class _HmVrrpDomainOperPriority_Type(Integer32):
    """Custom type hmVrrpDomainOperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmVrrpDomainOperPriority_Type.__name__ = "Integer32"
_HmVrrpDomainOperPriority_Object = MibTableColumn
hmVrrpDomainOperPriority = _HmVrrpDomainOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 3, 1, 6),
    _HmVrrpDomainOperPriority_Type()
)
hmVrrpDomainOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmVrrpDomainOperPriority.setStatus("current")


class _HmVrrpDomainSupervisorOperState_Type(Integer32):
    """Custom type hmVrrpDomainSupervisorOperState based on Integer32"""
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
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3),
          ("unknown", 4))
    )


_HmVrrpDomainSupervisorOperState_Type.__name__ = "Integer32"
_HmVrrpDomainSupervisorOperState_Object = MibTableColumn
hmVrrpDomainSupervisorOperState = _HmVrrpDomainSupervisorOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 2, 9, 3, 1, 7),
    _HmVrrpDomainSupervisorOperState_Type()
)
hmVrrpDomainSupervisorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmVrrpDomainSupervisorOperState.setStatus("current")
rip2IfConfEntry.registerAugmentions(
    ("HIRSCHMANN-MMP4-ROUTING-MIB",
     "hmAgentRip2IfConfEntry")
)
hmAgentRip2IfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("HIRSCHMANN-MMP4-ROUTING-MIB",
     "hmAgentOspfIfEntry")
)
hmAgentOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("HIRSCHMANN-MMP4-ROUTING-MIB",
     "hmAgentOspfVirtIfEntry")
)
hmAgentOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-MMP4-ROUTING-MIB",
    **{"hmPlatform4Routing": hmPlatform4Routing,
       "hmAgentSwitchArpGroup": hmAgentSwitchArpGroup,
       "hmAgentSwitchArpAgeoutTime": hmAgentSwitchArpAgeoutTime,
       "hmAgentSwitchArpResponseTime": hmAgentSwitchArpResponseTime,
       "hmAgentSwitchArpMaxRetries": hmAgentSwitchArpMaxRetries,
       "hmAgentSwitchArpCacheSize": hmAgentSwitchArpCacheSize,
       "hmAgentSwitchArpDynamicRenew": hmAgentSwitchArpDynamicRenew,
       "hmAgentSwitchArpTotalEntryCountCurrent": hmAgentSwitchArpTotalEntryCountCurrent,
       "hmAgentSwitchArpTotalEntryCountPeak": hmAgentSwitchArpTotalEntryCountPeak,
       "hmAgentSwitchArpStaticEntryCountCurrent": hmAgentSwitchArpStaticEntryCountCurrent,
       "hmAgentSwitchArpStaticEntryCountMax": hmAgentSwitchArpStaticEntryCountMax,
       "hmAgentSwitchArpTable": hmAgentSwitchArpTable,
       "hmAgentSwitchArpEntry": hmAgentSwitchArpEntry,
       "hmAgentSwitchArpAge": hmAgentSwitchArpAge,
       "hmAgentSwitchArpIpAddress": hmAgentSwitchArpIpAddress,
       "hmAgentSwitchArpMacAddress": hmAgentSwitchArpMacAddress,
       "hmAgentSwitchArpInterface": hmAgentSwitchArpInterface,
       "hmAgentSwitchArpType": hmAgentSwitchArpType,
       "hmAgentSwitchArpStatus": hmAgentSwitchArpStatus,
       "hmAgentSwitchArpSparseLearn": hmAgentSwitchArpSparseLearn,
       "hmAgentSwitchIpGroup": hmAgentSwitchIpGroup,
       "hmAgentSwitchIpRoutingMode": hmAgentSwitchIpRoutingMode,
       "hmAgentSwitchIpVRRPMode": hmAgentSwitchIpVRRPMode,
       "hmAgentSwitchIpInterfaceTable": hmAgentSwitchIpInterfaceTable,
       "hmAgentSwitchIpInterfaceEntry": hmAgentSwitchIpInterfaceEntry,
       "hmAgentSwitchIpInterfaceIfIndex": hmAgentSwitchIpInterfaceIfIndex,
       "hmAgentSwitchIpInterfaceIpAddress": hmAgentSwitchIpInterfaceIpAddress,
       "hmAgentSwitchIpInterfaceNetMask": hmAgentSwitchIpInterfaceNetMask,
       "hmAgentSwitchIpInterfaceClearIp": hmAgentSwitchIpInterfaceClearIp,
       "hmAgentSwitchIpInterfaceRoutingMode": hmAgentSwitchIpInterfaceRoutingMode,
       "hmAgentSwitchIpInterfaceProxyARPMode": hmAgentSwitchIpInterfaceProxyARPMode,
       "hmAgentSwitchIpInterfaceMtuValue": hmAgentSwitchIpInterfaceMtuValue,
       "hmAgentSwitchIpInterfaceSlotNum": hmAgentSwitchIpInterfaceSlotNum,
       "hmAgentSwitchIpInterfacePortNum": hmAgentSwitchIpInterfacePortNum,
       "hmAgentSwitchIpInterfaceNetdirectedBCMode": hmAgentSwitchIpInterfaceNetdirectedBCMode,
       "hmAgentSwitchIpRouterDiscoveryTable": hmAgentSwitchIpRouterDiscoveryTable,
       "hmAgentSwitchIpRouterDiscoveryEntry": hmAgentSwitchIpRouterDiscoveryEntry,
       "hmAgentSwitchIpRouterDiscoveryIfIndex": hmAgentSwitchIpRouterDiscoveryIfIndex,
       "hmAgentSwitchIpRouterDiscoveryAdvertiseMode": hmAgentSwitchIpRouterDiscoveryAdvertiseMode,
       "hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval": hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval,
       "hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval": hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval,
       "hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime": hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime,
       "hmAgentSwitchIpRouterDiscoveryPreferenceLevel": hmAgentSwitchIpRouterDiscoveryPreferenceLevel,
       "hmAgentSwitchIpRouterDiscoveryAdvertisementAddress": hmAgentSwitchIpRouterDiscoveryAdvertisementAddress,
       "hmAgentSwitchIpVlanTable": hmAgentSwitchIpVlanTable,
       "hmAgentSwitchIpVlanEntry": hmAgentSwitchIpVlanEntry,
       "hmAgentSwitchIpVlanId": hmAgentSwitchIpVlanId,
       "hmAgentSwitchIpVlanIfIndex": hmAgentSwitchIpVlanIfIndex,
       "hmAgentSwitchIpVlanRoutingStatus": hmAgentSwitchIpVlanRoutingStatus,
       "hmAgentSwitchSecondaryAddressTable": hmAgentSwitchSecondaryAddressTable,
       "hmAgentSwitchSecondaryAddressEntry": hmAgentSwitchSecondaryAddressEntry,
       "hmAgentSwitchSecondaryIpAddress": hmAgentSwitchSecondaryIpAddress,
       "hmAgentSwitchSecondaryNetMask": hmAgentSwitchSecondaryNetMask,
       "hmAgentSwitchSecondaryStatus": hmAgentSwitchSecondaryStatus,
       "hmAgentSwitchIpRoutePreferenceTable": hmAgentSwitchIpRoutePreferenceTable,
       "hmAgentSwitchIpRoutePreferenceEntry": hmAgentSwitchIpRoutePreferenceEntry,
       "hmAgentSwitchIpRoutePreferenceSource": hmAgentSwitchIpRoutePreferenceSource,
       "hmAgentSwitchIpRoutePreferenceValue": hmAgentSwitchIpRoutePreferenceValue,
       "hmAgentSwitchIpRouteStaticTable": hmAgentSwitchIpRouteStaticTable,
       "hmAgentSwitchIpRouteStaticEntry": hmAgentSwitchIpRouteStaticEntry,
       "hmAgentSwitchIpRouteStaticDestination": hmAgentSwitchIpRouteStaticDestination,
       "hmAgentSwitchIpRouteStaticDestinationMask": hmAgentSwitchIpRouteStaticDestinationMask,
       "hmAgentSwitchIpRouteStaticNextHop": hmAgentSwitchIpRouteStaticNextHop,
       "hmAgentSwitchIpRouteStaticPreference": hmAgentSwitchIpRouteStaticPreference,
       "hmAgentSwitchIpRouteStaticStatus": hmAgentSwitchIpRouteStaticStatus,
       "hmAgentSwitchIpRouteStaticTrackId": hmAgentSwitchIpRouteStaticTrackId,
       "hmAgentSwitchIpVlanSingleMacMode": hmAgentSwitchIpVlanSingleMacMode,
       "hmAgentSwitchIpTableSizesGroup": hmAgentSwitchIpTableSizesGroup,
       "hmAgentSwitchIpTableSizeArp": hmAgentSwitchIpTableSizeArp,
       "hmAgentSwitchIpTableSizeUCRoutes": hmAgentSwitchIpTableSizeUCRoutes,
       "hmAgentSwitchIpTableSizeMCRoutes": hmAgentSwitchIpTableSizeMCRoutes,
       "hmAgentSwitchIpCurrentTableSizeArp": hmAgentSwitchIpCurrentTableSizeArp,
       "hmAgentSwitchIpCurrentTableSizeUCRoutes": hmAgentSwitchIpCurrentTableSizeUCRoutes,
       "hmAgentSwitchIpCurrentTableSizeMCRoutes": hmAgentSwitchIpCurrentTableSizeMCRoutes,
       "hmAgentRouterRipConfigGroup": hmAgentRouterRipConfigGroup,
       "hmAgentRouterRipAdminState": hmAgentRouterRipAdminState,
       "hmAgentRouterRipSplitHorizonMode": hmAgentRouterRipSplitHorizonMode,
       "hmAgentRouterRipAutoSummaryMode": hmAgentRouterRipAutoSummaryMode,
       "hmAgentRouterRipHostRoutesAcceptMode": hmAgentRouterRipHostRoutesAcceptMode,
       "hmAgentRouterRipDefaultMetric": hmAgentRouterRipDefaultMetric,
       "hmAgentRouterRipDefaultMetricConfigured": hmAgentRouterRipDefaultMetricConfigured,
       "hmAgentRouterRipDefaultInfoOriginate": hmAgentRouterRipDefaultInfoOriginate,
       "hmAgentRipRouteRedistTable": hmAgentRipRouteRedistTable,
       "hmAgentRipRouteRedistEntry": hmAgentRipRouteRedistEntry,
       "hmAgentRipRouteRedistSource": hmAgentRipRouteRedistSource,
       "hmAgentRipRouteRedistMode": hmAgentRipRouteRedistMode,
       "hmAgentRipRouteRedistMetric": hmAgentRipRouteRedistMetric,
       "hmAgentRipRouteRedistMetricConfigured": hmAgentRipRouteRedistMetricConfigured,
       "hmAgentRipRouteRedistMatchInternal": hmAgentRipRouteRedistMatchInternal,
       "hmAgentRipRouteRedistMatchExternal1": hmAgentRipRouteRedistMatchExternal1,
       "hmAgentRipRouteRedistMatchExternal2": hmAgentRipRouteRedistMatchExternal2,
       "hmAgentRipRouteRedistMatchNSSAExternal1": hmAgentRipRouteRedistMatchNSSAExternal1,
       "hmAgentRipRouteRedistMatchNSSAExternal2": hmAgentRipRouteRedistMatchNSSAExternal2,
       "hmAgentRipRouteRedistDistList": hmAgentRipRouteRedistDistList,
       "hmAgentRipRouteRedistDistListConfigured": hmAgentRipRouteRedistDistListConfigured,
       "hmAgentRip2IfConfTable": hmAgentRip2IfConfTable,
       "hmAgentRip2IfConfEntry": hmAgentRip2IfConfEntry,
       "hmAgentRip2IfConfAuthKeyId": hmAgentRip2IfConfAuthKeyId,
       "hmAgentRip2InterfaceTable": hmAgentRip2InterfaceTable,
       "hmAgentRip2InterfaceEntry": hmAgentRip2InterfaceEntry,
       "hmAgentRip2InterfaceIfIndex": hmAgentRip2InterfaceIfIndex,
       "hmAgentRip2InterfaceAuthType": hmAgentRip2InterfaceAuthType,
       "hmAgentRip2InterfaceAuthKey": hmAgentRip2InterfaceAuthKey,
       "hmAgentRip2InterfaceAuthKeyId": hmAgentRip2InterfaceAuthKeyId,
       "hmAgentRip2InterfaceSendVersion": hmAgentRip2InterfaceSendVersion,
       "hmAgentRip2InterfaceReceiveVersion": hmAgentRip2InterfaceReceiveVersion,
       "hmAgentRip2InterfaceAdminState": hmAgentRip2InterfaceAdminState,
       "hmAgentRip2RcvBadPackets": hmAgentRip2RcvBadPackets,
       "hmAgentRip2RcvBadRoutes": hmAgentRip2RcvBadRoutes,
       "hmAgentRip2SentUpdates": hmAgentRip2SentUpdates,
       "hmAgentRouterRipUpdateTimerInterval": hmAgentRouterRipUpdateTimerInterval,
       "hmAgentRouterOspfConfigGroup": hmAgentRouterOspfConfigGroup,
       "hmAgentOspfDefaultMetric": hmAgentOspfDefaultMetric,
       "hmAgentOspfDefaultMetricConfigured": hmAgentOspfDefaultMetricConfigured,
       "hmAgentOspfDefaultInfoOriginate": hmAgentOspfDefaultInfoOriginate,
       "hmAgentOspfDefaultInfoOriginateAlways": hmAgentOspfDefaultInfoOriginateAlways,
       "hmAgentOspfDefaultInfoOriginateMetric": hmAgentOspfDefaultInfoOriginateMetric,
       "hmAgentOspfDefaultInfoOriginateMetricConfigured": hmAgentOspfDefaultInfoOriginateMetricConfigured,
       "hmAgentOspfDefaultInfoOriginateMetricType": hmAgentOspfDefaultInfoOriginateMetricType,
       "hmAgentOspfRouteRedistTable": hmAgentOspfRouteRedistTable,
       "hmAgentOspfRouteRedistEntry": hmAgentOspfRouteRedistEntry,
       "hmAgentOspfRouteRedistSource": hmAgentOspfRouteRedistSource,
       "hmAgentOspfRouteRedistMode": hmAgentOspfRouteRedistMode,
       "hmAgentOspfRouteRedistMetric": hmAgentOspfRouteRedistMetric,
       "hmAgentOspfRouteRedistMetricConfigured": hmAgentOspfRouteRedistMetricConfigured,
       "hmAgentOspfRouteRedistMetricType": hmAgentOspfRouteRedistMetricType,
       "hmAgentOspfRouteRedistTag": hmAgentOspfRouteRedistTag,
       "hmAgentOspfRouteRedistSubnets": hmAgentOspfRouteRedistSubnets,
       "hmAgentOspfRouteRedistDistList": hmAgentOspfRouteRedistDistList,
       "hmAgentOspfRouteRedistDistListConfigured": hmAgentOspfRouteRedistDistListConfigured,
       "hmAgentOspfIfTable": hmAgentOspfIfTable,
       "hmAgentOspfIfEntry": hmAgentOspfIfEntry,
       "hmAgentOspfIfAuthKeyId": hmAgentOspfIfAuthKeyId,
       "hmAgentOspfIfIpMtuIgnoreFlag": hmAgentOspfIfIpMtuIgnoreFlag,
       "hmAgentOspfVirtIfTable": hmAgentOspfVirtIfTable,
       "hmAgentOspfVirtIfEntry": hmAgentOspfVirtIfEntry,
       "hmAgentOspfVirtIfAuthKeyId": hmAgentOspfVirtIfAuthKeyId,
       "hmAgentRouterOspfRFC1583CompatibilityMode": hmAgentRouterOspfRFC1583CompatibilityMode,
       "hmAgentSnmpTrapFlagsConfigGroupLayer3": hmAgentSnmpTrapFlagsConfigGroupLayer3,
       "hmAgentSnmpVRRPNewMasterTrapFlag": hmAgentSnmpVRRPNewMasterTrapFlag,
       "hmAgentSnmpVRRPAuthFailureTrapFlag": hmAgentSnmpVRRPAuthFailureTrapFlag,
       "hmAgentECMPGroup": hmAgentECMPGroup,
       "hmAgentECMPOspfMaxPaths": hmAgentECMPOspfMaxPaths,
       "hmAgentRouterVrrpConfigGroup": hmAgentRouterVrrpConfigGroup,
       "hmAgentRouterVrrpAdminState": hmAgentRouterVrrpAdminState,
       "hmVrrpExtGroup": hmVrrpExtGroup,
       "hmVrrpTrackingTable": hmVrrpTrackingTable,
       "hmVrrpTrackingEntry": hmVrrpTrackingEntry,
       "hmVrrpTrackIfIndex": hmVrrpTrackIfIndex,
       "hmVrrpTrackVrid": hmVrrpTrackVrid,
       "hmVrrpTrackId": hmVrrpTrackId,
       "hmVrrpTrackDecrement": hmVrrpTrackDecrement,
       "hmVrrpTrackOperStatus": hmVrrpTrackOperStatus,
       "hmVrrpTrackRowStatus": hmVrrpTrackRowStatus,
       "hmVrrpExtTable": hmVrrpExtTable,
       "hmVrrpExtEntry": hmVrrpExtEntry,
       "hmVrrpExtIfIndex": hmVrrpExtIfIndex,
       "hmVrrpExtVrid": hmVrrpExtVrid,
       "hmVrrpExtDomainId": hmVrrpExtDomainId,
       "hmVrrpExtDomainRole": hmVrrpExtDomainRole,
       "hmVrrpExtDomainStatus": hmVrrpExtDomainStatus,
       "hmVrrpExtAdvertAddress": hmVrrpExtAdvertAddress,
       "hmVrrpExtAdvertTimer": hmVrrpExtAdvertTimer,
       "hmVrrpExtOperPriority": hmVrrpExtOperPriority,
       "hmVrrpExtNotifyAddress": hmVrrpExtNotifyAddress,
       "hmVrrpExtNotifyLinkdown": hmVrrpExtNotifyLinkdown,
       "hmVrrpExtPreemptionDelay": hmVrrpExtPreemptionDelay,
       "hmVrrpDomainTable": hmVrrpDomainTable,
       "hmVrrpDomainEntry": hmVrrpDomainEntry,
       "hmVrrpDomainId": hmVrrpDomainId,
       "hmVrrpDomainMemberSendAdv": hmVrrpDomainMemberSendAdv,
       "hmVrrpDomainStatus": hmVrrpDomainStatus,
       "hmVrrpDomainSupervisorIfIndex": hmVrrpDomainSupervisorIfIndex,
       "hmVrrpDomainSupervisorVrid": hmVrrpDomainSupervisorVrid,
       "hmVrrpDomainOperPriority": hmVrrpDomainOperPriority,
       "hmVrrpDomainSupervisorOperState": hmVrrpDomainSupervisorOperState}
)
