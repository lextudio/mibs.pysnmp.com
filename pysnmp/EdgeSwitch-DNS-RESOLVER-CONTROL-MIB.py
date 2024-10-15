# SNMP MIB module (EdgeSwitch-DNS-RESOLVER-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-DNS-RESOLVER-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:42:42 2024
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
    "EdgeSwitch-REF-MIB",
    "fastPath")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathDnsResControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37)
)
fastPathDnsResControlMIB.setRevisions(
        ("2011-12-14 00:00",
         "2011-01-26 00:00",
         "2007-05-23 00:00",
         "2005-03-28 11:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DnsCacheEntryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnsCacheAddresstype", 1),
          ("dnsCacheCnametye", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FastPathDnsResCtlMIBObjects_ObjectIdentity = ObjectIdentity
fastPathDnsResCtlMIBObjects = _FastPathDnsResCtlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1)
)
_AgentResCtlglobal_ObjectIdentity = ObjectIdentity
agentResCtlglobal = _AgentResCtlglobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1)
)
_AgentResCtlAdminMode_Type = TruthValue
_AgentResCtlAdminMode_Object = MibScalar
agentResCtlAdminMode = _AgentResCtlAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 1),
    _AgentResCtlAdminMode_Type()
)
agentResCtlAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentResCtlAdminMode.setStatus("current")


class _AgentResCtlDefDomainName_Type(OctetString):
    """Custom type agentResCtlDefDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentResCtlDefDomainName_Type.__name__ = "OctetString"
_AgentResCtlDefDomainName_Object = MibScalar
agentResCtlDefDomainName = _AgentResCtlDefDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 2),
    _AgentResCtlDefDomainName_Type()
)
agentResCtlDefDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentResCtlDefDomainName.setStatus("current")


class _AgentResCtlCacheFlushStatus_Type(Integer32):
    """Custom type agentResCtlCacheFlushStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnsCacheFlushDisable", 2),
          ("dnsCacheFlushEnable", 1))
    )


_AgentResCtlCacheFlushStatus_Type.__name__ = "Integer32"
_AgentResCtlCacheFlushStatus_Object = MibScalar
agentResCtlCacheFlushStatus = _AgentResCtlCacheFlushStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 3),
    _AgentResCtlCacheFlushStatus_Type()
)
agentResCtlCacheFlushStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentResCtlCacheFlushStatus.setStatus("current")


class _AgentResCtlRequestTimeout_Type(Integer32):
    """Custom type agentResCtlRequestTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AgentResCtlRequestTimeout_Type.__name__ = "Integer32"
_AgentResCtlRequestTimeout_Object = MibScalar
agentResCtlRequestTimeout = _AgentResCtlRequestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 4),
    _AgentResCtlRequestTimeout_Type()
)
agentResCtlRequestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentResCtlRequestTimeout.setStatus("current")


class _AgentResCtlRequestRetransmits_Type(Integer32):
    """Custom type agentResCtlRequestRetransmits based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentResCtlRequestRetransmits_Type.__name__ = "Integer32"
_AgentResCtlRequestRetransmits_Object = MibScalar
agentResCtlRequestRetransmits = _AgentResCtlRequestRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 5),
    _AgentResCtlRequestRetransmits_Type()
)
agentResCtlRequestRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentResCtlRequestRetransmits.setStatus("current")
_AgentResCtlDomainListTable_Object = MibTable
agentResCtlDomainListTable = _AgentResCtlDomainListTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 6)
)
if mibBuilder.loadTexts:
    agentResCtlDomainListTable.setStatus("current")
_AgentResCtlDomainListEntry_Object = MibTableRow
agentResCtlDomainListEntry = _AgentResCtlDomainListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 6, 1)
)
agentResCtlDomainListEntry.setIndexNames(
    (0, "EdgeSwitch-DNS-RESOLVER-CONTROL-MIB", "agentResCtlDomainListName"),
)
if mibBuilder.loadTexts:
    agentResCtlDomainListEntry.setStatus("current")
_AgentResCtlDomainListName_Type = DisplayString
_AgentResCtlDomainListName_Object = MibTableColumn
agentResCtlDomainListName = _AgentResCtlDomainListName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 6, 1, 1),
    _AgentResCtlDomainListName_Type()
)
agentResCtlDomainListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentResCtlDomainListName.setStatus("current")
_AgentResCtlDomainListNameStatus_Type = RowStatus
_AgentResCtlDomainListNameStatus_Object = MibTableColumn
agentResCtlDomainListNameStatus = _AgentResCtlDomainListNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 6, 1, 2),
    _AgentResCtlDomainListNameStatus_Type()
)
agentResCtlDomainListNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentResCtlDomainListNameStatus.setStatus("current")
_AgentResCtlSourceInterface_Type = InterfaceIndexOrZero
_AgentResCtlSourceInterface_Object = MibScalar
agentResCtlSourceInterface = _AgentResCtlSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 1, 7),
    _AgentResCtlSourceInterface_Type()
)
agentResCtlSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentResCtlSourceInterface.setStatus("current")
_AgentResCtlServConfig_ObjectIdentity = ObjectIdentity
agentResCtlServConfig = _AgentResCtlServConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 2)
)
_AgentResCtlServConfigTable_Object = MibTable
agentResCtlServConfigTable = _AgentResCtlServConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 2, 1)
)
if mibBuilder.loadTexts:
    agentResCtlServConfigTable.setStatus("current")
_AgentResCtlConfigIPEntry_Object = MibTableRow
agentResCtlConfigIPEntry = _AgentResCtlConfigIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 2, 1, 1)
)
agentResCtlConfigIPEntry.setIndexNames(
    (0, "EdgeSwitch-DNS-RESOLVER-CONTROL-MIB", "agentResCtlDnsNameServerIPType"),
    (0, "EdgeSwitch-DNS-RESOLVER-CONTROL-MIB", "agentResCtlDnsNameServerIP"),
)
if mibBuilder.loadTexts:
    agentResCtlConfigIPEntry.setStatus("current")
_AgentResCtlDnsNameServerIPType_Type = InetAddressType
_AgentResCtlDnsNameServerIPType_Object = MibTableColumn
agentResCtlDnsNameServerIPType = _AgentResCtlDnsNameServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 2, 1, 1, 1),
    _AgentResCtlDnsNameServerIPType_Type()
)
agentResCtlDnsNameServerIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentResCtlDnsNameServerIPType.setStatus("current")


class _AgentResCtlDnsNameServerIP_Type(InetAddress):
    """Custom type agentResCtlDnsNameServerIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AgentResCtlDnsNameServerIP_Type.__name__ = "InetAddress"
_AgentResCtlDnsNameServerIP_Object = MibTableColumn
agentResCtlDnsNameServerIP = _AgentResCtlDnsNameServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 2, 1, 1, 2),
    _AgentResCtlDnsNameServerIP_Type()
)
agentResCtlDnsNameServerIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentResCtlDnsNameServerIP.setStatus("current")
_AgentResCtlDnsNameServerStatus_Type = RowStatus
_AgentResCtlDnsNameServerStatus_Object = MibTableColumn
agentResCtlDnsNameServerStatus = _AgentResCtlDnsNameServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 2, 1, 1, 3),
    _AgentResCtlDnsNameServerStatus_Type()
)
agentResCtlDnsNameServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentResCtlDnsNameServerStatus.setStatus("current")
_AgentResCtlStaticServConfig_ObjectIdentity = ObjectIdentity
agentResCtlStaticServConfig = _AgentResCtlStaticServConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 3)
)
_AgentResCtlStaticServConfigTable_Object = MibTable
agentResCtlStaticServConfigTable = _AgentResCtlStaticServConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 3, 1)
)
if mibBuilder.loadTexts:
    agentResCtlStaticServConfigTable.setStatus("current")
_AgentResCtlStaticServEntry_Object = MibTableRow
agentResCtlStaticServEntry = _AgentResCtlStaticServEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 3, 1, 1)
)
agentResCtlStaticServEntry.setIndexNames(
    (0, "EdgeSwitch-DNS-RESOLVER-CONTROL-MIB", "agentResCtlStaticHostName"),
    (0, "EdgeSwitch-DNS-RESOLVER-CONTROL-MIB", "agentResCtlStaticIPAddress"),
)
if mibBuilder.loadTexts:
    agentResCtlStaticServEntry.setStatus("current")


class _AgentResCtlStaticHostName_Type(OctetString):
    """Custom type agentResCtlStaticHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentResCtlStaticHostName_Type.__name__ = "OctetString"
_AgentResCtlStaticHostName_Object = MibTableColumn
agentResCtlStaticHostName = _AgentResCtlStaticHostName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 3, 1, 1, 1),
    _AgentResCtlStaticHostName_Type()
)
agentResCtlStaticHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentResCtlStaticHostName.setStatus("current")
_AgentResCtlStaticIPAddress_Type = IpAddress
_AgentResCtlStaticIPAddress_Object = MibTableColumn
agentResCtlStaticIPAddress = _AgentResCtlStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 3, 1, 1, 2),
    _AgentResCtlStaticIPAddress_Type()
)
agentResCtlStaticIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentResCtlStaticIPAddress.setStatus("current")
_AgentResCtlStaticNameServerStatus_Type = RowStatus
_AgentResCtlStaticNameServerStatus_Object = MibTableColumn
agentResCtlStaticNameServerStatus = _AgentResCtlStaticNameServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 37, 1, 3, 1, 1, 3),
    _AgentResCtlStaticNameServerStatus_Type()
)
agentResCtlStaticNameServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentResCtlStaticNameServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-DNS-RESOLVER-CONTROL-MIB",
    **{"DnsCacheEntryType": DnsCacheEntryType,
       "fastPathDnsResControlMIB": fastPathDnsResControlMIB,
       "fastPathDnsResCtlMIBObjects": fastPathDnsResCtlMIBObjects,
       "agentResCtlglobal": agentResCtlglobal,
       "agentResCtlAdminMode": agentResCtlAdminMode,
       "agentResCtlDefDomainName": agentResCtlDefDomainName,
       "agentResCtlCacheFlushStatus": agentResCtlCacheFlushStatus,
       "agentResCtlRequestTimeout": agentResCtlRequestTimeout,
       "agentResCtlRequestRetransmits": agentResCtlRequestRetransmits,
       "agentResCtlDomainListTable": agentResCtlDomainListTable,
       "agentResCtlDomainListEntry": agentResCtlDomainListEntry,
       "agentResCtlDomainListName": agentResCtlDomainListName,
       "agentResCtlDomainListNameStatus": agentResCtlDomainListNameStatus,
       "agentResCtlSourceInterface": agentResCtlSourceInterface,
       "agentResCtlServConfig": agentResCtlServConfig,
       "agentResCtlServConfigTable": agentResCtlServConfigTable,
       "agentResCtlConfigIPEntry": agentResCtlConfigIPEntry,
       "agentResCtlDnsNameServerIPType": agentResCtlDnsNameServerIPType,
       "agentResCtlDnsNameServerIP": agentResCtlDnsNameServerIP,
       "agentResCtlDnsNameServerStatus": agentResCtlDnsNameServerStatus,
       "agentResCtlStaticServConfig": agentResCtlStaticServConfig,
       "agentResCtlStaticServConfigTable": agentResCtlStaticServConfigTable,
       "agentResCtlStaticServEntry": agentResCtlStaticServEntry,
       "agentResCtlStaticHostName": agentResCtlStaticHostName,
       "agentResCtlStaticIPAddress": agentResCtlStaticIPAddress,
       "agentResCtlStaticNameServerStatus": agentResCtlStaticNameServerStatus}
)
