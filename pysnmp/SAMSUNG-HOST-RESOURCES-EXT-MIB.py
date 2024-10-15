# SNMP MIB module (SAMSUNG-HOST-RESOURCES-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAMSUNG-HOST-RESOURCES-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:39 2024
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(samsungCommonMIB,) = mibBuilder.importSymbols(
    "SAMSUNG-COMMON-MIB",
    "samsungCommonMIB")

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

scmHrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScmHrDevCountJobTypeTC(Integer32, TextualConvention):
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
              11,
              12,
              21)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("digitalRecieve", 12),
          ("digitalSend", 11),
          ("faxIn", 3),
          ("faxOut", 4),
          ("localStorage", 21),
          ("print", 1),
          ("report", 6),
          ("scan", 5))
    )



class ScmHrDevCountMediaSizeTC(Integer32, TextualConvention):
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
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("a3", 20),
          ("a3Over", 31),
          ("a4", 5),
          ("a4P", 26),
          ("a5", 16),
          ("a5P", 28),
          ("a6", 18),
          ("b5Envelope", 32),
          ("c5", 12),
          ("c6", 14),
          ("com10", 9),
          ("custom", 24),
          ("dl", 11),
          ("executive", 6),
          ("executiveP", 29),
          ("folio", 15),
          ("isoB5", 8),
          ("jisB4", 21),
          ("jisB5", 7),
          ("jisB5P", 27),
          ("jpost", 22),
          ("jpostd", 23),
          ("large", 2),
          ("ledger", 19),
          ("legal", 4),
          ("letter", 3),
          ("letterP", 25),
          ("monarch", 10),
          ("postA6", 13),
          ("small", 1),
          ("statement", 17),
          ("statementP", 30))
    )



class ScmHrDevCountUnitTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("feet", 16),
          ("hours", 11),
          ("hundrethsOfFluidOunces", 14),
          ("impressions", 7),
          ("items", 18),
          ("meters", 17),
          ("micrometers", 4),
          ("other", 1),
          ("percent", 19),
          ("sheets", 8),
          ("tenThousandthsOfInches", 3),
          ("tenthsOfGrams", 13),
          ("tenthsOfMilliliters", 15),
          ("thousandthsOfOunces", 12),
          ("unknown", 2))
    )



class ScmHrDevCountDuplexTC(Integer32, TextualConvention):
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
        *(("duplex", 2),
          ("duplexSingle", 3),
          ("simplex", 1))
    )



class ScmHrDevCountColorTC(Integer32, TextualConvention):
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
        *(("fullColor", 1),
          ("monoColor", 3),
          ("singleColor", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ScmHrMIBConformance_ObjectIdentity = ObjectIdentity
scmHrMIBConformance = _ScmHrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2)
)
_ScmHrMIBGroups_ObjectIdentity = ObjectIdentity
scmHrMIBGroups = _ScmHrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2, 2)
)
_ScmHrDevCount_ObjectIdentity = ObjectIdentity
scmHrDevCount = _ScmHrDevCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11)
)
_ScmHrDevCountSimple_ObjectIdentity = ObjectIdentity
scmHrDevCountSimple = _ScmHrDevCountSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 1)
)
_ScmHrDevCountTable_Object = MibTable
scmHrDevCountTable = _ScmHrDevCountTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2)
)
if mibBuilder.loadTexts:
    scmHrDevCountTable.setStatus("current")
_ScmHrDevCountEntry_Object = MibTableRow
scmHrDevCountEntry = _ScmHrDevCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1)
)
scmHrDevCountEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountIndex"),
)
if mibBuilder.loadTexts:
    scmHrDevCountEntry.setStatus("current")


class _ScmHrDevCountIndex_Type(Integer32):
    """Custom type scmHrDevCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_ScmHrDevCountIndex_Type.__name__ = "Integer32"
_ScmHrDevCountIndex_Object = MibTableColumn
scmHrDevCountIndex = _ScmHrDevCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 1),
    _ScmHrDevCountIndex_Type()
)
scmHrDevCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountIndex.setStatus("current")
_ScmHrDevCountJobType_Type = ScmHrDevCountJobTypeTC
_ScmHrDevCountJobType_Object = MibTableColumn
scmHrDevCountJobType = _ScmHrDevCountJobType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 2),
    _ScmHrDevCountJobType_Type()
)
scmHrDevCountJobType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountJobType.setStatus("current")
_ScmHrDevCountMediaSize_Type = ScmHrDevCountMediaSizeTC
_ScmHrDevCountMediaSize_Object = MibTableColumn
scmHrDevCountMediaSize = _ScmHrDevCountMediaSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 3),
    _ScmHrDevCountMediaSize_Type()
)
scmHrDevCountMediaSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountMediaSize.setStatus("current")
_ScmHrDevCountUnit_Type = ScmHrDevCountUnitTC
_ScmHrDevCountUnit_Object = MibTableColumn
scmHrDevCountUnit = _ScmHrDevCountUnit_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 4),
    _ScmHrDevCountUnit_Type()
)
scmHrDevCountUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountUnit.setStatus("current")
_ScmHrDevCountDuplex_Type = ScmHrDevCountDuplexTC
_ScmHrDevCountDuplex_Object = MibTableColumn
scmHrDevCountDuplex = _ScmHrDevCountDuplex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 5),
    _ScmHrDevCountDuplex_Type()
)
scmHrDevCountDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountDuplex.setStatus("current")
_ScmHrDevCountColor_Type = ScmHrDevCountColorTC
_ScmHrDevCountColor_Object = MibTableColumn
scmHrDevCountColor = _ScmHrDevCountColor_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 6),
    _ScmHrDevCountColor_Type()
)
scmHrDevCountColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountColor.setStatus("current")
_ScmHrDevCountValue_Type = Counter32
_ScmHrDevCountValue_Object = MibTableColumn
scmHrDevCountValue = _ScmHrDevCountValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 7),
    _ScmHrDevCountValue_Type()
)
scmHrDevCountValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountValue.setStatus("current")

# Managed Objects groups

scmHrDevInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2, 2, 3)
)
scmHrDevInfoGroup.setObjects(
      *(("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountIndex"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountJobType"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountMediaSize"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountUnit"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountDuplex"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountColor"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountValue"))
)
if mibBuilder.loadTexts:
    scmHrDevInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMSUNG-HOST-RESOURCES-EXT-MIB",
    **{"ScmHrDevCountJobTypeTC": ScmHrDevCountJobTypeTC,
       "ScmHrDevCountMediaSizeTC": ScmHrDevCountMediaSizeTC,
       "ScmHrDevCountUnitTC": ScmHrDevCountUnitTC,
       "ScmHrDevCountDuplexTC": ScmHrDevCountDuplexTC,
       "ScmHrDevCountColorTC": ScmHrDevCountColorTC,
       "scmHrMIB": scmHrMIB,
       "scmHrMIBConformance": scmHrMIBConformance,
       "scmHrMIBGroups": scmHrMIBGroups,
       "scmHrDevInfoGroup": scmHrDevInfoGroup,
       "scmHrDevCount": scmHrDevCount,
       "scmHrDevCountSimple": scmHrDevCountSimple,
       "scmHrDevCountTable": scmHrDevCountTable,
       "scmHrDevCountEntry": scmHrDevCountEntry,
       "scmHrDevCountIndex": scmHrDevCountIndex,
       "scmHrDevCountJobType": scmHrDevCountJobType,
       "scmHrDevCountMediaSize": scmHrDevCountMediaSize,
       "scmHrDevCountUnit": scmHrDevCountUnit,
       "scmHrDevCountDuplex": scmHrDevCountDuplex,
       "scmHrDevCountColor": scmHrDevCountColor,
       "scmHrDevCountValue": scmHrDevCountValue}
)
