# SNMP MIB module (F10-Z-SERIES-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F10-Z-SERIES-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:30 2024
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(F10CardOperStatus,
 F10ChassisType,
 F10HundredthdB,
 F10MfgDate,
 F10ProcessorModuleType,
 F10SSeriesPortType,
 F10SwDate) = mibBuilder.importSymbols(
    "FORCE10-TC",
    "F10CardOperStatus",
    "F10ChassisType",
    "F10HundredthdB",
    "F10MfgDate",
    "F10ProcessorModuleType",
    "F10SSeriesPortType",
    "F10SwDate")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

f10ZSerChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25)
)
f10ZSerChassisMib.setRevisions(
        ("2014-04-16 12:00",
         "2013-10-10 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10ZSerChassisObject_ObjectIdentity = ObjectIdentity
f10ZSerChassisObject = _F10ZSerChassisObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1)
)
_ChObjects_ObjectIdentity = ObjectIdentity
chObjects = _ChObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1)
)
_ChType_Type = F10ChassisType
_ChType_Object = MibScalar
chType = _ChType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 1),
    _ChType_Type()
)
chType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chType.setStatus("current")


class _ChSwVersion_Type(DisplayString):
    """Custom type chSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChSwVersion_Type.__name__ = "DisplayString"
_ChSwVersion_Object = MibScalar
chSwVersion = _ChSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 2),
    _ChSwVersion_Type()
)
chSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSwVersion.setStatus("current")
_ChMacAddr_Type = MacAddress
_ChMacAddr_Object = MibScalar
chMacAddr = _ChMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 3),
    _ChMacAddr_Type()
)
chMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chMacAddr.setStatus("current")


class _ChSerialNumber_Type(DisplayString):
    """Custom type chSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChSerialNumber_Type.__name__ = "DisplayString"
_ChSerialNumber_Object = MibScalar
chSerialNumber = _ChSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 4),
    _ChSerialNumber_Type()
)
chSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSerialNumber.setStatus("current")


class _ChPartNum_Type(DisplayString):
    """Custom type chPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ChPartNum_Type.__name__ = "DisplayString"
_ChPartNum_Object = MibScalar
chPartNum = _ChPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 5),
    _ChPartNum_Type()
)
chPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPartNum.setStatus("current")


class _ChProductRev_Type(DisplayString):
    """Custom type chProductRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ChProductRev_Type.__name__ = "DisplayString"
_ChProductRev_Object = MibScalar
chProductRev = _ChProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 6),
    _ChProductRev_Type()
)
chProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chProductRev.setStatus("current")


class _ChVendorId_Type(DisplayString):
    """Custom type chVendorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ChVendorId_Type.__name__ = "DisplayString"
_ChVendorId_Object = MibScalar
chVendorId = _ChVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 7),
    _ChVendorId_Type()
)
chVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVendorId.setStatus("current")
_ChMfgDate_Type = F10MfgDate
_ChMfgDate_Object = MibScalar
chMfgDate = _ChMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 8),
    _ChMfgDate_Type()
)
chMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chMfgDate.setStatus("current")


class _ChCountryCode_Type(DisplayString):
    """Custom type chCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_ChCountryCode_Type.__name__ = "DisplayString"
_ChCountryCode_Object = MibScalar
chCountryCode = _ChCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 9),
    _ChCountryCode_Type()
)
chCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCountryCode.setStatus("current")


class _ChPiecePartID_Type(DisplayString):
    """Custom type chPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ChPiecePartID_Type.__name__ = "DisplayString"
_ChPiecePartID_Object = MibScalar
chPiecePartID = _ChPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 10),
    _ChPiecePartID_Type()
)
chPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPiecePartID.setStatus("current")


class _ChPPIDRevision_Type(DisplayString):
    """Custom type chPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ChPPIDRevision_Type.__name__ = "DisplayString"
_ChPPIDRevision_Object = MibScalar
chPPIDRevision = _ChPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 11),
    _ChPPIDRevision_Type()
)
chPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPPIDRevision.setStatus("current")


class _ChServiceTag_Type(DisplayString):
    """Custom type chServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ChServiceTag_Type.__name__ = "DisplayString"
_ChServiceTag_Object = MibScalar
chServiceTag = _ChServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 12),
    _ChServiceTag_Type()
)
chServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chServiceTag.setStatus("current")


class _ChExpressServiceCode_Type(DisplayString):
    """Custom type chExpressServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChExpressServiceCode_Type.__name__ = "DisplayString"
_ChExpressServiceCode_Object = MibScalar
chExpressServiceCode = _ChExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 13),
    _ChExpressServiceCode_Type()
)
chExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chExpressServiceCode.setStatus("current")
_ChNum10GigEtherPorts_Type = Integer32
_ChNum10GigEtherPorts_Object = MibScalar
chNum10GigEtherPorts = _ChNum10GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 14),
    _ChNum10GigEtherPorts_Type()
)
chNum10GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNum10GigEtherPorts.setStatus("current")
_ChNum40GigEtherPorts_Type = Integer32
_ChNum40GigEtherPorts_Object = MibScalar
chNum40GigEtherPorts = _ChNum40GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 15),
    _ChNum40GigEtherPorts_Type()
)
chNum40GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNum40GigEtherPorts.setStatus("current")
_ChNumLineCards_Type = Integer32
_ChNumLineCards_Object = MibScalar
chNumLineCards = _ChNumLineCards_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 16),
    _ChNumLineCards_Type()
)
chNumLineCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumLineCards.setStatus("current")
_ChNumFanTrays_Type = Integer32
_ChNumFanTrays_Object = MibScalar
chNumFanTrays = _ChNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 17),
    _ChNumFanTrays_Type()
)
chNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumFanTrays.setStatus("current")
_ChNumPowerSupplies_Type = Integer32
_ChNumPowerSupplies_Object = MibScalar
chNumPowerSupplies = _ChNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 18),
    _ChNumPowerSupplies_Type()
)
chNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumPowerSupplies.setStatus("current")
_ChSysObjects_ObjectIdentity = ObjectIdentity
chSysObjects = _ChSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2)
)
_ChSysProcessorTable_Object = MibTable
chSysProcessorTable = _ChSysProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chSysProcessorTable.setStatus("current")
_ChSysProcessorEntry_Object = MibTableRow
chSysProcessorEntry = _ChSysProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1)
)
chSysProcessorEntry.setIndexNames(
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorIndex"),
)
if mibBuilder.loadTexts:
    chSysProcessorEntry.setStatus("current")


class _ChSysProcessorIndex_Type(Integer32):
    """Custom type chSysProcessorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChSysProcessorIndex_Type.__name__ = "Integer32"
_ChSysProcessorIndex_Object = MibTableColumn
chSysProcessorIndex = _ChSysProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1, 1),
    _ChSysProcessorIndex_Type()
)
chSysProcessorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chSysProcessorIndex.setStatus("current")
_ChSysProcessorType_Type = F10ProcessorModuleType
_ChSysProcessorType_Object = MibTableColumn
chSysProcessorType = _ChSysProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1, 2),
    _ChSysProcessorType_Type()
)
chSysProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorType.setStatus("current")
_ChSysProcessorUpTime_Type = TimeTicks
_ChSysProcessorUpTime_Object = MibTableColumn
chSysProcessorUpTime = _ChSysProcessorUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1, 3),
    _ChSysProcessorUpTime_Type()
)
chSysProcessorUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorUpTime.setStatus("current")
_ChSysProcessorMemSize_Type = Integer32
_ChSysProcessorMemSize_Object = MibTableColumn
chSysProcessorMemSize = _ChSysProcessorMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1, 4),
    _ChSysProcessorMemSize_Type()
)
chSysProcessorMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorMemSize.setStatus("current")
_ChSysSwModuleTable_Object = MibTable
chSysSwModuleTable = _ChSysSwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2)
)
if mibBuilder.loadTexts:
    chSysSwModuleTable.setStatus("current")
_ChSysSwModuleEntry_Object = MibTableRow
chSysSwModuleEntry = _ChSysSwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1)
)
chSysSwModuleEntry.setIndexNames(
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorIndex"),
)
if mibBuilder.loadTexts:
    chSysSwModuleEntry.setStatus("current")


class _ChSysSwModuleRuntimeImgVersion_Type(DisplayString):
    """Custom type chSysSwModuleRuntimeImgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChSysSwModuleRuntimeImgVersion_Type.__name__ = "DisplayString"
_ChSysSwModuleRuntimeImgVersion_Object = MibTableColumn
chSysSwModuleRuntimeImgVersion = _ChSysSwModuleRuntimeImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 1),
    _ChSysSwModuleRuntimeImgVersion_Type()
)
chSysSwModuleRuntimeImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwModuleRuntimeImgVersion.setStatus("current")


class _ChSysSwModuleRuntimeImgDate_Type(F10SwDate):
    """Custom type chSysSwModuleRuntimeImgDate based on F10SwDate"""
    subtypeSpec = F10SwDate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ChSysSwModuleRuntimeImgDate_Type.__name__ = "F10SwDate"
_ChSysSwModuleRuntimeImgDate_Object = MibTableColumn
chSysSwModuleRuntimeImgDate = _ChSysSwModuleRuntimeImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 2),
    _ChSysSwModuleRuntimeImgDate_Type()
)
chSysSwModuleRuntimeImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwModuleRuntimeImgDate.setStatus("current")


class _ChSysSwModuleBootFlashImgVersion_Type(DisplayString):
    """Custom type chSysSwModuleBootFlashImgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChSysSwModuleBootFlashImgVersion_Type.__name__ = "DisplayString"
_ChSysSwModuleBootFlashImgVersion_Object = MibTableColumn
chSysSwModuleBootFlashImgVersion = _ChSysSwModuleBootFlashImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 3),
    _ChSysSwModuleBootFlashImgVersion_Type()
)
chSysSwModuleBootFlashImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwModuleBootFlashImgVersion.setStatus("current")


class _ChSysSwModuleBootSelectorImgVersion_Type(DisplayString):
    """Custom type chSysSwModuleBootSelectorImgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChSysSwModuleBootSelectorImgVersion_Type.__name__ = "DisplayString"
_ChSysSwModuleBootSelectorImgVersion_Object = MibTableColumn
chSysSwModuleBootSelectorImgVersion = _ChSysSwModuleBootSelectorImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 4),
    _ChSysSwModuleBootSelectorImgVersion_Type()
)
chSysSwModuleBootSelectorImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwModuleBootSelectorImgVersion.setStatus("current")


class _ChSysSwModuleNextRebootImage_Type(Integer32):
    """Custom type chSysSwModuleNextRebootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkBoot", 3),
          ("partitionA", 1),
          ("partitionB", 2))
    )


_ChSysSwModuleNextRebootImage_Type.__name__ = "Integer32"
_ChSysSwModuleNextRebootImage_Object = MibTableColumn
chSysSwModuleNextRebootImage = _ChSysSwModuleNextRebootImage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 5),
    _ChSysSwModuleNextRebootImage_Type()
)
chSysSwModuleNextRebootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwModuleNextRebootImage.setStatus("current")


class _ChSysSwModuleCurrentBootImage_Type(Integer32):
    """Custom type chSysSwModuleCurrentBootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkBoot", 3),
          ("partitionA", 1),
          ("partitionB", 2))
    )


_ChSysSwModuleCurrentBootImage_Type.__name__ = "Integer32"
_ChSysSwModuleCurrentBootImage_Object = MibTableColumn
chSysSwModuleCurrentBootImage = _ChSysSwModuleCurrentBootImage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 6),
    _ChSysSwModuleCurrentBootImage_Type()
)
chSysSwModuleCurrentBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwModuleCurrentBootImage.setStatus("current")


class _ChSysSwModuleInPartitionAImgVers_Type(DisplayString):
    """Custom type chSysSwModuleInPartitionAImgVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChSysSwModuleInPartitionAImgVers_Type.__name__ = "DisplayString"
_ChSysSwModuleInPartitionAImgVers_Object = MibTableColumn
chSysSwModuleInPartitionAImgVers = _ChSysSwModuleInPartitionAImgVers_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 7),
    _ChSysSwModuleInPartitionAImgVers_Type()
)
chSysSwModuleInPartitionAImgVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwModuleInPartitionAImgVers.setStatus("current")


class _ChSysSwModuleInPartitionBImgVers_Type(DisplayString):
    """Custom type chSysSwModuleInPartitionBImgVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChSysSwModuleInPartitionBImgVers_Type.__name__ = "DisplayString"
_ChSysSwModuleInPartitionBImgVers_Object = MibTableColumn
chSysSwModuleInPartitionBImgVers = _ChSysSwModuleInPartitionBImgVers_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 8),
    _ChSysSwModuleInPartitionBImgVers_Type()
)
chSysSwModuleInPartitionBImgVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwModuleInPartitionBImgVers.setStatus("current")
_ChSysCpuUtilTable_Object = MibTable
chSysCpuUtilTable = _ChSysCpuUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3)
)
if mibBuilder.loadTexts:
    chSysCpuUtilTable.setStatus("current")
_ChSysCpuUtilEntry_Object = MibTableRow
chSysCpuUtilEntry = _ChSysCpuUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1)
)
chSysCpuUtilEntry.setIndexNames(
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorIndex"),
)
if mibBuilder.loadTexts:
    chSysCpuUtilEntry.setStatus("current")


class _ChSysCpuUtil5Sec_Type(Gauge32):
    """Custom type chSysCpuUtil5Sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChSysCpuUtil5Sec_Type.__name__ = "Gauge32"
_ChSysCpuUtil5Sec_Object = MibTableColumn
chSysCpuUtil5Sec = _ChSysCpuUtil5Sec_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 1),
    _ChSysCpuUtil5Sec_Type()
)
chSysCpuUtil5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCpuUtil5Sec.setStatus("current")


class _ChSysCpuUtil1Min_Type(Gauge32):
    """Custom type chSysCpuUtil1Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChSysCpuUtil1Min_Type.__name__ = "Gauge32"
_ChSysCpuUtil1Min_Object = MibTableColumn
chSysCpuUtil1Min = _ChSysCpuUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 2),
    _ChSysCpuUtil1Min_Type()
)
chSysCpuUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCpuUtil1Min.setStatus("current")


class _ChSysCpuUtil5Min_Type(Gauge32):
    """Custom type chSysCpuUtil5Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChSysCpuUtil5Min_Type.__name__ = "Gauge32"
_ChSysCpuUtil5Min_Object = MibTableColumn
chSysCpuUtil5Min = _ChSysCpuUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 3),
    _ChSysCpuUtil5Min_Type()
)
chSysCpuUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCpuUtil5Min.setStatus("current")


class _ChSysCpuUtilMemUsage_Type(Gauge32):
    """Custom type chSysCpuUtilMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChSysCpuUtilMemUsage_Type.__name__ = "Gauge32"
_ChSysCpuUtilMemUsage_Object = MibTableColumn
chSysCpuUtilMemUsage = _ChSysCpuUtilMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 4),
    _ChSysCpuUtilMemUsage_Type()
)
chSysCpuUtilMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCpuUtilMemUsage.setStatus("current")


class _ChSysCpuUtilFlashUsage_Type(Gauge32):
    """Custom type chSysCpuUtilFlashUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChSysCpuUtilFlashUsage_Type.__name__ = "Gauge32"
_ChSysCpuUtilFlashUsage_Object = MibTableColumn
chSysCpuUtilFlashUsage = _ChSysCpuUtilFlashUsage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 5),
    _ChSysCpuUtilFlashUsage_Type()
)
chSysCpuUtilFlashUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCpuUtilFlashUsage.setStatus("current")
_ChSysLineCardTable_Object = MibTable
chSysLineCardTable = _ChSysLineCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4)
)
if mibBuilder.loadTexts:
    chSysLineCardTable.setStatus("current")
_ChSysLineCardEntry_Object = MibTableRow
chSysLineCardEntry = _ChSysLineCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1)
)
chSysLineCardEntry.setIndexNames(
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardIndex"),
)
if mibBuilder.loadTexts:
    chSysLineCardEntry.setStatus("current")


class _ChSysLineCardIndex_Type(Integer32):
    """Custom type chSysLineCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ChSysLineCardIndex_Type.__name__ = "Integer32"
_ChSysLineCardIndex_Object = MibTableColumn
chSysLineCardIndex = _ChSysLineCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 1),
    _ChSysLineCardIndex_Type()
)
chSysLineCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chSysLineCardIndex.setStatus("current")


class _ChSysLineCardType_Type(Integer32):
    """Custom type chSysLineCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("z9500LC36", 1),
          ("z9500LC48", 2))
    )


_ChSysLineCardType_Type.__name__ = "Integer32"
_ChSysLineCardType_Object = MibTableColumn
chSysLineCardType = _ChSysLineCardType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 2),
    _ChSysLineCardType_Type()
)
chSysLineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysLineCardType.setStatus("current")


class _ChSysLineCardDescription_Type(DisplayString):
    """Custom type chSysLineCardDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ChSysLineCardDescription_Type.__name__ = "DisplayString"
_ChSysLineCardDescription_Object = MibTableColumn
chSysLineCardDescription = _ChSysLineCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 3),
    _ChSysLineCardDescription_Type()
)
chSysLineCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysLineCardDescription.setStatus("current")
_ChSysLineCardStatus_Type = F10CardOperStatus
_ChSysLineCardStatus_Object = MibTableColumn
chSysLineCardStatus = _ChSysLineCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 4),
    _ChSysLineCardStatus_Type()
)
chSysLineCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysLineCardStatus.setStatus("current")
_ChSysLineCardTemp_Type = Integer32
_ChSysLineCardTemp_Object = MibTableColumn
chSysLineCardTemp = _ChSysLineCardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 5),
    _ChSysLineCardTemp_Type()
)
chSysLineCardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysLineCardTemp.setStatus("current")
if mibBuilder.loadTexts:
    chSysLineCardTemp.setUnits("degrees Centigrade")
_ChSysLineCardNum10GigEtherPorts_Type = Integer32
_ChSysLineCardNum10GigEtherPorts_Object = MibTableColumn
chSysLineCardNum10GigEtherPorts = _ChSysLineCardNum10GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 6),
    _ChSysLineCardNum10GigEtherPorts_Type()
)
chSysLineCardNum10GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysLineCardNum10GigEtherPorts.setStatus("current")
_ChSysLineCardNum40GigEtherPorts_Type = Integer32
_ChSysLineCardNum40GigEtherPorts_Object = MibTableColumn
chSysLineCardNum40GigEtherPorts = _ChSysLineCardNum40GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 7),
    _ChSysLineCardNum40GigEtherPorts_Type()
)
chSysLineCardNum40GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysLineCardNum40GigEtherPorts.setStatus("current")
_ChSysPortTable_Object = MibTable
chSysPortTable = _ChSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5)
)
if mibBuilder.loadTexts:
    chSysPortTable.setStatus("current")
_ChSysPortEntry_Object = MibTableRow
chSysPortEntry = _ChSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1)
)
chSysPortEntry.setIndexNames(
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardIndex"),
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysPortIndex"),
)
if mibBuilder.loadTexts:
    chSysPortEntry.setStatus("current")


class _ChSysPortIndex_Type(Integer32):
    """Custom type chSysPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_ChSysPortIndex_Type.__name__ = "Integer32"
_ChSysPortIndex_Object = MibTableColumn
chSysPortIndex = _ChSysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 1),
    _ChSysPortIndex_Type()
)
chSysPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chSysPortIndex.setStatus("current")
_ChSysPortType_Type = F10SSeriesPortType
_ChSysPortType_Object = MibTableColumn
chSysPortType = _ChSysPortType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 2),
    _ChSysPortType_Type()
)
chSysPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortType.setStatus("current")


class _ChSysPortAdminStatus_Type(Integer32):
    """Custom type chSysPortAdminStatus based on Integer32"""
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


_ChSysPortAdminStatus_Type.__name__ = "Integer32"
_ChSysPortAdminStatus_Object = MibTableColumn
chSysPortAdminStatus = _ChSysPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 3),
    _ChSysPortAdminStatus_Type()
)
chSysPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortAdminStatus.setStatus("current")


class _ChSysPortOperStatus_Type(Integer32):
    """Custom type chSysPortOperStatus based on Integer32"""
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
        *(("cardDown", 5),
          ("cardProblem", 4),
          ("notPresent", 6),
          ("portDown", 2),
          ("portProblem", 3),
          ("ready", 1))
    )


_ChSysPortOperStatus_Type.__name__ = "Integer32"
_ChSysPortOperStatus_Object = MibTableColumn
chSysPortOperStatus = _ChSysPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 4),
    _ChSysPortOperStatus_Type()
)
chSysPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortOperStatus.setStatus("current")
_ChSysPortIfIndex_Type = Integer32
_ChSysPortIfIndex_Object = MibTableColumn
chSysPortIfIndex = _ChSysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 5),
    _ChSysPortIfIndex_Type()
)
chSysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortIfIndex.setStatus("current")
_ChSysPortXfpRxPower_Type = F10HundredthdB
_ChSysPortXfpRxPower_Object = MibTableColumn
chSysPortXfpRxPower = _ChSysPortXfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 6),
    _ChSysPortXfpRxPower_Type()
)
chSysPortXfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortXfpRxPower.setStatus("current")
if mibBuilder.loadTexts:
    chSysPortXfpRxPower.setUnits("dB")
_ChSysPortXfpRxTemp_Type = Integer32
_ChSysPortXfpRxTemp_Object = MibTableColumn
chSysPortXfpRxTemp = _ChSysPortXfpRxTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 7),
    _ChSysPortXfpRxTemp_Type()
)
chSysPortXfpRxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortXfpRxTemp.setStatus("current")
if mibBuilder.loadTexts:
    chSysPortXfpRxTemp.setUnits("degrees Centigrade")
_ChSysPortXfpTxPower_Type = F10HundredthdB
_ChSysPortXfpTxPower_Object = MibTableColumn
chSysPortXfpTxPower = _ChSysPortXfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 8),
    _ChSysPortXfpTxPower_Type()
)
chSysPortXfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortXfpTxPower.setStatus("current")
if mibBuilder.loadTexts:
    chSysPortXfpTxPower.setUnits("dB")
_ChSysPowerSupplyTable_Object = MibTable
chSysPowerSupplyTable = _ChSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6)
)
if mibBuilder.loadTexts:
    chSysPowerSupplyTable.setStatus("current")
_ChSysPowerSupplyEntry_Object = MibTableRow
chSysPowerSupplyEntry = _ChSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1)
)
chSysPowerSupplyEntry.setIndexNames(
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    chSysPowerSupplyEntry.setStatus("current")


class _ChSysPowerSupplyIndex_Type(Integer32):
    """Custom type chSysPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ChSysPowerSupplyIndex_Type.__name__ = "Integer32"
_ChSysPowerSupplyIndex_Object = MibTableColumn
chSysPowerSupplyIndex = _ChSysPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 1),
    _ChSysPowerSupplyIndex_Type()
)
chSysPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chSysPowerSupplyIndex.setStatus("current")


class _ChSysPowerSupplyOperStatus_Type(Integer32):
    """Custom type chSysPowerSupplyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("down", 2),
          ("up", 1))
    )


_ChSysPowerSupplyOperStatus_Type.__name__ = "Integer32"
_ChSysPowerSupplyOperStatus_Object = MibTableColumn
chSysPowerSupplyOperStatus = _ChSysPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 2),
    _ChSysPowerSupplyOperStatus_Type()
)
chSysPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyOperStatus.setStatus("current")


class _ChSysPowerSupplyType_Type(Integer32):
    """Custom type chSysPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )


_ChSysPowerSupplyType_Type.__name__ = "Integer32"
_ChSysPowerSupplyType_Object = MibTableColumn
chSysPowerSupplyType = _ChSysPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 3),
    _ChSysPowerSupplyType_Type()
)
chSysPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyType.setStatus("current")


class _ChSysPowerSupplyPiecePartID_Type(DisplayString):
    """Custom type chSysPowerSupplyPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ChSysPowerSupplyPiecePartID_Type.__name__ = "DisplayString"
_ChSysPowerSupplyPiecePartID_Object = MibTableColumn
chSysPowerSupplyPiecePartID = _ChSysPowerSupplyPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 4),
    _ChSysPowerSupplyPiecePartID_Type()
)
chSysPowerSupplyPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyPiecePartID.setStatus("current")


class _ChSysPowerSupplyPPIDRevision_Type(DisplayString):
    """Custom type chSysPowerSupplyPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ChSysPowerSupplyPPIDRevision_Type.__name__ = "DisplayString"
_ChSysPowerSupplyPPIDRevision_Object = MibTableColumn
chSysPowerSupplyPPIDRevision = _ChSysPowerSupplyPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 5),
    _ChSysPowerSupplyPPIDRevision_Type()
)
chSysPowerSupplyPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyPPIDRevision.setStatus("current")


class _ChSysPowerSupplyServiceTag_Type(DisplayString):
    """Custom type chSysPowerSupplyServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ChSysPowerSupplyServiceTag_Type.__name__ = "DisplayString"
_ChSysPowerSupplyServiceTag_Object = MibTableColumn
chSysPowerSupplyServiceTag = _ChSysPowerSupplyServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 6),
    _ChSysPowerSupplyServiceTag_Type()
)
chSysPowerSupplyServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyServiceTag.setStatus("current")


class _ChSysPowerSupplyExpressServiceCode_Type(DisplayString):
    """Custom type chSysPowerSupplyExpressServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChSysPowerSupplyExpressServiceCode_Type.__name__ = "DisplayString"
_ChSysPowerSupplyExpressServiceCode_Object = MibTableColumn
chSysPowerSupplyExpressServiceCode = _ChSysPowerSupplyExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 7),
    _ChSysPowerSupplyExpressServiceCode_Type()
)
chSysPowerSupplyExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyExpressServiceCode.setStatus("current")
_ChSysPowerSupplyUsage_Type = Integer32
_ChSysPowerSupplyUsage_Object = MibTableColumn
chSysPowerSupplyUsage = _ChSysPowerSupplyUsage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 8),
    _ChSysPowerSupplyUsage_Type()
)
chSysPowerSupplyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyUsage.setStatus("current")
_ChSysFanTrayTable_Object = MibTable
chSysFanTrayTable = _ChSysFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7)
)
if mibBuilder.loadTexts:
    chSysFanTrayTable.setStatus("current")
_ChSysFanTrayEntry_Object = MibTableRow
chSysFanTrayEntry = _ChSysFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1)
)
chSysFanTrayEntry.setIndexNames(
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayIndex"),
)
if mibBuilder.loadTexts:
    chSysFanTrayEntry.setStatus("current")


class _ChSysFanTrayIndex_Type(Integer32):
    """Custom type chSysFanTrayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChSysFanTrayIndex_Type.__name__ = "Integer32"
_ChSysFanTrayIndex_Object = MibTableColumn
chSysFanTrayIndex = _ChSysFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 1),
    _ChSysFanTrayIndex_Type()
)
chSysFanTrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chSysFanTrayIndex.setStatus("current")


class _ChSysFanTrayOperStatus_Type(Integer32):
    """Custom type chSysFanTrayOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("down", 2),
          ("up", 1))
    )


_ChSysFanTrayOperStatus_Type.__name__ = "Integer32"
_ChSysFanTrayOperStatus_Object = MibTableColumn
chSysFanTrayOperStatus = _ChSysFanTrayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 2),
    _ChSysFanTrayOperStatus_Type()
)
chSysFanTrayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayOperStatus.setStatus("current")


class _ChSysFanTrayPiecePartID_Type(DisplayString):
    """Custom type chSysFanTrayPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ChSysFanTrayPiecePartID_Type.__name__ = "DisplayString"
_ChSysFanTrayPiecePartID_Object = MibTableColumn
chSysFanTrayPiecePartID = _ChSysFanTrayPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 3),
    _ChSysFanTrayPiecePartID_Type()
)
chSysFanTrayPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayPiecePartID.setStatus("current")


class _ChSysFanTrayPPIDRevision_Type(DisplayString):
    """Custom type chSysFanTrayPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ChSysFanTrayPPIDRevision_Type.__name__ = "DisplayString"
_ChSysFanTrayPPIDRevision_Object = MibTableColumn
chSysFanTrayPPIDRevision = _ChSysFanTrayPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 4),
    _ChSysFanTrayPPIDRevision_Type()
)
chSysFanTrayPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayPPIDRevision.setStatus("current")


class _ChSysFanTrayServiceTag_Type(DisplayString):
    """Custom type chSysFanTrayServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ChSysFanTrayServiceTag_Type.__name__ = "DisplayString"
_ChSysFanTrayServiceTag_Object = MibTableColumn
chSysFanTrayServiceTag = _ChSysFanTrayServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 5),
    _ChSysFanTrayServiceTag_Type()
)
chSysFanTrayServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayServiceTag.setStatus("current")


class _ChSysFanTrayExpressServiceCode_Type(DisplayString):
    """Custom type chSysFanTrayExpressServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChSysFanTrayExpressServiceCode_Type.__name__ = "DisplayString"
_ChSysFanTrayExpressServiceCode_Object = MibTableColumn
chSysFanTrayExpressServiceCode = _ChSysFanTrayExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 6),
    _ChSysFanTrayExpressServiceCode_Type()
)
chSysFanTrayExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayExpressServiceCode.setStatus("current")
_ChSysSwCoresTable_Object = MibTable
chSysSwCoresTable = _ChSysSwCoresTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8)
)
if mibBuilder.loadTexts:
    chSysSwCoresTable.setStatus("current")
_ChSysCoresEntry_Object = MibTableRow
chSysCoresEntry = _ChSysCoresEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1)
)
chSysCoresEntry.setIndexNames(
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorIndex"),
    (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysCoresInstance"),
)
if mibBuilder.loadTexts:
    chSysCoresEntry.setStatus("current")
_ChSysCoresInstance_Type = Integer32
_ChSysCoresInstance_Object = MibTableColumn
chSysCoresInstance = _ChSysCoresInstance_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 1),
    _ChSysCoresInstance_Type()
)
chSysCoresInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresInstance.setStatus("current")
_ChSysCoresFileName_Type = DisplayString
_ChSysCoresFileName_Object = MibTableColumn
chSysCoresFileName = _ChSysCoresFileName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 2),
    _ChSysCoresFileName_Type()
)
chSysCoresFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresFileName.setStatus("current")
_ChSysCoresTimeCreated_Type = F10SwDate
_ChSysCoresTimeCreated_Object = MibTableColumn
chSysCoresTimeCreated = _ChSysCoresTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 3),
    _ChSysCoresTimeCreated_Type()
)
chSysCoresTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresTimeCreated.setStatus("current")
_ChSysCoresProcessorName_Type = DisplayString
_ChSysCoresProcessorName_Object = MibTableColumn
chSysCoresProcessorName = _ChSysCoresProcessorName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 4),
    _ChSysCoresProcessorName_Type()
)
chSysCoresProcessorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresProcessorName.setStatus("current")
_ChSysCoresProcess_Type = DisplayString
_ChSysCoresProcess_Object = MibTableColumn
chSysCoresProcess = _ChSysCoresProcess_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 5),
    _ChSysCoresProcess_Type()
)
chSysCoresProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCoresProcess.setStatus("current")
_F10ZSeriesChassisMibConformance_ObjectIdentity = ObjectIdentity
f10ZSeriesChassisMibConformance = _F10ZSeriesChassisMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 2)
)
_F10ZSeriesChassisMibCompliances_ObjectIdentity = ObjectIdentity
f10ZSeriesChassisMibCompliances = _F10ZSeriesChassisMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 1)
)
_F10ZSeriesChassisMibGroups_ObjectIdentity = ObjectIdentity
f10ZSeriesChassisMibGroups = _F10ZSeriesChassisMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 2)
)

# Managed Objects groups

f10ZSeriesComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 2, 1)
)
f10ZSeriesComponentGroup.setObjects(
      *(("F10-Z-SERIES-CHASSIS-MIB", "chType"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSwVersion"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chMacAddr"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSerialNumber"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chPartNum"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chProductRev"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chVendorId"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chMfgDate"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chCountryCode"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chPiecePartID"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chPPIDRevision"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chServiceTag"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chExpressServiceCode"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chNum10GigEtherPorts"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chNum40GigEtherPorts"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chNumLineCards"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chNumFanTrays"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chNumPowerSupplies"))
)
if mibBuilder.loadTexts:
    f10ZSeriesComponentGroup.setStatus("current")

f10ZSeriesSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 2, 2)
)
f10ZSeriesSystemGroup.setObjects(
      *(("F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorType"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorUpTime"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorMemSize"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleRuntimeImgVersion"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleRuntimeImgDate"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleBootFlashImgVersion"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleBootSelectorImgVersion"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleNextRebootImage"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleCurrentBootImage"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleInPartitionAImgVers"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleInPartitionBImgVers"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtil5Sec"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtil1Min"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtil5Min"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtilMemUsage"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtilFlashUsage"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardType"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardDescription"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardStatus"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardTemp"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardNum10GigEtherPorts"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardNum40GigEtherPorts"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortType"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortAdminStatus"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortOperStatus"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortIfIndex"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortXfpRxPower"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortXfpRxTemp"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortXfpTxPower"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyOperStatus"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyType"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyPiecePartID"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyPPIDRevision"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyServiceTag"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyExpressServiceCode"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyUsage"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayOperStatus"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayPiecePartID"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayPPIDRevision"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayServiceTag"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayExpressServiceCode"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresInstance"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresFileName"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresTimeCreated"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresProcessorName"),
        ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresProcess"))
)
if mibBuilder.loadTexts:
    f10ZSeriesSystemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f10ZSeriesChassisMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f10ZSeriesChassisMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-Z-SERIES-CHASSIS-MIB",
    **{"f10ZSerChassisMib": f10ZSerChassisMib,
       "f10ZSerChassisObject": f10ZSerChassisObject,
       "chObjects": chObjects,
       "chType": chType,
       "chSwVersion": chSwVersion,
       "chMacAddr": chMacAddr,
       "chSerialNumber": chSerialNumber,
       "chPartNum": chPartNum,
       "chProductRev": chProductRev,
       "chVendorId": chVendorId,
       "chMfgDate": chMfgDate,
       "chCountryCode": chCountryCode,
       "chPiecePartID": chPiecePartID,
       "chPPIDRevision": chPPIDRevision,
       "chServiceTag": chServiceTag,
       "chExpressServiceCode": chExpressServiceCode,
       "chNum10GigEtherPorts": chNum10GigEtherPorts,
       "chNum40GigEtherPorts": chNum40GigEtherPorts,
       "chNumLineCards": chNumLineCards,
       "chNumFanTrays": chNumFanTrays,
       "chNumPowerSupplies": chNumPowerSupplies,
       "chSysObjects": chSysObjects,
       "chSysProcessorTable": chSysProcessorTable,
       "chSysProcessorEntry": chSysProcessorEntry,
       "chSysProcessorIndex": chSysProcessorIndex,
       "chSysProcessorType": chSysProcessorType,
       "chSysProcessorUpTime": chSysProcessorUpTime,
       "chSysProcessorMemSize": chSysProcessorMemSize,
       "chSysSwModuleTable": chSysSwModuleTable,
       "chSysSwModuleEntry": chSysSwModuleEntry,
       "chSysSwModuleRuntimeImgVersion": chSysSwModuleRuntimeImgVersion,
       "chSysSwModuleRuntimeImgDate": chSysSwModuleRuntimeImgDate,
       "chSysSwModuleBootFlashImgVersion": chSysSwModuleBootFlashImgVersion,
       "chSysSwModuleBootSelectorImgVersion": chSysSwModuleBootSelectorImgVersion,
       "chSysSwModuleNextRebootImage": chSysSwModuleNextRebootImage,
       "chSysSwModuleCurrentBootImage": chSysSwModuleCurrentBootImage,
       "chSysSwModuleInPartitionAImgVers": chSysSwModuleInPartitionAImgVers,
       "chSysSwModuleInPartitionBImgVers": chSysSwModuleInPartitionBImgVers,
       "chSysCpuUtilTable": chSysCpuUtilTable,
       "chSysCpuUtilEntry": chSysCpuUtilEntry,
       "chSysCpuUtil5Sec": chSysCpuUtil5Sec,
       "chSysCpuUtil1Min": chSysCpuUtil1Min,
       "chSysCpuUtil5Min": chSysCpuUtil5Min,
       "chSysCpuUtilMemUsage": chSysCpuUtilMemUsage,
       "chSysCpuUtilFlashUsage": chSysCpuUtilFlashUsage,
       "chSysLineCardTable": chSysLineCardTable,
       "chSysLineCardEntry": chSysLineCardEntry,
       "chSysLineCardIndex": chSysLineCardIndex,
       "chSysLineCardType": chSysLineCardType,
       "chSysLineCardDescription": chSysLineCardDescription,
       "chSysLineCardStatus": chSysLineCardStatus,
       "chSysLineCardTemp": chSysLineCardTemp,
       "chSysLineCardNum10GigEtherPorts": chSysLineCardNum10GigEtherPorts,
       "chSysLineCardNum40GigEtherPorts": chSysLineCardNum40GigEtherPorts,
       "chSysPortTable": chSysPortTable,
       "chSysPortEntry": chSysPortEntry,
       "chSysPortIndex": chSysPortIndex,
       "chSysPortType": chSysPortType,
       "chSysPortAdminStatus": chSysPortAdminStatus,
       "chSysPortOperStatus": chSysPortOperStatus,
       "chSysPortIfIndex": chSysPortIfIndex,
       "chSysPortXfpRxPower": chSysPortXfpRxPower,
       "chSysPortXfpRxTemp": chSysPortXfpRxTemp,
       "chSysPortXfpTxPower": chSysPortXfpTxPower,
       "chSysPowerSupplyTable": chSysPowerSupplyTable,
       "chSysPowerSupplyEntry": chSysPowerSupplyEntry,
       "chSysPowerSupplyIndex": chSysPowerSupplyIndex,
       "chSysPowerSupplyOperStatus": chSysPowerSupplyOperStatus,
       "chSysPowerSupplyType": chSysPowerSupplyType,
       "chSysPowerSupplyPiecePartID": chSysPowerSupplyPiecePartID,
       "chSysPowerSupplyPPIDRevision": chSysPowerSupplyPPIDRevision,
       "chSysPowerSupplyServiceTag": chSysPowerSupplyServiceTag,
       "chSysPowerSupplyExpressServiceCode": chSysPowerSupplyExpressServiceCode,
       "chSysPowerSupplyUsage": chSysPowerSupplyUsage,
       "chSysFanTrayTable": chSysFanTrayTable,
       "chSysFanTrayEntry": chSysFanTrayEntry,
       "chSysFanTrayIndex": chSysFanTrayIndex,
       "chSysFanTrayOperStatus": chSysFanTrayOperStatus,
       "chSysFanTrayPiecePartID": chSysFanTrayPiecePartID,
       "chSysFanTrayPPIDRevision": chSysFanTrayPPIDRevision,
       "chSysFanTrayServiceTag": chSysFanTrayServiceTag,
       "chSysFanTrayExpressServiceCode": chSysFanTrayExpressServiceCode,
       "chSysSwCoresTable": chSysSwCoresTable,
       "chSysCoresEntry": chSysCoresEntry,
       "chSysCoresInstance": chSysCoresInstance,
       "chSysCoresFileName": chSysCoresFileName,
       "chSysCoresTimeCreated": chSysCoresTimeCreated,
       "chSysCoresProcessorName": chSysCoresProcessorName,
       "chSysCoresProcess": chSysCoresProcess,
       "f10ZSeriesChassisMibConformance": f10ZSeriesChassisMibConformance,
       "f10ZSeriesChassisMibCompliances": f10ZSeriesChassisMibCompliances,
       "f10ZSeriesChassisMibCompliance": f10ZSeriesChassisMibCompliance,
       "f10ZSeriesChassisMibGroups": f10ZSeriesChassisMibGroups,
       "f10ZSeriesComponentGroup": f10ZSeriesComponentGroup,
       "f10ZSeriesSystemGroup": f10ZSeriesSystemGroup}
)
