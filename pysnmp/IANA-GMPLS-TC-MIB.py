# SNMP MIB module (IANA-GMPLS-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IANA-GMPLS-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:46 2024
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

ianaGmpls = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 152)
)
ianaGmpls.setRevisions(
        ("2015-11-04 00:00",
         "2015-09-22 00:00",
         "2014-05-09 00:00",
         "2014-03-11 00:00",
         "2013-12-16 00:00",
         "2013-11-04 00:00",
         "2013-10-14 00:00",
         "2013-10-10 00:00",
         "2013-10-09 00:00",
         "2010-04-13 00:00",
         "2010-02-22 00:00",
         "2010-02-19 00:00",
         "2007-02-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAGmplsLSPEncodingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              7,
              8,
              9,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("tunnelDigitalPath", 12),
          ("tunnelLine", 14),
          ("tunnelLspAnsiEtsiPdh", 3),
          ("tunnelLspDigitalWrapper", 7),
          ("tunnelLspEthernet", 2),
          ("tunnelLspFiber", 9),
          ("tunnelLspFiberChannel", 11),
          ("tunnelLspLambda", 8),
          ("tunnelLspNotGmpls", 0),
          ("tunnelLspPacket", 1),
          ("tunnelLspSdhSonet", 5),
          ("tunnelOpticalChannel", 13))
    )



class IANAGmplsSwitchingTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              30,
              40,
              51,
              100,
              110,
              125,
              150,
              151,
              200)
        )
    )
    namedValues = NamedValues(
        *(("dcsc", 125),
          ("evpl", 30),
          ("fsc", 200),
          ("l2sc", 51),
          ("lsc", 150),
          ("otntdm", 110),
          ("pbb", 40),
          ("psc1", 1),
          ("psc2", 2),
          ("psc3", 3),
          ("psc4", 4),
          ("tdm", 100),
          ("unknown", 0),
          ("wsonlsc", 151))
    )



class IANAGmplsGeneralizedPidTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              36,
              37,
              38,
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
              70)
        )
    )
    namedValues = NamedValues(
        *(("ansiEtsiPdh", 38),
          ("asynchDS1T1", 16),
          ("asynchDS2T2", 10),
          ("asynchDS3T3", 6),
          ("asynchE1", 13),
          ("asynchE3", 7),
          ("asynchE4", 5),
          ("atm", 32),
          ("bitsynchDS1T1", 17),
          ("bitsynchDS2T2", 11),
          ("bitsynchE3", 8),
          ("bytesynch31ByDS0", 15),
          ("bytesynchDS1T1", 18),
          ("bytesynchE1", 14),
          ("bytesynchE3", 9),
          ("dVBASI", 65),
          ("digitalwrapper", 36),
          ("dqdb", 42),
          ("ds1ESFAsynch", 23),
          ("ds1SFAsynch", 22),
          ("ds3CBitParityAsynch", 25),
          ("ds3M23Asynch", 24),
          ("ethernet", 33),
          ("ethernet802dot3Only", 46),
          ("ethernetV2DixOnly", 45),
          ("fddi", 41),
          ("fiberChannel3", 43),
          ("framedGFP", 59),
          ("g709BSNT", 52),
          ("g709BSOT", 51),
          ("g709CBRb", 50),
          ("g709CBRorCBRa", 49),
          ("g709ESCON", 56),
          ("g709FICON", 57),
          ("g709FiberChannel", 58),
          ("g709ODU125G", 66),
          ("g709ODUAny", 67),
          ("g709ODUj", 47),
          ("g709OTUk", 48),
          ("gfpEthernetMAC", 54),
          ("gfpEthernetPHY", 55),
          ("gfpIPorPPP", 53),
          ("hdlc", 44),
          ("infiniBand", 62),
          ("lambda", 37),
          ("lapsSdh", 40),
          ("nullTest", 68),
          ("posNoScramble16BitCrc", 28),
          ("posNoScramble32BitCrc", 29),
          ("posScramble16BitCrc", 30),
          ("posScramble32BitCrc", 31),
          ("randomTest", 69),
          ("reservedByRFC3471first", 12),
          ("reservedByRFC3471second", 20),
          ("reservedByRFC3471third", 21),
          ("sDI", 63),
          ("sDI1point001", 64),
          ("sTM1", 60),
          ("sTM4", 61),
          ("sdhSonet", 34),
          ("sixtyfourB66BGFPFEthernet", 70),
          ("stsSpeHovc", 27),
          ("unknown", 0),
          ("vc1vc12", 19),
          ("vtLovc", 26))
    )



class IANAGmplsAdminStatusInformationTC(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-GMPLS-TC-MIB",
    **{"IANAGmplsLSPEncodingTypeTC": IANAGmplsLSPEncodingTypeTC,
       "IANAGmplsSwitchingTypeTC": IANAGmplsSwitchingTypeTC,
       "IANAGmplsGeneralizedPidTC": IANAGmplsGeneralizedPidTC,
       "IANAGmplsAdminStatusInformationTC": IANAGmplsAdminStatusInformationTC,
       "ianaGmpls": ianaGmpls}
)
