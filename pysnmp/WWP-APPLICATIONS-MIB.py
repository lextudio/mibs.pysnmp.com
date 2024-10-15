# SNMP MIB module (WWP-APPLICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-APPLICATIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:35 2024
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

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpApplicationsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6)
)
wwpApplicationsMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpApplicationsMIBObjects_ObjectIdentity = ObjectIdentity
wwpApplicationsMIBObjects = _WwpApplicationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1)
)
_WwpWeb_ObjectIdentity = ObjectIdentity
wwpWeb = _WwpWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 2)
)


class _WwpWebEnable_Type(Integer32):
    """Custom type wwpWebEnable based on Integer32"""
    defaultValue = 1

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


_WwpWebEnable_Type.__name__ = "Integer32"
_WwpWebEnable_Object = MibScalar
wwpWebEnable = _WwpWebEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 2, 1),
    _WwpWebEnable_Type()
)
wwpWebEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpWebEnable.setStatus("current")


class _WwpWebMaxLogins_Type(Integer32):
    """Custom type wwpWebMaxLogins based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_WwpWebMaxLogins_Type.__name__ = "Integer32"
_WwpWebMaxLogins_Object = MibScalar
wwpWebMaxLogins = _WwpWebMaxLogins_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 2, 2),
    _WwpWebMaxLogins_Type()
)
wwpWebMaxLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpWebMaxLogins.setStatus("current")


class _WwpWebInactivityTimeout_Type(Integer32):
    """Custom type wwpWebInactivityTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WwpWebInactivityTimeout_Type.__name__ = "Integer32"
_WwpWebInactivityTimeout_Object = MibScalar
wwpWebInactivityTimeout = _WwpWebInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 2, 3),
    _WwpWebInactivityTimeout_Type()
)
wwpWebInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpWebInactivityTimeout.setStatus("current")
_WwpTelnet_ObjectIdentity = ObjectIdentity
wwpTelnet = _WwpTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 3)
)


class _WwpTelnetEnableServer_Type(Integer32):
    """Custom type wwpTelnetEnableServer based on Integer32"""
    defaultValue = 1

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


_WwpTelnetEnableServer_Type.__name__ = "Integer32"
_WwpTelnetEnableServer_Object = MibScalar
wwpTelnetEnableServer = _WwpTelnetEnableServer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 3, 1),
    _WwpTelnetEnableServer_Type()
)
wwpTelnetEnableServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpTelnetEnableServer.setStatus("current")


class _WwpTelnetMaxConnections_Type(Integer32):
    """Custom type wwpTelnetMaxConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_WwpTelnetMaxConnections_Type.__name__ = "Integer32"
_WwpTelnetMaxConnections_Object = MibScalar
wwpTelnetMaxConnections = _WwpTelnetMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 3, 2),
    _WwpTelnetMaxConnections_Type()
)
wwpTelnetMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpTelnetMaxConnections.setStatus("current")


class _WwpTelnetTimeout_Type(Integer32):
    """Custom type wwpTelnetTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_WwpTelnetTimeout_Type.__name__ = "Integer32"
_WwpTelnetTimeout_Object = MibScalar
wwpTelnetTimeout = _WwpTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 3, 3),
    _WwpTelnetTimeout_Type()
)
wwpTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpTelnetTimeout.setStatus("current")


class _WwpTelnetEnableClient_Type(Integer32):
    """Custom type wwpTelnetEnableClient based on Integer32"""
    defaultValue = 1

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


_WwpTelnetEnableClient_Type.__name__ = "Integer32"
_WwpTelnetEnableClient_Object = MibScalar
wwpTelnetEnableClient = _WwpTelnetEnableClient_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 3, 4),
    _WwpTelnetEnableClient_Type()
)
wwpTelnetEnableClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpTelnetEnableClient.setStatus("current")
_WwpDns_ObjectIdentity = ObjectIdentity
wwpDns = _WwpDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 4)
)


class _WwpDnsEnable_Type(Integer32):
    """Custom type wwpDnsEnable based on Integer32"""
    defaultValue = 1

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


_WwpDnsEnable_Type.__name__ = "Integer32"
_WwpDnsEnable_Object = MibScalar
wwpDnsEnable = _WwpDnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 4, 1),
    _WwpDnsEnable_Type()
)
wwpDnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDnsEnable.setStatus("current")


class _WwpDnsDomainName_Type(DisplayString):
    """Custom type wwpDnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpDnsDomainName_Type.__name__ = "DisplayString"
_WwpDnsDomainName_Object = MibScalar
wwpDnsDomainName = _WwpDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 4, 2),
    _WwpDnsDomainName_Type()
)
wwpDnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDnsDomainName.setStatus("current")
_WwpDnsServerTable_Object = MibTable
wwpDnsServerTable = _WwpDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    wwpDnsServerTable.setStatus("current")
_WwpDnsServerEntry_Object = MibTableRow
wwpDnsServerEntry = _WwpDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 4, 3, 1)
)
wwpDnsServerEntry.setIndexNames(
    (0, "WWP-APPLICATIONS-MIB", "wwpDnsServerIpAddr"),
)
if mibBuilder.loadTexts:
    wwpDnsServerEntry.setStatus("current")
_WwpDnsServerIpAddr_Type = IpAddress
_WwpDnsServerIpAddr_Object = MibTableColumn
wwpDnsServerIpAddr = _WwpDnsServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 4, 3, 1, 1),
    _WwpDnsServerIpAddr_Type()
)
wwpDnsServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDnsServerIpAddr.setStatus("current")


class _WwpDnsServerPrimary_Type(Integer32):
    """Custom type wwpDnsServerPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_WwpDnsServerPrimary_Type.__name__ = "Integer32"
_WwpDnsServerPrimary_Object = MibTableColumn
wwpDnsServerPrimary = _WwpDnsServerPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 4, 3, 1, 2),
    _WwpDnsServerPrimary_Type()
)
wwpDnsServerPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDnsServerPrimary.setStatus("current")
_WwpDnsServerRowStatus_Type = RowStatus
_WwpDnsServerRowStatus_Object = MibTableColumn
wwpDnsServerRowStatus = _WwpDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 4, 3, 1, 3),
    _WwpDnsServerRowStatus_Type()
)
wwpDnsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpDnsServerRowStatus.setStatus("current")
_WwpLog_ObjectIdentity = ObjectIdentity
wwpLog = _WwpLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 5)
)
_WwpLogServerAddr_Type = IpAddress
_WwpLogServerAddr_Object = MibScalar
wwpLogServerAddr = _WwpLogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 5, 1),
    _WwpLogServerAddr_Type()
)
wwpLogServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLogServerAddr.setStatus("current")


class _WwpLogServerPort_Type(Integer32):
    """Custom type wwpLogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLogServerPort_Type.__name__ = "Integer32"
_WwpLogServerPort_Object = MibScalar
wwpLogServerPort = _WwpLogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 1, 5, 2),
    _WwpLogServerPort_Type()
)
wwpLogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLogServerPort.setStatus("current")
_WwpApplicationsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpApplicationsMIBNotificationPrefix = _WwpApplicationsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 2)
)
_WwpApplicationsMIBNotifications_ObjectIdentity = ObjectIdentity
wwpApplicationsMIBNotifications = _WwpApplicationsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 2, 0)
)
_WwpApplicationsMIBConformance_ObjectIdentity = ObjectIdentity
wwpApplicationsMIBConformance = _WwpApplicationsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 3)
)
_WwpApplicationsMIBCompliances_ObjectIdentity = ObjectIdentity
wwpApplicationsMIBCompliances = _WwpApplicationsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 3, 1)
)
_WwpApplicationsMIBGroups_ObjectIdentity = ObjectIdentity
wwpApplicationsMIBGroups = _WwpApplicationsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 6, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-APPLICATIONS-MIB",
    **{"wwpApplicationsMIB": wwpApplicationsMIB,
       "wwpApplicationsMIBObjects": wwpApplicationsMIBObjects,
       "wwpWeb": wwpWeb,
       "wwpWebEnable": wwpWebEnable,
       "wwpWebMaxLogins": wwpWebMaxLogins,
       "wwpWebInactivityTimeout": wwpWebInactivityTimeout,
       "wwpTelnet": wwpTelnet,
       "wwpTelnetEnableServer": wwpTelnetEnableServer,
       "wwpTelnetMaxConnections": wwpTelnetMaxConnections,
       "wwpTelnetTimeout": wwpTelnetTimeout,
       "wwpTelnetEnableClient": wwpTelnetEnableClient,
       "wwpDns": wwpDns,
       "wwpDnsEnable": wwpDnsEnable,
       "wwpDnsDomainName": wwpDnsDomainName,
       "wwpDnsServerTable": wwpDnsServerTable,
       "wwpDnsServerEntry": wwpDnsServerEntry,
       "wwpDnsServerIpAddr": wwpDnsServerIpAddr,
       "wwpDnsServerPrimary": wwpDnsServerPrimary,
       "wwpDnsServerRowStatus": wwpDnsServerRowStatus,
       "wwpLog": wwpLog,
       "wwpLogServerAddr": wwpLogServerAddr,
       "wwpLogServerPort": wwpLogServerPort,
       "wwpApplicationsMIBNotificationPrefix": wwpApplicationsMIBNotificationPrefix,
       "wwpApplicationsMIBNotifications": wwpApplicationsMIBNotifications,
       "wwpApplicationsMIBConformance": wwpApplicationsMIBConformance,
       "wwpApplicationsMIBCompliances": wwpApplicationsMIBCompliances,
       "wwpApplicationsMIBGroups": wwpApplicationsMIBGroups}
)
