# SNMP MIB module (CT-FASTPATH-DHCPSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-FASTPATH-DHCPSERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:11 2024
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

(ctDhcpServerExpMib,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctDhcpServerExpMib")

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

ctFastPathDHCPServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtAgentDhcpServerGroup_ObjectIdentity = ObjectIdentity
ctAgentDhcpServerGroup = _CtAgentDhcpServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1)
)


class _CtAgentDhcpServerAdminMode_Type(Integer32):
    """Custom type ctAgentDhcpServerAdminMode based on Integer32"""
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


_CtAgentDhcpServerAdminMode_Type.__name__ = "Integer32"
_CtAgentDhcpServerAdminMode_Object = MibScalar
ctAgentDhcpServerAdminMode = _CtAgentDhcpServerAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 1),
    _CtAgentDhcpServerAdminMode_Type()
)
ctAgentDhcpServerAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerAdminMode.setStatus("current")


class _CtAgentDhcpServerPingPktNos_Type(Integer32):
    """Custom type ctAgentDhcpServerPingPktNos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 10),
    )


_CtAgentDhcpServerPingPktNos_Type.__name__ = "Integer32"
_CtAgentDhcpServerPingPktNos_Object = MibScalar
ctAgentDhcpServerPingPktNos = _CtAgentDhcpServerPingPktNos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 2),
    _CtAgentDhcpServerPingPktNos_Type()
)
ctAgentDhcpServerPingPktNos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPingPktNos.setStatus("current")
_CtAgentDhcpServerAutomaticBindingsNos_Type = Counter32
_CtAgentDhcpServerAutomaticBindingsNos_Object = MibScalar
ctAgentDhcpServerAutomaticBindingsNos = _CtAgentDhcpServerAutomaticBindingsNos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 3),
    _CtAgentDhcpServerAutomaticBindingsNos_Type()
)
ctAgentDhcpServerAutomaticBindingsNos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerAutomaticBindingsNos.setStatus("current")
_CtAgentDhcpServerExpiredBindingsNos_Type = Counter32
_CtAgentDhcpServerExpiredBindingsNos_Object = MibScalar
ctAgentDhcpServerExpiredBindingsNos = _CtAgentDhcpServerExpiredBindingsNos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 4),
    _CtAgentDhcpServerExpiredBindingsNos_Type()
)
ctAgentDhcpServerExpiredBindingsNos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerExpiredBindingsNos.setStatus("current")
_CtAgentDhcpServerMalformedMessagesReceived_Type = Counter32
_CtAgentDhcpServerMalformedMessagesReceived_Object = MibScalar
ctAgentDhcpServerMalformedMessagesReceived = _CtAgentDhcpServerMalformedMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 5),
    _CtAgentDhcpServerMalformedMessagesReceived_Type()
)
ctAgentDhcpServerMalformedMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerMalformedMessagesReceived.setStatus("current")
_CtAgentDhcpServerDISCOVERMessagesReceived_Type = Counter32
_CtAgentDhcpServerDISCOVERMessagesReceived_Object = MibScalar
ctAgentDhcpServerDISCOVERMessagesReceived = _CtAgentDhcpServerDISCOVERMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 6),
    _CtAgentDhcpServerDISCOVERMessagesReceived_Type()
)
ctAgentDhcpServerDISCOVERMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerDISCOVERMessagesReceived.setStatus("current")
_CtAgentDhcpServerREQUESTMessagesReceived_Type = Counter32
_CtAgentDhcpServerREQUESTMessagesReceived_Object = MibScalar
ctAgentDhcpServerREQUESTMessagesReceived = _CtAgentDhcpServerREQUESTMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 7),
    _CtAgentDhcpServerREQUESTMessagesReceived_Type()
)
ctAgentDhcpServerREQUESTMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerREQUESTMessagesReceived.setStatus("current")
_CtAgentDhcpServerDECLINEMessagesReceived_Type = Counter32
_CtAgentDhcpServerDECLINEMessagesReceived_Object = MibScalar
ctAgentDhcpServerDECLINEMessagesReceived = _CtAgentDhcpServerDECLINEMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 8),
    _CtAgentDhcpServerDECLINEMessagesReceived_Type()
)
ctAgentDhcpServerDECLINEMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerDECLINEMessagesReceived.setStatus("current")
_CtAgentDhcpServerRELEASEMessagesReceived_Type = Counter32
_CtAgentDhcpServerRELEASEMessagesReceived_Object = MibScalar
ctAgentDhcpServerRELEASEMessagesReceived = _CtAgentDhcpServerRELEASEMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 9),
    _CtAgentDhcpServerRELEASEMessagesReceived_Type()
)
ctAgentDhcpServerRELEASEMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerRELEASEMessagesReceived.setStatus("current")
_CtAgentDhcpServerINFORMMessagesReceived_Type = Counter32
_CtAgentDhcpServerINFORMMessagesReceived_Object = MibScalar
ctAgentDhcpServerINFORMMessagesReceived = _CtAgentDhcpServerINFORMMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 10),
    _CtAgentDhcpServerINFORMMessagesReceived_Type()
)
ctAgentDhcpServerINFORMMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerINFORMMessagesReceived.setStatus("current")
_CtAgentDhcpServerOFFERMessagesSent_Type = Counter32
_CtAgentDhcpServerOFFERMessagesSent_Object = MibScalar
ctAgentDhcpServerOFFERMessagesSent = _CtAgentDhcpServerOFFERMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 11),
    _CtAgentDhcpServerOFFERMessagesSent_Type()
)
ctAgentDhcpServerOFFERMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerOFFERMessagesSent.setStatus("current")
_CtAgentDhcpServerACKMessagesSent_Type = Counter32
_CtAgentDhcpServerACKMessagesSent_Object = MibScalar
ctAgentDhcpServerACKMessagesSent = _CtAgentDhcpServerACKMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 12),
    _CtAgentDhcpServerACKMessagesSent_Type()
)
ctAgentDhcpServerACKMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerACKMessagesSent.setStatus("current")
_CtAgentDhcpServerNAKMessagesSent_Type = Counter32
_CtAgentDhcpServerNAKMessagesSent_Object = MibScalar
ctAgentDhcpServerNAKMessagesSent = _CtAgentDhcpServerNAKMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 13),
    _CtAgentDhcpServerNAKMessagesSent_Type()
)
ctAgentDhcpServerNAKMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerNAKMessagesSent.setStatus("current")


class _CtAgentDhcpServerClearStatistics_Type(Integer32):
    """Custom type ctAgentDhcpServerClearStatistics based on Integer32"""
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


_CtAgentDhcpServerClearStatistics_Type.__name__ = "Integer32"
_CtAgentDhcpServerClearStatistics_Object = MibScalar
ctAgentDhcpServerClearStatistics = _CtAgentDhcpServerClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 14),
    _CtAgentDhcpServerClearStatistics_Type()
)
ctAgentDhcpServerClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerClearStatistics.setStatus("current")


class _CtAgentDhcpServerBootpAutomatic_Type(Integer32):
    """Custom type ctAgentDhcpServerBootpAutomatic based on Integer32"""
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


_CtAgentDhcpServerBootpAutomatic_Type.__name__ = "Integer32"
_CtAgentDhcpServerBootpAutomatic_Object = MibScalar
ctAgentDhcpServerBootpAutomatic = _CtAgentDhcpServerBootpAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 15),
    _CtAgentDhcpServerBootpAutomatic_Type()
)
ctAgentDhcpServerBootpAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerBootpAutomatic.setStatus("current")
_CtAgentDhcpServerPoolConfigGroup_ObjectIdentity = ObjectIdentity
ctAgentDhcpServerPoolConfigGroup = _CtAgentDhcpServerPoolConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2)
)


class _CtAgentDhcpServerPoolNameCreate_Type(DisplayString):
    """Custom type ctAgentDhcpServerPoolNameCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 31),
    )


_CtAgentDhcpServerPoolNameCreate_Type.__name__ = "DisplayString"
_CtAgentDhcpServerPoolNameCreate_Object = MibScalar
ctAgentDhcpServerPoolNameCreate = _CtAgentDhcpServerPoolNameCreate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 1),
    _CtAgentDhcpServerPoolNameCreate_Type()
)
ctAgentDhcpServerPoolNameCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolNameCreate.setStatus("current")
_CtAgentDhcpServerPoolConfigTable_Object = MibTable
ctAgentDhcpServerPoolConfigTable = _CtAgentDhcpServerPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolConfigTable.setStatus("current")
_CtAgentDhcpServerPoolConfigEntry_Object = MibTableRow
ctAgentDhcpServerPoolConfigEntry = _CtAgentDhcpServerPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1)
)
ctAgentDhcpServerPoolConfigEntry.setIndexNames(
    (0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolIndex"),
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolConfigEntry.setStatus("current")


class _CtAgentDhcpServerPoolIndex_Type(Unsigned32):
    """Custom type ctAgentDhcpServerPoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtAgentDhcpServerPoolIndex_Type.__name__ = "Unsigned32"
_CtAgentDhcpServerPoolIndex_Object = MibTableColumn
ctAgentDhcpServerPoolIndex = _CtAgentDhcpServerPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 1),
    _CtAgentDhcpServerPoolIndex_Type()
)
ctAgentDhcpServerPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolIndex.setStatus("current")


class _CtAgentDhcpServerPoolName_Type(DisplayString):
    """Custom type ctAgentDhcpServerPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CtAgentDhcpServerPoolName_Type.__name__ = "DisplayString"
_CtAgentDhcpServerPoolName_Object = MibTableColumn
ctAgentDhcpServerPoolName = _CtAgentDhcpServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 2),
    _CtAgentDhcpServerPoolName_Type()
)
ctAgentDhcpServerPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolName.setStatus("current")
_CtAgentDhcpServerPoolDefRouter_Type = DisplayString
_CtAgentDhcpServerPoolDefRouter_Object = MibTableColumn
ctAgentDhcpServerPoolDefRouter = _CtAgentDhcpServerPoolDefRouter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 3),
    _CtAgentDhcpServerPoolDefRouter_Type()
)
ctAgentDhcpServerPoolDefRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolDefRouter.setStatus("current")
_CtAgentDhcpServerPoolDNSServer_Type = DisplayString
_CtAgentDhcpServerPoolDNSServer_Object = MibTableColumn
ctAgentDhcpServerPoolDNSServer = _CtAgentDhcpServerPoolDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 4),
    _CtAgentDhcpServerPoolDNSServer_Type()
)
ctAgentDhcpServerPoolDNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolDNSServer.setStatus("current")


class _CtAgentDhcpServerPoolLeaseTime_Type(Integer32):
    """Custom type ctAgentDhcpServerPoolLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CtAgentDhcpServerPoolLeaseTime_Type.__name__ = "Integer32"
_CtAgentDhcpServerPoolLeaseTime_Object = MibTableColumn
ctAgentDhcpServerPoolLeaseTime = _CtAgentDhcpServerPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 5),
    _CtAgentDhcpServerPoolLeaseTime_Type()
)
ctAgentDhcpServerPoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolLeaseTime.setStatus("current")


class _CtAgentDhcpServerPoolType_Type(Integer32):
    """Custom type ctAgentDhcpServerPoolType based on Integer32"""
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


_CtAgentDhcpServerPoolType_Type.__name__ = "Integer32"
_CtAgentDhcpServerPoolType_Object = MibTableColumn
ctAgentDhcpServerPoolType = _CtAgentDhcpServerPoolType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 6),
    _CtAgentDhcpServerPoolType_Type()
)
ctAgentDhcpServerPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolType.setStatus("current")
_CtAgentDhcpServerPoolNetbiosNameServer_Type = DisplayString
_CtAgentDhcpServerPoolNetbiosNameServer_Object = MibTableColumn
ctAgentDhcpServerPoolNetbiosNameServer = _CtAgentDhcpServerPoolNetbiosNameServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 7),
    _CtAgentDhcpServerPoolNetbiosNameServer_Type()
)
ctAgentDhcpServerPoolNetbiosNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolNetbiosNameServer.setStatus("current")


class _CtAgentDhcpServerPoolNetbiosNodeType_Type(Integer32):
    """Custom type ctAgentDhcpServerPoolNetbiosNodeType based on Integer32"""
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


_CtAgentDhcpServerPoolNetbiosNodeType_Type.__name__ = "Integer32"
_CtAgentDhcpServerPoolNetbiosNodeType_Object = MibTableColumn
ctAgentDhcpServerPoolNetbiosNodeType = _CtAgentDhcpServerPoolNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 8),
    _CtAgentDhcpServerPoolNetbiosNodeType_Type()
)
ctAgentDhcpServerPoolNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolNetbiosNodeType.setStatus("current")
_CtAgentDhcpServerPoolNextServer_Type = IpAddress
_CtAgentDhcpServerPoolNextServer_Object = MibTableColumn
ctAgentDhcpServerPoolNextServer = _CtAgentDhcpServerPoolNextServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 9),
    _CtAgentDhcpServerPoolNextServer_Type()
)
ctAgentDhcpServerPoolNextServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolNextServer.setStatus("current")


class _CtAgentDhcpServerPoolDomainName_Type(DisplayString):
    """Custom type ctAgentDhcpServerPoolDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CtAgentDhcpServerPoolDomainName_Type.__name__ = "DisplayString"
_CtAgentDhcpServerPoolDomainName_Object = MibTableColumn
ctAgentDhcpServerPoolDomainName = _CtAgentDhcpServerPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 10),
    _CtAgentDhcpServerPoolDomainName_Type()
)
ctAgentDhcpServerPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolDomainName.setStatus("current")


class _CtAgentDhcpServerPoolBootfile_Type(DisplayString):
    """Custom type ctAgentDhcpServerPoolBootfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CtAgentDhcpServerPoolBootfile_Type.__name__ = "DisplayString"
_CtAgentDhcpServerPoolBootfile_Object = MibTableColumn
ctAgentDhcpServerPoolBootfile = _CtAgentDhcpServerPoolBootfile_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 11),
    _CtAgentDhcpServerPoolBootfile_Type()
)
ctAgentDhcpServerPoolBootfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolBootfile.setStatus("current")
_CtAgentDhcpServerPoolRowStatus_Type = RowStatus
_CtAgentDhcpServerPoolRowStatus_Object = MibTableColumn
ctAgentDhcpServerPoolRowStatus = _CtAgentDhcpServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 12),
    _CtAgentDhcpServerPoolRowStatus_Type()
)
ctAgentDhcpServerPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolRowStatus.setStatus("current")
_CtAgentDhcpServerPoolAllocationTable_Object = MibTable
ctAgentDhcpServerPoolAllocationTable = _CtAgentDhcpServerPoolAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolAllocationTable.setStatus("current")
_CtAgentDhcpServerPoolAllocationEntry_Object = MibTableRow
ctAgentDhcpServerPoolAllocationEntry = _CtAgentDhcpServerPoolAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolAllocationEntry.setStatus("current")


class _CtAgentDhcpServerPoolAllocationName_Type(DisplayString):
    """Custom type ctAgentDhcpServerPoolAllocationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_CtAgentDhcpServerPoolAllocationName_Type.__name__ = "DisplayString"
_CtAgentDhcpServerPoolAllocationName_Object = MibTableColumn
ctAgentDhcpServerPoolAllocationName = _CtAgentDhcpServerPoolAllocationName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 1),
    _CtAgentDhcpServerPoolAllocationName_Type()
)
ctAgentDhcpServerPoolAllocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolAllocationName.setStatus("current")
_CtAgentDhcpServerDynamicPoolIpAddress_Type = IpAddress
_CtAgentDhcpServerDynamicPoolIpAddress_Object = MibTableColumn
ctAgentDhcpServerDynamicPoolIpAddress = _CtAgentDhcpServerDynamicPoolIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 2),
    _CtAgentDhcpServerDynamicPoolIpAddress_Type()
)
ctAgentDhcpServerDynamicPoolIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerDynamicPoolIpAddress.setStatus("current")
_CtAgentDhcpServerDynamicPoolIpMask_Type = IpAddress
_CtAgentDhcpServerDynamicPoolIpMask_Object = MibTableColumn
ctAgentDhcpServerDynamicPoolIpMask = _CtAgentDhcpServerDynamicPoolIpMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 3),
    _CtAgentDhcpServerDynamicPoolIpMask_Type()
)
ctAgentDhcpServerDynamicPoolIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerDynamicPoolIpMask.setStatus("current")
_CtAgentDhcpServerDynamicPoolIpPrefixLength_Type = Unsigned32
_CtAgentDhcpServerDynamicPoolIpPrefixLength_Object = MibTableColumn
ctAgentDhcpServerDynamicPoolIpPrefixLength = _CtAgentDhcpServerDynamicPoolIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 4),
    _CtAgentDhcpServerDynamicPoolIpPrefixLength_Type()
)
ctAgentDhcpServerDynamicPoolIpPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerDynamicPoolIpPrefixLength.setStatus("current")


class _CtAgentDhcpServerPoolAllocationType_Type(Integer32):
    """Custom type ctAgentDhcpServerPoolAllocationType based on Integer32"""
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


_CtAgentDhcpServerPoolAllocationType_Type.__name__ = "Integer32"
_CtAgentDhcpServerPoolAllocationType_Object = MibTableColumn
ctAgentDhcpServerPoolAllocationType = _CtAgentDhcpServerPoolAllocationType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 5),
    _CtAgentDhcpServerPoolAllocationType_Type()
)
ctAgentDhcpServerPoolAllocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolAllocationType.setStatus("current")
_CtAgentDhcpServerManualPoolClientIdentifier_Type = DisplayString
_CtAgentDhcpServerManualPoolClientIdentifier_Object = MibTableColumn
ctAgentDhcpServerManualPoolClientIdentifier = _CtAgentDhcpServerManualPoolClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 6),
    _CtAgentDhcpServerManualPoolClientIdentifier_Type()
)
ctAgentDhcpServerManualPoolClientIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerManualPoolClientIdentifier.setStatus("current")


class _CtAgentDhcpServerManualPoolClientName_Type(DisplayString):
    """Custom type ctAgentDhcpServerManualPoolClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_CtAgentDhcpServerManualPoolClientName_Type.__name__ = "DisplayString"
_CtAgentDhcpServerManualPoolClientName_Object = MibTableColumn
ctAgentDhcpServerManualPoolClientName = _CtAgentDhcpServerManualPoolClientName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 7),
    _CtAgentDhcpServerManualPoolClientName_Type()
)
ctAgentDhcpServerManualPoolClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerManualPoolClientName.setStatus("current")
_CtAgentDhcpServerManualPoolClientHWAddr_Type = DisplayString
_CtAgentDhcpServerManualPoolClientHWAddr_Object = MibTableColumn
ctAgentDhcpServerManualPoolClientHWAddr = _CtAgentDhcpServerManualPoolClientHWAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 8),
    _CtAgentDhcpServerManualPoolClientHWAddr_Type()
)
ctAgentDhcpServerManualPoolClientHWAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerManualPoolClientHWAddr.setStatus("current")


class _CtAgentDhcpServerManualPoolClientHWType_Type(Integer32):
    """Custom type ctAgentDhcpServerManualPoolClientHWType based on Integer32"""
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


_CtAgentDhcpServerManualPoolClientHWType_Type.__name__ = "Integer32"
_CtAgentDhcpServerManualPoolClientHWType_Object = MibTableColumn
ctAgentDhcpServerManualPoolClientHWType = _CtAgentDhcpServerManualPoolClientHWType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 9),
    _CtAgentDhcpServerManualPoolClientHWType_Type()
)
ctAgentDhcpServerManualPoolClientHWType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerManualPoolClientHWType.setStatus("current")
_CtAgentDhcpServerManualPoolIpAddress_Type = IpAddress
_CtAgentDhcpServerManualPoolIpAddress_Object = MibTableColumn
ctAgentDhcpServerManualPoolIpAddress = _CtAgentDhcpServerManualPoolIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 10),
    _CtAgentDhcpServerManualPoolIpAddress_Type()
)
ctAgentDhcpServerManualPoolIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerManualPoolIpAddress.setStatus("current")
_CtAgentDhcpServerManualPoolIpMask_Type = IpAddress
_CtAgentDhcpServerManualPoolIpMask_Object = MibTableColumn
ctAgentDhcpServerManualPoolIpMask = _CtAgentDhcpServerManualPoolIpMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 11),
    _CtAgentDhcpServerManualPoolIpMask_Type()
)
ctAgentDhcpServerManualPoolIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerManualPoolIpMask.setStatus("current")
_CtAgentDhcpServerManualPoolIpPrefixLength_Type = Unsigned32
_CtAgentDhcpServerManualPoolIpPrefixLength_Object = MibTableColumn
ctAgentDhcpServerManualPoolIpPrefixLength = _CtAgentDhcpServerManualPoolIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 12),
    _CtAgentDhcpServerManualPoolIpPrefixLength_Type()
)
ctAgentDhcpServerManualPoolIpPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerManualPoolIpPrefixLength.setStatus("current")
_CtAgentDhcpServerExcludedAddressRangeCreate_Type = DisplayString
_CtAgentDhcpServerExcludedAddressRangeCreate_Object = MibScalar
ctAgentDhcpServerExcludedAddressRangeCreate = _CtAgentDhcpServerExcludedAddressRangeCreate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 4),
    _CtAgentDhcpServerExcludedAddressRangeCreate_Type()
)
ctAgentDhcpServerExcludedAddressRangeCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerExcludedAddressRangeCreate.setStatus("current")
_CtAgentDhcpServerExcludedAddressRangeTable_Object = MibTable
ctAgentDhcpServerExcludedAddressRangeTable = _CtAgentDhcpServerExcludedAddressRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerExcludedAddressRangeTable.setStatus("current")
_CtAgentDhcpServerExcludedAddressRangeEntry_Object = MibTableRow
ctAgentDhcpServerExcludedAddressRangeEntry = _CtAgentDhcpServerExcludedAddressRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1)
)
ctAgentDhcpServerExcludedAddressRangeEntry.setIndexNames(
    (0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerExcludedRangeIndex"),
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerExcludedAddressRangeEntry.setStatus("current")


class _CtAgentDhcpServerExcludedRangeIndex_Type(Unsigned32):
    """Custom type ctAgentDhcpServerExcludedRangeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CtAgentDhcpServerExcludedRangeIndex_Type.__name__ = "Unsigned32"
_CtAgentDhcpServerExcludedRangeIndex_Object = MibTableColumn
ctAgentDhcpServerExcludedRangeIndex = _CtAgentDhcpServerExcludedRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 1),
    _CtAgentDhcpServerExcludedRangeIndex_Type()
)
ctAgentDhcpServerExcludedRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerExcludedRangeIndex.setStatus("current")
_CtAgentDhcpServerExcludedStartIpAddress_Type = IpAddress
_CtAgentDhcpServerExcludedStartIpAddress_Object = MibTableColumn
ctAgentDhcpServerExcludedStartIpAddress = _CtAgentDhcpServerExcludedStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 2),
    _CtAgentDhcpServerExcludedStartIpAddress_Type()
)
ctAgentDhcpServerExcludedStartIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerExcludedStartIpAddress.setStatus("current")
_CtAgentDhcpServerExcludedEndIpAddress_Type = IpAddress
_CtAgentDhcpServerExcludedEndIpAddress_Object = MibTableColumn
ctAgentDhcpServerExcludedEndIpAddress = _CtAgentDhcpServerExcludedEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 3),
    _CtAgentDhcpServerExcludedEndIpAddress_Type()
)
ctAgentDhcpServerExcludedEndIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerExcludedEndIpAddress.setStatus("current")
_CtAgentDhcpServerExcludedAddressRangeStatus_Type = RowStatus
_CtAgentDhcpServerExcludedAddressRangeStatus_Object = MibTableColumn
ctAgentDhcpServerExcludedAddressRangeStatus = _CtAgentDhcpServerExcludedAddressRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 4),
    _CtAgentDhcpServerExcludedAddressRangeStatus_Type()
)
ctAgentDhcpServerExcludedAddressRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerExcludedAddressRangeStatus.setStatus("current")
_CtAgentDhcpServerPoolOptionCreate_Type = DisplayString
_CtAgentDhcpServerPoolOptionCreate_Object = MibScalar
ctAgentDhcpServerPoolOptionCreate = _CtAgentDhcpServerPoolOptionCreate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 6),
    _CtAgentDhcpServerPoolOptionCreate_Type()
)
ctAgentDhcpServerPoolOptionCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolOptionCreate.setStatus("current")
_CtAgentDhcpServerPoolOptionTable_Object = MibTable
ctAgentDhcpServerPoolOptionTable = _CtAgentDhcpServerPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolOptionTable.setStatus("current")
_CtAgentDhcpServerPoolOptionEntry_Object = MibTableRow
ctAgentDhcpServerPoolOptionEntry = _CtAgentDhcpServerPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1)
)
ctAgentDhcpServerPoolOptionEntry.setIndexNames(
    (0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolOptionIndex"),
    (0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolOptionCode"),
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolOptionEntry.setStatus("current")


class _CtAgentDhcpServerPoolOptionIndex_Type(Unsigned32):
    """Custom type ctAgentDhcpServerPoolOptionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtAgentDhcpServerPoolOptionIndex_Type.__name__ = "Unsigned32"
_CtAgentDhcpServerPoolOptionIndex_Object = MibTableColumn
ctAgentDhcpServerPoolOptionIndex = _CtAgentDhcpServerPoolOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 1),
    _CtAgentDhcpServerPoolOptionIndex_Type()
)
ctAgentDhcpServerPoolOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolOptionIndex.setStatus("current")


class _CtAgentDhcpServerPoolOptionCode_Type(Unsigned32):
    """Custom type ctAgentDhcpServerPoolOptionCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_CtAgentDhcpServerPoolOptionCode_Type.__name__ = "Unsigned32"
_CtAgentDhcpServerPoolOptionCode_Object = MibTableColumn
ctAgentDhcpServerPoolOptionCode = _CtAgentDhcpServerPoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 2),
    _CtAgentDhcpServerPoolOptionCode_Type()
)
ctAgentDhcpServerPoolOptionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolOptionCode.setStatus("current")


class _CtAgentDhcpServerOptionPoolName_Type(DisplayString):
    """Custom type ctAgentDhcpServerOptionPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CtAgentDhcpServerOptionPoolName_Type.__name__ = "DisplayString"
_CtAgentDhcpServerOptionPoolName_Object = MibTableColumn
ctAgentDhcpServerOptionPoolName = _CtAgentDhcpServerOptionPoolName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 3),
    _CtAgentDhcpServerOptionPoolName_Type()
)
ctAgentDhcpServerOptionPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerOptionPoolName.setStatus("current")


class _CtAgentDhcpServerPoolOptionAsciiData_Type(DisplayString):
    """Custom type ctAgentDhcpServerPoolOptionAsciiData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 441),
    )


_CtAgentDhcpServerPoolOptionAsciiData_Type.__name__ = "DisplayString"
_CtAgentDhcpServerPoolOptionAsciiData_Object = MibTableColumn
ctAgentDhcpServerPoolOptionAsciiData = _CtAgentDhcpServerPoolOptionAsciiData_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 4),
    _CtAgentDhcpServerPoolOptionAsciiData_Type()
)
ctAgentDhcpServerPoolOptionAsciiData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolOptionAsciiData.setStatus("current")


class _CtAgentDhcpServerPoolOptionHexData_Type(DisplayString):
    """Custom type ctAgentDhcpServerPoolOptionHexData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1324),
    )


_CtAgentDhcpServerPoolOptionHexData_Type.__name__ = "DisplayString"
_CtAgentDhcpServerPoolOptionHexData_Object = MibTableColumn
ctAgentDhcpServerPoolOptionHexData = _CtAgentDhcpServerPoolOptionHexData_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 5),
    _CtAgentDhcpServerPoolOptionHexData_Type()
)
ctAgentDhcpServerPoolOptionHexData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolOptionHexData.setStatus("current")
_CtAgentDhcpServerPoolOptionIpAddressData_Type = DisplayString
_CtAgentDhcpServerPoolOptionIpAddressData_Object = MibTableColumn
ctAgentDhcpServerPoolOptionIpAddressData = _CtAgentDhcpServerPoolOptionIpAddressData_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 6),
    _CtAgentDhcpServerPoolOptionIpAddressData_Type()
)
ctAgentDhcpServerPoolOptionIpAddressData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolOptionIpAddressData.setStatus("current")
_CtAgentDhcpServerPoolOptionStatus_Type = RowStatus
_CtAgentDhcpServerPoolOptionStatus_Object = MibTableColumn
ctAgentDhcpServerPoolOptionStatus = _CtAgentDhcpServerPoolOptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 7),
    _CtAgentDhcpServerPoolOptionStatus_Type()
)
ctAgentDhcpServerPoolOptionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerPoolOptionStatus.setStatus("current")
_CtAgentDhcpServerLeaseGroup_ObjectIdentity = ObjectIdentity
ctAgentDhcpServerLeaseGroup = _CtAgentDhcpServerLeaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3)
)


class _CtAgentDhcpServerLeaseClearAllBindings_Type(Integer32):
    """Custom type ctAgentDhcpServerLeaseClearAllBindings based on Integer32"""
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


_CtAgentDhcpServerLeaseClearAllBindings_Type.__name__ = "Integer32"
_CtAgentDhcpServerLeaseClearAllBindings_Object = MibScalar
ctAgentDhcpServerLeaseClearAllBindings = _CtAgentDhcpServerLeaseClearAllBindings_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 1),
    _CtAgentDhcpServerLeaseClearAllBindings_Type()
)
ctAgentDhcpServerLeaseClearAllBindings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerLeaseClearAllBindings.setStatus("current")
_CtAgentDhcpServerLeaseTable_Object = MibTable
ctAgentDhcpServerLeaseTable = _CtAgentDhcpServerLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerLeaseTable.setStatus("current")
_CtAgentDhcpServerLeaseEntry_Object = MibTableRow
ctAgentDhcpServerLeaseEntry = _CtAgentDhcpServerLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1)
)
ctAgentDhcpServerLeaseEntry.setIndexNames(
    (0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerLeaseIPAddress"),
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerLeaseEntry.setStatus("current")
_CtAgentDhcpServerLeaseIPAddress_Type = IpAddress
_CtAgentDhcpServerLeaseIPAddress_Object = MibTableColumn
ctAgentDhcpServerLeaseIPAddress = _CtAgentDhcpServerLeaseIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 1),
    _CtAgentDhcpServerLeaseIPAddress_Type()
)
ctAgentDhcpServerLeaseIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerLeaseIPAddress.setStatus("current")
_CtAgentDhcpServerLeaseIPMask_Type = IpAddress
_CtAgentDhcpServerLeaseIPMask_Object = MibTableColumn
ctAgentDhcpServerLeaseIPMask = _CtAgentDhcpServerLeaseIPMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 2),
    _CtAgentDhcpServerLeaseIPMask_Type()
)
ctAgentDhcpServerLeaseIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerLeaseIPMask.setStatus("current")
_CtAgentDhcpServerLeaseHWAddress_Type = MacAddress
_CtAgentDhcpServerLeaseHWAddress_Object = MibTableColumn
ctAgentDhcpServerLeaseHWAddress = _CtAgentDhcpServerLeaseHWAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 3),
    _CtAgentDhcpServerLeaseHWAddress_Type()
)
ctAgentDhcpServerLeaseHWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerLeaseHWAddress.setStatus("current")
_CtAgentDhcpServerLeaseRemainingTime_Type = TimeTicks
_CtAgentDhcpServerLeaseRemainingTime_Object = MibTableColumn
ctAgentDhcpServerLeaseRemainingTime = _CtAgentDhcpServerLeaseRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 4),
    _CtAgentDhcpServerLeaseRemainingTime_Type()
)
ctAgentDhcpServerLeaseRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerLeaseRemainingTime.setStatus("current")


class _CtAgentDhcpServerLeaseType_Type(Integer32):
    """Custom type ctAgentDhcpServerLeaseType based on Integer32"""
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


_CtAgentDhcpServerLeaseType_Type.__name__ = "Integer32"
_CtAgentDhcpServerLeaseType_Object = MibTableColumn
ctAgentDhcpServerLeaseType = _CtAgentDhcpServerLeaseType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 5),
    _CtAgentDhcpServerLeaseType_Type()
)
ctAgentDhcpServerLeaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerLeaseType.setStatus("current")
_CtAgentDhcpServerLeaseStatus_Type = RowStatus
_CtAgentDhcpServerLeaseStatus_Object = MibTableColumn
ctAgentDhcpServerLeaseStatus = _CtAgentDhcpServerLeaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 6),
    _CtAgentDhcpServerLeaseStatus_Type()
)
ctAgentDhcpServerLeaseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerLeaseStatus.setStatus("current")
_CtAgentDhcpServerAddressConflictGroup_ObjectIdentity = ObjectIdentity
ctAgentDhcpServerAddressConflictGroup = _CtAgentDhcpServerAddressConflictGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4)
)


class _CtAgentDhcpServerClearAllAddressConflicts_Type(Integer32):
    """Custom type ctAgentDhcpServerClearAllAddressConflicts based on Integer32"""
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


_CtAgentDhcpServerClearAllAddressConflicts_Type.__name__ = "Integer32"
_CtAgentDhcpServerClearAllAddressConflicts_Object = MibScalar
ctAgentDhcpServerClearAllAddressConflicts = _CtAgentDhcpServerClearAllAddressConflicts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 1),
    _CtAgentDhcpServerClearAllAddressConflicts_Type()
)
ctAgentDhcpServerClearAllAddressConflicts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerClearAllAddressConflicts.setStatus("current")


class _CtAgentDhcpServerAddressConflictLogging_Type(Integer32):
    """Custom type ctAgentDhcpServerAddressConflictLogging based on Integer32"""
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


_CtAgentDhcpServerAddressConflictLogging_Type.__name__ = "Integer32"
_CtAgentDhcpServerAddressConflictLogging_Object = MibScalar
ctAgentDhcpServerAddressConflictLogging = _CtAgentDhcpServerAddressConflictLogging_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 2),
    _CtAgentDhcpServerAddressConflictLogging_Type()
)
ctAgentDhcpServerAddressConflictLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerAddressConflictLogging.setStatus("current")
_CtAgentDhcpServerAddressConflictTable_Object = MibTable
ctAgentDhcpServerAddressConflictTable = _CtAgentDhcpServerAddressConflictTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerAddressConflictTable.setStatus("current")
_CtAgentDhcpServerAddressConflictEntry_Object = MibTableRow
ctAgentDhcpServerAddressConflictEntry = _CtAgentDhcpServerAddressConflictEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1)
)
ctAgentDhcpServerAddressConflictEntry.setIndexNames(
    (0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerAddressConflictIP"),
)
if mibBuilder.loadTexts:
    ctAgentDhcpServerAddressConflictEntry.setStatus("current")
_CtAgentDhcpServerAddressConflictIP_Type = IpAddress
_CtAgentDhcpServerAddressConflictIP_Object = MibTableColumn
ctAgentDhcpServerAddressConflictIP = _CtAgentDhcpServerAddressConflictIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 1),
    _CtAgentDhcpServerAddressConflictIP_Type()
)
ctAgentDhcpServerAddressConflictIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerAddressConflictIP.setStatus("current")


class _CtAgentDhcpServerAddressConflictDetectionType_Type(Integer32):
    """Custom type ctAgentDhcpServerAddressConflictDetectionType based on Integer32"""
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


_CtAgentDhcpServerAddressConflictDetectionType_Type.__name__ = "Integer32"
_CtAgentDhcpServerAddressConflictDetectionType_Object = MibTableColumn
ctAgentDhcpServerAddressConflictDetectionType = _CtAgentDhcpServerAddressConflictDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 2),
    _CtAgentDhcpServerAddressConflictDetectionType_Type()
)
ctAgentDhcpServerAddressConflictDetectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerAddressConflictDetectionType.setStatus("current")
_CtAgentDhcpServerAddressConflictDetectionTime_Type = TimeTicks
_CtAgentDhcpServerAddressConflictDetectionTime_Object = MibTableColumn
ctAgentDhcpServerAddressConflictDetectionTime = _CtAgentDhcpServerAddressConflictDetectionTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 3),
    _CtAgentDhcpServerAddressConflictDetectionTime_Type()
)
ctAgentDhcpServerAddressConflictDetectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDhcpServerAddressConflictDetectionTime.setStatus("current")
_CtAgentDhcpServerAddressConflictStatus_Type = RowStatus
_CtAgentDhcpServerAddressConflictStatus_Object = MibTableColumn
ctAgentDhcpServerAddressConflictStatus = _CtAgentDhcpServerAddressConflictStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 4),
    _CtAgentDhcpServerAddressConflictStatus_Type()
)
ctAgentDhcpServerAddressConflictStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDhcpServerAddressConflictStatus.setStatus("current")
ctAgentDhcpServerPoolConfigEntry.registerAugmentions(
    ("CT-FASTPATH-DHCPSERVER-MIB",
     "ctAgentDhcpServerPoolAllocationEntry")
)
ctAgentDhcpServerPoolAllocationEntry.setIndexNames(*ctAgentDhcpServerPoolConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-FASTPATH-DHCPSERVER-MIB",
    **{"ctFastPathDHCPServerMIB": ctFastPathDHCPServerMIB,
       "ctAgentDhcpServerGroup": ctAgentDhcpServerGroup,
       "ctAgentDhcpServerAdminMode": ctAgentDhcpServerAdminMode,
       "ctAgentDhcpServerPingPktNos": ctAgentDhcpServerPingPktNos,
       "ctAgentDhcpServerAutomaticBindingsNos": ctAgentDhcpServerAutomaticBindingsNos,
       "ctAgentDhcpServerExpiredBindingsNos": ctAgentDhcpServerExpiredBindingsNos,
       "ctAgentDhcpServerMalformedMessagesReceived": ctAgentDhcpServerMalformedMessagesReceived,
       "ctAgentDhcpServerDISCOVERMessagesReceived": ctAgentDhcpServerDISCOVERMessagesReceived,
       "ctAgentDhcpServerREQUESTMessagesReceived": ctAgentDhcpServerREQUESTMessagesReceived,
       "ctAgentDhcpServerDECLINEMessagesReceived": ctAgentDhcpServerDECLINEMessagesReceived,
       "ctAgentDhcpServerRELEASEMessagesReceived": ctAgentDhcpServerRELEASEMessagesReceived,
       "ctAgentDhcpServerINFORMMessagesReceived": ctAgentDhcpServerINFORMMessagesReceived,
       "ctAgentDhcpServerOFFERMessagesSent": ctAgentDhcpServerOFFERMessagesSent,
       "ctAgentDhcpServerACKMessagesSent": ctAgentDhcpServerACKMessagesSent,
       "ctAgentDhcpServerNAKMessagesSent": ctAgentDhcpServerNAKMessagesSent,
       "ctAgentDhcpServerClearStatistics": ctAgentDhcpServerClearStatistics,
       "ctAgentDhcpServerBootpAutomatic": ctAgentDhcpServerBootpAutomatic,
       "ctAgentDhcpServerPoolConfigGroup": ctAgentDhcpServerPoolConfigGroup,
       "ctAgentDhcpServerPoolNameCreate": ctAgentDhcpServerPoolNameCreate,
       "ctAgentDhcpServerPoolConfigTable": ctAgentDhcpServerPoolConfigTable,
       "ctAgentDhcpServerPoolConfigEntry": ctAgentDhcpServerPoolConfigEntry,
       "ctAgentDhcpServerPoolIndex": ctAgentDhcpServerPoolIndex,
       "ctAgentDhcpServerPoolName": ctAgentDhcpServerPoolName,
       "ctAgentDhcpServerPoolDefRouter": ctAgentDhcpServerPoolDefRouter,
       "ctAgentDhcpServerPoolDNSServer": ctAgentDhcpServerPoolDNSServer,
       "ctAgentDhcpServerPoolLeaseTime": ctAgentDhcpServerPoolLeaseTime,
       "ctAgentDhcpServerPoolType": ctAgentDhcpServerPoolType,
       "ctAgentDhcpServerPoolNetbiosNameServer": ctAgentDhcpServerPoolNetbiosNameServer,
       "ctAgentDhcpServerPoolNetbiosNodeType": ctAgentDhcpServerPoolNetbiosNodeType,
       "ctAgentDhcpServerPoolNextServer": ctAgentDhcpServerPoolNextServer,
       "ctAgentDhcpServerPoolDomainName": ctAgentDhcpServerPoolDomainName,
       "ctAgentDhcpServerPoolBootfile": ctAgentDhcpServerPoolBootfile,
       "ctAgentDhcpServerPoolRowStatus": ctAgentDhcpServerPoolRowStatus,
       "ctAgentDhcpServerPoolAllocationTable": ctAgentDhcpServerPoolAllocationTable,
       "ctAgentDhcpServerPoolAllocationEntry": ctAgentDhcpServerPoolAllocationEntry,
       "ctAgentDhcpServerPoolAllocationName": ctAgentDhcpServerPoolAllocationName,
       "ctAgentDhcpServerDynamicPoolIpAddress": ctAgentDhcpServerDynamicPoolIpAddress,
       "ctAgentDhcpServerDynamicPoolIpMask": ctAgentDhcpServerDynamicPoolIpMask,
       "ctAgentDhcpServerDynamicPoolIpPrefixLength": ctAgentDhcpServerDynamicPoolIpPrefixLength,
       "ctAgentDhcpServerPoolAllocationType": ctAgentDhcpServerPoolAllocationType,
       "ctAgentDhcpServerManualPoolClientIdentifier": ctAgentDhcpServerManualPoolClientIdentifier,
       "ctAgentDhcpServerManualPoolClientName": ctAgentDhcpServerManualPoolClientName,
       "ctAgentDhcpServerManualPoolClientHWAddr": ctAgentDhcpServerManualPoolClientHWAddr,
       "ctAgentDhcpServerManualPoolClientHWType": ctAgentDhcpServerManualPoolClientHWType,
       "ctAgentDhcpServerManualPoolIpAddress": ctAgentDhcpServerManualPoolIpAddress,
       "ctAgentDhcpServerManualPoolIpMask": ctAgentDhcpServerManualPoolIpMask,
       "ctAgentDhcpServerManualPoolIpPrefixLength": ctAgentDhcpServerManualPoolIpPrefixLength,
       "ctAgentDhcpServerExcludedAddressRangeCreate": ctAgentDhcpServerExcludedAddressRangeCreate,
       "ctAgentDhcpServerExcludedAddressRangeTable": ctAgentDhcpServerExcludedAddressRangeTable,
       "ctAgentDhcpServerExcludedAddressRangeEntry": ctAgentDhcpServerExcludedAddressRangeEntry,
       "ctAgentDhcpServerExcludedRangeIndex": ctAgentDhcpServerExcludedRangeIndex,
       "ctAgentDhcpServerExcludedStartIpAddress": ctAgentDhcpServerExcludedStartIpAddress,
       "ctAgentDhcpServerExcludedEndIpAddress": ctAgentDhcpServerExcludedEndIpAddress,
       "ctAgentDhcpServerExcludedAddressRangeStatus": ctAgentDhcpServerExcludedAddressRangeStatus,
       "ctAgentDhcpServerPoolOptionCreate": ctAgentDhcpServerPoolOptionCreate,
       "ctAgentDhcpServerPoolOptionTable": ctAgentDhcpServerPoolOptionTable,
       "ctAgentDhcpServerPoolOptionEntry": ctAgentDhcpServerPoolOptionEntry,
       "ctAgentDhcpServerPoolOptionIndex": ctAgentDhcpServerPoolOptionIndex,
       "ctAgentDhcpServerPoolOptionCode": ctAgentDhcpServerPoolOptionCode,
       "ctAgentDhcpServerOptionPoolName": ctAgentDhcpServerOptionPoolName,
       "ctAgentDhcpServerPoolOptionAsciiData": ctAgentDhcpServerPoolOptionAsciiData,
       "ctAgentDhcpServerPoolOptionHexData": ctAgentDhcpServerPoolOptionHexData,
       "ctAgentDhcpServerPoolOptionIpAddressData": ctAgentDhcpServerPoolOptionIpAddressData,
       "ctAgentDhcpServerPoolOptionStatus": ctAgentDhcpServerPoolOptionStatus,
       "ctAgentDhcpServerLeaseGroup": ctAgentDhcpServerLeaseGroup,
       "ctAgentDhcpServerLeaseClearAllBindings": ctAgentDhcpServerLeaseClearAllBindings,
       "ctAgentDhcpServerLeaseTable": ctAgentDhcpServerLeaseTable,
       "ctAgentDhcpServerLeaseEntry": ctAgentDhcpServerLeaseEntry,
       "ctAgentDhcpServerLeaseIPAddress": ctAgentDhcpServerLeaseIPAddress,
       "ctAgentDhcpServerLeaseIPMask": ctAgentDhcpServerLeaseIPMask,
       "ctAgentDhcpServerLeaseHWAddress": ctAgentDhcpServerLeaseHWAddress,
       "ctAgentDhcpServerLeaseRemainingTime": ctAgentDhcpServerLeaseRemainingTime,
       "ctAgentDhcpServerLeaseType": ctAgentDhcpServerLeaseType,
       "ctAgentDhcpServerLeaseStatus": ctAgentDhcpServerLeaseStatus,
       "ctAgentDhcpServerAddressConflictGroup": ctAgentDhcpServerAddressConflictGroup,
       "ctAgentDhcpServerClearAllAddressConflicts": ctAgentDhcpServerClearAllAddressConflicts,
       "ctAgentDhcpServerAddressConflictLogging": ctAgentDhcpServerAddressConflictLogging,
       "ctAgentDhcpServerAddressConflictTable": ctAgentDhcpServerAddressConflictTable,
       "ctAgentDhcpServerAddressConflictEntry": ctAgentDhcpServerAddressConflictEntry,
       "ctAgentDhcpServerAddressConflictIP": ctAgentDhcpServerAddressConflictIP,
       "ctAgentDhcpServerAddressConflictDetectionType": ctAgentDhcpServerAddressConflictDetectionType,
       "ctAgentDhcpServerAddressConflictDetectionTime": ctAgentDhcpServerAddressConflictDetectionTime,
       "ctAgentDhcpServerAddressConflictStatus": ctAgentDhcpServerAddressConflictStatus}
)
