# SNMP MIB module (CISCO-DMN-DSG-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-TIME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:35 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGTime = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23)
)
ciscoDSGTime.setRevisions(
        ("2010-08-30 11:00",
         "2010-04-12 06:00",
         "2009-12-20 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TimeInfo_ObjectIdentity = ObjectIdentity
timeInfo = _TimeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1)
)


class _TimeFormat_Type(Integer32):
    """Custom type timeFormat based on Integer32"""
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
        *(("twelveHr", 3),
          ("twelveHrSuspendZero", 4),
          ("twentyFourHr", 1),
          ("twentyFourHrSuspendZero", 2))
    )


_TimeFormat_Type.__name__ = "Integer32"
_TimeFormat_Object = MibScalar
timeFormat = _TimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 1),
    _TimeFormat_Type()
)
timeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeFormat.setStatus("current")


class _TimeDateFormat_Type(Integer32):
    """Custom type timeDateFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddmmyyyy", 2),
          ("mmddyyyy", 3),
          ("yyyymmdd", 1))
    )


_TimeDateFormat_Type.__name__ = "Integer32"
_TimeDateFormat_Object = MibScalar
timeDateFormat = _TimeDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 2),
    _TimeDateFormat_Type()
)
timeDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDateFormat.setStatus("current")


class _TimeGMTOffset_Type(Integer32):
    """Custom type timeGMTOffset based on Integer32"""
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
              33)
        )
    )
    namedValues = NamedValues(
        *(("minusEight", 5),
          ("minusEleven", 2),
          ("minusFive", 8),
          ("minusFour", 9),
          ("minusNine", 4),
          ("minusOne", 13),
          ("minusSeven", 6),
          ("minusSix", 7),
          ("minusTen", 3),
          ("minusThreeAndAHalf", 10),
          ("minusTwelve", 1),
          ("minusTwo", 12),
          ("plusEight", 27),
          ("plusEleven", 31),
          ("plusFive", 21),
          ("plusFiveAndAHalf", 22),
          ("plusFiveAndThreeQuarter", 23),
          ("plusFour", 19),
          ("plusFourAndAHalf", 20),
          ("plusNine", 28),
          ("plusNineAndAHalf", 29),
          ("plusOne", 15),
          ("plusSeven", 26),
          ("plusSix", 24),
          ("plusSixAndAHalf", 25),
          ("plusTen", 30),
          ("plusThirteen", 33),
          ("plusThree", 17),
          ("plusThreeAndAHalf", 18),
          ("plusTwelve", 32),
          ("plusTwo", 16),
          ("zeroGMT", 14))
    )


_TimeGMTOffset_Type.__name__ = "Integer32"
_TimeGMTOffset_Object = MibScalar
timeGMTOffset = _TimeGMTOffset_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 3),
    _TimeGMTOffset_Type()
)
timeGMTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeGMTOffset.setStatus("current")


class _TimeCurrent_Type(DisplayString):
    """Custom type timeCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TimeCurrent_Type.__name__ = "DisplayString"
_TimeCurrent_Object = MibScalar
timeCurrent = _TimeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 4),
    _TimeCurrent_Type()
)
timeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeCurrent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-TIME-MIB",
    **{"ciscoDSGTime": ciscoDSGTime,
       "timeInfo": timeInfo,
       "timeFormat": timeFormat,
       "timeDateFormat": timeDateFormat,
       "timeGMTOffset": timeGMTOffset,
       "timeCurrent": timeCurrent}
)
