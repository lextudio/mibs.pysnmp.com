# SNMP MIB module (CT-FASTPATH-DHCPSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-FASTPATH-DHCPSNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:12 2024
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

(ctDhcpSnoopingExpMib,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctDhcpSnoopingExpMib")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ctFastPathDHCPSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtAgentDhcpSnoopingConfigGroup_ObjectIdentity = ObjectIdentity
ctAgentDhcpSnoopingConfigGroup = _CtAgentDhcpSnoopingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1)
)


class _CtAgentDhcpSnoopingAdminMode_Type(TruthValue):
    """Custom type ctAgentDhcpSnoopingAdminMode based on TruthValue"""


_CtAgentDhcpSnoopingAdminMode_Object = MibScalar
ctAgentDhcpSnoopingAdminMode = _CtAgentDhcpSnoopingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 1),
    _CtAgentDhcpSnoopingAdminMode_Type()
)
ctAgentDhcpSnoopingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingAdminMode.setStatus("current")


class _CtAgentDhcpSnoopingVerifyMac_Type(TruthValue):
    """Custom type ctAgentDhcpSnoopingVerifyMac based on TruthValue"""


_CtAgentDhcpSnoopingVerifyMac_Object = MibScalar
ctAgentDhcpSnoopingVerifyMac = _CtAgentDhcpSnoopingVerifyMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 2),
    _CtAgentDhcpSnoopingVerifyMac_Type()
)
ctAgentDhcpSnoopingVerifyMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingVerifyMac.setStatus("current")
_CtAgentDhcpSnoopingVlanConfigTable_Object = MibTable
ctAgentDhcpSnoopingVlanConfigTable = _CtAgentDhcpSnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingVlanConfigTable.setStatus("current")
_CtAgentDhcpSnoopingVlanConfigEntry_Object = MibTableRow
ctAgentDhcpSnoopingVlanConfigEntry = _CtAgentDhcpSnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 3, 1)
)
ctAgentDhcpSnoopingVlanConfigEntry.setIndexNames(
    (0, "CT-FASTPATH-DHCPSNOOPING-MIB", "ctAgentDhcpSnoopingVlanIndex"),
)
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingVlanConfigEntry.setStatus("current")
_CtAgentDhcpSnoopingVlanIndex_Type = VlanIndex
_CtAgentDhcpSnoopingVlanIndex_Object = MibTableColumn
ctAgentDhcpSnoopingVlanIndex = _CtAgentDhcpSnoopingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 3, 1, 1),
    _CtAgentDhcpSnoopingVlanIndex_Type()
)
ctAgentDhcpSnoopingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingVlanIndex.setStatus("current")


class _CtAgentDhcpSnoopingVlanEnable_Type(TruthValue):
    """Custom type ctAgentDhcpSnoopingVlanEnable based on TruthValue"""


_CtAgentDhcpSnoopingVlanEnable_Object = MibTableColumn
ctAgentDhcpSnoopingVlanEnable = _CtAgentDhcpSnoopingVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 3, 1, 2),
    _CtAgentDhcpSnoopingVlanEnable_Type()
)
ctAgentDhcpSnoopingVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingVlanEnable.setStatus("current")
_CtAgentDhcpSnoopingIfConfigTable_Object = MibTable
ctAgentDhcpSnoopingIfConfigTable = _CtAgentDhcpSnoopingIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingIfConfigTable.setStatus("current")
_CtAgentDhcpSnoopingIfConfigEntry_Object = MibTableRow
ctAgentDhcpSnoopingIfConfigEntry = _CtAgentDhcpSnoopingIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 4, 1)
)
ctAgentDhcpSnoopingIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingIfConfigEntry.setStatus("current")


class _CtAgentDhcpSnoopingIfTrustEnable_Type(TruthValue):
    """Custom type ctAgentDhcpSnoopingIfTrustEnable based on TruthValue"""


_CtAgentDhcpSnoopingIfTrustEnable_Object = MibTableColumn
ctAgentDhcpSnoopingIfTrustEnable = _CtAgentDhcpSnoopingIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 4, 1, 1),
    _CtAgentDhcpSnoopingIfTrustEnable_Type()
)
ctAgentDhcpSnoopingIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingIfTrustEnable.setStatus("current")


class _CtAgentDhcpSnoopingIfLogEnable_Type(TruthValue):
    """Custom type ctAgentDhcpSnoopingIfLogEnable based on TruthValue"""


_CtAgentDhcpSnoopingIfLogEnable_Object = MibTableColumn
ctAgentDhcpSnoopingIfLogEnable = _CtAgentDhcpSnoopingIfLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 4, 1, 2),
    _CtAgentDhcpSnoopingIfLogEnable_Type()
)
ctAgentDhcpSnoopingIfLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingIfLogEnable.setStatus("current")


class _CtAgentDhcpSnoopingIfRateLimit_Type(Unsigned32):
    """Custom type ctAgentDhcpSnoopingIfRateLimit based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CtAgentDhcpSnoopingIfRateLimit_Type.__name__ = "Unsigned32"
_CtAgentDhcpSnoopingIfRateLimit_Object = MibTableColumn
ctAgentDhcpSnoopingIfRateLimit = _CtAgentDhcpSnoopingIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 4, 1, 3),
    _CtAgentDhcpSnoopingIfRateLimit_Type()
)
ctAgentDhcpSnoopingIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingIfRateLimit.setUnits("packets per second")


class _CtAgentDhcpSnoopingIfBurstInterval_Type(Unsigned32):
    """Custom type ctAgentDhcpSnoopingIfBurstInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CtAgentDhcpSnoopingIfBurstInterval_Type.__name__ = "Unsigned32"
_CtAgentDhcpSnoopingIfBurstInterval_Object = MibTableColumn
ctAgentDhcpSnoopingIfBurstInterval = _CtAgentDhcpSnoopingIfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 4, 1, 4),
    _CtAgentDhcpSnoopingIfBurstInterval_Type()
)
ctAgentDhcpSnoopingIfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingIfBurstInterval.setStatus("current")


class _CtAgentDhcpSnoopingStatsReset_Type(Integer32):
    """Custom type ctAgentDhcpSnoopingStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_CtAgentDhcpSnoopingStatsReset_Type.__name__ = "Integer32"
_CtAgentDhcpSnoopingStatsReset_Object = MibScalar
ctAgentDhcpSnoopingStatsReset = _CtAgentDhcpSnoopingStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 6),
    _CtAgentDhcpSnoopingStatsReset_Type()
)
ctAgentDhcpSnoopingStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingStatsReset.setStatus("current")
_CtAgentDhcpSnoopingStatsTable_Object = MibTable
ctAgentDhcpSnoopingStatsTable = _CtAgentDhcpSnoopingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingStatsTable.setStatus("current")
_CtAgentDhcpSnoopingStatsEntry_Object = MibTableRow
ctAgentDhcpSnoopingStatsEntry = _CtAgentDhcpSnoopingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 7, 1)
)
ctAgentDhcpSnoopingStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingStatsEntry.setStatus("current")
_CtAgentDhcpSnoopingMacVerifyFailures_Type = Counter32
_CtAgentDhcpSnoopingMacVerifyFailures_Object = MibTableColumn
ctAgentDhcpSnoopingMacVerifyFailures = _CtAgentDhcpSnoopingMacVerifyFailures_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 7, 1, 1),
    _CtAgentDhcpSnoopingMacVerifyFailures_Type()
)
ctAgentDhcpSnoopingMacVerifyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingMacVerifyFailures.setStatus("current")
_CtAgentDhcpSnoopingInvalidClientMessages_Type = Counter32
_CtAgentDhcpSnoopingInvalidClientMessages_Object = MibTableColumn
ctAgentDhcpSnoopingInvalidClientMessages = _CtAgentDhcpSnoopingInvalidClientMessages_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 7, 1, 2),
    _CtAgentDhcpSnoopingInvalidClientMessages_Type()
)
ctAgentDhcpSnoopingInvalidClientMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingInvalidClientMessages.setStatus("current")
_CtAgentDhcpSnoopingInvalidServerMessages_Type = Counter32
_CtAgentDhcpSnoopingInvalidServerMessages_Object = MibTableColumn
ctAgentDhcpSnoopingInvalidServerMessages = _CtAgentDhcpSnoopingInvalidServerMessages_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 7, 1, 3),
    _CtAgentDhcpSnoopingInvalidServerMessages_Type()
)
ctAgentDhcpSnoopingInvalidServerMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpSnoopingInvalidServerMessages.setStatus("current")
_CtAgentStaticDsBindingTable_Object = MibTable
ctAgentStaticDsBindingTable = _CtAgentStaticDsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ctAgentStaticDsBindingTable.setStatus("current")
_CtAgentStaticDsBinding_Object = MibTableRow
ctAgentStaticDsBinding = _CtAgentStaticDsBinding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 10, 1)
)
ctAgentStaticDsBinding.setIndexNames(
    (0, "CT-FASTPATH-DHCPSNOOPING-MIB", "ctAgentStaticDsBindingMacAddr"),
)
if mibBuilder.loadTexts:
    ctAgentStaticDsBinding.setStatus("current")
_CtAgentStaticDsBindingIfIndex_Type = InterfaceIndex
_CtAgentStaticDsBindingIfIndex_Object = MibTableColumn
ctAgentStaticDsBindingIfIndex = _CtAgentStaticDsBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 10, 1, 1),
    _CtAgentStaticDsBindingIfIndex_Type()
)
ctAgentStaticDsBindingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentStaticDsBindingIfIndex.setStatus("current")
_CtAgentStaticDsBindingVlanId_Type = VlanIndex
_CtAgentStaticDsBindingVlanId_Object = MibTableColumn
ctAgentStaticDsBindingVlanId = _CtAgentStaticDsBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 10, 1, 2),
    _CtAgentStaticDsBindingVlanId_Type()
)
ctAgentStaticDsBindingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentStaticDsBindingVlanId.setStatus("current")
_CtAgentStaticDsBindingMacAddr_Type = MacAddress
_CtAgentStaticDsBindingMacAddr_Object = MibTableColumn
ctAgentStaticDsBindingMacAddr = _CtAgentStaticDsBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 10, 1, 3),
    _CtAgentStaticDsBindingMacAddr_Type()
)
ctAgentStaticDsBindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentStaticDsBindingMacAddr.setStatus("current")
_CtAgentStaticDsBindingIpAddr_Type = IpAddress
_CtAgentStaticDsBindingIpAddr_Object = MibTableColumn
ctAgentStaticDsBindingIpAddr = _CtAgentStaticDsBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 10, 1, 4),
    _CtAgentStaticDsBindingIpAddr_Type()
)
ctAgentStaticDsBindingIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentStaticDsBindingIpAddr.setStatus("current")
_CtAgentStaticDsBindingRowStatus_Type = RowStatus
_CtAgentStaticDsBindingRowStatus_Object = MibTableColumn
ctAgentStaticDsBindingRowStatus = _CtAgentStaticDsBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 10, 1, 5),
    _CtAgentStaticDsBindingRowStatus_Type()
)
ctAgentStaticDsBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentStaticDsBindingRowStatus.setStatus("current")
_CtAgentDynamicDsBindingTable_Object = MibTable
ctAgentDynamicDsBindingTable = _CtAgentDynamicDsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 11)
)
if mibBuilder.loadTexts:
    ctAgentDynamicDsBindingTable.setStatus("current")
_CtAgentDynamicDsBinding_Object = MibTableRow
ctAgentDynamicDsBinding = _CtAgentDynamicDsBinding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 11, 11)
)
ctAgentDynamicDsBinding.setIndexNames(
    (0, "CT-FASTPATH-DHCPSNOOPING-MIB", "ctAgentDynamicDsBindingMacAddr"),
)
if mibBuilder.loadTexts:
    ctAgentDynamicDsBinding.setStatus("current")
_CtAgentDynamicDsBindingIfIndex_Type = InterfaceIndex
_CtAgentDynamicDsBindingIfIndex_Object = MibTableColumn
ctAgentDynamicDsBindingIfIndex = _CtAgentDynamicDsBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 11, 11, 1),
    _CtAgentDynamicDsBindingIfIndex_Type()
)
ctAgentDynamicDsBindingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDynamicDsBindingIfIndex.setStatus("current")
_CtAgentDynamicDsBindingVlanId_Type = VlanIndex
_CtAgentDynamicDsBindingVlanId_Object = MibTableColumn
ctAgentDynamicDsBindingVlanId = _CtAgentDynamicDsBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 11, 11, 2),
    _CtAgentDynamicDsBindingVlanId_Type()
)
ctAgentDynamicDsBindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDynamicDsBindingVlanId.setStatus("current")
_CtAgentDynamicDsBindingMacAddr_Type = MacAddress
_CtAgentDynamicDsBindingMacAddr_Object = MibTableColumn
ctAgentDynamicDsBindingMacAddr = _CtAgentDynamicDsBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 11, 11, 3),
    _CtAgentDynamicDsBindingMacAddr_Type()
)
ctAgentDynamicDsBindingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDynamicDsBindingMacAddr.setStatus("current")
_CtAgentDynamicDsBindingIpAddr_Type = IpAddress
_CtAgentDynamicDsBindingIpAddr_Object = MibTableColumn
ctAgentDynamicDsBindingIpAddr = _CtAgentDynamicDsBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 11, 11, 4),
    _CtAgentDynamicDsBindingIpAddr_Type()
)
ctAgentDynamicDsBindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDynamicDsBindingIpAddr.setStatus("current")

# Managed Objects groups


# Notification objects

ctDhcpSnoopingIntfErrorDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35, 1, 1, 12)
)
ctDhcpSnoopingIntfErrorDisabledTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ctDhcpSnoopingIntfErrorDisabledTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-FASTPATH-DHCPSNOOPING-MIB",
    **{"ctFastPathDHCPSnoopingMIB": ctFastPathDHCPSnoopingMIB,
       "ctAgentDhcpSnoopingConfigGroup": ctAgentDhcpSnoopingConfigGroup,
       "ctAgentDhcpSnoopingAdminMode": ctAgentDhcpSnoopingAdminMode,
       "ctAgentDhcpSnoopingVerifyMac": ctAgentDhcpSnoopingVerifyMac,
       "ctAgentDhcpSnoopingVlanConfigTable": ctAgentDhcpSnoopingVlanConfigTable,
       "ctAgentDhcpSnoopingVlanConfigEntry": ctAgentDhcpSnoopingVlanConfigEntry,
       "ctAgentDhcpSnoopingVlanIndex": ctAgentDhcpSnoopingVlanIndex,
       "ctAgentDhcpSnoopingVlanEnable": ctAgentDhcpSnoopingVlanEnable,
       "ctAgentDhcpSnoopingIfConfigTable": ctAgentDhcpSnoopingIfConfigTable,
       "ctAgentDhcpSnoopingIfConfigEntry": ctAgentDhcpSnoopingIfConfigEntry,
       "ctAgentDhcpSnoopingIfTrustEnable": ctAgentDhcpSnoopingIfTrustEnable,
       "ctAgentDhcpSnoopingIfLogEnable": ctAgentDhcpSnoopingIfLogEnable,
       "ctAgentDhcpSnoopingIfRateLimit": ctAgentDhcpSnoopingIfRateLimit,
       "ctAgentDhcpSnoopingIfBurstInterval": ctAgentDhcpSnoopingIfBurstInterval,
       "ctAgentDhcpSnoopingStatsReset": ctAgentDhcpSnoopingStatsReset,
       "ctAgentDhcpSnoopingStatsTable": ctAgentDhcpSnoopingStatsTable,
       "ctAgentDhcpSnoopingStatsEntry": ctAgentDhcpSnoopingStatsEntry,
       "ctAgentDhcpSnoopingMacVerifyFailures": ctAgentDhcpSnoopingMacVerifyFailures,
       "ctAgentDhcpSnoopingInvalidClientMessages": ctAgentDhcpSnoopingInvalidClientMessages,
       "ctAgentDhcpSnoopingInvalidServerMessages": ctAgentDhcpSnoopingInvalidServerMessages,
       "ctAgentStaticDsBindingTable": ctAgentStaticDsBindingTable,
       "ctAgentStaticDsBinding": ctAgentStaticDsBinding,
       "ctAgentStaticDsBindingIfIndex": ctAgentStaticDsBindingIfIndex,
       "ctAgentStaticDsBindingVlanId": ctAgentStaticDsBindingVlanId,
       "ctAgentStaticDsBindingMacAddr": ctAgentStaticDsBindingMacAddr,
       "ctAgentStaticDsBindingIpAddr": ctAgentStaticDsBindingIpAddr,
       "ctAgentStaticDsBindingRowStatus": ctAgentStaticDsBindingRowStatus,
       "ctAgentDynamicDsBindingTable": ctAgentDynamicDsBindingTable,
       "ctAgentDynamicDsBinding": ctAgentDynamicDsBinding,
       "ctAgentDynamicDsBindingIfIndex": ctAgentDynamicDsBindingIfIndex,
       "ctAgentDynamicDsBindingVlanId": ctAgentDynamicDsBindingVlanId,
       "ctAgentDynamicDsBindingMacAddr": ctAgentDynamicDsBindingMacAddr,
       "ctAgentDynamicDsBindingIpAddr": ctAgentDynamicDsBindingIpAddr,
       "ctDhcpSnoopingIntfErrorDisabledTrap": ctDhcpSnoopingIntfErrorDisabledTrap}
)
