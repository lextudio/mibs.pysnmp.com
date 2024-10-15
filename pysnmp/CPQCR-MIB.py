# SNMP MIB module (CPQCR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQCR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:17 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqClusteredRAID_ObjectIdentity = ObjectIdentity
cpqClusteredRAID = _CpqClusteredRAID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141)
)
_CpqCrMibRev_ObjectIdentity = ObjectIdentity
cpqCrMibRev = _CpqCrMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 1)
)


class _CpqCrMibRevMajor_Type(Integer32):
    """Custom type cpqCrMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqCrMibRevMajor_Type.__name__ = "Integer32"
_CpqCrMibRevMajor_Object = MibScalar
cpqCrMibRevMajor = _CpqCrMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 1, 1),
    _CpqCrMibRevMajor_Type()
)
cpqCrMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrMibRevMajor.setStatus("mandatory")


class _CpqCrMibRevMinor_Type(Integer32):
    """Custom type cpqCrMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqCrMibRevMinor_Type.__name__ = "Integer32"
_CpqCrMibRevMinor_Object = MibScalar
cpqCrMibRevMinor = _CpqCrMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 1, 2),
    _CpqCrMibRevMinor_Type()
)
cpqCrMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrMibRevMinor.setStatus("mandatory")


class _CpqCrMibCondition_Type(Integer32):
    """Custom type cpqCrMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrMibCondition_Type.__name__ = "Integer32"
_CpqCrMibCondition_Object = MibScalar
cpqCrMibCondition = _CpqCrMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 1, 3),
    _CpqCrMibCondition_Type()
)
cpqCrMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrMibCondition.setStatus("mandatory")
_CpqCrComponent_ObjectIdentity = ObjectIdentity
cpqCrComponent = _CpqCrComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2)
)
_CpqCrInterface_ObjectIdentity = ObjectIdentity
cpqCrInterface = _CpqCrInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 1)
)
_CpqCrOsCommon_ObjectIdentity = ObjectIdentity
cpqCrOsCommon = _CpqCrOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 1, 4)
)


class _CpqCrOsCommonPollFreq_Type(Integer32):
    """Custom type cpqCrOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqCrOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqCrOsCommonPollFreq_Object = MibScalar
cpqCrOsCommonPollFreq = _CpqCrOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 1, 4, 1),
    _CpqCrOsCommonPollFreq_Type()
)
cpqCrOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCrOsCommonPollFreq.setStatus("mandatory")
_CpqCrCntlr_ObjectIdentity = ObjectIdentity
cpqCrCntlr = _CpqCrCntlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2)
)
_CpqCrCntlrTable_Object = MibTable
cpqCrCntlrTable = _CpqCrCntlrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqCrCntlrTable.setStatus("mandatory")
_CpqCrCntlrEntry_Object = MibTableRow
cpqCrCntlrEntry = _CpqCrCntlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1)
)
cpqCrCntlrEntry.setIndexNames(
    (0, "CPQCR-MIB", "cpqCrCntlrIndex"),
)
if mibBuilder.loadTexts:
    cpqCrCntlrEntry.setStatus("mandatory")


class _CpqCrCntlrIndex_Type(Integer32):
    """Custom type cpqCrCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrCntlrIndex_Type.__name__ = "Integer32"
_CpqCrCntlrIndex_Object = MibTableColumn
cpqCrCntlrIndex = _CpqCrCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 1),
    _CpqCrCntlrIndex_Type()
)
cpqCrCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrIndex.setStatus("mandatory")


class _CpqCrCntlrSerialNumber_Type(DisplayString):
    """Custom type cpqCrCntlrSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqCrCntlrSerialNumber_Type.__name__ = "DisplayString"
_CpqCrCntlrSerialNumber_Object = MibTableColumn
cpqCrCntlrSerialNumber = _CpqCrCntlrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 2),
    _CpqCrCntlrSerialNumber_Type()
)
cpqCrCntlrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrSerialNumber.setStatus("mandatory")


class _CpqCrCntlrFWRev_Type(DisplayString):
    """Custom type cpqCrCntlrFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqCrCntlrFWRev_Type.__name__ = "DisplayString"
_CpqCrCntlrFWRev_Object = MibTableColumn
cpqCrCntlrFWRev = _CpqCrCntlrFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 3),
    _CpqCrCntlrFWRev_Type()
)
cpqCrCntlrFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrFWRev.setStatus("mandatory")


class _CpqCrCntlrCondition_Type(Integer32):
    """Custom type cpqCrCntlrCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrCntlrCondition_Type.__name__ = "Integer32"
_CpqCrCntlrCondition_Object = MibTableColumn
cpqCrCntlrCondition = _CpqCrCntlrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 4),
    _CpqCrCntlrCondition_Type()
)
cpqCrCntlrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrCondition.setStatus("mandatory")


class _CpqCrCntlrCurrentRole_Type(Integer32):
    """Custom type cpqCrCntlrCurrentRole based on Integer32"""
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
        *(("active", 3),
          ("backup", 4),
          ("notDuplexed", 2),
          ("other", 1))
    )


_CpqCrCntlrCurrentRole_Type.__name__ = "Integer32"
_CpqCrCntlrCurrentRole_Object = MibTableColumn
cpqCrCntlrCurrentRole = _CpqCrCntlrCurrentRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 8),
    _CpqCrCntlrCurrentRole_Type()
)
cpqCrCntlrCurrentRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrCurrentRole.setStatus("mandatory")


class _CpqCrCntlrDriveOwnership_Type(Integer32):
    """Custom type cpqCrCntlrDriveOwnership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOwner", 3),
          ("other", 1),
          ("owner", 2))
    )


_CpqCrCntlrDriveOwnership_Type.__name__ = "Integer32"
_CpqCrCntlrDriveOwnership_Object = MibTableColumn
cpqCrCntlrDriveOwnership = _CpqCrCntlrDriveOwnership_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 9),
    _CpqCrCntlrDriveOwnership_Type()
)
cpqCrCntlrDriveOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrDriveOwnership.setStatus("mandatory")


class _CpqCrCntlrRebuildRate_Type(Integer32):
    """Custom type cpqCrCntlrRebuildRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpqCrCntlrRebuildRate_Type.__name__ = "Integer32"
_CpqCrCntlrRebuildRate_Object = MibTableColumn
cpqCrCntlrRebuildRate = _CpqCrCntlrRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 10),
    _CpqCrCntlrRebuildRate_Type()
)
cpqCrCntlrRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrRebuildRate.setStatus("mandatory")


class _CpqCrCntlrCreateRate_Type(Integer32):
    """Custom type cpqCrCntlrCreateRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpqCrCntlrCreateRate_Type.__name__ = "Integer32"
_CpqCrCntlrCreateRate_Object = MibTableColumn
cpqCrCntlrCreateRate = _CpqCrCntlrCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 11),
    _CpqCrCntlrCreateRate_Type()
)
cpqCrCntlrCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrCreateRate.setStatus("mandatory")


class _CpqCrCntlrCacheSize_Type(Integer32):
    """Custom type cpqCrCntlrCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_CpqCrCntlrCacheSize_Type.__name__ = "Integer32"
_CpqCrCntlrCacheSize_Object = MibTableColumn
cpqCrCntlrCacheSize = _CpqCrCntlrCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 12),
    _CpqCrCntlrCacheSize_Type()
)
cpqCrCntlrCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrCacheSize.setStatus("mandatory")


class _CpqCrCntlrSimmSizeA_Type(Integer32):
    """Custom type cpqCrCntlrSimmSizeA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CpqCrCntlrSimmSizeA_Type.__name__ = "Integer32"
_CpqCrCntlrSimmSizeA_Object = MibTableColumn
cpqCrCntlrSimmSizeA = _CpqCrCntlrSimmSizeA_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 13),
    _CpqCrCntlrSimmSizeA_Type()
)
cpqCrCntlrSimmSizeA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrSimmSizeA.setStatus("mandatory")


class _CpqCrCntlrSimmSizeB_Type(Integer32):
    """Custom type cpqCrCntlrSimmSizeB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CpqCrCntlrSimmSizeB_Type.__name__ = "Integer32"
_CpqCrCntlrSimmSizeB_Object = MibTableColumn
cpqCrCntlrSimmSizeB = _CpqCrCntlrSimmSizeB_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 2, 1, 1, 14),
    _CpqCrCntlrSimmSizeB_Type()
)
cpqCrCntlrSimmSizeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrCntlrSimmSizeB.setStatus("mandatory")
_CpqCrLogDrv_ObjectIdentity = ObjectIdentity
cpqCrLogDrv = _CpqCrLogDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3)
)
_CpqCrLogDrvTable_Object = MibTable
cpqCrLogDrvTable = _CpqCrLogDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqCrLogDrvTable.setStatus("mandatory")
_CpqCrLogDrvEntry_Object = MibTableRow
cpqCrLogDrvEntry = _CpqCrLogDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1)
)
cpqCrLogDrvEntry.setIndexNames(
    (0, "CPQCR-MIB", "cpqCrLogDrvCntlrIndex"),
    (0, "CPQCR-MIB", "cpqCrLogDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqCrLogDrvEntry.setStatus("mandatory")


class _CpqCrLogDrvCntlrIndex_Type(Integer32):
    """Custom type cpqCrLogDrvCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrLogDrvCntlrIndex_Type.__name__ = "Integer32"
_CpqCrLogDrvCntlrIndex_Object = MibTableColumn
cpqCrLogDrvCntlrIndex = _CpqCrLogDrvCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 1),
    _CpqCrLogDrvCntlrIndex_Type()
)
cpqCrLogDrvCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvCntlrIndex.setStatus("mandatory")


class _CpqCrLogDrvIndex_Type(Integer32):
    """Custom type cpqCrLogDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrLogDrvIndex_Type.__name__ = "Integer32"
_CpqCrLogDrvIndex_Object = MibTableColumn
cpqCrLogDrvIndex = _CpqCrLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 2),
    _CpqCrLogDrvIndex_Type()
)
cpqCrLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvIndex.setStatus("mandatory")


class _CpqCrLogDrvRAIDLevel_Type(Integer32):
    """Custom type cpqCrLogDrvRAIDLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("jbod", 2),
          ("other", 1),
          ("raid0", 3),
          ("raid0plus1", 5),
          ("raid1", 4),
          ("raid4", 6),
          ("raid5", 7))
    )


_CpqCrLogDrvRAIDLevel_Type.__name__ = "Integer32"
_CpqCrLogDrvRAIDLevel_Object = MibTableColumn
cpqCrLogDrvRAIDLevel = _CpqCrLogDrvRAIDLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 3),
    _CpqCrLogDrvRAIDLevel_Type()
)
cpqCrLogDrvRAIDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvRAIDLevel.setStatus("mandatory")


class _CpqCrLogDrvStatus_Type(Integer32):
    """Custom type cpqCrLogDrvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("good", 2),
          ("initializing", 6),
          ("other", 1),
          ("reconstructing", 5),
          ("reduced", 3))
    )


_CpqCrLogDrvStatus_Type.__name__ = "Integer32"
_CpqCrLogDrvStatus_Object = MibTableColumn
cpqCrLogDrvStatus = _CpqCrLogDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 4),
    _CpqCrLogDrvStatus_Type()
)
cpqCrLogDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvStatus.setStatus("mandatory")


class _CpqCrLogDrvRebuildPercentage_Type(Integer32):
    """Custom type cpqCrLogDrvRebuildPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqCrLogDrvRebuildPercentage_Type.__name__ = "Integer32"
_CpqCrLogDrvRebuildPercentage_Object = MibTableColumn
cpqCrLogDrvRebuildPercentage = _CpqCrLogDrvRebuildPercentage_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 5),
    _CpqCrLogDrvRebuildPercentage_Type()
)
cpqCrLogDrvRebuildPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvRebuildPercentage.setStatus("mandatory")


class _CpqCrLogDrvAvailSpares_Type(OctetString):
    """Custom type cpqCrLogDrvAvailSpares based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqCrLogDrvAvailSpares_Type.__name__ = "OctetString"
_CpqCrLogDrvAvailSpares_Object = MibTableColumn
cpqCrLogDrvAvailSpares = _CpqCrLogDrvAvailSpares_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 7),
    _CpqCrLogDrvAvailSpares_Type()
)
cpqCrLogDrvAvailSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvAvailSpares.setStatus("mandatory")


class _CpqCrLogDrvSize_Type(Integer32):
    """Custom type cpqCrLogDrvSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqCrLogDrvSize_Type.__name__ = "Integer32"
_CpqCrLogDrvSize_Object = MibTableColumn
cpqCrLogDrvSize = _CpqCrLogDrvSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 8),
    _CpqCrLogDrvSize_Type()
)
cpqCrLogDrvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvSize.setStatus("mandatory")


class _CpqCrLogDrvPhyDrvIDs_Type(OctetString):
    """Custom type cpqCrLogDrvPhyDrvIDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqCrLogDrvPhyDrvIDs_Type.__name__ = "OctetString"
_CpqCrLogDrvPhyDrvIDs_Object = MibTableColumn
cpqCrLogDrvPhyDrvIDs = _CpqCrLogDrvPhyDrvIDs_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 9),
    _CpqCrLogDrvPhyDrvIDs_Type()
)
cpqCrLogDrvPhyDrvIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvPhyDrvIDs.setStatus("mandatory")


class _CpqCrLogDrvCondition_Type(Integer32):
    """Custom type cpqCrLogDrvCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrLogDrvCondition_Type.__name__ = "Integer32"
_CpqCrLogDrvCondition_Object = MibTableColumn
cpqCrLogDrvCondition = _CpqCrLogDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 10),
    _CpqCrLogDrvCondition_Type()
)
cpqCrLogDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvCondition.setStatus("mandatory")


class _CpqCrLogDrvPartitionIDs_Type(OctetString):
    """Custom type cpqCrLogDrvPartitionIDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqCrLogDrvPartitionIDs_Type.__name__ = "OctetString"
_CpqCrLogDrvPartitionIDs_Object = MibTableColumn
cpqCrLogDrvPartitionIDs = _CpqCrLogDrvPartitionIDs_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 3, 1, 1, 11),
    _CpqCrLogDrvPartitionIDs_Type()
)
cpqCrLogDrvPartitionIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrLogDrvPartitionIDs.setStatus("mandatory")
_CpqCrSpareDrv_ObjectIdentity = ObjectIdentity
cpqCrSpareDrv = _CpqCrSpareDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 4)
)
_CpqCrSpareTable_Object = MibTable
cpqCrSpareTable = _CpqCrSpareTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqCrSpareTable.setStatus("mandatory")
_CpqCrSpareEntry_Object = MibTableRow
cpqCrSpareEntry = _CpqCrSpareEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 4, 1, 1)
)
cpqCrSpareEntry.setIndexNames(
    (0, "CPQCR-MIB", "cpqCrSpareCntlrIndex"),
    (0, "CPQCR-MIB", "cpqCrSparePhyDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqCrSpareEntry.setStatus("mandatory")


class _CpqCrSpareCntlrIndex_Type(Integer32):
    """Custom type cpqCrSpareCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrSpareCntlrIndex_Type.__name__ = "Integer32"
_CpqCrSpareCntlrIndex_Object = MibTableColumn
cpqCrSpareCntlrIndex = _CpqCrSpareCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 4, 1, 1, 1),
    _CpqCrSpareCntlrIndex_Type()
)
cpqCrSpareCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrSpareCntlrIndex.setStatus("mandatory")


class _CpqCrSparePhyDrvIndex_Type(Integer32):
    """Custom type cpqCrSparePhyDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrSparePhyDrvIndex_Type.__name__ = "Integer32"
_CpqCrSparePhyDrvIndex_Object = MibTableColumn
cpqCrSparePhyDrvIndex = _CpqCrSparePhyDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 4, 1, 1, 2),
    _CpqCrSparePhyDrvIndex_Type()
)
cpqCrSparePhyDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrSparePhyDrvIndex.setStatus("mandatory")


class _CpqCrSpareStatus_Type(Integer32):
    """Custom type cpqCrSpareStatus based on Integer32"""
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
        *(("addingSpare", 9),
          ("creating", 7),
          ("empty", 2),
          ("formatting", 10),
          ("hotSpare", 5),
          ("offline", 3),
          ("online", 4),
          ("other", 1),
          ("rebuilding", 8),
          ("warmSpare", 6))
    )


_CpqCrSpareStatus_Type.__name__ = "Integer32"
_CpqCrSpareStatus_Object = MibTableColumn
cpqCrSpareStatus = _CpqCrSpareStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 4, 1, 1, 3),
    _CpqCrSpareStatus_Type()
)
cpqCrSpareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrSpareStatus.setStatus("mandatory")


class _CpqCrSpareCondition_Type(Integer32):
    """Custom type cpqCrSpareCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrSpareCondition_Type.__name__ = "Integer32"
_CpqCrSpareCondition_Object = MibTableColumn
cpqCrSpareCondition = _CpqCrSpareCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 4, 1, 1, 4),
    _CpqCrSpareCondition_Type()
)
cpqCrSpareCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrSpareCondition.setStatus("mandatory")


class _CpqCrSpareScsiID_Type(Integer32):
    """Custom type cpqCrSpareScsiID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrSpareScsiID_Type.__name__ = "Integer32"
_CpqCrSpareScsiID_Object = MibTableColumn
cpqCrSpareScsiID = _CpqCrSpareScsiID_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 4, 1, 1, 5),
    _CpqCrSpareScsiID_Type()
)
cpqCrSpareScsiID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrSpareScsiID.setStatus("mandatory")
_CpqCrPhyDrv_ObjectIdentity = ObjectIdentity
cpqCrPhyDrv = _CpqCrPhyDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5)
)
_CpqCrPhyDrvTable_Object = MibTable
cpqCrPhyDrvTable = _CpqCrPhyDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqCrPhyDrvTable.setStatus("mandatory")
_CpqCrPhyDrvEntry_Object = MibTableRow
cpqCrPhyDrvEntry = _CpqCrPhyDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1)
)
cpqCrPhyDrvEntry.setIndexNames(
    (0, "CPQCR-MIB", "cpqCrPhyDrvCntlrIndex"),
    (0, "CPQCR-MIB", "cpqCrPhyDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqCrPhyDrvEntry.setStatus("mandatory")


class _CpqCrPhyDrvCntlrIndex_Type(Integer32):
    """Custom type cpqCrPhyDrvCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrPhyDrvCntlrIndex_Type.__name__ = "Integer32"
_CpqCrPhyDrvCntlrIndex_Object = MibTableColumn
cpqCrPhyDrvCntlrIndex = _CpqCrPhyDrvCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1, 1),
    _CpqCrPhyDrvCntlrIndex_Type()
)
cpqCrPhyDrvCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPhyDrvCntlrIndex.setStatus("mandatory")


class _CpqCrPhyDrvIndex_Type(Integer32):
    """Custom type cpqCrPhyDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrPhyDrvIndex_Type.__name__ = "Integer32"
_CpqCrPhyDrvIndex_Object = MibTableColumn
cpqCrPhyDrvIndex = _CpqCrPhyDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1, 2),
    _CpqCrPhyDrvIndex_Type()
)
cpqCrPhyDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPhyDrvIndex.setStatus("mandatory")


class _CpqCrPhyDrvVendor_Type(DisplayString):
    """Custom type cpqCrPhyDrvVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqCrPhyDrvVendor_Type.__name__ = "DisplayString"
_CpqCrPhyDrvVendor_Object = MibTableColumn
cpqCrPhyDrvVendor = _CpqCrPhyDrvVendor_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1, 3),
    _CpqCrPhyDrvVendor_Type()
)
cpqCrPhyDrvVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPhyDrvVendor.setStatus("mandatory")


class _CpqCrPhyDrvModel_Type(DisplayString):
    """Custom type cpqCrPhyDrvModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqCrPhyDrvModel_Type.__name__ = "DisplayString"
_CpqCrPhyDrvModel_Object = MibTableColumn
cpqCrPhyDrvModel = _CpqCrPhyDrvModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1, 4),
    _CpqCrPhyDrvModel_Type()
)
cpqCrPhyDrvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPhyDrvModel.setStatus("mandatory")


class _CpqCrPhyDrvRevision_Type(DisplayString):
    """Custom type cpqCrPhyDrvRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqCrPhyDrvRevision_Type.__name__ = "DisplayString"
_CpqCrPhyDrvRevision_Object = MibTableColumn
cpqCrPhyDrvRevision = _CpqCrPhyDrvRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1, 5),
    _CpqCrPhyDrvRevision_Type()
)
cpqCrPhyDrvRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPhyDrvRevision.setStatus("mandatory")


class _CpqCrPhyDrvStatus_Type(Integer32):
    """Custom type cpqCrPhyDrvStatus based on Integer32"""
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
        *(("addingSpare", 9),
          ("creating", 7),
          ("empty", 2),
          ("formatting", 10),
          ("hotSpare", 5),
          ("offline", 3),
          ("online", 4),
          ("other", 1),
          ("rebuilding", 8),
          ("warmSpare", 6))
    )


_CpqCrPhyDrvStatus_Type.__name__ = "Integer32"
_CpqCrPhyDrvStatus_Object = MibTableColumn
cpqCrPhyDrvStatus = _CpqCrPhyDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1, 6),
    _CpqCrPhyDrvStatus_Type()
)
cpqCrPhyDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPhyDrvStatus.setStatus("mandatory")
_CpqCrPhyDrvSize_Type = Integer32
_CpqCrPhyDrvSize_Object = MibTableColumn
cpqCrPhyDrvSize = _CpqCrPhyDrvSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1, 7),
    _CpqCrPhyDrvSize_Type()
)
cpqCrPhyDrvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPhyDrvSize.setStatus("mandatory")


class _CpqCrPhyDrvCondition_Type(Integer32):
    """Custom type cpqCrPhyDrvCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrPhyDrvCondition_Type.__name__ = "Integer32"
_CpqCrPhyDrvCondition_Object = MibTableColumn
cpqCrPhyDrvCondition = _CpqCrPhyDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1, 8),
    _CpqCrPhyDrvCondition_Type()
)
cpqCrPhyDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPhyDrvCondition.setStatus("mandatory")


class _CpqCrPhyDrvScsiID_Type(Integer32):
    """Custom type cpqCrPhyDrvScsiID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrPhyDrvScsiID_Type.__name__ = "Integer32"
_CpqCrPhyDrvScsiID_Object = MibTableColumn
cpqCrPhyDrvScsiID = _CpqCrPhyDrvScsiID_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 5, 1, 1, 9),
    _CpqCrPhyDrvScsiID_Type()
)
cpqCrPhyDrvScsiID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPhyDrvScsiID.setStatus("mandatory")
_CpqCrEMU_ObjectIdentity = ObjectIdentity
cpqCrEMU = _CpqCrEMU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7)
)


class _CpqCrEMUBoardTemperatureStatus_Type(Integer32):
    """Custom type cpqCrEMUBoardTemperatureStatus based on Integer32"""
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
        *(("emuBoardTempAboveNormal", 5),
          ("emuBoardTempBackToNormal", 8),
          ("emuBoardTempBelowNormal", 4),
          ("emuBoardTempFarAboveNormal", 7),
          ("emuBoardTempFarBelowNormal", 6),
          ("emuBoardTempNormal", 3),
          ("emuBoardTempNotInstalled", 2),
          ("other", 1))
    )


_CpqCrEMUBoardTemperatureStatus_Type.__name__ = "Integer32"
_CpqCrEMUBoardTemperatureStatus_Object = MibScalar
cpqCrEMUBoardTemperatureStatus = _CpqCrEMUBoardTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 1),
    _CpqCrEMUBoardTemperatureStatus_Type()
)
cpqCrEMUBoardTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUBoardTemperatureStatus.setStatus("deprecated")


class _CpqCrEMUEnclosureTemperatureStatus_Type(Integer32):
    """Custom type cpqCrEMUEnclosureTemperatureStatus based on Integer32"""
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
        *(("emuEnclosureTempAboveNormal", 5),
          ("emuEnclosureTempBackToNormal", 8),
          ("emuEnclosureTempBelowNormal", 4),
          ("emuEnclosureTempFarAboveNormal", 7),
          ("emuEnclosureTempFarBelowNormal", 6),
          ("emuEnclosureTempNormal", 3),
          ("emuEnclosureTempNotInstalled", 2),
          ("other", 1))
    )


_CpqCrEMUEnclosureTemperatureStatus_Type.__name__ = "Integer32"
_CpqCrEMUEnclosureTemperatureStatus_Object = MibScalar
cpqCrEMUEnclosureTemperatureStatus = _CpqCrEMUEnclosureTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 2),
    _CpqCrEMUEnclosureTemperatureStatus_Type()
)
cpqCrEMUEnclosureTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUEnclosureTemperatureStatus.setStatus("deprecated")


class _CpqCrEMUBoardTemperatureLevel_Type(Integer32):
    """Custom type cpqCrEMUBoardTemperatureLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrEMUBoardTemperatureLevel_Type.__name__ = "Integer32"
_CpqCrEMUBoardTemperatureLevel_Object = MibScalar
cpqCrEMUBoardTemperatureLevel = _CpqCrEMUBoardTemperatureLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 3),
    _CpqCrEMUBoardTemperatureLevel_Type()
)
cpqCrEMUBoardTemperatureLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUBoardTemperatureLevel.setStatus("deprecated")


class _CpqCrEMUEnclosureTemperatureLevel_Type(Integer32):
    """Custom type cpqCrEMUEnclosureTemperatureLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrEMUEnclosureTemperatureLevel_Type.__name__ = "Integer32"
_CpqCrEMUEnclosureTemperatureLevel_Object = MibScalar
cpqCrEMUEnclosureTemperatureLevel = _CpqCrEMUEnclosureTemperatureLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 4),
    _CpqCrEMUEnclosureTemperatureLevel_Type()
)
cpqCrEMUEnclosureTemperatureLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUEnclosureTemperatureLevel.setStatus("deprecated")


class _CpqCrEMUCondition_Type(Integer32):
    """Custom type cpqCrEMUCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrEMUCondition_Type.__name__ = "Integer32"
_CpqCrEMUCondition_Object = MibScalar
cpqCrEMUCondition = _CpqCrEMUCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 5),
    _CpqCrEMUCondition_Type()
)
cpqCrEMUCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUCondition.setStatus("mandatory")


class _CpqCrEMUFanStatus_Type(Integer32):
    """Custom type cpqCrEMUFanStatus based on Integer32"""
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
        *(("emuFanCritical", 3),
          ("emuFanOK", 2),
          ("emuFanUnknown", 4),
          ("other", 1))
    )


_CpqCrEMUFanStatus_Type.__name__ = "Integer32"
_CpqCrEMUFanStatus_Object = MibScalar
cpqCrEMUFanStatus = _CpqCrEMUFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 6),
    _CpqCrEMUFanStatus_Type()
)
cpqCrEMUFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUFanStatus.setStatus("mandatory")


class _CpqCrEMUFanCondition_Type(Integer32):
    """Custom type cpqCrEMUFanCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrEMUFanCondition_Type.__name__ = "Integer32"
_CpqCrEMUFanCondition_Object = MibScalar
cpqCrEMUFanCondition = _CpqCrEMUFanCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 7),
    _CpqCrEMUFanCondition_Type()
)
cpqCrEMUFanCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUFanCondition.setStatus("mandatory")


class _CpqCrEMUPowerSupplyStatus_Type(Integer32):
    """Custom type cpqCrEMUPowerSupplyStatus based on Integer32"""
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
        *(("emuPwrSupplyCritical", 3),
          ("emuPwrSupplyNotInstalled", 4),
          ("emuPwrSupplyOK", 2),
          ("emuPwrSupplyUnknown", 5),
          ("other", 1))
    )


_CpqCrEMUPowerSupplyStatus_Type.__name__ = "Integer32"
_CpqCrEMUPowerSupplyStatus_Object = MibScalar
cpqCrEMUPowerSupplyStatus = _CpqCrEMUPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 8),
    _CpqCrEMUPowerSupplyStatus_Type()
)
cpqCrEMUPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUPowerSupplyStatus.setStatus("mandatory")


class _CpqCrEMUPowerSupplyCondition_Type(Integer32):
    """Custom type cpqCrEMUPowerSupplyCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrEMUPowerSupplyCondition_Type.__name__ = "Integer32"
_CpqCrEMUPowerSupplyCondition_Object = MibScalar
cpqCrEMUPowerSupplyCondition = _CpqCrEMUPowerSupplyCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 9),
    _CpqCrEMUPowerSupplyCondition_Type()
)
cpqCrEMUPowerSupplyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUPowerSupplyCondition.setStatus("mandatory")


class _CpqCrEMUTemperatureStatus_Type(Integer32):
    """Custom type cpqCrEMUTemperatureStatus based on Integer32"""
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
        *(("emuTempCritical", 3),
          ("emuTempNonCritical", 4),
          ("emuTempOK", 2),
          ("emuTempUnknown", 5),
          ("other", 1))
    )


_CpqCrEMUTemperatureStatus_Type.__name__ = "Integer32"
_CpqCrEMUTemperatureStatus_Object = MibScalar
cpqCrEMUTemperatureStatus = _CpqCrEMUTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 10),
    _CpqCrEMUTemperatureStatus_Type()
)
cpqCrEMUTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUTemperatureStatus.setStatus("mandatory")


class _CpqCrEMUTemperatureLevel_Type(Integer32):
    """Custom type cpqCrEMUTemperatureLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrEMUTemperatureLevel_Type.__name__ = "Integer32"
_CpqCrEMUTemperatureLevel_Object = MibScalar
cpqCrEMUTemperatureLevel = _CpqCrEMUTemperatureLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 11),
    _CpqCrEMUTemperatureLevel_Type()
)
cpqCrEMUTemperatureLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUTemperatureLevel.setStatus("mandatory")


class _CpqCrEMUTemperatureCondition_Type(Integer32):
    """Custom type cpqCrEMUTemperatureCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrEMUTemperatureCondition_Type.__name__ = "Integer32"
_CpqCrEMUTemperatureCondition_Object = MibScalar
cpqCrEMUTemperatureCondition = _CpqCrEMUTemperatureCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 7, 12),
    _CpqCrEMUTemperatureCondition_Type()
)
cpqCrEMUTemperatureCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrEMUTemperatureCondition.setStatus("mandatory")
_CpqCrExpCab_ObjectIdentity = ObjectIdentity
cpqCrExpCab = _CpqCrExpCab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 8)
)


class _CpqCrExpCabPowerSupplyStatus_Type(Integer32):
    """Custom type cpqCrExpCabPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("expCabPwrSupplyNonCritical", 3),
          ("expCabPwrSupplyOK", 2),
          ("expCabPwrSupplyUnknown", 5),
          ("other", 1))
    )


_CpqCrExpCabPowerSupplyStatus_Type.__name__ = "Integer32"
_CpqCrExpCabPowerSupplyStatus_Object = MibScalar
cpqCrExpCabPowerSupplyStatus = _CpqCrExpCabPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 8, 1),
    _CpqCrExpCabPowerSupplyStatus_Type()
)
cpqCrExpCabPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrExpCabPowerSupplyStatus.setStatus("mandatory")


class _CpqCrExpCabFanStatus_Type(Integer32):
    """Custom type cpqCrExpCabFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("expCabFanNonCritical", 4),
          ("expCabFanNotInstalled", 5),
          ("expCabFanOK", 2),
          ("expCabFanUnknown", 6),
          ("other", 1))
    )


_CpqCrExpCabFanStatus_Type.__name__ = "Integer32"
_CpqCrExpCabFanStatus_Object = MibScalar
cpqCrExpCabFanStatus = _CpqCrExpCabFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 8, 2),
    _CpqCrExpCabFanStatus_Type()
)
cpqCrExpCabFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrExpCabFanStatus.setStatus("mandatory")


class _CpqCrExpCabTemperatureStatus_Type(Integer32):
    """Custom type cpqCrExpCabTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("expCabTempCritical", 3),
          ("expCabTempNonCritical", 4),
          ("expCabTempNotInstalled", 5),
          ("expCabTempOK", 2),
          ("expCabTempUnknown", 6),
          ("other", 1))
    )


_CpqCrExpCabTemperatureStatus_Type.__name__ = "Integer32"
_CpqCrExpCabTemperatureStatus_Object = MibScalar
cpqCrExpCabTemperatureStatus = _CpqCrExpCabTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 8, 3),
    _CpqCrExpCabTemperatureStatus_Type()
)
cpqCrExpCabTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrExpCabTemperatureStatus.setStatus("mandatory")


class _CpqCrExpCabCondition_Type(Integer32):
    """Custom type cpqCrExpCabCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrExpCabCondition_Type.__name__ = "Integer32"
_CpqCrExpCabCondition_Object = MibScalar
cpqCrExpCabCondition = _CpqCrExpCabCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 8, 6),
    _CpqCrExpCabCondition_Type()
)
cpqCrExpCabCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrExpCabCondition.setStatus("mandatory")


class _CpqCrExpCabPowerSupplyCondition_Type(Integer32):
    """Custom type cpqCrExpCabPowerSupplyCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrExpCabPowerSupplyCondition_Type.__name__ = "Integer32"
_CpqCrExpCabPowerSupplyCondition_Object = MibScalar
cpqCrExpCabPowerSupplyCondition = _CpqCrExpCabPowerSupplyCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 8, 7),
    _CpqCrExpCabPowerSupplyCondition_Type()
)
cpqCrExpCabPowerSupplyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrExpCabPowerSupplyCondition.setStatus("mandatory")


class _CpqCrExpCabFanCondition_Type(Integer32):
    """Custom type cpqCrExpCabFanCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrExpCabFanCondition_Type.__name__ = "Integer32"
_CpqCrExpCabFanCondition_Object = MibScalar
cpqCrExpCabFanCondition = _CpqCrExpCabFanCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 8, 9),
    _CpqCrExpCabFanCondition_Type()
)
cpqCrExpCabFanCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrExpCabFanCondition.setStatus("mandatory")


class _CpqCrExpCabTemperatureCondition_Type(Integer32):
    """Custom type cpqCrExpCabTemperatureCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrExpCabTemperatureCondition_Type.__name__ = "Integer32"
_CpqCrExpCabTemperatureCondition_Object = MibScalar
cpqCrExpCabTemperatureCondition = _CpqCrExpCabTemperatureCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 8, 10),
    _CpqCrExpCabTemperatureCondition_Type()
)
cpqCrExpCabTemperatureCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrExpCabTemperatureCondition.setStatus("mandatory")
_CpqCrPartition_ObjectIdentity = ObjectIdentity
cpqCrPartition = _CpqCrPartition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 9)
)
_CpqCrPartitionTable_Object = MibTable
cpqCrPartitionTable = _CpqCrPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 9, 1)
)
if mibBuilder.loadTexts:
    cpqCrPartitionTable.setStatus("mandatory")
_CpqCrPartitionEntry_Object = MibTableRow
cpqCrPartitionEntry = _CpqCrPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 9, 1, 1)
)
cpqCrPartitionEntry.setIndexNames(
    (0, "CPQCR-MIB", "cpqCrPartitionLogDrvIndex"),
    (0, "CPQCR-MIB", "cpqCrPartitionIndex"),
)
if mibBuilder.loadTexts:
    cpqCrPartitionEntry.setStatus("mandatory")


class _CpqCrPartitionLogDrvIndex_Type(Integer32):
    """Custom type cpqCrPartitionLogDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrPartitionLogDrvIndex_Type.__name__ = "Integer32"
_CpqCrPartitionLogDrvIndex_Object = MibTableColumn
cpqCrPartitionLogDrvIndex = _CpqCrPartitionLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 9, 1, 1, 1),
    _CpqCrPartitionLogDrvIndex_Type()
)
cpqCrPartitionLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPartitionLogDrvIndex.setStatus("mandatory")


class _CpqCrPartitionIndex_Type(Integer32):
    """Custom type cpqCrPartitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCrPartitionIndex_Type.__name__ = "Integer32"
_CpqCrPartitionIndex_Object = MibTableColumn
cpqCrPartitionIndex = _CpqCrPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 9, 1, 1, 2),
    _CpqCrPartitionIndex_Type()
)
cpqCrPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPartitionIndex.setStatus("mandatory")


class _CpqCrPartitionRAIDLevel_Type(Integer32):
    """Custom type cpqCrPartitionRAIDLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("jbod", 2),
          ("other", 1),
          ("raid0", 3),
          ("raid0plus1", 5),
          ("raid1", 4),
          ("raid4", 6),
          ("raid5", 7))
    )


_CpqCrPartitionRAIDLevel_Type.__name__ = "Integer32"
_CpqCrPartitionRAIDLevel_Object = MibTableColumn
cpqCrPartitionRAIDLevel = _CpqCrPartitionRAIDLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 9, 1, 1, 3),
    _CpqCrPartitionRAIDLevel_Type()
)
cpqCrPartitionRAIDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPartitionRAIDLevel.setStatus("mandatory")


class _CpqCrPartitionStatus_Type(Integer32):
    """Custom type cpqCrPartitionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("good", 2),
          ("initializing", 6),
          ("other", 1),
          ("reconstructing", 5),
          ("reduced", 3))
    )


_CpqCrPartitionStatus_Type.__name__ = "Integer32"
_CpqCrPartitionStatus_Object = MibTableColumn
cpqCrPartitionStatus = _CpqCrPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 9, 1, 1, 4),
    _CpqCrPartitionStatus_Type()
)
cpqCrPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPartitionStatus.setStatus("mandatory")


class _CpqCrPartitionSize_Type(Integer32):
    """Custom type cpqCrPartitionSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqCrPartitionSize_Type.__name__ = "Integer32"
_CpqCrPartitionSize_Object = MibTableColumn
cpqCrPartitionSize = _CpqCrPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 9, 1, 1, 5),
    _CpqCrPartitionSize_Type()
)
cpqCrPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPartitionSize.setStatus("mandatory")


class _CpqCrPartitionCondition_Type(Integer32):
    """Custom type cpqCrPartitionCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCrPartitionCondition_Type.__name__ = "Integer32"
_CpqCrPartitionCondition_Object = MibTableColumn
cpqCrPartitionCondition = _CpqCrPartitionCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 141, 2, 9, 1, 1, 6),
    _CpqCrPartitionCondition_Type()
)
cpqCrPartitionCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCrPartitionCondition.setStatus("mandatory")
_CpqCrTrap_ObjectIdentity = ObjectIdentity
cpqCrTrap = _CpqCrTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 3)
)
_CpqCrInterfaceTrap_ObjectIdentity = ObjectIdentity
cpqCrInterfaceTrap = _CpqCrInterfaceTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 1)
)
_CpqCrCntlrTrap_ObjectIdentity = ObjectIdentity
cpqCrCntlrTrap = _CpqCrCntlrTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 2)
)
_CpqCrLogDrvTrap_ObjectIdentity = ObjectIdentity
cpqCrLogDrvTrap = _CpqCrLogDrvTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 3)
)
_CpqCrSpareDrvTrap_ObjectIdentity = ObjectIdentity
cpqCrSpareDrvTrap = _CpqCrSpareDrvTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 4)
)
_CpqCrPhyDrvTrap_ObjectIdentity = ObjectIdentity
cpqCrPhyDrvTrap = _CpqCrPhyDrvTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5)
)
_CpqCrEMUTrap_ObjectIdentity = ObjectIdentity
cpqCrEMUTrap = _CpqCrEMUTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 7)
)
_CpqCrExpCabTrap_ObjectIdentity = ObjectIdentity
cpqCrExpCabTrap = _CpqCrExpCabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 8)
)

# Managed Objects groups


# Notification objects

cpqCrController1FailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 2, 0, 1)
)
cpqCrController1FailureTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrController1FailureTrap.setStatus(
        ""
    )

cpqCrController1InformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 2, 0, 2)
)
cpqCrController1InformationTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrController1InformationTrap.setStatus(
        ""
    )

cpqCrController2FailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 2, 0, 3)
)
cpqCrController2FailureTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrController2FailureTrap.setStatus(
        ""
    )

cpqCrController2InformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 2, 0, 4)
)
cpqCrController2InformationTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrController2InformationTrap.setStatus(
        ""
    )

cpqCrLogDriveInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 3, 0, 5)
)
cpqCrLogDriveInformationTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrLogDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrLogDriveInformationTrap.setStatus(
        ""
    )

cpqCrLogDriveFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 3, 0, 6)
)
cpqCrLogDriveFailureTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrLogDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrLogDriveFailureTrap.setStatus(
        ""
    )

cpqCrLogDriveReconstructTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 3, 0, 7)
)
cpqCrLogDriveReconstructTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrLogDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrLogDriveReconstructTrap.setStatus(
        ""
    )

cpqCrLogDriveReducedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 3, 0, 8)
)
cpqCrLogDriveReducedTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrLogDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrLogDriveReducedTrap.setStatus(
        ""
    )

cpqCrLogDriveInitializingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 3, 0, 9)
)
cpqCrLogDriveInitializingTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrLogDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrLogDriveInitializingTrap.setStatus(
        ""
    )

cpqCrDiskInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 10)
)
cpqCrDiskInformationTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrPhyDrvCntlrIndex"),
        ("CPQCR-MIB", "cpqCrPhyDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrDiskInformationTrap.setStatus(
        ""
    )

cpqCrDiskFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 11)
)
cpqCrDiskFailureTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrPhyDrvCntlrIndex"),
        ("CPQCR-MIB", "cpqCrPhyDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrDiskFailureTrap.setStatus(
        ""
    )

cpqCrDiskReconstructTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 12)
)
cpqCrDiskReconstructTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrPhyDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrDiskReconstructTrap.setStatus(
        ""
    )

cpqCrDiskAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 13)
)
cpqCrDiskAvailableTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrPhyDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrDiskAvailableTrap.setStatus(
        ""
    )

cpqCrDiskSpareTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 14)
)
cpqCrDiskSpareTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrPhyDrvIndex"))
)
if mibBuilder.loadTexts:
    cpqCrDiskSpareTrap.setStatus(
        ""
    )

cpqCrPhyDiskInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 30)
)
cpqCrPhyDiskInformationTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrPhyDrvScsiID"))
)
if mibBuilder.loadTexts:
    cpqCrPhyDiskInformationTrap.setStatus(
        ""
    )

cpqCrPhyDiskFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 31)
)
cpqCrPhyDiskFailureTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrPhyDrvScsiID"))
)
if mibBuilder.loadTexts:
    cpqCrPhyDiskFailureTrap.setStatus(
        ""
    )

cpqCrPhyDiskReconstructTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 32)
)
cpqCrPhyDiskReconstructTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrPhyDrvScsiID"))
)
if mibBuilder.loadTexts:
    cpqCrPhyDiskReconstructTrap.setStatus(
        ""
    )

cpqCrPhyDiskAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 33)
)
cpqCrPhyDiskAvailableTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrPhyDrvScsiID"))
)
if mibBuilder.loadTexts:
    cpqCrPhyDiskAvailableTrap.setStatus(
        ""
    )

cpqCrPhyDiskSpareTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 5, 0, 34)
)
cpqCrPhyDiskSpareTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQCR-MIB", "cpqCrSpareScsiID"))
)
if mibBuilder.loadTexts:
    cpqCrPhyDiskSpareTrap.setStatus(
        ""
    )

cpqCrEMUNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 7, 0, 15)
)
cpqCrEMUNormalTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrEMUNormalTrap.setStatus(
        ""
    )

cpqCrEMUFanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 7, 0, 16)
)
cpqCrEMUFanFailureTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrEMUFanFailureTrap.setStatus(
        ""
    )

cpqCrEMUFanInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 7, 0, 17)
)
cpqCrEMUFanInformationTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrEMUFanInformationTrap.setStatus(
        ""
    )

cpqCrEMUPowerSupplyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 7, 0, 18)
)
cpqCrEMUPowerSupplyFailureTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrEMUPowerSupplyFailureTrap.setStatus(
        ""
    )

cpqCrEMUPowerSupplyInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 7, 0, 19)
)
cpqCrEMUPowerSupplyInformationTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrEMUPowerSupplyInformationTrap.setStatus(
        ""
    )

cpqCrEMUTemperatureWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 7, 0, 23)
)
cpqCrEMUTemperatureWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrEMUTemperatureWarningTrap.setStatus(
        ""
    )

cpqCrEMUTemperatureCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 7, 0, 24)
)
cpqCrEMUTemperatureCriticalTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrEMUTemperatureCriticalTrap.setStatus(
        ""
    )

cpqCrEMUTemperatureInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 7, 0, 25)
)
cpqCrEMUTemperatureInformationTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrEMUTemperatureInformationTrap.setStatus(
        ""
    )

cpqCrExpCabFanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 8, 0, 20)
)
cpqCrExpCabFanFailureTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrExpCabFanFailureTrap.setStatus(
        ""
    )

cpqCrExpCabFanInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 8, 0, 21)
)
cpqCrExpCabFanInformationTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrExpCabFanInformationTrap.setStatus(
        ""
    )

cpqCrExpCabPowerSupplyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 8, 0, 22)
)
cpqCrExpCabPowerSupplyFailureTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrExpCabPowerSupplyFailureTrap.setStatus(
        ""
    )

cpqCrExpCabTemperatureWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 8, 0, 26)
)
cpqCrExpCabTemperatureWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrExpCabTemperatureWarningTrap.setStatus(
        ""
    )

cpqCrExpCabTemperatureCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 8, 0, 27)
)
cpqCrExpCabTemperatureCriticalTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrExpCabTemperatureCriticalTrap.setStatus(
        ""
    )

cpqCrExpCabTemperatureInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 8, 0, 28)
)
cpqCrExpCabTemperatureInformationTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrExpCabTemperatureInformationTrap.setStatus(
        ""
    )

cpqCrExpCabPowerSupplyInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 141, 3, 8, 0, 29)
)
cpqCrExpCabPowerSupplyInformationTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqCrExpCabPowerSupplyInformationTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQCR-MIB",
    **{"cpqClusteredRAID": cpqClusteredRAID,
       "cpqCrMibRev": cpqCrMibRev,
       "cpqCrMibRevMajor": cpqCrMibRevMajor,
       "cpqCrMibRevMinor": cpqCrMibRevMinor,
       "cpqCrMibCondition": cpqCrMibCondition,
       "cpqCrComponent": cpqCrComponent,
       "cpqCrInterface": cpqCrInterface,
       "cpqCrOsCommon": cpqCrOsCommon,
       "cpqCrOsCommonPollFreq": cpqCrOsCommonPollFreq,
       "cpqCrCntlr": cpqCrCntlr,
       "cpqCrCntlrTable": cpqCrCntlrTable,
       "cpqCrCntlrEntry": cpqCrCntlrEntry,
       "cpqCrCntlrIndex": cpqCrCntlrIndex,
       "cpqCrCntlrSerialNumber": cpqCrCntlrSerialNumber,
       "cpqCrCntlrFWRev": cpqCrCntlrFWRev,
       "cpqCrCntlrCondition": cpqCrCntlrCondition,
       "cpqCrCntlrCurrentRole": cpqCrCntlrCurrentRole,
       "cpqCrCntlrDriveOwnership": cpqCrCntlrDriveOwnership,
       "cpqCrCntlrRebuildRate": cpqCrCntlrRebuildRate,
       "cpqCrCntlrCreateRate": cpqCrCntlrCreateRate,
       "cpqCrCntlrCacheSize": cpqCrCntlrCacheSize,
       "cpqCrCntlrSimmSizeA": cpqCrCntlrSimmSizeA,
       "cpqCrCntlrSimmSizeB": cpqCrCntlrSimmSizeB,
       "cpqCrLogDrv": cpqCrLogDrv,
       "cpqCrLogDrvTable": cpqCrLogDrvTable,
       "cpqCrLogDrvEntry": cpqCrLogDrvEntry,
       "cpqCrLogDrvCntlrIndex": cpqCrLogDrvCntlrIndex,
       "cpqCrLogDrvIndex": cpqCrLogDrvIndex,
       "cpqCrLogDrvRAIDLevel": cpqCrLogDrvRAIDLevel,
       "cpqCrLogDrvStatus": cpqCrLogDrvStatus,
       "cpqCrLogDrvRebuildPercentage": cpqCrLogDrvRebuildPercentage,
       "cpqCrLogDrvAvailSpares": cpqCrLogDrvAvailSpares,
       "cpqCrLogDrvSize": cpqCrLogDrvSize,
       "cpqCrLogDrvPhyDrvIDs": cpqCrLogDrvPhyDrvIDs,
       "cpqCrLogDrvCondition": cpqCrLogDrvCondition,
       "cpqCrLogDrvPartitionIDs": cpqCrLogDrvPartitionIDs,
       "cpqCrSpareDrv": cpqCrSpareDrv,
       "cpqCrSpareTable": cpqCrSpareTable,
       "cpqCrSpareEntry": cpqCrSpareEntry,
       "cpqCrSpareCntlrIndex": cpqCrSpareCntlrIndex,
       "cpqCrSparePhyDrvIndex": cpqCrSparePhyDrvIndex,
       "cpqCrSpareStatus": cpqCrSpareStatus,
       "cpqCrSpareCondition": cpqCrSpareCondition,
       "cpqCrSpareScsiID": cpqCrSpareScsiID,
       "cpqCrPhyDrv": cpqCrPhyDrv,
       "cpqCrPhyDrvTable": cpqCrPhyDrvTable,
       "cpqCrPhyDrvEntry": cpqCrPhyDrvEntry,
       "cpqCrPhyDrvCntlrIndex": cpqCrPhyDrvCntlrIndex,
       "cpqCrPhyDrvIndex": cpqCrPhyDrvIndex,
       "cpqCrPhyDrvVendor": cpqCrPhyDrvVendor,
       "cpqCrPhyDrvModel": cpqCrPhyDrvModel,
       "cpqCrPhyDrvRevision": cpqCrPhyDrvRevision,
       "cpqCrPhyDrvStatus": cpqCrPhyDrvStatus,
       "cpqCrPhyDrvSize": cpqCrPhyDrvSize,
       "cpqCrPhyDrvCondition": cpqCrPhyDrvCondition,
       "cpqCrPhyDrvScsiID": cpqCrPhyDrvScsiID,
       "cpqCrEMU": cpqCrEMU,
       "cpqCrEMUBoardTemperatureStatus": cpqCrEMUBoardTemperatureStatus,
       "cpqCrEMUEnclosureTemperatureStatus": cpqCrEMUEnclosureTemperatureStatus,
       "cpqCrEMUBoardTemperatureLevel": cpqCrEMUBoardTemperatureLevel,
       "cpqCrEMUEnclosureTemperatureLevel": cpqCrEMUEnclosureTemperatureLevel,
       "cpqCrEMUCondition": cpqCrEMUCondition,
       "cpqCrEMUFanStatus": cpqCrEMUFanStatus,
       "cpqCrEMUFanCondition": cpqCrEMUFanCondition,
       "cpqCrEMUPowerSupplyStatus": cpqCrEMUPowerSupplyStatus,
       "cpqCrEMUPowerSupplyCondition": cpqCrEMUPowerSupplyCondition,
       "cpqCrEMUTemperatureStatus": cpqCrEMUTemperatureStatus,
       "cpqCrEMUTemperatureLevel": cpqCrEMUTemperatureLevel,
       "cpqCrEMUTemperatureCondition": cpqCrEMUTemperatureCondition,
       "cpqCrExpCab": cpqCrExpCab,
       "cpqCrExpCabPowerSupplyStatus": cpqCrExpCabPowerSupplyStatus,
       "cpqCrExpCabFanStatus": cpqCrExpCabFanStatus,
       "cpqCrExpCabTemperatureStatus": cpqCrExpCabTemperatureStatus,
       "cpqCrExpCabCondition": cpqCrExpCabCondition,
       "cpqCrExpCabPowerSupplyCondition": cpqCrExpCabPowerSupplyCondition,
       "cpqCrExpCabFanCondition": cpqCrExpCabFanCondition,
       "cpqCrExpCabTemperatureCondition": cpqCrExpCabTemperatureCondition,
       "cpqCrPartition": cpqCrPartition,
       "cpqCrPartitionTable": cpqCrPartitionTable,
       "cpqCrPartitionEntry": cpqCrPartitionEntry,
       "cpqCrPartitionLogDrvIndex": cpqCrPartitionLogDrvIndex,
       "cpqCrPartitionIndex": cpqCrPartitionIndex,
       "cpqCrPartitionRAIDLevel": cpqCrPartitionRAIDLevel,
       "cpqCrPartitionStatus": cpqCrPartitionStatus,
       "cpqCrPartitionSize": cpqCrPartitionSize,
       "cpqCrPartitionCondition": cpqCrPartitionCondition,
       "cpqCrTrap": cpqCrTrap,
       "cpqCrInterfaceTrap": cpqCrInterfaceTrap,
       "cpqCrCntlrTrap": cpqCrCntlrTrap,
       "cpqCrController1FailureTrap": cpqCrController1FailureTrap,
       "cpqCrController1InformationTrap": cpqCrController1InformationTrap,
       "cpqCrController2FailureTrap": cpqCrController2FailureTrap,
       "cpqCrController2InformationTrap": cpqCrController2InformationTrap,
       "cpqCrLogDrvTrap": cpqCrLogDrvTrap,
       "cpqCrLogDriveInformationTrap": cpqCrLogDriveInformationTrap,
       "cpqCrLogDriveFailureTrap": cpqCrLogDriveFailureTrap,
       "cpqCrLogDriveReconstructTrap": cpqCrLogDriveReconstructTrap,
       "cpqCrLogDriveReducedTrap": cpqCrLogDriveReducedTrap,
       "cpqCrLogDriveInitializingTrap": cpqCrLogDriveInitializingTrap,
       "cpqCrSpareDrvTrap": cpqCrSpareDrvTrap,
       "cpqCrPhyDrvTrap": cpqCrPhyDrvTrap,
       "cpqCrDiskInformationTrap": cpqCrDiskInformationTrap,
       "cpqCrDiskFailureTrap": cpqCrDiskFailureTrap,
       "cpqCrDiskReconstructTrap": cpqCrDiskReconstructTrap,
       "cpqCrDiskAvailableTrap": cpqCrDiskAvailableTrap,
       "cpqCrDiskSpareTrap": cpqCrDiskSpareTrap,
       "cpqCrPhyDiskInformationTrap": cpqCrPhyDiskInformationTrap,
       "cpqCrPhyDiskFailureTrap": cpqCrPhyDiskFailureTrap,
       "cpqCrPhyDiskReconstructTrap": cpqCrPhyDiskReconstructTrap,
       "cpqCrPhyDiskAvailableTrap": cpqCrPhyDiskAvailableTrap,
       "cpqCrPhyDiskSpareTrap": cpqCrPhyDiskSpareTrap,
       "cpqCrEMUTrap": cpqCrEMUTrap,
       "cpqCrEMUNormalTrap": cpqCrEMUNormalTrap,
       "cpqCrEMUFanFailureTrap": cpqCrEMUFanFailureTrap,
       "cpqCrEMUFanInformationTrap": cpqCrEMUFanInformationTrap,
       "cpqCrEMUPowerSupplyFailureTrap": cpqCrEMUPowerSupplyFailureTrap,
       "cpqCrEMUPowerSupplyInformationTrap": cpqCrEMUPowerSupplyInformationTrap,
       "cpqCrEMUTemperatureWarningTrap": cpqCrEMUTemperatureWarningTrap,
       "cpqCrEMUTemperatureCriticalTrap": cpqCrEMUTemperatureCriticalTrap,
       "cpqCrEMUTemperatureInformationTrap": cpqCrEMUTemperatureInformationTrap,
       "cpqCrExpCabTrap": cpqCrExpCabTrap,
       "cpqCrExpCabFanFailureTrap": cpqCrExpCabFanFailureTrap,
       "cpqCrExpCabFanInformationTrap": cpqCrExpCabFanInformationTrap,
       "cpqCrExpCabPowerSupplyFailureTrap": cpqCrExpCabPowerSupplyFailureTrap,
       "cpqCrExpCabTemperatureWarningTrap": cpqCrExpCabTemperatureWarningTrap,
       "cpqCrExpCabTemperatureCriticalTrap": cpqCrExpCabTemperatureCriticalTrap,
       "cpqCrExpCabTemperatureInformationTrap": cpqCrExpCabTemperatureInformationTrap,
       "cpqCrExpCabPowerSupplyInformationTrap": cpqCrExpCabPowerSupplyInformationTrap}
)
