# SNMP MIB module (CPQNIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQNIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:32 2024
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

(cpqSiServerSystemId,) = mibBuilder.importSymbols(
    "CPQSINFO-MIB",
    "cpqSiServerSystemId")

(cpqSePciSlotBoardName,) = mibBuilder.importSymbols(
    "CPQSTDEQ-MIB",
    "cpqSePciSlotBoardName")

(ipAdEntAddr,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr")

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

_CpqNic_ObjectIdentity = ObjectIdentity
cpqNic = _CpqNic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 18)
)
_CpqNicMibRev_ObjectIdentity = ObjectIdentity
cpqNicMibRev = _CpqNicMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 18, 1)
)


class _CpqNicMibRevMajor_Type(Integer32):
    """Custom type cpqNicMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqNicMibRevMajor_Type.__name__ = "Integer32"
_CpqNicMibRevMajor_Object = MibScalar
cpqNicMibRevMajor = _CpqNicMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 1, 1),
    _CpqNicMibRevMajor_Type()
)
cpqNicMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicMibRevMajor.setStatus("mandatory")


class _CpqNicMibRevMinor_Type(Integer32):
    """Custom type cpqNicMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqNicMibRevMinor_Type.__name__ = "Integer32"
_CpqNicMibRevMinor_Object = MibScalar
cpqNicMibRevMinor = _CpqNicMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 1, 2),
    _CpqNicMibRevMinor_Type()
)
cpqNicMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicMibRevMinor.setStatus("mandatory")


class _CpqNicMibCondition_Type(Integer32):
    """Custom type cpqNicMibCondition based on Integer32"""
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
          ("unknown", 1))
    )


_CpqNicMibCondition_Type.__name__ = "Integer32"
_CpqNicMibCondition_Object = MibScalar
cpqNicMibCondition = _CpqNicMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 1, 3),
    _CpqNicMibCondition_Type()
)
cpqNicMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicMibCondition.setStatus("mandatory")
_CpqNicComponent_ObjectIdentity = ObjectIdentity
cpqNicComponent = _CpqNicComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 18, 2)
)
_CpqNicInterface_ObjectIdentity = ObjectIdentity
cpqNicInterface = _CpqNicInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1)
)
_CpqNicOsCommon_ObjectIdentity = ObjectIdentity
cpqNicOsCommon = _CpqNicOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1, 4)
)


class _CpqNicOsCommonPollFreq_Type(Integer32):
    """Custom type cpqNicOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqNicOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqNicOsCommonPollFreq_Object = MibScalar
cpqNicOsCommonPollFreq = _CpqNicOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1, 4, 1),
    _CpqNicOsCommonPollFreq_Type()
)
cpqNicOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqNicOsCommonPollFreq.setStatus("mandatory")
_CpqNicOsCommonModuleTable_Object = MibTable
cpqNicOsCommonModuleTable = _CpqNicOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqNicOsCommonModuleTable.setStatus("deprecated")
_CpqNicOsCommonModuleEntry_Object = MibTableRow
cpqNicOsCommonModuleEntry = _CpqNicOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1, 4, 2, 1)
)
cpqNicOsCommonModuleEntry.setIndexNames(
    (0, "CPQNIC-MIB", "cpqNicOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqNicOsCommonModuleEntry.setStatus("deprecated")


class _CpqNicOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqNicOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqNicOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqNicOsCommonModuleIndex_Object = MibTableColumn
cpqNicOsCommonModuleIndex = _CpqNicOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1, 4, 2, 1, 1),
    _CpqNicOsCommonModuleIndex_Type()
)
cpqNicOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicOsCommonModuleIndex.setStatus("deprecated")


class _CpqNicOsCommonModuleName_Type(DisplayString):
    """Custom type cpqNicOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqNicOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqNicOsCommonModuleName_Object = MibTableColumn
cpqNicOsCommonModuleName = _CpqNicOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1, 4, 2, 1, 2),
    _CpqNicOsCommonModuleName_Type()
)
cpqNicOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicOsCommonModuleName.setStatus("deprecated")


class _CpqNicOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqNicOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqNicOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqNicOsCommonModuleVersion_Object = MibTableColumn
cpqNicOsCommonModuleVersion = _CpqNicOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1, 4, 2, 1, 3),
    _CpqNicOsCommonModuleVersion_Type()
)
cpqNicOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicOsCommonModuleVersion.setStatus("deprecated")


class _CpqNicOsCommonModuleDate_Type(OctetString):
    """Custom type cpqNicOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqNicOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqNicOsCommonModuleDate_Object = MibTableColumn
cpqNicOsCommonModuleDate = _CpqNicOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1, 4, 2, 1, 4),
    _CpqNicOsCommonModuleDate_Type()
)
cpqNicOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicOsCommonModuleDate.setStatus("deprecated")


class _CpqNicOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqNicOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqNicOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqNicOsCommonModulePurpose_Object = MibTableColumn
cpqNicOsCommonModulePurpose = _CpqNicOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 1, 4, 2, 1, 5),
    _CpqNicOsCommonModulePurpose_Type()
)
cpqNicOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicOsCommonModulePurpose.setStatus("deprecated")
_CpqNicIfLogMap_ObjectIdentity = ObjectIdentity
cpqNicIfLogMap = _CpqNicIfLogMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2)
)
_CpqNicIfLogMapTable_Object = MibTable
cpqNicIfLogMapTable = _CpqNicIfLogMapTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqNicIfLogMapTable.setStatus("mandatory")
_CpqNicIfLogMapEntry_Object = MibTableRow
cpqNicIfLogMapEntry = _CpqNicIfLogMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1)
)
cpqNicIfLogMapEntry.setIndexNames(
    (0, "CPQNIC-MIB", "cpqNicIfLogMapIndex"),
)
if mibBuilder.loadTexts:
    cpqNicIfLogMapEntry.setStatus("mandatory")


class _CpqNicIfLogMapIndex_Type(Integer32):
    """Custom type cpqNicIfLogMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqNicIfLogMapIndex_Type.__name__ = "Integer32"
_CpqNicIfLogMapIndex_Object = MibTableColumn
cpqNicIfLogMapIndex = _CpqNicIfLogMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 1),
    _CpqNicIfLogMapIndex_Type()
)
cpqNicIfLogMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapIndex.setStatus("mandatory")
_CpqNicIfLogMapIfNumber_Type = OctetString
_CpqNicIfLogMapIfNumber_Object = MibTableColumn
cpqNicIfLogMapIfNumber = _CpqNicIfLogMapIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 2),
    _CpqNicIfLogMapIfNumber_Type()
)
cpqNicIfLogMapIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapIfNumber.setStatus("mandatory")


class _CpqNicIfLogMapDescription_Type(DisplayString):
    """Custom type cpqNicIfLogMapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqNicIfLogMapDescription_Type.__name__ = "DisplayString"
_CpqNicIfLogMapDescription_Object = MibTableColumn
cpqNicIfLogMapDescription = _CpqNicIfLogMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 3),
    _CpqNicIfLogMapDescription_Type()
)
cpqNicIfLogMapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapDescription.setStatus("mandatory")


class _CpqNicIfLogMapGroupType_Type(Integer32):
    """Custom type cpqNicIfLogMapGroupType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("ad", 8),
          ("alb", 5),
          ("fec", 6),
          ("gec", 7),
          ("nft", 4),
          ("none", 2),
          ("redundancySet", 11),
          ("redundantPair", 3),
          ("slb", 9),
          ("tlb", 10),
          ("unknown", 1))
    )


_CpqNicIfLogMapGroupType_Type.__name__ = "Integer32"
_CpqNicIfLogMapGroupType_Object = MibTableColumn
cpqNicIfLogMapGroupType = _CpqNicIfLogMapGroupType_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 4),
    _CpqNicIfLogMapGroupType_Type()
)
cpqNicIfLogMapGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapGroupType.setStatus("mandatory")


class _CpqNicIfLogMapAdapterCount_Type(Integer32):
    """Custom type cpqNicIfLogMapAdapterCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CpqNicIfLogMapAdapterCount_Type.__name__ = "Integer32"
_CpqNicIfLogMapAdapterCount_Object = MibTableColumn
cpqNicIfLogMapAdapterCount = _CpqNicIfLogMapAdapterCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 5),
    _CpqNicIfLogMapAdapterCount_Type()
)
cpqNicIfLogMapAdapterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapAdapterCount.setStatus("mandatory")


class _CpqNicIfLogMapAdapterOKCount_Type(Integer32):
    """Custom type cpqNicIfLogMapAdapterOKCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CpqNicIfLogMapAdapterOKCount_Type.__name__ = "Integer32"
_CpqNicIfLogMapAdapterOKCount_Object = MibTableColumn
cpqNicIfLogMapAdapterOKCount = _CpqNicIfLogMapAdapterOKCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 6),
    _CpqNicIfLogMapAdapterOKCount_Type()
)
cpqNicIfLogMapAdapterOKCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapAdapterOKCount.setStatus("mandatory")


class _CpqNicIfLogMapPhysicalAdapters_Type(OctetString):
    """Custom type cpqNicIfLogMapPhysicalAdapters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqNicIfLogMapPhysicalAdapters_Type.__name__ = "OctetString"
_CpqNicIfLogMapPhysicalAdapters_Object = MibTableColumn
cpqNicIfLogMapPhysicalAdapters = _CpqNicIfLogMapPhysicalAdapters_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 7),
    _CpqNicIfLogMapPhysicalAdapters_Type()
)
cpqNicIfLogMapPhysicalAdapters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapPhysicalAdapters.setStatus("mandatory")


class _CpqNicIfLogMapMACAddress_Type(OctetString):
    """Custom type cpqNicIfLogMapMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CpqNicIfLogMapMACAddress_Type.__name__ = "OctetString"
_CpqNicIfLogMapMACAddress_Object = MibTableColumn
cpqNicIfLogMapMACAddress = _CpqNicIfLogMapMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 8),
    _CpqNicIfLogMapMACAddress_Type()
)
cpqNicIfLogMapMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapMACAddress.setStatus("mandatory")


class _CpqNicIfLogMapSwitchoverMode_Type(Integer32):
    """Custom type cpqNicIfLogMapSwitchoverMode based on Integer32"""
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
        *(("auto", 6),
          ("manual", 3),
          ("none", 2),
          ("preferenceOrder", 7),
          ("preferredPrimary", 5),
          ("switchOnFail", 4),
          ("unknown", 1))
    )


_CpqNicIfLogMapSwitchoverMode_Type.__name__ = "Integer32"
_CpqNicIfLogMapSwitchoverMode_Object = MibTableColumn
cpqNicIfLogMapSwitchoverMode = _CpqNicIfLogMapSwitchoverMode_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 9),
    _CpqNicIfLogMapSwitchoverMode_Type()
)
cpqNicIfLogMapSwitchoverMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapSwitchoverMode.setStatus("mandatory")


class _CpqNicIfLogMapCondition_Type(Integer32):
    """Custom type cpqNicIfLogMapCondition based on Integer32"""
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


_CpqNicIfLogMapCondition_Type.__name__ = "Integer32"
_CpqNicIfLogMapCondition_Object = MibTableColumn
cpqNicIfLogMapCondition = _CpqNicIfLogMapCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 10),
    _CpqNicIfLogMapCondition_Type()
)
cpqNicIfLogMapCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapCondition.setStatus("mandatory")


class _CpqNicIfLogMapStatus_Type(Integer32):
    """Custom type cpqNicIfLogMapStatus based on Integer32"""
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
        *(("groupFailed", 5),
          ("ok", 2),
          ("primaryFailed", 3),
          ("redundancyLost", 7),
          ("redundancyReduced", 6),
          ("standbyFailed", 4),
          ("unknown", 1))
    )


_CpqNicIfLogMapStatus_Type.__name__ = "Integer32"
_CpqNicIfLogMapStatus_Object = MibTableColumn
cpqNicIfLogMapStatus = _CpqNicIfLogMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 11),
    _CpqNicIfLogMapStatus_Type()
)
cpqNicIfLogMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapStatus.setStatus("mandatory")
_CpqNicIfLogMapNumSwitchovers_Type = Counter32
_CpqNicIfLogMapNumSwitchovers_Object = MibTableColumn
cpqNicIfLogMapNumSwitchovers = _CpqNicIfLogMapNumSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 12),
    _CpqNicIfLogMapNumSwitchovers_Type()
)
cpqNicIfLogMapNumSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapNumSwitchovers.setStatus("mandatory")


class _CpqNicIfLogMapHwLocation_Type(DisplayString):
    """Custom type cpqNicIfLogMapHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqNicIfLogMapHwLocation_Type.__name__ = "DisplayString"
_CpqNicIfLogMapHwLocation_Object = MibTableColumn
cpqNicIfLogMapHwLocation = _CpqNicIfLogMapHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 13),
    _CpqNicIfLogMapHwLocation_Type()
)
cpqNicIfLogMapHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapHwLocation.setStatus("optional")
_CpqNicIfLogMapSpeed_Type = Gauge32
_CpqNicIfLogMapSpeed_Object = MibTableColumn
cpqNicIfLogMapSpeed = _CpqNicIfLogMapSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 14),
    _CpqNicIfLogMapSpeed_Type()
)
cpqNicIfLogMapSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapSpeed.setStatus("mandatory")


class _CpqNicIfLogMapVlanCount_Type(Integer32):
    """Custom type cpqNicIfLogMapVlanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CpqNicIfLogMapVlanCount_Type.__name__ = "Integer32"
_CpqNicIfLogMapVlanCount_Object = MibTableColumn
cpqNicIfLogMapVlanCount = _CpqNicIfLogMapVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 15),
    _CpqNicIfLogMapVlanCount_Type()
)
cpqNicIfLogMapVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapVlanCount.setStatus("mandatory")


class _CpqNicIfLogMapVlans_Type(OctetString):
    """Custom type cpqNicIfLogMapVlans based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqNicIfLogMapVlans_Type.__name__ = "OctetString"
_CpqNicIfLogMapVlans_Object = MibTableColumn
cpqNicIfLogMapVlans = _CpqNicIfLogMapVlans_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 16),
    _CpqNicIfLogMapVlans_Type()
)
cpqNicIfLogMapVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapVlans.setStatus("mandatory")
_CpqNicIfLogMapLastChange_Type = TimeTicks
_CpqNicIfLogMapLastChange_Object = MibTableColumn
cpqNicIfLogMapLastChange = _CpqNicIfLogMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 17),
    _CpqNicIfLogMapLastChange_Type()
)
cpqNicIfLogMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapLastChange.setStatus("mandatory")
_CpqNicIfLogMapAdvancedTeaming_Type = Integer32
_CpqNicIfLogMapAdvancedTeaming_Object = MibTableColumn
cpqNicIfLogMapAdvancedTeaming = _CpqNicIfLogMapAdvancedTeaming_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 18),
    _CpqNicIfLogMapAdvancedTeaming_Type()
)
cpqNicIfLogMapAdvancedTeaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapAdvancedTeaming.setStatus("mandatory")
_CpqNicIfLogMapSpeedMbps_Type = Gauge32
_CpqNicIfLogMapSpeedMbps_Object = MibTableColumn
cpqNicIfLogMapSpeedMbps = _CpqNicIfLogMapSpeedMbps_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 19),
    _CpqNicIfLogMapSpeedMbps_Type()
)
cpqNicIfLogMapSpeedMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapSpeedMbps.setStatus("optional")
_CpqNicIfLogMapIPV6Address_Type = DisplayString
_CpqNicIfLogMapIPV6Address_Object = MibTableColumn
cpqNicIfLogMapIPV6Address = _CpqNicIfLogMapIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 20),
    _CpqNicIfLogMapIPV6Address_Type()
)
cpqNicIfLogMapIPV6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapIPV6Address.setStatus("optional")
_CpqNicIfLogMapLACNumber_Type = DisplayString
_CpqNicIfLogMapLACNumber_Object = MibTableColumn
cpqNicIfLogMapLACNumber = _CpqNicIfLogMapLACNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 1, 1, 21),
    _CpqNicIfLogMapLACNumber_Type()
)
cpqNicIfLogMapLACNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapLACNumber.setStatus("optional")


class _CpqNicIfLogMapOverallCondition_Type(Integer32):
    """Custom type cpqNicIfLogMapOverallCondition based on Integer32"""
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


_CpqNicIfLogMapOverallCondition_Type.__name__ = "Integer32"
_CpqNicIfLogMapOverallCondition_Object = MibScalar
cpqNicIfLogMapOverallCondition = _CpqNicIfLogMapOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 2, 2),
    _CpqNicIfLogMapOverallCondition_Type()
)
cpqNicIfLogMapOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfLogMapOverallCondition.setStatus("mandatory")
_CpqNicIfPhysAdapter_ObjectIdentity = ObjectIdentity
cpqNicIfPhysAdapter = _CpqNicIfPhysAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3)
)
_CpqNicIfPhysAdapterTable_Object = MibTable
cpqNicIfPhysAdapterTable = _CpqNicIfPhysAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterTable.setStatus("mandatory")
_CpqNicIfPhysAdapterEntry_Object = MibTableRow
cpqNicIfPhysAdapterEntry = _CpqNicIfPhysAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1)
)
cpqNicIfPhysAdapterEntry.setIndexNames(
    (0, "CPQNIC-MIB", "cpqNicIfPhysAdapterIndex"),
)
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterEntry.setStatus("mandatory")


class _CpqNicIfPhysAdapterIndex_Type(Integer32):
    """Custom type cpqNicIfPhysAdapterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqNicIfPhysAdapterIndex_Type.__name__ = "Integer32"
_CpqNicIfPhysAdapterIndex_Object = MibTableColumn
cpqNicIfPhysAdapterIndex = _CpqNicIfPhysAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 1),
    _CpqNicIfPhysAdapterIndex_Type()
)
cpqNicIfPhysAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterIndex.setStatus("mandatory")
_CpqNicIfPhysAdapterIfNumber_Type = OctetString
_CpqNicIfPhysAdapterIfNumber_Object = MibTableColumn
cpqNicIfPhysAdapterIfNumber = _CpqNicIfPhysAdapterIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 2),
    _CpqNicIfPhysAdapterIfNumber_Type()
)
cpqNicIfPhysAdapterIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterIfNumber.setStatus("mandatory")


class _CpqNicIfPhysAdapterRole_Type(Integer32):
    """Custom type cpqNicIfPhysAdapterRole based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("member", 4),
          ("none", 8),
          ("notApplicable", 255),
          ("primary", 2),
          ("secondary", 3),
          ("standby", 7),
          ("tx", 6),
          ("txRx", 5),
          ("unknown", 1))
    )


_CpqNicIfPhysAdapterRole_Type.__name__ = "Integer32"
_CpqNicIfPhysAdapterRole_Object = MibTableColumn
cpqNicIfPhysAdapterRole = _CpqNicIfPhysAdapterRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 3),
    _CpqNicIfPhysAdapterRole_Type()
)
cpqNicIfPhysAdapterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterRole.setStatus("mandatory")


class _CpqNicIfPhysAdapterMACAddress_Type(OctetString):
    """Custom type cpqNicIfPhysAdapterMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CpqNicIfPhysAdapterMACAddress_Type.__name__ = "OctetString"
_CpqNicIfPhysAdapterMACAddress_Object = MibTableColumn
cpqNicIfPhysAdapterMACAddress = _CpqNicIfPhysAdapterMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 4),
    _CpqNicIfPhysAdapterMACAddress_Type()
)
cpqNicIfPhysAdapterMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterMACAddress.setStatus("mandatory")
_CpqNicIfPhysAdapterSlot_Type = Integer32
_CpqNicIfPhysAdapterSlot_Object = MibTableColumn
cpqNicIfPhysAdapterSlot = _CpqNicIfPhysAdapterSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 5),
    _CpqNicIfPhysAdapterSlot_Type()
)
cpqNicIfPhysAdapterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterSlot.setStatus("mandatory")
_CpqNicIfPhysAdapterIoAddr_Type = Integer32
_CpqNicIfPhysAdapterIoAddr_Object = MibTableColumn
cpqNicIfPhysAdapterIoAddr = _CpqNicIfPhysAdapterIoAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 6),
    _CpqNicIfPhysAdapterIoAddr_Type()
)
cpqNicIfPhysAdapterIoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterIoAddr.setStatus("mandatory")


class _CpqNicIfPhysAdapterIrq_Type(Integer32):
    """Custom type cpqNicIfPhysAdapterIrq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqNicIfPhysAdapterIrq_Type.__name__ = "Integer32"
_CpqNicIfPhysAdapterIrq_Object = MibTableColumn
cpqNicIfPhysAdapterIrq = _CpqNicIfPhysAdapterIrq_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 7),
    _CpqNicIfPhysAdapterIrq_Type()
)
cpqNicIfPhysAdapterIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterIrq.setStatus("mandatory")
_CpqNicIfPhysAdapterDma_Type = Integer32
_CpqNicIfPhysAdapterDma_Object = MibTableColumn
cpqNicIfPhysAdapterDma = _CpqNicIfPhysAdapterDma_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 8),
    _CpqNicIfPhysAdapterDma_Type()
)
cpqNicIfPhysAdapterDma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterDma.setStatus("mandatory")
_CpqNicIfPhysAdapterMemAddr_Type = Integer32
_CpqNicIfPhysAdapterMemAddr_Object = MibTableColumn
cpqNicIfPhysAdapterMemAddr = _CpqNicIfPhysAdapterMemAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 9),
    _CpqNicIfPhysAdapterMemAddr_Type()
)
cpqNicIfPhysAdapterMemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterMemAddr.setStatus("mandatory")
_CpqNicIfPhysAdapterPort_Type = Integer32
_CpqNicIfPhysAdapterPort_Object = MibTableColumn
cpqNicIfPhysAdapterPort = _CpqNicIfPhysAdapterPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 10),
    _CpqNicIfPhysAdapterPort_Type()
)
cpqNicIfPhysAdapterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterPort.setStatus("mandatory")


class _CpqNicIfPhysAdapterDuplexState_Type(Integer32):
    """Custom type cpqNicIfPhysAdapterDuplexState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("half", 2),
          ("unknown", 1))
    )


_CpqNicIfPhysAdapterDuplexState_Type.__name__ = "Integer32"
_CpqNicIfPhysAdapterDuplexState_Object = MibTableColumn
cpqNicIfPhysAdapterDuplexState = _CpqNicIfPhysAdapterDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 11),
    _CpqNicIfPhysAdapterDuplexState_Type()
)
cpqNicIfPhysAdapterDuplexState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterDuplexState.setStatus("mandatory")


class _CpqNicIfPhysAdapterCondition_Type(Integer32):
    """Custom type cpqNicIfPhysAdapterCondition based on Integer32"""
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


_CpqNicIfPhysAdapterCondition_Type.__name__ = "Integer32"
_CpqNicIfPhysAdapterCondition_Object = MibTableColumn
cpqNicIfPhysAdapterCondition = _CpqNicIfPhysAdapterCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 12),
    _CpqNicIfPhysAdapterCondition_Type()
)
cpqNicIfPhysAdapterCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterCondition.setStatus("mandatory")


class _CpqNicIfPhysAdapterState_Type(Integer32):
    """Custom type cpqNicIfPhysAdapterState based on Integer32"""
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
        *(("active", 2),
          ("failed", 4),
          ("standby", 3),
          ("unknown", 1))
    )


_CpqNicIfPhysAdapterState_Type.__name__ = "Integer32"
_CpqNicIfPhysAdapterState_Object = MibTableColumn
cpqNicIfPhysAdapterState = _CpqNicIfPhysAdapterState_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 13),
    _CpqNicIfPhysAdapterState_Type()
)
cpqNicIfPhysAdapterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterState.setStatus("mandatory")


class _CpqNicIfPhysAdapterStatus_Type(Integer32):
    """Custom type cpqNicIfPhysAdapterStatus based on Integer32"""
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
        *(("generalFailure", 3),
          ("linkFailure", 4),
          ("ok", 2),
          ("unknown", 1))
    )


_CpqNicIfPhysAdapterStatus_Type.__name__ = "Integer32"
_CpqNicIfPhysAdapterStatus_Object = MibTableColumn
cpqNicIfPhysAdapterStatus = _CpqNicIfPhysAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 14),
    _CpqNicIfPhysAdapterStatus_Type()
)
cpqNicIfPhysAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterStatus.setStatus("mandatory")


class _CpqNicIfPhysAdapterStatsValid_Type(Integer32):
    """Custom type cpqNicIfPhysAdapterStatsValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CpqNicIfPhysAdapterStatsValid_Type.__name__ = "Integer32"
_CpqNicIfPhysAdapterStatsValid_Object = MibTableColumn
cpqNicIfPhysAdapterStatsValid = _CpqNicIfPhysAdapterStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 15),
    _CpqNicIfPhysAdapterStatsValid_Type()
)
cpqNicIfPhysAdapterStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterStatsValid.setStatus("mandatory")
_CpqNicIfPhysAdapterGoodTransmits_Type = Counter32
_CpqNicIfPhysAdapterGoodTransmits_Object = MibTableColumn
cpqNicIfPhysAdapterGoodTransmits = _CpqNicIfPhysAdapterGoodTransmits_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 16),
    _CpqNicIfPhysAdapterGoodTransmits_Type()
)
cpqNicIfPhysAdapterGoodTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterGoodTransmits.setStatus("mandatory")
_CpqNicIfPhysAdapterGoodReceives_Type = Counter32
_CpqNicIfPhysAdapterGoodReceives_Object = MibTableColumn
cpqNicIfPhysAdapterGoodReceives = _CpqNicIfPhysAdapterGoodReceives_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 17),
    _CpqNicIfPhysAdapterGoodReceives_Type()
)
cpqNicIfPhysAdapterGoodReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterGoodReceives.setStatus("mandatory")
_CpqNicIfPhysAdapterBadTransmits_Type = Counter32
_CpqNicIfPhysAdapterBadTransmits_Object = MibTableColumn
cpqNicIfPhysAdapterBadTransmits = _CpqNicIfPhysAdapterBadTransmits_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 18),
    _CpqNicIfPhysAdapterBadTransmits_Type()
)
cpqNicIfPhysAdapterBadTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterBadTransmits.setStatus("mandatory")
_CpqNicIfPhysAdapterBadReceives_Type = Counter32
_CpqNicIfPhysAdapterBadReceives_Object = MibTableColumn
cpqNicIfPhysAdapterBadReceives = _CpqNicIfPhysAdapterBadReceives_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 19),
    _CpqNicIfPhysAdapterBadReceives_Type()
)
cpqNicIfPhysAdapterBadReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterBadReceives.setStatus("mandatory")
_CpqNicIfPhysAdapterAlignmentErrors_Type = Counter32
_CpqNicIfPhysAdapterAlignmentErrors_Object = MibTableColumn
cpqNicIfPhysAdapterAlignmentErrors = _CpqNicIfPhysAdapterAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 20),
    _CpqNicIfPhysAdapterAlignmentErrors_Type()
)
cpqNicIfPhysAdapterAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterAlignmentErrors.setStatus("mandatory")
_CpqNicIfPhysAdapterFCSErrors_Type = Counter32
_CpqNicIfPhysAdapterFCSErrors_Object = MibTableColumn
cpqNicIfPhysAdapterFCSErrors = _CpqNicIfPhysAdapterFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 21),
    _CpqNicIfPhysAdapterFCSErrors_Type()
)
cpqNicIfPhysAdapterFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterFCSErrors.setStatus("mandatory")
_CpqNicIfPhysAdapterSingleCollisionFrames_Type = Counter32
_CpqNicIfPhysAdapterSingleCollisionFrames_Object = MibTableColumn
cpqNicIfPhysAdapterSingleCollisionFrames = _CpqNicIfPhysAdapterSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 22),
    _CpqNicIfPhysAdapterSingleCollisionFrames_Type()
)
cpqNicIfPhysAdapterSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterSingleCollisionFrames.setStatus("mandatory")
_CpqNicIfPhysAdapterMultipleCollisionFrames_Type = Counter32
_CpqNicIfPhysAdapterMultipleCollisionFrames_Object = MibTableColumn
cpqNicIfPhysAdapterMultipleCollisionFrames = _CpqNicIfPhysAdapterMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 23),
    _CpqNicIfPhysAdapterMultipleCollisionFrames_Type()
)
cpqNicIfPhysAdapterMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterMultipleCollisionFrames.setStatus("mandatory")
_CpqNicIfPhysAdapterDeferredTransmissions_Type = Counter32
_CpqNicIfPhysAdapterDeferredTransmissions_Object = MibTableColumn
cpqNicIfPhysAdapterDeferredTransmissions = _CpqNicIfPhysAdapterDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 24),
    _CpqNicIfPhysAdapterDeferredTransmissions_Type()
)
cpqNicIfPhysAdapterDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterDeferredTransmissions.setStatus("mandatory")
_CpqNicIfPhysAdapterLateCollisions_Type = Counter32
_CpqNicIfPhysAdapterLateCollisions_Object = MibTableColumn
cpqNicIfPhysAdapterLateCollisions = _CpqNicIfPhysAdapterLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 25),
    _CpqNicIfPhysAdapterLateCollisions_Type()
)
cpqNicIfPhysAdapterLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterLateCollisions.setStatus("mandatory")
_CpqNicIfPhysAdapterExcessiveCollisions_Type = Counter32
_CpqNicIfPhysAdapterExcessiveCollisions_Object = MibTableColumn
cpqNicIfPhysAdapterExcessiveCollisions = _CpqNicIfPhysAdapterExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 26),
    _CpqNicIfPhysAdapterExcessiveCollisions_Type()
)
cpqNicIfPhysAdapterExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterExcessiveCollisions.setStatus("mandatory")
_CpqNicIfPhysAdapterInternalMacTransmitErrors_Type = Counter32
_CpqNicIfPhysAdapterInternalMacTransmitErrors_Object = MibTableColumn
cpqNicIfPhysAdapterInternalMacTransmitErrors = _CpqNicIfPhysAdapterInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 27),
    _CpqNicIfPhysAdapterInternalMacTransmitErrors_Type()
)
cpqNicIfPhysAdapterInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterInternalMacTransmitErrors.setStatus("mandatory")
_CpqNicIfPhysAdapterCarrierSenseErrors_Type = Counter32
_CpqNicIfPhysAdapterCarrierSenseErrors_Object = MibTableColumn
cpqNicIfPhysAdapterCarrierSenseErrors = _CpqNicIfPhysAdapterCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 28),
    _CpqNicIfPhysAdapterCarrierSenseErrors_Type()
)
cpqNicIfPhysAdapterCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterCarrierSenseErrors.setStatus("mandatory")
_CpqNicIfPhysAdapterFrameTooLongs_Type = Counter32
_CpqNicIfPhysAdapterFrameTooLongs_Object = MibTableColumn
cpqNicIfPhysAdapterFrameTooLongs = _CpqNicIfPhysAdapterFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 29),
    _CpqNicIfPhysAdapterFrameTooLongs_Type()
)
cpqNicIfPhysAdapterFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterFrameTooLongs.setStatus("mandatory")
_CpqNicIfPhysAdapterInternalMacReceiveErrors_Type = Counter32
_CpqNicIfPhysAdapterInternalMacReceiveErrors_Object = MibTableColumn
cpqNicIfPhysAdapterInternalMacReceiveErrors = _CpqNicIfPhysAdapterInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 30),
    _CpqNicIfPhysAdapterInternalMacReceiveErrors_Type()
)
cpqNicIfPhysAdapterInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterInternalMacReceiveErrors.setStatus("mandatory")


class _CpqNicIfPhysAdapterHwLocation_Type(DisplayString):
    """Custom type cpqNicIfPhysAdapterHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqNicIfPhysAdapterHwLocation_Type.__name__ = "DisplayString"
_CpqNicIfPhysAdapterHwLocation_Object = MibTableColumn
cpqNicIfPhysAdapterHwLocation = _CpqNicIfPhysAdapterHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 31),
    _CpqNicIfPhysAdapterHwLocation_Type()
)
cpqNicIfPhysAdapterHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterHwLocation.setStatus("optional")


class _CpqNicIfPhysAdapterPartNumber_Type(DisplayString):
    """Custom type cpqNicIfPhysAdapterPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqNicIfPhysAdapterPartNumber_Type.__name__ = "DisplayString"
_CpqNicIfPhysAdapterPartNumber_Object = MibTableColumn
cpqNicIfPhysAdapterPartNumber = _CpqNicIfPhysAdapterPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 32),
    _CpqNicIfPhysAdapterPartNumber_Type()
)
cpqNicIfPhysAdapterPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterPartNumber.setStatus("mandatory")
_CpqNicIfPhysAdapterSpeed_Type = Gauge32
_CpqNicIfPhysAdapterSpeed_Object = MibTableColumn
cpqNicIfPhysAdapterSpeed = _CpqNicIfPhysAdapterSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 33),
    _CpqNicIfPhysAdapterSpeed_Type()
)
cpqNicIfPhysAdapterSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterSpeed.setStatus("mandatory")


class _CpqNicIfPhysAdapterConfSpeedDuplex_Type(Integer32):
    """Custom type cpqNicIfPhysAdapterConfSpeedDuplex based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("autoAuto", 2),
          ("ethernetFull", 4),
          ("ethernetHalf", 3),
          ("fastEthernetFull", 6),
          ("fastEthernetHalf", 5),
          ("gig10EthernetFull", 9),
          ("gigEthernetFull", 8),
          ("gigEthernetHalf", 7),
          ("other", 1))
    )


_CpqNicIfPhysAdapterConfSpeedDuplex_Type.__name__ = "Integer32"
_CpqNicIfPhysAdapterConfSpeedDuplex_Object = MibTableColumn
cpqNicIfPhysAdapterConfSpeedDuplex = _CpqNicIfPhysAdapterConfSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 34),
    _CpqNicIfPhysAdapterConfSpeedDuplex_Type()
)
cpqNicIfPhysAdapterConfSpeedDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterConfSpeedDuplex.setStatus("mandatory")
_CpqNicIfPhysAdapterAggregationGID_Type = Integer32
_CpqNicIfPhysAdapterAggregationGID_Object = MibTableColumn
cpqNicIfPhysAdapterAggregationGID = _CpqNicIfPhysAdapterAggregationGID_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 35),
    _CpqNicIfPhysAdapterAggregationGID_Type()
)
cpqNicIfPhysAdapterAggregationGID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterAggregationGID.setStatus("mandatory")
_CpqNicIfPhysAdapterSpeedMbps_Type = Gauge32
_CpqNicIfPhysAdapterSpeedMbps_Object = MibTableColumn
cpqNicIfPhysAdapterSpeedMbps = _CpqNicIfPhysAdapterSpeedMbps_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 36),
    _CpqNicIfPhysAdapterSpeedMbps_Type()
)
cpqNicIfPhysAdapterSpeedMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterSpeedMbps.setStatus("optional")
_CpqNicIfPhysAdapterInOctets_Type = Counter32
_CpqNicIfPhysAdapterInOctets_Object = MibTableColumn
cpqNicIfPhysAdapterInOctets = _CpqNicIfPhysAdapterInOctets_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 37),
    _CpqNicIfPhysAdapterInOctets_Type()
)
cpqNicIfPhysAdapterInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterInOctets.setStatus("optional")
_CpqNicIfPhysAdapterOutOctets_Type = Counter32
_CpqNicIfPhysAdapterOutOctets_Object = MibTableColumn
cpqNicIfPhysAdapterOutOctets = _CpqNicIfPhysAdapterOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 38),
    _CpqNicIfPhysAdapterOutOctets_Type()
)
cpqNicIfPhysAdapterOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterOutOctets.setStatus("optional")


class _CpqNicIfPhysAdapterName_Type(DisplayString):
    """Custom type cpqNicIfPhysAdapterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqNicIfPhysAdapterName_Type.__name__ = "DisplayString"
_CpqNicIfPhysAdapterName_Object = MibTableColumn
cpqNicIfPhysAdapterName = _CpqNicIfPhysAdapterName_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 39),
    _CpqNicIfPhysAdapterName_Type()
)
cpqNicIfPhysAdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterName.setStatus("optional")
_CpqNicIfPhysAdapterIoBayNo_Type = Integer32
_CpqNicIfPhysAdapterIoBayNo_Object = MibTableColumn
cpqNicIfPhysAdapterIoBayNo = _CpqNicIfPhysAdapterIoBayNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 40),
    _CpqNicIfPhysAdapterIoBayNo_Type()
)
cpqNicIfPhysAdapterIoBayNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterIoBayNo.setStatus("optional")


class _CpqNicIfPhysAdapterFWVersion_Type(DisplayString):
    """Custom type cpqNicIfPhysAdapterFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqNicIfPhysAdapterFWVersion_Type.__name__ = "DisplayString"
_CpqNicIfPhysAdapterFWVersion_Object = MibTableColumn
cpqNicIfPhysAdapterFWVersion = _CpqNicIfPhysAdapterFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 1, 1, 41),
    _CpqNicIfPhysAdapterFWVersion_Type()
)
cpqNicIfPhysAdapterFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfPhysAdapterFWVersion.setStatus("optional")
_CpqNicPhyAdapBaseMemTable_Object = MibTable
cpqNicPhyAdapBaseMemTable = _CpqNicPhyAdapBaseMemTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cpqNicPhyAdapBaseMemTable.setStatus("optional")
_CpqNicPhyAdapBaseMemEntry_Object = MibTableRow
cpqNicPhyAdapBaseMemEntry = _CpqNicPhyAdapBaseMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 2, 1)
)
cpqNicPhyAdapBaseMemEntry.setIndexNames(
    (0, "CPQNIC-MIB", "cpqNicPhyAdapBaseMemIndex"),
)
if mibBuilder.loadTexts:
    cpqNicPhyAdapBaseMemEntry.setStatus("optional")


class _CpqNicPhyAdapBaseMemIndex_Type(Integer32):
    """Custom type cpqNicPhyAdapBaseMemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqNicPhyAdapBaseMemIndex_Type.__name__ = "Integer32"
_CpqNicPhyAdapBaseMemIndex_Object = MibTableColumn
cpqNicPhyAdapBaseMemIndex = _CpqNicPhyAdapBaseMemIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 2, 1, 1),
    _CpqNicPhyAdapBaseMemIndex_Type()
)
cpqNicPhyAdapBaseMemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicPhyAdapBaseMemIndex.setStatus("optional")
_CpqNicPhyAdapBaseMemIfIndex_Type = Integer32
_CpqNicPhyAdapBaseMemIfIndex_Object = MibTableColumn
cpqNicPhyAdapBaseMemIfIndex = _CpqNicPhyAdapBaseMemIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 2, 1, 2),
    _CpqNicPhyAdapBaseMemIfIndex_Type()
)
cpqNicPhyAdapBaseMemIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicPhyAdapBaseMemIfIndex.setStatus("optional")
_CpqNicPhyAdapBaseMemAddr_Type = Integer32
_CpqNicPhyAdapBaseMemAddr_Object = MibTableColumn
cpqNicPhyAdapBaseMemAddr = _CpqNicPhyAdapBaseMemAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 3, 2, 1, 3),
    _CpqNicPhyAdapBaseMemAddr_Type()
)
cpqNicPhyAdapBaseMemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicPhyAdapBaseMemAddr.setStatus("optional")
_CpqNicIfVlanMap_ObjectIdentity = ObjectIdentity
cpqNicIfVlanMap = _CpqNicIfVlanMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4)
)
_CpqNicIfVlanMapTable_Object = MibTable
cpqNicIfVlanMapTable = _CpqNicIfVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqNicIfVlanMapTable.setStatus("mandatory")
_CpqNicIfVlanMapEntry_Object = MibTableRow
cpqNicIfVlanMapEntry = _CpqNicIfVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4, 1, 1)
)
cpqNicIfVlanMapEntry.setIndexNames(
    (0, "CPQNIC-MIB", "cpqNicIfVlanMapIndex"),
)
if mibBuilder.loadTexts:
    cpqNicIfVlanMapEntry.setStatus("mandatory")


class _CpqNicIfVlanMapIndex_Type(Integer32):
    """Custom type cpqNicIfVlanMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqNicIfVlanMapIndex_Type.__name__ = "Integer32"
_CpqNicIfVlanMapIndex_Object = MibTableColumn
cpqNicIfVlanMapIndex = _CpqNicIfVlanMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4, 1, 1, 1),
    _CpqNicIfVlanMapIndex_Type()
)
cpqNicIfVlanMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfVlanMapIndex.setStatus("mandatory")


class _CpqNicIfVlanMapLogIndex_Type(Integer32):
    """Custom type cpqNicIfVlanMapLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqNicIfVlanMapLogIndex_Type.__name__ = "Integer32"
_CpqNicIfVlanMapLogIndex_Object = MibTableColumn
cpqNicIfVlanMapLogIndex = _CpqNicIfVlanMapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4, 1, 1, 2),
    _CpqNicIfVlanMapLogIndex_Type()
)
cpqNicIfVlanMapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfVlanMapLogIndex.setStatus("mandatory")
_CpqNicIfVlanMapIfIndex_Type = Integer32
_CpqNicIfVlanMapIfIndex_Object = MibTableColumn
cpqNicIfVlanMapIfIndex = _CpqNicIfVlanMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4, 1, 1, 3),
    _CpqNicIfVlanMapIfIndex_Type()
)
cpqNicIfVlanMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfVlanMapIfIndex.setStatus("mandatory")


class _CpqNicIfVlanMapVlanId_Type(Integer32):
    """Custom type cpqNicIfVlanMapVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CpqNicIfVlanMapVlanId_Type.__name__ = "Integer32"
_CpqNicIfVlanMapVlanId_Object = MibTableColumn
cpqNicIfVlanMapVlanId = _CpqNicIfVlanMapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4, 1, 1, 4),
    _CpqNicIfVlanMapVlanId_Type()
)
cpqNicIfVlanMapVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfVlanMapVlanId.setStatus("mandatory")


class _CpqNicIfVlanMapVlanName_Type(DisplayString):
    """Custom type cpqNicIfVlanMapVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CpqNicIfVlanMapVlanName_Type.__name__ = "DisplayString"
_CpqNicIfVlanMapVlanName_Object = MibTableColumn
cpqNicIfVlanMapVlanName = _CpqNicIfVlanMapVlanName_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4, 1, 1, 5),
    _CpqNicIfVlanMapVlanName_Type()
)
cpqNicIfVlanMapVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfVlanMapVlanName.setStatus("mandatory")
_CpqNicIfVlanMapVlanIPV6Address_Type = DisplayString
_CpqNicIfVlanMapVlanIPV6Address_Object = MibTableColumn
cpqNicIfVlanMapVlanIPV6Address = _CpqNicIfVlanMapVlanIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4, 1, 1, 6),
    _CpqNicIfVlanMapVlanIPV6Address_Type()
)
cpqNicIfVlanMapVlanIPV6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfVlanMapVlanIPV6Address.setStatus("optional")
_CpqNicIfVlanMapVlanLACNumber_Type = DisplayString
_CpqNicIfVlanMapVlanLACNumber_Object = MibTableColumn
cpqNicIfVlanMapVlanLACNumber = _CpqNicIfVlanMapVlanLACNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 4, 1, 1, 7),
    _CpqNicIfVlanMapVlanLACNumber_Type()
)
cpqNicIfVlanMapVlanLACNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicIfVlanMapVlanLACNumber.setStatus("optional")
_CpqNicVirusThrottle_ObjectIdentity = ObjectIdentity
cpqNicVirusThrottle = _CpqNicVirusThrottle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 5)
)


class _CpqNicVtInstalled_Type(Integer32):
    """Custom type cpqNicVtInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_CpqNicVtInstalled_Type.__name__ = "Integer32"
_CpqNicVtInstalled_Object = MibScalar
cpqNicVtInstalled = _CpqNicVtInstalled_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 5, 1),
    _CpqNicVtInstalled_Type()
)
cpqNicVtInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicVtInstalled.setStatus("mandatory")


class _CpqNicVtLicensed_Type(Integer32):
    """Custom type cpqNicVtLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licensed", 2),
          ("notLicensed", 1))
    )


_CpqNicVtLicensed_Type.__name__ = "Integer32"
_CpqNicVtLicensed_Object = MibScalar
cpqNicVtLicensed = _CpqNicVtLicensed_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 5, 2),
    _CpqNicVtLicensed_Type()
)
cpqNicVtLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicVtLicensed.setStatus("mandatory")


class _CpqNicVtVirusActivity_Type(Integer32):
    """Custom type cpqNicVtVirusActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 2),
          ("notDetected", 1))
    )


_CpqNicVtVirusActivity_Type.__name__ = "Integer32"
_CpqNicVtVirusActivity_Object = MibScalar
cpqNicVtVirusActivity = _CpqNicVtVirusActivity_Object(
    (1, 3, 6, 1, 4, 1, 232, 18, 2, 5, 3),
    _CpqNicVtVirusActivity_Type()
)
cpqNicVtVirusActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNicVtVirusActivity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqNicConnectivityRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18001)
)
cpqNicConnectivityRestored.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"))
)
if mibBuilder.loadTexts:
    cpqNicConnectivityRestored.setStatus(
        ""
    )

cpqNicConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18002)
)
cpqNicConnectivityLost.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"))
)
if mibBuilder.loadTexts:
    cpqNicConnectivityLost.setStatus(
        ""
    )

cpqNicRedundancyIncreased = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18003)
)
cpqNicRedundancyIncreased.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQNIC-MIB", "cpqNicIfLogMapAdapterOKCount"))
)
if mibBuilder.loadTexts:
    cpqNicRedundancyIncreased.setStatus(
        ""
    )

cpqNicRedundancyReduced = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18004)
)
cpqNicRedundancyReduced.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQNIC-MIB", "cpqNicIfLogMapAdapterOKCount"))
)
if mibBuilder.loadTexts:
    cpqNicRedundancyReduced.setStatus(
        ""
    )

cpqNic2ConnectivityRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18005)
)
cpqNic2ConnectivityRestored.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterStatus"),
        ("CPQSTDEQ-MIB", "cpqSePciSlotBoardName"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPartNumber"),
        ("IP-MIB", "ipAdEntAddr"))
)
if mibBuilder.loadTexts:
    cpqNic2ConnectivityRestored.setStatus(
        ""
    )

cpqNic2ConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18006)
)
cpqNic2ConnectivityLost.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterStatus"),
        ("CPQSTDEQ-MIB", "cpqSePciSlotBoardName"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPartNumber"),
        ("IP-MIB", "ipAdEntAddr"))
)
if mibBuilder.loadTexts:
    cpqNic2ConnectivityLost.setStatus(
        ""
    )

cpqNic2RedundancyIncreased = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18007)
)
cpqNic2RedundancyIncreased.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterStatus"),
        ("CPQSTDEQ-MIB", "cpqSePciSlotBoardName"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPartNumber"),
        ("IP-MIB", "ipAdEntAddr"),
        ("CPQNIC-MIB", "cpqNicIfLogMapAdapterOKCount"))
)
if mibBuilder.loadTexts:
    cpqNic2RedundancyIncreased.setStatus(
        ""
    )

cpqNic2RedundancyReduced = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18008)
)
cpqNic2RedundancyReduced.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterStatus"),
        ("CPQSTDEQ-MIB", "cpqSePciSlotBoardName"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPartNumber"),
        ("IP-MIB", "ipAdEntAddr"),
        ("CPQNIC-MIB", "cpqNicIfLogMapAdapterOKCount"))
)
if mibBuilder.loadTexts:
    cpqNic2RedundancyReduced.setStatus(
        ""
    )

cpqNicVirusLikeActivityDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18009)
)
cpqNicVirusLikeActivityDetected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"))
)
if mibBuilder.loadTexts:
    cpqNicVirusLikeActivityDetected.setStatus(
        ""
    )

cpqNicVirusLikeActivityStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18010)
)
cpqNicVirusLikeActivityStopped.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"))
)
if mibBuilder.loadTexts:
    cpqNicVirusLikeActivityStopped.setStatus(
        ""
    )

cpqNic3ConnectivityRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18011)
)
cpqNic3ConnectivityRestored.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterStatus"),
        ("CPQSTDEQ-MIB", "cpqSePciSlotBoardName"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPartNumber"),
        ("IP-MIB", "ipAdEntAddr"),
        ("CPQNIC-MIB", "cpqNicIfLogMapIPV6Address"))
)
if mibBuilder.loadTexts:
    cpqNic3ConnectivityRestored.setStatus(
        ""
    )

cpqNic3ConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18012)
)
cpqNic3ConnectivityLost.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterStatus"),
        ("CPQSTDEQ-MIB", "cpqSePciSlotBoardName"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPartNumber"),
        ("IP-MIB", "ipAdEntAddr"),
        ("CPQNIC-MIB", "cpqNicIfLogMapIPV6Address"))
)
if mibBuilder.loadTexts:
    cpqNic3ConnectivityLost.setStatus(
        ""
    )

cpqNic3RedundancyIncreased = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18013)
)
cpqNic3RedundancyIncreased.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterStatus"),
        ("CPQSTDEQ-MIB", "cpqSePciSlotBoardName"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPartNumber"),
        ("IP-MIB", "ipAdEntAddr"),
        ("CPQNIC-MIB", "cpqNicIfLogMapIPV6Address"),
        ("CPQNIC-MIB", "cpqNicIfLogMapAdapterOKCount"))
)
if mibBuilder.loadTexts:
    cpqNic3RedundancyIncreased.setStatus(
        ""
    )

cpqNic3RedundancyReduced = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 18014)
)
cpqNic3RedundancyReduced.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterSlot"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPort"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterStatus"),
        ("CPQSTDEQ-MIB", "cpqSePciSlotBoardName"),
        ("CPQNIC-MIB", "cpqNicIfPhysAdapterPartNumber"),
        ("IP-MIB", "ipAdEntAddr"),
        ("CPQNIC-MIB", "cpqNicIfLogMapIPV6Address"),
        ("CPQNIC-MIB", "cpqNicIfLogMapAdapterOKCount"))
)
if mibBuilder.loadTexts:
    cpqNic3RedundancyReduced.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQNIC-MIB",
    **{"cpqNicConnectivityRestored": cpqNicConnectivityRestored,
       "cpqNicConnectivityLost": cpqNicConnectivityLost,
       "cpqNicRedundancyIncreased": cpqNicRedundancyIncreased,
       "cpqNicRedundancyReduced": cpqNicRedundancyReduced,
       "cpqNic2ConnectivityRestored": cpqNic2ConnectivityRestored,
       "cpqNic2ConnectivityLost": cpqNic2ConnectivityLost,
       "cpqNic2RedundancyIncreased": cpqNic2RedundancyIncreased,
       "cpqNic2RedundancyReduced": cpqNic2RedundancyReduced,
       "cpqNicVirusLikeActivityDetected": cpqNicVirusLikeActivityDetected,
       "cpqNicVirusLikeActivityStopped": cpqNicVirusLikeActivityStopped,
       "cpqNic3ConnectivityRestored": cpqNic3ConnectivityRestored,
       "cpqNic3ConnectivityLost": cpqNic3ConnectivityLost,
       "cpqNic3RedundancyIncreased": cpqNic3RedundancyIncreased,
       "cpqNic3RedundancyReduced": cpqNic3RedundancyReduced,
       "cpqNic": cpqNic,
       "cpqNicMibRev": cpqNicMibRev,
       "cpqNicMibRevMajor": cpqNicMibRevMajor,
       "cpqNicMibRevMinor": cpqNicMibRevMinor,
       "cpqNicMibCondition": cpqNicMibCondition,
       "cpqNicComponent": cpqNicComponent,
       "cpqNicInterface": cpqNicInterface,
       "cpqNicOsCommon": cpqNicOsCommon,
       "cpqNicOsCommonPollFreq": cpqNicOsCommonPollFreq,
       "cpqNicOsCommonModuleTable": cpqNicOsCommonModuleTable,
       "cpqNicOsCommonModuleEntry": cpqNicOsCommonModuleEntry,
       "cpqNicOsCommonModuleIndex": cpqNicOsCommonModuleIndex,
       "cpqNicOsCommonModuleName": cpqNicOsCommonModuleName,
       "cpqNicOsCommonModuleVersion": cpqNicOsCommonModuleVersion,
       "cpqNicOsCommonModuleDate": cpqNicOsCommonModuleDate,
       "cpqNicOsCommonModulePurpose": cpqNicOsCommonModulePurpose,
       "cpqNicIfLogMap": cpqNicIfLogMap,
       "cpqNicIfLogMapTable": cpqNicIfLogMapTable,
       "cpqNicIfLogMapEntry": cpqNicIfLogMapEntry,
       "cpqNicIfLogMapIndex": cpqNicIfLogMapIndex,
       "cpqNicIfLogMapIfNumber": cpqNicIfLogMapIfNumber,
       "cpqNicIfLogMapDescription": cpqNicIfLogMapDescription,
       "cpqNicIfLogMapGroupType": cpqNicIfLogMapGroupType,
       "cpqNicIfLogMapAdapterCount": cpqNicIfLogMapAdapterCount,
       "cpqNicIfLogMapAdapterOKCount": cpqNicIfLogMapAdapterOKCount,
       "cpqNicIfLogMapPhysicalAdapters": cpqNicIfLogMapPhysicalAdapters,
       "cpqNicIfLogMapMACAddress": cpqNicIfLogMapMACAddress,
       "cpqNicIfLogMapSwitchoverMode": cpqNicIfLogMapSwitchoverMode,
       "cpqNicIfLogMapCondition": cpqNicIfLogMapCondition,
       "cpqNicIfLogMapStatus": cpqNicIfLogMapStatus,
       "cpqNicIfLogMapNumSwitchovers": cpqNicIfLogMapNumSwitchovers,
       "cpqNicIfLogMapHwLocation": cpqNicIfLogMapHwLocation,
       "cpqNicIfLogMapSpeed": cpqNicIfLogMapSpeed,
       "cpqNicIfLogMapVlanCount": cpqNicIfLogMapVlanCount,
       "cpqNicIfLogMapVlans": cpqNicIfLogMapVlans,
       "cpqNicIfLogMapLastChange": cpqNicIfLogMapLastChange,
       "cpqNicIfLogMapAdvancedTeaming": cpqNicIfLogMapAdvancedTeaming,
       "cpqNicIfLogMapSpeedMbps": cpqNicIfLogMapSpeedMbps,
       "cpqNicIfLogMapIPV6Address": cpqNicIfLogMapIPV6Address,
       "cpqNicIfLogMapLACNumber": cpqNicIfLogMapLACNumber,
       "cpqNicIfLogMapOverallCondition": cpqNicIfLogMapOverallCondition,
       "cpqNicIfPhysAdapter": cpqNicIfPhysAdapter,
       "cpqNicIfPhysAdapterTable": cpqNicIfPhysAdapterTable,
       "cpqNicIfPhysAdapterEntry": cpqNicIfPhysAdapterEntry,
       "cpqNicIfPhysAdapterIndex": cpqNicIfPhysAdapterIndex,
       "cpqNicIfPhysAdapterIfNumber": cpqNicIfPhysAdapterIfNumber,
       "cpqNicIfPhysAdapterRole": cpqNicIfPhysAdapterRole,
       "cpqNicIfPhysAdapterMACAddress": cpqNicIfPhysAdapterMACAddress,
       "cpqNicIfPhysAdapterSlot": cpqNicIfPhysAdapterSlot,
       "cpqNicIfPhysAdapterIoAddr": cpqNicIfPhysAdapterIoAddr,
       "cpqNicIfPhysAdapterIrq": cpqNicIfPhysAdapterIrq,
       "cpqNicIfPhysAdapterDma": cpqNicIfPhysAdapterDma,
       "cpqNicIfPhysAdapterMemAddr": cpqNicIfPhysAdapterMemAddr,
       "cpqNicIfPhysAdapterPort": cpqNicIfPhysAdapterPort,
       "cpqNicIfPhysAdapterDuplexState": cpqNicIfPhysAdapterDuplexState,
       "cpqNicIfPhysAdapterCondition": cpqNicIfPhysAdapterCondition,
       "cpqNicIfPhysAdapterState": cpqNicIfPhysAdapterState,
       "cpqNicIfPhysAdapterStatus": cpqNicIfPhysAdapterStatus,
       "cpqNicIfPhysAdapterStatsValid": cpqNicIfPhysAdapterStatsValid,
       "cpqNicIfPhysAdapterGoodTransmits": cpqNicIfPhysAdapterGoodTransmits,
       "cpqNicIfPhysAdapterGoodReceives": cpqNicIfPhysAdapterGoodReceives,
       "cpqNicIfPhysAdapterBadTransmits": cpqNicIfPhysAdapterBadTransmits,
       "cpqNicIfPhysAdapterBadReceives": cpqNicIfPhysAdapterBadReceives,
       "cpqNicIfPhysAdapterAlignmentErrors": cpqNicIfPhysAdapterAlignmentErrors,
       "cpqNicIfPhysAdapterFCSErrors": cpqNicIfPhysAdapterFCSErrors,
       "cpqNicIfPhysAdapterSingleCollisionFrames": cpqNicIfPhysAdapterSingleCollisionFrames,
       "cpqNicIfPhysAdapterMultipleCollisionFrames": cpqNicIfPhysAdapterMultipleCollisionFrames,
       "cpqNicIfPhysAdapterDeferredTransmissions": cpqNicIfPhysAdapterDeferredTransmissions,
       "cpqNicIfPhysAdapterLateCollisions": cpqNicIfPhysAdapterLateCollisions,
       "cpqNicIfPhysAdapterExcessiveCollisions": cpqNicIfPhysAdapterExcessiveCollisions,
       "cpqNicIfPhysAdapterInternalMacTransmitErrors": cpqNicIfPhysAdapterInternalMacTransmitErrors,
       "cpqNicIfPhysAdapterCarrierSenseErrors": cpqNicIfPhysAdapterCarrierSenseErrors,
       "cpqNicIfPhysAdapterFrameTooLongs": cpqNicIfPhysAdapterFrameTooLongs,
       "cpqNicIfPhysAdapterInternalMacReceiveErrors": cpqNicIfPhysAdapterInternalMacReceiveErrors,
       "cpqNicIfPhysAdapterHwLocation": cpqNicIfPhysAdapterHwLocation,
       "cpqNicIfPhysAdapterPartNumber": cpqNicIfPhysAdapterPartNumber,
       "cpqNicIfPhysAdapterSpeed": cpqNicIfPhysAdapterSpeed,
       "cpqNicIfPhysAdapterConfSpeedDuplex": cpqNicIfPhysAdapterConfSpeedDuplex,
       "cpqNicIfPhysAdapterAggregationGID": cpqNicIfPhysAdapterAggregationGID,
       "cpqNicIfPhysAdapterSpeedMbps": cpqNicIfPhysAdapterSpeedMbps,
       "cpqNicIfPhysAdapterInOctets": cpqNicIfPhysAdapterInOctets,
       "cpqNicIfPhysAdapterOutOctets": cpqNicIfPhysAdapterOutOctets,
       "cpqNicIfPhysAdapterName": cpqNicIfPhysAdapterName,
       "cpqNicIfPhysAdapterIoBayNo": cpqNicIfPhysAdapterIoBayNo,
       "cpqNicIfPhysAdapterFWVersion": cpqNicIfPhysAdapterFWVersion,
       "cpqNicPhyAdapBaseMemTable": cpqNicPhyAdapBaseMemTable,
       "cpqNicPhyAdapBaseMemEntry": cpqNicPhyAdapBaseMemEntry,
       "cpqNicPhyAdapBaseMemIndex": cpqNicPhyAdapBaseMemIndex,
       "cpqNicPhyAdapBaseMemIfIndex": cpqNicPhyAdapBaseMemIfIndex,
       "cpqNicPhyAdapBaseMemAddr": cpqNicPhyAdapBaseMemAddr,
       "cpqNicIfVlanMap": cpqNicIfVlanMap,
       "cpqNicIfVlanMapTable": cpqNicIfVlanMapTable,
       "cpqNicIfVlanMapEntry": cpqNicIfVlanMapEntry,
       "cpqNicIfVlanMapIndex": cpqNicIfVlanMapIndex,
       "cpqNicIfVlanMapLogIndex": cpqNicIfVlanMapLogIndex,
       "cpqNicIfVlanMapIfIndex": cpqNicIfVlanMapIfIndex,
       "cpqNicIfVlanMapVlanId": cpqNicIfVlanMapVlanId,
       "cpqNicIfVlanMapVlanName": cpqNicIfVlanMapVlanName,
       "cpqNicIfVlanMapVlanIPV6Address": cpqNicIfVlanMapVlanIPV6Address,
       "cpqNicIfVlanMapVlanLACNumber": cpqNicIfVlanMapVlanLACNumber,
       "cpqNicVirusThrottle": cpqNicVirusThrottle,
       "cpqNicVtInstalled": cpqNicVtInstalled,
       "cpqNicVtLicensed": cpqNicVtLicensed,
       "cpqNicVtVirusActivity": cpqNicVtVirusActivity}
)
