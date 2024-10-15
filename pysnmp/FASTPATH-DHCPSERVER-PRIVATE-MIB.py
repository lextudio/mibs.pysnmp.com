# SNMP MIB module (FASTPATH-DHCPSERVER-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-DHCPSERVER-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:47 2024
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
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathDHCPServerPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12)
)
fastPathDHCPServerPrivate.setRevisions(
        ("2007-05-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentDhcpServerGroup_ObjectIdentity = ObjectIdentity
agentDhcpServerGroup = _AgentDhcpServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1)
)


class _AgentDhcpServerAdminMode_Type(Integer32):
    """Custom type agentDhcpServerAdminMode based on Integer32"""
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


_AgentDhcpServerAdminMode_Type.__name__ = "Integer32"
_AgentDhcpServerAdminMode_Object = MibScalar
agentDhcpServerAdminMode = _AgentDhcpServerAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 1),
    _AgentDhcpServerAdminMode_Type()
)
agentDhcpServerAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerAdminMode.setStatus("current")


class _AgentDhcpServerPingPktNos_Type(Integer32):
    """Custom type agentDhcpServerPingPktNos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 10),
    )


_AgentDhcpServerPingPktNos_Type.__name__ = "Integer32"
_AgentDhcpServerPingPktNos_Object = MibScalar
agentDhcpServerPingPktNos = _AgentDhcpServerPingPktNos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 2),
    _AgentDhcpServerPingPktNos_Type()
)
agentDhcpServerPingPktNos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPingPktNos.setStatus("current")
_AgentDhcpServerAutomaticBindingsNos_Type = Counter32
_AgentDhcpServerAutomaticBindingsNos_Object = MibScalar
agentDhcpServerAutomaticBindingsNos = _AgentDhcpServerAutomaticBindingsNos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 3),
    _AgentDhcpServerAutomaticBindingsNos_Type()
)
agentDhcpServerAutomaticBindingsNos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerAutomaticBindingsNos.setStatus("current")
_AgentDhcpServerExpiredBindingsNos_Type = Counter32
_AgentDhcpServerExpiredBindingsNos_Object = MibScalar
agentDhcpServerExpiredBindingsNos = _AgentDhcpServerExpiredBindingsNos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 4),
    _AgentDhcpServerExpiredBindingsNos_Type()
)
agentDhcpServerExpiredBindingsNos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerExpiredBindingsNos.setStatus("current")
_AgentDhcpServerMalformedMessagesReceived_Type = Counter32
_AgentDhcpServerMalformedMessagesReceived_Object = MibScalar
agentDhcpServerMalformedMessagesReceived = _AgentDhcpServerMalformedMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 5),
    _AgentDhcpServerMalformedMessagesReceived_Type()
)
agentDhcpServerMalformedMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerMalformedMessagesReceived.setStatus("current")
_AgentDhcpServerDISCOVERMessagesReceived_Type = Counter32
_AgentDhcpServerDISCOVERMessagesReceived_Object = MibScalar
agentDhcpServerDISCOVERMessagesReceived = _AgentDhcpServerDISCOVERMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 6),
    _AgentDhcpServerDISCOVERMessagesReceived_Type()
)
agentDhcpServerDISCOVERMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerDISCOVERMessagesReceived.setStatus("current")
_AgentDhcpServerREQUESTMessagesReceived_Type = Counter32
_AgentDhcpServerREQUESTMessagesReceived_Object = MibScalar
agentDhcpServerREQUESTMessagesReceived = _AgentDhcpServerREQUESTMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 7),
    _AgentDhcpServerREQUESTMessagesReceived_Type()
)
agentDhcpServerREQUESTMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerREQUESTMessagesReceived.setStatus("current")
_AgentDhcpServerDECLINEMessagesReceived_Type = Counter32
_AgentDhcpServerDECLINEMessagesReceived_Object = MibScalar
agentDhcpServerDECLINEMessagesReceived = _AgentDhcpServerDECLINEMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 8),
    _AgentDhcpServerDECLINEMessagesReceived_Type()
)
agentDhcpServerDECLINEMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerDECLINEMessagesReceived.setStatus("current")
_AgentDhcpServerRELEASEMessagesReceived_Type = Counter32
_AgentDhcpServerRELEASEMessagesReceived_Object = MibScalar
agentDhcpServerRELEASEMessagesReceived = _AgentDhcpServerRELEASEMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 9),
    _AgentDhcpServerRELEASEMessagesReceived_Type()
)
agentDhcpServerRELEASEMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerRELEASEMessagesReceived.setStatus("current")
_AgentDhcpServerINFORMMessagesReceived_Type = Counter32
_AgentDhcpServerINFORMMessagesReceived_Object = MibScalar
agentDhcpServerINFORMMessagesReceived = _AgentDhcpServerINFORMMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 10),
    _AgentDhcpServerINFORMMessagesReceived_Type()
)
agentDhcpServerINFORMMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerINFORMMessagesReceived.setStatus("current")
_AgentDhcpServerOFFERMessagesSent_Type = Counter32
_AgentDhcpServerOFFERMessagesSent_Object = MibScalar
agentDhcpServerOFFERMessagesSent = _AgentDhcpServerOFFERMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 11),
    _AgentDhcpServerOFFERMessagesSent_Type()
)
agentDhcpServerOFFERMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerOFFERMessagesSent.setStatus("current")
_AgentDhcpServerACKMessagesSent_Type = Counter32
_AgentDhcpServerACKMessagesSent_Object = MibScalar
agentDhcpServerACKMessagesSent = _AgentDhcpServerACKMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 12),
    _AgentDhcpServerACKMessagesSent_Type()
)
agentDhcpServerACKMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerACKMessagesSent.setStatus("current")
_AgentDhcpServerNAKMessagesSent_Type = Counter32
_AgentDhcpServerNAKMessagesSent_Object = MibScalar
agentDhcpServerNAKMessagesSent = _AgentDhcpServerNAKMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 13),
    _AgentDhcpServerNAKMessagesSent_Type()
)
agentDhcpServerNAKMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerNAKMessagesSent.setStatus("current")


class _AgentDhcpServerClearStatistics_Type(Integer32):
    """Custom type agentDhcpServerClearStatistics based on Integer32"""
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


_AgentDhcpServerClearStatistics_Type.__name__ = "Integer32"
_AgentDhcpServerClearStatistics_Object = MibScalar
agentDhcpServerClearStatistics = _AgentDhcpServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 14),
    _AgentDhcpServerClearStatistics_Type()
)
agentDhcpServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerClearStatistics.setStatus("current")


class _AgentDhcpServerBootpAutomatic_Type(Integer32):
    """Custom type agentDhcpServerBootpAutomatic based on Integer32"""
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


_AgentDhcpServerBootpAutomatic_Type.__name__ = "Integer32"
_AgentDhcpServerBootpAutomatic_Object = MibScalar
agentDhcpServerBootpAutomatic = _AgentDhcpServerBootpAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 1, 15),
    _AgentDhcpServerBootpAutomatic_Type()
)
agentDhcpServerBootpAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerBootpAutomatic.setStatus("current")
_AgentDhcpServerPoolConfigGroup_ObjectIdentity = ObjectIdentity
agentDhcpServerPoolConfigGroup = _AgentDhcpServerPoolConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2)
)


class _AgentDhcpServerPoolNameCreate_Type(DisplayString):
    """Custom type agentDhcpServerPoolNameCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 31),
    )


_AgentDhcpServerPoolNameCreate_Type.__name__ = "DisplayString"
_AgentDhcpServerPoolNameCreate_Object = MibScalar
agentDhcpServerPoolNameCreate = _AgentDhcpServerPoolNameCreate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 1),
    _AgentDhcpServerPoolNameCreate_Type()
)
agentDhcpServerPoolNameCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolNameCreate.setStatus("current")
_AgentDhcpServerPoolConfigTable_Object = MibTable
agentDhcpServerPoolConfigTable = _AgentDhcpServerPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2)
)
if mibBuilder.loadTexts:
    agentDhcpServerPoolConfigTable.setStatus("current")
_AgentDhcpServerPoolConfigEntry_Object = MibTableRow
agentDhcpServerPoolConfigEntry = _AgentDhcpServerPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1)
)
agentDhcpServerPoolConfigEntry.setIndexNames(
    (0, "FASTPATH-DHCPSERVER-PRIVATE-MIB", "agentDhcpServerPoolIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpServerPoolConfigEntry.setStatus("current")


class _AgentDhcpServerPoolIndex_Type(Unsigned32):
    """Custom type agentDhcpServerPoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_AgentDhcpServerPoolIndex_Type.__name__ = "Unsigned32"
_AgentDhcpServerPoolIndex_Object = MibTableColumn
agentDhcpServerPoolIndex = _AgentDhcpServerPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 1),
    _AgentDhcpServerPoolIndex_Type()
)
agentDhcpServerPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerPoolIndex.setStatus("current")


class _AgentDhcpServerPoolName_Type(DisplayString):
    """Custom type agentDhcpServerPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AgentDhcpServerPoolName_Type.__name__ = "DisplayString"
_AgentDhcpServerPoolName_Object = MibTableColumn
agentDhcpServerPoolName = _AgentDhcpServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 2),
    _AgentDhcpServerPoolName_Type()
)
agentDhcpServerPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerPoolName.setStatus("current")
_AgentDhcpServerPoolDefRouter_Type = DisplayString
_AgentDhcpServerPoolDefRouter_Object = MibTableColumn
agentDhcpServerPoolDefRouter = _AgentDhcpServerPoolDefRouter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 3),
    _AgentDhcpServerPoolDefRouter_Type()
)
agentDhcpServerPoolDefRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolDefRouter.setStatus("current")
_AgentDhcpServerPoolDNSServer_Type = DisplayString
_AgentDhcpServerPoolDNSServer_Object = MibTableColumn
agentDhcpServerPoolDNSServer = _AgentDhcpServerPoolDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 4),
    _AgentDhcpServerPoolDNSServer_Type()
)
agentDhcpServerPoolDNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolDNSServer.setStatus("current")


class _AgentDhcpServerPoolLeaseTime_Type(Integer32):
    """Custom type agentDhcpServerPoolLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_AgentDhcpServerPoolLeaseTime_Type.__name__ = "Integer32"
_AgentDhcpServerPoolLeaseTime_Object = MibTableColumn
agentDhcpServerPoolLeaseTime = _AgentDhcpServerPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 5),
    _AgentDhcpServerPoolLeaseTime_Type()
)
agentDhcpServerPoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolLeaseTime.setStatus("current")


class _AgentDhcpServerPoolType_Type(Integer32):
    """Custom type agentDhcpServerPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("manual", 2),
          ("un-allocated", 0))
    )


_AgentDhcpServerPoolType_Type.__name__ = "Integer32"
_AgentDhcpServerPoolType_Object = MibTableColumn
agentDhcpServerPoolType = _AgentDhcpServerPoolType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 6),
    _AgentDhcpServerPoolType_Type()
)
agentDhcpServerPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerPoolType.setStatus("current")
_AgentDhcpServerPoolNetbiosNameServer_Type = DisplayString
_AgentDhcpServerPoolNetbiosNameServer_Object = MibTableColumn
agentDhcpServerPoolNetbiosNameServer = _AgentDhcpServerPoolNetbiosNameServer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 7),
    _AgentDhcpServerPoolNetbiosNameServer_Type()
)
agentDhcpServerPoolNetbiosNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolNetbiosNameServer.setStatus("current")


class _AgentDhcpServerPoolNetbiosNodeType_Type(Integer32):
    """Custom type agentDhcpServerPoolNetbiosNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("b-node", 1),
          ("h-node", 8),
          ("m-node", 4),
          ("none", 0),
          ("p-node", 2))
    )


_AgentDhcpServerPoolNetbiosNodeType_Type.__name__ = "Integer32"
_AgentDhcpServerPoolNetbiosNodeType_Object = MibTableColumn
agentDhcpServerPoolNetbiosNodeType = _AgentDhcpServerPoolNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 8),
    _AgentDhcpServerPoolNetbiosNodeType_Type()
)
agentDhcpServerPoolNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolNetbiosNodeType.setStatus("current")
_AgentDhcpServerPoolNextServer_Type = IpAddress
_AgentDhcpServerPoolNextServer_Object = MibTableColumn
agentDhcpServerPoolNextServer = _AgentDhcpServerPoolNextServer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 9),
    _AgentDhcpServerPoolNextServer_Type()
)
agentDhcpServerPoolNextServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolNextServer.setStatus("current")


class _AgentDhcpServerPoolDomainName_Type(DisplayString):
    """Custom type agentDhcpServerPoolDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AgentDhcpServerPoolDomainName_Type.__name__ = "DisplayString"
_AgentDhcpServerPoolDomainName_Object = MibTableColumn
agentDhcpServerPoolDomainName = _AgentDhcpServerPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 10),
    _AgentDhcpServerPoolDomainName_Type()
)
agentDhcpServerPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolDomainName.setStatus("current")


class _AgentDhcpServerPoolBootfile_Type(DisplayString):
    """Custom type agentDhcpServerPoolBootfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AgentDhcpServerPoolBootfile_Type.__name__ = "DisplayString"
_AgentDhcpServerPoolBootfile_Object = MibTableColumn
agentDhcpServerPoolBootfile = _AgentDhcpServerPoolBootfile_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 11),
    _AgentDhcpServerPoolBootfile_Type()
)
agentDhcpServerPoolBootfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolBootfile.setStatus("current")
_AgentDhcpServerPoolRowStatus_Type = RowStatus
_AgentDhcpServerPoolRowStatus_Object = MibTableColumn
agentDhcpServerPoolRowStatus = _AgentDhcpServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 2, 1, 12),
    _AgentDhcpServerPoolRowStatus_Type()
)
agentDhcpServerPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolRowStatus.setStatus("current")
_AgentDhcpServerPoolAllocationTable_Object = MibTable
agentDhcpServerPoolAllocationTable = _AgentDhcpServerPoolAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3)
)
if mibBuilder.loadTexts:
    agentDhcpServerPoolAllocationTable.setStatus("current")
_AgentDhcpServerPoolAllocationEntry_Object = MibTableRow
agentDhcpServerPoolAllocationEntry = _AgentDhcpServerPoolAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1)
)
if mibBuilder.loadTexts:
    agentDhcpServerPoolAllocationEntry.setStatus("current")


class _AgentDhcpServerPoolAllocationName_Type(DisplayString):
    """Custom type agentDhcpServerPoolAllocationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_AgentDhcpServerPoolAllocationName_Type.__name__ = "DisplayString"
_AgentDhcpServerPoolAllocationName_Object = MibTableColumn
agentDhcpServerPoolAllocationName = _AgentDhcpServerPoolAllocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 1),
    _AgentDhcpServerPoolAllocationName_Type()
)
agentDhcpServerPoolAllocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerPoolAllocationName.setStatus("current")
_AgentDhcpServerDynamicPoolIpAddress_Type = IpAddress
_AgentDhcpServerDynamicPoolIpAddress_Object = MibTableColumn
agentDhcpServerDynamicPoolIpAddress = _AgentDhcpServerDynamicPoolIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 2),
    _AgentDhcpServerDynamicPoolIpAddress_Type()
)
agentDhcpServerDynamicPoolIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerDynamicPoolIpAddress.setStatus("current")
_AgentDhcpServerDynamicPoolIpMask_Type = IpAddress
_AgentDhcpServerDynamicPoolIpMask_Object = MibTableColumn
agentDhcpServerDynamicPoolIpMask = _AgentDhcpServerDynamicPoolIpMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 3),
    _AgentDhcpServerDynamicPoolIpMask_Type()
)
agentDhcpServerDynamicPoolIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerDynamicPoolIpMask.setStatus("current")
_AgentDhcpServerDynamicPoolIpPrefixLength_Type = Unsigned32
_AgentDhcpServerDynamicPoolIpPrefixLength_Object = MibTableColumn
agentDhcpServerDynamicPoolIpPrefixLength = _AgentDhcpServerDynamicPoolIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 4),
    _AgentDhcpServerDynamicPoolIpPrefixLength_Type()
)
agentDhcpServerDynamicPoolIpPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerDynamicPoolIpPrefixLength.setStatus("current")


class _AgentDhcpServerPoolAllocationType_Type(Integer32):
    """Custom type agentDhcpServerPoolAllocationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("manual", 2),
          ("un-allocated", 0))
    )


_AgentDhcpServerPoolAllocationType_Type.__name__ = "Integer32"
_AgentDhcpServerPoolAllocationType_Object = MibTableColumn
agentDhcpServerPoolAllocationType = _AgentDhcpServerPoolAllocationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 5),
    _AgentDhcpServerPoolAllocationType_Type()
)
agentDhcpServerPoolAllocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerPoolAllocationType.setStatus("current")
_AgentDhcpServerManualPoolClientIdentifier_Type = DisplayString
_AgentDhcpServerManualPoolClientIdentifier_Object = MibTableColumn
agentDhcpServerManualPoolClientIdentifier = _AgentDhcpServerManualPoolClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 6),
    _AgentDhcpServerManualPoolClientIdentifier_Type()
)
agentDhcpServerManualPoolClientIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerManualPoolClientIdentifier.setStatus("current")


class _AgentDhcpServerManualPoolClientName_Type(DisplayString):
    """Custom type agentDhcpServerManualPoolClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_AgentDhcpServerManualPoolClientName_Type.__name__ = "DisplayString"
_AgentDhcpServerManualPoolClientName_Object = MibTableColumn
agentDhcpServerManualPoolClientName = _AgentDhcpServerManualPoolClientName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 7),
    _AgentDhcpServerManualPoolClientName_Type()
)
agentDhcpServerManualPoolClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerManualPoolClientName.setStatus("current")
_AgentDhcpServerManualPoolClientHWAddr_Type = DisplayString
_AgentDhcpServerManualPoolClientHWAddr_Object = MibTableColumn
agentDhcpServerManualPoolClientHWAddr = _AgentDhcpServerManualPoolClientHWAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 8),
    _AgentDhcpServerManualPoolClientHWAddr_Type()
)
agentDhcpServerManualPoolClientHWAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerManualPoolClientHWAddr.setStatus("current")


class _AgentDhcpServerManualPoolClientHWType_Type(Integer32):
    """Custom type agentDhcpServerManualPoolClientHWType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee802", 6))
    )


_AgentDhcpServerManualPoolClientHWType_Type.__name__ = "Integer32"
_AgentDhcpServerManualPoolClientHWType_Object = MibTableColumn
agentDhcpServerManualPoolClientHWType = _AgentDhcpServerManualPoolClientHWType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 9),
    _AgentDhcpServerManualPoolClientHWType_Type()
)
agentDhcpServerManualPoolClientHWType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerManualPoolClientHWType.setStatus("current")
_AgentDhcpServerManualPoolIpAddress_Type = IpAddress
_AgentDhcpServerManualPoolIpAddress_Object = MibTableColumn
agentDhcpServerManualPoolIpAddress = _AgentDhcpServerManualPoolIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 10),
    _AgentDhcpServerManualPoolIpAddress_Type()
)
agentDhcpServerManualPoolIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerManualPoolIpAddress.setStatus("current")
_AgentDhcpServerManualPoolIpMask_Type = IpAddress
_AgentDhcpServerManualPoolIpMask_Object = MibTableColumn
agentDhcpServerManualPoolIpMask = _AgentDhcpServerManualPoolIpMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 11),
    _AgentDhcpServerManualPoolIpMask_Type()
)
agentDhcpServerManualPoolIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerManualPoolIpMask.setStatus("current")
_AgentDhcpServerManualPoolIpPrefixLength_Type = Unsigned32
_AgentDhcpServerManualPoolIpPrefixLength_Object = MibTableColumn
agentDhcpServerManualPoolIpPrefixLength = _AgentDhcpServerManualPoolIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 3, 1, 12),
    _AgentDhcpServerManualPoolIpPrefixLength_Type()
)
agentDhcpServerManualPoolIpPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerManualPoolIpPrefixLength.setStatus("current")
_AgentDhcpServerExcludedAddressRangeCreate_Type = DisplayString
_AgentDhcpServerExcludedAddressRangeCreate_Object = MibScalar
agentDhcpServerExcludedAddressRangeCreate = _AgentDhcpServerExcludedAddressRangeCreate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 4),
    _AgentDhcpServerExcludedAddressRangeCreate_Type()
)
agentDhcpServerExcludedAddressRangeCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerExcludedAddressRangeCreate.setStatus("current")
_AgentDhcpServerExcludedAddressRangeTable_Object = MibTable
agentDhcpServerExcludedAddressRangeTable = _AgentDhcpServerExcludedAddressRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 5)
)
if mibBuilder.loadTexts:
    agentDhcpServerExcludedAddressRangeTable.setStatus("current")
_AgentDhcpServerExcludedAddressRangeEntry_Object = MibTableRow
agentDhcpServerExcludedAddressRangeEntry = _AgentDhcpServerExcludedAddressRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 5, 1)
)
agentDhcpServerExcludedAddressRangeEntry.setIndexNames(
    (0, "FASTPATH-DHCPSERVER-PRIVATE-MIB", "agentDhcpServerExcludedRangeIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpServerExcludedAddressRangeEntry.setStatus("current")


class _AgentDhcpServerExcludedRangeIndex_Type(Unsigned32):
    """Custom type agentDhcpServerExcludedRangeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AgentDhcpServerExcludedRangeIndex_Type.__name__ = "Unsigned32"
_AgentDhcpServerExcludedRangeIndex_Object = MibTableColumn
agentDhcpServerExcludedRangeIndex = _AgentDhcpServerExcludedRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 5, 1, 1),
    _AgentDhcpServerExcludedRangeIndex_Type()
)
agentDhcpServerExcludedRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerExcludedRangeIndex.setStatus("current")
_AgentDhcpServerExcludedStartIpAddress_Type = IpAddress
_AgentDhcpServerExcludedStartIpAddress_Object = MibTableColumn
agentDhcpServerExcludedStartIpAddress = _AgentDhcpServerExcludedStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 5, 1, 2),
    _AgentDhcpServerExcludedStartIpAddress_Type()
)
agentDhcpServerExcludedStartIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerExcludedStartIpAddress.setStatus("current")
_AgentDhcpServerExcludedEndIpAddress_Type = IpAddress
_AgentDhcpServerExcludedEndIpAddress_Object = MibTableColumn
agentDhcpServerExcludedEndIpAddress = _AgentDhcpServerExcludedEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 5, 1, 3),
    _AgentDhcpServerExcludedEndIpAddress_Type()
)
agentDhcpServerExcludedEndIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerExcludedEndIpAddress.setStatus("current")
_AgentDhcpServerExcludedAddressRangeStatus_Type = RowStatus
_AgentDhcpServerExcludedAddressRangeStatus_Object = MibTableColumn
agentDhcpServerExcludedAddressRangeStatus = _AgentDhcpServerExcludedAddressRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 5, 1, 4),
    _AgentDhcpServerExcludedAddressRangeStatus_Type()
)
agentDhcpServerExcludedAddressRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerExcludedAddressRangeStatus.setStatus("current")
_AgentDhcpServerPoolOptionCreate_Type = DisplayString
_AgentDhcpServerPoolOptionCreate_Object = MibScalar
agentDhcpServerPoolOptionCreate = _AgentDhcpServerPoolOptionCreate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 6),
    _AgentDhcpServerPoolOptionCreate_Type()
)
agentDhcpServerPoolOptionCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolOptionCreate.setStatus("current")
_AgentDhcpServerPoolOptionTable_Object = MibTable
agentDhcpServerPoolOptionTable = _AgentDhcpServerPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 7)
)
if mibBuilder.loadTexts:
    agentDhcpServerPoolOptionTable.setStatus("current")
_AgentDhcpServerPoolOptionEntry_Object = MibTableRow
agentDhcpServerPoolOptionEntry = _AgentDhcpServerPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 7, 1)
)
agentDhcpServerPoolOptionEntry.setIndexNames(
    (0, "FASTPATH-DHCPSERVER-PRIVATE-MIB", "agentDhcpServerPoolOptionIndex"),
    (0, "FASTPATH-DHCPSERVER-PRIVATE-MIB", "agentDhcpServerPoolOptionCode"),
)
if mibBuilder.loadTexts:
    agentDhcpServerPoolOptionEntry.setStatus("current")


class _AgentDhcpServerPoolOptionIndex_Type(Unsigned32):
    """Custom type agentDhcpServerPoolOptionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_AgentDhcpServerPoolOptionIndex_Type.__name__ = "Unsigned32"
_AgentDhcpServerPoolOptionIndex_Object = MibTableColumn
agentDhcpServerPoolOptionIndex = _AgentDhcpServerPoolOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 7, 1, 1),
    _AgentDhcpServerPoolOptionIndex_Type()
)
agentDhcpServerPoolOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerPoolOptionIndex.setStatus("current")


class _AgentDhcpServerPoolOptionCode_Type(Unsigned32):
    """Custom type agentDhcpServerPoolOptionCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AgentDhcpServerPoolOptionCode_Type.__name__ = "Unsigned32"
_AgentDhcpServerPoolOptionCode_Object = MibTableColumn
agentDhcpServerPoolOptionCode = _AgentDhcpServerPoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 7, 1, 2),
    _AgentDhcpServerPoolOptionCode_Type()
)
agentDhcpServerPoolOptionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolOptionCode.setStatus("current")


class _AgentDhcpServerOptionPoolName_Type(DisplayString):
    """Custom type agentDhcpServerOptionPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AgentDhcpServerOptionPoolName_Type.__name__ = "DisplayString"
_AgentDhcpServerOptionPoolName_Object = MibTableColumn
agentDhcpServerOptionPoolName = _AgentDhcpServerOptionPoolName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 7, 1, 3),
    _AgentDhcpServerOptionPoolName_Type()
)
agentDhcpServerOptionPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerOptionPoolName.setStatus("current")


class _AgentDhcpServerPoolOptionAsciiData_Type(DisplayString):
    """Custom type agentDhcpServerPoolOptionAsciiData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 441),
    )


_AgentDhcpServerPoolOptionAsciiData_Type.__name__ = "DisplayString"
_AgentDhcpServerPoolOptionAsciiData_Object = MibTableColumn
agentDhcpServerPoolOptionAsciiData = _AgentDhcpServerPoolOptionAsciiData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 7, 1, 4),
    _AgentDhcpServerPoolOptionAsciiData_Type()
)
agentDhcpServerPoolOptionAsciiData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolOptionAsciiData.setStatus("current")


class _AgentDhcpServerPoolOptionHexData_Type(DisplayString):
    """Custom type agentDhcpServerPoolOptionHexData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1324),
    )


_AgentDhcpServerPoolOptionHexData_Type.__name__ = "DisplayString"
_AgentDhcpServerPoolOptionHexData_Object = MibTableColumn
agentDhcpServerPoolOptionHexData = _AgentDhcpServerPoolOptionHexData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 7, 1, 5),
    _AgentDhcpServerPoolOptionHexData_Type()
)
agentDhcpServerPoolOptionHexData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolOptionHexData.setStatus("current")
_AgentDhcpServerPoolOptionIpAddressData_Type = DisplayString
_AgentDhcpServerPoolOptionIpAddressData_Object = MibTableColumn
agentDhcpServerPoolOptionIpAddressData = _AgentDhcpServerPoolOptionIpAddressData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 7, 1, 6),
    _AgentDhcpServerPoolOptionIpAddressData_Type()
)
agentDhcpServerPoolOptionIpAddressData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolOptionIpAddressData.setStatus("current")
_AgentDhcpServerPoolOptionStatus_Type = RowStatus
_AgentDhcpServerPoolOptionStatus_Object = MibTableColumn
agentDhcpServerPoolOptionStatus = _AgentDhcpServerPoolOptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 2, 7, 1, 7),
    _AgentDhcpServerPoolOptionStatus_Type()
)
agentDhcpServerPoolOptionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerPoolOptionStatus.setStatus("current")
_AgentDhcpServerLeaseGroup_ObjectIdentity = ObjectIdentity
agentDhcpServerLeaseGroup = _AgentDhcpServerLeaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3)
)


class _AgentDhcpServerLeaseClearAllBindings_Type(Integer32):
    """Custom type agentDhcpServerLeaseClearAllBindings based on Integer32"""
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


_AgentDhcpServerLeaseClearAllBindings_Type.__name__ = "Integer32"
_AgentDhcpServerLeaseClearAllBindings_Object = MibScalar
agentDhcpServerLeaseClearAllBindings = _AgentDhcpServerLeaseClearAllBindings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3, 1),
    _AgentDhcpServerLeaseClearAllBindings_Type()
)
agentDhcpServerLeaseClearAllBindings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerLeaseClearAllBindings.setStatus("current")
_AgentDhcpServerLeaseTable_Object = MibTable
agentDhcpServerLeaseTable = _AgentDhcpServerLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3, 2)
)
if mibBuilder.loadTexts:
    agentDhcpServerLeaseTable.setStatus("current")
_AgentDhcpServerLeaseEntry_Object = MibTableRow
agentDhcpServerLeaseEntry = _AgentDhcpServerLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3, 2, 1)
)
agentDhcpServerLeaseEntry.setIndexNames(
    (0, "FASTPATH-DHCPSERVER-PRIVATE-MIB", "agentDhcpServerLeaseIPAddress"),
)
if mibBuilder.loadTexts:
    agentDhcpServerLeaseEntry.setStatus("current")
_AgentDhcpServerLeaseIPAddress_Type = IpAddress
_AgentDhcpServerLeaseIPAddress_Object = MibTableColumn
agentDhcpServerLeaseIPAddress = _AgentDhcpServerLeaseIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3, 2, 1, 1),
    _AgentDhcpServerLeaseIPAddress_Type()
)
agentDhcpServerLeaseIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerLeaseIPAddress.setStatus("current")
_AgentDhcpServerLeaseIPMask_Type = IpAddress
_AgentDhcpServerLeaseIPMask_Object = MibTableColumn
agentDhcpServerLeaseIPMask = _AgentDhcpServerLeaseIPMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3, 2, 1, 2),
    _AgentDhcpServerLeaseIPMask_Type()
)
agentDhcpServerLeaseIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerLeaseIPMask.setStatus("current")
_AgentDhcpServerLeaseHWAddress_Type = MacAddress
_AgentDhcpServerLeaseHWAddress_Object = MibTableColumn
agentDhcpServerLeaseHWAddress = _AgentDhcpServerLeaseHWAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3, 2, 1, 3),
    _AgentDhcpServerLeaseHWAddress_Type()
)
agentDhcpServerLeaseHWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerLeaseHWAddress.setStatus("current")
_AgentDhcpServerLeaseRemainingTime_Type = TimeTicks
_AgentDhcpServerLeaseRemainingTime_Object = MibTableColumn
agentDhcpServerLeaseRemainingTime = _AgentDhcpServerLeaseRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3, 2, 1, 4),
    _AgentDhcpServerLeaseRemainingTime_Type()
)
agentDhcpServerLeaseRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerLeaseRemainingTime.setStatus("current")


class _AgentDhcpServerLeaseType_Type(Integer32):
    """Custom type agentDhcpServerLeaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_AgentDhcpServerLeaseType_Type.__name__ = "Integer32"
_AgentDhcpServerLeaseType_Object = MibTableColumn
agentDhcpServerLeaseType = _AgentDhcpServerLeaseType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3, 2, 1, 5),
    _AgentDhcpServerLeaseType_Type()
)
agentDhcpServerLeaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerLeaseType.setStatus("current")
_AgentDhcpServerLeaseStatus_Type = RowStatus
_AgentDhcpServerLeaseStatus_Object = MibTableColumn
agentDhcpServerLeaseStatus = _AgentDhcpServerLeaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 3, 2, 1, 6),
    _AgentDhcpServerLeaseStatus_Type()
)
agentDhcpServerLeaseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerLeaseStatus.setStatus("current")
_AgentDhcpServerAddressConflictGroup_ObjectIdentity = ObjectIdentity
agentDhcpServerAddressConflictGroup = _AgentDhcpServerAddressConflictGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 4)
)


class _AgentDhcpServerClearAllAddressConflicts_Type(Integer32):
    """Custom type agentDhcpServerClearAllAddressConflicts based on Integer32"""
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


_AgentDhcpServerClearAllAddressConflicts_Type.__name__ = "Integer32"
_AgentDhcpServerClearAllAddressConflicts_Object = MibScalar
agentDhcpServerClearAllAddressConflicts = _AgentDhcpServerClearAllAddressConflicts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 4, 1),
    _AgentDhcpServerClearAllAddressConflicts_Type()
)
agentDhcpServerClearAllAddressConflicts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerClearAllAddressConflicts.setStatus("current")


class _AgentDhcpServerAddressConflictLogging_Type(Integer32):
    """Custom type agentDhcpServerAddressConflictLogging based on Integer32"""
    defaultValue = 1

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


_AgentDhcpServerAddressConflictLogging_Type.__name__ = "Integer32"
_AgentDhcpServerAddressConflictLogging_Object = MibScalar
agentDhcpServerAddressConflictLogging = _AgentDhcpServerAddressConflictLogging_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 4, 2),
    _AgentDhcpServerAddressConflictLogging_Type()
)
agentDhcpServerAddressConflictLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerAddressConflictLogging.setStatus("current")
_AgentDhcpServerAddressConflictTable_Object = MibTable
agentDhcpServerAddressConflictTable = _AgentDhcpServerAddressConflictTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 4, 3)
)
if mibBuilder.loadTexts:
    agentDhcpServerAddressConflictTable.setStatus("current")
_AgentDhcpServerAddressConflictEntry_Object = MibTableRow
agentDhcpServerAddressConflictEntry = _AgentDhcpServerAddressConflictEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 4, 3, 1)
)
agentDhcpServerAddressConflictEntry.setIndexNames(
    (0, "FASTPATH-DHCPSERVER-PRIVATE-MIB", "agentDhcpServerAddressConflictIP"),
)
if mibBuilder.loadTexts:
    agentDhcpServerAddressConflictEntry.setStatus("current")
_AgentDhcpServerAddressConflictIP_Type = IpAddress
_AgentDhcpServerAddressConflictIP_Object = MibTableColumn
agentDhcpServerAddressConflictIP = _AgentDhcpServerAddressConflictIP_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 4, 3, 1, 1),
    _AgentDhcpServerAddressConflictIP_Type()
)
agentDhcpServerAddressConflictIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerAddressConflictIP.setStatus("current")


class _AgentDhcpServerAddressConflictDetectionType_Type(Integer32):
    """Custom type agentDhcpServerAddressConflictDetectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gratuitousArp", 2),
          ("ping", 1))
    )


_AgentDhcpServerAddressConflictDetectionType_Type.__name__ = "Integer32"
_AgentDhcpServerAddressConflictDetectionType_Object = MibTableColumn
agentDhcpServerAddressConflictDetectionType = _AgentDhcpServerAddressConflictDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 4, 3, 1, 2),
    _AgentDhcpServerAddressConflictDetectionType_Type()
)
agentDhcpServerAddressConflictDetectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerAddressConflictDetectionType.setStatus("current")
_AgentDhcpServerAddressConflictDetectionTime_Type = TimeTicks
_AgentDhcpServerAddressConflictDetectionTime_Object = MibTableColumn
agentDhcpServerAddressConflictDetectionTime = _AgentDhcpServerAddressConflictDetectionTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 4, 3, 1, 3),
    _AgentDhcpServerAddressConflictDetectionTime_Type()
)
agentDhcpServerAddressConflictDetectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerAddressConflictDetectionTime.setStatus("current")
_AgentDhcpServerAddressConflictStatus_Type = RowStatus
_AgentDhcpServerAddressConflictStatus_Object = MibTableColumn
agentDhcpServerAddressConflictStatus = _AgentDhcpServerAddressConflictStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 12, 4, 3, 1, 4),
    _AgentDhcpServerAddressConflictStatus_Type()
)
agentDhcpServerAddressConflictStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDhcpServerAddressConflictStatus.setStatus("current")
agentDhcpServerPoolConfigEntry.registerAugmentions(
    ("FASTPATH-DHCPSERVER-PRIVATE-MIB",
     "agentDhcpServerPoolAllocationEntry")
)
agentDhcpServerPoolAllocationEntry.setIndexNames(*agentDhcpServerPoolConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-DHCPSERVER-PRIVATE-MIB",
    **{"fastPathDHCPServerPrivate": fastPathDHCPServerPrivate,
       "agentDhcpServerGroup": agentDhcpServerGroup,
       "agentDhcpServerAdminMode": agentDhcpServerAdminMode,
       "agentDhcpServerPingPktNos": agentDhcpServerPingPktNos,
       "agentDhcpServerAutomaticBindingsNos": agentDhcpServerAutomaticBindingsNos,
       "agentDhcpServerExpiredBindingsNos": agentDhcpServerExpiredBindingsNos,
       "agentDhcpServerMalformedMessagesReceived": agentDhcpServerMalformedMessagesReceived,
       "agentDhcpServerDISCOVERMessagesReceived": agentDhcpServerDISCOVERMessagesReceived,
       "agentDhcpServerREQUESTMessagesReceived": agentDhcpServerREQUESTMessagesReceived,
       "agentDhcpServerDECLINEMessagesReceived": agentDhcpServerDECLINEMessagesReceived,
       "agentDhcpServerRELEASEMessagesReceived": agentDhcpServerRELEASEMessagesReceived,
       "agentDhcpServerINFORMMessagesReceived": agentDhcpServerINFORMMessagesReceived,
       "agentDhcpServerOFFERMessagesSent": agentDhcpServerOFFERMessagesSent,
       "agentDhcpServerACKMessagesSent": agentDhcpServerACKMessagesSent,
       "agentDhcpServerNAKMessagesSent": agentDhcpServerNAKMessagesSent,
       "agentDhcpServerClearStatistics": agentDhcpServerClearStatistics,
       "agentDhcpServerBootpAutomatic": agentDhcpServerBootpAutomatic,
       "agentDhcpServerPoolConfigGroup": agentDhcpServerPoolConfigGroup,
       "agentDhcpServerPoolNameCreate": agentDhcpServerPoolNameCreate,
       "agentDhcpServerPoolConfigTable": agentDhcpServerPoolConfigTable,
       "agentDhcpServerPoolConfigEntry": agentDhcpServerPoolConfigEntry,
       "agentDhcpServerPoolIndex": agentDhcpServerPoolIndex,
       "agentDhcpServerPoolName": agentDhcpServerPoolName,
       "agentDhcpServerPoolDefRouter": agentDhcpServerPoolDefRouter,
       "agentDhcpServerPoolDNSServer": agentDhcpServerPoolDNSServer,
       "agentDhcpServerPoolLeaseTime": agentDhcpServerPoolLeaseTime,
       "agentDhcpServerPoolType": agentDhcpServerPoolType,
       "agentDhcpServerPoolNetbiosNameServer": agentDhcpServerPoolNetbiosNameServer,
       "agentDhcpServerPoolNetbiosNodeType": agentDhcpServerPoolNetbiosNodeType,
       "agentDhcpServerPoolNextServer": agentDhcpServerPoolNextServer,
       "agentDhcpServerPoolDomainName": agentDhcpServerPoolDomainName,
       "agentDhcpServerPoolBootfile": agentDhcpServerPoolBootfile,
       "agentDhcpServerPoolRowStatus": agentDhcpServerPoolRowStatus,
       "agentDhcpServerPoolAllocationTable": agentDhcpServerPoolAllocationTable,
       "agentDhcpServerPoolAllocationEntry": agentDhcpServerPoolAllocationEntry,
       "agentDhcpServerPoolAllocationName": agentDhcpServerPoolAllocationName,
       "agentDhcpServerDynamicPoolIpAddress": agentDhcpServerDynamicPoolIpAddress,
       "agentDhcpServerDynamicPoolIpMask": agentDhcpServerDynamicPoolIpMask,
       "agentDhcpServerDynamicPoolIpPrefixLength": agentDhcpServerDynamicPoolIpPrefixLength,
       "agentDhcpServerPoolAllocationType": agentDhcpServerPoolAllocationType,
       "agentDhcpServerManualPoolClientIdentifier": agentDhcpServerManualPoolClientIdentifier,
       "agentDhcpServerManualPoolClientName": agentDhcpServerManualPoolClientName,
       "agentDhcpServerManualPoolClientHWAddr": agentDhcpServerManualPoolClientHWAddr,
       "agentDhcpServerManualPoolClientHWType": agentDhcpServerManualPoolClientHWType,
       "agentDhcpServerManualPoolIpAddress": agentDhcpServerManualPoolIpAddress,
       "agentDhcpServerManualPoolIpMask": agentDhcpServerManualPoolIpMask,
       "agentDhcpServerManualPoolIpPrefixLength": agentDhcpServerManualPoolIpPrefixLength,
       "agentDhcpServerExcludedAddressRangeCreate": agentDhcpServerExcludedAddressRangeCreate,
       "agentDhcpServerExcludedAddressRangeTable": agentDhcpServerExcludedAddressRangeTable,
       "agentDhcpServerExcludedAddressRangeEntry": agentDhcpServerExcludedAddressRangeEntry,
       "agentDhcpServerExcludedRangeIndex": agentDhcpServerExcludedRangeIndex,
       "agentDhcpServerExcludedStartIpAddress": agentDhcpServerExcludedStartIpAddress,
       "agentDhcpServerExcludedEndIpAddress": agentDhcpServerExcludedEndIpAddress,
       "agentDhcpServerExcludedAddressRangeStatus": agentDhcpServerExcludedAddressRangeStatus,
       "agentDhcpServerPoolOptionCreate": agentDhcpServerPoolOptionCreate,
       "agentDhcpServerPoolOptionTable": agentDhcpServerPoolOptionTable,
       "agentDhcpServerPoolOptionEntry": agentDhcpServerPoolOptionEntry,
       "agentDhcpServerPoolOptionIndex": agentDhcpServerPoolOptionIndex,
       "agentDhcpServerPoolOptionCode": agentDhcpServerPoolOptionCode,
       "agentDhcpServerOptionPoolName": agentDhcpServerOptionPoolName,
       "agentDhcpServerPoolOptionAsciiData": agentDhcpServerPoolOptionAsciiData,
       "agentDhcpServerPoolOptionHexData": agentDhcpServerPoolOptionHexData,
       "agentDhcpServerPoolOptionIpAddressData": agentDhcpServerPoolOptionIpAddressData,
       "agentDhcpServerPoolOptionStatus": agentDhcpServerPoolOptionStatus,
       "agentDhcpServerLeaseGroup": agentDhcpServerLeaseGroup,
       "agentDhcpServerLeaseClearAllBindings": agentDhcpServerLeaseClearAllBindings,
       "agentDhcpServerLeaseTable": agentDhcpServerLeaseTable,
       "agentDhcpServerLeaseEntry": agentDhcpServerLeaseEntry,
       "agentDhcpServerLeaseIPAddress": agentDhcpServerLeaseIPAddress,
       "agentDhcpServerLeaseIPMask": agentDhcpServerLeaseIPMask,
       "agentDhcpServerLeaseHWAddress": agentDhcpServerLeaseHWAddress,
       "agentDhcpServerLeaseRemainingTime": agentDhcpServerLeaseRemainingTime,
       "agentDhcpServerLeaseType": agentDhcpServerLeaseType,
       "agentDhcpServerLeaseStatus": agentDhcpServerLeaseStatus,
       "agentDhcpServerAddressConflictGroup": agentDhcpServerAddressConflictGroup,
       "agentDhcpServerClearAllAddressConflicts": agentDhcpServerClearAllAddressConflicts,
       "agentDhcpServerAddressConflictLogging": agentDhcpServerAddressConflictLogging,
       "agentDhcpServerAddressConflictTable": agentDhcpServerAddressConflictTable,
       "agentDhcpServerAddressConflictEntry": agentDhcpServerAddressConflictEntry,
       "agentDhcpServerAddressConflictIP": agentDhcpServerAddressConflictIP,
       "agentDhcpServerAddressConflictDetectionType": agentDhcpServerAddressConflictDetectionType,
       "agentDhcpServerAddressConflictDetectionTime": agentDhcpServerAddressConflictDetectionTime,
       "agentDhcpServerAddressConflictStatus": agentDhcpServerAddressConflictStatus}
)
