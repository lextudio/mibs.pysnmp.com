# SNMP MIB module (AT-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:27 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58)
)
ping.setRevisions(
        ("2006-06-28 12:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PingTraps_ObjectIdentity = ObjectIdentity
pingTraps = _PingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 0)
)
_PingTable_Object = MibTable
pingTable = _PingTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1)
)
if mibBuilder.loadTexts:
    pingTable.setStatus("current")
_PingEntry_Object = MibTableRow
pingEntry = _PingEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1)
)
pingEntry.setIndexNames(
    (0, "AT-PING-MIB", "pingIndex"),
)
if mibBuilder.loadTexts:
    pingEntry.setStatus("current")


class _PingIndex_Type(Integer32):
    """Custom type pingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_PingIndex_Type.__name__ = "Integer32"
_PingIndex_Object = MibTableColumn
pingIndex = _PingIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 1),
    _PingIndex_Type()
)
pingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingIndex.setStatus("current")


class _PingProtocol_Type(Integer32):
    """Custom type pingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("apple", 1),
          ("ip", 2),
          ("ipx", 3),
          ("osi", 4),
          ("undefined", 0))
    )


_PingProtocol_Type.__name__ = "Integer32"
_PingProtocol_Object = MibTableColumn
pingProtocol = _PingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 2),
    _PingProtocol_Type()
)
pingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingProtocol.setStatus("current")
_PingAddress_Type = OctetString
_PingAddress_Object = MibTableColumn
pingAddress = _PingAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 3),
    _PingAddress_Type()
)
pingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingAddress.setStatus("current")


class _PingNumberOfPackets_Type(Integer32):
    """Custom type pingNumberOfPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PingNumberOfPackets_Type.__name__ = "Integer32"
_PingNumberOfPackets_Object = MibTableColumn
pingNumberOfPackets = _PingNumberOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 4),
    _PingNumberOfPackets_Type()
)
pingNumberOfPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingNumberOfPackets.setStatus("current")


class _PingPacketSize_Type(Integer32):
    """Custom type pingPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_PingPacketSize_Type.__name__ = "Integer32"
_PingPacketSize_Object = MibTableColumn
pingPacketSize = _PingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 5),
    _PingPacketSize_Type()
)
pingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingPacketSize.setStatus("current")


class _PingTimeout_Type(Integer32):
    """Custom type pingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PingTimeout_Type.__name__ = "Integer32"
_PingTimeout_Object = MibTableColumn
pingTimeout = _PingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 6),
    _PingTimeout_Type()
)
pingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTimeout.setStatus("current")


class _PingDelay_Type(Integer32):
    """Custom type pingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PingDelay_Type.__name__ = "Integer32"
_PingDelay_Object = MibTableColumn
pingDelay = _PingDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 7),
    _PingDelay_Type()
)
pingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingDelay.setStatus("current")
_PingTrapOnCompletion_Type = TruthValue
_PingTrapOnCompletion_Object = MibTableColumn
pingTrapOnCompletion = _PingTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 8),
    _PingTrapOnCompletion_Type()
)
pingTrapOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTrapOnCompletion.setStatus("current")


class _PingTypeOfService_Type(Integer32):
    """Custom type pingTypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PingTypeOfService_Type.__name__ = "Integer32"
_PingTypeOfService_Object = MibTableColumn
pingTypeOfService = _PingTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 9),
    _PingTypeOfService_Type()
)
pingTypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTypeOfService.setStatus("current")
_PingPattern_Type = Unsigned32
_PingPattern_Object = MibTableColumn
pingPattern = _PingPattern_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 10),
    _PingPattern_Type()
)
pingPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingPattern.setStatus("current")


class _PingStatus_Type(Integer32):
    """Custom type pingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startRunning", 1),
          ("stopStopped", 2))
    )


_PingStatus_Type.__name__ = "Integer32"
_PingStatus_Object = MibScalar
pingStatus = _PingStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 2),
    _PingStatus_Type()
)
pingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingStatus.setStatus("current")
_PingStatistics_ObjectIdentity = ObjectIdentity
pingStatistics = _PingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3)
)
_PingSentPackets_Type = Integer32
_PingSentPackets_Object = MibScalar
pingSentPackets = _PingSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 1),
    _PingSentPackets_Type()
)
pingSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingSentPackets.setStatus("current")
_PingReceivedPackets_Type = Integer32
_PingReceivedPackets_Object = MibScalar
pingReceivedPackets = _PingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 2),
    _PingReceivedPackets_Type()
)
pingReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingReceivedPackets.setStatus("current")
_PingMinimumRoundTripTime_Type = Integer32
_PingMinimumRoundTripTime_Object = MibScalar
pingMinimumRoundTripTime = _PingMinimumRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 3),
    _PingMinimumRoundTripTime_Type()
)
pingMinimumRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingMinimumRoundTripTime.setStatus("current")
_PingAverageRoundTripTime_Type = Integer32
_PingAverageRoundTripTime_Object = MibScalar
pingAverageRoundTripTime = _PingAverageRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 4),
    _PingAverageRoundTripTime_Type()
)
pingAverageRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingAverageRoundTripTime.setStatus("current")
_PingMaximumRoundTripTime_Type = Integer32
_PingMaximumRoundTripTime_Object = MibScalar
pingMaximumRoundTripTime = _PingMaximumRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 5),
    _PingMaximumRoundTripTime_Type()
)
pingMaximumRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingMaximumRoundTripTime.setStatus("current")

# Managed Objects groups


# Notification objects

pingCompletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 0, 1)
)
if mibBuilder.loadTexts:
    pingCompletionTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PING-MIB",
    **{"ping": ping,
       "pingTraps": pingTraps,
       "pingCompletionTrap": pingCompletionTrap,
       "pingTable": pingTable,
       "pingEntry": pingEntry,
       "pingIndex": pingIndex,
       "pingProtocol": pingProtocol,
       "pingAddress": pingAddress,
       "pingNumberOfPackets": pingNumberOfPackets,
       "pingPacketSize": pingPacketSize,
       "pingTimeout": pingTimeout,
       "pingDelay": pingDelay,
       "pingTrapOnCompletion": pingTrapOnCompletion,
       "pingTypeOfService": pingTypeOfService,
       "pingPattern": pingPattern,
       "pingStatus": pingStatus,
       "pingStatistics": pingStatistics,
       "pingSentPackets": pingSentPackets,
       "pingReceivedPackets": pingReceivedPackets,
       "pingMinimumRoundTripTime": pingMinimumRoundTripTime,
       "pingAverageRoundTripTime": pingAverageRoundTripTime,
       "pingMaximumRoundTripTime": pingMaximumRoundTripTime}
)
