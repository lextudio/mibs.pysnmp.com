# SNMP MIB module (SW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:31 2024
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

(bcsiModules,
 fcSwitch) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules",
    "fcSwitch")

(FcWwn,
 SwDomainIndex,
 SwNbIndex,
 SwPortIndex,
 SwSensorIndex,
 SwTrunkMaster) = mibBuilder.importSymbols(
    "Brocade-TC",
    "FcWwn",
    "SwDomainIndex",
    "SwNbIndex",
    "SwPortIndex",
    "SwSensorIndex",
    "SwTrunkMaster")

(connUnitPortEntry,
 connUnitPortStatEntry) = mibBuilder.importSymbols(
    "FCMGMT-MIB",
    "connUnitPortEntry",
    "connUnitPortStatEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 3)
)
swMibModule.setRevisions(
        ("2003-01-13 14:30",
         "2003-07-20 14:30",
         "2004-04-15 10:30",
         "2004-08-06 18:30",
         "2005-04-29 20:16",
         "2006-01-09 09:00",
         "2006-05-17 09:00",
         "2007-01-23 09:00",
         "2007-06-08 12:00",
         "2007-06-27 10:30",
         "2007-08-01 12:20",
         "2007-08-29 04:42",
         "2008-01-29 07:59",
         "2008-07-17 03:45",
         "2008-07-24 02:32",
         "2008-07-25 02:32",
         "2008-09-09 09:00",
         "2009-09-28 09:00",
         "2009-02-21 09:00",
         "2009-03-30 09:00",
         "2009-06-25 12:00",
         "2009-06-29 01:00",
         "2009-06-30 13:06",
         "2009-06-30 06:00",
         "2009-10-30 05:00",
         "2009-11-03 13:06",
         "2009-11-05 12:00",
         "2009-11-05 05:00",
         "2009-11-06 11:30",
         "2009-11-30 10:30",
         "2009-12-03 17:30",
         "2010-01-30 17:30",
         "2010-07-08 11:30",
         "2010-07-15 11:30",
         "2010-07-21 11:30",
         "2010-08-06 11:30",
         "2010-08-20 10:30",
         "2010-10-07 10:30",
         "2010-10-09 10:30",
         "2010-10-25 10:30",
         "2010-11-01 06:00",
         "2010-11-02 10:30",
         "2010-12-02 10:30",
         "2010-12-08 10:30",
         "2010-12-20 10:00",
         "2010-12-21 04:00",
         "2010-12-22 10:00",
         "2010-12-30 10:00",
         "2011-01-06 10:30",
         "2011-01-07 10:30",
         "2011-02-18 06:00",
         "2012-02-23 10:30",
         "2012-03-05 03:33",
         "2012-05-15 14:25",
         "2012-06-04 17:20",
         "2012-06-14 10:00",
         "2012-06-29 15:20",
         "2012-07-10 16:00",
         "2012-09-26 14:00",
         "2013-03-21 13:00",
         "2013-04-04 17:48",
         "2013-04-22 11:30",
         "2013-04-25 18:03",
         "2013-05-15 14:30",
         "2013-06-05 16:00",
         "2013-06-29 10:00",
         "2013-09-12 10:00",
         "2013-10-04 13:40")
)


# Types definitions



class SwFwActs(Integer32):
    """Custom type SwFwActs based on Integer32"""
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
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("swFwElMailAlertRn", 25),
          ("swFwElPf", 33),
          ("swFwElPlPf", 37),
          ("swFwElPlRn", 13),
          ("swFwElPlRnPf", 45),
          ("swFwElRn", 9),
          ("swFwElRnPf", 41),
          ("swFwElStPf", 35),
          ("swFwElStPlPf", 39),
          ("swFwElStPlRn", 15),
          ("swFwElStPlRnPf", 47),
          ("swFwElStRn", 11),
          ("swFwElStRnPf", 43),
          ("swFwErrlog", 1),
          ("swFwErrlogPortloglock", 5),
          ("swFwErrlogSnmptrap", 3),
          ("swFwErrlogSnmptrapPortloglock", 7),
          ("swFwMailAlert", 16),
          ("swFwMailAlertElPf", 49),
          ("swFwMailAlertElPlPf", 53),
          ("swFwMailAlertElPlRn", 29),
          ("swFwMailAlertElPlRnPf", 61),
          ("swFwMailAlertElRnPf", 57),
          ("swFwMailAlertElStPf", 51),
          ("swFwMailAlertElStPlPf", 55),
          ("swFwMailAlertElStPlRn", 31),
          ("swFwMailAlertElStPlRnPf", 63),
          ("swFwMailAlertElStRn", 27),
          ("swFwMailAlertElStRnPf", 59),
          ("swFwMailAlertErrlog", 17),
          ("swFwMailAlertErrlogPortloglock", 21),
          ("swFwMailAlertErrlogSnmptrap", 19),
          ("swFwMailAlertErrlogSnmptrapPortloglock", 23),
          ("swFwMailAlertPf", 48),
          ("swFwMailAlertPlPf", 52),
          ("swFwMailAlertPlRn", 28),
          ("swFwMailAlertPlRnPf", 60),
          ("swFwMailAlertPortloglock", 20),
          ("swFwMailAlertRn", 24),
          ("swFwMailAlertRnPf", 56),
          ("swFwMailAlertSnmptrap", 18),
          ("swFwMailAlertSnmptrapPortloglock", 22),
          ("swFwMailAlertStPf", 50),
          ("swFwMailAlertStPlPf", 54),
          ("swFwMailAlertStPlRn", 30),
          ("swFwMailAlertStPlRnPf", 62),
          ("swFwMailAlertStRn", 26),
          ("swFwMailAlertStRnPf", 58),
          ("swFwNoAction", 0),
          ("swFwPf", 32),
          ("swFwPlPf", 36),
          ("swFwPlRn", 12),
          ("swFwPlRnPf", 44),
          ("swFwPortloglock", 4),
          ("swFwRn", 8),
          ("swFwRnPf", 40),
          ("swFwSnmptrap", 2),
          ("swFwSnmptrapPortloglock", 6),
          ("swFwStPf", 34),
          ("swFwStPlPf", 38),
          ("swFwStPlRn", 14),
          ("swFwStPlRnPf", 46),
          ("swFwStRn", 10),
          ("swFwStRnPf", 42))
    )





class SwFwLevels(Integer32):
    """Custom type SwFwLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("swFwCustom", 3),
          ("swFwDefault", 2),
          ("swFwReserved", 1))
    )





class SwFwClassesAreas(Integer32):
    """Custom type SwFwClassesAreas based on Integer32"""
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
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152)
        )
    )
    namedValues = NamedValues(
        *(("filterFmCfg1", 101),
          ("filterFmCfg10", 110),
          ("filterFmCfg11", 111),
          ("filterFmCfg12", 112),
          ("filterFmCfg13", 113),
          ("filterFmCfg14", 114),
          ("filterFmCfg15", 115),
          ("filterFmCfg16", 116),
          ("filterFmCfg17", 117),
          ("filterFmCfg18", 118),
          ("filterFmCfg19", 119),
          ("filterFmCfg2", 102),
          ("filterFmCfg20", 120),
          ("filterFmCfg21", 121),
          ("filterFmCfg22", 122),
          ("filterFmCfg23", 123),
          ("filterFmCfg24", 124),
          ("filterFmCfg25", 125),
          ("filterFmCfg26", 126),
          ("filterFmCfg27", 127),
          ("filterFmCfg28", 128),
          ("filterFmCfg29", 129),
          ("filterFmCfg3", 103),
          ("filterFmCfg30", 130),
          ("filterFmCfg31", 131),
          ("filterFmCfg32", 132),
          ("filterFmCfg33", 133),
          ("filterFmCfg34", 134),
          ("filterFmCfg35", 135),
          ("filterFmCfg36", 136),
          ("filterFmCfg37", 137),
          ("filterFmCfg38", 138),
          ("filterFmCfg39", 139),
          ("filterFmCfg4", 104),
          ("filterFmCfg40", 140),
          ("filterFmCfg41", 141),
          ("filterFmCfg42", 142),
          ("filterFmCfg43", 143),
          ("filterFmCfg44", 144),
          ("filterFmCfg45", 145),
          ("filterFmCfg46", 146),
          ("filterFmCfg47", 147),
          ("filterFmCfg48", 148),
          ("filterFmCfg49", 149),
          ("filterFmCfg5", 105),
          ("filterFmCfg50", 150),
          ("filterFmCfg51", 151),
          ("filterFmCfg6", 106),
          ("filterFmCfg7", 107),
          ("filterFmCfg8", 108),
          ("filterFmCfg9", 109),
          ("swFwCPUMemUsage", 100),
          ("swFwEPortC3Discard", 91),
          ("swFwEPortCrcs", 30),
          ("swFwEPortLink", 25),
          ("swFwEPortLr", 87),
          ("swFwEPortPe", 28),
          ("swFwEPortPktl", 85),
          ("swFwEPortRXPerf", 31),
          ("swFwEPortSignal", 27),
          ("swFwEPortState", 33),
          ("swFwEPortSync", 26),
          ("swFwEPortTXPerf", 32),
          ("swFwEPortTrunkUtil", 97),
          ("swFwEPortUtil", 84),
          ("swFwEPortWords", 29),
          ("swFwEnvFan", 2),
          ("swFwEnvPs", 3),
          ("swFwEnvTemp", 1),
          ("swFwFCUPortC3Discard", 92),
          ("swFwFCUPortCrcs", 39),
          ("swFwFCUPortLink", 34),
          ("swFwFCUPortLr", 88),
          ("swFwFCUPortPe", 37),
          ("swFwFCUPortRXPerf", 40),
          ("swFwFCUPortSignal", 36),
          ("swFwFCUPortState", 42),
          ("swFwFCUPortSync", 35),
          ("swFwFCUPortTXPerf", 41),
          ("swFwFCUPortTrunkUtil", 98),
          ("swFwFCUPortWords", 38),
          ("swFwFOPPortC3Discard", 93),
          ("swFwFOPPortCrcs", 48),
          ("swFwFOPPortLink", 43),
          ("swFwFOPPortLr", 89),
          ("swFwFOPPortPe", 46),
          ("swFwFOPPortRXPerf", 49),
          ("swFwFOPPortSignal", 45),
          ("swFwFOPPortState", 51),
          ("swFwFOPPortSync", 44),
          ("swFwFOPPortTXPerf", 50),
          ("swFwFOPPortTrunkUtil", 99),
          ("swFwFOPPortWords", 47),
          ("swFwFabricDi", 19),
          ("swFwFabricEd", 17),
          ("swFwFabricFl", 23),
          ("swFwFabricFq", 22),
          ("swFwFabricFr", 18),
          ("swFwFabricGs", 24),
          ("swFwFabricSc", 20),
          ("swFwFabricZc", 21),
          ("swFwPerfALPACRC", 52),
          ("swFwPerfEToECRC", 53),
          ("swFwPerfEToERxCnt", 54),
          ("swFwPerfEToETxCnt", 55),
          ("swFwPerffltCusDef", 56),
          ("swFwPortC3Discard", 90),
          ("swFwPortCrcs", 13),
          ("swFwPortLink", 8),
          ("swFwPortLr", 86),
          ("swFwPortPe", 11),
          ("swFwPortRXPerf", 14),
          ("swFwPortSignal", 10),
          ("swFwPortState", 16),
          ("swFwPortSync", 9),
          ("swFwPortTXPerf", 15),
          ("swFwPortWords", 12),
          ("swFwPowerOnHours", 152),
          ("swFwResourceFlash", 83),
          ("swFwSAMDurationOfOccur", 81),
          ("swFwSAMFreqOfOccur", 82),
          ("swFwSAMTotalDownTime", 79),
          ("swFwSAMTotalUpTime", 80),
          ("swFwSecAPIViolations", 60),
          ("swFwSecDCCViolations", 68),
          ("swFwSecFPViolations", 66),
          ("swFwSecHTTPViolations", 59),
          ("swFwSecIllegalCmd", 78),
          ("swFwSecIncompDB", 77),
          ("swFwSecInvalidCert", 72),
          ("swFwSecInvalidSign", 71),
          ("swFwSecInvalidTS", 70),
          ("swFwSecLoginViolations", 69),
          ("swFwSecMSViolations", 64),
          ("swFwSecNoFcs", 76),
          ("swFwSecRSNMPViolations", 61),
          ("swFwSecSCCViolations", 67),
          ("swFwSecSESViolations", 63),
          ("swFwSecSerialViolations", 65),
          ("swFwSecSlapBadPkt", 74),
          ("swFwSecSlapFail", 73),
          ("swFwSecTSOutSync", 75),
          ("swFwSecTelnetViolations", 58),
          ("swFwSecWSNMPViolations", 62),
          ("swFwTransceiverCurrent", 7),
          ("swFwTransceiverRxp", 5),
          ("swFwTransceiverTemp", 4),
          ("swFwTransceiverTxp", 6),
          ("swFwTransceiverVoltage", 57),
          ("swFwVEPortPktLoss", 96),
          ("swFwVEPortStateChange", 94),
          ("swFwVEPortUtil", 95))
    )





class SwFwWriteVals(Integer32):
    """Custom type SwFwWriteVals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swFwApplyWrite", 2),
          ("swFwCancelWrite", 1))
    )





class SwFwTimebase(Integer32):
    """Custom type SwFwTimebase based on Integer32"""
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
        *(("swFwTbDay", 5),
          ("swFwTbHour", 4),
          ("swFwTbMin", 3),
          ("swFwTbNone", 1),
          ("swFwTbSec", 2))
    )





class SwFwStatus(Integer32):
    """Custom type SwFwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )





class SwFwEvent(Integer32):
    """Custom type SwFwEvent based on Integer32"""
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
        *(("above", 5),
          ("below", 4),
          ("changed", 2),
          ("exceeded", 3),
          ("inBetween", 6),
          ("lowBufferCrsd", 7),
          ("started", 1))
    )





class SwFwBehavior(Integer32):
    """Custom type SwFwBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("triggered", 1))
    )





class SwFwState(Integer32):
    """Custom type SwFwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("swFwFaulty", 3),
          ("swFwInformative", 1),
          ("swFwNormal", 2))
    )





class SwFwLicense(Integer32):
    """Custom type SwFwLicense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swFwLicensed", 1),
          ("swFwNotLicensed", 2))
    )




# TEXTUAL-CONVENTIONS



class SwSevType(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 1),
          ("debug", 5),
          ("error", 2),
          ("informational", 4),
          ("none", 0),
          ("warning", 3))
    )



class FcPortFlag(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Sw_ObjectIdentity = ObjectIdentity
sw = _Sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sw.setStatus("current")
_SwTrapsV2_ObjectIdentity = ObjectIdentity
swTrapsV2 = _SwTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0)
)
if mibBuilder.loadTexts:
    swTrapsV2.setStatus("current")
_SwSystem_ObjectIdentity = ObjectIdentity
swSystem = _SwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    swSystem.setStatus("current")


class _SwCurrentDate_Type(DisplayString):
    """Custom type swCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwCurrentDate_Type.__name__ = "DisplayString"
_SwCurrentDate_Object = MibScalar
swCurrentDate = _SwCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 1),
    _SwCurrentDate_Type()
)
swCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCurrentDate.setStatus("current")


class _SwBootDate_Type(DisplayString):
    """Custom type swBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwBootDate_Type.__name__ = "DisplayString"
_SwBootDate_Object = MibScalar
swBootDate = _SwBootDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 2),
    _SwBootDate_Type()
)
swBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootDate.setStatus("current")


class _SwFWLastUpdated_Type(DisplayString):
    """Custom type swFWLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFWLastUpdated_Type.__name__ = "DisplayString"
_SwFWLastUpdated_Object = MibScalar
swFWLastUpdated = _SwFWLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 3),
    _SwFWLastUpdated_Type()
)
swFWLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFWLastUpdated.setStatus("current")


class _SwFlashLastUpdated_Type(DisplayString):
    """Custom type swFlashLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFlashLastUpdated_Type.__name__ = "DisplayString"
_SwFlashLastUpdated_Object = MibScalar
swFlashLastUpdated = _SwFlashLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 4),
    _SwFlashLastUpdated_Type()
)
swFlashLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashLastUpdated.setStatus("current")


class _SwBootPromLastUpdated_Type(DisplayString):
    """Custom type swBootPromLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwBootPromLastUpdated_Type.__name__ = "DisplayString"
_SwBootPromLastUpdated_Object = MibScalar
swBootPromLastUpdated = _SwBootPromLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 5),
    _SwBootPromLastUpdated_Type()
)
swBootPromLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootPromLastUpdated.setStatus("current")


class _SwFirmwareVersion_Type(DisplayString):
    """Custom type swFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SwFirmwareVersion_Type.__name__ = "DisplayString"
_SwFirmwareVersion_Object = MibScalar
swFirmwareVersion = _SwFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 6),
    _SwFirmwareVersion_Type()
)
swFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareVersion.setStatus("current")


class _SwOperStatus_Type(Integer32):
    """Custom type swOperStatus based on Integer32"""
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
        *(("faulty", 4),
          ("offline", 2),
          ("online", 1),
          ("testing", 3))
    )


_SwOperStatus_Type.__name__ = "Integer32"
_SwOperStatus_Object = MibScalar
swOperStatus = _SwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 7),
    _SwOperStatus_Type()
)
swOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOperStatus.setStatus("current")


class _SwAdmStatus_Type(Integer32):
    """Custom type swAdmStatus based on Integer32"""
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
        *(("fastboot", 6),
          ("faulty", 4),
          ("offline", 2),
          ("online", 1),
          ("reboot", 5),
          ("testing", 3))
    )


_SwAdmStatus_Type.__name__ = "Integer32"
_SwAdmStatus_Object = MibScalar
swAdmStatus = _SwAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 8),
    _SwAdmStatus_Type()
)
swAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAdmStatus.setStatus("current")


class _SwTelnetShellAdmStatus_Type(Integer32):
    """Custom type swTelnetShellAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("terminated", 1),
          ("unknown", 0))
    )


_SwTelnetShellAdmStatus_Type.__name__ = "Integer32"
_SwTelnetShellAdmStatus_Object = MibScalar
swTelnetShellAdmStatus = _SwTelnetShellAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 9),
    _SwTelnetShellAdmStatus_Type()
)
swTelnetShellAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTelnetShellAdmStatus.setStatus("current")


class _SwSsn_Type(DisplayString):
    """Custom type swSsn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwSsn_Type.__name__ = "DisplayString"
_SwSsn_Object = MibScalar
swSsn = _SwSsn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 10),
    _SwSsn_Type()
)
swSsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSsn.setStatus("current")


class _SwFlashDLOperStatus_Type(Integer32):
    """Custom type swFlashDLOperStatus based on Integer32"""
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
        *(("swCfDownloaded", 4),
          ("swCfUploaded", 3),
          ("swCurrent", 1),
          ("swFwCorrupted", 5),
          ("swFwUpgraded", 2),
          ("unknown", 0))
    )


_SwFlashDLOperStatus_Type.__name__ = "Integer32"
_SwFlashDLOperStatus_Object = MibScalar
swFlashDLOperStatus = _SwFlashDLOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 11),
    _SwFlashDLOperStatus_Type()
)
swFlashDLOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashDLOperStatus.setStatus("current")


class _SwFlashDLAdmStatus_Type(Integer32):
    """Custom type swFlashDLAdmStatus based on Integer32"""
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
        *(("swCfDownload", 4),
          ("swCfUpload", 3),
          ("swCurrent", 1),
          ("swFwCorrupted", 5),
          ("swFwUpgrade", 2))
    )


_SwFlashDLAdmStatus_Type.__name__ = "Integer32"
_SwFlashDLAdmStatus_Object = MibScalar
swFlashDLAdmStatus = _SwFlashDLAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 12),
    _SwFlashDLAdmStatus_Type()
)
swFlashDLAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLAdmStatus.setStatus("current")


class _SwFlashDLHost_Type(DisplayString):
    """Custom type swFlashDLHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFlashDLHost_Type.__name__ = "DisplayString"
_SwFlashDLHost_Object = MibScalar
swFlashDLHost = _SwFlashDLHost_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 13),
    _SwFlashDLHost_Type()
)
swFlashDLHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLHost.setStatus("current")


class _SwFlashDLUser_Type(DisplayString):
    """Custom type swFlashDLUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFlashDLUser_Type.__name__ = "DisplayString"
_SwFlashDLUser_Object = MibScalar
swFlashDLUser = _SwFlashDLUser_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 14),
    _SwFlashDLUser_Type()
)
swFlashDLUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLUser.setStatus("current")
_SwFlashDLFile_Type = DisplayString
_SwFlashDLFile_Object = MibScalar
swFlashDLFile = _SwFlashDLFile_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 15),
    _SwFlashDLFile_Type()
)
swFlashDLFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLFile.setStatus("current")


class _SwFlashDLPassword_Type(DisplayString):
    """Custom type swFlashDLPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SwFlashDLPassword_Type.__name__ = "DisplayString"
_SwFlashDLPassword_Object = MibScalar
swFlashDLPassword = _SwFlashDLPassword_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 16),
    _SwFlashDLPassword_Type()
)
swFlashDLPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLPassword.setStatus("current")


class _SwBeaconOperStatus_Type(Integer32):
    """Custom type swBeaconOperStatus based on Integer32"""
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


_SwBeaconOperStatus_Type.__name__ = "Integer32"
_SwBeaconOperStatus_Object = MibScalar
swBeaconOperStatus = _SwBeaconOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 18),
    _SwBeaconOperStatus_Type()
)
swBeaconOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBeaconOperStatus.setStatus("current")


class _SwBeaconAdmStatus_Type(Integer32):
    """Custom type swBeaconAdmStatus based on Integer32"""
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


_SwBeaconAdmStatus_Type.__name__ = "Integer32"
_SwBeaconAdmStatus_Object = MibScalar
swBeaconAdmStatus = _SwBeaconAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 19),
    _SwBeaconAdmStatus_Type()
)
swBeaconAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBeaconAdmStatus.setStatus("current")


class _SwDiagResult_Type(Integer32):
    """Custom type swDiagResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sw-embedded-port-fault", 3),
          ("sw-faulty", 2),
          ("sw-ok", 1))
    )


_SwDiagResult_Type.__name__ = "Integer32"
_SwDiagResult_Object = MibScalar
swDiagResult = _SwDiagResult_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 20),
    _SwDiagResult_Type()
)
swDiagResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDiagResult.setStatus("current")


class _SwNumSensors_Type(Integer32):
    """Custom type swNumSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNumSensors_Type.__name__ = "Integer32"
_SwNumSensors_Object = MibScalar
swNumSensors = _SwNumSensors_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 21),
    _SwNumSensors_Type()
)
swNumSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNumSensors.setStatus("current")
_SwSensorTable_Object = MibTable
swSensorTable = _SwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    swSensorTable.setStatus("current")
_SwSensorEntry_Object = MibTableRow
swSensorEntry = _SwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1)
)
swSensorEntry.setIndexNames(
    (0, "SW-MIB", "swSensorIndex"),
)
if mibBuilder.loadTexts:
    swSensorEntry.setStatus("current")
_SwSensorIndex_Type = SwSensorIndex
_SwSensorIndex_Object = MibTableColumn
swSensorIndex = _SwSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 1),
    _SwSensorIndex_Type()
)
swSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorIndex.setStatus("current")


class _SwSensorType_Type(Integer32):
    """Custom type swSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fan", 2),
          ("power-supply", 3),
          ("temperature", 1))
    )


_SwSensorType_Type.__name__ = "Integer32"
_SwSensorType_Object = MibTableColumn
swSensorType = _SwSensorType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 2),
    _SwSensorType_Type()
)
swSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorType.setStatus("current")


class _SwSensorStatus_Type(Integer32):
    """Custom type swSensorStatus based on Integer32"""
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
        *(("above-max", 5),
          ("absent", 6),
          ("below-min", 3),
          ("faulty", 2),
          ("nominal", 4),
          ("unknown", 1))
    )


_SwSensorStatus_Type.__name__ = "Integer32"
_SwSensorStatus_Object = MibTableColumn
swSensorStatus = _SwSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 3),
    _SwSensorStatus_Type()
)
swSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorStatus.setStatus("current")
_SwSensorValue_Type = Integer32
_SwSensorValue_Object = MibTableColumn
swSensorValue = _SwSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 4),
    _SwSensorValue_Type()
)
swSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorValue.setStatus("current")


class _SwSensorInfo_Type(DisplayString):
    """Custom type swSensorInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwSensorInfo_Type.__name__ = "DisplayString"
_SwSensorInfo_Object = MibTableColumn
swSensorInfo = _SwSensorInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 5),
    _SwSensorInfo_Type()
)
swSensorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorInfo.setStatus("current")
_SwTrackChangesInfo_Type = DisplayString
_SwTrackChangesInfo_Object = MibScalar
swTrackChangesInfo = _SwTrackChangesInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 23),
    _SwTrackChangesInfo_Type()
)
swTrackChangesInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrackChangesInfo.setStatus("current")
_SwID_Type = Integer32
_SwID_Object = MibScalar
swID = _SwID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 24),
    _SwID_Type()
)
swID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swID.setStatus("current")
_SwEtherIPAddress_Type = IpAddress
_SwEtherIPAddress_Object = MibScalar
swEtherIPAddress = _SwEtherIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 25),
    _SwEtherIPAddress_Type()
)
swEtherIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherIPAddress.setStatus("current")
_SwEtherIPMask_Type = IpAddress
_SwEtherIPMask_Object = MibScalar
swEtherIPMask = _SwEtherIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 26),
    _SwEtherIPMask_Type()
)
swEtherIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherIPMask.setStatus("current")
_SwFCIPAddress_Type = IpAddress
_SwFCIPAddress_Object = MibScalar
swFCIPAddress = _SwFCIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 27),
    _SwFCIPAddress_Type()
)
swFCIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCIPAddress.setStatus("current")
_SwFCIPMask_Type = IpAddress
_SwFCIPMask_Object = MibScalar
swFCIPMask = _SwFCIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 28),
    _SwFCIPMask_Type()
)
swFCIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCIPMask.setStatus("current")
_SwIPv6Address_Type = DisplayString
_SwIPv6Address_Object = MibScalar
swIPv6Address = _SwIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 29),
    _SwIPv6Address_Type()
)
swIPv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIPv6Address.setStatus("current")


class _SwIPv6Status_Type(Integer32):
    """Custom type swIPv6Status based on Integer32"""
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
        *(("inactive", 4),
          ("ipdeprecated", 3),
          ("preferred", 2),
          ("tentative", 1))
    )


_SwIPv6Status_Type.__name__ = "Integer32"
_SwIPv6Status_Object = MibScalar
swIPv6Status = _SwIPv6Status_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 30),
    _SwIPv6Status_Type()
)
swIPv6Status.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIPv6Status.setStatus("current")


class _SwModel_Type(Integer32):
    """Custom type swModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("switch7500", 1),
          ("switch7500E", 2))
    )


_SwModel_Type.__name__ = "Integer32"
_SwModel_Object = MibScalar
swModel = _SwModel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 31),
    _SwModel_Type()
)
swModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModel.setStatus("current")


class _SwTestString_Type(DisplayString):
    """Custom type swTestString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwTestString_Type.__name__ = "DisplayString"
_SwTestString_Object = MibScalar
swTestString = _SwTestString_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 32),
    _SwTestString_Type()
)
swTestString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swTestString.setStatus("current")
_SwPortList_Type = OctetString
_SwPortList_Object = MibScalar
swPortList = _SwPortList_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 33),
    _SwPortList_Type()
)
swPortList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortList.setStatus("current")
_SwBrcdTrapBitMask_Type = Integer32
_SwBrcdTrapBitMask_Object = MibScalar
swBrcdTrapBitMask = _SwBrcdTrapBitMask_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 34),
    _SwBrcdTrapBitMask_Type()
)
swBrcdTrapBitMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swBrcdTrapBitMask.setStatus("current")


class _SwFCPortPrevType_Type(Integer32):
    """Custom type swFCPortPrevType based on Integer32"""
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
        *(("e-port", 5),
          ("ex-port", 7),
          ("f-port", 4),
          ("fl-port", 3),
          ("g-port", 6),
          ("other", 2),
          ("unknown", 1))
    )


_SwFCPortPrevType_Type.__name__ = "Integer32"
_SwFCPortPrevType_Object = MibScalar
swFCPortPrevType = _SwFCPortPrevType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 35),
    _SwFCPortPrevType_Type()
)
swFCPortPrevType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swFCPortPrevType.setStatus("current")


class _SwDeviceStatus_Type(Integer32):
    """Custom type swDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("login", 1),
          ("logout", 2),
          ("unknown", 3))
    )


_SwDeviceStatus_Type.__name__ = "Integer32"
_SwDeviceStatus_Object = MibScalar
swDeviceStatus = _SwDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 36),
    _SwDeviceStatus_Type()
)
swDeviceStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDeviceStatus.setStatus("current")
_SwFabric_ObjectIdentity = ObjectIdentity
swFabric = _SwFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    swFabric.setStatus("current")
_SwDomainID_Type = SwDomainIndex
_SwDomainID_Object = MibScalar
swDomainID = _SwDomainID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 1),
    _SwDomainID_Type()
)
swDomainID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDomainID.setStatus("current")


class _SwPrincipalSwitch_Type(Integer32):
    """Custom type swPrincipalSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SwPrincipalSwitch_Type.__name__ = "Integer32"
_SwPrincipalSwitch_Object = MibScalar
swPrincipalSwitch = _SwPrincipalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 2),
    _SwPrincipalSwitch_Type()
)
swPrincipalSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPrincipalSwitch.setStatus("current")


class _SwNumNbs_Type(Integer32):
    """Custom type swNumNbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNumNbs_Type.__name__ = "Integer32"
_SwNumNbs_Object = MibScalar
swNumNbs = _SwNumNbs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 8),
    _SwNumNbs_Type()
)
swNumNbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNumNbs.setStatus("current")
_SwNbTable_Object = MibTable
swNbTable = _SwNbTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    swNbTable.setStatus("current")
_SwNbEntry_Object = MibTableRow
swNbEntry = _SwNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1)
)
swNbEntry.setIndexNames(
    (0, "SW-MIB", "swNbIndex"),
)
if mibBuilder.loadTexts:
    swNbEntry.setStatus("current")
_SwNbIndex_Type = SwNbIndex
_SwNbIndex_Object = MibTableColumn
swNbIndex = _SwNbIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 1),
    _SwNbIndex_Type()
)
swNbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbIndex.setStatus("current")
_SwNbMyPort_Type = SwPortIndex
_SwNbMyPort_Object = MibTableColumn
swNbMyPort = _SwNbMyPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 2),
    _SwNbMyPort_Type()
)
swNbMyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbMyPort.setStatus("current")
_SwNbRemDomain_Type = SwDomainIndex
_SwNbRemDomain_Object = MibTableColumn
swNbRemDomain = _SwNbRemDomain_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 3),
    _SwNbRemDomain_Type()
)
swNbRemDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbRemDomain.setStatus("current")
_SwNbRemPort_Type = SwPortIndex
_SwNbRemPort_Object = MibTableColumn
swNbRemPort = _SwNbRemPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 4),
    _SwNbRemPort_Type()
)
swNbRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbRemPort.setStatus("current")


class _SwNbBaudRate_Type(Integer32):
    """Custom type swNbBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("decuple", 256),
          ("double", 32),
          ("full", 16),
          ("half", 8),
          ("octuple", 128),
          ("oneEighth", 2),
          ("other", 1),
          ("quadruple", 64),
          ("quarter", 4),
          ("sexdecuple", 512))
    )


_SwNbBaudRate_Type.__name__ = "Integer32"
_SwNbBaudRate_Object = MibTableColumn
swNbBaudRate = _SwNbBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 5),
    _SwNbBaudRate_Type()
)
swNbBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbBaudRate.setStatus("current")


class _SwNbIslState_Type(Integer32):
    """Custom type swNbIslState based on Integer32"""
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
        *(("sw-active", 5),
          ("sw-down", 0),
          ("sw-init", 1),
          ("sw-internal2", 2),
          ("sw-internal3", 3),
          ("sw-internal4", 4))
    )


_SwNbIslState_Type.__name__ = "Integer32"
_SwNbIslState_Object = MibTableColumn
swNbIslState = _SwNbIslState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 6),
    _SwNbIslState_Type()
)
swNbIslState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbIslState.setStatus("current")


class _SwNbIslCost_Type(Integer32):
    """Custom type swNbIslCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNbIslCost_Type.__name__ = "Integer32"
_SwNbIslCost_Object = MibTableColumn
swNbIslCost = _SwNbIslCost_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 7),
    _SwNbIslCost_Type()
)
swNbIslCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swNbIslCost.setStatus("current")


class _SwNbRemPortName_Type(OctetString):
    """Custom type swNbRemPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwNbRemPortName_Type.__name__ = "OctetString"
_SwNbRemPortName_Object = MibTableColumn
swNbRemPortName = _SwNbRemPortName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 8),
    _SwNbRemPortName_Type()
)
swNbRemPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbRemPortName.setStatus("current")
_SwFabricMemTable_Object = MibTable
swFabricMemTable = _SwFabricMemTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    swFabricMemTable.setStatus("current")
_SwFabricMemEntry_Object = MibTableRow
swFabricMemEntry = _SwFabricMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1)
)
swFabricMemEntry.setIndexNames(
    (0, "SW-MIB", "swFabricMemWwn"),
)
if mibBuilder.loadTexts:
    swFabricMemEntry.setStatus("current")
_SwFabricMemWwn_Type = FcWwn
_SwFabricMemWwn_Object = MibTableColumn
swFabricMemWwn = _SwFabricMemWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 1),
    _SwFabricMemWwn_Type()
)
swFabricMemWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemWwn.setStatus("current")
_SwFabricMemDid_Type = SwDomainIndex
_SwFabricMemDid_Object = MibTableColumn
swFabricMemDid = _SwFabricMemDid_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 2),
    _SwFabricMemDid_Type()
)
swFabricMemDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemDid.setStatus("current")


class _SwFabricMemName_Type(DisplayString):
    """Custom type swFabricMemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFabricMemName_Type.__name__ = "DisplayString"
_SwFabricMemName_Object = MibTableColumn
swFabricMemName = _SwFabricMemName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 3),
    _SwFabricMemName_Type()
)
swFabricMemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemName.setStatus("current")
_SwFabricMemEIP_Type = IpAddress
_SwFabricMemEIP_Object = MibTableColumn
swFabricMemEIP = _SwFabricMemEIP_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 4),
    _SwFabricMemEIP_Type()
)
swFabricMemEIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemEIP.setStatus("current")
_SwFabricMemFCIP_Type = IpAddress
_SwFabricMemFCIP_Object = MibTableColumn
swFabricMemFCIP = _SwFabricMemFCIP_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 5),
    _SwFabricMemFCIP_Type()
)
swFabricMemFCIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemFCIP.setStatus("current")
_SwFabricMemGWIP_Type = IpAddress
_SwFabricMemGWIP_Object = MibTableColumn
swFabricMemGWIP = _SwFabricMemGWIP_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 6),
    _SwFabricMemGWIP_Type()
)
swFabricMemGWIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemGWIP.setStatus("current")


class _SwFabricMemType_Type(Integer32):
    """Custom type swFabricMemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFabricMemType_Type.__name__ = "Integer32"
_SwFabricMemType_Object = MibTableColumn
swFabricMemType = _SwFabricMemType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 7),
    _SwFabricMemType_Type()
)
swFabricMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemType.setStatus("current")


class _SwFabricMemShortVersion_Type(OctetString):
    """Custom type swFabricMemShortVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SwFabricMemShortVersion_Type.__name__ = "OctetString"
_SwFabricMemShortVersion_Object = MibTableColumn
swFabricMemShortVersion = _SwFabricMemShortVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 8),
    _SwFabricMemShortVersion_Type()
)
swFabricMemShortVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemShortVersion.setStatus("current")


class _SwIDIDMode_Type(Integer32):
    """Custom type swIDIDMode based on Integer32"""
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


_SwIDIDMode_Type.__name__ = "Integer32"
_SwIDIDMode_Object = MibScalar
swIDIDMode = _SwIDIDMode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 11),
    _SwIDIDMode_Type()
)
swIDIDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIDIDMode.setStatus("current")


class _SwPmgrEventType_Type(Integer32):
    """Custom type swPmgrEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("basechange", 4),
          ("create", 0),
          ("delete", 1),
          ("fidchange", 3),
          ("moveport", 2),
          ("vfstatechange", 6))
    )


_SwPmgrEventType_Type.__name__ = "Integer32"
_SwPmgrEventType_Object = MibScalar
swPmgrEventType = _SwPmgrEventType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 12),
    _SwPmgrEventType_Type()
)
swPmgrEventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPmgrEventType.setStatus("current")


class _SwPmgrEventTime_Type(DisplayString):
    """Custom type swPmgrEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwPmgrEventTime_Type.__name__ = "DisplayString"
_SwPmgrEventTime_Object = MibScalar
swPmgrEventTime = _SwPmgrEventTime_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 13),
    _SwPmgrEventTime_Type()
)
swPmgrEventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPmgrEventTime.setStatus("current")


class _SwPmgrEventDescr_Type(DisplayString):
    """Custom type swPmgrEventDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwPmgrEventDescr_Type.__name__ = "DisplayString"
_SwPmgrEventDescr_Object = MibScalar
swPmgrEventDescr = _SwPmgrEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 14),
    _SwPmgrEventDescr_Type()
)
swPmgrEventDescr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPmgrEventDescr.setStatus("current")


class _SwVfId_Type(Integer32):
    """Custom type swVfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwVfId_Type.__name__ = "Integer32"
_SwVfId_Object = MibScalar
swVfId = _SwVfId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 15),
    _SwVfId_Type()
)
swVfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVfId.setStatus("current")
_SwVfName_Type = DisplayString
_SwVfName_Object = MibScalar
swVfName = _SwVfName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 16),
    _SwVfName_Type()
)
swVfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVfName.setStatus("current")
_SwModule_ObjectIdentity = ObjectIdentity
swModule = _SwModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    swModule.setStatus("current")
_SwAgtCfg_ObjectIdentity = ObjectIdentity
swAgtCfg = _SwAgtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    swAgtCfg.setStatus("current")
_SwAgtCmtyTable_Object = MibTable
swAgtCmtyTable = _SwAgtCmtyTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11)
)
if mibBuilder.loadTexts:
    swAgtCmtyTable.setStatus("deprecated")
_SwAgtCmtyEntry_Object = MibTableRow
swAgtCmtyEntry = _SwAgtCmtyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1)
)
swAgtCmtyEntry.setIndexNames(
    (0, "SW-MIB", "swAgtCmtyIdx"),
)
if mibBuilder.loadTexts:
    swAgtCmtyEntry.setStatus("deprecated")


class _SwAgtCmtyIdx_Type(Integer32):
    """Custom type swAgtCmtyIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SwAgtCmtyIdx_Type.__name__ = "Integer32"
_SwAgtCmtyIdx_Object = MibTableColumn
swAgtCmtyIdx = _SwAgtCmtyIdx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 1),
    _SwAgtCmtyIdx_Type()
)
swAgtCmtyIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAgtCmtyIdx.setStatus("deprecated")


class _SwAgtCmtyStr_Type(DisplayString):
    """Custom type swAgtCmtyStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_SwAgtCmtyStr_Type.__name__ = "DisplayString"
_SwAgtCmtyStr_Object = MibTableColumn
swAgtCmtyStr = _SwAgtCmtyStr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 2),
    _SwAgtCmtyStr_Type()
)
swAgtCmtyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAgtCmtyStr.setStatus("deprecated")
_SwAgtTrapRcp_Type = IpAddress
_SwAgtTrapRcp_Object = MibTableColumn
swAgtTrapRcp = _SwAgtTrapRcp_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 3),
    _SwAgtTrapRcp_Type()
)
swAgtTrapRcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAgtTrapRcp.setStatus("deprecated")
_SwAgtTrapSeverityLevel_Type = SwSevType
_SwAgtTrapSeverityLevel_Object = MibTableColumn
swAgtTrapSeverityLevel = _SwAgtTrapSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 4),
    _SwAgtTrapSeverityLevel_Type()
)
swAgtTrapSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAgtTrapSeverityLevel.setStatus("deprecated")


class _SwauthProtocolPassword_Type(OctetString):
    """Custom type swauthProtocolPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwauthProtocolPassword_Type.__name__ = "OctetString"
_SwauthProtocolPassword_Object = MibScalar
swauthProtocolPassword = _SwauthProtocolPassword_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 12),
    _SwauthProtocolPassword_Type()
)
swauthProtocolPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swauthProtocolPassword.setStatus("current")


class _SwprivProtocolPassword_Type(OctetString):
    """Custom type swprivProtocolPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwprivProtocolPassword_Type.__name__ = "OctetString"
_SwprivProtocolPassword_Object = MibScalar
swprivProtocolPassword = _SwprivProtocolPassword_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 13),
    _SwprivProtocolPassword_Type()
)
swprivProtocolPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swprivProtocolPassword.setStatus("current")
_SwFCport_ObjectIdentity = ObjectIdentity
swFCport = _SwFCport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    swFCport.setStatus("current")


class _SwFCPortCapacity_Type(Integer32):
    """Custom type swFCPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFCPortCapacity_Type.__name__ = "Integer32"
_SwFCPortCapacity_Object = MibScalar
swFCPortCapacity = _SwFCPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 1),
    _SwFCPortCapacity_Type()
)
swFCPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortCapacity.setStatus("current")
_SwFCPortTable_Object = MibTable
swFCPortTable = _SwFCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    swFCPortTable.setStatus("current")
_SwFCPortEntry_Object = MibTableRow
swFCPortEntry = _SwFCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1)
)
swFCPortEntry.setIndexNames(
    (0, "SW-MIB", "swFCPortIndex"),
)
if mibBuilder.loadTexts:
    swFCPortEntry.setStatus("current")
_SwFCPortIndex_Type = SwPortIndex
_SwFCPortIndex_Object = MibTableColumn
swFCPortIndex = _SwFCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 1),
    _SwFCPortIndex_Type()
)
swFCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortIndex.setStatus("current")


class _SwFCPortType_Type(Integer32):
    """Custom type swFCPortType based on Integer32"""
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
        *(("bloom", 4),
          ("flannel", 2),
          ("loom", 3),
          ("other", 7),
          ("rdbloom", 5),
          ("stitch", 1),
          ("unknown", 8),
          ("wormhole", 6))
    )


_SwFCPortType_Type.__name__ = "Integer32"
_SwFCPortType_Object = MibTableColumn
swFCPortType = _SwFCPortType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 2),
    _SwFCPortType_Type()
)
swFCPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortType.setStatus("current")


class _SwFCPortPhyState_Type(Integer32):
    """Custom type swFCPortPhyState based on Integer32"""
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
              14,
              255)
        )
    )
    namedValues = NamedValues(
        *(("diagFault", 8),
          ("inSync", 6),
          ("invalidModule", 11),
          ("laserFault", 3),
          ("lockRef", 9),
          ("noCard", 1),
          ("noLight", 4),
          ("noSigDet", 14),
          ("noSync", 5),
          ("noTransceiver", 2),
          ("portFault", 7),
          ("unknown", 255),
          ("validating", 10))
    )


_SwFCPortPhyState_Type.__name__ = "Integer32"
_SwFCPortPhyState_Object = MibTableColumn
swFCPortPhyState = _SwFCPortPhyState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 3),
    _SwFCPortPhyState_Type()
)
swFCPortPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortPhyState.setStatus("current")


class _SwFCPortOpStatus_Type(Integer32):
    """Custom type swFCPortOpStatus based on Integer32"""
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
        *(("faulty", 4),
          ("offline", 2),
          ("online", 1),
          ("testing", 3),
          ("unknown", 0))
    )


_SwFCPortOpStatus_Type.__name__ = "Integer32"
_SwFCPortOpStatus_Object = MibTableColumn
swFCPortOpStatus = _SwFCPortOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 4),
    _SwFCPortOpStatus_Type()
)
swFCPortOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortOpStatus.setStatus("current")


class _SwFCPortAdmStatus_Type(Integer32):
    """Custom type swFCPortAdmStatus based on Integer32"""
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
        *(("faulty", 4),
          ("offline", 2),
          ("online", 1),
          ("testing", 3))
    )


_SwFCPortAdmStatus_Type.__name__ = "Integer32"
_SwFCPortAdmStatus_Object = MibTableColumn
swFCPortAdmStatus = _SwFCPortAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 5),
    _SwFCPortAdmStatus_Type()
)
swFCPortAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFCPortAdmStatus.setStatus("current")


class _SwFCPortLinkState_Type(Integer32):
    """Custom type swFCPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("loopback", 3))
    )


_SwFCPortLinkState_Type.__name__ = "Integer32"
_SwFCPortLinkState_Object = MibTableColumn
swFCPortLinkState = _SwFCPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 6),
    _SwFCPortLinkState_Type()
)
swFCPortLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFCPortLinkState.setStatus("current")


class _SwFCPortTxType_Type(Integer32):
    """Custom type swFCPortTxType based on Integer32"""
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
        *(("cu", 5),
          ("ld", 4),
          ("lw", 2),
          ("sw", 3),
          ("unknown", 1))
    )


_SwFCPortTxType_Type.__name__ = "Integer32"
_SwFCPortTxType_Object = MibTableColumn
swFCPortTxType = _SwFCPortTxType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 7),
    _SwFCPortTxType_Type()
)
swFCPortTxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxType.setStatus("current")
_SwFCPortTxWords_Type = Counter32
_SwFCPortTxWords_Object = MibTableColumn
swFCPortTxWords = _SwFCPortTxWords_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 11),
    _SwFCPortTxWords_Type()
)
swFCPortTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxWords.setStatus("current")
_SwFCPortRxWords_Type = Counter32
_SwFCPortRxWords_Object = MibTableColumn
swFCPortRxWords = _SwFCPortRxWords_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 12),
    _SwFCPortRxWords_Type()
)
swFCPortRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxWords.setStatus("current")
_SwFCPortTxFrames_Type = Counter32
_SwFCPortTxFrames_Object = MibTableColumn
swFCPortTxFrames = _SwFCPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 13),
    _SwFCPortTxFrames_Type()
)
swFCPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxFrames.setStatus("current")
_SwFCPortRxFrames_Type = Counter32
_SwFCPortRxFrames_Object = MibTableColumn
swFCPortRxFrames = _SwFCPortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 14),
    _SwFCPortRxFrames_Type()
)
swFCPortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxFrames.setStatus("current")
_SwFCPortRxC2Frames_Type = Counter32
_SwFCPortRxC2Frames_Object = MibTableColumn
swFCPortRxC2Frames = _SwFCPortRxC2Frames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 15),
    _SwFCPortRxC2Frames_Type()
)
swFCPortRxC2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxC2Frames.setStatus("current")
_SwFCPortRxC3Frames_Type = Counter32
_SwFCPortRxC3Frames_Object = MibTableColumn
swFCPortRxC3Frames = _SwFCPortRxC3Frames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 16),
    _SwFCPortRxC3Frames_Type()
)
swFCPortRxC3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxC3Frames.setStatus("current")
_SwFCPortRxLCs_Type = Counter32
_SwFCPortRxLCs_Object = MibTableColumn
swFCPortRxLCs = _SwFCPortRxLCs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 17),
    _SwFCPortRxLCs_Type()
)
swFCPortRxLCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxLCs.setStatus("current")
_SwFCPortRxMcasts_Type = Counter32
_SwFCPortRxMcasts_Object = MibTableColumn
swFCPortRxMcasts = _SwFCPortRxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 18),
    _SwFCPortRxMcasts_Type()
)
swFCPortRxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxMcasts.setStatus("current")
_SwFCPortTooManyRdys_Type = Counter32
_SwFCPortTooManyRdys_Object = MibTableColumn
swFCPortTooManyRdys = _SwFCPortTooManyRdys_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 19),
    _SwFCPortTooManyRdys_Type()
)
swFCPortTooManyRdys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTooManyRdys.setStatus("current")
_SwFCPortNoTxCredits_Type = Counter32
_SwFCPortNoTxCredits_Object = MibTableColumn
swFCPortNoTxCredits = _SwFCPortNoTxCredits_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 20),
    _SwFCPortNoTxCredits_Type()
)
swFCPortNoTxCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortNoTxCredits.setStatus("current")
_SwFCPortRxEncInFrs_Type = Counter32
_SwFCPortRxEncInFrs_Object = MibTableColumn
swFCPortRxEncInFrs = _SwFCPortRxEncInFrs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 21),
    _SwFCPortRxEncInFrs_Type()
)
swFCPortRxEncInFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxEncInFrs.setStatus("current")
_SwFCPortRxCrcs_Type = Counter32
_SwFCPortRxCrcs_Object = MibTableColumn
swFCPortRxCrcs = _SwFCPortRxCrcs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 22),
    _SwFCPortRxCrcs_Type()
)
swFCPortRxCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxCrcs.setStatus("current")
_SwFCPortRxTruncs_Type = Counter32
_SwFCPortRxTruncs_Object = MibTableColumn
swFCPortRxTruncs = _SwFCPortRxTruncs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 23),
    _SwFCPortRxTruncs_Type()
)
swFCPortRxTruncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxTruncs.setStatus("current")
_SwFCPortRxTooLongs_Type = Counter32
_SwFCPortRxTooLongs_Object = MibTableColumn
swFCPortRxTooLongs = _SwFCPortRxTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 24),
    _SwFCPortRxTooLongs_Type()
)
swFCPortRxTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxTooLongs.setStatus("current")
_SwFCPortRxBadEofs_Type = Counter32
_SwFCPortRxBadEofs_Object = MibTableColumn
swFCPortRxBadEofs = _SwFCPortRxBadEofs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 25),
    _SwFCPortRxBadEofs_Type()
)
swFCPortRxBadEofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxBadEofs.setStatus("current")
_SwFCPortRxEncOutFrs_Type = Counter32
_SwFCPortRxEncOutFrs_Object = MibTableColumn
swFCPortRxEncOutFrs = _SwFCPortRxEncOutFrs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 26),
    _SwFCPortRxEncOutFrs_Type()
)
swFCPortRxEncOutFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxEncOutFrs.setStatus("current")
_SwFCPortRxBadOs_Type = Counter32
_SwFCPortRxBadOs_Object = MibTableColumn
swFCPortRxBadOs = _SwFCPortRxBadOs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 27),
    _SwFCPortRxBadOs_Type()
)
swFCPortRxBadOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxBadOs.setStatus("current")
_SwFCPortC3Discards_Type = Counter32
_SwFCPortC3Discards_Object = MibTableColumn
swFCPortC3Discards = _SwFCPortC3Discards_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 28),
    _SwFCPortC3Discards_Type()
)
swFCPortC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortC3Discards.setStatus("current")
_SwFCPortMcastTimedOuts_Type = Counter32
_SwFCPortMcastTimedOuts_Object = MibTableColumn
swFCPortMcastTimedOuts = _SwFCPortMcastTimedOuts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 29),
    _SwFCPortMcastTimedOuts_Type()
)
swFCPortMcastTimedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortMcastTimedOuts.setStatus("current")
_SwFCPortTxMcasts_Type = Counter32
_SwFCPortTxMcasts_Object = MibTableColumn
swFCPortTxMcasts = _SwFCPortTxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 30),
    _SwFCPortTxMcasts_Type()
)
swFCPortTxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxMcasts.setStatus("current")
_SwFCPortLipIns_Type = Counter32
_SwFCPortLipIns_Object = MibTableColumn
swFCPortLipIns = _SwFCPortLipIns_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 31),
    _SwFCPortLipIns_Type()
)
swFCPortLipIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipIns.setStatus("current")
_SwFCPortLipOuts_Type = Counter32
_SwFCPortLipOuts_Object = MibTableColumn
swFCPortLipOuts = _SwFCPortLipOuts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 32),
    _SwFCPortLipOuts_Type()
)
swFCPortLipOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipOuts.setStatus("current")


class _SwFCPortLipLastAlpa_Type(OctetString):
    """Custom type swFCPortLipLastAlpa based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwFCPortLipLastAlpa_Type.__name__ = "OctetString"
_SwFCPortLipLastAlpa_Object = MibTableColumn
swFCPortLipLastAlpa = _SwFCPortLipLastAlpa_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 33),
    _SwFCPortLipLastAlpa_Type()
)
swFCPortLipLastAlpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipLastAlpa.setStatus("current")


class _SwFCPortWwn_Type(OctetString):
    """Custom type swFCPortWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwFCPortWwn_Type.__name__ = "OctetString"
_SwFCPortWwn_Object = MibTableColumn
swFCPortWwn = _SwFCPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 34),
    _SwFCPortWwn_Type()
)
swFCPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortWwn.setStatus("current")


class _SwFCPortSpeed_Type(Integer32):
    """Custom type swFCPortSpeed based on Integer32"""
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
        *(("auto-Negotiate", 3),
          ("eight-GB", 5),
          ("four-GB", 4),
          ("one-GB", 1),
          ("sixteen-GB", 8),
          ("ten-GB", 6),
          ("two-GB", 2),
          ("unknown", 7))
    )


_SwFCPortSpeed_Type.__name__ = "Integer32"
_SwFCPortSpeed_Object = MibTableColumn
swFCPortSpeed = _SwFCPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 35),
    _SwFCPortSpeed_Type()
)
swFCPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFCPortSpeed.setStatus("obsolete")


class _SwFCPortName_Type(DisplayString):
    """Custom type swFCPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFCPortName_Type.__name__ = "DisplayString"
_SwFCPortName_Object = MibTableColumn
swFCPortName = _SwFCPortName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 36),
    _SwFCPortName_Type()
)
swFCPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortName.setStatus("current")
_SwFCPortSpecifier_Type = DisplayString
_SwFCPortSpecifier_Object = MibTableColumn
swFCPortSpecifier = _SwFCPortSpecifier_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 37),
    _SwFCPortSpecifier_Type()
)
swFCPortSpecifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortSpecifier.setStatus("current")
_SwFCPortFlag_Type = FcPortFlag
_SwFCPortFlag_Object = MibTableColumn
swFCPortFlag = _SwFCPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 38),
    _SwFCPortFlag_Type()
)
swFCPortFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortFlag.setStatus("current")


class _SwFCPortBrcdType_Type(Integer32):
    """Custom type swFCPortBrcdType based on Integer32"""
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
        *(("e-port", 5),
          ("ex-port", 7),
          ("f-port", 4),
          ("fl-port", 3),
          ("g-port", 6),
          ("other", 2),
          ("unknown", 1))
    )


_SwFCPortBrcdType_Type.__name__ = "Integer32"
_SwFCPortBrcdType_Object = MibTableColumn
swFCPortBrcdType = _SwFCPortBrcdType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 39),
    _SwFCPortBrcdType_Type()
)
swFCPortBrcdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortBrcdType.setStatus("current")


class _SwFCPortDisableReason_Type(Integer32):
    """Custom type swFCPortDisableReason based on Integer32"""
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
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
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
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230)
        )
    )
    namedValues = NamedValues(
        *(("f-port-disable-no-trk-lic", 110),
          ("f-port-tr-disable-speed-not-ok", 113),
          ("r-10g-mode-incompat", 149),
          ("r-1g-mode-incompat", 148),
          ("r-ad", 135),
          ("r-area-in-use", 100),
          ("r-auth-fail-retry", 38),
          ("r-auth-not-supported-in-switch", 228),
          ("r-auth-rejected", 36),
          ("r-auth-timeout", 37),
          ("r-authentication-required", 121),
          ("r-bad-ecp-rcvd", 23),
          ("r-base-switch-supports-no-device", 116),
          ("r-bl-disabled", 5),
          ("r-bl-enabled", 8),
          ("r-brcdfabconn", 91),
          ("r-buf-starv", 29),
          ("r-cannot-unbind-existing-area", 119),
          ("r-cannot-use-10bit-area", 120),
          ("r-cfg-not-supported", 106),
          ("r-cfgspeed-not-supported", 203),
          ("r-did-overlap", 125),
          ("r-domain-id-change", 35),
          ("r-dual-mode-incompat", 150),
          ("r-dup-wwn", 133),
          ("r-ecp-in-testing", 19),
          ("r-ecp-longdist", 132),
          ("r-ecp-retries-exceeded", 21),
          ("r-eicl-license-limited", 221),
          ("r-elp-fctl-mismatch", 30),
          ("r-elp-in-testing", 20),
          ("r-elp-retries-exceeded", 51),
          ("r-em-incnst", 27),
          ("r-enh-tizone", 181),
          ("r-eport-c3txto-th-exceeded", 162),
          ("r-eport-crc-th-exceeded", 159),
          ("r-eport-disabled", 31),
          ("r-eport-inw-th-exceeded", 158),
          ("r-eport-isolated", 134),
          ("r-eport-ll-th-exceeded", 155),
          ("r-eport-locked", 180),
          ("r-eport-lr-th-exceeded", 160),
          ("r-eport-not-supported", 104),
          ("r-eport-not-supported-def-sw", 154),
          ("r-eport-pe-th-exceeded", 157),
          ("r-eport-seg", 127),
          ("r-eport-st-th-exceeded", 161),
          ("r-eport-synl-th-exceeded", 156),
          ("r-esc-base-sw", 222),
          ("r-esc-did-offset", 136),
          ("r-esc-etiz", 137),
          ("r-esc-fid", 138),
          ("r-esc-vlanid", 184),
          ("r-fcr-authn-reject", 60),
          ("r-fcr-class-f-incompat", 67),
          ("r-fcr-class-n-incompat", 68),
          ("r-fcr-conf-ex", 54),
          ("r-fcr-conf-mismatch1", 39),
          ("r-fcr-conf-mismatch2", 40),
          ("r-fcr-elp-fctl-mismatch", 46),
          ("r-fcr-elp-ver-inconsis", 45),
          ("r-fcr-ex-port-not-allowed", 204),
          ("r-fcr-export-in-non-base-sw", 115),
          ("r-fcr-export-lf-conflict", 123),
          ("r-fcr-exports-exceeded", 52),
          ("r-fcr-fabric-binding-failure", 98),
          ("r-fcr-fowner-conflict", 57),
          ("r-fcr-ftag-conflict", 56),
          ("r-fcr-ftag-over", 55),
          ("r-fcr-generic", 65),
          ("r-fcr-incompatible-mode", 63),
          ("r-fcr-insistent-front-did-mismatch", 97),
          ("r-fcr-interop-conf", 216),
          ("r-fcr-invalid-flow-rcvd", 69),
          ("r-fcr-isolated", 50),
          ("r-fcr-ld-credit-mismatch", 42),
          ("r-fcr-ld-incompat", 49),
          ("r-fcr-license", 53),
          ("r-fcr-non-standard-domain-offset", 99),
          ("r-fcr-pid-mismatch", 47),
          ("r-fcr-port-ld-mode-mismatch", 41),
          ("r-fcr-port-state-to", 59),
          ("r-fcr-sec-failure", 62),
          ("r-fcr-sec-fcs-list", 61),
          ("r-fcr-sec-scc-list", 64),
          ("r-fcr-set-rtc-failed", 44),
          ("r-fcr-set-vcc-failed", 43),
          ("r-fcr-state-disabled", 70),
          ("r-fcr-tov-mismatch", 48),
          ("r-fcr-trunk-master-sfid-not-set", 206),
          ("r-fcr-zone-resource", 58),
          ("r-fcuport-c3txto-th-exceeded", 178),
          ("r-fcuport-crc-th-exceeded", 175),
          ("r-fcuport-inw-th-exceeded", 174),
          ("r-fcuport-ll-th-exceeded", 171),
          ("r-fcuport-lr-th-exceeded", 176),
          ("r-fcuport-pe-th-exceeded", 173),
          ("r-fcuport-st-th-exceeded", 177),
          ("r-fcuport-synl-th-exceeded", 172),
          ("r-fdd-cfg-conflict", 95),
          ("r-fdd-cfg-conflict-na-neigh", 96),
          ("r-fdd-strict-conflict", 94),
          ("r-fdd-strict-dcc-conflict", 212),
          ("r-fdd-strict-exist", 71),
          ("r-fdd-strict-fabwide-conflict", 214),
          ("r-fdd-strict-fcs-conflict", 213),
          ("r-fdd-strict-pwd-conflict", 215),
          ("r-fdd-strict-scc-conflict", 211),
          ("r-flogidupalpa", 87),
          ("r-flogifailed", 83),
          ("r-floginport", 93),
          ("r-fopport-c3txto-th-exceeded", 170),
          ("r-fopport-crc-th-exceeded", 167),
          ("r-fopport-inw-th-exceeded", 166),
          ("r-fopport-ll-th-exceeded", 163),
          ("r-fopport-lr-th-exceeded", 168),
          ("r-fopport-pe-th-exceeded", 165),
          ("r-fopport-st-th-exceeded", 169),
          ("r-fopport-synl-th-exceeded", 164),
          ("r-forced", 3),
          ("r-fport-not-supported", 105),
          ("r-fport-slow-drain-condition", 183),
          ("r-icl-ex-on-non-vf", 229),
          ("r-implict-plt-service-block", 151),
          ("r-incompat", 124),
          ("r-inconsistent", 17),
          ("r-invalid-ecp-state", 22),
          ("r-invalid-reason", 2),
          ("r-last-port-disable-msg", 72),
          ("r-link-reinit", 34),
          ("r-loopcfg", 88),
          ("r-max-flogi-reached", 227),
          ("r-msfr", 146),
          ("r-mstr-diff-area", 102),
          ("r-mstr-diff-pg", 101),
          ("r-no-area-avail", 118),
          ("r-no-eicl-license", 220),
          ("r-no-icl-license", 209),
          ("r-no-icl-pod2-license", 224),
          ("r-no-license", 128),
          ("r-no-port-open-rsp", 219),
          ("r-no-ten-gig-license", 210),
          ("r-noenclicense", 89),
          ("r-nofiportmapping", 90),
          ("r-noflogi", 85),
          ("r-noflogiresp", 86),
          ("r-nomapping", 80),
          ("r-non-rcs-rem-dom", 198),
          ("r-nonpiv", 79),
          ("r-nportbusy", 84),
          ("r-nportistrunkmem", 207),
          ("r-nportlogin-inprogress", 78),
          ("r-nportoffline", 82),
          ("r-online-incomplete", 15),
          ("r-online-route-fail", 16),
          ("r-pci-attach-fail", 28),
          ("r-peer-port-in-di-zone", 74),
          ("r-pers-pid-on-lport", 142),
          ("r-pers-pid-port-addr-bnd", 145),
          ("r-pers-pid-port-on-same-area", 144),
          ("r-pers-pid-portaddr-collision", 143),
          ("r-persistid", 10),
          ("r-platform-db", 129),
          ("r-policynotsupported", 208),
          ("r-port-area-mismatch-pers-disable", 225),
          ("r-port-auto-disable", 114),
          ("r-port-auto-disable-lip", 190),
          ("r-port-auto-disable-losg", 187),
          ("r-port-auto-disable-losn", 186),
          ("r-port-auto-disable-nos", 189),
          ("r-port-auto-disable-ols", 188),
          ("r-port-c3txto-th-exceeded", 153),
          ("r-port-comp-interop-conflict", 218),
          ("r-port-compression", 191),
          ("r-port-crc-th-exceeded", 112),
          ("r-port-data-fail", 14),
          ("r-port-decommissioned", 194),
          ("r-port-disable-on-zeroize", 202),
          ("r-port-dport-incompat", 196),
          ("r-port-dportmode", 195),
          ("r-port-duplicate-pwwn", 205),
          ("r-port-enc-auth-disabled", 201),
          ("r-port-enc-comp-mismatch", 197),
          ("r-port-enc-interop-conflict", 217),
          ("r-port-enccomp-res", 193),
          ("r-port-encryption", 192),
          ("r-port-fips-comp-mismatch", 199),
          ("r-port-inw-th-exceeded", 111),
          ("r-port-ll-th-exceeded", 107),
          ("r-port-lr-th-exceeded", 122),
          ("r-port-no-area-avail-pers-disable", 179),
          ("r-port-non-fips-comp-mismatch", 200),
          ("r-port-pe-th-exceeded", 109),
          ("r-port-recov-state", 185),
          ("r-port-reset", 92),
          ("r-port-st-th-exceeded", 152),
          ("r-port-synl-th-exceeded", 108),
          ("r-port-trunk-proto-error", 117),
          ("r-prv-dev-violation", 12),
          ("r-pub-dev-violation", 13),
          ("r-recover-fail", 1),
          ("r-safe-zone", 139),
          ("r-save-link-rtt-fail", 26),
          ("r-sec-incompat", 130),
          ("r-sec-violation", 131),
          ("r-send-ecp-fail", 25),
          ("r-send-rtmark-fail", 24),
          ("r-set-vcc-fail", 18),
          ("r-slot-off", 6),
          ("r-slot-on", 9),
          ("r-sw-config-l-port-not-support", 76),
          ("r-sw-cpu-overload", 223),
          ("r-sw-disabled", 4),
          ("r-sw-enabled", 7),
          ("r-sw-ex-port-not-ready", 66),
          ("r-sw-fl-port-not-ready", 33),
          ("r-sw-halfbw-lic", 147),
          ("r-sw-l-port-not-support", 73),
          ("r-sw-port-mirror-configured", 77),
          ("r-sw-port-swap-not-supported", 182),
          ("r-sw-violation", 11),
          ("r-ta-not-supported", 103),
          ("r-trunk-with-vcxlt", 32),
          ("r-unauthorized-device", 226),
          ("r-unknowntype", 81),
          ("r-user-disabled-reason", 230),
          ("r-vf", 140),
          ("r-vf-bs-incompat", 141),
          ("r-zone-conflict", 126),
          ("r-zone-incompat", 75))
    )


_SwFCPortDisableReason_Type.__name__ = "Integer32"
_SwFCPortDisableReason_Object = MibTableColumn
swFCPortDisableReason = _SwFCPortDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 40),
    _SwFCPortDisableReason_Type()
)
swFCPortDisableReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swFCPortDisableReason.setStatus("current")
_SwNs_ObjectIdentity = ObjectIdentity
swNs = _SwNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    swNs.setStatus("current")


class _SwNsLocalNumEntry_Type(Integer32):
    """Custom type swNsLocalNumEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNsLocalNumEntry_Type.__name__ = "Integer32"
_SwNsLocalNumEntry_Object = MibScalar
swNsLocalNumEntry = _SwNsLocalNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 1),
    _SwNsLocalNumEntry_Type()
)
swNsLocalNumEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsLocalNumEntry.setStatus("current")
_SwNsLocalTable_Object = MibTable
swNsLocalTable = _SwNsLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    swNsLocalTable.setStatus("current")
_SwNsLocalEntry_Object = MibTableRow
swNsLocalEntry = _SwNsLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1)
)
swNsLocalEntry.setIndexNames(
    (0, "SW-MIB", "swNsEntryIndex"),
)
if mibBuilder.loadTexts:
    swNsLocalEntry.setStatus("current")


class _SwNsEntryIndex_Type(Integer32):
    """Custom type swNsEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNsEntryIndex_Type.__name__ = "Integer32"
_SwNsEntryIndex_Object = MibTableColumn
swNsEntryIndex = _SwNsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 1),
    _SwNsEntryIndex_Type()
)
swNsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsEntryIndex.setStatus("current")


class _SwNsPortID_Type(OctetString):
    """Custom type swNsPortID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwNsPortID_Type.__name__ = "OctetString"
_SwNsPortID_Object = MibTableColumn
swNsPortID = _SwNsPortID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 2),
    _SwNsPortID_Type()
)
swNsPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortID.setStatus("current")


class _SwNsPortType_Type(Integer32):
    """Custom type swNsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nPort", 1),
          ("nlPort", 2))
    )


_SwNsPortType_Type.__name__ = "Integer32"
_SwNsPortType_Object = MibTableColumn
swNsPortType = _SwNsPortType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 3),
    _SwNsPortType_Type()
)
swNsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortType.setStatus("current")
_SwNsPortName_Type = FcWwn
_SwNsPortName_Object = MibTableColumn
swNsPortName = _SwNsPortName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 4),
    _SwNsPortName_Type()
)
swNsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortName.setStatus("current")


class _SwNsPortSymb_Type(OctetString):
    """Custom type swNsPortSymb based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwNsPortSymb_Type.__name__ = "OctetString"
_SwNsPortSymb_Object = MibTableColumn
swNsPortSymb = _SwNsPortSymb_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 5),
    _SwNsPortSymb_Type()
)
swNsPortSymb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortSymb.setStatus("current")
_SwNsNodeName_Type = FcWwn
_SwNsNodeName_Object = MibTableColumn
swNsNodeName = _SwNsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 6),
    _SwNsNodeName_Type()
)
swNsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsNodeName.setStatus("current")


class _SwNsNodeSymb_Type(OctetString):
    """Custom type swNsNodeSymb based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwNsNodeSymb_Type.__name__ = "OctetString"
_SwNsNodeSymb_Object = MibTableColumn
swNsNodeSymb = _SwNsNodeSymb_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 7),
    _SwNsNodeSymb_Type()
)
swNsNodeSymb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsNodeSymb.setStatus("current")


class _SwNsIPA_Type(OctetString):
    """Custom type swNsIPA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwNsIPA_Type.__name__ = "OctetString"
_SwNsIPA_Object = MibTableColumn
swNsIPA = _SwNsIPA_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 8),
    _SwNsIPA_Type()
)
swNsIPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsIPA.setStatus("current")


class _SwNsIpAddress_Type(OctetString):
    """Custom type swNsIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwNsIpAddress_Type.__name__ = "OctetString"
_SwNsIpAddress_Object = MibTableColumn
swNsIpAddress = _SwNsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 9),
    _SwNsIpAddress_Type()
)
swNsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsIpAddress.setStatus("current")


class _SwNsCos_Type(Integer32):
    """Custom type swNsCos based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("class-1", 2),
          ("class-1-2", 6),
          ("class-1-2-3", 14),
          ("class-1-3", 10),
          ("class-2", 4),
          ("class-2-3", 12),
          ("class-3", 8),
          ("class-F", 1),
          ("class-F-1", 3),
          ("class-F-1-2", 7),
          ("class-F-1-2-3", 15),
          ("class-F-1-3", 11),
          ("class-F-2", 5),
          ("class-F-2-3", 13),
          ("class-F-3", 9))
    )


_SwNsCos_Type.__name__ = "Integer32"
_SwNsCos_Object = MibTableColumn
swNsCos = _SwNsCos_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 10),
    _SwNsCos_Type()
)
swNsCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsCos.setStatus("current")


class _SwNsFc4_Type(OctetString):
    """Custom type swNsFc4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SwNsFc4_Type.__name__ = "OctetString"
_SwNsFc4_Object = MibTableColumn
swNsFc4 = _SwNsFc4_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 11),
    _SwNsFc4_Type()
)
swNsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsFc4.setStatus("current")


class _SwNsIpNxPort_Type(OctetString):
    """Custom type swNsIpNxPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwNsIpNxPort_Type.__name__ = "OctetString"
_SwNsIpNxPort_Object = MibTableColumn
swNsIpNxPort = _SwNsIpNxPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 12),
    _SwNsIpNxPort_Type()
)
swNsIpNxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsIpNxPort.setStatus("current")


class _SwNsWwn_Type(OctetString):
    """Custom type swNsWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwNsWwn_Type.__name__ = "OctetString"
_SwNsWwn_Object = MibTableColumn
swNsWwn = _SwNsWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 13),
    _SwNsWwn_Type()
)
swNsWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsWwn.setStatus("current")


class _SwNsHardAddr_Type(OctetString):
    """Custom type swNsHardAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SwNsHardAddr_Type.__name__ = "OctetString"
_SwNsHardAddr_Object = MibTableColumn
swNsHardAddr = _SwNsHardAddr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 14),
    _SwNsHardAddr_Type()
)
swNsHardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsHardAddr.setStatus("current")
_SwEvent_ObjectIdentity = ObjectIdentity
swEvent = _SwEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    swEvent.setStatus("current")


class _SwEventTrapLevel_Type(Integer32):
    """Custom type swEventTrapLevel based on Integer32"""
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
        *(("critical", 1),
          ("debug", 5),
          ("error", 2),
          ("informational", 4),
          ("none", 0),
          ("warning", 3))
    )


_SwEventTrapLevel_Type.__name__ = "Integer32"
_SwEventTrapLevel_Object = MibScalar
swEventTrapLevel = _SwEventTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 1),
    _SwEventTrapLevel_Type()
)
swEventTrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEventTrapLevel.setStatus("deprecated")


class _SwEventNumEntries_Type(Integer32):
    """Custom type swEventNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventNumEntries_Type.__name__ = "Integer32"
_SwEventNumEntries_Object = MibScalar
swEventNumEntries = _SwEventNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 4),
    _SwEventNumEntries_Type()
)
swEventNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventNumEntries.setStatus("current")
_SwEventTable_Object = MibTable
swEventTable = _SwEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    swEventTable.setStatus("current")
_SwEventEntry_Object = MibTableRow
swEventEntry = _SwEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1)
)
swEventEntry.setIndexNames(
    (0, "SW-MIB", "swEventIndex"),
)
if mibBuilder.loadTexts:
    swEventEntry.setStatus("current")


class _SwEventIndex_Type(Integer32):
    """Custom type swEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventIndex_Type.__name__ = "Integer32"
_SwEventIndex_Object = MibTableColumn
swEventIndex = _SwEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 1),
    _SwEventIndex_Type()
)
swEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventIndex.setStatus("current")


class _SwEventTimeInfo_Type(DisplayString):
    """Custom type swEventTimeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwEventTimeInfo_Type.__name__ = "DisplayString"
_SwEventTimeInfo_Object = MibTableColumn
swEventTimeInfo = _SwEventTimeInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 2),
    _SwEventTimeInfo_Type()
)
swEventTimeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventTimeInfo.setStatus("current")


class _SwEventLevel_Type(Integer32):
    """Custom type swEventLevel based on Integer32"""
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
        *(("critical", 1),
          ("debug", 5),
          ("error", 2),
          ("informational", 4),
          ("warning", 3))
    )


_SwEventLevel_Type.__name__ = "Integer32"
_SwEventLevel_Object = MibTableColumn
swEventLevel = _SwEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 3),
    _SwEventLevel_Type()
)
swEventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventLevel.setStatus("current")


class _SwEventRepeatCount_Type(Integer32):
    """Custom type swEventRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventRepeatCount_Type.__name__ = "Integer32"
_SwEventRepeatCount_Object = MibTableColumn
swEventRepeatCount = _SwEventRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 4),
    _SwEventRepeatCount_Type()
)
swEventRepeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventRepeatCount.setStatus("current")
_SwEventDescr_Type = DisplayString
_SwEventDescr_Object = MibTableColumn
swEventDescr = _SwEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 5),
    _SwEventDescr_Type()
)
swEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventDescr.setStatus("current")


class _SwEventVfId_Type(Integer32):
    """Custom type swEventVfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwEventVfId_Type.__name__ = "Integer32"
_SwEventVfId_Object = MibTableColumn
swEventVfId = _SwEventVfId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 6),
    _SwEventVfId_Type()
)
swEventVfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventVfId.setStatus("current")
_SwFwSystem_ObjectIdentity = ObjectIdentity
swFwSystem = _SwFwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    swFwSystem.setStatus("current")
_SwFwFabricWatchLicense_Type = SwFwLicense
_SwFwFabricWatchLicense_Object = MibScalar
swFwFabricWatchLicense = _SwFwFabricWatchLicense_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 1),
    _SwFwFabricWatchLicense_Type()
)
swFwFabricWatchLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwFabricWatchLicense.setStatus("current")
_SwFwClassAreaTable_Object = MibTable
swFwClassAreaTable = _SwFwClassAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    swFwClassAreaTable.setStatus("current")
_SwFwClassAreaEntry_Object = MibTableRow
swFwClassAreaEntry = _SwFwClassAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1)
)
swFwClassAreaEntry.setIndexNames(
    (0, "SW-MIB", "swFwClassAreaIndex"),
)
if mibBuilder.loadTexts:
    swFwClassAreaEntry.setStatus("current")
_SwFwClassAreaIndex_Type = SwFwClassesAreas
_SwFwClassAreaIndex_Object = MibTableColumn
swFwClassAreaIndex = _SwFwClassAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 1),
    _SwFwClassAreaIndex_Type()
)
swFwClassAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwClassAreaIndex.setStatus("current")
_SwFwWriteThVals_Type = SwFwWriteVals
_SwFwWriteThVals_Object = MibTableColumn
swFwWriteThVals = _SwFwWriteThVals_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 2),
    _SwFwWriteThVals_Type()
)
swFwWriteThVals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwWriteThVals.setStatus("current")
_SwFwDefaultUnit_Type = DisplayString
_SwFwDefaultUnit_Object = MibTableColumn
swFwDefaultUnit = _SwFwDefaultUnit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 3),
    _SwFwDefaultUnit_Type()
)
swFwDefaultUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultUnit.setStatus("current")
_SwFwDefaultTimebase_Type = SwFwTimebase
_SwFwDefaultTimebase_Object = MibTableColumn
swFwDefaultTimebase = _SwFwDefaultTimebase_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 4),
    _SwFwDefaultTimebase_Type()
)
swFwDefaultTimebase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultTimebase.setStatus("current")


class _SwFwDefaultLow_Type(Integer32):
    """Custom type swFwDefaultLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwDefaultLow_Type.__name__ = "Integer32"
_SwFwDefaultLow_Object = MibTableColumn
swFwDefaultLow = _SwFwDefaultLow_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 5),
    _SwFwDefaultLow_Type()
)
swFwDefaultLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultLow.setStatus("current")


class _SwFwDefaultHigh_Type(Integer32):
    """Custom type swFwDefaultHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwDefaultHigh_Type.__name__ = "Integer32"
_SwFwDefaultHigh_Object = MibTableColumn
swFwDefaultHigh = _SwFwDefaultHigh_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 6),
    _SwFwDefaultHigh_Type()
)
swFwDefaultHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultHigh.setStatus("current")


class _SwFwDefaultBufSize_Type(Integer32):
    """Custom type swFwDefaultBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwDefaultBufSize_Type.__name__ = "Integer32"
_SwFwDefaultBufSize_Object = MibTableColumn
swFwDefaultBufSize = _SwFwDefaultBufSize_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 7),
    _SwFwDefaultBufSize_Type()
)
swFwDefaultBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultBufSize.setStatus("current")
_SwFwCustUnit_Type = DisplayString
_SwFwCustUnit_Object = MibTableColumn
swFwCustUnit = _SwFwCustUnit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 8),
    _SwFwCustUnit_Type()
)
swFwCustUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwCustUnit.setStatus("current")
_SwFwCustTimebase_Type = SwFwTimebase
_SwFwCustTimebase_Object = MibTableColumn
swFwCustTimebase = _SwFwCustTimebase_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 9),
    _SwFwCustTimebase_Type()
)
swFwCustTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustTimebase.setStatus("current")


class _SwFwCustLow_Type(Integer32):
    """Custom type swFwCustLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwCustLow_Type.__name__ = "Integer32"
_SwFwCustLow_Object = MibTableColumn
swFwCustLow = _SwFwCustLow_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 10),
    _SwFwCustLow_Type()
)
swFwCustLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustLow.setStatus("current")


class _SwFwCustHigh_Type(Integer32):
    """Custom type swFwCustHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwCustHigh_Type.__name__ = "Integer32"
_SwFwCustHigh_Object = MibTableColumn
swFwCustHigh = _SwFwCustHigh_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 11),
    _SwFwCustHigh_Type()
)
swFwCustHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustHigh.setStatus("current")


class _SwFwCustBufSize_Type(Integer32):
    """Custom type swFwCustBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwCustBufSize_Type.__name__ = "Integer32"
_SwFwCustBufSize_Object = MibTableColumn
swFwCustBufSize = _SwFwCustBufSize_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 12),
    _SwFwCustBufSize_Type()
)
swFwCustBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustBufSize.setStatus("current")
_SwFwThLevel_Type = SwFwLevels
_SwFwThLevel_Object = MibTableColumn
swFwThLevel = _SwFwThLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 13),
    _SwFwThLevel_Type()
)
swFwThLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwThLevel.setStatus("current")
_SwFwWriteActVals_Type = SwFwWriteVals
_SwFwWriteActVals_Object = MibTableColumn
swFwWriteActVals = _SwFwWriteActVals_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 14),
    _SwFwWriteActVals_Type()
)
swFwWriteActVals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwWriteActVals.setStatus("current")
_SwFwDefaultChangedActs_Type = SwFwActs
_SwFwDefaultChangedActs_Object = MibTableColumn
swFwDefaultChangedActs = _SwFwDefaultChangedActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 15),
    _SwFwDefaultChangedActs_Type()
)
swFwDefaultChangedActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultChangedActs.setStatus("current")
_SwFwDefaultExceededActs_Type = SwFwActs
_SwFwDefaultExceededActs_Object = MibTableColumn
swFwDefaultExceededActs = _SwFwDefaultExceededActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 16),
    _SwFwDefaultExceededActs_Type()
)
swFwDefaultExceededActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultExceededActs.setStatus("current")
_SwFwDefaultBelowActs_Type = SwFwActs
_SwFwDefaultBelowActs_Object = MibTableColumn
swFwDefaultBelowActs = _SwFwDefaultBelowActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 17),
    _SwFwDefaultBelowActs_Type()
)
swFwDefaultBelowActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultBelowActs.setStatus("current")
_SwFwDefaultAboveActs_Type = SwFwActs
_SwFwDefaultAboveActs_Object = MibTableColumn
swFwDefaultAboveActs = _SwFwDefaultAboveActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 18),
    _SwFwDefaultAboveActs_Type()
)
swFwDefaultAboveActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultAboveActs.setStatus("current")
_SwFwDefaultInBetweenActs_Type = SwFwActs
_SwFwDefaultInBetweenActs_Object = MibTableColumn
swFwDefaultInBetweenActs = _SwFwDefaultInBetweenActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 19),
    _SwFwDefaultInBetweenActs_Type()
)
swFwDefaultInBetweenActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultInBetweenActs.setStatus("current")
_SwFwCustChangedActs_Type = SwFwActs
_SwFwCustChangedActs_Object = MibTableColumn
swFwCustChangedActs = _SwFwCustChangedActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 20),
    _SwFwCustChangedActs_Type()
)
swFwCustChangedActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustChangedActs.setStatus("current")
_SwFwCustExceededActs_Type = SwFwActs
_SwFwCustExceededActs_Object = MibTableColumn
swFwCustExceededActs = _SwFwCustExceededActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 21),
    _SwFwCustExceededActs_Type()
)
swFwCustExceededActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustExceededActs.setStatus("current")
_SwFwCustBelowActs_Type = SwFwActs
_SwFwCustBelowActs_Object = MibTableColumn
swFwCustBelowActs = _SwFwCustBelowActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 22),
    _SwFwCustBelowActs_Type()
)
swFwCustBelowActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustBelowActs.setStatus("current")
_SwFwCustAboveActs_Type = SwFwActs
_SwFwCustAboveActs_Object = MibTableColumn
swFwCustAboveActs = _SwFwCustAboveActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 23),
    _SwFwCustAboveActs_Type()
)
swFwCustAboveActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustAboveActs.setStatus("current")
_SwFwCustInBetweenActs_Type = SwFwActs
_SwFwCustInBetweenActs_Object = MibTableColumn
swFwCustInBetweenActs = _SwFwCustInBetweenActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 24),
    _SwFwCustInBetweenActs_Type()
)
swFwCustInBetweenActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustInBetweenActs.setStatus("current")
_SwFwValidActs_Type = SwFwActs
_SwFwValidActs_Object = MibTableColumn
swFwValidActs = _SwFwValidActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 25),
    _SwFwValidActs_Type()
)
swFwValidActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwValidActs.setStatus("current")
_SwFwActLevel_Type = SwFwLevels
_SwFwActLevel_Object = MibTableColumn
swFwActLevel = _SwFwActLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 26),
    _SwFwActLevel_Type()
)
swFwActLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwActLevel.setStatus("current")
_SwFwThresholdTable_Object = MibTable
swFwThresholdTable = _SwFwThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    swFwThresholdTable.setStatus("current")
_SwFwThresholdEntry_Object = MibTableRow
swFwThresholdEntry = _SwFwThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1)
)
swFwThresholdEntry.setIndexNames(
    (0, "SW-MIB", "swFwClassAreaIndex"),
    (0, "SW-MIB", "swFwThresholdIndex"),
)
if mibBuilder.loadTexts:
    swFwThresholdEntry.setStatus("current")


class _SwFwThresholdIndex_Type(Integer32):
    """Custom type swFwThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwThresholdIndex_Type.__name__ = "Integer32"
_SwFwThresholdIndex_Object = MibTableColumn
swFwThresholdIndex = _SwFwThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 1),
    _SwFwThresholdIndex_Type()
)
swFwThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwThresholdIndex.setStatus("current")
_SwFwStatus_Type = SwFwStatus
_SwFwStatus_Object = MibTableColumn
swFwStatus = _SwFwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 2),
    _SwFwStatus_Type()
)
swFwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwStatus.setStatus("current")


class _SwFwName_Type(DisplayString):
    """Custom type swFwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwFwName_Type.__name__ = "DisplayString"
_SwFwName_Object = MibTableColumn
swFwName = _SwFwName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 3),
    _SwFwName_Type()
)
swFwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwName.setStatus("current")


class _SwFwLabel_Type(DisplayString):
    """Custom type swFwLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SwFwLabel_Type.__name__ = "DisplayString"
_SwFwLabel_Object = MibTableColumn
swFwLabel = _SwFwLabel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 4),
    _SwFwLabel_Type()
)
swFwLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLabel.setStatus("current")


class _SwFwCurVal_Type(Integer32):
    """Custom type swFwCurVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwCurVal_Type.__name__ = "Integer32"
_SwFwCurVal_Object = MibTableColumn
swFwCurVal = _SwFwCurVal_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 5),
    _SwFwCurVal_Type()
)
swFwCurVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwCurVal.setStatus("current")
_SwFwLastEvent_Type = SwFwEvent
_SwFwLastEvent_Object = MibTableColumn
swFwLastEvent = _SwFwLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 6),
    _SwFwLastEvent_Type()
)
swFwLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastEvent.setStatus("current")


class _SwFwLastEventVal_Type(Integer32):
    """Custom type swFwLastEventVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwLastEventVal_Type.__name__ = "Integer32"
_SwFwLastEventVal_Object = MibTableColumn
swFwLastEventVal = _SwFwLastEventVal_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 7),
    _SwFwLastEventVal_Type()
)
swFwLastEventVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastEventVal.setStatus("current")


class _SwFwLastEventTime_Type(DisplayString):
    """Custom type swFwLastEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwFwLastEventTime_Type.__name__ = "DisplayString"
_SwFwLastEventTime_Object = MibTableColumn
swFwLastEventTime = _SwFwLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 8),
    _SwFwLastEventTime_Type()
)
swFwLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastEventTime.setStatus("current")
_SwFwLastState_Type = SwFwState
_SwFwLastState_Object = MibTableColumn
swFwLastState = _SwFwLastState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 9),
    _SwFwLastState_Type()
)
swFwLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastState.setStatus("current")
_SwFwBehaviorType_Type = SwFwBehavior
_SwFwBehaviorType_Object = MibTableColumn
swFwBehaviorType = _SwFwBehaviorType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 10),
    _SwFwBehaviorType_Type()
)
swFwBehaviorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwBehaviorType.setStatus("current")


class _SwFwBehaviorInt_Type(Integer32):
    """Custom type swFwBehaviorInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwBehaviorInt_Type.__name__ = "Integer32"
_SwFwBehaviorInt_Object = MibTableColumn
swFwBehaviorInt = _SwFwBehaviorInt_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 11),
    _SwFwBehaviorInt_Type()
)
swFwBehaviorInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwBehaviorInt.setStatus("current")
_SwFwLastSeverityLevel_Type = SwSevType
_SwFwLastSeverityLevel_Object = MibTableColumn
swFwLastSeverityLevel = _SwFwLastSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 12),
    _SwFwLastSeverityLevel_Type()
)
swFwLastSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastSeverityLevel.setStatus("current")
_SwEndDevice_ObjectIdentity = ObjectIdentity
swEndDevice = _SwEndDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21)
)
if mibBuilder.loadTexts:
    swEndDevice.setStatus("current")
_SwEndDeviceRlsTable_Object = MibTable
swEndDeviceRlsTable = _SwEndDeviceRlsTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1)
)
if mibBuilder.loadTexts:
    swEndDeviceRlsTable.setStatus("current")
_SwEndDeviceRlsEntry_Object = MibTableRow
swEndDeviceRlsEntry = _SwEndDeviceRlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1)
)
swEndDeviceRlsEntry.setIndexNames(
    (0, "SW-MIB", "swEndDevicePort"),
    (0, "SW-MIB", "swEndDeviceAlpa"),
)
if mibBuilder.loadTexts:
    swEndDeviceRlsEntry.setStatus("current")


class _SwEndDevicePort_Type(Integer32):
    """Custom type swEndDevicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDevicePort_Type.__name__ = "Integer32"
_SwEndDevicePort_Object = MibTableColumn
swEndDevicePort = _SwEndDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 1),
    _SwEndDevicePort_Type()
)
swEndDevicePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEndDevicePort.setStatus("current")


class _SwEndDeviceAlpa_Type(Integer32):
    """Custom type swEndDeviceAlpa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDeviceAlpa_Type.__name__ = "Integer32"
_SwEndDeviceAlpa_Object = MibTableColumn
swEndDeviceAlpa = _SwEndDeviceAlpa_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 2),
    _SwEndDeviceAlpa_Type()
)
swEndDeviceAlpa.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEndDeviceAlpa.setStatus("current")


class _SwEndDevicePortID_Type(OctetString):
    """Custom type swEndDevicePortID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwEndDevicePortID_Type.__name__ = "OctetString"
_SwEndDevicePortID_Object = MibTableColumn
swEndDevicePortID = _SwEndDevicePortID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 3),
    _SwEndDevicePortID_Type()
)
swEndDevicePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDevicePortID.setStatus("current")
_SwEndDeviceLinkFailure_Type = Counter32
_SwEndDeviceLinkFailure_Object = MibTableColumn
swEndDeviceLinkFailure = _SwEndDeviceLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 4),
    _SwEndDeviceLinkFailure_Type()
)
swEndDeviceLinkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceLinkFailure.setStatus("current")
_SwEndDeviceSyncLoss_Type = Counter32
_SwEndDeviceSyncLoss_Object = MibTableColumn
swEndDeviceSyncLoss = _SwEndDeviceSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 5),
    _SwEndDeviceSyncLoss_Type()
)
swEndDeviceSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceSyncLoss.setStatus("current")
_SwEndDeviceSigLoss_Type = Counter32
_SwEndDeviceSigLoss_Object = MibTableColumn
swEndDeviceSigLoss = _SwEndDeviceSigLoss_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 6),
    _SwEndDeviceSigLoss_Type()
)
swEndDeviceSigLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceSigLoss.setStatus("current")
_SwEndDeviceProtoErr_Type = Counter32
_SwEndDeviceProtoErr_Object = MibTableColumn
swEndDeviceProtoErr = _SwEndDeviceProtoErr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 7),
    _SwEndDeviceProtoErr_Type()
)
swEndDeviceProtoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceProtoErr.setStatus("current")
_SwEndDeviceInvalidWord_Type = Counter32
_SwEndDeviceInvalidWord_Object = MibTableColumn
swEndDeviceInvalidWord = _SwEndDeviceInvalidWord_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 8),
    _SwEndDeviceInvalidWord_Type()
)
swEndDeviceInvalidWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceInvalidWord.setStatus("current")
_SwEndDeviceInvalidCRC_Type = Counter32
_SwEndDeviceInvalidCRC_Object = MibTableColumn
swEndDeviceInvalidCRC = _SwEndDeviceInvalidCRC_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 9),
    _SwEndDeviceInvalidCRC_Type()
)
swEndDeviceInvalidCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceInvalidCRC.setStatus("current")
_SwGroup_ObjectIdentity = ObjectIdentity
swGroup = _SwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    swGroup.setStatus("obsolete")
_SwGroupTable_Object = MibTable
swGroupTable = _SwGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1)
)
if mibBuilder.loadTexts:
    swGroupTable.setStatus("obsolete")
_SwGroupEntry_Object = MibTableRow
swGroupEntry = _SwGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1, 1)
)
swGroupEntry.setIndexNames(
    (0, "SW-MIB", "swGroupIndex"),
)
if mibBuilder.loadTexts:
    swGroupEntry.setStatus("obsolete")


class _SwGroupIndex_Type(Integer32):
    """Custom type swGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwGroupIndex_Type.__name__ = "Integer32"
_SwGroupIndex_Object = MibTableColumn
swGroupIndex = _SwGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1, 1, 1),
    _SwGroupIndex_Type()
)
swGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupIndex.setStatus("obsolete")


class _SwGroupName_Type(OctetString):
    """Custom type swGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwGroupName_Type.__name__ = "OctetString"
_SwGroupName_Object = MibTableColumn
swGroupName = _SwGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1, 1, 2),
    _SwGroupName_Type()
)
swGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupName.setStatus("obsolete")


class _SwGroupType_Type(OctetString):
    """Custom type swGroupType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwGroupType_Type.__name__ = "OctetString"
_SwGroupType_Object = MibTableColumn
swGroupType = _SwGroupType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1, 1, 3),
    _SwGroupType_Type()
)
swGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupType.setStatus("obsolete")
_SwGroupMemTable_Object = MibTable
swGroupMemTable = _SwGroupMemTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2)
)
if mibBuilder.loadTexts:
    swGroupMemTable.setStatus("obsolete")
_SwGroupMemEntry_Object = MibTableRow
swGroupMemEntry = _SwGroupMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2, 1)
)
swGroupMemEntry.setIndexNames(
    (0, "SW-MIB", "swGroupId"),
    (0, "SW-MIB", "swGroupMemWwn"),
)
if mibBuilder.loadTexts:
    swGroupMemEntry.setStatus("obsolete")


class _SwGroupId_Type(Integer32):
    """Custom type swGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwGroupId_Type.__name__ = "Integer32"
_SwGroupId_Object = MibTableColumn
swGroupId = _SwGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2, 1, 1),
    _SwGroupId_Type()
)
swGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupId.setStatus("obsolete")
_SwGroupMemWwn_Type = FcWwn
_SwGroupMemWwn_Object = MibTableColumn
swGroupMemWwn = _SwGroupMemWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2, 1, 2),
    _SwGroupMemWwn_Type()
)
swGroupMemWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupMemWwn.setStatus("obsolete")


class _SwGroupMemPos_Type(Integer32):
    """Custom type swGroupMemPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwGroupMemPos_Type.__name__ = "Integer32"
_SwGroupMemPos_Object = MibTableColumn
swGroupMemPos = _SwGroupMemPos_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2, 1, 3),
    _SwGroupMemPos_Type()
)
swGroupMemPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupMemPos.setStatus("obsolete")
_SwBlmPerfMnt_ObjectIdentity = ObjectIdentity
swBlmPerfMnt = _SwBlmPerfMnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23)
)
if mibBuilder.loadTexts:
    swBlmPerfMnt.setStatus("current")
_SwBlmPerfALPAMntTable_Object = MibTable
swBlmPerfALPAMntTable = _SwBlmPerfALPAMntTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1)
)
if mibBuilder.loadTexts:
    swBlmPerfALPAMntTable.setStatus("current")
_SwBlmPerfALPAMntEntry_Object = MibTableRow
swBlmPerfALPAMntEntry = _SwBlmPerfALPAMntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1)
)
swBlmPerfALPAMntEntry.setIndexNames(
    (0, "SW-MIB", "swBlmPerfAlpaPort"),
    (0, "SW-MIB", "swBlmPerfAlpaIndx"),
)
if mibBuilder.loadTexts:
    swBlmPerfALPAMntEntry.setStatus("current")
_SwBlmPerfAlpaPort_Type = SwPortIndex
_SwBlmPerfAlpaPort_Object = MibTableColumn
swBlmPerfAlpaPort = _SwBlmPerfAlpaPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1, 1),
    _SwBlmPerfAlpaPort_Type()
)
swBlmPerfAlpaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfAlpaPort.setStatus("current")


class _SwBlmPerfAlpaIndx_Type(Integer32):
    """Custom type swBlmPerfAlpaIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_SwBlmPerfAlpaIndx_Type.__name__ = "Integer32"
_SwBlmPerfAlpaIndx_Object = MibTableColumn
swBlmPerfAlpaIndx = _SwBlmPerfAlpaIndx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1, 2),
    _SwBlmPerfAlpaIndx_Type()
)
swBlmPerfAlpaIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfAlpaIndx.setStatus("current")


class _SwBlmPerfAlpa_Type(Integer32):
    """Custom type swBlmPerfAlpa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwBlmPerfAlpa_Type.__name__ = "Integer32"
_SwBlmPerfAlpa_Object = MibTableColumn
swBlmPerfAlpa = _SwBlmPerfAlpa_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1, 3),
    _SwBlmPerfAlpa_Type()
)
swBlmPerfAlpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfAlpa.setStatus("current")


class _SwBlmPerfAlpaCRCCnt_Type(OctetString):
    """Custom type swBlmPerfAlpaCRCCnt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwBlmPerfAlpaCRCCnt_Type.__name__ = "OctetString"
_SwBlmPerfAlpaCRCCnt_Object = MibTableColumn
swBlmPerfAlpaCRCCnt = _SwBlmPerfAlpaCRCCnt_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1, 4),
    _SwBlmPerfAlpaCRCCnt_Type()
)
swBlmPerfAlpaCRCCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfAlpaCRCCnt.setStatus("current")
_SwBlmPerfEEMntTable_Object = MibTable
swBlmPerfEEMntTable = _SwBlmPerfEEMntTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2)
)
if mibBuilder.loadTexts:
    swBlmPerfEEMntTable.setStatus("current")
_SwBlmPerfEEMntEntry_Object = MibTableRow
swBlmPerfEEMntEntry = _SwBlmPerfEEMntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1)
)
swBlmPerfEEMntEntry.setIndexNames(
    (0, "SW-MIB", "swBlmPerfEEPort"),
    (0, "SW-MIB", "swBlmPerfEERefKey"),
)
if mibBuilder.loadTexts:
    swBlmPerfEEMntEntry.setStatus("current")
_SwBlmPerfEEPort_Type = SwPortIndex
_SwBlmPerfEEPort_Object = MibTableColumn
swBlmPerfEEPort = _SwBlmPerfEEPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 1),
    _SwBlmPerfEEPort_Type()
)
swBlmPerfEEPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEEPort.setStatus("current")


class _SwBlmPerfEERefKey_Type(Integer32):
    """Custom type swBlmPerfEERefKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SwBlmPerfEERefKey_Type.__name__ = "Integer32"
_SwBlmPerfEERefKey_Object = MibTableColumn
swBlmPerfEERefKey = _SwBlmPerfEERefKey_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 2),
    _SwBlmPerfEERefKey_Type()
)
swBlmPerfEERefKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEERefKey.setStatus("current")


class _SwBlmPerfEECRC_Type(OctetString):
    """Custom type swBlmPerfEECRC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwBlmPerfEECRC_Type.__name__ = "OctetString"
_SwBlmPerfEECRC_Object = MibTableColumn
swBlmPerfEECRC = _SwBlmPerfEECRC_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 3),
    _SwBlmPerfEECRC_Type()
)
swBlmPerfEECRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEECRC.setStatus("current")


class _SwBlmPerfEEFCWRx_Type(OctetString):
    """Custom type swBlmPerfEEFCWRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwBlmPerfEEFCWRx_Type.__name__ = "OctetString"
_SwBlmPerfEEFCWRx_Object = MibTableColumn
swBlmPerfEEFCWRx = _SwBlmPerfEEFCWRx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 4),
    _SwBlmPerfEEFCWRx_Type()
)
swBlmPerfEEFCWRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEEFCWRx.setStatus("current")


class _SwBlmPerfEEFCWTx_Type(OctetString):
    """Custom type swBlmPerfEEFCWTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwBlmPerfEEFCWTx_Type.__name__ = "OctetString"
_SwBlmPerfEEFCWTx_Object = MibTableColumn
swBlmPerfEEFCWTx = _SwBlmPerfEEFCWTx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 5),
    _SwBlmPerfEEFCWTx_Type()
)
swBlmPerfEEFCWTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEEFCWTx.setStatus("current")


class _SwBlmPerfEESid_Type(Integer32):
    """Custom type swBlmPerfEESid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwBlmPerfEESid_Type.__name__ = "Integer32"
_SwBlmPerfEESid_Object = MibTableColumn
swBlmPerfEESid = _SwBlmPerfEESid_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 6),
    _SwBlmPerfEESid_Type()
)
swBlmPerfEESid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEESid.setStatus("current")


class _SwBlmPerfEEDid_Type(Integer32):
    """Custom type swBlmPerfEEDid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwBlmPerfEEDid_Type.__name__ = "Integer32"
_SwBlmPerfEEDid_Object = MibTableColumn
swBlmPerfEEDid = _SwBlmPerfEEDid_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 7),
    _SwBlmPerfEEDid_Type()
)
swBlmPerfEEDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEEDid.setStatus("current")
_SwBlmPerfFltMntTable_Object = MibTable
swBlmPerfFltMntTable = _SwBlmPerfFltMntTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3)
)
if mibBuilder.loadTexts:
    swBlmPerfFltMntTable.setStatus("current")
_SwBlmPerfFltMntEntry_Object = MibTableRow
swBlmPerfFltMntEntry = _SwBlmPerfFltMntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1)
)
swBlmPerfFltMntEntry.setIndexNames(
    (0, "SW-MIB", "swBlmPerfFltPort"),
    (0, "SW-MIB", "swBlmPerfFltRefkey"),
)
if mibBuilder.loadTexts:
    swBlmPerfFltMntEntry.setStatus("current")
_SwBlmPerfFltPort_Type = SwPortIndex
_SwBlmPerfFltPort_Object = MibTableColumn
swBlmPerfFltPort = _SwBlmPerfFltPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1, 1),
    _SwBlmPerfFltPort_Type()
)
swBlmPerfFltPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfFltPort.setStatus("current")


class _SwBlmPerfFltRefkey_Type(Integer32):
    """Custom type swBlmPerfFltRefkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SwBlmPerfFltRefkey_Type.__name__ = "Integer32"
_SwBlmPerfFltRefkey_Object = MibTableColumn
swBlmPerfFltRefkey = _SwBlmPerfFltRefkey_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1, 2),
    _SwBlmPerfFltRefkey_Type()
)
swBlmPerfFltRefkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfFltRefkey.setStatus("current")


class _SwBlmPerfFltCnt_Type(OctetString):
    """Custom type swBlmPerfFltCnt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwBlmPerfFltCnt_Type.__name__ = "OctetString"
_SwBlmPerfFltCnt_Object = MibTableColumn
swBlmPerfFltCnt = _SwBlmPerfFltCnt_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1, 3),
    _SwBlmPerfFltCnt_Type()
)
swBlmPerfFltCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfFltCnt.setStatus("current")


class _SwBlmPerfFltAlias_Type(DisplayString):
    """Custom type swBlmPerfFltAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBlmPerfFltAlias_Type.__name__ = "DisplayString"
_SwBlmPerfFltAlias_Object = MibTableColumn
swBlmPerfFltAlias = _SwBlmPerfFltAlias_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1, 4),
    _SwBlmPerfFltAlias_Type()
)
swBlmPerfFltAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfFltAlias.setStatus("current")
_SwTrunk_ObjectIdentity = ObjectIdentity
swTrunk = _SwTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24)
)
if mibBuilder.loadTexts:
    swTrunk.setStatus("current")


class _SwSwitchTrunkable_Type(Integer32):
    """Custom type swSwitchTrunkable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 8))
    )


_SwSwitchTrunkable_Type.__name__ = "Integer32"
_SwSwitchTrunkable_Object = MibScalar
swSwitchTrunkable = _SwSwitchTrunkable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 1),
    _SwSwitchTrunkable_Type()
)
swSwitchTrunkable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSwitchTrunkable.setStatus("current")
_SwTrunkTable_Object = MibTable
swTrunkTable = _SwTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2)
)
if mibBuilder.loadTexts:
    swTrunkTable.setStatus("current")
_SwTrunkEntry_Object = MibTableRow
swTrunkEntry = _SwTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1)
)
swTrunkEntry.setIndexNames(
    (0, "SW-MIB", "swTrunkPortIndex"),
)
if mibBuilder.loadTexts:
    swTrunkEntry.setStatus("current")
_SwTrunkPortIndex_Type = SwPortIndex
_SwTrunkPortIndex_Object = MibTableColumn
swTrunkPortIndex = _SwTrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1, 1),
    _SwTrunkPortIndex_Type()
)
swTrunkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkPortIndex.setStatus("current")


class _SwTrunkGroupNumber_Type(Integer32):
    """Custom type swTrunkGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwTrunkGroupNumber_Type.__name__ = "Integer32"
_SwTrunkGroupNumber_Object = MibTableColumn
swTrunkGroupNumber = _SwTrunkGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1, 2),
    _SwTrunkGroupNumber_Type()
)
swTrunkGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGroupNumber.setStatus("current")
_SwTrunkMaster_Type = SwTrunkMaster
_SwTrunkMaster_Object = MibTableColumn
swTrunkMaster = _SwTrunkMaster_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1, 3),
    _SwTrunkMaster_Type()
)
swTrunkMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkMaster.setStatus("current")


class _SwPortTrunked_Type(Integer32):
    """Custom type swPortTrunked based on Integer32"""
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


_SwPortTrunked_Type.__name__ = "Integer32"
_SwPortTrunked_Object = MibTableColumn
swPortTrunked = _SwPortTrunked_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1, 4),
    _SwPortTrunked_Type()
)
swPortTrunked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunked.setStatus("current")
_SwTrunkGrpTable_Object = MibTable
swTrunkGrpTable = _SwTrunkGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3)
)
if mibBuilder.loadTexts:
    swTrunkGrpTable.setStatus("current")
_SwTrunkGrpEntry_Object = MibTableRow
swTrunkGrpEntry = _SwTrunkGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1)
)
swTrunkGrpEntry.setIndexNames(
    (0, "SW-MIB", "swTrunkGrpNumber"),
)
if mibBuilder.loadTexts:
    swTrunkGrpEntry.setStatus("current")


class _SwTrunkGrpNumber_Type(Integer32):
    """Custom type swTrunkGrpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwTrunkGrpNumber_Type.__name__ = "Integer32"
_SwTrunkGrpNumber_Object = MibTableColumn
swTrunkGrpNumber = _SwTrunkGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1, 1),
    _SwTrunkGrpNumber_Type()
)
swTrunkGrpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGrpNumber.setStatus("current")
_SwTrunkGrpMaster_Type = SwTrunkMaster
_SwTrunkGrpMaster_Object = MibTableColumn
swTrunkGrpMaster = _SwTrunkGrpMaster_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1, 2),
    _SwTrunkGrpMaster_Type()
)
swTrunkGrpMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGrpMaster.setStatus("current")


class _SwTrunkGrpTx_Type(OctetString):
    """Custom type swTrunkGrpTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwTrunkGrpTx_Type.__name__ = "OctetString"
_SwTrunkGrpTx_Object = MibTableColumn
swTrunkGrpTx = _SwTrunkGrpTx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1, 3),
    _SwTrunkGrpTx_Type()
)
swTrunkGrpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGrpTx.setStatus("current")


class _SwTrunkGrpRx_Type(OctetString):
    """Custom type swTrunkGrpRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwTrunkGrpRx_Type.__name__ = "OctetString"
_SwTrunkGrpRx_Object = MibTableColumn
swTrunkGrpRx = _SwTrunkGrpRx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1, 4),
    _SwTrunkGrpRx_Type()
)
swTrunkGrpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGrpRx.setStatus("current")
_SwTopTalker_ObjectIdentity = ObjectIdentity
swTopTalker = _SwTopTalker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25)
)
if mibBuilder.loadTexts:
    swTopTalker.setStatus("current")


class _SwTopTalkerMntMode_Type(Integer32):
    """Custom type swTopTalkerMntMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fabricmode", 1),
          ("portmode", 2))
    )


_SwTopTalkerMntMode_Type.__name__ = "Integer32"
_SwTopTalkerMntMode_Object = MibScalar
swTopTalkerMntMode = _SwTopTalkerMntMode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 1),
    _SwTopTalkerMntMode_Type()
)
swTopTalkerMntMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTopTalkerMntMode.setStatus("current")


class _SwTopTalkerMntNumEntries_Type(Integer32):
    """Custom type swTopTalkerMntNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwTopTalkerMntNumEntries_Type.__name__ = "Integer32"
_SwTopTalkerMntNumEntries_Object = MibScalar
swTopTalkerMntNumEntries = _SwTopTalkerMntNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 2),
    _SwTopTalkerMntNumEntries_Type()
)
swTopTalkerMntNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTopTalkerMntNumEntries.setStatus("current")
_SwTopTalkerMntTable_Object = MibTable
swTopTalkerMntTable = _SwTopTalkerMntTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 3)
)
if mibBuilder.loadTexts:
    swTopTalkerMntTable.setStatus("current")
_SwTopTalkerMntEntry_Object = MibTableRow
swTopTalkerMntEntry = _SwTopTalkerMntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 3, 1)
)
swTopTalkerMntEntry.setIndexNames(
    (0, "SW-MIB", "swTopTalkerMntIndex"),
)
if mibBuilder.loadTexts:
    swTopTalkerMntEntry.setStatus("current")


class _SwTopTalkerMntIndex_Type(Integer32):
    """Custom type swTopTalkerMntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwTopTalkerMntIndex_Type.__name__ = "Integer32"
_SwTopTalkerMntIndex_Object = MibTableColumn
swTopTalkerMntIndex = _SwTopTalkerMntIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 3, 1, 1),
    _SwTopTalkerMntIndex_Type()
)
swTopTalkerMntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTopTalkerMntIndex.setStatus("current")


class _SwTopTalkerMntPort_Type(Integer32):
    """Custom type swTopTalkerMntPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwTopTalkerMntPort_Type.__name__ = "Integer32"
_SwTopTalkerMntPort_Object = MibTableColumn
swTopTalkerMntPort = _SwTopTalkerMntPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 3, 1, 2),
    _SwTopTalkerMntPort_Type()
)
swTopTalkerMntPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTopTalkerMntPort.setStatus("current")


class _SwTopTalkerMntSpid_Type(Integer32):
    """Custom type swTopTalkerMntSpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwTopTalkerMntSpid_Type.__name__ = "Integer32"
_SwTopTalkerMntSpid_Object = MibTableColumn
swTopTalkerMntSpid = _SwTopTalkerMntSpid_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 3, 1, 3),
    _SwTopTalkerMntSpid_Type()
)
swTopTalkerMntSpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTopTalkerMntSpid.setStatus("current")


class _SwTopTalkerMntDpid_Type(Integer32):
    """Custom type swTopTalkerMntDpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwTopTalkerMntDpid_Type.__name__ = "Integer32"
_SwTopTalkerMntDpid_Object = MibTableColumn
swTopTalkerMntDpid = _SwTopTalkerMntDpid_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 3, 1, 4),
    _SwTopTalkerMntDpid_Type()
)
swTopTalkerMntDpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTopTalkerMntDpid.setStatus("current")


class _SwTopTalkerMntflow_Type(Integer32):
    """Custom type swTopTalkerMntflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwTopTalkerMntflow_Type.__name__ = "Integer32"
_SwTopTalkerMntflow_Object = MibTableColumn
swTopTalkerMntflow = _SwTopTalkerMntflow_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 3, 1, 5),
    _SwTopTalkerMntflow_Type()
)
swTopTalkerMntflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTopTalkerMntflow.setStatus("current")
_SwTopTalkerMntSwwn_Type = FcWwn
_SwTopTalkerMntSwwn_Object = MibTableColumn
swTopTalkerMntSwwn = _SwTopTalkerMntSwwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 3, 1, 6),
    _SwTopTalkerMntSwwn_Type()
)
swTopTalkerMntSwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTopTalkerMntSwwn.setStatus("current")
_SwTopTalkerMntDwwn_Type = FcWwn
_SwTopTalkerMntDwwn_Object = MibTableColumn
swTopTalkerMntDwwn = _SwTopTalkerMntDwwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 25, 3, 1, 7),
    _SwTopTalkerMntDwwn_Type()
)
swTopTalkerMntDwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTopTalkerMntDwwn.setStatus("current")
_SwCpuOrMemoryUsage_ObjectIdentity = ObjectIdentity
swCpuOrMemoryUsage = _SwCpuOrMemoryUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26)
)
if mibBuilder.loadTexts:
    swCpuOrMemoryUsage.setStatus("current")


class _SwCpuUsage_Type(Integer32):
    """Custom type swCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwCpuUsage_Type.__name__ = "Integer32"
_SwCpuUsage_Object = MibScalar
swCpuUsage = _SwCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 1),
    _SwCpuUsage_Type()
)
swCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuUsage.setStatus("current")


class _SwCpuNoOfRetries_Type(Integer32):
    """Custom type swCpuNoOfRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SwCpuNoOfRetries_Type.__name__ = "Integer32"
_SwCpuNoOfRetries_Object = MibScalar
swCpuNoOfRetries = _SwCpuNoOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 2),
    _SwCpuNoOfRetries_Type()
)
swCpuNoOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuNoOfRetries.setStatus("current")


class _SwCpuUsageLimit_Type(Integer32):
    """Custom type swCpuUsageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SwCpuUsageLimit_Type.__name__ = "Integer32"
_SwCpuUsageLimit_Object = MibScalar
swCpuUsageLimit = _SwCpuUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 3),
    _SwCpuUsageLimit_Type()
)
swCpuUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuUsageLimit.setStatus("current")


class _SwCpuPollingInterval_Type(Integer32):
    """Custom type swCpuPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SwCpuPollingInterval_Type.__name__ = "Integer32"
_SwCpuPollingInterval_Object = MibScalar
swCpuPollingInterval = _SwCpuPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 4),
    _SwCpuPollingInterval_Type()
)
swCpuPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    swCpuPollingInterval.setUnits("seconds")


class _SwCpuAction_Type(Integer32):
    """Custom type swCpuAction based on Integer32"""
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
        *(("none", 0),
          ("raslog", 1),
          ("raslogandSnmp", 3),
          ("snmp", 2))
    )


_SwCpuAction_Type.__name__ = "Integer32"
_SwCpuAction_Object = MibScalar
swCpuAction = _SwCpuAction_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 5),
    _SwCpuAction_Type()
)
swCpuAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAction.setStatus("current")
_SwMemUsage_Type = Integer32
_SwMemUsage_Object = MibScalar
swMemUsage = _SwMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 6),
    _SwMemUsage_Type()
)
swMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemUsage.setStatus("current")
_SwMemNoOfRetries_Type = Integer32
_SwMemNoOfRetries_Object = MibScalar
swMemNoOfRetries = _SwMemNoOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 7),
    _SwMemNoOfRetries_Type()
)
swMemNoOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemNoOfRetries.setStatus("current")
_SwMemUsageLimit_Type = Integer32
_SwMemUsageLimit_Object = MibScalar
swMemUsageLimit = _SwMemUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 8),
    _SwMemUsageLimit_Type()
)
swMemUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemUsageLimit.setStatus("current")


class _SwMemPollingInterval_Type(Integer32):
    """Custom type swMemPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SwMemPollingInterval_Type.__name__ = "Integer32"
_SwMemPollingInterval_Object = MibScalar
swMemPollingInterval = _SwMemPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 9),
    _SwMemPollingInterval_Type()
)
swMemPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    swMemPollingInterval.setUnits("seconds")


class _SwMemAction_Type(Integer32):
    """Custom type swMemAction based on Integer32"""
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
        *(("none", 0),
          ("raslog", 1),
          ("raslogandSnmp", 3),
          ("snmp", 2))
    )


_SwMemAction_Type.__name__ = "Integer32"
_SwMemAction_Object = MibScalar
swMemAction = _SwMemAction_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 10),
    _SwMemAction_Type()
)
swMemAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemAction.setStatus("current")
_SwMemUsageLimit1_Type = Integer32
_SwMemUsageLimit1_Object = MibScalar
swMemUsageLimit1 = _SwMemUsageLimit1_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 11),
    _SwMemUsageLimit1_Type()
)
swMemUsageLimit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemUsageLimit1.setStatus("current")
_SwMemUsageLimit3_Type = Integer32
_SwMemUsageLimit3_Object = MibScalar
swMemUsageLimit3 = _SwMemUsageLimit3_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 12),
    _SwMemUsageLimit3_Type()
)
swMemUsageLimit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemUsageLimit3.setStatus("current")
_SwConnUnitPortStatExtentionTable_Object = MibTable
swConnUnitPortStatExtentionTable = _SwConnUnitPortStatExtentionTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27)
)
if mibBuilder.loadTexts:
    swConnUnitPortStatExtentionTable.setStatus("current")
_SwConnUnitPortStatEntry_Object = MibTableRow
swConnUnitPortStatEntry = _SwConnUnitPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1)
)
if mibBuilder.loadTexts:
    swConnUnitPortStatEntry.setStatus("current")


class _SwConnUnitCRCWithBadEOF_Type(OctetString):
    """Custom type swConnUnitCRCWithBadEOF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitCRCWithBadEOF_Type.__name__ = "OctetString"
_SwConnUnitCRCWithBadEOF_Object = MibTableColumn
swConnUnitCRCWithBadEOF = _SwConnUnitCRCWithBadEOF_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 1),
    _SwConnUnitCRCWithBadEOF_Type()
)
swConnUnitCRCWithBadEOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitCRCWithBadEOF.setStatus("current")


class _SwConnUnitZeroTenancy_Type(OctetString):
    """Custom type swConnUnitZeroTenancy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitZeroTenancy_Type.__name__ = "OctetString"
_SwConnUnitZeroTenancy_Object = MibTableColumn
swConnUnitZeroTenancy = _SwConnUnitZeroTenancy_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 2),
    _SwConnUnitZeroTenancy_Type()
)
swConnUnitZeroTenancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitZeroTenancy.setStatus("current")


class _SwConnUnitFLNumOfTenancy_Type(OctetString):
    """Custom type swConnUnitFLNumOfTenancy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitFLNumOfTenancy_Type.__name__ = "OctetString"
_SwConnUnitFLNumOfTenancy_Object = MibTableColumn
swConnUnitFLNumOfTenancy = _SwConnUnitFLNumOfTenancy_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 3),
    _SwConnUnitFLNumOfTenancy_Type()
)
swConnUnitFLNumOfTenancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitFLNumOfTenancy.setStatus("current")


class _SwConnUnitNLNumOfTenancy_Type(OctetString):
    """Custom type swConnUnitNLNumOfTenancy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitNLNumOfTenancy_Type.__name__ = "OctetString"
_SwConnUnitNLNumOfTenancy_Object = MibTableColumn
swConnUnitNLNumOfTenancy = _SwConnUnitNLNumOfTenancy_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 4),
    _SwConnUnitNLNumOfTenancy_Type()
)
swConnUnitNLNumOfTenancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitNLNumOfTenancy.setStatus("current")


class _SwConnUnitStopTenancyStarVation_Type(OctetString):
    """Custom type swConnUnitStopTenancyStarVation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitStopTenancyStarVation_Type.__name__ = "OctetString"
_SwConnUnitStopTenancyStarVation_Object = MibTableColumn
swConnUnitStopTenancyStarVation = _SwConnUnitStopTenancyStarVation_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 5),
    _SwConnUnitStopTenancyStarVation_Type()
)
swConnUnitStopTenancyStarVation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitStopTenancyStarVation.setStatus("current")


class _SwConnUnitOpend_Type(OctetString):
    """Custom type swConnUnitOpend based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitOpend_Type.__name__ = "OctetString"
_SwConnUnitOpend_Object = MibTableColumn
swConnUnitOpend = _SwConnUnitOpend_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 6),
    _SwConnUnitOpend_Type()
)
swConnUnitOpend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitOpend.setStatus("current")


class _SwConnUnitTransferConnection_Type(OctetString):
    """Custom type swConnUnitTransferConnection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitTransferConnection_Type.__name__ = "OctetString"
_SwConnUnitTransferConnection_Object = MibTableColumn
swConnUnitTransferConnection = _SwConnUnitTransferConnection_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 7),
    _SwConnUnitTransferConnection_Type()
)
swConnUnitTransferConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitTransferConnection.setStatus("current")


class _SwConnUnitOpen_Type(OctetString):
    """Custom type swConnUnitOpen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitOpen_Type.__name__ = "OctetString"
_SwConnUnitOpen_Object = MibTableColumn
swConnUnitOpen = _SwConnUnitOpen_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 8),
    _SwConnUnitOpen_Type()
)
swConnUnitOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitOpen.setStatus("current")


class _SwConnUnitInvalidARB_Type(OctetString):
    """Custom type swConnUnitInvalidARB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitInvalidARB_Type.__name__ = "OctetString"
_SwConnUnitInvalidARB_Object = MibTableColumn
swConnUnitInvalidARB = _SwConnUnitInvalidARB_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 9),
    _SwConnUnitInvalidARB_Type()
)
swConnUnitInvalidARB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitInvalidARB.setStatus("current")


class _SwConnUnitFTB1Miss_Type(OctetString):
    """Custom type swConnUnitFTB1Miss based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitFTB1Miss_Type.__name__ = "OctetString"
_SwConnUnitFTB1Miss_Object = MibTableColumn
swConnUnitFTB1Miss = _SwConnUnitFTB1Miss_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 10),
    _SwConnUnitFTB1Miss_Type()
)
swConnUnitFTB1Miss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitFTB1Miss.setStatus("current")


class _SwConnUnitFTB2Miss_Type(OctetString):
    """Custom type swConnUnitFTB2Miss based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitFTB2Miss_Type.__name__ = "OctetString"
_SwConnUnitFTB2Miss_Object = MibTableColumn
swConnUnitFTB2Miss = _SwConnUnitFTB2Miss_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 11),
    _SwConnUnitFTB2Miss_Type()
)
swConnUnitFTB2Miss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitFTB2Miss.setStatus("current")


class _SwConnUnitFTB6Miss_Type(OctetString):
    """Custom type swConnUnitFTB6Miss based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitFTB6Miss_Type.__name__ = "OctetString"
_SwConnUnitFTB6Miss_Object = MibTableColumn
swConnUnitFTB6Miss = _SwConnUnitFTB6Miss_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 12),
    _SwConnUnitFTB6Miss_Type()
)
swConnUnitFTB6Miss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitFTB6Miss.setStatus("current")


class _SwConnUnitZoneMiss_Type(OctetString):
    """Custom type swConnUnitZoneMiss based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitZoneMiss_Type.__name__ = "OctetString"
_SwConnUnitZoneMiss_Object = MibTableColumn
swConnUnitZoneMiss = _SwConnUnitZoneMiss_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 13),
    _SwConnUnitZoneMiss_Type()
)
swConnUnitZoneMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitZoneMiss.setStatus("current")


class _SwConnUnitLunZoneMiss_Type(OctetString):
    """Custom type swConnUnitLunZoneMiss based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitLunZoneMiss_Type.__name__ = "OctetString"
_SwConnUnitLunZoneMiss_Object = MibTableColumn
swConnUnitLunZoneMiss = _SwConnUnitLunZoneMiss_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 14),
    _SwConnUnitLunZoneMiss_Type()
)
swConnUnitLunZoneMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitLunZoneMiss.setStatus("current")


class _SwConnUnitBadEOF_Type(OctetString):
    """Custom type swConnUnitBadEOF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitBadEOF_Type.__name__ = "OctetString"
_SwConnUnitBadEOF_Object = MibTableColumn
swConnUnitBadEOF = _SwConnUnitBadEOF_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 15),
    _SwConnUnitBadEOF_Type()
)
swConnUnitBadEOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitBadEOF.setStatus("current")


class _SwConnUnitLCRX_Type(OctetString):
    """Custom type swConnUnitLCRX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitLCRX_Type.__name__ = "OctetString"
_SwConnUnitLCRX_Object = MibTableColumn
swConnUnitLCRX = _SwConnUnitLCRX_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 16),
    _SwConnUnitLCRX_Type()
)
swConnUnitLCRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitLCRX.setStatus("current")


class _SwConnUnitRDYPriority_Type(OctetString):
    """Custom type swConnUnitRDYPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitRDYPriority_Type.__name__ = "OctetString"
_SwConnUnitRDYPriority_Object = MibTableColumn
swConnUnitRDYPriority = _SwConnUnitRDYPriority_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 17),
    _SwConnUnitRDYPriority_Type()
)
swConnUnitRDYPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitRDYPriority.setStatus("current")


class _SwConnUnitLli_Type(OctetString):
    """Custom type swConnUnitLli based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitLli_Type.__name__ = "OctetString"
_SwConnUnitLli_Object = MibTableColumn
swConnUnitLli = _SwConnUnitLli_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 18),
    _SwConnUnitLli_Type()
)
swConnUnitLli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitLli.setStatus("current")


class _SwConnUnitInterrupts_Type(OctetString):
    """Custom type swConnUnitInterrupts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitInterrupts_Type.__name__ = "OctetString"
_SwConnUnitInterrupts_Object = MibTableColumn
swConnUnitInterrupts = _SwConnUnitInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 19),
    _SwConnUnitInterrupts_Type()
)
swConnUnitInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitInterrupts.setStatus("current")


class _SwConnUnitUnknownInterrupts_Type(OctetString):
    """Custom type swConnUnitUnknownInterrupts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitUnknownInterrupts_Type.__name__ = "OctetString"
_SwConnUnitUnknownInterrupts_Object = MibTableColumn
swConnUnitUnknownInterrupts = _SwConnUnitUnknownInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 20),
    _SwConnUnitUnknownInterrupts_Type()
)
swConnUnitUnknownInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitUnknownInterrupts.setStatus("current")


class _SwConnUnitTimedOut_Type(OctetString):
    """Custom type swConnUnitTimedOut based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitTimedOut_Type.__name__ = "OctetString"
_SwConnUnitTimedOut_Object = MibTableColumn
swConnUnitTimedOut = _SwConnUnitTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 21),
    _SwConnUnitTimedOut_Type()
)
swConnUnitTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitTimedOut.setStatus("current")


class _SwConnUnitProcRequired_Type(OctetString):
    """Custom type swConnUnitProcRequired based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitProcRequired_Type.__name__ = "OctetString"
_SwConnUnitProcRequired_Object = MibTableColumn
swConnUnitProcRequired = _SwConnUnitProcRequired_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 22),
    _SwConnUnitProcRequired_Type()
)
swConnUnitProcRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitProcRequired.setStatus("current")


class _SwConnUnitTxBufferUnavailable_Type(OctetString):
    """Custom type swConnUnitTxBufferUnavailable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitTxBufferUnavailable_Type.__name__ = "OctetString"
_SwConnUnitTxBufferUnavailable_Object = MibTableColumn
swConnUnitTxBufferUnavailable = _SwConnUnitTxBufferUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 23),
    _SwConnUnitTxBufferUnavailable_Type()
)
swConnUnitTxBufferUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitTxBufferUnavailable.setStatus("current")


class _SwConnUnitStateChange_Type(OctetString):
    """Custom type swConnUnitStateChange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitStateChange_Type.__name__ = "OctetString"
_SwConnUnitStateChange_Object = MibTableColumn
swConnUnitStateChange = _SwConnUnitStateChange_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 24),
    _SwConnUnitStateChange_Type()
)
swConnUnitStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitStateChange.setStatus("current")


class _SwConnUnitC3DiscardDueToRXTimeout_Type(OctetString):
    """Custom type swConnUnitC3DiscardDueToRXTimeout based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitC3DiscardDueToRXTimeout_Type.__name__ = "OctetString"
_SwConnUnitC3DiscardDueToRXTimeout_Object = MibTableColumn
swConnUnitC3DiscardDueToRXTimeout = _SwConnUnitC3DiscardDueToRXTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 25),
    _SwConnUnitC3DiscardDueToRXTimeout_Type()
)
swConnUnitC3DiscardDueToRXTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitC3DiscardDueToRXTimeout.setStatus("current")


class _SwConnUnitC3DiscardDueToDestUnreachable_Type(OctetString):
    """Custom type swConnUnitC3DiscardDueToDestUnreachable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitC3DiscardDueToDestUnreachable_Type.__name__ = "OctetString"
_SwConnUnitC3DiscardDueToDestUnreachable_Object = MibTableColumn
swConnUnitC3DiscardDueToDestUnreachable = _SwConnUnitC3DiscardDueToDestUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 26),
    _SwConnUnitC3DiscardDueToDestUnreachable_Type()
)
swConnUnitC3DiscardDueToDestUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitC3DiscardDueToDestUnreachable.setStatus("current")


class _SwConnUnitC3DiscardDueToTXTimeout_Type(OctetString):
    """Custom type swConnUnitC3DiscardDueToTXTimeout based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitC3DiscardDueToTXTimeout_Type.__name__ = "OctetString"
_SwConnUnitC3DiscardDueToTXTimeout_Object = MibTableColumn
swConnUnitC3DiscardDueToTXTimeout = _SwConnUnitC3DiscardDueToTXTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 27),
    _SwConnUnitC3DiscardDueToTXTimeout_Type()
)
swConnUnitC3DiscardDueToTXTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitC3DiscardDueToTXTimeout.setStatus("current")


class _SwConnUnitC3DiscardOther_Type(OctetString):
    """Custom type swConnUnitC3DiscardOther based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitC3DiscardOther_Type.__name__ = "OctetString"
_SwConnUnitC3DiscardOther_Object = MibTableColumn
swConnUnitC3DiscardOther = _SwConnUnitC3DiscardOther_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 28),
    _SwConnUnitC3DiscardOther_Type()
)
swConnUnitC3DiscardOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitC3DiscardOther.setStatus("current")


class _SwConnUnitPCSErrorCounter_Type(OctetString):
    """Custom type swConnUnitPCSErrorCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitPCSErrorCounter_Type.__name__ = "OctetString"
_SwConnUnitPCSErrorCounter_Object = MibTableColumn
swConnUnitPCSErrorCounter = _SwConnUnitPCSErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 29),
    _SwConnUnitPCSErrorCounter_Type()
)
swConnUnitPCSErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitPCSErrorCounter.setStatus("current")


class _SwConnUnitUnroutableFrameCounter_Type(OctetString):
    """Custom type swConnUnitUnroutableFrameCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwConnUnitUnroutableFrameCounter_Type.__name__ = "OctetString"
_SwConnUnitUnroutableFrameCounter_Object = MibTableColumn
swConnUnitUnroutableFrameCounter = _SwConnUnitUnroutableFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 30),
    _SwConnUnitUnroutableFrameCounter_Type()
)
swConnUnitUnroutableFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitUnroutableFrameCounter.setStatus("current")


class _SwConnUnitFECCorrectedCounter_Type(OctetString):
    """Custom type swConnUnitFECCorrectedCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwConnUnitFECCorrectedCounter_Type.__name__ = "OctetString"
_SwConnUnitFECCorrectedCounter_Object = MibTableColumn
swConnUnitFECCorrectedCounter = _SwConnUnitFECCorrectedCounter_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 31),
    _SwConnUnitFECCorrectedCounter_Type()
)
swConnUnitFECCorrectedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitFECCorrectedCounter.setStatus("current")


class _SwConnUnitFECUnCorrectedCounter_Type(OctetString):
    """Custom type swConnUnitFECUnCorrectedCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwConnUnitFECUnCorrectedCounter_Type.__name__ = "OctetString"
_SwConnUnitFECUnCorrectedCounter_Object = MibTableColumn
swConnUnitFECUnCorrectedCounter = _SwConnUnitFECUnCorrectedCounter_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 27, 1, 32),
    _SwConnUnitFECUnCorrectedCounter_Type()
)
swConnUnitFECUnCorrectedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swConnUnitFECUnCorrectedCounter.setStatus("current")
_Sw28k_ObjectIdentity = ObjectIdentity
sw28k = _Sw28k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sw28k.setStatus("current")
_Sw21kN24k_ObjectIdentity = ObjectIdentity
sw21kN24k = _Sw21kN24k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sw21kN24k.setStatus("current")
_Sw20x0_ObjectIdentity = ObjectIdentity
sw20x0 = _Sw20x0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sw20x0.setStatus("current")
connUnitPortStatEntry.registerAugmentions(
    ("SW-MIB",
     "swConnUnitPortStatEntry")
)
swConnUnitPortStatEntry.setIndexNames(*connUnitPortStatEntry.getIndexNames())

# Managed Objects groups


# Notification objects

swFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 1)
)
swFault.setObjects(
      *(("SW-MIB", "swDiagResult"),
        ("SW-MIB", "swSsn"))
)
if mibBuilder.loadTexts:
    swFault.setStatus(
        "obsolete"
    )

swSensorScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 2)
)
swSensorScn.setObjects(
      *(("SW-MIB", "swSensorStatus"),
        ("SW-MIB", "swSensorIndex"),
        ("SW-MIB", "swSensorType"),
        ("SW-MIB", "swSensorValue"),
        ("SW-MIB", "swSensorInfo"),
        ("SW-MIB", "swSsn"))
)
if mibBuilder.loadTexts:
    swSensorScn.setStatus(
        "current"
    )

swFCPortScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 3)
)
swFCPortScn.setObjects(
      *(("SW-MIB", "swFCPortOpStatus"),
        ("SW-MIB", "swFCPortIndex"),
        ("SW-MIB", "swFCPortName"),
        ("SW-MIB", "swFCPortWwn"),
        ("SW-MIB", "swFCPortPrevType"),
        ("SW-MIB", "swFCPortBrcdType"),
        ("SW-MIB", "swSsn"),
        ("SW-MIB", "swFCPortFlag"),
        ("SW-MIB", "swFCPortDisableReason"),
        ("SW-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swFCPortScn.setStatus(
        "current"
    )

swEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 4)
)
swEventTrap.setObjects(
      *(("SW-MIB", "swEventIndex"),
        ("SW-MIB", "swEventTimeInfo"),
        ("SW-MIB", "swEventLevel"),
        ("SW-MIB", "swEventRepeatCount"),
        ("SW-MIB", "swEventDescr"),
        ("SW-MIB", "swSsn"),
        ("SW-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swEventTrap.setStatus(
        "current"
    )

swFabricWatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 5)
)
swFabricWatchTrap.setObjects(
      *(("SW-MIB", "swFwClassAreaIndex"),
        ("SW-MIB", "swFwThresholdIndex"),
        ("SW-MIB", "swFwName"),
        ("SW-MIB", "swFwLabel"),
        ("SW-MIB", "swFwLastEventVal"),
        ("SW-MIB", "swFwLastEventTime"),
        ("SW-MIB", "swFwLastEvent"),
        ("SW-MIB", "swFwLastState"),
        ("SW-MIB", "swFwLastSeverityLevel"),
        ("SW-MIB", "swSsn"),
        ("SW-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swFabricWatchTrap.setStatus(
        "current"
    )

swTrackChangesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 6)
)
swTrackChangesTrap.setObjects(
      *(("SW-MIB", "swTrackChangesInfo"),
        ("SW-MIB", "swSsn"),
        ("SW-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swTrackChangesTrap.setStatus(
        "current"
    )

swIPv6ChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 7)
)
swIPv6ChangeTrap.setObjects(
      *(("SW-MIB", "swIPv6Address"),
        ("SW-MIB", "swIPv6Status"))
)
if mibBuilder.loadTexts:
    swIPv6ChangeTrap.setStatus(
        "current"
    )

swPmgrEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 8)
)
swPmgrEventTrap.setObjects(
      *(("SW-MIB", "swPmgrEventType"),
        ("SW-MIB", "swPmgrEventTime"),
        ("SW-MIB", "swPmgrEventDescr"),
        ("SW-MIB", "swSsn"),
        ("SW-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swPmgrEventTrap.setStatus(
        "current"
    )

swFabricReconfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 9)
)
swFabricReconfigTrap.setObjects(
    ("SW-MIB", "swDomainID")
)
if mibBuilder.loadTexts:
    swFabricReconfigTrap.setStatus(
        "current"
    )

swFabricSegmentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 10)
)
swFabricSegmentTrap.setObjects(
      *(("SW-MIB", "swFCPortIndex"),
        ("SW-MIB", "swFCPortName"),
        ("SW-MIB", "swSsn"),
        ("SW-MIB", "swFCPortFlag"),
        ("SW-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swFabricSegmentTrap.setStatus(
        "current"
    )

swExtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 11)
)
if mibBuilder.loadTexts:
    swExtTrap.setStatus(
        "current"
    )

swStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 12)
)
swStateChangeTrap.setObjects(
      *(("SW-MIB", "swOperStatus"),
        ("SW-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swStateChangeTrap.setStatus(
        "current"
    )

swPortMoveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 13)
)
swPortMoveTrap.setObjects(
      *(("SW-MIB", "swPortList"),
        ("SW-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swPortMoveTrap.setStatus(
        "current"
    )

swBrcdGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 14)
)
swBrcdGenericTrap.setObjects(
    ("SW-MIB", "swBrcdTrapBitMask")
)
if mibBuilder.loadTexts:
    swBrcdGenericTrap.setStatus(
        "current"
    )

swDeviceStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 15)
)
swDeviceStatusTrap.setObjects(
      *(("SW-MIB", "swFCPortSpecifier"),
        ("SW-MIB", "swDeviceStatus"),
        ("SW-MIB", "swEndDevicePortID"),
        ("SW-MIB", "swNsNodeName"))
)
if mibBuilder.loadTexts:
    swDeviceStatusTrap.setStatus(
        "current"
    )

swZoneConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 16)
)
swZoneConfigChangeTrap.setObjects(
    ("SW-MIB", "swVfId")
)
if mibBuilder.loadTexts:
    swZoneConfigChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-MIB",
    **{"SwSevType": SwSevType,
       "FcPortFlag": FcPortFlag,
       "SwFwActs": SwFwActs,
       "SwFwLevels": SwFwLevels,
       "SwFwClassesAreas": SwFwClassesAreas,
       "SwFwWriteVals": SwFwWriteVals,
       "SwFwTimebase": SwFwTimebase,
       "SwFwStatus": SwFwStatus,
       "SwFwEvent": SwFwEvent,
       "SwFwBehavior": SwFwBehavior,
       "SwFwState": SwFwState,
       "SwFwLicense": SwFwLicense,
       "sw": sw,
       "swTrapsV2": swTrapsV2,
       "swFault": swFault,
       "swSensorScn": swSensorScn,
       "swFCPortScn": swFCPortScn,
       "swEventTrap": swEventTrap,
       "swFabricWatchTrap": swFabricWatchTrap,
       "swTrackChangesTrap": swTrackChangesTrap,
       "swIPv6ChangeTrap": swIPv6ChangeTrap,
       "swPmgrEventTrap": swPmgrEventTrap,
       "swFabricReconfigTrap": swFabricReconfigTrap,
       "swFabricSegmentTrap": swFabricSegmentTrap,
       "swExtTrap": swExtTrap,
       "swStateChangeTrap": swStateChangeTrap,
       "swPortMoveTrap": swPortMoveTrap,
       "swBrcdGenericTrap": swBrcdGenericTrap,
       "swDeviceStatusTrap": swDeviceStatusTrap,
       "swZoneConfigChangeTrap": swZoneConfigChangeTrap,
       "swSystem": swSystem,
       "swCurrentDate": swCurrentDate,
       "swBootDate": swBootDate,
       "swFWLastUpdated": swFWLastUpdated,
       "swFlashLastUpdated": swFlashLastUpdated,
       "swBootPromLastUpdated": swBootPromLastUpdated,
       "swFirmwareVersion": swFirmwareVersion,
       "swOperStatus": swOperStatus,
       "swAdmStatus": swAdmStatus,
       "swTelnetShellAdmStatus": swTelnetShellAdmStatus,
       "swSsn": swSsn,
       "swFlashDLOperStatus": swFlashDLOperStatus,
       "swFlashDLAdmStatus": swFlashDLAdmStatus,
       "swFlashDLHost": swFlashDLHost,
       "swFlashDLUser": swFlashDLUser,
       "swFlashDLFile": swFlashDLFile,
       "swFlashDLPassword": swFlashDLPassword,
       "swBeaconOperStatus": swBeaconOperStatus,
       "swBeaconAdmStatus": swBeaconAdmStatus,
       "swDiagResult": swDiagResult,
       "swNumSensors": swNumSensors,
       "swSensorTable": swSensorTable,
       "swSensorEntry": swSensorEntry,
       "swSensorIndex": swSensorIndex,
       "swSensorType": swSensorType,
       "swSensorStatus": swSensorStatus,
       "swSensorValue": swSensorValue,
       "swSensorInfo": swSensorInfo,
       "swTrackChangesInfo": swTrackChangesInfo,
       "swID": swID,
       "swEtherIPAddress": swEtherIPAddress,
       "swEtherIPMask": swEtherIPMask,
       "swFCIPAddress": swFCIPAddress,
       "swFCIPMask": swFCIPMask,
       "swIPv6Address": swIPv6Address,
       "swIPv6Status": swIPv6Status,
       "swModel": swModel,
       "swTestString": swTestString,
       "swPortList": swPortList,
       "swBrcdTrapBitMask": swBrcdTrapBitMask,
       "swFCPortPrevType": swFCPortPrevType,
       "swDeviceStatus": swDeviceStatus,
       "swFabric": swFabric,
       "swDomainID": swDomainID,
       "swPrincipalSwitch": swPrincipalSwitch,
       "swNumNbs": swNumNbs,
       "swNbTable": swNbTable,
       "swNbEntry": swNbEntry,
       "swNbIndex": swNbIndex,
       "swNbMyPort": swNbMyPort,
       "swNbRemDomain": swNbRemDomain,
       "swNbRemPort": swNbRemPort,
       "swNbBaudRate": swNbBaudRate,
       "swNbIslState": swNbIslState,
       "swNbIslCost": swNbIslCost,
       "swNbRemPortName": swNbRemPortName,
       "swFabricMemTable": swFabricMemTable,
       "swFabricMemEntry": swFabricMemEntry,
       "swFabricMemWwn": swFabricMemWwn,
       "swFabricMemDid": swFabricMemDid,
       "swFabricMemName": swFabricMemName,
       "swFabricMemEIP": swFabricMemEIP,
       "swFabricMemFCIP": swFabricMemFCIP,
       "swFabricMemGWIP": swFabricMemGWIP,
       "swFabricMemType": swFabricMemType,
       "swFabricMemShortVersion": swFabricMemShortVersion,
       "swIDIDMode": swIDIDMode,
       "swPmgrEventType": swPmgrEventType,
       "swPmgrEventTime": swPmgrEventTime,
       "swPmgrEventDescr": swPmgrEventDescr,
       "swVfId": swVfId,
       "swVfName": swVfName,
       "swModule": swModule,
       "swAgtCfg": swAgtCfg,
       "swAgtCmtyTable": swAgtCmtyTable,
       "swAgtCmtyEntry": swAgtCmtyEntry,
       "swAgtCmtyIdx": swAgtCmtyIdx,
       "swAgtCmtyStr": swAgtCmtyStr,
       "swAgtTrapRcp": swAgtTrapRcp,
       "swAgtTrapSeverityLevel": swAgtTrapSeverityLevel,
       "swauthProtocolPassword": swauthProtocolPassword,
       "swprivProtocolPassword": swprivProtocolPassword,
       "swFCport": swFCport,
       "swFCPortCapacity": swFCPortCapacity,
       "swFCPortTable": swFCPortTable,
       "swFCPortEntry": swFCPortEntry,
       "swFCPortIndex": swFCPortIndex,
       "swFCPortType": swFCPortType,
       "swFCPortPhyState": swFCPortPhyState,
       "swFCPortOpStatus": swFCPortOpStatus,
       "swFCPortAdmStatus": swFCPortAdmStatus,
       "swFCPortLinkState": swFCPortLinkState,
       "swFCPortTxType": swFCPortTxType,
       "swFCPortTxWords": swFCPortTxWords,
       "swFCPortRxWords": swFCPortRxWords,
       "swFCPortTxFrames": swFCPortTxFrames,
       "swFCPortRxFrames": swFCPortRxFrames,
       "swFCPortRxC2Frames": swFCPortRxC2Frames,
       "swFCPortRxC3Frames": swFCPortRxC3Frames,
       "swFCPortRxLCs": swFCPortRxLCs,
       "swFCPortRxMcasts": swFCPortRxMcasts,
       "swFCPortTooManyRdys": swFCPortTooManyRdys,
       "swFCPortNoTxCredits": swFCPortNoTxCredits,
       "swFCPortRxEncInFrs": swFCPortRxEncInFrs,
       "swFCPortRxCrcs": swFCPortRxCrcs,
       "swFCPortRxTruncs": swFCPortRxTruncs,
       "swFCPortRxTooLongs": swFCPortRxTooLongs,
       "swFCPortRxBadEofs": swFCPortRxBadEofs,
       "swFCPortRxEncOutFrs": swFCPortRxEncOutFrs,
       "swFCPortRxBadOs": swFCPortRxBadOs,
       "swFCPortC3Discards": swFCPortC3Discards,
       "swFCPortMcastTimedOuts": swFCPortMcastTimedOuts,
       "swFCPortTxMcasts": swFCPortTxMcasts,
       "swFCPortLipIns": swFCPortLipIns,
       "swFCPortLipOuts": swFCPortLipOuts,
       "swFCPortLipLastAlpa": swFCPortLipLastAlpa,
       "swFCPortWwn": swFCPortWwn,
       "swFCPortSpeed": swFCPortSpeed,
       "swFCPortName": swFCPortName,
       "swFCPortSpecifier": swFCPortSpecifier,
       "swFCPortFlag": swFCPortFlag,
       "swFCPortBrcdType": swFCPortBrcdType,
       "swFCPortDisableReason": swFCPortDisableReason,
       "swNs": swNs,
       "swNsLocalNumEntry": swNsLocalNumEntry,
       "swNsLocalTable": swNsLocalTable,
       "swNsLocalEntry": swNsLocalEntry,
       "swNsEntryIndex": swNsEntryIndex,
       "swNsPortID": swNsPortID,
       "swNsPortType": swNsPortType,
       "swNsPortName": swNsPortName,
       "swNsPortSymb": swNsPortSymb,
       "swNsNodeName": swNsNodeName,
       "swNsNodeSymb": swNsNodeSymb,
       "swNsIPA": swNsIPA,
       "swNsIpAddress": swNsIpAddress,
       "swNsCos": swNsCos,
       "swNsFc4": swNsFc4,
       "swNsIpNxPort": swNsIpNxPort,
       "swNsWwn": swNsWwn,
       "swNsHardAddr": swNsHardAddr,
       "swEvent": swEvent,
       "swEventTrapLevel": swEventTrapLevel,
       "swEventNumEntries": swEventNumEntries,
       "swEventTable": swEventTable,
       "swEventEntry": swEventEntry,
       "swEventIndex": swEventIndex,
       "swEventTimeInfo": swEventTimeInfo,
       "swEventLevel": swEventLevel,
       "swEventRepeatCount": swEventRepeatCount,
       "swEventDescr": swEventDescr,
       "swEventVfId": swEventVfId,
       "swFwSystem": swFwSystem,
       "swFwFabricWatchLicense": swFwFabricWatchLicense,
       "swFwClassAreaTable": swFwClassAreaTable,
       "swFwClassAreaEntry": swFwClassAreaEntry,
       "swFwClassAreaIndex": swFwClassAreaIndex,
       "swFwWriteThVals": swFwWriteThVals,
       "swFwDefaultUnit": swFwDefaultUnit,
       "swFwDefaultTimebase": swFwDefaultTimebase,
       "swFwDefaultLow": swFwDefaultLow,
       "swFwDefaultHigh": swFwDefaultHigh,
       "swFwDefaultBufSize": swFwDefaultBufSize,
       "swFwCustUnit": swFwCustUnit,
       "swFwCustTimebase": swFwCustTimebase,
       "swFwCustLow": swFwCustLow,
       "swFwCustHigh": swFwCustHigh,
       "swFwCustBufSize": swFwCustBufSize,
       "swFwThLevel": swFwThLevel,
       "swFwWriteActVals": swFwWriteActVals,
       "swFwDefaultChangedActs": swFwDefaultChangedActs,
       "swFwDefaultExceededActs": swFwDefaultExceededActs,
       "swFwDefaultBelowActs": swFwDefaultBelowActs,
       "swFwDefaultAboveActs": swFwDefaultAboveActs,
       "swFwDefaultInBetweenActs": swFwDefaultInBetweenActs,
       "swFwCustChangedActs": swFwCustChangedActs,
       "swFwCustExceededActs": swFwCustExceededActs,
       "swFwCustBelowActs": swFwCustBelowActs,
       "swFwCustAboveActs": swFwCustAboveActs,
       "swFwCustInBetweenActs": swFwCustInBetweenActs,
       "swFwValidActs": swFwValidActs,
       "swFwActLevel": swFwActLevel,
       "swFwThresholdTable": swFwThresholdTable,
       "swFwThresholdEntry": swFwThresholdEntry,
       "swFwThresholdIndex": swFwThresholdIndex,
       "swFwStatus": swFwStatus,
       "swFwName": swFwName,
       "swFwLabel": swFwLabel,
       "swFwCurVal": swFwCurVal,
       "swFwLastEvent": swFwLastEvent,
       "swFwLastEventVal": swFwLastEventVal,
       "swFwLastEventTime": swFwLastEventTime,
       "swFwLastState": swFwLastState,
       "swFwBehaviorType": swFwBehaviorType,
       "swFwBehaviorInt": swFwBehaviorInt,
       "swFwLastSeverityLevel": swFwLastSeverityLevel,
       "swEndDevice": swEndDevice,
       "swEndDeviceRlsTable": swEndDeviceRlsTable,
       "swEndDeviceRlsEntry": swEndDeviceRlsEntry,
       "swEndDevicePort": swEndDevicePort,
       "swEndDeviceAlpa": swEndDeviceAlpa,
       "swEndDevicePortID": swEndDevicePortID,
       "swEndDeviceLinkFailure": swEndDeviceLinkFailure,
       "swEndDeviceSyncLoss": swEndDeviceSyncLoss,
       "swEndDeviceSigLoss": swEndDeviceSigLoss,
       "swEndDeviceProtoErr": swEndDeviceProtoErr,
       "swEndDeviceInvalidWord": swEndDeviceInvalidWord,
       "swEndDeviceInvalidCRC": swEndDeviceInvalidCRC,
       "swGroup": swGroup,
       "swGroupTable": swGroupTable,
       "swGroupEntry": swGroupEntry,
       "swGroupIndex": swGroupIndex,
       "swGroupName": swGroupName,
       "swGroupType": swGroupType,
       "swGroupMemTable": swGroupMemTable,
       "swGroupMemEntry": swGroupMemEntry,
       "swGroupId": swGroupId,
       "swGroupMemWwn": swGroupMemWwn,
       "swGroupMemPos": swGroupMemPos,
       "swBlmPerfMnt": swBlmPerfMnt,
       "swBlmPerfALPAMntTable": swBlmPerfALPAMntTable,
       "swBlmPerfALPAMntEntry": swBlmPerfALPAMntEntry,
       "swBlmPerfAlpaPort": swBlmPerfAlpaPort,
       "swBlmPerfAlpaIndx": swBlmPerfAlpaIndx,
       "swBlmPerfAlpa": swBlmPerfAlpa,
       "swBlmPerfAlpaCRCCnt": swBlmPerfAlpaCRCCnt,
       "swBlmPerfEEMntTable": swBlmPerfEEMntTable,
       "swBlmPerfEEMntEntry": swBlmPerfEEMntEntry,
       "swBlmPerfEEPort": swBlmPerfEEPort,
       "swBlmPerfEERefKey": swBlmPerfEERefKey,
       "swBlmPerfEECRC": swBlmPerfEECRC,
       "swBlmPerfEEFCWRx": swBlmPerfEEFCWRx,
       "swBlmPerfEEFCWTx": swBlmPerfEEFCWTx,
       "swBlmPerfEESid": swBlmPerfEESid,
       "swBlmPerfEEDid": swBlmPerfEEDid,
       "swBlmPerfFltMntTable": swBlmPerfFltMntTable,
       "swBlmPerfFltMntEntry": swBlmPerfFltMntEntry,
       "swBlmPerfFltPort": swBlmPerfFltPort,
       "swBlmPerfFltRefkey": swBlmPerfFltRefkey,
       "swBlmPerfFltCnt": swBlmPerfFltCnt,
       "swBlmPerfFltAlias": swBlmPerfFltAlias,
       "swTrunk": swTrunk,
       "swSwitchTrunkable": swSwitchTrunkable,
       "swTrunkTable": swTrunkTable,
       "swTrunkEntry": swTrunkEntry,
       "swTrunkPortIndex": swTrunkPortIndex,
       "swTrunkGroupNumber": swTrunkGroupNumber,
       "swTrunkMaster": swTrunkMaster,
       "swPortTrunked": swPortTrunked,
       "swTrunkGrpTable": swTrunkGrpTable,
       "swTrunkGrpEntry": swTrunkGrpEntry,
       "swTrunkGrpNumber": swTrunkGrpNumber,
       "swTrunkGrpMaster": swTrunkGrpMaster,
       "swTrunkGrpTx": swTrunkGrpTx,
       "swTrunkGrpRx": swTrunkGrpRx,
       "swTopTalker": swTopTalker,
       "swTopTalkerMntMode": swTopTalkerMntMode,
       "swTopTalkerMntNumEntries": swTopTalkerMntNumEntries,
       "swTopTalkerMntTable": swTopTalkerMntTable,
       "swTopTalkerMntEntry": swTopTalkerMntEntry,
       "swTopTalkerMntIndex": swTopTalkerMntIndex,
       "swTopTalkerMntPort": swTopTalkerMntPort,
       "swTopTalkerMntSpid": swTopTalkerMntSpid,
       "swTopTalkerMntDpid": swTopTalkerMntDpid,
       "swTopTalkerMntflow": swTopTalkerMntflow,
       "swTopTalkerMntSwwn": swTopTalkerMntSwwn,
       "swTopTalkerMntDwwn": swTopTalkerMntDwwn,
       "swCpuOrMemoryUsage": swCpuOrMemoryUsage,
       "swCpuUsage": swCpuUsage,
       "swCpuNoOfRetries": swCpuNoOfRetries,
       "swCpuUsageLimit": swCpuUsageLimit,
       "swCpuPollingInterval": swCpuPollingInterval,
       "swCpuAction": swCpuAction,
       "swMemUsage": swMemUsage,
       "swMemNoOfRetries": swMemNoOfRetries,
       "swMemUsageLimit": swMemUsageLimit,
       "swMemPollingInterval": swMemPollingInterval,
       "swMemAction": swMemAction,
       "swMemUsageLimit1": swMemUsageLimit1,
       "swMemUsageLimit3": swMemUsageLimit3,
       "swConnUnitPortStatExtentionTable": swConnUnitPortStatExtentionTable,
       "swConnUnitPortStatEntry": swConnUnitPortStatEntry,
       "swConnUnitCRCWithBadEOF": swConnUnitCRCWithBadEOF,
       "swConnUnitZeroTenancy": swConnUnitZeroTenancy,
       "swConnUnitFLNumOfTenancy": swConnUnitFLNumOfTenancy,
       "swConnUnitNLNumOfTenancy": swConnUnitNLNumOfTenancy,
       "swConnUnitStopTenancyStarVation": swConnUnitStopTenancyStarVation,
       "swConnUnitOpend": swConnUnitOpend,
       "swConnUnitTransferConnection": swConnUnitTransferConnection,
       "swConnUnitOpen": swConnUnitOpen,
       "swConnUnitInvalidARB": swConnUnitInvalidARB,
       "swConnUnitFTB1Miss": swConnUnitFTB1Miss,
       "swConnUnitFTB2Miss": swConnUnitFTB2Miss,
       "swConnUnitFTB6Miss": swConnUnitFTB6Miss,
       "swConnUnitZoneMiss": swConnUnitZoneMiss,
       "swConnUnitLunZoneMiss": swConnUnitLunZoneMiss,
       "swConnUnitBadEOF": swConnUnitBadEOF,
       "swConnUnitLCRX": swConnUnitLCRX,
       "swConnUnitRDYPriority": swConnUnitRDYPriority,
       "swConnUnitLli": swConnUnitLli,
       "swConnUnitInterrupts": swConnUnitInterrupts,
       "swConnUnitUnknownInterrupts": swConnUnitUnknownInterrupts,
       "swConnUnitTimedOut": swConnUnitTimedOut,
       "swConnUnitProcRequired": swConnUnitProcRequired,
       "swConnUnitTxBufferUnavailable": swConnUnitTxBufferUnavailable,
       "swConnUnitStateChange": swConnUnitStateChange,
       "swConnUnitC3DiscardDueToRXTimeout": swConnUnitC3DiscardDueToRXTimeout,
       "swConnUnitC3DiscardDueToDestUnreachable": swConnUnitC3DiscardDueToDestUnreachable,
       "swConnUnitC3DiscardDueToTXTimeout": swConnUnitC3DiscardDueToTXTimeout,
       "swConnUnitC3DiscardOther": swConnUnitC3DiscardOther,
       "swConnUnitPCSErrorCounter": swConnUnitPCSErrorCounter,
       "swConnUnitUnroutableFrameCounter": swConnUnitUnroutableFrameCounter,
       "swConnUnitFECCorrectedCounter": swConnUnitFECCorrectedCounter,
       "swConnUnitFECUnCorrectedCounter": swConnUnitFECUnCorrectedCounter,
       "sw28k": sw28k,
       "sw21kN24k": sw21kN24k,
       "sw20x0": sw20x0,
       "swMibModule": swMibModule}
)
