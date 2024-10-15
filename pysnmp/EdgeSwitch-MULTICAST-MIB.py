# SNMP MIB module (EdgeSwitch-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:42:52 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(pimBsrCandidateBSREntry,) = mibBuilder.importSymbols(
    "PIM-BSR-MIB",
    "pimBsrCandidateBSREntry")

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

fastPathMulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4)
)
fastPathMulticast.setRevisions(
        ("2011-01-26 00:00",
         "2009-01-03 00:00",
         "2007-05-23 00:00",
         "2003-11-21 00:00",
         "2002-05-08 14:18")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentMulticastIGMPConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastIGMPConfigGroup = _AgentMulticastIGMPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 1),
    _AgentMulticastIGMPAdminMode_Type()
)
agentMulticastIGMPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIGMPAdminMode.setStatus("current")
_AgentMulticastIGMPInterfaceTable_Object = MibTable
agentMulticastIGMPInterfaceTable = _AgentMulticastIGMPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceTable.setStatus("obsolete")
_AgentMulticastIGMPInterfaceEntry_Object = MibTableRow
agentMulticastIGMPInterfaceEntry = _AgentMulticastIGMPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 2, 1)
)
agentMulticastIGMPInterfaceEntry.setIndexNames(
    (0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastIGMPInterfaceIfIndex"),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 2, 1, 2),
    _AgentMulticastIGMPInterfaceAdminMode_Type()
)
agentMulticastIGMPInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastIGMPInterfaceAdminMode.setStatus("obsolete")
_AgentMulticastPIMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastPIMConfigGroup = _AgentMulticastPIMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 2)
)


class _AgentMulticastPIMConfigMode_Type(Integer32):
    """Custom type agentMulticastPIMConfigMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 2),
          ("sparse", 1))
    )


_AgentMulticastPIMConfigMode_Type.__name__ = "Integer32"
_AgentMulticastPIMConfigMode_Object = MibScalar
agentMulticastPIMConfigMode = _AgentMulticastPIMConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 2, 1),
    _AgentMulticastPIMConfigMode_Type()
)
agentMulticastPIMConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMConfigMode.setStatus("obsolete")
_AgentMulticastPIMSMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastPIMSMConfigGroup = _AgentMulticastPIMSMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3)
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 1),
    _AgentMulticastPIMSMAdminMode_Type()
)
agentMulticastPIMSMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMAdminMode.setStatus("current")
_AgentMulticastPIMSMStaticRPTable_Object = MibTable
agentMulticastPIMSMStaticRPTable = _AgentMulticastPIMSMStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPTable.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPEntry_Object = MibTableRow
agentMulticastPIMSMStaticRPEntry = _AgentMulticastPIMSMStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1)
)
agentMulticastPIMSMStaticRPEntry.setIndexNames(
    (0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastPIMSMStaticRPIpAddr"),
    (0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastPIMSMStaticRPGroupIpAddr"),
    (0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastPIMSMStaticRPGroupIpMask"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPEntry.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPIpAddr_Type = IpAddress
_AgentMulticastPIMSMStaticRPIpAddr_Object = MibTableColumn
agentMulticastPIMSMStaticRPIpAddr = _AgentMulticastPIMSMStaticRPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1, 1),
    _AgentMulticastPIMSMStaticRPIpAddr_Type()
)
agentMulticastPIMSMStaticRPIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPIpAddr.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPGroupIpAddr_Type = IpAddress
_AgentMulticastPIMSMStaticRPGroupIpAddr_Object = MibTableColumn
agentMulticastPIMSMStaticRPGroupIpAddr = _AgentMulticastPIMSMStaticRPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1, 2),
    _AgentMulticastPIMSMStaticRPGroupIpAddr_Type()
)
agentMulticastPIMSMStaticRPGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPGroupIpAddr.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPGroupIpMask_Type = IpAddress
_AgentMulticastPIMSMStaticRPGroupIpMask_Object = MibTableColumn
agentMulticastPIMSMStaticRPGroupIpMask = _AgentMulticastPIMSMStaticRPGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1, 3),
    _AgentMulticastPIMSMStaticRPGroupIpMask_Type()
)
agentMulticastPIMSMStaticRPGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPGroupIpMask.setStatus("obsolete")
_AgentMulticastPIMSMStaticRPStatus_Type = RowStatus
_AgentMulticastPIMSMStaticRPStatus_Object = MibTableColumn
agentMulticastPIMSMStaticRPStatus = _AgentMulticastPIMSMStaticRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1, 4),
    _AgentMulticastPIMSMStaticRPStatus_Type()
)
agentMulticastPIMSMStaticRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMulticastPIMSMStaticRPStatus.setStatus("obsolete")
_AgentMulticastPIMSMInterfaceTable_Object = MibTable
agentMulticastPIMSMInterfaceTable = _AgentMulticastPIMSMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceTable.setStatus("obsolete")
_AgentMulticastPIMSMInterfaceEntry_Object = MibTableRow
agentMulticastPIMSMInterfaceEntry = _AgentMulticastPIMSMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3, 1)
)
agentMulticastPIMSMInterfaceEntry.setIndexNames(
    (0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastPIMSMInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceEntry.setStatus("obsolete")
_AgentMulticastPIMSMInterfaceIndex_Type = Unsigned32
_AgentMulticastPIMSMInterfaceIndex_Object = MibTableColumn
agentMulticastPIMSMInterfaceIndex = _AgentMulticastPIMSMInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3, 1, 1),
    _AgentMulticastPIMSMInterfaceIndex_Type()
)
agentMulticastPIMSMInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceIndex.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3, 1, 3),
    _AgentMulticastPIMSMInterfaceCRPPreference_Type()
)
agentMulticastPIMSMInterfaceCRPPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMSMInterfaceCRPPreference.setStatus("obsolete")
_AgentPIMBsrCandidateConfTable_Object = MibTable
agentPIMBsrCandidateConfTable = _AgentPIMBsrCandidateConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    agentPIMBsrCandidateConfTable.setStatus("current")
_AgentPIMBsrCandidateConfEntry_Object = MibTableRow
agentPIMBsrCandidateConfEntry = _AgentPIMBsrCandidateConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 4, 1)
)
if mibBuilder.loadTexts:
    agentPIMBsrCandidateConfEntry.setStatus("current")
_PimBsrCandidateBSRAdvInterval_Type = Unsigned32
_PimBsrCandidateBSRAdvInterval_Object = MibTableColumn
pimBsrCandidateBSRAdvInterval = _PimBsrCandidateBSRAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 4, 1, 1),
    _PimBsrCandidateBSRAdvInterval_Type()
)
pimBsrCandidateBSRAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRAdvInterval.setStatus("current")
_AgentMulticastPIMDMConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastPIMDMConfigGroup = _AgentMulticastPIMDMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 4)
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 4, 1),
    _AgentMulticastPIMDMAdminMode_Type()
)
agentMulticastPIMDMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastPIMDMAdminMode.setStatus("current")
_AgentMulticastRoutingConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastRoutingConfigGroup = _AgentMulticastRoutingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 5)
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 5, 1),
    _AgentMulticastRoutingAdminMode_Type()
)
agentMulticastRoutingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastRoutingAdminMode.setStatus("current")
_AgentMulticastDVMRPConfigGroup_ObjectIdentity = ObjectIdentity
agentMulticastDVMRPConfigGroup = _AgentMulticastDVMRPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 6)
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 6, 1),
    _AgentMulticastDVMRPAdminMode_Type()
)
agentMulticastDVMRPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMulticastDVMRPAdminMode.setStatus("current")
_AgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity = ObjectIdentity
agentSnmpTrapFlagsConfigGroupMulticast = _AgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 7)
)


class _AgentSnmpDVMRPTrapFlag_Type(Integer32):
    """Custom type agentSnmpDVMRPTrapFlag based on Integer32"""
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


_AgentSnmpDVMRPTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpDVMRPTrapFlag_Object = MibScalar
agentSnmpDVMRPTrapFlag = _AgentSnmpDVMRPTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 7, 1),
    _AgentSnmpDVMRPTrapFlag_Type()
)
agentSnmpDVMRPTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpDVMRPTrapFlag.setStatus("current")


class _AgentSnmpPIMTrapFlag_Type(Integer32):
    """Custom type agentSnmpPIMTrapFlag based on Integer32"""
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


_AgentSnmpPIMTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpPIMTrapFlag_Object = MibScalar
agentSnmpPIMTrapFlag = _AgentSnmpPIMTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 7, 2),
    _AgentSnmpPIMTrapFlag_Type()
)
agentSnmpPIMTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpPIMTrapFlag.setStatus("current")
_AgentIpStaticMRouteTable_Object = MibTable
agentIpStaticMRouteTable = _AgentIpStaticMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    agentIpStaticMRouteTable.setStatus("current")
_AgentIpStaticMRouteEntry_Object = MibTableRow
agentIpStaticMRouteEntry = _AgentIpStaticMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1)
)
agentIpStaticMRouteEntry.setIndexNames(
    (0, "EdgeSwitch-MULTICAST-MIB", "agentIpStaticMRouteSrcAddressType"),
    (0, "EdgeSwitch-MULTICAST-MIB", "agentIpStaticMRouteSrcIpAddr"),
    (0, "EdgeSwitch-MULTICAST-MIB", "agentIpStaticMRouteSrcNetMask"),
)
if mibBuilder.loadTexts:
    agentIpStaticMRouteEntry.setStatus("current")
_AgentIpStaticMRouteSrcAddressType_Type = InetAddressType
_AgentIpStaticMRouteSrcAddressType_Object = MibTableColumn
agentIpStaticMRouteSrcAddressType = _AgentIpStaticMRouteSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 1),
    _AgentIpStaticMRouteSrcAddressType_Type()
)
agentIpStaticMRouteSrcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpStaticMRouteSrcAddressType.setStatus("current")
_AgentIpStaticMRouteSrcIpAddr_Type = InetAddress
_AgentIpStaticMRouteSrcIpAddr_Object = MibTableColumn
agentIpStaticMRouteSrcIpAddr = _AgentIpStaticMRouteSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 3),
    _AgentIpStaticMRouteSrcNetMask_Type()
)
agentIpStaticMRouteSrcNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpStaticMRouteSrcNetMask.setStatus("current")
_AgentIpStaticMRouteRpfIpAddr_Type = InetAddress
_AgentIpStaticMRouteRpfIpAddr_Object = MibTableColumn
agentIpStaticMRouteRpfIpAddr = _AgentIpStaticMRouteRpfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 4),
    _AgentIpStaticMRouteRpfIpAddr_Type()
)
agentIpStaticMRouteRpfIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpStaticMRouteRpfIpAddr.setStatus("current")
_AgentIpStaticMRouteIfIndex_Type = InterfaceIndex
_AgentIpStaticMRouteIfIndex_Object = MibTableColumn
agentIpStaticMRouteIfIndex = _AgentIpStaticMRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 6),
    _AgentIpStaticMRoutePreference_Type()
)
agentIpStaticMRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpStaticMRoutePreference.setStatus("current")
_AgentIpStaticMRouteStatus_Type = RowStatus
_AgentIpStaticMRouteStatus_Object = MibTableColumn
agentIpStaticMRouteStatus = _AgentIpStaticMRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 7),
    _AgentIpStaticMRouteStatus_Type()
)
agentIpStaticMRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpStaticMRouteStatus.setStatus("current")
pimBsrCandidateBSREntry.registerAugmentions(
    ("EdgeSwitch-MULTICAST-MIB",
     "agentPIMBsrCandidateConfEntry")
)
agentPIMBsrCandidateConfEntry.setIndexNames(*pimBsrCandidateBSREntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-MULTICAST-MIB",
    **{"fastPathMulticast": fastPathMulticast,
       "agentMulticastIGMPConfigGroup": agentMulticastIGMPConfigGroup,
       "agentMulticastIGMPAdminMode": agentMulticastIGMPAdminMode,
       "agentMulticastIGMPInterfaceTable": agentMulticastIGMPInterfaceTable,
       "agentMulticastIGMPInterfaceEntry": agentMulticastIGMPInterfaceEntry,
       "agentMulticastIGMPInterfaceIfIndex": agentMulticastIGMPInterfaceIfIndex,
       "agentMulticastIGMPInterfaceAdminMode": agentMulticastIGMPInterfaceAdminMode,
       "agentMulticastPIMConfigGroup": agentMulticastPIMConfigGroup,
       "agentMulticastPIMConfigMode": agentMulticastPIMConfigMode,
       "agentMulticastPIMSMConfigGroup": agentMulticastPIMSMConfigGroup,
       "agentMulticastPIMSMAdminMode": agentMulticastPIMSMAdminMode,
       "agentMulticastPIMSMStaticRPTable": agentMulticastPIMSMStaticRPTable,
       "agentMulticastPIMSMStaticRPEntry": agentMulticastPIMSMStaticRPEntry,
       "agentMulticastPIMSMStaticRPIpAddr": agentMulticastPIMSMStaticRPIpAddr,
       "agentMulticastPIMSMStaticRPGroupIpAddr": agentMulticastPIMSMStaticRPGroupIpAddr,
       "agentMulticastPIMSMStaticRPGroupIpMask": agentMulticastPIMSMStaticRPGroupIpMask,
       "agentMulticastPIMSMStaticRPStatus": agentMulticastPIMSMStaticRPStatus,
       "agentMulticastPIMSMInterfaceTable": agentMulticastPIMSMInterfaceTable,
       "agentMulticastPIMSMInterfaceEntry": agentMulticastPIMSMInterfaceEntry,
       "agentMulticastPIMSMInterfaceIndex": agentMulticastPIMSMInterfaceIndex,
       "agentMulticastPIMSMInterfaceCBSRHashMaskLength": agentMulticastPIMSMInterfaceCBSRHashMaskLength,
       "agentMulticastPIMSMInterfaceCRPPreference": agentMulticastPIMSMInterfaceCRPPreference,
       "agentPIMBsrCandidateConfTable": agentPIMBsrCandidateConfTable,
       "agentPIMBsrCandidateConfEntry": agentPIMBsrCandidateConfEntry,
       "pimBsrCandidateBSRAdvInterval": pimBsrCandidateBSRAdvInterval,
       "agentMulticastPIMDMConfigGroup": agentMulticastPIMDMConfigGroup,
       "agentMulticastPIMDMAdminMode": agentMulticastPIMDMAdminMode,
       "agentMulticastRoutingConfigGroup": agentMulticastRoutingConfigGroup,
       "agentMulticastRoutingAdminMode": agentMulticastRoutingAdminMode,
       "agentMulticastDVMRPConfigGroup": agentMulticastDVMRPConfigGroup,
       "agentMulticastDVMRPAdminMode": agentMulticastDVMRPAdminMode,
       "agentSnmpTrapFlagsConfigGroupMulticast": agentSnmpTrapFlagsConfigGroupMulticast,
       "agentSnmpDVMRPTrapFlag": agentSnmpDVMRPTrapFlag,
       "agentSnmpPIMTrapFlag": agentSnmpPIMTrapFlag,
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
