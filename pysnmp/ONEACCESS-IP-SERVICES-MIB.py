# SNMP MIB module (ONEACCESS-IP-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-IP-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:55 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(oacExpIMIp,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIp",
    "oacMIBModules")

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

oacIpServicesConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 683)
)
oacIpServicesConfigMIB.setRevisions(
        ("2011-07-29 00:00",
         "2011-06-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacIpServicesConfig_ObjectIdentity = ObjectIdentity
oacIpServicesConfig = _OacIpServicesConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8)
)
_OacIpServicesConfigObjects_ObjectIdentity = ObjectIdentity
oacIpServicesConfigObjects = _OacIpServicesConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1)
)
_OacIpServicesDnsConfigObjects_ObjectIdentity = ObjectIdentity
oacIpServicesDnsConfigObjects = _OacIpServicesDnsConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1)
)
_OacIpDnsConfigDomainName_Type = DisplayString
_OacIpDnsConfigDomainName_Object = MibScalar
oacIpDnsConfigDomainName = _OacIpDnsConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1, 1),
    _OacIpDnsConfigDomainName_Type()
)
oacIpDnsConfigDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacIpDnsConfigDomainName.setStatus("current")


class _OacIpDnsConfigMainAdd_Type(IpAddress):
    """Custom type oacIpDnsConfigMainAdd based on IpAddress"""
    defaultHexValue = "00000000"


_OacIpDnsConfigMainAdd_Object = MibScalar
oacIpDnsConfigMainAdd = _OacIpDnsConfigMainAdd_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1, 2),
    _OacIpDnsConfigMainAdd_Type()
)
oacIpDnsConfigMainAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacIpDnsConfigMainAdd.setStatus("current")


class _OacIpDnsConfigSndAdd_Type(IpAddress):
    """Custom type oacIpDnsConfigSndAdd based on IpAddress"""
    defaultHexValue = "00000000"


_OacIpDnsConfigSndAdd_Object = MibScalar
oacIpDnsConfigSndAdd = _OacIpDnsConfigSndAdd_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1, 3),
    _OacIpDnsConfigSndAdd_Type()
)
oacIpDnsConfigSndAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacIpDnsConfigSndAdd.setStatus("current")


class _OacIpDnsConfigTimeout_Type(Integer32):
    """Custom type oacIpDnsConfigTimeout based on Integer32"""
    defaultValue = 1

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
        *(("timeoutValue12", 3),
          ("timeoutValue120", 7),
          ("timeoutValue18", 4),
          ("timeoutValue4", 2),
          ("timeoutValue42", 5),
          ("timeoutValue90", 6),
          ("timeoutValueDefault", 1))
    )


_OacIpDnsConfigTimeout_Type.__name__ = "Integer32"
_OacIpDnsConfigTimeout_Object = MibScalar
oacIpDnsConfigTimeout = _OacIpDnsConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1, 4),
    _OacIpDnsConfigTimeout_Type()
)
oacIpDnsConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacIpDnsConfigTimeout.setStatus("current")
_OacIpServicesDHCPCConfigObjects_ObjectIdentity = ObjectIdentity
oacIpServicesDHCPCConfigObjects = _OacIpServicesDHCPCConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2)
)


class _OacDhcpClientAutoRestartAtm_Type(Integer32):
    """Custom type oacDhcpClientAutoRestartAtm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OacDhcpClientAutoRestartAtm_Type.__name__ = "Integer32"
_OacDhcpClientAutoRestartAtm_Object = MibScalar
oacDhcpClientAutoRestartAtm = _OacDhcpClientAutoRestartAtm_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 1),
    _OacDhcpClientAutoRestartAtm_Type()
)
oacDhcpClientAutoRestartAtm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacDhcpClientAutoRestartAtm.setStatus("current")


class _OacDhcpClientBroadcastFlag_Type(Integer32):
    """Custom type oacDhcpClientBroadcastFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OacDhcpClientBroadcastFlag_Type.__name__ = "Integer32"
_OacDhcpClientBroadcastFlag_Object = MibScalar
oacDhcpClientBroadcastFlag = _OacDhcpClientBroadcastFlag_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 2),
    _OacDhcpClientBroadcastFlag_Type()
)
oacDhcpClientBroadcastFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacDhcpClientBroadcastFlag.setStatus("current")


class _OacDhcpVendorId_Type(OctetString):
    """Custom type oacDhcpVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 199),
    )


_OacDhcpVendorId_Type.__name__ = "OctetString"
_OacDhcpVendorId_Object = MibScalar
oacDhcpVendorId = _OacDhcpVendorId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 3),
    _OacDhcpVendorId_Type()
)
oacDhcpVendorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacDhcpVendorId.setStatus("current")
_OacIpDhcpClientInterfaceTable_Object = MibTable
oacIpDhcpClientInterfaceTable = _OacIpDhcpClientInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    oacIpDhcpClientInterfaceTable.setStatus("current")
_OacIpDhcpClientInterfaceEntry_Object = MibTableRow
oacIpDhcpClientInterfaceEntry = _OacIpDhcpClientInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1)
)
oacIpDhcpClientInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacIpDhcpClientInterfaceEntry.setStatus("current")
_OacIpDhcpClientInterfaceIfName_Type = DisplayString
_OacIpDhcpClientInterfaceIfName_Object = MibTableColumn
oacIpDhcpClientInterfaceIfName = _OacIpDhcpClientInterfaceIfName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 1),
    _OacIpDhcpClientInterfaceIfName_Type()
)
oacIpDhcpClientInterfaceIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpDhcpClientInterfaceIfName.setStatus("current")


class _OacIpDhcpClientInterfaceIgnoreDefRoute_Type(TruthValue):
    """Custom type oacIpDhcpClientInterfaceIgnoreDefRoute based on TruthValue"""


_OacIpDhcpClientInterfaceIgnoreDefRoute_Object = MibTableColumn
oacIpDhcpClientInterfaceIgnoreDefRoute = _OacIpDhcpClientInterfaceIgnoreDefRoute_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 2),
    _OacIpDhcpClientInterfaceIgnoreDefRoute_Type()
)
oacIpDhcpClientInterfaceIgnoreDefRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpDhcpClientInterfaceIgnoreDefRoute.setStatus("current")


class _OacIpDhcpClientInterfaceLeaseOptLess_Type(TruthValue):
    """Custom type oacIpDhcpClientInterfaceLeaseOptLess based on TruthValue"""


_OacIpDhcpClientInterfaceLeaseOptLess_Object = MibTableColumn
oacIpDhcpClientInterfaceLeaseOptLess = _OacIpDhcpClientInterfaceLeaseOptLess_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 3),
    _OacIpDhcpClientInterfaceLeaseOptLess_Type()
)
oacIpDhcpClientInterfaceLeaseOptLess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpDhcpClientInterfaceLeaseOptLess.setStatus("current")
_OacIpDhcpClientInterfaceUserClassId_Type = DisplayString
_OacIpDhcpClientInterfaceUserClassId_Object = MibTableColumn
oacIpDhcpClientInterfaceUserClassId = _OacIpDhcpClientInterfaceUserClassId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 4),
    _OacIpDhcpClientInterfaceUserClassId_Type()
)
oacIpDhcpClientInterfaceUserClassId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpDhcpClientInterfaceUserClassId.setStatus("current")
_OacIpDhcpClientInterfaceRowStatus_Type = RowStatus
_OacIpDhcpClientInterfaceRowStatus_Object = MibTableColumn
oacIpDhcpClientInterfaceRowStatus = _OacIpDhcpClientInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 5),
    _OacIpDhcpClientInterfaceRowStatus_Type()
)
oacIpDhcpClientInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpDhcpClientInterfaceRowStatus.setStatus("current")
_OacIpDhcpAddClientInterfaceTable_Object = MibTable
oacIpDhcpAddClientInterfaceTable = _OacIpDhcpAddClientInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    oacIpDhcpAddClientInterfaceTable.setStatus("current")
_OacIpDhcpAddClientInterfaceEntry_Object = MibTableRow
oacIpDhcpAddClientInterfaceEntry = _OacIpDhcpAddClientInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1)
)
oacIpDhcpAddClientInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacIpDhcpAddClientInterfaceEntry.setStatus("current")


class _OacIpDhcpAddClientInterfaceActivate_Type(TruthValue):
    """Custom type oacIpDhcpAddClientInterfaceActivate based on TruthValue"""


_OacIpDhcpAddClientInterfaceActivate_Object = MibTableColumn
oacIpDhcpAddClientInterfaceActivate = _OacIpDhcpAddClientInterfaceActivate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 1),
    _OacIpDhcpAddClientInterfaceActivate_Type()
)
oacIpDhcpAddClientInterfaceActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpDhcpAddClientInterfaceActivate.setStatus("current")
_OacIpDhcpAddClientInterfaceIfName_Type = DisplayString
_OacIpDhcpAddClientInterfaceIfName_Object = MibTableColumn
oacIpDhcpAddClientInterfaceIfName = _OacIpDhcpAddClientInterfaceIfName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 2),
    _OacIpDhcpAddClientInterfaceIfName_Type()
)
oacIpDhcpAddClientInterfaceIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpDhcpAddClientInterfaceIfName.setStatus("current")
_OacIpDhcpAddClientInterfaceClientId_Type = DisplayString
_OacIpDhcpAddClientInterfaceClientId_Object = MibTableColumn
oacIpDhcpAddClientInterfaceClientId = _OacIpDhcpAddClientInterfaceClientId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 3),
    _OacIpDhcpAddClientInterfaceClientId_Type()
)
oacIpDhcpAddClientInterfaceClientId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpDhcpAddClientInterfaceClientId.setStatus("current")
_OacIpDhcpAddClientInterfaceHostname_Type = DisplayString
_OacIpDhcpAddClientInterfaceHostname_Object = MibTableColumn
oacIpDhcpAddClientInterfaceHostname = _OacIpDhcpAddClientInterfaceHostname_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 4),
    _OacIpDhcpAddClientInterfaceHostname_Type()
)
oacIpDhcpAddClientInterfaceHostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpDhcpAddClientInterfaceHostname.setStatus("current")
_OacIpDhcpAddClientInterfaceRowStatus_Type = RowStatus
_OacIpDhcpAddClientInterfaceRowStatus_Object = MibTableColumn
oacIpDhcpAddClientInterfaceRowStatus = _OacIpDhcpAddClientInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 5),
    _OacIpDhcpAddClientInterfaceRowStatus_Type()
)
oacIpDhcpAddClientInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpDhcpAddClientInterfaceRowStatus.setStatus("current")
_OacIpServicesArpProxyConfigObjects_ObjectIdentity = ObjectIdentity
oacIpServicesArpProxyConfigObjects = _OacIpServicesArpProxyConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3)
)
_OacIpProxyArpInterfaceConfigTable_Object = MibTable
oacIpProxyArpInterfaceConfigTable = _OacIpProxyArpInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    oacIpProxyArpInterfaceConfigTable.setStatus("current")
_OacIpProxyArpInterfaceConfigEntry_Object = MibTableRow
oacIpProxyArpInterfaceConfigEntry = _OacIpProxyArpInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1, 1)
)
oacIpProxyArpInterfaceConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacIpProxyArpInterfaceConfigEntry.setStatus("current")


class _OacIpProxyArpInterfaceConfigActivate_Type(TruthValue):
    """Custom type oacIpProxyArpInterfaceConfigActivate based on TruthValue"""


_OacIpProxyArpInterfaceConfigActivate_Object = MibTableColumn
oacIpProxyArpInterfaceConfigActivate = _OacIpProxyArpInterfaceConfigActivate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1, 1, 1),
    _OacIpProxyArpInterfaceConfigActivate_Type()
)
oacIpProxyArpInterfaceConfigActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpProxyArpInterfaceConfigActivate.setStatus("current")
_OacIpProxyArpInterfaceConfigIfName_Type = DisplayString
_OacIpProxyArpInterfaceConfigIfName_Object = MibTableColumn
oacIpProxyArpInterfaceConfigIfName = _OacIpProxyArpInterfaceConfigIfName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1, 1, 2),
    _OacIpProxyArpInterfaceConfigIfName_Type()
)
oacIpProxyArpInterfaceConfigIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacIpProxyArpInterfaceConfigIfName.setStatus("current")
_OacIpProxyArpInterfaceConfigRowStatus_Type = RowStatus
_OacIpProxyArpInterfaceConfigRowStatus_Object = MibTableColumn
oacIpProxyArpInterfaceConfigRowStatus = _OacIpProxyArpInterfaceConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1, 1, 3),
    _OacIpProxyArpInterfaceConfigRowStatus_Type()
)
oacIpProxyArpInterfaceConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacIpProxyArpInterfaceConfigRowStatus.setStatus("current")
_OacIpServicesIcmpRedirConfigObjects_ObjectIdentity = ObjectIdentity
oacIpServicesIcmpRedirConfigObjects = _OacIpServicesIcmpRedirConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 4)
)


class _OacIpIcmpRedirConfigActivate_Type(TruthValue):
    """Custom type oacIpIcmpRedirConfigActivate based on TruthValue"""


_OacIpIcmpRedirConfigActivate_Object = MibScalar
oacIpIcmpRedirConfigActivate = _OacIpIcmpRedirConfigActivate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 4, 1),
    _OacIpIcmpRedirConfigActivate_Type()
)
oacIpIcmpRedirConfigActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacIpIcmpRedirConfigActivate.setStatus("current")


class _OacIpIcmpRedirConfigRedirRoutesActivate_Type(Integer32):
    """Custom type oacIpIcmpRedirConfigRedirRoutesActivate based on Integer32"""
    defaultValue = 0


_OacIpIcmpRedirConfigRedirRoutesActivate_Object = MibScalar
oacIpIcmpRedirConfigRedirRoutesActivate = _OacIpIcmpRedirConfigRedirRoutesActivate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 4, 2),
    _OacIpIcmpRedirConfigRedirRoutesActivate_Type()
)
oacIpIcmpRedirConfigRedirRoutesActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacIpIcmpRedirConfigRedirRoutesActivate.setStatus("current")


class _OacIpIcmpRedirConfigRateLimitUnreach_Type(Integer32):
    """Custom type oacIpIcmpRedirConfigRateLimitUnreach based on Integer32"""
    defaultValue = 0


_OacIpIcmpRedirConfigRateLimitUnreach_Object = MibScalar
oacIpIcmpRedirConfigRateLimitUnreach = _OacIpIcmpRedirConfigRateLimitUnreach_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 4, 3),
    _OacIpIcmpRedirConfigRateLimitUnreach_Type()
)
oacIpIcmpRedirConfigRateLimitUnreach.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacIpIcmpRedirConfigRateLimitUnreach.setStatus("current")
_OacIpServicesConfigConformance_ObjectIdentity = ObjectIdentity
oacIpServicesConfigConformance = _OacIpServicesConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 2)
)
_OacIpServicesGroups_ObjectIdentity = ObjectIdentity
oacIpServicesGroups = _OacIpServicesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 2, 1)
)
_OacIpServicesCompls_ObjectIdentity = ObjectIdentity
oacIpServicesCompls = _OacIpServicesCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 2, 2)
)

# Managed Objects groups

oacIpServicesConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 2, 1, 1)
)
oacIpServicesConfigGroup.setObjects(
    ("ONEACCESS-IP-SERVICES-MIB", "oacIpDnsConfigDomainName")
)
if mibBuilder.loadTexts:
    oacIpServicesConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-IP-SERVICES-MIB",
    **{"oacIpServicesConfigMIB": oacIpServicesConfigMIB,
       "oacIpServicesConfig": oacIpServicesConfig,
       "oacIpServicesConfigObjects": oacIpServicesConfigObjects,
       "oacIpServicesDnsConfigObjects": oacIpServicesDnsConfigObjects,
       "oacIpDnsConfigDomainName": oacIpDnsConfigDomainName,
       "oacIpDnsConfigMainAdd": oacIpDnsConfigMainAdd,
       "oacIpDnsConfigSndAdd": oacIpDnsConfigSndAdd,
       "oacIpDnsConfigTimeout": oacIpDnsConfigTimeout,
       "oacIpServicesDHCPCConfigObjects": oacIpServicesDHCPCConfigObjects,
       "oacDhcpClientAutoRestartAtm": oacDhcpClientAutoRestartAtm,
       "oacDhcpClientBroadcastFlag": oacDhcpClientBroadcastFlag,
       "oacDhcpVendorId": oacDhcpVendorId,
       "oacIpDhcpClientInterfaceTable": oacIpDhcpClientInterfaceTable,
       "oacIpDhcpClientInterfaceEntry": oacIpDhcpClientInterfaceEntry,
       "oacIpDhcpClientInterfaceIfName": oacIpDhcpClientInterfaceIfName,
       "oacIpDhcpClientInterfaceIgnoreDefRoute": oacIpDhcpClientInterfaceIgnoreDefRoute,
       "oacIpDhcpClientInterfaceLeaseOptLess": oacIpDhcpClientInterfaceLeaseOptLess,
       "oacIpDhcpClientInterfaceUserClassId": oacIpDhcpClientInterfaceUserClassId,
       "oacIpDhcpClientInterfaceRowStatus": oacIpDhcpClientInterfaceRowStatus,
       "oacIpDhcpAddClientInterfaceTable": oacIpDhcpAddClientInterfaceTable,
       "oacIpDhcpAddClientInterfaceEntry": oacIpDhcpAddClientInterfaceEntry,
       "oacIpDhcpAddClientInterfaceActivate": oacIpDhcpAddClientInterfaceActivate,
       "oacIpDhcpAddClientInterfaceIfName": oacIpDhcpAddClientInterfaceIfName,
       "oacIpDhcpAddClientInterfaceClientId": oacIpDhcpAddClientInterfaceClientId,
       "oacIpDhcpAddClientInterfaceHostname": oacIpDhcpAddClientInterfaceHostname,
       "oacIpDhcpAddClientInterfaceRowStatus": oacIpDhcpAddClientInterfaceRowStatus,
       "oacIpServicesArpProxyConfigObjects": oacIpServicesArpProxyConfigObjects,
       "oacIpProxyArpInterfaceConfigTable": oacIpProxyArpInterfaceConfigTable,
       "oacIpProxyArpInterfaceConfigEntry": oacIpProxyArpInterfaceConfigEntry,
       "oacIpProxyArpInterfaceConfigActivate": oacIpProxyArpInterfaceConfigActivate,
       "oacIpProxyArpInterfaceConfigIfName": oacIpProxyArpInterfaceConfigIfName,
       "oacIpProxyArpInterfaceConfigRowStatus": oacIpProxyArpInterfaceConfigRowStatus,
       "oacIpServicesIcmpRedirConfigObjects": oacIpServicesIcmpRedirConfigObjects,
       "oacIpIcmpRedirConfigActivate": oacIpIcmpRedirConfigActivate,
       "oacIpIcmpRedirConfigRedirRoutesActivate": oacIpIcmpRedirConfigRedirRoutesActivate,
       "oacIpIcmpRedirConfigRateLimitUnreach": oacIpIcmpRedirConfigRateLimitUnreach,
       "oacIpServicesConfigConformance": oacIpServicesConfigConformance,
       "oacIpServicesGroups": oacIpServicesGroups,
       "oacIpServicesConfigGroup": oacIpServicesConfigGroup,
       "oacIpServicesCompls": oacIpServicesCompls}
)
