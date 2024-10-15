# SNMP MIB module (RADLAN-DNSCL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-DNSCL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:11 2024
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

(dnsResConfigSbeltEntry,) = mibBuilder.importSymbols(
    "DNS-RESOLVER-MIB",
    "dnsResConfigSbeltEntry")

(DnsName,) = mibBuilder.importSymbols(
    "DNS-SERVER-MIB",
    "DnsName")

(rlDnsCl,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rlDnsCl")

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

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDnsClMibVersion_Type = Integer32
_RlDnsClMibVersion_Object = MibScalar
rlDnsClMibVersion = _RlDnsClMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 1),
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
    (1, 3, 6, 1, 4, 1, 89, 93, 2),
    _RlDnsClEnable_Type()
)
rlDnsClEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClEnable.setStatus("current")
_RlDnsClDomainNameTable_Object = MibTable
rlDnsClDomainNameTable = _RlDnsClDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 3)
)
if mibBuilder.loadTexts:
    rlDnsClDomainNameTable.setStatus("current")
_RlDnsClDomainNameEntry_Object = MibTableRow
rlDnsClDomainNameEntry = _RlDnsClDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 3, 1)
)
rlDnsClDomainNameEntry.setIndexNames(
    (0, "RADLAN-DNSCL-MIB", "rlDnsClDomainNameName"),
)
if mibBuilder.loadTexts:
    rlDnsClDomainNameEntry.setStatus("current")
_RlDnsClDomainNameName_Type = DnsName
_RlDnsClDomainNameName_Object = MibTableColumn
rlDnsClDomainNameName = _RlDnsClDomainNameName_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 1),
    _RlDnsClDomainNameName_Type()
)
rlDnsClDomainNameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClDomainNameName.setStatus("current")


class _RlDnsClDomainNameOwner_Type(Integer32):
    """Custom type rlDnsClDomainNameOwner based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("static", 1))
    )


_RlDnsClDomainNameOwner_Type.__name__ = "Integer32"
_RlDnsClDomainNameOwner_Object = MibTableColumn
rlDnsClDomainNameOwner = _RlDnsClDomainNameOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 2),
    _RlDnsClDomainNameOwner_Type()
)
rlDnsClDomainNameOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClDomainNameOwner.setStatus("current")
_RlDnsClDomainNameRowStatus_Type = RowStatus
_RlDnsClDomainNameRowStatus_Object = MibTableColumn
rlDnsClDomainNameRowStatus = _RlDnsClDomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 3),
    _RlDnsClDomainNameRowStatus_Type()
)
rlDnsClDomainNameRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClDomainNameRowStatus.setStatus("current")


class _RlDnsClMaxNumOfRetransmissions_Type(Integer32):
    """Custom type rlDnsClMaxNumOfRetransmissions based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RlDnsClMaxNumOfRetransmissions_Type.__name__ = "Integer32"
_RlDnsClMaxNumOfRetransmissions_Object = MibScalar
rlDnsClMaxNumOfRetransmissions = _RlDnsClMaxNumOfRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 4),
    _RlDnsClMaxNumOfRetransmissions_Type()
)
rlDnsClMaxNumOfRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClMaxNumOfRetransmissions.setStatus("current")


class _RlDnsClMinRetransmissionInterval_Type(Integer32):
    """Custom type rlDnsClMinRetransmissionInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlDnsClMinRetransmissionInterval_Type.__name__ = "Integer32"
_RlDnsClMinRetransmissionInterval_Object = MibScalar
rlDnsClMinRetransmissionInterval = _RlDnsClMinRetransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 5),
    _RlDnsClMinRetransmissionInterval_Type()
)
rlDnsClMinRetransmissionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClMinRetransmissionInterval.setStatus("current")
_RlDnsClNamesTable_Object = MibTable
rlDnsClNamesTable = _RlDnsClNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 6)
)
if mibBuilder.loadTexts:
    rlDnsClNamesTable.setStatus("current")
_RlDnsClNamesEntry_Object = MibTableRow
rlDnsClNamesEntry = _RlDnsClNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 6, 1)
)
rlDnsClNamesEntry.setIndexNames(
    (0, "RADLAN-DNSCL-MIB", "rlDnsClNamesName"),
    (0, "RADLAN-DNSCL-MIB", "rlDnsClNamesOwner"),
    (0, "RADLAN-DNSCL-MIB", "rlDnsClNamesIndex"),
)
if mibBuilder.loadTexts:
    rlDnsClNamesEntry.setStatus("current")
_RlDnsClNamesName_Type = DnsName
_RlDnsClNamesName_Object = MibTableColumn
rlDnsClNamesName = _RlDnsClNamesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 1),
    _RlDnsClNamesName_Type()
)
rlDnsClNamesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDnsClNamesName.setStatus("current")


class _RlDnsClNamesOwner_Type(Integer32):
    """Custom type rlDnsClNamesOwner based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("static", 1))
    )


_RlDnsClNamesOwner_Type.__name__ = "Integer32"
_RlDnsClNamesOwner_Object = MibTableColumn
rlDnsClNamesOwner = _RlDnsClNamesOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 2),
    _RlDnsClNamesOwner_Type()
)
rlDnsClNamesOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClNamesOwner.setStatus("current")
_RlDnsClNamesIndex_Type = Integer32
_RlDnsClNamesIndex_Object = MibTableColumn
rlDnsClNamesIndex = _RlDnsClNamesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 3),
    _RlDnsClNamesIndex_Type()
)
rlDnsClNamesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDnsClNamesIndex.setStatus("current")
_RlDnsClNamesAddr_Type = IpAddress
_RlDnsClNamesAddr_Object = MibTableColumn
rlDnsClNamesAddr = _RlDnsClNamesAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 4),
    _RlDnsClNamesAddr_Type()
)
rlDnsClNamesAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClNamesAddr.setStatus("current")
_RlDnsClNamesRowStatus_Type = RowStatus
_RlDnsClNamesRowStatus_Object = MibTableColumn
rlDnsClNamesRowStatus = _RlDnsClNamesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 5),
    _RlDnsClNamesRowStatus_Type()
)
rlDnsClNamesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDnsClNamesRowStatus.setStatus("current")
_DnsResConfigSbeltExtTable_Object = MibTable
dnsResConfigSbeltExtTable = _DnsResConfigSbeltExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 7)
)
if mibBuilder.loadTexts:
    dnsResConfigSbeltExtTable.setStatus("current")
_DnsResConfigSbeltExtEntry_Object = MibTableRow
dnsResConfigSbeltExtEntry = _DnsResConfigSbeltExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 7, 1)
)
if mibBuilder.loadTexts:
    dnsResConfigSbeltExtEntry.setStatus("current")


class _DnsResConfigSbeltOwner_Type(Integer32):
    """Custom type dnsResConfigSbeltOwner based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("static", 1))
    )


_DnsResConfigSbeltOwner_Type.__name__ = "Integer32"
_DnsResConfigSbeltOwner_Object = MibTableColumn
dnsResConfigSbeltOwner = _DnsResConfigSbeltOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 93, 7, 1, 1),
    _DnsResConfigSbeltOwner_Type()
)
dnsResConfigSbeltOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResConfigSbeltOwner.setStatus("current")
dnsResConfigSbeltEntry.registerAugmentions(
    ("RADLAN-DNSCL-MIB",
     "dnsResConfigSbeltExtEntry")
)
dnsResConfigSbeltExtEntry.setIndexNames(*dnsResConfigSbeltEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-DNSCL-MIB",
    **{"rlDnsClMibVersion": rlDnsClMibVersion,
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
       "dnsResConfigSbeltExtTable": dnsResConfigSbeltExtTable,
       "dnsResConfigSbeltExtEntry": dnsResConfigSbeltExtEntry,
       "dnsResConfigSbeltOwner": dnsResConfigSbeltOwner}
)
