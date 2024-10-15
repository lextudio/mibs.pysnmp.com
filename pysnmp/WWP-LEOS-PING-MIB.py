# SNMP MIB module (WWP-LEOS-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:02 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

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

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19)
)
wwpLeosPingMIB.setRevisions(
        ("2012-04-02 00:00",
         "2001-07-03 12:57")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PingFailCause(Integer32, TextualConvention):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("asyncError", 6),
          ("bindError", 3),
          ("commandCompleted", 15),
          ("connectError", 4),
          ("isAlive", 13),
          ("mcastError", 8),
          ("mcastTtlError", 10),
          ("missingHost", 5),
          ("noStatus", 16),
          ("nonBlockError", 7),
          ("outputError", 11),
          ("sendRecvMismatch", 17),
          ("socketError", 2),
          ("ttlError", 9),
          ("txRx", 14),
          ("unknownHost", 1),
          ("unreachableError", 12))
    )



class PingState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("idle", 1),
          ("pingComplete", 3),
          ("pinging", 2))
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosPingMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosPingMIBObjects = _WwpLeosPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1)
)


class _WwpLeosPingDelay_Type(Integer32):
    """Custom type wwpLeosPingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WwpLeosPingDelay_Type.__name__ = "Integer32"
_WwpLeosPingDelay_Object = MibScalar
wwpLeosPingDelay = _WwpLeosPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 1),
    _WwpLeosPingDelay_Type()
)
wwpLeosPingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingDelay.setStatus("current")


class _WwpLeosPingPacketSize_Type(Integer32):
    """Custom type wwpLeosPingPacketSize based on Integer32"""
    defaultValue = 56

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1464),
    )


_WwpLeosPingPacketSize_Type.__name__ = "Integer32"
_WwpLeosPingPacketSize_Object = MibScalar
wwpLeosPingPacketSize = _WwpLeosPingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 2),
    _WwpLeosPingPacketSize_Type()
)
wwpLeosPingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingPacketSize.setStatus("current")
_WwpLeosPingActivate_Type = TruthValue
_WwpLeosPingActivate_Object = MibScalar
wwpLeosPingActivate = _WwpLeosPingActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 3),
    _WwpLeosPingActivate_Type()
)
wwpLeosPingActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingActivate.setStatus("current")
_WwpLeosPingAddrType_Type = AddressFamilyNumbers
_WwpLeosPingAddrType_Object = MibScalar
wwpLeosPingAddrType = _WwpLeosPingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 4),
    _WwpLeosPingAddrType_Type()
)
wwpLeosPingAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingAddrType.setStatus("current")
_WwpLeosPingAddr_Type = DisplayString
_WwpLeosPingAddr_Object = MibScalar
wwpLeosPingAddr = _WwpLeosPingAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 5),
    _WwpLeosPingAddr_Type()
)
wwpLeosPingAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingAddr.setStatus("current")


class _WwpLeosPingPacketCount_Type(Integer32):
    """Custom type wwpLeosPingPacketCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WwpLeosPingPacketCount_Type.__name__ = "Integer32"
_WwpLeosPingPacketCount_Object = MibScalar
wwpLeosPingPacketCount = _WwpLeosPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 6),
    _WwpLeosPingPacketCount_Type()
)
wwpLeosPingPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingPacketCount.setStatus("current")


class _WwpLeosPingPacketTimeout_Type(Integer32):
    """Custom type wwpLeosPingPacketTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WwpLeosPingPacketTimeout_Type.__name__ = "Integer32"
_WwpLeosPingPacketTimeout_Object = MibScalar
wwpLeosPingPacketTimeout = _WwpLeosPingPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 7),
    _WwpLeosPingPacketTimeout_Type()
)
wwpLeosPingPacketTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingPacketTimeout.setStatus("current")
_WwpLeosPingSentPackets_Type = Counter32
_WwpLeosPingSentPackets_Object = MibScalar
wwpLeosPingSentPackets = _WwpLeosPingSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 8),
    _WwpLeosPingSentPackets_Type()
)
wwpLeosPingSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingSentPackets.setStatus("current")
_WwpLeosPingReceivedPackets_Type = Counter32
_WwpLeosPingReceivedPackets_Object = MibScalar
wwpLeosPingReceivedPackets = _WwpLeosPingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 9),
    _WwpLeosPingReceivedPackets_Type()
)
wwpLeosPingReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingReceivedPackets.setStatus("current")
_WwpLeosPingFailCause_Type = PingFailCause
_WwpLeosPingFailCause_Object = MibScalar
wwpLeosPingFailCause = _WwpLeosPingFailCause_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 10),
    _WwpLeosPingFailCause_Type()
)
wwpLeosPingFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingFailCause.setStatus("current")


class _WwpLeosPingState_Type(PingState):
    """Custom type wwpLeosPingState based on PingState"""


_WwpLeosPingState_Object = MibScalar
wwpLeosPingState = _WwpLeosPingState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 11),
    _WwpLeosPingState_Type()
)
wwpLeosPingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingState.setStatus("current")


class _WwpLeosPingUntilStopped_Type(TruthValue):
    """Custom type wwpLeosPingUntilStopped based on TruthValue"""


_WwpLeosPingUntilStopped_Object = MibScalar
wwpLeosPingUntilStopped = _WwpLeosPingUntilStopped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 12),
    _WwpLeosPingUntilStopped_Type()
)
wwpLeosPingUntilStopped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingUntilStopped.setStatus("current")
_WwpLeosPingInetAddrType_Type = InetAddressType
_WwpLeosPingInetAddrType_Object = MibScalar
wwpLeosPingInetAddrType = _WwpLeosPingInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 13),
    _WwpLeosPingInetAddrType_Type()
)
wwpLeosPingInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingInetAddrType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-PING-MIB",
    **{"PingFailCause": PingFailCause,
       "PingState": PingState,
       "wwpLeosPingMIB": wwpLeosPingMIB,
       "wwpLeosPingMIBObjects": wwpLeosPingMIBObjects,
       "wwpLeosPingDelay": wwpLeosPingDelay,
       "wwpLeosPingPacketSize": wwpLeosPingPacketSize,
       "wwpLeosPingActivate": wwpLeosPingActivate,
       "wwpLeosPingAddrType": wwpLeosPingAddrType,
       "wwpLeosPingAddr": wwpLeosPingAddr,
       "wwpLeosPingPacketCount": wwpLeosPingPacketCount,
       "wwpLeosPingPacketTimeout": wwpLeosPingPacketTimeout,
       "wwpLeosPingSentPackets": wwpLeosPingSentPackets,
       "wwpLeosPingReceivedPackets": wwpLeosPingReceivedPackets,
       "wwpLeosPingFailCause": wwpLeosPingFailCause,
       "wwpLeosPingState": wwpLeosPingState,
       "wwpLeosPingUntilStopped": wwpLeosPingUntilStopped,
       "wwpLeosPingInetAddrType": wwpLeosPingInetAddrType}
)
