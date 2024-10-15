# SNMP MIB module (CISCO-LWAPP-MDNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-MDNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:40 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappMdnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994)
)
ciscoLwappMdnsMIB.setRevisions(
        ("2012-07-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappMdnsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMdnsMIBNotifs = _CiscoLwappMdnsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 0)
)
_CiscoLwappMdnsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMdnsMIBObjects = _CiscoLwappMdnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1)
)
_ClMdnsConfigObjects_ObjectIdentity = ObjectIdentity
clMdnsConfigObjects = _ClMdnsConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1)
)
_ClMdnsGlobalConfig_ObjectIdentity = ObjectIdentity
clMdnsGlobalConfig = _ClMdnsGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 1)
)


class _ClMdnsSnoopingEnabled_Type(TruthValue):
    """Custom type clMdnsSnoopingEnabled based on TruthValue"""


_ClMdnsSnoopingEnabled_Object = MibScalar
clMdnsSnoopingEnabled = _ClMdnsSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 1, 1),
    _ClMdnsSnoopingEnabled_Type()
)
clMdnsSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMdnsSnoopingEnabled.setStatus("current")
_ClMdnsQueryInterval_Type = Unsigned32
_ClMdnsQueryInterval_Object = MibScalar
clMdnsQueryInterval = _ClMdnsQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 1, 2),
    _ClMdnsQueryInterval_Type()
)
clMdnsQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMdnsQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    clMdnsQueryInterval.setUnits("minutes")
_ClMdnsMasterServiceTable_Object = MibTable
clMdnsMasterServiceTable = _ClMdnsMasterServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clMdnsMasterServiceTable.setStatus("current")
_ClMdnsMasterServiceEntry_Object = MibTableRow
clMdnsMasterServiceEntry = _ClMdnsMasterServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 2, 1)
)
clMdnsMasterServiceEntry.setIndexNames(
    (0, "CISCO-LWAPP-MDNS-MIB", "clMdnsServiceName"),
)
if mibBuilder.loadTexts:
    clMdnsMasterServiceEntry.setStatus("current")
_ClMdnsServiceName_Type = SnmpAdminString
_ClMdnsServiceName_Object = MibTableColumn
clMdnsServiceName = _ClMdnsServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 2, 1, 1),
    _ClMdnsServiceName_Type()
)
clMdnsServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clMdnsServiceName.setStatus("current")
_ClMdnsServiceString_Type = SnmpAdminString
_ClMdnsServiceString_Object = MibTableColumn
clMdnsServiceString = _ClMdnsServiceString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 2, 1, 2),
    _ClMdnsServiceString_Type()
)
clMdnsServiceString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMdnsServiceString.setStatus("current")


class _ClMdnsServiceQueryStatus_Type(TruthValue):
    """Custom type clMdnsServiceQueryStatus based on TruthValue"""


_ClMdnsServiceQueryStatus_Object = MibTableColumn
clMdnsServiceQueryStatus = _ClMdnsServiceQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 2, 1, 3),
    _ClMdnsServiceQueryStatus_Type()
)
clMdnsServiceQueryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMdnsServiceQueryStatus.setStatus("current")
_ClMdnsServiceRowStatus_Type = RowStatus
_ClMdnsServiceRowStatus_Object = MibTableColumn
clMdnsServiceRowStatus = _ClMdnsServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 2, 1, 4),
    _ClMdnsServiceRowStatus_Type()
)
clMdnsServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMdnsServiceRowStatus.setStatus("current")
_ClMdnsProfileTable_Object = MibTable
clMdnsProfileTable = _ClMdnsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 3)
)
if mibBuilder.loadTexts:
    clMdnsProfileTable.setStatus("current")
_ClMdnsProfileEntry_Object = MibTableRow
clMdnsProfileEntry = _ClMdnsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 3, 1)
)
clMdnsProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-MDNS-MIB", "clMdnsProfileName"),
)
if mibBuilder.loadTexts:
    clMdnsProfileEntry.setStatus("current")
_ClMdnsProfileName_Type = SnmpAdminString
_ClMdnsProfileName_Object = MibTableColumn
clMdnsProfileName = _ClMdnsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 3, 1, 1),
    _ClMdnsProfileName_Type()
)
clMdnsProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clMdnsProfileName.setStatus("current")
_ClMdnsProfileRowStatus_Type = RowStatus
_ClMdnsProfileRowStatus_Object = MibTableColumn
clMdnsProfileRowStatus = _ClMdnsProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 3, 1, 2),
    _ClMdnsProfileRowStatus_Type()
)
clMdnsProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMdnsProfileRowStatus.setStatus("current")
_ClMdnsProfileWlanCount_Type = Unsigned32
_ClMdnsProfileWlanCount_Object = MibTableColumn
clMdnsProfileWlanCount = _ClMdnsProfileWlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 3, 1, 3),
    _ClMdnsProfileWlanCount_Type()
)
clMdnsProfileWlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsProfileWlanCount.setStatus("current")
_ClMdnsProfileInterfaceCount_Type = Unsigned32
_ClMdnsProfileInterfaceCount_Object = MibTableColumn
clMdnsProfileInterfaceCount = _ClMdnsProfileInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 3, 1, 4),
    _ClMdnsProfileInterfaceCount_Type()
)
clMdnsProfileInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsProfileInterfaceCount.setStatus("current")
_ClMdnsProfileInterfaceGrpCount_Type = Unsigned32
_ClMdnsProfileInterfaceGrpCount_Object = MibTableColumn
clMdnsProfileInterfaceGrpCount = _ClMdnsProfileInterfaceGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 3, 1, 5),
    _ClMdnsProfileInterfaceGrpCount_Type()
)
clMdnsProfileInterfaceGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsProfileInterfaceGrpCount.setStatus("current")
_ClMdnsProfileServiceTable_Object = MibTable
clMdnsProfileServiceTable = _ClMdnsProfileServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 4)
)
if mibBuilder.loadTexts:
    clMdnsProfileServiceTable.setStatus("current")
_ClMdnsProfileServiceEntry_Object = MibTableRow
clMdnsProfileServiceEntry = _ClMdnsProfileServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 4, 1)
)
clMdnsProfileServiceEntry.setIndexNames(
    (0, "CISCO-LWAPP-MDNS-MIB", "clMdnsProfileName"),
    (0, "CISCO-LWAPP-MDNS-MIB", "clMdnsServiceName"),
)
if mibBuilder.loadTexts:
    clMdnsProfileServiceEntry.setStatus("current")
_ClMdnsProfileServiceRowStatus_Type = RowStatus
_ClMdnsProfileServiceRowStatus_Object = MibTableColumn
clMdnsProfileServiceRowStatus = _ClMdnsProfileServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 4, 1, 1),
    _ClMdnsProfileServiceRowStatus_Type()
)
clMdnsProfileServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMdnsProfileServiceRowStatus.setStatus("current")
_ClMdnsServiceProviderTable_Object = MibTable
clMdnsServiceProviderTable = _ClMdnsServiceProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 5)
)
if mibBuilder.loadTexts:
    clMdnsServiceProviderTable.setStatus("current")
_ClMdnsServiceProviderEntry_Object = MibTableRow
clMdnsServiceProviderEntry = _ClMdnsServiceProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 5, 1)
)
clMdnsServiceProviderEntry.setIndexNames(
    (0, "CISCO-LWAPP-MDNS-MIB", "clMdnsServiceName"),
    (0, "CISCO-LWAPP-MDNS-MIB", "clMdnsServiceProviderIndex"),
)
if mibBuilder.loadTexts:
    clMdnsServiceProviderEntry.setStatus("current")
_ClMdnsServiceProviderIndex_Type = Unsigned32
_ClMdnsServiceProviderIndex_Object = MibTableColumn
clMdnsServiceProviderIndex = _ClMdnsServiceProviderIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 5, 1, 1),
    _ClMdnsServiceProviderIndex_Type()
)
clMdnsServiceProviderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clMdnsServiceProviderIndex.setStatus("current")
_ClMdnsServiceProviderMacAddress_Type = MacAddress
_ClMdnsServiceProviderMacAddress_Object = MibTableColumn
clMdnsServiceProviderMacAddress = _ClMdnsServiceProviderMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 5, 1, 2),
    _ClMdnsServiceProviderMacAddress_Type()
)
clMdnsServiceProviderMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsServiceProviderMacAddress.setStatus("current")
_ClMdnsServiceProviderName_Type = SnmpAdminString
_ClMdnsServiceProviderName_Object = MibTableColumn
clMdnsServiceProviderName = _ClMdnsServiceProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 5, 1, 3),
    _ClMdnsServiceProviderName_Type()
)
clMdnsServiceProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsServiceProviderName.setStatus("current")
_ClMdnsServiceProviderVlan_Type = Unsigned32
_ClMdnsServiceProviderVlan_Object = MibTableColumn
clMdnsServiceProviderVlan = _ClMdnsServiceProviderVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 5, 1, 4),
    _ClMdnsServiceProviderVlan_Type()
)
clMdnsServiceProviderVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsServiceProviderVlan.setStatus("current")


class _ClMdnsServiceProviderType_Type(Integer32):
    """Custom type clMdnsServiceProviderType based on Integer32"""
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
        *(("both", 4),
          ("wired", 2),
          ("wired-guest", 3),
          ("wireless", 1))
    )


_ClMdnsServiceProviderType_Type.__name__ = "Integer32"
_ClMdnsServiceProviderType_Object = MibTableColumn
clMdnsServiceProviderType = _ClMdnsServiceProviderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 5, 1, 5),
    _ClMdnsServiceProviderType_Type()
)
clMdnsServiceProviderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsServiceProviderType.setStatus("current")
_ClMdnsServiceProviderTtl_Type = Unsigned32
_ClMdnsServiceProviderTtl_Object = MibTableColumn
clMdnsServiceProviderTtl = _ClMdnsServiceProviderTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 5, 1, 6),
    _ClMdnsServiceProviderTtl_Type()
)
clMdnsServiceProviderTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsServiceProviderTtl.setStatus("current")
if mibBuilder.loadTexts:
    clMdnsServiceProviderTtl.setUnits("seconds")
_ClMdnsServiceProviderTimeLeft_Type = Unsigned32
_ClMdnsServiceProviderTimeLeft_Object = MibTableColumn
clMdnsServiceProviderTimeLeft = _ClMdnsServiceProviderTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 5, 1, 7),
    _ClMdnsServiceProviderTimeLeft_Type()
)
clMdnsServiceProviderTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsServiceProviderTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    clMdnsServiceProviderTimeLeft.setUnits("seconds")
_ClMdnsDnipTable_Object = MibTable
clMdnsDnipTable = _ClMdnsDnipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6)
)
if mibBuilder.loadTexts:
    clMdnsDnipTable.setStatus("current")
_ClMdnsDnipEntry_Object = MibTableRow
clMdnsDnipEntry = _ClMdnsDnipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6, 1)
)
clMdnsDnipEntry.setIndexNames(
    (0, "CISCO-LWAPP-MDNS-MIB", "clMdnsDomainName"),
)
if mibBuilder.loadTexts:
    clMdnsDnipEntry.setStatus("current")
_ClMdnsDomainName_Type = SnmpAdminString
_ClMdnsDomainName_Object = MibTableColumn
clMdnsDomainName = _ClMdnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6, 1, 1),
    _ClMdnsDomainName_Type()
)
clMdnsDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clMdnsDomainName.setStatus("current")
_ClMdnsDomainMacAddress_Type = MacAddress
_ClMdnsDomainMacAddress_Object = MibTableColumn
clMdnsDomainMacAddress = _ClMdnsDomainMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6, 1, 2),
    _ClMdnsDomainMacAddress_Type()
)
clMdnsDomainMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsDomainMacAddress.setStatus("current")
_ClMdnsDomainIpAddressType_Type = InetAddressType
_ClMdnsDomainIpAddressType_Object = MibTableColumn
clMdnsDomainIpAddressType = _ClMdnsDomainIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6, 1, 3),
    _ClMdnsDomainIpAddressType_Type()
)
clMdnsDomainIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsDomainIpAddressType.setStatus("current")
_ClMdnsDomainIpAddress_Type = InetAddress
_ClMdnsDomainIpAddress_Object = MibTableColumn
clMdnsDomainIpAddress = _ClMdnsDomainIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6, 1, 4),
    _ClMdnsDomainIpAddress_Type()
)
clMdnsDomainIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsDomainIpAddress.setStatus("current")
_ClMdnsDomainVlan_Type = Unsigned32
_ClMdnsDomainVlan_Object = MibTableColumn
clMdnsDomainVlan = _ClMdnsDomainVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6, 1, 5),
    _ClMdnsDomainVlan_Type()
)
clMdnsDomainVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsDomainVlan.setStatus("current")


class _ClMdnsDomainType_Type(Integer32):
    """Custom type clMdnsDomainType based on Integer32"""
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
        *(("both", 4),
          ("wired", 2),
          ("wired-guest", 3),
          ("wireless", 1))
    )


_ClMdnsDomainType_Type.__name__ = "Integer32"
_ClMdnsDomainType_Object = MibTableColumn
clMdnsDomainType = _ClMdnsDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6, 1, 6),
    _ClMdnsDomainType_Type()
)
clMdnsDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsDomainType.setStatus("current")
_ClMdnsDomainEntryTtl_Type = Unsigned32
_ClMdnsDomainEntryTtl_Object = MibTableColumn
clMdnsDomainEntryTtl = _ClMdnsDomainEntryTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6, 1, 7),
    _ClMdnsDomainEntryTtl_Type()
)
clMdnsDomainEntryTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsDomainEntryTtl.setStatus("current")
if mibBuilder.loadTexts:
    clMdnsDomainEntryTtl.setUnits("seconds")
_ClMdnsDomainEntryTimeLeft_Type = Unsigned32
_ClMdnsDomainEntryTimeLeft_Object = MibTableColumn
clMdnsDomainEntryTimeLeft = _ClMdnsDomainEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 6, 1, 8),
    _ClMdnsDomainEntryTimeLeft_Type()
)
clMdnsDomainEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMdnsDomainEntryTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    clMdnsDomainEntryTimeLeft.setUnits("seconds")
_CLMdnsServiceGroupTable_Object = MibTable
cLMdnsServiceGroupTable = _CLMdnsServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cLMdnsServiceGroupTable.setStatus("current")
_CLMdnsServiceGroupEntry_Object = MibTableRow
cLMdnsServiceGroupEntry = _CLMdnsServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 7, 1)
)
cLMdnsServiceGroupEntry.setIndexNames(
    (0, "CISCO-LWAPP-MDNS-MIB", "cLMdnsServiceGroupName"),
)
if mibBuilder.loadTexts:
    cLMdnsServiceGroupEntry.setStatus("current")


class _CLMdnsServiceGroupName_Type(OctetString):
    """Custom type cLMdnsServiceGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CLMdnsServiceGroupName_Type.__name__ = "OctetString"
_CLMdnsServiceGroupName_Object = MibTableColumn
cLMdnsServiceGroupName = _CLMdnsServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 7, 1, 1),
    _CLMdnsServiceGroupName_Type()
)
cLMdnsServiceGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMdnsServiceGroupName.setStatus("current")


class _CLMdnsServiceGroupDescription_Type(OctetString):
    """Custom type cLMdnsServiceGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CLMdnsServiceGroupDescription_Type.__name__ = "OctetString"
_CLMdnsServiceGroupDescription_Object = MibTableColumn
cLMdnsServiceGroupDescription = _CLMdnsServiceGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 7, 1, 2),
    _CLMdnsServiceGroupDescription_Type()
)
cLMdnsServiceGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMdnsServiceGroupDescription.setStatus("current")
_CLMdnsServiceGroupRowStatus_Type = RowStatus
_CLMdnsServiceGroupRowStatus_Object = MibTableColumn
cLMdnsServiceGroupRowStatus = _CLMdnsServiceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 7, 1, 3),
    _CLMdnsServiceGroupRowStatus_Type()
)
cLMdnsServiceGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMdnsServiceGroupRowStatus.setStatus("current")
_CLMdnsServiceGroupDeviceMacTable_Object = MibTable
cLMdnsServiceGroupDeviceMacTable = _CLMdnsServiceGroupDeviceMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cLMdnsServiceGroupDeviceMacTable.setStatus("current")
_CLMdnsServiceGroupDeviceMacEntry_Object = MibTableRow
cLMdnsServiceGroupDeviceMacEntry = _CLMdnsServiceGroupDeviceMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 8, 1)
)
cLMdnsServiceGroupDeviceMacEntry.setIndexNames(
    (0, "CISCO-LWAPP-MDNS-MIB", "cLMdnsServiceGroupName"),
    (0, "CISCO-LWAPP-MDNS-MIB", "cLMdnsServiceGroupDeviceMac"),
)
if mibBuilder.loadTexts:
    cLMdnsServiceGroupDeviceMacEntry.setStatus("current")
_CLMdnsServiceGroupDeviceMac_Type = MacAddress
_CLMdnsServiceGroupDeviceMac_Object = MibTableColumn
cLMdnsServiceGroupDeviceMac = _CLMdnsServiceGroupDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 8, 1, 1),
    _CLMdnsServiceGroupDeviceMac_Type()
)
cLMdnsServiceGroupDeviceMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMdnsServiceGroupDeviceMac.setStatus("current")


class _CLMdnsServiceGroupDeviceName_Type(OctetString):
    """Custom type cLMdnsServiceGroupDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CLMdnsServiceGroupDeviceName_Type.__name__ = "OctetString"
_CLMdnsServiceGroupDeviceName_Object = MibTableColumn
cLMdnsServiceGroupDeviceName = _CLMdnsServiceGroupDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 8, 1, 2),
    _CLMdnsServiceGroupDeviceName_Type()
)
cLMdnsServiceGroupDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMdnsServiceGroupDeviceName.setStatus("current")


class _CLMdnsServiceGroupLocationName_Type(OctetString):
    """Custom type cLMdnsServiceGroupLocationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CLMdnsServiceGroupLocationName_Type.__name__ = "OctetString"
_CLMdnsServiceGroupLocationName_Object = MibTableColumn
cLMdnsServiceGroupLocationName = _CLMdnsServiceGroupLocationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 8, 1, 3),
    _CLMdnsServiceGroupLocationName_Type()
)
cLMdnsServiceGroupLocationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMdnsServiceGroupLocationName.setStatus("current")


class _CLMdnsServiceGroupLocationType_Type(Integer32):
    """Custom type cLMdnsServiceGroupLocationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apGroup", 2),
          ("apLocation", 3),
          ("apName", 1))
    )


_CLMdnsServiceGroupLocationType_Type.__name__ = "Integer32"
_CLMdnsServiceGroupLocationType_Object = MibTableColumn
cLMdnsServiceGroupLocationType = _CLMdnsServiceGroupLocationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 8, 1, 4),
    _CLMdnsServiceGroupLocationType_Type()
)
cLMdnsServiceGroupLocationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMdnsServiceGroupLocationType.setStatus("current")
_CLMdnsServiceGroupDeviceMacRowStatus_Type = RowStatus
_CLMdnsServiceGroupDeviceMacRowStatus_Object = MibTableColumn
cLMdnsServiceGroupDeviceMacRowStatus = _CLMdnsServiceGroupDeviceMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 8, 1, 5),
    _CLMdnsServiceGroupDeviceMacRowStatus_Type()
)
cLMdnsServiceGroupDeviceMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMdnsServiceGroupDeviceMacRowStatus.setStatus("current")
_CLMdnsServiceGroupRuleTable_Object = MibTable
cLMdnsServiceGroupRuleTable = _CLMdnsServiceGroupRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cLMdnsServiceGroupRuleTable.setStatus("current")
_CLMdnsServiceGroupRuleEntry_Object = MibTableRow
cLMdnsServiceGroupRuleEntry = _CLMdnsServiceGroupRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 9, 1)
)
cLMdnsServiceGroupRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-MDNS-MIB", "cLMdnsServiceGroupName"),
    (0, "CISCO-LWAPP-MDNS-MIB", "cLMdnsRuleName"),
)
if mibBuilder.loadTexts:
    cLMdnsServiceGroupRuleEntry.setStatus("current")


class _CLMdnsRuleName_Type(OctetString):
    """Custom type cLMdnsRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 266),
    )


_CLMdnsRuleName_Type.__name__ = "OctetString"
_CLMdnsRuleName_Object = MibTableColumn
cLMdnsRuleName = _CLMdnsRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 9, 1, 1),
    _CLMdnsRuleName_Type()
)
cLMdnsRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMdnsRuleName.setStatus("current")


class _CLMdnsRuleRole_Type(OctetString):
    """Custom type cLMdnsRuleRole based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CLMdnsRuleRole_Type.__name__ = "OctetString"
_CLMdnsRuleRole_Object = MibTableColumn
cLMdnsRuleRole = _CLMdnsRuleRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 9, 1, 2),
    _CLMdnsRuleRole_Type()
)
cLMdnsRuleRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMdnsRuleRole.setStatus("current")


class _CLMdnsRuleUserId_Type(OctetString):
    """Custom type cLMdnsRuleUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CLMdnsRuleUserId_Type.__name__ = "OctetString"
_CLMdnsRuleUserId_Object = MibTableColumn
cLMdnsRuleUserId = _CLMdnsRuleUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 9, 1, 3),
    _CLMdnsRuleUserId_Type()
)
cLMdnsRuleUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMdnsRuleUserId.setStatus("current")
_CLMdnsServiceGroupRuleRowStatus_Type = RowStatus
_CLMdnsServiceGroupRuleRowStatus_Object = MibTableColumn
cLMdnsServiceGroupRuleRowStatus = _CLMdnsServiceGroupRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 1, 1, 9, 1, 4),
    _CLMdnsServiceGroupRuleRowStatus_Type()
)
cLMdnsServiceGroupRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMdnsServiceGroupRuleRowStatus.setStatus("current")
_CiscoLwappMdnsMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMdnsMIBConform = _CiscoLwappMdnsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 2)
)
_CiscoLwappMdnsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMdnsMIBCompliances = _CiscoLwappMdnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 2, 1)
)
_CiscoLwappMdnsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMdnsMIBGroups = _CiscoLwappMdnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 2, 2)
)

# Managed Objects groups

cLMdnsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 2, 2, 1)
)
cLMdnsConfigGroup.setObjects(
      *(("CISCO-LWAPP-MDNS-MIB", "clMdnsSnoopingEnabled"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsQueryInterval"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceName"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceString"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceQueryStatus"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceRowStatus"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsProfileName"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsProfileRowStatus"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsProfileServiceRowStatus"))
)
if mibBuilder.loadTexts:
    cLMdnsConfigGroup.setStatus("current")

cLMdnsMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 2, 2, 2)
)
cLMdnsMonitorGroup.setObjects(
      *(("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceProviderIndex"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceProviderMacAddress"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceProviderName"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceProviderVlan"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceProviderType"),
        ("CISCO-LWAPP-MDNS-MIB", "clMdnsServiceProviderTtl"))
)
if mibBuilder.loadTexts:
    cLMdnsMonitorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappMdnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99994, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappMdnsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MDNS-MIB",
    **{"ciscoLwappMdnsMIB": ciscoLwappMdnsMIB,
       "ciscoLwappMdnsMIBNotifs": ciscoLwappMdnsMIBNotifs,
       "ciscoLwappMdnsMIBObjects": ciscoLwappMdnsMIBObjects,
       "clMdnsConfigObjects": clMdnsConfigObjects,
       "clMdnsGlobalConfig": clMdnsGlobalConfig,
       "clMdnsSnoopingEnabled": clMdnsSnoopingEnabled,
       "clMdnsQueryInterval": clMdnsQueryInterval,
       "clMdnsMasterServiceTable": clMdnsMasterServiceTable,
       "clMdnsMasterServiceEntry": clMdnsMasterServiceEntry,
       "clMdnsServiceName": clMdnsServiceName,
       "clMdnsServiceString": clMdnsServiceString,
       "clMdnsServiceQueryStatus": clMdnsServiceQueryStatus,
       "clMdnsServiceRowStatus": clMdnsServiceRowStatus,
       "clMdnsProfileTable": clMdnsProfileTable,
       "clMdnsProfileEntry": clMdnsProfileEntry,
       "clMdnsProfileName": clMdnsProfileName,
       "clMdnsProfileRowStatus": clMdnsProfileRowStatus,
       "clMdnsProfileWlanCount": clMdnsProfileWlanCount,
       "clMdnsProfileInterfaceCount": clMdnsProfileInterfaceCount,
       "clMdnsProfileInterfaceGrpCount": clMdnsProfileInterfaceGrpCount,
       "clMdnsProfileServiceTable": clMdnsProfileServiceTable,
       "clMdnsProfileServiceEntry": clMdnsProfileServiceEntry,
       "clMdnsProfileServiceRowStatus": clMdnsProfileServiceRowStatus,
       "clMdnsServiceProviderTable": clMdnsServiceProviderTable,
       "clMdnsServiceProviderEntry": clMdnsServiceProviderEntry,
       "clMdnsServiceProviderIndex": clMdnsServiceProviderIndex,
       "clMdnsServiceProviderMacAddress": clMdnsServiceProviderMacAddress,
       "clMdnsServiceProviderName": clMdnsServiceProviderName,
       "clMdnsServiceProviderVlan": clMdnsServiceProviderVlan,
       "clMdnsServiceProviderType": clMdnsServiceProviderType,
       "clMdnsServiceProviderTtl": clMdnsServiceProviderTtl,
       "clMdnsServiceProviderTimeLeft": clMdnsServiceProviderTimeLeft,
       "clMdnsDnipTable": clMdnsDnipTable,
       "clMdnsDnipEntry": clMdnsDnipEntry,
       "clMdnsDomainName": clMdnsDomainName,
       "clMdnsDomainMacAddress": clMdnsDomainMacAddress,
       "clMdnsDomainIpAddressType": clMdnsDomainIpAddressType,
       "clMdnsDomainIpAddress": clMdnsDomainIpAddress,
       "clMdnsDomainVlan": clMdnsDomainVlan,
       "clMdnsDomainType": clMdnsDomainType,
       "clMdnsDomainEntryTtl": clMdnsDomainEntryTtl,
       "clMdnsDomainEntryTimeLeft": clMdnsDomainEntryTimeLeft,
       "cLMdnsServiceGroupTable": cLMdnsServiceGroupTable,
       "cLMdnsServiceGroupEntry": cLMdnsServiceGroupEntry,
       "cLMdnsServiceGroupName": cLMdnsServiceGroupName,
       "cLMdnsServiceGroupDescription": cLMdnsServiceGroupDescription,
       "cLMdnsServiceGroupRowStatus": cLMdnsServiceGroupRowStatus,
       "cLMdnsServiceGroupDeviceMacTable": cLMdnsServiceGroupDeviceMacTable,
       "cLMdnsServiceGroupDeviceMacEntry": cLMdnsServiceGroupDeviceMacEntry,
       "cLMdnsServiceGroupDeviceMac": cLMdnsServiceGroupDeviceMac,
       "cLMdnsServiceGroupDeviceName": cLMdnsServiceGroupDeviceName,
       "cLMdnsServiceGroupLocationName": cLMdnsServiceGroupLocationName,
       "cLMdnsServiceGroupLocationType": cLMdnsServiceGroupLocationType,
       "cLMdnsServiceGroupDeviceMacRowStatus": cLMdnsServiceGroupDeviceMacRowStatus,
       "cLMdnsServiceGroupRuleTable": cLMdnsServiceGroupRuleTable,
       "cLMdnsServiceGroupRuleEntry": cLMdnsServiceGroupRuleEntry,
       "cLMdnsRuleName": cLMdnsRuleName,
       "cLMdnsRuleRole": cLMdnsRuleRole,
       "cLMdnsRuleUserId": cLMdnsRuleUserId,
       "cLMdnsServiceGroupRuleRowStatus": cLMdnsServiceGroupRuleRowStatus,
       "ciscoLwappMdnsMIBConform": ciscoLwappMdnsMIBConform,
       "ciscoLwappMdnsMIBCompliances": ciscoLwappMdnsMIBCompliances,
       "ciscoLwappMdnsMIBCompliance": ciscoLwappMdnsMIBCompliance,
       "ciscoLwappMdnsMIBGroups": ciscoLwappMdnsMIBGroups,
       "cLMdnsConfigGroup": cLMdnsConfigGroup,
       "cLMdnsMonitorGroup": cLMdnsMonitorGroup}
)
