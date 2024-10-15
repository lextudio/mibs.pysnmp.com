# SNMP MIB module (Juniper-System-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-System-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:26 2024
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

(PhysicalIndex,
 entPhysicalDescr) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalDescr")

(KBytes,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "KBytes")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,
 JuniTimeFilter) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniTimeFilter")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2)
)
juniSystemMIB.setRevisions(
        ("2010-03-12 13:45",
         "2008-06-11 11:01",
         "2008-05-05 12:41",
         "2007-05-07 10:12",
         "2006-12-18 21:25",
         "2006-11-24 09:13",
         "2006-05-18 08:31",
         "2006-01-06 18:17",
         "2005-12-16 07:21",
         "2005-11-18 22:30",
         "2005-09-15 14:14",
         "2005-08-19 17:48",
         "2005-07-29 17:48",
         "2005-05-18 18:10",
         "2005-05-04 18:10",
         "2005-01-31 18:13",
         "2004-12-31 10:13",
         "2004-12-29 10:10",
         "2004-05-25 18:13",
         "2004-01-07 22:46",
         "2003-11-24 20:59",
         "2003-11-24 19:39",
         "2003-07-22 14:10",
         "2003-01-27 21:22",
         "2002-10-17 21:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniSystemModuleType(Integer32, TextualConvention):
    status = "current"
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
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036,
              1037,
              1038,
              1039,
              1040,
              1041,
              1042,
              1043,
              1044,
              1045,
              1046,
              1047,
              1048,
              1049,
              1050,
              1051,
              1052,
              1053,
              1054,
              1055,
              1056,
              1057,
              1058,
              1059,
              1060,
              1061,
              1062,
              1063,
              1064,
              1065,
              1066,
              1067,
              1068,
              1069,
              1070,
              1071,
              1072,
              1073,
              1074,
              1075,
              1076,
              1077,
              1078,
              1079,
              2048,
              2049,
              2050,
              2051,
              2052,
              2053,
              2054,
              2055,
              3072,
              3073,
              3074,
              3075,
              3076,
              3077,
              3078,
              3079,
              3080,
              3081,
              3082,
              3083,
              4096,
              4097)
        )
    )
    namedValues = NamedValues(
        *(("e120Sfm120", 4097),
          ("e120Srp120", 4096),
          ("e320Sfm100", 2049),
          ("e320Sfm320", 2054),
          ("e320Srp100", 2048),
          ("e320Srp320", 2053),
          ("e320SrpIoa", 3072),
          ("erxCOc12AtmPosMm1ApsIoa", 1063),
          ("erxCOc12AtmPosMm1Ioa", 1060),
          ("erxCOc12AtmPosSmIr1ApsIoa", 1064),
          ("erxCOc12AtmPosSmIr1Ioa", 1061),
          ("erxCOc12AtmPosSmLr1ApsIoa", 1065),
          ("erxCOc12AtmPosSmLr1Ioa", 1062),
          ("erxCOc12Mm1ApsIoa", 1054),
          ("erxCOc12Mm1Ioa", 1041),
          ("erxCOc12SmIr1ApsIoa", 1055),
          ("erxCOc12SmIr1Ioa", 1042),
          ("erxCOc12SmLr1ApsIoa", 1056),
          ("erxCOc12SmLr1Ioa", 1043),
          ("erxCOc3Mm4Ioa", 1035),
          ("erxCOc3SmIr4Ioa", 1036),
          ("erxCOc3SmLr4Ioa", 1037),
          ("erxCOcxRedundantIoa", 1070),
          ("erxCe1", 8),
          ("erxCe1Ioa", 1026),
          ("erxCe1TIoa", 1027),
          ("erxCoc12", 21),
          ("erxCoc12F3", 29),
          ("erxCoc3", 20),
          ("erxCoc3F3", 30),
          ("erxCoc3oc12", 19),
          ("erxCocxF3", 31),
          ("erxCt1", 9),
          ("erxCt1Ioa", 1025),
          ("erxCt3", 2),
          ("erxCt3Ioa", 1028),
          ("erxCt3P12", 25),
          ("erxCt3P12Ioa", 1049),
          ("erxCt3RedundantIoa", 1068),
          ("erxDpfe", 10),
          ("erxE3Ioa", 1029),
          ("erxFe2Ioa", 1044),
          ("erxFe8", 16),
          ("erxFe8FxIoa", 1078),
          ("erxFe8Ioa", 1045),
          ("erxGe", 15),
          ("erxGe2", 38),
          ("erxGe2Ioa", 1077),
          ("erxGe8Ioa", 1079),
          ("erxGeFe", 24),
          ("erxGeHde", 39),
          ("erxGeMm1Ioa", 1046),
          ("erxGeSfpIoa", 1051),
          ("erxGeSm1Ioa", 1047),
          ("erxHssi", 23),
          ("erxHssiIoa", 1048),
          ("erxHybrid", 35),
          ("erxOc12Atm", 12),
          ("erxOc12Mm1ApsIoa", 1057),
          ("erxOc12Mm1Ioa", 1038),
          ("erxOc12Pos", 11),
          ("erxOc12Server", 22),
          ("erxOc12SmIr1ApsIoa", 1058),
          ("erxOc12SmIr1Ioa", 1039),
          ("erxOc12SmLr1ApsIoa", 1059),
          ("erxOc12SmLr1Ioa", 1040),
          ("erxOc3", 3),
          ("erxOc3Atm", 14),
          ("erxOc3Atm2Ge1Ioa", 1075),
          ("erxOc3Atm2Pos2Ioa", 1076),
          ("erxOc3AtmGe", 36),
          ("erxOc3AtmPos", 37),
          ("erxOc3Mm2Ioa", 1030),
          ("erxOc3Mm4ApsIoa", 1071),
          ("erxOc3Mm4Ioa", 1032),
          ("erxOc3Pos", 13),
          ("erxOc3Sm2Ioa", 1031),
          ("erxOc3SmIr4ApsIoa", 1072),
          ("erxOc3SmIr4Ioa", 1033),
          ("erxOc3SmLr4ApsIoa", 1073),
          ("erxOc3SmLr4Ioa", 1034),
          ("erxOc3oc12Atm", 18),
          ("erxOc3oc12Pos", 17),
          ("erxOc48", 33),
          ("erxOc48Ioa", 1074),
          ("erxOcxRedundantIoa", 1069),
          ("erxSrp", 1),
          ("erxSrpIoa", 1024),
          ("erxT1E1RedundantIoa", 1066),
          ("erxT3Atm4Ioa", 1053),
          ("erxT3E3RedundantIoa", 1067),
          ("erxUe3Atm", 6),
          ("erxUe3Frame", 7),
          ("erxUe3P12Ioa", 1052),
          ("erxUe3f12", 28),
          ("erxUt3Atm", 4),
          ("erxUt3Atm4", 34),
          ("erxUt3Frame", 5),
          ("erxUt3f12", 27),
          ("erxV35", 26),
          ("erxV35Ioa", 1050),
          ("erxVts", 32),
          ("es2Ge20S2Ioa", 3083),
          ("es2Ge4S1Ioa", 3073),
          ("es2Ge8S1Ioa", 3081),
          ("es2Lm10", 2052),
          ("es2Lm10Uplink", 2051),
          ("es2Lm10s", 2055),
          ("es2Lm4", 2050),
          ("es2Oc12Stm4x2AtmS1Ioa", 3079),
          ("es2Oc12Stm4x2PosS1Ioa", 3078),
          ("es2Oc3Stm1x8AtmS1Ioa", 3076),
          ("es2Oc48Stm16PosS1Ioa", 3074),
          ("es2RedundancyS1Ioa", 3077),
          ("es2ServiceS1Ioa", 3075),
          ("es2dash10GePrS2Ioa", 3082),
          ("es2dash10GeS1Ioa", 3080),
          ("unknown", 0))
    )



class JuniSystemSlotLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class JuniSystemSlotType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("erxLcIoaSlot", 4),
          ("erxLcmSlot", 2),
          ("erxSrpIoaSlot", 3),
          ("erxSrpSlot", 1),
          ("es2FIoaSlot", 20),
          ("es2FmSlot", 18),
          ("es2SfsSlot", 17),
          ("es2SrpIoaSlot", 19),
          ("es2SrpSlot", 16),
          ("noSlot", 0))
    )



class JuniSystemTimingSelector(Integer32, TextualConvention):
    status = "current"
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
        *(("error", 4),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )



class JuniSystemLocationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slot", 2),
          ("system", 1))
    )



class JuniSystemLocation(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class JuniSystemTaskName(OctetString, TextualConvention):
    status = "current"
    displayHint = "100a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )



# MIB Managed Objects in the order of their OIDs

_JuniSystemTrap_ObjectIdentity = ObjectIdentity
juniSystemTrap = _JuniSystemTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0)
)
_JuniSystemObjects_ObjectIdentity = ObjectIdentity
juniSystemObjects = _JuniSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1)
)
_JuniSystemGeneral_ObjectIdentity = ObjectIdentity
juniSystemGeneral = _JuniSystemGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1)
)
_JuniSystemSwVersion_Type = DisplayString
_JuniSystemSwVersion_Object = MibScalar
juniSystemSwVersion = _JuniSystemSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 1),
    _JuniSystemSwVersion_Type()
)
juniSystemSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemSwVersion.setStatus("current")
_JuniSystemSwBuildDate_Type = DisplayString
_JuniSystemSwBuildDate_Object = MibScalar
juniSystemSwBuildDate = _JuniSystemSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 2),
    _JuniSystemSwBuildDate_Type()
)
juniSystemSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemSwBuildDate.setStatus("current")


class _JuniSystemMemUtilPct_Type(Integer32):
    """Custom type juniSystemMemUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniSystemMemUtilPct_Type.__name__ = "Integer32"
_JuniSystemMemUtilPct_Object = MibScalar
juniSystemMemUtilPct = _JuniSystemMemUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 3),
    _JuniSystemMemUtilPct_Type()
)
juniSystemMemUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemMemUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemMemUtilPct.setUnits("percent")


class _JuniSystemMemCapacity_Type(Integer32):
    """Custom type juniSystemMemCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JuniSystemMemCapacity_Type.__name__ = "Integer32"
_JuniSystemMemCapacity_Object = MibScalar
juniSystemMemCapacity = _JuniSystemMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 4),
    _JuniSystemMemCapacity_Type()
)
juniSystemMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemMemCapacity.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemMemCapacity.setUnits("bytes")


class _JuniSystemHighMemUtilThreshold_Type(Integer32):
    """Custom type juniSystemHighMemUtilThreshold based on Integer32"""
    defaultValue = 85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_JuniSystemHighMemUtilThreshold_Type.__name__ = "Integer32"
_JuniSystemHighMemUtilThreshold_Object = MibScalar
juniSystemHighMemUtilThreshold = _JuniSystemHighMemUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 5),
    _JuniSystemHighMemUtilThreshold_Type()
)
juniSystemHighMemUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemHighMemUtilThreshold.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemHighMemUtilThreshold.setUnits("percent")


class _JuniSystemAbatedMemUtilThreshold_Type(Integer32):
    """Custom type juniSystemAbatedMemUtilThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 98),
    )


_JuniSystemAbatedMemUtilThreshold_Type.__name__ = "Integer32"
_JuniSystemAbatedMemUtilThreshold_Object = MibScalar
juniSystemAbatedMemUtilThreshold = _JuniSystemAbatedMemUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 6),
    _JuniSystemAbatedMemUtilThreshold_Type()
)
juniSystemAbatedMemUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemAbatedMemUtilThreshold.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemAbatedMemUtilThreshold.setUnits("percent")


class _JuniSystemBootConfigControl_Type(Integer32):
    """Custom type juniSystemBootConfigControl based on Integer32"""
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
        *(("factoryDefaults", 2),
          ("file", 0),
          ("fileOnce", 1),
          ("runningConfiguration", 3))
    )


_JuniSystemBootConfigControl_Type.__name__ = "Integer32"
_JuniSystemBootConfigControl_Object = MibScalar
juniSystemBootConfigControl = _JuniSystemBootConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 7),
    _JuniSystemBootConfigControl_Type()
)
juniSystemBootConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootConfigControl.setStatus("current")


class _JuniSystemBootBackupConfigControl_Type(Integer32):
    """Custom type juniSystemBootBackupConfigControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefaults", 1),
          ("file", 0),
          ("none", 2))
    )


_JuniSystemBootBackupConfigControl_Type.__name__ = "Integer32"
_JuniSystemBootBackupConfigControl_Object = MibScalar
juniSystemBootBackupConfigControl = _JuniSystemBootBackupConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 8),
    _JuniSystemBootBackupConfigControl_Type()
)
juniSystemBootBackupConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootBackupConfigControl.setStatus("current")


class _JuniSystemBootForceBackupControl_Type(Integer32):
    """Custom type juniSystemBootForceBackupControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_JuniSystemBootForceBackupControl_Type.__name__ = "Integer32"
_JuniSystemBootForceBackupControl_Object = MibScalar
juniSystemBootForceBackupControl = _JuniSystemBootForceBackupControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 9),
    _JuniSystemBootForceBackupControl_Type()
)
juniSystemBootForceBackupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootForceBackupControl.setStatus("current")


class _JuniSystemBootAutoRevertControl_Type(Integer32):
    """Custom type juniSystemBootAutoRevertControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("never", 1),
          ("set", 2))
    )


_JuniSystemBootAutoRevertControl_Type.__name__ = "Integer32"
_JuniSystemBootAutoRevertControl_Object = MibScalar
juniSystemBootAutoRevertControl = _JuniSystemBootAutoRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 10),
    _JuniSystemBootAutoRevertControl_Type()
)
juniSystemBootAutoRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootAutoRevertControl.setStatus("current")


class _JuniSystemBootAutoRevertCountTolerance_Type(Unsigned32):
    """Custom type juniSystemBootAutoRevertCountTolerance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_JuniSystemBootAutoRevertCountTolerance_Type.__name__ = "Unsigned32"
_JuniSystemBootAutoRevertCountTolerance_Object = MibScalar
juniSystemBootAutoRevertCountTolerance = _JuniSystemBootAutoRevertCountTolerance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 11),
    _JuniSystemBootAutoRevertCountTolerance_Type()
)
juniSystemBootAutoRevertCountTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootAutoRevertCountTolerance.setStatus("current")


class _JuniSystemBootAutoRevertTimeTolerance_Type(Unsigned32):
    """Custom type juniSystemBootAutoRevertTimeTolerance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_JuniSystemBootAutoRevertTimeTolerance_Type.__name__ = "Unsigned32"
_JuniSystemBootAutoRevertTimeTolerance_Object = MibScalar
juniSystemBootAutoRevertTimeTolerance = _JuniSystemBootAutoRevertTimeTolerance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 12),
    _JuniSystemBootAutoRevertTimeTolerance_Type()
)
juniSystemBootAutoRevertTimeTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootAutoRevertTimeTolerance.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemBootAutoRevertTimeTolerance.setUnits("seconds")


class _JuniSystemBootReleaseFile_Type(DisplayString):
    """Custom type juniSystemBootReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemBootReleaseFile_Type.__name__ = "DisplayString"
_JuniSystemBootReleaseFile_Object = MibScalar
juniSystemBootReleaseFile = _JuniSystemBootReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 13),
    _JuniSystemBootReleaseFile_Type()
)
juniSystemBootReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootReleaseFile.setStatus("current")


class _JuniSystemBootConfigFile_Type(DisplayString):
    """Custom type juniSystemBootConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemBootConfigFile_Type.__name__ = "DisplayString"
_JuniSystemBootConfigFile_Object = MibScalar
juniSystemBootConfigFile = _JuniSystemBootConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 14),
    _JuniSystemBootConfigFile_Type()
)
juniSystemBootConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootConfigFile.setStatus("current")


class _JuniSystemBootBackupReleaseFile_Type(DisplayString):
    """Custom type juniSystemBootBackupReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemBootBackupReleaseFile_Type.__name__ = "DisplayString"
_JuniSystemBootBackupReleaseFile_Object = MibScalar
juniSystemBootBackupReleaseFile = _JuniSystemBootBackupReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 15),
    _JuniSystemBootBackupReleaseFile_Type()
)
juniSystemBootBackupReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootBackupReleaseFile.setStatus("current")


class _JuniSystemBootBackupConfigFile_Type(DisplayString):
    """Custom type juniSystemBootBackupConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemBootBackupConfigFile_Type.__name__ = "DisplayString"
_JuniSystemBootBackupConfigFile_Object = MibScalar
juniSystemBootBackupConfigFile = _JuniSystemBootBackupConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 16),
    _JuniSystemBootBackupConfigFile_Type()
)
juniSystemBootBackupConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemBootBackupConfigFile.setStatus("current")


class _JuniSystemRedundancyRevertControl_Type(Integer32):
    """Custom type juniSystemRedundancyRevertControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("off", 0),
          ("timeOfDay", 2))
    )


_JuniSystemRedundancyRevertControl_Type.__name__ = "Integer32"
_JuniSystemRedundancyRevertControl_Object = MibScalar
juniSystemRedundancyRevertControl = _JuniSystemRedundancyRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 17),
    _JuniSystemRedundancyRevertControl_Type()
)
juniSystemRedundancyRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemRedundancyRevertControl.setStatus("current")


class _JuniSystemRedundancyRevertTimeOfDay_Type(Integer32):
    """Custom type juniSystemRedundancyRevertTimeOfDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_JuniSystemRedundancyRevertTimeOfDay_Type.__name__ = "Integer32"
_JuniSystemRedundancyRevertTimeOfDay_Object = MibScalar
juniSystemRedundancyRevertTimeOfDay = _JuniSystemRedundancyRevertTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 18),
    _JuniSystemRedundancyRevertTimeOfDay_Type()
)
juniSystemRedundancyRevertTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemRedundancyRevertTimeOfDay.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemRedundancyRevertTimeOfDay.setUnits("seconds")


class _JuniSystemMemUtilTrapEnable_Type(TruthValue):
    """Custom type juniSystemMemUtilTrapEnable based on TruthValue"""


_JuniSystemMemUtilTrapEnable_Object = MibScalar
juniSystemMemUtilTrapEnable = _JuniSystemMemUtilTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 19),
    _JuniSystemMemUtilTrapEnable_Type()
)
juniSystemMemUtilTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemMemUtilTrapEnable.setStatus("current")


class _JuniSystemReloadSlotNumber_Type(Integer32):
    """Custom type juniSystemReloadSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniSystemReloadSlotNumber_Type.__name__ = "Integer32"
_JuniSystemReloadSlotNumber_Object = MibScalar
juniSystemReloadSlotNumber = _JuniSystemReloadSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 20),
    _JuniSystemReloadSlotNumber_Type()
)
juniSystemReloadSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSystemReloadSlotNumber.setStatus("current")


class _JuniSystemUtilizationThresholdDirection_Type(Integer32):
    """Custom type juniSystemUtilizationThresholdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("falling", 2),
          ("rising", 1))
    )


_JuniSystemUtilizationThresholdDirection_Type.__name__ = "Integer32"
_JuniSystemUtilizationThresholdDirection_Object = MibScalar
juniSystemUtilizationThresholdDirection = _JuniSystemUtilizationThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 21),
    _JuniSystemUtilizationThresholdDirection_Type()
)
juniSystemUtilizationThresholdDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSystemUtilizationThresholdDirection.setStatus("current")


class _JuniSystemUtilizationTrapEnable_Type(TruthValue):
    """Custom type juniSystemUtilizationTrapEnable based on TruthValue"""


_JuniSystemUtilizationTrapEnable_Object = MibScalar
juniSystemUtilizationTrapEnable = _JuniSystemUtilizationTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 22),
    _JuniSystemUtilizationTrapEnable_Type()
)
juniSystemUtilizationTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemUtilizationTrapEnable.setStatus("current")
_JuniSystemMemKBytesCapacity_Type = KBytes
_JuniSystemMemKBytesCapacity_Object = MibScalar
juniSystemMemKBytesCapacity = _JuniSystemMemKBytesCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 23),
    _JuniSystemMemKBytesCapacity_Type()
)
juniSystemMemKBytesCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemMemKBytesCapacity.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemMemKBytesCapacity.setUnits("KBytes")
_JuniSystemPortSfpPowerThresholdIfIndex_Type = Unsigned32
_JuniSystemPortSfpPowerThresholdIfIndex_Object = MibScalar
juniSystemPortSfpPowerThresholdIfIndex = _JuniSystemPortSfpPowerThresholdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 24),
    _JuniSystemPortSfpPowerThresholdIfIndex_Type()
)
juniSystemPortSfpPowerThresholdIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSystemPortSfpPowerThresholdIfIndex.setStatus("current")


class _JuniSystemPortSfpPowerThresholdValue_Type(OctetString):
    """Custom type juniSystemPortSfpPowerThresholdValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniSystemPortSfpPowerThresholdValue_Type.__name__ = "OctetString"
_JuniSystemPortSfpPowerThresholdValue_Object = MibScalar
juniSystemPortSfpPowerThresholdValue = _JuniSystemPortSfpPowerThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 1, 25),
    _JuniSystemPortSfpPowerThresholdValue_Type()
)
juniSystemPortSfpPowerThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSystemPortSfpPowerThresholdValue.setStatus("current")
_JuniSystemSubsystem_ObjectIdentity = ObjectIdentity
juniSystemSubsystem = _JuniSystemSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 2)
)
_JuniSystemSubsystemTable_Object = MibTable
juniSystemSubsystemTable = _JuniSystemSubsystemTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniSystemSubsystemTable.setStatus("current")
_JuniSystemSubsystemEntry_Object = MibTableRow
juniSystemSubsystemEntry = _JuniSystemSubsystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 2, 1, 1)
)
juniSystemSubsystemEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemSubsystemIndex"),
)
if mibBuilder.loadTexts:
    juniSystemSubsystemEntry.setStatus("current")


class _JuniSystemSubsystemIndex_Type(Integer32):
    """Custom type juniSystemSubsystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemSubsystemIndex_Type.__name__ = "Integer32"
_JuniSystemSubsystemIndex_Object = MibTableColumn
juniSystemSubsystemIndex = _JuniSystemSubsystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 2, 1, 1, 1),
    _JuniSystemSubsystemIndex_Type()
)
juniSystemSubsystemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemSubsystemIndex.setStatus("current")


class _JuniSystemSubsystemName_Type(DisplayString):
    """Custom type juniSystemSubsystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemSubsystemName_Type.__name__ = "DisplayString"
_JuniSystemSubsystemName_Object = MibTableColumn
juniSystemSubsystemName = _JuniSystemSubsystemName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 2, 1, 1, 2),
    _JuniSystemSubsystemName_Type()
)
juniSystemSubsystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemSubsystemName.setStatus("current")


class _JuniSystemSubsystemBootReleaseFile_Type(DisplayString):
    """Custom type juniSystemSubsystemBootReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemSubsystemBootReleaseFile_Type.__name__ = "DisplayString"
_JuniSystemSubsystemBootReleaseFile_Object = MibTableColumn
juniSystemSubsystemBootReleaseFile = _JuniSystemSubsystemBootReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 2, 1, 1, 3),
    _JuniSystemSubsystemBootReleaseFile_Type()
)
juniSystemSubsystemBootReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemSubsystemBootReleaseFile.setStatus("current")


class _JuniSystemSubsystemBootBackupReleaseFile_Type(DisplayString):
    """Custom type juniSystemSubsystemBootBackupReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemSubsystemBootBackupReleaseFile_Type.__name__ = "DisplayString"
_JuniSystemSubsystemBootBackupReleaseFile_Object = MibTableColumn
juniSystemSubsystemBootBackupReleaseFile = _JuniSystemSubsystemBootBackupReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 2, 1, 1, 4),
    _JuniSystemSubsystemBootBackupReleaseFile_Type()
)
juniSystemSubsystemBootBackupReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemSubsystemBootBackupReleaseFile.setStatus("current")
_JuniSystemModule_ObjectIdentity = ObjectIdentity
juniSystemModule = _JuniSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3)
)


class _JuniSystemMaxSlotNumber_Type(Integer32):
    """Custom type juniSystemMaxSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniSystemMaxSlotNumber_Type.__name__ = "Integer32"
_JuniSystemMaxSlotNumber_Object = MibScalar
juniSystemMaxSlotNumber = _JuniSystemMaxSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 1),
    _JuniSystemMaxSlotNumber_Type()
)
juniSystemMaxSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemMaxSlotNumber.setStatus("current")


class _JuniSystemMaxModulesPerSlot_Type(Integer32):
    """Custom type juniSystemMaxModulesPerSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemMaxModulesPerSlot_Type.__name__ = "Integer32"
_JuniSystemMaxModulesPerSlot_Object = MibScalar
juniSystemMaxModulesPerSlot = _JuniSystemMaxModulesPerSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 2),
    _JuniSystemMaxModulesPerSlot_Type()
)
juniSystemMaxModulesPerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemMaxModulesPerSlot.setStatus("current")
_JuniSystemSlotTable_Object = MibTable
juniSystemSlotTable = _JuniSystemSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    juniSystemSlotTable.setStatus("current")
_JuniSystemSlotEntry_Object = MibTableRow
juniSystemSlotEntry = _JuniSystemSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 3, 1)
)
juniSystemSlotEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemSlotNumber"),
    (0, "Juniper-System-MIB", "juniSystemSlotLevel"),
)
if mibBuilder.loadTexts:
    juniSystemSlotEntry.setStatus("current")


class _JuniSystemSlotNumber_Type(Integer32):
    """Custom type juniSystemSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniSystemSlotNumber_Type.__name__ = "Integer32"
_JuniSystemSlotNumber_Object = MibTableColumn
juniSystemSlotNumber = _JuniSystemSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 3, 1, 1),
    _JuniSystemSlotNumber_Type()
)
juniSystemSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemSlotNumber.setStatus("current")
_JuniSystemSlotLevel_Type = JuniSystemSlotLevel
_JuniSystemSlotLevel_Object = MibTableColumn
juniSystemSlotLevel = _JuniSystemSlotLevel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 3, 1, 2),
    _JuniSystemSlotLevel_Type()
)
juniSystemSlotLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemSlotLevel.setStatus("current")


class _JuniSystemSlotStatus_Type(Integer32):
    """Custom type juniSystemSlotStatus based on Integer32"""
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
        *(("empty", 2),
          ("moduleNotPresent", 3),
          ("modulePresent", 4),
          ("noSlotContainer", 1),
          ("unknown", 0))
    )


_JuniSystemSlotStatus_Type.__name__ = "Integer32"
_JuniSystemSlotStatus_Object = MibTableColumn
juniSystemSlotStatus = _JuniSystemSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 3, 1, 3),
    _JuniSystemSlotStatus_Type()
)
juniSystemSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemSlotStatus.setStatus("current")
_JuniSystemSlotType_Type = JuniSystemSlotType
_JuniSystemSlotType_Object = MibTableColumn
juniSystemSlotType = _JuniSystemSlotType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 3, 1, 4),
    _JuniSystemSlotType_Type()
)
juniSystemSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemSlotType.setStatus("current")
_JuniSystemModuleTable_Object = MibTable
juniSystemModuleTable = _JuniSystemModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    juniSystemModuleTable.setStatus("current")
_JuniSystemModuleEntry_Object = MibTableRow
juniSystemModuleEntry = _JuniSystemModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1)
)
juniSystemModuleEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemSlotNumber"),
    (0, "Juniper-System-MIB", "juniSystemSlotLevel"),
)
if mibBuilder.loadTexts:
    juniSystemModuleEntry.setStatus("current")


class _JuniSystemModuleOperStatus_Type(Integer32):
    """Custom type juniSystemModuleOperStatus based on Integer32"""
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
        *(("booting", 4),
          ("disabled", 2),
          ("hardwareError", 3),
          ("inactive", 8),
          ("initializing", 5),
          ("notPresent", 1),
          ("notResponding", 9),
          ("online", 6),
          ("standby", 7),
          ("unknown", 0))
    )


_JuniSystemModuleOperStatus_Type.__name__ = "Integer32"
_JuniSystemModuleOperStatus_Object = MibTableColumn
juniSystemModuleOperStatus = _JuniSystemModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 1),
    _JuniSystemModuleOperStatus_Type()
)
juniSystemModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleOperStatus.setStatus("current")


class _JuniSystemModuleDisableReason_Type(Integer32):
    """Custom type juniSystemModuleDisableReason based on Integer32"""
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
        *(("admin", 3),
          ("assessing", 2),
          ("fabricLimit", 5),
          ("imageError", 6),
          ("none", 0),
          ("typeMismatch", 4),
          ("unknown", 1))
    )


_JuniSystemModuleDisableReason_Type.__name__ = "Integer32"
_JuniSystemModuleDisableReason_Object = MibTableColumn
juniSystemModuleDisableReason = _JuniSystemModuleDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 2),
    _JuniSystemModuleDisableReason_Type()
)
juniSystemModuleDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleDisableReason.setStatus("current")
_JuniSystemModuleLastChange_Type = TimeTicks
_JuniSystemModuleLastChange_Object = MibTableColumn
juniSystemModuleLastChange = _JuniSystemModuleLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 3),
    _JuniSystemModuleLastChange_Type()
)
juniSystemModuleLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleLastChange.setStatus("current")
_JuniSystemModuleCurrentType_Type = JuniSystemModuleType
_JuniSystemModuleCurrentType_Object = MibTableColumn
juniSystemModuleCurrentType = _JuniSystemModuleCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 4),
    _JuniSystemModuleCurrentType_Type()
)
juniSystemModuleCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleCurrentType.setStatus("current")
_JuniSystemModuleExpectedType_Type = JuniSystemModuleType
_JuniSystemModuleExpectedType_Object = MibTableColumn
juniSystemModuleExpectedType = _JuniSystemModuleExpectedType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 5),
    _JuniSystemModuleExpectedType_Type()
)
juniSystemModuleExpectedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleExpectedType.setStatus("current")


class _JuniSystemModuleDescr_Type(DisplayString):
    """Custom type juniSystemModuleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JuniSystemModuleDescr_Type.__name__ = "DisplayString"
_JuniSystemModuleDescr_Object = MibTableColumn
juniSystemModuleDescr = _JuniSystemModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 6),
    _JuniSystemModuleDescr_Type()
)
juniSystemModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleDescr.setStatus("current")


class _JuniSystemModuleSlotSpan_Type(Integer32):
    """Custom type juniSystemModuleSlotSpan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemModuleSlotSpan_Type.__name__ = "Integer32"
_JuniSystemModuleSlotSpan_Object = MibTableColumn
juniSystemModuleSlotSpan = _JuniSystemModuleSlotSpan_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 7),
    _JuniSystemModuleSlotSpan_Type()
)
juniSystemModuleSlotSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleSlotSpan.setStatus("current")
_JuniSystemModulePortCount_Type = Integer32
_JuniSystemModulePortCount_Object = MibTableColumn
juniSystemModulePortCount = _JuniSystemModulePortCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 8),
    _JuniSystemModulePortCount_Type()
)
juniSystemModulePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModulePortCount.setStatus("current")


class _JuniSystemModuleSerialNumber_Type(DisplayString):
    """Custom type juniSystemModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniSystemModuleSerialNumber_Type.__name__ = "DisplayString"
_JuniSystemModuleSerialNumber_Object = MibTableColumn
juniSystemModuleSerialNumber = _JuniSystemModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 9),
    _JuniSystemModuleSerialNumber_Type()
)
juniSystemModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleSerialNumber.setStatus("current")


class _JuniSystemModuleAssemblyPartNumber_Type(DisplayString):
    """Custom type juniSystemModuleAssemblyPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniSystemModuleAssemblyPartNumber_Type.__name__ = "DisplayString"
_JuniSystemModuleAssemblyPartNumber_Object = MibTableColumn
juniSystemModuleAssemblyPartNumber = _JuniSystemModuleAssemblyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 10),
    _JuniSystemModuleAssemblyPartNumber_Type()
)
juniSystemModuleAssemblyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleAssemblyPartNumber.setStatus("current")


class _JuniSystemModuleAssemblyRev_Type(DisplayString):
    """Custom type juniSystemModuleAssemblyRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_JuniSystemModuleAssemblyRev_Type.__name__ = "DisplayString"
_JuniSystemModuleAssemblyRev_Object = MibTableColumn
juniSystemModuleAssemblyRev = _JuniSystemModuleAssemblyRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 11),
    _JuniSystemModuleAssemblyRev_Type()
)
juniSystemModuleAssemblyRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleAssemblyRev.setStatus("current")
_JuniSystemModulePhysicalIndex_Type = PhysicalIndex
_JuniSystemModulePhysicalIndex_Object = MibTableColumn
juniSystemModulePhysicalIndex = _JuniSystemModulePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 12),
    _JuniSystemModulePhysicalIndex_Type()
)
juniSystemModulePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModulePhysicalIndex.setStatus("current")
_JuniSystemModuleSoftwareSupport_Type = TruthValue
_JuniSystemModuleSoftwareSupport_Object = MibTableColumn
juniSystemModuleSoftwareSupport = _JuniSystemModuleSoftwareSupport_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 13),
    _JuniSystemModuleSoftwareSupport_Type()
)
juniSystemModuleSoftwareSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleSoftwareSupport.setStatus("current")
_JuniSystemModuleRedundancySupport_Type = TruthValue
_JuniSystemModuleRedundancySupport_Object = MibTableColumn
juniSystemModuleRedundancySupport = _JuniSystemModuleRedundancySupport_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 14),
    _JuniSystemModuleRedundancySupport_Type()
)
juniSystemModuleRedundancySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleRedundancySupport.setStatus("current")


class _JuniSystemModuleLevelSpan_Type(Integer32):
    """Custom type juniSystemModuleLevelSpan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemModuleLevelSpan_Type.__name__ = "Integer32"
_JuniSystemModuleLevelSpan_Object = MibTableColumn
juniSystemModuleLevelSpan = _JuniSystemModuleLevelSpan_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 4, 1, 15),
    _JuniSystemModuleLevelSpan_Type()
)
juniSystemModuleLevelSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleLevelSpan.setStatus("current")
_JuniSystemModuleSoftwareTable_Object = MibTable
juniSystemModuleSoftwareTable = _JuniSystemModuleSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    juniSystemModuleSoftwareTable.setStatus("current")
_JuniSystemModuleSoftwareEntry_Object = MibTableRow
juniSystemModuleSoftwareEntry = _JuniSystemModuleSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1)
)
juniSystemModuleSoftwareEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemSlotNumber"),
    (0, "Juniper-System-MIB", "juniSystemSlotLevel"),
)
if mibBuilder.loadTexts:
    juniSystemModuleSoftwareEntry.setStatus("current")
_JuniSystemModuleSoftwareVersion_Type = DisplayString
_JuniSystemModuleSoftwareVersion_Object = MibTableColumn
juniSystemModuleSoftwareVersion = _JuniSystemModuleSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 2),
    _JuniSystemModuleSoftwareVersion_Type()
)
juniSystemModuleSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleSoftwareVersion.setStatus("current")


class _JuniSystemModuleCpuUtilPct_Type(Integer32):
    """Custom type juniSystemModuleCpuUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniSystemModuleCpuUtilPct_Type.__name__ = "Integer32"
_JuniSystemModuleCpuUtilPct_Object = MibTableColumn
juniSystemModuleCpuUtilPct = _JuniSystemModuleCpuUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 3),
    _JuniSystemModuleCpuUtilPct_Type()
)
juniSystemModuleCpuUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleCpuUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemModuleCpuUtilPct.setUnits("percent")


class _JuniSystemModuleMemUtilPct_Type(Integer32):
    """Custom type juniSystemModuleMemUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniSystemModuleMemUtilPct_Type.__name__ = "Integer32"
_JuniSystemModuleMemUtilPct_Object = MibTableColumn
juniSystemModuleMemUtilPct = _JuniSystemModuleMemUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 4),
    _JuniSystemModuleMemUtilPct_Type()
)
juniSystemModuleMemUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleMemUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemModuleMemUtilPct.setUnits("percent")
_JuniSystemModuleAdminStatus_Type = JuniEnable
_JuniSystemModuleAdminStatus_Object = MibTableColumn
juniSystemModuleAdminStatus = _JuniSystemModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 5),
    _JuniSystemModuleAdminStatus_Type()
)
juniSystemModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemModuleAdminStatus.setStatus("current")


class _JuniSystemModuleControl_Type(Integer32):
    """Custom type juniSystemModuleControl based on Integer32"""
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
        *(("flush", 1),
          ("noOperation", 0),
          ("reset", 2),
          ("resetBackup", 3))
    )


_JuniSystemModuleControl_Type.__name__ = "Integer32"
_JuniSystemModuleControl_Object = MibTableColumn
juniSystemModuleControl = _JuniSystemModuleControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 6),
    _JuniSystemModuleControl_Type()
)
juniSystemModuleControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemModuleControl.setStatus("current")


class _JuniSystemModuleBootReleaseFile_Type(DisplayString):
    """Custom type juniSystemModuleBootReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemModuleBootReleaseFile_Type.__name__ = "DisplayString"
_JuniSystemModuleBootReleaseFile_Object = MibTableColumn
juniSystemModuleBootReleaseFile = _JuniSystemModuleBootReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 7),
    _JuniSystemModuleBootReleaseFile_Type()
)
juniSystemModuleBootReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemModuleBootReleaseFile.setStatus("current")


class _JuniSystemModuleBootBackupReleaseFile_Type(DisplayString):
    """Custom type juniSystemModuleBootBackupReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemModuleBootBackupReleaseFile_Type.__name__ = "DisplayString"
_JuniSystemModuleBootBackupReleaseFile_Object = MibTableColumn
juniSystemModuleBootBackupReleaseFile = _JuniSystemModuleBootBackupReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 8),
    _JuniSystemModuleBootBackupReleaseFile_Type()
)
juniSystemModuleBootBackupReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemModuleBootBackupReleaseFile.setStatus("current")


class _JuniSystemModuleCpuFiveSecUtilPct_Type(Integer32):
    """Custom type juniSystemModuleCpuFiveSecUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniSystemModuleCpuFiveSecUtilPct_Type.__name__ = "Integer32"
_JuniSystemModuleCpuFiveSecUtilPct_Object = MibTableColumn
juniSystemModuleCpuFiveSecUtilPct = _JuniSystemModuleCpuFiveSecUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 9),
    _JuniSystemModuleCpuFiveSecUtilPct_Type()
)
juniSystemModuleCpuFiveSecUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleCpuFiveSecUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemModuleCpuFiveSecUtilPct.setUnits("percent")


class _JuniSystemModuleCpuOneMinAvgPct_Type(Integer32):
    """Custom type juniSystemModuleCpuOneMinAvgPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniSystemModuleCpuOneMinAvgPct_Type.__name__ = "Integer32"
_JuniSystemModuleCpuOneMinAvgPct_Object = MibTableColumn
juniSystemModuleCpuOneMinAvgPct = _JuniSystemModuleCpuOneMinAvgPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 10),
    _JuniSystemModuleCpuOneMinAvgPct_Type()
)
juniSystemModuleCpuOneMinAvgPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleCpuOneMinAvgPct.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemModuleCpuOneMinAvgPct.setUnits("percent")


class _JuniSystemModuleCpuFiveMinAvgPct_Type(Integer32):
    """Custom type juniSystemModuleCpuFiveMinAvgPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniSystemModuleCpuFiveMinAvgPct_Type.__name__ = "Integer32"
_JuniSystemModuleCpuFiveMinAvgPct_Object = MibTableColumn
juniSystemModuleCpuFiveMinAvgPct = _JuniSystemModuleCpuFiveMinAvgPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 5, 1, 11),
    _JuniSystemModuleCpuFiveMinAvgPct_Type()
)
juniSystemModuleCpuFiveMinAvgPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleCpuFiveMinAvgPct.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemModuleCpuFiveMinAvgPct.setUnits("percent")
_JuniSystemModuleRedundancyTable_Object = MibTable
juniSystemModuleRedundancyTable = _JuniSystemModuleRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    juniSystemModuleRedundancyTable.setStatus("current")
_JuniSystemModuleRedundancyEntry_Object = MibTableRow
juniSystemModuleRedundancyEntry = _JuniSystemModuleRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 6, 1)
)
juniSystemModuleRedundancyEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemSlotNumber"),
    (0, "Juniper-System-MIB", "juniSystemSlotLevel"),
)
if mibBuilder.loadTexts:
    juniSystemModuleRedundancyEntry.setStatus("current")
_JuniSystemModuleRedundancyGroupId_Type = Unsigned32
_JuniSystemModuleRedundancyGroupId_Object = MibTableColumn
juniSystemModuleRedundancyGroupId = _JuniSystemModuleRedundancyGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 6, 1, 1),
    _JuniSystemModuleRedundancyGroupId_Type()
)
juniSystemModuleRedundancyGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleRedundancyGroupId.setStatus("current")
_JuniSystemModuleRedundancySpare_Type = TruthValue
_JuniSystemModuleRedundancySpare_Object = MibTableColumn
juniSystemModuleRedundancySpare = _JuniSystemModuleRedundancySpare_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 6, 1, 2),
    _JuniSystemModuleRedundancySpare_Type()
)
juniSystemModuleRedundancySpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleRedundancySpare.setStatus("current")
_JuniSystemModuleRedundancyAssociatedSlot_Type = Integer32
_JuniSystemModuleRedundancyAssociatedSlot_Object = MibTableColumn
juniSystemModuleRedundancyAssociatedSlot = _JuniSystemModuleRedundancyAssociatedSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 6, 1, 3),
    _JuniSystemModuleRedundancyAssociatedSlot_Type()
)
juniSystemModuleRedundancyAssociatedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemModuleRedundancyAssociatedSlot.setStatus("current")
_JuniSystemModuleRedundancyLockout_Type = JuniEnable
_JuniSystemModuleRedundancyLockout_Object = MibTableColumn
juniSystemModuleRedundancyLockout = _JuniSystemModuleRedundancyLockout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 6, 1, 4),
    _JuniSystemModuleRedundancyLockout_Type()
)
juniSystemModuleRedundancyLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemModuleRedundancyLockout.setStatus("current")


class _JuniSystemModuleRedundancyRevertControl_Type(Integer32):
    """Custom type juniSystemModuleRedundancyRevertControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("off", 0),
          ("timeAndDate", 2))
    )


_JuniSystemModuleRedundancyRevertControl_Type.__name__ = "Integer32"
_JuniSystemModuleRedundancyRevertControl_Object = MibTableColumn
juniSystemModuleRedundancyRevertControl = _JuniSystemModuleRedundancyRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 6, 1, 5),
    _JuniSystemModuleRedundancyRevertControl_Type()
)
juniSystemModuleRedundancyRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemModuleRedundancyRevertControl.setStatus("current")


class _JuniSystemModuleRedundancyRevertTime_Type(DateAndTime):
    """Custom type juniSystemModuleRedundancyRevertTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniSystemModuleRedundancyRevertTime_Type.__name__ = "DateAndTime"
_JuniSystemModuleRedundancyRevertTime_Object = MibTableColumn
juniSystemModuleRedundancyRevertTime = _JuniSystemModuleRedundancyRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 3, 6, 1, 6),
    _JuniSystemModuleRedundancyRevertTime_Type()
)
juniSystemModuleRedundancyRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemModuleRedundancyRevertTime.setStatus("current")
_JuniSystemPort_ObjectIdentity = ObjectIdentity
juniSystemPort = _JuniSystemPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 4)
)
_JuniSystemPortTable_Object = MibTable
juniSystemPortTable = _JuniSystemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    juniSystemPortTable.setStatus("current")
_JuniSystemPortEntry_Object = MibTableRow
juniSystemPortEntry = _JuniSystemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 4, 1, 1)
)
juniSystemPortEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemSlotNumber"),
    (0, "Juniper-System-MIB", "juniSystemSlotLevel"),
    (0, "Juniper-System-MIB", "juniSystemPortNumber"),
)
if mibBuilder.loadTexts:
    juniSystemPortEntry.setStatus("current")


class _JuniSystemPortNumber_Type(Integer32):
    """Custom type juniSystemPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniSystemPortNumber_Type.__name__ = "Integer32"
_JuniSystemPortNumber_Object = MibTableColumn
juniSystemPortNumber = _JuniSystemPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 4, 1, 1, 1),
    _JuniSystemPortNumber_Type()
)
juniSystemPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemPortNumber.setStatus("current")
_JuniSystemPortIfIndex_Type = InterfaceIndexOrZero
_JuniSystemPortIfIndex_Object = MibTableColumn
juniSystemPortIfIndex = _JuniSystemPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 4, 1, 1, 2),
    _JuniSystemPortIfIndex_Type()
)
juniSystemPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemPortIfIndex.setStatus("current")
_JuniSystemPortPhysicalIndex_Type = PhysicalIndex
_JuniSystemPortPhysicalIndex_Object = MibTableColumn
juniSystemPortPhysicalIndex = _JuniSystemPortPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 4, 1, 1, 3),
    _JuniSystemPortPhysicalIndex_Type()
)
juniSystemPortPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemPortPhysicalIndex.setStatus("current")
_JuniSystemTiming_ObjectIdentity = ObjectIdentity
juniSystemTiming = _JuniSystemTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5)
)
_JuniSystemAdminTimingSource_Type = JuniSystemTimingSelector
_JuniSystemAdminTimingSource_Object = MibScalar
juniSystemAdminTimingSource = _JuniSystemAdminTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 1),
    _JuniSystemAdminTimingSource_Type()
)
juniSystemAdminTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemAdminTimingSource.setStatus("current")
_JuniSystemOperTimingSource_Type = JuniSystemTimingSelector
_JuniSystemOperTimingSource_Object = MibScalar
juniSystemOperTimingSource = _JuniSystemOperTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 2),
    _JuniSystemOperTimingSource_Type()
)
juniSystemOperTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemOperTimingSource.setStatus("current")


class _JuniSystemTimingAutoUpgrade_Type(JuniEnable):
    """Custom type juniSystemTimingAutoUpgrade based on JuniEnable"""


_JuniSystemTimingAutoUpgrade_Object = MibScalar
juniSystemTimingAutoUpgrade = _JuniSystemTimingAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 3),
    _JuniSystemTimingAutoUpgrade_Type()
)
juniSystemTimingAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemTimingAutoUpgrade.setStatus("current")
_JuniSystemTimingSelectorTable_Object = MibTable
juniSystemTimingSelectorTable = _JuniSystemTimingSelectorTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    juniSystemTimingSelectorTable.setStatus("current")
_JuniSystemTimingSelectorEntry_Object = MibTableRow
juniSystemTimingSelectorEntry = _JuniSystemTimingSelectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 4, 1)
)
juniSystemTimingSelectorEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemTimingSelectorIndex"),
)
if mibBuilder.loadTexts:
    juniSystemTimingSelectorEntry.setStatus("current")
_JuniSystemTimingSelectorIndex_Type = JuniSystemTimingSelector
_JuniSystemTimingSelectorIndex_Object = MibTableColumn
juniSystemTimingSelectorIndex = _JuniSystemTimingSelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 4, 1, 1),
    _JuniSystemTimingSelectorIndex_Type()
)
juniSystemTimingSelectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemTimingSelectorIndex.setStatus("current")


class _JuniSystemTimingSourceType_Type(Integer32):
    """Custom type juniSystemTimingSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timingInterfaceIfIndex", 1),
          ("timingInternal", 2),
          ("timingLine", 3))
    )


_JuniSystemTimingSourceType_Type.__name__ = "Integer32"
_JuniSystemTimingSourceType_Object = MibTableColumn
juniSystemTimingSourceType = _JuniSystemTimingSourceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 4, 1, 2),
    _JuniSystemTimingSourceType_Type()
)
juniSystemTimingSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemTimingSourceType.setStatus("current")


class _JuniSystemTimingSourceIfIndex_Type(InterfaceIndexOrZero):
    """Custom type juniSystemTimingSourceIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_JuniSystemTimingSourceIfIndex_Object = MibTableColumn
juniSystemTimingSourceIfIndex = _JuniSystemTimingSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 4, 1, 3),
    _JuniSystemTimingSourceIfIndex_Type()
)
juniSystemTimingSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemTimingSourceIfIndex.setStatus("current")


class _JuniSystemTimingSourceLine_Type(Integer32):
    """Custom type juniSystemTimingSourceLine based on Integer32"""
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
        *(("timingSourceLineE1PortA", 1),
          ("timingSourceLineE1PortB", 2),
          ("timingSourceLineT1PortA", 3),
          ("timingSourceLineT1PortB", 4),
          ("timingSourceLineUndefined", 0))
    )


_JuniSystemTimingSourceLine_Type.__name__ = "Integer32"
_JuniSystemTimingSourceLine_Object = MibTableColumn
juniSystemTimingSourceLine = _JuniSystemTimingSourceLine_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 4, 1, 4),
    _JuniSystemTimingSourceLine_Type()
)
juniSystemTimingSourceLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemTimingSourceLine.setStatus("current")


class _JuniSystemTimingWorkingStatus_Type(Integer32):
    """Custom type juniSystemTimingWorkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timingStatusError", 2),
          ("timingStatusOk", 1),
          ("timingStatusUnknown", 3))
    )


_JuniSystemTimingWorkingStatus_Type.__name__ = "Integer32"
_JuniSystemTimingWorkingStatus_Object = MibTableColumn
juniSystemTimingWorkingStatus = _JuniSystemTimingWorkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 4, 1, 5),
    _JuniSystemTimingWorkingStatus_Type()
)
juniSystemTimingWorkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemTimingWorkingStatus.setStatus("current")


class _JuniSystemTimingProtectedStatus_Type(Integer32):
    """Custom type juniSystemTimingProtectedStatus based on Integer32"""
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
        *(("sourceNotProtected", 4),
          ("timingStatusError", 2),
          ("timingStatusOk", 1),
          ("timingStatusUnknown", 3))
    )


_JuniSystemTimingProtectedStatus_Type.__name__ = "Integer32"
_JuniSystemTimingProtectedStatus_Object = MibTableColumn
juniSystemTimingProtectedStatus = _JuniSystemTimingProtectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 5, 4, 1, 6),
    _JuniSystemTimingProtectedStatus_Type()
)
juniSystemTimingProtectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemTimingProtectedStatus.setStatus("current")
_JuniSystemFabric_ObjectIdentity = ObjectIdentity
juniSystemFabric = _JuniSystemFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 6)
)
_JuniSystemFabricSpeed_Type = Unsigned32
_JuniSystemFabricSpeed_Object = MibScalar
juniSystemFabricSpeed = _JuniSystemFabricSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 6, 1),
    _JuniSystemFabricSpeed_Type()
)
juniSystemFabricSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemFabricSpeed.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemFabricSpeed.setUnits("gigabits per second")


class _JuniSystemFabricRev_Type(DisplayString):
    """Custom type juniSystemFabricRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniSystemFabricRev_Type.__name__ = "DisplayString"
_JuniSystemFabricRev_Object = MibScalar
juniSystemFabricRev = _JuniSystemFabricRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 6, 2),
    _JuniSystemFabricRev_Type()
)
juniSystemFabricRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemFabricRev.setStatus("current")
_JuniSystemNvs_ObjectIdentity = ObjectIdentity
juniSystemNvs = _JuniSystemNvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 7)
)


class _JuniSystemNvsCount_Type(Integer32):
    """Custom type juniSystemNvsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemNvsCount_Type.__name__ = "Integer32"
_JuniSystemNvsCount_Object = MibScalar
juniSystemNvsCount = _JuniSystemNvsCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 7, 1),
    _JuniSystemNvsCount_Type()
)
juniSystemNvsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemNvsCount.setStatus("current")
_JuniSystemNvsTable_Object = MibTable
juniSystemNvsTable = _JuniSystemNvsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    juniSystemNvsTable.setStatus("current")
_JuniSystemNvsEntry_Object = MibTableRow
juniSystemNvsEntry = _JuniSystemNvsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 7, 2, 1)
)
juniSystemNvsEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemNvsIndex"),
)
if mibBuilder.loadTexts:
    juniSystemNvsEntry.setStatus("current")


class _JuniSystemNvsIndex_Type(Integer32):
    """Custom type juniSystemNvsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemNvsIndex_Type.__name__ = "Integer32"
_JuniSystemNvsIndex_Object = MibTableColumn
juniSystemNvsIndex = _JuniSystemNvsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 7, 2, 1, 1),
    _JuniSystemNvsIndex_Type()
)
juniSystemNvsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemNvsIndex.setStatus("current")


class _JuniSystemNvsStatus_Type(Integer32):
    """Custom type juniSystemNvsStatus based on Integer32"""
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
        *(("nearCapacity", 3),
          ("noConfigSpace", 5),
          ("notPresent", 0),
          ("ok", 4),
          ("volumeError", 2),
          ("writeProtected", 1))
    )


_JuniSystemNvsStatus_Type.__name__ = "Integer32"
_JuniSystemNvsStatus_Object = MibTableColumn
juniSystemNvsStatus = _JuniSystemNvsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 7, 2, 1, 2),
    _JuniSystemNvsStatus_Type()
)
juniSystemNvsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemNvsStatus.setStatus("current")
_JuniSystemNvsCapacity_Type = Unsigned32
_JuniSystemNvsCapacity_Object = MibTableColumn
juniSystemNvsCapacity = _JuniSystemNvsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 7, 2, 1, 3),
    _JuniSystemNvsCapacity_Type()
)
juniSystemNvsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemNvsCapacity.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemNvsCapacity.setUnits("megabytes")


class _JuniSystemNvsUtilPct_Type(Integer32):
    """Custom type juniSystemNvsUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniSystemNvsUtilPct_Type.__name__ = "Integer32"
_JuniSystemNvsUtilPct_Object = MibTableColumn
juniSystemNvsUtilPct = _JuniSystemNvsUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 7, 2, 1, 4),
    _JuniSystemNvsUtilPct_Type()
)
juniSystemNvsUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemNvsUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemNvsUtilPct.setUnits("percent")
_JuniSystemNvsPhysicalIndex_Type = PhysicalIndex
_JuniSystemNvsPhysicalIndex_Object = MibTableColumn
juniSystemNvsPhysicalIndex = _JuniSystemNvsPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 7, 2, 1, 5),
    _JuniSystemNvsPhysicalIndex_Type()
)
juniSystemNvsPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemNvsPhysicalIndex.setStatus("current")
_JuniSystemPower_ObjectIdentity = ObjectIdentity
juniSystemPower = _JuniSystemPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 8)
)


class _JuniSystemPowerCount_Type(Integer32):
    """Custom type juniSystemPowerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemPowerCount_Type.__name__ = "Integer32"
_JuniSystemPowerCount_Object = MibScalar
juniSystemPowerCount = _JuniSystemPowerCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 8, 1),
    _JuniSystemPowerCount_Type()
)
juniSystemPowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemPowerCount.setStatus("current")
_JuniSystemPowerTable_Object = MibTable
juniSystemPowerTable = _JuniSystemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    juniSystemPowerTable.setStatus("current")
_JuniSystemPowerEntry_Object = MibTableRow
juniSystemPowerEntry = _JuniSystemPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 8, 2, 1)
)
juniSystemPowerEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemPowerIndex"),
)
if mibBuilder.loadTexts:
    juniSystemPowerEntry.setStatus("current")


class _JuniSystemPowerIndex_Type(Integer32):
    """Custom type juniSystemPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemPowerIndex_Type.__name__ = "Integer32"
_JuniSystemPowerIndex_Object = MibTableColumn
juniSystemPowerIndex = _JuniSystemPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 8, 2, 1, 1),
    _JuniSystemPowerIndex_Type()
)
juniSystemPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemPowerIndex.setStatus("current")


class _JuniSystemPowerStatus_Type(Integer32):
    """Custom type juniSystemPowerStatus based on Integer32"""
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
        *(("failed", 3),
          ("good", 2),
          ("inactive", 1),
          ("notPresent", 0),
          ("sensorFailed", 4),
          ("unknown", 5))
    )


_JuniSystemPowerStatus_Type.__name__ = "Integer32"
_JuniSystemPowerStatus_Object = MibTableColumn
juniSystemPowerStatus = _JuniSystemPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 8, 2, 1, 2),
    _JuniSystemPowerStatus_Type()
)
juniSystemPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemPowerStatus.setStatus("current")
_JuniSystemPowerPhysicalIndex_Type = PhysicalIndex
_JuniSystemPowerPhysicalIndex_Object = MibTableColumn
juniSystemPowerPhysicalIndex = _JuniSystemPowerPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 8, 2, 1, 3),
    _JuniSystemPowerPhysicalIndex_Type()
)
juniSystemPowerPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemPowerPhysicalIndex.setStatus("current")
_JuniSystemTemperature_ObjectIdentity = ObjectIdentity
juniSystemTemperature = _JuniSystemTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9)
)


class _JuniSystemFanCount_Type(Integer32):
    """Custom type juniSystemFanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniSystemFanCount_Type.__name__ = "Integer32"
_JuniSystemFanCount_Object = MibScalar
juniSystemFanCount = _JuniSystemFanCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 1),
    _JuniSystemFanCount_Type()
)
juniSystemFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemFanCount.setStatus("current")
_JuniSystemFanTable_Object = MibTable
juniSystemFanTable = _JuniSystemFanTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    juniSystemFanTable.setStatus("current")
_JuniSystemFanEntry_Object = MibTableRow
juniSystemFanEntry = _JuniSystemFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 2, 1)
)
juniSystemFanEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemFanIndex"),
)
if mibBuilder.loadTexts:
    juniSystemFanEntry.setStatus("current")


class _JuniSystemFanIndex_Type(Integer32):
    """Custom type juniSystemFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemFanIndex_Type.__name__ = "Integer32"
_JuniSystemFanIndex_Object = MibTableColumn
juniSystemFanIndex = _JuniSystemFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 2, 1, 1),
    _JuniSystemFanIndex_Type()
)
juniSystemFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemFanIndex.setStatus("current")


class _JuniSystemFanStatus_Type(Integer32):
    """Custom type juniSystemFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1),
          ("warning", 2))
    )


_JuniSystemFanStatus_Type.__name__ = "Integer32"
_JuniSystemFanStatus_Object = MibTableColumn
juniSystemFanStatus = _JuniSystemFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 2, 1, 2),
    _JuniSystemFanStatus_Type()
)
juniSystemFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemFanStatus.setStatus("current")
_JuniSystemFanPhysicalIndex_Type = PhysicalIndex
_JuniSystemFanPhysicalIndex_Object = MibTableColumn
juniSystemFanPhysicalIndex = _JuniSystemFanPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 2, 1, 3),
    _JuniSystemFanPhysicalIndex_Type()
)
juniSystemFanPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemFanPhysicalIndex.setStatus("current")


class _JuniSystemTempCount_Type(Integer32):
    """Custom type juniSystemTempCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniSystemTempCount_Type.__name__ = "Integer32"
_JuniSystemTempCount_Object = MibScalar
juniSystemTempCount = _JuniSystemTempCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 3),
    _JuniSystemTempCount_Type()
)
juniSystemTempCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemTempCount.setStatus("current")
_JuniSystemTempTable_Object = MibTable
juniSystemTempTable = _JuniSystemTempTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 4)
)
if mibBuilder.loadTexts:
    juniSystemTempTable.setStatus("current")
_JuniSystemTempEntry_Object = MibTableRow
juniSystemTempEntry = _JuniSystemTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 4, 1)
)
juniSystemTempEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemTempIndex"),
)
if mibBuilder.loadTexts:
    juniSystemTempEntry.setStatus("current")


class _JuniSystemTempIndex_Type(Integer32):
    """Custom type juniSystemTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniSystemTempIndex_Type.__name__ = "Integer32"
_JuniSystemTempIndex_Object = MibTableColumn
juniSystemTempIndex = _JuniSystemTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 4, 1, 1),
    _JuniSystemTempIndex_Type()
)
juniSystemTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemTempIndex.setStatus("current")


class _JuniSystemTempStatus_Type(Integer32):
    """Custom type juniSystemTempStatus based on Integer32"""
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
        *(("failed", 1),
          ("nominal", 3),
          ("tooHigh", 4),
          ("tooHighWarning", 6),
          ("tooLow", 2),
          ("tooLowWarning", 5),
          ("unknown", 0))
    )


_JuniSystemTempStatus_Type.__name__ = "Integer32"
_JuniSystemTempStatus_Object = MibTableColumn
juniSystemTempStatus = _JuniSystemTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 4, 1, 2),
    _JuniSystemTempStatus_Type()
)
juniSystemTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemTempStatus.setStatus("current")
_JuniSystemTempValue_Type = Integer32
_JuniSystemTempValue_Object = MibTableColumn
juniSystemTempValue = _JuniSystemTempValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 4, 1, 3),
    _JuniSystemTempValue_Type()
)
juniSystemTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemTempValue.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemTempValue.setUnits("degrees Celsius")


class _JuniSystemTempPhysicalIndex_Type(Integer32):
    """Custom type juniSystemTempPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniSystemTempPhysicalIndex_Type.__name__ = "Integer32"
_JuniSystemTempPhysicalIndex_Object = MibTableColumn
juniSystemTempPhysicalIndex = _JuniSystemTempPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 4, 1, 4),
    _JuniSystemTempPhysicalIndex_Type()
)
juniSystemTempPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemTempPhysicalIndex.setStatus("current")


class _JuniSystemTempProtectionStatus_Type(Integer32):
    """Custom type juniSystemTempProtectionStatus based on Integer32"""
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
        *(("activatedHoldOffExpired", 3),
          ("activatedTempTooHigh", 4),
          ("inHoldOff", 2),
          ("monitoring", 1),
          ("off", 0))
    )


_JuniSystemTempProtectionStatus_Type.__name__ = "Integer32"
_JuniSystemTempProtectionStatus_Object = MibScalar
juniSystemTempProtectionStatus = _JuniSystemTempProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 5),
    _JuniSystemTempProtectionStatus_Type()
)
juniSystemTempProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemTempProtectionStatus.setStatus("current")


class _JuniSystemTempProtectionHoldOffTime_Type(Integer32):
    """Custom type juniSystemTempProtectionHoldOffTime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_JuniSystemTempProtectionHoldOffTime_Type.__name__ = "Integer32"
_JuniSystemTempProtectionHoldOffTime_Object = MibScalar
juniSystemTempProtectionHoldOffTime = _JuniSystemTempProtectionHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 6),
    _JuniSystemTempProtectionHoldOffTime_Type()
)
juniSystemTempProtectionHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemTempProtectionHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemTempProtectionHoldOffTime.setUnits("seconds")


class _JuniSystemTempProtectionHoldOffTimeRemaining_Type(Integer32):
    """Custom type juniSystemTempProtectionHoldOffTimeRemaining based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_JuniSystemTempProtectionHoldOffTimeRemaining_Type.__name__ = "Integer32"
_JuniSystemTempProtectionHoldOffTimeRemaining_Object = MibScalar
juniSystemTempProtectionHoldOffTimeRemaining = _JuniSystemTempProtectionHoldOffTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 9, 7),
    _JuniSystemTempProtectionHoldOffTimeRemaining_Type()
)
juniSystemTempProtectionHoldOffTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemTempProtectionHoldOffTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemTempProtectionHoldOffTimeRemaining.setUnits("seconds")
_JuniSystemUtilization_ObjectIdentity = ObjectIdentity
juniSystemUtilization = _JuniSystemUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10)
)
_JuniSystemUtilizationTable_Object = MibTable
juniSystemUtilizationTable = _JuniSystemUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    juniSystemUtilizationTable.setStatus("current")
_JuniSystemUtilizationEntry_Object = MibTableRow
juniSystemUtilizationEntry = _JuniSystemUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1)
)
juniSystemUtilizationEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemUtilizationResourceType"),
    (0, "Juniper-System-MIB", "juniSystemUtilizationResourceSubType"),
    (0, "Juniper-System-MIB", "juniSystemUtilizationLocationType"),
    (0, "Juniper-System-MIB", "juniSystemUtilizationLocation"),
)
if mibBuilder.loadTexts:
    juniSystemUtilizationEntry.setStatus("current")


class _JuniSystemUtilizationResourceType_Type(Integer32):
    """Custom type juniSystemUtilizationResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("memory", 2))
    )


_JuniSystemUtilizationResourceType_Type.__name__ = "Integer32"
_JuniSystemUtilizationResourceType_Object = MibTableColumn
juniSystemUtilizationResourceType = _JuniSystemUtilizationResourceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1, 1),
    _JuniSystemUtilizationResourceType_Type()
)
juniSystemUtilizationResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemUtilizationResourceType.setStatus("current")


class _JuniSystemUtilizationResourceSubType_Type(Integer32):
    """Custom type juniSystemUtilizationResourceSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniSystemUtilizationResourceSubType_Type.__name__ = "Integer32"
_JuniSystemUtilizationResourceSubType_Object = MibTableColumn
juniSystemUtilizationResourceSubType = _JuniSystemUtilizationResourceSubType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1, 2),
    _JuniSystemUtilizationResourceSubType_Type()
)
juniSystemUtilizationResourceSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemUtilizationResourceSubType.setStatus("current")
_JuniSystemUtilizationLocationType_Type = JuniSystemLocationType
_JuniSystemUtilizationLocationType_Object = MibTableColumn
juniSystemUtilizationLocationType = _JuniSystemUtilizationLocationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1, 3),
    _JuniSystemUtilizationLocationType_Type()
)
juniSystemUtilizationLocationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemUtilizationLocationType.setStatus("current")
_JuniSystemUtilizationLocation_Type = JuniSystemLocation
_JuniSystemUtilizationLocation_Object = MibTableColumn
juniSystemUtilizationLocation = _JuniSystemUtilizationLocation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1, 4),
    _JuniSystemUtilizationLocation_Type()
)
juniSystemUtilizationLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemUtilizationLocation.setStatus("current")
_JuniSystemUtilizationMaxCapacity_Type = Gauge32
_JuniSystemUtilizationMaxCapacity_Object = MibTableColumn
juniSystemUtilizationMaxCapacity = _JuniSystemUtilizationMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1, 5),
    _JuniSystemUtilizationMaxCapacity_Type()
)
juniSystemUtilizationMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemUtilizationMaxCapacity.setStatus("current")
_JuniSystemUtilizationCurrentValue_Type = Gauge32
_JuniSystemUtilizationCurrentValue_Object = MibTableColumn
juniSystemUtilizationCurrentValue = _JuniSystemUtilizationCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1, 6),
    _JuniSystemUtilizationCurrentValue_Type()
)
juniSystemUtilizationCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemUtilizationCurrentValue.setStatus("current")
_JuniSystemUtilizationThresholdRising_Type = Gauge32
_JuniSystemUtilizationThresholdRising_Object = MibTableColumn
juniSystemUtilizationThresholdRising = _JuniSystemUtilizationThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1, 7),
    _JuniSystemUtilizationThresholdRising_Type()
)
juniSystemUtilizationThresholdRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemUtilizationThresholdRising.setStatus("current")
_JuniSystemUtilizationThresholdFalling_Type = Gauge32
_JuniSystemUtilizationThresholdFalling_Object = MibTableColumn
juniSystemUtilizationThresholdFalling = _JuniSystemUtilizationThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1, 8),
    _JuniSystemUtilizationThresholdFalling_Type()
)
juniSystemUtilizationThresholdFalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemUtilizationThresholdFalling.setStatus("current")
_JuniSystemUtilizationHoldDownTime_Type = Gauge32
_JuniSystemUtilizationHoldDownTime_Object = MibTableColumn
juniSystemUtilizationHoldDownTime = _JuniSystemUtilizationHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 1, 1, 9),
    _JuniSystemUtilizationHoldDownTime_Type()
)
juniSystemUtilizationHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSystemUtilizationHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemUtilizationHoldDownTime.setUnits("seconds")
_JuniSystemCpuUtilizationTable_Object = MibTable
juniSystemCpuUtilizationTable = _JuniSystemCpuUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationTable.setStatus("current")
_JuniSystemCpuUtilizationEntry_Object = MibTableRow
juniSystemCpuUtilizationEntry = _JuniSystemCpuUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1)
)
juniSystemCpuUtilizationEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemCpuUtilizationTimeMark"),
    (0, "Juniper-System-MIB", "juniSystemCpuUtilizationTaskName"),
)
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationEntry.setStatus("current")
_JuniSystemCpuUtilizationTimeMark_Type = JuniTimeFilter
_JuniSystemCpuUtilizationTimeMark_Object = MibTableColumn
juniSystemCpuUtilizationTimeMark = _JuniSystemCpuUtilizationTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 1),
    _JuniSystemCpuUtilizationTimeMark_Type()
)
juniSystemCpuUtilizationTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationTimeMark.setStatus("current")
_JuniSystemCpuUtilizationTaskName_Type = JuniSystemTaskName
_JuniSystemCpuUtilizationTaskName_Object = MibTableColumn
juniSystemCpuUtilizationTaskName = _JuniSystemCpuUtilizationTaskName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 2),
    _JuniSystemCpuUtilizationTaskName_Type()
)
juniSystemCpuUtilizationTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationTaskName.setStatus("current")
_JuniSystemCpuUtilizationInvoked_Type = Integer32
_JuniSystemCpuUtilizationInvoked_Object = MibTableColumn
juniSystemCpuUtilizationInvoked = _JuniSystemCpuUtilizationInvoked_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 3),
    _JuniSystemCpuUtilizationInvoked_Type()
)
juniSystemCpuUtilizationInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationInvoked.setStatus("current")
_JuniSystemCpuUtilizationInvokationPerSec_Type = Integer32
_JuniSystemCpuUtilizationInvokationPerSec_Object = MibTableColumn
juniSystemCpuUtilizationInvokationPerSec = _JuniSystemCpuUtilizationInvokationPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 4),
    _JuniSystemCpuUtilizationInvokationPerSec_Type()
)
juniSystemCpuUtilizationInvokationPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationInvokationPerSec.setStatus("current")
_JuniSystemCpuUtilizationTotalRunningTime_Type = Integer32
_JuniSystemCpuUtilizationTotalRunningTime_Object = MibTableColumn
juniSystemCpuUtilizationTotalRunningTime = _JuniSystemCpuUtilizationTotalRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 5),
    _JuniSystemCpuUtilizationTotalRunningTime_Type()
)
juniSystemCpuUtilizationTotalRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationTotalRunningTime.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationTotalRunningTime.setUnits("milli Seconds")


class _JuniSystemCpuUtilizationPercentageRunningTime_Type(Integer32):
    """Custom type juniSystemCpuUtilizationPercentageRunningTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniSystemCpuUtilizationPercentageRunningTime_Type.__name__ = "Integer32"
_JuniSystemCpuUtilizationPercentageRunningTime_Object = MibTableColumn
juniSystemCpuUtilizationPercentageRunningTime = _JuniSystemCpuUtilizationPercentageRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 6),
    _JuniSystemCpuUtilizationPercentageRunningTime_Type()
)
juniSystemCpuUtilizationPercentageRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationPercentageRunningTime.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationPercentageRunningTime.setUnits("percent")
_JuniSystemCpuUtilizationAverageTimePerInvokation_Type = Integer32
_JuniSystemCpuUtilizationAverageTimePerInvokation_Object = MibTableColumn
juniSystemCpuUtilizationAverageTimePerInvokation = _JuniSystemCpuUtilizationAverageTimePerInvokation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 7),
    _JuniSystemCpuUtilizationAverageTimePerInvokation_Type()
)
juniSystemCpuUtilizationAverageTimePerInvokation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationAverageTimePerInvokation.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationAverageTimePerInvokation.setUnits("micro Seconds")


class _JuniSystemCpuUtilizationFiveSecondUtilization_Type(Integer32):
    """Custom type juniSystemCpuUtilizationFiveSecondUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniSystemCpuUtilizationFiveSecondUtilization_Type.__name__ = "Integer32"
_JuniSystemCpuUtilizationFiveSecondUtilization_Object = MibTableColumn
juniSystemCpuUtilizationFiveSecondUtilization = _JuniSystemCpuUtilizationFiveSecondUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 8),
    _JuniSystemCpuUtilizationFiveSecondUtilization_Type()
)
juniSystemCpuUtilizationFiveSecondUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationFiveSecondUtilization.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationFiveSecondUtilization.setUnits("percent")


class _JuniSystemCpuUtilizationOneMinuteUtilization_Type(Integer32):
    """Custom type juniSystemCpuUtilizationOneMinuteUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniSystemCpuUtilizationOneMinuteUtilization_Type.__name__ = "Integer32"
_JuniSystemCpuUtilizationOneMinuteUtilization_Object = MibTableColumn
juniSystemCpuUtilizationOneMinuteUtilization = _JuniSystemCpuUtilizationOneMinuteUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 9),
    _JuniSystemCpuUtilizationOneMinuteUtilization_Type()
)
juniSystemCpuUtilizationOneMinuteUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationOneMinuteUtilization.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationOneMinuteUtilization.setUnits("percent")


class _JuniSystemCpuUtilizationFiveMinuteUtilization_Type(Integer32):
    """Custom type juniSystemCpuUtilizationFiveMinuteUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniSystemCpuUtilizationFiveMinuteUtilization_Type.__name__ = "Integer32"
_JuniSystemCpuUtilizationFiveMinuteUtilization_Object = MibTableColumn
juniSystemCpuUtilizationFiveMinuteUtilization = _JuniSystemCpuUtilizationFiveMinuteUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 10),
    _JuniSystemCpuUtilizationFiveMinuteUtilization_Type()
)
juniSystemCpuUtilizationFiveMinuteUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationFiveMinuteUtilization.setStatus("current")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationFiveMinuteUtilization.setUnits("percent")
_JuniSystemCpuUtilizationNumberOfInstances_Type = Integer32
_JuniSystemCpuUtilizationNumberOfInstances_Object = MibTableColumn
juniSystemCpuUtilizationNumberOfInstances = _JuniSystemCpuUtilizationNumberOfInstances_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 10, 2, 1, 11),
    _JuniSystemCpuUtilizationNumberOfInstances_Type()
)
juniSystemCpuUtilizationNumberOfInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemCpuUtilizationNumberOfInstances.setStatus("current")
_JuniSystemIssu_ObjectIdentity = ObjectIdentity
juniSystemIssu = _JuniSystemIssu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11)
)


class _JuniSystemIssuState_Type(Integer32):
    """Custom type juniSystemIssuState based on Integer32"""
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
        *(("idle", 1),
          ("initialized", 3),
          ("initializing", 2),
          ("stopping", 5),
          ("upgrading", 4))
    )


_JuniSystemIssuState_Type.__name__ = "Integer32"
_JuniSystemIssuState_Object = MibScalar
juniSystemIssuState = _JuniSystemIssuState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11, 1),
    _JuniSystemIssuState_Type()
)
juniSystemIssuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemIssuState.setStatus("current")


class _JuniSystemIssuRunningReleaseFile_Type(DisplayString):
    """Custom type juniSystemIssuRunningReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemIssuRunningReleaseFile_Type.__name__ = "DisplayString"
_JuniSystemIssuRunningReleaseFile_Object = MibScalar
juniSystemIssuRunningReleaseFile = _JuniSystemIssuRunningReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11, 2),
    _JuniSystemIssuRunningReleaseFile_Type()
)
juniSystemIssuRunningReleaseFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemIssuRunningReleaseFile.setStatus("current")


class _JuniSystemIssuArmedReleaseFile_Type(DisplayString):
    """Custom type juniSystemIssuArmedReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniSystemIssuArmedReleaseFile_Type.__name__ = "DisplayString"
_JuniSystemIssuArmedReleaseFile_Object = MibScalar
juniSystemIssuArmedReleaseFile = _JuniSystemIssuArmedReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11, 3),
    _JuniSystemIssuArmedReleaseFile_Type()
)
juniSystemIssuArmedReleaseFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemIssuArmedReleaseFile.setStatus("current")


class _JuniSystemIssuStatus_Type(Integer32):
    """Custom type juniSystemIssuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("ok", 1),
          ("warning", 2))
    )


_JuniSystemIssuStatus_Type.__name__ = "Integer32"
_JuniSystemIssuStatus_Object = MibScalar
juniSystemIssuStatus = _JuniSystemIssuStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11, 4),
    _JuniSystemIssuStatus_Type()
)
juniSystemIssuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemIssuStatus.setStatus("current")
_JuniSystemIssuCriteriaTable_Object = MibTable
juniSystemIssuCriteriaTable = _JuniSystemIssuCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11, 5)
)
if mibBuilder.loadTexts:
    juniSystemIssuCriteriaTable.setStatus("current")
_JuniSystemIssuCriteriaEntry_Object = MibTableRow
juniSystemIssuCriteriaEntry = _JuniSystemIssuCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11, 5, 1)
)
juniSystemIssuCriteriaEntry.setIndexNames(
    (0, "Juniper-System-MIB", "juniSystemIssuCriteriaIndex"),
)
if mibBuilder.loadTexts:
    juniSystemIssuCriteriaEntry.setStatus("current")


class _JuniSystemIssuCriteriaIndex_Type(Integer32):
    """Custom type juniSystemIssuCriteriaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniSystemIssuCriteriaIndex_Type.__name__ = "Integer32"
_JuniSystemIssuCriteriaIndex_Object = MibTableColumn
juniSystemIssuCriteriaIndex = _JuniSystemIssuCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11, 5, 1, 1),
    _JuniSystemIssuCriteriaIndex_Type()
)
juniSystemIssuCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSystemIssuCriteriaIndex.setStatus("current")


class _JuniSystemIssuCriteriaDescription_Type(DisplayString):
    """Custom type juniSystemIssuCriteriaDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JuniSystemIssuCriteriaDescription_Type.__name__ = "DisplayString"
_JuniSystemIssuCriteriaDescription_Object = MibTableColumn
juniSystemIssuCriteriaDescription = _JuniSystemIssuCriteriaDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11, 5, 1, 2),
    _JuniSystemIssuCriteriaDescription_Type()
)
juniSystemIssuCriteriaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemIssuCriteriaDescription.setStatus("current")


class _JuniSystemIssuCriteriaStatus_Type(Integer32):
    """Custom type juniSystemIssuCriteriaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("conditional", 3),
          ("no", 2),
          ("yes", 1))
    )


_JuniSystemIssuCriteriaStatus_Type.__name__ = "Integer32"
_JuniSystemIssuCriteriaStatus_Object = MibTableColumn
juniSystemIssuCriteriaStatus = _JuniSystemIssuCriteriaStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 1, 11, 5, 1, 3),
    _JuniSystemIssuCriteriaStatus_Type()
)
juniSystemIssuCriteriaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSystemIssuCriteriaStatus.setStatus("current")
_JuniSystemConformance_ObjectIdentity = ObjectIdentity
juniSystemConformance = _JuniSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2)
)
_JuniSystemCompliances_ObjectIdentity = ObjectIdentity
juniSystemCompliances = _JuniSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 1)
)
_JuniSystemGroups_ObjectIdentity = ObjectIdentity
juniSystemGroups = _JuniSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2)
)

# Managed Objects groups

juniSystemGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 1)
)
juniSystemGeneralGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemSwVersion"),
        ("Juniper-System-MIB", "juniSystemSwBuildDate"),
        ("Juniper-System-MIB", "juniSystemMemUtilPct"),
        ("Juniper-System-MIB", "juniSystemMemCapacity"),
        ("Juniper-System-MIB", "juniSystemHighMemUtilThreshold"),
        ("Juniper-System-MIB", "juniSystemAbatedMemUtilThreshold"),
        ("Juniper-System-MIB", "juniSystemMemUtilTrapEnable"),
        ("Juniper-System-MIB", "juniSystemBootConfigControl"),
        ("Juniper-System-MIB", "juniSystemBootBackupConfigControl"),
        ("Juniper-System-MIB", "juniSystemBootForceBackupControl"),
        ("Juniper-System-MIB", "juniSystemBootAutoRevertControl"),
        ("Juniper-System-MIB", "juniSystemBootAutoRevertCountTolerance"),
        ("Juniper-System-MIB", "juniSystemBootAutoRevertTimeTolerance"),
        ("Juniper-System-MIB", "juniSystemBootReleaseFile"),
        ("Juniper-System-MIB", "juniSystemBootConfigFile"),
        ("Juniper-System-MIB", "juniSystemBootBackupReleaseFile"),
        ("Juniper-System-MIB", "juniSystemBootBackupConfigFile"),
        ("Juniper-System-MIB", "juniSystemRedundancyRevertControl"),
        ("Juniper-System-MIB", "juniSystemRedundancyRevertTimeOfDay"))
)
if mibBuilder.loadTexts:
    juniSystemGeneralGroup.setStatus("obsolete")

juniSystemSubsystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 2)
)
juniSystemSubsystemGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemSubsystemName"),
        ("Juniper-System-MIB", "juniSystemSubsystemBootReleaseFile"),
        ("Juniper-System-MIB", "juniSystemSubsystemBootBackupReleaseFile"))
)
if mibBuilder.loadTexts:
    juniSystemSubsystemGroup.setStatus("current")

juniSystemModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 3)
)
juniSystemModuleGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemMaxSlotNumber"),
        ("Juniper-System-MIB", "juniSystemMaxModulesPerSlot"),
        ("Juniper-System-MIB", "juniSystemSlotStatus"),
        ("Juniper-System-MIB", "juniSystemSlotType"),
        ("Juniper-System-MIB", "juniSystemModuleOperStatus"),
        ("Juniper-System-MIB", "juniSystemModuleDisableReason"),
        ("Juniper-System-MIB", "juniSystemModuleLastChange"),
        ("Juniper-System-MIB", "juniSystemModuleCurrentType"),
        ("Juniper-System-MIB", "juniSystemModuleExpectedType"),
        ("Juniper-System-MIB", "juniSystemModuleDescr"),
        ("Juniper-System-MIB", "juniSystemModuleSlotSpan"),
        ("Juniper-System-MIB", "juniSystemModulePortCount"),
        ("Juniper-System-MIB", "juniSystemModuleSerialNumber"),
        ("Juniper-System-MIB", "juniSystemModuleAssemblyPartNumber"),
        ("Juniper-System-MIB", "juniSystemModuleAssemblyRev"),
        ("Juniper-System-MIB", "juniSystemModulePhysicalIndex"),
        ("Juniper-System-MIB", "juniSystemModuleSoftwareSupport"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancySupport"),
        ("Juniper-System-MIB", "juniSystemModuleSoftwareVersion"),
        ("Juniper-System-MIB", "juniSystemModuleCpuUtilPct"),
        ("Juniper-System-MIB", "juniSystemModuleMemUtilPct"),
        ("Juniper-System-MIB", "juniSystemModuleAdminStatus"),
        ("Juniper-System-MIB", "juniSystemModuleControl"),
        ("Juniper-System-MIB", "juniSystemModuleBootReleaseFile"),
        ("Juniper-System-MIB", "juniSystemModuleBootBackupReleaseFile"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyGroupId"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancySpare"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyAssociatedSlot"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyLockout"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyRevertControl"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyRevertTime"))
)
if mibBuilder.loadTexts:
    juniSystemModuleGroup.setStatus("obsolete")

juniSystemPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 4)
)
juniSystemPortGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemPortPhysicalIndex"),
        ("Juniper-System-MIB", "juniSystemPortIfIndex"))
)
if mibBuilder.loadTexts:
    juniSystemPortGroup.setStatus("current")

juniSystemTimingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 5)
)
juniSystemTimingGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemAdminTimingSource"),
        ("Juniper-System-MIB", "juniSystemOperTimingSource"),
        ("Juniper-System-MIB", "juniSystemTimingAutoUpgrade"),
        ("Juniper-System-MIB", "juniSystemTimingSourceType"),
        ("Juniper-System-MIB", "juniSystemTimingSourceIfIndex"),
        ("Juniper-System-MIB", "juniSystemTimingSourceLine"),
        ("Juniper-System-MIB", "juniSystemTimingWorkingStatus"),
        ("Juniper-System-MIB", "juniSystemTimingProtectedStatus"))
)
if mibBuilder.loadTexts:
    juniSystemTimingGroup.setStatus("current")

juniSystemFabricGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 6)
)
juniSystemFabricGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemFabricSpeed"),
        ("Juniper-System-MIB", "juniSystemFabricRev"))
)
if mibBuilder.loadTexts:
    juniSystemFabricGroup.setStatus("current")

juniSystemNvsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 7)
)
juniSystemNvsGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemNvsCount"),
        ("Juniper-System-MIB", "juniSystemNvsPhysicalIndex"),
        ("Juniper-System-MIB", "juniSystemNvsStatus"),
        ("Juniper-System-MIB", "juniSystemNvsCapacity"),
        ("Juniper-System-MIB", "juniSystemNvsUtilPct"))
)
if mibBuilder.loadTexts:
    juniSystemNvsGroup.setStatus("current")

juniSystemPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 8)
)
juniSystemPowerGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemPowerCount"),
        ("Juniper-System-MIB", "juniSystemPowerPhysicalIndex"),
        ("Juniper-System-MIB", "juniSystemPowerStatus"))
)
if mibBuilder.loadTexts:
    juniSystemPowerGroup.setStatus("current")

juniSystemTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 9)
)
juniSystemTemperatureGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemFanCount"),
        ("Juniper-System-MIB", "juniSystemFanPhysicalIndex"),
        ("Juniper-System-MIB", "juniSystemFanStatus"),
        ("Juniper-System-MIB", "juniSystemTempCount"),
        ("Juniper-System-MIB", "juniSystemTempStatus"),
        ("Juniper-System-MIB", "juniSystemTempValue"),
        ("Juniper-System-MIB", "juniSystemTempPhysicalIndex"),
        ("Juniper-System-MIB", "juniSystemTempProtectionStatus"),
        ("Juniper-System-MIB", "juniSystemTempProtectionHoldOffTime"),
        ("Juniper-System-MIB", "juniSystemTempProtectionHoldOffTimeRemaining"))
)
if mibBuilder.loadTexts:
    juniSystemTemperatureGroup.setStatus("current")

juniSystemNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 10)
)
juniSystemNotificationObjectsGroup.setObjects(
    ("Juniper-System-MIB", "juniSystemReloadSlotNumber")
)
if mibBuilder.loadTexts:
    juniSystemNotificationObjectsGroup.setStatus("current")

juniSystemUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 12)
)
juniSystemUtilizationGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemUtilizationMaxCapacity"),
        ("Juniper-System-MIB", "juniSystemUtilizationCurrentValue"),
        ("Juniper-System-MIB", "juniSystemUtilizationThresholdRising"),
        ("Juniper-System-MIB", "juniSystemUtilizationThresholdFalling"),
        ("Juniper-System-MIB", "juniSystemUtilizationHoldDownTime"),
        ("Juniper-System-MIB", "juniSystemUtilizationThresholdDirection"))
)
if mibBuilder.loadTexts:
    juniSystemUtilizationGroup.setStatus("obsolete")

juniSystemGeneralGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 14)
)
juniSystemGeneralGroup2.setObjects(
      *(("Juniper-System-MIB", "juniSystemSwVersion"),
        ("Juniper-System-MIB", "juniSystemSwBuildDate"),
        ("Juniper-System-MIB", "juniSystemMemUtilPct"),
        ("Juniper-System-MIB", "juniSystemMemCapacity"),
        ("Juniper-System-MIB", "juniSystemMemKBytesCapacity"),
        ("Juniper-System-MIB", "juniSystemHighMemUtilThreshold"),
        ("Juniper-System-MIB", "juniSystemAbatedMemUtilThreshold"),
        ("Juniper-System-MIB", "juniSystemMemUtilTrapEnable"),
        ("Juniper-System-MIB", "juniSystemUtilizationTrapEnable"),
        ("Juniper-System-MIB", "juniSystemBootConfigControl"),
        ("Juniper-System-MIB", "juniSystemBootBackupConfigControl"),
        ("Juniper-System-MIB", "juniSystemBootForceBackupControl"),
        ("Juniper-System-MIB", "juniSystemBootAutoRevertControl"),
        ("Juniper-System-MIB", "juniSystemBootAutoRevertCountTolerance"),
        ("Juniper-System-MIB", "juniSystemBootAutoRevertTimeTolerance"),
        ("Juniper-System-MIB", "juniSystemBootReleaseFile"),
        ("Juniper-System-MIB", "juniSystemBootConfigFile"),
        ("Juniper-System-MIB", "juniSystemBootBackupReleaseFile"),
        ("Juniper-System-MIB", "juniSystemBootBackupConfigFile"),
        ("Juniper-System-MIB", "juniSystemRedundancyRevertControl"),
        ("Juniper-System-MIB", "juniSystemRedundancyRevertTimeOfDay"))
)
if mibBuilder.loadTexts:
    juniSystemGeneralGroup2.setStatus("current")

juniSystemModuleGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 15)
)
juniSystemModuleGroup2.setObjects(
      *(("Juniper-System-MIB", "juniSystemMaxSlotNumber"),
        ("Juniper-System-MIB", "juniSystemMaxModulesPerSlot"),
        ("Juniper-System-MIB", "juniSystemSlotStatus"),
        ("Juniper-System-MIB", "juniSystemSlotType"),
        ("Juniper-System-MIB", "juniSystemModuleOperStatus"),
        ("Juniper-System-MIB", "juniSystemModuleDisableReason"),
        ("Juniper-System-MIB", "juniSystemModuleLastChange"),
        ("Juniper-System-MIB", "juniSystemModuleCurrentType"),
        ("Juniper-System-MIB", "juniSystemModuleExpectedType"),
        ("Juniper-System-MIB", "juniSystemModuleDescr"),
        ("Juniper-System-MIB", "juniSystemModuleSlotSpan"),
        ("Juniper-System-MIB", "juniSystemModulePortCount"),
        ("Juniper-System-MIB", "juniSystemModuleSerialNumber"),
        ("Juniper-System-MIB", "juniSystemModuleAssemblyPartNumber"),
        ("Juniper-System-MIB", "juniSystemModuleAssemblyRev"),
        ("Juniper-System-MIB", "juniSystemModulePhysicalIndex"),
        ("Juniper-System-MIB", "juniSystemModuleSoftwareSupport"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancySupport"),
        ("Juniper-System-MIB", "juniSystemModuleLevelSpan"),
        ("Juniper-System-MIB", "juniSystemModuleSoftwareVersion"),
        ("Juniper-System-MIB", "juniSystemModuleCpuUtilPct"),
        ("Juniper-System-MIB", "juniSystemModuleMemUtilPct"),
        ("Juniper-System-MIB", "juniSystemModuleAdminStatus"),
        ("Juniper-System-MIB", "juniSystemModuleControl"),
        ("Juniper-System-MIB", "juniSystemModuleBootReleaseFile"),
        ("Juniper-System-MIB", "juniSystemModuleBootBackupReleaseFile"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyGroupId"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancySpare"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyAssociatedSlot"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyLockout"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyRevertControl"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyRevertTime"))
)
if mibBuilder.loadTexts:
    juniSystemModuleGroup2.setStatus("obsolete")

juniSystemUtilizationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 16)
)
juniSystemUtilizationGroup2.setObjects(
      *(("Juniper-System-MIB", "juniSystemUtilizationMaxCapacity"),
        ("Juniper-System-MIB", "juniSystemUtilizationCurrentValue"),
        ("Juniper-System-MIB", "juniSystemUtilizationThresholdRising"),
        ("Juniper-System-MIB", "juniSystemUtilizationThresholdFalling"),
        ("Juniper-System-MIB", "juniSystemUtilizationHoldDownTime"),
        ("Juniper-System-MIB", "juniSystemUtilizationThresholdDirection"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationTaskName"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationInvoked"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationInvokationPerSec"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationTotalRunningTime"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationPercentageRunningTime"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationAverageTimePerInvokation"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationFiveSecondUtilization"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationOneMinuteUtilization"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationFiveMinuteUtilization"),
        ("Juniper-System-MIB", "juniSystemCpuUtilizationNumberOfInstances"))
)
if mibBuilder.loadTexts:
    juniSystemUtilizationGroup2.setStatus("current")

juniSystemModuleGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 17)
)
juniSystemModuleGroup3.setObjects(
      *(("Juniper-System-MIB", "juniSystemMaxSlotNumber"),
        ("Juniper-System-MIB", "juniSystemMaxModulesPerSlot"),
        ("Juniper-System-MIB", "juniSystemSlotStatus"),
        ("Juniper-System-MIB", "juniSystemSlotType"),
        ("Juniper-System-MIB", "juniSystemModuleOperStatus"),
        ("Juniper-System-MIB", "juniSystemModuleDisableReason"),
        ("Juniper-System-MIB", "juniSystemModuleLastChange"),
        ("Juniper-System-MIB", "juniSystemModuleCurrentType"),
        ("Juniper-System-MIB", "juniSystemModuleExpectedType"),
        ("Juniper-System-MIB", "juniSystemModuleDescr"),
        ("Juniper-System-MIB", "juniSystemModuleSlotSpan"),
        ("Juniper-System-MIB", "juniSystemModulePortCount"),
        ("Juniper-System-MIB", "juniSystemModuleSerialNumber"),
        ("Juniper-System-MIB", "juniSystemModuleAssemblyPartNumber"),
        ("Juniper-System-MIB", "juniSystemModuleAssemblyRev"),
        ("Juniper-System-MIB", "juniSystemModulePhysicalIndex"),
        ("Juniper-System-MIB", "juniSystemModuleSoftwareSupport"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancySupport"),
        ("Juniper-System-MIB", "juniSystemModuleLevelSpan"),
        ("Juniper-System-MIB", "juniSystemModuleSoftwareVersion"),
        ("Juniper-System-MIB", "juniSystemModuleCpuUtilPct"),
        ("Juniper-System-MIB", "juniSystemModuleMemUtilPct"),
        ("Juniper-System-MIB", "juniSystemModuleAdminStatus"),
        ("Juniper-System-MIB", "juniSystemModuleControl"),
        ("Juniper-System-MIB", "juniSystemModuleBootReleaseFile"),
        ("Juniper-System-MIB", "juniSystemModuleBootBackupReleaseFile"),
        ("Juniper-System-MIB", "juniSystemModuleCpuFiveSecUtilPct"),
        ("Juniper-System-MIB", "juniSystemModuleCpuOneMinAvgPct"),
        ("Juniper-System-MIB", "juniSystemModuleCpuFiveMinAvgPct"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyGroupId"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancySpare"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyAssociatedSlot"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyLockout"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyRevertControl"),
        ("Juniper-System-MIB", "juniSystemModuleRedundancyRevertTime"))
)
if mibBuilder.loadTexts:
    juniSystemModuleGroup3.setStatus("current")

juniSystemIssuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 18)
)
juniSystemIssuGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemIssuState"),
        ("Juniper-System-MIB", "juniSystemIssuArmedReleaseFile"),
        ("Juniper-System-MIB", "juniSystemIssuRunningReleaseFile"),
        ("Juniper-System-MIB", "juniSystemIssuStatus"),
        ("Juniper-System-MIB", "juniSystemIssuCriteriaDescription"),
        ("Juniper-System-MIB", "juniSystemIssuCriteriaStatus"))
)
if mibBuilder.loadTexts:
    juniSystemIssuGroup.setStatus("current")


# Notification objects

juniSystemHighMemUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 1)
)
juniSystemHighMemUtil.setObjects(
      *(("Juniper-System-MIB", "juniSystemMemCapacity"),
        ("Juniper-System-MIB", "juniSystemMemUtilPct"),
        ("Juniper-System-MIB", "juniSystemAbatedMemUtilThreshold"),
        ("Juniper-System-MIB", "juniSystemHighMemUtilThreshold"),
        ("Juniper-System-MIB", "juniSystemMemKBytesCapacity"))
)
if mibBuilder.loadTexts:
    juniSystemHighMemUtil.setStatus(
        "current"
    )

juniSystemAbatedMemUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 2)
)
juniSystemAbatedMemUtil.setObjects(
      *(("Juniper-System-MIB", "juniSystemMemCapacity"),
        ("Juniper-System-MIB", "juniSystemMemUtilPct"),
        ("Juniper-System-MIB", "juniSystemAbatedMemUtilThreshold"),
        ("Juniper-System-MIB", "juniSystemHighMemUtilThreshold"),
        ("Juniper-System-MIB", "juniSystemMemKBytesCapacity"))
)
if mibBuilder.loadTexts:
    juniSystemAbatedMemUtil.setStatus(
        "current"
    )

juniSystemModuleOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 3)
)
juniSystemModuleOperStatusChange.setObjects(
      *(("Juniper-System-MIB", "juniSystemModuleCurrentType"),
        ("Juniper-System-MIB", "juniSystemModuleAdminStatus"),
        ("Juniper-System-MIB", "juniSystemModuleOperStatus"),
        ("Juniper-System-MIB", "juniSystemModuleDisableReason"),
        ("Juniper-System-MIB", "juniSystemModuleDescr"))
)
if mibBuilder.loadTexts:
    juniSystemModuleOperStatusChange.setStatus(
        "current"
    )

juniSystemPowerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 4)
)
juniSystemPowerStatusChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("Juniper-System-MIB", "juniSystemPowerStatus"))
)
if mibBuilder.loadTexts:
    juniSystemPowerStatusChange.setStatus(
        "current"
    )

juniSystemFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 5)
)
juniSystemFanStatusChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("Juniper-System-MIB", "juniSystemFanStatus"))
)
if mibBuilder.loadTexts:
    juniSystemFanStatusChange.setStatus(
        "current"
    )

juniSystemTempStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 6)
)
juniSystemTempStatusChange.setObjects(
    ("Juniper-System-MIB", "juniSystemTempStatus")
)
if mibBuilder.loadTexts:
    juniSystemTempStatusChange.setStatus(
        "current"
    )

juniSystemTempProtectionStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 7)
)
juniSystemTempProtectionStatusChange.setObjects(
      *(("Juniper-System-MIB", "juniSystemTempProtectionStatus"),
        ("Juniper-System-MIB", "juniSystemTempProtectionHoldOffTimeRemaining"))
)
if mibBuilder.loadTexts:
    juniSystemTempProtectionStatusChange.setStatus(
        "current"
    )

juniSystemReloadCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 8)
)
if mibBuilder.loadTexts:
    juniSystemReloadCommand.setStatus(
        "current"
    )

juniSystemUtilizationThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 9)
)
juniSystemUtilizationThreshold.setObjects(
      *(("Juniper-System-MIB", "juniSystemUtilizationThresholdDirection"),
        ("Juniper-System-MIB", "juniSystemUtilizationMaxCapacity"),
        ("Juniper-System-MIB", "juniSystemUtilizationCurrentValue"),
        ("Juniper-System-MIB", "juniSystemUtilizationThresholdRising"),
        ("Juniper-System-MIB", "juniSystemUtilizationThresholdFalling"),
        ("Juniper-System-MIB", "juniSystemUtilizationHoldDownTime"))
)
if mibBuilder.loadTexts:
    juniSystemUtilizationThreshold.setStatus(
        "current"
    )

juniSystemIssuStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 10)
)
juniSystemIssuStateChange.setObjects(
    ("Juniper-System-MIB", "juniSystemIssuState")
)
if mibBuilder.loadTexts:
    juniSystemIssuStateChange.setStatus(
        "current"
    )

juniSystemPortSfpTxMaxPowerThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 11)
)
juniSystemPortSfpTxMaxPowerThreshold.setObjects(
      *(("Juniper-System-MIB", "juniSystemPortSfpPowerThresholdIfIndex"),
        ("Juniper-System-MIB", "juniSystemPortSfpPowerThresholdValue"))
)
if mibBuilder.loadTexts:
    juniSystemPortSfpTxMaxPowerThreshold.setStatus(
        "current"
    )

juniSystemPortSfpTxMinPowerThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 12)
)
juniSystemPortSfpTxMinPowerThreshold.setObjects(
      *(("Juniper-System-MIB", "juniSystemPortSfpPowerThresholdIfIndex"),
        ("Juniper-System-MIB", "juniSystemPortSfpPowerThresholdValue"))
)
if mibBuilder.loadTexts:
    juniSystemPortSfpTxMinPowerThreshold.setStatus(
        "current"
    )

juniSystemPortSfpRxMaxPowerThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 13)
)
juniSystemPortSfpRxMaxPowerThreshold.setObjects(
      *(("Juniper-System-MIB", "juniSystemPortSfpPowerThresholdIfIndex"),
        ("Juniper-System-MIB", "juniSystemPortSfpPowerThresholdValue"))
)
if mibBuilder.loadTexts:
    juniSystemPortSfpRxMaxPowerThreshold.setStatus(
        "current"
    )

juniSystemPortSfpRxMinPowerThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 0, 14)
)
juniSystemPortSfpRxMinPowerThreshold.setObjects(
      *(("Juniper-System-MIB", "juniSystemPortSfpPowerThresholdIfIndex"),
        ("Juniper-System-MIB", "juniSystemPortSfpPowerThresholdValue"))
)
if mibBuilder.loadTexts:
    juniSystemPortSfpRxMinPowerThreshold.setStatus(
        "current"
    )


# Notifications groups

juniSystemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 11)
)
juniSystemNotificationGroup.setObjects(
      *(("Juniper-System-MIB", "juniSystemHighMemUtil"),
        ("Juniper-System-MIB", "juniSystemAbatedMemUtil"),
        ("Juniper-System-MIB", "juniSystemModuleOperStatusChange"),
        ("Juniper-System-MIB", "juniSystemPowerStatusChange"),
        ("Juniper-System-MIB", "juniSystemFanStatusChange"),
        ("Juniper-System-MIB", "juniSystemTempStatusChange"),
        ("Juniper-System-MIB", "juniSystemTempProtectionStatusChange"),
        ("Juniper-System-MIB", "juniSystemReloadCommand"))
)
if mibBuilder.loadTexts:
    juniSystemNotificationGroup.setStatus(
        "obsolete"
    )

juniSystemNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 13)
)
juniSystemNotificationGroup2.setObjects(
      *(("Juniper-System-MIB", "juniSystemHighMemUtil"),
        ("Juniper-System-MIB", "juniSystemAbatedMemUtil"),
        ("Juniper-System-MIB", "juniSystemModuleOperStatusChange"),
        ("Juniper-System-MIB", "juniSystemPowerStatusChange"),
        ("Juniper-System-MIB", "juniSystemFanStatusChange"),
        ("Juniper-System-MIB", "juniSystemTempStatusChange"),
        ("Juniper-System-MIB", "juniSystemTempProtectionStatusChange"),
        ("Juniper-System-MIB", "juniSystemReloadCommand"),
        ("Juniper-System-MIB", "juniSystemUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    juniSystemNotificationGroup2.setStatus(
        "obsolete"
    )

juniSystemNotificationGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 19)
)
juniSystemNotificationGroup3.setObjects(
      *(("Juniper-System-MIB", "juniSystemHighMemUtil"),
        ("Juniper-System-MIB", "juniSystemAbatedMemUtil"),
        ("Juniper-System-MIB", "juniSystemModuleOperStatusChange"),
        ("Juniper-System-MIB", "juniSystemPowerStatusChange"),
        ("Juniper-System-MIB", "juniSystemFanStatusChange"),
        ("Juniper-System-MIB", "juniSystemTempStatusChange"),
        ("Juniper-System-MIB", "juniSystemTempProtectionStatusChange"),
        ("Juniper-System-MIB", "juniSystemReloadCommand"),
        ("Juniper-System-MIB", "juniSystemUtilizationThreshold"),
        ("Juniper-System-MIB", "juniSystemIssuStateChange"))
)
if mibBuilder.loadTexts:
    juniSystemNotificationGroup3.setStatus(
        "obsolete"
    )

juniSystemNotificationGroup4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 2, 20)
)
juniSystemNotificationGroup4.setObjects(
      *(("Juniper-System-MIB", "juniSystemHighMemUtil"),
        ("Juniper-System-MIB", "juniSystemAbatedMemUtil"),
        ("Juniper-System-MIB", "juniSystemModuleOperStatusChange"),
        ("Juniper-System-MIB", "juniSystemPowerStatusChange"),
        ("Juniper-System-MIB", "juniSystemFanStatusChange"),
        ("Juniper-System-MIB", "juniSystemTempStatusChange"),
        ("Juniper-System-MIB", "juniSystemTempProtectionStatusChange"),
        ("Juniper-System-MIB", "juniSystemReloadCommand"),
        ("Juniper-System-MIB", "juniSystemUtilizationThreshold"),
        ("Juniper-System-MIB", "juniSystemIssuStateChange"),
        ("Juniper-System-MIB", "juniSystemPortSfpTxMaxPowerThreshold"),
        ("Juniper-System-MIB", "juniSystemPortSfpTxMinPowerThreshold"),
        ("Juniper-System-MIB", "juniSystemPortSfpRxMaxPowerThreshold"),
        ("Juniper-System-MIB", "juniSystemPortSfpRxMinPowerThreshold"))
)
if mibBuilder.loadTexts:
    juniSystemNotificationGroup4.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniSystemCompliance.setStatus(
        "obsolete"
    )

juniSystemCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniSystemCompliance2.setStatus(
        "obsolete"
    )

juniSystemCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniSystemCompliance3.setStatus(
        "obsolete"
    )

juniSystemCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniSystemCompliance4.setStatus(
        "obsolete"
    )

juniSystemCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    juniSystemCompliance5.setStatus(
        "obsolete"
    )

juniSystemCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    juniSystemCompliance6.setStatus(
        "obsolete"
    )

juniSystemCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    juniSystemCompliance7.setStatus(
        "obsolete"
    )

juniSystemCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2, 2, 1, 8)
)
if mibBuilder.loadTexts:
    juniSystemCompliance8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-System-MIB",
    **{"JuniSystemModuleType": JuniSystemModuleType,
       "JuniSystemSlotLevel": JuniSystemSlotLevel,
       "JuniSystemSlotType": JuniSystemSlotType,
       "JuniSystemTimingSelector": JuniSystemTimingSelector,
       "JuniSystemLocationType": JuniSystemLocationType,
       "JuniSystemLocation": JuniSystemLocation,
       "JuniSystemTaskName": JuniSystemTaskName,
       "juniSystemMIB": juniSystemMIB,
       "juniSystemTrap": juniSystemTrap,
       "juniSystemHighMemUtil": juniSystemHighMemUtil,
       "juniSystemAbatedMemUtil": juniSystemAbatedMemUtil,
       "juniSystemModuleOperStatusChange": juniSystemModuleOperStatusChange,
       "juniSystemPowerStatusChange": juniSystemPowerStatusChange,
       "juniSystemFanStatusChange": juniSystemFanStatusChange,
       "juniSystemTempStatusChange": juniSystemTempStatusChange,
       "juniSystemTempProtectionStatusChange": juniSystemTempProtectionStatusChange,
       "juniSystemReloadCommand": juniSystemReloadCommand,
       "juniSystemUtilizationThreshold": juniSystemUtilizationThreshold,
       "juniSystemIssuStateChange": juniSystemIssuStateChange,
       "juniSystemPortSfpTxMaxPowerThreshold": juniSystemPortSfpTxMaxPowerThreshold,
       "juniSystemPortSfpTxMinPowerThreshold": juniSystemPortSfpTxMinPowerThreshold,
       "juniSystemPortSfpRxMaxPowerThreshold": juniSystemPortSfpRxMaxPowerThreshold,
       "juniSystemPortSfpRxMinPowerThreshold": juniSystemPortSfpRxMinPowerThreshold,
       "juniSystemObjects": juniSystemObjects,
       "juniSystemGeneral": juniSystemGeneral,
       "juniSystemSwVersion": juniSystemSwVersion,
       "juniSystemSwBuildDate": juniSystemSwBuildDate,
       "juniSystemMemUtilPct": juniSystemMemUtilPct,
       "juniSystemMemCapacity": juniSystemMemCapacity,
       "juniSystemHighMemUtilThreshold": juniSystemHighMemUtilThreshold,
       "juniSystemAbatedMemUtilThreshold": juniSystemAbatedMemUtilThreshold,
       "juniSystemBootConfigControl": juniSystemBootConfigControl,
       "juniSystemBootBackupConfigControl": juniSystemBootBackupConfigControl,
       "juniSystemBootForceBackupControl": juniSystemBootForceBackupControl,
       "juniSystemBootAutoRevertControl": juniSystemBootAutoRevertControl,
       "juniSystemBootAutoRevertCountTolerance": juniSystemBootAutoRevertCountTolerance,
       "juniSystemBootAutoRevertTimeTolerance": juniSystemBootAutoRevertTimeTolerance,
       "juniSystemBootReleaseFile": juniSystemBootReleaseFile,
       "juniSystemBootConfigFile": juniSystemBootConfigFile,
       "juniSystemBootBackupReleaseFile": juniSystemBootBackupReleaseFile,
       "juniSystemBootBackupConfigFile": juniSystemBootBackupConfigFile,
       "juniSystemRedundancyRevertControl": juniSystemRedundancyRevertControl,
       "juniSystemRedundancyRevertTimeOfDay": juniSystemRedundancyRevertTimeOfDay,
       "juniSystemMemUtilTrapEnable": juniSystemMemUtilTrapEnable,
       "juniSystemReloadSlotNumber": juniSystemReloadSlotNumber,
       "juniSystemUtilizationThresholdDirection": juniSystemUtilizationThresholdDirection,
       "juniSystemUtilizationTrapEnable": juniSystemUtilizationTrapEnable,
       "juniSystemMemKBytesCapacity": juniSystemMemKBytesCapacity,
       "juniSystemPortSfpPowerThresholdIfIndex": juniSystemPortSfpPowerThresholdIfIndex,
       "juniSystemPortSfpPowerThresholdValue": juniSystemPortSfpPowerThresholdValue,
       "juniSystemSubsystem": juniSystemSubsystem,
       "juniSystemSubsystemTable": juniSystemSubsystemTable,
       "juniSystemSubsystemEntry": juniSystemSubsystemEntry,
       "juniSystemSubsystemIndex": juniSystemSubsystemIndex,
       "juniSystemSubsystemName": juniSystemSubsystemName,
       "juniSystemSubsystemBootReleaseFile": juniSystemSubsystemBootReleaseFile,
       "juniSystemSubsystemBootBackupReleaseFile": juniSystemSubsystemBootBackupReleaseFile,
       "juniSystemModule": juniSystemModule,
       "juniSystemMaxSlotNumber": juniSystemMaxSlotNumber,
       "juniSystemMaxModulesPerSlot": juniSystemMaxModulesPerSlot,
       "juniSystemSlotTable": juniSystemSlotTable,
       "juniSystemSlotEntry": juniSystemSlotEntry,
       "juniSystemSlotNumber": juniSystemSlotNumber,
       "juniSystemSlotLevel": juniSystemSlotLevel,
       "juniSystemSlotStatus": juniSystemSlotStatus,
       "juniSystemSlotType": juniSystemSlotType,
       "juniSystemModuleTable": juniSystemModuleTable,
       "juniSystemModuleEntry": juniSystemModuleEntry,
       "juniSystemModuleOperStatus": juniSystemModuleOperStatus,
       "juniSystemModuleDisableReason": juniSystemModuleDisableReason,
       "juniSystemModuleLastChange": juniSystemModuleLastChange,
       "juniSystemModuleCurrentType": juniSystemModuleCurrentType,
       "juniSystemModuleExpectedType": juniSystemModuleExpectedType,
       "juniSystemModuleDescr": juniSystemModuleDescr,
       "juniSystemModuleSlotSpan": juniSystemModuleSlotSpan,
       "juniSystemModulePortCount": juniSystemModulePortCount,
       "juniSystemModuleSerialNumber": juniSystemModuleSerialNumber,
       "juniSystemModuleAssemblyPartNumber": juniSystemModuleAssemblyPartNumber,
       "juniSystemModuleAssemblyRev": juniSystemModuleAssemblyRev,
       "juniSystemModulePhysicalIndex": juniSystemModulePhysicalIndex,
       "juniSystemModuleSoftwareSupport": juniSystemModuleSoftwareSupport,
       "juniSystemModuleRedundancySupport": juniSystemModuleRedundancySupport,
       "juniSystemModuleLevelSpan": juniSystemModuleLevelSpan,
       "juniSystemModuleSoftwareTable": juniSystemModuleSoftwareTable,
       "juniSystemModuleSoftwareEntry": juniSystemModuleSoftwareEntry,
       "juniSystemModuleSoftwareVersion": juniSystemModuleSoftwareVersion,
       "juniSystemModuleCpuUtilPct": juniSystemModuleCpuUtilPct,
       "juniSystemModuleMemUtilPct": juniSystemModuleMemUtilPct,
       "juniSystemModuleAdminStatus": juniSystemModuleAdminStatus,
       "juniSystemModuleControl": juniSystemModuleControl,
       "juniSystemModuleBootReleaseFile": juniSystemModuleBootReleaseFile,
       "juniSystemModuleBootBackupReleaseFile": juniSystemModuleBootBackupReleaseFile,
       "juniSystemModuleCpuFiveSecUtilPct": juniSystemModuleCpuFiveSecUtilPct,
       "juniSystemModuleCpuOneMinAvgPct": juniSystemModuleCpuOneMinAvgPct,
       "juniSystemModuleCpuFiveMinAvgPct": juniSystemModuleCpuFiveMinAvgPct,
       "juniSystemModuleRedundancyTable": juniSystemModuleRedundancyTable,
       "juniSystemModuleRedundancyEntry": juniSystemModuleRedundancyEntry,
       "juniSystemModuleRedundancyGroupId": juniSystemModuleRedundancyGroupId,
       "juniSystemModuleRedundancySpare": juniSystemModuleRedundancySpare,
       "juniSystemModuleRedundancyAssociatedSlot": juniSystemModuleRedundancyAssociatedSlot,
       "juniSystemModuleRedundancyLockout": juniSystemModuleRedundancyLockout,
       "juniSystemModuleRedundancyRevertControl": juniSystemModuleRedundancyRevertControl,
       "juniSystemModuleRedundancyRevertTime": juniSystemModuleRedundancyRevertTime,
       "juniSystemPort": juniSystemPort,
       "juniSystemPortTable": juniSystemPortTable,
       "juniSystemPortEntry": juniSystemPortEntry,
       "juniSystemPortNumber": juniSystemPortNumber,
       "juniSystemPortIfIndex": juniSystemPortIfIndex,
       "juniSystemPortPhysicalIndex": juniSystemPortPhysicalIndex,
       "juniSystemTiming": juniSystemTiming,
       "juniSystemAdminTimingSource": juniSystemAdminTimingSource,
       "juniSystemOperTimingSource": juniSystemOperTimingSource,
       "juniSystemTimingAutoUpgrade": juniSystemTimingAutoUpgrade,
       "juniSystemTimingSelectorTable": juniSystemTimingSelectorTable,
       "juniSystemTimingSelectorEntry": juniSystemTimingSelectorEntry,
       "juniSystemTimingSelectorIndex": juniSystemTimingSelectorIndex,
       "juniSystemTimingSourceType": juniSystemTimingSourceType,
       "juniSystemTimingSourceIfIndex": juniSystemTimingSourceIfIndex,
       "juniSystemTimingSourceLine": juniSystemTimingSourceLine,
       "juniSystemTimingWorkingStatus": juniSystemTimingWorkingStatus,
       "juniSystemTimingProtectedStatus": juniSystemTimingProtectedStatus,
       "juniSystemFabric": juniSystemFabric,
       "juniSystemFabricSpeed": juniSystemFabricSpeed,
       "juniSystemFabricRev": juniSystemFabricRev,
       "juniSystemNvs": juniSystemNvs,
       "juniSystemNvsCount": juniSystemNvsCount,
       "juniSystemNvsTable": juniSystemNvsTable,
       "juniSystemNvsEntry": juniSystemNvsEntry,
       "juniSystemNvsIndex": juniSystemNvsIndex,
       "juniSystemNvsStatus": juniSystemNvsStatus,
       "juniSystemNvsCapacity": juniSystemNvsCapacity,
       "juniSystemNvsUtilPct": juniSystemNvsUtilPct,
       "juniSystemNvsPhysicalIndex": juniSystemNvsPhysicalIndex,
       "juniSystemPower": juniSystemPower,
       "juniSystemPowerCount": juniSystemPowerCount,
       "juniSystemPowerTable": juniSystemPowerTable,
       "juniSystemPowerEntry": juniSystemPowerEntry,
       "juniSystemPowerIndex": juniSystemPowerIndex,
       "juniSystemPowerStatus": juniSystemPowerStatus,
       "juniSystemPowerPhysicalIndex": juniSystemPowerPhysicalIndex,
       "juniSystemTemperature": juniSystemTemperature,
       "juniSystemFanCount": juniSystemFanCount,
       "juniSystemFanTable": juniSystemFanTable,
       "juniSystemFanEntry": juniSystemFanEntry,
       "juniSystemFanIndex": juniSystemFanIndex,
       "juniSystemFanStatus": juniSystemFanStatus,
       "juniSystemFanPhysicalIndex": juniSystemFanPhysicalIndex,
       "juniSystemTempCount": juniSystemTempCount,
       "juniSystemTempTable": juniSystemTempTable,
       "juniSystemTempEntry": juniSystemTempEntry,
       "juniSystemTempIndex": juniSystemTempIndex,
       "juniSystemTempStatus": juniSystemTempStatus,
       "juniSystemTempValue": juniSystemTempValue,
       "juniSystemTempPhysicalIndex": juniSystemTempPhysicalIndex,
       "juniSystemTempProtectionStatus": juniSystemTempProtectionStatus,
       "juniSystemTempProtectionHoldOffTime": juniSystemTempProtectionHoldOffTime,
       "juniSystemTempProtectionHoldOffTimeRemaining": juniSystemTempProtectionHoldOffTimeRemaining,
       "juniSystemUtilization": juniSystemUtilization,
       "juniSystemUtilizationTable": juniSystemUtilizationTable,
       "juniSystemUtilizationEntry": juniSystemUtilizationEntry,
       "juniSystemUtilizationResourceType": juniSystemUtilizationResourceType,
       "juniSystemUtilizationResourceSubType": juniSystemUtilizationResourceSubType,
       "juniSystemUtilizationLocationType": juniSystemUtilizationLocationType,
       "juniSystemUtilizationLocation": juniSystemUtilizationLocation,
       "juniSystemUtilizationMaxCapacity": juniSystemUtilizationMaxCapacity,
       "juniSystemUtilizationCurrentValue": juniSystemUtilizationCurrentValue,
       "juniSystemUtilizationThresholdRising": juniSystemUtilizationThresholdRising,
       "juniSystemUtilizationThresholdFalling": juniSystemUtilizationThresholdFalling,
       "juniSystemUtilizationHoldDownTime": juniSystemUtilizationHoldDownTime,
       "juniSystemCpuUtilizationTable": juniSystemCpuUtilizationTable,
       "juniSystemCpuUtilizationEntry": juniSystemCpuUtilizationEntry,
       "juniSystemCpuUtilizationTimeMark": juniSystemCpuUtilizationTimeMark,
       "juniSystemCpuUtilizationTaskName": juniSystemCpuUtilizationTaskName,
       "juniSystemCpuUtilizationInvoked": juniSystemCpuUtilizationInvoked,
       "juniSystemCpuUtilizationInvokationPerSec": juniSystemCpuUtilizationInvokationPerSec,
       "juniSystemCpuUtilizationTotalRunningTime": juniSystemCpuUtilizationTotalRunningTime,
       "juniSystemCpuUtilizationPercentageRunningTime": juniSystemCpuUtilizationPercentageRunningTime,
       "juniSystemCpuUtilizationAverageTimePerInvokation": juniSystemCpuUtilizationAverageTimePerInvokation,
       "juniSystemCpuUtilizationFiveSecondUtilization": juniSystemCpuUtilizationFiveSecondUtilization,
       "juniSystemCpuUtilizationOneMinuteUtilization": juniSystemCpuUtilizationOneMinuteUtilization,
       "juniSystemCpuUtilizationFiveMinuteUtilization": juniSystemCpuUtilizationFiveMinuteUtilization,
       "juniSystemCpuUtilizationNumberOfInstances": juniSystemCpuUtilizationNumberOfInstances,
       "juniSystemIssu": juniSystemIssu,
       "juniSystemIssuState": juniSystemIssuState,
       "juniSystemIssuRunningReleaseFile": juniSystemIssuRunningReleaseFile,
       "juniSystemIssuArmedReleaseFile": juniSystemIssuArmedReleaseFile,
       "juniSystemIssuStatus": juniSystemIssuStatus,
       "juniSystemIssuCriteriaTable": juniSystemIssuCriteriaTable,
       "juniSystemIssuCriteriaEntry": juniSystemIssuCriteriaEntry,
       "juniSystemIssuCriteriaIndex": juniSystemIssuCriteriaIndex,
       "juniSystemIssuCriteriaDescription": juniSystemIssuCriteriaDescription,
       "juniSystemIssuCriteriaStatus": juniSystemIssuCriteriaStatus,
       "juniSystemConformance": juniSystemConformance,
       "juniSystemCompliances": juniSystemCompliances,
       "juniSystemCompliance": juniSystemCompliance,
       "juniSystemCompliance2": juniSystemCompliance2,
       "juniSystemCompliance3": juniSystemCompliance3,
       "juniSystemCompliance4": juniSystemCompliance4,
       "juniSystemCompliance5": juniSystemCompliance5,
       "juniSystemCompliance6": juniSystemCompliance6,
       "juniSystemCompliance7": juniSystemCompliance7,
       "juniSystemCompliance8": juniSystemCompliance8,
       "juniSystemGroups": juniSystemGroups,
       "juniSystemGeneralGroup": juniSystemGeneralGroup,
       "juniSystemSubsystemGroup": juniSystemSubsystemGroup,
       "juniSystemModuleGroup": juniSystemModuleGroup,
       "juniSystemPortGroup": juniSystemPortGroup,
       "juniSystemTimingGroup": juniSystemTimingGroup,
       "juniSystemFabricGroup": juniSystemFabricGroup,
       "juniSystemNvsGroup": juniSystemNvsGroup,
       "juniSystemPowerGroup": juniSystemPowerGroup,
       "juniSystemTemperatureGroup": juniSystemTemperatureGroup,
       "juniSystemNotificationObjectsGroup": juniSystemNotificationObjectsGroup,
       "juniSystemNotificationGroup": juniSystemNotificationGroup,
       "juniSystemUtilizationGroup": juniSystemUtilizationGroup,
       "juniSystemNotificationGroup2": juniSystemNotificationGroup2,
       "juniSystemGeneralGroup2": juniSystemGeneralGroup2,
       "juniSystemModuleGroup2": juniSystemModuleGroup2,
       "juniSystemUtilizationGroup2": juniSystemUtilizationGroup2,
       "juniSystemModuleGroup3": juniSystemModuleGroup3,
       "juniSystemIssuGroup": juniSystemIssuGroup,
       "juniSystemNotificationGroup3": juniSystemNotificationGroup3,
       "juniSystemNotificationGroup4": juniSystemNotificationGroup4}
)
