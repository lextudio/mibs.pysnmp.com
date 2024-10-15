# SNMP MIB module (MBG-SNMP-LTNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MBG-SNMP-LTNG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:36 2024
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

(MeinbergSwitch,
 mbgSnmpRoot) = mibBuilder.importSymbols(
    "MBG-SNMP-ROOT-MIB",
    "MeinbergSwitch",
    "mbgSnmpRoot")

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


# MODULE-IDENTITY

mbgLantimeNG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30)
)
mbgLantimeNG.setRevisions(
        ("2016-05-18 05:17",
         "2015-08-27 08:44",
         "2015-04-17 06:32",
         "2014-11-25 07:24",
         "2014-08-29 08:10",
         "2014-01-30 09:19",
         "2013-11-01 09:39",
         "2013-10-09 11:50",
         "2013-10-01 08:10",
         "2013-09-18 12:16",
         "2013-02-20 07:00",
         "2012-11-07 14:20",
         "2012-03-30 07:13",
         "2012-01-25 07:45",
         "2011-09-12 08:18",
         "2011-09-02 11:10",
         "2011-06-21 09:30",
         "2011-05-20 10:00",
         "2011-05-16 13:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MbgLantimeNGStatus_ObjectIdentity = ObjectIdentity
mbgLantimeNGStatus = _MbgLantimeNGStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0)
)
_MbgLtNgInfo_ObjectIdentity = ObjectIdentity
mbgLtNgInfo = _MbgLtNgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 0)
)


class _MbgLtNgSnmpSubagentVersion_Type(DisplayString):
    """Custom type mbgLtNgSnmpSubagentVersion based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgSnmpSubagentVersion_Object = MibScalar
mbgLtNgSnmpSubagentVersion = _MbgLtNgSnmpSubagentVersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 0, 1),
    _MbgLtNgSnmpSubagentVersion_Type()
)
mbgLtNgSnmpSubagentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgSnmpSubagentVersion.setStatus("current")


class _MbgLtNgFirmwareVersion_Type(DisplayString):
    """Custom type mbgLtNgFirmwareVersion based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgFirmwareVersion_Object = MibScalar
mbgLtNgFirmwareVersion = _MbgLtNgFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 0, 2),
    _MbgLtNgFirmwareVersion_Type()
)
mbgLtNgFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgFirmwareVersion.setStatus("current")


class _MbgLtNgSerialNumber_Type(DisplayString):
    """Custom type mbgLtNgSerialNumber based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgSerialNumber_Object = MibScalar
mbgLtNgSerialNumber = _MbgLtNgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 0, 3),
    _MbgLtNgSerialNumber_Type()
)
mbgLtNgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgSerialNumber.setStatus("current")


class _MbgLtNgSubagentTimeticks_Type(Counter64):
    """Custom type mbgLtNgSubagentTimeticks based on Counter64"""
    defaultValue = 0


_MbgLtNgSubagentTimeticks_Object = MibScalar
mbgLtNgSubagentTimeticks = _MbgLtNgSubagentTimeticks_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 0, 4),
    _MbgLtNgSubagentTimeticks_Type()
)
mbgLtNgSubagentTimeticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgSubagentTimeticks.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgSubagentTimeticks.setUnits("sec")


class _MbgLtNgCpuSerialNumber_Type(DisplayString):
    """Custom type mbgLtNgCpuSerialNumber based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCpuSerialNumber_Object = MibScalar
mbgLtNgCpuSerialNumber = _MbgLtNgCpuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 0, 5),
    _MbgLtNgCpuSerialNumber_Type()
)
mbgLtNgCpuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCpuSerialNumber.setStatus("current")
_MbgLtNgRefclock_ObjectIdentity = ObjectIdentity
mbgLtNgRefclock = _MbgLtNgRefclock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1)
)


class _MbgLtNgNumberOfRefclocks_Type(Unsigned32):
    """Custom type mbgLtNgNumberOfRefclocks based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbgLtNgNumberOfRefclocks_Type.__name__ = "Unsigned32"
_MbgLtNgNumberOfRefclocks_Object = MibScalar
mbgLtNgNumberOfRefclocks = _MbgLtNgNumberOfRefclocks_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 1),
    _MbgLtNgNumberOfRefclocks_Type()
)
mbgLtNgNumberOfRefclocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNumberOfRefclocks.setStatus("current")
_MbgLtNgRefclockTable_Object = MibTable
mbgLtNgRefclockTable = _MbgLtNgRefclockTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2)
)
if mibBuilder.loadTexts:
    mbgLtNgRefclockTable.setStatus("current")
_MbgLtNgRefclockTableEntry_Object = MibTableRow
mbgLtNgRefclockTableEntry = _MbgLtNgRefclockTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1)
)
mbgLtNgRefclockTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgRefclockTableEntry.setStatus("current")


class _MbgLtNgRefclockIndex_Type(Unsigned32):
    """Custom type mbgLtNgRefclockIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MbgLtNgRefclockIndex_Type.__name__ = "Unsigned32"
_MbgLtNgRefclockIndex_Object = MibTableColumn
mbgLtNgRefclockIndex = _MbgLtNgRefclockIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 1),
    _MbgLtNgRefclockIndex_Type()
)
mbgLtNgRefclockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgRefclockIndex.setStatus("current")


class _MbgLtNgRefclockType_Type(Integer32):
    """Custom type mbgLtNgRefclockType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
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
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61)
        )
    )
    namedValues = NamedValues(
        *(("am511", 16),
          ("bpe", 49),
          ("cpe180", 42),
          ("dcf600HS", 46),
          ("dcf600RS", 47),
          ("esi180", 41),
          ("fdm180", 58),
          ("frc511PEX", 22),
          ("gen170", 23),
          ("gln170", 31),
          ("gln180Pex", 50),
          ("gps161", 8),
          ("gps162", 20),
          ("gps163", 6),
          ("gps164", 11),
          ("gps166", 1),
          ("gps167", 2),
          ("gps167PC", 4),
          ("gps167PCI", 5),
          ("gps167SV", 3),
          ("gps168PCI", 7),
          ("gps169PCI", 9),
          ("gps170", 14),
          ("gps170PCI", 12),
          ("gps170PEX", 19),
          ("gps180", 30),
          ("gps180AMC", 40),
          ("gps180HS", 39),
          ("gps180PEX", 32),
          ("grc170", 18),
          ("grc180", 44),
          ("jjy511", 27),
          ("jjy600", 38),
          ("liu", 45),
          ("lneGb", 53),
          ("lnePpg180", 54),
          ("lno180", 43),
          ("mdu300", 56),
          ("mgr170", 26),
          ("mgr180", 35),
          ("mri", 48),
          ("msf511", 17),
          ("msf600", 36),
          ("n2x", 51),
          ("ptp270PEX", 21),
          ("pzf180", 60),
          ("pzf180PEX", 34),
          ("pzf511", 13),
          ("pzf600", 28),
          ("rel1000", 61),
          ("rsc180", 52),
          ("scg", 55),
          ("sdi", 57),
          ("spt", 59),
          ("tcr167PCI", 10),
          ("tcr170PEX", 24),
          ("tcr180PEX", 33),
          ("tcr511", 15),
          ("tcr600", 29),
          ("unknown", 0),
          ("wwvb511", 25),
          ("wwvb600", 37))
    )


_MbgLtNgRefclockType_Type.__name__ = "Integer32"
_MbgLtNgRefclockType_Object = MibTableColumn
mbgLtNgRefclockType = _MbgLtNgRefclockType_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 2),
    _MbgLtNgRefclockType_Type()
)
mbgLtNgRefclockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockType.setStatus("current")


class _MbgLtNgRefclockUsage_Type(Integer32):
    """Custom type mbgLtNgRefclockUsage based on Integer32"""
    defaultValue = 0

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
        *(("compare", 2),
          ("notAvailable", 0),
          ("primary", 3),
          ("secondary", 1))
    )


_MbgLtNgRefclockUsage_Type.__name__ = "Integer32"
_MbgLtNgRefclockUsage_Object = MibTableColumn
mbgLtNgRefclockUsage = _MbgLtNgRefclockUsage_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 3),
    _MbgLtNgRefclockUsage_Type()
)
mbgLtNgRefclockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockUsage.setStatus("current")


class _MbgLtNgRefclockState_Type(Integer32):
    """Custom type mbgLtNgRefclockState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("notSynchronized", 2),
          ("synchronized", 1))
    )


_MbgLtNgRefclockState_Type.__name__ = "Integer32"
_MbgLtNgRefclockState_Object = MibTableColumn
mbgLtNgRefclockState = _MbgLtNgRefclockState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 4),
    _MbgLtNgRefclockState_Type()
)
mbgLtNgRefclockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockState.setStatus("current")


class _MbgLtNgRefclockSubstate_Type(Integer32):
    """Custom type mbgLtNgRefclockSubstate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              50,
              51,
              52,
              100,
              101,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167)
        )
    )
    namedValues = NamedValues(
        *(("gpsAntennaDisconnected", 3),
          ("gpsAntennaShortCircuit", 6),
          ("gpsColdBoot", 5),
          ("gpsSync", 1),
          ("gpsTracking", 2),
          ("gpsWarmBoot", 4),
          ("lwNeverSync", 50),
          ("lwNotSync", 51),
          ("lwSync", 52),
          ("mrs10MhzPpsInSync", 153),
          ("mrs10MhzSync", 151),
          ("mrsDcf77PzfSync", 162),
          ("mrsExtOscSync", 166),
          ("mrsFixedFreqInSync", 158),
          ("mrsGlonassGpsSync", 164),
          ("mrsGpsSync", 150),
          ("mrsHavequickSync", 165),
          ("mrsIntOscSync", 167),
          ("mrsIrigSync", 154),
          ("mrsLongwaveSync", 163),
          ("mrsNtpSync", 155),
          ("mrsPpsInSync", 152),
          ("mrsPpsStringSync", 159),
          ("mrsPtpIeee1588Sync", 156),
          ("mrsPtpOverE1Sync", 157),
          ("mrsRefNone", -1),
          ("mrsReserved", 161),
          ("mrsVarFreqGpioSync", 160),
          ("notAvailable", 0),
          ("tcrNotSync", 100),
          ("tcrSync", 101))
    )


_MbgLtNgRefclockSubstate_Type.__name__ = "Integer32"
_MbgLtNgRefclockSubstate_Object = MibTableColumn
mbgLtNgRefclockSubstate = _MbgLtNgRefclockSubstate_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 5),
    _MbgLtNgRefclockSubstate_Type()
)
mbgLtNgRefclockSubstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockSubstate.setStatus("current")


class _MbgLtNgRefclockStatusA_Type(Unsigned32):
    """Custom type mbgLtNgRefclockStatusA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MbgLtNgRefclockStatusA_Type.__name__ = "Unsigned32"
_MbgLtNgRefclockStatusA_Object = MibTableColumn
mbgLtNgRefclockStatusA = _MbgLtNgRefclockStatusA_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 6),
    _MbgLtNgRefclockStatusA_Type()
)
mbgLtNgRefclockStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockStatusA.setStatus("current")


class _MbgLtNgRefclockMaxStatusA_Type(Unsigned32):
    """Custom type mbgLtNgRefclockMaxStatusA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MbgLtNgRefclockMaxStatusA_Type.__name__ = "Unsigned32"
_MbgLtNgRefclockMaxStatusA_Object = MibTableColumn
mbgLtNgRefclockMaxStatusA = _MbgLtNgRefclockMaxStatusA_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 7),
    _MbgLtNgRefclockMaxStatusA_Type()
)
mbgLtNgRefclockMaxStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockMaxStatusA.setStatus("current")


class _MbgLtNgRefclockStatusB_Type(Unsigned32):
    """Custom type mbgLtNgRefclockStatusB based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MbgLtNgRefclockStatusB_Type.__name__ = "Unsigned32"
_MbgLtNgRefclockStatusB_Object = MibTableColumn
mbgLtNgRefclockStatusB = _MbgLtNgRefclockStatusB_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 8),
    _MbgLtNgRefclockStatusB_Type()
)
mbgLtNgRefclockStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockStatusB.setStatus("current")


class _MbgLtNgRefclockMaxStatusB_Type(Unsigned32):
    """Custom type mbgLtNgRefclockMaxStatusB based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MbgLtNgRefclockMaxStatusB_Type.__name__ = "Unsigned32"
_MbgLtNgRefclockMaxStatusB_Object = MibTableColumn
mbgLtNgRefclockMaxStatusB = _MbgLtNgRefclockMaxStatusB_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 9),
    _MbgLtNgRefclockMaxStatusB_Type()
)
mbgLtNgRefclockMaxStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockMaxStatusB.setStatus("current")


class _MbgLtNgRefclockAdditionalInfo_Type(Integer32):
    """Custom type mbgLtNgRefclockAdditionalInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("leapSecondAnnounced", 1),
          ("notAvailable", 0))
    )


_MbgLtNgRefclockAdditionalInfo_Type.__name__ = "Integer32"
_MbgLtNgRefclockAdditionalInfo_Object = MibTableColumn
mbgLtNgRefclockAdditionalInfo = _MbgLtNgRefclockAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 10),
    _MbgLtNgRefclockAdditionalInfo_Type()
)
mbgLtNgRefclockAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockAdditionalInfo.setStatus("current")


class _MbgLtNgRefclockLeapSecondDate_Type(DisplayString):
    """Custom type mbgLtNgRefclockLeapSecondDate based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgRefclockLeapSecondDate_Object = MibTableColumn
mbgLtNgRefclockLeapSecondDate = _MbgLtNgRefclockLeapSecondDate_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 2, 1, 11),
    _MbgLtNgRefclockLeapSecondDate_Type()
)
mbgLtNgRefclockLeapSecondDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockLeapSecondDate.setStatus("current")
_MbgLtNgRefclockGpsTable_Object = MibTable
mbgLtNgRefclockGpsTable = _MbgLtNgRefclockGpsTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 3)
)
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsTable.setStatus("current")
_MbgLtNgRefclockGpsTableEntry_Object = MibTableRow
mbgLtNgRefclockGpsTableEntry = _MbgLtNgRefclockGpsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 3, 1)
)
mbgLtNgRefclockGpsTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockGpsIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsTableEntry.setStatus("current")
_MbgLtNgRefclockGpsIndex_Type = Unsigned32
_MbgLtNgRefclockGpsIndex_Object = MibTableColumn
mbgLtNgRefclockGpsIndex = _MbgLtNgRefclockGpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 3, 1, 1),
    _MbgLtNgRefclockGpsIndex_Type()
)
mbgLtNgRefclockGpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsIndex.setStatus("current")


class _MbgLtNgRefclockGpsLatitude_Type(DisplayString):
    """Custom type mbgLtNgRefclockGpsLatitude based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgRefclockGpsLatitude_Object = MibTableColumn
mbgLtNgRefclockGpsLatitude = _MbgLtNgRefclockGpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 3, 1, 2),
    _MbgLtNgRefclockGpsLatitude_Type()
)
mbgLtNgRefclockGpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsLatitude.setStatus("current")


class _MbgLtNgRefclockGpsLongitude_Type(DisplayString):
    """Custom type mbgLtNgRefclockGpsLongitude based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgRefclockGpsLongitude_Object = MibTableColumn
mbgLtNgRefclockGpsLongitude = _MbgLtNgRefclockGpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 3, 1, 3),
    _MbgLtNgRefclockGpsLongitude_Type()
)
mbgLtNgRefclockGpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsLongitude.setStatus("current")


class _MbgLtNgRefclockGpsAltitude_Type(Integer32):
    """Custom type mbgLtNgRefclockGpsAltitude based on Integer32"""
    defaultValue = -1


_MbgLtNgRefclockGpsAltitude_Object = MibTableColumn
mbgLtNgRefclockGpsAltitude = _MbgLtNgRefclockGpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 3, 1, 4),
    _MbgLtNgRefclockGpsAltitude_Type()
)
mbgLtNgRefclockGpsAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsAltitude.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsAltitude.setUnits("m")


class _MbgLtNgRefclockGpsTdop_Type(DisplayString):
    """Custom type mbgLtNgRefclockGpsTdop based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgRefclockGpsTdop_Object = MibTableColumn
mbgLtNgRefclockGpsTdop = _MbgLtNgRefclockGpsTdop_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 3, 1, 5),
    _MbgLtNgRefclockGpsTdop_Type()
)
mbgLtNgRefclockGpsTdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsTdop.setStatus("current")


class _MbgLtNgRefclockGpsPdop_Type(DisplayString):
    """Custom type mbgLtNgRefclockGpsPdop based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgRefclockGpsPdop_Object = MibTableColumn
mbgLtNgRefclockGpsPdop = _MbgLtNgRefclockGpsPdop_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 3, 1, 6),
    _MbgLtNgRefclockGpsPdop_Type()
)
mbgLtNgRefclockGpsPdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsPdop.setStatus("current")


class _MbgLtNgRefclockGpsUtcOffset_Type(Integer32):
    """Custom type mbgLtNgRefclockGpsUtcOffset based on Integer32"""
    defaultValue = -1


_MbgLtNgRefclockGpsUtcOffset_Object = MibTableColumn
mbgLtNgRefclockGpsUtcOffset = _MbgLtNgRefclockGpsUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 3, 1, 7),
    _MbgLtNgRefclockGpsUtcOffset_Type()
)
mbgLtNgRefclockGpsUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsUtcOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsUtcOffset.setUnits("sec")


class _MbgLtNgRefclockTimeDiff_Type(Integer32):
    """Custom type mbgLtNgRefclockTimeDiff based on Integer32"""
    defaultValue = 0


_MbgLtNgRefclockTimeDiff_Object = MibScalar
mbgLtNgRefclockTimeDiff = _MbgLtNgRefclockTimeDiff_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 4),
    _MbgLtNgRefclockTimeDiff_Type()
)
mbgLtNgRefclockTimeDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockTimeDiff.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgRefclockTimeDiff.setUnits("ms")


class _MbgLtNgRefclockGpsPos_Type(DisplayString):
    """Custom type mbgLtNgRefclockGpsPos based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgRefclockGpsPos_Object = MibScalar
mbgLtNgRefclockGpsPos = _MbgLtNgRefclockGpsPos_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 1, 5),
    _MbgLtNgRefclockGpsPos_Type()
)
mbgLtNgRefclockGpsPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgRefclockGpsPos.setStatus("current")
_MbgLtNgNtp_ObjectIdentity = ObjectIdentity
mbgLtNgNtp = _MbgLtNgNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2)
)


class _MbgLtNgNtpCurrentState_Type(Integer32):
    """Custom type mbgLtNgNtpCurrentState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("notSynchronized", 1),
          ("synchronized", 2))
    )


_MbgLtNgNtpCurrentState_Type.__name__ = "Integer32"
_MbgLtNgNtpCurrentState_Object = MibScalar
mbgLtNgNtpCurrentState = _MbgLtNgNtpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 1),
    _MbgLtNgNtpCurrentState_Type()
)
mbgLtNgNtpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpCurrentState.setStatus("current")


class _MbgLtNgNtpStratum_Type(Integer32):
    """Custom type mbgLtNgNtpStratum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MbgLtNgNtpStratum_Type.__name__ = "Integer32"
_MbgLtNgNtpStratum_Object = MibScalar
mbgLtNgNtpStratum = _MbgLtNgNtpStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 2),
    _MbgLtNgNtpStratum_Type()
)
mbgLtNgNtpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpStratum.setStatus("current")


class _MbgLtNgNtpRefclockName_Type(DisplayString):
    """Custom type mbgLtNgNtpRefclockName based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgNtpRefclockName_Object = MibScalar
mbgLtNgNtpRefclockName = _MbgLtNgNtpRefclockName_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 3),
    _MbgLtNgNtpRefclockName_Type()
)
mbgLtNgNtpRefclockName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpRefclockName.setStatus("current")


class _MbgLtNgNtpRefclockOffset_Type(DisplayString):
    """Custom type mbgLtNgNtpRefclockOffset based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgNtpRefclockOffset_Object = MibScalar
mbgLtNgNtpRefclockOffset = _MbgLtNgNtpRefclockOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 4),
    _MbgLtNgNtpRefclockOffset_Type()
)
mbgLtNgNtpRefclockOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpRefclockOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgNtpRefclockOffset.setUnits("ms")


class _MbgLtNgNtpVersion_Type(DisplayString):
    """Custom type mbgLtNgNtpVersion based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgNtpVersion_Object = MibScalar
mbgLtNgNtpVersion = _MbgLtNgNtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 5),
    _MbgLtNgNtpVersion_Type()
)
mbgLtNgNtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpVersion.setStatus("current")
_MbgLtNgNtpClientCounter_ObjectIdentity = ObjectIdentity
mbgLtNgNtpClientCounter = _MbgLtNgNtpClientCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 8)
)


class _MbgLtNgNtpCCStartedAt_Type(Counter64):
    """Custom type mbgLtNgNtpCCStartedAt based on Counter64"""
    defaultValue = 0


_MbgLtNgNtpCCStartedAt_Object = MibScalar
mbgLtNgNtpCCStartedAt = _MbgLtNgNtpCCStartedAt_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 8, 1),
    _MbgLtNgNtpCCStartedAt_Type()
)
mbgLtNgNtpCCStartedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpCCStartedAt.setStatus("current")


class _MbgLtNgNtpCCDuration_Type(Unsigned32):
    """Custom type mbgLtNgNtpCCDuration based on Unsigned32"""
    defaultValue = 0


_MbgLtNgNtpCCDuration_Object = MibScalar
mbgLtNgNtpCCDuration = _MbgLtNgNtpCCDuration_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 8, 2),
    _MbgLtNgNtpCCDuration_Type()
)
mbgLtNgNtpCCDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpCCDuration.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgNtpCCDuration.setUnits("sec")


class _MbgLtNgNtpCCNumberOfClients_Type(Unsigned32):
    """Custom type mbgLtNgNtpCCNumberOfClients based on Unsigned32"""
    defaultValue = 0


_MbgLtNgNtpCCNumberOfClients_Object = MibScalar
mbgLtNgNtpCCNumberOfClients = _MbgLtNgNtpCCNumberOfClients_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 8, 3),
    _MbgLtNgNtpCCNumberOfClients_Type()
)
mbgLtNgNtpCCNumberOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpCCNumberOfClients.setStatus("current")


class _MbgLtNgNtpCCTotalRequests_Type(Counter64):
    """Custom type mbgLtNgNtpCCTotalRequests based on Counter64"""
    defaultValue = 0


_MbgLtNgNtpCCTotalRequests_Object = MibScalar
mbgLtNgNtpCCTotalRequests = _MbgLtNgNtpCCTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 8, 4),
    _MbgLtNgNtpCCTotalRequests_Type()
)
mbgLtNgNtpCCTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpCCTotalRequests.setStatus("current")


class _MbgLtNgNtpCCTotalRequestsCurrentDay_Type(Counter64):
    """Custom type mbgLtNgNtpCCTotalRequestsCurrentDay based on Counter64"""
    defaultValue = 0


_MbgLtNgNtpCCTotalRequestsCurrentDay_Object = MibScalar
mbgLtNgNtpCCTotalRequestsCurrentDay = _MbgLtNgNtpCCTotalRequestsCurrentDay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 8, 5),
    _MbgLtNgNtpCCTotalRequestsCurrentDay_Type()
)
mbgLtNgNtpCCTotalRequestsCurrentDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpCCTotalRequestsCurrentDay.setStatus("current")


class _MbgLtNgNtpCCTotalRequestsLastHour_Type(Counter64):
    """Custom type mbgLtNgNtpCCTotalRequestsLastHour based on Counter64"""
    defaultValue = 0


_MbgLtNgNtpCCTotalRequestsLastHour_Object = MibScalar
mbgLtNgNtpCCTotalRequestsLastHour = _MbgLtNgNtpCCTotalRequestsLastHour_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 8, 6),
    _MbgLtNgNtpCCTotalRequestsLastHour_Type()
)
mbgLtNgNtpCCTotalRequestsLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpCCTotalRequestsLastHour.setStatus("current")


class _MbgLtNgNtpCCTotalRequestsLastMinute_Type(Counter64):
    """Custom type mbgLtNgNtpCCTotalRequestsLastMinute based on Counter64"""
    defaultValue = 0


_MbgLtNgNtpCCTotalRequestsLastMinute_Object = MibScalar
mbgLtNgNtpCCTotalRequestsLastMinute = _MbgLtNgNtpCCTotalRequestsLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 8, 7),
    _MbgLtNgNtpCCTotalRequestsLastMinute_Type()
)
mbgLtNgNtpCCTotalRequestsLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpCCTotalRequestsLastMinute.setStatus("current")


class _MbgLtNgNtpCCTodaysClients_Type(Unsigned32):
    """Custom type mbgLtNgNtpCCTodaysClients based on Unsigned32"""
    defaultValue = 0


_MbgLtNgNtpCCTodaysClients_Object = MibScalar
mbgLtNgNtpCCTodaysClients = _MbgLtNgNtpCCTodaysClients_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 8, 8),
    _MbgLtNgNtpCCTodaysClients_Type()
)
mbgLtNgNtpCCTodaysClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpCCTodaysClients.setStatus("current")
_MbgLtNgNtpMrs_ObjectIdentity = ObjectIdentity
mbgLtNgNtpMrs = _MbgLtNgNtpMrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 9)
)


class _MbgLtNgNtpMrsServer_Type(DisplayString):
    """Custom type mbgLtNgNtpMrsServer based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgNtpMrsServer_Object = MibScalar
mbgLtNgNtpMrsServer = _MbgLtNgNtpMrsServer_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 9, 1),
    _MbgLtNgNtpMrsServer_Type()
)
mbgLtNgNtpMrsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpMrsServer.setStatus("current")


class _MbgLtNgNtpMrsOffset_Type(DisplayString):
    """Custom type mbgLtNgNtpMrsOffset based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgNtpMrsOffset_Object = MibScalar
mbgLtNgNtpMrsOffset = _MbgLtNgNtpMrsOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 2, 9, 2),
    _MbgLtNgNtpMrsOffset_Type()
)
mbgLtNgNtpMrsOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNtpMrsOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgNtpMrsOffset.setUnits("sec")
_MbgLtNgPtp_ObjectIdentity = ObjectIdentity
mbgLtNgPtp = _MbgLtNgPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3)
)


class _MbgLtNgPtpNumberOfModules_Type(Unsigned32):
    """Custom type mbgLtNgPtpNumberOfModules based on Unsigned32"""
    defaultValue = 0


_MbgLtNgPtpNumberOfModules_Object = MibScalar
mbgLtNgPtpNumberOfModules = _MbgLtNgPtpNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 1),
    _MbgLtNgPtpNumberOfModules_Type()
)
mbgLtNgPtpNumberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpNumberOfModules.setStatus("current")
_MbgLtNgPtpTable_Object = MibTable
mbgLtNgPtpTable = _MbgLtNgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2)
)
if mibBuilder.loadTexts:
    mbgLtNgPtpTable.setStatus("current")
_MbgLtNgPtpTableEntry_Object = MibTableRow
mbgLtNgPtpTableEntry = _MbgLtNgPtpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1)
)
mbgLtNgPtpTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgPtpIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgPtpTableEntry.setStatus("current")
_MbgLtNgPtpIndex_Type = Unsigned32
_MbgLtNgPtpIndex_Object = MibTableColumn
mbgLtNgPtpIndex = _MbgLtNgPtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 1),
    _MbgLtNgPtpIndex_Type()
)
mbgLtNgPtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgPtpIndex.setStatus("current")


class _MbgLtNgPtpMode_Type(Integer32):
    """Custom type mbgLtNgPtpMode based on Integer32"""
    defaultValue = 0

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
        *(("master", 2),
          ("notAvailable", 0),
          ("ordinary", 4),
          ("slave", 3),
          ("stopped", 1))
    )


_MbgLtNgPtpMode_Type.__name__ = "Integer32"
_MbgLtNgPtpMode_Object = MibTableColumn
mbgLtNgPtpMode = _MbgLtNgPtpMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 2),
    _MbgLtNgPtpMode_Type()
)
mbgLtNgPtpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpMode.setStatus("obsolete")


class _MbgLtNgPtpPortState_Type(Integer32):
    """Custom type mbgLtNgPtpPortState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("disabled", 3),
          ("faulty", 2),
          ("initializing", 1),
          ("listening", 4),
          ("master", 6),
          ("passive", 7),
          ("preMaster", 5),
          ("slave", 9),
          ("uncalibrated", 8),
          ("uninitialized", 0))
    )


_MbgLtNgPtpPortState_Type.__name__ = "Integer32"
_MbgLtNgPtpPortState_Object = MibTableColumn
mbgLtNgPtpPortState = _MbgLtNgPtpPortState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 3),
    _MbgLtNgPtpPortState_Type()
)
mbgLtNgPtpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpPortState.setStatus("current")


class _MbgLtNgPtpGrandmasterMac_Type(DisplayString):
    """Custom type mbgLtNgPtpGrandmasterMac based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgPtpGrandmasterMac_Object = MibTableColumn
mbgLtNgPtpGrandmasterMac = _MbgLtNgPtpGrandmasterMac_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 4),
    _MbgLtNgPtpGrandmasterMac_Type()
)
mbgLtNgPtpGrandmasterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpGrandmasterMac.setStatus("current")


class _MbgLtNgPtpClockAccuracy_Type(Integer32):
    """Custom type mbgLtNgPtpClockAccuracy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
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
              254)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("timeAccurateTo100ms", 45),
          ("timeAccurateTo100ns", 33),
          ("timeAccurateTo100us", 39),
          ("timeAccurateTo10ms", 43),
          ("timeAccurateTo10s", 48),
          ("timeAccurateTo10us", 37),
          ("timeAccurateTo1ms", 41),
          ("timeAccurateTo1s", 47),
          ("timeAccurateTo1us", 35),
          ("timeAccurateTo250ms", 46),
          ("timeAccurateTo250ns", 34),
          ("timeAccurateTo250us", 40),
          ("timeAccurateTo25ms", 44),
          ("timeAccurateTo25ns", 32),
          ("timeAccurateTo25us", 38),
          ("timeAccurateTo2Point5us", 36),
          ("timeAccurateTo2to5ms", 42),
          ("timeAccurateToGT10s", 49),
          ("timeAccurateToUnknown", 254))
    )


_MbgLtNgPtpClockAccuracy_Type.__name__ = "Integer32"
_MbgLtNgPtpClockAccuracy_Object = MibTableColumn
mbgLtNgPtpClockAccuracy = _MbgLtNgPtpClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 5),
    _MbgLtNgPtpClockAccuracy_Type()
)
mbgLtNgPtpClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpClockAccuracy.setStatus("current")


class _MbgLtNgPtpClockClass_Type(Unsigned32):
    """Custom type mbgLtNgPtpClockClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgLtNgPtpClockClass_Type.__name__ = "Unsigned32"
_MbgLtNgPtpClockClass_Object = MibTableColumn
mbgLtNgPtpClockClass = _MbgLtNgPtpClockClass_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 6),
    _MbgLtNgPtpClockClass_Type()
)
mbgLtNgPtpClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpClockClass.setStatus("current")


class _MbgLtNgPtpTimeSource_Type(Integer32):
    """Custom type mbgLtNgPtpTimeSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("handSet", 96),
          ("internalOscillator", 160),
          ("notAvailable", 0),
          ("ntp", 80),
          ("other", 144),
          ("ptp", 64),
          ("terrestrialRadio", 48))
    )


_MbgLtNgPtpTimeSource_Type.__name__ = "Integer32"
_MbgLtNgPtpTimeSource_Object = MibTableColumn
mbgLtNgPtpTimeSource = _MbgLtNgPtpTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 7),
    _MbgLtNgPtpTimeSource_Type()
)
mbgLtNgPtpTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpTimeSource.setStatus("current")


class _MbgLtNgPtpUtcOffset_Type(Unsigned32):
    """Custom type mbgLtNgPtpUtcOffset based on Unsigned32"""
    defaultValue = 35


_MbgLtNgPtpUtcOffset_Object = MibTableColumn
mbgLtNgPtpUtcOffset = _MbgLtNgPtpUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 8),
    _MbgLtNgPtpUtcOffset_Type()
)
mbgLtNgPtpUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpUtcOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgPtpUtcOffset.setUnits("seconds")


class _MbgLtNgPtpTimeSeconds_Type(Counter64):
    """Custom type mbgLtNgPtpTimeSeconds based on Counter64"""
    defaultValue = 0


_MbgLtNgPtpTimeSeconds_Object = MibTableColumn
mbgLtNgPtpTimeSeconds = _MbgLtNgPtpTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 9),
    _MbgLtNgPtpTimeSeconds_Type()
)
mbgLtNgPtpTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpTimeSeconds.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgPtpTimeSeconds.setUnits("seconds")


class _MbgLtNgPtpTsuTime_Type(DisplayString):
    """Custom type mbgLtNgPtpTsuTime based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgPtpTsuTime_Object = MibTableColumn
mbgLtNgPtpTsuTime = _MbgLtNgPtpTsuTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 10),
    _MbgLtNgPtpTsuTime_Type()
)
mbgLtNgPtpTsuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpTsuTime.setStatus("current")


class _MbgLtNgPtpSysTime_Type(DisplayString):
    """Custom type mbgLtNgPtpSysTime based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgPtpSysTime_Object = MibTableColumn
mbgLtNgPtpSysTime = _MbgLtNgPtpSysTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 11),
    _MbgLtNgPtpSysTime_Type()
)
mbgLtNgPtpSysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpSysTime.setStatus("current")


class _MbgLtNgPtpPortLinkup_Type(MeinbergSwitch):
    """Custom type mbgLtNgPtpPortLinkup based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgPtpPortLinkup_Object = MibTableColumn
mbgLtNgPtpPortLinkup = _MbgLtNgPtpPortLinkup_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 12),
    _MbgLtNgPtpPortLinkup_Type()
)
mbgLtNgPtpPortLinkup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpPortLinkup.setStatus("current")


class _MbgLtNgPtpOffsetFromGM_Type(DisplayString):
    """Custom type mbgLtNgPtpOffsetFromGM based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgPtpOffsetFromGM_Object = MibTableColumn
mbgLtNgPtpOffsetFromGM = _MbgLtNgPtpOffsetFromGM_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 13),
    _MbgLtNgPtpOffsetFromGM_Type()
)
mbgLtNgPtpOffsetFromGM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpOffsetFromGM.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgPtpOffsetFromGM.setUnits("ns")


class _MbgLtNgPtpPathDelay_Type(DisplayString):
    """Custom type mbgLtNgPtpPathDelay based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgPtpPathDelay_Object = MibTableColumn
mbgLtNgPtpPathDelay = _MbgLtNgPtpPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 14),
    _MbgLtNgPtpPathDelay_Type()
)
mbgLtNgPtpPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgPtpPathDelay.setUnits("ns")


class _MbgLtNgPtpDelayMec_Type(Integer32):
    """Custom type mbgLtNgPtpDelayMec based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("end2End", 0),
          ("peer2Peer", 1))
    )


_MbgLtNgPtpDelayMec_Type.__name__ = "Integer32"
_MbgLtNgPtpDelayMec_Object = MibTableColumn
mbgLtNgPtpDelayMec = _MbgLtNgPtpDelayMec_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 15),
    _MbgLtNgPtpDelayMec_Type()
)
mbgLtNgPtpDelayMec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpDelayMec.setStatus("current")


class _MbgLtNgPtpDomain_Type(Unsigned32):
    """Custom type mbgLtNgPtpDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgLtNgPtpDomain_Type.__name__ = "Unsigned32"
_MbgLtNgPtpDomain_Object = MibTableColumn
mbgLtNgPtpDomain = _MbgLtNgPtpDomain_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 16),
    _MbgLtNgPtpDomain_Type()
)
mbgLtNgPtpDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpDomain.setStatus("current")


class _MbgLtNgPtpGrandmasterUuid_Type(DisplayString):
    """Custom type mbgLtNgPtpGrandmasterUuid based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgPtpGrandmasterUuid_Object = MibTableColumn
mbgLtNgPtpGrandmasterUuid = _MbgLtNgPtpGrandmasterUuid_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 17),
    _MbgLtNgPtpGrandmasterUuid_Type()
)
mbgLtNgPtpGrandmasterUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpGrandmasterUuid.setStatus("current")


class _MbgLtNgPtpLocalMac_Type(DisplayString):
    """Custom type mbgLtNgPtpLocalMac based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgPtpLocalMac_Object = MibTableColumn
mbgLtNgPtpLocalMac = _MbgLtNgPtpLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 18),
    _MbgLtNgPtpLocalMac_Type()
)
mbgLtNgPtpLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpLocalMac.setStatus("current")


class _MbgLtNgPtpDelayAsymmetry_Type(DisplayString):
    """Custom type mbgLtNgPtpDelayAsymmetry based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgPtpDelayAsymmetry_Object = MibTableColumn
mbgLtNgPtpDelayAsymmetry = _MbgLtNgPtpDelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 19),
    _MbgLtNgPtpDelayAsymmetry_Type()
)
mbgLtNgPtpDelayAsymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpDelayAsymmetry.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgPtpDelayAsymmetry.setUnits("ns")


class _MbgLtNgPtpAvail_Type(Integer32):
    """Custom type mbgLtNgPtpAvail based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MbgLtNgPtpAvail_Type.__name__ = "Integer32"
_MbgLtNgPtpAvail_Object = MibTableColumn
mbgLtNgPtpAvail = _MbgLtNgPtpAvail_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 3, 2, 1, 20),
    _MbgLtNgPtpAvail_Type()
)
mbgLtNgPtpAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgPtpAvail.setStatus("current")
_MbgLtNgFdm_ObjectIdentity = ObjectIdentity
mbgLtNgFdm = _MbgLtNgFdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 4)
)


class _MbgLtNgFdmFreq_Type(Unsigned32):
    """Custom type mbgLtNgFdmFreq based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(45000, 65000),
    )


_MbgLtNgFdmFreq_Type.__name__ = "Unsigned32"
_MbgLtNgFdmFreq_Object = MibScalar
mbgLtNgFdmFreq = _MbgLtNgFdmFreq_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 4, 1),
    _MbgLtNgFdmFreq_Type()
)
mbgLtNgFdmFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgFdmFreq.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgFdmFreq.setUnits("mHz")


class _MbgLtNgFdmFreqDev_Type(Integer32):
    """Custom type mbgLtNgFdmFreqDev based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15000, 15000),
    )


_MbgLtNgFdmFreqDev_Type.__name__ = "Integer32"
_MbgLtNgFdmFreqDev_Object = MibScalar
mbgLtNgFdmFreqDev = _MbgLtNgFdmFreqDev_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 4, 2),
    _MbgLtNgFdmFreqDev_Type()
)
mbgLtNgFdmFreqDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgFdmFreqDev.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgFdmFreqDev.setUnits("mHz")


class _MbgLtNgFdmNomFreq_Type(Unsigned32):
    """Custom type mbgLtNgFdmNomFreq based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50000, 50000),
        ValueRangeConstraint(60000, 60000),
    )


_MbgLtNgFdmNomFreq_Type.__name__ = "Unsigned32"
_MbgLtNgFdmNomFreq_Object = MibScalar
mbgLtNgFdmNomFreq = _MbgLtNgFdmNomFreq_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 4, 3),
    _MbgLtNgFdmNomFreq_Type()
)
mbgLtNgFdmNomFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgFdmNomFreq.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgFdmNomFreq.setUnits("mHz")
_MbgLtNgSystemHardware_ObjectIdentity = ObjectIdentity
mbgLtNgSystemHardware = _MbgLtNgSystemHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5)
)
_MbgLtNgSysPowerSupply_ObjectIdentity = ObjectIdentity
mbgLtNgSysPowerSupply = _MbgLtNgSysPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 0)
)


class _MbgLtNgSysNumberOfPowerSupplies_Type(Unsigned32):
    """Custom type mbgLtNgSysNumberOfPowerSupplies based on Unsigned32"""
    defaultValue = 1


_MbgLtNgSysNumberOfPowerSupplies_Object = MibScalar
mbgLtNgSysNumberOfPowerSupplies = _MbgLtNgSysNumberOfPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 0, 1),
    _MbgLtNgSysNumberOfPowerSupplies_Type()
)
mbgLtNgSysNumberOfPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgSysNumberOfPowerSupplies.setStatus("current")
_MbgLtNgSysPsTable_Object = MibTable
mbgLtNgSysPsTable = _MbgLtNgSysPsTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 0, 2)
)
if mibBuilder.loadTexts:
    mbgLtNgSysPsTable.setStatus("current")
_MbgLtNgSysPsTableEntry_Object = MibTableRow
mbgLtNgSysPsTableEntry = _MbgLtNgSysPsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 0, 2, 1)
)
mbgLtNgSysPsTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgSysPsIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgSysPsTableEntry.setStatus("current")
_MbgLtNgSysPsIndex_Type = Unsigned32
_MbgLtNgSysPsIndex_Object = MibTableColumn
mbgLtNgSysPsIndex = _MbgLtNgSysPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 0, 2, 1, 1),
    _MbgLtNgSysPsIndex_Type()
)
mbgLtNgSysPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgSysPsIndex.setStatus("current")


class _MbgLtNgSysPsStatus_Type(Integer32):
    """Custom type mbgLtNgSysPsStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("notAvailable", 0),
          ("up", 2))
    )


_MbgLtNgSysPsStatus_Type.__name__ = "Integer32"
_MbgLtNgSysPsStatus_Object = MibTableColumn
mbgLtNgSysPsStatus = _MbgLtNgSysPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 0, 2, 1, 2),
    _MbgLtNgSysPsStatus_Type()
)
mbgLtNgSysPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgSysPsStatus.setStatus("current")
_MbgLtNgSysFan_ObjectIdentity = ObjectIdentity
mbgLtNgSysFan = _MbgLtNgSysFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 1)
)


class _MbgLtNgSysNumberOfFans_Type(Unsigned32):
    """Custom type mbgLtNgSysNumberOfFans based on Unsigned32"""
    defaultValue = 0


_MbgLtNgSysNumberOfFans_Object = MibScalar
mbgLtNgSysNumberOfFans = _MbgLtNgSysNumberOfFans_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 1, 1),
    _MbgLtNgSysNumberOfFans_Type()
)
mbgLtNgSysNumberOfFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgSysNumberOfFans.setStatus("current")
_MbgLtNgSysFanTable_Object = MibTable
mbgLtNgSysFanTable = _MbgLtNgSysFanTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 1, 2)
)
if mibBuilder.loadTexts:
    mbgLtNgSysFanTable.setStatus("current")
_MbgLtNgSysFanTableEntry_Object = MibTableRow
mbgLtNgSysFanTableEntry = _MbgLtNgSysFanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 1, 2, 1)
)
mbgLtNgSysFanTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgSysFanIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgSysFanTableEntry.setStatus("current")
_MbgLtNgSysFanIndex_Type = Unsigned32
_MbgLtNgSysFanIndex_Object = MibTableColumn
mbgLtNgSysFanIndex = _MbgLtNgSysFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 1, 2, 1, 1),
    _MbgLtNgSysFanIndex_Type()
)
mbgLtNgSysFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgSysFanIndex.setStatus("current")


class _MbgLtNgSysFanStatus_Type(Integer32):
    """Custom type mbgLtNgSysFanStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("off", 1),
          ("on", 2))
    )


_MbgLtNgSysFanStatus_Type.__name__ = "Integer32"
_MbgLtNgSysFanStatus_Object = MibTableColumn
mbgLtNgSysFanStatus = _MbgLtNgSysFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 1, 2, 1, 2),
    _MbgLtNgSysFanStatus_Type()
)
mbgLtNgSysFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgSysFanStatus.setStatus("current")


class _MbgLtNgSysFanError_Type(Integer32):
    """Custom type mbgLtNgSysFanError based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("notAvailable", 0),
          ("yes", 2))
    )


_MbgLtNgSysFanError_Type.__name__ = "Integer32"
_MbgLtNgSysFanError_Object = MibTableColumn
mbgLtNgSysFanError = _MbgLtNgSysFanError_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 1, 2, 1, 3),
    _MbgLtNgSysFanError_Type()
)
mbgLtNgSysFanError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgSysFanError.setStatus("current")
_MbgLtNgSysTemperature_ObjectIdentity = ObjectIdentity
mbgLtNgSysTemperature = _MbgLtNgSysTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 2)
)


class _MbgLtNgSysTempCelsius_Type(Unsigned32):
    """Custom type mbgLtNgSysTempCelsius based on Unsigned32"""
    defaultValue = 0


_MbgLtNgSysTempCelsius_Object = MibScalar
mbgLtNgSysTempCelsius = _MbgLtNgSysTempCelsius_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 5, 2, 1),
    _MbgLtNgSysTempCelsius_Type()
)
mbgLtNgSysTempCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgSysTempCelsius.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgSysTempCelsius.setUnits("C")
_MbgLtNgCluster_ObjectIdentity = ObjectIdentity
mbgLtNgCluster = _MbgLtNgCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6)
)


class _MbgLtNgNumberOfClusters_Type(Unsigned32):
    """Custom type mbgLtNgNumberOfClusters based on Unsigned32"""
    defaultValue = 0


_MbgLtNgNumberOfClusters_Object = MibScalar
mbgLtNgNumberOfClusters = _MbgLtNgNumberOfClusters_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 1),
    _MbgLtNgNumberOfClusters_Type()
)
mbgLtNgNumberOfClusters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgNumberOfClusters.setStatus("current")
_MbgLtNgClusterTable_Object = MibTable
mbgLtNgClusterTable = _MbgLtNgClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2)
)
if mibBuilder.loadTexts:
    mbgLtNgClusterTable.setStatus("current")
_MbgLtNgClusterTableEntry_Object = MibTableRow
mbgLtNgClusterTableEntry = _MbgLtNgClusterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1)
)
mbgLtNgClusterTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgClusterIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgClusterTableEntry.setStatus("current")
_MbgLtNgClusterIndex_Type = Unsigned32
_MbgLtNgClusterIndex_Object = MibTableColumn
mbgLtNgClusterIndex = _MbgLtNgClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 1),
    _MbgLtNgClusterIndex_Type()
)
mbgLtNgClusterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgClusterIndex.setStatus("current")


class _MbgLtNgClusterCommunicationIp_Type(DisplayString):
    """Custom type mbgLtNgClusterCommunicationIp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgClusterCommunicationIp_Object = MibTableColumn
mbgLtNgClusterCommunicationIp = _MbgLtNgClusterCommunicationIp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 2),
    _MbgLtNgClusterCommunicationIp_Type()
)
mbgLtNgClusterCommunicationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgClusterCommunicationIp.setStatus("current")


class _MbgLtNgClusterPortState_Type(Integer32):
    """Custom type mbgLtNgClusterPortState based on Integer32"""
    defaultValue = 0

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
        *(("listening", 3),
          ("master", 1),
          ("notAvailable", 0),
          ("slave", 2))
    )


_MbgLtNgClusterPortState_Type.__name__ = "Integer32"
_MbgLtNgClusterPortState_Object = MibTableColumn
mbgLtNgClusterPortState = _MbgLtNgClusterPortState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 3),
    _MbgLtNgClusterPortState_Type()
)
mbgLtNgClusterPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgClusterPortState.setStatus("current")


class _MbgLtNgClusterMasterSerial_Type(DisplayString):
    """Custom type mbgLtNgClusterMasterSerial based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgClusterMasterSerial_Object = MibTableColumn
mbgLtNgClusterMasterSerial = _MbgLtNgClusterMasterSerial_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 4),
    _MbgLtNgClusterMasterSerial_Type()
)
mbgLtNgClusterMasterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgClusterMasterSerial.setStatus("current")


class _MbgLtNgClusterMasterIp_Type(DisplayString):
    """Custom type mbgLtNgClusterMasterIp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgClusterMasterIp_Object = MibTableColumn
mbgLtNgClusterMasterIp = _MbgLtNgClusterMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 5),
    _MbgLtNgClusterMasterIp_Type()
)
mbgLtNgClusterMasterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgClusterMasterIp.setStatus("current")


class _MbgLtNgClusterMasterPriority_Type(Unsigned32):
    """Custom type mbgLtNgClusterMasterPriority based on Unsigned32"""
    defaultValue = 0


_MbgLtNgClusterMasterPriority_Object = MibTableColumn
mbgLtNgClusterMasterPriority = _MbgLtNgClusterMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 6),
    _MbgLtNgClusterMasterPriority_Type()
)
mbgLtNgClusterMasterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgClusterMasterPriority.setStatus("current")


class _MbgLtNgClusterClockClass_Type(Integer32):
    """Custom type mbgLtNgClusterClockClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("am", 5),
          ("e1", 10),
          ("gps", 3),
          ("irig", 6),
          ("notAvailable", 0),
          ("ntp", 9),
          ("pps", 7),
          ("ptp", 8),
          ("pzf", 4),
          ("rdt", 11))
    )


_MbgLtNgClusterClockClass_Type.__name__ = "Integer32"
_MbgLtNgClusterClockClass_Object = MibTableColumn
mbgLtNgClusterClockClass = _MbgLtNgClusterClockClass_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 7),
    _MbgLtNgClusterClockClass_Type()
)
mbgLtNgClusterClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgClusterClockClass.setStatus("current")


class _MbgLtNgClusterClockStatus_Type(Integer32):
    """Custom type mbgLtNgClusterClockStatus based on Integer32"""
    defaultValue = 0

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
        *(("antennaFailure", 3),
          ("freeRunningOrTracking", 2),
          ("invalid", 4),
          ("normalOperation", 1),
          ("notAvailable", 0))
    )


_MbgLtNgClusterClockStatus_Type.__name__ = "Integer32"
_MbgLtNgClusterClockStatus_Object = MibTableColumn
mbgLtNgClusterClockStatus = _MbgLtNgClusterClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 8),
    _MbgLtNgClusterClockStatus_Type()
)
mbgLtNgClusterClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgClusterClockStatus.setStatus("current")


class _MbgLtNgClusterReconfigurationState_Type(Integer32):
    """Custom type mbgLtNgClusterReconfigurationState based on Integer32"""
    defaultValue = 0

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
        *(("masterToSlave", 2),
          ("normal", 1),
          ("notAvailable", 0),
          ("slaveToMaster", 3))
    )


_MbgLtNgClusterReconfigurationState_Type.__name__ = "Integer32"
_MbgLtNgClusterReconfigurationState_Object = MibTableColumn
mbgLtNgClusterReconfigurationState = _MbgLtNgClusterReconfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 9),
    _MbgLtNgClusterReconfigurationState_Type()
)
mbgLtNgClusterReconfigurationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgClusterReconfigurationState.setStatus("current")


class _MbgLtNgClusterIsFalseticker_Type(Integer32):
    """Custom type mbgLtNgClusterIsFalseticker based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("notAvailable", 0),
          ("yes", 2))
    )


_MbgLtNgClusterIsFalseticker_Type.__name__ = "Integer32"
_MbgLtNgClusterIsFalseticker_Object = MibTableColumn
mbgLtNgClusterIsFalseticker = _MbgLtNgClusterIsFalseticker_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 6, 2, 1, 10),
    _MbgLtNgClusterIsFalseticker_Type()
)
mbgLtNgClusterIsFalseticker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgClusterIsFalseticker.setStatus("current")
_MbgLtNgMisc_ObjectIdentity = ObjectIdentity
mbgLtNgMisc = _MbgLtNgMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 7)
)
_MbgLtNgEthPortLinkTable_Object = MibTable
mbgLtNgEthPortLinkTable = _MbgLtNgEthPortLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 7, 1)
)
if mibBuilder.loadTexts:
    mbgLtNgEthPortLinkTable.setStatus("current")
_MbgLtNgEthPortLinkTableEntry_Object = MibTableRow
mbgLtNgEthPortLinkTableEntry = _MbgLtNgEthPortLinkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 7, 1, 1)
)
mbgLtNgEthPortLinkTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgEthPortLinkIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgEthPortLinkTableEntry.setStatus("current")
_MbgLtNgEthPortLinkIndex_Type = Unsigned32
_MbgLtNgEthPortLinkIndex_Object = MibTableColumn
mbgLtNgEthPortLinkIndex = _MbgLtNgEthPortLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 7, 1, 1, 1),
    _MbgLtNgEthPortLinkIndex_Type()
)
mbgLtNgEthPortLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgEthPortLinkIndex.setStatus("current")


class _MbgLtNgEthPortLinkState_Type(Integer32):
    """Custom type mbgLtNgEthPortLinkState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_MbgLtNgEthPortLinkState_Type.__name__ = "Integer32"
_MbgLtNgEthPortLinkState_Object = MibTableColumn
mbgLtNgEthPortLinkState = _MbgLtNgEthPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 0, 7, 1, 1, 2),
    _MbgLtNgEthPortLinkState_Type()
)
mbgLtNgEthPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgEthPortLinkState.setStatus("current")
_MbgLtNgConfig_ObjectIdentity = ObjectIdentity
mbgLtNgConfig = _MbgLtNgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1)
)
_MbgLtNgCfgEthernet_ObjectIdentity = ObjectIdentity
mbgLtNgCfgEthernet = _MbgLtNgCfgEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0)
)


class _MbgLtNgCfgEthernetHostname_Type(DisplayString):
    """Custom type mbgLtNgCfgEthernetHostname based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEthernetHostname_Object = MibScalar
mbgLtNgCfgEthernetHostname = _MbgLtNgCfgEthernetHostname_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 1),
    _MbgLtNgCfgEthernetHostname_Type()
)
mbgLtNgCfgEthernetHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEthernetHostname.setStatus("current")


class _MbgLtNgCfgEthernetDomain_Type(DisplayString):
    """Custom type mbgLtNgCfgEthernetDomain based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEthernetDomain_Object = MibScalar
mbgLtNgCfgEthernetDomain = _MbgLtNgCfgEthernetDomain_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 2),
    _MbgLtNgCfgEthernetDomain_Type()
)
mbgLtNgCfgEthernetDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEthernetDomain.setStatus("current")


class _MbgLtNgCfgEthernetNameserver1_Type(DisplayString):
    """Custom type mbgLtNgCfgEthernetNameserver1 based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEthernetNameserver1_Object = MibScalar
mbgLtNgCfgEthernetNameserver1 = _MbgLtNgCfgEthernetNameserver1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 3),
    _MbgLtNgCfgEthernetNameserver1_Type()
)
mbgLtNgCfgEthernetNameserver1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEthernetNameserver1.setStatus("current")


class _MbgLtNgCfgEthernetNameserver2_Type(DisplayString):
    """Custom type mbgLtNgCfgEthernetNameserver2 based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEthernetNameserver2_Object = MibScalar
mbgLtNgCfgEthernetNameserver2 = _MbgLtNgCfgEthernetNameserver2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 4),
    _MbgLtNgCfgEthernetNameserver2_Type()
)
mbgLtNgCfgEthernetNameserver2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEthernetNameserver2.setStatus("current")


class _MbgLtNgCfgEthernetIpv4Gateway_Type(DisplayString):
    """Custom type mbgLtNgCfgEthernetIpv4Gateway based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEthernetIpv4Gateway_Object = MibScalar
mbgLtNgCfgEthernetIpv4Gateway = _MbgLtNgCfgEthernetIpv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 5),
    _MbgLtNgCfgEthernetIpv4Gateway_Type()
)
mbgLtNgCfgEthernetIpv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEthernetIpv4Gateway.setStatus("current")


class _MbgLtNgCfgEthernetIpv6Gateway_Type(DisplayString):
    """Custom type mbgLtNgCfgEthernetIpv6Gateway based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEthernetIpv6Gateway_Object = MibScalar
mbgLtNgCfgEthernetIpv6Gateway = _MbgLtNgCfgEthernetIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 6),
    _MbgLtNgCfgEthernetIpv6Gateway_Type()
)
mbgLtNgCfgEthernetIpv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEthernetIpv6Gateway.setStatus("current")


class _MbgLtNgCfgNumberOfPhysicalIf_Type(Unsigned32):
    """Custom type mbgLtNgCfgNumberOfPhysicalIf based on Unsigned32"""
    defaultValue = 0


_MbgLtNgCfgNumberOfPhysicalIf_Object = MibScalar
mbgLtNgCfgNumberOfPhysicalIf = _MbgLtNgCfgNumberOfPhysicalIf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 7),
    _MbgLtNgCfgNumberOfPhysicalIf_Type()
)
mbgLtNgCfgNumberOfPhysicalIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgNumberOfPhysicalIf.setStatus("current")


class _MbgLtNgCfgNumberOfVirtualIf_Type(Unsigned32):
    """Custom type mbgLtNgCfgNumberOfVirtualIf based on Unsigned32"""
    defaultValue = 0


_MbgLtNgCfgNumberOfVirtualIf_Object = MibScalar
mbgLtNgCfgNumberOfVirtualIf = _MbgLtNgCfgNumberOfVirtualIf_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 8),
    _MbgLtNgCfgNumberOfVirtualIf_Type()
)
mbgLtNgCfgNumberOfVirtualIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgNumberOfVirtualIf.setStatus("current")
_MbgLtNgCfgPhysicalIfTable_Object = MibTable
mbgLtNgCfgPhysicalIfTable = _MbgLtNgCfgPhysicalIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 9)
)
if mibBuilder.loadTexts:
    mbgLtNgCfgPhysicalIfTable.setStatus("current")
_MbgLtNgCfgPhysicalIfTableEntry_Object = MibTableRow
mbgLtNgCfgPhysicalIfTableEntry = _MbgLtNgCfgPhysicalIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 9, 1)
)
mbgLtNgCfgPhysicalIfTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPhysicalIfIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgCfgPhysicalIfTableEntry.setStatus("current")
_MbgLtNgCfgPhysicalIfIndex_Type = Unsigned32
_MbgLtNgCfgPhysicalIfIndex_Object = MibTableColumn
mbgLtNgCfgPhysicalIfIndex = _MbgLtNgCfgPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 9, 1, 1),
    _MbgLtNgCfgPhysicalIfIndex_Type()
)
mbgLtNgCfgPhysicalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgCfgPhysicalIfIndex.setStatus("current")


class _MbgLtNgCfgPhysicalIfMac_Type(DisplayString):
    """Custom type mbgLtNgCfgPhysicalIfMac based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPhysicalIfMac_Object = MibTableColumn
mbgLtNgCfgPhysicalIfMac = _MbgLtNgCfgPhysicalIfMac_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 9, 1, 2),
    _MbgLtNgCfgPhysicalIfMac_Type()
)
mbgLtNgCfgPhysicalIfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgPhysicalIfMac.setStatus("current")


class _MbgLtNgCfgPhysicalIfNetLinkMode_Type(Integer32):
    """Custom type mbgLtNgCfgPhysicalIfNetLinkMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("fd1000Mbit", 6),
          ("fd100Mbit", 4),
          ("fd10Mbit", 2),
          ("hd1000Mbit", 5),
          ("hd100Mbit", 3),
          ("hd10Mbit", 1))
    )


_MbgLtNgCfgPhysicalIfNetLinkMode_Type.__name__ = "Integer32"
_MbgLtNgCfgPhysicalIfNetLinkMode_Object = MibTableColumn
mbgLtNgCfgPhysicalIfNetLinkMode = _MbgLtNgCfgPhysicalIfNetLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 9, 1, 3),
    _MbgLtNgCfgPhysicalIfNetLinkMode_Type()
)
mbgLtNgCfgPhysicalIfNetLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPhysicalIfNetLinkMode.setStatus("current")


class _MbgLtNgCfgPhysicalIfIndicateLink_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPhysicalIfIndicateLink based on MeinbergSwitch"""
    defaultValue = 1


_MbgLtNgCfgPhysicalIfIndicateLink_Object = MibTableColumn
mbgLtNgCfgPhysicalIfIndicateLink = _MbgLtNgCfgPhysicalIfIndicateLink_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 9, 1, 4),
    _MbgLtNgCfgPhysicalIfIndicateLink_Type()
)
mbgLtNgCfgPhysicalIfIndicateLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPhysicalIfIndicateLink.setStatus("current")


class _MbgLtNgCfgPhysicalIfBondingGroup_Type(Unsigned32):
    """Custom type mbgLtNgCfgPhysicalIfBondingGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_MbgLtNgCfgPhysicalIfBondingGroup_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPhysicalIfBondingGroup_Object = MibTableColumn
mbgLtNgCfgPhysicalIfBondingGroup = _MbgLtNgCfgPhysicalIfBondingGroup_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 9, 1, 5),
    _MbgLtNgCfgPhysicalIfBondingGroup_Type()
)
mbgLtNgCfgPhysicalIfBondingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPhysicalIfBondingGroup.setStatus("current")


class _MbgLtNgCfgPhysicalIfIpv6Mode_Type(Integer32):
    """Custom type mbgLtNgCfgPhysicalIfIpv6Mode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("activatedWithAutoconf", 2),
          ("deactivated", 0))
    )


_MbgLtNgCfgPhysicalIfIpv6Mode_Type.__name__ = "Integer32"
_MbgLtNgCfgPhysicalIfIpv6Mode_Object = MibTableColumn
mbgLtNgCfgPhysicalIfIpv6Mode = _MbgLtNgCfgPhysicalIfIpv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 9, 1, 6),
    _MbgLtNgCfgPhysicalIfIpv6Mode_Type()
)
mbgLtNgCfgPhysicalIfIpv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPhysicalIfIpv6Mode.setStatus("current")
_MbgLtNgCfgVirtualIfTable_Object = MibTable
mbgLtNgCfgVirtualIfTable = _MbgLtNgCfgVirtualIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10)
)
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfTable.setStatus("current")
_MbgLtNgCfgVirtualIfTableEntry_Object = MibTableRow
mbgLtNgCfgVirtualIfTableEntry = _MbgLtNgCfgVirtualIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1)
)
mbgLtNgCfgVirtualIfTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfTableEntry.setStatus("current")
_MbgLtNgCfgVirtualIfIndex_Type = Unsigned32
_MbgLtNgCfgVirtualIfIndex_Object = MibTableColumn
mbgLtNgCfgVirtualIfIndex = _MbgLtNgCfgVirtualIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 1),
    _MbgLtNgCfgVirtualIfIndex_Type()
)
mbgLtNgCfgVirtualIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIndex.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv4Addr_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv4Addr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv4Addr_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv4Addr = _MbgLtNgCfgVirtualIfIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 2),
    _MbgLtNgCfgVirtualIfIpv4Addr_Type()
)
mbgLtNgCfgVirtualIfIpv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv4Addr.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv4Netmask_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv4Netmask based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv4Netmask_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv4Netmask = _MbgLtNgCfgVirtualIfIpv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 3),
    _MbgLtNgCfgVirtualIfIpv4Netmask_Type()
)
mbgLtNgCfgVirtualIfIpv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv4Netmask.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv4Dhcp_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfIpv4Dhcp based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfIpv4Dhcp_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv4Dhcp = _MbgLtNgCfgVirtualIfIpv4Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 4),
    _MbgLtNgCfgVirtualIfIpv4Dhcp_Type()
)
mbgLtNgCfgVirtualIfIpv4Dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv4Dhcp.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv4AddrFromDhcp_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv4AddrFromDhcp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv4AddrFromDhcp_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv4AddrFromDhcp = _MbgLtNgCfgVirtualIfIpv4AddrFromDhcp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 5),
    _MbgLtNgCfgVirtualIfIpv4AddrFromDhcp_Type()
)
mbgLtNgCfgVirtualIfIpv4AddrFromDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv4AddrFromDhcp.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp = _MbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 6),
    _MbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp_Type()
)
mbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp = _MbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 7),
    _MbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp_Type()
)
mbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv4GatewayFromDhcp_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv4GatewayFromDhcp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv4GatewayFromDhcp_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv4GatewayFromDhcp = _MbgLtNgCfgVirtualIfIpv4GatewayFromDhcp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 8),
    _MbgLtNgCfgVirtualIfIpv4GatewayFromDhcp_Type()
)
mbgLtNgCfgVirtualIfIpv4GatewayFromDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv4GatewayFromDhcp.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv4DnsFromDhcp_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv4DnsFromDhcp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv4DnsFromDhcp_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv4DnsFromDhcp = _MbgLtNgCfgVirtualIfIpv4DnsFromDhcp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 9),
    _MbgLtNgCfgVirtualIfIpv4DnsFromDhcp_Type()
)
mbgLtNgCfgVirtualIfIpv4DnsFromDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv4DnsFromDhcp.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv4DomainFromDhcp_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv4DomainFromDhcp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv4DomainFromDhcp_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv4DomainFromDhcp = _MbgLtNgCfgVirtualIfIpv4DomainFromDhcp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 10),
    _MbgLtNgCfgVirtualIfIpv4DomainFromDhcp_Type()
)
mbgLtNgCfgVirtualIfIpv4DomainFromDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv4DomainFromDhcp.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv6Addr_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv6Addr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv6Addr_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv6Addr = _MbgLtNgCfgVirtualIfIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 11),
    _MbgLtNgCfgVirtualIfIpv6Addr_Type()
)
mbgLtNgCfgVirtualIfIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv6Addr.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv6Dhcp_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfIpv6Dhcp based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfIpv6Dhcp_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv6Dhcp = _MbgLtNgCfgVirtualIfIpv6Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 12),
    _MbgLtNgCfgVirtualIfIpv6Dhcp_Type()
)
mbgLtNgCfgVirtualIfIpv6Dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv6Dhcp.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv6RoutAdd_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv6RoutAdd based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv6RoutAdd_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv6RoutAdd = _MbgLtNgCfgVirtualIfIpv6RoutAdd_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 13),
    _MbgLtNgCfgVirtualIfIpv6RoutAdd_Type()
)
mbgLtNgCfgVirtualIfIpv6RoutAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv6RoutAdd.setStatus("current")


class _MbgLtNgCfgVirtualIfIpv6LinkLocal_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfIpv6LinkLocal based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfIpv6LinkLocal_Object = MibTableColumn
mbgLtNgCfgVirtualIfIpv6LinkLocal = _MbgLtNgCfgVirtualIfIpv6LinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 14),
    _MbgLtNgCfgVirtualIfIpv6LinkLocal_Type()
)
mbgLtNgCfgVirtualIfIpv6LinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfIpv6LinkLocal.setStatus("current")


class _MbgLtNgCfgVirtualIfAssigned_Type(Unsigned32):
    """Custom type mbgLtNgCfgVirtualIfAssigned based on Unsigned32"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfAssigned_Object = MibTableColumn
mbgLtNgCfgVirtualIfAssigned = _MbgLtNgCfgVirtualIfAssigned_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 15),
    _MbgLtNgCfgVirtualIfAssigned_Type()
)
mbgLtNgCfgVirtualIfAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfAssigned.setStatus("current")


class _MbgLtNgCfgVirtualIfMac_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfMac based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfMac_Object = MibTableColumn
mbgLtNgCfgVirtualIfMac = _MbgLtNgCfgVirtualIfMac_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 16),
    _MbgLtNgCfgVirtualIfMac_Type()
)
mbgLtNgCfgVirtualIfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfMac.setStatus("current")


class _MbgLtNgCfgVirtualIfLabel_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfLabel based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfLabel_Object = MibTableColumn
mbgLtNgCfgVirtualIfLabel = _MbgLtNgCfgVirtualIfLabel_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 17),
    _MbgLtNgCfgVirtualIfLabel_Type()
)
mbgLtNgCfgVirtualIfLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfLabel.setStatus("current")


class _MbgLtNgCfgVirtualIfVlan_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfVlan based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfVlan_Object = MibTableColumn
mbgLtNgCfgVirtualIfVlan = _MbgLtNgCfgVirtualIfVlan_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 18),
    _MbgLtNgCfgVirtualIfVlan_Type()
)
mbgLtNgCfgVirtualIfVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfVlan.setStatus("current")


class _MbgLtNgCfgVirtualIfVlanTag_Type(Unsigned32):
    """Custom type mbgLtNgCfgVirtualIfVlanTag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MbgLtNgCfgVirtualIfVlanTag_Type.__name__ = "Unsigned32"
_MbgLtNgCfgVirtualIfVlanTag_Object = MibTableColumn
mbgLtNgCfgVirtualIfVlanTag = _MbgLtNgCfgVirtualIfVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 19),
    _MbgLtNgCfgVirtualIfVlanTag_Type()
)
mbgLtNgCfgVirtualIfVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfVlanTag.setStatus("current")


class _MbgLtNgCfgVirtualIfVlanPrio_Type(Unsigned32):
    """Custom type mbgLtNgCfgVirtualIfVlanPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MbgLtNgCfgVirtualIfVlanPrio_Type.__name__ = "Unsigned32"
_MbgLtNgCfgVirtualIfVlanPrio_Object = MibTableColumn
mbgLtNgCfgVirtualIfVlanPrio = _MbgLtNgCfgVirtualIfVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 20),
    _MbgLtNgCfgVirtualIfVlanPrio_Type()
)
mbgLtNgCfgVirtualIfVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfVlanPrio.setStatus("current")


class _MbgLtNgCfgVirtualIfCluster_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfCluster based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfCluster_Object = MibTableColumn
mbgLtNgCfgVirtualIfCluster = _MbgLtNgCfgVirtualIfCluster_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 21),
    _MbgLtNgCfgVirtualIfCluster_Type()
)
mbgLtNgCfgVirtualIfCluster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfCluster.setStatus("current")


class _MbgLtNgCfgVirtualIfClusterIpv4Addr_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfClusterIpv4Addr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfClusterIpv4Addr_Object = MibTableColumn
mbgLtNgCfgVirtualIfClusterIpv4Addr = _MbgLtNgCfgVirtualIfClusterIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 22),
    _MbgLtNgCfgVirtualIfClusterIpv4Addr_Type()
)
mbgLtNgCfgVirtualIfClusterIpv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfClusterIpv4Addr.setStatus("current")


class _MbgLtNgCfgVirtualIfClusterIpv4Netmask_Type(DisplayString):
    """Custom type mbgLtNgCfgVirtualIfClusterIpv4Netmask based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVirtualIfClusterIpv4Netmask_Object = MibTableColumn
mbgLtNgCfgVirtualIfClusterIpv4Netmask = _MbgLtNgCfgVirtualIfClusterIpv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 23),
    _MbgLtNgCfgVirtualIfClusterIpv4Netmask_Type()
)
mbgLtNgCfgVirtualIfClusterIpv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfClusterIpv4Netmask.setStatus("current")


class _MbgLtNgCfgVirtualIfClusterPrio_Type(Unsigned32):
    """Custom type mbgLtNgCfgVirtualIfClusterPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MbgLtNgCfgVirtualIfClusterPrio_Type.__name__ = "Unsigned32"
_MbgLtNgCfgVirtualIfClusterPrio_Object = MibTableColumn
mbgLtNgCfgVirtualIfClusterPrio = _MbgLtNgCfgVirtualIfClusterPrio_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 24),
    _MbgLtNgCfgVirtualIfClusterPrio_Type()
)
mbgLtNgCfgVirtualIfClusterPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfClusterPrio.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceNtp_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceNtp based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceNtp_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceNtp = _MbgLtNgCfgVirtualIfServiceNtp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 25),
    _MbgLtNgCfgVirtualIfServiceNtp_Type()
)
mbgLtNgCfgVirtualIfServiceNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceNtp.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceHttp_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceHttp based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceHttp_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceHttp = _MbgLtNgCfgVirtualIfServiceHttp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 26),
    _MbgLtNgCfgVirtualIfServiceHttp_Type()
)
mbgLtNgCfgVirtualIfServiceHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceHttp.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceHttps_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceHttps based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceHttps_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceHttps = _MbgLtNgCfgVirtualIfServiceHttps_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 27),
    _MbgLtNgCfgVirtualIfServiceHttps_Type()
)
mbgLtNgCfgVirtualIfServiceHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceHttps.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceTelnet_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceTelnet based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceTelnet_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceTelnet = _MbgLtNgCfgVirtualIfServiceTelnet_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 28),
    _MbgLtNgCfgVirtualIfServiceTelnet_Type()
)
mbgLtNgCfgVirtualIfServiceTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceTelnet.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceSsh_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceSsh based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceSsh_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceSsh = _MbgLtNgCfgVirtualIfServiceSsh_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 29),
    _MbgLtNgCfgVirtualIfServiceSsh_Type()
)
mbgLtNgCfgVirtualIfServiceSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceSsh.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceSnmp_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceSnmp based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceSnmp_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceSnmp = _MbgLtNgCfgVirtualIfServiceSnmp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 30),
    _MbgLtNgCfgVirtualIfServiceSnmp_Type()
)
mbgLtNgCfgVirtualIfServiceSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceSnmp.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceFtp_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceFtp based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceFtp_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceFtp = _MbgLtNgCfgVirtualIfServiceFtp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 31),
    _MbgLtNgCfgVirtualIfServiceFtp_Type()
)
mbgLtNgCfgVirtualIfServiceFtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceFtp.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceTime_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceTime based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceTime_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceTime = _MbgLtNgCfgVirtualIfServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 32),
    _MbgLtNgCfgVirtualIfServiceTime_Type()
)
mbgLtNgCfgVirtualIfServiceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceTime.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceDaytime_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceDaytime based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceDaytime_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceDaytime = _MbgLtNgCfgVirtualIfServiceDaytime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 33),
    _MbgLtNgCfgVirtualIfServiceDaytime_Type()
)
mbgLtNgCfgVirtualIfServiceDaytime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceDaytime.setStatus("current")


class _MbgLtNgCfgVirtualIfServiceFpc_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgVirtualIfServiceFpc based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgVirtualIfServiceFpc_Object = MibTableColumn
mbgLtNgCfgVirtualIfServiceFpc = _MbgLtNgCfgVirtualIfServiceFpc_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 10, 1, 34),
    _MbgLtNgCfgVirtualIfServiceFpc_Type()
)
mbgLtNgCfgVirtualIfServiceFpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVirtualIfServiceFpc.setStatus("current")


class _MbgLtNgCfgEthernetGenClusterPort_Type(Unsigned32):
    """Custom type mbgLtNgCfgEthernetGenClusterPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MbgLtNgCfgEthernetGenClusterPort_Type.__name__ = "Unsigned32"
_MbgLtNgCfgEthernetGenClusterPort_Object = MibScalar
mbgLtNgCfgEthernetGenClusterPort = _MbgLtNgCfgEthernetGenClusterPort_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 11),
    _MbgLtNgCfgEthernetGenClusterPort_Type()
)
mbgLtNgCfgEthernetGenClusterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEthernetGenClusterPort.setStatus("current")
_MbgLtNgCfgEthernetGenClusterIp_Type = DisplayString
_MbgLtNgCfgEthernetGenClusterIp_Object = MibScalar
mbgLtNgCfgEthernetGenClusterIp = _MbgLtNgCfgEthernetGenClusterIp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 0, 12),
    _MbgLtNgCfgEthernetGenClusterIp_Type()
)
mbgLtNgCfgEthernetGenClusterIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEthernetGenClusterIp.setStatus("current")
_MbgLtNgCfgNotifications_ObjectIdentity = ObjectIdentity
mbgLtNgCfgNotifications = _MbgLtNgCfgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1)
)
_MbgLtNgCfgSyslog_ObjectIdentity = ObjectIdentity
mbgLtNgCfgSyslog = _MbgLtNgCfgSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 0)
)


class _MbgLtNgCfgSyslogServerAddr_Type(DisplayString):
    """Custom type mbgLtNgCfgSyslogServerAddr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgSyslogServerAddr_Object = MibScalar
mbgLtNgCfgSyslogServerAddr = _MbgLtNgCfgSyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 0, 1),
    _MbgLtNgCfgSyslogServerAddr_Type()
)
mbgLtNgCfgSyslogServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSyslogServerAddr.setStatus("current")


class _MbgLtNgCfgSyslogLoglevel_Type(Integer32):
    """Custom type mbgLtNgCfgSyslogLoglevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_MbgLtNgCfgSyslogLoglevel_Type.__name__ = "Integer32"
_MbgLtNgCfgSyslogLoglevel_Object = MibScalar
mbgLtNgCfgSyslogLoglevel = _MbgLtNgCfgSyslogLoglevel_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 0, 2),
    _MbgLtNgCfgSyslogLoglevel_Type()
)
mbgLtNgCfgSyslogLoglevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSyslogLoglevel.setStatus("current")
_MbgLtNgCfgEmail_ObjectIdentity = ObjectIdentity
mbgLtNgCfgEmail = _MbgLtNgCfgEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 1)
)


class _MbgLtNgCfgEmailTo_Type(DisplayString):
    """Custom type mbgLtNgCfgEmailTo based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEmailTo_Object = MibScalar
mbgLtNgCfgEmailTo = _MbgLtNgCfgEmailTo_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 1, 1),
    _MbgLtNgCfgEmailTo_Type()
)
mbgLtNgCfgEmailTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEmailTo.setStatus("current")


class _MbgLtNgCfgEmailFrom_Type(DisplayString):
    """Custom type mbgLtNgCfgEmailFrom based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEmailFrom_Object = MibScalar
mbgLtNgCfgEmailFrom = _MbgLtNgCfgEmailFrom_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 1, 2),
    _MbgLtNgCfgEmailFrom_Type()
)
mbgLtNgCfgEmailFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEmailFrom.setStatus("current")


class _MbgLtNgCfgEmailSmarthostAddr_Type(DisplayString):
    """Custom type mbgLtNgCfgEmailSmarthostAddr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEmailSmarthostAddr_Object = MibScalar
mbgLtNgCfgEmailSmarthostAddr = _MbgLtNgCfgEmailSmarthostAddr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 1, 3),
    _MbgLtNgCfgEmailSmarthostAddr_Type()
)
mbgLtNgCfgEmailSmarthostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEmailSmarthostAddr.setStatus("current")


class _MbgLtNgCfgEmailSmarthostPort_Type(Unsigned32):
    """Custom type mbgLtNgCfgEmailSmarthostPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MbgLtNgCfgEmailSmarthostPort_Type.__name__ = "Unsigned32"
_MbgLtNgCfgEmailSmarthostPort_Object = MibScalar
mbgLtNgCfgEmailSmarthostPort = _MbgLtNgCfgEmailSmarthostPort_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 1, 4),
    _MbgLtNgCfgEmailSmarthostPort_Type()
)
mbgLtNgCfgEmailSmarthostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEmailSmarthostPort.setStatus("current")


class _MbgLtNgCfgEmailSmarthostAuth_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgEmailSmarthostAuth based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgEmailSmarthostAuth_Object = MibScalar
mbgLtNgCfgEmailSmarthostAuth = _MbgLtNgCfgEmailSmarthostAuth_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 1, 5),
    _MbgLtNgCfgEmailSmarthostAuth_Type()
)
mbgLtNgCfgEmailSmarthostAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEmailSmarthostAuth.setStatus("current")


class _MbgLtNgCfgEmailSmarthostAuthUser_Type(DisplayString):
    """Custom type mbgLtNgCfgEmailSmarthostAuthUser based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEmailSmarthostAuthUser_Object = MibScalar
mbgLtNgCfgEmailSmarthostAuthUser = _MbgLtNgCfgEmailSmarthostAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 1, 6),
    _MbgLtNgCfgEmailSmarthostAuthUser_Type()
)
mbgLtNgCfgEmailSmarthostAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEmailSmarthostAuthUser.setStatus("current")


class _MbgLtNgCfgEmailSmarthostAuthPw_Type(DisplayString):
    """Custom type mbgLtNgCfgEmailSmarthostAuthPw based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgEmailSmarthostAuthPw_Object = MibScalar
mbgLtNgCfgEmailSmarthostAuthPw = _MbgLtNgCfgEmailSmarthostAuthPw_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 1, 7),
    _MbgLtNgCfgEmailSmarthostAuthPw_Type()
)
mbgLtNgCfgEmailSmarthostAuthPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEmailSmarthostAuthPw.setStatus("current")
_MbgLtNgCfgWinpopup_ObjectIdentity = ObjectIdentity
mbgLtNgCfgWinpopup = _MbgLtNgCfgWinpopup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 2)
)


class _MbgLtNgCfgWmailAddress1_Type(DisplayString):
    """Custom type mbgLtNgCfgWmailAddress1 based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgWmailAddress1_Object = MibScalar
mbgLtNgCfgWmailAddress1 = _MbgLtNgCfgWmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 2, 1),
    _MbgLtNgCfgWmailAddress1_Type()
)
mbgLtNgCfgWmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgWmailAddress1.setStatus("current")


class _MbgLtNgCfgWmailAddress2_Type(DisplayString):
    """Custom type mbgLtNgCfgWmailAddress2 based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgWmailAddress2_Object = MibScalar
mbgLtNgCfgWmailAddress2 = _MbgLtNgCfgWmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 2, 2),
    _MbgLtNgCfgWmailAddress2_Type()
)
mbgLtNgCfgWmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgWmailAddress2.setStatus("current")
_MbgLtNgCfgSNMP_ObjectIdentity = ObjectIdentity
mbgLtNgCfgSNMP = _MbgLtNgCfgSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3)
)
_MbgLtNgCfgSnmpTrapRecTable_Object = MibTable
mbgLtNgCfgSnmpTrapRecTable = _MbgLtNgCfgSnmpTrapRecTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpTrapRecTable.setStatus("current")
_MbgLtNgCfgSnmpTrapRecTableEntry_Object = MibTableRow
mbgLtNgCfgSnmpTrapRecTableEntry = _MbgLtNgCfgSnmpTrapRecTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 1, 1)
)
mbgLtNgCfgSnmpTrapRecTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpTrapRecIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpTrapRecTableEntry.setStatus("current")


class _MbgLtNgCfgSnmpTrapRecIndex_Type(Unsigned32):
    """Custom type mbgLtNgCfgSnmpTrapRecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MbgLtNgCfgSnmpTrapRecIndex_Type.__name__ = "Unsigned32"
_MbgLtNgCfgSnmpTrapRecIndex_Object = MibTableColumn
mbgLtNgCfgSnmpTrapRecIndex = _MbgLtNgCfgSnmpTrapRecIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 1, 1, 1),
    _MbgLtNgCfgSnmpTrapRecIndex_Type()
)
mbgLtNgCfgSnmpTrapRecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpTrapRecIndex.setStatus("current")


class _MbgLtNgCfgSnmpTrapRecAddr_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpTrapRecAddr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgSnmpTrapRecAddr_Object = MibTableColumn
mbgLtNgCfgSnmpTrapRecAddr = _MbgLtNgCfgSnmpTrapRecAddr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 1, 1, 2),
    _MbgLtNgCfgSnmpTrapRecAddr_Type()
)
mbgLtNgCfgSnmpTrapRecAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpTrapRecAddr.setStatus("current")


class _MbgLtNgCfgSnmpTrapRecCommunity_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpTrapRecCommunity based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgSnmpTrapRecCommunity_Object = MibTableColumn
mbgLtNgCfgSnmpTrapRecCommunity = _MbgLtNgCfgSnmpTrapRecCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 1, 1, 3),
    _MbgLtNgCfgSnmpTrapRecCommunity_Type()
)
mbgLtNgCfgSnmpTrapRecCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpTrapRecCommunity.setStatus("current")


class _MbgLtNgCfgSnmpTrapRecVersion_Type(Integer32):
    """Custom type mbgLtNgCfgSnmpTrapRecVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_MbgLtNgCfgSnmpTrapRecVersion_Type.__name__ = "Integer32"
_MbgLtNgCfgSnmpTrapRecVersion_Object = MibTableColumn
mbgLtNgCfgSnmpTrapRecVersion = _MbgLtNgCfgSnmpTrapRecVersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 1, 1, 4),
    _MbgLtNgCfgSnmpTrapRecVersion_Type()
)
mbgLtNgCfgSnmpTrapRecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpTrapRecVersion.setStatus("current")


class _MbgLtNgCfgSnmpReadCommunity_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpReadCommunity based on DisplayString"""
    defaultValue = OctetString("****")


_MbgLtNgCfgSnmpReadCommunity_Object = MibScalar
mbgLtNgCfgSnmpReadCommunity = _MbgLtNgCfgSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 2),
    _MbgLtNgCfgSnmpReadCommunity_Type()
)
mbgLtNgCfgSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpReadCommunity.setStatus("current")


class _MbgLtNgCfgSnmpWriteCommunity_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpWriteCommunity based on DisplayString"""
    defaultValue = OctetString("****")


_MbgLtNgCfgSnmpWriteCommunity_Object = MibScalar
mbgLtNgCfgSnmpWriteCommunity = _MbgLtNgCfgSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 3),
    _MbgLtNgCfgSnmpWriteCommunity_Type()
)
mbgLtNgCfgSnmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpWriteCommunity.setStatus("current")


class _MbgLtNgCfgSnmpContact_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpContact based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgSnmpContact_Object = MibScalar
mbgLtNgCfgSnmpContact = _MbgLtNgCfgSnmpContact_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 4),
    _MbgLtNgCfgSnmpContact_Type()
)
mbgLtNgCfgSnmpContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpContact.setStatus("current")


class _MbgLtNgCfgSnmpLocation_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpLocation based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgSnmpLocation_Object = MibScalar
mbgLtNgCfgSnmpLocation = _MbgLtNgCfgSnmpLocation_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 5),
    _MbgLtNgCfgSnmpLocation_Type()
)
mbgLtNgCfgSnmpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpLocation.setStatus("current")


class _MbgLtNgCfgSnmpV3UserName_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpV3UserName based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgSnmpV3UserName_Object = MibScalar
mbgLtNgCfgSnmpV3UserName = _MbgLtNgCfgSnmpV3UserName_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 6),
    _MbgLtNgCfgSnmpV3UserName_Type()
)
mbgLtNgCfgSnmpV3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpV3UserName.setStatus("current")


class _MbgLtNgCfgSnmpV3UserRights_Type(Integer32):
    """Custom type mbgLtNgCfgSnmpV3UserRights based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 0),
          ("readwrite", 1))
    )


_MbgLtNgCfgSnmpV3UserRights_Type.__name__ = "Integer32"
_MbgLtNgCfgSnmpV3UserRights_Object = MibScalar
mbgLtNgCfgSnmpV3UserRights = _MbgLtNgCfgSnmpV3UserRights_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 7),
    _MbgLtNgCfgSnmpV3UserRights_Type()
)
mbgLtNgCfgSnmpV3UserRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpV3UserRights.setStatus("current")


class _MbgLtNgCfgSnmpV3Context_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpV3Context based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgSnmpV3Context_Object = MibScalar
mbgLtNgCfgSnmpV3Context = _MbgLtNgCfgSnmpV3Context_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 8),
    _MbgLtNgCfgSnmpV3Context_Type()
)
mbgLtNgCfgSnmpV3Context.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpV3Context.setStatus("current")


class _MbgLtNgCfgSnmpV3SecurityLevel_Type(Integer32):
    """Custom type mbgLtNgCfgSnmpV3SecurityLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authNoPriv", 1),
          ("authPriv", 2),
          ("noAuthNoPriv", 0))
    )


_MbgLtNgCfgSnmpV3SecurityLevel_Type.__name__ = "Integer32"
_MbgLtNgCfgSnmpV3SecurityLevel_Object = MibScalar
mbgLtNgCfgSnmpV3SecurityLevel = _MbgLtNgCfgSnmpV3SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 9),
    _MbgLtNgCfgSnmpV3SecurityLevel_Type()
)
mbgLtNgCfgSnmpV3SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpV3SecurityLevel.setStatus("current")


class _MbgLtNgCfgSnmpV3AuthProtocol_Type(Integer32):
    """Custom type mbgLtNgCfgSnmpV3AuthProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_MbgLtNgCfgSnmpV3AuthProtocol_Type.__name__ = "Integer32"
_MbgLtNgCfgSnmpV3AuthProtocol_Object = MibScalar
mbgLtNgCfgSnmpV3AuthProtocol = _MbgLtNgCfgSnmpV3AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 10),
    _MbgLtNgCfgSnmpV3AuthProtocol_Type()
)
mbgLtNgCfgSnmpV3AuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpV3AuthProtocol.setStatus("current")


class _MbgLtNgCfgSnmpV3AuthPassphrase_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpV3AuthPassphrase based on DisplayString"""
    defaultValue = OctetString("****")


_MbgLtNgCfgSnmpV3AuthPassphrase_Object = MibScalar
mbgLtNgCfgSnmpV3AuthPassphrase = _MbgLtNgCfgSnmpV3AuthPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 11),
    _MbgLtNgCfgSnmpV3AuthPassphrase_Type()
)
mbgLtNgCfgSnmpV3AuthPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpV3AuthPassphrase.setStatus("current")


class _MbgLtNgCfgSnmpV3PrivProtocol_Type(Integer32):
    """Custom type mbgLtNgCfgSnmpV3PrivProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("des", 0))
    )


_MbgLtNgCfgSnmpV3PrivProtocol_Type.__name__ = "Integer32"
_MbgLtNgCfgSnmpV3PrivProtocol_Object = MibScalar
mbgLtNgCfgSnmpV3PrivProtocol = _MbgLtNgCfgSnmpV3PrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 12),
    _MbgLtNgCfgSnmpV3PrivProtocol_Type()
)
mbgLtNgCfgSnmpV3PrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpV3PrivProtocol.setStatus("current")


class _MbgLtNgCfgSnmpV3PrivPassphrase_Type(DisplayString):
    """Custom type mbgLtNgCfgSnmpV3PrivPassphrase based on DisplayString"""
    defaultValue = OctetString("****")


_MbgLtNgCfgSnmpV3PrivPassphrase_Object = MibScalar
mbgLtNgCfgSnmpV3PrivPassphrase = _MbgLtNgCfgSnmpV3PrivPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 13),
    _MbgLtNgCfgSnmpV3PrivPassphrase_Type()
)
mbgLtNgCfgSnmpV3PrivPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpV3PrivPassphrase.setStatus("current")


class _MbgLtNgCfgSnmpRetries_Type(Unsigned32):
    """Custom type mbgLtNgCfgSnmpRetries based on Unsigned32"""
    defaultValue = 3


_MbgLtNgCfgSnmpRetries_Object = MibScalar
mbgLtNgCfgSnmpRetries = _MbgLtNgCfgSnmpRetries_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 14),
    _MbgLtNgCfgSnmpRetries_Type()
)
mbgLtNgCfgSnmpRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpRetries.setStatus("current")


class _MbgLtNgCfgSnmpTimeout_Type(Unsigned32):
    """Custom type mbgLtNgCfgSnmpTimeout based on Unsigned32"""
    defaultValue = 3


_MbgLtNgCfgSnmpTimeout_Object = MibScalar
mbgLtNgCfgSnmpTimeout = _MbgLtNgCfgSnmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 15),
    _MbgLtNgCfgSnmpTimeout_Type()
)
mbgLtNgCfgSnmpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpTimeout.setUnits("sec")


class _MbgLtNgCfgSnmpEnabledVersion_Type(Integer32):
    """Custom type mbgLtNgCfgSnmpEnabledVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1ANDv2c", 0),
          ("v1ANDv2cANDv3", 2),
          ("v3only", 1))
    )


_MbgLtNgCfgSnmpEnabledVersion_Type.__name__ = "Integer32"
_MbgLtNgCfgSnmpEnabledVersion_Object = MibScalar
mbgLtNgCfgSnmpEnabledVersion = _MbgLtNgCfgSnmpEnabledVersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 3, 16),
    _MbgLtNgCfgSnmpEnabledVersion_Type()
)
mbgLtNgCfgSnmpEnabledVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSnmpEnabledVersion.setStatus("current")
_MbgLtNgCfgWalldisplay_ObjectIdentity = ObjectIdentity
mbgLtNgCfgWalldisplay = _MbgLtNgCfgWalldisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 4)
)


class _MbgLtNgCfgVP100Display1Addr_Type(DisplayString):
    """Custom type mbgLtNgCfgVP100Display1Addr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVP100Display1Addr_Object = MibScalar
mbgLtNgCfgVP100Display1Addr = _MbgLtNgCfgVP100Display1Addr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 4, 1),
    _MbgLtNgCfgVP100Display1Addr_Type()
)
mbgLtNgCfgVP100Display1Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVP100Display1Addr.setStatus("current")


class _MbgLtNgCfgVP100Display1SN_Type(DisplayString):
    """Custom type mbgLtNgCfgVP100Display1SN based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVP100Display1SN_Object = MibScalar
mbgLtNgCfgVP100Display1SN = _MbgLtNgCfgVP100Display1SN_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 4, 2),
    _MbgLtNgCfgVP100Display1SN_Type()
)
mbgLtNgCfgVP100Display1SN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVP100Display1SN.setStatus("current")


class _MbgLtNgCfgVP100Display2Addr_Type(DisplayString):
    """Custom type mbgLtNgCfgVP100Display2Addr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVP100Display2Addr_Object = MibScalar
mbgLtNgCfgVP100Display2Addr = _MbgLtNgCfgVP100Display2Addr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 4, 3),
    _MbgLtNgCfgVP100Display2Addr_Type()
)
mbgLtNgCfgVP100Display2Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVP100Display2Addr.setStatus("current")


class _MbgLtNgCfgVP100Display2SN_Type(DisplayString):
    """Custom type mbgLtNgCfgVP100Display2SN based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgVP100Display2SN_Object = MibScalar
mbgLtNgCfgVP100Display2SN = _MbgLtNgCfgVP100Display2SN_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 4, 4),
    _MbgLtNgCfgVP100Display2SN_Type()
)
mbgLtNgCfgVP100Display2SN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgVP100Display2SN.setStatus("current")
_MbgLtNgCfgNtpClientMonitoring_ObjectIdentity = ObjectIdentity
mbgLtNgCfgNtpClientMonitoring = _MbgLtNgCfgNtpClientMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 5)
)


class _MbgLtNgCfgNtpMaxClientOffset_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpMaxClientOffset based on Unsigned32"""
    defaultValue = 10


_MbgLtNgCfgNtpMaxClientOffset_Object = MibScalar
mbgLtNgCfgNtpMaxClientOffset = _MbgLtNgCfgNtpMaxClientOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 5, 1),
    _MbgLtNgCfgNtpMaxClientOffset_Type()
)
mbgLtNgCfgNtpMaxClientOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpMaxClientOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpMaxClientOffset.setUnits("ms")


class _MbgLtNgCfgNtpMaxClientStratum_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpMaxClientStratum based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MbgLtNgCfgNtpMaxClientStratum_Type.__name__ = "Unsigned32"
_MbgLtNgCfgNtpMaxClientStratum_Object = MibScalar
mbgLtNgCfgNtpMaxClientStratum = _MbgLtNgCfgNtpMaxClientStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 5, 2),
    _MbgLtNgCfgNtpMaxClientStratum_Type()
)
mbgLtNgCfgNtpMaxClientStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpMaxClientStratum.setStatus("current")
_MbgLtNgCfgTrapTrigger_ObjectIdentity = ObjectIdentity
mbgLtNgCfgTrapTrigger = _MbgLtNgCfgTrapTrigger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6)
)


class _MbgLtNgCfgTrapNormalOperation_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapNormalOperation based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapNormalOperation_Object = MibScalar
mbgLtNgCfgTrapNormalOperation = _MbgLtNgCfgTrapNormalOperation_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 1),
    _MbgLtNgCfgTrapNormalOperation_Type()
)
mbgLtNgCfgTrapNormalOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapNormalOperation.setStatus("current")


class _MbgLtNgCfgTrapNtpNotSync_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapNtpNotSync based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapNtpNotSync_Object = MibScalar
mbgLtNgCfgTrapNtpNotSync = _MbgLtNgCfgTrapNtpNotSync_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 2),
    _MbgLtNgCfgTrapNtpNotSync_Type()
)
mbgLtNgCfgTrapNtpNotSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapNtpNotSync.setStatus("current")


class _MbgLtNgCfgTrapNtpSync_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapNtpSync based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapNtpSync_Object = MibScalar
mbgLtNgCfgTrapNtpSync = _MbgLtNgCfgTrapNtpSync_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 3),
    _MbgLtNgCfgTrapNtpSync_Type()
)
mbgLtNgCfgTrapNtpSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapNtpSync.setStatus("current")


class _MbgLtNgCfgTrapNtpStopped_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapNtpStopped based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapNtpStopped_Object = MibScalar
mbgLtNgCfgTrapNtpStopped = _MbgLtNgCfgTrapNtpStopped_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 4),
    _MbgLtNgCfgTrapNtpStopped_Type()
)
mbgLtNgCfgTrapNtpStopped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapNtpStopped.setStatus("current")


class _MbgLtNgCfgTrapServerBoot_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapServerBoot based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapServerBoot_Object = MibScalar
mbgLtNgCfgTrapServerBoot = _MbgLtNgCfgTrapServerBoot_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 5),
    _MbgLtNgCfgTrapServerBoot_Type()
)
mbgLtNgCfgTrapServerBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapServerBoot.setStatus("current")


class _MbgLtNgCfgTrapRefclockNotResponding_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapRefclockNotResponding based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapRefclockNotResponding_Object = MibScalar
mbgLtNgCfgTrapRefclockNotResponding = _MbgLtNgCfgTrapRefclockNotResponding_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 6),
    _MbgLtNgCfgTrapRefclockNotResponding_Type()
)
mbgLtNgCfgTrapRefclockNotResponding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapRefclockNotResponding.setStatus("current")


class _MbgLtNgCfgTrapRefclockSynchronized_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapRefclockSynchronized based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapRefclockSynchronized_Object = MibScalar
mbgLtNgCfgTrapRefclockSynchronized = _MbgLtNgCfgTrapRefclockSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 7),
    _MbgLtNgCfgTrapRefclockSynchronized_Type()
)
mbgLtNgCfgTrapRefclockSynchronized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapRefclockSynchronized.setStatus("current")


class _MbgLtNgCfgTrapRefclockNotSynchronized_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapRefclockNotSynchronized based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapRefclockNotSynchronized_Object = MibScalar
mbgLtNgCfgTrapRefclockNotSynchronized = _MbgLtNgCfgTrapRefclockNotSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 8),
    _MbgLtNgCfgTrapRefclockNotSynchronized_Type()
)
mbgLtNgCfgTrapRefclockNotSynchronized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapRefclockNotSynchronized.setStatus("current")


class _MbgLtNgCfgTrapSecRefclockNotResponding_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapSecRefclockNotResponding based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapSecRefclockNotResponding_Object = MibScalar
mbgLtNgCfgTrapSecRefclockNotResponding = _MbgLtNgCfgTrapSecRefclockNotResponding_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 9),
    _MbgLtNgCfgTrapSecRefclockNotResponding_Type()
)
mbgLtNgCfgTrapSecRefclockNotResponding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapSecRefclockNotResponding.setStatus("current")


class _MbgLtNgCfgTrapSecRefclockSynchronized_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapSecRefclockSynchronized based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapSecRefclockSynchronized_Object = MibScalar
mbgLtNgCfgTrapSecRefclockSynchronized = _MbgLtNgCfgTrapSecRefclockSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 10),
    _MbgLtNgCfgTrapSecRefclockSynchronized_Type()
)
mbgLtNgCfgTrapSecRefclockSynchronized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapSecRefclockSynchronized.setStatus("current")


class _MbgLtNgCfgTrapSecRefclockNotSynchronized_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapSecRefclockNotSynchronized based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapSecRefclockNotSynchronized_Object = MibScalar
mbgLtNgCfgTrapSecRefclockNotSynchronized = _MbgLtNgCfgTrapSecRefclockNotSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 11),
    _MbgLtNgCfgTrapSecRefclockNotSynchronized_Type()
)
mbgLtNgCfgTrapSecRefclockNotSynchronized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapSecRefclockNotSynchronized.setStatus("current")


class _MbgLtNgCfgTrapAntennaFaulty_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapAntennaFaulty based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapAntennaFaulty_Object = MibScalar
mbgLtNgCfgTrapAntennaFaulty = _MbgLtNgCfgTrapAntennaFaulty_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 12),
    _MbgLtNgCfgTrapAntennaFaulty_Type()
)
mbgLtNgCfgTrapAntennaFaulty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapAntennaFaulty.setStatus("current")


class _MbgLtNgCfgTrapAntennaReconnect_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapAntennaReconnect based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapAntennaReconnect_Object = MibScalar
mbgLtNgCfgTrapAntennaReconnect = _MbgLtNgCfgTrapAntennaReconnect_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 13),
    _MbgLtNgCfgTrapAntennaReconnect_Type()
)
mbgLtNgCfgTrapAntennaReconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapAntennaReconnect.setStatus("current")


class _MbgLtNgCfgTrapAntennaShortCircuit_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapAntennaShortCircuit based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapAntennaShortCircuit_Object = MibScalar
mbgLtNgCfgTrapAntennaShortCircuit = _MbgLtNgCfgTrapAntennaShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 14),
    _MbgLtNgCfgTrapAntennaShortCircuit_Type()
)
mbgLtNgCfgTrapAntennaShortCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapAntennaShortCircuit.setStatus("current")


class _MbgLtNgCfgTrapConfigChanged_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapConfigChanged based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapConfigChanged_Object = MibScalar
mbgLtNgCfgTrapConfigChanged = _MbgLtNgCfgTrapConfigChanged_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 15),
    _MbgLtNgCfgTrapConfigChanged_Type()
)
mbgLtNgCfgTrapConfigChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapConfigChanged.setStatus("current")


class _MbgLtNgCfgTrapLeapSecAnnounced_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapLeapSecAnnounced based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapLeapSecAnnounced_Object = MibScalar
mbgLtNgCfgTrapLeapSecAnnounced = _MbgLtNgCfgTrapLeapSecAnnounced_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 16),
    _MbgLtNgCfgTrapLeapSecAnnounced_Type()
)
mbgLtNgCfgTrapLeapSecAnnounced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapLeapSecAnnounced.setStatus("current")


class _MbgLtNgCfgTrapNtpClientLimitExceeded_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapNtpClientLimitExceeded based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapNtpClientLimitExceeded_Object = MibScalar
mbgLtNgCfgTrapNtpClientLimitExceeded = _MbgLtNgCfgTrapNtpClientLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 17),
    _MbgLtNgCfgTrapNtpClientLimitExceeded_Type()
)
mbgLtNgCfgTrapNtpClientLimitExceeded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapNtpClientLimitExceeded.setStatus("current")


class _MbgLtNgCfgTrapRefSrcLimitExceeded_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapRefSrcLimitExceeded based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapRefSrcLimitExceeded_Object = MibScalar
mbgLtNgCfgTrapRefSrcLimitExceeded = _MbgLtNgCfgTrapRefSrcLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 18),
    _MbgLtNgCfgTrapRefSrcLimitExceeded_Type()
)
mbgLtNgCfgTrapRefSrcLimitExceeded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapRefSrcLimitExceeded.setStatus("current")


class _MbgLtNgCfgTrapRefSrcDisconnected_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapRefSrcDisconnected based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapRefSrcDisconnected_Object = MibScalar
mbgLtNgCfgTrapRefSrcDisconnected = _MbgLtNgCfgTrapRefSrcDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 19),
    _MbgLtNgCfgTrapRefSrcDisconnected_Type()
)
mbgLtNgCfgTrapRefSrcDisconnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapRefSrcDisconnected.setStatus("current")


class _MbgLtNgCfgTrapRefSrcReconnected_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapRefSrcReconnected based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapRefSrcReconnected_Object = MibScalar
mbgLtNgCfgTrapRefSrcReconnected = _MbgLtNgCfgTrapRefSrcReconnected_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 20),
    _MbgLtNgCfgTrapRefSrcReconnected_Type()
)
mbgLtNgCfgTrapRefSrcReconnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapRefSrcReconnected.setStatus("current")


class _MbgLtNgCfgTrapShsTimeLimitError_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapShsTimeLimitError based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapShsTimeLimitError_Object = MibScalar
mbgLtNgCfgTrapShsTimeLimitError = _MbgLtNgCfgTrapShsTimeLimitError_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 21),
    _MbgLtNgCfgTrapShsTimeLimitError_Type()
)
mbgLtNgCfgTrapShsTimeLimitError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapShsTimeLimitError.setStatus("current")


class _MbgLtNgCfgTrapShsTimeLimitWarning_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapShsTimeLimitWarning based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapShsTimeLimitWarning_Object = MibScalar
mbgLtNgCfgTrapShsTimeLimitWarning = _MbgLtNgCfgTrapShsTimeLimitWarning_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 22),
    _MbgLtNgCfgTrapShsTimeLimitWarning_Type()
)
mbgLtNgCfgTrapShsTimeLimitWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapShsTimeLimitWarning.setStatus("current")


class _MbgLtNgCfgTrapNetworkDown_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapNetworkDown based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapNetworkDown_Object = MibScalar
mbgLtNgCfgTrapNetworkDown = _MbgLtNgCfgTrapNetworkDown_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 23),
    _MbgLtNgCfgTrapNetworkDown_Type()
)
mbgLtNgCfgTrapNetworkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapNetworkDown.setStatus("current")


class _MbgLtNgCfgTrapNetworkUp_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapNetworkUp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapNetworkUp_Object = MibScalar
mbgLtNgCfgTrapNetworkUp = _MbgLtNgCfgTrapNetworkUp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 24),
    _MbgLtNgCfgTrapNetworkUp_Type()
)
mbgLtNgCfgTrapNetworkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapNetworkUp.setStatus("current")


class _MbgLtNgCfgTrapPowerSupplyUp_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapPowerSupplyUp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapPowerSupplyUp_Object = MibScalar
mbgLtNgCfgTrapPowerSupplyUp = _MbgLtNgCfgTrapPowerSupplyUp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 25),
    _MbgLtNgCfgTrapPowerSupplyUp_Type()
)
mbgLtNgCfgTrapPowerSupplyUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapPowerSupplyUp.setStatus("current")


class _MbgLtNgCfgTrapPowerSupplyDown_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapPowerSupplyDown based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapPowerSupplyDown_Object = MibScalar
mbgLtNgCfgTrapPowerSupplyDown = _MbgLtNgCfgTrapPowerSupplyDown_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 26),
    _MbgLtNgCfgTrapPowerSupplyDown_Type()
)
mbgLtNgCfgTrapPowerSupplyDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapPowerSupplyDown.setStatus("current")


class _MbgLtNgCfgTrapFdmError_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapFdmError based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapFdmError_Object = MibScalar
mbgLtNgCfgTrapFdmError = _MbgLtNgCfgTrapFdmError_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 27),
    _MbgLtNgCfgTrapFdmError_Type()
)
mbgLtNgCfgTrapFdmError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapFdmError.setStatus("current")


class _MbgLtNgCfgTrapLowSystemResources_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapLowSystemResources based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapLowSystemResources_Object = MibScalar
mbgLtNgCfgTrapLowSystemResources = _MbgLtNgCfgTrapLowSystemResources_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 28),
    _MbgLtNgCfgTrapLowSystemResources_Type()
)
mbgLtNgCfgTrapLowSystemResources.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapLowSystemResources.setStatus("current")


class _MbgLtNgCfgTrapPtpNetworkDown_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapPtpNetworkDown based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapPtpNetworkDown_Object = MibScalar
mbgLtNgCfgTrapPtpNetworkDown = _MbgLtNgCfgTrapPtpNetworkDown_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 29),
    _MbgLtNgCfgTrapPtpNetworkDown_Type()
)
mbgLtNgCfgTrapPtpNetworkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapPtpNetworkDown.setStatus("current")


class _MbgLtNgCfgTrapPtpNetworkUp_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapPtpNetworkUp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapPtpNetworkUp_Object = MibScalar
mbgLtNgCfgTrapPtpNetworkUp = _MbgLtNgCfgTrapPtpNetworkUp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 30),
    _MbgLtNgCfgTrapPtpNetworkUp_Type()
)
mbgLtNgCfgTrapPtpNetworkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapPtpNetworkUp.setStatus("current")


class _MbgLtNgCfgTrapPtpStateChanged_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapPtpStateChanged based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapPtpStateChanged_Object = MibScalar
mbgLtNgCfgTrapPtpStateChanged = _MbgLtNgCfgTrapPtpStateChanged_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 31),
    _MbgLtNgCfgTrapPtpStateChanged_Type()
)
mbgLtNgCfgTrapPtpStateChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapPtpStateChanged.setStatus("current")


class _MbgLtNgCfgTrapPtpError_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapPtpError based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapPtpError_Object = MibScalar
mbgLtNgCfgTrapPtpError = _MbgLtNgCfgTrapPtpError_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 32),
    _MbgLtNgCfgTrapPtpError_Type()
)
mbgLtNgCfgTrapPtpError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapPtpError.setStatus("current")


class _MbgLtNgCfgTrapFanDown_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapFanDown based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapFanDown_Object = MibScalar
mbgLtNgCfgTrapFanDown = _MbgLtNgCfgTrapFanDown_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 33),
    _MbgLtNgCfgTrapFanDown_Type()
)
mbgLtNgCfgTrapFanDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapFanDown.setStatus("current")


class _MbgLtNgCfgTrapFanUp_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapFanUp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapFanUp_Object = MibScalar
mbgLtNgCfgTrapFanUp = _MbgLtNgCfgTrapFanUp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 34),
    _MbgLtNgCfgTrapFanUp_Type()
)
mbgLtNgCfgTrapFanUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapFanUp.setStatus("current")


class _MbgLtNgCfgRepeatEvent_Type(Integer32):
    """Custom type mbgLtNgCfgRepeatEvent based on Integer32"""
    defaultValue = 0

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
        *(("everyDay", 3),
          ("everyHour", 2),
          ("everyMinute", 1),
          ("never", 0))
    )


_MbgLtNgCfgRepeatEvent_Type.__name__ = "Integer32"
_MbgLtNgCfgRepeatEvent_Object = MibScalar
mbgLtNgCfgRepeatEvent = _MbgLtNgCfgRepeatEvent_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 35),
    _MbgLtNgCfgRepeatEvent_Type()
)
mbgLtNgCfgRepeatEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgRepeatEvent.setStatus("current")


class _MbgLtNgCfgRepetitions_Type(Unsigned32):
    """Custom type mbgLtNgCfgRepetitions based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_MbgLtNgCfgRepetitions_Type.__name__ = "Unsigned32"
_MbgLtNgCfgRepetitions_Object = MibScalar
mbgLtNgCfgRepetitions = _MbgLtNgCfgRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 36),
    _MbgLtNgCfgRepetitions_Type()
)
mbgLtNgCfgRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgRepetitions.setStatus("current")


class _MbgLtNgCfgTrapWarmedUp_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapWarmedUp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapWarmedUp_Object = MibScalar
mbgLtNgCfgTrapWarmedUp = _MbgLtNgCfgTrapWarmedUp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 37),
    _MbgLtNgCfgTrapWarmedUp_Type()
)
mbgLtNgCfgTrapWarmedUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapWarmedUp.setStatus("current")


class _MbgLtNgCfgTrapNotWarmedUp_Type(DisplayString):
    """Custom type mbgLtNgCfgTrapNotWarmedUp based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgTrapNotWarmedUp_Object = MibScalar
mbgLtNgCfgTrapNotWarmedUp = _MbgLtNgCfgTrapNotWarmedUp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 1, 6, 38),
    _MbgLtNgCfgTrapNotWarmedUp_Type()
)
mbgLtNgCfgTrapNotWarmedUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgTrapNotWarmedUp.setStatus("current")
_MbgLtNgCfgSecurity_ObjectIdentity = ObjectIdentity
mbgLtNgCfgSecurity = _MbgLtNgCfgSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2)
)
_MbgLtNgCfgLoginAccess_ObjectIdentity = ObjectIdentity
mbgLtNgCfgLoginAccess = _MbgLtNgCfgLoginAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2, 0)
)


class _MbgLtNgCfgDisableRootLogin_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgDisableRootLogin based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgDisableRootLogin_Object = MibScalar
mbgLtNgCfgDisableRootLogin = _MbgLtNgCfgDisableRootLogin_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2, 0, 1),
    _MbgLtNgCfgDisableRootLogin_Type()
)
mbgLtNgCfgDisableRootLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgDisableRootLogin.setStatus("current")


class _MbgLtNgCfgAllowNetworkDiscovery_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgAllowNetworkDiscovery based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgAllowNetworkDiscovery_Object = MibScalar
mbgLtNgCfgAllowNetworkDiscovery = _MbgLtNgCfgAllowNetworkDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2, 0, 2),
    _MbgLtNgCfgAllowNetworkDiscovery_Type()
)
mbgLtNgCfgAllowNetworkDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgAllowNetworkDiscovery.setStatus("current")
_MbgLtNgCfgFrontPanel_ObjectIdentity = ObjectIdentity
mbgLtNgCfgFrontPanel = _MbgLtNgCfgFrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2, 1)
)


class _MbgLtNgCfgLockFrontPanel_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgLockFrontPanel based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgLockFrontPanel_Object = MibScalar
mbgLtNgCfgLockFrontPanel = _MbgLtNgCfgLockFrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2, 1, 1),
    _MbgLtNgCfgLockFrontPanel_Type()
)
mbgLtNgCfgLockFrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgLockFrontPanel.setStatus("current")


class _MbgLtNgCfgDisableUsbPort_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgDisableUsbPort based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgDisableUsbPort_Object = MibScalar
mbgLtNgCfgDisableUsbPort = _MbgLtNgCfgDisableUsbPort_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2, 1, 2),
    _MbgLtNgCfgDisableUsbPort_Type()
)
mbgLtNgCfgDisableUsbPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgDisableUsbPort.setStatus("current")
_MbgLtNgCfgSsh_ObjectIdentity = ObjectIdentity
mbgLtNgCfgSsh = _MbgLtNgCfgSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2, 2)
)


class _MbgLtNgCfgSshKeyLength_Type(Unsigned32):
    """Custom type mbgLtNgCfgSshKeyLength based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(768, 768),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
        ValueRangeConstraint(8192, 8192),
        ValueRangeConstraint(16384, 16384),
        ValueRangeConstraint(32768, 32768),
    )


_MbgLtNgCfgSshKeyLength_Type.__name__ = "Unsigned32"
_MbgLtNgCfgSshKeyLength_Object = MibScalar
mbgLtNgCfgSshKeyLength = _MbgLtNgCfgSshKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2, 2, 1),
    _MbgLtNgCfgSshKeyLength_Type()
)
mbgLtNgCfgSshKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSshKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgCfgSshKeyLength.setUnits("bits")


class _MbgLtNgCfgSshShellTimeout_Type(Unsigned32):
    """Custom type mbgLtNgCfgSshShellTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(3600, 3600),
        ValueRangeConstraint(10800, 10800),
        ValueRangeConstraint(18000, 18000),
        ValueRangeConstraint(86400, 86400),
    )


_MbgLtNgCfgSshShellTimeout_Type.__name__ = "Unsigned32"
_MbgLtNgCfgSshShellTimeout_Object = MibScalar
mbgLtNgCfgSshShellTimeout = _MbgLtNgCfgSshShellTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 2, 2, 2),
    _MbgLtNgCfgSshShellTimeout_Type()
)
mbgLtNgCfgSshShellTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgSshShellTimeout.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgCfgSshShellTimeout.setUnits("seconds")
_MbgLtNgCfgNtp_ObjectIdentity = ObjectIdentity
mbgLtNgCfgNtp = _MbgLtNgCfgNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3)
)
_MbgLtNgCfgNtpTable_Object = MibTable
mbgLtNgCfgNtpTable = _MbgLtNgCfgNtpTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpTable.setStatus("current")
_MbgLtNgCfgNtpTableEntry_Object = MibTableRow
mbgLtNgCfgNtpTableEntry = _MbgLtNgCfgNtpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 1, 1)
)
mbgLtNgCfgNtpTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpTableEntry.setStatus("current")


class _MbgLtNgCfgNtpIndex_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MbgLtNgCfgNtpIndex_Type.__name__ = "Unsigned32"
_MbgLtNgCfgNtpIndex_Object = MibTableColumn
mbgLtNgCfgNtpIndex = _MbgLtNgCfgNtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 1, 1, 1),
    _MbgLtNgCfgNtpIndex_Type()
)
mbgLtNgCfgNtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpIndex.setStatus("current")


class _MbgLtNgCfgNtpServerIP_Type(DisplayString):
    """Custom type mbgLtNgCfgNtpServerIP based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgNtpServerIP_Object = MibTableColumn
mbgLtNgCfgNtpServerIP = _MbgLtNgCfgNtpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 1, 1, 2),
    _MbgLtNgCfgNtpServerIP_Type()
)
mbgLtNgCfgNtpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpServerIP.setStatus("current")


class _MbgLtNgCfgNtpServerKey_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpServerKey based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgLtNgCfgNtpServerKey_Type.__name__ = "Unsigned32"
_MbgLtNgCfgNtpServerKey_Object = MibTableColumn
mbgLtNgCfgNtpServerKey = _MbgLtNgCfgNtpServerKey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 1, 1, 3),
    _MbgLtNgCfgNtpServerKey_Type()
)
mbgLtNgCfgNtpServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpServerKey.setStatus("current")


class _MbgLtNgCfgNtpServerAutokey_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpServerAutokey based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpServerAutokey_Object = MibTableColumn
mbgLtNgCfgNtpServerAutokey = _MbgLtNgCfgNtpServerAutokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 1, 1, 4),
    _MbgLtNgCfgNtpServerAutokey_Type()
)
mbgLtNgCfgNtpServerAutokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpServerAutokey.setStatus("current")


class _MbgLtNgCfgNtpServerMinpoll_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpServerMinpoll based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 10),
    )


_MbgLtNgCfgNtpServerMinpoll_Type.__name__ = "Unsigned32"
_MbgLtNgCfgNtpServerMinpoll_Object = MibTableColumn
mbgLtNgCfgNtpServerMinpoll = _MbgLtNgCfgNtpServerMinpoll_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 1, 1, 5),
    _MbgLtNgCfgNtpServerMinpoll_Type()
)
mbgLtNgCfgNtpServerMinpoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpServerMinpoll.setStatus("current")


class _MbgLtNgCfgNtpServerMaxpoll_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpServerMaxpoll based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 10),
    )


_MbgLtNgCfgNtpServerMaxpoll_Type.__name__ = "Unsigned32"
_MbgLtNgCfgNtpServerMaxpoll_Object = MibTableColumn
mbgLtNgCfgNtpServerMaxpoll = _MbgLtNgCfgNtpServerMaxpoll_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 1, 1, 6),
    _MbgLtNgCfgNtpServerMaxpoll_Type()
)
mbgLtNgCfgNtpServerMaxpoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpServerMaxpoll.setStatus("current")


class _MbgLtNgCfgNtpServerIburst_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpServerIburst based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpServerIburst_Object = MibTableColumn
mbgLtNgCfgNtpServerIburst = _MbgLtNgCfgNtpServerIburst_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 1, 1, 7),
    _MbgLtNgCfgNtpServerIburst_Type()
)
mbgLtNgCfgNtpServerIburst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpServerIburst.setStatus("current")
_MbgLtNgCfgNtpBMTable_Object = MibTable
mbgLtNgCfgNtpBMTable = _MbgLtNgCfgNtpBMTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpBMTable.setStatus("current")
_MbgLtNgCfgNtpBMTableEntry_Object = MibTableRow
mbgLtNgCfgNtpBMTableEntry = _MbgLtNgCfgNtpBMTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 2, 1)
)
mbgLtNgCfgNtpBMTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpBMIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpBMTableEntry.setStatus("current")


class _MbgLtNgCfgNtpBMIndex_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpBMIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MbgLtNgCfgNtpBMIndex_Type.__name__ = "Unsigned32"
_MbgLtNgCfgNtpBMIndex_Object = MibTableColumn
mbgLtNgCfgNtpBMIndex = _MbgLtNgCfgNtpBMIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 2, 1, 1),
    _MbgLtNgCfgNtpBMIndex_Type()
)
mbgLtNgCfgNtpBMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpBMIndex.setStatus("current")


class _MbgLtNgCfgNtpBroadAddr_Type(DisplayString):
    """Custom type mbgLtNgCfgNtpBroadAddr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgNtpBroadAddr_Object = MibTableColumn
mbgLtNgCfgNtpBroadAddr = _MbgLtNgCfgNtpBroadAddr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 2, 1, 2),
    _MbgLtNgCfgNtpBroadAddr_Type()
)
mbgLtNgCfgNtpBroadAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpBroadAddr.setStatus("current")


class _MbgLtNgCfgNtpBroadSymKey_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpBroadSymKey based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MbgLtNgCfgNtpBroadSymKey_Type.__name__ = "Unsigned32"
_MbgLtNgCfgNtpBroadSymKey_Object = MibTableColumn
mbgLtNgCfgNtpBroadSymKey = _MbgLtNgCfgNtpBroadSymKey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 2, 1, 3),
    _MbgLtNgCfgNtpBroadSymKey_Type()
)
mbgLtNgCfgNtpBroadSymKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpBroadSymKey.setStatus("current")


class _MbgLtNgCfgNtpBroadInterval_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpBroadInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MbgLtNgCfgNtpBroadInterval_Type.__name__ = "Unsigned32"
_MbgLtNgCfgNtpBroadInterval_Object = MibTableColumn
mbgLtNgCfgNtpBroadInterval = _MbgLtNgCfgNtpBroadInterval_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 2, 1, 4),
    _MbgLtNgCfgNtpBroadInterval_Type()
)
mbgLtNgCfgNtpBroadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpBroadInterval.setStatus("current")


class _MbgLtNgCfgNtpBroadUseAutokey_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpBroadUseAutokey based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpBroadUseAutokey_Object = MibTableColumn
mbgLtNgCfgNtpBroadUseAutokey = _MbgLtNgCfgNtpBroadUseAutokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 2, 1, 5),
    _MbgLtNgCfgNtpBroadUseAutokey_Type()
)
mbgLtNgCfgNtpBroadUseAutokey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpBroadUseAutokey.setStatus("current")


class _MbgLtNgCfgNtpEnableMulticast_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpEnableMulticast based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpEnableMulticast_Object = MibScalar
mbgLtNgCfgNtpEnableMulticast = _MbgLtNgCfgNtpEnableMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 3),
    _MbgLtNgCfgNtpEnableMulticast_Type()
)
mbgLtNgCfgNtpEnableMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpEnableMulticast.setStatus("current")


class _MbgLtNgCfgNtpMultiAddr_Type(DisplayString):
    """Custom type mbgLtNgCfgNtpMultiAddr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgNtpMultiAddr_Object = MibScalar
mbgLtNgCfgNtpMultiAddr = _MbgLtNgCfgNtpMultiAddr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 4),
    _MbgLtNgCfgNtpMultiAddr_Type()
)
mbgLtNgCfgNtpMultiAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpMultiAddr.setStatus("current")


class _MbgLtNgCfgNtpMultiInterval_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpMultiInterval based on Unsigned32"""
    defaultValue = 0


_MbgLtNgCfgNtpMultiInterval_Object = MibScalar
mbgLtNgCfgNtpMultiInterval = _MbgLtNgCfgNtpMultiInterval_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 5),
    _MbgLtNgCfgNtpMultiInterval_Type()
)
mbgLtNgCfgNtpMultiInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpMultiInterval.setStatus("current")


class _MbgLtNgCfgNtpMultiSymKey_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpMultiSymKey based on Unsigned32"""
    defaultValue = 0


_MbgLtNgCfgNtpMultiSymKey_Object = MibScalar
mbgLtNgCfgNtpMultiSymKey = _MbgLtNgCfgNtpMultiSymKey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 6),
    _MbgLtNgCfgNtpMultiSymKey_Type()
)
mbgLtNgCfgNtpMultiSymKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpMultiSymKey.setStatus("current")


class _MbgLtNgCfgNtpMultiUseAutokey_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpMultiUseAutokey based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpMultiUseAutokey_Object = MibScalar
mbgLtNgCfgNtpMultiUseAutokey = _MbgLtNgCfgNtpMultiUseAutokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 7),
    _MbgLtNgCfgNtpMultiUseAutokey_Type()
)
mbgLtNgCfgNtpMultiUseAutokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpMultiUseAutokey.setStatus("current")


class _MbgLtNgCfgNtpEnableManycast_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpEnableManycast based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpEnableManycast_Object = MibScalar
mbgLtNgCfgNtpEnableManycast = _MbgLtNgCfgNtpEnableManycast_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 8),
    _MbgLtNgCfgNtpEnableManycast_Type()
)
mbgLtNgCfgNtpEnableManycast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpEnableManycast.setStatus("current")


class _MbgLtNgCfgNtpManyAddr_Type(DisplayString):
    """Custom type mbgLtNgCfgNtpManyAddr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgNtpManyAddr_Object = MibScalar
mbgLtNgCfgNtpManyAddr = _MbgLtNgCfgNtpManyAddr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 9),
    _MbgLtNgCfgNtpManyAddr_Type()
)
mbgLtNgCfgNtpManyAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpManyAddr.setStatus("current")


class _MbgLtNgCfgNtpManySymKey_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpManySymKey based on Unsigned32"""
    defaultValue = 0


_MbgLtNgCfgNtpManySymKey_Object = MibScalar
mbgLtNgCfgNtpManySymKey = _MbgLtNgCfgNtpManySymKey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 11),
    _MbgLtNgCfgNtpManySymKey_Type()
)
mbgLtNgCfgNtpManySymKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpManySymKey.setStatus("current")


class _MbgLtNgCfgNtpManyUseAutokey_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpManyUseAutokey based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpManyUseAutokey_Object = MibScalar
mbgLtNgCfgNtpManyUseAutokey = _MbgLtNgCfgNtpManyUseAutokey_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 12),
    _MbgLtNgCfgNtpManyUseAutokey_Type()
)
mbgLtNgCfgNtpManyUseAutokey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpManyUseAutokey.setStatus("current")


class _MbgLtNgCfgNtpLocalClkStratum_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpLocalClkStratum based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MbgLtNgCfgNtpLocalClkStratum_Type.__name__ = "Unsigned32"
_MbgLtNgCfgNtpLocalClkStratum_Object = MibScalar
mbgLtNgCfgNtpLocalClkStratum = _MbgLtNgCfgNtpLocalClkStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 13),
    _MbgLtNgCfgNtpLocalClkStratum_Type()
)
mbgLtNgCfgNtpLocalClkStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpLocalClkStratum.setStatus("current")


class _MbgLtNgCfgNtpDisableLocalClk_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpDisableLocalClk based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpDisableLocalClk_Object = MibScalar
mbgLtNgCfgNtpDisableLocalClk = _MbgLtNgCfgNtpDisableLocalClk_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 14),
    _MbgLtNgCfgNtpDisableLocalClk_Type()
)
mbgLtNgCfgNtpDisableLocalClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpDisableLocalClk.setStatus("current")


class _MbgLtNgCfgNtpSpoofLocalTime_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpSpoofLocalTime based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpSpoofLocalTime_Object = MibScalar
mbgLtNgCfgNtpSpoofLocalTime = _MbgLtNgCfgNtpSpoofLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 15),
    _MbgLtNgCfgNtpSpoofLocalTime_Type()
)
mbgLtNgCfgNtpSpoofLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpSpoofLocalTime.setStatus("obsolete")


class _MbgLtNgCfgNtpLocalTrustedKeys_Type(DisplayString):
    """Custom type mbgLtNgCfgNtpLocalTrustedKeys based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgNtpLocalTrustedKeys_Object = MibScalar
mbgLtNgCfgNtpLocalTrustedKeys = _MbgLtNgCfgNtpLocalTrustedKeys_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 16),
    _MbgLtNgCfgNtpLocalTrustedKeys_Type()
)
mbgLtNgCfgNtpLocalTrustedKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpLocalTrustedKeys.setStatus("current")


class _MbgLtNgCfgNtpTrusttime_Type(Unsigned32):
    """Custom type mbgLtNgCfgNtpTrusttime based on Unsigned32"""
    defaultValue = 0


_MbgLtNgCfgNtpTrusttime_Object = MibScalar
mbgLtNgCfgNtpTrusttime = _MbgLtNgCfgNtpTrusttime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 17),
    _MbgLtNgCfgNtpTrusttime_Type()
)
mbgLtNgCfgNtpTrusttime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpTrusttime.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpTrusttime.setUnits("seconds")


class _MbgLtNgCfgNtpTimeScale_Type(Integer32):
    """Custom type mbgLtNgCfgNtpTimeScale based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("utc", 0))
    )


_MbgLtNgCfgNtpTimeScale_Type.__name__ = "Integer32"
_MbgLtNgCfgNtpTimeScale_Object = MibScalar
mbgLtNgCfgNtpTimeScale = _MbgLtNgCfgNtpTimeScale_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 18),
    _MbgLtNgCfgNtpTimeScale_Type()
)
mbgLtNgCfgNtpTimeScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpTimeScale.setStatus("current")


class _MbgLtNgCfgNtpEnableClientCounter_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgNtpEnableClientCounter based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgNtpEnableClientCounter_Object = MibScalar
mbgLtNgCfgNtpEnableClientCounter = _MbgLtNgCfgNtpEnableClientCounter_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 19),
    _MbgLtNgCfgNtpEnableClientCounter_Type()
)
mbgLtNgCfgNtpEnableClientCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpEnableClientCounter.setStatus("current")


class _MbgLtNgCfgNtpEnableClientCounterDuration_Type(Integer32):
    """Custom type mbgLtNgCfgNtpEnableClientCounterDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MbgLtNgCfgNtpEnableClientCounterDuration_Type.__name__ = "Integer32"
_MbgLtNgCfgNtpEnableClientCounterDuration_Object = MibScalar
mbgLtNgCfgNtpEnableClientCounterDuration = _MbgLtNgCfgNtpEnableClientCounterDuration_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 3, 20),
    _MbgLtNgCfgNtpEnableClientCounterDuration_Type()
)
mbgLtNgCfgNtpEnableClientCounterDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpEnableClientCounterDuration.setStatus("current")
if mibBuilder.loadTexts:
    mbgLtNgCfgNtpEnableClientCounterDuration.setUnits("seconds")
_MbgLtNgCfgPtp_ObjectIdentity = ObjectIdentity
mbgLtNgCfgPtp = _MbgLtNgCfgPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4)
)
_MbgLtNgCfgPtpTable_Object = MibTable
mbgLtNgCfgPtpTable = _MbgLtNgCfgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpTable.setStatus("current")
_MbgLtNgCfgPtpTableEntry_Object = MibTableRow
mbgLtNgCfgPtpTableEntry = _MbgLtNgCfgPtpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1)
)
mbgLtNgCfgPtpTableEntry.setIndexNames(
    (0, "MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpIndex"),
)
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpTableEntry.setStatus("current")
_MbgLtNgCfgPtpIndex_Type = Unsigned32
_MbgLtNgCfgPtpIndex_Object = MibTableColumn
mbgLtNgCfgPtpIndex = _MbgLtNgCfgPtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 1),
    _MbgLtNgCfgPtpIndex_Type()
)
mbgLtNgCfgPtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpIndex.setStatus("current")


class _MbgLtNgCfgPtpHostname_Type(DisplayString):
    """Custom type mbgLtNgCfgPtpHostname based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPtpHostname_Object = MibTableColumn
mbgLtNgCfgPtpHostname = _MbgLtNgCfgPtpHostname_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 2),
    _MbgLtNgCfgPtpHostname_Type()
)
mbgLtNgCfgPtpHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpHostname.setStatus("current")


class _MbgLtNgCfgPtpDomainname_Type(DisplayString):
    """Custom type mbgLtNgCfgPtpDomainname based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPtpDomainname_Object = MibTableColumn
mbgLtNgCfgPtpDomainname = _MbgLtNgCfgPtpDomainname_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 3),
    _MbgLtNgCfgPtpDomainname_Type()
)
mbgLtNgCfgPtpDomainname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpDomainname.setStatus("current")


class _MbgLtNgCfgPtpNameserver1_Type(DisplayString):
    """Custom type mbgLtNgCfgPtpNameserver1 based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPtpNameserver1_Object = MibTableColumn
mbgLtNgCfgPtpNameserver1 = _MbgLtNgCfgPtpNameserver1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 4),
    _MbgLtNgCfgPtpNameserver1_Type()
)
mbgLtNgCfgPtpNameserver1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpNameserver1.setStatus("current")


class _MbgLtNgCfgPtpNameserver2_Type(DisplayString):
    """Custom type mbgLtNgCfgPtpNameserver2 based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPtpNameserver2_Object = MibTableColumn
mbgLtNgCfgPtpNameserver2 = _MbgLtNgCfgPtpNameserver2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 5),
    _MbgLtNgCfgPtpNameserver2_Type()
)
mbgLtNgCfgPtpNameserver2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpNameserver2.setStatus("current")


class _MbgLtNgCfgPtpIpv4_Type(DisplayString):
    """Custom type mbgLtNgCfgPtpIpv4 based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPtpIpv4_Object = MibTableColumn
mbgLtNgCfgPtpIpv4 = _MbgLtNgCfgPtpIpv4_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 6),
    _MbgLtNgCfgPtpIpv4_Type()
)
mbgLtNgCfgPtpIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpIpv4.setStatus("current")


class _MbgLtNgCfgPtpNetmask_Type(DisplayString):
    """Custom type mbgLtNgCfgPtpNetmask based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPtpNetmask_Object = MibTableColumn
mbgLtNgCfgPtpNetmask = _MbgLtNgCfgPtpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 7),
    _MbgLtNgCfgPtpNetmask_Type()
)
mbgLtNgCfgPtpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpNetmask.setStatus("current")


class _MbgLtNgCfgPtpGateway_Type(DisplayString):
    """Custom type mbgLtNgCfgPtpGateway based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPtpGateway_Object = MibTableColumn
mbgLtNgCfgPtpGateway = _MbgLtNgCfgPtpGateway_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 8),
    _MbgLtNgCfgPtpGateway_Type()
)
mbgLtNgCfgPtpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpGateway.setStatus("current")


class _MbgLtNgCfgPtpEnableVlan_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPtpEnableVlan based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgPtpEnableVlan_Object = MibTableColumn
mbgLtNgCfgPtpEnableVlan = _MbgLtNgCfgPtpEnableVlan_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 9),
    _MbgLtNgCfgPtpEnableVlan_Type()
)
mbgLtNgCfgPtpEnableVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpEnableVlan.setStatus("current")


class _MbgLtNgCfgPtpVlanId_Type(Unsigned32):
    """Custom type mbgLtNgCfgPtpVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MbgLtNgCfgPtpVlanId_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPtpVlanId_Object = MibTableColumn
mbgLtNgCfgPtpVlanId = _MbgLtNgCfgPtpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 10),
    _MbgLtNgCfgPtpVlanId_Type()
)
mbgLtNgCfgPtpVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpVlanId.setStatus("current")


class _MbgLtNgCfgPtpVlanPriority_Type(Unsigned32):
    """Custom type mbgLtNgCfgPtpVlanPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MbgLtNgCfgPtpVlanPriority_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPtpVlanPriority_Object = MibTableColumn
mbgLtNgCfgPtpVlanPriority = _MbgLtNgCfgPtpVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 11),
    _MbgLtNgCfgPtpVlanPriority_Type()
)
mbgLtNgCfgPtpVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpVlanPriority.setStatus("current")


class _MbgLtNgCfgPtpEnableDhcp_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPtpEnableDhcp based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgPtpEnableDhcp_Object = MibTableColumn
mbgLtNgCfgPtpEnableDhcp = _MbgLtNgCfgPtpEnableDhcp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 12),
    _MbgLtNgCfgPtpEnableDhcp_Type()
)
mbgLtNgCfgPtpEnableDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpEnableDhcp.setStatus("current")


class _MbgLtNgCfgPtpMode_Type(Integer32):
    """Custom type mbgLtNgCfgPtpMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bothMaster", 5),
          ("multicastAuto", 4),
          ("multicastMaster", 2),
          ("multicastSlave", 0),
          ("ntpClient", 7),
          ("ntpServer", 6),
          ("unicastMaster", 3),
          ("unicastSlave", 1))
    )


_MbgLtNgCfgPtpMode_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpMode_Object = MibTableColumn
mbgLtNgCfgPtpMode = _MbgLtNgCfgPtpMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 13),
    _MbgLtNgCfgPtpMode_Type()
)
mbgLtNgCfgPtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpMode.setStatus("current")


class _MbgLtNgCfgPtpDelayMechanism_Type(Integer32):
    """Custom type mbgLtNgCfgPtpDelayMechanism based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 0),
          ("p2p", 1))
    )


_MbgLtNgCfgPtpDelayMechanism_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpDelayMechanism_Object = MibTableColumn
mbgLtNgCfgPtpDelayMechanism = _MbgLtNgCfgPtpDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 14),
    _MbgLtNgCfgPtpDelayMechanism_Type()
)
mbgLtNgCfgPtpDelayMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpDelayMechanism.setStatus("current")


class _MbgLtNgCfgPtpNetworkProtocol_Type(Integer32):
    """Custom type mbgLtNgCfgPtpNetworkProtocol based on Integer32"""
    defaultValue = 0

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
        *(("ieee8023", 3),
          ("reserved", 0),
          ("udpIpv4", 1),
          ("udpIpv6", 2))
    )


_MbgLtNgCfgPtpNetworkProtocol_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpNetworkProtocol_Object = MibTableColumn
mbgLtNgCfgPtpNetworkProtocol = _MbgLtNgCfgPtpNetworkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 15),
    _MbgLtNgCfgPtpNetworkProtocol_Type()
)
mbgLtNgCfgPtpNetworkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpNetworkProtocol.setStatus("current")


class _MbgLtNgCfgPtpDomainNumber_Type(Unsigned32):
    """Custom type mbgLtNgCfgPtpDomainNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgLtNgCfgPtpDomainNumber_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPtpDomainNumber_Object = MibTableColumn
mbgLtNgCfgPtpDomainNumber = _MbgLtNgCfgPtpDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 16),
    _MbgLtNgCfgPtpDomainNumber_Type()
)
mbgLtNgCfgPtpDomainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpDomainNumber.setStatus("current")


class _MbgLtNgCfgPtpPriority1_Type(Unsigned32):
    """Custom type mbgLtNgCfgPtpPriority1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgLtNgCfgPtpPriority1_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPtpPriority1_Object = MibTableColumn
mbgLtNgCfgPtpPriority1 = _MbgLtNgCfgPtpPriority1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 17),
    _MbgLtNgCfgPtpPriority1_Type()
)
mbgLtNgCfgPtpPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpPriority1.setStatus("current")


class _MbgLtNgCfgPtpPriority2_Type(Unsigned32):
    """Custom type mbgLtNgCfgPtpPriority2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgLtNgCfgPtpPriority2_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPtpPriority2_Object = MibTableColumn
mbgLtNgCfgPtpPriority2 = _MbgLtNgCfgPtpPriority2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 18),
    _MbgLtNgCfgPtpPriority2_Type()
)
mbgLtNgCfgPtpPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpPriority2.setStatus("current")


class _MbgLtNgCfgPtpSyncInterval_Type(Integer32):
    """Custom type mbgLtNgCfgPtpSyncInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_MbgLtNgCfgPtpSyncInterval_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpSyncInterval_Object = MibTableColumn
mbgLtNgCfgPtpSyncInterval = _MbgLtNgCfgPtpSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 19),
    _MbgLtNgCfgPtpSyncInterval_Type()
)
mbgLtNgCfgPtpSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpSyncInterval.setStatus("current")


class _MbgLtNgCfgPtpAnnounceInterval_Type(Integer32):
    """Custom type mbgLtNgCfgPtpAnnounceInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_MbgLtNgCfgPtpAnnounceInterval_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpAnnounceInterval_Object = MibTableColumn
mbgLtNgCfgPtpAnnounceInterval = _MbgLtNgCfgPtpAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 20),
    _MbgLtNgCfgPtpAnnounceInterval_Type()
)
mbgLtNgCfgPtpAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpAnnounceInterval.setStatus("current")


class _MbgLtNgCfgPtpDelayReqInterval_Type(Integer32):
    """Custom type mbgLtNgCfgPtpDelayReqInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_MbgLtNgCfgPtpDelayReqInterval_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpDelayReqInterval_Object = MibTableColumn
mbgLtNgCfgPtpDelayReqInterval = _MbgLtNgCfgPtpDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 21),
    _MbgLtNgCfgPtpDelayReqInterval_Type()
)
mbgLtNgCfgPtpDelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpDelayReqInterval.setStatus("current")


class _MbgLtNgCfgPtpTimescale_Type(Integer32):
    """Custom type mbgLtNgCfgPtpTimescale based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arbitrary", 0),
          ("ptp", 1))
    )


_MbgLtNgCfgPtpTimescale_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpTimescale_Object = MibTableColumn
mbgLtNgCfgPtpTimescale = _MbgLtNgCfgPtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 22),
    _MbgLtNgCfgPtpTimescale_Type()
)
mbgLtNgCfgPtpTimescale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpTimescale.setStatus("current")


class _MbgLtNgCfgPtpIpv6Avail_Type(Integer32):
    """Custom type mbgLtNgCfgPtpIpv6Avail based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MbgLtNgCfgPtpIpv6Avail_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpIpv6Avail_Object = MibTableColumn
mbgLtNgCfgPtpIpv6Avail = _MbgLtNgCfgPtpIpv6Avail_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 23),
    _MbgLtNgCfgPtpIpv6Avail_Type()
)
mbgLtNgCfgPtpIpv6Avail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpIpv6Avail.setStatus("current")


class _MbgLtNgCfgPtpIpv6Mode_Type(Integer32):
    """Custom type mbgLtNgCfgPtpIpv6Mode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("ra", 1),
          ("static", 0))
    )


_MbgLtNgCfgPtpIpv6Mode_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpIpv6Mode_Object = MibTableColumn
mbgLtNgCfgPtpIpv6Mode = _MbgLtNgCfgPtpIpv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 24),
    _MbgLtNgCfgPtpIpv6Mode_Type()
)
mbgLtNgCfgPtpIpv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpIpv6Mode.setStatus("current")


class _MbgLtNgCfgPtpIpv6Address_Type(DisplayString):
    """Custom type mbgLtNgCfgPtpIpv6Address based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPtpIpv6Address_Object = MibTableColumn
mbgLtNgCfgPtpIpv6Address = _MbgLtNgCfgPtpIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 25),
    _MbgLtNgCfgPtpIpv6Address_Type()
)
mbgLtNgCfgPtpIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpIpv6Address.setStatus("current")


class _MbgLtNgCfgPtpIpv6McastScope_Type(Integer32):
    """Custom type mbgLtNgCfgPtpIpv6McastScope based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              14)
        )
    )
    namedValues = NamedValues(
        *(("adminLocal", 4),
          ("globalScope", 14),
          ("intfLocal", 1),
          ("linkLocal", 2),
          ("orgaLocal", 8),
          ("realmLocal", 3),
          ("siteLocal", 5))
    )


_MbgLtNgCfgPtpIpv6McastScope_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpIpv6McastScope_Object = MibTableColumn
mbgLtNgCfgPtpIpv6McastScope = _MbgLtNgCfgPtpIpv6McastScope_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 26),
    _MbgLtNgCfgPtpIpv6McastScope_Type()
)
mbgLtNgCfgPtpIpv6McastScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpIpv6McastScope.setStatus("current")


class _MbgLtNgCfgPtpDisableSsh_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPtpDisableSsh based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgPtpDisableSsh_Object = MibTableColumn
mbgLtNgCfgPtpDisableSsh = _MbgLtNgCfgPtpDisableSsh_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 27),
    _MbgLtNgCfgPtpDisableSsh_Type()
)
mbgLtNgCfgPtpDisableSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpDisableSsh.setStatus("current")


class _MbgLtNgCfgPtpDscpClass_Type(Unsigned32):
    """Custom type mbgLtNgCfgPtpDscpClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_MbgLtNgCfgPtpDscpClass_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPtpDscpClass_Object = MibTableColumn
mbgLtNgCfgPtpDscpClass = _MbgLtNgCfgPtpDscpClass_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 28),
    _MbgLtNgCfgPtpDscpClass_Type()
)
mbgLtNgCfgPtpDscpClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpDscpClass.setStatus("current")


class _MbgLtNgCfgPtpMcastTtl_Type(Unsigned32):
    """Custom type mbgLtNgCfgPtpMcastTtl based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbgLtNgCfgPtpMcastTtl_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPtpMcastTtl_Object = MibTableColumn
mbgLtNgCfgPtpMcastTtl = _MbgLtNgCfgPtpMcastTtl_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 29),
    _MbgLtNgCfgPtpMcastTtl_Type()
)
mbgLtNgCfgPtpMcastTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpMcastTtl.setStatus("current")


class _MbgLtNgCfgPtpOpMode_Type(Integer32):
    """Custom type mbgLtNgCfgPtpOpMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ntp", 1),
          ("ptp", 0))
    )


_MbgLtNgCfgPtpOpMode_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpOpMode_Object = MibTableColumn
mbgLtNgCfgPtpOpMode = _MbgLtNgCfgPtpOpMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 30),
    _MbgLtNgCfgPtpOpMode_Type()
)
mbgLtNgCfgPtpOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpOpMode.setStatus("current")


class _MbgLtNgCfgPtpProfile_Type(Integer32):
    """Custom type mbgLtNgCfgPtpProfile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("custom", 0),
          ("defE2eIeee15882008", 1),
          ("defP2pIeee15882008", 2),
          ("powIeeeC37238", 3),
          ("smpteSt20592", 6),
          ("telItuTG82651", 4),
          ("telItuTG82751", 5))
    )


_MbgLtNgCfgPtpProfile_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpProfile_Object = MibTableColumn
mbgLtNgCfgPtpProfile = _MbgLtNgCfgPtpProfile_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 31),
    _MbgLtNgCfgPtpProfile_Type()
)
mbgLtNgCfgPtpProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpProfile.setStatus("current")


class _MbgLtNgCfgPtpHybridMode_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPtpHybridMode based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgPtpHybridMode_Object = MibTableColumn
mbgLtNgCfgPtpHybridMode = _MbgLtNgCfgPtpHybridMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 32),
    _MbgLtNgCfgPtpHybridMode_Type()
)
mbgLtNgCfgPtpHybridMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpHybridMode.setStatus("current")


class _MbgLtNgCfgPtpUcastMstAddr_Type(DisplayString):
    """Custom type mbgLtNgCfgPtpUcastMstAddr based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCfgPtpUcastMstAddr_Object = MibTableColumn
mbgLtNgCfgPtpUcastMstAddr = _MbgLtNgCfgPtpUcastMstAddr_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 33),
    _MbgLtNgCfgPtpUcastMstAddr_Type()
)
mbgLtNgCfgPtpUcastMstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpUcastMstAddr.setStatus("current")


class _MbgLtNgCfgPtpAnnRcptTmout_Type(Unsigned32):
    """Custom type mbgLtNgCfgPtpAnnRcptTmout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_MbgLtNgCfgPtpAnnRcptTmout_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPtpAnnRcptTmout_Object = MibTableColumn
mbgLtNgCfgPtpAnnRcptTmout = _MbgLtNgCfgPtpAnnRcptTmout_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 34),
    _MbgLtNgCfgPtpAnnRcptTmout_Type()
)
mbgLtNgCfgPtpAnnRcptTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpAnnRcptTmout.setStatus("current")


class _MbgLtNgCfgPtpMessageDuration_Type(Unsigned32):
    """Custom type mbgLtNgCfgPtpMessageDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_MbgLtNgCfgPtpMessageDuration_Type.__name__ = "Unsigned32"
_MbgLtNgCfgPtpMessageDuration_Object = MibTableColumn
mbgLtNgCfgPtpMessageDuration = _MbgLtNgCfgPtpMessageDuration_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 35),
    _MbgLtNgCfgPtpMessageDuration_Type()
)
mbgLtNgCfgPtpMessageDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpMessageDuration.setStatus("current")


class _MbgLtNgCfgPtpSyncEAvail_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPtpSyncEAvail based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgPtpSyncEAvail_Object = MibTableColumn
mbgLtNgCfgPtpSyncEAvail = _MbgLtNgCfgPtpSyncEAvail_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 36),
    _MbgLtNgCfgPtpSyncEAvail_Type()
)
mbgLtNgCfgPtpSyncEAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpSyncEAvail.setStatus("current")


class _MbgLtNgCfgPtpSyncEEnabled_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPtpSyncEEnabled based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgPtpSyncEEnabled_Object = MibTableColumn
mbgLtNgCfgPtpSyncEEnabled = _MbgLtNgCfgPtpSyncEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 37),
    _MbgLtNgCfgPtpSyncEEnabled_Type()
)
mbgLtNgCfgPtpSyncEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpSyncEEnabled.setStatus("current")


class _MbgLtNgCfgPtpSyncEQltLvlSelEnable_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPtpSyncEQltLvlSelEnable based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgPtpSyncEQltLvlSelEnable_Object = MibTableColumn
mbgLtNgCfgPtpSyncEQltLvlSelEnable = _MbgLtNgCfgPtpSyncEQltLvlSelEnable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 38),
    _MbgLtNgCfgPtpSyncEQltLvlSelEnable_Type()
)
mbgLtNgCfgPtpSyncEQltLvlSelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpSyncEQltLvlSelEnable.setStatus("current")


class _MbgLtNgCfgPtpSyncESdhNwOption_Type(Integer32):
    """Custom type mbgLtNgCfgPtpSyncESdhNwOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("opt1", 0),
          ("opt2", 1))
    )


_MbgLtNgCfgPtpSyncESdhNwOption_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpSyncESdhNwOption_Object = MibTableColumn
mbgLtNgCfgPtpSyncESdhNwOption = _MbgLtNgCfgPtpSyncESdhNwOption_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 39),
    _MbgLtNgCfgPtpSyncESdhNwOption_Type()
)
mbgLtNgCfgPtpSyncESdhNwOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpSyncESdhNwOption.setStatus("current")


class _MbgLtNgCfgPtpSyncEInputSsm_Type(Integer32):
    """Custom type mbgLtNgCfgPtpSyncEInputSsm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("dnuDus", 15),
          ("eec1Sec", 11),
          ("eec2St3", 10),
          ("inv3", 3),
          ("inv5", 5),
          ("inv6", 6),
          ("inv9", 9),
          ("prc", 2),
          ("prov", 14),
          ("prs", 1),
          ("smc", 12),
          ("ssuATnc", 4),
          ("ssuB", 8),
          ("st2", 7),
          ("st3e", 13),
          ("stuUkn", 0))
    )


_MbgLtNgCfgPtpSyncEInputSsm_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpSyncEInputSsm_Object = MibTableColumn
mbgLtNgCfgPtpSyncEInputSsm = _MbgLtNgCfgPtpSyncEInputSsm_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 40),
    _MbgLtNgCfgPtpSyncEInputSsm_Type()
)
mbgLtNgCfgPtpSyncEInputSsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpSyncEInputSsm.setStatus("current")


class _MbgLtNgCfgPtpSyncEOutputSsm_Type(Integer32):
    """Custom type mbgLtNgCfgPtpSyncEOutputSsm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("dnuDus", 15),
          ("eec1Sec", 11),
          ("eec2St3", 10),
          ("inv3", 3),
          ("inv5", 5),
          ("inv6", 6),
          ("inv9", 9),
          ("prc", 2),
          ("prov", 14),
          ("prs", 1),
          ("smc", 12),
          ("ssuATnc", 4),
          ("ssuB", 8),
          ("st2", 7),
          ("st3e", 13),
          ("stuUkn", 0))
    )


_MbgLtNgCfgPtpSyncEOutputSsm_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpSyncEOutputSsm_Object = MibTableColumn
mbgLtNgCfgPtpSyncEOutputSsm = _MbgLtNgCfgPtpSyncEOutputSsm_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 41),
    _MbgLtNgCfgPtpSyncEOutputSsm_Type()
)
mbgLtNgCfgPtpSyncEOutputSsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpSyncEOutputSsm.setStatus("current")


class _MbgLtNgCfgPtpSyncEGbitCopperMode_Type(Integer32):
    """Custom type mbgLtNgCfgPtpSyncEGbitCopperMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("forceOrIsMaster", 2),
          ("forceOrIsSlave", 3),
          ("forceSyncEAuto", 1),
          ("preferMaster", 4),
          ("preferSlave", 5))
    )


_MbgLtNgCfgPtpSyncEGbitCopperMode_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpSyncEGbitCopperMode_Object = MibTableColumn
mbgLtNgCfgPtpSyncEGbitCopperMode = _MbgLtNgCfgPtpSyncEGbitCopperMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 42),
    _MbgLtNgCfgPtpSyncEGbitCopperMode_Type()
)
mbgLtNgCfgPtpSyncEGbitCopperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpSyncEGbitCopperMode.setStatus("current")


class _MbgLtNgCfgPtpMiscEnable1Step_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPtpMiscEnable1Step based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgPtpMiscEnable1Step_Object = MibTableColumn
mbgLtNgCfgPtpMiscEnable1Step = _MbgLtNgCfgPtpMiscEnable1Step_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 43),
    _MbgLtNgCfgPtpMiscEnable1Step_Type()
)
mbgLtNgCfgPtpMiscEnable1Step.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpMiscEnable1Step.setStatus("current")


class _MbgLtNgCfgPtpDisableMgmtMsgs_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgPtpDisableMgmtMsgs based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgPtpDisableMgmtMsgs_Object = MibTableColumn
mbgLtNgCfgPtpDisableMgmtMsgs = _MbgLtNgCfgPtpDisableMgmtMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 44),
    _MbgLtNgCfgPtpDisableMgmtMsgs_Type()
)
mbgLtNgCfgPtpDisableMgmtMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpDisableMgmtMsgs.setStatus("current")


class _MbgLtNgCfgPtpOutput1_Type(Integer32):
    """Custom type mbgLtNgCfgPtpOutput1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("khzGPS2048", 3),
          ("mhz10", 2),
          ("mhzGPS10", 4),
          ("off", 0),
          ("pps", 1),
          ("ppsGPS", 5))
    )


_MbgLtNgCfgPtpOutput1_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpOutput1_Object = MibTableColumn
mbgLtNgCfgPtpOutput1 = _MbgLtNgCfgPtpOutput1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 45),
    _MbgLtNgCfgPtpOutput1_Type()
)
mbgLtNgCfgPtpOutput1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpOutput1.setStatus("current")


class _MbgLtNgCfgPtpOutput2_Type(Integer32):
    """Custom type mbgLtNgCfgPtpOutput2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("khzGPS2048", 3),
          ("mhz10", 2),
          ("mhzGPS10", 4),
          ("off", 0),
          ("pps", 1),
          ("ppsGPS", 5))
    )


_MbgLtNgCfgPtpOutput2_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpOutput2_Object = MibTableColumn
mbgLtNgCfgPtpOutput2 = _MbgLtNgCfgPtpOutput2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 1, 1, 46),
    _MbgLtNgCfgPtpOutput2_Type()
)
mbgLtNgCfgPtpOutput2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpOutput2.setStatus("current")


class _MbgLtNgCfgPtpCmd_Type(Integer32):
    """Custom type mbgLtNgCfgPtpCmd based on Integer32"""
    defaultValue = 0

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
        *(("apply", 3),
          ("configure", 1),
          ("none", 0),
          ("reset", 2))
    )


_MbgLtNgCfgPtpCmd_Type.__name__ = "Integer32"
_MbgLtNgCfgPtpCmd_Object = MibScalar
mbgLtNgCfgPtpCmd = _MbgLtNgCfgPtpCmd_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 4, 2),
    _MbgLtNgCfgPtpCmd_Type()
)
mbgLtNgCfgPtpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgPtpCmd.setStatus("current")
_MbgLtNgCfgSystem_ObjectIdentity = ObjectIdentity
mbgLtNgCfgSystem = _MbgLtNgCfgSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 5)
)
_MbgLtNgCfgGeneral_ObjectIdentity = ObjectIdentity
mbgLtNgCfgGeneral = _MbgLtNgCfgGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 5, 0)
)


class _MbgLtNgCfgWebLanguage_Type(Integer32):
    """Custom type mbgLtNgCfgWebLanguage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("englisch", 1),
          ("german", 2),
          ("notAvailable", 0))
    )


_MbgLtNgCfgWebLanguage_Type.__name__ = "Integer32"
_MbgLtNgCfgWebLanguage_Object = MibScalar
mbgLtNgCfgWebLanguage = _MbgLtNgCfgWebLanguage_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 5, 0, 1),
    _MbgLtNgCfgWebLanguage_Type()
)
mbgLtNgCfgWebLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgCfgWebLanguage.setStatus("current")


class _MbgLtNgCfgActivateChangesAsStartup_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgActivateChangesAsStartup based on MeinbergSwitch"""
    defaultValue = 1


_MbgLtNgCfgActivateChangesAsStartup_Object = MibScalar
mbgLtNgCfgActivateChangesAsStartup = _MbgLtNgCfgActivateChangesAsStartup_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 5, 0, 2),
    _MbgLtNgCfgActivateChangesAsStartup_Type()
)
mbgLtNgCfgActivateChangesAsStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgActivateChangesAsStartup.setStatus("current")
_MbgLtNgCfgDisplay_ObjectIdentity = ObjectIdentity
mbgLtNgCfgDisplay = _MbgLtNgCfgDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 5, 1)
)


class _MbgLtNgCfgEnableFrontPanelLight_Type(MeinbergSwitch):
    """Custom type mbgLtNgCfgEnableFrontPanelLight based on MeinbergSwitch"""
    defaultValue = 0


_MbgLtNgCfgEnableFrontPanelLight_Object = MibScalar
mbgLtNgCfgEnableFrontPanelLight = _MbgLtNgCfgEnableFrontPanelLight_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 1, 5, 1, 1),
    _MbgLtNgCfgEnableFrontPanelLight_Type()
)
mbgLtNgCfgEnableFrontPanelLight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCfgEnableFrontPanelLight.setStatus("current")
_MbgLtNgCommands_ObjectIdentity = ObjectIdentity
mbgLtNgCommands = _MbgLtNgCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 2)
)


class _MbgLtNgCmdExecute_Type(Integer32):
    """Custom type mbgLtNgCmdExecute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("applyChanges", 1),
          ("none", 0),
          ("reboot", 5),
          ("resendErrorConditions", 6),
          ("saveAndApplyChanges", 3),
          ("saveChanges", 2),
          ("sendTestNotifications", 7),
          ("startFirmwareUpdate", 4))
    )


_MbgLtNgCmdExecute_Type.__name__ = "Integer32"
_MbgLtNgCmdExecute_Object = MibScalar
mbgLtNgCmdExecute = _MbgLtNgCmdExecute_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 2, 1),
    _MbgLtNgCmdExecute_Type()
)
mbgLtNgCmdExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCmdExecute.setStatus("current")


class _MbgLtNgCmdSetTime_Type(DisplayString):
    """Custom type mbgLtNgCmdSetTime based on DisplayString"""
    defaultValue = OctetString("n/a")


_MbgLtNgCmdSetTime_Object = MibScalar
mbgLtNgCmdSetTime = _MbgLtNgCmdSetTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 2, 2),
    _MbgLtNgCmdSetTime_Type()
)
mbgLtNgCmdSetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgLtNgCmdSetTime.setStatus("current")
_MbgLtNgTrapNotifications_ObjectIdentity = ObjectIdentity
mbgLtNgTrapNotifications = _MbgLtNgTrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3)
)
_MbgLtNgTraps_ObjectIdentity = ObjectIdentity
mbgLtNgTraps = _MbgLtNgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0)
)


class _MbgLtNgTrapMessage_Type(DisplayString):
    """Custom type mbgLtNgTrapMessage based on DisplayString"""
    defaultValue = OctetString("no event")


_MbgLtNgTrapMessage_Object = MibScalar
mbgLtNgTrapMessage = _MbgLtNgTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 100),
    _MbgLtNgTrapMessage_Type()
)
mbgLtNgTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLtNgTrapMessage.setStatus("current")
_MbgLtNgConformance_ObjectIdentity = ObjectIdentity
mbgLtNgConformance = _MbgLtNgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 90)
)
_MbgLtNgCompliances_ObjectIdentity = ObjectIdentity
mbgLtNgCompliances = _MbgLtNgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 90, 1)
)
_MbgLtNgGroups_ObjectIdentity = ObjectIdentity
mbgLtNgGroups = _MbgLtNgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 30, 90, 2)
)

# Managed Objects groups

mbgLtNgObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5597, 30, 90, 2, 1)
)
mbgLtNgObjectsGroup.setObjects(
      *(("MBG-SNMP-LTNG-MIB", "mbgLtNgSnmpSubagentVersion"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgFirmwareVersion"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgSerialNumber"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgSubagentTimeticks"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCpuSerialNumber"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpCurrentState"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpStratum"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpRefclockName"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpRefclockOffset"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpVersion"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpCCStartedAt"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpCCDuration"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpCCNumberOfClients"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpCCTotalRequests"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpCCTotalRequestsLastHour"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpCCTotalRequestsLastMinute"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpCCTotalRequestsCurrentDay"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpCCTodaysClients"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpMrsServer"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNtpMrsOffset"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNumberOfRefclocks"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockType"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockUsage"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockState"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockSubstate"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockStatusA"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockMaxStatusA"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockStatusB"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockMaxStatusB"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockAdditionalInfo"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockLeapSecondDate"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockGpsLatitude"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockGpsLongitude"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockGpsTdop"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockGpsPdop"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockGpsUtcOffset"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockGpsAltitude"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockTimeDiff"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgRefclockGpsPos"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapMessage"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgNumberOfClusters"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgClusterCommunicationIp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgClusterPortState"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgClusterMasterSerial"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgClusterMasterIp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgClusterMasterPriority"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgClusterClockStatus"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgClusterClockClass"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgClusterReconfigurationState"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgClusterIsFalseticker"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpServerIP"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpServerKey"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpServerAutokey"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpServerMinpoll"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpServerMaxpoll"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpServerIburst"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpBroadAddr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpBroadInterval"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpBroadSymKey"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpBroadUseAutokey"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpEnableMulticast"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpMultiAddr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpMultiInterval"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpMultiSymKey"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpMultiUseAutokey"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpEnableManycast"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpManyAddr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpManySymKey"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpManyUseAutokey"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpLocalTrustedKeys"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpTrusttime"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpTimeScale"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpLocalClkStratum"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpDisableLocalClk"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpSpoofLocalTime"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpEnableClientCounter"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpEnableClientCounterDuration"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpHostname"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpDomainname"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpNameserver1"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpNameserver2"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpIpv4"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpNetmask"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpGateway"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpEnableVlan"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpVlanId"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpVlanPriority"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpEnableDhcp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpIpv6Avail"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpIpv6Mode"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpIpv6Address"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpIpv6McastScope"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpDisableSsh"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpDscpClass"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpMcastTtl"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpOpMode"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpMode"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpHybridMode"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpUcastMstAddr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpProfile"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpDelayMechanism"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpNetworkProtocol"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpDomainNumber"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpPriority1"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpPriority2"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpSyncInterval"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpAnnounceInterval"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpDelayReqInterval"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpTimescale"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpAnnRcptTmout"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpMessageDuration"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpCmd"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpSyncEAvail"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpSyncEEnabled"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpSyncEQltLvlSelEnable"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpSyncESdhNwOption"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpSyncEInputSsm"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpSyncEOutputSsm"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpSyncEGbitCopperMode"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpMiscEnable1Step"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpDisableMgmtMsgs"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpOutput1"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPtpOutput2"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEmailTo"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgEthPortLinkState"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEmailFrom"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEmailSmarthostAddr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEmailSmarthostPort"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEmailSmarthostAuth"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEmailSmarthostAuthUser"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEmailSmarthostAuthPw"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpContact"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpLocation"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVP100Display1Addr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVP100Display1SN"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVP100Display2Addr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVP100Display2SN"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEthernetHostname"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEthernetDomain"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEthernetNameserver1"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEthernetNameserver2"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEthernetIpv4Gateway"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEthernetIpv6Gateway"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNumberOfPhysicalIf"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNumberOfVirtualIf"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPhysicalIfMac"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPhysicalIfNetLinkMode"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPhysicalIfIndicateLink"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPhysicalIfBondingGroup"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgPhysicalIfIpv6Mode"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv4AddrFromDhcp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv4GatewayFromDhcp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv4DnsFromDhcp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv4DomainFromDhcp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfAssigned"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfMac"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfLabel"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceNtp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceHttp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceHttps"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceTelnet"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceSsh"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceSnmp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceFtp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceTime"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceDaytime"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfServiceFpc"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv4Addr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv4Netmask"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv4Dhcp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv6Addr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv6Dhcp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv6RoutAdd"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfIpv6LinkLocal"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfVlan"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfVlanTag"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfVlanPrio"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfCluster"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfClusterIpv4Addr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfClusterIpv4Netmask"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgVirtualIfClusterPrio"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEthernetGenClusterIp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEthernetGenClusterPort"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSyslogServerAddr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSyslogLoglevel"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgWmailAddress1"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgWmailAddress2"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpTrapRecAddr"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpTrapRecCommunity"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpTrapRecVersion"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpReadCommunity"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpWriteCommunity"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpV3UserName"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpV3UserRights"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpV3Context"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpV3SecurityLevel"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpV3AuthProtocol"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpV3AuthPassphrase"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpV3PrivProtocol"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpV3PrivPassphrase"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpRetries"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpTimeout"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSnmpEnabledVersion"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpMaxClientOffset"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgNtpMaxClientStratum"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapNormalOperation"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapNtpNotSync"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapNtpSync"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapNtpStopped"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapServerBoot"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapRefclockNotResponding"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapRefclockSynchronized"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapRefclockNotSynchronized"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapSecRefclockNotResponding"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapSecRefclockSynchronized"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapSecRefclockNotSynchronized"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapAntennaFaulty"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapAntennaReconnect"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapAntennaShortCircuit"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapConfigChanged"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapLeapSecAnnounced"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapNtpClientLimitExceeded"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapRefSrcDisconnected"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapRefSrcReconnected"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapShsTimeLimitError"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapShsTimeLimitWarning"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapNetworkDown"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapNetworkUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapPowerSupplyUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapPowerSupplyDown"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapFdmError"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapLowSystemResources"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapPtpNetworkDown"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapPtpNetworkUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapPtpStateChanged"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapPtpError"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapRefSrcLimitExceeded"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapFanDown"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapFanUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgRepeatEvent"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgRepetitions"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapWarmedUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgTrapNotWarmedUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgDisableRootLogin"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgDisableUsbPort"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgAllowNetworkDiscovery"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgLockFrontPanel"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSshKeyLength"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgSshShellTimeout"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgWebLanguage"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgActivateChangesAsStartup"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCfgEnableFrontPanelLight"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCmdExecute"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgCmdSetTime"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgFdmFreq"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgFdmFreqDev"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgFdmNomFreq"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpNumberOfModules"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpMode"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpPortState"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpLocalMac"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpGrandmasterMac"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpGrandmasterUuid"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpClockAccuracy"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpClockClass"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpTimeSource"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpUtcOffset"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpTimeSeconds"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpTsuTime"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpSysTime"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpPortLinkup"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpOffsetFromGM"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpPathDelay"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpDelayMec"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpDomain"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpDelayAsymmetry"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgPtpAvail"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgSysNumberOfPowerSupplies"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgSysPsStatus"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgSysNumberOfFans"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgSysFanStatus"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgSysFanError"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgSysTempCelsius"))
)
if mibBuilder.loadTexts:
    mbgLtNgObjectsGroup.setStatus("current")


# Notification objects

mbgLtNgTrapNTPNotSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 1)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapNTPNotSync.setStatus(
        "current"
    )

mbgLtNgTrapNTPStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 2)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapNTPStopped.setStatus(
        "current"
    )

mbgLtNgTrapServerBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 3)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapServerBoot.setStatus(
        "current"
    )

mbgLtNgTrapReceiverNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 4)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapReceiverNotResponding.setStatus(
        "current"
    )

mbgLtNgTrapReceiverNotSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 5)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapReceiverNotSync.setStatus(
        "current"
    )

mbgLtNgTrapAntennaFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 6)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapAntennaFaulty.setStatus(
        "current"
    )

mbgLtNgTrapAntennaReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 7)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapAntennaReconnect.setStatus(
        "current"
    )

mbgLtNgTrapConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 8)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapConfigChanged.setStatus(
        "current"
    )

mbgLtNgTrapLeapSecondAnnounced = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 9)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapLeapSecondAnnounced.setStatus(
        "current"
    )

mbgLtNgTrapSHSTimeLimitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 10)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapSHSTimeLimitError.setStatus(
        "current"
    )

mbgLtNgTrapSecondaryRecNotSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 11)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapSecondaryRecNotSync.setStatus(
        "current"
    )

mbgLtNgTrapPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 12)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapPowerSupplyFailure.setStatus(
        "current"
    )

mbgLtNgTrapAntennaShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 13)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapAntennaShortCircuit.setStatus(
        "current"
    )

mbgLtNgTrapReceiverSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 14)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapReceiverSync.setStatus(
        "current"
    )

mbgLtNgTrapNTPClientAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 15)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapNTPClientAlarm.setStatus(
        "current"
    )

mbgLtNgTrapPowerSupplyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 16)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapPowerSupplyUp.setStatus(
        "current"
    )

mbgLtNgTrapNetworkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 17)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapNetworkDown.setStatus(
        "current"
    )

mbgLtNgTrapNetworkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 18)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapNetworkUp.setStatus(
        "current"
    )

mbgLtNgTrapSecondaryRecNotResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 19)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapSecondaryRecNotResp.setStatus(
        "current"
    )

mbgLtNgTrapXmrLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 30)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapXmrLimitExceeded.setStatus(
        "current"
    )

mbgLtNgTrapXmrRefDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 31)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapXmrRefDisconnect.setStatus(
        "current"
    )

mbgLtNgTrapXmrRefReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 32)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapXmrRefReconnect.setStatus(
        "current"
    )

mbgLtNgTrapFdmError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 33)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapFdmError.setStatus(
        "current"
    )

mbgLtNgTrapSHSTimeLimitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 34)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapSHSTimeLimitWarning.setStatus(
        "current"
    )

mbgLtNgTrapSecondaryRecSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 35)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapSecondaryRecSync.setStatus(
        "current"
    )

mbgLtNgTrapNTPSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 36)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapNTPSync.setStatus(
        "current"
    )

mbgLtNgTrapPtpPortDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 37)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapPtpPortDisconnected.setStatus(
        "current"
    )

mbgLtNgTrapPtpPortConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 38)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapPtpPortConnected.setStatus(
        "current"
    )

mbgLtNgTrapPtpStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 39)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapPtpStateChanged.setStatus(
        "current"
    )

mbgLtNgTrapPtpError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 40)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapPtpError.setStatus(
        "current"
    )

mbgLtNgTrapLowSystemResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 41)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapLowSystemResources.setStatus(
        "current"
    )

mbgLtNgTrapFanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 45)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapFanDown.setStatus(
        "current"
    )

mbgLtNgTrapFanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 46)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapFanUp.setStatus(
        "current"
    )

mbgLtNgTrapCertificateExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 47)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapCertificateExpired.setStatus(
        "current"
    )

mbgLtNgTrapSufficientSystemResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 48)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapSufficientSystemResources.setStatus(
        "current"
    )

mbgLtNgTrapOscillatorWarmedUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 49)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapOscillatorWarmedUp.setStatus(
        "current"
    )

mbgLtNgTrapOscillatorNotWarmedUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 50)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapOscillatorNotWarmedUp.setStatus(
        "current"
    )

mbgLtNgTrapXmrRefChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 51)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapXmrRefChanged.setStatus(
        "current"
    )

mbgLtNgTrapClusterMasterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 52)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapClusterMasterChanged.setStatus(
        "current"
    )

mbgLtNgTrapClusterFalsetickerDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 53)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapClusterFalsetickerDetected.setStatus(
        "current"
    )

mbgLtNgTrapClusterFalsetickerCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 54)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapClusterFalsetickerCleared.setStatus(
        "current"
    )

mbgLtNgTrapSHSTimeLimitOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 55)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapSHSTimeLimitOk.setStatus(
        "current"
    )

mbgLtNgTrapIMSError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 56)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapIMSError.setStatus(
        "current"
    )

mbgLtNgTrapIMSOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 57)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapIMSOk.setStatus(
        "current"
    )

mbgLtNgTrapFDMOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 58)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapFDMOk.setStatus(
        "current"
    )

mbgLtNgTrapNTPOffsetLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 59)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapNTPOffsetLimitExceeded.setStatus(
        "current"
    )

mbgLtNgTrapNTPOffsetLimitOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 60)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapNTPOffsetLimitOk.setStatus(
        "current"
    )

mbgLtNgTrapNormalOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 77)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapNormalOperation.setStatus(
        "current"
    )

mbgLtNgTrapHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 88)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapHeartbeat.setStatus(
        "current"
    )

mbgLtNgTrapTestNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 30, 3, 0, 99)
)
if mibBuilder.loadTexts:
    mbgLtNgTrapTestNotification.setStatus(
        "current"
    )


# Notifications groups

mbgLtNgTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5597, 30, 90, 2, 2)
)
mbgLtNgTrapsGroup.setObjects(
      *(("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapNTPNotSync"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapNTPStopped"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapServerBoot"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapReceiverNotResponding"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapReceiverNotSync"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapAntennaFaulty"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapAntennaReconnect"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapConfigChanged"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapLeapSecondAnnounced"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapSHSTimeLimitError"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapSecondaryRecNotSync"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapPowerSupplyFailure"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapAntennaShortCircuit"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapReceiverSync"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapNTPClientAlarm"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapPowerSupplyUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapNetworkDown"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapNetworkUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapSecondaryRecNotResp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapXmrLimitExceeded"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapXmrRefDisconnect"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapXmrRefReconnect"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapFdmError"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapSHSTimeLimitWarning"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapSecondaryRecSync"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapNTPSync"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapNormalOperation"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapHeartbeat"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapTestNotification"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapPtpPortDisconnected"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapPtpPortConnected"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapPtpStateChanged"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapPtpError"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapLowSystemResources"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapSufficientSystemResources"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapFanDown"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapFanUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapCertificateExpired"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapOscillatorWarmedUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapOscillatorNotWarmedUp"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapXmrRefChanged"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapClusterMasterChanged"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapClusterFalsetickerDetected"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapClusterFalsetickerCleared"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapSHSTimeLimitOk"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapIMSError"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapIMSOk"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapFDMOk"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapNTPOffsetLimitExceeded"),
        ("MBG-SNMP-LTNG-MIB", "mbgLtNgTrapNTPOffsetLimitOk"))
)
if mibBuilder.loadTexts:
    mbgLtNgTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mbgLtNgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5597, 30, 90, 1, 1)
)
if mibBuilder.loadTexts:
    mbgLtNgCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MBG-SNMP-LTNG-MIB",
    **{"mbgLantimeNG": mbgLantimeNG,
       "mbgLantimeNGStatus": mbgLantimeNGStatus,
       "mbgLtNgInfo": mbgLtNgInfo,
       "mbgLtNgSnmpSubagentVersion": mbgLtNgSnmpSubagentVersion,
       "mbgLtNgFirmwareVersion": mbgLtNgFirmwareVersion,
       "mbgLtNgSerialNumber": mbgLtNgSerialNumber,
       "mbgLtNgSubagentTimeticks": mbgLtNgSubagentTimeticks,
       "mbgLtNgCpuSerialNumber": mbgLtNgCpuSerialNumber,
       "mbgLtNgRefclock": mbgLtNgRefclock,
       "mbgLtNgNumberOfRefclocks": mbgLtNgNumberOfRefclocks,
       "mbgLtNgRefclockTable": mbgLtNgRefclockTable,
       "mbgLtNgRefclockTableEntry": mbgLtNgRefclockTableEntry,
       "mbgLtNgRefclockIndex": mbgLtNgRefclockIndex,
       "mbgLtNgRefclockType": mbgLtNgRefclockType,
       "mbgLtNgRefclockUsage": mbgLtNgRefclockUsage,
       "mbgLtNgRefclockState": mbgLtNgRefclockState,
       "mbgLtNgRefclockSubstate": mbgLtNgRefclockSubstate,
       "mbgLtNgRefclockStatusA": mbgLtNgRefclockStatusA,
       "mbgLtNgRefclockMaxStatusA": mbgLtNgRefclockMaxStatusA,
       "mbgLtNgRefclockStatusB": mbgLtNgRefclockStatusB,
       "mbgLtNgRefclockMaxStatusB": mbgLtNgRefclockMaxStatusB,
       "mbgLtNgRefclockAdditionalInfo": mbgLtNgRefclockAdditionalInfo,
       "mbgLtNgRefclockLeapSecondDate": mbgLtNgRefclockLeapSecondDate,
       "mbgLtNgRefclockGpsTable": mbgLtNgRefclockGpsTable,
       "mbgLtNgRefclockGpsTableEntry": mbgLtNgRefclockGpsTableEntry,
       "mbgLtNgRefclockGpsIndex": mbgLtNgRefclockGpsIndex,
       "mbgLtNgRefclockGpsLatitude": mbgLtNgRefclockGpsLatitude,
       "mbgLtNgRefclockGpsLongitude": mbgLtNgRefclockGpsLongitude,
       "mbgLtNgRefclockGpsAltitude": mbgLtNgRefclockGpsAltitude,
       "mbgLtNgRefclockGpsTdop": mbgLtNgRefclockGpsTdop,
       "mbgLtNgRefclockGpsPdop": mbgLtNgRefclockGpsPdop,
       "mbgLtNgRefclockGpsUtcOffset": mbgLtNgRefclockGpsUtcOffset,
       "mbgLtNgRefclockTimeDiff": mbgLtNgRefclockTimeDiff,
       "mbgLtNgRefclockGpsPos": mbgLtNgRefclockGpsPos,
       "mbgLtNgNtp": mbgLtNgNtp,
       "mbgLtNgNtpCurrentState": mbgLtNgNtpCurrentState,
       "mbgLtNgNtpStratum": mbgLtNgNtpStratum,
       "mbgLtNgNtpRefclockName": mbgLtNgNtpRefclockName,
       "mbgLtNgNtpRefclockOffset": mbgLtNgNtpRefclockOffset,
       "mbgLtNgNtpVersion": mbgLtNgNtpVersion,
       "mbgLtNgNtpClientCounter": mbgLtNgNtpClientCounter,
       "mbgLtNgNtpCCStartedAt": mbgLtNgNtpCCStartedAt,
       "mbgLtNgNtpCCDuration": mbgLtNgNtpCCDuration,
       "mbgLtNgNtpCCNumberOfClients": mbgLtNgNtpCCNumberOfClients,
       "mbgLtNgNtpCCTotalRequests": mbgLtNgNtpCCTotalRequests,
       "mbgLtNgNtpCCTotalRequestsCurrentDay": mbgLtNgNtpCCTotalRequestsCurrentDay,
       "mbgLtNgNtpCCTotalRequestsLastHour": mbgLtNgNtpCCTotalRequestsLastHour,
       "mbgLtNgNtpCCTotalRequestsLastMinute": mbgLtNgNtpCCTotalRequestsLastMinute,
       "mbgLtNgNtpCCTodaysClients": mbgLtNgNtpCCTodaysClients,
       "mbgLtNgNtpMrs": mbgLtNgNtpMrs,
       "mbgLtNgNtpMrsServer": mbgLtNgNtpMrsServer,
       "mbgLtNgNtpMrsOffset": mbgLtNgNtpMrsOffset,
       "mbgLtNgPtp": mbgLtNgPtp,
       "mbgLtNgPtpNumberOfModules": mbgLtNgPtpNumberOfModules,
       "mbgLtNgPtpTable": mbgLtNgPtpTable,
       "mbgLtNgPtpTableEntry": mbgLtNgPtpTableEntry,
       "mbgLtNgPtpIndex": mbgLtNgPtpIndex,
       "mbgLtNgPtpMode": mbgLtNgPtpMode,
       "mbgLtNgPtpPortState": mbgLtNgPtpPortState,
       "mbgLtNgPtpGrandmasterMac": mbgLtNgPtpGrandmasterMac,
       "mbgLtNgPtpClockAccuracy": mbgLtNgPtpClockAccuracy,
       "mbgLtNgPtpClockClass": mbgLtNgPtpClockClass,
       "mbgLtNgPtpTimeSource": mbgLtNgPtpTimeSource,
       "mbgLtNgPtpUtcOffset": mbgLtNgPtpUtcOffset,
       "mbgLtNgPtpTimeSeconds": mbgLtNgPtpTimeSeconds,
       "mbgLtNgPtpTsuTime": mbgLtNgPtpTsuTime,
       "mbgLtNgPtpSysTime": mbgLtNgPtpSysTime,
       "mbgLtNgPtpPortLinkup": mbgLtNgPtpPortLinkup,
       "mbgLtNgPtpOffsetFromGM": mbgLtNgPtpOffsetFromGM,
       "mbgLtNgPtpPathDelay": mbgLtNgPtpPathDelay,
       "mbgLtNgPtpDelayMec": mbgLtNgPtpDelayMec,
       "mbgLtNgPtpDomain": mbgLtNgPtpDomain,
       "mbgLtNgPtpGrandmasterUuid": mbgLtNgPtpGrandmasterUuid,
       "mbgLtNgPtpLocalMac": mbgLtNgPtpLocalMac,
       "mbgLtNgPtpDelayAsymmetry": mbgLtNgPtpDelayAsymmetry,
       "mbgLtNgPtpAvail": mbgLtNgPtpAvail,
       "mbgLtNgFdm": mbgLtNgFdm,
       "mbgLtNgFdmFreq": mbgLtNgFdmFreq,
       "mbgLtNgFdmFreqDev": mbgLtNgFdmFreqDev,
       "mbgLtNgFdmNomFreq": mbgLtNgFdmNomFreq,
       "mbgLtNgSystemHardware": mbgLtNgSystemHardware,
       "mbgLtNgSysPowerSupply": mbgLtNgSysPowerSupply,
       "mbgLtNgSysNumberOfPowerSupplies": mbgLtNgSysNumberOfPowerSupplies,
       "mbgLtNgSysPsTable": mbgLtNgSysPsTable,
       "mbgLtNgSysPsTableEntry": mbgLtNgSysPsTableEntry,
       "mbgLtNgSysPsIndex": mbgLtNgSysPsIndex,
       "mbgLtNgSysPsStatus": mbgLtNgSysPsStatus,
       "mbgLtNgSysFan": mbgLtNgSysFan,
       "mbgLtNgSysNumberOfFans": mbgLtNgSysNumberOfFans,
       "mbgLtNgSysFanTable": mbgLtNgSysFanTable,
       "mbgLtNgSysFanTableEntry": mbgLtNgSysFanTableEntry,
       "mbgLtNgSysFanIndex": mbgLtNgSysFanIndex,
       "mbgLtNgSysFanStatus": mbgLtNgSysFanStatus,
       "mbgLtNgSysFanError": mbgLtNgSysFanError,
       "mbgLtNgSysTemperature": mbgLtNgSysTemperature,
       "mbgLtNgSysTempCelsius": mbgLtNgSysTempCelsius,
       "mbgLtNgCluster": mbgLtNgCluster,
       "mbgLtNgNumberOfClusters": mbgLtNgNumberOfClusters,
       "mbgLtNgClusterTable": mbgLtNgClusterTable,
       "mbgLtNgClusterTableEntry": mbgLtNgClusterTableEntry,
       "mbgLtNgClusterIndex": mbgLtNgClusterIndex,
       "mbgLtNgClusterCommunicationIp": mbgLtNgClusterCommunicationIp,
       "mbgLtNgClusterPortState": mbgLtNgClusterPortState,
       "mbgLtNgClusterMasterSerial": mbgLtNgClusterMasterSerial,
       "mbgLtNgClusterMasterIp": mbgLtNgClusterMasterIp,
       "mbgLtNgClusterMasterPriority": mbgLtNgClusterMasterPriority,
       "mbgLtNgClusterClockClass": mbgLtNgClusterClockClass,
       "mbgLtNgClusterClockStatus": mbgLtNgClusterClockStatus,
       "mbgLtNgClusterReconfigurationState": mbgLtNgClusterReconfigurationState,
       "mbgLtNgClusterIsFalseticker": mbgLtNgClusterIsFalseticker,
       "mbgLtNgMisc": mbgLtNgMisc,
       "mbgLtNgEthPortLinkTable": mbgLtNgEthPortLinkTable,
       "mbgLtNgEthPortLinkTableEntry": mbgLtNgEthPortLinkTableEntry,
       "mbgLtNgEthPortLinkIndex": mbgLtNgEthPortLinkIndex,
       "mbgLtNgEthPortLinkState": mbgLtNgEthPortLinkState,
       "mbgLtNgConfig": mbgLtNgConfig,
       "mbgLtNgCfgEthernet": mbgLtNgCfgEthernet,
       "mbgLtNgCfgEthernetHostname": mbgLtNgCfgEthernetHostname,
       "mbgLtNgCfgEthernetDomain": mbgLtNgCfgEthernetDomain,
       "mbgLtNgCfgEthernetNameserver1": mbgLtNgCfgEthernetNameserver1,
       "mbgLtNgCfgEthernetNameserver2": mbgLtNgCfgEthernetNameserver2,
       "mbgLtNgCfgEthernetIpv4Gateway": mbgLtNgCfgEthernetIpv4Gateway,
       "mbgLtNgCfgEthernetIpv6Gateway": mbgLtNgCfgEthernetIpv6Gateway,
       "mbgLtNgCfgNumberOfPhysicalIf": mbgLtNgCfgNumberOfPhysicalIf,
       "mbgLtNgCfgNumberOfVirtualIf": mbgLtNgCfgNumberOfVirtualIf,
       "mbgLtNgCfgPhysicalIfTable": mbgLtNgCfgPhysicalIfTable,
       "mbgLtNgCfgPhysicalIfTableEntry": mbgLtNgCfgPhysicalIfTableEntry,
       "mbgLtNgCfgPhysicalIfIndex": mbgLtNgCfgPhysicalIfIndex,
       "mbgLtNgCfgPhysicalIfMac": mbgLtNgCfgPhysicalIfMac,
       "mbgLtNgCfgPhysicalIfNetLinkMode": mbgLtNgCfgPhysicalIfNetLinkMode,
       "mbgLtNgCfgPhysicalIfIndicateLink": mbgLtNgCfgPhysicalIfIndicateLink,
       "mbgLtNgCfgPhysicalIfBondingGroup": mbgLtNgCfgPhysicalIfBondingGroup,
       "mbgLtNgCfgPhysicalIfIpv6Mode": mbgLtNgCfgPhysicalIfIpv6Mode,
       "mbgLtNgCfgVirtualIfTable": mbgLtNgCfgVirtualIfTable,
       "mbgLtNgCfgVirtualIfTableEntry": mbgLtNgCfgVirtualIfTableEntry,
       "mbgLtNgCfgVirtualIfIndex": mbgLtNgCfgVirtualIfIndex,
       "mbgLtNgCfgVirtualIfIpv4Addr": mbgLtNgCfgVirtualIfIpv4Addr,
       "mbgLtNgCfgVirtualIfIpv4Netmask": mbgLtNgCfgVirtualIfIpv4Netmask,
       "mbgLtNgCfgVirtualIfIpv4Dhcp": mbgLtNgCfgVirtualIfIpv4Dhcp,
       "mbgLtNgCfgVirtualIfIpv4AddrFromDhcp": mbgLtNgCfgVirtualIfIpv4AddrFromDhcp,
       "mbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp": mbgLtNgCfgVirtualIfIpv4NetmaskFromDhcp,
       "mbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp": mbgLtNgCfgVirtualIfIpv4BroadcastFromDhcp,
       "mbgLtNgCfgVirtualIfIpv4GatewayFromDhcp": mbgLtNgCfgVirtualIfIpv4GatewayFromDhcp,
       "mbgLtNgCfgVirtualIfIpv4DnsFromDhcp": mbgLtNgCfgVirtualIfIpv4DnsFromDhcp,
       "mbgLtNgCfgVirtualIfIpv4DomainFromDhcp": mbgLtNgCfgVirtualIfIpv4DomainFromDhcp,
       "mbgLtNgCfgVirtualIfIpv6Addr": mbgLtNgCfgVirtualIfIpv6Addr,
       "mbgLtNgCfgVirtualIfIpv6Dhcp": mbgLtNgCfgVirtualIfIpv6Dhcp,
       "mbgLtNgCfgVirtualIfIpv6RoutAdd": mbgLtNgCfgVirtualIfIpv6RoutAdd,
       "mbgLtNgCfgVirtualIfIpv6LinkLocal": mbgLtNgCfgVirtualIfIpv6LinkLocal,
       "mbgLtNgCfgVirtualIfAssigned": mbgLtNgCfgVirtualIfAssigned,
       "mbgLtNgCfgVirtualIfMac": mbgLtNgCfgVirtualIfMac,
       "mbgLtNgCfgVirtualIfLabel": mbgLtNgCfgVirtualIfLabel,
       "mbgLtNgCfgVirtualIfVlan": mbgLtNgCfgVirtualIfVlan,
       "mbgLtNgCfgVirtualIfVlanTag": mbgLtNgCfgVirtualIfVlanTag,
       "mbgLtNgCfgVirtualIfVlanPrio": mbgLtNgCfgVirtualIfVlanPrio,
       "mbgLtNgCfgVirtualIfCluster": mbgLtNgCfgVirtualIfCluster,
       "mbgLtNgCfgVirtualIfClusterIpv4Addr": mbgLtNgCfgVirtualIfClusterIpv4Addr,
       "mbgLtNgCfgVirtualIfClusterIpv4Netmask": mbgLtNgCfgVirtualIfClusterIpv4Netmask,
       "mbgLtNgCfgVirtualIfClusterPrio": mbgLtNgCfgVirtualIfClusterPrio,
       "mbgLtNgCfgVirtualIfServiceNtp": mbgLtNgCfgVirtualIfServiceNtp,
       "mbgLtNgCfgVirtualIfServiceHttp": mbgLtNgCfgVirtualIfServiceHttp,
       "mbgLtNgCfgVirtualIfServiceHttps": mbgLtNgCfgVirtualIfServiceHttps,
       "mbgLtNgCfgVirtualIfServiceTelnet": mbgLtNgCfgVirtualIfServiceTelnet,
       "mbgLtNgCfgVirtualIfServiceSsh": mbgLtNgCfgVirtualIfServiceSsh,
       "mbgLtNgCfgVirtualIfServiceSnmp": mbgLtNgCfgVirtualIfServiceSnmp,
       "mbgLtNgCfgVirtualIfServiceFtp": mbgLtNgCfgVirtualIfServiceFtp,
       "mbgLtNgCfgVirtualIfServiceTime": mbgLtNgCfgVirtualIfServiceTime,
       "mbgLtNgCfgVirtualIfServiceDaytime": mbgLtNgCfgVirtualIfServiceDaytime,
       "mbgLtNgCfgVirtualIfServiceFpc": mbgLtNgCfgVirtualIfServiceFpc,
       "mbgLtNgCfgEthernetGenClusterPort": mbgLtNgCfgEthernetGenClusterPort,
       "mbgLtNgCfgEthernetGenClusterIp": mbgLtNgCfgEthernetGenClusterIp,
       "mbgLtNgCfgNotifications": mbgLtNgCfgNotifications,
       "mbgLtNgCfgSyslog": mbgLtNgCfgSyslog,
       "mbgLtNgCfgSyslogServerAddr": mbgLtNgCfgSyslogServerAddr,
       "mbgLtNgCfgSyslogLoglevel": mbgLtNgCfgSyslogLoglevel,
       "mbgLtNgCfgEmail": mbgLtNgCfgEmail,
       "mbgLtNgCfgEmailTo": mbgLtNgCfgEmailTo,
       "mbgLtNgCfgEmailFrom": mbgLtNgCfgEmailFrom,
       "mbgLtNgCfgEmailSmarthostAddr": mbgLtNgCfgEmailSmarthostAddr,
       "mbgLtNgCfgEmailSmarthostPort": mbgLtNgCfgEmailSmarthostPort,
       "mbgLtNgCfgEmailSmarthostAuth": mbgLtNgCfgEmailSmarthostAuth,
       "mbgLtNgCfgEmailSmarthostAuthUser": mbgLtNgCfgEmailSmarthostAuthUser,
       "mbgLtNgCfgEmailSmarthostAuthPw": mbgLtNgCfgEmailSmarthostAuthPw,
       "mbgLtNgCfgWinpopup": mbgLtNgCfgWinpopup,
       "mbgLtNgCfgWmailAddress1": mbgLtNgCfgWmailAddress1,
       "mbgLtNgCfgWmailAddress2": mbgLtNgCfgWmailAddress2,
       "mbgLtNgCfgSNMP": mbgLtNgCfgSNMP,
       "mbgLtNgCfgSnmpTrapRecTable": mbgLtNgCfgSnmpTrapRecTable,
       "mbgLtNgCfgSnmpTrapRecTableEntry": mbgLtNgCfgSnmpTrapRecTableEntry,
       "mbgLtNgCfgSnmpTrapRecIndex": mbgLtNgCfgSnmpTrapRecIndex,
       "mbgLtNgCfgSnmpTrapRecAddr": mbgLtNgCfgSnmpTrapRecAddr,
       "mbgLtNgCfgSnmpTrapRecCommunity": mbgLtNgCfgSnmpTrapRecCommunity,
       "mbgLtNgCfgSnmpTrapRecVersion": mbgLtNgCfgSnmpTrapRecVersion,
       "mbgLtNgCfgSnmpReadCommunity": mbgLtNgCfgSnmpReadCommunity,
       "mbgLtNgCfgSnmpWriteCommunity": mbgLtNgCfgSnmpWriteCommunity,
       "mbgLtNgCfgSnmpContact": mbgLtNgCfgSnmpContact,
       "mbgLtNgCfgSnmpLocation": mbgLtNgCfgSnmpLocation,
       "mbgLtNgCfgSnmpV3UserName": mbgLtNgCfgSnmpV3UserName,
       "mbgLtNgCfgSnmpV3UserRights": mbgLtNgCfgSnmpV3UserRights,
       "mbgLtNgCfgSnmpV3Context": mbgLtNgCfgSnmpV3Context,
       "mbgLtNgCfgSnmpV3SecurityLevel": mbgLtNgCfgSnmpV3SecurityLevel,
       "mbgLtNgCfgSnmpV3AuthProtocol": mbgLtNgCfgSnmpV3AuthProtocol,
       "mbgLtNgCfgSnmpV3AuthPassphrase": mbgLtNgCfgSnmpV3AuthPassphrase,
       "mbgLtNgCfgSnmpV3PrivProtocol": mbgLtNgCfgSnmpV3PrivProtocol,
       "mbgLtNgCfgSnmpV3PrivPassphrase": mbgLtNgCfgSnmpV3PrivPassphrase,
       "mbgLtNgCfgSnmpRetries": mbgLtNgCfgSnmpRetries,
       "mbgLtNgCfgSnmpTimeout": mbgLtNgCfgSnmpTimeout,
       "mbgLtNgCfgSnmpEnabledVersion": mbgLtNgCfgSnmpEnabledVersion,
       "mbgLtNgCfgWalldisplay": mbgLtNgCfgWalldisplay,
       "mbgLtNgCfgVP100Display1Addr": mbgLtNgCfgVP100Display1Addr,
       "mbgLtNgCfgVP100Display1SN": mbgLtNgCfgVP100Display1SN,
       "mbgLtNgCfgVP100Display2Addr": mbgLtNgCfgVP100Display2Addr,
       "mbgLtNgCfgVP100Display2SN": mbgLtNgCfgVP100Display2SN,
       "mbgLtNgCfgNtpClientMonitoring": mbgLtNgCfgNtpClientMonitoring,
       "mbgLtNgCfgNtpMaxClientOffset": mbgLtNgCfgNtpMaxClientOffset,
       "mbgLtNgCfgNtpMaxClientStratum": mbgLtNgCfgNtpMaxClientStratum,
       "mbgLtNgCfgTrapTrigger": mbgLtNgCfgTrapTrigger,
       "mbgLtNgCfgTrapNormalOperation": mbgLtNgCfgTrapNormalOperation,
       "mbgLtNgCfgTrapNtpNotSync": mbgLtNgCfgTrapNtpNotSync,
       "mbgLtNgCfgTrapNtpSync": mbgLtNgCfgTrapNtpSync,
       "mbgLtNgCfgTrapNtpStopped": mbgLtNgCfgTrapNtpStopped,
       "mbgLtNgCfgTrapServerBoot": mbgLtNgCfgTrapServerBoot,
       "mbgLtNgCfgTrapRefclockNotResponding": mbgLtNgCfgTrapRefclockNotResponding,
       "mbgLtNgCfgTrapRefclockSynchronized": mbgLtNgCfgTrapRefclockSynchronized,
       "mbgLtNgCfgTrapRefclockNotSynchronized": mbgLtNgCfgTrapRefclockNotSynchronized,
       "mbgLtNgCfgTrapSecRefclockNotResponding": mbgLtNgCfgTrapSecRefclockNotResponding,
       "mbgLtNgCfgTrapSecRefclockSynchronized": mbgLtNgCfgTrapSecRefclockSynchronized,
       "mbgLtNgCfgTrapSecRefclockNotSynchronized": mbgLtNgCfgTrapSecRefclockNotSynchronized,
       "mbgLtNgCfgTrapAntennaFaulty": mbgLtNgCfgTrapAntennaFaulty,
       "mbgLtNgCfgTrapAntennaReconnect": mbgLtNgCfgTrapAntennaReconnect,
       "mbgLtNgCfgTrapAntennaShortCircuit": mbgLtNgCfgTrapAntennaShortCircuit,
       "mbgLtNgCfgTrapConfigChanged": mbgLtNgCfgTrapConfigChanged,
       "mbgLtNgCfgTrapLeapSecAnnounced": mbgLtNgCfgTrapLeapSecAnnounced,
       "mbgLtNgCfgTrapNtpClientLimitExceeded": mbgLtNgCfgTrapNtpClientLimitExceeded,
       "mbgLtNgCfgTrapRefSrcLimitExceeded": mbgLtNgCfgTrapRefSrcLimitExceeded,
       "mbgLtNgCfgTrapRefSrcDisconnected": mbgLtNgCfgTrapRefSrcDisconnected,
       "mbgLtNgCfgTrapRefSrcReconnected": mbgLtNgCfgTrapRefSrcReconnected,
       "mbgLtNgCfgTrapShsTimeLimitError": mbgLtNgCfgTrapShsTimeLimitError,
       "mbgLtNgCfgTrapShsTimeLimitWarning": mbgLtNgCfgTrapShsTimeLimitWarning,
       "mbgLtNgCfgTrapNetworkDown": mbgLtNgCfgTrapNetworkDown,
       "mbgLtNgCfgTrapNetworkUp": mbgLtNgCfgTrapNetworkUp,
       "mbgLtNgCfgTrapPowerSupplyUp": mbgLtNgCfgTrapPowerSupplyUp,
       "mbgLtNgCfgTrapPowerSupplyDown": mbgLtNgCfgTrapPowerSupplyDown,
       "mbgLtNgCfgTrapFdmError": mbgLtNgCfgTrapFdmError,
       "mbgLtNgCfgTrapLowSystemResources": mbgLtNgCfgTrapLowSystemResources,
       "mbgLtNgCfgTrapPtpNetworkDown": mbgLtNgCfgTrapPtpNetworkDown,
       "mbgLtNgCfgTrapPtpNetworkUp": mbgLtNgCfgTrapPtpNetworkUp,
       "mbgLtNgCfgTrapPtpStateChanged": mbgLtNgCfgTrapPtpStateChanged,
       "mbgLtNgCfgTrapPtpError": mbgLtNgCfgTrapPtpError,
       "mbgLtNgCfgTrapFanDown": mbgLtNgCfgTrapFanDown,
       "mbgLtNgCfgTrapFanUp": mbgLtNgCfgTrapFanUp,
       "mbgLtNgCfgRepeatEvent": mbgLtNgCfgRepeatEvent,
       "mbgLtNgCfgRepetitions": mbgLtNgCfgRepetitions,
       "mbgLtNgCfgTrapWarmedUp": mbgLtNgCfgTrapWarmedUp,
       "mbgLtNgCfgTrapNotWarmedUp": mbgLtNgCfgTrapNotWarmedUp,
       "mbgLtNgCfgSecurity": mbgLtNgCfgSecurity,
       "mbgLtNgCfgLoginAccess": mbgLtNgCfgLoginAccess,
       "mbgLtNgCfgDisableRootLogin": mbgLtNgCfgDisableRootLogin,
       "mbgLtNgCfgAllowNetworkDiscovery": mbgLtNgCfgAllowNetworkDiscovery,
       "mbgLtNgCfgFrontPanel": mbgLtNgCfgFrontPanel,
       "mbgLtNgCfgLockFrontPanel": mbgLtNgCfgLockFrontPanel,
       "mbgLtNgCfgDisableUsbPort": mbgLtNgCfgDisableUsbPort,
       "mbgLtNgCfgSsh": mbgLtNgCfgSsh,
       "mbgLtNgCfgSshKeyLength": mbgLtNgCfgSshKeyLength,
       "mbgLtNgCfgSshShellTimeout": mbgLtNgCfgSshShellTimeout,
       "mbgLtNgCfgNtp": mbgLtNgCfgNtp,
       "mbgLtNgCfgNtpTable": mbgLtNgCfgNtpTable,
       "mbgLtNgCfgNtpTableEntry": mbgLtNgCfgNtpTableEntry,
       "mbgLtNgCfgNtpIndex": mbgLtNgCfgNtpIndex,
       "mbgLtNgCfgNtpServerIP": mbgLtNgCfgNtpServerIP,
       "mbgLtNgCfgNtpServerKey": mbgLtNgCfgNtpServerKey,
       "mbgLtNgCfgNtpServerAutokey": mbgLtNgCfgNtpServerAutokey,
       "mbgLtNgCfgNtpServerMinpoll": mbgLtNgCfgNtpServerMinpoll,
       "mbgLtNgCfgNtpServerMaxpoll": mbgLtNgCfgNtpServerMaxpoll,
       "mbgLtNgCfgNtpServerIburst": mbgLtNgCfgNtpServerIburst,
       "mbgLtNgCfgNtpBMTable": mbgLtNgCfgNtpBMTable,
       "mbgLtNgCfgNtpBMTableEntry": mbgLtNgCfgNtpBMTableEntry,
       "mbgLtNgCfgNtpBMIndex": mbgLtNgCfgNtpBMIndex,
       "mbgLtNgCfgNtpBroadAddr": mbgLtNgCfgNtpBroadAddr,
       "mbgLtNgCfgNtpBroadSymKey": mbgLtNgCfgNtpBroadSymKey,
       "mbgLtNgCfgNtpBroadInterval": mbgLtNgCfgNtpBroadInterval,
       "mbgLtNgCfgNtpBroadUseAutokey": mbgLtNgCfgNtpBroadUseAutokey,
       "mbgLtNgCfgNtpEnableMulticast": mbgLtNgCfgNtpEnableMulticast,
       "mbgLtNgCfgNtpMultiAddr": mbgLtNgCfgNtpMultiAddr,
       "mbgLtNgCfgNtpMultiInterval": mbgLtNgCfgNtpMultiInterval,
       "mbgLtNgCfgNtpMultiSymKey": mbgLtNgCfgNtpMultiSymKey,
       "mbgLtNgCfgNtpMultiUseAutokey": mbgLtNgCfgNtpMultiUseAutokey,
       "mbgLtNgCfgNtpEnableManycast": mbgLtNgCfgNtpEnableManycast,
       "mbgLtNgCfgNtpManyAddr": mbgLtNgCfgNtpManyAddr,
       "mbgLtNgCfgNtpManySymKey": mbgLtNgCfgNtpManySymKey,
       "mbgLtNgCfgNtpManyUseAutokey": mbgLtNgCfgNtpManyUseAutokey,
       "mbgLtNgCfgNtpLocalClkStratum": mbgLtNgCfgNtpLocalClkStratum,
       "mbgLtNgCfgNtpDisableLocalClk": mbgLtNgCfgNtpDisableLocalClk,
       "mbgLtNgCfgNtpSpoofLocalTime": mbgLtNgCfgNtpSpoofLocalTime,
       "mbgLtNgCfgNtpLocalTrustedKeys": mbgLtNgCfgNtpLocalTrustedKeys,
       "mbgLtNgCfgNtpTrusttime": mbgLtNgCfgNtpTrusttime,
       "mbgLtNgCfgNtpTimeScale": mbgLtNgCfgNtpTimeScale,
       "mbgLtNgCfgNtpEnableClientCounter": mbgLtNgCfgNtpEnableClientCounter,
       "mbgLtNgCfgNtpEnableClientCounterDuration": mbgLtNgCfgNtpEnableClientCounterDuration,
       "mbgLtNgCfgPtp": mbgLtNgCfgPtp,
       "mbgLtNgCfgPtpTable": mbgLtNgCfgPtpTable,
       "mbgLtNgCfgPtpTableEntry": mbgLtNgCfgPtpTableEntry,
       "mbgLtNgCfgPtpIndex": mbgLtNgCfgPtpIndex,
       "mbgLtNgCfgPtpHostname": mbgLtNgCfgPtpHostname,
       "mbgLtNgCfgPtpDomainname": mbgLtNgCfgPtpDomainname,
       "mbgLtNgCfgPtpNameserver1": mbgLtNgCfgPtpNameserver1,
       "mbgLtNgCfgPtpNameserver2": mbgLtNgCfgPtpNameserver2,
       "mbgLtNgCfgPtpIpv4": mbgLtNgCfgPtpIpv4,
       "mbgLtNgCfgPtpNetmask": mbgLtNgCfgPtpNetmask,
       "mbgLtNgCfgPtpGateway": mbgLtNgCfgPtpGateway,
       "mbgLtNgCfgPtpEnableVlan": mbgLtNgCfgPtpEnableVlan,
       "mbgLtNgCfgPtpVlanId": mbgLtNgCfgPtpVlanId,
       "mbgLtNgCfgPtpVlanPriority": mbgLtNgCfgPtpVlanPriority,
       "mbgLtNgCfgPtpEnableDhcp": mbgLtNgCfgPtpEnableDhcp,
       "mbgLtNgCfgPtpMode": mbgLtNgCfgPtpMode,
       "mbgLtNgCfgPtpDelayMechanism": mbgLtNgCfgPtpDelayMechanism,
       "mbgLtNgCfgPtpNetworkProtocol": mbgLtNgCfgPtpNetworkProtocol,
       "mbgLtNgCfgPtpDomainNumber": mbgLtNgCfgPtpDomainNumber,
       "mbgLtNgCfgPtpPriority1": mbgLtNgCfgPtpPriority1,
       "mbgLtNgCfgPtpPriority2": mbgLtNgCfgPtpPriority2,
       "mbgLtNgCfgPtpSyncInterval": mbgLtNgCfgPtpSyncInterval,
       "mbgLtNgCfgPtpAnnounceInterval": mbgLtNgCfgPtpAnnounceInterval,
       "mbgLtNgCfgPtpDelayReqInterval": mbgLtNgCfgPtpDelayReqInterval,
       "mbgLtNgCfgPtpTimescale": mbgLtNgCfgPtpTimescale,
       "mbgLtNgCfgPtpIpv6Avail": mbgLtNgCfgPtpIpv6Avail,
       "mbgLtNgCfgPtpIpv6Mode": mbgLtNgCfgPtpIpv6Mode,
       "mbgLtNgCfgPtpIpv6Address": mbgLtNgCfgPtpIpv6Address,
       "mbgLtNgCfgPtpIpv6McastScope": mbgLtNgCfgPtpIpv6McastScope,
       "mbgLtNgCfgPtpDisableSsh": mbgLtNgCfgPtpDisableSsh,
       "mbgLtNgCfgPtpDscpClass": mbgLtNgCfgPtpDscpClass,
       "mbgLtNgCfgPtpMcastTtl": mbgLtNgCfgPtpMcastTtl,
       "mbgLtNgCfgPtpOpMode": mbgLtNgCfgPtpOpMode,
       "mbgLtNgCfgPtpProfile": mbgLtNgCfgPtpProfile,
       "mbgLtNgCfgPtpHybridMode": mbgLtNgCfgPtpHybridMode,
       "mbgLtNgCfgPtpUcastMstAddr": mbgLtNgCfgPtpUcastMstAddr,
       "mbgLtNgCfgPtpAnnRcptTmout": mbgLtNgCfgPtpAnnRcptTmout,
       "mbgLtNgCfgPtpMessageDuration": mbgLtNgCfgPtpMessageDuration,
       "mbgLtNgCfgPtpSyncEAvail": mbgLtNgCfgPtpSyncEAvail,
       "mbgLtNgCfgPtpSyncEEnabled": mbgLtNgCfgPtpSyncEEnabled,
       "mbgLtNgCfgPtpSyncEQltLvlSelEnable": mbgLtNgCfgPtpSyncEQltLvlSelEnable,
       "mbgLtNgCfgPtpSyncESdhNwOption": mbgLtNgCfgPtpSyncESdhNwOption,
       "mbgLtNgCfgPtpSyncEInputSsm": mbgLtNgCfgPtpSyncEInputSsm,
       "mbgLtNgCfgPtpSyncEOutputSsm": mbgLtNgCfgPtpSyncEOutputSsm,
       "mbgLtNgCfgPtpSyncEGbitCopperMode": mbgLtNgCfgPtpSyncEGbitCopperMode,
       "mbgLtNgCfgPtpMiscEnable1Step": mbgLtNgCfgPtpMiscEnable1Step,
       "mbgLtNgCfgPtpDisableMgmtMsgs": mbgLtNgCfgPtpDisableMgmtMsgs,
       "mbgLtNgCfgPtpOutput1": mbgLtNgCfgPtpOutput1,
       "mbgLtNgCfgPtpOutput2": mbgLtNgCfgPtpOutput2,
       "mbgLtNgCfgPtpCmd": mbgLtNgCfgPtpCmd,
       "mbgLtNgCfgSystem": mbgLtNgCfgSystem,
       "mbgLtNgCfgGeneral": mbgLtNgCfgGeneral,
       "mbgLtNgCfgWebLanguage": mbgLtNgCfgWebLanguage,
       "mbgLtNgCfgActivateChangesAsStartup": mbgLtNgCfgActivateChangesAsStartup,
       "mbgLtNgCfgDisplay": mbgLtNgCfgDisplay,
       "mbgLtNgCfgEnableFrontPanelLight": mbgLtNgCfgEnableFrontPanelLight,
       "mbgLtNgCommands": mbgLtNgCommands,
       "mbgLtNgCmdExecute": mbgLtNgCmdExecute,
       "mbgLtNgCmdSetTime": mbgLtNgCmdSetTime,
       "mbgLtNgTrapNotifications": mbgLtNgTrapNotifications,
       "mbgLtNgTraps": mbgLtNgTraps,
       "mbgLtNgTrapNTPNotSync": mbgLtNgTrapNTPNotSync,
       "mbgLtNgTrapNTPStopped": mbgLtNgTrapNTPStopped,
       "mbgLtNgTrapServerBoot": mbgLtNgTrapServerBoot,
       "mbgLtNgTrapReceiverNotResponding": mbgLtNgTrapReceiverNotResponding,
       "mbgLtNgTrapReceiverNotSync": mbgLtNgTrapReceiverNotSync,
       "mbgLtNgTrapAntennaFaulty": mbgLtNgTrapAntennaFaulty,
       "mbgLtNgTrapAntennaReconnect": mbgLtNgTrapAntennaReconnect,
       "mbgLtNgTrapConfigChanged": mbgLtNgTrapConfigChanged,
       "mbgLtNgTrapLeapSecondAnnounced": mbgLtNgTrapLeapSecondAnnounced,
       "mbgLtNgTrapSHSTimeLimitError": mbgLtNgTrapSHSTimeLimitError,
       "mbgLtNgTrapSecondaryRecNotSync": mbgLtNgTrapSecondaryRecNotSync,
       "mbgLtNgTrapPowerSupplyFailure": mbgLtNgTrapPowerSupplyFailure,
       "mbgLtNgTrapAntennaShortCircuit": mbgLtNgTrapAntennaShortCircuit,
       "mbgLtNgTrapReceiverSync": mbgLtNgTrapReceiverSync,
       "mbgLtNgTrapNTPClientAlarm": mbgLtNgTrapNTPClientAlarm,
       "mbgLtNgTrapPowerSupplyUp": mbgLtNgTrapPowerSupplyUp,
       "mbgLtNgTrapNetworkDown": mbgLtNgTrapNetworkDown,
       "mbgLtNgTrapNetworkUp": mbgLtNgTrapNetworkUp,
       "mbgLtNgTrapSecondaryRecNotResp": mbgLtNgTrapSecondaryRecNotResp,
       "mbgLtNgTrapXmrLimitExceeded": mbgLtNgTrapXmrLimitExceeded,
       "mbgLtNgTrapXmrRefDisconnect": mbgLtNgTrapXmrRefDisconnect,
       "mbgLtNgTrapXmrRefReconnect": mbgLtNgTrapXmrRefReconnect,
       "mbgLtNgTrapFdmError": mbgLtNgTrapFdmError,
       "mbgLtNgTrapSHSTimeLimitWarning": mbgLtNgTrapSHSTimeLimitWarning,
       "mbgLtNgTrapSecondaryRecSync": mbgLtNgTrapSecondaryRecSync,
       "mbgLtNgTrapNTPSync": mbgLtNgTrapNTPSync,
       "mbgLtNgTrapPtpPortDisconnected": mbgLtNgTrapPtpPortDisconnected,
       "mbgLtNgTrapPtpPortConnected": mbgLtNgTrapPtpPortConnected,
       "mbgLtNgTrapPtpStateChanged": mbgLtNgTrapPtpStateChanged,
       "mbgLtNgTrapPtpError": mbgLtNgTrapPtpError,
       "mbgLtNgTrapLowSystemResources": mbgLtNgTrapLowSystemResources,
       "mbgLtNgTrapFanDown": mbgLtNgTrapFanDown,
       "mbgLtNgTrapFanUp": mbgLtNgTrapFanUp,
       "mbgLtNgTrapCertificateExpired": mbgLtNgTrapCertificateExpired,
       "mbgLtNgTrapSufficientSystemResources": mbgLtNgTrapSufficientSystemResources,
       "mbgLtNgTrapOscillatorWarmedUp": mbgLtNgTrapOscillatorWarmedUp,
       "mbgLtNgTrapOscillatorNotWarmedUp": mbgLtNgTrapOscillatorNotWarmedUp,
       "mbgLtNgTrapXmrRefChanged": mbgLtNgTrapXmrRefChanged,
       "mbgLtNgTrapClusterMasterChanged": mbgLtNgTrapClusterMasterChanged,
       "mbgLtNgTrapClusterFalsetickerDetected": mbgLtNgTrapClusterFalsetickerDetected,
       "mbgLtNgTrapClusterFalsetickerCleared": mbgLtNgTrapClusterFalsetickerCleared,
       "mbgLtNgTrapSHSTimeLimitOk": mbgLtNgTrapSHSTimeLimitOk,
       "mbgLtNgTrapIMSError": mbgLtNgTrapIMSError,
       "mbgLtNgTrapIMSOk": mbgLtNgTrapIMSOk,
       "mbgLtNgTrapFDMOk": mbgLtNgTrapFDMOk,
       "mbgLtNgTrapNTPOffsetLimitExceeded": mbgLtNgTrapNTPOffsetLimitExceeded,
       "mbgLtNgTrapNTPOffsetLimitOk": mbgLtNgTrapNTPOffsetLimitOk,
       "mbgLtNgTrapNormalOperation": mbgLtNgTrapNormalOperation,
       "mbgLtNgTrapHeartbeat": mbgLtNgTrapHeartbeat,
       "mbgLtNgTrapTestNotification": mbgLtNgTrapTestNotification,
       "mbgLtNgTrapMessage": mbgLtNgTrapMessage,
       "mbgLtNgConformance": mbgLtNgConformance,
       "mbgLtNgCompliances": mbgLtNgCompliances,
       "mbgLtNgCompliance": mbgLtNgCompliance,
       "mbgLtNgGroups": mbgLtNgGroups,
       "mbgLtNgObjectsGroup": mbgLtNgObjectsGroup,
       "mbgLtNgTrapsGroup": mbgLtNgTrapsGroup}
)
