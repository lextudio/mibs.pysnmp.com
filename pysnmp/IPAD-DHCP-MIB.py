# SNMP MIB module (IPAD-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPAD-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:41 2024
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

(ipad,) = mibBuilder.importSymbols(
    "IPADv2-MIB",
    "ipad")

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


# MODULE-IDENTITY

ipadDhcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpadDhcpParms_ObjectIdentity = ObjectIdentity
ipadDhcpParms = _IpadDhcpParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1)
)


class _IpadDhcpEnable_Type(Integer32):
    """Custom type ipadDhcpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadDhcpEnable_Type.__name__ = "Integer32"
_IpadDhcpEnable_Object = MibScalar
ipadDhcpEnable = _IpadDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 1),
    _IpadDhcpEnable_Type()
)
ipadDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpEnable.setStatus("current")
_IpadDhcpNumberPorts_Type = Integer32
_IpadDhcpNumberPorts_Object = MibScalar
ipadDhcpNumberPorts = _IpadDhcpNumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 2),
    _IpadDhcpNumberPorts_Type()
)
ipadDhcpNumberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpNumberPorts.setStatus("current")
_IpadDhcpTTL_Type = Integer32
_IpadDhcpTTL_Object = MibScalar
ipadDhcpTTL = _IpadDhcpTTL_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 3),
    _IpadDhcpTTL_Type()
)
ipadDhcpTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpTTL.setStatus("current")
_IpadDhcpServiceType_Type = Integer32
_IpadDhcpServiceType_Object = MibScalar
ipadDhcpServiceType = _IpadDhcpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 4),
    _IpadDhcpServiceType_Type()
)
ipadDhcpServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServiceType.setStatus("current")
_IpadDhcpLeaseTime_Type = Integer32
_IpadDhcpLeaseTime_Object = MibScalar
ipadDhcpLeaseTime = _IpadDhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 5),
    _IpadDhcpLeaseTime_Type()
)
ipadDhcpLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpLeaseTime.setStatus("current")
_IpadDhcpServerDatabasePrimaryDnsIpAddress_Type = IpAddress
_IpadDhcpServerDatabasePrimaryDnsIpAddress_Object = MibScalar
ipadDhcpServerDatabasePrimaryDnsIpAddress = _IpadDhcpServerDatabasePrimaryDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 6),
    _IpadDhcpServerDatabasePrimaryDnsIpAddress_Type()
)
ipadDhcpServerDatabasePrimaryDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServerDatabasePrimaryDnsIpAddress.setStatus("current")
_IpadDhcpServerDatabaseSecondaryDnsIpAddress_Type = IpAddress
_IpadDhcpServerDatabaseSecondaryDnsIpAddress_Object = MibScalar
ipadDhcpServerDatabaseSecondaryDnsIpAddress = _IpadDhcpServerDatabaseSecondaryDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 7),
    _IpadDhcpServerDatabaseSecondaryDnsIpAddress_Type()
)
ipadDhcpServerDatabaseSecondaryDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServerDatabaseSecondaryDnsIpAddress.setStatus("current")
_IpadDhcpServerDatabaseDomainName_Type = DisplayString
_IpadDhcpServerDatabaseDomainName_Object = MibScalar
ipadDhcpServerDatabaseDomainName = _IpadDhcpServerDatabaseDomainName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 8),
    _IpadDhcpServerDatabaseDomainName_Type()
)
ipadDhcpServerDatabaseDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServerDatabaseDomainName.setStatus("current")
_IpadDhcpServerDatabaseRouterIpAddress_Type = IpAddress
_IpadDhcpServerDatabaseRouterIpAddress_Object = MibScalar
ipadDhcpServerDatabaseRouterIpAddress = _IpadDhcpServerDatabaseRouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 9),
    _IpadDhcpServerDatabaseRouterIpAddress_Type()
)
ipadDhcpServerDatabaseRouterIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServerDatabaseRouterIpAddress.setStatus("current")
_IpadDhcpServerHostNameTable_Object = MibTable
ipadDhcpServerHostNameTable = _IpadDhcpServerHostNameTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 10)
)
if mibBuilder.loadTexts:
    ipadDhcpServerHostNameTable.setStatus("current")
_IpadDhcpServerHostNameTableEntry_Object = MibTableRow
ipadDhcpServerHostNameTableEntry = _IpadDhcpServerHostNameTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 10, 1)
)
ipadDhcpServerHostNameTableEntry.setIndexNames(
    (0, "IPAD-DHCP-MIB", "ipadDhcpServerHostIndex"),
)
if mibBuilder.loadTexts:
    ipadDhcpServerHostNameTableEntry.setStatus("current")
_IpadDhcpServerHostIndex_Type = Integer32
_IpadDhcpServerHostIndex_Object = MibTableColumn
ipadDhcpServerHostIndex = _IpadDhcpServerHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 10, 1, 1),
    _IpadDhcpServerHostIndex_Type()
)
ipadDhcpServerHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDhcpServerHostIndex.setStatus("current")
_IpadDhcpServerHostName_Type = DisplayString
_IpadDhcpServerHostName_Object = MibTableColumn
ipadDhcpServerHostName = _IpadDhcpServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 10, 1, 2),
    _IpadDhcpServerHostName_Type()
)
ipadDhcpServerHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServerHostName.setStatus("current")


class _IpadDhcpServerHostAdd_Type(Integer32):
    """Custom type ipadDhcpServerHostAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadDhcpServerHostAdd_Type.__name__ = "Integer32"
_IpadDhcpServerHostAdd_Object = MibScalar
ipadDhcpServerHostAdd = _IpadDhcpServerHostAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 11),
    _IpadDhcpServerHostAdd_Type()
)
ipadDhcpServerHostAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServerHostAdd.setStatus("current")
_IpadDhcpServerHostDelete_Type = Integer32
_IpadDhcpServerHostDelete_Object = MibScalar
ipadDhcpServerHostDelete = _IpadDhcpServerHostDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 12),
    _IpadDhcpServerHostDelete_Type()
)
ipadDhcpServerHostDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServerHostDelete.setStatus("current")
_IpadDhcpStaticEntryTable_Object = MibTable
ipadDhcpStaticEntryTable = _IpadDhcpStaticEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 13)
)
if mibBuilder.loadTexts:
    ipadDhcpStaticEntryTable.setStatus("current")
_IpadDhcpStaticEntryTableEntry_Object = MibTableRow
ipadDhcpStaticEntryTableEntry = _IpadDhcpStaticEntryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 13, 1)
)
ipadDhcpStaticEntryTableEntry.setIndexNames(
    (0, "IPAD-DHCP-MIB", "ipadDhcpStaticEntryIndex"),
)
if mibBuilder.loadTexts:
    ipadDhcpStaticEntryTableEntry.setStatus("current")
_IpadDhcpStaticEntryIndex_Type = Integer32
_IpadDhcpStaticEntryIndex_Object = MibTableColumn
ipadDhcpStaticEntryIndex = _IpadDhcpStaticEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 13, 1, 1),
    _IpadDhcpStaticEntryIndex_Type()
)
ipadDhcpStaticEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDhcpStaticEntryIndex.setStatus("current")
_IpadDhcpStaticEntryMacAddress_Type = OctetString
_IpadDhcpStaticEntryMacAddress_Object = MibTableColumn
ipadDhcpStaticEntryMacAddress = _IpadDhcpStaticEntryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 13, 1, 2),
    _IpadDhcpStaticEntryMacAddress_Type()
)
ipadDhcpStaticEntryMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpStaticEntryMacAddress.setStatus("current")
_IpadDhcpStaticEntryIpAddress_Type = IpAddress
_IpadDhcpStaticEntryIpAddress_Object = MibTableColumn
ipadDhcpStaticEntryIpAddress = _IpadDhcpStaticEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 13, 1, 3),
    _IpadDhcpStaticEntryIpAddress_Type()
)
ipadDhcpStaticEntryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpStaticEntryIpAddress.setStatus("current")
_IpadDhcpStaticEntryMaskAddress_Type = IpAddress
_IpadDhcpStaticEntryMaskAddress_Object = MibTableColumn
ipadDhcpStaticEntryMaskAddress = _IpadDhcpStaticEntryMaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 13, 1, 4),
    _IpadDhcpStaticEntryMaskAddress_Type()
)
ipadDhcpStaticEntryMaskAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpStaticEntryMaskAddress.setStatus("current")
_IpadDhcpStaticEntryHostName_Type = DisplayString
_IpadDhcpStaticEntryHostName_Object = MibTableColumn
ipadDhcpStaticEntryHostName = _IpadDhcpStaticEntryHostName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 13, 1, 5),
    _IpadDhcpStaticEntryHostName_Type()
)
ipadDhcpStaticEntryHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpStaticEntryHostName.setStatus("current")


class _IpadDhcpStaticEntryAdd_Type(Integer32):
    """Custom type ipadDhcpStaticEntryAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadDhcpStaticEntryAdd_Type.__name__ = "Integer32"
_IpadDhcpStaticEntryAdd_Object = MibScalar
ipadDhcpStaticEntryAdd = _IpadDhcpStaticEntryAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 14),
    _IpadDhcpStaticEntryAdd_Type()
)
ipadDhcpStaticEntryAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpStaticEntryAdd.setStatus("current")
_IpadDhcpStaticEntryDelete_Type = Integer32
_IpadDhcpStaticEntryDelete_Object = MibScalar
ipadDhcpStaticEntryDelete = _IpadDhcpStaticEntryDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 15),
    _IpadDhcpStaticEntryDelete_Type()
)
ipadDhcpStaticEntryDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpStaticEntryDelete.setStatus("current")
_IpadDhcpAddressListTable_Object = MibTable
ipadDhcpAddressListTable = _IpadDhcpAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 16)
)
if mibBuilder.loadTexts:
    ipadDhcpAddressListTable.setStatus("current")
_IpadDhcpAddressListTableEntry_Object = MibTableRow
ipadDhcpAddressListTableEntry = _IpadDhcpAddressListTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 16, 1)
)
ipadDhcpAddressListTableEntry.setIndexNames(
    (0, "IPAD-DHCP-MIB", "ipadDhcpAddressListIndex"),
)
if mibBuilder.loadTexts:
    ipadDhcpAddressListTableEntry.setStatus("current")
_IpadDhcpAddressListIndex_Type = Integer32
_IpadDhcpAddressListIndex_Object = MibTableColumn
ipadDhcpAddressListIndex = _IpadDhcpAddressListIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 16, 1, 1),
    _IpadDhcpAddressListIndex_Type()
)
ipadDhcpAddressListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDhcpAddressListIndex.setStatus("current")
_IpadDhcpAddressListIpStart_Type = IpAddress
_IpadDhcpAddressListIpStart_Object = MibTableColumn
ipadDhcpAddressListIpStart = _IpadDhcpAddressListIpStart_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 16, 1, 2),
    _IpadDhcpAddressListIpStart_Type()
)
ipadDhcpAddressListIpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpAddressListIpStart.setStatus("current")
_IpadDhcpAddressListIpEnd_Type = IpAddress
_IpadDhcpAddressListIpEnd_Object = MibTableColumn
ipadDhcpAddressListIpEnd = _IpadDhcpAddressListIpEnd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 16, 1, 3),
    _IpadDhcpAddressListIpEnd_Type()
)
ipadDhcpAddressListIpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpAddressListIpEnd.setStatus("current")
_IpadDhcpAddressListSubnetMask_Type = IpAddress
_IpadDhcpAddressListSubnetMask_Object = MibTableColumn
ipadDhcpAddressListSubnetMask = _IpadDhcpAddressListSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 16, 1, 4),
    _IpadDhcpAddressListSubnetMask_Type()
)
ipadDhcpAddressListSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpAddressListSubnetMask.setStatus("current")
_IpadDhcpAddressListIpExcludeStart_Type = IpAddress
_IpadDhcpAddressListIpExcludeStart_Object = MibTableColumn
ipadDhcpAddressListIpExcludeStart = _IpadDhcpAddressListIpExcludeStart_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 16, 1, 5),
    _IpadDhcpAddressListIpExcludeStart_Type()
)
ipadDhcpAddressListIpExcludeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpAddressListIpExcludeStart.setStatus("current")
_IpadDhcpAddressListIpExcludeEnd_Type = IpAddress
_IpadDhcpAddressListIpExcludeEnd_Object = MibTableColumn
ipadDhcpAddressListIpExcludeEnd = _IpadDhcpAddressListIpExcludeEnd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 16, 1, 6),
    _IpadDhcpAddressListIpExcludeEnd_Type()
)
ipadDhcpAddressListIpExcludeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpAddressListIpExcludeEnd.setStatus("current")


class _IpadDhcpAddressListAdd_Type(Integer32):
    """Custom type ipadDhcpAddressListAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadDhcpAddressListAdd_Type.__name__ = "Integer32"
_IpadDhcpAddressListAdd_Object = MibScalar
ipadDhcpAddressListAdd = _IpadDhcpAddressListAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 17),
    _IpadDhcpAddressListAdd_Type()
)
ipadDhcpAddressListAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpAddressListAdd.setStatus("current")
_IpadDhcpAddressListDelete_Type = Integer32
_IpadDhcpAddressListDelete_Object = MibScalar
ipadDhcpAddressListDelete = _IpadDhcpAddressListDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 18),
    _IpadDhcpAddressListDelete_Type()
)
ipadDhcpAddressListDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpAddressListDelete.setStatus("current")
_IpadDhcpAddressStatusTable_Object = MibTable
ipadDhcpAddressStatusTable = _IpadDhcpAddressStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 19)
)
if mibBuilder.loadTexts:
    ipadDhcpAddressStatusTable.setStatus("current")
_IpadDhcpAddressStatusTableEntry_Object = MibTableRow
ipadDhcpAddressStatusTableEntry = _IpadDhcpAddressStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 19, 1)
)
ipadDhcpAddressStatusTableEntry.setIndexNames(
    (0, "IPAD-DHCP-MIB", "ipadDhcpAddressStatusIndex"),
)
if mibBuilder.loadTexts:
    ipadDhcpAddressStatusTableEntry.setStatus("current")
_IpadDhcpAddressStatusIndex_Type = Integer32
_IpadDhcpAddressStatusIndex_Object = MibTableColumn
ipadDhcpAddressStatusIndex = _IpadDhcpAddressStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 19, 1, 1),
    _IpadDhcpAddressStatusIndex_Type()
)
ipadDhcpAddressStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDhcpAddressStatusIndex.setStatus("current")
_IpadDhcpAddressStatusMacAddress_Type = OctetString
_IpadDhcpAddressStatusMacAddress_Object = MibTableColumn
ipadDhcpAddressStatusMacAddress = _IpadDhcpAddressStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 19, 1, 2),
    _IpadDhcpAddressStatusMacAddress_Type()
)
ipadDhcpAddressStatusMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDhcpAddressStatusMacAddress.setStatus("current")
_IpadDhcpAddressStatusIpAddress_Type = IpAddress
_IpadDhcpAddressStatusIpAddress_Object = MibTableColumn
ipadDhcpAddressStatusIpAddress = _IpadDhcpAddressStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 19, 1, 3),
    _IpadDhcpAddressStatusIpAddress_Type()
)
ipadDhcpAddressStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDhcpAddressStatusIpAddress.setStatus("current")


class _IpadDhcpAddressStatusStatus_Type(Integer32):
    """Custom type ipadDhcpAddressStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 3),
          ("available", 2),
          ("other", 1))
    )


_IpadDhcpAddressStatusStatus_Type.__name__ = "Integer32"
_IpadDhcpAddressStatusStatus_Object = MibTableColumn
ipadDhcpAddressStatusStatus = _IpadDhcpAddressStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 19, 1, 4),
    _IpadDhcpAddressStatusStatus_Type()
)
ipadDhcpAddressStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDhcpAddressStatusStatus.setStatus("current")
_IpadDhcpServerDatabaseWinsPrimary_Type = IpAddress
_IpadDhcpServerDatabaseWinsPrimary_Object = MibScalar
ipadDhcpServerDatabaseWinsPrimary = _IpadDhcpServerDatabaseWinsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 20),
    _IpadDhcpServerDatabaseWinsPrimary_Type()
)
ipadDhcpServerDatabaseWinsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServerDatabaseWinsPrimary.setStatus("current")
_IpadDhcpServerDatabaseWinsSecondary_Type = IpAddress
_IpadDhcpServerDatabaseWinsSecondary_Object = MibScalar
ipadDhcpServerDatabaseWinsSecondary = _IpadDhcpServerDatabaseWinsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 1, 21),
    _IpadDhcpServerDatabaseWinsSecondary_Type()
)
ipadDhcpServerDatabaseWinsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpServerDatabaseWinsSecondary.setStatus("current")
_IpadDhcpPortParms_ObjectIdentity = ObjectIdentity
ipadDhcpPortParms = _IpadDhcpPortParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 2)
)
_IpadDhcpPortTable_Object = MibTable
ipadDhcpPortTable = _IpadDhcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 2, 1)
)
if mibBuilder.loadTexts:
    ipadDhcpPortTable.setStatus("current")
_IpadDhcpPortTableEntry_Object = MibTableRow
ipadDhcpPortTableEntry = _IpadDhcpPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 2, 1, 1)
)
ipadDhcpPortTableEntry.setIndexNames(
    (0, "IPAD-DHCP-MIB", "ipadDhcpPortIndex"),
)
if mibBuilder.loadTexts:
    ipadDhcpPortTableEntry.setStatus("current")
_IpadDhcpPortIndex_Type = Integer32
_IpadDhcpPortIndex_Object = MibTableColumn
ipadDhcpPortIndex = _IpadDhcpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 2, 1, 1, 1),
    _IpadDhcpPortIndex_Type()
)
ipadDhcpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDhcpPortIndex.setStatus("current")
_IpadDhcpPortIpAddress_Type = IpAddress
_IpadDhcpPortIpAddress_Object = MibTableColumn
ipadDhcpPortIpAddress = _IpadDhcpPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 2, 1, 1, 2),
    _IpadDhcpPortIpAddress_Type()
)
ipadDhcpPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpPortIpAddress.setStatus("current")


class _IpadDhcpPortEnable_Type(Integer32):
    """Custom type ipadDhcpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadDhcpPortEnable_Type.__name__ = "Integer32"
_IpadDhcpPortEnable_Object = MibTableColumn
ipadDhcpPortEnable = _IpadDhcpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 2, 1, 1, 3),
    _IpadDhcpPortEnable_Type()
)
ipadDhcpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpPortEnable.setStatus("current")
_IpadDhcpPortAdd_Type = Integer32
_IpadDhcpPortAdd_Object = MibScalar
ipadDhcpPortAdd = _IpadDhcpPortAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 2, 2),
    _IpadDhcpPortAdd_Type()
)
ipadDhcpPortAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpPortAdd.setStatus("current")
_IpadDhcpPortDelete_Type = Integer32
_IpadDhcpPortDelete_Object = MibScalar
ipadDhcpPortDelete = _IpadDhcpPortDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27, 2, 3),
    _IpadDhcpPortDelete_Type()
)
ipadDhcpPortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDhcpPortDelete.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPAD-DHCP-MIB",
    **{"ipadDhcp": ipadDhcp,
       "ipadDhcpParms": ipadDhcpParms,
       "ipadDhcpEnable": ipadDhcpEnable,
       "ipadDhcpNumberPorts": ipadDhcpNumberPorts,
       "ipadDhcpTTL": ipadDhcpTTL,
       "ipadDhcpServiceType": ipadDhcpServiceType,
       "ipadDhcpLeaseTime": ipadDhcpLeaseTime,
       "ipadDhcpServerDatabasePrimaryDnsIpAddress": ipadDhcpServerDatabasePrimaryDnsIpAddress,
       "ipadDhcpServerDatabaseSecondaryDnsIpAddress": ipadDhcpServerDatabaseSecondaryDnsIpAddress,
       "ipadDhcpServerDatabaseDomainName": ipadDhcpServerDatabaseDomainName,
       "ipadDhcpServerDatabaseRouterIpAddress": ipadDhcpServerDatabaseRouterIpAddress,
       "ipadDhcpServerHostNameTable": ipadDhcpServerHostNameTable,
       "ipadDhcpServerHostNameTableEntry": ipadDhcpServerHostNameTableEntry,
       "ipadDhcpServerHostIndex": ipadDhcpServerHostIndex,
       "ipadDhcpServerHostName": ipadDhcpServerHostName,
       "ipadDhcpServerHostAdd": ipadDhcpServerHostAdd,
       "ipadDhcpServerHostDelete": ipadDhcpServerHostDelete,
       "ipadDhcpStaticEntryTable": ipadDhcpStaticEntryTable,
       "ipadDhcpStaticEntryTableEntry": ipadDhcpStaticEntryTableEntry,
       "ipadDhcpStaticEntryIndex": ipadDhcpStaticEntryIndex,
       "ipadDhcpStaticEntryMacAddress": ipadDhcpStaticEntryMacAddress,
       "ipadDhcpStaticEntryIpAddress": ipadDhcpStaticEntryIpAddress,
       "ipadDhcpStaticEntryMaskAddress": ipadDhcpStaticEntryMaskAddress,
       "ipadDhcpStaticEntryHostName": ipadDhcpStaticEntryHostName,
       "ipadDhcpStaticEntryAdd": ipadDhcpStaticEntryAdd,
       "ipadDhcpStaticEntryDelete": ipadDhcpStaticEntryDelete,
       "ipadDhcpAddressListTable": ipadDhcpAddressListTable,
       "ipadDhcpAddressListTableEntry": ipadDhcpAddressListTableEntry,
       "ipadDhcpAddressListIndex": ipadDhcpAddressListIndex,
       "ipadDhcpAddressListIpStart": ipadDhcpAddressListIpStart,
       "ipadDhcpAddressListIpEnd": ipadDhcpAddressListIpEnd,
       "ipadDhcpAddressListSubnetMask": ipadDhcpAddressListSubnetMask,
       "ipadDhcpAddressListIpExcludeStart": ipadDhcpAddressListIpExcludeStart,
       "ipadDhcpAddressListIpExcludeEnd": ipadDhcpAddressListIpExcludeEnd,
       "ipadDhcpAddressListAdd": ipadDhcpAddressListAdd,
       "ipadDhcpAddressListDelete": ipadDhcpAddressListDelete,
       "ipadDhcpAddressStatusTable": ipadDhcpAddressStatusTable,
       "ipadDhcpAddressStatusTableEntry": ipadDhcpAddressStatusTableEntry,
       "ipadDhcpAddressStatusIndex": ipadDhcpAddressStatusIndex,
       "ipadDhcpAddressStatusMacAddress": ipadDhcpAddressStatusMacAddress,
       "ipadDhcpAddressStatusIpAddress": ipadDhcpAddressStatusIpAddress,
       "ipadDhcpAddressStatusStatus": ipadDhcpAddressStatusStatus,
       "ipadDhcpServerDatabaseWinsPrimary": ipadDhcpServerDatabaseWinsPrimary,
       "ipadDhcpServerDatabaseWinsSecondary": ipadDhcpServerDatabaseWinsSecondary,
       "ipadDhcpPortParms": ipadDhcpPortParms,
       "ipadDhcpPortTable": ipadDhcpPortTable,
       "ipadDhcpPortTableEntry": ipadDhcpPortTableEntry,
       "ipadDhcpPortIndex": ipadDhcpPortIndex,
       "ipadDhcpPortIpAddress": ipadDhcpPortIpAddress,
       "ipadDhcpPortEnable": ipadDhcpPortEnable,
       "ipadDhcpPortAdd": ipadDhcpPortAdd,
       "ipadDhcpPortDelete": ipadDhcpPortDelete}
)
