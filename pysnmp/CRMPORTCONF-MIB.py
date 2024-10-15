# SNMP MIB module (CRMPORTCONF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CRMPORTCONF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:54 2024
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
_CrmPortConf_ObjectIdentity = ObjectIdentity
crmPortConf = _CrmPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9)
)
_CrmPortConfTable_Object = MibTable
crmPortConfTable = _CrmPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 1)
)
if mibBuilder.loadTexts:
    crmPortConfTable.setStatus("mandatory")
_CrmPortConfEntry_Object = MibTableRow
crmPortConfEntry = _CrmPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 1, 1)
)
crmPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crmPortConfEntry.setStatus("mandatory")


class _CrmPortType_Type(Integer32):
    """Custom type crmPortType based on Integer32"""
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
              16,
              17,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("atm15", 9),
          ("atm150", 2),
          ("atm600", 1),
          ("atm63", 6),
          ("e1", 25),
          ("fr15", 14),
          ("fr20", 13),
          ("hsd15", 10),
          ("hsd15clad", 11),
          ("hsd192", 12),
          ("hsd63", 7),
          ("hsd63clad", 8),
          ("ins15", 15),
          ("ins64", 16),
          ("rs449", 17),
          ("sdh150", 4),
          ("sdh50", 5),
          ("sonet150", 3),
          ("t1", 26))
    )


_CrmPortType_Type.__name__ = "Integer32"
_CrmPortType_Object = MibTableColumn
crmPortType = _CrmPortType_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 1, 1, 1),
    _CrmPortType_Type()
)
crmPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPortType.setStatus("mandatory")


class _CrmPortMode_Type(Integer32):
    """Custom type crmPortMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan-mode", 1),
          ("wan-mode", 2))
    )


_CrmPortMode_Type.__name__ = "Integer32"
_CrmPortMode_Object = MibTableColumn
crmPortMode = _CrmPortMode_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 1, 1, 2),
    _CrmPortMode_Type()
)
crmPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPortMode.setStatus("mandatory")


class _CrmPortConfAdminStatus_Type(Integer32):
    """Custom type crmPortConfAdminStatus based on Integer32"""
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


_CrmPortConfAdminStatus_Type.__name__ = "Integer32"
_CrmPortConfAdminStatus_Object = MibTableColumn
crmPortConfAdminStatus = _CrmPortConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 1, 1, 3),
    _CrmPortConfAdminStatus_Type()
)
crmPortConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPortConfAdminStatus.setStatus("mandatory")


class _CrmPortConfOperStatus_Type(Integer32):
    """Custom type crmPortConfOperStatus based on Integer32"""
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


_CrmPortConfOperStatus_Type.__name__ = "Integer32"
_CrmPortConfOperStatus_Object = MibTableColumn
crmPortConfOperStatus = _CrmPortConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 1, 1, 4),
    _CrmPortConfOperStatus_Type()
)
crmPortConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPortConfOperStatus.setStatus("mandatory")


class _CrmPortConfRowStatus_Type(Integer32):
    """Custom type crmPortConfRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPortConfRowStatus_Type.__name__ = "Integer32"
_CrmPortConfRowStatus_Object = MibTableColumn
crmPortConfRowStatus = _CrmPortConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 1, 1, 5),
    _CrmPortConfRowStatus_Type()
)
crmPortConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPortConfRowStatus.setStatus("mandatory")
_CrmPriContPatternTable_Object = MibTable
crmPriContPatternTable = _CrmPriContPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 2)
)
if mibBuilder.loadTexts:
    crmPriContPatternTable.setStatus("mandatory")
_CrmPriContPatternEntry_Object = MibTableRow
crmPriContPatternEntry = _CrmPriContPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 2, 1)
)
crmPriContPatternEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crmPriContPatternEntry.setStatus("mandatory")


class _CrmPriContPatternActnPattern_Type(Integer32):
    """Custom type crmPriContPatternActnPattern based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pricont-pattern1", 1),
          ("pricont-pattern2", 2),
          ("pricont-pattern3", 3),
          ("pricont-pattern4", 4),
          ("pricont-pattern5", 5),
          ("pricont-pattern6", 6),
          ("pricont-pattern7", 7),
          ("pricont-pattern8", 8))
    )


_CrmPriContPatternActnPattern_Type.__name__ = "Integer32"
_CrmPriContPatternActnPattern_Object = MibTableColumn
crmPriContPatternActnPattern = _CrmPriContPatternActnPattern_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 2, 1, 1),
    _CrmPriContPatternActnPattern_Type()
)
crmPriContPatternActnPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContPatternActnPattern.setStatus("mandatory")


class _CrmPriContPatternAdminStatus_Type(Integer32):
    """Custom type crmPriContPatternAdminStatus based on Integer32"""
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


_CrmPriContPatternAdminStatus_Type.__name__ = "Integer32"
_CrmPriContPatternAdminStatus_Object = MibTableColumn
crmPriContPatternAdminStatus = _CrmPriContPatternAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 2, 1, 2),
    _CrmPriContPatternAdminStatus_Type()
)
crmPriContPatternAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContPatternAdminStatus.setStatus("mandatory")


class _CrmPriContPatternOperStatus_Type(Integer32):
    """Custom type crmPriContPatternOperStatus based on Integer32"""
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


_CrmPriContPatternOperStatus_Type.__name__ = "Integer32"
_CrmPriContPatternOperStatus_Object = MibTableColumn
crmPriContPatternOperStatus = _CrmPriContPatternOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 2, 1, 3),
    _CrmPriContPatternOperStatus_Type()
)
crmPriContPatternOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPriContPatternOperStatus.setStatus("mandatory")


class _CrmPriContPatternRowStatus_Type(Integer32):
    """Custom type crmPriContPatternRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPriContPatternRowStatus_Type.__name__ = "Integer32"
_CrmPriContPatternRowStatus_Object = MibTableColumn
crmPriContPatternRowStatus = _CrmPriContPatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 2, 1, 4),
    _CrmPriContPatternRowStatus_Type()
)
crmPriContPatternRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContPatternRowStatus.setStatus("mandatory")
_CrmPriContBufManageTable_Object = MibTable
crmPriContBufManageTable = _CrmPriContBufManageTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 3)
)
if mibBuilder.loadTexts:
    crmPriContBufManageTable.setStatus("mandatory")
_CrmPriContBufManageEntry_Object = MibTableRow
crmPriContBufManageEntry = _CrmPriContBufManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 3, 1)
)
crmPriContBufManageEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crmPriContBufManageEntry.setStatus("mandatory")


class _CrmPriContBufSizeTblNumber_Type(Integer32):
    """Custom type crmPriContBufSizeTblNumber based on Integer32"""
    defaultValue = 0


_CrmPriContBufSizeTblNumber_Object = MibTableColumn
crmPriContBufSizeTblNumber = _CrmPriContBufSizeTblNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 3, 1, 1),
    _CrmPriContBufSizeTblNumber_Type()
)
crmPriContBufSizeTblNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPriContBufSizeTblNumber.setStatus("mandatory")


class _CrmPriContBufManageAdminStatus_Type(Integer32):
    """Custom type crmPriContBufManageAdminStatus based on Integer32"""
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


_CrmPriContBufManageAdminStatus_Type.__name__ = "Integer32"
_CrmPriContBufManageAdminStatus_Object = MibTableColumn
crmPriContBufManageAdminStatus = _CrmPriContBufManageAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 3, 1, 2),
    _CrmPriContBufManageAdminStatus_Type()
)
crmPriContBufManageAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContBufManageAdminStatus.setStatus("mandatory")


class _CrmPriContBufManageOperStatus_Type(Integer32):
    """Custom type crmPriContBufManageOperStatus based on Integer32"""
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


_CrmPriContBufManageOperStatus_Type.__name__ = "Integer32"
_CrmPriContBufManageOperStatus_Object = MibTableColumn
crmPriContBufManageOperStatus = _CrmPriContBufManageOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 3, 1, 3),
    _CrmPriContBufManageOperStatus_Type()
)
crmPriContBufManageOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPriContBufManageOperStatus.setStatus("mandatory")


class _CrmPriContBufManageRowStatus_Type(Integer32):
    """Custom type crmPriContBufManageRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPriContBufManageRowStatus_Type.__name__ = "Integer32"
_CrmPriContBufManageRowStatus_Object = MibTableColumn
crmPriContBufManageRowStatus = _CrmPriContBufManageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 3, 1, 4),
    _CrmPriContBufManageRowStatus_Type()
)
crmPriContBufManageRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContBufManageRowStatus.setStatus("mandatory")
_CrmPriContBufSizeTable_Object = MibTable
crmPriContBufSizeTable = _CrmPriContBufSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4)
)
if mibBuilder.loadTexts:
    crmPriContBufSizeTable.setStatus("mandatory")
_CrmPriContBufEntry_Object = MibTableRow
crmPriContBufEntry = _CrmPriContBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1)
)
crmPriContBufEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crmPriContBufEntry.setStatus("mandatory")


class _CrmPriContIfBufSize_Type(Integer32):
    """Custom type crmPriContIfBufSize based on Integer32"""
    defaultValue = 100


_CrmPriContIfBufSize_Object = MibTableColumn
crmPriContIfBufSize = _CrmPriContIfBufSize_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 1),
    _CrmPriContIfBufSize_Type()
)
crmPriContIfBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContIfBufSize.setStatus("mandatory")


class _CrmPriContCls1BufSize_Type(Integer32):
    """Custom type crmPriContCls1BufSize based on Integer32"""
    defaultValue = 10


_CrmPriContCls1BufSize_Object = MibTableColumn
crmPriContCls1BufSize = _CrmPriContCls1BufSize_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 2),
    _CrmPriContCls1BufSize_Type()
)
crmPriContCls1BufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContCls1BufSize.setStatus("mandatory")


class _CrmPriContCls2BufSize_Type(Integer32):
    """Custom type crmPriContCls2BufSize based on Integer32"""
    defaultValue = 20


_CrmPriContCls2BufSize_Object = MibTableColumn
crmPriContCls2BufSize = _CrmPriContCls2BufSize_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 3),
    _CrmPriContCls2BufSize_Type()
)
crmPriContCls2BufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContCls2BufSize.setStatus("mandatory")


class _CrmPriContCls3BufSize_Type(Integer32):
    """Custom type crmPriContCls3BufSize based on Integer32"""
    defaultValue = 30


_CrmPriContCls3BufSize_Object = MibTableColumn
crmPriContCls3BufSize = _CrmPriContCls3BufSize_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 4),
    _CrmPriContCls3BufSize_Type()
)
crmPriContCls3BufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContCls3BufSize.setStatus("mandatory")


class _CrmPriContCls4BufSize_Type(Integer32):
    """Custom type crmPriContCls4BufSize based on Integer32"""
    defaultValue = 40


_CrmPriContCls4BufSize_Object = MibTableColumn
crmPriContCls4BufSize = _CrmPriContCls4BufSize_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 5),
    _CrmPriContCls4BufSize_Type()
)
crmPriContCls4BufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContCls4BufSize.setStatus("mandatory")


class _CrmPriContCls1ConnNumber_Type(Integer32):
    """Custom type crmPriContCls1ConnNumber based on Integer32"""
    defaultValue = 16


_CrmPriContCls1ConnNumber_Object = MibTableColumn
crmPriContCls1ConnNumber = _CrmPriContCls1ConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 6),
    _CrmPriContCls1ConnNumber_Type()
)
crmPriContCls1ConnNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContCls1ConnNumber.setStatus("mandatory")


class _CrmPriContCls2ConnNumber_Type(Integer32):
    """Custom type crmPriContCls2ConnNumber based on Integer32"""
    defaultValue = 16


_CrmPriContCls2ConnNumber_Object = MibTableColumn
crmPriContCls2ConnNumber = _CrmPriContCls2ConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 7),
    _CrmPriContCls2ConnNumber_Type()
)
crmPriContCls2ConnNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContCls2ConnNumber.setStatus("mandatory")


class _CrmPriContCls3ConnNumber_Type(Integer32):
    """Custom type crmPriContCls3ConnNumber based on Integer32"""
    defaultValue = 16


_CrmPriContCls3ConnNumber_Object = MibTableColumn
crmPriContCls3ConnNumber = _CrmPriContCls3ConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 8),
    _CrmPriContCls3ConnNumber_Type()
)
crmPriContCls3ConnNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContCls3ConnNumber.setStatus("mandatory")


class _CrmPriContCls4ConnNumber_Type(Integer32):
    """Custom type crmPriContCls4ConnNumber based on Integer32"""
    defaultValue = 16


_CrmPriContCls4ConnNumber_Object = MibTableColumn
crmPriContCls4ConnNumber = _CrmPriContCls4ConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 9),
    _CrmPriContCls4ConnNumber_Type()
)
crmPriContCls4ConnNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContCls4ConnNumber.setStatus("mandatory")


class _CrmPriContShapingBufSize_Type(Integer32):
    """Custom type crmPriContShapingBufSize based on Integer32"""
    defaultValue = 0


_CrmPriContShapingBufSize_Object = MibTableColumn
crmPriContShapingBufSize = _CrmPriContShapingBufSize_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 10),
    _CrmPriContShapingBufSize_Type()
)
crmPriContShapingBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContShapingBufSize.setStatus("mandatory")


class _CrmPriContBufSizeRowStatus_Type(Integer32):
    """Custom type crmPriContBufSizeRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPriContBufSizeRowStatus_Type.__name__ = "Integer32"
_CrmPriContBufSizeRowStatus_Object = MibTableColumn
crmPriContBufSizeRowStatus = _CrmPriContBufSizeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 4, 1, 11),
    _CrmPriContBufSizeRowStatus_Type()
)
crmPriContBufSizeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContBufSizeRowStatus.setStatus("mandatory")
_CrmPriContVpiShaperTable_Object = MibTable
crmPriContVpiShaperTable = _CrmPriContVpiShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 5)
)
if mibBuilder.loadTexts:
    crmPriContVpiShaperTable.setStatus("mandatory")
_CrmPriContVpiShaperEntry_Object = MibTableRow
crmPriContVpiShaperEntry = _CrmPriContVpiShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 5, 1)
)
crmPriContVpiShaperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crmPriContVpiShaperEntry.setStatus("mandatory")


class _CrmPriContVpiShaperAdminStatus_Type(Integer32):
    """Custom type crmPriContVpiShaperAdminStatus based on Integer32"""
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


_CrmPriContVpiShaperAdminStatus_Type.__name__ = "Integer32"
_CrmPriContVpiShaperAdminStatus_Object = MibTableColumn
crmPriContVpiShaperAdminStatus = _CrmPriContVpiShaperAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 5, 1, 1),
    _CrmPriContVpiShaperAdminStatus_Type()
)
crmPriContVpiShaperAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContVpiShaperAdminStatus.setStatus("mandatory")


class _CrmPriContVpiShaperOperStatus_Type(Integer32):
    """Custom type crmPriContVpiShaperOperStatus based on Integer32"""
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


_CrmPriContVpiShaperOperStatus_Type.__name__ = "Integer32"
_CrmPriContVpiShaperOperStatus_Object = MibTableColumn
crmPriContVpiShaperOperStatus = _CrmPriContVpiShaperOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 5, 1, 2),
    _CrmPriContVpiShaperOperStatus_Type()
)
crmPriContVpiShaperOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmPriContVpiShaperOperStatus.setStatus("mandatory")


class _CrmPriContVpiShaperRowStatus_Type(Integer32):
    """Custom type crmPriContVpiShaperRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPriContVpiShaperRowStatus_Type.__name__ = "Integer32"
_CrmPriContVpiShaperRowStatus_Object = MibTableColumn
crmPriContVpiShaperRowStatus = _CrmPriContVpiShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 5, 1, 3),
    _CrmPriContVpiShaperRowStatus_Type()
)
crmPriContVpiShaperRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPriContVpiShaperRowStatus.setStatus("mandatory")
_CrmCacTable_Object = MibTable
crmCacTable = _CrmCacTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 6)
)
if mibBuilder.loadTexts:
    crmCacTable.setStatus("mandatory")
_CrmCacEntry_Object = MibTableRow
crmCacEntry = _CrmCacEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 6, 1)
)
crmCacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CRMPORTCONF-MIB", "crmCacDirection"),
)
if mibBuilder.loadTexts:
    crmCacEntry.setStatus("mandatory")


class _CrmCacDirection_Type(Integer32):
    """Custom type crmCacDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifp2sw", 1),
          ("sw2ifp", 2))
    )


_CrmCacDirection_Type.__name__ = "Integer32"
_CrmCacDirection_Object = MibTableColumn
crmCacDirection = _CrmCacDirection_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 6, 1, 1),
    _CrmCacDirection_Type()
)
crmCacDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmCacDirection.setStatus("mandatory")


class _CrmCacCurrentBand_Type(Integer32):
    """Custom type crmCacCurrentBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmCacCurrentBand_Type.__name__ = "Integer32"
_CrmCacCurrentBand_Object = MibTableColumn
crmCacCurrentBand = _CrmCacCurrentBand_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 6, 1, 2),
    _CrmCacCurrentBand_Type()
)
crmCacCurrentBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmCacCurrentBand.setStatus("mandatory")


class _CrmCacCapacityBand_Type(Integer32):
    """Custom type crmCacCapacityBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmCacCapacityBand_Type.__name__ = "Integer32"
_CrmCacCapacityBand_Object = MibTableColumn
crmCacCapacityBand = _CrmCacCapacityBand_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 6, 1, 3),
    _CrmCacCapacityBand_Type()
)
crmCacCapacityBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmCacCapacityBand.setStatus("mandatory")


class _CrmCacThreshold1_Type(Integer32):
    """Custom type crmCacThreshold1 based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmCacThreshold1_Type.__name__ = "Integer32"
_CrmCacThreshold1_Object = MibTableColumn
crmCacThreshold1 = _CrmCacThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 6, 1, 4),
    _CrmCacThreshold1_Type()
)
crmCacThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmCacThreshold1.setStatus("mandatory")


class _CrmCacThreshold2_Type(Integer32):
    """Custom type crmCacThreshold2 based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmCacThreshold2_Type.__name__ = "Integer32"
_CrmCacThreshold2_Object = MibTableColumn
crmCacThreshold2 = _CrmCacThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 6, 1, 5),
    _CrmCacThreshold2_Type()
)
crmCacThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmCacThreshold2.setStatus("mandatory")


class _CrmCacTrapStatus_Type(Integer32):
    """Custom type crmCacTrapStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CrmCacTrapStatus_Type.__name__ = "Integer32"
_CrmCacTrapStatus_Object = MibTableColumn
crmCacTrapStatus = _CrmCacTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 9, 6, 1, 6),
    _CrmCacTrapStatus_Type()
)
crmCacTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmCacTrapStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRMPORTCONF-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "ntt": ntt,
       "mibDoc": mibDoc,
       "ba3000": ba3000,
       "crmCommon": crmCommon,
       "crmPortConf": crmPortConf,
       "crmPortConfTable": crmPortConfTable,
       "crmPortConfEntry": crmPortConfEntry,
       "crmPortType": crmPortType,
       "crmPortMode": crmPortMode,
       "crmPortConfAdminStatus": crmPortConfAdminStatus,
       "crmPortConfOperStatus": crmPortConfOperStatus,
       "crmPortConfRowStatus": crmPortConfRowStatus,
       "crmPriContPatternTable": crmPriContPatternTable,
       "crmPriContPatternEntry": crmPriContPatternEntry,
       "crmPriContPatternActnPattern": crmPriContPatternActnPattern,
       "crmPriContPatternAdminStatus": crmPriContPatternAdminStatus,
       "crmPriContPatternOperStatus": crmPriContPatternOperStatus,
       "crmPriContPatternRowStatus": crmPriContPatternRowStatus,
       "crmPriContBufManageTable": crmPriContBufManageTable,
       "crmPriContBufManageEntry": crmPriContBufManageEntry,
       "crmPriContBufSizeTblNumber": crmPriContBufSizeTblNumber,
       "crmPriContBufManageAdminStatus": crmPriContBufManageAdminStatus,
       "crmPriContBufManageOperStatus": crmPriContBufManageOperStatus,
       "crmPriContBufManageRowStatus": crmPriContBufManageRowStatus,
       "crmPriContBufSizeTable": crmPriContBufSizeTable,
       "crmPriContBufEntry": crmPriContBufEntry,
       "crmPriContIfBufSize": crmPriContIfBufSize,
       "crmPriContCls1BufSize": crmPriContCls1BufSize,
       "crmPriContCls2BufSize": crmPriContCls2BufSize,
       "crmPriContCls3BufSize": crmPriContCls3BufSize,
       "crmPriContCls4BufSize": crmPriContCls4BufSize,
       "crmPriContCls1ConnNumber": crmPriContCls1ConnNumber,
       "crmPriContCls2ConnNumber": crmPriContCls2ConnNumber,
       "crmPriContCls3ConnNumber": crmPriContCls3ConnNumber,
       "crmPriContCls4ConnNumber": crmPriContCls4ConnNumber,
       "crmPriContShapingBufSize": crmPriContShapingBufSize,
       "crmPriContBufSizeRowStatus": crmPriContBufSizeRowStatus,
       "crmPriContVpiShaperTable": crmPriContVpiShaperTable,
       "crmPriContVpiShaperEntry": crmPriContVpiShaperEntry,
       "crmPriContVpiShaperAdminStatus": crmPriContVpiShaperAdminStatus,
       "crmPriContVpiShaperOperStatus": crmPriContVpiShaperOperStatus,
       "crmPriContVpiShaperRowStatus": crmPriContVpiShaperRowStatus,
       "crmCacTable": crmCacTable,
       "crmCacEntry": crmCacEntry,
       "crmCacDirection": crmCacDirection,
       "crmCacCurrentBand": crmCacCurrentBand,
       "crmCacCapacityBand": crmCacCapacityBand,
       "crmCacThreshold1": crmCacThreshold1,
       "crmCacThreshold2": crmCacThreshold2,
       "crmCacTrapStatus": crmCacTrapStatus}
)
