# SNMP MIB module (CISCOSB-DNSCL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-DNSCL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:13 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(dnsResConfigSbeltEntry,) = mibBuilder.importSymbols(
    "DNS-RESOLVER-MIB",
    "dnsResConfigSbeltEntry")

(DnsClass,
 DnsName,
 DnsNameAsIndex,
 DnsOpCode,
 DnsQClass,
 DnsQType,
 DnsRespCode,
 DnsTime,
 DnsType,
 dns) = mibBuilder.importSymbols(
    "DNS-SERVER-MIB",
    "DnsClass",
    "DnsName",
    "DnsNameAsIndex",
    "DnsOpCode",
    "DnsQClass",
    "DnsQType",
    "DnsRespCode",
    "DnsTime",
    "DnsType",
    "dns")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlDnsCl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93)
)
rlDnsCl.setRevisions(
        ("2013-04-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDnsClMibVersion_Type = Integer32
_RlDnsClMibVersion_Object = MibScalar
rlDnsClMibVersion = _RlDnsClMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 1),
    _RlDnsClMibVersion_Type()
)
rlDnsClMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClMibVersion.setStatus("current")


class _RlDnsClEnable_Type(Integer32):
    """Custom type rlDnsClEnable based on Integer32"""
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


_RlDnsClEnable_Type.__name__ = "Integer32"
_RlDnsClEnable_Object = MibScalar
rlDnsClEnable = _RlDnsClEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 2),
    _RlDnsClEnable_Type()
)
rlDnsClEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClEnable.setStatus("current")
_RlDnsClDomainNameTable_Object = MibTable
rlDnsClDomainNameTable = _RlDnsClDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 3)
)
if mibBuilder.loadTexts:
    rlDnsClDomainNameTable.setStatus("current")
_RlDnsClDomainNameEntry_Object = MibTableRow
rlDnsClDomainNameEntry = _RlDnsClDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 3, 1)
)
rlDnsClDomainNameEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClDomainNameName"),
)
if mibBuilder.loadTexts:
    rlDnsClDomainNameEntry.setStatus("current")
_RlDnsClDomainNameName_Type = DnsNameAsIndex
_RlDnsClDomainNameName_Object = MibTableColumn
rlDnsClDomainNameName = _RlDnsClDomainNameName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 3, 1, 1),
    _RlDnsClDomainNameName_Type()
)
rlDnsClDomainNameName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClDomainNameName.setStatus("current")


class _RlDnsClDomainNameOwner_Type(Integer32):
    """Custom type rlDnsClDomainNameOwner based on Integer32"""
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
        *(("dhcp", 2),
          ("dhcpv6", 3),
          ("static", 1))
    )


_RlDnsClDomainNameOwner_Type.__name__ = "Integer32"
_RlDnsClDomainNameOwner_Object = MibTableColumn
rlDnsClDomainNameOwner = _RlDnsClDomainNameOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 3, 1, 2),
    _RlDnsClDomainNameOwner_Type()
)
rlDnsClDomainNameOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClDomainNameOwner.setStatus("current")
_RlDnsClDomainNameRowStatus_Type = RowStatus
_RlDnsClDomainNameRowStatus_Object = MibTableColumn
rlDnsClDomainNameRowStatus = _RlDnsClDomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 3, 1, 3),
    _RlDnsClDomainNameRowStatus_Type()
)
rlDnsClDomainNameRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClDomainNameRowStatus.setStatus("current")


class _RlDnsClMaxNumOfRetransmissions_Type(Integer32):
    """Custom type rlDnsClMaxNumOfRetransmissions based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlDnsClMaxNumOfRetransmissions_Type.__name__ = "Integer32"
_RlDnsClMaxNumOfRetransmissions_Object = MibScalar
rlDnsClMaxNumOfRetransmissions = _RlDnsClMaxNumOfRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 4),
    _RlDnsClMaxNumOfRetransmissions_Type()
)
rlDnsClMaxNumOfRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClMaxNumOfRetransmissions.setStatus("current")


class _RlDnsClMinRetransmissionInterval_Type(Integer32):
    """Custom type rlDnsClMinRetransmissionInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RlDnsClMinRetransmissionInterval_Type.__name__ = "Integer32"
_RlDnsClMinRetransmissionInterval_Object = MibScalar
rlDnsClMinRetransmissionInterval = _RlDnsClMinRetransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 5),
    _RlDnsClMinRetransmissionInterval_Type()
)
rlDnsClMinRetransmissionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClMinRetransmissionInterval.setStatus("current")
_RlDnsClNamesTable_Object = MibTable
rlDnsClNamesTable = _RlDnsClNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 6)
)
if mibBuilder.loadTexts:
    rlDnsClNamesTable.setStatus("current")
_RlDnsClNamesEntry_Object = MibTableRow
rlDnsClNamesEntry = _RlDnsClNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 6, 1)
)
rlDnsClNamesEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClNamesName"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClNamesOwner"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClNamesIndex"),
)
if mibBuilder.loadTexts:
    rlDnsClNamesEntry.setStatus("current")
_RlDnsClNamesName_Type = DnsNameAsIndex
_RlDnsClNamesName_Object = MibTableColumn
rlDnsClNamesName = _RlDnsClNamesName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 6, 1, 1),
    _RlDnsClNamesName_Type()
)
rlDnsClNamesName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClNamesName.setStatus("current")


class _RlDnsClNamesOwner_Type(Integer32):
    """Custom type rlDnsClNamesOwner based on Integer32"""
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
        *(("dhcp", 2),
          ("dhcpv6", 3),
          ("static", 1))
    )


_RlDnsClNamesOwner_Type.__name__ = "Integer32"
_RlDnsClNamesOwner_Object = MibTableColumn
rlDnsClNamesOwner = _RlDnsClNamesOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 6, 1, 2),
    _RlDnsClNamesOwner_Type()
)
rlDnsClNamesOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClNamesOwner.setStatus("current")
_RlDnsClNamesIndex_Type = Integer32
_RlDnsClNamesIndex_Object = MibTableColumn
rlDnsClNamesIndex = _RlDnsClNamesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 6, 1, 3),
    _RlDnsClNamesIndex_Type()
)
rlDnsClNamesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClNamesIndex.setStatus("current")
_RlDnsClNamesAddr_Type = IpAddress
_RlDnsClNamesAddr_Object = MibTableColumn
rlDnsClNamesAddr = _RlDnsClNamesAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 6, 1, 4),
    _RlDnsClNamesAddr_Type()
)
rlDnsClNamesAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClNamesAddr.setStatus("current")
_RlDnsClNamesRowStatus_Type = RowStatus
_RlDnsClNamesRowStatus_Object = MibTableColumn
rlDnsClNamesRowStatus = _RlDnsClNamesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 6, 1, 5),
    _RlDnsClNamesRowStatus_Type()
)
rlDnsClNamesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClNamesRowStatus.setStatus("current")
_RlDnsResConfigSbeltExtTable_Object = MibTable
rlDnsResConfigSbeltExtTable = _RlDnsResConfigSbeltExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 7)
)
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltExtTable.setStatus("current")
_RlDnsResConfigSbeltExtEntry_Object = MibTableRow
rlDnsResConfigSbeltExtEntry = _RlDnsResConfigSbeltExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 7, 1)
)
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltExtEntry.setStatus("current")


class _RlDnsResConfigSbeltOwner_Type(Integer32):
    """Custom type rlDnsResConfigSbeltOwner based on Integer32"""
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
        *(("dhcp", 2),
          ("dhcpv6", 3),
          ("static", 1))
    )


_RlDnsResConfigSbeltOwner_Type.__name__ = "Integer32"
_RlDnsResConfigSbeltOwner_Object = MibTableColumn
rlDnsResConfigSbeltOwner = _RlDnsResConfigSbeltOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 7, 1, 1),
    _RlDnsResConfigSbeltOwner_Type()
)
rlDnsResConfigSbeltOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltOwner.setStatus("current")
_RlDnsClNamesInetTable_Object = MibTable
rlDnsClNamesInetTable = _RlDnsClNamesInetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 8)
)
if mibBuilder.loadTexts:
    rlDnsClNamesInetTable.setStatus("current")
_RlDnsClNamesInetEntry_Object = MibTableRow
rlDnsClNamesInetEntry = _RlDnsClNamesInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 8, 1)
)
rlDnsClNamesInetEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClNamesInetName"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClNamesInetOwner"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClNamesInetIndex"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClNamesInetRRType"),
)
if mibBuilder.loadTexts:
    rlDnsClNamesInetEntry.setStatus("current")
_RlDnsClNamesInetName_Type = DnsNameAsIndex
_RlDnsClNamesInetName_Object = MibTableColumn
rlDnsClNamesInetName = _RlDnsClNamesInetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 8, 1, 1),
    _RlDnsClNamesInetName_Type()
)
rlDnsClNamesInetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClNamesInetName.setStatus("current")


class _RlDnsClNamesInetOwner_Type(Integer32):
    """Custom type rlDnsClNamesInetOwner based on Integer32"""
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
        *(("dhcp", 2),
          ("dhcpv6", 3),
          ("static", 1))
    )


_RlDnsClNamesInetOwner_Type.__name__ = "Integer32"
_RlDnsClNamesInetOwner_Object = MibTableColumn
rlDnsClNamesInetOwner = _RlDnsClNamesInetOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 8, 1, 2),
    _RlDnsClNamesInetOwner_Type()
)
rlDnsClNamesInetOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClNamesInetOwner.setStatus("current")
_RlDnsClNamesInetIndex_Type = Integer32
_RlDnsClNamesInetIndex_Object = MibTableColumn
rlDnsClNamesInetIndex = _RlDnsClNamesInetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 8, 1, 3),
    _RlDnsClNamesInetIndex_Type()
)
rlDnsClNamesInetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClNamesInetIndex.setStatus("current")
_RlDnsClNamesInetRRType_Type = DnsType
_RlDnsClNamesInetRRType_Object = MibTableColumn
rlDnsClNamesInetRRType = _RlDnsClNamesInetRRType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 8, 1, 4),
    _RlDnsClNamesInetRRType_Type()
)
rlDnsClNamesInetRRType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClNamesInetRRType.setStatus("current")
_RlDnsClNamesInetAddrType_Type = InetAddressType
_RlDnsClNamesInetAddrType_Object = MibTableColumn
rlDnsClNamesInetAddrType = _RlDnsClNamesInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 8, 1, 5),
    _RlDnsClNamesInetAddrType_Type()
)
rlDnsClNamesInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClNamesInetAddrType.setStatus("current")
_RlDnsClNamesInetAddr_Type = InetAddress
_RlDnsClNamesInetAddr_Object = MibTableColumn
rlDnsClNamesInetAddr = _RlDnsClNamesInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 8, 1, 6),
    _RlDnsClNamesInetAddr_Type()
)
rlDnsClNamesInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClNamesInetAddr.setStatus("current")
_RlDnsClNamesInetRowStatus_Type = RowStatus
_RlDnsClNamesInetRowStatus_Object = MibTableColumn
rlDnsClNamesInetRowStatus = _RlDnsClNamesInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 8, 1, 7),
    _RlDnsClNamesInetRowStatus_Type()
)
rlDnsClNamesInetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClNamesInetRowStatus.setStatus("current")
_RlDnsResConfigSbeltInetTable_Object = MibTable
rlDnsResConfigSbeltInetTable = _RlDnsResConfigSbeltInetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9)
)
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetTable.setStatus("current")
_RlDnsResConfigSbeltInetEntry_Object = MibTableRow
rlDnsResConfigSbeltInetEntry = _RlDnsResConfigSbeltInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9, 1)
)
rlDnsResConfigSbeltInetEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResConfigSbeltInetAddrType"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResConfigSbeltInetAddr"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResConfigSbeltInetSubTree"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResConfigSbeltInetClass"),
)
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetEntry.setStatus("current")
_RlDnsResConfigSbeltInetAddrType_Type = InetAddressType
_RlDnsResConfigSbeltInetAddrType_Object = MibTableColumn
rlDnsResConfigSbeltInetAddrType = _RlDnsResConfigSbeltInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9, 1, 1),
    _RlDnsResConfigSbeltInetAddrType_Type()
)
rlDnsResConfigSbeltInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetAddrType.setStatus("current")
_RlDnsResConfigSbeltInetAddr_Type = InetAddress
_RlDnsResConfigSbeltInetAddr_Object = MibTableColumn
rlDnsResConfigSbeltInetAddr = _RlDnsResConfigSbeltInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9, 1, 2),
    _RlDnsResConfigSbeltInetAddr_Type()
)
rlDnsResConfigSbeltInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetAddr.setStatus("current")
_RlDnsResConfigSbeltInetName_Type = DnsName
_RlDnsResConfigSbeltInetName_Object = MibTableColumn
rlDnsResConfigSbeltInetName = _RlDnsResConfigSbeltInetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9, 1, 3),
    _RlDnsResConfigSbeltInetName_Type()
)
rlDnsResConfigSbeltInetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetName.setStatus("current")


class _RlDnsResConfigSbeltInetRecursion_Type(Integer32):
    """Custom type rlDnsResConfigSbeltInetRecursion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iterative", 1),
          ("recursive", 2),
          ("recursiveAndIterative", 3))
    )


_RlDnsResConfigSbeltInetRecursion_Type.__name__ = "Integer32"
_RlDnsResConfigSbeltInetRecursion_Object = MibTableColumn
rlDnsResConfigSbeltInetRecursion = _RlDnsResConfigSbeltInetRecursion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9, 1, 4),
    _RlDnsResConfigSbeltInetRecursion_Type()
)
rlDnsResConfigSbeltInetRecursion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetRecursion.setStatus("current")


class _RlDnsResConfigSbeltInetPref_Type(Integer32):
    """Custom type rlDnsResConfigSbeltInetPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlDnsResConfigSbeltInetPref_Type.__name__ = "Integer32"
_RlDnsResConfigSbeltInetPref_Object = MibTableColumn
rlDnsResConfigSbeltInetPref = _RlDnsResConfigSbeltInetPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9, 1, 5),
    _RlDnsResConfigSbeltInetPref_Type()
)
rlDnsResConfigSbeltInetPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetPref.setStatus("current")
_RlDnsResConfigSbeltInetSubTree_Type = DnsNameAsIndex
_RlDnsResConfigSbeltInetSubTree_Object = MibTableColumn
rlDnsResConfigSbeltInetSubTree = _RlDnsResConfigSbeltInetSubTree_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9, 1, 6),
    _RlDnsResConfigSbeltInetSubTree_Type()
)
rlDnsResConfigSbeltInetSubTree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetSubTree.setStatus("current")
_RlDnsResConfigSbeltInetClass_Type = DnsClass
_RlDnsResConfigSbeltInetClass_Object = MibTableColumn
rlDnsResConfigSbeltInetClass = _RlDnsResConfigSbeltInetClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9, 1, 7),
    _RlDnsResConfigSbeltInetClass_Type()
)
rlDnsResConfigSbeltInetClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetClass.setStatus("current")
_RlDnsResConfigSbeltInetStatus_Type = RowStatus
_RlDnsResConfigSbeltInetStatus_Object = MibTableColumn
rlDnsResConfigSbeltInetStatus = _RlDnsResConfigSbeltInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 9, 1, 8),
    _RlDnsResConfigSbeltInetStatus_Type()
)
rlDnsResConfigSbeltInetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetStatus.setStatus("current")
_RlDnsResCacheRRInetTable_Object = MibTable
rlDnsResCacheRRInetTable = _RlDnsResCacheRRInetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10)
)
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetTable.setStatus("current")
_RlDnsResCacheRRInetEntry_Object = MibTableRow
rlDnsResCacheRRInetEntry = _RlDnsResCacheRRInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1)
)
rlDnsResCacheRRInetEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResCacheRRInetName"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResCacheRRInetClass"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResCacheRRInetType"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResCacheRRInetIndex"),
)
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetEntry.setStatus("current")
_RlDnsResCacheRRInetName_Type = DnsNameAsIndex
_RlDnsResCacheRRInetName_Object = MibTableColumn
rlDnsResCacheRRInetName = _RlDnsResCacheRRInetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 1),
    _RlDnsResCacheRRInetName_Type()
)
rlDnsResCacheRRInetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetName.setStatus("current")
_RlDnsResCacheRRInetClass_Type = DnsClass
_RlDnsResCacheRRInetClass_Object = MibTableColumn
rlDnsResCacheRRInetClass = _RlDnsResCacheRRInetClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 2),
    _RlDnsResCacheRRInetClass_Type()
)
rlDnsResCacheRRInetClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetClass.setStatus("current")
_RlDnsResCacheRRInetType_Type = DnsType
_RlDnsResCacheRRInetType_Object = MibTableColumn
rlDnsResCacheRRInetType = _RlDnsResCacheRRInetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 3),
    _RlDnsResCacheRRInetType_Type()
)
rlDnsResCacheRRInetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetType.setStatus("current")
_RlDnsResCacheRRInetTTL_Type = DnsTime
_RlDnsResCacheRRInetTTL_Object = MibTableColumn
rlDnsResCacheRRInetTTL = _RlDnsResCacheRRInetTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 4),
    _RlDnsResCacheRRInetTTL_Type()
)
rlDnsResCacheRRInetTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetTTL.setStatus("current")
_RlDnsResCacheRRInetElapsedTTL_Type = DnsTime
_RlDnsResCacheRRInetElapsedTTL_Object = MibTableColumn
rlDnsResCacheRRInetElapsedTTL = _RlDnsResCacheRRInetElapsedTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 5),
    _RlDnsResCacheRRInetElapsedTTL_Type()
)
rlDnsResCacheRRInetElapsedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetElapsedTTL.setStatus("current")
_RlDnsResCacheRRInetSourceAddrType_Type = InetAddressType
_RlDnsResCacheRRInetSourceAddrType_Object = MibTableColumn
rlDnsResCacheRRInetSourceAddrType = _RlDnsResCacheRRInetSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 6),
    _RlDnsResCacheRRInetSourceAddrType_Type()
)
rlDnsResCacheRRInetSourceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetSourceAddrType.setStatus("current")
_RlDnsResCacheRRInetSource_Type = InetAddress
_RlDnsResCacheRRInetSource_Object = MibTableColumn
rlDnsResCacheRRInetSource = _RlDnsResCacheRRInetSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 7),
    _RlDnsResCacheRRInetSource_Type()
)
rlDnsResCacheRRInetSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetSource.setStatus("current")
_RlDnsResCacheRRInetData_Type = OctetString
_RlDnsResCacheRRInetData_Object = MibTableColumn
rlDnsResCacheRRInetData = _RlDnsResCacheRRInetData_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 8),
    _RlDnsResCacheRRInetData_Type()
)
rlDnsResCacheRRInetData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetData.setStatus("current")
_RlDnsResCacheRRInetStatus_Type = RowStatus
_RlDnsResCacheRRInetStatus_Object = MibTableColumn
rlDnsResCacheRRInetStatus = _RlDnsResCacheRRInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 9),
    _RlDnsResCacheRRInetStatus_Type()
)
rlDnsResCacheRRInetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetStatus.setStatus("current")
_RlDnsResCacheRRInetIndex_Type = Integer32
_RlDnsResCacheRRInetIndex_Object = MibTableColumn
rlDnsResCacheRRInetIndex = _RlDnsResCacheRRInetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 10),
    _RlDnsResCacheRRInetIndex_Type()
)
rlDnsResCacheRRInetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetIndex.setStatus("current")
_RlDnsResCacheRRInetPrettyName_Type = DnsName
_RlDnsResCacheRRInetPrettyName_Object = MibTableColumn
rlDnsResCacheRRInetPrettyName = _RlDnsResCacheRRInetPrettyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 10, 1, 11),
    _RlDnsResCacheRRInetPrettyName_Type()
)
rlDnsResCacheRRInetPrettyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResCacheRRInetPrettyName.setStatus("current")
_RlDnsResNCacheErrInetTable_Object = MibTable
rlDnsResNCacheErrInetTable = _RlDnsResNCacheErrInetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11)
)
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetTable.setStatus("current")
_RlDnsResNCacheErrInetEntry_Object = MibTableRow
rlDnsResNCacheErrInetEntry = _RlDnsResNCacheErrInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1)
)
rlDnsResNCacheErrInetEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResNCacheErrInetQName"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResNCacheErrInetQClass"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResNCacheErrInetQType"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsResNCacheErrInetIndex"),
)
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetEntry.setStatus("current")
_RlDnsResNCacheErrInetQName_Type = DnsNameAsIndex
_RlDnsResNCacheErrInetQName_Object = MibTableColumn
rlDnsResNCacheErrInetQName = _RlDnsResNCacheErrInetQName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 1),
    _RlDnsResNCacheErrInetQName_Type()
)
rlDnsResNCacheErrInetQName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetQName.setStatus("current")
_RlDnsResNCacheErrInetQClass_Type = DnsQClass
_RlDnsResNCacheErrInetQClass_Object = MibTableColumn
rlDnsResNCacheErrInetQClass = _RlDnsResNCacheErrInetQClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 2),
    _RlDnsResNCacheErrInetQClass_Type()
)
rlDnsResNCacheErrInetQClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetQClass.setStatus("current")
_RlDnsResNCacheErrInetQType_Type = DnsQType
_RlDnsResNCacheErrInetQType_Object = MibTableColumn
rlDnsResNCacheErrInetQType = _RlDnsResNCacheErrInetQType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 3),
    _RlDnsResNCacheErrInetQType_Type()
)
rlDnsResNCacheErrInetQType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetQType.setStatus("current")
_RlDnsResNCacheErrInetTTL_Type = DnsTime
_RlDnsResNCacheErrInetTTL_Object = MibTableColumn
rlDnsResNCacheErrInetTTL = _RlDnsResNCacheErrInetTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 4),
    _RlDnsResNCacheErrInetTTL_Type()
)
rlDnsResNCacheErrInetTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetTTL.setStatus("current")
_RlDnsResNCacheErrInetElapsedTTL_Type = DnsTime
_RlDnsResNCacheErrInetElapsedTTL_Object = MibTableColumn
rlDnsResNCacheErrInetElapsedTTL = _RlDnsResNCacheErrInetElapsedTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 5),
    _RlDnsResNCacheErrInetElapsedTTL_Type()
)
rlDnsResNCacheErrInetElapsedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetElapsedTTL.setStatus("current")
_RlDnsResNCacheErrInetSourceAddrType_Type = InetAddressType
_RlDnsResNCacheErrInetSourceAddrType_Object = MibTableColumn
rlDnsResNCacheErrInetSourceAddrType = _RlDnsResNCacheErrInetSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 6),
    _RlDnsResNCacheErrInetSourceAddrType_Type()
)
rlDnsResNCacheErrInetSourceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetSourceAddrType.setStatus("current")
_RlDnsResNCacheErrInetSource_Type = InetAddress
_RlDnsResNCacheErrInetSource_Object = MibTableColumn
rlDnsResNCacheErrInetSource = _RlDnsResNCacheErrInetSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 7),
    _RlDnsResNCacheErrInetSource_Type()
)
rlDnsResNCacheErrInetSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetSource.setStatus("current")


class _RlDnsResNCacheErrInetCode_Type(Integer32):
    """Custom type rlDnsResNCacheErrInetCode based on Integer32"""
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
        *(("noData", 2),
          ("nonexistantName", 1),
          ("other", 3),
          ("unresolved", 4))
    )


_RlDnsResNCacheErrInetCode_Type.__name__ = "Integer32"
_RlDnsResNCacheErrInetCode_Object = MibTableColumn
rlDnsResNCacheErrInetCode = _RlDnsResNCacheErrInetCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 8),
    _RlDnsResNCacheErrInetCode_Type()
)
rlDnsResNCacheErrInetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetCode.setStatus("current")
_RlDnsResNCacheErrInetStatus_Type = RowStatus
_RlDnsResNCacheErrInetStatus_Object = MibTableColumn
rlDnsResNCacheErrInetStatus = _RlDnsResNCacheErrInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 9),
    _RlDnsResNCacheErrInetStatus_Type()
)
rlDnsResNCacheErrInetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetStatus.setStatus("current")
_RlDnsResNCacheErrInetIndex_Type = Integer32
_RlDnsResNCacheErrInetIndex_Object = MibTableColumn
rlDnsResNCacheErrInetIndex = _RlDnsResNCacheErrInetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 10),
    _RlDnsResNCacheErrInetIndex_Type()
)
rlDnsResNCacheErrInetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetIndex.setStatus("current")
_RlDnsResNCacheErrInetPrettyName_Type = DnsName
_RlDnsResNCacheErrInetPrettyName_Object = MibTableColumn
rlDnsResNCacheErrInetPrettyName = _RlDnsResNCacheErrInetPrettyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 11, 1, 11),
    _RlDnsResNCacheErrInetPrettyName_Type()
)
rlDnsResNCacheErrInetPrettyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsResNCacheErrInetPrettyName.setStatus("current")
_RlDnsResConfigSbeltExtInetTable_Object = MibTable
rlDnsResConfigSbeltExtInetTable = _RlDnsResConfigSbeltExtInetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 12)
)
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltExtInetTable.setStatus("current")
_RlDnsResConfigSbeltExtInetEntry_Object = MibTableRow
rlDnsResConfigSbeltExtInetEntry = _RlDnsResConfigSbeltExtInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 12, 1)
)
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltExtInetEntry.setStatus("current")


class _RlDnsResConfigSbeltInetOwner_Type(Integer32):
    """Custom type rlDnsResConfigSbeltInetOwner based on Integer32"""
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
        *(("dhcp", 2),
          ("dhcpv6", 3),
          ("static", 1))
    )


_RlDnsResConfigSbeltInetOwner_Type.__name__ = "Integer32"
_RlDnsResConfigSbeltInetOwner_Object = MibTableColumn
rlDnsResConfigSbeltInetOwner = _RlDnsResConfigSbeltInetOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 12, 1, 1),
    _RlDnsResConfigSbeltInetOwner_Type()
)
rlDnsResConfigSbeltInetOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsResConfigSbeltInetOwner.setStatus("current")


class _RlDnsClMinPollingInterval_Type(Integer32):
    """Custom type rlDnsClMinPollingInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RlDnsClMinPollingInterval_Type.__name__ = "Integer32"
_RlDnsClMinPollingInterval_Object = MibScalar
rlDnsClMinPollingInterval = _RlDnsClMinPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 13),
    _RlDnsClMinPollingInterval_Type()
)
rlDnsClMinPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClMinPollingInterval.setStatus("current")
_RlDnsClv2DomainNameTable_Object = MibTable
rlDnsClv2DomainNameTable = _RlDnsClv2DomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 14)
)
if mibBuilder.loadTexts:
    rlDnsClv2DomainNameTable.setStatus("current")
_RlDnsClv2DomainNameEntry_Object = MibTableRow
rlDnsClv2DomainNameEntry = _RlDnsClv2DomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 14, 1)
)
rlDnsClv2DomainNameEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2DomainNameSource"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2DomainNameIfIndex"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2DomainNamePreference"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2DomainNameName"),
)
if mibBuilder.loadTexts:
    rlDnsClv2DomainNameEntry.setStatus("current")


class _RlDnsClv2DomainNameSource_Type(Integer32):
    """Custom type rlDnsClv2DomainNameSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv4", 4),
          ("dhcpv6", 3),
          ("static", 1))
    )


_RlDnsClv2DomainNameSource_Type.__name__ = "Integer32"
_RlDnsClv2DomainNameSource_Object = MibTableColumn
rlDnsClv2DomainNameSource = _RlDnsClv2DomainNameSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 14, 1, 1),
    _RlDnsClv2DomainNameSource_Type()
)
rlDnsClv2DomainNameSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2DomainNameSource.setStatus("current")


class _RlDnsClv2DomainNameIfIndex_Type(InterfaceIndex):
    """Custom type rlDnsClv2DomainNameIfIndex based on InterfaceIndex"""
    defaultValue = 1


_RlDnsClv2DomainNameIfIndex_Object = MibTableColumn
rlDnsClv2DomainNameIfIndex = _RlDnsClv2DomainNameIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 14, 1, 2),
    _RlDnsClv2DomainNameIfIndex_Type()
)
rlDnsClv2DomainNameIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2DomainNameIfIndex.setStatus("current")
_RlDnsClv2DomainNamePreference_Type = Integer32
_RlDnsClv2DomainNamePreference_Object = MibTableColumn
rlDnsClv2DomainNamePreference = _RlDnsClv2DomainNamePreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 14, 1, 3),
    _RlDnsClv2DomainNamePreference_Type()
)
rlDnsClv2DomainNamePreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2DomainNamePreference.setStatus("current")
_RlDnsClv2DomainNameName_Type = DnsNameAsIndex
_RlDnsClv2DomainNameName_Object = MibTableColumn
rlDnsClv2DomainNameName = _RlDnsClv2DomainNameName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 14, 1, 4),
    _RlDnsClv2DomainNameName_Type()
)
rlDnsClv2DomainNameName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2DomainNameName.setStatus("current")
_RlDnsClv2DomainNameRowStatus_Type = RowStatus
_RlDnsClv2DomainNameRowStatus_Object = MibTableColumn
rlDnsClv2DomainNameRowStatus = _RlDnsClv2DomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 14, 1, 5),
    _RlDnsClv2DomainNameRowStatus_Type()
)
rlDnsClv2DomainNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDnsClv2DomainNameRowStatus.setStatus("current")
_RlDnsClv2ServersTable_Object = MibTable
rlDnsClv2ServersTable = _RlDnsClv2ServersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15)
)
if mibBuilder.loadTexts:
    rlDnsClv2ServersTable.setStatus("current")
_RlDnsClv2ServersEntry_Object = MibTableRow
rlDnsClv2ServersEntry = _RlDnsClv2ServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15, 1)
)
rlDnsClv2ServersEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2ServersSource"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2ServersIfIndex"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2ServersPreference"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2ServersAddrType"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2ServersInetAddr"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2ServersSubTree"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2ServersClass"),
)
if mibBuilder.loadTexts:
    rlDnsClv2ServersEntry.setStatus("current")


class _RlDnsClv2ServersSource_Type(Integer32):
    """Custom type rlDnsClv2ServersSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv4", 4),
          ("dhcpv6", 3),
          ("static", 1))
    )


_RlDnsClv2ServersSource_Type.__name__ = "Integer32"
_RlDnsClv2ServersSource_Object = MibTableColumn
rlDnsClv2ServersSource = _RlDnsClv2ServersSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15, 1, 1),
    _RlDnsClv2ServersSource_Type()
)
rlDnsClv2ServersSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2ServersSource.setStatus("current")


class _RlDnsClv2ServersIfIndex_Type(InterfaceIndex):
    """Custom type rlDnsClv2ServersIfIndex based on InterfaceIndex"""
    defaultValue = 1


_RlDnsClv2ServersIfIndex_Object = MibTableColumn
rlDnsClv2ServersIfIndex = _RlDnsClv2ServersIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15, 1, 2),
    _RlDnsClv2ServersIfIndex_Type()
)
rlDnsClv2ServersIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2ServersIfIndex.setStatus("current")
_RlDnsClv2ServersPreference_Type = Integer32
_RlDnsClv2ServersPreference_Object = MibTableColumn
rlDnsClv2ServersPreference = _RlDnsClv2ServersPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15, 1, 3),
    _RlDnsClv2ServersPreference_Type()
)
rlDnsClv2ServersPreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2ServersPreference.setStatus("current")
_RlDnsClv2ServersAddrType_Type = InetAddressType
_RlDnsClv2ServersAddrType_Object = MibTableColumn
rlDnsClv2ServersAddrType = _RlDnsClv2ServersAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15, 1, 4),
    _RlDnsClv2ServersAddrType_Type()
)
rlDnsClv2ServersAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2ServersAddrType.setStatus("current")
_RlDnsClv2ServersInetAddr_Type = InetAddress
_RlDnsClv2ServersInetAddr_Object = MibTableColumn
rlDnsClv2ServersInetAddr = _RlDnsClv2ServersInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15, 1, 5),
    _RlDnsClv2ServersInetAddr_Type()
)
rlDnsClv2ServersInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2ServersInetAddr.setStatus("current")
_RlDnsClv2ServersSubTree_Type = DnsNameAsIndex
_RlDnsClv2ServersSubTree_Object = MibTableColumn
rlDnsClv2ServersSubTree = _RlDnsClv2ServersSubTree_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15, 1, 6),
    _RlDnsClv2ServersSubTree_Type()
)
rlDnsClv2ServersSubTree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2ServersSubTree.setStatus("current")
_RlDnsClv2ServersClass_Type = DnsClass
_RlDnsClv2ServersClass_Object = MibTableColumn
rlDnsClv2ServersClass = _RlDnsClv2ServersClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15, 1, 7),
    _RlDnsClv2ServersClass_Type()
)
rlDnsClv2ServersClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2ServersClass.setStatus("current")
_RlDnsClv2ServersRowStatus_Type = RowStatus
_RlDnsClv2ServersRowStatus_Object = MibTableColumn
rlDnsClv2ServersRowStatus = _RlDnsClv2ServersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 15, 1, 8),
    _RlDnsClv2ServersRowStatus_Type()
)
rlDnsClv2ServersRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDnsClv2ServersRowStatus.setStatus("current")
_RlDnsClv2FixedTable_Object = MibTable
rlDnsClv2FixedTable = _RlDnsClv2FixedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16)
)
if mibBuilder.loadTexts:
    rlDnsClv2FixedTable.setStatus("current")
_RlDnsClv2FixedEntry_Object = MibTableRow
rlDnsClv2FixedEntry = _RlDnsClv2FixedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16, 1)
)
rlDnsClv2FixedEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2FixedName"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2FixedType"),
)
if mibBuilder.loadTexts:
    rlDnsClv2FixedEntry.setStatus("current")
_RlDnsClv2FixedName_Type = DnsNameAsIndex
_RlDnsClv2FixedName_Object = MibTableColumn
rlDnsClv2FixedName = _RlDnsClv2FixedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16, 1, 1),
    _RlDnsClv2FixedName_Type()
)
rlDnsClv2FixedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2FixedName.setStatus("current")
_RlDnsClv2FixedType_Type = DnsType
_RlDnsClv2FixedType_Object = MibTableColumn
rlDnsClv2FixedType = _RlDnsClv2FixedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16, 1, 2),
    _RlDnsClv2FixedType_Type()
)
rlDnsClv2FixedType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2FixedType.setStatus("current")
_RlDnsClv2FixedPrettyName_Type = DnsName
_RlDnsClv2FixedPrettyName_Object = MibTableColumn
rlDnsClv2FixedPrettyName = _RlDnsClv2FixedPrettyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16, 1, 3),
    _RlDnsClv2FixedPrettyName_Type()
)
rlDnsClv2FixedPrettyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2FixedPrettyName.setStatus("current")


class _RlDnsClv2FixedState_Type(Integer32):
    """Custom type rlDnsClv2FixedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("polling", 5),
          ("ready", 2),
          ("refreshing", 4),
          ("resolving", 3))
    )


_RlDnsClv2FixedState_Type.__name__ = "Integer32"
_RlDnsClv2FixedState_Object = MibTableColumn
rlDnsClv2FixedState = _RlDnsClv2FixedState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16, 1, 4),
    _RlDnsClv2FixedState_Type()
)
rlDnsClv2FixedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2FixedState.setStatus("current")
_RlDnsClv2FixedCounter_Type = Integer32
_RlDnsClv2FixedCounter_Object = MibTableColumn
rlDnsClv2FixedCounter = _RlDnsClv2FixedCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16, 1, 5),
    _RlDnsClv2FixedCounter_Type()
)
rlDnsClv2FixedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2FixedCounter.setStatus("current")
_RlDnsClv2FixedTTL_Type = DnsTime
_RlDnsClv2FixedTTL_Object = MibTableColumn
rlDnsClv2FixedTTL = _RlDnsClv2FixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16, 1, 6),
    _RlDnsClv2FixedTTL_Type()
)
rlDnsClv2FixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2FixedTTL.setStatus("current")
_RlDnsClv2FixedTTRefresh_Type = DnsTime
_RlDnsClv2FixedTTRefresh_Object = MibTableColumn
rlDnsClv2FixedTTRefresh = _RlDnsClv2FixedTTRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16, 1, 7),
    _RlDnsClv2FixedTTRefresh_Type()
)
rlDnsClv2FixedTTRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2FixedTTRefresh.setStatus("current")
_RlDnsClv2FixedTTPolling_Type = DnsTime
_RlDnsClv2FixedTTPolling_Object = MibTableColumn
rlDnsClv2FixedTTPolling = _RlDnsClv2FixedTTPolling_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 16, 1, 8),
    _RlDnsClv2FixedTTPolling_Type()
)
rlDnsClv2FixedTTPolling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2FixedTTPolling.setStatus("current")


class _RlDnsClv2ClearCacheTable_Type(Integer32):
    """Custom type rlDnsClv2ClearCacheTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("dynamicOnly", 2),
          ("staticOnly", 1))
    )


_RlDnsClv2ClearCacheTable_Type.__name__ = "Integer32"
_RlDnsClv2ClearCacheTable_Object = MibScalar
rlDnsClv2ClearCacheTable = _RlDnsClv2ClearCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 17),
    _RlDnsClv2ClearCacheTable_Type()
)
rlDnsClv2ClearCacheTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClv2ClearCacheTable.setStatus("current")
_RlDnsClv2UnifiedCacheTable_Object = MibTable
rlDnsClv2UnifiedCacheTable = _RlDnsClv2UnifiedCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18)
)
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheTable.setStatus("current")
_RlDnsClv2UnifiedCacheEntry_Object = MibTableRow
rlDnsClv2UnifiedCacheEntry = _RlDnsClv2UnifiedCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1)
)
rlDnsClv2UnifiedCacheEntry.setIndexNames(
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2UnifiedCacheName"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2UnifiedCacheSource"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2UnifiedCacheState"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2UnifiedCacheType"),
    (0, "CISCOSB-DNSCL-MIB", "rlDnsClv2UnifiedCacheIndex"),
)
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheEntry.setStatus("current")
_RlDnsClv2UnifiedCacheName_Type = DnsNameAsIndex
_RlDnsClv2UnifiedCacheName_Object = MibTableColumn
rlDnsClv2UnifiedCacheName = _RlDnsClv2UnifiedCacheName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 1),
    _RlDnsClv2UnifiedCacheName_Type()
)
rlDnsClv2UnifiedCacheName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheName.setStatus("current")


class _RlDnsClv2UnifiedCacheSource_Type(Integer32):
    """Custom type rlDnsClv2UnifiedCacheSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("fixed", 3),
          ("static", 1))
    )


_RlDnsClv2UnifiedCacheSource_Type.__name__ = "Integer32"
_RlDnsClv2UnifiedCacheSource_Object = MibTableColumn
rlDnsClv2UnifiedCacheSource = _RlDnsClv2UnifiedCacheSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 2),
    _RlDnsClv2UnifiedCacheSource_Type()
)
rlDnsClv2UnifiedCacheSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheSource.setStatus("current")


class _RlDnsClv2UnifiedCacheState_Type(Integer32):
    """Custom type rlDnsClv2UnifiedCacheState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ne", 2),
          ("ok", 1),
          ("un", 3))
    )


_RlDnsClv2UnifiedCacheState_Type.__name__ = "Integer32"
_RlDnsClv2UnifiedCacheState_Object = MibTableColumn
rlDnsClv2UnifiedCacheState = _RlDnsClv2UnifiedCacheState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 3),
    _RlDnsClv2UnifiedCacheState_Type()
)
rlDnsClv2UnifiedCacheState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheState.setStatus("current")


class _RlDnsClv2UnifiedCacheType_Type(Integer32):
    """Custom type rlDnsClv2UnifiedCacheType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 2),
          ("ipv6", 1))
    )


_RlDnsClv2UnifiedCacheType_Type.__name__ = "Integer32"
_RlDnsClv2UnifiedCacheType_Object = MibTableColumn
rlDnsClv2UnifiedCacheType = _RlDnsClv2UnifiedCacheType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 4),
    _RlDnsClv2UnifiedCacheType_Type()
)
rlDnsClv2UnifiedCacheType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheType.setStatus("current")
_RlDnsClv2UnifiedCacheIndex_Type = Integer32
_RlDnsClv2UnifiedCacheIndex_Object = MibTableColumn
rlDnsClv2UnifiedCacheIndex = _RlDnsClv2UnifiedCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 5),
    _RlDnsClv2UnifiedCacheIndex_Type()
)
rlDnsClv2UnifiedCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheIndex.setStatus("current")
_RlDnsClv2UnifiedCacheInetAddrType_Type = InetAddressType
_RlDnsClv2UnifiedCacheInetAddrType_Object = MibTableColumn
rlDnsClv2UnifiedCacheInetAddrType = _RlDnsClv2UnifiedCacheInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 6),
    _RlDnsClv2UnifiedCacheInetAddrType_Type()
)
rlDnsClv2UnifiedCacheInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheInetAddrType.setStatus("current")
_RlDnsClv2UnifiedCacheInetAddr_Type = InetAddress
_RlDnsClv2UnifiedCacheInetAddr_Object = MibTableColumn
rlDnsClv2UnifiedCacheInetAddr = _RlDnsClv2UnifiedCacheInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 7),
    _RlDnsClv2UnifiedCacheInetAddr_Type()
)
rlDnsClv2UnifiedCacheInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheInetAddr.setStatus("current")
_RlDnsClv2UnifiedCacheTTL_Type = DnsTime
_RlDnsClv2UnifiedCacheTTL_Object = MibTableColumn
rlDnsClv2UnifiedCacheTTL = _RlDnsClv2UnifiedCacheTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 8),
    _RlDnsClv2UnifiedCacheTTL_Type()
)
rlDnsClv2UnifiedCacheTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheTTL.setStatus("current")
_RlDnsClv2UnifiedCacheRemainingTTL_Type = DnsTime
_RlDnsClv2UnifiedCacheRemainingTTL_Object = MibTableColumn
rlDnsClv2UnifiedCacheRemainingTTL = _RlDnsClv2UnifiedCacheRemainingTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 9),
    _RlDnsClv2UnifiedCacheRemainingTTL_Type()
)
rlDnsClv2UnifiedCacheRemainingTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCacheRemainingTTL.setStatus("current")
_RlDnsClv2UnifiedCachePrettyName_Type = DnsName
_RlDnsClv2UnifiedCachePrettyName_Object = MibTableColumn
rlDnsClv2UnifiedCachePrettyName = _RlDnsClv2UnifiedCachePrettyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93, 18, 1, 10),
    _RlDnsClv2UnifiedCachePrettyName_Type()
)
rlDnsClv2UnifiedCachePrettyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClv2UnifiedCachePrettyName.setStatus("current")
dnsResConfigSbeltEntry.registerAugmentions(
    ("CISCOSB-DNSCL-MIB",
     "rlDnsResConfigSbeltExtEntry")
)
rlDnsResConfigSbeltExtEntry.setIndexNames(*dnsResConfigSbeltEntry.getIndexNames())
rlDnsResConfigSbeltInetEntry.registerAugmentions(
    ("CISCOSB-DNSCL-MIB",
     "rlDnsResConfigSbeltExtInetEntry")
)
rlDnsResConfigSbeltExtInetEntry.setIndexNames(*rlDnsResConfigSbeltInetEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-DNSCL-MIB",
    **{"rlDnsCl": rlDnsCl,
       "rlDnsClMibVersion": rlDnsClMibVersion,
       "rlDnsClEnable": rlDnsClEnable,
       "rlDnsClDomainNameTable": rlDnsClDomainNameTable,
       "rlDnsClDomainNameEntry": rlDnsClDomainNameEntry,
       "rlDnsClDomainNameName": rlDnsClDomainNameName,
       "rlDnsClDomainNameOwner": rlDnsClDomainNameOwner,
       "rlDnsClDomainNameRowStatus": rlDnsClDomainNameRowStatus,
       "rlDnsClMaxNumOfRetransmissions": rlDnsClMaxNumOfRetransmissions,
       "rlDnsClMinRetransmissionInterval": rlDnsClMinRetransmissionInterval,
       "rlDnsClNamesTable": rlDnsClNamesTable,
       "rlDnsClNamesEntry": rlDnsClNamesEntry,
       "rlDnsClNamesName": rlDnsClNamesName,
       "rlDnsClNamesOwner": rlDnsClNamesOwner,
       "rlDnsClNamesIndex": rlDnsClNamesIndex,
       "rlDnsClNamesAddr": rlDnsClNamesAddr,
       "rlDnsClNamesRowStatus": rlDnsClNamesRowStatus,
       "rlDnsResConfigSbeltExtTable": rlDnsResConfigSbeltExtTable,
       "rlDnsResConfigSbeltExtEntry": rlDnsResConfigSbeltExtEntry,
       "rlDnsResConfigSbeltOwner": rlDnsResConfigSbeltOwner,
       "rlDnsClNamesInetTable": rlDnsClNamesInetTable,
       "rlDnsClNamesInetEntry": rlDnsClNamesInetEntry,
       "rlDnsClNamesInetName": rlDnsClNamesInetName,
       "rlDnsClNamesInetOwner": rlDnsClNamesInetOwner,
       "rlDnsClNamesInetIndex": rlDnsClNamesInetIndex,
       "rlDnsClNamesInetRRType": rlDnsClNamesInetRRType,
       "rlDnsClNamesInetAddrType": rlDnsClNamesInetAddrType,
       "rlDnsClNamesInetAddr": rlDnsClNamesInetAddr,
       "rlDnsClNamesInetRowStatus": rlDnsClNamesInetRowStatus,
       "rlDnsResConfigSbeltInetTable": rlDnsResConfigSbeltInetTable,
       "rlDnsResConfigSbeltInetEntry": rlDnsResConfigSbeltInetEntry,
       "rlDnsResConfigSbeltInetAddrType": rlDnsResConfigSbeltInetAddrType,
       "rlDnsResConfigSbeltInetAddr": rlDnsResConfigSbeltInetAddr,
       "rlDnsResConfigSbeltInetName": rlDnsResConfigSbeltInetName,
       "rlDnsResConfigSbeltInetRecursion": rlDnsResConfigSbeltInetRecursion,
       "rlDnsResConfigSbeltInetPref": rlDnsResConfigSbeltInetPref,
       "rlDnsResConfigSbeltInetSubTree": rlDnsResConfigSbeltInetSubTree,
       "rlDnsResConfigSbeltInetClass": rlDnsResConfigSbeltInetClass,
       "rlDnsResConfigSbeltInetStatus": rlDnsResConfigSbeltInetStatus,
       "rlDnsResCacheRRInetTable": rlDnsResCacheRRInetTable,
       "rlDnsResCacheRRInetEntry": rlDnsResCacheRRInetEntry,
       "rlDnsResCacheRRInetName": rlDnsResCacheRRInetName,
       "rlDnsResCacheRRInetClass": rlDnsResCacheRRInetClass,
       "rlDnsResCacheRRInetType": rlDnsResCacheRRInetType,
       "rlDnsResCacheRRInetTTL": rlDnsResCacheRRInetTTL,
       "rlDnsResCacheRRInetElapsedTTL": rlDnsResCacheRRInetElapsedTTL,
       "rlDnsResCacheRRInetSourceAddrType": rlDnsResCacheRRInetSourceAddrType,
       "rlDnsResCacheRRInetSource": rlDnsResCacheRRInetSource,
       "rlDnsResCacheRRInetData": rlDnsResCacheRRInetData,
       "rlDnsResCacheRRInetStatus": rlDnsResCacheRRInetStatus,
       "rlDnsResCacheRRInetIndex": rlDnsResCacheRRInetIndex,
       "rlDnsResCacheRRInetPrettyName": rlDnsResCacheRRInetPrettyName,
       "rlDnsResNCacheErrInetTable": rlDnsResNCacheErrInetTable,
       "rlDnsResNCacheErrInetEntry": rlDnsResNCacheErrInetEntry,
       "rlDnsResNCacheErrInetQName": rlDnsResNCacheErrInetQName,
       "rlDnsResNCacheErrInetQClass": rlDnsResNCacheErrInetQClass,
       "rlDnsResNCacheErrInetQType": rlDnsResNCacheErrInetQType,
       "rlDnsResNCacheErrInetTTL": rlDnsResNCacheErrInetTTL,
       "rlDnsResNCacheErrInetElapsedTTL": rlDnsResNCacheErrInetElapsedTTL,
       "rlDnsResNCacheErrInetSourceAddrType": rlDnsResNCacheErrInetSourceAddrType,
       "rlDnsResNCacheErrInetSource": rlDnsResNCacheErrInetSource,
       "rlDnsResNCacheErrInetCode": rlDnsResNCacheErrInetCode,
       "rlDnsResNCacheErrInetStatus": rlDnsResNCacheErrInetStatus,
       "rlDnsResNCacheErrInetIndex": rlDnsResNCacheErrInetIndex,
       "rlDnsResNCacheErrInetPrettyName": rlDnsResNCacheErrInetPrettyName,
       "rlDnsResConfigSbeltExtInetTable": rlDnsResConfigSbeltExtInetTable,
       "rlDnsResConfigSbeltExtInetEntry": rlDnsResConfigSbeltExtInetEntry,
       "rlDnsResConfigSbeltInetOwner": rlDnsResConfigSbeltInetOwner,
       "rlDnsClMinPollingInterval": rlDnsClMinPollingInterval,
       "rlDnsClv2DomainNameTable": rlDnsClv2DomainNameTable,
       "rlDnsClv2DomainNameEntry": rlDnsClv2DomainNameEntry,
       "rlDnsClv2DomainNameSource": rlDnsClv2DomainNameSource,
       "rlDnsClv2DomainNameIfIndex": rlDnsClv2DomainNameIfIndex,
       "rlDnsClv2DomainNamePreference": rlDnsClv2DomainNamePreference,
       "rlDnsClv2DomainNameName": rlDnsClv2DomainNameName,
       "rlDnsClv2DomainNameRowStatus": rlDnsClv2DomainNameRowStatus,
       "rlDnsClv2ServersTable": rlDnsClv2ServersTable,
       "rlDnsClv2ServersEntry": rlDnsClv2ServersEntry,
       "rlDnsClv2ServersSource": rlDnsClv2ServersSource,
       "rlDnsClv2ServersIfIndex": rlDnsClv2ServersIfIndex,
       "rlDnsClv2ServersPreference": rlDnsClv2ServersPreference,
       "rlDnsClv2ServersAddrType": rlDnsClv2ServersAddrType,
       "rlDnsClv2ServersInetAddr": rlDnsClv2ServersInetAddr,
       "rlDnsClv2ServersSubTree": rlDnsClv2ServersSubTree,
       "rlDnsClv2ServersClass": rlDnsClv2ServersClass,
       "rlDnsClv2ServersRowStatus": rlDnsClv2ServersRowStatus,
       "rlDnsClv2FixedTable": rlDnsClv2FixedTable,
       "rlDnsClv2FixedEntry": rlDnsClv2FixedEntry,
       "rlDnsClv2FixedName": rlDnsClv2FixedName,
       "rlDnsClv2FixedType": rlDnsClv2FixedType,
       "rlDnsClv2FixedPrettyName": rlDnsClv2FixedPrettyName,
       "rlDnsClv2FixedState": rlDnsClv2FixedState,
       "rlDnsClv2FixedCounter": rlDnsClv2FixedCounter,
       "rlDnsClv2FixedTTL": rlDnsClv2FixedTTL,
       "rlDnsClv2FixedTTRefresh": rlDnsClv2FixedTTRefresh,
       "rlDnsClv2FixedTTPolling": rlDnsClv2FixedTTPolling,
       "rlDnsClv2ClearCacheTable": rlDnsClv2ClearCacheTable,
       "rlDnsClv2UnifiedCacheTable": rlDnsClv2UnifiedCacheTable,
       "rlDnsClv2UnifiedCacheEntry": rlDnsClv2UnifiedCacheEntry,
       "rlDnsClv2UnifiedCacheName": rlDnsClv2UnifiedCacheName,
       "rlDnsClv2UnifiedCacheSource": rlDnsClv2UnifiedCacheSource,
       "rlDnsClv2UnifiedCacheState": rlDnsClv2UnifiedCacheState,
       "rlDnsClv2UnifiedCacheType": rlDnsClv2UnifiedCacheType,
       "rlDnsClv2UnifiedCacheIndex": rlDnsClv2UnifiedCacheIndex,
       "rlDnsClv2UnifiedCacheInetAddrType": rlDnsClv2UnifiedCacheInetAddrType,
       "rlDnsClv2UnifiedCacheInetAddr": rlDnsClv2UnifiedCacheInetAddr,
       "rlDnsClv2UnifiedCacheTTL": rlDnsClv2UnifiedCacheTTL,
       "rlDnsClv2UnifiedCacheRemainingTTL": rlDnsClv2UnifiedCacheRemainingTTL,
       "rlDnsClv2UnifiedCachePrettyName": rlDnsClv2UnifiedCachePrettyName}
)
