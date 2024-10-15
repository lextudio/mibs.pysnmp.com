# SNMP MIB module (HUAWEI-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:42 2024
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

(huaweiMgmt,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiMgmt")

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwAaa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2)
)
hwAaa.setRevisions(
        ("2015-06-10 12:50",
         "2015-04-23 16:55",
         "2015-04-17 12:50",
         "2015-03-10 12:50",
         "2014-12-26 16:17",
         "2014-09-06 16:17",
         "2014-09-03 10:50",
         "2014-08-20 10:50",
         "2014-08-06 10:50",
         "2014-07-14 10:50",
         "2014-03-06 10:50",
         "2013-12-17 10:30",
         "2013-12-13 17:25",
         "2013-10-15 17:25",
         "2013-08-08 20:12",
         "2013-07-19 18:00",
         "2013-07-04 17:09",
         "2013-06-27 17:19",
         "2013-04-17 09:19",
         "2013-04-03 22:22",
         "2013-03-15 11:11",
         "2013-09-14 15:18",
         "2013-11-28 16:51",
         "2014-03-18 10:51",
         "2014-03-24 10:51",
         "2014-04-17 10:26",
         "2014-04-17 10:27",
         "2014-07-08 15:44",
         "2014-08-12 17:25",
         "2014-08-27 15:44",
         "2014-08-27 15:44",
         "2014-09-21 15:44",
         "2014-12-27 15:44",
         "2014-12-31 15:44",
         "2014-12-26 16:17",
         "2015-01-23 10:25",
         "2015-03-20 13:14",
         "2015-03-26 09:35",
         "2015-07-07 20:36",
         "2015-07-16 17:11",
         "2015-07-28 16:41",
         "2015-07-28 20:55",
         "2015-07-28 21:00",
         "2015-07-31 09:17",
         "2015-08-08 09:35",
         "2015-08-26 16:05",
         "2015-09-11 11:38")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwAAAMibObjects_ObjectIdentity = ObjectIdentity
hwAAAMibObjects = _HwAAAMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1)
)
_HwAuthenSchemeTable_Object = MibTable
hwAuthenSchemeTable = _HwAuthenSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwAuthenSchemeTable.setStatus("current")
_HwAuthenSchemeEntry_Object = MibTableRow
hwAuthenSchemeEntry = _HwAuthenSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 1, 1)
)
hwAuthenSchemeEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAuthenSchemeName"),
)
if mibBuilder.loadTexts:
    hwAuthenSchemeEntry.setStatus("current")


class _HwAuthenSchemeName_Type(DisplayString):
    """Custom type hwAuthenSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwAuthenSchemeName_Type.__name__ = "DisplayString"
_HwAuthenSchemeName_Object = MibTableColumn
hwAuthenSchemeName = _HwAuthenSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 1, 1, 1),
    _HwAuthenSchemeName_Type()
)
hwAuthenSchemeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthenSchemeName.setStatus("current")


class _HwAuthenMethod_Type(Integer32):
    """Custom type hwAuthenMethod based on Integer32"""
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
        *(("local", 1),
          ("localNoauth", 11),
          ("localRadius", 4),
          ("localRadiusNoauth", 14),
          ("localRadiusTacacs", 20),
          ("localRadiusTacacsNoauth", 26),
          ("localTacacs", 9),
          ("localTacacsNoauth", 15),
          ("localTacacsRadius", 22),
          ("localTacacsRadiusNoauth", 27),
          ("noauth", 2),
          ("radius", 3),
          ("radiusLocal", 5),
          ("radiusLocalNoauth", 16),
          ("radiusLocalTacacs", 21),
          ("radiusLocalTacacsNoauth", 28),
          ("radiusNoauth", 6),
          ("radiusProxy", 32),
          ("radiusTacacs", 12),
          ("radiusTacacsLocal", 23),
          ("radiusTacacsLocalNoauth", 29),
          ("radiusTacacsNoauth", 17),
          ("tacacs", 7),
          ("tacacsLocal", 8),
          ("tacacsLocalNoauth", 18),
          ("tacacsLocalRadius", 24),
          ("tacacsLocalRadiusNoauth", 30),
          ("tacacsNoauth", 10),
          ("tacacsRadius", 13),
          ("tacacsRadiusLocal", 25),
          ("tacacsRadiusLocalNoauth", 31),
          ("tacacsRadiusNoauth", 19))
    )


_HwAuthenMethod_Type.__name__ = "Integer32"
_HwAuthenMethod_Object = MibTableColumn
hwAuthenMethod = _HwAuthenMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 1, 1, 2),
    _HwAuthenMethod_Type()
)
hwAuthenMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAuthenMethod.setStatus("current")
_HwAuthenRowStatus_Type = RowStatus
_HwAuthenRowStatus_Object = MibTableColumn
hwAuthenRowStatus = _HwAuthenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 1, 1, 3),
    _HwAuthenRowStatus_Type()
)
hwAuthenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAuthenRowStatus.setStatus("current")


class _HwAuthenFailPolicy_Type(Integer32):
    """Custom type hwAuthenFailPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HwAuthenFailPolicy_Type.__name__ = "Integer32"
_HwAuthenFailPolicy_Object = MibTableColumn
hwAuthenFailPolicy = _HwAuthenFailPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 1, 1, 4),
    _HwAuthenFailPolicy_Type()
)
hwAuthenFailPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAuthenFailPolicy.setStatus("current")


class _HwAuthenFailDomain_Type(DisplayString):
    """Custom type hwAuthenFailDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwAuthenFailDomain_Type.__name__ = "DisplayString"
_HwAuthenFailDomain_Object = MibTableColumn
hwAuthenFailDomain = _HwAuthenFailDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 1, 1, 5),
    _HwAuthenFailDomain_Type()
)
hwAuthenFailDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAuthenFailDomain.setStatus("current")
_HwAcctSchemeTable_Object = MibTable
hwAcctSchemeTable = _HwAcctSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwAcctSchemeTable.setStatus("current")
_HwAcctSchemeEntry_Object = MibTableRow
hwAcctSchemeEntry = _HwAcctSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 2, 1)
)
hwAcctSchemeEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAcctSchemeName"),
)
if mibBuilder.loadTexts:
    hwAcctSchemeEntry.setStatus("current")


class _HwAcctSchemeName_Type(DisplayString):
    """Custom type hwAcctSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwAcctSchemeName_Type.__name__ = "DisplayString"
_HwAcctSchemeName_Object = MibTableColumn
hwAcctSchemeName = _HwAcctSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 2, 1, 1),
    _HwAcctSchemeName_Type()
)
hwAcctSchemeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcctSchemeName.setStatus("current")


class _HwAccMethod_Type(Integer32):
    """Custom type hwAccMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hwtacacs", 5),
          ("noacct", 2),
          ("radius", 3))
    )


_HwAccMethod_Type.__name__ = "Integer32"
_HwAccMethod_Object = MibTableColumn
hwAccMethod = _HwAccMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 2, 1, 2),
    _HwAccMethod_Type()
)
hwAccMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAccMethod.setStatus("current")


class _HwAcctStartFail_Type(Integer32):
    """Custom type hwAcctStartFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("offline", 2))
    )


_HwAcctStartFail_Type.__name__ = "Integer32"
_HwAcctStartFail_Object = MibTableColumn
hwAcctStartFail = _HwAcctStartFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 2, 1, 3),
    _HwAcctStartFail_Type()
)
hwAcctStartFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAcctStartFail.setStatus("current")


class _HwAcctOnlineFail_Type(Integer32):
    """Custom type hwAcctOnlineFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("offline", 2))
    )


_HwAcctOnlineFail_Type.__name__ = "Integer32"
_HwAcctOnlineFail_Object = MibTableColumn
hwAcctOnlineFail = _HwAcctOnlineFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 2, 1, 4),
    _HwAcctOnlineFail_Type()
)
hwAcctOnlineFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAcctOnlineFail.setStatus("current")
_HwAccRealTimeInter_Type = Integer32
_HwAccRealTimeInter_Object = MibTableColumn
hwAccRealTimeInter = _HwAccRealTimeInter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 2, 1, 5),
    _HwAccRealTimeInter_Type()
)
hwAccRealTimeInter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAccRealTimeInter.setStatus("current")
_HwAcctRowStatus_Type = RowStatus
_HwAcctRowStatus_Object = MibTableColumn
hwAcctRowStatus = _HwAcctRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 2, 1, 6),
    _HwAcctRowStatus_Type()
)
hwAcctRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAcctRowStatus.setStatus("current")


class _HwAcctRealTimeIntervalUnit_Type(Integer32):
    """Custom type hwAcctRealTimeIntervalUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("minute", 1),
          ("none", 3),
          ("second", 2))
    )


_HwAcctRealTimeIntervalUnit_Type.__name__ = "Integer32"
_HwAcctRealTimeIntervalUnit_Object = MibTableColumn
hwAcctRealTimeIntervalUnit = _HwAcctRealTimeIntervalUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 2, 1, 7),
    _HwAcctRealTimeIntervalUnit_Type()
)
hwAcctRealTimeIntervalUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAcctRealTimeIntervalUnit.setStatus("current")
_HwDomainTable_Object = MibTable
hwDomainTable = _HwDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwDomainTable.setStatus("current")
_HwDomainEntry_Object = MibTableRow
hwDomainEntry = _HwDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1)
)
hwDomainEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwDomainName"),
)
if mibBuilder.loadTexts:
    hwDomainEntry.setStatus("current")


class _HwDomainName_Type(DisplayString):
    """Custom type hwDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwDomainName_Type.__name__ = "DisplayString"
_HwDomainName_Object = MibTableColumn
hwDomainName = _HwDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 1),
    _HwDomainName_Type()
)
hwDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainName.setStatus("current")


class _HwDomainAuthenSchemeName_Type(DisplayString):
    """Custom type hwDomainAuthenSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainAuthenSchemeName_Type.__name__ = "DisplayString"
_HwDomainAuthenSchemeName_Object = MibTableColumn
hwDomainAuthenSchemeName = _HwDomainAuthenSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 2),
    _HwDomainAuthenSchemeName_Type()
)
hwDomainAuthenSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainAuthenSchemeName.setStatus("current")


class _HwDomainAcctSchemeName_Type(DisplayString):
    """Custom type hwDomainAcctSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainAcctSchemeName_Type.__name__ = "DisplayString"
_HwDomainAcctSchemeName_Object = MibTableColumn
hwDomainAcctSchemeName = _HwDomainAcctSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 3),
    _HwDomainAcctSchemeName_Type()
)
hwDomainAcctSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainAcctSchemeName.setStatus("current")


class _HwDomainRadiusGroupName_Type(DisplayString):
    """Custom type hwDomainRadiusGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDomainRadiusGroupName_Type.__name__ = "DisplayString"
_HwDomainRadiusGroupName_Object = MibTableColumn
hwDomainRadiusGroupName = _HwDomainRadiusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 4),
    _HwDomainRadiusGroupName_Type()
)
hwDomainRadiusGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainRadiusGroupName.setStatus("current")


class _HwDomainAccessLimitNum_Type(Integer32):
    """Custom type hwDomainAccessLimitNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 283648),
    )


_HwDomainAccessLimitNum_Type.__name__ = "Integer32"
_HwDomainAccessLimitNum_Object = MibTableColumn
hwDomainAccessLimitNum = _HwDomainAccessLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 6),
    _HwDomainAccessLimitNum_Type()
)
hwDomainAccessLimitNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainAccessLimitNum.setStatus("current")
_HwDomainIfSrcRoute_Type = TruthValue
_HwDomainIfSrcRoute_Object = MibTableColumn
hwDomainIfSrcRoute = _HwDomainIfSrcRoute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 7),
    _HwDomainIfSrcRoute_Type()
)
hwDomainIfSrcRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIfSrcRoute.setStatus("current")
_HwDomainNextHopIP_Type = IpAddress
_HwDomainNextHopIP_Object = MibTableColumn
hwDomainNextHopIP = _HwDomainNextHopIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 8),
    _HwDomainNextHopIP_Type()
)
hwDomainNextHopIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainNextHopIP.setStatus("current")


class _HwDomainIdleCutTime_Type(Integer32):
    """Custom type hwDomainIdleCutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_HwDomainIdleCutTime_Type.__name__ = "Integer32"
_HwDomainIdleCutTime_Object = MibTableColumn
hwDomainIdleCutTime = _HwDomainIdleCutTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 9),
    _HwDomainIdleCutTime_Type()
)
hwDomainIdleCutTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainIdleCutTime.setStatus("current")


class _HwDomainIdleCutFlow_Type(Integer32):
    """Custom type hwDomainIdleCutFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 768000),
    )


_HwDomainIdleCutFlow_Type.__name__ = "Integer32"
_HwDomainIdleCutFlow_Object = MibTableColumn
hwDomainIdleCutFlow = _HwDomainIdleCutFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 10),
    _HwDomainIdleCutFlow_Type()
)
hwDomainIdleCutFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainIdleCutFlow.setStatus("current")
_HwDomainRowStatus_Type = RowStatus
_HwDomainRowStatus_Object = MibTableColumn
hwDomainRowStatus = _HwDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 11),
    _HwDomainRowStatus_Type()
)
hwDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainRowStatus.setStatus("current")


class _HwDomainType_Type(Integer32):
    """Custom type hwDomainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device", 2),
          ("normal", 1))
    )


_HwDomainType_Type.__name__ = "Integer32"
_HwDomainType_Object = MibTableColumn
hwDomainType = _HwDomainType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 12),
    _HwDomainType_Type()
)
hwDomainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainType.setStatus("current")


class _HwDomainServiceSchemeName_Type(DisplayString):
    """Custom type hwDomainServiceSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainServiceSchemeName_Type.__name__ = "DisplayString"
_HwDomainServiceSchemeName_Object = MibTableColumn
hwDomainServiceSchemeName = _HwDomainServiceSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 13),
    _HwDomainServiceSchemeName_Type()
)
hwDomainServiceSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainServiceSchemeName.setStatus("current")


class _HwDomainIdleCutType_Type(Integer32):
    """Custom type hwDomainIdleCutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("inbound", 2),
          ("outbound", 3))
    )


_HwDomainIdleCutType_Type.__name__ = "Integer32"
_HwDomainIdleCutType_Object = MibTableColumn
hwDomainIdleCutType = _HwDomainIdleCutType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 14),
    _HwDomainIdleCutType_Type()
)
hwDomainIdleCutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainIdleCutType.setStatus("current")


class _Hwdomainipv6nexthop_Type(DisplayString):
    """Custom type hwdomainipv6nexthop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hwdomainipv6nexthop_Type.__name__ = "DisplayString"
_Hwdomainipv6nexthop_Object = MibTableColumn
hwdomainipv6nexthop = _Hwdomainipv6nexthop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 15),
    _Hwdomainipv6nexthop_Type()
)
hwdomainipv6nexthop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdomainipv6nexthop.setStatus("current")


class _HwDomainForcePushUrl_Type(DisplayString):
    """Custom type hwDomainForcePushUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HwDomainForcePushUrl_Type.__name__ = "DisplayString"
_HwDomainForcePushUrl_Object = MibTableColumn
hwDomainForcePushUrl = _HwDomainForcePushUrl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 16),
    _HwDomainForcePushUrl_Type()
)
hwDomainForcePushUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainForcePushUrl.setStatus("current")


class _HwDomainForcePushUrlTemplate_Type(DisplayString):
    """Custom type hwDomainForcePushUrlTemplate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwDomainForcePushUrlTemplate_Type.__name__ = "DisplayString"
_HwDomainForcePushUrlTemplate_Object = MibTableColumn
hwDomainForcePushUrlTemplate = _HwDomainForcePushUrlTemplate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 17),
    _HwDomainForcePushUrlTemplate_Type()
)
hwDomainForcePushUrlTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainForcePushUrlTemplate.setStatus("current")


class _HwStateBlockFirstTimeRangeName_Type(DisplayString):
    """Custom type hwStateBlockFirstTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwStateBlockFirstTimeRangeName_Type.__name__ = "DisplayString"
_HwStateBlockFirstTimeRangeName_Object = MibTableColumn
hwStateBlockFirstTimeRangeName = _HwStateBlockFirstTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 18),
    _HwStateBlockFirstTimeRangeName_Type()
)
hwStateBlockFirstTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStateBlockFirstTimeRangeName.setStatus("current")


class _HwStateBlockSecondTimeRangeName_Type(DisplayString):
    """Custom type hwStateBlockSecondTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwStateBlockSecondTimeRangeName_Type.__name__ = "DisplayString"
_HwStateBlockSecondTimeRangeName_Object = MibTableColumn
hwStateBlockSecondTimeRangeName = _HwStateBlockSecondTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 19),
    _HwStateBlockSecondTimeRangeName_Type()
)
hwStateBlockSecondTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStateBlockSecondTimeRangeName.setStatus("current")


class _HwStateBlockThirdTimeRangeName_Type(DisplayString):
    """Custom type hwStateBlockThirdTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwStateBlockThirdTimeRangeName_Type.__name__ = "DisplayString"
_HwStateBlockThirdTimeRangeName_Object = MibTableColumn
hwStateBlockThirdTimeRangeName = _HwStateBlockThirdTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 20),
    _HwStateBlockThirdTimeRangeName_Type()
)
hwStateBlockThirdTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStateBlockThirdTimeRangeName.setStatus("current")


class _HwStateBlockForthTimeRangeName_Type(DisplayString):
    """Custom type hwStateBlockForthTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwStateBlockForthTimeRangeName_Type.__name__ = "DisplayString"
_HwStateBlockForthTimeRangeName_Object = MibTableColumn
hwStateBlockForthTimeRangeName = _HwStateBlockForthTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 21),
    _HwStateBlockForthTimeRangeName_Type()
)
hwStateBlockForthTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStateBlockForthTimeRangeName.setStatus("current")


class _HwDomainFlowStatistic_Type(Integer32):
    """Custom type hwDomainFlowStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwDomainFlowStatistic_Type.__name__ = "Integer32"
_HwDomainFlowStatistic_Object = MibTableColumn
hwDomainFlowStatistic = _HwDomainFlowStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 4, 1, 22),
    _HwDomainFlowStatistic_Type()
)
hwDomainFlowStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainFlowStatistic.setStatus("current")
_HwDomainExtTable_Object = MibTable
hwDomainExtTable = _HwDomainExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hwDomainExtTable.setStatus("current")
_HwDomainExtEntry_Object = MibTableRow
hwDomainExtEntry = _HwDomainExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1)
)
hwDomainExtEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwDomainName"),
)
if mibBuilder.loadTexts:
    hwDomainExtEntry.setStatus("current")


class _HwDomainPPPURL_Type(DisplayString):
    """Custom type hwDomainPPPURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_HwDomainPPPURL_Type.__name__ = "DisplayString"
_HwDomainPPPURL_Object = MibTableColumn
hwDomainPPPURL = _HwDomainPPPURL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 1),
    _HwDomainPPPURL_Type()
)
hwDomainPPPURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainPPPURL.setStatus("current")
_HwIfDomainActive_Type = TruthValue
_HwIfDomainActive_Object = MibTableColumn
hwIfDomainActive = _HwIfDomainActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 2),
    _HwIfDomainActive_Type()
)
hwIfDomainActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfDomainActive.setStatus("current")


class _HwPriority_Type(Integer32):
    """Custom type hwPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPriority_Type.__name__ = "Integer32"
_HwPriority_Object = MibTableColumn
hwPriority = _HwPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 3),
    _HwPriority_Type()
)
hwPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPriority.setStatus("current")


class _HwWebServerURL_Type(DisplayString):
    """Custom type hwWebServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_HwWebServerURL_Type.__name__ = "DisplayString"
_HwWebServerURL_Object = MibTableColumn
hwWebServerURL = _HwWebServerURL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 4),
    _HwWebServerURL_Type()
)
hwWebServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWebServerURL.setStatus("current")


class _HwIPPoolOneName_Type(DisplayString):
    """Custom type hwIPPoolOneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwIPPoolOneName_Type.__name__ = "DisplayString"
_HwIPPoolOneName_Object = MibTableColumn
hwIPPoolOneName = _HwIPPoolOneName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 5),
    _HwIPPoolOneName_Type()
)
hwIPPoolOneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolOneName.setStatus("current")


class _HwIPPoolTwoName_Type(DisplayString):
    """Custom type hwIPPoolTwoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwIPPoolTwoName_Type.__name__ = "DisplayString"
_HwIPPoolTwoName_Object = MibTableColumn
hwIPPoolTwoName = _HwIPPoolTwoName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 6),
    _HwIPPoolTwoName_Type()
)
hwIPPoolTwoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolTwoName.setStatus("current")


class _HwIPPoolThreeName_Type(DisplayString):
    """Custom type hwIPPoolThreeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwIPPoolThreeName_Type.__name__ = "DisplayString"
_HwIPPoolThreeName_Object = MibTableColumn
hwIPPoolThreeName = _HwIPPoolThreeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 7),
    _HwIPPoolThreeName_Type()
)
hwIPPoolThreeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolThreeName.setStatus("current")


class _HwTwoLevelAcctRadiusGroupName_Type(DisplayString):
    """Custom type hwTwoLevelAcctRadiusGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwTwoLevelAcctRadiusGroupName_Type.__name__ = "DisplayString"
_HwTwoLevelAcctRadiusGroupName_Object = MibTableColumn
hwTwoLevelAcctRadiusGroupName = _HwTwoLevelAcctRadiusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 9),
    _HwTwoLevelAcctRadiusGroupName_Type()
)
hwTwoLevelAcctRadiusGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTwoLevelAcctRadiusGroupName.setStatus("current")


class _HwVPDNGroupIndex_Type(Integer32):
    """Custom type hwVPDNGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
        ValueRangeConstraint(65535, 65535),
    )


_HwVPDNGroupIndex_Type.__name__ = "Integer32"
_HwVPDNGroupIndex_Object = MibTableColumn
hwVPDNGroupIndex = _HwVPDNGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 10),
    _HwVPDNGroupIndex_Type()
)
hwVPDNGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVPDNGroupIndex.setStatus("current")


class _HwUclIndex_Type(Integer32):
    """Custom type hwUclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
        ValueRangeConstraint(65535, 65535),
    )


_HwUclIndex_Type.__name__ = "Integer32"
_HwUclIndex_Object = MibTableColumn
hwUclIndex = _HwUclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 11),
    _HwUclIndex_Type()
)
hwUclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUclIndex.setStatus("current")
_HwIfPPPoeURL_Type = TruthValue
_HwIfPPPoeURL_Object = MibTableColumn
hwIfPPPoeURL = _HwIfPPPoeURL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 12),
    _HwIfPPPoeURL_Type()
)
hwIfPPPoeURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfPPPoeURL.setStatus("current")


class _HwUclGroupName_Type(DisplayString):
    """Custom type hwUclGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwUclGroupName_Type.__name__ = "DisplayString"
_HwUclGroupName_Object = MibTableColumn
hwUclGroupName = _HwUclGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 13),
    _HwUclGroupName_Type()
)
hwUclGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUclGroupName.setStatus("current")


class _HwVpdnGroupName_Type(DisplayString):
    """Custom type hwVpdnGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVpdnGroupName_Type.__name__ = "DisplayString"
_HwVpdnGroupName_Object = MibTableColumn
hwVpdnGroupName = _HwVpdnGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 15),
    _HwVpdnGroupName_Type()
)
hwVpdnGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVpdnGroupName.setStatus("current")


class _HwDomainVrf_Type(DisplayString):
    """Custom type hwDomainVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwDomainVrf_Type.__name__ = "DisplayString"
_HwDomainVrf_Object = MibTableColumn
hwDomainVrf = _HwDomainVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 16),
    _HwDomainVrf_Type()
)
hwDomainVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainVrf.setStatus("current")


class _HwDomainGre_Type(DisplayString):
    """Custom type hwDomainGre based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainGre_Type.__name__ = "DisplayString"
_HwDomainGre_Object = MibTableColumn
hwDomainGre = _HwDomainGre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 17),
    _HwDomainGre_Type()
)
hwDomainGre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainGre.setStatus("current")


class _HwDomainRenewIPTag_Type(TruthValue):
    """Custom type hwDomainRenewIPTag based on TruthValue"""


_HwDomainRenewIPTag_Object = MibTableColumn
hwDomainRenewIPTag = _HwDomainRenewIPTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 18),
    _HwDomainRenewIPTag_Type()
)
hwDomainRenewIPTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainRenewIPTag.setStatus("current")


class _HwPortalURL_Type(DisplayString):
    """Custom type hwPortalURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_HwPortalURL_Type.__name__ = "DisplayString"
_HwPortalURL_Object = MibTableColumn
hwPortalURL = _HwPortalURL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 19),
    _HwPortalURL_Type()
)
hwPortalURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalURL.setStatus("current")
_HwPortalServerIP_Type = IpAddress
_HwPortalServerIP_Object = MibTableColumn
hwPortalServerIP = _HwPortalServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 20),
    _HwPortalServerIP_Type()
)
hwPortalServerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalServerIP.setStatus("current")


class _HwRedirectTimesLimit_Type(Integer32):
    """Custom type hwRedirectTimesLimit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwRedirectTimesLimit_Type.__name__ = "Integer32"
_HwRedirectTimesLimit_Object = MibTableColumn
hwRedirectTimesLimit = _HwRedirectTimesLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 21),
    _HwRedirectTimesLimit_Type()
)
hwRedirectTimesLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectTimesLimit.setStatus("current")


class _HwDot1xTemplate_Type(Integer32):
    """Custom type hwDot1xTemplate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwDot1xTemplate_Type.__name__ = "Integer32"
_HwDot1xTemplate_Object = MibTableColumn
hwDot1xTemplate = _HwDot1xTemplate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 22),
    _HwDot1xTemplate_Type()
)
hwDot1xTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xTemplate.setStatus("current")
_HwWebServerIP_Type = IpAddress
_HwWebServerIP_Object = MibTableColumn
hwWebServerIP = _HwWebServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 23),
    _HwWebServerIP_Type()
)
hwWebServerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWebServerIP.setStatus("current")


class _HwWebServerMode_Type(Integer32):
    """Custom type hwWebServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwWebServerMode_Type.__name__ = "Integer32"
_HwWebServerMode_Object = MibTableColumn
hwWebServerMode = _HwWebServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 24),
    _HwWebServerMode_Type()
)
hwWebServerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWebServerMode.setStatus("current")


class _HwPoolWarningThreshold_Type(Integer32):
    """Custom type hwPoolWarningThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(255, 255),
    )


_HwPoolWarningThreshold_Type.__name__ = "Integer32"
_HwPoolWarningThreshold_Object = MibTableColumn
hwPoolWarningThreshold = _HwPoolWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 25),
    _HwPoolWarningThreshold_Type()
)
hwPoolWarningThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPoolWarningThreshold.setStatus("current")


class _HwTacGroupName_Type(DisplayString):
    """Custom type hwTacGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwTacGroupName_Type.__name__ = "DisplayString"
_HwTacGroupName_Object = MibTableColumn
hwTacGroupName = _HwTacGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 26),
    _HwTacGroupName_Type()
)
hwTacGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTacGroupName.setStatus("current")


class _HwServicePolicyName_Type(DisplayString):
    """Custom type hwServicePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwServicePolicyName_Type.__name__ = "DisplayString"
_HwServicePolicyName_Object = MibTableColumn
hwServicePolicyName = _HwServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 27),
    _HwServicePolicyName_Type()
)
hwServicePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServicePolicyName.setStatus("current")


class _HwCopsGroupSSGType_Type(DisplayString):
    """Custom type hwCopsGroupSSGType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwCopsGroupSSGType_Type.__name__ = "DisplayString"
_HwCopsGroupSSGType_Object = MibTableColumn
hwCopsGroupSSGType = _HwCopsGroupSSGType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 28),
    _HwCopsGroupSSGType_Type()
)
hwCopsGroupSSGType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCopsGroupSSGType.setStatus("current")


class _HwDomainAuthorSchemeName_Type(DisplayString):
    """Custom type hwDomainAuthorSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainAuthorSchemeName_Type.__name__ = "DisplayString"
_HwDomainAuthorSchemeName_Object = MibTableColumn
hwDomainAuthorSchemeName = _HwDomainAuthorSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 29),
    _HwDomainAuthorSchemeName_Type()
)
hwDomainAuthorSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainAuthorSchemeName.setStatus("current")


class _HwNtvUserProfileName_Type(DisplayString):
    """Custom type hwNtvUserProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwNtvUserProfileName_Type.__name__ = "DisplayString"
_HwNtvUserProfileName_Object = MibTableColumn
hwNtvUserProfileName = _HwNtvUserProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 30),
    _HwNtvUserProfileName_Type()
)
hwNtvUserProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNtvUserProfileName.setStatus("obsolete")


class _HwDomainQoSProfile_Type(DisplayString):
    """Custom type hwDomainQoSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainQoSProfile_Type.__name__ = "DisplayString"
_HwDomainQoSProfile_Object = MibTableColumn
hwDomainQoSProfile = _HwDomainQoSProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 31),
    _HwDomainQoSProfile_Type()
)
hwDomainQoSProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainQoSProfile.setStatus("current")


class _HwDomainZone_Type(DisplayString):
    """Custom type hwDomainZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainZone_Type.__name__ = "DisplayString"
_HwDomainZone_Object = MibTableColumn
hwDomainZone = _HwDomainZone_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 32),
    _HwDomainZone_Type()
)
hwDomainZone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainZone.setStatus("current")
_HwIfL2tpRadiusForce_Type = TruthValue
_HwIfL2tpRadiusForce_Object = MibTableColumn
hwIfL2tpRadiusForce = _HwIfL2tpRadiusForce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 33),
    _HwIfL2tpRadiusForce_Type()
)
hwIfL2tpRadiusForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIfL2tpRadiusForce.setStatus("current")


class _HwDownPriority_Type(Integer32):
    """Custom type hwDownPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwDownPriority_Type.__name__ = "Integer32"
_HwDownPriority_Object = MibTableColumn
hwDownPriority = _HwDownPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 34),
    _HwDownPriority_Type()
)
hwDownPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDownPriority.setStatus("current")


class _HwPPPForceAuthtype_Type(Integer32):
    """Custom type hwPPPForceAuthtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("mschapv1", 2),
          ("mschapv2", 3),
          ("none", 255),
          ("pap", 0))
    )


_HwPPPForceAuthtype_Type.__name__ = "Integer32"
_HwPPPForceAuthtype_Object = MibTableColumn
hwPPPForceAuthtype = _HwPPPForceAuthtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 35),
    _HwPPPForceAuthtype_Type()
)
hwPPPForceAuthtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPPPForceAuthtype.setStatus("current")
_HwDnsIPAddress_Type = IpAddress
_HwDnsIPAddress_Object = MibTableColumn
hwDnsIPAddress = _HwDnsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 36),
    _HwDnsIPAddress_Type()
)
hwDnsIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDnsIPAddress.setStatus("current")


class _HwAdminUserPriority_Type(Integer32):
    """Custom type hwAdminUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_HwAdminUserPriority_Type.__name__ = "Integer32"
_HwAdminUserPriority_Object = MibTableColumn
hwAdminUserPriority = _HwAdminUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 37),
    _HwAdminUserPriority_Type()
)
hwAdminUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAdminUserPriority.setStatus("current")


class _HwShapingTemplate_Type(DisplayString):
    """Custom type hwShapingTemplate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwShapingTemplate_Type.__name__ = "DisplayString"
_HwShapingTemplate_Object = MibTableColumn
hwShapingTemplate = _HwShapingTemplate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 38),
    _HwShapingTemplate_Type()
)
hwShapingTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwShapingTemplate.setStatus("current")


class _HwDomainDPIPolicyName_Type(DisplayString):
    """Custom type hwDomainDPIPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainDPIPolicyName_Type.__name__ = "DisplayString"
_HwDomainDPIPolicyName_Object = MibTableColumn
hwDomainDPIPolicyName = _HwDomainDPIPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 39),
    _HwDomainDPIPolicyName_Type()
)
hwDomainDPIPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainDPIPolicyName.setStatus("current")


class _HwCopsGroupSIGType_Type(DisplayString):
    """Custom type hwCopsGroupSIGType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwCopsGroupSIGType_Type.__name__ = "DisplayString"
_HwCopsGroupSIGType_Object = MibTableColumn
hwCopsGroupSIGType = _HwCopsGroupSIGType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 40),
    _HwCopsGroupSIGType_Type()
)
hwCopsGroupSIGType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCopsGroupSIGType.setStatus("current")


class _HwCopsGroupCIPNType_Type(DisplayString):
    """Custom type hwCopsGroupCIPNType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwCopsGroupCIPNType_Type.__name__ = "DisplayString"
_HwCopsGroupCIPNType_Object = MibTableColumn
hwCopsGroupCIPNType = _HwCopsGroupCIPNType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 41),
    _HwCopsGroupCIPNType_Type()
)
hwCopsGroupCIPNType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCopsGroupCIPNType.setStatus("current")


class _HwPCReduceCir_Type(Integer32):
    """Custom type hwPCReduceCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwPCReduceCir_Type.__name__ = "Integer32"
_HwPCReduceCir_Object = MibTableColumn
hwPCReduceCir = _HwPCReduceCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 43),
    _HwPCReduceCir_Type()
)
hwPCReduceCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPCReduceCir.setStatus("current")


class _HwValAcctType_Type(Integer32):
    """Custom type hwValAcctType based on Integer32"""
    defaultValue = 1

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
        *(("cops", 3),
          ("default", 1),
          ("none", 0),
          ("radius", 2))
    )


_HwValAcctType_Type.__name__ = "Integer32"
_HwValAcctType_Object = MibTableColumn
hwValAcctType = _HwValAcctType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 44),
    _HwValAcctType_Type()
)
hwValAcctType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwValAcctType.setStatus("current")


class _HwValRadiusServer_Type(DisplayString):
    """Custom type hwValRadiusServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwValRadiusServer_Type.__name__ = "DisplayString"
_HwValRadiusServer_Object = MibTableColumn
hwValRadiusServer = _HwValRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 45),
    _HwValRadiusServer_Type()
)
hwValRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwValRadiusServer.setStatus("current")


class _HwValCopsServer_Type(DisplayString):
    """Custom type hwValCopsServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwValCopsServer_Type.__name__ = "DisplayString"
_HwValCopsServer_Object = MibTableColumn
hwValCopsServer = _HwValCopsServer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 46),
    _HwValCopsServer_Type()
)
hwValCopsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwValCopsServer.setStatus("current")


class _HwPCReducePir_Type(Integer32):
    """Custom type hwPCReducePir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwPCReducePir_Type.__name__ = "Integer32"
_HwPCReducePir_Object = MibTableColumn
hwPCReducePir = _HwPCReducePir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 47),
    _HwPCReducePir_Type()
)
hwPCReducePir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPCReducePir.setStatus("current")


class _HwDomainInboundL2tpQoSProfile_Type(DisplayString):
    """Custom type hwDomainInboundL2tpQoSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwDomainInboundL2tpQoSProfile_Type.__name__ = "DisplayString"
_HwDomainInboundL2tpQoSProfile_Object = MibTableColumn
hwDomainInboundL2tpQoSProfile = _HwDomainInboundL2tpQoSProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 48),
    _HwDomainInboundL2tpQoSProfile_Type()
)
hwDomainInboundL2tpQoSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainInboundL2tpQoSProfile.setStatus("current")


class _HwDomainOutboundL2tpQoSProfile_Type(DisplayString):
    """Custom type hwDomainOutboundL2tpQoSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwDomainOutboundL2tpQoSProfile_Type.__name__ = "DisplayString"
_HwDomainOutboundL2tpQoSProfile_Object = MibTableColumn
hwDomainOutboundL2tpQoSProfile = _HwDomainOutboundL2tpQoSProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 49),
    _HwDomainOutboundL2tpQoSProfile_Type()
)
hwDomainOutboundL2tpQoSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainOutboundL2tpQoSProfile.setStatus("current")


class _HwIfMulticastForward_Type(TruthValue):
    """Custom type hwIfMulticastForward based on TruthValue"""
    defaultValue = 1


_HwIfMulticastForward_Object = MibTableColumn
hwIfMulticastForward = _HwIfMulticastForward_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 50),
    _HwIfMulticastForward_Type()
)
hwIfMulticastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfMulticastForward.setStatus("current")


class _HwMulticastVirtualSchedulRezCir_Type(Integer32):
    """Custom type hwMulticastVirtualSchedulRezCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 1000000),
    )


_HwMulticastVirtualSchedulRezCir_Type.__name__ = "Integer32"
_HwMulticastVirtualSchedulRezCir_Object = MibTableColumn
hwMulticastVirtualSchedulRezCir = _HwMulticastVirtualSchedulRezCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 51),
    _HwMulticastVirtualSchedulRezCir_Type()
)
hwMulticastVirtualSchedulRezCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMulticastVirtualSchedulRezCir.setStatus("current")


class _HwMulticastVirtualSchedulRezPir_Type(Integer32):
    """Custom type hwMulticastVirtualSchedulRezPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 1000000),
    )


_HwMulticastVirtualSchedulRezPir_Type.__name__ = "Integer32"
_HwMulticastVirtualSchedulRezPir_Object = MibTableColumn
hwMulticastVirtualSchedulRezPir = _HwMulticastVirtualSchedulRezPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 52),
    _HwMulticastVirtualSchedulRezPir_Type()
)
hwMulticastVirtualSchedulRezPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMulticastVirtualSchedulRezPir.setStatus("current")


class _HwMaxMulticastListNum_Type(Integer32):
    """Custom type hwMaxMulticastListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwMaxMulticastListNum_Type.__name__ = "Integer32"
_HwMaxMulticastListNum_Object = MibTableColumn
hwMaxMulticastListNum = _HwMaxMulticastListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 53),
    _HwMaxMulticastListNum_Type()
)
hwMaxMulticastListNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMaxMulticastListNum.setStatus("current")


class _HwMultiProfile_Type(DisplayString):
    """Custom type hwMultiProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMultiProfile_Type.__name__ = "DisplayString"
_HwMultiProfile_Object = MibTableColumn
hwMultiProfile = _HwMultiProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 54),
    _HwMultiProfile_Type()
)
hwMultiProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMultiProfile.setStatus("current")


class _HwDomainServiceType_Type(Integer32):
    """Custom type hwDomainServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hsi", 1),
          ("stb", 0))
    )


_HwDomainServiceType_Type.__name__ = "Integer32"
_HwDomainServiceType_Object = MibTableColumn
hwDomainServiceType = _HwDomainServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 55),
    _HwDomainServiceType_Type()
)
hwDomainServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainServiceType.setStatus("current")


class _HwWebServerUrlParameter_Type(TruthValue):
    """Custom type hwWebServerUrlParameter based on TruthValue"""
    defaultValue = 1


_HwWebServerUrlParameter_Object = MibTableColumn
hwWebServerUrlParameter = _HwWebServerUrlParameter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 56),
    _HwWebServerUrlParameter_Type()
)
hwWebServerUrlParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWebServerUrlParameter.setStatus("current")


class _HwWebServerRedirectKeyMscgName_Type(DisplayString):
    """Custom type hwWebServerRedirectKeyMscgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwWebServerRedirectKeyMscgName_Type.__name__ = "DisplayString"
_HwWebServerRedirectKeyMscgName_Object = MibTableColumn
hwWebServerRedirectKeyMscgName = _HwWebServerRedirectKeyMscgName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 57),
    _HwWebServerRedirectKeyMscgName_Type()
)
hwWebServerRedirectKeyMscgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWebServerRedirectKeyMscgName.setStatus("current")


class _HwPoratalServerUrlParameter_Type(TruthValue):
    """Custom type hwPoratalServerUrlParameter based on TruthValue"""
    defaultValue = 1


_HwPoratalServerUrlParameter_Object = MibTableColumn
hwPoratalServerUrlParameter = _HwPoratalServerUrlParameter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 58),
    _HwPoratalServerUrlParameter_Type()
)
hwPoratalServerUrlParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoratalServerUrlParameter.setStatus("current")


class _HwPoratalServerFirstUrlKeyName_Type(DisplayString):
    """Custom type hwPoratalServerFirstUrlKeyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwPoratalServerFirstUrlKeyName_Type.__name__ = "DisplayString"
_HwPoratalServerFirstUrlKeyName_Object = MibTableColumn
hwPoratalServerFirstUrlKeyName = _HwPoratalServerFirstUrlKeyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 59),
    _HwPoratalServerFirstUrlKeyName_Type()
)
hwPoratalServerFirstUrlKeyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoratalServerFirstUrlKeyName.setStatus("current")


class _HwPoratalServerFirstUrlKeyDefaultName_Type(TruthValue):
    """Custom type hwPoratalServerFirstUrlKeyDefaultName based on TruthValue"""
    defaultValue = 1


_HwPoratalServerFirstUrlKeyDefaultName_Object = MibTableColumn
hwPoratalServerFirstUrlKeyDefaultName = _HwPoratalServerFirstUrlKeyDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 60),
    _HwPoratalServerFirstUrlKeyDefaultName_Type()
)
hwPoratalServerFirstUrlKeyDefaultName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoratalServerFirstUrlKeyDefaultName.setStatus("current")
_HwDnsSecondIPAddress_Type = IpAddress
_HwDnsSecondIPAddress_Object = MibTableColumn
hwDnsSecondIPAddress = _HwDnsSecondIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 61),
    _HwDnsSecondIPAddress_Type()
)
hwDnsSecondIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDnsSecondIPAddress.setStatus("current")
_HwDomainIgmpEnable_Type = Integer32
_HwDomainIgmpEnable_Object = MibTableColumn
hwDomainIgmpEnable = _HwDomainIgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 62),
    _HwDomainIgmpEnable_Type()
)
hwDomainIgmpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainIgmpEnable.setStatus("current")


class _HwIPv6PoolName_Type(DisplayString):
    """Custom type hwIPv6PoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_HwIPv6PoolName_Type.__name__ = "DisplayString"
_HwIPv6PoolName_Object = MibTableColumn
hwIPv6PoolName = _HwIPv6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 63),
    _HwIPv6PoolName_Type()
)
hwIPv6PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolName.setStatus("current")


class _HwIPv6PrefixshareFlag_Type(Integer32):
    """Custom type hwIPv6PrefixshareFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shared", 1),
          ("unshared", 2))
    )


_HwIPv6PrefixshareFlag_Type.__name__ = "Integer32"
_HwIPv6PrefixshareFlag_Object = MibTableColumn
hwIPv6PrefixshareFlag = _HwIPv6PrefixshareFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 64),
    _HwIPv6PrefixshareFlag_Type()
)
hwIPv6PrefixshareFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixshareFlag.setStatus("current")


class _HwUserBasicServiceIPType_Type(DisplayString):
    """Custom type hwUserBasicServiceIPType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HwUserBasicServiceIPType_Type.__name__ = "DisplayString"
_HwUserBasicServiceIPType_Object = MibTableColumn
hwUserBasicServiceIPType = _HwUserBasicServiceIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 65),
    _HwUserBasicServiceIPType_Type()
)
hwUserBasicServiceIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUserBasicServiceIPType.setStatus("current")
_HwPriDnsIPv6Address_Type = Ipv6Address
_HwPriDnsIPv6Address_Object = MibTableColumn
hwPriDnsIPv6Address = _HwPriDnsIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 66),
    _HwPriDnsIPv6Address_Type()
)
hwPriDnsIPv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriDnsIPv6Address.setStatus("current")
_HwSecDnsIPv6Address_Type = Ipv6Address
_HwSecDnsIPv6Address_Object = MibTableColumn
hwSecDnsIPv6Address = _HwSecDnsIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 67),
    _HwSecDnsIPv6Address_Type()
)
hwSecDnsIPv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSecDnsIPv6Address.setStatus("current")


class _HwDualStackAccountingType_Type(Integer32):
    """Custom type hwDualStackAccountingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("identical", 2),
          ("seperate", 1))
    )


_HwDualStackAccountingType_Type.__name__ = "Integer32"
_HwDualStackAccountingType_Object = MibTableColumn
hwDualStackAccountingType = _HwDualStackAccountingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 68),
    _HwDualStackAccountingType_Type()
)
hwDualStackAccountingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDualStackAccountingType.setStatus("current")


class _HwIPv6PoolWarningThreshold_Type(Integer32):
    """Custom type hwIPv6PoolWarningThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwIPv6PoolWarningThreshold_Type.__name__ = "Integer32"
_HwIPv6PoolWarningThreshold_Object = MibTableColumn
hwIPv6PoolWarningThreshold = _HwIPv6PoolWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 69),
    _HwIPv6PoolWarningThreshold_Type()
)
hwIPv6PoolWarningThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolWarningThreshold.setStatus("current")


class _HwIPv6CPWaitDHCPv6Delay_Type(Integer32):
    """Custom type hwIPv6CPWaitDHCPv6Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_HwIPv6CPWaitDHCPv6Delay_Type.__name__ = "Integer32"
_HwIPv6CPWaitDHCPv6Delay_Object = MibTableColumn
hwIPv6CPWaitDHCPv6Delay = _HwIPv6CPWaitDHCPv6Delay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 70),
    _HwIPv6CPWaitDHCPv6Delay_Type()
)
hwIPv6CPWaitDHCPv6Delay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6CPWaitDHCPv6Delay.setStatus("current")


class _HwIPv6ManagedAddressFlag_Type(Integer32):
    """Custom type hwIPv6ManagedAddressFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv6", 2),
          ("ndra", 1))
    )


_HwIPv6ManagedAddressFlag_Type.__name__ = "Integer32"
_HwIPv6ManagedAddressFlag_Object = MibTableColumn
hwIPv6ManagedAddressFlag = _HwIPv6ManagedAddressFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 71),
    _HwIPv6ManagedAddressFlag_Type()
)
hwIPv6ManagedAddressFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6ManagedAddressFlag.setStatus("current")
_HwIPv6CPIFIDAvailable_Type = TruthValue
_HwIPv6CPIFIDAvailable_Object = MibTableColumn
hwIPv6CPIFIDAvailable = _HwIPv6CPIFIDAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 72),
    _HwIPv6CPIFIDAvailable_Type()
)
hwIPv6CPIFIDAvailable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6CPIFIDAvailable.setStatus("current")


class _HwIPv6OtherFlag_Type(Integer32):
    """Custom type hwIPv6OtherFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv6", 2),
          ("ndra", 1))
    )


_HwIPv6OtherFlag_Type.__name__ = "Integer32"
_HwIPv6OtherFlag_Object = MibTableColumn
hwIPv6OtherFlag = _HwIPv6OtherFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 73),
    _HwIPv6OtherFlag_Type()
)
hwIPv6OtherFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6OtherFlag.setStatus("current")
_HwIPv6CPAssignIFID_Type = TruthValue
_HwIPv6CPAssignIFID_Object = MibTableColumn
hwIPv6CPAssignIFID = _HwIPv6CPAssignIFID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 74),
    _HwIPv6CPAssignIFID_Type()
)
hwIPv6CPAssignIFID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6CPAssignIFID.setStatus("current")


class _HwMultiIPv6ProfileName_Type(DisplayString):
    """Custom type hwMultiIPv6ProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMultiIPv6ProfileName_Type.__name__ = "DisplayString"
_HwMultiIPv6ProfileName_Object = MibTableColumn
hwMultiIPv6ProfileName = _HwMultiIPv6ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 75),
    _HwMultiIPv6ProfileName_Type()
)
hwMultiIPv6ProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMultiIPv6ProfileName.setStatus("current")


class _HwWebServerURLSlave_Type(DisplayString):
    """Custom type hwWebServerURLSlave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_HwWebServerURLSlave_Type.__name__ = "DisplayString"
_HwWebServerURLSlave_Object = MibTableColumn
hwWebServerURLSlave = _HwWebServerURLSlave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 76),
    _HwWebServerURLSlave_Type()
)
hwWebServerURLSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWebServerURLSlave.setStatus("current")
_HwWebServerIPSlave_Type = IpAddress
_HwWebServerIPSlave_Object = MibTableColumn
hwWebServerIPSlave = _HwWebServerIPSlave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 77),
    _HwWebServerIPSlave_Type()
)
hwWebServerIPSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWebServerIPSlave.setStatus("current")
_HwBindAuthWebIP_Type = IpAddress
_HwBindAuthWebIP_Object = MibTableColumn
hwBindAuthWebIP = _HwBindAuthWebIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 78),
    _HwBindAuthWebIP_Type()
)
hwBindAuthWebIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBindAuthWebIP.setStatus("current")


class _HwBindAuthWebVrf_Type(DisplayString):
    """Custom type hwBindAuthWebVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBindAuthWebVrf_Type.__name__ = "DisplayString"
_HwBindAuthWebVrf_Object = MibTableColumn
hwBindAuthWebVrf = _HwBindAuthWebVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 79),
    _HwBindAuthWebVrf_Type()
)
hwBindAuthWebVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBindAuthWebVrf.setStatus("current")
_HwBindAuthWebIPSlave_Type = IpAddress
_HwBindAuthWebIPSlave_Object = MibTableColumn
hwBindAuthWebIPSlave = _HwBindAuthWebIPSlave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 80),
    _HwBindAuthWebIPSlave_Type()
)
hwBindAuthWebIPSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBindAuthWebIPSlave.setStatus("current")


class _HwBindAuthWebVrfSlave_Type(DisplayString):
    """Custom type hwBindAuthWebVrfSlave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBindAuthWebVrfSlave_Type.__name__ = "DisplayString"
_HwBindAuthWebVrfSlave_Object = MibTableColumn
hwBindAuthWebVrfSlave = _HwBindAuthWebVrfSlave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 81),
    _HwBindAuthWebVrfSlave_Type()
)
hwBindAuthWebVrfSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBindAuthWebVrfSlave.setStatus("current")


class _HwExtVpdnGroupName_Type(DisplayString):
    """Custom type hwExtVpdnGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwExtVpdnGroupName_Type.__name__ = "DisplayString"
_HwExtVpdnGroupName_Object = MibTableColumn
hwExtVpdnGroupName = _HwExtVpdnGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 82),
    _HwExtVpdnGroupName_Type()
)
hwExtVpdnGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwExtVpdnGroupName.setStatus("current")


class _HwDomainUserGroupName_Type(DisplayString):
    """Custom type hwDomainUserGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwDomainUserGroupName_Type.__name__ = "DisplayString"
_HwDomainUserGroupName_Object = MibTableColumn
hwDomainUserGroupName = _HwDomainUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 83),
    _HwDomainUserGroupName_Type()
)
hwDomainUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainUserGroupName.setStatus("current")


class _HwAFTRName_Type(DisplayString):
    """Custom type hwAFTRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwAFTRName_Type.__name__ = "DisplayString"
_HwAFTRName_Object = MibTableColumn
hwAFTRName = _HwAFTRName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 84),
    _HwAFTRName_Type()
)
hwAFTRName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAFTRName.setStatus("current")


class _HwDomainDhcpOpt64SepAndSeg_Type(DisplayString):
    """Custom type hwDomainDhcpOpt64SepAndSeg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_HwDomainDhcpOpt64SepAndSeg_Type.__name__ = "DisplayString"
_HwDomainDhcpOpt64SepAndSeg_Object = MibTableColumn
hwDomainDhcpOpt64SepAndSeg = _HwDomainDhcpOpt64SepAndSeg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 85),
    _HwDomainDhcpOpt64SepAndSeg_Type()
)
hwDomainDhcpOpt64SepAndSeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainDhcpOpt64SepAndSeg.setStatus("current")
_HwDomainDhcpServerAck_Type = TruthValue
_HwDomainDhcpServerAck_Object = MibTableColumn
hwDomainDhcpServerAck = _HwDomainDhcpServerAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 5, 1, 86),
    _HwDomainDhcpServerAck_Type()
)
hwDomainDhcpServerAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainDhcpServerAck.setStatus("current")
_HwDomainStatTable_Object = MibTable
hwDomainStatTable = _HwDomainStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hwDomainStatTable.setStatus("current")
_HwDomainStatEntry_Object = MibTableRow
hwDomainStatEntry = _HwDomainStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1)
)
hwDomainStatEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwDomainName"),
)
if mibBuilder.loadTexts:
    hwDomainStatEntry.setStatus("current")
_HwDomainAccessedNum_Type = Integer32
_HwDomainAccessedNum_Object = MibTableColumn
hwDomainAccessedNum = _HwDomainAccessedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 1),
    _HwDomainAccessedNum_Type()
)
hwDomainAccessedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainAccessedNum.setStatus("current")
_HwDomainOnlineNum_Type = Integer32
_HwDomainOnlineNum_Object = MibTableColumn
hwDomainOnlineNum = _HwDomainOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 2),
    _HwDomainOnlineNum_Type()
)
hwDomainOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainOnlineNum.setStatus("current")
_HwDomainOnlinePPPUser_Type = Integer32
_HwDomainOnlinePPPUser_Object = MibTableColumn
hwDomainOnlinePPPUser = _HwDomainOnlinePPPUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 3),
    _HwDomainOnlinePPPUser_Type()
)
hwDomainOnlinePPPUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainOnlinePPPUser.setStatus("current")
_HwDomainFlowDnByte_Type = Counter64
_HwDomainFlowDnByte_Object = MibTableColumn
hwDomainFlowDnByte = _HwDomainFlowDnByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 4),
    _HwDomainFlowDnByte_Type()
)
hwDomainFlowDnByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainFlowDnByte.setStatus("current")
_HwDomainFlowDnPkt_Type = Counter64
_HwDomainFlowDnPkt_Object = MibTableColumn
hwDomainFlowDnPkt = _HwDomainFlowDnPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 5),
    _HwDomainFlowDnPkt_Type()
)
hwDomainFlowDnPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainFlowDnPkt.setStatus("current")
_HwDomainFlowUpByte_Type = Counter64
_HwDomainFlowUpByte_Object = MibTableColumn
hwDomainFlowUpByte = _HwDomainFlowUpByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 6),
    _HwDomainFlowUpByte_Type()
)
hwDomainFlowUpByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainFlowUpByte.setStatus("current")
_HwDomainFlowUpPkt_Type = Counter64
_HwDomainFlowUpPkt_Object = MibTableColumn
hwDomainFlowUpPkt = _HwDomainFlowUpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 7),
    _HwDomainFlowUpPkt_Type()
)
hwDomainFlowUpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainFlowUpPkt.setStatus("current")
_HwDomainIPTotalNum_Type = Integer32
_HwDomainIPTotalNum_Object = MibTableColumn
hwDomainIPTotalNum = _HwDomainIPTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 8),
    _HwDomainIPTotalNum_Type()
)
hwDomainIPTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPTotalNum.setStatus("current")
_HwDomainIPUsedNum_Type = Integer32
_HwDomainIPUsedNum_Object = MibTableColumn
hwDomainIPUsedNum = _HwDomainIPUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 9),
    _HwDomainIPUsedNum_Type()
)
hwDomainIPUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPUsedNum.setStatus("current")
_HwDomainIPConflictNum_Type = Integer32
_HwDomainIPConflictNum_Object = MibTableColumn
hwDomainIPConflictNum = _HwDomainIPConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 10),
    _HwDomainIPConflictNum_Type()
)
hwDomainIPConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPConflictNum.setStatus("current")
_HwDomainIPExcludeNum_Type = Integer32
_HwDomainIPExcludeNum_Object = MibTableColumn
hwDomainIPExcludeNum = _HwDomainIPExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 11),
    _HwDomainIPExcludeNum_Type()
)
hwDomainIPExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPExcludeNum.setStatus("current")
_HwDomainIPIdleNum_Type = Integer32
_HwDomainIPIdleNum_Object = MibTableColumn
hwDomainIPIdleNum = _HwDomainIPIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 12),
    _HwDomainIPIdleNum_Type()
)
hwDomainIPIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPIdleNum.setStatus("current")


class _HwDomainIPUsedPercent_Type(DisplayString):
    """Custom type hwDomainIPUsedPercent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwDomainIPUsedPercent_Type.__name__ = "DisplayString"
_HwDomainIPUsedPercent_Object = MibTableColumn
hwDomainIPUsedPercent = _HwDomainIPUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 13),
    _HwDomainIPUsedPercent_Type()
)
hwDomainIPUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPUsedPercent.setStatus("current")
_HwDomainPPPoENum_Type = Integer32
_HwDomainPPPoENum_Object = MibTableColumn
hwDomainPPPoENum = _HwDomainPPPoENum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 14),
    _HwDomainPPPoENum_Type()
)
hwDomainPPPoENum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainPPPoENum.setStatus("current")
_HwDomainAuthenRequestsRcvNum_Type = Integer32
_HwDomainAuthenRequestsRcvNum_Object = MibTableColumn
hwDomainAuthenRequestsRcvNum = _HwDomainAuthenRequestsRcvNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 15),
    _HwDomainAuthenRequestsRcvNum_Type()
)
hwDomainAuthenRequestsRcvNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainAuthenRequestsRcvNum.setStatus("current")
_HwDomainAuthenAcceptsNum_Type = Integer32
_HwDomainAuthenAcceptsNum_Object = MibTableColumn
hwDomainAuthenAcceptsNum = _HwDomainAuthenAcceptsNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 16),
    _HwDomainAuthenAcceptsNum_Type()
)
hwDomainAuthenAcceptsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainAuthenAcceptsNum.setStatus("current")
_HwDomainAuthenRejectsNum_Type = Integer32
_HwDomainAuthenRejectsNum_Object = MibTableColumn
hwDomainAuthenRejectsNum = _HwDomainAuthenRejectsNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 17),
    _HwDomainAuthenRejectsNum_Type()
)
hwDomainAuthenRejectsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainAuthenRejectsNum.setStatus("current")
_HwDomainAcctRequestsRcvNum_Type = Integer32
_HwDomainAcctRequestsRcvNum_Object = MibTableColumn
hwDomainAcctRequestsRcvNum = _HwDomainAcctRequestsRcvNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 18),
    _HwDomainAcctRequestsRcvNum_Type()
)
hwDomainAcctRequestsRcvNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainAcctRequestsRcvNum.setStatus("current")
_HwDomainAcctRspSuccessNum_Type = Integer32
_HwDomainAcctRspSuccessNum_Object = MibTableColumn
hwDomainAcctRspSuccessNum = _HwDomainAcctRspSuccessNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 19),
    _HwDomainAcctRspSuccessNum_Type()
)
hwDomainAcctRspSuccessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainAcctRspSuccessNum.setStatus("current")
_HwDomainAcctRspFailuresNum_Type = Integer32
_HwDomainAcctRspFailuresNum_Object = MibTableColumn
hwDomainAcctRspFailuresNum = _HwDomainAcctRspFailuresNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 20),
    _HwDomainAcctRspFailuresNum_Type()
)
hwDomainAcctRspFailuresNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainAcctRspFailuresNum.setStatus("current")
_HwDomainIPv6AddressTotalNum_Type = Integer32
_HwDomainIPv6AddressTotalNum_Object = MibTableColumn
hwDomainIPv6AddressTotalNum = _HwDomainIPv6AddressTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 21),
    _HwDomainIPv6AddressTotalNum_Type()
)
hwDomainIPv6AddressTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6AddressTotalNum.setStatus("current")
_HwDomainIPv6AddressUsedNum_Type = Integer32
_HwDomainIPv6AddressUsedNum_Object = MibTableColumn
hwDomainIPv6AddressUsedNum = _HwDomainIPv6AddressUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 22),
    _HwDomainIPv6AddressUsedNum_Type()
)
hwDomainIPv6AddressUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6AddressUsedNum.setStatus("current")
_HwDomainIPv6AddressFreeNum_Type = Integer32
_HwDomainIPv6AddressFreeNum_Object = MibTableColumn
hwDomainIPv6AddressFreeNum = _HwDomainIPv6AddressFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 23),
    _HwDomainIPv6AddressFreeNum_Type()
)
hwDomainIPv6AddressFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6AddressFreeNum.setStatus("current")
_HwDomainIPv6AddressConflictNum_Type = Integer32
_HwDomainIPv6AddressConflictNum_Object = MibTableColumn
hwDomainIPv6AddressConflictNum = _HwDomainIPv6AddressConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 24),
    _HwDomainIPv6AddressConflictNum_Type()
)
hwDomainIPv6AddressConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6AddressConflictNum.setStatus("current")
_HwDomainIPv6AddressExcludeNum_Type = Integer32
_HwDomainIPv6AddressExcludeNum_Object = MibTableColumn
hwDomainIPv6AddressExcludeNum = _HwDomainIPv6AddressExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 25),
    _HwDomainIPv6AddressExcludeNum_Type()
)
hwDomainIPv6AddressExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6AddressExcludeNum.setStatus("current")


class _HwDomainIPv6AddressUsedPercent_Type(DisplayString):
    """Custom type hwDomainIPv6AddressUsedPercent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwDomainIPv6AddressUsedPercent_Type.__name__ = "DisplayString"
_HwDomainIPv6AddressUsedPercent_Object = MibTableColumn
hwDomainIPv6AddressUsedPercent = _HwDomainIPv6AddressUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 26),
    _HwDomainIPv6AddressUsedPercent_Type()
)
hwDomainIPv6AddressUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6AddressUsedPercent.setStatus("current")
_HwDomainNDRAPrefixTotalNum_Type = Integer32
_HwDomainNDRAPrefixTotalNum_Object = MibTableColumn
hwDomainNDRAPrefixTotalNum = _HwDomainNDRAPrefixTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 27),
    _HwDomainNDRAPrefixTotalNum_Type()
)
hwDomainNDRAPrefixTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainNDRAPrefixTotalNum.setStatus("current")
_HwDomainNDRAPrefixUsedNum_Type = Integer32
_HwDomainNDRAPrefixUsedNum_Object = MibTableColumn
hwDomainNDRAPrefixUsedNum = _HwDomainNDRAPrefixUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 28),
    _HwDomainNDRAPrefixUsedNum_Type()
)
hwDomainNDRAPrefixUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainNDRAPrefixUsedNum.setStatus("current")
_HwDomainNDRAPrefixFreeNum_Type = Integer32
_HwDomainNDRAPrefixFreeNum_Object = MibTableColumn
hwDomainNDRAPrefixFreeNum = _HwDomainNDRAPrefixFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 29),
    _HwDomainNDRAPrefixFreeNum_Type()
)
hwDomainNDRAPrefixFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainNDRAPrefixFreeNum.setStatus("current")
_HwDomainNDRAPrefixConflictNum_Type = Integer32
_HwDomainNDRAPrefixConflictNum_Object = MibTableColumn
hwDomainNDRAPrefixConflictNum = _HwDomainNDRAPrefixConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 30),
    _HwDomainNDRAPrefixConflictNum_Type()
)
hwDomainNDRAPrefixConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainNDRAPrefixConflictNum.setStatus("current")
_HwDomainNDRAPrefixExcludeNum_Type = Integer32
_HwDomainNDRAPrefixExcludeNum_Object = MibTableColumn
hwDomainNDRAPrefixExcludeNum = _HwDomainNDRAPrefixExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 31),
    _HwDomainNDRAPrefixExcludeNum_Type()
)
hwDomainNDRAPrefixExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainNDRAPrefixExcludeNum.setStatus("current")


class _HwDomainNDRAPrefixUsedPercent_Type(DisplayString):
    """Custom type hwDomainNDRAPrefixUsedPercent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwDomainNDRAPrefixUsedPercent_Type.__name__ = "DisplayString"
_HwDomainNDRAPrefixUsedPercent_Object = MibTableColumn
hwDomainNDRAPrefixUsedPercent = _HwDomainNDRAPrefixUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 32),
    _HwDomainNDRAPrefixUsedPercent_Type()
)
hwDomainNDRAPrefixUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainNDRAPrefixUsedPercent.setStatus("current")
_HwDomainPDPrefixTotalNum_Type = Integer32
_HwDomainPDPrefixTotalNum_Object = MibTableColumn
hwDomainPDPrefixTotalNum = _HwDomainPDPrefixTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 33),
    _HwDomainPDPrefixTotalNum_Type()
)
hwDomainPDPrefixTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainPDPrefixTotalNum.setStatus("current")
_HwDomainPDPrefixUsedNum_Type = Integer32
_HwDomainPDPrefixUsedNum_Object = MibTableColumn
hwDomainPDPrefixUsedNum = _HwDomainPDPrefixUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 34),
    _HwDomainPDPrefixUsedNum_Type()
)
hwDomainPDPrefixUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainPDPrefixUsedNum.setStatus("current")
_HwDomainPDPrefixFreeNum_Type = Integer32
_HwDomainPDPrefixFreeNum_Object = MibTableColumn
hwDomainPDPrefixFreeNum = _HwDomainPDPrefixFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 35),
    _HwDomainPDPrefixFreeNum_Type()
)
hwDomainPDPrefixFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainPDPrefixFreeNum.setStatus("current")
_HwDomainPDPrefixConflictNum_Type = Integer32
_HwDomainPDPrefixConflictNum_Object = MibTableColumn
hwDomainPDPrefixConflictNum = _HwDomainPDPrefixConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 36),
    _HwDomainPDPrefixConflictNum_Type()
)
hwDomainPDPrefixConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainPDPrefixConflictNum.setStatus("current")
_HwDomainPDPrefixExcludeNum_Type = Integer32
_HwDomainPDPrefixExcludeNum_Object = MibTableColumn
hwDomainPDPrefixExcludeNum = _HwDomainPDPrefixExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 37),
    _HwDomainPDPrefixExcludeNum_Type()
)
hwDomainPDPrefixExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainPDPrefixExcludeNum.setStatus("current")


class _HwDomainPDPrefixUsedPercent_Type(DisplayString):
    """Custom type hwDomainPDPrefixUsedPercent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwDomainPDPrefixUsedPercent_Type.__name__ = "DisplayString"
_HwDomainPDPrefixUsedPercent_Object = MibTableColumn
hwDomainPDPrefixUsedPercent = _HwDomainPDPrefixUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 38),
    _HwDomainPDPrefixUsedPercent_Type()
)
hwDomainPDPrefixUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainPDPrefixUsedPercent.setStatus("current")
_HwDomainIPv6FlowDnByte_Type = Counter64
_HwDomainIPv6FlowDnByte_Object = MibTableColumn
hwDomainIPv6FlowDnByte = _HwDomainIPv6FlowDnByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 39),
    _HwDomainIPv6FlowDnByte_Type()
)
hwDomainIPv6FlowDnByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6FlowDnByte.setStatus("current")
_HwDomainIPv6FlowDnPkt_Type = Counter64
_HwDomainIPv6FlowDnPkt_Object = MibTableColumn
hwDomainIPv6FlowDnPkt = _HwDomainIPv6FlowDnPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 40),
    _HwDomainIPv6FlowDnPkt_Type()
)
hwDomainIPv6FlowDnPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6FlowDnPkt.setStatus("current")
_HwDomainIPv6FlowUpByte_Type = Counter64
_HwDomainIPv6FlowUpByte_Object = MibTableColumn
hwDomainIPv6FlowUpByte = _HwDomainIPv6FlowUpByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 41),
    _HwDomainIPv6FlowUpByte_Type()
)
hwDomainIPv6FlowUpByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6FlowUpByte.setStatus("current")
_HwDomainIPv6FlowUpPkt_Type = Counter64
_HwDomainIPv6FlowUpPkt_Object = MibTableColumn
hwDomainIPv6FlowUpPkt = _HwDomainIPv6FlowUpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 6, 1, 42),
    _HwDomainIPv6FlowUpPkt_Type()
)
hwDomainIPv6FlowUpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIPv6FlowUpPkt.setStatus("current")
_HwAuthorSchemeTable_Object = MibTable
hwAuthorSchemeTable = _HwAuthorSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hwAuthorSchemeTable.setStatus("current")
_HwAuthorSchemeEntry_Object = MibTableRow
hwAuthorSchemeEntry = _HwAuthorSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 8, 1)
)
hwAuthorSchemeEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAuthorSchemeName"),
)
if mibBuilder.loadTexts:
    hwAuthorSchemeEntry.setStatus("current")


class _HwAuthorSchemeName_Type(DisplayString):
    """Custom type hwAuthorSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwAuthorSchemeName_Type.__name__ = "DisplayString"
_HwAuthorSchemeName_Object = MibTableColumn
hwAuthorSchemeName = _HwAuthorSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 8, 1, 1),
    _HwAuthorSchemeName_Type()
)
hwAuthorSchemeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthorSchemeName.setStatus("current")


class _HwAuthorMethod_Type(Integer32):
    """Custom type hwAuthorMethod based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("hwtacacs", 3),
          ("hwtacacsifauthenticated", 7),
          ("hwtacacsifauthenticatedlocal", 23),
          ("hwtacacsifauthenticatedlocalnone", 29),
          ("hwtacacsifauthenticatednone", 17),
          ("hwtacacslocal", 6),
          ("hwtacacslocalnone", 16),
          ("hwtacacsnone", 5),
          ("hwtacaslocalifauthenticated", 22),
          ("hwtacaslocalifauthenticatednone", 28),
          ("ifauthenticated", 4),
          ("ifauthenticatedhwtacacs", 13),
          ("ifauthenticatedhwtacacslocal", 25),
          ("ifauthenticatedhwtacacslocalnone", 31),
          ("ifauthenticatedhwtacacsnone", 19),
          ("ifauthenticatedlocal", 12),
          ("ifauthenticatedlocalhwtacacs", 24),
          ("ifauthenticatedlocalhwtacacsnone", 30),
          ("ifauthenticatedlocalnone", 18),
          ("ifauthenticatednone", 11),
          ("local", 2),
          ("localhwtacacs", 9),
          ("localhwtacacsifauthenticated", 20),
          ("localhwtacacsifauthenticatednone", 26),
          ("localhwtacacsnone", 14),
          ("localifauthenticated", 10),
          ("localifauthenticatedhwtacacs", 21),
          ("localifauthenticatedhwtacacsnone", 27),
          ("localifauthenticatednone", 15),
          ("localnone", 8),
          ("none", 1))
    )


_HwAuthorMethod_Type.__name__ = "Integer32"
_HwAuthorMethod_Object = MibTableColumn
hwAuthorMethod = _HwAuthorMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 8, 1, 2),
    _HwAuthorMethod_Type()
)
hwAuthorMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAuthorMethod.setStatus("current")
_HwAuthorRowStatus_Type = RowStatus
_HwAuthorRowStatus_Object = MibTableColumn
hwAuthorRowStatus = _HwAuthorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 8, 1, 3),
    _HwAuthorRowStatus_Type()
)
hwAuthorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAuthorRowStatus.setStatus("current")
_HwLocalUserTable_Object = MibTable
hwLocalUserTable = _HwLocalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hwLocalUserTable.setStatus("current")
_HwLocalUserEntry_Object = MibTableRow
hwLocalUserEntry = _HwLocalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1)
)
hwLocalUserEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwLocalUserName"),
)
if mibBuilder.loadTexts:
    hwLocalUserEntry.setStatus("current")


class _HwLocalUserName_Type(DisplayString):
    """Custom type hwLocalUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_HwLocalUserName_Type.__name__ = "DisplayString"
_HwLocalUserName_Object = MibTableColumn
hwLocalUserName = _HwLocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 1),
    _HwLocalUserName_Type()
)
hwLocalUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUserName.setStatus("current")


class _HwLocalUserPassword_Type(DisplayString):
    """Custom type hwLocalUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwLocalUserPassword_Type.__name__ = "DisplayString"
_HwLocalUserPassword_Object = MibTableColumn
hwLocalUserPassword = _HwLocalUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 2),
    _HwLocalUserPassword_Type()
)
hwLocalUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalUserPassword.setStatus("current")


class _HwLocalUserAccessType_Type(Unsigned32):
    """Custom type hwLocalUserAccessType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwLocalUserAccessType_Type.__name__ = "Unsigned32"
_HwLocalUserAccessType_Object = MibTableColumn
hwLocalUserAccessType = _HwLocalUserAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 3),
    _HwLocalUserAccessType_Type()
)
hwLocalUserAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalUserAccessType.setStatus("current")


class _HwLocalUserPriority_Type(Integer32):
    """Custom type hwLocalUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwLocalUserPriority_Type.__name__ = "Integer32"
_HwLocalUserPriority_Object = MibTableColumn
hwLocalUserPriority = _HwLocalUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 4),
    _HwLocalUserPriority_Type()
)
hwLocalUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalUserPriority.setStatus("current")


class _Hwftpdirction_Type(DisplayString):
    """Custom type hwftpdirction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hwftpdirction_Type.__name__ = "DisplayString"
_Hwftpdirction_Object = MibTableColumn
hwftpdirction = _Hwftpdirction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 5),
    _Hwftpdirction_Type()
)
hwftpdirction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwftpdirction.setStatus("current")


class _HwQosProfileName_Type(DisplayString):
    """Custom type hwQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwQosProfileName_Type.__name__ = "DisplayString"
_HwQosProfileName_Object = MibTableColumn
hwQosProfileName = _HwQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 6),
    _HwQosProfileName_Type()
)
hwQosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQosProfileName.setStatus("current")
_HwLocalUserRowStatus_Type = RowStatus
_HwLocalUserRowStatus_Object = MibTableColumn
hwLocalUserRowStatus = _HwLocalUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 12),
    _HwLocalUserRowStatus_Type()
)
hwLocalUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalUserRowStatus.setStatus("current")
_HwLocalUserIpAddress_Type = IpAddress
_HwLocalUserIpAddress_Object = MibTableColumn
hwLocalUserIpAddress = _HwLocalUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 13),
    _HwLocalUserIpAddress_Type()
)
hwLocalUserIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserIpAddress.setStatus("current")


class _HwLocalUserVpnInstance_Type(DisplayString):
    """Custom type hwLocalUserVpnInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwLocalUserVpnInstance_Type.__name__ = "DisplayString"
_HwLocalUserVpnInstance_Object = MibTableColumn
hwLocalUserVpnInstance = _HwLocalUserVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 14),
    _HwLocalUserVpnInstance_Type()
)
hwLocalUserVpnInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserVpnInstance.setStatus("current")


class _HwLocalUserAccessLimitNum_Type(Unsigned32):
    """Custom type hwLocalUserAccessLimitNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwLocalUserAccessLimitNum_Type.__name__ = "Unsigned32"
_HwLocalUserAccessLimitNum_Object = MibTableColumn
hwLocalUserAccessLimitNum = _HwLocalUserAccessLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 15),
    _HwLocalUserAccessLimitNum_Type()
)
hwLocalUserAccessLimitNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalUserAccessLimitNum.setStatus("current")


class _HwLocalUserPasswordLifetimeMin_Type(Integer32):
    """Custom type hwLocalUserPasswordLifetimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwLocalUserPasswordLifetimeMin_Type.__name__ = "Integer32"
_HwLocalUserPasswordLifetimeMin_Object = MibTableColumn
hwLocalUserPasswordLifetimeMin = _HwLocalUserPasswordLifetimeMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 16),
    _HwLocalUserPasswordLifetimeMin_Type()
)
hwLocalUserPasswordLifetimeMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalUserPasswordLifetimeMin.setStatus("current")


class _HwLocalUserPasswordLifetimeMax_Type(Integer32):
    """Custom type hwLocalUserPasswordLifetimeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwLocalUserPasswordLifetimeMax_Type.__name__ = "Integer32"
_HwLocalUserPasswordLifetimeMax_Object = MibTableColumn
hwLocalUserPasswordLifetimeMax = _HwLocalUserPasswordLifetimeMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 17),
    _HwLocalUserPasswordLifetimeMax_Type()
)
hwLocalUserPasswordLifetimeMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalUserPasswordLifetimeMax.setStatus("current")


class _HwLocalUserIfAllowWeakPassword_Type(Integer32):
    """Custom type hwLocalUserIfAllowWeakPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("notallow", 1))
    )


_HwLocalUserIfAllowWeakPassword_Type.__name__ = "Integer32"
_HwLocalUserIfAllowWeakPassword_Object = MibTableColumn
hwLocalUserIfAllowWeakPassword = _HwLocalUserIfAllowWeakPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 18),
    _HwLocalUserIfAllowWeakPassword_Type()
)
hwLocalUserIfAllowWeakPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserIfAllowWeakPassword.setStatus("current")


class _HwLocalUserPasswordSetTime_Type(DisplayString):
    """Custom type hwLocalUserPasswordSetTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwLocalUserPasswordSetTime_Type.__name__ = "DisplayString"
_HwLocalUserPasswordSetTime_Object = MibTableColumn
hwLocalUserPasswordSetTime = _HwLocalUserPasswordSetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 19),
    _HwLocalUserPasswordSetTime_Type()
)
hwLocalUserPasswordSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUserPasswordSetTime.setStatus("current")


class _HwLocalUserPasswordExpireTime_Type(DisplayString):
    """Custom type hwLocalUserPasswordExpireTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwLocalUserPasswordExpireTime_Type.__name__ = "DisplayString"
_HwLocalUserPasswordExpireTime_Object = MibTableColumn
hwLocalUserPasswordExpireTime = _HwLocalUserPasswordExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 20),
    _HwLocalUserPasswordExpireTime_Type()
)
hwLocalUserPasswordExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUserPasswordExpireTime.setStatus("current")


class _HwLocalUserPasswordIsExpired_Type(Integer32):
    """Custom type hwLocalUserPasswordIsExpired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("expired", 1),
          ("notExpired", 0))
    )


_HwLocalUserPasswordIsExpired_Type.__name__ = "Integer32"
_HwLocalUserPasswordIsExpired_Object = MibTableColumn
hwLocalUserPasswordIsExpired = _HwLocalUserPasswordIsExpired_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 21),
    _HwLocalUserPasswordIsExpired_Type()
)
hwLocalUserPasswordIsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUserPasswordIsExpired.setStatus("current")


class _HwLocalUserPasswordIsOrginal_Type(Integer32):
    """Custom type hwLocalUserPasswordIsOrginal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOrginal", 0),
          ("orginal", 1))
    )


_HwLocalUserPasswordIsOrginal_Type.__name__ = "Integer32"
_HwLocalUserPasswordIsOrginal_Object = MibTableColumn
hwLocalUserPasswordIsOrginal = _HwLocalUserPasswordIsOrginal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 10, 1, 22),
    _HwLocalUserPasswordIsOrginal_Type()
)
hwLocalUserPasswordIsOrginal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUserPasswordIsOrginal.setStatus("current")
_HwLocalUserExtTable_Object = MibTable
hwLocalUserExtTable = _HwLocalUserExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hwLocalUserExtTable.setStatus("current")
_HwLocalUserExtEntry_Object = MibTableRow
hwLocalUserExtEntry = _HwLocalUserExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1)
)
hwLocalUserExtEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwLocalUserName"),
)
if mibBuilder.loadTexts:
    hwLocalUserExtEntry.setStatus("current")


class _HwLocalUserState_Type(Integer32):
    """Custom type hwLocalUserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 0))
    )


_HwLocalUserState_Type.__name__ = "Integer32"
_HwLocalUserState_Object = MibTableColumn
hwLocalUserState = _HwLocalUserState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 2),
    _HwLocalUserState_Type()
)
hwLocalUserState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserState.setStatus("current")
_HwLocalUserNoCallBackVerify_Type = TruthValue
_HwLocalUserNoCallBackVerify_Object = MibTableColumn
hwLocalUserNoCallBackVerify = _HwLocalUserNoCallBackVerify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 3),
    _HwLocalUserNoCallBackVerify_Type()
)
hwLocalUserNoCallBackVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserNoCallBackVerify.setStatus("current")


class _HwLocalUserCallBackDialStr_Type(DisplayString):
    """Custom type hwLocalUserCallBackDialStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwLocalUserCallBackDialStr_Type.__name__ = "DisplayString"
_HwLocalUserCallBackDialStr_Object = MibTableColumn
hwLocalUserCallBackDialStr = _HwLocalUserCallBackDialStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 4),
    _HwLocalUserCallBackDialStr_Type()
)
hwLocalUserCallBackDialStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserCallBackDialStr.setStatus("current")


class _HwLocalUserBlockFailTimes_Type(Integer32):
    """Custom type hwLocalUserBlockFailTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HwLocalUserBlockFailTimes_Type.__name__ = "Integer32"
_HwLocalUserBlockFailTimes_Object = MibTableColumn
hwLocalUserBlockFailTimes = _HwLocalUserBlockFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 5),
    _HwLocalUserBlockFailTimes_Type()
)
hwLocalUserBlockFailTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalUserBlockFailTimes.setStatus("current")


class _HwLocalUserBlockInterval_Type(Integer32):
    """Custom type hwLocalUserBlockInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwLocalUserBlockInterval_Type.__name__ = "Integer32"
_HwLocalUserBlockInterval_Object = MibTableColumn
hwLocalUserBlockInterval = _HwLocalUserBlockInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 6),
    _HwLocalUserBlockInterval_Type()
)
hwLocalUserBlockInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalUserBlockInterval.setStatus("current")


class _HwLocalUserUserGroup_Type(DisplayString):
    """Custom type hwLocalUserUserGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwLocalUserUserGroup_Type.__name__ = "DisplayString"
_HwLocalUserUserGroup_Object = MibTableColumn
hwLocalUserUserGroup = _HwLocalUserUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 7),
    _HwLocalUserUserGroup_Type()
)
hwLocalUserUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserUserGroup.setStatus("current")


class _HwLocalUserDeviceType_Type(DisplayString):
    """Custom type hwLocalUserDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_HwLocalUserDeviceType_Type.__name__ = "DisplayString"
_HwLocalUserDeviceType_Object = MibTableColumn
hwLocalUserDeviceType = _HwLocalUserDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 8),
    _HwLocalUserDeviceType_Type()
)
hwLocalUserDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserDeviceType.setStatus("current")


class _HwLocalUserExpireDate_Type(DisplayString):
    """Custom type hwLocalUserExpireDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HwLocalUserExpireDate_Type.__name__ = "DisplayString"
_HwLocalUserExpireDate_Object = MibTableColumn
hwLocalUserExpireDate = _HwLocalUserExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 9),
    _HwLocalUserExpireDate_Type()
)
hwLocalUserExpireDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserExpireDate.setStatus("current")


class _HwLocalUserIdleTimeoutSecond_Type(Integer32):
    """Custom type hwLocalUserIdleTimeoutSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwLocalUserIdleTimeoutSecond_Type.__name__ = "Integer32"
_HwLocalUserIdleTimeoutSecond_Object = MibTableColumn
hwLocalUserIdleTimeoutSecond = _HwLocalUserIdleTimeoutSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 10),
    _HwLocalUserIdleTimeoutSecond_Type()
)
hwLocalUserIdleTimeoutSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserIdleTimeoutSecond.setStatus("current")


class _HwLocalUserTimeRange_Type(DisplayString):
    """Custom type hwLocalUserTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwLocalUserTimeRange_Type.__name__ = "DisplayString"
_HwLocalUserTimeRange_Object = MibTableColumn
hwLocalUserTimeRange = _HwLocalUserTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 11, 1, 11),
    _HwLocalUserTimeRange_Type()
)
hwLocalUserTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalUserTimeRange.setStatus("current")
_HwAAASetting_ObjectIdentity = ObjectIdentity
hwAAASetting = _HwAAASetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13)
)
_HwAAASettingEntry_ObjectIdentity = ObjectIdentity
hwAAASettingEntry = _HwAAASettingEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1)
)


class _HwRoamChar_Type(DisplayString):
    """Custom type hwRoamChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HwRoamChar_Type.__name__ = "DisplayString"
_HwRoamChar_Object = MibScalar
hwRoamChar = _HwRoamChar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 1),
    _HwRoamChar_Type()
)
hwRoamChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRoamChar.setStatus("current")
_HwGlobalControl_Type = TruthValue
_HwGlobalControl_Object = MibScalar
hwGlobalControl = _HwGlobalControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 2),
    _HwGlobalControl_Type()
)
hwGlobalControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalControl.setStatus("current")


class _HwSystemRecord_Type(DisplayString):
    """Custom type hwSystemRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwSystemRecord_Type.__name__ = "DisplayString"
_HwSystemRecord_Object = MibScalar
hwSystemRecord = _HwSystemRecord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 3),
    _HwSystemRecord_Type()
)
hwSystemRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSystemRecord.setStatus("current")


class _HwOutboundRecord_Type(DisplayString):
    """Custom type hwOutboundRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwOutboundRecord_Type.__name__ = "DisplayString"
_HwOutboundRecord_Object = MibScalar
hwOutboundRecord = _HwOutboundRecord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 4),
    _HwOutboundRecord_Type()
)
hwOutboundRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOutboundRecord.setStatus("current")


class _HwCmdRecord_Type(DisplayString):
    """Custom type hwCmdRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwCmdRecord_Type.__name__ = "DisplayString"
_HwCmdRecord_Object = MibScalar
hwCmdRecord = _HwCmdRecord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 5),
    _HwCmdRecord_Type()
)
hwCmdRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCmdRecord.setStatus("current")
_HwPPPUserOfflineStandardize_Type = TruthValue
_HwPPPUserOfflineStandardize_Object = MibScalar
hwPPPUserOfflineStandardize = _HwPPPUserOfflineStandardize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 6),
    _HwPPPUserOfflineStandardize_Type()
)
hwPPPUserOfflineStandardize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPPPUserOfflineStandardize.setStatus("current")


class _HwDomainNameParseDirection_Type(Integer32):
    """Custom type hwDomainNameParseDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lefttoright", 0),
          ("righttoleft", 1))
    )


_HwDomainNameParseDirection_Type.__name__ = "Integer32"
_HwDomainNameParseDirection_Object = MibScalar
hwDomainNameParseDirection = _HwDomainNameParseDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 7),
    _HwDomainNameParseDirection_Type()
)
hwDomainNameParseDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainNameParseDirection.setStatus("current")


class _HwDomainNameLocation_Type(Integer32):
    """Custom type hwDomainNameLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("afterdelimiter", 1),
          ("beforedelimiter", 0))
    )


_HwDomainNameLocation_Type.__name__ = "Integer32"
_HwDomainNameLocation_Object = MibScalar
hwDomainNameLocation = _HwDomainNameLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 8),
    _HwDomainNameLocation_Type()
)
hwDomainNameLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainNameLocation.setStatus("current")


class _HwAccessSpeedNumber_Type(Integer32):
    """Custom type hwAccessSpeedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAccessSpeedNumber_Type.__name__ = "Integer32"
_HwAccessSpeedNumber_Object = MibScalar
hwAccessSpeedNumber = _HwAccessSpeedNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 9),
    _HwAccessSpeedNumber_Type()
)
hwAccessSpeedNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccessSpeedNumber.setStatus("current")


class _HwAccessSpeedPeriod_Type(Integer32):
    """Custom type hwAccessSpeedPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAccessSpeedPeriod_Type.__name__ = "Integer32"
_HwAccessSpeedPeriod_Object = MibScalar
hwAccessSpeedPeriod = _HwAccessSpeedPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 10),
    _HwAccessSpeedPeriod_Type()
)
hwAccessSpeedPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccessSpeedPeriod.setStatus("current")


class _HwRealmNameChar_Type(DisplayString):
    """Custom type hwRealmNameChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HwRealmNameChar_Type.__name__ = "DisplayString"
_HwRealmNameChar_Object = MibScalar
hwRealmNameChar = _HwRealmNameChar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 11),
    _HwRealmNameChar_Type()
)
hwRealmNameChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRealmNameChar.setStatus("current")


class _HwRealmParseDirection_Type(Integer32):
    """Custom type hwRealmParseDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lefttoright", 0),
          ("righttoleft", 1))
    )


_HwRealmParseDirection_Type.__name__ = "Integer32"
_HwRealmParseDirection_Object = MibScalar
hwRealmParseDirection = _HwRealmParseDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 12),
    _HwRealmParseDirection_Type()
)
hwRealmParseDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRealmParseDirection.setStatus("current")


class _HwIPOXpassword_Type(DisplayString):
    """Custom type hwIPOXpassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwIPOXpassword_Type.__name__ = "DisplayString"
_HwIPOXpassword_Object = MibScalar
hwIPOXpassword = _HwIPOXpassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 14),
    _HwIPOXpassword_Type()
)
hwIPOXpassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPOXpassword.setStatus("current")


class _HwAccessDelayTransitionStep_Type(Integer32):
    """Custom type hwAccessDelayTransitionStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_HwAccessDelayTransitionStep_Type.__name__ = "Integer32"
_HwAccessDelayTransitionStep_Object = MibScalar
hwAccessDelayTransitionStep = _HwAccessDelayTransitionStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 16),
    _HwAccessDelayTransitionStep_Type()
)
hwAccessDelayTransitionStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccessDelayTransitionStep.setStatus("current")


class _HwAccessDelayTime_Type(Integer32):
    """Custom type hwAccessDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2550),
    )


_HwAccessDelayTime_Type.__name__ = "Integer32"
_HwAccessDelayTime_Object = MibScalar
hwAccessDelayTime = _HwAccessDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 17),
    _HwAccessDelayTime_Type()
)
hwAccessDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccessDelayTime.setStatus("current")


class _HwAccessDelayMinTime_Type(Integer32):
    """Custom type hwAccessDelayMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2550),
    )


_HwAccessDelayMinTime_Type.__name__ = "Integer32"
_HwAccessDelayMinTime_Object = MibScalar
hwAccessDelayMinTime = _HwAccessDelayMinTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 18),
    _HwAccessDelayMinTime_Type()
)
hwAccessDelayMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccessDelayMinTime.setStatus("current")


class _HwParsePriority_Type(Integer32):
    """Custom type hwParsePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("domainfirst", 0),
          ("realmfirst", 1))
    )


_HwParsePriority_Type.__name__ = "Integer32"
_HwParsePriority_Object = MibScalar
hwParsePriority = _HwParsePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 19),
    _HwParsePriority_Type()
)
hwParsePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwParsePriority.setStatus("current")


class _HwRealmNameLocation_Type(Integer32):
    """Custom type hwRealmNameLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("afterdelimiter", 1),
          ("beforedelimiter", 0))
    )


_HwRealmNameLocation_Type.__name__ = "Integer32"
_HwRealmNameLocation_Object = MibScalar
hwRealmNameLocation = _HwRealmNameLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 20),
    _HwRealmNameLocation_Type()
)
hwRealmNameLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRealmNameLocation.setStatus("current")


class _HwIPOXUsernameOption82_Type(Integer32):
    """Custom type hwIPOXUsernameOption82 based on Integer32"""
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
        *(("first", 1),
          ("fourth", 4),
          ("none", 0),
          ("second", 2),
          ("third", 3))
    )


_HwIPOXUsernameOption82_Type.__name__ = "Integer32"
_HwIPOXUsernameOption82_Object = MibScalar
hwIPOXUsernameOption82 = _HwIPOXUsernameOption82_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 21),
    _HwIPOXUsernameOption82_Type()
)
hwIPOXUsernameOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPOXUsernameOption82.setStatus("current")


class _HwIPOXUsernameIP_Type(Integer32):
    """Custom type hwIPOXUsernameIP based on Integer32"""
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
        *(("first", 1),
          ("fourth", 4),
          ("none", 0),
          ("second", 2),
          ("third", 3))
    )


_HwIPOXUsernameIP_Type.__name__ = "Integer32"
_HwIPOXUsernameIP_Object = MibScalar
hwIPOXUsernameIP = _HwIPOXUsernameIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 22),
    _HwIPOXUsernameIP_Type()
)
hwIPOXUsernameIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPOXUsernameIP.setStatus("current")


class _HwIPOXUsernameSysname_Type(Integer32):
    """Custom type hwIPOXUsernameSysname based on Integer32"""
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
        *(("first", 1),
          ("fourth", 4),
          ("none", 0),
          ("second", 2),
          ("third", 3))
    )


_HwIPOXUsernameSysname_Type.__name__ = "Integer32"
_HwIPOXUsernameSysname_Object = MibScalar
hwIPOXUsernameSysname = _HwIPOXUsernameSysname_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 23),
    _HwIPOXUsernameSysname_Type()
)
hwIPOXUsernameSysname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPOXUsernameSysname.setStatus("current")


class _HwIPOXUsernameMAC_Type(Integer32):
    """Custom type hwIPOXUsernameMAC based on Integer32"""
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
        *(("first", 1),
          ("fourth", 4),
          ("none", 0),
          ("second", 2),
          ("third", 3))
    )


_HwIPOXUsernameMAC_Type.__name__ = "Integer32"
_HwIPOXUsernameMAC_Object = MibScalar
hwIPOXUsernameMAC = _HwIPOXUsernameMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 24),
    _HwIPOXUsernameMAC_Type()
)
hwIPOXUsernameMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPOXUsernameMAC.setStatus("current")


class _HwDefaultUserName_Type(DisplayString):
    """Custom type hwDefaultUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDefaultUserName_Type.__name__ = "DisplayString"
_HwDefaultUserName_Object = MibScalar
hwDefaultUserName = _HwDefaultUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 25),
    _HwDefaultUserName_Type()
)
hwDefaultUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDefaultUserName.setStatus("current")


class _HwNasSerial_Type(DisplayString):
    """Custom type hwNasSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwNasSerial_Type.__name__ = "DisplayString"
_HwNasSerial_Object = MibScalar
hwNasSerial = _HwNasSerial_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 26),
    _HwNasSerial_Type()
)
hwNasSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNasSerial.setStatus("current")


class _HwAAAPasswordRepeatNumber_Type(Integer32):
    """Custom type hwAAAPasswordRepeatNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_HwAAAPasswordRepeatNumber_Type.__name__ = "Integer32"
_HwAAAPasswordRepeatNumber_Object = MibScalar
hwAAAPasswordRepeatNumber = _HwAAAPasswordRepeatNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 27),
    _HwAAAPasswordRepeatNumber_Type()
)
hwAAAPasswordRepeatNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAAAPasswordRepeatNumber.setStatus("current")


class _HwAAAPasswordRemindDay_Type(Integer32):
    """Custom type hwAAAPasswordRemindDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_HwAAAPasswordRemindDay_Type.__name__ = "Integer32"
_HwAAAPasswordRemindDay_Object = MibScalar
hwAAAPasswordRemindDay = _HwAAAPasswordRemindDay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 28),
    _HwAAAPasswordRemindDay_Type()
)
hwAAAPasswordRemindDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAAAPasswordRemindDay.setStatus("current")


class _HwOnlineUserNumLowerLimitThreshold_Type(Integer32):
    """Custom type hwOnlineUserNumLowerLimitThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
        ValueRangeConstraint(255, 255),
    )


_HwOnlineUserNumLowerLimitThreshold_Type.__name__ = "Integer32"
_HwOnlineUserNumLowerLimitThreshold_Object = MibScalar
hwOnlineUserNumLowerLimitThreshold = _HwOnlineUserNumLowerLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 29),
    _HwOnlineUserNumLowerLimitThreshold_Type()
)
hwOnlineUserNumLowerLimitThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOnlineUserNumLowerLimitThreshold.setStatus("current")


class _HwOnlineUserNumUpperLimitThreshold_Type(Integer32):
    """Custom type hwOnlineUserNumUpperLimitThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(255, 255),
    )


_HwOnlineUserNumUpperLimitThreshold_Type.__name__ = "Integer32"
_HwOnlineUserNumUpperLimitThreshold_Object = MibScalar
hwOnlineUserNumUpperLimitThreshold = _HwOnlineUserNumUpperLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 30),
    _HwOnlineUserNumUpperLimitThreshold_Type()
)
hwOnlineUserNumUpperLimitThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOnlineUserNumUpperLimitThreshold.setStatus("current")


class _HwTriggerLoose_Type(Unsigned32):
    """Custom type hwTriggerLoose based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_HwTriggerLoose_Type.__name__ = "Unsigned32"
_HwTriggerLoose_Object = MibScalar
hwTriggerLoose = _HwTriggerLoose_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 31),
    _HwTriggerLoose_Type()
)
hwTriggerLoose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTriggerLoose.setStatus("current")


class _HwOfflineSpeedNumber_Type(Integer32):
    """Custom type hwOfflineSpeedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 256),
    )


_HwOfflineSpeedNumber_Type.__name__ = "Integer32"
_HwOfflineSpeedNumber_Object = MibScalar
hwOfflineSpeedNumber = _HwOfflineSpeedNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 32),
    _HwOfflineSpeedNumber_Type()
)
hwOfflineSpeedNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOfflineSpeedNumber.setStatus("current")


class _HwIPOXpasswordKeyType_Type(Integer32):
    """Custom type hwIPOXpasswordKeyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("simple", 1))
    )


_HwIPOXpasswordKeyType_Type.__name__ = "Integer32"
_HwIPOXpasswordKeyType_Object = MibScalar
hwIPOXpasswordKeyType = _HwIPOXpasswordKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 33),
    _HwIPOXpasswordKeyType_Type()
)
hwIPOXpasswordKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPOXpasswordKeyType.setStatus("current")


class _HwReauthorizeEnable_Type(Integer32):
    """Custom type hwReauthorizeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwReauthorizeEnable_Type.__name__ = "Integer32"
_HwReauthorizeEnable_Object = MibScalar
hwReauthorizeEnable = _HwReauthorizeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 34),
    _HwReauthorizeEnable_Type()
)
hwReauthorizeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwReauthorizeEnable.setStatus("current")


class _HwDomainNameDelimiter_Type(DisplayString):
    """Custom type hwDomainNameDelimiter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HwDomainNameDelimiter_Type.__name__ = "DisplayString"
_HwDomainNameDelimiter_Object = MibScalar
hwDomainNameDelimiter = _HwDomainNameDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 35),
    _HwDomainNameDelimiter_Type()
)
hwDomainNameDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainNameDelimiter.setStatus("current")


class _HwDomainNameSecurityDelimiter_Type(DisplayString):
    """Custom type hwDomainNameSecurityDelimiter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HwDomainNameSecurityDelimiter_Type.__name__ = "DisplayString"
_HwDomainNameSecurityDelimiter_Object = MibScalar
hwDomainNameSecurityDelimiter = _HwDomainNameSecurityDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 36),
    _HwDomainNameSecurityDelimiter_Type()
)
hwDomainNameSecurityDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainNameSecurityDelimiter.setStatus("current")


class _HwGlobalAuthEventAuthFailResponseFail_Type(Integer32):
    """Custom type hwGlobalAuthEventAuthFailResponseFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwGlobalAuthEventAuthFailResponseFail_Type.__name__ = "Integer32"
_HwGlobalAuthEventAuthFailResponseFail_Object = MibScalar
hwGlobalAuthEventAuthFailResponseFail = _HwGlobalAuthEventAuthFailResponseFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 37),
    _HwGlobalAuthEventAuthFailResponseFail_Type()
)
hwGlobalAuthEventAuthFailResponseFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventAuthFailResponseFail.setStatus("current")


class _HwGlobalAuthEventAuthFailVlan_Type(Integer32):
    """Custom type hwGlobalAuthEventAuthFailVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwGlobalAuthEventAuthFailVlan_Type.__name__ = "Integer32"
_HwGlobalAuthEventAuthFailVlan_Object = MibScalar
hwGlobalAuthEventAuthFailVlan = _HwGlobalAuthEventAuthFailVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 38),
    _HwGlobalAuthEventAuthFailVlan_Type()
)
hwGlobalAuthEventAuthFailVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventAuthFailVlan.setStatus("current")


class _HwGlobalAuthEventAuthenServerDownResponseFail_Type(Integer32):
    """Custom type hwGlobalAuthEventAuthenServerDownResponseFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwGlobalAuthEventAuthenServerDownResponseFail_Type.__name__ = "Integer32"
_HwGlobalAuthEventAuthenServerDownResponseFail_Object = MibScalar
hwGlobalAuthEventAuthenServerDownResponseFail = _HwGlobalAuthEventAuthenServerDownResponseFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 39),
    _HwGlobalAuthEventAuthenServerDownResponseFail_Type()
)
hwGlobalAuthEventAuthenServerDownResponseFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventAuthenServerDownResponseFail.setStatus("current")


class _HwGlobalAuthEventAuthenServerDownVlan_Type(Integer32):
    """Custom type hwGlobalAuthEventAuthenServerDownVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwGlobalAuthEventAuthenServerDownVlan_Type.__name__ = "Integer32"
_HwGlobalAuthEventAuthenServerDownVlan_Object = MibScalar
hwGlobalAuthEventAuthenServerDownVlan = _HwGlobalAuthEventAuthenServerDownVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 40),
    _HwGlobalAuthEventAuthenServerDownVlan_Type()
)
hwGlobalAuthEventAuthenServerDownVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventAuthenServerDownVlan.setStatus("current")


class _HwGlobalAuthEventClientNoResponseVlan_Type(Integer32):
    """Custom type hwGlobalAuthEventClientNoResponseVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwGlobalAuthEventClientNoResponseVlan_Type.__name__ = "Integer32"
_HwGlobalAuthEventClientNoResponseVlan_Object = MibScalar
hwGlobalAuthEventClientNoResponseVlan = _HwGlobalAuthEventClientNoResponseVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 41),
    _HwGlobalAuthEventClientNoResponseVlan_Type()
)
hwGlobalAuthEventClientNoResponseVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventClientNoResponseVlan.setStatus("current")


class _HwGlobalAuthEventPreAuthVlan_Type(Integer32):
    """Custom type hwGlobalAuthEventPreAuthVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwGlobalAuthEventPreAuthVlan_Type.__name__ = "Integer32"
_HwGlobalAuthEventPreAuthVlan_Object = MibScalar
hwGlobalAuthEventPreAuthVlan = _HwGlobalAuthEventPreAuthVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 42),
    _HwGlobalAuthEventPreAuthVlan_Type()
)
hwGlobalAuthEventPreAuthVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventPreAuthVlan.setStatus("current")


class _HwGlobalAuthEventAuthFailUserGroup_Type(OctetString):
    """Custom type hwGlobalAuthEventAuthFailUserGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwGlobalAuthEventAuthFailUserGroup_Type.__name__ = "OctetString"
_HwGlobalAuthEventAuthFailUserGroup_Object = MibScalar
hwGlobalAuthEventAuthFailUserGroup = _HwGlobalAuthEventAuthFailUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 43),
    _HwGlobalAuthEventAuthFailUserGroup_Type()
)
hwGlobalAuthEventAuthFailUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventAuthFailUserGroup.setStatus("current")


class _HwGlobalAuthEventAuthenServerDownUserGroup_Type(OctetString):
    """Custom type hwGlobalAuthEventAuthenServerDownUserGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwGlobalAuthEventAuthenServerDownUserGroup_Type.__name__ = "OctetString"
_HwGlobalAuthEventAuthenServerDownUserGroup_Object = MibScalar
hwGlobalAuthEventAuthenServerDownUserGroup = _HwGlobalAuthEventAuthenServerDownUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 44),
    _HwGlobalAuthEventAuthenServerDownUserGroup_Type()
)
hwGlobalAuthEventAuthenServerDownUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventAuthenServerDownUserGroup.setStatus("current")


class _HwGlobalAuthEventClientNoResponseUserGroup_Type(OctetString):
    """Custom type hwGlobalAuthEventClientNoResponseUserGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwGlobalAuthEventClientNoResponseUserGroup_Type.__name__ = "OctetString"
_HwGlobalAuthEventClientNoResponseUserGroup_Object = MibScalar
hwGlobalAuthEventClientNoResponseUserGroup = _HwGlobalAuthEventClientNoResponseUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 45),
    _HwGlobalAuthEventClientNoResponseUserGroup_Type()
)
hwGlobalAuthEventClientNoResponseUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventClientNoResponseUserGroup.setStatus("current")


class _HwGlobalAuthEventPreAuthUserGroup_Type(OctetString):
    """Custom type hwGlobalAuthEventPreAuthUserGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwGlobalAuthEventPreAuthUserGroup_Type.__name__ = "OctetString"
_HwGlobalAuthEventPreAuthUserGroup_Object = MibScalar
hwGlobalAuthEventPreAuthUserGroup = _HwGlobalAuthEventPreAuthUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 46),
    _HwGlobalAuthEventPreAuthUserGroup_Type()
)
hwGlobalAuthEventPreAuthUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalAuthEventPreAuthUserGroup.setStatus("current")


class _HwAuthorModifyMode_Type(Integer32):
    """Custom type hwAuthorModifyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("modify", 1),
          ("overlay", 0))
    )


_HwAuthorModifyMode_Type.__name__ = "Integer32"
_HwAuthorModifyMode_Object = MibScalar
hwAuthorModifyMode = _HwAuthorModifyMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 47),
    _HwAuthorModifyMode_Type()
)
hwAuthorModifyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthorModifyMode.setStatus("current")


class _HwLocalRetryInterval_Type(Integer32):
    """Custom type hwLocalRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_HwLocalRetryInterval_Type.__name__ = "Integer32"
_HwLocalRetryInterval_Object = MibScalar
hwLocalRetryInterval = _HwLocalRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 48),
    _HwLocalRetryInterval_Type()
)
hwLocalRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalRetryInterval.setStatus("current")


class _HwLocalRetryTime_Type(Integer32):
    """Custom type hwLocalRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_HwLocalRetryTime_Type.__name__ = "Integer32"
_HwLocalRetryTime_Object = MibScalar
hwLocalRetryTime = _HwLocalRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 49),
    _HwLocalRetryTime_Type()
)
hwLocalRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalRetryTime.setStatus("current")


class _HwLocalBlockTime_Type(Integer32):
    """Custom type hwLocalBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_HwLocalBlockTime_Type.__name__ = "Integer32"
_HwLocalBlockTime_Object = MibScalar
hwLocalBlockTime = _HwLocalBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 50),
    _HwLocalBlockTime_Type()
)
hwLocalBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBlockTime.setStatus("current")


class _HwRemoteRetryInterval_Type(Integer32):
    """Custom type hwRemoteRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_HwRemoteRetryInterval_Type.__name__ = "Integer32"
_HwRemoteRetryInterval_Object = MibScalar
hwRemoteRetryInterval = _HwRemoteRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 51),
    _HwRemoteRetryInterval_Type()
)
hwRemoteRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteRetryInterval.setStatus("current")


class _HwRemoteRetryTime_Type(Integer32):
    """Custom type hwRemoteRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_HwRemoteRetryTime_Type.__name__ = "Integer32"
_HwRemoteRetryTime_Object = MibScalar
hwRemoteRetryTime = _HwRemoteRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 52),
    _HwRemoteRetryTime_Type()
)
hwRemoteRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteRetryTime.setStatus("current")


class _HwRemoteBlockTime_Type(Integer32):
    """Custom type hwRemoteBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_HwRemoteBlockTime_Type.__name__ = "Integer32"
_HwRemoteBlockTime_Object = MibScalar
hwRemoteBlockTime = _HwRemoteBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 53),
    _HwRemoteBlockTime_Type()
)
hwRemoteBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteBlockTime.setStatus("current")


class _HwBlockDisable_Type(Integer32):
    """Custom type hwBlockDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localremoteuser", 2),
          ("localuser", 0),
          ("remoteuser", 1))
    )


_HwBlockDisable_Type.__name__ = "Integer32"
_HwBlockDisable_Object = MibScalar
hwBlockDisable = _HwBlockDisable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 13, 1, 54),
    _HwBlockDisable_Type()
)
hwBlockDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBlockDisable.setStatus("current")
_HwAAAStat_ObjectIdentity = ObjectIdentity
hwAAAStat = _HwAAAStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14)
)
_HwAAAStatEntry_ObjectIdentity = ObjectIdentity
hwAAAStatEntry = _HwAAAStatEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1)
)


class _HwTotalOnlineNum_Type(Unsigned32):
    """Custom type hwTotalOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalOnlineNum_Object = MibScalar
hwTotalOnlineNum = _HwTotalOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 1),
    _HwTotalOnlineNum_Type()
)
hwTotalOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalOnlineNum.setStatus("current")


class _HwTotalPPPoeOnlineNum_Type(Unsigned32):
    """Custom type hwTotalPPPoeOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalPPPoeOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalPPPoeOnlineNum_Object = MibScalar
hwTotalPPPoeOnlineNum = _HwTotalPPPoeOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 2),
    _HwTotalPPPoeOnlineNum_Type()
)
hwTotalPPPoeOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalPPPoeOnlineNum.setStatus("current")


class _HwTotalPPPoAOnlineNum_Type(Unsigned32):
    """Custom type hwTotalPPPoAOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalPPPoAOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalPPPoAOnlineNum_Object = MibScalar
hwTotalPPPoAOnlineNum = _HwTotalPPPoAOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 3),
    _HwTotalPPPoAOnlineNum_Type()
)
hwTotalPPPoAOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalPPPoAOnlineNum.setStatus("current")


class _HwTotalftpOnlineNum_Type(Unsigned32):
    """Custom type hwTotalftpOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalftpOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalftpOnlineNum_Object = MibScalar
hwTotalftpOnlineNum = _HwTotalftpOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 4),
    _HwTotalftpOnlineNum_Type()
)
hwTotalftpOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalftpOnlineNum.setStatus("current")


class _HwTotalsshOnlineNum_Type(Unsigned32):
    """Custom type hwTotalsshOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalsshOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalsshOnlineNum_Object = MibScalar
hwTotalsshOnlineNum = _HwTotalsshOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 5),
    _HwTotalsshOnlineNum_Type()
)
hwTotalsshOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalsshOnlineNum.setStatus("current")


class _HwTotaltelnetOnlineNum_Type(Unsigned32):
    """Custom type hwTotaltelnetOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotaltelnetOnlineNum_Type.__name__ = "Unsigned32"
_HwTotaltelnetOnlineNum_Object = MibScalar
hwTotaltelnetOnlineNum = _HwTotaltelnetOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 6),
    _HwTotaltelnetOnlineNum_Type()
)
hwTotaltelnetOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotaltelnetOnlineNum.setStatus("current")


class _HwTotalVLANOnlineNum_Type(Unsigned32):
    """Custom type hwTotalVLANOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalVLANOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalVLANOnlineNum_Object = MibScalar
hwTotalVLANOnlineNum = _HwTotalVLANOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 7),
    _HwTotalVLANOnlineNum_Type()
)
hwTotalVLANOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalVLANOnlineNum.setStatus("current")


class _HwHistoricMaxOnlineNum_Type(Unsigned32):
    """Custom type hwHistoricMaxOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwHistoricMaxOnlineNum_Type.__name__ = "Unsigned32"
_HwHistoricMaxOnlineNum_Object = MibScalar
hwHistoricMaxOnlineNum = _HwHistoricMaxOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 8),
    _HwHistoricMaxOnlineNum_Type()
)
hwHistoricMaxOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHistoricMaxOnlineNum.setStatus("current")


class _HwResetHistoricMaxOnlineNum_Type(Integer32):
    """Custom type hwResetHistoricMaxOnlineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )


_HwResetHistoricMaxOnlineNum_Type.__name__ = "Integer32"
_HwResetHistoricMaxOnlineNum_Object = MibScalar
hwResetHistoricMaxOnlineNum = _HwResetHistoricMaxOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 9),
    _HwResetHistoricMaxOnlineNum_Type()
)
hwResetHistoricMaxOnlineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwResetHistoricMaxOnlineNum.setStatus("current")


class _HwResetOfflineReasonStatistic_Type(Integer32):
    """Custom type hwResetOfflineReasonStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )


_HwResetOfflineReasonStatistic_Type.__name__ = "Integer32"
_HwResetOfflineReasonStatistic_Object = MibScalar
hwResetOfflineReasonStatistic = _HwResetOfflineReasonStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 10),
    _HwResetOfflineReasonStatistic_Type()
)
hwResetOfflineReasonStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwResetOfflineReasonStatistic.setStatus("current")


class _HwResetOnlineFailReasonStatistic_Type(Integer32):
    """Custom type hwResetOnlineFailReasonStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )


_HwResetOnlineFailReasonStatistic_Type.__name__ = "Integer32"
_HwResetOnlineFailReasonStatistic_Object = MibScalar
hwResetOnlineFailReasonStatistic = _HwResetOnlineFailReasonStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 11),
    _HwResetOnlineFailReasonStatistic_Type()
)
hwResetOnlineFailReasonStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwResetOnlineFailReasonStatistic.setStatus("current")


class _HwMaxPPPoeOnlineNum_Type(Unsigned32):
    """Custom type hwMaxPPPoeOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwMaxPPPoeOnlineNum_Type.__name__ = "Unsigned32"
_HwMaxPPPoeOnlineNum_Object = MibScalar
hwMaxPPPoeOnlineNum = _HwMaxPPPoeOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 12),
    _HwMaxPPPoeOnlineNum_Type()
)
hwMaxPPPoeOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaxPPPoeOnlineNum.setStatus("current")


class _HwTotalPortalServerUserNum_Type(Unsigned32):
    """Custom type hwTotalPortalServerUserNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalPortalServerUserNum_Type.__name__ = "Unsigned32"
_HwTotalPortalServerUserNum_Object = MibScalar
hwTotalPortalServerUserNum = _HwTotalPortalServerUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 13),
    _HwTotalPortalServerUserNum_Type()
)
hwTotalPortalServerUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalPortalServerUserNum.setStatus("current")


class _HwMaxPortalServerUserNum_Type(Unsigned32):
    """Custom type hwMaxPortalServerUserNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwMaxPortalServerUserNum_Type.__name__ = "Unsigned32"
_HwMaxPortalServerUserNum_Object = MibScalar
hwMaxPortalServerUserNum = _HwMaxPortalServerUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 14),
    _HwMaxPortalServerUserNum_Type()
)
hwMaxPortalServerUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaxPortalServerUserNum.setStatus("current")


class _HwTotalIPv4OnlineNum_Type(Unsigned32):
    """Custom type hwTotalIPv4OnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalIPv4OnlineNum_Type.__name__ = "Unsigned32"
_HwTotalIPv4OnlineNum_Object = MibScalar
hwTotalIPv4OnlineNum = _HwTotalIPv4OnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 15),
    _HwTotalIPv4OnlineNum_Type()
)
hwTotalIPv4OnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv4OnlineNum.setStatus("current")


class _HwTotalIPv6OnlineNum_Type(Unsigned32):
    """Custom type hwTotalIPv6OnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalIPv6OnlineNum_Type.__name__ = "Unsigned32"
_HwTotalIPv6OnlineNum_Object = MibScalar
hwTotalIPv6OnlineNum = _HwTotalIPv6OnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 16),
    _HwTotalIPv6OnlineNum_Type()
)
hwTotalIPv6OnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv6OnlineNum.setStatus("current")


class _HwTotalDualStackOnlineNum_Type(Unsigned32):
    """Custom type hwTotalDualStackOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalDualStackOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalDualStackOnlineNum_Object = MibScalar
hwTotalDualStackOnlineNum = _HwTotalDualStackOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 17),
    _HwTotalDualStackOnlineNum_Type()
)
hwTotalDualStackOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalDualStackOnlineNum.setStatus("current")
_HwTotalIPv4FlowDnByte_Type = Counter64
_HwTotalIPv4FlowDnByte_Object = MibScalar
hwTotalIPv4FlowDnByte = _HwTotalIPv4FlowDnByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 18),
    _HwTotalIPv4FlowDnByte_Type()
)
hwTotalIPv4FlowDnByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv4FlowDnByte.setStatus("current")
_HwTotalIPv4FlowDnPkt_Type = Counter64
_HwTotalIPv4FlowDnPkt_Object = MibScalar
hwTotalIPv4FlowDnPkt = _HwTotalIPv4FlowDnPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 19),
    _HwTotalIPv4FlowDnPkt_Type()
)
hwTotalIPv4FlowDnPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv4FlowDnPkt.setStatus("current")
_HwTotalIPv4FlowUpByte_Type = Counter64
_HwTotalIPv4FlowUpByte_Object = MibScalar
hwTotalIPv4FlowUpByte = _HwTotalIPv4FlowUpByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 20),
    _HwTotalIPv4FlowUpByte_Type()
)
hwTotalIPv4FlowUpByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv4FlowUpByte.setStatus("current")
_HwTotalIPv4FlowUpPkt_Type = Counter64
_HwTotalIPv4FlowUpPkt_Object = MibScalar
hwTotalIPv4FlowUpPkt = _HwTotalIPv4FlowUpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 21),
    _HwTotalIPv4FlowUpPkt_Type()
)
hwTotalIPv4FlowUpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv4FlowUpPkt.setStatus("current")
_HwTotalIPv6FlowDnByte_Type = Counter64
_HwTotalIPv6FlowDnByte_Object = MibScalar
hwTotalIPv6FlowDnByte = _HwTotalIPv6FlowDnByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 22),
    _HwTotalIPv6FlowDnByte_Type()
)
hwTotalIPv6FlowDnByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv6FlowDnByte.setStatus("current")
_HwTotalIPv6FlowDnPkt_Type = Counter64
_HwTotalIPv6FlowDnPkt_Object = MibScalar
hwTotalIPv6FlowDnPkt = _HwTotalIPv6FlowDnPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 23),
    _HwTotalIPv6FlowDnPkt_Type()
)
hwTotalIPv6FlowDnPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv6FlowDnPkt.setStatus("current")
_HwTotalIPv6FlowUpByte_Type = Counter64
_HwTotalIPv6FlowUpByte_Object = MibScalar
hwTotalIPv6FlowUpByte = _HwTotalIPv6FlowUpByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 24),
    _HwTotalIPv6FlowUpByte_Type()
)
hwTotalIPv6FlowUpByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv6FlowUpByte.setStatus("current")
_HwTotalIPv6FlowUpPkt_Type = Counter64
_HwTotalIPv6FlowUpPkt_Object = MibScalar
hwTotalIPv6FlowUpPkt = _HwTotalIPv6FlowUpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 25),
    _HwTotalIPv6FlowUpPkt_Type()
)
hwTotalIPv6FlowUpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPv6FlowUpPkt.setStatus("current")


class _HwHistoricMaxOnlineAcctReadyNum_Type(Unsigned32):
    """Custom type hwHistoricMaxOnlineAcctReadyNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwHistoricMaxOnlineAcctReadyNum_Type.__name__ = "Unsigned32"
_HwHistoricMaxOnlineAcctReadyNum_Object = MibScalar
hwHistoricMaxOnlineAcctReadyNum = _HwHistoricMaxOnlineAcctReadyNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 26),
    _HwHistoricMaxOnlineAcctReadyNum_Type()
)
hwHistoricMaxOnlineAcctReadyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHistoricMaxOnlineAcctReadyNum.setStatus("current")


class _HwPubicLacUserNum_Type(Unsigned32):
    """Custom type hwPubicLacUserNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwPubicLacUserNum_Type.__name__ = "Unsigned32"
_HwPubicLacUserNum_Object = MibScalar
hwPubicLacUserNum = _HwPubicLacUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 27),
    _HwPubicLacUserNum_Type()
)
hwPubicLacUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPubicLacUserNum.setStatus("current")


class _HwHistoricMaxOnlineLocalNum_Type(Unsigned32):
    """Custom type hwHistoricMaxOnlineLocalNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwHistoricMaxOnlineLocalNum_Type.__name__ = "Unsigned32"
_HwHistoricMaxOnlineLocalNum_Object = MibScalar
hwHistoricMaxOnlineLocalNum = _HwHistoricMaxOnlineLocalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 28),
    _HwHistoricMaxOnlineLocalNum_Type()
)
hwHistoricMaxOnlineLocalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHistoricMaxOnlineLocalNum.setStatus("current")


class _HwHistoricMaxOnlineRemoteNum_Type(Unsigned32):
    """Custom type hwHistoricMaxOnlineRemoteNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwHistoricMaxOnlineRemoteNum_Type.__name__ = "Unsigned32"
_HwHistoricMaxOnlineRemoteNum_Object = MibScalar
hwHistoricMaxOnlineRemoteNum = _HwHistoricMaxOnlineRemoteNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 29),
    _HwHistoricMaxOnlineRemoteNum_Type()
)
hwHistoricMaxOnlineRemoteNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHistoricMaxOnlineRemoteNum.setStatus("current")


class _HwTotalLacOnlineNum_Type(Unsigned32):
    """Custom type hwTotalLacOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalLacOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalLacOnlineNum_Object = MibScalar
hwTotalLacOnlineNum = _HwTotalLacOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 30),
    _HwTotalLacOnlineNum_Type()
)
hwTotalLacOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalLacOnlineNum.setStatus("current")


class _HwTotalLnsOnlineNum_Type(Unsigned32):
    """Custom type hwTotalLnsOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalLnsOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalLnsOnlineNum_Object = MibScalar
hwTotalLnsOnlineNum = _HwTotalLnsOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 31),
    _HwTotalLnsOnlineNum_Type()
)
hwTotalLnsOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalLnsOnlineNum.setStatus("current")


class _HwTotalWlsOnlineNum_Type(Unsigned32):
    """Custom type hwTotalWlsOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalWlsOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalWlsOnlineNum_Object = MibScalar
hwTotalWlsOnlineNum = _HwTotalWlsOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 32),
    _HwTotalWlsOnlineNum_Type()
)
hwTotalWlsOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalWlsOnlineNum.setStatus("current")


class _HwTotalWrdOnlineNum_Type(Unsigned32):
    """Custom type hwTotalWrdOnlineNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwTotalWrdOnlineNum_Type.__name__ = "Unsigned32"
_HwTotalWrdOnlineNum_Object = MibScalar
hwTotalWrdOnlineNum = _HwTotalWrdOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 33),
    _HwTotalWrdOnlineNum_Type()
)
hwTotalWrdOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalWrdOnlineNum.setStatus("current")


class _HwDhcpUserOnlineFailCount_Type(Unsigned32):
    """Custom type hwDhcpUserOnlineFailCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwDhcpUserOnlineFailCount_Type.__name__ = "Unsigned32"
_HwDhcpUserOnlineFailCount_Object = MibScalar
hwDhcpUserOnlineFailCount = _HwDhcpUserOnlineFailCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 14, 1, 34),
    _HwDhcpUserOnlineFailCount_Type()
)
hwDhcpUserOnlineFailCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpUserOnlineFailCount.setStatus("current")
_HwAccessTable_Object = MibTable
hwAccessTable = _HwAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15)
)
if mibBuilder.loadTexts:
    hwAccessTable.setStatus("current")
_HwAccessEntry_Object = MibTableRow
hwAccessEntry = _HwAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1)
)
hwAccessEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAccessIndex"),
)
if mibBuilder.loadTexts:
    hwAccessEntry.setStatus("current")


class _HwAccessIndex_Type(Integer32):
    """Custom type hwAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwAccessIndex_Type.__name__ = "Integer32"
_HwAccessIndex_Object = MibTableColumn
hwAccessIndex = _HwAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 1),
    _HwAccessIndex_Type()
)
hwAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIndex.setStatus("current")


class _HwAccessUserName_Type(DisplayString):
    """Custom type hwAccessUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_HwAccessUserName_Type.__name__ = "DisplayString"
_HwAccessUserName_Object = MibTableColumn
hwAccessUserName = _HwAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 3),
    _HwAccessUserName_Type()
)
hwAccessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessUserName.setStatus("current")


class _HwAccessPortType_Type(Integer32):
    """Custom type hwAccessPortType based on Integer32"""
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
        *(("all", 1),
          ("ftp", 8),
          ("igmp", 10),
          ("ppp", 2),
          ("ssh", 9),
          ("telnet", 7),
          ("vlan", 3),
          ("vlan8021x", 6),
          ("vlanportal", 5),
          ("vlanweb", 4))
    )


_HwAccessPortType_Type.__name__ = "Integer32"
_HwAccessPortType_Object = MibTableColumn
hwAccessPortType = _HwAccessPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 5),
    _HwAccessPortType_Type()
)
hwAccessPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessPortType.setStatus("current")


class _HwAccessPriority_Type(Integer32):
    """Custom type hwAccessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HwAccessPriority_Type.__name__ = "Integer32"
_HwAccessPriority_Object = MibTableColumn
hwAccessPriority = _HwAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 6),
    _HwAccessPriority_Type()
)
hwAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessPriority.setStatus("current")
_HwAccessSlotNo_Type = Integer32
_HwAccessSlotNo_Object = MibTableColumn
hwAccessSlotNo = _HwAccessSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 8),
    _HwAccessSlotNo_Type()
)
hwAccessSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessSlotNo.setStatus("current")
_HwAccessSubSlotNo_Type = Integer32
_HwAccessSubSlotNo_Object = MibTableColumn
hwAccessSubSlotNo = _HwAccessSubSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 9),
    _HwAccessSubSlotNo_Type()
)
hwAccessSubSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessSubSlotNo.setStatus("current")
_HwAccessPortNo_Type = Integer32
_HwAccessPortNo_Object = MibTableColumn
hwAccessPortNo = _HwAccessPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 10),
    _HwAccessPortNo_Type()
)
hwAccessPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessPortNo.setStatus("current")
_HwAccessVLANID_Type = Integer32
_HwAccessVLANID_Object = MibTableColumn
hwAccessVLANID = _HwAccessVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 11),
    _HwAccessVLANID_Type()
)
hwAccessVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessVLANID.setStatus("current")
_HwAccessPVC_Type = Integer32
_HwAccessPVC_Object = MibTableColumn
hwAccessPVC = _HwAccessPVC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 12),
    _HwAccessPVC_Type()
)
hwAccessPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessPVC.setStatus("current")


class _HwAccessAuthenMethod_Type(Integer32):
    """Custom type hwAccessAuthenMethod based on Integer32"""
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
        *(("local", 1),
          ("localRadius", 4),
          ("localTacacs", 8),
          ("noauth", 2),
          ("radius", 3),
          ("radiusLocal", 5),
          ("radiusNoauth", 6),
          ("tacacs", 7),
          ("tacacsLocal", 9),
          ("tacacsNone", 10))
    )


_HwAccessAuthenMethod_Type.__name__ = "Integer32"
_HwAccessAuthenMethod_Object = MibTableColumn
hwAccessAuthenMethod = _HwAccessAuthenMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 13),
    _HwAccessAuthenMethod_Type()
)
hwAccessAuthenMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessAuthenMethod.setStatus("current")


class _HwAccessAcctMethod_Type(Integer32):
    """Custom type hwAccessAcctMethod based on Integer32"""
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
        *(("hwtacacs", 5),
          ("local", 1),
          ("localhwtacacsboth", 6),
          ("localradiusboth", 4),
          ("noacct", 3),
          ("radius", 2))
    )


_HwAccessAcctMethod_Type.__name__ = "Integer32"
_HwAccessAcctMethod_Object = MibTableColumn
hwAccessAcctMethod = _HwAccessAcctMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 14),
    _HwAccessAcctMethod_Type()
)
hwAccessAcctMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessAcctMethod.setStatus("current")
_HwAccessIPAddress_Type = IpAddress
_HwAccessIPAddress_Object = MibTableColumn
hwAccessIPAddress = _HwAccessIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 15),
    _HwAccessIPAddress_Type()
)
hwAccessIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPAddress.setStatus("current")


class _HwAccessVRF_Type(DisplayString):
    """Custom type hwAccessVRF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwAccessVRF_Type.__name__ = "DisplayString"
_HwAccessVRF_Object = MibTableColumn
hwAccessVRF = _HwAccessVRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 16),
    _HwAccessVRF_Type()
)
hwAccessVRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessVRF.setStatus("current")
_HwAccessMACAddress_Type = MacAddress
_HwAccessMACAddress_Object = MibTableColumn
hwAccessMACAddress = _HwAccessMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 17),
    _HwAccessMACAddress_Type()
)
hwAccessMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessMACAddress.setStatus("current")
_HwAccessIfIdleCut_Type = TruthValue
_HwAccessIfIdleCut_Object = MibTableColumn
hwAccessIfIdleCut = _HwAccessIfIdleCut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 18),
    _HwAccessIfIdleCut_Type()
)
hwAccessIfIdleCut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIfIdleCut.setStatus("current")
_HwAccessIdleCutTime_Type = Integer32
_HwAccessIdleCutTime_Object = MibTableColumn
hwAccessIdleCutTime = _HwAccessIdleCutTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 19),
    _HwAccessIdleCutTime_Type()
)
hwAccessIdleCutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIdleCutTime.setStatus("current")
_HwAccessIdleCutFlow_Type = Integer32
_HwAccessIdleCutFlow_Object = MibTableColumn
hwAccessIdleCutFlow = _HwAccessIdleCutFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 20),
    _HwAccessIdleCutFlow_Type()
)
hwAccessIdleCutFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIdleCutFlow.setStatus("current")
_HwAccessTimeLimit_Type = Integer32
_HwAccessTimeLimit_Object = MibTableColumn
hwAccessTimeLimit = _HwAccessTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 21),
    _HwAccessTimeLimit_Type()
)
hwAccessTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessTimeLimit.setStatus("current")
_HwAccessTotalFlow64Limit_Type = Counter64
_HwAccessTotalFlow64Limit_Object = MibTableColumn
hwAccessTotalFlow64Limit = _HwAccessTotalFlow64Limit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 22),
    _HwAccessTotalFlow64Limit_Type()
)
hwAccessTotalFlow64Limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessTotalFlow64Limit.setStatus("current")
_HwAccessStartTime_Type = DateAndTime
_HwAccessStartTime_Object = MibTableColumn
hwAccessStartTime = _HwAccessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 25),
    _HwAccessStartTime_Type()
)
hwAccessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessStartTime.setStatus("current")
_HwAccessCARIfUpActive_Type = TruthValue
_HwAccessCARIfUpActive_Object = MibTableColumn
hwAccessCARIfUpActive = _HwAccessCARIfUpActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 27),
    _HwAccessCARIfUpActive_Type()
)
hwAccessCARIfUpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARIfUpActive.setStatus("current")
_HwAccessCARIfDnActive_Type = TruthValue
_HwAccessCARIfDnActive_Object = MibTableColumn
hwAccessCARIfDnActive = _HwAccessCARIfDnActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 31),
    _HwAccessCARIfDnActive_Type()
)
hwAccessCARIfDnActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARIfDnActive.setStatus("current")
_HwAccessUpFlow64_Type = Counter64
_HwAccessUpFlow64_Object = MibTableColumn
hwAccessUpFlow64 = _HwAccessUpFlow64_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 36),
    _HwAccessUpFlow64_Type()
)
hwAccessUpFlow64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessUpFlow64.setStatus("current")
_HwAccessDnFlow64_Type = Counter64
_HwAccessDnFlow64_Object = MibTableColumn
hwAccessDnFlow64 = _HwAccessDnFlow64_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 37),
    _HwAccessDnFlow64_Type()
)
hwAccessDnFlow64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessDnFlow64.setStatus("current")
_HwAccessUpPacket64_Type = Counter64
_HwAccessUpPacket64_Object = MibTableColumn
hwAccessUpPacket64 = _HwAccessUpPacket64_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 38),
    _HwAccessUpPacket64_Type()
)
hwAccessUpPacket64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessUpPacket64.setStatus("current")
_HwAccessDnPacket64_Type = Counter64
_HwAccessDnPacket64_Object = MibTableColumn
hwAccessDnPacket64 = _HwAccessDnPacket64_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 39),
    _HwAccessDnPacket64_Type()
)
hwAccessDnPacket64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessDnPacket64.setStatus("current")


class _HwAccessCARUpCIR_Type(Integer32):
    """Custom type hwAccessCARUpCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 10000000),
    )


_HwAccessCARUpCIR_Type.__name__ = "Integer32"
_HwAccessCARUpCIR_Object = MibTableColumn
hwAccessCARUpCIR = _HwAccessCARUpCIR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 45),
    _HwAccessCARUpCIR_Type()
)
hwAccessCARUpCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARUpCIR.setStatus("current")


class _HwAccessCARUpPIR_Type(Integer32):
    """Custom type hwAccessCARUpPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 10000000),
    )


_HwAccessCARUpPIR_Type.__name__ = "Integer32"
_HwAccessCARUpPIR_Object = MibTableColumn
hwAccessCARUpPIR = _HwAccessCARUpPIR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 46),
    _HwAccessCARUpPIR_Type()
)
hwAccessCARUpPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARUpPIR.setStatus("current")


class _HwAccessCARUpCBS_Type(Unsigned32):
    """Custom type hwAccessCARUpCBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_HwAccessCARUpCBS_Type.__name__ = "Unsigned32"
_HwAccessCARUpCBS_Object = MibTableColumn
hwAccessCARUpCBS = _HwAccessCARUpCBS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 47),
    _HwAccessCARUpCBS_Type()
)
hwAccessCARUpCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARUpCBS.setStatus("current")


class _HwAccessCARUpPBS_Type(Unsigned32):
    """Custom type hwAccessCARUpPBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwAccessCARUpPBS_Type.__name__ = "Unsigned32"
_HwAccessCARUpPBS_Object = MibTableColumn
hwAccessCARUpPBS = _HwAccessCARUpPBS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 48),
    _HwAccessCARUpPBS_Type()
)
hwAccessCARUpPBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARUpPBS.setStatus("current")


class _HwAccessCARDnCIR_Type(Integer32):
    """Custom type hwAccessCARDnCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 10000000),
    )


_HwAccessCARDnCIR_Type.__name__ = "Integer32"
_HwAccessCARDnCIR_Object = MibTableColumn
hwAccessCARDnCIR = _HwAccessCARDnCIR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 49),
    _HwAccessCARDnCIR_Type()
)
hwAccessCARDnCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARDnCIR.setStatus("current")


class _HwAccessCARDnPIR_Type(Integer32):
    """Custom type hwAccessCARDnPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 10000000),
    )


_HwAccessCARDnPIR_Type.__name__ = "Integer32"
_HwAccessCARDnPIR_Object = MibTableColumn
hwAccessCARDnPIR = _HwAccessCARDnPIR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 50),
    _HwAccessCARDnPIR_Type()
)
hwAccessCARDnPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARDnPIR.setStatus("current")


class _HwAccessCARDnCBS_Type(Unsigned32):
    """Custom type hwAccessCARDnCBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_HwAccessCARDnCBS_Type.__name__ = "Unsigned32"
_HwAccessCARDnCBS_Object = MibTableColumn
hwAccessCARDnCBS = _HwAccessCARDnCBS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 51),
    _HwAccessCARDnCBS_Type()
)
hwAccessCARDnCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARDnCBS.setStatus("current")


class _HwAccessCARDnPBS_Type(Unsigned32):
    """Custom type hwAccessCARDnPBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwAccessCARDnPBS_Type.__name__ = "Unsigned32"
_HwAccessCARDnPBS_Object = MibTableColumn
hwAccessCARDnPBS = _HwAccessCARDnPBS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 52),
    _HwAccessCARDnPBS_Type()
)
hwAccessCARDnPBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCARDnPBS.setStatus("current")


class _HwAccessDownPriority_Type(Integer32):
    """Custom type hwAccessDownPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HwAccessDownPriority_Type.__name__ = "Integer32"
_HwAccessDownPriority_Object = MibTableColumn
hwAccessDownPriority = _HwAccessDownPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 53),
    _HwAccessDownPriority_Type()
)
hwAccessDownPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessDownPriority.setStatus("current")


class _HwAccessQosProfile_Type(DisplayString):
    """Custom type hwAccessQosProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwAccessQosProfile_Type.__name__ = "DisplayString"
_HwAccessQosProfile_Object = MibTableColumn
hwAccessQosProfile = _HwAccessQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 56),
    _HwAccessQosProfile_Type()
)
hwAccessQosProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAccessQosProfile.setStatus("current")


class _HwAccessInterface_Type(DisplayString):
    """Custom type hwAccessInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwAccessInterface_Type.__name__ = "DisplayString"
_HwAccessInterface_Object = MibTableColumn
hwAccessInterface = _HwAccessInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 57),
    _HwAccessInterface_Type()
)
hwAccessInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessInterface.setStatus("current")
_HwAccessIPv6IFID_Type = Ipv6AddressIfIdentifier
_HwAccessIPv6IFID_Object = MibTableColumn
hwAccessIPv6IFID = _HwAccessIPv6IFID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 58),
    _HwAccessIPv6IFID_Type()
)
hwAccessIPv6IFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6IFID.setStatus("current")
_HwAccessIPv6WanAddress_Type = Ipv6Address
_HwAccessIPv6WanAddress_Object = MibTableColumn
hwAccessIPv6WanAddress = _HwAccessIPv6WanAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 59),
    _HwAccessIPv6WanAddress_Type()
)
hwAccessIPv6WanAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6WanAddress.setStatus("current")
_HwAccessIPv6WanPrefix_Type = Ipv6AddressPrefix
_HwAccessIPv6WanPrefix_Object = MibTableColumn
hwAccessIPv6WanPrefix = _HwAccessIPv6WanPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 60),
    _HwAccessIPv6WanPrefix_Type()
)
hwAccessIPv6WanPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6WanPrefix.setStatus("current")
_HwAccessIPv6LanPrefix_Type = Ipv6AddressPrefix
_HwAccessIPv6LanPrefix_Object = MibTableColumn
hwAccessIPv6LanPrefix = _HwAccessIPv6LanPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 61),
    _HwAccessIPv6LanPrefix_Type()
)
hwAccessIPv6LanPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6LanPrefix.setStatus("current")


class _HwAccessIPv6LanPrefixLen_Type(Integer32):
    """Custom type hwAccessIPv6LanPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwAccessIPv6LanPrefixLen_Type.__name__ = "Integer32"
_HwAccessIPv6LanPrefixLen_Object = MibTableColumn
hwAccessIPv6LanPrefixLen = _HwAccessIPv6LanPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 62),
    _HwAccessIPv6LanPrefixLen_Type()
)
hwAccessIPv6LanPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6LanPrefixLen.setStatus("current")


class _HwAccessBasicIPType_Type(DisplayString):
    """Custom type hwAccessBasicIPType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_HwAccessBasicIPType_Type.__name__ = "DisplayString"
_HwAccessBasicIPType_Object = MibTableColumn
hwAccessBasicIPType = _HwAccessBasicIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 63),
    _HwAccessBasicIPType_Type()
)
hwAccessBasicIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessBasicIPType.setStatus("current")


class _HwAccessIPv6WaitDelay_Type(Integer32):
    """Custom type hwAccessIPv6WaitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_HwAccessIPv6WaitDelay_Type.__name__ = "Integer32"
_HwAccessIPv6WaitDelay_Object = MibTableColumn
hwAccessIPv6WaitDelay = _HwAccessIPv6WaitDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 64),
    _HwAccessIPv6WaitDelay_Type()
)
hwAccessIPv6WaitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6WaitDelay.setStatus("current")


class _HwAccessIPv6ManagedAddressFlag_Type(Integer32):
    """Custom type hwAccessIPv6ManagedAddressFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv6", 2),
          ("ndra", 1))
    )


_HwAccessIPv6ManagedAddressFlag_Type.__name__ = "Integer32"
_HwAccessIPv6ManagedAddressFlag_Object = MibTableColumn
hwAccessIPv6ManagedAddressFlag = _HwAccessIPv6ManagedAddressFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 65),
    _HwAccessIPv6ManagedAddressFlag_Type()
)
hwAccessIPv6ManagedAddressFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6ManagedAddressFlag.setStatus("current")
_HwAccessIPv6CPIFIDAvailable_Type = TruthValue
_HwAccessIPv6CPIFIDAvailable_Object = MibTableColumn
hwAccessIPv6CPIFIDAvailable = _HwAccessIPv6CPIFIDAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 66),
    _HwAccessIPv6CPIFIDAvailable_Type()
)
hwAccessIPv6CPIFIDAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6CPIFIDAvailable.setStatus("current")


class _HwAccessIPv6OtherFlag_Type(Integer32):
    """Custom type hwAccessIPv6OtherFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv6", 2),
          ("ndra", 1))
    )


_HwAccessIPv6OtherFlag_Type.__name__ = "Integer32"
_HwAccessIPv6OtherFlag_Object = MibTableColumn
hwAccessIPv6OtherFlag = _HwAccessIPv6OtherFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 67),
    _HwAccessIPv6OtherFlag_Type()
)
hwAccessIPv6OtherFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6OtherFlag.setStatus("current")
_HwAccessIPv6CPAssignIFID_Type = TruthValue
_HwAccessIPv6CPAssignIFID_Object = MibTableColumn
hwAccessIPv6CPAssignIFID = _HwAccessIPv6CPAssignIFID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 68),
    _HwAccessIPv6CPAssignIFID_Type()
)
hwAccessIPv6CPAssignIFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6CPAssignIFID.setStatus("current")


class _HwAccessLineID_Type(DisplayString):
    """Custom type hwAccessLineID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwAccessLineID_Type.__name__ = "DisplayString"
_HwAccessLineID_Object = MibTableColumn
hwAccessLineID = _HwAccessLineID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 69),
    _HwAccessLineID_Type()
)
hwAccessLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessLineID.setStatus("current")
_HwAccessIPv6UpFlow64_Type = Counter64
_HwAccessIPv6UpFlow64_Object = MibTableColumn
hwAccessIPv6UpFlow64 = _HwAccessIPv6UpFlow64_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 70),
    _HwAccessIPv6UpFlow64_Type()
)
hwAccessIPv6UpFlow64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6UpFlow64.setStatus("current")
_HwAccessIPv6DnFlow64_Type = Counter64
_HwAccessIPv6DnFlow64_Object = MibTableColumn
hwAccessIPv6DnFlow64 = _HwAccessIPv6DnFlow64_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 71),
    _HwAccessIPv6DnFlow64_Type()
)
hwAccessIPv6DnFlow64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6DnFlow64.setStatus("current")
_HwAccessIPv6UpPacket64_Type = Counter64
_HwAccessIPv6UpPacket64_Object = MibTableColumn
hwAccessIPv6UpPacket64 = _HwAccessIPv6UpPacket64_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 72),
    _HwAccessIPv6UpPacket64_Type()
)
hwAccessIPv6UpPacket64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6UpPacket64.setStatus("current")
_HwAccessIPv6DnPacket64_Type = Counter64
_HwAccessIPv6DnPacket64_Object = MibTableColumn
hwAccessIPv6DnPacket64 = _HwAccessIPv6DnPacket64_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 73),
    _HwAccessIPv6DnPacket64_Type()
)
hwAccessIPv6DnPacket64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessIPv6DnPacket64.setStatus("current")


class _HwAccessDeviceName_Type(DisplayString):
    """Custom type hwAccessDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwAccessDeviceName_Type.__name__ = "DisplayString"
_HwAccessDeviceName_Object = MibTableColumn
hwAccessDeviceName = _HwAccessDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 74),
    _HwAccessDeviceName_Type()
)
hwAccessDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessDeviceName.setStatus("current")
_HwAccessDeviceMACAddress_Type = MacAddress
_HwAccessDeviceMACAddress_Object = MibTableColumn
hwAccessDeviceMACAddress = _HwAccessDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 75),
    _HwAccessDeviceMACAddress_Type()
)
hwAccessDeviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessDeviceMACAddress.setStatus("current")
_HwAccessDevicePortName_Type = OctetString
_HwAccessDevicePortName_Object = MibTableColumn
hwAccessDevicePortName = _HwAccessDevicePortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 76),
    _HwAccessDevicePortName_Type()
)
hwAccessDevicePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessDevicePortName.setStatus("current")


class _HwAccessAPID_Type(Unsigned32):
    """Custom type hwAccessAPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294836225),
    )


_HwAccessAPID_Type.__name__ = "Unsigned32"
_HwAccessAPID_Object = MibTableColumn
hwAccessAPID = _HwAccessAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 15, 1, 77),
    _HwAccessAPID_Type()
)
hwAccessAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessAPID.setStatus("current")
_HwAccessExtTable_Object = MibTable
hwAccessExtTable = _HwAccessExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16)
)
if mibBuilder.loadTexts:
    hwAccessExtTable.setStatus("current")
_HwAccessExtEntry_Object = MibTableRow
hwAccessExtEntry = _HwAccessExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1)
)
hwAccessExtEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAccessIndex"),
)
if mibBuilder.loadTexts:
    hwAccessExtEntry.setStatus("current")


class _HwAccessUCLGroup_Type(Integer32):
    """Custom type hwAccessUCLGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
        ValueRangeConstraint(65535, 65535),
    )


_HwAccessUCLGroup_Type.__name__ = "Integer32"
_HwAccessUCLGroup_Object = MibTableColumn
hwAccessUCLGroup = _HwAccessUCLGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 2),
    _HwAccessUCLGroup_Type()
)
hwAccessUCLGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessUCLGroup.setStatus("current")


class _HwAuthenticationState_Type(Integer32):
    """Custom type hwAuthenticationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwAuthenticationState_Type.__name__ = "Integer32"
_HwAuthenticationState_Object = MibTableColumn
hwAuthenticationState = _HwAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 4),
    _HwAuthenticationState_Type()
)
hwAuthenticationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthenticationState.setStatus("current")


class _HwAuthorizationState_Type(Integer32):
    """Custom type hwAuthorizationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwAuthorizationState_Type.__name__ = "Integer32"
_HwAuthorizationState_Object = MibTableColumn
hwAuthorizationState = _HwAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 5),
    _HwAuthorizationState_Type()
)
hwAuthorizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthorizationState.setStatus("current")


class _HwAccountingState_Type(Integer32):
    """Custom type hwAccountingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HwAccountingState_Type.__name__ = "Integer32"
_HwAccountingState_Object = MibTableColumn
hwAccountingState = _HwAccountingState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 6),
    _HwAccountingState_Type()
)
hwAccountingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccountingState.setStatus("current")


class _HwAccessDomainName_Type(DisplayString):
    """Custom type hwAccessDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwAccessDomainName_Type.__name__ = "DisplayString"
_HwAccessDomainName_Object = MibTableColumn
hwAccessDomainName = _HwAccessDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 7),
    _HwAccessDomainName_Type()
)
hwAccessDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessDomainName.setStatus("current")


class _HwIdleTimeLength_Type(Integer32):
    """Custom type hwIdleTimeLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HwIdleTimeLength_Type.__name__ = "Integer32"
_HwIdleTimeLength_Object = MibTableColumn
hwIdleTimeLength = _HwIdleTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 8),
    _HwIdleTimeLength_Type()
)
hwIdleTimeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIdleTimeLength.setStatus("current")


class _HwAcctSessionID_Type(DisplayString):
    """Custom type hwAcctSessionID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_HwAcctSessionID_Type.__name__ = "DisplayString"
_HwAcctSessionID_Object = MibTableColumn
hwAcctSessionID = _HwAcctSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 9),
    _HwAcctSessionID_Type()
)
hwAcctSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcctSessionID.setStatus("current")
_HwAccessStartAcctTime_Type = DateAndTime
_HwAccessStartAcctTime_Object = MibTableColumn
hwAccessStartAcctTime = _HwAccessStartAcctTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 10),
    _HwAccessStartAcctTime_Type()
)
hwAccessStartAcctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessStartAcctTime.setStatus("current")


class _HwAccessNormalServerGroup_Type(DisplayString):
    """Custom type hwAccessNormalServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwAccessNormalServerGroup_Type.__name__ = "DisplayString"
_HwAccessNormalServerGroup_Object = MibTableColumn
hwAccessNormalServerGroup = _HwAccessNormalServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 11),
    _HwAccessNormalServerGroup_Type()
)
hwAccessNormalServerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessNormalServerGroup.setStatus("current")


class _HwAccessDomainAcctCopySeverGroup_Type(DisplayString):
    """Custom type hwAccessDomainAcctCopySeverGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwAccessDomainAcctCopySeverGroup_Type.__name__ = "DisplayString"
_HwAccessDomainAcctCopySeverGroup_Object = MibTableColumn
hwAccessDomainAcctCopySeverGroup = _HwAccessDomainAcctCopySeverGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 12),
    _HwAccessDomainAcctCopySeverGroup_Type()
)
hwAccessDomainAcctCopySeverGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessDomainAcctCopySeverGroup.setStatus("current")


class _HwAccessPVlanAcctCopyServerGroup_Type(DisplayString):
    """Custom type hwAccessPVlanAcctCopyServerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwAccessPVlanAcctCopyServerGroup_Type.__name__ = "DisplayString"
_HwAccessPVlanAcctCopyServerGroup_Object = MibTableColumn
hwAccessPVlanAcctCopyServerGroup = _HwAccessPVlanAcctCopyServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 13),
    _HwAccessPVlanAcctCopyServerGroup_Type()
)
hwAccessPVlanAcctCopyServerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessPVlanAcctCopyServerGroup.setStatus("current")


class _HwAccessCurAuthenPlace_Type(Integer32):
    """Custom type hwAccessCurAuthenPlace based on Integer32"""
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
        *(("local", 1),
          ("none", 0),
          ("radius", 2),
          ("tacacs", 3))
    )


_HwAccessCurAuthenPlace_Type.__name__ = "Integer32"
_HwAccessCurAuthenPlace_Object = MibTableColumn
hwAccessCurAuthenPlace = _HwAccessCurAuthenPlace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 14),
    _HwAccessCurAuthenPlace_Type()
)
hwAccessCurAuthenPlace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCurAuthenPlace.setStatus("current")


class _HwAccessActionFlag_Type(Integer32):
    """Custom type hwAccessActionFlag based on Integer32"""
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
        *(("authmodify", 5),
          ("connectup", 6),
          ("idle", 0),
          ("leaving", 4),
          ("logout", 3),
          ("newuserauth", 1),
          ("reauth", 2))
    )


_HwAccessActionFlag_Type.__name__ = "Integer32"
_HwAccessActionFlag_Object = MibTableColumn
hwAccessActionFlag = _HwAccessActionFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 15),
    _HwAccessActionFlag_Type()
)
hwAccessActionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessActionFlag.setStatus("current")


class _HwAccessAuthtype_Type(Integer32):
    """Custom type hwAccessAuthtype based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("admin", 7),
          ("bind", 4),
          ("dot1x", 2),
          ("fast", 5),
          ("none", 0),
          ("ppp", 1),
          ("tunnel", 8),
          ("web", 3),
          ("wlan", 6))
    )


_HwAccessAuthtype_Type.__name__ = "Integer32"
_HwAccessAuthtype_Object = MibTableColumn
hwAccessAuthtype = _HwAccessAuthtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 16),
    _HwAccessAuthtype_Type()
)
hwAccessAuthtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessAuthtype.setStatus("current")


class _HwAccessType_Type(Integer32):
    """Custom type hwAccessType based on Integer32"""
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
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("deviceuser", 28),
          ("e1pos", 24),
          ("eap", 13),
          ("ftp", 4),
          ("http", 32),
          ("ip", 15),
          ("lactunnel", 25),
          ("layer2leasedline", 17),
          ("layer2leasedlineuser", 18),
          ("layer3leasedline", 19),
          ("lnstunnel", 26),
          ("mac", 35),
          ("mip", 27),
          ("nmsleasedline", 21),
          ("ordinaryvlan", 12),
          ("ordinaryvlanor", 31),
          ("pnp", 14),
          ("ppp", 6),
          ("pppoa", 9),
          ("pppoe", 7),
          ("pppoeleasedline", 20),
          ("pppoeoa", 10),
          ("pppoeor", 29),
          ("pppoeovlan", 8),
          ("pppoeovlanor", 30),
          ("pppolns", 11),
          ("proxyleasedline", 22),
          ("relayleasedline", 23),
          ("ssh", 3),
          ("staticvlan", 16),
          ("telnet", 1),
          ("terminal", 2),
          ("vm", 36),
          ("web", 33),
          ("wlan", 34),
          ("x25pad", 5))
    )


_HwAccessType_Type.__name__ = "Integer32"
_HwAccessType_Object = MibTableColumn
hwAccessType = _HwAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 17),
    _HwAccessType_Type()
)
hwAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessType.setStatus("current")


class _HwAccessOnlineTime_Type(Unsigned32):
    """Custom type hwAccessOnlineTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwAccessOnlineTime_Type.__name__ = "Unsigned32"
_HwAccessOnlineTime_Object = MibTableColumn
hwAccessOnlineTime = _HwAccessOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 18),
    _HwAccessOnlineTime_Type()
)
hwAccessOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessOnlineTime.setStatus("current")


class _HwAccessDomain_Type(DisplayString):
    """Custom type hwAccessDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwAccessDomain_Type.__name__ = "DisplayString"
_HwAccessDomain_Object = MibTableColumn
hwAccessDomain = _HwAccessDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 19),
    _HwAccessDomain_Type()
)
hwAccessDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccessDomain.setStatus("current")
_HwAccessGateway_Type = IpAddress
_HwAccessGateway_Object = MibTableColumn
hwAccessGateway = _HwAccessGateway_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 20),
    _HwAccessGateway_Type()
)
hwAccessGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessGateway.setStatus("current")


class _HwAccessSSID_Type(DisplayString):
    """Custom type hwAccessSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwAccessSSID_Type.__name__ = "DisplayString"
_HwAccessSSID_Object = MibTableColumn
hwAccessSSID = _HwAccessSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 21),
    _HwAccessSSID_Type()
)
hwAccessSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccessSSID.setStatus("current")
_HwAccessAPMAC_Type = MacAddress
_HwAccessAPMAC_Object = MibTableColumn
hwAccessAPMAC = _HwAccessAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 22),
    _HwAccessAPMAC_Type()
)
hwAccessAPMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessAPMAC.setStatus("current")


class _HwAccessCurAccountingPlace_Type(Integer32):
    """Custom type hwAccessCurAccountingPlace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("radius", 2),
          ("tacacs", 3))
    )


_HwAccessCurAccountingPlace_Type.__name__ = "Integer32"
_HwAccessCurAccountingPlace_Object = MibTableColumn
hwAccessCurAccountingPlace = _HwAccessCurAccountingPlace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 23),
    _HwAccessCurAccountingPlace_Type()
)
hwAccessCurAccountingPlace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCurAccountingPlace.setStatus("current")


class _HwAccessCurAuthorPlace_Type(Integer32):
    """Custom type hwAccessCurAuthorPlace based on Integer32"""
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
        *(("ifauthen", 3),
          ("local", 2),
          ("none", 1),
          ("tacacs", 4))
    )


_HwAccessCurAuthorPlace_Type.__name__ = "Integer32"
_HwAccessCurAuthorPlace_Object = MibTableColumn
hwAccessCurAuthorPlace = _HwAccessCurAuthorPlace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 24),
    _HwAccessCurAuthorPlace_Type()
)
hwAccessCurAuthorPlace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessCurAuthorPlace.setStatus("current")


class _HwAccessUserGroup_Type(DisplayString):
    """Custom type hwAccessUserGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwAccessUserGroup_Type.__name__ = "DisplayString"
_HwAccessUserGroup_Object = MibTableColumn
hwAccessUserGroup = _HwAccessUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 25),
    _HwAccessUserGroup_Type()
)
hwAccessUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccessUserGroup.setStatus("current")


class _HwAccessResourceInsufficientInbound_Type(Integer32):
    """Custom type hwAccessResourceInsufficientInbound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwAccessResourceInsufficientInbound_Type.__name__ = "Integer32"
_HwAccessResourceInsufficientInbound_Object = MibTableColumn
hwAccessResourceInsufficientInbound = _HwAccessResourceInsufficientInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 26),
    _HwAccessResourceInsufficientInbound_Type()
)
hwAccessResourceInsufficientInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessResourceInsufficientInbound.setStatus("current")


class _HwAccessResourceInsufficientOutbound_Type(Integer32):
    """Custom type hwAccessResourceInsufficientOutbound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwAccessResourceInsufficientOutbound_Type.__name__ = "Integer32"
_HwAccessResourceInsufficientOutbound_Object = MibTableColumn
hwAccessResourceInsufficientOutbound = _HwAccessResourceInsufficientOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 16, 1, 27),
    _HwAccessResourceInsufficientOutbound_Type()
)
hwAccessResourceInsufficientOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessResourceInsufficientOutbound.setStatus("current")
_HwAcctSchemeExtTable_Object = MibTable
hwAcctSchemeExtTable = _HwAcctSchemeExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 19)
)
if mibBuilder.loadTexts:
    hwAcctSchemeExtTable.setStatus("current")
_HwAcctSchemeExtEntry_Object = MibTableRow
hwAcctSchemeExtEntry = _HwAcctSchemeExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 19, 1)
)
hwAcctSchemeExtEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAcctSchemeName"),
)
if mibBuilder.loadTexts:
    hwAcctSchemeExtEntry.setStatus("current")


class _HwIfRealtimeAcct_Type(TruthValue):
    """Custom type hwIfRealtimeAcct based on TruthValue"""


_HwIfRealtimeAcct_Object = MibTableColumn
hwIfRealtimeAcct = _HwIfRealtimeAcct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 19, 1, 1),
    _HwIfRealtimeAcct_Type()
)
hwIfRealtimeAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfRealtimeAcct.setStatus("current")


class _HwRealtimeFailMaxnum_Type(Integer32):
    """Custom type hwRealtimeFailMaxnum based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwRealtimeFailMaxnum_Type.__name__ = "Integer32"
_HwRealtimeFailMaxnum_Object = MibTableColumn
hwRealtimeFailMaxnum = _HwRealtimeFailMaxnum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 19, 1, 2),
    _HwRealtimeFailMaxnum_Type()
)
hwRealtimeFailMaxnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRealtimeFailMaxnum.setStatus("current")


class _HwStartFailOnlineIfSendInterim_Type(TruthValue):
    """Custom type hwStartFailOnlineIfSendInterim based on TruthValue"""


_HwStartFailOnlineIfSendInterim_Object = MibTableColumn
hwStartFailOnlineIfSendInterim = _HwStartFailOnlineIfSendInterim_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 19, 1, 4),
    _HwStartFailOnlineIfSendInterim_Type()
)
hwStartFailOnlineIfSendInterim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStartFailOnlineIfSendInterim.setStatus("current")
_HwBillPoolTable_ObjectIdentity = ObjectIdentity
hwBillPoolTable = _HwBillPoolTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 21)
)
_HwBillsPoolVolume_Type = Integer32
_HwBillsPoolVolume_Object = MibScalar
hwBillsPoolVolume = _HwBillsPoolVolume_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 21, 1),
    _HwBillsPoolVolume_Type()
)
hwBillsPoolVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBillsPoolVolume.setStatus("current")
_HwBillsPoolNum_Type = Integer32
_HwBillsPoolNum_Object = MibScalar
hwBillsPoolNum = _HwBillsPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 21, 2),
    _HwBillsPoolNum_Type()
)
hwBillsPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBillsPoolNum.setStatus("current")


class _HwBillsPoolAlarmThreshold_Type(Integer32):
    """Custom type hwBillsPoolAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_HwBillsPoolAlarmThreshold_Type.__name__ = "Integer32"
_HwBillsPoolAlarmThreshold_Object = MibScalar
hwBillsPoolAlarmThreshold = _HwBillsPoolAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 21, 3),
    _HwBillsPoolAlarmThreshold_Type()
)
hwBillsPoolAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBillsPoolAlarmThreshold.setStatus("current")


class _HwBillsPoolBackupMode_Type(Integer32):
    """Custom type hwBillsPoolBackupMode based on Integer32"""
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
        *(("cfcardmode", 4),
          ("hdmode", 3),
          ("nobackup", 1),
          ("tftpmode", 2))
    )


_HwBillsPoolBackupMode_Type.__name__ = "Integer32"
_HwBillsPoolBackupMode_Object = MibScalar
hwBillsPoolBackupMode = _HwBillsPoolBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 21, 4),
    _HwBillsPoolBackupMode_Type()
)
hwBillsPoolBackupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBillsPoolBackupMode.setStatus("current")


class _HwBillsPoolBackupInterval_Type(Integer32):
    """Custom type hwBillsPoolBackupInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBillsPoolBackupInterval_Type.__name__ = "Integer32"
_HwBillsPoolBackupInterval_Object = MibScalar
hwBillsPoolBackupInterval = _HwBillsPoolBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 21, 5),
    _HwBillsPoolBackupInterval_Type()
)
hwBillsPoolBackupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBillsPoolBackupInterval.setStatus("current")


class _HwBillsPoolBackupNow_Type(Integer32):
    """Custom type hwBillsPoolBackupNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwBillsPoolBackupNow_Type.__name__ = "Integer32"
_HwBillsPoolBackupNow_Object = MibScalar
hwBillsPoolBackupNow = _HwBillsPoolBackupNow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 21, 6),
    _HwBillsPoolBackupNow_Type()
)
hwBillsPoolBackupNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBillsPoolBackupNow.setStatus("current")


class _HwBillsPoolReset_Type(Integer32):
    """Custom type hwBillsPoolReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwBillsPoolReset_Type.__name__ = "Integer32"
_HwBillsPoolReset_Object = MibScalar
hwBillsPoolReset = _HwBillsPoolReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 21, 7),
    _HwBillsPoolReset_Type()
)
hwBillsPoolReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBillsPoolReset.setStatus("current")
_HwBillTFTPTable_ObjectIdentity = ObjectIdentity
hwBillTFTPTable = _HwBillTFTPTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 22)
)
_HwBillsTFTPSrvIP_Type = IpAddress
_HwBillsTFTPSrvIP_Object = MibScalar
hwBillsTFTPSrvIP = _HwBillsTFTPSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 22, 1),
    _HwBillsTFTPSrvIP_Type()
)
hwBillsTFTPSrvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBillsTFTPSrvIP.setStatus("current")


class _HwBillsTFTPMainFileName_Type(DisplayString):
    """Custom type hwBillsTFTPMainFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HwBillsTFTPMainFileName_Type.__name__ = "DisplayString"
_HwBillsTFTPMainFileName_Object = MibScalar
hwBillsTFTPMainFileName = _HwBillsTFTPMainFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 22, 2),
    _HwBillsTFTPMainFileName_Type()
)
hwBillsTFTPMainFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBillsTFTPMainFileName.setStatus("current")
_HwUclGrpTable_Object = MibTable
hwUclGrpTable = _HwUclGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 25)
)
if mibBuilder.loadTexts:
    hwUclGrpTable.setStatus("current")
_HwUclGrpEntry_Object = MibTableRow
hwUclGrpEntry = _HwUclGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 25, 1)
)
hwUclGrpEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwUclGrpName"),
)
if mibBuilder.loadTexts:
    hwUclGrpEntry.setStatus("current")


class _HwUclGrpName_Type(DisplayString):
    """Custom type hwUclGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwUclGrpName_Type.__name__ = "DisplayString"
_HwUclGrpName_Object = MibTableColumn
hwUclGrpName = _HwUclGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 25, 1, 1),
    _HwUclGrpName_Type()
)
hwUclGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUclGrpName.setStatus("current")
_HwUclGrpRowStatus_Type = RowStatus
_HwUclGrpRowStatus_Object = MibTableColumn
hwUclGrpRowStatus = _HwUclGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 25, 1, 2),
    _HwUclGrpRowStatus_Type()
)
hwUclGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUclGrpRowStatus.setStatus("current")
_HwIPAccessTable_Object = MibTable
hwIPAccessTable = _HwIPAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 27)
)
if mibBuilder.loadTexts:
    hwIPAccessTable.setStatus("current")
_HwIPAccessEntry_Object = MibTableRow
hwIPAccessEntry = _HwIPAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 27, 1)
)
hwIPAccessEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwIPAccessIPaddress"),
    (0, "HUAWEI-AAA-MIB", "hwIPAccessVRF"),
)
if mibBuilder.loadTexts:
    hwIPAccessEntry.setStatus("current")
_HwIPAccessIPaddress_Type = IpAddress
_HwIPAccessIPaddress_Object = MibTableColumn
hwIPAccessIPaddress = _HwIPAccessIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 27, 1, 1),
    _HwIPAccessIPaddress_Type()
)
hwIPAccessIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPAccessIPaddress.setStatus("current")
_HwIPAccessCID_Type = Integer32
_HwIPAccessCID_Object = MibTableColumn
hwIPAccessCID = _HwIPAccessCID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 27, 1, 2),
    _HwIPAccessCID_Type()
)
hwIPAccessCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPAccessCID.setStatus("current")


class _HwIPAccessVRF_Type(DisplayString):
    """Custom type hwIPAccessVRF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPAccessVRF_Type.__name__ = "DisplayString"
_HwIPAccessVRF_Object = MibTableColumn
hwIPAccessVRF = _HwIPAccessVRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 27, 1, 3),
    _HwIPAccessVRF_Type()
)
hwIPAccessVRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPAccessVRF.setStatus("current")
_HwCutAccessUserTable_ObjectIdentity = ObjectIdentity
hwCutAccessUserTable = _HwCutAccessUserTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28)
)
_HwCutStartUserID_Type = Integer32
_HwCutStartUserID_Object = MibScalar
hwCutStartUserID = _HwCutStartUserID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 1),
    _HwCutStartUserID_Type()
)
hwCutStartUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutStartUserID.setStatus("current")
_HwCutEndUserID_Type = Integer32
_HwCutEndUserID_Object = MibScalar
hwCutEndUserID = _HwCutEndUserID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 2),
    _HwCutEndUserID_Type()
)
hwCutEndUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutEndUserID.setStatus("current")
_HwCutIPaddress_Type = IpAddress
_HwCutIPaddress_Object = MibScalar
hwCutIPaddress = _HwCutIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 3),
    _HwCutIPaddress_Type()
)
hwCutIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutIPaddress.setStatus("current")
_HwCutMacAddres_Type = MacAddress
_HwCutMacAddres_Object = MibScalar
hwCutMacAddres = _HwCutMacAddres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 4),
    _HwCutMacAddres_Type()
)
hwCutMacAddres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutMacAddres.setStatus("current")


class _HwCutUserName_Type(DisplayString):
    """Custom type hwCutUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_HwCutUserName_Type.__name__ = "DisplayString"
_HwCutUserName_Object = MibScalar
hwCutUserName = _HwCutUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 5),
    _HwCutUserName_Type()
)
hwCutUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutUserName.setStatus("current")


class _HwCutUserAttri_Type(Integer32):
    """Custom type hwCutUserAttri based on Integer32"""
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
        *(("all", 0),
          ("hwtacacs", 4),
          ("local", 2),
          ("noauth", 1),
          ("radiusauth", 3))
    )


_HwCutUserAttri_Type.__name__ = "Integer32"
_HwCutUserAttri_Object = MibScalar
hwCutUserAttri = _HwCutUserAttri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 6),
    _HwCutUserAttri_Type()
)
hwCutUserAttri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutUserAttri.setStatus("current")


class _HwCutDomain_Type(DisplayString):
    """Custom type hwCutDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCutDomain_Type.__name__ = "DisplayString"
_HwCutDomain_Object = MibScalar
hwCutDomain = _HwCutDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 7),
    _HwCutDomain_Type()
)
hwCutDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutDomain.setStatus("current")


class _HwCutIPPoolName_Type(DisplayString):
    """Custom type hwCutIPPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwCutIPPoolName_Type.__name__ = "DisplayString"
_HwCutIPPoolName_Object = MibScalar
hwCutIPPoolName = _HwCutIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 8),
    _HwCutIPPoolName_Type()
)
hwCutIPPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutIPPoolName.setStatus("current")
_HwCutIfIndex_Type = Integer32
_HwCutIfIndex_Object = MibScalar
hwCutIfIndex = _HwCutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 9),
    _HwCutIfIndex_Type()
)
hwCutIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutIfIndex.setStatus("current")


class _HwCutVlanID_Type(Integer32):
    """Custom type hwCutVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268308478),
    )


_HwCutVlanID_Type.__name__ = "Integer32"
_HwCutVlanID_Object = MibScalar
hwCutVlanID = _HwCutVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 10),
    _HwCutVlanID_Type()
)
hwCutVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutVlanID.setStatus("current")


class _HwCutVPI_Type(Integer32):
    """Custom type hwCutVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwCutVPI_Type.__name__ = "Integer32"
_HwCutVPI_Object = MibScalar
hwCutVPI = _HwCutVPI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 11),
    _HwCutVPI_Type()
)
hwCutVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutVPI.setStatus("current")


class _HwCutVCI_Type(Integer32):
    """Custom type hwCutVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HwCutVCI_Type.__name__ = "Integer32"
_HwCutVCI_Object = MibScalar
hwCutVCI = _HwCutVCI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 12),
    _HwCutVCI_Type()
)
hwCutVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutVCI.setStatus("current")


class _HwCutVRF_Type(DisplayString):
    """Custom type hwCutVRF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCutVRF_Type.__name__ = "DisplayString"
_HwCutVRF_Object = MibScalar
hwCutVRF = _HwCutVRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 13),
    _HwCutVRF_Type()
)
hwCutVRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutVRF.setStatus("current")


class _HwCutAccessInterface_Type(DisplayString):
    """Custom type hwCutAccessInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwCutAccessInterface_Type.__name__ = "DisplayString"
_HwCutAccessInterface_Object = MibScalar
hwCutAccessInterface = _HwCutAccessInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 14),
    _HwCutAccessInterface_Type()
)
hwCutAccessInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutAccessInterface.setStatus("current")


class _HwCutUserSSID_Type(DisplayString):
    """Custom type hwCutUserSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwCutUserSSID_Type.__name__ = "DisplayString"
_HwCutUserSSID_Object = MibScalar
hwCutUserSSID = _HwCutUserSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 15),
    _HwCutUserSSID_Type()
)
hwCutUserSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutUserSSID.setStatus("current")
_HwCutAccessSlot_Type = Integer32
_HwCutAccessSlot_Object = MibScalar
hwCutAccessSlot = _HwCutAccessSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 16),
    _HwCutAccessSlot_Type()
)
hwCutAccessSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutAccessSlot.setStatus("current")


class _HwCutUserGroup_Type(DisplayString):
    """Custom type hwCutUserGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCutUserGroup_Type.__name__ = "DisplayString"
_HwCutUserGroup_Object = MibScalar
hwCutUserGroup = _HwCutUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 28, 17),
    _HwCutUserGroup_Type()
)
hwCutUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCutUserGroup.setStatus("current")
_HwAAACallRate_ObjectIdentity = ObjectIdentity
hwAAACallRate = _HwAAACallRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29)
)
_HwAAAUserPPP_ObjectIdentity = ObjectIdentity
hwAAAUserPPP = _HwAAAUserPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 1)
)
_HwTotalConnectNum_Type = Counter32
_HwTotalConnectNum_Object = MibScalar
hwTotalConnectNum = _HwTotalConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 1, 1),
    _HwTotalConnectNum_Type()
)
hwTotalConnectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalConnectNum.setStatus("current")
_HwTotalSuccessNum_Type = Counter32
_HwTotalSuccessNum_Object = MibScalar
hwTotalSuccessNum = _HwTotalSuccessNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 1, 2),
    _HwTotalSuccessNum_Type()
)
hwTotalSuccessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalSuccessNum.setStatus("current")
_HwTotalLCPFailNum_Type = Counter32
_HwTotalLCPFailNum_Object = MibScalar
hwTotalLCPFailNum = _HwTotalLCPFailNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 1, 3),
    _HwTotalLCPFailNum_Type()
)
hwTotalLCPFailNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalLCPFailNum.setStatus("current")
_HwTotalAuthenFailNum_Type = Counter32
_HwTotalAuthenFailNum_Object = MibScalar
hwTotalAuthenFailNum = _HwTotalAuthenFailNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 1, 4),
    _HwTotalAuthenFailNum_Type()
)
hwTotalAuthenFailNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalAuthenFailNum.setStatus("current")
_HwTotalNCPFailNum_Type = Counter32
_HwTotalNCPFailNum_Object = MibScalar
hwTotalNCPFailNum = _HwTotalNCPFailNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 1, 5),
    _HwTotalNCPFailNum_Type()
)
hwTotalNCPFailNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalNCPFailNum.setStatus("current")
_HwTotalIPAllocFailNum_Type = Counter32
_HwTotalIPAllocFailNum_Object = MibScalar
hwTotalIPAllocFailNum = _HwTotalIPAllocFailNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 1, 6),
    _HwTotalIPAllocFailNum_Type()
)
hwTotalIPAllocFailNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalIPAllocFailNum.setStatus("current")
_HwTotalOtherPPPFailNum_Type = Counter32
_HwTotalOtherPPPFailNum_Object = MibScalar
hwTotalOtherPPPFailNum = _HwTotalOtherPPPFailNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 1, 7),
    _HwTotalOtherPPPFailNum_Type()
)
hwTotalOtherPPPFailNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalOtherPPPFailNum.setStatus("current")
_HwAAAUserWebandFast_ObjectIdentity = ObjectIdentity
hwAAAUserWebandFast = _HwAAAUserWebandFast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 2)
)
_HwTotalWebConnectNum_Type = Counter32
_HwTotalWebConnectNum_Object = MibScalar
hwTotalWebConnectNum = _HwTotalWebConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 2, 1),
    _HwTotalWebConnectNum_Type()
)
hwTotalWebConnectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalWebConnectNum.setStatus("current")
_HwTotalSuccessWebConnectNum_Type = Counter32
_HwTotalSuccessWebConnectNum_Object = MibScalar
hwTotalSuccessWebConnectNum = _HwTotalSuccessWebConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 2, 2),
    _HwTotalSuccessWebConnectNum_Type()
)
hwTotalSuccessWebConnectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalSuccessWebConnectNum.setStatus("current")
_HwAAAUserDot1X_ObjectIdentity = ObjectIdentity
hwAAAUserDot1X = _HwAAAUserDot1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 3)
)
_HwTotalDot1XConnectNum_Type = Counter32
_HwTotalDot1XConnectNum_Object = MibScalar
hwTotalDot1XConnectNum = _HwTotalDot1XConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 3, 1),
    _HwTotalDot1XConnectNum_Type()
)
hwTotalDot1XConnectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalDot1XConnectNum.setStatus("current")
_HwTotalSuccessDot1XConnectNum_Type = Counter32
_HwTotalSuccessDot1XConnectNum_Object = MibScalar
hwTotalSuccessDot1XConnectNum = _HwTotalSuccessDot1XConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 3, 2),
    _HwTotalSuccessDot1XConnectNum_Type()
)
hwTotalSuccessDot1XConnectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalSuccessDot1XConnectNum.setStatus("current")
_HwAAAUserBind_ObjectIdentity = ObjectIdentity
hwAAAUserBind = _HwAAAUserBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 4)
)
_HwTotalBindConnectNum_Type = Counter32
_HwTotalBindConnectNum_Object = MibScalar
hwTotalBindConnectNum = _HwTotalBindConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 4, 1),
    _HwTotalBindConnectNum_Type()
)
hwTotalBindConnectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalBindConnectNum.setStatus("current")
_HwTotalSuccessBindConnectNum_Type = Counter32
_HwTotalSuccessBindConnectNum_Object = MibScalar
hwTotalSuccessBindConnectNum = _HwTotalSuccessBindConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 29, 4, 2),
    _HwTotalSuccessBindConnectNum_Type()
)
hwTotalSuccessBindConnectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalSuccessBindConnectNum.setStatus("current")
_HwRecordSchemeTable_Object = MibTable
hwRecordSchemeTable = _HwRecordSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 30)
)
if mibBuilder.loadTexts:
    hwRecordSchemeTable.setStatus("current")
_HwRecordSchemeEntry_Object = MibTableRow
hwRecordSchemeEntry = _HwRecordSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 30, 1)
)
hwRecordSchemeEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwRecordSchemeName"),
)
if mibBuilder.loadTexts:
    hwRecordSchemeEntry.setStatus("current")


class _HwRecordSchemeName_Type(DisplayString):
    """Custom type hwRecordSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwRecordSchemeName_Type.__name__ = "DisplayString"
_HwRecordSchemeName_Object = MibTableColumn
hwRecordSchemeName = _HwRecordSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 30, 1, 1),
    _HwRecordSchemeName_Type()
)
hwRecordSchemeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRecordSchemeName.setStatus("current")


class _HwRecordTacGroupName_Type(DisplayString):
    """Custom type hwRecordTacGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwRecordTacGroupName_Type.__name__ = "DisplayString"
_HwRecordTacGroupName_Object = MibTableColumn
hwRecordTacGroupName = _HwRecordTacGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 30, 1, 2),
    _HwRecordTacGroupName_Type()
)
hwRecordTacGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRecordTacGroupName.setStatus("current")
_HwRecordRowStatus_Type = RowStatus
_HwRecordRowStatus_Object = MibTableColumn
hwRecordRowStatus = _HwRecordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 30, 1, 3),
    _HwRecordRowStatus_Type()
)
hwRecordRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRecordRowStatus.setStatus("current")
_HwMACAccessTable_Object = MibTable
hwMACAccessTable = _HwMACAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 31)
)
if mibBuilder.loadTexts:
    hwMACAccessTable.setStatus("current")
_HwMACAccessEntry_Object = MibTableRow
hwMACAccessEntry = _HwMACAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 31, 1)
)
hwMACAccessEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwMACAccessMACAddress"),
)
if mibBuilder.loadTexts:
    hwMACAccessEntry.setStatus("current")
_HwMACAccessMACAddress_Type = MacAddress
_HwMACAccessMACAddress_Object = MibTableColumn
hwMACAccessMACAddress = _HwMACAccessMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 31, 1, 1),
    _HwMACAccessMACAddress_Type()
)
hwMACAccessMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACAccessMACAddress.setStatus("current")
_HwMACAccessCID_Type = Integer32
_HwMACAccessCID_Object = MibTableColumn
hwMACAccessCID = _HwMACAccessCID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 31, 1, 2),
    _HwMACAccessCID_Type()
)
hwMACAccessCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACAccessCID.setStatus("current")
_HwSlotConnectNumTable_Object = MibTable
hwSlotConnectNumTable = _HwSlotConnectNumTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 32)
)
if mibBuilder.loadTexts:
    hwSlotConnectNumTable.setStatus("current")
_HwSlotConnectNumEntry_Object = MibTableRow
hwSlotConnectNumEntry = _HwSlotConnectNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 32, 1)
)
hwSlotConnectNumEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwSlotConnectNumSlot"),
)
if mibBuilder.loadTexts:
    hwSlotConnectNumEntry.setStatus("current")


class _HwSlotConnectNumSlot_Type(Integer32):
    """Custom type hwSlotConnectNumSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSlotConnectNumSlot_Type.__name__ = "Integer32"
_HwSlotConnectNumSlot_Object = MibTableColumn
hwSlotConnectNumSlot = _HwSlotConnectNumSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 32, 1, 1),
    _HwSlotConnectNumSlot_Type()
)
hwSlotConnectNumSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotConnectNumSlot.setStatus("current")
_HwSlotConnectNumOnlineNum_Type = Integer32
_HwSlotConnectNumOnlineNum_Object = MibTableColumn
hwSlotConnectNumOnlineNum = _HwSlotConnectNumOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 32, 1, 2),
    _HwSlotConnectNumOnlineNum_Type()
)
hwSlotConnectNumOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotConnectNumOnlineNum.setStatus("current")
_HwSlotConnectNumMaxOnlineNum_Type = Integer32
_HwSlotConnectNumMaxOnlineNum_Object = MibTableColumn
hwSlotConnectNumMaxOnlineNum = _HwSlotConnectNumMaxOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 32, 1, 3),
    _HwSlotConnectNumMaxOnlineNum_Type()
)
hwSlotConnectNumMaxOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotConnectNumMaxOnlineNum.setStatus("current")
_HwSlotConnectNumMaxOnlineAcctReadyNum_Type = Integer32
_HwSlotConnectNumMaxOnlineAcctReadyNum_Object = MibTableColumn
hwSlotConnectNumMaxOnlineAcctReadyNum = _HwSlotConnectNumMaxOnlineAcctReadyNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 32, 1, 4),
    _HwSlotConnectNumMaxOnlineAcctReadyNum_Type()
)
hwSlotConnectNumMaxOnlineAcctReadyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotConnectNumMaxOnlineAcctReadyNum.setStatus("current")
_HwSlotCardConnectNumTable_Object = MibTable
hwSlotCardConnectNumTable = _HwSlotCardConnectNumTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33)
)
if mibBuilder.loadTexts:
    hwSlotCardConnectNumTable.setStatus("current")
_HwSlotCardConnectNumEntry_Object = MibTableRow
hwSlotCardConnectNumEntry = _HwSlotCardConnectNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1)
)
hwSlotCardConnectNumEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwSlotCardConnectNumSlot"),
    (0, "HUAWEI-AAA-MIB", "hwSlotCardConnectNumCard"),
)
if mibBuilder.loadTexts:
    hwSlotCardConnectNumEntry.setStatus("current")


class _HwSlotCardConnectNumSlot_Type(Integer32):
    """Custom type hwSlotCardConnectNumSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSlotCardConnectNumSlot_Type.__name__ = "Integer32"
_HwSlotCardConnectNumSlot_Object = MibTableColumn
hwSlotCardConnectNumSlot = _HwSlotCardConnectNumSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 1),
    _HwSlotCardConnectNumSlot_Type()
)
hwSlotCardConnectNumSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumSlot.setStatus("current")
_HwSlotCardConnectNumCard_Type = Integer32
_HwSlotCardConnectNumCard_Object = MibTableColumn
hwSlotCardConnectNumCard = _HwSlotCardConnectNumCard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 2),
    _HwSlotCardConnectNumCard_Type()
)
hwSlotCardConnectNumCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumCard.setStatus("current")
_HwSlotCardConnectNumOnlineNum_Type = Integer32
_HwSlotCardConnectNumOnlineNum_Object = MibTableColumn
hwSlotCardConnectNumOnlineNum = _HwSlotCardConnectNumOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 3),
    _HwSlotCardConnectNumOnlineNum_Type()
)
hwSlotCardConnectNumOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumOnlineNum.setStatus("current")
_HwSlotCardConnectNumIPv4OnlineNum_Type = Integer32
_HwSlotCardConnectNumIPv4OnlineNum_Object = MibTableColumn
hwSlotCardConnectNumIPv4OnlineNum = _HwSlotCardConnectNumIPv4OnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 4),
    _HwSlotCardConnectNumIPv4OnlineNum_Type()
)
hwSlotCardConnectNumIPv4OnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumIPv4OnlineNum.setStatus("current")
_HwSlotCardConnectNumIPv6OnlineNum_Type = Integer32
_HwSlotCardConnectNumIPv6OnlineNum_Object = MibTableColumn
hwSlotCardConnectNumIPv6OnlineNum = _HwSlotCardConnectNumIPv6OnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 5),
    _HwSlotCardConnectNumIPv6OnlineNum_Type()
)
hwSlotCardConnectNumIPv6OnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumIPv6OnlineNum.setStatus("current")
_HwSlotCardConnectNumDualOnlineNum_Type = Integer32
_HwSlotCardConnectNumDualOnlineNum_Object = MibTableColumn
hwSlotCardConnectNumDualOnlineNum = _HwSlotCardConnectNumDualOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 6),
    _HwSlotCardConnectNumDualOnlineNum_Type()
)
hwSlotCardConnectNumDualOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumDualOnlineNum.setStatus("current")
_HwSlotCardConnectNumNoAuthNum_Type = Integer32
_HwSlotCardConnectNumNoAuthNum_Object = MibTableColumn
hwSlotCardConnectNumNoAuthNum = _HwSlotCardConnectNumNoAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 7),
    _HwSlotCardConnectNumNoAuthNum_Type()
)
hwSlotCardConnectNumNoAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumNoAuthNum.setStatus("current")
_HwSlotCardConnectNumPPPAuthNum_Type = Integer32
_HwSlotCardConnectNumPPPAuthNum_Object = MibTableColumn
hwSlotCardConnectNumPPPAuthNum = _HwSlotCardConnectNumPPPAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 8),
    _HwSlotCardConnectNumPPPAuthNum_Type()
)
hwSlotCardConnectNumPPPAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumPPPAuthNum.setStatus("current")
_HwSlotCardConnectNum8021xAuthNum_Type = Integer32
_HwSlotCardConnectNum8021xAuthNum_Object = MibTableColumn
hwSlotCardConnectNum8021xAuthNum = _HwSlotCardConnectNum8021xAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 9),
    _HwSlotCardConnectNum8021xAuthNum_Type()
)
hwSlotCardConnectNum8021xAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNum8021xAuthNum.setStatus("current")
_HwSlotCardConnectNumWebAuthNum_Type = Integer32
_HwSlotCardConnectNumWebAuthNum_Object = MibTableColumn
hwSlotCardConnectNumWebAuthNum = _HwSlotCardConnectNumWebAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 10),
    _HwSlotCardConnectNumWebAuthNum_Type()
)
hwSlotCardConnectNumWebAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumWebAuthNum.setStatus("current")
_HwSlotCardConnectNumBindAuthNum_Type = Integer32
_HwSlotCardConnectNumBindAuthNum_Object = MibTableColumn
hwSlotCardConnectNumBindAuthNum = _HwSlotCardConnectNumBindAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 11),
    _HwSlotCardConnectNumBindAuthNum_Type()
)
hwSlotCardConnectNumBindAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumBindAuthNum.setStatus("current")
_HwSlotCardConnectNumFastAuthNum_Type = Integer32
_HwSlotCardConnectNumFastAuthNum_Object = MibTableColumn
hwSlotCardConnectNumFastAuthNum = _HwSlotCardConnectNumFastAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 12),
    _HwSlotCardConnectNumFastAuthNum_Type()
)
hwSlotCardConnectNumFastAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumFastAuthNum.setStatus("current")
_HwSlotCardConnectNumWlanAuthNum_Type = Integer32
_HwSlotCardConnectNumWlanAuthNum_Object = MibTableColumn
hwSlotCardConnectNumWlanAuthNum = _HwSlotCardConnectNumWlanAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 13),
    _HwSlotCardConnectNumWlanAuthNum_Type()
)
hwSlotCardConnectNumWlanAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumWlanAuthNum.setStatus("current")
_HwSlotCardConnectNumAdminAuthNum_Type = Integer32
_HwSlotCardConnectNumAdminAuthNum_Object = MibTableColumn
hwSlotCardConnectNumAdminAuthNum = _HwSlotCardConnectNumAdminAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 14),
    _HwSlotCardConnectNumAdminAuthNum_Type()
)
hwSlotCardConnectNumAdminAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumAdminAuthNum.setStatus("current")
_HwSlotCardConnectNumTunnelAuthNum_Type = Integer32
_HwSlotCardConnectNumTunnelAuthNum_Object = MibTableColumn
hwSlotCardConnectNumTunnelAuthNum = _HwSlotCardConnectNumTunnelAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 15),
    _HwSlotCardConnectNumTunnelAuthNum_Type()
)
hwSlotCardConnectNumTunnelAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumTunnelAuthNum.setStatus("current")
_HwSlotCardConnectNumMIPAuthNum_Type = Integer32
_HwSlotCardConnectNumMIPAuthNum_Object = MibTableColumn
hwSlotCardConnectNumMIPAuthNum = _HwSlotCardConnectNumMIPAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 33, 1, 16),
    _HwSlotCardConnectNumMIPAuthNum_Type()
)
hwSlotCardConnectNumMIPAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotCardConnectNumMIPAuthNum.setStatus("current")
_HwOfflineReasonStatTable_Object = MibTable
hwOfflineReasonStatTable = _HwOfflineReasonStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 34)
)
if mibBuilder.loadTexts:
    hwOfflineReasonStatTable.setStatus("current")
_HwOfflineReasonStatEntry_Object = MibTableRow
hwOfflineReasonStatEntry = _HwOfflineReasonStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 34, 1)
)
hwOfflineReasonStatEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwOfflineReason"),
)
if mibBuilder.loadTexts:
    hwOfflineReasonStatEntry.setStatus("current")


class _HwOfflineReason_Type(Integer32):
    """Custom type hwOfflineReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HwOfflineReason_Type.__name__ = "Integer32"
_HwOfflineReason_Object = MibTableColumn
hwOfflineReason = _HwOfflineReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 34, 1, 1),
    _HwOfflineReason_Type()
)
hwOfflineReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineReason.setStatus("current")
_HwOfflineReasonStatistic_Type = Integer32
_HwOfflineReasonStatistic_Object = MibTableColumn
hwOfflineReasonStatistic = _HwOfflineReasonStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 34, 1, 2),
    _HwOfflineReasonStatistic_Type()
)
hwOfflineReasonStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineReasonStatistic.setStatus("current")
_HwOnlineFailReasonStatistic_Type = Integer32
_HwOnlineFailReasonStatistic_Object = MibTableColumn
hwOnlineFailReasonStatistic = _HwOnlineFailReasonStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 34, 1, 3),
    _HwOnlineFailReasonStatistic_Type()
)
hwOnlineFailReasonStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOnlineFailReasonStatistic.setStatus("current")
_HwMulticastListTable_Object = MibTable
hwMulticastListTable = _HwMulticastListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35)
)
if mibBuilder.loadTexts:
    hwMulticastListTable.setStatus("current")
_HwMulticastListEntry_Object = MibTableRow
hwMulticastListEntry = _HwMulticastListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35, 1)
)
hwMulticastListEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwMulticastListIndex"),
)
if mibBuilder.loadTexts:
    hwMulticastListEntry.setStatus("current")


class _HwMulticastListIndex_Type(Integer32):
    """Custom type hwMulticastListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_HwMulticastListIndex_Type.__name__ = "Integer32"
_HwMulticastListIndex_Object = MibTableColumn
hwMulticastListIndex = _HwMulticastListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35, 1, 1),
    _HwMulticastListIndex_Type()
)
hwMulticastListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMulticastListIndex.setStatus("current")


class _HwMulticastListName_Type(DisplayString):
    """Custom type hwMulticastListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMulticastListName_Type.__name__ = "DisplayString"
_HwMulticastListName_Object = MibTableColumn
hwMulticastListName = _HwMulticastListName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35, 1, 2),
    _HwMulticastListName_Type()
)
hwMulticastListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastListName.setStatus("current")
_HwMulticastListSourceIp_Type = IpAddress
_HwMulticastListSourceIp_Object = MibTableColumn
hwMulticastListSourceIp = _HwMulticastListSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35, 1, 3),
    _HwMulticastListSourceIp_Type()
)
hwMulticastListSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastListSourceIp.setStatus("current")


class _HwMulticastListSourceIpMask_Type(Integer32):
    """Custom type hwMulticastListSourceIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwMulticastListSourceIpMask_Type.__name__ = "Integer32"
_HwMulticastListSourceIpMask_Object = MibTableColumn
hwMulticastListSourceIpMask = _HwMulticastListSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35, 1, 4),
    _HwMulticastListSourceIpMask_Type()
)
hwMulticastListSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastListSourceIpMask.setStatus("current")
_HwMulticastListGroupIp_Type = IpAddress
_HwMulticastListGroupIp_Object = MibTableColumn
hwMulticastListGroupIp = _HwMulticastListGroupIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35, 1, 5),
    _HwMulticastListGroupIp_Type()
)
hwMulticastListGroupIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastListGroupIp.setStatus("current")


class _HwMulticastListGroupIpMask_Type(Integer32):
    """Custom type hwMulticastListGroupIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwMulticastListGroupIpMask_Type.__name__ = "Integer32"
_HwMulticastListGroupIpMask_Object = MibTableColumn
hwMulticastListGroupIpMask = _HwMulticastListGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35, 1, 6),
    _HwMulticastListGroupIpMask_Type()
)
hwMulticastListGroupIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastListGroupIpMask.setStatus("current")


class _HwMulticastListVpnInstance_Type(DisplayString):
    """Custom type hwMulticastListVpnInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMulticastListVpnInstance_Type.__name__ = "DisplayString"
_HwMulticastListVpnInstance_Object = MibTableColumn
hwMulticastListVpnInstance = _HwMulticastListVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35, 1, 7),
    _HwMulticastListVpnInstance_Type()
)
hwMulticastListVpnInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastListVpnInstance.setStatus("current")
_HwMulticastListRowStatus_Type = RowStatus
_HwMulticastListRowStatus_Object = MibTableColumn
hwMulticastListRowStatus = _HwMulticastListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 35, 1, 8),
    _HwMulticastListRowStatus_Type()
)
hwMulticastListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastListRowStatus.setStatus("current")
_HwMulticastProfileTable_Object = MibTable
hwMulticastProfileTable = _HwMulticastProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 36)
)
if mibBuilder.loadTexts:
    hwMulticastProfileTable.setStatus("current")
_HwMulticastProfileEntry_Object = MibTableRow
hwMulticastProfileEntry = _HwMulticastProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 36, 1)
)
hwMulticastProfileEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwMulticastProfileIndex"),
)
if mibBuilder.loadTexts:
    hwMulticastProfileEntry.setStatus("current")


class _HwMulticastProfileIndex_Type(Integer32):
    """Custom type hwMulticastProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwMulticastProfileIndex_Type.__name__ = "Integer32"
_HwMulticastProfileIndex_Object = MibTableColumn
hwMulticastProfileIndex = _HwMulticastProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 36, 1, 1),
    _HwMulticastProfileIndex_Type()
)
hwMulticastProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMulticastProfileIndex.setStatus("current")


class _HwMulticastProfileName_Type(DisplayString):
    """Custom type hwMulticastProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMulticastProfileName_Type.__name__ = "DisplayString"
_HwMulticastProfileName_Object = MibTableColumn
hwMulticastProfileName = _HwMulticastProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 36, 1, 2),
    _HwMulticastProfileName_Type()
)
hwMulticastProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastProfileName.setStatus("current")
_HwMulticastProfileRowStatus_Type = RowStatus
_HwMulticastProfileRowStatus_Object = MibTableColumn
hwMulticastProfileRowStatus = _HwMulticastProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 36, 1, 3),
    _HwMulticastProfileRowStatus_Type()
)
hwMulticastProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastProfileRowStatus.setStatus("current")
_HwMulticastProfileExtTable_Object = MibTable
hwMulticastProfileExtTable = _HwMulticastProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 37)
)
if mibBuilder.loadTexts:
    hwMulticastProfileExtTable.setStatus("current")
_HwMulticastProfileExtEntry_Object = MibTableRow
hwMulticastProfileExtEntry = _HwMulticastProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 37, 1)
)
hwMulticastProfileExtEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwMulticastProfileIndex"),
    (0, "HUAWEI-AAA-MIB", "hwMulticastListIndex"),
)
if mibBuilder.loadTexts:
    hwMulticastProfileExtEntry.setStatus("current")


class _HwMulticastListBindName_Type(DisplayString):
    """Custom type hwMulticastListBindName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMulticastListBindName_Type.__name__ = "DisplayString"
_HwMulticastListBindName_Object = MibTableColumn
hwMulticastListBindName = _HwMulticastListBindName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 37, 1, 1),
    _HwMulticastListBindName_Type()
)
hwMulticastListBindName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastListBindName.setStatus("current")
_HwMulticastProfileExtRowStatus_Type = RowStatus
_HwMulticastProfileExtRowStatus_Object = MibTableColumn
hwMulticastProfileExtRowStatus = _HwMulticastProfileExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 37, 1, 2),
    _HwMulticastProfileExtRowStatus_Type()
)
hwMulticastProfileExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMulticastProfileExtRowStatus.setStatus("current")
_HwServiceSchemeTable_Object = MibTable
hwServiceSchemeTable = _HwServiceSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38)
)
if mibBuilder.loadTexts:
    hwServiceSchemeTable.setStatus("current")
_HwServiceSchemeEntry_Object = MibTableRow
hwServiceSchemeEntry = _HwServiceSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1)
)
hwServiceSchemeEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwServiceSchemeName"),
)
if mibBuilder.loadTexts:
    hwServiceSchemeEntry.setStatus("current")


class _HwServiceSchemeName_Type(DisplayString):
    """Custom type hwServiceSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwServiceSchemeName_Type.__name__ = "DisplayString"
_HwServiceSchemeName_Object = MibTableColumn
hwServiceSchemeName = _HwServiceSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 1),
    _HwServiceSchemeName_Type()
)
hwServiceSchemeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceSchemeName.setStatus("current")
_HwServiceSchemeNextHopIp_Type = IpAddress
_HwServiceSchemeNextHopIp_Object = MibTableColumn
hwServiceSchemeNextHopIp = _HwServiceSchemeNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 11),
    _HwServiceSchemeNextHopIp_Type()
)
hwServiceSchemeNextHopIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwServiceSchemeNextHopIp.setStatus("current")


class _HwServiceSchemeUserPriority_Type(Integer32):
    """Custom type hwServiceSchemeUserPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwServiceSchemeUserPriority_Type.__name__ = "Integer32"
_HwServiceSchemeUserPriority_Object = MibTableColumn
hwServiceSchemeUserPriority = _HwServiceSchemeUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 12),
    _HwServiceSchemeUserPriority_Type()
)
hwServiceSchemeUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwServiceSchemeUserPriority.setStatus("current")


class _HwServiceSchemeIdleCutTime_Type(Integer32):
    """Custom type hwServiceSchemeIdleCutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HwServiceSchemeIdleCutTime_Type.__name__ = "Integer32"
_HwServiceSchemeIdleCutTime_Object = MibTableColumn
hwServiceSchemeIdleCutTime = _HwServiceSchemeIdleCutTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 13),
    _HwServiceSchemeIdleCutTime_Type()
)
hwServiceSchemeIdleCutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwServiceSchemeIdleCutTime.setStatus("current")


class _HwServiceSchemeIdleCutFlow_Type(Integer32):
    """Custom type hwServiceSchemeIdleCutFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 768000),
    )


_HwServiceSchemeIdleCutFlow_Type.__name__ = "Integer32"
_HwServiceSchemeIdleCutFlow_Object = MibTableColumn
hwServiceSchemeIdleCutFlow = _HwServiceSchemeIdleCutFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 14),
    _HwServiceSchemeIdleCutFlow_Type()
)
hwServiceSchemeIdleCutFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwServiceSchemeIdleCutFlow.setStatus("current")
_HwServiceSchemeDnsFirst_Type = IpAddress
_HwServiceSchemeDnsFirst_Object = MibTableColumn
hwServiceSchemeDnsFirst = _HwServiceSchemeDnsFirst_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 15),
    _HwServiceSchemeDnsFirst_Type()
)
hwServiceSchemeDnsFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwServiceSchemeDnsFirst.setStatus("current")
_HwServiceSchemeDnsSecond_Type = IpAddress
_HwServiceSchemeDnsSecond_Object = MibTableColumn
hwServiceSchemeDnsSecond = _HwServiceSchemeDnsSecond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 16),
    _HwServiceSchemeDnsSecond_Type()
)
hwServiceSchemeDnsSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwServiceSchemeDnsSecond.setStatus("current")


class _HwSrvSchemeAdminUserPriority_Type(Integer32):
    """Custom type hwSrvSchemeAdminUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_HwSrvSchemeAdminUserPriority_Type.__name__ = "Integer32"
_HwSrvSchemeAdminUserPriority_Object = MibTableColumn
hwSrvSchemeAdminUserPriority = _HwSrvSchemeAdminUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 17),
    _HwSrvSchemeAdminUserPriority_Type()
)
hwSrvSchemeAdminUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSrvSchemeAdminUserPriority.setStatus("current")


class _HwSrvSchemeIpPoolOneName_Type(DisplayString):
    """Custom type hwSrvSchemeIpPoolOneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSrvSchemeIpPoolOneName_Type.__name__ = "DisplayString"
_HwSrvSchemeIpPoolOneName_Object = MibTableColumn
hwSrvSchemeIpPoolOneName = _HwSrvSchemeIpPoolOneName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 18),
    _HwSrvSchemeIpPoolOneName_Type()
)
hwSrvSchemeIpPoolOneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSrvSchemeIpPoolOneName.setStatus("current")


class _HwSrvSchemeIpPoolTwoName_Type(DisplayString):
    """Custom type hwSrvSchemeIpPoolTwoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSrvSchemeIpPoolTwoName_Type.__name__ = "DisplayString"
_HwSrvSchemeIpPoolTwoName_Object = MibTableColumn
hwSrvSchemeIpPoolTwoName = _HwSrvSchemeIpPoolTwoName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 19),
    _HwSrvSchemeIpPoolTwoName_Type()
)
hwSrvSchemeIpPoolTwoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSrvSchemeIpPoolTwoName.setStatus("current")


class _HwSrvSchemeIpPoolThreeName_Type(DisplayString):
    """Custom type hwSrvSchemeIpPoolThreeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSrvSchemeIpPoolThreeName_Type.__name__ = "DisplayString"
_HwSrvSchemeIpPoolThreeName_Object = MibTableColumn
hwSrvSchemeIpPoolThreeName = _HwSrvSchemeIpPoolThreeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 20),
    _HwSrvSchemeIpPoolThreeName_Type()
)
hwSrvSchemeIpPoolThreeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSrvSchemeIpPoolThreeName.setStatus("current")
_HwServiceSchemeRowStatus_Type = RowStatus
_HwServiceSchemeRowStatus_Object = MibTableColumn
hwServiceSchemeRowStatus = _HwServiceSchemeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 51),
    _HwServiceSchemeRowStatus_Type()
)
hwServiceSchemeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwServiceSchemeRowStatus.setStatus("current")


class _HwServiceSchemeIdleCutType_Type(Integer32):
    """Custom type hwServiceSchemeIdleCutType based on Integer32"""
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
        *(("both", 3),
          ("inbound", 1),
          ("none", 4),
          ("outbound", 2))
    )


_HwServiceSchemeIdleCutType_Type.__name__ = "Integer32"
_HwServiceSchemeIdleCutType_Object = MibTableColumn
hwServiceSchemeIdleCutType = _HwServiceSchemeIdleCutType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 52),
    _HwServiceSchemeIdleCutType_Type()
)
hwServiceSchemeIdleCutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwServiceSchemeIdleCutType.setStatus("current")


class _HwServiceSchemeIdleCutFlowValue_Type(Unsigned32):
    """Custom type hwServiceSchemeIdleCutFlowValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwServiceSchemeIdleCutFlowValue_Type.__name__ = "Unsigned32"
_HwServiceSchemeIdleCutFlowValue_Object = MibTableColumn
hwServiceSchemeIdleCutFlowValue = _HwServiceSchemeIdleCutFlowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 53),
    _HwServiceSchemeIdleCutFlowValue_Type()
)
hwServiceSchemeIdleCutFlowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwServiceSchemeIdleCutFlowValue.setStatus("current")


class _HwLocalAuthorize_Type(DisplayString):
    """Custom type hwLocalAuthorize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwLocalAuthorize_Type.__name__ = "DisplayString"
_HwLocalAuthorize_Object = MibTableColumn
hwLocalAuthorize = _HwLocalAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 54),
    _HwLocalAuthorize_Type()
)
hwLocalAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalAuthorize.setStatus("current")


class _HwRemoteAuthorize_Type(DisplayString):
    """Custom type hwRemoteAuthorize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwRemoteAuthorize_Type.__name__ = "DisplayString"
_HwRemoteAuthorize_Object = MibTableColumn
hwRemoteAuthorize = _HwRemoteAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 38, 1, 55),
    _HwRemoteAuthorize_Type()
)
hwRemoteAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteAuthorize.setStatus("current")
_HwDhcpOpt121RouteTable_Object = MibTable
hwDhcpOpt121RouteTable = _HwDhcpOpt121RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 39)
)
if mibBuilder.loadTexts:
    hwDhcpOpt121RouteTable.setStatus("current")
_HwDhcpOpt121RouteEntry_Object = MibTableRow
hwDhcpOpt121RouteEntry = _HwDhcpOpt121RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 39, 1)
)
hwDhcpOpt121RouteEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwDomainName"),
    (0, "HUAWEI-AAA-MIB", "hwDhcpOpt121RouteDestIp"),
    (0, "HUAWEI-AAA-MIB", "hwDhcpOpt121RouteMask"),
    (0, "HUAWEI-AAA-MIB", "hwDhcpOpt121RouteNextHop"),
)
if mibBuilder.loadTexts:
    hwDhcpOpt121RouteEntry.setStatus("current")
_HwDhcpOpt121RouteDestIp_Type = IpAddress
_HwDhcpOpt121RouteDestIp_Object = MibTableColumn
hwDhcpOpt121RouteDestIp = _HwDhcpOpt121RouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 39, 1, 1),
    _HwDhcpOpt121RouteDestIp_Type()
)
hwDhcpOpt121RouteDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpOpt121RouteDestIp.setStatus("current")


class _HwDhcpOpt121RouteMask_Type(Integer32):
    """Custom type hwDhcpOpt121RouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwDhcpOpt121RouteMask_Type.__name__ = "Integer32"
_HwDhcpOpt121RouteMask_Object = MibTableColumn
hwDhcpOpt121RouteMask = _HwDhcpOpt121RouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 39, 1, 2),
    _HwDhcpOpt121RouteMask_Type()
)
hwDhcpOpt121RouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpOpt121RouteMask.setStatus("current")
_HwDhcpOpt121RouteNextHop_Type = IpAddress
_HwDhcpOpt121RouteNextHop_Object = MibTableColumn
hwDhcpOpt121RouteNextHop = _HwDhcpOpt121RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 39, 1, 3),
    _HwDhcpOpt121RouteNextHop_Type()
)
hwDhcpOpt121RouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpOpt121RouteNextHop.setStatus("current")
_HwDhcpOpt121RouteRowStatus_Type = RowStatus
_HwDhcpOpt121RouteRowStatus_Object = MibTableColumn
hwDhcpOpt121RouteRowStatus = _HwDhcpOpt121RouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 39, 1, 4),
    _HwDhcpOpt121RouteRowStatus_Type()
)
hwDhcpOpt121RouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpOpt121RouteRowStatus.setStatus("current")
_HwAccessDelayPerSlotTable_Object = MibTable
hwAccessDelayPerSlotTable = _HwAccessDelayPerSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 40)
)
if mibBuilder.loadTexts:
    hwAccessDelayPerSlotTable.setStatus("current")
_HwAccessDelayPerSlotEntry_Object = MibTableRow
hwAccessDelayPerSlotEntry = _HwAccessDelayPerSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 40, 1)
)
hwAccessDelayPerSlotEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAccessDelayPerSlotSlot"),
)
if mibBuilder.loadTexts:
    hwAccessDelayPerSlotEntry.setStatus("current")


class _HwAccessDelayPerSlotSlot_Type(Integer32):
    """Custom type hwAccessDelayPerSlotSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwAccessDelayPerSlotSlot_Type.__name__ = "Integer32"
_HwAccessDelayPerSlotSlot_Object = MibTableColumn
hwAccessDelayPerSlotSlot = _HwAccessDelayPerSlotSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 40, 1, 1),
    _HwAccessDelayPerSlotSlot_Type()
)
hwAccessDelayPerSlotSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccessDelayPerSlotSlot.setStatus("current")


class _HwAccessDelayPerSlotTransitionStep_Type(Integer32):
    """Custom type hwAccessDelayPerSlotTransitionStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262144),
    )


_HwAccessDelayPerSlotTransitionStep_Type.__name__ = "Integer32"
_HwAccessDelayPerSlotTransitionStep_Object = MibTableColumn
hwAccessDelayPerSlotTransitionStep = _HwAccessDelayPerSlotTransitionStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 40, 1, 2),
    _HwAccessDelayPerSlotTransitionStep_Type()
)
hwAccessDelayPerSlotTransitionStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAccessDelayPerSlotTransitionStep.setStatus("current")


class _HwAccessDelayPerSlotMaxTime_Type(Integer32):
    """Custom type hwAccessDelayPerSlotMaxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2550),
    )


_HwAccessDelayPerSlotMaxTime_Type.__name__ = "Integer32"
_HwAccessDelayPerSlotMaxTime_Object = MibTableColumn
hwAccessDelayPerSlotMaxTime = _HwAccessDelayPerSlotMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 40, 1, 3),
    _HwAccessDelayPerSlotMaxTime_Type()
)
hwAccessDelayPerSlotMaxTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAccessDelayPerSlotMaxTime.setStatus("current")


class _HwAccessDelayPerSlotMinTime_Type(Integer32):
    """Custom type hwAccessDelayPerSlotMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2550),
    )


_HwAccessDelayPerSlotMinTime_Type.__name__ = "Integer32"
_HwAccessDelayPerSlotMinTime_Object = MibTableColumn
hwAccessDelayPerSlotMinTime = _HwAccessDelayPerSlotMinTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 40, 1, 4),
    _HwAccessDelayPerSlotMinTime_Type()
)
hwAccessDelayPerSlotMinTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAccessDelayPerSlotMinTime.setStatus("current")
_HwAccessDelayPerSlotRowStatus_Type = RowStatus
_HwAccessDelayPerSlotRowStatus_Object = MibTableColumn
hwAccessDelayPerSlotRowStatus = _HwAccessDelayPerSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 40, 1, 5),
    _HwAccessDelayPerSlotRowStatus_Type()
)
hwAccessDelayPerSlotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAccessDelayPerSlotRowStatus.setStatus("current")
_HwVpnAccessUserStatTable_Object = MibTable
hwVpnAccessUserStatTable = _HwVpnAccessUserStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 41)
)
if mibBuilder.loadTexts:
    hwVpnAccessUserStatTable.setStatus("current")
_HwVpnAccessUserStatEntry_Object = MibTableRow
hwVpnAccessUserStatEntry = _HwVpnAccessUserStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 41, 1)
)
hwVpnAccessUserStatEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwUserType"),
    (0, "HUAWEI-AAA-MIB", "hwVpnAccessUserStatVpnName"),
)
if mibBuilder.loadTexts:
    hwVpnAccessUserStatEntry.setStatus("current")


class _HwUserType_Type(Integer32):
    """Custom type hwUserType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 9),
          ("dhcp", 3),
          ("dualStack", 8),
          ("ipv4", 6),
          ("ipv6", 7),
          ("lac", 5),
          ("lns", 4),
          ("pppoa", 2),
          ("pppoe", 1))
    )


_HwUserType_Type.__name__ = "Integer32"
_HwUserType_Object = MibTableColumn
hwUserType = _HwUserType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 41, 1, 1),
    _HwUserType_Type()
)
hwUserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserType.setStatus("current")


class _HwVpnAccessUserStatVpnName_Type(DisplayString):
    """Custom type hwVpnAccessUserStatVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVpnAccessUserStatVpnName_Type.__name__ = "DisplayString"
_HwVpnAccessUserStatVpnName_Object = MibTableColumn
hwVpnAccessUserStatVpnName = _HwVpnAccessUserStatVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 41, 1, 2),
    _HwVpnAccessUserStatVpnName_Type()
)
hwVpnAccessUserStatVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnAccessUserStatVpnName.setStatus("current")


class _HwVpnAccessUserStatUserStat_Type(Integer32):
    """Custom type hwVpnAccessUserStatUserStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_HwVpnAccessUserStatUserStat_Type.__name__ = "Integer32"
_HwVpnAccessUserStatUserStat_Object = MibTableColumn
hwVpnAccessUserStatUserStat = _HwVpnAccessUserStatUserStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 41, 1, 3),
    _HwVpnAccessUserStatUserStat_Type()
)
hwVpnAccessUserStatUserStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnAccessUserStatUserStat.setStatus("current")
_HwInterfaceAccessUserStatTable_Object = MibTable
hwInterfaceAccessUserStatTable = _HwInterfaceAccessUserStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 42)
)
if mibBuilder.loadTexts:
    hwInterfaceAccessUserStatTable.setStatus("current")
_HwInterfaceAccessUserStatEntry_Object = MibTableRow
hwInterfaceAccessUserStatEntry = _HwInterfaceAccessUserStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 42, 1)
)
hwInterfaceAccessUserStatEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwUserType"),
    (0, "HUAWEI-AAA-MIB", "hwInterfaceAccessUserStatInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwInterfaceAccessUserStatEntry.setStatus("current")


class _HwInterfaceAccessUserStatInterfaceIndex_Type(Unsigned32):
    """Custom type hwInterfaceAccessUserStatInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwInterfaceAccessUserStatInterfaceIndex_Type.__name__ = "Unsigned32"
_HwInterfaceAccessUserStatInterfaceIndex_Object = MibTableColumn
hwInterfaceAccessUserStatInterfaceIndex = _HwInterfaceAccessUserStatInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 42, 1, 1),
    _HwInterfaceAccessUserStatInterfaceIndex_Type()
)
hwInterfaceAccessUserStatInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInterfaceAccessUserStatInterfaceIndex.setStatus("current")


class _HwInterfaceAccessUserStatUserStat_Type(Integer32):
    """Custom type hwInterfaceAccessUserStatUserStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_HwInterfaceAccessUserStatUserStat_Type.__name__ = "Integer32"
_HwInterfaceAccessUserStatUserStat_Object = MibTableColumn
hwInterfaceAccessUserStatUserStat = _HwInterfaceAccessUserStatUserStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 42, 1, 2),
    _HwInterfaceAccessUserStatUserStat_Type()
)
hwInterfaceAccessUserStatUserStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInterfaceAccessUserStatUserStat.setStatus("current")
_HwDomainAccessUserStatTable_Object = MibTable
hwDomainAccessUserStatTable = _HwDomainAccessUserStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 43)
)
if mibBuilder.loadTexts:
    hwDomainAccessUserStatTable.setStatus("current")
_HwDomainAccessUserStatEntry_Object = MibTableRow
hwDomainAccessUserStatEntry = _HwDomainAccessUserStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 43, 1)
)
hwDomainAccessUserStatEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwUserType"),
    (0, "HUAWEI-AAA-MIB", "hwDomainName"),
)
if mibBuilder.loadTexts:
    hwDomainAccessUserStatEntry.setStatus("current")


class _HwDomainAccessUserStatUserStat_Type(Integer32):
    """Custom type hwDomainAccessUserStatUserStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_HwDomainAccessUserStatUserStat_Type.__name__ = "Integer32"
_HwDomainAccessUserStatUserStat_Object = MibTableColumn
hwDomainAccessUserStatUserStat = _HwDomainAccessUserStatUserStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 43, 1, 1),
    _HwDomainAccessUserStatUserStat_Type()
)
hwDomainAccessUserStatUserStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainAccessUserStatUserStat.setStatus("current")
_HwSlotAccessUserStatTable_Object = MibTable
hwSlotAccessUserStatTable = _HwSlotAccessUserStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 44)
)
if mibBuilder.loadTexts:
    hwSlotAccessUserStatTable.setStatus("current")
_HwSlotAccessUserStatEntry_Object = MibTableRow
hwSlotAccessUserStatEntry = _HwSlotAccessUserStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 44, 1)
)
hwSlotAccessUserStatEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwUserType"),
    (0, "HUAWEI-AAA-MIB", "hwSlotAccessUserStatSlot"),
)
if mibBuilder.loadTexts:
    hwSlotAccessUserStatEntry.setStatus("current")


class _HwSlotAccessUserStatSlot_Type(Integer32):
    """Custom type hwSlotAccessUserStatSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSlotAccessUserStatSlot_Type.__name__ = "Integer32"
_HwSlotAccessUserStatSlot_Object = MibTableColumn
hwSlotAccessUserStatSlot = _HwSlotAccessUserStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 44, 1, 1),
    _HwSlotAccessUserStatSlot_Type()
)
hwSlotAccessUserStatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotAccessUserStatSlot.setStatus("current")


class _HwSlotAccessUserStatUserStat_Type(Integer32):
    """Custom type hwSlotAccessUserStatUserStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_HwSlotAccessUserStatUserStat_Type.__name__ = "Integer32"
_HwSlotAccessUserStatUserStat_Object = MibTableColumn
hwSlotAccessUserStatUserStat = _HwSlotAccessUserStatUserStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 44, 1, 2),
    _HwSlotAccessUserStatUserStat_Type()
)
hwSlotAccessUserStatUserStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotAccessUserStatUserStat.setStatus("current")
_HwDomainIncludePoolGroupTable_Object = MibTable
hwDomainIncludePoolGroupTable = _HwDomainIncludePoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 45)
)
if mibBuilder.loadTexts:
    hwDomainIncludePoolGroupTable.setStatus("current")
_HwDomainIncludePoolGroupEntry_Object = MibTableRow
hwDomainIncludePoolGroupEntry = _HwDomainIncludePoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 45, 1)
)
hwDomainIncludePoolGroupEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwDomainName"),
    (0, "HUAWEI-AAA-MIB", "hwDomainIncludeIPPoolGroupName"),
)
if mibBuilder.loadTexts:
    hwDomainIncludePoolGroupEntry.setStatus("current")


class _HwDomainIncludeIPPoolGroupName_Type(DisplayString):
    """Custom type hwDomainIncludeIPPoolGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainIncludeIPPoolGroupName_Type.__name__ = "DisplayString"
_HwDomainIncludeIPPoolGroupName_Object = MibTableColumn
hwDomainIncludeIPPoolGroupName = _HwDomainIncludeIPPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 45, 1, 1),
    _HwDomainIncludeIPPoolGroupName_Type()
)
hwDomainIncludeIPPoolGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIncludeIPPoolGroupName.setStatus("current")
_HwDomainIncludeIPPoolGroupRowStates_Type = RowStatus
_HwDomainIncludeIPPoolGroupRowStates_Object = MibTableColumn
hwDomainIncludeIPPoolGroupRowStates = _HwDomainIncludeIPPoolGroupRowStates_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 45, 1, 2),
    _HwDomainIncludeIPPoolGroupRowStates_Type()
)
hwDomainIncludeIPPoolGroupRowStates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDomainIncludeIPPoolGroupRowStates.setStatus("current")
_HwDomainIPPoolMoveToTable_Object = MibTable
hwDomainIPPoolMoveToTable = _HwDomainIPPoolMoveToTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 46)
)
if mibBuilder.loadTexts:
    hwDomainIPPoolMoveToTable.setStatus("current")
_HwDomainIPPoolMoveToEntry_Object = MibTableRow
hwDomainIPPoolMoveToEntry = _HwDomainIPPoolMoveToEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 46, 1)
)
hwDomainIPPoolMoveToEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwDomainName"),
    (0, "HUAWEI-AAA-MIB", "hwDomainIncludeIPPoolName"),
)
if mibBuilder.loadTexts:
    hwDomainIPPoolMoveToEntry.setStatus("current")


class _HwDomainIncludeIPPoolName_Type(DisplayString):
    """Custom type hwDomainIncludeIPPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDomainIncludeIPPoolName_Type.__name__ = "DisplayString"
_HwDomainIncludeIPPoolName_Object = MibTableColumn
hwDomainIncludeIPPoolName = _HwDomainIncludeIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 46, 1, 1),
    _HwDomainIncludeIPPoolName_Type()
)
hwDomainIncludeIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainIncludeIPPoolName.setStatus("current")


class _HwDomainIncludeIPPoolMoveto_Type(Integer32):
    """Custom type hwDomainIncludeIPPoolMoveto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HwDomainIncludeIPPoolMoveto_Type.__name__ = "Integer32"
_HwDomainIncludeIPPoolMoveto_Object = MibTableColumn
hwDomainIncludeIPPoolMoveto = _HwDomainIncludeIPPoolMoveto_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 46, 1, 2),
    _HwDomainIncludeIPPoolMoveto_Type()
)
hwDomainIncludeIPPoolMoveto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDomainIncludeIPPoolMoveto.setStatus("current")
_HwDomainExt2Table_Object = MibTable
hwDomainExt2Table = _HwDomainExt2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 47)
)
if mibBuilder.loadTexts:
    hwDomainExt2Table.setStatus("current")
_HwDomainExt2Entry_Object = MibTableRow
hwDomainExt2Entry = _HwDomainExt2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 47, 1)
)
hwDomainExt2Entry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwDomainName"),
)
if mibBuilder.loadTexts:
    hwDomainExt2Entry.setStatus("current")


class _HwRedKeyUserMac_Type(DisplayString):
    """Custom type hwRedKeyUserMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwRedKeyUserMac_Type.__name__ = "DisplayString"
_HwRedKeyUserMac_Object = MibTableColumn
hwRedKeyUserMac = _HwRedKeyUserMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 47, 1, 1),
    _HwRedKeyUserMac_Type()
)
hwRedKeyUserMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRedKeyUserMac.setStatus("current")


class _HwIfUserMacSimple_Type(TruthValue):
    """Custom type hwIfUserMacSimple based on TruthValue"""


_HwIfUserMacSimple_Object = MibTableColumn
hwIfUserMacSimple = _HwIfUserMacSimple_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 47, 1, 2),
    _HwIfUserMacSimple_Type()
)
hwIfUserMacSimple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIfUserMacSimple.setStatus("current")


class _HwPoolLowerLimitWarningThreshold_Type(Integer32):
    """Custom type hwPoolLowerLimitWarningThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
        ValueRangeConstraint(255, 255),
    )


_HwPoolLowerLimitWarningThreshold_Type.__name__ = "Integer32"
_HwPoolLowerLimitWarningThreshold_Object = MibTableColumn
hwPoolLowerLimitWarningThreshold = _HwPoolLowerLimitWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 47, 1, 3),
    _HwPoolLowerLimitWarningThreshold_Type()
)
hwPoolLowerLimitWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoolLowerLimitWarningThreshold.setStatus("current")


class _HwIPv6PoolLowerLimitWarningThreshold_Type(Integer32):
    """Custom type hwIPv6PoolLowerLimitWarningThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
        ValueRangeConstraint(255, 255),
    )


_HwIPv6PoolLowerLimitWarningThreshold_Type.__name__ = "Integer32"
_HwIPv6PoolLowerLimitWarningThreshold_Object = MibTableColumn
hwIPv6PoolLowerLimitWarningThreshold = _HwIPv6PoolLowerLimitWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 47, 1, 4),
    _HwIPv6PoolLowerLimitWarningThreshold_Type()
)
hwIPv6PoolLowerLimitWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPv6PoolLowerLimitWarningThreshold.setStatus("current")


class _HwAAADomainInboundQoSProfile_Type(DisplayString):
    """Custom type hwAAADomainInboundQoSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwAAADomainInboundQoSProfile_Type.__name__ = "DisplayString"
_HwAAADomainInboundQoSProfile_Object = MibTableColumn
hwAAADomainInboundQoSProfile = _HwAAADomainInboundQoSProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 47, 1, 5),
    _HwAAADomainInboundQoSProfile_Type()
)
hwAAADomainInboundQoSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAAADomainInboundQoSProfile.setStatus("current")


class _HwAAADomainOutboundQoSProfile_Type(DisplayString):
    """Custom type hwAAADomainOutboundQoSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwAAADomainOutboundQoSProfile_Type.__name__ = "DisplayString"
_HwAAADomainOutboundQoSProfile_Object = MibTableColumn
hwAAADomainOutboundQoSProfile = _HwAAADomainOutboundQoSProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 47, 1, 6),
    _HwAAADomainOutboundQoSProfile_Type()
)
hwAAADomainOutboundQoSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAAADomainOutboundQoSProfile.setStatus("current")


class _HwAAADomainInboundVPNInstance_Type(DisplayString):
    """Custom type hwAAADomainInboundVPNInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwAAADomainInboundVPNInstance_Type.__name__ = "DisplayString"
_HwAAADomainInboundVPNInstance_Object = MibTableColumn
hwAAADomainInboundVPNInstance = _HwAAADomainInboundVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 47, 1, 7),
    _HwAAADomainInboundVPNInstance_Type()
)
hwAAADomainInboundVPNInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAAADomainInboundVPNInstance.setStatus("current")
_HwAAAOnlineFailRecordTable_Object = MibTable
hwAAAOnlineFailRecordTable = _HwAAAOnlineFailRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48)
)
if mibBuilder.loadTexts:
    hwAAAOnlineFailRecordTable.setStatus("current")
_HwAAAOnlineFailRecordEntry_Object = MibTableRow
hwAAAOnlineFailRecordEntry = _HwAAAOnlineFailRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1)
)
hwAAAOnlineFailRecordEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAAAOnlineFailIndex"),
)
if mibBuilder.loadTexts:
    hwAAAOnlineFailRecordEntry.setStatus("current")
_HwAAAOnlineFailIndex_Type = Integer32
_HwAAAOnlineFailIndex_Object = MibTableColumn
hwAAAOnlineFailIndex = _HwAAAOnlineFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 1),
    _HwAAAOnlineFailIndex_Type()
)
hwAAAOnlineFailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAAOnlineFailIndex.setStatus("current")


class _HwUserName_Type(DisplayString):
    """Custom type hwUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_HwUserName_Type.__name__ = "DisplayString"
_HwUserName_Object = MibTableColumn
hwUserName = _HwUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 2),
    _HwUserName_Type()
)
hwUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserName.setStatus("current")


class _HwUserDomainName_Type(DisplayString):
    """Custom type hwUserDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwUserDomainName_Type.__name__ = "DisplayString"
_HwUserDomainName_Object = MibTableColumn
hwUserDomainName = _HwUserDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 3),
    _HwUserDomainName_Type()
)
hwUserDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserDomainName.setStatus("current")
_HwUserMAC_Type = MacAddress
_HwUserMAC_Object = MibTableColumn
hwUserMAC = _HwUserMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 4),
    _HwUserMAC_Type()
)
hwUserMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserMAC.setStatus("current")


class _HwUserAccessType_Type(DisplayString):
    """Custom type hwUserAccessType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwUserAccessType_Type.__name__ = "DisplayString"
_HwUserAccessType_Object = MibTableColumn
hwUserAccessType = _HwUserAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 5),
    _HwUserAccessType_Type()
)
hwUserAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserAccessType.setStatus("current")


class _HwUserInterface_Type(DisplayString):
    """Custom type hwUserInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwUserInterface_Type.__name__ = "DisplayString"
_HwUserInterface_Object = MibTableColumn
hwUserInterface = _HwUserInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 6),
    _HwUserInterface_Type()
)
hwUserInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserInterface.setStatus("current")


class _HwUserAccessPVC_Type(DisplayString):
    """Custom type hwUserAccessPVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwUserAccessPVC_Type.__name__ = "DisplayString"
_HwUserAccessPVC_Object = MibTableColumn
hwUserAccessPVC = _HwUserAccessPVC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 7),
    _HwUserAccessPVC_Type()
)
hwUserAccessPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserAccessPVC.setStatus("current")
_HwUserAccessPeVlan_Type = Integer32
_HwUserAccessPeVlan_Object = MibTableColumn
hwUserAccessPeVlan = _HwUserAccessPeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 8),
    _HwUserAccessPeVlan_Type()
)
hwUserAccessPeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserAccessPeVlan.setStatus("current")
_HwUserAccessCeVlan_Type = Integer32
_HwUserAccessCeVlan_Object = MibTableColumn
hwUserAccessCeVlan = _HwUserAccessCeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 9),
    _HwUserAccessCeVlan_Type()
)
hwUserAccessCeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserAccessCeVlan.setStatus("current")
_HwUserIPAddress_Type = IpAddress
_HwUserIPAddress_Object = MibTableColumn
hwUserIPAddress = _HwUserIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 10),
    _HwUserIPAddress_Type()
)
hwUserIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserIPAddress.setStatus("current")
_HwUserIPv6NDRAPrefix_Type = Ipv6AddressPrefix
_HwUserIPv6NDRAPrefix_Object = MibTableColumn
hwUserIPv6NDRAPrefix = _HwUserIPv6NDRAPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 11),
    _HwUserIPv6NDRAPrefix_Type()
)
hwUserIPv6NDRAPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserIPv6NDRAPrefix.setStatus("current")
_HwUserIPv6Address_Type = Ipv6Address
_HwUserIPv6Address_Object = MibTableColumn
hwUserIPv6Address = _HwUserIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 12),
    _HwUserIPv6Address_Type()
)
hwUserIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserIPv6Address.setStatus("current")
_HwUserIPv6PDPrefix_Type = Ipv6AddressPrefix
_HwUserIPv6PDPrefix_Object = MibTableColumn
hwUserIPv6PDPrefix = _HwUserIPv6PDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 13),
    _HwUserIPv6PDPrefix_Type()
)
hwUserIPv6PDPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserIPv6PDPrefix.setStatus("current")


class _HwUserIPv6PDPrefixLength_Type(Integer32):
    """Custom type hwUserIPv6PDPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwUserIPv6PDPrefixLength_Type.__name__ = "Integer32"
_HwUserIPv6PDPrefixLength_Object = MibTableColumn
hwUserIPv6PDPrefixLength = _HwUserIPv6PDPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 14),
    _HwUserIPv6PDPrefixLength_Type()
)
hwUserIPv6PDPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserIPv6PDPrefixLength.setStatus("current")
_HwUserID_Type = Integer32
_HwUserID_Object = MibTableColumn
hwUserID = _HwUserID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 15),
    _HwUserID_Type()
)
hwUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserID.setStatus("current")


class _HwUserAuthenState_Type(Integer32):
    """Custom type hwUserAuthenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("authIdle", 0),
          ("authWait", 1),
          ("authed", 2),
          ("unknown", 255))
    )


_HwUserAuthenState_Type.__name__ = "Integer32"
_HwUserAuthenState_Object = MibTableColumn
hwUserAuthenState = _HwUserAuthenState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 16),
    _HwUserAuthenState_Type()
)
hwUserAuthenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserAuthenState.setStatus("current")


class _HwUserAcctState_Type(Integer32):
    """Custom type hwUserAcctState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              12,
              255)
        )
    )
    namedValues = NamedValues(
        *(("acctAccting", 6),
          ("acctIdle", 3),
          ("acctLeavingFlowQuery", 7),
          ("acctReady", 4),
          ("acctSendForceStopWait", 12),
          ("acctStartWait", 5),
          ("acctStopWait", 8),
          ("unknown", 255))
    )


_HwUserAcctState_Type.__name__ = "Integer32"
_HwUserAcctState_Object = MibTableColumn
hwUserAcctState = _HwUserAcctState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 17),
    _HwUserAcctState_Type()
)
hwUserAcctState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserAcctState.setStatus("current")


class _HwUserAuthorState_Type(Integer32):
    """Custom type hwUserAuthorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("authorIdle", 9),
          ("authorServerAckWait", 11),
          ("authorUserAckWait", 10),
          ("unknown", 255))
    )


_HwUserAuthorState_Type.__name__ = "Integer32"
_HwUserAuthorState_Object = MibTableColumn
hwUserAuthorState = _HwUserAuthorState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 18),
    _HwUserAuthorState_Type()
)
hwUserAuthorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserAuthorState.setStatus("current")
_HwUserLoginTime_Type = DateAndTime
_HwUserLoginTime_Object = MibTableColumn
hwUserLoginTime = _HwUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 19),
    _HwUserLoginTime_Type()
)
hwUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserLoginTime.setStatus("current")


class _HwOnlineFailReason_Type(DisplayString):
    """Custom type hwOnlineFailReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_HwOnlineFailReason_Type.__name__ = "DisplayString"
_HwOnlineFailReason_Object = MibTableColumn
hwOnlineFailReason = _HwOnlineFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 20),
    _HwOnlineFailReason_Type()
)
hwOnlineFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOnlineFailReason.setStatus("current")


class _HwReplyMessage_Type(DisplayString):
    """Custom type hwReplyMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwReplyMessage_Type.__name__ = "DisplayString"
_HwReplyMessage_Object = MibTableColumn
hwReplyMessage = _HwReplyMessage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 48, 1, 21),
    _HwReplyMessage_Type()
)
hwReplyMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwReplyMessage.setStatus("current")
_HwUserLogTable_ObjectIdentity = ObjectIdentity
hwUserLogTable = _HwUserLogTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 49)
)
_HwUserLogEntry_ObjectIdentity = ObjectIdentity
hwUserLogEntry = _HwUserLogEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 49, 1)
)
_HwUserLogAccess_Type = TruthValue
_HwUserLogAccess_Object = MibScalar
hwUserLogAccess = _HwUserLogAccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 49, 1, 1),
    _HwUserLogAccess_Type()
)
hwUserLogAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserLogAccess.setStatus("current")
_HwUserLogIPAddress_Type = IpAddress
_HwUserLogIPAddress_Object = MibScalar
hwUserLogIPAddress = _HwUserLogIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 49, 1, 2),
    _HwUserLogIPAddress_Type()
)
hwUserLogIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserLogIPAddress.setStatus("current")


class _HwUserLogPort_Type(Integer32):
    """Custom type hwUserLogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwUserLogPort_Type.__name__ = "Integer32"
_HwUserLogPort_Object = MibScalar
hwUserLogPort = _HwUserLogPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 49, 1, 3),
    _HwUserLogPort_Type()
)
hwUserLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserLogPort.setStatus("current")


class _HwUserLogVersion_Type(Integer32):
    """Custom type hwUserLogVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwUserLogVersion_Type.__name__ = "Integer32"
_HwUserLogVersion_Object = MibScalar
hwUserLogVersion = _HwUserLogVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 49, 1, 4),
    _HwUserLogVersion_Type()
)
hwUserLogVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserLogVersion.setStatus("current")
_HwShowUserLogStatistic_Type = Integer32
_HwShowUserLogStatistic_Object = MibScalar
hwShowUserLogStatistic = _HwShowUserLogStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 49, 1, 5),
    _HwShowUserLogStatistic_Type()
)
hwShowUserLogStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwShowUserLogStatistic.setStatus("current")


class _HwResetUserLogStatistic_Type(Integer32):
    """Custom type hwResetUserLogStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )


_HwResetUserLogStatistic_Type.__name__ = "Integer32"
_HwResetUserLogStatistic_Object = MibScalar
hwResetUserLogStatistic = _HwResetUserLogStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 49, 1, 6),
    _HwResetUserLogStatistic_Type()
)
hwResetUserLogStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwResetUserLogStatistic.setStatus("current")
_HwReauthorizeTable_Object = MibTable
hwReauthorizeTable = _HwReauthorizeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 50)
)
if mibBuilder.loadTexts:
    hwReauthorizeTable.setStatus("current")
_HwReauthorizeEntry_Object = MibTableRow
hwReauthorizeEntry = _HwReauthorizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 50, 1)
)
hwReauthorizeEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwReauthorizeUsername"),
)
if mibBuilder.loadTexts:
    hwReauthorizeEntry.setStatus("current")


class _HwReauthorizeUsername_Type(DisplayString):
    """Custom type hwReauthorizeUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_HwReauthorizeUsername_Type.__name__ = "DisplayString"
_HwReauthorizeUsername_Object = MibTableColumn
hwReauthorizeUsername = _HwReauthorizeUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 50, 1, 1),
    _HwReauthorizeUsername_Type()
)
hwReauthorizeUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwReauthorizeUsername.setStatus("current")


class _HwReauthorizeUsergroup_Type(DisplayString):
    """Custom type hwReauthorizeUsergroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwReauthorizeUsergroup_Type.__name__ = "DisplayString"
_HwReauthorizeUsergroup_Object = MibTableColumn
hwReauthorizeUsergroup = _HwReauthorizeUsergroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 50, 1, 2),
    _HwReauthorizeUsergroup_Type()
)
hwReauthorizeUsergroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwReauthorizeUsergroup.setStatus("current")
_HwUserGroupTable_Object = MibTable
hwUserGroupTable = _HwUserGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51)
)
if mibBuilder.loadTexts:
    hwUserGroupTable.setStatus("current")
_HwUserGroupEntry_Object = MibTableRow
hwUserGroupEntry = _HwUserGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1)
)
hwUserGroupEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwUserGroupIndex"),
)
if mibBuilder.loadTexts:
    hwUserGroupEntry.setStatus("current")


class _HwUserGroupIndex_Type(Integer32):
    """Custom type hwUserGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwUserGroupIndex_Type.__name__ = "Integer32"
_HwUserGroupIndex_Object = MibTableColumn
hwUserGroupIndex = _HwUserGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 1),
    _HwUserGroupIndex_Type()
)
hwUserGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserGroupIndex.setStatus("current")


class _HwUserGroupName_Type(DisplayString):
    """Custom type hwUserGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwUserGroupName_Type.__name__ = "DisplayString"
_HwUserGroupName_Object = MibTableColumn
hwUserGroupName = _HwUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 2),
    _HwUserGroupName_Type()
)
hwUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUserGroupName.setStatus("current")


class _HwAclId_Type(DisplayString):
    """Custom type hwAclId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwAclId_Type.__name__ = "DisplayString"
_HwAclId_Object = MibTableColumn
hwAclId = _HwAclId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 3),
    _HwAclId_Type()
)
hwAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclId.setStatus("current")


class _HwQoSProfileName_Type(DisplayString):
    """Custom type hwQoSProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwQoSProfileName_Type.__name__ = "DisplayString"
_HwQoSProfileName_Object = MibTableColumn
hwQoSProfileName = _HwQoSProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 4),
    _HwQoSProfileName_Type()
)
hwQoSProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQoSProfileName.setStatus("current")


class _HwInterIsolateFlag_Type(Integer32):
    """Custom type hwInterIsolateFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HwInterIsolateFlag_Type.__name__ = "Integer32"
_HwInterIsolateFlag_Object = MibTableColumn
hwInterIsolateFlag = _HwInterIsolateFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 5),
    _HwInterIsolateFlag_Type()
)
hwInterIsolateFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwInterIsolateFlag.setStatus("current")


class _HwInnerIsolateFlag_Type(Integer32):
    """Custom type hwInnerIsolateFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HwInnerIsolateFlag_Type.__name__ = "Integer32"
_HwInnerIsolateFlag_Object = MibTableColumn
hwInnerIsolateFlag = _HwInnerIsolateFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 6),
    _HwInnerIsolateFlag_Type()
)
hwInnerIsolateFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwInnerIsolateFlag.setStatus("current")
_HwUserGroupRowStatus_Type = RowStatus
_HwUserGroupRowStatus_Object = MibTableColumn
hwUserGroupRowStatus = _HwUserGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 7),
    _HwUserGroupRowStatus_Type()
)
hwUserGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUserGroupRowStatus.setStatus("current")


class _HwUserVlan_Type(Integer32):
    """Custom type hwUserVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwUserVlan_Type.__name__ = "Integer32"
_HwUserVlan_Object = MibTableColumn
hwUserVlan = _HwUserVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 8),
    _HwUserVlan_Type()
)
hwUserVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUserVlan.setStatus("current")


class _Hw8021pRemark_Type(Integer32):
    """Custom type hw8021pRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_Hw8021pRemark_Type.__name__ = "Integer32"
_Hw8021pRemark_Object = MibTableColumn
hw8021pRemark = _Hw8021pRemark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 9),
    _Hw8021pRemark_Type()
)
hw8021pRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hw8021pRemark.setStatus("current")


class _HwDscpRemark_Type(Integer32):
    """Custom type hwDscpRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_HwDscpRemark_Type.__name__ = "Integer32"
_HwDscpRemark_Object = MibTableColumn
hwDscpRemark = _HwDscpRemark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 10),
    _HwDscpRemark_Type()
)
hwDscpRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDscpRemark.setStatus("current")


class _HwExpRemark_Type(Integer32):
    """Custom type hwExpRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_HwExpRemark_Type.__name__ = "Integer32"
_HwExpRemark_Object = MibTableColumn
hwExpRemark = _HwExpRemark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 11),
    _HwExpRemark_Type()
)
hwExpRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwExpRemark.setStatus("current")


class _HwLpRemark_Type(Integer32):
    """Custom type hwLpRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_HwLpRemark_Type.__name__ = "Integer32"
_HwLpRemark_Object = MibTableColumn
hwLpRemark = _HwLpRemark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 12),
    _HwLpRemark_Type()
)
hwLpRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLpRemark.setStatus("current")
_HwUserGroupCarCir_Type = Unsigned32
_HwUserGroupCarCir_Object = MibTableColumn
hwUserGroupCarCir = _HwUserGroupCarCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 13),
    _HwUserGroupCarCir_Type()
)
hwUserGroupCarCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserGroupCarCir.setStatus("current")
_HwUserGroupCarPir_Type = Unsigned32
_HwUserGroupCarPir_Object = MibTableColumn
hwUserGroupCarPir = _HwUserGroupCarPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 14),
    _HwUserGroupCarPir_Type()
)
hwUserGroupCarPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserGroupCarPir.setStatus("current")
_HwUserGroupCarCbs_Type = Unsigned32
_HwUserGroupCarCbs_Object = MibTableColumn
hwUserGroupCarCbs = _HwUserGroupCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 15),
    _HwUserGroupCarCbs_Type()
)
hwUserGroupCarCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserGroupCarCbs.setStatus("current")
_HwUserGroupCarPbs_Type = Unsigned32
_HwUserGroupCarPbs_Object = MibTableColumn
hwUserGroupCarPbs = _HwUserGroupCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 16),
    _HwUserGroupCarPbs_Type()
)
hwUserGroupCarPbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserGroupCarPbs.setStatus("current")


class _HwUserGroupEnable_Type(Integer32):
    """Custom type hwUserGroupEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwUserGroupEnable_Type.__name__ = "Integer32"
_HwUserGroupEnable_Object = MibTableColumn
hwUserGroupEnable = _HwUserGroupEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 17),
    _HwUserGroupEnable_Type()
)
hwUserGroupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserGroupEnable.setStatus("current")
_HwUserGroupCarInBoundCir_Type = Unsigned32
_HwUserGroupCarInBoundCir_Object = MibTableColumn
hwUserGroupCarInBoundCir = _HwUserGroupCarInBoundCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 18),
    _HwUserGroupCarInBoundCir_Type()
)
hwUserGroupCarInBoundCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserGroupCarInBoundCir.setStatus("current")
_HwUserGroupCarInBoundPir_Type = Unsigned32
_HwUserGroupCarInBoundPir_Object = MibTableColumn
hwUserGroupCarInBoundPir = _HwUserGroupCarInBoundPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 19),
    _HwUserGroupCarInBoundPir_Type()
)
hwUserGroupCarInBoundPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserGroupCarInBoundPir.setStatus("current")
_HwUserGroupCarInBoundCbs_Type = Unsigned32
_HwUserGroupCarInBoundCbs_Object = MibTableColumn
hwUserGroupCarInBoundCbs = _HwUserGroupCarInBoundCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 20),
    _HwUserGroupCarInBoundCbs_Type()
)
hwUserGroupCarInBoundCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserGroupCarInBoundCbs.setStatus("current")
_HwUserGroupCarInBoundPbs_Type = Unsigned32
_HwUserGroupCarInBoundPbs_Object = MibTableColumn
hwUserGroupCarInBoundPbs = _HwUserGroupCarInBoundPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 21),
    _HwUserGroupCarInBoundPbs_Type()
)
hwUserGroupCarInBoundPbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserGroupCarInBoundPbs.setStatus("current")


class _HwUserGroupUserVlanPool_Type(DisplayString):
    """Custom type hwUserGroupUserVlanPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwUserGroupUserVlanPool_Type.__name__ = "DisplayString"
_HwUserGroupUserVlanPool_Object = MibTableColumn
hwUserGroupUserVlanPool = _HwUserGroupUserVlanPool_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 51, 1, 22),
    _HwUserGroupUserVlanPool_Type()
)
hwUserGroupUserVlanPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUserGroupUserVlanPool.setStatus("current")
_HwAAAOfflineRecordTable_Object = MibTable
hwAAAOfflineRecordTable = _HwAAAOfflineRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52)
)
if mibBuilder.loadTexts:
    hwAAAOfflineRecordTable.setStatus("current")
_HwAAAOfflineRecordEntry_Object = MibTableRow
hwAAAOfflineRecordEntry = _HwAAAOfflineRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1)
)
hwAAAOfflineRecordEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAAAOfflineIndex"),
)
if mibBuilder.loadTexts:
    hwAAAOfflineRecordEntry.setStatus("current")
_HwAAAOfflineIndex_Type = Integer32
_HwAAAOfflineIndex_Object = MibTableColumn
hwAAAOfflineIndex = _HwAAAOfflineIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 1),
    _HwAAAOfflineIndex_Type()
)
hwAAAOfflineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAAOfflineIndex.setStatus("current")


class _HwOfflineRecordUserName_Type(DisplayString):
    """Custom type hwOfflineRecordUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_HwOfflineRecordUserName_Type.__name__ = "DisplayString"
_HwOfflineRecordUserName_Object = MibTableColumn
hwOfflineRecordUserName = _HwOfflineRecordUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 2),
    _HwOfflineRecordUserName_Type()
)
hwOfflineRecordUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordUserName.setStatus("current")


class _HwOfflineRecordDomainName_Type(DisplayString):
    """Custom type hwOfflineRecordDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwOfflineRecordDomainName_Type.__name__ = "DisplayString"
_HwOfflineRecordDomainName_Object = MibTableColumn
hwOfflineRecordDomainName = _HwOfflineRecordDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 3),
    _HwOfflineRecordDomainName_Type()
)
hwOfflineRecordDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordDomainName.setStatus("current")
_HwOfflineRecordUserMAC_Type = MacAddress
_HwOfflineRecordUserMAC_Object = MibTableColumn
hwOfflineRecordUserMAC = _HwOfflineRecordUserMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 4),
    _HwOfflineRecordUserMAC_Type()
)
hwOfflineRecordUserMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordUserMAC.setStatus("current")


class _HwOfflineRecordAccessType_Type(DisplayString):
    """Custom type hwOfflineRecordAccessType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwOfflineRecordAccessType_Type.__name__ = "DisplayString"
_HwOfflineRecordAccessType_Object = MibTableColumn
hwOfflineRecordAccessType = _HwOfflineRecordAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 5),
    _HwOfflineRecordAccessType_Type()
)
hwOfflineRecordAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordAccessType.setStatus("current")


class _HwOfflineRecordInterface_Type(DisplayString):
    """Custom type hwOfflineRecordInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwOfflineRecordInterface_Type.__name__ = "DisplayString"
_HwOfflineRecordInterface_Object = MibTableColumn
hwOfflineRecordInterface = _HwOfflineRecordInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 6),
    _HwOfflineRecordInterface_Type()
)
hwOfflineRecordInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordInterface.setStatus("current")
_HwOfflineRecordAccessPeVlan_Type = Integer32
_HwOfflineRecordAccessPeVlan_Object = MibTableColumn
hwOfflineRecordAccessPeVlan = _HwOfflineRecordAccessPeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 7),
    _HwOfflineRecordAccessPeVlan_Type()
)
hwOfflineRecordAccessPeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordAccessPeVlan.setStatus("current")
_HwOfflineRecordAccessCeVlan_Type = Integer32
_HwOfflineRecordAccessCeVlan_Object = MibTableColumn
hwOfflineRecordAccessCeVlan = _HwOfflineRecordAccessCeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 8),
    _HwOfflineRecordAccessCeVlan_Type()
)
hwOfflineRecordAccessCeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordAccessCeVlan.setStatus("current")
_HwOfflineRecordIPAddress_Type = IpAddress
_HwOfflineRecordIPAddress_Object = MibTableColumn
hwOfflineRecordIPAddress = _HwOfflineRecordIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 9),
    _HwOfflineRecordIPAddress_Type()
)
hwOfflineRecordIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordIPAddress.setStatus("current")
_HwOfflineRecordUserID_Type = Integer32
_HwOfflineRecordUserID_Object = MibTableColumn
hwOfflineRecordUserID = _HwOfflineRecordUserID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 10),
    _HwOfflineRecordUserID_Type()
)
hwOfflineRecordUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordUserID.setStatus("current")
_HwOfflineRecordUserLoginTime_Type = DateAndTime
_HwOfflineRecordUserLoginTime_Object = MibTableColumn
hwOfflineRecordUserLoginTime = _HwOfflineRecordUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 11),
    _HwOfflineRecordUserLoginTime_Type()
)
hwOfflineRecordUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordUserLoginTime.setStatus("current")
_HwOfflineRecordUserLogoutTime_Type = DateAndTime
_HwOfflineRecordUserLogoutTime_Object = MibTableColumn
hwOfflineRecordUserLogoutTime = _HwOfflineRecordUserLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 12),
    _HwOfflineRecordUserLogoutTime_Type()
)
hwOfflineRecordUserLogoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordUserLogoutTime.setStatus("current")


class _HwOfflineRecordOfflineReason_Type(DisplayString):
    """Custom type hwOfflineRecordOfflineReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwOfflineRecordOfflineReason_Type.__name__ = "DisplayString"
_HwOfflineRecordOfflineReason_Object = MibTableColumn
hwOfflineRecordOfflineReason = _HwOfflineRecordOfflineReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 52, 1, 13),
    _HwOfflineRecordOfflineReason_Type()
)
hwOfflineRecordOfflineReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOfflineRecordOfflineReason.setStatus("current")


class _HwGlobalDhcpOpt64SepAndSeg_Type(DisplayString):
    """Custom type hwGlobalDhcpOpt64SepAndSeg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_HwGlobalDhcpOpt64SepAndSeg_Type.__name__ = "DisplayString"
_HwGlobalDhcpOpt64SepAndSeg_Object = MibScalar
hwGlobalDhcpOpt64SepAndSeg = _HwGlobalDhcpOpt64SepAndSeg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 53),
    _HwGlobalDhcpOpt64SepAndSeg_Type()
)
hwGlobalDhcpOpt64SepAndSeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGlobalDhcpOpt64SepAndSeg.setStatus("current")
_HwGlobalDhcpServerAck_Type = TruthValue
_HwGlobalDhcpServerAck_Object = MibScalar
hwGlobalDhcpServerAck = _HwGlobalDhcpServerAck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 54),
    _HwGlobalDhcpServerAck_Type()
)
hwGlobalDhcpServerAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGlobalDhcpServerAck.setStatus("current")
_HwAuthEventCfgTable_Object = MibTable
hwAuthEventCfgTable = _HwAuthEventCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55)
)
if mibBuilder.loadTexts:
    hwAuthEventCfgTable.setStatus("current")
_HwAuthEventCfgEntry_Object = MibTableRow
hwAuthEventCfgEntry = _HwAuthEventCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1)
)
hwAuthEventCfgEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAuthEventPortIndex"),
)
if mibBuilder.loadTexts:
    hwAuthEventCfgEntry.setStatus("current")


class _HwAuthEventPortIndex_Type(Unsigned32):
    """Custom type hwAuthEventPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwAuthEventPortIndex_Type.__name__ = "Unsigned32"
_HwAuthEventPortIndex_Object = MibTableColumn
hwAuthEventPortIndex = _HwAuthEventPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 1),
    _HwAuthEventPortIndex_Type()
)
hwAuthEventPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthEventPortIndex.setStatus("current")


class _HwAuthEventAuthFailResponseFail_Type(Integer32):
    """Custom type hwAuthEventAuthFailResponseFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabel", 2),
          ("enable", 1))
    )


_HwAuthEventAuthFailResponseFail_Type.__name__ = "Integer32"
_HwAuthEventAuthFailResponseFail_Object = MibTableColumn
hwAuthEventAuthFailResponseFail = _HwAuthEventAuthFailResponseFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 2),
    _HwAuthEventAuthFailResponseFail_Type()
)
hwAuthEventAuthFailResponseFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventAuthFailResponseFail.setStatus("current")


class _HwAuthEventAuthFailVlan_Type(Integer32):
    """Custom type hwAuthEventAuthFailVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwAuthEventAuthFailVlan_Type.__name__ = "Integer32"
_HwAuthEventAuthFailVlan_Object = MibTableColumn
hwAuthEventAuthFailVlan = _HwAuthEventAuthFailVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 3),
    _HwAuthEventAuthFailVlan_Type()
)
hwAuthEventAuthFailVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventAuthFailVlan.setStatus("current")


class _HwAuthEventAuthenServerDownResponseFail_Type(Integer32):
    """Custom type hwAuthEventAuthenServerDownResponseFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwAuthEventAuthenServerDownResponseFail_Type.__name__ = "Integer32"
_HwAuthEventAuthenServerDownResponseFail_Object = MibTableColumn
hwAuthEventAuthenServerDownResponseFail = _HwAuthEventAuthenServerDownResponseFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 4),
    _HwAuthEventAuthenServerDownResponseFail_Type()
)
hwAuthEventAuthenServerDownResponseFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventAuthenServerDownResponseFail.setStatus("current")


class _HwAuthEventAuthenServerDownVlan_Type(Integer32):
    """Custom type hwAuthEventAuthenServerDownVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwAuthEventAuthenServerDownVlan_Type.__name__ = "Integer32"
_HwAuthEventAuthenServerDownVlan_Object = MibTableColumn
hwAuthEventAuthenServerDownVlan = _HwAuthEventAuthenServerDownVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 5),
    _HwAuthEventAuthenServerDownVlan_Type()
)
hwAuthEventAuthenServerDownVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventAuthenServerDownVlan.setStatus("current")


class _HwAuthEventClientNoResponseVlan_Type(Integer32):
    """Custom type hwAuthEventClientNoResponseVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwAuthEventClientNoResponseVlan_Type.__name__ = "Integer32"
_HwAuthEventClientNoResponseVlan_Object = MibTableColumn
hwAuthEventClientNoResponseVlan = _HwAuthEventClientNoResponseVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 6),
    _HwAuthEventClientNoResponseVlan_Type()
)
hwAuthEventClientNoResponseVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventClientNoResponseVlan.setStatus("current")


class _HwAuthEventPreAuthVlan_Type(Integer32):
    """Custom type hwAuthEventPreAuthVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwAuthEventPreAuthVlan_Type.__name__ = "Integer32"
_HwAuthEventPreAuthVlan_Object = MibTableColumn
hwAuthEventPreAuthVlan = _HwAuthEventPreAuthVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 7),
    _HwAuthEventPreAuthVlan_Type()
)
hwAuthEventPreAuthVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventPreAuthVlan.setStatus("current")


class _HwAuthEventAuthFailUserGroup_Type(OctetString):
    """Custom type hwAuthEventAuthFailUserGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwAuthEventAuthFailUserGroup_Type.__name__ = "OctetString"
_HwAuthEventAuthFailUserGroup_Object = MibTableColumn
hwAuthEventAuthFailUserGroup = _HwAuthEventAuthFailUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 8),
    _HwAuthEventAuthFailUserGroup_Type()
)
hwAuthEventAuthFailUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventAuthFailUserGroup.setStatus("current")


class _HwAuthEventAuthenServerDownUserGroup_Type(OctetString):
    """Custom type hwAuthEventAuthenServerDownUserGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwAuthEventAuthenServerDownUserGroup_Type.__name__ = "OctetString"
_HwAuthEventAuthenServerDownUserGroup_Object = MibTableColumn
hwAuthEventAuthenServerDownUserGroup = _HwAuthEventAuthenServerDownUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 9),
    _HwAuthEventAuthenServerDownUserGroup_Type()
)
hwAuthEventAuthenServerDownUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventAuthenServerDownUserGroup.setStatus("current")


class _HwAuthEventClientNoResponseUserGroup_Type(OctetString):
    """Custom type hwAuthEventClientNoResponseUserGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwAuthEventClientNoResponseUserGroup_Type.__name__ = "OctetString"
_HwAuthEventClientNoResponseUserGroup_Object = MibTableColumn
hwAuthEventClientNoResponseUserGroup = _HwAuthEventClientNoResponseUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 10),
    _HwAuthEventClientNoResponseUserGroup_Type()
)
hwAuthEventClientNoResponseUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventClientNoResponseUserGroup.setStatus("current")


class _HwAuthEventPreAuthUserGroup_Type(OctetString):
    """Custom type hwAuthEventPreAuthUserGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwAuthEventPreAuthUserGroup_Type.__name__ = "OctetString"
_HwAuthEventPreAuthUserGroup_Object = MibTableColumn
hwAuthEventPreAuthUserGroup = _HwAuthEventPreAuthUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 55, 1, 11),
    _HwAuthEventPreAuthUserGroup_Type()
)
hwAuthEventPreAuthUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAuthEventPreAuthUserGroup.setStatus("current")
_HwWlanInterfaceTable_Object = MibTable
hwWlanInterfaceTable = _HwWlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 56)
)
if mibBuilder.loadTexts:
    hwWlanInterfaceTable.setStatus("current")
_HwWlanInterfaceEntry_Object = MibTableRow
hwWlanInterfaceEntry = _HwWlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 56, 1)
)
hwWlanInterfaceEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwWlanInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwWlanInterfaceEntry.setStatus("current")


class _HwWlanInterfaceIndex_Type(Integer32):
    """Custom type hwWlanInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwWlanInterfaceIndex_Type.__name__ = "Integer32"
_HwWlanInterfaceIndex_Object = MibTableColumn
hwWlanInterfaceIndex = _HwWlanInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 56, 1, 1),
    _HwWlanInterfaceIndex_Type()
)
hwWlanInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanInterfaceIndex.setStatus("current")


class _HwWlanInterfaceName_Type(DisplayString):
    """Custom type hwWlanInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwWlanInterfaceName_Type.__name__ = "DisplayString"
_HwWlanInterfaceName_Object = MibTableColumn
hwWlanInterfaceName = _HwWlanInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 56, 1, 2),
    _HwWlanInterfaceName_Type()
)
hwWlanInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanInterfaceName.setStatus("current")


class _HwWlanInterfaceDomainNameDelimiter_Type(DisplayString):
    """Custom type hwWlanInterfaceDomainNameDelimiter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HwWlanInterfaceDomainNameDelimiter_Type.__name__ = "DisplayString"
_HwWlanInterfaceDomainNameDelimiter_Object = MibTableColumn
hwWlanInterfaceDomainNameDelimiter = _HwWlanInterfaceDomainNameDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 56, 1, 3),
    _HwWlanInterfaceDomainNameDelimiter_Type()
)
hwWlanInterfaceDomainNameDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanInterfaceDomainNameDelimiter.setStatus("current")


class _HwWlanInterfaceDomainNameSecurityDelimiter_Type(DisplayString):
    """Custom type hwWlanInterfaceDomainNameSecurityDelimiter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HwWlanInterfaceDomainNameSecurityDelimiter_Type.__name__ = "DisplayString"
_HwWlanInterfaceDomainNameSecurityDelimiter_Object = MibTableColumn
hwWlanInterfaceDomainNameSecurityDelimiter = _HwWlanInterfaceDomainNameSecurityDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 56, 1, 4),
    _HwWlanInterfaceDomainNameSecurityDelimiter_Type()
)
hwWlanInterfaceDomainNameSecurityDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanInterfaceDomainNameSecurityDelimiter.setStatus("current")


class _HwWlanInterfaceDomainNameParseDirection_Type(Integer32):
    """Custom type hwWlanInterfaceDomainNameParseDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("lefttoright", 0),
          ("righttoleft", 1))
    )


_HwWlanInterfaceDomainNameParseDirection_Type.__name__ = "Integer32"
_HwWlanInterfaceDomainNameParseDirection_Object = MibTableColumn
hwWlanInterfaceDomainNameParseDirection = _HwWlanInterfaceDomainNameParseDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 56, 1, 5),
    _HwWlanInterfaceDomainNameParseDirection_Type()
)
hwWlanInterfaceDomainNameParseDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanInterfaceDomainNameParseDirection.setStatus("current")


class _HwWlanInterfaceDomainNameLocation_Type(Integer32):
    """Custom type hwWlanInterfaceDomainNameLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("afterdelimiter", 1),
          ("beforedelimiter", 0),
          ("invalid", 2))
    )


_HwWlanInterfaceDomainNameLocation_Type.__name__ = "Integer32"
_HwWlanInterfaceDomainNameLocation_Object = MibTableColumn
hwWlanInterfaceDomainNameLocation = _HwWlanInterfaceDomainNameLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 56, 1, 6),
    _HwWlanInterfaceDomainNameLocation_Type()
)
hwWlanInterfaceDomainNameLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanInterfaceDomainNameLocation.setStatus("current")
_HwAuthorCmdTable_Object = MibTable
hwAuthorCmdTable = _HwAuthorCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 57)
)
if mibBuilder.loadTexts:
    hwAuthorCmdTable.setStatus("current")
_HwAuthorCmdEntry_Object = MibTableRow
hwAuthorCmdEntry = _HwAuthorCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 57, 1)
)
hwAuthorCmdEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAuthorSchemeName"),
    (0, "HUAWEI-AAA-MIB", "hwAuthorCmdLevel"),
)
if mibBuilder.loadTexts:
    hwAuthorCmdEntry.setStatus("current")


class _HwAuthorCmdLevel_Type(Integer32):
    """Custom type hwAuthorCmdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwAuthorCmdLevel_Type.__name__ = "Integer32"
_HwAuthorCmdLevel_Object = MibTableColumn
hwAuthorCmdLevel = _HwAuthorCmdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 57, 1, 1),
    _HwAuthorCmdLevel_Type()
)
hwAuthorCmdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthorCmdLevel.setStatus("current")


class _HwAuthorCmdMode_Type(Integer32):
    """Custom type hwAuthorCmdMode based on Integer32"""
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
        *(("hwtacacs", 0),
          ("hwtacacslocal", 2),
          ("hwtacacslocalnone", 3),
          ("hwtacacsnone", 1))
    )


_HwAuthorCmdMode_Type.__name__ = "Integer32"
_HwAuthorCmdMode_Object = MibTableColumn
hwAuthorCmdMode = _HwAuthorCmdMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 57, 1, 2),
    _HwAuthorCmdMode_Type()
)
hwAuthorCmdMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAuthorCmdMode.setStatus("current")
_HwAuthorCmdRowStatus_Type = RowStatus
_HwAuthorCmdRowStatus_Object = MibTableColumn
hwAuthorCmdRowStatus = _HwAuthorCmdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 57, 1, 3),
    _HwAuthorCmdRowStatus_Type()
)
hwAuthorCmdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAuthorCmdRowStatus.setStatus("current")
_HwAAARateTable_Object = MibTable
hwAAARateTable = _HwAAARateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 58)
)
if mibBuilder.loadTexts:
    hwAAARateTable.setStatus("current")
_HwAAARateEntry_Object = MibTableRow
hwAAARateEntry = _HwAAARateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 58, 1)
)
hwAAARateEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAAARateDirection"),
    (0, "HUAWEI-AAA-MIB", "hwAAARateType"),
)
if mibBuilder.loadTexts:
    hwAAARateEntry.setStatus("current")


class _HwAAARateDirection_Type(Integer32):
    """Custom type hwAAARateDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwAAARateDirection_Type.__name__ = "Integer32"
_HwAAARateDirection_Object = MibTableColumn
hwAAARateDirection = _HwAAARateDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 58, 1, 1),
    _HwAAARateDirection_Type()
)
hwAAARateDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAARateDirection.setStatus("current")
_HwAAARateType_Type = Integer32
_HwAAARateType_Object = MibTableColumn
hwAAARateType = _HwAAARateType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 58, 1, 2),
    _HwAAARateType_Type()
)
hwAAARateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAARateType.setStatus("current")
_HwAAARateRealPeak_Type = Integer32
_HwAAARateRealPeak_Object = MibTableColumn
hwAAARateRealPeak = _HwAAARateRealPeak_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 58, 1, 3),
    _HwAAARateRealPeak_Type()
)
hwAAARateRealPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAARateRealPeak.setStatus("current")
_HwAAARateRealAverage_Type = Integer32
_HwAAARateRealAverage_Object = MibTableColumn
hwAAARateRealAverage = _HwAAARateRealAverage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 58, 1, 4),
    _HwAAARateRealAverage_Type()
)
hwAAARateRealAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAARateRealAverage.setStatus("current")
_HwAAARateRealUsedCount_Type = Integer32
_HwAAARateRealUsedCount_Object = MibTableColumn
hwAAARateRealUsedCount = _HwAAARateRealUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 58, 1, 5),
    _HwAAARateRealUsedCount_Type()
)
hwAAARateRealUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAARateRealUsedCount.setStatus("current")


class _HwAAARateRealPercent_Type(Integer32):
    """Custom type hwAAARateRealPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwAAARateRealPercent_Type.__name__ = "Integer32"
_HwAAARateRealPercent_Object = MibTableColumn
hwAAARateRealPercent = _HwAAARateRealPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 58, 1, 6),
    _HwAAARateRealPercent_Type()
)
hwAAARateRealPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAARateRealPercent.setStatus("current")
_HwLocalUserPwPolicyAdmin_ObjectIdentity = ObjectIdentity
hwLocalUserPwPolicyAdmin = _HwLocalUserPwPolicyAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 59)
)
_HwLocalUserPwPolicyAdminEntry_ObjectIdentity = ObjectIdentity
hwLocalUserPwPolicyAdminEntry = _HwLocalUserPwPolicyAdminEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 59, 1)
)


class _HwAdminEnable_Type(Integer32):
    """Custom type hwAdminEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwAdminEnable_Type.__name__ = "Integer32"
_HwAdminEnable_Object = MibScalar
hwAdminEnable = _HwAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 59, 1, 1),
    _HwAdminEnable_Type()
)
hwAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAdminEnable.setStatus("current")


class _HwAdminExpire_Type(Integer32):
    """Custom type hwAdminExpire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_HwAdminExpire_Type.__name__ = "Integer32"
_HwAdminExpire_Object = MibScalar
hwAdminExpire = _HwAdminExpire_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 59, 1, 2),
    _HwAdminExpire_Type()
)
hwAdminExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAdminExpire.setStatus("current")


class _HwAdminPwHistroyRecordNum_Type(Integer32):
    """Custom type hwAdminPwHistroyRecordNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_HwAdminPwHistroyRecordNum_Type.__name__ = "Integer32"
_HwAdminPwHistroyRecordNum_Object = MibScalar
hwAdminPwHistroyRecordNum = _HwAdminPwHistroyRecordNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 59, 1, 3),
    _HwAdminPwHistroyRecordNum_Type()
)
hwAdminPwHistroyRecordNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAdminPwHistroyRecordNum.setStatus("current")


class _HwAdminAlertBefore_Type(Integer32):
    """Custom type hwAdminAlertBefore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_HwAdminAlertBefore_Type.__name__ = "Integer32"
_HwAdminAlertBefore_Object = MibScalar
hwAdminAlertBefore = _HwAdminAlertBefore_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 59, 1, 4),
    _HwAdminAlertBefore_Type()
)
hwAdminAlertBefore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAdminAlertBefore.setStatus("current")


class _HwAdminAlertOrginal_Type(Integer32):
    """Custom type hwAdminAlertOrginal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwAdminAlertOrginal_Type.__name__ = "Integer32"
_HwAdminAlertOrginal_Object = MibScalar
hwAdminAlertOrginal = _HwAdminAlertOrginal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 59, 1, 5),
    _HwAdminAlertOrginal_Type()
)
hwAdminAlertOrginal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAdminAlertOrginal.setStatus("current")
_HwLocalUserPwPolicyAcc_ObjectIdentity = ObjectIdentity
hwLocalUserPwPolicyAcc = _HwLocalUserPwPolicyAcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 60)
)
_HwLocalUserPwPolicyAccEntry_ObjectIdentity = ObjectIdentity
hwLocalUserPwPolicyAccEntry = _HwLocalUserPwPolicyAccEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 60, 1)
)


class _HwAccEnable_Type(Integer32):
    """Custom type hwAccEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwAccEnable_Type.__name__ = "Integer32"
_HwAccEnable_Object = MibScalar
hwAccEnable = _HwAccEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 60, 1, 1),
    _HwAccEnable_Type()
)
hwAccEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccEnable.setStatus("current")


class _HwAccPwHistroyRecordNum_Type(Integer32):
    """Custom type hwAccPwHistroyRecordNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_HwAccPwHistroyRecordNum_Type.__name__ = "Integer32"
_HwAccPwHistroyRecordNum_Object = MibScalar
hwAccPwHistroyRecordNum = _HwAccPwHistroyRecordNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 60, 1, 2),
    _HwAccPwHistroyRecordNum_Type()
)
hwAccPwHistroyRecordNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAccPwHistroyRecordNum.setStatus("current")
_HwAAADomainIPPoolTable_Object = MibTable
hwAAADomainIPPoolTable = _HwAAADomainIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 61)
)
if mibBuilder.loadTexts:
    hwAAADomainIPPoolTable.setStatus("current")
_HwAAADomainIPPoolEntry_Object = MibTableRow
hwAAADomainIPPoolEntry = _HwAAADomainIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 61, 1)
)
hwAAADomainIPPoolEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwDomainName"),
    (0, "HUAWEI-AAA-MIB", "hwAAADomainIPPoolName"),
)
if mibBuilder.loadTexts:
    hwAAADomainIPPoolEntry.setStatus("current")


class _HwAAADomainIPPoolName_Type(OctetString):
    """Custom type hwAAADomainIPPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwAAADomainIPPoolName_Type.__name__ = "OctetString"
_HwAAADomainIPPoolName_Object = MibTableColumn
hwAAADomainIPPoolName = _HwAAADomainIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 61, 1, 1),
    _HwAAADomainIPPoolName_Type()
)
hwAAADomainIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAADomainIPPoolName.setStatus("current")
_HwAAADomainIPPoolIndex_Type = Integer32
_HwAAADomainIPPoolIndex_Object = MibTableColumn
hwAAADomainIPPoolIndex = _HwAAADomainIPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 61, 1, 2),
    _HwAAADomainIPPoolIndex_Type()
)
hwAAADomainIPPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAADomainIPPoolIndex.setStatus("current")


class _HwAAADomainIPPoolConstantIndex_Type(Integer32):
    """Custom type hwAAADomainIPPoolConstantIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwAAADomainIPPoolConstantIndex_Type.__name__ = "Integer32"
_HwAAADomainIPPoolConstantIndex_Object = MibTableColumn
hwAAADomainIPPoolConstantIndex = _HwAAADomainIPPoolConstantIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 61, 1, 3),
    _HwAAADomainIPPoolConstantIndex_Type()
)
hwAAADomainIPPoolConstantIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAADomainIPPoolConstantIndex.setStatus("current")


class _HwAAADomainIPPoolPosition_Type(Integer32):
    """Custom type hwAAADomainIPPoolPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwAAADomainIPPoolPosition_Type.__name__ = "Integer32"
_HwAAADomainIPPoolPosition_Object = MibTableColumn
hwAAADomainIPPoolPosition = _HwAAADomainIPPoolPosition_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 61, 1, 4),
    _HwAAADomainIPPoolPosition_Type()
)
hwAAADomainIPPoolPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAAADomainIPPoolPosition.setStatus("current")
_HwAAADomainIPPoolRowStatus_Type = RowStatus
_HwAAADomainIPPoolRowStatus_Object = MibTableColumn
hwAAADomainIPPoolRowStatus = _HwAAADomainIPPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 61, 1, 50),
    _HwAAADomainIPPoolRowStatus_Type()
)
hwAAADomainIPPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAAADomainIPPoolRowStatus.setStatus("current")
_UserAuthenProfileTable_Object = MibTable
userAuthenProfileTable = _UserAuthenProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62)
)
if mibBuilder.loadTexts:
    userAuthenProfileTable.setStatus("current")
_UserAuthenProfileEntry_Object = MibTableRow
userAuthenProfileEntry = _UserAuthenProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1)
)
userAuthenProfileEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "userAuthenProfileName"),
)
if mibBuilder.loadTexts:
    userAuthenProfileEntry.setStatus("current")


class _UserAuthenProfileName_Type(OctetString):
    """Custom type userAuthenProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_UserAuthenProfileName_Type.__name__ = "OctetString"
_UserAuthenProfileName_Object = MibTableColumn
userAuthenProfileName = _UserAuthenProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 1),
    _UserAuthenProfileName_Type()
)
userAuthenProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenProfileName.setStatus("current")


class _UserAuthenProfileDot1xAccessProfileName_Type(OctetString):
    """Custom type userAuthenProfileDot1xAccessProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_UserAuthenProfileDot1xAccessProfileName_Type.__name__ = "OctetString"
_UserAuthenProfileDot1xAccessProfileName_Object = MibTableColumn
userAuthenProfileDot1xAccessProfileName = _UserAuthenProfileDot1xAccessProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 2),
    _UserAuthenProfileDot1xAccessProfileName_Type()
)
userAuthenProfileDot1xAccessProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileDot1xAccessProfileName.setStatus("current")


class _UserAuthenProfileMacAuthenAccessProfileName_Type(OctetString):
    """Custom type userAuthenProfileMacAuthenAccessProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_UserAuthenProfileMacAuthenAccessProfileName_Type.__name__ = "OctetString"
_UserAuthenProfileMacAuthenAccessProfileName_Object = MibTableColumn
userAuthenProfileMacAuthenAccessProfileName = _UserAuthenProfileMacAuthenAccessProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 3),
    _UserAuthenProfileMacAuthenAccessProfileName_Type()
)
userAuthenProfileMacAuthenAccessProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileMacAuthenAccessProfileName.setStatus("current")


class _UserAuthenProfilePortalAccessProfileName_Type(OctetString):
    """Custom type userAuthenProfilePortalAccessProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_UserAuthenProfilePortalAccessProfileName_Type.__name__ = "OctetString"
_UserAuthenProfilePortalAccessProfileName_Object = MibTableColumn
userAuthenProfilePortalAccessProfileName = _UserAuthenProfilePortalAccessProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 4),
    _UserAuthenProfilePortalAccessProfileName_Type()
)
userAuthenProfilePortalAccessProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfilePortalAccessProfileName.setStatus("current")
_UserAuthenProfileSingleAccess_Type = TruthValue
_UserAuthenProfileSingleAccess_Object = MibTableColumn
userAuthenProfileSingleAccess = _UserAuthenProfileSingleAccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 5),
    _UserAuthenProfileSingleAccess_Type()
)
userAuthenProfileSingleAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileSingleAccess.setStatus("current")


class _UserAuthenProfilePreAuthenServiceSchemeName_Type(OctetString):
    """Custom type userAuthenProfilePreAuthenServiceSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthenProfilePreAuthenServiceSchemeName_Type.__name__ = "OctetString"
_UserAuthenProfilePreAuthenServiceSchemeName_Object = MibTableColumn
userAuthenProfilePreAuthenServiceSchemeName = _UserAuthenProfilePreAuthenServiceSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 6),
    _UserAuthenProfilePreAuthenServiceSchemeName_Type()
)
userAuthenProfilePreAuthenServiceSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfilePreAuthenServiceSchemeName.setStatus("current")


class _UserAuthenProfilePreAuthenUserGroupName_Type(OctetString):
    """Custom type userAuthenProfilePreAuthenUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfilePreAuthenUserGroupName_Type.__name__ = "OctetString"
_UserAuthenProfilePreAuthenUserGroupName_Object = MibTableColumn
userAuthenProfilePreAuthenUserGroupName = _UserAuthenProfilePreAuthenUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 7),
    _UserAuthenProfilePreAuthenUserGroupName_Type()
)
userAuthenProfilePreAuthenUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfilePreAuthenUserGroupName.setStatus("current")


class _UserAuthenProfilePreAuthenVLAN_Type(Integer32):
    """Custom type userAuthenProfilePreAuthenVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_UserAuthenProfilePreAuthenVLAN_Type.__name__ = "Integer32"
_UserAuthenProfilePreAuthenVLAN_Object = MibTableColumn
userAuthenProfilePreAuthenVLAN = _UserAuthenProfilePreAuthenVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 8),
    _UserAuthenProfilePreAuthenVLAN_Type()
)
userAuthenProfilePreAuthenVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfilePreAuthenVLAN.setStatus("current")


class _UserAuthenProfileAuthenFailAuthorServiceSchemeName_Type(OctetString):
    """Custom type userAuthenProfileAuthenFailAuthorServiceSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthenProfileAuthenFailAuthorServiceSchemeName_Type.__name__ = "OctetString"
_UserAuthenProfileAuthenFailAuthorServiceSchemeName_Object = MibTableColumn
userAuthenProfileAuthenFailAuthorServiceSchemeName = _UserAuthenProfileAuthenFailAuthorServiceSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 9),
    _UserAuthenProfileAuthenFailAuthorServiceSchemeName_Type()
)
userAuthenProfileAuthenFailAuthorServiceSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenFailAuthorServiceSchemeName.setStatus("current")


class _UserAuthenProfileAuthenFailAuthorUserGroupName_Type(OctetString):
    """Custom type userAuthenProfileAuthenFailAuthorUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfileAuthenFailAuthorUserGroupName_Type.__name__ = "OctetString"
_UserAuthenProfileAuthenFailAuthorUserGroupName_Object = MibTableColumn
userAuthenProfileAuthenFailAuthorUserGroupName = _UserAuthenProfileAuthenFailAuthorUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 10),
    _UserAuthenProfileAuthenFailAuthorUserGroupName_Type()
)
userAuthenProfileAuthenFailAuthorUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenFailAuthorUserGroupName.setStatus("current")


class _UserAuthenProfileAuthenFailAuthorVLAN_Type(Integer32):
    """Custom type userAuthenProfileAuthenFailAuthorVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_UserAuthenProfileAuthenFailAuthorVLAN_Type.__name__ = "Integer32"
_UserAuthenProfileAuthenFailAuthorVLAN_Object = MibTableColumn
userAuthenProfileAuthenFailAuthorVLAN = _UserAuthenProfileAuthenFailAuthorVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 11),
    _UserAuthenProfileAuthenFailAuthorVLAN_Type()
)
userAuthenProfileAuthenFailAuthorVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenFailAuthorVLAN.setStatus("current")


class _UserAuthenProfileAuthenServerDownServiceSchemeName_Type(OctetString):
    """Custom type userAuthenProfileAuthenServerDownServiceSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthenProfileAuthenServerDownServiceSchemeName_Type.__name__ = "OctetString"
_UserAuthenProfileAuthenServerDownServiceSchemeName_Object = MibTableColumn
userAuthenProfileAuthenServerDownServiceSchemeName = _UserAuthenProfileAuthenServerDownServiceSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 12),
    _UserAuthenProfileAuthenServerDownServiceSchemeName_Type()
)
userAuthenProfileAuthenServerDownServiceSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenServerDownServiceSchemeName.setStatus("current")


class _UserAuthenProfileAuthenServerDownUserGroupName_Type(OctetString):
    """Custom type userAuthenProfileAuthenServerDownUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfileAuthenServerDownUserGroupName_Type.__name__ = "OctetString"
_UserAuthenProfileAuthenServerDownUserGroupName_Object = MibTableColumn
userAuthenProfileAuthenServerDownUserGroupName = _UserAuthenProfileAuthenServerDownUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 13),
    _UserAuthenProfileAuthenServerDownUserGroupName_Type()
)
userAuthenProfileAuthenServerDownUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenServerDownUserGroupName.setStatus("current")


class _UserAuthenProfileAuthenServerDownVLAN_Type(Integer32):
    """Custom type userAuthenProfileAuthenServerDownVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_UserAuthenProfileAuthenServerDownVLAN_Type.__name__ = "Integer32"
_UserAuthenProfileAuthenServerDownVLAN_Object = MibTableColumn
userAuthenProfileAuthenServerDownVLAN = _UserAuthenProfileAuthenServerDownVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 14),
    _UserAuthenProfileAuthenServerDownVLAN_Type()
)
userAuthenProfileAuthenServerDownVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenServerDownVLAN.setStatus("current")
_UserAuthenProfileAuthenServerDownResponseSuccess_Type = TruthValue
_UserAuthenProfileAuthenServerDownResponseSuccess_Object = MibTableColumn
userAuthenProfileAuthenServerDownResponseSuccess = _UserAuthenProfileAuthenServerDownResponseSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 15),
    _UserAuthenProfileAuthenServerDownResponseSuccess_Type()
)
userAuthenProfileAuthenServerDownResponseSuccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenServerDownResponseSuccess.setStatus("current")
_UserAuthenProfileAuthenServerUpReauthen_Type = TruthValue
_UserAuthenProfileAuthenServerUpReauthen_Object = MibTableColumn
userAuthenProfileAuthenServerUpReauthen = _UserAuthenProfileAuthenServerUpReauthen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 16),
    _UserAuthenProfileAuthenServerUpReauthen_Type()
)
userAuthenProfileAuthenServerUpReauthen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenServerUpReauthen.setStatus("current")
_UserAuthenProfileMacAuthenFirst_Type = TruthValue
_UserAuthenProfileMacAuthenFirst_Object = MibTableColumn
userAuthenProfileMacAuthenFirst = _UserAuthenProfileMacAuthenFirst_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 17),
    _UserAuthenProfileMacAuthenFirst_Type()
)
userAuthenProfileMacAuthenFirst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileMacAuthenFirst.setStatus("current")
_UserAuthenProfileMACBypass_Type = TruthValue
_UserAuthenProfileMACBypass_Object = MibTableColumn
userAuthenProfileMACBypass = _UserAuthenProfileMACBypass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 18),
    _UserAuthenProfileMACBypass_Type()
)
userAuthenProfileMACBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileMACBypass.setStatus("current")


class _UserAuthenProfileDot1xForceDomain_Type(OctetString):
    """Custom type userAuthenProfileDot1xForceDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfileDot1xForceDomain_Type.__name__ = "OctetString"
_UserAuthenProfileDot1xForceDomain_Object = MibTableColumn
userAuthenProfileDot1xForceDomain = _UserAuthenProfileDot1xForceDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 19),
    _UserAuthenProfileDot1xForceDomain_Type()
)
userAuthenProfileDot1xForceDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileDot1xForceDomain.setStatus("current")


class _UserAuthenProfileMACAuthenForceDomain_Type(OctetString):
    """Custom type userAuthenProfileMACAuthenForceDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfileMACAuthenForceDomain_Type.__name__ = "OctetString"
_UserAuthenProfileMACAuthenForceDomain_Object = MibTableColumn
userAuthenProfileMACAuthenForceDomain = _UserAuthenProfileMACAuthenForceDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 20),
    _UserAuthenProfileMACAuthenForceDomain_Type()
)
userAuthenProfileMACAuthenForceDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileMACAuthenForceDomain.setStatus("current")


class _UserAuthenProfilePortalForceDomain_Type(OctetString):
    """Custom type userAuthenProfilePortalForceDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfilePortalForceDomain_Type.__name__ = "OctetString"
_UserAuthenProfilePortalForceDomain_Object = MibTableColumn
userAuthenProfilePortalForceDomain = _UserAuthenProfilePortalForceDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 21),
    _UserAuthenProfilePortalForceDomain_Type()
)
userAuthenProfilePortalForceDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfilePortalForceDomain.setStatus("current")


class _UserAuthenProfileDot1xDefaultDomain_Type(OctetString):
    """Custom type userAuthenProfileDot1xDefaultDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfileDot1xDefaultDomain_Type.__name__ = "OctetString"
_UserAuthenProfileDot1xDefaultDomain_Object = MibTableColumn
userAuthenProfileDot1xDefaultDomain = _UserAuthenProfileDot1xDefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 22),
    _UserAuthenProfileDot1xDefaultDomain_Type()
)
userAuthenProfileDot1xDefaultDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileDot1xDefaultDomain.setStatus("current")


class _UserAuthenProfileMACAuthenDefaultDomain_Type(OctetString):
    """Custom type userAuthenProfileMACAuthenDefaultDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfileMACAuthenDefaultDomain_Type.__name__ = "OctetString"
_UserAuthenProfileMACAuthenDefaultDomain_Object = MibTableColumn
userAuthenProfileMACAuthenDefaultDomain = _UserAuthenProfileMACAuthenDefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 23),
    _UserAuthenProfileMACAuthenDefaultDomain_Type()
)
userAuthenProfileMACAuthenDefaultDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileMACAuthenDefaultDomain.setStatus("current")


class _UserAuthenProfilePortalDefaultDomain_Type(OctetString):
    """Custom type userAuthenProfilePortalDefaultDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfilePortalDefaultDomain_Type.__name__ = "OctetString"
_UserAuthenProfilePortalDefaultDomain_Object = MibTableColumn
userAuthenProfilePortalDefaultDomain = _UserAuthenProfilePortalDefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 24),
    _UserAuthenProfilePortalDefaultDomain_Type()
)
userAuthenProfilePortalDefaultDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfilePortalDefaultDomain.setStatus("current")


class _UserAuthenProfileDefaultDomain_Type(OctetString):
    """Custom type userAuthenProfileDefaultDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfileDefaultDomain_Type.__name__ = "OctetString"
_UserAuthenProfileDefaultDomain_Object = MibTableColumn
userAuthenProfileDefaultDomain = _UserAuthenProfileDefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 25),
    _UserAuthenProfileDefaultDomain_Type()
)
userAuthenProfileDefaultDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileDefaultDomain.setStatus("current")


class _UserAuthenProfileForceDomain_Type(OctetString):
    """Custom type userAuthenProfileForceDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfileForceDomain_Type.__name__ = "OctetString"
_UserAuthenProfileForceDomain_Object = MibTableColumn
userAuthenProfileForceDomain = _UserAuthenProfileForceDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 26),
    _UserAuthenProfileForceDomain_Type()
)
userAuthenProfileForceDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileForceDomain.setStatus("current")


class _UserAuthenProfileDomainNameDelimiter_Type(OctetString):
    """Custom type userAuthenProfileDomainNameDelimiter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_UserAuthenProfileDomainNameDelimiter_Type.__name__ = "OctetString"
_UserAuthenProfileDomainNameDelimiter_Object = MibTableColumn
userAuthenProfileDomainNameDelimiter = _UserAuthenProfileDomainNameDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 27),
    _UserAuthenProfileDomainNameDelimiter_Type()
)
userAuthenProfileDomainNameDelimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileDomainNameDelimiter.setStatus("current")


class _UserAuthenProfileDomainNameLocation_Type(Integer32):
    """Custom type userAuthenProfileDomainNameLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domainnamepositionahead", 0),
          ("domainnamepositionbehind", 1),
          ("domainnamepositioninvalid", 2))
    )


_UserAuthenProfileDomainNameLocation_Type.__name__ = "Integer32"
_UserAuthenProfileDomainNameLocation_Object = MibTableColumn
userAuthenProfileDomainNameLocation = _UserAuthenProfileDomainNameLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 28),
    _UserAuthenProfileDomainNameLocation_Type()
)
userAuthenProfileDomainNameLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileDomainNameLocation.setStatus("current")


class _UserAuthenProfileDomainNameParseDirection_Type(Integer32):
    """Custom type userAuthenProfileDomainNameParseDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domainparseinvalid", 2),
          ("domainparselefttoright", 0),
          ("domainparserighttoleft", 1))
    )


_UserAuthenProfileDomainNameParseDirection_Type.__name__ = "Integer32"
_UserAuthenProfileDomainNameParseDirection_Object = MibTableColumn
userAuthenProfileDomainNameParseDirection = _UserAuthenProfileDomainNameParseDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 29),
    _UserAuthenProfileDomainNameParseDirection_Type()
)
userAuthenProfileDomainNameParseDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileDomainNameParseDirection.setStatus("current")


class _UserAuthenProfileSecurityNameDelimiter_Type(OctetString):
    """Custom type userAuthenProfileSecurityNameDelimiter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_UserAuthenProfileSecurityNameDelimiter_Type.__name__ = "OctetString"
_UserAuthenProfileSecurityNameDelimiter_Object = MibTableColumn
userAuthenProfileSecurityNameDelimiter = _UserAuthenProfileSecurityNameDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 30),
    _UserAuthenProfileSecurityNameDelimiter_Type()
)
userAuthenProfileSecurityNameDelimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileSecurityNameDelimiter.setStatus("current")


class _UserAuthenProfilePreAuthenReAuthenTimer_Type(Integer32):
    """Custom type userAuthenProfilePreAuthenReAuthenTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 7200),
    )


_UserAuthenProfilePreAuthenReAuthenTimer_Type.__name__ = "Integer32"
_UserAuthenProfilePreAuthenReAuthenTimer_Object = MibTableColumn
userAuthenProfilePreAuthenReAuthenTimer = _UserAuthenProfilePreAuthenReAuthenTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 31),
    _UserAuthenProfilePreAuthenReAuthenTimer_Type()
)
userAuthenProfilePreAuthenReAuthenTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfilePreAuthenReAuthenTimer.setStatus("current")


class _UserAuthenProfileAuthenFailReAuthenTimer_Type(Integer32):
    """Custom type userAuthenProfileAuthenFailReAuthenTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 7200),
    )


_UserAuthenProfileAuthenFailReAuthenTimer_Type.__name__ = "Integer32"
_UserAuthenProfileAuthenFailReAuthenTimer_Object = MibTableColumn
userAuthenProfileAuthenFailReAuthenTimer = _UserAuthenProfileAuthenFailReAuthenTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 32),
    _UserAuthenProfileAuthenFailReAuthenTimer_Type()
)
userAuthenProfileAuthenFailReAuthenTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenFailReAuthenTimer.setStatus("current")


class _UserAuthenProfilePreAuthenAgingTime_Type(Integer32):
    """Custom type userAuthenProfilePreAuthenAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294860),
    )


_UserAuthenProfilePreAuthenAgingTime_Type.__name__ = "Integer32"
_UserAuthenProfilePreAuthenAgingTime_Object = MibTableColumn
userAuthenProfilePreAuthenAgingTime = _UserAuthenProfilePreAuthenAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 33),
    _UserAuthenProfilePreAuthenAgingTime_Type()
)
userAuthenProfilePreAuthenAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfilePreAuthenAgingTime.setStatus("current")


class _UserAuthenProfileAuthenFailAgingTime_Type(Integer32):
    """Custom type userAuthenProfileAuthenFailAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294860),
    )


_UserAuthenProfileAuthenFailAgingTime_Type.__name__ = "Integer32"
_UserAuthenProfileAuthenFailAgingTime_Object = MibTableColumn
userAuthenProfileAuthenFailAgingTime = _UserAuthenProfileAuthenFailAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 34),
    _UserAuthenProfileAuthenFailAgingTime_Type()
)
userAuthenProfileAuthenFailAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenFailAgingTime.setStatus("current")


class _UserAuthenProfileFreeRuleName_Type(OctetString):
    """Custom type userAuthenProfileFreeRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_UserAuthenProfileFreeRuleName_Type.__name__ = "OctetString"
_UserAuthenProfileFreeRuleName_Object = MibTableColumn
userAuthenProfileFreeRuleName = _UserAuthenProfileFreeRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 35),
    _UserAuthenProfileFreeRuleName_Type()
)
userAuthenProfileFreeRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileFreeRuleName.setStatus("current")


class _UserAuthenProfileAuthenSchemeName_Type(OctetString):
    """Custom type userAuthenProfileAuthenSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthenProfileAuthenSchemeName_Type.__name__ = "OctetString"
_UserAuthenProfileAuthenSchemeName_Object = MibTableColumn
userAuthenProfileAuthenSchemeName = _UserAuthenProfileAuthenSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 36),
    _UserAuthenProfileAuthenSchemeName_Type()
)
userAuthenProfileAuthenSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenSchemeName.setStatus("current")


class _UserAuthenProfileAuthorSchemeName_Type(OctetString):
    """Custom type userAuthenProfileAuthorSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthenProfileAuthorSchemeName_Type.__name__ = "OctetString"
_UserAuthenProfileAuthorSchemeName_Object = MibTableColumn
userAuthenProfileAuthorSchemeName = _UserAuthenProfileAuthorSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 37),
    _UserAuthenProfileAuthorSchemeName_Type()
)
userAuthenProfileAuthorSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthorSchemeName.setStatus("current")


class _UserAuthenProfileAcctSchemeName_Type(OctetString):
    """Custom type userAuthenProfileAcctSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthenProfileAcctSchemeName_Type.__name__ = "OctetString"
_UserAuthenProfileAcctSchemeName_Object = MibTableColumn
userAuthenProfileAcctSchemeName = _UserAuthenProfileAcctSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 38),
    _UserAuthenProfileAcctSchemeName_Type()
)
userAuthenProfileAcctSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAcctSchemeName.setStatus("current")


class _UserAuthenProfileServiceSchemeName_Type(OctetString):
    """Custom type userAuthenProfileServiceSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthenProfileServiceSchemeName_Type.__name__ = "OctetString"
_UserAuthenProfileServiceSchemeName_Object = MibTableColumn
userAuthenProfileServiceSchemeName = _UserAuthenProfileServiceSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 39),
    _UserAuthenProfileServiceSchemeName_Type()
)
userAuthenProfileServiceSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileServiceSchemeName.setStatus("current")


class _UserAuthenProfileUserGroupName_Type(OctetString):
    """Custom type userAuthenProfileUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenProfileUserGroupName_Type.__name__ = "OctetString"
_UserAuthenProfileUserGroupName_Object = MibTableColumn
userAuthenProfileUserGroupName = _UserAuthenProfileUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 40),
    _UserAuthenProfileUserGroupName_Type()
)
userAuthenProfileUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileUserGroupName.setStatus("current")


class _UserAuthenProfileRadiusServerName_Type(OctetString):
    """Custom type userAuthenProfileRadiusServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthenProfileRadiusServerName_Type.__name__ = "OctetString"
_UserAuthenProfileRadiusServerName_Object = MibTableColumn
userAuthenProfileRadiusServerName = _UserAuthenProfileRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 41),
    _UserAuthenProfileRadiusServerName_Type()
)
userAuthenProfileRadiusServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileRadiusServerName.setStatus("current")


class _UserAuthenProfileHwtacacsServerName_Type(OctetString):
    """Custom type userAuthenProfileHwtacacsServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthenProfileHwtacacsServerName_Type.__name__ = "OctetString"
_UserAuthenProfileHwtacacsServerName_Object = MibTableColumn
userAuthenProfileHwtacacsServerName = _UserAuthenProfileHwtacacsServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 42),
    _UserAuthenProfileHwtacacsServerName_Type()
)
userAuthenProfileHwtacacsServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileHwtacacsServerName.setStatus("current")


class _UserAuthenProfileAuthenticationMode_Type(Integer32):
    """Custom type userAuthenProfileAuthenticationMode based on Integer32"""
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
        *(("multishare", 2),
          ("multiterminal", 3),
          ("singleterminal", 0),
          ("singlevoicewithdata", 1))
    )


_UserAuthenProfileAuthenticationMode_Type.__name__ = "Integer32"
_UserAuthenProfileAuthenticationMode_Object = MibTableColumn
userAuthenProfileAuthenticationMode = _UserAuthenProfileAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 43),
    _UserAuthenProfileAuthenticationMode_Type()
)
userAuthenProfileAuthenticationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenticationMode.setStatus("current")
_UserAuthenProfileMaxUser_Type = Integer32
_UserAuthenProfileMaxUser_Object = MibTableColumn
userAuthenProfileMaxUser = _UserAuthenProfileMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 44),
    _UserAuthenProfileMaxUser_Type()
)
userAuthenProfileMaxUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileMaxUser.setStatus("current")
_UserAuthenProfileArpDetect_Type = TruthValue
_UserAuthenProfileArpDetect_Object = MibTableColumn
userAuthenProfileArpDetect = _UserAuthenProfileArpDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 45),
    _UserAuthenProfileArpDetect_Type()
)
userAuthenProfileArpDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileArpDetect.setStatus("current")


class _UserAuthenProfileArpDetectTimer_Type(Integer32):
    """Custom type userAuthenProfileArpDetectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 7200),
    )


_UserAuthenProfileArpDetectTimer_Type.__name__ = "Integer32"
_UserAuthenProfileArpDetectTimer_Object = MibTableColumn
userAuthenProfileArpDetectTimer = _UserAuthenProfileArpDetectTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 46),
    _UserAuthenProfileArpDetectTimer_Type()
)
userAuthenProfileArpDetectTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileArpDetectTimer.setStatus("current")
_UserAuthenProfileRowStatus_Type = RowStatus
_UserAuthenProfileRowStatus_Object = MibTableColumn
userAuthenProfileRowStatus = _UserAuthenProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 47),
    _UserAuthenProfileRowStatus_Type()
)
userAuthenProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileRowStatus.setStatus("current")


class _UserAuthenProfilePermitDomain_Type(OctetString):
    """Custom type userAuthenProfilePermitDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 259),
    )


_UserAuthenProfilePermitDomain_Type.__name__ = "OctetString"
_UserAuthenProfilePermitDomain_Object = MibTableColumn
userAuthenProfilePermitDomain = _UserAuthenProfilePermitDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 48),
    _UserAuthenProfilePermitDomain_Type()
)
userAuthenProfilePermitDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfilePermitDomain.setStatus("current")


class _UserAuthenProfileAuthenticationMaxUser_Type(Integer32):
    """Custom type userAuthenProfileAuthenticationMaxUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_UserAuthenProfileAuthenticationMaxUser_Type.__name__ = "Integer32"
_UserAuthenProfileAuthenticationMaxUser_Object = MibTableColumn
userAuthenProfileAuthenticationMaxUser = _UserAuthenProfileAuthenticationMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 49),
    _UserAuthenProfileAuthenticationMaxUser_Type()
)
userAuthenProfileAuthenticationMaxUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenticationMaxUser.setStatus("current")
_UserAuthenProfileAuthenFailAuthorResponseSuccess_Type = TruthValue
_UserAuthenProfileAuthenFailAuthorResponseSuccess_Object = MibTableColumn
userAuthenProfileAuthenFailAuthorResponseSuccess = _UserAuthenProfileAuthenFailAuthorResponseSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 62, 1, 50),
    _UserAuthenProfileAuthenFailAuthorResponseSuccess_Type()
)
userAuthenProfileAuthenFailAuthorResponseSuccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenProfileAuthenFailAuthorResponseSuccess.setStatus("current")
_UserAuthenticationFreeRuleTable_Object = MibTable
userAuthenticationFreeRuleTable = _UserAuthenticationFreeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 63)
)
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleTable.setStatus("current")
_UserAuthenticationFreeRuleEntry_Object = MibTableRow
userAuthenticationFreeRuleEntry = _UserAuthenticationFreeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 63, 1)
)
userAuthenticationFreeRuleEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "userAuthenticationFreeRuleName"),
)
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleEntry.setStatus("current")


class _UserAuthenticationFreeRuleName_Type(DisplayString):
    """Custom type userAuthenticationFreeRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_UserAuthenticationFreeRuleName_Type.__name__ = "DisplayString"
_UserAuthenticationFreeRuleName_Object = MibTableColumn
userAuthenticationFreeRuleName = _UserAuthenticationFreeRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 63, 1, 1),
    _UserAuthenticationFreeRuleName_Type()
)
userAuthenticationFreeRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleName.setStatus("current")


class _UserAuthenticationFreeRuleACLNumber_Type(Integer32):
    """Custom type userAuthenticationFreeRuleACLNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(6000, 6031),
    )


_UserAuthenticationFreeRuleACLNumber_Type.__name__ = "Integer32"
_UserAuthenticationFreeRuleACLNumber_Object = MibTableColumn
userAuthenticationFreeRuleACLNumber = _UserAuthenticationFreeRuleACLNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 63, 1, 2),
    _UserAuthenticationFreeRuleACLNumber_Type()
)
userAuthenticationFreeRuleACLNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleACLNumber.setStatus("current")


class _UserAuthenticationFreeRuleIPv6ACLNumber_Type(Integer32):
    """Custom type userAuthenticationFreeRuleIPv6ACLNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3000, 3031),
    )


_UserAuthenticationFreeRuleIPv6ACLNumber_Type.__name__ = "Integer32"
_UserAuthenticationFreeRuleIPv6ACLNumber_Object = MibTableColumn
userAuthenticationFreeRuleIPv6ACLNumber = _UserAuthenticationFreeRuleIPv6ACLNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 63, 1, 3),
    _UserAuthenticationFreeRuleIPv6ACLNumber_Type()
)
userAuthenticationFreeRuleIPv6ACLNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleIPv6ACLNumber.setStatus("current")
_UserAuthenticationFreeRuleRowStatus_Type = RowStatus
_UserAuthenticationFreeRuleRowStatus_Object = MibTableColumn
userAuthenticationFreeRuleRowStatus = _UserAuthenticationFreeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 63, 1, 4),
    _UserAuthenticationFreeRuleRowStatus_Type()
)
userAuthenticationFreeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleRowStatus.setStatus("current")
_HwDot1xAccessProfileTable_Object = MibTable
hwDot1xAccessProfileTable = _HwDot1xAccessProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64)
)
if mibBuilder.loadTexts:
    hwDot1xAccessProfileTable.setStatus("current")
_HwDot1xAccessProfileEntry_Object = MibTableRow
hwDot1xAccessProfileEntry = _HwDot1xAccessProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1)
)
hwDot1xAccessProfileEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwDot1xAccessProfileName"),
)
if mibBuilder.loadTexts:
    hwDot1xAccessProfileEntry.setStatus("current")


class _HwDot1xAccessProfileName_Type(DisplayString):
    """Custom type hwDot1xAccessProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwDot1xAccessProfileName_Type.__name__ = "DisplayString"
_HwDot1xAccessProfileName_Object = MibTableColumn
hwDot1xAccessProfileName = _HwDot1xAccessProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 1),
    _HwDot1xAccessProfileName_Type()
)
hwDot1xAccessProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileName.setStatus("current")


class _HwDot1xAccessProfileGuestAuthorServiceSchemeName_Type(DisplayString):
    """Custom type hwDot1xAccessProfileGuestAuthorServiceSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDot1xAccessProfileGuestAuthorServiceSchemeName_Type.__name__ = "DisplayString"
_HwDot1xAccessProfileGuestAuthorServiceSchemeName_Object = MibTableColumn
hwDot1xAccessProfileGuestAuthorServiceSchemeName = _HwDot1xAccessProfileGuestAuthorServiceSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 2),
    _HwDot1xAccessProfileGuestAuthorServiceSchemeName_Type()
)
hwDot1xAccessProfileGuestAuthorServiceSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileGuestAuthorServiceSchemeName.setStatus("current")


class _HwDot1xAccessProfileGuestAuthorUserGroupName_Type(DisplayString):
    """Custom type hwDot1xAccessProfileGuestAuthorUserGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwDot1xAccessProfileGuestAuthorUserGroupName_Type.__name__ = "DisplayString"
_HwDot1xAccessProfileGuestAuthorUserGroupName_Object = MibTableColumn
hwDot1xAccessProfileGuestAuthorUserGroupName = _HwDot1xAccessProfileGuestAuthorUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 3),
    _HwDot1xAccessProfileGuestAuthorUserGroupName_Type()
)
hwDot1xAccessProfileGuestAuthorUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileGuestAuthorUserGroupName.setStatus("current")


class _HwDot1xAccessProfileGuestAuthorVLAN_Type(Integer32):
    """Custom type hwDot1xAccessProfileGuestAuthorVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwDot1xAccessProfileGuestAuthorVLAN_Type.__name__ = "Integer32"
_HwDot1xAccessProfileGuestAuthorVLAN_Object = MibTableColumn
hwDot1xAccessProfileGuestAuthorVLAN = _HwDot1xAccessProfileGuestAuthorVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 4),
    _HwDot1xAccessProfileGuestAuthorVLAN_Type()
)
hwDot1xAccessProfileGuestAuthorVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileGuestAuthorVLAN.setStatus("current")
_HwDot1xAccessProfileHandshakeSwitch_Type = TruthValue
_HwDot1xAccessProfileHandshakeSwitch_Object = MibTableColumn
hwDot1xAccessProfileHandshakeSwitch = _HwDot1xAccessProfileHandshakeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 5),
    _HwDot1xAccessProfileHandshakeSwitch_Type()
)
hwDot1xAccessProfileHandshakeSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileHandshakeSwitch.setStatus("current")


class _HwDot1xAccessProfileHandShakePktType_Type(Integer32):
    """Custom type hwDot1xAccessProfileHandShakePktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              20)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("srpsha1", 20))
    )


_HwDot1xAccessProfileHandShakePktType_Type.__name__ = "Integer32"
_HwDot1xAccessProfileHandShakePktType_Object = MibTableColumn
hwDot1xAccessProfileHandShakePktType = _HwDot1xAccessProfileHandShakePktType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 6),
    _HwDot1xAccessProfileHandShakePktType_Type()
)
hwDot1xAccessProfileHandShakePktType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileHandShakePktType.setStatus("current")


class _HwDot1xAccessProfileHandshakeInterval_Type(Integer32):
    """Custom type hwDot1xAccessProfileHandshakeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 7200),
    )


_HwDot1xAccessProfileHandshakeInterval_Type.__name__ = "Integer32"
_HwDot1xAccessProfileHandshakeInterval_Object = MibTableColumn
hwDot1xAccessProfileHandshakeInterval = _HwDot1xAccessProfileHandshakeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 7),
    _HwDot1xAccessProfileHandshakeInterval_Type()
)
hwDot1xAccessProfileHandshakeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileHandshakeInterval.setStatus("current")
_HwDot1xAccessProfileIfEAPEnd_Type = TruthValue
_HwDot1xAccessProfileIfEAPEnd_Object = MibTableColumn
hwDot1xAccessProfileIfEAPEnd = _HwDot1xAccessProfileIfEAPEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 8),
    _HwDot1xAccessProfileIfEAPEnd_Type()
)
hwDot1xAccessProfileIfEAPEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileIfEAPEnd.setStatus("current")


class _HwDot1xAccessProfileEAPEndMethod_Type(Integer32):
    """Custom type hwDot1xAccessProfileEAPEndMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("eap", 3),
          ("pap", 2))
    )


_HwDot1xAccessProfileEAPEndMethod_Type.__name__ = "Integer32"
_HwDot1xAccessProfileEAPEndMethod_Object = MibTableColumn
hwDot1xAccessProfileEAPEndMethod = _HwDot1xAccessProfileEAPEndMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 9),
    _HwDot1xAccessProfileEAPEndMethod_Type()
)
hwDot1xAccessProfileEAPEndMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileEAPEndMethod.setStatus("current")


class _HwDot1xAccessProfileEAPNotifyPktEAPCode_Type(Integer32):
    """Custom type hwDot1xAccessProfileEAPNotifyPktEAPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_HwDot1xAccessProfileEAPNotifyPktEAPCode_Type.__name__ = "Integer32"
_HwDot1xAccessProfileEAPNotifyPktEAPCode_Object = MibTableColumn
hwDot1xAccessProfileEAPNotifyPktEAPCode = _HwDot1xAccessProfileEAPNotifyPktEAPCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 10),
    _HwDot1xAccessProfileEAPNotifyPktEAPCode_Type()
)
hwDot1xAccessProfileEAPNotifyPktEAPCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileEAPNotifyPktEAPCode.setStatus("current")


class _HwDot1xAccessProfileEAPNotifyPktEAPType_Type(Integer32):
    """Custom type hwDot1xAccessProfileEAPNotifyPktEAPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwDot1xAccessProfileEAPNotifyPktEAPType_Type.__name__ = "Integer32"
_HwDot1xAccessProfileEAPNotifyPktEAPType_Object = MibTableColumn
hwDot1xAccessProfileEAPNotifyPktEAPType = _HwDot1xAccessProfileEAPNotifyPktEAPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 11),
    _HwDot1xAccessProfileEAPNotifyPktEAPType_Type()
)
hwDot1xAccessProfileEAPNotifyPktEAPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileEAPNotifyPktEAPType.setStatus("current")
_HwDot1xAccessProfileReAuthenEnable_Type = TruthValue
_HwDot1xAccessProfileReAuthenEnable_Object = MibTableColumn
hwDot1xAccessProfileReAuthenEnable = _HwDot1xAccessProfileReAuthenEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 12),
    _HwDot1xAccessProfileReAuthenEnable_Type()
)
hwDot1xAccessProfileReAuthenEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileReAuthenEnable.setStatus("current")


class _HwDot1xAccessProfileReauthenticationTimeout_Type(Integer32):
    """Custom type hwDot1xAccessProfileReauthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_HwDot1xAccessProfileReauthenticationTimeout_Type.__name__ = "Integer32"
_HwDot1xAccessProfileReauthenticationTimeout_Object = MibTableColumn
hwDot1xAccessProfileReauthenticationTimeout = _HwDot1xAccessProfileReauthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 13),
    _HwDot1xAccessProfileReauthenticationTimeout_Type()
)
hwDot1xAccessProfileReauthenticationTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileReauthenticationTimeout.setStatus("current")


class _HwDot1xAccessProfileClientTimeout_Type(Integer32):
    """Custom type hwDot1xAccessProfileClientTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwDot1xAccessProfileClientTimeout_Type.__name__ = "Integer32"
_HwDot1xAccessProfileClientTimeout_Object = MibTableColumn
hwDot1xAccessProfileClientTimeout = _HwDot1xAccessProfileClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 14),
    _HwDot1xAccessProfileClientTimeout_Type()
)
hwDot1xAccessProfileClientTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileClientTimeout.setStatus("current")


class _HwDot1xAccessProfileServerTimeout_Type(Integer32):
    """Custom type hwDot1xAccessProfileServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwDot1xAccessProfileServerTimeout_Type.__name__ = "Integer32"
_HwDot1xAccessProfileServerTimeout_Object = MibTableColumn
hwDot1xAccessProfileServerTimeout = _HwDot1xAccessProfileServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 15),
    _HwDot1xAccessProfileServerTimeout_Type()
)
hwDot1xAccessProfileServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileServerTimeout.setStatus("current")


class _HwDot1xAccessProfileTxPeriod_Type(Integer32):
    """Custom type hwDot1xAccessProfileTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwDot1xAccessProfileTxPeriod_Type.__name__ = "Integer32"
_HwDot1xAccessProfileTxPeriod_Object = MibTableColumn
hwDot1xAccessProfileTxPeriod = _HwDot1xAccessProfileTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 16),
    _HwDot1xAccessProfileTxPeriod_Type()
)
hwDot1xAccessProfileTxPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileTxPeriod.setStatus("current")


class _HwDot1xAccessProfileMaxRetryValue_Type(Integer32):
    """Custom type hwDot1xAccessProfileMaxRetryValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwDot1xAccessProfileMaxRetryValue_Type.__name__ = "Integer32"
_HwDot1xAccessProfileMaxRetryValue_Object = MibTableColumn
hwDot1xAccessProfileMaxRetryValue = _HwDot1xAccessProfileMaxRetryValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 17),
    _HwDot1xAccessProfileMaxRetryValue_Type()
)
hwDot1xAccessProfileMaxRetryValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileMaxRetryValue.setStatus("current")
_HwDot1xAccessProfileSpeedLimitAuto_Type = TruthValue
_HwDot1xAccessProfileSpeedLimitAuto_Object = MibTableColumn
hwDot1xAccessProfileSpeedLimitAuto = _HwDot1xAccessProfileSpeedLimitAuto_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 18),
    _HwDot1xAccessProfileSpeedLimitAuto_Type()
)
hwDot1xAccessProfileSpeedLimitAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileSpeedLimitAuto.setStatus("current")


class _HwDot1xAccessProfileTriggerPktType_Type(Integer32):
    """Custom type hwDot1xAccessProfileTriggerPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("default", 0),
          ("dhcp", 2))
    )


_HwDot1xAccessProfileTriggerPktType_Type.__name__ = "Integer32"
_HwDot1xAccessProfileTriggerPktType_Object = MibTableColumn
hwDot1xAccessProfileTriggerPktType = _HwDot1xAccessProfileTriggerPktType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 19),
    _HwDot1xAccessProfileTriggerPktType_Type()
)
hwDot1xAccessProfileTriggerPktType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileTriggerPktType.setStatus("current")
_HwDot1xAccessProfileUnicastTrigger_Type = TruthValue
_HwDot1xAccessProfileUnicastTrigger_Object = MibTableColumn
hwDot1xAccessProfileUnicastTrigger = _HwDot1xAccessProfileUnicastTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 20),
    _HwDot1xAccessProfileUnicastTrigger_Type()
)
hwDot1xAccessProfileUnicastTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileUnicastTrigger.setStatus("current")


class _HwDot1xAccessProfileURL_Type(DisplayString):
    """Custom type hwDot1xAccessProfileURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HwDot1xAccessProfileURL_Type.__name__ = "DisplayString"
_HwDot1xAccessProfileURL_Object = MibTableColumn
hwDot1xAccessProfileURL = _HwDot1xAccessProfileURL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 21),
    _HwDot1xAccessProfileURL_Type()
)
hwDot1xAccessProfileURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileURL.setStatus("current")


class _HwDot1xAccessProfileEthTrunkHandShakePeriod_Type(Integer32):
    """Custom type hwDot1xAccessProfileEthTrunkHandShakePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 7200),
    )


_HwDot1xAccessProfileEthTrunkHandShakePeriod_Type.__name__ = "Integer32"
_HwDot1xAccessProfileEthTrunkHandShakePeriod_Object = MibTableColumn
hwDot1xAccessProfileEthTrunkHandShakePeriod = _HwDot1xAccessProfileEthTrunkHandShakePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 22),
    _HwDot1xAccessProfileEthTrunkHandShakePeriod_Type()
)
hwDot1xAccessProfileEthTrunkHandShakePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileEthTrunkHandShakePeriod.setStatus("current")
_HwDot1xAccessProfileRowStatus_Type = RowStatus
_HwDot1xAccessProfileRowStatus_Object = MibTableColumn
hwDot1xAccessProfileRowStatus = _HwDot1xAccessProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 64, 1, 23),
    _HwDot1xAccessProfileRowStatus_Type()
)
hwDot1xAccessProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xAccessProfileRowStatus.setStatus("current")
_HwMACAuthenAccessProfileTable_Object = MibTable
hwMACAuthenAccessProfileTable = _HwMACAuthenAccessProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65)
)
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileTable.setStatus("current")
_HwMACAuthenAccessProfileEntry_Object = MibTableRow
hwMACAuthenAccessProfileEntry = _HwMACAuthenAccessProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1)
)
hwMACAuthenAccessProfileEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileName"),
)
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileEntry.setStatus("current")


class _HwMACAuthenAccessProfileName_Type(DisplayString):
    """Custom type hwMACAuthenAccessProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMACAuthenAccessProfileName_Type.__name__ = "DisplayString"
_HwMACAuthenAccessProfileName_Object = MibTableColumn
hwMACAuthenAccessProfileName = _HwMACAuthenAccessProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 1),
    _HwMACAuthenAccessProfileName_Type()
)
hwMACAuthenAccessProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileName.setStatus("current")
_HwMACAuthenAccessProfileReAuthenEnable_Type = TruthValue
_HwMACAuthenAccessProfileReAuthenEnable_Object = MibTableColumn
hwMACAuthenAccessProfileReAuthenEnable = _HwMACAuthenAccessProfileReAuthenEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 2),
    _HwMACAuthenAccessProfileReAuthenEnable_Type()
)
hwMACAuthenAccessProfileReAuthenEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileReAuthenEnable.setStatus("current")


class _HwMACAuthenAccessProfileReauthenticationTimeout_Type(Integer32):
    """Custom type hwMACAuthenAccessProfileReauthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_HwMACAuthenAccessProfileReauthenticationTimeout_Type.__name__ = "Integer32"
_HwMACAuthenAccessProfileReauthenticationTimeout_Object = MibTableColumn
hwMACAuthenAccessProfileReauthenticationTimeout = _HwMACAuthenAccessProfileReauthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 3),
    _HwMACAuthenAccessProfileReauthenticationTimeout_Type()
)
hwMACAuthenAccessProfileReauthenticationTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileReauthenticationTimeout.setStatus("current")


class _HwMACAuthenAccessProfileServerTimeout_Type(Integer32):
    """Custom type hwMACAuthenAccessProfileServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwMACAuthenAccessProfileServerTimeout_Type.__name__ = "Integer32"
_HwMACAuthenAccessProfileServerTimeout_Object = MibTableColumn
hwMACAuthenAccessProfileServerTimeout = _HwMACAuthenAccessProfileServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 4),
    _HwMACAuthenAccessProfileServerTimeout_Type()
)
hwMACAuthenAccessProfileServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileServerTimeout.setStatus("current")


class _HwMACAuthenAccessProfileUserNameFixedUserName_Type(OctetString):
    """Custom type hwMACAuthenAccessProfileUserNameFixedUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwMACAuthenAccessProfileUserNameFixedUserName_Type.__name__ = "OctetString"
_HwMACAuthenAccessProfileUserNameFixedUserName_Object = MibTableColumn
hwMACAuthenAccessProfileUserNameFixedUserName = _HwMACAuthenAccessProfileUserNameFixedUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 5),
    _HwMACAuthenAccessProfileUserNameFixedUserName_Type()
)
hwMACAuthenAccessProfileUserNameFixedUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileUserNameFixedUserName.setStatus("current")


class _HwMACAuthenAccessProfileFixedPassword_Type(OctetString):
    """Custom type hwMACAuthenAccessProfileFixedPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwMACAuthenAccessProfileFixedPassword_Type.__name__ = "OctetString"
_HwMACAuthenAccessProfileFixedPassword_Object = MibTableColumn
hwMACAuthenAccessProfileFixedPassword = _HwMACAuthenAccessProfileFixedPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 6),
    _HwMACAuthenAccessProfileFixedPassword_Type()
)
hwMACAuthenAccessProfileFixedPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileFixedPassword.setStatus("current")


class _HwMACAuthenAccessProfileMACAddressFormat_Type(Integer32):
    """Custom type hwMACAuthenAccessProfileMACAddressFormat based on Integer32"""
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
        *(("fixed", 3),
          ("invalid", 0),
          ("macAddressWithHyphen", 2),
          ("macAddressWithoutHyphen", 1),
          ("option", 4))
    )


_HwMACAuthenAccessProfileMACAddressFormat_Type.__name__ = "Integer32"
_HwMACAuthenAccessProfileMACAddressFormat_Object = MibTableColumn
hwMACAuthenAccessProfileMACAddressFormat = _HwMACAuthenAccessProfileMACAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 7),
    _HwMACAuthenAccessProfileMACAddressFormat_Type()
)
hwMACAuthenAccessProfileMACAddressFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileMACAddressFormat.setStatus("current")


class _HwMACAuthenAccessProfileMACAddressPassword_Type(OctetString):
    """Custom type hwMACAuthenAccessProfileMACAddressPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwMACAuthenAccessProfileMACAddressPassword_Type.__name__ = "OctetString"
_HwMACAuthenAccessProfileMACAddressPassword_Object = MibTableColumn
hwMACAuthenAccessProfileMACAddressPassword = _HwMACAuthenAccessProfileMACAddressPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 8),
    _HwMACAuthenAccessProfileMACAddressPassword_Type()
)
hwMACAuthenAccessProfileMACAddressPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileMACAddressPassword.setStatus("current")


class _HwMACAuthenAccessProfileUserNameDHCPOption_Type(Integer32):
    """Custom type hwMACAuthenAccessProfileUserNameDHCPOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              82)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("dhcpoption", 82))
    )


_HwMACAuthenAccessProfileUserNameDHCPOption_Type.__name__ = "Integer32"
_HwMACAuthenAccessProfileUserNameDHCPOption_Object = MibTableColumn
hwMACAuthenAccessProfileUserNameDHCPOption = _HwMACAuthenAccessProfileUserNameDHCPOption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 9),
    _HwMACAuthenAccessProfileUserNameDHCPOption_Type()
)
hwMACAuthenAccessProfileUserNameDHCPOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileUserNameDHCPOption.setStatus("current")


class _HwMACAuthenAccessProfileUserNameDHCPOSubOption_Type(Integer32):
    """Custom type hwMACAuthenAccessProfileUserNameDHCPOSubOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optionremoteid", 2),
          ("optionsubcircuitid", 1),
          ("optionsubinvalid", 0))
    )


_HwMACAuthenAccessProfileUserNameDHCPOSubOption_Type.__name__ = "Integer32"
_HwMACAuthenAccessProfileUserNameDHCPOSubOption_Object = MibTableColumn
hwMACAuthenAccessProfileUserNameDHCPOSubOption = _HwMACAuthenAccessProfileUserNameDHCPOSubOption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 10),
    _HwMACAuthenAccessProfileUserNameDHCPOSubOption_Type()
)
hwMACAuthenAccessProfileUserNameDHCPOSubOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileUserNameDHCPOSubOption.setStatus("current")


class _HwMACAuthenAccessProfileTriggerPktType_Type(Integer32):
    """Custom type hwMACAuthenAccessProfileTriggerPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMACAuthenAccessProfileTriggerPktType_Type.__name__ = "Integer32"
_HwMACAuthenAccessProfileTriggerPktType_Object = MibTableColumn
hwMACAuthenAccessProfileTriggerPktType = _HwMACAuthenAccessProfileTriggerPktType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 11),
    _HwMACAuthenAccessProfileTriggerPktType_Type()
)
hwMACAuthenAccessProfileTriggerPktType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileTriggerPktType.setStatus("current")


class _HwMACAuthenAccessProfileTriggerDHCPOptionType_Type(Integer32):
    """Custom type hwMACAuthenAccessProfileTriggerDHCPOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              82)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("optioncode", 82))
    )


_HwMACAuthenAccessProfileTriggerDHCPOptionType_Type.__name__ = "Integer32"
_HwMACAuthenAccessProfileTriggerDHCPOptionType_Object = MibTableColumn
hwMACAuthenAccessProfileTriggerDHCPOptionType = _HwMACAuthenAccessProfileTriggerDHCPOptionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 12),
    _HwMACAuthenAccessProfileTriggerDHCPOptionType_Type()
)
hwMACAuthenAccessProfileTriggerDHCPOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileTriggerDHCPOptionType.setStatus("current")
_HwMACAuthenAccessProfileDHCPRelaseOffline_Type = TruthValue
_HwMACAuthenAccessProfileDHCPRelaseOffline_Object = MibTableColumn
hwMACAuthenAccessProfileDHCPRelaseOffline = _HwMACAuthenAccessProfileDHCPRelaseOffline_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 13),
    _HwMACAuthenAccessProfileDHCPRelaseOffline_Type()
)
hwMACAuthenAccessProfileDHCPRelaseOffline.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileDHCPRelaseOffline.setStatus("current")
_HwMACAuthenAccessProfileDHCPRenewReAuthen_Type = TruthValue
_HwMACAuthenAccessProfileDHCPRenewReAuthen_Object = MibTableColumn
hwMACAuthenAccessProfileDHCPRenewReAuthen = _HwMACAuthenAccessProfileDHCPRenewReAuthen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 14),
    _HwMACAuthenAccessProfileDHCPRenewReAuthen_Type()
)
hwMACAuthenAccessProfileDHCPRenewReAuthen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileDHCPRenewReAuthen.setStatus("current")
_HwMACAuthenAccessProfilePermitAuthenMAC_Type = MacAddress
_HwMACAuthenAccessProfilePermitAuthenMAC_Object = MibTableColumn
hwMACAuthenAccessProfilePermitAuthenMAC = _HwMACAuthenAccessProfilePermitAuthenMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 15),
    _HwMACAuthenAccessProfilePermitAuthenMAC_Type()
)
hwMACAuthenAccessProfilePermitAuthenMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfilePermitAuthenMAC.setStatus("current")
_HwMACAuthenAccessProfilePermitAuthenMACMask_Type = MacAddress
_HwMACAuthenAccessProfilePermitAuthenMACMask_Object = MibTableColumn
hwMACAuthenAccessProfilePermitAuthenMACMask = _HwMACAuthenAccessProfilePermitAuthenMACMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 16),
    _HwMACAuthenAccessProfilePermitAuthenMACMask_Type()
)
hwMACAuthenAccessProfilePermitAuthenMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfilePermitAuthenMACMask.setStatus("current")
_HwMACAuthenAccessProfileRowStatus_Type = RowStatus
_HwMACAuthenAccessProfileRowStatus_Object = MibTableColumn
hwMACAuthenAccessProfileRowStatus = _HwMACAuthenAccessProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 65, 1, 17),
    _HwMACAuthenAccessProfileRowStatus_Type()
)
hwMACAuthenAccessProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileRowStatus.setStatus("current")
_HwPortalAccessProfileTable_Object = MibTable
hwPortalAccessProfileTable = _HwPortalAccessProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66)
)
if mibBuilder.loadTexts:
    hwPortalAccessProfileTable.setStatus("current")
_HwPortalAccessProfileEntry_Object = MibTableRow
hwPortalAccessProfileEntry = _HwPortalAccessProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1)
)
hwPortalAccessProfileEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwPortalAccessProfileName"),
)
if mibBuilder.loadTexts:
    hwPortalAccessProfileEntry.setStatus("current")


class _HwPortalAccessProfileName_Type(DisplayString):
    """Custom type hwPortalAccessProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwPortalAccessProfileName_Type.__name__ = "DisplayString"
_HwPortalAccessProfileName_Object = MibTableColumn
hwPortalAccessProfileName = _HwPortalAccessProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 1),
    _HwPortalAccessProfileName_Type()
)
hwPortalAccessProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortalAccessProfileName.setStatus("current")


class _HwPortalAccessProfileDetectPeriod_Type(Integer32):
    """Custom type hwPortalAccessProfileDetectPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 7200),
    )


_HwPortalAccessProfileDetectPeriod_Type.__name__ = "Integer32"
_HwPortalAccessProfileDetectPeriod_Object = MibTableColumn
hwPortalAccessProfileDetectPeriod = _HwPortalAccessProfileDetectPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 2),
    _HwPortalAccessProfileDetectPeriod_Type()
)
hwPortalAccessProfileDetectPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfileDetectPeriod.setStatus("current")


class _HwPortalAccessProfilePortalServerDownServiceSchemeName_Type(OctetString):
    """Custom type hwPortalAccessProfilePortalServerDownServiceSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwPortalAccessProfilePortalServerDownServiceSchemeName_Type.__name__ = "OctetString"
_HwPortalAccessProfilePortalServerDownServiceSchemeName_Object = MibTableColumn
hwPortalAccessProfilePortalServerDownServiceSchemeName = _HwPortalAccessProfilePortalServerDownServiceSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 3),
    _HwPortalAccessProfilePortalServerDownServiceSchemeName_Type()
)
hwPortalAccessProfilePortalServerDownServiceSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfilePortalServerDownServiceSchemeName.setStatus("current")


class _HwPortalAccessProfilePortalServerDownUserGroupName_Type(OctetString):
    """Custom type hwPortalAccessProfilePortalServerDownUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwPortalAccessProfilePortalServerDownUserGroupName_Type.__name__ = "OctetString"
_HwPortalAccessProfilePortalServerDownUserGroupName_Object = MibTableColumn
hwPortalAccessProfilePortalServerDownUserGroupName = _HwPortalAccessProfilePortalServerDownUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 4),
    _HwPortalAccessProfilePortalServerDownUserGroupName_Type()
)
hwPortalAccessProfilePortalServerDownUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfilePortalServerDownUserGroupName.setStatus("current")
_HwPortalAccessProfilePortalServerUpReAuthen_Type = TruthValue
_HwPortalAccessProfilePortalServerUpReAuthen_Object = MibTableColumn
hwPortalAccessProfilePortalServerUpReAuthen = _HwPortalAccessProfilePortalServerUpReAuthen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 5),
    _HwPortalAccessProfilePortalServerUpReAuthen_Type()
)
hwPortalAccessProfilePortalServerUpReAuthen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfilePortalServerUpReAuthen.setStatus("current")


class _HwPortalAccessProfileAlarmUserLowNum_Type(Integer32):
    """Custom type hwPortalAccessProfileAlarmUserLowNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwPortalAccessProfileAlarmUserLowNum_Type.__name__ = "Integer32"
_HwPortalAccessProfileAlarmUserLowNum_Object = MibTableColumn
hwPortalAccessProfileAlarmUserLowNum = _HwPortalAccessProfileAlarmUserLowNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 6),
    _HwPortalAccessProfileAlarmUserLowNum_Type()
)
hwPortalAccessProfileAlarmUserLowNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfileAlarmUserLowNum.setStatus("current")


class _HwPortalAccessProfileAlarmUserHighNum_Type(Integer32):
    """Custom type hwPortalAccessProfileAlarmUserHighNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwPortalAccessProfileAlarmUserHighNum_Type.__name__ = "Integer32"
_HwPortalAccessProfileAlarmUserHighNum_Object = MibTableColumn
hwPortalAccessProfileAlarmUserHighNum = _HwPortalAccessProfileAlarmUserHighNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 7),
    _HwPortalAccessProfileAlarmUserHighNum_Type()
)
hwPortalAccessProfileAlarmUserHighNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfileAlarmUserHighNum.setStatus("current")


class _HwPortalAccessProfileAuthenNetWork_Type(OctetString):
    """Custom type hwPortalAccessProfileAuthenNetWork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_HwPortalAccessProfileAuthenNetWork_Type.__name__ = "OctetString"
_HwPortalAccessProfileAuthenNetWork_Object = MibTableColumn
hwPortalAccessProfileAuthenNetWork = _HwPortalAccessProfileAuthenNetWork_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 8),
    _HwPortalAccessProfileAuthenNetWork_Type()
)
hwPortalAccessProfileAuthenNetWork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfileAuthenNetWork.setStatus("current")


class _HwPortalAccessProfileAuthenNetWorkMask_Type(OctetString):
    """Custom type hwPortalAccessProfileAuthenNetWorkMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_HwPortalAccessProfileAuthenNetWorkMask_Type.__name__ = "OctetString"
_HwPortalAccessProfileAuthenNetWorkMask_Object = MibTableColumn
hwPortalAccessProfileAuthenNetWorkMask = _HwPortalAccessProfileAuthenNetWorkMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 9),
    _HwPortalAccessProfileAuthenNetWorkMask_Type()
)
hwPortalAccessProfileAuthenNetWorkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfileAuthenNetWorkMask.setStatus("current")


class _HwPortalAccessProfilePortalServerName_Type(DisplayString):
    """Custom type hwPortalAccessProfilePortalServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwPortalAccessProfilePortalServerName_Type.__name__ = "DisplayString"
_HwPortalAccessProfilePortalServerName_Object = MibTableColumn
hwPortalAccessProfilePortalServerName = _HwPortalAccessProfilePortalServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 10),
    _HwPortalAccessProfilePortalServerName_Type()
)
hwPortalAccessProfilePortalServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfilePortalServerName.setStatus("current")


class _HwPortalAccessProfilePortalAccessDirect_Type(Integer32):
    """Custom type hwPortalAccessProfilePortalAccessDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("invalid", 0),
          ("layer3", 3))
    )


_HwPortalAccessProfilePortalAccessDirect_Type.__name__ = "Integer32"
_HwPortalAccessProfilePortalAccessDirect_Object = MibTableColumn
hwPortalAccessProfilePortalAccessDirect = _HwPortalAccessProfilePortalAccessDirect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 11),
    _HwPortalAccessProfilePortalAccessDirect_Type()
)
hwPortalAccessProfilePortalAccessDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfilePortalAccessDirect.setStatus("current")
_HwPortalAccessProfileLocalServerEnable_Type = TruthValue
_HwPortalAccessProfileLocalServerEnable_Object = MibTableColumn
hwPortalAccessProfileLocalServerEnable = _HwPortalAccessProfileLocalServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 12),
    _HwPortalAccessProfileLocalServerEnable_Type()
)
hwPortalAccessProfileLocalServerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfileLocalServerEnable.setStatus("current")
_HwPortalAccessProfileLocalServerAnonymous_Type = TruthValue
_HwPortalAccessProfileLocalServerAnonymous_Object = MibTableColumn
hwPortalAccessProfileLocalServerAnonymous = _HwPortalAccessProfileLocalServerAnonymous_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 13),
    _HwPortalAccessProfileLocalServerAnonymous_Type()
)
hwPortalAccessProfileLocalServerAnonymous.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfileLocalServerAnonymous.setStatus("current")
_HwPortalAccessProfileRowStatus_Type = RowStatus
_HwPortalAccessProfileRowStatus_Object = MibTableColumn
hwPortalAccessProfileRowStatus = _HwPortalAccessProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 14),
    _HwPortalAccessProfileRowStatus_Type()
)
hwPortalAccessProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfileRowStatus.setStatus("current")


class _HwPortalAccessProfilePortalBackupServerName_Type(DisplayString):
    """Custom type hwPortalAccessProfilePortalBackupServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwPortalAccessProfilePortalBackupServerName_Type.__name__ = "DisplayString"
_HwPortalAccessProfilePortalBackupServerName_Object = MibTableColumn
hwPortalAccessProfilePortalBackupServerName = _HwPortalAccessProfilePortalBackupServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 66, 1, 15),
    _HwPortalAccessProfilePortalBackupServerName_Type()
)
hwPortalAccessProfilePortalBackupServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortalAccessProfilePortalBackupServerName.setStatus("current")
_HwAAAInboundVPNAccessUserStatTable_Object = MibTable
hwAAAInboundVPNAccessUserStatTable = _HwAAAInboundVPNAccessUserStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 67)
)
if mibBuilder.loadTexts:
    hwAAAInboundVPNAccessUserStatTable.setStatus("current")
_HwAAAInboundVPNAccessUserStatEntry_Object = MibTableRow
hwAAAInboundVPNAccessUserStatEntry = _HwAAAInboundVPNAccessUserStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 67, 1)
)
hwAAAInboundVPNAccessUserStatEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "hwAAAInboundVPNUserType"),
    (0, "HUAWEI-AAA-MIB", "hwAAAInboundVPNName"),
)
if mibBuilder.loadTexts:
    hwAAAInboundVPNAccessUserStatEntry.setStatus("current")


class _HwAAAInboundVPNUserType_Type(Integer32):
    """Custom type hwAAAInboundVPNUserType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 9),
          ("dhcp", 3),
          ("dualStack", 8),
          ("ipv4", 6),
          ("ipv6", 7),
          ("lac", 5),
          ("lns", 4),
          ("pppoa", 2),
          ("pppoe", 1))
    )


_HwAAAInboundVPNUserType_Type.__name__ = "Integer32"
_HwAAAInboundVPNUserType_Object = MibTableColumn
hwAAAInboundVPNUserType = _HwAAAInboundVPNUserType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 67, 1, 1),
    _HwAAAInboundVPNUserType_Type()
)
hwAAAInboundVPNUserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAAInboundVPNUserType.setStatus("current")


class _HwAAAInboundVPNName_Type(DisplayString):
    """Custom type hwAAAInboundVPNName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwAAAInboundVPNName_Type.__name__ = "DisplayString"
_HwAAAInboundVPNName_Object = MibTableColumn
hwAAAInboundVPNName = _HwAAAInboundVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 67, 1, 2),
    _HwAAAInboundVPNName_Type()
)
hwAAAInboundVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAAInboundVPNName.setStatus("current")


class _HwAAAInboundVPNAccessUserStat_Type(Integer32):
    """Custom type hwAAAInboundVPNAccessUserStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_HwAAAInboundVPNAccessUserStat_Type.__name__ = "Integer32"
_HwAAAInboundVPNAccessUserStat_Object = MibTableColumn
hwAAAInboundVPNAccessUserStat = _HwAAAInboundVPNAccessUserStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 67, 1, 3),
    _HwAAAInboundVPNAccessUserStat_Type()
)
hwAAAInboundVPNAccessUserStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAAAInboundVPNAccessUserStat.setStatus("current")
_UserAuthenticationFreeRuleExtTable_Object = MibTable
userAuthenticationFreeRuleExtTable = _UserAuthenticationFreeRuleExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68)
)
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleExtTable.setStatus("current")
_UserAuthenticationFreeRuleExtEntry_Object = MibTableRow
userAuthenticationFreeRuleExtEntry = _UserAuthenticationFreeRuleExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1)
)
userAuthenticationFreeRuleExtEntry.setIndexNames(
    (0, "HUAWEI-AAA-MIB", "userAuthenticationFreeRuleName"),
    (0, "HUAWEI-AAA-MIB", "userAuthenticationFreeRuleNumber"),
)
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleExtEntry.setStatus("current")


class _UserAuthenticationFreeRuleNumber_Type(Integer32):
    """Custom type userAuthenticationFreeRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 129),
    )


_UserAuthenticationFreeRuleNumber_Type.__name__ = "Integer32"
_UserAuthenticationFreeRuleNumber_Object = MibTableColumn
userAuthenticationFreeRuleNumber = _UserAuthenticationFreeRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 1),
    _UserAuthenticationFreeRuleNumber_Type()
)
userAuthenticationFreeRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleNumber.setStatus("current")


class _UserAuthenticationFreeRuleSourceMode_Type(Integer32):
    """Custom type userAuthenticationFreeRuleSourceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_UserAuthenticationFreeRuleSourceMode_Type.__name__ = "Integer32"
_UserAuthenticationFreeRuleSourceMode_Object = MibTableColumn
userAuthenticationFreeRuleSourceMode = _UserAuthenticationFreeRuleSourceMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 2),
    _UserAuthenticationFreeRuleSourceMode_Type()
)
userAuthenticationFreeRuleSourceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleSourceMode.setStatus("current")


class _UserAuthenticationFreeRuleSourceVlan_Type(Integer32):
    """Custom type userAuthenticationFreeRuleSourceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_UserAuthenticationFreeRuleSourceVlan_Type.__name__ = "Integer32"
_UserAuthenticationFreeRuleSourceVlan_Object = MibTableColumn
userAuthenticationFreeRuleSourceVlan = _UserAuthenticationFreeRuleSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 3),
    _UserAuthenticationFreeRuleSourceVlan_Type()
)
userAuthenticationFreeRuleSourceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleSourceVlan.setStatus("current")


class _UserAuthenticationFreeRuleSourceInterface_Type(OctetString):
    """Custom type userAuthenticationFreeRuleSourceInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_UserAuthenticationFreeRuleSourceInterface_Type.__name__ = "OctetString"
_UserAuthenticationFreeRuleSourceInterface_Object = MibTableColumn
userAuthenticationFreeRuleSourceInterface = _UserAuthenticationFreeRuleSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 4),
    _UserAuthenticationFreeRuleSourceInterface_Type()
)
userAuthenticationFreeRuleSourceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleSourceInterface.setStatus("current")
_UserAuthenticationFreeRuleSourceIP_Type = IpAddress
_UserAuthenticationFreeRuleSourceIP_Object = MibTableColumn
userAuthenticationFreeRuleSourceIP = _UserAuthenticationFreeRuleSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 5),
    _UserAuthenticationFreeRuleSourceIP_Type()
)
userAuthenticationFreeRuleSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleSourceIP.setStatus("current")
_UserAuthenticationFreeRuleSourceIPMask_Type = IpAddress
_UserAuthenticationFreeRuleSourceIPMask_Object = MibTableColumn
userAuthenticationFreeRuleSourceIPMask = _UserAuthenticationFreeRuleSourceIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 6),
    _UserAuthenticationFreeRuleSourceIPMask_Type()
)
userAuthenticationFreeRuleSourceIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleSourceIPMask.setStatus("current")
_UserAuthenticationFreeRuleSourceMac_Type = MacAddress
_UserAuthenticationFreeRuleSourceMac_Object = MibTableColumn
userAuthenticationFreeRuleSourceMac = _UserAuthenticationFreeRuleSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 7),
    _UserAuthenticationFreeRuleSourceMac_Type()
)
userAuthenticationFreeRuleSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleSourceMac.setStatus("current")


class _UserAuthenticationFreeRuleDestinationMode_Type(Integer32):
    """Custom type userAuthenticationFreeRuleDestinationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_UserAuthenticationFreeRuleDestinationMode_Type.__name__ = "Integer32"
_UserAuthenticationFreeRuleDestinationMode_Object = MibTableColumn
userAuthenticationFreeRuleDestinationMode = _UserAuthenticationFreeRuleDestinationMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 8),
    _UserAuthenticationFreeRuleDestinationMode_Type()
)
userAuthenticationFreeRuleDestinationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleDestinationMode.setStatus("current")
_UserAuthenticationFreeRuleDestinationIP_Type = IpAddress
_UserAuthenticationFreeRuleDestinationIP_Object = MibTableColumn
userAuthenticationFreeRuleDestinationIP = _UserAuthenticationFreeRuleDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 9),
    _UserAuthenticationFreeRuleDestinationIP_Type()
)
userAuthenticationFreeRuleDestinationIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleDestinationIP.setStatus("current")
_UserAuthenticationFreeRuleDestinationIPMask_Type = IpAddress
_UserAuthenticationFreeRuleDestinationIPMask_Object = MibTableColumn
userAuthenticationFreeRuleDestinationIPMask = _UserAuthenticationFreeRuleDestinationIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 10),
    _UserAuthenticationFreeRuleDestinationIPMask_Type()
)
userAuthenticationFreeRuleDestinationIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleDestinationIPMask.setStatus("current")


class _UserAuthenticationFreeRuleDestinationProtocol_Type(Integer32):
    """Custom type userAuthenticationFreeRuleDestinationProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_UserAuthenticationFreeRuleDestinationProtocol_Type.__name__ = "Integer32"
_UserAuthenticationFreeRuleDestinationProtocol_Object = MibTableColumn
userAuthenticationFreeRuleDestinationProtocol = _UserAuthenticationFreeRuleDestinationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 11),
    _UserAuthenticationFreeRuleDestinationProtocol_Type()
)
userAuthenticationFreeRuleDestinationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleDestinationProtocol.setStatus("current")
_UserAuthenticationFreeRuleDestinationPort_Type = Integer32
_UserAuthenticationFreeRuleDestinationPort_Object = MibTableColumn
userAuthenticationFreeRuleDestinationPort = _UserAuthenticationFreeRuleDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 12),
    _UserAuthenticationFreeRuleDestinationPort_Type()
)
userAuthenticationFreeRuleDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleDestinationPort.setStatus("current")


class _UserAuthenticationFreeRuleDestinationUserGroup_Type(OctetString):
    """Custom type userAuthenticationFreeRuleDestinationUserGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UserAuthenticationFreeRuleDestinationUserGroup_Type.__name__ = "OctetString"
_UserAuthenticationFreeRuleDestinationUserGroup_Object = MibTableColumn
userAuthenticationFreeRuleDestinationUserGroup = _UserAuthenticationFreeRuleDestinationUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 13),
    _UserAuthenticationFreeRuleDestinationUserGroup_Type()
)
userAuthenticationFreeRuleDestinationUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleDestinationUserGroup.setStatus("current")
_UserAuthenticationFreeRuleExtRowStatus_Type = RowStatus
_UserAuthenticationFreeRuleExtRowStatus_Object = MibTableColumn
userAuthenticationFreeRuleExtRowStatus = _UserAuthenticationFreeRuleExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 1, 68, 1, 14),
    _UserAuthenticationFreeRuleExtRowStatus_Type()
)
userAuthenticationFreeRuleExtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleExtRowStatus.setStatus("current")
_HwAAAMibTrap_ObjectIdentity = ObjectIdentity
hwAAAMibTrap = _HwAAAMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2)
)
_HwAAATrapOid_ObjectIdentity = ObjectIdentity
hwAAATrapOid = _HwAAATrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1)
)


class _HwDomainIndex_Type(Integer32):
    """Custom type hwDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1152),
    )


_HwDomainIndex_Type.__name__ = "Integer32"
_HwDomainIndex_Object = MibScalar
hwDomainIndex = _HwDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 1),
    _HwDomainIndex_Type()
)
hwDomainIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDomainIndex.setStatus("current")
_HwHdFreeamount_Type = Integer32
_HwHdFreeamount_Object = MibScalar
hwHdFreeamount = _HwHdFreeamount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 2),
    _HwHdFreeamount_Type()
)
hwHdFreeamount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwHdFreeamount.setStatus("current")
_HwHdWarningThreshold_Type = Integer32
_HwHdWarningThreshold_Object = MibScalar
hwHdWarningThreshold = _HwHdWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 3),
    _HwHdWarningThreshold_Type()
)
hwHdWarningThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwHdWarningThreshold.setStatus("current")
_HwUserSlot_Type = Integer32
_HwUserSlot_Object = MibScalar
hwUserSlot = _HwUserSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 4),
    _HwUserSlot_Type()
)
hwUserSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUserSlot.setStatus("current")
_HwUserSlotMaxNumThreshold_Type = Integer32
_HwUserSlotMaxNumThreshold_Object = MibScalar
hwUserSlotMaxNumThreshold = _HwUserSlotMaxNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 5),
    _HwUserSlotMaxNumThreshold_Type()
)
hwUserSlotMaxNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUserSlotMaxNumThreshold.setStatus("current")
_HwOnlineUserNumThreshold_Type = Integer32
_HwOnlineUserNumThreshold_Object = MibScalar
hwOnlineUserNumThreshold = _HwOnlineUserNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 6),
    _HwOnlineUserNumThreshold_Type()
)
hwOnlineUserNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwOnlineUserNumThreshold.setStatus("current")
_HwMaxUserThresholdType_Type = Integer32
_HwMaxUserThresholdType_Object = MibScalar
hwMaxUserThresholdType = _HwMaxUserThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 7),
    _HwMaxUserThresholdType_Type()
)
hwMaxUserThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMaxUserThresholdType.setStatus("current")


class _HwRbpChangeName_Type(DisplayString):
    """Custom type hwRbpChangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_HwRbpChangeName_Type.__name__ = "DisplayString"
_HwRbpChangeName_Object = MibScalar
hwRbpChangeName = _HwRbpChangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 8),
    _HwRbpChangeName_Type()
)
hwRbpChangeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRbpChangeName.setStatus("current")


class _HwRbpOldState_Type(Integer32):
    """Custom type hwRbpOldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("init", 0),
          ("master", 1))
    )


_HwRbpOldState_Type.__name__ = "Integer32"
_HwRbpOldState_Object = MibScalar
hwRbpOldState = _HwRbpOldState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 9),
    _HwRbpOldState_Type()
)
hwRbpOldState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRbpOldState.setStatus("current")


class _HwRbpNewState_Type(Integer32):
    """Custom type hwRbpNewState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("init", 0),
          ("master", 1))
    )


_HwRbpNewState_Type.__name__ = "Integer32"
_HwRbpNewState_Object = MibScalar
hwRbpNewState = _HwRbpNewState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 10),
    _HwRbpNewState_Type()
)
hwRbpNewState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRbpNewState.setStatus("current")


class _HwRbpChangeReason_Type(DisplayString):
    """Custom type hwRbpChangeReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_HwRbpChangeReason_Type.__name__ = "DisplayString"
_HwRbpChangeReason_Object = MibScalar
hwRbpChangeReason = _HwRbpChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 11),
    _HwRbpChangeReason_Type()
)
hwRbpChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRbpChangeReason.setStatus("current")


class _HwRbsName_Type(DisplayString):
    """Custom type hwRbsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_HwRbsName_Type.__name__ = "DisplayString"
_HwRbsName_Object = MibScalar
hwRbsName = _HwRbsName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 12),
    _HwRbsName_Type()
)
hwRbsName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRbsName.setStatus("current")


class _HwRbsDownReason_Type(DisplayString):
    """Custom type hwRbsDownReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_HwRbsDownReason_Type.__name__ = "DisplayString"
_HwRbsDownReason_Object = MibScalar
hwRbsDownReason = _HwRbsDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 13),
    _HwRbsDownReason_Type()
)
hwRbsDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRbsDownReason.setStatus("current")
_HwPolicyRouteThreshold_Type = Integer32
_HwPolicyRouteThreshold_Object = MibScalar
hwPolicyRouteThreshold = _HwPolicyRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 14),
    _HwPolicyRouteThreshold_Type()
)
hwPolicyRouteThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPolicyRouteThreshold.setStatus("current")


class _HwPolicyRoute_Type(DisplayString):
    """Custom type hwPolicyRoute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwPolicyRoute_Type.__name__ = "DisplayString"
_HwPolicyRoute_Object = MibScalar
hwPolicyRoute = _HwPolicyRoute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 15),
    _HwPolicyRoute_Type()
)
hwPolicyRoute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPolicyRoute.setStatus("current")
_HwRemoteDownloadAclUsedValue_Type = Integer32
_HwRemoteDownloadAclUsedValue_Object = MibScalar
hwRemoteDownloadAclUsedValue = _HwRemoteDownloadAclUsedValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 16),
    _HwRemoteDownloadAclUsedValue_Type()
)
hwRemoteDownloadAclUsedValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRemoteDownloadAclUsedValue.setStatus("current")
_HwRemoteDownloadAclThresholdValue_Type = Integer32
_HwRemoteDownloadAclThresholdValue_Object = MibScalar
hwRemoteDownloadAclThresholdValue = _HwRemoteDownloadAclThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 17),
    _HwRemoteDownloadAclThresholdValue_Type()
)
hwRemoteDownloadAclThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRemoteDownloadAclThresholdValue.setStatus("current")
_HwLoginFailedTimes_Type = Integer32
_HwLoginFailedTimes_Object = MibScalar
hwLoginFailedTimes = _HwLoginFailedTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 18),
    _HwLoginFailedTimes_Type()
)
hwLoginFailedTimes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLoginFailedTimes.setStatus("current")
_HwStatisticPeriod_Type = Integer32
_HwStatisticPeriod_Object = MibScalar
hwStatisticPeriod = _HwStatisticPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 19),
    _HwStatisticPeriod_Type()
)
hwStatisticPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStatisticPeriod.setStatus("current")
_HwUserGroupNumThreshold_Type = Integer32
_HwUserGroupNumThreshold_Object = MibScalar
hwUserGroupNumThreshold = _HwUserGroupNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 20),
    _HwUserGroupNumThreshold_Type()
)
hwUserGroupNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUserGroupNumThreshold.setStatus("current")
_HwUserGroupUsedNum_Type = Integer32
_HwUserGroupUsedNum_Object = MibScalar
hwUserGroupUsedNum = _HwUserGroupUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 21),
    _HwUserGroupUsedNum_Type()
)
hwUserGroupUsedNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUserGroupUsedNum.setStatus("current")
_HwAAACpuUsage_Type = Integer32
_HwAAACpuUsage_Object = MibScalar
hwAAACpuUsage = _HwAAACpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 22),
    _HwAAACpuUsage_Type()
)
hwAAACpuUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAACpuUsage.setStatus("current")
_HwAAAUserResourceUsage_Type = Integer32
_HwAAAUserResourceUsage_Object = MibScalar
hwAAAUserResourceUsage = _HwAAAUserResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 23),
    _HwAAAUserResourceUsage_Type()
)
hwAAAUserResourceUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAAUserResourceUsage.setStatus("current")


class _HwAAASessionGroupUpperLimitThreshold_Type(Integer32):
    """Custom type hwAAASessionGroupUpperLimitThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(255, 255),
    )


_HwAAASessionGroupUpperLimitThreshold_Type.__name__ = "Integer32"
_HwAAASessionGroupUpperLimitThreshold_Object = MibScalar
hwAAASessionGroupUpperLimitThreshold = _HwAAASessionGroupUpperLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 24),
    _HwAAASessionGroupUpperLimitThreshold_Type()
)
hwAAASessionGroupUpperLimitThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAASessionGroupUpperLimitThreshold.setStatus("current")


class _HwAAASessionGroupLowerLimitThreshold_Type(Integer32):
    """Custom type hwAAASessionGroupLowerLimitThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
        ValueRangeConstraint(255, 255),
    )


_HwAAASessionGroupLowerLimitThreshold_Type.__name__ = "Integer32"
_HwAAASessionGroupLowerLimitThreshold_Object = MibScalar
hwAAASessionGroupLowerLimitThreshold = _HwAAASessionGroupLowerLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 25),
    _HwAAASessionGroupLowerLimitThreshold_Type()
)
hwAAASessionGroupLowerLimitThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAASessionGroupLowerLimitThreshold.setStatus("current")


class _HwAAASessionUpperLimitThreshold_Type(Integer32):
    """Custom type hwAAASessionUpperLimitThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(255, 255),
    )


_HwAAASessionUpperLimitThreshold_Type.__name__ = "Integer32"
_HwAAASessionUpperLimitThreshold_Object = MibScalar
hwAAASessionUpperLimitThreshold = _HwAAASessionUpperLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 26),
    _HwAAASessionUpperLimitThreshold_Type()
)
hwAAASessionUpperLimitThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAASessionUpperLimitThreshold.setStatus("current")


class _HwAAASessionLowerLimitThreshold_Type(Integer32):
    """Custom type hwAAASessionLowerLimitThreshold based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
        ValueRangeConstraint(255, 255),
    )


_HwAAASessionLowerLimitThreshold_Type.__name__ = "Integer32"
_HwAAASessionLowerLimitThreshold_Object = MibScalar
hwAAASessionLowerLimitThreshold = _HwAAASessionLowerLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 27),
    _HwAAASessionLowerLimitThreshold_Type()
)
hwAAASessionLowerLimitThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAASessionLowerLimitThreshold.setStatus("current")


class _HwAAATimerExpireMajorLevelThreshold_Type(Unsigned32):
    """Custom type hwAAATimerExpireMajorLevelThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwAAATimerExpireMajorLevelThreshold_Type.__name__ = "Unsigned32"
_HwAAATimerExpireMajorLevelThreshold_Object = MibScalar
hwAAATimerExpireMajorLevelThreshold = _HwAAATimerExpireMajorLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 28),
    _HwAAATimerExpireMajorLevelThreshold_Type()
)
hwAAATimerExpireMajorLevelThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAATimerExpireMajorLevelThreshold.setStatus("current")


class _HwAAATimerExpireMajorLevelResumeThreshold_Type(Unsigned32):
    """Custom type hwAAATimerExpireMajorLevelResumeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwAAATimerExpireMajorLevelResumeThreshold_Type.__name__ = "Unsigned32"
_HwAAATimerExpireMajorLevelResumeThreshold_Object = MibScalar
hwAAATimerExpireMajorLevelResumeThreshold = _HwAAATimerExpireMajorLevelResumeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 29),
    _HwAAATimerExpireMajorLevelResumeThreshold_Type()
)
hwAAATimerExpireMajorLevelResumeThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAATimerExpireMajorLevelResumeThreshold.setStatus("current")


class _HwAAATimerExpireCriticalLevelThreshold_Type(Unsigned32):
    """Custom type hwAAATimerExpireCriticalLevelThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwAAATimerExpireCriticalLevelThreshold_Type.__name__ = "Unsigned32"
_HwAAATimerExpireCriticalLevelThreshold_Object = MibScalar
hwAAATimerExpireCriticalLevelThreshold = _HwAAATimerExpireCriticalLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 30),
    _HwAAATimerExpireCriticalLevelThreshold_Type()
)
hwAAATimerExpireCriticalLevelThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAATimerExpireCriticalLevelThreshold.setStatus("current")


class _HwAAATimerExpireCriticalLevelResumeThreshold_Type(Unsigned32):
    """Custom type hwAAATimerExpireCriticalLevelResumeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwAAATimerExpireCriticalLevelResumeThreshold_Type.__name__ = "Unsigned32"
_HwAAATimerExpireCriticalLevelResumeThreshold_Object = MibScalar
hwAAATimerExpireCriticalLevelResumeThreshold = _HwAAATimerExpireCriticalLevelResumeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 31),
    _HwAAATimerExpireCriticalLevelResumeThreshold_Type()
)
hwAAATimerExpireCriticalLevelResumeThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAATimerExpireCriticalLevelResumeThreshold.setStatus("current")
_HwMacMovedQuietUserSpec_Type = Integer32
_HwMacMovedQuietUserSpec_Object = MibScalar
hwMacMovedQuietUserSpec = _HwMacMovedQuietUserSpec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 32),
    _HwMacMovedQuietUserSpec_Type()
)
hwMacMovedQuietUserSpec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacMovedQuietUserSpec.setStatus("current")
_HwMacMovedUserPercentage_Type = Integer32
_HwMacMovedUserPercentage_Object = MibScalar
hwMacMovedUserPercentage = _HwMacMovedUserPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 33),
    _HwMacMovedUserPercentage_Type()
)
hwMacMovedUserPercentage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacMovedUserPercentage.setStatus("current")
_HwLowerMacMovedUserPercentage_Type = Integer32
_HwLowerMacMovedUserPercentage_Object = MibScalar
hwLowerMacMovedUserPercentage = _HwLowerMacMovedUserPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 34),
    _HwLowerMacMovedUserPercentage_Type()
)
hwLowerMacMovedUserPercentage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLowerMacMovedUserPercentage.setStatus("current")
_HwUpperMacMovedUserPercentage_Type = Integer32
_HwUpperMacMovedUserPercentage_Object = MibScalar
hwUpperMacMovedUserPercentage = _HwUpperMacMovedUserPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 35),
    _HwUpperMacMovedUserPercentage_Type()
)
hwUpperMacMovedUserPercentage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUpperMacMovedUserPercentage.setStatus("current")


class _HwAAAChasisIPv6AddressThreshold_Type(Unsigned32):
    """Custom type hwAAAChasisIPv6AddressThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwAAAChasisIPv6AddressThreshold_Type.__name__ = "Unsigned32"
_HwAAAChasisIPv6AddressThreshold_Object = MibScalar
hwAAAChasisIPv6AddressThreshold = _HwAAAChasisIPv6AddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 36),
    _HwAAAChasisIPv6AddressThreshold_Type()
)
hwAAAChasisIPv6AddressThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAAChasisIPv6AddressThreshold.setStatus("current")


class _HwAAASlotIPv6AddressThreshold_Type(Unsigned32):
    """Custom type hwAAASlotIPv6AddressThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwAAASlotIPv6AddressThreshold_Type.__name__ = "Unsigned32"
_HwAAASlotIPv6AddressThreshold_Object = MibScalar
hwAAASlotIPv6AddressThreshold = _HwAAASlotIPv6AddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 1, 37),
    _HwAAASlotIPv6AddressThreshold_Type()
)
hwAAASlotIPv6AddressThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAAASlotIPv6AddressThreshold.setStatus("current")
_HwAAATrapsDefine_ObjectIdentity = ObjectIdentity
hwAAATrapsDefine = _HwAAATrapsDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2)
)
_HwAAATraps_ObjectIdentity = ObjectIdentity
hwAAATraps = _HwAAATraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0)
)
_HwLAMTrapsDefine_ObjectIdentity = ObjectIdentity
hwLAMTrapsDefine = _HwLAMTrapsDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 3)
)
_HwLAMTraps_ObjectIdentity = ObjectIdentity
hwLAMTraps = _HwLAMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 3, 0)
)
_HwAaaConformance_ObjectIdentity = ObjectIdentity
hwAaaConformance = _HwAaaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5)
)
_HwAaaCompliances_ObjectIdentity = ObjectIdentity
hwAaaCompliances = _HwAaaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 1)
)
_HwAaaObjectGroups_ObjectIdentity = ObjectIdentity
hwAaaObjectGroups = _HwAaaObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2)
)

# Managed Objects groups

hwAuthenSchemeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 1)
)
hwAuthenSchemeGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAuthenSchemeName"),
        ("HUAWEI-AAA-MIB", "hwAuthenMethod"),
        ("HUAWEI-AAA-MIB", "hwAuthenRowStatus"),
        ("HUAWEI-AAA-MIB", "hwAuthenFailPolicy"),
        ("HUAWEI-AAA-MIB", "hwAuthenFailDomain"))
)
if mibBuilder.loadTexts:
    hwAuthenSchemeGroup.setStatus("current")

hwAcctSchemeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 2)
)
hwAcctSchemeGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAcctSchemeName"),
        ("HUAWEI-AAA-MIB", "hwAccMethod"),
        ("HUAWEI-AAA-MIB", "hwAcctStartFail"),
        ("HUAWEI-AAA-MIB", "hwAcctOnlineFail"),
        ("HUAWEI-AAA-MIB", "hwAccRealTimeInter"),
        ("HUAWEI-AAA-MIB", "hwAcctRowStatus"),
        ("HUAWEI-AAA-MIB", "hwAcctRealTimeIntervalUnit"))
)
if mibBuilder.loadTexts:
    hwAcctSchemeGroup.setStatus("current")

hwDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 3)
)
hwDomainGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwDomainAuthenSchemeName"),
        ("HUAWEI-AAA-MIB", "hwDomainAcctSchemeName"),
        ("HUAWEI-AAA-MIB", "hwDomainRadiusGroupName"),
        ("HUAWEI-AAA-MIB", "hwDomainAccessLimitNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIfSrcRoute"),
        ("HUAWEI-AAA-MIB", "hwDomainNextHopIP"),
        ("HUAWEI-AAA-MIB", "hwDomainIdleCutTime"),
        ("HUAWEI-AAA-MIB", "hwDomainIdleCutFlow"),
        ("HUAWEI-AAA-MIB", "hwDomainRowStatus"),
        ("HUAWEI-AAA-MIB", "hwDomainType"),
        ("HUAWEI-AAA-MIB", "hwDomainServiceSchemeName"),
        ("HUAWEI-AAA-MIB", "hwDomainIdleCutType"),
        ("HUAWEI-AAA-MIB", "hwDomainForcePushUrl"),
        ("HUAWEI-AAA-MIB", "hwDomainForcePushUrlTemplate"),
        ("HUAWEI-AAA-MIB", "hwStateBlockFirstTimeRangeName"),
        ("HUAWEI-AAA-MIB", "hwStateBlockSecondTimeRangeName"),
        ("HUAWEI-AAA-MIB", "hwStateBlockThirdTimeRangeName"),
        ("HUAWEI-AAA-MIB", "hwStateBlockForthTimeRangeName"),
        ("HUAWEI-AAA-MIB", "hwDomainFlowStatistic"))
)
if mibBuilder.loadTexts:
    hwDomainGroup.setStatus("current")

hwDomainExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 4)
)
hwDomainExtGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainPPPURL"),
        ("HUAWEI-AAA-MIB", "hwIfDomainActive"),
        ("HUAWEI-AAA-MIB", "hwPriority"),
        ("HUAWEI-AAA-MIB", "hwWebServerURL"),
        ("HUAWEI-AAA-MIB", "hwIPPoolOneName"),
        ("HUAWEI-AAA-MIB", "hwIPPoolTwoName"),
        ("HUAWEI-AAA-MIB", "hwIPPoolThreeName"),
        ("HUAWEI-AAA-MIB", "hwTwoLevelAcctRadiusGroupName"),
        ("HUAWEI-AAA-MIB", "hwVPDNGroupIndex"),
        ("HUAWEI-AAA-MIB", "hwUclIndex"),
        ("HUAWEI-AAA-MIB", "hwIfPPPoeURL"),
        ("HUAWEI-AAA-MIB", "hwUclGroupName"),
        ("HUAWEI-AAA-MIB", "hwVpdnGroupName"),
        ("HUAWEI-AAA-MIB", "hwDomainVrf"),
        ("HUAWEI-AAA-MIB", "hwDomainGre"),
        ("HUAWEI-AAA-MIB", "hwDomainRenewIPTag"),
        ("HUAWEI-AAA-MIB", "hwPortalURL"),
        ("HUAWEI-AAA-MIB", "hwPortalServerIP"),
        ("HUAWEI-AAA-MIB", "hwRedirectTimesLimit"),
        ("HUAWEI-AAA-MIB", "hwDot1xTemplate"),
        ("HUAWEI-AAA-MIB", "hwWebServerIP"),
        ("HUAWEI-AAA-MIB", "hwWebServerMode"),
        ("HUAWEI-AAA-MIB", "hwPoolWarningThreshold"),
        ("HUAWEI-AAA-MIB", "hwTacGroupName"),
        ("HUAWEI-AAA-MIB", "hwServicePolicyName"),
        ("HUAWEI-AAA-MIB", "hwCopsGroupSSGType"),
        ("HUAWEI-AAA-MIB", "hwDomainAuthorSchemeName"),
        ("HUAWEI-AAA-MIB", "hwDomainQoSProfile"),
        ("HUAWEI-AAA-MIB", "hwDomainZone"),
        ("HUAWEI-AAA-MIB", "hwIfL2tpRadiusForce"),
        ("HUAWEI-AAA-MIB", "hwDownPriority"),
        ("HUAWEI-AAA-MIB", "hwPPPForceAuthtype"),
        ("HUAWEI-AAA-MIB", "hwDnsIPAddress"),
        ("HUAWEI-AAA-MIB", "hwAdminUserPriority"),
        ("HUAWEI-AAA-MIB", "hwShapingTemplate"),
        ("HUAWEI-AAA-MIB", "hwDomainDPIPolicyName"),
        ("HUAWEI-AAA-MIB", "hwCopsGroupSIGType"),
        ("HUAWEI-AAA-MIB", "hwCopsGroupCIPNType"),
        ("HUAWEI-AAA-MIB", "hwPCReduceCir"),
        ("HUAWEI-AAA-MIB", "hwValAcctType"),
        ("HUAWEI-AAA-MIB", "hwValRadiusServer"),
        ("HUAWEI-AAA-MIB", "hwValCopsServer"),
        ("HUAWEI-AAA-MIB", "hwPCReducePir"),
        ("HUAWEI-AAA-MIB", "hwDomainInboundL2tpQoSProfile"),
        ("HUAWEI-AAA-MIB", "hwDomainOutboundL2tpQoSProfile"),
        ("HUAWEI-AAA-MIB", "hwIfMulticastForward"),
        ("HUAWEI-AAA-MIB", "hwMulticastVirtualSchedulRezCir"),
        ("HUAWEI-AAA-MIB", "hwMulticastVirtualSchedulRezPir"),
        ("HUAWEI-AAA-MIB", "hwMaxMulticastListNum"),
        ("HUAWEI-AAA-MIB", "hwMultiProfile"),
        ("HUAWEI-AAA-MIB", "hwDomainServiceType"),
        ("HUAWEI-AAA-MIB", "hwWebServerUrlParameter"),
        ("HUAWEI-AAA-MIB", "hwWebServerRedirectKeyMscgName"),
        ("HUAWEI-AAA-MIB", "hwPoratalServerUrlParameter"),
        ("HUAWEI-AAA-MIB", "hwPoratalServerFirstUrlKeyName"),
        ("HUAWEI-AAA-MIB", "hwPoratalServerFirstUrlKeyDefaultName"),
        ("HUAWEI-AAA-MIB", "hwDnsSecondIPAddress"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PrefixshareFlag"),
        ("HUAWEI-AAA-MIB", "hwUserBasicServiceIPType"),
        ("HUAWEI-AAA-MIB", "hwPriDnsIPv6Address"),
        ("HUAWEI-AAA-MIB", "hwSecDnsIPv6Address"),
        ("HUAWEI-AAA-MIB", "hwDualStackAccountingType"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolWarningThreshold"),
        ("HUAWEI-AAA-MIB", "hwIPv6CPWaitDHCPv6Delay"),
        ("HUAWEI-AAA-MIB", "hwIPv6ManagedAddressFlag"),
        ("HUAWEI-AAA-MIB", "hwIPv6CPIFIDAvailable"),
        ("HUAWEI-AAA-MIB", "hwIPv6OtherFlag"),
        ("HUAWEI-AAA-MIB", "hwIPv6CPAssignIFID"),
        ("HUAWEI-AAA-MIB", "hwMultiIPv6ProfileName"),
        ("HUAWEI-AAA-MIB", "hwWebServerURLSlave"),
        ("HUAWEI-AAA-MIB", "hwWebServerIPSlave"),
        ("HUAWEI-AAA-MIB", "hwBindAuthWebIP"),
        ("HUAWEI-AAA-MIB", "hwBindAuthWebVrf"),
        ("HUAWEI-AAA-MIB", "hwBindAuthWebIPSlave"),
        ("HUAWEI-AAA-MIB", "hwBindAuthWebVrfSlave"),
        ("HUAWEI-AAA-MIB", "hwExtVpdnGroupName"),
        ("HUAWEI-AAA-MIB", "hwDomainUserGroupName"),
        ("HUAWEI-AAA-MIB", "hwAFTRName"),
        ("HUAWEI-AAA-MIB", "hwDomainDhcpOpt64SepAndSeg"),
        ("HUAWEI-AAA-MIB", "hwDomainDhcpServerAck"))
)
if mibBuilder.loadTexts:
    hwDomainExtGroup.setStatus("current")

hwDomainStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 5)
)
hwDomainStatGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainAccessedNum"),
        ("HUAWEI-AAA-MIB", "hwDomainOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwDomainOnlinePPPUser"),
        ("HUAWEI-AAA-MIB", "hwDomainFlowDnByte"),
        ("HUAWEI-AAA-MIB", "hwDomainFlowDnPkt"),
        ("HUAWEI-AAA-MIB", "hwDomainFlowUpByte"),
        ("HUAWEI-AAA-MIB", "hwDomainFlowUpPkt"),
        ("HUAWEI-AAA-MIB", "hwDomainIPTotalNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPUsedNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPConflictNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPExcludeNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPIdleNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPUsedPercent"),
        ("HUAWEI-AAA-MIB", "hwDomainPPPoENum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6AddressTotalNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6AddressUsedNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6AddressFreeNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6AddressConflictNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6AddressExcludeNum"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6AddressUsedPercent"),
        ("HUAWEI-AAA-MIB", "hwDomainNDRAPrefixTotalNum"),
        ("HUAWEI-AAA-MIB", "hwDomainNDRAPrefixUsedNum"),
        ("HUAWEI-AAA-MIB", "hwDomainNDRAPrefixFreeNum"),
        ("HUAWEI-AAA-MIB", "hwDomainNDRAPrefixConflictNum"),
        ("HUAWEI-AAA-MIB", "hwDomainNDRAPrefixExcludeNum"),
        ("HUAWEI-AAA-MIB", "hwDomainNDRAPrefixUsedPercent"),
        ("HUAWEI-AAA-MIB", "hwDomainPDPrefixTotalNum"),
        ("HUAWEI-AAA-MIB", "hwDomainPDPrefixUsedNum"),
        ("HUAWEI-AAA-MIB", "hwDomainPDPrefixFreeNum"),
        ("HUAWEI-AAA-MIB", "hwDomainPDPrefixConflictNum"),
        ("HUAWEI-AAA-MIB", "hwDomainPDPrefixExcludeNum"),
        ("HUAWEI-AAA-MIB", "hwDomainPDPrefixUsedPercent"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6FlowDnByte"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6FlowDnPkt"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6FlowUpByte"),
        ("HUAWEI-AAA-MIB", "hwDomainIPv6FlowUpPkt"))
)
if mibBuilder.loadTexts:
    hwDomainStatGroup.setStatus("current")

hwAuthorSchemeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 6)
)
hwAuthorSchemeGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAuthorSchemeName"),
        ("HUAWEI-AAA-MIB", "hwAuthorMethod"),
        ("HUAWEI-AAA-MIB", "hwAuthorRowStatus"))
)
if mibBuilder.loadTexts:
    hwAuthorSchemeGroup.setStatus("current")

hwLocalUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 7)
)
hwLocalUserGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwLocalUserName"),
        ("HUAWEI-AAA-MIB", "hwLocalUserPassword"),
        ("HUAWEI-AAA-MIB", "hwLocalUserAccessType"),
        ("HUAWEI-AAA-MIB", "hwLocalUserPriority"),
        ("HUAWEI-AAA-MIB", "hwftpdirction"),
        ("HUAWEI-AAA-MIB", "hwQosProfileName"),
        ("HUAWEI-AAA-MIB", "hwLocalUserRowStatus"),
        ("HUAWEI-AAA-MIB", "hwLocalUserIpAddress"),
        ("HUAWEI-AAA-MIB", "hwLocalUserVpnInstance"),
        ("HUAWEI-AAA-MIB", "hwLocalUserAccessLimitNum"),
        ("HUAWEI-AAA-MIB", "hwLocalUserPasswordLifetimeMin"),
        ("HUAWEI-AAA-MIB", "hwLocalUserPasswordLifetimeMax"),
        ("HUAWEI-AAA-MIB", "hwLocalUserIfAllowWeakPassword"))
)
if mibBuilder.loadTexts:
    hwLocalUserGroup.setStatus("current")

hwLocalUserExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 8)
)
hwLocalUserExtGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwLocalUserState"),
        ("HUAWEI-AAA-MIB", "hwLocalUserNoCallBackVerify"),
        ("HUAWEI-AAA-MIB", "hwLocalUserCallBackDialStr"),
        ("HUAWEI-AAA-MIB", "hwLocalUserBlockFailTimes"),
        ("HUAWEI-AAA-MIB", "hwLocalUserBlockInterval"),
        ("HUAWEI-AAA-MIB", "hwLocalUserUserGroup"),
        ("HUAWEI-AAA-MIB", "hwLocalUserDeviceType"),
        ("HUAWEI-AAA-MIB", "hwLocalUserExpireDate"),
        ("HUAWEI-AAA-MIB", "hwLocalUserIdleTimeoutSecond"),
        ("HUAWEI-AAA-MIB", "hwLocalUserTimeRange"))
)
if mibBuilder.loadTexts:
    hwLocalUserExtGroup.setStatus("current")

hwAaaSettingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 9)
)
hwAaaSettingGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwRoamChar"),
        ("HUAWEI-AAA-MIB", "hwGlobalControl"),
        ("HUAWEI-AAA-MIB", "hwSystemRecord"),
        ("HUAWEI-AAA-MIB", "hwOutboundRecord"),
        ("HUAWEI-AAA-MIB", "hwCmdRecord"),
        ("HUAWEI-AAA-MIB", "hwPPPUserOfflineStandardize"),
        ("HUAWEI-AAA-MIB", "hwDomainNameParseDirection"),
        ("HUAWEI-AAA-MIB", "hwDomainNameLocation"),
        ("HUAWEI-AAA-MIB", "hwAccessSpeedNumber"),
        ("HUAWEI-AAA-MIB", "hwAccessSpeedPeriod"),
        ("HUAWEI-AAA-MIB", "hwRealmNameChar"),
        ("HUAWEI-AAA-MIB", "hwRealmParseDirection"),
        ("HUAWEI-AAA-MIB", "hwIPOXpassword"),
        ("HUAWEI-AAA-MIB", "hwAccessDelayTransitionStep"),
        ("HUAWEI-AAA-MIB", "hwAccessDelayTime"),
        ("HUAWEI-AAA-MIB", "hwAccessDelayMinTime"),
        ("HUAWEI-AAA-MIB", "hwParsePriority"),
        ("HUAWEI-AAA-MIB", "hwRealmNameLocation"),
        ("HUAWEI-AAA-MIB", "hwIPOXUsernameOption82"),
        ("HUAWEI-AAA-MIB", "hwIPOXUsernameIP"),
        ("HUAWEI-AAA-MIB", "hwIPOXUsernameSysname"),
        ("HUAWEI-AAA-MIB", "hwIPOXUsernameMAC"),
        ("HUAWEI-AAA-MIB", "hwDefaultUserName"),
        ("HUAWEI-AAA-MIB", "hwNasSerial"),
        ("HUAWEI-AAA-MIB", "hwAAAPasswordRepeatNumber"),
        ("HUAWEI-AAA-MIB", "hwAAAPasswordRemindDay"),
        ("HUAWEI-AAA-MIB", "hwOnlineUserNumLowerLimitThreshold"),
        ("HUAWEI-AAA-MIB", "hwOnlineUserNumUpperLimitThreshold"),
        ("HUAWEI-AAA-MIB", "hwIPOXpasswordKeyType"),
        ("HUAWEI-AAA-MIB", "hwReauthorizeEnable"),
        ("HUAWEI-AAA-MIB", "hwDomainNameDelimiter"),
        ("HUAWEI-AAA-MIB", "hwDomainNameSecurityDelimiter"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventAuthFailResponseFail"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventAuthFailVlan"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventAuthenServerDownResponseFail"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventAuthenServerDownVlan"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventClientNoResponseVlan"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventPreAuthVlan"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventAuthFailUserGroup"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventAuthenServerDownUserGroup"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventClientNoResponseUserGroup"),
        ("HUAWEI-AAA-MIB", "hwGlobalAuthEventPreAuthUserGroup"),
        ("HUAWEI-AAA-MIB", "hwTriggerLoose"),
        ("HUAWEI-AAA-MIB", "hwOfflineSpeedNumber"),
        ("HUAWEI-AAA-MIB", "hwAuthorModifyMode"),
        ("HUAWEI-AAA-MIB", "hwLocalRetryInterval"),
        ("HUAWEI-AAA-MIB", "hwLocalRetryTime"),
        ("HUAWEI-AAA-MIB", "hwLocalBlockTime"),
        ("HUAWEI-AAA-MIB", "hwRemoteRetryInterval"),
        ("HUAWEI-AAA-MIB", "hwRemoteRetryTime"),
        ("HUAWEI-AAA-MIB", "hwRemoteBlockTime"),
        ("HUAWEI-AAA-MIB", "hwBlockDisable"))
)
if mibBuilder.loadTexts:
    hwAaaSettingGroup.setStatus("current")

hwAaaStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 10)
)
hwAaaStatGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwTotalOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalPPPoeOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalPPPoAOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalftpOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalsshOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotaltelnetOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalVLANOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwHistoricMaxOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwResetHistoricMaxOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwResetOfflineReasonStatistic"),
        ("HUAWEI-AAA-MIB", "hwResetOnlineFailReasonStatistic"),
        ("HUAWEI-AAA-MIB", "hwMaxPPPoeOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalPortalServerUserNum"),
        ("HUAWEI-AAA-MIB", "hwMaxPortalServerUserNum"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv4OnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv6OnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalDualStackOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv4FlowDnByte"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv4FlowDnPkt"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv4FlowUpByte"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv4FlowUpPkt"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv6FlowDnByte"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv6FlowDnPkt"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv6FlowUpByte"),
        ("HUAWEI-AAA-MIB", "hwTotalIPv6FlowUpPkt"),
        ("HUAWEI-AAA-MIB", "hwHistoricMaxOnlineAcctReadyNum"),
        ("HUAWEI-AAA-MIB", "hwPubicLacUserNum"),
        ("HUAWEI-AAA-MIB", "hwHistoricMaxOnlineLocalNum"),
        ("HUAWEI-AAA-MIB", "hwHistoricMaxOnlineRemoteNum"),
        ("HUAWEI-AAA-MIB", "hwTotalLacOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalLnsOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalWlsOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwTotalWrdOnlineNum"))
)
if mibBuilder.loadTexts:
    hwAaaStatGroup.setStatus("current")

hwAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 11)
)
hwAccessGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAccessIndex"),
        ("HUAWEI-AAA-MIB", "hwAccessUserName"),
        ("HUAWEI-AAA-MIB", "hwAccessPortType"),
        ("HUAWEI-AAA-MIB", "hwAccessPriority"),
        ("HUAWEI-AAA-MIB", "hwAccessSlotNo"),
        ("HUAWEI-AAA-MIB", "hwAccessSubSlotNo"),
        ("HUAWEI-AAA-MIB", "hwAccessPortNo"),
        ("HUAWEI-AAA-MIB", "hwAccessVLANID"),
        ("HUAWEI-AAA-MIB", "hwAccessPVC"),
        ("HUAWEI-AAA-MIB", "hwAccessAuthenMethod"),
        ("HUAWEI-AAA-MIB", "hwAccessAcctMethod"),
        ("HUAWEI-AAA-MIB", "hwAccessIPAddress"),
        ("HUAWEI-AAA-MIB", "hwAccessVRF"),
        ("HUAWEI-AAA-MIB", "hwAccessMACAddress"),
        ("HUAWEI-AAA-MIB", "hwAccessIfIdleCut"),
        ("HUAWEI-AAA-MIB", "hwAccessIdleCutTime"),
        ("HUAWEI-AAA-MIB", "hwAccessIdleCutFlow"),
        ("HUAWEI-AAA-MIB", "hwAccessTimeLimit"),
        ("HUAWEI-AAA-MIB", "hwAccessTotalFlow64Limit"),
        ("HUAWEI-AAA-MIB", "hwAccessStartTime"),
        ("HUAWEI-AAA-MIB", "hwAccessCARIfUpActive"),
        ("HUAWEI-AAA-MIB", "hwAccessCARIfDnActive"),
        ("HUAWEI-AAA-MIB", "hwAccessUpFlow64"),
        ("HUAWEI-AAA-MIB", "hwAccessDnFlow64"),
        ("HUAWEI-AAA-MIB", "hwAccessUpPacket64"),
        ("HUAWEI-AAA-MIB", "hwAccessDnPacket64"),
        ("HUAWEI-AAA-MIB", "hwAccessCARUpCIR"),
        ("HUAWEI-AAA-MIB", "hwAccessCARUpPIR"),
        ("HUAWEI-AAA-MIB", "hwAccessCARUpCBS"),
        ("HUAWEI-AAA-MIB", "hwAccessCARUpPBS"),
        ("HUAWEI-AAA-MIB", "hwAccessCARDnCIR"),
        ("HUAWEI-AAA-MIB", "hwAccessCARDnPIR"),
        ("HUAWEI-AAA-MIB", "hwAccessCARDnCBS"),
        ("HUAWEI-AAA-MIB", "hwAccessCARDnPBS"),
        ("HUAWEI-AAA-MIB", "hwAccessDownPriority"),
        ("HUAWEI-AAA-MIB", "hwAccessQosProfile"),
        ("HUAWEI-AAA-MIB", "hwAccessInterface"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6IFID"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6WanAddress"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6WanPrefix"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6LanPrefix"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6LanPrefixLen"),
        ("HUAWEI-AAA-MIB", "hwAccessBasicIPType"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6WaitDelay"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6ManagedAddressFlag"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6CPIFIDAvailable"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6OtherFlag"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6CPAssignIFID"),
        ("HUAWEI-AAA-MIB", "hwAccessLineID"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6UpFlow64"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6DnFlow64"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6UpPacket64"),
        ("HUAWEI-AAA-MIB", "hwAccessIPv6DnPacket64"),
        ("HUAWEI-AAA-MIB", "hwAccessDeviceName"),
        ("HUAWEI-AAA-MIB", "hwAccessDeviceMACAddress"),
        ("HUAWEI-AAA-MIB", "hwAccessDevicePortName"),
        ("HUAWEI-AAA-MIB", "hwAccessAPID"))
)
if mibBuilder.loadTexts:
    hwAccessGroup.setStatus("current")

hwAccessExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 12)
)
hwAccessExtGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAccessUCLGroup"),
        ("HUAWEI-AAA-MIB", "hwAuthenticationState"),
        ("HUAWEI-AAA-MIB", "hwAuthorizationState"),
        ("HUAWEI-AAA-MIB", "hwAccountingState"),
        ("HUAWEI-AAA-MIB", "hwAccessDomainName"),
        ("HUAWEI-AAA-MIB", "hwIdleTimeLength"),
        ("HUAWEI-AAA-MIB", "hwAcctSessionID"),
        ("HUAWEI-AAA-MIB", "hwAccessStartAcctTime"),
        ("HUAWEI-AAA-MIB", "hwAccessNormalServerGroup"),
        ("HUAWEI-AAA-MIB", "hwAccessDomainAcctCopySeverGroup"),
        ("HUAWEI-AAA-MIB", "hwAccessPVlanAcctCopyServerGroup"),
        ("HUAWEI-AAA-MIB", "hwAccessCurAuthenPlace"),
        ("HUAWEI-AAA-MIB", "hwAccessActionFlag"),
        ("HUAWEI-AAA-MIB", "hwAccessAuthtype"),
        ("HUAWEI-AAA-MIB", "hwAccessType"),
        ("HUAWEI-AAA-MIB", "hwAccessOnlineTime"),
        ("HUAWEI-AAA-MIB", "hwAccessGateway"),
        ("HUAWEI-AAA-MIB", "hwAccessSSID"),
        ("HUAWEI-AAA-MIB", "hwAccessAPMAC"),
        ("HUAWEI-AAA-MIB", "hwAccessDomain"),
        ("HUAWEI-AAA-MIB", "hwAccessCurAccountingPlace"),
        ("HUAWEI-AAA-MIB", "hwAccessCurAuthorPlace"),
        ("HUAWEI-AAA-MIB", "hwAccessUserGroup"),
        ("HUAWEI-AAA-MIB", "hwAccessResourceInsufficientInbound"),
        ("HUAWEI-AAA-MIB", "hwAccessResourceInsufficientOutbound"))
)
if mibBuilder.loadTexts:
    hwAccessExtGroup.setStatus("current")

hwAcctSchemeExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 13)
)
hwAcctSchemeExtGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwIfRealtimeAcct"),
        ("HUAWEI-AAA-MIB", "hwRealtimeFailMaxnum"),
        ("HUAWEI-AAA-MIB", "hwStartFailOnlineIfSendInterim"))
)
if mibBuilder.loadTexts:
    hwAcctSchemeExtGroup.setStatus("current")

hwBillPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 14)
)
hwBillPoolGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwBillsPoolVolume"),
        ("HUAWEI-AAA-MIB", "hwBillsPoolNum"),
        ("HUAWEI-AAA-MIB", "hwBillsPoolAlarmThreshold"),
        ("HUAWEI-AAA-MIB", "hwBillsPoolBackupMode"),
        ("HUAWEI-AAA-MIB", "hwBillsPoolBackupInterval"),
        ("HUAWEI-AAA-MIB", "hwBillsPoolBackupNow"),
        ("HUAWEI-AAA-MIB", "hwBillsPoolReset"))
)
if mibBuilder.loadTexts:
    hwBillPoolGroup.setStatus("current")

hwBillTFTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 15)
)
hwBillTFTPGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwBillsTFTPSrvIP"),
        ("HUAWEI-AAA-MIB", "hwBillsTFTPMainFileName"))
)
if mibBuilder.loadTexts:
    hwBillTFTPGroup.setStatus("current")

hwUclGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 16)
)
hwUclGrpGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUclGrpName"),
        ("HUAWEI-AAA-MIB", "hwUclGrpRowStatus"))
)
if mibBuilder.loadTexts:
    hwUclGrpGroup.setStatus("current")

hwIpAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 17)
)
hwIpAccessGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwIPAccessIPaddress"),
        ("HUAWEI-AAA-MIB", "hwIPAccessCID"),
        ("HUAWEI-AAA-MIB", "hwIPAccessVRF"))
)
if mibBuilder.loadTexts:
    hwIpAccessGroup.setStatus("current")

hwCutAccessUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 18)
)
hwCutAccessUserGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwCutStartUserID"),
        ("HUAWEI-AAA-MIB", "hwCutEndUserID"),
        ("HUAWEI-AAA-MIB", "hwCutIPaddress"),
        ("HUAWEI-AAA-MIB", "hwCutMacAddres"),
        ("HUAWEI-AAA-MIB", "hwCutUserName"),
        ("HUAWEI-AAA-MIB", "hwCutUserAttri"),
        ("HUAWEI-AAA-MIB", "hwCutDomain"),
        ("HUAWEI-AAA-MIB", "hwCutIPPoolName"),
        ("HUAWEI-AAA-MIB", "hwCutIfIndex"),
        ("HUAWEI-AAA-MIB", "hwCutVlanID"),
        ("HUAWEI-AAA-MIB", "hwCutVPI"),
        ("HUAWEI-AAA-MIB", "hwCutVCI"),
        ("HUAWEI-AAA-MIB", "hwCutVRF"),
        ("HUAWEI-AAA-MIB", "hwCutAccessInterface"),
        ("HUAWEI-AAA-MIB", "hwCutUserSSID"),
        ("HUAWEI-AAA-MIB", "hwCutAccessSlot"),
        ("HUAWEI-AAA-MIB", "hwCutUserGroup"))
)
if mibBuilder.loadTexts:
    hwCutAccessUserGroup.setStatus("current")

hwAaaUserPppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 19)
)
hwAaaUserPppGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwTotalConnectNum"),
        ("HUAWEI-AAA-MIB", "hwTotalSuccessNum"),
        ("HUAWEI-AAA-MIB", "hwTotalLCPFailNum"),
        ("HUAWEI-AAA-MIB", "hwTotalAuthenFailNum"),
        ("HUAWEI-AAA-MIB", "hwTotalNCPFailNum"),
        ("HUAWEI-AAA-MIB", "hwTotalIPAllocFailNum"),
        ("HUAWEI-AAA-MIB", "hwTotalOtherPPPFailNum"))
)
if mibBuilder.loadTexts:
    hwAaaUserPppGroup.setStatus("current")

hwAaaUserWebandFastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 20)
)
hwAaaUserWebandFastGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwTotalWebConnectNum"),
        ("HUAWEI-AAA-MIB", "hwTotalSuccessWebConnectNum"))
)
if mibBuilder.loadTexts:
    hwAaaUserWebandFastGroup.setStatus("current")

hwAaaUserDot1XGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 21)
)
hwAaaUserDot1XGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwTotalDot1XConnectNum"),
        ("HUAWEI-AAA-MIB", "hwTotalSuccessDot1XConnectNum"))
)
if mibBuilder.loadTexts:
    hwAaaUserDot1XGroup.setStatus("current")

hwAaaUserBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 22)
)
hwAaaUserBindGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwTotalBindConnectNum"),
        ("HUAWEI-AAA-MIB", "hwTotalSuccessBindConnectNum"))
)
if mibBuilder.loadTexts:
    hwAaaUserBindGroup.setStatus("current")

hwRecordSchemeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 23)
)
hwRecordSchemeGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwRecordSchemeName"),
        ("HUAWEI-AAA-MIB", "hwRecordTacGroupName"),
        ("HUAWEI-AAA-MIB", "hwRecordRowStatus"))
)
if mibBuilder.loadTexts:
    hwRecordSchemeGroup.setStatus("current")

hwMACAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 24)
)
hwMACAccessGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwMACAccessMACAddress"),
        ("HUAWEI-AAA-MIB", "hwMACAccessCID"))
)
if mibBuilder.loadTexts:
    hwMACAccessGroup.setStatus("current")

hwSlotConnectNumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 25)
)
hwSlotConnectNumGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwSlotConnectNumSlot"),
        ("HUAWEI-AAA-MIB", "hwSlotConnectNumOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwSlotConnectNumMaxOnlineNum"),
        ("HUAWEI-AAA-MIB", "hwSlotConnectNumMaxOnlineAcctReadyNum"))
)
if mibBuilder.loadTexts:
    hwSlotConnectNumGroup.setStatus("current")

hwOfflineReasonStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 26)
)
hwOfflineReasonStatGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwOfflineReason"),
        ("HUAWEI-AAA-MIB", "hwOfflineReasonStatistic"),
        ("HUAWEI-AAA-MIB", "hwOnlineFailReasonStatistic"))
)
if mibBuilder.loadTexts:
    hwOfflineReasonStatGroup.setStatus("current")

hwMulticastListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 27)
)
hwMulticastListGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwMulticastListIndex"),
        ("HUAWEI-AAA-MIB", "hwMulticastListName"),
        ("HUAWEI-AAA-MIB", "hwMulticastListSourceIp"),
        ("HUAWEI-AAA-MIB", "hwMulticastListSourceIpMask"),
        ("HUAWEI-AAA-MIB", "hwMulticastListGroupIp"),
        ("HUAWEI-AAA-MIB", "hwMulticastListGroupIpMask"),
        ("HUAWEI-AAA-MIB", "hwMulticastListVpnInstance"),
        ("HUAWEI-AAA-MIB", "hwMulticastListRowStatus"))
)
if mibBuilder.loadTexts:
    hwMulticastListGroup.setStatus("current")

hwMulticastProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 28)
)
hwMulticastProfileGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwMulticastProfileIndex"),
        ("HUAWEI-AAA-MIB", "hwMulticastProfileName"),
        ("HUAWEI-AAA-MIB", "hwMulticastProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwMulticastProfileGroup.setStatus("current")

hwMulticastProfileExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 29)
)
hwMulticastProfileExtGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwMulticastListBindName"),
        ("HUAWEI-AAA-MIB", "hwMulticastProfileExtRowStatus"))
)
if mibBuilder.loadTexts:
    hwMulticastProfileExtGroup.setStatus("current")

hwAaaTrapOidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 30)
)
hwAaaTrapOidGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwHdFreeamount"),
        ("HUAWEI-AAA-MIB", "hwHdWarningThreshold"),
        ("HUAWEI-AAA-MIB", "hwUserSlot"),
        ("HUAWEI-AAA-MIB", "hwUserSlotMaxNumThreshold"),
        ("HUAWEI-AAA-MIB", "hwOnlineUserNumThreshold"),
        ("HUAWEI-AAA-MIB", "hwPolicyRoute"),
        ("HUAWEI-AAA-MIB", "hwPolicyRouteThreshold"),
        ("HUAWEI-AAA-MIB", "hwRbsDownReason"),
        ("HUAWEI-AAA-MIB", "hwRbpOldState"),
        ("HUAWEI-AAA-MIB", "hwRbpChangeName"),
        ("HUAWEI-AAA-MIB", "hwMaxUserThresholdType"),
        ("HUAWEI-AAA-MIB", "hwRbpNewState"),
        ("HUAWEI-AAA-MIB", "hwRbsName"),
        ("HUAWEI-AAA-MIB", "hwRbpChangeReason"),
        ("HUAWEI-AAA-MIB", "hwRemoteDownloadAclUsedValue"),
        ("HUAWEI-AAA-MIB", "hwRemoteDownloadAclThresholdValue"))
)
if mibBuilder.loadTexts:
    hwAaaTrapOidGroup.setStatus("current")

hwObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 33)
)
hwObsoleteGroup.setObjects(
    ("HUAWEI-AAA-MIB", "hwNtvUserProfileName")
)
if mibBuilder.loadTexts:
    hwObsoleteGroup.setStatus("obsolete")

hwServiceSchemeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 34)
)
hwServiceSchemeGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwServiceSchemeNextHopIp"),
        ("HUAWEI-AAA-MIB", "hwServiceSchemeUserPriority"),
        ("HUAWEI-AAA-MIB", "hwServiceSchemeIdleCutTime"),
        ("HUAWEI-AAA-MIB", "hwServiceSchemeIdleCutFlow"),
        ("HUAWEI-AAA-MIB", "hwServiceSchemeDnsFirst"),
        ("HUAWEI-AAA-MIB", "hwServiceSchemeDnsSecond"),
        ("HUAWEI-AAA-MIB", "hwSrvSchemeAdminUserPriority"),
        ("HUAWEI-AAA-MIB", "hwSrvSchemeIpPoolOneName"),
        ("HUAWEI-AAA-MIB", "hwSrvSchemeIpPoolTwoName"),
        ("HUAWEI-AAA-MIB", "hwSrvSchemeIpPoolThreeName"),
        ("HUAWEI-AAA-MIB", "hwServiceSchemeRowStatus"),
        ("HUAWEI-AAA-MIB", "hwServiceSchemeIdleCutType"),
        ("HUAWEI-AAA-MIB", "hwServiceSchemeIdleCutFlowValue"))
)
if mibBuilder.loadTexts:
    hwServiceSchemeGroup.setStatus("current")

hwDhcpOpt121RouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 35)
)
hwDhcpOpt121RouteGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDhcpOpt121RouteDestIp"),
        ("HUAWEI-AAA-MIB", "hwDhcpOpt121RouteMask"),
        ("HUAWEI-AAA-MIB", "hwDhcpOpt121RouteNextHop"),
        ("HUAWEI-AAA-MIB", "hwDhcpOpt121RouteRowStatus"))
)
if mibBuilder.loadTexts:
    hwDhcpOpt121RouteGroup.setStatus("current")

hwAccessDelayPerSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 36)
)
hwAccessDelayPerSlotGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAccessDelayPerSlotSlot"),
        ("HUAWEI-AAA-MIB", "hwAccessDelayPerSlotTransitionStep"),
        ("HUAWEI-AAA-MIB", "hwAccessDelayPerSlotMaxTime"),
        ("HUAWEI-AAA-MIB", "hwAccessDelayPerSlotMinTime"),
        ("HUAWEI-AAA-MIB", "hwAccessDelayPerSlotRowStatus"))
)
if mibBuilder.loadTexts:
    hwAccessDelayPerSlotGroup.setStatus("current")

hwVpnAccessUserStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 37)
)
hwVpnAccessUserStatGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserType"),
        ("HUAWEI-AAA-MIB", "hwVpnAccessUserStatVpnName"),
        ("HUAWEI-AAA-MIB", "hwVpnAccessUserStatUserStat"))
)
if mibBuilder.loadTexts:
    hwVpnAccessUserStatGroup.setStatus("current")

hwInterfaceAccessUserStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 38)
)
hwInterfaceAccessUserStatGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwInterfaceAccessUserStatInterfaceIndex"),
        ("HUAWEI-AAA-MIB", "hwInterfaceAccessUserStatUserStat"))
)
if mibBuilder.loadTexts:
    hwInterfaceAccessUserStatGroup.setStatus("current")

hwDomainAccessUserStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 39)
)
hwDomainAccessUserStatGroup.setObjects(
    ("HUAWEI-AAA-MIB", "hwDomainAccessUserStatUserStat")
)
if mibBuilder.loadTexts:
    hwDomainAccessUserStatGroup.setStatus("current")

hwSlotAccessUserStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 40)
)
hwSlotAccessUserStatGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwSlotAccessUserStatSlot"),
        ("HUAWEI-AAA-MIB", "hwSlotAccessUserStatUserStat"))
)
if mibBuilder.loadTexts:
    hwSlotAccessUserStatGroup.setStatus("current")

hwDomainIncludePoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 45)
)
hwDomainIncludePoolGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIncludeIPPoolGroupName"),
        ("HUAWEI-AAA-MIB", "hwDomainIncludeIPPoolGroupRowStates"))
)
if mibBuilder.loadTexts:
    hwDomainIncludePoolGroup.setStatus("current")

hwDomainIPPoolMoveTo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 46)
)
hwDomainIPPoolMoveTo.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIncludeIPPoolName"),
        ("HUAWEI-AAA-MIB", "hwDomainIncludeIPPoolMoveto"))
)
if mibBuilder.loadTexts:
    hwDomainIPPoolMoveTo.setStatus("current")

hwUserLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 47)
)
hwUserLogGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserLogAccess"),
        ("HUAWEI-AAA-MIB", "hwUserLogIPAddress"),
        ("HUAWEI-AAA-MIB", "hwUserLogPort"),
        ("HUAWEI-AAA-MIB", "hwUserLogVersion"),
        ("HUAWEI-AAA-MIB", "hwShowUserLogStatistic"),
        ("HUAWEI-AAA-MIB", "hwResetUserLogStatistic"))
)
if mibBuilder.loadTexts:
    hwUserLogGroup.setStatus("current")

hwGlobalDhcpOpt64SepAndSegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 48)
)
hwGlobalDhcpOpt64SepAndSegGroup.setObjects(
    ("HUAWEI-AAA-MIB", "hwGlobalDhcpOpt64SepAndSeg")
)
if mibBuilder.loadTexts:
    hwGlobalDhcpOpt64SepAndSegGroup.setStatus("current")

hwGlobalDhcpServerAckGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 49)
)
hwGlobalDhcpServerAckGroup.setObjects(
    ("HUAWEI-AAA-MIB", "hwGlobalDhcpServerAck")
)
if mibBuilder.loadTexts:
    hwGlobalDhcpServerAckGroup.setStatus("current")

hwReauthorizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 50)
)
hwReauthorizeGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwReauthorizeUsername"),
        ("HUAWEI-AAA-MIB", "hwReauthorizeUsergroup"))
)
if mibBuilder.loadTexts:
    hwReauthorizeGroup.setStatus("current")

hwWlanInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 56)
)
hwWlanInterfaceGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwWlanInterfaceIndex"),
        ("HUAWEI-AAA-MIB", "hwWlanInterfaceName"),
        ("HUAWEI-AAA-MIB", "hwWlanInterfaceDomainNameDelimiter"),
        ("HUAWEI-AAA-MIB", "hwWlanInterfaceDomainNameSecurityDelimiter"),
        ("HUAWEI-AAA-MIB", "hwWlanInterfaceDomainNameParseDirection"),
        ("HUAWEI-AAA-MIB", "hwWlanInterfaceDomainNameLocation"))
)
if mibBuilder.loadTexts:
    hwWlanInterfaceGroup.setStatus("current")

hwAuthorCmdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 57)
)
hwAuthorCmdGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAuthorCmdLevel"),
        ("HUAWEI-AAA-MIB", "hwAuthorCmdMode"),
        ("HUAWEI-AAA-MIB", "hwAuthorCmdRowStatus"))
)
if mibBuilder.loadTexts:
    hwAuthorCmdGroup.setStatus("current")

hwAAARateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 58)
)
hwAAARateGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAAARateDirection"),
        ("HUAWEI-AAA-MIB", "hwAAARateType"),
        ("HUAWEI-AAA-MIB", "hwAAARateRealPeak"),
        ("HUAWEI-AAA-MIB", "hwAAARateRealAverage"),
        ("HUAWEI-AAA-MIB", "hwAAARateRealUsedCount"),
        ("HUAWEI-AAA-MIB", "hwAAARateRealPercent"))
)
if mibBuilder.loadTexts:
    hwAAARateGroup.setStatus("current")

hwLocalUserPwPolicyAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 59)
)
hwLocalUserPwPolicyAdminGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAdminEnable"),
        ("HUAWEI-AAA-MIB", "hwAdminExpire"),
        ("HUAWEI-AAA-MIB", "hwAdminPwHistroyRecordNum"),
        ("HUAWEI-AAA-MIB", "hwAdminAlertBefore"),
        ("HUAWEI-AAA-MIB", "hwAdminAlertOrginal"))
)
if mibBuilder.loadTexts:
    hwLocalUserPwPolicyAdminGroup.setStatus("current")

hwLocalUserPwPolicyAccGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 60)
)
hwLocalUserPwPolicyAccGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAccEnable"),
        ("HUAWEI-AAA-MIB", "hwAccPwHistroyRecordNum"))
)
if mibBuilder.loadTexts:
    hwLocalUserPwPolicyAccGroup.setStatus("current")

hwAAADomainIPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 61)
)
hwAAADomainIPPoolGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAAADomainIPPoolName"),
        ("HUAWEI-AAA-MIB", "hwAAADomainIPPoolIndex"),
        ("HUAWEI-AAA-MIB", "hwAAADomainIPPoolConstantIndex"),
        ("HUAWEI-AAA-MIB", "hwAAADomainIPPoolPosition"),
        ("HUAWEI-AAA-MIB", "hwAAADomainIPPoolRowStatus"))
)
if mibBuilder.loadTexts:
    hwAAADomainIPPoolGroup.setStatus("current")

userAuthenProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 62)
)
userAuthenProfileGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "userAuthenProfileName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileDot1xAccessProfileName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileMacAuthenAccessProfileName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfilePortalAccessProfileName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileSingleAccess"),
        ("HUAWEI-AAA-MIB", "userAuthenProfilePreAuthenServiceSchemeName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfilePreAuthenUserGroupName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfilePreAuthenVLAN"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenFailAuthorServiceSchemeName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenFailAuthorUserGroupName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenFailAuthorVLAN"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenServerDownServiceSchemeName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenServerDownUserGroupName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenServerDownVLAN"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenServerDownResponseSuccess"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenServerUpReauthen"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileMacAuthenFirst"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileMACBypass"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileDot1xForceDomain"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileMACAuthenForceDomain"),
        ("HUAWEI-AAA-MIB", "userAuthenProfilePortalForceDomain"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileDot1xDefaultDomain"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileMACAuthenDefaultDomain"),
        ("HUAWEI-AAA-MIB", "userAuthenProfilePortalDefaultDomain"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileSecurityNameDelimiter"),
        ("HUAWEI-AAA-MIB", "userAuthenProfilePreAuthenReAuthenTimer"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenFailReAuthenTimer"),
        ("HUAWEI-AAA-MIB", "userAuthenProfilePreAuthenAgingTime"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenFailAgingTime"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileFreeRuleName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenSchemeName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthorSchemeName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAcctSchemeName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileServiceSchemeName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileUserGroupName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileRadiusServerName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileHwtacacsServerName"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenticationMode"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileMaxUser"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileAuthenFailAuthorResponseSuccess"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileArpDetect"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileArpDetectTimer"),
        ("HUAWEI-AAA-MIB", "userAuthenProfileRowStatus"))
)
if mibBuilder.loadTexts:
    userAuthenProfileGroup.setStatus("current")

userAuthenticationFreeRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 63)
)
userAuthenticationFreeRuleGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleName"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleACLNumber"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleIPv6ACLNumber"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleNumber"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleSourceMode"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleSourceVlan"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleSourceInterface"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleSourceIP"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleSourceIPMask"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleSourceMac"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleDestinationMode"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleDestinationIP"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleDestinationIPMask"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleDestinationProtocol"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleDestinationPort"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleDestinationUserGroup"),
        ("HUAWEI-AAA-MIB", "userAuthenticationFreeRuleRowStatus"))
)
if mibBuilder.loadTexts:
    userAuthenticationFreeRuleGroup.setStatus("current")

hwDot1xAccessProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 64)
)
hwDot1xAccessProfileGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDot1xAccessProfileName"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileGuestAuthorServiceSchemeName"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileGuestAuthorUserGroupName"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileGuestAuthorVLAN"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileHandshakeSwitch"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileHandShakePktType"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileHandshakeInterval"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileIfEAPEnd"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileEAPEndMethod"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileEAPNotifyPktEAPCode"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileEAPNotifyPktEAPType"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileReAuthenEnable"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileReauthenticationTimeout"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileClientTimeout"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileServerTimeout"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileTxPeriod"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileMaxRetryValue"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileSpeedLimitAuto"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileTriggerPktType"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileUnicastTrigger"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileURL"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileEthTrunkHandShakePeriod"),
        ("HUAWEI-AAA-MIB", "hwDot1xAccessProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwDot1xAccessProfileGroup.setStatus("current")

hwMACAuthenAccessProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 65)
)
hwMACAuthenAccessProfileGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileName"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileReAuthenEnable"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileReauthenticationTimeout"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileServerTimeout"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileUserNameFixedUserName"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileFixedPassword"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileMACAddressFormat"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileMACAddressPassword"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileUserNameDHCPOption"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileUserNameDHCPOSubOption"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileTriggerPktType"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileTriggerDHCPOptionType"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileDHCPRelaseOffline"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileDHCPRenewReAuthen"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfilePermitAuthenMAC"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfilePermitAuthenMACMask"),
        ("HUAWEI-AAA-MIB", "hwMACAuthenAccessProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwMACAuthenAccessProfileGroup.setStatus("current")

hwPortalAccessProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 66)
)
hwPortalAccessProfileGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwPortalAccessProfileName"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfileDetectPeriod"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfilePortalServerDownServiceSchemeName"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfilePortalServerDownUserGroupName"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfilePortalServerUpReAuthen"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfileAlarmUserLowNum"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfileAlarmUserHighNum"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfileAuthenNetWork"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfileAuthenNetWorkMask"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfilePortalServerName"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfilePortalAccessDirect"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfileLocalServerEnable"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfileRowStatus"),
        ("HUAWEI-AAA-MIB", "hwPortalAccessProfilePortalBackupServerName"))
)
if mibBuilder.loadTexts:
    hwPortalAccessProfileGroup.setStatus("current")


# Notification objects

hwUserIPAllocAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 1)
)
hwUserIPAllocAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwPoolWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwUserIPAllocAlarm.setStatus(
        "current"
    )

hwUserSlotMaxNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 2)
)
hwUserSlotMaxNum.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserSlot"),
        ("HUAWEI-AAA-MIB", "hwUserSlotMaxNumThreshold"))
)
if mibBuilder.loadTexts:
    hwUserSlotMaxNum.setStatus(
        "current"
    )

hwOnlineUserNumAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 3)
)
hwOnlineUserNumAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwOnlineUserNumThreshold")
)
if mibBuilder.loadTexts:
    hwOnlineUserNumAlarm.setStatus(
        "current"
    )

hwSetUserQosProfileFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 4)
)
hwSetUserQosProfileFail.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAccessIndex"),
        ("HUAWEI-AAA-MIB", "hwAccessUserName"),
        ("HUAWEI-AAA-MIB", "hwAccessQosProfile"))
)
if mibBuilder.loadTexts:
    hwSetUserQosProfileFail.setStatus(
        "current"
    )

hwUserMaxNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 5)
)
hwUserMaxNum.setObjects(
      *(("HUAWEI-AAA-MIB", "hwMaxUserThresholdType"),
        ("HUAWEI-AAA-MIB", "hwUserSlot"),
        ("HUAWEI-AAA-MIB", "hwUserSlotMaxNumThreshold"))
)
if mibBuilder.loadTexts:
    hwUserMaxNum.setStatus(
        "current"
    )

hwRbpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 6)
)
hwRbpStateChange.setObjects(
      *(("HUAWEI-AAA-MIB", "hwRbpChangeName"),
        ("HUAWEI-AAA-MIB", "hwRbpOldState"),
        ("HUAWEI-AAA-MIB", "hwRbpNewState"),
        ("HUAWEI-AAA-MIB", "hwRbpChangeReason"))
)
if mibBuilder.loadTexts:
    hwRbpStateChange.setStatus(
        "current"
    )

hwRbsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 7)
)
hwRbsDown.setObjects(
      *(("HUAWEI-AAA-MIB", "hwRbsName"),
        ("HUAWEI-AAA-MIB", "hwRbsDownReason"))
)
if mibBuilder.loadTexts:
    hwRbsDown.setStatus(
        "current"
    )

hwRbsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 8)
)
hwRbsUp.setObjects(
    ("HUAWEI-AAA-MIB", "hwRbsName")
)
if mibBuilder.loadTexts:
    hwRbsUp.setStatus(
        "current"
    )

hwUserIPv6AddressAllocAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 9)
)
hwUserIPv6AddressAllocAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwUserIPv6AddressAllocAlarm.setStatus(
        "current"
    )

hwUserNDRAPrefixAllocAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 10)
)
hwUserNDRAPrefixAllocAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwUserNDRAPrefixAllocAlarm.setStatus(
        "current"
    )

hwUserDelegationPrefixAllocAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 11)
)
hwUserDelegationPrefixAllocAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwUserDelegationPrefixAllocAlarm.setStatus(
        "current"
    )

hwUserIPAllocAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 12)
)
hwUserIPAllocAlarmResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwPoolWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwUserIPAllocAlarmResume.setStatus(
        "current"
    )

hwUserIPv6AddressAllocAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 13)
)
hwUserIPv6AddressAllocAlarmResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwUserIPv6AddressAllocAlarmResume.setStatus(
        "current"
    )

hwUserNDRAPrefixAllocAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 14)
)
hwUserNDRAPrefixAllocAlarmResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwUserNDRAPrefixAllocAlarmResume.setStatus(
        "current"
    )

hwUserDelegationPrefixAllocAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 15)
)
hwUserDelegationPrefixAllocAlarmResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwUserDelegationPrefixAllocAlarmResume.setStatus(
        "current"
    )

hwOnlineUserNumUpperLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 16)
)
hwOnlineUserNumUpperLimitAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwOnlineUserNumUpperLimitThreshold")
)
if mibBuilder.loadTexts:
    hwOnlineUserNumUpperLimitAlarm.setStatus(
        "current"
    )

hwOnlineUserNumUpperLimitResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 17)
)
hwOnlineUserNumUpperLimitResume.setObjects(
    ("HUAWEI-AAA-MIB", "hwOnlineUserNumUpperLimitThreshold")
)
if mibBuilder.loadTexts:
    hwOnlineUserNumUpperLimitResume.setStatus(
        "current"
    )

hwOnlineUserNumLowerLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 18)
)
hwOnlineUserNumLowerLimitAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwOnlineUserNumLowerLimitThreshold")
)
if mibBuilder.loadTexts:
    hwOnlineUserNumLowerLimitAlarm.setStatus(
        "current"
    )

hwOnlineUserNumLowerLimitResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 19)
)
hwOnlineUserNumLowerLimitResume.setObjects(
    ("HUAWEI-AAA-MIB", "hwOnlineUserNumLowerLimitThreshold")
)
if mibBuilder.loadTexts:
    hwOnlineUserNumLowerLimitResume.setStatus(
        "current"
    )

hwIPLowerlimitWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 20)
)
hwIPLowerlimitWarningAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwPoolLowerLimitWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwIPLowerlimitWarningAlarm.setStatus(
        "current"
    )

hwIPLowerlimitWarningResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 21)
)
hwIPLowerlimitWarningResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwPoolLowerLimitWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwIPLowerlimitWarningResume.setStatus(
        "current"
    )

hwIPv6AddressLowerlimitWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 22)
)
hwIPv6AddressLowerlimitWarningAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolLowerLimitWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwIPv6AddressLowerlimitWarningAlarm.setStatus(
        "current"
    )

hwIPv6AddressLowerlimitWarningResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 23)
)
hwIPv6AddressLowerlimitWarningResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolLowerLimitWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwIPv6AddressLowerlimitWarningResume.setStatus(
        "current"
    )

hwIPv6NDRAPrefixLowerlimitWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 24)
)
hwIPv6NDRAPrefixLowerlimitWarningAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolLowerLimitWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwIPv6NDRAPrefixLowerlimitWarningAlarm.setStatus(
        "current"
    )

hwIPv6NDRAPrefixLowerlimitWarningResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 25)
)
hwIPv6NDRAPrefixLowerlimitWarningResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolLowerLimitWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwIPv6NDRAPrefixLowerlimitWarningResume.setStatus(
        "current"
    )

hwIPv6PDPrefixLowerlimitWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 26)
)
hwIPv6PDPrefixLowerlimitWarningAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolLowerLimitWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwIPv6PDPrefixLowerlimitWarningAlarm.setStatus(
        "current"
    )

hwIPv6PDPrefixLowerlimitWarningResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 27)
)
hwIPv6PDPrefixLowerlimitWarningResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwDomainIndex"),
        ("HUAWEI-AAA-MIB", "hwDomainName"),
        ("HUAWEI-AAA-MIB", "hwIPv6PoolLowerLimitWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwIPv6PDPrefixLowerlimitWarningResume.setStatus(
        "current"
    )

hwPolicyRouteSlotMaxNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 28)
)
hwPolicyRouteSlotMaxNum.setObjects(
      *(("HUAWEI-AAA-MIB", "hwAccessSlotNo"),
        ("HUAWEI-AAA-MIB", "hwPolicyRouteThreshold"),
        ("HUAWEI-AAA-MIB", "hwAccessIndex"),
        ("HUAWEI-AAA-MIB", "hwPolicyRoute"))
)
if mibBuilder.loadTexts:
    hwPolicyRouteSlotMaxNum.setStatus(
        "current"
    )

hwRemoteDownloadAclThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 29)
)
hwRemoteDownloadAclThresholdAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwRemoteDownloadAclUsedValue"),
        ("HUAWEI-AAA-MIB", "hwRemoteDownloadAclThresholdValue"))
)
if mibBuilder.loadTexts:
    hwRemoteDownloadAclThresholdAlarm.setStatus(
        "current"
    )

hwRemoteDownloadAclThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 30)
)
hwRemoteDownloadAclThresholdResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwRemoteDownloadAclUsedValue"),
        ("HUAWEI-AAA-MIB", "hwRemoteDownloadAclThresholdValue"))
)
if mibBuilder.loadTexts:
    hwRemoteDownloadAclThresholdResume.setStatus(
        "current"
    )

hwAdminLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 31)
)
hwAdminLoginFailed.setObjects(
      *(("HUAWEI-AAA-MIB", "hwLoginFailedTimes"),
        ("HUAWEI-AAA-MIB", "hwStatisticPeriod"))
)
if mibBuilder.loadTexts:
    hwAdminLoginFailed.setStatus(
        "current"
    )

hwAdminLoginFailedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 32)
)
hwAdminLoginFailedClear.setObjects(
      *(("HUAWEI-AAA-MIB", "hwLoginFailedTimes"),
        ("HUAWEI-AAA-MIB", "hwStatisticPeriod"))
)
if mibBuilder.loadTexts:
    hwAdminLoginFailedClear.setStatus(
        "current"
    )

hwUserGroupThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 33)
)
hwUserGroupThresholdAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserGroupNumThreshold"),
        ("HUAWEI-AAA-MIB", "hwUserGroupUsedNum"))
)
if mibBuilder.loadTexts:
    hwUserGroupThresholdAlarm.setStatus(
        "current"
    )

hwUserGroupThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 34)
)
hwUserGroupThresholdResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserGroupNumThreshold"),
        ("HUAWEI-AAA-MIB", "hwUserGroupUsedNum"))
)
if mibBuilder.loadTexts:
    hwUserGroupThresholdResume.setStatus(
        "current"
    )

hwEDSGLicenseExpireAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 35)
)
if mibBuilder.loadTexts:
    hwEDSGLicenseExpireAlarm.setStatus(
        "current"
    )

hwEDSGLicenseExpireResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 36)
)
if mibBuilder.loadTexts:
    hwEDSGLicenseExpireResume.setStatus(
        "current"
    )

hwAAAAccessUserResourceOrCpuAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 37)
)
hwAAAAccessUserResourceOrCpuAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserSlot"),
        ("HUAWEI-AAA-MIB", "hwAAACpuUsage"),
        ("HUAWEI-AAA-MIB", "hwAAAUserResourceUsage"))
)
if mibBuilder.loadTexts:
    hwAAAAccessUserResourceOrCpuAlarm.setStatus(
        "current"
    )

hwAAAAccessUserResourceOrCpuResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 38)
)
hwAAAAccessUserResourceOrCpuResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserSlot"),
        ("HUAWEI-AAA-MIB", "hwAAACpuUsage"),
        ("HUAWEI-AAA-MIB", "hwAAAUserResourceUsage"))
)
if mibBuilder.loadTexts:
    hwAAAAccessUserResourceOrCpuResume.setStatus(
        "current"
    )

hwAAASessionGroupUpperLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 39)
)
hwAAASessionGroupUpperLimitAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAASessionGroupUpperLimitThreshold")
)
if mibBuilder.loadTexts:
    hwAAASessionGroupUpperLimitAlarm.setStatus(
        "current"
    )

hwAAASessionGroupUpperLimitResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 40)
)
hwAAASessionGroupUpperLimitResume.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAASessionGroupUpperLimitThreshold")
)
if mibBuilder.loadTexts:
    hwAAASessionGroupUpperLimitResume.setStatus(
        "current"
    )

hwAAASessionGroupLowerLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 41)
)
hwAAASessionGroupLowerLimitAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAASessionGroupLowerLimitThreshold")
)
if mibBuilder.loadTexts:
    hwAAASessionGroupLowerLimitAlarm.setStatus(
        "current"
    )

hwAAASessionGroupLowerLimitResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 42)
)
hwAAASessionGroupLowerLimitResume.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAASessionGroupLowerLimitThreshold")
)
if mibBuilder.loadTexts:
    hwAAASessionGroupLowerLimitResume.setStatus(
        "current"
    )

hwAAAOnlineSessoinUpperLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 43)
)
hwAAAOnlineSessoinUpperLimitAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAASessionUpperLimitThreshold")
)
if mibBuilder.loadTexts:
    hwAAAOnlineSessoinUpperLimitAlarm.setStatus(
        "current"
    )

hwAAAOnlineSessoinUpperLimitResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 44)
)
hwAAAOnlineSessoinUpperLimitResume.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAASessionUpperLimitThreshold")
)
if mibBuilder.loadTexts:
    hwAAAOnlineSessoinUpperLimitResume.setStatus(
        "current"
    )

hwAAAOnlineSessoinLowerLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 45)
)
hwAAAOnlineSessoinLowerLimitAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAASessionLowerLimitThreshold")
)
if mibBuilder.loadTexts:
    hwAAAOnlineSessoinLowerLimitAlarm.setStatus(
        "current"
    )

hwAAAOnlineSessoinLowerLimitResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 46)
)
hwAAAOnlineSessoinLowerLimitResume.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAASessionLowerLimitThreshold")
)
if mibBuilder.loadTexts:
    hwAAAOnlineSessoinLowerLimitResume.setStatus(
        "current"
    )

hwAAASlotOnlineUserNumAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 47)
)
hwAAASlotOnlineUserNumAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserSlot"),
        ("HUAWEI-AAA-MIB", "hwUserSlotMaxNumThreshold"))
)
if mibBuilder.loadTexts:
    hwAAASlotOnlineUserNumAlarm.setStatus(
        "current"
    )

hwAAASlotOnlineUserNumResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 48)
)
hwAAASlotOnlineUserNumResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserSlot"),
        ("HUAWEI-AAA-MIB", "hwUserSlotMaxNumThreshold"))
)
if mibBuilder.loadTexts:
    hwAAASlotOnlineUserNumResume.setStatus(
        "current"
    )

hwAAATimerExpireMajorLevelAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 49)
)
hwAAATimerExpireMajorLevelAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAATimerExpireMajorLevelThreshold")
)
if mibBuilder.loadTexts:
    hwAAATimerExpireMajorLevelAlarm.setStatus(
        "current"
    )

hwAAATimerExpireMajorLevelResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 50)
)
hwAAATimerExpireMajorLevelResume.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAATimerExpireMajorLevelResumeThreshold")
)
if mibBuilder.loadTexts:
    hwAAATimerExpireMajorLevelResume.setStatus(
        "current"
    )

hwAAATimerExpireCriticalLevelAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 51)
)
hwAAATimerExpireCriticalLevelAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAATimerExpireCriticalLevelThreshold")
)
if mibBuilder.loadTexts:
    hwAAATimerExpireCriticalLevelAlarm.setStatus(
        "current"
    )

hwAAATimerExpireCriticalLevelResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 52)
)
hwAAATimerExpireCriticalLevelResume.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAATimerExpireCriticalLevelResumeThreshold")
)
if mibBuilder.loadTexts:
    hwAAATimerExpireCriticalLevelResume.setStatus(
        "current"
    )

hwMacMovedQuietMaxUserAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 53)
)
hwMacMovedQuietMaxUserAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwMacMovedQuietUserSpec"),
        ("HUAWEI-AAA-MIB", "hwMacMovedUserPercentage"),
        ("HUAWEI-AAA-MIB", "hwLowerMacMovedUserPercentage"),
        ("HUAWEI-AAA-MIB", "hwUpperMacMovedUserPercentage"))
)
if mibBuilder.loadTexts:
    hwMacMovedQuietMaxUserAlarm.setStatus(
        "current"
    )

hwMacMovedQuietUserClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 54)
)
hwMacMovedQuietUserClearAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwMacMovedQuietUserSpec"),
        ("HUAWEI-AAA-MIB", "hwMacMovedUserPercentage"),
        ("HUAWEI-AAA-MIB", "hwLowerMacMovedUserPercentage"),
        ("HUAWEI-AAA-MIB", "hwUpperMacMovedUserPercentage"))
)
if mibBuilder.loadTexts:
    hwMacMovedQuietUserClearAlarm.setStatus(
        "current"
    )

hwAAAChasisIPv6AddressThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 55)
)
hwAAAChasisIPv6AddressThresholdAlarm.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAAChasisIPv6AddressThreshold")
)
if mibBuilder.loadTexts:
    hwAAAChasisIPv6AddressThresholdAlarm.setStatus(
        "current"
    )

hwAAAChasisIPv6AddressThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 56)
)
hwAAAChasisIPv6AddressThresholdResume.setObjects(
    ("HUAWEI-AAA-MIB", "hwAAAChasisIPv6AddressThreshold")
)
if mibBuilder.loadTexts:
    hwAAAChasisIPv6AddressThresholdResume.setStatus(
        "current"
    )

hwAAASlotIPv6AddressThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 57)
)
hwAAASlotIPv6AddressThresholdAlarm.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserSlot"),
        ("HUAWEI-AAA-MIB", "hwAAASlotIPv6AddressThreshold"))
)
if mibBuilder.loadTexts:
    hwAAASlotIPv6AddressThresholdAlarm.setStatus(
        "current"
    )

hwAAASlotIPv6AddressThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 2, 0, 58)
)
hwAAASlotIPv6AddressThresholdResume.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserSlot"),
        ("HUAWEI-AAA-MIB", "hwAAASlotIPv6AddressThreshold"))
)
if mibBuilder.loadTexts:
    hwAAASlotIPv6AddressThresholdResume.setStatus(
        "current"
    )

hwHarddiskoverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 3, 0, 1)
)
hwHarddiskoverflow.setObjects(
      *(("HUAWEI-AAA-MIB", "hwHdFreeamount"),
        ("HUAWEI-AAA-MIB", "hwHdWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwHarddiskoverflow.setStatus(
        "current"
    )

hwHarddiskReachThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 3, 0, 2)
)
hwHarddiskReachThreshold.setObjects(
      *(("HUAWEI-AAA-MIB", "hwHdFreeamount"),
        ("HUAWEI-AAA-MIB", "hwHdWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwHarddiskReachThreshold.setStatus(
        "current"
    )

hwHarddiskOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 3, 0, 3)
)
hwHarddiskOK.setObjects(
      *(("HUAWEI-AAA-MIB", "hwHdFreeamount"),
        ("HUAWEI-AAA-MIB", "hwHdWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwHarddiskOK.setStatus(
        "current"
    )

hwCachetoFTPFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 3, 0, 4)
)
hwCachetoFTPFail.setObjects(
      *(("HUAWEI-AAA-MIB", "hwHdFreeamount"),
        ("HUAWEI-AAA-MIB", "hwHdWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwCachetoFTPFail.setStatus(
        "current"
    )

hwHDtoFTPFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 2, 3, 0, 5)
)
hwHDtoFTPFail.setObjects(
      *(("HUAWEI-AAA-MIB", "hwHdFreeamount"),
        ("HUAWEI-AAA-MIB", "hwHdWarningThreshold"))
)
if mibBuilder.loadTexts:
    hwHDtoFTPFail.setStatus(
        "current"
    )


# Notifications groups

hwAaaTrapsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 31)
)
hwAaaTrapsNotificationsGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwUserIPAllocAlarm"),
        ("HUAWEI-AAA-MIB", "hwUserIPv6AddressAllocAlarm"),
        ("HUAWEI-AAA-MIB", "hwUserNDRAPrefixAllocAlarm"),
        ("HUAWEI-AAA-MIB", "hwUserDelegationPrefixAllocAlarm"),
        ("HUAWEI-AAA-MIB", "hwUserSlotMaxNum"),
        ("HUAWEI-AAA-MIB", "hwOnlineUserNumAlarm"),
        ("HUAWEI-AAA-MIB", "hwSetUserQosProfileFail"),
        ("HUAWEI-AAA-MIB", "hwUserMaxNum"),
        ("HUAWEI-AAA-MIB", "hwRbpStateChange"),
        ("HUAWEI-AAA-MIB", "hwRbsDown"),
        ("HUAWEI-AAA-MIB", "hwRbsUp"),
        ("HUAWEI-AAA-MIB", "hwUserIPAllocAlarmResume"),
        ("HUAWEI-AAA-MIB", "hwUserIPv6AddressAllocAlarmResume"),
        ("HUAWEI-AAA-MIB", "hwUserNDRAPrefixAllocAlarmResume"),
        ("HUAWEI-AAA-MIB", "hwUserDelegationPrefixAllocAlarmResume"),
        ("HUAWEI-AAA-MIB", "hwOnlineUserNumUpperLimitAlarm"),
        ("HUAWEI-AAA-MIB", "hwOnlineUserNumUpperLimitResume"),
        ("HUAWEI-AAA-MIB", "hwOnlineUserNumLowerLimitAlarm"),
        ("HUAWEI-AAA-MIB", "hwOnlineUserNumLowerLimitResume"),
        ("HUAWEI-AAA-MIB", "hwIPLowerlimitWarningAlarm"),
        ("HUAWEI-AAA-MIB", "hwIPLowerlimitWarningResume"),
        ("HUAWEI-AAA-MIB", "hwIPv6AddressLowerlimitWarningAlarm"),
        ("HUAWEI-AAA-MIB", "hwIPv6AddressLowerlimitWarningResume"),
        ("HUAWEI-AAA-MIB", "hwIPv6NDRAPrefixLowerlimitWarningAlarm"),
        ("HUAWEI-AAA-MIB", "hwIPv6NDRAPrefixLowerlimitWarningResume"),
        ("HUAWEI-AAA-MIB", "hwIPv6PDPrefixLowerlimitWarningAlarm"),
        ("HUAWEI-AAA-MIB", "hwIPv6PDPrefixLowerlimitWarningResume"),
        ("HUAWEI-AAA-MIB", "hwPolicyRouteSlotMaxNum"),
        ("HUAWEI-AAA-MIB", "hwRemoteDownloadAclThresholdAlarm"),
        ("HUAWEI-AAA-MIB", "hwRemoteDownloadAclThresholdResume"),
        ("HUAWEI-AAA-MIB", "hwAdminLoginFailed"),
        ("HUAWEI-AAA-MIB", "hwAdminLoginFailedClear"),
        ("HUAWEI-AAA-MIB", "hwUserGroupThresholdAlarm"),
        ("HUAWEI-AAA-MIB", "hwUserGroupThresholdResume"),
        ("HUAWEI-AAA-MIB", "hwEDSGLicenseExpireAlarm"),
        ("HUAWEI-AAA-MIB", "hwEDSGLicenseExpireResume"),
        ("HUAWEI-AAA-MIB", "hwAAAAccessUserResourceOrCpuAlarm"),
        ("HUAWEI-AAA-MIB", "hwAAAAccessUserResourceOrCpuResume"))
)
if mibBuilder.loadTexts:
    hwAaaTrapsNotificationsGroup.setStatus(
        "current"
    )

hwLamTrapsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 2, 32)
)
hwLamTrapsNotificationsGroup.setObjects(
      *(("HUAWEI-AAA-MIB", "hwHarddiskoverflow"),
        ("HUAWEI-AAA-MIB", "hwHarddiskReachThreshold"),
        ("HUAWEI-AAA-MIB", "hwHarddiskOK"),
        ("HUAWEI-AAA-MIB", "hwCachetoFTPFail"),
        ("HUAWEI-AAA-MIB", "hwHDtoFTPFail"))
)
if mibBuilder.loadTexts:
    hwLamTrapsNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwAaaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwAaaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-AAA-MIB",
    **{"hwAaa": hwAaa,
       "hwAAAMibObjects": hwAAAMibObjects,
       "hwAuthenSchemeTable": hwAuthenSchemeTable,
       "hwAuthenSchemeEntry": hwAuthenSchemeEntry,
       "hwAuthenSchemeName": hwAuthenSchemeName,
       "hwAuthenMethod": hwAuthenMethod,
       "hwAuthenRowStatus": hwAuthenRowStatus,
       "hwAuthenFailPolicy": hwAuthenFailPolicy,
       "hwAuthenFailDomain": hwAuthenFailDomain,
       "hwAcctSchemeTable": hwAcctSchemeTable,
       "hwAcctSchemeEntry": hwAcctSchemeEntry,
       "hwAcctSchemeName": hwAcctSchemeName,
       "hwAccMethod": hwAccMethod,
       "hwAcctStartFail": hwAcctStartFail,
       "hwAcctOnlineFail": hwAcctOnlineFail,
       "hwAccRealTimeInter": hwAccRealTimeInter,
       "hwAcctRowStatus": hwAcctRowStatus,
       "hwAcctRealTimeIntervalUnit": hwAcctRealTimeIntervalUnit,
       "hwDomainTable": hwDomainTable,
       "hwDomainEntry": hwDomainEntry,
       "hwDomainName": hwDomainName,
       "hwDomainAuthenSchemeName": hwDomainAuthenSchemeName,
       "hwDomainAcctSchemeName": hwDomainAcctSchemeName,
       "hwDomainRadiusGroupName": hwDomainRadiusGroupName,
       "hwDomainAccessLimitNum": hwDomainAccessLimitNum,
       "hwDomainIfSrcRoute": hwDomainIfSrcRoute,
       "hwDomainNextHopIP": hwDomainNextHopIP,
       "hwDomainIdleCutTime": hwDomainIdleCutTime,
       "hwDomainIdleCutFlow": hwDomainIdleCutFlow,
       "hwDomainRowStatus": hwDomainRowStatus,
       "hwDomainType": hwDomainType,
       "hwDomainServiceSchemeName": hwDomainServiceSchemeName,
       "hwDomainIdleCutType": hwDomainIdleCutType,
       "hwdomainipv6nexthop": hwdomainipv6nexthop,
       "hwDomainForcePushUrl": hwDomainForcePushUrl,
       "hwDomainForcePushUrlTemplate": hwDomainForcePushUrlTemplate,
       "hwStateBlockFirstTimeRangeName": hwStateBlockFirstTimeRangeName,
       "hwStateBlockSecondTimeRangeName": hwStateBlockSecondTimeRangeName,
       "hwStateBlockThirdTimeRangeName": hwStateBlockThirdTimeRangeName,
       "hwStateBlockForthTimeRangeName": hwStateBlockForthTimeRangeName,
       "hwDomainFlowStatistic": hwDomainFlowStatistic,
       "hwDomainExtTable": hwDomainExtTable,
       "hwDomainExtEntry": hwDomainExtEntry,
       "hwDomainPPPURL": hwDomainPPPURL,
       "hwIfDomainActive": hwIfDomainActive,
       "hwPriority": hwPriority,
       "hwWebServerURL": hwWebServerURL,
       "hwIPPoolOneName": hwIPPoolOneName,
       "hwIPPoolTwoName": hwIPPoolTwoName,
       "hwIPPoolThreeName": hwIPPoolThreeName,
       "hwTwoLevelAcctRadiusGroupName": hwTwoLevelAcctRadiusGroupName,
       "hwVPDNGroupIndex": hwVPDNGroupIndex,
       "hwUclIndex": hwUclIndex,
       "hwIfPPPoeURL": hwIfPPPoeURL,
       "hwUclGroupName": hwUclGroupName,
       "hwVpdnGroupName": hwVpdnGroupName,
       "hwDomainVrf": hwDomainVrf,
       "hwDomainGre": hwDomainGre,
       "hwDomainRenewIPTag": hwDomainRenewIPTag,
       "hwPortalURL": hwPortalURL,
       "hwPortalServerIP": hwPortalServerIP,
       "hwRedirectTimesLimit": hwRedirectTimesLimit,
       "hwDot1xTemplate": hwDot1xTemplate,
       "hwWebServerIP": hwWebServerIP,
       "hwWebServerMode": hwWebServerMode,
       "hwPoolWarningThreshold": hwPoolWarningThreshold,
       "hwTacGroupName": hwTacGroupName,
       "hwServicePolicyName": hwServicePolicyName,
       "hwCopsGroupSSGType": hwCopsGroupSSGType,
       "hwDomainAuthorSchemeName": hwDomainAuthorSchemeName,
       "hwNtvUserProfileName": hwNtvUserProfileName,
       "hwDomainQoSProfile": hwDomainQoSProfile,
       "hwDomainZone": hwDomainZone,
       "hwIfL2tpRadiusForce": hwIfL2tpRadiusForce,
       "hwDownPriority": hwDownPriority,
       "hwPPPForceAuthtype": hwPPPForceAuthtype,
       "hwDnsIPAddress": hwDnsIPAddress,
       "hwAdminUserPriority": hwAdminUserPriority,
       "hwShapingTemplate": hwShapingTemplate,
       "hwDomainDPIPolicyName": hwDomainDPIPolicyName,
       "hwCopsGroupSIGType": hwCopsGroupSIGType,
       "hwCopsGroupCIPNType": hwCopsGroupCIPNType,
       "hwPCReduceCir": hwPCReduceCir,
       "hwValAcctType": hwValAcctType,
       "hwValRadiusServer": hwValRadiusServer,
       "hwValCopsServer": hwValCopsServer,
       "hwPCReducePir": hwPCReducePir,
       "hwDomainInboundL2tpQoSProfile": hwDomainInboundL2tpQoSProfile,
       "hwDomainOutboundL2tpQoSProfile": hwDomainOutboundL2tpQoSProfile,
       "hwIfMulticastForward": hwIfMulticastForward,
       "hwMulticastVirtualSchedulRezCir": hwMulticastVirtualSchedulRezCir,
       "hwMulticastVirtualSchedulRezPir": hwMulticastVirtualSchedulRezPir,
       "hwMaxMulticastListNum": hwMaxMulticastListNum,
       "hwMultiProfile": hwMultiProfile,
       "hwDomainServiceType": hwDomainServiceType,
       "hwWebServerUrlParameter": hwWebServerUrlParameter,
       "hwWebServerRedirectKeyMscgName": hwWebServerRedirectKeyMscgName,
       "hwPoratalServerUrlParameter": hwPoratalServerUrlParameter,
       "hwPoratalServerFirstUrlKeyName": hwPoratalServerFirstUrlKeyName,
       "hwPoratalServerFirstUrlKeyDefaultName": hwPoratalServerFirstUrlKeyDefaultName,
       "hwDnsSecondIPAddress": hwDnsSecondIPAddress,
       "hwDomainIgmpEnable": hwDomainIgmpEnable,
       "hwIPv6PoolName": hwIPv6PoolName,
       "hwIPv6PrefixshareFlag": hwIPv6PrefixshareFlag,
       "hwUserBasicServiceIPType": hwUserBasicServiceIPType,
       "hwPriDnsIPv6Address": hwPriDnsIPv6Address,
       "hwSecDnsIPv6Address": hwSecDnsIPv6Address,
       "hwDualStackAccountingType": hwDualStackAccountingType,
       "hwIPv6PoolWarningThreshold": hwIPv6PoolWarningThreshold,
       "hwIPv6CPWaitDHCPv6Delay": hwIPv6CPWaitDHCPv6Delay,
       "hwIPv6ManagedAddressFlag": hwIPv6ManagedAddressFlag,
       "hwIPv6CPIFIDAvailable": hwIPv6CPIFIDAvailable,
       "hwIPv6OtherFlag": hwIPv6OtherFlag,
       "hwIPv6CPAssignIFID": hwIPv6CPAssignIFID,
       "hwMultiIPv6ProfileName": hwMultiIPv6ProfileName,
       "hwWebServerURLSlave": hwWebServerURLSlave,
       "hwWebServerIPSlave": hwWebServerIPSlave,
       "hwBindAuthWebIP": hwBindAuthWebIP,
       "hwBindAuthWebVrf": hwBindAuthWebVrf,
       "hwBindAuthWebIPSlave": hwBindAuthWebIPSlave,
       "hwBindAuthWebVrfSlave": hwBindAuthWebVrfSlave,
       "hwExtVpdnGroupName": hwExtVpdnGroupName,
       "hwDomainUserGroupName": hwDomainUserGroupName,
       "hwAFTRName": hwAFTRName,
       "hwDomainDhcpOpt64SepAndSeg": hwDomainDhcpOpt64SepAndSeg,
       "hwDomainDhcpServerAck": hwDomainDhcpServerAck,
       "hwDomainStatTable": hwDomainStatTable,
       "hwDomainStatEntry": hwDomainStatEntry,
       "hwDomainAccessedNum": hwDomainAccessedNum,
       "hwDomainOnlineNum": hwDomainOnlineNum,
       "hwDomainOnlinePPPUser": hwDomainOnlinePPPUser,
       "hwDomainFlowDnByte": hwDomainFlowDnByte,
       "hwDomainFlowDnPkt": hwDomainFlowDnPkt,
       "hwDomainFlowUpByte": hwDomainFlowUpByte,
       "hwDomainFlowUpPkt": hwDomainFlowUpPkt,
       "hwDomainIPTotalNum": hwDomainIPTotalNum,
       "hwDomainIPUsedNum": hwDomainIPUsedNum,
       "hwDomainIPConflictNum": hwDomainIPConflictNum,
       "hwDomainIPExcludeNum": hwDomainIPExcludeNum,
       "hwDomainIPIdleNum": hwDomainIPIdleNum,
       "hwDomainIPUsedPercent": hwDomainIPUsedPercent,
       "hwDomainPPPoENum": hwDomainPPPoENum,
       "hwDomainAuthenRequestsRcvNum": hwDomainAuthenRequestsRcvNum,
       "hwDomainAuthenAcceptsNum": hwDomainAuthenAcceptsNum,
       "hwDomainAuthenRejectsNum": hwDomainAuthenRejectsNum,
       "hwDomainAcctRequestsRcvNum": hwDomainAcctRequestsRcvNum,
       "hwDomainAcctRspSuccessNum": hwDomainAcctRspSuccessNum,
       "hwDomainAcctRspFailuresNum": hwDomainAcctRspFailuresNum,
       "hwDomainIPv6AddressTotalNum": hwDomainIPv6AddressTotalNum,
       "hwDomainIPv6AddressUsedNum": hwDomainIPv6AddressUsedNum,
       "hwDomainIPv6AddressFreeNum": hwDomainIPv6AddressFreeNum,
       "hwDomainIPv6AddressConflictNum": hwDomainIPv6AddressConflictNum,
       "hwDomainIPv6AddressExcludeNum": hwDomainIPv6AddressExcludeNum,
       "hwDomainIPv6AddressUsedPercent": hwDomainIPv6AddressUsedPercent,
       "hwDomainNDRAPrefixTotalNum": hwDomainNDRAPrefixTotalNum,
       "hwDomainNDRAPrefixUsedNum": hwDomainNDRAPrefixUsedNum,
       "hwDomainNDRAPrefixFreeNum": hwDomainNDRAPrefixFreeNum,
       "hwDomainNDRAPrefixConflictNum": hwDomainNDRAPrefixConflictNum,
       "hwDomainNDRAPrefixExcludeNum": hwDomainNDRAPrefixExcludeNum,
       "hwDomainNDRAPrefixUsedPercent": hwDomainNDRAPrefixUsedPercent,
       "hwDomainPDPrefixTotalNum": hwDomainPDPrefixTotalNum,
       "hwDomainPDPrefixUsedNum": hwDomainPDPrefixUsedNum,
       "hwDomainPDPrefixFreeNum": hwDomainPDPrefixFreeNum,
       "hwDomainPDPrefixConflictNum": hwDomainPDPrefixConflictNum,
       "hwDomainPDPrefixExcludeNum": hwDomainPDPrefixExcludeNum,
       "hwDomainPDPrefixUsedPercent": hwDomainPDPrefixUsedPercent,
       "hwDomainIPv6FlowDnByte": hwDomainIPv6FlowDnByte,
       "hwDomainIPv6FlowDnPkt": hwDomainIPv6FlowDnPkt,
       "hwDomainIPv6FlowUpByte": hwDomainIPv6FlowUpByte,
       "hwDomainIPv6FlowUpPkt": hwDomainIPv6FlowUpPkt,
       "hwAuthorSchemeTable": hwAuthorSchemeTable,
       "hwAuthorSchemeEntry": hwAuthorSchemeEntry,
       "hwAuthorSchemeName": hwAuthorSchemeName,
       "hwAuthorMethod": hwAuthorMethod,
       "hwAuthorRowStatus": hwAuthorRowStatus,
       "hwLocalUserTable": hwLocalUserTable,
       "hwLocalUserEntry": hwLocalUserEntry,
       "hwLocalUserName": hwLocalUserName,
       "hwLocalUserPassword": hwLocalUserPassword,
       "hwLocalUserAccessType": hwLocalUserAccessType,
       "hwLocalUserPriority": hwLocalUserPriority,
       "hwftpdirction": hwftpdirction,
       "hwQosProfileName": hwQosProfileName,
       "hwLocalUserRowStatus": hwLocalUserRowStatus,
       "hwLocalUserIpAddress": hwLocalUserIpAddress,
       "hwLocalUserVpnInstance": hwLocalUserVpnInstance,
       "hwLocalUserAccessLimitNum": hwLocalUserAccessLimitNum,
       "hwLocalUserPasswordLifetimeMin": hwLocalUserPasswordLifetimeMin,
       "hwLocalUserPasswordLifetimeMax": hwLocalUserPasswordLifetimeMax,
       "hwLocalUserIfAllowWeakPassword": hwLocalUserIfAllowWeakPassword,
       "hwLocalUserPasswordSetTime": hwLocalUserPasswordSetTime,
       "hwLocalUserPasswordExpireTime": hwLocalUserPasswordExpireTime,
       "hwLocalUserPasswordIsExpired": hwLocalUserPasswordIsExpired,
       "hwLocalUserPasswordIsOrginal": hwLocalUserPasswordIsOrginal,
       "hwLocalUserExtTable": hwLocalUserExtTable,
       "hwLocalUserExtEntry": hwLocalUserExtEntry,
       "hwLocalUserState": hwLocalUserState,
       "hwLocalUserNoCallBackVerify": hwLocalUserNoCallBackVerify,
       "hwLocalUserCallBackDialStr": hwLocalUserCallBackDialStr,
       "hwLocalUserBlockFailTimes": hwLocalUserBlockFailTimes,
       "hwLocalUserBlockInterval": hwLocalUserBlockInterval,
       "hwLocalUserUserGroup": hwLocalUserUserGroup,
       "hwLocalUserDeviceType": hwLocalUserDeviceType,
       "hwLocalUserExpireDate": hwLocalUserExpireDate,
       "hwLocalUserIdleTimeoutSecond": hwLocalUserIdleTimeoutSecond,
       "hwLocalUserTimeRange": hwLocalUserTimeRange,
       "hwAAASetting": hwAAASetting,
       "hwAAASettingEntry": hwAAASettingEntry,
       "hwRoamChar": hwRoamChar,
       "hwGlobalControl": hwGlobalControl,
       "hwSystemRecord": hwSystemRecord,
       "hwOutboundRecord": hwOutboundRecord,
       "hwCmdRecord": hwCmdRecord,
       "hwPPPUserOfflineStandardize": hwPPPUserOfflineStandardize,
       "hwDomainNameParseDirection": hwDomainNameParseDirection,
       "hwDomainNameLocation": hwDomainNameLocation,
       "hwAccessSpeedNumber": hwAccessSpeedNumber,
       "hwAccessSpeedPeriod": hwAccessSpeedPeriod,
       "hwRealmNameChar": hwRealmNameChar,
       "hwRealmParseDirection": hwRealmParseDirection,
       "hwIPOXpassword": hwIPOXpassword,
       "hwAccessDelayTransitionStep": hwAccessDelayTransitionStep,
       "hwAccessDelayTime": hwAccessDelayTime,
       "hwAccessDelayMinTime": hwAccessDelayMinTime,
       "hwParsePriority": hwParsePriority,
       "hwRealmNameLocation": hwRealmNameLocation,
       "hwIPOXUsernameOption82": hwIPOXUsernameOption82,
       "hwIPOXUsernameIP": hwIPOXUsernameIP,
       "hwIPOXUsernameSysname": hwIPOXUsernameSysname,
       "hwIPOXUsernameMAC": hwIPOXUsernameMAC,
       "hwDefaultUserName": hwDefaultUserName,
       "hwNasSerial": hwNasSerial,
       "hwAAAPasswordRepeatNumber": hwAAAPasswordRepeatNumber,
       "hwAAAPasswordRemindDay": hwAAAPasswordRemindDay,
       "hwOnlineUserNumLowerLimitThreshold": hwOnlineUserNumLowerLimitThreshold,
       "hwOnlineUserNumUpperLimitThreshold": hwOnlineUserNumUpperLimitThreshold,
       "hwTriggerLoose": hwTriggerLoose,
       "hwOfflineSpeedNumber": hwOfflineSpeedNumber,
       "hwIPOXpasswordKeyType": hwIPOXpasswordKeyType,
       "hwReauthorizeEnable": hwReauthorizeEnable,
       "hwDomainNameDelimiter": hwDomainNameDelimiter,
       "hwDomainNameSecurityDelimiter": hwDomainNameSecurityDelimiter,
       "hwGlobalAuthEventAuthFailResponseFail": hwGlobalAuthEventAuthFailResponseFail,
       "hwGlobalAuthEventAuthFailVlan": hwGlobalAuthEventAuthFailVlan,
       "hwGlobalAuthEventAuthenServerDownResponseFail": hwGlobalAuthEventAuthenServerDownResponseFail,
       "hwGlobalAuthEventAuthenServerDownVlan": hwGlobalAuthEventAuthenServerDownVlan,
       "hwGlobalAuthEventClientNoResponseVlan": hwGlobalAuthEventClientNoResponseVlan,
       "hwGlobalAuthEventPreAuthVlan": hwGlobalAuthEventPreAuthVlan,
       "hwGlobalAuthEventAuthFailUserGroup": hwGlobalAuthEventAuthFailUserGroup,
       "hwGlobalAuthEventAuthenServerDownUserGroup": hwGlobalAuthEventAuthenServerDownUserGroup,
       "hwGlobalAuthEventClientNoResponseUserGroup": hwGlobalAuthEventClientNoResponseUserGroup,
       "hwGlobalAuthEventPreAuthUserGroup": hwGlobalAuthEventPreAuthUserGroup,
       "hwAuthorModifyMode": hwAuthorModifyMode,
       "hwLocalRetryInterval": hwLocalRetryInterval,
       "hwLocalRetryTime": hwLocalRetryTime,
       "hwLocalBlockTime": hwLocalBlockTime,
       "hwRemoteRetryInterval": hwRemoteRetryInterval,
       "hwRemoteRetryTime": hwRemoteRetryTime,
       "hwRemoteBlockTime": hwRemoteBlockTime,
       "hwBlockDisable": hwBlockDisable,
       "hwAAAStat": hwAAAStat,
       "hwAAAStatEntry": hwAAAStatEntry,
       "hwTotalOnlineNum": hwTotalOnlineNum,
       "hwTotalPPPoeOnlineNum": hwTotalPPPoeOnlineNum,
       "hwTotalPPPoAOnlineNum": hwTotalPPPoAOnlineNum,
       "hwTotalftpOnlineNum": hwTotalftpOnlineNum,
       "hwTotalsshOnlineNum": hwTotalsshOnlineNum,
       "hwTotaltelnetOnlineNum": hwTotaltelnetOnlineNum,
       "hwTotalVLANOnlineNum": hwTotalVLANOnlineNum,
       "hwHistoricMaxOnlineNum": hwHistoricMaxOnlineNum,
       "hwResetHistoricMaxOnlineNum": hwResetHistoricMaxOnlineNum,
       "hwResetOfflineReasonStatistic": hwResetOfflineReasonStatistic,
       "hwResetOnlineFailReasonStatistic": hwResetOnlineFailReasonStatistic,
       "hwMaxPPPoeOnlineNum": hwMaxPPPoeOnlineNum,
       "hwTotalPortalServerUserNum": hwTotalPortalServerUserNum,
       "hwMaxPortalServerUserNum": hwMaxPortalServerUserNum,
       "hwTotalIPv4OnlineNum": hwTotalIPv4OnlineNum,
       "hwTotalIPv6OnlineNum": hwTotalIPv6OnlineNum,
       "hwTotalDualStackOnlineNum": hwTotalDualStackOnlineNum,
       "hwTotalIPv4FlowDnByte": hwTotalIPv4FlowDnByte,
       "hwTotalIPv4FlowDnPkt": hwTotalIPv4FlowDnPkt,
       "hwTotalIPv4FlowUpByte": hwTotalIPv4FlowUpByte,
       "hwTotalIPv4FlowUpPkt": hwTotalIPv4FlowUpPkt,
       "hwTotalIPv6FlowDnByte": hwTotalIPv6FlowDnByte,
       "hwTotalIPv6FlowDnPkt": hwTotalIPv6FlowDnPkt,
       "hwTotalIPv6FlowUpByte": hwTotalIPv6FlowUpByte,
       "hwTotalIPv6FlowUpPkt": hwTotalIPv6FlowUpPkt,
       "hwHistoricMaxOnlineAcctReadyNum": hwHistoricMaxOnlineAcctReadyNum,
       "hwPubicLacUserNum": hwPubicLacUserNum,
       "hwHistoricMaxOnlineLocalNum": hwHistoricMaxOnlineLocalNum,
       "hwHistoricMaxOnlineRemoteNum": hwHistoricMaxOnlineRemoteNum,
       "hwTotalLacOnlineNum": hwTotalLacOnlineNum,
       "hwTotalLnsOnlineNum": hwTotalLnsOnlineNum,
       "hwTotalWlsOnlineNum": hwTotalWlsOnlineNum,
       "hwTotalWrdOnlineNum": hwTotalWrdOnlineNum,
       "hwDhcpUserOnlineFailCount": hwDhcpUserOnlineFailCount,
       "hwAccessTable": hwAccessTable,
       "hwAccessEntry": hwAccessEntry,
       "hwAccessIndex": hwAccessIndex,
       "hwAccessUserName": hwAccessUserName,
       "hwAccessPortType": hwAccessPortType,
       "hwAccessPriority": hwAccessPriority,
       "hwAccessSlotNo": hwAccessSlotNo,
       "hwAccessSubSlotNo": hwAccessSubSlotNo,
       "hwAccessPortNo": hwAccessPortNo,
       "hwAccessVLANID": hwAccessVLANID,
       "hwAccessPVC": hwAccessPVC,
       "hwAccessAuthenMethod": hwAccessAuthenMethod,
       "hwAccessAcctMethod": hwAccessAcctMethod,
       "hwAccessIPAddress": hwAccessIPAddress,
       "hwAccessVRF": hwAccessVRF,
       "hwAccessMACAddress": hwAccessMACAddress,
       "hwAccessIfIdleCut": hwAccessIfIdleCut,
       "hwAccessIdleCutTime": hwAccessIdleCutTime,
       "hwAccessIdleCutFlow": hwAccessIdleCutFlow,
       "hwAccessTimeLimit": hwAccessTimeLimit,
       "hwAccessTotalFlow64Limit": hwAccessTotalFlow64Limit,
       "hwAccessStartTime": hwAccessStartTime,
       "hwAccessCARIfUpActive": hwAccessCARIfUpActive,
       "hwAccessCARIfDnActive": hwAccessCARIfDnActive,
       "hwAccessUpFlow64": hwAccessUpFlow64,
       "hwAccessDnFlow64": hwAccessDnFlow64,
       "hwAccessUpPacket64": hwAccessUpPacket64,
       "hwAccessDnPacket64": hwAccessDnPacket64,
       "hwAccessCARUpCIR": hwAccessCARUpCIR,
       "hwAccessCARUpPIR": hwAccessCARUpPIR,
       "hwAccessCARUpCBS": hwAccessCARUpCBS,
       "hwAccessCARUpPBS": hwAccessCARUpPBS,
       "hwAccessCARDnCIR": hwAccessCARDnCIR,
       "hwAccessCARDnPIR": hwAccessCARDnPIR,
       "hwAccessCARDnCBS": hwAccessCARDnCBS,
       "hwAccessCARDnPBS": hwAccessCARDnPBS,
       "hwAccessDownPriority": hwAccessDownPriority,
       "hwAccessQosProfile": hwAccessQosProfile,
       "hwAccessInterface": hwAccessInterface,
       "hwAccessIPv6IFID": hwAccessIPv6IFID,
       "hwAccessIPv6WanAddress": hwAccessIPv6WanAddress,
       "hwAccessIPv6WanPrefix": hwAccessIPv6WanPrefix,
       "hwAccessIPv6LanPrefix": hwAccessIPv6LanPrefix,
       "hwAccessIPv6LanPrefixLen": hwAccessIPv6LanPrefixLen,
       "hwAccessBasicIPType": hwAccessBasicIPType,
       "hwAccessIPv6WaitDelay": hwAccessIPv6WaitDelay,
       "hwAccessIPv6ManagedAddressFlag": hwAccessIPv6ManagedAddressFlag,
       "hwAccessIPv6CPIFIDAvailable": hwAccessIPv6CPIFIDAvailable,
       "hwAccessIPv6OtherFlag": hwAccessIPv6OtherFlag,
       "hwAccessIPv6CPAssignIFID": hwAccessIPv6CPAssignIFID,
       "hwAccessLineID": hwAccessLineID,
       "hwAccessIPv6UpFlow64": hwAccessIPv6UpFlow64,
       "hwAccessIPv6DnFlow64": hwAccessIPv6DnFlow64,
       "hwAccessIPv6UpPacket64": hwAccessIPv6UpPacket64,
       "hwAccessIPv6DnPacket64": hwAccessIPv6DnPacket64,
       "hwAccessDeviceName": hwAccessDeviceName,
       "hwAccessDeviceMACAddress": hwAccessDeviceMACAddress,
       "hwAccessDevicePortName": hwAccessDevicePortName,
       "hwAccessAPID": hwAccessAPID,
       "hwAccessExtTable": hwAccessExtTable,
       "hwAccessExtEntry": hwAccessExtEntry,
       "hwAccessUCLGroup": hwAccessUCLGroup,
       "hwAuthenticationState": hwAuthenticationState,
       "hwAuthorizationState": hwAuthorizationState,
       "hwAccountingState": hwAccountingState,
       "hwAccessDomainName": hwAccessDomainName,
       "hwIdleTimeLength": hwIdleTimeLength,
       "hwAcctSessionID": hwAcctSessionID,
       "hwAccessStartAcctTime": hwAccessStartAcctTime,
       "hwAccessNormalServerGroup": hwAccessNormalServerGroup,
       "hwAccessDomainAcctCopySeverGroup": hwAccessDomainAcctCopySeverGroup,
       "hwAccessPVlanAcctCopyServerGroup": hwAccessPVlanAcctCopyServerGroup,
       "hwAccessCurAuthenPlace": hwAccessCurAuthenPlace,
       "hwAccessActionFlag": hwAccessActionFlag,
       "hwAccessAuthtype": hwAccessAuthtype,
       "hwAccessType": hwAccessType,
       "hwAccessOnlineTime": hwAccessOnlineTime,
       "hwAccessDomain": hwAccessDomain,
       "hwAccessGateway": hwAccessGateway,
       "hwAccessSSID": hwAccessSSID,
       "hwAccessAPMAC": hwAccessAPMAC,
       "hwAccessCurAccountingPlace": hwAccessCurAccountingPlace,
       "hwAccessCurAuthorPlace": hwAccessCurAuthorPlace,
       "hwAccessUserGroup": hwAccessUserGroup,
       "hwAccessResourceInsufficientInbound": hwAccessResourceInsufficientInbound,
       "hwAccessResourceInsufficientOutbound": hwAccessResourceInsufficientOutbound,
       "hwAcctSchemeExtTable": hwAcctSchemeExtTable,
       "hwAcctSchemeExtEntry": hwAcctSchemeExtEntry,
       "hwIfRealtimeAcct": hwIfRealtimeAcct,
       "hwRealtimeFailMaxnum": hwRealtimeFailMaxnum,
       "hwStartFailOnlineIfSendInterim": hwStartFailOnlineIfSendInterim,
       "hwBillPoolTable": hwBillPoolTable,
       "hwBillsPoolVolume": hwBillsPoolVolume,
       "hwBillsPoolNum": hwBillsPoolNum,
       "hwBillsPoolAlarmThreshold": hwBillsPoolAlarmThreshold,
       "hwBillsPoolBackupMode": hwBillsPoolBackupMode,
       "hwBillsPoolBackupInterval": hwBillsPoolBackupInterval,
       "hwBillsPoolBackupNow": hwBillsPoolBackupNow,
       "hwBillsPoolReset": hwBillsPoolReset,
       "hwBillTFTPTable": hwBillTFTPTable,
       "hwBillsTFTPSrvIP": hwBillsTFTPSrvIP,
       "hwBillsTFTPMainFileName": hwBillsTFTPMainFileName,
       "hwUclGrpTable": hwUclGrpTable,
       "hwUclGrpEntry": hwUclGrpEntry,
       "hwUclGrpName": hwUclGrpName,
       "hwUclGrpRowStatus": hwUclGrpRowStatus,
       "hwIPAccessTable": hwIPAccessTable,
       "hwIPAccessEntry": hwIPAccessEntry,
       "hwIPAccessIPaddress": hwIPAccessIPaddress,
       "hwIPAccessCID": hwIPAccessCID,
       "hwIPAccessVRF": hwIPAccessVRF,
       "hwCutAccessUserTable": hwCutAccessUserTable,
       "hwCutStartUserID": hwCutStartUserID,
       "hwCutEndUserID": hwCutEndUserID,
       "hwCutIPaddress": hwCutIPaddress,
       "hwCutMacAddres": hwCutMacAddres,
       "hwCutUserName": hwCutUserName,
       "hwCutUserAttri": hwCutUserAttri,
       "hwCutDomain": hwCutDomain,
       "hwCutIPPoolName": hwCutIPPoolName,
       "hwCutIfIndex": hwCutIfIndex,
       "hwCutVlanID": hwCutVlanID,
       "hwCutVPI": hwCutVPI,
       "hwCutVCI": hwCutVCI,
       "hwCutVRF": hwCutVRF,
       "hwCutAccessInterface": hwCutAccessInterface,
       "hwCutUserSSID": hwCutUserSSID,
       "hwCutAccessSlot": hwCutAccessSlot,
       "hwCutUserGroup": hwCutUserGroup,
       "hwAAACallRate": hwAAACallRate,
       "hwAAAUserPPP": hwAAAUserPPP,
       "hwTotalConnectNum": hwTotalConnectNum,
       "hwTotalSuccessNum": hwTotalSuccessNum,
       "hwTotalLCPFailNum": hwTotalLCPFailNum,
       "hwTotalAuthenFailNum": hwTotalAuthenFailNum,
       "hwTotalNCPFailNum": hwTotalNCPFailNum,
       "hwTotalIPAllocFailNum": hwTotalIPAllocFailNum,
       "hwTotalOtherPPPFailNum": hwTotalOtherPPPFailNum,
       "hwAAAUserWebandFast": hwAAAUserWebandFast,
       "hwTotalWebConnectNum": hwTotalWebConnectNum,
       "hwTotalSuccessWebConnectNum": hwTotalSuccessWebConnectNum,
       "hwAAAUserDot1X": hwAAAUserDot1X,
       "hwTotalDot1XConnectNum": hwTotalDot1XConnectNum,
       "hwTotalSuccessDot1XConnectNum": hwTotalSuccessDot1XConnectNum,
       "hwAAAUserBind": hwAAAUserBind,
       "hwTotalBindConnectNum": hwTotalBindConnectNum,
       "hwTotalSuccessBindConnectNum": hwTotalSuccessBindConnectNum,
       "hwRecordSchemeTable": hwRecordSchemeTable,
       "hwRecordSchemeEntry": hwRecordSchemeEntry,
       "hwRecordSchemeName": hwRecordSchemeName,
       "hwRecordTacGroupName": hwRecordTacGroupName,
       "hwRecordRowStatus": hwRecordRowStatus,
       "hwMACAccessTable": hwMACAccessTable,
       "hwMACAccessEntry": hwMACAccessEntry,
       "hwMACAccessMACAddress": hwMACAccessMACAddress,
       "hwMACAccessCID": hwMACAccessCID,
       "hwSlotConnectNumTable": hwSlotConnectNumTable,
       "hwSlotConnectNumEntry": hwSlotConnectNumEntry,
       "hwSlotConnectNumSlot": hwSlotConnectNumSlot,
       "hwSlotConnectNumOnlineNum": hwSlotConnectNumOnlineNum,
       "hwSlotConnectNumMaxOnlineNum": hwSlotConnectNumMaxOnlineNum,
       "hwSlotConnectNumMaxOnlineAcctReadyNum": hwSlotConnectNumMaxOnlineAcctReadyNum,
       "hwSlotCardConnectNumTable": hwSlotCardConnectNumTable,
       "hwSlotCardConnectNumEntry": hwSlotCardConnectNumEntry,
       "hwSlotCardConnectNumSlot": hwSlotCardConnectNumSlot,
       "hwSlotCardConnectNumCard": hwSlotCardConnectNumCard,
       "hwSlotCardConnectNumOnlineNum": hwSlotCardConnectNumOnlineNum,
       "hwSlotCardConnectNumIPv4OnlineNum": hwSlotCardConnectNumIPv4OnlineNum,
       "hwSlotCardConnectNumIPv6OnlineNum": hwSlotCardConnectNumIPv6OnlineNum,
       "hwSlotCardConnectNumDualOnlineNum": hwSlotCardConnectNumDualOnlineNum,
       "hwSlotCardConnectNumNoAuthNum": hwSlotCardConnectNumNoAuthNum,
       "hwSlotCardConnectNumPPPAuthNum": hwSlotCardConnectNumPPPAuthNum,
       "hwSlotCardConnectNum8021xAuthNum": hwSlotCardConnectNum8021xAuthNum,
       "hwSlotCardConnectNumWebAuthNum": hwSlotCardConnectNumWebAuthNum,
       "hwSlotCardConnectNumBindAuthNum": hwSlotCardConnectNumBindAuthNum,
       "hwSlotCardConnectNumFastAuthNum": hwSlotCardConnectNumFastAuthNum,
       "hwSlotCardConnectNumWlanAuthNum": hwSlotCardConnectNumWlanAuthNum,
       "hwSlotCardConnectNumAdminAuthNum": hwSlotCardConnectNumAdminAuthNum,
       "hwSlotCardConnectNumTunnelAuthNum": hwSlotCardConnectNumTunnelAuthNum,
       "hwSlotCardConnectNumMIPAuthNum": hwSlotCardConnectNumMIPAuthNum,
       "hwOfflineReasonStatTable": hwOfflineReasonStatTable,
       "hwOfflineReasonStatEntry": hwOfflineReasonStatEntry,
       "hwOfflineReason": hwOfflineReason,
       "hwOfflineReasonStatistic": hwOfflineReasonStatistic,
       "hwOnlineFailReasonStatistic": hwOnlineFailReasonStatistic,
       "hwMulticastListTable": hwMulticastListTable,
       "hwMulticastListEntry": hwMulticastListEntry,
       "hwMulticastListIndex": hwMulticastListIndex,
       "hwMulticastListName": hwMulticastListName,
       "hwMulticastListSourceIp": hwMulticastListSourceIp,
       "hwMulticastListSourceIpMask": hwMulticastListSourceIpMask,
       "hwMulticastListGroupIp": hwMulticastListGroupIp,
       "hwMulticastListGroupIpMask": hwMulticastListGroupIpMask,
       "hwMulticastListVpnInstance": hwMulticastListVpnInstance,
       "hwMulticastListRowStatus": hwMulticastListRowStatus,
       "hwMulticastProfileTable": hwMulticastProfileTable,
       "hwMulticastProfileEntry": hwMulticastProfileEntry,
       "hwMulticastProfileIndex": hwMulticastProfileIndex,
       "hwMulticastProfileName": hwMulticastProfileName,
       "hwMulticastProfileRowStatus": hwMulticastProfileRowStatus,
       "hwMulticastProfileExtTable": hwMulticastProfileExtTable,
       "hwMulticastProfileExtEntry": hwMulticastProfileExtEntry,
       "hwMulticastListBindName": hwMulticastListBindName,
       "hwMulticastProfileExtRowStatus": hwMulticastProfileExtRowStatus,
       "hwServiceSchemeTable": hwServiceSchemeTable,
       "hwServiceSchemeEntry": hwServiceSchemeEntry,
       "hwServiceSchemeName": hwServiceSchemeName,
       "hwServiceSchemeNextHopIp": hwServiceSchemeNextHopIp,
       "hwServiceSchemeUserPriority": hwServiceSchemeUserPriority,
       "hwServiceSchemeIdleCutTime": hwServiceSchemeIdleCutTime,
       "hwServiceSchemeIdleCutFlow": hwServiceSchemeIdleCutFlow,
       "hwServiceSchemeDnsFirst": hwServiceSchemeDnsFirst,
       "hwServiceSchemeDnsSecond": hwServiceSchemeDnsSecond,
       "hwSrvSchemeAdminUserPriority": hwSrvSchemeAdminUserPriority,
       "hwSrvSchemeIpPoolOneName": hwSrvSchemeIpPoolOneName,
       "hwSrvSchemeIpPoolTwoName": hwSrvSchemeIpPoolTwoName,
       "hwSrvSchemeIpPoolThreeName": hwSrvSchemeIpPoolThreeName,
       "hwServiceSchemeRowStatus": hwServiceSchemeRowStatus,
       "hwServiceSchemeIdleCutType": hwServiceSchemeIdleCutType,
       "hwServiceSchemeIdleCutFlowValue": hwServiceSchemeIdleCutFlowValue,
       "hwLocalAuthorize": hwLocalAuthorize,
       "hwRemoteAuthorize": hwRemoteAuthorize,
       "hwDhcpOpt121RouteTable": hwDhcpOpt121RouteTable,
       "hwDhcpOpt121RouteEntry": hwDhcpOpt121RouteEntry,
       "hwDhcpOpt121RouteDestIp": hwDhcpOpt121RouteDestIp,
       "hwDhcpOpt121RouteMask": hwDhcpOpt121RouteMask,
       "hwDhcpOpt121RouteNextHop": hwDhcpOpt121RouteNextHop,
       "hwDhcpOpt121RouteRowStatus": hwDhcpOpt121RouteRowStatus,
       "hwAccessDelayPerSlotTable": hwAccessDelayPerSlotTable,
       "hwAccessDelayPerSlotEntry": hwAccessDelayPerSlotEntry,
       "hwAccessDelayPerSlotSlot": hwAccessDelayPerSlotSlot,
       "hwAccessDelayPerSlotTransitionStep": hwAccessDelayPerSlotTransitionStep,
       "hwAccessDelayPerSlotMaxTime": hwAccessDelayPerSlotMaxTime,
       "hwAccessDelayPerSlotMinTime": hwAccessDelayPerSlotMinTime,
       "hwAccessDelayPerSlotRowStatus": hwAccessDelayPerSlotRowStatus,
       "hwVpnAccessUserStatTable": hwVpnAccessUserStatTable,
       "hwVpnAccessUserStatEntry": hwVpnAccessUserStatEntry,
       "hwUserType": hwUserType,
       "hwVpnAccessUserStatVpnName": hwVpnAccessUserStatVpnName,
       "hwVpnAccessUserStatUserStat": hwVpnAccessUserStatUserStat,
       "hwInterfaceAccessUserStatTable": hwInterfaceAccessUserStatTable,
       "hwInterfaceAccessUserStatEntry": hwInterfaceAccessUserStatEntry,
       "hwInterfaceAccessUserStatInterfaceIndex": hwInterfaceAccessUserStatInterfaceIndex,
       "hwInterfaceAccessUserStatUserStat": hwInterfaceAccessUserStatUserStat,
       "hwDomainAccessUserStatTable": hwDomainAccessUserStatTable,
       "hwDomainAccessUserStatEntry": hwDomainAccessUserStatEntry,
       "hwDomainAccessUserStatUserStat": hwDomainAccessUserStatUserStat,
       "hwSlotAccessUserStatTable": hwSlotAccessUserStatTable,
       "hwSlotAccessUserStatEntry": hwSlotAccessUserStatEntry,
       "hwSlotAccessUserStatSlot": hwSlotAccessUserStatSlot,
       "hwSlotAccessUserStatUserStat": hwSlotAccessUserStatUserStat,
       "hwDomainIncludePoolGroupTable": hwDomainIncludePoolGroupTable,
       "hwDomainIncludePoolGroupEntry": hwDomainIncludePoolGroupEntry,
       "hwDomainIncludeIPPoolGroupName": hwDomainIncludeIPPoolGroupName,
       "hwDomainIncludeIPPoolGroupRowStates": hwDomainIncludeIPPoolGroupRowStates,
       "hwDomainIPPoolMoveToTable": hwDomainIPPoolMoveToTable,
       "hwDomainIPPoolMoveToEntry": hwDomainIPPoolMoveToEntry,
       "hwDomainIncludeIPPoolName": hwDomainIncludeIPPoolName,
       "hwDomainIncludeIPPoolMoveto": hwDomainIncludeIPPoolMoveto,
       "hwDomainExt2Table": hwDomainExt2Table,
       "hwDomainExt2Entry": hwDomainExt2Entry,
       "hwRedKeyUserMac": hwRedKeyUserMac,
       "hwIfUserMacSimple": hwIfUserMacSimple,
       "hwPoolLowerLimitWarningThreshold": hwPoolLowerLimitWarningThreshold,
       "hwIPv6PoolLowerLimitWarningThreshold": hwIPv6PoolLowerLimitWarningThreshold,
       "hwAAADomainInboundQoSProfile": hwAAADomainInboundQoSProfile,
       "hwAAADomainOutboundQoSProfile": hwAAADomainOutboundQoSProfile,
       "hwAAADomainInboundVPNInstance": hwAAADomainInboundVPNInstance,
       "hwAAAOnlineFailRecordTable": hwAAAOnlineFailRecordTable,
       "hwAAAOnlineFailRecordEntry": hwAAAOnlineFailRecordEntry,
       "hwAAAOnlineFailIndex": hwAAAOnlineFailIndex,
       "hwUserName": hwUserName,
       "hwUserDomainName": hwUserDomainName,
       "hwUserMAC": hwUserMAC,
       "hwUserAccessType": hwUserAccessType,
       "hwUserInterface": hwUserInterface,
       "hwUserAccessPVC": hwUserAccessPVC,
       "hwUserAccessPeVlan": hwUserAccessPeVlan,
       "hwUserAccessCeVlan": hwUserAccessCeVlan,
       "hwUserIPAddress": hwUserIPAddress,
       "hwUserIPv6NDRAPrefix": hwUserIPv6NDRAPrefix,
       "hwUserIPv6Address": hwUserIPv6Address,
       "hwUserIPv6PDPrefix": hwUserIPv6PDPrefix,
       "hwUserIPv6PDPrefixLength": hwUserIPv6PDPrefixLength,
       "hwUserID": hwUserID,
       "hwUserAuthenState": hwUserAuthenState,
       "hwUserAcctState": hwUserAcctState,
       "hwUserAuthorState": hwUserAuthorState,
       "hwUserLoginTime": hwUserLoginTime,
       "hwOnlineFailReason": hwOnlineFailReason,
       "hwReplyMessage": hwReplyMessage,
       "hwUserLogTable": hwUserLogTable,
       "hwUserLogEntry": hwUserLogEntry,
       "hwUserLogAccess": hwUserLogAccess,
       "hwUserLogIPAddress": hwUserLogIPAddress,
       "hwUserLogPort": hwUserLogPort,
       "hwUserLogVersion": hwUserLogVersion,
       "hwShowUserLogStatistic": hwShowUserLogStatistic,
       "hwResetUserLogStatistic": hwResetUserLogStatistic,
       "hwReauthorizeTable": hwReauthorizeTable,
       "hwReauthorizeEntry": hwReauthorizeEntry,
       "hwReauthorizeUsername": hwReauthorizeUsername,
       "hwReauthorizeUsergroup": hwReauthorizeUsergroup,
       "hwUserGroupTable": hwUserGroupTable,
       "hwUserGroupEntry": hwUserGroupEntry,
       "hwUserGroupIndex": hwUserGroupIndex,
       "hwUserGroupName": hwUserGroupName,
       "hwAclId": hwAclId,
       "hwQoSProfileName": hwQoSProfileName,
       "hwInterIsolateFlag": hwInterIsolateFlag,
       "hwInnerIsolateFlag": hwInnerIsolateFlag,
       "hwUserGroupRowStatus": hwUserGroupRowStatus,
       "hwUserVlan": hwUserVlan,
       "hw8021pRemark": hw8021pRemark,
       "hwDscpRemark": hwDscpRemark,
       "hwExpRemark": hwExpRemark,
       "hwLpRemark": hwLpRemark,
       "hwUserGroupCarCir": hwUserGroupCarCir,
       "hwUserGroupCarPir": hwUserGroupCarPir,
       "hwUserGroupCarCbs": hwUserGroupCarCbs,
       "hwUserGroupCarPbs": hwUserGroupCarPbs,
       "hwUserGroupEnable": hwUserGroupEnable,
       "hwUserGroupCarInBoundCir": hwUserGroupCarInBoundCir,
       "hwUserGroupCarInBoundPir": hwUserGroupCarInBoundPir,
       "hwUserGroupCarInBoundCbs": hwUserGroupCarInBoundCbs,
       "hwUserGroupCarInBoundPbs": hwUserGroupCarInBoundPbs,
       "hwUserGroupUserVlanPool": hwUserGroupUserVlanPool,
       "hwAAAOfflineRecordTable": hwAAAOfflineRecordTable,
       "hwAAAOfflineRecordEntry": hwAAAOfflineRecordEntry,
       "hwAAAOfflineIndex": hwAAAOfflineIndex,
       "hwOfflineRecordUserName": hwOfflineRecordUserName,
       "hwOfflineRecordDomainName": hwOfflineRecordDomainName,
       "hwOfflineRecordUserMAC": hwOfflineRecordUserMAC,
       "hwOfflineRecordAccessType": hwOfflineRecordAccessType,
       "hwOfflineRecordInterface": hwOfflineRecordInterface,
       "hwOfflineRecordAccessPeVlan": hwOfflineRecordAccessPeVlan,
       "hwOfflineRecordAccessCeVlan": hwOfflineRecordAccessCeVlan,
       "hwOfflineRecordIPAddress": hwOfflineRecordIPAddress,
       "hwOfflineRecordUserID": hwOfflineRecordUserID,
       "hwOfflineRecordUserLoginTime": hwOfflineRecordUserLoginTime,
       "hwOfflineRecordUserLogoutTime": hwOfflineRecordUserLogoutTime,
       "hwOfflineRecordOfflineReason": hwOfflineRecordOfflineReason,
       "hwGlobalDhcpOpt64SepAndSeg": hwGlobalDhcpOpt64SepAndSeg,
       "hwGlobalDhcpServerAck": hwGlobalDhcpServerAck,
       "hwAuthEventCfgTable": hwAuthEventCfgTable,
       "hwAuthEventCfgEntry": hwAuthEventCfgEntry,
       "hwAuthEventPortIndex": hwAuthEventPortIndex,
       "hwAuthEventAuthFailResponseFail": hwAuthEventAuthFailResponseFail,
       "hwAuthEventAuthFailVlan": hwAuthEventAuthFailVlan,
       "hwAuthEventAuthenServerDownResponseFail": hwAuthEventAuthenServerDownResponseFail,
       "hwAuthEventAuthenServerDownVlan": hwAuthEventAuthenServerDownVlan,
       "hwAuthEventClientNoResponseVlan": hwAuthEventClientNoResponseVlan,
       "hwAuthEventPreAuthVlan": hwAuthEventPreAuthVlan,
       "hwAuthEventAuthFailUserGroup": hwAuthEventAuthFailUserGroup,
       "hwAuthEventAuthenServerDownUserGroup": hwAuthEventAuthenServerDownUserGroup,
       "hwAuthEventClientNoResponseUserGroup": hwAuthEventClientNoResponseUserGroup,
       "hwAuthEventPreAuthUserGroup": hwAuthEventPreAuthUserGroup,
       "hwWlanInterfaceTable": hwWlanInterfaceTable,
       "hwWlanInterfaceEntry": hwWlanInterfaceEntry,
       "hwWlanInterfaceIndex": hwWlanInterfaceIndex,
       "hwWlanInterfaceName": hwWlanInterfaceName,
       "hwWlanInterfaceDomainNameDelimiter": hwWlanInterfaceDomainNameDelimiter,
       "hwWlanInterfaceDomainNameSecurityDelimiter": hwWlanInterfaceDomainNameSecurityDelimiter,
       "hwWlanInterfaceDomainNameParseDirection": hwWlanInterfaceDomainNameParseDirection,
       "hwWlanInterfaceDomainNameLocation": hwWlanInterfaceDomainNameLocation,
       "hwAuthorCmdTable": hwAuthorCmdTable,
       "hwAuthorCmdEntry": hwAuthorCmdEntry,
       "hwAuthorCmdLevel": hwAuthorCmdLevel,
       "hwAuthorCmdMode": hwAuthorCmdMode,
       "hwAuthorCmdRowStatus": hwAuthorCmdRowStatus,
       "hwAAARateTable": hwAAARateTable,
       "hwAAARateEntry": hwAAARateEntry,
       "hwAAARateDirection": hwAAARateDirection,
       "hwAAARateType": hwAAARateType,
       "hwAAARateRealPeak": hwAAARateRealPeak,
       "hwAAARateRealAverage": hwAAARateRealAverage,
       "hwAAARateRealUsedCount": hwAAARateRealUsedCount,
       "hwAAARateRealPercent": hwAAARateRealPercent,
       "hwLocalUserPwPolicyAdmin": hwLocalUserPwPolicyAdmin,
       "hwLocalUserPwPolicyAdminEntry": hwLocalUserPwPolicyAdminEntry,
       "hwAdminEnable": hwAdminEnable,
       "hwAdminExpire": hwAdminExpire,
       "hwAdminPwHistroyRecordNum": hwAdminPwHistroyRecordNum,
       "hwAdminAlertBefore": hwAdminAlertBefore,
       "hwAdminAlertOrginal": hwAdminAlertOrginal,
       "hwLocalUserPwPolicyAcc": hwLocalUserPwPolicyAcc,
       "hwLocalUserPwPolicyAccEntry": hwLocalUserPwPolicyAccEntry,
       "hwAccEnable": hwAccEnable,
       "hwAccPwHistroyRecordNum": hwAccPwHistroyRecordNum,
       "hwAAADomainIPPoolTable": hwAAADomainIPPoolTable,
       "hwAAADomainIPPoolEntry": hwAAADomainIPPoolEntry,
       "hwAAADomainIPPoolName": hwAAADomainIPPoolName,
       "hwAAADomainIPPoolIndex": hwAAADomainIPPoolIndex,
       "hwAAADomainIPPoolConstantIndex": hwAAADomainIPPoolConstantIndex,
       "hwAAADomainIPPoolPosition": hwAAADomainIPPoolPosition,
       "hwAAADomainIPPoolRowStatus": hwAAADomainIPPoolRowStatus,
       "userAuthenProfileTable": userAuthenProfileTable,
       "userAuthenProfileEntry": userAuthenProfileEntry,
       "userAuthenProfileName": userAuthenProfileName,
       "userAuthenProfileDot1xAccessProfileName": userAuthenProfileDot1xAccessProfileName,
       "userAuthenProfileMacAuthenAccessProfileName": userAuthenProfileMacAuthenAccessProfileName,
       "userAuthenProfilePortalAccessProfileName": userAuthenProfilePortalAccessProfileName,
       "userAuthenProfileSingleAccess": userAuthenProfileSingleAccess,
       "userAuthenProfilePreAuthenServiceSchemeName": userAuthenProfilePreAuthenServiceSchemeName,
       "userAuthenProfilePreAuthenUserGroupName": userAuthenProfilePreAuthenUserGroupName,
       "userAuthenProfilePreAuthenVLAN": userAuthenProfilePreAuthenVLAN,
       "userAuthenProfileAuthenFailAuthorServiceSchemeName": userAuthenProfileAuthenFailAuthorServiceSchemeName,
       "userAuthenProfileAuthenFailAuthorUserGroupName": userAuthenProfileAuthenFailAuthorUserGroupName,
       "userAuthenProfileAuthenFailAuthorVLAN": userAuthenProfileAuthenFailAuthorVLAN,
       "userAuthenProfileAuthenServerDownServiceSchemeName": userAuthenProfileAuthenServerDownServiceSchemeName,
       "userAuthenProfileAuthenServerDownUserGroupName": userAuthenProfileAuthenServerDownUserGroupName,
       "userAuthenProfileAuthenServerDownVLAN": userAuthenProfileAuthenServerDownVLAN,
       "userAuthenProfileAuthenServerDownResponseSuccess": userAuthenProfileAuthenServerDownResponseSuccess,
       "userAuthenProfileAuthenServerUpReauthen": userAuthenProfileAuthenServerUpReauthen,
       "userAuthenProfileMacAuthenFirst": userAuthenProfileMacAuthenFirst,
       "userAuthenProfileMACBypass": userAuthenProfileMACBypass,
       "userAuthenProfileDot1xForceDomain": userAuthenProfileDot1xForceDomain,
       "userAuthenProfileMACAuthenForceDomain": userAuthenProfileMACAuthenForceDomain,
       "userAuthenProfilePortalForceDomain": userAuthenProfilePortalForceDomain,
       "userAuthenProfileDot1xDefaultDomain": userAuthenProfileDot1xDefaultDomain,
       "userAuthenProfileMACAuthenDefaultDomain": userAuthenProfileMACAuthenDefaultDomain,
       "userAuthenProfilePortalDefaultDomain": userAuthenProfilePortalDefaultDomain,
       "userAuthenProfileDefaultDomain": userAuthenProfileDefaultDomain,
       "userAuthenProfileForceDomain": userAuthenProfileForceDomain,
       "userAuthenProfileDomainNameDelimiter": userAuthenProfileDomainNameDelimiter,
       "userAuthenProfileDomainNameLocation": userAuthenProfileDomainNameLocation,
       "userAuthenProfileDomainNameParseDirection": userAuthenProfileDomainNameParseDirection,
       "userAuthenProfileSecurityNameDelimiter": userAuthenProfileSecurityNameDelimiter,
       "userAuthenProfilePreAuthenReAuthenTimer": userAuthenProfilePreAuthenReAuthenTimer,
       "userAuthenProfileAuthenFailReAuthenTimer": userAuthenProfileAuthenFailReAuthenTimer,
       "userAuthenProfilePreAuthenAgingTime": userAuthenProfilePreAuthenAgingTime,
       "userAuthenProfileAuthenFailAgingTime": userAuthenProfileAuthenFailAgingTime,
       "userAuthenProfileFreeRuleName": userAuthenProfileFreeRuleName,
       "userAuthenProfileAuthenSchemeName": userAuthenProfileAuthenSchemeName,
       "userAuthenProfileAuthorSchemeName": userAuthenProfileAuthorSchemeName,
       "userAuthenProfileAcctSchemeName": userAuthenProfileAcctSchemeName,
       "userAuthenProfileServiceSchemeName": userAuthenProfileServiceSchemeName,
       "userAuthenProfileUserGroupName": userAuthenProfileUserGroupName,
       "userAuthenProfileRadiusServerName": userAuthenProfileRadiusServerName,
       "userAuthenProfileHwtacacsServerName": userAuthenProfileHwtacacsServerName,
       "userAuthenProfileAuthenticationMode": userAuthenProfileAuthenticationMode,
       "userAuthenProfileMaxUser": userAuthenProfileMaxUser,
       "userAuthenProfileArpDetect": userAuthenProfileArpDetect,
       "userAuthenProfileArpDetectTimer": userAuthenProfileArpDetectTimer,
       "userAuthenProfileRowStatus": userAuthenProfileRowStatus,
       "userAuthenProfilePermitDomain": userAuthenProfilePermitDomain,
       "userAuthenProfileAuthenticationMaxUser": userAuthenProfileAuthenticationMaxUser,
       "userAuthenProfileAuthenFailAuthorResponseSuccess": userAuthenProfileAuthenFailAuthorResponseSuccess,
       "userAuthenticationFreeRuleTable": userAuthenticationFreeRuleTable,
       "userAuthenticationFreeRuleEntry": userAuthenticationFreeRuleEntry,
       "userAuthenticationFreeRuleName": userAuthenticationFreeRuleName,
       "userAuthenticationFreeRuleACLNumber": userAuthenticationFreeRuleACLNumber,
       "userAuthenticationFreeRuleIPv6ACLNumber": userAuthenticationFreeRuleIPv6ACLNumber,
       "userAuthenticationFreeRuleRowStatus": userAuthenticationFreeRuleRowStatus,
       "hwDot1xAccessProfileTable": hwDot1xAccessProfileTable,
       "hwDot1xAccessProfileEntry": hwDot1xAccessProfileEntry,
       "hwDot1xAccessProfileName": hwDot1xAccessProfileName,
       "hwDot1xAccessProfileGuestAuthorServiceSchemeName": hwDot1xAccessProfileGuestAuthorServiceSchemeName,
       "hwDot1xAccessProfileGuestAuthorUserGroupName": hwDot1xAccessProfileGuestAuthorUserGroupName,
       "hwDot1xAccessProfileGuestAuthorVLAN": hwDot1xAccessProfileGuestAuthorVLAN,
       "hwDot1xAccessProfileHandshakeSwitch": hwDot1xAccessProfileHandshakeSwitch,
       "hwDot1xAccessProfileHandShakePktType": hwDot1xAccessProfileHandShakePktType,
       "hwDot1xAccessProfileHandshakeInterval": hwDot1xAccessProfileHandshakeInterval,
       "hwDot1xAccessProfileIfEAPEnd": hwDot1xAccessProfileIfEAPEnd,
       "hwDot1xAccessProfileEAPEndMethod": hwDot1xAccessProfileEAPEndMethod,
       "hwDot1xAccessProfileEAPNotifyPktEAPCode": hwDot1xAccessProfileEAPNotifyPktEAPCode,
       "hwDot1xAccessProfileEAPNotifyPktEAPType": hwDot1xAccessProfileEAPNotifyPktEAPType,
       "hwDot1xAccessProfileReAuthenEnable": hwDot1xAccessProfileReAuthenEnable,
       "hwDot1xAccessProfileReauthenticationTimeout": hwDot1xAccessProfileReauthenticationTimeout,
       "hwDot1xAccessProfileClientTimeout": hwDot1xAccessProfileClientTimeout,
       "hwDot1xAccessProfileServerTimeout": hwDot1xAccessProfileServerTimeout,
       "hwDot1xAccessProfileTxPeriod": hwDot1xAccessProfileTxPeriod,
       "hwDot1xAccessProfileMaxRetryValue": hwDot1xAccessProfileMaxRetryValue,
       "hwDot1xAccessProfileSpeedLimitAuto": hwDot1xAccessProfileSpeedLimitAuto,
       "hwDot1xAccessProfileTriggerPktType": hwDot1xAccessProfileTriggerPktType,
       "hwDot1xAccessProfileUnicastTrigger": hwDot1xAccessProfileUnicastTrigger,
       "hwDot1xAccessProfileURL": hwDot1xAccessProfileURL,
       "hwDot1xAccessProfileEthTrunkHandShakePeriod": hwDot1xAccessProfileEthTrunkHandShakePeriod,
       "hwDot1xAccessProfileRowStatus": hwDot1xAccessProfileRowStatus,
       "hwMACAuthenAccessProfileTable": hwMACAuthenAccessProfileTable,
       "hwMACAuthenAccessProfileEntry": hwMACAuthenAccessProfileEntry,
       "hwMACAuthenAccessProfileName": hwMACAuthenAccessProfileName,
       "hwMACAuthenAccessProfileReAuthenEnable": hwMACAuthenAccessProfileReAuthenEnable,
       "hwMACAuthenAccessProfileReauthenticationTimeout": hwMACAuthenAccessProfileReauthenticationTimeout,
       "hwMACAuthenAccessProfileServerTimeout": hwMACAuthenAccessProfileServerTimeout,
       "hwMACAuthenAccessProfileUserNameFixedUserName": hwMACAuthenAccessProfileUserNameFixedUserName,
       "hwMACAuthenAccessProfileFixedPassword": hwMACAuthenAccessProfileFixedPassword,
       "hwMACAuthenAccessProfileMACAddressFormat": hwMACAuthenAccessProfileMACAddressFormat,
       "hwMACAuthenAccessProfileMACAddressPassword": hwMACAuthenAccessProfileMACAddressPassword,
       "hwMACAuthenAccessProfileUserNameDHCPOption": hwMACAuthenAccessProfileUserNameDHCPOption,
       "hwMACAuthenAccessProfileUserNameDHCPOSubOption": hwMACAuthenAccessProfileUserNameDHCPOSubOption,
       "hwMACAuthenAccessProfileTriggerPktType": hwMACAuthenAccessProfileTriggerPktType,
       "hwMACAuthenAccessProfileTriggerDHCPOptionType": hwMACAuthenAccessProfileTriggerDHCPOptionType,
       "hwMACAuthenAccessProfileDHCPRelaseOffline": hwMACAuthenAccessProfileDHCPRelaseOffline,
       "hwMACAuthenAccessProfileDHCPRenewReAuthen": hwMACAuthenAccessProfileDHCPRenewReAuthen,
       "hwMACAuthenAccessProfilePermitAuthenMAC": hwMACAuthenAccessProfilePermitAuthenMAC,
       "hwMACAuthenAccessProfilePermitAuthenMACMask": hwMACAuthenAccessProfilePermitAuthenMACMask,
       "hwMACAuthenAccessProfileRowStatus": hwMACAuthenAccessProfileRowStatus,
       "hwPortalAccessProfileTable": hwPortalAccessProfileTable,
       "hwPortalAccessProfileEntry": hwPortalAccessProfileEntry,
       "hwPortalAccessProfileName": hwPortalAccessProfileName,
       "hwPortalAccessProfileDetectPeriod": hwPortalAccessProfileDetectPeriod,
       "hwPortalAccessProfilePortalServerDownServiceSchemeName": hwPortalAccessProfilePortalServerDownServiceSchemeName,
       "hwPortalAccessProfilePortalServerDownUserGroupName": hwPortalAccessProfilePortalServerDownUserGroupName,
       "hwPortalAccessProfilePortalServerUpReAuthen": hwPortalAccessProfilePortalServerUpReAuthen,
       "hwPortalAccessProfileAlarmUserLowNum": hwPortalAccessProfileAlarmUserLowNum,
       "hwPortalAccessProfileAlarmUserHighNum": hwPortalAccessProfileAlarmUserHighNum,
       "hwPortalAccessProfileAuthenNetWork": hwPortalAccessProfileAuthenNetWork,
       "hwPortalAccessProfileAuthenNetWorkMask": hwPortalAccessProfileAuthenNetWorkMask,
       "hwPortalAccessProfilePortalServerName": hwPortalAccessProfilePortalServerName,
       "hwPortalAccessProfilePortalAccessDirect": hwPortalAccessProfilePortalAccessDirect,
       "hwPortalAccessProfileLocalServerEnable": hwPortalAccessProfileLocalServerEnable,
       "hwPortalAccessProfileLocalServerAnonymous": hwPortalAccessProfileLocalServerAnonymous,
       "hwPortalAccessProfileRowStatus": hwPortalAccessProfileRowStatus,
       "hwPortalAccessProfilePortalBackupServerName": hwPortalAccessProfilePortalBackupServerName,
       "hwAAAInboundVPNAccessUserStatTable": hwAAAInboundVPNAccessUserStatTable,
       "hwAAAInboundVPNAccessUserStatEntry": hwAAAInboundVPNAccessUserStatEntry,
       "hwAAAInboundVPNUserType": hwAAAInboundVPNUserType,
       "hwAAAInboundVPNName": hwAAAInboundVPNName,
       "hwAAAInboundVPNAccessUserStat": hwAAAInboundVPNAccessUserStat,
       "userAuthenticationFreeRuleExtTable": userAuthenticationFreeRuleExtTable,
       "userAuthenticationFreeRuleExtEntry": userAuthenticationFreeRuleExtEntry,
       "userAuthenticationFreeRuleNumber": userAuthenticationFreeRuleNumber,
       "userAuthenticationFreeRuleSourceMode": userAuthenticationFreeRuleSourceMode,
       "userAuthenticationFreeRuleSourceVlan": userAuthenticationFreeRuleSourceVlan,
       "userAuthenticationFreeRuleSourceInterface": userAuthenticationFreeRuleSourceInterface,
       "userAuthenticationFreeRuleSourceIP": userAuthenticationFreeRuleSourceIP,
       "userAuthenticationFreeRuleSourceIPMask": userAuthenticationFreeRuleSourceIPMask,
       "userAuthenticationFreeRuleSourceMac": userAuthenticationFreeRuleSourceMac,
       "userAuthenticationFreeRuleDestinationMode": userAuthenticationFreeRuleDestinationMode,
       "userAuthenticationFreeRuleDestinationIP": userAuthenticationFreeRuleDestinationIP,
       "userAuthenticationFreeRuleDestinationIPMask": userAuthenticationFreeRuleDestinationIPMask,
       "userAuthenticationFreeRuleDestinationProtocol": userAuthenticationFreeRuleDestinationProtocol,
       "userAuthenticationFreeRuleDestinationPort": userAuthenticationFreeRuleDestinationPort,
       "userAuthenticationFreeRuleDestinationUserGroup": userAuthenticationFreeRuleDestinationUserGroup,
       "userAuthenticationFreeRuleExtRowStatus": userAuthenticationFreeRuleExtRowStatus,
       "hwAAAMibTrap": hwAAAMibTrap,
       "hwAAATrapOid": hwAAATrapOid,
       "hwDomainIndex": hwDomainIndex,
       "hwHdFreeamount": hwHdFreeamount,
       "hwHdWarningThreshold": hwHdWarningThreshold,
       "hwUserSlot": hwUserSlot,
       "hwUserSlotMaxNumThreshold": hwUserSlotMaxNumThreshold,
       "hwOnlineUserNumThreshold": hwOnlineUserNumThreshold,
       "hwMaxUserThresholdType": hwMaxUserThresholdType,
       "hwRbpChangeName": hwRbpChangeName,
       "hwRbpOldState": hwRbpOldState,
       "hwRbpNewState": hwRbpNewState,
       "hwRbpChangeReason": hwRbpChangeReason,
       "hwRbsName": hwRbsName,
       "hwRbsDownReason": hwRbsDownReason,
       "hwPolicyRouteThreshold": hwPolicyRouteThreshold,
       "hwPolicyRoute": hwPolicyRoute,
       "hwRemoteDownloadAclUsedValue": hwRemoteDownloadAclUsedValue,
       "hwRemoteDownloadAclThresholdValue": hwRemoteDownloadAclThresholdValue,
       "hwLoginFailedTimes": hwLoginFailedTimes,
       "hwStatisticPeriod": hwStatisticPeriod,
       "hwUserGroupNumThreshold": hwUserGroupNumThreshold,
       "hwUserGroupUsedNum": hwUserGroupUsedNum,
       "hwAAACpuUsage": hwAAACpuUsage,
       "hwAAAUserResourceUsage": hwAAAUserResourceUsage,
       "hwAAASessionGroupUpperLimitThreshold": hwAAASessionGroupUpperLimitThreshold,
       "hwAAASessionGroupLowerLimitThreshold": hwAAASessionGroupLowerLimitThreshold,
       "hwAAASessionUpperLimitThreshold": hwAAASessionUpperLimitThreshold,
       "hwAAASessionLowerLimitThreshold": hwAAASessionLowerLimitThreshold,
       "hwAAATimerExpireMajorLevelThreshold": hwAAATimerExpireMajorLevelThreshold,
       "hwAAATimerExpireMajorLevelResumeThreshold": hwAAATimerExpireMajorLevelResumeThreshold,
       "hwAAATimerExpireCriticalLevelThreshold": hwAAATimerExpireCriticalLevelThreshold,
       "hwAAATimerExpireCriticalLevelResumeThreshold": hwAAATimerExpireCriticalLevelResumeThreshold,
       "hwMacMovedQuietUserSpec": hwMacMovedQuietUserSpec,
       "hwMacMovedUserPercentage": hwMacMovedUserPercentage,
       "hwLowerMacMovedUserPercentage": hwLowerMacMovedUserPercentage,
       "hwUpperMacMovedUserPercentage": hwUpperMacMovedUserPercentage,
       "hwAAAChasisIPv6AddressThreshold": hwAAAChasisIPv6AddressThreshold,
       "hwAAASlotIPv6AddressThreshold": hwAAASlotIPv6AddressThreshold,
       "hwAAATrapsDefine": hwAAATrapsDefine,
       "hwAAATraps": hwAAATraps,
       "hwUserIPAllocAlarm": hwUserIPAllocAlarm,
       "hwUserSlotMaxNum": hwUserSlotMaxNum,
       "hwOnlineUserNumAlarm": hwOnlineUserNumAlarm,
       "hwSetUserQosProfileFail": hwSetUserQosProfileFail,
       "hwUserMaxNum": hwUserMaxNum,
       "hwRbpStateChange": hwRbpStateChange,
       "hwRbsDown": hwRbsDown,
       "hwRbsUp": hwRbsUp,
       "hwUserIPv6AddressAllocAlarm": hwUserIPv6AddressAllocAlarm,
       "hwUserNDRAPrefixAllocAlarm": hwUserNDRAPrefixAllocAlarm,
       "hwUserDelegationPrefixAllocAlarm": hwUserDelegationPrefixAllocAlarm,
       "hwUserIPAllocAlarmResume": hwUserIPAllocAlarmResume,
       "hwUserIPv6AddressAllocAlarmResume": hwUserIPv6AddressAllocAlarmResume,
       "hwUserNDRAPrefixAllocAlarmResume": hwUserNDRAPrefixAllocAlarmResume,
       "hwUserDelegationPrefixAllocAlarmResume": hwUserDelegationPrefixAllocAlarmResume,
       "hwOnlineUserNumUpperLimitAlarm": hwOnlineUserNumUpperLimitAlarm,
       "hwOnlineUserNumUpperLimitResume": hwOnlineUserNumUpperLimitResume,
       "hwOnlineUserNumLowerLimitAlarm": hwOnlineUserNumLowerLimitAlarm,
       "hwOnlineUserNumLowerLimitResume": hwOnlineUserNumLowerLimitResume,
       "hwIPLowerlimitWarningAlarm": hwIPLowerlimitWarningAlarm,
       "hwIPLowerlimitWarningResume": hwIPLowerlimitWarningResume,
       "hwIPv6AddressLowerlimitWarningAlarm": hwIPv6AddressLowerlimitWarningAlarm,
       "hwIPv6AddressLowerlimitWarningResume": hwIPv6AddressLowerlimitWarningResume,
       "hwIPv6NDRAPrefixLowerlimitWarningAlarm": hwIPv6NDRAPrefixLowerlimitWarningAlarm,
       "hwIPv6NDRAPrefixLowerlimitWarningResume": hwIPv6NDRAPrefixLowerlimitWarningResume,
       "hwIPv6PDPrefixLowerlimitWarningAlarm": hwIPv6PDPrefixLowerlimitWarningAlarm,
       "hwIPv6PDPrefixLowerlimitWarningResume": hwIPv6PDPrefixLowerlimitWarningResume,
       "hwPolicyRouteSlotMaxNum": hwPolicyRouteSlotMaxNum,
       "hwRemoteDownloadAclThresholdAlarm": hwRemoteDownloadAclThresholdAlarm,
       "hwRemoteDownloadAclThresholdResume": hwRemoteDownloadAclThresholdResume,
       "hwAdminLoginFailed": hwAdminLoginFailed,
       "hwAdminLoginFailedClear": hwAdminLoginFailedClear,
       "hwUserGroupThresholdAlarm": hwUserGroupThresholdAlarm,
       "hwUserGroupThresholdResume": hwUserGroupThresholdResume,
       "hwEDSGLicenseExpireAlarm": hwEDSGLicenseExpireAlarm,
       "hwEDSGLicenseExpireResume": hwEDSGLicenseExpireResume,
       "hwAAAAccessUserResourceOrCpuAlarm": hwAAAAccessUserResourceOrCpuAlarm,
       "hwAAAAccessUserResourceOrCpuResume": hwAAAAccessUserResourceOrCpuResume,
       "hwAAASessionGroupUpperLimitAlarm": hwAAASessionGroupUpperLimitAlarm,
       "hwAAASessionGroupUpperLimitResume": hwAAASessionGroupUpperLimitResume,
       "hwAAASessionGroupLowerLimitAlarm": hwAAASessionGroupLowerLimitAlarm,
       "hwAAASessionGroupLowerLimitResume": hwAAASessionGroupLowerLimitResume,
       "hwAAAOnlineSessoinUpperLimitAlarm": hwAAAOnlineSessoinUpperLimitAlarm,
       "hwAAAOnlineSessoinUpperLimitResume": hwAAAOnlineSessoinUpperLimitResume,
       "hwAAAOnlineSessoinLowerLimitAlarm": hwAAAOnlineSessoinLowerLimitAlarm,
       "hwAAAOnlineSessoinLowerLimitResume": hwAAAOnlineSessoinLowerLimitResume,
       "hwAAASlotOnlineUserNumAlarm": hwAAASlotOnlineUserNumAlarm,
       "hwAAASlotOnlineUserNumResume": hwAAASlotOnlineUserNumResume,
       "hwAAATimerExpireMajorLevelAlarm": hwAAATimerExpireMajorLevelAlarm,
       "hwAAATimerExpireMajorLevelResume": hwAAATimerExpireMajorLevelResume,
       "hwAAATimerExpireCriticalLevelAlarm": hwAAATimerExpireCriticalLevelAlarm,
       "hwAAATimerExpireCriticalLevelResume": hwAAATimerExpireCriticalLevelResume,
       "hwMacMovedQuietMaxUserAlarm": hwMacMovedQuietMaxUserAlarm,
       "hwMacMovedQuietUserClearAlarm": hwMacMovedQuietUserClearAlarm,
       "hwAAAChasisIPv6AddressThresholdAlarm": hwAAAChasisIPv6AddressThresholdAlarm,
       "hwAAAChasisIPv6AddressThresholdResume": hwAAAChasisIPv6AddressThresholdResume,
       "hwAAASlotIPv6AddressThresholdAlarm": hwAAASlotIPv6AddressThresholdAlarm,
       "hwAAASlotIPv6AddressThresholdResume": hwAAASlotIPv6AddressThresholdResume,
       "hwLAMTrapsDefine": hwLAMTrapsDefine,
       "hwLAMTraps": hwLAMTraps,
       "hwHarddiskoverflow": hwHarddiskoverflow,
       "hwHarddiskReachThreshold": hwHarddiskReachThreshold,
       "hwHarddiskOK": hwHarddiskOK,
       "hwCachetoFTPFail": hwCachetoFTPFail,
       "hwHDtoFTPFail": hwHDtoFTPFail,
       "hwAaaConformance": hwAaaConformance,
       "hwAaaCompliances": hwAaaCompliances,
       "hwAaaCompliance": hwAaaCompliance,
       "hwAaaObjectGroups": hwAaaObjectGroups,
       "hwAuthenSchemeGroup": hwAuthenSchemeGroup,
       "hwAcctSchemeGroup": hwAcctSchemeGroup,
       "hwDomainGroup": hwDomainGroup,
       "hwDomainExtGroup": hwDomainExtGroup,
       "hwDomainStatGroup": hwDomainStatGroup,
       "hwAuthorSchemeGroup": hwAuthorSchemeGroup,
       "hwLocalUserGroup": hwLocalUserGroup,
       "hwLocalUserExtGroup": hwLocalUserExtGroup,
       "hwAaaSettingGroup": hwAaaSettingGroup,
       "hwAaaStatGroup": hwAaaStatGroup,
       "hwAccessGroup": hwAccessGroup,
       "hwAccessExtGroup": hwAccessExtGroup,
       "hwAcctSchemeExtGroup": hwAcctSchemeExtGroup,
       "hwBillPoolGroup": hwBillPoolGroup,
       "hwBillTFTPGroup": hwBillTFTPGroup,
       "hwUclGrpGroup": hwUclGrpGroup,
       "hwIpAccessGroup": hwIpAccessGroup,
       "hwCutAccessUserGroup": hwCutAccessUserGroup,
       "hwAaaUserPppGroup": hwAaaUserPppGroup,
       "hwAaaUserWebandFastGroup": hwAaaUserWebandFastGroup,
       "hwAaaUserDot1XGroup": hwAaaUserDot1XGroup,
       "hwAaaUserBindGroup": hwAaaUserBindGroup,
       "hwRecordSchemeGroup": hwRecordSchemeGroup,
       "hwMACAccessGroup": hwMACAccessGroup,
       "hwSlotConnectNumGroup": hwSlotConnectNumGroup,
       "hwOfflineReasonStatGroup": hwOfflineReasonStatGroup,
       "hwMulticastListGroup": hwMulticastListGroup,
       "hwMulticastProfileGroup": hwMulticastProfileGroup,
       "hwMulticastProfileExtGroup": hwMulticastProfileExtGroup,
       "hwAaaTrapOidGroup": hwAaaTrapOidGroup,
       "hwAaaTrapsNotificationsGroup": hwAaaTrapsNotificationsGroup,
       "hwLamTrapsNotificationsGroup": hwLamTrapsNotificationsGroup,
       "hwObsoleteGroup": hwObsoleteGroup,
       "hwServiceSchemeGroup": hwServiceSchemeGroup,
       "hwDhcpOpt121RouteGroup": hwDhcpOpt121RouteGroup,
       "hwAccessDelayPerSlotGroup": hwAccessDelayPerSlotGroup,
       "hwVpnAccessUserStatGroup": hwVpnAccessUserStatGroup,
       "hwInterfaceAccessUserStatGroup": hwInterfaceAccessUserStatGroup,
       "hwDomainAccessUserStatGroup": hwDomainAccessUserStatGroup,
       "hwSlotAccessUserStatGroup": hwSlotAccessUserStatGroup,
       "hwDomainIncludePoolGroup": hwDomainIncludePoolGroup,
       "hwDomainIPPoolMoveTo": hwDomainIPPoolMoveTo,
       "hwUserLogGroup": hwUserLogGroup,
       "hwGlobalDhcpOpt64SepAndSegGroup": hwGlobalDhcpOpt64SepAndSegGroup,
       "hwGlobalDhcpServerAckGroup": hwGlobalDhcpServerAckGroup,
       "hwReauthorizeGroup": hwReauthorizeGroup,
       "hwWlanInterfaceGroup": hwWlanInterfaceGroup,
       "hwAuthorCmdGroup": hwAuthorCmdGroup,
       "hwAAARateGroup": hwAAARateGroup,
       "hwLocalUserPwPolicyAdminGroup": hwLocalUserPwPolicyAdminGroup,
       "hwLocalUserPwPolicyAccGroup": hwLocalUserPwPolicyAccGroup,
       "hwAAADomainIPPoolGroup": hwAAADomainIPPoolGroup,
       "userAuthenProfileGroup": userAuthenProfileGroup,
       "userAuthenticationFreeRuleGroup": userAuthenticationFreeRuleGroup,
       "hwDot1xAccessProfileGroup": hwDot1xAccessProfileGroup,
       "hwMACAuthenAccessProfileGroup": hwMACAuthenAccessProfileGroup,
       "hwPortalAccessProfileGroup": hwPortalAccessProfileGroup}
)
