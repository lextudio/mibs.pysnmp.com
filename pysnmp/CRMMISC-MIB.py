# SNMP MIB module (CRMMISC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CRMMISC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:52 2024
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
_CrmMisc_ObjectIdentity = ObjectIdentity
crmMisc = _CrmMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8)
)
_CrmFileBup_ObjectIdentity = ObjectIdentity
crmFileBup = _CrmFileBup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 1)
)
_CrmFileBupTable_Object = MibTable
crmFileBupTable = _CrmFileBupTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    crmFileBupTable.setStatus("mandatory")
_CrmFileBupEntry_Object = MibTableRow
crmFileBupEntry = _CrmFileBupEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 1, 1, 1)
)
crmFileBupEntry.setIndexNames(
    (0, "CRMMISC-MIB", "crmFileBupFileType"),
    (0, "CRMMISC-MIB", "crmFileBupWriteHd"),
    (0, "CRMMISC-MIB", "crmFileBupWriteMod"),
)
if mibBuilder.loadTexts:
    crmFileBupEntry.setStatus("mandatory")


class _CrmFileBupFileType_Type(Integer32):
    """Custom type crmFileBupFileType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("atmAdrChgInfo", 13),
          ("atmAdrInfo", 11),
          ("callFilterInfo", 10),
          ("clkInfo", 8),
          ("dataFile", 2),
          ("dynamicInfo", 4),
          ("fr-lineDlciInfo", 5),
          ("managePathInfo", 7),
          ("p-mpPathInfo", 3),
          ("priContInfo", 9),
          ("routeInfo", 6),
          ("sapInfo", 12),
          ("spvcInfo", 14),
          ("systemFile", 1))
    )


_CrmFileBupFileType_Type.__name__ = "Integer32"
_CrmFileBupFileType_Object = MibTableColumn
crmFileBupFileType = _CrmFileBupFileType_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 1, 1, 1, 1),
    _CrmFileBupFileType_Type()
)
crmFileBupFileType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmFileBupFileType.setStatus("mandatory")


class _CrmFileBupWriteHd_Type(Integer32):
    """Custom type crmFileBupWriteHd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system0", 1),
          ("system1", 2))
    )


_CrmFileBupWriteHd_Type.__name__ = "Integer32"
_CrmFileBupWriteHd_Object = MibTableColumn
crmFileBupWriteHd = _CrmFileBupWriteHd_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 1, 1, 1, 2),
    _CrmFileBupWriteHd_Type()
)
crmFileBupWriteHd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmFileBupWriteHd.setStatus("mandatory")


class _CrmFileBupWriteMod_Type(Integer32):
    """Custom type crmFileBupWriteMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asNewFile", 1),
          ("asOldFile", 2))
    )


_CrmFileBupWriteMod_Type.__name__ = "Integer32"
_CrmFileBupWriteMod_Object = MibTableColumn
crmFileBupWriteMod = _CrmFileBupWriteMod_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 1, 1, 1, 3),
    _CrmFileBupWriteMod_Type()
)
crmFileBupWriteMod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmFileBupWriteMod.setStatus("mandatory")


class _CrmFileBupStatus_Type(Integer32):
    """Custom type crmFileBupStatus based on Integer32"""
    defaultValue = 2

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
        *(("errorEnd", 3),
          ("normalEnd", 2),
          ("others", 4),
          ("writeFile", 1))
    )


_CrmFileBupStatus_Type.__name__ = "Integer32"
_CrmFileBupStatus_Object = MibTableColumn
crmFileBupStatus = _CrmFileBupStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 1, 1, 1, 4),
    _CrmFileBupStatus_Type()
)
crmFileBupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmFileBupStatus.setStatus("mandatory")
_CrmFileBupName_Type = DisplayString
_CrmFileBupName_Object = MibTableColumn
crmFileBupName = _CrmFileBupName_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 1, 1, 1, 5),
    _CrmFileBupName_Type()
)
crmFileBupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmFileBupName.setStatus("mandatory")
_CrmMemCont_ObjectIdentity = ObjectIdentity
crmMemCont = _CrmMemCont_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2)
)
_CrmPkgMemBranch_ObjectIdentity = ObjectIdentity
crmPkgMemBranch = _CrmPkgMemBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 1)
)


class _CrmPkgMemType_Type(Integer32):
    """Custom type crmPkgMemType based on Integer32"""
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
        *(("acm", 3),
          ("asw", 2),
          ("asws", 5),
          ("cpm", 1),
          ("ifp", 4))
    )


_CrmPkgMemType_Type.__name__ = "Integer32"
_CrmPkgMemType_Object = MibScalar
crmPkgMemType = _CrmPkgMemType_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 1, 1),
    _CrmPkgMemType_Type()
)
crmPkgMemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgMemType.setStatus("mandatory")
_CrmPkgMemShelfIndex_Type = Integer32
_CrmPkgMemShelfIndex_Object = MibScalar
crmPkgMemShelfIndex = _CrmPkgMemShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 1, 2),
    _CrmPkgMemShelfIndex_Type()
)
crmPkgMemShelfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgMemShelfIndex.setStatus("mandatory")
_CrmPkgMemPkgIndex_Type = Integer32
_CrmPkgMemPkgIndex_Object = MibScalar
crmPkgMemPkgIndex = _CrmPkgMemPkgIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 1, 3),
    _CrmPkgMemPkgIndex_Type()
)
crmPkgMemPkgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgMemPkgIndex.setStatus("mandatory")


class _CrmPkgMemProcessorIndex_Type(Integer32):
    """Custom type crmPkgMemProcessorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmPkgMemProcessorIndex_Type.__name__ = "Integer32"
_CrmPkgMemProcessorIndex_Object = MibScalar
crmPkgMemProcessorIndex = _CrmPkgMemProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 1, 4),
    _CrmPkgMemProcessorIndex_Type()
)
crmPkgMemProcessorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgMemProcessorIndex.setStatus("mandatory")
_CrmPkgMemAddress_Type = DisplayString
_CrmPkgMemAddress_Object = MibScalar
crmPkgMemAddress = _CrmPkgMemAddress_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 1, 5),
    _CrmPkgMemAddress_Type()
)
crmPkgMemAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgMemAddress.setStatus("mandatory")


class _CrmPkgMemSize_Type(Integer32):
    """Custom type crmPkgMemSize based on Integer32"""
    defaultValue = 0


_CrmPkgMemSize_Object = MibScalar
crmPkgMemSize = _CrmPkgMemSize_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 1, 6),
    _CrmPkgMemSize_Type()
)
crmPkgMemSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgMemSize.setStatus("mandatory")
_CrmPkgMemData_Type = DisplayString
_CrmPkgMemData_Object = MibScalar
crmPkgMemData = _CrmPkgMemData_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 1, 7),
    _CrmPkgMemData_Type()
)
crmPkgMemData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmPkgMemData.setStatus("mandatory")
_CrmFileDataBranch_ObjectIdentity = ObjectIdentity
crmFileDataBranch = _CrmFileDataBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 2)
)
_CrmFilePathName_Type = DisplayString
_CrmFilePathName_Object = MibScalar
crmFilePathName = _CrmFilePathName_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 2, 1),
    _CrmFilePathName_Type()
)
crmFilePathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmFilePathName.setStatus("mandatory")
_CrmFileDataAddress_Type = DisplayString
_CrmFileDataAddress_Object = MibScalar
crmFileDataAddress = _CrmFileDataAddress_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 2, 2),
    _CrmFileDataAddress_Type()
)
crmFileDataAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmFileDataAddress.setStatus("mandatory")
_CrmFileDataSize_Type = Integer32
_CrmFileDataSize_Object = MibScalar
crmFileDataSize = _CrmFileDataSize_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 2, 3),
    _CrmFileDataSize_Type()
)
crmFileDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmFileDataSize.setStatus("mandatory")


class _CrmFileHdSysNo_Type(Integer32):
    """Custom type crmFileHdSysNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system0", 1),
          ("system1", 2))
    )


_CrmFileHdSysNo_Type.__name__ = "Integer32"
_CrmFileHdSysNo_Object = MibScalar
crmFileHdSysNo = _CrmFileHdSysNo_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 2, 4),
    _CrmFileHdSysNo_Type()
)
crmFileHdSysNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmFileHdSysNo.setStatus("mandatory")
_CrmFileData_Type = DisplayString
_CrmFileData_Object = MibScalar
crmFileData = _CrmFileData_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 2, 2, 5),
    _CrmFileData_Type()
)
crmFileData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmFileData.setStatus("mandatory")
_CrmFileRead_ObjectIdentity = ObjectIdentity
crmFileRead = _CrmFileRead_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 3)
)
_CrmFileReadPathName_Type = DisplayString
_CrmFileReadPathName_Object = MibScalar
crmFileReadPathName = _CrmFileReadPathName_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 3, 1),
    _CrmFileReadPathName_Type()
)
crmFileReadPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmFileReadPathName.setStatus("mandatory")


class _CrmFileReadStatus_Type(Integer32):
    """Custom type crmFileReadStatus based on Integer32"""
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
        *(("errorEnd", 3),
          ("normalEnd", 2),
          ("others", 4),
          ("readFile", 1))
    )


_CrmFileReadStatus_Type.__name__ = "Integer32"
_CrmFileReadStatus_Object = MibScalar
crmFileReadStatus = _CrmFileReadStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 3, 2),
    _CrmFileReadStatus_Type()
)
crmFileReadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmFileReadStatus.setStatus("mandatory")
_CrmAlmSup_ObjectIdentity = ObjectIdentity
crmAlmSup = _CrmAlmSup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4)
)
_CrmAlmSupIfTable_Object = MibTable
crmAlmSupIfTable = _CrmAlmSupIfTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    crmAlmSupIfTable.setStatus("mandatory")
_CrmAlmSupIfEntry_Object = MibTableRow
crmAlmSupIfEntry = _CrmAlmSupIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 1, 1)
)
crmAlmSupIfEntry.setIndexNames(
    (0, "CRMMISC-MIB", "crmAlmSupIfIndex"),
)
if mibBuilder.loadTexts:
    crmAlmSupIfEntry.setStatus("mandatory")
_CrmAlmSupIfIndex_Type = InterfaceIndex
_CrmAlmSupIfIndex_Object = MibTableColumn
crmAlmSupIfIndex = _CrmAlmSupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 1, 1, 1),
    _CrmAlmSupIfIndex_Type()
)
crmAlmSupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmAlmSupIfIndex.setStatus("mandatory")


class _CrmAlmSupIfAdminStatus_Type(Integer32):
    """Custom type crmAlmSupIfAdminStatus based on Integer32"""
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


_CrmAlmSupIfAdminStatus_Type.__name__ = "Integer32"
_CrmAlmSupIfAdminStatus_Object = MibTableColumn
crmAlmSupIfAdminStatus = _CrmAlmSupIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 1, 1, 2),
    _CrmAlmSupIfAdminStatus_Type()
)
crmAlmSupIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAlmSupIfAdminStatus.setStatus("mandatory")


class _CrmAlmSupIfOperStatus_Type(Integer32):
    """Custom type crmAlmSupIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("other", 3),
          ("up", 1))
    )


_CrmAlmSupIfOperStatus_Type.__name__ = "Integer32"
_CrmAlmSupIfOperStatus_Object = MibTableColumn
crmAlmSupIfOperStatus = _CrmAlmSupIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 1, 1, 3),
    _CrmAlmSupIfOperStatus_Type()
)
crmAlmSupIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmAlmSupIfOperStatus.setStatus("mandatory")
_CrmAlmSupIfPkgTable_Object = MibTable
crmAlmSupIfPkgTable = _CrmAlmSupIfPkgTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 2)
)
if mibBuilder.loadTexts:
    crmAlmSupIfPkgTable.setStatus("mandatory")
_CrmAlmSupIfPkgEntry_Object = MibTableRow
crmAlmSupIfPkgEntry = _CrmAlmSupIfPkgEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 2, 1)
)
crmAlmSupIfPkgEntry.setIndexNames(
    (0, "CRMMISC-MIB", "crmAlmSupIfPkgShelfNumber"),
    (0, "CRMMISC-MIB", "crmAlmSupIfPkgIndex"),
)
if mibBuilder.loadTexts:
    crmAlmSupIfPkgEntry.setStatus("mandatory")
_CrmAlmSupIfPkgShelfNumber_Type = Integer32
_CrmAlmSupIfPkgShelfNumber_Object = MibTableColumn
crmAlmSupIfPkgShelfNumber = _CrmAlmSupIfPkgShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 2, 1, 1),
    _CrmAlmSupIfPkgShelfNumber_Type()
)
crmAlmSupIfPkgShelfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmAlmSupIfPkgShelfNumber.setStatus("mandatory")
_CrmAlmSupIfPkgIndex_Type = Integer32
_CrmAlmSupIfPkgIndex_Object = MibTableColumn
crmAlmSupIfPkgIndex = _CrmAlmSupIfPkgIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 2, 1, 2),
    _CrmAlmSupIfPkgIndex_Type()
)
crmAlmSupIfPkgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmAlmSupIfPkgIndex.setStatus("mandatory")


class _CrmAlmSupIfPkgAdminStatus_Type(Integer32):
    """Custom type crmAlmSupIfPkgAdminStatus based on Integer32"""
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


_CrmAlmSupIfPkgAdminStatus_Type.__name__ = "Integer32"
_CrmAlmSupIfPkgAdminStatus_Object = MibTableColumn
crmAlmSupIfPkgAdminStatus = _CrmAlmSupIfPkgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 2, 1, 3),
    _CrmAlmSupIfPkgAdminStatus_Type()
)
crmAlmSupIfPkgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAlmSupIfPkgAdminStatus.setStatus("mandatory")


class _CrmAlmSupIfPkgOperStatus_Type(Integer32):
    """Custom type crmAlmSupIfPkgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("other", 3),
          ("up", 1))
    )


_CrmAlmSupIfPkgOperStatus_Type.__name__ = "Integer32"
_CrmAlmSupIfPkgOperStatus_Object = MibTableColumn
crmAlmSupIfPkgOperStatus = _CrmAlmSupIfPkgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 2, 1, 4),
    _CrmAlmSupIfPkgOperStatus_Type()
)
crmAlmSupIfPkgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmAlmSupIfPkgOperStatus.setStatus("mandatory")


class _CrmAlmSupSwPkgAdminStatus_Type(Integer32):
    """Custom type crmAlmSupSwPkgAdminStatus based on Integer32"""
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


_CrmAlmSupSwPkgAdminStatus_Type.__name__ = "Integer32"
_CrmAlmSupSwPkgAdminStatus_Object = MibScalar
crmAlmSupSwPkgAdminStatus = _CrmAlmSupSwPkgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 3),
    _CrmAlmSupSwPkgAdminStatus_Type()
)
crmAlmSupSwPkgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAlmSupSwPkgAdminStatus.setStatus("mandatory")


class _CrmAlmSupSwPkgOperStatus_Type(Integer32):
    """Custom type crmAlmSupSwPkgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("other", 3),
          ("up", 1))
    )


_CrmAlmSupSwPkgOperStatus_Type.__name__ = "Integer32"
_CrmAlmSupSwPkgOperStatus_Object = MibScalar
crmAlmSupSwPkgOperStatus = _CrmAlmSupSwPkgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 4, 4),
    _CrmAlmSupSwPkgOperStatus_Type()
)
crmAlmSupSwPkgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmAlmSupSwPkgOperStatus.setStatus("mandatory")
_CrmAddInfo_ObjectIdentity = ObjectIdentity
crmAddInfo = _CrmAddInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5)
)


class _CrmAddInfoData1_Type(Integer32):
    """Custom type crmAddInfoData1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoData1_Type.__name__ = "Integer32"
_CrmAddInfoData1_Object = MibScalar
crmAddInfoData1 = _CrmAddInfoData1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 1),
    _CrmAddInfoData1_Type()
)
crmAddInfoData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmAddInfoData1.setStatus("mandatory")


class _CrmAddInfoDebugData1_Type(Integer32):
    """Custom type crmAddInfoDebugData1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData1_Type.__name__ = "Integer32"
_CrmAddInfoDebugData1_Object = MibScalar
crmAddInfoDebugData1 = _CrmAddInfoDebugData1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 2),
    _CrmAddInfoDebugData1_Type()
)
crmAddInfoDebugData1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData1.setStatus("mandatory")


class _CrmAddInfoDebugData2_Type(Integer32):
    """Custom type crmAddInfoDebugData2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData2_Type.__name__ = "Integer32"
_CrmAddInfoDebugData2_Object = MibScalar
crmAddInfoDebugData2 = _CrmAddInfoDebugData2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 3),
    _CrmAddInfoDebugData2_Type()
)
crmAddInfoDebugData2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData2.setStatus("mandatory")


class _CrmAddInfoDebugData3_Type(Integer32):
    """Custom type crmAddInfoDebugData3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData3_Type.__name__ = "Integer32"
_CrmAddInfoDebugData3_Object = MibScalar
crmAddInfoDebugData3 = _CrmAddInfoDebugData3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 4),
    _CrmAddInfoDebugData3_Type()
)
crmAddInfoDebugData3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData3.setStatus("mandatory")


class _CrmAddInfoDebugData4_Type(Integer32):
    """Custom type crmAddInfoDebugData4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData4_Type.__name__ = "Integer32"
_CrmAddInfoDebugData4_Object = MibScalar
crmAddInfoDebugData4 = _CrmAddInfoDebugData4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 5),
    _CrmAddInfoDebugData4_Type()
)
crmAddInfoDebugData4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData4.setStatus("mandatory")


class _CrmAddInfoDebugData5_Type(Integer32):
    """Custom type crmAddInfoDebugData5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData5_Type.__name__ = "Integer32"
_CrmAddInfoDebugData5_Object = MibScalar
crmAddInfoDebugData5 = _CrmAddInfoDebugData5_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 6),
    _CrmAddInfoDebugData5_Type()
)
crmAddInfoDebugData5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData5.setStatus("mandatory")


class _CrmAddInfoDebugData6_Type(Integer32):
    """Custom type crmAddInfoDebugData6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData6_Type.__name__ = "Integer32"
_CrmAddInfoDebugData6_Object = MibScalar
crmAddInfoDebugData6 = _CrmAddInfoDebugData6_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 7),
    _CrmAddInfoDebugData6_Type()
)
crmAddInfoDebugData6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData6.setStatus("mandatory")


class _CrmAddInfoDebugData7_Type(Integer32):
    """Custom type crmAddInfoDebugData7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData7_Type.__name__ = "Integer32"
_CrmAddInfoDebugData7_Object = MibScalar
crmAddInfoDebugData7 = _CrmAddInfoDebugData7_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 8),
    _CrmAddInfoDebugData7_Type()
)
crmAddInfoDebugData7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData7.setStatus("mandatory")


class _CrmAddInfoDebugData8_Type(Integer32):
    """Custom type crmAddInfoDebugData8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData8_Type.__name__ = "Integer32"
_CrmAddInfoDebugData8_Object = MibScalar
crmAddInfoDebugData8 = _CrmAddInfoDebugData8_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 9),
    _CrmAddInfoDebugData8_Type()
)
crmAddInfoDebugData8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData8.setStatus("mandatory")


class _CrmAddInfoDebugData9_Type(Integer32):
    """Custom type crmAddInfoDebugData9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData9_Type.__name__ = "Integer32"
_CrmAddInfoDebugData9_Object = MibScalar
crmAddInfoDebugData9 = _CrmAddInfoDebugData9_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 10),
    _CrmAddInfoDebugData9_Type()
)
crmAddInfoDebugData9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData9.setStatus("mandatory")


class _CrmAddInfoDebugData10_Type(Integer32):
    """Custom type crmAddInfoDebugData10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmAddInfoDebugData10_Type.__name__ = "Integer32"
_CrmAddInfoDebugData10_Object = MibScalar
crmAddInfoDebugData10 = _CrmAddInfoDebugData10_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 5, 11),
    _CrmAddInfoDebugData10_Type()
)
crmAddInfoDebugData10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmAddInfoDebugData10.setStatus("mandatory")
_CrmChangeBand_ObjectIdentity = ObjectIdentity
crmChangeBand = _CrmChangeBand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 6)
)


class _CrmChangeBandIfIndex_Type(Integer32):
    """Custom type crmChangeBandIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmChangeBandIfIndex_Type.__name__ = "Integer32"
_CrmChangeBandIfIndex_Object = MibScalar
crmChangeBandIfIndex = _CrmChangeBandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 6, 1),
    _CrmChangeBandIfIndex_Type()
)
crmChangeBandIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmChangeBandIfIndex.setStatus("mandatory")


class _CrmChangeBandMaxSpeed_Type(Integer32):
    """Custom type crmChangeBandMaxSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmChangeBandMaxSpeed_Type.__name__ = "Integer32"
_CrmChangeBandMaxSpeed_Object = MibScalar
crmChangeBandMaxSpeed = _CrmChangeBandMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 6, 2),
    _CrmChangeBandMaxSpeed_Type()
)
crmChangeBandMaxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmChangeBandMaxSpeed.setStatus("mandatory")


class _CrmChangeBandStatus_Type(Integer32):
    """Custom type crmChangeBandStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmChangeBandStatus_Type.__name__ = "Integer32"
_CrmChangeBandStatus_Object = MibScalar
crmChangeBandStatus = _CrmChangeBandStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 8, 6, 3),
    _CrmChangeBandStatus_Type()
)
crmChangeBandStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmChangeBandStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRMMISC-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "ntt": ntt,
       "mibDoc": mibDoc,
       "ba3000": ba3000,
       "crmCommon": crmCommon,
       "crmMisc": crmMisc,
       "crmFileBup": crmFileBup,
       "crmFileBupTable": crmFileBupTable,
       "crmFileBupEntry": crmFileBupEntry,
       "crmFileBupFileType": crmFileBupFileType,
       "crmFileBupWriteHd": crmFileBupWriteHd,
       "crmFileBupWriteMod": crmFileBupWriteMod,
       "crmFileBupStatus": crmFileBupStatus,
       "crmFileBupName": crmFileBupName,
       "crmMemCont": crmMemCont,
       "crmPkgMemBranch": crmPkgMemBranch,
       "crmPkgMemType": crmPkgMemType,
       "crmPkgMemShelfIndex": crmPkgMemShelfIndex,
       "crmPkgMemPkgIndex": crmPkgMemPkgIndex,
       "crmPkgMemProcessorIndex": crmPkgMemProcessorIndex,
       "crmPkgMemAddress": crmPkgMemAddress,
       "crmPkgMemSize": crmPkgMemSize,
       "crmPkgMemData": crmPkgMemData,
       "crmFileDataBranch": crmFileDataBranch,
       "crmFilePathName": crmFilePathName,
       "crmFileDataAddress": crmFileDataAddress,
       "crmFileDataSize": crmFileDataSize,
       "crmFileHdSysNo": crmFileHdSysNo,
       "crmFileData": crmFileData,
       "crmFileRead": crmFileRead,
       "crmFileReadPathName": crmFileReadPathName,
       "crmFileReadStatus": crmFileReadStatus,
       "crmAlmSup": crmAlmSup,
       "crmAlmSupIfTable": crmAlmSupIfTable,
       "crmAlmSupIfEntry": crmAlmSupIfEntry,
       "crmAlmSupIfIndex": crmAlmSupIfIndex,
       "crmAlmSupIfAdminStatus": crmAlmSupIfAdminStatus,
       "crmAlmSupIfOperStatus": crmAlmSupIfOperStatus,
       "crmAlmSupIfPkgTable": crmAlmSupIfPkgTable,
       "crmAlmSupIfPkgEntry": crmAlmSupIfPkgEntry,
       "crmAlmSupIfPkgShelfNumber": crmAlmSupIfPkgShelfNumber,
       "crmAlmSupIfPkgIndex": crmAlmSupIfPkgIndex,
       "crmAlmSupIfPkgAdminStatus": crmAlmSupIfPkgAdminStatus,
       "crmAlmSupIfPkgOperStatus": crmAlmSupIfPkgOperStatus,
       "crmAlmSupSwPkgAdminStatus": crmAlmSupSwPkgAdminStatus,
       "crmAlmSupSwPkgOperStatus": crmAlmSupSwPkgOperStatus,
       "crmAddInfo": crmAddInfo,
       "crmAddInfoData1": crmAddInfoData1,
       "crmAddInfoDebugData1": crmAddInfoDebugData1,
       "crmAddInfoDebugData2": crmAddInfoDebugData2,
       "crmAddInfoDebugData3": crmAddInfoDebugData3,
       "crmAddInfoDebugData4": crmAddInfoDebugData4,
       "crmAddInfoDebugData5": crmAddInfoDebugData5,
       "crmAddInfoDebugData6": crmAddInfoDebugData6,
       "crmAddInfoDebugData7": crmAddInfoDebugData7,
       "crmAddInfoDebugData8": crmAddInfoDebugData8,
       "crmAddInfoDebugData9": crmAddInfoDebugData9,
       "crmAddInfoDebugData10": crmAddInfoDebugData10,
       "crmChangeBand": crmChangeBand,
       "crmChangeBandIfIndex": crmChangeBandIfIndex,
       "crmChangeBandMaxSpeed": crmChangeBandMaxSpeed,
       "crmChangeBandStatus": crmChangeBandStatus}
)
