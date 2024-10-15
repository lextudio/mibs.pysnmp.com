# SNMP MIB module (CISCO-IPSLA-JITTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSLA-JITTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:00 2024
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

(IpSlaCodecType,) = mibBuilder.importSymbols(
    "CISCO-IPSLA-TC-MIB",
    "IpSlaCodecType")

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

ciscoIpSlaJitterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 635)
)
ciscoIpSlaJitterMIB.setRevisions(
        ("2007-07-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpSlaJitterMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpSlaJitterMIBNotifs = _CiscoIpSlaJitterMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 0)
)
_CiscoIpSlaJitterMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpSlaJitterMIBObjects = _CiscoIpSlaJitterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1)
)
_CipslaUdpJitterTmplTable_Object = MibTable
cipslaUdpJitterTmplTable = _CipslaUdpJitterTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1)
)
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplTable.setStatus("current")
_CipslaUdpJitterTmplEntry_Object = MibTableRow
cipslaUdpJitterTmplEntry = _CipslaUdpJitterTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1)
)
cipslaUdpJitterTmplEntry.setIndexNames(
    (0, "CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplName"),
)
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplEntry.setStatus("current")


class _CipslaUdpJitterTmplName_Type(SnmpAdminString):
    """Custom type cipslaUdpJitterTmplName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CipslaUdpJitterTmplName_Type.__name__ = "SnmpAdminString"
_CipslaUdpJitterTmplName_Object = MibTableColumn
cipslaUdpJitterTmplName = _CipslaUdpJitterTmplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 1),
    _CipslaUdpJitterTmplName_Type()
)
cipslaUdpJitterTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplName.setStatus("current")


class _CipslaUdpJitterTmplDescription_Type(SnmpAdminString):
    """Custom type cipslaUdpJitterTmplDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CipslaUdpJitterTmplDescription_Type.__name__ = "SnmpAdminString"
_CipslaUdpJitterTmplDescription_Object = MibTableColumn
cipslaUdpJitterTmplDescription = _CipslaUdpJitterTmplDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 2),
    _CipslaUdpJitterTmplDescription_Type()
)
cipslaUdpJitterTmplDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplDescription.setStatus("current")


class _CipslaUdpJitterTmplControlEnable_Type(TruthValue):
    """Custom type cipslaUdpJitterTmplControlEnable based on TruthValue"""


_CipslaUdpJitterTmplControlEnable_Object = MibTableColumn
cipslaUdpJitterTmplControlEnable = _CipslaUdpJitterTmplControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 3),
    _CipslaUdpJitterTmplControlEnable_Type()
)
cipslaUdpJitterTmplControlEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplControlEnable.setStatus("current")


class _CipslaUdpJitterTmplTimeOut_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplTimeOut based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_CipslaUdpJitterTmplTimeOut_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplTimeOut_Object = MibTableColumn
cipslaUdpJitterTmplTimeOut = _CipslaUdpJitterTmplTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 4),
    _CipslaUdpJitterTmplTimeOut_Type()
)
cipslaUdpJitterTmplTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplTimeOut.setUnits("milliseconds")


class _CipslaUdpJitterTmplVerifyData_Type(TruthValue):
    """Custom type cipslaUdpJitterTmplVerifyData based on TruthValue"""


_CipslaUdpJitterTmplVerifyData_Object = MibTableColumn
cipslaUdpJitterTmplVerifyData = _CipslaUdpJitterTmplVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 5),
    _CipslaUdpJitterTmplVerifyData_Type()
)
cipslaUdpJitterTmplVerifyData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplVerifyData.setStatus("current")
_CipslaUdpJitterTmplCodecType_Type = IpSlaCodecType
_CipslaUdpJitterTmplCodecType_Object = MibTableColumn
cipslaUdpJitterTmplCodecType = _CipslaUdpJitterTmplCodecType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 6),
    _CipslaUdpJitterTmplCodecType_Type()
)
cipslaUdpJitterTmplCodecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplCodecType.setStatus("current")


class _CipslaUdpJitterTmplCodecInterval_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplCodecInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60000),
    )


_CipslaUdpJitterTmplCodecInterval_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplCodecInterval_Object = MibTableColumn
cipslaUdpJitterTmplCodecInterval = _CipslaUdpJitterTmplCodecInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 7),
    _CipslaUdpJitterTmplCodecInterval_Type()
)
cipslaUdpJitterTmplCodecInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplCodecInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplCodecInterval.setUnits("milliseconds")


class _CipslaUdpJitterTmplCodecPayload_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplCodecPayload based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_CipslaUdpJitterTmplCodecPayload_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplCodecPayload_Object = MibTableColumn
cipslaUdpJitterTmplCodecPayload = _CipslaUdpJitterTmplCodecPayload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 8),
    _CipslaUdpJitterTmplCodecPayload_Type()
)
cipslaUdpJitterTmplCodecPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplCodecPayload.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplCodecPayload.setUnits("octets")


class _CipslaUdpJitterTmplCodecNumPkts_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplCodecNumPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_CipslaUdpJitterTmplCodecNumPkts_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplCodecNumPkts_Object = MibTableColumn
cipslaUdpJitterTmplCodecNumPkts = _CipslaUdpJitterTmplCodecNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 9),
    _CipslaUdpJitterTmplCodecNumPkts_Type()
)
cipslaUdpJitterTmplCodecNumPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplCodecNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplCodecNumPkts.setUnits("packets")


class _CipslaUdpJitterTmplInterval_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60000),
    )


_CipslaUdpJitterTmplInterval_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplInterval_Object = MibTableColumn
cipslaUdpJitterTmplInterval = _CipslaUdpJitterTmplInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 10),
    _CipslaUdpJitterTmplInterval_Type()
)
cipslaUdpJitterTmplInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplInterval.setUnits("milliseconds")


class _CipslaUdpJitterTmplNumPkts_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplNumPkts based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_CipslaUdpJitterTmplNumPkts_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplNumPkts_Object = MibTableColumn
cipslaUdpJitterTmplNumPkts = _CipslaUdpJitterTmplNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 11),
    _CipslaUdpJitterTmplNumPkts_Type()
)
cipslaUdpJitterTmplNumPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplNumPkts.setUnits("packets")


class _CipslaUdpJitterTmplSrcAddrType_Type(InetAddressType):
    """Custom type cipslaUdpJitterTmplSrcAddrType based on InetAddressType"""


_CipslaUdpJitterTmplSrcAddrType_Object = MibTableColumn
cipslaUdpJitterTmplSrcAddrType = _CipslaUdpJitterTmplSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 12),
    _CipslaUdpJitterTmplSrcAddrType_Type()
)
cipslaUdpJitterTmplSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplSrcAddrType.setStatus("current")
_CipslaUdpJitterTmplSrcAddr_Type = InetAddress
_CipslaUdpJitterTmplSrcAddr_Object = MibTableColumn
cipslaUdpJitterTmplSrcAddr = _CipslaUdpJitterTmplSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 13),
    _CipslaUdpJitterTmplSrcAddr_Type()
)
cipslaUdpJitterTmplSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplSrcAddr.setStatus("current")


class _CipslaUdpJitterTmplSrcPort_Type(InetPortNumber):
    """Custom type cipslaUdpJitterTmplSrcPort based on InetPortNumber"""
    defaultValue = 0


_CipslaUdpJitterTmplSrcPort_Object = MibTableColumn
cipslaUdpJitterTmplSrcPort = _CipslaUdpJitterTmplSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 14),
    _CipslaUdpJitterTmplSrcPort_Type()
)
cipslaUdpJitterTmplSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplSrcPort.setStatus("current")


class _CipslaUdpJitterTmplPrecision_Type(Integer32):
    """Custom type cipslaUdpJitterTmplPrecision based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("microseconds", 2),
          ("milliseconds", 1))
    )


_CipslaUdpJitterTmplPrecision_Type.__name__ = "Integer32"
_CipslaUdpJitterTmplPrecision_Object = MibTableColumn
cipslaUdpJitterTmplPrecision = _CipslaUdpJitterTmplPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 15),
    _CipslaUdpJitterTmplPrecision_Type()
)
cipslaUdpJitterTmplPrecision.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplPrecision.setStatus("current")


class _CipslaUdpJitterTmplReqDataSize_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplReqDataSize based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 65024),
    )


_CipslaUdpJitterTmplReqDataSize_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplReqDataSize_Object = MibTableColumn
cipslaUdpJitterTmplReqDataSize = _CipslaUdpJitterTmplReqDataSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 16),
    _CipslaUdpJitterTmplReqDataSize_Type()
)
cipslaUdpJitterTmplReqDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplReqDataSize.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplReqDataSize.setUnits("octets")


class _CipslaUdpJitterTmplPktPriority_Type(Integer32):
    """Custom type cipslaUdpJitterTmplPktPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_CipslaUdpJitterTmplPktPriority_Type.__name__ = "Integer32"
_CipslaUdpJitterTmplPktPriority_Object = MibTableColumn
cipslaUdpJitterTmplPktPriority = _CipslaUdpJitterTmplPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 17),
    _CipslaUdpJitterTmplPktPriority_Type()
)
cipslaUdpJitterTmplPktPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplPktPriority.setStatus("current")


class _CipslaUdpJitterTmplTOS_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplTOS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CipslaUdpJitterTmplTOS_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplTOS_Object = MibTableColumn
cipslaUdpJitterTmplTOS = _CipslaUdpJitterTmplTOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 18),
    _CipslaUdpJitterTmplTOS_Type()
)
cipslaUdpJitterTmplTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplTOS.setStatus("current")


class _CipslaUdpJitterTmplVrfName_Type(SnmpAdminString):
    """Custom type cipslaUdpJitterTmplVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CipslaUdpJitterTmplVrfName_Type.__name__ = "SnmpAdminString"
_CipslaUdpJitterTmplVrfName_Object = MibTableColumn
cipslaUdpJitterTmplVrfName = _CipslaUdpJitterTmplVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 19),
    _CipslaUdpJitterTmplVrfName_Type()
)
cipslaUdpJitterTmplVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplVrfName.setStatus("current")


class _CipslaUdpJitterTmplThreshold_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplThreshold based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipslaUdpJitterTmplThreshold_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplThreshold_Object = MibTableColumn
cipslaUdpJitterTmplThreshold = _CipslaUdpJitterTmplThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 20),
    _CipslaUdpJitterTmplThreshold_Type()
)
cipslaUdpJitterTmplThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplThreshold.setUnits("milliseconds")


class _CipslaUdpJitterTmplNTPTolAbs_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplNTPTolAbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CipslaUdpJitterTmplNTPTolAbs_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplNTPTolAbs_Object = MibTableColumn
cipslaUdpJitterTmplNTPTolAbs = _CipslaUdpJitterTmplNTPTolAbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 21),
    _CipslaUdpJitterTmplNTPTolAbs_Type()
)
cipslaUdpJitterTmplNTPTolAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplNTPTolAbs.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplNTPTolAbs.setUnits("microseconds")


class _CipslaUdpJitterTmplNTPTolPct_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplNTPTolPct based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipslaUdpJitterTmplNTPTolPct_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplNTPTolPct_Object = MibTableColumn
cipslaUdpJitterTmplNTPTolPct = _CipslaUdpJitterTmplNTPTolPct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 22),
    _CipslaUdpJitterTmplNTPTolPct_Type()
)
cipslaUdpJitterTmplNTPTolPct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplNTPTolPct.setStatus("current")


class _CipslaUdpJitterTmplNTPTolType_Type(Integer32):
    """Custom type cipslaUdpJitterTmplNTPTolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 2),
          ("percent", 1))
    )


_CipslaUdpJitterTmplNTPTolType_Type.__name__ = "Integer32"
_CipslaUdpJitterTmplNTPTolType_Object = MibTableColumn
cipslaUdpJitterTmplNTPTolType = _CipslaUdpJitterTmplNTPTolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 23),
    _CipslaUdpJitterTmplNTPTolType_Type()
)
cipslaUdpJitterTmplNTPTolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplNTPTolType.setStatus("current")


class _CipslaUdpJitterTmplIcpifFactor_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplIcpifFactor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CipslaUdpJitterTmplIcpifFactor_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplIcpifFactor_Object = MibTableColumn
cipslaUdpJitterTmplIcpifFactor = _CipslaUdpJitterTmplIcpifFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 24),
    _CipslaUdpJitterTmplIcpifFactor_Type()
)
cipslaUdpJitterTmplIcpifFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplIcpifFactor.setStatus("current")


class _CipslaUdpJitterTmplStatsHours_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplStatsHours based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_CipslaUdpJitterTmplStatsHours_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplStatsHours_Object = MibTableColumn
cipslaUdpJitterTmplStatsHours = _CipslaUdpJitterTmplStatsHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 25),
    _CipslaUdpJitterTmplStatsHours_Type()
)
cipslaUdpJitterTmplStatsHours.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplStatsHours.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplStatsHours.setUnits("hours")


class _CipslaUdpJitterTmplDistBuckets_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplDistBuckets based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CipslaUdpJitterTmplDistBuckets_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplDistBuckets_Object = MibTableColumn
cipslaUdpJitterTmplDistBuckets = _CipslaUdpJitterTmplDistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 26),
    _CipslaUdpJitterTmplDistBuckets_Type()
)
cipslaUdpJitterTmplDistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplDistBuckets.setStatus("current")


class _CipslaUdpJitterTmplDistInterval_Type(Unsigned32):
    """Custom type cipslaUdpJitterTmplDistInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CipslaUdpJitterTmplDistInterval_Type.__name__ = "Unsigned32"
_CipslaUdpJitterTmplDistInterval_Object = MibTableColumn
cipslaUdpJitterTmplDistInterval = _CipslaUdpJitterTmplDistInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 27),
    _CipslaUdpJitterTmplDistInterval_Type()
)
cipslaUdpJitterTmplDistInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplDistInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplDistInterval.setUnits("milliseconds")


class _CipslaUdpJitterTmplStorageType_Type(StorageType):
    """Custom type cipslaUdpJitterTmplStorageType based on StorageType"""


_CipslaUdpJitterTmplStorageType_Object = MibTableColumn
cipslaUdpJitterTmplStorageType = _CipslaUdpJitterTmplStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 28),
    _CipslaUdpJitterTmplStorageType_Type()
)
cipslaUdpJitterTmplStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplStorageType.setStatus("current")
_CipslaUdpJitterTmplRowStatus_Type = RowStatus
_CipslaUdpJitterTmplRowStatus_Object = MibTableColumn
cipslaUdpJitterTmplRowStatus = _CipslaUdpJitterTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 1, 1, 30),
    _CipslaUdpJitterTmplRowStatus_Type()
)
cipslaUdpJitterTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaUdpJitterTmplRowStatus.setStatus("current")
_CipslaIcmpJitterTmplTable_Object = MibTable
cipslaIcmpJitterTmplTable = _CipslaIcmpJitterTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2)
)
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplTable.setStatus("current")
_CipslaIcmpJitterTmplEntry_Object = MibTableRow
cipslaIcmpJitterTmplEntry = _CipslaIcmpJitterTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1)
)
cipslaIcmpJitterTmplEntry.setIndexNames(
    (0, "CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplName"),
)
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplEntry.setStatus("current")


class _CipslaIcmpJitterTmplName_Type(SnmpAdminString):
    """Custom type cipslaIcmpJitterTmplName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CipslaIcmpJitterTmplName_Type.__name__ = "SnmpAdminString"
_CipslaIcmpJitterTmplName_Object = MibTableColumn
cipslaIcmpJitterTmplName = _CipslaIcmpJitterTmplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 1),
    _CipslaIcmpJitterTmplName_Type()
)
cipslaIcmpJitterTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplName.setStatus("current")


class _CipslaIcmpJitterTmplDescription_Type(SnmpAdminString):
    """Custom type cipslaIcmpJitterTmplDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CipslaIcmpJitterTmplDescription_Type.__name__ = "SnmpAdminString"
_CipslaIcmpJitterTmplDescription_Object = MibTableColumn
cipslaIcmpJitterTmplDescription = _CipslaIcmpJitterTmplDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 2),
    _CipslaIcmpJitterTmplDescription_Type()
)
cipslaIcmpJitterTmplDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplDescription.setStatus("current")


class _CipslaIcmpJitterTmplTimeOut_Type(Unsigned32):
    """Custom type cipslaIcmpJitterTmplTimeOut based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_CipslaIcmpJitterTmplTimeOut_Type.__name__ = "Unsigned32"
_CipslaIcmpJitterTmplTimeOut_Object = MibTableColumn
cipslaIcmpJitterTmplTimeOut = _CipslaIcmpJitterTmplTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 3),
    _CipslaIcmpJitterTmplTimeOut_Type()
)
cipslaIcmpJitterTmplTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplTimeOut.setUnits("milliseconds")


class _CipslaIcmpJitterTmplVerifyData_Type(TruthValue):
    """Custom type cipslaIcmpJitterTmplVerifyData based on TruthValue"""


_CipslaIcmpJitterTmplVerifyData_Object = MibTableColumn
cipslaIcmpJitterTmplVerifyData = _CipslaIcmpJitterTmplVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 4),
    _CipslaIcmpJitterTmplVerifyData_Type()
)
cipslaIcmpJitterTmplVerifyData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplVerifyData.setStatus("current")


class _CipslaIcmpJitterTmplNumPkts_Type(Unsigned32):
    """Custom type cipslaIcmpJitterTmplNumPkts based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_CipslaIcmpJitterTmplNumPkts_Type.__name__ = "Unsigned32"
_CipslaIcmpJitterTmplNumPkts_Object = MibTableColumn
cipslaIcmpJitterTmplNumPkts = _CipslaIcmpJitterTmplNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 5),
    _CipslaIcmpJitterTmplNumPkts_Type()
)
cipslaIcmpJitterTmplNumPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplNumPkts.setUnits("packets")


class _CipslaIcmpJitterTmplInterval_Type(Unsigned32):
    """Custom type cipslaIcmpJitterTmplInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60000),
    )


_CipslaIcmpJitterTmplInterval_Type.__name__ = "Unsigned32"
_CipslaIcmpJitterTmplInterval_Object = MibTableColumn
cipslaIcmpJitterTmplInterval = _CipslaIcmpJitterTmplInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 6),
    _CipslaIcmpJitterTmplInterval_Type()
)
cipslaIcmpJitterTmplInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplInterval.setUnits("milliseconds")


class _CipslaIcmpJitterTmplSrcAddrType_Type(InetAddressType):
    """Custom type cipslaIcmpJitterTmplSrcAddrType based on InetAddressType"""


_CipslaIcmpJitterTmplSrcAddrType_Object = MibTableColumn
cipslaIcmpJitterTmplSrcAddrType = _CipslaIcmpJitterTmplSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 7),
    _CipslaIcmpJitterTmplSrcAddrType_Type()
)
cipslaIcmpJitterTmplSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplSrcAddrType.setStatus("current")
_CipslaIcmpJitterTmplSrcAddr_Type = InetAddress
_CipslaIcmpJitterTmplSrcAddr_Object = MibTableColumn
cipslaIcmpJitterTmplSrcAddr = _CipslaIcmpJitterTmplSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 8),
    _CipslaIcmpJitterTmplSrcAddr_Type()
)
cipslaIcmpJitterTmplSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplSrcAddr.setStatus("current")


class _CipslaIcmpJitterTmplTOS_Type(Unsigned32):
    """Custom type cipslaIcmpJitterTmplTOS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CipslaIcmpJitterTmplTOS_Type.__name__ = "Unsigned32"
_CipslaIcmpJitterTmplTOS_Object = MibTableColumn
cipslaIcmpJitterTmplTOS = _CipslaIcmpJitterTmplTOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 9),
    _CipslaIcmpJitterTmplTOS_Type()
)
cipslaIcmpJitterTmplTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplTOS.setStatus("current")


class _CipslaIcmpJitterTmplVrfName_Type(SnmpAdminString):
    """Custom type cipslaIcmpJitterTmplVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CipslaIcmpJitterTmplVrfName_Type.__name__ = "SnmpAdminString"
_CipslaIcmpJitterTmplVrfName_Object = MibTableColumn
cipslaIcmpJitterTmplVrfName = _CipslaIcmpJitterTmplVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 10),
    _CipslaIcmpJitterTmplVrfName_Type()
)
cipslaIcmpJitterTmplVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplVrfName.setStatus("current")


class _CipslaIcmpJitterTmplThreshold_Type(Unsigned32):
    """Custom type cipslaIcmpJitterTmplThreshold based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipslaIcmpJitterTmplThreshold_Type.__name__ = "Unsigned32"
_CipslaIcmpJitterTmplThreshold_Object = MibTableColumn
cipslaIcmpJitterTmplThreshold = _CipslaIcmpJitterTmplThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 11),
    _CipslaIcmpJitterTmplThreshold_Type()
)
cipslaIcmpJitterTmplThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplThreshold.setUnits("milliseconds")


class _CipslaIcmpJitterTmplStatsHours_Type(Unsigned32):
    """Custom type cipslaIcmpJitterTmplStatsHours based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_CipslaIcmpJitterTmplStatsHours_Type.__name__ = "Unsigned32"
_CipslaIcmpJitterTmplStatsHours_Object = MibTableColumn
cipslaIcmpJitterTmplStatsHours = _CipslaIcmpJitterTmplStatsHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 12),
    _CipslaIcmpJitterTmplStatsHours_Type()
)
cipslaIcmpJitterTmplStatsHours.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplStatsHours.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplStatsHours.setUnits("hours")


class _CipslaIcmpJitterTmplDistBuckets_Type(Unsigned32):
    """Custom type cipslaIcmpJitterTmplDistBuckets based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CipslaIcmpJitterTmplDistBuckets_Type.__name__ = "Unsigned32"
_CipslaIcmpJitterTmplDistBuckets_Object = MibTableColumn
cipslaIcmpJitterTmplDistBuckets = _CipslaIcmpJitterTmplDistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 13),
    _CipslaIcmpJitterTmplDistBuckets_Type()
)
cipslaIcmpJitterTmplDistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplDistBuckets.setStatus("current")


class _CipslaIcmpJitterTmplDistInterval_Type(Unsigned32):
    """Custom type cipslaIcmpJitterTmplDistInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CipslaIcmpJitterTmplDistInterval_Type.__name__ = "Unsigned32"
_CipslaIcmpJitterTmplDistInterval_Object = MibTableColumn
cipslaIcmpJitterTmplDistInterval = _CipslaIcmpJitterTmplDistInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 14),
    _CipslaIcmpJitterTmplDistInterval_Type()
)
cipslaIcmpJitterTmplDistInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplDistInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplDistInterval.setUnits("milliseconds")


class _CipslaIcmpJitterTmplStorageType_Type(StorageType):
    """Custom type cipslaIcmpJitterTmplStorageType based on StorageType"""


_CipslaIcmpJitterTmplStorageType_Object = MibTableColumn
cipslaIcmpJitterTmplStorageType = _CipslaIcmpJitterTmplStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 15),
    _CipslaIcmpJitterTmplStorageType_Type()
)
cipslaIcmpJitterTmplStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplStorageType.setStatus("current")
_CipslaIcmpJitterTmplRowStatus_Type = RowStatus
_CipslaIcmpJitterTmplRowStatus_Object = MibTableColumn
cipslaIcmpJitterTmplRowStatus = _CipslaIcmpJitterTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 1, 2, 1, 16),
    _CipslaIcmpJitterTmplRowStatus_Type()
)
cipslaIcmpJitterTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipslaIcmpJitterTmplRowStatus.setStatus("current")
_CiscoIpSlaJitterMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpSlaJitterMIBConform = _CiscoIpSlaJitterMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 2)
)
_CiscoIpSlaJitterMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpSlaJitterMIBCompliances = _CiscoIpSlaJitterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 2, 1)
)
_CiscoIpSlaJitterMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpSlaJitterMIBGroups = _CiscoIpSlaJitterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 2, 2)
)

# Managed Objects groups

ciscoIpSlaUdpJitterTmplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 2, 2, 1)
)
ciscoIpSlaUdpJitterTmplGroup.setObjects(
      *(("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplDescription"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplControlEnable"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplTimeOut"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplVerifyData"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplCodecType"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplCodecInterval"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplCodecPayload"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplCodecNumPkts"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplInterval"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplNumPkts"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplSrcAddrType"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplSrcAddr"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplSrcPort"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplPrecision"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplReqDataSize"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplPktPriority"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplTOS"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplVrfName"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplThreshold"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplNTPTolAbs"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplNTPTolPct"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplNTPTolType"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplIcpifFactor"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplStatsHours"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplDistBuckets"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplDistInterval"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplStorageType"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaUdpJitterTmplRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaUdpJitterTmplGroup.setStatus("current")

ciscoIpSlaIcmpJitterTmplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 2, 2, 2)
)
ciscoIpSlaIcmpJitterTmplGroup.setObjects(
      *(("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplDescription"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplTimeOut"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplVerifyData"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplNumPkts"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplInterval"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplSrcAddrType"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplSrcAddr"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplTOS"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplVrfName"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplThreshold"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplStatsHours"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplDistBuckets"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplDistInterval"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplStorageType"),
        ("CISCO-IPSLA-JITTER-MIB", "cipslaIcmpJitterTmplRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpSlaIcmpJitterTmplGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpSlaJitterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 635, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpSlaJitterMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSLA-JITTER-MIB",
    **{"ciscoIpSlaJitterMIB": ciscoIpSlaJitterMIB,
       "ciscoIpSlaJitterMIBNotifs": ciscoIpSlaJitterMIBNotifs,
       "ciscoIpSlaJitterMIBObjects": ciscoIpSlaJitterMIBObjects,
       "cipslaUdpJitterTmplTable": cipslaUdpJitterTmplTable,
       "cipslaUdpJitterTmplEntry": cipslaUdpJitterTmplEntry,
       "cipslaUdpJitterTmplName": cipslaUdpJitterTmplName,
       "cipslaUdpJitterTmplDescription": cipslaUdpJitterTmplDescription,
       "cipslaUdpJitterTmplControlEnable": cipslaUdpJitterTmplControlEnable,
       "cipslaUdpJitterTmplTimeOut": cipslaUdpJitterTmplTimeOut,
       "cipslaUdpJitterTmplVerifyData": cipslaUdpJitterTmplVerifyData,
       "cipslaUdpJitterTmplCodecType": cipslaUdpJitterTmplCodecType,
       "cipslaUdpJitterTmplCodecInterval": cipslaUdpJitterTmplCodecInterval,
       "cipslaUdpJitterTmplCodecPayload": cipslaUdpJitterTmplCodecPayload,
       "cipslaUdpJitterTmplCodecNumPkts": cipslaUdpJitterTmplCodecNumPkts,
       "cipslaUdpJitterTmplInterval": cipslaUdpJitterTmplInterval,
       "cipslaUdpJitterTmplNumPkts": cipslaUdpJitterTmplNumPkts,
       "cipslaUdpJitterTmplSrcAddrType": cipslaUdpJitterTmplSrcAddrType,
       "cipslaUdpJitterTmplSrcAddr": cipslaUdpJitterTmplSrcAddr,
       "cipslaUdpJitterTmplSrcPort": cipslaUdpJitterTmplSrcPort,
       "cipslaUdpJitterTmplPrecision": cipslaUdpJitterTmplPrecision,
       "cipslaUdpJitterTmplReqDataSize": cipslaUdpJitterTmplReqDataSize,
       "cipslaUdpJitterTmplPktPriority": cipslaUdpJitterTmplPktPriority,
       "cipslaUdpJitterTmplTOS": cipslaUdpJitterTmplTOS,
       "cipslaUdpJitterTmplVrfName": cipslaUdpJitterTmplVrfName,
       "cipslaUdpJitterTmplThreshold": cipslaUdpJitterTmplThreshold,
       "cipslaUdpJitterTmplNTPTolAbs": cipslaUdpJitterTmplNTPTolAbs,
       "cipslaUdpJitterTmplNTPTolPct": cipslaUdpJitterTmplNTPTolPct,
       "cipslaUdpJitterTmplNTPTolType": cipslaUdpJitterTmplNTPTolType,
       "cipslaUdpJitterTmplIcpifFactor": cipslaUdpJitterTmplIcpifFactor,
       "cipslaUdpJitterTmplStatsHours": cipslaUdpJitterTmplStatsHours,
       "cipslaUdpJitterTmplDistBuckets": cipslaUdpJitterTmplDistBuckets,
       "cipslaUdpJitterTmplDistInterval": cipslaUdpJitterTmplDistInterval,
       "cipslaUdpJitterTmplStorageType": cipslaUdpJitterTmplStorageType,
       "cipslaUdpJitterTmplRowStatus": cipslaUdpJitterTmplRowStatus,
       "cipslaIcmpJitterTmplTable": cipslaIcmpJitterTmplTable,
       "cipslaIcmpJitterTmplEntry": cipslaIcmpJitterTmplEntry,
       "cipslaIcmpJitterTmplName": cipslaIcmpJitterTmplName,
       "cipslaIcmpJitterTmplDescription": cipslaIcmpJitterTmplDescription,
       "cipslaIcmpJitterTmplTimeOut": cipslaIcmpJitterTmplTimeOut,
       "cipslaIcmpJitterTmplVerifyData": cipslaIcmpJitterTmplVerifyData,
       "cipslaIcmpJitterTmplNumPkts": cipslaIcmpJitterTmplNumPkts,
       "cipslaIcmpJitterTmplInterval": cipslaIcmpJitterTmplInterval,
       "cipslaIcmpJitterTmplSrcAddrType": cipslaIcmpJitterTmplSrcAddrType,
       "cipslaIcmpJitterTmplSrcAddr": cipslaIcmpJitterTmplSrcAddr,
       "cipslaIcmpJitterTmplTOS": cipslaIcmpJitterTmplTOS,
       "cipslaIcmpJitterTmplVrfName": cipslaIcmpJitterTmplVrfName,
       "cipslaIcmpJitterTmplThreshold": cipslaIcmpJitterTmplThreshold,
       "cipslaIcmpJitterTmplStatsHours": cipslaIcmpJitterTmplStatsHours,
       "cipslaIcmpJitterTmplDistBuckets": cipslaIcmpJitterTmplDistBuckets,
       "cipslaIcmpJitterTmplDistInterval": cipslaIcmpJitterTmplDistInterval,
       "cipslaIcmpJitterTmplStorageType": cipslaIcmpJitterTmplStorageType,
       "cipslaIcmpJitterTmplRowStatus": cipslaIcmpJitterTmplRowStatus,
       "ciscoIpSlaJitterMIBConform": ciscoIpSlaJitterMIBConform,
       "ciscoIpSlaJitterMIBCompliances": ciscoIpSlaJitterMIBCompliances,
       "ciscoIpSlaJitterMIBCompliance": ciscoIpSlaJitterMIBCompliance,
       "ciscoIpSlaJitterMIBGroups": ciscoIpSlaJitterMIBGroups,
       "ciscoIpSlaUdpJitterTmplGroup": ciscoIpSlaUdpJitterTmplGroup,
       "ciscoIpSlaIcmpJitterTmplGroup": ciscoIpSlaIcmpJitterTmplGroup}
)
