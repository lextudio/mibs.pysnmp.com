# SNMP MIB module (HP-ICF-URPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-URPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:23 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfUrpfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131)
)
hpicfUrpfMIB.setRevisions(
        ("2016-06-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfUrpfConfig_ObjectIdentity = ObjectIdentity
hpicfUrpfConfig = _HpicfUrpfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1)
)


class _HpicfUrpfConfigGlobalEnable_Type(TruthValue):
    """Custom type hpicfUrpfConfigGlobalEnable based on TruthValue"""


_HpicfUrpfConfigGlobalEnable_Object = MibScalar
hpicfUrpfConfigGlobalEnable = _HpicfUrpfConfigGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 1),
    _HpicfUrpfConfigGlobalEnable_Type()
)
hpicfUrpfConfigGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUrpfConfigGlobalEnable.setStatus("current")


class _HpicfUrpfConfigGlobalLogTimeout_Type(Integer32):
    """Custom type hpicfUrpfConfigGlobalLogTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_HpicfUrpfConfigGlobalLogTimeout_Type.__name__ = "Integer32"
_HpicfUrpfConfigGlobalLogTimeout_Object = MibScalar
hpicfUrpfConfigGlobalLogTimeout = _HpicfUrpfConfigGlobalLogTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 2),
    _HpicfUrpfConfigGlobalLogTimeout_Type()
)
hpicfUrpfConfigGlobalLogTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUrpfConfigGlobalLogTimeout.setStatus("current")
_HpicfUrpfConfigTable_Object = MibTable
hpicfUrpfConfigTable = _HpicfUrpfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfUrpfConfigTable.setStatus("current")
_HpicfUrpfConfigEntry_Object = MibTableRow
hpicfUrpfConfigEntry = _HpicfUrpfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1)
)
hpicfUrpfConfigEntry.setIndexNames(
    (0, "HP-ICF-URPF-MIB", "hpicfUrpfIfIndex"),
    (0, "HP-ICF-URPF-MIB", "hpicfUrpfAddrFamily"),
)
if mibBuilder.loadTexts:
    hpicfUrpfConfigEntry.setStatus("current")
_HpicfUrpfIfIndex_Type = InterfaceIndex
_HpicfUrpfIfIndex_Object = MibTableColumn
hpicfUrpfIfIndex = _HpicfUrpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 1),
    _HpicfUrpfIfIndex_Type()
)
hpicfUrpfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUrpfIfIndex.setStatus("current")
_HpicfUrpfAddrFamily_Type = InetAddressType
_HpicfUrpfAddrFamily_Object = MibTableColumn
hpicfUrpfAddrFamily = _HpicfUrpfAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 2),
    _HpicfUrpfAddrFamily_Type()
)
hpicfUrpfAddrFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUrpfAddrFamily.setStatus("current")


class _HpicfUrpfConfigMode_Type(Integer32):
    """Custom type hpicfUrpfConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loose", 3),
          ("none", 1),
          ("strict", 2))
    )


_HpicfUrpfConfigMode_Type.__name__ = "Integer32"
_HpicfUrpfConfigMode_Object = MibTableColumn
hpicfUrpfConfigMode = _HpicfUrpfConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 3),
    _HpicfUrpfConfigMode_Type()
)
hpicfUrpfConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUrpfConfigMode.setStatus("current")


class _HpicfUrpfConfigDefRoute_Type(TruthValue):
    """Custom type hpicfUrpfConfigDefRoute based on TruthValue"""


_HpicfUrpfConfigDefRoute_Object = MibTableColumn
hpicfUrpfConfigDefRoute = _HpicfUrpfConfigDefRoute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 4),
    _HpicfUrpfConfigDefRoute_Type()
)
hpicfUrpfConfigDefRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUrpfConfigDefRoute.setStatus("current")


class _HpicfUrpfConfigAllowDhcp_Type(TruthValue):
    """Custom type hpicfUrpfConfigAllowDhcp based on TruthValue"""


_HpicfUrpfConfigAllowDhcp_Object = MibTableColumn
hpicfUrpfConfigAllowDhcp = _HpicfUrpfConfigAllowDhcp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 5),
    _HpicfUrpfConfigAllowDhcp_Type()
)
hpicfUrpfConfigAllowDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUrpfConfigAllowDhcp.setStatus("current")


class _HpicfUrpfConfigLogging_Type(TruthValue):
    """Custom type hpicfUrpfConfigLogging based on TruthValue"""


_HpicfUrpfConfigLogging_Object = MibTableColumn
hpicfUrpfConfigLogging = _HpicfUrpfConfigLogging_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 6),
    _HpicfUrpfConfigLogging_Type()
)
hpicfUrpfConfigLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUrpfConfigLogging.setStatus("current")


class _HpicfUrpfConfigHasWhitelistAcl_Type(TruthValue):
    """Custom type hpicfUrpfConfigHasWhitelistAcl based on TruthValue"""


_HpicfUrpfConfigHasWhitelistAcl_Object = MibTableColumn
hpicfUrpfConfigHasWhitelistAcl = _HpicfUrpfConfigHasWhitelistAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 7),
    _HpicfUrpfConfigHasWhitelistAcl_Type()
)
hpicfUrpfConfigHasWhitelistAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUrpfConfigHasWhitelistAcl.setStatus("current")
_HpicfUrpfConfigWhitelistAclName_Type = SnmpAdminString
_HpicfUrpfConfigWhitelistAclName_Object = MibTableColumn
hpicfUrpfConfigWhitelistAclName = _HpicfUrpfConfigWhitelistAclName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 8),
    _HpicfUrpfConfigWhitelistAclName_Type()
)
hpicfUrpfConfigWhitelistAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUrpfConfigWhitelistAclName.setStatus("current")
_HpicfUrpfStats_ObjectIdentity = ObjectIdentity
hpicfUrpfStats = _HpicfUrpfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2)
)
_HpicfUrpfStatsTable_Object = MibTable
hpicfUrpfStatsTable = _HpicfUrpfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfUrpfStatsTable.setStatus("current")
_HpicfUrpfStatsEntry_Object = MibTableRow
hpicfUrpfStatsEntry = _HpicfUrpfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2, 1, 1)
)
hpicfUrpfStatsEntry.setIndexNames(
    (0, "HP-ICF-URPF-MIB", "hpicfUrpfIfIndex"),
    (0, "HP-ICF-URPF-MIB", "hpicfUrpfAddrFamily"),
)
if mibBuilder.loadTexts:
    hpicfUrpfStatsEntry.setStatus("current")
_HpicfUrpfStatsBlockedPackets_Type = Counter64
_HpicfUrpfStatsBlockedPackets_Object = MibTableColumn
hpicfUrpfStatsBlockedPackets = _HpicfUrpfStatsBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2, 1, 1, 1),
    _HpicfUrpfStatsBlockedPackets_Type()
)
hpicfUrpfStatsBlockedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUrpfStatsBlockedPackets.setStatus("current")
_HpicfUrpfStatsBlockedOctets_Type = Counter64
_HpicfUrpfStatsBlockedOctets_Object = MibTableColumn
hpicfUrpfStatsBlockedOctets = _HpicfUrpfStatsBlockedOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2, 1, 1, 2),
    _HpicfUrpfStatsBlockedOctets_Type()
)
hpicfUrpfStatsBlockedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUrpfStatsBlockedOctets.setStatus("current")
_HpicfUrpfConformance_ObjectIdentity = ObjectIdentity
hpicfUrpfConformance = _HpicfUrpfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3)
)
_HpicfUrpfMIBGroups_ObjectIdentity = ObjectIdentity
hpicfUrpfMIBGroups = _HpicfUrpfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 1)
)
_HpicfUrpfMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfUrpfMIBCompliances = _HpicfUrpfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 2)
)

# Managed Objects groups

hpicfUrpfScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 1, 1)
)
hpicfUrpfScalarGroup.setObjects(
      *(("HP-ICF-URPF-MIB", "hpicfUrpfConfigGlobalEnable"),
        ("HP-ICF-URPF-MIB", "hpicfUrpfConfigGlobalLogTimeout"))
)
if mibBuilder.loadTexts:
    hpicfUrpfScalarGroup.setStatus("current")

hpicfUrpfConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 1, 2)
)
hpicfUrpfConfigTableGroup.setObjects(
      *(("HP-ICF-URPF-MIB", "hpicfUrpfConfigMode"),
        ("HP-ICF-URPF-MIB", "hpicfUrpfConfigDefRoute"),
        ("HP-ICF-URPF-MIB", "hpicfUrpfConfigAllowDhcp"),
        ("HP-ICF-URPF-MIB", "hpicfUrpfConfigLogging"),
        ("HP-ICF-URPF-MIB", "hpicfUrpfConfigHasWhitelistAcl"),
        ("HP-ICF-URPF-MIB", "hpicfUrpfConfigWhitelistAclName"))
)
if mibBuilder.loadTexts:
    hpicfUrpfConfigTableGroup.setStatus("current")

hpicfUrpfStatsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 1, 3)
)
hpicfUrpfStatsTableGroup.setObjects(
      *(("HP-ICF-URPF-MIB", "hpicfUrpfStatsBlockedPackets"),
        ("HP-ICF-URPF-MIB", "hpicfUrpfStatsBlockedOctets"))
)
if mibBuilder.loadTexts:
    hpicfUrpfStatsTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfUrpfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfUrpfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-URPF-MIB",
    **{"hpicfUrpfMIB": hpicfUrpfMIB,
       "hpicfUrpfConfig": hpicfUrpfConfig,
       "hpicfUrpfConfigGlobalEnable": hpicfUrpfConfigGlobalEnable,
       "hpicfUrpfConfigGlobalLogTimeout": hpicfUrpfConfigGlobalLogTimeout,
       "hpicfUrpfConfigTable": hpicfUrpfConfigTable,
       "hpicfUrpfConfigEntry": hpicfUrpfConfigEntry,
       "hpicfUrpfIfIndex": hpicfUrpfIfIndex,
       "hpicfUrpfAddrFamily": hpicfUrpfAddrFamily,
       "hpicfUrpfConfigMode": hpicfUrpfConfigMode,
       "hpicfUrpfConfigDefRoute": hpicfUrpfConfigDefRoute,
       "hpicfUrpfConfigAllowDhcp": hpicfUrpfConfigAllowDhcp,
       "hpicfUrpfConfigLogging": hpicfUrpfConfigLogging,
       "hpicfUrpfConfigHasWhitelistAcl": hpicfUrpfConfigHasWhitelistAcl,
       "hpicfUrpfConfigWhitelistAclName": hpicfUrpfConfigWhitelistAclName,
       "hpicfUrpfStats": hpicfUrpfStats,
       "hpicfUrpfStatsTable": hpicfUrpfStatsTable,
       "hpicfUrpfStatsEntry": hpicfUrpfStatsEntry,
       "hpicfUrpfStatsBlockedPackets": hpicfUrpfStatsBlockedPackets,
       "hpicfUrpfStatsBlockedOctets": hpicfUrpfStatsBlockedOctets,
       "hpicfUrpfConformance": hpicfUrpfConformance,
       "hpicfUrpfMIBGroups": hpicfUrpfMIBGroups,
       "hpicfUrpfScalarGroup": hpicfUrpfScalarGroup,
       "hpicfUrpfConfigTableGroup": hpicfUrpfConfigTableGroup,
       "hpicfUrpfStatsTableGroup": hpicfUrpfStatsTableGroup,
       "hpicfUrpfMIBCompliances": hpicfUrpfMIBCompliances,
       "hpicfUrpfMIBCompliance": hpicfUrpfMIBCompliance}
)
