# SNMP MIB module (CRMPKGCONF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CRMPKGCONF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:53 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Ntt_ObjectIdentity = ObjectIdentity
ntt = _Ntt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2)
)
_Ba3000_ObjectIdentity = ObjectIdentity
ba3000 = _Ba3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8)
)
_CrmCommon_ObjectIdentity = ObjectIdentity
crmCommon = _CrmCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1)
)
_CrmPkgConf_ObjectIdentity = ObjectIdentity
crmPkgConf = _CrmPkgConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2)
)
_CrmPkgDirectionTable_Object = MibTable
crmPkgDirectionTable = _CrmPkgDirectionTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    crmPkgDirectionTable.setStatus("mandatory")
_CrmPkgDirectionEntry_Object = MibTableRow
crmPkgDirectionEntry = _CrmPkgDirectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 1, 1)
)
crmPkgDirectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crmPkgDirectionEntry.setStatus("mandatory")
_CrmPkgDirectionNumber_Type = Integer32
_CrmPkgDirectionNumber_Object = MibTableColumn
crmPkgDirectionNumber = _CrmPkgDirectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 1, 1, 1),
    _CrmPkgDirectionNumber_Type()
)
crmPkgDirectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgDirectionNumber.setStatus("mandatory")
_CrmPkgHsdTable_Object = MibTable
crmPkgHsdTable = _CrmPkgHsdTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    crmPkgHsdTable.setStatus("mandatory")
_CrmPkgHsdEntry_Object = MibTableRow
crmPkgHsdEntry = _CrmPkgHsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 2, 1)
)
crmPkgHsdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CRMPKGCONF-MIB", "crmPkgHsdIfIndex"),
)
if mibBuilder.loadTexts:
    crmPkgHsdEntry.setStatus("mandatory")
_CrmPkgHsdIfIndex_Type = Integer32
_CrmPkgHsdIfIndex_Object = MibTableColumn
crmPkgHsdIfIndex = _CrmPkgHsdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 2, 1, 1),
    _CrmPkgHsdIfIndex_Type()
)
crmPkgHsdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmPkgHsdIfIndex.setStatus("mandatory")
_CrmPkgHsdLogIndex_Type = InterfaceIndex
_CrmPkgHsdLogIndex_Object = MibTableColumn
crmPkgHsdLogIndex = _CrmPkgHsdLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 2, 1, 2),
    _CrmPkgHsdLogIndex_Type()
)
crmPkgHsdLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgHsdLogIndex.setStatus("mandatory")
_CrmPkgHsdFirstTsNumber_Type = Integer32
_CrmPkgHsdFirstTsNumber_Object = MibTableColumn
crmPkgHsdFirstTsNumber = _CrmPkgHsdFirstTsNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 2, 1, 3),
    _CrmPkgHsdFirstTsNumber_Type()
)
crmPkgHsdFirstTsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdFirstTsNumber.setStatus("mandatory")
_CrmPkgHsdSubUsageInfo_Type = Integer32
_CrmPkgHsdSubUsageInfo_Object = MibTableColumn
crmPkgHsdSubUsageInfo = _CrmPkgHsdSubUsageInfo_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 2, 1, 4),
    _CrmPkgHsdSubUsageInfo_Type()
)
crmPkgHsdSubUsageInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdSubUsageInfo.setStatus("mandatory")


class _CrmPkgHsdAdminStatus_Type(Integer32):
    """Custom type crmPkgHsdAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgHsdAdminStatus_Type.__name__ = "Integer32"
_CrmPkgHsdAdminStatus_Object = MibTableColumn
crmPkgHsdAdminStatus = _CrmPkgHsdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 2, 1, 5),
    _CrmPkgHsdAdminStatus_Type()
)
crmPkgHsdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdAdminStatus.setStatus("mandatory")


class _CrmPkgHsdOperStatus_Type(Integer32):
    """Custom type crmPkgHsdOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgHsdOperStatus_Type.__name__ = "Integer32"
_CrmPkgHsdOperStatus_Object = MibTableColumn
crmPkgHsdOperStatus = _CrmPkgHsdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 2, 1, 6),
    _CrmPkgHsdOperStatus_Type()
)
crmPkgHsdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgHsdOperStatus.setStatus("mandatory")


class _CrmPkgHsdRowStatus_Type(Integer32):
    """Custom type crmPkgHsdRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgHsdRowStatus_Type.__name__ = "Integer32"
_CrmPkgHsdRowStatus_Object = MibTableColumn
crmPkgHsdRowStatus = _CrmPkgHsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 2, 1, 7),
    _CrmPkgHsdRowStatus_Type()
)
crmPkgHsdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdRowStatus.setStatus("mandatory")
_CrmPkgHsdAtmChgTable_Object = MibTable
crmPkgHsdAtmChgTable = _CrmPkgHsdAtmChgTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    crmPkgHsdAtmChgTable.setStatus("mandatory")
_CrmPkgHsdAtmChgEntry_Object = MibTableRow
crmPkgHsdAtmChgEntry = _CrmPkgHsdAtmChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 3, 1)
)
crmPkgHsdAtmChgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CRMPKGCONF-MIB", "crmPkgHsdAtmChgVpi"),
)
if mibBuilder.loadTexts:
    crmPkgHsdAtmChgEntry.setStatus("mandatory")


class _CrmPkgHsdAtmChgVpi_Type(Integer32):
    """Custom type crmPkgHsdAtmChgVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgHsdAtmChgVpi_Type.__name__ = "Integer32"
_CrmPkgHsdAtmChgVpi_Object = MibTableColumn
crmPkgHsdAtmChgVpi = _CrmPkgHsdAtmChgVpi_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 3, 1, 1),
    _CrmPkgHsdAtmChgVpi_Type()
)
crmPkgHsdAtmChgVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmPkgHsdAtmChgVpi.setStatus("mandatory")
_CrmPkgHsdAtmChgIndex_Type = Integer32
_CrmPkgHsdAtmChgIndex_Object = MibTableColumn
crmPkgHsdAtmChgIndex = _CrmPkgHsdAtmChgIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 3, 1, 2),
    _CrmPkgHsdAtmChgIndex_Type()
)
crmPkgHsdAtmChgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdAtmChgIndex.setStatus("mandatory")


class _CrmPkgHsdAtmAdminStatus_Type(Integer32):
    """Custom type crmPkgHsdAtmAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgHsdAtmAdminStatus_Type.__name__ = "Integer32"
_CrmPkgHsdAtmAdminStatus_Object = MibTableColumn
crmPkgHsdAtmAdminStatus = _CrmPkgHsdAtmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 3, 1, 3),
    _CrmPkgHsdAtmAdminStatus_Type()
)
crmPkgHsdAtmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdAtmAdminStatus.setStatus("mandatory")


class _CrmPkgHsdAtmOperStatus_Type(Integer32):
    """Custom type crmPkgHsdAtmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgHsdAtmOperStatus_Type.__name__ = "Integer32"
_CrmPkgHsdAtmOperStatus_Object = MibTableColumn
crmPkgHsdAtmOperStatus = _CrmPkgHsdAtmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 3, 1, 4),
    _CrmPkgHsdAtmOperStatus_Type()
)
crmPkgHsdAtmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgHsdAtmOperStatus.setStatus("mandatory")


class _CrmPkgHsdAtmRowStatus_Type(Integer32):
    """Custom type crmPkgHsdAtmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgHsdAtmRowStatus_Type.__name__ = "Integer32"
_CrmPkgHsdAtmRowStatus_Object = MibTableColumn
crmPkgHsdAtmRowStatus = _CrmPkgHsdAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 3, 1, 5),
    _CrmPkgHsdAtmRowStatus_Type()
)
crmPkgHsdAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdAtmRowStatus.setStatus("mandatory")
_CrmPkgHsdcTable_Object = MibTable
crmPkgHsdcTable = _CrmPkgHsdcTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    crmPkgHsdcTable.setStatus("mandatory")
_CrmPkgHsdcEntry_Object = MibTableRow
crmPkgHsdcEntry = _CrmPkgHsdcEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 4, 1)
)
crmPkgHsdcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CRMPKGCONF-MIB", "crmPkgHsdcIfIndex"),
)
if mibBuilder.loadTexts:
    crmPkgHsdcEntry.setStatus("mandatory")
_CrmPkgHsdcIfIndex_Type = Integer32
_CrmPkgHsdcIfIndex_Object = MibTableColumn
crmPkgHsdcIfIndex = _CrmPkgHsdcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 4, 1, 1),
    _CrmPkgHsdcIfIndex_Type()
)
crmPkgHsdcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmPkgHsdcIfIndex.setStatus("mandatory")
_CrmPkgHsdcLogIndex_Type = InterfaceIndex
_CrmPkgHsdcLogIndex_Object = MibTableColumn
crmPkgHsdcLogIndex = _CrmPkgHsdcLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 4, 1, 2),
    _CrmPkgHsdcLogIndex_Type()
)
crmPkgHsdcLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgHsdcLogIndex.setStatus("mandatory")
_CrmPkgHsdcFirstTsNumber_Type = Integer32
_CrmPkgHsdcFirstTsNumber_Object = MibTableColumn
crmPkgHsdcFirstTsNumber = _CrmPkgHsdcFirstTsNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 4, 1, 3),
    _CrmPkgHsdcFirstTsNumber_Type()
)
crmPkgHsdcFirstTsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdcFirstTsNumber.setStatus("mandatory")
_CrmPkgHsdcSubUsageInfo_Type = Integer32
_CrmPkgHsdcSubUsageInfo_Object = MibTableColumn
crmPkgHsdcSubUsageInfo = _CrmPkgHsdcSubUsageInfo_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 4, 1, 4),
    _CrmPkgHsdcSubUsageInfo_Type()
)
crmPkgHsdcSubUsageInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdcSubUsageInfo.setStatus("mandatory")


class _CrmPkgHsdcRowStatus_Type(Integer32):
    """Custom type crmPkgHsdcRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgHsdcRowStatus_Type.__name__ = "Integer32"
_CrmPkgHsdcRowStatus_Object = MibTableColumn
crmPkgHsdcRowStatus = _CrmPkgHsdcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 4, 1, 5),
    _CrmPkgHsdcRowStatus_Type()
)
crmPkgHsdcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdcRowStatus.setStatus("mandatory")
_CrmPkgHsdcAtmChgTable_Object = MibTable
crmPkgHsdcAtmChgTable = _CrmPkgHsdcAtmChgTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    crmPkgHsdcAtmChgTable.setStatus("mandatory")
_CrmPkgHsdcAtmChgEntry_Object = MibTableRow
crmPkgHsdcAtmChgEntry = _CrmPkgHsdcAtmChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 5, 1)
)
crmPkgHsdcAtmChgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CRMPKGCONF-MIB", "crmPkgHsdcAtmChgIndex"),
)
if mibBuilder.loadTexts:
    crmPkgHsdcAtmChgEntry.setStatus("mandatory")
_CrmPkgHsdcAtmChgIndex_Type = Integer32
_CrmPkgHsdcAtmChgIndex_Object = MibTableColumn
crmPkgHsdcAtmChgIndex = _CrmPkgHsdcAtmChgIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 5, 1, 1),
    _CrmPkgHsdcAtmChgIndex_Type()
)
crmPkgHsdcAtmChgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmPkgHsdcAtmChgIndex.setStatus("mandatory")


class _CrmPkgHsdcAtmChgVpi_Type(Integer32):
    """Custom type crmPkgHsdcAtmChgVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgHsdcAtmChgVpi_Type.__name__ = "Integer32"
_CrmPkgHsdcAtmChgVpi_Object = MibTableColumn
crmPkgHsdcAtmChgVpi = _CrmPkgHsdcAtmChgVpi_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 5, 1, 2),
    _CrmPkgHsdcAtmChgVpi_Type()
)
crmPkgHsdcAtmChgVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdcAtmChgVpi.setStatus("mandatory")


class _CrmPkgHsdcAtmChgVci_Type(Integer32):
    """Custom type crmPkgHsdcAtmChgVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgHsdcAtmChgVci_Type.__name__ = "Integer32"
_CrmPkgHsdcAtmChgVci_Object = MibTableColumn
crmPkgHsdcAtmChgVci = _CrmPkgHsdcAtmChgVci_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 5, 1, 3),
    _CrmPkgHsdcAtmChgVci_Type()
)
crmPkgHsdcAtmChgVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdcAtmChgVci.setStatus("mandatory")


class _CrmPkgHsdcAtmCsPduLength_Type(Integer32):
    """Custom type crmPkgHsdcAtmCsPduLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgHsdcAtmCsPduLength_Type.__name__ = "Integer32"
_CrmPkgHsdcAtmCsPduLength_Object = MibTableColumn
crmPkgHsdcAtmCsPduLength = _CrmPkgHsdcAtmCsPduLength_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 5, 1, 4),
    _CrmPkgHsdcAtmCsPduLength_Type()
)
crmPkgHsdcAtmCsPduLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdcAtmCsPduLength.setStatus("mandatory")


class _CrmPkgHsdcAtmAdminStatus_Type(Integer32):
    """Custom type crmPkgHsdcAtmAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgHsdcAtmAdminStatus_Type.__name__ = "Integer32"
_CrmPkgHsdcAtmAdminStatus_Object = MibTableColumn
crmPkgHsdcAtmAdminStatus = _CrmPkgHsdcAtmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 5, 1, 5),
    _CrmPkgHsdcAtmAdminStatus_Type()
)
crmPkgHsdcAtmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdcAtmAdminStatus.setStatus("mandatory")


class _CrmPkgHsdcAtmOperStatus_Type(Integer32):
    """Custom type crmPkgHsdcAtmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgHsdcAtmOperStatus_Type.__name__ = "Integer32"
_CrmPkgHsdcAtmOperStatus_Object = MibTableColumn
crmPkgHsdcAtmOperStatus = _CrmPkgHsdcAtmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 5, 1, 6),
    _CrmPkgHsdcAtmOperStatus_Type()
)
crmPkgHsdcAtmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgHsdcAtmOperStatus.setStatus("mandatory")


class _CrmPkgHsdcAtmRowStatus_Type(Integer32):
    """Custom type crmPkgHsdcAtmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgHsdcAtmRowStatus_Type.__name__ = "Integer32"
_CrmPkgHsdcAtmRowStatus_Object = MibTableColumn
crmPkgHsdcAtmRowStatus = _CrmPkgHsdcAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 5, 1, 7),
    _CrmPkgHsdcAtmRowStatus_Type()
)
crmPkgHsdcAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgHsdcAtmRowStatus.setStatus("mandatory")
_CrmPkgFrLineTable_Object = MibTable
crmPkgFrLineTable = _CrmPkgFrLineTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6)
)
if mibBuilder.loadTexts:
    crmPkgFrLineTable.setStatus("mandatory")
_CrmPkgFrLineEntry_Object = MibTableRow
crmPkgFrLineEntry = _CrmPkgFrLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1)
)
crmPkgFrLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crmPkgFrLineEntry.setStatus("mandatory")


class _CrmPkgFrLineStMode_Type(Integer32):
    """Custom type crmPkgFrLineStMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("st1-mode", 1),
          ("st2-mode", 2))
    )


_CrmPkgFrLineStMode_Type.__name__ = "Integer32"
_CrmPkgFrLineStMode_Object = MibTableColumn
crmPkgFrLineStMode = _CrmPkgFrLineStMode_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 1),
    _CrmPkgFrLineStMode_Type()
)
crmPkgFrLineStMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineStMode.setStatus("mandatory")


class _CrmPkgFrLineRate_Type(Integer32):
    """Custom type crmPkgFrLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bps1024k", 8),
          ("bps128k", 2),
          ("bps1536k", 9),
          ("bps192k", 3),
          ("bps2048k", 10),
          ("bps256k", 4),
          ("bps384k", 5),
          ("bps512k", 6),
          ("bps64K", 1),
          ("bps768k", 7))
    )


_CrmPkgFrLineRate_Type.__name__ = "Integer32"
_CrmPkgFrLineRate_Object = MibTableColumn
crmPkgFrLineRate = _CrmPkgFrLineRate_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 2),
    _CrmPkgFrLineRate_Type()
)
crmPkgFrLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineRate.setStatus("mandatory")


class _CrmPkgFrLineProtcol_Type(Integer32):
    """Custom type crmPkgFrLineProtcol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 2),
          ("itu", 1))
    )


_CrmPkgFrLineProtcol_Type.__name__ = "Integer32"
_CrmPkgFrLineProtcol_Object = MibTableColumn
crmPkgFrLineProtcol = _CrmPkgFrLineProtcol_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 3),
    _CrmPkgFrLineProtcol_Type()
)
crmPkgFrLineProtcol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineProtcol.setStatus("mandatory")


class _CrmPkgFrLineAalMode_Type(Integer32):
    """Custom type crmPkgFrLineAalMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("message-mode-assured", 2),
          ("message-mode-unassured", 3),
          ("stream-mode", 1))
    )


_CrmPkgFrLineAalMode_Type.__name__ = "Integer32"
_CrmPkgFrLineAalMode_Object = MibTableColumn
crmPkgFrLineAalMode = _CrmPkgFrLineAalMode_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 4),
    _CrmPkgFrLineAalMode_Type()
)
crmPkgFrLineAalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineAalMode.setStatus("mandatory")


class _CrmPkgFrLineFrameLength_Type(Integer32):
    """Custom type crmPkgFrLineFrameLength based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrLineFrameLength_Type.__name__ = "Integer32"
_CrmPkgFrLineFrameLength_Object = MibTableColumn
crmPkgFrLineFrameLength = _CrmPkgFrLineFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 5),
    _CrmPkgFrLineFrameLength_Type()
)
crmPkgFrLineFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineFrameLength.setStatus("mandatory")


class _CrmPkgFrLineLmiMode_Type(Integer32):
    """Custom type crmPkgFrLineLmiMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CrmPkgFrLineLmiMode_Type.__name__ = "Integer32"
_CrmPkgFrLineLmiMode_Object = MibTableColumn
crmPkgFrLineLmiMode = _CrmPkgFrLineLmiMode_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 6),
    _CrmPkgFrLineLmiMode_Type()
)
crmPkgFrLineLmiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineLmiMode.setStatus("mandatory")


class _CrmPkgFrLineDeClpMode_Type(Integer32):
    """Custom type crmPkgFrLineDeClpMode based on Integer32"""
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
        *(("off-mode", 1),
          ("on-mode", 2),
          ("user-info-mode", 3))
    )


_CrmPkgFrLineDeClpMode_Type.__name__ = "Integer32"
_CrmPkgFrLineDeClpMode_Object = MibTableColumn
crmPkgFrLineDeClpMode = _CrmPkgFrLineDeClpMode_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 7),
    _CrmPkgFrLineDeClpMode_Type()
)
crmPkgFrLineDeClpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineDeClpMode.setStatus("mandatory")


class _CrmPkgFrLineClpDeMode_Type(Integer32):
    """Custom type crmPkgFrLineClpDeMode based on Integer32"""
    defaultValue = 3

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
        *(("mapping-mode", 4),
          ("off-mode", 1),
          ("on-mode", 2),
          ("user-info-mode", 3))
    )


_CrmPkgFrLineClpDeMode_Type.__name__ = "Integer32"
_CrmPkgFrLineClpDeMode_Object = MibTableColumn
crmPkgFrLineClpDeMode = _CrmPkgFrLineClpDeMode_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 8),
    _CrmPkgFrLineClpDeMode_Type()
)
crmPkgFrLineClpDeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineClpDeMode.setStatus("mandatory")


class _CrmPkgFrLineFecnEfciMode_Type(Integer32):
    """Custom type crmPkgFrLineFecnEfciMode based on Integer32"""
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
        *(("off-mode", 1),
          ("on-mode", 2),
          ("user-info-mode", 3))
    )


_CrmPkgFrLineFecnEfciMode_Type.__name__ = "Integer32"
_CrmPkgFrLineFecnEfciMode_Object = MibTableColumn
crmPkgFrLineFecnEfciMode = _CrmPkgFrLineFecnEfciMode_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 9),
    _CrmPkgFrLineFecnEfciMode_Type()
)
crmPkgFrLineFecnEfciMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineFecnEfciMode.setStatus("mandatory")


class _CrmPkgFrLineEfciFecnMode_Type(Integer32):
    """Custom type crmPkgFrLineEfciFecnMode based on Integer32"""
    defaultValue = 3

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
        *(("mapping-mode", 4),
          ("off-mode", 1),
          ("on-mode", 2),
          ("user-info-mode", 3))
    )


_CrmPkgFrLineEfciFecnMode_Type.__name__ = "Integer32"
_CrmPkgFrLineEfciFecnMode_Object = MibTableColumn
crmPkgFrLineEfciFecnMode = _CrmPkgFrLineEfciFecnMode_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 10),
    _CrmPkgFrLineEfciFecnMode_Type()
)
crmPkgFrLineEfciFecnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineEfciFecnMode.setStatus("mandatory")


class _CrmPkgFrLineFrSwLightSet_Type(Integer32):
    """Custom type crmPkgFrLineFrSwLightSet based on Integer32"""
    defaultValue = 60


_CrmPkgFrLineFrSwLightSet_Object = MibTableColumn
crmPkgFrLineFrSwLightSet = _CrmPkgFrLineFrSwLightSet_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 11),
    _CrmPkgFrLineFrSwLightSet_Type()
)
crmPkgFrLineFrSwLightSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineFrSwLightSet.setStatus("mandatory")


class _CrmPkgFrLineFrSwLightCancel_Type(Integer32):
    """Custom type crmPkgFrLineFrSwLightCancel based on Integer32"""
    defaultValue = 50


_CrmPkgFrLineFrSwLightCancel_Object = MibTableColumn
crmPkgFrLineFrSwLightCancel = _CrmPkgFrLineFrSwLightCancel_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 12),
    _CrmPkgFrLineFrSwLightCancel_Type()
)
crmPkgFrLineFrSwLightCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineFrSwLightCancel.setStatus("mandatory")


class _CrmPkgFrLineFrSwHeavySet_Type(Integer32):
    """Custom type crmPkgFrLineFrSwHeavySet based on Integer32"""
    defaultValue = 80


_CrmPkgFrLineFrSwHeavySet_Object = MibTableColumn
crmPkgFrLineFrSwHeavySet = _CrmPkgFrLineFrSwHeavySet_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 13),
    _CrmPkgFrLineFrSwHeavySet_Type()
)
crmPkgFrLineFrSwHeavySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineFrSwHeavySet.setStatus("mandatory")


class _CrmPkgFrLineFrSwHeavyCancel_Type(Integer32):
    """Custom type crmPkgFrLineFrSwHeavyCancel based on Integer32"""
    defaultValue = 70


_CrmPkgFrLineFrSwHeavyCancel_Object = MibTableColumn
crmPkgFrLineFrSwHeavyCancel = _CrmPkgFrLineFrSwHeavyCancel_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 14),
    _CrmPkgFrLineFrSwHeavyCancel_Type()
)
crmPkgFrLineFrSwHeavyCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineFrSwHeavyCancel.setStatus("mandatory")


class _CrmPkgFrLineSwFrLightSet_Type(Integer32):
    """Custom type crmPkgFrLineSwFrLightSet based on Integer32"""
    defaultValue = 60


_CrmPkgFrLineSwFrLightSet_Object = MibTableColumn
crmPkgFrLineSwFrLightSet = _CrmPkgFrLineSwFrLightSet_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 15),
    _CrmPkgFrLineSwFrLightSet_Type()
)
crmPkgFrLineSwFrLightSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineSwFrLightSet.setStatus("mandatory")


class _CrmPkgFrLineSwFrLightCancel_Type(Integer32):
    """Custom type crmPkgFrLineSwFrLightCancel based on Integer32"""
    defaultValue = 50


_CrmPkgFrLineSwFrLightCancel_Object = MibTableColumn
crmPkgFrLineSwFrLightCancel = _CrmPkgFrLineSwFrLightCancel_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 16),
    _CrmPkgFrLineSwFrLightCancel_Type()
)
crmPkgFrLineSwFrLightCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineSwFrLightCancel.setStatus("mandatory")


class _CrmPkgFrLineSwFrHeavySet_Type(Integer32):
    """Custom type crmPkgFrLineSwFrHeavySet based on Integer32"""
    defaultValue = 80


_CrmPkgFrLineSwFrHeavySet_Object = MibTableColumn
crmPkgFrLineSwFrHeavySet = _CrmPkgFrLineSwFrHeavySet_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 17),
    _CrmPkgFrLineSwFrHeavySet_Type()
)
crmPkgFrLineSwFrHeavySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineSwFrHeavySet.setStatus("mandatory")


class _CrmPkgFrLineSwFrHeavyCancel_Type(Integer32):
    """Custom type crmPkgFrLineSwFrHeavyCancel based on Integer32"""
    defaultValue = 70


_CrmPkgFrLineSwFrHeavyCancel_Object = MibTableColumn
crmPkgFrLineSwFrHeavyCancel = _CrmPkgFrLineSwFrHeavyCancel_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 18),
    _CrmPkgFrLineSwFrHeavyCancel_Type()
)
crmPkgFrLineSwFrHeavyCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineSwFrHeavyCancel.setStatus("mandatory")


class _CrmPkgFrLineT392Timer_Type(Integer32):
    """Custom type crmPkgFrLineT392Timer based on Integer32"""
    defaultValue = 15


_CrmPkgFrLineT392Timer_Object = MibTableColumn
crmPkgFrLineT392Timer = _CrmPkgFrLineT392Timer_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 19),
    _CrmPkgFrLineT392Timer_Type()
)
crmPkgFrLineT392Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineT392Timer.setStatus("mandatory")


class _CrmPkgFrLineN392Counter_Type(Integer32):
    """Custom type crmPkgFrLineN392Counter based on Integer32"""
    defaultValue = 3


_CrmPkgFrLineN392Counter_Object = MibTableColumn
crmPkgFrLineN392Counter = _CrmPkgFrLineN392Counter_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 20),
    _CrmPkgFrLineN392Counter_Type()
)
crmPkgFrLineN392Counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineN392Counter.setStatus("mandatory")


class _CrmPkgFrLineN393Counter_Type(Integer32):
    """Custom type crmPkgFrLineN393Counter based on Integer32"""
    defaultValue = 4


_CrmPkgFrLineN393Counter_Object = MibTableColumn
crmPkgFrLineN393Counter = _CrmPkgFrLineN393Counter_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 21),
    _CrmPkgFrLineN393Counter_Type()
)
crmPkgFrLineN393Counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineN393Counter.setStatus("mandatory")


class _CrmPkgFrLineArrivedCellTimer_Type(Integer32):
    """Custom type crmPkgFrLineArrivedCellTimer based on Integer32"""
    defaultValue = 10


_CrmPkgFrLineArrivedCellTimer_Object = MibTableColumn
crmPkgFrLineArrivedCellTimer = _CrmPkgFrLineArrivedCellTimer_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 22),
    _CrmPkgFrLineArrivedCellTimer_Type()
)
crmPkgFrLineArrivedCellTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineArrivedCellTimer.setStatus("mandatory")


class _CrmPkgFrLineShapingLevel1_Type(Integer32):
    """Custom type crmPkgFrLineShapingLevel1 based on Integer32"""
    defaultValue = 1908

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrLineShapingLevel1_Type.__name__ = "Integer32"
_CrmPkgFrLineShapingLevel1_Object = MibTableColumn
crmPkgFrLineShapingLevel1 = _CrmPkgFrLineShapingLevel1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 23),
    _CrmPkgFrLineShapingLevel1_Type()
)
crmPkgFrLineShapingLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineShapingLevel1.setStatus("mandatory")


class _CrmPkgFrLineShapingLevel2_Type(Integer32):
    """Custom type crmPkgFrLineShapingLevel2 based on Integer32"""
    defaultValue = 2544

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrLineShapingLevel2_Type.__name__ = "Integer32"
_CrmPkgFrLineShapingLevel2_Object = MibTableColumn
crmPkgFrLineShapingLevel2 = _CrmPkgFrLineShapingLevel2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 24),
    _CrmPkgFrLineShapingLevel2_Type()
)
crmPkgFrLineShapingLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineShapingLevel2.setStatus("mandatory")


class _CrmPkgFrLineShapingLevel3_Type(Integer32):
    """Custom type crmPkgFrLineShapingLevel3 based on Integer32"""
    defaultValue = 6452

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrLineShapingLevel3_Type.__name__ = "Integer32"
_CrmPkgFrLineShapingLevel3_Object = MibTableColumn
crmPkgFrLineShapingLevel3 = _CrmPkgFrLineShapingLevel3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 25),
    _CrmPkgFrLineShapingLevel3_Type()
)
crmPkgFrLineShapingLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineShapingLevel3.setStatus("mandatory")


class _CrmPkgFrLineShapingLevel4_Type(Integer32):
    """Custom type crmPkgFrLineShapingLevel4 based on Integer32"""
    defaultValue = 155883

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrLineShapingLevel4_Type.__name__ = "Integer32"
_CrmPkgFrLineShapingLevel4_Object = MibTableColumn
crmPkgFrLineShapingLevel4 = _CrmPkgFrLineShapingLevel4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 26),
    _CrmPkgFrLineShapingLevel4_Type()
)
crmPkgFrLineShapingLevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineShapingLevel4.setStatus("mandatory")


class _CrmPkgFrLineAdminStatus_Type(Integer32):
    """Custom type crmPkgFrLineAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgFrLineAdminStatus_Type.__name__ = "Integer32"
_CrmPkgFrLineAdminStatus_Object = MibTableColumn
crmPkgFrLineAdminStatus = _CrmPkgFrLineAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 27),
    _CrmPkgFrLineAdminStatus_Type()
)
crmPkgFrLineAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineAdminStatus.setStatus("mandatory")


class _CrmPkgFrLineOperStatus_Type(Integer32):
    """Custom type crmPkgFrLineOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgFrLineOperStatus_Type.__name__ = "Integer32"
_CrmPkgFrLineOperStatus_Object = MibTableColumn
crmPkgFrLineOperStatus = _CrmPkgFrLineOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 28),
    _CrmPkgFrLineOperStatus_Type()
)
crmPkgFrLineOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgFrLineOperStatus.setStatus("mandatory")


class _CrmPkgFrLineRowStatus_Type(Integer32):
    """Custom type crmPkgFrLineRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrLineRowStatus_Type.__name__ = "Integer32"
_CrmPkgFrLineRowStatus_Object = MibTableColumn
crmPkgFrLineRowStatus = _CrmPkgFrLineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 29),
    _CrmPkgFrLineRowStatus_Type()
)
crmPkgFrLineRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineRowStatus.setStatus("mandatory")


class _CrmPkgFrLineAbrMode_Type(Integer32):
    """Custom type crmPkgFrLineAbrMode based on Integer32"""
    defaultValue = 1


_CrmPkgFrLineAbrMode_Object = MibTableColumn
crmPkgFrLineAbrMode = _CrmPkgFrLineAbrMode_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 6, 1, 30),
    _CrmPkgFrLineAbrMode_Type()
)
crmPkgFrLineAbrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrLineAbrMode.setStatus("mandatory")
_CrmPkgFrDlcTable_Object = MibTable
crmPkgFrDlcTable = _CrmPkgFrDlcTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 7)
)
if mibBuilder.loadTexts:
    crmPkgFrDlcTable.setStatus("mandatory")
_CrmPkgFrDlcEntry_Object = MibTableRow
crmPkgFrDlcEntry = _CrmPkgFrDlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 7, 1)
)
crmPkgFrDlcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CRMPKGCONF-MIB", "crmPkgFrDlcIndex"),
)
if mibBuilder.loadTexts:
    crmPkgFrDlcEntry.setStatus("mandatory")
_CrmPkgFrDlcIndex_Type = Integer32
_CrmPkgFrDlcIndex_Object = MibTableColumn
crmPkgFrDlcIndex = _CrmPkgFrDlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 7, 1, 1),
    _CrmPkgFrDlcIndex_Type()
)
crmPkgFrDlcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmPkgFrDlcIndex.setStatus("mandatory")
_CrmPkgFrDlcCir_Type = Integer32
_CrmPkgFrDlcCir_Object = MibTableColumn
crmPkgFrDlcCir = _CrmPkgFrDlcCir_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 7, 1, 2),
    _CrmPkgFrDlcCir_Type()
)
crmPkgFrDlcCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrDlcCir.setStatus("mandatory")
_CrmPkgFrDlcEir_Type = Integer32
_CrmPkgFrDlcEir_Object = MibTableColumn
crmPkgFrDlcEir = _CrmPkgFrDlcEir_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 7, 1, 3),
    _CrmPkgFrDlcEir_Type()
)
crmPkgFrDlcEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrDlcEir.setStatus("mandatory")


class _CrmPkgFrDlcTc_Type(Integer32):
    """Custom type crmPkgFrDlcTc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrDlcTc_Type.__name__ = "Integer32"
_CrmPkgFrDlcTc_Object = MibTableColumn
crmPkgFrDlcTc = _CrmPkgFrDlcTc_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 7, 1, 4),
    _CrmPkgFrDlcTc_Type()
)
crmPkgFrDlcTc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrDlcTc.setStatus("mandatory")


class _CrmPkgFrDlcRowStatus_Type(Integer32):
    """Custom type crmPkgFrDlcRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrDlcRowStatus_Type.__name__ = "Integer32"
_CrmPkgFrDlcRowStatus_Object = MibTableColumn
crmPkgFrDlcRowStatus = _CrmPkgFrDlcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 7, 1, 5),
    _CrmPkgFrDlcRowStatus_Type()
)
crmPkgFrDlcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrDlcRowStatus.setStatus("mandatory")
_CrmPkgFrAtmChgTable_Object = MibTable
crmPkgFrAtmChgTable = _CrmPkgFrAtmChgTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 8)
)
if mibBuilder.loadTexts:
    crmPkgFrAtmChgTable.setStatus("mandatory")
_CrmPkgFrAtmChgEntry_Object = MibTableRow
crmPkgFrAtmChgEntry = _CrmPkgFrAtmChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 8, 1)
)
crmPkgFrAtmChgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CRMPKGCONF-MIB", "crmPkgFrAtmChgDlci"),
)
if mibBuilder.loadTexts:
    crmPkgFrAtmChgEntry.setStatus("mandatory")
_CrmPkgFrAtmChgDlci_Type = Integer32
_CrmPkgFrAtmChgDlci_Object = MibTableColumn
crmPkgFrAtmChgDlci = _CrmPkgFrAtmChgDlci_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 8, 1, 1),
    _CrmPkgFrAtmChgDlci_Type()
)
crmPkgFrAtmChgDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmPkgFrAtmChgDlci.setStatus("mandatory")
_CrmPkgFrAtmChgSscsDlci_Type = Integer32
_CrmPkgFrAtmChgSscsDlci_Object = MibTableColumn
crmPkgFrAtmChgSscsDlci = _CrmPkgFrAtmChgSscsDlci_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 8, 1, 2),
    _CrmPkgFrAtmChgSscsDlci_Type()
)
crmPkgFrAtmChgSscsDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrAtmChgSscsDlci.setStatus("mandatory")


class _CrmPkgFrAtmChgVpi_Type(Integer32):
    """Custom type crmPkgFrAtmChgVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrAtmChgVpi_Type.__name__ = "Integer32"
_CrmPkgFrAtmChgVpi_Object = MibTableColumn
crmPkgFrAtmChgVpi = _CrmPkgFrAtmChgVpi_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 8, 1, 3),
    _CrmPkgFrAtmChgVpi_Type()
)
crmPkgFrAtmChgVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrAtmChgVpi.setStatus("mandatory")


class _CrmPkgFrAtmChgVci_Type(Integer32):
    """Custom type crmPkgFrAtmChgVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrAtmChgVci_Type.__name__ = "Integer32"
_CrmPkgFrAtmChgVci_Object = MibTableColumn
crmPkgFrAtmChgVci = _CrmPkgFrAtmChgVci_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 8, 1, 4),
    _CrmPkgFrAtmChgVci_Type()
)
crmPkgFrAtmChgVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrAtmChgVci.setStatus("mandatory")


class _CrmPkgFrAtmChgAdminStatus_Type(Integer32):
    """Custom type crmPkgFrAtmChgAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgFrAtmChgAdminStatus_Type.__name__ = "Integer32"
_CrmPkgFrAtmChgAdminStatus_Object = MibTableColumn
crmPkgFrAtmChgAdminStatus = _CrmPkgFrAtmChgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 8, 1, 5),
    _CrmPkgFrAtmChgAdminStatus_Type()
)
crmPkgFrAtmChgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrAtmChgAdminStatus.setStatus("mandatory")


class _CrmPkgFrAtmChgOperStatus_Type(Integer32):
    """Custom type crmPkgFrAtmChgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgFrAtmChgOperStatus_Type.__name__ = "Integer32"
_CrmPkgFrAtmChgOperStatus_Object = MibTableColumn
crmPkgFrAtmChgOperStatus = _CrmPkgFrAtmChgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 8, 1, 6),
    _CrmPkgFrAtmChgOperStatus_Type()
)
crmPkgFrAtmChgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgFrAtmChgOperStatus.setStatus("mandatory")


class _CrmPkgFrAtmChgRowStatus_Type(Integer32):
    """Custom type crmPkgFrAtmChgRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgFrAtmChgRowStatus_Type.__name__ = "Integer32"
_CrmPkgFrAtmChgRowStatus_Object = MibTableColumn
crmPkgFrAtmChgRowStatus = _CrmPkgFrAtmChgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 8, 1, 7),
    _CrmPkgFrAtmChgRowStatus_Type()
)
crmPkgFrAtmChgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgFrAtmChgRowStatus.setStatus("mandatory")
_CrmPkgInsDchTable_Object = MibTable
crmPkgInsDchTable = _CrmPkgInsDchTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 9)
)
if mibBuilder.loadTexts:
    crmPkgInsDchTable.setStatus("mandatory")
_CrmPkgInsDchEntry_Object = MibTableRow
crmPkgInsDchEntry = _CrmPkgInsDchEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 9, 1)
)
crmPkgInsDchEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crmPkgInsDchEntry.setStatus("mandatory")


class _CrmPkgInsDch_Type(Integer32):
    """Custom type crmPkgInsDch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgInsDch_Type.__name__ = "Integer32"
_CrmPkgInsDch_Object = MibTableColumn
crmPkgInsDch = _CrmPkgInsDch_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 9, 1, 1),
    _CrmPkgInsDch_Type()
)
crmPkgInsDch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgInsDch.setStatus("mandatory")


class _CrmPkgInsDchRowStatus_Type(Integer32):
    """Custom type crmPkgInsDchRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgInsDchRowStatus_Type.__name__ = "Integer32"
_CrmPkgInsDchRowStatus_Object = MibTableColumn
crmPkgInsDchRowStatus = _CrmPkgInsDchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 9, 1, 2),
    _CrmPkgInsDchRowStatus_Type()
)
crmPkgInsDchRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgInsDchRowStatus.setStatus("mandatory")
_CrmPkgInsTable_Object = MibTable
crmPkgInsTable = _CrmPkgInsTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 10)
)
if mibBuilder.loadTexts:
    crmPkgInsTable.setStatus("mandatory")
_CrmPkgInsEntry_Object = MibTableRow
crmPkgInsEntry = _CrmPkgInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 10, 1)
)
crmPkgInsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CRMPKGCONF-MIB", "crmPkgInsChNumber"),
)
if mibBuilder.loadTexts:
    crmPkgInsEntry.setStatus("mandatory")
_CrmPkgInsChNumber_Type = Integer32
_CrmPkgInsChNumber_Object = MibTableColumn
crmPkgInsChNumber = _CrmPkgInsChNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 10, 1, 1),
    _CrmPkgInsChNumber_Type()
)
crmPkgInsChNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmPkgInsChNumber.setStatus("mandatory")
_CrmPkgInsLogIndex_Type = InterfaceIndex
_CrmPkgInsLogIndex_Object = MibTableColumn
crmPkgInsLogIndex = _CrmPkgInsLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 10, 1, 2),
    _CrmPkgInsLogIndex_Type()
)
crmPkgInsLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgInsLogIndex.setStatus("mandatory")


class _CrmPkgInsIfid_Type(Integer32):
    """Custom type crmPkgInsIfid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgInsIfid_Type.__name__ = "Integer32"
_CrmPkgInsIfid_Object = MibTableColumn
crmPkgInsIfid = _CrmPkgInsIfid_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 10, 1, 3),
    _CrmPkgInsIfid_Type()
)
crmPkgInsIfid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgInsIfid.setStatus("mandatory")


class _CrmPkgInsAdminStatus_Type(Integer32):
    """Custom type crmPkgInsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgInsAdminStatus_Type.__name__ = "Integer32"
_CrmPkgInsAdminStatus_Object = MibTableColumn
crmPkgInsAdminStatus = _CrmPkgInsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 10, 1, 4),
    _CrmPkgInsAdminStatus_Type()
)
crmPkgInsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgInsAdminStatus.setStatus("mandatory")


class _CrmPkgInsOperStatus_Type(Integer32):
    """Custom type crmPkgInsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgInsOperStatus_Type.__name__ = "Integer32"
_CrmPkgInsOperStatus_Object = MibTableColumn
crmPkgInsOperStatus = _CrmPkgInsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 10, 1, 5),
    _CrmPkgInsOperStatus_Type()
)
crmPkgInsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgInsOperStatus.setStatus("mandatory")


class _CrmPkgInsRowStatus_Type(Integer32):
    """Custom type crmPkgInsRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgInsRowStatus_Type.__name__ = "Integer32"
_CrmPkgInsRowStatus_Object = MibTableColumn
crmPkgInsRowStatus = _CrmPkgInsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 10, 1, 6),
    _CrmPkgInsRowStatus_Type()
)
crmPkgInsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgInsRowStatus.setStatus("mandatory")
_CrmPkgInsAtmChgTable_Object = MibTable
crmPkgInsAtmChgTable = _CrmPkgInsAtmChgTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 11)
)
if mibBuilder.loadTexts:
    crmPkgInsAtmChgTable.setStatus("mandatory")
_CrmPkgInsAtmChgEntry_Object = MibTableRow
crmPkgInsAtmChgEntry = _CrmPkgInsAtmChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 11, 1)
)
crmPkgInsAtmChgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CRMPKGCONF-MIB", "crmPkgInsAtmChgVpi"),
)
if mibBuilder.loadTexts:
    crmPkgInsAtmChgEntry.setStatus("mandatory")


class _CrmPkgInsAtmChgVpi_Type(Integer32):
    """Custom type crmPkgInsAtmChgVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgInsAtmChgVpi_Type.__name__ = "Integer32"
_CrmPkgInsAtmChgVpi_Object = MibTableColumn
crmPkgInsAtmChgVpi = _CrmPkgInsAtmChgVpi_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 11, 1, 1),
    _CrmPkgInsAtmChgVpi_Type()
)
crmPkgInsAtmChgVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmPkgInsAtmChgVpi.setStatus("mandatory")
_CrmPkgInsAtmChNumber_Type = Integer32
_CrmPkgInsAtmChNumber_Object = MibTableColumn
crmPkgInsAtmChNumber = _CrmPkgInsAtmChNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 11, 1, 2),
    _CrmPkgInsAtmChNumber_Type()
)
crmPkgInsAtmChNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgInsAtmChNumber.setStatus("mandatory")


class _CrmPkgInsAtmAdminStatus_Type(Integer32):
    """Custom type crmPkgInsAtmAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgInsAtmAdminStatus_Type.__name__ = "Integer32"
_CrmPkgInsAtmAdminStatus_Object = MibTableColumn
crmPkgInsAtmAdminStatus = _CrmPkgInsAtmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 11, 1, 3),
    _CrmPkgInsAtmAdminStatus_Type()
)
crmPkgInsAtmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgInsAtmAdminStatus.setStatus("mandatory")


class _CrmPkgInsAtmOperStatus_Type(Integer32):
    """Custom type crmPkgInsAtmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgInsAtmOperStatus_Type.__name__ = "Integer32"
_CrmPkgInsAtmOperStatus_Object = MibTableColumn
crmPkgInsAtmOperStatus = _CrmPkgInsAtmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 11, 1, 4),
    _CrmPkgInsAtmOperStatus_Type()
)
crmPkgInsAtmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgInsAtmOperStatus.setStatus("mandatory")


class _CrmPkgInsAtmRowStatus_Type(Integer32):
    """Custom type crmPkgInsAtmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgInsAtmRowStatus_Type.__name__ = "Integer32"
_CrmPkgInsAtmRowStatus_Object = MibTableColumn
crmPkgInsAtmRowStatus = _CrmPkgInsAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 11, 1, 5),
    _CrmPkgInsAtmRowStatus_Type()
)
crmPkgInsAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgInsAtmRowStatus.setStatus("mandatory")
_CrmPkgRs449Table_Object = MibTable
crmPkgRs449Table = _CrmPkgRs449Table_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 12)
)
if mibBuilder.loadTexts:
    crmPkgRs449Table.setStatus("mandatory")
_CrmPkgRs449Entry_Object = MibTableRow
crmPkgRs449Entry = _CrmPkgRs449Entry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 12, 1)
)
crmPkgRs449Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crmPkgRs449Entry.setStatus("mandatory")


class _CrmPkgRs449LineRate_Type(Integer32):
    """Custom type crmPkgRs449LineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bps1024k", 9),
          ("bps1152k", 10),
          ("bps128k", 2),
          ("bps1536k", 11),
          ("bps192k", 3),
          ("bps2048k", 12),
          ("bps2304k", 13),
          ("bps256k", 4),
          ("bps3072k", 14),
          ("bps384k", 5),
          ("bps4608k", 15),
          ("bps512k", 6),
          ("bps576k", 7),
          ("bps6144k", 16),
          ("bps64k", 1),
          ("bps768k", 8))
    )


_CrmPkgRs449LineRate_Type.__name__ = "Integer32"
_CrmPkgRs449LineRate_Object = MibTableColumn
crmPkgRs449LineRate = _CrmPkgRs449LineRate_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 12, 1, 1),
    _CrmPkgRs449LineRate_Type()
)
crmPkgRs449LineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgRs449LineRate.setStatus("mandatory")


class _CrmPkgRs449AdminStatus_Type(Integer32):
    """Custom type crmPkgRs449AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgRs449AdminStatus_Type.__name__ = "Integer32"
_CrmPkgRs449AdminStatus_Object = MibTableColumn
crmPkgRs449AdminStatus = _CrmPkgRs449AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 12, 1, 2),
    _CrmPkgRs449AdminStatus_Type()
)
crmPkgRs449AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgRs449AdminStatus.setStatus("mandatory")


class _CrmPkgRs449OperStatus_Type(Integer32):
    """Custom type crmPkgRs449OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CrmPkgRs449OperStatus_Type.__name__ = "Integer32"
_CrmPkgRs449OperStatus_Object = MibTableColumn
crmPkgRs449OperStatus = _CrmPkgRs449OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 12, 1, 3),
    _CrmPkgRs449OperStatus_Type()
)
crmPkgRs449OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPkgRs449OperStatus.setStatus("mandatory")


class _CrmPkgRs449RowStatus_Type(Integer32):
    """Custom type crmPkgRs449RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgRs449RowStatus_Type.__name__ = "Integer32"
_CrmPkgRs449RowStatus_Object = MibTableColumn
crmPkgRs449RowStatus = _CrmPkgRs449RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 2, 12, 1, 4),
    _CrmPkgRs449RowStatus_Type()
)
crmPkgRs449RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgRs449RowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRMPKGCONF-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "ntt": ntt,
       "mibDoc": mibDoc,
       "ba3000": ba3000,
       "crmCommon": crmCommon,
       "crmPkgConf": crmPkgConf,
       "crmPkgDirectionTable": crmPkgDirectionTable,
       "crmPkgDirectionEntry": crmPkgDirectionEntry,
       "crmPkgDirectionNumber": crmPkgDirectionNumber,
       "crmPkgHsdTable": crmPkgHsdTable,
       "crmPkgHsdEntry": crmPkgHsdEntry,
       "crmPkgHsdIfIndex": crmPkgHsdIfIndex,
       "crmPkgHsdLogIndex": crmPkgHsdLogIndex,
       "crmPkgHsdFirstTsNumber": crmPkgHsdFirstTsNumber,
       "crmPkgHsdSubUsageInfo": crmPkgHsdSubUsageInfo,
       "crmPkgHsdAdminStatus": crmPkgHsdAdminStatus,
       "crmPkgHsdOperStatus": crmPkgHsdOperStatus,
       "crmPkgHsdRowStatus": crmPkgHsdRowStatus,
       "crmPkgHsdAtmChgTable": crmPkgHsdAtmChgTable,
       "crmPkgHsdAtmChgEntry": crmPkgHsdAtmChgEntry,
       "crmPkgHsdAtmChgVpi": crmPkgHsdAtmChgVpi,
       "crmPkgHsdAtmChgIndex": crmPkgHsdAtmChgIndex,
       "crmPkgHsdAtmAdminStatus": crmPkgHsdAtmAdminStatus,
       "crmPkgHsdAtmOperStatus": crmPkgHsdAtmOperStatus,
       "crmPkgHsdAtmRowStatus": crmPkgHsdAtmRowStatus,
       "crmPkgHsdcTable": crmPkgHsdcTable,
       "crmPkgHsdcEntry": crmPkgHsdcEntry,
       "crmPkgHsdcIfIndex": crmPkgHsdcIfIndex,
       "crmPkgHsdcLogIndex": crmPkgHsdcLogIndex,
       "crmPkgHsdcFirstTsNumber": crmPkgHsdcFirstTsNumber,
       "crmPkgHsdcSubUsageInfo": crmPkgHsdcSubUsageInfo,
       "crmPkgHsdcRowStatus": crmPkgHsdcRowStatus,
       "crmPkgHsdcAtmChgTable": crmPkgHsdcAtmChgTable,
       "crmPkgHsdcAtmChgEntry": crmPkgHsdcAtmChgEntry,
       "crmPkgHsdcAtmChgIndex": crmPkgHsdcAtmChgIndex,
       "crmPkgHsdcAtmChgVpi": crmPkgHsdcAtmChgVpi,
       "crmPkgHsdcAtmChgVci": crmPkgHsdcAtmChgVci,
       "crmPkgHsdcAtmCsPduLength": crmPkgHsdcAtmCsPduLength,
       "crmPkgHsdcAtmAdminStatus": crmPkgHsdcAtmAdminStatus,
       "crmPkgHsdcAtmOperStatus": crmPkgHsdcAtmOperStatus,
       "crmPkgHsdcAtmRowStatus": crmPkgHsdcAtmRowStatus,
       "crmPkgFrLineTable": crmPkgFrLineTable,
       "crmPkgFrLineEntry": crmPkgFrLineEntry,
       "crmPkgFrLineStMode": crmPkgFrLineStMode,
       "crmPkgFrLineRate": crmPkgFrLineRate,
       "crmPkgFrLineProtcol": crmPkgFrLineProtcol,
       "crmPkgFrLineAalMode": crmPkgFrLineAalMode,
       "crmPkgFrLineFrameLength": crmPkgFrLineFrameLength,
       "crmPkgFrLineLmiMode": crmPkgFrLineLmiMode,
       "crmPkgFrLineDeClpMode": crmPkgFrLineDeClpMode,
       "crmPkgFrLineClpDeMode": crmPkgFrLineClpDeMode,
       "crmPkgFrLineFecnEfciMode": crmPkgFrLineFecnEfciMode,
       "crmPkgFrLineEfciFecnMode": crmPkgFrLineEfciFecnMode,
       "crmPkgFrLineFrSwLightSet": crmPkgFrLineFrSwLightSet,
       "crmPkgFrLineFrSwLightCancel": crmPkgFrLineFrSwLightCancel,
       "crmPkgFrLineFrSwHeavySet": crmPkgFrLineFrSwHeavySet,
       "crmPkgFrLineFrSwHeavyCancel": crmPkgFrLineFrSwHeavyCancel,
       "crmPkgFrLineSwFrLightSet": crmPkgFrLineSwFrLightSet,
       "crmPkgFrLineSwFrLightCancel": crmPkgFrLineSwFrLightCancel,
       "crmPkgFrLineSwFrHeavySet": crmPkgFrLineSwFrHeavySet,
       "crmPkgFrLineSwFrHeavyCancel": crmPkgFrLineSwFrHeavyCancel,
       "crmPkgFrLineT392Timer": crmPkgFrLineT392Timer,
       "crmPkgFrLineN392Counter": crmPkgFrLineN392Counter,
       "crmPkgFrLineN393Counter": crmPkgFrLineN393Counter,
       "crmPkgFrLineArrivedCellTimer": crmPkgFrLineArrivedCellTimer,
       "crmPkgFrLineShapingLevel1": crmPkgFrLineShapingLevel1,
       "crmPkgFrLineShapingLevel2": crmPkgFrLineShapingLevel2,
       "crmPkgFrLineShapingLevel3": crmPkgFrLineShapingLevel3,
       "crmPkgFrLineShapingLevel4": crmPkgFrLineShapingLevel4,
       "crmPkgFrLineAdminStatus": crmPkgFrLineAdminStatus,
       "crmPkgFrLineOperStatus": crmPkgFrLineOperStatus,
       "crmPkgFrLineRowStatus": crmPkgFrLineRowStatus,
       "crmPkgFrLineAbrMode": crmPkgFrLineAbrMode,
       "crmPkgFrDlcTable": crmPkgFrDlcTable,
       "crmPkgFrDlcEntry": crmPkgFrDlcEntry,
       "crmPkgFrDlcIndex": crmPkgFrDlcIndex,
       "crmPkgFrDlcCir": crmPkgFrDlcCir,
       "crmPkgFrDlcEir": crmPkgFrDlcEir,
       "crmPkgFrDlcTc": crmPkgFrDlcTc,
       "crmPkgFrDlcRowStatus": crmPkgFrDlcRowStatus,
       "crmPkgFrAtmChgTable": crmPkgFrAtmChgTable,
       "crmPkgFrAtmChgEntry": crmPkgFrAtmChgEntry,
       "crmPkgFrAtmChgDlci": crmPkgFrAtmChgDlci,
       "crmPkgFrAtmChgSscsDlci": crmPkgFrAtmChgSscsDlci,
       "crmPkgFrAtmChgVpi": crmPkgFrAtmChgVpi,
       "crmPkgFrAtmChgVci": crmPkgFrAtmChgVci,
       "crmPkgFrAtmChgAdminStatus": crmPkgFrAtmChgAdminStatus,
       "crmPkgFrAtmChgOperStatus": crmPkgFrAtmChgOperStatus,
       "crmPkgFrAtmChgRowStatus": crmPkgFrAtmChgRowStatus,
       "crmPkgInsDchTable": crmPkgInsDchTable,
       "crmPkgInsDchEntry": crmPkgInsDchEntry,
       "crmPkgInsDch": crmPkgInsDch,
       "crmPkgInsDchRowStatus": crmPkgInsDchRowStatus,
       "crmPkgInsTable": crmPkgInsTable,
       "crmPkgInsEntry": crmPkgInsEntry,
       "crmPkgInsChNumber": crmPkgInsChNumber,
       "crmPkgInsLogIndex": crmPkgInsLogIndex,
       "crmPkgInsIfid": crmPkgInsIfid,
       "crmPkgInsAdminStatus": crmPkgInsAdminStatus,
       "crmPkgInsOperStatus": crmPkgInsOperStatus,
       "crmPkgInsRowStatus": crmPkgInsRowStatus,
       "crmPkgInsAtmChgTable": crmPkgInsAtmChgTable,
       "crmPkgInsAtmChgEntry": crmPkgInsAtmChgEntry,
       "crmPkgInsAtmChgVpi": crmPkgInsAtmChgVpi,
       "crmPkgInsAtmChNumber": crmPkgInsAtmChNumber,
       "crmPkgInsAtmAdminStatus": crmPkgInsAtmAdminStatus,
       "crmPkgInsAtmOperStatus": crmPkgInsAtmOperStatus,
       "crmPkgInsAtmRowStatus": crmPkgInsAtmRowStatus,
       "crmPkgRs449Table": crmPkgRs449Table,
       "crmPkgRs449Entry": crmPkgRs449Entry,
       "crmPkgRs449LineRate": crmPkgRs449LineRate,
       "crmPkgRs449AdminStatus": crmPkgRs449AdminStatus,
       "crmPkgRs449OperStatus": crmPkgRs449OperStatus,
       "crmPkgRs449RowStatus": crmPkgRs449RowStatus}
)
