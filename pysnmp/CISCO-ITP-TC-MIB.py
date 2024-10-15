# SNMP MIB module (CISCO-ITP-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:13 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoItpTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 231)
)
ciscoItpTextualConventions.setRevisions(
        ("2004-04-26 00:00",
         "2003-08-03 00:00",
         "2003-01-29 00:00",
         "2001-12-11 00:00",
         "2001-10-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CItpTcAclId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2700, 2999),
    )



class CItpTcCLLI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )



class CItpTcDisplayPC(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )



class CItpTcEncodingSchemeValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class CItpTcGlobalTitleSelector(Integer32, TextualConvention):
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
        *(("nai", 1),
          ("tt", 2),
          ("ttNpEs", 3),
          ("ttNpNaiEs", 4))
    )



class CItpTcGlobalTitleSelectorName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )



class CItpTcGtaAddr(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class CItpTcGtaLongAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CItpTcGtaDisplay(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )



class CItpTcGtaDisplayZB(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )



class CItpTcGtaLongDisplay(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CItpTcGtaDisplayLen(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class CItpTcGtaLongDisplayLen(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class CItpTcNetworkName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )



class CItpTcInstanceNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpTcLinksetId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )



class CItpTcLinkSLC(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class CItpTcLinkType(Integer32, TextualConvention):
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
        *(("hsl", 4),
          ("other", 1),
          ("sctpIp", 3),
          ("serial", 2),
          ("virtual", 5))
    )



class CItpTcNAI(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpTcNetworkIndicator(Integer32, TextualConvention):
    status = "current"
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
        *(("international", 0),
          ("internationatSpare", 1),
          ("national", 2),
          ("nationalSpare", 3))
    )



class CItpTcNumberingPlan(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpTcPointCode(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )



class CItpTcPointCodeMask(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )



class CItpTcPointCodeType(Integer32, TextualConvention):
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
        *(("additional", 2),
          ("capability", 3),
          ("primary", 1),
          ("xua", 4))
    )



class CItpTcQos(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )



class CItpTcRouteTableName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )



class CItpTcServiceIndicator(Integer32, TextualConvention):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("bisup", 9),
          ("dupc", 6),
          ("dupf", 7),
          ("isup", 5),
          ("mtup", 8),
          ("sccp", 3),
          ("sisup", 10),
          ("snmm", 0),
          ("sntm", 1),
          ("spare11", 11),
          ("spare12", 12),
          ("spare13", 13),
          ("spare14", 14),
          ("spare15", 15),
          ("spare2", 2),
          ("tup", 4))
    )



class CItpTcSls(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpTcSs7Variant(Integer32, TextualConvention):
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
        *(("ansi", 1),
          ("china", 3),
          ("itu", 2))
    )



class CItpTcSubSystemNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 255),
    )



class CItpTcSubSystemNumberMask(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )



class CItpTcTableLoadStatus(Integer32, TextualConvention):
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
        *(("loadComplete", 3),
          ("loadCompleteWithErrors", 4),
          ("loadFailed", 5),
          ("loadInProgress", 2),
          ("loadNotRequested", 1))
    )



class CItpTcTimerMtp2T01(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 150000),
    )



class CItpTcTimerMtp2T02(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 150000),
    )



class CItpTcTimerMtp2T03(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 14000),
    )



class CItpTcTimerMtp2T04E(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(400, 660),
    )



class CItpTcTimerMtp2T04N(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2007, 9500),
    )



class CItpTcTimerMtp2T05(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(80, 120),
    )



class CItpTcTimerMtp2T06(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 6000),
    )



class CItpTcTimerMtp2T07(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 6000),
    )



class CItpTcTimerMtp3T01(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T02(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 2000),
    )



class CItpTcTimerMtp3T03(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T04(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T05(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T06(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )



class CItpTcTimerMtp3T07(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 2000),
    )



class CItpTcTimerMtp3T08(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1200),
    )



class CItpTcTimerMtp3T10(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 60000),
    )



class CItpTcTimerMtp3T11(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 90000),
    )



class CItpTcTimerMtp3T12(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1500),
    )



class CItpTcTimerMtp3T13(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1500),
    )



class CItpTcTimerMtp3T14(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3000),
    )



class CItpTcTimerMtp3T15(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3000),
    )



class CItpTcTimerMtp3T16(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400, 2000),
    )



class CItpTcTimerMtp3T17(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1500),
    )



class CItpTcTimerMtp3T18(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 31000),
    )



class CItpTcTimerMtp3T19(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(67000, 600000),
    )



class CItpTcTimerMtp3T20(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 120000),
    )



class CItpTcTimerMtp3T21(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(63000, 120000),
    )



class CItpTcTimerMtp3T22(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36000, 360000),
    )



class CItpTcTimerMtp3T23(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9000, 360000),
    )



class CItpTcTimerMtp3T24(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )



class CItpTcTimerMtp3T25(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30000, 35000),
    )



class CItpTcTimerMtp3T26(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(12000, 15000),
    )



class CItpTcTimerMtp3T27(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 50000),
    )



class CItpTcTimerMtp3T28(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3000, 35000),
    )



class CItpTcTimerMtp3T29(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60000, 65000),
    )



class CItpTcTimerMtp3T30(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30000, 35000),
    )



class CItpTcTimerMtp3T31(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10000, 120000),
    )



class CItpTcTimerMtp3T32(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 120000),
    )



class CItpTcTimerMtp3T33(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60000, 600000),
    )



class CItpTcTimerMtp3T34(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 120000),
    )



class CItpTcTimerLinkTest(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 12000),
    )



class CItpTcTimerLinkMessage(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30000, 90000),
    )



class CItpTcTimerLinkActRetry(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60000, 90000),
    )



class CItpTcTranslationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssn", 2),
          ("tt", 1))
    )



class CItpTcURL(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CItpTcXuaName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-TC-MIB",
    **{"CItpTcAclId": CItpTcAclId,
       "CItpTcCLLI": CItpTcCLLI,
       "CItpTcDisplayPC": CItpTcDisplayPC,
       "CItpTcEncodingSchemeValue": CItpTcEncodingSchemeValue,
       "CItpTcGlobalTitleSelector": CItpTcGlobalTitleSelector,
       "CItpTcGlobalTitleSelectorName": CItpTcGlobalTitleSelectorName,
       "CItpTcGtaAddr": CItpTcGtaAddr,
       "CItpTcGtaLongAddr": CItpTcGtaLongAddr,
       "CItpTcGtaDisplay": CItpTcGtaDisplay,
       "CItpTcGtaDisplayZB": CItpTcGtaDisplayZB,
       "CItpTcGtaLongDisplay": CItpTcGtaLongDisplay,
       "CItpTcGtaDisplayLen": CItpTcGtaDisplayLen,
       "CItpTcGtaLongDisplayLen": CItpTcGtaLongDisplayLen,
       "CItpTcNetworkName": CItpTcNetworkName,
       "CItpTcInstanceNumber": CItpTcInstanceNumber,
       "CItpTcLinksetId": CItpTcLinksetId,
       "CItpTcLinkSLC": CItpTcLinkSLC,
       "CItpTcLinkType": CItpTcLinkType,
       "CItpTcNAI": CItpTcNAI,
       "CItpTcNetworkIndicator": CItpTcNetworkIndicator,
       "CItpTcNumberingPlan": CItpTcNumberingPlan,
       "CItpTcPointCode": CItpTcPointCode,
       "CItpTcPointCodeMask": CItpTcPointCodeMask,
       "CItpTcPointCodeType": CItpTcPointCodeType,
       "CItpTcQos": CItpTcQos,
       "CItpTcRouteTableName": CItpTcRouteTableName,
       "CItpTcServiceIndicator": CItpTcServiceIndicator,
       "CItpTcSls": CItpTcSls,
       "CItpTcSs7Variant": CItpTcSs7Variant,
       "CItpTcSubSystemNumber": CItpTcSubSystemNumber,
       "CItpTcSubSystemNumberMask": CItpTcSubSystemNumberMask,
       "CItpTcTableLoadStatus": CItpTcTableLoadStatus,
       "CItpTcTimerMtp2T01": CItpTcTimerMtp2T01,
       "CItpTcTimerMtp2T02": CItpTcTimerMtp2T02,
       "CItpTcTimerMtp2T03": CItpTcTimerMtp2T03,
       "CItpTcTimerMtp2T04E": CItpTcTimerMtp2T04E,
       "CItpTcTimerMtp2T04N": CItpTcTimerMtp2T04N,
       "CItpTcTimerMtp2T05": CItpTcTimerMtp2T05,
       "CItpTcTimerMtp2T06": CItpTcTimerMtp2T06,
       "CItpTcTimerMtp2T07": CItpTcTimerMtp2T07,
       "CItpTcTimerMtp3T01": CItpTcTimerMtp3T01,
       "CItpTcTimerMtp3T02": CItpTcTimerMtp3T02,
       "CItpTcTimerMtp3T03": CItpTcTimerMtp3T03,
       "CItpTcTimerMtp3T04": CItpTcTimerMtp3T04,
       "CItpTcTimerMtp3T05": CItpTcTimerMtp3T05,
       "CItpTcTimerMtp3T06": CItpTcTimerMtp3T06,
       "CItpTcTimerMtp3T07": CItpTcTimerMtp3T07,
       "CItpTcTimerMtp3T08": CItpTcTimerMtp3T08,
       "CItpTcTimerMtp3T10": CItpTcTimerMtp3T10,
       "CItpTcTimerMtp3T11": CItpTcTimerMtp3T11,
       "CItpTcTimerMtp3T12": CItpTcTimerMtp3T12,
       "CItpTcTimerMtp3T13": CItpTcTimerMtp3T13,
       "CItpTcTimerMtp3T14": CItpTcTimerMtp3T14,
       "CItpTcTimerMtp3T15": CItpTcTimerMtp3T15,
       "CItpTcTimerMtp3T16": CItpTcTimerMtp3T16,
       "CItpTcTimerMtp3T17": CItpTcTimerMtp3T17,
       "CItpTcTimerMtp3T18": CItpTcTimerMtp3T18,
       "CItpTcTimerMtp3T19": CItpTcTimerMtp3T19,
       "CItpTcTimerMtp3T20": CItpTcTimerMtp3T20,
       "CItpTcTimerMtp3T21": CItpTcTimerMtp3T21,
       "CItpTcTimerMtp3T22": CItpTcTimerMtp3T22,
       "CItpTcTimerMtp3T23": CItpTcTimerMtp3T23,
       "CItpTcTimerMtp3T24": CItpTcTimerMtp3T24,
       "CItpTcTimerMtp3T25": CItpTcTimerMtp3T25,
       "CItpTcTimerMtp3T26": CItpTcTimerMtp3T26,
       "CItpTcTimerMtp3T27": CItpTcTimerMtp3T27,
       "CItpTcTimerMtp3T28": CItpTcTimerMtp3T28,
       "CItpTcTimerMtp3T29": CItpTcTimerMtp3T29,
       "CItpTcTimerMtp3T30": CItpTcTimerMtp3T30,
       "CItpTcTimerMtp3T31": CItpTcTimerMtp3T31,
       "CItpTcTimerMtp3T32": CItpTcTimerMtp3T32,
       "CItpTcTimerMtp3T33": CItpTcTimerMtp3T33,
       "CItpTcTimerMtp3T34": CItpTcTimerMtp3T34,
       "CItpTcTimerLinkTest": CItpTcTimerLinkTest,
       "CItpTcTimerLinkMessage": CItpTcTimerLinkMessage,
       "CItpTcTimerLinkActRetry": CItpTcTimerLinkActRetry,
       "CItpTcTranslationType": CItpTcTranslationType,
       "CItpTcURL": CItpTcURL,
       "CItpTcXuaName": CItpTcXuaName,
       "ciscoItpTextualConventions": ciscoItpTextualConventions}
)
