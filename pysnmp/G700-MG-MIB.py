# SNMP MIB module (G700-MG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/G700-MG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:34 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(genAppFileId,
 genAppFileName,
 genAppFileVersionNumber,
 genOpLastFailureIndex,
 genOpLastWarningDisplay) = mibBuilder.importSymbols(
    "LOAD-MIB",
    "genAppFileId",
    "genAppFileName",
    "genAppFileVersionNumber",
    "genOpLastFailureIndex",
    "genOpLastWarningDisplay")

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

cmgmib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1)
)
cmgmib.setRevisions(
        ("2014-05-08 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CmgItuPerceivedSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("cleared", 1),
          ("critical", 3),
          ("indeterminate", 2),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



class CmgModuleSlot(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )



# MIB Managed Objects in the order of their OIDs

_Avaya_ObjectIdentity = ObjectIdentity
avaya = _Avaya_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1)
)
_G700MediaGateway_ObjectIdentity = ObjectIdentity
g700MediaGateway = _G700MediaGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 9)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2)
)
_G700MediaGatewayMIB_ObjectIdentity = ObjectIdentity
g700MediaGatewayMIB = _G700MediaGatewayMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9)
)
_CmgChassis_ObjectIdentity = ObjectIdentity
cmgChassis = _CmgChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1)
)


class _CmgHWType_Type(Integer32):
    """Custom type cmgHWType based on Integer32"""
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
              10,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              37,
              41)
        )
    )
    namedValues = NamedValues(
        *(("avayaCommunicationManagerBranchEditionG430", 37),
          ("avayaCommunicationManagerBranchEditionG450", 35),
          ("avayaCommunicationManagerBranchEditioni120", 28),
          ("avayaCommunicationManagerBranchEditioni40-A14", 34),
          ("avayaCommunicationManagerBranchEditioni40-Analog", 29),
          ("avayaCommunicationManagerBranchEditioni40-BRI", 30),
          ("avayaCommunicationManagerBranchEditioni40-DCP", 32),
          ("avayaCommunicationManagerBranchEditioni40-DS1", 31),
          ("avayaG250", 3),
          ("avayaG250-A14", 8),
          ("avayaG250-BRI", 4),
          ("avayaG250-DCP", 6),
          ("avayaG250-DS1", 5),
          ("avayaG430", 41),
          ("avayaG450", 7),
          ("avayaTGM550", 10),
          ("avayaTRM480", 33),
          ("g350", 2),
          ("media-gateway", 1))
    )


_CmgHWType_Type.__name__ = "Integer32"
_CmgHWType_Object = MibScalar
cmgHWType = _CmgHWType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 1),
    _CmgHWType_Type()
)
cmgHWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgHWType.setStatus("current")


class _CmgModelNumber_Type(DisplayString):
    """Custom type cmgModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmgModelNumber_Type.__name__ = "DisplayString"
_CmgModelNumber_Object = MibScalar
cmgModelNumber = _CmgModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 2),
    _CmgModelNumber_Type()
)
cmgModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModelNumber.setStatus("current")


class _CmgDescription_Type(DisplayString):
    """Custom type cmgDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmgDescription_Type.__name__ = "DisplayString"
_CmgDescription_Object = MibScalar
cmgDescription = _CmgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 3),
    _CmgDescription_Type()
)
cmgDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDescription.setStatus("current")


class _CmgSerialNumber_Type(DisplayString):
    """Custom type cmgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmgSerialNumber_Type.__name__ = "DisplayString"
_CmgSerialNumber_Object = MibScalar
cmgSerialNumber = _CmgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 4),
    _CmgSerialNumber_Type()
)
cmgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgSerialNumber.setStatus("current")


class _CmgHWVintage_Type(DisplayString):
    """Custom type cmgHWVintage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmgHWVintage_Type.__name__ = "DisplayString"
_CmgHWVintage_Object = MibScalar
cmgHWVintage = _CmgHWVintage_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 5),
    _CmgHWVintage_Type()
)
cmgHWVintage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgHWVintage.setStatus("current")


class _CmgHWSuffix_Type(DisplayString):
    """Custom type cmgHWSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CmgHWSuffix_Type.__name__ = "DisplayString"
_CmgHWSuffix_Object = MibScalar
cmgHWSuffix = _CmgHWSuffix_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 6),
    _CmgHWSuffix_Type()
)
cmgHWSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgHWSuffix.setStatus("current")


class _CmgStackPosition_Type(Integer32):
    """Custom type cmgStackPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CmgStackPosition_Type.__name__ = "Integer32"
_CmgStackPosition_Object = MibScalar
cmgStackPosition = _CmgStackPosition_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 7),
    _CmgStackPosition_Type()
)
cmgStackPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgStackPosition.setStatus("current")


class _CmgModuleList_Type(OctetString):
    """Custom type cmgModuleList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_CmgModuleList_Type.__name__ = "OctetString"
_CmgModuleList_Object = MibScalar
cmgModuleList = _CmgModuleList_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 8),
    _CmgModuleList_Type()
)
cmgModuleList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleList.setStatus("current")


class _CmgReset_Type(Integer32):
    """Custom type cmgReset based on Integer32"""
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


_CmgReset_Type.__name__ = "Integer32"
_CmgReset_Object = MibScalar
cmgReset = _CmgReset_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 9),
    _CmgReset_Type()
)
cmgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgReset.setStatus("current")
_CmgHardware_ObjectIdentity = ObjectIdentity
cmgHardware = _CmgHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10)
)
_CmgCpuTemp_Type = Integer32
_CmgCpuTemp_Object = MibScalar
cmgCpuTemp = _CmgCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 1),
    _CmgCpuTemp_Type()
)
cmgCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCpuTemp.setStatus("current")
_CmgCpuTempWarningThresh_Type = Integer32
_CmgCpuTempWarningThresh_Object = MibScalar
cmgCpuTempWarningThresh = _CmgCpuTempWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 2),
    _CmgCpuTempWarningThresh_Type()
)
cmgCpuTempWarningThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCpuTempWarningThresh.setStatus("current")
_CmgCpuTempShutdownThresh_Type = Integer32
_CmgCpuTempShutdownThresh_Object = MibScalar
cmgCpuTempShutdownThresh = _CmgCpuTempShutdownThresh_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 3),
    _CmgCpuTempShutdownThresh_Type()
)
cmgCpuTempShutdownThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCpuTempShutdownThresh.setStatus("current")
_CmgDspTemp_Type = Integer32
_CmgDspTemp_Object = MibScalar
cmgDspTemp = _CmgDspTemp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 4),
    _CmgDspTemp_Type()
)
cmgDspTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDspTemp.setStatus("current")
_CmgDspTempWarningThresh_Type = Integer32
_CmgDspTempWarningThresh_Object = MibScalar
cmgDspTempWarningThresh = _CmgDspTempWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 5),
    _CmgDspTempWarningThresh_Type()
)
cmgDspTempWarningThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDspTempWarningThresh.setStatus("current")
_CmgDspTempShutdownThresh_Type = Integer32
_CmgDspTempShutdownThresh_Object = MibScalar
cmgDspTempShutdownThresh = _CmgDspTempShutdownThresh_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 6),
    _CmgDspTempShutdownThresh_Type()
)
cmgDspTempShutdownThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDspTempShutdownThresh.setStatus("current")
_CmgPowerMgProcessor_Type = Integer32
_CmgPowerMgProcessor_Object = MibScalar
cmgPowerMgProcessor = _CmgPowerMgProcessor_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 7),
    _CmgPowerMgProcessor_Type()
)
cmgPowerMgProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgPowerMgProcessor.setStatus("current")
_CmgPowerMediaModules_Type = Integer32
_CmgPowerMediaModules_Object = MibScalar
cmgPowerMediaModules = _CmgPowerMediaModules_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 8),
    _CmgPowerMediaModules_Type()
)
cmgPowerMediaModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgPowerMediaModules.setStatus("current")
_CmgPowerVoipComplex_Type = Integer32
_CmgPowerVoipComplex_Object = MibScalar
cmgPowerVoipComplex = _CmgPowerVoipComplex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 9),
    _CmgPowerVoipComplex_Type()
)
cmgPowerVoipComplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgPowerVoipComplex.setStatus("current")
_CmgPowerDsp_Type = Integer32
_CmgPowerDsp_Object = MibScalar
cmgPowerDsp = _CmgPowerDsp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 10),
    _CmgPowerDsp_Type()
)
cmgPowerDsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgPowerDsp.setStatus("current")
_CmgPower8260_Type = Integer32
_CmgPower8260_Object = MibScalar
cmgPower8260 = _CmgPower8260_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 11),
    _CmgPower8260_Type()
)
cmgPower8260.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgPower8260.setStatus("current")


class _CmgHardwareFaultMask_Type(OctetString):
    """Custom type cmgHardwareFaultMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CmgHardwareFaultMask_Type.__name__ = "OctetString"
_CmgHardwareFaultMask_Object = MibScalar
cmgHardwareFaultMask = _CmgHardwareFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 12),
    _CmgHardwareFaultMask_Type()
)
cmgHardwareFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgHardwareFaultMask.setStatus("current")


class _CmgHardwareStatusMask_Type(OctetString):
    """Custom type cmgHardwareStatusMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CmgHardwareStatusMask_Type.__name__ = "OctetString"
_CmgHardwareStatusMask_Object = MibScalar
cmgHardwareStatusMask = _CmgHardwareStatusMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 13),
    _CmgHardwareStatusMask_Type()
)
cmgHardwareStatusMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgHardwareStatusMask.setStatus("current")


class _CmgHardwareFanLowSpeedLevel_Type(Integer32):
    """Custom type cmgHardwareFanLowSpeedLevel based on Integer32"""
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


_CmgHardwareFanLowSpeedLevel_Type.__name__ = "Integer32"
_CmgHardwareFanLowSpeedLevel_Object = MibScalar
cmgHardwareFanLowSpeedLevel = _CmgHardwareFanLowSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 10, 14),
    _CmgHardwareFanLowSpeedLevel_Type()
)
cmgHardwareFanLowSpeedLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgHardwareFanLowSpeedLevel.setStatus("current")
_CmgModules_ObjectIdentity = ObjectIdentity
cmgModules = _CmgModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11)
)
_CmgModuleTable_Object = MibTable
cmgModuleTable = _CmgModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cmgModuleTable.setStatus("current")
_CmgModuleEntry_Object = MibTableRow
cmgModuleEntry = _CmgModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1)
)
cmgModuleEntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgModuleSlot"),
)
if mibBuilder.loadTexts:
    cmgModuleEntry.setStatus("current")


class _CmgModuleSlot_Type(Integer32):
    """Custom type cmgModuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_CmgModuleSlot_Type.__name__ = "Integer32"
_CmgModuleSlot_Object = MibTableColumn
cmgModuleSlot = _CmgModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 1),
    _CmgModuleSlot_Type()
)
cmgModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleSlot.setStatus("current")


class _CmgModuleType_Type(Integer32):
    """Custom type cmgModuleType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
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
              29,
              30,
              31,
              32,
              33,
              34,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              253,
              255)
        )
    )
    namedValues = NamedValues(
        *(("analog", 4),
          ("avayaAM110ApplicationModule", 34),
          ("avayaCommunicationManagerBranchEditionG450Mainboard", 50),
          ("bri", 2),
          ("bri2", 10),
          ("bri8", 52),
          ("dcp", 3),
          ("dcp24", 17),
          ("dcp24hd", 13),
          ("ds1wan", 11),
          ("fxo4fxs4", 9),
          ("fxs24", 18),
          ("g250-int-12pDCP", 23),
          ("g250-int-BRI", 21),
          ("g250-int-DS1", 24),
          ("g250-int-analog-2L1T", 20),
          ("g250-int-analog-2L4T", 19),
          ("g250-int-analog-6L8T", 29),
          ("g350intana", 16),
          ("g430Mainboard", 51),
          ("g450Mainboard", 40),
          ("i120-intana", 44),
          ("i40-A14-int-analog-6L8T", 49),
          ("i40-int-BRI", 47),
          ("i40-int-DS1", 48),
          ("i40-int-analog-2L1T", 46),
          ("i40-int-analog-2L4T", 45),
          ("icc", 7),
          ("invalid", 253),
          ("poe24", 14),
          ("poe24cr", 25),
          ("poe40", 22),
          ("poe8", 26),
          ("t1e1", 5),
          ("t1e1-voip", 1),
          ("tgm550-int-analog-2L2T", 30),
          ("tim508", 41),
          ("tim510", 32),
          ("tim514", 31),
          ("tim516", 42),
          ("tim518", 43),
          ("tim521", 33),
          ("unknown", 255),
          ("uspwan", 12),
          ("voip", 6))
    )


_CmgModuleType_Type.__name__ = "Integer32"
_CmgModuleType_Object = MibTableColumn
cmgModuleType = _CmgModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 2),
    _CmgModuleType_Type()
)
cmgModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleType.setStatus("current")


class _CmgModuleDescription_Type(DisplayString):
    """Custom type cmgModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmgModuleDescription_Type.__name__ = "DisplayString"
_CmgModuleDescription_Object = MibTableColumn
cmgModuleDescription = _CmgModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 3),
    _CmgModuleDescription_Type()
)
cmgModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleDescription.setStatus("current")


class _CmgModuleName_Type(DisplayString):
    """Custom type cmgModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmgModuleName_Type.__name__ = "DisplayString"
_CmgModuleName_Object = MibTableColumn
cmgModuleName = _CmgModuleName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 4),
    _CmgModuleName_Type()
)
cmgModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleName.setStatus("current")


class _CmgModuleSerialNumber_Type(DisplayString):
    """Custom type cmgModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmgModuleSerialNumber_Type.__name__ = "DisplayString"
_CmgModuleSerialNumber_Object = MibTableColumn
cmgModuleSerialNumber = _CmgModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 5),
    _CmgModuleSerialNumber_Type()
)
cmgModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleSerialNumber.setStatus("current")


class _CmgModuleHWVintage_Type(DisplayString):
    """Custom type cmgModuleHWVintage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmgModuleHWVintage_Type.__name__ = "DisplayString"
_CmgModuleHWVintage_Object = MibTableColumn
cmgModuleHWVintage = _CmgModuleHWVintage_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 6),
    _CmgModuleHWVintage_Type()
)
cmgModuleHWVintage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleHWVintage.setStatus("current")


class _CmgModuleHWSuffix_Type(DisplayString):
    """Custom type cmgModuleHWSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CmgModuleHWSuffix_Type.__name__ = "DisplayString"
_CmgModuleHWSuffix_Object = MibTableColumn
cmgModuleHWSuffix = _CmgModuleHWSuffix_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 7),
    _CmgModuleHWSuffix_Type()
)
cmgModuleHWSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleHWSuffix.setStatus("current")


class _CmgModuleFWVersion_Type(DisplayString):
    """Custom type cmgModuleFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmgModuleFWVersion_Type.__name__ = "DisplayString"
_CmgModuleFWVersion_Object = MibTableColumn
cmgModuleFWVersion = _CmgModuleFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 8),
    _CmgModuleFWVersion_Type()
)
cmgModuleFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleFWVersion.setStatus("current")


class _CmgModuleNumberOfPorts_Type(Integer32):
    """Custom type cmgModuleNumberOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CmgModuleNumberOfPorts_Type.__name__ = "Integer32"
_CmgModuleNumberOfPorts_Object = MibTableColumn
cmgModuleNumberOfPorts = _CmgModuleNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 9),
    _CmgModuleNumberOfPorts_Type()
)
cmgModuleNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleNumberOfPorts.setStatus("current")


class _CmgModuleFaultMask_Type(OctetString):
    """Custom type cmgModuleFaultMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CmgModuleFaultMask_Type.__name__ = "OctetString"
_CmgModuleFaultMask_Object = MibTableColumn
cmgModuleFaultMask = _CmgModuleFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 10),
    _CmgModuleFaultMask_Type()
)
cmgModuleFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleFaultMask.setStatus("current")


class _CmgModuleStatusMask_Type(OctetString):
    """Custom type cmgModuleStatusMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CmgModuleStatusMask_Type.__name__ = "OctetString"
_CmgModuleStatusMask_Object = MibTableColumn
cmgModuleStatusMask = _CmgModuleStatusMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 11),
    _CmgModuleStatusMask_Type()
)
cmgModuleStatusMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleStatusMask.setStatus("current")


class _CmgModuleReset_Type(Integer32):
    """Custom type cmgModuleReset based on Integer32"""
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


_CmgModuleReset_Type.__name__ = "Integer32"
_CmgModuleReset_Object = MibTableColumn
cmgModuleReset = _CmgModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 12),
    _CmgModuleReset_Type()
)
cmgModuleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgModuleReset.setStatus("current")


class _CmgModuleNumberOfChannels_Type(Integer32):
    """Custom type cmgModuleNumberOfChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CmgModuleNumberOfChannels_Type.__name__ = "Integer32"
_CmgModuleNumberOfChannels_Object = MibTableColumn
cmgModuleNumberOfChannels = _CmgModuleNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 1, 1, 13),
    _CmgModuleNumberOfChannels_Type()
)
cmgModuleNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgModuleNumberOfChannels.setStatus("current")
_CmgDsu_ObjectIdentity = ObjectIdentity
cmgDsu = _CmgDsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2)
)
_CmgDsuConfigTable_Object = MibTable
cmgDsuConfigTable = _CmgDsuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    cmgDsuConfigTable.setStatus("obsolete")
_CmgDsuConfigEntry_Object = MibTableRow
cmgDsuConfigEntry = _CmgDsuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1)
)
cmgDsuConfigEntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgDsuSlot"),
    (0, "G700-MG-MIB", "cmgDsuPort"),
)
if mibBuilder.loadTexts:
    cmgDsuConfigEntry.setStatus("obsolete")


class _CmgDsuSlot_Type(Integer32):
    """Custom type cmgDsuSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmgDsuSlot_Type.__name__ = "Integer32"
_CmgDsuSlot_Object = MibTableColumn
cmgDsuSlot = _CmgDsuSlot_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 1),
    _CmgDsuSlot_Type()
)
cmgDsuSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuSlot.setStatus("obsolete")


class _CmgDsuPort_Type(Integer32):
    """Custom type cmgDsuPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CmgDsuPort_Type.__name__ = "Integer32"
_CmgDsuPort_Object = MibTableColumn
cmgDsuPort = _CmgDsuPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 2),
    _CmgDsuPort_Type()
)
cmgDsuPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuPort.setStatus("obsolete")


class _CmgDsuPortEnable_Type(Integer32):
    """Custom type cmgDsuPortEnable based on Integer32"""
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


_CmgDsuPortEnable_Type.__name__ = "Integer32"
_CmgDsuPortEnable_Object = MibTableColumn
cmgDsuPortEnable = _CmgDsuPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 3),
    _CmgDsuPortEnable_Type()
)
cmgDsuPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuPortEnable.setStatus("obsolete")


class _CmgDsuDataFormat_Type(Integer32):
    """Custom type cmgDsuDataFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate56Kbps", 1),
          ("rate64KbpsClear", 2))
    )


_CmgDsuDataFormat_Type.__name__ = "Integer32"
_CmgDsuDataFormat_Object = MibTableColumn
cmgDsuDataFormat = _CmgDsuDataFormat_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 4),
    _CmgDsuDataFormat_Type()
)
cmgDsuDataFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuDataFormat.setStatus("obsolete")


class _CmgDsuFlowControl_Type(Integer32):
    """Custom type cmgDsuFlowControl based on Integer32"""
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
        *(("disable", 4),
          ("dtr", 2),
          ("dtr-rts", 1),
          ("rts", 3))
    )


_CmgDsuFlowControl_Type.__name__ = "Integer32"
_CmgDsuFlowControl_Object = MibTableColumn
cmgDsuFlowControl = _CmgDsuFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 5),
    _CmgDsuFlowControl_Type()
)
cmgDsuFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuFlowControl.setStatus("obsolete")


class _CmgDsuYellowAlarmAction_Type(Integer32):
    """Custom type cmgDsuYellowAlarmAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halt", 2),
          ("noAction", 1))
    )


_CmgDsuYellowAlarmAction_Type.__name__ = "Integer32"
_CmgDsuYellowAlarmAction_Object = MibTableColumn
cmgDsuYellowAlarmAction = _CmgDsuYellowAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 6),
    _CmgDsuYellowAlarmAction_Type()
)
cmgDsuYellowAlarmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuYellowAlarmAction.setStatus("obsolete")


class _CmgDsuReceiveClock_Type(Integer32):
    """Custom type cmgDsuReceiveClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_CmgDsuReceiveClock_Type.__name__ = "Integer32"
_CmgDsuReceiveClock_Object = MibTableColumn
cmgDsuReceiveClock = _CmgDsuReceiveClock_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 7),
    _CmgDsuReceiveClock_Type()
)
cmgDsuReceiveClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuReceiveClock.setStatus("obsolete")


class _CmgDsuInvertTxC_Type(Integer32):
    """Custom type cmgDsuInvertTxC based on Integer32"""
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


_CmgDsuInvertTxC_Type.__name__ = "Integer32"
_CmgDsuInvertTxC_Object = MibTableColumn
cmgDsuInvertTxC = _CmgDsuInvertTxC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 8),
    _CmgDsuInvertTxC_Type()
)
cmgDsuInvertTxC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuInvertTxC.setStatus("obsolete")


class _CmgDsuInvertRxC_Type(Integer32):
    """Custom type cmgDsuInvertRxC based on Integer32"""
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


_CmgDsuInvertRxC_Type.__name__ = "Integer32"
_CmgDsuInvertRxC_Object = MibTableColumn
cmgDsuInvertRxC = _CmgDsuInvertRxC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 9),
    _CmgDsuInvertRxC_Type()
)
cmgDsuInvertRxC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuInvertRxC.setStatus("obsolete")


class _CmgDsuInvertTxD_Type(Integer32):
    """Custom type cmgDsuInvertTxD based on Integer32"""
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


_CmgDsuInvertTxD_Type.__name__ = "Integer32"
_CmgDsuInvertTxD_Object = MibTableColumn
cmgDsuInvertTxD = _CmgDsuInvertTxD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 10),
    _CmgDsuInvertTxD_Type()
)
cmgDsuInvertTxD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuInvertTxD.setStatus("obsolete")


class _CmgDsuInvertRxD_Type(Integer32):
    """Custom type cmgDsuInvertRxD based on Integer32"""
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


_CmgDsuInvertRxD_Type.__name__ = "Integer32"
_CmgDsuInvertRxD_Object = MibTableColumn
cmgDsuInvertRxD = _CmgDsuInvertRxD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 11),
    _CmgDsuInvertRxD_Type()
)
cmgDsuInvertRxD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuInvertRxD.setStatus("obsolete")


class _CmgDsuPortInitiatedLoopback_Type(Integer32):
    """Custom type cmgDsuPortInitiatedLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_CmgDsuPortInitiatedLoopback_Type.__name__ = "Integer32"
_CmgDsuPortInitiatedLoopback_Object = MibTableColumn
cmgDsuPortInitiatedLoopback = _CmgDsuPortInitiatedLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 12),
    _CmgDsuPortInitiatedLoopback_Type()
)
cmgDsuPortInitiatedLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuPortInitiatedLoopback.setStatus("obsolete")


class _CmgDsuNetworkInitiatedLoopback_Type(Integer32):
    """Custom type cmgDsuNetworkInitiatedLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_CmgDsuNetworkInitiatedLoopback_Type.__name__ = "Integer32"
_CmgDsuNetworkInitiatedLoopback_Object = MibTableColumn
cmgDsuNetworkInitiatedLoopback = _CmgDsuNetworkInitiatedLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 13),
    _CmgDsuNetworkInitiatedLoopback_Type()
)
cmgDsuNetworkInitiatedLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuNetworkInitiatedLoopback.setStatus("obsolete")


class _CmgDsuChannelAssignments_Type(OctetString):
    """Custom type cmgDsuChannelAssignments based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CmgDsuChannelAssignments_Type.__name__ = "OctetString"
_CmgDsuChannelAssignments_Object = MibTableColumn
cmgDsuChannelAssignments = _CmgDsuChannelAssignments_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 14),
    _CmgDsuChannelAssignments_Type()
)
cmgDsuChannelAssignments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuChannelAssignments.setStatus("obsolete")


class _CmgDsuDataRate_Type(Integer32):
    """Custom type cmgDsuDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CmgDsuDataRate_Type.__name__ = "Integer32"
_CmgDsuDataRate_Object = MibTableColumn
cmgDsuDataRate = _CmgDsuDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 1, 1, 15),
    _CmgDsuDataRate_Type()
)
cmgDsuDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuDataRate.setStatus("obsolete")
_CmgDsuPortStatusTable_Object = MibTable
cmgDsuPortStatusTable = _CmgDsuPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    cmgDsuPortStatusTable.setStatus("obsolete")
_CmgDsuPortStatusEntry_Object = MibTableRow
cmgDsuPortStatusEntry = _CmgDsuPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1)
)
cmgDsuPortStatusEntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgDsuSlot"),
    (0, "G700-MG-MIB", "cmgDsuPort"),
)
if mibBuilder.loadTexts:
    cmgDsuPortStatusEntry.setStatus("obsolete")


class _CmgDsuRTS_Type(Integer32):
    """Custom type cmgDsuRTS based on Integer32"""
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


_CmgDsuRTS_Type.__name__ = "Integer32"
_CmgDsuRTS_Object = MibTableColumn
cmgDsuRTS = _CmgDsuRTS_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 1),
    _CmgDsuRTS_Type()
)
cmgDsuRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuRTS.setStatus("obsolete")


class _CmgDsuDTR_Type(Integer32):
    """Custom type cmgDsuDTR based on Integer32"""
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


_CmgDsuDTR_Type.__name__ = "Integer32"
_CmgDsuDTR_Object = MibTableColumn
cmgDsuDTR = _CmgDsuDTR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 2),
    _CmgDsuDTR_Type()
)
cmgDsuDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuDTR.setStatus("obsolete")


class _CmgDsuLL_Type(Integer32):
    """Custom type cmgDsuLL based on Integer32"""
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


_CmgDsuLL_Type.__name__ = "Integer32"
_CmgDsuLL_Object = MibTableColumn
cmgDsuLL = _CmgDsuLL_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 3),
    _CmgDsuLL_Type()
)
cmgDsuLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuLL.setStatus("obsolete")


class _CmgDsuRL_Type(Integer32):
    """Custom type cmgDsuRL based on Integer32"""
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


_CmgDsuRL_Type.__name__ = "Integer32"
_CmgDsuRL_Object = MibTableColumn
cmgDsuRL = _CmgDsuRL_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 4),
    _CmgDsuRL_Type()
)
cmgDsuRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuRL.setStatus("obsolete")


class _CmgDsuRLSD_Type(Integer32):
    """Custom type cmgDsuRLSD based on Integer32"""
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


_CmgDsuRLSD_Type.__name__ = "Integer32"
_CmgDsuRLSD_Object = MibTableColumn
cmgDsuRLSD = _CmgDsuRLSD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 5),
    _CmgDsuRLSD_Type()
)
cmgDsuRLSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuRLSD.setStatus("obsolete")


class _CmgDsuCTS_Type(Integer32):
    """Custom type cmgDsuCTS based on Integer32"""
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


_CmgDsuCTS_Type.__name__ = "Integer32"
_CmgDsuCTS_Object = MibTableColumn
cmgDsuCTS = _CmgDsuCTS_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 6),
    _CmgDsuCTS_Type()
)
cmgDsuCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuCTS.setStatus("obsolete")


class _CmgDsuDSR_Type(Integer32):
    """Custom type cmgDsuDSR based on Integer32"""
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


_CmgDsuDSR_Type.__name__ = "Integer32"
_CmgDsuDSR_Object = MibTableColumn
cmgDsuDSR = _CmgDsuDSR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 7),
    _CmgDsuDSR_Type()
)
cmgDsuDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuDSR.setStatus("obsolete")


class _CmgDsuRing_Type(Integer32):
    """Custom type cmgDsuRing based on Integer32"""
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


_CmgDsuRing_Type.__name__ = "Integer32"
_CmgDsuRing_Object = MibTableColumn
cmgDsuRing = _CmgDsuRing_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 8),
    _CmgDsuRing_Type()
)
cmgDsuRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuRing.setStatus("obsolete")


class _CmgDsuTestMode_Type(Integer32):
    """Custom type cmgDsuTestMode based on Integer32"""
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


_CmgDsuTestMode_Type.__name__ = "Integer32"
_CmgDsuTestMode_Object = MibTableColumn
cmgDsuTestMode = _CmgDsuTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 9),
    _CmgDsuTestMode_Type()
)
cmgDsuTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuTestMode.setStatus("obsolete")


class _CmgDsuTxD_Type(Integer32):
    """Custom type cmgDsuTxD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycling", 3),
          ("mark", 1),
          ("space", 2))
    )


_CmgDsuTxD_Type.__name__ = "Integer32"
_CmgDsuTxD_Object = MibTableColumn
cmgDsuTxD = _CmgDsuTxD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 10),
    _CmgDsuTxD_Type()
)
cmgDsuTxD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuTxD.setStatus("obsolete")


class _CmgDsuRxD_Type(Integer32):
    """Custom type cmgDsuRxD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycling", 3),
          ("mark", 1),
          ("space", 2))
    )


_CmgDsuRxD_Type.__name__ = "Integer32"
_CmgDsuRxD_Object = MibTableColumn
cmgDsuRxD = _CmgDsuRxD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 11),
    _CmgDsuRxD_Type()
)
cmgDsuRxD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuRxD.setStatus("obsolete")


class _CmgDsuFaultMask_Type(OctetString):
    """Custom type cmgDsuFaultMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CmgDsuFaultMask_Type.__name__ = "OctetString"
_CmgDsuFaultMask_Object = MibTableColumn
cmgDsuFaultMask = _CmgDsuFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 12),
    _CmgDsuFaultMask_Type()
)
cmgDsuFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuFaultMask.setStatus("obsolete")


class _CmgDsuStatusMask_Type(OctetString):
    """Custom type cmgDsuStatusMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CmgDsuStatusMask_Type.__name__ = "OctetString"
_CmgDsuStatusMask_Object = MibTableColumn
cmgDsuStatusMask = _CmgDsuStatusMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 2, 1, 13),
    _CmgDsuStatusMask_Type()
)
cmgDsuStatusMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuStatusMask.setStatus("obsolete")
_CmgDsuTestTable_Object = MibTable
cmgDsuTestTable = _CmgDsuTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 3)
)
if mibBuilder.loadTexts:
    cmgDsuTestTable.setStatus("obsolete")
_CmgDsuTestEntry_Object = MibTableRow
cmgDsuTestEntry = _CmgDsuTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 3, 1)
)
cmgDsuTestEntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgDsuSlot"),
    (0, "G700-MG-MIB", "cmgDsuPort"),
)
if mibBuilder.loadTexts:
    cmgDsuTestEntry.setStatus("obsolete")


class _CmgDsuLoopbackPattern_Type(Integer32):
    """Custom type cmgDsuLoopbackPattern based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 2),
          ("allZeroes", 1),
          ("none", 255),
          ("oneIn5", 4),
          ("oneIn8", 5),
          ("oneZeroOne", 3),
          ("qrs", 7),
          ("qrs2047", 9),
          ("qrs511", 8),
          ("threeIn24", 6))
    )


_CmgDsuLoopbackPattern_Type.__name__ = "Integer32"
_CmgDsuLoopbackPattern_Object = MibTableColumn
cmgDsuLoopbackPattern = _CmgDsuLoopbackPattern_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 3, 1, 1),
    _CmgDsuLoopbackPattern_Type()
)
cmgDsuLoopbackPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuLoopbackPattern.setStatus("obsolete")


class _CmgDsuLocalDteLoopback_Type(Integer32):
    """Custom type cmgDsuLocalDteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CmgDsuLocalDteLoopback_Type.__name__ = "Integer32"
_CmgDsuLocalDteLoopback_Object = MibTableColumn
cmgDsuLocalDteLoopback = _CmgDsuLocalDteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 3, 1, 2),
    _CmgDsuLocalDteLoopback_Type()
)
cmgDsuLocalDteLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuLocalDteLoopback.setStatus("obsolete")


class _CmgDsuNearEndDataChannelLoopback_Type(Integer32):
    """Custom type cmgDsuNearEndDataChannelLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CmgDsuNearEndDataChannelLoopback_Type.__name__ = "Integer32"
_CmgDsuNearEndDataChannelLoopback_Object = MibTableColumn
cmgDsuNearEndDataChannelLoopback = _CmgDsuNearEndDataChannelLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 3, 1, 3),
    _CmgDsuNearEndDataChannelLoopback_Type()
)
cmgDsuNearEndDataChannelLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuNearEndDataChannelLoopback.setStatus("obsolete")


class _CmgDsuFarEndDataChannelLoopback_Type(Integer32):
    """Custom type cmgDsuFarEndDataChannelLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CmgDsuFarEndDataChannelLoopback_Type.__name__ = "Integer32"
_CmgDsuFarEndDataChannelLoopback_Object = MibTableColumn
cmgDsuFarEndDataChannelLoopback = _CmgDsuFarEndDataChannelLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 3, 1, 4),
    _CmgDsuFarEndDataChannelLoopback_Type()
)
cmgDsuFarEndDataChannelLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuFarEndDataChannelLoopback.setStatus("obsolete")


class _CmgDsuRemoteLoopback_Type(Integer32):
    """Custom type cmgDsuRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CmgDsuRemoteLoopback_Type.__name__ = "Integer32"
_CmgDsuRemoteLoopback_Object = MibTableColumn
cmgDsuRemoteLoopback = _CmgDsuRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 3, 1, 5),
    _CmgDsuRemoteLoopback_Type()
)
cmgDsuRemoteLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuRemoteLoopback.setStatus("obsolete")


class _CmgDsuDataTerminalLoopback_Type(Integer32):
    """Custom type cmgDsuDataTerminalLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CmgDsuDataTerminalLoopback_Type.__name__ = "Integer32"
_CmgDsuDataTerminalLoopback_Object = MibTableColumn
cmgDsuDataTerminalLoopback = _CmgDsuDataTerminalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 3, 1, 6),
    _CmgDsuDataTerminalLoopback_Type()
)
cmgDsuDataTerminalLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDsuDataTerminalLoopback.setStatus("obsolete")


class _CmgDsuReset_Type(Integer32):
    """Custom type cmgDsuReset based on Integer32"""
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


_CmgDsuReset_Type.__name__ = "Integer32"
_CmgDsuReset_Object = MibTableColumn
cmgDsuReset = _CmgDsuReset_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 11, 2, 3, 1, 7),
    _CmgDsuReset_Type()
)
cmgDsuReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDsuReset.setStatus("obsolete")
_CmgAnalogPorts_ObjectIdentity = ObjectIdentity
cmgAnalogPorts = _CmgAnalogPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12)
)
_CmgAnalogPortTable_Object = MibTable
cmgAnalogPortTable = _CmgAnalogPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cmgAnalogPortTable.setStatus("current")
_CmgAnalogPortEntry_Object = MibTableRow
cmgAnalogPortEntry = _CmgAnalogPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1, 1)
)
cmgAnalogPortEntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgAnalogSlot"),
    (0, "G700-MG-MIB", "cmgAnalogPort"),
)
if mibBuilder.loadTexts:
    cmgAnalogPortEntry.setStatus("current")


class _CmgAnalogSlot_Type(Integer32):
    """Custom type cmgAnalogSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_CmgAnalogSlot_Type.__name__ = "Integer32"
_CmgAnalogSlot_Object = MibTableColumn
cmgAnalogSlot = _CmgAnalogSlot_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1, 1, 1),
    _CmgAnalogSlot_Type()
)
cmgAnalogSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgAnalogSlot.setStatus("current")


class _CmgAnalogPort_Type(Integer32):
    """Custom type cmgAnalogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CmgAnalogPort_Type.__name__ = "Integer32"
_CmgAnalogPort_Object = MibTableColumn
cmgAnalogPort = _CmgAnalogPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1, 1, 2),
    _CmgAnalogPort_Type()
)
cmgAnalogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgAnalogPort.setStatus("current")


class _CmgAnalogEchoCancellerControl_Type(Integer32):
    """Custom type cmgAnalogEchoCancellerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("fixedOn", 3),
          ("notSupported", 4),
          ("off", 2),
          ("on", 1))
    )


_CmgAnalogEchoCancellerControl_Type.__name__ = "Integer32"
_CmgAnalogEchoCancellerControl_Object = MibTableColumn
cmgAnalogEchoCancellerControl = _CmgAnalogEchoCancellerControl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1, 1, 3),
    _CmgAnalogEchoCancellerControl_Type()
)
cmgAnalogEchoCancellerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgAnalogEchoCancellerControl.setStatus("current")


class _CmgAnalogEchoCancellerConfig1_Type(Integer32):
    """Custom type cmgAnalogEchoCancellerConfig1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmgAnalogEchoCancellerConfig1_Type.__name__ = "Integer32"
_CmgAnalogEchoCancellerConfig1_Object = MibTableColumn
cmgAnalogEchoCancellerConfig1 = _CmgAnalogEchoCancellerConfig1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1, 1, 4),
    _CmgAnalogEchoCancellerConfig1_Type()
)
cmgAnalogEchoCancellerConfig1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgAnalogEchoCancellerConfig1.setStatus("current")


class _CmgAnalogEchoCancellerConfig2_Type(Integer32):
    """Custom type cmgAnalogEchoCancellerConfig2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmgAnalogEchoCancellerConfig2_Type.__name__ = "Integer32"
_CmgAnalogEchoCancellerConfig2_Object = MibTableColumn
cmgAnalogEchoCancellerConfig2 = _CmgAnalogEchoCancellerConfig2_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1, 1, 5),
    _CmgAnalogEchoCancellerConfig2_Type()
)
cmgAnalogEchoCancellerConfig2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgAnalogEchoCancellerConfig2.setStatus("current")


class _CmgAnalogBalance_Type(Integer32):
    """Custom type cmgAnalogBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CmgAnalogBalance_Type.__name__ = "Integer32"
_CmgAnalogBalance_Object = MibTableColumn
cmgAnalogBalance = _CmgAnalogBalance_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1, 1, 6),
    _CmgAnalogBalance_Type()
)
cmgAnalogBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgAnalogBalance.setStatus("current")


class _CmgAnalogReceiveGain_Type(Integer32):
    """Custom type cmgAnalogReceiveGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 300),
    )


_CmgAnalogReceiveGain_Type.__name__ = "Integer32"
_CmgAnalogReceiveGain_Object = MibTableColumn
cmgAnalogReceiveGain = _CmgAnalogReceiveGain_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1, 1, 7),
    _CmgAnalogReceiveGain_Type()
)
cmgAnalogReceiveGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgAnalogReceiveGain.setStatus("current")


class _CmgAnalogTransmitGain_Type(Integer32):
    """Custom type cmgAnalogTransmitGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 300),
    )


_CmgAnalogTransmitGain_Type.__name__ = "Integer32"
_CmgAnalogTransmitGain_Object = MibTableColumn
cmgAnalogTransmitGain = _CmgAnalogTransmitGain_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 12, 1, 1, 8),
    _CmgAnalogTransmitGain_Type()
)
cmgAnalogTransmitGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgAnalogTransmitGain.setStatus("current")
_CmgExpansionUnits_ObjectIdentity = ObjectIdentity
cmgExpansionUnits = _CmgExpansionUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13)
)
_CmgExpansionUnitsTable_Object = MibTable
cmgExpansionUnitsTable = _CmgExpansionUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    cmgExpansionUnitsTable.setStatus("current")
_CmgExpansions_Object = MibTableRow
cmgExpansions = _CmgExpansions_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1, 1)
)
cmgExpansions.setIndexNames(
    (0, "G700-MG-MIB", "cmgExpansionSlot"),
)
if mibBuilder.loadTexts:
    cmgExpansions.setStatus("current")


class _CmgExpansionSlot_Type(Integer32):
    """Custom type cmgExpansionSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CmgExpansionSlot_Type.__name__ = "Integer32"
_CmgExpansionSlot_Object = MibTableColumn
cmgExpansionSlot = _CmgExpansionSlot_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1, 1, 1),
    _CmgExpansionSlot_Type()
)
cmgExpansionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgExpansionSlot.setStatus("current")


class _CmgExpansionModelNumber_Type(DisplayString):
    """Custom type cmgExpansionModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmgExpansionModelNumber_Type.__name__ = "DisplayString"
_CmgExpansionModelNumber_Object = MibTableColumn
cmgExpansionModelNumber = _CmgExpansionModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1, 1, 2),
    _CmgExpansionModelNumber_Type()
)
cmgExpansionModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgExpansionModelNumber.setStatus("current")


class _CmgExpansionDescription_Type(DisplayString):
    """Custom type cmgExpansionDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmgExpansionDescription_Type.__name__ = "DisplayString"
_CmgExpansionDescription_Object = MibTableColumn
cmgExpansionDescription = _CmgExpansionDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1, 1, 3),
    _CmgExpansionDescription_Type()
)
cmgExpansionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgExpansionDescription.setStatus("current")


class _CmgExpansionSerialNumber_Type(DisplayString):
    """Custom type cmgExpansionSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmgExpansionSerialNumber_Type.__name__ = "DisplayString"
_CmgExpansionSerialNumber_Object = MibTableColumn
cmgExpansionSerialNumber = _CmgExpansionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1, 1, 4),
    _CmgExpansionSerialNumber_Type()
)
cmgExpansionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgExpansionSerialNumber.setStatus("current")


class _CmgExpansionHWVintage_Type(DisplayString):
    """Custom type cmgExpansionHWVintage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmgExpansionHWVintage_Type.__name__ = "DisplayString"
_CmgExpansionHWVintage_Object = MibTableColumn
cmgExpansionHWVintage = _CmgExpansionHWVintage_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1, 1, 5),
    _CmgExpansionHWVintage_Type()
)
cmgExpansionHWVintage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgExpansionHWVintage.setStatus("current")


class _CmgExpansionHWSuffix_Type(DisplayString):
    """Custom type cmgExpansionHWSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CmgExpansionHWSuffix_Type.__name__ = "DisplayString"
_CmgExpansionHWSuffix_Object = MibTableColumn
cmgExpansionHWSuffix = _CmgExpansionHWSuffix_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1, 1, 6),
    _CmgExpansionHWSuffix_Type()
)
cmgExpansionHWSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgExpansionHWSuffix.setStatus("current")


class _CmgExpansionDemandTest_Type(Integer32):
    """Custom type cmgExpansionDemandTest based on Integer32"""
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


_CmgExpansionDemandTest_Type.__name__ = "Integer32"
_CmgExpansionDemandTest_Object = MibTableColumn
cmgExpansionDemandTest = _CmgExpansionDemandTest_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1, 1, 7),
    _CmgExpansionDemandTest_Type()
)
cmgExpansionDemandTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgExpansionDemandTest.setStatus("current")


class _CmgExpansionDemandTestResult_Type(Integer32):
    """Custom type cmgExpansionDemandTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("pass", 255))
    )


_CmgExpansionDemandTestResult_Type.__name__ = "Integer32"
_CmgExpansionDemandTestResult_Object = MibTableColumn
cmgExpansionDemandTestResult = _CmgExpansionDemandTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 13, 1, 1, 8),
    _CmgExpansionDemandTestResult_Type()
)
cmgExpansionDemandTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgExpansionDemandTestResult.setStatus("current")


class _CmgTimeslotMonitoring_Type(Integer32):
    """Custom type cmgTimeslotMonitoring based on Integer32"""
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


_CmgTimeslotMonitoring_Type.__name__ = "Integer32"
_CmgTimeslotMonitoring_Object = MibScalar
cmgTimeslotMonitoring = _CmgTimeslotMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 14),
    _CmgTimeslotMonitoring_Type()
)
cmgTimeslotMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgTimeslotMonitoring.setStatus("current")


class _CmgTimeslotUpperThreshold_Type(Integer32):
    """Custom type cmgTimeslotUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CmgTimeslotUpperThreshold_Type.__name__ = "Integer32"
_CmgTimeslotUpperThreshold_Object = MibScalar
cmgTimeslotUpperThreshold = _CmgTimeslotUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 15),
    _CmgTimeslotUpperThreshold_Type()
)
cmgTimeslotUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgTimeslotUpperThreshold.setStatus("current")


class _CmgTimeslotLowerThreshold_Type(Integer32):
    """Custom type cmgTimeslotLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CmgTimeslotLowerThreshold_Type.__name__ = "Integer32"
_CmgTimeslotLowerThreshold_Object = MibScalar
cmgTimeslotLowerThreshold = _CmgTimeslotLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 1, 16),
    _CmgTimeslotLowerThreshold_Type()
)
cmgTimeslotLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgTimeslotLowerThreshold.setStatus("current")
_CmgProcessor_ObjectIdentity = ObjectIdentity
cmgProcessor = _CmgProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2)
)
_CmgProcessorConfig_ObjectIdentity = ObjectIdentity
cmgProcessorConfig = _CmgProcessorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1)
)


class _CmgGatewayNumber_Type(DisplayString):
    """Custom type cmgGatewayNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CmgGatewayNumber_Type.__name__ = "DisplayString"
_CmgGatewayNumber_Object = MibScalar
cmgGatewayNumber = _CmgGatewayNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 1),
    _CmgGatewayNumber_Type()
)
cmgGatewayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgGatewayNumber.setStatus("current")


class _CmgMACAddress_Type(OctetString):
    """Custom type cmgMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CmgMACAddress_Type.__name__ = "OctetString"
_CmgMACAddress_Object = MibScalar
cmgMACAddress = _CmgMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 2),
    _CmgMACAddress_Type()
)
cmgMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgMACAddress.setStatus("current")


class _CmgFWVersion_Type(OctetString):
    """Custom type cmgFWVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CmgFWVersion_Type.__name__ = "OctetString"
_CmgFWVersion_Object = MibScalar
cmgFWVersion = _CmgFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 3),
    _CmgFWVersion_Type()
)
cmgFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgFWVersion.setStatus("current")
_CmgCurrentIpAddress_Type = IpAddress
_CmgCurrentIpAddress_Object = MibScalar
cmgCurrentIpAddress = _CmgCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 4),
    _CmgCurrentIpAddress_Type()
)
cmgCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCurrentIpAddress.setStatus("current")


class _CmgUseDhcpForIpAddress_Type(Integer32):
    """Custom type cmgUseDhcpForIpAddress based on Integer32"""
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


_CmgUseDhcpForIpAddress_Type.__name__ = "Integer32"
_CmgUseDhcpForIpAddress_Object = MibScalar
cmgUseDhcpForIpAddress = _CmgUseDhcpForIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 7),
    _CmgUseDhcpForIpAddress_Type()
)
cmgUseDhcpForIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgUseDhcpForIpAddress.setStatus("current")


class _CmgUseDhcpForVlan_Type(Integer32):
    """Custom type cmgUseDhcpForVlan based on Integer32"""
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


_CmgUseDhcpForVlan_Type.__name__ = "Integer32"
_CmgUseDhcpForVlan_Object = MibScalar
cmgUseDhcpForVlan = _CmgUseDhcpForVlan_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 8),
    _CmgUseDhcpForVlan_Type()
)
cmgUseDhcpForVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgUseDhcpForVlan.setStatus("current")


class _CmgDhcpSson_Type(Integer32):
    """Custom type cmgDhcpSson based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_CmgDhcpSson_Type.__name__ = "Integer32"
_CmgDhcpSson_Object = MibScalar
cmgDhcpSson = _CmgDhcpSson_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 9),
    _CmgDhcpSson_Type()
)
cmgDhcpSson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDhcpSson.setStatus("current")
_CmgStaticIpAddress_Type = IpAddress
_CmgStaticIpAddress_Object = MibScalar
cmgStaticIpAddress = _CmgStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 10),
    _CmgStaticIpAddress_Type()
)
cmgStaticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgStaticIpAddress.setStatus("current")


class _CmgDnsServerList_Type(DisplayString):
    """Custom type cmgDnsServerList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmgDnsServerList_Type.__name__ = "DisplayString"
_CmgDnsServerList_Object = MibScalar
cmgDnsServerList = _CmgDnsServerList_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 13),
    _CmgDnsServerList_Type()
)
cmgDnsServerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDnsServerList.setStatus("current")


class _CmgDnsHostname_Type(DisplayString):
    """Custom type cmgDnsHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmgDnsHostname_Type.__name__ = "DisplayString"
_CmgDnsHostname_Object = MibScalar
cmgDnsHostname = _CmgDnsHostname_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 14),
    _CmgDnsHostname_Type()
)
cmgDnsHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDnsHostname.setStatus("current")


class _CmgMgpFaultMask_Type(OctetString):
    """Custom type cmgMgpFaultMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CmgMgpFaultMask_Type.__name__ = "OctetString"
_CmgMgpFaultMask_Object = MibScalar
cmgMgpFaultMask = _CmgMgpFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 15),
    _CmgMgpFaultMask_Type()
)
cmgMgpFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgMgpFaultMask.setStatus("current")
_CmgCurrentInetAddressType_Type = InetAddressType
_CmgCurrentInetAddressType_Object = MibScalar
cmgCurrentInetAddressType = _CmgCurrentInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 16),
    _CmgCurrentInetAddressType_Type()
)
cmgCurrentInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCurrentInetAddressType.setStatus("current")
_CmgCurrentInetAddress_Type = InetAddress
_CmgCurrentInetAddress_Object = MibScalar
cmgCurrentInetAddress = _CmgCurrentInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 1, 17),
    _CmgCurrentInetAddress_Type()
)
cmgCurrentInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCurrentInetAddress.setStatus("current")
_CmgProcessorQos_ObjectIdentity = ObjectIdentity
cmgProcessorQos = _CmgProcessorQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 2)
)


class _CmgQosControl_Type(Integer32):
    """Custom type cmgQosControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_CmgQosControl_Type.__name__ = "Integer32"
_CmgQosControl_Object = MibScalar
cmgQosControl = _CmgQosControl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 2, 1),
    _CmgQosControl_Type()
)
cmgQosControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgQosControl.setStatus("current")


class _CmgRemoteSigDscp_Type(Integer32):
    """Custom type cmgRemoteSigDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CmgRemoteSigDscp_Type.__name__ = "Integer32"
_CmgRemoteSigDscp_Object = MibScalar
cmgRemoteSigDscp = _CmgRemoteSigDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 2, 2),
    _CmgRemoteSigDscp_Type()
)
cmgRemoteSigDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgRemoteSigDscp.setStatus("current")


class _CmgRemoteSig802Priority_Type(Integer32):
    """Custom type cmgRemoteSig802Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CmgRemoteSig802Priority_Type.__name__ = "Integer32"
_CmgRemoteSig802Priority_Object = MibScalar
cmgRemoteSig802Priority = _CmgRemoteSig802Priority_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 2, 3),
    _CmgRemoteSig802Priority_Type()
)
cmgRemoteSig802Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgRemoteSig802Priority.setStatus("current")


class _CmgLocalSigDscp_Type(Integer32):
    """Custom type cmgLocalSigDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CmgLocalSigDscp_Type.__name__ = "Integer32"
_CmgLocalSigDscp_Object = MibScalar
cmgLocalSigDscp = _CmgLocalSigDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 2, 4),
    _CmgLocalSigDscp_Type()
)
cmgLocalSigDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgLocalSigDscp.setStatus("current")


class _CmgLocalSig802Priority_Type(Integer32):
    """Custom type cmgLocalSig802Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CmgLocalSig802Priority_Type.__name__ = "Integer32"
_CmgLocalSig802Priority_Object = MibScalar
cmgLocalSig802Priority = _CmgLocalSig802Priority_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 2, 5),
    _CmgLocalSig802Priority_Type()
)
cmgLocalSig802Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgLocalSig802Priority.setStatus("current")


class _CmgStatic802Vlan_Type(Integer32):
    """Custom type cmgStatic802Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_CmgStatic802Vlan_Type.__name__ = "Integer32"
_CmgStatic802Vlan_Object = MibScalar
cmgStatic802Vlan = _CmgStatic802Vlan_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 2, 6),
    _CmgStatic802Vlan_Type()
)
cmgStatic802Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgStatic802Vlan.setStatus("current")


class _CmgCurrent802Vlan_Type(Integer32):
    """Custom type cmgCurrent802Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_CmgCurrent802Vlan_Type.__name__ = "Integer32"
_CmgCurrent802Vlan_Object = MibScalar
cmgCurrent802Vlan = _CmgCurrent802Vlan_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 2, 7),
    _CmgCurrent802Vlan_Type()
)
cmgCurrent802Vlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCurrent802Vlan.setStatus("current")
_CmgProcessorClock_ObjectIdentity = ObjectIdentity
cmgProcessorClock = _CmgProcessorClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 3)
)


class _CmgPrimaryClockSource_Type(DisplayString):
    """Custom type cmgPrimaryClockSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_CmgPrimaryClockSource_Type.__name__ = "DisplayString"
_CmgPrimaryClockSource_Object = MibScalar
cmgPrimaryClockSource = _CmgPrimaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 3, 1),
    _CmgPrimaryClockSource_Type()
)
cmgPrimaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgPrimaryClockSource.setStatus("current")


class _CmgSecondaryClockSource_Type(DisplayString):
    """Custom type cmgSecondaryClockSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_CmgSecondaryClockSource_Type.__name__ = "DisplayString"
_CmgSecondaryClockSource_Object = MibScalar
cmgSecondaryClockSource = _CmgSecondaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 3, 2),
    _CmgSecondaryClockSource_Type()
)
cmgSecondaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgSecondaryClockSource.setStatus("current")


class _CmgActiveClockSource_Type(Integer32):
    """Custom type cmgActiveClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_CmgActiveClockSource_Type.__name__ = "Integer32"
_CmgActiveClockSource_Object = MibScalar
cmgActiveClockSource = _CmgActiveClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 3, 3),
    _CmgActiveClockSource_Type()
)
cmgActiveClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgActiveClockSource.setStatus("current")


class _CmgClockSwitching_Type(Integer32):
    """Custom type cmgClockSwitching based on Integer32"""
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


_CmgClockSwitching_Type.__name__ = "Integer32"
_CmgClockSwitching_Object = MibScalar
cmgClockSwitching = _CmgClockSwitching_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 3, 4),
    _CmgClockSwitching_Type()
)
cmgClockSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgClockSwitching.setStatus("current")


class _CmgClockSourceControl_Type(Integer32):
    """Custom type cmgClockSourceControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_CmgClockSourceControl_Type.__name__ = "Integer32"
_CmgClockSourceControl_Object = MibScalar
cmgClockSourceControl = _CmgClockSourceControl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 2, 3, 5),
    _CmgClockSourceControl_Type()
)
cmgClockSourceControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgClockSourceControl.setStatus("current")
_CmgControllers_ObjectIdentity = ObjectIdentity
cmgControllers = _CmgControllers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3)
)


class _CmgRegistrationState_Type(Integer32):
    """Custom type cmgRegistrationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 2),
          ("registered", 1))
    )


_CmgRegistrationState_Type.__name__ = "Integer32"
_CmgRegistrationState_Object = MibScalar
cmgRegistrationState = _CmgRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 1),
    _CmgRegistrationState_Type()
)
cmgRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgRegistrationState.setStatus("current")
_CmgActiveControllerAddress_Type = IpAddress
_CmgActiveControllerAddress_Object = MibScalar
cmgActiveControllerAddress = _CmgActiveControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 2),
    _CmgActiveControllerAddress_Type()
)
cmgActiveControllerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgActiveControllerAddress.setStatus("current")


class _CmgH248LinkStatus_Type(Integer32):
    """Custom type cmgH248LinkStatus based on Integer32"""
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


_CmgH248LinkStatus_Type.__name__ = "Integer32"
_CmgH248LinkStatus_Object = MibScalar
cmgH248LinkStatus = _CmgH248LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 3),
    _CmgH248LinkStatus_Type()
)
cmgH248LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgH248LinkStatus.setStatus("current")
_CmgH248LinkErrorCode_Type = Integer32
_CmgH248LinkErrorCode_Object = MibScalar
cmgH248LinkErrorCode = _CmgH248LinkErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 4),
    _CmgH248LinkErrorCode_Type()
)
cmgH248LinkErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgH248LinkErrorCode.setStatus("current")


class _CmgUseDhcpForMgcList_Type(Integer32):
    """Custom type cmgUseDhcpForMgcList based on Integer32"""
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


_CmgUseDhcpForMgcList_Type.__name__ = "Integer32"
_CmgUseDhcpForMgcList_Object = MibScalar
cmgUseDhcpForMgcList = _CmgUseDhcpForMgcList_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 5),
    _CmgUseDhcpForMgcList_Type()
)
cmgUseDhcpForMgcList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgUseDhcpForMgcList.setStatus("current")


class _CmgStaticControllerHosts_Type(DisplayString):
    """Custom type cmgStaticControllerHosts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmgStaticControllerHosts_Type.__name__ = "DisplayString"
_CmgStaticControllerHosts_Object = MibScalar
cmgStaticControllerHosts = _CmgStaticControllerHosts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 6),
    _CmgStaticControllerHosts_Type()
)
cmgStaticControllerHosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgStaticControllerHosts.setStatus("current")


class _CmgDhcpControllerHosts_Type(DisplayString):
    """Custom type cmgDhcpControllerHosts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmgDhcpControllerHosts_Type.__name__ = "DisplayString"
_CmgDhcpControllerHosts_Object = MibScalar
cmgDhcpControllerHosts = _CmgDhcpControllerHosts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 7),
    _CmgDhcpControllerHosts_Type()
)
cmgDhcpControllerHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDhcpControllerHosts.setStatus("current")


class _CmgPrimarySearchTime_Type(Integer32):
    """Custom type cmgPrimarySearchTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 59),
    )


_CmgPrimarySearchTime_Type.__name__ = "Integer32"
_CmgPrimarySearchTime_Object = MibScalar
cmgPrimarySearchTime = _CmgPrimarySearchTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 8),
    _CmgPrimarySearchTime_Type()
)
cmgPrimarySearchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgPrimarySearchTime.setStatus("current")


class _CmgTotalSearchTime_Type(Integer32):
    """Custom type cmgTotalSearchTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_CmgTotalSearchTime_Type.__name__ = "Integer32"
_CmgTotalSearchTime_Object = MibScalar
cmgTotalSearchTime = _CmgTotalSearchTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 9),
    _CmgTotalSearchTime_Type()
)
cmgTotalSearchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgTotalSearchTime.setStatus("current")


class _CmgTransitionPoint_Type(Integer32):
    """Custom type cmgTransitionPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmgTransitionPoint_Type.__name__ = "Integer32"
_CmgTransitionPoint_Object = MibScalar
cmgTransitionPoint = _CmgTransitionPoint_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 10),
    _CmgTransitionPoint_Type()
)
cmgTransitionPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgTransitionPoint.setStatus("current")


class _CmgActiveControllerSoftwareVersion_Type(DisplayString):
    """Custom type cmgActiveControllerSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmgActiveControllerSoftwareVersion_Type.__name__ = "DisplayString"
_CmgActiveControllerSoftwareVersion_Object = MibScalar
cmgActiveControllerSoftwareVersion = _CmgActiveControllerSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 11),
    _CmgActiveControllerSoftwareVersion_Type()
)
cmgActiveControllerSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgActiveControllerSoftwareVersion.setStatus("current")
_CmgActiveControllerInetAddressType_Type = InetAddressType
_CmgActiveControllerInetAddressType_Object = MibScalar
cmgActiveControllerInetAddressType = _CmgActiveControllerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 12),
    _CmgActiveControllerInetAddressType_Type()
)
cmgActiveControllerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgActiveControllerInetAddressType.setStatus("current")
_CmgActiveControllerInetAddress_Type = InetAddress
_CmgActiveControllerInetAddress_Object = MibScalar
cmgActiveControllerInetAddress = _CmgActiveControllerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 3, 13),
    _CmgActiveControllerInetAddress_Type()
)
cmgActiveControllerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgActiveControllerInetAddress.setStatus("current")
_CmgVoip_ObjectIdentity = ObjectIdentity
cmgVoip = _CmgVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4)
)


class _CmgVoipEngineUseDhcp_Type(Integer32):
    """Custom type cmgVoipEngineUseDhcp based on Integer32"""
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


_CmgVoipEngineUseDhcp_Type.__name__ = "Integer32"
_CmgVoipEngineUseDhcp_Object = MibScalar
cmgVoipEngineUseDhcp = _CmgVoipEngineUseDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 1),
    _CmgVoipEngineUseDhcp_Type()
)
cmgVoipEngineUseDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipEngineUseDhcp.setStatus("current")


class _CmgVoipQosControl_Type(Integer32):
    """Custom type cmgVoipQosControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_CmgVoipQosControl_Type.__name__ = "Integer32"
_CmgVoipQosControl_Object = MibScalar
cmgVoipQosControl = _CmgVoipQosControl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 2),
    _CmgVoipQosControl_Type()
)
cmgVoipQosControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipQosControl.setStatus("current")
_CmgVoipRemoteParameters_ObjectIdentity = ObjectIdentity
cmgVoipRemoteParameters = _CmgVoipRemoteParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3)
)
_CmgVoipRemoteQosParameters_ObjectIdentity = ObjectIdentity
cmgVoipRemoteQosParameters = _CmgVoipRemoteQosParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 1)
)


class _CmgVoipRemoteBbeDscp_Type(Integer32):
    """Custom type cmgVoipRemoteBbeDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CmgVoipRemoteBbeDscp_Type.__name__ = "Integer32"
_CmgVoipRemoteBbeDscp_Object = MibScalar
cmgVoipRemoteBbeDscp = _CmgVoipRemoteBbeDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 1, 1),
    _CmgVoipRemoteBbeDscp_Type()
)
cmgVoipRemoteBbeDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteBbeDscp.setStatus("current")


class _CmgVoipRemoteEfDscp_Type(Integer32):
    """Custom type cmgVoipRemoteEfDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CmgVoipRemoteEfDscp_Type.__name__ = "Integer32"
_CmgVoipRemoteEfDscp_Object = MibScalar
cmgVoipRemoteEfDscp = _CmgVoipRemoteEfDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 1, 2),
    _CmgVoipRemoteEfDscp_Type()
)
cmgVoipRemoteEfDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteEfDscp.setStatus("current")


class _CmgVoipRemote802Priority_Type(Integer32):
    """Custom type cmgVoipRemote802Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CmgVoipRemote802Priority_Type.__name__ = "Integer32"
_CmgVoipRemote802Priority_Object = MibScalar
cmgVoipRemote802Priority = _CmgVoipRemote802Priority_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 1, 3),
    _CmgVoipRemote802Priority_Type()
)
cmgVoipRemote802Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemote802Priority.setStatus("current")


class _CmgVoipRemoteMinRtpPort_Type(Integer32):
    """Custom type cmgVoipRemoteMinRtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65533),
    )


_CmgVoipRemoteMinRtpPort_Type.__name__ = "Integer32"
_CmgVoipRemoteMinRtpPort_Object = MibScalar
cmgVoipRemoteMinRtpPort = _CmgVoipRemoteMinRtpPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 1, 4),
    _CmgVoipRemoteMinRtpPort_Type()
)
cmgVoipRemoteMinRtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteMinRtpPort.setStatus("current")


class _CmgVoipRemoteMaxRtpPort_Type(Integer32):
    """Custom type cmgVoipRemoteMaxRtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_CmgVoipRemoteMaxRtpPort_Type.__name__ = "Integer32"
_CmgVoipRemoteMaxRtpPort_Object = MibScalar
cmgVoipRemoteMaxRtpPort = _CmgVoipRemoteMaxRtpPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 1, 5),
    _CmgVoipRemoteMaxRtpPort_Type()
)
cmgVoipRemoteMaxRtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteMaxRtpPort.setStatus("current")
_CmgVoipRemoteRtcpParameters_ObjectIdentity = ObjectIdentity
cmgVoipRemoteRtcpParameters = _CmgVoipRemoteRtcpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 2)
)


class _CmgVoipRemoteRtcpEnabled_Type(Integer32):
    """Custom type cmgVoipRemoteRtcpEnabled based on Integer32"""
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


_CmgVoipRemoteRtcpEnabled_Type.__name__ = "Integer32"
_CmgVoipRemoteRtcpEnabled_Object = MibScalar
cmgVoipRemoteRtcpEnabled = _CmgVoipRemoteRtcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 2, 1),
    _CmgVoipRemoteRtcpEnabled_Type()
)
cmgVoipRemoteRtcpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRtcpEnabled.setStatus("current")
_CmgVoipRemoteRtcpMonitorIpAddress_Type = IpAddress
_CmgVoipRemoteRtcpMonitorIpAddress_Object = MibScalar
cmgVoipRemoteRtcpMonitorIpAddress = _CmgVoipRemoteRtcpMonitorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 2, 2),
    _CmgVoipRemoteRtcpMonitorIpAddress_Type()
)
cmgVoipRemoteRtcpMonitorIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRtcpMonitorIpAddress.setStatus("current")


class _CmgVoipRemoteRtcpMonitorPort_Type(Integer32):
    """Custom type cmgVoipRemoteRtcpMonitorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmgVoipRemoteRtcpMonitorPort_Type.__name__ = "Integer32"
_CmgVoipRemoteRtcpMonitorPort_Object = MibScalar
cmgVoipRemoteRtcpMonitorPort = _CmgVoipRemoteRtcpMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 2, 3),
    _CmgVoipRemoteRtcpMonitorPort_Type()
)
cmgVoipRemoteRtcpMonitorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRtcpMonitorPort.setStatus("current")


class _CmgVoipRemoteRtcpReportPeriod_Type(Integer32):
    """Custom type cmgVoipRemoteRtcpReportPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_CmgVoipRemoteRtcpReportPeriod_Type.__name__ = "Integer32"
_CmgVoipRemoteRtcpReportPeriod_Object = MibScalar
cmgVoipRemoteRtcpReportPeriod = _CmgVoipRemoteRtcpReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 2, 4),
    _CmgVoipRemoteRtcpReportPeriod_Type()
)
cmgVoipRemoteRtcpReportPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRtcpReportPeriod.setStatus("current")
_CmgVoipRemoteRtcpMonitorInetAddressType_Type = InetAddressType
_CmgVoipRemoteRtcpMonitorInetAddressType_Object = MibScalar
cmgVoipRemoteRtcpMonitorInetAddressType = _CmgVoipRemoteRtcpMonitorInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 2, 5),
    _CmgVoipRemoteRtcpMonitorInetAddressType_Type()
)
cmgVoipRemoteRtcpMonitorInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRtcpMonitorInetAddressType.setStatus("current")
_CmgVoipRemoteRtcpMonitorInetAddress_Type = InetAddress
_CmgVoipRemoteRtcpMonitorInetAddress_Object = MibScalar
cmgVoipRemoteRtcpMonitorInetAddress = _CmgVoipRemoteRtcpMonitorInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 2, 6),
    _CmgVoipRemoteRtcpMonitorInetAddress_Type()
)
cmgVoipRemoteRtcpMonitorInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRtcpMonitorInetAddress.setStatus("current")


class _CmgVoipRemoteRtcpMonitorPortInetAddress_Type(Integer32):
    """Custom type cmgVoipRemoteRtcpMonitorPortInetAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmgVoipRemoteRtcpMonitorPortInetAddress_Type.__name__ = "Integer32"
_CmgVoipRemoteRtcpMonitorPortInetAddress_Object = MibScalar
cmgVoipRemoteRtcpMonitorPortInetAddress = _CmgVoipRemoteRtcpMonitorPortInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 2, 7),
    _CmgVoipRemoteRtcpMonitorPortInetAddress_Type()
)
cmgVoipRemoteRtcpMonitorPortInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRtcpMonitorPortInetAddress.setStatus("current")
_CmgVoipRemoteRsvpParameters_ObjectIdentity = ObjectIdentity
cmgVoipRemoteRsvpParameters = _CmgVoipRemoteRsvpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 3)
)


class _CmgVoipRemoteRsvpEnabled_Type(Integer32):
    """Custom type cmgVoipRemoteRsvpEnabled based on Integer32"""
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


_CmgVoipRemoteRsvpEnabled_Type.__name__ = "Integer32"
_CmgVoipRemoteRsvpEnabled_Object = MibScalar
cmgVoipRemoteRsvpEnabled = _CmgVoipRemoteRsvpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 3, 1),
    _CmgVoipRemoteRsvpEnabled_Type()
)
cmgVoipRemoteRsvpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRsvpEnabled.setStatus("current")


class _CmgVoipRemoteRetryOnFailure_Type(Integer32):
    """Custom type cmgVoipRemoteRetryOnFailure based on Integer32"""
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


_CmgVoipRemoteRetryOnFailure_Type.__name__ = "Integer32"
_CmgVoipRemoteRetryOnFailure_Object = MibScalar
cmgVoipRemoteRetryOnFailure = _CmgVoipRemoteRetryOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 3, 2),
    _CmgVoipRemoteRetryOnFailure_Type()
)
cmgVoipRemoteRetryOnFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRetryOnFailure.setStatus("current")


class _CmgVoipRemoteRetryDelay_Type(Integer32):
    """Custom type cmgVoipRemoteRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CmgVoipRemoteRetryDelay_Type.__name__ = "Integer32"
_CmgVoipRemoteRetryDelay_Object = MibScalar
cmgVoipRemoteRetryDelay = _CmgVoipRemoteRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 3, 3),
    _CmgVoipRemoteRetryDelay_Type()
)
cmgVoipRemoteRetryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRetryDelay.setStatus("current")


class _CmgVoipRemoteRsvpProfile_Type(Integer32):
    """Custom type cmgVoipRemoteRsvpProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlledLoadService", 2),
          ("guaranteedService", 1))
    )


_CmgVoipRemoteRsvpProfile_Type.__name__ = "Integer32"
_CmgVoipRemoteRsvpProfile_Object = MibScalar
cmgVoipRemoteRsvpProfile = _CmgVoipRemoteRsvpProfile_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 3, 3, 4),
    _CmgVoipRemoteRsvpProfile_Type()
)
cmgVoipRemoteRsvpProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipRemoteRsvpProfile.setStatus("current")
_CmgVoipLocalParameters_ObjectIdentity = ObjectIdentity
cmgVoipLocalParameters = _CmgVoipLocalParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4)
)
_CmgVoipLocalQosParameters_ObjectIdentity = ObjectIdentity
cmgVoipLocalQosParameters = _CmgVoipLocalQosParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 1)
)


class _CmgVoipLocalBbeDscp_Type(Integer32):
    """Custom type cmgVoipLocalBbeDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CmgVoipLocalBbeDscp_Type.__name__ = "Integer32"
_CmgVoipLocalBbeDscp_Object = MibScalar
cmgVoipLocalBbeDscp = _CmgVoipLocalBbeDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 1, 1),
    _CmgVoipLocalBbeDscp_Type()
)
cmgVoipLocalBbeDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalBbeDscp.setStatus("current")


class _CmgVoipLocalEfDscp_Type(Integer32):
    """Custom type cmgVoipLocalEfDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CmgVoipLocalEfDscp_Type.__name__ = "Integer32"
_CmgVoipLocalEfDscp_Object = MibScalar
cmgVoipLocalEfDscp = _CmgVoipLocalEfDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 1, 2),
    _CmgVoipLocalEfDscp_Type()
)
cmgVoipLocalEfDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalEfDscp.setStatus("current")


class _CmgVoipLocal802Priority_Type(Integer32):
    """Custom type cmgVoipLocal802Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CmgVoipLocal802Priority_Type.__name__ = "Integer32"
_CmgVoipLocal802Priority_Object = MibScalar
cmgVoipLocal802Priority = _CmgVoipLocal802Priority_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 1, 3),
    _CmgVoipLocal802Priority_Type()
)
cmgVoipLocal802Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocal802Priority.setStatus("current")


class _CmgVoipLocalMinRtpPort_Type(Integer32):
    """Custom type cmgVoipLocalMinRtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65533),
    )


_CmgVoipLocalMinRtpPort_Type.__name__ = "Integer32"
_CmgVoipLocalMinRtpPort_Object = MibScalar
cmgVoipLocalMinRtpPort = _CmgVoipLocalMinRtpPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 1, 4),
    _CmgVoipLocalMinRtpPort_Type()
)
cmgVoipLocalMinRtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalMinRtpPort.setStatus("current")


class _CmgVoipLocalMaxRtpPort_Type(Integer32):
    """Custom type cmgVoipLocalMaxRtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_CmgVoipLocalMaxRtpPort_Type.__name__ = "Integer32"
_CmgVoipLocalMaxRtpPort_Object = MibScalar
cmgVoipLocalMaxRtpPort = _CmgVoipLocalMaxRtpPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 1, 5),
    _CmgVoipLocalMaxRtpPort_Type()
)
cmgVoipLocalMaxRtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalMaxRtpPort.setStatus("current")
_CmgVoipLocalRtcpParameters_ObjectIdentity = ObjectIdentity
cmgVoipLocalRtcpParameters = _CmgVoipLocalRtcpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 2)
)


class _CmgVoipLocalRtcpEnabled_Type(Integer32):
    """Custom type cmgVoipLocalRtcpEnabled based on Integer32"""
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


_CmgVoipLocalRtcpEnabled_Type.__name__ = "Integer32"
_CmgVoipLocalRtcpEnabled_Object = MibScalar
cmgVoipLocalRtcpEnabled = _CmgVoipLocalRtcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 2, 1),
    _CmgVoipLocalRtcpEnabled_Type()
)
cmgVoipLocalRtcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalRtcpEnabled.setStatus("current")
_CmgVoipLocalRtcpMonitorIpAddress_Type = IpAddress
_CmgVoipLocalRtcpMonitorIpAddress_Object = MibScalar
cmgVoipLocalRtcpMonitorIpAddress = _CmgVoipLocalRtcpMonitorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 2, 2),
    _CmgVoipLocalRtcpMonitorIpAddress_Type()
)
cmgVoipLocalRtcpMonitorIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalRtcpMonitorIpAddress.setStatus("current")


class _CmgVoipLocalRtcpMonitorPort_Type(Integer32):
    """Custom type cmgVoipLocalRtcpMonitorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmgVoipLocalRtcpMonitorPort_Type.__name__ = "Integer32"
_CmgVoipLocalRtcpMonitorPort_Object = MibScalar
cmgVoipLocalRtcpMonitorPort = _CmgVoipLocalRtcpMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 2, 3),
    _CmgVoipLocalRtcpMonitorPort_Type()
)
cmgVoipLocalRtcpMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalRtcpMonitorPort.setStatus("current")


class _CmgVoipLocalRtcpReportPeriod_Type(Integer32):
    """Custom type cmgVoipLocalRtcpReportPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_CmgVoipLocalRtcpReportPeriod_Type.__name__ = "Integer32"
_CmgVoipLocalRtcpReportPeriod_Object = MibScalar
cmgVoipLocalRtcpReportPeriod = _CmgVoipLocalRtcpReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 2, 4),
    _CmgVoipLocalRtcpReportPeriod_Type()
)
cmgVoipLocalRtcpReportPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalRtcpReportPeriod.setStatus("current")
_CmgVoipLocalRtcpMonitorInetAddressType_Type = InetAddressType
_CmgVoipLocalRtcpMonitorInetAddressType_Object = MibScalar
cmgVoipLocalRtcpMonitorInetAddressType = _CmgVoipLocalRtcpMonitorInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 2, 5),
    _CmgVoipLocalRtcpMonitorInetAddressType_Type()
)
cmgVoipLocalRtcpMonitorInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipLocalRtcpMonitorInetAddressType.setStatus("current")
_CmgVoipLocalRtcpMonitorInetAddress_Type = InetAddress
_CmgVoipLocalRtcpMonitorInetAddress_Object = MibScalar
cmgVoipLocalRtcpMonitorInetAddress = _CmgVoipLocalRtcpMonitorInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 2, 6),
    _CmgVoipLocalRtcpMonitorInetAddress_Type()
)
cmgVoipLocalRtcpMonitorInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipLocalRtcpMonitorInetAddress.setStatus("current")


class _CmgVoipLocalRtcpMonitorPortInetAddress_Type(Integer32):
    """Custom type cmgVoipLocalRtcpMonitorPortInetAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmgVoipLocalRtcpMonitorPortInetAddress_Type.__name__ = "Integer32"
_CmgVoipLocalRtcpMonitorPortInetAddress_Object = MibScalar
cmgVoipLocalRtcpMonitorPortInetAddress = _CmgVoipLocalRtcpMonitorPortInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 2, 7),
    _CmgVoipLocalRtcpMonitorPortInetAddress_Type()
)
cmgVoipLocalRtcpMonitorPortInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalRtcpMonitorPortInetAddress.setStatus("current")
_CmgVoipLocalRsvpParameters_ObjectIdentity = ObjectIdentity
cmgVoipLocalRsvpParameters = _CmgVoipLocalRsvpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 3)
)


class _CmgVoipLocalRsvpEnabled_Type(Integer32):
    """Custom type cmgVoipLocalRsvpEnabled based on Integer32"""
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


_CmgVoipLocalRsvpEnabled_Type.__name__ = "Integer32"
_CmgVoipLocalRsvpEnabled_Object = MibScalar
cmgVoipLocalRsvpEnabled = _CmgVoipLocalRsvpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 3, 1),
    _CmgVoipLocalRsvpEnabled_Type()
)
cmgVoipLocalRsvpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalRsvpEnabled.setStatus("current")


class _CmgVoipLocalRetryOnFailure_Type(Integer32):
    """Custom type cmgVoipLocalRetryOnFailure based on Integer32"""
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


_CmgVoipLocalRetryOnFailure_Type.__name__ = "Integer32"
_CmgVoipLocalRetryOnFailure_Object = MibScalar
cmgVoipLocalRetryOnFailure = _CmgVoipLocalRetryOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 3, 2),
    _CmgVoipLocalRetryOnFailure_Type()
)
cmgVoipLocalRetryOnFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalRetryOnFailure.setStatus("current")


class _CmgVoipLocalRetryDelay_Type(Integer32):
    """Custom type cmgVoipLocalRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CmgVoipLocalRetryDelay_Type.__name__ = "Integer32"
_CmgVoipLocalRetryDelay_Object = MibScalar
cmgVoipLocalRetryDelay = _CmgVoipLocalRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 3, 3),
    _CmgVoipLocalRetryDelay_Type()
)
cmgVoipLocalRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalRetryDelay.setStatus("current")


class _CmgVoipLocalRsvpProfile_Type(Integer32):
    """Custom type cmgVoipLocalRsvpProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlledLoadService", 2),
          ("guaranteedService", 1))
    )


_CmgVoipLocalRsvpProfile_Type.__name__ = "Integer32"
_CmgVoipLocalRsvpProfile_Object = MibScalar
cmgVoipLocalRsvpProfile = _CmgVoipLocalRsvpProfile_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 4, 3, 4),
    _CmgVoipLocalRsvpProfile_Type()
)
cmgVoipLocalRsvpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipLocalRsvpProfile.setStatus("current")
_CmgVoipEngineTable_Object = MibTable
cmgVoipEngineTable = _CmgVoipEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cmgVoipEngineTable.setStatus("current")
_CmgVoipEngineEntry_Object = MibTableRow
cmgVoipEngineEntry = _CmgVoipEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1)
)
cmgVoipEngineEntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgVoipSlot"),
)
if mibBuilder.loadTexts:
    cmgVoipEngineEntry.setStatus("current")


class _CmgVoipSlot_Type(Integer32):
    """Custom type cmgVoipSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 104),
    )


_CmgVoipSlot_Type.__name__ = "Integer32"
_CmgVoipSlot_Object = MibTableColumn
cmgVoipSlot = _CmgVoipSlot_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 1),
    _CmgVoipSlot_Type()
)
cmgVoipSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipSlot.setStatus("current")


class _CmgVoipMACAddress_Type(OctetString):
    """Custom type cmgVoipMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CmgVoipMACAddress_Type.__name__ = "OctetString"
_CmgVoipMACAddress_Object = MibTableColumn
cmgVoipMACAddress = _CmgVoipMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 2),
    _CmgVoipMACAddress_Type()
)
cmgVoipMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipMACAddress.setStatus("current")
_CmgVoipStaticIpAddress_Type = IpAddress
_CmgVoipStaticIpAddress_Object = MibTableColumn
cmgVoipStaticIpAddress = _CmgVoipStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 3),
    _CmgVoipStaticIpAddress_Type()
)
cmgVoipStaticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipStaticIpAddress.setStatus("current")
_CmgVoipCurrentIpAddress_Type = IpAddress
_CmgVoipCurrentIpAddress_Object = MibTableColumn
cmgVoipCurrentIpAddress = _CmgVoipCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 4),
    _CmgVoipCurrentIpAddress_Type()
)
cmgVoipCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipCurrentIpAddress.setStatus("current")
_CmgVoipJitterBufferSize_Type = Integer32
_CmgVoipJitterBufferSize_Object = MibTableColumn
cmgVoipJitterBufferSize = _CmgVoipJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 5),
    _CmgVoipJitterBufferSize_Type()
)
cmgVoipJitterBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipJitterBufferSize.setStatus("current")
_CmgVoipTotalChannels_Type = Integer32
_CmgVoipTotalChannels_Object = MibTableColumn
cmgVoipTotalChannels = _CmgVoipTotalChannels_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 6),
    _CmgVoipTotalChannels_Type()
)
cmgVoipTotalChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipTotalChannels.setStatus("current")
_CmgVoipChannelsInUse_Type = Integer32
_CmgVoipChannelsInUse_Object = MibTableColumn
cmgVoipChannelsInUse = _CmgVoipChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 7),
    _CmgVoipChannelsInUse_Type()
)
cmgVoipChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipChannelsInUse.setStatus("current")


class _CmgVoipAverageOccupancy_Type(Integer32):
    """Custom type cmgVoipAverageOccupancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmgVoipAverageOccupancy_Type.__name__ = "Integer32"
_CmgVoipAverageOccupancy_Object = MibTableColumn
cmgVoipAverageOccupancy = _CmgVoipAverageOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 8),
    _CmgVoipAverageOccupancy_Type()
)
cmgVoipAverageOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipAverageOccupancy.setStatus("current")


class _CmgVoipHyperactivity_Type(Integer32):
    """Custom type cmgVoipHyperactivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hyperactive", 2),
          ("normal", 1),
          ("unknown", 255))
    )


_CmgVoipHyperactivity_Type.__name__ = "Integer32"
_CmgVoipHyperactivity_Object = MibTableColumn
cmgVoipHyperactivity = _CmgVoipHyperactivity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 9),
    _CmgVoipHyperactivity_Type()
)
cmgVoipHyperactivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipHyperactivity.setStatus("current")


class _CmgVoipAdminState_Type(Integer32):
    """Custom type cmgVoipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("busy-out", 1),
          ("camp-on", 3),
          ("release", 2),
          ("unknown", 255))
    )


_CmgVoipAdminState_Type.__name__ = "Integer32"
_CmgVoipAdminState_Object = MibTableColumn
cmgVoipAdminState = _CmgVoipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 10),
    _CmgVoipAdminState_Type()
)
cmgVoipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipAdminState.setStatus("current")


class _CmgVoipDspFWVersion_Type(DisplayString):
    """Custom type cmgVoipDspFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CmgVoipDspFWVersion_Type.__name__ = "DisplayString"
_CmgVoipDspFWVersion_Object = MibTableColumn
cmgVoipDspFWVersion = _CmgVoipDspFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 11),
    _CmgVoipDspFWVersion_Type()
)
cmgVoipDspFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipDspFWVersion.setStatus("current")


class _CmgVoipDspStatus_Type(Integer32):
    """Custom type cmgVoipDspStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("idle", 1),
          ("inUse", 2))
    )


_CmgVoipDspStatus_Type.__name__ = "Integer32"
_CmgVoipDspStatus_Object = MibTableColumn
cmgVoipDspStatus = _CmgVoipDspStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 12),
    _CmgVoipDspStatus_Type()
)
cmgVoipDspStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipDspStatus.setStatus("current")


class _CmgVoipEngineReset_Type(Integer32):
    """Custom type cmgVoipEngineReset based on Integer32"""
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


_CmgVoipEngineReset_Type.__name__ = "Integer32"
_CmgVoipEngineReset_Object = MibTableColumn
cmgVoipEngineReset = _CmgVoipEngineReset_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 13),
    _CmgVoipEngineReset_Type()
)
cmgVoipEngineReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipEngineReset.setStatus("current")


class _CmgVoipFaultMask_Type(OctetString):
    """Custom type cmgVoipFaultMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CmgVoipFaultMask_Type.__name__ = "OctetString"
_CmgVoipFaultMask_Object = MibTableColumn
cmgVoipFaultMask = _CmgVoipFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 14),
    _CmgVoipFaultMask_Type()
)
cmgVoipFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipFaultMask.setStatus("current")
_CmgVoipStaticInetAddressType_Type = InetAddressType
_CmgVoipStaticInetAddressType_Object = MibTableColumn
cmgVoipStaticInetAddressType = _CmgVoipStaticInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 15),
    _CmgVoipStaticInetAddressType_Type()
)
cmgVoipStaticInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipStaticInetAddressType.setStatus("current")
_CmgVoipStaticInetAddress_Type = InetAddress
_CmgVoipStaticInetAddress_Object = MibTableColumn
cmgVoipStaticInetAddress = _CmgVoipStaticInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 16),
    _CmgVoipStaticInetAddress_Type()
)
cmgVoipStaticInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipStaticInetAddress.setStatus("current")
_CmgVoipCurrentInetAddressType_Type = InetAddressType
_CmgVoipCurrentInetAddressType_Object = MibTableColumn
cmgVoipCurrentInetAddressType = _CmgVoipCurrentInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 17),
    _CmgVoipCurrentInetAddressType_Type()
)
cmgVoipCurrentInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipCurrentInetAddressType.setStatus("current")
_CmgVoipCurrentInetAddress_Type = InetAddress
_CmgVoipCurrentInetAddress_Object = MibTableColumn
cmgVoipCurrentInetAddress = _CmgVoipCurrentInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 5, 1, 18),
    _CmgVoipCurrentInetAddress_Type()
)
cmgVoipCurrentInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipCurrentInetAddress.setStatus("current")
_CmgVoipDSPCoreTable_Object = MibTable
cmgVoipDSPCoreTable = _CmgVoipDSPCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 6)
)
if mibBuilder.loadTexts:
    cmgVoipDSPCoreTable.setStatus("current")
_CmgVoipDSPCoreEntry_Object = MibTableRow
cmgVoipDSPCoreEntry = _CmgVoipDSPCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 6, 1)
)
cmgVoipDSPCoreEntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgVoipSlot"),
    (0, "G700-MG-MIB", "cmgDSPCoreCoreId"),
)
if mibBuilder.loadTexts:
    cmgVoipDSPCoreEntry.setStatus("current")


class _CmgDSPCoreCoreId_Type(Integer32):
    """Custom type cmgDSPCoreCoreId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmgDSPCoreCoreId_Type.__name__ = "Integer32"
_CmgDSPCoreCoreId_Object = MibTableColumn
cmgDSPCoreCoreId = _CmgDSPCoreCoreId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 6, 1, 1),
    _CmgDSPCoreCoreId_Type()
)
cmgDSPCoreCoreId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDSPCoreCoreId.setStatus("current")


class _CmgDSPCoreTotalChannels_Type(Integer32):
    """Custom type cmgDSPCoreTotalChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CmgDSPCoreTotalChannels_Type.__name__ = "Integer32"
_CmgDSPCoreTotalChannels_Object = MibTableColumn
cmgDSPCoreTotalChannels = _CmgDSPCoreTotalChannels_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 6, 1, 2),
    _CmgDSPCoreTotalChannels_Type()
)
cmgDSPCoreTotalChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDSPCoreTotalChannels.setStatus("current")


class _CmgDSPCoreChannelsInUse_Type(Integer32):
    """Custom type cmgDSPCoreChannelsInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CmgDSPCoreChannelsInUse_Type.__name__ = "Integer32"
_CmgDSPCoreChannelsInUse_Object = MibTableColumn
cmgDSPCoreChannelsInUse = _CmgDSPCoreChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 6, 1, 3),
    _CmgDSPCoreChannelsInUse_Type()
)
cmgDSPCoreChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDSPCoreChannelsInUse.setStatus("current")


class _CmgDSPCoreAdminState_Type(Integer32):
    """Custom type cmgDSPCoreAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("busy-out", 1),
          ("camp-on", 3),
          ("release", 2),
          ("unknown", 255))
    )


_CmgDSPCoreAdminState_Type.__name__ = "Integer32"
_CmgDSPCoreAdminState_Object = MibTableColumn
cmgDSPCoreAdminState = _CmgDSPCoreAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 6, 1, 4),
    _CmgDSPCoreAdminState_Type()
)
cmgDSPCoreAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDSPCoreAdminState.setStatus("current")


class _CmgDSPCoreStatus_Type(Integer32):
    """Custom type cmgDSPCoreStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("idle", 1),
          ("inUse", 2))
    )


_CmgDSPCoreStatus_Type.__name__ = "Integer32"
_CmgDSPCoreStatus_Object = MibTableColumn
cmgDSPCoreStatus = _CmgDSPCoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 6, 1, 5),
    _CmgDSPCoreStatus_Type()
)
cmgDSPCoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDSPCoreStatus.setStatus("current")


class _CmgDSPCoreDemandTest_Type(Integer32):
    """Custom type cmgDSPCoreDemandTest based on Integer32"""
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


_CmgDSPCoreDemandTest_Type.__name__ = "Integer32"
_CmgDSPCoreDemandTest_Object = MibTableColumn
cmgDSPCoreDemandTest = _CmgDSPCoreDemandTest_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 6, 1, 6),
    _CmgDSPCoreDemandTest_Type()
)
cmgDSPCoreDemandTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgDSPCoreDemandTest.setStatus("current")


class _CmgDSPCoreDemandTestResult_Type(Integer32):
    """Custom type cmgDSPCoreDemandTestResult based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("errorCode1", 1),
          ("errorCode2", 2),
          ("errorCode3", 3),
          ("errorCode4", 4),
          ("errorCode5", 5),
          ("errorCode6", 6),
          ("notResponding", 7),
          ("pass", 255))
    )


_CmgDSPCoreDemandTestResult_Type.__name__ = "Integer32"
_CmgDSPCoreDemandTestResult_Object = MibTableColumn
cmgDSPCoreDemandTestResult = _CmgDSPCoreDemandTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 6, 1, 7),
    _CmgDSPCoreDemandTestResult_Type()
)
cmgDSPCoreDemandTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDSPCoreDemandTestResult.setStatus("current")


class _CmgVoipEchoCancellerControl_Type(Integer32):
    """Custom type cmgVoipEchoCancellerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("fixedOn", 3),
          ("off", 2),
          ("on", 1))
    )


_CmgVoipEchoCancellerControl_Type.__name__ = "Integer32"
_CmgVoipEchoCancellerControl_Object = MibScalar
cmgVoipEchoCancellerControl = _CmgVoipEchoCancellerControl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 7),
    _CmgVoipEchoCancellerControl_Type()
)
cmgVoipEchoCancellerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipEchoCancellerControl.setStatus("current")


class _CmgVoipEchoCancellerConfig1_Type(Integer32):
    """Custom type cmgVoipEchoCancellerConfig1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmgVoipEchoCancellerConfig1_Type.__name__ = "Integer32"
_CmgVoipEchoCancellerConfig1_Object = MibScalar
cmgVoipEchoCancellerConfig1 = _CmgVoipEchoCancellerConfig1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 8),
    _CmgVoipEchoCancellerConfig1_Type()
)
cmgVoipEchoCancellerConfig1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipEchoCancellerConfig1.setStatus("current")


class _CmgVoipEchoCancellerConfig2_Type(Integer32):
    """Custom type cmgVoipEchoCancellerConfig2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmgVoipEchoCancellerConfig2_Type.__name__ = "Integer32"
_CmgVoipEchoCancellerConfig2_Object = MibScalar
cmgVoipEchoCancellerConfig2 = _CmgVoipEchoCancellerConfig2_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 9),
    _CmgVoipEchoCancellerConfig2_Type()
)
cmgVoipEchoCancellerConfig2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgVoipEchoCancellerConfig2.setStatus("current")
_CmgVoipTotalChannelsEnforcedByCM_Type = Integer32
_CmgVoipTotalChannelsEnforcedByCM_Object = MibScalar
cmgVoipTotalChannelsEnforcedByCM = _CmgVoipTotalChannelsEnforcedByCM_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 4, 10),
    _CmgVoipTotalChannelsEnforcedByCM_Type()
)
cmgVoipTotalChannelsEnforcedByCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgVoipTotalChannelsEnforcedByCM.setStatus("current")
_CmgTraps_ObjectIdentity = ObjectIdentity
cmgTraps = _CmgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5)
)
_CmgTrapManagerTable_Object = MibTable
cmgTrapManagerTable = _CmgTrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cmgTrapManagerTable.setStatus("current")
_CmgTrapManagerEntry_Object = MibTableRow
cmgTrapManagerEntry = _CmgTrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 1, 1)
)
cmgTrapManagerEntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgTrapManagerAddress"),
)
if mibBuilder.loadTexts:
    cmgTrapManagerEntry.setStatus("current")
_CmgTrapManagerAddress_Type = IpAddress
_CmgTrapManagerAddress_Object = MibTableColumn
cmgTrapManagerAddress = _CmgTrapManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 1, 1, 1),
    _CmgTrapManagerAddress_Type()
)
cmgTrapManagerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgTrapManagerAddress.setStatus("current")


class _CmgTrapManagerControl_Type(Integer32):
    """Custom type cmgTrapManagerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CmgTrapManagerControl_Type.__name__ = "Integer32"
_CmgTrapManagerControl_Object = MibTableColumn
cmgTrapManagerControl = _CmgTrapManagerControl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 1, 1, 3),
    _CmgTrapManagerControl_Type()
)
cmgTrapManagerControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgTrapManagerControl.setStatus("current")
_CmgTrapManagerMask_Type = Integer32
_CmgTrapManagerMask_Object = MibTableColumn
cmgTrapManagerMask = _CmgTrapManagerMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 1, 1, 4),
    _CmgTrapManagerMask_Type()
)
cmgTrapManagerMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgTrapManagerMask.setStatus("current")
_CmgTrapManagerRowStatus_Type = RowStatus
_CmgTrapManagerRowStatus_Object = MibTableColumn
cmgTrapManagerRowStatus = _CmgTrapManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 1, 1, 5),
    _CmgTrapManagerRowStatus_Type()
)
cmgTrapManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgTrapManagerRowStatus.setStatus("current")
_CmgTrapDefinitions_ObjectIdentity = ObjectIdentity
cmgTrapDefinitions = _CmgTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2)
)
_CmgTrapVariables_ObjectIdentity = ObjectIdentity
cmgTrapVariables = _CmgTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1)
)


class _CmgTrapLocation_Type(DisplayString):
    """Custom type cmgTrapLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmgTrapLocation_Type.__name__ = "DisplayString"
_CmgTrapLocation_Object = MibScalar
cmgTrapLocation = _CmgTrapLocation_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 1),
    _CmgTrapLocation_Type()
)
cmgTrapLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmgTrapLocation.setStatus("current")


class _CmgTrapOnBoard_Type(DisplayString):
    """Custom type cmgTrapOnBoard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CmgTrapOnBoard_Type.__name__ = "DisplayString"
_CmgTrapOnBoard_Object = MibScalar
cmgTrapOnBoard = _CmgTrapOnBoard_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 2),
    _CmgTrapOnBoard_Type()
)
cmgTrapOnBoard.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmgTrapOnBoard.setStatus("current")


class _CmgTrapSubsystem_Type(DisplayString):
    """Custom type cmgTrapSubsystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CmgTrapSubsystem_Type.__name__ = "DisplayString"
_CmgTrapSubsystem_Object = MibScalar
cmgTrapSubsystem = _CmgTrapSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 3),
    _CmgTrapSubsystem_Type()
)
cmgTrapSubsystem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmgTrapSubsystem.setStatus("current")


class _CmgTrapOnIccMissing_Type(Integer32):
    """Custom type cmgTrapOnIccMissing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmgTrapOnIccMissing_Type.__name__ = "Integer32"
_CmgTrapOnIccMissing_Object = MibScalar
cmgTrapOnIccMissing = _CmgTrapOnIccMissing_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 4),
    _CmgTrapOnIccMissing_Type()
)
cmgTrapOnIccMissing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgTrapOnIccMissing.setStatus("current")


class _CmgTrapModule_Type(DisplayString):
    """Custom type cmgTrapModule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmgTrapModule_Type.__name__ = "DisplayString"
_CmgTrapModule_Object = MibScalar
cmgTrapModule = _CmgTrapModule_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 5),
    _CmgTrapModule_Type()
)
cmgTrapModule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmgTrapModule.setStatus("current")
_CmgTrapSeverity_Type = CmgItuPerceivedSeverity
_CmgTrapSeverity_Object = MibScalar
cmgTrapSeverity = _CmgTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 6),
    _CmgTrapSeverity_Type()
)
cmgTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmgTrapSeverity.setStatus("current")


class _CmgProductId_Type(DisplayString):
    """Custom type cmgProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmgProductId_Type.__name__ = "DisplayString"
_CmgProductId_Object = MibScalar
cmgProductId = _CmgProductId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 7),
    _CmgProductId_Type()
)
cmgProductId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmgProductId.setStatus("current")
_CmgTrapAvailableTimeslots_Type = Integer32
_CmgTrapAvailableTimeslots_Object = MibScalar
cmgTrapAvailableTimeslots = _CmgTrapAvailableTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 8),
    _CmgTrapAvailableTimeslots_Type()
)
cmgTrapAvailableTimeslots.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmgTrapAvailableTimeslots.setStatus("current")
_CmgTrapInUseTimeslots_Type = Integer32
_CmgTrapInUseTimeslots_Object = MibScalar
cmgTrapInUseTimeslots = _CmgTrapInUseTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 9),
    _CmgTrapInUseTimeslots_Type()
)
cmgTrapInUseTimeslots.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmgTrapInUseTimeslots.setStatus("current")


class _CmgFipsErrorType_Type(Integer32):
    """Custom type cmgFipsErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cryptoTestError", 1),
          ("hashIntegrity", 3),
          ("prngFailure", 2))
    )


_CmgFipsErrorType_Type.__name__ = "Integer32"
_CmgFipsErrorType_Object = MibScalar
cmgFipsErrorType = _CmgFipsErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 1, 10),
    _CmgFipsErrorType_Type()
)
cmgFipsErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmgFipsErrorType.setStatus("current")
_CmgTrapTypes_ObjectIdentity = ObjectIdentity
cmgTrapTypes = _CmgTrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2)
)
_CmgTrapV3separator_ObjectIdentity = ObjectIdentity
cmgTrapV3separator = _CmgTrapV3separator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0)
)
_CmgContactClosures_ObjectIdentity = ObjectIdentity
cmgContactClosures = _CmgContactClosures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 6)
)
_CmgContactClosuresTable_Object = MibTable
cmgContactClosuresTable = _CmgContactClosuresTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cmgContactClosuresTable.setStatus("current")
_CmgContactClosuresEntry_Object = MibTableRow
cmgContactClosuresEntry = _CmgContactClosuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 6, 1, 1)
)
cmgContactClosuresEntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgCcModule"),
    (0, "G700-MG-MIB", "cmgCcPort"),
    (0, "G700-MG-MIB", "cmgCcRelay"),
)
if mibBuilder.loadTexts:
    cmgContactClosuresEntry.setStatus("current")


class _CmgCcModule_Type(Integer32):
    """Custom type cmgCcModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
    )


_CmgCcModule_Type.__name__ = "Integer32"
_CmgCcModule_Object = MibTableColumn
cmgCcModule = _CmgCcModule_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 6, 1, 1, 1),
    _CmgCcModule_Type()
)
cmgCcModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCcModule.setStatus("current")


class _CmgCcPort_Type(Integer32):
    """Custom type cmgCcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CmgCcPort_Type.__name__ = "Integer32"
_CmgCcPort_Object = MibTableColumn
cmgCcPort = _CmgCcPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 6, 1, 1, 2),
    _CmgCcPort_Type()
)
cmgCcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCcPort.setStatus("current")


class _CmgCcRelay_Type(Integer32):
    """Custom type cmgCcRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CmgCcRelay_Type.__name__ = "Integer32"
_CmgCcRelay_Object = MibTableColumn
cmgCcRelay = _CmgCcRelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 6, 1, 1, 3),
    _CmgCcRelay_Type()
)
cmgCcRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCcRelay.setStatus("current")


class _CmgCcAdminState_Type(Integer32):
    """Custom type cmgCcAdminState based on Integer32"""
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
        *(("auto", 1),
          ("manualOff", 3),
          ("manualTrigger", 2))
    )


_CmgCcAdminState_Type.__name__ = "Integer32"
_CmgCcAdminState_Object = MibTableColumn
cmgCcAdminState = _CmgCcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 6, 1, 1, 4),
    _CmgCcAdminState_Type()
)
cmgCcAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgCcAdminState.setStatus("current")


class _CmgCcPulseDuration_Type(Integer32):
    """Custom type cmgCcPulseDuration based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CmgCcPulseDuration_Type.__name__ = "Integer32"
_CmgCcPulseDuration_Object = MibTableColumn
cmgCcPulseDuration = _CmgCcPulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 6, 1, 1, 5),
    _CmgCcPulseDuration_Type()
)
cmgCcPulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgCcPulseDuration.setStatus("current")


class _CmgCcStatus_Type(Integer32):
    """Custom type cmgCcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("triggered", 1))
    )


_CmgCcStatus_Type.__name__ = "Integer32"
_CmgCcStatus_Object = MibTableColumn
cmgCcStatus = _CmgCcStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 6, 1, 1, 6),
    _CmgCcStatus_Type()
)
cmgCcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgCcStatus.setStatus("current")
_CmgETR_ObjectIdentity = ObjectIdentity
cmgETR = _CmgETR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 7)
)
_CmgETRTable_Object = MibTable
cmgETRTable = _CmgETRTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cmgETRTable.setStatus("current")
_CmgETREntry_Object = MibTableRow
cmgETREntry = _CmgETREntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 7, 1, 1)
)
cmgETREntry.setIndexNames(
    (0, "G700-MG-MIB", "cmgEtrModule"),
)
if mibBuilder.loadTexts:
    cmgETREntry.setStatus("current")


class _CmgEtrModule_Type(Integer32):
    """Custom type cmgEtrModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CmgEtrModule_Type.__name__ = "Integer32"
_CmgEtrModule_Object = MibTableColumn
cmgEtrModule = _CmgEtrModule_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 7, 1, 1, 1),
    _CmgEtrModule_Type()
)
cmgEtrModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgEtrModule.setStatus("current")


class _CmgEtrAdminState_Type(Integer32):
    """Custom type cmgEtrAdminState based on Integer32"""
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
        *(("auto", 1),
          ("off", 3),
          ("on", 2))
    )


_CmgEtrAdminState_Type.__name__ = "Integer32"
_CmgEtrAdminState_Object = MibTableColumn
cmgEtrAdminState = _CmgEtrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 7, 1, 1, 2),
    _CmgEtrAdminState_Type()
)
cmgEtrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgEtrAdminState.setStatus("current")


class _CmgEtrNumberOfPairs_Type(Integer32):
    """Custom type cmgEtrNumberOfPairs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CmgEtrNumberOfPairs_Type.__name__ = "Integer32"
_CmgEtrNumberOfPairs_Object = MibTableColumn
cmgEtrNumberOfPairs = _CmgEtrNumberOfPairs_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 7, 1, 1, 3),
    _CmgEtrNumberOfPairs_Type()
)
cmgEtrNumberOfPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgEtrNumberOfPairs.setStatus("current")


class _CmgEtrStatus_Type(Integer32):
    """Custom type cmgEtrStatus based on Integer32"""
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


_CmgEtrStatus_Type.__name__ = "Integer32"
_CmgEtrStatus_Object = MibTableColumn
cmgEtrStatus = _CmgEtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 7, 1, 1, 4),
    _CmgEtrStatus_Type()
)
cmgEtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgEtrStatus.setStatus("current")


class _CmgEtrCurrentLoopDetect_Type(OctetString):
    """Custom type cmgEtrCurrentLoopDetect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CmgEtrCurrentLoopDetect_Type.__name__ = "OctetString"
_CmgEtrCurrentLoopDetect_Object = MibTableColumn
cmgEtrCurrentLoopDetect = _CmgEtrCurrentLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 7, 1, 1, 5),
    _CmgEtrCurrentLoopDetect_Type()
)
cmgEtrCurrentLoopDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgEtrCurrentLoopDetect.setStatus("current")
_CmgDynamicCAC_ObjectIdentity = ObjectIdentity
cmgDynamicCAC = _CmgDynamicCAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 8)
)


class _CmgDynCacStatus_Type(Integer32):
    """Custom type cmgDynCacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("armedNotConfigured", 4),
          ("notArmed", 3),
          ("notConfigured", 2),
          ("notSupported", 255))
    )


_CmgDynCacStatus_Type.__name__ = "Integer32"
_CmgDynCacStatus_Object = MibScalar
cmgDynCacStatus = _CmgDynCacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 8, 1),
    _CmgDynCacStatus_Type()
)
cmgDynCacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDynCacStatus.setStatus("current")
_CmgDynCacRBBL_Type = Integer32
_CmgDynCacRBBL_Object = MibScalar
cmgDynCacRBBL = _CmgDynCacRBBL_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 8, 2),
    _CmgDynCacRBBL_Type()
)
cmgDynCacRBBL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDynCacRBBL.setStatus("current")
_CmgDynCacLastUpdate_Type = TimeTicks
_CmgDynCacLastUpdate_Object = MibScalar
cmgDynCacLastUpdate = _CmgDynCacLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 8, 3),
    _CmgDynCacLastUpdate_Type()
)
cmgDynCacLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgDynCacLastUpdate.setStatus("current")
_CmgSLAMonitor_ObjectIdentity = ObjectIdentity
cmgSLAMonitor = _CmgSLAMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 9)
)


class _CmgSLAMonitorState_Type(Integer32):
    """Custom type cmgSLAMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CmgSLAMonitorState_Type.__name__ = "Integer32"
_CmgSLAMonitorState_Object = MibScalar
cmgSLAMonitorState = _CmgSLAMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 9, 1),
    _CmgSLAMonitorState_Type()
)
cmgSLAMonitorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgSLAMonitorState.setStatus("current")
_CmgSLAMonitorServerInetAddressType_Type = InetAddressType
_CmgSLAMonitorServerInetAddressType_Object = MibScalar
cmgSLAMonitorServerInetAddressType = _CmgSLAMonitorServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 9, 2),
    _CmgSLAMonitorServerInetAddressType_Type()
)
cmgSLAMonitorServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgSLAMonitorServerInetAddressType.setStatus("current")
_CmgSLAMonitorServerInetAddress_Type = InetAddress
_CmgSLAMonitorServerInetAddress_Object = MibScalar
cmgSLAMonitorServerInetAddress = _CmgSLAMonitorServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 9, 3),
    _CmgSLAMonitorServerInetAddress_Type()
)
cmgSLAMonitorServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgSLAMonitorServerInetAddress.setStatus("current")


class _CmgSLAMonitorServerPort_Type(Integer32):
    """Custom type cmgSLAMonitorServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmgSLAMonitorServerPort_Type.__name__ = "Integer32"
_CmgSLAMonitorServerPort_Object = MibScalar
cmgSLAMonitorServerPort = _CmgSLAMonitorServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 9, 4),
    _CmgSLAMonitorServerPort_Type()
)
cmgSLAMonitorServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgSLAMonitorServerPort.setStatus("current")


class _CmgSLAMonitorPacketCaptureMode_Type(Integer32):
    """Custom type cmgSLAMonitorPacketCaptureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("none", 0),
          ("withoutPayload", 1))
    )


_CmgSLAMonitorPacketCaptureMode_Type.__name__ = "Integer32"
_CmgSLAMonitorPacketCaptureMode_Object = MibScalar
cmgSLAMonitorPacketCaptureMode = _CmgSLAMonitorPacketCaptureMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 9, 10),
    _CmgSLAMonitorPacketCaptureMode_Type()
)
cmgSLAMonitorPacketCaptureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgSLAMonitorPacketCaptureMode.setStatus("current")


class _CmgSLAMonitorVersion_Type(DisplayString):
    """Custom type cmgSLAMonitorVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmgSLAMonitorVersion_Type.__name__ = "DisplayString"
_CmgSLAMonitorVersion_Object = MibScalar
cmgSLAMonitorVersion = _CmgSLAMonitorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 9, 99),
    _CmgSLAMonitorVersion_Type()
)
cmgSLAMonitorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgSLAMonitorVersion.setStatus("current")

# Managed Objects groups


# Notification objects

cmgMultipleFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 2)
)
cmgMultipleFanFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgMultipleFanFault.setStatus(
        "current"
    )

cmgMultipleFanClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 3)
)
cmgMultipleFanClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgMultipleFanClear.setStatus(
        "current"
    )

cmgPsuFanBriefFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 4)
)
cmgPsuFanBriefFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgPsuFanBriefFault.setStatus(
        "current"
    )

cmgPsuFanBriefClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 5)
)
cmgPsuFanBriefClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgPsuFanBriefClear.setStatus(
        "current"
    )

cmgPsuFanProlongedFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 6)
)
cmgPsuFanProlongedFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgPsuFanProlongedFault.setStatus(
        "current"
    )

cmgPsuFanProlongedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 7)
)
cmgPsuFanProlongedClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgPsuFanProlongedClear.setStatus(
        "current"
    )

cmgCpuTempWarningFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 10)
)
cmgCpuTempWarningFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgCpuTemp"),
        ("G700-MG-MIB", "cmgCpuTempWarningThresh"),
        ("G700-MG-MIB", "cmgCpuTempShutdownThresh"))
)
if mibBuilder.loadTexts:
    cmgCpuTempWarningFault.setStatus(
        "current"
    )

cmgCpuTempWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 11)
)
cmgCpuTempWarningClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgCpuTemp"),
        ("G700-MG-MIB", "cmgCpuTempWarningThresh"),
        ("G700-MG-MIB", "cmgCpuTempShutdownThresh"))
)
if mibBuilder.loadTexts:
    cmgCpuTempWarningClear.setStatus(
        "current"
    )

cmgDspTempWarningFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 12)
)
cmgDspTempWarningFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgDspTemp"),
        ("G700-MG-MIB", "cmgDspTempWarningThresh"),
        ("G700-MG-MIB", "cmgDspTempShutdownThresh"))
)
if mibBuilder.loadTexts:
    cmgDspTempWarningFault.setStatus(
        "current"
    )

cmgDspTempWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 13)
)
cmgDspTempWarningClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgDspTemp"),
        ("G700-MG-MIB", "cmgDspTempWarningThresh"),
        ("G700-MG-MIB", "cmgDspTempShutdownThresh"))
)
if mibBuilder.loadTexts:
    cmgDspTempWarningClear.setStatus(
        "current"
    )

cmgTempShutdownFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 14)
)
cmgTempShutdownFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgCpuTemp"),
        ("G700-MG-MIB", "cmgCpuTempShutdownThresh"),
        ("G700-MG-MIB", "cmgDspTemp"),
        ("G700-MG-MIB", "cmgDspTempShutdownThresh"))
)
if mibBuilder.loadTexts:
    cmgTempShutdownFault.setStatus(
        "current"
    )

cmgMgpPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 16)
)
cmgMgpPowerFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPowerMgProcessor"))
)
if mibBuilder.loadTexts:
    cmgMgpPowerFault.setStatus(
        "current"
    )

cmgMgpPowerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 17)
)
cmgMgpPowerClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPowerMgProcessor"))
)
if mibBuilder.loadTexts:
    cmgMgpPowerClear.setStatus(
        "current"
    )

cmgMediaModulePowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 18)
)
cmgMediaModulePowerFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPowerMediaModules"))
)
if mibBuilder.loadTexts:
    cmgMediaModulePowerFault.setStatus(
        "current"
    )

cmgMediaModulePowerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 19)
)
cmgMediaModulePowerClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPowerMediaModules"))
)
if mibBuilder.loadTexts:
    cmgMediaModulePowerClear.setStatus(
        "current"
    )

cmgVoipPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 20)
)
cmgVoipPowerFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPowerVoipComplex"))
)
if mibBuilder.loadTexts:
    cmgVoipPowerFault.setStatus(
        "current"
    )

cmgVoipPowerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 21)
)
cmgVoipPowerClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPowerVoipComplex"))
)
if mibBuilder.loadTexts:
    cmgVoipPowerClear.setStatus(
        "current"
    )

cmgDspPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 22)
)
cmgDspPowerFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPowerDsp"))
)
if mibBuilder.loadTexts:
    cmgDspPowerFault.setStatus(
        "current"
    )

cmgDspPowerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 23)
)
cmgDspPowerClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPowerDsp"))
)
if mibBuilder.loadTexts:
    cmgDspPowerClear.setStatus(
        "current"
    )

cmg8260PowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 24)
)
cmg8260PowerFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPower8260"))
)
if mibBuilder.loadTexts:
    cmg8260PowerFault.setStatus(
        "current"
    )

cmg8260PowerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 25)
)
cmg8260PowerClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPower8260"))
)
if mibBuilder.loadTexts:
    cmg8260PowerClear.setStatus(
        "current"
    )

cmgAuxPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 26)
)
cmgAuxPowerFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgAuxPowerFault.setStatus(
        "current"
    )

cmgAuxPowerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 27)
)
cmgAuxPowerClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgAuxPowerClear.setStatus(
        "current"
    )

cmgFanPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 28)
)
cmgFanPowerFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgFanPowerFault.setStatus(
        "current"
    )

cmgFanPowerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 29)
)
cmgFanPowerClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"))
)
if mibBuilder.loadTexts:
    cmgFanPowerClear.setStatus(
        "current"
    )

cmgSyncSignalFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 30)
)
cmgSyncSignalFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPrimaryClockSource"),
        ("G700-MG-MIB", "cmgSecondaryClockSource"),
        ("G700-MG-MIB", "cmgActiveClockSource"))
)
if mibBuilder.loadTexts:
    cmgSyncSignalFault.setStatus(
        "current"
    )

cmgSyncSignalClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 31)
)
cmgSyncSignalClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPrimaryClockSource"),
        ("G700-MG-MIB", "cmgSecondaryClockSource"),
        ("G700-MG-MIB", "cmgActiveClockSource"))
)
if mibBuilder.loadTexts:
    cmgSyncSignalClear.setStatus(
        "current"
    )

cmgVoipHardwareFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 32)
)
cmgVoipHardwareFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"))
)
if mibBuilder.loadTexts:
    cmgVoipHardwareFault.setStatus(
        "current"
    )

cmgVoipHardwareClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 33)
)
cmgVoipHardwareClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"))
)
if mibBuilder.loadTexts:
    cmgVoipHardwareClear.setStatus(
        "current"
    )

cmgSyncSignalWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 34)
)
cmgSyncSignalWarn.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPrimaryClockSource"),
        ("G700-MG-MIB", "cmgSecondaryClockSource"),
        ("G700-MG-MIB", "cmgActiveClockSource"))
)
if mibBuilder.loadTexts:
    cmgSyncSignalWarn.setStatus(
        "current"
    )

cmgSyncWarnClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 35)
)
cmgSyncWarnClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPrimaryClockSource"),
        ("G700-MG-MIB", "cmgSecondaryClockSource"),
        ("G700-MG-MIB", "cmgActiveClockSource"))
)
if mibBuilder.loadTexts:
    cmgSyncWarnClear.setStatus(
        "current"
    )

cmgSyncSignalExcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 36)
)
cmgSyncSignalExcess.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPrimaryClockSource"),
        ("G700-MG-MIB", "cmgSecondaryClockSource"),
        ("G700-MG-MIB", "cmgActiveClockSource"))
)
if mibBuilder.loadTexts:
    cmgSyncSignalExcess.setStatus(
        "current"
    )

cmgSyncExcessClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 37)
)
cmgSyncExcessClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgHardwareFaultMask"),
        ("G700-MG-MIB", "cmgPrimaryClockSource"),
        ("G700-MG-MIB", "cmgSecondaryClockSource"),
        ("G700-MG-MIB", "cmgActiveClockSource"))
)
if mibBuilder.loadTexts:
    cmgSyncExcessClear.setStatus(
        "current"
    )

cmgVoipCoreFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 38)
)
cmgVoipCoreFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"))
)
if mibBuilder.loadTexts:
    cmgVoipCoreFault.setStatus(
        "current"
    )

cmgVoipCoreClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 39)
)
cmgVoipCoreClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"))
)
if mibBuilder.loadTexts:
    cmgVoipCoreClear.setStatus(
        "current"
    )

cmgModuleRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 50)
)
cmgModuleRemove.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapModule"))
)
if mibBuilder.loadTexts:
    cmgModuleRemove.setStatus(
        "current"
    )

cmgModuleInsertFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 52)
)
cmgModuleInsertFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgModuleFaultMask"),
        ("G700-MG-MIB", "cmgTrapModule"))
)
if mibBuilder.loadTexts:
    cmgModuleInsertFault.setStatus(
        "current"
    )

cmgModuleInsertSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 53)
)
cmgModuleInsertSuccess.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapModule"))
)
if mibBuilder.loadTexts:
    cmgModuleInsertSuccess.setStatus(
        "current"
    )

cmgMgBusyout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 54)
)
cmgMgBusyout.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgMgBusyout.setStatus(
        "current"
    )

cmgMgRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 55)
)
cmgMgRelease.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgMgRelease.setStatus(
        "current"
    )

cmgUnsupportedMmEnrolement = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 56)
)
cmgUnsupportedMmEnrolement.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgModuleSlot"),
        ("G700-MG-MIB", "cmgModuleType"),
        ("G700-MG-MIB", "cmgModuleName"))
)
if mibBuilder.loadTexts:
    cmgUnsupportedMmEnrolement.setStatus(
        "current"
    )

cmgDataModuleAwohConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 57)
)
cmgDataModuleAwohConflict.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgModuleSlot"),
        ("G700-MG-MIB", "cmgModuleType"),
        ("G700-MG-MIB", "cmgModuleName"))
)
if mibBuilder.loadTexts:
    cmgDataModuleAwohConflict.setStatus(
        "current"
    )

cmgFirmwareDownloadBegun = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 70)
)
cmgFirmwareDownloadBegun.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("LOAD-MIB", "genAppFileId"),
        ("LOAD-MIB", "genAppFileName"),
        ("LOAD-MIB", "genAppFileVersionNumber"),
        ("G700-MG-MIB", "cmgProductId"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgFirmwareDownloadBegun.setStatus(
        "current"
    )

cmgFirmwareDownloadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 71)
)
cmgFirmwareDownloadSuccess.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("LOAD-MIB", "genAppFileId"),
        ("LOAD-MIB", "genAppFileName"),
        ("LOAD-MIB", "genAppFileVersionNumber"))
)
if mibBuilder.loadTexts:
    cmgFirmwareDownloadSuccess.setStatus(
        "current"
    )

cmgRegistrationSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 73)
)
cmgRegistrationSuccess.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgActiveControllerAddress"))
)
if mibBuilder.loadTexts:
    cmgRegistrationSuccess.setStatus(
        "current"
    )

cmgMgManualReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 74)
)
cmgMgManualReset.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgMgManualReset.setStatus(
        "current"
    )

cmgModuleManualReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 75)
)
cmgModuleManualReset.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgModuleManualReset.setStatus(
        "current"
    )

cmgVoipManualReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 76)
)
cmgVoipManualReset.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgVoipManualReset.setStatus(
        "current"
    )

cmgDsuManualReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 77)
)
cmgDsuManualReset.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuManualReset.setStatus(
        "obsolete"
    )

cmgConfigUploadBegun = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 78)
)
cmgConfigUploadBegun.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgConfigUploadBegun.setStatus(
        "current"
    )

cmgConfigUploadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 79)
)
cmgConfigUploadSuccess.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgConfigUploadSuccess.setStatus(
        "current"
    )

cmgMemoryFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 90)
)
cmgMemoryFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgMemoryFault.setStatus(
        "current"
    )

cmgMemoryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 91)
)
cmgMemoryClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgMemoryClear.setStatus(
        "current"
    )

cmgDhcpRequestFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 92)
)
cmgDhcpRequestFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgDhcpRequestFault.setStatus(
        "current"
    )

cmgDhcpRequestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 93)
)
cmgDhcpRequestClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgDhcpRequestClear.setStatus(
        "current"
    )

cmgFirmwareDownloadFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 94)
)
cmgFirmwareDownloadFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"),
        ("LOAD-MIB", "genAppFileId"),
        ("LOAD-MIB", "genAppFileName"),
        ("LOAD-MIB", "genAppFileVersionNumber"),
        ("LOAD-MIB", "genOpLastFailureIndex"))
)
if mibBuilder.loadTexts:
    cmgFirmwareDownloadFault.setStatus(
        "current"
    )

cmgProcessRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 96)
)
cmgProcessRestart.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgProcessRestart.setStatus(
        "current"
    )

cmgProcessRestartClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 97)
)
cmgProcessRestartClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgProcessRestartClear.setStatus(
        "current"
    )

cmgIccMissingFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 98)
)
cmgIccMissingFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgIccMissingFault.setStatus(
        "current"
    )

cmgIccMissingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 99)
)
cmgIccMissingClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgIccMissingClear.setStatus(
        "current"
    )

cmgIccAutoReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 100)
)
cmgIccAutoReset.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgIccAutoReset.setStatus(
        "current"
    )

cmgIccAutoResetClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 101)
)
cmgIccAutoResetClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgIccAutoResetClear.setStatus(
        "current"
    )

cmgPrimaryControllerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 102)
)
cmgPrimaryControllerFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"),
        ("G700-MG-MIB", "cmgUseDhcpForMgcList"))
)
if mibBuilder.loadTexts:
    cmgPrimaryControllerFault.setStatus(
        "current"
    )

cmgPrimaryControllerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 103)
)
cmgPrimaryControllerClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"),
        ("G700-MG-MIB", "cmgUseDhcpForMgcList"))
)
if mibBuilder.loadTexts:
    cmgPrimaryControllerClear.setStatus(
        "current"
    )

cmgNoControllerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 104)
)
cmgNoControllerFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"),
        ("G700-MG-MIB", "cmgUseDhcpForMgcList"))
)
if mibBuilder.loadTexts:
    cmgNoControllerFault.setStatus(
        "current"
    )

cmgNoControllerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 105)
)
cmgNoControllerClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"),
        ("G700-MG-MIB", "cmgUseDhcpForMgcList"))
)
if mibBuilder.loadTexts:
    cmgNoControllerClear.setStatus(
        "current"
    )

cmgRegistrationFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 106)
)
cmgRegistrationFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"),
        ("G700-MG-MIB", "cmgActiveControllerAddress"))
)
if mibBuilder.loadTexts:
    cmgRegistrationFault.setStatus(
        "current"
    )

cmgH248LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 108)
)
cmgH248LinkDown.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgH248LinkDown.setStatus(
        "current"
    )

cmgH248LinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 109)
)
cmgH248LinkUp.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgH248LinkUp.setStatus(
        "current"
    )

cmgTestFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 110)
)
cmgTestFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgTestFault.setStatus(
        "current"
    )

cmgTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 111)
)
cmgTestClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgTestClear.setStatus(
        "current"
    )

cmgTestThresholdFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 112)
)
cmgTestThresholdFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgTestThresholdFault.setStatus(
        "current"
    )

cmgTestThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 113)
)
cmgTestThresholdClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgTestThresholdClear.setStatus(
        "current"
    )

cmgMgAutoReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 114)
)
cmgMgAutoReset.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"))
)
if mibBuilder.loadTexts:
    cmgMgAutoReset.setStatus(
        "current"
    )

cmgModuleAutoReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 116)
)
cmgModuleAutoReset.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgModuleFaultMask"))
)
if mibBuilder.loadTexts:
    cmgModuleAutoReset.setStatus(
        "current"
    )

cmgModuleAutoResetClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 117)
)
cmgModuleAutoResetClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgModuleFaultMask"))
)
if mibBuilder.loadTexts:
    cmgModuleAutoResetClear.setStatus(
        "current"
    )

cmgModulePostFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 118)
)
cmgModulePostFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgModuleFaultMask"))
)
if mibBuilder.loadTexts:
    cmgModulePostFault.setStatus(
        "current"
    )

cmgModulePostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 119)
)
cmgModulePostClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgModuleFaultMask"))
)
if mibBuilder.loadTexts:
    cmgModulePostClear.setStatus(
        "current"
    )

cmgModuleParameterFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 120)
)
cmgModuleParameterFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgModuleFaultMask"))
)
if mibBuilder.loadTexts:
    cmgModuleParameterFault.setStatus(
        "current"
    )

cmgModuleParameterClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 121)
)
cmgModuleParameterClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgModuleFaultMask"))
)
if mibBuilder.loadTexts:
    cmgModuleParameterClear.setStatus(
        "current"
    )

cmgConfigUploadFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 122)
)
cmgConfigUploadFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"),
        ("LOAD-MIB", "genOpLastFailureIndex"))
)
if mibBuilder.loadTexts:
    cmgConfigUploadFault.setStatus(
        "current"
    )

cmgVoipOccFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 124)
)
cmgVoipOccFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"),
        ("G700-MG-MIB", "cmgVoipChannelsInUse"),
        ("G700-MG-MIB", "cmgVoipTotalChannels"))
)
if mibBuilder.loadTexts:
    cmgVoipOccFault.setStatus(
        "current"
    )

cmgVoipOccClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 125)
)
cmgVoipOccClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"),
        ("G700-MG-MIB", "cmgVoipChannelsInUse"),
        ("G700-MG-MIB", "cmgVoipTotalChannels"))
)
if mibBuilder.loadTexts:
    cmgVoipOccClear.setStatus(
        "current"
    )

cmgVoipAvgOccFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 126)
)
cmgVoipAvgOccFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"),
        ("G700-MG-MIB", "cmgVoipAverageOccupancy"))
)
if mibBuilder.loadTexts:
    cmgVoipAvgOccFault.setStatus(
        "current"
    )

cmgVoipAvgOccClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 127)
)
cmgVoipAvgOccClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"),
        ("G700-MG-MIB", "cmgVoipAverageOccupancy"))
)
if mibBuilder.loadTexts:
    cmgVoipAvgOccClear.setStatus(
        "current"
    )

cmgVoipAutoReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 128)
)
cmgVoipAutoReset.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"))
)
if mibBuilder.loadTexts:
    cmgVoipAutoReset.setStatus(
        "current"
    )

cmgVoipAutoResetClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 129)
)
cmgVoipAutoResetClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"))
)
if mibBuilder.loadTexts:
    cmgVoipAutoResetClear.setStatus(
        "current"
    )

cmgDsuFpgaConfigureFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 130)
)
cmgDsuFpgaConfigureFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuFpgaConfigureFault.setStatus(
        "obsolete"
    )

cmgDsuFpgaConfigureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 131)
)
cmgDsuFpgaConfigureClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuFpgaConfigureClear.setStatus(
        "obsolete"
    )

cmgDsuAutoReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 132)
)
cmgDsuAutoReset.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuAutoReset.setStatus(
        "obsolete"
    )

cmgDsuAutoResetClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 133)
)
cmgDsuAutoResetClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuAutoResetClear.setStatus(
        "obsolete"
    )

cmgDsuDteDtrFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 134)
)
cmgDsuDteDtrFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuDteDtrFault.setStatus(
        "obsolete"
    )

cmgDsuDteDtrClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 135)
)
cmgDsuDteDtrClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuDteDtrClear.setStatus(
        "obsolete"
    )

cmgDsuDteRtsFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 136)
)
cmgDsuDteRtsFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuDteRtsFault.setStatus(
        "obsolete"
    )

cmgDsuDteRtsClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 137)
)
cmgDsuDteRtsClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuDteRtsClear.setStatus(
        "obsolete"
    )

cmgDsuTxDFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 138)
)
cmgDsuTxDFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuTxDFault.setStatus(
        "obsolete"
    )

cmgDsuTxDClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 139)
)
cmgDsuTxDClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuTxDClear.setStatus(
        "obsolete"
    )

cmgDsuRxDFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 140)
)
cmgDsuRxDFailure.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuRxDFailure.setStatus(
        "obsolete"
    )

cmgDsuRxDClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 141)
)
cmgDsuRxDClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgDsuRxDClear.setStatus(
        "obsolete"
    )

cmgVoipIpConfigFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 142)
)
cmgVoipIpConfigFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"),
        ("G700-MG-MIB", "cmgVoipCurrentIpAddress"))
)
if mibBuilder.loadTexts:
    cmgVoipIpConfigFault.setStatus(
        "current"
    )

cmgVoipIpConfigClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 143)
)
cmgVoipIpConfigClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgVoipFaultMask"),
        ("G700-MG-MIB", "cmgVoipCurrentIpAddress"))
)
if mibBuilder.loadTexts:
    cmgVoipIpConfigClear.setStatus(
        "current"
    )

cmgConfigDownloadFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 144)
)
cmgConfigDownloadFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"),
        ("LOAD-MIB", "genOpLastFailureIndex"))
)
if mibBuilder.loadTexts:
    cmgConfigDownloadFault.setStatus(
        "current"
    )

cmgConfigDownloadBegun = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 145)
)
cmgConfigDownloadBegun.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgConfigDownloadBegun.setStatus(
        "current"
    )

cmgConfigDownloadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 146)
)
cmgConfigDownloadSuccess.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"))
)
if mibBuilder.loadTexts:
    cmgConfigDownloadSuccess.setStatus(
        "current"
    )

cmgTimeslotOccupancyFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 147)
)
cmgTimeslotOccupancyFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapAvailableTimeslots"),
        ("G700-MG-MIB", "cmgTrapInUseTimeslots"))
)
if mibBuilder.loadTexts:
    cmgTimeslotOccupancyFault.setStatus(
        "current"
    )

cmgTimeslotOccupancyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 148)
)
cmgTimeslotOccupancyClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapAvailableTimeslots"),
        ("G700-MG-MIB", "cmgTrapInUseTimeslots"))
)
if mibBuilder.loadTexts:
    cmgTimeslotOccupancyClear.setStatus(
        "current"
    )

cmgTimeslotAvailabilityFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 149)
)
cmgTimeslotAvailabilityFault.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapAvailableTimeslots"),
        ("G700-MG-MIB", "cmgTrapInUseTimeslots"))
)
if mibBuilder.loadTexts:
    cmgTimeslotAvailabilityFault.setStatus(
        "current"
    )

cmgTimeslotAvailabilityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 150)
)
cmgTimeslotAvailabilityClear.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapAvailableTimeslots"),
        ("G700-MG-MIB", "cmgTrapInUseTimeslots"))
)
if mibBuilder.loadTexts:
    cmgTimeslotAvailabilityClear.setStatus(
        "current"
    )

cmgRegistrationSuccessInetAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 151)
)
cmgRegistrationSuccessInetAddress.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgActiveControllerInetAddressType"),
        ("G700-MG-MIB", "cmgActiveControllerInetAddress"),
        ("G700-MG-MIB", "cmgProductId"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgRegistrationSuccessInetAddress.setStatus(
        "current"
    )

cmgRegistrationFaultInetAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 152)
)
cmgRegistrationFaultInetAddress.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgMgpFaultMask"),
        ("G700-MG-MIB", "cmgActiveControllerInetAddressType"),
        ("G700-MG-MIB", "cmgActiveControllerInetAddress"),
        ("G700-MG-MIB", "cmgProductId"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgRegistrationFaultInetAddress.setStatus(
        "current"
    )

cmgDs1Layer2Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 153)
)
cmgDs1Layer2Down.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapModule"))
)
if mibBuilder.loadTexts:
    cmgDs1Layer2Down.setStatus(
        "current"
    )

cmgDs1Layer2Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 154)
)
cmgDs1Layer2Up.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapModule"))
)
if mibBuilder.loadTexts:
    cmgDs1Layer2Up.setStatus(
        "current"
    )

cmgFipsErrorMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 155)
)
cmgFipsErrorMode.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapModule"),
        ("G700-MG-MIB", "cmgFipsErrorType"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgFipsErrorMode.setStatus(
        "current"
    )

cmgCertErrorCertRevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 156)
)
cmgCertErrorCertRevoked.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgCertErrorCertRevoked.setStatus(
        "current"
    )

cmgCrlAccessDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 157)
)
cmgCrlAccessDenied.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgCrlAccessDenied.setStatus(
        "current"
    )

cmgCrlFileSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 158)
)
cmgCrlFileSize.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgCrlFileSize.setStatus(
        "current"
    )

cmgCertErrorCertExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 159)
)
cmgCertErrorCertExpired.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgCertErrorCertExpired.setStatus(
        "current"
    )

cmgCertErrorNearExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 160)
)
cmgCertErrorNearExpiry.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgCertErrorNearExpiry.setStatus(
        "current"
    )

cmgCertErrorIdAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 0, 161)
)
cmgCertErrorIdAuthentication.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("G700-MG-MIB", "cmgTrapSeverity"))
)
if mibBuilder.loadTexts:
    cmgCertErrorIdAuthentication.setStatus(
        "current"
    )

cmgFirmwareDownloadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 9, 1, 5, 2, 2, 95)
)
cmgFirmwareDownloadWarning.setObjects(
      *(("G700-MG-MIB", "cmgTrapSubsystem"),
        ("G700-MG-MIB", "cmgTrapOnBoard"),
        ("G700-MG-MIB", "cmgTrapLocation"),
        ("LOAD-MIB", "genAppFileId"),
        ("LOAD-MIB", "genAppFileName"),
        ("LOAD-MIB", "genAppFileVersionNumber"),
        ("LOAD-MIB", "genOpLastWarningDisplay"))
)
if mibBuilder.loadTexts:
    cmgFirmwareDownloadWarning.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G700-MG-MIB",
    **{"CmgItuPerceivedSeverity": CmgItuPerceivedSeverity,
       "CmgModuleSlot": CmgModuleSlot,
       "avaya": avaya,
       "products": products,
       "g700MediaGateway": g700MediaGateway,
       "mibs": mibs,
       "g700MediaGatewayMIB": g700MediaGatewayMIB,
       "cmgmib": cmgmib,
       "cmgChassis": cmgChassis,
       "cmgHWType": cmgHWType,
       "cmgModelNumber": cmgModelNumber,
       "cmgDescription": cmgDescription,
       "cmgSerialNumber": cmgSerialNumber,
       "cmgHWVintage": cmgHWVintage,
       "cmgHWSuffix": cmgHWSuffix,
       "cmgStackPosition": cmgStackPosition,
       "cmgModuleList": cmgModuleList,
       "cmgReset": cmgReset,
       "cmgHardware": cmgHardware,
       "cmgCpuTemp": cmgCpuTemp,
       "cmgCpuTempWarningThresh": cmgCpuTempWarningThresh,
       "cmgCpuTempShutdownThresh": cmgCpuTempShutdownThresh,
       "cmgDspTemp": cmgDspTemp,
       "cmgDspTempWarningThresh": cmgDspTempWarningThresh,
       "cmgDspTempShutdownThresh": cmgDspTempShutdownThresh,
       "cmgPowerMgProcessor": cmgPowerMgProcessor,
       "cmgPowerMediaModules": cmgPowerMediaModules,
       "cmgPowerVoipComplex": cmgPowerVoipComplex,
       "cmgPowerDsp": cmgPowerDsp,
       "cmgPower8260": cmgPower8260,
       "cmgHardwareFaultMask": cmgHardwareFaultMask,
       "cmgHardwareStatusMask": cmgHardwareStatusMask,
       "cmgHardwareFanLowSpeedLevel": cmgHardwareFanLowSpeedLevel,
       "cmgModules": cmgModules,
       "cmgModuleTable": cmgModuleTable,
       "cmgModuleEntry": cmgModuleEntry,
       "cmgModuleSlot": cmgModuleSlot,
       "cmgModuleType": cmgModuleType,
       "cmgModuleDescription": cmgModuleDescription,
       "cmgModuleName": cmgModuleName,
       "cmgModuleSerialNumber": cmgModuleSerialNumber,
       "cmgModuleHWVintage": cmgModuleHWVintage,
       "cmgModuleHWSuffix": cmgModuleHWSuffix,
       "cmgModuleFWVersion": cmgModuleFWVersion,
       "cmgModuleNumberOfPorts": cmgModuleNumberOfPorts,
       "cmgModuleFaultMask": cmgModuleFaultMask,
       "cmgModuleStatusMask": cmgModuleStatusMask,
       "cmgModuleReset": cmgModuleReset,
       "cmgModuleNumberOfChannels": cmgModuleNumberOfChannels,
       "cmgDsu": cmgDsu,
       "cmgDsuConfigTable": cmgDsuConfigTable,
       "cmgDsuConfigEntry": cmgDsuConfigEntry,
       "cmgDsuSlot": cmgDsuSlot,
       "cmgDsuPort": cmgDsuPort,
       "cmgDsuPortEnable": cmgDsuPortEnable,
       "cmgDsuDataFormat": cmgDsuDataFormat,
       "cmgDsuFlowControl": cmgDsuFlowControl,
       "cmgDsuYellowAlarmAction": cmgDsuYellowAlarmAction,
       "cmgDsuReceiveClock": cmgDsuReceiveClock,
       "cmgDsuInvertTxC": cmgDsuInvertTxC,
       "cmgDsuInvertRxC": cmgDsuInvertRxC,
       "cmgDsuInvertTxD": cmgDsuInvertTxD,
       "cmgDsuInvertRxD": cmgDsuInvertRxD,
       "cmgDsuPortInitiatedLoopback": cmgDsuPortInitiatedLoopback,
       "cmgDsuNetworkInitiatedLoopback": cmgDsuNetworkInitiatedLoopback,
       "cmgDsuChannelAssignments": cmgDsuChannelAssignments,
       "cmgDsuDataRate": cmgDsuDataRate,
       "cmgDsuPortStatusTable": cmgDsuPortStatusTable,
       "cmgDsuPortStatusEntry": cmgDsuPortStatusEntry,
       "cmgDsuRTS": cmgDsuRTS,
       "cmgDsuDTR": cmgDsuDTR,
       "cmgDsuLL": cmgDsuLL,
       "cmgDsuRL": cmgDsuRL,
       "cmgDsuRLSD": cmgDsuRLSD,
       "cmgDsuCTS": cmgDsuCTS,
       "cmgDsuDSR": cmgDsuDSR,
       "cmgDsuRing": cmgDsuRing,
       "cmgDsuTestMode": cmgDsuTestMode,
       "cmgDsuTxD": cmgDsuTxD,
       "cmgDsuRxD": cmgDsuRxD,
       "cmgDsuFaultMask": cmgDsuFaultMask,
       "cmgDsuStatusMask": cmgDsuStatusMask,
       "cmgDsuTestTable": cmgDsuTestTable,
       "cmgDsuTestEntry": cmgDsuTestEntry,
       "cmgDsuLoopbackPattern": cmgDsuLoopbackPattern,
       "cmgDsuLocalDteLoopback": cmgDsuLocalDteLoopback,
       "cmgDsuNearEndDataChannelLoopback": cmgDsuNearEndDataChannelLoopback,
       "cmgDsuFarEndDataChannelLoopback": cmgDsuFarEndDataChannelLoopback,
       "cmgDsuRemoteLoopback": cmgDsuRemoteLoopback,
       "cmgDsuDataTerminalLoopback": cmgDsuDataTerminalLoopback,
       "cmgDsuReset": cmgDsuReset,
       "cmgAnalogPorts": cmgAnalogPorts,
       "cmgAnalogPortTable": cmgAnalogPortTable,
       "cmgAnalogPortEntry": cmgAnalogPortEntry,
       "cmgAnalogSlot": cmgAnalogSlot,
       "cmgAnalogPort": cmgAnalogPort,
       "cmgAnalogEchoCancellerControl": cmgAnalogEchoCancellerControl,
       "cmgAnalogEchoCancellerConfig1": cmgAnalogEchoCancellerConfig1,
       "cmgAnalogEchoCancellerConfig2": cmgAnalogEchoCancellerConfig2,
       "cmgAnalogBalance": cmgAnalogBalance,
       "cmgAnalogReceiveGain": cmgAnalogReceiveGain,
       "cmgAnalogTransmitGain": cmgAnalogTransmitGain,
       "cmgExpansionUnits": cmgExpansionUnits,
       "cmgExpansionUnitsTable": cmgExpansionUnitsTable,
       "cmgExpansions": cmgExpansions,
       "cmgExpansionSlot": cmgExpansionSlot,
       "cmgExpansionModelNumber": cmgExpansionModelNumber,
       "cmgExpansionDescription": cmgExpansionDescription,
       "cmgExpansionSerialNumber": cmgExpansionSerialNumber,
       "cmgExpansionHWVintage": cmgExpansionHWVintage,
       "cmgExpansionHWSuffix": cmgExpansionHWSuffix,
       "cmgExpansionDemandTest": cmgExpansionDemandTest,
       "cmgExpansionDemandTestResult": cmgExpansionDemandTestResult,
       "cmgTimeslotMonitoring": cmgTimeslotMonitoring,
       "cmgTimeslotUpperThreshold": cmgTimeslotUpperThreshold,
       "cmgTimeslotLowerThreshold": cmgTimeslotLowerThreshold,
       "cmgProcessor": cmgProcessor,
       "cmgProcessorConfig": cmgProcessorConfig,
       "cmgGatewayNumber": cmgGatewayNumber,
       "cmgMACAddress": cmgMACAddress,
       "cmgFWVersion": cmgFWVersion,
       "cmgCurrentIpAddress": cmgCurrentIpAddress,
       "cmgUseDhcpForIpAddress": cmgUseDhcpForIpAddress,
       "cmgUseDhcpForVlan": cmgUseDhcpForVlan,
       "cmgDhcpSson": cmgDhcpSson,
       "cmgStaticIpAddress": cmgStaticIpAddress,
       "cmgDnsServerList": cmgDnsServerList,
       "cmgDnsHostname": cmgDnsHostname,
       "cmgMgpFaultMask": cmgMgpFaultMask,
       "cmgCurrentInetAddressType": cmgCurrentInetAddressType,
       "cmgCurrentInetAddress": cmgCurrentInetAddress,
       "cmgProcessorQos": cmgProcessorQos,
       "cmgQosControl": cmgQosControl,
       "cmgRemoteSigDscp": cmgRemoteSigDscp,
       "cmgRemoteSig802Priority": cmgRemoteSig802Priority,
       "cmgLocalSigDscp": cmgLocalSigDscp,
       "cmgLocalSig802Priority": cmgLocalSig802Priority,
       "cmgStatic802Vlan": cmgStatic802Vlan,
       "cmgCurrent802Vlan": cmgCurrent802Vlan,
       "cmgProcessorClock": cmgProcessorClock,
       "cmgPrimaryClockSource": cmgPrimaryClockSource,
       "cmgSecondaryClockSource": cmgSecondaryClockSource,
       "cmgActiveClockSource": cmgActiveClockSource,
       "cmgClockSwitching": cmgClockSwitching,
       "cmgClockSourceControl": cmgClockSourceControl,
       "cmgControllers": cmgControllers,
       "cmgRegistrationState": cmgRegistrationState,
       "cmgActiveControllerAddress": cmgActiveControllerAddress,
       "cmgH248LinkStatus": cmgH248LinkStatus,
       "cmgH248LinkErrorCode": cmgH248LinkErrorCode,
       "cmgUseDhcpForMgcList": cmgUseDhcpForMgcList,
       "cmgStaticControllerHosts": cmgStaticControllerHosts,
       "cmgDhcpControllerHosts": cmgDhcpControllerHosts,
       "cmgPrimarySearchTime": cmgPrimarySearchTime,
       "cmgTotalSearchTime": cmgTotalSearchTime,
       "cmgTransitionPoint": cmgTransitionPoint,
       "cmgActiveControllerSoftwareVersion": cmgActiveControllerSoftwareVersion,
       "cmgActiveControllerInetAddressType": cmgActiveControllerInetAddressType,
       "cmgActiveControllerInetAddress": cmgActiveControllerInetAddress,
       "cmgVoip": cmgVoip,
       "cmgVoipEngineUseDhcp": cmgVoipEngineUseDhcp,
       "cmgVoipQosControl": cmgVoipQosControl,
       "cmgVoipRemoteParameters": cmgVoipRemoteParameters,
       "cmgVoipRemoteQosParameters": cmgVoipRemoteQosParameters,
       "cmgVoipRemoteBbeDscp": cmgVoipRemoteBbeDscp,
       "cmgVoipRemoteEfDscp": cmgVoipRemoteEfDscp,
       "cmgVoipRemote802Priority": cmgVoipRemote802Priority,
       "cmgVoipRemoteMinRtpPort": cmgVoipRemoteMinRtpPort,
       "cmgVoipRemoteMaxRtpPort": cmgVoipRemoteMaxRtpPort,
       "cmgVoipRemoteRtcpParameters": cmgVoipRemoteRtcpParameters,
       "cmgVoipRemoteRtcpEnabled": cmgVoipRemoteRtcpEnabled,
       "cmgVoipRemoteRtcpMonitorIpAddress": cmgVoipRemoteRtcpMonitorIpAddress,
       "cmgVoipRemoteRtcpMonitorPort": cmgVoipRemoteRtcpMonitorPort,
       "cmgVoipRemoteRtcpReportPeriod": cmgVoipRemoteRtcpReportPeriod,
       "cmgVoipRemoteRtcpMonitorInetAddressType": cmgVoipRemoteRtcpMonitorInetAddressType,
       "cmgVoipRemoteRtcpMonitorInetAddress": cmgVoipRemoteRtcpMonitorInetAddress,
       "cmgVoipRemoteRtcpMonitorPortInetAddress": cmgVoipRemoteRtcpMonitorPortInetAddress,
       "cmgVoipRemoteRsvpParameters": cmgVoipRemoteRsvpParameters,
       "cmgVoipRemoteRsvpEnabled": cmgVoipRemoteRsvpEnabled,
       "cmgVoipRemoteRetryOnFailure": cmgVoipRemoteRetryOnFailure,
       "cmgVoipRemoteRetryDelay": cmgVoipRemoteRetryDelay,
       "cmgVoipRemoteRsvpProfile": cmgVoipRemoteRsvpProfile,
       "cmgVoipLocalParameters": cmgVoipLocalParameters,
       "cmgVoipLocalQosParameters": cmgVoipLocalQosParameters,
       "cmgVoipLocalBbeDscp": cmgVoipLocalBbeDscp,
       "cmgVoipLocalEfDscp": cmgVoipLocalEfDscp,
       "cmgVoipLocal802Priority": cmgVoipLocal802Priority,
       "cmgVoipLocalMinRtpPort": cmgVoipLocalMinRtpPort,
       "cmgVoipLocalMaxRtpPort": cmgVoipLocalMaxRtpPort,
       "cmgVoipLocalRtcpParameters": cmgVoipLocalRtcpParameters,
       "cmgVoipLocalRtcpEnabled": cmgVoipLocalRtcpEnabled,
       "cmgVoipLocalRtcpMonitorIpAddress": cmgVoipLocalRtcpMonitorIpAddress,
       "cmgVoipLocalRtcpMonitorPort": cmgVoipLocalRtcpMonitorPort,
       "cmgVoipLocalRtcpReportPeriod": cmgVoipLocalRtcpReportPeriod,
       "cmgVoipLocalRtcpMonitorInetAddressType": cmgVoipLocalRtcpMonitorInetAddressType,
       "cmgVoipLocalRtcpMonitorInetAddress": cmgVoipLocalRtcpMonitorInetAddress,
       "cmgVoipLocalRtcpMonitorPortInetAddress": cmgVoipLocalRtcpMonitorPortInetAddress,
       "cmgVoipLocalRsvpParameters": cmgVoipLocalRsvpParameters,
       "cmgVoipLocalRsvpEnabled": cmgVoipLocalRsvpEnabled,
       "cmgVoipLocalRetryOnFailure": cmgVoipLocalRetryOnFailure,
       "cmgVoipLocalRetryDelay": cmgVoipLocalRetryDelay,
       "cmgVoipLocalRsvpProfile": cmgVoipLocalRsvpProfile,
       "cmgVoipEngineTable": cmgVoipEngineTable,
       "cmgVoipEngineEntry": cmgVoipEngineEntry,
       "cmgVoipSlot": cmgVoipSlot,
       "cmgVoipMACAddress": cmgVoipMACAddress,
       "cmgVoipStaticIpAddress": cmgVoipStaticIpAddress,
       "cmgVoipCurrentIpAddress": cmgVoipCurrentIpAddress,
       "cmgVoipJitterBufferSize": cmgVoipJitterBufferSize,
       "cmgVoipTotalChannels": cmgVoipTotalChannels,
       "cmgVoipChannelsInUse": cmgVoipChannelsInUse,
       "cmgVoipAverageOccupancy": cmgVoipAverageOccupancy,
       "cmgVoipHyperactivity": cmgVoipHyperactivity,
       "cmgVoipAdminState": cmgVoipAdminState,
       "cmgVoipDspFWVersion": cmgVoipDspFWVersion,
       "cmgVoipDspStatus": cmgVoipDspStatus,
       "cmgVoipEngineReset": cmgVoipEngineReset,
       "cmgVoipFaultMask": cmgVoipFaultMask,
       "cmgVoipStaticInetAddressType": cmgVoipStaticInetAddressType,
       "cmgVoipStaticInetAddress": cmgVoipStaticInetAddress,
       "cmgVoipCurrentInetAddressType": cmgVoipCurrentInetAddressType,
       "cmgVoipCurrentInetAddress": cmgVoipCurrentInetAddress,
       "cmgVoipDSPCoreTable": cmgVoipDSPCoreTable,
       "cmgVoipDSPCoreEntry": cmgVoipDSPCoreEntry,
       "cmgDSPCoreCoreId": cmgDSPCoreCoreId,
       "cmgDSPCoreTotalChannels": cmgDSPCoreTotalChannels,
       "cmgDSPCoreChannelsInUse": cmgDSPCoreChannelsInUse,
       "cmgDSPCoreAdminState": cmgDSPCoreAdminState,
       "cmgDSPCoreStatus": cmgDSPCoreStatus,
       "cmgDSPCoreDemandTest": cmgDSPCoreDemandTest,
       "cmgDSPCoreDemandTestResult": cmgDSPCoreDemandTestResult,
       "cmgVoipEchoCancellerControl": cmgVoipEchoCancellerControl,
       "cmgVoipEchoCancellerConfig1": cmgVoipEchoCancellerConfig1,
       "cmgVoipEchoCancellerConfig2": cmgVoipEchoCancellerConfig2,
       "cmgVoipTotalChannelsEnforcedByCM": cmgVoipTotalChannelsEnforcedByCM,
       "cmgTraps": cmgTraps,
       "cmgTrapManagerTable": cmgTrapManagerTable,
       "cmgTrapManagerEntry": cmgTrapManagerEntry,
       "cmgTrapManagerAddress": cmgTrapManagerAddress,
       "cmgTrapManagerControl": cmgTrapManagerControl,
       "cmgTrapManagerMask": cmgTrapManagerMask,
       "cmgTrapManagerRowStatus": cmgTrapManagerRowStatus,
       "cmgTrapDefinitions": cmgTrapDefinitions,
       "cmgTrapVariables": cmgTrapVariables,
       "cmgTrapLocation": cmgTrapLocation,
       "cmgTrapOnBoard": cmgTrapOnBoard,
       "cmgTrapSubsystem": cmgTrapSubsystem,
       "cmgTrapOnIccMissing": cmgTrapOnIccMissing,
       "cmgTrapModule": cmgTrapModule,
       "cmgTrapSeverity": cmgTrapSeverity,
       "cmgProductId": cmgProductId,
       "cmgTrapAvailableTimeslots": cmgTrapAvailableTimeslots,
       "cmgTrapInUseTimeslots": cmgTrapInUseTimeslots,
       "cmgFipsErrorType": cmgFipsErrorType,
       "cmgTrapTypes": cmgTrapTypes,
       "cmgTrapV3separator": cmgTrapV3separator,
       "cmgMultipleFanFault": cmgMultipleFanFault,
       "cmgMultipleFanClear": cmgMultipleFanClear,
       "cmgPsuFanBriefFault": cmgPsuFanBriefFault,
       "cmgPsuFanBriefClear": cmgPsuFanBriefClear,
       "cmgPsuFanProlongedFault": cmgPsuFanProlongedFault,
       "cmgPsuFanProlongedClear": cmgPsuFanProlongedClear,
       "cmgCpuTempWarningFault": cmgCpuTempWarningFault,
       "cmgCpuTempWarningClear": cmgCpuTempWarningClear,
       "cmgDspTempWarningFault": cmgDspTempWarningFault,
       "cmgDspTempWarningClear": cmgDspTempWarningClear,
       "cmgTempShutdownFault": cmgTempShutdownFault,
       "cmgMgpPowerFault": cmgMgpPowerFault,
       "cmgMgpPowerClear": cmgMgpPowerClear,
       "cmgMediaModulePowerFault": cmgMediaModulePowerFault,
       "cmgMediaModulePowerClear": cmgMediaModulePowerClear,
       "cmgVoipPowerFault": cmgVoipPowerFault,
       "cmgVoipPowerClear": cmgVoipPowerClear,
       "cmgDspPowerFault": cmgDspPowerFault,
       "cmgDspPowerClear": cmgDspPowerClear,
       "cmg8260PowerFault": cmg8260PowerFault,
       "cmg8260PowerClear": cmg8260PowerClear,
       "cmgAuxPowerFault": cmgAuxPowerFault,
       "cmgAuxPowerClear": cmgAuxPowerClear,
       "cmgFanPowerFault": cmgFanPowerFault,
       "cmgFanPowerClear": cmgFanPowerClear,
       "cmgSyncSignalFault": cmgSyncSignalFault,
       "cmgSyncSignalClear": cmgSyncSignalClear,
       "cmgVoipHardwareFault": cmgVoipHardwareFault,
       "cmgVoipHardwareClear": cmgVoipHardwareClear,
       "cmgSyncSignalWarn": cmgSyncSignalWarn,
       "cmgSyncWarnClear": cmgSyncWarnClear,
       "cmgSyncSignalExcess": cmgSyncSignalExcess,
       "cmgSyncExcessClear": cmgSyncExcessClear,
       "cmgVoipCoreFault": cmgVoipCoreFault,
       "cmgVoipCoreClear": cmgVoipCoreClear,
       "cmgModuleRemove": cmgModuleRemove,
       "cmgModuleInsertFault": cmgModuleInsertFault,
       "cmgModuleInsertSuccess": cmgModuleInsertSuccess,
       "cmgMgBusyout": cmgMgBusyout,
       "cmgMgRelease": cmgMgRelease,
       "cmgUnsupportedMmEnrolement": cmgUnsupportedMmEnrolement,
       "cmgDataModuleAwohConflict": cmgDataModuleAwohConflict,
       "cmgFirmwareDownloadBegun": cmgFirmwareDownloadBegun,
       "cmgFirmwareDownloadSuccess": cmgFirmwareDownloadSuccess,
       "cmgRegistrationSuccess": cmgRegistrationSuccess,
       "cmgMgManualReset": cmgMgManualReset,
       "cmgModuleManualReset": cmgModuleManualReset,
       "cmgVoipManualReset": cmgVoipManualReset,
       "cmgDsuManualReset": cmgDsuManualReset,
       "cmgConfigUploadBegun": cmgConfigUploadBegun,
       "cmgConfigUploadSuccess": cmgConfigUploadSuccess,
       "cmgMemoryFault": cmgMemoryFault,
       "cmgMemoryClear": cmgMemoryClear,
       "cmgDhcpRequestFault": cmgDhcpRequestFault,
       "cmgDhcpRequestClear": cmgDhcpRequestClear,
       "cmgFirmwareDownloadFault": cmgFirmwareDownloadFault,
       "cmgProcessRestart": cmgProcessRestart,
       "cmgProcessRestartClear": cmgProcessRestartClear,
       "cmgIccMissingFault": cmgIccMissingFault,
       "cmgIccMissingClear": cmgIccMissingClear,
       "cmgIccAutoReset": cmgIccAutoReset,
       "cmgIccAutoResetClear": cmgIccAutoResetClear,
       "cmgPrimaryControllerFault": cmgPrimaryControllerFault,
       "cmgPrimaryControllerClear": cmgPrimaryControllerClear,
       "cmgNoControllerFault": cmgNoControllerFault,
       "cmgNoControllerClear": cmgNoControllerClear,
       "cmgRegistrationFault": cmgRegistrationFault,
       "cmgH248LinkDown": cmgH248LinkDown,
       "cmgH248LinkUp": cmgH248LinkUp,
       "cmgTestFault": cmgTestFault,
       "cmgTestClear": cmgTestClear,
       "cmgTestThresholdFault": cmgTestThresholdFault,
       "cmgTestThresholdClear": cmgTestThresholdClear,
       "cmgMgAutoReset": cmgMgAutoReset,
       "cmgModuleAutoReset": cmgModuleAutoReset,
       "cmgModuleAutoResetClear": cmgModuleAutoResetClear,
       "cmgModulePostFault": cmgModulePostFault,
       "cmgModulePostClear": cmgModulePostClear,
       "cmgModuleParameterFault": cmgModuleParameterFault,
       "cmgModuleParameterClear": cmgModuleParameterClear,
       "cmgConfigUploadFault": cmgConfigUploadFault,
       "cmgVoipOccFault": cmgVoipOccFault,
       "cmgVoipOccClear": cmgVoipOccClear,
       "cmgVoipAvgOccFault": cmgVoipAvgOccFault,
       "cmgVoipAvgOccClear": cmgVoipAvgOccClear,
       "cmgVoipAutoReset": cmgVoipAutoReset,
       "cmgVoipAutoResetClear": cmgVoipAutoResetClear,
       "cmgDsuFpgaConfigureFault": cmgDsuFpgaConfigureFault,
       "cmgDsuFpgaConfigureClear": cmgDsuFpgaConfigureClear,
       "cmgDsuAutoReset": cmgDsuAutoReset,
       "cmgDsuAutoResetClear": cmgDsuAutoResetClear,
       "cmgDsuDteDtrFault": cmgDsuDteDtrFault,
       "cmgDsuDteDtrClear": cmgDsuDteDtrClear,
       "cmgDsuDteRtsFault": cmgDsuDteRtsFault,
       "cmgDsuDteRtsClear": cmgDsuDteRtsClear,
       "cmgDsuTxDFault": cmgDsuTxDFault,
       "cmgDsuTxDClear": cmgDsuTxDClear,
       "cmgDsuRxDFailure": cmgDsuRxDFailure,
       "cmgDsuRxDClear": cmgDsuRxDClear,
       "cmgVoipIpConfigFault": cmgVoipIpConfigFault,
       "cmgVoipIpConfigClear": cmgVoipIpConfigClear,
       "cmgConfigDownloadFault": cmgConfigDownloadFault,
       "cmgConfigDownloadBegun": cmgConfigDownloadBegun,
       "cmgConfigDownloadSuccess": cmgConfigDownloadSuccess,
       "cmgTimeslotOccupancyFault": cmgTimeslotOccupancyFault,
       "cmgTimeslotOccupancyClear": cmgTimeslotOccupancyClear,
       "cmgTimeslotAvailabilityFault": cmgTimeslotAvailabilityFault,
       "cmgTimeslotAvailabilityClear": cmgTimeslotAvailabilityClear,
       "cmgRegistrationSuccessInetAddress": cmgRegistrationSuccessInetAddress,
       "cmgRegistrationFaultInetAddress": cmgRegistrationFaultInetAddress,
       "cmgDs1Layer2Down": cmgDs1Layer2Down,
       "cmgDs1Layer2Up": cmgDs1Layer2Up,
       "cmgFipsErrorMode": cmgFipsErrorMode,
       "cmgCertErrorCertRevoked": cmgCertErrorCertRevoked,
       "cmgCrlAccessDenied": cmgCrlAccessDenied,
       "cmgCrlFileSize": cmgCrlFileSize,
       "cmgCertErrorCertExpired": cmgCertErrorCertExpired,
       "cmgCertErrorNearExpiry": cmgCertErrorNearExpiry,
       "cmgCertErrorIdAuthentication": cmgCertErrorIdAuthentication,
       "cmgFirmwareDownloadWarning": cmgFirmwareDownloadWarning,
       "cmgContactClosures": cmgContactClosures,
       "cmgContactClosuresTable": cmgContactClosuresTable,
       "cmgContactClosuresEntry": cmgContactClosuresEntry,
       "cmgCcModule": cmgCcModule,
       "cmgCcPort": cmgCcPort,
       "cmgCcRelay": cmgCcRelay,
       "cmgCcAdminState": cmgCcAdminState,
       "cmgCcPulseDuration": cmgCcPulseDuration,
       "cmgCcStatus": cmgCcStatus,
       "cmgETR": cmgETR,
       "cmgETRTable": cmgETRTable,
       "cmgETREntry": cmgETREntry,
       "cmgEtrModule": cmgEtrModule,
       "cmgEtrAdminState": cmgEtrAdminState,
       "cmgEtrNumberOfPairs": cmgEtrNumberOfPairs,
       "cmgEtrStatus": cmgEtrStatus,
       "cmgEtrCurrentLoopDetect": cmgEtrCurrentLoopDetect,
       "cmgDynamicCAC": cmgDynamicCAC,
       "cmgDynCacStatus": cmgDynCacStatus,
       "cmgDynCacRBBL": cmgDynCacRBBL,
       "cmgDynCacLastUpdate": cmgDynCacLastUpdate,
       "cmgSLAMonitor": cmgSLAMonitor,
       "cmgSLAMonitorState": cmgSLAMonitorState,
       "cmgSLAMonitorServerInetAddressType": cmgSLAMonitorServerInetAddressType,
       "cmgSLAMonitorServerInetAddress": cmgSLAMonitorServerInetAddress,
       "cmgSLAMonitorServerPort": cmgSLAMonitorServerPort,
       "cmgSLAMonitorPacketCaptureMode": cmgSLAMonitorPacketCaptureMode,
       "cmgSLAMonitorVersion": cmgSLAMonitorVersion}
)
