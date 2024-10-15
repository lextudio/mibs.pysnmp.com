# SNMP MIB module (REDSTONE-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:34 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsEnable,) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsEnable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rsDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22)
)
rsDhcpMIB.setRevisions(
        ("1999-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsDhcpObjects_ObjectIdentity = ObjectIdentity
rsDhcpObjects = _RsDhcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 1)
)
_RsDhcpRelay_ObjectIdentity = ObjectIdentity
rsDhcpRelay = _RsDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1)
)
_RsDhcpRelayScalars_ObjectIdentity = ObjectIdentity
rsDhcpRelayScalars = _RsDhcpRelayScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 1)
)
_RsDhcpRelayAgentInfoEnable_Type = RsEnable
_RsDhcpRelayAgentInfoEnable_Object = MibScalar
rsDhcpRelayAgentInfoEnable = _RsDhcpRelayAgentInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 1, 1),
    _RsDhcpRelayAgentInfoEnable_Type()
)
rsDhcpRelayAgentInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDhcpRelayAgentInfoEnable.setStatus("current")
_RsDhcpRelayServerTable_Object = MibTable
rsDhcpRelayServerTable = _RsDhcpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsDhcpRelayServerTable.setStatus("current")
_RsDhcpRelayServerEntry_Object = MibTableRow
rsDhcpRelayServerEntry = _RsDhcpRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 2, 1)
)
rsDhcpRelayServerEntry.setIndexNames(
    (0, "REDSTONE-DHCP-MIB", "rsDhcpRelayServerAddress"),
)
if mibBuilder.loadTexts:
    rsDhcpRelayServerEntry.setStatus("current")
_RsDhcpRelayServerAddress_Type = IpAddress
_RsDhcpRelayServerAddress_Object = MibTableColumn
rsDhcpRelayServerAddress = _RsDhcpRelayServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 2, 1, 1),
    _RsDhcpRelayServerAddress_Type()
)
rsDhcpRelayServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsDhcpRelayServerAddress.setStatus("current")
_RsDhcpRelayServerRowStatus_Type = RowStatus
_RsDhcpRelayServerRowStatus_Object = MibTableColumn
rsDhcpRelayServerRowStatus = _RsDhcpRelayServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 2, 1, 2),
    _RsDhcpRelayServerRowStatus_Type()
)
rsDhcpRelayServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsDhcpRelayServerRowStatus.setStatus("current")
_RsDhcpProxy_ObjectIdentity = ObjectIdentity
rsDhcpProxy = _RsDhcpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 2)
)
_RsDhcpMIBConformance_ObjectIdentity = ObjectIdentity
rsDhcpMIBConformance = _RsDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 4)
)
_RsDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
rsDhcpMIBCompliances = _RsDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 4, 1)
)
_RsDhcpMIBGroups_ObjectIdentity = ObjectIdentity
rsDhcpMIBGroups = _RsDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 4, 2)
)

# Managed Objects groups

rsDhcpRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 4, 2, 1)
)
rsDhcpRelayGroup.setObjects(
      *(("REDSTONE-DHCP-MIB", "rsDhcpRelayAgentInfoEnable"),
        ("REDSTONE-DHCP-MIB", "rsDhcpRelayServerRowStatus"))
)
if mibBuilder.loadTexts:
    rsDhcpRelayGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsDhcpRelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 22, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsDhcpRelayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-DHCP-MIB",
    **{"rsDhcpMIB": rsDhcpMIB,
       "rsDhcpObjects": rsDhcpObjects,
       "rsDhcpRelay": rsDhcpRelay,
       "rsDhcpRelayScalars": rsDhcpRelayScalars,
       "rsDhcpRelayAgentInfoEnable": rsDhcpRelayAgentInfoEnable,
       "rsDhcpRelayServerTable": rsDhcpRelayServerTable,
       "rsDhcpRelayServerEntry": rsDhcpRelayServerEntry,
       "rsDhcpRelayServerAddress": rsDhcpRelayServerAddress,
       "rsDhcpRelayServerRowStatus": rsDhcpRelayServerRowStatus,
       "rsDhcpProxy": rsDhcpProxy,
       "rsDhcpMIBConformance": rsDhcpMIBConformance,
       "rsDhcpMIBCompliances": rsDhcpMIBCompliances,
       "rsDhcpRelayCompliance": rsDhcpRelayCompliance,
       "rsDhcpMIBGroups": rsDhcpMIBGroups,
       "rsDhcpRelayGroup": rsDhcpRelayGroup}
)
