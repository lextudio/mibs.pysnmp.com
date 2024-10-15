# SNMP MIB module (RADLAN-DHCPv6-CLIENT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-DHCPv6-CLIENT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:06 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

(rlDhcpv6Client,) = mibBuilder.importSymbols(
    "RADLAN-DHCPv6",
    "rlDhcpv6Client")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDhcpv6ClientMibVersion_Type = Integer32
_RlDhcpv6ClientMibVersion_Object = MibScalar
rlDhcpv6ClientMibVersion = _RlDhcpv6ClientMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 1),
    _RlDhcpv6ClientMibVersion_Type()
)
rlDhcpv6ClientMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientMibVersion.setStatus("current")
_RlDhcpv6ClientSupported_Type = TruthValue
_RlDhcpv6ClientSupported_Object = MibScalar
rlDhcpv6ClientSupported = _RlDhcpv6ClientSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 2),
    _RlDhcpv6ClientSupported_Type()
)
rlDhcpv6ClientSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientSupported.setStatus("current")
_RlDhcpv6ClientTable_Object = MibTable
rlDhcpv6ClientTable = _RlDhcpv6ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3)
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientTable.setStatus("current")
_RlDhcpv6ClientEntry_Object = MibTableRow
rlDhcpv6ClientEntry = _RlDhcpv6ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1)
)
rlDhcpv6ClientEntry.setIndexNames(
    (0, "RADLAN-DHCPv6-CLIENT", "rlDhcpv6ClientIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientEntry.setStatus("current")
_RlDhcpv6ClientIfIndex_Type = InterfaceIndex
_RlDhcpv6ClientIfIndex_Object = MibTableColumn
rlDhcpv6ClientIfIndex = _RlDhcpv6ClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 1),
    _RlDhcpv6ClientIfIndex_Type()
)
rlDhcpv6ClientIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientIfIndex.setStatus("current")


class _RlDhcpv6ClientPd_Type(Integer32):
    """Custom type rlDhcpv6ClientPd based on Integer32"""
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


_RlDhcpv6ClientPd_Type.__name__ = "Integer32"
_RlDhcpv6ClientPd_Object = MibTableColumn
rlDhcpv6ClientPd = _RlDhcpv6ClientPd_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 2),
    _RlDhcpv6ClientPd_Type()
)
rlDhcpv6ClientPd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientPd.setStatus("current")


class _RlDhcpv6ClientStateless_Type(Integer32):
    """Custom type rlDhcpv6ClientStateless based on Integer32"""
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


_RlDhcpv6ClientStateless_Type.__name__ = "Integer32"
_RlDhcpv6ClientStateless_Object = MibTableColumn
rlDhcpv6ClientStateless = _RlDhcpv6ClientStateless_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 3),
    _RlDhcpv6ClientStateless_Type()
)
rlDhcpv6ClientStateless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpv6ClientStateless.setStatus("current")


class _RlDhcpv6ClientReconfigure_Type(Integer32):
    """Custom type rlDhcpv6ClientReconfigure based on Integer32"""
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


_RlDhcpv6ClientReconfigure_Type.__name__ = "Integer32"
_RlDhcpv6ClientReconfigure_Object = MibTableColumn
rlDhcpv6ClientReconfigure = _RlDhcpv6ClientReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 4),
    _RlDhcpv6ClientReconfigure_Type()
)
rlDhcpv6ClientReconfigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientReconfigure.setStatus("current")


class _RlDhcpv6ClientInfoRefreshMin_Type(Unsigned32):
    """Custom type rlDhcpv6ClientInfoRefreshMin based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4294967295),
    )


_RlDhcpv6ClientInfoRefreshMin_Type.__name__ = "Unsigned32"
_RlDhcpv6ClientInfoRefreshMin_Object = MibTableColumn
rlDhcpv6ClientInfoRefreshMin = _RlDhcpv6ClientInfoRefreshMin_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 5),
    _RlDhcpv6ClientInfoRefreshMin_Type()
)
rlDhcpv6ClientInfoRefreshMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpv6ClientInfoRefreshMin.setStatus("current")


class _RlDhcpv6ClientInfoRefreshConf_Type(Unsigned32):
    """Custom type rlDhcpv6ClientInfoRefreshConf based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(86400, 4294967295),
    )


_RlDhcpv6ClientInfoRefreshConf_Type.__name__ = "Unsigned32"
_RlDhcpv6ClientInfoRefreshConf_Object = MibTableColumn
rlDhcpv6ClientInfoRefreshConf = _RlDhcpv6ClientInfoRefreshConf_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 6),
    _RlDhcpv6ClientInfoRefreshConf_Type()
)
rlDhcpv6ClientInfoRefreshConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpv6ClientInfoRefreshConf.setStatus("current")
_RlDhcpv6ClientInfoRefreshReceived_Type = Unsigned32
_RlDhcpv6ClientInfoRefreshReceived_Object = MibTableColumn
rlDhcpv6ClientInfoRefreshReceived = _RlDhcpv6ClientInfoRefreshReceived_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 7),
    _RlDhcpv6ClientInfoRefreshReceived_Type()
)
rlDhcpv6ClientInfoRefreshReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientInfoRefreshReceived.setStatus("current")
_RlDhcpv6ClientInfoRefreshRemain_Type = Unsigned32
_RlDhcpv6ClientInfoRefreshRemain_Object = MibTableColumn
rlDhcpv6ClientInfoRefreshRemain = _RlDhcpv6ClientInfoRefreshRemain_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 8),
    _RlDhcpv6ClientInfoRefreshRemain_Type()
)
rlDhcpv6ClientInfoRefreshRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientInfoRefreshRemain.setStatus("current")
_RlDhcpv6ClientDhcpServerInetAddressType_Type = InetAddressType
_RlDhcpv6ClientDhcpServerInetAddressType_Object = MibTableColumn
rlDhcpv6ClientDhcpServerInetAddressType = _RlDhcpv6ClientDhcpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 9),
    _RlDhcpv6ClientDhcpServerInetAddressType_Type()
)
rlDhcpv6ClientDhcpServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientDhcpServerInetAddressType.setStatus("current")
_RlDhcpv6ClientDhcpServerInetAddress_Type = InetAddress
_RlDhcpv6ClientDhcpServerInetAddress_Object = MibTableColumn
rlDhcpv6ClientDhcpServerInetAddress = _RlDhcpv6ClientDhcpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 10),
    _RlDhcpv6ClientDhcpServerInetAddress_Type()
)
rlDhcpv6ClientDhcpServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientDhcpServerInetAddress.setStatus("current")
_RlDhcpv6ClientDhcpServerDuid_Type = OctetString
_RlDhcpv6ClientDhcpServerDuid_Object = MibTableColumn
rlDhcpv6ClientDhcpServerDuid = _RlDhcpv6ClientDhcpServerDuid_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 11),
    _RlDhcpv6ClientDhcpServerDuid_Type()
)
rlDhcpv6ClientDhcpServerDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientDhcpServerDuid.setStatus("current")
_RlDhcpv6ClientDhcpServerPreference_Type = Unsigned32
_RlDhcpv6ClientDhcpServerPreference_Object = MibTableColumn
rlDhcpv6ClientDhcpServerPreference = _RlDhcpv6ClientDhcpServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 12),
    _RlDhcpv6ClientDhcpServerPreference_Type()
)
rlDhcpv6ClientDhcpServerPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientDhcpServerPreference.setStatus("current")


class _RlDhcpv6ClientState_Type(Integer32):
    """Custom type rlDhcpv6ClientState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 3),
          ("configuring", 2),
          ("idle", 1))
    )


_RlDhcpv6ClientState_Type.__name__ = "Integer32"
_RlDhcpv6ClientState_Object = MibTableColumn
rlDhcpv6ClientState = _RlDhcpv6ClientState_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 13),
    _RlDhcpv6ClientState_Type()
)
rlDhcpv6ClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientState.setStatus("current")


class _RlDhcpv6ClientTftpServerName_Type(DisplayString):
    """Custom type rlDhcpv6ClientTftpServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlDhcpv6ClientTftpServerName_Type.__name__ = "DisplayString"
_RlDhcpv6ClientTftpServerName_Object = MibTableColumn
rlDhcpv6ClientTftpServerName = _RlDhcpv6ClientTftpServerName_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 14),
    _RlDhcpv6ClientTftpServerName_Type()
)
rlDhcpv6ClientTftpServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientTftpServerName.setStatus("current")


class _RlDhcpv6ClientTftpFileName_Type(DisplayString):
    """Custom type rlDhcpv6ClientTftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlDhcpv6ClientTftpFileName_Type.__name__ = "DisplayString"
_RlDhcpv6ClientTftpFileName_Object = MibTableColumn
rlDhcpv6ClientTftpFileName = _RlDhcpv6ClientTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 15),
    _RlDhcpv6ClientTftpFileName_Type()
)
rlDhcpv6ClientTftpFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientTftpFileName.setStatus("current")


class _RlDhcpv6ClientTimeZone_Type(DisplayString):
    """Custom type rlDhcpv6ClientTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RlDhcpv6ClientTimeZone_Type.__name__ = "DisplayString"
_RlDhcpv6ClientTimeZone_Object = MibTableColumn
rlDhcpv6ClientTimeZone = _RlDhcpv6ClientTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 16),
    _RlDhcpv6ClientTimeZone_Type()
)
rlDhcpv6ClientTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientTimeZone.setStatus("current")


class _RlDhcpv6ClientOperStatus_Type(Integer32):
    """Custom type rlDhcpv6ClientOperStatus based on Integer32"""
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


_RlDhcpv6ClientOperStatus_Type.__name__ = "Integer32"
_RlDhcpv6ClientOperStatus_Object = MibTableColumn
rlDhcpv6ClientOperStatus = _RlDhcpv6ClientOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 17),
    _RlDhcpv6ClientOperStatus_Type()
)
rlDhcpv6ClientOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientOperStatus.setStatus("current")


class _RlDhcpv6ClientDisableReason_Type(Integer32):
    """Custom type rlDhcpv6ClientDisableReason based on Integer32"""
    defaultValue = 1

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
        *(("ipv6Disable", 2),
          ("none", 1),
          ("portDown", 3),
          ("portDownAndIpv6Disable", 4))
    )


_RlDhcpv6ClientDisableReason_Type.__name__ = "Integer32"
_RlDhcpv6ClientDisableReason_Object = MibTableColumn
rlDhcpv6ClientDisableReason = _RlDhcpv6ClientDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 18),
    _RlDhcpv6ClientDisableReason_Type()
)
rlDhcpv6ClientDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientDisableReason.setStatus("current")
_RlDhcpv6ClientStatus_Type = RowStatus
_RlDhcpv6ClientStatus_Object = MibTableColumn
rlDhcpv6ClientStatus = _RlDhcpv6ClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 19),
    _RlDhcpv6ClientStatus_Type()
)
rlDhcpv6ClientStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpv6ClientStatus.setStatus("current")


class _RlDhcpv6ClientInfoRefreshIsReceived_Type(TruthValue):
    """Custom type rlDhcpv6ClientInfoRefreshIsReceived based on TruthValue"""


_RlDhcpv6ClientInfoRefreshIsReceived_Object = MibTableColumn
rlDhcpv6ClientInfoRefreshIsReceived = _RlDhcpv6ClientInfoRefreshIsReceived_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 20),
    _RlDhcpv6ClientInfoRefreshIsReceived_Type()
)
rlDhcpv6ClientInfoRefreshIsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientInfoRefreshIsReceived.setStatus("current")


class _RlDhcpv6ClientIndirectImageFileName_Type(DisplayString):
    """Custom type rlDhcpv6ClientIndirectImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlDhcpv6ClientIndirectImageFileName_Type.__name__ = "DisplayString"
_RlDhcpv6ClientIndirectImageFileName_Object = MibTableColumn
rlDhcpv6ClientIndirectImageFileName = _RlDhcpv6ClientIndirectImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 21),
    _RlDhcpv6ClientIndirectImageFileName_Type()
)
rlDhcpv6ClientIndirectImageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientIndirectImageFileName.setStatus("current")
_RlDhcpv6ClientAuxDnsServerListTable_Object = MibTable
rlDhcpv6ClientAuxDnsServerListTable = _RlDhcpv6ClientAuxDnsServerListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 4)
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDnsServerListTable.setStatus("current")
_RlDhcpv6ClientAuxDnsServerListEntry_Object = MibTableRow
rlDhcpv6ClientAuxDnsServerListEntry = _RlDhcpv6ClientAuxDnsServerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1)
)
rlDhcpv6ClientAuxDnsServerListEntry.setIndexNames(
    (0, "RADLAN-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDnsServerListIfIndex"),
    (0, "RADLAN-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDnsServerListPriority"),
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDnsServerListEntry.setStatus("current")
_RlDhcpv6ClientAuxDnsServerListIfIndex_Type = InterfaceIndex
_RlDhcpv6ClientAuxDnsServerListIfIndex_Object = MibTableColumn
rlDhcpv6ClientAuxDnsServerListIfIndex = _RlDhcpv6ClientAuxDnsServerListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1, 1),
    _RlDhcpv6ClientAuxDnsServerListIfIndex_Type()
)
rlDhcpv6ClientAuxDnsServerListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDnsServerListIfIndex.setStatus("current")
_RlDhcpv6ClientAuxDnsServerListPriority_Type = Integer32
_RlDhcpv6ClientAuxDnsServerListPriority_Object = MibTableColumn
rlDhcpv6ClientAuxDnsServerListPriority = _RlDhcpv6ClientAuxDnsServerListPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1, 2),
    _RlDhcpv6ClientAuxDnsServerListPriority_Type()
)
rlDhcpv6ClientAuxDnsServerListPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDnsServerListPriority.setStatus("current")
_RlDhcpv6ClientAuxDnsServerListAddress_Type = InetAddressIPv6
_RlDhcpv6ClientAuxDnsServerListAddress_Object = MibTableColumn
rlDhcpv6ClientAuxDnsServerListAddress = _RlDhcpv6ClientAuxDnsServerListAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1, 3),
    _RlDhcpv6ClientAuxDnsServerListAddress_Type()
)
rlDhcpv6ClientAuxDnsServerListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDnsServerListAddress.setStatus("current")
_RlDhcpv6ClientAuxSntpServerListTable_Object = MibTable
rlDhcpv6ClientAuxSntpServerListTable = _RlDhcpv6ClientAuxSntpServerListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 5)
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxSntpServerListTable.setStatus("current")
_RlDhcpv6ClientAuxSntpServerListEntry_Object = MibTableRow
rlDhcpv6ClientAuxSntpServerListEntry = _RlDhcpv6ClientAuxSntpServerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1)
)
rlDhcpv6ClientAuxSntpServerListEntry.setIndexNames(
    (0, "RADLAN-DHCPv6-CLIENT", "rlDhcpv6ClientAuxSntpServerListIfIndex"),
    (0, "RADLAN-DHCPv6-CLIENT", "rlDhcpv6ClientAuxSntpServerListPriority"),
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxSntpServerListEntry.setStatus("current")
_RlDhcpv6ClientAuxSntpServerListIfIndex_Type = InterfaceIndex
_RlDhcpv6ClientAuxSntpServerListIfIndex_Object = MibTableColumn
rlDhcpv6ClientAuxSntpServerListIfIndex = _RlDhcpv6ClientAuxSntpServerListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1, 1),
    _RlDhcpv6ClientAuxSntpServerListIfIndex_Type()
)
rlDhcpv6ClientAuxSntpServerListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxSntpServerListIfIndex.setStatus("current")
_RlDhcpv6ClientAuxSntpServerListPriority_Type = Integer32
_RlDhcpv6ClientAuxSntpServerListPriority_Object = MibTableColumn
rlDhcpv6ClientAuxSntpServerListPriority = _RlDhcpv6ClientAuxSntpServerListPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1, 2),
    _RlDhcpv6ClientAuxSntpServerListPriority_Type()
)
rlDhcpv6ClientAuxSntpServerListPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxSntpServerListPriority.setStatus("current")
_RlDhcpv6ClientAuxSntpServerListAddress_Type = InetAddressIPv6
_RlDhcpv6ClientAuxSntpServerListAddress_Object = MibTableColumn
rlDhcpv6ClientAuxSntpServerListAddress = _RlDhcpv6ClientAuxSntpServerListAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1, 3),
    _RlDhcpv6ClientAuxSntpServerListAddress_Type()
)
rlDhcpv6ClientAuxSntpServerListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxSntpServerListAddress.setStatus("current")
_RlDhcpv6ClientAuxDomainNameSearchListTable_Object = MibTable
rlDhcpv6ClientAuxDomainNameSearchListTable = _RlDhcpv6ClientAuxDomainNameSearchListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 6)
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDomainNameSearchListTable.setStatus("current")
_RlDhcpv6ClientAuxDomainNameSearchListEntry_Object = MibTableRow
rlDhcpv6ClientAuxDomainNameSearchListEntry = _RlDhcpv6ClientAuxDomainNameSearchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1)
)
rlDhcpv6ClientAuxDomainNameSearchListEntry.setIndexNames(
    (0, "RADLAN-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDomainNameSearchListIfIndex"),
    (0, "RADLAN-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDomainNameSearchListPriority"),
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDomainNameSearchListEntry.setStatus("current")
_RlDhcpv6ClientAuxDomainNameSearchListIfIndex_Type = InterfaceIndex
_RlDhcpv6ClientAuxDomainNameSearchListIfIndex_Object = MibTableColumn
rlDhcpv6ClientAuxDomainNameSearchListIfIndex = _RlDhcpv6ClientAuxDomainNameSearchListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1, 1),
    _RlDhcpv6ClientAuxDomainNameSearchListIfIndex_Type()
)
rlDhcpv6ClientAuxDomainNameSearchListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDomainNameSearchListIfIndex.setStatus("current")
_RlDhcpv6ClientAuxDomainNameSearchListPriority_Type = Integer32
_RlDhcpv6ClientAuxDomainNameSearchListPriority_Object = MibTableColumn
rlDhcpv6ClientAuxDomainNameSearchListPriority = _RlDhcpv6ClientAuxDomainNameSearchListPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1, 2),
    _RlDhcpv6ClientAuxDomainNameSearchListPriority_Type()
)
rlDhcpv6ClientAuxDomainNameSearchListPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDomainNameSearchListPriority.setStatus("current")


class _RlDhcpv6ClientAuxDomainNameSearchListName_Type(DisplayString):
    """Custom type rlDhcpv6ClientAuxDomainNameSearchListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlDhcpv6ClientAuxDomainNameSearchListName_Type.__name__ = "DisplayString"
_RlDhcpv6ClientAuxDomainNameSearchListName_Object = MibTableColumn
rlDhcpv6ClientAuxDomainNameSearchListName = _RlDhcpv6ClientAuxDomainNameSearchListName_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1, 3),
    _RlDhcpv6ClientAuxDomainNameSearchListName_Type()
)
rlDhcpv6ClientAuxDomainNameSearchListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpv6ClientAuxDomainNameSearchListName.setStatus("current")
_RlDhcpv6ClientCommandTable_Object = MibTable
rlDhcpv6ClientCommandTable = _RlDhcpv6ClientCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 7)
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientCommandTable.setStatus("current")
_RlDhcpv6ClientCommandEntry_Object = MibTableRow
rlDhcpv6ClientCommandEntry = _RlDhcpv6ClientCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 7, 1)
)
rlDhcpv6ClientCommandEntry.setIndexNames(
    (0, "RADLAN-DHCPv6-CLIENT", "rlDhcpv6ClientCommandIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpv6ClientCommandEntry.setStatus("current")
_RlDhcpv6ClientCommandIfIndex_Type = InterfaceIndex
_RlDhcpv6ClientCommandIfIndex_Object = MibTableColumn
rlDhcpv6ClientCommandIfIndex = _RlDhcpv6ClientCommandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 7, 1, 1),
    _RlDhcpv6ClientCommandIfIndex_Type()
)
rlDhcpv6ClientCommandIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6ClientCommandIfIndex.setStatus("current")


class _RlDhcpv6ClientCommandAction_Type(Integer32):
    """Custom type rlDhcpv6ClientCommandAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("renew", 1))
    )


_RlDhcpv6ClientCommandAction_Type.__name__ = "Integer32"
_RlDhcpv6ClientCommandAction_Object = MibTableColumn
rlDhcpv6ClientCommandAction = _RlDhcpv6ClientCommandAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 7, 1, 2),
    _RlDhcpv6ClientCommandAction_Type()
)
rlDhcpv6ClientCommandAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpv6ClientCommandAction.setStatus("current")


class _RlDhcpv6ClientEnabledByDefaultRemovedIfindex_Type(Integer32):
    """Custom type rlDhcpv6ClientEnabledByDefaultRemovedIfindex based on Integer32"""
    defaultValue = 0


_RlDhcpv6ClientEnabledByDefaultRemovedIfindex_Object = MibScalar
rlDhcpv6ClientEnabledByDefaultRemovedIfindex = _RlDhcpv6ClientEnabledByDefaultRemovedIfindex_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 2, 8),
    _RlDhcpv6ClientEnabledByDefaultRemovedIfindex_Type()
)
rlDhcpv6ClientEnabledByDefaultRemovedIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpv6ClientEnabledByDefaultRemovedIfindex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-DHCPv6-CLIENT",
    **{"rlDhcpv6ClientMibVersion": rlDhcpv6ClientMibVersion,
       "rlDhcpv6ClientSupported": rlDhcpv6ClientSupported,
       "rlDhcpv6ClientTable": rlDhcpv6ClientTable,
       "rlDhcpv6ClientEntry": rlDhcpv6ClientEntry,
       "rlDhcpv6ClientIfIndex": rlDhcpv6ClientIfIndex,
       "rlDhcpv6ClientPd": rlDhcpv6ClientPd,
       "rlDhcpv6ClientStateless": rlDhcpv6ClientStateless,
       "rlDhcpv6ClientReconfigure": rlDhcpv6ClientReconfigure,
       "rlDhcpv6ClientInfoRefreshMin": rlDhcpv6ClientInfoRefreshMin,
       "rlDhcpv6ClientInfoRefreshConf": rlDhcpv6ClientInfoRefreshConf,
       "rlDhcpv6ClientInfoRefreshReceived": rlDhcpv6ClientInfoRefreshReceived,
       "rlDhcpv6ClientInfoRefreshRemain": rlDhcpv6ClientInfoRefreshRemain,
       "rlDhcpv6ClientDhcpServerInetAddressType": rlDhcpv6ClientDhcpServerInetAddressType,
       "rlDhcpv6ClientDhcpServerInetAddress": rlDhcpv6ClientDhcpServerInetAddress,
       "rlDhcpv6ClientDhcpServerDuid": rlDhcpv6ClientDhcpServerDuid,
       "rlDhcpv6ClientDhcpServerPreference": rlDhcpv6ClientDhcpServerPreference,
       "rlDhcpv6ClientState": rlDhcpv6ClientState,
       "rlDhcpv6ClientTftpServerName": rlDhcpv6ClientTftpServerName,
       "rlDhcpv6ClientTftpFileName": rlDhcpv6ClientTftpFileName,
       "rlDhcpv6ClientTimeZone": rlDhcpv6ClientTimeZone,
       "rlDhcpv6ClientOperStatus": rlDhcpv6ClientOperStatus,
       "rlDhcpv6ClientDisableReason": rlDhcpv6ClientDisableReason,
       "rlDhcpv6ClientStatus": rlDhcpv6ClientStatus,
       "rlDhcpv6ClientInfoRefreshIsReceived": rlDhcpv6ClientInfoRefreshIsReceived,
       "rlDhcpv6ClientIndirectImageFileName": rlDhcpv6ClientIndirectImageFileName,
       "rlDhcpv6ClientAuxDnsServerListTable": rlDhcpv6ClientAuxDnsServerListTable,
       "rlDhcpv6ClientAuxDnsServerListEntry": rlDhcpv6ClientAuxDnsServerListEntry,
       "rlDhcpv6ClientAuxDnsServerListIfIndex": rlDhcpv6ClientAuxDnsServerListIfIndex,
       "rlDhcpv6ClientAuxDnsServerListPriority": rlDhcpv6ClientAuxDnsServerListPriority,
       "rlDhcpv6ClientAuxDnsServerListAddress": rlDhcpv6ClientAuxDnsServerListAddress,
       "rlDhcpv6ClientAuxSntpServerListTable": rlDhcpv6ClientAuxSntpServerListTable,
       "rlDhcpv6ClientAuxSntpServerListEntry": rlDhcpv6ClientAuxSntpServerListEntry,
       "rlDhcpv6ClientAuxSntpServerListIfIndex": rlDhcpv6ClientAuxSntpServerListIfIndex,
       "rlDhcpv6ClientAuxSntpServerListPriority": rlDhcpv6ClientAuxSntpServerListPriority,
       "rlDhcpv6ClientAuxSntpServerListAddress": rlDhcpv6ClientAuxSntpServerListAddress,
       "rlDhcpv6ClientAuxDomainNameSearchListTable": rlDhcpv6ClientAuxDomainNameSearchListTable,
       "rlDhcpv6ClientAuxDomainNameSearchListEntry": rlDhcpv6ClientAuxDomainNameSearchListEntry,
       "rlDhcpv6ClientAuxDomainNameSearchListIfIndex": rlDhcpv6ClientAuxDomainNameSearchListIfIndex,
       "rlDhcpv6ClientAuxDomainNameSearchListPriority": rlDhcpv6ClientAuxDomainNameSearchListPriority,
       "rlDhcpv6ClientAuxDomainNameSearchListName": rlDhcpv6ClientAuxDomainNameSearchListName,
       "rlDhcpv6ClientCommandTable": rlDhcpv6ClientCommandTable,
       "rlDhcpv6ClientCommandEntry": rlDhcpv6ClientCommandEntry,
       "rlDhcpv6ClientCommandIfIndex": rlDhcpv6ClientCommandIfIndex,
       "rlDhcpv6ClientCommandAction": rlDhcpv6ClientCommandAction,
       "rlDhcpv6ClientEnabledByDefaultRemovedIfindex": rlDhcpv6ClientEnabledByDefaultRemovedIfindex}
)
