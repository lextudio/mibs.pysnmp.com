# SNMP MIB module (DNOS-LOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-LOOPBACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:59 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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


# MODULE-IDENTITY

fastPathLoopback = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22)
)
fastPathLoopback.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentLoopbackGroup_ObjectIdentity = ObjectIdentity
agentLoopbackGroup = _AgentLoopbackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1)
)
_AgentLoopbackTable_Object = MibTable
agentLoopbackTable = _AgentLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1)
)
if mibBuilder.loadTexts:
    agentLoopbackTable.setStatus("current")
_AgentLoopbackEntry_Object = MibTableRow
agentLoopbackEntry = _AgentLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1)
)
agentLoopbackEntry.setIndexNames(
    (0, "DNOS-LOOPBACK-MIB", "agentLoopbackID"),
)
if mibBuilder.loadTexts:
    agentLoopbackEntry.setStatus("current")


class _AgentLoopbackID_Type(Integer32):
    """Custom type agentLoopbackID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentLoopbackID_Type.__name__ = "Integer32"
_AgentLoopbackID_Object = MibTableColumn
agentLoopbackID = _AgentLoopbackID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 1),
    _AgentLoopbackID_Type()
)
agentLoopbackID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLoopbackID.setStatus("current")
_AgentLoopbackIfIndex_Type = Integer32
_AgentLoopbackIfIndex_Object = MibTableColumn
agentLoopbackIfIndex = _AgentLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 2),
    _AgentLoopbackIfIndex_Type()
)
agentLoopbackIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoopbackIfIndex.setStatus("current")
_AgentLoopbackIPAddress_Type = InetAddressIPv4
_AgentLoopbackIPAddress_Object = MibTableColumn
agentLoopbackIPAddress = _AgentLoopbackIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 3),
    _AgentLoopbackIPAddress_Type()
)
agentLoopbackIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLoopbackIPAddress.setStatus("current")
_AgentLoopbackIPSubnet_Type = InetAddressIPv4
_AgentLoopbackIPSubnet_Object = MibTableColumn
agentLoopbackIPSubnet = _AgentLoopbackIPSubnet_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 4),
    _AgentLoopbackIPSubnet_Type()
)
agentLoopbackIPSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLoopbackIPSubnet.setStatus("current")
_AgentLoopbackStatus_Type = RowStatus
_AgentLoopbackStatus_Object = MibTableColumn
agentLoopbackStatus = _AgentLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 5),
    _AgentLoopbackStatus_Type()
)
agentLoopbackStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLoopbackStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-LOOPBACK-MIB",
    **{"fastPathLoopback": fastPathLoopback,
       "agentLoopbackGroup": agentLoopbackGroup,
       "agentLoopbackTable": agentLoopbackTable,
       "agentLoopbackEntry": agentLoopbackEntry,
       "agentLoopbackID": agentLoopbackID,
       "agentLoopbackIfIndex": agentLoopbackIfIndex,
       "agentLoopbackIPAddress": agentLoopbackIPAddress,
       "agentLoopbackIPSubnet": agentLoopbackIPSubnet,
       "agentLoopbackStatus": agentLoopbackStatus}
)
