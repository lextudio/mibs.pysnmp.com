# SNMP MIB module (MITEL-DNSGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-DNSGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:16 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mitelIpGrpDnsGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3)
)
mitelIpGrpDnsGroup.setRevisions(
        ("2003-03-21 03:18",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelRouterIpGroup_ObjectIdentity = ObjectIdentity
mitelRouterIpGroup = _MitelRouterIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1)
)


class _MitelDnsGrpDomainName_Type(DisplayString):
    """Custom type mitelDnsGrpDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MitelDnsGrpDomainName_Type.__name__ = "DisplayString"
_MitelDnsGrpDomainName_Object = MibScalar
mitelDnsGrpDomainName = _MitelDnsGrpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 1),
    _MitelDnsGrpDomainName_Type()
)
mitelDnsGrpDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsGrpDomainName.setStatus("current")
_MitelDnsGrpPrimaryDns_Type = IpAddress
_MitelDnsGrpPrimaryDns_Object = MibScalar
mitelDnsGrpPrimaryDns = _MitelDnsGrpPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 2),
    _MitelDnsGrpPrimaryDns_Type()
)
mitelDnsGrpPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsGrpPrimaryDns.setStatus("current")
_MitelDnsGrpSecondaryDns_Type = IpAddress
_MitelDnsGrpSecondaryDns_Object = MibScalar
mitelDnsGrpSecondaryDns = _MitelDnsGrpSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 3),
    _MitelDnsGrpSecondaryDns_Type()
)
mitelDnsGrpSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsGrpSecondaryDns.setStatus("current")


class _MitelDnsGrpQueryOrder_Type(Integer32):
    """Custom type mitelDnsGrpQueryOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dns-first", 2),
          ("dns-only", 3),
          ("local-first", 1))
    )


_MitelDnsGrpQueryOrder_Type.__name__ = "Integer32"
_MitelDnsGrpQueryOrder_Object = MibScalar
mitelDnsGrpQueryOrder = _MitelDnsGrpQueryOrder_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 4),
    _MitelDnsGrpQueryOrder_Type()
)
mitelDnsGrpQueryOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsGrpQueryOrder.setStatus("current")
_MitelDnsGrpAnswerTtl_Type = Integer32
_MitelDnsGrpAnswerTtl_Object = MibScalar
mitelDnsGrpAnswerTtl = _MitelDnsGrpAnswerTtl_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 5),
    _MitelDnsGrpAnswerTtl_Type()
)
mitelDnsGrpAnswerTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsGrpAnswerTtl.setStatus("current")
_MitelDnsGrpDnsPort_Type = Integer32
_MitelDnsGrpDnsPort_Object = MibScalar
mitelDnsGrpDnsPort = _MitelDnsGrpDnsPort_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 6),
    _MitelDnsGrpDnsPort_Type()
)
mitelDnsGrpDnsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsGrpDnsPort.setStatus("current")


class _MitelDnsGrpFilterEnabled_Type(Integer32):
    """Custom type mitelDnsGrpFilterEnabled based on Integer32"""
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


_MitelDnsGrpFilterEnabled_Type.__name__ = "Integer32"
_MitelDnsGrpFilterEnabled_Object = MibScalar
mitelDnsGrpFilterEnabled = _MitelDnsGrpFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 7),
    _MitelDnsGrpFilterEnabled_Type()
)
mitelDnsGrpFilterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsGrpFilterEnabled.setStatus("current")
_MitelDnsGrpDnsStatistics_ObjectIdentity = ObjectIdentity
mitelDnsGrpDnsStatistics = _MitelDnsGrpDnsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9)
)
_MitelDnsStatsQueryTotal_Type = Integer32
_MitelDnsStatsQueryTotal_Object = MibScalar
mitelDnsStatsQueryTotal = _MitelDnsStatsQueryTotal_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 1),
    _MitelDnsStatsQueryTotal_Type()
)
mitelDnsStatsQueryTotal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsStatsQueryTotal.setStatus("current")
_MitelDnsStatsQueryFiltered_Type = Integer32
_MitelDnsStatsQueryFiltered_Object = MibScalar
mitelDnsStatsQueryFiltered = _MitelDnsStatsQueryFiltered_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 2),
    _MitelDnsStatsQueryFiltered_Type()
)
mitelDnsStatsQueryFiltered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsStatsQueryFiltered.setStatus("current")
_MitelDnsStatsQueryLocal_Type = Integer32
_MitelDnsStatsQueryLocal_Object = MibScalar
mitelDnsStatsQueryLocal = _MitelDnsStatsQueryLocal_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 3),
    _MitelDnsStatsQueryLocal_Type()
)
mitelDnsStatsQueryLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsStatsQueryLocal.setStatus("current")
_MitelDnsStatsQueryLocalFail_Type = Integer32
_MitelDnsStatsQueryLocalFail_Object = MibScalar
mitelDnsStatsQueryLocalFail = _MitelDnsStatsQueryLocalFail_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 4),
    _MitelDnsStatsQueryLocalFail_Type()
)
mitelDnsStatsQueryLocalFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsStatsQueryLocalFail.setStatus("current")
_MitelDnsStatsQueryExternal_Type = Integer32
_MitelDnsStatsQueryExternal_Object = MibScalar
mitelDnsStatsQueryExternal = _MitelDnsStatsQueryExternal_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 5),
    _MitelDnsStatsQueryExternal_Type()
)
mitelDnsStatsQueryExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsStatsQueryExternal.setStatus("current")
_MitelDnsStatsQueryExternalFail_Type = Integer32
_MitelDnsStatsQueryExternalFail_Object = MibScalar
mitelDnsStatsQueryExternalFail = _MitelDnsStatsQueryExternalFail_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 6),
    _MitelDnsStatsQueryExternalFail_Type()
)
mitelDnsStatsQueryExternalFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsStatsQueryExternalFail.setStatus("current")
_MitelDnsStatsQueryInvalid_Type = Integer32
_MitelDnsStatsQueryInvalid_Object = MibScalar
mitelDnsStatsQueryInvalid = _MitelDnsStatsQueryInvalid_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 7),
    _MitelDnsStatsQueryInvalid_Type()
)
mitelDnsStatsQueryInvalid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsStatsQueryInvalid.setStatus("current")
_MitelDnsGrpDnsHostTable_Object = MibTable
mitelDnsGrpDnsHostTable = _MitelDnsGrpDnsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    mitelDnsGrpDnsHostTable.setStatus("current")
_MitelDnsGrpDnsHostEntry_Object = MibTableRow
mitelDnsGrpDnsHostEntry = _MitelDnsGrpDnsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10, 1)
)
mitelDnsGrpDnsHostEntry.setIndexNames(
    (0, "MITEL-DNSGROUP-MIB", "mitelDnsHostTableIpAddress"),
    (0, "MITEL-DNSGROUP-MIB", "mitelDnsHostTableHostName"),
)
if mibBuilder.loadTexts:
    mitelDnsGrpDnsHostEntry.setStatus("current")
_MitelDnsHostTableIpAddress_Type = IpAddress
_MitelDnsHostTableIpAddress_Object = MibTableColumn
mitelDnsHostTableIpAddress = _MitelDnsHostTableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10, 1, 1),
    _MitelDnsHostTableIpAddress_Type()
)
mitelDnsHostTableIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsHostTableIpAddress.setStatus("current")


class _MitelDnsHostTableHostName_Type(DisplayString):
    """Custom type mitelDnsHostTableHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_MitelDnsHostTableHostName_Type.__name__ = "DisplayString"
_MitelDnsHostTableHostName_Object = MibTableColumn
mitelDnsHostTableHostName = _MitelDnsHostTableHostName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10, 1, 2),
    _MitelDnsHostTableHostName_Type()
)
mitelDnsHostTableHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDnsHostTableHostName.setStatus("current")
_MitelDnsHostTableRowStatus_Type = RowStatus
_MitelDnsHostTableRowStatus_Object = MibTableColumn
mitelDnsHostTableRowStatus = _MitelDnsHostTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10, 1, 3),
    _MitelDnsHostTableRowStatus_Type()
)
mitelDnsHostTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelDnsHostTableRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-DNSGROUP-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterIpGroup": mitelRouterIpGroup,
       "mitelIpGrpDnsGroup": mitelIpGrpDnsGroup,
       "mitelDnsGrpDomainName": mitelDnsGrpDomainName,
       "mitelDnsGrpPrimaryDns": mitelDnsGrpPrimaryDns,
       "mitelDnsGrpSecondaryDns": mitelDnsGrpSecondaryDns,
       "mitelDnsGrpQueryOrder": mitelDnsGrpQueryOrder,
       "mitelDnsGrpAnswerTtl": mitelDnsGrpAnswerTtl,
       "mitelDnsGrpDnsPort": mitelDnsGrpDnsPort,
       "mitelDnsGrpFilterEnabled": mitelDnsGrpFilterEnabled,
       "mitelDnsGrpDnsStatistics": mitelDnsGrpDnsStatistics,
       "mitelDnsStatsQueryTotal": mitelDnsStatsQueryTotal,
       "mitelDnsStatsQueryFiltered": mitelDnsStatsQueryFiltered,
       "mitelDnsStatsQueryLocal": mitelDnsStatsQueryLocal,
       "mitelDnsStatsQueryLocalFail": mitelDnsStatsQueryLocalFail,
       "mitelDnsStatsQueryExternal": mitelDnsStatsQueryExternal,
       "mitelDnsStatsQueryExternalFail": mitelDnsStatsQueryExternalFail,
       "mitelDnsStatsQueryInvalid": mitelDnsStatsQueryInvalid,
       "mitelDnsGrpDnsHostTable": mitelDnsGrpDnsHostTable,
       "mitelDnsGrpDnsHostEntry": mitelDnsGrpDnsHostEntry,
       "mitelDnsHostTableIpAddress": mitelDnsHostTableIpAddress,
       "mitelDnsHostTableHostName": mitelDnsHostTableHostName,
       "mitelDnsHostTableRowStatus": mitelDnsHostTableRowStatus}
)
