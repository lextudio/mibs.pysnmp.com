# SNMP MIB module (ADSL2-LINE-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADSL2-LINE-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:00 2024
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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

adsl2TCMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 2)
)
adsl2TCMIB.setRevisions(
        ("2006-10-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Adsl2Unit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atuc", 1),
          ("atur", 2))
    )



class Adsl2Direction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )



class Adsl2TransmissionModeType(Bits, TextualConvention):
    status = "current"


class Adsl2RaMode(Integer32, TextualConvention):
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
        *(("dynamicRa", 3),
          ("manual", 1),
          ("raInit", 2))
    )



class Adsl2InitResult(Integer32, TextualConvention):
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
        *(("commFail", 3),
          ("configError", 1),
          ("configNotFeasible", 2),
          ("noFail", 0),
          ("noPeerAtu", 4),
          ("otherCause", 5))
    )



class Adsl2OperationModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              9,
              10,
              11,
              14,
              15,
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
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("adsl", 2),
          ("defMode", 1),
          ("g9923AnnexIAllDigNonOverlapped", 18),
          ("g9923AnnexIAllDigOverlapped", 19),
          ("g9923AnnexJAllDigNonOverlapped", 20),
          ("g9923AnnexJAllDigOverlapped", 21),
          ("g9923AnnexLMode1NonOverlapped", 24),
          ("g9923AnnexLMode2NonOverlapped", 25),
          ("g9923AnnexLMode3Overlapped", 26),
          ("g9923AnnexLMode4Overlapped", 27),
          ("g9923AnnexMPotsNonOverlapped", 28),
          ("g9923AnnexMPotsOverlapped", 29),
          ("g9923IsdnNonOverlapped", 10),
          ("g9923PotsNonOverlapped", 8),
          ("g9923PotsOverlapped", 9),
          ("g9923isdnOverlapped", 11),
          ("g9924AnnexIAllDigNonOverlapped", 22),
          ("g9924AnnexIAllDigOverlapped", 23),
          ("g9924potsNonOverlapped", 14),
          ("g9924potsOverlapped", 15),
          ("g9925AnnexIAllDigNonOverlapped", 36),
          ("g9925AnnexIAllDigOverlapped", 37),
          ("g9925AnnexJAllDigNonOverlapped", 38),
          ("g9925AnnexJAllDigOverlapped", 39),
          ("g9925AnnexMPotsNonOverlapped", 40),
          ("g9925AnnexMPotsOverlapped", 41),
          ("g9925IsdnNonOverlapped", 32),
          ("g9925PotsNonOverlapped", 30),
          ("g9925PotsOverlapped", 31),
          ("g9925isdnOverlapped", 33))
    )



class Adsl2PowerMngState(Integer32, TextualConvention):
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
        *(("l0", 1),
          ("l1", 2),
          ("l2", 3),
          ("l3", 4))
    )



class Adsl2ConfPmsForce(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l0orL2toL3", 3),
          ("l0toL2", 2),
          ("l3toL0", 0))
    )



class Adsl2LConfProfPmMode(Bits, TextualConvention):
    status = "current"


class Adsl2LineLdsf(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("inhibit", 0))
    )



class Adsl2LdsfResult(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 6),
          ("adminUp", 9),
          ("cannotRun", 5),
          ("failed", 7),
          ("illegalMode", 8),
          ("inProgress", 3),
          ("noResources", 11),
          ("none", 1),
          ("success", 2),
          ("tableFull", 10),
          ("unsupported", 4))
    )



class Adsl2SymbolProtection(Integer32, TextualConvention):
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
        *(("eightSymbols", 10),
          ("elevenSymbols", 13),
          ("fifteenSymbols", 17),
          ("fiveSymbols", 7),
          ("fourSymbols", 6),
          ("fourteenSymbols", 16),
          ("halfSymbol", 2),
          ("nineSymbols", 11),
          ("noProtection", 1),
          ("sevenSymbols", 9),
          ("singleSymbol", 3),
          ("sixSymbols", 8),
          ("sixteenSymbols", 18),
          ("tenSymbols", 12),
          ("thirteeSymbols", 15),
          ("threeSymbols", 5),
          ("twelveSymbols", 14),
          ("twoSymbols", 4))
    )



class Adsl2MaxBer(Integer32, TextualConvention):
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
        *(("eminus3", 1),
          ("eminus5", 2),
          ("eminus7", 3))
    )



class Adsl2ScMaskDs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class Adsl2ScMaskUs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class Adsl2RfiDs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class Adsl2PsdMaskDs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )



class Adsl2PsdMaskUs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class Adsl2Tssi(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )



class Adsl2LastTransmittedState(Integer32, TextualConvention):
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
              131)
        )
    )
    namedValues = NamedValues(
        *(("atucComb1", 2),
          ("atucComb2", 4),
          ("atucComb3", 8),
          ("atucEct", 16),
          ("atucExchmarker", 25),
          ("atucG9941", 0),
          ("atucIComb2", 9),
          ("atucIcomb1", 5),
          ("atucLineprob", 6),
          ("atucMedley", 24),
          ("atucMsg1", 21),
          ("atucMsg2", 26),
          ("atucMsgfmt", 10),
          ("atucMsgpcb", 11),
          ("atucParams", 29),
          ("atucQuiet1", 1),
          ("atucQuiet2", 3),
          ("atucQuiet3", 7),
          ("atucQuiet4", 12),
          ("atucReverb1", 13),
          ("atucReverb2", 15),
          ("atucReverb3", 17),
          ("atucReverb4", 19),
          ("atucReverb5", 22),
          ("atucReverb6", 27),
          ("atucReverb7", 30),
          ("atucSegue1", 20),
          ("atucSegue2", 23),
          ("atucSegue3", 28),
          ("atucSegue4", 31),
          ("atucShowtime", 32),
          ("atucTref1", 14),
          ("atucTref2", 18),
          ("aturComb1", 102),
          ("aturComb2", 104),
          ("aturComb3", 108),
          ("aturEct", 117),
          ("aturExchmarker", 124),
          ("aturG9941", 100),
          ("aturIcomb1", 105),
          ("aturIcomb2", 109),
          ("aturLineprob", 106),
          ("aturMedley", 123),
          ("aturMsg1", 122),
          ("aturMsg2", 125),
          ("aturMsgfmt", 110),
          ("aturMsgpcb", 111),
          ("aturParams", 128),
          ("aturQuiet1", 101),
          ("aturQuiet2", 103),
          ("aturQuiet3", 107),
          ("aturQuiet4", 113),
          ("aturQuiet5", 115),
          ("aturReverb1", 112),
          ("aturReverb2", 114),
          ("aturReverb3", 116),
          ("aturReverb4", 118),
          ("aturReverb5", 120),
          ("aturReverb6", 126),
          ("aturReverb7", 129),
          ("aturSegue1", 119),
          ("aturSegue2", 121),
          ("aturSegue3", 127),
          ("aturSegue4", 130),
          ("aturShowtime", 131))
    )



class Adsl2LineStatus(Bits, TextualConvention):
    status = "current"


class Adsl2ChAtmStatus(Bits, TextualConvention):
    status = "current"


class Adsl2ChPtmStatus(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADSL2-LINE-TC-MIB",
    **{"Adsl2Unit": Adsl2Unit,
       "Adsl2Direction": Adsl2Direction,
       "Adsl2TransmissionModeType": Adsl2TransmissionModeType,
       "Adsl2RaMode": Adsl2RaMode,
       "Adsl2InitResult": Adsl2InitResult,
       "Adsl2OperationModes": Adsl2OperationModes,
       "Adsl2PowerMngState": Adsl2PowerMngState,
       "Adsl2ConfPmsForce": Adsl2ConfPmsForce,
       "Adsl2LConfProfPmMode": Adsl2LConfProfPmMode,
       "Adsl2LineLdsf": Adsl2LineLdsf,
       "Adsl2LdsfResult": Adsl2LdsfResult,
       "Adsl2SymbolProtection": Adsl2SymbolProtection,
       "Adsl2MaxBer": Adsl2MaxBer,
       "Adsl2ScMaskDs": Adsl2ScMaskDs,
       "Adsl2ScMaskUs": Adsl2ScMaskUs,
       "Adsl2RfiDs": Adsl2RfiDs,
       "Adsl2PsdMaskDs": Adsl2PsdMaskDs,
       "Adsl2PsdMaskUs": Adsl2PsdMaskUs,
       "Adsl2Tssi": Adsl2Tssi,
       "Adsl2LastTransmittedState": Adsl2LastTransmittedState,
       "Adsl2LineStatus": Adsl2LineStatus,
       "Adsl2ChAtmStatus": Adsl2ChAtmStatus,
       "Adsl2ChPtmStatus": Adsl2ChPtmStatus,
       "adsl2TCMIB": adsl2TCMIB}
)
