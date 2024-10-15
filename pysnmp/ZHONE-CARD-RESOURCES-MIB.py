# SNMP MIB module (ZHONE-CARD-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-CARD-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:07 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zhoneCard,
 zhoneModules,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneCard",
    "zhoneModules",
    "zhoneShelfIndex",
    "zhoneSlotIndex")

(ZhoneAdminString,
 ZhoneCardType,
 ZhoneDiagAction) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneCardType",
    "ZhoneDiagAction")


# MODULE-IDENTITY

zhoneCardResourcesModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 4)
)
zhoneCardResourcesModule.setRevisions(
        ("2011-10-24 14:47",
         "2011-10-12 12:44",
         "2011-08-24 15:33",
         "2010-07-13 10:41",
         "2009-05-12 07:58",
         "2009-04-24 08:51",
         "2008-10-22 03:11",
         "2007-08-15 17:30",
         "2006-10-17 15:03",
         "2006-09-28 11:42",
         "2005-10-11 16:47",
         "2005-10-05 11:16",
         "2005-05-23 14:22",
         "2004-04-15 13:27",
         "2003-12-22 12:14",
         "2003-11-21 15:18",
         "2002-10-29 15:30",
         "2002-10-24 17:24",
         "2002-07-09 11:27",
         "2002-06-07 17:38",
         "2002-05-24 12:58",
         "2002-03-22 14:55",
         "2001-11-16 18:11",
         "2001-10-23 11:10",
         "2001-10-09 10:00",
         "2001-10-08 13:36",
         "2001-10-04 12:26",
         "2001-09-17 16:50",
         "2001-09-07 16:40",
         "2001-09-06 16:03",
         "2001-09-05 20:38",
         "2001-08-29 11:23",
         "2001-08-09 10:43",
         "2001-07-26 10:47",
         "2001-07-20 13:20",
         "2000-09-12 10:59",
         "2000-09-20 11:00",
         "2000-11-11 10:59",
         "2000-11-21 18:31",
         "2000-12-01 12:18",
         "2000-12-18 19:11",
         "2001-01-22 14:56",
         "2001-03-27 10:29",
         "2001-04-06 14:25",
         "2001-04-27 11:49",
         "2001-05-24 13:15")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Kbytes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ZhoneServiceId(Integer32, TextualConvention):
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("aal2Resource", 4),
          ("callControlResource", 6),
          ("cardServer", 18),
          ("cssService", 25),
          ("ctrpCallResource", 5),
          ("dhcpServer", 19),
          ("dspResource", 1),
          ("filterUpdate", 20),
          ("ifCfgMgrResource", 16),
          ("informationServices", 14),
          ("lineResource", 15),
          ("logServer", 17),
          ("mamaResource", 8),
          ("mgcpResource", 27),
          ("mprrResource", 7),
          ("npRedundantServer", 28),
          ("numberService", 2),
          ("pppResourceProvider", 23),
          ("raFtdResource", 9),
          ("ringGenerator", 21),
          ("rootDirectoryService", 24),
          ("shelfControllerService", 11),
          ("sipResource", 26),
          ("snmpMasterAgent", 12),
          ("tadService", 3),
          ("trapService", 13),
          ("voiceCall", 10),
          ("zhoneRouteTableService", 22))
    )



# MIB Managed Objects in the order of their OIDs

_CardResourceTable_Object = MibTable
cardResourceTable = _CardResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cardResourceTable.setStatus("current")
_CardResourceEntry_Object = MibTableRow
cardResourceEntry = _CardResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1)
)
cardResourceEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    cardResourceEntry.setStatus("current")
_CardIdentification_Type = ZhoneAdminString
_CardIdentification_Object = MibTableColumn
cardIdentification = _CardIdentification_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 1),
    _CardIdentification_Type()
)
cardIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIdentification.setStatus("current")
_CardZhoneType_Type = ZhoneCardType
_CardZhoneType_Object = MibTableColumn
cardZhoneType = _CardZhoneType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 2),
    _CardZhoneType_Type()
)
cardZhoneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardZhoneType.setStatus("current")
_CardMfgSerialNumber_Type = ZhoneAdminString
_CardMfgSerialNumber_Object = MibTableColumn
cardMfgSerialNumber = _CardMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 3),
    _CardMfgSerialNumber_Type()
)
cardMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMfgSerialNumber.setStatus("current")
_CardMfgCLEICode_Type = ZhoneAdminString
_CardMfgCLEICode_Object = MibTableColumn
cardMfgCLEICode = _CardMfgCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 4),
    _CardMfgCLEICode_Type()
)
cardMfgCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMfgCLEICode.setStatus("current")
_CardMfgRevisionCode_Type = ZhoneAdminString
_CardMfgRevisionCode_Object = MibTableColumn
cardMfgRevisionCode = _CardMfgRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 5),
    _CardMfgRevisionCode_Type()
)
cardMfgRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMfgRevisionCode.setStatus("current")
_CardMfgBootRevision_Type = ZhoneAdminString
_CardMfgBootRevision_Object = MibTableColumn
cardMfgBootRevision = _CardMfgBootRevision_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 6),
    _CardMfgBootRevision_Type()
)
cardMfgBootRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMfgBootRevision.setStatus("current")
_CardPostResults_Type = ZhoneAdminString
_CardPostResults_Object = MibTableColumn
cardPostResults = _CardPostResults_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 7),
    _CardPostResults_Type()
)
cardPostResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPostResults.setStatus("current")


class _CardAdminStatus_Type(Integer32):
    """Custom type cardAdminStatus based on Integer32"""
    defaultValue = 1

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
        *(("disable", 2),
          ("maintenance", 3),
          ("operational", 1),
          ("reset", 5),
          ("warmreset", 4))
    )


_CardAdminStatus_Type.__name__ = "Integer32"
_CardAdminStatus_Object = MibTableColumn
cardAdminStatus = _CardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 8),
    _CardAdminStatus_Type()
)
cardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAdminStatus.setStatus("current")


class _CardOperStatus_Type(Integer32):
    """Custom type cardOperStatus based on Integer32"""
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
        *(("maintenance", 4),
          ("nonoperating", 3),
          ("operating", 2),
          ("unknown", 1))
    )


_CardOperStatus_Type.__name__ = "Integer32"
_CardOperStatus_Object = MibTableColumn
cardOperStatus = _CardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 9),
    _CardOperStatus_Type()
)
cardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOperStatus.setStatus("current")


class _CardAdminStatsEnable_Type(Integer32):
    """Custom type cardAdminStatsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CardAdminStatsEnable_Type.__name__ = "Integer32"
_CardAdminStatsEnable_Object = MibTableColumn
cardAdminStatsEnable = _CardAdminStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 10),
    _CardAdminStatsEnable_Type()
)
cardAdminStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAdminStatsEnable.setStatus("current")
_CardUpTime_Type = TimeTicks
_CardUpTime_Object = MibTableColumn
cardUpTime = _CardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 11),
    _CardUpTime_Type()
)
cardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardUpTime.setStatus("current")
_CardProcessorType_Type = ZhoneAdminString
_CardProcessorType_Object = MibTableColumn
cardProcessorType = _CardProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 12),
    _CardProcessorType_Type()
)
cardProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProcessorType.setStatus("current")
_CardPortStatus_Type = OctetString
_CardPortStatus_Object = MibTableColumn
cardPortStatus = _CardPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 13),
    _CardPortStatus_Type()
)
cardPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPortStatus.setStatus("current")
_CardInterfaceType_Type = ZhoneCardType
_CardInterfaceType_Object = MibTableColumn
cardInterfaceType = _CardInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 14),
    _CardInterfaceType_Type()
)
cardInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInterfaceType.setStatus("current")


class _CardAtmManualAal2bw_Type(Integer32):
    """Custom type cardAtmManualAal2bw based on Integer32"""
    defaultBinValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CardAtmManualAal2bw_Type.__name__ = "Integer32"
_CardAtmManualAal2bw_Object = MibTableColumn
cardAtmManualAal2bw = _CardAtmManualAal2bw_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 15),
    _CardAtmManualAal2bw_Type()
)
cardAtmManualAal2bw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAtmManualAal2bw.setStatus("current")


class _CardAtmManualAal2h_Type(Integer32):
    """Custom type cardAtmManualAal2h based on Integer32"""
    defaultBinValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CardAtmManualAal2h_Type.__name__ = "Integer32"
_CardAtmManualAal2h_Object = MibTableColumn
cardAtmManualAal2h = _CardAtmManualAal2h_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 16),
    _CardAtmManualAal2h_Type()
)
cardAtmManualAal2h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAtmManualAal2h.setStatus("current")


class _CardLineVoltage_Type(Integer32):
    """Custom type cardLineVoltage based on Integer32"""
    defaultValue = 1

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
        *(("line-voltage-100-volts", 5),
          ("line-voltage-110-volts", 6),
          ("line-voltage-60-volts", 2),
          ("line-voltage-68-volts", 3),
          ("line-voltage-95-volts", 4),
          ("line-voltage-not-used", 1))
    )


_CardLineVoltage_Type.__name__ = "Integer32"
_CardLineVoltage_Object = MibTableColumn
cardLineVoltage = _CardLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 17),
    _CardLineVoltage_Type()
)
cardLineVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardLineVoltage.setStatus("deprecated")


class _CardVpiVciRange_Type(Integer32):
    """Custom type cardVpiVciRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vpivci-range-not-applicable", 1),
          ("vpivci-range-vpi-15-vci-63", 2),
          ("vpivci-range-vpi-7-vci-127", 3))
    )


_CardVpiVciRange_Type.__name__ = "Integer32"
_CardVpiVciRange_Object = MibTableColumn
cardVpiVciRange = _CardVpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 18),
    _CardVpiVciRange_Type()
)
cardVpiVciRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardVpiVciRange.setStatus("deprecated")


class _CardPweTimingMode_Type(Integer32):
    """Custom type cardPweTimingMode based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("remote-adaptive", 5),
          ("remote-differential", 4),
          ("source-adaptive", 3),
          ("source-differential", 2))
    )


_CardPweTimingMode_Type.__name__ = "Integer32"
_CardPweTimingMode_Object = MibTableColumn
cardPweTimingMode = _CardPweTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 1, 1, 19),
    _CardPweTimingMode_Type()
)
cardPweTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardPweTimingMode.setStatus("current")
_CardSoftwareTable_Object = MibTable
cardSoftwareTable = _CardSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 2)
)
if mibBuilder.loadTexts:
    cardSoftwareTable.setStatus("current")
_CardSoftwareEntry_Object = MibTableRow
cardSoftwareEntry = _CardSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cardSoftwareEntry.setStatus("current")
_CardSwRunningVers_Type = ZhoneAdminString
_CardSwRunningVers_Object = MibTableColumn
cardSwRunningVers = _CardSwRunningVers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 2, 1, 1),
    _CardSwRunningVers_Type()
)
cardSwRunningVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSwRunningVers.setStatus("current")
_CardSwUpgradeVers_Type = ZhoneAdminString
_CardSwUpgradeVers_Object = MibTableColumn
cardSwUpgradeVers = _CardSwUpgradeVers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 2, 1, 2),
    _CardSwUpgradeVers_Type()
)
cardSwUpgradeVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSwUpgradeVers.setStatus("current")


class _CardSwAdmin_Type(Integer32):
    """Custom type cardSwAdmin based on Integer32"""
    defaultValue = 4

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
        *(("loadUpgradeSw", 1),
          ("reloadCurrRev", 4),
          ("upgradeNow", 2),
          ("upgradeOnReset", 3))
    )


_CardSwAdmin_Type.__name__ = "Integer32"
_CardSwAdmin_Object = MibTableColumn
cardSwAdmin = _CardSwAdmin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 2, 1, 3),
    _CardSwAdmin_Type()
)
cardSwAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSwAdmin.setStatus("current")


class _CardSwStatus_Type(Integer32):
    """Custom type cardSwStatus based on Integer32"""
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
        *(("loadingSw", 2),
          ("pendingUpgradeOnReset", 7),
          ("upgradeFailed", 5),
          ("upgradeImageNotAvail", 6),
          ("upgradeLoadFailed", 4),
          ("upgradeLoadSuccessful", 1),
          ("upgradeNotRequested", 8),
          ("upgrading", 3))
    )


_CardSwStatus_Type.__name__ = "Integer32"
_CardSwStatus_Object = MibTableColumn
cardSwStatus = _CardSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 2, 1, 4),
    _CardSwStatus_Type()
)
cardSwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSwStatus.setStatus("current")
_CardRuntimeTable_Object = MibTable
cardRuntimeTable = _CardRuntimeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3)
)
if mibBuilder.loadTexts:
    cardRuntimeTable.setStatus("current")
_CardRuntimeEntry_Object = MibTableRow
cardRuntimeEntry = _CardRuntimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cardRuntimeEntry.setStatus("current")
_CardPeakMemUsage_Type = Kbytes
_CardPeakMemUsage_Object = MibTableColumn
cardPeakMemUsage = _CardPeakMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 1),
    _CardPeakMemUsage_Type()
)
cardPeakMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPeakMemUsage.setStatus("current")
_CardAvailMem_Type = Kbytes
_CardAvailMem_Object = MibTableColumn
cardAvailMem = _CardAvailMem_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 2),
    _CardAvailMem_Type()
)
cardAvailMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAvailMem.setStatus("current")
_CardTotalMem_Type = Kbytes
_CardTotalMem_Object = MibTableColumn
cardTotalMem = _CardTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 3),
    _CardTotalMem_Type()
)
cardTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTotalMem.setStatus("current")
_CardProcessorIdle_Type = Integer32
_CardProcessorIdle_Object = MibTableColumn
cardProcessorIdle = _CardProcessorIdle_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 4),
    _CardProcessorIdle_Type()
)
cardProcessorIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProcessorIdle.setStatus("current")
_CardProcessorUsage_Type = Integer32
_CardProcessorUsage_Object = MibTableColumn
cardProcessorUsage = _CardProcessorUsage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 5),
    _CardProcessorUsage_Type()
)
cardProcessorUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProcessorUsage.setStatus("current")


class _CardMemStatus_Type(Integer32):
    """Custom type cardMemStatus based on Integer32"""
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
        *(("flashMemLow", 4),
          ("flashMemOK", 3),
          ("flashMemOut", 5),
          ("ramMemLow", 2),
          ("ramMemOK", 1))
    )


_CardMemStatus_Type.__name__ = "Integer32"
_CardMemStatus_Object = MibTableColumn
cardMemStatus = _CardMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 6),
    _CardMemStatus_Type()
)
cardMemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMemStatus.setStatus("current")


class _CardProcessorHighUsage_Type(Integer32):
    """Custom type cardProcessorHighUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CardProcessorHighUsage_Type.__name__ = "Integer32"
_CardProcessorHighUsage_Object = MibTableColumn
cardProcessorHighUsage = _CardProcessorHighUsage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 7),
    _CardProcessorHighUsage_Type()
)
cardProcessorHighUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProcessorHighUsage.setStatus("current")


class _CardProcessorServicesUsage_Type(Integer32):
    """Custom type cardProcessorServicesUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CardProcessorServicesUsage_Type.__name__ = "Integer32"
_CardProcessorServicesUsage_Object = MibTableColumn
cardProcessorServicesUsage = _CardProcessorServicesUsage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 8),
    _CardProcessorServicesUsage_Type()
)
cardProcessorServicesUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProcessorServicesUsage.setStatus("current")


class _CardProcessorFrameworkUsage_Type(Integer32):
    """Custom type cardProcessorFrameworkUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CardProcessorFrameworkUsage_Type.__name__ = "Integer32"
_CardProcessorFrameworkUsage_Object = MibTableColumn
cardProcessorFrameworkUsage = _CardProcessorFrameworkUsage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 9),
    _CardProcessorFrameworkUsage_Type()
)
cardProcessorFrameworkUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProcessorFrameworkUsage.setStatus("current")


class _CardProcessorLowUsage_Type(Integer32):
    """Custom type cardProcessorLowUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CardProcessorLowUsage_Type.__name__ = "Integer32"
_CardProcessorLowUsage_Object = MibTableColumn
cardProcessorLowUsage = _CardProcessorLowUsage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 3, 1, 10),
    _CardProcessorLowUsage_Type()
)
cardProcessorLowUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProcessorLowUsage.setStatus("current")
_ZhoneCardServices_ObjectIdentity = ObjectIdentity
zhoneCardServices = _ZhoneCardServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4)
)
_CardServicesTable_Object = MibTable
cardServicesTable = _CardServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cardServicesTable.setStatus("current")
_CardServicesEntry_Object = MibTableRow
cardServicesEntry = _CardServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 1, 1)
)
cardServicesEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
    (0, "ZHONE-CARD-RESOURCES-MIB", "cardServiceId"),
    (0, "ZHONE-CARD-RESOURCES-MIB", "cardServiceInstance"),
)
if mibBuilder.loadTexts:
    cardServicesEntry.setStatus("current")
_CardServiceId_Type = ZhoneServiceId
_CardServiceId_Object = MibTableColumn
cardServiceId = _CardServiceId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 1, 1, 1),
    _CardServiceId_Type()
)
cardServiceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cardServiceId.setStatus("current")
_CardServiceInstance_Type = Unsigned32
_CardServiceInstance_Object = MibTableColumn
cardServiceInstance = _CardServiceInstance_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 1, 1, 2),
    _CardServiceInstance_Type()
)
cardServiceInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cardServiceInstance.setStatus("current")
_CardServiceChangeTime_Type = TimeTicks
_CardServiceChangeTime_Object = MibTableColumn
cardServiceChangeTime = _CardServiceChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 1, 1, 3),
    _CardServiceChangeTime_Type()
)
cardServiceChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardServiceChangeTime.setStatus("current")


class _CardServiceStatus_Type(Integer32):
    """Custom type cardServiceStatus based on Integer32"""
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
        *(("active", 4),
          ("inActive", 2),
          ("standBy", 3),
          ("unAvailable", 1))
    )


_CardServiceStatus_Type.__name__ = "Integer32"
_CardServiceStatus_Object = MibTableColumn
cardServiceStatus = _CardServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 1, 1, 4),
    _CardServiceStatus_Type()
)
cardServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardServiceStatus.setStatus("current")
_ActiveServicesTable_Object = MibTable
activeServicesTable = _ActiveServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    activeServicesTable.setStatus("current")
_ActiveServicesEntry_Object = MibTableRow
activeServicesEntry = _ActiveServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 2, 1)
)
activeServicesEntry.setIndexNames(
    (0, "ZHONE-CARD-RESOURCES-MIB", "cardServiceId"),
    (0, "ZHONE-CARD-RESOURCES-MIB", "cardServiceInstance"),
)
if mibBuilder.loadTexts:
    activeServicesEntry.setStatus("current")
_ActiveServiceShelf_Type = Integer32
_ActiveServiceShelf_Object = MibTableColumn
activeServiceShelf = _ActiveServiceShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 2, 1, 1),
    _ActiveServiceShelf_Type()
)
activeServiceShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeServiceShelf.setStatus("current")
_ActiveServiceSlot_Type = Integer32
_ActiveServiceSlot_Object = MibTableColumn
activeServiceSlot = _ActiveServiceSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 2, 1, 2),
    _ActiveServiceSlot_Type()
)
activeServiceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeServiceSlot.setStatus("current")
_ActiveServiceChangeTime_Type = TimeTicks
_ActiveServiceChangeTime_Object = MibTableColumn
activeServiceChangeTime = _ActiveServiceChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 2, 1, 3),
    _ActiveServiceChangeTime_Type()
)
activeServiceChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeServiceChangeTime.setStatus("current")
_StandbyServicesTable_Object = MibTable
standbyServicesTable = _StandbyServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 3)
)
if mibBuilder.loadTexts:
    standbyServicesTable.setStatus("current")
_StandbyServicesEntry_Object = MibTableRow
standbyServicesEntry = _StandbyServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 3, 1)
)
standbyServicesEntry.setIndexNames(
    (0, "ZHONE-CARD-RESOURCES-MIB", "cardServiceId"),
    (0, "ZHONE-CARD-RESOURCES-MIB", "cardServiceInstance"),
)
if mibBuilder.loadTexts:
    standbyServicesEntry.setStatus("current")
_StandbyServiceShelf_Type = Integer32
_StandbyServiceShelf_Object = MibTableColumn
standbyServiceShelf = _StandbyServiceShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 3, 1, 1),
    _StandbyServiceShelf_Type()
)
standbyServiceShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbyServiceShelf.setStatus("current")
_StandbyServiceSlot_Type = Integer32
_StandbyServiceSlot_Object = MibTableColumn
standbyServiceSlot = _StandbyServiceSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 3, 1, 2),
    _StandbyServiceSlot_Type()
)
standbyServiceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbyServiceSlot.setStatus("current")
_StandbyServiceChangeTime_Type = TimeTicks
_StandbyServiceChangeTime_Object = MibTableColumn
standbyServiceChangeTime = _StandbyServiceChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 3, 1, 3),
    _StandbyServiceChangeTime_Type()
)
standbyServiceChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbyServiceChangeTime.setStatus("current")
_ZhoneTrapCardServices_ObjectIdentity = ObjectIdentity
zhoneTrapCardServices = _ZhoneTrapCardServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 4)
)
if mibBuilder.loadTexts:
    zhoneTrapCardServices.setStatus("current")
_ZhoneTrapCardServicesV2Traps_ObjectIdentity = ObjectIdentity
zhoneTrapCardServicesV2Traps = _ZhoneTrapCardServicesV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 4, 0)
)
if mibBuilder.loadTexts:
    zhoneTrapCardServicesV2Traps.setStatus("current")
_ZhoneExternalRelay_ObjectIdentity = ObjectIdentity
zhoneExternalRelay = _ZhoneExternalRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8)
)
if mibBuilder.loadTexts:
    zhoneExternalRelay.setStatus("current")
_ZhoneExternalRelayTable_Object = MibTable
zhoneExternalRelayTable = _ZhoneExternalRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 1)
)
if mibBuilder.loadTexts:
    zhoneExternalRelayTable.setStatus("current")
_ZhoneExternalRelayEntry_Object = MibTableRow
zhoneExternalRelayEntry = _ZhoneExternalRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 1, 1)
)
zhoneExternalRelayEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
    (0, "ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayId"),
)
if mibBuilder.loadTexts:
    zhoneExternalRelayEntry.setStatus("current")


class _ZhoneExternalRelayName_Type(ZhoneAdminString):
    """Custom type zhoneExternalRelayName based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZhoneExternalRelayName_Type.__name__ = "ZhoneAdminString"
_ZhoneExternalRelayName_Object = MibTableColumn
zhoneExternalRelayName = _ZhoneExternalRelayName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 1, 1, 1),
    _ZhoneExternalRelayName_Type()
)
zhoneExternalRelayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneExternalRelayName.setStatus("current")


class _ZhoneExternalRelayState_Type(Integer32):
    """Custom type zhoneExternalRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("relayStateClosed", 2),
          ("relayStateOpen", 1))
    )


_ZhoneExternalRelayState_Type.__name__ = "Integer32"
_ZhoneExternalRelayState_Object = MibTableColumn
zhoneExternalRelayState = _ZhoneExternalRelayState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 1, 1, 2),
    _ZhoneExternalRelayState_Type()
)
zhoneExternalRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneExternalRelayState.setStatus("current")


class _ZhoneExternalRelayNormalState_Type(Integer32):
    """Custom type zhoneExternalRelayNormalState based on Integer32"""
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
        *(("normallyClosed", 3),
          ("normallyOpen", 2),
          ("notSpecified", 1))
    )


_ZhoneExternalRelayNormalState_Type.__name__ = "Integer32"
_ZhoneExternalRelayNormalState_Object = MibTableColumn
zhoneExternalRelayNormalState = _ZhoneExternalRelayNormalState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 1, 1, 3),
    _ZhoneExternalRelayNormalState_Type()
)
zhoneExternalRelayNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneExternalRelayNormalState.setStatus("current")
_ZhoneExternalRelayMappingTable_Object = MibTable
zhoneExternalRelayMappingTable = _ZhoneExternalRelayMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 2)
)
if mibBuilder.loadTexts:
    zhoneExternalRelayMappingTable.setStatus("current")
_ZhoneExternalRelayMappingEntry_Object = MibTableRow
zhoneExternalRelayMappingEntry = _ZhoneExternalRelayMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 2, 1)
)
zhoneExternalRelayMappingEntry.setIndexNames(
    (1, "ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayName"),
)
if mibBuilder.loadTexts:
    zhoneExternalRelayMappingEntry.setStatus("current")


class _ZhoneExternalRelayId_Type(Integer32):
    """Custom type zhoneExternalRelayId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ZhoneExternalRelayId_Type.__name__ = "Integer32"
_ZhoneExternalRelayId_Object = MibTableColumn
zhoneExternalRelayId = _ZhoneExternalRelayId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 2, 1, 1),
    _ZhoneExternalRelayId_Type()
)
zhoneExternalRelayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneExternalRelayId.setStatus("current")
_ZhoneTrapExternalRelay_ObjectIdentity = ObjectIdentity
zhoneTrapExternalRelay = _ZhoneTrapExternalRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 3)
)
if mibBuilder.loadTexts:
    zhoneTrapExternalRelay.setStatus("current")
_ZhoneTrapExternalRelayV2Traps_ObjectIdentity = ObjectIdentity
zhoneTrapExternalRelayV2Traps = _ZhoneTrapExternalRelayV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 3, 0)
)
if mibBuilder.loadTexts:
    zhoneTrapExternalRelayV2Traps.setStatus("current")
_ZhoneCardCompliances_ObjectIdentity = ObjectIdentity
zhoneCardCompliances = _ZhoneCardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 9)
)
_ZhoneCardGroups_ObjectIdentity = ObjectIdentity
zhoneCardGroups = _ZhoneCardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 9, 1)
)
_ZhoneTrapCardMemV2Traps_ObjectIdentity = ObjectIdentity
zhoneTrapCardMemV2Traps = _ZhoneTrapCardMemV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 10)
)
if mibBuilder.loadTexts:
    zhoneTrapCardMemV2Traps.setStatus("current")
_ZrgResources_ObjectIdentity = ObjectIdentity
zrgResources = _ZrgResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 11)
)
if mibBuilder.loadTexts:
    zrgResources.setStatus("current")


class _ZrgBatteryRelayStatus_Type(Bits):
    """Custom type zrgBatteryRelayStatus based on Bits"""
    namedValues = NamedValues(
        *(("batteryBAD", 3),
          ("batteryGone", 4),
          ("batteryLOW", 2),
          ("batteryON", 1),
          ("noUPS", 5),
          ("normalMode", 0))
    )

_ZrgBatteryRelayStatus_Type.__name__ = "Bits"
_ZrgBatteryRelayStatus_Object = MibScalar
zrgBatteryRelayStatus = _ZrgBatteryRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 11, 1),
    _ZrgBatteryRelayStatus_Type()
)
zrgBatteryRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zrgBatteryRelayStatus.setStatus("current")
_ZrgTrapBatteryRelay_ObjectIdentity = ObjectIdentity
zrgTrapBatteryRelay = _ZrgTrapBatteryRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 11, 2)
)
if mibBuilder.loadTexts:
    zrgTrapBatteryRelay.setStatus("current")
_ZrgBatterRelayTrapV2_ObjectIdentity = ObjectIdentity
zrgBatterRelayTrapV2 = _ZrgBatterRelayTrapV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 11, 2, 0)
)
if mibBuilder.loadTexts:
    zrgBatterRelayTrapV2.setStatus("current")
_ZnidResources_ObjectIdentity = ObjectIdentity
znidResources = _ZnidResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 14)
)
if mibBuilder.loadTexts:
    znidResources.setStatus("current")


class _ZnidBatteryStatus_Type(Bits):
    """Custom type znidBatteryStatus based on Bits"""
    namedValues = NamedValues(
        *(("batteryPowerLow", 2),
          ("batteryRemoved", 4),
          ("noUPS", 5),
          ("normal", 0),
          ("onBatteryPower", 1),
          ("replaceBattery", 3))
    )

_ZnidBatteryStatus_Type.__name__ = "Bits"
_ZnidBatteryStatus_Object = MibScalar
znidBatteryStatus = _ZnidBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 14, 1),
    _ZnidBatteryStatus_Type()
)
znidBatteryStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    znidBatteryStatus.setStatus("current")
_ZnidSerialNumber_Type = Unsigned32
_ZnidSerialNumber_Object = MibScalar
znidSerialNumber = _ZnidSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 14, 2),
    _ZnidSerialNumber_Type()
)
znidSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    znidSerialNumber.setStatus("current")
_ZnidNotificationObjects_ObjectIdentity = ObjectIdentity
znidNotificationObjects = _ZnidNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 14, 3)
)
if mibBuilder.loadTexts:
    znidNotificationObjects.setStatus("current")
_ZnidNotifications_ObjectIdentity = ObjectIdentity
znidNotifications = _ZnidNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 14, 3, 0)
)
if mibBuilder.loadTexts:
    znidNotifications.setStatus("current")
cardResourceEntry.registerAugmentions(
    ("ZHONE-CARD-RESOURCES-MIB",
     "cardSoftwareEntry")
)
cardSoftwareEntry.setIndexNames(*cardResourceEntry.getIndexNames())
cardResourceEntry.registerAugmentions(
    ("ZHONE-CARD-RESOURCES-MIB",
     "cardRuntimeEntry")
)
cardRuntimeEntry.setIndexNames(*cardResourceEntry.getIndexNames())

# Managed Objects groups

zhoneCardResourcesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 9, 1, 1)
)
zhoneCardResourcesGroup.setObjects(
      *(("ZHONE-CARD-RESOURCES-MIB", "cardIdentification"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardZhoneType"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardMfgSerialNumber"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardMfgCLEICode"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardMfgRevisionCode"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardMfgBootRevision"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardPostResults"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardAdminStatus"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardOperStatus"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardAdminStatsEnable"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardUpTime"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardProcessorType"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardPortStatus"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardInterfaceType"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardSwRunningVers"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardSwUpgradeVers"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardSwAdmin"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardSwStatus"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardPeakMemUsage"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardAvailMem"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardTotalMem"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardProcessorIdle"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardProcessorUsage"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardProcessorServicesUsage"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardProcessorFrameworkUsage"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardProcessorLowUsage"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardProcessorHighUsage"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardMemStatus"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardPweTimingMode"))
)
if mibBuilder.loadTexts:
    zhoneCardResourcesGroup.setStatus("current")

zhoneExternalRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 9, 1, 2)
)
zhoneExternalRelayGroup.setObjects(
      *(("ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayName"),
        ("ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayState"),
        ("ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayId"))
)
if mibBuilder.loadTexts:
    zhoneExternalRelayGroup.setStatus("current")

znidOjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 14, 3, 2)
)
znidOjectGroup.setObjects(
      *(("ZHONE-CARD-RESOURCES-MIB", "znidBatteryStatus"),
        ("ZHONE-CARD-RESOURCES-MIB", "znidSerialNumber"))
)
if mibBuilder.loadTexts:
    znidOjectGroup.setStatus("current")


# Notification objects

zhoneCardServicesStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 4, 0, 1)
)
zhoneCardServicesStatusChange.setObjects(
    ("ZHONE-CARD-RESOURCES-MIB", "cardServiceStatus")
)
if mibBuilder.loadTexts:
    zhoneCardServicesStatusChange.setStatus(
        "current"
    )

zhoneCardServicesStandbyReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 4, 4, 0, 2)
)
zhoneCardServicesStandbyReady.setObjects(
      *(("ZHONE-CARD-RESOURCES-MIB", "standbyServiceShelf"),
        ("ZHONE-CARD-RESOURCES-MIB", "standbyServiceSlot"))
)
if mibBuilder.loadTexts:
    zhoneCardServicesStandbyReady.setStatus(
        "current"
    )

zhoneExternalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 3, 0, 1)
)
zhoneExternalAlarmTrap.setObjects(
      *(("ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayName"),
        ("ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayState"))
)
if mibBuilder.loadTexts:
    zhoneExternalAlarmTrap.setStatus(
        "current"
    )

zhoneMxkAlarmInputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 8, 3, 0, 2)
)
zhoneMxkAlarmInputTrap.setObjects(
      *(("ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayName"),
        ("ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayState"),
        ("ZHONE-CARD-RESOURCES-MIB", "zhoneExternalRelayNormalState"))
)
if mibBuilder.loadTexts:
    zhoneMxkAlarmInputTrap.setStatus(
        "current"
    )

zhoneTrapCardMemStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 10, 2)
)
zhoneTrapCardMemStatus.setObjects(
    ("ZHONE-CARD-RESOURCES-MIB", "cardMemStatus")
)
if mibBuilder.loadTexts:
    zhoneTrapCardMemStatus.setStatus(
        "current"
    )

zhoneTrapProcessorUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 10, 3)
)
zhoneTrapProcessorUsage.setObjects(
    ("ZHONE-CARD-RESOURCES-MIB", "cardProcessorUsage")
)
if mibBuilder.loadTexts:
    zhoneTrapProcessorUsage.setStatus(
        "current"
    )

zrgBatteryRelayNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 11, 2, 0, 1)
)
zrgBatteryRelayNotification.setObjects(
    ("ZHONE-CARD-RESOURCES-MIB", "zrgBatteryRelayStatus")
)
if mibBuilder.loadTexts:
    zrgBatteryRelayNotification.setStatus(
        "current"
    )

znidBatteryStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 14, 3, 0, 1)
)
znidBatteryStatusNotification.setObjects(
      *(("ZHONE-CARD-RESOURCES-MIB", "znidSerialNumber"),
        ("ZHONE-CARD-RESOURCES-MIB", "znidBatteryStatus"))
)
if mibBuilder.loadTexts:
    znidBatteryStatusNotification.setStatus(
        "current"
    )


# Notifications groups

zhoneExternalAlarmTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 9, 1, 3)
)
zhoneExternalAlarmTrapGroup.setObjects(
      *(("ZHONE-CARD-RESOURCES-MIB", "zhoneExternalAlarmTrap"),
        ("ZHONE-CARD-RESOURCES-MIB", "zhoneMxkAlarmInputTrap"))
)
if mibBuilder.loadTexts:
    zhoneExternalAlarmTrapGroup.setStatus(
        "current"
    )

zhoneTrapCardMemGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 10, 1)
)
zhoneTrapCardMemGroup.setObjects(
      *(("ZHONE-CARD-RESOURCES-MIB", "zhoneTrapCardMemStatus"),
        ("ZHONE-CARD-RESOURCES-MIB", "zhoneTrapProcessorUsage"))
)
if mibBuilder.loadTexts:
    zhoneTrapCardMemGroup.setStatus(
        "current"
    )

znidNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 14, 3, 1)
)
znidNotificationGroup.setObjects(
    ("ZHONE-CARD-RESOURCES-MIB", "znidBatteryStatusNotification")
)
if mibBuilder.loadTexts:
    znidNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-CARD-RESOURCES-MIB",
    **{"Kbytes": Kbytes,
       "ZhoneServiceId": ZhoneServiceId,
       "cardResourceTable": cardResourceTable,
       "cardResourceEntry": cardResourceEntry,
       "cardIdentification": cardIdentification,
       "cardZhoneType": cardZhoneType,
       "cardMfgSerialNumber": cardMfgSerialNumber,
       "cardMfgCLEICode": cardMfgCLEICode,
       "cardMfgRevisionCode": cardMfgRevisionCode,
       "cardMfgBootRevision": cardMfgBootRevision,
       "cardPostResults": cardPostResults,
       "cardAdminStatus": cardAdminStatus,
       "cardOperStatus": cardOperStatus,
       "cardAdminStatsEnable": cardAdminStatsEnable,
       "cardUpTime": cardUpTime,
       "cardProcessorType": cardProcessorType,
       "cardPortStatus": cardPortStatus,
       "cardInterfaceType": cardInterfaceType,
       "cardAtmManualAal2bw": cardAtmManualAal2bw,
       "cardAtmManualAal2h": cardAtmManualAal2h,
       "cardLineVoltage": cardLineVoltage,
       "cardVpiVciRange": cardVpiVciRange,
       "cardPweTimingMode": cardPweTimingMode,
       "cardSoftwareTable": cardSoftwareTable,
       "cardSoftwareEntry": cardSoftwareEntry,
       "cardSwRunningVers": cardSwRunningVers,
       "cardSwUpgradeVers": cardSwUpgradeVers,
       "cardSwAdmin": cardSwAdmin,
       "cardSwStatus": cardSwStatus,
       "cardRuntimeTable": cardRuntimeTable,
       "cardRuntimeEntry": cardRuntimeEntry,
       "cardPeakMemUsage": cardPeakMemUsage,
       "cardAvailMem": cardAvailMem,
       "cardTotalMem": cardTotalMem,
       "cardProcessorIdle": cardProcessorIdle,
       "cardProcessorUsage": cardProcessorUsage,
       "cardMemStatus": cardMemStatus,
       "cardProcessorHighUsage": cardProcessorHighUsage,
       "cardProcessorServicesUsage": cardProcessorServicesUsage,
       "cardProcessorFrameworkUsage": cardProcessorFrameworkUsage,
       "cardProcessorLowUsage": cardProcessorLowUsage,
       "zhoneCardServices": zhoneCardServices,
       "cardServicesTable": cardServicesTable,
       "cardServicesEntry": cardServicesEntry,
       "cardServiceId": cardServiceId,
       "cardServiceInstance": cardServiceInstance,
       "cardServiceChangeTime": cardServiceChangeTime,
       "cardServiceStatus": cardServiceStatus,
       "activeServicesTable": activeServicesTable,
       "activeServicesEntry": activeServicesEntry,
       "activeServiceShelf": activeServiceShelf,
       "activeServiceSlot": activeServiceSlot,
       "activeServiceChangeTime": activeServiceChangeTime,
       "standbyServicesTable": standbyServicesTable,
       "standbyServicesEntry": standbyServicesEntry,
       "standbyServiceShelf": standbyServiceShelf,
       "standbyServiceSlot": standbyServiceSlot,
       "standbyServiceChangeTime": standbyServiceChangeTime,
       "zhoneTrapCardServices": zhoneTrapCardServices,
       "zhoneTrapCardServicesV2Traps": zhoneTrapCardServicesV2Traps,
       "zhoneCardServicesStatusChange": zhoneCardServicesStatusChange,
       "zhoneCardServicesStandbyReady": zhoneCardServicesStandbyReady,
       "zhoneExternalRelay": zhoneExternalRelay,
       "zhoneExternalRelayTable": zhoneExternalRelayTable,
       "zhoneExternalRelayEntry": zhoneExternalRelayEntry,
       "zhoneExternalRelayName": zhoneExternalRelayName,
       "zhoneExternalRelayState": zhoneExternalRelayState,
       "zhoneExternalRelayNormalState": zhoneExternalRelayNormalState,
       "zhoneExternalRelayMappingTable": zhoneExternalRelayMappingTable,
       "zhoneExternalRelayMappingEntry": zhoneExternalRelayMappingEntry,
       "zhoneExternalRelayId": zhoneExternalRelayId,
       "zhoneTrapExternalRelay": zhoneTrapExternalRelay,
       "zhoneTrapExternalRelayV2Traps": zhoneTrapExternalRelayV2Traps,
       "zhoneExternalAlarmTrap": zhoneExternalAlarmTrap,
       "zhoneMxkAlarmInputTrap": zhoneMxkAlarmInputTrap,
       "zhoneCardCompliances": zhoneCardCompliances,
       "zhoneCardGroups": zhoneCardGroups,
       "zhoneCardResourcesGroup": zhoneCardResourcesGroup,
       "zhoneExternalRelayGroup": zhoneExternalRelayGroup,
       "zhoneExternalAlarmTrapGroup": zhoneExternalAlarmTrapGroup,
       "zhoneTrapCardMemV2Traps": zhoneTrapCardMemV2Traps,
       "zhoneTrapCardMemGroup": zhoneTrapCardMemGroup,
       "zhoneTrapCardMemStatus": zhoneTrapCardMemStatus,
       "zhoneTrapProcessorUsage": zhoneTrapProcessorUsage,
       "zrgResources": zrgResources,
       "zrgBatteryRelayStatus": zrgBatteryRelayStatus,
       "zrgTrapBatteryRelay": zrgTrapBatteryRelay,
       "zrgBatterRelayTrapV2": zrgBatterRelayTrapV2,
       "zrgBatteryRelayNotification": zrgBatteryRelayNotification,
       "znidResources": znidResources,
       "znidBatteryStatus": znidBatteryStatus,
       "znidSerialNumber": znidSerialNumber,
       "znidNotificationObjects": znidNotificationObjects,
       "znidNotifications": znidNotifications,
       "znidBatteryStatusNotification": znidBatteryStatusNotification,
       "znidNotificationGroup": znidNotificationGroup,
       "znidOjectGroup": znidOjectGroup,
       "zhoneCardResourcesModule": zhoneCardResourcesModule}
)
