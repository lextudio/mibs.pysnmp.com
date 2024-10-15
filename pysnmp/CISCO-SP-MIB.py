# SNMP MIB module (CISCO-SP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:43 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73)
)
ciscoSpMIB.setRevisions(
        ("2006-01-16 00:00",
         "2001-06-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CSpPointCode(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )



class CSpSs7Variant(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("itu", 2))
    )



class CSpLinkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sctpIp", 3),
          ("serial", 2))
    )



class CSpLinkSLC(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class CSpLinksetId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )



class CSpAclAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("discard", 2))
    )



class CSpOsiState(Integer32, TextualConvention):
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
        *(("active", 1),
          ("inactive", 2),
          ("inhibited", 3),
          ("noshut", 6),
          ("shut", 5),
          ("uninhibited", 4))
    )



class CSpAclId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )



class CSpRouteTableName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )



class CSpAclSi(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class CSpRouteStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("restricted", 2),
          ("unavailable", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSpMIBObjects = _CiscoSpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1)
)
_CSpScalars_ObjectIdentity = ObjectIdentity
cSpScalars = _CSpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1)
)
_CSpSs7Variant_Type = CSpSs7Variant
_CSpSs7Variant_Object = MibScalar
cSpSs7Variant = _CSpSs7Variant_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 1),
    _CSpSs7Variant_Type()
)
cSpSs7Variant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpSs7Variant.setStatus("current")
_CSpPointCode_Type = CSpPointCode
_CSpPointCode_Object = MibScalar
cSpPointCode = _CSpPointCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 2),
    _CSpPointCode_Type()
)
cSpPointCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpPointCode.setStatus("current")
_CSpMtp2T01_Type = Unsigned32
_CSpMtp2T01_Object = MibScalar
cSpMtp2T01 = _CSpMtp2T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 3),
    _CSpMtp2T01_Type()
)
cSpMtp2T01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp2T01.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp2T01.setUnits("milli-seconds")
_CSpMtp2T02_Type = Unsigned32
_CSpMtp2T02_Object = MibScalar
cSpMtp2T02 = _CSpMtp2T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 4),
    _CSpMtp2T02_Type()
)
cSpMtp2T02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp2T02.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp2T02.setUnits("100 milli-seconds")
_CSpMtp2T03_Type = Unsigned32
_CSpMtp2T03_Object = MibScalar
cSpMtp2T03 = _CSpMtp2T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 5),
    _CSpMtp2T03_Type()
)
cSpMtp2T03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp2T03.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp2T03.setUnits("milli-seconds")
_CSpMtp2T4N_Type = Unsigned32
_CSpMtp2T4N_Object = MibScalar
cSpMtp2T4N = _CSpMtp2T4N_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 6),
    _CSpMtp2T4N_Type()
)
cSpMtp2T4N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp2T4N.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp2T4N.setUnits("milli-seconds")
_CSpMtp2T4E_Type = Unsigned32
_CSpMtp2T4E_Object = MibScalar
cSpMtp2T4E = _CSpMtp2T4E_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 7),
    _CSpMtp2T4E_Type()
)
cSpMtp2T4E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp2T4E.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp2T4E.setUnits("milli-seconds")
_CSpMtp2T05_Type = Unsigned32
_CSpMtp2T05_Object = MibScalar
cSpMtp2T05 = _CSpMtp2T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 8),
    _CSpMtp2T05_Type()
)
cSpMtp2T05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp2T05.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp2T05.setUnits("milli-seconds")
_CSpMtp2T06_Type = Unsigned32
_CSpMtp2T06_Object = MibScalar
cSpMtp2T06 = _CSpMtp2T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 9),
    _CSpMtp2T06_Type()
)
cSpMtp2T06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp2T06.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp2T06.setUnits("milli-seconds.")
_CSpMtp2T07_Type = Unsigned32
_CSpMtp2T07_Object = MibScalar
cSpMtp2T07 = _CSpMtp2T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 10),
    _CSpMtp2T07_Type()
)
cSpMtp2T07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp2T07.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp2T07.setUnits("milli-seconds.")
_CSpMtp2T08_Type = Unsigned32
_CSpMtp2T08_Object = MibScalar
cSpMtp2T08 = _CSpMtp2T08_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 11),
    _CSpMtp2T08_Type()
)
cSpMtp2T08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp2T08.setStatus("current")
_CSpMtp3T01_Type = Unsigned32
_CSpMtp3T01_Object = MibScalar
cSpMtp3T01 = _CSpMtp3T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 12),
    _CSpMtp3T01_Type()
)
cSpMtp3T01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T01.setStatus("current")
_CSpMtp3T02_Type = Unsigned32
_CSpMtp3T02_Object = MibScalar
cSpMtp3T02 = _CSpMtp3T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 13),
    _CSpMtp3T02_Type()
)
cSpMtp3T02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T02.setStatus("current")
_CSpMtp3T03_Type = Unsigned32
_CSpMtp3T03_Object = MibScalar
cSpMtp3T03 = _CSpMtp3T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 14),
    _CSpMtp3T03_Type()
)
cSpMtp3T03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T03.setStatus("current")
_CSpMtp3T04_Type = Unsigned32
_CSpMtp3T04_Object = MibScalar
cSpMtp3T04 = _CSpMtp3T04_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 15),
    _CSpMtp3T04_Type()
)
cSpMtp3T04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T04.setStatus("current")
_CSpMtp3T05_Type = Unsigned32
_CSpMtp3T05_Object = MibScalar
cSpMtp3T05 = _CSpMtp3T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 16),
    _CSpMtp3T05_Type()
)
cSpMtp3T05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T05.setStatus("current")
_CSpMtp3T06_Type = Unsigned32
_CSpMtp3T06_Object = MibScalar
cSpMtp3T06 = _CSpMtp3T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 17),
    _CSpMtp3T06_Type()
)
cSpMtp3T06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T06.setStatus("current")
_CSpMtp3T07_Type = Unsigned32
_CSpMtp3T07_Object = MibScalar
cSpMtp3T07 = _CSpMtp3T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 18),
    _CSpMtp3T07_Type()
)
cSpMtp3T07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T07.setStatus("current")
_CSpMtp3T08_Type = Unsigned32
_CSpMtp3T08_Object = MibScalar
cSpMtp3T08 = _CSpMtp3T08_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 19),
    _CSpMtp3T08_Type()
)
cSpMtp3T08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T08.setStatus("current")
_CSpMtp3T10_Type = Unsigned32
_CSpMtp3T10_Object = MibScalar
cSpMtp3T10 = _CSpMtp3T10_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 20),
    _CSpMtp3T10_Type()
)
cSpMtp3T10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T10.setStatus("current")
_CSpMtp3T11_Type = Unsigned32
_CSpMtp3T11_Object = MibScalar
cSpMtp3T11 = _CSpMtp3T11_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 21),
    _CSpMtp3T11_Type()
)
cSpMtp3T11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T11.setStatus("current")
_CSpMtp3T12_Type = Unsigned32
_CSpMtp3T12_Object = MibScalar
cSpMtp3T12 = _CSpMtp3T12_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 22),
    _CSpMtp3T12_Type()
)
cSpMtp3T12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T12.setStatus("current")
_CSpMtp3T13_Type = Unsigned32
_CSpMtp3T13_Object = MibScalar
cSpMtp3T13 = _CSpMtp3T13_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 23),
    _CSpMtp3T13_Type()
)
cSpMtp3T13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T13.setStatus("current")
_CSpMtp3T14_Type = Unsigned32
_CSpMtp3T14_Object = MibScalar
cSpMtp3T14 = _CSpMtp3T14_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 24),
    _CSpMtp3T14_Type()
)
cSpMtp3T14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T14.setStatus("current")
_CSpMtp3T15_Type = Unsigned32
_CSpMtp3T15_Object = MibScalar
cSpMtp3T15 = _CSpMtp3T15_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 25),
    _CSpMtp3T15_Type()
)
cSpMtp3T15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T15.setStatus("current")
_CSpMtp3T16_Type = Unsigned32
_CSpMtp3T16_Object = MibScalar
cSpMtp3T16 = _CSpMtp3T16_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 26),
    _CSpMtp3T16_Type()
)
cSpMtp3T16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T16.setStatus("current")
_CSpMtp3T17_Type = Unsigned32
_CSpMtp3T17_Object = MibScalar
cSpMtp3T17 = _CSpMtp3T17_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 27),
    _CSpMtp3T17_Type()
)
cSpMtp3T17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T17.setStatus("current")
_CSpMtp3T18_Type = Unsigned32
_CSpMtp3T18_Object = MibScalar
cSpMtp3T18 = _CSpMtp3T18_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 28),
    _CSpMtp3T18_Type()
)
cSpMtp3T18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T18.setStatus("current")
_CSpMtp3T19_Type = Unsigned32
_CSpMtp3T19_Object = MibScalar
cSpMtp3T19 = _CSpMtp3T19_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 29),
    _CSpMtp3T19_Type()
)
cSpMtp3T19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T19.setStatus("current")
_CSpMtp3T20_Type = Unsigned32
_CSpMtp3T20_Object = MibScalar
cSpMtp3T20 = _CSpMtp3T20_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 30),
    _CSpMtp3T20_Type()
)
cSpMtp3T20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T20.setStatus("current")
_CSpMtp3T21_Type = Unsigned32
_CSpMtp3T21_Object = MibScalar
cSpMtp3T21 = _CSpMtp3T21_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 31),
    _CSpMtp3T21_Type()
)
cSpMtp3T21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T21.setStatus("current")
_CSpMtp3T22_Type = Unsigned32
_CSpMtp3T22_Object = MibScalar
cSpMtp3T22 = _CSpMtp3T22_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 32),
    _CSpMtp3T22_Type()
)
cSpMtp3T22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T22.setStatus("current")
_CSpMtp3T23_Type = Unsigned32
_CSpMtp3T23_Object = MibScalar
cSpMtp3T23 = _CSpMtp3T23_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 33),
    _CSpMtp3T23_Type()
)
cSpMtp3T23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T23.setStatus("current")
_CSpMtp3T24_Type = Unsigned32
_CSpMtp3T24_Object = MibScalar
cSpMtp3T24 = _CSpMtp3T24_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 34),
    _CSpMtp3T24_Type()
)
cSpMtp3T24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T24.setStatus("current")
_CSpMtp3T25_Type = Unsigned32
_CSpMtp3T25_Object = MibScalar
cSpMtp3T25 = _CSpMtp3T25_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 35),
    _CSpMtp3T25_Type()
)
cSpMtp3T25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T25.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T25.setUnits("seconds.")
_CSpMtp3T26_Type = Unsigned32
_CSpMtp3T26_Object = MibScalar
cSpMtp3T26 = _CSpMtp3T26_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 36),
    _CSpMtp3T26_Type()
)
cSpMtp3T26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T26.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T26.setUnits("seconds.")
_CSpMtp3T27_Type = Unsigned32
_CSpMtp3T27_Object = MibScalar
cSpMtp3T27 = _CSpMtp3T27_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 37),
    _CSpMtp3T27_Type()
)
cSpMtp3T27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T27.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T27.setUnits("seconds.")
_CSpMtp3T28_Type = Unsigned32
_CSpMtp3T28_Object = MibScalar
cSpMtp3T28 = _CSpMtp3T28_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 38),
    _CSpMtp3T28_Type()
)
cSpMtp3T28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T28.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T28.setUnits("seconds.")
_CSpMtp3T29_Type = Unsigned32
_CSpMtp3T29_Object = MibScalar
cSpMtp3T29 = _CSpMtp3T29_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 39),
    _CSpMtp3T29_Type()
)
cSpMtp3T29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T29.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T29.setUnits("seconds.")
_CSpMtp3T30_Type = Unsigned32
_CSpMtp3T30_Object = MibScalar
cSpMtp3T30 = _CSpMtp3T30_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 40),
    _CSpMtp3T30_Type()
)
cSpMtp3T30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T30.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T30.setUnits("seconds.")
_CSpMtp3T31_Type = Unsigned32
_CSpMtp3T31_Object = MibScalar
cSpMtp3T31 = _CSpMtp3T31_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 41),
    _CSpMtp3T31_Type()
)
cSpMtp3T31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T31.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T31.setUnits("seconds.")
_CSpMtp3T32_Type = Unsigned32
_CSpMtp3T32_Object = MibScalar
cSpMtp3T32 = _CSpMtp3T32_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 42),
    _CSpMtp3T32_Type()
)
cSpMtp3T32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T32.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T32.setUnits("seconds.")
_CSpMtp3T33_Type = Unsigned32
_CSpMtp3T33_Object = MibScalar
cSpMtp3T33 = _CSpMtp3T33_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 43),
    _CSpMtp3T33_Type()
)
cSpMtp3T33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T33.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T33.setUnits("seconds.")
_CSpMtp3T34_Type = Unsigned32
_CSpMtp3T34_Object = MibScalar
cSpMtp3T34 = _CSpMtp3T34_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 1, 44),
    _CSpMtp3T34_Type()
)
cSpMtp3T34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpMtp3T34.setStatus("current")
if mibBuilder.loadTexts:
    cSpMtp3T34.setUnits("seconds.")
_CSpLinkset_ObjectIdentity = ObjectIdentity
cSpLinkset = _CSpLinkset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2)
)
_CSpLinksetTable_Object = MibTable
cSpLinksetTable = _CSpLinksetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cSpLinksetTable.setStatus("current")
_CSpLinksetTableEntry_Object = MibTableRow
cSpLinksetTableEntry = _CSpLinksetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1)
)
cSpLinksetTableEntry.setIndexNames(
    (0, "CISCO-SP-MIB", "cSpLinksetName"),
)
if mibBuilder.loadTexts:
    cSpLinksetTableEntry.setStatus("current")
_CSpLinksetName_Type = CSpLinksetId
_CSpLinksetName_Object = MibTableColumn
cSpLinksetName = _CSpLinksetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 1),
    _CSpLinksetName_Type()
)
cSpLinksetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpLinksetName.setStatus("current")
_CSpLinksetAdjacentPointCode_Type = CSpPointCode
_CSpLinksetAdjacentPointCode_Object = MibTableColumn
cSpLinksetAdjacentPointCode = _CSpLinksetAdjacentPointCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 2),
    _CSpLinksetAdjacentPointCode_Type()
)
cSpLinksetAdjacentPointCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetAdjacentPointCode.setStatus("current")
_CSpLinksetState_Type = CSpOsiState
_CSpLinksetState_Object = MibTableColumn
cSpLinksetState = _CSpLinksetState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 3),
    _CSpLinksetState_Type()
)
cSpLinksetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetState.setStatus("current")
_CSpLinksetInboundAcl_Type = CSpAclId
_CSpLinksetInboundAcl_Object = MibTableColumn
cSpLinksetInboundAcl = _CSpLinksetInboundAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 4),
    _CSpLinksetInboundAcl_Type()
)
cSpLinksetInboundAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetInboundAcl.setStatus("current")
_CSpLinksetOutboundAcl_Type = CSpAclId
_CSpLinksetOutboundAcl_Object = MibTableColumn
cSpLinksetOutboundAcl = _CSpLinksetOutboundAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 5),
    _CSpLinksetOutboundAcl_Type()
)
cSpLinksetOutboundAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetOutboundAcl.setStatus("current")
_CSpLinksetSnmmRouteTableName_Type = CSpRouteTableName
_CSpLinksetSnmmRouteTableName_Object = MibTableColumn
cSpLinksetSnmmRouteTableName = _CSpLinksetSnmmRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 6),
    _CSpLinksetSnmmRouteTableName_Type()
)
cSpLinksetSnmmRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSnmmRouteTableName.setStatus("current")
_CSpLinksetSntmRouteTableName_Type = CSpRouteTableName
_CSpLinksetSntmRouteTableName_Object = MibTableColumn
cSpLinksetSntmRouteTableName = _CSpLinksetSntmRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 7),
    _CSpLinksetSntmRouteTableName_Type()
)
cSpLinksetSntmRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSntmRouteTableName.setStatus("current")
_CSpLinksetSpare2RouteTableName_Type = CSpRouteTableName
_CSpLinksetSpare2RouteTableName_Object = MibTableColumn
cSpLinksetSpare2RouteTableName = _CSpLinksetSpare2RouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 8),
    _CSpLinksetSpare2RouteTableName_Type()
)
cSpLinksetSpare2RouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSpare2RouteTableName.setStatus("current")
_CSpLinksetSccpRouteTableName_Type = CSpRouteTableName
_CSpLinksetSccpRouteTableName_Object = MibTableColumn
cSpLinksetSccpRouteTableName = _CSpLinksetSccpRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 9),
    _CSpLinksetSccpRouteTableName_Type()
)
cSpLinksetSccpRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSccpRouteTableName.setStatus("current")
_CSpLinksetTupRouteTableName_Type = CSpRouteTableName
_CSpLinksetTupRouteTableName_Object = MibTableColumn
cSpLinksetTupRouteTableName = _CSpLinksetTupRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 10),
    _CSpLinksetTupRouteTableName_Type()
)
cSpLinksetTupRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetTupRouteTableName.setStatus("current")
_CSpLinksetIsupRouteTableName_Type = CSpRouteTableName
_CSpLinksetIsupRouteTableName_Object = MibTableColumn
cSpLinksetIsupRouteTableName = _CSpLinksetIsupRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 11),
    _CSpLinksetIsupRouteTableName_Type()
)
cSpLinksetIsupRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetIsupRouteTableName.setStatus("current")
_CSpLinksetDupcRouteTableName_Type = CSpRouteTableName
_CSpLinksetDupcRouteTableName_Object = MibTableColumn
cSpLinksetDupcRouteTableName = _CSpLinksetDupcRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 12),
    _CSpLinksetDupcRouteTableName_Type()
)
cSpLinksetDupcRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetDupcRouteTableName.setStatus("current")
_CSpLinksetDupfRouteTableName_Type = CSpRouteTableName
_CSpLinksetDupfRouteTableName_Object = MibTableColumn
cSpLinksetDupfRouteTableName = _CSpLinksetDupfRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 13),
    _CSpLinksetDupfRouteTableName_Type()
)
cSpLinksetDupfRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetDupfRouteTableName.setStatus("current")
_CSpLinksetMtupRouteTableName_Type = CSpRouteTableName
_CSpLinksetMtupRouteTableName_Object = MibTableColumn
cSpLinksetMtupRouteTableName = _CSpLinksetMtupRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 14),
    _CSpLinksetMtupRouteTableName_Type()
)
cSpLinksetMtupRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtupRouteTableName.setStatus("current")
_CSpLinksetBisupRouteTableName_Type = CSpRouteTableName
_CSpLinksetBisupRouteTableName_Object = MibTableColumn
cSpLinksetBisupRouteTableName = _CSpLinksetBisupRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 15),
    _CSpLinksetBisupRouteTableName_Type()
)
cSpLinksetBisupRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetBisupRouteTableName.setStatus("current")
_CSpLinksetSisupRouteTableName_Type = CSpRouteTableName
_CSpLinksetSisupRouteTableName_Object = MibTableColumn
cSpLinksetSisupRouteTableName = _CSpLinksetSisupRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 16),
    _CSpLinksetSisupRouteTableName_Type()
)
cSpLinksetSisupRouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSisupRouteTableName.setStatus("current")
_CSpLinksetSpare11RouteTableName_Type = CSpRouteTableName
_CSpLinksetSpare11RouteTableName_Object = MibTableColumn
cSpLinksetSpare11RouteTableName = _CSpLinksetSpare11RouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 17),
    _CSpLinksetSpare11RouteTableName_Type()
)
cSpLinksetSpare11RouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSpare11RouteTableName.setStatus("current")
_CSpLinksetSpare12RouteTableName_Type = CSpRouteTableName
_CSpLinksetSpare12RouteTableName_Object = MibTableColumn
cSpLinksetSpare12RouteTableName = _CSpLinksetSpare12RouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 18),
    _CSpLinksetSpare12RouteTableName_Type()
)
cSpLinksetSpare12RouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSpare12RouteTableName.setStatus("current")
_CSpLinksetSpare13RouteTableName_Type = CSpRouteTableName
_CSpLinksetSpare13RouteTableName_Object = MibTableColumn
cSpLinksetSpare13RouteTableName = _CSpLinksetSpare13RouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 19),
    _CSpLinksetSpare13RouteTableName_Type()
)
cSpLinksetSpare13RouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSpare13RouteTableName.setStatus("current")
_CSpLinksetSpare14RouteTableName_Type = CSpRouteTableName
_CSpLinksetSpare14RouteTableName_Object = MibTableColumn
cSpLinksetSpare14RouteTableName = _CSpLinksetSpare14RouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 20),
    _CSpLinksetSpare14RouteTableName_Type()
)
cSpLinksetSpare14RouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSpare14RouteTableName.setStatus("current")
_CSpLinksetSpare15RouteTableName_Type = CSpRouteTableName
_CSpLinksetSpare15RouteTableName_Object = MibTableColumn
cSpLinksetSpare15RouteTableName = _CSpLinksetSpare15RouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 21),
    _CSpLinksetSpare15RouteTableName_Type()
)
cSpLinksetSpare15RouteTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetSpare15RouteTableName.setStatus("current")


class _CSpLinksetAccountingEnabled_Type(TruthValue):
    """Custom type cSpLinksetAccountingEnabled based on TruthValue"""


_CSpLinksetAccountingEnabled_Object = MibTableColumn
cSpLinksetAccountingEnabled = _CSpLinksetAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 22),
    _CSpLinksetAccountingEnabled_Type()
)
cSpLinksetAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetAccountingEnabled.setStatus("current")
_CSpLinksetNumLinks_Type = Unsigned32
_CSpLinksetNumLinks_Object = MibTableColumn
cSpLinksetNumLinks = _CSpLinksetNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 23),
    _CSpLinksetNumLinks_Type()
)
cSpLinksetNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetNumLinks.setStatus("current")
_CSpLinksetPacketsSent_Type = Counter32
_CSpLinksetPacketsSent_Object = MibTableColumn
cSpLinksetPacketsSent = _CSpLinksetPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 24),
    _CSpLinksetPacketsSent_Type()
)
cSpLinksetPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetPacketsSent.setUnits("packets")
_CSpLinksetHCPacketsSent_Type = Counter64
_CSpLinksetHCPacketsSent_Object = MibTableColumn
cSpLinksetHCPacketsSent = _CSpLinksetHCPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 25),
    _CSpLinksetHCPacketsSent_Type()
)
cSpLinksetHCPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetHCPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetHCPacketsSent.setUnits("packets")
_CSpLinksetPacketsRcvd_Type = Counter32
_CSpLinksetPacketsRcvd_Object = MibTableColumn
cSpLinksetPacketsRcvd = _CSpLinksetPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 26),
    _CSpLinksetPacketsRcvd_Type()
)
cSpLinksetPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetPacketsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetPacketsRcvd.setUnits("packets")
_CSpLinksetHCPacketsRcvd_Type = Counter64
_CSpLinksetHCPacketsRcvd_Object = MibTableColumn
cSpLinksetHCPacketsRcvd = _CSpLinksetHCPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 27),
    _CSpLinksetHCPacketsRcvd_Type()
)
cSpLinksetHCPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetHCPacketsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetHCPacketsRcvd.setUnits("packets")
_CSpLinksetBytesSent_Type = Counter32
_CSpLinksetBytesSent_Object = MibTableColumn
cSpLinksetBytesSent = _CSpLinksetBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 28),
    _CSpLinksetBytesSent_Type()
)
cSpLinksetBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetBytesSent.setUnits("bytes")
_CSpLinksetHCBytesSent_Type = Counter64
_CSpLinksetHCBytesSent_Object = MibTableColumn
cSpLinksetHCBytesSent = _CSpLinksetHCBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 29),
    _CSpLinksetHCBytesSent_Type()
)
cSpLinksetHCBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetHCBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetHCBytesSent.setUnits("bytes")
_CSpLinksetBytesRcvd_Type = Counter32
_CSpLinksetBytesRcvd_Object = MibTableColumn
cSpLinksetBytesRcvd = _CSpLinksetBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 30),
    _CSpLinksetBytesRcvd_Type()
)
cSpLinksetBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetBytesRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetBytesRcvd.setUnits("bytes")
_CSpLinksetHCBytesRcvd_Type = Counter64
_CSpLinksetHCBytesRcvd_Object = MibTableColumn
cSpLinksetHCBytesRcvd = _CSpLinksetHCBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 31),
    _CSpLinksetHCBytesRcvd_Type()
)
cSpLinksetHCBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetHCBytesRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetHCBytesRcvd.setUnits("bytes")
_CSpLinksetDurationInService_Type = TimeTicks
_CSpLinksetDurationInService_Object = MibTableColumn
cSpLinksetDurationInService = _CSpLinksetDurationInService_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 32),
    _CSpLinksetDurationInService_Type()
)
cSpLinksetDurationInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetDurationInService.setStatus("current")
_CSpLinksetDurationOutService_Type = TimeTicks
_CSpLinksetDurationOutService_Object = MibTableColumn
cSpLinksetDurationOutService = _CSpLinksetDurationOutService_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 33),
    _CSpLinksetDurationOutService_Type()
)
cSpLinksetDurationOutService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetDurationOutService.setStatus("current")
_CSpLinksetMtp2T01_Type = Unsigned32
_CSpLinksetMtp2T01_Object = MibTableColumn
cSpLinksetMtp2T01 = _CSpLinksetMtp2T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 34),
    _CSpLinksetMtp2T01_Type()
)
cSpLinksetMtp2T01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T01.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T01.setUnits("100 milli-seconds")
_CSpLinksetMtp2T02_Type = Unsigned32
_CSpLinksetMtp2T02_Object = MibTableColumn
cSpLinksetMtp2T02 = _CSpLinksetMtp2T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 35),
    _CSpLinksetMtp2T02_Type()
)
cSpLinksetMtp2T02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T02.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T02.setUnits("100 milli-seconds")
_CSpLinksetMtp2T03_Type = Unsigned32
_CSpLinksetMtp2T03_Object = MibTableColumn
cSpLinksetMtp2T03 = _CSpLinksetMtp2T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 36),
    _CSpLinksetMtp2T03_Type()
)
cSpLinksetMtp2T03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T03.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T03.setUnits("100 milli-seconds")
_CSpLinksetMtp2T4N_Type = Unsigned32
_CSpLinksetMtp2T4N_Object = MibTableColumn
cSpLinksetMtp2T4N = _CSpLinksetMtp2T4N_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 37),
    _CSpLinksetMtp2T4N_Type()
)
cSpLinksetMtp2T4N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T4N.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T4N.setUnits("100 milli-seconds")
_CSpLinksetMtp2T4E_Type = Unsigned32
_CSpLinksetMtp2T4E_Object = MibTableColumn
cSpLinksetMtp2T4E = _CSpLinksetMtp2T4E_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 38),
    _CSpLinksetMtp2T4E_Type()
)
cSpLinksetMtp2T4E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T4E.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T4E.setUnits("100 milli-seconds")
_CSpLinksetMtp2T05_Type = Unsigned32
_CSpLinksetMtp2T05_Object = MibTableColumn
cSpLinksetMtp2T05 = _CSpLinksetMtp2T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 39),
    _CSpLinksetMtp2T05_Type()
)
cSpLinksetMtp2T05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T05.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T05.setUnits("milli-seconds")
_CSpLinksetMtp2T06_Type = Unsigned32
_CSpLinksetMtp2T06_Object = MibTableColumn
cSpLinksetMtp2T06 = _CSpLinksetMtp2T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 40),
    _CSpLinksetMtp2T06_Type()
)
cSpLinksetMtp2T06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T06.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T06.setUnits("100 milli-seconds.")
_CSpLinksetMtp2T07_Type = Unsigned32
_CSpLinksetMtp2T07_Object = MibTableColumn
cSpLinksetMtp2T07 = _CSpLinksetMtp2T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 41),
    _CSpLinksetMtp2T07_Type()
)
cSpLinksetMtp2T07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T07.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T07.setUnits("100 milli-seconds.")
_CSpLinksetMtp2T08_Type = Unsigned32
_CSpLinksetMtp2T08_Object = MibTableColumn
cSpLinksetMtp2T08 = _CSpLinksetMtp2T08_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 42),
    _CSpLinksetMtp2T08_Type()
)
cSpLinksetMtp2T08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp2T08.setStatus("current")
_CSpLinksetMtp3T01_Type = Unsigned32
_CSpLinksetMtp3T01_Object = MibTableColumn
cSpLinksetMtp3T01 = _CSpLinksetMtp3T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 43),
    _CSpLinksetMtp3T01_Type()
)
cSpLinksetMtp3T01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T01.setStatus("current")
_CSpLinksetMtp3T02_Type = Unsigned32
_CSpLinksetMtp3T02_Object = MibTableColumn
cSpLinksetMtp3T02 = _CSpLinksetMtp3T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 44),
    _CSpLinksetMtp3T02_Type()
)
cSpLinksetMtp3T02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T02.setStatus("current")
_CSpLinksetMtp3T03_Type = Unsigned32
_CSpLinksetMtp3T03_Object = MibTableColumn
cSpLinksetMtp3T03 = _CSpLinksetMtp3T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 45),
    _CSpLinksetMtp3T03_Type()
)
cSpLinksetMtp3T03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T03.setStatus("current")
_CSpLinksetMtp3T04_Type = Unsigned32
_CSpLinksetMtp3T04_Object = MibTableColumn
cSpLinksetMtp3T04 = _CSpLinksetMtp3T04_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 46),
    _CSpLinksetMtp3T04_Type()
)
cSpLinksetMtp3T04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T04.setStatus("current")
_CSpLinksetMtp3T05_Type = Unsigned32
_CSpLinksetMtp3T05_Object = MibTableColumn
cSpLinksetMtp3T05 = _CSpLinksetMtp3T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 47),
    _CSpLinksetMtp3T05_Type()
)
cSpLinksetMtp3T05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T05.setStatus("current")
_CSpLinksetMtp3T06_Type = Unsigned32
_CSpLinksetMtp3T06_Object = MibTableColumn
cSpLinksetMtp3T06 = _CSpLinksetMtp3T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 48),
    _CSpLinksetMtp3T06_Type()
)
cSpLinksetMtp3T06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T06.setStatus("current")
_CSpLinksetMtp3T07_Type = Unsigned32
_CSpLinksetMtp3T07_Object = MibTableColumn
cSpLinksetMtp3T07 = _CSpLinksetMtp3T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 49),
    _CSpLinksetMtp3T07_Type()
)
cSpLinksetMtp3T07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T07.setStatus("current")
_CSpLinksetMtp3T08_Type = Unsigned32
_CSpLinksetMtp3T08_Object = MibTableColumn
cSpLinksetMtp3T08 = _CSpLinksetMtp3T08_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 50),
    _CSpLinksetMtp3T08_Type()
)
cSpLinksetMtp3T08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T08.setStatus("current")
_CSpLinksetMtp3T10_Type = Unsigned32
_CSpLinksetMtp3T10_Object = MibTableColumn
cSpLinksetMtp3T10 = _CSpLinksetMtp3T10_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 51),
    _CSpLinksetMtp3T10_Type()
)
cSpLinksetMtp3T10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T10.setStatus("current")
_CSpLinksetMtp3T11_Type = Unsigned32
_CSpLinksetMtp3T11_Object = MibTableColumn
cSpLinksetMtp3T11 = _CSpLinksetMtp3T11_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 52),
    _CSpLinksetMtp3T11_Type()
)
cSpLinksetMtp3T11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T11.setStatus("current")
_CSpLinksetMtp3T12_Type = Unsigned32
_CSpLinksetMtp3T12_Object = MibTableColumn
cSpLinksetMtp3T12 = _CSpLinksetMtp3T12_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 53),
    _CSpLinksetMtp3T12_Type()
)
cSpLinksetMtp3T12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T12.setStatus("current")
_CSpLinksetMtp3T13_Type = Unsigned32
_CSpLinksetMtp3T13_Object = MibTableColumn
cSpLinksetMtp3T13 = _CSpLinksetMtp3T13_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 54),
    _CSpLinksetMtp3T13_Type()
)
cSpLinksetMtp3T13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T13.setStatus("current")
_CSpLinksetMtp3T14_Type = Unsigned32
_CSpLinksetMtp3T14_Object = MibTableColumn
cSpLinksetMtp3T14 = _CSpLinksetMtp3T14_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 55),
    _CSpLinksetMtp3T14_Type()
)
cSpLinksetMtp3T14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T14.setStatus("current")
_CSpLinksetMtp3T15_Type = Unsigned32
_CSpLinksetMtp3T15_Object = MibTableColumn
cSpLinksetMtp3T15 = _CSpLinksetMtp3T15_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 56),
    _CSpLinksetMtp3T15_Type()
)
cSpLinksetMtp3T15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T15.setStatus("current")
_CSpLinksetMtp3T16_Type = Unsigned32
_CSpLinksetMtp3T16_Object = MibTableColumn
cSpLinksetMtp3T16 = _CSpLinksetMtp3T16_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 57),
    _CSpLinksetMtp3T16_Type()
)
cSpLinksetMtp3T16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T16.setStatus("current")
_CSpLinksetMtp3T17_Type = Unsigned32
_CSpLinksetMtp3T17_Object = MibTableColumn
cSpLinksetMtp3T17 = _CSpLinksetMtp3T17_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 58),
    _CSpLinksetMtp3T17_Type()
)
cSpLinksetMtp3T17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T17.setStatus("current")
_CSpLinksetMtp3T18_Type = Unsigned32
_CSpLinksetMtp3T18_Object = MibTableColumn
cSpLinksetMtp3T18 = _CSpLinksetMtp3T18_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 59),
    _CSpLinksetMtp3T18_Type()
)
cSpLinksetMtp3T18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T18.setStatus("current")
_CSpLinksetMtp3T19_Type = Unsigned32
_CSpLinksetMtp3T19_Object = MibTableColumn
cSpLinksetMtp3T19 = _CSpLinksetMtp3T19_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 60),
    _CSpLinksetMtp3T19_Type()
)
cSpLinksetMtp3T19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T19.setStatus("current")
_CSpLinksetMtp3T20_Type = Unsigned32
_CSpLinksetMtp3T20_Object = MibTableColumn
cSpLinksetMtp3T20 = _CSpLinksetMtp3T20_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 61),
    _CSpLinksetMtp3T20_Type()
)
cSpLinksetMtp3T20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T20.setStatus("current")
_CSpLinksetMtp3T21_Type = Unsigned32
_CSpLinksetMtp3T21_Object = MibTableColumn
cSpLinksetMtp3T21 = _CSpLinksetMtp3T21_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 62),
    _CSpLinksetMtp3T21_Type()
)
cSpLinksetMtp3T21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T21.setStatus("current")
_CSpLinksetMtp3T22_Type = Unsigned32
_CSpLinksetMtp3T22_Object = MibTableColumn
cSpLinksetMtp3T22 = _CSpLinksetMtp3T22_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 63),
    _CSpLinksetMtp3T22_Type()
)
cSpLinksetMtp3T22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T22.setStatus("current")
_CSpLinksetMtp3T23_Type = Unsigned32
_CSpLinksetMtp3T23_Object = MibTableColumn
cSpLinksetMtp3T23 = _CSpLinksetMtp3T23_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 64),
    _CSpLinksetMtp3T23_Type()
)
cSpLinksetMtp3T23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T23.setStatus("current")
_CSpLinksetMtp3T24_Type = Unsigned32
_CSpLinksetMtp3T24_Object = MibTableColumn
cSpLinksetMtp3T24 = _CSpLinksetMtp3T24_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 65),
    _CSpLinksetMtp3T24_Type()
)
cSpLinksetMtp3T24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T24.setStatus("current")
_CSpLinksetMtp3T25_Type = Unsigned32
_CSpLinksetMtp3T25_Object = MibTableColumn
cSpLinksetMtp3T25 = _CSpLinksetMtp3T25_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 66),
    _CSpLinksetMtp3T25_Type()
)
cSpLinksetMtp3T25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T25.setStatus("current")
_CSpLinksetMtp3T26_Type = Unsigned32
_CSpLinksetMtp3T26_Object = MibTableColumn
cSpLinksetMtp3T26 = _CSpLinksetMtp3T26_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 67),
    _CSpLinksetMtp3T26_Type()
)
cSpLinksetMtp3T26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T26.setStatus("current")
_CSpLinksetMtp3T27_Type = Unsigned32
_CSpLinksetMtp3T27_Object = MibTableColumn
cSpLinksetMtp3T27 = _CSpLinksetMtp3T27_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 68),
    _CSpLinksetMtp3T27_Type()
)
cSpLinksetMtp3T27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T27.setStatus("current")
_CSpLinksetMtp3T28_Type = Unsigned32
_CSpLinksetMtp3T28_Object = MibTableColumn
cSpLinksetMtp3T28 = _CSpLinksetMtp3T28_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 69),
    _CSpLinksetMtp3T28_Type()
)
cSpLinksetMtp3T28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T28.setStatus("current")
_CSpLinksetMtp3T29_Type = Unsigned32
_CSpLinksetMtp3T29_Object = MibTableColumn
cSpLinksetMtp3T29 = _CSpLinksetMtp3T29_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 70),
    _CSpLinksetMtp3T29_Type()
)
cSpLinksetMtp3T29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T29.setStatus("current")
_CSpLinksetMtp3T30_Type = Unsigned32
_CSpLinksetMtp3T30_Object = MibTableColumn
cSpLinksetMtp3T30 = _CSpLinksetMtp3T30_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 71),
    _CSpLinksetMtp3T30_Type()
)
cSpLinksetMtp3T30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T30.setStatus("current")
_CSpLinksetMtp3T31_Type = Unsigned32
_CSpLinksetMtp3T31_Object = MibTableColumn
cSpLinksetMtp3T31 = _CSpLinksetMtp3T31_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 72),
    _CSpLinksetMtp3T31_Type()
)
cSpLinksetMtp3T31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T31.setStatus("current")
_CSpLinksetMtp3T32_Type = Unsigned32
_CSpLinksetMtp3T32_Object = MibTableColumn
cSpLinksetMtp3T32 = _CSpLinksetMtp3T32_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 73),
    _CSpLinksetMtp3T32_Type()
)
cSpLinksetMtp3T32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T32.setStatus("current")
_CSpLinksetMtp3T33_Type = Unsigned32
_CSpLinksetMtp3T33_Object = MibTableColumn
cSpLinksetMtp3T33 = _CSpLinksetMtp3T33_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 74),
    _CSpLinksetMtp3T33_Type()
)
cSpLinksetMtp3T33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T33.setStatus("current")
_CSpLinksetMtp3T34_Type = Unsigned32
_CSpLinksetMtp3T34_Object = MibTableColumn
cSpLinksetMtp3T34 = _CSpLinksetMtp3T34_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 2, 1, 1, 75),
    _CSpLinksetMtp3T34_Type()
)
cSpLinksetMtp3T34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinksetMtp3T34.setStatus("current")
_CSpLink_ObjectIdentity = ObjectIdentity
cSpLink = _CSpLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3)
)
_CSpLinkTable_Object = MibTable
cSpLinkTable = _CSpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cSpLinkTable.setStatus("current")
_CSpLinkTableEntry_Object = MibTableRow
cSpLinkTableEntry = _CSpLinkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1)
)
cSpLinkTableEntry.setIndexNames(
    (0, "CISCO-SP-MIB", "cSpLinksetName"),
    (0, "CISCO-SP-MIB", "cSpLinkSlc"),
)
if mibBuilder.loadTexts:
    cSpLinkTableEntry.setStatus("current")
_CSpLinkSlc_Type = CSpLinkSLC
_CSpLinkSlc_Object = MibTableColumn
cSpLinkSlc = _CSpLinkSlc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 1),
    _CSpLinkSlc_Type()
)
cSpLinkSlc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpLinkSlc.setStatus("current")
_CSpLinkState_Type = CSpOsiState
_CSpLinkState_Object = MibTableColumn
cSpLinkState = _CSpLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 2),
    _CSpLinkState_Type()
)
cSpLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkState.setStatus("current")
_CSpLinkType_Type = CSpLinkType
_CSpLinkType_Object = MibTableColumn
cSpLinkType = _CSpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 3),
    _CSpLinkType_Type()
)
cSpLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkType.setStatus("current")
_CSpLinkifIndex_Type = InterfaceIndexOrZero
_CSpLinkifIndex_Object = MibTableColumn
cSpLinkifIndex = _CSpLinkifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 4),
    _CSpLinkifIndex_Type()
)
cSpLinkifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkifIndex.setStatus("current")


class _CSpLinkSctpAssociation_Type(Integer32):
    """Custom type cSpLinkSctpAssociation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CSpLinkSctpAssociation_Type.__name__ = "Integer32"
_CSpLinkSctpAssociation_Object = MibTableColumn
cSpLinkSctpAssociation = _CSpLinkSctpAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 5),
    _CSpLinkSctpAssociation_Type()
)
cSpLinkSctpAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkSctpAssociation.setStatus("current")
_CSpLinkMtp3PacketsRcvd_Type = Counter32
_CSpLinkMtp3PacketsRcvd_Object = MibTableColumn
cSpLinkMtp3PacketsRcvd = _CSpLinkMtp3PacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 6),
    _CSpLinkMtp3PacketsRcvd_Type()
)
cSpLinkMtp3PacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3PacketsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp3PacketsRcvd.setUnits("packets")
_CSpLinkMtp3PacketsSent_Type = Counter32
_CSpLinkMtp3PacketsSent_Object = MibTableColumn
cSpLinkMtp3PacketsSent = _CSpLinkMtp3PacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 7),
    _CSpLinkMtp3PacketsSent_Type()
)
cSpLinkMtp3PacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3PacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp3PacketsSent.setUnits("packets")
_CSpLinkHCMtp3PacketsRcvd_Type = Counter64
_CSpLinkHCMtp3PacketsRcvd_Object = MibTableColumn
cSpLinkHCMtp3PacketsRcvd = _CSpLinkHCMtp3PacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 8),
    _CSpLinkHCMtp3PacketsRcvd_Type()
)
cSpLinkHCMtp3PacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkHCMtp3PacketsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkHCMtp3PacketsRcvd.setUnits("bytes")
_CSpLinkHCMtp3PacketsSent_Type = Counter64
_CSpLinkHCMtp3PacketsSent_Object = MibTableColumn
cSpLinkHCMtp3PacketsSent = _CSpLinkHCMtp3PacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 9),
    _CSpLinkHCMtp3PacketsSent_Type()
)
cSpLinkHCMtp3PacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkHCMtp3PacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkHCMtp3PacketsSent.setUnits("bytes")
_CSpLinkMtp3BytesRcvd_Type = Counter32
_CSpLinkMtp3BytesRcvd_Object = MibTableColumn
cSpLinkMtp3BytesRcvd = _CSpLinkMtp3BytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 10),
    _CSpLinkMtp3BytesRcvd_Type()
)
cSpLinkMtp3BytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3BytesRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp3BytesRcvd.setUnits("bytes")
_CSpLinkMtp3BytesSent_Type = Counter32
_CSpLinkMtp3BytesSent_Object = MibTableColumn
cSpLinkMtp3BytesSent = _CSpLinkMtp3BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 11),
    _CSpLinkMtp3BytesSent_Type()
)
cSpLinkMtp3BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3BytesSent.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp3BytesSent.setUnits("bytes")
_CSpLinkHCMtp3BytesRcvd_Type = Counter64
_CSpLinkHCMtp3BytesRcvd_Object = MibTableColumn
cSpLinkHCMtp3BytesRcvd = _CSpLinkHCMtp3BytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 12),
    _CSpLinkHCMtp3BytesRcvd_Type()
)
cSpLinkHCMtp3BytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkHCMtp3BytesRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkHCMtp3BytesRcvd.setUnits("bytes")
_CSpLinkHCMtp3BytesSent_Type = Counter64
_CSpLinkHCMtp3BytesSent_Object = MibTableColumn
cSpLinkHCMtp3BytesSent = _CSpLinkHCMtp3BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 13),
    _CSpLinkHCMtp3BytesSent_Type()
)
cSpLinkHCMtp3BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkHCMtp3BytesSent.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkHCMtp3BytesSent.setUnits("bytes")
_CSpLinkMtp2T01_Type = Unsigned32
_CSpLinkMtp2T01_Object = MibTableColumn
cSpLinkMtp2T01 = _CSpLinkMtp2T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 14),
    _CSpLinkMtp2T01_Type()
)
cSpLinkMtp2T01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp2T01.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp2T01.setUnits("100 milli-seconds")
_CSpLinkMtp2T02_Type = Unsigned32
_CSpLinkMtp2T02_Object = MibTableColumn
cSpLinkMtp2T02 = _CSpLinkMtp2T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 15),
    _CSpLinkMtp2T02_Type()
)
cSpLinkMtp2T02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp2T02.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp2T02.setUnits("100 milli-seconds")
_CSpLinkMtp2T03_Type = Unsigned32
_CSpLinkMtp2T03_Object = MibTableColumn
cSpLinkMtp2T03 = _CSpLinkMtp2T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 16),
    _CSpLinkMtp2T03_Type()
)
cSpLinkMtp2T03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp2T03.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp2T03.setUnits("100 milli-seconds")
_CSpLinkMtp2T4N_Type = Unsigned32
_CSpLinkMtp2T4N_Object = MibTableColumn
cSpLinkMtp2T4N = _CSpLinkMtp2T4N_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 17),
    _CSpLinkMtp2T4N_Type()
)
cSpLinkMtp2T4N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp2T4N.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp2T4N.setUnits("100 milli-seconds")
_CSpLinkMtp2T4E_Type = Unsigned32
_CSpLinkMtp2T4E_Object = MibTableColumn
cSpLinkMtp2T4E = _CSpLinkMtp2T4E_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 18),
    _CSpLinkMtp2T4E_Type()
)
cSpLinkMtp2T4E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp2T4E.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp2T4E.setUnits("100 milli-seconds")
_CSpLinkMtp2T05_Type = Unsigned32
_CSpLinkMtp2T05_Object = MibTableColumn
cSpLinkMtp2T05 = _CSpLinkMtp2T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 19),
    _CSpLinkMtp2T05_Type()
)
cSpLinkMtp2T05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp2T05.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp2T05.setUnits("milli-seconds")
_CSpLinkMtp2T06_Type = Unsigned32
_CSpLinkMtp2T06_Object = MibTableColumn
cSpLinkMtp2T06 = _CSpLinkMtp2T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 20),
    _CSpLinkMtp2T06_Type()
)
cSpLinkMtp2T06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp2T06.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp2T06.setUnits("100 milli-seconds.")
_CSpLinkMtp2T07_Type = Unsigned32
_CSpLinkMtp2T07_Object = MibTableColumn
cSpLinkMtp2T07 = _CSpLinkMtp2T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 21),
    _CSpLinkMtp2T07_Type()
)
cSpLinkMtp2T07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp2T07.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp2T07.setUnits("100 milli-seconds.")
_CSpLinkMtp2T08_Type = Unsigned32
_CSpLinkMtp2T08_Object = MibTableColumn
cSpLinkMtp2T08 = _CSpLinkMtp2T08_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 22),
    _CSpLinkMtp2T08_Type()
)
cSpLinkMtp2T08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp2T08.setStatus("current")
_CSpLinkMtp3T01_Type = Unsigned32
_CSpLinkMtp3T01_Object = MibTableColumn
cSpLinkMtp3T01 = _CSpLinkMtp3T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 23),
    _CSpLinkMtp3T01_Type()
)
cSpLinkMtp3T01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T01.setStatus("current")
_CSpLinkMtp3T02_Type = Unsigned32
_CSpLinkMtp3T02_Object = MibTableColumn
cSpLinkMtp3T02 = _CSpLinkMtp3T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 24),
    _CSpLinkMtp3T02_Type()
)
cSpLinkMtp3T02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T02.setStatus("current")
_CSpLinkMtp3T03_Type = Unsigned32
_CSpLinkMtp3T03_Object = MibTableColumn
cSpLinkMtp3T03 = _CSpLinkMtp3T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 25),
    _CSpLinkMtp3T03_Type()
)
cSpLinkMtp3T03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T03.setStatus("current")
_CSpLinkMtp3T04_Type = Unsigned32
_CSpLinkMtp3T04_Object = MibTableColumn
cSpLinkMtp3T04 = _CSpLinkMtp3T04_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 26),
    _CSpLinkMtp3T04_Type()
)
cSpLinkMtp3T04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T04.setStatus("current")
_CSpLinkMtp3T05_Type = Unsigned32
_CSpLinkMtp3T05_Object = MibTableColumn
cSpLinkMtp3T05 = _CSpLinkMtp3T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 27),
    _CSpLinkMtp3T05_Type()
)
cSpLinkMtp3T05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T05.setStatus("current")
_CSpLinkMtp3T06_Type = Unsigned32
_CSpLinkMtp3T06_Object = MibTableColumn
cSpLinkMtp3T06 = _CSpLinkMtp3T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 28),
    _CSpLinkMtp3T06_Type()
)
cSpLinkMtp3T06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T06.setStatus("current")
_CSpLinkMtp3T07_Type = Unsigned32
_CSpLinkMtp3T07_Object = MibTableColumn
cSpLinkMtp3T07 = _CSpLinkMtp3T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 29),
    _CSpLinkMtp3T07_Type()
)
cSpLinkMtp3T07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T07.setStatus("current")
_CSpLinkMtp3T08_Type = Unsigned32
_CSpLinkMtp3T08_Object = MibTableColumn
cSpLinkMtp3T08 = _CSpLinkMtp3T08_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 30),
    _CSpLinkMtp3T08_Type()
)
cSpLinkMtp3T08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T08.setStatus("current")
_CSpLinkMtp3T10_Type = Unsigned32
_CSpLinkMtp3T10_Object = MibTableColumn
cSpLinkMtp3T10 = _CSpLinkMtp3T10_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 31),
    _CSpLinkMtp3T10_Type()
)
cSpLinkMtp3T10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T10.setStatus("current")
_CSpLinkMtp3T11_Type = Unsigned32
_CSpLinkMtp3T11_Object = MibTableColumn
cSpLinkMtp3T11 = _CSpLinkMtp3T11_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 32),
    _CSpLinkMtp3T11_Type()
)
cSpLinkMtp3T11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T11.setStatus("current")
_CSpLinkMtp3T12_Type = Unsigned32
_CSpLinkMtp3T12_Object = MibTableColumn
cSpLinkMtp3T12 = _CSpLinkMtp3T12_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 33),
    _CSpLinkMtp3T12_Type()
)
cSpLinkMtp3T12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T12.setStatus("current")
_CSpLinkMtp3T13_Type = Unsigned32
_CSpLinkMtp3T13_Object = MibTableColumn
cSpLinkMtp3T13 = _CSpLinkMtp3T13_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 34),
    _CSpLinkMtp3T13_Type()
)
cSpLinkMtp3T13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T13.setStatus("current")
_CSpLinkMtp3T14_Type = Unsigned32
_CSpLinkMtp3T14_Object = MibTableColumn
cSpLinkMtp3T14 = _CSpLinkMtp3T14_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 35),
    _CSpLinkMtp3T14_Type()
)
cSpLinkMtp3T14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T14.setStatus("current")
_CSpLinkMtp3T15_Type = Unsigned32
_CSpLinkMtp3T15_Object = MibTableColumn
cSpLinkMtp3T15 = _CSpLinkMtp3T15_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 36),
    _CSpLinkMtp3T15_Type()
)
cSpLinkMtp3T15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T15.setStatus("current")
_CSpLinkMtp3T16_Type = Unsigned32
_CSpLinkMtp3T16_Object = MibTableColumn
cSpLinkMtp3T16 = _CSpLinkMtp3T16_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 37),
    _CSpLinkMtp3T16_Type()
)
cSpLinkMtp3T16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T16.setStatus("current")
_CSpLinkMtp3T17_Type = Unsigned32
_CSpLinkMtp3T17_Object = MibTableColumn
cSpLinkMtp3T17 = _CSpLinkMtp3T17_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 38),
    _CSpLinkMtp3T17_Type()
)
cSpLinkMtp3T17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T17.setStatus("current")
_CSpLinkMtp3T18_Type = Unsigned32
_CSpLinkMtp3T18_Object = MibTableColumn
cSpLinkMtp3T18 = _CSpLinkMtp3T18_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 39),
    _CSpLinkMtp3T18_Type()
)
cSpLinkMtp3T18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T18.setStatus("current")
_CSpLinkMtp3T19_Type = Unsigned32
_CSpLinkMtp3T19_Object = MibTableColumn
cSpLinkMtp3T19 = _CSpLinkMtp3T19_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 40),
    _CSpLinkMtp3T19_Type()
)
cSpLinkMtp3T19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T19.setStatus("current")
_CSpLinkMtp3T20_Type = Unsigned32
_CSpLinkMtp3T20_Object = MibTableColumn
cSpLinkMtp3T20 = _CSpLinkMtp3T20_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 41),
    _CSpLinkMtp3T20_Type()
)
cSpLinkMtp3T20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T20.setStatus("current")
_CSpLinkMtp3T21_Type = Unsigned32
_CSpLinkMtp3T21_Object = MibTableColumn
cSpLinkMtp3T21 = _CSpLinkMtp3T21_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 42),
    _CSpLinkMtp3T21_Type()
)
cSpLinkMtp3T21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T21.setStatus("current")
_CSpLinkMtp3T22_Type = Unsigned32
_CSpLinkMtp3T22_Object = MibTableColumn
cSpLinkMtp3T22 = _CSpLinkMtp3T22_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 43),
    _CSpLinkMtp3T22_Type()
)
cSpLinkMtp3T22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T22.setStatus("current")
_CSpLinkMtp3T23_Type = Unsigned32
_CSpLinkMtp3T23_Object = MibTableColumn
cSpLinkMtp3T23 = _CSpLinkMtp3T23_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 44),
    _CSpLinkMtp3T23_Type()
)
cSpLinkMtp3T23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T23.setStatus("current")
_CSpLinkMtp3T24_Type = Unsigned32
_CSpLinkMtp3T24_Object = MibTableColumn
cSpLinkMtp3T24 = _CSpLinkMtp3T24_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 45),
    _CSpLinkMtp3T24_Type()
)
cSpLinkMtp3T24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T24.setStatus("current")
_CSpLinkMtp3T25_Type = Unsigned32
_CSpLinkMtp3T25_Object = MibTableColumn
cSpLinkMtp3T25 = _CSpLinkMtp3T25_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 46),
    _CSpLinkMtp3T25_Type()
)
cSpLinkMtp3T25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T25.setStatus("current")
_CSpLinkMtp3T26_Type = Unsigned32
_CSpLinkMtp3T26_Object = MibTableColumn
cSpLinkMtp3T26 = _CSpLinkMtp3T26_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 47),
    _CSpLinkMtp3T26_Type()
)
cSpLinkMtp3T26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T26.setStatus("current")
_CSpLinkMtp3T27_Type = Unsigned32
_CSpLinkMtp3T27_Object = MibTableColumn
cSpLinkMtp3T27 = _CSpLinkMtp3T27_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 48),
    _CSpLinkMtp3T27_Type()
)
cSpLinkMtp3T27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T27.setStatus("current")
_CSpLinkMtp3T28_Type = Unsigned32
_CSpLinkMtp3T28_Object = MibTableColumn
cSpLinkMtp3T28 = _CSpLinkMtp3T28_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 49),
    _CSpLinkMtp3T28_Type()
)
cSpLinkMtp3T28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T28.setStatus("current")
_CSpLinkMtp3T29_Type = Unsigned32
_CSpLinkMtp3T29_Object = MibTableColumn
cSpLinkMtp3T29 = _CSpLinkMtp3T29_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 50),
    _CSpLinkMtp3T29_Type()
)
cSpLinkMtp3T29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T29.setStatus("current")
_CSpLinkMtp3T30_Type = Unsigned32
_CSpLinkMtp3T30_Object = MibTableColumn
cSpLinkMtp3T30 = _CSpLinkMtp3T30_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 51),
    _CSpLinkMtp3T30_Type()
)
cSpLinkMtp3T30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T30.setStatus("current")
_CSpLinkMtp3T31_Type = Unsigned32
_CSpLinkMtp3T31_Object = MibTableColumn
cSpLinkMtp3T31 = _CSpLinkMtp3T31_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 52),
    _CSpLinkMtp3T31_Type()
)
cSpLinkMtp3T31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T31.setStatus("current")
_CSpLinkMtp3T32_Type = Unsigned32
_CSpLinkMtp3T32_Object = MibTableColumn
cSpLinkMtp3T32 = _CSpLinkMtp3T32_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 53),
    _CSpLinkMtp3T32_Type()
)
cSpLinkMtp3T32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T32.setStatus("current")
_CSpLinkMtp3T33_Type = Unsigned32
_CSpLinkMtp3T33_Object = MibTableColumn
cSpLinkMtp3T33 = _CSpLinkMtp3T33_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 54),
    _CSpLinkMtp3T33_Type()
)
cSpLinkMtp3T33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T33.setStatus("current")
_CSpLinkMtp3T34_Type = Unsigned32
_CSpLinkMtp3T34_Object = MibTableColumn
cSpLinkMtp3T34 = _CSpLinkMtp3T34_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 55),
    _CSpLinkMtp3T34_Type()
)
cSpLinkMtp3T34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3T34.setStatus("current")
_CSpLinkXmitQueueDepth_Type = Gauge32
_CSpLinkXmitQueueDepth_Object = MibTableColumn
cSpLinkXmitQueueDepth = _CSpLinkXmitQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 56),
    _CSpLinkXmitQueueDepth_Type()
)
cSpLinkXmitQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkXmitQueueDepth.setStatus("current")
_CSpLinkXmitQueueDepthHigh_Type = Unsigned32
_CSpLinkXmitQueueDepthHigh_Object = MibTableColumn
cSpLinkXmitQueueDepthHigh = _CSpLinkXmitQueueDepthHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 57),
    _CSpLinkXmitQueueDepthHigh_Type()
)
cSpLinkXmitQueueDepthHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSpLinkXmitQueueDepthHigh.setStatus("current")
_CSpLinkXmitQueueDepthHighReset_Type = TimeStamp
_CSpLinkXmitQueueDepthHighReset_Object = MibTableColumn
cSpLinkXmitQueueDepthHighReset = _CSpLinkXmitQueueDepthHighReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 58),
    _CSpLinkXmitQueueDepthHighReset_Type()
)
cSpLinkXmitQueueDepthHighReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkXmitQueueDepthHighReset.setStatus("current")


class _CSpLinkCongestionState_Type(Unsigned32):
    """Custom type cSpLinkCongestionState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CSpLinkCongestionState_Type.__name__ = "Unsigned32"
_CSpLinkCongestionState_Object = MibTableColumn
cSpLinkCongestionState = _CSpLinkCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 59),
    _CSpLinkCongestionState_Type()
)
cSpLinkCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkCongestionState.setStatus("current")
_CSpLinkCongestionAbate1_Type = Unsigned32
_CSpLinkCongestionAbate1_Object = MibTableColumn
cSpLinkCongestionAbate1 = _CSpLinkCongestionAbate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 60),
    _CSpLinkCongestionAbate1_Type()
)
cSpLinkCongestionAbate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkCongestionAbate1.setStatus("current")
_CSpLinkCongestionAbate2_Type = Unsigned32
_CSpLinkCongestionAbate2_Object = MibTableColumn
cSpLinkCongestionAbate2 = _CSpLinkCongestionAbate2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 61),
    _CSpLinkCongestionAbate2_Type()
)
cSpLinkCongestionAbate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkCongestionAbate2.setStatus("current")
_CSpLinkCongestionAbate3_Type = Unsigned32
_CSpLinkCongestionAbate3_Object = MibTableColumn
cSpLinkCongestionAbate3 = _CSpLinkCongestionAbate3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 62),
    _CSpLinkCongestionAbate3_Type()
)
cSpLinkCongestionAbate3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkCongestionAbate3.setStatus("current")
_CSpLinkCongestionOnset1_Type = Unsigned32
_CSpLinkCongestionOnset1_Object = MibTableColumn
cSpLinkCongestionOnset1 = _CSpLinkCongestionOnset1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 63),
    _CSpLinkCongestionOnset1_Type()
)
cSpLinkCongestionOnset1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkCongestionOnset1.setStatus("current")
_CSpLinkCongestionOnset2_Type = Unsigned32
_CSpLinkCongestionOnset2_Object = MibTableColumn
cSpLinkCongestionOnset2 = _CSpLinkCongestionOnset2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 64),
    _CSpLinkCongestionOnset2_Type()
)
cSpLinkCongestionOnset2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkCongestionOnset2.setStatus("current")
_CSpLinkCongestionOnset3_Type = Unsigned32
_CSpLinkCongestionOnset3_Object = MibTableColumn
cSpLinkCongestionOnset3 = _CSpLinkCongestionOnset3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 65),
    _CSpLinkCongestionOnset3_Type()
)
cSpLinkCongestionOnset3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkCongestionOnset3.setStatus("current")


class _CSpLinkSigLinkTest_Type(TruthValue):
    """Custom type cSpLinkSigLinkTest based on TruthValue"""


_CSpLinkSigLinkTest_Object = MibTableColumn
cSpLinkSigLinkTest = _CSpLinkSigLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 66),
    _CSpLinkSigLinkTest_Type()
)
cSpLinkSigLinkTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkSigLinkTest.setStatus("current")
_CSpLinkQ752T1E1_Type = TimeTicks
_CSpLinkQ752T1E1_Object = MibTableColumn
cSpLinkQ752T1E1 = _CSpLinkQ752T1E1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 67),
    _CSpLinkQ752T1E1_Type()
)
cSpLinkQ752T1E1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E1.setStatus("current")
_CSpLinkQ752T1E2_Type = Counter32
_CSpLinkQ752T1E2_Object = MibTableColumn
cSpLinkQ752T1E2 = _CSpLinkQ752T1E2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 68),
    _CSpLinkQ752T1E2_Type()
)
cSpLinkQ752T1E2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E2.setStatus("current")
_CSpLinkQ752T1E3_Type = Counter32
_CSpLinkQ752T1E3_Object = MibTableColumn
cSpLinkQ752T1E3 = _CSpLinkQ752T1E3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 69),
    _CSpLinkQ752T1E3_Type()
)
cSpLinkQ752T1E3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E3.setStatus("current")
_CSpLinkQ752T1E4_Type = Counter32
_CSpLinkQ752T1E4_Object = MibTableColumn
cSpLinkQ752T1E4 = _CSpLinkQ752T1E4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 70),
    _CSpLinkQ752T1E4_Type()
)
cSpLinkQ752T1E4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E4.setStatus("current")
_CSpLinkQ752T1E5_Type = Counter32
_CSpLinkQ752T1E5_Object = MibTableColumn
cSpLinkQ752T1E5 = _CSpLinkQ752T1E5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 71),
    _CSpLinkQ752T1E5_Type()
)
cSpLinkQ752T1E5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E5.setStatus("current")
_CSpLinkQ752T1E6_Type = Counter32
_CSpLinkQ752T1E6_Object = MibTableColumn
cSpLinkQ752T1E6 = _CSpLinkQ752T1E6_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 72),
    _CSpLinkQ752T1E6_Type()
)
cSpLinkQ752T1E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E6.setStatus("current")
_CSpLinkQ752T1E7_Type = Counter32
_CSpLinkQ752T1E7_Object = MibTableColumn
cSpLinkQ752T1E7 = _CSpLinkQ752T1E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 73),
    _CSpLinkQ752T1E7_Type()
)
cSpLinkQ752T1E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E7.setStatus("current")
_CSpLinkQ752T1E8_Type = Counter32
_CSpLinkQ752T1E8_Object = MibTableColumn
cSpLinkQ752T1E8 = _CSpLinkQ752T1E8_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 74),
    _CSpLinkQ752T1E8_Type()
)
cSpLinkQ752T1E8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E8.setStatus("current")
_CSpLinkQ752T1E9_Type = Counter32
_CSpLinkQ752T1E9_Object = MibTableColumn
cSpLinkQ752T1E9 = _CSpLinkQ752T1E9_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 75),
    _CSpLinkQ752T1E9_Type()
)
cSpLinkQ752T1E9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E9.setStatus("current")
_CSpLinkQ752T1E10_Type = Counter32
_CSpLinkQ752T1E10_Object = MibTableColumn
cSpLinkQ752T1E10 = _CSpLinkQ752T1E10_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 76),
    _CSpLinkQ752T1E10_Type()
)
cSpLinkQ752T1E10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E10.setStatus("current")
_CSpLinkQ752T1E11_Type = Counter32
_CSpLinkQ752T1E11_Object = MibTableColumn
cSpLinkQ752T1E11 = _CSpLinkQ752T1E11_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 77),
    _CSpLinkQ752T1E11_Type()
)
cSpLinkQ752T1E11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T1E11.setStatus("current")
_CSpLinkQ752T2E1_Type = TimeTicks
_CSpLinkQ752T2E1_Object = MibTableColumn
cSpLinkQ752T2E1 = _CSpLinkQ752T2E1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 78),
    _CSpLinkQ752T2E1_Type()
)
cSpLinkQ752T2E1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T2E1.setStatus("current")
_CSpLinkQ752T2E5_Type = TimeTicks
_CSpLinkQ752T2E5_Object = MibTableColumn
cSpLinkQ752T2E5 = _CSpLinkQ752T2E5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 79),
    _CSpLinkQ752T2E5_Type()
)
cSpLinkQ752T2E5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T2E5.setStatus("current")
_CSpLinkQ752T2E6_Type = TimeTicks
_CSpLinkQ752T2E6_Object = MibTableColumn
cSpLinkQ752T2E6 = _CSpLinkQ752T2E6_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 80),
    _CSpLinkQ752T2E6_Type()
)
cSpLinkQ752T2E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T2E6.setStatus("current")
_CSpLinkQ752T2E7_Type = TimeTicks
_CSpLinkQ752T2E7_Object = MibTableColumn
cSpLinkQ752T2E7 = _CSpLinkQ752T2E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 81),
    _CSpLinkQ752T2E7_Type()
)
cSpLinkQ752T2E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T2E7.setStatus("current")
_CSpLinkQ752T2E9_Type = TimeTicks
_CSpLinkQ752T2E9_Object = MibTableColumn
cSpLinkQ752T2E9 = _CSpLinkQ752T2E9_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 82),
    _CSpLinkQ752T2E9_Type()
)
cSpLinkQ752T2E9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T2E9.setStatus("current")
_CSpLinkQ752T2E10_Type = Counter32
_CSpLinkQ752T2E10_Object = MibTableColumn
cSpLinkQ752T2E10 = _CSpLinkQ752T2E10_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 83),
    _CSpLinkQ752T2E10_Type()
)
cSpLinkQ752T2E10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T2E10.setStatus("current")
_CSpLinkQ752T2E15_Type = TimeTicks
_CSpLinkQ752T2E15_Object = MibTableColumn
cSpLinkQ752T2E15 = _CSpLinkQ752T2E15_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 84),
    _CSpLinkQ752T2E15_Type()
)
cSpLinkQ752T2E15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T2E15.setStatus("current")
_CSpLinkQ752T2E16_Type = Counter32
_CSpLinkQ752T2E16_Object = MibTableColumn
cSpLinkQ752T2E16 = _CSpLinkQ752T2E16_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 85),
    _CSpLinkQ752T2E16_Type()
)
cSpLinkQ752T2E16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T2E16.setStatus("current")
_CSpLinkQ752T2E18_Type = Counter32
_CSpLinkQ752T2E18_Object = MibTableColumn
cSpLinkQ752T2E18 = _CSpLinkQ752T2E18_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 86),
    _CSpLinkQ752T2E18_Type()
)
cSpLinkQ752T2E18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T2E18.setStatus("current")
_CSpLinkMtp3PacketsRetrans_Type = Counter32
_CSpLinkMtp3PacketsRetrans_Object = MibTableColumn
cSpLinkMtp3PacketsRetrans = _CSpLinkMtp3PacketsRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 87),
    _CSpLinkMtp3PacketsRetrans_Type()
)
cSpLinkMtp3PacketsRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3PacketsRetrans.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp3PacketsRetrans.setUnits("packets")
_CSpLinkMtp3BytesRetrans_Type = Counter32
_CSpLinkMtp3BytesRetrans_Object = MibTableColumn
cSpLinkMtp3BytesRetrans = _CSpLinkMtp3BytesRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 88),
    _CSpLinkMtp3BytesRetrans_Type()
)
cSpLinkMtp3BytesRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkMtp3BytesRetrans.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkMtp3BytesRetrans.setUnits("bytes")
_CSpLinkQ752T3E6_Type = Counter32
_CSpLinkQ752T3E6_Object = MibTableColumn
cSpLinkQ752T3E6 = _CSpLinkQ752T3E6_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 89),
    _CSpLinkQ752T3E6_Type()
)
cSpLinkQ752T3E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E6.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E6.setUnits("events")
_CSpLinkQ752T3E7_Type = TimeTicks
_CSpLinkQ752T3E7_Object = MibTableColumn
cSpLinkQ752T3E7 = _CSpLinkQ752T3E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 90),
    _CSpLinkQ752T3E7_Type()
)
cSpLinkQ752T3E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E7.setStatus("current")
_CSpLinkQ752T3E10L1_Type = Counter32
_CSpLinkQ752T3E10L1_Object = MibTableColumn
cSpLinkQ752T3E10L1 = _CSpLinkQ752T3E10L1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 91),
    _CSpLinkQ752T3E10L1_Type()
)
cSpLinkQ752T3E10L1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E10L1.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E10L1.setUnits("Packets")
_CSpLinkQ752T3E10L2_Type = Counter32
_CSpLinkQ752T3E10L2_Object = MibTableColumn
cSpLinkQ752T3E10L2 = _CSpLinkQ752T3E10L2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 92),
    _CSpLinkQ752T3E10L2_Type()
)
cSpLinkQ752T3E10L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E10L2.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E10L2.setUnits("Packets")
_CSpLinkQ752T3E10L3_Type = Counter32
_CSpLinkQ752T3E10L3_Object = MibTableColumn
cSpLinkQ752T3E10L3 = _CSpLinkQ752T3E10L3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 93),
    _CSpLinkQ752T3E10L3_Type()
)
cSpLinkQ752T3E10L3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E10L3.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E10L3.setUnits("Packets")
_CSpLinkQ752T3E11L1_Type = Counter32
_CSpLinkQ752T3E11L1_Object = MibTableColumn
cSpLinkQ752T3E11L1 = _CSpLinkQ752T3E11L1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 94),
    _CSpLinkQ752T3E11L1_Type()
)
cSpLinkQ752T3E11L1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E11L1.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E11L1.setUnits("bytes")
_CSpLinkQ752T3E11L2_Type = Counter32
_CSpLinkQ752T3E11L2_Object = MibTableColumn
cSpLinkQ752T3E11L2 = _CSpLinkQ752T3E11L2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 95),
    _CSpLinkQ752T3E11L2_Type()
)
cSpLinkQ752T3E11L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E11L2.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E11L2.setUnits("bytes")
_CSpLinkQ752T3E11L3_Type = Counter32
_CSpLinkQ752T3E11L3_Object = MibTableColumn
cSpLinkQ752T3E11L3 = _CSpLinkQ752T3E11L3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 3, 1, 1, 96),
    _CSpLinkQ752T3E11L3_Type()
)
cSpLinkQ752T3E11L3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E11L3.setStatus("current")
if mibBuilder.loadTexts:
    cSpLinkQ752T3E11L3.setUnits("bytes")
_CSpRoute_ObjectIdentity = ObjectIdentity
cSpRoute = _CSpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 4)
)
_CSpRouteTable_Object = MibTable
cSpRouteTable = _CSpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cSpRouteTable.setStatus("current")
_CSpRouteTableEntry_Object = MibTableRow
cSpRouteTableEntry = _CSpRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 4, 1, 1)
)
cSpRouteTableEntry.setIndexNames(
    (0, "CISCO-SP-MIB", "cSpRouteTableName"),
    (0, "CISCO-SP-MIB", "cSpRouteDpc"),
    (0, "CISCO-SP-MIB", "cSpRouteDestLsCost"),
    (0, "CISCO-SP-MIB", "cSpRouteDestLinkset"),
    (0, "CISCO-SP-MIB", "cSpRouteMask"),
)
if mibBuilder.loadTexts:
    cSpRouteTableEntry.setStatus("current")
_CSpRouteTableName_Type = CSpRouteTableName
_CSpRouteTableName_Object = MibTableColumn
cSpRouteTableName = _CSpRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 4, 1, 1, 1),
    _CSpRouteTableName_Type()
)
cSpRouteTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpRouteTableName.setStatus("current")
_CSpRouteDpc_Type = CSpPointCode
_CSpRouteDpc_Object = MibTableColumn
cSpRouteDpc = _CSpRouteDpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 4, 1, 1, 2),
    _CSpRouteDpc_Type()
)
cSpRouteDpc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpRouteDpc.setStatus("current")


class _CSpRouteDestLsCost_Type(Unsigned32):
    """Custom type cSpRouteDestLsCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_CSpRouteDestLsCost_Type.__name__ = "Unsigned32"
_CSpRouteDestLsCost_Object = MibTableColumn
cSpRouteDestLsCost = _CSpRouteDestLsCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 4, 1, 1, 3),
    _CSpRouteDestLsCost_Type()
)
cSpRouteDestLsCost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpRouteDestLsCost.setStatus("current")
_CSpRouteDestLinkset_Type = CSpLinksetId
_CSpRouteDestLinkset_Object = MibTableColumn
cSpRouteDestLinkset = _CSpRouteDestLinkset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 4, 1, 1, 4),
    _CSpRouteDestLinkset_Type()
)
cSpRouteDestLinkset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpRouteDestLinkset.setStatus("current")
_CSpRouteMask_Type = Unsigned32
_CSpRouteMask_Object = MibTableColumn
cSpRouteMask = _CSpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 4, 1, 1, 5),
    _CSpRouteMask_Type()
)
cSpRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpRouteMask.setStatus("current")
_CSpRouteStatus_Type = CSpRouteStatus
_CSpRouteStatus_Object = MibTableColumn
cSpRouteStatus = _CSpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 4, 1, 1, 6),
    _CSpRouteStatus_Type()
)
cSpRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpRouteStatus.setStatus("current")
_CSpAccessControlList_ObjectIdentity = ObjectIdentity
cSpAccessControlList = _CSpAccessControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5)
)
_CSpAclTable_Object = MibTable
cSpAclTable = _CSpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cSpAclTable.setStatus("current")
_CSpAclTableEntry_Object = MibTableRow
cSpAclTableEntry = _CSpAclTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1)
)
cSpAclTableEntry.setIndexNames(
    (0, "CISCO-SP-MIB", "cSpAclId"),
    (0, "CISCO-SP-MIB", "cSpAclEntryNumber"),
)
if mibBuilder.loadTexts:
    cSpAclTableEntry.setStatus("current")
_CSpAclId_Type = CSpAclId
_CSpAclId_Object = MibTableColumn
cSpAclId = _CSpAclId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 1),
    _CSpAclId_Type()
)
cSpAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpAclId.setStatus("current")
_CSpAclEntryNumber_Type = Unsigned32
_CSpAclEntryNumber_Object = MibTableColumn
cSpAclEntryNumber = _CSpAclEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 2),
    _CSpAclEntryNumber_Type()
)
cSpAclEntryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpAclEntryNumber.setStatus("current")


class _CSpAclType_Type(Integer32):
    """Custom type cSpAclType based on Integer32"""
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
        *(("dpc", 1),
          ("opc", 2),
          ("pattern", 3),
          ("sio", 4))
    )


_CSpAclType_Type.__name__ = "Integer32"
_CSpAclType_Object = MibTableColumn
cSpAclType = _CSpAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 3),
    _CSpAclType_Type()
)
cSpAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAclType.setStatus("current")
_CSpAclDpc_Type = CSpPointCode
_CSpAclDpc_Object = MibTableColumn
cSpAclDpc = _CSpAclDpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 4),
    _CSpAclDpc_Type()
)
cSpAclDpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAclDpc.setStatus("current")
_CSpAclDpcMask_Type = Unsigned32
_CSpAclDpcMask_Object = MibTableColumn
cSpAclDpcMask = _CSpAclDpcMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 5),
    _CSpAclDpcMask_Type()
)
cSpAclDpcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAclDpcMask.setStatus("current")
_CSpAclOpc_Type = CSpPointCode
_CSpAclOpc_Object = MibTableColumn
cSpAclOpc = _CSpAclOpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 6),
    _CSpAclOpc_Type()
)
cSpAclOpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAclOpc.setStatus("current")
_CSpAclOpcMask_Type = Unsigned32
_CSpAclOpcMask_Object = MibTableColumn
cSpAclOpcMask = _CSpAclOpcMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 7),
    _CSpAclOpcMask_Type()
)
cSpAclOpcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAclOpcMask.setStatus("current")
_CSpAclSi_Type = CSpAclSi
_CSpAclSi_Object = MibTableColumn
cSpAclSi = _CSpAclSi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 8),
    _CSpAclSi_Type()
)
cSpAclSi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAclSi.setStatus("current")


class _CSpAclPattern_Type(DisplayString):
    """Custom type cSpAclPattern based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CSpAclPattern_Type.__name__ = "DisplayString"
_CSpAclPattern_Object = MibTableColumn
cSpAclPattern = _CSpAclPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 9),
    _CSpAclPattern_Type()
)
cSpAclPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAclPattern.setStatus("current")
_CSpAclOffset_Type = Unsigned32
_CSpAclOffset_Object = MibTableColumn
cSpAclOffset = _CSpAclOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 10),
    _CSpAclOffset_Type()
)
cSpAclOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAclOffset.setStatus("current")
_CSpAclAction_Type = CSpAclAction
_CSpAclAction_Object = MibTableColumn
cSpAclAction = _CSpAclAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 5, 1, 1, 11),
    _CSpAclAction_Type()
)
cSpAclAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAclAction.setStatus("current")
_CSpAccounting_ObjectIdentity = ObjectIdentity
cSpAccounting = _CSpAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6)
)
_CSpAccountingTable_Object = MibTable
cSpAccountingTable = _CSpAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cSpAccountingTable.setStatus("current")
_CSpAccountingTableEntry_Object = MibTableRow
cSpAccountingTableEntry = _CSpAccountingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1)
)
cSpAccountingTableEntry.setIndexNames(
    (0, "CISCO-SP-MIB", "cSpAccTableId"),
    (0, "CISCO-SP-MIB", "cSpLinksetName"),
    (0, "CISCO-SP-MIB", "cSpAccDpc"),
    (0, "CISCO-SP-MIB", "cSpAccOpc"),
)
if mibBuilder.loadTexts:
    cSpAccountingTableEntry.setStatus("current")


class _CSpAccTableId_Type(Integer32):
    """Custom type cSpAccTableId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passed", 1),
          ("violation", 2))
    )


_CSpAccTableId_Type.__name__ = "Integer32"
_CSpAccTableId_Object = MibTableColumn
cSpAccTableId = _CSpAccTableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 1),
    _CSpAccTableId_Type()
)
cSpAccTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpAccTableId.setStatus("current")
_CSpAccDpc_Type = CSpPointCode
_CSpAccDpc_Object = MibTableColumn
cSpAccDpc = _CSpAccDpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 2),
    _CSpAccDpc_Type()
)
cSpAccDpc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpAccDpc.setStatus("current")
_CSpAccOpc_Type = CSpPointCode
_CSpAccOpc_Object = MibTableColumn
cSpAccOpc = _CSpAccOpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 3),
    _CSpAccOpc_Type()
)
cSpAccOpc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSpAccOpc.setStatus("current")
_CSpAccRcvdPackets_Type = Counter32
_CSpAccRcvdPackets_Object = MibTableColumn
cSpAccRcvdPackets = _CSpAccRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 4),
    _CSpAccRcvdPackets_Type()
)
cSpAccRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccRcvdPackets.setUnits("packets")
_CSpAccHCRcvdPackets_Type = Counter64
_CSpAccHCRcvdPackets_Object = MibTableColumn
cSpAccHCRcvdPackets = _CSpAccHCRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 5),
    _CSpAccHCRcvdPackets_Type()
)
cSpAccHCRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCRcvdPackets.setUnits("packets")
_CSpAccSentPackets_Type = Counter32
_CSpAccSentPackets_Object = MibTableColumn
cSpAccSentPackets = _CSpAccSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 6),
    _CSpAccSentPackets_Type()
)
cSpAccSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSentPackets.setUnits("packets")
_CSpAccHCSentPackets_Type = Counter64
_CSpAccHCSentPackets_Object = MibTableColumn
cSpAccHCSentPackets = _CSpAccHCSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 7),
    _CSpAccHCSentPackets_Type()
)
cSpAccHCSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSentPackets.setUnits("packets")
_CSpAccRcvdBytes_Type = Counter32
_CSpAccRcvdBytes_Object = MibTableColumn
cSpAccRcvdBytes = _CSpAccRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 8),
    _CSpAccRcvdBytes_Type()
)
cSpAccRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccRcvdBytes.setUnits("bytes")
_CSpAccHCRcvdBytes_Type = Counter64
_CSpAccHCRcvdBytes_Object = MibTableColumn
cSpAccHCRcvdBytes = _CSpAccHCRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 9),
    _CSpAccHCRcvdBytes_Type()
)
cSpAccHCRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCRcvdBytes.setUnits("bytes")
_CSpAccSentBytes_Type = Counter32
_CSpAccSentBytes_Object = MibTableColumn
cSpAccSentBytes = _CSpAccSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 10),
    _CSpAccSentBytes_Type()
)
cSpAccSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSentBytes.setUnits("bytes")
_CSpAccHCSentBytes_Type = Counter64
_CSpAccHCSentBytes_Object = MibTableColumn
cSpAccHCSentBytes = _CSpAccHCSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 11),
    _CSpAccHCSentBytes_Type()
)
cSpAccHCSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSentBytes.setUnits("bytes")
_CSpAccSnmmRcvdPackets_Type = Counter32
_CSpAccSnmmRcvdPackets_Object = MibTableColumn
cSpAccSnmmRcvdPackets = _CSpAccSnmmRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 12),
    _CSpAccSnmmRcvdPackets_Type()
)
cSpAccSnmmRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSnmmRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSnmmRcvdPackets.setUnits("packets")
_CSpAccHCSnmmRcvdPackets_Type = Counter64
_CSpAccHCSnmmRcvdPackets_Object = MibTableColumn
cSpAccHCSnmmRcvdPackets = _CSpAccHCSnmmRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 13),
    _CSpAccHCSnmmRcvdPackets_Type()
)
cSpAccHCSnmmRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSnmmRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSnmmRcvdPackets.setUnits("packets")
_CSpAccSnmmRcvdBytes_Type = Counter32
_CSpAccSnmmRcvdBytes_Object = MibTableColumn
cSpAccSnmmRcvdBytes = _CSpAccSnmmRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 14),
    _CSpAccSnmmRcvdBytes_Type()
)
cSpAccSnmmRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSnmmRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSnmmRcvdBytes.setUnits("bytes")
_CSpAccHCSnmmRcvdBytes_Type = Counter64
_CSpAccHCSnmmRcvdBytes_Object = MibTableColumn
cSpAccHCSnmmRcvdBytes = _CSpAccHCSnmmRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 15),
    _CSpAccHCSnmmRcvdBytes_Type()
)
cSpAccHCSnmmRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSnmmRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSnmmRcvdBytes.setUnits("bytes")
_CSpAccSnmmSentPackets_Type = Counter32
_CSpAccSnmmSentPackets_Object = MibTableColumn
cSpAccSnmmSentPackets = _CSpAccSnmmSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 16),
    _CSpAccSnmmSentPackets_Type()
)
cSpAccSnmmSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSnmmSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSnmmSentPackets.setUnits("packets")
_CSpAccHCSnmmSentPackets_Type = Counter64
_CSpAccHCSnmmSentPackets_Object = MibTableColumn
cSpAccHCSnmmSentPackets = _CSpAccHCSnmmSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 17),
    _CSpAccHCSnmmSentPackets_Type()
)
cSpAccHCSnmmSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSnmmSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSnmmSentPackets.setUnits("packets")
_CSpAccSnmmSentBytes_Type = Counter32
_CSpAccSnmmSentBytes_Object = MibTableColumn
cSpAccSnmmSentBytes = _CSpAccSnmmSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 18),
    _CSpAccSnmmSentBytes_Type()
)
cSpAccSnmmSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSnmmSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSnmmSentBytes.setUnits("bytes")
_CSpAccHCSnmmSentBytes_Type = Counter64
_CSpAccHCSnmmSentBytes_Object = MibTableColumn
cSpAccHCSnmmSentBytes = _CSpAccHCSnmmSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 19),
    _CSpAccHCSnmmSentBytes_Type()
)
cSpAccHCSnmmSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSnmmSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSnmmSentBytes.setUnits("bytes")
_CSpAccSntmRcvdPackets_Type = Counter32
_CSpAccSntmRcvdPackets_Object = MibTableColumn
cSpAccSntmRcvdPackets = _CSpAccSntmRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 20),
    _CSpAccSntmRcvdPackets_Type()
)
cSpAccSntmRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSntmRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSntmRcvdPackets.setUnits("packets")
_CSpAccHCSntmRcvdPackets_Type = Counter64
_CSpAccHCSntmRcvdPackets_Object = MibTableColumn
cSpAccHCSntmRcvdPackets = _CSpAccHCSntmRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 21),
    _CSpAccHCSntmRcvdPackets_Type()
)
cSpAccHCSntmRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSntmRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSntmRcvdPackets.setUnits("packets")
_CSpAccSntmRcvdBytes_Type = Counter32
_CSpAccSntmRcvdBytes_Object = MibTableColumn
cSpAccSntmRcvdBytes = _CSpAccSntmRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 22),
    _CSpAccSntmRcvdBytes_Type()
)
cSpAccSntmRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSntmRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSntmRcvdBytes.setUnits("bytes")
_CSpAccHCSntmRcvdBytes_Type = Counter64
_CSpAccHCSntmRcvdBytes_Object = MibTableColumn
cSpAccHCSntmRcvdBytes = _CSpAccHCSntmRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 23),
    _CSpAccHCSntmRcvdBytes_Type()
)
cSpAccHCSntmRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSntmRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSntmRcvdBytes.setUnits("bytes")
_CSpAccSntmSentPackets_Type = Counter32
_CSpAccSntmSentPackets_Object = MibTableColumn
cSpAccSntmSentPackets = _CSpAccSntmSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 24),
    _CSpAccSntmSentPackets_Type()
)
cSpAccSntmSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSntmSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSntmSentPackets.setUnits("packets")
_CSpAccHCSntmSentPackets_Type = Counter64
_CSpAccHCSntmSentPackets_Object = MibTableColumn
cSpAccHCSntmSentPackets = _CSpAccHCSntmSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 25),
    _CSpAccHCSntmSentPackets_Type()
)
cSpAccHCSntmSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSntmSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSntmSentPackets.setUnits("packets")
_CSpAccSntmSentBytes_Type = Counter32
_CSpAccSntmSentBytes_Object = MibTableColumn
cSpAccSntmSentBytes = _CSpAccSntmSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 26),
    _CSpAccSntmSentBytes_Type()
)
cSpAccSntmSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSntmSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSntmSentBytes.setUnits("bytes")
_CSpAccHCSntmSentBytes_Type = Counter64
_CSpAccHCSntmSentBytes_Object = MibTableColumn
cSpAccHCSntmSentBytes = _CSpAccHCSntmSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 27),
    _CSpAccHCSntmSentBytes_Type()
)
cSpAccHCSntmSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSntmSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSntmSentBytes.setUnits("bytes")
_CSpAccSpare2RcvdPackets_Type = Counter32
_CSpAccSpare2RcvdPackets_Object = MibTableColumn
cSpAccSpare2RcvdPackets = _CSpAccSpare2RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 28),
    _CSpAccSpare2RcvdPackets_Type()
)
cSpAccSpare2RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare2RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare2RcvdPackets.setUnits("packets")
_CSpAccHCSpare2RcvdPackets_Type = Counter64
_CSpAccHCSpare2RcvdPackets_Object = MibTableColumn
cSpAccHCSpare2RcvdPackets = _CSpAccHCSpare2RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 29),
    _CSpAccHCSpare2RcvdPackets_Type()
)
cSpAccHCSpare2RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare2RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare2RcvdPackets.setUnits("packets")
_CSpAccSpare2RcvdBytes_Type = Counter32
_CSpAccSpare2RcvdBytes_Object = MibTableColumn
cSpAccSpare2RcvdBytes = _CSpAccSpare2RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 30),
    _CSpAccSpare2RcvdBytes_Type()
)
cSpAccSpare2RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare2RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare2RcvdBytes.setUnits("bytes")
_CSpAccHCSpare2RcvdBytes_Type = Counter64
_CSpAccHCSpare2RcvdBytes_Object = MibTableColumn
cSpAccHCSpare2RcvdBytes = _CSpAccHCSpare2RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 31),
    _CSpAccHCSpare2RcvdBytes_Type()
)
cSpAccHCSpare2RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare2RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare2RcvdBytes.setUnits("bytes")
_CSpAccSpare2SentPackets_Type = Counter32
_CSpAccSpare2SentPackets_Object = MibTableColumn
cSpAccSpare2SentPackets = _CSpAccSpare2SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 32),
    _CSpAccSpare2SentPackets_Type()
)
cSpAccSpare2SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare2SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare2SentPackets.setUnits("packets")
_CSpAccHCSpare2SentPackets_Type = Counter64
_CSpAccHCSpare2SentPackets_Object = MibTableColumn
cSpAccHCSpare2SentPackets = _CSpAccHCSpare2SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 33),
    _CSpAccHCSpare2SentPackets_Type()
)
cSpAccHCSpare2SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare2SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare2SentPackets.setUnits("packets")
_CSpAccSpare2SentBytes_Type = Counter32
_CSpAccSpare2SentBytes_Object = MibTableColumn
cSpAccSpare2SentBytes = _CSpAccSpare2SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 34),
    _CSpAccSpare2SentBytes_Type()
)
cSpAccSpare2SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare2SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare2SentBytes.setUnits("bytes")
_CSpAccHCSpare2SentBytes_Type = Counter64
_CSpAccHCSpare2SentBytes_Object = MibTableColumn
cSpAccHCSpare2SentBytes = _CSpAccHCSpare2SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 35),
    _CSpAccHCSpare2SentBytes_Type()
)
cSpAccHCSpare2SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare2SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare2SentBytes.setUnits("bytes")
_CSpAccSccpRcvdPackets_Type = Counter32
_CSpAccSccpRcvdPackets_Object = MibTableColumn
cSpAccSccpRcvdPackets = _CSpAccSccpRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 36),
    _CSpAccSccpRcvdPackets_Type()
)
cSpAccSccpRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSccpRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSccpRcvdPackets.setUnits("packets")
_CSpAccHCSccpRcvdPackets_Type = Counter64
_CSpAccHCSccpRcvdPackets_Object = MibTableColumn
cSpAccHCSccpRcvdPackets = _CSpAccHCSccpRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 37),
    _CSpAccHCSccpRcvdPackets_Type()
)
cSpAccHCSccpRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSccpRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSccpRcvdPackets.setUnits("packets")
_CSpAccSccpRcvdBytes_Type = Counter32
_CSpAccSccpRcvdBytes_Object = MibTableColumn
cSpAccSccpRcvdBytes = _CSpAccSccpRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 38),
    _CSpAccSccpRcvdBytes_Type()
)
cSpAccSccpRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSccpRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSccpRcvdBytes.setUnits("bytes")
_CSpAccHCSccpRcvdBytes_Type = Counter64
_CSpAccHCSccpRcvdBytes_Object = MibTableColumn
cSpAccHCSccpRcvdBytes = _CSpAccHCSccpRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 39),
    _CSpAccHCSccpRcvdBytes_Type()
)
cSpAccHCSccpRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSccpRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSccpRcvdBytes.setUnits("bytes")
_CSpAccSccpSentPackets_Type = Counter32
_CSpAccSccpSentPackets_Object = MibTableColumn
cSpAccSccpSentPackets = _CSpAccSccpSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 40),
    _CSpAccSccpSentPackets_Type()
)
cSpAccSccpSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSccpSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSccpSentPackets.setUnits("packets")
_CSpAccHCSccpSentPackets_Type = Counter64
_CSpAccHCSccpSentPackets_Object = MibTableColumn
cSpAccHCSccpSentPackets = _CSpAccHCSccpSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 41),
    _CSpAccHCSccpSentPackets_Type()
)
cSpAccHCSccpSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSccpSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSccpSentPackets.setUnits("packets")
_CSpAccSccpSentBytes_Type = Counter32
_CSpAccSccpSentBytes_Object = MibTableColumn
cSpAccSccpSentBytes = _CSpAccSccpSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 42),
    _CSpAccSccpSentBytes_Type()
)
cSpAccSccpSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSccpSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSccpSentBytes.setUnits("bytes")
_CSpAccHCSccpSentBytes_Type = Counter64
_CSpAccHCSccpSentBytes_Object = MibTableColumn
cSpAccHCSccpSentBytes = _CSpAccHCSccpSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 43),
    _CSpAccHCSccpSentBytes_Type()
)
cSpAccHCSccpSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSccpSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSccpSentBytes.setUnits("bytes")
_CSpAccTupRcvdPackets_Type = Counter32
_CSpAccTupRcvdPackets_Object = MibTableColumn
cSpAccTupRcvdPackets = _CSpAccTupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 44),
    _CSpAccTupRcvdPackets_Type()
)
cSpAccTupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccTupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccTupRcvdPackets.setUnits("packets")
_CSpAccHCTupRcvdPackets_Type = Counter64
_CSpAccHCTupRcvdPackets_Object = MibTableColumn
cSpAccHCTupRcvdPackets = _CSpAccHCTupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 45),
    _CSpAccHCTupRcvdPackets_Type()
)
cSpAccHCTupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCTupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCTupRcvdPackets.setUnits("packets")
_CSpAccTupRcvdBytes_Type = Counter32
_CSpAccTupRcvdBytes_Object = MibTableColumn
cSpAccTupRcvdBytes = _CSpAccTupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 46),
    _CSpAccTupRcvdBytes_Type()
)
cSpAccTupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccTupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccTupRcvdBytes.setUnits("bytes")
_CSpAccHCTupRcvdBytes_Type = Counter64
_CSpAccHCTupRcvdBytes_Object = MibTableColumn
cSpAccHCTupRcvdBytes = _CSpAccHCTupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 47),
    _CSpAccHCTupRcvdBytes_Type()
)
cSpAccHCTupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCTupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCTupRcvdBytes.setUnits("bytes")
_CSpAccTupSentPackets_Type = Counter32
_CSpAccTupSentPackets_Object = MibTableColumn
cSpAccTupSentPackets = _CSpAccTupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 48),
    _CSpAccTupSentPackets_Type()
)
cSpAccTupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccTupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccTupSentPackets.setUnits("packets")
_CSpAccHCTupSentPackets_Type = Counter64
_CSpAccHCTupSentPackets_Object = MibTableColumn
cSpAccHCTupSentPackets = _CSpAccHCTupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 49),
    _CSpAccHCTupSentPackets_Type()
)
cSpAccHCTupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCTupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCTupSentPackets.setUnits("packets")
_CSpAccTupSentBytes_Type = Counter32
_CSpAccTupSentBytes_Object = MibTableColumn
cSpAccTupSentBytes = _CSpAccTupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 50),
    _CSpAccTupSentBytes_Type()
)
cSpAccTupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccTupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccTupSentBytes.setUnits("bytes")
_CSpAccHCTupSentBytes_Type = Counter64
_CSpAccHCTupSentBytes_Object = MibTableColumn
cSpAccHCTupSentBytes = _CSpAccHCTupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 51),
    _CSpAccHCTupSentBytes_Type()
)
cSpAccHCTupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCTupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCTupSentBytes.setUnits("bytes")
_CSpAccIsupRcvdPackets_Type = Counter32
_CSpAccIsupRcvdPackets_Object = MibTableColumn
cSpAccIsupRcvdPackets = _CSpAccIsupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 52),
    _CSpAccIsupRcvdPackets_Type()
)
cSpAccIsupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccIsupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccIsupRcvdPackets.setUnits("packets")
_CSpAccHCIsupRcvdPackets_Type = Counter64
_CSpAccHCIsupRcvdPackets_Object = MibTableColumn
cSpAccHCIsupRcvdPackets = _CSpAccHCIsupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 53),
    _CSpAccHCIsupRcvdPackets_Type()
)
cSpAccHCIsupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCIsupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCIsupRcvdPackets.setUnits("packets")
_CSpAccIsupRcvdBytes_Type = Counter32
_CSpAccIsupRcvdBytes_Object = MibTableColumn
cSpAccIsupRcvdBytes = _CSpAccIsupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 54),
    _CSpAccIsupRcvdBytes_Type()
)
cSpAccIsupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccIsupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccIsupRcvdBytes.setUnits("bytes")
_CSpAccHCIsupRcvdBytes_Type = Counter64
_CSpAccHCIsupRcvdBytes_Object = MibTableColumn
cSpAccHCIsupRcvdBytes = _CSpAccHCIsupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 55),
    _CSpAccHCIsupRcvdBytes_Type()
)
cSpAccHCIsupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCIsupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCIsupRcvdBytes.setUnits("bytes")
_CSpAccIsupSentPackets_Type = Counter32
_CSpAccIsupSentPackets_Object = MibTableColumn
cSpAccIsupSentPackets = _CSpAccIsupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 56),
    _CSpAccIsupSentPackets_Type()
)
cSpAccIsupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccIsupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccIsupSentPackets.setUnits("packets")
_CSpAccHCIsupSentPackets_Type = Counter64
_CSpAccHCIsupSentPackets_Object = MibTableColumn
cSpAccHCIsupSentPackets = _CSpAccHCIsupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 57),
    _CSpAccHCIsupSentPackets_Type()
)
cSpAccHCIsupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCIsupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCIsupSentPackets.setUnits("packets")
_CSpAccIsupSentBytes_Type = Counter32
_CSpAccIsupSentBytes_Object = MibTableColumn
cSpAccIsupSentBytes = _CSpAccIsupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 58),
    _CSpAccIsupSentBytes_Type()
)
cSpAccIsupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccIsupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccIsupSentBytes.setUnits("bytes")
_CSpAccHCIsupSentBytes_Type = Counter64
_CSpAccHCIsupSentBytes_Object = MibTableColumn
cSpAccHCIsupSentBytes = _CSpAccHCIsupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 59),
    _CSpAccHCIsupSentBytes_Type()
)
cSpAccHCIsupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCIsupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCIsupSentBytes.setUnits("bytes")
_CSpAccDupcRcvdPackets_Type = Counter32
_CSpAccDupcRcvdPackets_Object = MibTableColumn
cSpAccDupcRcvdPackets = _CSpAccDupcRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 60),
    _CSpAccDupcRcvdPackets_Type()
)
cSpAccDupcRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccDupcRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccDupcRcvdPackets.setUnits("packets")
_CSpAccHCDupcRcvdPackets_Type = Counter64
_CSpAccHCDupcRcvdPackets_Object = MibTableColumn
cSpAccHCDupcRcvdPackets = _CSpAccHCDupcRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 61),
    _CSpAccHCDupcRcvdPackets_Type()
)
cSpAccHCDupcRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCDupcRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCDupcRcvdPackets.setUnits("packets")
_CSpAccDupcRcvdBytes_Type = Counter32
_CSpAccDupcRcvdBytes_Object = MibTableColumn
cSpAccDupcRcvdBytes = _CSpAccDupcRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 62),
    _CSpAccDupcRcvdBytes_Type()
)
cSpAccDupcRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccDupcRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccDupcRcvdBytes.setUnits("bytes")
_CSpAccHCDupcRcvdBytes_Type = Counter64
_CSpAccHCDupcRcvdBytes_Object = MibTableColumn
cSpAccHCDupcRcvdBytes = _CSpAccHCDupcRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 63),
    _CSpAccHCDupcRcvdBytes_Type()
)
cSpAccHCDupcRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCDupcRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCDupcRcvdBytes.setUnits("bytes")
_CSpAccDupcSentPackets_Type = Counter32
_CSpAccDupcSentPackets_Object = MibTableColumn
cSpAccDupcSentPackets = _CSpAccDupcSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 64),
    _CSpAccDupcSentPackets_Type()
)
cSpAccDupcSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccDupcSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccDupcSentPackets.setUnits("packets")
_CSpAccHCDupcSentPackets_Type = Counter64
_CSpAccHCDupcSentPackets_Object = MibTableColumn
cSpAccHCDupcSentPackets = _CSpAccHCDupcSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 65),
    _CSpAccHCDupcSentPackets_Type()
)
cSpAccHCDupcSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCDupcSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCDupcSentPackets.setUnits("packets")
_CSpAccDupcSentBytes_Type = Counter32
_CSpAccDupcSentBytes_Object = MibTableColumn
cSpAccDupcSentBytes = _CSpAccDupcSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 66),
    _CSpAccDupcSentBytes_Type()
)
cSpAccDupcSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccDupcSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccDupcSentBytes.setUnits("bytes")
_CSpAccHCDupcSentBytes_Type = Counter64
_CSpAccHCDupcSentBytes_Object = MibTableColumn
cSpAccHCDupcSentBytes = _CSpAccHCDupcSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 67),
    _CSpAccHCDupcSentBytes_Type()
)
cSpAccHCDupcSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCDupcSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCDupcSentBytes.setUnits("bytes")
_CSpAccDupfRcvdPackets_Type = Counter32
_CSpAccDupfRcvdPackets_Object = MibTableColumn
cSpAccDupfRcvdPackets = _CSpAccDupfRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 68),
    _CSpAccDupfRcvdPackets_Type()
)
cSpAccDupfRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccDupfRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccDupfRcvdPackets.setUnits("packets")
_CSpAccHCDupfRcvdPackets_Type = Counter64
_CSpAccHCDupfRcvdPackets_Object = MibTableColumn
cSpAccHCDupfRcvdPackets = _CSpAccHCDupfRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 69),
    _CSpAccHCDupfRcvdPackets_Type()
)
cSpAccHCDupfRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCDupfRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCDupfRcvdPackets.setUnits("packets")
_CSpAccDupfRcvdBytes_Type = Counter32
_CSpAccDupfRcvdBytes_Object = MibTableColumn
cSpAccDupfRcvdBytes = _CSpAccDupfRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 70),
    _CSpAccDupfRcvdBytes_Type()
)
cSpAccDupfRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccDupfRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccDupfRcvdBytes.setUnits("bytes")
_CSpAccHCDupfRcvdBytes_Type = Counter64
_CSpAccHCDupfRcvdBytes_Object = MibTableColumn
cSpAccHCDupfRcvdBytes = _CSpAccHCDupfRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 71),
    _CSpAccHCDupfRcvdBytes_Type()
)
cSpAccHCDupfRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCDupfRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCDupfRcvdBytes.setUnits("bytes")
_CSpAccDupfSentPackets_Type = Counter32
_CSpAccDupfSentPackets_Object = MibTableColumn
cSpAccDupfSentPackets = _CSpAccDupfSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 72),
    _CSpAccDupfSentPackets_Type()
)
cSpAccDupfSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccDupfSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccDupfSentPackets.setUnits("packets")
_CSpAccHCDupfSentPackets_Type = Counter64
_CSpAccHCDupfSentPackets_Object = MibTableColumn
cSpAccHCDupfSentPackets = _CSpAccHCDupfSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 73),
    _CSpAccHCDupfSentPackets_Type()
)
cSpAccHCDupfSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCDupfSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCDupfSentPackets.setUnits("packets")
_CSpAccDupfSentBytes_Type = Counter32
_CSpAccDupfSentBytes_Object = MibTableColumn
cSpAccDupfSentBytes = _CSpAccDupfSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 74),
    _CSpAccDupfSentBytes_Type()
)
cSpAccDupfSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccDupfSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccDupfSentBytes.setUnits("bytes")
_CSpAccHCDupfSentBytes_Type = Counter64
_CSpAccHCDupfSentBytes_Object = MibTableColumn
cSpAccHCDupfSentBytes = _CSpAccHCDupfSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 75),
    _CSpAccHCDupfSentBytes_Type()
)
cSpAccHCDupfSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCDupfSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCDupfSentBytes.setUnits("bytes")
_CSpAccMtupRcvdPackets_Type = Counter32
_CSpAccMtupRcvdPackets_Object = MibTableColumn
cSpAccMtupRcvdPackets = _CSpAccMtupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 76),
    _CSpAccMtupRcvdPackets_Type()
)
cSpAccMtupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccMtupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccMtupRcvdPackets.setUnits("packets")
_CSpAccHCMtupRcvdPackets_Type = Counter64
_CSpAccHCMtupRcvdPackets_Object = MibTableColumn
cSpAccHCMtupRcvdPackets = _CSpAccHCMtupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 77),
    _CSpAccHCMtupRcvdPackets_Type()
)
cSpAccHCMtupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCMtupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCMtupRcvdPackets.setUnits("packets")
_CSpAccMtupRcvdBytes_Type = Counter32
_CSpAccMtupRcvdBytes_Object = MibTableColumn
cSpAccMtupRcvdBytes = _CSpAccMtupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 78),
    _CSpAccMtupRcvdBytes_Type()
)
cSpAccMtupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccMtupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccMtupRcvdBytes.setUnits("bytes")
_CSpAccHCMtupRcvdBytes_Type = Counter64
_CSpAccHCMtupRcvdBytes_Object = MibTableColumn
cSpAccHCMtupRcvdBytes = _CSpAccHCMtupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 79),
    _CSpAccHCMtupRcvdBytes_Type()
)
cSpAccHCMtupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCMtupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCMtupRcvdBytes.setUnits("bytes")
_CSpAccMtupSentPackets_Type = Counter32
_CSpAccMtupSentPackets_Object = MibTableColumn
cSpAccMtupSentPackets = _CSpAccMtupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 80),
    _CSpAccMtupSentPackets_Type()
)
cSpAccMtupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccMtupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccMtupSentPackets.setUnits("packets")
_CSpAccHCMtupSentPackets_Type = Counter64
_CSpAccHCMtupSentPackets_Object = MibTableColumn
cSpAccHCMtupSentPackets = _CSpAccHCMtupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 81),
    _CSpAccHCMtupSentPackets_Type()
)
cSpAccHCMtupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCMtupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCMtupSentPackets.setUnits("packets")
_CSpAccMtupSentBytes_Type = Counter32
_CSpAccMtupSentBytes_Object = MibTableColumn
cSpAccMtupSentBytes = _CSpAccMtupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 82),
    _CSpAccMtupSentBytes_Type()
)
cSpAccMtupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccMtupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccMtupSentBytes.setUnits("bytes")
_CSpAccHCMtupSentBytes_Type = Counter64
_CSpAccHCMtupSentBytes_Object = MibTableColumn
cSpAccHCMtupSentBytes = _CSpAccHCMtupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 83),
    _CSpAccHCMtupSentBytes_Type()
)
cSpAccHCMtupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCMtupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCMtupSentBytes.setUnits("bytes")
_CSpAccBisupRcvdPackets_Type = Counter32
_CSpAccBisupRcvdPackets_Object = MibTableColumn
cSpAccBisupRcvdPackets = _CSpAccBisupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 84),
    _CSpAccBisupRcvdPackets_Type()
)
cSpAccBisupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccBisupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccBisupRcvdPackets.setUnits("packets")
_CSpAccHCBisupRcvdPackets_Type = Counter64
_CSpAccHCBisupRcvdPackets_Object = MibTableColumn
cSpAccHCBisupRcvdPackets = _CSpAccHCBisupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 85),
    _CSpAccHCBisupRcvdPackets_Type()
)
cSpAccHCBisupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCBisupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCBisupRcvdPackets.setUnits("packets")
_CSpAccBisupRcvdBytes_Type = Counter32
_CSpAccBisupRcvdBytes_Object = MibTableColumn
cSpAccBisupRcvdBytes = _CSpAccBisupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 86),
    _CSpAccBisupRcvdBytes_Type()
)
cSpAccBisupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccBisupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccBisupRcvdBytes.setUnits("bytes")
_CSpAccHCBisupRcvdBytes_Type = Counter64
_CSpAccHCBisupRcvdBytes_Object = MibTableColumn
cSpAccHCBisupRcvdBytes = _CSpAccHCBisupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 87),
    _CSpAccHCBisupRcvdBytes_Type()
)
cSpAccHCBisupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCBisupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCBisupRcvdBytes.setUnits("bytes")
_CSpAccBisupSentPackets_Type = Counter32
_CSpAccBisupSentPackets_Object = MibTableColumn
cSpAccBisupSentPackets = _CSpAccBisupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 88),
    _CSpAccBisupSentPackets_Type()
)
cSpAccBisupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccBisupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccBisupSentPackets.setUnits("packets")
_CSpAccHCBisupSentPackets_Type = Counter64
_CSpAccHCBisupSentPackets_Object = MibTableColumn
cSpAccHCBisupSentPackets = _CSpAccHCBisupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 89),
    _CSpAccHCBisupSentPackets_Type()
)
cSpAccHCBisupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCBisupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCBisupSentPackets.setUnits("packets")
_CSpAccBisupSentBytes_Type = Counter32
_CSpAccBisupSentBytes_Object = MibTableColumn
cSpAccBisupSentBytes = _CSpAccBisupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 90),
    _CSpAccBisupSentBytes_Type()
)
cSpAccBisupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccBisupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccBisupSentBytes.setUnits("bytes")
_CSpAccHCBisupSentBytes_Type = Counter64
_CSpAccHCBisupSentBytes_Object = MibTableColumn
cSpAccHCBisupSentBytes = _CSpAccHCBisupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 91),
    _CSpAccHCBisupSentBytes_Type()
)
cSpAccHCBisupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCBisupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCBisupSentBytes.setUnits("bytes")
_CSpAccSisupRcvdPackets_Type = Counter32
_CSpAccSisupRcvdPackets_Object = MibTableColumn
cSpAccSisupRcvdPackets = _CSpAccSisupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 92),
    _CSpAccSisupRcvdPackets_Type()
)
cSpAccSisupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSisupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSisupRcvdPackets.setUnits("packets")
_CSpAccHCSisupRcvdPackets_Type = Counter64
_CSpAccHCSisupRcvdPackets_Object = MibTableColumn
cSpAccHCSisupRcvdPackets = _CSpAccHCSisupRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 93),
    _CSpAccHCSisupRcvdPackets_Type()
)
cSpAccHCSisupRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSisupRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSisupRcvdPackets.setUnits("packets")
_CSpAccSisupRcvdBytes_Type = Counter32
_CSpAccSisupRcvdBytes_Object = MibTableColumn
cSpAccSisupRcvdBytes = _CSpAccSisupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 94),
    _CSpAccSisupRcvdBytes_Type()
)
cSpAccSisupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSisupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSisupRcvdBytes.setUnits("bytes")
_CSpAccHCSisupRcvdBytes_Type = Counter64
_CSpAccHCSisupRcvdBytes_Object = MibTableColumn
cSpAccHCSisupRcvdBytes = _CSpAccHCSisupRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 95),
    _CSpAccHCSisupRcvdBytes_Type()
)
cSpAccHCSisupRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSisupRcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSisupRcvdBytes.setUnits("bytes")
_CSpAccSisupSentPackets_Type = Counter32
_CSpAccSisupSentPackets_Object = MibTableColumn
cSpAccSisupSentPackets = _CSpAccSisupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 96),
    _CSpAccSisupSentPackets_Type()
)
cSpAccSisupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSisupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSisupSentPackets.setUnits("packets")
_CSpAccHCSisupSentPackets_Type = Counter64
_CSpAccHCSisupSentPackets_Object = MibTableColumn
cSpAccHCSisupSentPackets = _CSpAccHCSisupSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 97),
    _CSpAccHCSisupSentPackets_Type()
)
cSpAccHCSisupSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSisupSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSisupSentPackets.setUnits("packets")
_CSpAccSisupSentBytes_Type = Counter32
_CSpAccSisupSentBytes_Object = MibTableColumn
cSpAccSisupSentBytes = _CSpAccSisupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 98),
    _CSpAccSisupSentBytes_Type()
)
cSpAccSisupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSisupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSisupSentBytes.setUnits("bytes")
_CSpAccHCSisupSentBytes_Type = Counter64
_CSpAccHCSisupSentBytes_Object = MibTableColumn
cSpAccHCSisupSentBytes = _CSpAccHCSisupSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 99),
    _CSpAccHCSisupSentBytes_Type()
)
cSpAccHCSisupSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSisupSentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSisupSentBytes.setUnits("bytes")
_CSpAccSpare11RcvdPackets_Type = Counter32
_CSpAccSpare11RcvdPackets_Object = MibTableColumn
cSpAccSpare11RcvdPackets = _CSpAccSpare11RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 100),
    _CSpAccSpare11RcvdPackets_Type()
)
cSpAccSpare11RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare11RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare11RcvdPackets.setUnits("packets")
_CSpAccHCSpare11RcvdPackets_Type = Counter64
_CSpAccHCSpare11RcvdPackets_Object = MibTableColumn
cSpAccHCSpare11RcvdPackets = _CSpAccHCSpare11RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 101),
    _CSpAccHCSpare11RcvdPackets_Type()
)
cSpAccHCSpare11RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare11RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare11RcvdPackets.setUnits("packets")
_CSpAccSpare11RcvdBytes_Type = Counter32
_CSpAccSpare11RcvdBytes_Object = MibTableColumn
cSpAccSpare11RcvdBytes = _CSpAccSpare11RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 102),
    _CSpAccSpare11RcvdBytes_Type()
)
cSpAccSpare11RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare11RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare11RcvdBytes.setUnits("bytes")
_CSpAccHCSpare11RcvdBytes_Type = Counter64
_CSpAccHCSpare11RcvdBytes_Object = MibTableColumn
cSpAccHCSpare11RcvdBytes = _CSpAccHCSpare11RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 103),
    _CSpAccHCSpare11RcvdBytes_Type()
)
cSpAccHCSpare11RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare11RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare11RcvdBytes.setUnits("bytes")
_CSpAccSpare11SentPackets_Type = Counter32
_CSpAccSpare11SentPackets_Object = MibTableColumn
cSpAccSpare11SentPackets = _CSpAccSpare11SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 104),
    _CSpAccSpare11SentPackets_Type()
)
cSpAccSpare11SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare11SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare11SentPackets.setUnits("packets")
_CSpAccHCSpare11SentPackets_Type = Counter64
_CSpAccHCSpare11SentPackets_Object = MibTableColumn
cSpAccHCSpare11SentPackets = _CSpAccHCSpare11SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 105),
    _CSpAccHCSpare11SentPackets_Type()
)
cSpAccHCSpare11SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare11SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare11SentPackets.setUnits("packets")
_CSpAccSpare11SentBytes_Type = Counter32
_CSpAccSpare11SentBytes_Object = MibTableColumn
cSpAccSpare11SentBytes = _CSpAccSpare11SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 106),
    _CSpAccSpare11SentBytes_Type()
)
cSpAccSpare11SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare11SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare11SentBytes.setUnits("bytes")
_CSpAccHCSpare11SentBytes_Type = Counter64
_CSpAccHCSpare11SentBytes_Object = MibTableColumn
cSpAccHCSpare11SentBytes = _CSpAccHCSpare11SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 107),
    _CSpAccHCSpare11SentBytes_Type()
)
cSpAccHCSpare11SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare11SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare11SentBytes.setUnits("bytes")
_CSpAccSpare12RcvdPackets_Type = Counter32
_CSpAccSpare12RcvdPackets_Object = MibTableColumn
cSpAccSpare12RcvdPackets = _CSpAccSpare12RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 108),
    _CSpAccSpare12RcvdPackets_Type()
)
cSpAccSpare12RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare12RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare12RcvdPackets.setUnits("packets")
_CSpAccHCSpare12RcvdPackets_Type = Counter64
_CSpAccHCSpare12RcvdPackets_Object = MibTableColumn
cSpAccHCSpare12RcvdPackets = _CSpAccHCSpare12RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 109),
    _CSpAccHCSpare12RcvdPackets_Type()
)
cSpAccHCSpare12RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare12RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare12RcvdPackets.setUnits("packets")
_CSpAccSpare12RcvdBytes_Type = Counter32
_CSpAccSpare12RcvdBytes_Object = MibTableColumn
cSpAccSpare12RcvdBytes = _CSpAccSpare12RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 110),
    _CSpAccSpare12RcvdBytes_Type()
)
cSpAccSpare12RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare12RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare12RcvdBytes.setUnits("bytes")
_CSpAccHCSpare12RcvdBytes_Type = Counter64
_CSpAccHCSpare12RcvdBytes_Object = MibTableColumn
cSpAccHCSpare12RcvdBytes = _CSpAccHCSpare12RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 111),
    _CSpAccHCSpare12RcvdBytes_Type()
)
cSpAccHCSpare12RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare12RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare12RcvdBytes.setUnits("bytes")
_CSpAccSpare12SentPackets_Type = Counter32
_CSpAccSpare12SentPackets_Object = MibTableColumn
cSpAccSpare12SentPackets = _CSpAccSpare12SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 112),
    _CSpAccSpare12SentPackets_Type()
)
cSpAccSpare12SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare12SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare12SentPackets.setUnits("packets")
_CSpAccHCSpare12SentPackets_Type = Counter64
_CSpAccHCSpare12SentPackets_Object = MibTableColumn
cSpAccHCSpare12SentPackets = _CSpAccHCSpare12SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 113),
    _CSpAccHCSpare12SentPackets_Type()
)
cSpAccHCSpare12SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare12SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare12SentPackets.setUnits("packets")
_CSpAccSpare12SentBytes_Type = Counter32
_CSpAccSpare12SentBytes_Object = MibTableColumn
cSpAccSpare12SentBytes = _CSpAccSpare12SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 114),
    _CSpAccSpare12SentBytes_Type()
)
cSpAccSpare12SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare12SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare12SentBytes.setUnits("bytes")
_CSpAccHCSpare12SentBytes_Type = Counter64
_CSpAccHCSpare12SentBytes_Object = MibTableColumn
cSpAccHCSpare12SentBytes = _CSpAccHCSpare12SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 115),
    _CSpAccHCSpare12SentBytes_Type()
)
cSpAccHCSpare12SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare12SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare12SentBytes.setUnits("bytes")
_CSpAccSpare13RcvdPackets_Type = Counter32
_CSpAccSpare13RcvdPackets_Object = MibTableColumn
cSpAccSpare13RcvdPackets = _CSpAccSpare13RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 116),
    _CSpAccSpare13RcvdPackets_Type()
)
cSpAccSpare13RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare13RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare13RcvdPackets.setUnits("packets")
_CSpAccHCSpare13RcvdPackets_Type = Counter64
_CSpAccHCSpare13RcvdPackets_Object = MibTableColumn
cSpAccHCSpare13RcvdPackets = _CSpAccHCSpare13RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 117),
    _CSpAccHCSpare13RcvdPackets_Type()
)
cSpAccHCSpare13RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare13RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare13RcvdPackets.setUnits("packets")
_CSpAccSpare13RcvdBytes_Type = Counter32
_CSpAccSpare13RcvdBytes_Object = MibTableColumn
cSpAccSpare13RcvdBytes = _CSpAccSpare13RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 118),
    _CSpAccSpare13RcvdBytes_Type()
)
cSpAccSpare13RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare13RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare13RcvdBytes.setUnits("bytes")
_CSpAccHCSpare13RcvdBytes_Type = Counter64
_CSpAccHCSpare13RcvdBytes_Object = MibTableColumn
cSpAccHCSpare13RcvdBytes = _CSpAccHCSpare13RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 119),
    _CSpAccHCSpare13RcvdBytes_Type()
)
cSpAccHCSpare13RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare13RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare13RcvdBytes.setUnits("bytes")
_CSpAccSpare13SentPackets_Type = Counter32
_CSpAccSpare13SentPackets_Object = MibTableColumn
cSpAccSpare13SentPackets = _CSpAccSpare13SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 120),
    _CSpAccSpare13SentPackets_Type()
)
cSpAccSpare13SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare13SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare13SentPackets.setUnits("packets")
_CSpAccHCSpare13SentPackets_Type = Counter64
_CSpAccHCSpare13SentPackets_Object = MibTableColumn
cSpAccHCSpare13SentPackets = _CSpAccHCSpare13SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 121),
    _CSpAccHCSpare13SentPackets_Type()
)
cSpAccHCSpare13SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare13SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare13SentPackets.setUnits("packets")
_CSpAccSpare13SentBytes_Type = Counter32
_CSpAccSpare13SentBytes_Object = MibTableColumn
cSpAccSpare13SentBytes = _CSpAccSpare13SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 122),
    _CSpAccSpare13SentBytes_Type()
)
cSpAccSpare13SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare13SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare13SentBytes.setUnits("bytes")
_CSpAccHCSpare13SentBytes_Type = Counter64
_CSpAccHCSpare13SentBytes_Object = MibTableColumn
cSpAccHCSpare13SentBytes = _CSpAccHCSpare13SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 123),
    _CSpAccHCSpare13SentBytes_Type()
)
cSpAccHCSpare13SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare13SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare13SentBytes.setUnits("bytes")
_CSpAccSpare14RcvdPackets_Type = Counter32
_CSpAccSpare14RcvdPackets_Object = MibTableColumn
cSpAccSpare14RcvdPackets = _CSpAccSpare14RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 124),
    _CSpAccSpare14RcvdPackets_Type()
)
cSpAccSpare14RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare14RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare14RcvdPackets.setUnits("packets")
_CSpAccHCSpare14RcvdPackets_Type = Counter64
_CSpAccHCSpare14RcvdPackets_Object = MibTableColumn
cSpAccHCSpare14RcvdPackets = _CSpAccHCSpare14RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 125),
    _CSpAccHCSpare14RcvdPackets_Type()
)
cSpAccHCSpare14RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare14RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare14RcvdPackets.setUnits("packets")
_CSpAccSpare14RcvdBytes_Type = Counter32
_CSpAccSpare14RcvdBytes_Object = MibTableColumn
cSpAccSpare14RcvdBytes = _CSpAccSpare14RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 126),
    _CSpAccSpare14RcvdBytes_Type()
)
cSpAccSpare14RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare14RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare14RcvdBytes.setUnits("bytes")
_CSpAccHCSpare14RcvdBytes_Type = Counter64
_CSpAccHCSpare14RcvdBytes_Object = MibTableColumn
cSpAccHCSpare14RcvdBytes = _CSpAccHCSpare14RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 127),
    _CSpAccHCSpare14RcvdBytes_Type()
)
cSpAccHCSpare14RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare14RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare14RcvdBytes.setUnits("bytes")
_CSpAccSpare14SentPackets_Type = Counter32
_CSpAccSpare14SentPackets_Object = MibTableColumn
cSpAccSpare14SentPackets = _CSpAccSpare14SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 128),
    _CSpAccSpare14SentPackets_Type()
)
cSpAccSpare14SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare14SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare14SentPackets.setUnits("packets")
_CSpAccHCSpare14SentPackets_Type = Counter64
_CSpAccHCSpare14SentPackets_Object = MibTableColumn
cSpAccHCSpare14SentPackets = _CSpAccHCSpare14SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 129),
    _CSpAccHCSpare14SentPackets_Type()
)
cSpAccHCSpare14SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare14SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare14SentPackets.setUnits("packets")
_CSpAccSpare14SentBytes_Type = Counter32
_CSpAccSpare14SentBytes_Object = MibTableColumn
cSpAccSpare14SentBytes = _CSpAccSpare14SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 130),
    _CSpAccSpare14SentBytes_Type()
)
cSpAccSpare14SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare14SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare14SentBytes.setUnits("bytes")
_CSpAccHCSpare14SentBytes_Type = Counter64
_CSpAccHCSpare14SentBytes_Object = MibTableColumn
cSpAccHCSpare14SentBytes = _CSpAccHCSpare14SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 131),
    _CSpAccHCSpare14SentBytes_Type()
)
cSpAccHCSpare14SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare14SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare14SentBytes.setUnits("bytes")
_CSpAccSpare15RcvdPackets_Type = Counter32
_CSpAccSpare15RcvdPackets_Object = MibTableColumn
cSpAccSpare15RcvdPackets = _CSpAccSpare15RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 132),
    _CSpAccSpare15RcvdPackets_Type()
)
cSpAccSpare15RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare15RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare15RcvdPackets.setUnits("packets")
_CSpAccHCSpare15RcvdPackets_Type = Counter64
_CSpAccHCSpare15RcvdPackets_Object = MibTableColumn
cSpAccHCSpare15RcvdPackets = _CSpAccHCSpare15RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 133),
    _CSpAccHCSpare15RcvdPackets_Type()
)
cSpAccHCSpare15RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare15RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare15RcvdPackets.setUnits("packets")
_CSpAccSpare15RcvdBytes_Type = Counter32
_CSpAccSpare15RcvdBytes_Object = MibTableColumn
cSpAccSpare15RcvdBytes = _CSpAccSpare15RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 134),
    _CSpAccSpare15RcvdBytes_Type()
)
cSpAccSpare15RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare15RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare15RcvdBytes.setUnits("bytes")
_CSpAccHCSpare15RcvdBytes_Type = Counter64
_CSpAccHCSpare15RcvdBytes_Object = MibTableColumn
cSpAccHCSpare15RcvdBytes = _CSpAccHCSpare15RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 135),
    _CSpAccHCSpare15RcvdBytes_Type()
)
cSpAccHCSpare15RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare15RcvdBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare15RcvdBytes.setUnits("bytes")
_CSpAccSpare15SentPackets_Type = Counter32
_CSpAccSpare15SentPackets_Object = MibTableColumn
cSpAccSpare15SentPackets = _CSpAccSpare15SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 136),
    _CSpAccSpare15SentPackets_Type()
)
cSpAccSpare15SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare15SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare15SentPackets.setUnits("packets")
_CSpAccHCSpare15SentPackets_Type = Counter64
_CSpAccHCSpare15SentPackets_Object = MibTableColumn
cSpAccHCSpare15SentPackets = _CSpAccHCSpare15SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 137),
    _CSpAccHCSpare15SentPackets_Type()
)
cSpAccHCSpare15SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare15SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare15SentPackets.setUnits("packets")
_CSpAccSpare15SentBytes_Type = Counter32
_CSpAccSpare15SentBytes_Object = MibTableColumn
cSpAccSpare15SentBytes = _CSpAccSpare15SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 138),
    _CSpAccSpare15SentBytes_Type()
)
cSpAccSpare15SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccSpare15SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccSpare15SentBytes.setUnits("bytes")
_CSpAccHCSpare15SentBytes_Type = Counter64
_CSpAccHCSpare15SentBytes_Object = MibTableColumn
cSpAccHCSpare15SentBytes = _CSpAccHCSpare15SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 6, 1, 1, 139),
    _CSpAccHCSpare15SentBytes_Type()
)
cSpAccHCSpare15SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSpAccHCSpare15SentBytes.setStatus("current")
if mibBuilder.loadTexts:
    cSpAccHCSpare15SentBytes.setUnits("bytes")
_CSpNotificationsEnable_ObjectIdentity = ObjectIdentity
cSpNotificationsEnable = _CSpNotificationsEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 7)
)


class _CSpLsStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cSpLsStateChangeNotifEnabled based on TruthValue"""


_CSpLsStateChangeNotifEnabled_Object = MibScalar
cSpLsStateChangeNotifEnabled = _CSpLsStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 7, 1),
    _CSpLsStateChangeNotifEnabled_Type()
)
cSpLsStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSpLsStateChangeNotifEnabled.setStatus("current")


class _CSpLnkStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cSpLnkStateChangeNotifEnabled based on TruthValue"""


_CSpLnkStateChangeNotifEnabled_Object = MibScalar
cSpLnkStateChangeNotifEnabled = _CSpLnkStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 1, 7, 2),
    _CSpLnkStateChangeNotifEnabled_Type()
)
cSpLnkStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSpLnkStateChangeNotifEnabled.setStatus("current")
_CiscoSpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoSpMIBNotificationPrefix = _CiscoSpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 2)
)
_CiscoSpMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSpMIBNotifications = _CiscoSpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 2, 0)
)
_CiscoSpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSpMIBConformance = _CiscoSpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3)
)
_CiscoSpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSpMIBCompliances = _CiscoSpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 1)
)
_CiscoSpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSpMIBGroups = _CiscoSpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 2)
)

# Managed Objects groups

ciscoSpSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 2, 1)
)
ciscoSpSwitchGroup.setObjects(
      *(("CISCO-SP-MIB", "cSpPointCode"),
        ("CISCO-SP-MIB", "cSpSs7Variant"),
        ("CISCO-SP-MIB", "cSpMtp2T01"),
        ("CISCO-SP-MIB", "cSpMtp2T02"),
        ("CISCO-SP-MIB", "cSpMtp2T03"),
        ("CISCO-SP-MIB", "cSpMtp2T4N"),
        ("CISCO-SP-MIB", "cSpMtp2T4E"),
        ("CISCO-SP-MIB", "cSpMtp2T05"),
        ("CISCO-SP-MIB", "cSpMtp2T06"),
        ("CISCO-SP-MIB", "cSpMtp2T07"),
        ("CISCO-SP-MIB", "cSpMtp2T08"),
        ("CISCO-SP-MIB", "cSpMtp3T01"),
        ("CISCO-SP-MIB", "cSpMtp3T02"),
        ("CISCO-SP-MIB", "cSpMtp3T03"),
        ("CISCO-SP-MIB", "cSpMtp3T04"),
        ("CISCO-SP-MIB", "cSpMtp3T05"),
        ("CISCO-SP-MIB", "cSpMtp3T06"),
        ("CISCO-SP-MIB", "cSpMtp3T07"),
        ("CISCO-SP-MIB", "cSpMtp3T08"),
        ("CISCO-SP-MIB", "cSpMtp3T10"),
        ("CISCO-SP-MIB", "cSpMtp3T11"),
        ("CISCO-SP-MIB", "cSpMtp3T12"),
        ("CISCO-SP-MIB", "cSpMtp3T13"),
        ("CISCO-SP-MIB", "cSpMtp3T14"),
        ("CISCO-SP-MIB", "cSpMtp3T15"),
        ("CISCO-SP-MIB", "cSpMtp3T16"),
        ("CISCO-SP-MIB", "cSpMtp3T17"),
        ("CISCO-SP-MIB", "cSpMtp3T18"),
        ("CISCO-SP-MIB", "cSpMtp3T19"),
        ("CISCO-SP-MIB", "cSpMtp3T20"),
        ("CISCO-SP-MIB", "cSpMtp3T21"),
        ("CISCO-SP-MIB", "cSpMtp3T22"),
        ("CISCO-SP-MIB", "cSpMtp3T23"),
        ("CISCO-SP-MIB", "cSpMtp3T24"),
        ("CISCO-SP-MIB", "cSpMtp3T25"),
        ("CISCO-SP-MIB", "cSpMtp3T26"),
        ("CISCO-SP-MIB", "cSpMtp3T27"),
        ("CISCO-SP-MIB", "cSpMtp3T28"),
        ("CISCO-SP-MIB", "cSpMtp3T29"),
        ("CISCO-SP-MIB", "cSpMtp3T30"),
        ("CISCO-SP-MIB", "cSpMtp3T31"),
        ("CISCO-SP-MIB", "cSpMtp3T32"),
        ("CISCO-SP-MIB", "cSpMtp3T33"),
        ("CISCO-SP-MIB", "cSpMtp3T34"))
)
if mibBuilder.loadTexts:
    ciscoSpSwitchGroup.setStatus("current")

ciscoSpLinksetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 2, 2)
)
ciscoSpLinksetGroup.setObjects(
      *(("CISCO-SP-MIB", "cSpLinksetAdjacentPointCode"),
        ("CISCO-SP-MIB", "cSpLinksetState"),
        ("CISCO-SP-MIB", "cSpLinksetInboundAcl"),
        ("CISCO-SP-MIB", "cSpLinksetOutboundAcl"),
        ("CISCO-SP-MIB", "cSpLinksetSnmmRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetSntmRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetSpare2RouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetSccpRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetTupRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetIsupRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetDupcRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetDupfRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetMtupRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetBisupRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetSisupRouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetSpare11RouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetSpare12RouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetSpare13RouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetSpare14RouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetSpare15RouteTableName"),
        ("CISCO-SP-MIB", "cSpLinksetAccountingEnabled"),
        ("CISCO-SP-MIB", "cSpLinksetNumLinks"),
        ("CISCO-SP-MIB", "cSpLinksetPacketsSent"),
        ("CISCO-SP-MIB", "cSpLinksetHCPacketsSent"),
        ("CISCO-SP-MIB", "cSpLinksetPacketsRcvd"),
        ("CISCO-SP-MIB", "cSpLinksetHCPacketsRcvd"),
        ("CISCO-SP-MIB", "cSpLinksetBytesSent"),
        ("CISCO-SP-MIB", "cSpLinksetHCBytesSent"),
        ("CISCO-SP-MIB", "cSpLinksetBytesRcvd"),
        ("CISCO-SP-MIB", "cSpLinksetHCBytesRcvd"),
        ("CISCO-SP-MIB", "cSpLinksetDurationInService"),
        ("CISCO-SP-MIB", "cSpLinksetDurationOutService"),
        ("CISCO-SP-MIB", "cSpLinksetMtp2T01"),
        ("CISCO-SP-MIB", "cSpLinksetMtp2T02"),
        ("CISCO-SP-MIB", "cSpLinksetMtp2T03"),
        ("CISCO-SP-MIB", "cSpLinksetMtp2T4N"),
        ("CISCO-SP-MIB", "cSpLinksetMtp2T4E"),
        ("CISCO-SP-MIB", "cSpLinksetMtp2T05"),
        ("CISCO-SP-MIB", "cSpLinksetMtp2T06"),
        ("CISCO-SP-MIB", "cSpLinksetMtp2T07"),
        ("CISCO-SP-MIB", "cSpLinksetMtp2T08"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T01"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T02"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T03"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T04"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T05"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T06"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T07"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T08"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T10"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T11"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T12"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T13"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T14"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T15"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T16"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T17"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T18"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T19"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T20"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T21"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T22"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T23"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T24"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T25"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T26"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T27"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T28"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T29"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T30"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T31"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T32"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T33"),
        ("CISCO-SP-MIB", "cSpLinksetMtp3T34"))
)
if mibBuilder.loadTexts:
    ciscoSpLinksetGroup.setStatus("current")

ciscoSpLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 2, 3)
)
ciscoSpLinkGroup.setObjects(
      *(("CISCO-SP-MIB", "cSpLinkState"),
        ("CISCO-SP-MIB", "cSpLinkType"),
        ("CISCO-SP-MIB", "cSpLinkifIndex"),
        ("CISCO-SP-MIB", "cSpLinkSctpAssociation"),
        ("CISCO-SP-MIB", "cSpLinkMtp3PacketsRcvd"),
        ("CISCO-SP-MIB", "cSpLinkMtp3PacketsSent"),
        ("CISCO-SP-MIB", "cSpLinkHCMtp3PacketsRcvd"),
        ("CISCO-SP-MIB", "cSpLinkHCMtp3PacketsSent"),
        ("CISCO-SP-MIB", "cSpLinkMtp3BytesRcvd"),
        ("CISCO-SP-MIB", "cSpLinkMtp3BytesSent"),
        ("CISCO-SP-MIB", "cSpLinkHCMtp3BytesRcvd"),
        ("CISCO-SP-MIB", "cSpLinkHCMtp3BytesSent"),
        ("CISCO-SP-MIB", "cSpLinkMtp2T01"),
        ("CISCO-SP-MIB", "cSpLinkMtp2T02"),
        ("CISCO-SP-MIB", "cSpLinkMtp2T03"),
        ("CISCO-SP-MIB", "cSpLinkMtp2T4N"),
        ("CISCO-SP-MIB", "cSpLinkMtp2T4E"),
        ("CISCO-SP-MIB", "cSpLinkMtp2T05"),
        ("CISCO-SP-MIB", "cSpLinkMtp2T06"),
        ("CISCO-SP-MIB", "cSpLinkMtp2T07"),
        ("CISCO-SP-MIB", "cSpLinkMtp2T08"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T01"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T02"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T03"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T04"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T05"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T06"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T07"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T08"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T10"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T11"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T12"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T13"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T14"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T15"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T16"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T17"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T18"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T19"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T20"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T21"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T22"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T23"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T24"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T25"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T26"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T27"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T28"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T29"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T30"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T31"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T32"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T33"),
        ("CISCO-SP-MIB", "cSpLinkMtp3T34"),
        ("CISCO-SP-MIB", "cSpLinkXmitQueueDepth"),
        ("CISCO-SP-MIB", "cSpLinkXmitQueueDepthHigh"),
        ("CISCO-SP-MIB", "cSpLinkXmitQueueDepthHighReset"),
        ("CISCO-SP-MIB", "cSpLinkCongestionState"),
        ("CISCO-SP-MIB", "cSpLinkCongestionAbate1"),
        ("CISCO-SP-MIB", "cSpLinkCongestionAbate2"),
        ("CISCO-SP-MIB", "cSpLinkCongestionAbate3"),
        ("CISCO-SP-MIB", "cSpLinkCongestionOnset1"),
        ("CISCO-SP-MIB", "cSpLinkCongestionOnset2"),
        ("CISCO-SP-MIB", "cSpLinkCongestionOnset3"),
        ("CISCO-SP-MIB", "cSpLinkSigLinkTest"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E1"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E2"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E3"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E4"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E5"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E6"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E7"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E8"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E9"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E10"),
        ("CISCO-SP-MIB", "cSpLinkQ752T1E11"),
        ("CISCO-SP-MIB", "cSpLinkQ752T2E1"),
        ("CISCO-SP-MIB", "cSpLinkQ752T2E5"),
        ("CISCO-SP-MIB", "cSpLinkQ752T2E6"),
        ("CISCO-SP-MIB", "cSpLinkQ752T2E7"),
        ("CISCO-SP-MIB", "cSpLinkQ752T2E9"),
        ("CISCO-SP-MIB", "cSpLinkQ752T2E10"),
        ("CISCO-SP-MIB", "cSpLinkQ752T2E15"),
        ("CISCO-SP-MIB", "cSpLinkQ752T2E16"),
        ("CISCO-SP-MIB", "cSpLinkQ752T2E18"),
        ("CISCO-SP-MIB", "cSpLinkMtp3PacketsRetrans"),
        ("CISCO-SP-MIB", "cSpLinkMtp3BytesRetrans"),
        ("CISCO-SP-MIB", "cSpLinkQ752T3E6"),
        ("CISCO-SP-MIB", "cSpLinkQ752T3E7"),
        ("CISCO-SP-MIB", "cSpLinkQ752T3E10L1"),
        ("CISCO-SP-MIB", "cSpLinkQ752T3E10L2"),
        ("CISCO-SP-MIB", "cSpLinkQ752T3E10L3"),
        ("CISCO-SP-MIB", "cSpLinkQ752T3E11L1"),
        ("CISCO-SP-MIB", "cSpLinkQ752T3E11L2"),
        ("CISCO-SP-MIB", "cSpLinkQ752T3E11L3"))
)
if mibBuilder.loadTexts:
    ciscoSpLinkGroup.setStatus("current")

ciscoSpRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 2, 4)
)
ciscoSpRouteGroup.setObjects(
    ("CISCO-SP-MIB", "cSpRouteStatus")
)
if mibBuilder.loadTexts:
    ciscoSpRouteGroup.setStatus("current")

ciscoSpAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 2, 5)
)
ciscoSpAccessListGroup.setObjects(
      *(("CISCO-SP-MIB", "cSpAclType"),
        ("CISCO-SP-MIB", "cSpAclDpc"),
        ("CISCO-SP-MIB", "cSpAclDpcMask"),
        ("CISCO-SP-MIB", "cSpAclOpc"),
        ("CISCO-SP-MIB", "cSpAclOpcMask"),
        ("CISCO-SP-MIB", "cSpAclSi"),
        ("CISCO-SP-MIB", "cSpAclPattern"),
        ("CISCO-SP-MIB", "cSpAclOffset"),
        ("CISCO-SP-MIB", "cSpAclAction"))
)
if mibBuilder.loadTexts:
    ciscoSpAccessListGroup.setStatus("current")

ciscoSpAccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 2, 6)
)
ciscoSpAccountingGroup.setObjects(
      *(("CISCO-SP-MIB", "cSpAccRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSentPackets"),
        ("CISCO-SP-MIB", "cSpAccRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSentBytes"),
        ("CISCO-SP-MIB", "cSpAccSnmmRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSnmmRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSnmmRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSnmmRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSnmmSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSnmmSentPackets"),
        ("CISCO-SP-MIB", "cSpAccSnmmSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSnmmSentBytes"),
        ("CISCO-SP-MIB", "cSpAccSntmRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSntmRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSntmRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSntmRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSntmSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSntmSentPackets"),
        ("CISCO-SP-MIB", "cSpAccSntmSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSntmSentBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare2RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare2RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare2RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare2RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare2SentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare2SentPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare2SentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare2SentBytes"),
        ("CISCO-SP-MIB", "cSpAccSccpRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSccpRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSccpRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSccpRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSccpSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSccpSentPackets"),
        ("CISCO-SP-MIB", "cSpAccSccpSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSccpSentBytes"),
        ("CISCO-SP-MIB", "cSpAccTupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCTupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccTupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCTupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccTupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCTupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccTupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCTupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccIsupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCIsupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccIsupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCIsupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccIsupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCIsupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccIsupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCIsupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccDupcRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCDupcRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccDupcRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCDupcRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccDupcSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCDupcSentPackets"),
        ("CISCO-SP-MIB", "cSpAccDupcSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCDupcSentBytes"),
        ("CISCO-SP-MIB", "cSpAccDupfRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCDupfRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccDupfRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCDupfRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccDupfSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCDupfSentPackets"),
        ("CISCO-SP-MIB", "cSpAccDupfSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCDupfSentBytes"),
        ("CISCO-SP-MIB", "cSpAccMtupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCMtupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccMtupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCMtupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccMtupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCMtupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccMtupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCMtupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccBisupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCBisupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccBisupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCBisupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccBisupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCBisupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccBisupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCBisupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccSisupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSisupRcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSisupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSisupRcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSisupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSisupSentPackets"),
        ("CISCO-SP-MIB", "cSpAccSisupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSisupSentBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare11RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare11RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare11RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare11RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare11SentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare11SentPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare11SentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare11SentBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare12RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare12RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare12RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare12RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare12SentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare12SentPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare12SentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare12SentBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare13RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare13RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare13RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare13RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare13SentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare13SentPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare13SentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare13SentBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare14RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare14RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare14RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare14RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare14SentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare14SentPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare14SentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare14SentBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare15RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare15RcvdPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare15RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare15RcvdBytes"),
        ("CISCO-SP-MIB", "cSpAccSpare15SentPackets"),
        ("CISCO-SP-MIB", "cSpAccHCSpare15SentPackets"),
        ("CISCO-SP-MIB", "cSpAccSpare15SentBytes"),
        ("CISCO-SP-MIB", "cSpAccHCSpare15SentBytes"))
)
if mibBuilder.loadTexts:
    ciscoSpAccountingGroup.setStatus("current")

ciscoSpNotificationsEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 2, 7)
)
ciscoSpNotificationsEnableGroup.setObjects(
      *(("CISCO-SP-MIB", "cSpLsStateChangeNotifEnabled"),
        ("CISCO-SP-MIB", "cSpLnkStateChangeNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoSpNotificationsEnableGroup.setStatus("current")


# Notification objects

ciscoSpLinksetStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 2, 0, 1)
)
ciscoSpLinksetStateChange.setObjects(
    ("CISCO-SP-MIB", "cSpLinksetState")
)
if mibBuilder.loadTexts:
    ciscoSpLinksetStateChange.setStatus(
        "current"
    )

ciscoSpLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 2, 0, 2)
)
ciscoSpLinkStateChange.setObjects(
    ("CISCO-SP-MIB", "cSpLinkState")
)
if mibBuilder.loadTexts:
    ciscoSpLinkStateChange.setStatus(
        "current"
    )


# Notifications groups

ciscoSpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 2, 8)
)
ciscoSpNotificationsGroup.setObjects(
      *(("CISCO-SP-MIB", "ciscoSpLinksetStateChange"),
        ("CISCO-SP-MIB", "ciscoSpLinkStateChange"))
)
if mibBuilder.loadTexts:
    ciscoSpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 73, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SP-MIB",
    **{"CSpPointCode": CSpPointCode,
       "CSpSs7Variant": CSpSs7Variant,
       "CSpLinkType": CSpLinkType,
       "CSpLinkSLC": CSpLinkSLC,
       "CSpLinksetId": CSpLinksetId,
       "CSpAclAction": CSpAclAction,
       "CSpOsiState": CSpOsiState,
       "CSpAclId": CSpAclId,
       "CSpRouteTableName": CSpRouteTableName,
       "CSpAclSi": CSpAclSi,
       "CSpRouteStatus": CSpRouteStatus,
       "ciscoSpMIB": ciscoSpMIB,
       "ciscoSpMIBObjects": ciscoSpMIBObjects,
       "cSpScalars": cSpScalars,
       "cSpSs7Variant": cSpSs7Variant,
       "cSpPointCode": cSpPointCode,
       "cSpMtp2T01": cSpMtp2T01,
       "cSpMtp2T02": cSpMtp2T02,
       "cSpMtp2T03": cSpMtp2T03,
       "cSpMtp2T4N": cSpMtp2T4N,
       "cSpMtp2T4E": cSpMtp2T4E,
       "cSpMtp2T05": cSpMtp2T05,
       "cSpMtp2T06": cSpMtp2T06,
       "cSpMtp2T07": cSpMtp2T07,
       "cSpMtp2T08": cSpMtp2T08,
       "cSpMtp3T01": cSpMtp3T01,
       "cSpMtp3T02": cSpMtp3T02,
       "cSpMtp3T03": cSpMtp3T03,
       "cSpMtp3T04": cSpMtp3T04,
       "cSpMtp3T05": cSpMtp3T05,
       "cSpMtp3T06": cSpMtp3T06,
       "cSpMtp3T07": cSpMtp3T07,
       "cSpMtp3T08": cSpMtp3T08,
       "cSpMtp3T10": cSpMtp3T10,
       "cSpMtp3T11": cSpMtp3T11,
       "cSpMtp3T12": cSpMtp3T12,
       "cSpMtp3T13": cSpMtp3T13,
       "cSpMtp3T14": cSpMtp3T14,
       "cSpMtp3T15": cSpMtp3T15,
       "cSpMtp3T16": cSpMtp3T16,
       "cSpMtp3T17": cSpMtp3T17,
       "cSpMtp3T18": cSpMtp3T18,
       "cSpMtp3T19": cSpMtp3T19,
       "cSpMtp3T20": cSpMtp3T20,
       "cSpMtp3T21": cSpMtp3T21,
       "cSpMtp3T22": cSpMtp3T22,
       "cSpMtp3T23": cSpMtp3T23,
       "cSpMtp3T24": cSpMtp3T24,
       "cSpMtp3T25": cSpMtp3T25,
       "cSpMtp3T26": cSpMtp3T26,
       "cSpMtp3T27": cSpMtp3T27,
       "cSpMtp3T28": cSpMtp3T28,
       "cSpMtp3T29": cSpMtp3T29,
       "cSpMtp3T30": cSpMtp3T30,
       "cSpMtp3T31": cSpMtp3T31,
       "cSpMtp3T32": cSpMtp3T32,
       "cSpMtp3T33": cSpMtp3T33,
       "cSpMtp3T34": cSpMtp3T34,
       "cSpLinkset": cSpLinkset,
       "cSpLinksetTable": cSpLinksetTable,
       "cSpLinksetTableEntry": cSpLinksetTableEntry,
       "cSpLinksetName": cSpLinksetName,
       "cSpLinksetAdjacentPointCode": cSpLinksetAdjacentPointCode,
       "cSpLinksetState": cSpLinksetState,
       "cSpLinksetInboundAcl": cSpLinksetInboundAcl,
       "cSpLinksetOutboundAcl": cSpLinksetOutboundAcl,
       "cSpLinksetSnmmRouteTableName": cSpLinksetSnmmRouteTableName,
       "cSpLinksetSntmRouteTableName": cSpLinksetSntmRouteTableName,
       "cSpLinksetSpare2RouteTableName": cSpLinksetSpare2RouteTableName,
       "cSpLinksetSccpRouteTableName": cSpLinksetSccpRouteTableName,
       "cSpLinksetTupRouteTableName": cSpLinksetTupRouteTableName,
       "cSpLinksetIsupRouteTableName": cSpLinksetIsupRouteTableName,
       "cSpLinksetDupcRouteTableName": cSpLinksetDupcRouteTableName,
       "cSpLinksetDupfRouteTableName": cSpLinksetDupfRouteTableName,
       "cSpLinksetMtupRouteTableName": cSpLinksetMtupRouteTableName,
       "cSpLinksetBisupRouteTableName": cSpLinksetBisupRouteTableName,
       "cSpLinksetSisupRouteTableName": cSpLinksetSisupRouteTableName,
       "cSpLinksetSpare11RouteTableName": cSpLinksetSpare11RouteTableName,
       "cSpLinksetSpare12RouteTableName": cSpLinksetSpare12RouteTableName,
       "cSpLinksetSpare13RouteTableName": cSpLinksetSpare13RouteTableName,
       "cSpLinksetSpare14RouteTableName": cSpLinksetSpare14RouteTableName,
       "cSpLinksetSpare15RouteTableName": cSpLinksetSpare15RouteTableName,
       "cSpLinksetAccountingEnabled": cSpLinksetAccountingEnabled,
       "cSpLinksetNumLinks": cSpLinksetNumLinks,
       "cSpLinksetPacketsSent": cSpLinksetPacketsSent,
       "cSpLinksetHCPacketsSent": cSpLinksetHCPacketsSent,
       "cSpLinksetPacketsRcvd": cSpLinksetPacketsRcvd,
       "cSpLinksetHCPacketsRcvd": cSpLinksetHCPacketsRcvd,
       "cSpLinksetBytesSent": cSpLinksetBytesSent,
       "cSpLinksetHCBytesSent": cSpLinksetHCBytesSent,
       "cSpLinksetBytesRcvd": cSpLinksetBytesRcvd,
       "cSpLinksetHCBytesRcvd": cSpLinksetHCBytesRcvd,
       "cSpLinksetDurationInService": cSpLinksetDurationInService,
       "cSpLinksetDurationOutService": cSpLinksetDurationOutService,
       "cSpLinksetMtp2T01": cSpLinksetMtp2T01,
       "cSpLinksetMtp2T02": cSpLinksetMtp2T02,
       "cSpLinksetMtp2T03": cSpLinksetMtp2T03,
       "cSpLinksetMtp2T4N": cSpLinksetMtp2T4N,
       "cSpLinksetMtp2T4E": cSpLinksetMtp2T4E,
       "cSpLinksetMtp2T05": cSpLinksetMtp2T05,
       "cSpLinksetMtp2T06": cSpLinksetMtp2T06,
       "cSpLinksetMtp2T07": cSpLinksetMtp2T07,
       "cSpLinksetMtp2T08": cSpLinksetMtp2T08,
       "cSpLinksetMtp3T01": cSpLinksetMtp3T01,
       "cSpLinksetMtp3T02": cSpLinksetMtp3T02,
       "cSpLinksetMtp3T03": cSpLinksetMtp3T03,
       "cSpLinksetMtp3T04": cSpLinksetMtp3T04,
       "cSpLinksetMtp3T05": cSpLinksetMtp3T05,
       "cSpLinksetMtp3T06": cSpLinksetMtp3T06,
       "cSpLinksetMtp3T07": cSpLinksetMtp3T07,
       "cSpLinksetMtp3T08": cSpLinksetMtp3T08,
       "cSpLinksetMtp3T10": cSpLinksetMtp3T10,
       "cSpLinksetMtp3T11": cSpLinksetMtp3T11,
       "cSpLinksetMtp3T12": cSpLinksetMtp3T12,
       "cSpLinksetMtp3T13": cSpLinksetMtp3T13,
       "cSpLinksetMtp3T14": cSpLinksetMtp3T14,
       "cSpLinksetMtp3T15": cSpLinksetMtp3T15,
       "cSpLinksetMtp3T16": cSpLinksetMtp3T16,
       "cSpLinksetMtp3T17": cSpLinksetMtp3T17,
       "cSpLinksetMtp3T18": cSpLinksetMtp3T18,
       "cSpLinksetMtp3T19": cSpLinksetMtp3T19,
       "cSpLinksetMtp3T20": cSpLinksetMtp3T20,
       "cSpLinksetMtp3T21": cSpLinksetMtp3T21,
       "cSpLinksetMtp3T22": cSpLinksetMtp3T22,
       "cSpLinksetMtp3T23": cSpLinksetMtp3T23,
       "cSpLinksetMtp3T24": cSpLinksetMtp3T24,
       "cSpLinksetMtp3T25": cSpLinksetMtp3T25,
       "cSpLinksetMtp3T26": cSpLinksetMtp3T26,
       "cSpLinksetMtp3T27": cSpLinksetMtp3T27,
       "cSpLinksetMtp3T28": cSpLinksetMtp3T28,
       "cSpLinksetMtp3T29": cSpLinksetMtp3T29,
       "cSpLinksetMtp3T30": cSpLinksetMtp3T30,
       "cSpLinksetMtp3T31": cSpLinksetMtp3T31,
       "cSpLinksetMtp3T32": cSpLinksetMtp3T32,
       "cSpLinksetMtp3T33": cSpLinksetMtp3T33,
       "cSpLinksetMtp3T34": cSpLinksetMtp3T34,
       "cSpLink": cSpLink,
       "cSpLinkTable": cSpLinkTable,
       "cSpLinkTableEntry": cSpLinkTableEntry,
       "cSpLinkSlc": cSpLinkSlc,
       "cSpLinkState": cSpLinkState,
       "cSpLinkType": cSpLinkType,
       "cSpLinkifIndex": cSpLinkifIndex,
       "cSpLinkSctpAssociation": cSpLinkSctpAssociation,
       "cSpLinkMtp3PacketsRcvd": cSpLinkMtp3PacketsRcvd,
       "cSpLinkMtp3PacketsSent": cSpLinkMtp3PacketsSent,
       "cSpLinkHCMtp3PacketsRcvd": cSpLinkHCMtp3PacketsRcvd,
       "cSpLinkHCMtp3PacketsSent": cSpLinkHCMtp3PacketsSent,
       "cSpLinkMtp3BytesRcvd": cSpLinkMtp3BytesRcvd,
       "cSpLinkMtp3BytesSent": cSpLinkMtp3BytesSent,
       "cSpLinkHCMtp3BytesRcvd": cSpLinkHCMtp3BytesRcvd,
       "cSpLinkHCMtp3BytesSent": cSpLinkHCMtp3BytesSent,
       "cSpLinkMtp2T01": cSpLinkMtp2T01,
       "cSpLinkMtp2T02": cSpLinkMtp2T02,
       "cSpLinkMtp2T03": cSpLinkMtp2T03,
       "cSpLinkMtp2T4N": cSpLinkMtp2T4N,
       "cSpLinkMtp2T4E": cSpLinkMtp2T4E,
       "cSpLinkMtp2T05": cSpLinkMtp2T05,
       "cSpLinkMtp2T06": cSpLinkMtp2T06,
       "cSpLinkMtp2T07": cSpLinkMtp2T07,
       "cSpLinkMtp2T08": cSpLinkMtp2T08,
       "cSpLinkMtp3T01": cSpLinkMtp3T01,
       "cSpLinkMtp3T02": cSpLinkMtp3T02,
       "cSpLinkMtp3T03": cSpLinkMtp3T03,
       "cSpLinkMtp3T04": cSpLinkMtp3T04,
       "cSpLinkMtp3T05": cSpLinkMtp3T05,
       "cSpLinkMtp3T06": cSpLinkMtp3T06,
       "cSpLinkMtp3T07": cSpLinkMtp3T07,
       "cSpLinkMtp3T08": cSpLinkMtp3T08,
       "cSpLinkMtp3T10": cSpLinkMtp3T10,
       "cSpLinkMtp3T11": cSpLinkMtp3T11,
       "cSpLinkMtp3T12": cSpLinkMtp3T12,
       "cSpLinkMtp3T13": cSpLinkMtp3T13,
       "cSpLinkMtp3T14": cSpLinkMtp3T14,
       "cSpLinkMtp3T15": cSpLinkMtp3T15,
       "cSpLinkMtp3T16": cSpLinkMtp3T16,
       "cSpLinkMtp3T17": cSpLinkMtp3T17,
       "cSpLinkMtp3T18": cSpLinkMtp3T18,
       "cSpLinkMtp3T19": cSpLinkMtp3T19,
       "cSpLinkMtp3T20": cSpLinkMtp3T20,
       "cSpLinkMtp3T21": cSpLinkMtp3T21,
       "cSpLinkMtp3T22": cSpLinkMtp3T22,
       "cSpLinkMtp3T23": cSpLinkMtp3T23,
       "cSpLinkMtp3T24": cSpLinkMtp3T24,
       "cSpLinkMtp3T25": cSpLinkMtp3T25,
       "cSpLinkMtp3T26": cSpLinkMtp3T26,
       "cSpLinkMtp3T27": cSpLinkMtp3T27,
       "cSpLinkMtp3T28": cSpLinkMtp3T28,
       "cSpLinkMtp3T29": cSpLinkMtp3T29,
       "cSpLinkMtp3T30": cSpLinkMtp3T30,
       "cSpLinkMtp3T31": cSpLinkMtp3T31,
       "cSpLinkMtp3T32": cSpLinkMtp3T32,
       "cSpLinkMtp3T33": cSpLinkMtp3T33,
       "cSpLinkMtp3T34": cSpLinkMtp3T34,
       "cSpLinkXmitQueueDepth": cSpLinkXmitQueueDepth,
       "cSpLinkXmitQueueDepthHigh": cSpLinkXmitQueueDepthHigh,
       "cSpLinkXmitQueueDepthHighReset": cSpLinkXmitQueueDepthHighReset,
       "cSpLinkCongestionState": cSpLinkCongestionState,
       "cSpLinkCongestionAbate1": cSpLinkCongestionAbate1,
       "cSpLinkCongestionAbate2": cSpLinkCongestionAbate2,
       "cSpLinkCongestionAbate3": cSpLinkCongestionAbate3,
       "cSpLinkCongestionOnset1": cSpLinkCongestionOnset1,
       "cSpLinkCongestionOnset2": cSpLinkCongestionOnset2,
       "cSpLinkCongestionOnset3": cSpLinkCongestionOnset3,
       "cSpLinkSigLinkTest": cSpLinkSigLinkTest,
       "cSpLinkQ752T1E1": cSpLinkQ752T1E1,
       "cSpLinkQ752T1E2": cSpLinkQ752T1E2,
       "cSpLinkQ752T1E3": cSpLinkQ752T1E3,
       "cSpLinkQ752T1E4": cSpLinkQ752T1E4,
       "cSpLinkQ752T1E5": cSpLinkQ752T1E5,
       "cSpLinkQ752T1E6": cSpLinkQ752T1E6,
       "cSpLinkQ752T1E7": cSpLinkQ752T1E7,
       "cSpLinkQ752T1E8": cSpLinkQ752T1E8,
       "cSpLinkQ752T1E9": cSpLinkQ752T1E9,
       "cSpLinkQ752T1E10": cSpLinkQ752T1E10,
       "cSpLinkQ752T1E11": cSpLinkQ752T1E11,
       "cSpLinkQ752T2E1": cSpLinkQ752T2E1,
       "cSpLinkQ752T2E5": cSpLinkQ752T2E5,
       "cSpLinkQ752T2E6": cSpLinkQ752T2E6,
       "cSpLinkQ752T2E7": cSpLinkQ752T2E7,
       "cSpLinkQ752T2E9": cSpLinkQ752T2E9,
       "cSpLinkQ752T2E10": cSpLinkQ752T2E10,
       "cSpLinkQ752T2E15": cSpLinkQ752T2E15,
       "cSpLinkQ752T2E16": cSpLinkQ752T2E16,
       "cSpLinkQ752T2E18": cSpLinkQ752T2E18,
       "cSpLinkMtp3PacketsRetrans": cSpLinkMtp3PacketsRetrans,
       "cSpLinkMtp3BytesRetrans": cSpLinkMtp3BytesRetrans,
       "cSpLinkQ752T3E6": cSpLinkQ752T3E6,
       "cSpLinkQ752T3E7": cSpLinkQ752T3E7,
       "cSpLinkQ752T3E10L1": cSpLinkQ752T3E10L1,
       "cSpLinkQ752T3E10L2": cSpLinkQ752T3E10L2,
       "cSpLinkQ752T3E10L3": cSpLinkQ752T3E10L3,
       "cSpLinkQ752T3E11L1": cSpLinkQ752T3E11L1,
       "cSpLinkQ752T3E11L2": cSpLinkQ752T3E11L2,
       "cSpLinkQ752T3E11L3": cSpLinkQ752T3E11L3,
       "cSpRoute": cSpRoute,
       "cSpRouteTable": cSpRouteTable,
       "cSpRouteTableEntry": cSpRouteTableEntry,
       "cSpRouteTableName": cSpRouteTableName,
       "cSpRouteDpc": cSpRouteDpc,
       "cSpRouteDestLsCost": cSpRouteDestLsCost,
       "cSpRouteDestLinkset": cSpRouteDestLinkset,
       "cSpRouteMask": cSpRouteMask,
       "cSpRouteStatus": cSpRouteStatus,
       "cSpAccessControlList": cSpAccessControlList,
       "cSpAclTable": cSpAclTable,
       "cSpAclTableEntry": cSpAclTableEntry,
       "cSpAclId": cSpAclId,
       "cSpAclEntryNumber": cSpAclEntryNumber,
       "cSpAclType": cSpAclType,
       "cSpAclDpc": cSpAclDpc,
       "cSpAclDpcMask": cSpAclDpcMask,
       "cSpAclOpc": cSpAclOpc,
       "cSpAclOpcMask": cSpAclOpcMask,
       "cSpAclSi": cSpAclSi,
       "cSpAclPattern": cSpAclPattern,
       "cSpAclOffset": cSpAclOffset,
       "cSpAclAction": cSpAclAction,
       "cSpAccounting": cSpAccounting,
       "cSpAccountingTable": cSpAccountingTable,
       "cSpAccountingTableEntry": cSpAccountingTableEntry,
       "cSpAccTableId": cSpAccTableId,
       "cSpAccDpc": cSpAccDpc,
       "cSpAccOpc": cSpAccOpc,
       "cSpAccRcvdPackets": cSpAccRcvdPackets,
       "cSpAccHCRcvdPackets": cSpAccHCRcvdPackets,
       "cSpAccSentPackets": cSpAccSentPackets,
       "cSpAccHCSentPackets": cSpAccHCSentPackets,
       "cSpAccRcvdBytes": cSpAccRcvdBytes,
       "cSpAccHCRcvdBytes": cSpAccHCRcvdBytes,
       "cSpAccSentBytes": cSpAccSentBytes,
       "cSpAccHCSentBytes": cSpAccHCSentBytes,
       "cSpAccSnmmRcvdPackets": cSpAccSnmmRcvdPackets,
       "cSpAccHCSnmmRcvdPackets": cSpAccHCSnmmRcvdPackets,
       "cSpAccSnmmRcvdBytes": cSpAccSnmmRcvdBytes,
       "cSpAccHCSnmmRcvdBytes": cSpAccHCSnmmRcvdBytes,
       "cSpAccSnmmSentPackets": cSpAccSnmmSentPackets,
       "cSpAccHCSnmmSentPackets": cSpAccHCSnmmSentPackets,
       "cSpAccSnmmSentBytes": cSpAccSnmmSentBytes,
       "cSpAccHCSnmmSentBytes": cSpAccHCSnmmSentBytes,
       "cSpAccSntmRcvdPackets": cSpAccSntmRcvdPackets,
       "cSpAccHCSntmRcvdPackets": cSpAccHCSntmRcvdPackets,
       "cSpAccSntmRcvdBytes": cSpAccSntmRcvdBytes,
       "cSpAccHCSntmRcvdBytes": cSpAccHCSntmRcvdBytes,
       "cSpAccSntmSentPackets": cSpAccSntmSentPackets,
       "cSpAccHCSntmSentPackets": cSpAccHCSntmSentPackets,
       "cSpAccSntmSentBytes": cSpAccSntmSentBytes,
       "cSpAccHCSntmSentBytes": cSpAccHCSntmSentBytes,
       "cSpAccSpare2RcvdPackets": cSpAccSpare2RcvdPackets,
       "cSpAccHCSpare2RcvdPackets": cSpAccHCSpare2RcvdPackets,
       "cSpAccSpare2RcvdBytes": cSpAccSpare2RcvdBytes,
       "cSpAccHCSpare2RcvdBytes": cSpAccHCSpare2RcvdBytes,
       "cSpAccSpare2SentPackets": cSpAccSpare2SentPackets,
       "cSpAccHCSpare2SentPackets": cSpAccHCSpare2SentPackets,
       "cSpAccSpare2SentBytes": cSpAccSpare2SentBytes,
       "cSpAccHCSpare2SentBytes": cSpAccHCSpare2SentBytes,
       "cSpAccSccpRcvdPackets": cSpAccSccpRcvdPackets,
       "cSpAccHCSccpRcvdPackets": cSpAccHCSccpRcvdPackets,
       "cSpAccSccpRcvdBytes": cSpAccSccpRcvdBytes,
       "cSpAccHCSccpRcvdBytes": cSpAccHCSccpRcvdBytes,
       "cSpAccSccpSentPackets": cSpAccSccpSentPackets,
       "cSpAccHCSccpSentPackets": cSpAccHCSccpSentPackets,
       "cSpAccSccpSentBytes": cSpAccSccpSentBytes,
       "cSpAccHCSccpSentBytes": cSpAccHCSccpSentBytes,
       "cSpAccTupRcvdPackets": cSpAccTupRcvdPackets,
       "cSpAccHCTupRcvdPackets": cSpAccHCTupRcvdPackets,
       "cSpAccTupRcvdBytes": cSpAccTupRcvdBytes,
       "cSpAccHCTupRcvdBytes": cSpAccHCTupRcvdBytes,
       "cSpAccTupSentPackets": cSpAccTupSentPackets,
       "cSpAccHCTupSentPackets": cSpAccHCTupSentPackets,
       "cSpAccTupSentBytes": cSpAccTupSentBytes,
       "cSpAccHCTupSentBytes": cSpAccHCTupSentBytes,
       "cSpAccIsupRcvdPackets": cSpAccIsupRcvdPackets,
       "cSpAccHCIsupRcvdPackets": cSpAccHCIsupRcvdPackets,
       "cSpAccIsupRcvdBytes": cSpAccIsupRcvdBytes,
       "cSpAccHCIsupRcvdBytes": cSpAccHCIsupRcvdBytes,
       "cSpAccIsupSentPackets": cSpAccIsupSentPackets,
       "cSpAccHCIsupSentPackets": cSpAccHCIsupSentPackets,
       "cSpAccIsupSentBytes": cSpAccIsupSentBytes,
       "cSpAccHCIsupSentBytes": cSpAccHCIsupSentBytes,
       "cSpAccDupcRcvdPackets": cSpAccDupcRcvdPackets,
       "cSpAccHCDupcRcvdPackets": cSpAccHCDupcRcvdPackets,
       "cSpAccDupcRcvdBytes": cSpAccDupcRcvdBytes,
       "cSpAccHCDupcRcvdBytes": cSpAccHCDupcRcvdBytes,
       "cSpAccDupcSentPackets": cSpAccDupcSentPackets,
       "cSpAccHCDupcSentPackets": cSpAccHCDupcSentPackets,
       "cSpAccDupcSentBytes": cSpAccDupcSentBytes,
       "cSpAccHCDupcSentBytes": cSpAccHCDupcSentBytes,
       "cSpAccDupfRcvdPackets": cSpAccDupfRcvdPackets,
       "cSpAccHCDupfRcvdPackets": cSpAccHCDupfRcvdPackets,
       "cSpAccDupfRcvdBytes": cSpAccDupfRcvdBytes,
       "cSpAccHCDupfRcvdBytes": cSpAccHCDupfRcvdBytes,
       "cSpAccDupfSentPackets": cSpAccDupfSentPackets,
       "cSpAccHCDupfSentPackets": cSpAccHCDupfSentPackets,
       "cSpAccDupfSentBytes": cSpAccDupfSentBytes,
       "cSpAccHCDupfSentBytes": cSpAccHCDupfSentBytes,
       "cSpAccMtupRcvdPackets": cSpAccMtupRcvdPackets,
       "cSpAccHCMtupRcvdPackets": cSpAccHCMtupRcvdPackets,
       "cSpAccMtupRcvdBytes": cSpAccMtupRcvdBytes,
       "cSpAccHCMtupRcvdBytes": cSpAccHCMtupRcvdBytes,
       "cSpAccMtupSentPackets": cSpAccMtupSentPackets,
       "cSpAccHCMtupSentPackets": cSpAccHCMtupSentPackets,
       "cSpAccMtupSentBytes": cSpAccMtupSentBytes,
       "cSpAccHCMtupSentBytes": cSpAccHCMtupSentBytes,
       "cSpAccBisupRcvdPackets": cSpAccBisupRcvdPackets,
       "cSpAccHCBisupRcvdPackets": cSpAccHCBisupRcvdPackets,
       "cSpAccBisupRcvdBytes": cSpAccBisupRcvdBytes,
       "cSpAccHCBisupRcvdBytes": cSpAccHCBisupRcvdBytes,
       "cSpAccBisupSentPackets": cSpAccBisupSentPackets,
       "cSpAccHCBisupSentPackets": cSpAccHCBisupSentPackets,
       "cSpAccBisupSentBytes": cSpAccBisupSentBytes,
       "cSpAccHCBisupSentBytes": cSpAccHCBisupSentBytes,
       "cSpAccSisupRcvdPackets": cSpAccSisupRcvdPackets,
       "cSpAccHCSisupRcvdPackets": cSpAccHCSisupRcvdPackets,
       "cSpAccSisupRcvdBytes": cSpAccSisupRcvdBytes,
       "cSpAccHCSisupRcvdBytes": cSpAccHCSisupRcvdBytes,
       "cSpAccSisupSentPackets": cSpAccSisupSentPackets,
       "cSpAccHCSisupSentPackets": cSpAccHCSisupSentPackets,
       "cSpAccSisupSentBytes": cSpAccSisupSentBytes,
       "cSpAccHCSisupSentBytes": cSpAccHCSisupSentBytes,
       "cSpAccSpare11RcvdPackets": cSpAccSpare11RcvdPackets,
       "cSpAccHCSpare11RcvdPackets": cSpAccHCSpare11RcvdPackets,
       "cSpAccSpare11RcvdBytes": cSpAccSpare11RcvdBytes,
       "cSpAccHCSpare11RcvdBytes": cSpAccHCSpare11RcvdBytes,
       "cSpAccSpare11SentPackets": cSpAccSpare11SentPackets,
       "cSpAccHCSpare11SentPackets": cSpAccHCSpare11SentPackets,
       "cSpAccSpare11SentBytes": cSpAccSpare11SentBytes,
       "cSpAccHCSpare11SentBytes": cSpAccHCSpare11SentBytes,
       "cSpAccSpare12RcvdPackets": cSpAccSpare12RcvdPackets,
       "cSpAccHCSpare12RcvdPackets": cSpAccHCSpare12RcvdPackets,
       "cSpAccSpare12RcvdBytes": cSpAccSpare12RcvdBytes,
       "cSpAccHCSpare12RcvdBytes": cSpAccHCSpare12RcvdBytes,
       "cSpAccSpare12SentPackets": cSpAccSpare12SentPackets,
       "cSpAccHCSpare12SentPackets": cSpAccHCSpare12SentPackets,
       "cSpAccSpare12SentBytes": cSpAccSpare12SentBytes,
       "cSpAccHCSpare12SentBytes": cSpAccHCSpare12SentBytes,
       "cSpAccSpare13RcvdPackets": cSpAccSpare13RcvdPackets,
       "cSpAccHCSpare13RcvdPackets": cSpAccHCSpare13RcvdPackets,
       "cSpAccSpare13RcvdBytes": cSpAccSpare13RcvdBytes,
       "cSpAccHCSpare13RcvdBytes": cSpAccHCSpare13RcvdBytes,
       "cSpAccSpare13SentPackets": cSpAccSpare13SentPackets,
       "cSpAccHCSpare13SentPackets": cSpAccHCSpare13SentPackets,
       "cSpAccSpare13SentBytes": cSpAccSpare13SentBytes,
       "cSpAccHCSpare13SentBytes": cSpAccHCSpare13SentBytes,
       "cSpAccSpare14RcvdPackets": cSpAccSpare14RcvdPackets,
       "cSpAccHCSpare14RcvdPackets": cSpAccHCSpare14RcvdPackets,
       "cSpAccSpare14RcvdBytes": cSpAccSpare14RcvdBytes,
       "cSpAccHCSpare14RcvdBytes": cSpAccHCSpare14RcvdBytes,
       "cSpAccSpare14SentPackets": cSpAccSpare14SentPackets,
       "cSpAccHCSpare14SentPackets": cSpAccHCSpare14SentPackets,
       "cSpAccSpare14SentBytes": cSpAccSpare14SentBytes,
       "cSpAccHCSpare14SentBytes": cSpAccHCSpare14SentBytes,
       "cSpAccSpare15RcvdPackets": cSpAccSpare15RcvdPackets,
       "cSpAccHCSpare15RcvdPackets": cSpAccHCSpare15RcvdPackets,
       "cSpAccSpare15RcvdBytes": cSpAccSpare15RcvdBytes,
       "cSpAccHCSpare15RcvdBytes": cSpAccHCSpare15RcvdBytes,
       "cSpAccSpare15SentPackets": cSpAccSpare15SentPackets,
       "cSpAccHCSpare15SentPackets": cSpAccHCSpare15SentPackets,
       "cSpAccSpare15SentBytes": cSpAccSpare15SentBytes,
       "cSpAccHCSpare15SentBytes": cSpAccHCSpare15SentBytes,
       "cSpNotificationsEnable": cSpNotificationsEnable,
       "cSpLsStateChangeNotifEnabled": cSpLsStateChangeNotifEnabled,
       "cSpLnkStateChangeNotifEnabled": cSpLnkStateChangeNotifEnabled,
       "ciscoSpMIBNotificationPrefix": ciscoSpMIBNotificationPrefix,
       "ciscoSpMIBNotifications": ciscoSpMIBNotifications,
       "ciscoSpLinksetStateChange": ciscoSpLinksetStateChange,
       "ciscoSpLinkStateChange": ciscoSpLinkStateChange,
       "ciscoSpMIBConformance": ciscoSpMIBConformance,
       "ciscoSpMIBCompliances": ciscoSpMIBCompliances,
       "ciscoSpMIBCompliance": ciscoSpMIBCompliance,
       "ciscoSpMIBGroups": ciscoSpMIBGroups,
       "ciscoSpSwitchGroup": ciscoSpSwitchGroup,
       "ciscoSpLinksetGroup": ciscoSpLinksetGroup,
       "ciscoSpLinkGroup": ciscoSpLinkGroup,
       "ciscoSpRouteGroup": ciscoSpRouteGroup,
       "ciscoSpAccessListGroup": ciscoSpAccessListGroup,
       "ciscoSpAccountingGroup": ciscoSpAccountingGroup,
       "ciscoSpNotificationsEnableGroup": ciscoSpNotificationsEnableGroup,
       "ciscoSpNotificationsGroup": ciscoSpNotificationsGroup}
)
