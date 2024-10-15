# SNMP MIB module (RADLAN-SOCKET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-SOCKET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:27 2024
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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


# MODULE-IDENTITY

rlSocket = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 85)
)
rlSocket.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlSocketMibVersion_Type = Integer32
_RlSocketMibVersion_Object = MibScalar
rlSocketMibVersion = _RlSocketMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 1),
    _RlSocketMibVersion_Type()
)
rlSocketMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketMibVersion.setStatus("current")
_RlSocketTable_Object = MibTable
rlSocketTable = _RlSocketTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2)
)
if mibBuilder.loadTexts:
    rlSocketTable.setStatus("current")
_RlSocketEntry_Object = MibTableRow
rlSocketEntry = _RlSocketEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1)
)
rlSocketEntry.setIndexNames(
    (0, "RADLAN-SOCKET-MIB", "rlSocketId"),
)
if mibBuilder.loadTexts:
    rlSocketEntry.setStatus("current")
_RlSocketId_Type = Integer32
_RlSocketId_Object = MibTableColumn
rlSocketId = _RlSocketId_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 1),
    _RlSocketId_Type()
)
rlSocketId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketId.setStatus("current")


class _RlSocketType_Type(Integer32):
    """Custom type rlSocketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dgram", 2),
          ("raw", 3),
          ("stream", 1))
    )


_RlSocketType_Type.__name__ = "Integer32"
_RlSocketType_Object = MibTableColumn
rlSocketType = _RlSocketType_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 2),
    _RlSocketType_Type()
)
rlSocketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketType.setStatus("current")


class _RlSocketState_Type(Integer32):
    """Custom type rlSocketState based on Integer32"""
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
        *(("closed", 5),
          ("connected", 1),
          ("notConnected", 2),
          ("peerClosed", 6),
          ("recvClosed", 3),
          ("sendClosed", 4),
          ("sendRecvClosed", 7))
    )


_RlSocketState_Type.__name__ = "Integer32"
_RlSocketState_Object = MibTableColumn
rlSocketState = _RlSocketState_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 3),
    _RlSocketState_Type()
)
rlSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketState.setStatus("current")


class _RlSocketBlockMode_Type(Integer32):
    """Custom type rlSocketBlockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("nonBlocking", 2))
    )


_RlSocketBlockMode_Type.__name__ = "Integer32"
_RlSocketBlockMode_Object = MibTableColumn
rlSocketBlockMode = _RlSocketBlockMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 4),
    _RlSocketBlockMode_Type()
)
rlSocketBlockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketBlockMode.setStatus("current")
_RlSocketUpTime_Type = TimeTicks
_RlSocketUpTime_Object = MibTableColumn
rlSocketUpTime = _RlSocketUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 5),
    _RlSocketUpTime_Type()
)
rlSocketUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketUpTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-SOCKET-MIB",
    **{"rlSocket": rlSocket,
       "rlSocketMibVersion": rlSocketMibVersion,
       "rlSocketTable": rlSocketTable,
       "rlSocketEntry": rlSocketEntry,
       "rlSocketId": rlSocketId,
       "rlSocketType": rlSocketType,
       "rlSocketState": rlSocketState,
       "rlSocketBlockMode": rlSocketBlockMode,
       "rlSocketUpTime": rlSocketUpTime}
)
