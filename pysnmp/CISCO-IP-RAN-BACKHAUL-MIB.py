# SNMP MIB module (CISCO-IP-RAN-BACKHAUL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-RAN-BACKHAUL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:45 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifDescr",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIpRanBackHaulMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483)
)
ciscoIpRanBackHaulMIB.setRevisions(
        ("2010-03-24 00:00",
         "2007-05-30 00:00",
         "2006-08-25 00:00",
         "2005-10-18 00:00",
         "2005-09-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CirbhAlarmState(Integer32, TextualConvention):
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
        *(("blue", 1),
          ("green", 2),
          ("red", 3),
          ("unavailable", 5),
          ("yellow", 4))
    )



class CirbhBackHaulUtilization(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class CirbhBackHaulUtilizationState(Integer32, TextualConvention):
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
        *(("acceptable", 1),
          ("overloaded", 3),
          ("warning", 2))
    )



class CirbhCommpressInterfaceRate(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CirbhConnectGsmState(Integer32, TextualConvention):
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
        *(("ackConnect", 6),
          ("connected", 1),
          ("connectedCheck", 7),
          ("connectedRej", 5),
          ("disconnected", 2),
          ("recConnect", 4),
          ("sendConnect", 3))
    )



class CirbhConnectUmtsState(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ackReceived", 8),
          ("ackSent", 9),
          ("closed", 3),
          ("closing", 5),
          ("connectSent", 7),
          ("init", 1),
          ("open", 10),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )



class CirbhHistoryIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CirbhProtocol(Integer32, TextualConvention):
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
        *(("gsmAbis", 2),
          ("umtsIub", 3),
          ("undefined", 1))
    )



class CirbhRawInterfaceRate(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CirbhRedundancyState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )



class CirbhShortHaulUtilization(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CirbhTrafficDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("transmit", 2))
    )



class CirbhTrafficType(Integer32, TextualConvention):
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
        *(("all", 1),
          ("gsm", 2),
          ("umts", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIpRanBackHaulMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpRanBackHaulMIBNotifs = _CiscoIpRanBackHaulMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 0)
)
_CiscoIpRanBackHaulMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpRanBackHaulMIBObjects = _CiscoIpRanBackHaulMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1)
)
_CirbhScalars_ObjectIdentity = ObjectIdentity
cirbhScalars = _CirbhScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 1)
)


class _CirbhSnmpTrafficMode_Type(Integer32):
    """Custom type cirbhSnmpTrafficMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inBand", 2),
          ("outOfBand", 3),
          ("undefined", 1))
    )


_CirbhSnmpTrafficMode_Type.__name__ = "Integer32"
_CirbhSnmpTrafficMode_Object = MibScalar
cirbhSnmpTrafficMode = _CirbhSnmpTrafficMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 1, 1),
    _CirbhSnmpTrafficMode_Type()
)
cirbhSnmpTrafficMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhSnmpTrafficMode.setStatus("current")


class _CirbhLocation_Type(Integer32):
    """Custom type cirbhLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggSite", 2),
          ("cellSite", 3),
          ("undefined", 1))
    )


_CirbhLocation_Type.__name__ = "Integer32"
_CirbhLocation_Object = MibScalar
cirbhLocation = _CirbhLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 1, 2),
    _CirbhLocation_Type()
)
cirbhLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhLocation.setStatus("current")


class _CirbhBackHaulStatsInterval_Type(Unsigned32):
    """Custom type cirbhBackHaulStatsInterval based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_CirbhBackHaulStatsInterval_Type.__name__ = "Unsigned32"
_CirbhBackHaulStatsInterval_Object = MibScalar
cirbhBackHaulStatsInterval = _CirbhBackHaulStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 1, 3),
    _CirbhBackHaulStatsInterval_Type()
)
cirbhBackHaulStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhBackHaulStatsInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhBackHaulStatsInterval.setUnits("seconds")


class _CirbhBackHaulStatsEntries_Type(Unsigned32):
    """Custom type cirbhBackHaulStatsEntries based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 100),
    )


_CirbhBackHaulStatsEntries_Type.__name__ = "Unsigned32"
_CirbhBackHaulStatsEntries_Object = MibScalar
cirbhBackHaulStatsEntries = _CirbhBackHaulStatsEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 1, 4),
    _CirbhBackHaulStatsEntries_Type()
)
cirbhBackHaulStatsEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhBackHaulStatsEntries.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhBackHaulStatsEntries.setUnits("entries")


class _CirbhBackHaulAcceptableThreshold_Type(Unsigned32):
    """Custom type cirbhBackHaulAcceptableThreshold based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_CirbhBackHaulAcceptableThreshold_Type.__name__ = "Unsigned32"
_CirbhBackHaulAcceptableThreshold_Object = MibScalar
cirbhBackHaulAcceptableThreshold = _CirbhBackHaulAcceptableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 1, 5),
    _CirbhBackHaulAcceptableThreshold_Type()
)
cirbhBackHaulAcceptableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhBackHaulAcceptableThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhBackHaulAcceptableThreshold.setUnits("percent")


class _CirbhBackHaulWarningThreshold_Type(Unsigned32):
    """Custom type cirbhBackHaulWarningThreshold based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 100),
    )


_CirbhBackHaulWarningThreshold_Type.__name__ = "Unsigned32"
_CirbhBackHaulWarningThreshold_Object = MibScalar
cirbhBackHaulWarningThreshold = _CirbhBackHaulWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 1, 6),
    _CirbhBackHaulWarningThreshold_Type()
)
cirbhBackHaulWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhBackHaulWarningThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhBackHaulWarningThreshold.setUnits("percent")


class _CirbhBackHaulOverloadedThreshold_Type(Unsigned32):
    """Custom type cirbhBackHaulOverloadedThreshold based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_CirbhBackHaulOverloadedThreshold_Type.__name__ = "Unsigned32"
_CirbhBackHaulOverloadedThreshold_Object = MibScalar
cirbhBackHaulOverloadedThreshold = _CirbhBackHaulOverloadedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 1, 7),
    _CirbhBackHaulOverloadedThreshold_Type()
)
cirbhBackHaulOverloadedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhBackHaulOverloadedThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhBackHaulOverloadedThreshold.setUnits("percent")


class _CirbhBackHaulUtilInterval_Type(Unsigned32):
    """Custom type cirbhBackHaulUtilInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 3600),
    )


_CirbhBackHaulUtilInterval_Type.__name__ = "Unsigned32"
_CirbhBackHaulUtilInterval_Object = MibScalar
cirbhBackHaulUtilInterval = _CirbhBackHaulUtilInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 1, 8),
    _CirbhBackHaulUtilInterval_Type()
)
cirbhBackHaulUtilInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhBackHaulUtilInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhBackHaulUtilInterval.setUnits("seconds")
_CirbhObjects_ObjectIdentity = ObjectIdentity
cirbhObjects = _CirbhObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2)
)
_CirbhShortHaul_ObjectIdentity = ObjectIdentity
cirbhShortHaul = _CirbhShortHaul_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1)
)
_CirbhShortHaulInfo_ObjectIdentity = ObjectIdentity
cirbhShortHaulInfo = _CirbhShortHaulInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1)
)
_CirbhInfoTable_Object = MibTable
cirbhInfoTable = _CirbhInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cirbhInfoTable.setStatus("current")
_CirbhInfoTableEntry_Object = MibTableRow
cirbhInfoTableEntry = _CirbhInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1)
)
cirbhInfoTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhInfoTableEntry.setStatus("current")
_CirbhInfoProtocol_Type = CirbhProtocol
_CirbhInfoProtocol_Object = MibTableColumn
cirbhInfoProtocol = _CirbhInfoProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 1),
    _CirbhInfoProtocol_Type()
)
cirbhInfoProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoProtocol.setStatus("current")
_CirbhInfoLocalAddrType_Type = InetAddressType
_CirbhInfoLocalAddrType_Object = MibTableColumn
cirbhInfoLocalAddrType = _CirbhInfoLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 2),
    _CirbhInfoLocalAddrType_Type()
)
cirbhInfoLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoLocalAddrType.setStatus("current")
_CirbhInfoLocalAddr_Type = InetAddress
_CirbhInfoLocalAddr_Object = MibTableColumn
cirbhInfoLocalAddr = _CirbhInfoLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 3),
    _CirbhInfoLocalAddr_Type()
)
cirbhInfoLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoLocalAddr.setStatus("current")
_CirbhInfoLocalPortNumber_Type = InetPortNumber
_CirbhInfoLocalPortNumber_Object = MibTableColumn
cirbhInfoLocalPortNumber = _CirbhInfoLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 4),
    _CirbhInfoLocalPortNumber_Type()
)
cirbhInfoLocalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoLocalPortNumber.setStatus("current")
_CirbhInfoRemoteAddrType_Type = InetAddressType
_CirbhInfoRemoteAddrType_Object = MibTableColumn
cirbhInfoRemoteAddrType = _CirbhInfoRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 5),
    _CirbhInfoRemoteAddrType_Type()
)
cirbhInfoRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoRemoteAddrType.setStatus("current")
_CirbhInfoRemoteAddr_Type = InetAddress
_CirbhInfoRemoteAddr_Object = MibTableColumn
cirbhInfoRemoteAddr = _CirbhInfoRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 6),
    _CirbhInfoRemoteAddr_Type()
)
cirbhInfoRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoRemoteAddr.setStatus("current")
_CirbhInfoRemotePortNumber_Type = InetPortNumber
_CirbhInfoRemotePortNumber_Object = MibTableColumn
cirbhInfoRemotePortNumber = _CirbhInfoRemotePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 7),
    _CirbhInfoRemotePortNumber_Type()
)
cirbhInfoRemotePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoRemotePortNumber.setStatus("current")
_CirbhInfoAdjectSerialNum_Type = SnmpAdminString
_CirbhInfoAdjectSerialNum_Object = MibTableColumn
cirbhInfoAdjectSerialNum = _CirbhInfoAdjectSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 8),
    _CirbhInfoAdjectSerialNum_Type()
)
cirbhInfoAdjectSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoAdjectSerialNum.setStatus("current")
_CirbhInfoAdjectVendorType_Type = AutonomousType
_CirbhInfoAdjectVendorType_Object = MibTableColumn
cirbhInfoAdjectVendorType = _CirbhInfoAdjectVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 9),
    _CirbhInfoAdjectVendorType_Type()
)
cirbhInfoAdjectVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoAdjectVendorType.setStatus("current")
_CirbhInfoBackhaulRxIfIndex_Type = InterfaceIndexOrZero
_CirbhInfoBackhaulRxIfIndex_Object = MibTableColumn
cirbhInfoBackhaulRxIfIndex = _CirbhInfoBackhaulRxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 10),
    _CirbhInfoBackhaulRxIfIndex_Type()
)
cirbhInfoBackhaulRxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoBackhaulRxIfIndex.setStatus("current")
_CirbhInfoBackhaulTxIfIndex_Type = InterfaceIndexOrZero
_CirbhInfoBackhaulTxIfIndex_Object = MibTableColumn
cirbhInfoBackhaulTxIfIndex = _CirbhInfoBackhaulTxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 11),
    _CirbhInfoBackhaulTxIfIndex_Type()
)
cirbhInfoBackhaulTxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoBackhaulTxIfIndex.setStatus("current")
_CirbhInfoShBulkLastIndex_Type = CirbhHistoryIndex
_CirbhInfoShBulkLastIndex_Object = MibTableColumn
cirbhInfoShBulkLastIndex = _CirbhInfoShBulkLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 12),
    _CirbhInfoShBulkLastIndex_Type()
)
cirbhInfoShBulkLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoShBulkLastIndex.setStatus("current")
_CirbhInfoOptimizeTraffic_Type = TruthValue
_CirbhInfoOptimizeTraffic_Object = MibTableColumn
cirbhInfoOptimizeTraffic = _CirbhInfoOptimizeTraffic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 1, 1, 1, 13),
    _CirbhInfoOptimizeTraffic_Type()
)
cirbhInfoOptimizeTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhInfoOptimizeTraffic.setStatus("current")
_CirbhShortHaulAlarmInfo_ObjectIdentity = ObjectIdentity
cirbhShortHaulAlarmInfo = _CirbhShortHaulAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2)
)
_CirbhGsmAlarmTable_Object = MibTable
cirbhGsmAlarmTable = _CirbhGsmAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cirbhGsmAlarmTable.setStatus("current")
_CirbhGsmAlarmTableEntry_Object = MibTableRow
cirbhGsmAlarmTableEntry = _CirbhGsmAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 1, 1)
)
cirbhGsmAlarmTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhGsmAlarmTableEntry.setStatus("current")
_CirbhGsmAlarmConnectState_Type = CirbhConnectGsmState
_CirbhGsmAlarmConnectState_Object = MibTableColumn
cirbhGsmAlarmConnectState = _CirbhGsmAlarmConnectState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 1, 1, 1),
    _CirbhGsmAlarmConnectState_Type()
)
cirbhGsmAlarmConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmAlarmConnectState.setStatus("current")
_CirbhGsmAlarmLocalState_Type = CirbhAlarmState
_CirbhGsmAlarmLocalState_Object = MibTableColumn
cirbhGsmAlarmLocalState = _CirbhGsmAlarmLocalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 1, 1, 2),
    _CirbhGsmAlarmLocalState_Type()
)
cirbhGsmAlarmLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmAlarmLocalState.setStatus("current")
_CirbhGsmAlarmRemoteState_Type = CirbhAlarmState
_CirbhGsmAlarmRemoteState_Object = MibTableColumn
cirbhGsmAlarmRemoteState = _CirbhGsmAlarmRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 1, 1, 3),
    _CirbhGsmAlarmRemoteState_Type()
)
cirbhGsmAlarmRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmAlarmRemoteState.setStatus("current")
_CirbhGsmAlarmRedundancyState_Type = CirbhRedundancyState
_CirbhGsmAlarmRedundancyState_Object = MibTableColumn
cirbhGsmAlarmRedundancyState = _CirbhGsmAlarmRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 1, 1, 4),
    _CirbhGsmAlarmRedundancyState_Type()
)
cirbhGsmAlarmRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmAlarmRedundancyState.setStatus("current")
_CirbhUmtsConnectionTable_Object = MibTable
cirbhUmtsConnectionTable = _CirbhUmtsConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cirbhUmtsConnectionTable.setStatus("current")
_CirbhUmtsConnectionTableEntry_Object = MibTableRow
cirbhUmtsConnectionTableEntry = _CirbhUmtsConnectionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 2, 1)
)
cirbhUmtsConnectionTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhUmtsConnectionTableEntry.setStatus("current")
_CirbhUmtsConnectionState_Type = CirbhConnectUmtsState
_CirbhUmtsConnectionState_Object = MibTableColumn
cirbhUmtsConnectionState = _CirbhUmtsConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 2, 1, 1),
    _CirbhUmtsConnectionState_Type()
)
cirbhUmtsConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsConnectionState.setStatus("current")
_CirbhUmtsConnectionRedundState_Type = CirbhRedundancyState
_CirbhUmtsConnectionRedundState_Object = MibTableColumn
cirbhUmtsConnectionRedundState = _CirbhUmtsConnectionRedundState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 2, 1, 2),
    _CirbhUmtsConnectionRedundState_Type()
)
cirbhUmtsConnectionRedundState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsConnectionRedundState.setStatus("current")
_CirbhUmtsConnectionRootIfIndex_Type = InterfaceIndexOrZero
_CirbhUmtsConnectionRootIfIndex_Object = MibTableColumn
cirbhUmtsConnectionRootIfIndex = _CirbhUmtsConnectionRootIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 2, 1, 3),
    _CirbhUmtsConnectionRootIfIndex_Type()
)
cirbhUmtsConnectionRootIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsConnectionRootIfIndex.setStatus("current")
_CirbhUmtsAlarmTable_Object = MibTable
cirbhUmtsAlarmTable = _CirbhUmtsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cirbhUmtsAlarmTable.setStatus("current")
_CirbhUmtsAlarmTableEntry_Object = MibTableRow
cirbhUmtsAlarmTableEntry = _CirbhUmtsAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 3, 1)
)
cirbhUmtsAlarmTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhUmtsAlarmTableEntry.setStatus("current")
_CirbhUmtsAlarmRxLocalState_Type = CirbhAlarmState
_CirbhUmtsAlarmRxLocalState_Object = MibTableColumn
cirbhUmtsAlarmRxLocalState = _CirbhUmtsAlarmRxLocalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 3, 1, 1),
    _CirbhUmtsAlarmRxLocalState_Type()
)
cirbhUmtsAlarmRxLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsAlarmRxLocalState.setStatus("current")
_CirbhUmtsAlarmRxRemoteState_Type = CirbhAlarmState
_CirbhUmtsAlarmRxRemoteState_Object = MibTableColumn
cirbhUmtsAlarmRxRemoteState = _CirbhUmtsAlarmRxRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 3, 1, 2),
    _CirbhUmtsAlarmRxRemoteState_Type()
)
cirbhUmtsAlarmRxRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsAlarmRxRemoteState.setStatus("current")
_CirbhUmtsAlarmTxLocalState_Type = CirbhAlarmState
_CirbhUmtsAlarmTxLocalState_Object = MibTableColumn
cirbhUmtsAlarmTxLocalState = _CirbhUmtsAlarmTxLocalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 3, 1, 3),
    _CirbhUmtsAlarmTxLocalState_Type()
)
cirbhUmtsAlarmTxLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsAlarmTxLocalState.setStatus("current")
_CirbhUmtsAlarmTxRemoteState_Type = CirbhAlarmState
_CirbhUmtsAlarmTxRemoteState_Object = MibTableColumn
cirbhUmtsAlarmTxRemoteState = _CirbhUmtsAlarmTxRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 2, 3, 1, 4),
    _CirbhUmtsAlarmTxRemoteState_Type()
)
cirbhUmtsAlarmTxRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsAlarmTxRemoteState.setStatus("current")
_CirbhShortHaulStats_ObjectIdentity = ObjectIdentity
cirbhShortHaulStats = _CirbhShortHaulStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3)
)
_CirbhStatsTable_Object = MibTable
cirbhStatsTable = _CirbhStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cirbhStatsTable.setStatus("current")
_CirbhStatsTableEntry_Object = MibTableRow
cirbhStatsTableEntry = _CirbhStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 1, 1)
)
cirbhStatsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhStatsTableEntry.setStatus("current")
_CirbhStatsRcvdSamples_Type = Counter32
_CirbhStatsRcvdSamples_Object = MibTableColumn
cirbhStatsRcvdSamples = _CirbhStatsRcvdSamples_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 1, 1, 1),
    _CirbhStatsRcvdSamples_Type()
)
cirbhStatsRcvdSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsRcvdSamples.setStatus("current")
_CirbhStatsSentSamples_Type = Counter32
_CirbhStatsSentSamples_Object = MibTableColumn
cirbhStatsSentSamples = _CirbhStatsSentSamples_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 1, 1, 2),
    _CirbhStatsSentSamples_Type()
)
cirbhStatsSentSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsSentSamples.setStatus("current")
_CirbhStatsRcvdBackHaulPackets_Type = Counter32
_CirbhStatsRcvdBackHaulPackets_Object = MibTableColumn
cirbhStatsRcvdBackHaulPackets = _CirbhStatsRcvdBackHaulPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 1, 1, 3),
    _CirbhStatsRcvdBackHaulPackets_Type()
)
cirbhStatsRcvdBackHaulPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsRcvdBackHaulPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhStatsRcvdBackHaulPackets.setUnits("packets")
_CirbhStatsSentBackHaulPackets_Type = Counter32
_CirbhStatsSentBackHaulPackets_Object = MibTableColumn
cirbhStatsSentBackHaulPackets = _CirbhStatsSentBackHaulPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 1, 1, 4),
    _CirbhStatsSentBackHaulPackets_Type()
)
cirbhStatsSentBackHaulPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsSentBackHaulPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhStatsSentBackHaulPackets.setUnits("packets")
_CirbhStatsRcvdBackHaulBytes_Type = Counter32
_CirbhStatsRcvdBackHaulBytes_Object = MibTableColumn
cirbhStatsRcvdBackHaulBytes = _CirbhStatsRcvdBackHaulBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 1, 1, 5),
    _CirbhStatsRcvdBackHaulBytes_Type()
)
cirbhStatsRcvdBackHaulBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsRcvdBackHaulBytes.setStatus("current")
if mibBuilder.loadTexts:
    cirbhStatsRcvdBackHaulBytes.setUnits("bytes")
_CirbhStatsSentBackHaulBytes_Type = Counter32
_CirbhStatsSentBackHaulBytes_Object = MibTableColumn
cirbhStatsSentBackHaulBytes = _CirbhStatsSentBackHaulBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 1, 1, 6),
    _CirbhStatsSentBackHaulBytes_Type()
)
cirbhStatsSentBackHaulBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsSentBackHaulBytes.setStatus("current")
if mibBuilder.loadTexts:
    cirbhStatsSentBackHaulBytes.setUnits("bytes")
_CirbhErrorsTable_Object = MibTable
cirbhErrorsTable = _CirbhErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cirbhErrorsTable.setStatus("deprecated")
_CirbhErrorsTableEntry_Object = MibTableRow
cirbhErrorsTableEntry = _CirbhErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1)
)
cirbhErrorsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhErrorsTableEntry.setStatus("deprecated")
_CirbhErrorsBhPeerNotReadyDrops_Type = Counter32
_CirbhErrorsBhPeerNotReadyDrops_Object = MibTableColumn
cirbhErrorsBhPeerNotReadyDrops = _CirbhErrorsBhPeerNotReadyDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 1),
    _CirbhErrorsBhPeerNotReadyDrops_Type()
)
cirbhErrorsBhPeerNotReadyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhPeerNotReadyDrops.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhPeerNotReadyDrops.setUnits("packets")
_CirbhErrorsBhPeerNotActiveDrops_Type = Counter32
_CirbhErrorsBhPeerNotActiveDrops_Object = MibTableColumn
cirbhErrorsBhPeerNotActiveDrops = _CirbhErrorsBhPeerNotActiveDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 2),
    _CirbhErrorsBhPeerNotActiveDrops_Type()
)
cirbhErrorsBhPeerNotActiveDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhPeerNotActiveDrops.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhPeerNotActiveDrops.setUnits("packets")
_CirbhErrorsBhInvalidPackets_Type = Counter32
_CirbhErrorsBhInvalidPackets_Object = MibTableColumn
cirbhErrorsBhInvalidPackets = _CirbhErrorsBhInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 3),
    _CirbhErrorsBhInvalidPackets_Type()
)
cirbhErrorsBhInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhInvalidPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhInvalidPackets.setUnits("packets")
_CirbhErrorsBhLostRcvdPackets_Type = Counter32
_CirbhErrorsBhLostRcvdPackets_Object = MibTableColumn
cirbhErrorsBhLostRcvdPackets = _CirbhErrorsBhLostRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 4),
    _CirbhErrorsBhLostRcvdPackets_Type()
)
cirbhErrorsBhLostRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhLostRcvdPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhLostRcvdPackets.setUnits("packets")
_CirbhErrorsBhLostSentPackets_Type = Counter32
_CirbhErrorsBhLostSentPackets_Object = MibTableColumn
cirbhErrorsBhLostSentPackets = _CirbhErrorsBhLostSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 5),
    _CirbhErrorsBhLostSentPackets_Type()
)
cirbhErrorsBhLostSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhLostSentPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhLostSentPackets.setUnits("packets")
_CirbhErrorsBhMissedPackets_Type = Counter32
_CirbhErrorsBhMissedPackets_Object = MibTableColumn
cirbhErrorsBhMissedPackets = _CirbhErrorsBhMissedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 6),
    _CirbhErrorsBhMissedPackets_Type()
)
cirbhErrorsBhMissedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedPackets.setUnits("packets")
_CirbhErrorsBhMissedLatePackets_Type = Counter32
_CirbhErrorsBhMissedLatePackets_Object = MibTableColumn
cirbhErrorsBhMissedLatePackets = _CirbhErrorsBhMissedLatePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 7),
    _CirbhErrorsBhMissedLatePackets_Type()
)
cirbhErrorsBhMissedLatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedLatePackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedLatePackets.setUnits("packets")
_CirbhErrorsBhMissedLostPackets_Type = Counter32
_CirbhErrorsBhMissedLostPackets_Object = MibTableColumn
cirbhErrorsBhMissedLostPackets = _CirbhErrorsBhMissedLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 8),
    _CirbhErrorsBhMissedLostPackets_Type()
)
cirbhErrorsBhMissedLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedLostPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedLostPackets.setUnits("packets")
_CirbhErrorsBhMissedNoMemPackets_Type = Counter32
_CirbhErrorsBhMissedNoMemPackets_Object = MibTableColumn
cirbhErrorsBhMissedNoMemPackets = _CirbhErrorsBhMissedNoMemPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 9),
    _CirbhErrorsBhMissedNoMemPackets_Type()
)
cirbhErrorsBhMissedNoMemPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedNoMemPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedNoMemPackets.setUnits("packets")
_CirbhErrorsBhMissedResetPackets_Type = Counter32
_CirbhErrorsBhMissedResetPackets_Object = MibTableColumn
cirbhErrorsBhMissedResetPackets = _CirbhErrorsBhMissedResetPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 10),
    _CirbhErrorsBhMissedResetPackets_Type()
)
cirbhErrorsBhMissedResetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedResetPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsBhMissedResetPackets.setUnits("packets")
_CirbhErrorsDecompFailures_Type = Counter32
_CirbhErrorsDecompFailures_Object = MibTableColumn
cirbhErrorsDecompFailures = _CirbhErrorsDecompFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 11),
    _CirbhErrorsDecompFailures_Type()
)
cirbhErrorsDecompFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsDecompFailures.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsDecompFailures.setUnits("failures")
_CirbhErrorsCompFailures_Type = Counter32
_CirbhErrorsCompFailures_Object = MibTableColumn
cirbhErrorsCompFailures = _CirbhErrorsCompFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 12),
    _CirbhErrorsCompFailures_Type()
)
cirbhErrorsCompFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsCompFailures.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsCompFailures.setUnits("failures")
_CirbhErrorsCompNoPacketFailures_Type = Counter32
_CirbhErrorsCompNoPacketFailures_Object = MibTableColumn
cirbhErrorsCompNoPacketFailures = _CirbhErrorsCompNoPacketFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 13),
    _CirbhErrorsCompNoPacketFailures_Type()
)
cirbhErrorsCompNoPacketFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsCompNoPacketFailures.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsCompNoPacketFailures.setUnits("failures")
_CirbhErrorsCompNoIntFailures_Type = Counter32
_CirbhErrorsCompNoIntFailures_Object = MibTableColumn
cirbhErrorsCompNoIntFailures = _CirbhErrorsCompNoIntFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 14),
    _CirbhErrorsCompNoIntFailures_Type()
)
cirbhErrorsCompNoIntFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsCompNoIntFailures.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsCompNoIntFailures.setUnits("failures")
_CirbhErrorsCompIntDownFailures_Type = Counter32
_CirbhErrorsCompIntDownFailures_Object = MibTableColumn
cirbhErrorsCompIntDownFailures = _CirbhErrorsCompIntDownFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 15),
    _CirbhErrorsCompIntDownFailures_Type()
)
cirbhErrorsCompIntDownFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsCompIntDownFailures.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsCompIntDownFailures.setUnits("failures")
_CirbhErrorsCompEncapFailures_Type = Counter32
_CirbhErrorsCompEncapFailures_Object = MibTableColumn
cirbhErrorsCompEncapFailures = _CirbhErrorsCompEncapFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 16),
    _CirbhErrorsCompEncapFailures_Type()
)
cirbhErrorsCompEncapFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsCompEncapFailures.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsCompEncapFailures.setUnits("failures")
_CirbhErrorsCompQosDrops_Type = Counter32
_CirbhErrorsCompQosDrops_Object = MibTableColumn
cirbhErrorsCompQosDrops = _CirbhErrorsCompQosDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 2, 1, 17),
    _CirbhErrorsCompQosDrops_Type()
)
cirbhErrorsCompQosDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhErrorsCompQosDrops.setStatus("deprecated")
if mibBuilder.loadTexts:
    cirbhErrorsCompQosDrops.setUnits("drops")
_CirbhShortHaulHistoryTable_Object = MibTable
cirbhShortHaulHistoryTable = _CirbhShortHaulHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cirbhShortHaulHistoryTable.setStatus("obsolete")
_CirbhShortHaulHistoryTableEntry_Object = MibTableRow
cirbhShortHaulHistoryTableEntry = _CirbhShortHaulHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3, 1)
)
cirbhShortHaulHistoryTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulHistory"),
)
if mibBuilder.loadTexts:
    cirbhShortHaulHistoryTableEntry.setStatus("obsolete")
_CirbhShortHaulHistory_Type = CirbhHistoryIndex
_CirbhShortHaulHistory_Object = MibTableColumn
cirbhShortHaulHistory = _CirbhShortHaulHistory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3, 1, 1),
    _CirbhShortHaulHistory_Type()
)
cirbhShortHaulHistory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhShortHaulHistory.setStatus("obsolete")
_CirbhShortHaulRcvdRate_Type = CirbhRawInterfaceRate
_CirbhShortHaulRcvdRate_Object = MibTableColumn
cirbhShortHaulRcvdRate = _CirbhShortHaulRcvdRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3, 1, 2),
    _CirbhShortHaulRcvdRate_Type()
)
cirbhShortHaulRcvdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulRcvdRate.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhShortHaulRcvdRate.setUnits("bytes/second")
_CirbhShortHaulSentRate_Type = CirbhRawInterfaceRate
_CirbhShortHaulSentRate_Object = MibTableColumn
cirbhShortHaulSentRate = _CirbhShortHaulSentRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3, 1, 3),
    _CirbhShortHaulSentRate_Type()
)
cirbhShortHaulSentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulSentRate.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhShortHaulSentRate.setUnits("bytes/second")
_CirbhShortHaulRcvdCompressRate_Type = CirbhCommpressInterfaceRate
_CirbhShortHaulRcvdCompressRate_Object = MibTableColumn
cirbhShortHaulRcvdCompressRate = _CirbhShortHaulRcvdCompressRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3, 1, 4),
    _CirbhShortHaulRcvdCompressRate_Type()
)
cirbhShortHaulRcvdCompressRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulRcvdCompressRate.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhShortHaulRcvdCompressRate.setUnits("bytes/second")
_CirbhShortHaulSentCompressRate_Type = CirbhCommpressInterfaceRate
_CirbhShortHaulSentCompressRate_Object = MibTableColumn
cirbhShortHaulSentCompressRate = _CirbhShortHaulSentCompressRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3, 1, 5),
    _CirbhShortHaulSentCompressRate_Type()
)
cirbhShortHaulSentCompressRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulSentCompressRate.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhShortHaulSentCompressRate.setUnits("bytes/second")
_CirbhShortHaulTimeStamp_Type = TimeStamp
_CirbhShortHaulTimeStamp_Object = MibTableColumn
cirbhShortHaulTimeStamp = _CirbhShortHaulTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3, 1, 6),
    _CirbhShortHaulTimeStamp_Type()
)
cirbhShortHaulTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulTimeStamp.setStatus("obsolete")
_CirbhShortHaulRcvdUtilization_Type = CirbhShortHaulUtilization
_CirbhShortHaulRcvdUtilization_Object = MibTableColumn
cirbhShortHaulRcvdUtilization = _CirbhShortHaulRcvdUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3, 1, 7),
    _CirbhShortHaulRcvdUtilization_Type()
)
cirbhShortHaulRcvdUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulRcvdUtilization.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhShortHaulRcvdUtilization.setUnits("percent of DS load")
_CirbhShortHaulSentUtilization_Type = CirbhShortHaulUtilization
_CirbhShortHaulSentUtilization_Object = MibTableColumn
cirbhShortHaulSentUtilization = _CirbhShortHaulSentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 3, 1, 8),
    _CirbhShortHaulSentUtilization_Type()
)
cirbhShortHaulSentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulSentUtilization.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhShortHaulSentUtilization.setUnits("percent of DS load")
_CirbhCongestionTable_Object = MibTable
cirbhCongestionTable = _CirbhCongestionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cirbhCongestionTable.setStatus("current")
_CirbhCongestionTableEntry_Object = MibTableRow
cirbhCongestionTableEntry = _CirbhCongestionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 4, 1)
)
cirbhCongestionTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhCongestionTableEntry.setStatus("current")
_CirbhCongestionEnabled_Type = TruthValue
_CirbhCongestionEnabled_Object = MibTableColumn
cirbhCongestionEnabled = _CirbhCongestionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 4, 1, 1),
    _CirbhCongestionEnabled_Type()
)
cirbhCongestionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhCongestionEnabled.setStatus("current")
_CirbhCongestionDrops_Type = Counter32
_CirbhCongestionDrops_Object = MibTableColumn
cirbhCongestionDrops = _CirbhCongestionDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 4, 1, 2),
    _CirbhCongestionDrops_Type()
)
cirbhCongestionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhCongestionDrops.setStatus("current")
_CirbhCongestionDroppedBytes_Type = Counter32
_CirbhCongestionDroppedBytes_Object = MibTableColumn
cirbhCongestionDroppedBytes = _CirbhCongestionDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 4, 1, 3),
    _CirbhCongestionDroppedBytes_Type()
)
cirbhCongestionDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhCongestionDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    cirbhCongestionDroppedBytes.setUnits("bytes")
_CirbhCongestionEvents_Type = Counter32
_CirbhCongestionEvents_Object = MibTableColumn
cirbhCongestionEvents = _CirbhCongestionEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 4, 1, 4),
    _CirbhCongestionEvents_Type()
)
cirbhCongestionEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhCongestionEvents.setStatus("current")
if mibBuilder.loadTexts:
    cirbhCongestionEvents.setUnits("occurences")
_CirbhCongestionActive_Type = TruthValue
_CirbhCongestionActive_Object = MibTableColumn
cirbhCongestionActive = _CirbhCongestionActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 4, 1, 5),
    _CirbhCongestionActive_Type()
)
cirbhCongestionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhCongestionActive.setStatus("current")
_CirbhCongestionDuration_Type = Counter32
_CirbhCongestionDuration_Object = MibTableColumn
cirbhCongestionDuration = _CirbhCongestionDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 4, 1, 6),
    _CirbhCongestionDuration_Type()
)
cirbhCongestionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhCongestionDuration.setStatus("current")
if mibBuilder.loadTexts:
    cirbhCongestionDuration.setUnits("seconds")
_CirbhGsmErrorsTable_Object = MibTable
cirbhGsmErrorsTable = _CirbhGsmErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cirbhGsmErrorsTable.setStatus("current")
_CirbhGsmErrorsTableEntry_Object = MibTableRow
cirbhGsmErrorsTableEntry = _CirbhGsmErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1)
)
cirbhGsmErrorsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhGsmErrorsTableEntry.setStatus("current")
_CirbhGsmErrorsPeerNotReadyDrops_Type = Counter32
_CirbhGsmErrorsPeerNotReadyDrops_Object = MibTableColumn
cirbhGsmErrorsPeerNotReadyDrops = _CirbhGsmErrorsPeerNotReadyDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 1),
    _CirbhGsmErrorsPeerNotReadyDrops_Type()
)
cirbhGsmErrorsPeerNotReadyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsPeerNotReadyDrops.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsPeerNotReadyDrops.setUnits("packets")
_CirbhGsmErrorsPeerNotActiveDrops_Type = Counter32
_CirbhGsmErrorsPeerNotActiveDrops_Object = MibTableColumn
cirbhGsmErrorsPeerNotActiveDrops = _CirbhGsmErrorsPeerNotActiveDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 2),
    _CirbhGsmErrorsPeerNotActiveDrops_Type()
)
cirbhGsmErrorsPeerNotActiveDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsPeerNotActiveDrops.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsPeerNotActiveDrops.setUnits("packets")
_CirbhGsmErrorsInvalidPackets_Type = Counter32
_CirbhGsmErrorsInvalidPackets_Object = MibTableColumn
cirbhGsmErrorsInvalidPackets = _CirbhGsmErrorsInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 3),
    _CirbhGsmErrorsInvalidPackets_Type()
)
cirbhGsmErrorsInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsInvalidPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsInvalidPackets.setUnits("packets")
_CirbhGsmErrorsLostRcvdPackets_Type = Counter32
_CirbhGsmErrorsLostRcvdPackets_Object = MibTableColumn
cirbhGsmErrorsLostRcvdPackets = _CirbhGsmErrorsLostRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 4),
    _CirbhGsmErrorsLostRcvdPackets_Type()
)
cirbhGsmErrorsLostRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsLostRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsLostRcvdPackets.setUnits("packets")
_CirbhGsmErrorsLostSentPackets_Type = Counter32
_CirbhGsmErrorsLostSentPackets_Object = MibTableColumn
cirbhGsmErrorsLostSentPackets = _CirbhGsmErrorsLostSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 5),
    _CirbhGsmErrorsLostSentPackets_Type()
)
cirbhGsmErrorsLostSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsLostSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsLostSentPackets.setUnits("packets")
_CirbhGsmErrorsMissedPackets_Type = Counter32
_CirbhGsmErrorsMissedPackets_Object = MibTableColumn
cirbhGsmErrorsMissedPackets = _CirbhGsmErrorsMissedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 6),
    _CirbhGsmErrorsMissedPackets_Type()
)
cirbhGsmErrorsMissedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedPackets.setUnits("packets")
_CirbhGsmErrorsMissedLatePackets_Type = Counter32
_CirbhGsmErrorsMissedLatePackets_Object = MibTableColumn
cirbhGsmErrorsMissedLatePackets = _CirbhGsmErrorsMissedLatePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 7),
    _CirbhGsmErrorsMissedLatePackets_Type()
)
cirbhGsmErrorsMissedLatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedLatePackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedLatePackets.setUnits("packets")
_CirbhGsmErrorsMissedLostPackets_Type = Counter32
_CirbhGsmErrorsMissedLostPackets_Object = MibTableColumn
cirbhGsmErrorsMissedLostPackets = _CirbhGsmErrorsMissedLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 8),
    _CirbhGsmErrorsMissedLostPackets_Type()
)
cirbhGsmErrorsMissedLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedLostPackets.setUnits("packets")
_CirbhGsmErrorsMissedNoMemPackets_Type = Counter32
_CirbhGsmErrorsMissedNoMemPackets_Object = MibTableColumn
cirbhGsmErrorsMissedNoMemPackets = _CirbhGsmErrorsMissedNoMemPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 9),
    _CirbhGsmErrorsMissedNoMemPackets_Type()
)
cirbhGsmErrorsMissedNoMemPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedNoMemPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedNoMemPackets.setUnits("packets")
_CirbhGsmErrorsMissedResetPackets_Type = Counter32
_CirbhGsmErrorsMissedResetPackets_Object = MibTableColumn
cirbhGsmErrorsMissedResetPackets = _CirbhGsmErrorsMissedResetPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 10),
    _CirbhGsmErrorsMissedResetPackets_Type()
)
cirbhGsmErrorsMissedResetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedResetPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsMissedResetPackets.setUnits("packets")
_CirbhGsmErrorsDecompFailures_Type = Counter32
_CirbhGsmErrorsDecompFailures_Object = MibTableColumn
cirbhGsmErrorsDecompFailures = _CirbhGsmErrorsDecompFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 11),
    _CirbhGsmErrorsDecompFailures_Type()
)
cirbhGsmErrorsDecompFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsDecompFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsDecompFailures.setUnits("failures")
_CirbhGsmErrorsCompFailures_Type = Counter32
_CirbhGsmErrorsCompFailures_Object = MibTableColumn
cirbhGsmErrorsCompFailures = _CirbhGsmErrorsCompFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 12),
    _CirbhGsmErrorsCompFailures_Type()
)
cirbhGsmErrorsCompFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompFailures.setUnits("failures")
_CirbhGsmErrorsCompNoPacketFailures_Type = Counter32
_CirbhGsmErrorsCompNoPacketFailures_Object = MibTableColumn
cirbhGsmErrorsCompNoPacketFailures = _CirbhGsmErrorsCompNoPacketFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 13),
    _CirbhGsmErrorsCompNoPacketFailures_Type()
)
cirbhGsmErrorsCompNoPacketFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompNoPacketFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompNoPacketFailures.setUnits("failures")
_CirbhGsmErrorsCompNoIntFailures_Type = Counter32
_CirbhGsmErrorsCompNoIntFailures_Object = MibTableColumn
cirbhGsmErrorsCompNoIntFailures = _CirbhGsmErrorsCompNoIntFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 14),
    _CirbhGsmErrorsCompNoIntFailures_Type()
)
cirbhGsmErrorsCompNoIntFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompNoIntFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompNoIntFailures.setUnits("failures")
_CirbhGsmErrorsCompIntDownFailures_Type = Counter32
_CirbhGsmErrorsCompIntDownFailures_Object = MibTableColumn
cirbhGsmErrorsCompIntDownFailures = _CirbhGsmErrorsCompIntDownFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 15),
    _CirbhGsmErrorsCompIntDownFailures_Type()
)
cirbhGsmErrorsCompIntDownFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompIntDownFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompIntDownFailures.setUnits("failures")
_CirbhGsmErrorsCompEncapFailures_Type = Counter32
_CirbhGsmErrorsCompEncapFailures_Object = MibTableColumn
cirbhGsmErrorsCompEncapFailures = _CirbhGsmErrorsCompEncapFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 16),
    _CirbhGsmErrorsCompEncapFailures_Type()
)
cirbhGsmErrorsCompEncapFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompEncapFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompEncapFailures.setUnits("failures")
_CirbhGsmErrorsCompQosDrops_Type = Counter32
_CirbhGsmErrorsCompQosDrops_Object = MibTableColumn
cirbhGsmErrorsCompQosDrops = _CirbhGsmErrorsCompQosDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 17),
    _CirbhGsmErrorsCompQosDrops_Type()
)
cirbhGsmErrorsCompQosDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompQosDrops.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsCompQosDrops.setUnits("drops")
_CirbhGsmErrorsFastSendFailures_Type = Counter32
_CirbhGsmErrorsFastSendFailures_Object = MibTableColumn
cirbhGsmErrorsFastSendFailures = _CirbhGsmErrorsFastSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 18),
    _CirbhGsmErrorsFastSendFailures_Type()
)
cirbhGsmErrorsFastSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsFastSendFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsFastSendFailures.setUnits("occurences")
_CirbhGsmErrorsTxPacketFailures_Type = Counter32
_CirbhGsmErrorsTxPacketFailures_Object = MibTableColumn
cirbhGsmErrorsTxPacketFailures = _CirbhGsmErrorsTxPacketFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 19),
    _CirbhGsmErrorsTxPacketFailures_Type()
)
cirbhGsmErrorsTxPacketFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsTxPacketFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsTxPacketFailures.setUnits("occurences")
_CirbhGsmErrorsTxNoBuffers_Type = Counter32
_CirbhGsmErrorsTxNoBuffers_Object = MibTableColumn
cirbhGsmErrorsTxNoBuffers = _CirbhGsmErrorsTxNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 20),
    _CirbhGsmErrorsTxNoBuffers_Type()
)
cirbhGsmErrorsTxNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsTxNoBuffers.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsTxNoBuffers.setUnits("occurences")
_CirbhGsmErrorsTxResets_Type = Counter32
_CirbhGsmErrorsTxResets_Object = MibTableColumn
cirbhGsmErrorsTxResets = _CirbhGsmErrorsTxResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 21),
    _CirbhGsmErrorsTxResets_Type()
)
cirbhGsmErrorsTxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsTxResets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsTxResets.setUnits("occurences")
_CirbhGsmErrorsOverruns_Type = Counter32
_CirbhGsmErrorsOverruns_Object = MibTableColumn
cirbhGsmErrorsOverruns = _CirbhGsmErrorsOverruns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 22),
    _CirbhGsmErrorsOverruns_Type()
)
cirbhGsmErrorsOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsOverruns.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsOverruns.setUnits("occurences")
_CirbhGsmErrorsInterruptFailures_Type = Counter32
_CirbhGsmErrorsInterruptFailures_Object = MibTableColumn
cirbhGsmErrorsInterruptFailures = _CirbhGsmErrorsInterruptFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 23),
    _CirbhGsmErrorsInterruptFailures_Type()
)
cirbhGsmErrorsInterruptFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsInterruptFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsInterruptFailures.setUnits("Failures")
_CirbhGsmErrorsLateArrivals_Type = Counter32
_CirbhGsmErrorsLateArrivals_Object = MibTableColumn
cirbhGsmErrorsLateArrivals = _CirbhGsmErrorsLateArrivals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 24),
    _CirbhGsmErrorsLateArrivals_Type()
)
cirbhGsmErrorsLateArrivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsLateArrivals.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsLateArrivals.setUnits("packets")
_CirbhGsmErrorsEarlyArrivals_Type = Counter32
_CirbhGsmErrorsEarlyArrivals_Object = MibTableColumn
cirbhGsmErrorsEarlyArrivals = _CirbhGsmErrorsEarlyArrivals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 5, 1, 25),
    _CirbhGsmErrorsEarlyArrivals_Type()
)
cirbhGsmErrorsEarlyArrivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhGsmErrorsEarlyArrivals.setStatus("current")
if mibBuilder.loadTexts:
    cirbhGsmErrorsEarlyArrivals.setUnits("packets")
_CirbhUmtsErrorsTable_Object = MibTable
cirbhUmtsErrorsTable = _CirbhUmtsErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cirbhUmtsErrorsTable.setStatus("current")
_CirbhUmtsErrorsTableEntry_Object = MibTableRow
cirbhUmtsErrorsTableEntry = _CirbhUmtsErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1)
)
cirbhUmtsErrorsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhUmtsErrorsTableEntry.setStatus("current")
_CirbhUmtsErrorsPeerNotReadyDrops_Type = Counter32
_CirbhUmtsErrorsPeerNotReadyDrops_Object = MibTableColumn
cirbhUmtsErrorsPeerNotReadyDrops = _CirbhUmtsErrorsPeerNotReadyDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 1),
    _CirbhUmtsErrorsPeerNotReadyDrops_Type()
)
cirbhUmtsErrorsPeerNotReadyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsPeerNotReadyDrops.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsPeerNotReadyDrops.setUnits("packets")
_CirbhUmtsErrorsInvalidPackets_Type = Counter32
_CirbhUmtsErrorsInvalidPackets_Object = MibTableColumn
cirbhUmtsErrorsInvalidPackets = _CirbhUmtsErrorsInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 2),
    _CirbhUmtsErrorsInvalidPackets_Type()
)
cirbhUmtsErrorsInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsInvalidPackets.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsInvalidPackets.setUnits("packets")
_CirbhUmtsErrorsDecompFailures_Type = Counter32
_CirbhUmtsErrorsDecompFailures_Object = MibTableColumn
cirbhUmtsErrorsDecompFailures = _CirbhUmtsErrorsDecompFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 3),
    _CirbhUmtsErrorsDecompFailures_Type()
)
cirbhUmtsErrorsDecompFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsDecompFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsDecompFailures.setUnits("failures")
_CirbhUmtsErrorsCompFailures_Type = Counter32
_CirbhUmtsErrorsCompFailures_Object = MibTableColumn
cirbhUmtsErrorsCompFailures = _CirbhUmtsErrorsCompFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 4),
    _CirbhUmtsErrorsCompFailures_Type()
)
cirbhUmtsErrorsCompFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompFailures.setUnits("failures")
_CirbhUmtsErrorsCompNoPacketFailures_Type = Counter32
_CirbhUmtsErrorsCompNoPacketFailures_Object = MibTableColumn
cirbhUmtsErrorsCompNoPacketFailures = _CirbhUmtsErrorsCompNoPacketFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 5),
    _CirbhUmtsErrorsCompNoPacketFailures_Type()
)
cirbhUmtsErrorsCompNoPacketFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompNoPacketFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompNoPacketFailures.setUnits("failures")
_CirbhUmtsErrorsCompNoIntFailures_Type = Counter32
_CirbhUmtsErrorsCompNoIntFailures_Object = MibTableColumn
cirbhUmtsErrorsCompNoIntFailures = _CirbhUmtsErrorsCompNoIntFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 6),
    _CirbhUmtsErrorsCompNoIntFailures_Type()
)
cirbhUmtsErrorsCompNoIntFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompNoIntFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompNoIntFailures.setUnits("failures")
_CirbhUmtsErrorsCompIntDownFailures_Type = Counter32
_CirbhUmtsErrorsCompIntDownFailures_Object = MibTableColumn
cirbhUmtsErrorsCompIntDownFailures = _CirbhUmtsErrorsCompIntDownFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 7),
    _CirbhUmtsErrorsCompIntDownFailures_Type()
)
cirbhUmtsErrorsCompIntDownFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompIntDownFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompIntDownFailures.setUnits("failures")
_CirbhUmtsErrorsCompEncapFailures_Type = Counter32
_CirbhUmtsErrorsCompEncapFailures_Object = MibTableColumn
cirbhUmtsErrorsCompEncapFailures = _CirbhUmtsErrorsCompEncapFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 8),
    _CirbhUmtsErrorsCompEncapFailures_Type()
)
cirbhUmtsErrorsCompEncapFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompEncapFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompEncapFailures.setUnits("failures")
_CirbhUmtsErrorsCompQosDrops_Type = Counter32
_CirbhUmtsErrorsCompQosDrops_Object = MibTableColumn
cirbhUmtsErrorsCompQosDrops = _CirbhUmtsErrorsCompQosDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 9),
    _CirbhUmtsErrorsCompQosDrops_Type()
)
cirbhUmtsErrorsCompQosDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompQosDrops.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsCompQosDrops.setUnits("drops")
_CirbhUmtsErrorsShorthaulPakFailures_Type = Counter32
_CirbhUmtsErrorsShorthaulPakFailures_Object = MibTableColumn
cirbhUmtsErrorsShorthaulPakFailures = _CirbhUmtsErrorsShorthaulPakFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 10),
    _CirbhUmtsErrorsShorthaulPakFailures_Type()
)
cirbhUmtsErrorsShorthaulPakFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsShorthaulPakFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsShorthaulPakFailures.setUnits("occurrences")
_CirbhUmtsErrorsUmtsEncapFailures_Type = Counter32
_CirbhUmtsErrorsUmtsEncapFailures_Object = MibTableColumn
cirbhUmtsErrorsUmtsEncapFailures = _CirbhUmtsErrorsUmtsEncapFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 11),
    _CirbhUmtsErrorsUmtsEncapFailures_Type()
)
cirbhUmtsErrorsUmtsEncapFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsUmtsEncapFailures.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsUmtsEncapFailures.setUnits("occurences")
_CirbhUmtsErrorsLocalPvcDrops_Type = Counter32
_CirbhUmtsErrorsLocalPvcDrops_Object = MibTableColumn
cirbhUmtsErrorsLocalPvcDrops = _CirbhUmtsErrorsLocalPvcDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 12),
    _CirbhUmtsErrorsLocalPvcDrops_Type()
)
cirbhUmtsErrorsLocalPvcDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsLocalPvcDrops.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsLocalPvcDrops.setUnits("packets")
_CirbhUmtsErrorsRemotePvcDrops_Type = Counter32
_CirbhUmtsErrorsRemotePvcDrops_Object = MibTableColumn
cirbhUmtsErrorsRemotePvcDrops = _CirbhUmtsErrorsRemotePvcDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 13),
    _CirbhUmtsErrorsRemotePvcDrops_Type()
)
cirbhUmtsErrorsRemotePvcDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsRemotePvcDrops.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsRemotePvcDrops.setUnits("packets")
_CirbhUmtsErrorsBackhaulDrops_Type = Counter32
_CirbhUmtsErrorsBackhaulDrops_Object = MibTableColumn
cirbhUmtsErrorsBackhaulDrops = _CirbhUmtsErrorsBackhaulDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 6, 1, 14),
    _CirbhUmtsErrorsBackhaulDrops_Type()
)
cirbhUmtsErrorsBackhaulDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsBackhaulDrops.setStatus("current")
if mibBuilder.loadTexts:
    cirbhUmtsErrorsBackhaulDrops.setUnits("packets")
_CirbhShortHaulBulkTable_Object = MibTable
cirbhShortHaulBulkTable = _CirbhShortHaulBulkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cirbhShortHaulBulkTable.setStatus("current")
_CirbhShortHaulBulkTableEntry_Object = MibTableRow
cirbhShortHaulBulkTableEntry = _CirbhShortHaulBulkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 7, 1)
)
cirbhShortHaulBulkTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulBulkHistory"),
)
if mibBuilder.loadTexts:
    cirbhShortHaulBulkTableEntry.setStatus("current")
_CirbhShortHaulBulkHistory_Type = CirbhHistoryIndex
_CirbhShortHaulBulkHistory_Object = MibTableColumn
cirbhShortHaulBulkHistory = _CirbhShortHaulBulkHistory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 7, 1, 1),
    _CirbhShortHaulBulkHistory_Type()
)
cirbhShortHaulBulkHistory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhShortHaulBulkHistory.setStatus("current")
_CirbhShortHaulBulkTimeStamp_Type = TimeStamp
_CirbhShortHaulBulkTimeStamp_Object = MibTableColumn
cirbhShortHaulBulkTimeStamp = _CirbhShortHaulBulkTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 7, 1, 2),
    _CirbhShortHaulBulkTimeStamp_Type()
)
cirbhShortHaulBulkTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulBulkTimeStamp.setStatus("current")


class _CirbhShortHaulBulkBaseUnit_Type(Unsigned32):
    """Custom type cirbhShortHaulBulkBaseUnit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_CirbhShortHaulBulkBaseUnit_Type.__name__ = "Unsigned32"
_CirbhShortHaulBulkBaseUnit_Object = MibTableColumn
cirbhShortHaulBulkBaseUnit = _CirbhShortHaulBulkBaseUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 7, 1, 3),
    _CirbhShortHaulBulkBaseUnit_Type()
)
cirbhShortHaulBulkBaseUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulBulkBaseUnit.setStatus("current")
if mibBuilder.loadTexts:
    cirbhShortHaulBulkBaseUnit.setUnits("Bytes")


class _CirbhShortHaulBulkUtil_Type(OctetString):
    """Custom type cirbhShortHaulBulkUtil based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CirbhShortHaulBulkUtil_Type.__name__ = "OctetString"
_CirbhShortHaulBulkUtil_Object = MibTableColumn
cirbhShortHaulBulkUtil = _CirbhShortHaulBulkUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 1, 3, 7, 1, 4),
    _CirbhShortHaulBulkUtil_Type()
)
cirbhShortHaulBulkUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhShortHaulBulkUtil.setStatus("current")
if mibBuilder.loadTexts:
    cirbhShortHaulBulkUtil.setUnits("Bytes/Second")
_CirbhBackHaul_ObjectIdentity = ObjectIdentity
cirbhBackHaul = _CirbhBackHaul_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2)
)
_CirbhBackHaulInfo_ObjectIdentity = ObjectIdentity
cirbhBackHaulInfo = _CirbhBackHaulInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1)
)
_CirbhBackHaulTable_Object = MibTable
cirbhBackHaulTable = _CirbhBackHaulTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cirbhBackHaulTable.setStatus("obsolete")
_CirbhBackHaulEntry_Object = MibTableRow
cirbhBackHaulEntry = _CirbhBackHaulEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 1, 1)
)
cirbhBackHaulEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cirbhBackHaulEntry.setStatus("obsolete")
_CirbhBackHaulAdjectSerialNum_Type = SnmpAdminString
_CirbhBackHaulAdjectSerialNum_Object = MibTableColumn
cirbhBackHaulAdjectSerialNum = _CirbhBackHaulAdjectSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 1, 1, 1),
    _CirbhBackHaulAdjectSerialNum_Type()
)
cirbhBackHaulAdjectSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulAdjectSerialNum.setStatus("obsolete")
_CirbhBackHaulAdjectVendorType_Type = AutonomousType
_CirbhBackHaulAdjectVendorType_Object = MibTableColumn
cirbhBackHaulAdjectVendorType = _CirbhBackHaulAdjectVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 1, 1, 2),
    _CirbhBackHaulAdjectVendorType_Type()
)
cirbhBackHaulAdjectVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulAdjectVendorType.setStatus("obsolete")
_CirbhBackHaulRcvdUtilState_Type = CirbhBackHaulUtilizationState
_CirbhBackHaulRcvdUtilState_Object = MibTableColumn
cirbhBackHaulRcvdUtilState = _CirbhBackHaulRcvdUtilState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 1, 1, 3),
    _CirbhBackHaulRcvdUtilState_Type()
)
cirbhBackHaulRcvdUtilState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulRcvdUtilState.setStatus("obsolete")
_CirbhBackHaulSentUtilState_Type = CirbhBackHaulUtilizationState
_CirbhBackHaulSentUtilState_Object = MibTableColumn
cirbhBackHaulSentUtilState = _CirbhBackHaulSentUtilState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 1, 1, 4),
    _CirbhBackHaulSentUtilState_Type()
)
cirbhBackHaulSentUtilState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulSentUtilState.setStatus("obsolete")
_CirbhBackHaulRcvdUtil_Type = CirbhBackHaulUtilization
_CirbhBackHaulRcvdUtil_Object = MibTableColumn
cirbhBackHaulRcvdUtil = _CirbhBackHaulRcvdUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 1, 1, 5),
    _CirbhBackHaulRcvdUtil_Type()
)
cirbhBackHaulRcvdUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulRcvdUtil.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhBackHaulRcvdUtil.setUnits("percent")
_CirbhBackHaulSentUtil_Type = CirbhBackHaulUtilization
_CirbhBackHaulSentUtil_Object = MibTableColumn
cirbhBackHaulSentUtil = _CirbhBackHaulSentUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 1, 1, 6),
    _CirbhBackHaulSentUtil_Type()
)
cirbhBackHaulSentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulSentUtil.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhBackHaulSentUtil.setUnits("percent")
_CirbhBackHaulShortHaulTable_Object = MibTable
cirbhBackHaulShortHaulTable = _CirbhBackHaulShortHaulTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cirbhBackHaulShortHaulTable.setStatus("obsolete")
_CirbhBackHaulShortHaulEntry_Object = MibTableRow
cirbhBackHaulShortHaulEntry = _CirbhBackHaulShortHaulEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 2, 1)
)
cirbhBackHaulShortHaulEntry.setIndexNames(
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulShortHaulBhIndex"),
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulShortHaulShIndex"),
)
if mibBuilder.loadTexts:
    cirbhBackHaulShortHaulEntry.setStatus("obsolete")
_CirbhBackHaulShortHaulBhIndex_Type = InterfaceIndex
_CirbhBackHaulShortHaulBhIndex_Object = MibTableColumn
cirbhBackHaulShortHaulBhIndex = _CirbhBackHaulShortHaulBhIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 2, 1, 1),
    _CirbhBackHaulShortHaulBhIndex_Type()
)
cirbhBackHaulShortHaulBhIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhBackHaulShortHaulBhIndex.setStatus("obsolete")
_CirbhBackHaulShortHaulShIndex_Type = InterfaceIndex
_CirbhBackHaulShortHaulShIndex_Object = MibTableColumn
cirbhBackHaulShortHaulShIndex = _CirbhBackHaulShortHaulShIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 2, 1, 2),
    _CirbhBackHaulShortHaulShIndex_Type()
)
cirbhBackHaulShortHaulShIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhBackHaulShortHaulShIndex.setStatus("obsolete")
_CirbhBackHaulShortHaulTimestamp_Type = TimeStamp
_CirbhBackHaulShortHaulTimestamp_Object = MibTableColumn
cirbhBackHaulShortHaulTimestamp = _CirbhBackHaulShortHaulTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 1, 2, 1, 3),
    _CirbhBackHaulShortHaulTimestamp_Type()
)
cirbhBackHaulShortHaulTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulShortHaulTimestamp.setStatus("obsolete")
_CirbhBackHaulStats_ObjectIdentity = ObjectIdentity
cirbhBackHaulStats = _CirbhBackHaulStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2)
)
_CirbhBackHaulHistoryTable_Object = MibTable
cirbhBackHaulHistoryTable = _CirbhBackHaulHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryTable.setStatus("obsolete")
_CirbhBackHaulHistoryEntry_Object = MibTableRow
cirbhBackHaulHistoryEntry = _CirbhBackHaulHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1, 1)
)
cirbhBackHaulHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulHistoryIndex"),
)
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryEntry.setStatus("obsolete")
_CirbhBackHaulHistoryIndex_Type = CirbhHistoryIndex
_CirbhBackHaulHistoryIndex_Object = MibTableColumn
cirbhBackHaulHistoryIndex = _CirbhBackHaulHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1, 1, 1),
    _CirbhBackHaulHistoryIndex_Type()
)
cirbhBackHaulHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryIndex.setStatus("obsolete")
_CirbhBackHaulHistoryRcvdUtil_Type = CirbhBackHaulUtilization
_CirbhBackHaulHistoryRcvdUtil_Object = MibTableColumn
cirbhBackHaulHistoryRcvdUtil = _CirbhBackHaulHistoryRcvdUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1, 1, 2),
    _CirbhBackHaulHistoryRcvdUtil_Type()
)
cirbhBackHaulHistoryRcvdUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryRcvdUtil.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryRcvdUtil.setUnits("percent")
_CirbhBackHaulHistorySentUtil_Type = CirbhBackHaulUtilization
_CirbhBackHaulHistorySentUtil_Object = MibTableColumn
cirbhBackHaulHistorySentUtil = _CirbhBackHaulHistorySentUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1, 1, 3),
    _CirbhBackHaulHistorySentUtil_Type()
)
cirbhBackHaulHistorySentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulHistorySentUtil.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhBackHaulHistorySentUtil.setUnits("percent")
_CirbhBackHaulHistoryRcvdAbisUtil_Type = CirbhBackHaulUtilization
_CirbhBackHaulHistoryRcvdAbisUtil_Object = MibTableColumn
cirbhBackHaulHistoryRcvdAbisUtil = _CirbhBackHaulHistoryRcvdAbisUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1, 1, 4),
    _CirbhBackHaulHistoryRcvdAbisUtil_Type()
)
cirbhBackHaulHistoryRcvdAbisUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryRcvdAbisUtil.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryRcvdAbisUtil.setUnits("percent")
_CirbhBackHaulHistorySentAbisUtil_Type = CirbhBackHaulUtilization
_CirbhBackHaulHistorySentAbisUtil_Object = MibTableColumn
cirbhBackHaulHistorySentAbisUtil = _CirbhBackHaulHistorySentAbisUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1, 1, 5),
    _CirbhBackHaulHistorySentAbisUtil_Type()
)
cirbhBackHaulHistorySentAbisUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulHistorySentAbisUtil.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhBackHaulHistorySentAbisUtil.setUnits("percent")
_CirbhBackHaulHistoryRcvdUmtsUtil_Type = CirbhBackHaulUtilization
_CirbhBackHaulHistoryRcvdUmtsUtil_Object = MibTableColumn
cirbhBackHaulHistoryRcvdUmtsUtil = _CirbhBackHaulHistoryRcvdUmtsUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1, 1, 6),
    _CirbhBackHaulHistoryRcvdUmtsUtil_Type()
)
cirbhBackHaulHistoryRcvdUmtsUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryRcvdUmtsUtil.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryRcvdUmtsUtil.setUnits("percent")
_CirbhBackHaulHistorySentUmtsUtil_Type = CirbhBackHaulUtilization
_CirbhBackHaulHistorySentUmtsUtil_Object = MibTableColumn
cirbhBackHaulHistorySentUmtsUtil = _CirbhBackHaulHistorySentUmtsUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1, 1, 7),
    _CirbhBackHaulHistorySentUmtsUtil_Type()
)
cirbhBackHaulHistorySentUmtsUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulHistorySentUmtsUtil.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhBackHaulHistorySentUmtsUtil.setUnits("percent")
_CirbhBackHaulHistoryTimeStamp_Type = TimeStamp
_CirbhBackHaulHistoryTimeStamp_Object = MibTableColumn
cirbhBackHaulHistoryTimeStamp = _CirbhBackHaulHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 1, 1, 8),
    _CirbhBackHaulHistoryTimeStamp_Type()
)
cirbhBackHaulHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhBackHaulHistoryTimeStamp.setStatus("obsolete")
_CirbhBackHaulStatsTable_Object = MibTable
cirbhBackHaulStatsTable = _CirbhBackHaulStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cirbhBackHaulStatsTable.setStatus("obsolete")
_CirbhBackHaulStatsEntry_Object = MibTableRow
cirbhBackHaulStatsEntry = _CirbhBackHaulStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1)
)
cirbhBackHaulStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsDirection"),
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsTrafficType"),
)
if mibBuilder.loadTexts:
    cirbhBackHaulStatsEntry.setStatus("obsolete")
_CirbhStatsDirection_Type = CirbhTrafficDirection
_CirbhStatsDirection_Object = MibTableColumn
cirbhStatsDirection = _CirbhStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 1),
    _CirbhStatsDirection_Type()
)
cirbhStatsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhStatsDirection.setStatus("obsolete")
_CirbhStatsTrafficType_Type = CirbhTrafficType
_CirbhStatsTrafficType_Object = MibTableColumn
cirbhStatsTrafficType = _CirbhStatsTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 2),
    _CirbhStatsTrafficType_Type()
)
cirbhStatsTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhStatsTrafficType.setStatus("obsolete")
_CirbhStats000to009Seconds_Type = PerfCurrentCount
_CirbhStats000to009Seconds_Object = MibTableColumn
cirbhStats000to009Seconds = _CirbhStats000to009Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 3),
    _CirbhStats000to009Seconds_Type()
)
cirbhStats000to009Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats000to009Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats000to009Seconds.setUnits("seconds")
_CirbhStats010to019Seconds_Type = PerfCurrentCount
_CirbhStats010to019Seconds_Object = MibTableColumn
cirbhStats010to019Seconds = _CirbhStats010to019Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 4),
    _CirbhStats010to019Seconds_Type()
)
cirbhStats010to019Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats010to019Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats010to019Seconds.setUnits("seconds")
_CirbhStats020to029Seconds_Type = PerfCurrentCount
_CirbhStats020to029Seconds_Object = MibTableColumn
cirbhStats020to029Seconds = _CirbhStats020to029Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 5),
    _CirbhStats020to029Seconds_Type()
)
cirbhStats020to029Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats020to029Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats020to029Seconds.setUnits("seconds")
_CirbhStats030to039Seconds_Type = PerfCurrentCount
_CirbhStats030to039Seconds_Object = MibTableColumn
cirbhStats030to039Seconds = _CirbhStats030to039Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 6),
    _CirbhStats030to039Seconds_Type()
)
cirbhStats030to039Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats030to039Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats030to039Seconds.setUnits("seconds")
_CirbhStats040to049Seconds_Type = PerfCurrentCount
_CirbhStats040to049Seconds_Object = MibTableColumn
cirbhStats040to049Seconds = _CirbhStats040to049Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 7),
    _CirbhStats040to049Seconds_Type()
)
cirbhStats040to049Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats040to049Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats040to049Seconds.setUnits("seconds")
_CirbhStats050to059Seconds_Type = PerfCurrentCount
_CirbhStats050to059Seconds_Object = MibTableColumn
cirbhStats050to059Seconds = _CirbhStats050to059Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 8),
    _CirbhStats050to059Seconds_Type()
)
cirbhStats050to059Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats050to059Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats050to059Seconds.setUnits("seconds")
_CirbhStats060to069Seconds_Type = PerfCurrentCount
_CirbhStats060to069Seconds_Object = MibTableColumn
cirbhStats060to069Seconds = _CirbhStats060to069Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 9),
    _CirbhStats060to069Seconds_Type()
)
cirbhStats060to069Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats060to069Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats060to069Seconds.setUnits("seconds")
_CirbhStats070to079Seconds_Type = PerfCurrentCount
_CirbhStats070to079Seconds_Object = MibTableColumn
cirbhStats070to079Seconds = _CirbhStats070to079Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 10),
    _CirbhStats070to079Seconds_Type()
)
cirbhStats070to079Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats070to079Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats070to079Seconds.setUnits("seconds")
_CirbhStats080to089Seconds_Type = PerfCurrentCount
_CirbhStats080to089Seconds_Object = MibTableColumn
cirbhStats080to089Seconds = _CirbhStats080to089Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 11),
    _CirbhStats080to089Seconds_Type()
)
cirbhStats080to089Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats080to089Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats080to089Seconds.setUnits("seconds")
_CirbhStats090to100Seconds_Type = PerfCurrentCount
_CirbhStats090to100Seconds_Object = MibTableColumn
cirbhStats090to100Seconds = _CirbhStats090to100Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 12),
    _CirbhStats090to100Seconds_Type()
)
cirbhStats090to100Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStats090to100Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStats090to100Seconds.setUnits("seconds")
_CirbhStatsTimeStamp_Type = TimeStamp
_CirbhStatsTimeStamp_Object = MibTableColumn
cirbhStatsTimeStamp = _CirbhStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 13),
    _CirbhStatsTimeStamp_Type()
)
cirbhStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsTimeStamp.setStatus("obsolete")
_CirbhStatsMaxUtilization_Type = CirbhBackHaulUtilization
_CirbhStatsMaxUtilization_Object = MibTableColumn
cirbhStatsMaxUtilization = _CirbhStatsMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 14),
    _CirbhStatsMaxUtilization_Type()
)
cirbhStatsMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsMaxUtilization.setStatus("obsolete")
_CirbhStatsMaxTimeStamp_Type = TimeStamp
_CirbhStatsMaxTimeStamp_Object = MibTableColumn
cirbhStatsMaxTimeStamp = _CirbhStatsMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 2, 2, 2, 1, 15),
    _CirbhStatsMaxTimeStamp_Type()
)
cirbhStatsMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsMaxTimeStamp.setStatus("obsolete")
_CirbhBackHaulStatsHistoryTable_Object = MibTable
cirbhBackHaulStatsHistoryTable = _CirbhBackHaulStatsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cirbhBackHaulStatsHistoryTable.setStatus("obsolete")
_CirbhBackHaulStatsHistoryEntry_Object = MibTableRow
cirbhBackHaulStatsHistoryEntry = _CirbhBackHaulStatsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1)
)
cirbhBackHaulStatsHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistoryIndex"),
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistoryDirection"),
    (0, "CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistoryTrafficType"),
)
if mibBuilder.loadTexts:
    cirbhBackHaulStatsHistoryEntry.setStatus("obsolete")
_CirbhStatsHistoryIndex_Type = CirbhHistoryIndex
_CirbhStatsHistoryIndex_Object = MibTableColumn
cirbhStatsHistoryIndex = _CirbhStatsHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 1),
    _CirbhStatsHistoryIndex_Type()
)
cirbhStatsHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhStatsHistoryIndex.setStatus("obsolete")
_CirbhStatsHistoryDirection_Type = CirbhTrafficDirection
_CirbhStatsHistoryDirection_Object = MibTableColumn
cirbhStatsHistoryDirection = _CirbhStatsHistoryDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 2),
    _CirbhStatsHistoryDirection_Type()
)
cirbhStatsHistoryDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhStatsHistoryDirection.setStatus("obsolete")
_CirbhStatsHistoryTrafficType_Type = CirbhTrafficType
_CirbhStatsHistoryTrafficType_Object = MibTableColumn
cirbhStatsHistoryTrafficType = _CirbhStatsHistoryTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 3),
    _CirbhStatsHistoryTrafficType_Type()
)
cirbhStatsHistoryTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cirbhStatsHistoryTrafficType.setStatus("obsolete")
_CirbhStatsHistory000to009Seconds_Type = PerfIntervalCount
_CirbhStatsHistory000to009Seconds_Object = MibTableColumn
cirbhStatsHistory000to009Seconds = _CirbhStatsHistory000to009Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 4),
    _CirbhStatsHistory000to009Seconds_Type()
)
cirbhStatsHistory000to009Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory000to009Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory000to009Seconds.setUnits("seconds")
_CirbhStatsHistory010to019Seconds_Type = PerfIntervalCount
_CirbhStatsHistory010to019Seconds_Object = MibTableColumn
cirbhStatsHistory010to019Seconds = _CirbhStatsHistory010to019Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 5),
    _CirbhStatsHistory010to019Seconds_Type()
)
cirbhStatsHistory010to019Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory010to019Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory010to019Seconds.setUnits("seconds")
_CirbhStatsHistory020to029Seconds_Type = PerfIntervalCount
_CirbhStatsHistory020to029Seconds_Object = MibTableColumn
cirbhStatsHistory020to029Seconds = _CirbhStatsHistory020to029Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 6),
    _CirbhStatsHistory020to029Seconds_Type()
)
cirbhStatsHistory020to029Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory020to029Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory020to029Seconds.setUnits("seconds")
_CirbhStatsHistory030to039Seconds_Type = PerfIntervalCount
_CirbhStatsHistory030to039Seconds_Object = MibTableColumn
cirbhStatsHistory030to039Seconds = _CirbhStatsHistory030to039Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 7),
    _CirbhStatsHistory030to039Seconds_Type()
)
cirbhStatsHistory030to039Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory030to039Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory030to039Seconds.setUnits("seconds")
_CirbhStatsHistory040to049Seconds_Type = PerfIntervalCount
_CirbhStatsHistory040to049Seconds_Object = MibTableColumn
cirbhStatsHistory040to049Seconds = _CirbhStatsHistory040to049Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 8),
    _CirbhStatsHistory040to049Seconds_Type()
)
cirbhStatsHistory040to049Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory040to049Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory040to049Seconds.setUnits("seconds")
_CirbhStatsHistory050to059Seconds_Type = PerfIntervalCount
_CirbhStatsHistory050to059Seconds_Object = MibTableColumn
cirbhStatsHistory050to059Seconds = _CirbhStatsHistory050to059Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 9),
    _CirbhStatsHistory050to059Seconds_Type()
)
cirbhStatsHistory050to059Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory050to059Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory050to059Seconds.setUnits("seconds")
_CirbhStatsHistory060to069Seconds_Type = PerfIntervalCount
_CirbhStatsHistory060to069Seconds_Object = MibTableColumn
cirbhStatsHistory060to069Seconds = _CirbhStatsHistory060to069Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 10),
    _CirbhStatsHistory060to069Seconds_Type()
)
cirbhStatsHistory060to069Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory060to069Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory060to069Seconds.setUnits("seconds")
_CirbhStatsHistory070to079Seconds_Type = PerfIntervalCount
_CirbhStatsHistory070to079Seconds_Object = MibTableColumn
cirbhStatsHistory070to079Seconds = _CirbhStatsHistory070to079Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 11),
    _CirbhStatsHistory070to079Seconds_Type()
)
cirbhStatsHistory070to079Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory070to079Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory070to079Seconds.setUnits("seconds")
_CirbhStatsHistory080to089Seconds_Type = PerfIntervalCount
_CirbhStatsHistory080to089Seconds_Object = MibTableColumn
cirbhStatsHistory080to089Seconds = _CirbhStatsHistory080to089Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 12),
    _CirbhStatsHistory080to089Seconds_Type()
)
cirbhStatsHistory080to089Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory080to089Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory080to089Seconds.setUnits("seconds")
_CirbhStatsHistory090to100Seconds_Type = PerfIntervalCount
_CirbhStatsHistory090to100Seconds_Object = MibTableColumn
cirbhStatsHistory090to100Seconds = _CirbhStatsHistory090to100Seconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 13),
    _CirbhStatsHistory090to100Seconds_Type()
)
cirbhStatsHistory090to100Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistory090to100Seconds.setStatus("obsolete")
if mibBuilder.loadTexts:
    cirbhStatsHistory090to100Seconds.setUnits("seconds")
_CirbhStatsHistoryTimeStamp_Type = TimeStamp
_CirbhStatsHistoryTimeStamp_Object = MibTableColumn
cirbhStatsHistoryTimeStamp = _CirbhStatsHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 14),
    _CirbhStatsHistoryTimeStamp_Type()
)
cirbhStatsHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistoryTimeStamp.setStatus("obsolete")
_CirbhStatsHistoryMaxUtilization_Type = CirbhBackHaulUtilization
_CirbhStatsHistoryMaxUtilization_Object = MibTableColumn
cirbhStatsHistoryMaxUtilization = _CirbhStatsHistoryMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 15),
    _CirbhStatsHistoryMaxUtilization_Type()
)
cirbhStatsHistoryMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistoryMaxUtilization.setStatus("obsolete")
_CirbhStatsHistoryMaxTimeStamp_Type = TimeStamp
_CirbhStatsHistoryMaxTimeStamp_Object = MibTableColumn
cirbhStatsHistoryMaxTimeStamp = _CirbhStatsHistoryMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 16),
    _CirbhStatsHistoryMaxTimeStamp_Type()
)
cirbhStatsHistoryMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistoryMaxTimeStamp.setStatus("obsolete")
_CirbhStatsHistoryAverage_Type = CirbhBackHaulUtilization
_CirbhStatsHistoryAverage_Object = MibTableColumn
cirbhStatsHistoryAverage = _CirbhStatsHistoryAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 2, 12, 1, 17),
    _CirbhStatsHistoryAverage_Type()
)
cirbhStatsHistoryAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirbhStatsHistoryAverage.setStatus("obsolete")
_CirbhNotifEnables_ObjectIdentity = ObjectIdentity
cirbhNotifEnables = _CirbhNotifEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 3)
)


class _CirbhGsmAlarmNotifEnabled_Type(TruthValue):
    """Custom type cirbhGsmAlarmNotifEnabled based on TruthValue"""


_CirbhGsmAlarmNotifEnabled_Object = MibScalar
cirbhGsmAlarmNotifEnabled = _CirbhGsmAlarmNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 3, 1),
    _CirbhGsmAlarmNotifEnabled_Type()
)
cirbhGsmAlarmNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhGsmAlarmNotifEnabled.setStatus("current")


class _CirbhUmtsAlarmNotifEnabled_Type(TruthValue):
    """Custom type cirbhUmtsAlarmNotifEnabled based on TruthValue"""


_CirbhUmtsAlarmNotifEnabled_Object = MibScalar
cirbhUmtsAlarmNotifEnabled = _CirbhUmtsAlarmNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 3, 2),
    _CirbhUmtsAlarmNotifEnabled_Type()
)
cirbhUmtsAlarmNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhUmtsAlarmNotifEnabled.setStatus("current")


class _CirbhUtilNotifEnabled_Type(TruthValue):
    """Custom type cirbhUtilNotifEnabled based on TruthValue"""


_CirbhUtilNotifEnabled_Object = MibScalar
cirbhUtilNotifEnabled = _CirbhUtilNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 1, 3, 3),
    _CirbhUtilNotifEnabled_Type()
)
cirbhUtilNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cirbhUtilNotifEnabled.setStatus("deprecated")
_CiscoIpRanBackHaulMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpRanBackHaulMIBConform = _CiscoIpRanBackHaulMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2)
)
_CiscoIpRanBackHaulMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpRanBackHaulMIBCompliances = _CiscoIpRanBackHaulMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 1)
)
_CiscoIpRanBackHaulMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpRanBackHaulMIBGroups = _CiscoIpRanBackHaulMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2)
)

# Managed Objects groups

ciscoIpRanBackHaulScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 1)
)
ciscoIpRanBackHaulScalarsGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhSnmpTrafficMode"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhLocation"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulStatsInterval"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulStatsEntries"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulAcceptableThreshold"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulWarningThreshold"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulOverloadedThreshold"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulUtilInterval"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmNotifEnabled"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmNotifEnabled"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUtilNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulScalarsGroup.setStatus("deprecated")

ciscoIpRanBackHaulConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 2)
)
ciscoIpRanBackHaulConfigGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoProtocol"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoLocalAddrType"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoLocalAddr"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoLocalPortNumber"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoRemoteAddrType"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoRemoteAddr"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoRemotePortNumber"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulConfigGroup.setStatus("current")

ciscoIpRanBackHaulStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 3)
)
ciscoIpRanBackHaulStatsGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsRcvdSamples"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsSentSamples"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsRcvdBackHaulPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsSentBackHaulPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsRcvdBackHaulBytes"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsSentBackHaulBytes"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulStatsGroup.setStatus("current")

ciscoIpRanBackHaulAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 4)
)
ciscoIpRanBackHaulAlarmGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmConnectState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmLocalState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmRemoteState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmRedundancyState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsConnectionState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsConnectionRedundState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmRxLocalState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmRxRemoteState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmTxLocalState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmTxRemoteState"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulAlarmGroup.setStatus("current")

ciscoIpRanBackHaulErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 5)
)
ciscoIpRanBackHaulErrorsGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhPeerNotReadyDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhPeerNotActiveDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhInvalidPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhLostRcvdPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhLostSentPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhMissedPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhMissedLatePackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhMissedLostPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhMissedNoMemPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsBhMissedResetPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsDecompFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsCompFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsCompNoPacketFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsCompNoIntFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsCompIntDownFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsCompEncapFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhErrorsCompQosDrops"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulErrorsGroup.setStatus("deprecated")

ciscoIpRanBackHaulHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 6)
)
ciscoIpRanBackHaulHistoryGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulRcvdRate"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulSentRate"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulRcvdCompressRate"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulSentCompressRate"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulTimeStamp"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulRcvdUtilization"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulSentUtilization"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulRcvdUtilState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulSentUtilState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulRcvdUtil"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulSentUtil"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulAdjectSerialNum"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulAdjectVendorType"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulHistoryRcvdUtil"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulHistorySentUtil"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulHistoryRcvdAbisUtil"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulHistorySentAbisUtil"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulHistoryRcvdUmtsUtil"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulHistorySentUmtsUtil"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulHistoryTimeStamp"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats000to009Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats010to019Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats020to029Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats030to039Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats040to049Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats050to059Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats060to069Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats070to079Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats080to089Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStats090to100Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsTimeStamp"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsMaxUtilization"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsMaxTimeStamp"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory000to009Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory010to019Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory020to029Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory030to039Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory040to049Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory050to059Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory060to069Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory070to079Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory080to089Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistory090to100Seconds"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistoryTimeStamp"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistoryMaxUtilization"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistoryMaxTimeStamp"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhStatsHistoryAverage"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulHistoryGroup.setStatus("obsolete")

ciscoIpRanBackHaulShortHaulGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 8)
)
ciscoIpRanBackHaulShortHaulGroup.setObjects(
    ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulShortHaulTimestamp")
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulShortHaulGroup.setStatus("obsolete")

ciscoIpRanBackHaulAlarmGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 9)
)
ciscoIpRanBackHaulAlarmGroupSup1.setObjects(
    ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsConnectionRootIfIndex")
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulAlarmGroupSup1.setStatus("current")

ciscoIpRanBackHaulScalarsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 10)
)
ciscoIpRanBackHaulScalarsGroupRev2.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhSnmpTrafficMode"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhLocation"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmNotifEnabled"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulScalarsGroupRev2.setStatus("current")

ciscoIpRanBackHaulConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 11)
)
ciscoIpRanBackHaulConfigGroupSup2.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoAdjectSerialNum"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoAdjectVendorType"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoBackhaulRxIfIndex"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoBackhaulTxIfIndex"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoShBulkLastIndex"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulConfigGroupSup2.setStatus("current")

ciscoIpRanBackHaulHistoryGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 12)
)
ciscoIpRanBackHaulHistoryGroupRev2.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulRcvdRate"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulSentRate"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulRcvdCompressRate"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulSentCompressRate"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulTimeStamp"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulRcvdUtilization"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulSentUtilization"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulBulkTimeStamp"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulBulkBaseUnit"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulBulkUtil"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulHistoryGroupRev2.setStatus("obsolete")

ciscoIpRanBackHaulCongestionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 14)
)
ciscoIpRanBackHaulCongestionGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhCongestionEnabled"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhCongestionDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhCongestionDroppedBytes"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhCongestionEvents"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhCongestionActive"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhCongestionDuration"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulCongestionGroup.setStatus("current")

ciscoIpRanBackHaulGsmErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 15)
)
ciscoIpRanBackHaulGsmErrorsGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsPeerNotReadyDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsPeerNotActiveDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsInvalidPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsLostRcvdPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsLostSentPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsMissedPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsMissedLatePackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsMissedLostPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsMissedNoMemPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsMissedResetPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsDecompFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsCompFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsCompNoPacketFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsCompNoIntFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsCompIntDownFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsCompEncapFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsCompQosDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsFastSendFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsTxPacketFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsTxNoBuffers"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsTxResets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsOverruns"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsInterruptFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsLateArrivals"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmErrorsEarlyArrivals"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulGsmErrorsGroup.setStatus("current")

ciscoIpRanBackHaulUmtsErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 16)
)
ciscoIpRanBackHaulUmtsErrorsGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsPeerNotReadyDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsInvalidPackets"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsDecompFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsCompFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsCompNoPacketFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsCompNoIntFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsCompIntDownFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsCompEncapFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsCompQosDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsShorthaulPakFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsUmtsEncapFailures"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsLocalPvcDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsRemotePvcDrops"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsErrorsBackhaulDrops"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulUmtsErrorsGroup.setStatus("current")

ciscoIpRanBackHaulConfigGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 17)
)
ciscoIpRanBackHaulConfigGroupSup3.setObjects(
    ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhInfoOptimizeTraffic")
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulConfigGroupSup3.setStatus("current")

ciscoIpRanBackHaulHistoryGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 18)
)
ciscoIpRanBackHaulHistoryGroupRev3.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulBulkTimeStamp"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulBulkBaseUnit"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhShortHaulBulkUtil"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulHistoryGroupRev3.setStatus("current")


# Notification objects

ciscoIpRanBackHaulGsmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 0, 1)
)
ciscoIpRanBackHaulGsmAlarm.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmConnectState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmLocalState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmRemoteState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhGsmAlarmRedundancyState"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulGsmAlarm.setStatus(
        "current"
    )

ciscoIpRanBackHaulUmtsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 0, 2)
)
ciscoIpRanBackHaulUmtsAlarm.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsConnectionState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmRxLocalState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmRxRemoteState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmTxLocalState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsAlarmTxRemoteState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhUmtsConnectionRedundState"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulUmtsAlarm.setStatus(
        "current"
    )

ciscoIpRanBackHaulRcvdUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 0, 3)
)
ciscoIpRanBackHaulRcvdUtil.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulRcvdUtilState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulRcvdUtil"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulRcvdUtil.setStatus(
        "obsolete"
    )

ciscoIpRanBackHaulSentUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 0, 4)
)
ciscoIpRanBackHaulSentUtil.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulSentUtilState"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "cirbhBackHaulSentUtil"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulSentUtil.setStatus(
        "obsolete"
    )


# Notifications groups

ciscoIpRanBackHaulNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 7)
)
ciscoIpRanBackHaulNotifGroup.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "ciscoIpRanBackHaulGsmAlarm"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "ciscoIpRanBackHaulUmtsAlarm"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "ciscoIpRanBackHaulRcvdUtil"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "ciscoIpRanBackHaulSentUtil"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulNotifGroup.setStatus(
        "obsolete"
    )

ciscoIpRanBackHaulNotifGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 2, 13)
)
ciscoIpRanBackHaulNotifGroupRev2.setObjects(
      *(("CISCO-IP-RAN-BACKHAUL-MIB", "ciscoIpRanBackHaulGsmAlarm"),
        ("CISCO-IP-RAN-BACKHAUL-MIB", "ciscoIpRanBackHaulUmtsAlarm"))
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulNotifGroupRev2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIpRanBackHaulMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulMIBCompliance.setStatus(
        "obsolete"
    )

ciscoIpRanBackHaulMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulMIBComplianceRev1.setStatus(
        "obsolete"
    )

ciscoIpRanBackHaulMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulMIBComplianceRev2.setStatus(
        "obsolete"
    )

ciscoIpRanBackHaulMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 483, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoIpRanBackHaulMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-RAN-BACKHAUL-MIB",
    **{"CirbhAlarmState": CirbhAlarmState,
       "CirbhBackHaulUtilization": CirbhBackHaulUtilization,
       "CirbhBackHaulUtilizationState": CirbhBackHaulUtilizationState,
       "CirbhCommpressInterfaceRate": CirbhCommpressInterfaceRate,
       "CirbhConnectGsmState": CirbhConnectGsmState,
       "CirbhConnectUmtsState": CirbhConnectUmtsState,
       "CirbhHistoryIndex": CirbhHistoryIndex,
       "CirbhProtocol": CirbhProtocol,
       "CirbhRawInterfaceRate": CirbhRawInterfaceRate,
       "CirbhRedundancyState": CirbhRedundancyState,
       "CirbhShortHaulUtilization": CirbhShortHaulUtilization,
       "CirbhTrafficDirection": CirbhTrafficDirection,
       "CirbhTrafficType": CirbhTrafficType,
       "ciscoIpRanBackHaulMIB": ciscoIpRanBackHaulMIB,
       "ciscoIpRanBackHaulMIBNotifs": ciscoIpRanBackHaulMIBNotifs,
       "ciscoIpRanBackHaulGsmAlarm": ciscoIpRanBackHaulGsmAlarm,
       "ciscoIpRanBackHaulUmtsAlarm": ciscoIpRanBackHaulUmtsAlarm,
       "ciscoIpRanBackHaulRcvdUtil": ciscoIpRanBackHaulRcvdUtil,
       "ciscoIpRanBackHaulSentUtil": ciscoIpRanBackHaulSentUtil,
       "ciscoIpRanBackHaulMIBObjects": ciscoIpRanBackHaulMIBObjects,
       "cirbhScalars": cirbhScalars,
       "cirbhSnmpTrafficMode": cirbhSnmpTrafficMode,
       "cirbhLocation": cirbhLocation,
       "cirbhBackHaulStatsInterval": cirbhBackHaulStatsInterval,
       "cirbhBackHaulStatsEntries": cirbhBackHaulStatsEntries,
       "cirbhBackHaulAcceptableThreshold": cirbhBackHaulAcceptableThreshold,
       "cirbhBackHaulWarningThreshold": cirbhBackHaulWarningThreshold,
       "cirbhBackHaulOverloadedThreshold": cirbhBackHaulOverloadedThreshold,
       "cirbhBackHaulUtilInterval": cirbhBackHaulUtilInterval,
       "cirbhObjects": cirbhObjects,
       "cirbhShortHaul": cirbhShortHaul,
       "cirbhShortHaulInfo": cirbhShortHaulInfo,
       "cirbhInfoTable": cirbhInfoTable,
       "cirbhInfoTableEntry": cirbhInfoTableEntry,
       "cirbhInfoProtocol": cirbhInfoProtocol,
       "cirbhInfoLocalAddrType": cirbhInfoLocalAddrType,
       "cirbhInfoLocalAddr": cirbhInfoLocalAddr,
       "cirbhInfoLocalPortNumber": cirbhInfoLocalPortNumber,
       "cirbhInfoRemoteAddrType": cirbhInfoRemoteAddrType,
       "cirbhInfoRemoteAddr": cirbhInfoRemoteAddr,
       "cirbhInfoRemotePortNumber": cirbhInfoRemotePortNumber,
       "cirbhInfoAdjectSerialNum": cirbhInfoAdjectSerialNum,
       "cirbhInfoAdjectVendorType": cirbhInfoAdjectVendorType,
       "cirbhInfoBackhaulRxIfIndex": cirbhInfoBackhaulRxIfIndex,
       "cirbhInfoBackhaulTxIfIndex": cirbhInfoBackhaulTxIfIndex,
       "cirbhInfoShBulkLastIndex": cirbhInfoShBulkLastIndex,
       "cirbhInfoOptimizeTraffic": cirbhInfoOptimizeTraffic,
       "cirbhShortHaulAlarmInfo": cirbhShortHaulAlarmInfo,
       "cirbhGsmAlarmTable": cirbhGsmAlarmTable,
       "cirbhGsmAlarmTableEntry": cirbhGsmAlarmTableEntry,
       "cirbhGsmAlarmConnectState": cirbhGsmAlarmConnectState,
       "cirbhGsmAlarmLocalState": cirbhGsmAlarmLocalState,
       "cirbhGsmAlarmRemoteState": cirbhGsmAlarmRemoteState,
       "cirbhGsmAlarmRedundancyState": cirbhGsmAlarmRedundancyState,
       "cirbhUmtsConnectionTable": cirbhUmtsConnectionTable,
       "cirbhUmtsConnectionTableEntry": cirbhUmtsConnectionTableEntry,
       "cirbhUmtsConnectionState": cirbhUmtsConnectionState,
       "cirbhUmtsConnectionRedundState": cirbhUmtsConnectionRedundState,
       "cirbhUmtsConnectionRootIfIndex": cirbhUmtsConnectionRootIfIndex,
       "cirbhUmtsAlarmTable": cirbhUmtsAlarmTable,
       "cirbhUmtsAlarmTableEntry": cirbhUmtsAlarmTableEntry,
       "cirbhUmtsAlarmRxLocalState": cirbhUmtsAlarmRxLocalState,
       "cirbhUmtsAlarmRxRemoteState": cirbhUmtsAlarmRxRemoteState,
       "cirbhUmtsAlarmTxLocalState": cirbhUmtsAlarmTxLocalState,
       "cirbhUmtsAlarmTxRemoteState": cirbhUmtsAlarmTxRemoteState,
       "cirbhShortHaulStats": cirbhShortHaulStats,
       "cirbhStatsTable": cirbhStatsTable,
       "cirbhStatsTableEntry": cirbhStatsTableEntry,
       "cirbhStatsRcvdSamples": cirbhStatsRcvdSamples,
       "cirbhStatsSentSamples": cirbhStatsSentSamples,
       "cirbhStatsRcvdBackHaulPackets": cirbhStatsRcvdBackHaulPackets,
       "cirbhStatsSentBackHaulPackets": cirbhStatsSentBackHaulPackets,
       "cirbhStatsRcvdBackHaulBytes": cirbhStatsRcvdBackHaulBytes,
       "cirbhStatsSentBackHaulBytes": cirbhStatsSentBackHaulBytes,
       "cirbhErrorsTable": cirbhErrorsTable,
       "cirbhErrorsTableEntry": cirbhErrorsTableEntry,
       "cirbhErrorsBhPeerNotReadyDrops": cirbhErrorsBhPeerNotReadyDrops,
       "cirbhErrorsBhPeerNotActiveDrops": cirbhErrorsBhPeerNotActiveDrops,
       "cirbhErrorsBhInvalidPackets": cirbhErrorsBhInvalidPackets,
       "cirbhErrorsBhLostRcvdPackets": cirbhErrorsBhLostRcvdPackets,
       "cirbhErrorsBhLostSentPackets": cirbhErrorsBhLostSentPackets,
       "cirbhErrorsBhMissedPackets": cirbhErrorsBhMissedPackets,
       "cirbhErrorsBhMissedLatePackets": cirbhErrorsBhMissedLatePackets,
       "cirbhErrorsBhMissedLostPackets": cirbhErrorsBhMissedLostPackets,
       "cirbhErrorsBhMissedNoMemPackets": cirbhErrorsBhMissedNoMemPackets,
       "cirbhErrorsBhMissedResetPackets": cirbhErrorsBhMissedResetPackets,
       "cirbhErrorsDecompFailures": cirbhErrorsDecompFailures,
       "cirbhErrorsCompFailures": cirbhErrorsCompFailures,
       "cirbhErrorsCompNoPacketFailures": cirbhErrorsCompNoPacketFailures,
       "cirbhErrorsCompNoIntFailures": cirbhErrorsCompNoIntFailures,
       "cirbhErrorsCompIntDownFailures": cirbhErrorsCompIntDownFailures,
       "cirbhErrorsCompEncapFailures": cirbhErrorsCompEncapFailures,
       "cirbhErrorsCompQosDrops": cirbhErrorsCompQosDrops,
       "cirbhShortHaulHistoryTable": cirbhShortHaulHistoryTable,
       "cirbhShortHaulHistoryTableEntry": cirbhShortHaulHistoryTableEntry,
       "cirbhShortHaulHistory": cirbhShortHaulHistory,
       "cirbhShortHaulRcvdRate": cirbhShortHaulRcvdRate,
       "cirbhShortHaulSentRate": cirbhShortHaulSentRate,
       "cirbhShortHaulRcvdCompressRate": cirbhShortHaulRcvdCompressRate,
       "cirbhShortHaulSentCompressRate": cirbhShortHaulSentCompressRate,
       "cirbhShortHaulTimeStamp": cirbhShortHaulTimeStamp,
       "cirbhShortHaulRcvdUtilization": cirbhShortHaulRcvdUtilization,
       "cirbhShortHaulSentUtilization": cirbhShortHaulSentUtilization,
       "cirbhCongestionTable": cirbhCongestionTable,
       "cirbhCongestionTableEntry": cirbhCongestionTableEntry,
       "cirbhCongestionEnabled": cirbhCongestionEnabled,
       "cirbhCongestionDrops": cirbhCongestionDrops,
       "cirbhCongestionDroppedBytes": cirbhCongestionDroppedBytes,
       "cirbhCongestionEvents": cirbhCongestionEvents,
       "cirbhCongestionActive": cirbhCongestionActive,
       "cirbhCongestionDuration": cirbhCongestionDuration,
       "cirbhGsmErrorsTable": cirbhGsmErrorsTable,
       "cirbhGsmErrorsTableEntry": cirbhGsmErrorsTableEntry,
       "cirbhGsmErrorsPeerNotReadyDrops": cirbhGsmErrorsPeerNotReadyDrops,
       "cirbhGsmErrorsPeerNotActiveDrops": cirbhGsmErrorsPeerNotActiveDrops,
       "cirbhGsmErrorsInvalidPackets": cirbhGsmErrorsInvalidPackets,
       "cirbhGsmErrorsLostRcvdPackets": cirbhGsmErrorsLostRcvdPackets,
       "cirbhGsmErrorsLostSentPackets": cirbhGsmErrorsLostSentPackets,
       "cirbhGsmErrorsMissedPackets": cirbhGsmErrorsMissedPackets,
       "cirbhGsmErrorsMissedLatePackets": cirbhGsmErrorsMissedLatePackets,
       "cirbhGsmErrorsMissedLostPackets": cirbhGsmErrorsMissedLostPackets,
       "cirbhGsmErrorsMissedNoMemPackets": cirbhGsmErrorsMissedNoMemPackets,
       "cirbhGsmErrorsMissedResetPackets": cirbhGsmErrorsMissedResetPackets,
       "cirbhGsmErrorsDecompFailures": cirbhGsmErrorsDecompFailures,
       "cirbhGsmErrorsCompFailures": cirbhGsmErrorsCompFailures,
       "cirbhGsmErrorsCompNoPacketFailures": cirbhGsmErrorsCompNoPacketFailures,
       "cirbhGsmErrorsCompNoIntFailures": cirbhGsmErrorsCompNoIntFailures,
       "cirbhGsmErrorsCompIntDownFailures": cirbhGsmErrorsCompIntDownFailures,
       "cirbhGsmErrorsCompEncapFailures": cirbhGsmErrorsCompEncapFailures,
       "cirbhGsmErrorsCompQosDrops": cirbhGsmErrorsCompQosDrops,
       "cirbhGsmErrorsFastSendFailures": cirbhGsmErrorsFastSendFailures,
       "cirbhGsmErrorsTxPacketFailures": cirbhGsmErrorsTxPacketFailures,
       "cirbhGsmErrorsTxNoBuffers": cirbhGsmErrorsTxNoBuffers,
       "cirbhGsmErrorsTxResets": cirbhGsmErrorsTxResets,
       "cirbhGsmErrorsOverruns": cirbhGsmErrorsOverruns,
       "cirbhGsmErrorsInterruptFailures": cirbhGsmErrorsInterruptFailures,
       "cirbhGsmErrorsLateArrivals": cirbhGsmErrorsLateArrivals,
       "cirbhGsmErrorsEarlyArrivals": cirbhGsmErrorsEarlyArrivals,
       "cirbhUmtsErrorsTable": cirbhUmtsErrorsTable,
       "cirbhUmtsErrorsTableEntry": cirbhUmtsErrorsTableEntry,
       "cirbhUmtsErrorsPeerNotReadyDrops": cirbhUmtsErrorsPeerNotReadyDrops,
       "cirbhUmtsErrorsInvalidPackets": cirbhUmtsErrorsInvalidPackets,
       "cirbhUmtsErrorsDecompFailures": cirbhUmtsErrorsDecompFailures,
       "cirbhUmtsErrorsCompFailures": cirbhUmtsErrorsCompFailures,
       "cirbhUmtsErrorsCompNoPacketFailures": cirbhUmtsErrorsCompNoPacketFailures,
       "cirbhUmtsErrorsCompNoIntFailures": cirbhUmtsErrorsCompNoIntFailures,
       "cirbhUmtsErrorsCompIntDownFailures": cirbhUmtsErrorsCompIntDownFailures,
       "cirbhUmtsErrorsCompEncapFailures": cirbhUmtsErrorsCompEncapFailures,
       "cirbhUmtsErrorsCompQosDrops": cirbhUmtsErrorsCompQosDrops,
       "cirbhUmtsErrorsShorthaulPakFailures": cirbhUmtsErrorsShorthaulPakFailures,
       "cirbhUmtsErrorsUmtsEncapFailures": cirbhUmtsErrorsUmtsEncapFailures,
       "cirbhUmtsErrorsLocalPvcDrops": cirbhUmtsErrorsLocalPvcDrops,
       "cirbhUmtsErrorsRemotePvcDrops": cirbhUmtsErrorsRemotePvcDrops,
       "cirbhUmtsErrorsBackhaulDrops": cirbhUmtsErrorsBackhaulDrops,
       "cirbhShortHaulBulkTable": cirbhShortHaulBulkTable,
       "cirbhShortHaulBulkTableEntry": cirbhShortHaulBulkTableEntry,
       "cirbhShortHaulBulkHistory": cirbhShortHaulBulkHistory,
       "cirbhShortHaulBulkTimeStamp": cirbhShortHaulBulkTimeStamp,
       "cirbhShortHaulBulkBaseUnit": cirbhShortHaulBulkBaseUnit,
       "cirbhShortHaulBulkUtil": cirbhShortHaulBulkUtil,
       "cirbhBackHaul": cirbhBackHaul,
       "cirbhBackHaulInfo": cirbhBackHaulInfo,
       "cirbhBackHaulTable": cirbhBackHaulTable,
       "cirbhBackHaulEntry": cirbhBackHaulEntry,
       "cirbhBackHaulAdjectSerialNum": cirbhBackHaulAdjectSerialNum,
       "cirbhBackHaulAdjectVendorType": cirbhBackHaulAdjectVendorType,
       "cirbhBackHaulRcvdUtilState": cirbhBackHaulRcvdUtilState,
       "cirbhBackHaulSentUtilState": cirbhBackHaulSentUtilState,
       "cirbhBackHaulRcvdUtil": cirbhBackHaulRcvdUtil,
       "cirbhBackHaulSentUtil": cirbhBackHaulSentUtil,
       "cirbhBackHaulShortHaulTable": cirbhBackHaulShortHaulTable,
       "cirbhBackHaulShortHaulEntry": cirbhBackHaulShortHaulEntry,
       "cirbhBackHaulShortHaulBhIndex": cirbhBackHaulShortHaulBhIndex,
       "cirbhBackHaulShortHaulShIndex": cirbhBackHaulShortHaulShIndex,
       "cirbhBackHaulShortHaulTimestamp": cirbhBackHaulShortHaulTimestamp,
       "cirbhBackHaulStats": cirbhBackHaulStats,
       "cirbhBackHaulHistoryTable": cirbhBackHaulHistoryTable,
       "cirbhBackHaulHistoryEntry": cirbhBackHaulHistoryEntry,
       "cirbhBackHaulHistoryIndex": cirbhBackHaulHistoryIndex,
       "cirbhBackHaulHistoryRcvdUtil": cirbhBackHaulHistoryRcvdUtil,
       "cirbhBackHaulHistorySentUtil": cirbhBackHaulHistorySentUtil,
       "cirbhBackHaulHistoryRcvdAbisUtil": cirbhBackHaulHistoryRcvdAbisUtil,
       "cirbhBackHaulHistorySentAbisUtil": cirbhBackHaulHistorySentAbisUtil,
       "cirbhBackHaulHistoryRcvdUmtsUtil": cirbhBackHaulHistoryRcvdUmtsUtil,
       "cirbhBackHaulHistorySentUmtsUtil": cirbhBackHaulHistorySentUmtsUtil,
       "cirbhBackHaulHistoryTimeStamp": cirbhBackHaulHistoryTimeStamp,
       "cirbhBackHaulStatsTable": cirbhBackHaulStatsTable,
       "cirbhBackHaulStatsEntry": cirbhBackHaulStatsEntry,
       "cirbhStatsDirection": cirbhStatsDirection,
       "cirbhStatsTrafficType": cirbhStatsTrafficType,
       "cirbhStats000to009Seconds": cirbhStats000to009Seconds,
       "cirbhStats010to019Seconds": cirbhStats010to019Seconds,
       "cirbhStats020to029Seconds": cirbhStats020to029Seconds,
       "cirbhStats030to039Seconds": cirbhStats030to039Seconds,
       "cirbhStats040to049Seconds": cirbhStats040to049Seconds,
       "cirbhStats050to059Seconds": cirbhStats050to059Seconds,
       "cirbhStats060to069Seconds": cirbhStats060to069Seconds,
       "cirbhStats070to079Seconds": cirbhStats070to079Seconds,
       "cirbhStats080to089Seconds": cirbhStats080to089Seconds,
       "cirbhStats090to100Seconds": cirbhStats090to100Seconds,
       "cirbhStatsTimeStamp": cirbhStatsTimeStamp,
       "cirbhStatsMaxUtilization": cirbhStatsMaxUtilization,
       "cirbhStatsMaxTimeStamp": cirbhStatsMaxTimeStamp,
       "cirbhBackHaulStatsHistoryTable": cirbhBackHaulStatsHistoryTable,
       "cirbhBackHaulStatsHistoryEntry": cirbhBackHaulStatsHistoryEntry,
       "cirbhStatsHistoryIndex": cirbhStatsHistoryIndex,
       "cirbhStatsHistoryDirection": cirbhStatsHistoryDirection,
       "cirbhStatsHistoryTrafficType": cirbhStatsHistoryTrafficType,
       "cirbhStatsHistory000to009Seconds": cirbhStatsHistory000to009Seconds,
       "cirbhStatsHistory010to019Seconds": cirbhStatsHistory010to019Seconds,
       "cirbhStatsHistory020to029Seconds": cirbhStatsHistory020to029Seconds,
       "cirbhStatsHistory030to039Seconds": cirbhStatsHistory030to039Seconds,
       "cirbhStatsHistory040to049Seconds": cirbhStatsHistory040to049Seconds,
       "cirbhStatsHistory050to059Seconds": cirbhStatsHistory050to059Seconds,
       "cirbhStatsHistory060to069Seconds": cirbhStatsHistory060to069Seconds,
       "cirbhStatsHistory070to079Seconds": cirbhStatsHistory070to079Seconds,
       "cirbhStatsHistory080to089Seconds": cirbhStatsHistory080to089Seconds,
       "cirbhStatsHistory090to100Seconds": cirbhStatsHistory090to100Seconds,
       "cirbhStatsHistoryTimeStamp": cirbhStatsHistoryTimeStamp,
       "cirbhStatsHistoryMaxUtilization": cirbhStatsHistoryMaxUtilization,
       "cirbhStatsHistoryMaxTimeStamp": cirbhStatsHistoryMaxTimeStamp,
       "cirbhStatsHistoryAverage": cirbhStatsHistoryAverage,
       "cirbhNotifEnables": cirbhNotifEnables,
       "cirbhGsmAlarmNotifEnabled": cirbhGsmAlarmNotifEnabled,
       "cirbhUmtsAlarmNotifEnabled": cirbhUmtsAlarmNotifEnabled,
       "cirbhUtilNotifEnabled": cirbhUtilNotifEnabled,
       "ciscoIpRanBackHaulMIBConform": ciscoIpRanBackHaulMIBConform,
       "ciscoIpRanBackHaulMIBCompliances": ciscoIpRanBackHaulMIBCompliances,
       "ciscoIpRanBackHaulMIBCompliance": ciscoIpRanBackHaulMIBCompliance,
       "ciscoIpRanBackHaulMIBComplianceRev1": ciscoIpRanBackHaulMIBComplianceRev1,
       "ciscoIpRanBackHaulMIBComplianceRev2": ciscoIpRanBackHaulMIBComplianceRev2,
       "ciscoIpRanBackHaulMIBComplianceRev3": ciscoIpRanBackHaulMIBComplianceRev3,
       "ciscoIpRanBackHaulMIBGroups": ciscoIpRanBackHaulMIBGroups,
       "ciscoIpRanBackHaulScalarsGroup": ciscoIpRanBackHaulScalarsGroup,
       "ciscoIpRanBackHaulConfigGroup": ciscoIpRanBackHaulConfigGroup,
       "ciscoIpRanBackHaulStatsGroup": ciscoIpRanBackHaulStatsGroup,
       "ciscoIpRanBackHaulAlarmGroup": ciscoIpRanBackHaulAlarmGroup,
       "ciscoIpRanBackHaulErrorsGroup": ciscoIpRanBackHaulErrorsGroup,
       "ciscoIpRanBackHaulHistoryGroup": ciscoIpRanBackHaulHistoryGroup,
       "ciscoIpRanBackHaulNotifGroup": ciscoIpRanBackHaulNotifGroup,
       "ciscoIpRanBackHaulShortHaulGroup": ciscoIpRanBackHaulShortHaulGroup,
       "ciscoIpRanBackHaulAlarmGroupSup1": ciscoIpRanBackHaulAlarmGroupSup1,
       "ciscoIpRanBackHaulScalarsGroupRev2": ciscoIpRanBackHaulScalarsGroupRev2,
       "ciscoIpRanBackHaulConfigGroupSup2": ciscoIpRanBackHaulConfigGroupSup2,
       "ciscoIpRanBackHaulHistoryGroupRev2": ciscoIpRanBackHaulHistoryGroupRev2,
       "ciscoIpRanBackHaulNotifGroupRev2": ciscoIpRanBackHaulNotifGroupRev2,
       "ciscoIpRanBackHaulCongestionGroup": ciscoIpRanBackHaulCongestionGroup,
       "ciscoIpRanBackHaulGsmErrorsGroup": ciscoIpRanBackHaulGsmErrorsGroup,
       "ciscoIpRanBackHaulUmtsErrorsGroup": ciscoIpRanBackHaulUmtsErrorsGroup,
       "ciscoIpRanBackHaulConfigGroupSup3": ciscoIpRanBackHaulConfigGroupSup3,
       "ciscoIpRanBackHaulHistoryGroupRev3": ciscoIpRanBackHaulHistoryGroupRev3}
)
