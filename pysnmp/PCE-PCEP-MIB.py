# SNMP MIB module (PCE-PCEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCE-PCEP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:08 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pcePcepMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 227)
)
pcePcepMIB.setRevisions(
        ("2014-12-17 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PcePcepNotifications_ObjectIdentity = ObjectIdentity
pcePcepNotifications = _PcePcepNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 227, 0)
)
_PcePcepObjects_ObjectIdentity = ObjectIdentity
pcePcepObjects = _PcePcepObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 227, 1)
)
_PcePcepEntityTable_Object = MibTable
pcePcepEntityTable = _PcePcepEntityTable_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1)
)
if mibBuilder.loadTexts:
    pcePcepEntityTable.setStatus("current")
_PcePcepEntityEntry_Object = MibTableRow
pcePcepEntityEntry = _PcePcepEntityEntry_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1)
)
pcePcepEntityEntry.setIndexNames(
    (0, "PCE-PCEP-MIB", "pcePcepEntityIndex"),
)
if mibBuilder.loadTexts:
    pcePcepEntityEntry.setStatus("current")
_PcePcepEntityIndex_Type = Unsigned32
_PcePcepEntityIndex_Object = MibTableColumn
pcePcepEntityIndex = _PcePcepEntityIndex_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 1),
    _PcePcepEntityIndex_Type()
)
pcePcepEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcePcepEntityIndex.setStatus("current")


class _PcePcepEntityAdminStatus_Type(Integer32):
    """Custom type pcePcepEntityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )


_PcePcepEntityAdminStatus_Type.__name__ = "Integer32"
_PcePcepEntityAdminStatus_Object = MibTableColumn
pcePcepEntityAdminStatus = _PcePcepEntityAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 2),
    _PcePcepEntityAdminStatus_Type()
)
pcePcepEntityAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityAdminStatus.setStatus("current")


class _PcePcepEntityOperStatus_Type(Integer32):
    """Custom type pcePcepEntityOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("operStatusDown", 2),
          ("operStatusFailed", 5),
          ("operStatusFailedPerm", 6),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )


_PcePcepEntityOperStatus_Type.__name__ = "Integer32"
_PcePcepEntityOperStatus_Object = MibTableColumn
pcePcepEntityOperStatus = _PcePcepEntityOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 3),
    _PcePcepEntityOperStatus_Type()
)
pcePcepEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityOperStatus.setStatus("current")
_PcePcepEntityAddrType_Type = InetAddressType
_PcePcepEntityAddrType_Object = MibTableColumn
pcePcepEntityAddrType = _PcePcepEntityAddrType_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 4),
    _PcePcepEntityAddrType_Type()
)
pcePcepEntityAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityAddrType.setStatus("current")
_PcePcepEntityAddr_Type = InetAddress
_PcePcepEntityAddr_Object = MibTableColumn
pcePcepEntityAddr = _PcePcepEntityAddr_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 5),
    _PcePcepEntityAddr_Type()
)
pcePcepEntityAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityAddr.setStatus("current")


class _PcePcepEntityConnectTimer_Type(Unsigned32):
    """Custom type pcePcepEntityConnectTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcePcepEntityConnectTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityConnectTimer_Object = MibTableColumn
pcePcepEntityConnectTimer = _PcePcepEntityConnectTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 6),
    _PcePcepEntityConnectTimer_Type()
)
pcePcepEntityConnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityConnectTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityConnectTimer.setUnits("seconds")
_PcePcepEntityConnectMaxRetry_Type = Unsigned32
_PcePcepEntityConnectMaxRetry_Object = MibTableColumn
pcePcepEntityConnectMaxRetry = _PcePcepEntityConnectMaxRetry_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 7),
    _PcePcepEntityConnectMaxRetry_Type()
)
pcePcepEntityConnectMaxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityConnectMaxRetry.setStatus("current")


class _PcePcepEntityInitBackoffTimer_Type(Unsigned32):
    """Custom type pcePcepEntityInitBackoffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcePcepEntityInitBackoffTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityInitBackoffTimer_Object = MibTableColumn
pcePcepEntityInitBackoffTimer = _PcePcepEntityInitBackoffTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 8),
    _PcePcepEntityInitBackoffTimer_Type()
)
pcePcepEntityInitBackoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityInitBackoffTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityInitBackoffTimer.setUnits("seconds")
_PcePcepEntityMaxBackoffTimer_Type = Unsigned32
_PcePcepEntityMaxBackoffTimer_Object = MibTableColumn
pcePcepEntityMaxBackoffTimer = _PcePcepEntityMaxBackoffTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 9),
    _PcePcepEntityMaxBackoffTimer_Type()
)
pcePcepEntityMaxBackoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityMaxBackoffTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityMaxBackoffTimer.setUnits("seconds")


class _PcePcepEntityOpenWaitTimer_Type(Unsigned32):
    """Custom type pcePcepEntityOpenWaitTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcePcepEntityOpenWaitTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityOpenWaitTimer_Object = MibTableColumn
pcePcepEntityOpenWaitTimer = _PcePcepEntityOpenWaitTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 10),
    _PcePcepEntityOpenWaitTimer_Type()
)
pcePcepEntityOpenWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityOpenWaitTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityOpenWaitTimer.setUnits("seconds")


class _PcePcepEntityKeepWaitTimer_Type(Unsigned32):
    """Custom type pcePcepEntityKeepWaitTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcePcepEntityKeepWaitTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityKeepWaitTimer_Object = MibTableColumn
pcePcepEntityKeepWaitTimer = _PcePcepEntityKeepWaitTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 11),
    _PcePcepEntityKeepWaitTimer_Type()
)
pcePcepEntityKeepWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityKeepWaitTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityKeepWaitTimer.setUnits("seconds")


class _PcePcepEntityKeepAliveTimer_Type(Unsigned32):
    """Custom type pcePcepEntityKeepAliveTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepEntityKeepAliveTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityKeepAliveTimer_Object = MibTableColumn
pcePcepEntityKeepAliveTimer = _PcePcepEntityKeepAliveTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 12),
    _PcePcepEntityKeepAliveTimer_Type()
)
pcePcepEntityKeepAliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityKeepAliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityKeepAliveTimer.setUnits("seconds")


class _PcePcepEntityDeadTimer_Type(Unsigned32):
    """Custom type pcePcepEntityDeadTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepEntityDeadTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityDeadTimer_Object = MibTableColumn
pcePcepEntityDeadTimer = _PcePcepEntityDeadTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 13),
    _PcePcepEntityDeadTimer_Type()
)
pcePcepEntityDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityDeadTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityDeadTimer.setUnits("seconds")
_PcePcepEntityAllowNegotiation_Type = TruthValue
_PcePcepEntityAllowNegotiation_Object = MibTableColumn
pcePcepEntityAllowNegotiation = _PcePcepEntityAllowNegotiation_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 14),
    _PcePcepEntityAllowNegotiation_Type()
)
pcePcepEntityAllowNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityAllowNegotiation.setStatus("current")


class _PcePcepEntityMaxKeepAliveTimer_Type(Unsigned32):
    """Custom type pcePcepEntityMaxKeepAliveTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepEntityMaxKeepAliveTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityMaxKeepAliveTimer_Object = MibTableColumn
pcePcepEntityMaxKeepAliveTimer = _PcePcepEntityMaxKeepAliveTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 15),
    _PcePcepEntityMaxKeepAliveTimer_Type()
)
pcePcepEntityMaxKeepAliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityMaxKeepAliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityMaxKeepAliveTimer.setUnits("seconds")


class _PcePcepEntityMaxDeadTimer_Type(Unsigned32):
    """Custom type pcePcepEntityMaxDeadTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepEntityMaxDeadTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityMaxDeadTimer_Object = MibTableColumn
pcePcepEntityMaxDeadTimer = _PcePcepEntityMaxDeadTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 16),
    _PcePcepEntityMaxDeadTimer_Type()
)
pcePcepEntityMaxDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityMaxDeadTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityMaxDeadTimer.setUnits("seconds")


class _PcePcepEntityMinKeepAliveTimer_Type(Unsigned32):
    """Custom type pcePcepEntityMinKeepAliveTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepEntityMinKeepAliveTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityMinKeepAliveTimer_Object = MibTableColumn
pcePcepEntityMinKeepAliveTimer = _PcePcepEntityMinKeepAliveTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 17),
    _PcePcepEntityMinKeepAliveTimer_Type()
)
pcePcepEntityMinKeepAliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityMinKeepAliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityMinKeepAliveTimer.setUnits("seconds")


class _PcePcepEntityMinDeadTimer_Type(Unsigned32):
    """Custom type pcePcepEntityMinDeadTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepEntityMinDeadTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityMinDeadTimer_Object = MibTableColumn
pcePcepEntityMinDeadTimer = _PcePcepEntityMinDeadTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 18),
    _PcePcepEntityMinDeadTimer_Type()
)
pcePcepEntityMinDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityMinDeadTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityMinDeadTimer.setUnits("seconds")


class _PcePcepEntitySyncTimer_Type(Unsigned32):
    """Custom type pcePcepEntitySyncTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PcePcepEntitySyncTimer_Type.__name__ = "Unsigned32"
_PcePcepEntitySyncTimer_Object = MibTableColumn
pcePcepEntitySyncTimer = _PcePcepEntitySyncTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 19),
    _PcePcepEntitySyncTimer_Type()
)
pcePcepEntitySyncTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntitySyncTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntitySyncTimer.setUnits("seconds")


class _PcePcepEntityRequestTimer_Type(Unsigned32):
    """Custom type pcePcepEntityRequestTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PcePcepEntityRequestTimer_Type.__name__ = "Unsigned32"
_PcePcepEntityRequestTimer_Object = MibTableColumn
pcePcepEntityRequestTimer = _PcePcepEntityRequestTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 20),
    _PcePcepEntityRequestTimer_Type()
)
pcePcepEntityRequestTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityRequestTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepEntityRequestTimer.setUnits("seconds")
_PcePcepEntityMaxSessions_Type = Unsigned32
_PcePcepEntityMaxSessions_Object = MibTableColumn
pcePcepEntityMaxSessions = _PcePcepEntityMaxSessions_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 21),
    _PcePcepEntityMaxSessions_Type()
)
pcePcepEntityMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityMaxSessions.setStatus("current")
_PcePcepEntityMaxUnknownReqs_Type = Unsigned32
_PcePcepEntityMaxUnknownReqs_Object = MibTableColumn
pcePcepEntityMaxUnknownReqs = _PcePcepEntityMaxUnknownReqs_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 22),
    _PcePcepEntityMaxUnknownReqs_Type()
)
pcePcepEntityMaxUnknownReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityMaxUnknownReqs.setStatus("current")
_PcePcepEntityMaxUnknownMsgs_Type = Unsigned32
_PcePcepEntityMaxUnknownMsgs_Object = MibTableColumn
pcePcepEntityMaxUnknownMsgs = _PcePcepEntityMaxUnknownMsgs_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 1, 1, 23),
    _PcePcepEntityMaxUnknownMsgs_Type()
)
pcePcepEntityMaxUnknownMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepEntityMaxUnknownMsgs.setStatus("current")
_PcePcepPeerTable_Object = MibTable
pcePcepPeerTable = _PcePcepPeerTable_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2)
)
if mibBuilder.loadTexts:
    pcePcepPeerTable.setStatus("current")
_PcePcepPeerEntry_Object = MibTableRow
pcePcepPeerEntry = _PcePcepPeerEntry_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1)
)
pcePcepPeerEntry.setIndexNames(
    (0, "PCE-PCEP-MIB", "pcePcepEntityIndex"),
    (0, "PCE-PCEP-MIB", "pcePcepPeerAddrType"),
    (0, "PCE-PCEP-MIB", "pcePcepPeerAddr"),
)
if mibBuilder.loadTexts:
    pcePcepPeerEntry.setStatus("current")
_PcePcepPeerAddrType_Type = InetAddressType
_PcePcepPeerAddrType_Object = MibTableColumn
pcePcepPeerAddrType = _PcePcepPeerAddrType_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 1),
    _PcePcepPeerAddrType_Type()
)
pcePcepPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcePcepPeerAddrType.setStatus("current")
_PcePcepPeerAddr_Type = InetAddress
_PcePcepPeerAddr_Object = MibTableColumn
pcePcepPeerAddr = _PcePcepPeerAddr_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 2),
    _PcePcepPeerAddr_Type()
)
pcePcepPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcePcepPeerAddr.setStatus("current")


class _PcePcepPeerRole_Type(Integer32):
    """Custom type pcePcepPeerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pcc", 1),
          ("pccAndPce", 3),
          ("pce", 2),
          ("unknown", 0))
    )


_PcePcepPeerRole_Type.__name__ = "Integer32"
_PcePcepPeerRole_Object = MibTableColumn
pcePcepPeerRole = _PcePcepPeerRole_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 3),
    _PcePcepPeerRole_Type()
)
pcePcepPeerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerRole.setStatus("current")
_PcePcepPeerDiscontinuityTime_Type = TimeStamp
_PcePcepPeerDiscontinuityTime_Object = MibTableColumn
pcePcepPeerDiscontinuityTime = _PcePcepPeerDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 4),
    _PcePcepPeerDiscontinuityTime_Type()
)
pcePcepPeerDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerDiscontinuityTime.setStatus("current")
_PcePcepPeerInitiateSession_Type = TruthValue
_PcePcepPeerInitiateSession_Object = MibTableColumn
pcePcepPeerInitiateSession = _PcePcepPeerInitiateSession_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 5),
    _PcePcepPeerInitiateSession_Type()
)
pcePcepPeerInitiateSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerInitiateSession.setStatus("current")
_PcePcepPeerSessionExists_Type = TruthValue
_PcePcepPeerSessionExists_Object = MibTableColumn
pcePcepPeerSessionExists = _PcePcepPeerSessionExists_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 6),
    _PcePcepPeerSessionExists_Type()
)
pcePcepPeerSessionExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerSessionExists.setStatus("current")
_PcePcepPeerNumSessSetupOK_Type = Counter32
_PcePcepPeerNumSessSetupOK_Object = MibTableColumn
pcePcepPeerNumSessSetupOK = _PcePcepPeerNumSessSetupOK_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 7),
    _PcePcepPeerNumSessSetupOK_Type()
)
pcePcepPeerNumSessSetupOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumSessSetupOK.setStatus("current")
_PcePcepPeerNumSessSetupFail_Type = Counter32
_PcePcepPeerNumSessSetupFail_Object = MibTableColumn
pcePcepPeerNumSessSetupFail = _PcePcepPeerNumSessSetupFail_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 8),
    _PcePcepPeerNumSessSetupFail_Type()
)
pcePcepPeerNumSessSetupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumSessSetupFail.setStatus("current")
_PcePcepPeerSessionUpTime_Type = TimeStamp
_PcePcepPeerSessionUpTime_Object = MibTableColumn
pcePcepPeerSessionUpTime = _PcePcepPeerSessionUpTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 9),
    _PcePcepPeerSessionUpTime_Type()
)
pcePcepPeerSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerSessionUpTime.setStatus("current")
_PcePcepPeerSessionFailTime_Type = TimeStamp
_PcePcepPeerSessionFailTime_Object = MibTableColumn
pcePcepPeerSessionFailTime = _PcePcepPeerSessionFailTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 10),
    _PcePcepPeerSessionFailTime_Type()
)
pcePcepPeerSessionFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerSessionFailTime.setStatus("current")
_PcePcepPeerSessionFailUpTime_Type = TimeStamp
_PcePcepPeerSessionFailUpTime_Object = MibTableColumn
pcePcepPeerSessionFailUpTime = _PcePcepPeerSessionFailUpTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 11),
    _PcePcepPeerSessionFailUpTime_Type()
)
pcePcepPeerSessionFailUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerSessionFailUpTime.setStatus("current")
_PcePcepPeerAvgRspTime_Type = Unsigned32
_PcePcepPeerAvgRspTime_Object = MibTableColumn
pcePcepPeerAvgRspTime = _PcePcepPeerAvgRspTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 12),
    _PcePcepPeerAvgRspTime_Type()
)
pcePcepPeerAvgRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerAvgRspTime.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepPeerAvgRspTime.setUnits("milliseconds")
_PcePcepPeerLWMRspTime_Type = Unsigned32
_PcePcepPeerLWMRspTime_Object = MibTableColumn
pcePcepPeerLWMRspTime = _PcePcepPeerLWMRspTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 13),
    _PcePcepPeerLWMRspTime_Type()
)
pcePcepPeerLWMRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerLWMRspTime.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepPeerLWMRspTime.setUnits("milliseconds")
_PcePcepPeerHWMRspTime_Type = Unsigned32
_PcePcepPeerHWMRspTime_Object = MibTableColumn
pcePcepPeerHWMRspTime = _PcePcepPeerHWMRspTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 14),
    _PcePcepPeerHWMRspTime_Type()
)
pcePcepPeerHWMRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerHWMRspTime.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepPeerHWMRspTime.setUnits("milliseconds")
_PcePcepPeerNumPCReqSent_Type = Counter32
_PcePcepPeerNumPCReqSent_Object = MibTableColumn
pcePcepPeerNumPCReqSent = _PcePcepPeerNumPCReqSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 15),
    _PcePcepPeerNumPCReqSent_Type()
)
pcePcepPeerNumPCReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumPCReqSent.setStatus("current")
_PcePcepPeerNumPCReqRcvd_Type = Counter32
_PcePcepPeerNumPCReqRcvd_Object = MibTableColumn
pcePcepPeerNumPCReqRcvd = _PcePcepPeerNumPCReqRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 16),
    _PcePcepPeerNumPCReqRcvd_Type()
)
pcePcepPeerNumPCReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumPCReqRcvd.setStatus("current")
_PcePcepPeerNumPCRepSent_Type = Counter32
_PcePcepPeerNumPCRepSent_Object = MibTableColumn
pcePcepPeerNumPCRepSent = _PcePcepPeerNumPCRepSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 17),
    _PcePcepPeerNumPCRepSent_Type()
)
pcePcepPeerNumPCRepSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumPCRepSent.setStatus("current")
_PcePcepPeerNumPCRepRcvd_Type = Counter32
_PcePcepPeerNumPCRepRcvd_Object = MibTableColumn
pcePcepPeerNumPCRepRcvd = _PcePcepPeerNumPCRepRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 18),
    _PcePcepPeerNumPCRepRcvd_Type()
)
pcePcepPeerNumPCRepRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumPCRepRcvd.setStatus("current")
_PcePcepPeerNumPCErrSent_Type = Counter32
_PcePcepPeerNumPCErrSent_Object = MibTableColumn
pcePcepPeerNumPCErrSent = _PcePcepPeerNumPCErrSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 19),
    _PcePcepPeerNumPCErrSent_Type()
)
pcePcepPeerNumPCErrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumPCErrSent.setStatus("current")
_PcePcepPeerNumPCErrRcvd_Type = Counter32
_PcePcepPeerNumPCErrRcvd_Object = MibTableColumn
pcePcepPeerNumPCErrRcvd = _PcePcepPeerNumPCErrRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 20),
    _PcePcepPeerNumPCErrRcvd_Type()
)
pcePcepPeerNumPCErrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumPCErrRcvd.setStatus("current")
_PcePcepPeerNumPCNtfSent_Type = Counter32
_PcePcepPeerNumPCNtfSent_Object = MibTableColumn
pcePcepPeerNumPCNtfSent = _PcePcepPeerNumPCNtfSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 21),
    _PcePcepPeerNumPCNtfSent_Type()
)
pcePcepPeerNumPCNtfSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumPCNtfSent.setStatus("current")
_PcePcepPeerNumPCNtfRcvd_Type = Counter32
_PcePcepPeerNumPCNtfRcvd_Object = MibTableColumn
pcePcepPeerNumPCNtfRcvd = _PcePcepPeerNumPCNtfRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 22),
    _PcePcepPeerNumPCNtfRcvd_Type()
)
pcePcepPeerNumPCNtfRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumPCNtfRcvd.setStatus("current")
_PcePcepPeerNumKeepaliveSent_Type = Counter32
_PcePcepPeerNumKeepaliveSent_Object = MibTableColumn
pcePcepPeerNumKeepaliveSent = _PcePcepPeerNumKeepaliveSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 23),
    _PcePcepPeerNumKeepaliveSent_Type()
)
pcePcepPeerNumKeepaliveSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumKeepaliveSent.setStatus("current")
_PcePcepPeerNumKeepaliveRcvd_Type = Counter32
_PcePcepPeerNumKeepaliveRcvd_Object = MibTableColumn
pcePcepPeerNumKeepaliveRcvd = _PcePcepPeerNumKeepaliveRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 24),
    _PcePcepPeerNumKeepaliveRcvd_Type()
)
pcePcepPeerNumKeepaliveRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumKeepaliveRcvd.setStatus("current")
_PcePcepPeerNumUnknownRcvd_Type = Counter32
_PcePcepPeerNumUnknownRcvd_Object = MibTableColumn
pcePcepPeerNumUnknownRcvd = _PcePcepPeerNumUnknownRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 25),
    _PcePcepPeerNumUnknownRcvd_Type()
)
pcePcepPeerNumUnknownRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumUnknownRcvd.setStatus("current")
_PcePcepPeerNumCorruptRcvd_Type = Counter32
_PcePcepPeerNumCorruptRcvd_Object = MibTableColumn
pcePcepPeerNumCorruptRcvd = _PcePcepPeerNumCorruptRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 26),
    _PcePcepPeerNumCorruptRcvd_Type()
)
pcePcepPeerNumCorruptRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumCorruptRcvd.setStatus("current")
_PcePcepPeerNumReqSent_Type = Counter32
_PcePcepPeerNumReqSent_Object = MibTableColumn
pcePcepPeerNumReqSent = _PcePcepPeerNumReqSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 27),
    _PcePcepPeerNumReqSent_Type()
)
pcePcepPeerNumReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqSent.setStatus("current")
_PcePcepPeerNumSvecSent_Type = Counter32
_PcePcepPeerNumSvecSent_Object = MibTableColumn
pcePcepPeerNumSvecSent = _PcePcepPeerNumSvecSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 28),
    _PcePcepPeerNumSvecSent_Type()
)
pcePcepPeerNumSvecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumSvecSent.setStatus("current")
_PcePcepPeerNumSvecReqSent_Type = Counter32
_PcePcepPeerNumSvecReqSent_Object = MibTableColumn
pcePcepPeerNumSvecReqSent = _PcePcepPeerNumSvecReqSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 29),
    _PcePcepPeerNumSvecReqSent_Type()
)
pcePcepPeerNumSvecReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumSvecReqSent.setStatus("current")
_PcePcepPeerNumReqSentPendRep_Type = Counter32
_PcePcepPeerNumReqSentPendRep_Object = MibTableColumn
pcePcepPeerNumReqSentPendRep = _PcePcepPeerNumReqSentPendRep_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 30),
    _PcePcepPeerNumReqSentPendRep_Type()
)
pcePcepPeerNumReqSentPendRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqSentPendRep.setStatus("current")
_PcePcepPeerNumReqSentEroRcvd_Type = Counter32
_PcePcepPeerNumReqSentEroRcvd_Object = MibTableColumn
pcePcepPeerNumReqSentEroRcvd = _PcePcepPeerNumReqSentEroRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 31),
    _PcePcepPeerNumReqSentEroRcvd_Type()
)
pcePcepPeerNumReqSentEroRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqSentEroRcvd.setStatus("current")
_PcePcepPeerNumReqSentNoPathRcvd_Type = Counter32
_PcePcepPeerNumReqSentNoPathRcvd_Object = MibTableColumn
pcePcepPeerNumReqSentNoPathRcvd = _PcePcepPeerNumReqSentNoPathRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 32),
    _PcePcepPeerNumReqSentNoPathRcvd_Type()
)
pcePcepPeerNumReqSentNoPathRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqSentNoPathRcvd.setStatus("current")
_PcePcepPeerNumReqSentCancelRcvd_Type = Counter32
_PcePcepPeerNumReqSentCancelRcvd_Object = MibTableColumn
pcePcepPeerNumReqSentCancelRcvd = _PcePcepPeerNumReqSentCancelRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 33),
    _PcePcepPeerNumReqSentCancelRcvd_Type()
)
pcePcepPeerNumReqSentCancelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqSentCancelRcvd.setStatus("current")
_PcePcepPeerNumReqSentErrorRcvd_Type = Counter32
_PcePcepPeerNumReqSentErrorRcvd_Object = MibTableColumn
pcePcepPeerNumReqSentErrorRcvd = _PcePcepPeerNumReqSentErrorRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 34),
    _PcePcepPeerNumReqSentErrorRcvd_Type()
)
pcePcepPeerNumReqSentErrorRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqSentErrorRcvd.setStatus("current")
_PcePcepPeerNumReqSentTimeout_Type = Counter32
_PcePcepPeerNumReqSentTimeout_Object = MibTableColumn
pcePcepPeerNumReqSentTimeout = _PcePcepPeerNumReqSentTimeout_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 35),
    _PcePcepPeerNumReqSentTimeout_Type()
)
pcePcepPeerNumReqSentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqSentTimeout.setStatus("current")
_PcePcepPeerNumReqSentCancelSent_Type = Counter32
_PcePcepPeerNumReqSentCancelSent_Object = MibTableColumn
pcePcepPeerNumReqSentCancelSent = _PcePcepPeerNumReqSentCancelSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 36),
    _PcePcepPeerNumReqSentCancelSent_Type()
)
pcePcepPeerNumReqSentCancelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqSentCancelSent.setStatus("current")
_PcePcepPeerNumReqSentClosed_Type = Counter32
_PcePcepPeerNumReqSentClosed_Object = MibTableColumn
pcePcepPeerNumReqSentClosed = _PcePcepPeerNumReqSentClosed_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 37),
    _PcePcepPeerNumReqSentClosed_Type()
)
pcePcepPeerNumReqSentClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqSentClosed.setStatus("current")
_PcePcepPeerNumReqRcvd_Type = Counter32
_PcePcepPeerNumReqRcvd_Object = MibTableColumn
pcePcepPeerNumReqRcvd = _PcePcepPeerNumReqRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 38),
    _PcePcepPeerNumReqRcvd_Type()
)
pcePcepPeerNumReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqRcvd.setStatus("current")
_PcePcepPeerNumSvecRcvd_Type = Counter32
_PcePcepPeerNumSvecRcvd_Object = MibTableColumn
pcePcepPeerNumSvecRcvd = _PcePcepPeerNumSvecRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 39),
    _PcePcepPeerNumSvecRcvd_Type()
)
pcePcepPeerNumSvecRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumSvecRcvd.setStatus("current")
_PcePcepPeerNumSvecReqRcvd_Type = Counter32
_PcePcepPeerNumSvecReqRcvd_Object = MibTableColumn
pcePcepPeerNumSvecReqRcvd = _PcePcepPeerNumSvecReqRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 40),
    _PcePcepPeerNumSvecReqRcvd_Type()
)
pcePcepPeerNumSvecReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumSvecReqRcvd.setStatus("current")
_PcePcepPeerNumReqRcvdPendRep_Type = Counter32
_PcePcepPeerNumReqRcvdPendRep_Object = MibTableColumn
pcePcepPeerNumReqRcvdPendRep = _PcePcepPeerNumReqRcvdPendRep_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 41),
    _PcePcepPeerNumReqRcvdPendRep_Type()
)
pcePcepPeerNumReqRcvdPendRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqRcvdPendRep.setStatus("current")
_PcePcepPeerNumReqRcvdEroSent_Type = Counter32
_PcePcepPeerNumReqRcvdEroSent_Object = MibTableColumn
pcePcepPeerNumReqRcvdEroSent = _PcePcepPeerNumReqRcvdEroSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 42),
    _PcePcepPeerNumReqRcvdEroSent_Type()
)
pcePcepPeerNumReqRcvdEroSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqRcvdEroSent.setStatus("current")
_PcePcepPeerNumReqRcvdNoPathSent_Type = Counter32
_PcePcepPeerNumReqRcvdNoPathSent_Object = MibTableColumn
pcePcepPeerNumReqRcvdNoPathSent = _PcePcepPeerNumReqRcvdNoPathSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 43),
    _PcePcepPeerNumReqRcvdNoPathSent_Type()
)
pcePcepPeerNumReqRcvdNoPathSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqRcvdNoPathSent.setStatus("current")
_PcePcepPeerNumReqRcvdCancelSent_Type = Counter32
_PcePcepPeerNumReqRcvdCancelSent_Object = MibTableColumn
pcePcepPeerNumReqRcvdCancelSent = _PcePcepPeerNumReqRcvdCancelSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 44),
    _PcePcepPeerNumReqRcvdCancelSent_Type()
)
pcePcepPeerNumReqRcvdCancelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqRcvdCancelSent.setStatus("current")
_PcePcepPeerNumReqRcvdErrorSent_Type = Counter32
_PcePcepPeerNumReqRcvdErrorSent_Object = MibTableColumn
pcePcepPeerNumReqRcvdErrorSent = _PcePcepPeerNumReqRcvdErrorSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 45),
    _PcePcepPeerNumReqRcvdErrorSent_Type()
)
pcePcepPeerNumReqRcvdErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqRcvdErrorSent.setStatus("current")
_PcePcepPeerNumReqRcvdCancelRcvd_Type = Counter32
_PcePcepPeerNumReqRcvdCancelRcvd_Object = MibTableColumn
pcePcepPeerNumReqRcvdCancelRcvd = _PcePcepPeerNumReqRcvdCancelRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 46),
    _PcePcepPeerNumReqRcvdCancelRcvd_Type()
)
pcePcepPeerNumReqRcvdCancelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqRcvdCancelRcvd.setStatus("current")
_PcePcepPeerNumReqRcvdClosed_Type = Counter32
_PcePcepPeerNumReqRcvdClosed_Object = MibTableColumn
pcePcepPeerNumReqRcvdClosed = _PcePcepPeerNumReqRcvdClosed_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 47),
    _PcePcepPeerNumReqRcvdClosed_Type()
)
pcePcepPeerNumReqRcvdClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqRcvdClosed.setStatus("current")
_PcePcepPeerNumRepRcvdUnknown_Type = Counter32
_PcePcepPeerNumRepRcvdUnknown_Object = MibTableColumn
pcePcepPeerNumRepRcvdUnknown = _PcePcepPeerNumRepRcvdUnknown_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 48),
    _PcePcepPeerNumRepRcvdUnknown_Type()
)
pcePcepPeerNumRepRcvdUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumRepRcvdUnknown.setStatus("current")
_PcePcepPeerNumReqRcvdUnknown_Type = Counter32
_PcePcepPeerNumReqRcvdUnknown_Object = MibTableColumn
pcePcepPeerNumReqRcvdUnknown = _PcePcepPeerNumReqRcvdUnknown_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 2, 1, 49),
    _PcePcepPeerNumReqRcvdUnknown_Type()
)
pcePcepPeerNumReqRcvdUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepPeerNumReqRcvdUnknown.setStatus("current")
_PcePcepSessTable_Object = MibTable
pcePcepSessTable = _PcePcepSessTable_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3)
)
if mibBuilder.loadTexts:
    pcePcepSessTable.setStatus("current")
_PcePcepSessEntry_Object = MibTableRow
pcePcepSessEntry = _PcePcepSessEntry_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1)
)
pcePcepSessEntry.setIndexNames(
    (0, "PCE-PCEP-MIB", "pcePcepEntityIndex"),
    (0, "PCE-PCEP-MIB", "pcePcepPeerAddrType"),
    (0, "PCE-PCEP-MIB", "pcePcepPeerAddr"),
    (0, "PCE-PCEP-MIB", "pcePcepSessInitiator"),
)
if mibBuilder.loadTexts:
    pcePcepSessEntry.setStatus("current")


class _PcePcepSessInitiator_Type(Integer32):
    """Custom type pcePcepSessInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_PcePcepSessInitiator_Type.__name__ = "Integer32"
_PcePcepSessInitiator_Object = MibTableColumn
pcePcepSessInitiator = _PcePcepSessInitiator_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 1),
    _PcePcepSessInitiator_Type()
)
pcePcepSessInitiator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcePcepSessInitiator.setStatus("current")
_PcePcepSessStateLastChange_Type = TimeStamp
_PcePcepSessStateLastChange_Object = MibTableColumn
pcePcepSessStateLastChange = _PcePcepSessStateLastChange_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 2),
    _PcePcepSessStateLastChange_Type()
)
pcePcepSessStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessStateLastChange.setStatus("current")


class _PcePcepSessState_Type(Integer32):
    """Custom type pcePcepSessState based on Integer32"""
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
        *(("keepWait", 3),
          ("openWait", 2),
          ("sessionUp", 4),
          ("tcpPending", 1))
    )


_PcePcepSessState_Type.__name__ = "Integer32"
_PcePcepSessState_Object = MibTableColumn
pcePcepSessState = _PcePcepSessState_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 3),
    _PcePcepSessState_Type()
)
pcePcepSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessState.setStatus("current")
_PcePcepSessConnectRetry_Type = Counter32
_PcePcepSessConnectRetry_Object = MibTableColumn
pcePcepSessConnectRetry = _PcePcepSessConnectRetry_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 4),
    _PcePcepSessConnectRetry_Type()
)
pcePcepSessConnectRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessConnectRetry.setStatus("current")


class _PcePcepSessLocalID_Type(Unsigned32):
    """Custom type pcePcepSessLocalID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepSessLocalID_Type.__name__ = "Unsigned32"
_PcePcepSessLocalID_Object = MibTableColumn
pcePcepSessLocalID = _PcePcepSessLocalID_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 5),
    _PcePcepSessLocalID_Type()
)
pcePcepSessLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessLocalID.setStatus("current")


class _PcePcepSessRemoteID_Type(Unsigned32):
    """Custom type pcePcepSessRemoteID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepSessRemoteID_Type.__name__ = "Unsigned32"
_PcePcepSessRemoteID_Object = MibTableColumn
pcePcepSessRemoteID = _PcePcepSessRemoteID_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 6),
    _PcePcepSessRemoteID_Type()
)
pcePcepSessRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessRemoteID.setStatus("current")


class _PcePcepSessKeepaliveTimer_Type(Unsigned32):
    """Custom type pcePcepSessKeepaliveTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepSessKeepaliveTimer_Type.__name__ = "Unsigned32"
_PcePcepSessKeepaliveTimer_Object = MibTableColumn
pcePcepSessKeepaliveTimer = _PcePcepSessKeepaliveTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 7),
    _PcePcepSessKeepaliveTimer_Type()
)
pcePcepSessKeepaliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessKeepaliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessKeepaliveTimer.setUnits("seconds")


class _PcePcepSessPeerKeepaliveTimer_Type(Unsigned32):
    """Custom type pcePcepSessPeerKeepaliveTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepSessPeerKeepaliveTimer_Type.__name__ = "Unsigned32"
_PcePcepSessPeerKeepaliveTimer_Object = MibTableColumn
pcePcepSessPeerKeepaliveTimer = _PcePcepSessPeerKeepaliveTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 8),
    _PcePcepSessPeerKeepaliveTimer_Type()
)
pcePcepSessPeerKeepaliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessPeerKeepaliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessPeerKeepaliveTimer.setUnits("seconds")


class _PcePcepSessDeadTimer_Type(Unsigned32):
    """Custom type pcePcepSessDeadTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepSessDeadTimer_Type.__name__ = "Unsigned32"
_PcePcepSessDeadTimer_Object = MibTableColumn
pcePcepSessDeadTimer = _PcePcepSessDeadTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 9),
    _PcePcepSessDeadTimer_Type()
)
pcePcepSessDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessDeadTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessDeadTimer.setUnits("seconds")


class _PcePcepSessPeerDeadTimer_Type(Unsigned32):
    """Custom type pcePcepSessPeerDeadTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepSessPeerDeadTimer_Type.__name__ = "Unsigned32"
_PcePcepSessPeerDeadTimer_Object = MibTableColumn
pcePcepSessPeerDeadTimer = _PcePcepSessPeerDeadTimer_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 10),
    _PcePcepSessPeerDeadTimer_Type()
)
pcePcepSessPeerDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessPeerDeadTimer.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessPeerDeadTimer.setUnits("seconds")


class _PcePcepSessKAHoldTimeRem_Type(Unsigned32):
    """Custom type pcePcepSessKAHoldTimeRem based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PcePcepSessKAHoldTimeRem_Type.__name__ = "Unsigned32"
_PcePcepSessKAHoldTimeRem_Object = MibTableColumn
pcePcepSessKAHoldTimeRem = _PcePcepSessKAHoldTimeRem_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 11),
    _PcePcepSessKAHoldTimeRem_Type()
)
pcePcepSessKAHoldTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessKAHoldTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessKAHoldTimeRem.setUnits("seconds")
_PcePcepSessOverloaded_Type = TruthValue
_PcePcepSessOverloaded_Object = MibTableColumn
pcePcepSessOverloaded = _PcePcepSessOverloaded_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 12),
    _PcePcepSessOverloaded_Type()
)
pcePcepSessOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessOverloaded.setStatus("current")
_PcePcepSessOverloadTime_Type = Unsigned32
_PcePcepSessOverloadTime_Object = MibTableColumn
pcePcepSessOverloadTime = _PcePcepSessOverloadTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 13),
    _PcePcepSessOverloadTime_Type()
)
pcePcepSessOverloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessOverloadTime.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessOverloadTime.setUnits("seconds")
_PcePcepSessPeerOverloaded_Type = TruthValue
_PcePcepSessPeerOverloaded_Object = MibTableColumn
pcePcepSessPeerOverloaded = _PcePcepSessPeerOverloaded_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 14),
    _PcePcepSessPeerOverloaded_Type()
)
pcePcepSessPeerOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessPeerOverloaded.setStatus("current")
_PcePcepSessPeerOverloadTime_Type = Unsigned32
_PcePcepSessPeerOverloadTime_Object = MibTableColumn
pcePcepSessPeerOverloadTime = _PcePcepSessPeerOverloadTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 15),
    _PcePcepSessPeerOverloadTime_Type()
)
pcePcepSessPeerOverloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessPeerOverloadTime.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessPeerOverloadTime.setUnits("seconds")
_PcePcepSessDiscontinuityTime_Type = TimeStamp
_PcePcepSessDiscontinuityTime_Object = MibTableColumn
pcePcepSessDiscontinuityTime = _PcePcepSessDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 16),
    _PcePcepSessDiscontinuityTime_Type()
)
pcePcepSessDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessDiscontinuityTime.setStatus("current")
_PcePcepSessAvgRspTime_Type = Unsigned32
_PcePcepSessAvgRspTime_Object = MibTableColumn
pcePcepSessAvgRspTime = _PcePcepSessAvgRspTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 17),
    _PcePcepSessAvgRspTime_Type()
)
pcePcepSessAvgRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessAvgRspTime.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessAvgRspTime.setUnits("milliseconds")
_PcePcepSessLWMRspTime_Type = Unsigned32
_PcePcepSessLWMRspTime_Object = MibTableColumn
pcePcepSessLWMRspTime = _PcePcepSessLWMRspTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 18),
    _PcePcepSessLWMRspTime_Type()
)
pcePcepSessLWMRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessLWMRspTime.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessLWMRspTime.setUnits("milliseconds")
_PcePcepSessHWMRspTime_Type = Unsigned32
_PcePcepSessHWMRspTime_Object = MibTableColumn
pcePcepSessHWMRspTime = _PcePcepSessHWMRspTime_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 19),
    _PcePcepSessHWMRspTime_Type()
)
pcePcepSessHWMRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessHWMRspTime.setStatus("current")
if mibBuilder.loadTexts:
    pcePcepSessHWMRspTime.setUnits("milliseconds")
_PcePcepSessNumPCReqSent_Type = Counter32
_PcePcepSessNumPCReqSent_Object = MibTableColumn
pcePcepSessNumPCReqSent = _PcePcepSessNumPCReqSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 20),
    _PcePcepSessNumPCReqSent_Type()
)
pcePcepSessNumPCReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumPCReqSent.setStatus("current")
_PcePcepSessNumPCReqRcvd_Type = Counter32
_PcePcepSessNumPCReqRcvd_Object = MibTableColumn
pcePcepSessNumPCReqRcvd = _PcePcepSessNumPCReqRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 21),
    _PcePcepSessNumPCReqRcvd_Type()
)
pcePcepSessNumPCReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumPCReqRcvd.setStatus("current")
_PcePcepSessNumPCRepSent_Type = Counter32
_PcePcepSessNumPCRepSent_Object = MibTableColumn
pcePcepSessNumPCRepSent = _PcePcepSessNumPCRepSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 22),
    _PcePcepSessNumPCRepSent_Type()
)
pcePcepSessNumPCRepSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumPCRepSent.setStatus("current")
_PcePcepSessNumPCRepRcvd_Type = Counter32
_PcePcepSessNumPCRepRcvd_Object = MibTableColumn
pcePcepSessNumPCRepRcvd = _PcePcepSessNumPCRepRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 23),
    _PcePcepSessNumPCRepRcvd_Type()
)
pcePcepSessNumPCRepRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumPCRepRcvd.setStatus("current")
_PcePcepSessNumPCErrSent_Type = Counter32
_PcePcepSessNumPCErrSent_Object = MibTableColumn
pcePcepSessNumPCErrSent = _PcePcepSessNumPCErrSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 24),
    _PcePcepSessNumPCErrSent_Type()
)
pcePcepSessNumPCErrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumPCErrSent.setStatus("current")
_PcePcepSessNumPCErrRcvd_Type = Counter32
_PcePcepSessNumPCErrRcvd_Object = MibTableColumn
pcePcepSessNumPCErrRcvd = _PcePcepSessNumPCErrRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 25),
    _PcePcepSessNumPCErrRcvd_Type()
)
pcePcepSessNumPCErrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumPCErrRcvd.setStatus("current")
_PcePcepSessNumPCNtfSent_Type = Counter32
_PcePcepSessNumPCNtfSent_Object = MibTableColumn
pcePcepSessNumPCNtfSent = _PcePcepSessNumPCNtfSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 26),
    _PcePcepSessNumPCNtfSent_Type()
)
pcePcepSessNumPCNtfSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumPCNtfSent.setStatus("current")
_PcePcepSessNumPCNtfRcvd_Type = Counter32
_PcePcepSessNumPCNtfRcvd_Object = MibTableColumn
pcePcepSessNumPCNtfRcvd = _PcePcepSessNumPCNtfRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 27),
    _PcePcepSessNumPCNtfRcvd_Type()
)
pcePcepSessNumPCNtfRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumPCNtfRcvd.setStatus("current")
_PcePcepSessNumKeepaliveSent_Type = Counter32
_PcePcepSessNumKeepaliveSent_Object = MibTableColumn
pcePcepSessNumKeepaliveSent = _PcePcepSessNumKeepaliveSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 28),
    _PcePcepSessNumKeepaliveSent_Type()
)
pcePcepSessNumKeepaliveSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumKeepaliveSent.setStatus("current")
_PcePcepSessNumKeepaliveRcvd_Type = Counter32
_PcePcepSessNumKeepaliveRcvd_Object = MibTableColumn
pcePcepSessNumKeepaliveRcvd = _PcePcepSessNumKeepaliveRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 29),
    _PcePcepSessNumKeepaliveRcvd_Type()
)
pcePcepSessNumKeepaliveRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumKeepaliveRcvd.setStatus("current")
_PcePcepSessNumUnknownRcvd_Type = Counter32
_PcePcepSessNumUnknownRcvd_Object = MibTableColumn
pcePcepSessNumUnknownRcvd = _PcePcepSessNumUnknownRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 30),
    _PcePcepSessNumUnknownRcvd_Type()
)
pcePcepSessNumUnknownRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumUnknownRcvd.setStatus("current")
_PcePcepSessNumCorruptRcvd_Type = Counter32
_PcePcepSessNumCorruptRcvd_Object = MibTableColumn
pcePcepSessNumCorruptRcvd = _PcePcepSessNumCorruptRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 31),
    _PcePcepSessNumCorruptRcvd_Type()
)
pcePcepSessNumCorruptRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumCorruptRcvd.setStatus("current")
_PcePcepSessNumReqSent_Type = Counter32
_PcePcepSessNumReqSent_Object = MibTableColumn
pcePcepSessNumReqSent = _PcePcepSessNumReqSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 32),
    _PcePcepSessNumReqSent_Type()
)
pcePcepSessNumReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqSent.setStatus("current")
_PcePcepSessNumSvecSent_Type = Counter32
_PcePcepSessNumSvecSent_Object = MibTableColumn
pcePcepSessNumSvecSent = _PcePcepSessNumSvecSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 33),
    _PcePcepSessNumSvecSent_Type()
)
pcePcepSessNumSvecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumSvecSent.setStatus("current")
_PcePcepSessNumSvecReqSent_Type = Counter32
_PcePcepSessNumSvecReqSent_Object = MibTableColumn
pcePcepSessNumSvecReqSent = _PcePcepSessNumSvecReqSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 34),
    _PcePcepSessNumSvecReqSent_Type()
)
pcePcepSessNumSvecReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumSvecReqSent.setStatus("current")
_PcePcepSessNumReqSentPendRep_Type = Counter32
_PcePcepSessNumReqSentPendRep_Object = MibTableColumn
pcePcepSessNumReqSentPendRep = _PcePcepSessNumReqSentPendRep_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 35),
    _PcePcepSessNumReqSentPendRep_Type()
)
pcePcepSessNumReqSentPendRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqSentPendRep.setStatus("current")
_PcePcepSessNumReqSentEroRcvd_Type = Counter32
_PcePcepSessNumReqSentEroRcvd_Object = MibTableColumn
pcePcepSessNumReqSentEroRcvd = _PcePcepSessNumReqSentEroRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 36),
    _PcePcepSessNumReqSentEroRcvd_Type()
)
pcePcepSessNumReqSentEroRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqSentEroRcvd.setStatus("current")
_PcePcepSessNumReqSentNoPathRcvd_Type = Counter32
_PcePcepSessNumReqSentNoPathRcvd_Object = MibTableColumn
pcePcepSessNumReqSentNoPathRcvd = _PcePcepSessNumReqSentNoPathRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 37),
    _PcePcepSessNumReqSentNoPathRcvd_Type()
)
pcePcepSessNumReqSentNoPathRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqSentNoPathRcvd.setStatus("current")
_PcePcepSessNumReqSentCancelRcvd_Type = Counter32
_PcePcepSessNumReqSentCancelRcvd_Object = MibTableColumn
pcePcepSessNumReqSentCancelRcvd = _PcePcepSessNumReqSentCancelRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 38),
    _PcePcepSessNumReqSentCancelRcvd_Type()
)
pcePcepSessNumReqSentCancelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqSentCancelRcvd.setStatus("current")
_PcePcepSessNumReqSentErrorRcvd_Type = Counter32
_PcePcepSessNumReqSentErrorRcvd_Object = MibTableColumn
pcePcepSessNumReqSentErrorRcvd = _PcePcepSessNumReqSentErrorRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 39),
    _PcePcepSessNumReqSentErrorRcvd_Type()
)
pcePcepSessNumReqSentErrorRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqSentErrorRcvd.setStatus("current")
_PcePcepSessNumReqSentTimeout_Type = Counter32
_PcePcepSessNumReqSentTimeout_Object = MibTableColumn
pcePcepSessNumReqSentTimeout = _PcePcepSessNumReqSentTimeout_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 40),
    _PcePcepSessNumReqSentTimeout_Type()
)
pcePcepSessNumReqSentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqSentTimeout.setStatus("current")
_PcePcepSessNumReqSentCancelSent_Type = Counter32
_PcePcepSessNumReqSentCancelSent_Object = MibTableColumn
pcePcepSessNumReqSentCancelSent = _PcePcepSessNumReqSentCancelSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 41),
    _PcePcepSessNumReqSentCancelSent_Type()
)
pcePcepSessNumReqSentCancelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqSentCancelSent.setStatus("current")
_PcePcepSessNumReqRcvd_Type = Counter32
_PcePcepSessNumReqRcvd_Object = MibTableColumn
pcePcepSessNumReqRcvd = _PcePcepSessNumReqRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 42),
    _PcePcepSessNumReqRcvd_Type()
)
pcePcepSessNumReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqRcvd.setStatus("current")
_PcePcepSessNumSvecRcvd_Type = Counter32
_PcePcepSessNumSvecRcvd_Object = MibTableColumn
pcePcepSessNumSvecRcvd = _PcePcepSessNumSvecRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 43),
    _PcePcepSessNumSvecRcvd_Type()
)
pcePcepSessNumSvecRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumSvecRcvd.setStatus("current")
_PcePcepSessNumSvecReqRcvd_Type = Counter32
_PcePcepSessNumSvecReqRcvd_Object = MibTableColumn
pcePcepSessNumSvecReqRcvd = _PcePcepSessNumSvecReqRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 44),
    _PcePcepSessNumSvecReqRcvd_Type()
)
pcePcepSessNumSvecReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumSvecReqRcvd.setStatus("current")
_PcePcepSessNumReqRcvdPendRep_Type = Counter32
_PcePcepSessNumReqRcvdPendRep_Object = MibTableColumn
pcePcepSessNumReqRcvdPendRep = _PcePcepSessNumReqRcvdPendRep_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 45),
    _PcePcepSessNumReqRcvdPendRep_Type()
)
pcePcepSessNumReqRcvdPendRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqRcvdPendRep.setStatus("current")
_PcePcepSessNumReqRcvdEroSent_Type = Counter32
_PcePcepSessNumReqRcvdEroSent_Object = MibTableColumn
pcePcepSessNumReqRcvdEroSent = _PcePcepSessNumReqRcvdEroSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 46),
    _PcePcepSessNumReqRcvdEroSent_Type()
)
pcePcepSessNumReqRcvdEroSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqRcvdEroSent.setStatus("current")
_PcePcepSessNumReqRcvdNoPathSent_Type = Counter32
_PcePcepSessNumReqRcvdNoPathSent_Object = MibTableColumn
pcePcepSessNumReqRcvdNoPathSent = _PcePcepSessNumReqRcvdNoPathSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 47),
    _PcePcepSessNumReqRcvdNoPathSent_Type()
)
pcePcepSessNumReqRcvdNoPathSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqRcvdNoPathSent.setStatus("current")
_PcePcepSessNumReqRcvdCancelSent_Type = Counter32
_PcePcepSessNumReqRcvdCancelSent_Object = MibTableColumn
pcePcepSessNumReqRcvdCancelSent = _PcePcepSessNumReqRcvdCancelSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 48),
    _PcePcepSessNumReqRcvdCancelSent_Type()
)
pcePcepSessNumReqRcvdCancelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqRcvdCancelSent.setStatus("current")
_PcePcepSessNumReqRcvdErrorSent_Type = Counter32
_PcePcepSessNumReqRcvdErrorSent_Object = MibTableColumn
pcePcepSessNumReqRcvdErrorSent = _PcePcepSessNumReqRcvdErrorSent_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 49),
    _PcePcepSessNumReqRcvdErrorSent_Type()
)
pcePcepSessNumReqRcvdErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqRcvdErrorSent.setStatus("current")
_PcePcepSessNumReqRcvdCancelRcvd_Type = Counter32
_PcePcepSessNumReqRcvdCancelRcvd_Object = MibTableColumn
pcePcepSessNumReqRcvdCancelRcvd = _PcePcepSessNumReqRcvdCancelRcvd_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 50),
    _PcePcepSessNumReqRcvdCancelRcvd_Type()
)
pcePcepSessNumReqRcvdCancelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqRcvdCancelRcvd.setStatus("current")
_PcePcepSessNumRepRcvdUnknown_Type = Counter32
_PcePcepSessNumRepRcvdUnknown_Object = MibTableColumn
pcePcepSessNumRepRcvdUnknown = _PcePcepSessNumRepRcvdUnknown_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 51),
    _PcePcepSessNumRepRcvdUnknown_Type()
)
pcePcepSessNumRepRcvdUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumRepRcvdUnknown.setStatus("current")
_PcePcepSessNumReqRcvdUnknown_Type = Counter32
_PcePcepSessNumReqRcvdUnknown_Object = MibTableColumn
pcePcepSessNumReqRcvdUnknown = _PcePcepSessNumReqRcvdUnknown_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 3, 1, 52),
    _PcePcepSessNumReqRcvdUnknown_Type()
)
pcePcepSessNumReqRcvdUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcePcepSessNumReqRcvdUnknown.setStatus("current")
_PcePcepNotificationsMaxRate_Type = Unsigned32
_PcePcepNotificationsMaxRate_Object = MibScalar
pcePcepNotificationsMaxRate = _PcePcepNotificationsMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 227, 1, 4),
    _PcePcepNotificationsMaxRate_Type()
)
pcePcepNotificationsMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcePcepNotificationsMaxRate.setStatus("current")
_PcePcepConformance_ObjectIdentity = ObjectIdentity
pcePcepConformance = _PcePcepConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 227, 2)
)
_PcePcepCompliances_ObjectIdentity = ObjectIdentity
pcePcepCompliances = _PcePcepCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 227, 2, 1)
)
_PcePcepGroups_ObjectIdentity = ObjectIdentity
pcePcepGroups = _PcePcepGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 227, 2, 2)
)

# Managed Objects groups

pcePcepGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 227, 2, 2, 1)
)
pcePcepGeneralGroup.setObjects(
      *(("PCE-PCEP-MIB", "pcePcepEntityAdminStatus"),
        ("PCE-PCEP-MIB", "pcePcepEntityOperStatus"),
        ("PCE-PCEP-MIB", "pcePcepEntityAddrType"),
        ("PCE-PCEP-MIB", "pcePcepEntityAddr"),
        ("PCE-PCEP-MIB", "pcePcepEntityConnectTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityConnectMaxRetry"),
        ("PCE-PCEP-MIB", "pcePcepEntityInitBackoffTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityMaxBackoffTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityOpenWaitTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityKeepWaitTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityKeepAliveTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityDeadTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityAllowNegotiation"),
        ("PCE-PCEP-MIB", "pcePcepEntityMaxKeepAliveTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityMaxDeadTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityMinKeepAliveTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityMinDeadTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntitySyncTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityRequestTimer"),
        ("PCE-PCEP-MIB", "pcePcepEntityMaxSessions"),
        ("PCE-PCEP-MIB", "pcePcepEntityMaxUnknownReqs"),
        ("PCE-PCEP-MIB", "pcePcepEntityMaxUnknownMsgs"),
        ("PCE-PCEP-MIB", "pcePcepPeerRole"),
        ("PCE-PCEP-MIB", "pcePcepPeerDiscontinuityTime"),
        ("PCE-PCEP-MIB", "pcePcepPeerInitiateSession"),
        ("PCE-PCEP-MIB", "pcePcepPeerSessionExists"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumSessSetupOK"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumSessSetupFail"),
        ("PCE-PCEP-MIB", "pcePcepPeerSessionUpTime"),
        ("PCE-PCEP-MIB", "pcePcepPeerSessionFailTime"),
        ("PCE-PCEP-MIB", "pcePcepPeerSessionFailUpTime"),
        ("PCE-PCEP-MIB", "pcePcepPeerAvgRspTime"),
        ("PCE-PCEP-MIB", "pcePcepPeerLWMRspTime"),
        ("PCE-PCEP-MIB", "pcePcepPeerHWMRspTime"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumPCReqSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumPCReqRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumPCRepSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumPCRepRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumPCErrSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumPCErrRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumPCNtfSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumPCNtfRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumKeepaliveSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumKeepaliveRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumUnknownRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumCorruptRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumSvecSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumSvecReqSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqSentPendRep"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqSentEroRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqSentNoPathRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqSentCancelRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqSentErrorRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqSentTimeout"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqSentCancelSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqSentClosed"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumSvecRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumSvecReqRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqRcvdPendRep"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqRcvdEroSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqRcvdNoPathSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqRcvdCancelSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqRcvdErrorSent"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqRcvdCancelRcvd"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqRcvdClosed"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumRepRcvdUnknown"),
        ("PCE-PCEP-MIB", "pcePcepPeerNumReqRcvdUnknown"),
        ("PCE-PCEP-MIB", "pcePcepSessStateLastChange"),
        ("PCE-PCEP-MIB", "pcePcepSessState"),
        ("PCE-PCEP-MIB", "pcePcepSessConnectRetry"),
        ("PCE-PCEP-MIB", "pcePcepSessLocalID"),
        ("PCE-PCEP-MIB", "pcePcepSessRemoteID"),
        ("PCE-PCEP-MIB", "pcePcepSessKeepaliveTimer"),
        ("PCE-PCEP-MIB", "pcePcepSessPeerKeepaliveTimer"),
        ("PCE-PCEP-MIB", "pcePcepSessDeadTimer"),
        ("PCE-PCEP-MIB", "pcePcepSessPeerDeadTimer"),
        ("PCE-PCEP-MIB", "pcePcepSessKAHoldTimeRem"),
        ("PCE-PCEP-MIB", "pcePcepSessOverloaded"),
        ("PCE-PCEP-MIB", "pcePcepSessOverloadTime"),
        ("PCE-PCEP-MIB", "pcePcepSessPeerOverloaded"),
        ("PCE-PCEP-MIB", "pcePcepSessPeerOverloadTime"),
        ("PCE-PCEP-MIB", "pcePcepSessDiscontinuityTime"),
        ("PCE-PCEP-MIB", "pcePcepSessAvgRspTime"),
        ("PCE-PCEP-MIB", "pcePcepSessLWMRspTime"),
        ("PCE-PCEP-MIB", "pcePcepSessHWMRspTime"),
        ("PCE-PCEP-MIB", "pcePcepSessNumPCReqSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumPCReqRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumPCRepSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumPCRepRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumPCErrSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumPCErrRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumPCNtfSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumPCNtfRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumKeepaliveSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumKeepaliveRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumUnknownRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumCorruptRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumSvecSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumSvecReqSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqSentPendRep"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqSentEroRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqSentNoPathRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqSentCancelRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqSentErrorRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqSentTimeout"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqSentCancelSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumSvecRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumSvecReqRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqRcvdPendRep"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqRcvdEroSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqRcvdNoPathSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqRcvdCancelSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqRcvdErrorSent"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqRcvdCancelRcvd"),
        ("PCE-PCEP-MIB", "pcePcepSessNumRepRcvdUnknown"),
        ("PCE-PCEP-MIB", "pcePcepSessNumReqRcvdUnknown"),
        ("PCE-PCEP-MIB", "pcePcepNotificationsMaxRate"))
)
if mibBuilder.loadTexts:
    pcePcepGeneralGroup.setStatus("current")


# Notification objects

pcePcepSessUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 227, 0, 1)
)
pcePcepSessUp.setObjects(
      *(("PCE-PCEP-MIB", "pcePcepSessState"),
        ("PCE-PCEP-MIB", "pcePcepSessStateLastChange"))
)
if mibBuilder.loadTexts:
    pcePcepSessUp.setStatus(
        "current"
    )

pcePcepSessDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 227, 0, 2)
)
pcePcepSessDown.setObjects(
      *(("PCE-PCEP-MIB", "pcePcepSessState"),
        ("PCE-PCEP-MIB", "pcePcepSessStateLastChange"))
)
if mibBuilder.loadTexts:
    pcePcepSessDown.setStatus(
        "current"
    )

pcePcepSessLocalOverload = NotificationType(
    (1, 3, 6, 1, 2, 1, 227, 0, 3)
)
pcePcepSessLocalOverload.setObjects(
      *(("PCE-PCEP-MIB", "pcePcepSessOverloaded"),
        ("PCE-PCEP-MIB", "pcePcepSessOverloadTime"))
)
if mibBuilder.loadTexts:
    pcePcepSessLocalOverload.setStatus(
        "current"
    )

pcePcepSessLocalOverloadClear = NotificationType(
    (1, 3, 6, 1, 2, 1, 227, 0, 4)
)
pcePcepSessLocalOverloadClear.setObjects(
    ("PCE-PCEP-MIB", "pcePcepSessOverloaded")
)
if mibBuilder.loadTexts:
    pcePcepSessLocalOverloadClear.setStatus(
        "current"
    )

pcePcepSessPeerOverload = NotificationType(
    (1, 3, 6, 1, 2, 1, 227, 0, 5)
)
pcePcepSessPeerOverload.setObjects(
      *(("PCE-PCEP-MIB", "pcePcepSessPeerOverloaded"),
        ("PCE-PCEP-MIB", "pcePcepSessPeerOverloadTime"))
)
if mibBuilder.loadTexts:
    pcePcepSessPeerOverload.setStatus(
        "current"
    )

pcePcepSessPeerOverloadClear = NotificationType(
    (1, 3, 6, 1, 2, 1, 227, 0, 6)
)
pcePcepSessPeerOverloadClear.setObjects(
    ("PCE-PCEP-MIB", "pcePcepSessPeerOverloaded")
)
if mibBuilder.loadTexts:
    pcePcepSessPeerOverloadClear.setStatus(
        "current"
    )


# Notifications groups

pcePcepNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 227, 2, 2, 2)
)
pcePcepNotificationsGroup.setObjects(
      *(("PCE-PCEP-MIB", "pcePcepSessUp"),
        ("PCE-PCEP-MIB", "pcePcepSessDown"),
        ("PCE-PCEP-MIB", "pcePcepSessLocalOverload"),
        ("PCE-PCEP-MIB", "pcePcepSessLocalOverloadClear"),
        ("PCE-PCEP-MIB", "pcePcepSessPeerOverload"),
        ("PCE-PCEP-MIB", "pcePcepSessPeerOverloadClear"))
)
if mibBuilder.loadTexts:
    pcePcepNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pcePcepModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 227, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pcePcepModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCE-PCEP-MIB",
    **{"pcePcepMIB": pcePcepMIB,
       "pcePcepNotifications": pcePcepNotifications,
       "pcePcepSessUp": pcePcepSessUp,
       "pcePcepSessDown": pcePcepSessDown,
       "pcePcepSessLocalOverload": pcePcepSessLocalOverload,
       "pcePcepSessLocalOverloadClear": pcePcepSessLocalOverloadClear,
       "pcePcepSessPeerOverload": pcePcepSessPeerOverload,
       "pcePcepSessPeerOverloadClear": pcePcepSessPeerOverloadClear,
       "pcePcepObjects": pcePcepObjects,
       "pcePcepEntityTable": pcePcepEntityTable,
       "pcePcepEntityEntry": pcePcepEntityEntry,
       "pcePcepEntityIndex": pcePcepEntityIndex,
       "pcePcepEntityAdminStatus": pcePcepEntityAdminStatus,
       "pcePcepEntityOperStatus": pcePcepEntityOperStatus,
       "pcePcepEntityAddrType": pcePcepEntityAddrType,
       "pcePcepEntityAddr": pcePcepEntityAddr,
       "pcePcepEntityConnectTimer": pcePcepEntityConnectTimer,
       "pcePcepEntityConnectMaxRetry": pcePcepEntityConnectMaxRetry,
       "pcePcepEntityInitBackoffTimer": pcePcepEntityInitBackoffTimer,
       "pcePcepEntityMaxBackoffTimer": pcePcepEntityMaxBackoffTimer,
       "pcePcepEntityOpenWaitTimer": pcePcepEntityOpenWaitTimer,
       "pcePcepEntityKeepWaitTimer": pcePcepEntityKeepWaitTimer,
       "pcePcepEntityKeepAliveTimer": pcePcepEntityKeepAliveTimer,
       "pcePcepEntityDeadTimer": pcePcepEntityDeadTimer,
       "pcePcepEntityAllowNegotiation": pcePcepEntityAllowNegotiation,
       "pcePcepEntityMaxKeepAliveTimer": pcePcepEntityMaxKeepAliveTimer,
       "pcePcepEntityMaxDeadTimer": pcePcepEntityMaxDeadTimer,
       "pcePcepEntityMinKeepAliveTimer": pcePcepEntityMinKeepAliveTimer,
       "pcePcepEntityMinDeadTimer": pcePcepEntityMinDeadTimer,
       "pcePcepEntitySyncTimer": pcePcepEntitySyncTimer,
       "pcePcepEntityRequestTimer": pcePcepEntityRequestTimer,
       "pcePcepEntityMaxSessions": pcePcepEntityMaxSessions,
       "pcePcepEntityMaxUnknownReqs": pcePcepEntityMaxUnknownReqs,
       "pcePcepEntityMaxUnknownMsgs": pcePcepEntityMaxUnknownMsgs,
       "pcePcepPeerTable": pcePcepPeerTable,
       "pcePcepPeerEntry": pcePcepPeerEntry,
       "pcePcepPeerAddrType": pcePcepPeerAddrType,
       "pcePcepPeerAddr": pcePcepPeerAddr,
       "pcePcepPeerRole": pcePcepPeerRole,
       "pcePcepPeerDiscontinuityTime": pcePcepPeerDiscontinuityTime,
       "pcePcepPeerInitiateSession": pcePcepPeerInitiateSession,
       "pcePcepPeerSessionExists": pcePcepPeerSessionExists,
       "pcePcepPeerNumSessSetupOK": pcePcepPeerNumSessSetupOK,
       "pcePcepPeerNumSessSetupFail": pcePcepPeerNumSessSetupFail,
       "pcePcepPeerSessionUpTime": pcePcepPeerSessionUpTime,
       "pcePcepPeerSessionFailTime": pcePcepPeerSessionFailTime,
       "pcePcepPeerSessionFailUpTime": pcePcepPeerSessionFailUpTime,
       "pcePcepPeerAvgRspTime": pcePcepPeerAvgRspTime,
       "pcePcepPeerLWMRspTime": pcePcepPeerLWMRspTime,
       "pcePcepPeerHWMRspTime": pcePcepPeerHWMRspTime,
       "pcePcepPeerNumPCReqSent": pcePcepPeerNumPCReqSent,
       "pcePcepPeerNumPCReqRcvd": pcePcepPeerNumPCReqRcvd,
       "pcePcepPeerNumPCRepSent": pcePcepPeerNumPCRepSent,
       "pcePcepPeerNumPCRepRcvd": pcePcepPeerNumPCRepRcvd,
       "pcePcepPeerNumPCErrSent": pcePcepPeerNumPCErrSent,
       "pcePcepPeerNumPCErrRcvd": pcePcepPeerNumPCErrRcvd,
       "pcePcepPeerNumPCNtfSent": pcePcepPeerNumPCNtfSent,
       "pcePcepPeerNumPCNtfRcvd": pcePcepPeerNumPCNtfRcvd,
       "pcePcepPeerNumKeepaliveSent": pcePcepPeerNumKeepaliveSent,
       "pcePcepPeerNumKeepaliveRcvd": pcePcepPeerNumKeepaliveRcvd,
       "pcePcepPeerNumUnknownRcvd": pcePcepPeerNumUnknownRcvd,
       "pcePcepPeerNumCorruptRcvd": pcePcepPeerNumCorruptRcvd,
       "pcePcepPeerNumReqSent": pcePcepPeerNumReqSent,
       "pcePcepPeerNumSvecSent": pcePcepPeerNumSvecSent,
       "pcePcepPeerNumSvecReqSent": pcePcepPeerNumSvecReqSent,
       "pcePcepPeerNumReqSentPendRep": pcePcepPeerNumReqSentPendRep,
       "pcePcepPeerNumReqSentEroRcvd": pcePcepPeerNumReqSentEroRcvd,
       "pcePcepPeerNumReqSentNoPathRcvd": pcePcepPeerNumReqSentNoPathRcvd,
       "pcePcepPeerNumReqSentCancelRcvd": pcePcepPeerNumReqSentCancelRcvd,
       "pcePcepPeerNumReqSentErrorRcvd": pcePcepPeerNumReqSentErrorRcvd,
       "pcePcepPeerNumReqSentTimeout": pcePcepPeerNumReqSentTimeout,
       "pcePcepPeerNumReqSentCancelSent": pcePcepPeerNumReqSentCancelSent,
       "pcePcepPeerNumReqSentClosed": pcePcepPeerNumReqSentClosed,
       "pcePcepPeerNumReqRcvd": pcePcepPeerNumReqRcvd,
       "pcePcepPeerNumSvecRcvd": pcePcepPeerNumSvecRcvd,
       "pcePcepPeerNumSvecReqRcvd": pcePcepPeerNumSvecReqRcvd,
       "pcePcepPeerNumReqRcvdPendRep": pcePcepPeerNumReqRcvdPendRep,
       "pcePcepPeerNumReqRcvdEroSent": pcePcepPeerNumReqRcvdEroSent,
       "pcePcepPeerNumReqRcvdNoPathSent": pcePcepPeerNumReqRcvdNoPathSent,
       "pcePcepPeerNumReqRcvdCancelSent": pcePcepPeerNumReqRcvdCancelSent,
       "pcePcepPeerNumReqRcvdErrorSent": pcePcepPeerNumReqRcvdErrorSent,
       "pcePcepPeerNumReqRcvdCancelRcvd": pcePcepPeerNumReqRcvdCancelRcvd,
       "pcePcepPeerNumReqRcvdClosed": pcePcepPeerNumReqRcvdClosed,
       "pcePcepPeerNumRepRcvdUnknown": pcePcepPeerNumRepRcvdUnknown,
       "pcePcepPeerNumReqRcvdUnknown": pcePcepPeerNumReqRcvdUnknown,
       "pcePcepSessTable": pcePcepSessTable,
       "pcePcepSessEntry": pcePcepSessEntry,
       "pcePcepSessInitiator": pcePcepSessInitiator,
       "pcePcepSessStateLastChange": pcePcepSessStateLastChange,
       "pcePcepSessState": pcePcepSessState,
       "pcePcepSessConnectRetry": pcePcepSessConnectRetry,
       "pcePcepSessLocalID": pcePcepSessLocalID,
       "pcePcepSessRemoteID": pcePcepSessRemoteID,
       "pcePcepSessKeepaliveTimer": pcePcepSessKeepaliveTimer,
       "pcePcepSessPeerKeepaliveTimer": pcePcepSessPeerKeepaliveTimer,
       "pcePcepSessDeadTimer": pcePcepSessDeadTimer,
       "pcePcepSessPeerDeadTimer": pcePcepSessPeerDeadTimer,
       "pcePcepSessKAHoldTimeRem": pcePcepSessKAHoldTimeRem,
       "pcePcepSessOverloaded": pcePcepSessOverloaded,
       "pcePcepSessOverloadTime": pcePcepSessOverloadTime,
       "pcePcepSessPeerOverloaded": pcePcepSessPeerOverloaded,
       "pcePcepSessPeerOverloadTime": pcePcepSessPeerOverloadTime,
       "pcePcepSessDiscontinuityTime": pcePcepSessDiscontinuityTime,
       "pcePcepSessAvgRspTime": pcePcepSessAvgRspTime,
       "pcePcepSessLWMRspTime": pcePcepSessLWMRspTime,
       "pcePcepSessHWMRspTime": pcePcepSessHWMRspTime,
       "pcePcepSessNumPCReqSent": pcePcepSessNumPCReqSent,
       "pcePcepSessNumPCReqRcvd": pcePcepSessNumPCReqRcvd,
       "pcePcepSessNumPCRepSent": pcePcepSessNumPCRepSent,
       "pcePcepSessNumPCRepRcvd": pcePcepSessNumPCRepRcvd,
       "pcePcepSessNumPCErrSent": pcePcepSessNumPCErrSent,
       "pcePcepSessNumPCErrRcvd": pcePcepSessNumPCErrRcvd,
       "pcePcepSessNumPCNtfSent": pcePcepSessNumPCNtfSent,
       "pcePcepSessNumPCNtfRcvd": pcePcepSessNumPCNtfRcvd,
       "pcePcepSessNumKeepaliveSent": pcePcepSessNumKeepaliveSent,
       "pcePcepSessNumKeepaliveRcvd": pcePcepSessNumKeepaliveRcvd,
       "pcePcepSessNumUnknownRcvd": pcePcepSessNumUnknownRcvd,
       "pcePcepSessNumCorruptRcvd": pcePcepSessNumCorruptRcvd,
       "pcePcepSessNumReqSent": pcePcepSessNumReqSent,
       "pcePcepSessNumSvecSent": pcePcepSessNumSvecSent,
       "pcePcepSessNumSvecReqSent": pcePcepSessNumSvecReqSent,
       "pcePcepSessNumReqSentPendRep": pcePcepSessNumReqSentPendRep,
       "pcePcepSessNumReqSentEroRcvd": pcePcepSessNumReqSentEroRcvd,
       "pcePcepSessNumReqSentNoPathRcvd": pcePcepSessNumReqSentNoPathRcvd,
       "pcePcepSessNumReqSentCancelRcvd": pcePcepSessNumReqSentCancelRcvd,
       "pcePcepSessNumReqSentErrorRcvd": pcePcepSessNumReqSentErrorRcvd,
       "pcePcepSessNumReqSentTimeout": pcePcepSessNumReqSentTimeout,
       "pcePcepSessNumReqSentCancelSent": pcePcepSessNumReqSentCancelSent,
       "pcePcepSessNumReqRcvd": pcePcepSessNumReqRcvd,
       "pcePcepSessNumSvecRcvd": pcePcepSessNumSvecRcvd,
       "pcePcepSessNumSvecReqRcvd": pcePcepSessNumSvecReqRcvd,
       "pcePcepSessNumReqRcvdPendRep": pcePcepSessNumReqRcvdPendRep,
       "pcePcepSessNumReqRcvdEroSent": pcePcepSessNumReqRcvdEroSent,
       "pcePcepSessNumReqRcvdNoPathSent": pcePcepSessNumReqRcvdNoPathSent,
       "pcePcepSessNumReqRcvdCancelSent": pcePcepSessNumReqRcvdCancelSent,
       "pcePcepSessNumReqRcvdErrorSent": pcePcepSessNumReqRcvdErrorSent,
       "pcePcepSessNumReqRcvdCancelRcvd": pcePcepSessNumReqRcvdCancelRcvd,
       "pcePcepSessNumRepRcvdUnknown": pcePcepSessNumRepRcvdUnknown,
       "pcePcepSessNumReqRcvdUnknown": pcePcepSessNumReqRcvdUnknown,
       "pcePcepNotificationsMaxRate": pcePcepNotificationsMaxRate,
       "pcePcepConformance": pcePcepConformance,
       "pcePcepCompliances": pcePcepCompliances,
       "pcePcepModuleReadOnlyCompliance": pcePcepModuleReadOnlyCompliance,
       "pcePcepGroups": pcePcepGroups,
       "pcePcepGeneralGroup": pcePcepGeneralGroup,
       "pcePcepNotificationsGroup": pcePcepNotificationsGroup}
)
