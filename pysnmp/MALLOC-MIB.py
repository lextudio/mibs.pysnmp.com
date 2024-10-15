# SNMP MIB module (MALLOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MALLOC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:00 2024
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

(IANAmallocRangeSource,
 IANAscopeSource) = mibBuilder.importSymbols(
    "IANA-MALLOC-MIB",
    "IANAmallocRangeSource",
    "IANAscopeSource")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(LanguageTag,) = mibBuilder.importSymbols(
    "IPMROUTE-STD-MIB",
    "LanguageTag")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mallocMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 101)
)
mallocMIB.setRevisions(
        ("2003-06-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MallocMIBObjects_ObjectIdentity = ObjectIdentity
mallocMIBObjects = _MallocMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 101, 1)
)
_Malloc_ObjectIdentity = ObjectIdentity
malloc = _Malloc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 101, 1, 1)
)


class _MallocCapabilities_Type(Bits):
    """Custom type mallocCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("retryAfter", 2),
          ("serverMobility", 1),
          ("startTime", 0))
    )

_MallocCapabilities_Type.__name__ = "Bits"
_MallocCapabilities_Object = MibScalar
mallocCapabilities = _MallocCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 1),
    _MallocCapabilities_Type()
)
mallocCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocCapabilities.setStatus("current")
_MallocScopeTable_Object = MibTable
mallocScopeTable = _MallocScopeTable_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mallocScopeTable.setStatus("current")
_MallocScopeEntry_Object = MibTableRow
mallocScopeEntry = _MallocScopeEntry_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1)
)
mallocScopeEntry.setIndexNames(
    (0, "MALLOC-MIB", "mallocScopeAddressType"),
    (0, "MALLOC-MIB", "mallocScopeFirstAddress"),
)
if mibBuilder.loadTexts:
    mallocScopeEntry.setStatus("current")
_MallocScopeAddressType_Type = InetAddressType
_MallocScopeAddressType_Object = MibTableColumn
mallocScopeAddressType = _MallocScopeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 1),
    _MallocScopeAddressType_Type()
)
mallocScopeAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mallocScopeAddressType.setStatus("current")


class _MallocScopeFirstAddress_Type(InetAddress):
    """Custom type mallocScopeFirstAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MallocScopeFirstAddress_Type.__name__ = "InetAddress"
_MallocScopeFirstAddress_Object = MibTableColumn
mallocScopeFirstAddress = _MallocScopeFirstAddress_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 2),
    _MallocScopeFirstAddress_Type()
)
mallocScopeFirstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mallocScopeFirstAddress.setStatus("current")


class _MallocScopeLastAddress_Type(InetAddress):
    """Custom type mallocScopeLastAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MallocScopeLastAddress_Type.__name__ = "InetAddress"
_MallocScopeLastAddress_Object = MibTableColumn
mallocScopeLastAddress = _MallocScopeLastAddress_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 3),
    _MallocScopeLastAddress_Type()
)
mallocScopeLastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeLastAddress.setStatus("current")


class _MallocScopeHopLimit_Type(Unsigned32):
    """Custom type mallocScopeHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MallocScopeHopLimit_Type.__name__ = "Unsigned32"
_MallocScopeHopLimit_Object = MibTableColumn
mallocScopeHopLimit = _MallocScopeHopLimit_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 4),
    _MallocScopeHopLimit_Type()
)
mallocScopeHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeHopLimit.setStatus("current")
_MallocScopeStatus_Type = RowStatus
_MallocScopeStatus_Object = MibTableColumn
mallocScopeStatus = _MallocScopeStatus_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 5),
    _MallocScopeStatus_Type()
)
mallocScopeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeStatus.setStatus("current")
_MallocScopeSource_Type = IANAscopeSource
_MallocScopeSource_Object = MibTableColumn
mallocScopeSource = _MallocScopeSource_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 6),
    _MallocScopeSource_Type()
)
mallocScopeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocScopeSource.setStatus("current")


class _MallocScopeDivisible_Type(TruthValue):
    """Custom type mallocScopeDivisible based on TruthValue"""


_MallocScopeDivisible_Object = MibTableColumn
mallocScopeDivisible = _MallocScopeDivisible_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 7),
    _MallocScopeDivisible_Type()
)
mallocScopeDivisible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeDivisible.setStatus("current")


class _MallocScopeServerAddressType_Type(InetAddressType):
    """Custom type mallocScopeServerAddressType based on InetAddressType"""


_MallocScopeServerAddressType_Object = MibTableColumn
mallocScopeServerAddressType = _MallocScopeServerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 8),
    _MallocScopeServerAddressType_Type()
)
mallocScopeServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeServerAddressType.setStatus("current")


class _MallocScopeServerAddress_Type(InetAddress):
    """Custom type mallocScopeServerAddress based on InetAddress"""
    defaultHexValue = ""


_MallocScopeServerAddress_Object = MibTableColumn
mallocScopeServerAddress = _MallocScopeServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 9),
    _MallocScopeServerAddress_Type()
)
mallocScopeServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeServerAddress.setStatus("current")


class _MallocScopeSSM_Type(TruthValue):
    """Custom type mallocScopeSSM based on TruthValue"""


_MallocScopeSSM_Object = MibTableColumn
mallocScopeSSM = _MallocScopeSSM_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 10),
    _MallocScopeSSM_Type()
)
mallocScopeSSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeSSM.setStatus("current")


class _MallocScopeStorage_Type(StorageType):
    """Custom type mallocScopeStorage based on StorageType"""


_MallocScopeStorage_Object = MibTableColumn
mallocScopeStorage = _MallocScopeStorage_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 2, 1, 11),
    _MallocScopeStorage_Type()
)
mallocScopeStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeStorage.setStatus("current")
_MallocScopeNameTable_Object = MibTable
mallocScopeNameTable = _MallocScopeNameTable_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mallocScopeNameTable.setStatus("current")
_MallocScopeNameEntry_Object = MibTableRow
mallocScopeNameEntry = _MallocScopeNameEntry_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 3, 1)
)
mallocScopeNameEntry.setIndexNames(
    (0, "MALLOC-MIB", "mallocScopeAddressType"),
    (0, "MALLOC-MIB", "mallocScopeFirstAddress"),
    (1, "MALLOC-MIB", "mallocScopeNameLangName"),
)
if mibBuilder.loadTexts:
    mallocScopeNameEntry.setStatus("current")


class _MallocScopeNameLangName_Type(LanguageTag):
    """Custom type mallocScopeNameLangName based on LanguageTag"""
    subtypeSpec = LanguageTag.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 94),
    )


_MallocScopeNameLangName_Type.__name__ = "LanguageTag"
_MallocScopeNameLangName_Object = MibTableColumn
mallocScopeNameLangName = _MallocScopeNameLangName_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 3, 1, 1),
    _MallocScopeNameLangName_Type()
)
mallocScopeNameLangName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mallocScopeNameLangName.setStatus("current")
_MallocScopeNameScopeName_Type = SnmpAdminString
_MallocScopeNameScopeName_Object = MibTableColumn
mallocScopeNameScopeName = _MallocScopeNameScopeName_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 3, 1, 2),
    _MallocScopeNameScopeName_Type()
)
mallocScopeNameScopeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeNameScopeName.setStatus("current")


class _MallocScopeNameDefault_Type(TruthValue):
    """Custom type mallocScopeNameDefault based on TruthValue"""


_MallocScopeNameDefault_Object = MibTableColumn
mallocScopeNameDefault = _MallocScopeNameDefault_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 3, 1, 3),
    _MallocScopeNameDefault_Type()
)
mallocScopeNameDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeNameDefault.setStatus("current")
_MallocScopeNameStatus_Type = RowStatus
_MallocScopeNameStatus_Object = MibTableColumn
mallocScopeNameStatus = _MallocScopeNameStatus_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 3, 1, 4),
    _MallocScopeNameStatus_Type()
)
mallocScopeNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeNameStatus.setStatus("current")


class _MallocScopeNameStorage_Type(StorageType):
    """Custom type mallocScopeNameStorage based on StorageType"""


_MallocScopeNameStorage_Object = MibTableColumn
mallocScopeNameStorage = _MallocScopeNameStorage_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 3, 1, 5),
    _MallocScopeNameStorage_Type()
)
mallocScopeNameStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocScopeNameStorage.setStatus("current")
_MallocAllocRangeTable_Object = MibTable
mallocAllocRangeTable = _MallocAllocRangeTable_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mallocAllocRangeTable.setStatus("current")
_MallocAllocRangeEntry_Object = MibTableRow
mallocAllocRangeEntry = _MallocAllocRangeEntry_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1)
)
mallocAllocRangeEntry.setIndexNames(
    (0, "MALLOC-MIB", "mallocScopeAddressType"),
    (0, "MALLOC-MIB", "mallocScopeFirstAddress"),
    (0, "MALLOC-MIB", "mallocAllocRangeFirstAddress"),
)
if mibBuilder.loadTexts:
    mallocAllocRangeEntry.setStatus("current")


class _MallocAllocRangeFirstAddress_Type(InetAddress):
    """Custom type mallocAllocRangeFirstAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MallocAllocRangeFirstAddress_Type.__name__ = "InetAddress"
_MallocAllocRangeFirstAddress_Object = MibTableColumn
mallocAllocRangeFirstAddress = _MallocAllocRangeFirstAddress_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 1),
    _MallocAllocRangeFirstAddress_Type()
)
mallocAllocRangeFirstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mallocAllocRangeFirstAddress.setStatus("current")


class _MallocAllocRangeLastAddress_Type(InetAddress):
    """Custom type mallocAllocRangeLastAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MallocAllocRangeLastAddress_Type.__name__ = "InetAddress"
_MallocAllocRangeLastAddress_Object = MibTableColumn
mallocAllocRangeLastAddress = _MallocAllocRangeLastAddress_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 2),
    _MallocAllocRangeLastAddress_Type()
)
mallocAllocRangeLastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocAllocRangeLastAddress.setStatus("current")
_MallocAllocRangeStatus_Type = RowStatus
_MallocAllocRangeStatus_Object = MibTableColumn
mallocAllocRangeStatus = _MallocAllocRangeStatus_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 3),
    _MallocAllocRangeStatus_Type()
)
mallocAllocRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocAllocRangeStatus.setStatus("current")
_MallocAllocRangeSource_Type = IANAmallocRangeSource
_MallocAllocRangeSource_Object = MibTableColumn
mallocAllocRangeSource = _MallocAllocRangeSource_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 4),
    _MallocAllocRangeSource_Type()
)
mallocAllocRangeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocAllocRangeSource.setStatus("current")


class _MallocAllocRangeLifetime_Type(Unsigned32):
    """Custom type mallocAllocRangeLifetime based on Unsigned32"""
    defaultValue = 0


_MallocAllocRangeLifetime_Object = MibTableColumn
mallocAllocRangeLifetime = _MallocAllocRangeLifetime_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 5),
    _MallocAllocRangeLifetime_Type()
)
mallocAllocRangeLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocAllocRangeLifetime.setStatus("current")
if mibBuilder.loadTexts:
    mallocAllocRangeLifetime.setUnits("seconds")


class _MallocAllocRangeMaxLeaseAddrs_Type(Unsigned32):
    """Custom type mallocAllocRangeMaxLeaseAddrs based on Unsigned32"""
    defaultValue = 0


_MallocAllocRangeMaxLeaseAddrs_Object = MibTableColumn
mallocAllocRangeMaxLeaseAddrs = _MallocAllocRangeMaxLeaseAddrs_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 6),
    _MallocAllocRangeMaxLeaseAddrs_Type()
)
mallocAllocRangeMaxLeaseAddrs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocAllocRangeMaxLeaseAddrs.setStatus("current")


class _MallocAllocRangeMaxLeaseTime_Type(Unsigned32):
    """Custom type mallocAllocRangeMaxLeaseTime based on Unsigned32"""
    defaultValue = 0


_MallocAllocRangeMaxLeaseTime_Object = MibTableColumn
mallocAllocRangeMaxLeaseTime = _MallocAllocRangeMaxLeaseTime_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 7),
    _MallocAllocRangeMaxLeaseTime_Type()
)
mallocAllocRangeMaxLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocAllocRangeMaxLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    mallocAllocRangeMaxLeaseTime.setUnits("seconds")
_MallocAllocRangeNumAllocatedAddrs_Type = Gauge32
_MallocAllocRangeNumAllocatedAddrs_Object = MibTableColumn
mallocAllocRangeNumAllocatedAddrs = _MallocAllocRangeNumAllocatedAddrs_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 8),
    _MallocAllocRangeNumAllocatedAddrs_Type()
)
mallocAllocRangeNumAllocatedAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocAllocRangeNumAllocatedAddrs.setStatus("current")
_MallocAllocRangeNumOfferedAddrs_Type = Gauge32
_MallocAllocRangeNumOfferedAddrs_Object = MibTableColumn
mallocAllocRangeNumOfferedAddrs = _MallocAllocRangeNumOfferedAddrs_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 9),
    _MallocAllocRangeNumOfferedAddrs_Type()
)
mallocAllocRangeNumOfferedAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocAllocRangeNumOfferedAddrs.setStatus("current")
_MallocAllocRangeNumWaitingAddrs_Type = Gauge32
_MallocAllocRangeNumWaitingAddrs_Object = MibTableColumn
mallocAllocRangeNumWaitingAddrs = _MallocAllocRangeNumWaitingAddrs_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 10),
    _MallocAllocRangeNumWaitingAddrs_Type()
)
mallocAllocRangeNumWaitingAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocAllocRangeNumWaitingAddrs.setStatus("current")
_MallocAllocRangeNumTryingAddrs_Type = Gauge32
_MallocAllocRangeNumTryingAddrs_Object = MibTableColumn
mallocAllocRangeNumTryingAddrs = _MallocAllocRangeNumTryingAddrs_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 11),
    _MallocAllocRangeNumTryingAddrs_Type()
)
mallocAllocRangeNumTryingAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocAllocRangeNumTryingAddrs.setStatus("current")
_MallocAllocRangeAdvertisable_Type = TruthValue
_MallocAllocRangeAdvertisable_Object = MibTableColumn
mallocAllocRangeAdvertisable = _MallocAllocRangeAdvertisable_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 12),
    _MallocAllocRangeAdvertisable_Type()
)
mallocAllocRangeAdvertisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocAllocRangeAdvertisable.setStatus("current")
_MallocAllocRangeTotalAllocatedAddrs_Type = Gauge32
_MallocAllocRangeTotalAllocatedAddrs_Object = MibTableColumn
mallocAllocRangeTotalAllocatedAddrs = _MallocAllocRangeTotalAllocatedAddrs_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 13),
    _MallocAllocRangeTotalAllocatedAddrs_Type()
)
mallocAllocRangeTotalAllocatedAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocAllocRangeTotalAllocatedAddrs.setStatus("current")
_MallocAllocRangeTotalRequestedAddrs_Type = Gauge32
_MallocAllocRangeTotalRequestedAddrs_Object = MibTableColumn
mallocAllocRangeTotalRequestedAddrs = _MallocAllocRangeTotalRequestedAddrs_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 14),
    _MallocAllocRangeTotalRequestedAddrs_Type()
)
mallocAllocRangeTotalRequestedAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocAllocRangeTotalRequestedAddrs.setStatus("current")


class _MallocAllocRangeStorage_Type(StorageType):
    """Custom type mallocAllocRangeStorage based on StorageType"""


_MallocAllocRangeStorage_Object = MibTableColumn
mallocAllocRangeStorage = _MallocAllocRangeStorage_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 4, 1, 15),
    _MallocAllocRangeStorage_Type()
)
mallocAllocRangeStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mallocAllocRangeStorage.setStatus("current")
_MallocRequestTable_Object = MibTable
mallocRequestTable = _MallocRequestTable_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mallocRequestTable.setStatus("current")
_MallocRequestEntry_Object = MibTableRow
mallocRequestEntry = _MallocRequestEntry_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1)
)
mallocRequestEntry.setIndexNames(
    (0, "MALLOC-MIB", "mallocRequestId"),
)
if mibBuilder.loadTexts:
    mallocRequestEntry.setStatus("current")


class _MallocRequestId_Type(Unsigned32):
    """Custom type mallocRequestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MallocRequestId_Type.__name__ = "Unsigned32"
_MallocRequestId_Object = MibTableColumn
mallocRequestId = _MallocRequestId_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 1),
    _MallocRequestId_Type()
)
mallocRequestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mallocRequestId.setStatus("current")
_MallocRequestScopeAddressType_Type = InetAddressType
_MallocRequestScopeAddressType_Object = MibTableColumn
mallocRequestScopeAddressType = _MallocRequestScopeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 2),
    _MallocRequestScopeAddressType_Type()
)
mallocRequestScopeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestScopeAddressType.setStatus("current")
_MallocRequestScopeFirstAddress_Type = InetAddress
_MallocRequestScopeFirstAddress_Object = MibTableColumn
mallocRequestScopeFirstAddress = _MallocRequestScopeFirstAddress_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 3),
    _MallocRequestScopeFirstAddress_Type()
)
mallocRequestScopeFirstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestScopeFirstAddress.setStatus("current")
_MallocRequestStartTime_Type = Unsigned32
_MallocRequestStartTime_Object = MibTableColumn
mallocRequestStartTime = _MallocRequestStartTime_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 4),
    _MallocRequestStartTime_Type()
)
mallocRequestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestStartTime.setStatus("current")
if mibBuilder.loadTexts:
    mallocRequestStartTime.setUnits("seconds")
_MallocRequestEndTime_Type = Unsigned32
_MallocRequestEndTime_Object = MibTableColumn
mallocRequestEndTime = _MallocRequestEndTime_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 5),
    _MallocRequestEndTime_Type()
)
mallocRequestEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestEndTime.setStatus("current")
if mibBuilder.loadTexts:
    mallocRequestEndTime.setUnits("seconds")
_MallocRequestNumAddrs_Type = Unsigned32
_MallocRequestNumAddrs_Object = MibTableColumn
mallocRequestNumAddrs = _MallocRequestNumAddrs_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 6),
    _MallocRequestNumAddrs_Type()
)
mallocRequestNumAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestNumAddrs.setStatus("current")


class _MallocRequestState_Type(Integer32):
    """Custom type mallocRequestState based on Integer32"""
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
        *(("allocated", 1),
          ("offered", 2),
          ("trying", 4),
          ("waiting", 3))
    )


_MallocRequestState_Type.__name__ = "Integer32"
_MallocRequestState_Object = MibTableColumn
mallocRequestState = _MallocRequestState_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 7),
    _MallocRequestState_Type()
)
mallocRequestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestState.setStatus("current")
_MallocRequestClientAddressType_Type = InetAddressType
_MallocRequestClientAddressType_Object = MibTableColumn
mallocRequestClientAddressType = _MallocRequestClientAddressType_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 8),
    _MallocRequestClientAddressType_Type()
)
mallocRequestClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestClientAddressType.setStatus("current")
_MallocRequestClientAddress_Type = InetAddress
_MallocRequestClientAddress_Object = MibTableColumn
mallocRequestClientAddress = _MallocRequestClientAddress_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 9),
    _MallocRequestClientAddress_Type()
)
mallocRequestClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestClientAddress.setStatus("current")
_MallocRequestServerAddressType_Type = InetAddressType
_MallocRequestServerAddressType_Object = MibTableColumn
mallocRequestServerAddressType = _MallocRequestServerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 10),
    _MallocRequestServerAddressType_Type()
)
mallocRequestServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestServerAddressType.setStatus("current")
_MallocRequestServerAddress_Type = InetAddress
_MallocRequestServerAddress_Object = MibTableColumn
mallocRequestServerAddress = _MallocRequestServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 11),
    _MallocRequestServerAddress_Type()
)
mallocRequestServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestServerAddress.setStatus("current")


class _MallocRequestLeaseIdentifier_Type(OctetString):
    """Custom type mallocRequestLeaseIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MallocRequestLeaseIdentifier_Type.__name__ = "OctetString"
_MallocRequestLeaseIdentifier_Object = MibTableColumn
mallocRequestLeaseIdentifier = _MallocRequestLeaseIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 5, 1, 12),
    _MallocRequestLeaseIdentifier_Type()
)
mallocRequestLeaseIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocRequestLeaseIdentifier.setStatus("current")
_MallocAddressTable_Object = MibTable
mallocAddressTable = _MallocAddressTable_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mallocAddressTable.setStatus("current")
_MallocAddressEntry_Object = MibTableRow
mallocAddressEntry = _MallocAddressEntry_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 6, 1)
)
mallocAddressEntry.setIndexNames(
    (0, "MALLOC-MIB", "mallocAddressAddressType"),
    (0, "MALLOC-MIB", "mallocAddressFirstAddress"),
)
if mibBuilder.loadTexts:
    mallocAddressEntry.setStatus("current")
_MallocAddressAddressType_Type = InetAddressType
_MallocAddressAddressType_Object = MibTableColumn
mallocAddressAddressType = _MallocAddressAddressType_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 6, 1, 1),
    _MallocAddressAddressType_Type()
)
mallocAddressAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mallocAddressAddressType.setStatus("current")


class _MallocAddressFirstAddress_Type(InetAddress):
    """Custom type mallocAddressFirstAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MallocAddressFirstAddress_Type.__name__ = "InetAddress"
_MallocAddressFirstAddress_Object = MibTableColumn
mallocAddressFirstAddress = _MallocAddressFirstAddress_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 6, 1, 2),
    _MallocAddressFirstAddress_Type()
)
mallocAddressFirstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mallocAddressFirstAddress.setStatus("current")
_MallocAddressNumAddrs_Type = Unsigned32
_MallocAddressNumAddrs_Object = MibTableColumn
mallocAddressNumAddrs = _MallocAddressNumAddrs_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 6, 1, 3),
    _MallocAddressNumAddrs_Type()
)
mallocAddressNumAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocAddressNumAddrs.setStatus("current")
_MallocAddressRequestId_Type = Unsigned32
_MallocAddressRequestId_Object = MibTableColumn
mallocAddressRequestId = _MallocAddressRequestId_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 1, 6, 1, 4),
    _MallocAddressRequestId_Type()
)
mallocAddressRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocAddressRequestId.setStatus("current")
_Madcap_ObjectIdentity = ObjectIdentity
madcap = _Madcap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 101, 1, 2)
)
_MadcapConfig_ObjectIdentity = ObjectIdentity
madcapConfig = _MadcapConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 1)
)
if mibBuilder.loadTexts:
    madcapConfig.setStatus("current")
_MadcapConfigExtraAllocationTime_Type = Unsigned32
_MadcapConfigExtraAllocationTime_Object = MibScalar
madcapConfigExtraAllocationTime = _MadcapConfigExtraAllocationTime_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 1, 1),
    _MadcapConfigExtraAllocationTime_Type()
)
madcapConfigExtraAllocationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madcapConfigExtraAllocationTime.setStatus("current")
if mibBuilder.loadTexts:
    madcapConfigExtraAllocationTime.setUnits("seconds")
_MadcapConfigNoResponseDelay_Type = Unsigned32
_MadcapConfigNoResponseDelay_Object = MibScalar
madcapConfigNoResponseDelay = _MadcapConfigNoResponseDelay_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 1, 2),
    _MadcapConfigNoResponseDelay_Type()
)
madcapConfigNoResponseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madcapConfigNoResponseDelay.setStatus("current")
if mibBuilder.loadTexts:
    madcapConfigNoResponseDelay.setUnits("seconds")
_MadcapConfigOfferHold_Type = Unsigned32
_MadcapConfigOfferHold_Object = MibScalar
madcapConfigOfferHold = _MadcapConfigOfferHold_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 1, 3),
    _MadcapConfigOfferHold_Type()
)
madcapConfigOfferHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madcapConfigOfferHold.setStatus("current")
if mibBuilder.loadTexts:
    madcapConfigOfferHold.setUnits("seconds")


class _MadcapConfigResponseCacheInterval_Type(Unsigned32):
    """Custom type madcapConfigResponseCacheInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_MadcapConfigResponseCacheInterval_Type.__name__ = "Unsigned32"
_MadcapConfigResponseCacheInterval_Object = MibScalar
madcapConfigResponseCacheInterval = _MadcapConfigResponseCacheInterval_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 1, 4),
    _MadcapConfigResponseCacheInterval_Type()
)
madcapConfigResponseCacheInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madcapConfigResponseCacheInterval.setStatus("current")
if mibBuilder.loadTexts:
    madcapConfigResponseCacheInterval.setUnits("seconds")
_MadcapConfigClockSkewAllowance_Type = Unsigned32
_MadcapConfigClockSkewAllowance_Object = MibScalar
madcapConfigClockSkewAllowance = _MadcapConfigClockSkewAllowance_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 1, 5),
    _MadcapConfigClockSkewAllowance_Type()
)
madcapConfigClockSkewAllowance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madcapConfigClockSkewAllowance.setStatus("current")
if mibBuilder.loadTexts:
    madcapConfigClockSkewAllowance.setUnits("seconds")
_MadcapCounters_ObjectIdentity = ObjectIdentity
madcapCounters = _MadcapCounters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2)
)
if mibBuilder.loadTexts:
    madcapCounters.setStatus("current")
_MadcapTotalErrors_Type = Counter32
_MadcapTotalErrors_Object = MibScalar
madcapTotalErrors = _MadcapTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 1),
    _MadcapTotalErrors_Type()
)
madcapTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapTotalErrors.setStatus("current")
_MadcapRequestsDenied_Type = Counter32
_MadcapRequestsDenied_Object = MibScalar
madcapRequestsDenied = _MadcapRequestsDenied_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 2),
    _MadcapRequestsDenied_Type()
)
madcapRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapRequestsDenied.setStatus("current")
_MadcapInvalidRequests_Type = Counter32
_MadcapInvalidRequests_Object = MibScalar
madcapInvalidRequests = _MadcapInvalidRequests_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 3),
    _MadcapInvalidRequests_Type()
)
madcapInvalidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapInvalidRequests.setStatus("current")
_MadcapExcessiveClockSkews_Type = Counter32
_MadcapExcessiveClockSkews_Object = MibScalar
madcapExcessiveClockSkews = _MadcapExcessiveClockSkews_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 4),
    _MadcapExcessiveClockSkews_Type()
)
madcapExcessiveClockSkews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapExcessiveClockSkews.setStatus("current")
_MadcapBadLeaseIds_Type = Counter32
_MadcapBadLeaseIds_Object = MibScalar
madcapBadLeaseIds = _MadcapBadLeaseIds_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 5),
    _MadcapBadLeaseIds_Type()
)
madcapBadLeaseIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapBadLeaseIds.setStatus("current")
_MadcapDiscovers_Type = Counter32
_MadcapDiscovers_Object = MibScalar
madcapDiscovers = _MadcapDiscovers_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 6),
    _MadcapDiscovers_Type()
)
madcapDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapDiscovers.setStatus("current")
_MadcapInforms_Type = Counter32
_MadcapInforms_Object = MibScalar
madcapInforms = _MadcapInforms_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 7),
    _MadcapInforms_Type()
)
madcapInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapInforms.setStatus("current")
_MadcapRequests_Type = Counter32
_MadcapRequests_Object = MibScalar
madcapRequests = _MadcapRequests_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 8),
    _MadcapRequests_Type()
)
madcapRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapRequests.setStatus("current")
_MadcapRenews_Type = Counter32
_MadcapRenews_Object = MibScalar
madcapRenews = _MadcapRenews_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 9),
    _MadcapRenews_Type()
)
madcapRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapRenews.setStatus("current")
_MadcapReleases_Type = Counter32
_MadcapReleases_Object = MibScalar
madcapReleases = _MadcapReleases_Object(
    (1, 3, 6, 1, 2, 1, 101, 1, 2, 2, 10),
    _MadcapReleases_Type()
)
madcapReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madcapReleases.setStatus("current")
_MallocConformance_ObjectIdentity = ObjectIdentity
mallocConformance = _MallocConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 101, 2)
)
_MallocCompliances_ObjectIdentity = ObjectIdentity
mallocCompliances = _MallocCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 101, 2, 1)
)
_MallocGroups_ObjectIdentity = ObjectIdentity
mallocGroups = _MallocGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 101, 2, 2)
)

# Managed Objects groups

mallocBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 101, 2, 2, 1)
)
mallocBasicGroup.setObjects(
      *(("MALLOC-MIB", "mallocCapabilities"),
        ("MALLOC-MIB", "mallocRequestScopeAddressType"),
        ("MALLOC-MIB", "mallocRequestScopeFirstAddress"),
        ("MALLOC-MIB", "mallocRequestStartTime"),
        ("MALLOC-MIB", "mallocRequestEndTime"),
        ("MALLOC-MIB", "mallocRequestNumAddrs"),
        ("MALLOC-MIB", "mallocRequestState"),
        ("MALLOC-MIB", "mallocAddressNumAddrs"),
        ("MALLOC-MIB", "mallocAddressRequestId"))
)
if mibBuilder.loadTexts:
    mallocBasicGroup.setStatus("current")

mallocServerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 101, 2, 2, 2)
)
mallocServerGroup.setObjects(
      *(("MALLOC-MIB", "mallocScopeLastAddress"),
        ("MALLOC-MIB", "mallocScopeHopLimit"),
        ("MALLOC-MIB", "mallocScopeSSM"),
        ("MALLOC-MIB", "mallocScopeStatus"),
        ("MALLOC-MIB", "mallocScopeStorage"),
        ("MALLOC-MIB", "mallocAllocRangeLastAddress"),
        ("MALLOC-MIB", "mallocAllocRangeLifetime"),
        ("MALLOC-MIB", "mallocAllocRangeNumAllocatedAddrs"),
        ("MALLOC-MIB", "mallocAllocRangeNumOfferedAddrs"),
        ("MALLOC-MIB", "mallocAllocRangeNumWaitingAddrs"),
        ("MALLOC-MIB", "mallocAllocRangeNumTryingAddrs"),
        ("MALLOC-MIB", "mallocAllocRangeMaxLeaseAddrs"),
        ("MALLOC-MIB", "mallocAllocRangeMaxLeaseTime"),
        ("MALLOC-MIB", "mallocAllocRangeSource"),
        ("MALLOC-MIB", "mallocAllocRangeStatus"),
        ("MALLOC-MIB", "mallocAllocRangeStorage"),
        ("MALLOC-MIB", "mallocScopeDivisible"),
        ("MALLOC-MIB", "mallocScopeSource"),
        ("MALLOC-MIB", "mallocScopeNameScopeName"),
        ("MALLOC-MIB", "mallocScopeNameDefault"),
        ("MALLOC-MIB", "mallocScopeNameStatus"),
        ("MALLOC-MIB", "mallocScopeNameStorage"),
        ("MALLOC-MIB", "mallocRequestClientAddressType"),
        ("MALLOC-MIB", "mallocRequestClientAddress"))
)
if mibBuilder.loadTexts:
    mallocServerGroup.setStatus("current")

mallocClientGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 101, 2, 2, 3)
)
mallocClientGroup.setObjects(
      *(("MALLOC-MIB", "mallocRequestServerAddressType"),
        ("MALLOC-MIB", "mallocRequestServerAddress"))
)
if mibBuilder.loadTexts:
    mallocClientGroup.setStatus("current")

madcapServerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 101, 2, 2, 4)
)
madcapServerGroup.setObjects(
      *(("MALLOC-MIB", "madcapConfigClockSkewAllowance"),
        ("MALLOC-MIB", "madcapConfigExtraAllocationTime"),
        ("MALLOC-MIB", "madcapConfigOfferHold"),
        ("MALLOC-MIB", "madcapConfigResponseCacheInterval"),
        ("MALLOC-MIB", "madcapTotalErrors"),
        ("MALLOC-MIB", "madcapRequestsDenied"),
        ("MALLOC-MIB", "madcapInvalidRequests"),
        ("MALLOC-MIB", "madcapBadLeaseIds"),
        ("MALLOC-MIB", "madcapExcessiveClockSkews"),
        ("MALLOC-MIB", "madcapDiscovers"),
        ("MALLOC-MIB", "madcapInforms"),
        ("MALLOC-MIB", "madcapRequests"),
        ("MALLOC-MIB", "madcapRenews"),
        ("MALLOC-MIB", "madcapReleases"))
)
if mibBuilder.loadTexts:
    madcapServerGroup.setStatus("current")

madcapClientGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 101, 2, 2, 5)
)
madcapClientGroup.setObjects(
      *(("MALLOC-MIB", "mallocRequestLeaseIdentifier"),
        ("MALLOC-MIB", "madcapConfigNoResponseDelay"))
)
if mibBuilder.loadTexts:
    madcapClientGroup.setStatus("current")

mallocClientScopeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 101, 2, 2, 6)
)
mallocClientScopeGroup.setObjects(
      *(("MALLOC-MIB", "mallocScopeLastAddress"),
        ("MALLOC-MIB", "mallocScopeHopLimit"),
        ("MALLOC-MIB", "mallocScopeStatus"),
        ("MALLOC-MIB", "mallocScopeStorage"),
        ("MALLOC-MIB", "mallocScopeSource"),
        ("MALLOC-MIB", "mallocScopeServerAddressType"),
        ("MALLOC-MIB", "mallocScopeServerAddress"),
        ("MALLOC-MIB", "mallocScopeSSM"),
        ("MALLOC-MIB", "mallocScopeNameScopeName"),
        ("MALLOC-MIB", "mallocScopeNameDefault"),
        ("MALLOC-MIB", "mallocScopeNameStatus"),
        ("MALLOC-MIB", "mallocScopeNameStorage"))
)
if mibBuilder.loadTexts:
    mallocClientScopeGroup.setStatus("current")

mallocPrefixCoordinatorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 101, 2, 2, 7)
)
mallocPrefixCoordinatorGroup.setObjects(
      *(("MALLOC-MIB", "mallocAllocRangeLastAddress"),
        ("MALLOC-MIB", "mallocAllocRangeLifetime"),
        ("MALLOC-MIB", "mallocAllocRangeStatus"),
        ("MALLOC-MIB", "mallocAllocRangeStorage"),
        ("MALLOC-MIB", "mallocAllocRangeSource"),
        ("MALLOC-MIB", "mallocAllocRangeTotalAllocatedAddrs"),
        ("MALLOC-MIB", "mallocAllocRangeTotalRequestedAddrs"),
        ("MALLOC-MIB", "mallocAllocRangeAdvertisable"),
        ("MALLOC-MIB", "mallocScopeLastAddress"),
        ("MALLOC-MIB", "mallocScopeDivisible"),
        ("MALLOC-MIB", "mallocScopeSource"))
)
if mibBuilder.loadTexts:
    mallocPrefixCoordinatorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mallocServerReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 101, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mallocServerReadOnlyCompliance.setStatus(
        "current"
    )

mallocClientReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 101, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mallocClientReadOnlyCompliance.setStatus(
        "current"
    )

mallocPrefixCoordinatorReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 101, 2, 1, 3)
)
if mibBuilder.loadTexts:
    mallocPrefixCoordinatorReadOnlyCompliance.setStatus(
        "current"
    )

mallocServerFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 101, 2, 1, 4)
)
if mibBuilder.loadTexts:
    mallocServerFullCompliance.setStatus(
        "current"
    )

mallocClientFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 101, 2, 1, 5)
)
if mibBuilder.loadTexts:
    mallocClientFullCompliance.setStatus(
        "current"
    )

mallocPrefixCoordinatorFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 101, 2, 1, 6)
)
if mibBuilder.loadTexts:
    mallocPrefixCoordinatorFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MALLOC-MIB",
    **{"mallocMIB": mallocMIB,
       "mallocMIBObjects": mallocMIBObjects,
       "malloc": malloc,
       "mallocCapabilities": mallocCapabilities,
       "mallocScopeTable": mallocScopeTable,
       "mallocScopeEntry": mallocScopeEntry,
       "mallocScopeAddressType": mallocScopeAddressType,
       "mallocScopeFirstAddress": mallocScopeFirstAddress,
       "mallocScopeLastAddress": mallocScopeLastAddress,
       "mallocScopeHopLimit": mallocScopeHopLimit,
       "mallocScopeStatus": mallocScopeStatus,
       "mallocScopeSource": mallocScopeSource,
       "mallocScopeDivisible": mallocScopeDivisible,
       "mallocScopeServerAddressType": mallocScopeServerAddressType,
       "mallocScopeServerAddress": mallocScopeServerAddress,
       "mallocScopeSSM": mallocScopeSSM,
       "mallocScopeStorage": mallocScopeStorage,
       "mallocScopeNameTable": mallocScopeNameTable,
       "mallocScopeNameEntry": mallocScopeNameEntry,
       "mallocScopeNameLangName": mallocScopeNameLangName,
       "mallocScopeNameScopeName": mallocScopeNameScopeName,
       "mallocScopeNameDefault": mallocScopeNameDefault,
       "mallocScopeNameStatus": mallocScopeNameStatus,
       "mallocScopeNameStorage": mallocScopeNameStorage,
       "mallocAllocRangeTable": mallocAllocRangeTable,
       "mallocAllocRangeEntry": mallocAllocRangeEntry,
       "mallocAllocRangeFirstAddress": mallocAllocRangeFirstAddress,
       "mallocAllocRangeLastAddress": mallocAllocRangeLastAddress,
       "mallocAllocRangeStatus": mallocAllocRangeStatus,
       "mallocAllocRangeSource": mallocAllocRangeSource,
       "mallocAllocRangeLifetime": mallocAllocRangeLifetime,
       "mallocAllocRangeMaxLeaseAddrs": mallocAllocRangeMaxLeaseAddrs,
       "mallocAllocRangeMaxLeaseTime": mallocAllocRangeMaxLeaseTime,
       "mallocAllocRangeNumAllocatedAddrs": mallocAllocRangeNumAllocatedAddrs,
       "mallocAllocRangeNumOfferedAddrs": mallocAllocRangeNumOfferedAddrs,
       "mallocAllocRangeNumWaitingAddrs": mallocAllocRangeNumWaitingAddrs,
       "mallocAllocRangeNumTryingAddrs": mallocAllocRangeNumTryingAddrs,
       "mallocAllocRangeAdvertisable": mallocAllocRangeAdvertisable,
       "mallocAllocRangeTotalAllocatedAddrs": mallocAllocRangeTotalAllocatedAddrs,
       "mallocAllocRangeTotalRequestedAddrs": mallocAllocRangeTotalRequestedAddrs,
       "mallocAllocRangeStorage": mallocAllocRangeStorage,
       "mallocRequestTable": mallocRequestTable,
       "mallocRequestEntry": mallocRequestEntry,
       "mallocRequestId": mallocRequestId,
       "mallocRequestScopeAddressType": mallocRequestScopeAddressType,
       "mallocRequestScopeFirstAddress": mallocRequestScopeFirstAddress,
       "mallocRequestStartTime": mallocRequestStartTime,
       "mallocRequestEndTime": mallocRequestEndTime,
       "mallocRequestNumAddrs": mallocRequestNumAddrs,
       "mallocRequestState": mallocRequestState,
       "mallocRequestClientAddressType": mallocRequestClientAddressType,
       "mallocRequestClientAddress": mallocRequestClientAddress,
       "mallocRequestServerAddressType": mallocRequestServerAddressType,
       "mallocRequestServerAddress": mallocRequestServerAddress,
       "mallocRequestLeaseIdentifier": mallocRequestLeaseIdentifier,
       "mallocAddressTable": mallocAddressTable,
       "mallocAddressEntry": mallocAddressEntry,
       "mallocAddressAddressType": mallocAddressAddressType,
       "mallocAddressFirstAddress": mallocAddressFirstAddress,
       "mallocAddressNumAddrs": mallocAddressNumAddrs,
       "mallocAddressRequestId": mallocAddressRequestId,
       "madcap": madcap,
       "madcapConfig": madcapConfig,
       "madcapConfigExtraAllocationTime": madcapConfigExtraAllocationTime,
       "madcapConfigNoResponseDelay": madcapConfigNoResponseDelay,
       "madcapConfigOfferHold": madcapConfigOfferHold,
       "madcapConfigResponseCacheInterval": madcapConfigResponseCacheInterval,
       "madcapConfigClockSkewAllowance": madcapConfigClockSkewAllowance,
       "madcapCounters": madcapCounters,
       "madcapTotalErrors": madcapTotalErrors,
       "madcapRequestsDenied": madcapRequestsDenied,
       "madcapInvalidRequests": madcapInvalidRequests,
       "madcapExcessiveClockSkews": madcapExcessiveClockSkews,
       "madcapBadLeaseIds": madcapBadLeaseIds,
       "madcapDiscovers": madcapDiscovers,
       "madcapInforms": madcapInforms,
       "madcapRequests": madcapRequests,
       "madcapRenews": madcapRenews,
       "madcapReleases": madcapReleases,
       "mallocConformance": mallocConformance,
       "mallocCompliances": mallocCompliances,
       "mallocServerReadOnlyCompliance": mallocServerReadOnlyCompliance,
       "mallocClientReadOnlyCompliance": mallocClientReadOnlyCompliance,
       "mallocPrefixCoordinatorReadOnlyCompliance": mallocPrefixCoordinatorReadOnlyCompliance,
       "mallocServerFullCompliance": mallocServerFullCompliance,
       "mallocClientFullCompliance": mallocClientFullCompliance,
       "mallocPrefixCoordinatorFullCompliance": mallocPrefixCoordinatorFullCompliance,
       "mallocGroups": mallocGroups,
       "mallocBasicGroup": mallocBasicGroup,
       "mallocServerGroup": mallocServerGroup,
       "mallocClientGroup": mallocClientGroup,
       "madcapServerGroup": madcapServerGroup,
       "madcapClientGroup": madcapClientGroup,
       "mallocClientScopeGroup": mallocClientScopeGroup,
       "mallocPrefixCoordinatorGroup": mallocPrefixCoordinatorGroup}
)
