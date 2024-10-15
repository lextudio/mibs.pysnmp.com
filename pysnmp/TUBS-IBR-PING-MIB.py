# SNMP MIB module (TUBS-IBR-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TUBS-IBR-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:55 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(ibr,) = mibBuilder.importSymbols(
    "TUBS-SMI",
    "ibr")


# MODULE-IDENTITY

pingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8)
)
pingMIB.setRevisions(
        ("2000-07-07 00:00",
         "2000-03-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PingNotifications_ObjectIdentity = ObjectIdentity
pingNotifications = _PingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 0)
)
_PingObjects_ObjectIdentity = ObjectIdentity
pingObjects = _PingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 1)
)
_PingTable_Object = MibTable
pingTable = _PingTable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    pingTable.setStatus("current")
_PingEntry_Object = MibTableRow
pingEntry = _PingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 1, 1, 1)
)
pingEntry.setIndexNames(
    (0, "TUBS-IBR-PING-MIB", "pingIndex"),
)
if mibBuilder.loadTexts:
    pingEntry.setStatus("current")
_PingIndex_Type = Unsigned32
_PingIndex_Object = MibTableColumn
pingIndex = _PingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 1, 1, 1, 1),
    _PingIndex_Type()
)
pingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingIndex.setStatus("current")
_PingAddress_Type = IpAddress
_PingAddress_Object = MibTableColumn
pingAddress = _PingAddress_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 1, 1, 1, 2),
    _PingAddress_Type()
)
pingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingAddress.setStatus("current")
_PingRtt_Type = Unsigned32
_PingRtt_Object = MibTableColumn
pingRtt = _PingRtt_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 1, 1, 1, 3),
    _PingRtt_Type()
)
pingRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingRtt.setStatus("current")
if mibBuilder.loadTexts:
    pingRtt.setUnits("milliseconds")
_PingStatistics_ObjectIdentity = ObjectIdentity
pingStatistics = _PingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 1, 2)
)
_PingTimeout_Type = Unsigned32
_PingTimeout_Object = MibScalar
pingTimeout = _PingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 1, 2, 1),
    _PingTimeout_Type()
)
pingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pingTimeout.setUnits("milliseconds")
_PingAvgRtt_Type = Unsigned32
_PingAvgRtt_Object = MibScalar
pingAvgRtt = _PingAvgRtt_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 1, 2, 2),
    _PingAvgRtt_Type()
)
pingAvgRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingAvgRtt.setStatus("current")
if mibBuilder.loadTexts:
    pingAvgRtt.setUnits("milliseconds")

# Managed Objects groups


# Notification objects

pingNoResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 1575, 1, 8, 0, 1)
)
pingNoResponse.setObjects(
      *(("TUBS-IBR-PING-MIB", "pingRtt"),
        ("TUBS-IBR-PING-MIB", "pingTimeout"))
)
if mibBuilder.loadTexts:
    pingNoResponse.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TUBS-IBR-PING-MIB",
    **{"pingMIB": pingMIB,
       "pingNotifications": pingNotifications,
       "pingNoResponse": pingNoResponse,
       "pingObjects": pingObjects,
       "pingTable": pingTable,
       "pingEntry": pingEntry,
       "pingIndex": pingIndex,
       "pingAddress": pingAddress,
       "pingRtt": pingRtt,
       "pingStatistics": pingStatistics,
       "pingTimeout": pingTimeout,
       "pingAvgRtt": pingAvgRtt}
)
