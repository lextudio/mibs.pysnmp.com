# SNMP MIB module (MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:07 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(quanta,
 switch) = mibBuilder.importSymbols(
    "QUANTA-SWITCH-MIB",
    "quanta",
    "switch")

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


# MODULE-IDENTITY

multicast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4)
)
multicast.setRevisions(
        ("2011-08-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentMulticastIGMPConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastIGMPConfigGroup = _AgentMulticastIGMPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1)
)


class _AgentMulticastIGMPAdminMode_Type(Integer32):
    """Custom type agentMulticastIGMPAdminMode based on Integer32"""
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


_AgentMulticastIGMPAdminMode_Type.__name__ = "Integer32"
_AgentMulticastIGMPAdminMode_Object = MibScalar
agentMulticastIGMPAdminMode = _AgentMulticastIGMPAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 1),
    _AgentMulticastIGMPAdminMode_Type()
)
agentMulticastIGMPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIGMPAdminMode.setStatus("current")
_AgentMulticastIGMPInterfaceTable_Object = MibTable
agentMulticastIGMPInterfaceTable = _AgentMulticastIGMPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceTable.setStatus("obsolete")
_AgentMulticastIGMPInterfaceEntry_Object = MibTableRow
agentMulticastIGMPInterfaceEntry = _AgentMulticastIGMPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 2, 1)
)
agentMulticastIGMPInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastIGMPInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceEntry.setStatus("obsolete")


class _AgentMulticastIGMPInterfaceIfIndex_Type(Integer32):
    """Custom type agentMulticastIGMPInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentMulticastIGMPInterfaceIfIndex_Type.__name__ = "Integer32"
_AgentMulticastIGMPInterfaceIfIndex_Object = MibTableColumn
agentMulticastIGMPInterfaceIfIndex = _AgentMulticastIGMPInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 2, 1, 1),
    _AgentMulticastIGMPInterfaceIfIndex_Type()
)
agentMulticastIGMPInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceIfIndex.setStatus("obsolete")


class _AgentMulticastIGMPInterfaceAdminMode_Type(Integer32):
    """Custom type agentMulticastIGMPInterfaceAdminMode based on Integer32"""
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


_AgentMulticastIGMPInterfaceAdminMode_Type.__name__ = "Integer32"
_AgentMulticastIGMPInterfaceAdminMode_Object = MibTableColumn
agentMulticastIGMPInterfaceAdminMode = _AgentMulticastIGMPInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 2, 1, 2),
    _AgentMulticastIGMPInterfaceAdminMode_Type()
)
agentMulticastIGMPInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceAdminMode.setStatus("obsolete")
_AgentMulticastIGMPProxyInterfaceTable_Object = MibTable
agentMulticastIGMPProxyInterfaceTable = _AgentMulticastIGMPProxyInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    agentMulticastIGMPProxyInterfaceTable.setStatus("obsolete")
_AgentMulticastIGMPProxyInterfaceEntry_Object = MibTableRow
agentMulticastIGMPProxyInterfaceEntry = _AgentMulticastIGMPProxyInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 3, 1)
)
agentMulticastIGMPProxyInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastIGMPProxyInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastIGMPProxyInterfaceEntry.setStatus("obsolete")


class _AgentMulticastIGMPProxyInterfaceIfIndex_Type(Integer32):
    """Custom type agentMulticastIGMPProxyInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentMulticastIGMPProxyInterfaceIfIndex_Type.__name__ = "Integer32"
_AgentMulticastIGMPProxyInterfaceIfIndex_Object = MibTableColumn
agentMulticastIGMPProxyInterfaceIfIndex = _AgentMulticastIGMPProxyInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 3, 1, 1),
    _AgentMulticastIGMPProxyInterfaceIfIndex_Type()
)
agentMulticastIGMPProxyInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMulticastIGMPProxyInterfaceIfIndex.setStatus("obsolete")


class _AgentMulticastIGMPProxyInterfaceAdminMode_Type(Integer32):
    """Custom type agentMulticastIGMPProxyInterfaceAdminMode based on Integer32"""
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


_AgentMulticastIGMPProxyInterfaceAdminMode_Type.__name__ = "Integer32"
_AgentMulticastIGMPProxyInterfaceAdminMode_Object = MibTableColumn
agentMulticastIGMPProxyInterfaceAdminMode = _AgentMulticastIGMPProxyInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 3, 1, 2),
    _AgentMulticastIGMPProxyInterfaceAdminMode_Type()
)
agentMulticastIGMPProxyInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIGMPProxyInterfaceAdminMode.setStatus("obsolete")


class _AgentMulticastIGMPProxyInterfaceInterval_Type(Integer32):
    """Custom type agentMulticastIGMPProxyInterfaceInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 260),
    )


_AgentMulticastIGMPProxyInterfaceInterval_Type.__name__ = "Integer32"
_AgentMulticastIGMPProxyInterfaceInterval_Object = MibTableColumn
agentMulticastIGMPProxyInterfaceInterval = _AgentMulticastIGMPProxyInterfaceInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 1, 3, 1, 3),
    _AgentMulticastIGMPProxyInterfaceInterval_Type()
)
agentMulticastIGMPProxyInterfaceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIGMPProxyInterfaceInterval.setStatus("obsolete")
_AgentMulticastPIMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastPIMConfigGroup = _AgentMulticastPIMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 2)
)


class _AgentMulticastPIMConfigMode_Type(Integer32):
    """Custom type agentMulticastPIMConfigMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 2),
          ("none", 0),
          ("sparse", 1))
    )


_AgentMulticastPIMConfigMode_Type.__name__ = "Integer32"
_AgentMulticastPIMConfigMode_Object = MibScalar
agentMulticastPIMConfigMode = _AgentMulticastPIMConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 2, 1),
    _AgentMulticastPIMConfigMode_Type()
)
agentMulticastPIMConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMulticastPIMConfigMode.setStatus("obsolete")
_AgentMulticastPIMSMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastPIMSMConfigGroup = _AgentMulticastPIMSMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3)
)


class _AgentMulticastPIMSMAdminMode_Type(Integer32):
    """Custom type agentMulticastPIMSMAdminMode based on Integer32"""
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


_AgentMulticastPIMSMAdminMode_Type.__name__ = "Integer32"
_AgentMulticastPIMSMAdminMode_Object = MibScalar
agentMulticastPIMSMAdminMode = _AgentMulticastPIMSMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 1),
    _AgentMulticastPIMSMAdminMode_Type()
)
agentMulticastPIMSMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMAdminMode.setStatus("current")


class _AgentMulticastPIMSMDataThresholdRate_Type(Integer32):
    """Custom type agentMulticastPIMSMDataThresholdRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AgentMulticastPIMSMDataThresholdRate_Type.__name__ = "Integer32"
_AgentMulticastPIMSMDataThresholdRate_Object = MibScalar
agentMulticastPIMSMDataThresholdRate = _AgentMulticastPIMSMDataThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 2),
    _AgentMulticastPIMSMDataThresholdRate_Type()
)
agentMulticastPIMSMDataThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMDataThresholdRate.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPTable_Object = MibTable
agentMulticastPIMSMStaticRPTable = _AgentMulticastPIMSMStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 4)
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPTable.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPEntry_Object = MibTableRow
agentMulticastPIMSMStaticRPEntry = _AgentMulticastPIMSMStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 4, 1)
)
agentMulticastPIMSMStaticRPEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastPIMSMStaticRPIpAddr"),
    (0, "MULTICAST-MIB", "agentMulticastPIMSMStaticRPGroupIpAddr"),
    (0, "MULTICAST-MIB", "agentMulticastPIMSMStaticRPGroupIpMask"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPEntry.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPIpAddr_Type = IpAddress
_AgentMulticastPIMSMStaticRPIpAddr_Object = MibTableColumn
agentMulticastPIMSMStaticRPIpAddr = _AgentMulticastPIMSMStaticRPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 4, 1, 1),
    _AgentMulticastPIMSMStaticRPIpAddr_Type()
)
agentMulticastPIMSMStaticRPIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPIpAddr.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPGroupIpAddr_Type = IpAddress
_AgentMulticastPIMSMStaticRPGroupIpAddr_Object = MibTableColumn
agentMulticastPIMSMStaticRPGroupIpAddr = _AgentMulticastPIMSMStaticRPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 4, 1, 2),
    _AgentMulticastPIMSMStaticRPGroupIpAddr_Type()
)
agentMulticastPIMSMStaticRPGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPGroupIpAddr.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPGroupIpMask_Type = IpAddress
_AgentMulticastPIMSMStaticRPGroupIpMask_Object = MibTableColumn
agentMulticastPIMSMStaticRPGroupIpMask = _AgentMulticastPIMSMStaticRPGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 4, 1, 3),
    _AgentMulticastPIMSMStaticRPGroupIpMask_Type()
)
agentMulticastPIMSMStaticRPGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPGroupIpMask.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPStatus_Type = RowStatus
_AgentMulticastPIMSMStaticRPStatus_Object = MibTableColumn
agentMulticastPIMSMStaticRPStatus = _AgentMulticastPIMSMStaticRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 4, 1, 4),
    _AgentMulticastPIMSMStaticRPStatus_Type()
)
agentMulticastPIMSMStaticRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPStatus.setStatus("obsolete")
_AgentMulticastPIMSMCBSRInterfaceTable_Object = MibTable
agentMulticastPIMSMCBSRInterfaceTable = _AgentMulticastPIMSMCBSRInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 5)
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMCBSRInterfaceTable.setStatus("obsolete")
_AgentMulticastPIMSMCBSRInterfaceEntry_Object = MibTableRow
agentMulticastPIMSMCBSRInterfaceEntry = _AgentMulticastPIMSMCBSRInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 5, 1)
)
agentMulticastPIMSMCBSRInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastPIMSMCBSRInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMCBSRInterfaceEntry.setStatus("obsolete")
_AgentMulticastPIMSMCBSRInterfaceIndex_Type = Unsigned32
_AgentMulticastPIMSMCBSRInterfaceIndex_Object = MibTableColumn
agentMulticastPIMSMCBSRInterfaceIndex = _AgentMulticastPIMSMCBSRInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 5, 1, 1),
    _AgentMulticastPIMSMCBSRInterfaceIndex_Type()
)
agentMulticastPIMSMCBSRInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMCBSRInterfaceIndex.setStatus("obsolete")


class _AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Type(Unsigned32):
    """Custom type agentMulticastPIMSMCBSRInterfaceHashMaskLength based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Type.__name__ = "Unsigned32"
_AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Object = MibTableColumn
agentMulticastPIMSMCBSRInterfaceHashMaskLength = _AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 5, 1, 2),
    _AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Type()
)
agentMulticastPIMSMCBSRInterfaceHashMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMCBSRInterfaceHashMaskLength.setStatus("obsolete")


class _AgentMulticastPIMSMCBSRInterfacePriority_Type(Integer32):
    """Custom type agentMulticastPIMSMCBSRInterfacePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AgentMulticastPIMSMCBSRInterfacePriority_Type.__name__ = "Integer32"
_AgentMulticastPIMSMCBSRInterfacePriority_Object = MibTableColumn
agentMulticastPIMSMCBSRInterfacePriority = _AgentMulticastPIMSMCBSRInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 5, 1, 3),
    _AgentMulticastPIMSMCBSRInterfacePriority_Type()
)
agentMulticastPIMSMCBSRInterfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMCBSRInterfacePriority.setStatus("obsolete")
_AgentMulticastPIMSMSSMTable_Object = MibTable
agentMulticastPIMSMSSMTable = _AgentMulticastPIMSMSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 6)
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMSSMTable.setStatus("obsolete")
_AgentMulticastPIMSMSSMEntry_Object = MibTableRow
agentMulticastPIMSMSSMEntry = _AgentMulticastPIMSMSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 6, 1)
)
agentMulticastPIMSMSSMEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastPIMSMSSMGroupAddress"),
    (0, "MULTICAST-MIB", "agentMulticastPIMSMSSMGroupMask"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMSSMEntry.setStatus("obsolete")
_AgentMulticastPIMSMSSMGroupAddress_Type = IpAddress
_AgentMulticastPIMSMSSMGroupAddress_Object = MibTableColumn
agentMulticastPIMSMSSMGroupAddress = _AgentMulticastPIMSMSSMGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 6, 1, 1),
    _AgentMulticastPIMSMSSMGroupAddress_Type()
)
agentMulticastPIMSMSSMGroupAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMSSMGroupAddress.setStatus("obsolete")


class _AgentMulticastPIMSMSSMGroupMask_Type(Unsigned32):
    """Custom type agentMulticastPIMSMSSMGroupMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AgentMulticastPIMSMSSMGroupMask_Type.__name__ = "Unsigned32"
_AgentMulticastPIMSMSSMGroupMask_Object = MibTableColumn
agentMulticastPIMSMSSMGroupMask = _AgentMulticastPIMSMSSMGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 6, 1, 2),
    _AgentMulticastPIMSMSSMGroupMask_Type()
)
agentMulticastPIMSMSSMGroupMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMSSMGroupMask.setStatus("obsolete")


class _AgentMulticastPIMSMSSMStatus_Type(Integer32):
    """Custom type agentMulticastPIMSMSSMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 4),
          ("destory", 6))
    )


_AgentMulticastPIMSMSSMStatus_Type.__name__ = "Integer32"
_AgentMulticastPIMSMSSMStatus_Object = MibTableColumn
agentMulticastPIMSMSSMStatus = _AgentMulticastPIMSMSSMStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 6, 1, 3),
    _AgentMulticastPIMSMSSMStatus_Type()
)
agentMulticastPIMSMSSMStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMSSMStatus.setStatus("obsolete")
_AgentMulticastPIMSMInterfaceTable_Object = MibTable
agentMulticastPIMSMInterfaceTable = _AgentMulticastPIMSMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7)
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceTable.setStatus("obsolete")
_AgentMulticastPIMSMInterfaceEntry_Object = MibTableRow
agentMulticastPIMSMInterfaceEntry = _AgentMulticastPIMSMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7, 1)
)
agentMulticastPIMSMInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastPIMSMInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceEntry.setStatus("obsolete")
_AgentMulticastPIMSMInterfaceIndex_Type = Unsigned32
_AgentMulticastPIMSMInterfaceIndex_Object = MibTableColumn
agentMulticastPIMSMInterfaceIndex = _AgentMulticastPIMSMInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7, 1, 1),
    _AgentMulticastPIMSMInterfaceIndex_Type()
)
agentMulticastPIMSMInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceIndex.setStatus("obsolete")


class _AgentMulticastPIMSMInterfaceAdminMode_Type(Integer32):
    """Custom type agentMulticastPIMSMInterfaceAdminMode based on Integer32"""
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


_AgentMulticastPIMSMInterfaceAdminMode_Type.__name__ = "Integer32"
_AgentMulticastPIMSMInterfaceAdminMode_Object = MibTableColumn
agentMulticastPIMSMInterfaceAdminMode = _AgentMulticastPIMSMInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7, 1, 2),
    _AgentMulticastPIMSMInterfaceAdminMode_Type()
)
agentMulticastPIMSMInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceAdminMode.setStatus("current")


class _AgentMulticastPIMSMInterfaceHelloInterval_Type(Unsigned32):
    """Custom type agentMulticastPIMSMInterfaceHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_AgentMulticastPIMSMInterfaceHelloInterval_Type.__name__ = "Unsigned32"
_AgentMulticastPIMSMInterfaceHelloInterval_Object = MibTableColumn
agentMulticastPIMSMInterfaceHelloInterval = _AgentMulticastPIMSMInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7, 1, 3),
    _AgentMulticastPIMSMInterfaceHelloInterval_Type()
)
agentMulticastPIMSMInterfaceHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceHelloInterval.setStatus("obsolete")


class _AgentMulticastPIMSMInterfaceJoinPruneInterval_Type(Unsigned32):
    """Custom type agentMulticastPIMSMInterfaceJoinPruneInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_AgentMulticastPIMSMInterfaceJoinPruneInterval_Type.__name__ = "Unsigned32"
_AgentMulticastPIMSMInterfaceJoinPruneInterval_Object = MibTableColumn
agentMulticastPIMSMInterfaceJoinPruneInterval = _AgentMulticastPIMSMInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7, 1, 4),
    _AgentMulticastPIMSMInterfaceJoinPruneInterval_Type()
)
agentMulticastPIMSMInterfaceJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceJoinPruneInterval.setStatus("obsolete")


class _AgentMulticastPIMSMInterfaceBsrBorder_Type(Integer32):
    """Custom type agentMulticastPIMSMInterfaceBsrBorder based on Integer32"""
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


_AgentMulticastPIMSMInterfaceBsrBorder_Type.__name__ = "Integer32"
_AgentMulticastPIMSMInterfaceBsrBorder_Object = MibTableColumn
agentMulticastPIMSMInterfaceBsrBorder = _AgentMulticastPIMSMInterfaceBsrBorder_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7, 1, 5),
    _AgentMulticastPIMSMInterfaceBsrBorder_Type()
)
agentMulticastPIMSMInterfaceBsrBorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceBsrBorder.setStatus("current")


class _AgentMulticastPIMSMInterfaceDrPriority_Type(Unsigned32):
    """Custom type agentMulticastPIMSMInterfaceDrPriority based on Unsigned32"""
    defaultValue = 1


_AgentMulticastPIMSMInterfaceDrPriority_Object = MibTableColumn
agentMulticastPIMSMInterfaceDrPriority = _AgentMulticastPIMSMInterfaceDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7, 1, 6),
    _AgentMulticastPIMSMInterfaceDrPriority_Type()
)
agentMulticastPIMSMInterfaceDrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceDrPriority.setStatus("obsolete")


class _AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type(Unsigned32):
    """Custom type agentMulticastPIMSMInterfaceCBSRHashMaskLength based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type.__name__ = "Unsigned32"
_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object = MibTableColumn
agentMulticastPIMSMInterfaceCBSRHashMaskLength = _AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7, 1, 7),
    _AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type()
)
agentMulticastPIMSMInterfaceCBSRHashMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceCBSRHashMaskLength.setStatus("obsolete")


class _AgentMulticastPIMSMInterfaceCRPPreference_Type(Integer32):
    """Custom type agentMulticastPIMSMInterfaceCRPPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AgentMulticastPIMSMInterfaceCRPPreference_Type.__name__ = "Integer32"
_AgentMulticastPIMSMInterfaceCRPPreference_Object = MibTableColumn
agentMulticastPIMSMInterfaceCRPPreference = _AgentMulticastPIMSMInterfaceCRPPreference_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 7, 1, 8),
    _AgentMulticastPIMSMInterfaceCRPPreference_Type()
)
agentMulticastPIMSMInterfaceCRPPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceCRPPreference.setStatus("obsolete")
_AgentMulticastPIMSMCandRPTable_Object = MibTable
agentMulticastPIMSMCandRPTable = _AgentMulticastPIMSMCandRPTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 8)
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMCandRPTable.setStatus("obsolete")
_AgentMulticastPIMSMCandRPEntry_Object = MibTableRow
agentMulticastPIMSMCandRPEntry = _AgentMulticastPIMSMCandRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 8, 1)
)
agentMulticastPIMSMCandRPEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastPIMSMCandRPAddress"),
    (0, "MULTICAST-MIB", "agentMulticastPIMSMCandRPGroupAddress"),
    (0, "MULTICAST-MIB", "agentMulticastPIMSMCandRPGroupPrefixLength"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMCandRPEntry.setStatus("obsolete")
_AgentMulticastPIMSMCandRPAddress_Type = IpAddress
_AgentMulticastPIMSMCandRPAddress_Object = MibTableColumn
agentMulticastPIMSMCandRPAddress = _AgentMulticastPIMSMCandRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 8, 1, 1),
    _AgentMulticastPIMSMCandRPAddress_Type()
)
agentMulticastPIMSMCandRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMCandRPAddress.setStatus("obsolete")
_AgentMulticastPIMSMCandRPGroupAddress_Type = IpAddress
_AgentMulticastPIMSMCandRPGroupAddress_Object = MibTableColumn
agentMulticastPIMSMCandRPGroupAddress = _AgentMulticastPIMSMCandRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 8, 1, 2),
    _AgentMulticastPIMSMCandRPGroupAddress_Type()
)
agentMulticastPIMSMCandRPGroupAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMCandRPGroupAddress.setStatus("obsolete")


class _AgentMulticastPIMSMCandRPGroupPrefixLength_Type(Unsigned32):
    """Custom type agentMulticastPIMSMCandRPGroupPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AgentMulticastPIMSMCandRPGroupPrefixLength_Type.__name__ = "Unsigned32"
_AgentMulticastPIMSMCandRPGroupPrefixLength_Object = MibTableColumn
agentMulticastPIMSMCandRPGroupPrefixLength = _AgentMulticastPIMSMCandRPGroupPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 8, 1, 3),
    _AgentMulticastPIMSMCandRPGroupPrefixLength_Type()
)
agentMulticastPIMSMCandRPGroupPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMCandRPGroupPrefixLength.setStatus("obsolete")


class _AgentMulticastPIMSMCandRPStatus_Type(Integer32):
    """Custom type agentMulticastPIMSMCandRPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 4),
          ("destory", 6))
    )


_AgentMulticastPIMSMCandRPStatus_Type.__name__ = "Integer32"
_AgentMulticastPIMSMCandRPStatus_Object = MibTableColumn
agentMulticastPIMSMCandRPStatus = _AgentMulticastPIMSMCandRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 3, 8, 1, 4),
    _AgentMulticastPIMSMCandRPStatus_Type()
)
agentMulticastPIMSMCandRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMCandRPStatus.setStatus("obsolete")
_AgentMulticastPIMDMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastPIMDMConfigGroup = _AgentMulticastPIMDMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 4)
)


class _AgentMulticastPIMDMAdminMode_Type(Integer32):
    """Custom type agentMulticastPIMDMAdminMode based on Integer32"""
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


_AgentMulticastPIMDMAdminMode_Type.__name__ = "Integer32"
_AgentMulticastPIMDMAdminMode_Object = MibScalar
agentMulticastPIMDMAdminMode = _AgentMulticastPIMDMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 4, 1),
    _AgentMulticastPIMDMAdminMode_Type()
)
agentMulticastPIMDMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMDMAdminMode.setStatus("current")
_AgentMulticastPIMDMInterfaceTable_Object = MibTable
agentMulticastPIMDMInterfaceTable = _AgentMulticastPIMDMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    agentMulticastPIMDMInterfaceTable.setStatus("obsolete")
_AgentMulticastPIMDMInterfaceEntry_Object = MibTableRow
agentMulticastPIMDMInterfaceEntry = _AgentMulticastPIMDMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 4, 2, 1)
)
agentMulticastPIMDMInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastPIMDMInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMDMInterfaceEntry.setStatus("obsolete")
_AgentMulticastPIMDMInterfaceIndex_Type = Unsigned32
_AgentMulticastPIMDMInterfaceIndex_Object = MibTableColumn
agentMulticastPIMDMInterfaceIndex = _AgentMulticastPIMDMInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 4, 2, 1, 1),
    _AgentMulticastPIMDMInterfaceIndex_Type()
)
agentMulticastPIMDMInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMDMInterfaceIndex.setStatus("obsolete")


class _AgentMulticastPIMDMInterfaceMode_Type(Integer32):
    """Custom type agentMulticastPIMDMInterfaceMode based on Integer32"""
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


_AgentMulticastPIMDMInterfaceMode_Type.__name__ = "Integer32"
_AgentMulticastPIMDMInterfaceMode_Object = MibTableColumn
agentMulticastPIMDMInterfaceMode = _AgentMulticastPIMDMInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 4, 2, 1, 2),
    _AgentMulticastPIMDMInterfaceMode_Type()
)
agentMulticastPIMDMInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMDMInterfaceMode.setStatus("obsolete")


class _AgentMulticastPIMDMInterfaceHelloInterval_Type(Integer32):
    """Custom type agentMulticastPIMDMInterfaceHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_AgentMulticastPIMDMInterfaceHelloInterval_Type.__name__ = "Integer32"
_AgentMulticastPIMDMInterfaceHelloInterval_Object = MibTableColumn
agentMulticastPIMDMInterfaceHelloInterval = _AgentMulticastPIMDMInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 4, 2, 1, 3),
    _AgentMulticastPIMDMInterfaceHelloInterval_Type()
)
agentMulticastPIMDMInterfaceHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMDMInterfaceHelloInterval.setStatus("obsolete")
_AgentMulticastRoutingConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastRoutingConfigGroup = _AgentMulticastRoutingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 5)
)


class _AgentMulticastRoutingAdminMode_Type(Integer32):
    """Custom type agentMulticastRoutingAdminMode based on Integer32"""
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


_AgentMulticastRoutingAdminMode_Type.__name__ = "Integer32"
_AgentMulticastRoutingAdminMode_Object = MibScalar
agentMulticastRoutingAdminMode = _AgentMulticastRoutingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 5, 1),
    _AgentMulticastRoutingAdminMode_Type()
)
agentMulticastRoutingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastRoutingAdminMode.setStatus("obsolete")
_AgentMulticastDVMRPConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastDVMRPConfigGroup = _AgentMulticastDVMRPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 6)
)


class _AgentMulticastDVMRPAdminMode_Type(Integer32):
    """Custom type agentMulticastDVMRPAdminMode based on Integer32"""
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


_AgentMulticastDVMRPAdminMode_Type.__name__ = "Integer32"
_AgentMulticastDVMRPAdminMode_Object = MibScalar
agentMulticastDVMRPAdminMode = _AgentMulticastDVMRPAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 6, 1),
    _AgentMulticastDVMRPAdminMode_Type()
)
agentMulticastDVMRPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastDVMRPAdminMode.setStatus("current")
_AgentMulticastDVMRPInterfaceTable_Object = MibTable
agentMulticastDVMRPInterfaceTable = _AgentMulticastDVMRPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 6, 2)
)
if mibBuilder.loadTexts:
    agentMulticastDVMRPInterfaceTable.setStatus("obsolete")
_AgentMulticastDVMRPInterfaceEntry_Object = MibTableRow
agentMulticastDVMRPInterfaceEntry = _AgentMulticastDVMRPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 6, 2, 1)
)
agentMulticastDVMRPInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastDVMRPInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastDVMRPInterfaceEntry.setStatus("obsolete")


class _AgentMulticastDVMRPInterfaceIfIndex_Type(Integer32):
    """Custom type agentMulticastDVMRPInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentMulticastDVMRPInterfaceIfIndex_Type.__name__ = "Integer32"
_AgentMulticastDVMRPInterfaceIfIndex_Object = MibTableColumn
agentMulticastDVMRPInterfaceIfIndex = _AgentMulticastDVMRPInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 6, 2, 1, 1),
    _AgentMulticastDVMRPInterfaceIfIndex_Type()
)
agentMulticastDVMRPInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMulticastDVMRPInterfaceIfIndex.setStatus("obsolete")


class _AgentMulticastDVMRPInterfaceAdminMode_Type(Integer32):
    """Custom type agentMulticastDVMRPInterfaceAdminMode based on Integer32"""
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


_AgentMulticastDVMRPInterfaceAdminMode_Type.__name__ = "Integer32"
_AgentMulticastDVMRPInterfaceAdminMode_Object = MibTableColumn
agentMulticastDVMRPInterfaceAdminMode = _AgentMulticastDVMRPInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 6, 2, 1, 2),
    _AgentMulticastDVMRPInterfaceAdminMode_Type()
)
agentMulticastDVMRPInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastDVMRPInterfaceAdminMode.setStatus("obsolete")


class _AgentMulticastDVMRPInterfaceMetric_Type(Integer32):
    """Custom type agentMulticastDVMRPInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AgentMulticastDVMRPInterfaceMetric_Type.__name__ = "Integer32"
_AgentMulticastDVMRPInterfaceMetric_Object = MibTableColumn
agentMulticastDVMRPInterfaceMetric = _AgentMulticastDVMRPInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 6, 2, 1, 3),
    _AgentMulticastDVMRPInterfaceMetric_Type()
)
agentMulticastDVMRPInterfaceMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastDVMRPInterfaceMetric.setStatus("obsolete")
_AgentMulticastDVMRPInterfaceGenerationId_Type = Integer32
_AgentMulticastDVMRPInterfaceGenerationId_Object = MibTableColumn
agentMulticastDVMRPInterfaceGenerationId = _AgentMulticastDVMRPInterfaceGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 6, 2, 1, 4),
    _AgentMulticastDVMRPInterfaceGenerationId_Type()
)
agentMulticastDVMRPInterfaceGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMulticastDVMRPInterfaceGenerationId.setStatus("obsolete")
_AgentMulticastMLDConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastMLDConfigGroup = _AgentMulticastMLDConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8)
)


class _AgentMulticastMLDAdminMode_Type(Integer32):
    """Custom type agentMulticastMLDAdminMode based on Integer32"""
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


_AgentMulticastMLDAdminMode_Type.__name__ = "Integer32"
_AgentMulticastMLDAdminMode_Object = MibScalar
agentMulticastMLDAdminMode = _AgentMulticastMLDAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 1),
    _AgentMulticastMLDAdminMode_Type()
)
agentMulticastMLDAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastMLDAdminMode.setStatus("current")
_AgentMulticastMLDInterfaceTable_Object = MibTable
agentMulticastMLDInterfaceTable = _AgentMulticastMLDInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 2)
)
if mibBuilder.loadTexts:
    agentMulticastMLDInterfaceTable.setStatus("obsolete")
_AgentMulticastMLDInterfaceEntry_Object = MibTableRow
agentMulticastMLDInterfaceEntry = _AgentMulticastMLDInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 2, 1)
)
agentMulticastMLDInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastMLDInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastMLDInterfaceEntry.setStatus("obsolete")


class _AgentMulticastMLDInterfaceIfIndex_Type(Integer32):
    """Custom type agentMulticastMLDInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentMulticastMLDInterfaceIfIndex_Type.__name__ = "Integer32"
_AgentMulticastMLDInterfaceIfIndex_Object = MibTableColumn
agentMulticastMLDInterfaceIfIndex = _AgentMulticastMLDInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 2, 1, 1),
    _AgentMulticastMLDInterfaceIfIndex_Type()
)
agentMulticastMLDInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMulticastMLDInterfaceIfIndex.setStatus("obsolete")


class _AgentMulticastMLDInterfaceAdminMode_Type(Integer32):
    """Custom type agentMulticastMLDInterfaceAdminMode based on Integer32"""
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


_AgentMulticastMLDInterfaceAdminMode_Type.__name__ = "Integer32"
_AgentMulticastMLDInterfaceAdminMode_Object = MibTableColumn
agentMulticastMLDInterfaceAdminMode = _AgentMulticastMLDInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 2, 1, 2),
    _AgentMulticastMLDInterfaceAdminMode_Type()
)
agentMulticastMLDInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastMLDInterfaceAdminMode.setStatus("obsolete")
_AgentMulticastMLDProxyInterfaceTable_Object = MibTable
agentMulticastMLDProxyInterfaceTable = _AgentMulticastMLDProxyInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 3)
)
if mibBuilder.loadTexts:
    agentMulticastMLDProxyInterfaceTable.setStatus("obsolete")
_AgentMulticastMLDProxyInterfaceEntry_Object = MibTableRow
agentMulticastMLDProxyInterfaceEntry = _AgentMulticastMLDProxyInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 3, 1)
)
agentMulticastMLDProxyInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastMLDProxyInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastMLDProxyInterfaceEntry.setStatus("obsolete")


class _AgentMulticastMLDProxyInterfaceIfIndex_Type(Integer32):
    """Custom type agentMulticastMLDProxyInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentMulticastMLDProxyInterfaceIfIndex_Type.__name__ = "Integer32"
_AgentMulticastMLDProxyInterfaceIfIndex_Object = MibTableColumn
agentMulticastMLDProxyInterfaceIfIndex = _AgentMulticastMLDProxyInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 3, 1, 1),
    _AgentMulticastMLDProxyInterfaceIfIndex_Type()
)
agentMulticastMLDProxyInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMulticastMLDProxyInterfaceIfIndex.setStatus("obsolete")


class _AgentMulticastMLDProxyInterfaceAdminMode_Type(Integer32):
    """Custom type agentMulticastMLDProxyInterfaceAdminMode based on Integer32"""
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


_AgentMulticastMLDProxyInterfaceAdminMode_Type.__name__ = "Integer32"
_AgentMulticastMLDProxyInterfaceAdminMode_Object = MibTableColumn
agentMulticastMLDProxyInterfaceAdminMode = _AgentMulticastMLDProxyInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 3, 1, 2),
    _AgentMulticastMLDProxyInterfaceAdminMode_Type()
)
agentMulticastMLDProxyInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastMLDProxyInterfaceAdminMode.setStatus("obsolete")


class _AgentMulticastMLDProxyInterfaceInterval_Type(Integer32):
    """Custom type agentMulticastMLDProxyInterfaceInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 260),
    )


_AgentMulticastMLDProxyInterfaceInterval_Type.__name__ = "Integer32"
_AgentMulticastMLDProxyInterfaceInterval_Object = MibTableColumn
agentMulticastMLDProxyInterfaceInterval = _AgentMulticastMLDProxyInterfaceInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 8, 3, 1, 3),
    _AgentMulticastMLDProxyInterfaceInterval_Type()
)
agentMulticastMLDProxyInterfaceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastMLDProxyInterfaceInterval.setStatus("obsolete")
_AgentMulticastIPv6PIMSMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastIPv6PIMSMConfigGroup = _AgentMulticastIPv6PIMSMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9)
)


class _AgentMulticastIPv6PIMSMAdminMode_Type(Integer32):
    """Custom type agentMulticastIPv6PIMSMAdminMode based on Integer32"""
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


_AgentMulticastIPv6PIMSMAdminMode_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMSMAdminMode_Object = MibScalar
agentMulticastIPv6PIMSMAdminMode = _AgentMulticastIPv6PIMSMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 1),
    _AgentMulticastIPv6PIMSMAdminMode_Type()
)
agentMulticastIPv6PIMSMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMAdminMode.setStatus("current")


class _AgentMulticastIPv6PIMSMDataThresholdRate_Type(Integer32):
    """Custom type agentMulticastIPv6PIMSMDataThresholdRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AgentMulticastIPv6PIMSMDataThresholdRate_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMSMDataThresholdRate_Object = MibScalar
agentMulticastIPv6PIMSMDataThresholdRate = _AgentMulticastIPv6PIMSMDataThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 2),
    _AgentMulticastIPv6PIMSMDataThresholdRate_Type()
)
agentMulticastIPv6PIMSMDataThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMDataThresholdRate.setStatus("obsolete")
_AgentMulticastIPv6PIMSMStaticRPTable_Object = MibTable
agentMulticastIPv6PIMSMStaticRPTable = _AgentMulticastIPv6PIMSMStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 4)
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMStaticRPTable.setStatus("obsolete")
_AgentMulticastIPv6PIMSMStaticRPEntry_Object = MibTableRow
agentMulticastIPv6PIMSMStaticRPEntry = _AgentMulticastIPv6PIMSMStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 4, 1)
)
agentMulticastIPv6PIMSMStaticRPEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMStaticRPIpAddr"),
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMStaticRPGroupIpAddr"),
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMStaticRPGroupIpPrefix"),
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMStaticRPEntry.setStatus("obsolete")
_AgentMulticastIPv6PIMSMStaticRPIpAddr_Type = Ipv6Address
_AgentMulticastIPv6PIMSMStaticRPIpAddr_Object = MibTableColumn
agentMulticastIPv6PIMSMStaticRPIpAddr = _AgentMulticastIPv6PIMSMStaticRPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 4, 1, 1),
    _AgentMulticastIPv6PIMSMStaticRPIpAddr_Type()
)
agentMulticastIPv6PIMSMStaticRPIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMStaticRPIpAddr.setStatus("obsolete")
_AgentMulticastIPv6PIMSMStaticRPGroupIpAddr_Type = Ipv6Address
_AgentMulticastIPv6PIMSMStaticRPGroupIpAddr_Object = MibTableColumn
agentMulticastIPv6PIMSMStaticRPGroupIpAddr = _AgentMulticastIPv6PIMSMStaticRPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 4, 1, 2),
    _AgentMulticastIPv6PIMSMStaticRPGroupIpAddr_Type()
)
agentMulticastIPv6PIMSMStaticRPGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMStaticRPGroupIpAddr.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Type(Integer32):
    """Custom type agentMulticastIPv6PIMSMStaticRPGroupIpPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Object = MibTableColumn
agentMulticastIPv6PIMSMStaticRPGroupIpPrefix = _AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 4, 1, 3),
    _AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Type()
)
agentMulticastIPv6PIMSMStaticRPGroupIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMStaticRPGroupIpPrefix.setStatus("obsolete")
_AgentMulticastIPv6PIMSMStaticRPStatus_Type = RowStatus
_AgentMulticastIPv6PIMSMStaticRPStatus_Object = MibTableColumn
agentMulticastIPv6PIMSMStaticRPStatus = _AgentMulticastIPv6PIMSMStaticRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 4, 1, 4),
    _AgentMulticastIPv6PIMSMStaticRPStatus_Type()
)
agentMulticastIPv6PIMSMStaticRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMStaticRPStatus.setStatus("obsolete")
_AgentMulticastIPv6PIMSMCBSRInterfaceTable_Object = MibTable
agentMulticastIPv6PIMSMCBSRInterfaceTable = _AgentMulticastIPv6PIMSMCBSRInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 5)
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCBSRInterfaceTable.setStatus("obsolete")
_AgentMulticastIPv6PIMSMCBSRInterfaceEntry_Object = MibTableRow
agentMulticastIPv6PIMSMCBSRInterfaceEntry = _AgentMulticastIPv6PIMSMCBSRInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 5, 1)
)
agentMulticastIPv6PIMSMCBSRInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMCBSRInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCBSRInterfaceEntry.setStatus("obsolete")
_AgentMulticastIPv6PIMSMCBSRInterfaceIndex_Type = Unsigned32
_AgentMulticastIPv6PIMSMCBSRInterfaceIndex_Object = MibTableColumn
agentMulticastIPv6PIMSMCBSRInterfaceIndex = _AgentMulticastIPv6PIMSMCBSRInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 5, 1, 1),
    _AgentMulticastIPv6PIMSMCBSRInterfaceIndex_Type()
)
agentMulticastIPv6PIMSMCBSRInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCBSRInterfaceIndex.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Type(Unsigned32):
    """Custom type agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Type.__name__ = "Unsigned32"
_AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Object = MibTableColumn
agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength = _AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 5, 1, 2),
    _AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Type()
)
agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMCBSRInterfacePriority_Type(Integer32):
    """Custom type agentMulticastIPv6PIMSMCBSRInterfacePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AgentMulticastIPv6PIMSMCBSRInterfacePriority_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMSMCBSRInterfacePriority_Object = MibTableColumn
agentMulticastIPv6PIMSMCBSRInterfacePriority = _AgentMulticastIPv6PIMSMCBSRInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 5, 1, 3),
    _AgentMulticastIPv6PIMSMCBSRInterfacePriority_Type()
)
agentMulticastIPv6PIMSMCBSRInterfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCBSRInterfacePriority.setStatus("obsolete")
_AgentMulticastIPv6PIMSMSSMTable_Object = MibTable
agentMulticastIPv6PIMSMSSMTable = _AgentMulticastIPv6PIMSMSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 6)
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMSSMTable.setStatus("obsolete")
_AgentMulticastIPv6PIMSMSSMEntry_Object = MibTableRow
agentMulticastIPv6PIMSMSSMEntry = _AgentMulticastIPv6PIMSMSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 6, 1)
)
agentMulticastIPv6PIMSMSSMEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMSSMGroupAddress"),
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMSSMGroupMask"),
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMSSMEntry.setStatus("obsolete")
_AgentMulticastIPv6PIMSMSSMGroupAddress_Type = Ipv6Address
_AgentMulticastIPv6PIMSMSSMGroupAddress_Object = MibTableColumn
agentMulticastIPv6PIMSMSSMGroupAddress = _AgentMulticastIPv6PIMSMSSMGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 6, 1, 1),
    _AgentMulticastIPv6PIMSMSSMGroupAddress_Type()
)
agentMulticastIPv6PIMSMSSMGroupAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMSSMGroupAddress.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMSSMGroupMask_Type(Unsigned32):
    """Custom type agentMulticastIPv6PIMSMSSMGroupMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentMulticastIPv6PIMSMSSMGroupMask_Type.__name__ = "Unsigned32"
_AgentMulticastIPv6PIMSMSSMGroupMask_Object = MibTableColumn
agentMulticastIPv6PIMSMSSMGroupMask = _AgentMulticastIPv6PIMSMSSMGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 6, 1, 2),
    _AgentMulticastIPv6PIMSMSSMGroupMask_Type()
)
agentMulticastIPv6PIMSMSSMGroupMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMSSMGroupMask.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMSSMStatus_Type(Integer32):
    """Custom type agentMulticastIPv6PIMSMSSMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 4),
          ("destory", 6))
    )


_AgentMulticastIPv6PIMSMSSMStatus_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMSMSSMStatus_Object = MibTableColumn
agentMulticastIPv6PIMSMSSMStatus = _AgentMulticastIPv6PIMSMSSMStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 6, 1, 3),
    _AgentMulticastIPv6PIMSMSSMStatus_Type()
)
agentMulticastIPv6PIMSMSSMStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMSSMStatus.setStatus("obsolete")
_AgentMulticastIPv6PIMSMInterfaceTable_Object = MibTable
agentMulticastIPv6PIMSMInterfaceTable = _AgentMulticastIPv6PIMSMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 7)
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMInterfaceTable.setStatus("obsolete")
_AgentMulticastIPv6PIMSMInterfaceEntry_Object = MibTableRow
agentMulticastIPv6PIMSMInterfaceEntry = _AgentMulticastIPv6PIMSMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 7, 1)
)
agentMulticastIPv6PIMSMInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMInterfaceEntry.setStatus("obsolete")
_AgentMulticastIPv6PIMSMInterfaceIndex_Type = Unsigned32
_AgentMulticastIPv6PIMSMInterfaceIndex_Object = MibTableColumn
agentMulticastIPv6PIMSMInterfaceIndex = _AgentMulticastIPv6PIMSMInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 7, 1, 1),
    _AgentMulticastIPv6PIMSMInterfaceIndex_Type()
)
agentMulticastIPv6PIMSMInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMInterfaceIndex.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMInterfaceAdminMode_Type(Integer32):
    """Custom type agentMulticastIPv6PIMSMInterfaceAdminMode based on Integer32"""
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


_AgentMulticastIPv6PIMSMInterfaceAdminMode_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMSMInterfaceAdminMode_Object = MibTableColumn
agentMulticastIPv6PIMSMInterfaceAdminMode = _AgentMulticastIPv6PIMSMInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 7, 1, 2),
    _AgentMulticastIPv6PIMSMInterfaceAdminMode_Type()
)
agentMulticastIPv6PIMSMInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMInterfaceAdminMode.setStatus("current")


class _AgentMulticastIPv6PIMSMInterfaceHelloInterval_Type(Unsigned32):
    """Custom type agentMulticastIPv6PIMSMInterfaceHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_AgentMulticastIPv6PIMSMInterfaceHelloInterval_Type.__name__ = "Unsigned32"
_AgentMulticastIPv6PIMSMInterfaceHelloInterval_Object = MibTableColumn
agentMulticastIPv6PIMSMInterfaceHelloInterval = _AgentMulticastIPv6PIMSMInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 7, 1, 3),
    _AgentMulticastIPv6PIMSMInterfaceHelloInterval_Type()
)
agentMulticastIPv6PIMSMInterfaceHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMInterfaceHelloInterval.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Type(Unsigned32):
    """Custom type agentMulticastIPv6PIMSMInterfaceJoinPruneInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Type.__name__ = "Unsigned32"
_AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Object = MibTableColumn
agentMulticastIPv6PIMSMInterfaceJoinPruneInterval = _AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 7, 1, 4),
    _AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Type()
)
agentMulticastIPv6PIMSMInterfaceJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMInterfaceJoinPruneInterval.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMInterfaceBsrBorder_Type(Integer32):
    """Custom type agentMulticastIPv6PIMSMInterfaceBsrBorder based on Integer32"""
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


_AgentMulticastIPv6PIMSMInterfaceBsrBorder_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMSMInterfaceBsrBorder_Object = MibTableColumn
agentMulticastIPv6PIMSMInterfaceBsrBorder = _AgentMulticastIPv6PIMSMInterfaceBsrBorder_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 7, 1, 5),
    _AgentMulticastIPv6PIMSMInterfaceBsrBorder_Type()
)
agentMulticastIPv6PIMSMInterfaceBsrBorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMInterfaceBsrBorder.setStatus("current")


class _AgentMulticastIPv6PIMSMInterfaceDrPriority_Type(Unsigned32):
    """Custom type agentMulticastIPv6PIMSMInterfaceDrPriority based on Unsigned32"""
    defaultValue = 1


_AgentMulticastIPv6PIMSMInterfaceDrPriority_Object = MibTableColumn
agentMulticastIPv6PIMSMInterfaceDrPriority = _AgentMulticastIPv6PIMSMInterfaceDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 7, 1, 6),
    _AgentMulticastIPv6PIMSMInterfaceDrPriority_Type()
)
agentMulticastIPv6PIMSMInterfaceDrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMInterfaceDrPriority.setStatus("obsolete")
_AgentMulticastIPv6PIMSMCandRPTable_Object = MibTable
agentMulticastIPv6PIMSMCandRPTable = _AgentMulticastIPv6PIMSMCandRPTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 8)
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCandRPTable.setStatus("obsolete")
_AgentMulticastIPv6PIMSMCandRPEntry_Object = MibTableRow
agentMulticastIPv6PIMSMCandRPEntry = _AgentMulticastIPv6PIMSMCandRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 8, 1)
)
agentMulticastIPv6PIMSMCandRPEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMCandRPAddress"),
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMCandRPGroupAddress"),
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMSMCandRPGroupPrefixLength"),
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCandRPEntry.setStatus("obsolete")
_AgentMulticastIPv6PIMSMCandRPAddress_Type = Ipv6Address
_AgentMulticastIPv6PIMSMCandRPAddress_Object = MibTableColumn
agentMulticastIPv6PIMSMCandRPAddress = _AgentMulticastIPv6PIMSMCandRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 8, 1, 1),
    _AgentMulticastIPv6PIMSMCandRPAddress_Type()
)
agentMulticastIPv6PIMSMCandRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCandRPAddress.setStatus("obsolete")
_AgentMulticastIPv6PIMSMCandRPGroupAddress_Type = Ipv6Address
_AgentMulticastIPv6PIMSMCandRPGroupAddress_Object = MibTableColumn
agentMulticastIPv6PIMSMCandRPGroupAddress = _AgentMulticastIPv6PIMSMCandRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 8, 1, 2),
    _AgentMulticastIPv6PIMSMCandRPGroupAddress_Type()
)
agentMulticastIPv6PIMSMCandRPGroupAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCandRPGroupAddress.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Type(Unsigned32):
    """Custom type agentMulticastIPv6PIMSMCandRPGroupPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Type.__name__ = "Unsigned32"
_AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Object = MibTableColumn
agentMulticastIPv6PIMSMCandRPGroupPrefixLength = _AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 8, 1, 3),
    _AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Type()
)
agentMulticastIPv6PIMSMCandRPGroupPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCandRPGroupPrefixLength.setStatus("obsolete")


class _AgentMulticastIPv6PIMSMCandRPStatus_Type(Integer32):
    """Custom type agentMulticastIPv6PIMSMCandRPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 4),
          ("destory", 6))
    )


_AgentMulticastIPv6PIMSMCandRPStatus_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMSMCandRPStatus_Object = MibTableColumn
agentMulticastIPv6PIMSMCandRPStatus = _AgentMulticastIPv6PIMSMCandRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 9, 8, 1, 4),
    _AgentMulticastIPv6PIMSMCandRPStatus_Type()
)
agentMulticastIPv6PIMSMCandRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMSMCandRPStatus.setStatus("obsolete")
_AgentMulticastIPv6PIMDMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastIPv6PIMDMConfigGroup = _AgentMulticastIPv6PIMDMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 10)
)


class _AgentMulticastIPv6PIMDMAdminMode_Type(Integer32):
    """Custom type agentMulticastIPv6PIMDMAdminMode based on Integer32"""
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


_AgentMulticastIPv6PIMDMAdminMode_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMDMAdminMode_Object = MibScalar
agentMulticastIPv6PIMDMAdminMode = _AgentMulticastIPv6PIMDMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 10, 1),
    _AgentMulticastIPv6PIMDMAdminMode_Type()
)
agentMulticastIPv6PIMDMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMDMAdminMode.setStatus("current")
_AgentMulticastIPv6PIMDMInterfaceTable_Object = MibTable
agentMulticastIPv6PIMDMInterfaceTable = _AgentMulticastIPv6PIMDMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 10, 2)
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMDMInterfaceTable.setStatus("obsolete")
_AgentMulticastIPv6PIMDMInterfaceEntry_Object = MibTableRow
agentMulticastIPv6PIMDMInterfaceEntry = _AgentMulticastIPv6PIMDMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 10, 2, 1)
)
agentMulticastIPv6PIMDMInterfaceEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastIPv6PIMDMInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMDMInterfaceEntry.setStatus("obsolete")
_AgentMulticastIPv6PIMDMInterfaceIndex_Type = Unsigned32
_AgentMulticastIPv6PIMDMInterfaceIndex_Object = MibTableColumn
agentMulticastIPv6PIMDMInterfaceIndex = _AgentMulticastIPv6PIMDMInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 10, 2, 1, 1),
    _AgentMulticastIPv6PIMDMInterfaceIndex_Type()
)
agentMulticastIPv6PIMDMInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMDMInterfaceIndex.setStatus("obsolete")


class _AgentMulticastIPv6PIMDMInterfaceMode_Type(Integer32):
    """Custom type agentMulticastIPv6PIMDMInterfaceMode based on Integer32"""
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


_AgentMulticastIPv6PIMDMInterfaceMode_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMDMInterfaceMode_Object = MibTableColumn
agentMulticastIPv6PIMDMInterfaceMode = _AgentMulticastIPv6PIMDMInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 10, 2, 1, 2),
    _AgentMulticastIPv6PIMDMInterfaceMode_Type()
)
agentMulticastIPv6PIMDMInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMDMInterfaceMode.setStatus("obsolete")


class _AgentMulticastIPv6PIMDMInterfaceHelloInterval_Type(Integer32):
    """Custom type agentMulticastIPv6PIMDMInterfaceHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_AgentMulticastIPv6PIMDMInterfaceHelloInterval_Type.__name__ = "Integer32"
_AgentMulticastIPv6PIMDMInterfaceHelloInterval_Object = MibTableColumn
agentMulticastIPv6PIMDMInterfaceHelloInterval = _AgentMulticastIPv6PIMDMInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 10, 2, 1, 3),
    _AgentMulticastIPv6PIMDMInterfaceHelloInterval_Type()
)
agentMulticastIPv6PIMDMInterfaceHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIPv6PIMDMInterfaceHelloInterval.setStatus("obsolete")
_AgentMulticastAdminBoundaryConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastAdminBoundaryConfigGroup = _AgentMulticastAdminBoundaryConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 11)
)
_AgentMulticastAdminBoundaryTable_Object = MibTable
agentMulticastAdminBoundaryTable = _AgentMulticastAdminBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 11, 1)
)
if mibBuilder.loadTexts:
    agentMulticastAdminBoundaryTable.setStatus("obsolete")
_AgentMulticastAdminBoundaryEntry_Object = MibTableRow
agentMulticastAdminBoundaryEntry = _AgentMulticastAdminBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 11, 1, 1)
)
agentMulticastAdminBoundaryEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastAdminBoundaryIndex"),
    (0, "MULTICAST-MIB", "agentMulticastAdminBoundaryGroupAddress"),
    (0, "MULTICAST-MIB", "agentMulticastAdminBoundaryGroupMask"),
)
if mibBuilder.loadTexts:
    agentMulticastAdminBoundaryEntry.setStatus("obsolete")
_AgentMulticastAdminBoundaryIndex_Type = Unsigned32
_AgentMulticastAdminBoundaryIndex_Object = MibTableColumn
agentMulticastAdminBoundaryIndex = _AgentMulticastAdminBoundaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 11, 1, 1, 1),
    _AgentMulticastAdminBoundaryIndex_Type()
)
agentMulticastAdminBoundaryIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastAdminBoundaryIndex.setStatus("obsolete")
_AgentMulticastAdminBoundaryGroupAddress_Type = IpAddress
_AgentMulticastAdminBoundaryGroupAddress_Object = MibTableColumn
agentMulticastAdminBoundaryGroupAddress = _AgentMulticastAdminBoundaryGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 11, 1, 1, 2),
    _AgentMulticastAdminBoundaryGroupAddress_Type()
)
agentMulticastAdminBoundaryGroupAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastAdminBoundaryGroupAddress.setStatus("obsolete")
_AgentMulticastAdminBoundaryGroupMask_Type = IpAddress
_AgentMulticastAdminBoundaryGroupMask_Object = MibTableColumn
agentMulticastAdminBoundaryGroupMask = _AgentMulticastAdminBoundaryGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 11, 1, 1, 3),
    _AgentMulticastAdminBoundaryGroupMask_Type()
)
agentMulticastAdminBoundaryGroupMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastAdminBoundaryGroupMask.setStatus("obsolete")


class _AgentMulticastAdminBoundaryStatus_Type(Integer32):
    """Custom type agentMulticastAdminBoundaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 4),
          ("destory", 6))
    )


_AgentMulticastAdminBoundaryStatus_Type.__name__ = "Integer32"
_AgentMulticastAdminBoundaryStatus_Object = MibTableColumn
agentMulticastAdminBoundaryStatus = _AgentMulticastAdminBoundaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 11, 1, 1, 4),
    _AgentMulticastAdminBoundaryStatus_Type()
)
agentMulticastAdminBoundaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastAdminBoundaryStatus.setStatus("obsolete")
_AgentMulticastStaticRouteConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastStaticRouteConfigGroup = _AgentMulticastStaticRouteConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 12)
)
_AgentMulticastStaticRouteTable_Object = MibTable
agentMulticastStaticRouteTable = _AgentMulticastStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 12, 1)
)
if mibBuilder.loadTexts:
    agentMulticastStaticRouteTable.setStatus("obsolete")
_AgentMulticastStaticRouteEntry_Object = MibTableRow
agentMulticastStaticRouteEntry = _AgentMulticastStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 12, 1, 1)
)
agentMulticastStaticRouteEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentMulticastStaticRouteSourceIP"),
)
if mibBuilder.loadTexts:
    agentMulticastStaticRouteEntry.setStatus("obsolete")
_AgentMulticastStaticRouteSourceIP_Type = IpAddress
_AgentMulticastStaticRouteSourceIP_Object = MibTableColumn
agentMulticastStaticRouteSourceIP = _AgentMulticastStaticRouteSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 12, 1, 1, 1),
    _AgentMulticastStaticRouteSourceIP_Type()
)
agentMulticastStaticRouteSourceIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastStaticRouteSourceIP.setStatus("obsolete")
_AgentMulticastStaticRouteSourceMask_Type = IpAddress
_AgentMulticastStaticRouteSourceMask_Object = MibTableColumn
agentMulticastStaticRouteSourceMask = _AgentMulticastStaticRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 12, 1, 1, 2),
    _AgentMulticastStaticRouteSourceMask_Type()
)
agentMulticastStaticRouteSourceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastStaticRouteSourceMask.setStatus("obsolete")
_AgentMulticastStaticRouteRPFNeighbor_Type = IpAddress
_AgentMulticastStaticRouteRPFNeighbor_Object = MibTableColumn
agentMulticastStaticRouteRPFNeighbor = _AgentMulticastStaticRouteRPFNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 12, 1, 1, 3),
    _AgentMulticastStaticRouteRPFNeighbor_Type()
)
agentMulticastStaticRouteRPFNeighbor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastStaticRouteRPFNeighbor.setStatus("obsolete")


class _AgentMulticastStaticRouteMetric_Type(Unsigned32):
    """Custom type agentMulticastStaticRouteMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentMulticastStaticRouteMetric_Type.__name__ = "Unsigned32"
_AgentMulticastStaticRouteMetric_Object = MibTableColumn
agentMulticastStaticRouteMetric = _AgentMulticastStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 12, 1, 1, 4),
    _AgentMulticastStaticRouteMetric_Type()
)
agentMulticastStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastStaticRouteMetric.setStatus("obsolete")
_AgentMulticastStaticRouteInterface_Type = Unsigned32
_AgentMulticastStaticRouteInterface_Object = MibTableColumn
agentMulticastStaticRouteInterface = _AgentMulticastStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 12, 1, 1, 5),
    _AgentMulticastStaticRouteInterface_Type()
)
agentMulticastStaticRouteInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastStaticRouteInterface.setStatus("obsolete")


class _AgentMulticastStaticRouteStatus_Type(Integer32):
    """Custom type agentMulticastStaticRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 4),
          ("destory", 6))
    )


_AgentMulticastStaticRouteStatus_Type.__name__ = "Integer32"
_AgentMulticastStaticRouteStatus_Object = MibTableColumn
agentMulticastStaticRouteStatus = _AgentMulticastStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 12, 1, 1, 6),
    _AgentMulticastStaticRouteStatus_Type()
)
agentMulticastStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastStaticRouteStatus.setStatus("obsolete")
_AgentIpStaticMRouteTable_Object = MibTable
agentIpStaticMRouteTable = _AgentIpStaticMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 13)
)
if mibBuilder.loadTexts:
    agentIpStaticMRouteTable.setStatus("current")
_AgentIpStaticMRouteEntry_Object = MibTableRow
agentIpStaticMRouteEntry = _AgentIpStaticMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 13, 1)
)
agentIpStaticMRouteEntry.setIndexNames(
    (0, "MULTICAST-MIB", "agentIpStaticMRouteSrcAddressType"),
    (0, "MULTICAST-MIB", "agentIpStaticMRouteSrcIpAddr"),
    (0, "MULTICAST-MIB", "agentIpStaticMRouteSrcNetMask"),
)
if mibBuilder.loadTexts:
    agentIpStaticMRouteEntry.setStatus("current")
_AgentIpStaticMRouteSrcAddressType_Type = InetAddressType
_AgentIpStaticMRouteSrcAddressType_Object = MibTableColumn
agentIpStaticMRouteSrcAddressType = _AgentIpStaticMRouteSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 13, 1, 1),
    _AgentIpStaticMRouteSrcAddressType_Type()
)
agentIpStaticMRouteSrcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpStaticMRouteSrcAddressType.setStatus("current")
_AgentIpStaticMRouteSrcIpAddr_Type = InetAddress
_AgentIpStaticMRouteSrcIpAddr_Object = MibTableColumn
agentIpStaticMRouteSrcIpAddr = _AgentIpStaticMRouteSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 13, 1, 2),
    _AgentIpStaticMRouteSrcIpAddr_Type()
)
agentIpStaticMRouteSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpStaticMRouteSrcIpAddr.setStatus("current")


class _AgentIpStaticMRouteSrcNetMask_Type(Integer32):
    """Custom type agentIpStaticMRouteSrcNetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AgentIpStaticMRouteSrcNetMask_Type.__name__ = "Integer32"
_AgentIpStaticMRouteSrcNetMask_Object = MibTableColumn
agentIpStaticMRouteSrcNetMask = _AgentIpStaticMRouteSrcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 13, 1, 3),
    _AgentIpStaticMRouteSrcNetMask_Type()
)
agentIpStaticMRouteSrcNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpStaticMRouteSrcNetMask.setStatus("current")
_AgentIpStaticMRouteRpfIpAddr_Type = InetAddress
_AgentIpStaticMRouteRpfIpAddr_Object = MibTableColumn
agentIpStaticMRouteRpfIpAddr = _AgentIpStaticMRouteRpfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 13, 1, 4),
    _AgentIpStaticMRouteRpfIpAddr_Type()
)
agentIpStaticMRouteRpfIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpStaticMRouteRpfIpAddr.setStatus("current")
_AgentIpStaticMRouteIfIndex_Type = InterfaceIndex
_AgentIpStaticMRouteIfIndex_Object = MibTableColumn
agentIpStaticMRouteIfIndex = _AgentIpStaticMRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 13, 1, 5),
    _AgentIpStaticMRouteIfIndex_Type()
)
agentIpStaticMRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpStaticMRouteIfIndex.setStatus("current")


class _AgentIpStaticMRoutePreference_Type(Integer32):
    """Custom type agentIpStaticMRoutePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentIpStaticMRoutePreference_Type.__name__ = "Integer32"
_AgentIpStaticMRoutePreference_Object = MibTableColumn
agentIpStaticMRoutePreference = _AgentIpStaticMRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 13, 1, 6),
    _AgentIpStaticMRoutePreference_Type()
)
agentIpStaticMRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpStaticMRoutePreference.setStatus("current")
_AgentIpStaticMRouteStatus_Type = RowStatus
_AgentIpStaticMRouteStatus_Object = MibTableColumn
agentIpStaticMRouteStatus = _AgentIpStaticMRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 4, 13, 1, 7),
    _AgentIpStaticMRouteStatus_Type()
)
agentIpStaticMRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpStaticMRouteStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MULTICAST-MIB",
    **{"multicast": multicast,
       "agentMulticastIGMPConfigGroup": agentMulticastIGMPConfigGroup,
       "agentMulticastIGMPAdminMode": agentMulticastIGMPAdminMode,
       "agentMulticastIGMPInterfaceTable": agentMulticastIGMPInterfaceTable,
       "agentMulticastIGMPInterfaceEntry": agentMulticastIGMPInterfaceEntry,
       "agentMulticastIGMPInterfaceIfIndex": agentMulticastIGMPInterfaceIfIndex,
       "agentMulticastIGMPInterfaceAdminMode": agentMulticastIGMPInterfaceAdminMode,
       "agentMulticastIGMPProxyInterfaceTable": agentMulticastIGMPProxyInterfaceTable,
       "agentMulticastIGMPProxyInterfaceEntry": agentMulticastIGMPProxyInterfaceEntry,
       "agentMulticastIGMPProxyInterfaceIfIndex": agentMulticastIGMPProxyInterfaceIfIndex,
       "agentMulticastIGMPProxyInterfaceAdminMode": agentMulticastIGMPProxyInterfaceAdminMode,
       "agentMulticastIGMPProxyInterfaceInterval": agentMulticastIGMPProxyInterfaceInterval,
       "agentMulticastPIMConfigGroup": agentMulticastPIMConfigGroup,
       "agentMulticastPIMConfigMode": agentMulticastPIMConfigMode,
       "agentMulticastPIMSMConfigGroup": agentMulticastPIMSMConfigGroup,
       "agentMulticastPIMSMAdminMode": agentMulticastPIMSMAdminMode,
       "agentMulticastPIMSMDataThresholdRate": agentMulticastPIMSMDataThresholdRate,
       "agentMulticastPIMSMStaticRPTable": agentMulticastPIMSMStaticRPTable,
       "agentMulticastPIMSMStaticRPEntry": agentMulticastPIMSMStaticRPEntry,
       "agentMulticastPIMSMStaticRPIpAddr": agentMulticastPIMSMStaticRPIpAddr,
       "agentMulticastPIMSMStaticRPGroupIpAddr": agentMulticastPIMSMStaticRPGroupIpAddr,
       "agentMulticastPIMSMStaticRPGroupIpMask": agentMulticastPIMSMStaticRPGroupIpMask,
       "agentMulticastPIMSMStaticRPStatus": agentMulticastPIMSMStaticRPStatus,
       "agentMulticastPIMSMCBSRInterfaceTable": agentMulticastPIMSMCBSRInterfaceTable,
       "agentMulticastPIMSMCBSRInterfaceEntry": agentMulticastPIMSMCBSRInterfaceEntry,
       "agentMulticastPIMSMCBSRInterfaceIndex": agentMulticastPIMSMCBSRInterfaceIndex,
       "agentMulticastPIMSMCBSRInterfaceHashMaskLength": agentMulticastPIMSMCBSRInterfaceHashMaskLength,
       "agentMulticastPIMSMCBSRInterfacePriority": agentMulticastPIMSMCBSRInterfacePriority,
       "agentMulticastPIMSMSSMTable": agentMulticastPIMSMSSMTable,
       "agentMulticastPIMSMSSMEntry": agentMulticastPIMSMSSMEntry,
       "agentMulticastPIMSMSSMGroupAddress": agentMulticastPIMSMSSMGroupAddress,
       "agentMulticastPIMSMSSMGroupMask": agentMulticastPIMSMSSMGroupMask,
       "agentMulticastPIMSMSSMStatus": agentMulticastPIMSMSSMStatus,
       "agentMulticastPIMSMInterfaceTable": agentMulticastPIMSMInterfaceTable,
       "agentMulticastPIMSMInterfaceEntry": agentMulticastPIMSMInterfaceEntry,
       "agentMulticastPIMSMInterfaceIndex": agentMulticastPIMSMInterfaceIndex,
       "agentMulticastPIMSMInterfaceAdminMode": agentMulticastPIMSMInterfaceAdminMode,
       "agentMulticastPIMSMInterfaceHelloInterval": agentMulticastPIMSMInterfaceHelloInterval,
       "agentMulticastPIMSMInterfaceJoinPruneInterval": agentMulticastPIMSMInterfaceJoinPruneInterval,
       "agentMulticastPIMSMInterfaceBsrBorder": agentMulticastPIMSMInterfaceBsrBorder,
       "agentMulticastPIMSMInterfaceDrPriority": agentMulticastPIMSMInterfaceDrPriority,
       "agentMulticastPIMSMInterfaceCBSRHashMaskLength": agentMulticastPIMSMInterfaceCBSRHashMaskLength,
       "agentMulticastPIMSMInterfaceCRPPreference": agentMulticastPIMSMInterfaceCRPPreference,
       "agentMulticastPIMSMCandRPTable": agentMulticastPIMSMCandRPTable,
       "agentMulticastPIMSMCandRPEntry": agentMulticastPIMSMCandRPEntry,
       "agentMulticastPIMSMCandRPAddress": agentMulticastPIMSMCandRPAddress,
       "agentMulticastPIMSMCandRPGroupAddress": agentMulticastPIMSMCandRPGroupAddress,
       "agentMulticastPIMSMCandRPGroupPrefixLength": agentMulticastPIMSMCandRPGroupPrefixLength,
       "agentMulticastPIMSMCandRPStatus": agentMulticastPIMSMCandRPStatus,
       "agentMulticastPIMDMConfigGroup": agentMulticastPIMDMConfigGroup,
       "agentMulticastPIMDMAdminMode": agentMulticastPIMDMAdminMode,
       "agentMulticastPIMDMInterfaceTable": agentMulticastPIMDMInterfaceTable,
       "agentMulticastPIMDMInterfaceEntry": agentMulticastPIMDMInterfaceEntry,
       "agentMulticastPIMDMInterfaceIndex": agentMulticastPIMDMInterfaceIndex,
       "agentMulticastPIMDMInterfaceMode": agentMulticastPIMDMInterfaceMode,
       "agentMulticastPIMDMInterfaceHelloInterval": agentMulticastPIMDMInterfaceHelloInterval,
       "agentMulticastRoutingConfigGroup": agentMulticastRoutingConfigGroup,
       "agentMulticastRoutingAdminMode": agentMulticastRoutingAdminMode,
       "agentMulticastDVMRPConfigGroup": agentMulticastDVMRPConfigGroup,
       "agentMulticastDVMRPAdminMode": agentMulticastDVMRPAdminMode,
       "agentMulticastDVMRPInterfaceTable": agentMulticastDVMRPInterfaceTable,
       "agentMulticastDVMRPInterfaceEntry": agentMulticastDVMRPInterfaceEntry,
       "agentMulticastDVMRPInterfaceIfIndex": agentMulticastDVMRPInterfaceIfIndex,
       "agentMulticastDVMRPInterfaceAdminMode": agentMulticastDVMRPInterfaceAdminMode,
       "agentMulticastDVMRPInterfaceMetric": agentMulticastDVMRPInterfaceMetric,
       "agentMulticastDVMRPInterfaceGenerationId": agentMulticastDVMRPInterfaceGenerationId,
       "agentMulticastMLDConfigGroup": agentMulticastMLDConfigGroup,
       "agentMulticastMLDAdminMode": agentMulticastMLDAdminMode,
       "agentMulticastMLDInterfaceTable": agentMulticastMLDInterfaceTable,
       "agentMulticastMLDInterfaceEntry": agentMulticastMLDInterfaceEntry,
       "agentMulticastMLDInterfaceIfIndex": agentMulticastMLDInterfaceIfIndex,
       "agentMulticastMLDInterfaceAdminMode": agentMulticastMLDInterfaceAdminMode,
       "agentMulticastMLDProxyInterfaceTable": agentMulticastMLDProxyInterfaceTable,
       "agentMulticastMLDProxyInterfaceEntry": agentMulticastMLDProxyInterfaceEntry,
       "agentMulticastMLDProxyInterfaceIfIndex": agentMulticastMLDProxyInterfaceIfIndex,
       "agentMulticastMLDProxyInterfaceAdminMode": agentMulticastMLDProxyInterfaceAdminMode,
       "agentMulticastMLDProxyInterfaceInterval": agentMulticastMLDProxyInterfaceInterval,
       "agentMulticastIPv6PIMSMConfigGroup": agentMulticastIPv6PIMSMConfigGroup,
       "agentMulticastIPv6PIMSMAdminMode": agentMulticastIPv6PIMSMAdminMode,
       "agentMulticastIPv6PIMSMDataThresholdRate": agentMulticastIPv6PIMSMDataThresholdRate,
       "agentMulticastIPv6PIMSMStaticRPTable": agentMulticastIPv6PIMSMStaticRPTable,
       "agentMulticastIPv6PIMSMStaticRPEntry": agentMulticastIPv6PIMSMStaticRPEntry,
       "agentMulticastIPv6PIMSMStaticRPIpAddr": agentMulticastIPv6PIMSMStaticRPIpAddr,
       "agentMulticastIPv6PIMSMStaticRPGroupIpAddr": agentMulticastIPv6PIMSMStaticRPGroupIpAddr,
       "agentMulticastIPv6PIMSMStaticRPGroupIpPrefix": agentMulticastIPv6PIMSMStaticRPGroupIpPrefix,
       "agentMulticastIPv6PIMSMStaticRPStatus": agentMulticastIPv6PIMSMStaticRPStatus,
       "agentMulticastIPv6PIMSMCBSRInterfaceTable": agentMulticastIPv6PIMSMCBSRInterfaceTable,
       "agentMulticastIPv6PIMSMCBSRInterfaceEntry": agentMulticastIPv6PIMSMCBSRInterfaceEntry,
       "agentMulticastIPv6PIMSMCBSRInterfaceIndex": agentMulticastIPv6PIMSMCBSRInterfaceIndex,
       "agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength": agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength,
       "agentMulticastIPv6PIMSMCBSRInterfacePriority": agentMulticastIPv6PIMSMCBSRInterfacePriority,
       "agentMulticastIPv6PIMSMSSMTable": agentMulticastIPv6PIMSMSSMTable,
       "agentMulticastIPv6PIMSMSSMEntry": agentMulticastIPv6PIMSMSSMEntry,
       "agentMulticastIPv6PIMSMSSMGroupAddress": agentMulticastIPv6PIMSMSSMGroupAddress,
       "agentMulticastIPv6PIMSMSSMGroupMask": agentMulticastIPv6PIMSMSSMGroupMask,
       "agentMulticastIPv6PIMSMSSMStatus": agentMulticastIPv6PIMSMSSMStatus,
       "agentMulticastIPv6PIMSMInterfaceTable": agentMulticastIPv6PIMSMInterfaceTable,
       "agentMulticastIPv6PIMSMInterfaceEntry": agentMulticastIPv6PIMSMInterfaceEntry,
       "agentMulticastIPv6PIMSMInterfaceIndex": agentMulticastIPv6PIMSMInterfaceIndex,
       "agentMulticastIPv6PIMSMInterfaceAdminMode": agentMulticastIPv6PIMSMInterfaceAdminMode,
       "agentMulticastIPv6PIMSMInterfaceHelloInterval": agentMulticastIPv6PIMSMInterfaceHelloInterval,
       "agentMulticastIPv6PIMSMInterfaceJoinPruneInterval": agentMulticastIPv6PIMSMInterfaceJoinPruneInterval,
       "agentMulticastIPv6PIMSMInterfaceBsrBorder": agentMulticastIPv6PIMSMInterfaceBsrBorder,
       "agentMulticastIPv6PIMSMInterfaceDrPriority": agentMulticastIPv6PIMSMInterfaceDrPriority,
       "agentMulticastIPv6PIMSMCandRPTable": agentMulticastIPv6PIMSMCandRPTable,
       "agentMulticastIPv6PIMSMCandRPEntry": agentMulticastIPv6PIMSMCandRPEntry,
       "agentMulticastIPv6PIMSMCandRPAddress": agentMulticastIPv6PIMSMCandRPAddress,
       "agentMulticastIPv6PIMSMCandRPGroupAddress": agentMulticastIPv6PIMSMCandRPGroupAddress,
       "agentMulticastIPv6PIMSMCandRPGroupPrefixLength": agentMulticastIPv6PIMSMCandRPGroupPrefixLength,
       "agentMulticastIPv6PIMSMCandRPStatus": agentMulticastIPv6PIMSMCandRPStatus,
       "agentMulticastIPv6PIMDMConfigGroup": agentMulticastIPv6PIMDMConfigGroup,
       "agentMulticastIPv6PIMDMAdminMode": agentMulticastIPv6PIMDMAdminMode,
       "agentMulticastIPv6PIMDMInterfaceTable": agentMulticastIPv6PIMDMInterfaceTable,
       "agentMulticastIPv6PIMDMInterfaceEntry": agentMulticastIPv6PIMDMInterfaceEntry,
       "agentMulticastIPv6PIMDMInterfaceIndex": agentMulticastIPv6PIMDMInterfaceIndex,
       "agentMulticastIPv6PIMDMInterfaceMode": agentMulticastIPv6PIMDMInterfaceMode,
       "agentMulticastIPv6PIMDMInterfaceHelloInterval": agentMulticastIPv6PIMDMInterfaceHelloInterval,
       "agentMulticastAdminBoundaryConfigGroup": agentMulticastAdminBoundaryConfigGroup,
       "agentMulticastAdminBoundaryTable": agentMulticastAdminBoundaryTable,
       "agentMulticastAdminBoundaryEntry": agentMulticastAdminBoundaryEntry,
       "agentMulticastAdminBoundaryIndex": agentMulticastAdminBoundaryIndex,
       "agentMulticastAdminBoundaryGroupAddress": agentMulticastAdminBoundaryGroupAddress,
       "agentMulticastAdminBoundaryGroupMask": agentMulticastAdminBoundaryGroupMask,
       "agentMulticastAdminBoundaryStatus": agentMulticastAdminBoundaryStatus,
       "agentMulticastStaticRouteConfigGroup": agentMulticastStaticRouteConfigGroup,
       "agentMulticastStaticRouteTable": agentMulticastStaticRouteTable,
       "agentMulticastStaticRouteEntry": agentMulticastStaticRouteEntry,
       "agentMulticastStaticRouteSourceIP": agentMulticastStaticRouteSourceIP,
       "agentMulticastStaticRouteSourceMask": agentMulticastStaticRouteSourceMask,
       "agentMulticastStaticRouteRPFNeighbor": agentMulticastStaticRouteRPFNeighbor,
       "agentMulticastStaticRouteMetric": agentMulticastStaticRouteMetric,
       "agentMulticastStaticRouteInterface": agentMulticastStaticRouteInterface,
       "agentMulticastStaticRouteStatus": agentMulticastStaticRouteStatus,
       "agentIpStaticMRouteTable": agentIpStaticMRouteTable,
       "agentIpStaticMRouteEntry": agentIpStaticMRouteEntry,
       "agentIpStaticMRouteSrcAddressType": agentIpStaticMRouteSrcAddressType,
       "agentIpStaticMRouteSrcIpAddr": agentIpStaticMRouteSrcIpAddr,
       "agentIpStaticMRouteSrcNetMask": agentIpStaticMRouteSrcNetMask,
       "agentIpStaticMRouteRpfIpAddr": agentIpStaticMRouteRpfIpAddr,
       "agentIpStaticMRouteIfIndex": agentIpStaticMRouteIfIndex,
       "agentIpStaticMRoutePreference": agentIpStaticMRoutePreference,
       "agentIpStaticMRouteStatus": agentIpStaticMRouteStatus}
)
