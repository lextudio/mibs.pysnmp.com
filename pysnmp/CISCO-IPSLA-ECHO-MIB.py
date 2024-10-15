# SNMP MIB module (CISCO-IPSLA-ECHO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSLA-ECHO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:57 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIpSlaEchoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 636)
)
ciscoIpSlaEchoMIB.setRevisions(
        ("2007-08-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpSlaEchoMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpSlaEchoMIBNotifs = _CiscoIpSlaEchoMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 0)
)
_CiscoIpSlaEchoMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpSlaEchoMIBObjects = _CiscoIpSlaEchoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1)
)
_CipslaIcmpEchoTmplTable_Object = MibTable
cipslaIcmpEchoTmplTable = _CipslaIcmpEchoTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1)
)
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplTable.setStatus("current")
_CipslaIcmpEchoTmplEntry_Object = MibTableRow
cipslaIcmpEchoTmplEntry = _CipslaIcmpEchoTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1)
)
cipslaIcmpEchoTmplEntry.setIndexNames(
    (0, "CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplName"),
)
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplEntry.setStatus("current")


class _CipslaIcmpEchoTmplName_Type(SnmpAdminString):
    """Custom type cipslaIcmpEchoTmplName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CipslaIcmpEchoTmplName_Type.__name__ = "SnmpAdminString"
_CipslaIcmpEchoTmplName_Object = MibTableColumn
cipslaIcmpEchoTmplName = _CipslaIcmpEchoTmplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 1),
    _CipslaIcmpEchoTmplName_Type()
)
cipslaIcmpEchoTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplName.setStatus("current")


class _CipslaIcmpEchoTmplDescription_Type(SnmpAdminString):
    """Custom type cipslaIcmpEchoTmplDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CipslaIcmpEchoTmplDescription_Type.__name__ = "SnmpAdminString"
_CipslaIcmpEchoTmplDescription_Object = MibTableColumn
cipslaIcmpEchoTmplDescription = _CipslaIcmpEchoTmplDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 2),
    _CipslaIcmpEchoTmplDescription_Type()
)
cipslaIcmpEchoTmplDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplDescription.setStatus("current")


class _CipslaIcmpEchoTmplSrcAddrType_Type(InetAddressType):
    """Custom type cipslaIcmpEchoTmplSrcAddrType based on InetAddressType"""


_CipslaIcmpEchoTmplSrcAddrType_Object = MibTableColumn
cipslaIcmpEchoTmplSrcAddrType = _CipslaIcmpEchoTmplSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 3),
    _CipslaIcmpEchoTmplSrcAddrType_Type()
)
cipslaIcmpEchoTmplSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplSrcAddrType.setStatus("current")
_CipslaIcmpEchoTmplSrcAddr_Type = InetAddress
_CipslaIcmpEchoTmplSrcAddr_Object = MibTableColumn
cipslaIcmpEchoTmplSrcAddr = _CipslaIcmpEchoTmplSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 4),
    _CipslaIcmpEchoTmplSrcAddr_Type()
)
cipslaIcmpEchoTmplSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplSrcAddr.setStatus("current")


class _CipslaIcmpEchoTmplTimeOut_Type(Unsigned32):
    """Custom type cipslaIcmpEchoTmplTimeOut based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_CipslaIcmpEchoTmplTimeOut_Type.__name__ = "Unsigned32"
_CipslaIcmpEchoTmplTimeOut_Object = MibTableColumn
cipslaIcmpEchoTmplTimeOut = _CipslaIcmpEchoTmplTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 5),
    _CipslaIcmpEchoTmplTimeOut_Type()
)
cipslaIcmpEchoTmplTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplTimeOut.setUnits("milliseconds")


class _CipslaIcmpEchoTmplVerifyData_Type(TruthValue):
    """Custom type cipslaIcmpEchoTmplVerifyData based on TruthValue"""


_CipslaIcmpEchoTmplVerifyData_Object = MibTableColumn
cipslaIcmpEchoTmplVerifyData = _CipslaIcmpEchoTmplVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 6),
    _CipslaIcmpEchoTmplVerifyData_Type()
)
cipslaIcmpEchoTmplVerifyData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplVerifyData.setStatus("current")


class _CipslaIcmpEchoTmplReqDataSize_Type(Unsigned32):
    """Custom type cipslaIcmpEchoTmplReqDataSize based on Unsigned32"""
    defaultValue = 28

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_CipslaIcmpEchoTmplReqDataSize_Type.__name__ = "Unsigned32"
_CipslaIcmpEchoTmplReqDataSize_Object = MibTableColumn
cipslaIcmpEchoTmplReqDataSize = _CipslaIcmpEchoTmplReqDataSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 7),
    _CipslaIcmpEchoTmplReqDataSize_Type()
)
cipslaIcmpEchoTmplReqDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplReqDataSize.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplReqDataSize.setUnits("octets")


class _CipslaIcmpEchoTmplTOS_Type(Unsigned32):
    """Custom type cipslaIcmpEchoTmplTOS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CipslaIcmpEchoTmplTOS_Type.__name__ = "Unsigned32"
_CipslaIcmpEchoTmplTOS_Object = MibTableColumn
cipslaIcmpEchoTmplTOS = _CipslaIcmpEchoTmplTOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 8),
    _CipslaIcmpEchoTmplTOS_Type()
)
cipslaIcmpEchoTmplTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplTOS.setStatus("current")


class _CipslaIcmpEchoTmplVrfName_Type(SnmpAdminString):
    """Custom type cipslaIcmpEchoTmplVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CipslaIcmpEchoTmplVrfName_Type.__name__ = "SnmpAdminString"
_CipslaIcmpEchoTmplVrfName_Object = MibTableColumn
cipslaIcmpEchoTmplVrfName = _CipslaIcmpEchoTmplVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 9),
    _CipslaIcmpEchoTmplVrfName_Type()
)
cipslaIcmpEchoTmplVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplVrfName.setStatus("current")


class _CipslaIcmpEchoTmplThreshold_Type(Unsigned32):
    """Custom type cipslaIcmpEchoTmplThreshold based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipslaIcmpEchoTmplThreshold_Type.__name__ = "Unsigned32"
_CipslaIcmpEchoTmplThreshold_Object = MibTableColumn
cipslaIcmpEchoTmplThreshold = _CipslaIcmpEchoTmplThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 10),
    _CipslaIcmpEchoTmplThreshold_Type()
)
cipslaIcmpEchoTmplThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplThreshold.setUnits("milliseconds")


class _CipslaIcmpEchoTmplHistLives_Type(Unsigned32):
    """Custom type cipslaIcmpEchoTmplHistLives based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CipslaIcmpEchoTmplHistLives_Type.__name__ = "Unsigned32"
_CipslaIcmpEchoTmplHistLives_Object = MibTableColumn
cipslaIcmpEchoTmplHistLives = _CipslaIcmpEchoTmplHistLives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 11),
    _CipslaIcmpEchoTmplHistLives_Type()
)
cipslaIcmpEchoTmplHistLives.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplHistLives.setStatus("current")


class _CipslaIcmpEchoTmplHistBuckets_Type(Unsigned32):
    """Custom type cipslaIcmpEchoTmplHistBuckets based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CipslaIcmpEchoTmplHistBuckets_Type.__name__ = "Unsigned32"
_CipslaIcmpEchoTmplHistBuckets_Object = MibTableColumn
cipslaIcmpEchoTmplHistBuckets = _CipslaIcmpEchoTmplHistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 12),
    _CipslaIcmpEchoTmplHistBuckets_Type()
)
cipslaIcmpEchoTmplHistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplHistBuckets.setStatus("current")


class _CipslaIcmpEchoTmplHistFilter_Type(Integer32):
    """Custom type cipslaIcmpEchoTmplHistFilter based on Integer32"""
    defaultValue = 1

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
        *(("all", 2),
          ("failures", 4),
          ("none", 1),
          ("overThreshold", 3))
    )


_CipslaIcmpEchoTmplHistFilter_Type.__name__ = "Integer32"
_CipslaIcmpEchoTmplHistFilter_Object = MibTableColumn
cipslaIcmpEchoTmplHistFilter = _CipslaIcmpEchoTmplHistFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 13),
    _CipslaIcmpEchoTmplHistFilter_Type()
)
cipslaIcmpEchoTmplHistFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplHistFilter.setStatus("current")


class _CipslaIcmpEchoTmplStatsHours_Type(Unsigned32):
    """Custom type cipslaIcmpEchoTmplStatsHours based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_CipslaIcmpEchoTmplStatsHours_Type.__name__ = "Unsigned32"
_CipslaIcmpEchoTmplStatsHours_Object = MibTableColumn
cipslaIcmpEchoTmplStatsHours = _CipslaIcmpEchoTmplStatsHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 14),
    _CipslaIcmpEchoTmplStatsHours_Type()
)
cipslaIcmpEchoTmplStatsHours.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplStatsHours.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplStatsHours.setUnits("hours")


class _CipslaIcmpEchoTmplDistBuckets_Type(Unsigned32):
    """Custom type cipslaIcmpEchoTmplDistBuckets based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CipslaIcmpEchoTmplDistBuckets_Type.__name__ = "Unsigned32"
_CipslaIcmpEchoTmplDistBuckets_Object = MibTableColumn
cipslaIcmpEchoTmplDistBuckets = _CipslaIcmpEchoTmplDistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 15),
    _CipslaIcmpEchoTmplDistBuckets_Type()
)
cipslaIcmpEchoTmplDistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplDistBuckets.setStatus("current")


class _CipslaIcmpEchoTmplDistInterval_Type(Unsigned32):
    """Custom type cipslaIcmpEchoTmplDistInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CipslaIcmpEchoTmplDistInterval_Type.__name__ = "Unsigned32"
_CipslaIcmpEchoTmplDistInterval_Object = MibTableColumn
cipslaIcmpEchoTmplDistInterval = _CipslaIcmpEchoTmplDistInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 16),
    _CipslaIcmpEchoTmplDistInterval_Type()
)
cipslaIcmpEchoTmplDistInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplDistInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplDistInterval.setUnits("milliseconds")


class _CipslaIcmpEchoTmplStorageType_Type(StorageType):
    """Custom type cipslaIcmpEchoTmplStorageType based on StorageType"""


_CipslaIcmpEchoTmplStorageType_Object = MibTableColumn
cipslaIcmpEchoTmplStorageType = _CipslaIcmpEchoTmplStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 17),
    _CipslaIcmpEchoTmplStorageType_Type()
)
cipslaIcmpEchoTmplStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplStorageType.setStatus("current")
_CipslaIcmpEchoTmplRowStatus_Type = RowStatus
_CipslaIcmpEchoTmplRowStatus_Object = MibTableColumn
cipslaIcmpEchoTmplRowStatus = _CipslaIcmpEchoTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 1, 1, 18),
    _CipslaIcmpEchoTmplRowStatus_Type()
)
cipslaIcmpEchoTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpEchoTmplRowStatus.setStatus("current")
_CipslaUdpEchoTmplTable_Object = MibTable
cipslaUdpEchoTmplTable = _CipslaUdpEchoTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2)
)
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplTable.setStatus("current")
_CipslaUdpEchoTmplEntry_Object = MibTableRow
cipslaUdpEchoTmplEntry = _CipslaUdpEchoTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1)
)
cipslaUdpEchoTmplEntry.setIndexNames(
    (0, "CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplName"),
)
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplEntry.setStatus("current")


class _CipslaUdpEchoTmplName_Type(SnmpAdminString):
    """Custom type cipslaUdpEchoTmplName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CipslaUdpEchoTmplName_Type.__name__ = "SnmpAdminString"
_CipslaUdpEchoTmplName_Object = MibTableColumn
cipslaUdpEchoTmplName = _CipslaUdpEchoTmplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 1),
    _CipslaUdpEchoTmplName_Type()
)
cipslaUdpEchoTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplName.setStatus("current")


class _CipslaUdpEchoTmplDescription_Type(SnmpAdminString):
    """Custom type cipslaUdpEchoTmplDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CipslaUdpEchoTmplDescription_Type.__name__ = "SnmpAdminString"
_CipslaUdpEchoTmplDescription_Object = MibTableColumn
cipslaUdpEchoTmplDescription = _CipslaUdpEchoTmplDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 2),
    _CipslaUdpEchoTmplDescription_Type()
)
cipslaUdpEchoTmplDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplDescription.setStatus("current")


class _CipslaUdpEchoTmplControlEnable_Type(TruthValue):
    """Custom type cipslaUdpEchoTmplControlEnable based on TruthValue"""


_CipslaUdpEchoTmplControlEnable_Object = MibTableColumn
cipslaUdpEchoTmplControlEnable = _CipslaUdpEchoTmplControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 3),
    _CipslaUdpEchoTmplControlEnable_Type()
)
cipslaUdpEchoTmplControlEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplControlEnable.setStatus("current")


class _CipslaUdpEchoTmplSrcAddrType_Type(InetAddressType):
    """Custom type cipslaUdpEchoTmplSrcAddrType based on InetAddressType"""


_CipslaUdpEchoTmplSrcAddrType_Object = MibTableColumn
cipslaUdpEchoTmplSrcAddrType = _CipslaUdpEchoTmplSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 4),
    _CipslaUdpEchoTmplSrcAddrType_Type()
)
cipslaUdpEchoTmplSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplSrcAddrType.setStatus("current")
_CipslaUdpEchoTmplSrcAddr_Type = InetAddress
_CipslaUdpEchoTmplSrcAddr_Object = MibTableColumn
cipslaUdpEchoTmplSrcAddr = _CipslaUdpEchoTmplSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 5),
    _CipslaUdpEchoTmplSrcAddr_Type()
)
cipslaUdpEchoTmplSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplSrcAddr.setStatus("current")


class _CipslaUdpEchoTmplSrcPort_Type(InetPortNumber):
    """Custom type cipslaUdpEchoTmplSrcPort based on InetPortNumber"""
    defaultValue = 0


_CipslaUdpEchoTmplSrcPort_Object = MibTableColumn
cipslaUdpEchoTmplSrcPort = _CipslaUdpEchoTmplSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 6),
    _CipslaUdpEchoTmplSrcPort_Type()
)
cipslaUdpEchoTmplSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplSrcPort.setStatus("current")


class _CipslaUdpEchoTmplTimeOut_Type(Unsigned32):
    """Custom type cipslaUdpEchoTmplTimeOut based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_CipslaUdpEchoTmplTimeOut_Type.__name__ = "Unsigned32"
_CipslaUdpEchoTmplTimeOut_Object = MibTableColumn
cipslaUdpEchoTmplTimeOut = _CipslaUdpEchoTmplTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 7),
    _CipslaUdpEchoTmplTimeOut_Type()
)
cipslaUdpEchoTmplTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplTimeOut.setUnits("milliseconds")


class _CipslaUdpEchoTmplVerifyData_Type(TruthValue):
    """Custom type cipslaUdpEchoTmplVerifyData based on TruthValue"""


_CipslaUdpEchoTmplVerifyData_Object = MibTableColumn
cipslaUdpEchoTmplVerifyData = _CipslaUdpEchoTmplVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 8),
    _CipslaUdpEchoTmplVerifyData_Type()
)
cipslaUdpEchoTmplVerifyData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplVerifyData.setStatus("current")


class _CipslaUdpEchoTmplReqDataSize_Type(Unsigned32):
    """Custom type cipslaUdpEchoTmplReqDataSize based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1500),
    )


_CipslaUdpEchoTmplReqDataSize_Type.__name__ = "Unsigned32"
_CipslaUdpEchoTmplReqDataSize_Object = MibTableColumn
cipslaUdpEchoTmplReqDataSize = _CipslaUdpEchoTmplReqDataSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 9),
    _CipslaUdpEchoTmplReqDataSize_Type()
)
cipslaUdpEchoTmplReqDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplReqDataSize.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplReqDataSize.setUnits("octets")


class _CipslaUdpEchoTmplTOS_Type(Unsigned32):
    """Custom type cipslaUdpEchoTmplTOS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CipslaUdpEchoTmplTOS_Type.__name__ = "Unsigned32"
_CipslaUdpEchoTmplTOS_Object = MibTableColumn
cipslaUdpEchoTmplTOS = _CipslaUdpEchoTmplTOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 10),
    _CipslaUdpEchoTmplTOS_Type()
)
cipslaUdpEchoTmplTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplTOS.setStatus("current")


class _CipslaUdpEchoTmplVrfName_Type(SnmpAdminString):
    """Custom type cipslaUdpEchoTmplVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CipslaUdpEchoTmplVrfName_Type.__name__ = "SnmpAdminString"
_CipslaUdpEchoTmplVrfName_Object = MibTableColumn
cipslaUdpEchoTmplVrfName = _CipslaUdpEchoTmplVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 11),
    _CipslaUdpEchoTmplVrfName_Type()
)
cipslaUdpEchoTmplVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplVrfName.setStatus("current")


class _CipslaUdpEchoTmplThreshold_Type(Unsigned32):
    """Custom type cipslaUdpEchoTmplThreshold based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipslaUdpEchoTmplThreshold_Type.__name__ = "Unsigned32"
_CipslaUdpEchoTmplThreshold_Object = MibTableColumn
cipslaUdpEchoTmplThreshold = _CipslaUdpEchoTmplThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 12),
    _CipslaUdpEchoTmplThreshold_Type()
)
cipslaUdpEchoTmplThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplThreshold.setUnits("milliseconds")


class _CipslaUdpEchoTmplHistLives_Type(Unsigned32):
    """Custom type cipslaUdpEchoTmplHistLives based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CipslaUdpEchoTmplHistLives_Type.__name__ = "Unsigned32"
_CipslaUdpEchoTmplHistLives_Object = MibTableColumn
cipslaUdpEchoTmplHistLives = _CipslaUdpEchoTmplHistLives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 13),
    _CipslaUdpEchoTmplHistLives_Type()
)
cipslaUdpEchoTmplHistLives.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplHistLives.setStatus("current")


class _CipslaUdpEchoTmplHistBuckets_Type(Unsigned32):
    """Custom type cipslaUdpEchoTmplHistBuckets based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CipslaUdpEchoTmplHistBuckets_Type.__name__ = "Unsigned32"
_CipslaUdpEchoTmplHistBuckets_Object = MibTableColumn
cipslaUdpEchoTmplHistBuckets = _CipslaUdpEchoTmplHistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 14),
    _CipslaUdpEchoTmplHistBuckets_Type()
)
cipslaUdpEchoTmplHistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplHistBuckets.setStatus("current")


class _CipslaUdpEchoTmplHistFilter_Type(Integer32):
    """Custom type cipslaUdpEchoTmplHistFilter based on Integer32"""
    defaultValue = 1

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
        *(("all", 2),
          ("failures", 4),
          ("none", 1),
          ("overThreshold", 3))
    )


_CipslaUdpEchoTmplHistFilter_Type.__name__ = "Integer32"
_CipslaUdpEchoTmplHistFilter_Object = MibTableColumn
cipslaUdpEchoTmplHistFilter = _CipslaUdpEchoTmplHistFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 15),
    _CipslaUdpEchoTmplHistFilter_Type()
)
cipslaUdpEchoTmplHistFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplHistFilter.setStatus("current")


class _CipslaUdpEchoTmplStatsHours_Type(Unsigned32):
    """Custom type cipslaUdpEchoTmplStatsHours based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_CipslaUdpEchoTmplStatsHours_Type.__name__ = "Unsigned32"
_CipslaUdpEchoTmplStatsHours_Object = MibTableColumn
cipslaUdpEchoTmplStatsHours = _CipslaUdpEchoTmplStatsHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 16),
    _CipslaUdpEchoTmplStatsHours_Type()
)
cipslaUdpEchoTmplStatsHours.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplStatsHours.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplStatsHours.setUnits("hours")


class _CipslaUdpEchoTmplDistBuckets_Type(Unsigned32):
    """Custom type cipslaUdpEchoTmplDistBuckets based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CipslaUdpEchoTmplDistBuckets_Type.__name__ = "Unsigned32"
_CipslaUdpEchoTmplDistBuckets_Object = MibTableColumn
cipslaUdpEchoTmplDistBuckets = _CipslaUdpEchoTmplDistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 17),
    _CipslaUdpEchoTmplDistBuckets_Type()
)
cipslaUdpEchoTmplDistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplDistBuckets.setStatus("current")


class _CipslaUdpEchoTmplDistInterval_Type(Unsigned32):
    """Custom type cipslaUdpEchoTmplDistInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CipslaUdpEchoTmplDistInterval_Type.__name__ = "Unsigned32"
_CipslaUdpEchoTmplDistInterval_Object = MibTableColumn
cipslaUdpEchoTmplDistInterval = _CipslaUdpEchoTmplDistInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 18),
    _CipslaUdpEchoTmplDistInterval_Type()
)
cipslaUdpEchoTmplDistInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplDistInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplDistInterval.setUnits("milliseconds")


class _CipslaUdpEchoTmplStorageType_Type(StorageType):
    """Custom type cipslaUdpEchoTmplStorageType based on StorageType"""


_CipslaUdpEchoTmplStorageType_Object = MibTableColumn
cipslaUdpEchoTmplStorageType = _CipslaUdpEchoTmplStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 19),
    _CipslaUdpEchoTmplStorageType_Type()
)
cipslaUdpEchoTmplStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplStorageType.setStatus("current")
_CipslaUdpEchoTmplRowStatus_Type = RowStatus
_CipslaUdpEchoTmplRowStatus_Object = MibTableColumn
cipslaUdpEchoTmplRowStatus = _CipslaUdpEchoTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 2, 1, 20),
    _CipslaUdpEchoTmplRowStatus_Type()
)
cipslaUdpEchoTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpEchoTmplRowStatus.setStatus("current")
_CipslaTcpConnTmplTable_Object = MibTable
cipslaTcpConnTmplTable = _CipslaTcpConnTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3)
)
if mibBuilder.loadTexts:
    cipslaTcpConnTmplTable.setStatus("current")
_CipslaTcpConnTmplEntry_Object = MibTableRow
cipslaTcpConnTmplEntry = _CipslaTcpConnTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1)
)
cipslaTcpConnTmplEntry.setIndexNames(
    (0, "CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplName"),
)
if mibBuilder.loadTexts:
    cipslaTcpConnTmplEntry.setStatus("current")


class _CipslaTcpConnTmplName_Type(SnmpAdminString):
    """Custom type cipslaTcpConnTmplName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CipslaTcpConnTmplName_Type.__name__ = "SnmpAdminString"
_CipslaTcpConnTmplName_Object = MibTableColumn
cipslaTcpConnTmplName = _CipslaTcpConnTmplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 1),
    _CipslaTcpConnTmplName_Type()
)
cipslaTcpConnTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplName.setStatus("current")


class _CipslaTcpConnTmplDescription_Type(SnmpAdminString):
    """Custom type cipslaTcpConnTmplDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CipslaTcpConnTmplDescription_Type.__name__ = "SnmpAdminString"
_CipslaTcpConnTmplDescription_Object = MibTableColumn
cipslaTcpConnTmplDescription = _CipslaTcpConnTmplDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 2),
    _CipslaTcpConnTmplDescription_Type()
)
cipslaTcpConnTmplDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplDescription.setStatus("current")


class _CipslaTcpConnTmplControlEnable_Type(TruthValue):
    """Custom type cipslaTcpConnTmplControlEnable based on TruthValue"""


_CipslaTcpConnTmplControlEnable_Object = MibTableColumn
cipslaTcpConnTmplControlEnable = _CipslaTcpConnTmplControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 3),
    _CipslaTcpConnTmplControlEnable_Type()
)
cipslaTcpConnTmplControlEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplControlEnable.setStatus("current")


class _CipslaTcpConnTmplSrcAddrType_Type(InetAddressType):
    """Custom type cipslaTcpConnTmplSrcAddrType based on InetAddressType"""


_CipslaTcpConnTmplSrcAddrType_Object = MibTableColumn
cipslaTcpConnTmplSrcAddrType = _CipslaTcpConnTmplSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 4),
    _CipslaTcpConnTmplSrcAddrType_Type()
)
cipslaTcpConnTmplSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplSrcAddrType.setStatus("current")
_CipslaTcpConnTmplSrcAddr_Type = InetAddress
_CipslaTcpConnTmplSrcAddr_Object = MibTableColumn
cipslaTcpConnTmplSrcAddr = _CipslaTcpConnTmplSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 5),
    _CipslaTcpConnTmplSrcAddr_Type()
)
cipslaTcpConnTmplSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplSrcAddr.setStatus("current")


class _CipslaTcpConnTmplSrcPort_Type(InetPortNumber):
    """Custom type cipslaTcpConnTmplSrcPort based on InetPortNumber"""
    defaultValue = 0


_CipslaTcpConnTmplSrcPort_Object = MibTableColumn
cipslaTcpConnTmplSrcPort = _CipslaTcpConnTmplSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 6),
    _CipslaTcpConnTmplSrcPort_Type()
)
cipslaTcpConnTmplSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplSrcPort.setStatus("current")


class _CipslaTcpConnTmplTimeOut_Type(Unsigned32):
    """Custom type cipslaTcpConnTmplTimeOut based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_CipslaTcpConnTmplTimeOut_Type.__name__ = "Unsigned32"
_CipslaTcpConnTmplTimeOut_Object = MibTableColumn
cipslaTcpConnTmplTimeOut = _CipslaTcpConnTmplTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 7),
    _CipslaTcpConnTmplTimeOut_Type()
)
cipslaTcpConnTmplTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplTimeOut.setUnits("milliseconds")


class _CipslaTcpConnTmplVerifyData_Type(TruthValue):
    """Custom type cipslaTcpConnTmplVerifyData based on TruthValue"""


_CipslaTcpConnTmplVerifyData_Object = MibTableColumn
cipslaTcpConnTmplVerifyData = _CipslaTcpConnTmplVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 8),
    _CipslaTcpConnTmplVerifyData_Type()
)
cipslaTcpConnTmplVerifyData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplVerifyData.setStatus("current")


class _CipslaTcpConnTmplTOS_Type(Unsigned32):
    """Custom type cipslaTcpConnTmplTOS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CipslaTcpConnTmplTOS_Type.__name__ = "Unsigned32"
_CipslaTcpConnTmplTOS_Object = MibTableColumn
cipslaTcpConnTmplTOS = _CipslaTcpConnTmplTOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 9),
    _CipslaTcpConnTmplTOS_Type()
)
cipslaTcpConnTmplTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplTOS.setStatus("current")


class _CipslaTcpConnTmplThreshold_Type(Unsigned32):
    """Custom type cipslaTcpConnTmplThreshold based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipslaTcpConnTmplThreshold_Type.__name__ = "Unsigned32"
_CipslaTcpConnTmplThreshold_Object = MibTableColumn
cipslaTcpConnTmplThreshold = _CipslaTcpConnTmplThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 10),
    _CipslaTcpConnTmplThreshold_Type()
)
cipslaTcpConnTmplThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplThreshold.setUnits("milliseconds")


class _CipslaTcpConnTmplHistLives_Type(Unsigned32):
    """Custom type cipslaTcpConnTmplHistLives based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CipslaTcpConnTmplHistLives_Type.__name__ = "Unsigned32"
_CipslaTcpConnTmplHistLives_Object = MibTableColumn
cipslaTcpConnTmplHistLives = _CipslaTcpConnTmplHistLives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 11),
    _CipslaTcpConnTmplHistLives_Type()
)
cipslaTcpConnTmplHistLives.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplHistLives.setStatus("current")


class _CipslaTcpConnTmplHistBuckets_Type(Unsigned32):
    """Custom type cipslaTcpConnTmplHistBuckets based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CipslaTcpConnTmplHistBuckets_Type.__name__ = "Unsigned32"
_CipslaTcpConnTmplHistBuckets_Object = MibTableColumn
cipslaTcpConnTmplHistBuckets = _CipslaTcpConnTmplHistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 12),
    _CipslaTcpConnTmplHistBuckets_Type()
)
cipslaTcpConnTmplHistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplHistBuckets.setStatus("current")


class _CipslaTcpConnTmplHistFilter_Type(Integer32):
    """Custom type cipslaTcpConnTmplHistFilter based on Integer32"""
    defaultValue = 1

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
        *(("all", 2),
          ("failures", 4),
          ("none", 1),
          ("overThreshold", 3))
    )


_CipslaTcpConnTmplHistFilter_Type.__name__ = "Integer32"
_CipslaTcpConnTmplHistFilter_Object = MibTableColumn
cipslaTcpConnTmplHistFilter = _CipslaTcpConnTmplHistFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 13),
    _CipslaTcpConnTmplHistFilter_Type()
)
cipslaTcpConnTmplHistFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplHistFilter.setStatus("current")


class _CipslaTcpConnTmplStatsHours_Type(Unsigned32):
    """Custom type cipslaTcpConnTmplStatsHours based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_CipslaTcpConnTmplStatsHours_Type.__name__ = "Unsigned32"
_CipslaTcpConnTmplStatsHours_Object = MibTableColumn
cipslaTcpConnTmplStatsHours = _CipslaTcpConnTmplStatsHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 14),
    _CipslaTcpConnTmplStatsHours_Type()
)
cipslaTcpConnTmplStatsHours.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplStatsHours.setStatus("current")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplStatsHours.setUnits("hours")


class _CipslaTcpConnTmplDistBuckets_Type(Unsigned32):
    """Custom type cipslaTcpConnTmplDistBuckets based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CipslaTcpConnTmplDistBuckets_Type.__name__ = "Unsigned32"
_CipslaTcpConnTmplDistBuckets_Object = MibTableColumn
cipslaTcpConnTmplDistBuckets = _CipslaTcpConnTmplDistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 15),
    _CipslaTcpConnTmplDistBuckets_Type()
)
cipslaTcpConnTmplDistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplDistBuckets.setStatus("current")


class _CipslaTcpConnTmplDistInterval_Type(Unsigned32):
    """Custom type cipslaTcpConnTmplDistInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CipslaTcpConnTmplDistInterval_Type.__name__ = "Unsigned32"
_CipslaTcpConnTmplDistInterval_Object = MibTableColumn
cipslaTcpConnTmplDistInterval = _CipslaTcpConnTmplDistInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 16),
    _CipslaTcpConnTmplDistInterval_Type()
)
cipslaTcpConnTmplDistInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplDistInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplDistInterval.setUnits("milliseconds")


class _CipslaTcpConnTmplStorageType_Type(StorageType):
    """Custom type cipslaTcpConnTmplStorageType based on StorageType"""


_CipslaTcpConnTmplStorageType_Object = MibTableColumn
cipslaTcpConnTmplStorageType = _CipslaTcpConnTmplStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 17),
    _CipslaTcpConnTmplStorageType_Type()
)
cipslaTcpConnTmplStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplStorageType.setStatus("current")
_CipslaTcpConnTmplRowStatus_Type = RowStatus
_CipslaTcpConnTmplRowStatus_Object = MibTableColumn
cipslaTcpConnTmplRowStatus = _CipslaTcpConnTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 1, 3, 1, 18),
    _CipslaTcpConnTmplRowStatus_Type()
)
cipslaTcpConnTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaTcpConnTmplRowStatus.setStatus("current")
_CiscoIpSlaEchoMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpSlaEchoMIBConform = _CiscoIpSlaEchoMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 2)
)
_CiscoIpSlaEchoMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpSlaEchoMIBCompliances = _CiscoIpSlaEchoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 2, 1)
)
_CiscoIpSlaEchoMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpSlaEchoMIBGroups = _CiscoIpSlaEchoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 2, 2)
)

# Managed Objects groups

ciscoIpSlaIcmpEchoTmplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 2, 2, 1)
)
ciscoIpSlaIcmpEchoTmplGroup.setObjects(
      *(("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplDescription"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplSrcAddrType"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplSrcAddr"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplTimeOut"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplVerifyData"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplReqDataSize"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplTOS"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplVrfName"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplThreshold"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplHistLives"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplHistBuckets"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplHistFilter"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplStatsHours"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplDistBuckets"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplDistInterval"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplStorageType"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaIcmpEchoTmplRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaIcmpEchoTmplGroup.setStatus("current")

ciscoIpSlaUdpEchoTmplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 2, 2, 2)
)
ciscoIpSlaUdpEchoTmplGroup.setObjects(
      *(("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplDescription"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplControlEnable"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplSrcAddrType"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplSrcAddr"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplSrcPort"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplTimeOut"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplVerifyData"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplReqDataSize"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplTOS"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplVrfName"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplThreshold"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplHistLives"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplHistBuckets"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplHistFilter"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplStatsHours"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplDistBuckets"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplDistInterval"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplStorageType"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaUdpEchoTmplRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaUdpEchoTmplGroup.setStatus("current")

ciscoIpSlaTcpConnTmplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 2, 2, 3)
)
ciscoIpSlaTcpConnTmplGroup.setObjects(
      *(("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplDescription"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplControlEnable"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplSrcAddrType"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplSrcAddr"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplSrcPort"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplTimeOut"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplVerifyData"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplTOS"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplThreshold"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplHistLives"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplHistBuckets"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplHistFilter"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplStatsHours"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplDistBuckets"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplDistInterval"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplStorageType"),
        ("CISCO-IPSLA-ECHO-MIB", "cipslaTcpConnTmplRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaTcpConnTmplGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpSlaEchoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 636, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpSlaEchoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSLA-ECHO-MIB",
    **{"ciscoIpSlaEchoMIB": ciscoIpSlaEchoMIB,
       "ciscoIpSlaEchoMIBNotifs": ciscoIpSlaEchoMIBNotifs,
       "ciscoIpSlaEchoMIBObjects": ciscoIpSlaEchoMIBObjects,
       "cipslaIcmpEchoTmplTable": cipslaIcmpEchoTmplTable,
       "cipslaIcmpEchoTmplEntry": cipslaIcmpEchoTmplEntry,
       "cipslaIcmpEchoTmplName": cipslaIcmpEchoTmplName,
       "cipslaIcmpEchoTmplDescription": cipslaIcmpEchoTmplDescription,
       "cipslaIcmpEchoTmplSrcAddrType": cipslaIcmpEchoTmplSrcAddrType,
       "cipslaIcmpEchoTmplSrcAddr": cipslaIcmpEchoTmplSrcAddr,
       "cipslaIcmpEchoTmplTimeOut": cipslaIcmpEchoTmplTimeOut,
       "cipslaIcmpEchoTmplVerifyData": cipslaIcmpEchoTmplVerifyData,
       "cipslaIcmpEchoTmplReqDataSize": cipslaIcmpEchoTmplReqDataSize,
       "cipslaIcmpEchoTmplTOS": cipslaIcmpEchoTmplTOS,
       "cipslaIcmpEchoTmplVrfName": cipslaIcmpEchoTmplVrfName,
       "cipslaIcmpEchoTmplThreshold": cipslaIcmpEchoTmplThreshold,
       "cipslaIcmpEchoTmplHistLives": cipslaIcmpEchoTmplHistLives,
       "cipslaIcmpEchoTmplHistBuckets": cipslaIcmpEchoTmplHistBuckets,
       "cipslaIcmpEchoTmplHistFilter": cipslaIcmpEchoTmplHistFilter,
       "cipslaIcmpEchoTmplStatsHours": cipslaIcmpEchoTmplStatsHours,
       "cipslaIcmpEchoTmplDistBuckets": cipslaIcmpEchoTmplDistBuckets,
       "cipslaIcmpEchoTmplDistInterval": cipslaIcmpEchoTmplDistInterval,
       "cipslaIcmpEchoTmplStorageType": cipslaIcmpEchoTmplStorageType,
       "cipslaIcmpEchoTmplRowStatus": cipslaIcmpEchoTmplRowStatus,
       "cipslaUdpEchoTmplTable": cipslaUdpEchoTmplTable,
       "cipslaUdpEchoTmplEntry": cipslaUdpEchoTmplEntry,
       "cipslaUdpEchoTmplName": cipslaUdpEchoTmplName,
       "cipslaUdpEchoTmplDescription": cipslaUdpEchoTmplDescription,
       "cipslaUdpEchoTmplControlEnable": cipslaUdpEchoTmplControlEnable,
       "cipslaUdpEchoTmplSrcAddrType": cipslaUdpEchoTmplSrcAddrType,
       "cipslaUdpEchoTmplSrcAddr": cipslaUdpEchoTmplSrcAddr,
       "cipslaUdpEchoTmplSrcPort": cipslaUdpEchoTmplSrcPort,
       "cipslaUdpEchoTmplTimeOut": cipslaUdpEchoTmplTimeOut,
       "cipslaUdpEchoTmplVerifyData": cipslaUdpEchoTmplVerifyData,
       "cipslaUdpEchoTmplReqDataSize": cipslaUdpEchoTmplReqDataSize,
       "cipslaUdpEchoTmplTOS": cipslaUdpEchoTmplTOS,
       "cipslaUdpEchoTmplVrfName": cipslaUdpEchoTmplVrfName,
       "cipslaUdpEchoTmplThreshold": cipslaUdpEchoTmplThreshold,
       "cipslaUdpEchoTmplHistLives": cipslaUdpEchoTmplHistLives,
       "cipslaUdpEchoTmplHistBuckets": cipslaUdpEchoTmplHistBuckets,
       "cipslaUdpEchoTmplHistFilter": cipslaUdpEchoTmplHistFilter,
       "cipslaUdpEchoTmplStatsHours": cipslaUdpEchoTmplStatsHours,
       "cipslaUdpEchoTmplDistBuckets": cipslaUdpEchoTmplDistBuckets,
       "cipslaUdpEchoTmplDistInterval": cipslaUdpEchoTmplDistInterval,
       "cipslaUdpEchoTmplStorageType": cipslaUdpEchoTmplStorageType,
       "cipslaUdpEchoTmplRowStatus": cipslaUdpEchoTmplRowStatus,
       "cipslaTcpConnTmplTable": cipslaTcpConnTmplTable,
       "cipslaTcpConnTmplEntry": cipslaTcpConnTmplEntry,
       "cipslaTcpConnTmplName": cipslaTcpConnTmplName,
       "cipslaTcpConnTmplDescription": cipslaTcpConnTmplDescription,
       "cipslaTcpConnTmplControlEnable": cipslaTcpConnTmplControlEnable,
       "cipslaTcpConnTmplSrcAddrType": cipslaTcpConnTmplSrcAddrType,
       "cipslaTcpConnTmplSrcAddr": cipslaTcpConnTmplSrcAddr,
       "cipslaTcpConnTmplSrcPort": cipslaTcpConnTmplSrcPort,
       "cipslaTcpConnTmplTimeOut": cipslaTcpConnTmplTimeOut,
       "cipslaTcpConnTmplVerifyData": cipslaTcpConnTmplVerifyData,
       "cipslaTcpConnTmplTOS": cipslaTcpConnTmplTOS,
       "cipslaTcpConnTmplThreshold": cipslaTcpConnTmplThreshold,
       "cipslaTcpConnTmplHistLives": cipslaTcpConnTmplHistLives,
       "cipslaTcpConnTmplHistBuckets": cipslaTcpConnTmplHistBuckets,
       "cipslaTcpConnTmplHistFilter": cipslaTcpConnTmplHistFilter,
       "cipslaTcpConnTmplStatsHours": cipslaTcpConnTmplStatsHours,
       "cipslaTcpConnTmplDistBuckets": cipslaTcpConnTmplDistBuckets,
       "cipslaTcpConnTmplDistInterval": cipslaTcpConnTmplDistInterval,
       "cipslaTcpConnTmplStorageType": cipslaTcpConnTmplStorageType,
       "cipslaTcpConnTmplRowStatus": cipslaTcpConnTmplRowStatus,
       "ciscoIpSlaEchoMIBConform": ciscoIpSlaEchoMIBConform,
       "ciscoIpSlaEchoMIBCompliances": ciscoIpSlaEchoMIBCompliances,
       "ciscoIpSlaEchoMIBCompliance": ciscoIpSlaEchoMIBCompliance,
       "ciscoIpSlaEchoMIBGroups": ciscoIpSlaEchoMIBGroups,
       "ciscoIpSlaIcmpEchoTmplGroup": ciscoIpSlaIcmpEchoTmplGroup,
       "ciscoIpSlaUdpEchoTmplGroup": ciscoIpSlaUdpEchoTmplGroup,
       "ciscoIpSlaTcpConnTmplGroup": ciscoIpSlaTcpConnTmplGroup}
)
