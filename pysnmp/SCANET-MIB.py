# SNMP MIB module (SCANET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCANET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:54 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Scanet_ObjectIdentity = ObjectIdentity
scanet = _Scanet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1)
)
_Ts_2104_ObjectIdentity = ObjectIdentity
ts_2104 = _Ts_2104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 12)
)
_Cs_72xx_ObjectIdentity = ObjectIdentity
cs_72xx = _Cs_72xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 13)
)
_Cs_76xx_ObjectIdentity = ObjectIdentity
cs_76xx = _Cs_76xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 15)
)
_Cs_14xx_ObjectIdentity = ObjectIdentity
cs_14xx = _Cs_14xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 32)
)
_EthernetSwitch_ObjectIdentity = ObjectIdentity
ethernetSwitch = _EthernetSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 35)
)
_Es_1810_ObjectIdentity = ObjectIdentity
es_1810 = _Es_1810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 35, 1)
)
_Es_1820_ObjectIdentity = ObjectIdentity
es_1820 = _Es_1820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 35, 2)
)
_Es10t24_ObjectIdentity = ObjectIdentity
es10t24 = _Es10t24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 35, 3)
)
_Es10t24plus_ObjectIdentity = ObjectIdentity
es10t24plus = _Es10t24plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 35, 4)
)
_Es_1520_ObjectIdentity = ObjectIdentity
es_1520 = _Es_1520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 35, 5)
)
_Es_1850_ObjectIdentity = ObjectIdentity
es_1850 = _Es_1850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 35, 6)
)
_Es_1851_ObjectIdentity = ObjectIdentity
es_1851 = _Es_1851_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 35, 7)
)
_Es100fx_ObjectIdentity = ObjectIdentity
es100fx = _Es100fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 35, 8)
)
_Cs_3300_ObjectIdentity = ObjectIdentity
cs_3300 = _Cs_3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 42)
)
_Mfts_ObjectIdentity = ObjectIdentity
mfts = _Mfts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 67)
)
_Cs_21xx_ObjectIdentity = ObjectIdentity
cs_21xx = _Cs_21xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 68)
)
_Ct_30xx_ObjectIdentity = ObjectIdentity
ct_30xx = _Ct_30xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 69)
)
_In_40xx_ObjectIdentity = ObjectIdentity
in_40xx = _In_40xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 82)
)
_Ct_40xx_ObjectIdentity = ObjectIdentity
ct_40xx = _Ct_40xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 83)
)
_MatchboxRouter_ObjectIdentity = ObjectIdentity
matchboxRouter = _MatchboxRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88)
)
_Mr_1010_ObjectIdentity = ObjectIdentity
mr_1010 = _Mr_1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 1)
)
_Mr_1011_ObjectIdentity = ObjectIdentity
mr_1011 = _Mr_1011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 2)
)
_Mr_1013_ObjectIdentity = ObjectIdentity
mr_1013 = _Mr_1013_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 3)
)
_Mr_1014_ObjectIdentity = ObjectIdentity
mr_1014 = _Mr_1014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 4)
)
_Mr_1050_ObjectIdentity = ObjectIdentity
mr_1050 = _Mr_1050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 5)
)
_Mr_1051_ObjectIdentity = ObjectIdentity
mr_1051 = _Mr_1051_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 6)
)
_Mr_1110_ObjectIdentity = ObjectIdentity
mr_1110 = _Mr_1110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 7)
)
_Mr_1111_ObjectIdentity = ObjectIdentity
mr_1111 = _Mr_1111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 8)
)
_Mr_1113_ObjectIdentity = ObjectIdentity
mr_1113 = _Mr_1113_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 9)
)
_Mr_1114_ObjectIdentity = ObjectIdentity
mr_1114 = _Mr_1114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 10)
)
_Mr_1150_ObjectIdentity = ObjectIdentity
mr_1150 = _Mr_1150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 11)
)
_Mr_1151_ObjectIdentity = ObjectIdentity
mr_1151 = _Mr_1151_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 12)
)
_Mr_1055_ObjectIdentity = ObjectIdentity
mr_1055 = _Mr_1055_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 13)
)
_Mr_1155_ObjectIdentity = ObjectIdentity
mr_1155 = _Mr_1155_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 14)
)
_Mr_1020_ObjectIdentity = ObjectIdentity
mr_1020 = _Mr_1020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 15)
)
_Mr_1120_ObjectIdentity = ObjectIdentity
mr_1120 = _Mr_1120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 16)
)
_Mr_1023_ObjectIdentity = ObjectIdentity
mr_1023 = _Mr_1023_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 17)
)
_Mr_1123_ObjectIdentity = ObjectIdentity
mr_1123 = _Mr_1123_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 18)
)
_Mr_1024_ObjectIdentity = ObjectIdentity
mr_1024 = _Mr_1024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 19)
)
_Mr_1124_ObjectIdentity = ObjectIdentity
mr_1124 = _Mr_1124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 20)
)
_Mr_1040_ObjectIdentity = ObjectIdentity
mr_1040 = _Mr_1040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 21)
)
_Mr_1140_ObjectIdentity = ObjectIdentity
mr_1140 = _Mr_1140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 22)
)
_Mr_1021_ObjectIdentity = ObjectIdentity
mr_1021 = _Mr_1021_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 23)
)
_Mr_1121_ObjectIdentity = ObjectIdentity
mr_1121 = _Mr_1121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 24)
)
_Er9100_ObjectIdentity = ObjectIdentity
er9100 = _Er9100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 25)
)
_Er9200_ObjectIdentity = ObjectIdentity
er9200 = _Er9200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 26)
)
_Er9300_ObjectIdentity = ObjectIdentity
er9300 = _Er9300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 27)
)
_Er9400_ObjectIdentity = ObjectIdentity
er9400 = _Er9400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 1, 88, 28)
)
_Mib2ext_ObjectIdentity = ObjectIdentity
mib2ext = _Mib2ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 2, 1)
)


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("rebootAndLoadFlash", 10),
          ("reloadAnnounce", 9),
          ("reloadDefault", 13),
          ("reloadDefaultKeepIP", 12),
          ("reloadParm", 7),
          ("reloadProfile", 6),
          ("reloadTerminfo", 5),
          ("reset1hour", 3),
          ("reset8hours", 4),
          ("resetIdle", 2),
          ("resetNow", 1),
          ("resetWarm", 11),
          ("saveParm", 8))
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 1),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("mandatory")
_Ram_Type = Integer32
_Ram_Object = MibScalar
ram = _Ram_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 2),
    _Ram_Type()
)
ram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ram.setStatus("mandatory")
_IdTable_Object = MibTable
idTable = _IdTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 3)
)
if mibBuilder.loadTexts:
    idTable.setStatus("mandatory")
_IdEntry_Object = MibTableRow
idEntry = _IdEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 3, 1)
)
idEntry.setIndexNames(
    (0, "SCANET-MIB", "brdNumber"),
)
if mibBuilder.loadTexts:
    idEntry.setStatus("mandatory")
_BrdNumber_Type = Integer32
_BrdNumber_Object = MibTableColumn
brdNumber = _BrdNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 3, 1, 1),
    _BrdNumber_Type()
)
brdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdNumber.setStatus("mandatory")


class _HwId_Type(DisplayString):
    """Custom type hwId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwId_Type.__name__ = "DisplayString"
_HwId_Object = MibTableColumn
hwId = _HwId_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 3, 1, 2),
    _HwId_Type()
)
hwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwId.setStatus("mandatory")


class _FwId_Type(DisplayString):
    """Custom type fwId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwId_Type.__name__ = "DisplayString"
_FwId_Object = MibTableColumn
fwId = _FwId_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 3, 1, 3),
    _FwId_Type()
)
fwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwId.setStatus("mandatory")
_SwTable_Object = MibTable
swTable = _SwTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 4)
)
if mibBuilder.loadTexts:
    swTable.setStatus("mandatory")
_SwEntry_Object = MibTableRow
swEntry = _SwEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    swEntry.setStatus("mandatory")


class _SwName_Type(DisplayString):
    """Custom type swName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwName_Type.__name__ = "DisplayString"
_SwName_Object = MibTableColumn
swName = _SwName_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 4, 1, 1),
    _SwName_Type()
)
swName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swName.setStatus("mandatory")
_ErrorLogNumber_Type = Integer32
_ErrorLogNumber_Object = MibScalar
errorLogNumber = _ErrorLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 5),
    _ErrorLogNumber_Type()
)
errorLogNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorLogNumber.setStatus("mandatory")
_SystemLogNumber_Type = Integer32
_SystemLogNumber_Object = MibScalar
systemLogNumber = _SystemLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 6),
    _SystemLogNumber_Type()
)
systemLogNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogNumber.setStatus("mandatory")
_AutAccessTable_Object = MibTable
autAccessTable = _AutAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 7)
)
if mibBuilder.loadTexts:
    autAccessTable.setStatus("mandatory")
_AutAccessEntry_Object = MibTableRow
autAccessEntry = _AutAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 7, 1)
)
autAccessEntry.setIndexNames(
    (0, "SCANET-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    autAccessEntry.setStatus("mandatory")
_AutAccessIP_Type = IpAddress
_AutAccessIP_Object = MibTableColumn
autAccessIP = _AutAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 7, 1, 1),
    _AutAccessIP_Type()
)
autAccessIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autAccessIP.setStatus("mandatory")
_AutAccessTime_Type = TimeTicks
_AutAccessTime_Object = MibTableColumn
autAccessTime = _AutAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 7, 1, 2),
    _AutAccessTime_Type()
)
autAccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autAccessTime.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 7, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_TimeOfDay_Type = Integer32
_TimeOfDay_Object = MibScalar
timeOfDay = _TimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 8),
    _TimeOfDay_Type()
)
timeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeOfDay.setStatus("mandatory")
_ConfigurationLastChanged_Type = Integer32
_ConfigurationLastChanged_Object = MibScalar
configurationLastChanged = _ConfigurationLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 9),
    _ConfigurationLastChanged_Type()
)
configurationLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationLastChanged.setStatus("mandatory")
_ConfigurationLastSaved_Type = Integer32
_ConfigurationLastSaved_Object = MibScalar
configurationLastSaved = _ConfigurationLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 10),
    _ConfigurationLastSaved_Type()
)
configurationLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationLastSaved.setStatus("mandatory")


class _UnsavedConfiguration_Type(Integer32):
    """Custom type unsavedConfiguration based on Integer32"""
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


_UnsavedConfiguration_Type.__name__ = "Integer32"
_UnsavedConfiguration_Object = MibScalar
unsavedConfiguration = _UnsavedConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 1, 11),
    _UnsavedConfiguration_Type()
)
unsavedConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unsavedConfiguration.setStatus("mandatory")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 2, 4)
)
_IpTable_Object = MibTable
ipTable = _IpTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ipTable.setStatus("mandatory")
_IpEntry_Object = MibTableRow
ipEntry = _IpEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 4, 1, 1)
)
ipEntry.setIndexNames(
    (0, "SCANET-MIB", "ipIndex"),
    (0, "SCANET-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    ipEntry.setStatus("mandatory")
_IpIndex_Type = Integer32
_IpIndex_Object = MibTableColumn
ipIndex = _IpIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 4, 1, 1, 1),
    _IpIndex_Type()
)
ipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIndex.setStatus("mandatory")


class _IpAddrAndMask_Type(OctetString):
    """Custom type ipAddrAndMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IpAddrAndMask_Type.__name__ = "OctetString"
_IpAddrAndMask_Object = MibTableColumn
ipAddrAndMask = _IpAddrAndMask_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 4, 1, 1, 2),
    _IpAddrAndMask_Type()
)
ipAddrAndMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddrAndMask.setStatus("mandatory")
_PysmiFakeCol2_Type = IpAddress
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 4, 1, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 2, 11)
)


class _Filter_Type(Integer32):
    """Custom type filter based on Integer32"""
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
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_Filter_Type.__name__ = "Integer32"
_Filter_Object = MibScalar
filter = _Filter_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 1),
    _Filter_Type()
)
filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filter.setStatus("obsolete")


class _Print_Type(DisplayString):
    """Custom type print based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Print_Type.__name__ = "DisplayString"
_Print_Object = MibScalar
print = _Print_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 2),
    _Print_Type()
)
print.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print.setStatus("mandatory")


class _Cause_Type(DisplayString):
    """Custom type cause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cause_Type.__name__ = "DisplayString"
_Cause_Object = MibScalar
cause = _Cause_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 3),
    _Cause_Type()
)
cause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cause.setStatus("mandatory")


class _Solution_Type(DisplayString):
    """Custom type solution based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Solution_Type.__name__ = "DisplayString"
_Solution_Object = MibScalar
solution = _Solution_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 4),
    _Solution_Type()
)
solution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solution.setStatus("mandatory")
_AutMaxEntries_Type = Integer32
_AutMaxEntries_Object = MibScalar
autMaxEntries = _AutMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 5),
    _AutMaxEntries_Type()
)
autMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autMaxEntries.setStatus("mandatory")
_AutTable_Object = MibTable
autTable = _AutTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 6)
)
if mibBuilder.loadTexts:
    autTable.setStatus("mandatory")
_AutEntry_Object = MibTableRow
autEntry = _AutEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 6, 1)
)
autEntry.setIndexNames(
    (0, "SCANET-MIB", "autNumber"),
)
if mibBuilder.loadTexts:
    autEntry.setStatus("mandatory")
_AutNumber_Type = Integer32
_AutNumber_Object = MibTableColumn
autNumber = _AutNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 6, 1, 1),
    _AutNumber_Type()
)
autNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autNumber.setStatus("mandatory")


class _AutIpAndAccessAndCommunity_Type(OctetString):
    """Custom type autIpAndAccessAndCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_AutIpAndAccessAndCommunity_Type.__name__ = "OctetString"
_AutIpAndAccessAndCommunity_Object = MibTableColumn
autIpAndAccessAndCommunity = _AutIpAndAccessAndCommunity_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 6, 1, 2),
    _AutIpAndAccessAndCommunity_Type()
)
autIpAndAccessAndCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autIpAndAccessAndCommunity.setStatus("mandatory")


class _AutDelete_Type(Integer32):
    """Custom type autDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_AutDelete_Type.__name__ = "Integer32"
_AutDelete_Object = MibTableColumn
autDelete = _AutDelete_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 6, 1, 3),
    _AutDelete_Type()
)
autDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autDelete.setStatus("mandatory")
_TrapMaxEntries_Type = Integer32
_TrapMaxEntries_Object = MibScalar
trapMaxEntries = _TrapMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 7),
    _TrapMaxEntries_Type()
)
trapMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMaxEntries.setStatus("mandatory")
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 8)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("mandatory")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 8, 1)
)
trapEntry.setIndexNames(
    (0, "SCANET-MIB", "trapNumber"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("mandatory")
_TrapNumber_Type = Integer32
_TrapNumber_Object = MibTableColumn
trapNumber = _TrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 8, 1, 1),
    _TrapNumber_Type()
)
trapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNumber.setStatus("mandatory")


class _TrapIpAndCommunity_Type(OctetString):
    """Custom type trapIpAndCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_TrapIpAndCommunity_Type.__name__ = "OctetString"
_TrapIpAndCommunity_Object = MibTableColumn
trapIpAndCommunity = _TrapIpAndCommunity_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 8, 1, 2),
    _TrapIpAndCommunity_Type()
)
trapIpAndCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIpAndCommunity.setStatus("mandatory")


class _TrapDelete_Type(Integer32):
    """Custom type trapDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_TrapDelete_Type.__name__ = "Integer32"
_TrapDelete_Object = MibTableColumn
trapDelete = _TrapDelete_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 11, 8, 1, 3),
    _TrapDelete_Type()
)
trapDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDelete.setStatus("mandatory")
_SwUpdate_ObjectIdentity = ObjectIdentity
swUpdate = _SwUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 2, 40)
)
_SwInfoTable_Object = MibTable
swInfoTable = _SwInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 40, 1)
)
if mibBuilder.loadTexts:
    swInfoTable.setStatus("mandatory")
_SwInfoEntry_Object = MibTableRow
swInfoEntry = _SwInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 40, 1, 1)
)
swInfoEntry.setIndexNames(
    (0, "SCANET-MIB", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    swInfoEntry.setStatus("mandatory")


class _SwStatus_Type(Integer32):
    """Custom type swStatus based on Integer32"""
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
        *(("approved", 2),
          ("experimental", 3),
          ("none", 4),
          ("unavailable", 1))
    )


_SwStatus_Type.__name__ = "Integer32"
_SwStatus_Object = MibTableColumn
swStatus = _SwStatus_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 40, 1, 1, 1),
    _SwStatus_Type()
)
swStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swStatus.setStatus("mandatory")


class _SwName2_Type(OctetString):
    """Custom type swName2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_SwName2_Type.__name__ = "OctetString"
_SwName2_Object = MibScalar
swName2 = _SwName2_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 40, 1, 1, 2),
    _SwName2_Type()
)
swName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swName2.setStatus("mandatory")
_SwLoadTime_Type = TimeTicks
_SwLoadTime_Object = MibTableColumn
swLoadTime = _SwLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 40, 1, 1, 3),
    _SwLoadTime_Type()
)
swLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLoadTime.setStatus("mandatory")
_SwTftpIp_Type = IpAddress
_SwTftpIp_Object = MibTableColumn
swTftpIp = _SwTftpIp_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 40, 1, 1, 4),
    _SwTftpIp_Type()
)
swTftpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTftpIp.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 40, 1, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")


class _SwTftpIpAndSwName_Type(OctetString):
    """Custom type swTftpIpAndSwName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SwTftpIpAndSwName_Type.__name__ = "OctetString"
_SwTftpIpAndSwName_Object = MibScalar
swTftpIpAndSwName = _SwTftpIpAndSwName_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 40, 2),
    _SwTftpIpAndSwName_Type()
)
swTftpIpAndSwName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTftpIpAndSwName.setStatus("mandatory")


class _SwUpdateResult_Type(Integer32):
    """Custom type swUpdateResult based on Integer32"""
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
        *(("errorMoreFlash", 7),
          ("errorMoreRAM", 8),
          ("errorNoSoftware", 5),
          ("errorNoTftpServer", 4),
          ("errorSoftwareMismatch", 6),
          ("errorUnknown", 3),
          ("noError", 1),
          ("swUpdateRunning", 2))
    )


_SwUpdateResult_Type.__name__ = "Integer32"
_SwUpdateResult_Object = MibScalar
swUpdateResult = _SwUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 208, 2, 40, 3),
    _SwUpdateResult_Type()
)
swUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUpdateResult.setStatus("mandatory")
_ScaProt_ObjectIdentity = ObjectIdentity
scaProt = _ScaProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCANET-MIB",
    **{"scanet": scanet,
       "products": products,
       "ts-2104": ts_2104,
       "cs-72xx": cs_72xx,
       "cs-76xx": cs_76xx,
       "cs-14xx": cs_14xx,
       "ethernetSwitch": ethernetSwitch,
       "es-1810": es_1810,
       "es-1820": es_1820,
       "es10t24": es10t24,
       "es10t24plus": es10t24plus,
       "es-1520": es_1520,
       "es-1850": es_1850,
       "es-1851": es_1851,
       "es100fx": es100fx,
       "cs-3300": cs_3300,
       "mfts": mfts,
       "cs-21xx": cs_21xx,
       "ct-30xx": ct_30xx,
       "in-40xx": in_40xx,
       "ct-40xx": ct_40xx,
       "matchboxRouter": matchboxRouter,
       "mr-1010": mr_1010,
       "mr-1011": mr_1011,
       "mr-1013": mr_1013,
       "mr-1014": mr_1014,
       "mr-1050": mr_1050,
       "mr-1051": mr_1051,
       "mr-1110": mr_1110,
       "mr-1111": mr_1111,
       "mr-1113": mr_1113,
       "mr-1114": mr_1114,
       "mr-1150": mr_1150,
       "mr-1151": mr_1151,
       "mr-1055": mr_1055,
       "mr-1155": mr_1155,
       "mr-1020": mr_1020,
       "mr-1120": mr_1120,
       "mr-1023": mr_1023,
       "mr-1123": mr_1123,
       "mr-1024": mr_1024,
       "mr-1124": mr_1124,
       "mr-1040": mr_1040,
       "mr-1140": mr_1140,
       "mr-1021": mr_1021,
       "mr-1121": mr_1121,
       "er9100": er9100,
       "er9200": er9200,
       "er9300": er9300,
       "er9400": er9400,
       "mib2ext": mib2ext,
       "system": system,
       "reboot": reboot,
       "ram": ram,
       "idTable": idTable,
       "idEntry": idEntry,
       "brdNumber": brdNumber,
       "hwId": hwId,
       "fwId": fwId,
       "swTable": swTable,
       "swEntry": swEntry,
       "swName": swName,
       "errorLogNumber": errorLogNumber,
       "systemLogNumber": systemLogNumber,
       "autAccessTable": autAccessTable,
       "autAccessEntry": autAccessEntry,
       "autAccessIP": autAccessIP,
       "autAccessTime": autAccessTime,
       "pysmiFakeCol1": pysmiFakeCol1,
       "timeOfDay": timeOfDay,
       "configurationLastChanged": configurationLastChanged,
       "configurationLastSaved": configurationLastSaved,
       "unsavedConfiguration": unsavedConfiguration,
       "ip": ip,
       "ipTable": ipTable,
       "ipEntry": ipEntry,
       "ipIndex": ipIndex,
       "ipAddrAndMask": ipAddrAndMask,
       "pysmiFakeCol2": pysmiFakeCol2,
       "snmp": snmp,
       "filter": filter,
       "print": print,
       "cause": cause,
       "solution": solution,
       "autMaxEntries": autMaxEntries,
       "autTable": autTable,
       "autEntry": autEntry,
       "autNumber": autNumber,
       "autIpAndAccessAndCommunity": autIpAndAccessAndCommunity,
       "autDelete": autDelete,
       "trapMaxEntries": trapMaxEntries,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapNumber": trapNumber,
       "trapIpAndCommunity": trapIpAndCommunity,
       "trapDelete": trapDelete,
       "swUpdate": swUpdate,
       "swInfoTable": swInfoTable,
       "swInfoEntry": swInfoEntry,
       "swStatus": swStatus,
       "swName2": swName2,
       "swLoadTime": swLoadTime,
       "swTftpIp": swTftpIp,
       "pysmiFakeCol3": pysmiFakeCol3,
       "swTftpIpAndSwName": swTftpIpAndSwName,
       "swUpdateResult": swUpdateResult,
       "scaProt": scaProt}
)
