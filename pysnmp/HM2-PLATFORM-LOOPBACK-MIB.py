# SNMP MIB module (HM2-PLATFORM-LOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-LOOPBACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:13 2024
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

(hm2PlatformMibs,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "hm2PlatformMibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hm2PlatformLoopback = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 22)
)
hm2PlatformLoopback.setRevisions(
        ("2011-09-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentLoopbackGroup_ObjectIdentity = ObjectIdentity
hm2AgentLoopbackGroup = _Hm2AgentLoopbackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 22, 1)
)
_Hm2AgentLoopbackTable_Object = MibTable
hm2AgentLoopbackTable = _Hm2AgentLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 22, 1, 1)
)
if mibBuilder.loadTexts:
    hm2AgentLoopbackTable.setStatus("current")
_Hm2AgentLoopbackEntry_Object = MibTableRow
hm2AgentLoopbackEntry = _Hm2AgentLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 22, 1, 1, 1)
)
hm2AgentLoopbackEntry.setIndexNames(
    (0, "HM2-PLATFORM-LOOPBACK-MIB", "hm2AgentLoopbackID"),
)
if mibBuilder.loadTexts:
    hm2AgentLoopbackEntry.setStatus("current")


class _Hm2AgentLoopbackID_Type(Integer32):
    """Custom type hm2AgentLoopbackID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentLoopbackID_Type.__name__ = "Integer32"
_Hm2AgentLoopbackID_Object = MibTableColumn
hm2AgentLoopbackID = _Hm2AgentLoopbackID_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 22, 1, 1, 1, 1),
    _Hm2AgentLoopbackID_Type()
)
hm2AgentLoopbackID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentLoopbackID.setStatus("current")
_Hm2AgentLoopbackIfIndex_Type = InterfaceIndex
_Hm2AgentLoopbackIfIndex_Object = MibTableColumn
hm2AgentLoopbackIfIndex = _Hm2AgentLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 22, 1, 1, 1, 2),
    _Hm2AgentLoopbackIfIndex_Type()
)
hm2AgentLoopbackIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLoopbackIfIndex.setStatus("current")
_Hm2AgentLoopbackIPAddress_Type = InetAddressIPv4
_Hm2AgentLoopbackIPAddress_Object = MibTableColumn
hm2AgentLoopbackIPAddress = _Hm2AgentLoopbackIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 22, 1, 1, 1, 3),
    _Hm2AgentLoopbackIPAddress_Type()
)
hm2AgentLoopbackIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentLoopbackIPAddress.setStatus("current")
_Hm2AgentLoopbackIPSubnet_Type = InetAddressIPv4
_Hm2AgentLoopbackIPSubnet_Object = MibTableColumn
hm2AgentLoopbackIPSubnet = _Hm2AgentLoopbackIPSubnet_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 22, 1, 1, 1, 4),
    _Hm2AgentLoopbackIPSubnet_Type()
)
hm2AgentLoopbackIPSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentLoopbackIPSubnet.setStatus("current")
_Hm2AgentLoopbackStatus_Type = RowStatus
_Hm2AgentLoopbackStatus_Object = MibTableColumn
hm2AgentLoopbackStatus = _Hm2AgentLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 22, 1, 1, 1, 5),
    _Hm2AgentLoopbackStatus_Type()
)
hm2AgentLoopbackStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLoopbackStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-LOOPBACK-MIB",
    **{"hm2PlatformLoopback": hm2PlatformLoopback,
       "hm2AgentLoopbackGroup": hm2AgentLoopbackGroup,
       "hm2AgentLoopbackTable": hm2AgentLoopbackTable,
       "hm2AgentLoopbackEntry": hm2AgentLoopbackEntry,
       "hm2AgentLoopbackID": hm2AgentLoopbackID,
       "hm2AgentLoopbackIfIndex": hm2AgentLoopbackIfIndex,
       "hm2AgentLoopbackIPAddress": hm2AgentLoopbackIPAddress,
       "hm2AgentLoopbackIPSubnet": hm2AgentLoopbackIPSubnet,
       "hm2AgentLoopbackStatus": hm2AgentLoopbackStatus}
)
