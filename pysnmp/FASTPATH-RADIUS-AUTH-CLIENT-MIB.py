# SNMP MIB module (FASTPATH-RADIUS-AUTH-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-RADIUS-AUTH-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:09 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "BROADCOM-REF-MIB",
    "fastPath")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathRadius = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8)
)
fastPathRadius.setRevisions(
        ("2007-05-23 00:00",
         "2003-11-21 00:00",
         "2003-05-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentRadiusConfigGroup_ObjectIdentity = ObjectIdentity
agentRadiusConfigGroup = _AgentRadiusConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1)
)


class _AgentRadiusRetransmit_Type(Unsigned32):
    """Custom type agentRadiusRetransmit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AgentRadiusRetransmit_Type.__name__ = "Unsigned32"
_AgentRadiusRetransmit_Object = MibScalar
agentRadiusRetransmit = _AgentRadiusRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 1),
    _AgentRadiusRetransmit_Type()
)
agentRadiusRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusRetransmit.setStatus("current")


class _AgentRadiusTimeout_Type(Unsigned32):
    """Custom type agentRadiusTimeout based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentRadiusTimeout_Type.__name__ = "Unsigned32"
_AgentRadiusTimeout_Object = MibScalar
agentRadiusTimeout = _AgentRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 2),
    _AgentRadiusTimeout_Type()
)
agentRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusTimeout.setStatus("current")


class _AgentRadiusDeadTime_Type(Unsigned32):
    """Custom type agentRadiusDeadTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AgentRadiusDeadTime_Type.__name__ = "Unsigned32"
_AgentRadiusDeadTime_Object = MibScalar
agentRadiusDeadTime = _AgentRadiusDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 3),
    _AgentRadiusDeadTime_Type()
)
agentRadiusDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusDeadTime.setStatus("current")


class _AgentRadiusServerKey_Type(DisplayString):
    """Custom type agentRadiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentRadiusServerKey_Type.__name__ = "DisplayString"
_AgentRadiusServerKey_Object = MibScalar
agentRadiusServerKey = _AgentRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 4),
    _AgentRadiusServerKey_Type()
)
agentRadiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerKey.setStatus("obsolete")
_AgentRadiusSourceIPAddr_Type = IpAddress
_AgentRadiusSourceIPAddr_Object = MibScalar
agentRadiusSourceIPAddr = _AgentRadiusSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 5),
    _AgentRadiusSourceIPAddr_Type()
)
agentRadiusSourceIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusSourceIPAddr.setStatus("current")


class _AgentRadiusServerIndexNextValid_Type(Integer32):
    """Custom type agentRadiusServerIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusServerIndexNextValid_Type.__name__ = "Integer32"
_AgentRadiusServerIndexNextValid_Object = MibScalar
agentRadiusServerIndexNextValid = _AgentRadiusServerIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 6),
    _AgentRadiusServerIndexNextValid_Type()
)
agentRadiusServerIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusServerIndexNextValid.setStatus("current")
_AgentRadiusServerConfigTable_Object = MibTable
agentRadiusServerConfigTable = _AgentRadiusServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7)
)
if mibBuilder.loadTexts:
    agentRadiusServerConfigTable.setStatus("current")
_AgentRadiusServerConfigEntry_Object = MibTableRow
agentRadiusServerConfigEntry = _AgentRadiusServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1)
)
agentRadiusServerConfigEntry.setIndexNames(
    (0, "FASTPATH-RADIUS-AUTH-CLIENT-MIB", "agentRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    agentRadiusServerConfigEntry.setStatus("current")


class _AgentRadiusServerIndex_Type(Integer32):
    """Custom type agentRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusServerIndex_Type.__name__ = "Integer32"
_AgentRadiusServerIndex_Object = MibTableColumn
agentRadiusServerIndex = _AgentRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 1),
    _AgentRadiusServerIndex_Type()
)
agentRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRadiusServerIndex.setStatus("current")
_AgentRadiusServerAddress_Type = InetAddress
_AgentRadiusServerAddress_Object = MibTableColumn
agentRadiusServerAddress = _AgentRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 2),
    _AgentRadiusServerAddress_Type()
)
agentRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerAddress.setStatus("obsolete")


class _AgentRadiusServerPort_Type(Unsigned32):
    """Custom type agentRadiusServerPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentRadiusServerPort_Type.__name__ = "Unsigned32"
_AgentRadiusServerPort_Object = MibTableColumn
agentRadiusServerPort = _AgentRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 3),
    _AgentRadiusServerPort_Type()
)
agentRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerPort.setStatus("current")


class _AgentRadiusServerTimeout_Type(Unsigned32):
    """Custom type agentRadiusServerTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentRadiusServerTimeout_Type.__name__ = "Unsigned32"
_AgentRadiusServerTimeout_Object = MibTableColumn
agentRadiusServerTimeout = _AgentRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 4),
    _AgentRadiusServerTimeout_Type()
)
agentRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerTimeout.setStatus("current")


class _AgentRadiusServerRetransmit_Type(Unsigned32):
    """Custom type agentRadiusServerRetransmit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentRadiusServerRetransmit_Type.__name__ = "Unsigned32"
_AgentRadiusServerRetransmit_Object = MibTableColumn
agentRadiusServerRetransmit = _AgentRadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 5),
    _AgentRadiusServerRetransmit_Type()
)
agentRadiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerRetransmit.setStatus("current")


class _AgentRadiusServerDeadtime_Type(Unsigned32):
    """Custom type agentRadiusServerDeadtime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AgentRadiusServerDeadtime_Type.__name__ = "Unsigned32"
_AgentRadiusServerDeadtime_Object = MibTableColumn
agentRadiusServerDeadtime = _AgentRadiusServerDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 6),
    _AgentRadiusServerDeadtime_Type()
)
agentRadiusServerDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerDeadtime.setStatus("current")
_AgentRadiusServerSourceIPAddr_Type = IpAddress
_AgentRadiusServerSourceIPAddr_Object = MibTableColumn
agentRadiusServerSourceIPAddr = _AgentRadiusServerSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 7),
    _AgentRadiusServerSourceIPAddr_Type()
)
agentRadiusServerSourceIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerSourceIPAddr.setStatus("current")


class _AgentRadiusServerSecret_Type(DisplayString):
    """Custom type agentRadiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentRadiusServerSecret_Type.__name__ = "DisplayString"
_AgentRadiusServerSecret_Object = MibTableColumn
agentRadiusServerSecret = _AgentRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 8),
    _AgentRadiusServerSecret_Type()
)
agentRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerSecret.setStatus("current")


class _AgentRadiusServerPriority_Type(Unsigned32):
    """Custom type agentRadiusServerPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentRadiusServerPriority_Type.__name__ = "Unsigned32"
_AgentRadiusServerPriority_Object = MibTableColumn
agentRadiusServerPriority = _AgentRadiusServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 9),
    _AgentRadiusServerPriority_Type()
)
agentRadiusServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerPriority.setStatus("current")


class _AgentRadiusServerUsageType_Type(Integer32):
    """Custom type agentRadiusServerUsageType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("dot1x", 3),
          ("login", 2))
    )


_AgentRadiusServerUsageType_Type.__name__ = "Integer32"
_AgentRadiusServerUsageType_Object = MibTableColumn
agentRadiusServerUsageType = _AgentRadiusServerUsageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 10),
    _AgentRadiusServerUsageType_Type()
)
agentRadiusServerUsageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerUsageType.setStatus("current")
_AgentRadiusServerAddressRowStatus_Type = RowStatus
_AgentRadiusServerAddressRowStatus_Object = MibTableColumn
agentRadiusServerAddressRowStatus = _AgentRadiusServerAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 11),
    _AgentRadiusServerAddressRowStatus_Type()
)
agentRadiusServerAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerAddressRowStatus.setStatus("current")


class _AgentRadiusServerPrimaryMode_Type(Integer32):
    """Custom type agentRadiusServerPrimaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentRadiusServerPrimaryMode_Type.__name__ = "Integer32"
_AgentRadiusServerPrimaryMode_Object = MibTableColumn
agentRadiusServerPrimaryMode = _AgentRadiusServerPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 12),
    _AgentRadiusServerPrimaryMode_Type()
)
agentRadiusServerPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerPrimaryMode.setStatus("current")


class _AgentRadiusServerCurrentMode_Type(Integer32):
    """Custom type agentRadiusServerCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AgentRadiusServerCurrentMode_Type.__name__ = "Integer32"
_AgentRadiusServerCurrentMode_Object = MibTableColumn
agentRadiusServerCurrentMode = _AgentRadiusServerCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 13),
    _AgentRadiusServerCurrentMode_Type()
)
agentRadiusServerCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusServerCurrentMode.setStatus("current")


class _AgentRadiusServerMsgAuth_Type(Integer32):
    """Custom type agentRadiusServerMsgAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentRadiusServerMsgAuth_Type.__name__ = "Integer32"
_AgentRadiusServerMsgAuth_Object = MibTableColumn
agentRadiusServerMsgAuth = _AgentRadiusServerMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 14),
    _AgentRadiusServerMsgAuth_Type()
)
agentRadiusServerMsgAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerMsgAuth.setStatus("current")


class _AgentRadiusServerName_Type(DisplayString):
    """Custom type agentRadiusServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentRadiusServerName_Type.__name__ = "DisplayString"
_AgentRadiusServerName_Object = MibTableColumn
agentRadiusServerName = _AgentRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 15),
    _AgentRadiusServerName_Type()
)
agentRadiusServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerName.setStatus("current")
_AgentRadiusServerInetAddress_Type = InetAddress
_AgentRadiusServerInetAddress_Object = MibTableColumn
agentRadiusServerInetAddress = _AgentRadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 16),
    _AgentRadiusServerInetAddress_Type()
)
agentRadiusServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerInetAddress.setStatus("current")
_AgentRadiusServerAddressType_Type = InetAddressType
_AgentRadiusServerAddressType_Object = MibTableColumn
agentRadiusServerAddressType = _AgentRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 7, 1, 17),
    _AgentRadiusServerAddressType_Type()
)
agentRadiusServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerAddressType.setStatus("current")
_AgentRadiusNasIpAddress_Type = IpAddress
_AgentRadiusNasIpAddress_Object = MibScalar
agentRadiusNasIpAddress = _AgentRadiusNasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 8),
    _AgentRadiusNasIpAddress_Type()
)
agentRadiusNasIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusNasIpAddress.setStatus("current")


class _AgentAuthorizationNetworkRadiusMode_Type(Integer32):
    """Custom type agentAuthorizationNetworkRadiusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentAuthorizationNetworkRadiusMode_Type.__name__ = "Integer32"
_AgentAuthorizationNetworkRadiusMode_Object = MibScalar
agentAuthorizationNetworkRadiusMode = _AgentAuthorizationNetworkRadiusMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 9),
    _AgentAuthorizationNetworkRadiusMode_Type()
)
agentAuthorizationNetworkRadiusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthorizationNetworkRadiusMode.setStatus("current")


class _AgentRadiusAccountingIndexNextValid_Type(Integer32):
    """Custom type agentRadiusAccountingIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusAccountingIndexNextValid_Type.__name__ = "Integer32"
_AgentRadiusAccountingIndexNextValid_Object = MibScalar
agentRadiusAccountingIndexNextValid = _AgentRadiusAccountingIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 10),
    _AgentRadiusAccountingIndexNextValid_Type()
)
agentRadiusAccountingIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAccountingIndexNextValid.setStatus("current")
_AgentRadiusAccountingConfigTable_Object = MibTable
agentRadiusAccountingConfigTable = _AgentRadiusAccountingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 11)
)
if mibBuilder.loadTexts:
    agentRadiusAccountingConfigTable.setStatus("current")
_AgentRadiusAccountingConfigEntry_Object = MibTableRow
agentRadiusAccountingConfigEntry = _AgentRadiusAccountingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 11, 1)
)
agentRadiusAccountingConfigEntry.setIndexNames(
    (0, "FASTPATH-RADIUS-AUTH-CLIENT-MIB", "agentRadiusAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    agentRadiusAccountingConfigEntry.setStatus("current")


class _AgentRadiusAccountingServerIndex_Type(Integer32):
    """Custom type agentRadiusAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusAccountingServerIndex_Type.__name__ = "Integer32"
_AgentRadiusAccountingServerIndex_Object = MibTableColumn
agentRadiusAccountingServerIndex = _AgentRadiusAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 11, 1, 1),
    _AgentRadiusAccountingServerIndex_Type()
)
agentRadiusAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerIndex.setStatus("current")
_AgentRadiusAccountingServerAddress_Type = InetAddress
_AgentRadiusAccountingServerAddress_Object = MibTableColumn
agentRadiusAccountingServerAddress = _AgentRadiusAccountingServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 11, 1, 2),
    _AgentRadiusAccountingServerAddress_Type()
)
agentRadiusAccountingServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerAddress.setStatus("current")
_AgentRadiusAccountingServerAddressType_Type = InetAddressType
_AgentRadiusAccountingServerAddressType_Object = MibTableColumn
agentRadiusAccountingServerAddressType = _AgentRadiusAccountingServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 11, 1, 3),
    _AgentRadiusAccountingServerAddressType_Type()
)
agentRadiusAccountingServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerAddressType.setStatus("current")


class _AgentRadiusAccountingPort_Type(Unsigned32):
    """Custom type agentRadiusAccountingPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentRadiusAccountingPort_Type.__name__ = "Unsigned32"
_AgentRadiusAccountingPort_Object = MibTableColumn
agentRadiusAccountingPort = _AgentRadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 11, 1, 4),
    _AgentRadiusAccountingPort_Type()
)
agentRadiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingPort.setStatus("current")


class _AgentRadiusAccountingSecret_Type(DisplayString):
    """Custom type agentRadiusAccountingSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentRadiusAccountingSecret_Type.__name__ = "DisplayString"
_AgentRadiusAccountingSecret_Object = MibTableColumn
agentRadiusAccountingSecret = _AgentRadiusAccountingSecret_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 11, 1, 5),
    _AgentRadiusAccountingSecret_Type()
)
agentRadiusAccountingSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingSecret.setStatus("current")
_AgentRadiusAccountingStatus_Type = RowStatus
_AgentRadiusAccountingStatus_Object = MibTableColumn
agentRadiusAccountingStatus = _AgentRadiusAccountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 11, 1, 6),
    _AgentRadiusAccountingStatus_Type()
)
agentRadiusAccountingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingStatus.setStatus("current")


class _AgentRadiusAccountingServerName_Type(DisplayString):
    """Custom type agentRadiusAccountingServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentRadiusAccountingServerName_Type.__name__ = "DisplayString"
_AgentRadiusAccountingServerName_Object = MibTableColumn
agentRadiusAccountingServerName = _AgentRadiusAccountingServerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 11, 1, 7),
    _AgentRadiusAccountingServerName_Type()
)
agentRadiusAccountingServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerName.setStatus("current")


class _AgentRadiusAccountingMode_Type(Integer32):
    """Custom type agentRadiusAccountingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentRadiusAccountingMode_Type.__name__ = "Integer32"
_AgentRadiusAccountingMode_Object = MibScalar
agentRadiusAccountingMode = _AgentRadiusAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 12),
    _AgentRadiusAccountingMode_Type()
)
agentRadiusAccountingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingMode.setStatus("current")


class _AgentRadiusStatsClear_Type(Integer32):
    """Custom type agentRadiusStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentRadiusStatsClear_Type.__name__ = "Integer32"
_AgentRadiusStatsClear_Object = MibScalar
agentRadiusStatsClear = _AgentRadiusStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 13),
    _AgentRadiusStatsClear_Type()
)
agentRadiusStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusStatsClear.setStatus("current")
_AgentRadiusAuthenticationServers_Type = Unsigned32
_AgentRadiusAuthenticationServers_Object = MibScalar
agentRadiusAuthenticationServers = _AgentRadiusAuthenticationServers_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 14),
    _AgentRadiusAuthenticationServers_Type()
)
agentRadiusAuthenticationServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAuthenticationServers.setStatus("current")
_AgentRadiusAccountingServers_Type = Unsigned32
_AgentRadiusAccountingServers_Object = MibScalar
agentRadiusAccountingServers = _AgentRadiusAccountingServers_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 15),
    _AgentRadiusAccountingServers_Type()
)
agentRadiusAccountingServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAccountingServers.setStatus("current")
_AgentRadiusNamedAuthenticationServerGroups_Type = Unsigned32
_AgentRadiusNamedAuthenticationServerGroups_Object = MibScalar
agentRadiusNamedAuthenticationServerGroups = _AgentRadiusNamedAuthenticationServerGroups_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 16),
    _AgentRadiusNamedAuthenticationServerGroups_Type()
)
agentRadiusNamedAuthenticationServerGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusNamedAuthenticationServerGroups.setStatus("current")
_AgentRadiusNamedAccountingServerGroups_Type = Unsigned32
_AgentRadiusNamedAccountingServerGroups_Object = MibScalar
agentRadiusNamedAccountingServerGroups = _AgentRadiusNamedAccountingServerGroups_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 8, 1, 17),
    _AgentRadiusNamedAccountingServerGroups_Type()
)
agentRadiusNamedAccountingServerGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusNamedAccountingServerGroups.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-RADIUS-AUTH-CLIENT-MIB",
    **{"fastPathRadius": fastPathRadius,
       "agentRadiusConfigGroup": agentRadiusConfigGroup,
       "agentRadiusRetransmit": agentRadiusRetransmit,
       "agentRadiusTimeout": agentRadiusTimeout,
       "agentRadiusDeadTime": agentRadiusDeadTime,
       "agentRadiusServerKey": agentRadiusServerKey,
       "agentRadiusSourceIPAddr": agentRadiusSourceIPAddr,
       "agentRadiusServerIndexNextValid": agentRadiusServerIndexNextValid,
       "agentRadiusServerConfigTable": agentRadiusServerConfigTable,
       "agentRadiusServerConfigEntry": agentRadiusServerConfigEntry,
       "agentRadiusServerIndex": agentRadiusServerIndex,
       "agentRadiusServerAddress": agentRadiusServerAddress,
       "agentRadiusServerPort": agentRadiusServerPort,
       "agentRadiusServerTimeout": agentRadiusServerTimeout,
       "agentRadiusServerRetransmit": agentRadiusServerRetransmit,
       "agentRadiusServerDeadtime": agentRadiusServerDeadtime,
       "agentRadiusServerSourceIPAddr": agentRadiusServerSourceIPAddr,
       "agentRadiusServerSecret": agentRadiusServerSecret,
       "agentRadiusServerPriority": agentRadiusServerPriority,
       "agentRadiusServerUsageType": agentRadiusServerUsageType,
       "agentRadiusServerAddressRowStatus": agentRadiusServerAddressRowStatus,
       "agentRadiusServerPrimaryMode": agentRadiusServerPrimaryMode,
       "agentRadiusServerCurrentMode": agentRadiusServerCurrentMode,
       "agentRadiusServerMsgAuth": agentRadiusServerMsgAuth,
       "agentRadiusServerName": agentRadiusServerName,
       "agentRadiusServerInetAddress": agentRadiusServerInetAddress,
       "agentRadiusServerAddressType": agentRadiusServerAddressType,
       "agentRadiusNasIpAddress": agentRadiusNasIpAddress,
       "agentAuthorizationNetworkRadiusMode": agentAuthorizationNetworkRadiusMode,
       "agentRadiusAccountingIndexNextValid": agentRadiusAccountingIndexNextValid,
       "agentRadiusAccountingConfigTable": agentRadiusAccountingConfigTable,
       "agentRadiusAccountingConfigEntry": agentRadiusAccountingConfigEntry,
       "agentRadiusAccountingServerIndex": agentRadiusAccountingServerIndex,
       "agentRadiusAccountingServerAddress": agentRadiusAccountingServerAddress,
       "agentRadiusAccountingServerAddressType": agentRadiusAccountingServerAddressType,
       "agentRadiusAccountingPort": agentRadiusAccountingPort,
       "agentRadiusAccountingSecret": agentRadiusAccountingSecret,
       "agentRadiusAccountingStatus": agentRadiusAccountingStatus,
       "agentRadiusAccountingServerName": agentRadiusAccountingServerName,
       "agentRadiusAccountingMode": agentRadiusAccountingMode,
       "agentRadiusStatsClear": agentRadiusStatsClear,
       "agentRadiusAuthenticationServers": agentRadiusAuthenticationServers,
       "agentRadiusAccountingServers": agentRadiusAccountingServers,
       "agentRadiusNamedAuthenticationServerGroups": agentRadiusNamedAuthenticationServerGroups,
       "agentRadiusNamedAccountingServerGroups": agentRadiusNamedAccountingServerGroups}
)
