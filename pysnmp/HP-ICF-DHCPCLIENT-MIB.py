# SNMP MIB module (HP-ICF-DHCPCLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DHCPCLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:17 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetVersion,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetVersion")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpicfDhcpClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57)
)
hpicfDhcpClient.setRevisions(
        ("2013-06-01 00:00",
         "2012-05-31 00:00",
         "2010-08-09 00:00",
         "2009-03-18 00:00",
         "2008-10-30 00:00",
         "2008-08-27 00:38")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDhcpClientOptions_ObjectIdentity = ObjectIdentity
hpicfDhcpClientOptions = _HpicfDhcpClientOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1)
)


class _HpicfDhcpClientVendorSpecOptionStatus_Type(Integer32):
    """Custom type hpicfDhcpClientVendorSpecOptionStatus based on Integer32"""
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


_HpicfDhcpClientVendorSpecOptionStatus_Type.__name__ = "Integer32"
_HpicfDhcpClientVendorSpecOptionStatus_Object = MibScalar
hpicfDhcpClientVendorSpecOptionStatus = _HpicfDhcpClientVendorSpecOptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 1),
    _HpicfDhcpClientVendorSpecOptionStatus_Type()
)
hpicfDhcpClientVendorSpecOptionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpClientVendorSpecOptionStatus.setStatus("current")


class _HpicfDhcpClientHostNameOption_Type(Integer32):
    """Custom type hpicfDhcpClientHostNameOption based on Integer32"""
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


_HpicfDhcpClientHostNameOption_Type.__name__ = "Integer32"
_HpicfDhcpClientHostNameOption_Object = MibScalar
hpicfDhcpClientHostNameOption = _HpicfDhcpClientHostNameOption_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 2),
    _HpicfDhcpClientHostNameOption_Type()
)
hpicfDhcpClientHostNameOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpClientHostNameOption.setStatus("current")


class _HpicfDhcpClientImageFileUpdate_Type(Integer32):
    """Custom type hpicfDhcpClientImageFileUpdate based on Integer32"""
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


_HpicfDhcpClientImageFileUpdate_Type.__name__ = "Integer32"
_HpicfDhcpClientImageFileUpdate_Object = MibScalar
hpicfDhcpClientImageFileUpdate = _HpicfDhcpClientImageFileUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 3),
    _HpicfDhcpClientImageFileUpdate_Type()
)
hpicfDhcpClientImageFileUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpClientImageFileUpdate.setStatus("current")
_HpicfDhcpClientintfTable_Object = MibTable
hpicfDhcpClientintfTable = _HpicfDhcpClientintfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfDhcpClientintfTable.setStatus("current")
_HpicfDhcpClientintfEntry_Object = MibTableRow
hpicfDhcpClientintfEntry = _HpicfDhcpClientintfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 4, 1)
)
hpicfDhcpClientintfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfDhcpClientintfEntry.setStatus("current")


class _HpicfDhcpClientAuthType_Type(Integer32):
    """Custom type hpicfDhcpClientAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("none", 0))
    )


_HpicfDhcpClientAuthType_Type.__name__ = "Integer32"
_HpicfDhcpClientAuthType_Object = MibTableColumn
hpicfDhcpClientAuthType = _HpicfDhcpClientAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 4, 1, 1),
    _HpicfDhcpClientAuthType_Type()
)
hpicfDhcpClientAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpClientAuthType.setStatus("current")


class _HpicfDhcpClientKeyChain_Type(DisplayString):
    """Custom type hpicfDhcpClientKeyChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpicfDhcpClientKeyChain_Type.__name__ = "DisplayString"
_HpicfDhcpClientKeyChain_Object = MibTableColumn
hpicfDhcpClientKeyChain = _HpicfDhcpClientKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 4, 1, 2),
    _HpicfDhcpClientKeyChain_Type()
)
hpicfDhcpClientKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpClientKeyChain.setStatus("current")
_HpicfDhcpClientStatisticsTable_Object = MibTable
hpicfDhcpClientStatisticsTable = _HpicfDhcpClientStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfDhcpClientStatisticsTable.setStatus("current")
_HpicfDhcpClientStatisticsEntry_Object = MibTableRow
hpicfDhcpClientStatisticsEntry = _HpicfDhcpClientStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1)
)
hpicfDhcpClientStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-DHCPCLIENT-MIB", "hpicfIPVersion"),
)
if mibBuilder.loadTexts:
    hpicfDhcpClientStatisticsEntry.setStatus("current")
_HpicfIPVersion_Type = InetVersion
_HpicfIPVersion_Object = MibTableColumn
hpicfIPVersion = _HpicfIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1, 1),
    _HpicfIPVersion_Type()
)
hpicfIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIPVersion.setStatus("current")
_HpicfDhcpClientPktTx_Type = Counter32
_HpicfDhcpClientPktTx_Object = MibTableColumn
hpicfDhcpClientPktTx = _HpicfDhcpClientPktTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1, 2),
    _HpicfDhcpClientPktTx_Type()
)
hpicfDhcpClientPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpClientPktTx.setStatus("current")
_HpicfDhcpClientPktRx_Type = Counter32
_HpicfDhcpClientPktRx_Object = MibTableColumn
hpicfDhcpClientPktRx = _HpicfDhcpClientPktRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1, 3),
    _HpicfDhcpClientPktRx_Type()
)
hpicfDhcpClientPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpClientPktRx.setStatus("current")
_HpicfDhcpClientPktAuthFailed_Type = Counter32
_HpicfDhcpClientPktAuthFailed_Object = MibTableColumn
hpicfDhcpClientPktAuthFailed = _HpicfDhcpClientPktAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1, 4),
    _HpicfDhcpClientPktAuthFailed_Type()
)
hpicfDhcpClientPktAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpClientPktAuthFailed.setStatus("current")


class _HpicfDhcpv6ClientDuid_Type(OctetString):
    """Custom type hpicfDhcpv6ClientDuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 128),
    )


_HpicfDhcpv6ClientDuid_Type.__name__ = "OctetString"
_HpicfDhcpv6ClientDuid_Object = MibScalar
hpicfDhcpv6ClientDuid = _HpicfDhcpv6ClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 6),
    _HpicfDhcpv6ClientDuid_Type()
)
hpicfDhcpv6ClientDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv6ClientDuid.setStatus("current")


class _HpicfDhcpClientTR069AcsUrlOptionStatus_Type(Integer32):
    """Custom type hpicfDhcpClientTR069AcsUrlOptionStatus based on Integer32"""
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


_HpicfDhcpClientTR069AcsUrlOptionStatus_Type.__name__ = "Integer32"
_HpicfDhcpClientTR069AcsUrlOptionStatus_Object = MibScalar
hpicfDhcpClientTR069AcsUrlOptionStatus = _HpicfDhcpClientTR069AcsUrlOptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 7),
    _HpicfDhcpClientTR069AcsUrlOptionStatus_Type()
)
hpicfDhcpClientTR069AcsUrlOptionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpClientTR069AcsUrlOptionStatus.setStatus("current")
_HpicfDhcpClientOptionsConf_ObjectIdentity = ObjectIdentity
hpicfDhcpClientOptionsConf = _HpicfDhcpClientOptionsConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2)
)
_HpicfDhcpClientGroups_ObjectIdentity = ObjectIdentity
hpicfDhcpClientGroups = _HpicfDhcpClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1)
)
_HpicfDhcpClientCompliances_ObjectIdentity = ObjectIdentity
hpicfDhcpClientCompliances = _HpicfDhcpClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2)
)

# Managed Objects groups

hpicfDhcpClientOptionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 1)
)
hpicfDhcpClientOptionsGroup.setObjects(
      *(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientVendorSpecOptionStatus"),
        ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientHostNameOption"))
)
if mibBuilder.loadTexts:
    hpicfDhcpClientOptionsGroup.setStatus("current")

hpicfDhcpClientVendorSpecOptionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 2)
)
hpicfDhcpClientVendorSpecOptionsGroup.setObjects(
    ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientImageFileUpdate")
)
if mibBuilder.loadTexts:
    hpicfDhcpClientVendorSpecOptionsGroup.setStatus("current")

hpicfDhcpClientAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 3)
)
hpicfDhcpClientAuthGroup.setObjects(
      *(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientAuthType"),
        ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientKeyChain"),
        ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientPktTx"),
        ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientPktRx"),
        ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientPktAuthFailed"))
)
if mibBuilder.loadTexts:
    hpicfDhcpClientAuthGroup.setStatus("current")

hpicfDhcpv6ClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 4)
)
hpicfDhcpv6ClientGroup.setObjects(
    ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpv6ClientDuid")
)
if mibBuilder.loadTexts:
    hpicfDhcpv6ClientGroup.setStatus("current")

hpicfDhcpClientTR069OptionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 5)
)
hpicfDhcpClientTR069OptionsGroup.setObjects(
    ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientTR069AcsUrlOptionStatus")
)
if mibBuilder.loadTexts:
    hpicfDhcpClientTR069OptionsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDhcpClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfDhcpClientCompliance.setStatus(
        "current"
    )

hpicfDhcpClientVendorSpecOptionsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfDhcpClientVendorSpecOptionsCompliance.setStatus(
        "current"
    )

hpicfDhcpClientAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfDhcpClientAuthCompliance.setStatus(
        "current"
    )

hpicfDhcpv6ClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfDhcpv6ClientCompliance.setStatus(
        "current"
    )

hpicfDhcpClientTR069OptionsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfDhcpClientTR069OptionsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DHCPCLIENT-MIB",
    **{"hpicfDhcpClient": hpicfDhcpClient,
       "hpicfDhcpClientOptions": hpicfDhcpClientOptions,
       "hpicfDhcpClientVendorSpecOptionStatus": hpicfDhcpClientVendorSpecOptionStatus,
       "hpicfDhcpClientHostNameOption": hpicfDhcpClientHostNameOption,
       "hpicfDhcpClientImageFileUpdate": hpicfDhcpClientImageFileUpdate,
       "hpicfDhcpClientintfTable": hpicfDhcpClientintfTable,
       "hpicfDhcpClientintfEntry": hpicfDhcpClientintfEntry,
       "hpicfDhcpClientAuthType": hpicfDhcpClientAuthType,
       "hpicfDhcpClientKeyChain": hpicfDhcpClientKeyChain,
       "hpicfDhcpClientStatisticsTable": hpicfDhcpClientStatisticsTable,
       "hpicfDhcpClientStatisticsEntry": hpicfDhcpClientStatisticsEntry,
       "hpicfIPVersion": hpicfIPVersion,
       "hpicfDhcpClientPktTx": hpicfDhcpClientPktTx,
       "hpicfDhcpClientPktRx": hpicfDhcpClientPktRx,
       "hpicfDhcpClientPktAuthFailed": hpicfDhcpClientPktAuthFailed,
       "hpicfDhcpv6ClientDuid": hpicfDhcpv6ClientDuid,
       "hpicfDhcpClientTR069AcsUrlOptionStatus": hpicfDhcpClientTR069AcsUrlOptionStatus,
       "hpicfDhcpClientOptionsConf": hpicfDhcpClientOptionsConf,
       "hpicfDhcpClientGroups": hpicfDhcpClientGroups,
       "hpicfDhcpClientOptionsGroup": hpicfDhcpClientOptionsGroup,
       "hpicfDhcpClientVendorSpecOptionsGroup": hpicfDhcpClientVendorSpecOptionsGroup,
       "hpicfDhcpClientAuthGroup": hpicfDhcpClientAuthGroup,
       "hpicfDhcpv6ClientGroup": hpicfDhcpv6ClientGroup,
       "hpicfDhcpClientTR069OptionsGroup": hpicfDhcpClientTR069OptionsGroup,
       "hpicfDhcpClientCompliances": hpicfDhcpClientCompliances,
       "hpicfDhcpClientCompliance": hpicfDhcpClientCompliance,
       "hpicfDhcpClientVendorSpecOptionsCompliance": hpicfDhcpClientVendorSpecOptionsCompliance,
       "hpicfDhcpClientAuthCompliance": hpicfDhcpClientAuthCompliance,
       "hpicfDhcpv6ClientCompliance": hpicfDhcpv6ClientCompliance,
       "hpicfDhcpClientTR069OptionsCompliance": hpicfDhcpClientTR069OptionsCompliance}
)
