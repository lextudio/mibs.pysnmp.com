# SNMP MIB module (CISCO-ALPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ALPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:34 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(X121Address,) = mibBuilder.importSymbols(
    "RFC1382-MIB",
    "X121Address")

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
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoAlpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95)
)
ciscoAlpsMIB.setRevisions(
        ("2008-02-14 00:00",
         "2000-01-28 00:00",
         "1999-01-07 00:00",
         "1998-12-31 00:00",
         "1998-12-08 00:00",
         "1998-05-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlpsCktName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )



class AlpsAscuA1A2Value(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAlpsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAlpsMIBObjects = _CiscoAlpsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1)
)
_AlpsGroups_ObjectIdentity = ObjectIdentity
alpsGroups = _AlpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 1)
)
_AlpsPeerObjects_ObjectIdentity = ObjectIdentity
alpsPeerObjects = _AlpsPeerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2)
)
_AlpsPeer_ObjectIdentity = ObjectIdentity
alpsPeer = _AlpsPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 1)
)
_AlpsPeerLocalIpAddr_Type = IpAddress
_AlpsPeerLocalIpAddr_Object = MibScalar
alpsPeerLocalIpAddr = _AlpsPeerLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 1, 1),
    _AlpsPeerLocalIpAddr_Type()
)
alpsPeerLocalIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsPeerLocalIpAddr.setStatus("current")


class _AlpsPeerLocalAtpPort_Type(Integer32):
    """Custom type alpsPeerLocalAtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlpsPeerLocalAtpPort_Type.__name__ = "Integer32"
_AlpsPeerLocalAtpPort_Object = MibScalar
alpsPeerLocalAtpPort = _AlpsPeerLocalAtpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 1, 2),
    _AlpsPeerLocalAtpPort_Type()
)
alpsPeerLocalAtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsPeerLocalAtpPort.setStatus("current")
_AlpsPeerKeepaliveTimeout_Type = TimeInterval
_AlpsPeerKeepaliveTimeout_Object = MibScalar
alpsPeerKeepaliveTimeout = _AlpsPeerKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 1, 3),
    _AlpsPeerKeepaliveTimeout_Type()
)
alpsPeerKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsPeerKeepaliveTimeout.setStatus("current")


class _AlpsPeerKeepaliveMaxRetries_Type(Integer32):
    """Custom type alpsPeerKeepaliveMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AlpsPeerKeepaliveMaxRetries_Type.__name__ = "Integer32"
_AlpsPeerKeepaliveMaxRetries_Object = MibScalar
alpsPeerKeepaliveMaxRetries = _AlpsPeerKeepaliveMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 1, 4),
    _AlpsPeerKeepaliveMaxRetries_Type()
)
alpsPeerKeepaliveMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsPeerKeepaliveMaxRetries.setStatus("current")


class _AlpsPeerInCallsAcceptFlag_Type(TruthValue):
    """Custom type alpsPeerInCallsAcceptFlag based on TruthValue"""


_AlpsPeerInCallsAcceptFlag_Object = MibScalar
alpsPeerInCallsAcceptFlag = _AlpsPeerInCallsAcceptFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 1, 5),
    _AlpsPeerInCallsAcceptFlag_Type()
)
alpsPeerInCallsAcceptFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsPeerInCallsAcceptFlag.setStatus("current")
_AlpsRemPeerTable_Object = MibTable
alpsRemPeerTable = _AlpsRemPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alpsRemPeerTable.setStatus("deprecated")
_AlpsRemPeerEntry_Object = MibTableRow
alpsRemPeerEntry = _AlpsRemPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1)
)
alpsRemPeerEntry.setIndexNames(
    (0, "CISCO-ALPS-MIB", "alpsRemPeerIpAddr"),
)
if mibBuilder.loadTexts:
    alpsRemPeerEntry.setStatus("deprecated")
_AlpsRemPeerIpAddr_Type = IpAddress
_AlpsRemPeerIpAddr_Object = MibTableColumn
alpsRemPeerIpAddr = _AlpsRemPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 1),
    _AlpsRemPeerIpAddr_Type()
)
alpsRemPeerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsRemPeerIpAddr.setStatus("deprecated")


class _AlpsRemPeerConnType_Type(Integer32):
    """Custom type alpsRemPeerConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("permanent", 1))
    )


_AlpsRemPeerConnType_Type.__name__ = "Integer32"
_AlpsRemPeerConnType_Object = MibTableColumn
alpsRemPeerConnType = _AlpsRemPeerConnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 2),
    _AlpsRemPeerConnType_Type()
)
alpsRemPeerConnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerConnType.setStatus("deprecated")


class _AlpsRemPeerLocalPort_Type(Integer32):
    """Custom type alpsRemPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlpsRemPeerLocalPort_Type.__name__ = "Integer32"
_AlpsRemPeerLocalPort_Object = MibTableColumn
alpsRemPeerLocalPort = _AlpsRemPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 3),
    _AlpsRemPeerLocalPort_Type()
)
alpsRemPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerLocalPort.setStatus("deprecated")


class _AlpsRemPeerRemotePort_Type(Integer32):
    """Custom type alpsRemPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlpsRemPeerRemotePort_Type.__name__ = "Integer32"
_AlpsRemPeerRemotePort_Object = MibTableColumn
alpsRemPeerRemotePort = _AlpsRemPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 4),
    _AlpsRemPeerRemotePort_Type()
)
alpsRemPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerRemotePort.setStatus("deprecated")


class _AlpsRemPeerState_Type(Integer32):
    """Custom type alpsRemPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("opened", 3),
          ("opening", 2))
    )


_AlpsRemPeerState_Type.__name__ = "Integer32"
_AlpsRemPeerState_Object = MibTableColumn
alpsRemPeerState = _AlpsRemPeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 5),
    _AlpsRemPeerState_Type()
)
alpsRemPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerState.setStatus("deprecated")
_AlpsRemPeerUptime_Type = TimeTicks
_AlpsRemPeerUptime_Object = MibTableColumn
alpsRemPeerUptime = _AlpsRemPeerUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 6),
    _AlpsRemPeerUptime_Type()
)
alpsRemPeerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerUptime.setStatus("deprecated")
_AlpsRemPeerNumActiveCkts_Type = Gauge32
_AlpsRemPeerNumActiveCkts_Object = MibTableColumn
alpsRemPeerNumActiveCkts = _AlpsRemPeerNumActiveCkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 7),
    _AlpsRemPeerNumActiveCkts_Type()
)
alpsRemPeerNumActiveCkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerNumActiveCkts.setStatus("deprecated")
_AlpsRemPeerIdleTimer_Type = TimeInterval
_AlpsRemPeerIdleTimer_Object = MibTableColumn
alpsRemPeerIdleTimer = _AlpsRemPeerIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 8),
    _AlpsRemPeerIdleTimer_Type()
)
alpsRemPeerIdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerIdleTimer.setStatus("deprecated")


class _AlpsRemPeerAlarmsEnabled_Type(TruthValue):
    """Custom type alpsRemPeerAlarmsEnabled based on TruthValue"""


_AlpsRemPeerAlarmsEnabled_Object = MibTableColumn
alpsRemPeerAlarmsEnabled = _AlpsRemPeerAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 9),
    _AlpsRemPeerAlarmsEnabled_Type()
)
alpsRemPeerAlarmsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerAlarmsEnabled.setStatus("deprecated")


class _AlpsRemPeerTCPQlen_Type(Integer32):
    """Custom type alpsRemPeerTCPQlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AlpsRemPeerTCPQlen_Type.__name__ = "Integer32"
_AlpsRemPeerTCPQlen_Object = MibTableColumn
alpsRemPeerTCPQlen = _AlpsRemPeerTCPQlen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 10),
    _AlpsRemPeerTCPQlen_Type()
)
alpsRemPeerTCPQlen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerTCPQlen.setStatus("deprecated")
if mibBuilder.loadTexts:
    alpsRemPeerTCPQlen.setUnits("packets")
_AlpsRemPeerOutPackets_Type = Counter32
_AlpsRemPeerOutPackets_Object = MibTableColumn
alpsRemPeerOutPackets = _AlpsRemPeerOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 11),
    _AlpsRemPeerOutPackets_Type()
)
alpsRemPeerOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerOutPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    alpsRemPeerOutPackets.setUnits("packets")
_AlpsRemPeerOutOctets_Type = Counter32
_AlpsRemPeerOutOctets_Object = MibTableColumn
alpsRemPeerOutOctets = _AlpsRemPeerOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 12),
    _AlpsRemPeerOutOctets_Type()
)
alpsRemPeerOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerOutOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    alpsRemPeerOutOctets.setUnits("octets")
_AlpsRemPeerInPackets_Type = Counter32
_AlpsRemPeerInPackets_Object = MibTableColumn
alpsRemPeerInPackets = _AlpsRemPeerInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 13),
    _AlpsRemPeerInPackets_Type()
)
alpsRemPeerInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerInPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    alpsRemPeerInPackets.setUnits("packets")
_AlpsRemPeerInOctets_Type = Counter32
_AlpsRemPeerInOctets_Object = MibTableColumn
alpsRemPeerInOctets = _AlpsRemPeerInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 14),
    _AlpsRemPeerInOctets_Type()
)
alpsRemPeerInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerInOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    alpsRemPeerInOctets.setUnits("octets")
_AlpsRemPeerDropsGiant_Type = Counter32
_AlpsRemPeerDropsGiant_Object = MibTableColumn
alpsRemPeerDropsGiant = _AlpsRemPeerDropsGiant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 15),
    _AlpsRemPeerDropsGiant_Type()
)
alpsRemPeerDropsGiant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerDropsGiant.setStatus("deprecated")
if mibBuilder.loadTexts:
    alpsRemPeerDropsGiant.setUnits("packets")
_AlpsRemPeerDropsQFull_Type = Counter32
_AlpsRemPeerDropsQFull_Object = MibTableColumn
alpsRemPeerDropsQFull = _AlpsRemPeerDropsQFull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 16),
    _AlpsRemPeerDropsQFull_Type()
)
alpsRemPeerDropsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerDropsQFull.setStatus("deprecated")
if mibBuilder.loadTexts:
    alpsRemPeerDropsQFull.setUnits("packets")
_AlpsRemPeerDropsPeerUnreach_Type = Counter32
_AlpsRemPeerDropsPeerUnreach_Object = MibTableColumn
alpsRemPeerDropsPeerUnreach = _AlpsRemPeerDropsPeerUnreach_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 17),
    _AlpsRemPeerDropsPeerUnreach_Type()
)
alpsRemPeerDropsPeerUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerDropsPeerUnreach.setStatus("deprecated")
if mibBuilder.loadTexts:
    alpsRemPeerDropsPeerUnreach.setUnits("packets")
_AlpsRemPeerRowStatus_Type = RowStatus
_AlpsRemPeerRowStatus_Object = MibTableColumn
alpsRemPeerRowStatus = _AlpsRemPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 2, 1, 18),
    _AlpsRemPeerRowStatus_Type()
)
alpsRemPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerRowStatus.setStatus("deprecated")
_AlpsRemPeerCfgTable_Object = MibTable
alpsRemPeerCfgTable = _AlpsRemPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alpsRemPeerCfgTable.setStatus("current")
_AlpsRemPeerCfgEntry_Object = MibTableRow
alpsRemPeerCfgEntry = _AlpsRemPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1)
)
alpsRemPeerCfgEntry.setIndexNames(
    (0, "CISCO-ALPS-MIB", "alpsRemPeerCfgIpAddr"),
    (0, "CISCO-ALPS-MIB", "alpsRemPeerCfgProtocol"),
)
if mibBuilder.loadTexts:
    alpsRemPeerCfgEntry.setStatus("current")
_AlpsRemPeerCfgIpAddr_Type = IpAddress
_AlpsRemPeerCfgIpAddr_Object = MibTableColumn
alpsRemPeerCfgIpAddr = _AlpsRemPeerCfgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 1),
    _AlpsRemPeerCfgIpAddr_Type()
)
alpsRemPeerCfgIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsRemPeerCfgIpAddr.setStatus("current")


class _AlpsRemPeerCfgProtocol_Type(Integer32):
    """Custom type alpsRemPeerCfgProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atp", 1),
          ("matipTypeA", 2))
    )


_AlpsRemPeerCfgProtocol_Type.__name__ = "Integer32"
_AlpsRemPeerCfgProtocol_Object = MibTableColumn
alpsRemPeerCfgProtocol = _AlpsRemPeerCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 2),
    _AlpsRemPeerCfgProtocol_Type()
)
alpsRemPeerCfgProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsRemPeerCfgProtocol.setStatus("current")


class _AlpsRemPeerCfgActivation_Type(Integer32):
    """Custom type alpsRemPeerCfgActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("permanent", 1))
    )


_AlpsRemPeerCfgActivation_Type.__name__ = "Integer32"
_AlpsRemPeerCfgActivation_Object = MibTableColumn
alpsRemPeerCfgActivation = _AlpsRemPeerCfgActivation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 3),
    _AlpsRemPeerCfgActivation_Type()
)
alpsRemPeerCfgActivation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerCfgActivation.setStatus("current")


class _AlpsRemPeerCfgTCPQLen_Type(Integer32):
    """Custom type alpsRemPeerCfgTCPQLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlpsRemPeerCfgTCPQLen_Type.__name__ = "Integer32"
_AlpsRemPeerCfgTCPQLen_Object = MibTableColumn
alpsRemPeerCfgTCPQLen = _AlpsRemPeerCfgTCPQLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 4),
    _AlpsRemPeerCfgTCPQLen_Type()
)
alpsRemPeerCfgTCPQLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerCfgTCPQLen.setStatus("current")
if mibBuilder.loadTexts:
    alpsRemPeerCfgTCPQLen.setUnits("packets")
_AlpsRemPeerCfgIdleTimer_Type = TimeInterval
_AlpsRemPeerCfgIdleTimer_Object = MibTableColumn
alpsRemPeerCfgIdleTimer = _AlpsRemPeerCfgIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 5),
    _AlpsRemPeerCfgIdleTimer_Type()
)
alpsRemPeerCfgIdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerCfgIdleTimer.setStatus("current")
_AlpsRemPeerCfgNoCircTimer_Type = TimeInterval
_AlpsRemPeerCfgNoCircTimer_Object = MibTableColumn
alpsRemPeerCfgNoCircTimer = _AlpsRemPeerCfgNoCircTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 6),
    _AlpsRemPeerCfgNoCircTimer_Type()
)
alpsRemPeerCfgNoCircTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerCfgNoCircTimer.setStatus("current")


class _AlpsRemPeerCfgAlarmsOn_Type(TruthValue):
    """Custom type alpsRemPeerCfgAlarmsOn based on TruthValue"""


_AlpsRemPeerCfgAlarmsOn_Object = MibTableColumn
alpsRemPeerCfgAlarmsOn = _AlpsRemPeerCfgAlarmsOn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 7),
    _AlpsRemPeerCfgAlarmsOn_Type()
)
alpsRemPeerCfgAlarmsOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerCfgAlarmsOn.setStatus("current")
_AlpsRemPeerCfgStatIntvl_Type = TimeInterval
_AlpsRemPeerCfgStatIntvl_Object = MibTableColumn
alpsRemPeerCfgStatIntvl = _AlpsRemPeerCfgStatIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 8),
    _AlpsRemPeerCfgStatIntvl_Type()
)
alpsRemPeerCfgStatIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerCfgStatIntvl.setStatus("current")


class _AlpsRemPeerCfgStatRetry_Type(Integer32):
    """Custom type alpsRemPeerCfgStatRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlpsRemPeerCfgStatRetry_Type.__name__ = "Integer32"
_AlpsRemPeerCfgStatRetry_Object = MibTableColumn
alpsRemPeerCfgStatRetry = _AlpsRemPeerCfgStatRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 9),
    _AlpsRemPeerCfgStatRetry_Type()
)
alpsRemPeerCfgStatRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerCfgStatRetry.setStatus("current")
_AlpsRemPeerCfgRowStatus_Type = RowStatus
_AlpsRemPeerCfgRowStatus_Object = MibTableColumn
alpsRemPeerCfgRowStatus = _AlpsRemPeerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 3, 1, 10),
    _AlpsRemPeerCfgRowStatus_Type()
)
alpsRemPeerCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsRemPeerCfgRowStatus.setStatus("current")
_AlpsRemPeerConnTable_Object = MibTable
alpsRemPeerConnTable = _AlpsRemPeerConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4)
)
if mibBuilder.loadTexts:
    alpsRemPeerConnTable.setStatus("current")
_AlpsRemPeerConnEntry_Object = MibTableRow
alpsRemPeerConnEntry = _AlpsRemPeerConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1)
)
alpsRemPeerConnEntry.setIndexNames(
    (0, "CISCO-ALPS-MIB", "alpsRemPeerConnIpAddr"),
    (0, "CISCO-ALPS-MIB", "alpsRemPeerConnIdString"),
)
if mibBuilder.loadTexts:
    alpsRemPeerConnEntry.setStatus("current")
_AlpsRemPeerConnIpAddr_Type = IpAddress
_AlpsRemPeerConnIpAddr_Object = MibTableColumn
alpsRemPeerConnIpAddr = _AlpsRemPeerConnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 1),
    _AlpsRemPeerConnIpAddr_Type()
)
alpsRemPeerConnIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsRemPeerConnIpAddr.setStatus("current")


class _AlpsRemPeerConnIdString_Type(DisplayString):
    """Custom type alpsRemPeerConnIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AlpsRemPeerConnIdString_Type.__name__ = "DisplayString"
_AlpsRemPeerConnIdString_Object = MibTableColumn
alpsRemPeerConnIdString = _AlpsRemPeerConnIdString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 2),
    _AlpsRemPeerConnIdString_Type()
)
alpsRemPeerConnIdString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsRemPeerConnIdString.setStatus("current")


class _AlpsRemPeerConnLocalPort_Type(Integer32):
    """Custom type alpsRemPeerConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlpsRemPeerConnLocalPort_Type.__name__ = "Integer32"
_AlpsRemPeerConnLocalPort_Object = MibTableColumn
alpsRemPeerConnLocalPort = _AlpsRemPeerConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 3),
    _AlpsRemPeerConnLocalPort_Type()
)
alpsRemPeerConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnLocalPort.setStatus("current")


class _AlpsRemPeerConnForeignPort_Type(Integer32):
    """Custom type alpsRemPeerConnForeignPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlpsRemPeerConnForeignPort_Type.__name__ = "Integer32"
_AlpsRemPeerConnForeignPort_Object = MibTableColumn
alpsRemPeerConnForeignPort = _AlpsRemPeerConnForeignPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 4),
    _AlpsRemPeerConnForeignPort_Type()
)
alpsRemPeerConnForeignPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnForeignPort.setStatus("current")


class _AlpsRemPeerConnState_Type(Integer32):
    """Custom type alpsRemPeerConnState based on Integer32"""
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
        *(("busy", 4),
          ("closed", 1),
          ("opened", 3),
          ("opening", 2))
    )


_AlpsRemPeerConnState_Type.__name__ = "Integer32"
_AlpsRemPeerConnState_Object = MibTableColumn
alpsRemPeerConnState = _AlpsRemPeerConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 5),
    _AlpsRemPeerConnState_Type()
)
alpsRemPeerConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnState.setStatus("current")


class _AlpsRemPeerConnProtocol_Type(Integer32):
    """Custom type alpsRemPeerConnProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atp", 1),
          ("matipTypeA", 2))
    )


_AlpsRemPeerConnProtocol_Type.__name__ = "Integer32"
_AlpsRemPeerConnProtocol_Object = MibTableColumn
alpsRemPeerConnProtocol = _AlpsRemPeerConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 6),
    _AlpsRemPeerConnProtocol_Type()
)
alpsRemPeerConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnProtocol.setStatus("current")


class _AlpsRemPeerConnCreation_Type(Integer32):
    """Custom type alpsRemPeerConnCreation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("learned", 2))
    )


_AlpsRemPeerConnCreation_Type.__name__ = "Integer32"
_AlpsRemPeerConnCreation_Object = MibTableColumn
alpsRemPeerConnCreation = _AlpsRemPeerConnCreation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 7),
    _AlpsRemPeerConnCreation_Type()
)
alpsRemPeerConnCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnCreation.setStatus("current")


class _AlpsRemPeerConnActivation_Type(Integer32):
    """Custom type alpsRemPeerConnActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("permanent", 1))
    )


_AlpsRemPeerConnActivation_Type.__name__ = "Integer32"
_AlpsRemPeerConnActivation_Object = MibTableColumn
alpsRemPeerConnActivation = _AlpsRemPeerConnActivation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 8),
    _AlpsRemPeerConnActivation_Type()
)
alpsRemPeerConnActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnActivation.setStatus("current")
_AlpsRemPeerConnUptime_Type = TimeTicks
_AlpsRemPeerConnUptime_Object = MibTableColumn
alpsRemPeerConnUptime = _AlpsRemPeerConnUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 9),
    _AlpsRemPeerConnUptime_Type()
)
alpsRemPeerConnUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnUptime.setStatus("current")


class _AlpsRemPeerConnNumActCirc_Type(Integer32):
    """Custom type alpsRemPeerConnNumActCirc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlpsRemPeerConnNumActCirc_Type.__name__ = "Integer32"
_AlpsRemPeerConnNumActCirc_Object = MibTableColumn
alpsRemPeerConnNumActCirc = _AlpsRemPeerConnNumActCirc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 10),
    _AlpsRemPeerConnNumActCirc_Type()
)
alpsRemPeerConnNumActCirc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnNumActCirc.setStatus("current")
_AlpsRemPeerConnLastTxRx_Type = TimeStamp
_AlpsRemPeerConnLastTxRx_Object = MibTableColumn
alpsRemPeerConnLastTxRx = _AlpsRemPeerConnLastTxRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 11),
    _AlpsRemPeerConnLastTxRx_Type()
)
alpsRemPeerConnLastTxRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnLastTxRx.setStatus("current")
_AlpsRemPeerConnLastRxAny_Type = TimeStamp
_AlpsRemPeerConnLastRxAny_Object = MibTableColumn
alpsRemPeerConnLastRxAny = _AlpsRemPeerConnLastRxAny_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 12),
    _AlpsRemPeerConnLastRxAny_Type()
)
alpsRemPeerConnLastRxAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnLastRxAny.setStatus("current")
_AlpsRemPeerConnIdleTimer_Type = TimeInterval
_AlpsRemPeerConnIdleTimer_Object = MibTableColumn
alpsRemPeerConnIdleTimer = _AlpsRemPeerConnIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 13),
    _AlpsRemPeerConnIdleTimer_Type()
)
alpsRemPeerConnIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnIdleTimer.setStatus("current")
_AlpsRemPeerConnNoCircTimer_Type = TimeInterval
_AlpsRemPeerConnNoCircTimer_Object = MibTableColumn
alpsRemPeerConnNoCircTimer = _AlpsRemPeerConnNoCircTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 14),
    _AlpsRemPeerConnNoCircTimer_Type()
)
alpsRemPeerConnNoCircTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnNoCircTimer.setStatus("current")


class _AlpsRemPeerConnTCPQLen_Type(Integer32):
    """Custom type alpsRemPeerConnTCPQLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlpsRemPeerConnTCPQLen_Type.__name__ = "Integer32"
_AlpsRemPeerConnTCPQLen_Object = MibTableColumn
alpsRemPeerConnTCPQLen = _AlpsRemPeerConnTCPQLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 15),
    _AlpsRemPeerConnTCPQLen_Type()
)
alpsRemPeerConnTCPQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnTCPQLen.setStatus("current")
_AlpsRemPeerConnAlarmsOn_Type = TruthValue
_AlpsRemPeerConnAlarmsOn_Object = MibTableColumn
alpsRemPeerConnAlarmsOn = _AlpsRemPeerConnAlarmsOn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 16),
    _AlpsRemPeerConnAlarmsOn_Type()
)
alpsRemPeerConnAlarmsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnAlarmsOn.setStatus("current")


class _AlpsRemPeerConnStatIntvl_Type(Integer32):
    """Custom type alpsRemPeerConnStatIntvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AlpsRemPeerConnStatIntvl_Type.__name__ = "Integer32"
_AlpsRemPeerConnStatIntvl_Object = MibTableColumn
alpsRemPeerConnStatIntvl = _AlpsRemPeerConnStatIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 17),
    _AlpsRemPeerConnStatIntvl_Type()
)
alpsRemPeerConnStatIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnStatIntvl.setStatus("current")


class _AlpsRemPeerConnStatRetry_Type(Integer32):
    """Custom type alpsRemPeerConnStatRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlpsRemPeerConnStatRetry_Type.__name__ = "Integer32"
_AlpsRemPeerConnStatRetry_Object = MibTableColumn
alpsRemPeerConnStatRetry = _AlpsRemPeerConnStatRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 18),
    _AlpsRemPeerConnStatRetry_Type()
)
alpsRemPeerConnStatRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnStatRetry.setStatus("current")


class _AlpsRemPeerConnDownReason_Type(Integer32):
    """Custom type alpsRemPeerConnDownReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("destUnreachable", 4),
          ("foreignReset", 5),
          ("idle", 2),
          ("localReset", 6),
          ("noCircuits", 3),
          ("noMemory", 7),
          ("openingTimeout", 8),
          ("unknown", 1))
    )


_AlpsRemPeerConnDownReason_Type.__name__ = "Integer32"
_AlpsRemPeerConnDownReason_Object = MibTableColumn
alpsRemPeerConnDownReason = _AlpsRemPeerConnDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 19),
    _AlpsRemPeerConnDownReason_Type()
)
alpsRemPeerConnDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnDownReason.setStatus("current")
_AlpsRemPeerConnOutPackets_Type = Counter32
_AlpsRemPeerConnOutPackets_Object = MibTableColumn
alpsRemPeerConnOutPackets = _AlpsRemPeerConnOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 20),
    _AlpsRemPeerConnOutPackets_Type()
)
alpsRemPeerConnOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    alpsRemPeerConnOutPackets.setUnits("packets")
_AlpsRemPeerConnOutOctets_Type = Counter32
_AlpsRemPeerConnOutOctets_Object = MibTableColumn
alpsRemPeerConnOutOctets = _AlpsRemPeerConnOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 21),
    _AlpsRemPeerConnOutOctets_Type()
)
alpsRemPeerConnOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    alpsRemPeerConnOutOctets.setUnits("packets")
_AlpsRemPeerConnInPackets_Type = Counter32
_AlpsRemPeerConnInPackets_Object = MibTableColumn
alpsRemPeerConnInPackets = _AlpsRemPeerConnInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 22),
    _AlpsRemPeerConnInPackets_Type()
)
alpsRemPeerConnInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnInPackets.setStatus("current")
if mibBuilder.loadTexts:
    alpsRemPeerConnInPackets.setUnits("packets")
_AlpsRemPeerConnInOctets_Type = Counter32
_AlpsRemPeerConnInOctets_Object = MibTableColumn
alpsRemPeerConnInOctets = _AlpsRemPeerConnInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 23),
    _AlpsRemPeerConnInOctets_Type()
)
alpsRemPeerConnInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnInOctets.setStatus("current")
if mibBuilder.loadTexts:
    alpsRemPeerConnInOctets.setUnits("packets")
_AlpsRemPeerConnDropsGiant_Type = Counter32
_AlpsRemPeerConnDropsGiant_Object = MibTableColumn
alpsRemPeerConnDropsGiant = _AlpsRemPeerConnDropsGiant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 24),
    _AlpsRemPeerConnDropsGiant_Type()
)
alpsRemPeerConnDropsGiant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnDropsGiant.setStatus("current")
if mibBuilder.loadTexts:
    alpsRemPeerConnDropsGiant.setUnits("packets")
_AlpsRemPeerConnDropsQFull_Type = Counter32
_AlpsRemPeerConnDropsQFull_Object = MibTableColumn
alpsRemPeerConnDropsQFull = _AlpsRemPeerConnDropsQFull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 25),
    _AlpsRemPeerConnDropsQFull_Type()
)
alpsRemPeerConnDropsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnDropsQFull.setStatus("current")
if mibBuilder.loadTexts:
    alpsRemPeerConnDropsQFull.setUnits("packets")
_AlpsRemPeerConnDropsUnreach_Type = Counter32
_AlpsRemPeerConnDropsUnreach_Object = MibTableColumn
alpsRemPeerConnDropsUnreach = _AlpsRemPeerConnDropsUnreach_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 26),
    _AlpsRemPeerConnDropsUnreach_Type()
)
alpsRemPeerConnDropsUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnDropsUnreach.setStatus("current")
if mibBuilder.loadTexts:
    alpsRemPeerConnDropsUnreach.setUnits("packets")
_AlpsRemPeerConnDropsVersion_Type = Counter32
_AlpsRemPeerConnDropsVersion_Object = MibTableColumn
alpsRemPeerConnDropsVersion = _AlpsRemPeerConnDropsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 2, 4, 1, 27),
    _AlpsRemPeerConnDropsVersion_Type()
)
alpsRemPeerConnDropsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsRemPeerConnDropsVersion.setStatus("current")
if mibBuilder.loadTexts:
    alpsRemPeerConnDropsVersion.setUnits("packets")
_AlpsCktObjects_ObjectIdentity = ObjectIdentity
alpsCktObjects = _AlpsCktObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3)
)
_AlpsCktBaseTable_Object = MibTable
alpsCktBaseTable = _AlpsCktBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alpsCktBaseTable.setStatus("current")
_AlpsCktBaseEntry_Object = MibTableRow
alpsCktBaseEntry = _AlpsCktBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1)
)
alpsCktBaseEntry.setIndexNames(
    (0, "CISCO-ALPS-MIB", "alpsCktBaseName"),
    (0, "CISCO-ALPS-MIB", "alpsCktBaseDlcType"),
)
if mibBuilder.loadTexts:
    alpsCktBaseEntry.setStatus("current")
_AlpsCktBaseName_Type = AlpsCktName
_AlpsCktBaseName_Object = MibTableColumn
alpsCktBaseName = _AlpsCktBaseName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 1),
    _AlpsCktBaseName_Type()
)
alpsCktBaseName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsCktBaseName.setStatus("current")


class _AlpsCktBaseDlcType_Type(Integer32):
    """Custom type alpsCktBaseDlcType based on Integer32"""
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
        *(("alc", 3),
          ("ax25", 2),
          ("emtox", 1),
          ("uts", 4))
    )


_AlpsCktBaseDlcType_Type.__name__ = "Integer32"
_AlpsCktBaseDlcType_Object = MibTableColumn
alpsCktBaseDlcType = _AlpsCktBaseDlcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 2),
    _AlpsCktBaseDlcType_Type()
)
alpsCktBaseDlcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsCktBaseDlcType.setStatus("current")
_AlpsCktBasePriPeerAddr_Type = IpAddress
_AlpsCktBasePriPeerAddr_Object = MibTableColumn
alpsCktBasePriPeerAddr = _AlpsCktBasePriPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 3),
    _AlpsCktBasePriPeerAddr_Type()
)
alpsCktBasePriPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBasePriPeerAddr.setStatus("current")


class _AlpsCktBaseAlarmsEnabled_Type(TruthValue):
    """Custom type alpsCktBaseAlarmsEnabled based on TruthValue"""


_AlpsCktBaseAlarmsEnabled_Object = MibTableColumn
alpsCktBaseAlarmsEnabled = _AlpsCktBaseAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 4),
    _AlpsCktBaseAlarmsEnabled_Type()
)
alpsCktBaseAlarmsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBaseAlarmsEnabled.setStatus("current")


class _AlpsCktBaseConnType_Type(Integer32):
    """Custom type alpsCktBaseConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("permanent", 1))
    )


_AlpsCktBaseConnType_Type.__name__ = "Integer32"
_AlpsCktBaseConnType_Object = MibTableColumn
alpsCktBaseConnType = _AlpsCktBaseConnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 5),
    _AlpsCktBaseConnType_Type()
)
alpsCktBaseConnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBaseConnType.setStatus("current")


class _AlpsCktBaseState_Type(Integer32):
    """Custom type alpsCktBaseState based on Integer32"""
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
        *(("cktBusy", 5),
          ("disabled", 1),
          ("inoperable", 2),
          ("opened", 4),
          ("opening", 3),
          ("peerBusy", 6),
          ("updating", 7))
    )


_AlpsCktBaseState_Type.__name__ = "Integer32"
_AlpsCktBaseState_Object = MibTableColumn
alpsCktBaseState = _AlpsCktBaseState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 6),
    _AlpsCktBaseState_Type()
)
alpsCktBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseState.setStatus("current")


class _AlpsCktBaseNumActiveAscus_Type(Integer32):
    """Custom type alpsCktBaseNumActiveAscus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AlpsCktBaseNumActiveAscus_Type.__name__ = "Integer32"
_AlpsCktBaseNumActiveAscus_Object = MibTableColumn
alpsCktBaseNumActiveAscus = _AlpsCktBaseNumActiveAscus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 7),
    _AlpsCktBaseNumActiveAscus_Type()
)
alpsCktBaseNumActiveAscus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseNumActiveAscus.setStatus("current")
_AlpsCktBaseCurrentPeer_Type = IpAddress
_AlpsCktBaseCurrentPeer_Object = MibTableColumn
alpsCktBaseCurrentPeer = _AlpsCktBaseCurrentPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 8),
    _AlpsCktBaseCurrentPeer_Type()
)
alpsCktBaseCurrentPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseCurrentPeer.setStatus("current")
_AlpsCktBaseLifeTimeTimer_Type = TimeInterval
_AlpsCktBaseLifeTimeTimer_Object = MibTableColumn
alpsCktBaseLifeTimeTimer = _AlpsCktBaseLifeTimeTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 9),
    _AlpsCktBaseLifeTimeTimer_Type()
)
alpsCktBaseLifeTimeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBaseLifeTimeTimer.setStatus("current")


class _AlpsCktBaseHostLinkNumber_Type(Integer32):
    """Custom type alpsCktBaseHostLinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlpsCktBaseHostLinkNumber_Type.__name__ = "Integer32"
_AlpsCktBaseHostLinkNumber_Object = MibTableColumn
alpsCktBaseHostLinkNumber = _AlpsCktBaseHostLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 10),
    _AlpsCktBaseHostLinkNumber_Type()
)
alpsCktBaseHostLinkNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBaseHostLinkNumber.setStatus("current")


class _AlpsCktBaseHostLinkType_Type(Integer32):
    """Custom type alpsCktBaseHostLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ax25", 1),
          ("emtox", 2))
    )


_AlpsCktBaseHostLinkType_Type.__name__ = "Integer32"
_AlpsCktBaseHostLinkType_Object = MibTableColumn
alpsCktBaseHostLinkType = _AlpsCktBaseHostLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 11),
    _AlpsCktBaseHostLinkType_Type()
)
alpsCktBaseHostLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBaseHostLinkType.setStatus("current")


class _AlpsCktBaseRemHld_Type(Integer32):
    """Custom type alpsCktBaseRemHld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32639),
    )


_AlpsCktBaseRemHld_Type.__name__ = "Integer32"
_AlpsCktBaseRemHld_Object = MibTableColumn
alpsCktBaseRemHld = _AlpsCktBaseRemHld_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 12),
    _AlpsCktBaseRemHld_Type()
)
alpsCktBaseRemHld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBaseRemHld.setStatus("current")


class _AlpsCktBaseLocalHld_Type(Integer32):
    """Custom type alpsCktBaseLocalHld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32639),
    )


_AlpsCktBaseLocalHld_Type.__name__ = "Integer32"
_AlpsCktBaseLocalHld_Object = MibTableColumn
alpsCktBaseLocalHld = _AlpsCktBaseLocalHld_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 13),
    _AlpsCktBaseLocalHld_Type()
)
alpsCktBaseLocalHld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBaseLocalHld.setStatus("current")


class _AlpsCktBaseDownReason_Type(Integer32):
    """Custom type alpsCktBaseDownReason based on Integer32"""
    defaultValue = 2

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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42)
        )
    )
    namedValues = NamedValues(
        *(("ascuInSession", 42),
          ("cktDisabled", 4),
          ("cktIdle", 16),
          ("cktNameInUse", 8),
          ("cktOpeningTimeout", 11),
          ("codingMismatch", 41),
          ("configMismatch", 13),
          ("hostLinkDisabled", 5),
          ("hostLinkDown", 3),
          ("incompatibleA1A2", 15),
          ("mpxHdrMismatch", 39),
          ("mpxUnknown", 38),
          ("noAscusConfigured", 18),
          ("noHldMatched", 7),
          ("noHostLinkMatched", 6),
          ("noReason", 2),
          ("noResourcesAvail", 14),
          ("noSvcLcnAvail", 33),
          ("openMsgTooShort", 37),
          ("peerDown", 17),
          ("peerIdle", 34),
          ("presMismatch", 36),
          ("presUnknown", 35),
          ("pvcLcnInUse", 32),
          ("pvcLcnOutOfRange", 9),
          ("trafTypeMismatch", 40),
          ("unknown", 1),
          ("x25ClearCallerUnauth", 24),
          ("x25ClearCallerUnknown", 23),
          ("x25ClearConfigFallback", 26),
          ("x25ClearConfigIncompat", 27),
          ("x25ClearConfigRejected", 25),
          ("x25ClearDteNoReason", 12),
          ("x25ClearFacilRejected", 30),
          ("x25ClearHLDUnknown", 28),
          ("x25ClearHostDisabled", 21),
          ("x25ClearHostDown", 20),
          ("x25ClearHostSaturated", 22),
          ("x25ClearHostUnknown", 19),
          ("x25ClearNetNoReason", 31),
          ("x25ClearPIDUnknown", 29),
          ("x25ParamInvalid", 10))
    )


_AlpsCktBaseDownReason_Type.__name__ = "Integer32"
_AlpsCktBaseDownReason_Object = MibTableColumn
alpsCktBaseDownReason = _AlpsCktBaseDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 14),
    _AlpsCktBaseDownReason_Type()
)
alpsCktBaseDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseDownReason.setStatus("current")
_AlpsCktBaseOutPackets_Type = Counter32
_AlpsCktBaseOutPackets_Object = MibTableColumn
alpsCktBaseOutPackets = _AlpsCktBaseOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 15),
    _AlpsCktBaseOutPackets_Type()
)
alpsCktBaseOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktBaseOutPackets.setUnits("packets")
_AlpsCktBaseOutOctets_Type = Counter32
_AlpsCktBaseOutOctets_Object = MibTableColumn
alpsCktBaseOutOctets = _AlpsCktBaseOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 16),
    _AlpsCktBaseOutOctets_Type()
)
alpsCktBaseOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktBaseOutOctets.setUnits("octets")
_AlpsCktBaseInPackets_Type = Counter32
_AlpsCktBaseInPackets_Object = MibTableColumn
alpsCktBaseInPackets = _AlpsCktBaseInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 17),
    _AlpsCktBaseInPackets_Type()
)
alpsCktBaseInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseInPackets.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktBaseInPackets.setUnits("packets")
_AlpsCktBaseInOctets_Type = Counter32
_AlpsCktBaseInOctets_Object = MibTableColumn
alpsCktBaseInOctets = _AlpsCktBaseInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 18),
    _AlpsCktBaseInOctets_Type()
)
alpsCktBaseInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseInOctets.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktBaseInOctets.setUnits("octets")
_AlpsCktBaseDropsCktDisabled_Type = Counter32
_AlpsCktBaseDropsCktDisabled_Object = MibTableColumn
alpsCktBaseDropsCktDisabled = _AlpsCktBaseDropsCktDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 19),
    _AlpsCktBaseDropsCktDisabled_Type()
)
alpsCktBaseDropsCktDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseDropsCktDisabled.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktBaseDropsCktDisabled.setUnits("packets")
_AlpsCktBaseDropsQOverflow_Type = Counter32
_AlpsCktBaseDropsQOverflow_Object = MibTableColumn
alpsCktBaseDropsQOverflow = _AlpsCktBaseDropsQOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 20),
    _AlpsCktBaseDropsQOverflow_Type()
)
alpsCktBaseDropsQOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseDropsQOverflow.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktBaseDropsQOverflow.setUnits("packets")
_AlpsCktBaseDropsLifeTimeExpd_Type = Counter32
_AlpsCktBaseDropsLifeTimeExpd_Object = MibTableColumn
alpsCktBaseDropsLifeTimeExpd = _AlpsCktBaseDropsLifeTimeExpd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 21),
    _AlpsCktBaseDropsLifeTimeExpd_Type()
)
alpsCktBaseDropsLifeTimeExpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseDropsLifeTimeExpd.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktBaseDropsLifeTimeExpd.setUnits("packets")


class _AlpsCktBaseEnabled_Type(TruthValue):
    """Custom type alpsCktBaseEnabled based on TruthValue"""


_AlpsCktBaseEnabled_Object = MibTableColumn
alpsCktBaseEnabled = _AlpsCktBaseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 22),
    _AlpsCktBaseEnabled_Type()
)
alpsCktBaseEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBaseEnabled.setStatus("current")
_AlpsCktBaseRowStatus_Type = RowStatus
_AlpsCktBaseRowStatus_Object = MibTableColumn
alpsCktBaseRowStatus = _AlpsCktBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 23),
    _AlpsCktBaseRowStatus_Type()
)
alpsCktBaseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktBaseRowStatus.setStatus("current")


class _AlpsCktBaseCurrPeerConnId_Type(DisplayString):
    """Custom type alpsCktBaseCurrPeerConnId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AlpsCktBaseCurrPeerConnId_Type.__name__ = "DisplayString"
_AlpsCktBaseCurrPeerConnId_Object = MibTableColumn
alpsCktBaseCurrPeerConnId = _AlpsCktBaseCurrPeerConnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 1, 1, 24),
    _AlpsCktBaseCurrPeerConnId_Type()
)
alpsCktBaseCurrPeerConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktBaseCurrPeerConnId.setStatus("current")
_AlpsCktX25Table_Object = MibTable
alpsCktX25Table = _AlpsCktX25Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 2)
)
if mibBuilder.loadTexts:
    alpsCktX25Table.setStatus("current")
_AlpsCktX25Entry_Object = MibTableRow
alpsCktX25Entry = _AlpsCktX25Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 2, 1)
)
alpsCktX25Entry.setIndexNames(
    (0, "CISCO-ALPS-MIB", "alpsCktBaseName"),
    (0, "CISCO-ALPS-MIB", "alpsCktX25DlcType"),
)
if mibBuilder.loadTexts:
    alpsCktX25Entry.setStatus("current")


class _AlpsCktX25DlcType_Type(Integer32):
    """Custom type alpsCktX25DlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ax25", 2),
          ("emtox", 1))
    )


_AlpsCktX25DlcType_Type.__name__ = "Integer32"
_AlpsCktX25DlcType_Object = MibTableColumn
alpsCktX25DlcType = _AlpsCktX25DlcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 2, 1, 1),
    _AlpsCktX25DlcType_Type()
)
alpsCktX25DlcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsCktX25DlcType.setStatus("current")
_AlpsCktX25IfIndex_Type = InterfaceIndex
_AlpsCktX25IfIndex_Object = MibTableColumn
alpsCktX25IfIndex = _AlpsCktX25IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 2, 1, 2),
    _AlpsCktX25IfIndex_Type()
)
alpsCktX25IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktX25IfIndex.setStatus("current")


class _AlpsCktX25LCN_Type(Integer32):
    """Custom type alpsCktX25LCN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlpsCktX25LCN_Type.__name__ = "Integer32"
_AlpsCktX25LCN_Object = MibTableColumn
alpsCktX25LCN = _AlpsCktX25LCN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 2, 1, 3),
    _AlpsCktX25LCN_Type()
)
alpsCktX25LCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktX25LCN.setStatus("current")
_AlpsCktX25HostX121_Type = X121Address
_AlpsCktX25HostX121_Object = MibTableColumn
alpsCktX25HostX121 = _AlpsCktX25HostX121_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 2, 1, 4),
    _AlpsCktX25HostX121_Type()
)
alpsCktX25HostX121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktX25HostX121.setStatus("current")
_AlpsCktX25RemoteX121_Type = X121Address
_AlpsCktX25RemoteX121_Object = MibTableColumn
alpsCktX25RemoteX121 = _AlpsCktX25RemoteX121_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 2, 1, 5),
    _AlpsCktX25RemoteX121_Type()
)
alpsCktX25RemoteX121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktX25RemoteX121.setStatus("current")
_AlpsCktX25DropsVcReset_Type = Counter32
_AlpsCktX25DropsVcReset_Object = MibTableColumn
alpsCktX25DropsVcReset = _AlpsCktX25DropsVcReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 2, 1, 6),
    _AlpsCktX25DropsVcReset_Type()
)
alpsCktX25DropsVcReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktX25DropsVcReset.setStatus("current")
_AlpsCktP1024Table_Object = MibTable
alpsCktP1024Table = _AlpsCktP1024Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3)
)
if mibBuilder.loadTexts:
    alpsCktP1024Table.setStatus("current")
_AlpsCktP1024Entry_Object = MibTableRow
alpsCktP1024Entry = _AlpsCktP1024Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1)
)
alpsCktP1024Entry.setIndexNames(
    (0, "CISCO-ALPS-MIB", "alpsCktBaseName"),
    (0, "CISCO-ALPS-MIB", "alpsCktP1024DlcType"),
)
if mibBuilder.loadTexts:
    alpsCktP1024Entry.setStatus("current")


class _AlpsCktP1024DlcType_Type(Integer32):
    """Custom type alpsCktP1024DlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alc", 3),
          ("uts", 4))
    )


_AlpsCktP1024DlcType_Type.__name__ = "Integer32"
_AlpsCktP1024DlcType_Object = MibTableColumn
alpsCktP1024DlcType = _AlpsCktP1024DlcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 1),
    _AlpsCktP1024DlcType_Type()
)
alpsCktP1024DlcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsCktP1024DlcType.setStatus("current")
_AlpsCktP1024BackupPeerAddr_Type = IpAddress
_AlpsCktP1024BackupPeerAddr_Object = MibTableColumn
alpsCktP1024BackupPeerAddr = _AlpsCktP1024BackupPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 2),
    _AlpsCktP1024BackupPeerAddr_Type()
)
alpsCktP1024BackupPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024BackupPeerAddr.setStatus("current")
_AlpsCktP1024RetryTimer_Type = TimeInterval
_AlpsCktP1024RetryTimer_Object = MibTableColumn
alpsCktP1024RetryTimer = _AlpsCktP1024RetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 3),
    _AlpsCktP1024RetryTimer_Type()
)
alpsCktP1024RetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024RetryTimer.setStatus("current")
_AlpsCktP1024IdleTimer_Type = TimeInterval
_AlpsCktP1024IdleTimer_Object = MibTableColumn
alpsCktP1024IdleTimer = _AlpsCktP1024IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 4),
    _AlpsCktP1024IdleTimer_Type()
)
alpsCktP1024IdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024IdleTimer.setStatus("current")
_AlpsCktP1024EmtoxX121_Type = X121Address
_AlpsCktP1024EmtoxX121_Object = MibTableColumn
alpsCktP1024EmtoxX121 = _AlpsCktP1024EmtoxX121_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 5),
    _AlpsCktP1024EmtoxX121_Type()
)
alpsCktP1024EmtoxX121.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024EmtoxX121.setStatus("current")


class _AlpsCktP1024Ax25LCN_Type(Integer32):
    """Custom type alpsCktP1024Ax25LCN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AlpsCktP1024Ax25LCN_Type.__name__ = "Integer32"
_AlpsCktP1024Ax25LCN_Object = MibTableColumn
alpsCktP1024Ax25LCN = _AlpsCktP1024Ax25LCN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 6),
    _AlpsCktP1024Ax25LCN_Type()
)
alpsCktP1024Ax25LCN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024Ax25LCN.setStatus("current")


class _AlpsCktP1024WinOut_Type(Integer32):
    """Custom type alpsCktP1024WinOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AlpsCktP1024WinOut_Type.__name__ = "Integer32"
_AlpsCktP1024WinOut_Object = MibTableColumn
alpsCktP1024WinOut = _AlpsCktP1024WinOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 7),
    _AlpsCktP1024WinOut_Type()
)
alpsCktP1024WinOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024WinOut.setStatus("current")


class _AlpsCktP1024WinIn_Type(Integer32):
    """Custom type alpsCktP1024WinIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AlpsCktP1024WinIn_Type.__name__ = "Integer32"
_AlpsCktP1024WinIn_Object = MibTableColumn
alpsCktP1024WinIn = _AlpsCktP1024WinIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 8),
    _AlpsCktP1024WinIn_Type()
)
alpsCktP1024WinIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024WinIn.setStatus("current")


class _AlpsCktP1024OutPktSize_Type(Integer32):
    """Custom type alpsCktP1024OutPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 4096),
    )


_AlpsCktP1024OutPktSize_Type.__name__ = "Integer32"
_AlpsCktP1024OutPktSize_Object = MibTableColumn
alpsCktP1024OutPktSize = _AlpsCktP1024OutPktSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 9),
    _AlpsCktP1024OutPktSize_Type()
)
alpsCktP1024OutPktSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024OutPktSize.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktP1024OutPktSize.setUnits("bytes")


class _AlpsCktP1024InPktSize_Type(Integer32):
    """Custom type alpsCktP1024InPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 4096),
    )


_AlpsCktP1024InPktSize_Type.__name__ = "Integer32"
_AlpsCktP1024InPktSize_Object = MibTableColumn
alpsCktP1024InPktSize = _AlpsCktP1024InPktSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 10),
    _AlpsCktP1024InPktSize_Type()
)
alpsCktP1024InPktSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024InPktSize.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktP1024InPktSize.setUnits("bytes")


class _AlpsCktP1024SvcMsgList_Type(Integer32):
    """Custom type alpsCktP1024SvcMsgList based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AlpsCktP1024SvcMsgList_Type.__name__ = "Integer32"
_AlpsCktP1024SvcMsgList_Object = MibTableColumn
alpsCktP1024SvcMsgList = _AlpsCktP1024SvcMsgList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 11),
    _AlpsCktP1024SvcMsgList_Type()
)
alpsCktP1024SvcMsgList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024SvcMsgList.setStatus("current")
_AlpsCktP1024SvcMsgIntvl_Type = TimeTicks
_AlpsCktP1024SvcMsgIntvl_Object = MibTableColumn
alpsCktP1024SvcMsgIntvl = _AlpsCktP1024SvcMsgIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 12),
    _AlpsCktP1024SvcMsgIntvl_Type()
)
alpsCktP1024SvcMsgIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024SvcMsgIntvl.setStatus("current")
_AlpsCktP1024DropsUnkAscu_Type = Counter32
_AlpsCktP1024DropsUnkAscu_Object = MibTableColumn
alpsCktP1024DropsUnkAscu = _AlpsCktP1024DropsUnkAscu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 13),
    _AlpsCktP1024DropsUnkAscu_Type()
)
alpsCktP1024DropsUnkAscu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktP1024DropsUnkAscu.setStatus("current")
if mibBuilder.loadTexts:
    alpsCktP1024DropsUnkAscu.setUnits("packets")
_AlpsCktP1024RowStatus_Type = RowStatus
_AlpsCktP1024RowStatus_Object = MibTableColumn
alpsCktP1024RowStatus = _AlpsCktP1024RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 14),
    _AlpsCktP1024RowStatus_Type()
)
alpsCktP1024RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024RowStatus.setStatus("current")
_AlpsCktP1024MatipCloseDelay_Type = TimeInterval
_AlpsCktP1024MatipCloseDelay_Object = MibTableColumn
alpsCktP1024MatipCloseDelay = _AlpsCktP1024MatipCloseDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 3, 1, 15),
    _AlpsCktP1024MatipCloseDelay_Type()
)
alpsCktP1024MatipCloseDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsCktP1024MatipCloseDelay.setStatus("current")
_AlpsCktAscuTable_Object = MibTable
alpsCktAscuTable = _AlpsCktAscuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 4)
)
if mibBuilder.loadTexts:
    alpsCktAscuTable.setStatus("current")
_AlpsCktAscuEntry_Object = MibTableRow
alpsCktAscuEntry = _AlpsCktAscuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 4, 1)
)
alpsCktAscuEntry.setIndexNames(
    (0, "CISCO-ALPS-MIB", "alpsCktAscuCktName"),
    (0, "CISCO-ALPS-MIB", "alpsCktAscuCktDlcType"),
    (0, "CISCO-ALPS-MIB", "alpsCktAscuA1"),
    (0, "CISCO-ALPS-MIB", "alpsCktAscuA2"),
)
if mibBuilder.loadTexts:
    alpsCktAscuEntry.setStatus("current")
_AlpsCktAscuCktName_Type = AlpsCktName
_AlpsCktAscuCktName_Object = MibTableColumn
alpsCktAscuCktName = _AlpsCktAscuCktName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 4, 1, 1),
    _AlpsCktAscuCktName_Type()
)
alpsCktAscuCktName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsCktAscuCktName.setStatus("current")


class _AlpsCktAscuCktDlcType_Type(Integer32):
    """Custom type alpsCktAscuCktDlcType based on Integer32"""
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
        *(("alc", 3),
          ("ax25", 2),
          ("emtox", 1),
          ("uts", 4))
    )


_AlpsCktAscuCktDlcType_Type.__name__ = "Integer32"
_AlpsCktAscuCktDlcType_Object = MibTableColumn
alpsCktAscuCktDlcType = _AlpsCktAscuCktDlcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 4, 1, 2),
    _AlpsCktAscuCktDlcType_Type()
)
alpsCktAscuCktDlcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsCktAscuCktDlcType.setStatus("current")
_AlpsCktAscuA1_Type = AlpsAscuA1A2Value
_AlpsCktAscuA1_Object = MibTableColumn
alpsCktAscuA1 = _AlpsCktAscuA1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 4, 1, 3),
    _AlpsCktAscuA1_Type()
)
alpsCktAscuA1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsCktAscuA1.setStatus("current")
_AlpsCktAscuA2_Type = AlpsAscuA1A2Value
_AlpsCktAscuA2_Object = MibTableColumn
alpsCktAscuA2 = _AlpsCktAscuA2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 4, 1, 4),
    _AlpsCktAscuA2_Type()
)
alpsCktAscuA2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsCktAscuA2.setStatus("current")
_AlpsCktAscuIfIndex_Type = InterfaceIndex
_AlpsCktAscuIfIndex_Object = MibTableColumn
alpsCktAscuIfIndex = _AlpsCktAscuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 4, 1, 5),
    _AlpsCktAscuIfIndex_Type()
)
alpsCktAscuIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktAscuIfIndex.setStatus("current")


class _AlpsCktAscuId_Type(Integer32):
    """Custom type alpsCktAscuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AlpsCktAscuId_Type.__name__ = "Integer32"
_AlpsCktAscuId_Object = MibTableColumn
alpsCktAscuId = _AlpsCktAscuId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 4, 1, 6),
    _AlpsCktAscuId_Type()
)
alpsCktAscuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktAscuId.setStatus("current")


class _AlpsCktAscuStatus_Type(Integer32):
    """Custom type alpsCktAscuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("new", 4),
          ("ok", 2),
          ("pending", 5),
          ("reject", 3),
          ("unknown", 1))
    )


_AlpsCktAscuStatus_Type.__name__ = "Integer32"
_AlpsCktAscuStatus_Object = MibTableColumn
alpsCktAscuStatus = _AlpsCktAscuStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 3, 4, 1, 7),
    _AlpsCktAscuStatus_Type()
)
alpsCktAscuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsCktAscuStatus.setStatus("current")
_AlpsIfObjects_ObjectIdentity = ObjectIdentity
alpsIfObjects = _AlpsIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4)
)
_AlpsIfP1024Table_Object = MibTable
alpsIfP1024Table = _AlpsIfP1024Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alpsIfP1024Table.setStatus("current")
_AlpsIfP1024Entry_Object = MibTableRow
alpsIfP1024Entry = _AlpsIfP1024Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1)
)
alpsIfP1024Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alpsIfP1024Entry.setStatus("current")


class _AlpsIfP1024EncapType_Type(Integer32):
    """Custom type alpsIfP1024EncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alc", 1),
          ("uts", 2))
    )


_AlpsIfP1024EncapType_Type.__name__ = "Integer32"
_AlpsIfP1024EncapType_Object = MibTableColumn
alpsIfP1024EncapType = _AlpsIfP1024EncapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 1),
    _AlpsIfP1024EncapType_Type()
)
alpsIfP1024EncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsIfP1024EncapType.setStatus("current")


class _AlpsIfP1024PollRespTimeout_Type(TimeInterval):
    """Custom type alpsIfP1024PollRespTimeout based on TimeInterval"""
    defaultValue = 500


_AlpsIfP1024PollRespTimeout_Object = MibTableColumn
alpsIfP1024PollRespTimeout = _AlpsIfP1024PollRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 2),
    _AlpsIfP1024PollRespTimeout_Type()
)
alpsIfP1024PollRespTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024PollRespTimeout.setStatus("current")


class _AlpsIfP1024GATimeout_Type(TimeInterval):
    """Custom type alpsIfP1024GATimeout based on TimeInterval"""
    defaultValue = 600


_AlpsIfP1024GATimeout_Object = MibTableColumn
alpsIfP1024GATimeout = _AlpsIfP1024GATimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 3),
    _AlpsIfP1024GATimeout_Type()
)
alpsIfP1024GATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024GATimeout.setStatus("current")


class _AlpsIfP1024PollPauseTimeout_Type(TimeInterval):
    """Custom type alpsIfP1024PollPauseTimeout based on TimeInterval"""
    defaultValue = 50


_AlpsIfP1024PollPauseTimeout_Object = MibTableColumn
alpsIfP1024PollPauseTimeout = _AlpsIfP1024PollPauseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 4),
    _AlpsIfP1024PollPauseTimeout_Type()
)
alpsIfP1024PollPauseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024PollPauseTimeout.setStatus("current")


class _AlpsIfP1024MaxErrCnt_Type(Integer32):
    """Custom type alpsIfP1024MaxErrCnt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AlpsIfP1024MaxErrCnt_Type.__name__ = "Integer32"
_AlpsIfP1024MaxErrCnt_Object = MibTableColumn
alpsIfP1024MaxErrCnt = _AlpsIfP1024MaxErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 5),
    _AlpsIfP1024MaxErrCnt_Type()
)
alpsIfP1024MaxErrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024MaxErrCnt.setStatus("current")


class _AlpsIfP1024MaxRetrans_Type(Integer32):
    """Custom type alpsIfP1024MaxRetrans based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AlpsIfP1024MaxRetrans_Type.__name__ = "Integer32"
_AlpsIfP1024MaxRetrans_Object = MibTableColumn
alpsIfP1024MaxRetrans = _AlpsIfP1024MaxRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 6),
    _AlpsIfP1024MaxRetrans_Type()
)
alpsIfP1024MaxRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024MaxRetrans.setStatus("current")


class _AlpsIfP1024CurrErrCnt_Type(Integer32):
    """Custom type alpsIfP1024CurrErrCnt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AlpsIfP1024CurrErrCnt_Type.__name__ = "Integer32"
_AlpsIfP1024CurrErrCnt_Object = MibTableColumn
alpsIfP1024CurrErrCnt = _AlpsIfP1024CurrErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 7),
    _AlpsIfP1024CurrErrCnt_Type()
)
alpsIfP1024CurrErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsIfP1024CurrErrCnt.setStatus("current")


class _AlpsIfP1024MinGoodPollResp_Type(Integer32):
    """Custom type alpsIfP1024MinGoodPollResp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AlpsIfP1024MinGoodPollResp_Type.__name__ = "Integer32"
_AlpsIfP1024MinGoodPollResp_Object = MibTableColumn
alpsIfP1024MinGoodPollResp = _AlpsIfP1024MinGoodPollResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 8),
    _AlpsIfP1024MinGoodPollResp_Type()
)
alpsIfP1024MinGoodPollResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024MinGoodPollResp.setStatus("current")


class _AlpsIfP1024PollingRatio_Type(Integer32):
    """Custom type alpsIfP1024PollingRatio based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AlpsIfP1024PollingRatio_Type.__name__ = "Integer32"
_AlpsIfP1024PollingRatio_Object = MibTableColumn
alpsIfP1024PollingRatio = _AlpsIfP1024PollingRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 9),
    _AlpsIfP1024PollingRatio_Type()
)
alpsIfP1024PollingRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024PollingRatio.setStatus("current")


class _AlpsIfP1024NumAscus_Type(Gauge32):
    """Custom type alpsIfP1024NumAscus based on Gauge32"""
    defaultValue = 0


_AlpsIfP1024NumAscus_Object = MibTableColumn
alpsIfP1024NumAscus = _AlpsIfP1024NumAscus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 10),
    _AlpsIfP1024NumAscus_Type()
)
alpsIfP1024NumAscus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsIfP1024NumAscus.setStatus("current")
if mibBuilder.loadTexts:
    alpsIfP1024NumAscus.setUnits("Ascus")


class _AlpsIfP1024ServMsgFormat_Type(Integer32):
    """Custom type alpsIfP1024ServMsgFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apollo", 2),
          ("sita", 1))
    )


_AlpsIfP1024ServMsgFormat_Type.__name__ = "Integer32"
_AlpsIfP1024ServMsgFormat_Object = MibTableColumn
alpsIfP1024ServMsgFormat = _AlpsIfP1024ServMsgFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 11),
    _AlpsIfP1024ServMsgFormat_Type()
)
alpsIfP1024ServMsgFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024ServMsgFormat.setStatus("current")


class _AlpsIfP1024ServMsgStatusChange_Type(TruthValue):
    """Custom type alpsIfP1024ServMsgStatusChange based on TruthValue"""


_AlpsIfP1024ServMsgStatusChange_Object = MibTableColumn
alpsIfP1024ServMsgStatusChange = _AlpsIfP1024ServMsgStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 12),
    _AlpsIfP1024ServMsgStatusChange_Type()
)
alpsIfP1024ServMsgStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024ServMsgStatusChange.setStatus("current")


class _AlpsIfP1024ServMsgDropTermAddr_Type(Integer32):
    """Custom type alpsIfP1024ServMsgDropTermAddr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configterm", 2),
          ("msgterm", 1))
    )


_AlpsIfP1024ServMsgDropTermAddr_Type.__name__ = "Integer32"
_AlpsIfP1024ServMsgDropTermAddr_Object = MibTableColumn
alpsIfP1024ServMsgDropTermAddr = _AlpsIfP1024ServMsgDropTermAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 1, 1, 13),
    _AlpsIfP1024ServMsgDropTermAddr_Type()
)
alpsIfP1024ServMsgDropTermAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alpsIfP1024ServMsgDropTermAddr.setStatus("current")
_AlpsIfHLinkTable_Object = MibTable
alpsIfHLinkTable = _AlpsIfHLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 2)
)
if mibBuilder.loadTexts:
    alpsIfHLinkTable.setStatus("current")
_AlpsIfHLinkEntry_Object = MibTableRow
alpsIfHLinkEntry = _AlpsIfHLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 2, 1)
)
alpsIfHLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ALPS-MIB", "alpsIfHLinkHostHld"),
    (0, "CISCO-ALPS-MIB", "alpsIfHLinkNumber"),
)
if mibBuilder.loadTexts:
    alpsIfHLinkEntry.setStatus("current")


class _AlpsIfHLinkHostHld_Type(Integer32):
    """Custom type alpsIfHLinkHostHld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlpsIfHLinkHostHld_Type.__name__ = "Integer32"
_AlpsIfHLinkHostHld_Object = MibTableColumn
alpsIfHLinkHostHld = _AlpsIfHLinkHostHld_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 2, 1, 1),
    _AlpsIfHLinkHostHld_Type()
)
alpsIfHLinkHostHld.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsIfHLinkHostHld.setStatus("current")


class _AlpsIfHLinkNumber_Type(Integer32):
    """Custom type alpsIfHLinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlpsIfHLinkNumber_Type.__name__ = "Integer32"
_AlpsIfHLinkNumber_Object = MibTableColumn
alpsIfHLinkNumber = _AlpsIfHLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 2, 1, 2),
    _AlpsIfHLinkNumber_Type()
)
alpsIfHLinkNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsIfHLinkNumber.setStatus("current")


class _AlpsIfHLinkX25ProtocolType_Type(Integer32):
    """Custom type alpsIfHLinkX25ProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ax25", 1),
          ("emtox", 2))
    )


_AlpsIfHLinkX25ProtocolType_Type.__name__ = "Integer32"
_AlpsIfHLinkX25ProtocolType_Object = MibTableColumn
alpsIfHLinkX25ProtocolType = _AlpsIfHLinkX25ProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 2, 1, 3),
    _AlpsIfHLinkX25ProtocolType_Type()
)
alpsIfHLinkX25ProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsIfHLinkX25ProtocolType.setStatus("current")
_AlpsIfHLinkAx25PvcDamp_Type = TimeInterval
_AlpsIfHLinkAx25PvcDamp_Object = MibTableColumn
alpsIfHLinkAx25PvcDamp = _AlpsIfHLinkAx25PvcDamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 2, 1, 4),
    _AlpsIfHLinkAx25PvcDamp_Type()
)
alpsIfHLinkAx25PvcDamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsIfHLinkAx25PvcDamp.setStatus("current")
_AlpsIfHLinkEmtoxHostX121_Type = X121Address
_AlpsIfHLinkEmtoxHostX121_Object = MibTableColumn
alpsIfHLinkEmtoxHostX121 = _AlpsIfHLinkEmtoxHostX121_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 2, 1, 5),
    _AlpsIfHLinkEmtoxHostX121_Type()
)
alpsIfHLinkEmtoxHostX121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsIfHLinkEmtoxHostX121.setStatus("current")


class _AlpsIfHLinkActiveCkts_Type(Integer32):
    """Custom type alpsIfHLinkActiveCkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AlpsIfHLinkActiveCkts_Type.__name__ = "Integer32"
_AlpsIfHLinkActiveCkts_Object = MibTableColumn
alpsIfHLinkActiveCkts = _AlpsIfHLinkActiveCkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 4, 2, 1, 6),
    _AlpsIfHLinkActiveCkts_Type()
)
alpsIfHLinkActiveCkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsIfHLinkActiveCkts.setStatus("current")
if mibBuilder.loadTexts:
    alpsIfHLinkActiveCkts.setUnits("circuits")
_AlpsAscuObjects_ObjectIdentity = ObjectIdentity
alpsAscuObjects = _AlpsAscuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5)
)
_AlpsAscuTable_Object = MibTable
alpsAscuTable = _AlpsAscuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alpsAscuTable.setStatus("current")
_AlpsAscuEntry_Object = MibTableRow
alpsAscuEntry = _AlpsAscuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1)
)
alpsAscuEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ALPS-MIB", "alpsAscuId"),
)
if mibBuilder.loadTexts:
    alpsAscuEntry.setStatus("current")


class _AlpsAscuId_Type(Integer32):
    """Custom type alpsAscuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AlpsAscuId_Type.__name__ = "Integer32"
_AlpsAscuId_Object = MibTableColumn
alpsAscuId = _AlpsAscuId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 1),
    _AlpsAscuId_Type()
)
alpsAscuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsAscuId.setStatus("current")
_AlpsAscuA1_Type = AlpsAscuA1A2Value
_AlpsAscuA1_Object = MibTableColumn
alpsAscuA1 = _AlpsAscuA1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 2),
    _AlpsAscuA1_Type()
)
alpsAscuA1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuA1.setStatus("current")
_AlpsAscuA2_Type = AlpsAscuA1A2Value
_AlpsAscuA2_Object = MibTableColumn
alpsAscuA2 = _AlpsAscuA2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 3),
    _AlpsAscuA2_Type()
)
alpsAscuA2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuA2.setStatus("current")
_AlpsAscuCktName_Type = AlpsCktName
_AlpsAscuCktName_Object = MibTableColumn
alpsAscuCktName = _AlpsAscuCktName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 4),
    _AlpsAscuCktName_Type()
)
alpsAscuCktName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuCktName.setStatus("current")


class _AlpsAscuAlarmsEnabled_Type(TruthValue):
    """Custom type alpsAscuAlarmsEnabled based on TruthValue"""


_AlpsAscuAlarmsEnabled_Object = MibTableColumn
alpsAscuAlarmsEnabled = _AlpsAscuAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 5),
    _AlpsAscuAlarmsEnabled_Type()
)
alpsAscuAlarmsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuAlarmsEnabled.setStatus("current")


class _AlpsAscuRetryOption_Type(Integer32):
    """Custom type alpsAscuRetryOption based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("reenter", 2),
          ("resend", 1))
    )


_AlpsAscuRetryOption_Type.__name__ = "Integer32"
_AlpsAscuRetryOption_Object = MibTableColumn
alpsAscuRetryOption = _AlpsAscuRetryOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 6),
    _AlpsAscuRetryOption_Type()
)
alpsAscuRetryOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuRetryOption.setStatus("current")


class _AlpsAscuMaxMsgLength_Type(Integer32):
    """Custom type alpsAscuMaxMsgLength based on Integer32"""
    defaultValue = 962

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3840),
    )


_AlpsAscuMaxMsgLength_Type.__name__ = "Integer32"
_AlpsAscuMaxMsgLength_Object = MibTableColumn
alpsAscuMaxMsgLength = _AlpsAscuMaxMsgLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 7),
    _AlpsAscuMaxMsgLength_Type()
)
alpsAscuMaxMsgLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuMaxMsgLength.setStatus("current")
if mibBuilder.loadTexts:
    alpsAscuMaxMsgLength.setUnits("bytes")


class _AlpsAscuFwdStatusOption_Type(TruthValue):
    """Custom type alpsAscuFwdStatusOption based on TruthValue"""


_AlpsAscuFwdStatusOption_Object = MibTableColumn
alpsAscuFwdStatusOption = _AlpsAscuFwdStatusOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 8),
    _AlpsAscuFwdStatusOption_Type()
)
alpsAscuFwdStatusOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuFwdStatusOption.setStatus("current")


class _AlpsAscuState_Type(Integer32):
    """Custom type alpsAscuState based on Integer32"""
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
        *(("disabled", 1),
          ("down", 3),
          ("unknown", 2),
          ("up", 4))
    )


_AlpsAscuState_Type.__name__ = "Integer32"
_AlpsAscuState_Object = MibTableColumn
alpsAscuState = _AlpsAscuState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 9),
    _AlpsAscuState_Type()
)
alpsAscuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsAscuState.setStatus("current")


class _AlpsAscuDownReason_Type(Integer32):
    """Custom type alpsAscuDownReason based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ascuDisabled", 4),
          ("errorThresholdExceeded", 5),
          ("noReason", 2),
          ("notDown", 3),
          ("unknown", 1))
    )


_AlpsAscuDownReason_Type.__name__ = "Integer32"
_AlpsAscuDownReason_Object = MibTableColumn
alpsAscuDownReason = _AlpsAscuDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 10),
    _AlpsAscuDownReason_Type()
)
alpsAscuDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsAscuDownReason.setStatus("current")
_AlpsAscuOutPackets_Type = Counter32
_AlpsAscuOutPackets_Object = MibTableColumn
alpsAscuOutPackets = _AlpsAscuOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 11),
    _AlpsAscuOutPackets_Type()
)
alpsAscuOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsAscuOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    alpsAscuOutPackets.setUnits("packets")
_AlpsAscuOutOctets_Type = Counter32
_AlpsAscuOutOctets_Object = MibTableColumn
alpsAscuOutOctets = _AlpsAscuOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 12),
    _AlpsAscuOutOctets_Type()
)
alpsAscuOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsAscuOutOctets.setStatus("current")
_AlpsAscuInPackets_Type = Counter32
_AlpsAscuInPackets_Object = MibTableColumn
alpsAscuInPackets = _AlpsAscuInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 13),
    _AlpsAscuInPackets_Type()
)
alpsAscuInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsAscuInPackets.setStatus("current")
if mibBuilder.loadTexts:
    alpsAscuInPackets.setUnits("packets")
_AlpsAscuInOctets_Type = Counter32
_AlpsAscuInOctets_Object = MibTableColumn
alpsAscuInOctets = _AlpsAscuInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 14),
    _AlpsAscuInOctets_Type()
)
alpsAscuInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsAscuInOctets.setStatus("current")
_AlpsAscuDropsGarbledPkts_Type = Counter32
_AlpsAscuDropsGarbledPkts_Object = MibTableColumn
alpsAscuDropsGarbledPkts = _AlpsAscuDropsGarbledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 15),
    _AlpsAscuDropsGarbledPkts_Type()
)
alpsAscuDropsGarbledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsAscuDropsGarbledPkts.setStatus("current")
_AlpsAscuDropsAscuDown_Type = Counter32
_AlpsAscuDropsAscuDown_Object = MibTableColumn
alpsAscuDropsAscuDown = _AlpsAscuDropsAscuDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 16),
    _AlpsAscuDropsAscuDown_Type()
)
alpsAscuDropsAscuDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsAscuDropsAscuDown.setStatus("current")
_AlpsAscuDropsAscuDisabled_Type = Counter32
_AlpsAscuDropsAscuDisabled_Object = MibTableColumn
alpsAscuDropsAscuDisabled = _AlpsAscuDropsAscuDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 17),
    _AlpsAscuDropsAscuDisabled_Type()
)
alpsAscuDropsAscuDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alpsAscuDropsAscuDisabled.setStatus("current")


class _AlpsAscuEnabled_Type(TruthValue):
    """Custom type alpsAscuEnabled based on TruthValue"""


_AlpsAscuEnabled_Object = MibTableColumn
alpsAscuEnabled = _AlpsAscuEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 18),
    _AlpsAscuEnabled_Type()
)
alpsAscuEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuEnabled.setStatus("current")
_AlpsAscuRowStatus_Type = RowStatus
_AlpsAscuRowStatus_Object = MibTableColumn
alpsAscuRowStatus = _AlpsAscuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 19),
    _AlpsAscuRowStatus_Type()
)
alpsAscuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuRowStatus.setStatus("current")


class _AlpsAscuAutoReset_Type(TruthValue):
    """Custom type alpsAscuAutoReset based on TruthValue"""


_AlpsAscuAutoReset_Object = MibTableColumn
alpsAscuAutoReset = _AlpsAscuAutoReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 5, 1, 1, 20),
    _AlpsAscuAutoReset_Type()
)
alpsAscuAutoReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsAscuAutoReset.setStatus("current")
_AlpsGlobalObjects_ObjectIdentity = ObjectIdentity
alpsGlobalObjects = _AlpsGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6)
)
_AlpsSvcMsgTable_Object = MibTable
alpsSvcMsgTable = _AlpsSvcMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alpsSvcMsgTable.setStatus("current")
_AlpsSvcMsgEntry_Object = MibTableRow
alpsSvcMsgEntry = _AlpsSvcMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 1, 1)
)
alpsSvcMsgEntry.setIndexNames(
    (0, "CISCO-ALPS-MIB", "alpsSvcMsgListNum"),
    (0, "CISCO-ALPS-MIB", "alpsSvcMsgNum"),
)
if mibBuilder.loadTexts:
    alpsSvcMsgEntry.setStatus("current")


class _AlpsSvcMsgListNum_Type(Integer32):
    """Custom type alpsSvcMsgListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlpsSvcMsgListNum_Type.__name__ = "Integer32"
_AlpsSvcMsgListNum_Object = MibTableColumn
alpsSvcMsgListNum = _AlpsSvcMsgListNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 1, 1, 1),
    _AlpsSvcMsgListNum_Type()
)
alpsSvcMsgListNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsSvcMsgListNum.setStatus("current")


class _AlpsSvcMsgNum_Type(Integer32):
    """Custom type alpsSvcMsgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlpsSvcMsgNum_Type.__name__ = "Integer32"
_AlpsSvcMsgNum_Object = MibTableColumn
alpsSvcMsgNum = _AlpsSvcMsgNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 1, 1, 2),
    _AlpsSvcMsgNum_Type()
)
alpsSvcMsgNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsSvcMsgNum.setStatus("current")


class _AlpsSvcMsg_Type(DisplayString):
    """Custom type alpsSvcMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AlpsSvcMsg_Type.__name__ = "DisplayString"
_AlpsSvcMsg_Object = MibTableColumn
alpsSvcMsg = _AlpsSvcMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 1, 1, 3),
    _AlpsSvcMsg_Type()
)
alpsSvcMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsSvcMsg.setStatus("current")
_AlpsSvcMsgRowStatus_Type = RowStatus
_AlpsSvcMsgRowStatus_Object = MibTableColumn
alpsSvcMsgRowStatus = _AlpsSvcMsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 1, 1, 4),
    _AlpsSvcMsgRowStatus_Type()
)
alpsSvcMsgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsSvcMsgRowStatus.setStatus("current")
_AlpsX121ToIpTransTable_Object = MibTable
alpsX121ToIpTransTable = _AlpsX121ToIpTransTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 2)
)
if mibBuilder.loadTexts:
    alpsX121ToIpTransTable.setStatus("current")
_AlpsX121ToIpTransEntry_Object = MibTableRow
alpsX121ToIpTransEntry = _AlpsX121ToIpTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 2, 1)
)
alpsX121ToIpTransEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ALPS-MIB", "alpsX121"),
)
if mibBuilder.loadTexts:
    alpsX121ToIpTransEntry.setStatus("current")
_AlpsX121_Type = X121Address
_AlpsX121_Object = MibTableColumn
alpsX121 = _AlpsX121_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 2, 1, 1),
    _AlpsX121_Type()
)
alpsX121.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alpsX121.setStatus("current")
_AlpsIpAddress_Type = IpAddress
_AlpsIpAddress_Object = MibTableColumn
alpsIpAddress = _AlpsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 2, 1, 2),
    _AlpsIpAddress_Type()
)
alpsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsIpAddress.setStatus("current")
_AlpsX121ToIpTransRowStatus_Type = RowStatus
_AlpsX121ToIpTransRowStatus_Object = MibTableColumn
alpsX121ToIpTransRowStatus = _AlpsX121ToIpTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 1, 6, 2, 1, 3),
    _AlpsX121ToIpTransRowStatus_Type()
)
alpsX121ToIpTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alpsX121ToIpTransRowStatus.setStatus("current")
_CiscoAlpsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoAlpsMIBNotificationPrefix = _CiscoAlpsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 2)
)
_CiscoAlpsMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoAlpsMIBNotifications = _CiscoAlpsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 2, 0)
)
_AlpsMibConformance_ObjectIdentity = ObjectIdentity
alpsMibConformance = _AlpsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3)
)
_AlpsMibCompliances_ObjectIdentity = ObjectIdentity
alpsMibCompliances = _AlpsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 1)
)
_AlpsMibGroups_ObjectIdentity = ObjectIdentity
alpsMibGroups = _AlpsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2)
)

# Managed Objects groups

alpsPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 1)
)
alpsPeerGroup.setObjects(
      *(("CISCO-ALPS-MIB", "alpsPeerLocalIpAddr"),
        ("CISCO-ALPS-MIB", "alpsPeerLocalAtpPort"),
        ("CISCO-ALPS-MIB", "alpsPeerKeepaliveTimeout"),
        ("CISCO-ALPS-MIB", "alpsPeerKeepaliveMaxRetries"),
        ("CISCO-ALPS-MIB", "alpsPeerInCallsAcceptFlag"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnType"),
        ("CISCO-ALPS-MIB", "alpsRemPeerLocalPort"),
        ("CISCO-ALPS-MIB", "alpsRemPeerRemotePort"),
        ("CISCO-ALPS-MIB", "alpsRemPeerState"),
        ("CISCO-ALPS-MIB", "alpsRemPeerUptime"),
        ("CISCO-ALPS-MIB", "alpsRemPeerNumActiveCkts"),
        ("CISCO-ALPS-MIB", "alpsRemPeerIdleTimer"),
        ("CISCO-ALPS-MIB", "alpsRemPeerAlarmsEnabled"),
        ("CISCO-ALPS-MIB", "alpsRemPeerTCPQlen"),
        ("CISCO-ALPS-MIB", "alpsRemPeerOutPackets"),
        ("CISCO-ALPS-MIB", "alpsRemPeerOutOctets"),
        ("CISCO-ALPS-MIB", "alpsRemPeerInPackets"),
        ("CISCO-ALPS-MIB", "alpsRemPeerInOctets"),
        ("CISCO-ALPS-MIB", "alpsRemPeerDropsGiant"),
        ("CISCO-ALPS-MIB", "alpsRemPeerDropsQFull"),
        ("CISCO-ALPS-MIB", "alpsRemPeerDropsPeerUnreach"),
        ("CISCO-ALPS-MIB", "alpsRemPeerRowStatus"))
)
if mibBuilder.loadTexts:
    alpsPeerGroup.setStatus("deprecated")

alpsCktGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 2)
)
alpsCktGroup.setObjects(
      *(("CISCO-ALPS-MIB", "alpsCktBasePriPeerAddr"),
        ("CISCO-ALPS-MIB", "alpsCktBaseAlarmsEnabled"),
        ("CISCO-ALPS-MIB", "alpsCktBaseConnType"),
        ("CISCO-ALPS-MIB", "alpsCktBaseState"),
        ("CISCO-ALPS-MIB", "alpsCktBaseNumActiveAscus"),
        ("CISCO-ALPS-MIB", "alpsCktBaseCurrentPeer"),
        ("CISCO-ALPS-MIB", "alpsCktBaseLifeTimeTimer"),
        ("CISCO-ALPS-MIB", "alpsCktBaseHostLinkNumber"),
        ("CISCO-ALPS-MIB", "alpsCktBaseHostLinkType"),
        ("CISCO-ALPS-MIB", "alpsCktBaseRemHld"),
        ("CISCO-ALPS-MIB", "alpsCktBaseLocalHld"),
        ("CISCO-ALPS-MIB", "alpsCktBaseDownReason"),
        ("CISCO-ALPS-MIB", "alpsCktBaseOutPackets"),
        ("CISCO-ALPS-MIB", "alpsCktBaseOutOctets"),
        ("CISCO-ALPS-MIB", "alpsCktBaseInPackets"),
        ("CISCO-ALPS-MIB", "alpsCktBaseInOctets"),
        ("CISCO-ALPS-MIB", "alpsCktBaseDropsCktDisabled"),
        ("CISCO-ALPS-MIB", "alpsCktBaseDropsQOverflow"),
        ("CISCO-ALPS-MIB", "alpsCktBaseDropsLifeTimeExpd"),
        ("CISCO-ALPS-MIB", "alpsCktBaseEnabled"),
        ("CISCO-ALPS-MIB", "alpsCktBaseRowStatus"),
        ("CISCO-ALPS-MIB", "alpsCktX25IfIndex"),
        ("CISCO-ALPS-MIB", "alpsCktX25LCN"),
        ("CISCO-ALPS-MIB", "alpsCktX25HostX121"),
        ("CISCO-ALPS-MIB", "alpsCktX25RemoteX121"),
        ("CISCO-ALPS-MIB", "alpsCktX25DropsVcReset"),
        ("CISCO-ALPS-MIB", "alpsCktP1024BackupPeerAddr"),
        ("CISCO-ALPS-MIB", "alpsCktP1024RetryTimer"),
        ("CISCO-ALPS-MIB", "alpsCktP1024IdleTimer"),
        ("CISCO-ALPS-MIB", "alpsCktP1024EmtoxX121"),
        ("CISCO-ALPS-MIB", "alpsCktP1024Ax25LCN"),
        ("CISCO-ALPS-MIB", "alpsCktP1024WinOut"),
        ("CISCO-ALPS-MIB", "alpsCktP1024WinIn"),
        ("CISCO-ALPS-MIB", "alpsCktP1024OutPktSize"),
        ("CISCO-ALPS-MIB", "alpsCktP1024InPktSize"),
        ("CISCO-ALPS-MIB", "alpsCktP1024SvcMsgList"),
        ("CISCO-ALPS-MIB", "alpsCktP1024SvcMsgIntvl"),
        ("CISCO-ALPS-MIB", "alpsCktP1024DropsUnkAscu"),
        ("CISCO-ALPS-MIB", "alpsCktP1024RowStatus"),
        ("CISCO-ALPS-MIB", "alpsCktAscuIfIndex"),
        ("CISCO-ALPS-MIB", "alpsCktAscuId"),
        ("CISCO-ALPS-MIB", "alpsCktAscuStatus"),
        ("CISCO-ALPS-MIB", "alpsCktBaseCurrPeerConnId"),
        ("CISCO-ALPS-MIB", "alpsCktP1024MatipCloseDelay"))
)
if mibBuilder.loadTexts:
    alpsCktGroup.setStatus("current")

alpsIfP1024Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 3)
)
alpsIfP1024Group.setObjects(
      *(("CISCO-ALPS-MIB", "alpsIfP1024EncapType"),
        ("CISCO-ALPS-MIB", "alpsIfP1024PollRespTimeout"),
        ("CISCO-ALPS-MIB", "alpsIfP1024GATimeout"),
        ("CISCO-ALPS-MIB", "alpsIfP1024PollPauseTimeout"),
        ("CISCO-ALPS-MIB", "alpsIfP1024MaxErrCnt"),
        ("CISCO-ALPS-MIB", "alpsIfP1024MaxRetrans"),
        ("CISCO-ALPS-MIB", "alpsIfP1024CurrErrCnt"),
        ("CISCO-ALPS-MIB", "alpsIfP1024MinGoodPollResp"),
        ("CISCO-ALPS-MIB", "alpsIfP1024PollingRatio"),
        ("CISCO-ALPS-MIB", "alpsIfP1024NumAscus"))
)
if mibBuilder.loadTexts:
    alpsIfP1024Group.setStatus("deprecated")

alpsIfHostlinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 4)
)
alpsIfHostlinkGroup.setObjects(
      *(("CISCO-ALPS-MIB", "alpsIfHLinkX25ProtocolType"),
        ("CISCO-ALPS-MIB", "alpsIfHLinkAx25PvcDamp"),
        ("CISCO-ALPS-MIB", "alpsIfHLinkEmtoxHostX121"),
        ("CISCO-ALPS-MIB", "alpsIfHLinkActiveCkts"))
)
if mibBuilder.loadTexts:
    alpsIfHostlinkGroup.setStatus("current")

alpsAscuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 5)
)
alpsAscuGroup.setObjects(
      *(("CISCO-ALPS-MIB", "alpsAscuA1"),
        ("CISCO-ALPS-MIB", "alpsAscuA2"),
        ("CISCO-ALPS-MIB", "alpsAscuCktName"),
        ("CISCO-ALPS-MIB", "alpsAscuAlarmsEnabled"),
        ("CISCO-ALPS-MIB", "alpsAscuRetryOption"),
        ("CISCO-ALPS-MIB", "alpsAscuMaxMsgLength"),
        ("CISCO-ALPS-MIB", "alpsAscuFwdStatusOption"),
        ("CISCO-ALPS-MIB", "alpsAscuState"),
        ("CISCO-ALPS-MIB", "alpsAscuDownReason"),
        ("CISCO-ALPS-MIB", "alpsAscuOutPackets"),
        ("CISCO-ALPS-MIB", "alpsAscuOutOctets"),
        ("CISCO-ALPS-MIB", "alpsAscuInPackets"),
        ("CISCO-ALPS-MIB", "alpsAscuInOctets"),
        ("CISCO-ALPS-MIB", "alpsAscuDropsGarbledPkts"),
        ("CISCO-ALPS-MIB", "alpsAscuDropsAscuDown"),
        ("CISCO-ALPS-MIB", "alpsAscuDropsAscuDisabled"),
        ("CISCO-ALPS-MIB", "alpsAscuEnabled"),
        ("CISCO-ALPS-MIB", "alpsAscuRowStatus"))
)
if mibBuilder.loadTexts:
    alpsAscuGroup.setStatus("deprecated")

alpsSvcMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 6)
)
alpsSvcMsgGroup.setObjects(
      *(("CISCO-ALPS-MIB", "alpsSvcMsg"),
        ("CISCO-ALPS-MIB", "alpsSvcMsgRowStatus"))
)
if mibBuilder.loadTexts:
    alpsSvcMsgGroup.setStatus("current")

alpsAddrTransGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 7)
)
alpsAddrTransGroup.setObjects(
      *(("CISCO-ALPS-MIB", "alpsIpAddress"),
        ("CISCO-ALPS-MIB", "alpsX121ToIpTransRowStatus"))
)
if mibBuilder.loadTexts:
    alpsAddrTransGroup.setStatus("current")

alpsPeerGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 9)
)
alpsPeerGroupRev1.setObjects(
      *(("CISCO-ALPS-MIB", "alpsPeerLocalIpAddr"),
        ("CISCO-ALPS-MIB", "alpsPeerLocalAtpPort"),
        ("CISCO-ALPS-MIB", "alpsPeerKeepaliveTimeout"),
        ("CISCO-ALPS-MIB", "alpsPeerKeepaliveMaxRetries"),
        ("CISCO-ALPS-MIB", "alpsPeerInCallsAcceptFlag"),
        ("CISCO-ALPS-MIB", "alpsRemPeerCfgActivation"),
        ("CISCO-ALPS-MIB", "alpsRemPeerCfgTCPQLen"),
        ("CISCO-ALPS-MIB", "alpsRemPeerCfgIdleTimer"),
        ("CISCO-ALPS-MIB", "alpsRemPeerCfgNoCircTimer"),
        ("CISCO-ALPS-MIB", "alpsRemPeerCfgAlarmsOn"),
        ("CISCO-ALPS-MIB", "alpsRemPeerCfgStatIntvl"),
        ("CISCO-ALPS-MIB", "alpsRemPeerCfgStatRetry"),
        ("CISCO-ALPS-MIB", "alpsRemPeerCfgRowStatus"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnLocalPort"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnForeignPort"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnState"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnProtocol"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnCreation"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnActivation"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnUptime"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnNumActCirc"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnLastTxRx"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnLastRxAny"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnIdleTimer"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnNoCircTimer"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnTCPQLen"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnAlarmsOn"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnStatIntvl"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnStatRetry"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnDownReason"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnOutPackets"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnOutOctets"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnInPackets"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnInOctets"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnDropsGiant"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnDropsQFull"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnDropsUnreach"),
        ("CISCO-ALPS-MIB", "alpsRemPeerConnDropsVersion"))
)
if mibBuilder.loadTexts:
    alpsPeerGroupRev1.setStatus("current")

alpsIfP1024GroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 11)
)
alpsIfP1024GroupRev1.setObjects(
      *(("CISCO-ALPS-MIB", "alpsIfP1024EncapType"),
        ("CISCO-ALPS-MIB", "alpsIfP1024PollRespTimeout"),
        ("CISCO-ALPS-MIB", "alpsIfP1024GATimeout"),
        ("CISCO-ALPS-MIB", "alpsIfP1024PollPauseTimeout"),
        ("CISCO-ALPS-MIB", "alpsIfP1024MaxErrCnt"),
        ("CISCO-ALPS-MIB", "alpsIfP1024MaxRetrans"),
        ("CISCO-ALPS-MIB", "alpsIfP1024CurrErrCnt"),
        ("CISCO-ALPS-MIB", "alpsIfP1024MinGoodPollResp"),
        ("CISCO-ALPS-MIB", "alpsIfP1024PollingRatio"),
        ("CISCO-ALPS-MIB", "alpsIfP1024NumAscus"),
        ("CISCO-ALPS-MIB", "alpsIfP1024ServMsgFormat"),
        ("CISCO-ALPS-MIB", "alpsIfP1024ServMsgStatusChange"),
        ("CISCO-ALPS-MIB", "alpsIfP1024ServMsgDropTermAddr"))
)
if mibBuilder.loadTexts:
    alpsIfP1024GroupRev1.setStatus("current")

alpsAscuGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 12)
)
alpsAscuGroupRev1.setObjects(
      *(("CISCO-ALPS-MIB", "alpsAscuA1"),
        ("CISCO-ALPS-MIB", "alpsAscuA2"),
        ("CISCO-ALPS-MIB", "alpsAscuCktName"),
        ("CISCO-ALPS-MIB", "alpsAscuAlarmsEnabled"),
        ("CISCO-ALPS-MIB", "alpsAscuRetryOption"),
        ("CISCO-ALPS-MIB", "alpsAscuMaxMsgLength"),
        ("CISCO-ALPS-MIB", "alpsAscuFwdStatusOption"),
        ("CISCO-ALPS-MIB", "alpsAscuState"),
        ("CISCO-ALPS-MIB", "alpsAscuDownReason"),
        ("CISCO-ALPS-MIB", "alpsAscuOutPackets"),
        ("CISCO-ALPS-MIB", "alpsAscuOutOctets"),
        ("CISCO-ALPS-MIB", "alpsAscuInPackets"),
        ("CISCO-ALPS-MIB", "alpsAscuInOctets"),
        ("CISCO-ALPS-MIB", "alpsAscuDropsGarbledPkts"),
        ("CISCO-ALPS-MIB", "alpsAscuDropsAscuDown"),
        ("CISCO-ALPS-MIB", "alpsAscuDropsAscuDisabled"),
        ("CISCO-ALPS-MIB", "alpsAscuEnabled"),
        ("CISCO-ALPS-MIB", "alpsAscuRowStatus"),
        ("CISCO-ALPS-MIB", "alpsAscuAutoReset"))
)
if mibBuilder.loadTexts:
    alpsAscuGroupRev1.setStatus("current")


# Notification objects

alpsPeerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 2, 0, 1)
)
alpsPeerStatusChange.setObjects(
    ("CISCO-ALPS-MIB", "alpsRemPeerState")
)
if mibBuilder.loadTexts:
    alpsPeerStatusChange.setStatus(
        "deprecated"
    )

alpsCktStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 2, 0, 2)
)
alpsCktStatusChange.setObjects(
    ("CISCO-ALPS-MIB", "alpsCktBaseState")
)
if mibBuilder.loadTexts:
    alpsCktStatusChange.setStatus(
        "current"
    )

alpsAscuStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 2, 0, 3)
)
alpsAscuStatusChange.setObjects(
    ("CISCO-ALPS-MIB", "alpsAscuState")
)
if mibBuilder.loadTexts:
    alpsAscuStatusChange.setStatus(
        "current"
    )

alpsPeerConnStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 2, 0, 4)
)
alpsPeerConnStatusChange.setObjects(
    ("CISCO-ALPS-MIB", "alpsRemPeerConnState")
)
if mibBuilder.loadTexts:
    alpsPeerConnStatusChange.setStatus(
        "current"
    )

alpsCktOpenFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 2, 0, 5)
)
alpsCktOpenFailure.setObjects(
    ("CISCO-ALPS-MIB", "alpsCktBaseDownReason")
)
if mibBuilder.loadTexts:
    alpsCktOpenFailure.setStatus(
        "current"
    )

alpsCktPartialReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 2, 0, 6)
)
alpsCktPartialReject.setObjects(
      *(("CISCO-ALPS-MIB", "alpsCktAscuIfIndex"),
        ("CISCO-ALPS-MIB", "alpsCktAscuId"))
)
if mibBuilder.loadTexts:
    alpsCktPartialReject.setStatus(
        "current"
    )


# Notifications groups

alpsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 8)
)
alpsNotificationGroup.setObjects(
      *(("CISCO-ALPS-MIB", "alpsPeerStatusChange"),
        ("CISCO-ALPS-MIB", "alpsCktStatusChange"),
        ("CISCO-ALPS-MIB", "alpsAscuStatusChange"))
)
if mibBuilder.loadTexts:
    alpsNotificationGroup.setStatus(
        "obsolete"
    )

alpsNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 10)
)
alpsNotificationGroupRev1.setObjects(
      *(("CISCO-ALPS-MIB", "alpsCktStatusChange"),
        ("CISCO-ALPS-MIB", "alpsAscuStatusChange"),
        ("CISCO-ALPS-MIB", "alpsPeerConnStatusChange"))
)
if mibBuilder.loadTexts:
    alpsNotificationGroupRev1.setStatus(
        "deprecated"
    )

alpsNotificationGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 2, 13)
)
alpsNotificationGroupRev2.setObjects(
      *(("CISCO-ALPS-MIB", "alpsCktStatusChange"),
        ("CISCO-ALPS-MIB", "alpsAscuStatusChange"),
        ("CISCO-ALPS-MIB", "alpsPeerConnStatusChange"),
        ("CISCO-ALPS-MIB", "alpsCktOpenFailure"),
        ("CISCO-ALPS-MIB", "alpsCktPartialReject"))
)
if mibBuilder.loadTexts:
    alpsNotificationGroupRev2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alpsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alpsMibCompliance.setStatus(
        "deprecated"
    )

alpsMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alpsMibComplianceRev1.setStatus(
        "deprecated"
    )

alpsMibComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 95, 3, 1, 3)
)
if mibBuilder.loadTexts:
    alpsMibComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ALPS-MIB",
    **{"AlpsCktName": AlpsCktName,
       "AlpsAscuA1A2Value": AlpsAscuA1A2Value,
       "ciscoAlpsMIB": ciscoAlpsMIB,
       "ciscoAlpsMIBObjects": ciscoAlpsMIBObjects,
       "alpsGroups": alpsGroups,
       "alpsPeerObjects": alpsPeerObjects,
       "alpsPeer": alpsPeer,
       "alpsPeerLocalIpAddr": alpsPeerLocalIpAddr,
       "alpsPeerLocalAtpPort": alpsPeerLocalAtpPort,
       "alpsPeerKeepaliveTimeout": alpsPeerKeepaliveTimeout,
       "alpsPeerKeepaliveMaxRetries": alpsPeerKeepaliveMaxRetries,
       "alpsPeerInCallsAcceptFlag": alpsPeerInCallsAcceptFlag,
       "alpsRemPeerTable": alpsRemPeerTable,
       "alpsRemPeerEntry": alpsRemPeerEntry,
       "alpsRemPeerIpAddr": alpsRemPeerIpAddr,
       "alpsRemPeerConnType": alpsRemPeerConnType,
       "alpsRemPeerLocalPort": alpsRemPeerLocalPort,
       "alpsRemPeerRemotePort": alpsRemPeerRemotePort,
       "alpsRemPeerState": alpsRemPeerState,
       "alpsRemPeerUptime": alpsRemPeerUptime,
       "alpsRemPeerNumActiveCkts": alpsRemPeerNumActiveCkts,
       "alpsRemPeerIdleTimer": alpsRemPeerIdleTimer,
       "alpsRemPeerAlarmsEnabled": alpsRemPeerAlarmsEnabled,
       "alpsRemPeerTCPQlen": alpsRemPeerTCPQlen,
       "alpsRemPeerOutPackets": alpsRemPeerOutPackets,
       "alpsRemPeerOutOctets": alpsRemPeerOutOctets,
       "alpsRemPeerInPackets": alpsRemPeerInPackets,
       "alpsRemPeerInOctets": alpsRemPeerInOctets,
       "alpsRemPeerDropsGiant": alpsRemPeerDropsGiant,
       "alpsRemPeerDropsQFull": alpsRemPeerDropsQFull,
       "alpsRemPeerDropsPeerUnreach": alpsRemPeerDropsPeerUnreach,
       "alpsRemPeerRowStatus": alpsRemPeerRowStatus,
       "alpsRemPeerCfgTable": alpsRemPeerCfgTable,
       "alpsRemPeerCfgEntry": alpsRemPeerCfgEntry,
       "alpsRemPeerCfgIpAddr": alpsRemPeerCfgIpAddr,
       "alpsRemPeerCfgProtocol": alpsRemPeerCfgProtocol,
       "alpsRemPeerCfgActivation": alpsRemPeerCfgActivation,
       "alpsRemPeerCfgTCPQLen": alpsRemPeerCfgTCPQLen,
       "alpsRemPeerCfgIdleTimer": alpsRemPeerCfgIdleTimer,
       "alpsRemPeerCfgNoCircTimer": alpsRemPeerCfgNoCircTimer,
       "alpsRemPeerCfgAlarmsOn": alpsRemPeerCfgAlarmsOn,
       "alpsRemPeerCfgStatIntvl": alpsRemPeerCfgStatIntvl,
       "alpsRemPeerCfgStatRetry": alpsRemPeerCfgStatRetry,
       "alpsRemPeerCfgRowStatus": alpsRemPeerCfgRowStatus,
       "alpsRemPeerConnTable": alpsRemPeerConnTable,
       "alpsRemPeerConnEntry": alpsRemPeerConnEntry,
       "alpsRemPeerConnIpAddr": alpsRemPeerConnIpAddr,
       "alpsRemPeerConnIdString": alpsRemPeerConnIdString,
       "alpsRemPeerConnLocalPort": alpsRemPeerConnLocalPort,
       "alpsRemPeerConnForeignPort": alpsRemPeerConnForeignPort,
       "alpsRemPeerConnState": alpsRemPeerConnState,
       "alpsRemPeerConnProtocol": alpsRemPeerConnProtocol,
       "alpsRemPeerConnCreation": alpsRemPeerConnCreation,
       "alpsRemPeerConnActivation": alpsRemPeerConnActivation,
       "alpsRemPeerConnUptime": alpsRemPeerConnUptime,
       "alpsRemPeerConnNumActCirc": alpsRemPeerConnNumActCirc,
       "alpsRemPeerConnLastTxRx": alpsRemPeerConnLastTxRx,
       "alpsRemPeerConnLastRxAny": alpsRemPeerConnLastRxAny,
       "alpsRemPeerConnIdleTimer": alpsRemPeerConnIdleTimer,
       "alpsRemPeerConnNoCircTimer": alpsRemPeerConnNoCircTimer,
       "alpsRemPeerConnTCPQLen": alpsRemPeerConnTCPQLen,
       "alpsRemPeerConnAlarmsOn": alpsRemPeerConnAlarmsOn,
       "alpsRemPeerConnStatIntvl": alpsRemPeerConnStatIntvl,
       "alpsRemPeerConnStatRetry": alpsRemPeerConnStatRetry,
       "alpsRemPeerConnDownReason": alpsRemPeerConnDownReason,
       "alpsRemPeerConnOutPackets": alpsRemPeerConnOutPackets,
       "alpsRemPeerConnOutOctets": alpsRemPeerConnOutOctets,
       "alpsRemPeerConnInPackets": alpsRemPeerConnInPackets,
       "alpsRemPeerConnInOctets": alpsRemPeerConnInOctets,
       "alpsRemPeerConnDropsGiant": alpsRemPeerConnDropsGiant,
       "alpsRemPeerConnDropsQFull": alpsRemPeerConnDropsQFull,
       "alpsRemPeerConnDropsUnreach": alpsRemPeerConnDropsUnreach,
       "alpsRemPeerConnDropsVersion": alpsRemPeerConnDropsVersion,
       "alpsCktObjects": alpsCktObjects,
       "alpsCktBaseTable": alpsCktBaseTable,
       "alpsCktBaseEntry": alpsCktBaseEntry,
       "alpsCktBaseName": alpsCktBaseName,
       "alpsCktBaseDlcType": alpsCktBaseDlcType,
       "alpsCktBasePriPeerAddr": alpsCktBasePriPeerAddr,
       "alpsCktBaseAlarmsEnabled": alpsCktBaseAlarmsEnabled,
       "alpsCktBaseConnType": alpsCktBaseConnType,
       "alpsCktBaseState": alpsCktBaseState,
       "alpsCktBaseNumActiveAscus": alpsCktBaseNumActiveAscus,
       "alpsCktBaseCurrentPeer": alpsCktBaseCurrentPeer,
       "alpsCktBaseLifeTimeTimer": alpsCktBaseLifeTimeTimer,
       "alpsCktBaseHostLinkNumber": alpsCktBaseHostLinkNumber,
       "alpsCktBaseHostLinkType": alpsCktBaseHostLinkType,
       "alpsCktBaseRemHld": alpsCktBaseRemHld,
       "alpsCktBaseLocalHld": alpsCktBaseLocalHld,
       "alpsCktBaseDownReason": alpsCktBaseDownReason,
       "alpsCktBaseOutPackets": alpsCktBaseOutPackets,
       "alpsCktBaseOutOctets": alpsCktBaseOutOctets,
       "alpsCktBaseInPackets": alpsCktBaseInPackets,
       "alpsCktBaseInOctets": alpsCktBaseInOctets,
       "alpsCktBaseDropsCktDisabled": alpsCktBaseDropsCktDisabled,
       "alpsCktBaseDropsQOverflow": alpsCktBaseDropsQOverflow,
       "alpsCktBaseDropsLifeTimeExpd": alpsCktBaseDropsLifeTimeExpd,
       "alpsCktBaseEnabled": alpsCktBaseEnabled,
       "alpsCktBaseRowStatus": alpsCktBaseRowStatus,
       "alpsCktBaseCurrPeerConnId": alpsCktBaseCurrPeerConnId,
       "alpsCktX25Table": alpsCktX25Table,
       "alpsCktX25Entry": alpsCktX25Entry,
       "alpsCktX25DlcType": alpsCktX25DlcType,
       "alpsCktX25IfIndex": alpsCktX25IfIndex,
       "alpsCktX25LCN": alpsCktX25LCN,
       "alpsCktX25HostX121": alpsCktX25HostX121,
       "alpsCktX25RemoteX121": alpsCktX25RemoteX121,
       "alpsCktX25DropsVcReset": alpsCktX25DropsVcReset,
       "alpsCktP1024Table": alpsCktP1024Table,
       "alpsCktP1024Entry": alpsCktP1024Entry,
       "alpsCktP1024DlcType": alpsCktP1024DlcType,
       "alpsCktP1024BackupPeerAddr": alpsCktP1024BackupPeerAddr,
       "alpsCktP1024RetryTimer": alpsCktP1024RetryTimer,
       "alpsCktP1024IdleTimer": alpsCktP1024IdleTimer,
       "alpsCktP1024EmtoxX121": alpsCktP1024EmtoxX121,
       "alpsCktP1024Ax25LCN": alpsCktP1024Ax25LCN,
       "alpsCktP1024WinOut": alpsCktP1024WinOut,
       "alpsCktP1024WinIn": alpsCktP1024WinIn,
       "alpsCktP1024OutPktSize": alpsCktP1024OutPktSize,
       "alpsCktP1024InPktSize": alpsCktP1024InPktSize,
       "alpsCktP1024SvcMsgList": alpsCktP1024SvcMsgList,
       "alpsCktP1024SvcMsgIntvl": alpsCktP1024SvcMsgIntvl,
       "alpsCktP1024DropsUnkAscu": alpsCktP1024DropsUnkAscu,
       "alpsCktP1024RowStatus": alpsCktP1024RowStatus,
       "alpsCktP1024MatipCloseDelay": alpsCktP1024MatipCloseDelay,
       "alpsCktAscuTable": alpsCktAscuTable,
       "alpsCktAscuEntry": alpsCktAscuEntry,
       "alpsCktAscuCktName": alpsCktAscuCktName,
       "alpsCktAscuCktDlcType": alpsCktAscuCktDlcType,
       "alpsCktAscuA1": alpsCktAscuA1,
       "alpsCktAscuA2": alpsCktAscuA2,
       "alpsCktAscuIfIndex": alpsCktAscuIfIndex,
       "alpsCktAscuId": alpsCktAscuId,
       "alpsCktAscuStatus": alpsCktAscuStatus,
       "alpsIfObjects": alpsIfObjects,
       "alpsIfP1024Table": alpsIfP1024Table,
       "alpsIfP1024Entry": alpsIfP1024Entry,
       "alpsIfP1024EncapType": alpsIfP1024EncapType,
       "alpsIfP1024PollRespTimeout": alpsIfP1024PollRespTimeout,
       "alpsIfP1024GATimeout": alpsIfP1024GATimeout,
       "alpsIfP1024PollPauseTimeout": alpsIfP1024PollPauseTimeout,
       "alpsIfP1024MaxErrCnt": alpsIfP1024MaxErrCnt,
       "alpsIfP1024MaxRetrans": alpsIfP1024MaxRetrans,
       "alpsIfP1024CurrErrCnt": alpsIfP1024CurrErrCnt,
       "alpsIfP1024MinGoodPollResp": alpsIfP1024MinGoodPollResp,
       "alpsIfP1024PollingRatio": alpsIfP1024PollingRatio,
       "alpsIfP1024NumAscus": alpsIfP1024NumAscus,
       "alpsIfP1024ServMsgFormat": alpsIfP1024ServMsgFormat,
       "alpsIfP1024ServMsgStatusChange": alpsIfP1024ServMsgStatusChange,
       "alpsIfP1024ServMsgDropTermAddr": alpsIfP1024ServMsgDropTermAddr,
       "alpsIfHLinkTable": alpsIfHLinkTable,
       "alpsIfHLinkEntry": alpsIfHLinkEntry,
       "alpsIfHLinkHostHld": alpsIfHLinkHostHld,
       "alpsIfHLinkNumber": alpsIfHLinkNumber,
       "alpsIfHLinkX25ProtocolType": alpsIfHLinkX25ProtocolType,
       "alpsIfHLinkAx25PvcDamp": alpsIfHLinkAx25PvcDamp,
       "alpsIfHLinkEmtoxHostX121": alpsIfHLinkEmtoxHostX121,
       "alpsIfHLinkActiveCkts": alpsIfHLinkActiveCkts,
       "alpsAscuObjects": alpsAscuObjects,
       "alpsAscuTable": alpsAscuTable,
       "alpsAscuEntry": alpsAscuEntry,
       "alpsAscuId": alpsAscuId,
       "alpsAscuA1": alpsAscuA1,
       "alpsAscuA2": alpsAscuA2,
       "alpsAscuCktName": alpsAscuCktName,
       "alpsAscuAlarmsEnabled": alpsAscuAlarmsEnabled,
       "alpsAscuRetryOption": alpsAscuRetryOption,
       "alpsAscuMaxMsgLength": alpsAscuMaxMsgLength,
       "alpsAscuFwdStatusOption": alpsAscuFwdStatusOption,
       "alpsAscuState": alpsAscuState,
       "alpsAscuDownReason": alpsAscuDownReason,
       "alpsAscuOutPackets": alpsAscuOutPackets,
       "alpsAscuOutOctets": alpsAscuOutOctets,
       "alpsAscuInPackets": alpsAscuInPackets,
       "alpsAscuInOctets": alpsAscuInOctets,
       "alpsAscuDropsGarbledPkts": alpsAscuDropsGarbledPkts,
       "alpsAscuDropsAscuDown": alpsAscuDropsAscuDown,
       "alpsAscuDropsAscuDisabled": alpsAscuDropsAscuDisabled,
       "alpsAscuEnabled": alpsAscuEnabled,
       "alpsAscuRowStatus": alpsAscuRowStatus,
       "alpsAscuAutoReset": alpsAscuAutoReset,
       "alpsGlobalObjects": alpsGlobalObjects,
       "alpsSvcMsgTable": alpsSvcMsgTable,
       "alpsSvcMsgEntry": alpsSvcMsgEntry,
       "alpsSvcMsgListNum": alpsSvcMsgListNum,
       "alpsSvcMsgNum": alpsSvcMsgNum,
       "alpsSvcMsg": alpsSvcMsg,
       "alpsSvcMsgRowStatus": alpsSvcMsgRowStatus,
       "alpsX121ToIpTransTable": alpsX121ToIpTransTable,
       "alpsX121ToIpTransEntry": alpsX121ToIpTransEntry,
       "alpsX121": alpsX121,
       "alpsIpAddress": alpsIpAddress,
       "alpsX121ToIpTransRowStatus": alpsX121ToIpTransRowStatus,
       "ciscoAlpsMIBNotificationPrefix": ciscoAlpsMIBNotificationPrefix,
       "ciscoAlpsMIBNotifications": ciscoAlpsMIBNotifications,
       "alpsPeerStatusChange": alpsPeerStatusChange,
       "alpsCktStatusChange": alpsCktStatusChange,
       "alpsAscuStatusChange": alpsAscuStatusChange,
       "alpsPeerConnStatusChange": alpsPeerConnStatusChange,
       "alpsCktOpenFailure": alpsCktOpenFailure,
       "alpsCktPartialReject": alpsCktPartialReject,
       "alpsMibConformance": alpsMibConformance,
       "alpsMibCompliances": alpsMibCompliances,
       "alpsMibCompliance": alpsMibCompliance,
       "alpsMibComplianceRev1": alpsMibComplianceRev1,
       "alpsMibComplianceRev2": alpsMibComplianceRev2,
       "alpsMibGroups": alpsMibGroups,
       "alpsPeerGroup": alpsPeerGroup,
       "alpsCktGroup": alpsCktGroup,
       "alpsIfP1024Group": alpsIfP1024Group,
       "alpsIfHostlinkGroup": alpsIfHostlinkGroup,
       "alpsAscuGroup": alpsAscuGroup,
       "alpsSvcMsgGroup": alpsSvcMsgGroup,
       "alpsAddrTransGroup": alpsAddrTransGroup,
       "alpsNotificationGroup": alpsNotificationGroup,
       "alpsPeerGroupRev1": alpsPeerGroupRev1,
       "alpsNotificationGroupRev1": alpsNotificationGroupRev1,
       "alpsIfP1024GroupRev1": alpsIfP1024GroupRev1,
       "alpsAscuGroupRev1": alpsAscuGroupRev1,
       "alpsNotificationGroupRev2": alpsNotificationGroupRev2}
)
