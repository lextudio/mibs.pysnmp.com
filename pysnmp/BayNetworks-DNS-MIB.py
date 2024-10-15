# SNMP MIB module (BayNetworks-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BayNetworks-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:19 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfDnsGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDnsGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDns_ObjectIdentity = ObjectIdentity
wfDns = _WfDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1)
)


class _WfDnsDelete_Type(Integer32):
    """Custom type wfDnsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDnsDelete_Type.__name__ = "Integer32"
_WfDnsDelete_Object = MibScalar
wfDnsDelete = _WfDnsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 1),
    _WfDnsDelete_Type()
)
wfDnsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsDelete.setStatus("mandatory")


class _WfDnsDisable_Type(Integer32):
    """Custom type wfDnsDisable based on Integer32"""
    defaultValue = 1

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


_WfDnsDisable_Type.__name__ = "Integer32"
_WfDnsDisable_Object = MibScalar
wfDnsDisable = _WfDnsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 2),
    _WfDnsDisable_Type()
)
wfDnsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsDisable.setStatus("mandatory")


class _WfDnsTimeOut_Type(Integer32):
    """Custom type wfDnsTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfDnsTimeOut_Type.__name__ = "Integer32"
_WfDnsTimeOut_Object = MibScalar
wfDnsTimeOut = _WfDnsTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 3),
    _WfDnsTimeOut_Type()
)
wfDnsTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsTimeOut.setStatus("mandatory")


class _WfDnsRexmit_Type(Integer32):
    """Custom type wfDnsRexmit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfDnsRexmit_Type.__name__ = "Integer32"
_WfDnsRexmit_Object = MibScalar
wfDnsRexmit = _WfDnsRexmit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 4),
    _WfDnsRexmit_Type()
)
wfDnsRexmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsRexmit.setStatus("mandatory")


class _WfDnsMaxAllow_Type(Integer32):
    """Custom type wfDnsMaxAllow based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfDnsMaxAllow_Type.__name__ = "Integer32"
_WfDnsMaxAllow_Object = MibScalar
wfDnsMaxAllow = _WfDnsMaxAllow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 5),
    _WfDnsMaxAllow_Type()
)
wfDnsMaxAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsMaxAllow.setStatus("mandatory")


class _WfDnsIpTos_Type(Integer32):
    """Custom type wfDnsIpTos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowdelay", 2),
          ("normal", 1))
    )


_WfDnsIpTos_Type.__name__ = "Integer32"
_WfDnsIpTos_Object = MibScalar
wfDnsIpTos = _WfDnsIpTos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 6),
    _WfDnsIpTos_Type()
)
wfDnsIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsIpTos.setStatus("obsolete")
_WfDnsDomainName_Type = DisplayString
_WfDnsDomainName_Object = MibScalar
wfDnsDomainName = _WfDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 7),
    _WfDnsDomainName_Type()
)
wfDnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsDomainName.setStatus("mandatory")


class _WfDnsRecursion_Type(Integer32):
    """Custom type wfDnsRecursion based on Integer32"""
    defaultValue = 1

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


_WfDnsRecursion_Type.__name__ = "Integer32"
_WfDnsRecursion_Object = MibScalar
wfDnsRecursion = _WfDnsRecursion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 8),
    _WfDnsRecursion_Type()
)
wfDnsRecursion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsRecursion.setStatus("mandatory")


class _WfDnsTruncation_Type(Integer32):
    """Custom type wfDnsTruncation based on Integer32"""
    defaultValue = 1

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


_WfDnsTruncation_Type.__name__ = "Integer32"
_WfDnsTruncation_Object = MibScalar
wfDnsTruncation = _WfDnsTruncation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 9),
    _WfDnsTruncation_Type()
)
wfDnsTruncation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsTruncation.setStatus("mandatory")


class _WfDnsAuthOnly_Type(Integer32):
    """Custom type wfDnsAuthOnly based on Integer32"""
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


_WfDnsAuthOnly_Type.__name__ = "Integer32"
_WfDnsAuthOnly_Object = MibScalar
wfDnsAuthOnly = _WfDnsAuthOnly_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 10),
    _WfDnsAuthOnly_Type()
)
wfDnsAuthOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsAuthOnly.setStatus("mandatory")


class _WfDnsDefDomain_Type(Integer32):
    """Custom type wfDnsDefDomain based on Integer32"""
    defaultValue = 1

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


_WfDnsDefDomain_Type.__name__ = "Integer32"
_WfDnsDefDomain_Object = MibScalar
wfDnsDefDomain = _WfDnsDefDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 11),
    _WfDnsDefDomain_Type()
)
wfDnsDefDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsDefDomain.setStatus("mandatory")
_WfDnsQueries_Type = Counter32
_WfDnsQueries_Object = MibScalar
wfDnsQueries = _WfDnsQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 12),
    _WfDnsQueries_Type()
)
wfDnsQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsQueries.setStatus("mandatory")
_WfDnsResps_Type = Counter32
_WfDnsResps_Object = MibScalar
wfDnsResps = _WfDnsResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 13),
    _WfDnsResps_Type()
)
wfDnsResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsResps.setStatus("mandatory")
_WfDnsNonAuthResps_Type = Counter32
_WfDnsNonAuthResps_Object = MibScalar
wfDnsNonAuthResps = _WfDnsNonAuthResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 14),
    _WfDnsNonAuthResps_Type()
)
wfDnsNonAuthResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsNonAuthResps.setStatus("mandatory")
_WfDnsNoData_Type = Counter32
_WfDnsNoData_Object = MibScalar
wfDnsNoData = _WfDnsNoData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 15),
    _WfDnsNoData_Type()
)
wfDnsNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsNoData.setStatus("mandatory")
_WfDnsMartians_Type = Counter32
_WfDnsMartians_Object = MibScalar
wfDnsMartians = _WfDnsMartians_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 16),
    _WfDnsMartians_Type()
)
wfDnsMartians.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsMartians.setStatus("mandatory")
_WfDnsUnParseResps_Type = Counter32
_WfDnsUnParseResps_Object = MibScalar
wfDnsUnParseResps = _WfDnsUnParseResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 17),
    _WfDnsUnParseResps_Type()
)
wfDnsUnParseResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsUnParseResps.setStatus("mandatory")
_WfDnsRexmitPkts_Type = Counter32
_WfDnsRexmitPkts_Object = MibScalar
wfDnsRexmitPkts = _WfDnsRexmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 18),
    _WfDnsRexmitPkts_Type()
)
wfDnsRexmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsRexmitPkts.setStatus("mandatory")
_WfDnsTimeOuts_Type = Counter32
_WfDnsTimeOuts_Object = MibScalar
wfDnsTimeOuts = _WfDnsTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 19),
    _WfDnsTimeOuts_Type()
)
wfDnsTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsTimeOuts.setStatus("mandatory")
_WfDnsHostsFile_Type = DisplayString
_WfDnsHostsFile_Object = MibScalar
wfDnsHostsFile = _WfDnsHostsFile_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 20),
    _WfDnsHostsFile_Type()
)
wfDnsHostsFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsHostsFile.setStatus("mandatory")
_WfDnsRcvdError_Type = Counter32
_WfDnsRcvdError_Object = MibScalar
wfDnsRcvdError = _WfDnsRcvdError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 21),
    _WfDnsRcvdError_Type()
)
wfDnsRcvdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsRcvdError.setStatus("mandatory")
_WfDnsLocalError_Type = Counter32
_WfDnsLocalError_Object = MibScalar
wfDnsLocalError = _WfDnsLocalError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 1, 22),
    _WfDnsLocalError_Type()
)
wfDnsLocalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsLocalError.setStatus("mandatory")
_WfDnsServerTable_Object = MibTable
wfDnsServerTable = _WfDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 2)
)
if mibBuilder.loadTexts:
    wfDnsServerTable.setStatus("mandatory")
_WfDnsServerEntry_Object = MibTableRow
wfDnsServerEntry = _WfDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 2, 1)
)
wfDnsServerEntry.setIndexNames(
    (0, "BayNetworks-DNS-MIB", "wfDnsServerIndex"),
)
if mibBuilder.loadTexts:
    wfDnsServerEntry.setStatus("mandatory")


class _WfDnsServerDelete_Type(Integer32):
    """Custom type wfDnsServerDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDnsServerDelete_Type.__name__ = "Integer32"
_WfDnsServerDelete_Object = MibTableColumn
wfDnsServerDelete = _WfDnsServerDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 2, 1, 1),
    _WfDnsServerDelete_Type()
)
wfDnsServerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsServerDelete.setStatus("mandatory")
_WfDnsServerIndex_Type = Integer32
_WfDnsServerIndex_Object = MibTableColumn
wfDnsServerIndex = _WfDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 2, 1, 2),
    _WfDnsServerIndex_Type()
)
wfDnsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsServerIndex.setStatus("mandatory")
_WfDnsServerAddr_Type = IpAddress
_WfDnsServerAddr_Object = MibTableColumn
wfDnsServerAddr = _WfDnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 2, 1, 3),
    _WfDnsServerAddr_Type()
)
wfDnsServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsServerAddr.setStatus("mandatory")


class _WfDnsServerPortNo_Type(Integer32):
    """Custom type wfDnsServerPortNo based on Integer32"""
    defaultValue = 53


_WfDnsServerPortNo_Object = MibTableColumn
wfDnsServerPortNo = _WfDnsServerPortNo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 2, 1, 4),
    _WfDnsServerPortNo_Type()
)
wfDnsServerPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsServerPortNo.setStatus("mandatory")
_WfDnsProxyIntfTable_Object = MibTable
wfDnsProxyIntfTable = _WfDnsProxyIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3)
)
if mibBuilder.loadTexts:
    wfDnsProxyIntfTable.setStatus("mandatory")
_WfDnsProxyIntfEntry_Object = MibTableRow
wfDnsProxyIntfEntry = _WfDnsProxyIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1)
)
wfDnsProxyIntfEntry.setIndexNames(
    (0, "BayNetworks-DNS-MIB", "wfDnsProxyIntfAddress"),
)
if mibBuilder.loadTexts:
    wfDnsProxyIntfEntry.setStatus("mandatory")


class _WfDnsProxyIntfDelete_Type(Integer32):
    """Custom type wfDnsProxyIntfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDnsProxyIntfDelete_Type.__name__ = "Integer32"
_WfDnsProxyIntfDelete_Object = MibTableColumn
wfDnsProxyIntfDelete = _WfDnsProxyIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 1),
    _WfDnsProxyIntfDelete_Type()
)
wfDnsProxyIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfDelete.setStatus("mandatory")


class _WfDnsProxyIntfDisable_Type(Integer32):
    """Custom type wfDnsProxyIntfDisable based on Integer32"""
    defaultValue = 1

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


_WfDnsProxyIntfDisable_Type.__name__ = "Integer32"
_WfDnsProxyIntfDisable_Object = MibTableColumn
wfDnsProxyIntfDisable = _WfDnsProxyIntfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 2),
    _WfDnsProxyIntfDisable_Type()
)
wfDnsProxyIntfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfDisable.setStatus("mandatory")


class _WfDnsProxyIntfState_Type(Integer32):
    """Custom type wfDnsProxyIntfState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("invalid", 4),
          ("notpres", 5),
          ("up", 1))
    )


_WfDnsProxyIntfState_Type.__name__ = "Integer32"
_WfDnsProxyIntfState_Object = MibTableColumn
wfDnsProxyIntfState = _WfDnsProxyIntfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 3),
    _WfDnsProxyIntfState_Type()
)
wfDnsProxyIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfState.setStatus("mandatory")
_WfDnsProxyIntfAddress_Type = IpAddress
_WfDnsProxyIntfAddress_Object = MibTableColumn
wfDnsProxyIntfAddress = _WfDnsProxyIntfAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 4),
    _WfDnsProxyIntfAddress_Type()
)
wfDnsProxyIntfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfAddress.setStatus("mandatory")


class _WfDnsProxyIntfPortNo_Type(Integer32):
    """Custom type wfDnsProxyIntfPortNo based on Integer32"""
    defaultValue = 53


_WfDnsProxyIntfPortNo_Object = MibTableColumn
wfDnsProxyIntfPortNo = _WfDnsProxyIntfPortNo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 5),
    _WfDnsProxyIntfPortNo_Type()
)
wfDnsProxyIntfPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfPortNo.setStatus("mandatory")


class _WfDnsProxyIntfMode_Type(Integer32):
    """Custom type wfDnsProxyIntfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nat-translation", 2),
          ("pass-thru", 1))
    )


_WfDnsProxyIntfMode_Type.__name__ = "Integer32"
_WfDnsProxyIntfMode_Object = MibTableColumn
wfDnsProxyIntfMode = _WfDnsProxyIntfMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 6),
    _WfDnsProxyIntfMode_Type()
)
wfDnsProxyIntfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfMode.setStatus("mandatory")
_WfDnsProxyIntfDomain_Type = DisplayString
_WfDnsProxyIntfDomain_Object = MibTableColumn
wfDnsProxyIntfDomain = _WfDnsProxyIntfDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 7),
    _WfDnsProxyIntfDomain_Type()
)
wfDnsProxyIntfDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfDomain.setStatus("mandatory")
_WfDnsProxyIntfFwdServer1_Type = IpAddress
_WfDnsProxyIntfFwdServer1_Object = MibTableColumn
wfDnsProxyIntfFwdServer1 = _WfDnsProxyIntfFwdServer1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 8),
    _WfDnsProxyIntfFwdServer1_Type()
)
wfDnsProxyIntfFwdServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfFwdServer1.setStatus("mandatory")
_WfDnsProxyIntfFwdServer2_Type = IpAddress
_WfDnsProxyIntfFwdServer2_Object = MibTableColumn
wfDnsProxyIntfFwdServer2 = _WfDnsProxyIntfFwdServer2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 9),
    _WfDnsProxyIntfFwdServer2_Type()
)
wfDnsProxyIntfFwdServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfFwdServer2.setStatus("mandatory")
_WfDnsProxyIntfFwdServer3_Type = IpAddress
_WfDnsProxyIntfFwdServer3_Object = MibTableColumn
wfDnsProxyIntfFwdServer3 = _WfDnsProxyIntfFwdServer3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 10),
    _WfDnsProxyIntfFwdServer3_Type()
)
wfDnsProxyIntfFwdServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfFwdServer3.setStatus("mandatory")


class _WfDnsProxyIntfFwdServerPortNo_Type(Integer32):
    """Custom type wfDnsProxyIntfFwdServerPortNo based on Integer32"""
    defaultValue = 53


_WfDnsProxyIntfFwdServerPortNo_Object = MibTableColumn
wfDnsProxyIntfFwdServerPortNo = _WfDnsProxyIntfFwdServerPortNo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 11),
    _WfDnsProxyIntfFwdServerPortNo_Type()
)
wfDnsProxyIntfFwdServerPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfFwdServerPortNo.setStatus("mandatory")


class _WfDnsProxyIntfTimeOut_Type(Integer32):
    """Custom type wfDnsProxyIntfTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfDnsProxyIntfTimeOut_Type.__name__ = "Integer32"
_WfDnsProxyIntfTimeOut_Object = MibTableColumn
wfDnsProxyIntfTimeOut = _WfDnsProxyIntfTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 12),
    _WfDnsProxyIntfTimeOut_Type()
)
wfDnsProxyIntfTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfTimeOut.setStatus("mandatory")


class _WfDnsProxyIntfRexmit_Type(Integer32):
    """Custom type wfDnsProxyIntfRexmit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfDnsProxyIntfRexmit_Type.__name__ = "Integer32"
_WfDnsProxyIntfRexmit_Object = MibTableColumn
wfDnsProxyIntfRexmit = _WfDnsProxyIntfRexmit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 13),
    _WfDnsProxyIntfRexmit_Type()
)
wfDnsProxyIntfRexmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfRexmit.setStatus("mandatory")


class _WfDnsProxyIntfMaxAllow_Type(Integer32):
    """Custom type wfDnsProxyIntfMaxAllow based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfDnsProxyIntfMaxAllow_Type.__name__ = "Integer32"
_WfDnsProxyIntfMaxAllow_Object = MibTableColumn
wfDnsProxyIntfMaxAllow = _WfDnsProxyIntfMaxAllow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 14),
    _WfDnsProxyIntfMaxAllow_Type()
)
wfDnsProxyIntfMaxAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfMaxAllow.setStatus("mandatory")


class _WfDnsProxyIntfTruncDnsAnswer_Type(Integer32):
    """Custom type wfDnsProxyIntfTruncDnsAnswer based on Integer32"""
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


_WfDnsProxyIntfTruncDnsAnswer_Type.__name__ = "Integer32"
_WfDnsProxyIntfTruncDnsAnswer_Object = MibTableColumn
wfDnsProxyIntfTruncDnsAnswer = _WfDnsProxyIntfTruncDnsAnswer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 15),
    _WfDnsProxyIntfTruncDnsAnswer_Type()
)
wfDnsProxyIntfTruncDnsAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfTruncDnsAnswer.setStatus("mandatory")


class _WfDnsProxyIntfTruncMaxNo_Type(Integer32):
    """Custom type wfDnsProxyIntfTruncMaxNo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfDnsProxyIntfTruncMaxNo_Type.__name__ = "Integer32"
_WfDnsProxyIntfTruncMaxNo_Object = MibTableColumn
wfDnsProxyIntfTruncMaxNo = _WfDnsProxyIntfTruncMaxNo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 16),
    _WfDnsProxyIntfTruncMaxNo_Type()
)
wfDnsProxyIntfTruncMaxNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfTruncMaxNo.setStatus("mandatory")


class _WfDnsProxyIntfCacheSize_Type(Integer32):
    """Custom type wfDnsProxyIntfCacheSize based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfDnsProxyIntfCacheSize_Type.__name__ = "Integer32"
_WfDnsProxyIntfCacheSize_Object = MibTableColumn
wfDnsProxyIntfCacheSize = _WfDnsProxyIntfCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 17),
    _WfDnsProxyIntfCacheSize_Type()
)
wfDnsProxyIntfCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDnsProxyIntfCacheSize.setStatus("mandatory")
_WfDnsProxyIntfForward_Type = Counter32
_WfDnsProxyIntfForward_Object = MibTableColumn
wfDnsProxyIntfForward = _WfDnsProxyIntfForward_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 18),
    _WfDnsProxyIntfForward_Type()
)
wfDnsProxyIntfForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfForward.setStatus("mandatory")
_WfDnsProxyIntfResps_Type = Counter32
_WfDnsProxyIntfResps_Object = MibTableColumn
wfDnsProxyIntfResps = _WfDnsProxyIntfResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 19),
    _WfDnsProxyIntfResps_Type()
)
wfDnsProxyIntfResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfResps.setStatus("mandatory")
_WfDnsProxyIntfDropped_Type = Counter32
_WfDnsProxyIntfDropped_Object = MibTableColumn
wfDnsProxyIntfDropped = _WfDnsProxyIntfDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 20),
    _WfDnsProxyIntfDropped_Type()
)
wfDnsProxyIntfDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfDropped.setStatus("mandatory")
_WfDnsProxyIntfMartians_Type = Counter32
_WfDnsProxyIntfMartians_Object = MibTableColumn
wfDnsProxyIntfMartians = _WfDnsProxyIntfMartians_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 21),
    _WfDnsProxyIntfMartians_Type()
)
wfDnsProxyIntfMartians.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfMartians.setStatus("mandatory")
_WfDnsProxyIntfUnParseResps_Type = Counter32
_WfDnsProxyIntfUnParseResps_Object = MibTableColumn
wfDnsProxyIntfUnParseResps = _WfDnsProxyIntfUnParseResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 22),
    _WfDnsProxyIntfUnParseResps_Type()
)
wfDnsProxyIntfUnParseResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfUnParseResps.setStatus("mandatory")
_WfDnsProxyIntfRexmitPkts_Type = Counter32
_WfDnsProxyIntfRexmitPkts_Object = MibTableColumn
wfDnsProxyIntfRexmitPkts = _WfDnsProxyIntfRexmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 23),
    _WfDnsProxyIntfRexmitPkts_Type()
)
wfDnsProxyIntfRexmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfRexmitPkts.setStatus("mandatory")
_WfDnsProxyIntfTimeOuts_Type = Counter32
_WfDnsProxyIntfTimeOuts_Object = MibTableColumn
wfDnsProxyIntfTimeOuts = _WfDnsProxyIntfTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 24),
    _WfDnsProxyIntfTimeOuts_Type()
)
wfDnsProxyIntfTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfTimeOuts.setStatus("mandatory")
_WfDnsProxyIntfLocalError_Type = Counter32
_WfDnsProxyIntfLocalError_Object = MibTableColumn
wfDnsProxyIntfLocalError = _WfDnsProxyIntfLocalError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 25),
    _WfDnsProxyIntfLocalError_Type()
)
wfDnsProxyIntfLocalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfLocalError.setStatus("mandatory")
_WfDnsProxyIntfCacheHits_Type = Counter32
_WfDnsProxyIntfCacheHits_Object = MibTableColumn
wfDnsProxyIntfCacheHits = _WfDnsProxyIntfCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19, 3, 1, 26),
    _WfDnsProxyIntfCacheHits_Type()
)
wfDnsProxyIntfCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDnsProxyIntfCacheHits.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BayNetworks-DNS-MIB",
    **{"wfDns": wfDns,
       "wfDnsDelete": wfDnsDelete,
       "wfDnsDisable": wfDnsDisable,
       "wfDnsTimeOut": wfDnsTimeOut,
       "wfDnsRexmit": wfDnsRexmit,
       "wfDnsMaxAllow": wfDnsMaxAllow,
       "wfDnsIpTos": wfDnsIpTos,
       "wfDnsDomainName": wfDnsDomainName,
       "wfDnsRecursion": wfDnsRecursion,
       "wfDnsTruncation": wfDnsTruncation,
       "wfDnsAuthOnly": wfDnsAuthOnly,
       "wfDnsDefDomain": wfDnsDefDomain,
       "wfDnsQueries": wfDnsQueries,
       "wfDnsResps": wfDnsResps,
       "wfDnsNonAuthResps": wfDnsNonAuthResps,
       "wfDnsNoData": wfDnsNoData,
       "wfDnsMartians": wfDnsMartians,
       "wfDnsUnParseResps": wfDnsUnParseResps,
       "wfDnsRexmitPkts": wfDnsRexmitPkts,
       "wfDnsTimeOuts": wfDnsTimeOuts,
       "wfDnsHostsFile": wfDnsHostsFile,
       "wfDnsRcvdError": wfDnsRcvdError,
       "wfDnsLocalError": wfDnsLocalError,
       "wfDnsServerTable": wfDnsServerTable,
       "wfDnsServerEntry": wfDnsServerEntry,
       "wfDnsServerDelete": wfDnsServerDelete,
       "wfDnsServerIndex": wfDnsServerIndex,
       "wfDnsServerAddr": wfDnsServerAddr,
       "wfDnsServerPortNo": wfDnsServerPortNo,
       "wfDnsProxyIntfTable": wfDnsProxyIntfTable,
       "wfDnsProxyIntfEntry": wfDnsProxyIntfEntry,
       "wfDnsProxyIntfDelete": wfDnsProxyIntfDelete,
       "wfDnsProxyIntfDisable": wfDnsProxyIntfDisable,
       "wfDnsProxyIntfState": wfDnsProxyIntfState,
       "wfDnsProxyIntfAddress": wfDnsProxyIntfAddress,
       "wfDnsProxyIntfPortNo": wfDnsProxyIntfPortNo,
       "wfDnsProxyIntfMode": wfDnsProxyIntfMode,
       "wfDnsProxyIntfDomain": wfDnsProxyIntfDomain,
       "wfDnsProxyIntfFwdServer1": wfDnsProxyIntfFwdServer1,
       "wfDnsProxyIntfFwdServer2": wfDnsProxyIntfFwdServer2,
       "wfDnsProxyIntfFwdServer3": wfDnsProxyIntfFwdServer3,
       "wfDnsProxyIntfFwdServerPortNo": wfDnsProxyIntfFwdServerPortNo,
       "wfDnsProxyIntfTimeOut": wfDnsProxyIntfTimeOut,
       "wfDnsProxyIntfRexmit": wfDnsProxyIntfRexmit,
       "wfDnsProxyIntfMaxAllow": wfDnsProxyIntfMaxAllow,
       "wfDnsProxyIntfTruncDnsAnswer": wfDnsProxyIntfTruncDnsAnswer,
       "wfDnsProxyIntfTruncMaxNo": wfDnsProxyIntfTruncMaxNo,
       "wfDnsProxyIntfCacheSize": wfDnsProxyIntfCacheSize,
       "wfDnsProxyIntfForward": wfDnsProxyIntfForward,
       "wfDnsProxyIntfResps": wfDnsProxyIntfResps,
       "wfDnsProxyIntfDropped": wfDnsProxyIntfDropped,
       "wfDnsProxyIntfMartians": wfDnsProxyIntfMartians,
       "wfDnsProxyIntfUnParseResps": wfDnsProxyIntfUnParseResps,
       "wfDnsProxyIntfRexmitPkts": wfDnsProxyIntfRexmitPkts,
       "wfDnsProxyIntfTimeOuts": wfDnsProxyIntfTimeOuts,
       "wfDnsProxyIntfLocalError": wfDnsProxyIntfLocalError,
       "wfDnsProxyIntfCacheHits": wfDnsProxyIntfCacheHits}
)
