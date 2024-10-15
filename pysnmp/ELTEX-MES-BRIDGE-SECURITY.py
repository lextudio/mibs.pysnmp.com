# SNMP MIB module (ELTEX-MES-BRIDGE-SECURITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-BRIDGE-SECURITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:28 2024
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

(eltMes,
 eltMesBridgeSecurity) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes",
    "eltMesBridgeSecurity")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

(rlIpArpInspectEnableVlanEntry,) = mibBuilder.importSymbols(
    "RADLAN-BRIDGE-SECURITY",
    "rlIpArpInspectEnableVlanEntry")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class EltCircuitIdType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class EltRemoteIdType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class EltOpt82CombinationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bin", 5),
          ("pv", 3),
          ("sp", 1),
          ("spv", 4),
          ("sv", 2))
    )



class EltOpt82DelimiterType(Integer32, TextualConvention):
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
        *(("comma", 3),
          ("dot", 2),
          ("hash", 5),
          ("semicolon", 4),
          ("slash", 6),
          ("space", 7),
          ("tr101", 1))
    )



class EltOpt82SuboptionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 2),
          ("tr101", 1))
    )



class EltDHCPSnoopRateLimitType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )



class EltPppoeIaSessionIDType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class EltIpv6DhcpGuardRoleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )



class EltIpv6RaGuardRoleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("router", 1))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIpDhcpSnoop_ObjectIdentity = ObjectIdentity
eltMesIpDhcpSnoop = _EltMesIpDhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1)
)
_EltMesIpDhcpSnoopNotif_ObjectIdentity = ObjectIdentity
eltMesIpDhcpSnoopNotif = _EltMesIpDhcpSnoopNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 0)
)


class _EltIpDhcpOpt82AccessNodeIdentifier_Type(DisplayString):
    """Custom type eltIpDhcpOpt82AccessNodeIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_EltIpDhcpOpt82AccessNodeIdentifier_Type.__name__ = "DisplayString"
_EltIpDhcpOpt82AccessNodeIdentifier_Object = MibScalar
eltIpDhcpOpt82AccessNodeIdentifier = _EltIpDhcpOpt82AccessNodeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 14),
    _EltIpDhcpOpt82AccessNodeIdentifier_Type()
)
eltIpDhcpOpt82AccessNodeIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpDhcpOpt82AccessNodeIdentifier.setStatus("current")
_EltIpDhcpOpt82CircuitIdSuboptionsCombination_Type = EltOpt82CombinationType
_EltIpDhcpOpt82CircuitIdSuboptionsCombination_Object = MibScalar
eltIpDhcpOpt82CircuitIdSuboptionsCombination = _EltIpDhcpOpt82CircuitIdSuboptionsCombination_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 15),
    _EltIpDhcpOpt82CircuitIdSuboptionsCombination_Type()
)
eltIpDhcpOpt82CircuitIdSuboptionsCombination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpDhcpOpt82CircuitIdSuboptionsCombination.setStatus("current")
_EltIpDhcpOpt82CircuitIdSuboptionsDelimeter_Type = EltOpt82DelimiterType
_EltIpDhcpOpt82CircuitIdSuboptionsDelimeter_Object = MibScalar
eltIpDhcpOpt82CircuitIdSuboptionsDelimeter = _EltIpDhcpOpt82CircuitIdSuboptionsDelimeter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 16),
    _EltIpDhcpOpt82CircuitIdSuboptionsDelimeter_Type()
)
eltIpDhcpOpt82CircuitIdSuboptionsDelimeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpDhcpOpt82CircuitIdSuboptionsDelimeter.setStatus("current")
_EltIpDhcpOpt82PortTable_Object = MibTable
eltIpDhcpOpt82PortTable = _EltIpDhcpOpt82PortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 17)
)
if mibBuilder.loadTexts:
    eltIpDhcpOpt82PortTable.setStatus("current")
_EltIpDhcpOpt82PortEntry_Object = MibTableRow
eltIpDhcpOpt82PortEntry = _EltIpDhcpOpt82PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 17, 1)
)
eltIpDhcpOpt82PortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltIpDhcpOpt82PortEntry.setStatus("current")
_EltIpDhcpOpt82PortCircuitId_Type = EltCircuitIdType
_EltIpDhcpOpt82PortCircuitId_Object = MibTableColumn
eltIpDhcpOpt82PortCircuitId = _EltIpDhcpOpt82PortCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 17, 1, 2),
    _EltIpDhcpOpt82PortCircuitId_Type()
)
eltIpDhcpOpt82PortCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpDhcpOpt82PortCircuitId.setStatus("current")
_EltIpDhcpOpt82PortRemoteId_Type = EltRemoteIdType
_EltIpDhcpOpt82PortRemoteId_Object = MibTableColumn
eltIpDhcpOpt82PortRemoteId = _EltIpDhcpOpt82PortRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 17, 1, 3),
    _EltIpDhcpOpt82PortRemoteId_Type()
)
eltIpDhcpOpt82PortRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpDhcpOpt82PortRemoteId.setStatus("current")
_EltIpDhcpOpt82PortRowStatus_Type = RowStatus
_EltIpDhcpOpt82PortRowStatus_Object = MibTableColumn
eltIpDhcpOpt82PortRowStatus = _EltIpDhcpOpt82PortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 17, 1, 4),
    _EltIpDhcpOpt82PortRowStatus_Type()
)
eltIpDhcpOpt82PortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpDhcpOpt82PortRowStatus.setStatus("current")
_EltIpDhcpOpt82SuboptionType_Type = EltOpt82SuboptionType
_EltIpDhcpOpt82SuboptionType_Object = MibScalar
eltIpDhcpOpt82SuboptionType = _EltIpDhcpOpt82SuboptionType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 18),
    _EltIpDhcpOpt82SuboptionType_Type()
)
eltIpDhcpOpt82SuboptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpDhcpOpt82SuboptionType.setStatus("current")


class _EltIpDhcpOpt82RemoteIdentifier_Type(DisplayString):
    """Custom type eltIpDhcpOpt82RemoteIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EltIpDhcpOpt82RemoteIdentifier_Type.__name__ = "DisplayString"
_EltIpDhcpOpt82RemoteIdentifier_Object = MibScalar
eltIpDhcpOpt82RemoteIdentifier = _EltIpDhcpOpt82RemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 19),
    _EltIpDhcpOpt82RemoteIdentifier_Type()
)
eltIpDhcpOpt82RemoteIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpDhcpOpt82RemoteIdentifier.setStatus("current")
_EltIpDhcpSnoopPortTable_Object = MibTable
eltIpDhcpSnoopPortTable = _EltIpDhcpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 20)
)
if mibBuilder.loadTexts:
    eltIpDhcpSnoopPortTable.setStatus("current")
_EltIpDhcpSnoopPortEntry_Object = MibTableRow
eltIpDhcpSnoopPortEntry = _EltIpDhcpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 20, 1)
)
eltIpDhcpSnoopPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltIpDhcpSnoopPortEntry.setStatus("current")


class _EltIpDhcpSnoopPortRateLimit_Type(EltDHCPSnoopRateLimitType):
    """Custom type eltIpDhcpSnoopPortRateLimit based on EltDHCPSnoopRateLimitType"""
    defaultValue = 0


_EltIpDhcpSnoopPortRateLimit_Object = MibTableColumn
eltIpDhcpSnoopPortRateLimit = _EltIpDhcpSnoopPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 20, 1, 2),
    _EltIpDhcpSnoopPortRateLimit_Type()
)
eltIpDhcpSnoopPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpDhcpSnoopPortRateLimit.setStatus("current")
_EltIpDhcpSnoopPortRowStatus_Type = RowStatus
_EltIpDhcpSnoopPortRowStatus_Object = MibTableColumn
eltIpDhcpSnoopPortRowStatus = _EltIpDhcpSnoopPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 20, 1, 3),
    _EltIpDhcpSnoopPortRowStatus_Type()
)
eltIpDhcpSnoopPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpDhcpSnoopPortRowStatus.setStatus("current")
_EltMesIpv6DhcpGuard_ObjectIdentity = ObjectIdentity
eltMesIpv6DhcpGuard = _EltMesIpv6DhcpGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2)
)


class _EltIpv6DhcpGuardEnable_Type(Integer32):
    """Custom type eltIpv6DhcpGuardEnable based on Integer32"""
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


_EltIpv6DhcpGuardEnable_Type.__name__ = "Integer32"
_EltIpv6DhcpGuardEnable_Object = MibScalar
eltIpv6DhcpGuardEnable = _EltIpv6DhcpGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 1),
    _EltIpv6DhcpGuardEnable_Type()
)
eltIpv6DhcpGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardEnable.setStatus("current")
_EltIpv6DhcpGuardEnableTable_Object = MibTable
eltIpv6DhcpGuardEnableTable = _EltIpv6DhcpGuardEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 2)
)
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardEnableTable.setStatus("current")
_EltIpv6DhcpGuardEnableEntry_Object = MibTableRow
eltIpv6DhcpGuardEnableEntry = _EltIpv6DhcpGuardEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 2, 1)
)
eltIpv6DhcpGuardEnableEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-SECURITY", "eltIpv6DhcpGuardEnableVlanTag"),
)
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardEnableEntry.setStatus("current")
_EltIpv6DhcpGuardEnableVlanTag_Type = VlanId
_EltIpv6DhcpGuardEnableVlanTag_Object = MibTableColumn
eltIpv6DhcpGuardEnableVlanTag = _EltIpv6DhcpGuardEnableVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 2, 1, 1),
    _EltIpv6DhcpGuardEnableVlanTag_Type()
)
eltIpv6DhcpGuardEnableVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardEnableVlanTag.setStatus("current")
_EltIpv6DhcpGuardEnableVlanRowStatus_Type = RowStatus
_EltIpv6DhcpGuardEnableVlanRowStatus_Object = MibTableColumn
eltIpv6DhcpGuardEnableVlanRowStatus = _EltIpv6DhcpGuardEnableVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 2, 1, 2),
    _EltIpv6DhcpGuardEnableVlanRowStatus_Type()
)
eltIpv6DhcpGuardEnableVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardEnableVlanRowStatus.setStatus("current")
_EltIpv6DhcpGuardTable_Object = MibTable
eltIpv6DhcpGuardTable = _EltIpv6DhcpGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 3)
)
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardTable.setStatus("current")
_EltIpv6DhcpGuardEntry_Object = MibTableRow
eltIpv6DhcpGuardEntry = _EltIpv6DhcpGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 3, 1)
)
eltIpv6DhcpGuardEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-SECURITY", "eltIpv6DhcpGuardIfIndex"),
)
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardEntry.setStatus("current")
_EltIpv6DhcpGuardIfIndex_Type = Integer32
_EltIpv6DhcpGuardIfIndex_Object = MibTableColumn
eltIpv6DhcpGuardIfIndex = _EltIpv6DhcpGuardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 3, 1, 1),
    _EltIpv6DhcpGuardIfIndex_Type()
)
eltIpv6DhcpGuardIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardIfIndex.setStatus("current")
_EltIpv6DhcpGuardRole_Type = EltIpv6DhcpGuardRoleType
_EltIpv6DhcpGuardRole_Object = MibTableColumn
eltIpv6DhcpGuardRole = _EltIpv6DhcpGuardRole_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 3, 1, 2),
    _EltIpv6DhcpGuardRole_Type()
)
eltIpv6DhcpGuardRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardRole.setStatus("current")
_EltIpv6DhcpGuardAcl_Type = Integer32
_EltIpv6DhcpGuardAcl_Object = MibTableColumn
eltIpv6DhcpGuardAcl = _EltIpv6DhcpGuardAcl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 3, 1, 3),
    _EltIpv6DhcpGuardAcl_Type()
)
eltIpv6DhcpGuardAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardAcl.setStatus("current")


class _EltIpv6DhcpGuardPrefList_Type(DisplayString):
    """Custom type eltIpv6DhcpGuardPrefList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltIpv6DhcpGuardPrefList_Type.__name__ = "DisplayString"
_EltIpv6DhcpGuardPrefList_Object = MibTableColumn
eltIpv6DhcpGuardPrefList = _EltIpv6DhcpGuardPrefList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 3, 1, 4),
    _EltIpv6DhcpGuardPrefList_Type()
)
eltIpv6DhcpGuardPrefList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardPrefList.setStatus("current")


class _EltIpv6DhcpGuardTrusted_Type(Integer32):
    """Custom type eltIpv6DhcpGuardTrusted based on Integer32"""
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


_EltIpv6DhcpGuardTrusted_Type.__name__ = "Integer32"
_EltIpv6DhcpGuardTrusted_Object = MibTableColumn
eltIpv6DhcpGuardTrusted = _EltIpv6DhcpGuardTrusted_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 3, 1, 5),
    _EltIpv6DhcpGuardTrusted_Type()
)
eltIpv6DhcpGuardTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardTrusted.setStatus("current")
_EltIpv6DhcpGuardRowStatus_Type = RowStatus
_EltIpv6DhcpGuardRowStatus_Object = MibTableColumn
eltIpv6DhcpGuardRowStatus = _EltIpv6DhcpGuardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 2, 3, 1, 6),
    _EltIpv6DhcpGuardRowStatus_Type()
)
eltIpv6DhcpGuardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6DhcpGuardRowStatus.setStatus("current")
_EltMesIpv6RaGuard_ObjectIdentity = ObjectIdentity
eltMesIpv6RaGuard = _EltMesIpv6RaGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3)
)


class _EltIpv6RaGuardEnable_Type(Integer32):
    """Custom type eltIpv6RaGuardEnable based on Integer32"""
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


_EltIpv6RaGuardEnable_Type.__name__ = "Integer32"
_EltIpv6RaGuardEnable_Object = MibScalar
eltIpv6RaGuardEnable = _EltIpv6RaGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 1),
    _EltIpv6RaGuardEnable_Type()
)
eltIpv6RaGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6RaGuardEnable.setStatus("current")
_EltIpv6RaGuardEnableTable_Object = MibTable
eltIpv6RaGuardEnableTable = _EltIpv6RaGuardEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 2)
)
if mibBuilder.loadTexts:
    eltIpv6RaGuardEnableTable.setStatus("current")
_EltIpv6RaGuardEnableEntry_Object = MibTableRow
eltIpv6RaGuardEnableEntry = _EltIpv6RaGuardEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 2, 1)
)
eltIpv6RaGuardEnableEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-SECURITY", "eltIpv6RaGuardEnableVlanTag"),
)
if mibBuilder.loadTexts:
    eltIpv6RaGuardEnableEntry.setStatus("current")
_EltIpv6RaGuardEnableVlanTag_Type = VlanId
_EltIpv6RaGuardEnableVlanTag_Object = MibTableColumn
eltIpv6RaGuardEnableVlanTag = _EltIpv6RaGuardEnableVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 2, 1, 1),
    _EltIpv6RaGuardEnableVlanTag_Type()
)
eltIpv6RaGuardEnableVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpv6RaGuardEnableVlanTag.setStatus("current")
_EltIpv6RaGuardEnableVlanRowStatus_Type = RowStatus
_EltIpv6RaGuardEnableVlanRowStatus_Object = MibTableColumn
eltIpv6RaGuardEnableVlanRowStatus = _EltIpv6RaGuardEnableVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 2, 1, 2),
    _EltIpv6RaGuardEnableVlanRowStatus_Type()
)
eltIpv6RaGuardEnableVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6RaGuardEnableVlanRowStatus.setStatus("current")
_EltIpv6RaGuardTable_Object = MibTable
eltIpv6RaGuardTable = _EltIpv6RaGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 3)
)
if mibBuilder.loadTexts:
    eltIpv6RaGuardTable.setStatus("current")
_EltIpv6RaGuardEntry_Object = MibTableRow
eltIpv6RaGuardEntry = _EltIpv6RaGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 3, 1)
)
eltIpv6RaGuardEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-SECURITY", "eltIpv6RaGuardIfIndex"),
)
if mibBuilder.loadTexts:
    eltIpv6RaGuardEntry.setStatus("current")
_EltIpv6RaGuardIfIndex_Type = Integer32
_EltIpv6RaGuardIfIndex_Object = MibTableColumn
eltIpv6RaGuardIfIndex = _EltIpv6RaGuardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 3, 1, 1),
    _EltIpv6RaGuardIfIndex_Type()
)
eltIpv6RaGuardIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6RaGuardIfIndex.setStatus("current")
_EltIpv6RaGuardRole_Type = EltIpv6RaGuardRoleType
_EltIpv6RaGuardRole_Object = MibTableColumn
eltIpv6RaGuardRole = _EltIpv6RaGuardRole_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 3, 1, 2),
    _EltIpv6RaGuardRole_Type()
)
eltIpv6RaGuardRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6RaGuardRole.setStatus("current")
_EltIpv6RaGuardAcl_Type = Integer32
_EltIpv6RaGuardAcl_Object = MibTableColumn
eltIpv6RaGuardAcl = _EltIpv6RaGuardAcl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 3, 1, 3),
    _EltIpv6RaGuardAcl_Type()
)
eltIpv6RaGuardAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6RaGuardAcl.setStatus("current")


class _EltIpv6RaGuardPrefList_Type(DisplayString):
    """Custom type eltIpv6RaGuardPrefList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltIpv6RaGuardPrefList_Type.__name__ = "DisplayString"
_EltIpv6RaGuardPrefList_Object = MibTableColumn
eltIpv6RaGuardPrefList = _EltIpv6RaGuardPrefList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 3, 1, 4),
    _EltIpv6RaGuardPrefList_Type()
)
eltIpv6RaGuardPrefList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6RaGuardPrefList.setStatus("current")


class _EltIpv6RaGuardTrusted_Type(Integer32):
    """Custom type eltIpv6RaGuardTrusted based on Integer32"""
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


_EltIpv6RaGuardTrusted_Type.__name__ = "Integer32"
_EltIpv6RaGuardTrusted_Object = MibTableColumn
eltIpv6RaGuardTrusted = _EltIpv6RaGuardTrusted_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 3, 1, 5),
    _EltIpv6RaGuardTrusted_Type()
)
eltIpv6RaGuardTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6RaGuardTrusted.setStatus("current")
_EltIpv6RaGuardRowStatus_Type = RowStatus
_EltIpv6RaGuardRowStatus_Object = MibTableColumn
eltIpv6RaGuardRowStatus = _EltIpv6RaGuardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 3, 3, 1, 6),
    _EltIpv6RaGuardRowStatus_Type()
)
eltIpv6RaGuardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6RaGuardRowStatus.setStatus("current")


class _EltIpv6RelayAgentEnable_Type(Integer32):
    """Custom type eltIpv6RelayAgentEnable based on Integer32"""
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


_EltIpv6RelayAgentEnable_Type.__name__ = "Integer32"
_EltIpv6RelayAgentEnable_Object = MibScalar
eltIpv6RelayAgentEnable = _EltIpv6RelayAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 4),
    _EltIpv6RelayAgentEnable_Type()
)
eltIpv6RelayAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpv6RelayAgentEnable.setStatus("current")
_EltMesPppoeIa_ObjectIdentity = ObjectIdentity
eltMesPppoeIa = _EltMesPppoeIa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6)
)


class _EltPppoeIaEnable_Type(Integer32):
    """Custom type eltPppoeIaEnable based on Integer32"""
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


_EltPppoeIaEnable_Type.__name__ = "Integer32"
_EltPppoeIaEnable_Object = MibScalar
eltPppoeIaEnable = _EltPppoeIaEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 1),
    _EltPppoeIaEnable_Type()
)
eltPppoeIaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaEnable.setStatus("current")


class _EltPppoeIaAccessNodeIdentifier_Type(DisplayString):
    """Custom type eltPppoeIaAccessNodeIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_EltPppoeIaAccessNodeIdentifier_Type.__name__ = "DisplayString"
_EltPppoeIaAccessNodeIdentifier_Object = MibScalar
eltPppoeIaAccessNodeIdentifier = _EltPppoeIaAccessNodeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 2),
    _EltPppoeIaAccessNodeIdentifier_Type()
)
eltPppoeIaAccessNodeIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaAccessNodeIdentifier.setStatus("current")
_EltPppoeIaCircuitIdSuboptionsCombination_Type = EltOpt82CombinationType
_EltPppoeIaCircuitIdSuboptionsCombination_Object = MibScalar
eltPppoeIaCircuitIdSuboptionsCombination = _EltPppoeIaCircuitIdSuboptionsCombination_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 3),
    _EltPppoeIaCircuitIdSuboptionsCombination_Type()
)
eltPppoeIaCircuitIdSuboptionsCombination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaCircuitIdSuboptionsCombination.setStatus("current")
_EltPppoeIaCircuitIdSuboptionsDelimeter_Type = EltOpt82DelimiterType
_EltPppoeIaCircuitIdSuboptionsDelimeter_Object = MibScalar
eltPppoeIaCircuitIdSuboptionsDelimeter = _EltPppoeIaCircuitIdSuboptionsDelimeter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 4),
    _EltPppoeIaCircuitIdSuboptionsDelimeter_Type()
)
eltPppoeIaCircuitIdSuboptionsDelimeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaCircuitIdSuboptionsDelimeter.setStatus("current")


class _EltPppoeIaGenericErrorMessage_Type(DisplayString):
    """Custom type eltPppoeIaGenericErrorMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EltPppoeIaGenericErrorMessage_Type.__name__ = "DisplayString"
_EltPppoeIaGenericErrorMessage_Object = MibScalar
eltPppoeIaGenericErrorMessage = _EltPppoeIaGenericErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 5),
    _EltPppoeIaGenericErrorMessage_Type()
)
eltPppoeIaGenericErrorMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaGenericErrorMessage.setStatus("current")
_EltPppoeIaPortTable_Object = MibTable
eltPppoeIaPortTable = _EltPppoeIaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6)
)
if mibBuilder.loadTexts:
    eltPppoeIaPortTable.setStatus("current")
_EltPppoeIaPortEntry_Object = MibTableRow
eltPppoeIaPortEntry = _EltPppoeIaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1)
)
eltPppoeIaPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltPppoeIaPortEntry.setStatus("current")
_EltPppoeIaPortEnabled_Type = TruthValue
_EltPppoeIaPortEnabled_Object = MibTableColumn
eltPppoeIaPortEnabled = _EltPppoeIaPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 2),
    _EltPppoeIaPortEnabled_Type()
)
eltPppoeIaPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaPortEnabled.setStatus("current")
_EltPppoeIaPortTrusted_Type = TruthValue
_EltPppoeIaPortTrusted_Object = MibTableColumn
eltPppoeIaPortTrusted = _EltPppoeIaPortTrusted_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 3),
    _EltPppoeIaPortTrusted_Type()
)
eltPppoeIaPortTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaPortTrusted.setStatus("current")
_EltPppoeIaPortCircuitId_Type = EltCircuitIdType
_EltPppoeIaPortCircuitId_Object = MibTableColumn
eltPppoeIaPortCircuitId = _EltPppoeIaPortCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 4),
    _EltPppoeIaPortCircuitId_Type()
)
eltPppoeIaPortCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaPortCircuitId.setStatus("current")
_EltPppoeIaPortRemoteId_Type = EltRemoteIdType
_EltPppoeIaPortRemoteId_Object = MibTableColumn
eltPppoeIaPortRemoteId = _EltPppoeIaPortRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 5),
    _EltPppoeIaPortRemoteId_Type()
)
eltPppoeIaPortRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaPortRemoteId.setStatus("current")
_EltPppoeIaPortStripVendorTag_Type = TruthValue
_EltPppoeIaPortStripVendorTag_Object = MibTableColumn
eltPppoeIaPortStripVendorTag = _EltPppoeIaPortStripVendorTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 6),
    _EltPppoeIaPortStripVendorTag_Type()
)
eltPppoeIaPortStripVendorTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaPortStripVendorTag.setStatus("current")
_EltPppoeIaPortStatsRxPADI_Type = Counter32
_EltPppoeIaPortStatsRxPADI_Object = MibTableColumn
eltPppoeIaPortStatsRxPADI = _EltPppoeIaPortStatsRxPADI_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 7),
    _EltPppoeIaPortStatsRxPADI_Type()
)
eltPppoeIaPortStatsRxPADI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsRxPADI.setStatus("current")
_EltPppoeIaPortStatsRxPADO_Type = Counter32
_EltPppoeIaPortStatsRxPADO_Object = MibTableColumn
eltPppoeIaPortStatsRxPADO = _EltPppoeIaPortStatsRxPADO_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 8),
    _EltPppoeIaPortStatsRxPADO_Type()
)
eltPppoeIaPortStatsRxPADO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsRxPADO.setStatus("current")
_EltPppoeIaPortStatsRxPADR_Type = Counter32
_EltPppoeIaPortStatsRxPADR_Object = MibTableColumn
eltPppoeIaPortStatsRxPADR = _EltPppoeIaPortStatsRxPADR_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 9),
    _EltPppoeIaPortStatsRxPADR_Type()
)
eltPppoeIaPortStatsRxPADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsRxPADR.setStatus("current")
_EltPppoeIaPortStatsRxPADS_Type = Counter32
_EltPppoeIaPortStatsRxPADS_Object = MibTableColumn
eltPppoeIaPortStatsRxPADS = _EltPppoeIaPortStatsRxPADS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 10),
    _EltPppoeIaPortStatsRxPADS_Type()
)
eltPppoeIaPortStatsRxPADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsRxPADS.setStatus("current")
_EltPppoeIaPortStatsRxPADT_Type = Counter32
_EltPppoeIaPortStatsRxPADT_Object = MibTableColumn
eltPppoeIaPortStatsRxPADT = _EltPppoeIaPortStatsRxPADT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 11),
    _EltPppoeIaPortStatsRxPADT_Type()
)
eltPppoeIaPortStatsRxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsRxPADT.setStatus("current")
_EltPppoeIaPortStatsTxGenError_Type = Counter32
_EltPppoeIaPortStatsTxGenError_Object = MibTableColumn
eltPppoeIaPortStatsTxGenError = _EltPppoeIaPortStatsTxGenError_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 12),
    _EltPppoeIaPortStatsTxGenError_Type()
)
eltPppoeIaPortStatsTxGenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsTxGenError.setStatus("current")
_EltPppoeIaPortStatsDroppedResponseFromUntrusted_Type = Counter32
_EltPppoeIaPortStatsDroppedResponseFromUntrusted_Object = MibTableColumn
eltPppoeIaPortStatsDroppedResponseFromUntrusted = _EltPppoeIaPortStatsDroppedResponseFromUntrusted_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 13),
    _EltPppoeIaPortStatsDroppedResponseFromUntrusted_Type()
)
eltPppoeIaPortStatsDroppedResponseFromUntrusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsDroppedResponseFromUntrusted.setStatus("current")
_EltPppoeIaPortStatsDroppedRequestToUntrusted_Type = Counter32
_EltPppoeIaPortStatsDroppedRequestToUntrusted_Object = MibTableColumn
eltPppoeIaPortStatsDroppedRequestToUntrusted = _EltPppoeIaPortStatsDroppedRequestToUntrusted_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 14),
    _EltPppoeIaPortStatsDroppedRequestToUntrusted_Type()
)
eltPppoeIaPortStatsDroppedRequestToUntrusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsDroppedRequestToUntrusted.setStatus("current")
_EltPppoeIaPortStatsDroppedMalformed_Type = Counter32
_EltPppoeIaPortStatsDroppedMalformed_Object = MibTableColumn
eltPppoeIaPortStatsDroppedMalformed = _EltPppoeIaPortStatsDroppedMalformed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 15),
    _EltPppoeIaPortStatsDroppedMalformed_Type()
)
eltPppoeIaPortStatsDroppedMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsDroppedMalformed.setStatus("current")


class _EltPppoeIaPortStatsClearCountersAction_Type(TruthValue):
    """Custom type eltPppoeIaPortStatsClearCountersAction based on TruthValue"""


_EltPppoeIaPortStatsClearCountersAction_Object = MibTableColumn
eltPppoeIaPortStatsClearCountersAction = _EltPppoeIaPortStatsClearCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 16),
    _EltPppoeIaPortStatsClearCountersAction_Type()
)
eltPppoeIaPortStatsClearCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaPortStatsClearCountersAction.setStatus("current")
_EltPppoeIaPortRowStatus_Type = RowStatus
_EltPppoeIaPortRowStatus_Object = MibTableColumn
eltPppoeIaPortRowStatus = _EltPppoeIaPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 6, 1, 17),
    _EltPppoeIaPortRowStatus_Type()
)
eltPppoeIaPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaPortRowStatus.setStatus("current")


class _EltPppoeIaClearCountersAction_Type(TruthValue):
    """Custom type eltPppoeIaClearCountersAction based on TruthValue"""


_EltPppoeIaClearCountersAction_Object = MibScalar
eltPppoeIaClearCountersAction = _EltPppoeIaClearCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 7),
    _EltPppoeIaClearCountersAction_Type()
)
eltPppoeIaClearCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPppoeIaClearCountersAction.setStatus("current")
_EltPppoeIaSessionTable_Object = MibTable
eltPppoeIaSessionTable = _EltPppoeIaSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 8)
)
if mibBuilder.loadTexts:
    eltPppoeIaSessionTable.setStatus("current")
_EltPppoeIaSessionEntry_Object = MibTableRow
eltPppoeIaSessionEntry = _EltPppoeIaSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 8, 1)
)
eltPppoeIaSessionEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-SECURITY", "eltPppoeIaSessionVLANTag"),
    (0, "ELTEX-MES-BRIDGE-SECURITY", "eltPppoeIaSessionMACAddress"),
)
if mibBuilder.loadTexts:
    eltPppoeIaSessionEntry.setStatus("current")
_EltPppoeIaSessionVLANTag_Type = VlanId
_EltPppoeIaSessionVLANTag_Object = MibTableColumn
eltPppoeIaSessionVLANTag = _EltPppoeIaSessionVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 8, 1, 1),
    _EltPppoeIaSessionVLANTag_Type()
)
eltPppoeIaSessionVLANTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaSessionVLANTag.setStatus("current")
_EltPppoeIaSessionMACAddress_Type = MacAddress
_EltPppoeIaSessionMACAddress_Object = MibTableColumn
eltPppoeIaSessionMACAddress = _EltPppoeIaSessionMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 8, 1, 2),
    _EltPppoeIaSessionMACAddress_Type()
)
eltPppoeIaSessionMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaSessionMACAddress.setStatus("current")
_EltPppoeIaSessionPort_Type = InterfaceIndex
_EltPppoeIaSessionPort_Object = MibTableColumn
eltPppoeIaSessionPort = _EltPppoeIaSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 8, 1, 3),
    _EltPppoeIaSessionPort_Type()
)
eltPppoeIaSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaSessionPort.setStatus("current")
_EltPppoeIaSessionID_Type = EltPppoeIaSessionIDType
_EltPppoeIaSessionID_Object = MibTableColumn
eltPppoeIaSessionID = _EltPppoeIaSessionID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 8, 1, 4),
    _EltPppoeIaSessionID_Type()
)
eltPppoeIaSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaSessionID.setStatus("current")
_EltPppoeIaSessionTimer_Type = Unsigned32
_EltPppoeIaSessionTimer_Object = MibTableColumn
eltPppoeIaSessionTimer = _EltPppoeIaSessionTimer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 8, 1, 5),
    _EltPppoeIaSessionTimer_Type()
)
eltPppoeIaSessionTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaSessionTimer.setStatus("current")
_EltPppoeIaSessionRowStatus_Type = RowStatus
_EltPppoeIaSessionRowStatus_Object = MibTableColumn
eltPppoeIaSessionRowStatus = _EltPppoeIaSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 6, 8, 1, 6),
    _EltPppoeIaSessionRowStatus_Type()
)
eltPppoeIaSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPppoeIaSessionRowStatus.setStatus("current")
_EltMesIpArpInspect_ObjectIdentity = ObjectIdentity
eltMesIpArpInspect = _EltMesIpArpInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7)
)
_EltIpArpInspectPortStatTable_Object = MibTable
eltIpArpInspectPortStatTable = _EltIpArpInspectPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 1)
)
if mibBuilder.loadTexts:
    eltIpArpInspectPortStatTable.setStatus("current")
_EltIpArpInspectPortStatEntry_Object = MibTableRow
eltIpArpInspectPortStatEntry = _EltIpArpInspectPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 1, 1)
)
eltIpArpInspectPortStatEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-SECURITY", "eltIpArpInspectPortIndex"),
)
if mibBuilder.loadTexts:
    eltIpArpInspectPortStatEntry.setStatus("current")
_EltIpArpInspectPortIndex_Type = Integer32
_EltIpArpInspectPortIndex_Object = MibTableColumn
eltIpArpInspectPortIndex = _EltIpArpInspectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 1, 1, 1),
    _EltIpArpInspectPortIndex_Type()
)
eltIpArpInspectPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltIpArpInspectPortIndex.setStatus("current")
_EltIpArpInspectPortNumOfArpForwarded_Type = Counter32
_EltIpArpInspectPortNumOfArpForwarded_Object = MibTableColumn
eltIpArpInspectPortNumOfArpForwarded = _EltIpArpInspectPortNumOfArpForwarded_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 1, 1, 2),
    _EltIpArpInspectPortNumOfArpForwarded_Type()
)
eltIpArpInspectPortNumOfArpForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpArpInspectPortNumOfArpForwarded.setStatus("current")
_EltIpArpInspectPortNumOfArpDropped_Type = Counter32
_EltIpArpInspectPortNumOfArpDropped_Object = MibTableColumn
eltIpArpInspectPortNumOfArpDropped = _EltIpArpInspectPortNumOfArpDropped_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 1, 1, 3),
    _EltIpArpInspectPortNumOfArpDropped_Type()
)
eltIpArpInspectPortNumOfArpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpArpInspectPortNumOfArpDropped.setStatus("current")
_EltIpArpInspectPortNumOfArpMismatched_Type = Counter32
_EltIpArpInspectPortNumOfArpMismatched_Object = MibTableColumn
eltIpArpInspectPortNumOfArpMismatched = _EltIpArpInspectPortNumOfArpMismatched_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 1, 1, 4),
    _EltIpArpInspectPortNumOfArpMismatched_Type()
)
eltIpArpInspectPortNumOfArpMismatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpArpInspectPortNumOfArpMismatched.setStatus("current")
_EltIpArpInspectLastDropIP_Type = IpAddress
_EltIpArpInspectLastDropIP_Object = MibTableColumn
eltIpArpInspectLastDropIP = _EltIpArpInspectLastDropIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 1, 1, 5),
    _EltIpArpInspectLastDropIP_Type()
)
eltIpArpInspectLastDropIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpArpInspectLastDropIP.setStatus("current")
_EltIpArpInspectLastDropMac_Type = MacAddress
_EltIpArpInspectLastDropMac_Object = MibTableColumn
eltIpArpInspectLastDropMac = _EltIpArpInspectLastDropMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 1, 1, 6),
    _EltIpArpInspectLastDropMac_Type()
)
eltIpArpInspectLastDropMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpArpInspectLastDropMac.setStatus("current")
_EltIpArpInspectLastDropTime_Type = TimeTicks
_EltIpArpInspectLastDropTime_Object = MibTableColumn
eltIpArpInspectLastDropTime = _EltIpArpInspectLastDropTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 1, 1, 7),
    _EltIpArpInspectLastDropTime_Type()
)
eltIpArpInspectLastDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpArpInspectLastDropTime.setStatus("current")
_EltIpArpInspectEnableVlanTable_Object = MibTable
eltIpArpInspectEnableVlanTable = _EltIpArpInspectEnableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 2)
)
if mibBuilder.loadTexts:
    eltIpArpInspectEnableVlanTable.setStatus("current")
_EltIpArpInspectEnableVlanEntry_Object = MibTableRow
eltIpArpInspectEnableVlanEntry = _EltIpArpInspectEnableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 2, 1)
)
if mibBuilder.loadTexts:
    eltIpArpInspectEnableVlanEntry.setStatus("current")
_EltIpArpInspectVlanLastDropIP_Type = IpAddress
_EltIpArpInspectVlanLastDropIP_Object = MibTableColumn
eltIpArpInspectVlanLastDropIP = _EltIpArpInspectVlanLastDropIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 2, 1, 1),
    _EltIpArpInspectVlanLastDropIP_Type()
)
eltIpArpInspectVlanLastDropIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpArpInspectVlanLastDropIP.setStatus("current")
_EltIpArpInspectVlanLastDropMac_Type = MacAddress
_EltIpArpInspectVlanLastDropMac_Object = MibTableColumn
eltIpArpInspectVlanLastDropMac = _EltIpArpInspectVlanLastDropMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 2, 1, 2),
    _EltIpArpInspectVlanLastDropMac_Type()
)
eltIpArpInspectVlanLastDropMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpArpInspectVlanLastDropMac.setStatus("current")
_EltIpArpInspectVlanLastDropTime_Type = TimeTicks
_EltIpArpInspectVlanLastDropTime_Object = MibTableColumn
eltIpArpInspectVlanLastDropTime = _EltIpArpInspectVlanLastDropTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 2, 1, 3),
    _EltIpArpInspectVlanLastDropTime_Type()
)
eltIpArpInspectVlanLastDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpArpInspectVlanLastDropTime.setStatus("current")
_EltIpArpInspectPortClearCountersAction_Type = PortList
_EltIpArpInspectPortClearCountersAction_Object = MibScalar
eltIpArpInspectPortClearCountersAction = _EltIpArpInspectPortClearCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 7, 3),
    _EltIpArpInspectPortClearCountersAction_Type()
)
eltIpArpInspectPortClearCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpArpInspectPortClearCountersAction.setStatus("current")
rlIpArpInspectEnableVlanEntry.registerAugmentions(
    ("ELTEX-MES-BRIDGE-SECURITY",
     "eltIpArpInspectEnableVlanEntry")
)
eltIpArpInspectEnableVlanEntry.setIndexNames(*rlIpArpInspectEnableVlanEntry.getIndexNames())

# Managed Objects groups


# Notification objects

eltIpDhcpSnoopRateLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112, 1, 0, 1)
)
eltIpDhcpSnoopRateLimitTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ELTEX-MES-BRIDGE-SECURITY", "eltIpDhcpSnoopPortRateLimit"))
)
if mibBuilder.loadTexts:
    eltIpDhcpSnoopRateLimitTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-BRIDGE-SECURITY",
    **{"EltCircuitIdType": EltCircuitIdType,
       "EltRemoteIdType": EltRemoteIdType,
       "EltOpt82CombinationType": EltOpt82CombinationType,
       "EltOpt82DelimiterType": EltOpt82DelimiterType,
       "EltOpt82SuboptionType": EltOpt82SuboptionType,
       "EltDHCPSnoopRateLimitType": EltDHCPSnoopRateLimitType,
       "EltPppoeIaSessionIDType": EltPppoeIaSessionIDType,
       "EltIpv6DhcpGuardRoleType": EltIpv6DhcpGuardRoleType,
       "EltIpv6RaGuardRoleType": EltIpv6RaGuardRoleType,
       "eltMesIpDhcpSnoop": eltMesIpDhcpSnoop,
       "eltMesIpDhcpSnoopNotif": eltMesIpDhcpSnoopNotif,
       "eltIpDhcpSnoopRateLimitTrap": eltIpDhcpSnoopRateLimitTrap,
       "eltIpDhcpOpt82AccessNodeIdentifier": eltIpDhcpOpt82AccessNodeIdentifier,
       "eltIpDhcpOpt82CircuitIdSuboptionsCombination": eltIpDhcpOpt82CircuitIdSuboptionsCombination,
       "eltIpDhcpOpt82CircuitIdSuboptionsDelimeter": eltIpDhcpOpt82CircuitIdSuboptionsDelimeter,
       "eltIpDhcpOpt82PortTable": eltIpDhcpOpt82PortTable,
       "eltIpDhcpOpt82PortEntry": eltIpDhcpOpt82PortEntry,
       "eltIpDhcpOpt82PortCircuitId": eltIpDhcpOpt82PortCircuitId,
       "eltIpDhcpOpt82PortRemoteId": eltIpDhcpOpt82PortRemoteId,
       "eltIpDhcpOpt82PortRowStatus": eltIpDhcpOpt82PortRowStatus,
       "eltIpDhcpOpt82SuboptionType": eltIpDhcpOpt82SuboptionType,
       "eltIpDhcpOpt82RemoteIdentifier": eltIpDhcpOpt82RemoteIdentifier,
       "eltIpDhcpSnoopPortTable": eltIpDhcpSnoopPortTable,
       "eltIpDhcpSnoopPortEntry": eltIpDhcpSnoopPortEntry,
       "eltIpDhcpSnoopPortRateLimit": eltIpDhcpSnoopPortRateLimit,
       "eltIpDhcpSnoopPortRowStatus": eltIpDhcpSnoopPortRowStatus,
       "eltMesIpv6DhcpGuard": eltMesIpv6DhcpGuard,
       "eltIpv6DhcpGuardEnable": eltIpv6DhcpGuardEnable,
       "eltIpv6DhcpGuardEnableTable": eltIpv6DhcpGuardEnableTable,
       "eltIpv6DhcpGuardEnableEntry": eltIpv6DhcpGuardEnableEntry,
       "eltIpv6DhcpGuardEnableVlanTag": eltIpv6DhcpGuardEnableVlanTag,
       "eltIpv6DhcpGuardEnableVlanRowStatus": eltIpv6DhcpGuardEnableVlanRowStatus,
       "eltIpv6DhcpGuardTable": eltIpv6DhcpGuardTable,
       "eltIpv6DhcpGuardEntry": eltIpv6DhcpGuardEntry,
       "eltIpv6DhcpGuardIfIndex": eltIpv6DhcpGuardIfIndex,
       "eltIpv6DhcpGuardRole": eltIpv6DhcpGuardRole,
       "eltIpv6DhcpGuardAcl": eltIpv6DhcpGuardAcl,
       "eltIpv6DhcpGuardPrefList": eltIpv6DhcpGuardPrefList,
       "eltIpv6DhcpGuardTrusted": eltIpv6DhcpGuardTrusted,
       "eltIpv6DhcpGuardRowStatus": eltIpv6DhcpGuardRowStatus,
       "eltMesIpv6RaGuard": eltMesIpv6RaGuard,
       "eltIpv6RaGuardEnable": eltIpv6RaGuardEnable,
       "eltIpv6RaGuardEnableTable": eltIpv6RaGuardEnableTable,
       "eltIpv6RaGuardEnableEntry": eltIpv6RaGuardEnableEntry,
       "eltIpv6RaGuardEnableVlanTag": eltIpv6RaGuardEnableVlanTag,
       "eltIpv6RaGuardEnableVlanRowStatus": eltIpv6RaGuardEnableVlanRowStatus,
       "eltIpv6RaGuardTable": eltIpv6RaGuardTable,
       "eltIpv6RaGuardEntry": eltIpv6RaGuardEntry,
       "eltIpv6RaGuardIfIndex": eltIpv6RaGuardIfIndex,
       "eltIpv6RaGuardRole": eltIpv6RaGuardRole,
       "eltIpv6RaGuardAcl": eltIpv6RaGuardAcl,
       "eltIpv6RaGuardPrefList": eltIpv6RaGuardPrefList,
       "eltIpv6RaGuardTrusted": eltIpv6RaGuardTrusted,
       "eltIpv6RaGuardRowStatus": eltIpv6RaGuardRowStatus,
       "eltIpv6RelayAgentEnable": eltIpv6RelayAgentEnable,
       "eltMesPppoeIa": eltMesPppoeIa,
       "eltPppoeIaEnable": eltPppoeIaEnable,
       "eltPppoeIaAccessNodeIdentifier": eltPppoeIaAccessNodeIdentifier,
       "eltPppoeIaCircuitIdSuboptionsCombination": eltPppoeIaCircuitIdSuboptionsCombination,
       "eltPppoeIaCircuitIdSuboptionsDelimeter": eltPppoeIaCircuitIdSuboptionsDelimeter,
       "eltPppoeIaGenericErrorMessage": eltPppoeIaGenericErrorMessage,
       "eltPppoeIaPortTable": eltPppoeIaPortTable,
       "eltPppoeIaPortEntry": eltPppoeIaPortEntry,
       "eltPppoeIaPortEnabled": eltPppoeIaPortEnabled,
       "eltPppoeIaPortTrusted": eltPppoeIaPortTrusted,
       "eltPppoeIaPortCircuitId": eltPppoeIaPortCircuitId,
       "eltPppoeIaPortRemoteId": eltPppoeIaPortRemoteId,
       "eltPppoeIaPortStripVendorTag": eltPppoeIaPortStripVendorTag,
       "eltPppoeIaPortStatsRxPADI": eltPppoeIaPortStatsRxPADI,
       "eltPppoeIaPortStatsRxPADO": eltPppoeIaPortStatsRxPADO,
       "eltPppoeIaPortStatsRxPADR": eltPppoeIaPortStatsRxPADR,
       "eltPppoeIaPortStatsRxPADS": eltPppoeIaPortStatsRxPADS,
       "eltPppoeIaPortStatsRxPADT": eltPppoeIaPortStatsRxPADT,
       "eltPppoeIaPortStatsTxGenError": eltPppoeIaPortStatsTxGenError,
       "eltPppoeIaPortStatsDroppedResponseFromUntrusted": eltPppoeIaPortStatsDroppedResponseFromUntrusted,
       "eltPppoeIaPortStatsDroppedRequestToUntrusted": eltPppoeIaPortStatsDroppedRequestToUntrusted,
       "eltPppoeIaPortStatsDroppedMalformed": eltPppoeIaPortStatsDroppedMalformed,
       "eltPppoeIaPortStatsClearCountersAction": eltPppoeIaPortStatsClearCountersAction,
       "eltPppoeIaPortRowStatus": eltPppoeIaPortRowStatus,
       "eltPppoeIaClearCountersAction": eltPppoeIaClearCountersAction,
       "eltPppoeIaSessionTable": eltPppoeIaSessionTable,
       "eltPppoeIaSessionEntry": eltPppoeIaSessionEntry,
       "eltPppoeIaSessionVLANTag": eltPppoeIaSessionVLANTag,
       "eltPppoeIaSessionMACAddress": eltPppoeIaSessionMACAddress,
       "eltPppoeIaSessionPort": eltPppoeIaSessionPort,
       "eltPppoeIaSessionID": eltPppoeIaSessionID,
       "eltPppoeIaSessionTimer": eltPppoeIaSessionTimer,
       "eltPppoeIaSessionRowStatus": eltPppoeIaSessionRowStatus,
       "eltMesIpArpInspect": eltMesIpArpInspect,
       "eltIpArpInspectPortStatTable": eltIpArpInspectPortStatTable,
       "eltIpArpInspectPortStatEntry": eltIpArpInspectPortStatEntry,
       "eltIpArpInspectPortIndex": eltIpArpInspectPortIndex,
       "eltIpArpInspectPortNumOfArpForwarded": eltIpArpInspectPortNumOfArpForwarded,
       "eltIpArpInspectPortNumOfArpDropped": eltIpArpInspectPortNumOfArpDropped,
       "eltIpArpInspectPortNumOfArpMismatched": eltIpArpInspectPortNumOfArpMismatched,
       "eltIpArpInspectLastDropIP": eltIpArpInspectLastDropIP,
       "eltIpArpInspectLastDropMac": eltIpArpInspectLastDropMac,
       "eltIpArpInspectLastDropTime": eltIpArpInspectLastDropTime,
       "eltIpArpInspectEnableVlanTable": eltIpArpInspectEnableVlanTable,
       "eltIpArpInspectEnableVlanEntry": eltIpArpInspectEnableVlanEntry,
       "eltIpArpInspectVlanLastDropIP": eltIpArpInspectVlanLastDropIP,
       "eltIpArpInspectVlanLastDropMac": eltIpArpInspectVlanLastDropMac,
       "eltIpArpInspectVlanLastDropTime": eltIpArpInspectVlanLastDropTime,
       "eltIpArpInspectPortClearCountersAction": eltIpArpInspectPortClearCountersAction}
)
