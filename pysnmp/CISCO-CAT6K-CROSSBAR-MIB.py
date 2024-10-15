# SNMP MIB module (CISCO-CAT6K-CROSSBAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CAT6K-CROSSBAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:01 2024
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

(Percent,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalDescr,
 entPhysicalIndex,
 entPhysicalName,
 entPhysicalVendorType) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex",
    "entPhysicalName",
    "entPhysicalVendorType")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCat6kCrossbarMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217)
)
ciscoCat6kCrossbarMIB.setRevisions(
        ("2013-09-16 00:00",
         "2012-05-31 00:00",
         "2009-02-15 00:00",
         "2007-12-18 00:00",
         "2006-12-19 00:00",
         "2004-11-19 00:00",
         "2004-08-11 00:00",
         "2004-06-11 00:00",
         "2003-09-29 00:00",
         "2003-04-02 00:00",
         "2002-12-05 00:00",
         "2001-06-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ModuleSlotNumber(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class FabricChannelNumber(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class ChannelStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("bufferError", 5),
          ("crcError", 4),
          ("heartbeatError", 3),
          ("ok", 1),
          ("syncError", 2),
          ("timeoutError", 6),
          ("unused", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCat6kXbarMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCat6kXbarMIBNotifs = _CiscoCat6kXbarMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 0)
)
_CiscoCat6kXbarMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCat6kXbarMIBObjects = _CiscoCat6kXbarMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1)
)
_Cc6kxbarConfiguration_ObjectIdentity = ObjectIdentity
cc6kxbarConfiguration = _Cc6kxbarConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1)
)


class _Cc6kxbarFallbackMode_Type(TruthValue):
    """Custom type cc6kxbarFallbackMode based on TruthValue"""


_Cc6kxbarFallbackMode_Object = MibScalar
cc6kxbarFallbackMode = _Cc6kxbarFallbackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 1),
    _Cc6kxbarFallbackMode_Type()
)
cc6kxbarFallbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarFallbackMode.setStatus("current")
_Cc6kxbarBusOnlyModeAllowed_Type = TruthValue
_Cc6kxbarBusOnlyModeAllowed_Object = MibScalar
cc6kxbarBusOnlyModeAllowed = _Cc6kxbarBusOnlyModeAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 2),
    _Cc6kxbarBusOnlyModeAllowed_Type()
)
cc6kxbarBusOnlyModeAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarBusOnlyModeAllowed.setStatus("current")
_Cc6kxbarTruncatedModeAllowed_Type = TruthValue
_Cc6kxbarTruncatedModeAllowed_Object = MibScalar
cc6kxbarTruncatedModeAllowed = _Cc6kxbarTruncatedModeAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 3),
    _Cc6kxbarTruncatedModeAllowed_Type()
)
cc6kxbarTruncatedModeAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTruncatedModeAllowed.setStatus("current")
_Cc6kxbarMinFabricPresent_Type = Unsigned32
_Cc6kxbarMinFabricPresent_Object = MibScalar
cc6kxbarMinFabricPresent = _Cc6kxbarMinFabricPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 4),
    _Cc6kxbarMinFabricPresent_Type()
)
cc6kxbarMinFabricPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarMinFabricPresent.setStatus("current")
_Cc6kxbarLcdBannerTable_Object = MibTable
cc6kxbarLcdBannerTable = _Cc6kxbarLcdBannerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cc6kxbarLcdBannerTable.setStatus("current")
_Cc6kxbarLcdBannerEntry_Object = MibTableRow
cc6kxbarLcdBannerEntry = _Cc6kxbarLcdBannerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 5, 1)
)
cc6kxbarLcdBannerEntry.setIndexNames(
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarLcdBannerIndex"),
)
if mibBuilder.loadTexts:
    cc6kxbarLcdBannerEntry.setStatus("current")
_Cc6kxbarLcdBannerIndex_Type = Unsigned32
_Cc6kxbarLcdBannerIndex_Object = MibTableColumn
cc6kxbarLcdBannerIndex = _Cc6kxbarLcdBannerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 5, 1, 1),
    _Cc6kxbarLcdBannerIndex_Type()
)
cc6kxbarLcdBannerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarLcdBannerIndex.setStatus("current")
_Cc6kxbarLcdBannerBanner_Type = DisplayString
_Cc6kxbarLcdBannerBanner_Object = MibTableColumn
cc6kxbarLcdBannerBanner = _Cc6kxbarLcdBannerBanner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 5, 1, 2),
    _Cc6kxbarLcdBannerBanner_Type()
)
cc6kxbarLcdBannerBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarLcdBannerBanner.setStatus("current")
_Cc6kxbarLcdBannerMaxSize_Type = Unsigned32
_Cc6kxbarLcdBannerMaxSize_Object = MibTableColumn
cc6kxbarLcdBannerMaxSize = _Cc6kxbarLcdBannerMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 5, 1, 3),
    _Cc6kxbarLcdBannerMaxSize_Type()
)
cc6kxbarLcdBannerMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarLcdBannerMaxSize.setStatus("current")
_Cc6kxbarTruncatedModeOper_Type = TruthValue
_Cc6kxbarTruncatedModeOper_Object = MibScalar
cc6kxbarTruncatedModeOper = _Cc6kxbarTruncatedModeOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 6),
    _Cc6kxbarTruncatedModeOper_Type()
)
cc6kxbarTruncatedModeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarTruncatedModeOper.setStatus("current")
_Cc6kxbarDcefOnlyModeAllowed_Type = TruthValue
_Cc6kxbarDcefOnlyModeAllowed_Object = MibScalar
cc6kxbarDcefOnlyModeAllowed = _Cc6kxbarDcefOnlyModeAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 7),
    _Cc6kxbarDcefOnlyModeAllowed_Type()
)
cc6kxbarDcefOnlyModeAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarDcefOnlyModeAllowed.setStatus("current")
_Cc6kxbarForceBusMode_Type = TruthValue
_Cc6kxbarForceBusMode_Object = MibScalar
cc6kxbarForceBusMode = _Cc6kxbarForceBusMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 8),
    _Cc6kxbarForceBusMode_Type()
)
cc6kxbarForceBusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarForceBusMode.setStatus("current")
_Cc6kxbarBusOnlyModeOper_Type = TruthValue
_Cc6kxbarBusOnlyModeOper_Object = MibScalar
cc6kxbarBusOnlyModeOper = _Cc6kxbarBusOnlyModeOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 1, 9),
    _Cc6kxbarBusOnlyModeOper_Type()
)
cc6kxbarBusOnlyModeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarBusOnlyModeOper.setStatus("current")
_Cc6kxbarStatus_ObjectIdentity = ObjectIdentity
cc6kxbarStatus = _Cc6kxbarStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2)
)
_Cc6kxbarFabricActiveSlot_Type = ModuleSlotNumber
_Cc6kxbarFabricActiveSlot_Object = MibScalar
cc6kxbarFabricActiveSlot = _Cc6kxbarFabricActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 1),
    _Cc6kxbarFabricActiveSlot_Type()
)
cc6kxbarFabricActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarFabricActiveSlot.setStatus("current")
_Cc6kxbarFabricBackupSlot_Type = ModuleSlotNumber
_Cc6kxbarFabricBackupSlot_Object = MibScalar
cc6kxbarFabricBackupSlot = _Cc6kxbarFabricBackupSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 2),
    _Cc6kxbarFabricBackupSlot_Type()
)
cc6kxbarFabricBackupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarFabricBackupSlot.setStatus("current")
_Cc6kxbarModuleModeTable_Object = MibTable
cc6kxbarModuleModeTable = _Cc6kxbarModuleModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cc6kxbarModuleModeTable.setStatus("current")
_Cc6kxbarModuleModeEntry_Object = MibTableRow
cc6kxbarModuleModeEntry = _Cc6kxbarModuleModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 3, 1)
)
cc6kxbarModuleModeEntry.setIndexNames(
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarModuleModeModule"),
)
if mibBuilder.loadTexts:
    cc6kxbarModuleModeEntry.setStatus("current")
_Cc6kxbarModuleModeModule_Type = ModuleSlotNumber
_Cc6kxbarModuleModeModule_Object = MibTableColumn
cc6kxbarModuleModeModule = _Cc6kxbarModuleModeModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 3, 1, 1),
    _Cc6kxbarModuleModeModule_Type()
)
cc6kxbarModuleModeModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarModuleModeModule.setStatus("current")


class _Cc6kxbarModuleModeSwitchingMode_Type(Integer32):
    """Custom type cc6kxbarModuleModeSwitchingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busmode", 1),
          ("crossbarmode", 2),
          ("dcefmode", 3))
    )


_Cc6kxbarModuleModeSwitchingMode_Type.__name__ = "Integer32"
_Cc6kxbarModuleModeSwitchingMode_Object = MibTableColumn
cc6kxbarModuleModeSwitchingMode = _Cc6kxbarModuleModeSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 3, 1, 2),
    _Cc6kxbarModuleModeSwitchingMode_Type()
)
cc6kxbarModuleModeSwitchingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarModuleModeSwitchingMode.setStatus("current")
_Cc6kxbarModuleChannelTable_Object = MibTable
cc6kxbarModuleChannelTable = _Cc6kxbarModuleChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cc6kxbarModuleChannelTable.setStatus("current")
_Cc6kxbarModuleChannelEntry_Object = MibTableRow
cc6kxbarModuleChannelEntry = _Cc6kxbarModuleChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 4, 1)
)
cc6kxbarModuleChannelEntry.setIndexNames(
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarModuleChannelModule"),
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarModuleChannelChannel"),
)
if mibBuilder.loadTexts:
    cc6kxbarModuleChannelEntry.setStatus("current")
_Cc6kxbarModuleChannelModule_Type = ModuleSlotNumber
_Cc6kxbarModuleChannelModule_Object = MibTableColumn
cc6kxbarModuleChannelModule = _Cc6kxbarModuleChannelModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 4, 1, 1),
    _Cc6kxbarModuleChannelModule_Type()
)
cc6kxbarModuleChannelModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarModuleChannelModule.setStatus("current")
_Cc6kxbarModuleChannelChannel_Type = FabricChannelNumber
_Cc6kxbarModuleChannelChannel_Object = MibTableColumn
cc6kxbarModuleChannelChannel = _Cc6kxbarModuleChannelChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 4, 1, 2),
    _Cc6kxbarModuleChannelChannel_Type()
)
cc6kxbarModuleChannelChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarModuleChannelChannel.setStatus("current")
_Cc6kxbarModuleChannelModStatus_Type = ChannelStatus
_Cc6kxbarModuleChannelModStatus_Object = MibTableColumn
cc6kxbarModuleChannelModStatus = _Cc6kxbarModuleChannelModStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 4, 1, 3),
    _Cc6kxbarModuleChannelModStatus_Type()
)
cc6kxbarModuleChannelModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarModuleChannelModStatus.setStatus("current")
_Cc6kxbarModuleChannelFabStatus_Type = ChannelStatus
_Cc6kxbarModuleChannelFabStatus_Object = MibTableColumn
cc6kxbarModuleChannelFabStatus = _Cc6kxbarModuleChannelFabStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 4, 1, 4),
    _Cc6kxbarModuleChannelFabStatus_Type()
)
cc6kxbarModuleChannelFabStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarModuleChannelFabStatus.setStatus("current")
_Cc6kxbarModuleChannelSpeed_Type = Gauge32
_Cc6kxbarModuleChannelSpeed_Object = MibTableColumn
cc6kxbarModuleChannelSpeed = _Cc6kxbarModuleChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 2, 4, 1, 5),
    _Cc6kxbarModuleChannelSpeed_Type()
)
cc6kxbarModuleChannelSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarModuleChannelSpeed.setStatus("current")
_Cc6kxbarStatistics_ObjectIdentity = ObjectIdentity
cc6kxbarStatistics = _Cc6kxbarStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3)
)
_Cc6kxbarStatisticsTable_Object = MibTable
cc6kxbarStatisticsTable = _Cc6kxbarStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cc6kxbarStatisticsTable.setStatus("current")
_Cc6kxbarStatisticsEntry_Object = MibTableRow
cc6kxbarStatisticsEntry = _Cc6kxbarStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1)
)
cc6kxbarStatisticsEntry.setIndexNames(
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsModule"),
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsChannel"),
)
if mibBuilder.loadTexts:
    cc6kxbarStatisticsEntry.setStatus("current")
_Cc6kxbarStatisticsModule_Type = ModuleSlotNumber
_Cc6kxbarStatisticsModule_Object = MibTableColumn
cc6kxbarStatisticsModule = _Cc6kxbarStatisticsModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 1),
    _Cc6kxbarStatisticsModule_Type()
)
cc6kxbarStatisticsModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsModule.setStatus("current")
_Cc6kxbarStatisticsChannel_Type = FabricChannelNumber
_Cc6kxbarStatisticsChannel_Object = MibTableColumn
cc6kxbarStatisticsChannel = _Cc6kxbarStatisticsChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 2),
    _Cc6kxbarStatisticsChannel_Type()
)
cc6kxbarStatisticsChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsChannel.setStatus("current")
_Cc6kxbarStatisticsInErrors_Type = Counter32
_Cc6kxbarStatisticsInErrors_Object = MibTableColumn
cc6kxbarStatisticsInErrors = _Cc6kxbarStatisticsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 3),
    _Cc6kxbarStatisticsInErrors_Type()
)
cc6kxbarStatisticsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsInErrors.setStatus("current")
_Cc6kxbarStatisticsOutErrors_Type = Counter32
_Cc6kxbarStatisticsOutErrors_Object = MibTableColumn
cc6kxbarStatisticsOutErrors = _Cc6kxbarStatisticsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 4),
    _Cc6kxbarStatisticsOutErrors_Type()
)
cc6kxbarStatisticsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsOutErrors.setStatus("current")
_Cc6kxbarStatisticsOutDropped_Type = Counter32
_Cc6kxbarStatisticsOutDropped_Object = MibTableColumn
cc6kxbarStatisticsOutDropped = _Cc6kxbarStatisticsOutDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 5),
    _Cc6kxbarStatisticsOutDropped_Type()
)
cc6kxbarStatisticsOutDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsOutDropped.setStatus("current")
_Cc6kxbarStatisticsInUtil_Type = Percent
_Cc6kxbarStatisticsInUtil_Object = MibTableColumn
cc6kxbarStatisticsInUtil = _Cc6kxbarStatisticsInUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 6),
    _Cc6kxbarStatisticsInUtil_Type()
)
cc6kxbarStatisticsInUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsInUtil.setStatus("current")
_Cc6kxbarStatisticsOutUtil_Type = Percent
_Cc6kxbarStatisticsOutUtil_Object = MibTableColumn
cc6kxbarStatisticsOutUtil = _Cc6kxbarStatisticsOutUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 7),
    _Cc6kxbarStatisticsOutUtil_Type()
)
cc6kxbarStatisticsOutUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsOutUtil.setStatus("current")
_Cc6kxbarStatisticsPeakInUtil_Type = Percent
_Cc6kxbarStatisticsPeakInUtil_Object = MibTableColumn
cc6kxbarStatisticsPeakInUtil = _Cc6kxbarStatisticsPeakInUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 8),
    _Cc6kxbarStatisticsPeakInUtil_Type()
)
cc6kxbarStatisticsPeakInUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsPeakInUtil.setStatus("current")
_Cc6kxbarStatisticsPeakTmInUtil_Type = DateAndTime
_Cc6kxbarStatisticsPeakTmInUtil_Object = MibTableColumn
cc6kxbarStatisticsPeakTmInUtil = _Cc6kxbarStatisticsPeakTmInUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 9),
    _Cc6kxbarStatisticsPeakTmInUtil_Type()
)
cc6kxbarStatisticsPeakTmInUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsPeakTmInUtil.setStatus("current")
_Cc6kxbarStatisticsPeakOutUtil_Type = Percent
_Cc6kxbarStatisticsPeakOutUtil_Object = MibTableColumn
cc6kxbarStatisticsPeakOutUtil = _Cc6kxbarStatisticsPeakOutUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 10),
    _Cc6kxbarStatisticsPeakOutUtil_Type()
)
cc6kxbarStatisticsPeakOutUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsPeakOutUtil.setStatus("current")
_Cc6kxbarStatisticsPeakTmOutUtil_Type = DateAndTime
_Cc6kxbarStatisticsPeakTmOutUtil_Object = MibTableColumn
cc6kxbarStatisticsPeakTmOutUtil = _Cc6kxbarStatisticsPeakTmOutUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 11),
    _Cc6kxbarStatisticsPeakTmOutUtil_Type()
)
cc6kxbarStatisticsPeakTmOutUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsPeakTmOutUtil.setStatus("current")
_Cc6kxbarStatisticsLbusDrops_Type = Counter32
_Cc6kxbarStatisticsLbusDrops_Object = MibTableColumn
cc6kxbarStatisticsLbusDrops = _Cc6kxbarStatisticsLbusDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 1, 1, 12),
    _Cc6kxbarStatisticsLbusDrops_Type()
)
cc6kxbarStatisticsLbusDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarStatisticsLbusDrops.setStatus("current")
_Cc6kxbarErrorTable_Object = MibTable
cc6kxbarErrorTable = _Cc6kxbarErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cc6kxbarErrorTable.setStatus("current")
_Cc6kxbarErrorEntry_Object = MibTableRow
cc6kxbarErrorEntry = _Cc6kxbarErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1)
)
cc6kxbarErrorEntry.setIndexNames(
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrorModule"),
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrorChannel"),
)
if mibBuilder.loadTexts:
    cc6kxbarErrorEntry.setStatus("current")
_Cc6kxbarErrorModule_Type = ModuleSlotNumber
_Cc6kxbarErrorModule_Object = MibTableColumn
cc6kxbarErrorModule = _Cc6kxbarErrorModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1, 1),
    _Cc6kxbarErrorModule_Type()
)
cc6kxbarErrorModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarErrorModule.setStatus("current")
_Cc6kxbarErrorChannel_Type = FabricChannelNumber
_Cc6kxbarErrorChannel_Object = MibTableColumn
cc6kxbarErrorChannel = _Cc6kxbarErrorChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1, 2),
    _Cc6kxbarErrorChannel_Type()
)
cc6kxbarErrorChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarErrorChannel.setStatus("current")
_Cc6kxbarErrorModuleCrc_Type = Gauge32
_Cc6kxbarErrorModuleCrc_Object = MibTableColumn
cc6kxbarErrorModuleCrc = _Cc6kxbarErrorModuleCrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1, 3),
    _Cc6kxbarErrorModuleCrc_Type()
)
cc6kxbarErrorModuleCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarErrorModuleCrc.setStatus("current")
_Cc6kxbarErrorModuleHbeat_Type = Gauge32
_Cc6kxbarErrorModuleHbeat_Object = MibTableColumn
cc6kxbarErrorModuleHbeat = _Cc6kxbarErrorModuleHbeat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1, 4),
    _Cc6kxbarErrorModuleHbeat_Type()
)
cc6kxbarErrorModuleHbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarErrorModuleHbeat.setStatus("current")
_Cc6kxbarErrorModuleSync_Type = Gauge32
_Cc6kxbarErrorModuleSync_Object = MibTableColumn
cc6kxbarErrorModuleSync = _Cc6kxbarErrorModuleSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1, 5),
    _Cc6kxbarErrorModuleSync_Type()
)
cc6kxbarErrorModuleSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarErrorModuleSync.setStatus("current")
_Cc6kxbarErrorModuleDDRSync_Type = Gauge32
_Cc6kxbarErrorModuleDDRSync_Object = MibTableColumn
cc6kxbarErrorModuleDDRSync = _Cc6kxbarErrorModuleDDRSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1, 6),
    _Cc6kxbarErrorModuleDDRSync_Type()
)
cc6kxbarErrorModuleDDRSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarErrorModuleDDRSync.setStatus("current")
_Cc6kxbarErrorChannelSync_Type = Gauge32
_Cc6kxbarErrorChannelSync_Object = MibTableColumn
cc6kxbarErrorChannelSync = _Cc6kxbarErrorChannelSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1, 7),
    _Cc6kxbarErrorChannelSync_Type()
)
cc6kxbarErrorChannelSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarErrorChannelSync.setStatus("current")
_Cc6kxbarErrorChannelBuffer_Type = Gauge32
_Cc6kxbarErrorChannelBuffer_Object = MibTableColumn
cc6kxbarErrorChannelBuffer = _Cc6kxbarErrorChannelBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1, 8),
    _Cc6kxbarErrorChannelBuffer_Type()
)
cc6kxbarErrorChannelBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarErrorChannelBuffer.setStatus("current")
_Cc6kxbarErrorChannelTimeout_Type = Gauge32
_Cc6kxbarErrorChannelTimeout_Object = MibTableColumn
cc6kxbarErrorChannelTimeout = _Cc6kxbarErrorChannelTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 3, 2, 1, 9),
    _Cc6kxbarErrorChannelTimeout_Type()
)
cc6kxbarErrorChannelTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarErrorChannelTimeout.setStatus("current")
_Cc6kxbarSwBusObjects_ObjectIdentity = ObjectIdentity
cc6kxbarSwBusObjects = _Cc6kxbarSwBusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 4)
)


class _Cc6kxbarSwBusSwitchingStatus_Type(Integer32):
    """Custom type cc6kxbarSwBusSwitchingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 3),
          ("normal", 1),
          ("stalled", 2))
    )


_Cc6kxbarSwBusSwitchingStatus_Type.__name__ = "Integer32"
_Cc6kxbarSwBusSwitchingStatus_Object = MibScalar
cc6kxbarSwBusSwitchingStatus = _Cc6kxbarSwBusSwitchingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 4, 1),
    _Cc6kxbarSwBusSwitchingStatus_Type()
)
cc6kxbarSwBusSwitchingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarSwBusSwitchingStatus.setStatus("current")
_Cc6kxbarSwBusFailureDuration_Type = Unsigned32
_Cc6kxbarSwBusFailureDuration_Object = MibScalar
cc6kxbarSwBusFailureDuration = _Cc6kxbarSwBusFailureDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 4, 2),
    _Cc6kxbarSwBusFailureDuration_Type()
)
cc6kxbarSwBusFailureDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarSwBusFailureDuration.setStatus("current")
if mibBuilder.loadTexts:
    cc6kxbarSwBusFailureDuration.setUnits("seconds")
_Cc6kxbarSwBusNotifEnable_Type = TruthValue
_Cc6kxbarSwBusNotifEnable_Object = MibScalar
cc6kxbarSwBusNotifEnable = _Cc6kxbarSwBusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 4, 3),
    _Cc6kxbarSwBusNotifEnable_Type()
)
cc6kxbarSwBusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarSwBusNotifEnable.setStatus("current")
_Cc6kxbarSwBusUtilization_Type = Percent
_Cc6kxbarSwBusUtilization_Object = MibScalar
cc6kxbarSwBusUtilization = _Cc6kxbarSwBusUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 4, 4),
    _Cc6kxbarSwBusUtilization_Type()
)
cc6kxbarSwBusUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarSwBusUtilization.setStatus("current")
_Cc6kxbarSwBusPeakUtilization_Type = Percent
_Cc6kxbarSwBusPeakUtilization_Object = MibScalar
cc6kxbarSwBusPeakUtilization = _Cc6kxbarSwBusPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 4, 5),
    _Cc6kxbarSwBusPeakUtilization_Type()
)
cc6kxbarSwBusPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarSwBusPeakUtilization.setStatus("current")
_Cc6kxbarSwBusPeakTimeUtil_Type = DateAndTime
_Cc6kxbarSwBusPeakTimeUtil_Object = MibScalar
cc6kxbarSwBusPeakTimeUtil = _Cc6kxbarSwBusPeakTimeUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 4, 6),
    _Cc6kxbarSwBusPeakTimeUtil_Type()
)
cc6kxbarSwBusPeakTimeUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarSwBusPeakTimeUtil.setStatus("current")
_Cc6kxbarIntBusObjects_ObjectIdentity = ObjectIdentity
cc6kxbarIntBusObjects = _Cc6kxbarIntBusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 5)
)


class _Cc6kxbarIntBusNotifEnable_Type(Bits):
    """Custom type cc6kxbarIntBusNotifEnable based on Bits"""
    namedValues = NamedValues(
        *(("intBusCRCErrExcd", 0),
          ("intBusCRCErrRcvrd", 1))
    )

_Cc6kxbarIntBusNotifEnable_Type.__name__ = "Bits"
_Cc6kxbarIntBusNotifEnable_Object = MibScalar
cc6kxbarIntBusNotifEnable = _Cc6kxbarIntBusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 5, 1),
    _Cc6kxbarIntBusNotifEnable_Type()
)
cc6kxbarIntBusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarIntBusNotifEnable.setStatus("current")
_Cc6kxbarIntBusCRCErrTable_Object = MibTable
cc6kxbarIntBusCRCErrTable = _Cc6kxbarIntBusCRCErrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cc6kxbarIntBusCRCErrTable.setStatus("current")
_Cc6kxbarIntBusCRCErrEntry_Object = MibTableRow
cc6kxbarIntBusCRCErrEntry = _Cc6kxbarIntBusCRCErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 5, 2, 1)
)
cc6kxbarIntBusCRCErrEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cc6kxbarIntBusCRCErrEntry.setStatus("current")
_Cc6kxbarIntBusCRCErrExcdStatus_Type = TruthValue
_Cc6kxbarIntBusCRCErrExcdStatus_Object = MibTableColumn
cc6kxbarIntBusCRCErrExcdStatus = _Cc6kxbarIntBusCRCErrExcdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 5, 2, 1, 1),
    _Cc6kxbarIntBusCRCErrExcdStatus_Type()
)
cc6kxbarIntBusCRCErrExcdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarIntBusCRCErrExcdStatus.setStatus("current")
_Cc6kxbarIntBusCRCErrExcdCount_Type = Unsigned32
_Cc6kxbarIntBusCRCErrExcdCount_Object = MibTableColumn
cc6kxbarIntBusCRCErrExcdCount = _Cc6kxbarIntBusCRCErrExcdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 5, 2, 1, 2),
    _Cc6kxbarIntBusCRCErrExcdCount_Type()
)
cc6kxbarIntBusCRCErrExcdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarIntBusCRCErrExcdCount.setStatus("current")
_Cc6kxbarFlowCtrlObjects_ObjectIdentity = ObjectIdentity
cc6kxbarFlowCtrlObjects = _Cc6kxbarFlowCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 6)
)


class _Cc6kxbarFlowCtrlNotifEnable_Type(Bits):
    """Custom type cc6kxbarFlowCtrlNotifEnable based on Bits"""
    namedValues = NamedValues(
        ("busThreshExcd", 0)
    )

_Cc6kxbarFlowCtrlNotifEnable_Type.__name__ = "Bits"
_Cc6kxbarFlowCtrlNotifEnable_Object = MibScalar
cc6kxbarFlowCtrlNotifEnable = _Cc6kxbarFlowCtrlNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 6, 1),
    _Cc6kxbarFlowCtrlNotifEnable_Type()
)
cc6kxbarFlowCtrlNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarFlowCtrlNotifEnable.setStatus("current")


class _Cc6kxbarFlowCtrlBusFIFOThrMode_Type(Integer32):
    """Custom type cc6kxbarFlowCtrlBusFIFOThrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("off", 1),
          ("on", 2))
    )


_Cc6kxbarFlowCtrlBusFIFOThrMode_Type.__name__ = "Integer32"
_Cc6kxbarFlowCtrlBusFIFOThrMode_Object = MibScalar
cc6kxbarFlowCtrlBusFIFOThrMode = _Cc6kxbarFlowCtrlBusFIFOThrMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 6, 2),
    _Cc6kxbarFlowCtrlBusFIFOThrMode_Type()
)
cc6kxbarFlowCtrlBusFIFOThrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarFlowCtrlBusFIFOThrMode.setStatus("current")


class _Cc6kxbarFlowCtrlBusFIFOThrValue_Type(Integer32):
    """Custom type cc6kxbarFlowCtrlBusFIFOThrValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 2),
          ("original", 1))
    )


_Cc6kxbarFlowCtrlBusFIFOThrValue_Type.__name__ = "Integer32"
_Cc6kxbarFlowCtrlBusFIFOThrValue_Object = MibScalar
cc6kxbarFlowCtrlBusFIFOThrValue = _Cc6kxbarFlowCtrlBusFIFOThrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 6, 3),
    _Cc6kxbarFlowCtrlBusFIFOThrValue_Type()
)
cc6kxbarFlowCtrlBusFIFOThrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarFlowCtrlBusFIFOThrValue.setStatus("current")
_Cc6kxbarFlowCtrlBusFIFOTransTime_Type = TimeStamp
_Cc6kxbarFlowCtrlBusFIFOTransTime_Object = MibScalar
cc6kxbarFlowCtrlBusFIFOTransTime = _Cc6kxbarFlowCtrlBusFIFOTransTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 6, 4),
    _Cc6kxbarFlowCtrlBusFIFOTransTime_Type()
)
cc6kxbarFlowCtrlBusFIFOTransTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarFlowCtrlBusFIFOTransTime.setStatus("current")
_Cc6kxbarSystemCapacityObjects_ObjectIdentity = ObjectIdentity
cc6kxbarSystemCapacityObjects = _Cc6kxbarSystemCapacityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 7)
)


class _Cc6kxbarSysCapPfcOperMode_Type(Integer32):
    """Custom type cc6kxbarSysCapPfcOperMode based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("pfc3a", 2),
          ("pfc3b", 3),
          ("pfc3bxl", 4),
          ("pfc3c", 7),
          ("pfc3cst1", 5),
          ("pfc3cxl", 8),
          ("pfc3cxlst1", 6),
          ("pfc4", 9),
          ("pfc4lite", 12),
          ("pfc4xl", 10),
          ("pfc4xxl", 11),
          ("unknown", 1))
    )


_Cc6kxbarSysCapPfcOperMode_Type.__name__ = "Integer32"
_Cc6kxbarSysCapPfcOperMode_Object = MibScalar
cc6kxbarSysCapPfcOperMode = _Cc6kxbarSysCapPfcOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 7, 1),
    _Cc6kxbarSysCapPfcOperMode_Type()
)
cc6kxbarSysCapPfcOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarSysCapPfcOperMode.setStatus("current")
_Cc6kxbarSysCapSwitchResTable_Object = MibTable
cc6kxbarSysCapSwitchResTable = _Cc6kxbarSysCapSwitchResTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cc6kxbarSysCapSwitchResTable.setStatus("current")
_Cc6kxbarSysCapSwitchResEntry_Object = MibTableRow
cc6kxbarSysCapSwitchResEntry = _Cc6kxbarSysCapSwitchResEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 7, 2, 1)
)
cc6kxbarSysCapSwitchResEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cc6kxbarSysCapSwitchResEntry.setStatus("current")


class _Cc6kxbarSysCapSwitchResSeries_Type(Integer32):
    """Custom type cc6kxbarSysCapSwitchResSeries based on Integer32"""
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
        *(("cef256", 8),
          ("cef720", 6),
          ("classic", 3),
          ("dcef256", 7),
          ("dcef720", 5),
          ("fabric", 4),
          ("supervisor", 2),
          ("unknown", 1))
    )


_Cc6kxbarSysCapSwitchResSeries_Type.__name__ = "Integer32"
_Cc6kxbarSysCapSwitchResSeries_Object = MibTableColumn
cc6kxbarSysCapSwitchResSeries = _Cc6kxbarSysCapSwitchResSeries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 7, 2, 1, 1),
    _Cc6kxbarSysCapSwitchResSeries_Type()
)
cc6kxbarSysCapSwitchResSeries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarSysCapSwitchResSeries.setStatus("current")


class _Cc6kxbarSysCapSwitchResCefMode_Type(Integer32):
    """Custom type cc6kxbarSysCapSwitchResCefMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cef", 3),
          ("dcef", 2),
          ("notApplicable", 1))
    )


_Cc6kxbarSysCapSwitchResCefMode_Type.__name__ = "Integer32"
_Cc6kxbarSysCapSwitchResCefMode_Object = MibTableColumn
cc6kxbarSysCapSwitchResCefMode = _Cc6kxbarSysCapSwitchResCefMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 7, 2, 1, 2),
    _Cc6kxbarSysCapSwitchResCefMode_Type()
)
cc6kxbarSysCapSwitchResCefMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarSysCapSwitchResCefMode.setStatus("current")
_Cc6kxbarErrorRecoveryObjects_ObjectIdentity = ObjectIdentity
cc6kxbarErrorRecoveryObjects = _Cc6kxbarErrorRecoveryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 8)
)


class _Cc6kxbarErrRcvryThreshLink_Type(Unsigned32):
    """Custom type cc6kxbarErrRcvryThreshLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Cc6kxbarErrRcvryThreshLink_Type.__name__ = "Unsigned32"
_Cc6kxbarErrRcvryThreshLink_Object = MibScalar
cc6kxbarErrRcvryThreshLink = _Cc6kxbarErrRcvryThreshLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 8, 1),
    _Cc6kxbarErrRcvryThreshLink_Type()
)
cc6kxbarErrRcvryThreshLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarErrRcvryThreshLink.setStatus("current")


class _Cc6kxbarErrRcvryThreshPersLink_Type(Unsigned32):
    """Custom type cc6kxbarErrRcvryThreshPersLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Cc6kxbarErrRcvryThreshPersLink_Type.__name__ = "Unsigned32"
_Cc6kxbarErrRcvryThreshPersLink_Object = MibScalar
cc6kxbarErrRcvryThreshPersLink = _Cc6kxbarErrRcvryThreshPersLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 8, 2),
    _Cc6kxbarErrRcvryThreshPersLink_Type()
)
cc6kxbarErrRcvryThreshPersLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarErrRcvryThreshPersLink.setStatus("current")
_Cc6kxbarErrRcvrySwitchoverEnable_Type = TruthValue
_Cc6kxbarErrRcvrySwitchoverEnable_Object = MibScalar
cc6kxbarErrRcvrySwitchoverEnable = _Cc6kxbarErrRcvrySwitchoverEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 8, 3),
    _Cc6kxbarErrRcvrySwitchoverEnable_Type()
)
cc6kxbarErrRcvrySwitchoverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarErrRcvrySwitchoverEnable.setStatus("current")
_Cc6kxbarErrRcvryPersLinkResync_Type = TruthValue
_Cc6kxbarErrRcvryPersLinkResync_Object = MibScalar
cc6kxbarErrRcvryPersLinkResync = _Cc6kxbarErrRcvryPersLinkResync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 8, 4),
    _Cc6kxbarErrRcvryPersLinkResync_Type()
)
cc6kxbarErrRcvryPersLinkResync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarErrRcvryPersLinkResync.setStatus("current")


class _Cc6kxbarErrRcvryChResyncCount_Type(Unsigned32):
    """Custom type cc6kxbarErrRcvryChResyncCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Cc6kxbarErrRcvryChResyncCount_Type.__name__ = "Unsigned32"
_Cc6kxbarErrRcvryChResyncCount_Object = MibScalar
cc6kxbarErrRcvryChResyncCount = _Cc6kxbarErrRcvryChResyncCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 8, 5),
    _Cc6kxbarErrRcvryChResyncCount_Type()
)
cc6kxbarErrRcvryChResyncCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarErrRcvryChResyncCount.setStatus("current")


class _Cc6kxbarErrRcvryChResyncInterval_Type(Unsigned32):
    """Custom type cc6kxbarErrRcvryChResyncInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Cc6kxbarErrRcvryChResyncInterval_Type.__name__ = "Unsigned32"
_Cc6kxbarErrRcvryChResyncInterval_Object = MibScalar
cc6kxbarErrRcvryChResyncInterval = _Cc6kxbarErrRcvryChResyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 8, 6),
    _Cc6kxbarErrRcvryChResyncInterval_Type()
)
cc6kxbarErrRcvryChResyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarErrRcvryChResyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    cc6kxbarErrRcvryChResyncInterval.setUnits("milliseconds")
_Cc6kxbarTrafficMonitorObjects_ObjectIdentity = ObjectIdentity
cc6kxbarTrafficMonitorObjects = _Cc6kxbarTrafficMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9)
)
_Cc6kxbarTrafficMonitorSwBusObjects_ObjectIdentity = ObjectIdentity
cc6kxbarTrafficMonitorSwBusObjects = _Cc6kxbarTrafficMonitorSwBusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 1)
)
_Cc6kxbarTMSwBusUtilEnable_Type = TruthValue
_Cc6kxbarTMSwBusUtilEnable_Object = MibScalar
cc6kxbarTMSwBusUtilEnable = _Cc6kxbarTMSwBusUtilEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 1, 1),
    _Cc6kxbarTMSwBusUtilEnable_Type()
)
cc6kxbarTMSwBusUtilEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilEnable.setStatus("current")


class _Cc6kxbarTMSwBusUtilInterval_Type(Unsigned32):
    """Custom type cc6kxbarTMSwBusUtilInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Cc6kxbarTMSwBusUtilInterval_Type.__name__ = "Unsigned32"
_Cc6kxbarTMSwBusUtilInterval_Object = MibScalar
cc6kxbarTMSwBusUtilInterval = _Cc6kxbarTMSwBusUtilInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 1, 2),
    _Cc6kxbarTMSwBusUtilInterval_Type()
)
cc6kxbarTMSwBusUtilInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilInterval.setStatus("current")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilInterval.setUnits("seconds")
_Cc6kxbarTMSwBusUtilThreshold_Type = Percent
_Cc6kxbarTMSwBusUtilThreshold_Object = MibScalar
cc6kxbarTMSwBusUtilThreshold = _Cc6kxbarTMSwBusUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 1, 3),
    _Cc6kxbarTMSwBusUtilThreshold_Type()
)
cc6kxbarTMSwBusUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilThreshold.setStatus("current")
_Cc6kxbarTMSwBusUtilLogCount_Type = Counter32
_Cc6kxbarTMSwBusUtilLogCount_Object = MibScalar
cc6kxbarTMSwBusUtilLogCount = _Cc6kxbarTMSwBusUtilLogCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 1, 4),
    _Cc6kxbarTMSwBusUtilLogCount_Type()
)
cc6kxbarTMSwBusUtilLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilLogCount.setStatus("current")
_Cc6kxbarTMSwBusUtilLastLogTime_Type = DateAndTime
_Cc6kxbarTMSwBusUtilLastLogTime_Object = MibScalar
cc6kxbarTMSwBusUtilLastLogTime = _Cc6kxbarTMSwBusUtilLastLogTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 1, 5),
    _Cc6kxbarTMSwBusUtilLastLogTime_Type()
)
cc6kxbarTMSwBusUtilLastLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilLastLogTime.setStatus("current")


class _Cc6kxbarTMSwBusUtilLogInterval_Type(Unsigned32):
    """Custom type cc6kxbarTMSwBusUtilLogInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Cc6kxbarTMSwBusUtilLogInterval_Type.__name__ = "Unsigned32"
_Cc6kxbarTMSwBusUtilLogInterval_Object = MibScalar
cc6kxbarTMSwBusUtilLogInterval = _Cc6kxbarTMSwBusUtilLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 1, 6),
    _Cc6kxbarTMSwBusUtilLogInterval_Type()
)
cc6kxbarTMSwBusUtilLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilLogInterval.setStatus("current")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilLogInterval.setUnits("seconds")
_Cc6kxbarTMSwBusUtilUtilization_Type = Percent
_Cc6kxbarTMSwBusUtilUtilization_Object = MibScalar
cc6kxbarTMSwBusUtilUtilization = _Cc6kxbarTMSwBusUtilUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 1, 7),
    _Cc6kxbarTMSwBusUtilUtilization_Type()
)
cc6kxbarTMSwBusUtilUtilization.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilUtilization.setStatus("current")
_Cc6kxbarTMSwBusUtilNotifEnable_Type = TruthValue
_Cc6kxbarTMSwBusUtilNotifEnable_Object = MibScalar
cc6kxbarTMSwBusUtilNotifEnable = _Cc6kxbarTMSwBusUtilNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 1, 8),
    _Cc6kxbarTMSwBusUtilNotifEnable_Type()
)
cc6kxbarTMSwBusUtilNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilNotifEnable.setStatus("current")
_Cc6kxbarTrafficMonitorChObjects_ObjectIdentity = ObjectIdentity
cc6kxbarTrafficMonitorChObjects = _Cc6kxbarTrafficMonitorChObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2)
)
_Cc6kxbarTMChUtilTable_Object = MibTable
cc6kxbarTMChUtilTable = _Cc6kxbarTMChUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilTable.setStatus("current")
_Cc6kxbarTMChUtilEntry_Object = MibTableRow
cc6kxbarTMChUtilEntry = _Cc6kxbarTMChUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1, 1)
)
cc6kxbarTMChUtilEntry.setIndexNames(
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilModule"),
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilChannel"),
    (0, "CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilDirection"),
)
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilEntry.setStatus("current")
_Cc6kxbarTMChUtilModule_Type = ModuleSlotNumber
_Cc6kxbarTMChUtilModule_Object = MibTableColumn
cc6kxbarTMChUtilModule = _Cc6kxbarTMChUtilModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1, 1, 1),
    _Cc6kxbarTMChUtilModule_Type()
)
cc6kxbarTMChUtilModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilModule.setStatus("current")
_Cc6kxbarTMChUtilChannel_Type = FabricChannelNumber
_Cc6kxbarTMChUtilChannel_Object = MibTableColumn
cc6kxbarTMChUtilChannel = _Cc6kxbarTMChUtilChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1, 1, 2),
    _Cc6kxbarTMChUtilChannel_Type()
)
cc6kxbarTMChUtilChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilChannel.setStatus("current")


class _Cc6kxbarTMChUtilDirection_Type(Integer32):
    """Custom type cc6kxbarTMChUtilDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_Cc6kxbarTMChUtilDirection_Type.__name__ = "Integer32"
_Cc6kxbarTMChUtilDirection_Object = MibTableColumn
cc6kxbarTMChUtilDirection = _Cc6kxbarTMChUtilDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1, 1, 3),
    _Cc6kxbarTMChUtilDirection_Type()
)
cc6kxbarTMChUtilDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilDirection.setStatus("current")
_Cc6kxbarTMChUtilEnable_Type = TruthValue
_Cc6kxbarTMChUtilEnable_Object = MibTableColumn
cc6kxbarTMChUtilEnable = _Cc6kxbarTMChUtilEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1, 1, 4),
    _Cc6kxbarTMChUtilEnable_Type()
)
cc6kxbarTMChUtilEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilEnable.setStatus("current")


class _Cc6kxbarTMChUtilInterval_Type(Unsigned32):
    """Custom type cc6kxbarTMChUtilInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Cc6kxbarTMChUtilInterval_Type.__name__ = "Unsigned32"
_Cc6kxbarTMChUtilInterval_Object = MibTableColumn
cc6kxbarTMChUtilInterval = _Cc6kxbarTMChUtilInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1, 1, 5),
    _Cc6kxbarTMChUtilInterval_Type()
)
cc6kxbarTMChUtilInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilInterval.setStatus("current")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilInterval.setUnits("seconds")
_Cc6kxbarTMChUtilThreshold_Type = Percent
_Cc6kxbarTMChUtilThreshold_Object = MibTableColumn
cc6kxbarTMChUtilThreshold = _Cc6kxbarTMChUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1, 1, 6),
    _Cc6kxbarTMChUtilThreshold_Type()
)
cc6kxbarTMChUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilThreshold.setStatus("current")
_Cc6kxbarTMChUtilLogCount_Type = Counter32
_Cc6kxbarTMChUtilLogCount_Object = MibTableColumn
cc6kxbarTMChUtilLogCount = _Cc6kxbarTMChUtilLogCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1, 1, 7),
    _Cc6kxbarTMChUtilLogCount_Type()
)
cc6kxbarTMChUtilLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilLogCount.setStatus("current")
_Cc6kxbarTMChUtilLastLogTime_Type = DateAndTime
_Cc6kxbarTMChUtilLastLogTime_Object = MibTableColumn
cc6kxbarTMChUtilLastLogTime = _Cc6kxbarTMChUtilLastLogTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 1, 1, 8),
    _Cc6kxbarTMChUtilLastLogTime_Type()
)
cc6kxbarTMChUtilLastLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilLastLogTime.setStatus("current")


class _Cc6kxbarTMChUtilLogInterval_Type(Unsigned32):
    """Custom type cc6kxbarTMChUtilLogInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Cc6kxbarTMChUtilLogInterval_Type.__name__ = "Unsigned32"
_Cc6kxbarTMChUtilLogInterval_Object = MibScalar
cc6kxbarTMChUtilLogInterval = _Cc6kxbarTMChUtilLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 2),
    _Cc6kxbarTMChUtilLogInterval_Type()
)
cc6kxbarTMChUtilLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilLogInterval.setStatus("current")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilLogInterval.setUnits("seconds")
_Cc6kxbarTMChUtilUtilization_Type = Percent
_Cc6kxbarTMChUtilUtilization_Object = MibScalar
cc6kxbarTMChUtilUtilization = _Cc6kxbarTMChUtilUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 3),
    _Cc6kxbarTMChUtilUtilization_Type()
)
cc6kxbarTMChUtilUtilization.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilUtilization.setStatus("current")
_Cc6kxbarTMChUtilNotifEnable_Type = TruthValue
_Cc6kxbarTMChUtilNotifEnable_Object = MibScalar
cc6kxbarTMChUtilNotifEnable = _Cc6kxbarTMChUtilNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 1, 9, 2, 4),
    _Cc6kxbarTMChUtilNotifEnable_Type()
)
cc6kxbarTMChUtilNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilNotifEnable.setStatus("current")
_Cc6kxbarMIBConformance_ObjectIdentity = ObjectIdentity
cc6kxbarMIBConformance = _Cc6kxbarMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3)
)
_Cc6kxbarMIBCompliances_ObjectIdentity = ObjectIdentity
cc6kxbarMIBCompliances = _Cc6kxbarMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1)
)
_Cc6kxbarMIBGroups_ObjectIdentity = ObjectIdentity
cc6kxbarMIBGroups = _Cc6kxbarMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2)
)

# Managed Objects groups

cc6kxbarModuleStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 1)
)
cc6kxbarModuleStatusGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarLcdBannerMaxSize"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarLcdBannerBanner"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTruncatedModeAllowed"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarMinFabricPresent"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFabricActiveSlot"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFabricBackupSlot"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarModuleModeSwitchingMode"))
)
if mibBuilder.loadTexts:
    cc6kxbarModuleStatusGroup.setStatus("deprecated")

cc6kxbarChannelStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 2)
)
cc6kxbarChannelStatusGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarModuleChannelModStatus"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarModuleChannelFabStatus"))
)
if mibBuilder.loadTexts:
    cc6kxbarChannelStatusGroup.setStatus("current")

cc6kxbarChannelStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 3)
)
cc6kxbarChannelStatisticsGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsInErrors"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsOutErrors"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsOutDropped"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsInUtil"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsOutUtil"))
)
if mibBuilder.loadTexts:
    cc6kxbarChannelStatisticsGroup.setStatus("deprecated")

cc6kxbarFallbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 4)
)
cc6kxbarFallbackGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFallbackMode")
)
if mibBuilder.loadTexts:
    cc6kxbarFallbackGroup.setStatus("current")

cc6kxbarBusOnlyAllowedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 5)
)
cc6kxbarBusOnlyAllowedGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarBusOnlyModeAllowed")
)
if mibBuilder.loadTexts:
    cc6kxbarBusOnlyAllowedGroup.setStatus("current")

cc6kxbarModuleStatusGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 6)
)
cc6kxbarModuleStatusGroupVer1.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTruncatedModeAllowed"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarMinFabricPresent"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFabricActiveSlot"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFabricBackupSlot"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarModuleModeSwitchingMode"))
)
if mibBuilder.loadTexts:
    cc6kxbarModuleStatusGroupVer1.setStatus("current")

cc6kxbarChannelStatisticsGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 7)
)
cc6kxbarChannelStatisticsGroupVer1.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsInErrors"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsOutErrors"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsOutDropped"))
)
if mibBuilder.loadTexts:
    cc6kxbarChannelStatisticsGroupVer1.setStatus("current")

cc6kxbarLcdBannerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 8)
)
cc6kxbarLcdBannerGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarLcdBannerMaxSize"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarLcdBannerBanner"))
)
if mibBuilder.loadTexts:
    cc6kxbarLcdBannerGroup.setStatus("current")

cc6kxbarChannelUtilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 9)
)
cc6kxbarChannelUtilGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsInUtil"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsOutUtil"))
)
if mibBuilder.loadTexts:
    cc6kxbarChannelUtilGroup.setStatus("current")

cc6kxbarChannelSpeedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 10)
)
cc6kxbarChannelSpeedGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarModuleChannelSpeed")
)
if mibBuilder.loadTexts:
    cc6kxbarChannelSpeedGroup.setStatus("current")

cc6kxbarSwBusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 11)
)
cc6kxbarSwBusGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSwBusSwitchingStatus"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSwBusFailureDuration"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSwBusNotifEnable"))
)
if mibBuilder.loadTexts:
    cc6kxbarSwBusGroup.setStatus("current")

cc6kxbarTruncatedOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 13)
)
cc6kxbarTruncatedOperGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTruncatedModeOper")
)
if mibBuilder.loadTexts:
    cc6kxbarTruncatedOperGroup.setStatus("current")

cc6kxbarIntBusNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 14)
)
cc6kxbarIntBusNotifControlGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarIntBusNotifEnable")
)
if mibBuilder.loadTexts:
    cc6kxbarIntBusNotifControlGroup.setStatus("current")

cc6kxbarIntBusCRCErrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 16)
)
cc6kxbarIntBusCRCErrGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarIntBusCRCErrExcdStatus"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarIntBusCRCErrExcdCount"))
)
if mibBuilder.loadTexts:
    cc6kxbarIntBusCRCErrGroup.setStatus("current")

cc6kxbarDcefOnlyModeAllowedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 17)
)
cc6kxbarDcefOnlyModeAllowedGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarDcefOnlyModeAllowed")
)
if mibBuilder.loadTexts:
    cc6kxbarDcefOnlyModeAllowedGroup.setStatus("current")

cc6kxbarForceBusModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 18)
)
cc6kxbarForceBusModeGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarForceBusMode")
)
if mibBuilder.loadTexts:
    cc6kxbarForceBusModeGroup.setStatus("current")

cc6kxbarFlowCtrlNotifCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 19)
)
cc6kxbarFlowCtrlNotifCtrlGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFlowCtrlNotifEnable")
)
if mibBuilder.loadTexts:
    cc6kxbarFlowCtrlNotifCtrlGroup.setStatus("current")

cc6kxbarFlowCtrlBusThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 20)
)
cc6kxbarFlowCtrlBusThreshGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFlowCtrlBusFIFOThrMode"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFlowCtrlBusFIFOThrValue"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFlowCtrlBusFIFOTransTime"))
)
if mibBuilder.loadTexts:
    cc6kxbarFlowCtrlBusThreshGroup.setStatus("current")

cc6kxbarBusOnlyModeOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 22)
)
cc6kxbarBusOnlyModeOperGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarBusOnlyModeOper")
)
if mibBuilder.loadTexts:
    cc6kxbarBusOnlyModeOperGroup.setStatus("current")

cc6kxbarSysCapPfcOperModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 23)
)
cc6kxbarSysCapPfcOperModeGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSysCapPfcOperMode")
)
if mibBuilder.loadTexts:
    cc6kxbarSysCapPfcOperModeGroup.setStatus("current")

cc6kxbarSysCapSwitchResGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 24)
)
cc6kxbarSysCapSwitchResGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSysCapSwitchResSeries"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSysCapSwitchResCefMode"))
)
if mibBuilder.loadTexts:
    cc6kxbarSysCapSwitchResGroup.setStatus("current")

cc6kxbarChannelUtilGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 25)
)
cc6kxbarChannelUtilGroup1.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsPeakInUtil"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsPeakTmInUtil"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsPeakOutUtil"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsPeakTmOutUtil"))
)
if mibBuilder.loadTexts:
    cc6kxbarChannelUtilGroup1.setStatus("current")

cc6kxbarSwBusGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 26)
)
cc6kxbarSwBusGroup1.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSwBusUtilization"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSwBusPeakUtilization"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSwBusPeakTimeUtil"))
)
if mibBuilder.loadTexts:
    cc6kxbarSwBusGroup1.setStatus("current")

cc6kxbarErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 27)
)
cc6kxbarErrorGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrorModuleCrc"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrorModuleHbeat"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrorModuleSync"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrorModuleDDRSync"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrorChannelSync"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrorChannelBuffer"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrorChannelTimeout"))
)
if mibBuilder.loadTexts:
    cc6kxbarErrorGroup.setStatus("current")

cc6kxbarErrRcvryThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 28)
)
cc6kxbarErrRcvryThresholdGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrRcvryThreshLink"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrRcvryThreshPersLink"))
)
if mibBuilder.loadTexts:
    cc6kxbarErrRcvryThresholdGroup.setStatus("current")

cc6kxbarErrRcvrySwitchoverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 29)
)
cc6kxbarErrRcvrySwitchoverGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrRcvrySwitchoverEnable")
)
if mibBuilder.loadTexts:
    cc6kxbarErrRcvrySwitchoverGroup.setStatus("current")

cc6kxbarErrRcvryPersLinkResGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 30)
)
cc6kxbarErrRcvryPersLinkResGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrRcvryPersLinkResync")
)
if mibBuilder.loadTexts:
    cc6kxbarErrRcvryPersLinkResGroup.setStatus("current")

cc6kxbarErrRcvryChResyncGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 31)
)
cc6kxbarErrRcvryChResyncGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrRcvryChResyncCount"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarErrRcvryChResyncInterval"))
)
if mibBuilder.loadTexts:
    cc6kxbarErrRcvryChResyncGroup.setStatus("current")

cc6kxbarTMSwBusUtilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 32)
)
cc6kxbarTMSwBusUtilGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilEnable"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilInterval"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilThreshold"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilLogCount"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilLastLogTime"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilLogInterval"))
)
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilGroup.setStatus("current")

cc6kxbarTMSwBusUtilNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 33)
)
cc6kxbarTMSwBusUtilNotifControlGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilNotifEnable")
)
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilNotifControlGroup.setStatus("current")

cc6kxbarTMSwBusUtilNotifObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 34)
)
cc6kxbarTMSwBusUtilNotifObjectGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilUtilization")
)
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilNotifObjectGroup.setStatus("current")

cc6kxbarTMChUtilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 36)
)
cc6kxbarTMChUtilGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilEnable"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilInterval"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilThreshold"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilLogCount"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilLastLogTime"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilLogInterval"))
)
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilGroup.setStatus("current")

cc6kxbarTMChUtilNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 37)
)
cc6kxbarTMChUtilNotifControlGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilNotifEnable")
)
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilNotifControlGroup.setStatus("current")

cc6kxbarTMChUtilNotifObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 38)
)
cc6kxbarTMChUtilNotifObjectGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilUtilization")
)
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilNotifObjectGroup.setStatus("current")

cc6kxbarStatisticsLbusDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 40)
)
cc6kxbarStatisticsLbusDropGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarStatisticsLbusDrops")
)
if mibBuilder.loadTexts:
    cc6kxbarStatisticsLbusDropGroup.setStatus("current")


# Notification objects

cc6kxbarSwBusStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 0, 1)
)
cc6kxbarSwBusStatusChangeNotif.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSwBusSwitchingStatus"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSwBusFailureDuration"))
)
if mibBuilder.loadTexts:
    cc6kxbarSwBusStatusChangeNotif.setStatus(
        "current"
    )

cc6kxbarIntBusCRCErrExcdNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 0, 2)
)
cc6kxbarIntBusCRCErrExcdNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalVendorType"))
)
if mibBuilder.loadTexts:
    cc6kxbarIntBusCRCErrExcdNotif.setStatus(
        "current"
    )

cc6kxbarIntBusCRCErrRcvrdNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 0, 3)
)
cc6kxbarIntBusCRCErrRcvrdNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalVendorType"))
)
if mibBuilder.loadTexts:
    cc6kxbarIntBusCRCErrRcvrdNotif.setStatus(
        "current"
    )

cc6kxbarFlowCtrlBusThrExcdNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 0, 4)
)
cc6kxbarFlowCtrlBusThrExcdNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalVendorType"))
)
if mibBuilder.loadTexts:
    cc6kxbarFlowCtrlBusThrExcdNotif.setStatus(
        "current"
    )

cc6kxbarTMSwBusUtilAboveNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 0, 5)
)
cc6kxbarTMSwBusUtilAboveNotif.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilUtilization"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilThreshold"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilInterval"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilAboveNotif.setStatus(
        "current"
    )

cc6kxbarTMSwBusUtilBelowNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 0, 6)
)
cc6kxbarTMSwBusUtilBelowNotif.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilUtilization"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilThreshold"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilInterval"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilBelowNotif.setStatus(
        "current"
    )

cc6kxbarTMChUtilAboveNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 0, 7)
)
cc6kxbarTMChUtilAboveNotif.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilUtilization"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilThreshold"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilInterval"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilAboveNotif.setStatus(
        "current"
    )

cc6kxbarTMChUtilBelowNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 0, 8)
)
cc6kxbarTMChUtilBelowNotif.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilUtilization"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilThreshold"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilInterval"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilBelowNotif.setStatus(
        "current"
    )


# Notifications groups

cc6kxbarSwBusNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 12)
)
cc6kxbarSwBusNotifGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarSwBusStatusChangeNotif")
)
if mibBuilder.loadTexts:
    cc6kxbarSwBusNotifGroup.setStatus(
        "current"
    )

cc6kxbarIntBusCRCErrNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 15)
)
cc6kxbarIntBusCRCErrNotifGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarIntBusCRCErrExcdNotif"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarIntBusCRCErrRcvrdNotif"))
)
if mibBuilder.loadTexts:
    cc6kxbarIntBusCRCErrNotifGroup.setStatus(
        "current"
    )

cc6kxbarFlowCtrlBusThrNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 21)
)
cc6kxbarFlowCtrlBusThrNotifGroup.setObjects(
    ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarFlowCtrlBusThrExcdNotif")
)
if mibBuilder.loadTexts:
    cc6kxbarFlowCtrlBusThrNotifGroup.setStatus(
        "current"
    )

cc6kxbarTMSwBusUtilNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 35)
)
cc6kxbarTMSwBusUtilNotifGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilAboveNotif"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMSwBusUtilBelowNotif"))
)
if mibBuilder.loadTexts:
    cc6kxbarTMSwBusUtilNotifGroup.setStatus(
        "current"
    )

cc6kxbarTMChUtilNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 2, 39)
)
cc6kxbarTMChUtilNotifGroup.setObjects(
      *(("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilAboveNotif"),
        ("CISCO-CAT6K-CROSSBAR-MIB", "cc6kxbarTMChUtilBelowNotif"))
)
if mibBuilder.loadTexts:
    cc6kxbarTMChUtilNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cc6kxbarMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cc6kxbarMIBCompliance.setStatus(
        "deprecated"
    )

cc6kxbarMIBComplianceVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cc6kxbarMIBComplianceVer1.setStatus(
        "deprecated"
    )

cc6kxbarMIBComplianceVer2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cc6kxbarMIBComplianceVer2.setStatus(
        "deprecated"
    )

cc6kxbarMIBComplianceVer3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cc6kxbarMIBComplianceVer3.setStatus(
        "deprecated"
    )

cc6kxbarMIBComplianceVer4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cc6kxbarMIBComplianceVer4.setStatus(
        "deprecated"
    )

cc6kxbarMIBComplianceVer5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cc6kxbarMIBComplianceVer5.setStatus(
        "deprecated"
    )

cc6kxbarMIBComplianceVer6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cc6kxbarMIBComplianceVer6.setStatus(
        "deprecated"
    )

cc6kxbarMIBComplianceVer7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cc6kxbarMIBComplianceVer7.setStatus(
        "deprecated"
    )

cc6kxbarMIBComplianceVer8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 217, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cc6kxbarMIBComplianceVer8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CAT6K-CROSSBAR-MIB",
    **{"ModuleSlotNumber": ModuleSlotNumber,
       "FabricChannelNumber": FabricChannelNumber,
       "ChannelStatus": ChannelStatus,
       "ciscoCat6kCrossbarMIB": ciscoCat6kCrossbarMIB,
       "ciscoCat6kXbarMIBNotifs": ciscoCat6kXbarMIBNotifs,
       "cc6kxbarSwBusStatusChangeNotif": cc6kxbarSwBusStatusChangeNotif,
       "cc6kxbarIntBusCRCErrExcdNotif": cc6kxbarIntBusCRCErrExcdNotif,
       "cc6kxbarIntBusCRCErrRcvrdNotif": cc6kxbarIntBusCRCErrRcvrdNotif,
       "cc6kxbarFlowCtrlBusThrExcdNotif": cc6kxbarFlowCtrlBusThrExcdNotif,
       "cc6kxbarTMSwBusUtilAboveNotif": cc6kxbarTMSwBusUtilAboveNotif,
       "cc6kxbarTMSwBusUtilBelowNotif": cc6kxbarTMSwBusUtilBelowNotif,
       "cc6kxbarTMChUtilAboveNotif": cc6kxbarTMChUtilAboveNotif,
       "cc6kxbarTMChUtilBelowNotif": cc6kxbarTMChUtilBelowNotif,
       "ciscoCat6kXbarMIBObjects": ciscoCat6kXbarMIBObjects,
       "cc6kxbarConfiguration": cc6kxbarConfiguration,
       "cc6kxbarFallbackMode": cc6kxbarFallbackMode,
       "cc6kxbarBusOnlyModeAllowed": cc6kxbarBusOnlyModeAllowed,
       "cc6kxbarTruncatedModeAllowed": cc6kxbarTruncatedModeAllowed,
       "cc6kxbarMinFabricPresent": cc6kxbarMinFabricPresent,
       "cc6kxbarLcdBannerTable": cc6kxbarLcdBannerTable,
       "cc6kxbarLcdBannerEntry": cc6kxbarLcdBannerEntry,
       "cc6kxbarLcdBannerIndex": cc6kxbarLcdBannerIndex,
       "cc6kxbarLcdBannerBanner": cc6kxbarLcdBannerBanner,
       "cc6kxbarLcdBannerMaxSize": cc6kxbarLcdBannerMaxSize,
       "cc6kxbarTruncatedModeOper": cc6kxbarTruncatedModeOper,
       "cc6kxbarDcefOnlyModeAllowed": cc6kxbarDcefOnlyModeAllowed,
       "cc6kxbarForceBusMode": cc6kxbarForceBusMode,
       "cc6kxbarBusOnlyModeOper": cc6kxbarBusOnlyModeOper,
       "cc6kxbarStatus": cc6kxbarStatus,
       "cc6kxbarFabricActiveSlot": cc6kxbarFabricActiveSlot,
       "cc6kxbarFabricBackupSlot": cc6kxbarFabricBackupSlot,
       "cc6kxbarModuleModeTable": cc6kxbarModuleModeTable,
       "cc6kxbarModuleModeEntry": cc6kxbarModuleModeEntry,
       "cc6kxbarModuleModeModule": cc6kxbarModuleModeModule,
       "cc6kxbarModuleModeSwitchingMode": cc6kxbarModuleModeSwitchingMode,
       "cc6kxbarModuleChannelTable": cc6kxbarModuleChannelTable,
       "cc6kxbarModuleChannelEntry": cc6kxbarModuleChannelEntry,
       "cc6kxbarModuleChannelModule": cc6kxbarModuleChannelModule,
       "cc6kxbarModuleChannelChannel": cc6kxbarModuleChannelChannel,
       "cc6kxbarModuleChannelModStatus": cc6kxbarModuleChannelModStatus,
       "cc6kxbarModuleChannelFabStatus": cc6kxbarModuleChannelFabStatus,
       "cc6kxbarModuleChannelSpeed": cc6kxbarModuleChannelSpeed,
       "cc6kxbarStatistics": cc6kxbarStatistics,
       "cc6kxbarStatisticsTable": cc6kxbarStatisticsTable,
       "cc6kxbarStatisticsEntry": cc6kxbarStatisticsEntry,
       "cc6kxbarStatisticsModule": cc6kxbarStatisticsModule,
       "cc6kxbarStatisticsChannel": cc6kxbarStatisticsChannel,
       "cc6kxbarStatisticsInErrors": cc6kxbarStatisticsInErrors,
       "cc6kxbarStatisticsOutErrors": cc6kxbarStatisticsOutErrors,
       "cc6kxbarStatisticsOutDropped": cc6kxbarStatisticsOutDropped,
       "cc6kxbarStatisticsInUtil": cc6kxbarStatisticsInUtil,
       "cc6kxbarStatisticsOutUtil": cc6kxbarStatisticsOutUtil,
       "cc6kxbarStatisticsPeakInUtil": cc6kxbarStatisticsPeakInUtil,
       "cc6kxbarStatisticsPeakTmInUtil": cc6kxbarStatisticsPeakTmInUtil,
       "cc6kxbarStatisticsPeakOutUtil": cc6kxbarStatisticsPeakOutUtil,
       "cc6kxbarStatisticsPeakTmOutUtil": cc6kxbarStatisticsPeakTmOutUtil,
       "cc6kxbarStatisticsLbusDrops": cc6kxbarStatisticsLbusDrops,
       "cc6kxbarErrorTable": cc6kxbarErrorTable,
       "cc6kxbarErrorEntry": cc6kxbarErrorEntry,
       "cc6kxbarErrorModule": cc6kxbarErrorModule,
       "cc6kxbarErrorChannel": cc6kxbarErrorChannel,
       "cc6kxbarErrorModuleCrc": cc6kxbarErrorModuleCrc,
       "cc6kxbarErrorModuleHbeat": cc6kxbarErrorModuleHbeat,
       "cc6kxbarErrorModuleSync": cc6kxbarErrorModuleSync,
       "cc6kxbarErrorModuleDDRSync": cc6kxbarErrorModuleDDRSync,
       "cc6kxbarErrorChannelSync": cc6kxbarErrorChannelSync,
       "cc6kxbarErrorChannelBuffer": cc6kxbarErrorChannelBuffer,
       "cc6kxbarErrorChannelTimeout": cc6kxbarErrorChannelTimeout,
       "cc6kxbarSwBusObjects": cc6kxbarSwBusObjects,
       "cc6kxbarSwBusSwitchingStatus": cc6kxbarSwBusSwitchingStatus,
       "cc6kxbarSwBusFailureDuration": cc6kxbarSwBusFailureDuration,
       "cc6kxbarSwBusNotifEnable": cc6kxbarSwBusNotifEnable,
       "cc6kxbarSwBusUtilization": cc6kxbarSwBusUtilization,
       "cc6kxbarSwBusPeakUtilization": cc6kxbarSwBusPeakUtilization,
       "cc6kxbarSwBusPeakTimeUtil": cc6kxbarSwBusPeakTimeUtil,
       "cc6kxbarIntBusObjects": cc6kxbarIntBusObjects,
       "cc6kxbarIntBusNotifEnable": cc6kxbarIntBusNotifEnable,
       "cc6kxbarIntBusCRCErrTable": cc6kxbarIntBusCRCErrTable,
       "cc6kxbarIntBusCRCErrEntry": cc6kxbarIntBusCRCErrEntry,
       "cc6kxbarIntBusCRCErrExcdStatus": cc6kxbarIntBusCRCErrExcdStatus,
       "cc6kxbarIntBusCRCErrExcdCount": cc6kxbarIntBusCRCErrExcdCount,
       "cc6kxbarFlowCtrlObjects": cc6kxbarFlowCtrlObjects,
       "cc6kxbarFlowCtrlNotifEnable": cc6kxbarFlowCtrlNotifEnable,
       "cc6kxbarFlowCtrlBusFIFOThrMode": cc6kxbarFlowCtrlBusFIFOThrMode,
       "cc6kxbarFlowCtrlBusFIFOThrValue": cc6kxbarFlowCtrlBusFIFOThrValue,
       "cc6kxbarFlowCtrlBusFIFOTransTime": cc6kxbarFlowCtrlBusFIFOTransTime,
       "cc6kxbarSystemCapacityObjects": cc6kxbarSystemCapacityObjects,
       "cc6kxbarSysCapPfcOperMode": cc6kxbarSysCapPfcOperMode,
       "cc6kxbarSysCapSwitchResTable": cc6kxbarSysCapSwitchResTable,
       "cc6kxbarSysCapSwitchResEntry": cc6kxbarSysCapSwitchResEntry,
       "cc6kxbarSysCapSwitchResSeries": cc6kxbarSysCapSwitchResSeries,
       "cc6kxbarSysCapSwitchResCefMode": cc6kxbarSysCapSwitchResCefMode,
       "cc6kxbarErrorRecoveryObjects": cc6kxbarErrorRecoveryObjects,
       "cc6kxbarErrRcvryThreshLink": cc6kxbarErrRcvryThreshLink,
       "cc6kxbarErrRcvryThreshPersLink": cc6kxbarErrRcvryThreshPersLink,
       "cc6kxbarErrRcvrySwitchoverEnable": cc6kxbarErrRcvrySwitchoverEnable,
       "cc6kxbarErrRcvryPersLinkResync": cc6kxbarErrRcvryPersLinkResync,
       "cc6kxbarErrRcvryChResyncCount": cc6kxbarErrRcvryChResyncCount,
       "cc6kxbarErrRcvryChResyncInterval": cc6kxbarErrRcvryChResyncInterval,
       "cc6kxbarTrafficMonitorObjects": cc6kxbarTrafficMonitorObjects,
       "cc6kxbarTrafficMonitorSwBusObjects": cc6kxbarTrafficMonitorSwBusObjects,
       "cc6kxbarTMSwBusUtilEnable": cc6kxbarTMSwBusUtilEnable,
       "cc6kxbarTMSwBusUtilInterval": cc6kxbarTMSwBusUtilInterval,
       "cc6kxbarTMSwBusUtilThreshold": cc6kxbarTMSwBusUtilThreshold,
       "cc6kxbarTMSwBusUtilLogCount": cc6kxbarTMSwBusUtilLogCount,
       "cc6kxbarTMSwBusUtilLastLogTime": cc6kxbarTMSwBusUtilLastLogTime,
       "cc6kxbarTMSwBusUtilLogInterval": cc6kxbarTMSwBusUtilLogInterval,
       "cc6kxbarTMSwBusUtilUtilization": cc6kxbarTMSwBusUtilUtilization,
       "cc6kxbarTMSwBusUtilNotifEnable": cc6kxbarTMSwBusUtilNotifEnable,
       "cc6kxbarTrafficMonitorChObjects": cc6kxbarTrafficMonitorChObjects,
       "cc6kxbarTMChUtilTable": cc6kxbarTMChUtilTable,
       "cc6kxbarTMChUtilEntry": cc6kxbarTMChUtilEntry,
       "cc6kxbarTMChUtilModule": cc6kxbarTMChUtilModule,
       "cc6kxbarTMChUtilChannel": cc6kxbarTMChUtilChannel,
       "cc6kxbarTMChUtilDirection": cc6kxbarTMChUtilDirection,
       "cc6kxbarTMChUtilEnable": cc6kxbarTMChUtilEnable,
       "cc6kxbarTMChUtilInterval": cc6kxbarTMChUtilInterval,
       "cc6kxbarTMChUtilThreshold": cc6kxbarTMChUtilThreshold,
       "cc6kxbarTMChUtilLogCount": cc6kxbarTMChUtilLogCount,
       "cc6kxbarTMChUtilLastLogTime": cc6kxbarTMChUtilLastLogTime,
       "cc6kxbarTMChUtilLogInterval": cc6kxbarTMChUtilLogInterval,
       "cc6kxbarTMChUtilUtilization": cc6kxbarTMChUtilUtilization,
       "cc6kxbarTMChUtilNotifEnable": cc6kxbarTMChUtilNotifEnable,
       "cc6kxbarMIBConformance": cc6kxbarMIBConformance,
       "cc6kxbarMIBCompliances": cc6kxbarMIBCompliances,
       "cc6kxbarMIBCompliance": cc6kxbarMIBCompliance,
       "cc6kxbarMIBComplianceVer1": cc6kxbarMIBComplianceVer1,
       "cc6kxbarMIBComplianceVer2": cc6kxbarMIBComplianceVer2,
       "cc6kxbarMIBComplianceVer3": cc6kxbarMIBComplianceVer3,
       "cc6kxbarMIBComplianceVer4": cc6kxbarMIBComplianceVer4,
       "cc6kxbarMIBComplianceVer5": cc6kxbarMIBComplianceVer5,
       "cc6kxbarMIBComplianceVer6": cc6kxbarMIBComplianceVer6,
       "cc6kxbarMIBComplianceVer7": cc6kxbarMIBComplianceVer7,
       "cc6kxbarMIBComplianceVer8": cc6kxbarMIBComplianceVer8,
       "cc6kxbarMIBGroups": cc6kxbarMIBGroups,
       "cc6kxbarModuleStatusGroup": cc6kxbarModuleStatusGroup,
       "cc6kxbarChannelStatusGroup": cc6kxbarChannelStatusGroup,
       "cc6kxbarChannelStatisticsGroup": cc6kxbarChannelStatisticsGroup,
       "cc6kxbarFallbackGroup": cc6kxbarFallbackGroup,
       "cc6kxbarBusOnlyAllowedGroup": cc6kxbarBusOnlyAllowedGroup,
       "cc6kxbarModuleStatusGroupVer1": cc6kxbarModuleStatusGroupVer1,
       "cc6kxbarChannelStatisticsGroupVer1": cc6kxbarChannelStatisticsGroupVer1,
       "cc6kxbarLcdBannerGroup": cc6kxbarLcdBannerGroup,
       "cc6kxbarChannelUtilGroup": cc6kxbarChannelUtilGroup,
       "cc6kxbarChannelSpeedGroup": cc6kxbarChannelSpeedGroup,
       "cc6kxbarSwBusGroup": cc6kxbarSwBusGroup,
       "cc6kxbarSwBusNotifGroup": cc6kxbarSwBusNotifGroup,
       "cc6kxbarTruncatedOperGroup": cc6kxbarTruncatedOperGroup,
       "cc6kxbarIntBusNotifControlGroup": cc6kxbarIntBusNotifControlGroup,
       "cc6kxbarIntBusCRCErrNotifGroup": cc6kxbarIntBusCRCErrNotifGroup,
       "cc6kxbarIntBusCRCErrGroup": cc6kxbarIntBusCRCErrGroup,
       "cc6kxbarDcefOnlyModeAllowedGroup": cc6kxbarDcefOnlyModeAllowedGroup,
       "cc6kxbarForceBusModeGroup": cc6kxbarForceBusModeGroup,
       "cc6kxbarFlowCtrlNotifCtrlGroup": cc6kxbarFlowCtrlNotifCtrlGroup,
       "cc6kxbarFlowCtrlBusThreshGroup": cc6kxbarFlowCtrlBusThreshGroup,
       "cc6kxbarFlowCtrlBusThrNotifGroup": cc6kxbarFlowCtrlBusThrNotifGroup,
       "cc6kxbarBusOnlyModeOperGroup": cc6kxbarBusOnlyModeOperGroup,
       "cc6kxbarSysCapPfcOperModeGroup": cc6kxbarSysCapPfcOperModeGroup,
       "cc6kxbarSysCapSwitchResGroup": cc6kxbarSysCapSwitchResGroup,
       "cc6kxbarChannelUtilGroup1": cc6kxbarChannelUtilGroup1,
       "cc6kxbarSwBusGroup1": cc6kxbarSwBusGroup1,
       "cc6kxbarErrorGroup": cc6kxbarErrorGroup,
       "cc6kxbarErrRcvryThresholdGroup": cc6kxbarErrRcvryThresholdGroup,
       "cc6kxbarErrRcvrySwitchoverGroup": cc6kxbarErrRcvrySwitchoverGroup,
       "cc6kxbarErrRcvryPersLinkResGroup": cc6kxbarErrRcvryPersLinkResGroup,
       "cc6kxbarErrRcvryChResyncGroup": cc6kxbarErrRcvryChResyncGroup,
       "cc6kxbarTMSwBusUtilGroup": cc6kxbarTMSwBusUtilGroup,
       "cc6kxbarTMSwBusUtilNotifControlGroup": cc6kxbarTMSwBusUtilNotifControlGroup,
       "cc6kxbarTMSwBusUtilNotifObjectGroup": cc6kxbarTMSwBusUtilNotifObjectGroup,
       "cc6kxbarTMSwBusUtilNotifGroup": cc6kxbarTMSwBusUtilNotifGroup,
       "cc6kxbarTMChUtilGroup": cc6kxbarTMChUtilGroup,
       "cc6kxbarTMChUtilNotifControlGroup": cc6kxbarTMChUtilNotifControlGroup,
       "cc6kxbarTMChUtilNotifObjectGroup": cc6kxbarTMChUtilNotifObjectGroup,
       "cc6kxbarTMChUtilNotifGroup": cc6kxbarTMChUtilNotifGroup,
       "cc6kxbarStatisticsLbusDropGroup": cc6kxbarStatisticsLbusDropGroup}
)
