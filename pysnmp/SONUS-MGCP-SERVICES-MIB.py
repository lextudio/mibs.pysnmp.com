# SNMP MIB module (SONUS-MGCP-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-MGCP-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:03 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")

(SonusAdminState,
 SonusBoolean,
 SonusName,
 SonusNameReference,
 SonusServiceState,
 SonusShelfIndex,
 SonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminState",
    "SonusBoolean",
    "SonusName",
    "SonusNameReference",
    "SonusServiceState",
    "SonusShelfIndex",
    "SonusSlotIndex")


# MODULE-IDENTITY

sonusMgcpServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusMgcpServicesMIBObjects_ObjectIdentity = ObjectIdentity
sonusMgcpServicesMIBObjects = _SonusMgcpServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1)
)
_SonusMgcpGateway_ObjectIdentity = ObjectIdentity
sonusMgcpGateway = _SonusMgcpGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 1)
)


class _SonusMgcpGatewayPort_Type(Integer32):
    """Custom type sonusMgcpGatewayPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusMgcpGatewayPort_Type.__name__ = "Integer32"
_SonusMgcpGatewayPort_Object = MibScalar
sonusMgcpGatewayPort = _SonusMgcpGatewayPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 1, 1),
    _SonusMgcpGatewayPort_Type()
)
sonusMgcpGatewayPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpGatewayPort.setStatus("current")


class _SonusMgcpGatewayRxThrottle_Type(Integer32):
    """Custom type sonusMgcpGatewayRxThrottle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusMgcpGatewayRxThrottle_Type.__name__ = "Integer32"
_SonusMgcpGatewayRxThrottle_Object = MibScalar
sonusMgcpGatewayRxThrottle = _SonusMgcpGatewayRxThrottle_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 1, 2),
    _SonusMgcpGatewayRxThrottle_Type()
)
sonusMgcpGatewayRxThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpGatewayRxThrottle.setStatus("current")


class _SonusMgcpGatewayMaxReXmit_Type(Integer32):
    """Custom type sonusMgcpGatewayMaxReXmit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_SonusMgcpGatewayMaxReXmit_Type.__name__ = "Integer32"
_SonusMgcpGatewayMaxReXmit_Object = MibScalar
sonusMgcpGatewayMaxReXmit = _SonusMgcpGatewayMaxReXmit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 1, 3),
    _SonusMgcpGatewayMaxReXmit_Type()
)
sonusMgcpGatewayMaxReXmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpGatewayMaxReXmit.setStatus("current")


class _SonusMgcpGatewayCmdTimeout_Type(Integer32):
    """Custom type sonusMgcpGatewayCmdTimeout based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SonusMgcpGatewayCmdTimeout_Type.__name__ = "Integer32"
_SonusMgcpGatewayCmdTimeout_Object = MibScalar
sonusMgcpGatewayCmdTimeout = _SonusMgcpGatewayCmdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 1, 4),
    _SonusMgcpGatewayCmdTimeout_Type()
)
sonusMgcpGatewayCmdTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpGatewayCmdTimeout.setStatus("current")


class _SonusMgcpGatewayRspTimeout_Type(Integer32):
    """Custom type sonusMgcpGatewayRspTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusMgcpGatewayRspTimeout_Type.__name__ = "Integer32"
_SonusMgcpGatewayRspTimeout_Object = MibScalar
sonusMgcpGatewayRspTimeout = _SonusMgcpGatewayRspTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 1, 5),
    _SonusMgcpGatewayRspTimeout_Type()
)
sonusMgcpGatewayRspTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpGatewayRspTimeout.setStatus("current")


class _SonusMgcpGatewayCriticalTimeout_Type(Integer32):
    """Custom type sonusMgcpGatewayCriticalTimeout based on Integer32"""
    defaultValue = 16000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 60000),
    )


_SonusMgcpGatewayCriticalTimeout_Type.__name__ = "Integer32"
_SonusMgcpGatewayCriticalTimeout_Object = MibScalar
sonusMgcpGatewayCriticalTimeout = _SonusMgcpGatewayCriticalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 1, 6),
    _SonusMgcpGatewayCriticalTimeout_Type()
)
sonusMgcpGatewayCriticalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpGatewayCriticalTimeout.setStatus("current")


class _SonusMgcpGatewayPartialTimeout_Type(Integer32):
    """Custom type sonusMgcpGatewayPartialTimeout based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 60000),
    )


_SonusMgcpGatewayPartialTimeout_Type.__name__ = "Integer32"
_SonusMgcpGatewayPartialTimeout_Object = MibScalar
sonusMgcpGatewayPartialTimeout = _SonusMgcpGatewayPartialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 1, 7),
    _SonusMgcpGatewayPartialTimeout_Type()
)
sonusMgcpGatewayPartialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpGatewayPartialTimeout.setStatus("current")


class _SonusMgcpGatewayMsgPiggyBacking_Type(SonusBoolean):
    """Custom type sonusMgcpGatewayMsgPiggyBacking based on SonusBoolean"""


_SonusMgcpGatewayMsgPiggyBacking_Object = MibScalar
sonusMgcpGatewayMsgPiggyBacking = _SonusMgcpGatewayMsgPiggyBacking_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 1, 8),
    _SonusMgcpGatewayMsgPiggyBacking_Type()
)
sonusMgcpGatewayMsgPiggyBacking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpGatewayMsgPiggyBacking.setStatus("current")
_SonusMgcpSession_ObjectIdentity = ObjectIdentity
sonusMgcpSession = _SonusMgcpSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2)
)
_SonusMgcpSessionNextIndex_Type = Integer32
_SonusMgcpSessionNextIndex_Object = MibScalar
sonusMgcpSessionNextIndex = _SonusMgcpSessionNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2, 1),
    _SonusMgcpSessionNextIndex_Type()
)
sonusMgcpSessionNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionNextIndex.setStatus("current")
_SonusMgcpSessionTable_Object = MibTable
sonusMgcpSessionTable = _SonusMgcpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusMgcpSessionTable.setStatus("current")
_SonusMgcpSessionEntry_Object = MibTableRow
sonusMgcpSessionEntry = _SonusMgcpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2, 2, 1)
)
sonusMgcpSessionEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusMgcpSessionIndex"),
)
if mibBuilder.loadTexts:
    sonusMgcpSessionEntry.setStatus("current")
_SonusMgcpSessionIndex_Type = Integer32
_SonusMgcpSessionIndex_Object = MibTableColumn
sonusMgcpSessionIndex = _SonusMgcpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2, 2, 1, 1),
    _SonusMgcpSessionIndex_Type()
)
sonusMgcpSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionIndex.setStatus("current")
_SonusMgcpSessionName_Type = SonusName
_SonusMgcpSessionName_Object = MibTableColumn
sonusMgcpSessionName = _SonusMgcpSessionName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2, 2, 1, 2),
    _SonusMgcpSessionName_Type()
)
sonusMgcpSessionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpSessionName.setStatus("current")


class _SonusMgcpSessionMode_Type(SonusServiceState):
    """Custom type sonusMgcpSessionMode based on SonusServiceState"""


_SonusMgcpSessionMode_Object = MibTableColumn
sonusMgcpSessionMode = _SonusMgcpSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2, 2, 1, 3),
    _SonusMgcpSessionMode_Type()
)
sonusMgcpSessionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpSessionMode.setStatus("current")


class _SonusMgcpSessionState_Type(SonusAdminState):
    """Custom type sonusMgcpSessionState based on SonusAdminState"""


_SonusMgcpSessionState_Object = MibTableColumn
sonusMgcpSessionState = _SonusMgcpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2, 2, 1, 4),
    _SonusMgcpSessionState_Type()
)
sonusMgcpSessionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpSessionState.setStatus("current")
_SonusMgcpSessionRowStatus_Type = RowStatus
_SonusMgcpSessionRowStatus_Object = MibTableColumn
sonusMgcpSessionRowStatus = _SonusMgcpSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2, 2, 1, 5),
    _SonusMgcpSessionRowStatus_Type()
)
sonusMgcpSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpSessionRowStatus.setStatus("current")


class _SonusMgcpSessionServProfileName_Type(SonusNameReference):
    """Custom type sonusMgcpSessionServProfileName based on SonusNameReference"""
    defaultValue = OctetString("default")


_SonusMgcpSessionServProfileName_Object = MibTableColumn
sonusMgcpSessionServProfileName = _SonusMgcpSessionServProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 2, 2, 1, 6),
    _SonusMgcpSessionServProfileName_Type()
)
sonusMgcpSessionServProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpSessionServProfileName.setStatus("current")
_SonusMgcpCallAgnt_ObjectIdentity = ObjectIdentity
sonusMgcpCallAgnt = _SonusMgcpCallAgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3)
)
_SonusMgcpCallAgntNextIndex_Type = Integer32
_SonusMgcpCallAgntNextIndex_Object = MibScalar
sonusMgcpCallAgntNextIndex = _SonusMgcpCallAgntNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3, 1),
    _SonusMgcpCallAgntNextIndex_Type()
)
sonusMgcpCallAgntNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntNextIndex.setStatus("current")
_SonusMgcpCallAgntTable_Object = MibTable
sonusMgcpCallAgntTable = _SonusMgcpCallAgntTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonusMgcpCallAgntTable.setStatus("current")
_SonusMgcpCallAgntEntry_Object = MibTableRow
sonusMgcpCallAgntEntry = _SonusMgcpCallAgntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3, 2, 1)
)
sonusMgcpCallAgntEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusMgcpCallAgntIndex"),
)
if mibBuilder.loadTexts:
    sonusMgcpCallAgntEntry.setStatus("current")
_SonusMgcpCallAgntIndex_Type = Integer32
_SonusMgcpCallAgntIndex_Object = MibTableColumn
sonusMgcpCallAgntIndex = _SonusMgcpCallAgntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3, 2, 1, 1),
    _SonusMgcpCallAgntIndex_Type()
)
sonusMgcpCallAgntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntIndex.setStatus("current")
_SonusMgcpCallAgntName_Type = SonusName
_SonusMgcpCallAgntName_Object = MibTableColumn
sonusMgcpCallAgntName = _SonusMgcpCallAgntName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3, 2, 1, 2),
    _SonusMgcpCallAgntName_Type()
)
sonusMgcpCallAgntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntName.setStatus("current")


class _SonusMgcpCallAgntState_Type(SonusAdminState):
    """Custom type sonusMgcpCallAgntState based on SonusAdminState"""


_SonusMgcpCallAgntState_Object = MibTableColumn
sonusMgcpCallAgntState = _SonusMgcpCallAgntState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3, 2, 1, 4),
    _SonusMgcpCallAgntState_Type()
)
sonusMgcpCallAgntState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntState.setStatus("current")
_SonusMgcpCallAgntRowStatus_Type = RowStatus
_SonusMgcpCallAgntRowStatus_Object = MibTableColumn
sonusMgcpCallAgntRowStatus = _SonusMgcpCallAgntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3, 2, 1, 5),
    _SonusMgcpCallAgntRowStatus_Type()
)
sonusMgcpCallAgntRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntRowStatus.setStatus("current")
_SonusMgcpCallAgntSessionName_Type = SonusNameReference
_SonusMgcpCallAgntSessionName_Object = MibTableColumn
sonusMgcpCallAgntSessionName = _SonusMgcpCallAgntSessionName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3, 2, 1, 6),
    _SonusMgcpCallAgntSessionName_Type()
)
sonusMgcpCallAgntSessionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntSessionName.setStatus("current")


class _SonusMgcpCallAgntDefNotEnt_Type(SonusBoolean):
    """Custom type sonusMgcpCallAgntDefNotEnt based on SonusBoolean"""


_SonusMgcpCallAgntDefNotEnt_Object = MibTableColumn
sonusMgcpCallAgntDefNotEnt = _SonusMgcpCallAgntDefNotEnt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 3, 2, 1, 7),
    _SonusMgcpCallAgntDefNotEnt_Type()
)
sonusMgcpCallAgntDefNotEnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntDefNotEnt.setStatus("current")
_SonusMgcpConnectionTable_Object = MibTable
sonusMgcpConnectionTable = _SonusMgcpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 4)
)
if mibBuilder.loadTexts:
    sonusMgcpConnectionTable.setStatus("current")
_SonusMgcpConnectionEntry_Object = MibTableRow
sonusMgcpConnectionEntry = _SonusMgcpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 4, 1)
)
sonusMgcpConnectionEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusMgcpConnectionIpaddr"),
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusMgcpConnectionPort"),
)
if mibBuilder.loadTexts:
    sonusMgcpConnectionEntry.setStatus("current")
_SonusMgcpConnectionIpaddr_Type = IpAddress
_SonusMgcpConnectionIpaddr_Object = MibTableColumn
sonusMgcpConnectionIpaddr = _SonusMgcpConnectionIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 4, 1, 1),
    _SonusMgcpConnectionIpaddr_Type()
)
sonusMgcpConnectionIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpConnectionIpaddr.setStatus("current")


class _SonusMgcpConnectionPort_Type(Integer32):
    """Custom type sonusMgcpConnectionPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusMgcpConnectionPort_Type.__name__ = "Integer32"
_SonusMgcpConnectionPort_Object = MibTableColumn
sonusMgcpConnectionPort = _SonusMgcpConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 4, 1, 2),
    _SonusMgcpConnectionPort_Type()
)
sonusMgcpConnectionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpConnectionPort.setStatus("current")


class _SonusMgcpConnectionState_Type(SonusAdminState):
    """Custom type sonusMgcpConnectionState based on SonusAdminState"""


_SonusMgcpConnectionState_Object = MibTableColumn
sonusMgcpConnectionState = _SonusMgcpConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 4, 1, 3),
    _SonusMgcpConnectionState_Type()
)
sonusMgcpConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpConnectionState.setStatus("current")
_SonusMgcpConnectionRowStatus_Type = RowStatus
_SonusMgcpConnectionRowStatus_Object = MibTableColumn
sonusMgcpConnectionRowStatus = _SonusMgcpConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 4, 1, 4),
    _SonusMgcpConnectionRowStatus_Type()
)
sonusMgcpConnectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpConnectionRowStatus.setStatus("current")
_SonusMgcpConnectionCallAgntName_Type = SonusNameReference
_SonusMgcpConnectionCallAgntName_Object = MibTableColumn
sonusMgcpConnectionCallAgntName = _SonusMgcpConnectionCallAgntName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 4, 1, 5),
    _SonusMgcpConnectionCallAgntName_Type()
)
sonusMgcpConnectionCallAgntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpConnectionCallAgntName.setStatus("current")
_SonusMgcpSessionStatusTable_Object = MibTable
sonusMgcpSessionStatusTable = _SonusMgcpSessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5)
)
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTable.setStatus("current")
_SonusMgcpSessionStatusEntry_Object = MibTableRow
sonusMgcpSessionStatusEntry = _SonusMgcpSessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1)
)
sonusMgcpSessionStatusEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusMgcpSessionStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusEntry.setStatus("current")
_SonusMgcpSessionStatusIndex_Type = Integer32
_SonusMgcpSessionStatusIndex_Object = MibTableColumn
sonusMgcpSessionStatusIndex = _SonusMgcpSessionStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 1),
    _SonusMgcpSessionStatusIndex_Type()
)
sonusMgcpSessionStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusIndex.setStatus("current")


class _SonusMgcpSessionStatusMajorVersion_Type(Integer32):
    """Custom type sonusMgcpSessionStatusMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusMgcpSessionStatusMajorVersion_Type.__name__ = "Integer32"
_SonusMgcpSessionStatusMajorVersion_Object = MibTableColumn
sonusMgcpSessionStatusMajorVersion = _SonusMgcpSessionStatusMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 3),
    _SonusMgcpSessionStatusMajorVersion_Type()
)
sonusMgcpSessionStatusMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusMajorVersion.setStatus("current")


class _SonusMgcpSessionStatusMinorVersion_Type(Integer32):
    """Custom type sonusMgcpSessionStatusMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusMgcpSessionStatusMinorVersion_Type.__name__ = "Integer32"
_SonusMgcpSessionStatusMinorVersion_Object = MibTableColumn
sonusMgcpSessionStatusMinorVersion = _SonusMgcpSessionStatusMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 4),
    _SonusMgcpSessionStatusMinorVersion_Type()
)
sonusMgcpSessionStatusMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusMinorVersion.setStatus("current")
_SonusMgcpSessionStatusNumCallAgnts_Type = Integer32
_SonusMgcpSessionStatusNumCallAgnts_Object = MibTableColumn
sonusMgcpSessionStatusNumCallAgnts = _SonusMgcpSessionStatusNumCallAgnts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 5),
    _SonusMgcpSessionStatusNumCallAgnts_Type()
)
sonusMgcpSessionStatusNumCallAgnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusNumCallAgnts.setStatus("current")


class _SonusMgcpSessionStatusStatus_Type(Integer32):
    """Custom type sonusMgcpSessionStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SonusMgcpSessionStatusStatus_Type.__name__ = "Integer32"
_SonusMgcpSessionStatusStatus_Object = MibTableColumn
sonusMgcpSessionStatusStatus = _SonusMgcpSessionStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 6),
    _SonusMgcpSessionStatusStatus_Type()
)
sonusMgcpSessionStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusStatus.setStatus("current")
_SonusMgcpSessionStatusRxMsgTotal_Type = Integer32
_SonusMgcpSessionStatusRxMsgTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxMsgTotal = _SonusMgcpSessionStatusRxMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 7),
    _SonusMgcpSessionStatusRxMsgTotal_Type()
)
sonusMgcpSessionStatusRxMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxMsgTotal.setStatus("current")
_SonusMgcpSessionStatusTxMsgTotal_Type = Integer32
_SonusMgcpSessionStatusTxMsgTotal_Object = MibTableColumn
sonusMgcpSessionStatusTxMsgTotal = _SonusMgcpSessionStatusTxMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 8),
    _SonusMgcpSessionStatusTxMsgTotal_Type()
)
sonusMgcpSessionStatusTxMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxMsgTotal.setStatus("current")
_SonusMgcpSessionStatusRxCmdTotal_Type = Integer32
_SonusMgcpSessionStatusRxCmdTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxCmdTotal = _SonusMgcpSessionStatusRxCmdTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 9),
    _SonusMgcpSessionStatusRxCmdTotal_Type()
)
sonusMgcpSessionStatusRxCmdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxCmdTotal.setStatus("current")
_SonusMgcpSessionStatusRxRspTotal_Type = Integer32
_SonusMgcpSessionStatusRxRspTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxRspTotal = _SonusMgcpSessionStatusRxRspTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 10),
    _SonusMgcpSessionStatusRxRspTotal_Type()
)
sonusMgcpSessionStatusRxRspTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxRspTotal.setStatus("current")
_SonusMgcpSessionStatusTxCmdTotal_Type = Integer32
_SonusMgcpSessionStatusTxCmdTotal_Object = MibTableColumn
sonusMgcpSessionStatusTxCmdTotal = _SonusMgcpSessionStatusTxCmdTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 11),
    _SonusMgcpSessionStatusTxCmdTotal_Type()
)
sonusMgcpSessionStatusTxCmdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxCmdTotal.setStatus("current")
_SonusMgcpSessionStatusTxRspTotal_Type = Integer32
_SonusMgcpSessionStatusTxRspTotal_Object = MibTableColumn
sonusMgcpSessionStatusTxRspTotal = _SonusMgcpSessionStatusTxRspTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 12),
    _SonusMgcpSessionStatusTxRspTotal_Type()
)
sonusMgcpSessionStatusTxRspTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxRspTotal.setStatus("current")
_SonusMgcpSessionStatusTxTOTotal_Type = Integer32
_SonusMgcpSessionStatusTxTOTotal_Object = MibTableColumn
sonusMgcpSessionStatusTxTOTotal = _SonusMgcpSessionStatusTxTOTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 13),
    _SonusMgcpSessionStatusTxTOTotal_Type()
)
sonusMgcpSessionStatusTxTOTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxTOTotal.setStatus("current")
_SonusMgcpSessionStatusTxAbortTotal_Type = Integer32
_SonusMgcpSessionStatusTxAbortTotal_Object = MibTableColumn
sonusMgcpSessionStatusTxAbortTotal = _SonusMgcpSessionStatusTxAbortTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 14),
    _SonusMgcpSessionStatusTxAbortTotal_Type()
)
sonusMgcpSessionStatusTxAbortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxAbortTotal.setStatus("current")
_SonusMgcpSessionStatusTxErrTotal_Type = Integer32
_SonusMgcpSessionStatusTxErrTotal_Object = MibTableColumn
sonusMgcpSessionStatusTxErrTotal = _SonusMgcpSessionStatusTxErrTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 15),
    _SonusMgcpSessionStatusTxErrTotal_Type()
)
sonusMgcpSessionStatusTxErrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxErrTotal.setStatus("current")
_SonusMgcpSessionStatusRxTOTotal_Type = Integer32
_SonusMgcpSessionStatusRxTOTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxTOTotal = _SonusMgcpSessionStatusRxTOTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 16),
    _SonusMgcpSessionStatusRxTOTotal_Type()
)
sonusMgcpSessionStatusRxTOTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxTOTotal.setStatus("current")
_SonusMgcpSessionStatusRxDupCmdTotal_Type = Integer32
_SonusMgcpSessionStatusRxDupCmdTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxDupCmdTotal = _SonusMgcpSessionStatusRxDupCmdTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 17),
    _SonusMgcpSessionStatusRxDupCmdTotal_Type()
)
sonusMgcpSessionStatusRxDupCmdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxDupCmdTotal.setStatus("current")
_SonusMgcpSessionStatusRxDupRspTotal_Type = Integer32
_SonusMgcpSessionStatusRxDupRspTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxDupRspTotal = _SonusMgcpSessionStatusRxDupRspTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 18),
    _SonusMgcpSessionStatusRxDupRspTotal_Type()
)
sonusMgcpSessionStatusRxDupRspTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxDupRspTotal.setStatus("current")
_SonusMgcpSessionStatusRxRspErrTotal_Type = Integer32
_SonusMgcpSessionStatusRxRspErrTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxRspErrTotal = _SonusMgcpSessionStatusRxRspErrTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 19),
    _SonusMgcpSessionStatusRxRspErrTotal_Type()
)
sonusMgcpSessionStatusRxRspErrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxRspErrTotal.setStatus("current")
_SonusMgcpSessionStatusRxRspInPTotal_Type = Integer32
_SonusMgcpSessionStatusRxRspInPTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxRspInPTotal = _SonusMgcpSessionStatusRxRspInPTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 20),
    _SonusMgcpSessionStatusRxRspInPTotal_Type()
)
sonusMgcpSessionStatusRxRspInPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxRspInPTotal.setStatus("current")
_SonusMgcpSessionStatusRxUnknownTotal_Type = Integer32
_SonusMgcpSessionStatusRxUnknownTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxUnknownTotal = _SonusMgcpSessionStatusRxUnknownTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 21),
    _SonusMgcpSessionStatusRxUnknownTotal_Type()
)
sonusMgcpSessionStatusRxUnknownTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxUnknownTotal.setStatus("current")
_SonusMgcpSessionStatusRxOverLenTotal_Type = Integer32
_SonusMgcpSessionStatusRxOverLenTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxOverLenTotal = _SonusMgcpSessionStatusRxOverLenTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 22),
    _SonusMgcpSessionStatusRxOverLenTotal_Type()
)
sonusMgcpSessionStatusRxOverLenTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxOverLenTotal.setStatus("current")
_SonusMgcpSessionStatusRxMaxByteCnt_Type = Integer32
_SonusMgcpSessionStatusRxMaxByteCnt_Object = MibTableColumn
sonusMgcpSessionStatusRxMaxByteCnt = _SonusMgcpSessionStatusRxMaxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 23),
    _SonusMgcpSessionStatusRxMaxByteCnt_Type()
)
sonusMgcpSessionStatusRxMaxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxMaxByteCnt.setStatus("current")
_SonusMgcpSessionStatusRxMaxPigBCnt_Type = Integer32
_SonusMgcpSessionStatusRxMaxPigBCnt_Object = MibTableColumn
sonusMgcpSessionStatusRxMaxPigBCnt = _SonusMgcpSessionStatusRxMaxPigBCnt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 24),
    _SonusMgcpSessionStatusRxMaxPigBCnt_Type()
)
sonusMgcpSessionStatusRxMaxPigBCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxMaxPigBCnt.setStatus("current")
_SonusMgcpSessionStatusTxMaxByteCnt_Type = Integer32
_SonusMgcpSessionStatusTxMaxByteCnt_Object = MibTableColumn
sonusMgcpSessionStatusTxMaxByteCnt = _SonusMgcpSessionStatusTxMaxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 25),
    _SonusMgcpSessionStatusTxMaxByteCnt_Type()
)
sonusMgcpSessionStatusTxMaxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxMaxByteCnt.setStatus("current")
_SonusMgcpSessionStatusTxMaxPigBCnt_Type = Integer32
_SonusMgcpSessionStatusTxMaxPigBCnt_Object = MibTableColumn
sonusMgcpSessionStatusTxMaxPigBCnt = _SonusMgcpSessionStatusTxMaxPigBCnt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 26),
    _SonusMgcpSessionStatusTxMaxPigBCnt_Type()
)
sonusMgcpSessionStatusTxMaxPigBCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxMaxPigBCnt.setStatus("current")
_SonusMgcpSessionStatusTxMaxCmdPnd_Type = Integer32
_SonusMgcpSessionStatusTxMaxCmdPnd_Object = MibTableColumn
sonusMgcpSessionStatusTxMaxCmdPnd = _SonusMgcpSessionStatusTxMaxCmdPnd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 27),
    _SonusMgcpSessionStatusTxMaxCmdPnd_Type()
)
sonusMgcpSessionStatusTxMaxCmdPnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxMaxCmdPnd.setStatus("current")
_SonusMgcpSessionStatusTxMaxRspPnd_Type = Integer32
_SonusMgcpSessionStatusTxMaxRspPnd_Object = MibTableColumn
sonusMgcpSessionStatusTxMaxRspPnd = _SonusMgcpSessionStatusTxMaxRspPnd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 28),
    _SonusMgcpSessionStatusTxMaxRspPnd_Type()
)
sonusMgcpSessionStatusTxMaxRspPnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxMaxRspPnd.setStatus("current")
_SonusMgcpSessionStatusRxCmdThrotCnt_Type = Integer32
_SonusMgcpSessionStatusRxCmdThrotCnt_Object = MibTableColumn
sonusMgcpSessionStatusRxCmdThrotCnt = _SonusMgcpSessionStatusRxCmdThrotCnt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 29),
    _SonusMgcpSessionStatusRxCmdThrotCnt_Type()
)
sonusMgcpSessionStatusRxCmdThrotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxCmdThrotCnt.setStatus("current")
_SonusMgcpSessionStatusRxErrorTotal_Type = Integer32
_SonusMgcpSessionStatusRxErrorTotal_Object = MibTableColumn
sonusMgcpSessionStatusRxErrorTotal = _SonusMgcpSessionStatusRxErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 30),
    _SonusMgcpSessionStatusRxErrorTotal_Type()
)
sonusMgcpSessionStatusRxErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxErrorTotal.setStatus("current")
_SonusMgcpSessionStatusTxErrorTotal_Type = Integer32
_SonusMgcpSessionStatusTxErrorTotal_Object = MibTableColumn
sonusMgcpSessionStatusTxErrorTotal = _SonusMgcpSessionStatusTxErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 31),
    _SonusMgcpSessionStatusTxErrorTotal_Type()
)
sonusMgcpSessionStatusTxErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxErrorTotal.setStatus("current")
_SonusMgcpSessionStatusRxCRCX_Type = Integer32
_SonusMgcpSessionStatusRxCRCX_Object = MibTableColumn
sonusMgcpSessionStatusRxCRCX = _SonusMgcpSessionStatusRxCRCX_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 32),
    _SonusMgcpSessionStatusRxCRCX_Type()
)
sonusMgcpSessionStatusRxCRCX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxCRCX.setStatus("current")
_SonusMgcpSessionStatusRxCRCXL_Type = Integer32
_SonusMgcpSessionStatusRxCRCXL_Object = MibTableColumn
sonusMgcpSessionStatusRxCRCXL = _SonusMgcpSessionStatusRxCRCXL_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 33),
    _SonusMgcpSessionStatusRxCRCXL_Type()
)
sonusMgcpSessionStatusRxCRCXL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxCRCXL.setStatus("current")
_SonusMgcpSessionStatusRxMDCX_Type = Integer32
_SonusMgcpSessionStatusRxMDCX_Object = MibTableColumn
sonusMgcpSessionStatusRxMDCX = _SonusMgcpSessionStatusRxMDCX_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 34),
    _SonusMgcpSessionStatusRxMDCX_Type()
)
sonusMgcpSessionStatusRxMDCX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxMDCX.setStatus("current")
_SonusMgcpSessionStatusRxDLCX_Type = Integer32
_SonusMgcpSessionStatusRxDLCX_Object = MibTableColumn
sonusMgcpSessionStatusRxDLCX = _SonusMgcpSessionStatusRxDLCX_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 35),
    _SonusMgcpSessionStatusRxDLCX_Type()
)
sonusMgcpSessionStatusRxDLCX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxDLCX.setStatus("current")
_SonusMgcpSessionStatusRxRQNT_Type = Integer32
_SonusMgcpSessionStatusRxRQNT_Object = MibTableColumn
sonusMgcpSessionStatusRxRQNT = _SonusMgcpSessionStatusRxRQNT_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 36),
    _SonusMgcpSessionStatusRxRQNT_Type()
)
sonusMgcpSessionStatusRxRQNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxRQNT.setStatus("current")
_SonusMgcpSessionStatusRxEPCF_Type = Integer32
_SonusMgcpSessionStatusRxEPCF_Object = MibTableColumn
sonusMgcpSessionStatusRxEPCF = _SonusMgcpSessionStatusRxEPCF_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 37),
    _SonusMgcpSessionStatusRxEPCF_Type()
)
sonusMgcpSessionStatusRxEPCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxEPCF.setStatus("current")
_SonusMgcpSessionStatusRxAUDT_Type = Integer32
_SonusMgcpSessionStatusRxAUDT_Object = MibTableColumn
sonusMgcpSessionStatusRxAUDT = _SonusMgcpSessionStatusRxAUDT_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 38),
    _SonusMgcpSessionStatusRxAUDT_Type()
)
sonusMgcpSessionStatusRxAUDT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusRxAUDT.setStatus("current")
_SonusMgcpSessionStatusTxCRCXRsp_Type = Integer32
_SonusMgcpSessionStatusTxCRCXRsp_Object = MibTableColumn
sonusMgcpSessionStatusTxCRCXRsp = _SonusMgcpSessionStatusTxCRCXRsp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 39),
    _SonusMgcpSessionStatusTxCRCXRsp_Type()
)
sonusMgcpSessionStatusTxCRCXRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxCRCXRsp.setStatus("current")
_SonusMgcpSessionStatusTxCRCXRspL_Type = Integer32
_SonusMgcpSessionStatusTxCRCXRspL_Object = MibTableColumn
sonusMgcpSessionStatusTxCRCXRspL = _SonusMgcpSessionStatusTxCRCXRspL_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 40),
    _SonusMgcpSessionStatusTxCRCXRspL_Type()
)
sonusMgcpSessionStatusTxCRCXRspL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxCRCXRspL.setStatus("current")
_SonusMgcpSessionStatusTxCRCXRspErr_Type = Integer32
_SonusMgcpSessionStatusTxCRCXRspErr_Object = MibTableColumn
sonusMgcpSessionStatusTxCRCXRspErr = _SonusMgcpSessionStatusTxCRCXRspErr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 41),
    _SonusMgcpSessionStatusTxCRCXRspErr_Type()
)
sonusMgcpSessionStatusTxCRCXRspErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxCRCXRspErr.setStatus("current")
_SonusMgcpSessionStatusTxMDCXRsp_Type = Integer32
_SonusMgcpSessionStatusTxMDCXRsp_Object = MibTableColumn
sonusMgcpSessionStatusTxMDCXRsp = _SonusMgcpSessionStatusTxMDCXRsp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 42),
    _SonusMgcpSessionStatusTxMDCXRsp_Type()
)
sonusMgcpSessionStatusTxMDCXRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxMDCXRsp.setStatus("current")
_SonusMgcpSessionStatusTxMDCXRspErr_Type = Integer32
_SonusMgcpSessionStatusTxMDCXRspErr_Object = MibTableColumn
sonusMgcpSessionStatusTxMDCXRspErr = _SonusMgcpSessionStatusTxMDCXRspErr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 43),
    _SonusMgcpSessionStatusTxMDCXRspErr_Type()
)
sonusMgcpSessionStatusTxMDCXRspErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxMDCXRspErr.setStatus("current")
_SonusMgcpSessionStatusTxDLCXRsp_Type = Integer32
_SonusMgcpSessionStatusTxDLCXRsp_Object = MibTableColumn
sonusMgcpSessionStatusTxDLCXRsp = _SonusMgcpSessionStatusTxDLCXRsp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 44),
    _SonusMgcpSessionStatusTxDLCXRsp_Type()
)
sonusMgcpSessionStatusTxDLCXRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxDLCXRsp.setStatus("current")
_SonusMgcpSessionStatusTxDLCXRspErr_Type = Integer32
_SonusMgcpSessionStatusTxDLCXRspErr_Object = MibTableColumn
sonusMgcpSessionStatusTxDLCXRspErr = _SonusMgcpSessionStatusTxDLCXRspErr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 45),
    _SonusMgcpSessionStatusTxDLCXRspErr_Type()
)
sonusMgcpSessionStatusTxDLCXRspErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxDLCXRspErr.setStatus("current")
_SonusMgcpSessionStatusTxAUDTRsp_Type = Integer32
_SonusMgcpSessionStatusTxAUDTRsp_Object = MibTableColumn
sonusMgcpSessionStatusTxAUDTRsp = _SonusMgcpSessionStatusTxAUDTRsp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 46),
    _SonusMgcpSessionStatusTxAUDTRsp_Type()
)
sonusMgcpSessionStatusTxAUDTRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxAUDTRsp.setStatus("current")
_SonusMgcpSessionStatusTxAUDTRspErr_Type = Integer32
_SonusMgcpSessionStatusTxAUDTRspErr_Object = MibTableColumn
sonusMgcpSessionStatusTxAUDTRspErr = _SonusMgcpSessionStatusTxAUDTRspErr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 47),
    _SonusMgcpSessionStatusTxAUDTRspErr_Type()
)
sonusMgcpSessionStatusTxAUDTRspErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxAUDTRspErr.setStatus("current")
_SonusMgcpSessionStatusTxRQNTRsp_Type = Integer32
_SonusMgcpSessionStatusTxRQNTRsp_Object = MibTableColumn
sonusMgcpSessionStatusTxRQNTRsp = _SonusMgcpSessionStatusTxRQNTRsp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 48),
    _SonusMgcpSessionStatusTxRQNTRsp_Type()
)
sonusMgcpSessionStatusTxRQNTRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxRQNTRsp.setStatus("current")
_SonusMgcpSessionStatusTxRQNTRspErr_Type = Integer32
_SonusMgcpSessionStatusTxRQNTRspErr_Object = MibTableColumn
sonusMgcpSessionStatusTxRQNTRspErr = _SonusMgcpSessionStatusTxRQNTRspErr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 49),
    _SonusMgcpSessionStatusTxRQNTRspErr_Type()
)
sonusMgcpSessionStatusTxRQNTRspErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxRQNTRspErr.setStatus("current")
_SonusMgcpSessionStatusTxRSIPCmd_Type = Integer32
_SonusMgcpSessionStatusTxRSIPCmd_Object = MibTableColumn
sonusMgcpSessionStatusTxRSIPCmd = _SonusMgcpSessionStatusTxRSIPCmd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 50),
    _SonusMgcpSessionStatusTxRSIPCmd_Type()
)
sonusMgcpSessionStatusTxRSIPCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxRSIPCmd.setStatus("current")
_SonusMgcpSessionStatusTxNTFYCmd_Type = Integer32
_SonusMgcpSessionStatusTxNTFYCmd_Object = MibTableColumn
sonusMgcpSessionStatusTxNTFYCmd = _SonusMgcpSessionStatusTxNTFYCmd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 51),
    _SonusMgcpSessionStatusTxNTFYCmd_Type()
)
sonusMgcpSessionStatusTxNTFYCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxNTFYCmd.setStatus("current")
_SonusMgcpSessionStatusTxDLCXCmd_Type = Integer32
_SonusMgcpSessionStatusTxDLCXCmd_Object = MibTableColumn
sonusMgcpSessionStatusTxDLCXCmd = _SonusMgcpSessionStatusTxDLCXCmd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 5, 1, 52),
    _SonusMgcpSessionStatusTxDLCXCmd_Type()
)
sonusMgcpSessionStatusTxDLCXCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpSessionStatusTxDLCXCmd.setStatus("current")
_SonusMgcpCallAgntStatusTable_Object = MibTable
sonusMgcpCallAgntStatusTable = _SonusMgcpCallAgntStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 6)
)
if mibBuilder.loadTexts:
    sonusMgcpCallAgntStatusTable.setStatus("current")
_SonusMgcpCallAgntStatusEntry_Object = MibTableRow
sonusMgcpCallAgntStatusEntry = _SonusMgcpCallAgntStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 6, 1)
)
sonusMgcpCallAgntStatusEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusMgcpCallAgntStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusMgcpCallAgntStatusEntry.setStatus("current")
_SonusMgcpCallAgntStatusIndex_Type = Integer32
_SonusMgcpCallAgntStatusIndex_Object = MibTableColumn
sonusMgcpCallAgntStatusIndex = _SonusMgcpCallAgntStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 6, 1, 1),
    _SonusMgcpCallAgntStatusIndex_Type()
)
sonusMgcpCallAgntStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntStatusIndex.setStatus("current")
_SonusMgcpCallAgntStatusNumConnections_Type = Integer32
_SonusMgcpCallAgntStatusNumConnections_Object = MibTableColumn
sonusMgcpCallAgntStatusNumConnections = _SonusMgcpCallAgntStatusNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 6, 1, 2),
    _SonusMgcpCallAgntStatusNumConnections_Type()
)
sonusMgcpCallAgntStatusNumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntStatusNumConnections.setStatus("current")


class _SonusMgcpCallAgntStatusStatus_Type(Integer32):
    """Custom type sonusMgcpCallAgntStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SonusMgcpCallAgntStatusStatus_Type.__name__ = "Integer32"
_SonusMgcpCallAgntStatusStatus_Object = MibTableColumn
sonusMgcpCallAgntStatusStatus = _SonusMgcpCallAgntStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 6, 1, 3),
    _SonusMgcpCallAgntStatusStatus_Type()
)
sonusMgcpCallAgntStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpCallAgntStatusStatus.setStatus("current")
_SonusMgcpServProfile_ObjectIdentity = ObjectIdentity
sonusMgcpServProfile = _SonusMgcpServProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8)
)
_SonusMgcpServProfileNextIndex_Type = Integer32
_SonusMgcpServProfileNextIndex_Object = MibScalar
sonusMgcpServProfileNextIndex = _SonusMgcpServProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 1),
    _SonusMgcpServProfileNextIndex_Type()
)
sonusMgcpServProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpServProfileNextIndex.setStatus("current")
_SonusMgcpServProfileTable_Object = MibTable
sonusMgcpServProfileTable = _SonusMgcpServProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2)
)
if mibBuilder.loadTexts:
    sonusMgcpServProfileTable.setStatus("current")
_SonusMgcpServProfileEntry_Object = MibTableRow
sonusMgcpServProfileEntry = _SonusMgcpServProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1)
)
sonusMgcpServProfileEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusMgcpServProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusMgcpServProfileEntry.setStatus("current")
_SonusMgcpServProfileIndex_Type = Integer32
_SonusMgcpServProfileIndex_Object = MibTableColumn
sonusMgcpServProfileIndex = _SonusMgcpServProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1, 1),
    _SonusMgcpServProfileIndex_Type()
)
sonusMgcpServProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgcpServProfileIndex.setStatus("current")
_SonusMgcpServProfileName_Type = SonusName
_SonusMgcpServProfileName_Object = MibTableColumn
sonusMgcpServProfileName = _SonusMgcpServProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1, 2),
    _SonusMgcpServProfileName_Type()
)
sonusMgcpServProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpServProfileName.setStatus("current")


class _SonusMgcpServProfileState_Type(SonusAdminState):
    """Custom type sonusMgcpServProfileState based on SonusAdminState"""


_SonusMgcpServProfileState_Object = MibTableColumn
sonusMgcpServProfileState = _SonusMgcpServProfileState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1, 3),
    _SonusMgcpServProfileState_Type()
)
sonusMgcpServProfileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpServProfileState.setStatus("current")
_SonusMgcpServProfileRowStatus_Type = RowStatus
_SonusMgcpServProfileRowStatus_Object = MibTableColumn
sonusMgcpServProfileRowStatus = _SonusMgcpServProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1, 4),
    _SonusMgcpServProfileRowStatus_Type()
)
sonusMgcpServProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpServProfileRowStatus.setStatus("current")


class _SonusMgcpServProfileEncodeType_Type(Integer32):
    """Custom type sonusMgcpServProfileEncodeType based on Integer32"""
    defaultValue = 1

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
        *(("g711alaw", 2),
          ("g711ulaw", 1),
          ("g723", 3),
          ("g729", 4))
    )


_SonusMgcpServProfileEncodeType_Type.__name__ = "Integer32"
_SonusMgcpServProfileEncodeType_Object = MibTableColumn
sonusMgcpServProfileEncodeType = _SonusMgcpServProfileEncodeType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1, 5),
    _SonusMgcpServProfileEncodeType_Type()
)
sonusMgcpServProfileEncodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpServProfileEncodeType.setStatus("current")


class _SonusMgcpServProfilePacketPeriod_Type(Integer32):
    """Custom type sonusMgcpServProfilePacketPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 40),
    )


_SonusMgcpServProfilePacketPeriod_Type.__name__ = "Integer32"
_SonusMgcpServProfilePacketPeriod_Object = MibTableColumn
sonusMgcpServProfilePacketPeriod = _SonusMgcpServProfilePacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1, 6),
    _SonusMgcpServProfilePacketPeriod_Type()
)
sonusMgcpServProfilePacketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpServProfilePacketPeriod.setStatus("current")


class _SonusMgcpServProfileTypeOfService_Type(Integer32):
    """Custom type sonusMgcpServProfileTypeOfService based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusMgcpServProfileTypeOfService_Type.__name__ = "Integer32"
_SonusMgcpServProfileTypeOfService_Object = MibTableColumn
sonusMgcpServProfileTypeOfService = _SonusMgcpServProfileTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1, 7),
    _SonusMgcpServProfileTypeOfService_Type()
)
sonusMgcpServProfileTypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpServProfileTypeOfService.setStatus("current")


class _SonusMgcpServProfileEchoCancellation_Type(Integer32):
    """Custom type sonusMgcpServProfileEchoCancellation based on Integer32"""
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
        *(("off", 1),
          ("on", 2),
          ("useCktProfile", 3))
    )


_SonusMgcpServProfileEchoCancellation_Type.__name__ = "Integer32"
_SonusMgcpServProfileEchoCancellation_Object = MibTableColumn
sonusMgcpServProfileEchoCancellation = _SonusMgcpServProfileEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1, 8),
    _SonusMgcpServProfileEchoCancellation_Type()
)
sonusMgcpServProfileEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpServProfileEchoCancellation.setStatus("current")


class _SonusMgcpServProfileSilenceSuppression_Type(Integer32):
    """Custom type sonusMgcpServProfileSilenceSuppression based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SonusMgcpServProfileSilenceSuppression_Type.__name__ = "Integer32"
_SonusMgcpServProfileSilenceSuppression_Object = MibTableColumn
sonusMgcpServProfileSilenceSuppression = _SonusMgcpServProfileSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 8, 2, 1, 9),
    _SonusMgcpServProfileSilenceSuppression_Type()
)
sonusMgcpServProfileSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgcpServProfileSilenceSuppression.setStatus("current")
_SonusIuaGateway_ObjectIdentity = ObjectIdentity
sonusIuaGateway = _SonusIuaGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9)
)


class _SonusIuaGatewayPort_Type(Integer32):
    """Custom type sonusIuaGatewayPort based on Integer32"""
    defaultValue = 9900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusIuaGatewayPort_Type.__name__ = "Integer32"
_SonusIuaGatewayPort_Object = MibScalar
sonusIuaGatewayPort = _SonusIuaGatewayPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9, 1),
    _SonusIuaGatewayPort_Type()
)
sonusIuaGatewayPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaGatewayPort.setStatus("current")


class _SonusIuaGatewayHbTimeout_Type(Integer32):
    """Custom type sonusIuaGatewayHbTimeout based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_SonusIuaGatewayHbTimeout_Type.__name__ = "Integer32"
_SonusIuaGatewayHbTimeout_Object = MibScalar
sonusIuaGatewayHbTimeout = _SonusIuaGatewayHbTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9, 2),
    _SonusIuaGatewayHbTimeout_Type()
)
sonusIuaGatewayHbTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaGatewayHbTimeout.setStatus("current")


class _SonusIuaGatewayASPendingTimeout_Type(Integer32):
    """Custom type sonusIuaGatewayASPendingTimeout based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_SonusIuaGatewayASPendingTimeout_Type.__name__ = "Integer32"
_SonusIuaGatewayASPendingTimeout_Object = MibScalar
sonusIuaGatewayASPendingTimeout = _SonusIuaGatewayASPendingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9, 3),
    _SonusIuaGatewayASPendingTimeout_Type()
)
sonusIuaGatewayASPendingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaGatewayASPendingTimeout.setStatus("current")


class _SonusIuaGatewayEstRelIndRetry_Type(Integer32):
    """Custom type sonusIuaGatewayEstRelIndRetry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SonusIuaGatewayEstRelIndRetry_Type.__name__ = "Integer32"
_SonusIuaGatewayEstRelIndRetry_Object = MibScalar
sonusIuaGatewayEstRelIndRetry = _SonusIuaGatewayEstRelIndRetry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9, 4),
    _SonusIuaGatewayEstRelIndRetry_Type()
)
sonusIuaGatewayEstRelIndRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaGatewayEstRelIndRetry.setStatus("current")


class _SonusIuaGatewayEstRelIndTimeout_Type(Integer32):
    """Custom type sonusIuaGatewayEstRelIndTimeout based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_SonusIuaGatewayEstRelIndTimeout_Type.__name__ = "Integer32"
_SonusIuaGatewayEstRelIndTimeout_Object = MibScalar
sonusIuaGatewayEstRelIndTimeout = _SonusIuaGatewayEstRelIndTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9, 5),
    _SonusIuaGatewayEstRelIndTimeout_Type()
)
sonusIuaGatewayEstRelIndTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaGatewayEstRelIndTimeout.setStatus("current")


class _SonusIuaGatewayDataIndTimeout_Type(Integer32):
    """Custom type sonusIuaGatewayDataIndTimeout based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_SonusIuaGatewayDataIndTimeout_Type.__name__ = "Integer32"
_SonusIuaGatewayDataIndTimeout_Object = MibScalar
sonusIuaGatewayDataIndTimeout = _SonusIuaGatewayDataIndTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9, 6),
    _SonusIuaGatewayDataIndTimeout_Type()
)
sonusIuaGatewayDataIndTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaGatewayDataIndTimeout.setStatus("current")


class _SonusIuaGatewayDataIndRetryExp_Type(Integer32):
    """Custom type sonusIuaGatewayDataIndRetryExp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SonusIuaGatewayDataIndRetryExp_Type.__name__ = "Integer32"
_SonusIuaGatewayDataIndRetryExp_Object = MibScalar
sonusIuaGatewayDataIndRetryExp = _SonusIuaGatewayDataIndRetryExp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9, 7),
    _SonusIuaGatewayDataIndRetryExp_Type()
)
sonusIuaGatewayDataIndRetryExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaGatewayDataIndRetryExp.setStatus("current")


class _SonusIuaGatewayDataIndWindowSize_Type(Integer32):
    """Custom type sonusIuaGatewayDataIndWindowSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusIuaGatewayDataIndWindowSize_Type.__name__ = "Integer32"
_SonusIuaGatewayDataIndWindowSize_Object = MibScalar
sonusIuaGatewayDataIndWindowSize = _SonusIuaGatewayDataIndWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9, 8),
    _SonusIuaGatewayDataIndWindowSize_Type()
)
sonusIuaGatewayDataIndWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaGatewayDataIndWindowSize.setStatus("current")


class _SonusIuaGatewayDataIndMaxTimeout_Type(Integer32):
    """Custom type sonusIuaGatewayDataIndMaxTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SonusIuaGatewayDataIndMaxTimeout_Type.__name__ = "Integer32"
_SonusIuaGatewayDataIndMaxTimeout_Object = MibScalar
sonusIuaGatewayDataIndMaxTimeout = _SonusIuaGatewayDataIndMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 9, 9),
    _SonusIuaGatewayDataIndMaxTimeout_Type()
)
sonusIuaGatewayDataIndMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaGatewayDataIndMaxTimeout.setStatus("current")
_SonusIuaAs_ObjectIdentity = ObjectIdentity
sonusIuaAs = _SonusIuaAs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 10)
)
_SonusIuaAsNextIndex_Type = Integer32
_SonusIuaAsNextIndex_Object = MibScalar
sonusIuaAsNextIndex = _SonusIuaAsNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 10, 1),
    _SonusIuaAsNextIndex_Type()
)
sonusIuaAsNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsNextIndex.setStatus("current")
_SonusIuaAsTable_Object = MibTable
sonusIuaAsTable = _SonusIuaAsTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 10, 2)
)
if mibBuilder.loadTexts:
    sonusIuaAsTable.setStatus("current")
_SonusIuaAsEntry_Object = MibTableRow
sonusIuaAsEntry = _SonusIuaAsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 10, 2, 1)
)
sonusIuaAsEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaAsIndex"),
)
if mibBuilder.loadTexts:
    sonusIuaAsEntry.setStatus("current")
_SonusIuaAsIndex_Type = Integer32
_SonusIuaAsIndex_Object = MibTableColumn
sonusIuaAsIndex = _SonusIuaAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 10, 2, 1, 1),
    _SonusIuaAsIndex_Type()
)
sonusIuaAsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsIndex.setStatus("current")
_SonusIuaAsName_Type = SonusName
_SonusIuaAsName_Object = MibTableColumn
sonusIuaAsName = _SonusIuaAsName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 10, 2, 1, 2),
    _SonusIuaAsName_Type()
)
sonusIuaAsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaAsName.setStatus("current")


class _SonusIuaAsMode_Type(SonusServiceState):
    """Custom type sonusIuaAsMode based on SonusServiceState"""


_SonusIuaAsMode_Object = MibTableColumn
sonusIuaAsMode = _SonusIuaAsMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 10, 2, 1, 3),
    _SonusIuaAsMode_Type()
)
sonusIuaAsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaAsMode.setStatus("current")


class _SonusIuaAsState_Type(SonusAdminState):
    """Custom type sonusIuaAsState based on SonusAdminState"""


_SonusIuaAsState_Object = MibTableColumn
sonusIuaAsState = _SonusIuaAsState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 10, 2, 1, 4),
    _SonusIuaAsState_Type()
)
sonusIuaAsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaAsState.setStatus("current")
_SonusIuaAsRowStatus_Type = RowStatus
_SonusIuaAsRowStatus_Object = MibTableColumn
sonusIuaAsRowStatus = _SonusIuaAsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 10, 2, 1, 5),
    _SonusIuaAsRowStatus_Type()
)
sonusIuaAsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaAsRowStatus.setStatus("current")
_SonusIuaAsp_ObjectIdentity = ObjectIdentity
sonusIuaAsp = _SonusIuaAsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 11)
)
_SonusIuaAspNextIndex_Type = Integer32
_SonusIuaAspNextIndex_Object = MibScalar
sonusIuaAspNextIndex = _SonusIuaAspNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 11, 1),
    _SonusIuaAspNextIndex_Type()
)
sonusIuaAspNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAspNextIndex.setStatus("current")
_SonusIuaAspTable_Object = MibTable
sonusIuaAspTable = _SonusIuaAspTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 11, 2)
)
if mibBuilder.loadTexts:
    sonusIuaAspTable.setStatus("current")
_SonusIuaAspEntry_Object = MibTableRow
sonusIuaAspEntry = _SonusIuaAspEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 11, 2, 1)
)
sonusIuaAspEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaAspIndex"),
)
if mibBuilder.loadTexts:
    sonusIuaAspEntry.setStatus("current")
_SonusIuaAspIndex_Type = Integer32
_SonusIuaAspIndex_Object = MibTableColumn
sonusIuaAspIndex = _SonusIuaAspIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 11, 2, 1, 1),
    _SonusIuaAspIndex_Type()
)
sonusIuaAspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAspIndex.setStatus("current")
_SonusIuaAspName_Type = SonusName
_SonusIuaAspName_Object = MibTableColumn
sonusIuaAspName = _SonusIuaAspName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 11, 2, 1, 2),
    _SonusIuaAspName_Type()
)
sonusIuaAspName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaAspName.setStatus("current")


class _SonusIuaAspState_Type(SonusAdminState):
    """Custom type sonusIuaAspState based on SonusAdminState"""


_SonusIuaAspState_Object = MibTableColumn
sonusIuaAspState = _SonusIuaAspState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 11, 2, 1, 3),
    _SonusIuaAspState_Type()
)
sonusIuaAspState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaAspState.setStatus("current")
_SonusIuaAspRowStatus_Type = RowStatus
_SonusIuaAspRowStatus_Object = MibTableColumn
sonusIuaAspRowStatus = _SonusIuaAspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 11, 2, 1, 4),
    _SonusIuaAspRowStatus_Type()
)
sonusIuaAspRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaAspRowStatus.setStatus("current")
_SonusIuaConnectionTable_Object = MibTable
sonusIuaConnectionTable = _SonusIuaConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 12)
)
if mibBuilder.loadTexts:
    sonusIuaConnectionTable.setStatus("current")
_SonusIuaConnectionEntry_Object = MibTableRow
sonusIuaConnectionEntry = _SonusIuaConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 12, 1)
)
sonusIuaConnectionEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaConnectionIpaddr"),
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaConnectionPort"),
)
if mibBuilder.loadTexts:
    sonusIuaConnectionEntry.setStatus("current")
_SonusIuaConnectionIpaddr_Type = IpAddress
_SonusIuaConnectionIpaddr_Object = MibTableColumn
sonusIuaConnectionIpaddr = _SonusIuaConnectionIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 12, 1, 1),
    _SonusIuaConnectionIpaddr_Type()
)
sonusIuaConnectionIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaConnectionIpaddr.setStatus("current")


class _SonusIuaConnectionPort_Type(Integer32):
    """Custom type sonusIuaConnectionPort based on Integer32"""
    defaultValue = 9900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusIuaConnectionPort_Type.__name__ = "Integer32"
_SonusIuaConnectionPort_Object = MibTableColumn
sonusIuaConnectionPort = _SonusIuaConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 12, 1, 2),
    _SonusIuaConnectionPort_Type()
)
sonusIuaConnectionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaConnectionPort.setStatus("current")


class _SonusIuaConnectionState_Type(SonusAdminState):
    """Custom type sonusIuaConnectionState based on SonusAdminState"""


_SonusIuaConnectionState_Object = MibTableColumn
sonusIuaConnectionState = _SonusIuaConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 12, 1, 3),
    _SonusIuaConnectionState_Type()
)
sonusIuaConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaConnectionState.setStatus("current")
_SonusIuaConnectionRowStatus_Type = RowStatus
_SonusIuaConnectionRowStatus_Object = MibTableColumn
sonusIuaConnectionRowStatus = _SonusIuaConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 12, 1, 4),
    _SonusIuaConnectionRowStatus_Type()
)
sonusIuaConnectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaConnectionRowStatus.setStatus("current")
_SonusIuaConnectionAspName_Type = SonusNameReference
_SonusIuaConnectionAspName_Object = MibTableColumn
sonusIuaConnectionAspName = _SonusIuaConnectionAspName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 12, 1, 5),
    _SonusIuaConnectionAspName_Type()
)
sonusIuaConnectionAspName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaConnectionAspName.setStatus("current")
_SonusIuaInterfaceTable_Object = MibTable
sonusIuaInterfaceTable = _SonusIuaInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 13)
)
if mibBuilder.loadTexts:
    sonusIuaInterfaceTable.setStatus("current")
_SonusIuaInterfaceEntry_Object = MibTableRow
sonusIuaInterfaceEntry = _SonusIuaInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 13, 1)
)
sonusIuaInterfaceEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaInterfaceShelf"),
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaInterfaceSlot"),
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaInterfacePort"),
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaInterfaceTimeslot"),
)
if mibBuilder.loadTexts:
    sonusIuaInterfaceEntry.setStatus("current")
_SonusIuaInterfaceShelf_Type = SonusShelfIndex
_SonusIuaInterfaceShelf_Object = MibTableColumn
sonusIuaInterfaceShelf = _SonusIuaInterfaceShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 13, 1, 1),
    _SonusIuaInterfaceShelf_Type()
)
sonusIuaInterfaceShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaInterfaceShelf.setStatus("current")
_SonusIuaInterfaceSlot_Type = SonusSlotIndex
_SonusIuaInterfaceSlot_Object = MibTableColumn
sonusIuaInterfaceSlot = _SonusIuaInterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 13, 1, 2),
    _SonusIuaInterfaceSlot_Type()
)
sonusIuaInterfaceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaInterfaceSlot.setStatus("current")


class _SonusIuaInterfacePort_Type(Integer32):
    """Custom type sonusIuaInterfacePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_SonusIuaInterfacePort_Type.__name__ = "Integer32"
_SonusIuaInterfacePort_Object = MibTableColumn
sonusIuaInterfacePort = _SonusIuaInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 13, 1, 3),
    _SonusIuaInterfacePort_Type()
)
sonusIuaInterfacePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaInterfacePort.setStatus("current")


class _SonusIuaInterfaceTimeslot_Type(Integer32):
    """Custom type sonusIuaInterfaceTimeslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusIuaInterfaceTimeslot_Type.__name__ = "Integer32"
_SonusIuaInterfaceTimeslot_Object = MibTableColumn
sonusIuaInterfaceTimeslot = _SonusIuaInterfaceTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 13, 1, 4),
    _SonusIuaInterfaceTimeslot_Type()
)
sonusIuaInterfaceTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaInterfaceTimeslot.setStatus("current")
_SonusIuaInterfaceRowStatus_Type = RowStatus
_SonusIuaInterfaceRowStatus_Object = MibTableColumn
sonusIuaInterfaceRowStatus = _SonusIuaInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 13, 1, 5),
    _SonusIuaInterfaceRowStatus_Type()
)
sonusIuaInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaInterfaceRowStatus.setStatus("current")
_SonusIuaInterfaceAsName_Type = SonusNameReference
_SonusIuaInterfaceAsName_Object = MibTableColumn
sonusIuaInterfaceAsName = _SonusIuaInterfaceAsName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 13, 1, 6),
    _SonusIuaInterfaceAsName_Type()
)
sonusIuaInterfaceAsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaInterfaceAsName.setStatus("current")
_SonusIuaAsaTable_Object = MibTable
sonusIuaAsaTable = _SonusIuaAsaTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 14)
)
if mibBuilder.loadTexts:
    sonusIuaAsaTable.setStatus("current")
_SonusIuaAsaEntry_Object = MibTableRow
sonusIuaAsaEntry = _SonusIuaAsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 14, 1)
)
sonusIuaAsaEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaAsaAsIndex"),
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaAsaAspIndex"),
)
if mibBuilder.loadTexts:
    sonusIuaAsaEntry.setStatus("current")
_SonusIuaAsaAsIndex_Type = Integer32
_SonusIuaAsaAsIndex_Object = MibTableColumn
sonusIuaAsaAsIndex = _SonusIuaAsaAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 14, 1, 1),
    _SonusIuaAsaAsIndex_Type()
)
sonusIuaAsaAsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsaAsIndex.setStatus("current")
_SonusIuaAsaAspIndex_Type = Integer32
_SonusIuaAsaAspIndex_Object = MibTableColumn
sonusIuaAsaAspIndex = _SonusIuaAsaAspIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 14, 1, 2),
    _SonusIuaAsaAspIndex_Type()
)
sonusIuaAsaAspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsaAspIndex.setStatus("current")
_SonusIuaAsaRowStatus_Type = RowStatus
_SonusIuaAsaRowStatus_Object = MibTableColumn
sonusIuaAsaRowStatus = _SonusIuaAsaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 14, 1, 3),
    _SonusIuaAsaRowStatus_Type()
)
sonusIuaAsaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIuaAsaRowStatus.setStatus("current")
_SonusIuaAsStatusTable_Object = MibTable
sonusIuaAsStatusTable = _SonusIuaAsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15)
)
if mibBuilder.loadTexts:
    sonusIuaAsStatusTable.setStatus("current")
_SonusIuaAsStatusEntry_Object = MibTableRow
sonusIuaAsStatusEntry = _SonusIuaAsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1)
)
sonusIuaAsStatusEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaAsStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusIuaAsStatusEntry.setStatus("current")
_SonusIuaAsStatusIndex_Type = Integer32
_SonusIuaAsStatusIndex_Object = MibTableColumn
sonusIuaAsStatusIndex = _SonusIuaAsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 1),
    _SonusIuaAsStatusIndex_Type()
)
sonusIuaAsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusIndex.setStatus("current")


class _SonusIuaAsStatusMessageVersion_Type(Integer32):
    """Custom type sonusIuaAsStatusMessageVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusIuaAsStatusMessageVersion_Type.__name__ = "Integer32"
_SonusIuaAsStatusMessageVersion_Object = MibTableColumn
sonusIuaAsStatusMessageVersion = _SonusIuaAsStatusMessageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 2),
    _SonusIuaAsStatusMessageVersion_Type()
)
sonusIuaAsStatusMessageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusMessageVersion.setStatus("current")
_SonusIuaAsStatusNumAsps_Type = Integer32
_SonusIuaAsStatusNumAsps_Object = MibTableColumn
sonusIuaAsStatusNumAsps = _SonusIuaAsStatusNumAsps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 4),
    _SonusIuaAsStatusNumAsps_Type()
)
sonusIuaAsStatusNumAsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusNumAsps.setStatus("current")
_SonusIuaAsStatusNumInterfaces_Type = Integer32
_SonusIuaAsStatusNumInterfaces_Object = MibTableColumn
sonusIuaAsStatusNumInterfaces = _SonusIuaAsStatusNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 5),
    _SonusIuaAsStatusNumInterfaces_Type()
)
sonusIuaAsStatusNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusNumInterfaces.setStatus("current")


class _SonusIuaAsStatusStatus_Type(Integer32):
    """Custom type sonusIuaAsStatusStatus based on Integer32"""
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
        *(("active", 4),
          ("down", 1),
          ("inactive", 2),
          ("pending", 3))
    )


_SonusIuaAsStatusStatus_Type.__name__ = "Integer32"
_SonusIuaAsStatusStatus_Object = MibTableColumn
sonusIuaAsStatusStatus = _SonusIuaAsStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 6),
    _SonusIuaAsStatusStatus_Type()
)
sonusIuaAsStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusStatus.setStatus("current")
_SonusIuaAsStatusRxMsgTotal_Type = Integer32
_SonusIuaAsStatusRxMsgTotal_Object = MibTableColumn
sonusIuaAsStatusRxMsgTotal = _SonusIuaAsStatusRxMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 7),
    _SonusIuaAsStatusRxMsgTotal_Type()
)
sonusIuaAsStatusRxMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxMsgTotal.setStatus("current")
_SonusIuaAsStatusTxMsgTotal_Type = Integer32
_SonusIuaAsStatusTxMsgTotal_Object = MibTableColumn
sonusIuaAsStatusTxMsgTotal = _SonusIuaAsStatusTxMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 8),
    _SonusIuaAsStatusTxMsgTotal_Type()
)
sonusIuaAsStatusTxMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxMsgTotal.setStatus("current")
_SonusIuaAsStatusRxQptmTotal_Type = Integer32
_SonusIuaAsStatusRxQptmTotal_Object = MibTableColumn
sonusIuaAsStatusRxQptmTotal = _SonusIuaAsStatusRxQptmTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 9),
    _SonusIuaAsStatusRxQptmTotal_Type()
)
sonusIuaAsStatusRxQptmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxQptmTotal.setStatus("current")
_SonusIuaAsStatusTxQptmTotal_Type = Integer32
_SonusIuaAsStatusTxQptmTotal_Object = MibTableColumn
sonusIuaAsStatusTxQptmTotal = _SonusIuaAsStatusTxQptmTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 10),
    _SonusIuaAsStatusTxQptmTotal_Type()
)
sonusIuaAsStatusTxQptmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxQptmTotal.setStatus("current")
_SonusIuaAsStatusRxAspSmTotal_Type = Integer32
_SonusIuaAsStatusRxAspSmTotal_Object = MibTableColumn
sonusIuaAsStatusRxAspSmTotal = _SonusIuaAsStatusRxAspSmTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 11),
    _SonusIuaAsStatusRxAspSmTotal_Type()
)
sonusIuaAsStatusRxAspSmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxAspSmTotal.setStatus("current")
_SonusIuaAsStatusTxAspSmTotal_Type = Integer32
_SonusIuaAsStatusTxAspSmTotal_Object = MibTableColumn
sonusIuaAsStatusTxAspSmTotal = _SonusIuaAsStatusTxAspSmTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 12),
    _SonusIuaAsStatusTxAspSmTotal_Type()
)
sonusIuaAsStatusTxAspSmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxAspSmTotal.setStatus("current")
_SonusIuaAsStatusRxAspTmTotal_Type = Integer32
_SonusIuaAsStatusRxAspTmTotal_Object = MibTableColumn
sonusIuaAsStatusRxAspTmTotal = _SonusIuaAsStatusRxAspTmTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 13),
    _SonusIuaAsStatusRxAspTmTotal_Type()
)
sonusIuaAsStatusRxAspTmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxAspTmTotal.setStatus("current")
_SonusIuaAsStatusTxAspTmTotal_Type = Integer32
_SonusIuaAsStatusTxAspTmTotal_Object = MibTableColumn
sonusIuaAsStatusTxAspTmTotal = _SonusIuaAsStatusTxAspTmTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 14),
    _SonusIuaAsStatusTxAspTmTotal_Type()
)
sonusIuaAsStatusTxAspTmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxAspTmTotal.setStatus("current")
_SonusIuaAsStatusTxTOTotal_Type = Integer32
_SonusIuaAsStatusTxTOTotal_Object = MibTableColumn
sonusIuaAsStatusTxTOTotal = _SonusIuaAsStatusTxTOTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 15),
    _SonusIuaAsStatusTxTOTotal_Type()
)
sonusIuaAsStatusTxTOTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxTOTotal.setStatus("current")
_SonusIuaAsStatusTxAbortTotal_Type = Integer32
_SonusIuaAsStatusTxAbortTotal_Object = MibTableColumn
sonusIuaAsStatusTxAbortTotal = _SonusIuaAsStatusTxAbortTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 16),
    _SonusIuaAsStatusTxAbortTotal_Type()
)
sonusIuaAsStatusTxAbortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxAbortTotal.setStatus("current")
_SonusIuaAsStatusTxErrTotal_Type = Integer32
_SonusIuaAsStatusTxErrTotal_Object = MibTableColumn
sonusIuaAsStatusTxErrTotal = _SonusIuaAsStatusTxErrTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 17),
    _SonusIuaAsStatusTxErrTotal_Type()
)
sonusIuaAsStatusTxErrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxErrTotal.setStatus("current")
_SonusIuaAsStatusRxUnknownTotal_Type = Integer32
_SonusIuaAsStatusRxUnknownTotal_Object = MibTableColumn
sonusIuaAsStatusRxUnknownTotal = _SonusIuaAsStatusRxUnknownTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 20),
    _SonusIuaAsStatusRxUnknownTotal_Type()
)
sonusIuaAsStatusRxUnknownTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxUnknownTotal.setStatus("current")
_SonusIuaAsStatusRxOverLenTotal_Type = Integer32
_SonusIuaAsStatusRxOverLenTotal_Object = MibTableColumn
sonusIuaAsStatusRxOverLenTotal = _SonusIuaAsStatusRxOverLenTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 21),
    _SonusIuaAsStatusRxOverLenTotal_Type()
)
sonusIuaAsStatusRxOverLenTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxOverLenTotal.setStatus("current")
_SonusIuaAsStatusRxAspUp_Type = Integer32
_SonusIuaAsStatusRxAspUp_Object = MibTableColumn
sonusIuaAsStatusRxAspUp = _SonusIuaAsStatusRxAspUp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 24),
    _SonusIuaAsStatusRxAspUp_Type()
)
sonusIuaAsStatusRxAspUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxAspUp.setStatus("current")
_SonusIuaAsStatusRxAspDown_Type = Integer32
_SonusIuaAsStatusRxAspDown_Object = MibTableColumn
sonusIuaAsStatusRxAspDown = _SonusIuaAsStatusRxAspDown_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 25),
    _SonusIuaAsStatusRxAspDown_Type()
)
sonusIuaAsStatusRxAspDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxAspDown.setStatus("current")
_SonusIuaAsStatusRxAspActive_Type = Integer32
_SonusIuaAsStatusRxAspActive_Object = MibTableColumn
sonusIuaAsStatusRxAspActive = _SonusIuaAsStatusRxAspActive_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 26),
    _SonusIuaAsStatusRxAspActive_Type()
)
sonusIuaAsStatusRxAspActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxAspActive.setStatus("current")
_SonusIuaAsStatusRxAspInactive_Type = Integer32
_SonusIuaAsStatusRxAspInactive_Object = MibTableColumn
sonusIuaAsStatusRxAspInactive = _SonusIuaAsStatusRxAspInactive_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 28),
    _SonusIuaAsStatusRxAspInactive_Type()
)
sonusIuaAsStatusRxAspInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxAspInactive.setStatus("current")
_SonusIuaAsStatusRxEstReq_Type = Integer32
_SonusIuaAsStatusRxEstReq_Object = MibTableColumn
sonusIuaAsStatusRxEstReq = _SonusIuaAsStatusRxEstReq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 29),
    _SonusIuaAsStatusRxEstReq_Type()
)
sonusIuaAsStatusRxEstReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxEstReq.setStatus("current")
_SonusIuaAsStatusRxRelReq_Type = Integer32
_SonusIuaAsStatusRxRelReq_Object = MibTableColumn
sonusIuaAsStatusRxRelReq = _SonusIuaAsStatusRxRelReq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 30),
    _SonusIuaAsStatusRxRelReq_Type()
)
sonusIuaAsStatusRxRelReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxRelReq.setStatus("current")
_SonusIuaAsStatusRxEstRsp_Type = Integer32
_SonusIuaAsStatusRxEstRsp_Object = MibTableColumn
sonusIuaAsStatusRxEstRsp = _SonusIuaAsStatusRxEstRsp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 31),
    _SonusIuaAsStatusRxEstRsp_Type()
)
sonusIuaAsStatusRxEstRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxEstRsp.setStatus("current")
_SonusIuaAsStatusRxRelRsp_Type = Integer32
_SonusIuaAsStatusRxRelRsp_Object = MibTableColumn
sonusIuaAsStatusRxRelRsp = _SonusIuaAsStatusRxRelRsp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 32),
    _SonusIuaAsStatusRxRelRsp_Type()
)
sonusIuaAsStatusRxRelRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxRelRsp.setStatus("current")
_SonusIuaAsStatusRxDataReq_Type = Integer32
_SonusIuaAsStatusRxDataReq_Object = MibTableColumn
sonusIuaAsStatusRxDataReq = _SonusIuaAsStatusRxDataReq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 33),
    _SonusIuaAsStatusRxDataReq_Type()
)
sonusIuaAsStatusRxDataReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxDataReq.setStatus("current")
_SonusIuaAsStatusRxDataIndAck_Type = Integer32
_SonusIuaAsStatusRxDataIndAck_Object = MibTableColumn
sonusIuaAsStatusRxDataIndAck = _SonusIuaAsStatusRxDataIndAck_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 34),
    _SonusIuaAsStatusRxDataIndAck_Type()
)
sonusIuaAsStatusRxDataIndAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxDataIndAck.setStatus("current")
_SonusIuaAsStatusTxAspUpAck_Type = Integer32
_SonusIuaAsStatusTxAspUpAck_Object = MibTableColumn
sonusIuaAsStatusTxAspUpAck = _SonusIuaAsStatusTxAspUpAck_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 35),
    _SonusIuaAsStatusTxAspUpAck_Type()
)
sonusIuaAsStatusTxAspUpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxAspUpAck.setStatus("current")
_SonusIuaAsStatusTxAspDownAck_Type = Integer32
_SonusIuaAsStatusTxAspDownAck_Object = MibTableColumn
sonusIuaAsStatusTxAspDownAck = _SonusIuaAsStatusTxAspDownAck_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 36),
    _SonusIuaAsStatusTxAspDownAck_Type()
)
sonusIuaAsStatusTxAspDownAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxAspDownAck.setStatus("current")
_SonusIuaAsStatusTxAspActiveAck_Type = Integer32
_SonusIuaAsStatusTxAspActiveAck_Object = MibTableColumn
sonusIuaAsStatusTxAspActiveAck = _SonusIuaAsStatusTxAspActiveAck_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 37),
    _SonusIuaAsStatusTxAspActiveAck_Type()
)
sonusIuaAsStatusTxAspActiveAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxAspActiveAck.setStatus("current")
_SonusIuaAsStatusTxAspInactiveAck_Type = Integer32
_SonusIuaAsStatusTxAspInactiveAck_Object = MibTableColumn
sonusIuaAsStatusTxAspInactiveAck = _SonusIuaAsStatusTxAspInactiveAck_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 38),
    _SonusIuaAsStatusTxAspInactiveAck_Type()
)
sonusIuaAsStatusTxAspInactiveAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxAspInactiveAck.setStatus("current")
_SonusIuaAsStatusTxEstConfirm_Type = Integer32
_SonusIuaAsStatusTxEstConfirm_Object = MibTableColumn
sonusIuaAsStatusTxEstConfirm = _SonusIuaAsStatusTxEstConfirm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 39),
    _SonusIuaAsStatusTxEstConfirm_Type()
)
sonusIuaAsStatusTxEstConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxEstConfirm.setStatus("current")
_SonusIuaAsStatusTxRelConfirm_Type = Integer32
_SonusIuaAsStatusTxRelConfirm_Object = MibTableColumn
sonusIuaAsStatusTxRelConfirm = _SonusIuaAsStatusTxRelConfirm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 40),
    _SonusIuaAsStatusTxRelConfirm_Type()
)
sonusIuaAsStatusTxRelConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxRelConfirm.setStatus("current")
_SonusIuaAsStatusTxEstInd_Type = Integer32
_SonusIuaAsStatusTxEstInd_Object = MibTableColumn
sonusIuaAsStatusTxEstInd = _SonusIuaAsStatusTxEstInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 41),
    _SonusIuaAsStatusTxEstInd_Type()
)
sonusIuaAsStatusTxEstInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxEstInd.setStatus("current")
_SonusIuaAsStatusTxRelInd_Type = Integer32
_SonusIuaAsStatusTxRelInd_Object = MibTableColumn
sonusIuaAsStatusTxRelInd = _SonusIuaAsStatusTxRelInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 42),
    _SonusIuaAsStatusTxRelInd_Type()
)
sonusIuaAsStatusTxRelInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxRelInd.setStatus("current")
_SonusIuaAsStatusTxDataReqAck_Type = Integer32
_SonusIuaAsStatusTxDataReqAck_Object = MibTableColumn
sonusIuaAsStatusTxDataReqAck = _SonusIuaAsStatusTxDataReqAck_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 43),
    _SonusIuaAsStatusTxDataReqAck_Type()
)
sonusIuaAsStatusTxDataReqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxDataReqAck.setStatus("current")
_SonusIuaAsStatusTxDataInd_Type = Integer32
_SonusIuaAsStatusTxDataInd_Object = MibTableColumn
sonusIuaAsStatusTxDataInd = _SonusIuaAsStatusTxDataInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 44),
    _SonusIuaAsStatusTxDataInd_Type()
)
sonusIuaAsStatusTxDataInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxDataInd.setStatus("current")
_SonusIuaAsStatusRxMaxByteCnt_Type = Integer32
_SonusIuaAsStatusRxMaxByteCnt_Object = MibTableColumn
sonusIuaAsStatusRxMaxByteCnt = _SonusIuaAsStatusRxMaxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 45),
    _SonusIuaAsStatusRxMaxByteCnt_Type()
)
sonusIuaAsStatusRxMaxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxMaxByteCnt.setStatus("current")
_SonusIuaAsStatusTxMaxByteCnt_Type = Integer32
_SonusIuaAsStatusTxMaxByteCnt_Object = MibTableColumn
sonusIuaAsStatusTxMaxByteCnt = _SonusIuaAsStatusTxMaxByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 46),
    _SonusIuaAsStatusTxMaxByteCnt_Type()
)
sonusIuaAsStatusTxMaxByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxMaxByteCnt.setStatus("current")
_SonusIuaAsStatusRxError_Type = Integer32
_SonusIuaAsStatusRxError_Object = MibTableColumn
sonusIuaAsStatusRxError = _SonusIuaAsStatusRxError_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 47),
    _SonusIuaAsStatusRxError_Type()
)
sonusIuaAsStatusRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxError.setStatus("current")
_SonusIuaAsStatusTxError_Type = Integer32
_SonusIuaAsStatusTxError_Object = MibTableColumn
sonusIuaAsStatusTxError = _SonusIuaAsStatusTxError_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 48),
    _SonusIuaAsStatusTxError_Type()
)
sonusIuaAsStatusTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxError.setStatus("current")
_SonusIuaAsStatusRxNotify_Type = Integer32
_SonusIuaAsStatusRxNotify_Object = MibTableColumn
sonusIuaAsStatusRxNotify = _SonusIuaAsStatusRxNotify_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 49),
    _SonusIuaAsStatusRxNotify_Type()
)
sonusIuaAsStatusRxNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxNotify.setStatus("current")
_SonusIuaAsStatusTxNotify_Type = Integer32
_SonusIuaAsStatusTxNotify_Object = MibTableColumn
sonusIuaAsStatusTxNotify = _SonusIuaAsStatusTxNotify_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 50),
    _SonusIuaAsStatusTxNotify_Type()
)
sonusIuaAsStatusTxNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxNotify.setStatus("current")


class _SonusIuaAsStatusActiveAsp_Type(DisplayString):
    """Custom type sonusIuaAsStatusActiveAsp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusIuaAsStatusActiveAsp_Type.__name__ = "DisplayString"
_SonusIuaAsStatusActiveAsp_Object = MibTableColumn
sonusIuaAsStatusActiveAsp = _SonusIuaAsStatusActiveAsp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 51),
    _SonusIuaAsStatusActiveAsp_Type()
)
sonusIuaAsStatusActiveAsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusActiveAsp.setStatus("current")


class _SonusIuaAsStatusSoftwareVersion_Type(DisplayString):
    """Custom type sonusIuaAsStatusSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SonusIuaAsStatusSoftwareVersion_Type.__name__ = "DisplayString"
_SonusIuaAsStatusSoftwareVersion_Object = MibTableColumn
sonusIuaAsStatusSoftwareVersion = _SonusIuaAsStatusSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 52),
    _SonusIuaAsStatusSoftwareVersion_Type()
)
sonusIuaAsStatusSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusSoftwareVersion.setStatus("current")
_SonusIuaAsStatusRxMgmtTotal_Type = Integer32
_SonusIuaAsStatusRxMgmtTotal_Object = MibTableColumn
sonusIuaAsStatusRxMgmtTotal = _SonusIuaAsStatusRxMgmtTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 53),
    _SonusIuaAsStatusRxMgmtTotal_Type()
)
sonusIuaAsStatusRxMgmtTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusRxMgmtTotal.setStatus("current")
_SonusIuaAsStatusTxMgmtTotal_Type = Integer32
_SonusIuaAsStatusTxMgmtTotal_Object = MibTableColumn
sonusIuaAsStatusTxMgmtTotal = _SonusIuaAsStatusTxMgmtTotal_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 15, 1, 54),
    _SonusIuaAsStatusTxMgmtTotal_Type()
)
sonusIuaAsStatusTxMgmtTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAsStatusTxMgmtTotal.setStatus("current")
_SonusIuaAspStatusTable_Object = MibTable
sonusIuaAspStatusTable = _SonusIuaAspStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 16)
)
if mibBuilder.loadTexts:
    sonusIuaAspStatusTable.setStatus("current")
_SonusIuaAspStatusEntry_Object = MibTableRow
sonusIuaAspStatusEntry = _SonusIuaAspStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 16, 1)
)
sonusIuaAspStatusEntry.setIndexNames(
    (0, "SONUS-MGCP-SERVICES-MIB", "sonusIuaAspStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusIuaAspStatusEntry.setStatus("current")
_SonusIuaAspStatusIndex_Type = Integer32
_SonusIuaAspStatusIndex_Object = MibTableColumn
sonusIuaAspStatusIndex = _SonusIuaAspStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 16, 1, 1),
    _SonusIuaAspStatusIndex_Type()
)
sonusIuaAspStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAspStatusIndex.setStatus("current")
_SonusIuaAspStatusNumConnections_Type = Integer32
_SonusIuaAspStatusNumConnections_Object = MibTableColumn
sonusIuaAspStatusNumConnections = _SonusIuaAspStatusNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 16, 1, 2),
    _SonusIuaAspStatusNumConnections_Type()
)
sonusIuaAspStatusNumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAspStatusNumConnections.setStatus("current")
_SonusIuaAspStatusNumAppServers_Type = Integer32
_SonusIuaAspStatusNumAppServers_Object = MibTableColumn
sonusIuaAspStatusNumAppServers = _SonusIuaAspStatusNumAppServers_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 16, 1, 3),
    _SonusIuaAspStatusNumAppServers_Type()
)
sonusIuaAspStatusNumAppServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAspStatusNumAppServers.setStatus("current")


class _SonusIuaAspStatusStatus_Type(Integer32):
    """Custom type sonusIuaAspStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_SonusIuaAspStatusStatus_Type.__name__ = "Integer32"
_SonusIuaAspStatusStatus_Object = MibTableColumn
sonusIuaAspStatusStatus = _SonusIuaAspStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 1, 16, 1, 4),
    _SonusIuaAspStatusStatus_Type()
)
sonusIuaAspStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIuaAspStatusStatus.setStatus("current")
_SonusMgcpServicesMIBNotifications_ObjectIdentity = ObjectIdentity
sonusMgcpServicesMIBNotifications = _SonusMgcpServicesMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2)
)
_SonusMgcpServicesMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusMgcpServicesMIBNotificationsPrefix = _SonusMgcpServicesMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0)
)
_SonusMgcpServicesMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusMgcpServicesMIBNotificationsObjects = _SonusMgcpServicesMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 1)
)

# Managed Objects groups


# Notification objects

sonusMgcpSessionConnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 1)
)
sonusMgcpSessionConnectNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusMgcpSessionName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusMgcpSessionConnectNotification.setStatus(
        "current"
    )

sonusMgcpSessionDisconnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 2)
)
sonusMgcpSessionDisconnectNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusMgcpSessionName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusMgcpSessionDisconnectNotification.setStatus(
        "current"
    )

sonusMgcpCallAgntConnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 3)
)
sonusMgcpCallAgntConnectNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusMgcpSessionName"),
        ("SONUS-MGCP-SERVICES-MIB", "sonusMgcpCallAgntName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusMgcpCallAgntConnectNotification.setStatus(
        "current"
    )

sonusMgcpCallAgntDisconnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 4)
)
sonusMgcpCallAgntDisconnectNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusMgcpSessionName"),
        ("SONUS-MGCP-SERVICES-MIB", "sonusMgcpCallAgntName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusMgcpCallAgntDisconnectNotification.setStatus(
        "current"
    )

sonusIuaAsDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 5)
)
sonusIuaAsDownNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusIuaAsName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIuaAsDownNotification.setStatus(
        "current"
    )

sonusIuaAsInactiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 6)
)
sonusIuaAsInactiveNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusIuaAsName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIuaAsInactiveNotification.setStatus(
        "current"
    )

sonusIuaAsActiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 7)
)
sonusIuaAsActiveNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusIuaAsName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIuaAsActiveNotification.setStatus(
        "current"
    )

sonusIuaAsPendingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 8)
)
sonusIuaAsPendingNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusIuaAsName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIuaAsPendingNotification.setStatus(
        "current"
    )

sonusIuaAspDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 9)
)
sonusIuaAspDownNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusIuaAspName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIuaAspDownNotification.setStatus(
        "current"
    )

sonusIuaAspUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 12, 2, 0, 10)
)
sonusIuaAspUpNotification.setObjects(
      *(("SONUS-MGCP-SERVICES-MIB", "sonusIuaAspName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIuaAspUpNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-MGCP-SERVICES-MIB",
    **{"sonusMgcpServicesMIB": sonusMgcpServicesMIB,
       "sonusMgcpServicesMIBObjects": sonusMgcpServicesMIBObjects,
       "sonusMgcpGateway": sonusMgcpGateway,
       "sonusMgcpGatewayPort": sonusMgcpGatewayPort,
       "sonusMgcpGatewayRxThrottle": sonusMgcpGatewayRxThrottle,
       "sonusMgcpGatewayMaxReXmit": sonusMgcpGatewayMaxReXmit,
       "sonusMgcpGatewayCmdTimeout": sonusMgcpGatewayCmdTimeout,
       "sonusMgcpGatewayRspTimeout": sonusMgcpGatewayRspTimeout,
       "sonusMgcpGatewayCriticalTimeout": sonusMgcpGatewayCriticalTimeout,
       "sonusMgcpGatewayPartialTimeout": sonusMgcpGatewayPartialTimeout,
       "sonusMgcpGatewayMsgPiggyBacking": sonusMgcpGatewayMsgPiggyBacking,
       "sonusMgcpSession": sonusMgcpSession,
       "sonusMgcpSessionNextIndex": sonusMgcpSessionNextIndex,
       "sonusMgcpSessionTable": sonusMgcpSessionTable,
       "sonusMgcpSessionEntry": sonusMgcpSessionEntry,
       "sonusMgcpSessionIndex": sonusMgcpSessionIndex,
       "sonusMgcpSessionName": sonusMgcpSessionName,
       "sonusMgcpSessionMode": sonusMgcpSessionMode,
       "sonusMgcpSessionState": sonusMgcpSessionState,
       "sonusMgcpSessionRowStatus": sonusMgcpSessionRowStatus,
       "sonusMgcpSessionServProfileName": sonusMgcpSessionServProfileName,
       "sonusMgcpCallAgnt": sonusMgcpCallAgnt,
       "sonusMgcpCallAgntNextIndex": sonusMgcpCallAgntNextIndex,
       "sonusMgcpCallAgntTable": sonusMgcpCallAgntTable,
       "sonusMgcpCallAgntEntry": sonusMgcpCallAgntEntry,
       "sonusMgcpCallAgntIndex": sonusMgcpCallAgntIndex,
       "sonusMgcpCallAgntName": sonusMgcpCallAgntName,
       "sonusMgcpCallAgntState": sonusMgcpCallAgntState,
       "sonusMgcpCallAgntRowStatus": sonusMgcpCallAgntRowStatus,
       "sonusMgcpCallAgntSessionName": sonusMgcpCallAgntSessionName,
       "sonusMgcpCallAgntDefNotEnt": sonusMgcpCallAgntDefNotEnt,
       "sonusMgcpConnectionTable": sonusMgcpConnectionTable,
       "sonusMgcpConnectionEntry": sonusMgcpConnectionEntry,
       "sonusMgcpConnectionIpaddr": sonusMgcpConnectionIpaddr,
       "sonusMgcpConnectionPort": sonusMgcpConnectionPort,
       "sonusMgcpConnectionState": sonusMgcpConnectionState,
       "sonusMgcpConnectionRowStatus": sonusMgcpConnectionRowStatus,
       "sonusMgcpConnectionCallAgntName": sonusMgcpConnectionCallAgntName,
       "sonusMgcpSessionStatusTable": sonusMgcpSessionStatusTable,
       "sonusMgcpSessionStatusEntry": sonusMgcpSessionStatusEntry,
       "sonusMgcpSessionStatusIndex": sonusMgcpSessionStatusIndex,
       "sonusMgcpSessionStatusMajorVersion": sonusMgcpSessionStatusMajorVersion,
       "sonusMgcpSessionStatusMinorVersion": sonusMgcpSessionStatusMinorVersion,
       "sonusMgcpSessionStatusNumCallAgnts": sonusMgcpSessionStatusNumCallAgnts,
       "sonusMgcpSessionStatusStatus": sonusMgcpSessionStatusStatus,
       "sonusMgcpSessionStatusRxMsgTotal": sonusMgcpSessionStatusRxMsgTotal,
       "sonusMgcpSessionStatusTxMsgTotal": sonusMgcpSessionStatusTxMsgTotal,
       "sonusMgcpSessionStatusRxCmdTotal": sonusMgcpSessionStatusRxCmdTotal,
       "sonusMgcpSessionStatusRxRspTotal": sonusMgcpSessionStatusRxRspTotal,
       "sonusMgcpSessionStatusTxCmdTotal": sonusMgcpSessionStatusTxCmdTotal,
       "sonusMgcpSessionStatusTxRspTotal": sonusMgcpSessionStatusTxRspTotal,
       "sonusMgcpSessionStatusTxTOTotal": sonusMgcpSessionStatusTxTOTotal,
       "sonusMgcpSessionStatusTxAbortTotal": sonusMgcpSessionStatusTxAbortTotal,
       "sonusMgcpSessionStatusTxErrTotal": sonusMgcpSessionStatusTxErrTotal,
       "sonusMgcpSessionStatusRxTOTotal": sonusMgcpSessionStatusRxTOTotal,
       "sonusMgcpSessionStatusRxDupCmdTotal": sonusMgcpSessionStatusRxDupCmdTotal,
       "sonusMgcpSessionStatusRxDupRspTotal": sonusMgcpSessionStatusRxDupRspTotal,
       "sonusMgcpSessionStatusRxRspErrTotal": sonusMgcpSessionStatusRxRspErrTotal,
       "sonusMgcpSessionStatusRxRspInPTotal": sonusMgcpSessionStatusRxRspInPTotal,
       "sonusMgcpSessionStatusRxUnknownTotal": sonusMgcpSessionStatusRxUnknownTotal,
       "sonusMgcpSessionStatusRxOverLenTotal": sonusMgcpSessionStatusRxOverLenTotal,
       "sonusMgcpSessionStatusRxMaxByteCnt": sonusMgcpSessionStatusRxMaxByteCnt,
       "sonusMgcpSessionStatusRxMaxPigBCnt": sonusMgcpSessionStatusRxMaxPigBCnt,
       "sonusMgcpSessionStatusTxMaxByteCnt": sonusMgcpSessionStatusTxMaxByteCnt,
       "sonusMgcpSessionStatusTxMaxPigBCnt": sonusMgcpSessionStatusTxMaxPigBCnt,
       "sonusMgcpSessionStatusTxMaxCmdPnd": sonusMgcpSessionStatusTxMaxCmdPnd,
       "sonusMgcpSessionStatusTxMaxRspPnd": sonusMgcpSessionStatusTxMaxRspPnd,
       "sonusMgcpSessionStatusRxCmdThrotCnt": sonusMgcpSessionStatusRxCmdThrotCnt,
       "sonusMgcpSessionStatusRxErrorTotal": sonusMgcpSessionStatusRxErrorTotal,
       "sonusMgcpSessionStatusTxErrorTotal": sonusMgcpSessionStatusTxErrorTotal,
       "sonusMgcpSessionStatusRxCRCX": sonusMgcpSessionStatusRxCRCX,
       "sonusMgcpSessionStatusRxCRCXL": sonusMgcpSessionStatusRxCRCXL,
       "sonusMgcpSessionStatusRxMDCX": sonusMgcpSessionStatusRxMDCX,
       "sonusMgcpSessionStatusRxDLCX": sonusMgcpSessionStatusRxDLCX,
       "sonusMgcpSessionStatusRxRQNT": sonusMgcpSessionStatusRxRQNT,
       "sonusMgcpSessionStatusRxEPCF": sonusMgcpSessionStatusRxEPCF,
       "sonusMgcpSessionStatusRxAUDT": sonusMgcpSessionStatusRxAUDT,
       "sonusMgcpSessionStatusTxCRCXRsp": sonusMgcpSessionStatusTxCRCXRsp,
       "sonusMgcpSessionStatusTxCRCXRspL": sonusMgcpSessionStatusTxCRCXRspL,
       "sonusMgcpSessionStatusTxCRCXRspErr": sonusMgcpSessionStatusTxCRCXRspErr,
       "sonusMgcpSessionStatusTxMDCXRsp": sonusMgcpSessionStatusTxMDCXRsp,
       "sonusMgcpSessionStatusTxMDCXRspErr": sonusMgcpSessionStatusTxMDCXRspErr,
       "sonusMgcpSessionStatusTxDLCXRsp": sonusMgcpSessionStatusTxDLCXRsp,
       "sonusMgcpSessionStatusTxDLCXRspErr": sonusMgcpSessionStatusTxDLCXRspErr,
       "sonusMgcpSessionStatusTxAUDTRsp": sonusMgcpSessionStatusTxAUDTRsp,
       "sonusMgcpSessionStatusTxAUDTRspErr": sonusMgcpSessionStatusTxAUDTRspErr,
       "sonusMgcpSessionStatusTxRQNTRsp": sonusMgcpSessionStatusTxRQNTRsp,
       "sonusMgcpSessionStatusTxRQNTRspErr": sonusMgcpSessionStatusTxRQNTRspErr,
       "sonusMgcpSessionStatusTxRSIPCmd": sonusMgcpSessionStatusTxRSIPCmd,
       "sonusMgcpSessionStatusTxNTFYCmd": sonusMgcpSessionStatusTxNTFYCmd,
       "sonusMgcpSessionStatusTxDLCXCmd": sonusMgcpSessionStatusTxDLCXCmd,
       "sonusMgcpCallAgntStatusTable": sonusMgcpCallAgntStatusTable,
       "sonusMgcpCallAgntStatusEntry": sonusMgcpCallAgntStatusEntry,
       "sonusMgcpCallAgntStatusIndex": sonusMgcpCallAgntStatusIndex,
       "sonusMgcpCallAgntStatusNumConnections": sonusMgcpCallAgntStatusNumConnections,
       "sonusMgcpCallAgntStatusStatus": sonusMgcpCallAgntStatusStatus,
       "sonusMgcpServProfile": sonusMgcpServProfile,
       "sonusMgcpServProfileNextIndex": sonusMgcpServProfileNextIndex,
       "sonusMgcpServProfileTable": sonusMgcpServProfileTable,
       "sonusMgcpServProfileEntry": sonusMgcpServProfileEntry,
       "sonusMgcpServProfileIndex": sonusMgcpServProfileIndex,
       "sonusMgcpServProfileName": sonusMgcpServProfileName,
       "sonusMgcpServProfileState": sonusMgcpServProfileState,
       "sonusMgcpServProfileRowStatus": sonusMgcpServProfileRowStatus,
       "sonusMgcpServProfileEncodeType": sonusMgcpServProfileEncodeType,
       "sonusMgcpServProfilePacketPeriod": sonusMgcpServProfilePacketPeriod,
       "sonusMgcpServProfileTypeOfService": sonusMgcpServProfileTypeOfService,
       "sonusMgcpServProfileEchoCancellation": sonusMgcpServProfileEchoCancellation,
       "sonusMgcpServProfileSilenceSuppression": sonusMgcpServProfileSilenceSuppression,
       "sonusIuaGateway": sonusIuaGateway,
       "sonusIuaGatewayPort": sonusIuaGatewayPort,
       "sonusIuaGatewayHbTimeout": sonusIuaGatewayHbTimeout,
       "sonusIuaGatewayASPendingTimeout": sonusIuaGatewayASPendingTimeout,
       "sonusIuaGatewayEstRelIndRetry": sonusIuaGatewayEstRelIndRetry,
       "sonusIuaGatewayEstRelIndTimeout": sonusIuaGatewayEstRelIndTimeout,
       "sonusIuaGatewayDataIndTimeout": sonusIuaGatewayDataIndTimeout,
       "sonusIuaGatewayDataIndRetryExp": sonusIuaGatewayDataIndRetryExp,
       "sonusIuaGatewayDataIndWindowSize": sonusIuaGatewayDataIndWindowSize,
       "sonusIuaGatewayDataIndMaxTimeout": sonusIuaGatewayDataIndMaxTimeout,
       "sonusIuaAs": sonusIuaAs,
       "sonusIuaAsNextIndex": sonusIuaAsNextIndex,
       "sonusIuaAsTable": sonusIuaAsTable,
       "sonusIuaAsEntry": sonusIuaAsEntry,
       "sonusIuaAsIndex": sonusIuaAsIndex,
       "sonusIuaAsName": sonusIuaAsName,
       "sonusIuaAsMode": sonusIuaAsMode,
       "sonusIuaAsState": sonusIuaAsState,
       "sonusIuaAsRowStatus": sonusIuaAsRowStatus,
       "sonusIuaAsp": sonusIuaAsp,
       "sonusIuaAspNextIndex": sonusIuaAspNextIndex,
       "sonusIuaAspTable": sonusIuaAspTable,
       "sonusIuaAspEntry": sonusIuaAspEntry,
       "sonusIuaAspIndex": sonusIuaAspIndex,
       "sonusIuaAspName": sonusIuaAspName,
       "sonusIuaAspState": sonusIuaAspState,
       "sonusIuaAspRowStatus": sonusIuaAspRowStatus,
       "sonusIuaConnectionTable": sonusIuaConnectionTable,
       "sonusIuaConnectionEntry": sonusIuaConnectionEntry,
       "sonusIuaConnectionIpaddr": sonusIuaConnectionIpaddr,
       "sonusIuaConnectionPort": sonusIuaConnectionPort,
       "sonusIuaConnectionState": sonusIuaConnectionState,
       "sonusIuaConnectionRowStatus": sonusIuaConnectionRowStatus,
       "sonusIuaConnectionAspName": sonusIuaConnectionAspName,
       "sonusIuaInterfaceTable": sonusIuaInterfaceTable,
       "sonusIuaInterfaceEntry": sonusIuaInterfaceEntry,
       "sonusIuaInterfaceShelf": sonusIuaInterfaceShelf,
       "sonusIuaInterfaceSlot": sonusIuaInterfaceSlot,
       "sonusIuaInterfacePort": sonusIuaInterfacePort,
       "sonusIuaInterfaceTimeslot": sonusIuaInterfaceTimeslot,
       "sonusIuaInterfaceRowStatus": sonusIuaInterfaceRowStatus,
       "sonusIuaInterfaceAsName": sonusIuaInterfaceAsName,
       "sonusIuaAsaTable": sonusIuaAsaTable,
       "sonusIuaAsaEntry": sonusIuaAsaEntry,
       "sonusIuaAsaAsIndex": sonusIuaAsaAsIndex,
       "sonusIuaAsaAspIndex": sonusIuaAsaAspIndex,
       "sonusIuaAsaRowStatus": sonusIuaAsaRowStatus,
       "sonusIuaAsStatusTable": sonusIuaAsStatusTable,
       "sonusIuaAsStatusEntry": sonusIuaAsStatusEntry,
       "sonusIuaAsStatusIndex": sonusIuaAsStatusIndex,
       "sonusIuaAsStatusMessageVersion": sonusIuaAsStatusMessageVersion,
       "sonusIuaAsStatusNumAsps": sonusIuaAsStatusNumAsps,
       "sonusIuaAsStatusNumInterfaces": sonusIuaAsStatusNumInterfaces,
       "sonusIuaAsStatusStatus": sonusIuaAsStatusStatus,
       "sonusIuaAsStatusRxMsgTotal": sonusIuaAsStatusRxMsgTotal,
       "sonusIuaAsStatusTxMsgTotal": sonusIuaAsStatusTxMsgTotal,
       "sonusIuaAsStatusRxQptmTotal": sonusIuaAsStatusRxQptmTotal,
       "sonusIuaAsStatusTxQptmTotal": sonusIuaAsStatusTxQptmTotal,
       "sonusIuaAsStatusRxAspSmTotal": sonusIuaAsStatusRxAspSmTotal,
       "sonusIuaAsStatusTxAspSmTotal": sonusIuaAsStatusTxAspSmTotal,
       "sonusIuaAsStatusRxAspTmTotal": sonusIuaAsStatusRxAspTmTotal,
       "sonusIuaAsStatusTxAspTmTotal": sonusIuaAsStatusTxAspTmTotal,
       "sonusIuaAsStatusTxTOTotal": sonusIuaAsStatusTxTOTotal,
       "sonusIuaAsStatusTxAbortTotal": sonusIuaAsStatusTxAbortTotal,
       "sonusIuaAsStatusTxErrTotal": sonusIuaAsStatusTxErrTotal,
       "sonusIuaAsStatusRxUnknownTotal": sonusIuaAsStatusRxUnknownTotal,
       "sonusIuaAsStatusRxOverLenTotal": sonusIuaAsStatusRxOverLenTotal,
       "sonusIuaAsStatusRxAspUp": sonusIuaAsStatusRxAspUp,
       "sonusIuaAsStatusRxAspDown": sonusIuaAsStatusRxAspDown,
       "sonusIuaAsStatusRxAspActive": sonusIuaAsStatusRxAspActive,
       "sonusIuaAsStatusRxAspInactive": sonusIuaAsStatusRxAspInactive,
       "sonusIuaAsStatusRxEstReq": sonusIuaAsStatusRxEstReq,
       "sonusIuaAsStatusRxRelReq": sonusIuaAsStatusRxRelReq,
       "sonusIuaAsStatusRxEstRsp": sonusIuaAsStatusRxEstRsp,
       "sonusIuaAsStatusRxRelRsp": sonusIuaAsStatusRxRelRsp,
       "sonusIuaAsStatusRxDataReq": sonusIuaAsStatusRxDataReq,
       "sonusIuaAsStatusRxDataIndAck": sonusIuaAsStatusRxDataIndAck,
       "sonusIuaAsStatusTxAspUpAck": sonusIuaAsStatusTxAspUpAck,
       "sonusIuaAsStatusTxAspDownAck": sonusIuaAsStatusTxAspDownAck,
       "sonusIuaAsStatusTxAspActiveAck": sonusIuaAsStatusTxAspActiveAck,
       "sonusIuaAsStatusTxAspInactiveAck": sonusIuaAsStatusTxAspInactiveAck,
       "sonusIuaAsStatusTxEstConfirm": sonusIuaAsStatusTxEstConfirm,
       "sonusIuaAsStatusTxRelConfirm": sonusIuaAsStatusTxRelConfirm,
       "sonusIuaAsStatusTxEstInd": sonusIuaAsStatusTxEstInd,
       "sonusIuaAsStatusTxRelInd": sonusIuaAsStatusTxRelInd,
       "sonusIuaAsStatusTxDataReqAck": sonusIuaAsStatusTxDataReqAck,
       "sonusIuaAsStatusTxDataInd": sonusIuaAsStatusTxDataInd,
       "sonusIuaAsStatusRxMaxByteCnt": sonusIuaAsStatusRxMaxByteCnt,
       "sonusIuaAsStatusTxMaxByteCnt": sonusIuaAsStatusTxMaxByteCnt,
       "sonusIuaAsStatusRxError": sonusIuaAsStatusRxError,
       "sonusIuaAsStatusTxError": sonusIuaAsStatusTxError,
       "sonusIuaAsStatusRxNotify": sonusIuaAsStatusRxNotify,
       "sonusIuaAsStatusTxNotify": sonusIuaAsStatusTxNotify,
       "sonusIuaAsStatusActiveAsp": sonusIuaAsStatusActiveAsp,
       "sonusIuaAsStatusSoftwareVersion": sonusIuaAsStatusSoftwareVersion,
       "sonusIuaAsStatusRxMgmtTotal": sonusIuaAsStatusRxMgmtTotal,
       "sonusIuaAsStatusTxMgmtTotal": sonusIuaAsStatusTxMgmtTotal,
       "sonusIuaAspStatusTable": sonusIuaAspStatusTable,
       "sonusIuaAspStatusEntry": sonusIuaAspStatusEntry,
       "sonusIuaAspStatusIndex": sonusIuaAspStatusIndex,
       "sonusIuaAspStatusNumConnections": sonusIuaAspStatusNumConnections,
       "sonusIuaAspStatusNumAppServers": sonusIuaAspStatusNumAppServers,
       "sonusIuaAspStatusStatus": sonusIuaAspStatusStatus,
       "sonusMgcpServicesMIBNotifications": sonusMgcpServicesMIBNotifications,
       "sonusMgcpServicesMIBNotificationsPrefix": sonusMgcpServicesMIBNotificationsPrefix,
       "sonusMgcpSessionConnectNotification": sonusMgcpSessionConnectNotification,
       "sonusMgcpSessionDisconnectNotification": sonusMgcpSessionDisconnectNotification,
       "sonusMgcpCallAgntConnectNotification": sonusMgcpCallAgntConnectNotification,
       "sonusMgcpCallAgntDisconnectNotification": sonusMgcpCallAgntDisconnectNotification,
       "sonusIuaAsDownNotification": sonusIuaAsDownNotification,
       "sonusIuaAsInactiveNotification": sonusIuaAsInactiveNotification,
       "sonusIuaAsActiveNotification": sonusIuaAsActiveNotification,
       "sonusIuaAsPendingNotification": sonusIuaAsPendingNotification,
       "sonusIuaAspDownNotification": sonusIuaAspDownNotification,
       "sonusIuaAspUpNotification": sonusIuaAspUpNotification,
       "sonusMgcpServicesMIBNotificationsObjects": sonusMgcpServicesMIBNotificationsObjects}
)
