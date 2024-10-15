# SNMP MIB module (IANA-FINISHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IANA-FINISHER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:00 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ianafinisherMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 110)
)
ianafinisherMIB.setRevisions(
        ("2014-05-22 00:00",
         "2009-11-03 00:00",
         "2004-06-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FinDeviceTypeTC(Integer32, TextualConvention):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bander", 14),
          ("binder", 5),
          ("dieCutter", 7),
          ("folder", 4),
          ("imprinter", 12),
          ("inserter", 18),
          ("makeEnvelope", 15),
          ("other", 1),
          ("perforater", 9),
          ("puncher", 8),
          ("separationCutter", 11),
          ("sheetRotator", 17),
          ("slitter", 10),
          ("stacker", 16),
          ("stitcher", 3),
          ("trimmer", 6),
          ("unknown", 2),
          ("wrapper", 13))
    )



class FinAttributeTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              30,
              31,
              40,
              50,
              80,
              81,
              82,
              83,
              100,
              130,
              160,
              161,
              162)
        )
    )
    namedValues = NamedValues(
        *(("bindingType", 50),
          ("deviceModel", 5),
          ("deviceName", 3),
          ("deviceSerialNumber", 7),
          ("deviceVendorName", 4),
          ("deviceVersion", 6),
          ("finAxisOffset", 11),
          ("finHeadLocation", 13),
          ("finJogEdge", 12),
          ("finMediaTypeRestriction", 17),
          ("finNextFinishingOperation", 20),
          ("finNumberOfPositions", 15),
          ("finOperationRestrictions", 14),
          ("finPreviousFinishingOperation", 19),
          ("finPrinterInputTraySupported", 18),
          ("finProcessOffsetUnits", 9),
          ("finReferenceEdge", 10),
          ("foldingType", 40),
          ("maximumSheets", 8),
          ("namedConfiguration", 16),
          ("other", 1),
          ("punchHoleSizeLongDim", 81),
          ("punchHoleSizeShortDim", 82),
          ("punchHoleType", 80),
          ("punchPattern", 83),
          ("slittingType", 100),
          ("stackOffset", 161),
          ("stackOutputType", 160),
          ("stackRotation", 162),
          ("stitchingDirection", 31),
          ("stitchingType", 30),
          ("wrappingType", 130))
    )



class FinEdgeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bottomEdge", 4),
          ("leftEdge", 5),
          ("rightEdge", 6),
          ("topEdge", 3))
    )



class FinStitchingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("edgeStitch", 9),
          ("other", 1),
          ("saddleStitch", 8),
          ("stapleBottomLeft", 5),
          ("stapleBottomRight", 7),
          ("stapleDual", 10),
          ("stapleTopLeft", 4),
          ("stapleTopRight", 6),
          ("unknown", 2))
    )



class FinStitchingDirTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bottomUp", 4),
          ("topDown", 3),
          ("unknown", 2))
    )



class FinStitchingAngleTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 3),
          ("slanted", 5),
          ("unknown", 2),
          ("vertical", 4))
    )



class FinFoldingTypeTC(Integer32, TextualConvention):
    status = "current"
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
        *(("halfFold", 4),
          ("letterFold", 5),
          ("other", 1),
          ("unknown", 2),
          ("zFold", 3))
    )



class FinBindingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
        *(("adhesive", 9),
          ("comb", 10),
          ("other", 1),
          ("padding", 11),
          ("perfect", 7),
          ("plastic", 5),
          ("plasticMultiRing", 12),
          ("spiral", 8),
          ("tape", 4),
          ("unknown", 2),
          ("velo", 6))
    )



class FinPunchHoleTypeTC(Integer32, TextualConvention):
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
        *(("oblong", 4),
          ("other", 1),
          ("rectangular", 6),
          ("round", 3),
          ("square", 5),
          ("star", 7),
          ("unknown", 2))
    )



class FinPunchPatternTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("fiveHoleUS", 13),
          ("fourHoleDIN", 7),
          ("metric26Hole", 17),
          ("metric30Hole", 18),
          ("mixed7H4S", 15),
          ("nineteenHoleUS", 9),
          ("norweg6Hole", 16),
          ("other", 1),
          ("sevenHoleUS", 14),
          ("swedish4Hole", 11),
          ("threeHoleUS", 5),
          ("twentyTwoHoleUS", 8),
          ("twoHoleDIN", 6),
          ("twoHoleMetric", 10),
          ("twoHoleUSSide", 12),
          ("twoHoleUSTop", 4),
          ("unknown", 2))
    )



class FinSlittingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("slitAndMerge", 5),
          ("slitAndSeparate", 4),
          ("unknown", 2))
    )



class FinWrappingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("paperWrap", 5),
          ("shrinkWrap", 4),
          ("unknown", 2))
    )



class FinStackOutputTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("crissCross", 6),
          ("offset", 5),
          ("other", 1),
          ("straight", 4),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-FINISHER-MIB",
    **{"FinDeviceTypeTC": FinDeviceTypeTC,
       "FinAttributeTypeTC": FinAttributeTypeTC,
       "FinEdgeTC": FinEdgeTC,
       "FinStitchingTypeTC": FinStitchingTypeTC,
       "FinStitchingDirTypeTC": FinStitchingDirTypeTC,
       "FinStitchingAngleTypeTC": FinStitchingAngleTypeTC,
       "FinFoldingTypeTC": FinFoldingTypeTC,
       "FinBindingTypeTC": FinBindingTypeTC,
       "FinPunchHoleTypeTC": FinPunchHoleTypeTC,
       "FinPunchPatternTC": FinPunchPatternTC,
       "FinSlittingTypeTC": FinSlittingTypeTC,
       "FinWrappingTypeTC": FinWrappingTypeTC,
       "FinStackOutputTypeTC": FinStackOutputTypeTC,
       "ianafinisherMIB": ianafinisherMIB}
)
