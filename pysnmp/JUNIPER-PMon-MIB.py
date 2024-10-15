# SNMP MIB module (JUNIPER-PMon-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-PMon-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:02 2024
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(jnxMibs,
 jnxPMonNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxPMonNotifications")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxPMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19)
)
jnxPMon.setRevisions(
        ("2002-06-05 00:00",
         "2002-08-27 00:00",
         "2002-09-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxPMonOverloadId(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxPMonFlowTable_Object = MibTable
jnxPMonFlowTable = _JnxPMonFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1)
)
if mibBuilder.loadTexts:
    jnxPMonFlowTable.setStatus("current")
_JnxPMonFlowEntry_Object = MibTableRow
jnxPMonFlowEntry = _JnxPMonFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1)
)
jnxPMonFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPMonFlowEntry.setStatus("current")
_JnxPMonCurrentActiveFlows_Type = Gauge32
_JnxPMonCurrentActiveFlows_Object = MibTableColumn
jnxPMonCurrentActiveFlows = _JnxPMonCurrentActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 1),
    _JnxPMonCurrentActiveFlows_Type()
)
jnxPMonCurrentActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonCurrentActiveFlows.setStatus("current")
_JnxPMonTotalFlows_Type = Counter32
_JnxPMonTotalFlows_Object = MibTableColumn
jnxPMonTotalFlows = _JnxPMonTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 2),
    _JnxPMonTotalFlows_Type()
)
jnxPMonTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTotalFlows.setStatus("current")
_JnxPMonTotalFlowsPackets_Type = Counter64
_JnxPMonTotalFlowsPackets_Object = MibTableColumn
jnxPMonTotalFlowsPackets = _JnxPMonTotalFlowsPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 3),
    _JnxPMonTotalFlowsPackets_Type()
)
jnxPMonTotalFlowsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTotalFlowsPackets.setStatus("current")
_JnxPMonTenSecondAverageFlowPackets_Type = Gauge32
_JnxPMonTenSecondAverageFlowPackets_Object = MibTableColumn
jnxPMonTenSecondAverageFlowPackets = _JnxPMonTenSecondAverageFlowPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 4),
    _JnxPMonTenSecondAverageFlowPackets_Type()
)
jnxPMonTenSecondAverageFlowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTenSecondAverageFlowPackets.setStatus("current")
_JnxPMonTotalFlowsBytes_Type = Counter64
_JnxPMonTotalFlowsBytes_Object = MibTableColumn
jnxPMonTotalFlowsBytes = _JnxPMonTotalFlowsBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 5),
    _JnxPMonTotalFlowsBytes_Type()
)
jnxPMonTotalFlowsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTotalFlowsBytes.setStatus("current")
_JnxPMonTenSecondAverageFlowBytes_Type = Gauge32
_JnxPMonTenSecondAverageFlowBytes_Object = MibTableColumn
jnxPMonTenSecondAverageFlowBytes = _JnxPMonTenSecondAverageFlowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 6),
    _JnxPMonTenSecondAverageFlowBytes_Type()
)
jnxPMonTenSecondAverageFlowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTenSecondAverageFlowBytes.setStatus("current")
_JnxPMonTotalFlowsExpired_Type = Counter32
_JnxPMonTotalFlowsExpired_Object = MibTableColumn
jnxPMonTotalFlowsExpired = _JnxPMonTotalFlowsExpired_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 7),
    _JnxPMonTotalFlowsExpired_Type()
)
jnxPMonTotalFlowsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTotalFlowsExpired.setStatus("current")
_JnxPMonTotalFlowsAged_Type = Counter32
_JnxPMonTotalFlowsAged_Object = MibTableColumn
jnxPMonTotalFlowsAged = _JnxPMonTotalFlowsAged_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 8),
    _JnxPMonTotalFlowsAged_Type()
)
jnxPMonTotalFlowsAged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTotalFlowsAged.setStatus("current")
_JnxPMonTotalFlowsExported_Type = Counter32
_JnxPMonTotalFlowsExported_Object = MibTableColumn
jnxPMonTotalFlowsExported = _JnxPMonTotalFlowsExported_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 9),
    _JnxPMonTotalFlowsExported_Type()
)
jnxPMonTotalFlowsExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTotalFlowsExported.setStatus("current")
_JnxPMonTotalFlowsPacketsExported_Type = Counter32
_JnxPMonTotalFlowsPacketsExported_Object = MibTableColumn
jnxPMonTotalFlowsPacketsExported = _JnxPMonTotalFlowsPacketsExported_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 1, 1, 10),
    _JnxPMonTotalFlowsPacketsExported_Type()
)
jnxPMonTotalFlowsPacketsExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTotalFlowsPacketsExported.setStatus("current")
_JnxPMonErrorTable_Object = MibTable
jnxPMonErrorTable = _JnxPMonErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2)
)
if mibBuilder.loadTexts:
    jnxPMonErrorTable.setStatus("current")
_JnxPMonErrorEntry_Object = MibTableRow
jnxPMonErrorEntry = _JnxPMonErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1)
)
jnxPMonErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPMonErrorEntry.setStatus("current")
_JnxPMonFlowAllocFailures_Type = Counter32
_JnxPMonFlowAllocFailures_Object = MibTableColumn
jnxPMonFlowAllocFailures = _JnxPMonFlowAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 1),
    _JnxPMonFlowAllocFailures_Type()
)
jnxPMonFlowAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonFlowAllocFailures.setStatus("current")
_JnxPMonFlowFreeFailures_Type = Counter32
_JnxPMonFlowFreeFailures_Object = MibTableColumn
jnxPMonFlowFreeFailures = _JnxPMonFlowFreeFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 2),
    _JnxPMonFlowFreeFailures_Type()
)
jnxPMonFlowFreeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonFlowFreeFailures.setStatus("current")
_JnxPMonFreeListFailures_Type = Counter32
_JnxPMonFreeListFailures_Object = MibTableColumn
jnxPMonFreeListFailures = _JnxPMonFreeListFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 3),
    _JnxPMonFreeListFailures_Type()
)
jnxPMonFreeListFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonFreeListFailures.setStatus("current")
_JnxPMonNoMemDrops_Type = Counter64
_JnxPMonNoMemDrops_Object = MibTableColumn
jnxPMonNoMemDrops = _JnxPMonNoMemDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 4),
    _JnxPMonNoMemDrops_Type()
)
jnxPMonNoMemDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonNoMemDrops.setStatus("current")
_JnxPMonNotIPDrops_Type = Counter64
_JnxPMonNotIPDrops_Object = MibTableColumn
jnxPMonNotIPDrops = _JnxPMonNotIPDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 5),
    _JnxPMonNotIPDrops_Type()
)
jnxPMonNotIPDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonNotIPDrops.setStatus("current")
_JnxPMonNotIPv4Drops_Type = Counter64
_JnxPMonNotIPv4Drops_Object = MibTableColumn
jnxPMonNotIPv4Drops = _JnxPMonNotIPv4Drops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 6),
    _JnxPMonNotIPv4Drops_Type()
)
jnxPMonNotIPv4Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonNotIPv4Drops.setStatus("current")
_JnxPMonTooSmallDrops_Type = Counter64
_JnxPMonTooSmallDrops_Object = MibTableColumn
jnxPMonTooSmallDrops = _JnxPMonTooSmallDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 7),
    _JnxPMonTooSmallDrops_Type()
)
jnxPMonTooSmallDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTooSmallDrops.setStatus("current")
_JnxPMonCurrentOverload_Type = JnxPMonOverloadId
_JnxPMonCurrentOverload_Object = MibTableColumn
jnxPMonCurrentOverload = _JnxPMonCurrentOverload_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 8),
    _JnxPMonCurrentOverload_Type()
)
jnxPMonCurrentOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonCurrentOverload.setStatus("current")
_JnxPMonLastOverload_Type = JnxPMonOverloadId
_JnxPMonLastOverload_Object = MibTableColumn
jnxPMonLastOverload = _JnxPMonLastOverload_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 9),
    _JnxPMonLastOverload_Type()
)
jnxPMonLastOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonLastOverload.setStatus("current")
_JnxPMonLastOverloadTime_Type = TimeTicks
_JnxPMonLastOverloadTime_Object = MibTableColumn
jnxPMonLastOverloadTime = _JnxPMonLastOverloadTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 10),
    _JnxPMonLastOverloadTime_Type()
)
jnxPMonLastOverloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonLastOverloadTime.setStatus("current")
_JnxPMonLastOverloadDate_Type = DateAndTime
_JnxPMonLastOverloadDate_Object = MibTableColumn
jnxPMonLastOverloadDate = _JnxPMonLastOverloadDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 11),
    _JnxPMonLastOverloadDate_Type()
)
jnxPMonLastOverloadDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonLastOverloadDate.setStatus("current")


class _JnxPMonLastOverloadEvent_Type(Integer32):
    """Custom type jnxPMonLastOverloadEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 3),
          ("none", 1),
          ("set", 2))
    )


_JnxPMonLastOverloadEvent_Type.__name__ = "Integer32"
_JnxPMonLastOverloadEvent_Object = MibTableColumn
jnxPMonLastOverloadEvent = _JnxPMonLastOverloadEvent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 2, 1, 12),
    _JnxPMonLastOverloadEvent_Type()
)
jnxPMonLastOverloadEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonLastOverloadEvent.setStatus("current")
_JnxPMonMemoryTable_Object = MibTable
jnxPMonMemoryTable = _JnxPMonMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 3)
)
if mibBuilder.loadTexts:
    jnxPMonMemoryTable.setStatus("current")
_JnxPMonMemoryEntry_Object = MibTableRow
jnxPMonMemoryEntry = _JnxPMonMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 3, 1)
)
jnxPMonMemoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPMonMemoryEntry.setStatus("current")
_JnxPMonFlowTotalAlloc_Type = Counter64
_JnxPMonFlowTotalAlloc_Object = MibTableColumn
jnxPMonFlowTotalAlloc = _JnxPMonFlowTotalAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 3, 1, 1),
    _JnxPMonFlowTotalAlloc_Type()
)
jnxPMonFlowTotalAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonFlowTotalAlloc.setStatus("current")
_JnxPMonFlowTotalFree_Type = Counter64
_JnxPMonFlowTotalFree_Object = MibTableColumn
jnxPMonFlowTotalFree = _JnxPMonFlowTotalFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 3, 1, 2),
    _JnxPMonFlowTotalFree_Type()
)
jnxPMonFlowTotalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonFlowTotalFree.setStatus("current")
_JnxPMonFlowMaxAlloc_Type = Counter64
_JnxPMonFlowMaxAlloc_Object = MibTableColumn
jnxPMonFlowMaxAlloc = _JnxPMonFlowMaxAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 3, 1, 3),
    _JnxPMonFlowMaxAlloc_Type()
)
jnxPMonFlowMaxAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonFlowMaxAlloc.setStatus("current")
_JnxPMonAllocPerSecond_Type = Gauge32
_JnxPMonAllocPerSecond_Object = MibTableColumn
jnxPMonAllocPerSecond = _JnxPMonAllocPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 3, 1, 4),
    _JnxPMonAllocPerSecond_Type()
)
jnxPMonAllocPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonAllocPerSecond.setStatus("current")
_JnxPMonFreePerSecond_Type = Gauge32
_JnxPMonFreePerSecond_Object = MibTableColumn
jnxPMonFreePerSecond = _JnxPMonFreePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 3, 1, 5),
    _JnxPMonFreePerSecond_Type()
)
jnxPMonFreePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonFreePerSecond.setStatus("current")
_JnxPMonTotalMemoryUsed_Type = Gauge32
_JnxPMonTotalMemoryUsed_Object = MibTableColumn
jnxPMonTotalMemoryUsed = _JnxPMonTotalMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 3, 1, 6),
    _JnxPMonTotalMemoryUsed_Type()
)
jnxPMonTotalMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTotalMemoryUsed.setStatus("current")
_JnxPMonTotalMemoryFree_Type = Gauge32
_JnxPMonTotalMemoryFree_Object = MibTableColumn
jnxPMonTotalMemoryFree = _JnxPMonTotalMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 19, 3, 1, 7),
    _JnxPMonTotalMemoryFree_Type()
)
jnxPMonTotalMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMonTotalMemoryFree.setStatus("current")
_JnxPMonNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxPMonNotificationPrefix = _JnxPMonNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 7, 0)
)

# Managed Objects groups


# Notification objects

jnxPMonOverloadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 7, 0, 1)
)
jnxPMonOverloadSet.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-PMon-MIB", "jnxPMonLastOverload"),
        ("JUNIPER-PMon-MIB", "jnxPMonCurrentOverload"),
        ("JUNIPER-PMon-MIB", "jnxPMonLastOverloadDate"))
)
if mibBuilder.loadTexts:
    jnxPMonOverloadSet.setStatus(
        "current"
    )

jnxPMonOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 7, 0, 2)
)
jnxPMonOverloadCleared.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-PMon-MIB", "jnxPMonLastOverload"),
        ("JUNIPER-PMon-MIB", "jnxPMonCurrentOverload"),
        ("JUNIPER-PMon-MIB", "jnxPMonLastOverloadDate"))
)
if mibBuilder.loadTexts:
    jnxPMonOverloadCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-PMon-MIB",
    **{"JnxPMonOverloadId": JnxPMonOverloadId,
       "jnxPMon": jnxPMon,
       "jnxPMonFlowTable": jnxPMonFlowTable,
       "jnxPMonFlowEntry": jnxPMonFlowEntry,
       "jnxPMonCurrentActiveFlows": jnxPMonCurrentActiveFlows,
       "jnxPMonTotalFlows": jnxPMonTotalFlows,
       "jnxPMonTotalFlowsPackets": jnxPMonTotalFlowsPackets,
       "jnxPMonTenSecondAverageFlowPackets": jnxPMonTenSecondAverageFlowPackets,
       "jnxPMonTotalFlowsBytes": jnxPMonTotalFlowsBytes,
       "jnxPMonTenSecondAverageFlowBytes": jnxPMonTenSecondAverageFlowBytes,
       "jnxPMonTotalFlowsExpired": jnxPMonTotalFlowsExpired,
       "jnxPMonTotalFlowsAged": jnxPMonTotalFlowsAged,
       "jnxPMonTotalFlowsExported": jnxPMonTotalFlowsExported,
       "jnxPMonTotalFlowsPacketsExported": jnxPMonTotalFlowsPacketsExported,
       "jnxPMonErrorTable": jnxPMonErrorTable,
       "jnxPMonErrorEntry": jnxPMonErrorEntry,
       "jnxPMonFlowAllocFailures": jnxPMonFlowAllocFailures,
       "jnxPMonFlowFreeFailures": jnxPMonFlowFreeFailures,
       "jnxPMonFreeListFailures": jnxPMonFreeListFailures,
       "jnxPMonNoMemDrops": jnxPMonNoMemDrops,
       "jnxPMonNotIPDrops": jnxPMonNotIPDrops,
       "jnxPMonNotIPv4Drops": jnxPMonNotIPv4Drops,
       "jnxPMonTooSmallDrops": jnxPMonTooSmallDrops,
       "jnxPMonCurrentOverload": jnxPMonCurrentOverload,
       "jnxPMonLastOverload": jnxPMonLastOverload,
       "jnxPMonLastOverloadTime": jnxPMonLastOverloadTime,
       "jnxPMonLastOverloadDate": jnxPMonLastOverloadDate,
       "jnxPMonLastOverloadEvent": jnxPMonLastOverloadEvent,
       "jnxPMonMemoryTable": jnxPMonMemoryTable,
       "jnxPMonMemoryEntry": jnxPMonMemoryEntry,
       "jnxPMonFlowTotalAlloc": jnxPMonFlowTotalAlloc,
       "jnxPMonFlowTotalFree": jnxPMonFlowTotalFree,
       "jnxPMonFlowMaxAlloc": jnxPMonFlowMaxAlloc,
       "jnxPMonAllocPerSecond": jnxPMonAllocPerSecond,
       "jnxPMonFreePerSecond": jnxPMonFreePerSecond,
       "jnxPMonTotalMemoryUsed": jnxPMonTotalMemoryUsed,
       "jnxPMonTotalMemoryFree": jnxPMonTotalMemoryFree,
       "jnxPMonNotificationPrefix": jnxPMonNotificationPrefix,
       "jnxPMonOverloadSet": jnxPMonOverloadSet,
       "jnxPMonOverloadCleared": jnxPMonOverloadCleared}
)
