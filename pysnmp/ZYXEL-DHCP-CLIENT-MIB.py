# SNMP MIB module (ZYXEL-DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-DHCP-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:31 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelDhcpClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDhcpClientSetup_ObjectIdentity = ObjectIdentity
zyxelDhcpClientSetup = _ZyxelDhcpClientSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1)
)
_ZyxelDhcpClientMaxNumberOfClient_Type = Integer32
_ZyxelDhcpClientMaxNumberOfClient_Object = MibScalar
zyxelDhcpClientMaxNumberOfClient = _ZyxelDhcpClientMaxNumberOfClient_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 1),
    _ZyxelDhcpClientMaxNumberOfClient_Type()
)
zyxelDhcpClientMaxNumberOfClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyxelDhcpClientMaxNumberOfClient.setStatus("current")
_ZyxelDhcpClientTable_Object = MibTable
zyxelDhcpClientTable = _ZyxelDhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelDhcpClientTable.setStatus("current")
_ZyxelDhcpClientEntry_Object = MibTableRow
zyxelDhcpClientEntry = _ZyxelDhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 2, 1)
)
zyxelDhcpClientEntry.setIndexNames(
    (0, "ZYXEL-DHCP-CLIENT-MIB", "zyDhcpClientID"),
)
if mibBuilder.loadTexts:
    zyxelDhcpClientEntry.setStatus("current")
_ZyDhcpClientID_Type = Integer32
_ZyDhcpClientID_Object = MibTableColumn
zyDhcpClientID = _ZyDhcpClientID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 2, 1, 1),
    _ZyDhcpClientID_Type()
)
zyDhcpClientID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDhcpClientID.setStatus("current")
_ZyDhcpClientRowStatus_Type = RowStatus
_ZyDhcpClientRowStatus_Object = MibTableColumn
zyDhcpClientRowStatus = _ZyDhcpClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 2, 1, 2),
    _ZyDhcpClientRowStatus_Type()
)
zyDhcpClientRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpClientRowStatus.setStatus("current")
_ZyxelDhcpClientStatus_ObjectIdentity = ObjectIdentity
zyxelDhcpClientStatus = _ZyxelDhcpClientStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2)
)
_ZyxelDhcpClientInfoTable_Object = MibTable
zyxelDhcpClientInfoTable = _ZyxelDhcpClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelDhcpClientInfoTable.setStatus("current")
_ZyxelDhcpClientInfoEntry_Object = MibTableRow
zyxelDhcpClientInfoEntry = _ZyxelDhcpClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1)
)
zyxelDhcpClientInfoEntry.setIndexNames(
    (0, "ZYXEL-DHCP-CLIENT-MIB", "zyDhcpClientInfoID"),
)
if mibBuilder.loadTexts:
    zyxelDhcpClientInfoEntry.setStatus("current")
_ZyDhcpClientInfoID_Type = Integer32
_ZyDhcpClientInfoID_Object = MibTableColumn
zyDhcpClientInfoID = _ZyDhcpClientInfoID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 1),
    _ZyDhcpClientInfoID_Type()
)
zyDhcpClientInfoID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDhcpClientInfoID.setStatus("current")
_ZyDhcpClientInfoIpAddress_Type = IpAddress
_ZyDhcpClientInfoIpAddress_Object = MibTableColumn
zyDhcpClientInfoIpAddress = _ZyDhcpClientInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 2),
    _ZyDhcpClientInfoIpAddress_Type()
)
zyDhcpClientInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoIpAddress.setStatus("current")
_ZyDhcpClientInfoMask_Type = IpAddress
_ZyDhcpClientInfoMask_Object = MibTableColumn
zyDhcpClientInfoMask = _ZyDhcpClientInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 3),
    _ZyDhcpClientInfoMask_Type()
)
zyDhcpClientInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoMask.setStatus("current")
_ZyDhcpClientInfoLeaseTime_Type = Integer32
_ZyDhcpClientInfoLeaseTime_Object = MibTableColumn
zyDhcpClientInfoLeaseTime = _ZyDhcpClientInfoLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 4),
    _ZyDhcpClientInfoLeaseTime_Type()
)
zyDhcpClientInfoLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoLeaseTime.setStatus("current")
_ZyDhcpClientInfoRenewTime_Type = Integer32
_ZyDhcpClientInfoRenewTime_Object = MibTableColumn
zyDhcpClientInfoRenewTime = _ZyDhcpClientInfoRenewTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 5),
    _ZyDhcpClientInfoRenewTime_Type()
)
zyDhcpClientInfoRenewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoRenewTime.setStatus("current")
_ZyDhcpClientInfoRebindTime_Type = Integer32
_ZyDhcpClientInfoRebindTime_Object = MibTableColumn
zyDhcpClientInfoRebindTime = _ZyDhcpClientInfoRebindTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 6),
    _ZyDhcpClientInfoRebindTime_Type()
)
zyDhcpClientInfoRebindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoRebindTime.setStatus("current")
_ZyDhcpClientInfoLeaseFrom_Type = DisplayString
_ZyDhcpClientInfoLeaseFrom_Object = MibTableColumn
zyDhcpClientInfoLeaseFrom = _ZyDhcpClientInfoLeaseFrom_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 7),
    _ZyDhcpClientInfoLeaseFrom_Type()
)
zyDhcpClientInfoLeaseFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoLeaseFrom.setStatus("current")
_ZyDhcpClientInfoLeaseTo_Type = DisplayString
_ZyDhcpClientInfoLeaseTo_Object = MibTableColumn
zyDhcpClientInfoLeaseTo = _ZyDhcpClientInfoLeaseTo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 8),
    _ZyDhcpClientInfoLeaseTo_Type()
)
zyDhcpClientInfoLeaseTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoLeaseTo.setStatus("current")
_ZyDhcpClientInfoDhcpServer_Type = IpAddress
_ZyDhcpClientInfoDhcpServer_Object = MibTableColumn
zyDhcpClientInfoDhcpServer = _ZyDhcpClientInfoDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 9),
    _ZyDhcpClientInfoDhcpServer_Type()
)
zyDhcpClientInfoDhcpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoDhcpServer.setStatus("current")
_ZyDhcpClientInfoDnsServer1_Type = IpAddress
_ZyDhcpClientInfoDnsServer1_Object = MibTableColumn
zyDhcpClientInfoDnsServer1 = _ZyDhcpClientInfoDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 10),
    _ZyDhcpClientInfoDnsServer1_Type()
)
zyDhcpClientInfoDnsServer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoDnsServer1.setStatus("current")
_ZyDhcpClientInfoDnsServer2_Type = IpAddress
_ZyDhcpClientInfoDnsServer2_Object = MibTableColumn
zyDhcpClientInfoDnsServer2 = _ZyDhcpClientInfoDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 11),
    _ZyDhcpClientInfoDnsServer2_Type()
)
zyDhcpClientInfoDnsServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoDnsServer2.setStatus("current")
_ZyDhcpClientInfoDefaultGateway_Type = IpAddress
_ZyDhcpClientInfoDefaultGateway_Object = MibTableColumn
zyDhcpClientInfoDefaultGateway = _ZyDhcpClientInfoDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 12),
    _ZyDhcpClientInfoDefaultGateway_Type()
)
zyDhcpClientInfoDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpClientInfoDefaultGateway.setStatus("current")
_ZyDhcpClientInfoRelease_Type = EnabledStatus
_ZyDhcpClientInfoRelease_Object = MibTableColumn
zyDhcpClientInfoRelease = _ZyDhcpClientInfoRelease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 13),
    _ZyDhcpClientInfoRelease_Type()
)
zyDhcpClientInfoRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpClientInfoRelease.setStatus("current")
_ZyDhcpClientInfoRenew_Type = EnabledStatus
_ZyDhcpClientInfoRenew_Object = MibTableColumn
zyDhcpClientInfoRenew = _ZyDhcpClientInfoRenew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 14),
    _ZyDhcpClientInfoRenew_Type()
)
zyDhcpClientInfoRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpClientInfoRenew.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DHCP-CLIENT-MIB",
    **{"zyxelDhcpClient": zyxelDhcpClient,
       "zyxelDhcpClientSetup": zyxelDhcpClientSetup,
       "zyxelDhcpClientMaxNumberOfClient": zyxelDhcpClientMaxNumberOfClient,
       "zyxelDhcpClientTable": zyxelDhcpClientTable,
       "zyxelDhcpClientEntry": zyxelDhcpClientEntry,
       "zyDhcpClientID": zyDhcpClientID,
       "zyDhcpClientRowStatus": zyDhcpClientRowStatus,
       "zyxelDhcpClientStatus": zyxelDhcpClientStatus,
       "zyxelDhcpClientInfoTable": zyxelDhcpClientInfoTable,
       "zyxelDhcpClientInfoEntry": zyxelDhcpClientInfoEntry,
       "zyDhcpClientInfoID": zyDhcpClientInfoID,
       "zyDhcpClientInfoIpAddress": zyDhcpClientInfoIpAddress,
       "zyDhcpClientInfoMask": zyDhcpClientInfoMask,
       "zyDhcpClientInfoLeaseTime": zyDhcpClientInfoLeaseTime,
       "zyDhcpClientInfoRenewTime": zyDhcpClientInfoRenewTime,
       "zyDhcpClientInfoRebindTime": zyDhcpClientInfoRebindTime,
       "zyDhcpClientInfoLeaseFrom": zyDhcpClientInfoLeaseFrom,
       "zyDhcpClientInfoLeaseTo": zyDhcpClientInfoLeaseTo,
       "zyDhcpClientInfoDhcpServer": zyDhcpClientInfoDhcpServer,
       "zyDhcpClientInfoDnsServer1": zyDhcpClientInfoDnsServer1,
       "zyDhcpClientInfoDnsServer2": zyDhcpClientInfoDnsServer2,
       "zyDhcpClientInfoDefaultGateway": zyDhcpClientInfoDefaultGateway,
       "zyDhcpClientInfoRelease": zyDhcpClientInfoRelease,
       "zyDhcpClientInfoRenew": zyDhcpClientInfoRenew}
)
