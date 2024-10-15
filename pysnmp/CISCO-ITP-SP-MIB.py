# SNMP MIB module (CISCO-ITP-SP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-SP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:34 2024
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

(CItpTcAclId,
 CItpTcCLLI,
 CItpTcDisplayPC,
 CItpTcLinkSLC,
 CItpTcLinkType,
 CItpTcLinksetId,
 CItpTcNetworkIndicator,
 CItpTcPointCode,
 CItpTcPointCodeType,
 CItpTcQos,
 CItpTcRouteTableName,
 CItpTcSs7Variant,
 CItpTcTimerLinkActRetry,
 CItpTcTimerLinkMessage,
 CItpTcTimerLinkTest,
 CItpTcTimerMtp2T01,
 CItpTcTimerMtp2T02,
 CItpTcTimerMtp2T03,
 CItpTcTimerMtp2T04E,
 CItpTcTimerMtp2T04N,
 CItpTcTimerMtp2T05,
 CItpTcTimerMtp2T06,
 CItpTcTimerMtp2T07,
 CItpTcTimerMtp3T01,
 CItpTcTimerMtp3T02,
 CItpTcTimerMtp3T03,
 CItpTcTimerMtp3T04,
 CItpTcTimerMtp3T05,
 CItpTcTimerMtp3T06,
 CItpTcTimerMtp3T07,
 CItpTcTimerMtp3T08,
 CItpTcTimerMtp3T10,
 CItpTcTimerMtp3T11,
 CItpTcTimerMtp3T12,
 CItpTcTimerMtp3T13,
 CItpTcTimerMtp3T14,
 CItpTcTimerMtp3T15,
 CItpTcTimerMtp3T16,
 CItpTcTimerMtp3T17,
 CItpTcTimerMtp3T18,
 CItpTcTimerMtp3T19,
 CItpTcTimerMtp3T20,
 CItpTcTimerMtp3T21,
 CItpTcTimerMtp3T22,
 CItpTcTimerMtp3T23,
 CItpTcTimerMtp3T24,
 CItpTcTimerMtp3T25,
 CItpTcTimerMtp3T26,
 CItpTcTimerMtp3T27,
 CItpTcTimerMtp3T28,
 CItpTcTimerMtp3T29,
 CItpTcTimerMtp3T30,
 CItpTcTimerMtp3T31,
 CItpTcTimerMtp3T32,
 CItpTcTimerMtp3T33,
 CItpTcTimerMtp3T34) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcAclId",
    "CItpTcCLLI",
    "CItpTcDisplayPC",
    "CItpTcLinkSLC",
    "CItpTcLinkType",
    "CItpTcLinksetId",
    "CItpTcNetworkIndicator",
    "CItpTcPointCode",
    "CItpTcPointCodeType",
    "CItpTcQos",
    "CItpTcRouteTableName",
    "CItpTcSs7Variant",
    "CItpTcTimerLinkActRetry",
    "CItpTcTimerLinkMessage",
    "CItpTcTimerLinkTest",
    "CItpTcTimerMtp2T01",
    "CItpTcTimerMtp2T02",
    "CItpTcTimerMtp2T03",
    "CItpTcTimerMtp2T04E",
    "CItpTcTimerMtp2T04N",
    "CItpTcTimerMtp2T05",
    "CItpTcTimerMtp2T06",
    "CItpTcTimerMtp2T07",
    "CItpTcTimerMtp3T01",
    "CItpTcTimerMtp3T02",
    "CItpTcTimerMtp3T03",
    "CItpTcTimerMtp3T04",
    "CItpTcTimerMtp3T05",
    "CItpTcTimerMtp3T06",
    "CItpTcTimerMtp3T07",
    "CItpTcTimerMtp3T08",
    "CItpTcTimerMtp3T10",
    "CItpTcTimerMtp3T11",
    "CItpTcTimerMtp3T12",
    "CItpTcTimerMtp3T13",
    "CItpTcTimerMtp3T14",
    "CItpTcTimerMtp3T15",
    "CItpTcTimerMtp3T16",
    "CItpTcTimerMtp3T17",
    "CItpTcTimerMtp3T18",
    "CItpTcTimerMtp3T19",
    "CItpTcTimerMtp3T20",
    "CItpTcTimerMtp3T21",
    "CItpTcTimerMtp3T22",
    "CItpTcTimerMtp3T23",
    "CItpTcTimerMtp3T24",
    "CItpTcTimerMtp3T25",
    "CItpTcTimerMtp3T26",
    "CItpTcTimerMtp3T27",
    "CItpTcTimerMtp3T28",
    "CItpTcTimerMtp3T29",
    "CItpTcTimerMtp3T30",
    "CItpTcTimerMtp3T31",
    "CItpTcTimerMtp3T32",
    "CItpTcTimerMtp3T33",
    "CItpTcTimerMtp3T34")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoItpSpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232)
)
ciscoItpSpMIB.setRevisions(
        ("2003-02-18 00:00",
         "2002-03-07 00:00",
         "2002-01-23 00:00",
         "2001-08-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CItpSpSequenceNumber(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CItpSpSampleInterval(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )



class CItpSpPercentThreshold(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class CItpSpLinkUtilization(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )



class CItpSpLinkCapacity(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(56000, 2147483647),
    )



class CItpSpLinkUtilizationState(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overThreshold", 2),
          ("unMonitored", 0),
          ("underThreshold", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CItpSpMIBNotifs_ObjectIdentity = ObjectIdentity
cItpSpMIBNotifs = _CItpSpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 0)
)
_CItpSpNotifications_ObjectIdentity = ObjectIdentity
cItpSpNotifications = _CItpSpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 0, 0)
)
_CItpSpMIBObjects_ObjectIdentity = ObjectIdentity
cItpSpMIBObjects = _CItpSpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1)
)
_CItpSpScalars_ObjectIdentity = ObjectIdentity
cItpSpScalars = _CItpSpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1)
)
_CItpSpVariant_Type = CItpTcSs7Variant
_CItpSpVariant_Object = MibScalar
cItpSpVariant = _CItpSpVariant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 1),
    _CItpSpVariant_Type()
)
cItpSpVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpVariant.setStatus("deprecated")
_CItpSpCLLICode_Type = CItpTcCLLI
_CItpSpCLLICode_Object = MibScalar
cItpSpCLLICode = _CItpSpCLLICode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 2),
    _CItpSpCLLICode_Type()
)
cItpSpCLLICode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpCLLICode.setStatus("deprecated")


class _CItpSpDisplayName_Type(SnmpAdminString):
    """Custom type cItpSpDisplayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CItpSpDisplayName_Type.__name__ = "SnmpAdminString"
_CItpSpDisplayName_Object = MibScalar
cItpSpDisplayName = _CItpSpDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 3),
    _CItpSpDisplayName_Type()
)
cItpSpDisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpDisplayName.setStatus("deprecated")


class _CItpSpDescription_Type(SnmpAdminString):
    """Custom type cItpSpDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CItpSpDescription_Type.__name__ = "SnmpAdminString"
_CItpSpDescription_Object = MibScalar
cItpSpDescription = _CItpSpDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 4),
    _CItpSpDescription_Type()
)
cItpSpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpDescription.setStatus("deprecated")
_CItpSpMtp2T01_Type = CItpTcTimerMtp2T01
_CItpSpMtp2T01_Object = MibScalar
cItpSpMtp2T01 = _CItpSpMtp2T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 5),
    _CItpSpMtp2T01_Type()
)
cItpSpMtp2T01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp2T01.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp2T01.setUnits("milliseconds")
_CItpSpMtp2T02_Type = CItpTcTimerMtp2T02
_CItpSpMtp2T02_Object = MibScalar
cItpSpMtp2T02 = _CItpSpMtp2T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 6),
    _CItpSpMtp2T02_Type()
)
cItpSpMtp2T02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp2T02.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp2T02.setUnits("milliseconds")
_CItpSpMtp2T03_Type = CItpTcTimerMtp2T03
_CItpSpMtp2T03_Object = MibScalar
cItpSpMtp2T03 = _CItpSpMtp2T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 7),
    _CItpSpMtp2T03_Type()
)
cItpSpMtp2T03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp2T03.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp2T03.setUnits("milliseconds")
_CItpSpMtp2T04E_Type = CItpTcTimerMtp2T04E
_CItpSpMtp2T04E_Object = MibScalar
cItpSpMtp2T04E = _CItpSpMtp2T04E_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 8),
    _CItpSpMtp2T04E_Type()
)
cItpSpMtp2T04E.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp2T04E.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp2T04E.setUnits("milliseconds")
_CItpSpMtp2T04N_Type = CItpTcTimerMtp2T04N
_CItpSpMtp2T04N_Object = MibScalar
cItpSpMtp2T04N = _CItpSpMtp2T04N_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 9),
    _CItpSpMtp2T04N_Type()
)
cItpSpMtp2T04N.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp2T04N.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp2T04N.setUnits("milliseconds")
_CItpSpMtp2T05_Type = CItpTcTimerMtp2T05
_CItpSpMtp2T05_Object = MibScalar
cItpSpMtp2T05 = _CItpSpMtp2T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 10),
    _CItpSpMtp2T05_Type()
)
cItpSpMtp2T05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp2T05.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp2T05.setUnits("milliseconds")
_CItpSpMtp2T06_Type = CItpTcTimerMtp2T06
_CItpSpMtp2T06_Object = MibScalar
cItpSpMtp2T06 = _CItpSpMtp2T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 11),
    _CItpSpMtp2T06_Type()
)
cItpSpMtp2T06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp2T06.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp2T06.setUnits("milliseconds")
_CItpSpMtp2T07_Type = CItpTcTimerMtp2T07
_CItpSpMtp2T07_Object = MibScalar
cItpSpMtp2T07 = _CItpSpMtp2T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 12),
    _CItpSpMtp2T07_Type()
)
cItpSpMtp2T07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp2T07.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp2T07.setUnits("milliseconds")
_CItpSpMtp3T01_Type = CItpTcTimerMtp3T01
_CItpSpMtp3T01_Object = MibScalar
cItpSpMtp3T01 = _CItpSpMtp3T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 13),
    _CItpSpMtp3T01_Type()
)
cItpSpMtp3T01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T01.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T01.setUnits("milliseconds")
_CItpSpMtp3T02_Type = CItpTcTimerMtp3T02
_CItpSpMtp3T02_Object = MibScalar
cItpSpMtp3T02 = _CItpSpMtp3T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 14),
    _CItpSpMtp3T02_Type()
)
cItpSpMtp3T02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T02.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T02.setUnits("milliseconds")
_CItpSpMtp3T03_Type = CItpTcTimerMtp3T03
_CItpSpMtp3T03_Object = MibScalar
cItpSpMtp3T03 = _CItpSpMtp3T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 15),
    _CItpSpMtp3T03_Type()
)
cItpSpMtp3T03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T03.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T03.setUnits("milliseconds")
_CItpSpMtp3T04_Type = CItpTcTimerMtp3T04
_CItpSpMtp3T04_Object = MibScalar
cItpSpMtp3T04 = _CItpSpMtp3T04_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 16),
    _CItpSpMtp3T04_Type()
)
cItpSpMtp3T04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T04.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T04.setUnits("milliseconds")
_CItpSpMtp3T05_Type = CItpTcTimerMtp3T05
_CItpSpMtp3T05_Object = MibScalar
cItpSpMtp3T05 = _CItpSpMtp3T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 17),
    _CItpSpMtp3T05_Type()
)
cItpSpMtp3T05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T05.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T05.setUnits("milliseconds")
_CItpSpMtp3T06_Type = CItpTcTimerMtp3T06
_CItpSpMtp3T06_Object = MibScalar
cItpSpMtp3T06 = _CItpSpMtp3T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 18),
    _CItpSpMtp3T06_Type()
)
cItpSpMtp3T06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T06.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T06.setUnits("milliseconds")
_CItpSpMtp3T07_Type = CItpTcTimerMtp3T07
_CItpSpMtp3T07_Object = MibScalar
cItpSpMtp3T07 = _CItpSpMtp3T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 19),
    _CItpSpMtp3T07_Type()
)
cItpSpMtp3T07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T07.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T07.setUnits("milliseconds")
_CItpSpMtp3T08_Type = CItpTcTimerMtp3T08
_CItpSpMtp3T08_Object = MibScalar
cItpSpMtp3T08 = _CItpSpMtp3T08_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 20),
    _CItpSpMtp3T08_Type()
)
cItpSpMtp3T08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T08.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T08.setUnits("milliseconds")
_CItpSpMtp3T10_Type = CItpTcTimerMtp3T10
_CItpSpMtp3T10_Object = MibScalar
cItpSpMtp3T10 = _CItpSpMtp3T10_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 21),
    _CItpSpMtp3T10_Type()
)
cItpSpMtp3T10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T10.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T10.setUnits("milliseconds")
_CItpSpMtp3T11_Type = CItpTcTimerMtp3T11
_CItpSpMtp3T11_Object = MibScalar
cItpSpMtp3T11 = _CItpSpMtp3T11_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 22),
    _CItpSpMtp3T11_Type()
)
cItpSpMtp3T11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T11.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T11.setUnits("milliseconds")
_CItpSpMtp3T12_Type = CItpTcTimerMtp3T12
_CItpSpMtp3T12_Object = MibScalar
cItpSpMtp3T12 = _CItpSpMtp3T12_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 23),
    _CItpSpMtp3T12_Type()
)
cItpSpMtp3T12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T12.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T12.setUnits("milliseconds")
_CItpSpMtp3T13_Type = CItpTcTimerMtp3T13
_CItpSpMtp3T13_Object = MibScalar
cItpSpMtp3T13 = _CItpSpMtp3T13_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 24),
    _CItpSpMtp3T13_Type()
)
cItpSpMtp3T13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T13.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T13.setUnits("milliseconds")
_CItpSpMtp3T14_Type = CItpTcTimerMtp3T14
_CItpSpMtp3T14_Object = MibScalar
cItpSpMtp3T14 = _CItpSpMtp3T14_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 25),
    _CItpSpMtp3T14_Type()
)
cItpSpMtp3T14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T14.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T14.setUnits("milliseconds")
_CItpSpMtp3T15_Type = CItpTcTimerMtp3T15
_CItpSpMtp3T15_Object = MibScalar
cItpSpMtp3T15 = _CItpSpMtp3T15_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 26),
    _CItpSpMtp3T15_Type()
)
cItpSpMtp3T15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T15.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T15.setUnits("milliseconds")
_CItpSpMtp3T16_Type = CItpTcTimerMtp3T16
_CItpSpMtp3T16_Object = MibScalar
cItpSpMtp3T16 = _CItpSpMtp3T16_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 27),
    _CItpSpMtp3T16_Type()
)
cItpSpMtp3T16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T16.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T16.setUnits("milliseconds")
_CItpSpMtp3T17_Type = CItpTcTimerMtp3T17
_CItpSpMtp3T17_Object = MibScalar
cItpSpMtp3T17 = _CItpSpMtp3T17_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 28),
    _CItpSpMtp3T17_Type()
)
cItpSpMtp3T17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T17.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T17.setUnits("milliseconds")
_CItpSpMtp3T18_Type = CItpTcTimerMtp3T18
_CItpSpMtp3T18_Object = MibScalar
cItpSpMtp3T18 = _CItpSpMtp3T18_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 29),
    _CItpSpMtp3T18_Type()
)
cItpSpMtp3T18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T18.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T18.setUnits("milliseconds")
_CItpSpMtp3T19_Type = CItpTcTimerMtp3T19
_CItpSpMtp3T19_Object = MibScalar
cItpSpMtp3T19 = _CItpSpMtp3T19_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 30),
    _CItpSpMtp3T19_Type()
)
cItpSpMtp3T19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T19.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T19.setUnits("milliseconds")
_CItpSpMtp3T20_Type = CItpTcTimerMtp3T20
_CItpSpMtp3T20_Object = MibScalar
cItpSpMtp3T20 = _CItpSpMtp3T20_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 31),
    _CItpSpMtp3T20_Type()
)
cItpSpMtp3T20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T20.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T20.setUnits("milliseconds")
_CItpSpMtp3T21_Type = CItpTcTimerMtp3T21
_CItpSpMtp3T21_Object = MibScalar
cItpSpMtp3T21 = _CItpSpMtp3T21_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 32),
    _CItpSpMtp3T21_Type()
)
cItpSpMtp3T21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T21.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T21.setUnits("milliseconds")
_CItpSpMtp3T22_Type = CItpTcTimerMtp3T22
_CItpSpMtp3T22_Object = MibScalar
cItpSpMtp3T22 = _CItpSpMtp3T22_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 33),
    _CItpSpMtp3T22_Type()
)
cItpSpMtp3T22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T22.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T22.setUnits("milliseconds")
_CItpSpMtp3T23_Type = CItpTcTimerMtp3T23
_CItpSpMtp3T23_Object = MibScalar
cItpSpMtp3T23 = _CItpSpMtp3T23_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 34),
    _CItpSpMtp3T23_Type()
)
cItpSpMtp3T23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T23.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T23.setUnits("milliseconds")
_CItpSpMtp3T24_Type = CItpTcTimerMtp3T24
_CItpSpMtp3T24_Object = MibScalar
cItpSpMtp3T24 = _CItpSpMtp3T24_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 35),
    _CItpSpMtp3T24_Type()
)
cItpSpMtp3T24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T24.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T24.setUnits("milliseconds")
_CItpSpMtp3T25_Type = CItpTcTimerMtp3T25
_CItpSpMtp3T25_Object = MibScalar
cItpSpMtp3T25 = _CItpSpMtp3T25_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 36),
    _CItpSpMtp3T25_Type()
)
cItpSpMtp3T25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T25.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T25.setUnits("milliseconds")
_CItpSpMtp3T26_Type = CItpTcTimerMtp3T26
_CItpSpMtp3T26_Object = MibScalar
cItpSpMtp3T26 = _CItpSpMtp3T26_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 37),
    _CItpSpMtp3T26_Type()
)
cItpSpMtp3T26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T26.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T26.setUnits("milliseconds")
_CItpSpMtp3T27_Type = CItpTcTimerMtp3T27
_CItpSpMtp3T27_Object = MibScalar
cItpSpMtp3T27 = _CItpSpMtp3T27_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 38),
    _CItpSpMtp3T27_Type()
)
cItpSpMtp3T27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T27.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T27.setUnits("milliseconds")
_CItpSpMtp3T28_Type = CItpTcTimerMtp3T28
_CItpSpMtp3T28_Object = MibScalar
cItpSpMtp3T28 = _CItpSpMtp3T28_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 39),
    _CItpSpMtp3T28_Type()
)
cItpSpMtp3T28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T28.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T28.setUnits("milliseconds")
_CItpSpMtp3T29_Type = CItpTcTimerMtp3T29
_CItpSpMtp3T29_Object = MibScalar
cItpSpMtp3T29 = _CItpSpMtp3T29_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 40),
    _CItpSpMtp3T29_Type()
)
cItpSpMtp3T29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T29.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T29.setUnits("milliseconds")
_CItpSpMtp3T30_Type = CItpTcTimerMtp3T30
_CItpSpMtp3T30_Object = MibScalar
cItpSpMtp3T30 = _CItpSpMtp3T30_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 41),
    _CItpSpMtp3T30_Type()
)
cItpSpMtp3T30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T30.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T30.setUnits("milliseconds")
_CItpSpMtp3T31_Type = CItpTcTimerMtp3T31
_CItpSpMtp3T31_Object = MibScalar
cItpSpMtp3T31 = _CItpSpMtp3T31_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 42),
    _CItpSpMtp3T31_Type()
)
cItpSpMtp3T31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T31.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T31.setUnits("milliseconds")
_CItpSpMtp3T32_Type = CItpTcTimerMtp3T32
_CItpSpMtp3T32_Object = MibScalar
cItpSpMtp3T32 = _CItpSpMtp3T32_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 43),
    _CItpSpMtp3T32_Type()
)
cItpSpMtp3T32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T32.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T32.setUnits("milliseconds")
_CItpSpMtp3T33_Type = CItpTcTimerMtp3T33
_CItpSpMtp3T33_Object = MibScalar
cItpSpMtp3T33 = _CItpSpMtp3T33_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 44),
    _CItpSpMtp3T33_Type()
)
cItpSpMtp3T33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T33.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T33.setUnits("milliseconds")
_CItpSpMtp3T34_Type = CItpTcTimerMtp3T34
_CItpSpMtp3T34_Object = MibScalar
cItpSpMtp3T34 = _CItpSpMtp3T34_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 45),
    _CItpSpMtp3T34_Type()
)
cItpSpMtp3T34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpMtp3T34.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpMtp3T34.setUnits("milliseconds")
_CItpSpTimerLinkTest_Type = CItpTcTimerLinkTest
_CItpSpTimerLinkTest_Object = MibScalar
cItpSpTimerLinkTest = _CItpSpTimerLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 46),
    _CItpSpTimerLinkTest_Type()
)
cItpSpTimerLinkTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpTimerLinkTest.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpTimerLinkTest.setUnits("milliseconds")
_CItpSpTimerLinkMessage_Type = CItpTcTimerLinkMessage
_CItpSpTimerLinkMessage_Object = MibScalar
cItpSpTimerLinkMessage = _CItpSpTimerLinkMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 47),
    _CItpSpTimerLinkMessage_Type()
)
cItpSpTimerLinkMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpTimerLinkMessage.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpTimerLinkMessage.setUnits("milliseconds")
_CItpSpTimerLinkActRetry_Type = CItpTcTimerLinkActRetry
_CItpSpTimerLinkActRetry_Object = MibScalar
cItpSpTimerLinkActRetry = _CItpSpTimerLinkActRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 48),
    _CItpSpTimerLinkActRetry_Type()
)
cItpSpTimerLinkActRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpTimerLinkActRetry.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpTimerLinkActRetry.setUnits("milliseconds")


class _CItpSpTFR_Type(TruthValue):
    """Custom type cItpSpTFR based on TruthValue"""


_CItpSpTFR_Object = MibScalar
cItpSpTFR = _CItpSpTFR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 49),
    _CItpSpTFR_Type()
)
cItpSpTFR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpTFR.setStatus("deprecated")


class _CItpSpCongestionsLevels_Type(TruthValue):
    """Custom type cItpSpCongestionsLevels based on TruthValue"""


_CItpSpCongestionsLevels_Object = MibScalar
cItpSpCongestionsLevels = _CItpSpCongestionsLevels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 50),
    _CItpSpCongestionsLevels_Type()
)
cItpSpCongestionsLevels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpCongestionsLevels.setStatus("deprecated")


class _CItpSpFastRestart_Type(TruthValue):
    """Custom type cItpSpFastRestart based on TruthValue"""


_CItpSpFastRestart_Object = MibScalar
cItpSpFastRestart = _CItpSpFastRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 51),
    _CItpSpFastRestart_Type()
)
cItpSpFastRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpFastRestart.setStatus("deprecated")


class _CItpSpDistSccpUnseq_Type(TruthValue):
    """Custom type cItpSpDistSccpUnseq based on TruthValue"""


_CItpSpDistSccpUnseq_Object = MibScalar
cItpSpDistSccpUnseq = _CItpSpDistSccpUnseq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 52),
    _CItpSpDistSccpUnseq_Type()
)
cItpSpDistSccpUnseq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpDistSccpUnseq.setStatus("deprecated")


class _CItpSpSummaryRoutingException_Type(TruthValue):
    """Custom type cItpSpSummaryRoutingException based on TruthValue"""


_CItpSpSummaryRoutingException_Object = MibScalar
cItpSpSummaryRoutingException = _CItpSpSummaryRoutingException_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 53),
    _CItpSpSummaryRoutingException_Type()
)
cItpSpSummaryRoutingException.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpSummaryRoutingException.setStatus("deprecated")


class _CItpSpUtilSampleInterval_Type(CItpSpSampleInterval):
    """Custom type cItpSpUtilSampleInterval based on CItpSpSampleInterval"""
    defaultValue = 300


_CItpSpUtilSampleInterval_Object = MibScalar
cItpSpUtilSampleInterval = _CItpSpUtilSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 54),
    _CItpSpUtilSampleInterval_Type()
)
cItpSpUtilSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpUtilSampleInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpUtilSampleInterval.setUnits("seconds")


class _CItpSpUtilThreshold_Type(CItpSpPercentThreshold):
    """Custom type cItpSpUtilThreshold based on CItpSpPercentThreshold"""
    defaultValue = 40


_CItpSpUtilThreshold_Object = MibScalar
cItpSpUtilThreshold = _CItpSpUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 55),
    _CItpSpUtilThreshold_Type()
)
cItpSpUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpUtilThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpUtilThreshold.setUnits("percent")


class _CItpSpUtilAbateDelta_Type(CItpSpPercentThreshold):
    """Custom type cItpSpUtilAbateDelta based on CItpSpPercentThreshold"""
    defaultValue = 0


_CItpSpUtilAbateDelta_Object = MibScalar
cItpSpUtilAbateDelta = _CItpSpUtilAbateDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 1, 56),
    _CItpSpUtilAbateDelta_Type()
)
cItpSpUtilAbateDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpUtilAbateDelta.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpUtilAbateDelta.setUnits("percent")
_CItpSpPointCode_ObjectIdentity = ObjectIdentity
cItpSpPointCode = _CItpSpPointCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 2)
)
_CItpSpPointCodeTable_Object = MibTable
cItpSpPointCodeTable = _CItpSpPointCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cItpSpPointCodeTable.setStatus("deprecated")
_CItpSpPointCodeTableEntry_Object = MibTableRow
cItpSpPointCodeTableEntry = _CItpSpPointCodeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 2, 1, 1)
)
cItpSpPointCodeTableEntry.setIndexNames(
    (0, "CISCO-ITP-SP-MIB", "cItpSpPointCodeNi"),
    (0, "CISCO-ITP-SP-MIB", "cItpSpPointCodeBin"),
)
if mibBuilder.loadTexts:
    cItpSpPointCodeTableEntry.setStatus("deprecated")
_CItpSpPointCodeNi_Type = CItpTcNetworkIndicator
_CItpSpPointCodeNi_Object = MibTableColumn
cItpSpPointCodeNi = _CItpSpPointCodeNi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 2, 1, 1, 1),
    _CItpSpPointCodeNi_Type()
)
cItpSpPointCodeNi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSpPointCodeNi.setStatus("deprecated")
_CItpSpPointCodeBin_Type = CItpTcPointCode
_CItpSpPointCodeBin_Object = MibTableColumn
cItpSpPointCodeBin = _CItpSpPointCodeBin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 2, 1, 1, 2),
    _CItpSpPointCodeBin_Type()
)
cItpSpPointCodeBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSpPointCodeBin.setStatus("deprecated")
_CItpSpPointCodeType_Type = CItpTcPointCodeType
_CItpSpPointCodeType_Object = MibTableColumn
cItpSpPointCodeType = _CItpSpPointCodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 2, 1, 1, 3),
    _CItpSpPointCodeType_Type()
)
cItpSpPointCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpPointCodeType.setStatus("deprecated")
_CItpSpPointCodeDisplay_Type = CItpTcDisplayPC
_CItpSpPointCodeDisplay_Object = MibTableColumn
cItpSpPointCodeDisplay = _CItpSpPointCodeDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 2, 1, 1, 4),
    _CItpSpPointCodeDisplay_Type()
)
cItpSpPointCodeDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpPointCodeDisplay.setStatus("deprecated")
_CItpSpPointCodeRowStatus_Type = RowStatus
_CItpSpPointCodeRowStatus_Object = MibTableColumn
cItpSpPointCodeRowStatus = _CItpSpPointCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 2, 1, 1, 5),
    _CItpSpPointCodeRowStatus_Type()
)
cItpSpPointCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpPointCodeRowStatus.setStatus("deprecated")
_CItpSpLinkset_ObjectIdentity = ObjectIdentity
cItpSpLinkset = _CItpSpLinkset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3)
)
_CItpSpLinksetTable_Object = MibTable
cItpSpLinksetTable = _CItpSpLinksetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cItpSpLinksetTable.setStatus("deprecated")
_CItpSpLinksetTableEntry_Object = MibTableRow
cItpSpLinksetTableEntry = _CItpSpLinksetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1)
)
cItpSpLinksetTableEntry.setIndexNames(
    (0, "CISCO-ITP-SP-MIB", "cItpSpLinksetName"),
)
if mibBuilder.loadTexts:
    cItpSpLinksetTableEntry.setStatus("deprecated")
_CItpSpLinksetName_Type = CItpTcLinksetId
_CItpSpLinksetName_Object = MibTableColumn
cItpSpLinksetName = _CItpSpLinksetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 1),
    _CItpSpLinksetName_Type()
)
cItpSpLinksetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSpLinksetName.setStatus("deprecated")
_CItpSpLinksetSourcePointCode_Type = CItpTcPointCode
_CItpSpLinksetSourcePointCode_Object = MibTableColumn
cItpSpLinksetSourcePointCode = _CItpSpLinksetSourcePointCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 2),
    _CItpSpLinksetSourcePointCode_Type()
)
cItpSpLinksetSourcePointCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSourcePointCode.setStatus("deprecated")
_CItpSpLinksetSourceDisplayPC_Type = CItpTcDisplayPC
_CItpSpLinksetSourceDisplayPC_Object = MibTableColumn
cItpSpLinksetSourceDisplayPC = _CItpSpLinksetSourceDisplayPC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 3),
    _CItpSpLinksetSourceDisplayPC_Type()
)
cItpSpLinksetSourceDisplayPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinksetSourceDisplayPC.setStatus("deprecated")
_CItpSpLinksetAdjacentPointCode_Type = CItpTcPointCode
_CItpSpLinksetAdjacentPointCode_Object = MibTableColumn
cItpSpLinksetAdjacentPointCode = _CItpSpLinksetAdjacentPointCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 4),
    _CItpSpLinksetAdjacentPointCode_Type()
)
cItpSpLinksetAdjacentPointCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetAdjacentPointCode.setStatus("deprecated")
_CItpSpLinksetAdjacentDisplayPC_Type = CItpTcDisplayPC
_CItpSpLinksetAdjacentDisplayPC_Object = MibTableColumn
cItpSpLinksetAdjacentDisplayPC = _CItpSpLinksetAdjacentDisplayPC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 5),
    _CItpSpLinksetAdjacentDisplayPC_Type()
)
cItpSpLinksetAdjacentDisplayPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinksetAdjacentDisplayPC.setStatus("deprecated")


class _CItpSpLinksetState_Type(Integer32):
    """Custom type cItpSpLinksetState based on Integer32"""
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
          ("shutdown", 2),
          ("unavailable", 3))
    )


_CItpSpLinksetState_Type.__name__ = "Integer32"
_CItpSpLinksetState_Object = MibTableColumn
cItpSpLinksetState = _CItpSpLinksetState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 6),
    _CItpSpLinksetState_Type()
)
cItpSpLinksetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinksetState.setStatus("deprecated")
_CItpSpLinksetInboundAcl_Type = CItpTcAclId
_CItpSpLinksetInboundAcl_Object = MibTableColumn
cItpSpLinksetInboundAcl = _CItpSpLinksetInboundAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 7),
    _CItpSpLinksetInboundAcl_Type()
)
cItpSpLinksetInboundAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetInboundAcl.setStatus("deprecated")
_CItpSpLinksetOutboundAcl_Type = CItpTcAclId
_CItpSpLinksetOutboundAcl_Object = MibTableColumn
cItpSpLinksetOutboundAcl = _CItpSpLinksetOutboundAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 8),
    _CItpSpLinksetOutboundAcl_Type()
)
cItpSpLinksetOutboundAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetOutboundAcl.setStatus("deprecated")
_CItpSpLinksetSnmmRTN_Type = CItpTcRouteTableName
_CItpSpLinksetSnmmRTN_Object = MibTableColumn
cItpSpLinksetSnmmRTN = _CItpSpLinksetSnmmRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 9),
    _CItpSpLinksetSnmmRTN_Type()
)
cItpSpLinksetSnmmRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSnmmRTN.setStatus("deprecated")
_CItpSpLinksetSntmRTN_Type = CItpTcRouteTableName
_CItpSpLinksetSntmRTN_Object = MibTableColumn
cItpSpLinksetSntmRTN = _CItpSpLinksetSntmRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 10),
    _CItpSpLinksetSntmRTN_Type()
)
cItpSpLinksetSntmRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSntmRTN.setStatus("deprecated")
_CItpSpLinksetSpare2RTN_Type = CItpTcRouteTableName
_CItpSpLinksetSpare2RTN_Object = MibTableColumn
cItpSpLinksetSpare2RTN = _CItpSpLinksetSpare2RTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 11),
    _CItpSpLinksetSpare2RTN_Type()
)
cItpSpLinksetSpare2RTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSpare2RTN.setStatus("deprecated")
_CItpSpLinksetSccpRTN_Type = CItpTcRouteTableName
_CItpSpLinksetSccpRTN_Object = MibTableColumn
cItpSpLinksetSccpRTN = _CItpSpLinksetSccpRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 12),
    _CItpSpLinksetSccpRTN_Type()
)
cItpSpLinksetSccpRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSccpRTN.setStatus("deprecated")
_CItpSpLinksetTupRTN_Type = CItpTcRouteTableName
_CItpSpLinksetTupRTN_Object = MibTableColumn
cItpSpLinksetTupRTN = _CItpSpLinksetTupRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 13),
    _CItpSpLinksetTupRTN_Type()
)
cItpSpLinksetTupRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetTupRTN.setStatus("deprecated")
_CItpSpLinksetIsupRTN_Type = CItpTcRouteTableName
_CItpSpLinksetIsupRTN_Object = MibTableColumn
cItpSpLinksetIsupRTN = _CItpSpLinksetIsupRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 14),
    _CItpSpLinksetIsupRTN_Type()
)
cItpSpLinksetIsupRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetIsupRTN.setStatus("deprecated")
_CItpSpLinksetDupcRTN_Type = CItpTcRouteTableName
_CItpSpLinksetDupcRTN_Object = MibTableColumn
cItpSpLinksetDupcRTN = _CItpSpLinksetDupcRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 15),
    _CItpSpLinksetDupcRTN_Type()
)
cItpSpLinksetDupcRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetDupcRTN.setStatus("deprecated")
_CItpSpLinksetDupfRTN_Type = CItpTcRouteTableName
_CItpSpLinksetDupfRTN_Object = MibTableColumn
cItpSpLinksetDupfRTN = _CItpSpLinksetDupfRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 16),
    _CItpSpLinksetDupfRTN_Type()
)
cItpSpLinksetDupfRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetDupfRTN.setStatus("deprecated")
_CItpSpLinksetMtupRTN_Type = CItpTcRouteTableName
_CItpSpLinksetMtupRTN_Object = MibTableColumn
cItpSpLinksetMtupRTN = _CItpSpLinksetMtupRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 17),
    _CItpSpLinksetMtupRTN_Type()
)
cItpSpLinksetMtupRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtupRTN.setStatus("deprecated")
_CItpSpLinksetBisupRTN_Type = CItpTcRouteTableName
_CItpSpLinksetBisupRTN_Object = MibTableColumn
cItpSpLinksetBisupRTN = _CItpSpLinksetBisupRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 18),
    _CItpSpLinksetBisupRTN_Type()
)
cItpSpLinksetBisupRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetBisupRTN.setStatus("deprecated")
_CItpSpLinksetSisupRTN_Type = CItpTcRouteTableName
_CItpSpLinksetSisupRTN_Object = MibTableColumn
cItpSpLinksetSisupRTN = _CItpSpLinksetSisupRTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 19),
    _CItpSpLinksetSisupRTN_Type()
)
cItpSpLinksetSisupRTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSisupRTN.setStatus("deprecated")
_CItpSpLinksetSpare11RTN_Type = CItpTcRouteTableName
_CItpSpLinksetSpare11RTN_Object = MibTableColumn
cItpSpLinksetSpare11RTN = _CItpSpLinksetSpare11RTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 20),
    _CItpSpLinksetSpare11RTN_Type()
)
cItpSpLinksetSpare11RTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSpare11RTN.setStatus("deprecated")
_CItpSpLinksetSpare12RTN_Type = CItpTcRouteTableName
_CItpSpLinksetSpare12RTN_Object = MibTableColumn
cItpSpLinksetSpare12RTN = _CItpSpLinksetSpare12RTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 21),
    _CItpSpLinksetSpare12RTN_Type()
)
cItpSpLinksetSpare12RTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSpare12RTN.setStatus("deprecated")
_CItpSpLinksetSpare13RTN_Type = CItpTcRouteTableName
_CItpSpLinksetSpare13RTN_Object = MibTableColumn
cItpSpLinksetSpare13RTN = _CItpSpLinksetSpare13RTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 22),
    _CItpSpLinksetSpare13RTN_Type()
)
cItpSpLinksetSpare13RTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSpare13RTN.setStatus("deprecated")
_CItpSpLinksetSpare14RTN_Type = CItpTcRouteTableName
_CItpSpLinksetSpare14RTN_Object = MibTableColumn
cItpSpLinksetSpare14RTN = _CItpSpLinksetSpare14RTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 23),
    _CItpSpLinksetSpare14RTN_Type()
)
cItpSpLinksetSpare14RTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSpare14RTN.setStatus("deprecated")
_CItpSpLinksetSpare15RTN_Type = CItpTcRouteTableName
_CItpSpLinksetSpare15RTN_Object = MibTableColumn
cItpSpLinksetSpare15RTN = _CItpSpLinksetSpare15RTN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 24),
    _CItpSpLinksetSpare15RTN_Type()
)
cItpSpLinksetSpare15RTN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetSpare15RTN.setStatus("deprecated")


class _CItpSpLinksetAccountingEnabled_Type(TruthValue):
    """Custom type cItpSpLinksetAccountingEnabled based on TruthValue"""


_CItpSpLinksetAccountingEnabled_Object = MibTableColumn
cItpSpLinksetAccountingEnabled = _CItpSpLinksetAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 25),
    _CItpSpLinksetAccountingEnabled_Type()
)
cItpSpLinksetAccountingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetAccountingEnabled.setStatus("deprecated")
_CItpSpLinksetNumLinks_Type = Unsigned32
_CItpSpLinksetNumLinks_Object = MibTableColumn
cItpSpLinksetNumLinks = _CItpSpLinksetNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 26),
    _CItpSpLinksetNumLinks_Type()
)
cItpSpLinksetNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinksetNumLinks.setStatus("deprecated")
_CItpSpLinksetDurationInService_Type = TimeTicks
_CItpSpLinksetDurationInService_Object = MibTableColumn
cItpSpLinksetDurationInService = _CItpSpLinksetDurationInService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 27),
    _CItpSpLinksetDurationInService_Type()
)
cItpSpLinksetDurationInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinksetDurationInService.setStatus("deprecated")
_CItpSpLinksetDurationOutService_Type = TimeTicks
_CItpSpLinksetDurationOutService_Object = MibTableColumn
cItpSpLinksetDurationOutService = _CItpSpLinksetDurationOutService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 28),
    _CItpSpLinksetDurationOutService_Type()
)
cItpSpLinksetDurationOutService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinksetDurationOutService.setStatus("deprecated")
_CItpSpLinksetMtp2T01_Type = CItpTcTimerMtp2T01
_CItpSpLinksetMtp2T01_Object = MibTableColumn
cItpSpLinksetMtp2T01 = _CItpSpLinksetMtp2T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 29),
    _CItpSpLinksetMtp2T01_Type()
)
cItpSpLinksetMtp2T01.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T01.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T01.setUnits("milliseconds")
_CItpSpLinksetMtp2T02_Type = CItpTcTimerMtp2T02
_CItpSpLinksetMtp2T02_Object = MibTableColumn
cItpSpLinksetMtp2T02 = _CItpSpLinksetMtp2T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 30),
    _CItpSpLinksetMtp2T02_Type()
)
cItpSpLinksetMtp2T02.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T02.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T02.setUnits("milliseconds")
_CItpSpLinksetMtp2T03_Type = CItpTcTimerMtp2T03
_CItpSpLinksetMtp2T03_Object = MibTableColumn
cItpSpLinksetMtp2T03 = _CItpSpLinksetMtp2T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 31),
    _CItpSpLinksetMtp2T03_Type()
)
cItpSpLinksetMtp2T03.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T03.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T03.setUnits("milliseconds")
_CItpSpLinksetMtp2T04E_Type = CItpTcTimerMtp2T04E
_CItpSpLinksetMtp2T04E_Object = MibTableColumn
cItpSpLinksetMtp2T04E = _CItpSpLinksetMtp2T04E_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 32),
    _CItpSpLinksetMtp2T04E_Type()
)
cItpSpLinksetMtp2T04E.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T04E.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T04E.setUnits("milliseconds")
_CItpSpLinksetMtp2T04N_Type = CItpTcTimerMtp2T04N
_CItpSpLinksetMtp2T04N_Object = MibTableColumn
cItpSpLinksetMtp2T04N = _CItpSpLinksetMtp2T04N_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 33),
    _CItpSpLinksetMtp2T04N_Type()
)
cItpSpLinksetMtp2T04N.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T04N.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T04N.setUnits("milliseconds")
_CItpSpLinksetMtp2T05_Type = CItpTcTimerMtp2T05
_CItpSpLinksetMtp2T05_Object = MibTableColumn
cItpSpLinksetMtp2T05 = _CItpSpLinksetMtp2T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 34),
    _CItpSpLinksetMtp2T05_Type()
)
cItpSpLinksetMtp2T05.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T05.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T05.setUnits("milliseconds")
_CItpSpLinksetMtp2T06_Type = CItpTcTimerMtp2T06
_CItpSpLinksetMtp2T06_Object = MibTableColumn
cItpSpLinksetMtp2T06 = _CItpSpLinksetMtp2T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 35),
    _CItpSpLinksetMtp2T06_Type()
)
cItpSpLinksetMtp2T06.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T06.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T06.setUnits("milliseconds")
_CItpSpLinksetMtp2T07_Type = CItpTcTimerMtp2T07
_CItpSpLinksetMtp2T07_Object = MibTableColumn
cItpSpLinksetMtp2T07 = _CItpSpLinksetMtp2T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 36),
    _CItpSpLinksetMtp2T07_Type()
)
cItpSpLinksetMtp2T07.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T07.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp2T07.setUnits("milliseconds")
_CItpSpLinksetMtp3T01_Type = CItpTcTimerMtp3T01
_CItpSpLinksetMtp3T01_Object = MibTableColumn
cItpSpLinksetMtp3T01 = _CItpSpLinksetMtp3T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 37),
    _CItpSpLinksetMtp3T01_Type()
)
cItpSpLinksetMtp3T01.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T01.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T01.setUnits("milliseconds")
_CItpSpLinksetMtp3T02_Type = CItpTcTimerMtp3T02
_CItpSpLinksetMtp3T02_Object = MibTableColumn
cItpSpLinksetMtp3T02 = _CItpSpLinksetMtp3T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 38),
    _CItpSpLinksetMtp3T02_Type()
)
cItpSpLinksetMtp3T02.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T02.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T02.setUnits("milliseconds")
_CItpSpLinksetMtp3T03_Type = CItpTcTimerMtp3T03
_CItpSpLinksetMtp3T03_Object = MibTableColumn
cItpSpLinksetMtp3T03 = _CItpSpLinksetMtp3T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 39),
    _CItpSpLinksetMtp3T03_Type()
)
cItpSpLinksetMtp3T03.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T03.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T03.setUnits("milliseconds")
_CItpSpLinksetMtp3T04_Type = CItpTcTimerMtp3T04
_CItpSpLinksetMtp3T04_Object = MibTableColumn
cItpSpLinksetMtp3T04 = _CItpSpLinksetMtp3T04_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 40),
    _CItpSpLinksetMtp3T04_Type()
)
cItpSpLinksetMtp3T04.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T04.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T04.setUnits("milliseconds")
_CItpSpLinksetMtp3T05_Type = CItpTcTimerMtp3T05
_CItpSpLinksetMtp3T05_Object = MibTableColumn
cItpSpLinksetMtp3T05 = _CItpSpLinksetMtp3T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 41),
    _CItpSpLinksetMtp3T05_Type()
)
cItpSpLinksetMtp3T05.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T05.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T05.setUnits("milliseconds")
_CItpSpLinksetMtp3T06_Type = CItpTcTimerMtp3T06
_CItpSpLinksetMtp3T06_Object = MibTableColumn
cItpSpLinksetMtp3T06 = _CItpSpLinksetMtp3T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 42),
    _CItpSpLinksetMtp3T06_Type()
)
cItpSpLinksetMtp3T06.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T06.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T06.setUnits("milliseconds")
_CItpSpLinksetMtp3T07_Type = CItpTcTimerMtp3T07
_CItpSpLinksetMtp3T07_Object = MibTableColumn
cItpSpLinksetMtp3T07 = _CItpSpLinksetMtp3T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 43),
    _CItpSpLinksetMtp3T07_Type()
)
cItpSpLinksetMtp3T07.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T07.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T07.setUnits("milliseconds")
_CItpSpLinksetMtp3T08_Type = CItpTcTimerMtp3T08
_CItpSpLinksetMtp3T08_Object = MibTableColumn
cItpSpLinksetMtp3T08 = _CItpSpLinksetMtp3T08_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 44),
    _CItpSpLinksetMtp3T08_Type()
)
cItpSpLinksetMtp3T08.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T08.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T08.setUnits("milliseconds")
_CItpSpLinksetMtp3T10_Type = CItpTcTimerMtp3T10
_CItpSpLinksetMtp3T10_Object = MibTableColumn
cItpSpLinksetMtp3T10 = _CItpSpLinksetMtp3T10_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 45),
    _CItpSpLinksetMtp3T10_Type()
)
cItpSpLinksetMtp3T10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T10.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T10.setUnits("milliseconds")
_CItpSpLinksetMtp3T11_Type = CItpTcTimerMtp3T11
_CItpSpLinksetMtp3T11_Object = MibTableColumn
cItpSpLinksetMtp3T11 = _CItpSpLinksetMtp3T11_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 46),
    _CItpSpLinksetMtp3T11_Type()
)
cItpSpLinksetMtp3T11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T11.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T11.setUnits("milliseconds")
_CItpSpLinksetMtp3T12_Type = CItpTcTimerMtp3T12
_CItpSpLinksetMtp3T12_Object = MibTableColumn
cItpSpLinksetMtp3T12 = _CItpSpLinksetMtp3T12_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 47),
    _CItpSpLinksetMtp3T12_Type()
)
cItpSpLinksetMtp3T12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T12.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T12.setUnits("milliseconds")
_CItpSpLinksetMtp3T13_Type = CItpTcTimerMtp3T13
_CItpSpLinksetMtp3T13_Object = MibTableColumn
cItpSpLinksetMtp3T13 = _CItpSpLinksetMtp3T13_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 48),
    _CItpSpLinksetMtp3T13_Type()
)
cItpSpLinksetMtp3T13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T13.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T13.setUnits("milliseconds")
_CItpSpLinksetMtp3T14_Type = CItpTcTimerMtp3T14
_CItpSpLinksetMtp3T14_Object = MibTableColumn
cItpSpLinksetMtp3T14 = _CItpSpLinksetMtp3T14_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 49),
    _CItpSpLinksetMtp3T14_Type()
)
cItpSpLinksetMtp3T14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T14.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T14.setUnits("milliseconds")
_CItpSpLinksetMtp3T15_Type = CItpTcTimerMtp3T15
_CItpSpLinksetMtp3T15_Object = MibTableColumn
cItpSpLinksetMtp3T15 = _CItpSpLinksetMtp3T15_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 50),
    _CItpSpLinksetMtp3T15_Type()
)
cItpSpLinksetMtp3T15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T15.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T15.setUnits("milliseconds")
_CItpSpLinksetMtp3T16_Type = CItpTcTimerMtp3T16
_CItpSpLinksetMtp3T16_Object = MibTableColumn
cItpSpLinksetMtp3T16 = _CItpSpLinksetMtp3T16_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 51),
    _CItpSpLinksetMtp3T16_Type()
)
cItpSpLinksetMtp3T16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T16.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T16.setUnits("milliseconds")
_CItpSpLinksetMtp3T17_Type = CItpTcTimerMtp3T17
_CItpSpLinksetMtp3T17_Object = MibTableColumn
cItpSpLinksetMtp3T17 = _CItpSpLinksetMtp3T17_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 52),
    _CItpSpLinksetMtp3T17_Type()
)
cItpSpLinksetMtp3T17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T17.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T17.setUnits("milliseconds")
_CItpSpLinksetMtp3T18_Type = CItpTcTimerMtp3T18
_CItpSpLinksetMtp3T18_Object = MibTableColumn
cItpSpLinksetMtp3T18 = _CItpSpLinksetMtp3T18_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 53),
    _CItpSpLinksetMtp3T18_Type()
)
cItpSpLinksetMtp3T18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T18.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T18.setUnits("milliseconds")
_CItpSpLinksetMtp3T19_Type = CItpTcTimerMtp3T19
_CItpSpLinksetMtp3T19_Object = MibTableColumn
cItpSpLinksetMtp3T19 = _CItpSpLinksetMtp3T19_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 54),
    _CItpSpLinksetMtp3T19_Type()
)
cItpSpLinksetMtp3T19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T19.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T19.setUnits("milliseconds")
_CItpSpLinksetMtp3T20_Type = CItpTcTimerMtp3T20
_CItpSpLinksetMtp3T20_Object = MibTableColumn
cItpSpLinksetMtp3T20 = _CItpSpLinksetMtp3T20_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 55),
    _CItpSpLinksetMtp3T20_Type()
)
cItpSpLinksetMtp3T20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T20.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T20.setUnits("milliseconds")
_CItpSpLinksetMtp3T21_Type = CItpTcTimerMtp3T21
_CItpSpLinksetMtp3T21_Object = MibTableColumn
cItpSpLinksetMtp3T21 = _CItpSpLinksetMtp3T21_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 56),
    _CItpSpLinksetMtp3T21_Type()
)
cItpSpLinksetMtp3T21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T21.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T21.setUnits("milliseconds")
_CItpSpLinksetMtp3T22_Type = CItpTcTimerMtp3T22
_CItpSpLinksetMtp3T22_Object = MibTableColumn
cItpSpLinksetMtp3T22 = _CItpSpLinksetMtp3T22_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 57),
    _CItpSpLinksetMtp3T22_Type()
)
cItpSpLinksetMtp3T22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T22.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T22.setUnits("milliseconds")
_CItpSpLinksetMtp3T23_Type = CItpTcTimerMtp3T23
_CItpSpLinksetMtp3T23_Object = MibTableColumn
cItpSpLinksetMtp3T23 = _CItpSpLinksetMtp3T23_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 58),
    _CItpSpLinksetMtp3T23_Type()
)
cItpSpLinksetMtp3T23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T23.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T23.setUnits("milliseconds")
_CItpSpLinksetMtp3T24_Type = CItpTcTimerMtp3T24
_CItpSpLinksetMtp3T24_Object = MibTableColumn
cItpSpLinksetMtp3T24 = _CItpSpLinksetMtp3T24_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 59),
    _CItpSpLinksetMtp3T24_Type()
)
cItpSpLinksetMtp3T24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T24.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T24.setUnits("milliseconds")
_CItpSpLinksetMtp3T25_Type = CItpTcTimerMtp3T25
_CItpSpLinksetMtp3T25_Object = MibTableColumn
cItpSpLinksetMtp3T25 = _CItpSpLinksetMtp3T25_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 60),
    _CItpSpLinksetMtp3T25_Type()
)
cItpSpLinksetMtp3T25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T25.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T25.setUnits("milliseconds")
_CItpSpLinksetMtp3T26_Type = CItpTcTimerMtp3T26
_CItpSpLinksetMtp3T26_Object = MibTableColumn
cItpSpLinksetMtp3T26 = _CItpSpLinksetMtp3T26_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 61),
    _CItpSpLinksetMtp3T26_Type()
)
cItpSpLinksetMtp3T26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T26.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T26.setUnits("milliseconds")
_CItpSpLinksetMtp3T27_Type = CItpTcTimerMtp3T27
_CItpSpLinksetMtp3T27_Object = MibTableColumn
cItpSpLinksetMtp3T27 = _CItpSpLinksetMtp3T27_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 62),
    _CItpSpLinksetMtp3T27_Type()
)
cItpSpLinksetMtp3T27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T27.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T27.setUnits("milliseconds")
_CItpSpLinksetMtp3T28_Type = CItpTcTimerMtp3T28
_CItpSpLinksetMtp3T28_Object = MibTableColumn
cItpSpLinksetMtp3T28 = _CItpSpLinksetMtp3T28_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 63),
    _CItpSpLinksetMtp3T28_Type()
)
cItpSpLinksetMtp3T28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T28.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T28.setUnits("milliseconds")
_CItpSpLinksetMtp3T29_Type = CItpTcTimerMtp3T29
_CItpSpLinksetMtp3T29_Object = MibTableColumn
cItpSpLinksetMtp3T29 = _CItpSpLinksetMtp3T29_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 64),
    _CItpSpLinksetMtp3T29_Type()
)
cItpSpLinksetMtp3T29.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T29.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T29.setUnits("milliseconds")
_CItpSpLinksetMtp3T30_Type = CItpTcTimerMtp3T30
_CItpSpLinksetMtp3T30_Object = MibTableColumn
cItpSpLinksetMtp3T30 = _CItpSpLinksetMtp3T30_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 65),
    _CItpSpLinksetMtp3T30_Type()
)
cItpSpLinksetMtp3T30.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T30.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T30.setUnits("milliseconds")
_CItpSpLinksetMtp3T31_Type = CItpTcTimerMtp3T31
_CItpSpLinksetMtp3T31_Object = MibTableColumn
cItpSpLinksetMtp3T31 = _CItpSpLinksetMtp3T31_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 66),
    _CItpSpLinksetMtp3T31_Type()
)
cItpSpLinksetMtp3T31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T31.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T31.setUnits("milliseconds")
_CItpSpLinksetMtp3T32_Type = CItpTcTimerMtp3T32
_CItpSpLinksetMtp3T32_Object = MibTableColumn
cItpSpLinksetMtp3T32 = _CItpSpLinksetMtp3T32_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 67),
    _CItpSpLinksetMtp3T32_Type()
)
cItpSpLinksetMtp3T32.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T32.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T32.setUnits("milliseconds")
_CItpSpLinksetMtp3T33_Type = CItpTcTimerMtp3T33
_CItpSpLinksetMtp3T33_Object = MibTableColumn
cItpSpLinksetMtp3T33 = _CItpSpLinksetMtp3T33_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 68),
    _CItpSpLinksetMtp3T33_Type()
)
cItpSpLinksetMtp3T33.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T33.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T33.setUnits("milliseconds")
_CItpSpLinksetMtp3T34_Type = CItpTcTimerMtp3T34
_CItpSpLinksetMtp3T34_Object = MibTableColumn
cItpSpLinksetMtp3T34 = _CItpSpLinksetMtp3T34_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 69),
    _CItpSpLinksetMtp3T34_Type()
)
cItpSpLinksetMtp3T34.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T34.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetMtp3T34.setUnits("milliseconds")
_CItpSpLinksetTimerLinkTest_Type = CItpTcTimerLinkTest
_CItpSpLinksetTimerLinkTest_Object = MibTableColumn
cItpSpLinksetTimerLinkTest = _CItpSpLinksetTimerLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 70),
    _CItpSpLinksetTimerLinkTest_Type()
)
cItpSpLinksetTimerLinkTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetTimerLinkTest.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetTimerLinkTest.setUnits("milliseconds")
_CItpSpLinksetTimerLinkMessage_Type = CItpTcTimerLinkMessage
_CItpSpLinksetTimerLinkMessage_Object = MibTableColumn
cItpSpLinksetTimerLinkMessage = _CItpSpLinksetTimerLinkMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 71),
    _CItpSpLinksetTimerLinkMessage_Type()
)
cItpSpLinksetTimerLinkMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetTimerLinkMessage.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetTimerLinkMessage.setUnits("milliseconds")
_CItpSpLinksetTimerLinkActRetry_Type = CItpTcTimerLinkActRetry
_CItpSpLinksetTimerLinkActRetry_Object = MibTableColumn
cItpSpLinksetTimerLinkActRetry = _CItpSpLinksetTimerLinkActRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 72),
    _CItpSpLinksetTimerLinkActRetry_Type()
)
cItpSpLinksetTimerLinkActRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetTimerLinkActRetry.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetTimerLinkActRetry.setUnits("milliseconds")


class _CItpSpLinksetPlanCapacity_Type(Integer32):
    """Custom type cItpSpLinksetPlanCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(56000, 2147483647),
    )


_CItpSpLinksetPlanCapacity_Type.__name__ = "Integer32"
_CItpSpLinksetPlanCapacity_Object = MibTableColumn
cItpSpLinksetPlanCapacity = _CItpSpLinksetPlanCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 73),
    _CItpSpLinksetPlanCapacity_Type()
)
cItpSpLinksetPlanCapacity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetPlanCapacity.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinksetPlanCapacity.setUnits("bps")


class _CItpSpLinksetActPriority_Type(Unsigned32):
    """Custom type cItpSpLinksetActPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CItpSpLinksetActPriority_Type.__name__ = "Unsigned32"
_CItpSpLinksetActPriority_Object = MibTableColumn
cItpSpLinksetActPriority = _CItpSpLinksetActPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 74),
    _CItpSpLinksetActPriority_Type()
)
cItpSpLinksetActPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetActPriority.setStatus("deprecated")


class _CItpSpLinksetType_Type(Integer32):
    """Custom type cItpSpLinksetType based on Integer32"""
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
        *(("access", 1),
          ("bridge", 2),
          ("cross", 3),
          ("diagonal", 4),
          ("fullyAssoc", 5))
    )


_CItpSpLinksetType_Type.__name__ = "Integer32"
_CItpSpLinksetType_Object = MibTableColumn
cItpSpLinksetType = _CItpSpLinksetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 75),
    _CItpSpLinksetType_Type()
)
cItpSpLinksetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetType.setStatus("deprecated")
_CItpSpLinksetRowStatus_Type = RowStatus
_CItpSpLinksetRowStatus_Object = MibTableColumn
cItpSpLinksetRowStatus = _CItpSpLinksetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 76),
    _CItpSpLinksetRowStatus_Type()
)
cItpSpLinksetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetRowStatus.setStatus("deprecated")
_CItpSpLinksetNi_Type = CItpTcNetworkIndicator
_CItpSpLinksetNi_Object = MibTableColumn
cItpSpLinksetNi = _CItpSpLinksetNi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 77),
    _CItpSpLinksetNi_Type()
)
cItpSpLinksetNi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetNi.setStatus("deprecated")


class _CItpSpLinksetDisplayName_Type(SnmpAdminString):
    """Custom type cItpSpLinksetDisplayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CItpSpLinksetDisplayName_Type.__name__ = "SnmpAdminString"
_CItpSpLinksetDisplayName_Object = MibTableColumn
cItpSpLinksetDisplayName = _CItpSpLinksetDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 78),
    _CItpSpLinksetDisplayName_Type()
)
cItpSpLinksetDisplayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetDisplayName.setStatus("deprecated")


class _CItpSpLinksetDescription_Type(SnmpAdminString):
    """Custom type cItpSpLinksetDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CItpSpLinksetDescription_Type.__name__ = "SnmpAdminString"
_CItpSpLinksetDescription_Object = MibTableColumn
cItpSpLinksetDescription = _CItpSpLinksetDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 79),
    _CItpSpLinksetDescription_Type()
)
cItpSpLinksetDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetDescription.setStatus("deprecated")
_CItpSpLinksetVariant_Type = CItpTcSs7Variant
_CItpSpLinksetVariant_Object = MibTableColumn
cItpSpLinksetVariant = _CItpSpLinksetVariant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 3, 1, 1, 80),
    _CItpSpLinksetVariant_Type()
)
cItpSpLinksetVariant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinksetVariant.setStatus("deprecated")
_CItpSpLink_ObjectIdentity = ObjectIdentity
cItpSpLink = _CItpSpLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4)
)
_CItpSpLinkTable_Object = MibTable
cItpSpLinkTable = _CItpSpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cItpSpLinkTable.setStatus("deprecated")
_CItpSpLinkTableEntry_Object = MibTableRow
cItpSpLinkTableEntry = _CItpSpLinkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1)
)
cItpSpLinkTableEntry.setIndexNames(
    (0, "CISCO-ITP-SP-MIB", "cItpSpLinksetName"),
    (0, "CISCO-ITP-SP-MIB", "cItpSpLinkSlc"),
)
if mibBuilder.loadTexts:
    cItpSpLinkTableEntry.setStatus("deprecated")
_CItpSpLinkSlc_Type = CItpTcLinkSLC
_CItpSpLinkSlc_Object = MibTableColumn
cItpSpLinkSlc = _CItpSpLinkSlc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 1),
    _CItpSpLinkSlc_Type()
)
cItpSpLinkSlc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSpLinkSlc.setStatus("deprecated")


class _CItpSpLinkDescription_Type(SnmpAdminString):
    """Custom type cItpSpLinkDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CItpSpLinkDescription_Type.__name__ = "SnmpAdminString"
_CItpSpLinkDescription_Object = MibTableColumn
cItpSpLinkDescription = _CItpSpLinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 2),
    _CItpSpLinkDescription_Type()
)
cItpSpLinkDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkDescription.setStatus("deprecated")


class _CItpSpLinkState_Type(Integer32):
    """Custom type cItpSpLinkState based on Integer32"""
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
        *(("available", 1),
          ("failed", 2),
          ("shutdown", 3),
          ("unavailable", 4))
    )


_CItpSpLinkState_Type.__name__ = "Integer32"
_CItpSpLinkState_Object = MibTableColumn
cItpSpLinkState = _CItpSpLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 3),
    _CItpSpLinkState_Type()
)
cItpSpLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkState.setStatus("deprecated")
_CItpSpLinkType_Type = CItpTcLinkType
_CItpSpLinkType_Object = MibTableColumn
cItpSpLinkType = _CItpSpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 4),
    _CItpSpLinkType_Type()
)
cItpSpLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkType.setStatus("deprecated")
_CItpSpLinkifIndex_Type = InterfaceIndexOrZero
_CItpSpLinkifIndex_Object = MibTableColumn
cItpSpLinkifIndex = _CItpSpLinkifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 5),
    _CItpSpLinkifIndex_Type()
)
cItpSpLinkifIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkifIndex.setStatus("deprecated")


class _CItpSpLinkSctpAssociation_Type(Integer32):
    """Custom type cItpSpLinkSctpAssociation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSpLinkSctpAssociation_Type.__name__ = "Integer32"
_CItpSpLinkSctpAssociation_Object = MibTableColumn
cItpSpLinkSctpAssociation = _CItpSpLinkSctpAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 6),
    _CItpSpLinkSctpAssociation_Type()
)
cItpSpLinkSctpAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkSctpAssociation.setStatus("deprecated")
_CItpSpLinkMtp3PacketsRcvd_Type = Counter32
_CItpSpLinkMtp3PacketsRcvd_Object = MibTableColumn
cItpSpLinkMtp3PacketsRcvd = _CItpSpLinkMtp3PacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 7),
    _CItpSpLinkMtp3PacketsRcvd_Type()
)
cItpSpLinkMtp3PacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3PacketsRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3PacketsRcvd.setUnits("packets")
_CItpSpLinkMtp3PacketsSent_Type = Counter32
_CItpSpLinkMtp3PacketsSent_Object = MibTableColumn
cItpSpLinkMtp3PacketsSent = _CItpSpLinkMtp3PacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 8),
    _CItpSpLinkMtp3PacketsSent_Type()
)
cItpSpLinkMtp3PacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3PacketsSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3PacketsSent.setUnits("packets")
_CItpSpLinkMtp3BytesRcvd_Type = Counter32
_CItpSpLinkMtp3BytesRcvd_Object = MibTableColumn
cItpSpLinkMtp3BytesRcvd = _CItpSpLinkMtp3BytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 9),
    _CItpSpLinkMtp3BytesRcvd_Type()
)
cItpSpLinkMtp3BytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3BytesRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3BytesRcvd.setUnits("bytes")
_CItpSpLinkMtp3BytesSent_Type = Counter32
_CItpSpLinkMtp3BytesSent_Object = MibTableColumn
cItpSpLinkMtp3BytesSent = _CItpSpLinkMtp3BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 10),
    _CItpSpLinkMtp3BytesSent_Type()
)
cItpSpLinkMtp3BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3BytesSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3BytesSent.setUnits("bytes")
_CItpSpLinkMtp2T01_Type = CItpTcTimerMtp2T01
_CItpSpLinkMtp2T01_Object = MibTableColumn
cItpSpLinkMtp2T01 = _CItpSpLinkMtp2T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 11),
    _CItpSpLinkMtp2T01_Type()
)
cItpSpLinkMtp2T01.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T01.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T01.setUnits("milliseconds")
_CItpSpLinkMtp2T02_Type = CItpTcTimerMtp2T02
_CItpSpLinkMtp2T02_Object = MibTableColumn
cItpSpLinkMtp2T02 = _CItpSpLinkMtp2T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 12),
    _CItpSpLinkMtp2T02_Type()
)
cItpSpLinkMtp2T02.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T02.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T02.setUnits("milliseconds")
_CItpSpLinkMtp2T03_Type = CItpTcTimerMtp2T03
_CItpSpLinkMtp2T03_Object = MibTableColumn
cItpSpLinkMtp2T03 = _CItpSpLinkMtp2T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 13),
    _CItpSpLinkMtp2T03_Type()
)
cItpSpLinkMtp2T03.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T03.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T03.setUnits("milliseconds")
_CItpSpLinkMtp2T04E_Type = CItpTcTimerMtp2T04E
_CItpSpLinkMtp2T04E_Object = MibTableColumn
cItpSpLinkMtp2T04E = _CItpSpLinkMtp2T04E_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 14),
    _CItpSpLinkMtp2T04E_Type()
)
cItpSpLinkMtp2T04E.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T04E.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T04E.setUnits("milliseconds")
_CItpSpLinkMtp2T04N_Type = CItpTcTimerMtp2T04N
_CItpSpLinkMtp2T04N_Object = MibTableColumn
cItpSpLinkMtp2T04N = _CItpSpLinkMtp2T04N_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 15),
    _CItpSpLinkMtp2T04N_Type()
)
cItpSpLinkMtp2T04N.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T04N.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T04N.setUnits("milliseconds")
_CItpSpLinkMtp2T05_Type = CItpTcTimerMtp2T05
_CItpSpLinkMtp2T05_Object = MibTableColumn
cItpSpLinkMtp2T05 = _CItpSpLinkMtp2T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 16),
    _CItpSpLinkMtp2T05_Type()
)
cItpSpLinkMtp2T05.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T05.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T05.setUnits("milliseconds")
_CItpSpLinkMtp2T06_Type = CItpTcTimerMtp2T06
_CItpSpLinkMtp2T06_Object = MibTableColumn
cItpSpLinkMtp2T06 = _CItpSpLinkMtp2T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 17),
    _CItpSpLinkMtp2T06_Type()
)
cItpSpLinkMtp2T06.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T06.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T06.setUnits("milliseconds")
_CItpSpLinkMtp2T07_Type = CItpTcTimerMtp2T07
_CItpSpLinkMtp2T07_Object = MibTableColumn
cItpSpLinkMtp2T07 = _CItpSpLinkMtp2T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 18),
    _CItpSpLinkMtp2T07_Type()
)
cItpSpLinkMtp2T07.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T07.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2T07.setUnits("milliseconds")
_CItpSpLinkMtp3T01_Type = CItpTcTimerMtp3T01
_CItpSpLinkMtp3T01_Object = MibTableColumn
cItpSpLinkMtp3T01 = _CItpSpLinkMtp3T01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 19),
    _CItpSpLinkMtp3T01_Type()
)
cItpSpLinkMtp3T01.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T01.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T01.setUnits("milliseconds")
_CItpSpLinkMtp3T02_Type = CItpTcTimerMtp3T02
_CItpSpLinkMtp3T02_Object = MibTableColumn
cItpSpLinkMtp3T02 = _CItpSpLinkMtp3T02_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 20),
    _CItpSpLinkMtp3T02_Type()
)
cItpSpLinkMtp3T02.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T02.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T02.setUnits("milliseconds")
_CItpSpLinkMtp3T03_Type = CItpTcTimerMtp3T03
_CItpSpLinkMtp3T03_Object = MibTableColumn
cItpSpLinkMtp3T03 = _CItpSpLinkMtp3T03_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 21),
    _CItpSpLinkMtp3T03_Type()
)
cItpSpLinkMtp3T03.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T03.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T03.setUnits("milliseconds")
_CItpSpLinkMtp3T04_Type = CItpTcTimerMtp3T04
_CItpSpLinkMtp3T04_Object = MibTableColumn
cItpSpLinkMtp3T04 = _CItpSpLinkMtp3T04_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 22),
    _CItpSpLinkMtp3T04_Type()
)
cItpSpLinkMtp3T04.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T04.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T04.setUnits("milliseconds")
_CItpSpLinkMtp3T05_Type = CItpTcTimerMtp3T05
_CItpSpLinkMtp3T05_Object = MibTableColumn
cItpSpLinkMtp3T05 = _CItpSpLinkMtp3T05_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 23),
    _CItpSpLinkMtp3T05_Type()
)
cItpSpLinkMtp3T05.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T05.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T05.setUnits("milliseconds")
_CItpSpLinkMtp3T06_Type = CItpTcTimerMtp3T06
_CItpSpLinkMtp3T06_Object = MibTableColumn
cItpSpLinkMtp3T06 = _CItpSpLinkMtp3T06_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 24),
    _CItpSpLinkMtp3T06_Type()
)
cItpSpLinkMtp3T06.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T06.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T06.setUnits("milliseconds")
_CItpSpLinkMtp3T07_Type = CItpTcTimerMtp3T07
_CItpSpLinkMtp3T07_Object = MibTableColumn
cItpSpLinkMtp3T07 = _CItpSpLinkMtp3T07_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 25),
    _CItpSpLinkMtp3T07_Type()
)
cItpSpLinkMtp3T07.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T07.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T07.setUnits("milliseconds")
_CItpSpLinkMtp3T08_Type = CItpTcTimerMtp3T08
_CItpSpLinkMtp3T08_Object = MibTableColumn
cItpSpLinkMtp3T08 = _CItpSpLinkMtp3T08_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 26),
    _CItpSpLinkMtp3T08_Type()
)
cItpSpLinkMtp3T08.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T08.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T08.setUnits("milliseconds")
_CItpSpLinkMtp3T10_Type = CItpTcTimerMtp3T10
_CItpSpLinkMtp3T10_Object = MibTableColumn
cItpSpLinkMtp3T10 = _CItpSpLinkMtp3T10_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 27),
    _CItpSpLinkMtp3T10_Type()
)
cItpSpLinkMtp3T10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T10.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T10.setUnits("milliseconds")
_CItpSpLinkMtp3T11_Type = CItpTcTimerMtp3T11
_CItpSpLinkMtp3T11_Object = MibTableColumn
cItpSpLinkMtp3T11 = _CItpSpLinkMtp3T11_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 28),
    _CItpSpLinkMtp3T11_Type()
)
cItpSpLinkMtp3T11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T11.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T11.setUnits("milliseconds")
_CItpSpLinkMtp3T12_Type = CItpTcTimerMtp3T12
_CItpSpLinkMtp3T12_Object = MibTableColumn
cItpSpLinkMtp3T12 = _CItpSpLinkMtp3T12_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 29),
    _CItpSpLinkMtp3T12_Type()
)
cItpSpLinkMtp3T12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T12.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T12.setUnits("milliseconds")
_CItpSpLinkMtp3T13_Type = CItpTcTimerMtp3T13
_CItpSpLinkMtp3T13_Object = MibTableColumn
cItpSpLinkMtp3T13 = _CItpSpLinkMtp3T13_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 30),
    _CItpSpLinkMtp3T13_Type()
)
cItpSpLinkMtp3T13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T13.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T13.setUnits("milliseconds")
_CItpSpLinkMtp3T14_Type = CItpTcTimerMtp3T14
_CItpSpLinkMtp3T14_Object = MibTableColumn
cItpSpLinkMtp3T14 = _CItpSpLinkMtp3T14_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 31),
    _CItpSpLinkMtp3T14_Type()
)
cItpSpLinkMtp3T14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T14.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T14.setUnits("milliseconds")
_CItpSpLinkMtp3T15_Type = CItpTcTimerMtp3T15
_CItpSpLinkMtp3T15_Object = MibTableColumn
cItpSpLinkMtp3T15 = _CItpSpLinkMtp3T15_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 32),
    _CItpSpLinkMtp3T15_Type()
)
cItpSpLinkMtp3T15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T15.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T15.setUnits("milliseconds")
_CItpSpLinkMtp3T16_Type = CItpTcTimerMtp3T16
_CItpSpLinkMtp3T16_Object = MibTableColumn
cItpSpLinkMtp3T16 = _CItpSpLinkMtp3T16_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 33),
    _CItpSpLinkMtp3T16_Type()
)
cItpSpLinkMtp3T16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T16.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T16.setUnits("milliseconds")
_CItpSpLinkMtp3T17_Type = CItpTcTimerMtp3T17
_CItpSpLinkMtp3T17_Object = MibTableColumn
cItpSpLinkMtp3T17 = _CItpSpLinkMtp3T17_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 34),
    _CItpSpLinkMtp3T17_Type()
)
cItpSpLinkMtp3T17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T17.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T17.setUnits("milliseconds")
_CItpSpLinkMtp3T18_Type = CItpTcTimerMtp3T18
_CItpSpLinkMtp3T18_Object = MibTableColumn
cItpSpLinkMtp3T18 = _CItpSpLinkMtp3T18_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 35),
    _CItpSpLinkMtp3T18_Type()
)
cItpSpLinkMtp3T18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T18.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T18.setUnits("milliseconds")
_CItpSpLinkMtp3T19_Type = CItpTcTimerMtp3T19
_CItpSpLinkMtp3T19_Object = MibTableColumn
cItpSpLinkMtp3T19 = _CItpSpLinkMtp3T19_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 36),
    _CItpSpLinkMtp3T19_Type()
)
cItpSpLinkMtp3T19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T19.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T19.setUnits("milliseconds")
_CItpSpLinkMtp3T20_Type = CItpTcTimerMtp3T20
_CItpSpLinkMtp3T20_Object = MibTableColumn
cItpSpLinkMtp3T20 = _CItpSpLinkMtp3T20_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 37),
    _CItpSpLinkMtp3T20_Type()
)
cItpSpLinkMtp3T20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T20.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T20.setUnits("milliseconds")
_CItpSpLinkMtp3T21_Type = CItpTcTimerMtp3T21
_CItpSpLinkMtp3T21_Object = MibTableColumn
cItpSpLinkMtp3T21 = _CItpSpLinkMtp3T21_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 38),
    _CItpSpLinkMtp3T21_Type()
)
cItpSpLinkMtp3T21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T21.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T21.setUnits("milliseconds")
_CItpSpLinkMtp3T22_Type = CItpTcTimerMtp3T22
_CItpSpLinkMtp3T22_Object = MibTableColumn
cItpSpLinkMtp3T22 = _CItpSpLinkMtp3T22_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 39),
    _CItpSpLinkMtp3T22_Type()
)
cItpSpLinkMtp3T22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T22.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T22.setUnits("milliseconds")
_CItpSpLinkMtp3T23_Type = CItpTcTimerMtp3T23
_CItpSpLinkMtp3T23_Object = MibTableColumn
cItpSpLinkMtp3T23 = _CItpSpLinkMtp3T23_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 40),
    _CItpSpLinkMtp3T23_Type()
)
cItpSpLinkMtp3T23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T23.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T23.setUnits("milliseconds")
_CItpSpLinkMtp3T24_Type = CItpTcTimerMtp3T24
_CItpSpLinkMtp3T24_Object = MibTableColumn
cItpSpLinkMtp3T24 = _CItpSpLinkMtp3T24_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 41),
    _CItpSpLinkMtp3T24_Type()
)
cItpSpLinkMtp3T24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T24.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T24.setUnits("milliseconds")
_CItpSpLinkMtp3T25_Type = CItpTcTimerMtp3T25
_CItpSpLinkMtp3T25_Object = MibTableColumn
cItpSpLinkMtp3T25 = _CItpSpLinkMtp3T25_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 42),
    _CItpSpLinkMtp3T25_Type()
)
cItpSpLinkMtp3T25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T25.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T25.setUnits("milliseconds")
_CItpSpLinkMtp3T26_Type = CItpTcTimerMtp3T26
_CItpSpLinkMtp3T26_Object = MibTableColumn
cItpSpLinkMtp3T26 = _CItpSpLinkMtp3T26_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 43),
    _CItpSpLinkMtp3T26_Type()
)
cItpSpLinkMtp3T26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T26.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T26.setUnits("milliseconds")
_CItpSpLinkMtp3T27_Type = CItpTcTimerMtp3T27
_CItpSpLinkMtp3T27_Object = MibTableColumn
cItpSpLinkMtp3T27 = _CItpSpLinkMtp3T27_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 44),
    _CItpSpLinkMtp3T27_Type()
)
cItpSpLinkMtp3T27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T27.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T27.setUnits("milliseconds")
_CItpSpLinkMtp3T28_Type = CItpTcTimerMtp3T28
_CItpSpLinkMtp3T28_Object = MibTableColumn
cItpSpLinkMtp3T28 = _CItpSpLinkMtp3T28_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 45),
    _CItpSpLinkMtp3T28_Type()
)
cItpSpLinkMtp3T28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T28.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T28.setUnits("milliseconds")
_CItpSpLinkMtp3T29_Type = CItpTcTimerMtp3T29
_CItpSpLinkMtp3T29_Object = MibTableColumn
cItpSpLinkMtp3T29 = _CItpSpLinkMtp3T29_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 46),
    _CItpSpLinkMtp3T29_Type()
)
cItpSpLinkMtp3T29.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T29.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T29.setUnits("milliseconds")
_CItpSpLinkMtp3T30_Type = CItpTcTimerMtp3T30
_CItpSpLinkMtp3T30_Object = MibTableColumn
cItpSpLinkMtp3T30 = _CItpSpLinkMtp3T30_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 47),
    _CItpSpLinkMtp3T30_Type()
)
cItpSpLinkMtp3T30.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T30.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T30.setUnits("milliseconds")
_CItpSpLinkMtp3T31_Type = CItpTcTimerMtp3T31
_CItpSpLinkMtp3T31_Object = MibTableColumn
cItpSpLinkMtp3T31 = _CItpSpLinkMtp3T31_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 48),
    _CItpSpLinkMtp3T31_Type()
)
cItpSpLinkMtp3T31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T31.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T31.setUnits("milliseconds")
_CItpSpLinkMtp3T32_Type = CItpTcTimerMtp3T32
_CItpSpLinkMtp3T32_Object = MibTableColumn
cItpSpLinkMtp3T32 = _CItpSpLinkMtp3T32_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 49),
    _CItpSpLinkMtp3T32_Type()
)
cItpSpLinkMtp3T32.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T32.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T32.setUnits("milliseconds")
_CItpSpLinkMtp3T33_Type = CItpTcTimerMtp3T33
_CItpSpLinkMtp3T33_Object = MibTableColumn
cItpSpLinkMtp3T33 = _CItpSpLinkMtp3T33_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 50),
    _CItpSpLinkMtp3T33_Type()
)
cItpSpLinkMtp3T33.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T33.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T33.setUnits("milliseconds")
_CItpSpLinkMtp3T34_Type = CItpTcTimerMtp3T34
_CItpSpLinkMtp3T34_Object = MibTableColumn
cItpSpLinkMtp3T34 = _CItpSpLinkMtp3T34_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 51),
    _CItpSpLinkMtp3T34_Type()
)
cItpSpLinkMtp3T34.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T34.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3T34.setUnits("milliseconds")
_CItpSpLinkTimerLinkTest_Type = CItpTcTimerLinkTest
_CItpSpLinkTimerLinkTest_Object = MibTableColumn
cItpSpLinkTimerLinkTest = _CItpSpLinkTimerLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 52),
    _CItpSpLinkTimerLinkTest_Type()
)
cItpSpLinkTimerLinkTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkTimerLinkTest.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkTimerLinkTest.setUnits("milliseconds")
_CItpSpLinkTimerLinkMessage_Type = CItpTcTimerLinkMessage
_CItpSpLinkTimerLinkMessage_Object = MibTableColumn
cItpSpLinkTimerLinkMessage = _CItpSpLinkTimerLinkMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 53),
    _CItpSpLinkTimerLinkMessage_Type()
)
cItpSpLinkTimerLinkMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkTimerLinkMessage.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkTimerLinkMessage.setUnits("milliseconds")
_CItpSpLinkTimerLinkActRetry_Type = CItpTcTimerLinkActRetry
_CItpSpLinkTimerLinkActRetry_Object = MibTableColumn
cItpSpLinkTimerLinkActRetry = _CItpSpLinkTimerLinkActRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 54),
    _CItpSpLinkTimerLinkActRetry_Type()
)
cItpSpLinkTimerLinkActRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkTimerLinkActRetry.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkTimerLinkActRetry.setUnits("milliseconds")
_CItpSpLinkXmitQueueDepth_Type = Gauge32
_CItpSpLinkXmitQueueDepth_Object = MibTableColumn
cItpSpLinkXmitQueueDepth = _CItpSpLinkXmitQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 55),
    _CItpSpLinkXmitQueueDepth_Type()
)
cItpSpLinkXmitQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkXmitQueueDepth.setStatus("deprecated")
_CItpSpLinkXmitQueueDepthHigh_Type = Unsigned32
_CItpSpLinkXmitQueueDepthHigh_Object = MibTableColumn
cItpSpLinkXmitQueueDepthHigh = _CItpSpLinkXmitQueueDepthHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 56),
    _CItpSpLinkXmitQueueDepthHigh_Type()
)
cItpSpLinkXmitQueueDepthHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkXmitQueueDepthHigh.setStatus("deprecated")
_CItpSpLinkXmitQueueDepthHighRT_Type = TimeStamp
_CItpSpLinkXmitQueueDepthHighRT_Object = MibTableColumn
cItpSpLinkXmitQueueDepthHighRT = _CItpSpLinkXmitQueueDepthHighRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 57),
    _CItpSpLinkXmitQueueDepthHighRT_Type()
)
cItpSpLinkXmitQueueDepthHighRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkXmitQueueDepthHighRT.setStatus("deprecated")


class _CItpSpLinkCongestionState_Type(Unsigned32):
    """Custom type cItpSpLinkCongestionState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CItpSpLinkCongestionState_Type.__name__ = "Unsigned32"
_CItpSpLinkCongestionState_Object = MibTableColumn
cItpSpLinkCongestionState = _CItpSpLinkCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 58),
    _CItpSpLinkCongestionState_Type()
)
cItpSpLinkCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkCongestionState.setStatus("deprecated")


class _CItpSpLinkCongestionAbate1_Type(Unsigned32):
    """Custom type cItpSpLinkCongestionAbate1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSpLinkCongestionAbate1_Type.__name__ = "Unsigned32"
_CItpSpLinkCongestionAbate1_Object = MibTableColumn
cItpSpLinkCongestionAbate1 = _CItpSpLinkCongestionAbate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 59),
    _CItpSpLinkCongestionAbate1_Type()
)
cItpSpLinkCongestionAbate1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkCongestionAbate1.setStatus("deprecated")


class _CItpSpLinkCongestionAbate2_Type(Unsigned32):
    """Custom type cItpSpLinkCongestionAbate2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSpLinkCongestionAbate2_Type.__name__ = "Unsigned32"
_CItpSpLinkCongestionAbate2_Object = MibTableColumn
cItpSpLinkCongestionAbate2 = _CItpSpLinkCongestionAbate2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 60),
    _CItpSpLinkCongestionAbate2_Type()
)
cItpSpLinkCongestionAbate2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkCongestionAbate2.setStatus("deprecated")


class _CItpSpLinkCongestionAbate3_Type(Unsigned32):
    """Custom type cItpSpLinkCongestionAbate3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSpLinkCongestionAbate3_Type.__name__ = "Unsigned32"
_CItpSpLinkCongestionAbate3_Object = MibTableColumn
cItpSpLinkCongestionAbate3 = _CItpSpLinkCongestionAbate3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 61),
    _CItpSpLinkCongestionAbate3_Type()
)
cItpSpLinkCongestionAbate3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkCongestionAbate3.setStatus("deprecated")


class _CItpSpLinkCongestionOnset1_Type(Unsigned32):
    """Custom type cItpSpLinkCongestionOnset1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSpLinkCongestionOnset1_Type.__name__ = "Unsigned32"
_CItpSpLinkCongestionOnset1_Object = MibTableColumn
cItpSpLinkCongestionOnset1 = _CItpSpLinkCongestionOnset1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 62),
    _CItpSpLinkCongestionOnset1_Type()
)
cItpSpLinkCongestionOnset1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkCongestionOnset1.setStatus("deprecated")


class _CItpSpLinkCongestionOnset2_Type(Unsigned32):
    """Custom type cItpSpLinkCongestionOnset2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSpLinkCongestionOnset2_Type.__name__ = "Unsigned32"
_CItpSpLinkCongestionOnset2_Object = MibTableColumn
cItpSpLinkCongestionOnset2 = _CItpSpLinkCongestionOnset2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 63),
    _CItpSpLinkCongestionOnset2_Type()
)
cItpSpLinkCongestionOnset2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkCongestionOnset2.setStatus("deprecated")


class _CItpSpLinkCongestionOnset3_Type(Unsigned32):
    """Custom type cItpSpLinkCongestionOnset3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSpLinkCongestionOnset3_Type.__name__ = "Unsigned32"
_CItpSpLinkCongestionOnset3_Object = MibTableColumn
cItpSpLinkCongestionOnset3 = _CItpSpLinkCongestionOnset3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 64),
    _CItpSpLinkCongestionOnset3_Type()
)
cItpSpLinkCongestionOnset3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkCongestionOnset3.setStatus("deprecated")


class _CItpSpLinkSigLinkTest_Type(TruthValue):
    """Custom type cItpSpLinkSigLinkTest based on TruthValue"""


_CItpSpLinkSigLinkTest_Object = MibTableColumn
cItpSpLinkSigLinkTest = _CItpSpLinkSigLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 65),
    _CItpSpLinkSigLinkTest_Type()
)
cItpSpLinkSigLinkTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkSigLinkTest.setStatus("deprecated")
_CItpSpLinkQ752T1E1_Type = TimeTicks
_CItpSpLinkQ752T1E1_Object = MibTableColumn
cItpSpLinkQ752T1E1 = _CItpSpLinkQ752T1E1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 66),
    _CItpSpLinkQ752T1E1_Type()
)
cItpSpLinkQ752T1E1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E1.setStatus("deprecated")
_CItpSpLinkQ752T1E2_Type = Counter32
_CItpSpLinkQ752T1E2_Object = MibTableColumn
cItpSpLinkQ752T1E2 = _CItpSpLinkQ752T1E2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 67),
    _CItpSpLinkQ752T1E2_Type()
)
cItpSpLinkQ752T1E2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E2.setStatus("deprecated")
_CItpSpLinkQ752T1E3_Type = Counter32
_CItpSpLinkQ752T1E3_Object = MibTableColumn
cItpSpLinkQ752T1E3 = _CItpSpLinkQ752T1E3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 68),
    _CItpSpLinkQ752T1E3_Type()
)
cItpSpLinkQ752T1E3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E3.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E3.setUnits("occurrences")
_CItpSpLinkQ752T1E4_Type = Counter32
_CItpSpLinkQ752T1E4_Object = MibTableColumn
cItpSpLinkQ752T1E4 = _CItpSpLinkQ752T1E4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 69),
    _CItpSpLinkQ752T1E4_Type()
)
cItpSpLinkQ752T1E4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E4.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E4.setUnits("occurrences")
_CItpSpLinkQ752T1E5_Type = Counter32
_CItpSpLinkQ752T1E5_Object = MibTableColumn
cItpSpLinkQ752T1E5 = _CItpSpLinkQ752T1E5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 70),
    _CItpSpLinkQ752T1E5_Type()
)
cItpSpLinkQ752T1E5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E5.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E5.setUnits("occurrences")
_CItpSpLinkQ752T1E6_Type = Counter32
_CItpSpLinkQ752T1E6_Object = MibTableColumn
cItpSpLinkQ752T1E6 = _CItpSpLinkQ752T1E6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 71),
    _CItpSpLinkQ752T1E6_Type()
)
cItpSpLinkQ752T1E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E6.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E6.setUnits("occurrences")
_CItpSpLinkQ752T1E7_Type = Counter32
_CItpSpLinkQ752T1E7_Object = MibTableColumn
cItpSpLinkQ752T1E7 = _CItpSpLinkQ752T1E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 72),
    _CItpSpLinkQ752T1E7_Type()
)
cItpSpLinkQ752T1E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E7.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E7.setUnits("occurrences")
_CItpSpLinkQ752T1E8_Type = Counter32
_CItpSpLinkQ752T1E8_Object = MibTableColumn
cItpSpLinkQ752T1E8 = _CItpSpLinkQ752T1E8_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 73),
    _CItpSpLinkQ752T1E8_Type()
)
cItpSpLinkQ752T1E8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E8.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E8.setUnits("occurrences")
_CItpSpLinkQ752T1E9_Type = Counter32
_CItpSpLinkQ752T1E9_Object = MibTableColumn
cItpSpLinkQ752T1E9 = _CItpSpLinkQ752T1E9_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 74),
    _CItpSpLinkQ752T1E9_Type()
)
cItpSpLinkQ752T1E9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E9.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E9.setUnits("negative acknowledgements")
_CItpSpLinkQ752T1E10_Type = Counter32
_CItpSpLinkQ752T1E10_Object = MibTableColumn
cItpSpLinkQ752T1E10 = _CItpSpLinkQ752T1E10_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 75),
    _CItpSpLinkQ752T1E10_Type()
)
cItpSpLinkQ752T1E10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E10.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E10.setUnits("occurrences")
_CItpSpLinkQ752T1E11_Type = Counter32
_CItpSpLinkQ752T1E11_Object = MibTableColumn
cItpSpLinkQ752T1E11 = _CItpSpLinkQ752T1E11_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 76),
    _CItpSpLinkQ752T1E11_Type()
)
cItpSpLinkQ752T1E11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E11.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T1E11.setUnits("occurrences")
_CItpSpLinkQ752T2E1_Type = TimeTicks
_CItpSpLinkQ752T2E1_Object = MibTableColumn
cItpSpLinkQ752T2E1 = _CItpSpLinkQ752T2E1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 77),
    _CItpSpLinkQ752T2E1_Type()
)
cItpSpLinkQ752T2E1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E1.setStatus("deprecated")
_CItpSpLinkQ752T2E5_Type = TimeTicks
_CItpSpLinkQ752T2E5_Object = MibTableColumn
cItpSpLinkQ752T2E5 = _CItpSpLinkQ752T2E5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 78),
    _CItpSpLinkQ752T2E5_Type()
)
cItpSpLinkQ752T2E5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E5.setStatus("deprecated")
_CItpSpLinkQ752T2E6_Type = TimeTicks
_CItpSpLinkQ752T2E6_Object = MibTableColumn
cItpSpLinkQ752T2E6 = _CItpSpLinkQ752T2E6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 79),
    _CItpSpLinkQ752T2E6_Type()
)
cItpSpLinkQ752T2E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E6.setStatus("deprecated")
_CItpSpLinkQ752T2E7_Type = TimeTicks
_CItpSpLinkQ752T2E7_Object = MibTableColumn
cItpSpLinkQ752T2E7 = _CItpSpLinkQ752T2E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 80),
    _CItpSpLinkQ752T2E7_Type()
)
cItpSpLinkQ752T2E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E7.setStatus("deprecated")
_CItpSpLinkQ752T2E9_Type = TimeTicks
_CItpSpLinkQ752T2E9_Object = MibTableColumn
cItpSpLinkQ752T2E9 = _CItpSpLinkQ752T2E9_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 81),
    _CItpSpLinkQ752T2E9_Type()
)
cItpSpLinkQ752T2E9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E9.setStatus("deprecated")
_CItpSpLinkQ752T2E10_Type = Counter32
_CItpSpLinkQ752T2E10_Object = MibTableColumn
cItpSpLinkQ752T2E10 = _CItpSpLinkQ752T2E10_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 82),
    _CItpSpLinkQ752T2E10_Type()
)
cItpSpLinkQ752T2E10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E10.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E10.setUnits("occurrences")
_CItpSpLinkQ752T2E15_Type = TimeTicks
_CItpSpLinkQ752T2E15_Object = MibTableColumn
cItpSpLinkQ752T2E15 = _CItpSpLinkQ752T2E15_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 83),
    _CItpSpLinkQ752T2E15_Type()
)
cItpSpLinkQ752T2E15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E15.setStatus("deprecated")
_CItpSpLinkQ752T2E16_Type = Counter32
_CItpSpLinkQ752T2E16_Object = MibTableColumn
cItpSpLinkQ752T2E16 = _CItpSpLinkQ752T2E16_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 84),
    _CItpSpLinkQ752T2E16_Type()
)
cItpSpLinkQ752T2E16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E16.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E16.setUnits("occurrences")
_CItpSpLinkQ752T2E18_Type = Counter32
_CItpSpLinkQ752T2E18_Object = MibTableColumn
cItpSpLinkQ752T2E18 = _CItpSpLinkQ752T2E18_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 85),
    _CItpSpLinkQ752T2E18_Type()
)
cItpSpLinkQ752T2E18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E18.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T2E18.setUnits("occurrences")
_CItpSpLinkMtp3PacketsRetrans_Type = Counter32
_CItpSpLinkMtp3PacketsRetrans_Object = MibTableColumn
cItpSpLinkMtp3PacketsRetrans = _CItpSpLinkMtp3PacketsRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 86),
    _CItpSpLinkMtp3PacketsRetrans_Type()
)
cItpSpLinkMtp3PacketsRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3PacketsRetrans.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3PacketsRetrans.setUnits("packets")
_CItpSpLinkMtp3BytesRetrans_Type = Counter32
_CItpSpLinkMtp3BytesRetrans_Object = MibTableColumn
cItpSpLinkMtp3BytesRetrans = _CItpSpLinkMtp3BytesRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 87),
    _CItpSpLinkMtp3BytesRetrans_Type()
)
cItpSpLinkMtp3BytesRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3BytesRetrans.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkMtp3BytesRetrans.setUnits("bytes")
_CItpSpLinkQ752T3E6_Type = Counter32
_CItpSpLinkQ752T3E6_Object = MibTableColumn
cItpSpLinkQ752T3E6 = _CItpSpLinkQ752T3E6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 88),
    _CItpSpLinkQ752T3E6_Type()
)
cItpSpLinkQ752T3E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E6.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E6.setUnits("events")
_CItpSpLinkQ752T3E7_Type = TimeTicks
_CItpSpLinkQ752T3E7_Object = MibTableColumn
cItpSpLinkQ752T3E7 = _CItpSpLinkQ752T3E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 89),
    _CItpSpLinkQ752T3E7_Type()
)
cItpSpLinkQ752T3E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E7.setStatus("deprecated")
_CItpSpLinkQ752T3E10L1_Type = Counter32
_CItpSpLinkQ752T3E10L1_Object = MibTableColumn
cItpSpLinkQ752T3E10L1 = _CItpSpLinkQ752T3E10L1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 90),
    _CItpSpLinkQ752T3E10L1_Type()
)
cItpSpLinkQ752T3E10L1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E10L1.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E10L1.setUnits("Packets")
_CItpSpLinkQ752T3E10L2_Type = Counter32
_CItpSpLinkQ752T3E10L2_Object = MibTableColumn
cItpSpLinkQ752T3E10L2 = _CItpSpLinkQ752T3E10L2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 91),
    _CItpSpLinkQ752T3E10L2_Type()
)
cItpSpLinkQ752T3E10L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E10L2.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E10L2.setUnits("Packets")
_CItpSpLinkQ752T3E10L3_Type = Counter32
_CItpSpLinkQ752T3E10L3_Object = MibTableColumn
cItpSpLinkQ752T3E10L3 = _CItpSpLinkQ752T3E10L3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 92),
    _CItpSpLinkQ752T3E10L3_Type()
)
cItpSpLinkQ752T3E10L3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E10L3.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E10L3.setUnits("Packets")
_CItpSpLinkQ752T3E11L1_Type = Counter32
_CItpSpLinkQ752T3E11L1_Object = MibTableColumn
cItpSpLinkQ752T3E11L1 = _CItpSpLinkQ752T3E11L1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 93),
    _CItpSpLinkQ752T3E11L1_Type()
)
cItpSpLinkQ752T3E11L1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E11L1.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E11L1.setUnits("bytes")
_CItpSpLinkQ752T3E11L2_Type = Counter32
_CItpSpLinkQ752T3E11L2_Object = MibTableColumn
cItpSpLinkQ752T3E11L2 = _CItpSpLinkQ752T3E11L2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 94),
    _CItpSpLinkQ752T3E11L2_Type()
)
cItpSpLinkQ752T3E11L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E11L2.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E11L2.setUnits("bytes")
_CItpSpLinkQ752T3E11L3_Type = Counter32
_CItpSpLinkQ752T3E11L3_Object = MibTableColumn
cItpSpLinkQ752T3E11L3 = _CItpSpLinkQ752T3E11L3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 95),
    _CItpSpLinkQ752T3E11L3_Type()
)
cItpSpLinkQ752T3E11L3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E11L3.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkQ752T3E11L3.setUnits("bytes")
_CItpSpLinkIPType1_Type = InetAddressType
_CItpSpLinkIPType1_Object = MibTableColumn
cItpSpLinkIPType1 = _CItpSpLinkIPType1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 96),
    _CItpSpLinkIPType1_Type()
)
cItpSpLinkIPType1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkIPType1.setStatus("deprecated")
_CItpSpLinkIPType2_Type = InetAddressType
_CItpSpLinkIPType2_Object = MibTableColumn
cItpSpLinkIPType2 = _CItpSpLinkIPType2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 97),
    _CItpSpLinkIPType2_Type()
)
cItpSpLinkIPType2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkIPType2.setStatus("deprecated")
_CItpSpLinkIPType3_Type = InetAddressType
_CItpSpLinkIPType3_Object = MibTableColumn
cItpSpLinkIPType3 = _CItpSpLinkIPType3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 98),
    _CItpSpLinkIPType3_Type()
)
cItpSpLinkIPType3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkIPType3.setStatus("deprecated")
_CItpSpLinkIPType4_Type = InetAddressType
_CItpSpLinkIPType4_Object = MibTableColumn
cItpSpLinkIPType4 = _CItpSpLinkIPType4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 99),
    _CItpSpLinkIPType4_Type()
)
cItpSpLinkIPType4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkIPType4.setStatus("deprecated")
_CItpSpLinkIPAddr1_Type = InetAddress
_CItpSpLinkIPAddr1_Object = MibTableColumn
cItpSpLinkIPAddr1 = _CItpSpLinkIPAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 100),
    _CItpSpLinkIPAddr1_Type()
)
cItpSpLinkIPAddr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkIPAddr1.setStatus("deprecated")
_CItpSpLinkIPAddr2_Type = InetAddress
_CItpSpLinkIPAddr2_Object = MibTableColumn
cItpSpLinkIPAddr2 = _CItpSpLinkIPAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 101),
    _CItpSpLinkIPAddr2_Type()
)
cItpSpLinkIPAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkIPAddr2.setStatus("deprecated")
_CItpSpLinkIPAddr3_Type = InetAddress
_CItpSpLinkIPAddr3_Object = MibTableColumn
cItpSpLinkIPAddr3 = _CItpSpLinkIPAddr3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 102),
    _CItpSpLinkIPAddr3_Type()
)
cItpSpLinkIPAddr3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkIPAddr3.setStatus("deprecated")
_CItpSpLinkIPAddr4_Type = InetAddress
_CItpSpLinkIPAddr4_Object = MibTableColumn
cItpSpLinkIPAddr4 = _CItpSpLinkIPAddr4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 103),
    _CItpSpLinkIPAddr4_Type()
)
cItpSpLinkIPAddr4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkIPAddr4.setStatus("deprecated")


class _CItpSpLinkLocalPort_Type(Unsigned32):
    """Custom type cItpSpLinkLocalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSpLinkLocalPort_Type.__name__ = "Unsigned32"
_CItpSpLinkLocalPort_Object = MibTableColumn
cItpSpLinkLocalPort = _CItpSpLinkLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 104),
    _CItpSpLinkLocalPort_Type()
)
cItpSpLinkLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkLocalPort.setStatus("deprecated")


class _CItpSpLinkRemotePort_Type(Unsigned32):
    """Custom type cItpSpLinkRemotePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSpLinkRemotePort_Type.__name__ = "Unsigned32"
_CItpSpLinkRemotePort_Object = MibTableColumn
cItpSpLinkRemotePort = _CItpSpLinkRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 105),
    _CItpSpLinkRemotePort_Type()
)
cItpSpLinkRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkRemotePort.setStatus("deprecated")
_CItpSpLinkQosClass_Type = CItpTcQos
_CItpSpLinkQosClass_Object = MibTableColumn
cItpSpLinkQosClass = _CItpSpLinkQosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 106),
    _CItpSpLinkQosClass_Type()
)
cItpSpLinkQosClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkQosClass.setStatus("deprecated")
_CItpSpLinkRowStatus_Type = RowStatus
_CItpSpLinkRowStatus_Object = MibTableColumn
cItpSpLinkRowStatus = _CItpSpLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 107),
    _CItpSpLinkRowStatus_Type()
)
cItpSpLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkRowStatus.setStatus("deprecated")


class _CItpSpLinkStateReason_Type(Bits):
    """Custom type cItpSpLinkStateReason based on Bits"""
    namedValues = NamedValues(
        *(("blocked", 2),
          ("localInhibit", 0),
          ("remoteInhibit", 1))
    )

_CItpSpLinkStateReason_Type.__name__ = "Bits"
_CItpSpLinkStateReason_Object = MibTableColumn
cItpSpLinkStateReason = _CItpSpLinkStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 108),
    _CItpSpLinkStateReason_Type()
)
cItpSpLinkStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkStateReason.setStatus("deprecated")


class _CItpSpLinkDisplayName_Type(SnmpAdminString):
    """Custom type cItpSpLinkDisplayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CItpSpLinkDisplayName_Type.__name__ = "SnmpAdminString"
_CItpSpLinkDisplayName_Object = MibTableColumn
cItpSpLinkDisplayName = _CItpSpLinkDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 109),
    _CItpSpLinkDisplayName_Type()
)
cItpSpLinkDisplayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkDisplayName.setStatus("deprecated")
_CItpSpLinkDroppedPkts_Type = Counter32
_CItpSpLinkDroppedPkts_Object = MibTableColumn
cItpSpLinkDroppedPkts = _CItpSpLinkDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 110),
    _CItpSpLinkDroppedPkts_Type()
)
cItpSpLinkDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkDroppedPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkDroppedPkts.setUnits("packets")
_CItpSpLinkTransmittedLssu_Type = Counter32
_CItpSpLinkTransmittedLssu_Object = MibTableColumn
cItpSpLinkTransmittedLssu = _CItpSpLinkTransmittedLssu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 111),
    _CItpSpLinkTransmittedLssu_Type()
)
cItpSpLinkTransmittedLssu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkTransmittedLssu.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkTransmittedLssu.setUnits("LSSU")
_CItpSpLinkReceivedLssu_Type = Counter32
_CItpSpLinkReceivedLssu_Object = MibTableColumn
cItpSpLinkReceivedLssu = _CItpSpLinkReceivedLssu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 112),
    _CItpSpLinkReceivedLssu_Type()
)
cItpSpLinkReceivedLssu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkReceivedLssu.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkReceivedLssu.setUnits("LSSU")


class _CItpSpLinkProtocolDetails_Type(Bits):
    """Custom type cItpSpLinkProtocolDetails based on Bits"""
    namedValues = NamedValues(
        *(("tcbcBuffering", 0),
          ("tcocBuffering", 1),
          ("tlacAdjacentSpRestarting", 2),
          ("tlacChangebackInProgress", 4),
          ("tlacChangeoverFailed", 6),
          ("tlacChangeoverInProgress", 5),
          ("tlacEmergencyCoInProgress", 3),
          ("tlacInhibitRetry", 7),
          ("tlacManagementRequest", 8),
          ("tlacSpRestarting", 9),
          ("tsrcAdjacentSpRestart", 11),
          ("tsrcChangeOverComplete", 10))
    )

_CItpSpLinkProtocolDetails_Type.__name__ = "Bits"
_CItpSpLinkProtocolDetails_Object = MibTableColumn
cItpSpLinkProtocolDetails = _CItpSpLinkProtocolDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 113),
    _CItpSpLinkProtocolDetails_Type()
)
cItpSpLinkProtocolDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkProtocolDetails.setStatus("deprecated")


class _CItpSpLinkLsacState_Type(Integer32):
    """Custom type cItpSpLinkLsacState based on Integer32"""
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
        *(("actAnsiWaitDeloaded", 7),
          ("actItuWaitStmReady", 8),
          ("actT17wait", 6),
          ("activatingRestoring", 4),
          ("active", 3),
          ("failed", 5),
          ("inactive", 2),
          ("undefined", 1))
    )


_CItpSpLinkLsacState_Type.__name__ = "Integer32"
_CItpSpLinkLsacState_Object = MibTableColumn
cItpSpLinkLsacState = _CItpSpLinkLsacState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 114),
    _CItpSpLinkLsacState_Type()
)
cItpSpLinkLsacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkLsacState.setStatus("deprecated")


class _CItpSpLinkTsrcState_Type(Integer32):
    """Custom type cItpSpLinkTsrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("undefined", 1),
          ("wait5", 3))
    )


_CItpSpLinkTsrcState_Type.__name__ = "Integer32"
_CItpSpLinkTsrcState_Object = MibTableColumn
cItpSpLinkTsrcState = _CItpSpLinkTsrcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 115),
    _CItpSpLinkTsrcState_Type()
)
cItpSpLinkTsrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkTsrcState.setStatus("deprecated")


class _CItpSpLinkTcocState_Type(Integer32):
    """Custom type cItpSpLinkTcocState based on Integer32"""
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
        *(("idle", 2),
          ("retrieving", 5),
          ("undefined", 1),
          ("wait2", 3),
          ("wait5", 6),
          ("wait7", 7),
          ("wait8", 8),
          ("waitForAck", 4))
    )


_CItpSpLinkTcocState_Type.__name__ = "Integer32"
_CItpSpLinkTcocState_Object = MibTableColumn
cItpSpLinkTcocState = _CItpSpLinkTcocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 116),
    _CItpSpLinkTcocState_Type()
)
cItpSpLinkTcocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkTcocState.setStatus("deprecated")
_CItpSpLinkTcocLocalBSNT_Type = CItpSpSequenceNumber
_CItpSpLinkTcocLocalBSNT_Object = MibTableColumn
cItpSpLinkTcocLocalBSNT = _CItpSpLinkTcocLocalBSNT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 117),
    _CItpSpLinkTcocLocalBSNT_Type()
)
cItpSpLinkTcocLocalBSNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkTcocLocalBSNT.setStatus("deprecated")
_CItpSpLinkTcocRemoteBSNT_Type = CItpSpSequenceNumber
_CItpSpLinkTcocRemoteBSNT_Object = MibTableColumn
cItpSpLinkTcocRemoteBSNT = _CItpSpLinkTcocRemoteBSNT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 118),
    _CItpSpLinkTcocRemoteBSNT_Type()
)
cItpSpLinkTcocRemoteBSNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkTcocRemoteBSNT.setStatus("deprecated")


class _CItpSpLinkTcbcState_Type(Integer32):
    """Custom type cItpSpLinkTcbcState based on Integer32"""
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
        *(("firstAttempt", 3),
          ("idle", 2),
          ("secondAttempt", 4),
          ("timeControlledDiversion", 5),
          ("undefined", 1))
    )


_CItpSpLinkTcbcState_Type.__name__ = "Integer32"
_CItpSpLinkTcbcState_Object = MibTableColumn
cItpSpLinkTcbcState = _CItpSpLinkTcbcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 119),
    _CItpSpLinkTcbcState_Type()
)
cItpSpLinkTcbcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkTcbcState.setStatus("deprecated")
_CItpSpLinkReceivedSIB_Type = Counter32
_CItpSpLinkReceivedSIB_Object = MibTableColumn
cItpSpLinkReceivedSIB = _CItpSpLinkReceivedSIB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 120),
    _CItpSpLinkReceivedSIB_Type()
)
cItpSpLinkReceivedSIB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkReceivedSIB.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkReceivedSIB.setUnits("SIB")
_CItpSpLinkTransmittedSIB_Type = Counter32
_CItpSpLinkTransmittedSIB_Object = MibTableColumn
cItpSpLinkTransmittedSIB = _CItpSpLinkTransmittedSIB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 121),
    _CItpSpLinkTransmittedSIB_Type()
)
cItpSpLinkTransmittedSIB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkTransmittedSIB.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkTransmittedSIB.setUnits("SIB")
_CItpSpLinkMtp2ExpiredT01_Type = Counter32
_CItpSpLinkMtp2ExpiredT01_Object = MibTableColumn
cItpSpLinkMtp2ExpiredT01 = _CItpSpLinkMtp2ExpiredT01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 122),
    _CItpSpLinkMtp2ExpiredT01_Type()
)
cItpSpLinkMtp2ExpiredT01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2ExpiredT01.setStatus("deprecated")
_CItpSpLinkMtp2ExpiredT02_Type = Counter32
_CItpSpLinkMtp2ExpiredT02_Object = MibTableColumn
cItpSpLinkMtp2ExpiredT02 = _CItpSpLinkMtp2ExpiredT02_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 123),
    _CItpSpLinkMtp2ExpiredT02_Type()
)
cItpSpLinkMtp2ExpiredT02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2ExpiredT02.setStatus("deprecated")
_CItpSpLinkMtp2ExpiredT03_Type = Counter32
_CItpSpLinkMtp2ExpiredT03_Object = MibTableColumn
cItpSpLinkMtp2ExpiredT03 = _CItpSpLinkMtp2ExpiredT03_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 124),
    _CItpSpLinkMtp2ExpiredT03_Type()
)
cItpSpLinkMtp2ExpiredT03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2ExpiredT03.setStatus("deprecated")
_CItpSpLinkMtp2ExpiredT04_Type = Counter32
_CItpSpLinkMtp2ExpiredT04_Object = MibTableColumn
cItpSpLinkMtp2ExpiredT04 = _CItpSpLinkMtp2ExpiredT04_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 125),
    _CItpSpLinkMtp2ExpiredT04_Type()
)
cItpSpLinkMtp2ExpiredT04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2ExpiredT04.setStatus("deprecated")
_CItpSpLinkMtp2ExpiredT05_Type = Counter32
_CItpSpLinkMtp2ExpiredT05_Object = MibTableColumn
cItpSpLinkMtp2ExpiredT05 = _CItpSpLinkMtp2ExpiredT05_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 126),
    _CItpSpLinkMtp2ExpiredT05_Type()
)
cItpSpLinkMtp2ExpiredT05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2ExpiredT05.setStatus("deprecated")
_CItpSpLinkMtp2ExpiredT06_Type = Counter32
_CItpSpLinkMtp2ExpiredT06_Object = MibTableColumn
cItpSpLinkMtp2ExpiredT06 = _CItpSpLinkMtp2ExpiredT06_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 127),
    _CItpSpLinkMtp2ExpiredT06_Type()
)
cItpSpLinkMtp2ExpiredT06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2ExpiredT06.setStatus("deprecated")
_CItpSpLinkMtp2ExpiredT07_Type = Counter32
_CItpSpLinkMtp2ExpiredT07_Object = MibTableColumn
cItpSpLinkMtp2ExpiredT07 = _CItpSpLinkMtp2ExpiredT07_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 128),
    _CItpSpLinkMtp2ExpiredT07_Type()
)
cItpSpLinkMtp2ExpiredT07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkMtp2ExpiredT07.setStatus("deprecated")
_CItpSpLinkOMAERMCount_Type = Counter32
_CItpSpLinkOMAERMCount_Object = MibTableColumn
cItpSpLinkOMAERMCount = _CItpSpLinkOMAERMCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 129),
    _CItpSpLinkOMAERMCount_Type()
)
cItpSpLinkOMAERMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkOMAERMCount.setStatus("deprecated")
_CItpSpLinkOMAERMFailCount_Type = Counter32
_CItpSpLinkOMAERMFailCount_Object = MibTableColumn
cItpSpLinkOMAERMFailCount = _CItpSpLinkOMAERMFailCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 130),
    _CItpSpLinkOMAERMFailCount_Type()
)
cItpSpLinkOMAERMFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkOMAERMFailCount.setStatus("deprecated")
_CItpSpLinkOMSURMCount_Type = Counter32
_CItpSpLinkOMSURMCount_Object = MibTableColumn
cItpSpLinkOMSURMCount = _CItpSpLinkOMSURMCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 131),
    _CItpSpLinkOMSURMCount_Type()
)
cItpSpLinkOMSURMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkOMSURMCount.setStatus("deprecated")
_CItpSpLinkOMSURMFailCount_Type = Counter32
_CItpSpLinkOMSURMFailCount_Object = MibTableColumn
cItpSpLinkOMSURMFailCount = _CItpSpLinkOMSURMFailCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 132),
    _CItpSpLinkOMSURMFailCount_Type()
)
cItpSpLinkOMSURMFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkOMSURMFailCount.setStatus("deprecated")
_CItpSpLinkPlanCapacityRcvd_Type = CItpSpLinkCapacity
_CItpSpLinkPlanCapacityRcvd_Object = MibTableColumn
cItpSpLinkPlanCapacityRcvd = _CItpSpLinkPlanCapacityRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 133),
    _CItpSpLinkPlanCapacityRcvd_Type()
)
cItpSpLinkPlanCapacityRcvd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkPlanCapacityRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkPlanCapacityRcvd.setUnits("bits per second")


class _CItpSpLinkUtilThresholdRcvd_Type(CItpSpPercentThreshold):
    """Custom type cItpSpLinkUtilThresholdRcvd based on CItpSpPercentThreshold"""
    defaultValue = 0


_CItpSpLinkUtilThresholdRcvd_Object = MibTableColumn
cItpSpLinkUtilThresholdRcvd = _CItpSpLinkUtilThresholdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 134),
    _CItpSpLinkUtilThresholdRcvd_Type()
)
cItpSpLinkUtilThresholdRcvd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkUtilThresholdRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkUtilThresholdRcvd.setUnits("percent")
_CItpSpLinkUtilizationRcvd_Type = CItpSpLinkUtilization
_CItpSpLinkUtilizationRcvd_Object = MibTableColumn
cItpSpLinkUtilizationRcvd = _CItpSpLinkUtilizationRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 135),
    _CItpSpLinkUtilizationRcvd_Type()
)
cItpSpLinkUtilizationRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkUtilizationRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkUtilizationRcvd.setUnits("percent")
_CItpSpLinkUtilStateRcvd_Type = CItpSpLinkUtilizationState
_CItpSpLinkUtilStateRcvd_Object = MibTableColumn
cItpSpLinkUtilStateRcvd = _CItpSpLinkUtilStateRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 136),
    _CItpSpLinkUtilStateRcvd_Type()
)
cItpSpLinkUtilStateRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkUtilStateRcvd.setStatus("deprecated")
_CItpSpLinkL2BytesRcvd_Type = Counter32
_CItpSpLinkL2BytesRcvd_Object = MibTableColumn
cItpSpLinkL2BytesRcvd = _CItpSpLinkL2BytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 137),
    _CItpSpLinkL2BytesRcvd_Type()
)
cItpSpLinkL2BytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkL2BytesRcvd.setStatus("deprecated")
_CItpSpLinkPlanCapacitySent_Type = CItpSpLinkCapacity
_CItpSpLinkPlanCapacitySent_Object = MibTableColumn
cItpSpLinkPlanCapacitySent = _CItpSpLinkPlanCapacitySent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 138),
    _CItpSpLinkPlanCapacitySent_Type()
)
cItpSpLinkPlanCapacitySent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkPlanCapacitySent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkPlanCapacitySent.setUnits("bits per second")


class _CItpSpLinkUtilThresholdSent_Type(CItpSpPercentThreshold):
    """Custom type cItpSpLinkUtilThresholdSent based on CItpSpPercentThreshold"""
    defaultValue = 0


_CItpSpLinkUtilThresholdSent_Object = MibTableColumn
cItpSpLinkUtilThresholdSent = _CItpSpLinkUtilThresholdSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 139),
    _CItpSpLinkUtilThresholdSent_Type()
)
cItpSpLinkUtilThresholdSent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpSpLinkUtilThresholdSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkUtilThresholdSent.setUnits("percent")
_CItpSpLinkUtilizationSent_Type = CItpSpLinkUtilization
_CItpSpLinkUtilizationSent_Object = MibTableColumn
cItpSpLinkUtilizationSent = _CItpSpLinkUtilizationSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 140),
    _CItpSpLinkUtilizationSent_Type()
)
cItpSpLinkUtilizationSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkUtilizationSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSpLinkUtilizationSent.setUnits("percent")
_CItpSpLinkUtilStateSent_Type = CItpSpLinkUtilizationState
_CItpSpLinkUtilStateSent_Object = MibTableColumn
cItpSpLinkUtilStateSent = _CItpSpLinkUtilStateSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 141),
    _CItpSpLinkUtilStateSent_Type()
)
cItpSpLinkUtilStateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkUtilStateSent.setStatus("deprecated")
_CItpSpLinkL2BytesSent_Type = Counter32
_CItpSpLinkL2BytesSent_Object = MibTableColumn
cItpSpLinkL2BytesSent = _CItpSpLinkL2BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 4, 1, 1, 142),
    _CItpSpLinkL2BytesSent_Type()
)
cItpSpLinkL2BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSpLinkL2BytesSent.setStatus("deprecated")
_CItpSpNotificationsEnable_ObjectIdentity = ObjectIdentity
cItpSpNotificationsEnable = _CItpSpNotificationsEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 5)
)


class _CItpSpLsStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cItpSpLsStateChangeNotifEnabled based on TruthValue"""


_CItpSpLsStateChangeNotifEnabled_Object = MibScalar
cItpSpLsStateChangeNotifEnabled = _CItpSpLsStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 5, 1),
    _CItpSpLsStateChangeNotifEnabled_Type()
)
cItpSpLsStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpLsStateChangeNotifEnabled.setStatus("deprecated")


class _CItpSpLnkStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cItpSpLnkStateChangeNotifEnabled based on TruthValue"""


_CItpSpLnkStateChangeNotifEnabled_Object = MibScalar
cItpSpLnkStateChangeNotifEnabled = _CItpSpLnkStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 5, 2),
    _CItpSpLnkStateChangeNotifEnabled_Type()
)
cItpSpLnkStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpLnkStateChangeNotifEnabled.setStatus("deprecated")


class _CItpSpCongestionNotifEnabled_Type(TruthValue):
    """Custom type cItpSpCongestionNotifEnabled based on TruthValue"""


_CItpSpCongestionNotifEnabled_Object = MibScalar
cItpSpCongestionNotifEnabled = _CItpSpCongestionNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 5, 3),
    _CItpSpCongestionNotifEnabled_Type()
)
cItpSpCongestionNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpCongestionNotifEnabled.setStatus("deprecated")


class _CItpSpLinkUtilNotifEnabled_Type(TruthValue):
    """Custom type cItpSpLinkUtilNotifEnabled based on TruthValue"""


_CItpSpLinkUtilNotifEnabled_Object = MibScalar
cItpSpLinkUtilNotifEnabled = _CItpSpLinkUtilNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 1, 5, 4),
    _CItpSpLinkUtilNotifEnabled_Type()
)
cItpSpLinkUtilNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSpLinkUtilNotifEnabled.setStatus("deprecated")
_CItpSpMIBConformance_ObjectIdentity = ObjectIdentity
cItpSpMIBConformance = _CItpSpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2)
)
_CItpSpMIBCompliances_ObjectIdentity = ObjectIdentity
cItpSpMIBCompliances = _CItpSpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 1)
)
_CItpSpMIBGroups_ObjectIdentity = ObjectIdentity
cItpSpMIBGroups = _CItpSpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2)
)

# Managed Objects groups

cItpSpScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 1)
)
cItpSpScalarsGroup.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpVariant"),
        ("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-SP-MIB", "cItpSpDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpDescription"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T04E"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T04N"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T04"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T08"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T10"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T11"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T12"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T13"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T14"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T15"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T16"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T17"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T18"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T19"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T20"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T21"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T22"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T23"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T24"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T25"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T26"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T27"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T28"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T29"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T30"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T31"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T32"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T33"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T34"),
        ("CISCO-ITP-SP-MIB", "cItpSpTimerLinkTest"),
        ("CISCO-ITP-SP-MIB", "cItpSpTimerLinkMessage"),
        ("CISCO-ITP-SP-MIB", "cItpSpTimerLinkActRetry"),
        ("CISCO-ITP-SP-MIB", "cItpSpTFR"),
        ("CISCO-ITP-SP-MIB", "cItpSpCongestionsLevels"),
        ("CISCO-ITP-SP-MIB", "cItpSpFastRestart"))
)
if mibBuilder.loadTexts:
    cItpSpScalarsGroup.setStatus("deprecated")

cItpSpPointCodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 2)
)
cItpSpPointCodeGroup.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpPointCodeType"),
        ("CISCO-ITP-SP-MIB", "cItpSpPointCodeDisplay"),
        ("CISCO-ITP-SP-MIB", "cItpSpPointCodeRowStatus"))
)
if mibBuilder.loadTexts:
    cItpSpPointCodeGroup.setStatus("deprecated")

cItpSpLinksetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 3)
)
cItpSpLinksetGroup.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpLinksetSourcePointCode"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSourceDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAdjacentPointCode"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetInboundAcl"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetOutboundAcl"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSnmmRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSntmRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare2RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSccpRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetTupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetIsupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDupcRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDupfRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetBisupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSisupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare11RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare12RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare13RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare14RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare15RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAccountingEnabled"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetNumLinks"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDurationInService"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDurationOutService"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T04E"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T04N"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T04"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T08"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T10"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T11"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T12"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T13"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T14"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T15"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T16"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T17"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T18"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T19"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T20"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T21"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T22"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T23"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T24"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T25"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T26"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T27"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T28"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T29"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T30"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T31"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T32"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T33"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T34"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetTimerLinkTest"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetTimerLinkMessage"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetTimerLinkActRetry"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetPlanCapacity"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetActPriority"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetType"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetRowStatus"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetNi"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDescription"))
)
if mibBuilder.loadTexts:
    cItpSpLinksetGroup.setStatus("deprecated")

cItpSpLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 4)
)
cItpSpLinkGroup.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpLinkDescription"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkType"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkifIndex"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkSctpAssociation"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3PacketsRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3PacketsSent"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3BytesRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3BytesSent"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T04E"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T04N"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T04"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T08"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T10"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T11"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T12"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T13"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T14"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T15"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T16"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T17"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T18"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T19"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T20"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T21"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T22"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T23"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T24"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T25"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T26"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T27"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T28"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T29"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T30"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T31"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T32"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T33"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T34"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTimerLinkTest"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTimerLinkMessage"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTimerLinkActRetry"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkXmitQueueDepth"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkXmitQueueDepthHigh"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkXmitQueueDepthHighRT"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionAbate1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionAbate2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionAbate3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionOnset1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionOnset2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionOnset3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkSigLinkTest"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E4"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E5"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E6"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E7"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E8"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E9"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E10"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E11"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E5"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E6"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E7"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E9"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E10"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E15"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E16"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E18"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3PacketsRetrans"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3BytesRetrans"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E6"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E7"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E10L1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E10L2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E10L3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E11L1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E11L2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E11L3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPType1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPType2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPType3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPType4"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPAddr1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPAddr2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPAddr3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPAddr4"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkLocalPort"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkRemotePort"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQosClass"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkRowStatus"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkStateReason"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkDisplayName"))
)
if mibBuilder.loadTexts:
    cItpSpLinkGroup.setStatus("deprecated")

cItpSpNotificationsEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 5)
)
cItpSpNotificationsEnableGroup.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpLsStateChangeNotifEnabled"),
        ("CISCO-ITP-SP-MIB", "cItpSpLnkStateChangeNotifEnabled"),
        ("CISCO-ITP-SP-MIB", "cItpSpCongestionNotifEnabled"))
)
if mibBuilder.loadTexts:
    cItpSpNotificationsEnableGroup.setStatus("deprecated")

cItpSpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 7)
)
cItpSpStatsGroup.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpDistSccpUnseq"),
        ("CISCO-ITP-SP-MIB", "cItpSpSummaryRoutingException"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetVariant"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkDroppedPkts"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTransmittedLssu"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkReceivedLssu"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkProtocolDetails"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkLsacState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTsrcState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTcocState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTcocLocalBSNT"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTcocRemoteBSNT"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTcbcState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkReceivedSIB"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTransmittedSIB"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT04"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkOMAERMCount"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkOMAERMFailCount"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkOMSURMCount"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkOMSURMFailCount"))
)
if mibBuilder.loadTexts:
    cItpSpStatsGroup.setStatus("deprecated")

cItpSpScalarsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 8)
)
cItpSpScalarsGroupRev2.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpVariant"),
        ("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-SP-MIB", "cItpSpDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpDescription"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T04E"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T04N"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp2T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T04"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T08"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T10"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T11"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T12"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T13"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T14"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T15"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T16"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T17"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T18"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T19"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T20"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T21"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T22"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T23"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T24"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T25"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T26"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T27"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T28"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T29"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T30"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T31"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T32"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T33"),
        ("CISCO-ITP-SP-MIB", "cItpSpMtp3T34"),
        ("CISCO-ITP-SP-MIB", "cItpSpTimerLinkTest"),
        ("CISCO-ITP-SP-MIB", "cItpSpTimerLinkMessage"),
        ("CISCO-ITP-SP-MIB", "cItpSpTimerLinkActRetry"),
        ("CISCO-ITP-SP-MIB", "cItpSpTFR"),
        ("CISCO-ITP-SP-MIB", "cItpSpCongestionsLevels"),
        ("CISCO-ITP-SP-MIB", "cItpSpFastRestart"),
        ("CISCO-ITP-SP-MIB", "cItpSpDistSccpUnseq"),
        ("CISCO-ITP-SP-MIB", "cItpSpSummaryRoutingException"),
        ("CISCO-ITP-SP-MIB", "cItpSpUtilSampleInterval"),
        ("CISCO-ITP-SP-MIB", "cItpSpUtilThreshold"),
        ("CISCO-ITP-SP-MIB", "cItpSpUtilAbateDelta"))
)
if mibBuilder.loadTexts:
    cItpSpScalarsGroupRev2.setStatus("deprecated")

cItpSpLinksetGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 9)
)
cItpSpLinksetGroupRev2.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpLinksetSourcePointCode"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSourceDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAdjacentPointCode"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetInboundAcl"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetOutboundAcl"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSnmmRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSntmRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare2RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSccpRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetTupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetIsupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDupcRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDupfRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetBisupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSisupRTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare11RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare12RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare13RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare14RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSpare15RTN"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAccountingEnabled"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetNumLinks"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDurationInService"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDurationOutService"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T04E"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T04N"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp2T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T04"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T08"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T10"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T11"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T12"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T13"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T14"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T15"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T16"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T17"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T18"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T19"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T20"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T21"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T22"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T23"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T24"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T25"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T26"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T27"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T28"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T29"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T30"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T31"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T32"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T33"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetMtp3T34"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetTimerLinkTest"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetTimerLinkMessage"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetTimerLinkActRetry"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetActPriority"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetType"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetRowStatus"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetNi"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDescription"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetVariant"))
)
if mibBuilder.loadTexts:
    cItpSpLinksetGroupRev2.setStatus("deprecated")

cItpSpLinkGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 10)
)
cItpSpLinkGroupRev2.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpLinkDescription"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkType"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkifIndex"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkSctpAssociation"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3PacketsRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3PacketsSent"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3BytesRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3BytesSent"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T04E"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T04N"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T04"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T08"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T10"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T11"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T12"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T13"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T14"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T15"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T16"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T17"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T18"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T19"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T20"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T21"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T22"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T23"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T24"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T25"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T26"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T27"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T28"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T29"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T30"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T31"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T32"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T33"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3T34"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTimerLinkTest"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTimerLinkMessage"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTimerLinkActRetry"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkXmitQueueDepth"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkXmitQueueDepthHigh"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkXmitQueueDepthHighRT"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionAbate1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionAbate2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionAbate3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionOnset1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionOnset2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionOnset3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkSigLinkTest"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E4"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E5"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E6"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E7"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E8"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E9"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E10"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T1E11"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E5"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E6"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E7"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E9"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E10"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E15"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E16"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T2E18"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3PacketsRetrans"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp3BytesRetrans"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E6"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E7"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E10L1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E10L2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E10L3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E11L1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E11L2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQ752T3E11L3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPType1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPType2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPType3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPType4"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPAddr1"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPAddr2"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPAddr3"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkIPAddr4"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkLocalPort"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkRemotePort"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkQosClass"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkRowStatus"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkStateReason"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkDroppedPkts"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTransmittedLssu"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkReceivedLssu"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkProtocolDetails"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkLsacState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTsrcState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTcocState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTcocLocalBSNT"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTcocRemoteBSNT"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTcbcState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkReceivedSIB"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkTransmittedSIB"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT01"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT02"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT03"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT04"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT05"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT06"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkMtp2ExpiredT07"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkOMAERMCount"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkOMAERMFailCount"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkOMSURMCount"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkOMSURMFailCount"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkPlanCapacityRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilThresholdRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilizationRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilStateRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkL2BytesRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkPlanCapacitySent"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilThresholdSent"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilizationSent"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilStateSent"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkL2BytesSent"))
)
if mibBuilder.loadTexts:
    cItpSpLinkGroupRev2.setStatus("deprecated")

cItpSpNotificationsEnableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 11)
)
cItpSpNotificationsEnableGroupRev2.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpLsStateChangeNotifEnabled"),
        ("CISCO-ITP-SP-MIB", "cItpSpLnkStateChangeNotifEnabled"),
        ("CISCO-ITP-SP-MIB", "cItpSpCongestionNotifEnabled"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilNotifEnabled"))
)
if mibBuilder.loadTexts:
    cItpSpNotificationsEnableGroupRev2.setStatus("deprecated")


# Notification objects

cItpSpLinksetStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 0, 0, 1)
)
cItpSpLinksetStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSourceDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAdjacentDisplayPC"))
)
if mibBuilder.loadTexts:
    cItpSpLinksetStateChange.setStatus(
        "deprecated"
    )

cItpSpLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 0, 0, 2)
)
cItpSpLinkStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSourceDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkStateReason"))
)
if mibBuilder.loadTexts:
    cItpSpLinkStateChange.setStatus(
        "deprecated"
    )

cItpSpCongestionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 0, 0, 3)
)
cItpSpCongestionChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkCongestionState"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSourceDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAdjacentDisplayPC"))
)
if mibBuilder.loadTexts:
    cItpSpCongestionChange.setStatus(
        "deprecated"
    )

cItpSpLinkRcvdUtilChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 0, 0, 4)
)
cItpSpLinkRcvdUtilChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilStateRcvd"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSourceDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilizationRcvd"))
)
if mibBuilder.loadTexts:
    cItpSpLinkRcvdUtilChange.setStatus(
        "deprecated"
    )

cItpSpLinkSentUtilChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 0, 0, 5)
)
cItpSpLinkSentUtilChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilStateSent"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkDisplayName"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetSourceDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkUtilizationSent"))
)
if mibBuilder.loadTexts:
    cItpSpLinkSentUtilChange.setStatus(
        "deprecated"
    )


# Notifications groups

cItpSpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 6)
)
cItpSpNotificationsGroup.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpLinksetStateChange"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkStateChange"),
        ("CISCO-ITP-SP-MIB", "cItpSpCongestionChange"))
)
if mibBuilder.loadTexts:
    cItpSpNotificationsGroup.setStatus(
        "deprecated"
    )

cItpSpNotificationsGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 2, 12)
)
cItpSpNotificationsGroupRev2.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpLinksetStateChange"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkStateChange"),
        ("CISCO-ITP-SP-MIB", "cItpSpCongestionChange"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkRcvdUtilChange"),
        ("CISCO-ITP-SP-MIB", "cItpSpLinkSentUtilChange"))
)
if mibBuilder.loadTexts:
    cItpSpNotificationsGroupRev2.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

cItpSpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cItpSpMIBCompliance.setStatus(
        "deprecated"
    )

cItpSpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cItpSpMIBComplianceRev1.setStatus(
        "deprecated"
    )

cItpSpMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 232, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cItpSpMIBComplianceRev2.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-SP-MIB",
    **{"CItpSpSequenceNumber": CItpSpSequenceNumber,
       "CItpSpSampleInterval": CItpSpSampleInterval,
       "CItpSpPercentThreshold": CItpSpPercentThreshold,
       "CItpSpLinkUtilization": CItpSpLinkUtilization,
       "CItpSpLinkCapacity": CItpSpLinkCapacity,
       "CItpSpLinkUtilizationState": CItpSpLinkUtilizationState,
       "ciscoItpSpMIB": ciscoItpSpMIB,
       "cItpSpMIBNotifs": cItpSpMIBNotifs,
       "cItpSpNotifications": cItpSpNotifications,
       "cItpSpLinksetStateChange": cItpSpLinksetStateChange,
       "cItpSpLinkStateChange": cItpSpLinkStateChange,
       "cItpSpCongestionChange": cItpSpCongestionChange,
       "cItpSpLinkRcvdUtilChange": cItpSpLinkRcvdUtilChange,
       "cItpSpLinkSentUtilChange": cItpSpLinkSentUtilChange,
       "cItpSpMIBObjects": cItpSpMIBObjects,
       "cItpSpScalars": cItpSpScalars,
       "cItpSpVariant": cItpSpVariant,
       "cItpSpCLLICode": cItpSpCLLICode,
       "cItpSpDisplayName": cItpSpDisplayName,
       "cItpSpDescription": cItpSpDescription,
       "cItpSpMtp2T01": cItpSpMtp2T01,
       "cItpSpMtp2T02": cItpSpMtp2T02,
       "cItpSpMtp2T03": cItpSpMtp2T03,
       "cItpSpMtp2T04E": cItpSpMtp2T04E,
       "cItpSpMtp2T04N": cItpSpMtp2T04N,
       "cItpSpMtp2T05": cItpSpMtp2T05,
       "cItpSpMtp2T06": cItpSpMtp2T06,
       "cItpSpMtp2T07": cItpSpMtp2T07,
       "cItpSpMtp3T01": cItpSpMtp3T01,
       "cItpSpMtp3T02": cItpSpMtp3T02,
       "cItpSpMtp3T03": cItpSpMtp3T03,
       "cItpSpMtp3T04": cItpSpMtp3T04,
       "cItpSpMtp3T05": cItpSpMtp3T05,
       "cItpSpMtp3T06": cItpSpMtp3T06,
       "cItpSpMtp3T07": cItpSpMtp3T07,
       "cItpSpMtp3T08": cItpSpMtp3T08,
       "cItpSpMtp3T10": cItpSpMtp3T10,
       "cItpSpMtp3T11": cItpSpMtp3T11,
       "cItpSpMtp3T12": cItpSpMtp3T12,
       "cItpSpMtp3T13": cItpSpMtp3T13,
       "cItpSpMtp3T14": cItpSpMtp3T14,
       "cItpSpMtp3T15": cItpSpMtp3T15,
       "cItpSpMtp3T16": cItpSpMtp3T16,
       "cItpSpMtp3T17": cItpSpMtp3T17,
       "cItpSpMtp3T18": cItpSpMtp3T18,
       "cItpSpMtp3T19": cItpSpMtp3T19,
       "cItpSpMtp3T20": cItpSpMtp3T20,
       "cItpSpMtp3T21": cItpSpMtp3T21,
       "cItpSpMtp3T22": cItpSpMtp3T22,
       "cItpSpMtp3T23": cItpSpMtp3T23,
       "cItpSpMtp3T24": cItpSpMtp3T24,
       "cItpSpMtp3T25": cItpSpMtp3T25,
       "cItpSpMtp3T26": cItpSpMtp3T26,
       "cItpSpMtp3T27": cItpSpMtp3T27,
       "cItpSpMtp3T28": cItpSpMtp3T28,
       "cItpSpMtp3T29": cItpSpMtp3T29,
       "cItpSpMtp3T30": cItpSpMtp3T30,
       "cItpSpMtp3T31": cItpSpMtp3T31,
       "cItpSpMtp3T32": cItpSpMtp3T32,
       "cItpSpMtp3T33": cItpSpMtp3T33,
       "cItpSpMtp3T34": cItpSpMtp3T34,
       "cItpSpTimerLinkTest": cItpSpTimerLinkTest,
       "cItpSpTimerLinkMessage": cItpSpTimerLinkMessage,
       "cItpSpTimerLinkActRetry": cItpSpTimerLinkActRetry,
       "cItpSpTFR": cItpSpTFR,
       "cItpSpCongestionsLevels": cItpSpCongestionsLevels,
       "cItpSpFastRestart": cItpSpFastRestart,
       "cItpSpDistSccpUnseq": cItpSpDistSccpUnseq,
       "cItpSpSummaryRoutingException": cItpSpSummaryRoutingException,
       "cItpSpUtilSampleInterval": cItpSpUtilSampleInterval,
       "cItpSpUtilThreshold": cItpSpUtilThreshold,
       "cItpSpUtilAbateDelta": cItpSpUtilAbateDelta,
       "cItpSpPointCode": cItpSpPointCode,
       "cItpSpPointCodeTable": cItpSpPointCodeTable,
       "cItpSpPointCodeTableEntry": cItpSpPointCodeTableEntry,
       "cItpSpPointCodeNi": cItpSpPointCodeNi,
       "cItpSpPointCodeBin": cItpSpPointCodeBin,
       "cItpSpPointCodeType": cItpSpPointCodeType,
       "cItpSpPointCodeDisplay": cItpSpPointCodeDisplay,
       "cItpSpPointCodeRowStatus": cItpSpPointCodeRowStatus,
       "cItpSpLinkset": cItpSpLinkset,
       "cItpSpLinksetTable": cItpSpLinksetTable,
       "cItpSpLinksetTableEntry": cItpSpLinksetTableEntry,
       "cItpSpLinksetName": cItpSpLinksetName,
       "cItpSpLinksetSourcePointCode": cItpSpLinksetSourcePointCode,
       "cItpSpLinksetSourceDisplayPC": cItpSpLinksetSourceDisplayPC,
       "cItpSpLinksetAdjacentPointCode": cItpSpLinksetAdjacentPointCode,
       "cItpSpLinksetAdjacentDisplayPC": cItpSpLinksetAdjacentDisplayPC,
       "cItpSpLinksetState": cItpSpLinksetState,
       "cItpSpLinksetInboundAcl": cItpSpLinksetInboundAcl,
       "cItpSpLinksetOutboundAcl": cItpSpLinksetOutboundAcl,
       "cItpSpLinksetSnmmRTN": cItpSpLinksetSnmmRTN,
       "cItpSpLinksetSntmRTN": cItpSpLinksetSntmRTN,
       "cItpSpLinksetSpare2RTN": cItpSpLinksetSpare2RTN,
       "cItpSpLinksetSccpRTN": cItpSpLinksetSccpRTN,
       "cItpSpLinksetTupRTN": cItpSpLinksetTupRTN,
       "cItpSpLinksetIsupRTN": cItpSpLinksetIsupRTN,
       "cItpSpLinksetDupcRTN": cItpSpLinksetDupcRTN,
       "cItpSpLinksetDupfRTN": cItpSpLinksetDupfRTN,
       "cItpSpLinksetMtupRTN": cItpSpLinksetMtupRTN,
       "cItpSpLinksetBisupRTN": cItpSpLinksetBisupRTN,
       "cItpSpLinksetSisupRTN": cItpSpLinksetSisupRTN,
       "cItpSpLinksetSpare11RTN": cItpSpLinksetSpare11RTN,
       "cItpSpLinksetSpare12RTN": cItpSpLinksetSpare12RTN,
       "cItpSpLinksetSpare13RTN": cItpSpLinksetSpare13RTN,
       "cItpSpLinksetSpare14RTN": cItpSpLinksetSpare14RTN,
       "cItpSpLinksetSpare15RTN": cItpSpLinksetSpare15RTN,
       "cItpSpLinksetAccountingEnabled": cItpSpLinksetAccountingEnabled,
       "cItpSpLinksetNumLinks": cItpSpLinksetNumLinks,
       "cItpSpLinksetDurationInService": cItpSpLinksetDurationInService,
       "cItpSpLinksetDurationOutService": cItpSpLinksetDurationOutService,
       "cItpSpLinksetMtp2T01": cItpSpLinksetMtp2T01,
       "cItpSpLinksetMtp2T02": cItpSpLinksetMtp2T02,
       "cItpSpLinksetMtp2T03": cItpSpLinksetMtp2T03,
       "cItpSpLinksetMtp2T04E": cItpSpLinksetMtp2T04E,
       "cItpSpLinksetMtp2T04N": cItpSpLinksetMtp2T04N,
       "cItpSpLinksetMtp2T05": cItpSpLinksetMtp2T05,
       "cItpSpLinksetMtp2T06": cItpSpLinksetMtp2T06,
       "cItpSpLinksetMtp2T07": cItpSpLinksetMtp2T07,
       "cItpSpLinksetMtp3T01": cItpSpLinksetMtp3T01,
       "cItpSpLinksetMtp3T02": cItpSpLinksetMtp3T02,
       "cItpSpLinksetMtp3T03": cItpSpLinksetMtp3T03,
       "cItpSpLinksetMtp3T04": cItpSpLinksetMtp3T04,
       "cItpSpLinksetMtp3T05": cItpSpLinksetMtp3T05,
       "cItpSpLinksetMtp3T06": cItpSpLinksetMtp3T06,
       "cItpSpLinksetMtp3T07": cItpSpLinksetMtp3T07,
       "cItpSpLinksetMtp3T08": cItpSpLinksetMtp3T08,
       "cItpSpLinksetMtp3T10": cItpSpLinksetMtp3T10,
       "cItpSpLinksetMtp3T11": cItpSpLinksetMtp3T11,
       "cItpSpLinksetMtp3T12": cItpSpLinksetMtp3T12,
       "cItpSpLinksetMtp3T13": cItpSpLinksetMtp3T13,
       "cItpSpLinksetMtp3T14": cItpSpLinksetMtp3T14,
       "cItpSpLinksetMtp3T15": cItpSpLinksetMtp3T15,
       "cItpSpLinksetMtp3T16": cItpSpLinksetMtp3T16,
       "cItpSpLinksetMtp3T17": cItpSpLinksetMtp3T17,
       "cItpSpLinksetMtp3T18": cItpSpLinksetMtp3T18,
       "cItpSpLinksetMtp3T19": cItpSpLinksetMtp3T19,
       "cItpSpLinksetMtp3T20": cItpSpLinksetMtp3T20,
       "cItpSpLinksetMtp3T21": cItpSpLinksetMtp3T21,
       "cItpSpLinksetMtp3T22": cItpSpLinksetMtp3T22,
       "cItpSpLinksetMtp3T23": cItpSpLinksetMtp3T23,
       "cItpSpLinksetMtp3T24": cItpSpLinksetMtp3T24,
       "cItpSpLinksetMtp3T25": cItpSpLinksetMtp3T25,
       "cItpSpLinksetMtp3T26": cItpSpLinksetMtp3T26,
       "cItpSpLinksetMtp3T27": cItpSpLinksetMtp3T27,
       "cItpSpLinksetMtp3T28": cItpSpLinksetMtp3T28,
       "cItpSpLinksetMtp3T29": cItpSpLinksetMtp3T29,
       "cItpSpLinksetMtp3T30": cItpSpLinksetMtp3T30,
       "cItpSpLinksetMtp3T31": cItpSpLinksetMtp3T31,
       "cItpSpLinksetMtp3T32": cItpSpLinksetMtp3T32,
       "cItpSpLinksetMtp3T33": cItpSpLinksetMtp3T33,
       "cItpSpLinksetMtp3T34": cItpSpLinksetMtp3T34,
       "cItpSpLinksetTimerLinkTest": cItpSpLinksetTimerLinkTest,
       "cItpSpLinksetTimerLinkMessage": cItpSpLinksetTimerLinkMessage,
       "cItpSpLinksetTimerLinkActRetry": cItpSpLinksetTimerLinkActRetry,
       "cItpSpLinksetPlanCapacity": cItpSpLinksetPlanCapacity,
       "cItpSpLinksetActPriority": cItpSpLinksetActPriority,
       "cItpSpLinksetType": cItpSpLinksetType,
       "cItpSpLinksetRowStatus": cItpSpLinksetRowStatus,
       "cItpSpLinksetNi": cItpSpLinksetNi,
       "cItpSpLinksetDisplayName": cItpSpLinksetDisplayName,
       "cItpSpLinksetDescription": cItpSpLinksetDescription,
       "cItpSpLinksetVariant": cItpSpLinksetVariant,
       "cItpSpLink": cItpSpLink,
       "cItpSpLinkTable": cItpSpLinkTable,
       "cItpSpLinkTableEntry": cItpSpLinkTableEntry,
       "cItpSpLinkSlc": cItpSpLinkSlc,
       "cItpSpLinkDescription": cItpSpLinkDescription,
       "cItpSpLinkState": cItpSpLinkState,
       "cItpSpLinkType": cItpSpLinkType,
       "cItpSpLinkifIndex": cItpSpLinkifIndex,
       "cItpSpLinkSctpAssociation": cItpSpLinkSctpAssociation,
       "cItpSpLinkMtp3PacketsRcvd": cItpSpLinkMtp3PacketsRcvd,
       "cItpSpLinkMtp3PacketsSent": cItpSpLinkMtp3PacketsSent,
       "cItpSpLinkMtp3BytesRcvd": cItpSpLinkMtp3BytesRcvd,
       "cItpSpLinkMtp3BytesSent": cItpSpLinkMtp3BytesSent,
       "cItpSpLinkMtp2T01": cItpSpLinkMtp2T01,
       "cItpSpLinkMtp2T02": cItpSpLinkMtp2T02,
       "cItpSpLinkMtp2T03": cItpSpLinkMtp2T03,
       "cItpSpLinkMtp2T04E": cItpSpLinkMtp2T04E,
       "cItpSpLinkMtp2T04N": cItpSpLinkMtp2T04N,
       "cItpSpLinkMtp2T05": cItpSpLinkMtp2T05,
       "cItpSpLinkMtp2T06": cItpSpLinkMtp2T06,
       "cItpSpLinkMtp2T07": cItpSpLinkMtp2T07,
       "cItpSpLinkMtp3T01": cItpSpLinkMtp3T01,
       "cItpSpLinkMtp3T02": cItpSpLinkMtp3T02,
       "cItpSpLinkMtp3T03": cItpSpLinkMtp3T03,
       "cItpSpLinkMtp3T04": cItpSpLinkMtp3T04,
       "cItpSpLinkMtp3T05": cItpSpLinkMtp3T05,
       "cItpSpLinkMtp3T06": cItpSpLinkMtp3T06,
       "cItpSpLinkMtp3T07": cItpSpLinkMtp3T07,
       "cItpSpLinkMtp3T08": cItpSpLinkMtp3T08,
       "cItpSpLinkMtp3T10": cItpSpLinkMtp3T10,
       "cItpSpLinkMtp3T11": cItpSpLinkMtp3T11,
       "cItpSpLinkMtp3T12": cItpSpLinkMtp3T12,
       "cItpSpLinkMtp3T13": cItpSpLinkMtp3T13,
       "cItpSpLinkMtp3T14": cItpSpLinkMtp3T14,
       "cItpSpLinkMtp3T15": cItpSpLinkMtp3T15,
       "cItpSpLinkMtp3T16": cItpSpLinkMtp3T16,
       "cItpSpLinkMtp3T17": cItpSpLinkMtp3T17,
       "cItpSpLinkMtp3T18": cItpSpLinkMtp3T18,
       "cItpSpLinkMtp3T19": cItpSpLinkMtp3T19,
       "cItpSpLinkMtp3T20": cItpSpLinkMtp3T20,
       "cItpSpLinkMtp3T21": cItpSpLinkMtp3T21,
       "cItpSpLinkMtp3T22": cItpSpLinkMtp3T22,
       "cItpSpLinkMtp3T23": cItpSpLinkMtp3T23,
       "cItpSpLinkMtp3T24": cItpSpLinkMtp3T24,
       "cItpSpLinkMtp3T25": cItpSpLinkMtp3T25,
       "cItpSpLinkMtp3T26": cItpSpLinkMtp3T26,
       "cItpSpLinkMtp3T27": cItpSpLinkMtp3T27,
       "cItpSpLinkMtp3T28": cItpSpLinkMtp3T28,
       "cItpSpLinkMtp3T29": cItpSpLinkMtp3T29,
       "cItpSpLinkMtp3T30": cItpSpLinkMtp3T30,
       "cItpSpLinkMtp3T31": cItpSpLinkMtp3T31,
       "cItpSpLinkMtp3T32": cItpSpLinkMtp3T32,
       "cItpSpLinkMtp3T33": cItpSpLinkMtp3T33,
       "cItpSpLinkMtp3T34": cItpSpLinkMtp3T34,
       "cItpSpLinkTimerLinkTest": cItpSpLinkTimerLinkTest,
       "cItpSpLinkTimerLinkMessage": cItpSpLinkTimerLinkMessage,
       "cItpSpLinkTimerLinkActRetry": cItpSpLinkTimerLinkActRetry,
       "cItpSpLinkXmitQueueDepth": cItpSpLinkXmitQueueDepth,
       "cItpSpLinkXmitQueueDepthHigh": cItpSpLinkXmitQueueDepthHigh,
       "cItpSpLinkXmitQueueDepthHighRT": cItpSpLinkXmitQueueDepthHighRT,
       "cItpSpLinkCongestionState": cItpSpLinkCongestionState,
       "cItpSpLinkCongestionAbate1": cItpSpLinkCongestionAbate1,
       "cItpSpLinkCongestionAbate2": cItpSpLinkCongestionAbate2,
       "cItpSpLinkCongestionAbate3": cItpSpLinkCongestionAbate3,
       "cItpSpLinkCongestionOnset1": cItpSpLinkCongestionOnset1,
       "cItpSpLinkCongestionOnset2": cItpSpLinkCongestionOnset2,
       "cItpSpLinkCongestionOnset3": cItpSpLinkCongestionOnset3,
       "cItpSpLinkSigLinkTest": cItpSpLinkSigLinkTest,
       "cItpSpLinkQ752T1E1": cItpSpLinkQ752T1E1,
       "cItpSpLinkQ752T1E2": cItpSpLinkQ752T1E2,
       "cItpSpLinkQ752T1E3": cItpSpLinkQ752T1E3,
       "cItpSpLinkQ752T1E4": cItpSpLinkQ752T1E4,
       "cItpSpLinkQ752T1E5": cItpSpLinkQ752T1E5,
       "cItpSpLinkQ752T1E6": cItpSpLinkQ752T1E6,
       "cItpSpLinkQ752T1E7": cItpSpLinkQ752T1E7,
       "cItpSpLinkQ752T1E8": cItpSpLinkQ752T1E8,
       "cItpSpLinkQ752T1E9": cItpSpLinkQ752T1E9,
       "cItpSpLinkQ752T1E10": cItpSpLinkQ752T1E10,
       "cItpSpLinkQ752T1E11": cItpSpLinkQ752T1E11,
       "cItpSpLinkQ752T2E1": cItpSpLinkQ752T2E1,
       "cItpSpLinkQ752T2E5": cItpSpLinkQ752T2E5,
       "cItpSpLinkQ752T2E6": cItpSpLinkQ752T2E6,
       "cItpSpLinkQ752T2E7": cItpSpLinkQ752T2E7,
       "cItpSpLinkQ752T2E9": cItpSpLinkQ752T2E9,
       "cItpSpLinkQ752T2E10": cItpSpLinkQ752T2E10,
       "cItpSpLinkQ752T2E15": cItpSpLinkQ752T2E15,
       "cItpSpLinkQ752T2E16": cItpSpLinkQ752T2E16,
       "cItpSpLinkQ752T2E18": cItpSpLinkQ752T2E18,
       "cItpSpLinkMtp3PacketsRetrans": cItpSpLinkMtp3PacketsRetrans,
       "cItpSpLinkMtp3BytesRetrans": cItpSpLinkMtp3BytesRetrans,
       "cItpSpLinkQ752T3E6": cItpSpLinkQ752T3E6,
       "cItpSpLinkQ752T3E7": cItpSpLinkQ752T3E7,
       "cItpSpLinkQ752T3E10L1": cItpSpLinkQ752T3E10L1,
       "cItpSpLinkQ752T3E10L2": cItpSpLinkQ752T3E10L2,
       "cItpSpLinkQ752T3E10L3": cItpSpLinkQ752T3E10L3,
       "cItpSpLinkQ752T3E11L1": cItpSpLinkQ752T3E11L1,
       "cItpSpLinkQ752T3E11L2": cItpSpLinkQ752T3E11L2,
       "cItpSpLinkQ752T3E11L3": cItpSpLinkQ752T3E11L3,
       "cItpSpLinkIPType1": cItpSpLinkIPType1,
       "cItpSpLinkIPType2": cItpSpLinkIPType2,
       "cItpSpLinkIPType3": cItpSpLinkIPType3,
       "cItpSpLinkIPType4": cItpSpLinkIPType4,
       "cItpSpLinkIPAddr1": cItpSpLinkIPAddr1,
       "cItpSpLinkIPAddr2": cItpSpLinkIPAddr2,
       "cItpSpLinkIPAddr3": cItpSpLinkIPAddr3,
       "cItpSpLinkIPAddr4": cItpSpLinkIPAddr4,
       "cItpSpLinkLocalPort": cItpSpLinkLocalPort,
       "cItpSpLinkRemotePort": cItpSpLinkRemotePort,
       "cItpSpLinkQosClass": cItpSpLinkQosClass,
       "cItpSpLinkRowStatus": cItpSpLinkRowStatus,
       "cItpSpLinkStateReason": cItpSpLinkStateReason,
       "cItpSpLinkDisplayName": cItpSpLinkDisplayName,
       "cItpSpLinkDroppedPkts": cItpSpLinkDroppedPkts,
       "cItpSpLinkTransmittedLssu": cItpSpLinkTransmittedLssu,
       "cItpSpLinkReceivedLssu": cItpSpLinkReceivedLssu,
       "cItpSpLinkProtocolDetails": cItpSpLinkProtocolDetails,
       "cItpSpLinkLsacState": cItpSpLinkLsacState,
       "cItpSpLinkTsrcState": cItpSpLinkTsrcState,
       "cItpSpLinkTcocState": cItpSpLinkTcocState,
       "cItpSpLinkTcocLocalBSNT": cItpSpLinkTcocLocalBSNT,
       "cItpSpLinkTcocRemoteBSNT": cItpSpLinkTcocRemoteBSNT,
       "cItpSpLinkTcbcState": cItpSpLinkTcbcState,
       "cItpSpLinkReceivedSIB": cItpSpLinkReceivedSIB,
       "cItpSpLinkTransmittedSIB": cItpSpLinkTransmittedSIB,
       "cItpSpLinkMtp2ExpiredT01": cItpSpLinkMtp2ExpiredT01,
       "cItpSpLinkMtp2ExpiredT02": cItpSpLinkMtp2ExpiredT02,
       "cItpSpLinkMtp2ExpiredT03": cItpSpLinkMtp2ExpiredT03,
       "cItpSpLinkMtp2ExpiredT04": cItpSpLinkMtp2ExpiredT04,
       "cItpSpLinkMtp2ExpiredT05": cItpSpLinkMtp2ExpiredT05,
       "cItpSpLinkMtp2ExpiredT06": cItpSpLinkMtp2ExpiredT06,
       "cItpSpLinkMtp2ExpiredT07": cItpSpLinkMtp2ExpiredT07,
       "cItpSpLinkOMAERMCount": cItpSpLinkOMAERMCount,
       "cItpSpLinkOMAERMFailCount": cItpSpLinkOMAERMFailCount,
       "cItpSpLinkOMSURMCount": cItpSpLinkOMSURMCount,
       "cItpSpLinkOMSURMFailCount": cItpSpLinkOMSURMFailCount,
       "cItpSpLinkPlanCapacityRcvd": cItpSpLinkPlanCapacityRcvd,
       "cItpSpLinkUtilThresholdRcvd": cItpSpLinkUtilThresholdRcvd,
       "cItpSpLinkUtilizationRcvd": cItpSpLinkUtilizationRcvd,
       "cItpSpLinkUtilStateRcvd": cItpSpLinkUtilStateRcvd,
       "cItpSpLinkL2BytesRcvd": cItpSpLinkL2BytesRcvd,
       "cItpSpLinkPlanCapacitySent": cItpSpLinkPlanCapacitySent,
       "cItpSpLinkUtilThresholdSent": cItpSpLinkUtilThresholdSent,
       "cItpSpLinkUtilizationSent": cItpSpLinkUtilizationSent,
       "cItpSpLinkUtilStateSent": cItpSpLinkUtilStateSent,
       "cItpSpLinkL2BytesSent": cItpSpLinkL2BytesSent,
       "cItpSpNotificationsEnable": cItpSpNotificationsEnable,
       "cItpSpLsStateChangeNotifEnabled": cItpSpLsStateChangeNotifEnabled,
       "cItpSpLnkStateChangeNotifEnabled": cItpSpLnkStateChangeNotifEnabled,
       "cItpSpCongestionNotifEnabled": cItpSpCongestionNotifEnabled,
       "cItpSpLinkUtilNotifEnabled": cItpSpLinkUtilNotifEnabled,
       "cItpSpMIBConformance": cItpSpMIBConformance,
       "cItpSpMIBCompliances": cItpSpMIBCompliances,
       "cItpSpMIBCompliance": cItpSpMIBCompliance,
       "cItpSpMIBComplianceRev1": cItpSpMIBComplianceRev1,
       "cItpSpMIBComplianceRev2": cItpSpMIBComplianceRev2,
       "cItpSpMIBGroups": cItpSpMIBGroups,
       "cItpSpScalarsGroup": cItpSpScalarsGroup,
       "cItpSpPointCodeGroup": cItpSpPointCodeGroup,
       "cItpSpLinksetGroup": cItpSpLinksetGroup,
       "cItpSpLinkGroup": cItpSpLinkGroup,
       "cItpSpNotificationsEnableGroup": cItpSpNotificationsEnableGroup,
       "cItpSpNotificationsGroup": cItpSpNotificationsGroup,
       "cItpSpStatsGroup": cItpSpStatsGroup,
       "cItpSpScalarsGroupRev2": cItpSpScalarsGroupRev2,
       "cItpSpLinksetGroupRev2": cItpSpLinksetGroupRev2,
       "cItpSpLinkGroupRev2": cItpSpLinkGroupRev2,
       "cItpSpNotificationsEnableGroupRev2": cItpSpNotificationsEnableGroupRev2,
       "cItpSpNotificationsGroupRev2": cItpSpNotificationsGroupRev2}
)
