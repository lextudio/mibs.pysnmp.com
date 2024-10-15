# SNMP MIB module (HM2-PLATFORM-MRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-MRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:14 2024
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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

hm2PlatformMRP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60)
)
hm2PlatformMRP.setRevisions(
        ("2013-04-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentDot1qMrp_ObjectIdentity = ObjectIdentity
hm2AgentDot1qMrp = _Hm2AgentDot1qMrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 1)
)
_Hm2AgentDot1qPortMrpTable_Object = MibTable
hm2AgentDot1qPortMrpTable = _Hm2AgentDot1qPortMrpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMrpTable.setStatus("current")
_Hm2AgentDot1qPortMrpEntry_Object = MibTableRow
hm2AgentDot1qPortMrpEntry = _Hm2AgentDot1qPortMrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1)
)
hm2AgentDot1qPortMrpEntry.setIndexNames(
    (0, "HM2-PLATFORM-MRP-MIB", "hm2AgentDot1qMrpPort"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMrpEntry.setStatus("current")


class _Hm2AgentDot1qMrpPort_Type(Integer32):
    """Custom type hm2AgentDot1qMrpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentDot1qMrpPort_Type.__name__ = "Integer32"
_Hm2AgentDot1qMrpPort_Object = MibTableColumn
hm2AgentDot1qMrpPort = _Hm2AgentDot1qMrpPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1, 1),
    _Hm2AgentDot1qMrpPort_Type()
)
hm2AgentDot1qMrpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpPort.setStatus("current")


class _Hm2AgentDot1qPortMrpJoinTime_Type(TimeInterval):
    """Custom type hm2AgentDot1qPortMrpJoinTime based on TimeInterval"""
    defaultValue = 20

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_Hm2AgentDot1qPortMrpJoinTime_Type.__name__ = "TimeInterval"
_Hm2AgentDot1qPortMrpJoinTime_Object = MibTableColumn
hm2AgentDot1qPortMrpJoinTime = _Hm2AgentDot1qPortMrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1, 2),
    _Hm2AgentDot1qPortMrpJoinTime_Type()
)
hm2AgentDot1qPortMrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMrpJoinTime.setStatus("current")


class _Hm2AgentDot1qPortMrpLeaveTime_Type(TimeInterval):
    """Custom type hm2AgentDot1qPortMrpLeaveTime based on TimeInterval"""
    defaultValue = 60

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 600),
    )


_Hm2AgentDot1qPortMrpLeaveTime_Type.__name__ = "TimeInterval"
_Hm2AgentDot1qPortMrpLeaveTime_Object = MibTableColumn
hm2AgentDot1qPortMrpLeaveTime = _Hm2AgentDot1qPortMrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1, 3),
    _Hm2AgentDot1qPortMrpLeaveTime_Type()
)
hm2AgentDot1qPortMrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMrpLeaveTime.setStatus("current")


class _Hm2AgentDot1qPortMrpLeaveAllTime_Type(TimeInterval):
    """Custom type hm2AgentDot1qPortMrpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 6000),
    )


_Hm2AgentDot1qPortMrpLeaveAllTime_Type.__name__ = "TimeInterval"
_Hm2AgentDot1qPortMrpLeaveAllTime_Object = MibTableColumn
hm2AgentDot1qPortMrpLeaveAllTime = _Hm2AgentDot1qPortMrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1, 4),
    _Hm2AgentDot1qPortMrpLeaveAllTime_Type()
)
hm2AgentDot1qPortMrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMrpLeaveAllTime.setStatus("current")
_Hm2AgentDot1qMrpMxrp_ObjectIdentity = ObjectIdentity
hm2AgentDot1qMrpMxrp = _Hm2AgentDot1qMrpMxrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-MRP-MIB",
    **{"hm2PlatformMRP": hm2PlatformMRP,
       "hm2AgentDot1qMrp": hm2AgentDot1qMrp,
       "hm2AgentDot1qPortMrpTable": hm2AgentDot1qPortMrpTable,
       "hm2AgentDot1qPortMrpEntry": hm2AgentDot1qPortMrpEntry,
       "hm2AgentDot1qMrpPort": hm2AgentDot1qMrpPort,
       "hm2AgentDot1qPortMrpJoinTime": hm2AgentDot1qPortMrpJoinTime,
       "hm2AgentDot1qPortMrpLeaveTime": hm2AgentDot1qPortMrpLeaveTime,
       "hm2AgentDot1qPortMrpLeaveAllTime": hm2AgentDot1qPortMrpLeaveAllTime,
       "hm2AgentDot1qMrpMxrp": hm2AgentDot1qMrpMxrp}
)
