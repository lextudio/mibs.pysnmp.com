# SNMP MIB module (ZHONE-COM-IP-DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-DHCP-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:11 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(ipInterfaceEntry,) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-REC-MIB",
    "ipInterfaceEntry")

(zhoneIp,
 zhoneModules,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules",
    "zhoneShelfIndex",
    "zhoneSlotIndex")

(ZhoneAdminString,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString")


# MODULE-IDENTITY

comIpDhcpClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 51)
)
comIpDhcpClient.setRevisions(
        ("2001-06-28 11:14",
         "2000-09-28 17:00",
         "2000-09-11 15:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhcpClient_ObjectIdentity = ObjectIdentity
dhcpClient = _DhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpClient.setStatus("current")
_DhcpClientResourceTable_Object = MibTable
dhcpClientResourceTable = _DhcpClientResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpClientResourceTable.setStatus("current")
_DhcpClientResourceEntry_Object = MibTableRow
dhcpClientResourceEntry = _DhcpClientResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 1, 1)
)
dhcpClientResourceEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    dhcpClientResourceEntry.setStatus("current")


class _DhcpOfferTimeout_Type(Unsigned32):
    """Custom type dhcpOfferTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DhcpOfferTimeout_Type.__name__ = "Unsigned32"
_DhcpOfferTimeout_Object = MibTableColumn
dhcpOfferTimeout = _DhcpOfferTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 1, 1, 1),
    _DhcpOfferTimeout_Type()
)
dhcpOfferTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOfferTimeout.setStatus("current")
if mibBuilder.loadTexts:
    dhcpOfferTimeout.setUnits("seconds")


class _DhcpDefaultLease_Type(Unsigned32):
    """Custom type dhcpDefaultLease based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 604800),
    )


_DhcpDefaultLease_Type.__name__ = "Unsigned32"
_DhcpDefaultLease_Object = MibTableColumn
dhcpDefaultLease = _DhcpDefaultLease_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 1, 1, 2),
    _DhcpDefaultLease_Type()
)
dhcpDefaultLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpDefaultLease.setStatus("current")
if mibBuilder.loadTexts:
    dhcpDefaultLease.setUnits("seconds")


class _DhcpMinLease_Type(Unsigned32):
    """Custom type dhcpMinLease based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_DhcpMinLease_Type.__name__ = "Unsigned32"
_DhcpMinLease_Object = MibTableColumn
dhcpMinLease = _DhcpMinLease_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 1, 1, 3),
    _DhcpMinLease_Type()
)
dhcpMinLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpMinLease.setStatus("current")
if mibBuilder.loadTexts:
    dhcpMinLease.setUnits("seconds")
_DhcpClientErrors_Type = Counter32
_DhcpClientErrors_Object = MibTableColumn
dhcpClientErrors = _DhcpClientErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 1, 1, 4),
    _DhcpClientErrors_Type()
)
dhcpClientErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientErrors.setStatus("current")
_DhcpAvgTimeForLease_Type = Gauge32
_DhcpAvgTimeForLease_Object = MibTableColumn
dhcpAvgTimeForLease = _DhcpAvgTimeForLease_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 1, 1, 5),
    _DhcpAvgTimeForLease_Type()
)
dhcpAvgTimeForLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAvgTimeForLease.setStatus("current")
if mibBuilder.loadTexts:
    dhcpAvgTimeForLease.setUnits("seconds")
_DhcpInterfacesTable_Object = MibTable
dhcpInterfacesTable = _DhcpInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dhcpInterfacesTable.setStatus("current")
_DhcpInterfacesEntry_Object = MibTableRow
dhcpInterfacesEntry = _DhcpInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpInterfacesEntry.setStatus("current")
_DhcpInterfaceServerName_Type = SnmpAdminString
_DhcpInterfaceServerName_Object = MibTableColumn
dhcpInterfaceServerName = _DhcpInterfaceServerName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 1),
    _DhcpInterfaceServerName_Type()
)
dhcpInterfaceServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceServerName.setStatus("current")
_DhcpInterfaceRenew_Type = Unsigned32
_DhcpInterfaceRenew_Object = MibTableColumn
dhcpInterfaceRenew = _DhcpInterfaceRenew_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 2),
    _DhcpInterfaceRenew_Type()
)
dhcpInterfaceRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceRenew.setStatus("current")
if mibBuilder.loadTexts:
    dhcpInterfaceRenew.setUnits("seconds")
_DhcpInterfaceRebind_Type = Unsigned32
_DhcpInterfaceRebind_Object = MibTableColumn
dhcpInterfaceRebind = _DhcpInterfaceRebind_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 3),
    _DhcpInterfaceRebind_Type()
)
dhcpInterfaceRebind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceRebind.setStatus("current")
if mibBuilder.loadTexts:
    dhcpInterfaceRebind.setUnits("seconds")


class _DhcpInterfaceBootFile_Type(SnmpAdminString):
    """Custom type dhcpInterfaceBootFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DhcpInterfaceBootFile_Type.__name__ = "SnmpAdminString"
_DhcpInterfaceBootFile_Object = MibTableColumn
dhcpInterfaceBootFile = _DhcpInterfaceBootFile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 4),
    _DhcpInterfaceBootFile_Type()
)
dhcpInterfaceBootFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceBootFile.setStatus("current")
_DhcpInterfaceTftp_Type = IpAddress
_DhcpInterfaceTftp_Object = MibTableColumn
dhcpInterfaceTftp = _DhcpInterfaceTftp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 5),
    _DhcpInterfaceTftp_Type()
)
dhcpInterfaceTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceTftp.setStatus("current")
_DhcpInterfaceHostname_Type = ZhoneAdminString
_DhcpInterfaceHostname_Object = MibTableColumn
dhcpInterfaceHostname = _DhcpInterfaceHostname_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 6),
    _DhcpInterfaceHostname_Type()
)
dhcpInterfaceHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceHostname.setStatus("current")
_DhcpInterfaceDomainName_Type = SnmpAdminString
_DhcpInterfaceDomainName_Object = MibTableColumn
dhcpInterfaceDomainName = _DhcpInterfaceDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 7),
    _DhcpInterfaceDomainName_Type()
)
dhcpInterfaceDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceDomainName.setStatus("current")


class _DhcpInterfaceVendorClassId_Type(OctetString):
    """Custom type dhcpInterfaceVendorClassId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DhcpInterfaceVendorClassId_Type.__name__ = "OctetString"
_DhcpInterfaceVendorClassId_Object = MibTableColumn
dhcpInterfaceVendorClassId = _DhcpInterfaceVendorClassId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 8),
    _DhcpInterfaceVendorClassId_Type()
)
dhcpInterfaceVendorClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceVendorClassId.setStatus("current")


class _DhcpInterfaceDhcpClientId_Type(OctetString):
    """Custom type dhcpInterfaceDhcpClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_DhcpInterfaceDhcpClientId_Type.__name__ = "OctetString"
_DhcpInterfaceDhcpClientId_Object = MibTableColumn
dhcpInterfaceDhcpClientId = _DhcpInterfaceDhcpClientId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 9),
    _DhcpInterfaceDhcpClientId_Type()
)
dhcpInterfaceDhcpClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpInterfaceDhcpClientId.setStatus("current")


class _DhcpInterfaceState_Type(Integer32):
    """Custom type dhcpInterfaceState based on Integer32"""
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
        *(("bind", 7),
          ("bound", 3),
          ("init", 1),
          ("invalid", 6),
          ("reboot", 2),
          ("release", 5),
          ("verify", 4))
    )


_DhcpInterfaceState_Type.__name__ = "Integer32"
_DhcpInterfaceState_Object = MibTableColumn
dhcpInterfaceState = _DhcpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 2, 1, 10),
    _DhcpInterfaceState_Type()
)
dhcpInterfaceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpInterfaceState.setStatus("current")
_DnsTable_Object = MibTable
dnsTable = _DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dnsTable.setStatus("current")
_DnsEntry_Object = MibTableRow
dnsEntry = _DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 3, 1)
)
dnsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-IP-DHCP-CLIENT-MIB", "dnsIpAddress"),
)
if mibBuilder.loadTexts:
    dnsEntry.setStatus("current")
_DnsIpAddress_Type = IpAddress
_DnsIpAddress_Object = MibTableColumn
dnsIpAddress = _DnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 3, 1, 1),
    _DnsIpAddress_Type()
)
dnsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsIpAddress.setStatus("current")
_RoutersTable_Object = MibTable
routersTable = _RoutersTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    routersTable.setStatus("current")
_RoutersEntry_Object = MibTableRow
routersEntry = _RoutersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 4, 1)
)
routersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-IP-DHCP-CLIENT-MIB", "routersIpAddress"),
)
if mibBuilder.loadTexts:
    routersEntry.setStatus("current")
_RoutersIpAddress_Type = IpAddress
_RoutersIpAddress_Object = MibTableColumn
routersIpAddress = _RoutersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 1, 4, 1, 1),
    _RoutersIpAddress_Type()
)
routersIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routersIpAddress.setStatus("current")
ipInterfaceEntry.registerAugmentions(
    ("ZHONE-COM-IP-DHCP-CLIENT-MIB",
     "dhcpInterfacesEntry")
)
dhcpInterfacesEntry.setIndexNames(*ipInterfaceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-DHCP-CLIENT-MIB",
    **{"dhcpClient": dhcpClient,
       "dhcpClientResourceTable": dhcpClientResourceTable,
       "dhcpClientResourceEntry": dhcpClientResourceEntry,
       "dhcpOfferTimeout": dhcpOfferTimeout,
       "dhcpDefaultLease": dhcpDefaultLease,
       "dhcpMinLease": dhcpMinLease,
       "dhcpClientErrors": dhcpClientErrors,
       "dhcpAvgTimeForLease": dhcpAvgTimeForLease,
       "dhcpInterfacesTable": dhcpInterfacesTable,
       "dhcpInterfacesEntry": dhcpInterfacesEntry,
       "dhcpInterfaceServerName": dhcpInterfaceServerName,
       "dhcpInterfaceRenew": dhcpInterfaceRenew,
       "dhcpInterfaceRebind": dhcpInterfaceRebind,
       "dhcpInterfaceBootFile": dhcpInterfaceBootFile,
       "dhcpInterfaceTftp": dhcpInterfaceTftp,
       "dhcpInterfaceHostname": dhcpInterfaceHostname,
       "dhcpInterfaceDomainName": dhcpInterfaceDomainName,
       "dhcpInterfaceVendorClassId": dhcpInterfaceVendorClassId,
       "dhcpInterfaceDhcpClientId": dhcpInterfaceDhcpClientId,
       "dhcpInterfaceState": dhcpInterfaceState,
       "dnsTable": dnsTable,
       "dnsEntry": dnsEntry,
       "dnsIpAddress": dnsIpAddress,
       "routersTable": routersTable,
       "routersEntry": routersEntry,
       "routersIpAddress": routersIpAddress,
       "comIpDhcpClient": comIpDhcpClient}
)
