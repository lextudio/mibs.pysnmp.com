# SNMP MIB module (ZHONE-COM-IP-IPSLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-IPSLA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:16 2024
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

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(ZhoneRDIndex,
 rdIndex) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-RD-MIB",
    "ZhoneRDIndex",
    "rdIndex")

(zhoneIp,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp")


# MODULE-IDENTITY

zhoneIpSLA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21)
)
zhoneIpSLA.setRevisions(
        ("2007-06-05 07:16",
         "2006-11-16 10:48",
         "2006-11-03 07:57")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneIpSLAMibObjects_ObjectIdentity = ObjectIdentity
zhoneIpSLAMibObjects = _ZhoneIpSLAMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1)
)


class _ZhoneIpSLAGlobalEnable_Type(Integer32):
    """Custom type zhoneIpSLAGlobalEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ZhoneIpSLAGlobalEnable_Type.__name__ = "Integer32"
_ZhoneIpSLAGlobalEnable_Object = MibScalar
zhoneIpSLAGlobalEnable = _ZhoneIpSLAGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 1),
    _ZhoneIpSLAGlobalEnable_Type()
)
zhoneIpSLAGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLAGlobalEnable.setStatus("current")


class _ZhoneIpSLAGlobalPollInterval_Type(Integer32):
    """Custom type zhoneIpSLAGlobalPollInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_ZhoneIpSLAGlobalPollInterval_Type.__name__ = "Integer32"
_ZhoneIpSLAGlobalPollInterval_Object = MibScalar
zhoneIpSLAGlobalPollInterval = _ZhoneIpSLAGlobalPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 2),
    _ZhoneIpSLAGlobalPollInterval_Type()
)
zhoneIpSLAGlobalPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLAGlobalPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLAGlobalPollInterval.setUnits("seconds")
_ZhoneIpSLACosActionTable_Object = MibTable
zhoneIpSLACosActionTable = _ZhoneIpSLACosActionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneIpSLACosActionTable.setStatus("current")
_ZhoneIpSLACosActionEntry_Object = MibTableRow
zhoneIpSLACosActionEntry = _ZhoneIpSLACosActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1)
)
zhoneIpSLACosActionEntry.setIndexNames(
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionIndex"),
)
if mibBuilder.loadTexts:
    zhoneIpSLACosActionEntry.setStatus("current")


class _ZhoneIpSLACosActionIndex_Type(Integer32):
    """Custom type zhoneIpSLACosActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZhoneIpSLACosActionIndex_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionIndex_Object = MibTableColumn
zhoneIpSLACosActionIndex = _ZhoneIpSLACosActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 1),
    _ZhoneIpSLACosActionIndex_Type()
)
zhoneIpSLACosActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionIndex.setStatus("current")


class _ZhoneIpSLACosActionName_Type(OctetString):
    """Custom type zhoneIpSLACosActionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_ZhoneIpSLACosActionName_Type.__name__ = "OctetString"
_ZhoneIpSLACosActionName_Object = MibTableColumn
zhoneIpSLACosActionName = _ZhoneIpSLACosActionName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 2),
    _ZhoneIpSLACosActionName_Type()
)
zhoneIpSLACosActionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionName.setStatus("current")


class _ZhoneIpSLACosActionTrapOnError_Type(Integer32):
    """Custom type zhoneIpSLACosActionTrapOnError based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ZhoneIpSLACosActionTrapOnError_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionTrapOnError_Object = MibTableColumn
zhoneIpSLACosActionTrapOnError = _ZhoneIpSLACosActionTrapOnError_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 3),
    _ZhoneIpSLACosActionTrapOnError_Type()
)
zhoneIpSLACosActionTrapOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionTrapOnError.setStatus("current")


class _ZhoneIpSLACosActionTimeoutErrThresh_Type(Integer32):
    """Custom type zhoneIpSLACosActionTimeoutErrThresh based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ZhoneIpSLACosActionTimeoutErrThresh_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionTimeoutErrThresh_Object = MibTableColumn
zhoneIpSLACosActionTimeoutErrThresh = _ZhoneIpSLACosActionTimeoutErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 4),
    _ZhoneIpSLACosActionTimeoutErrThresh_Type()
)
zhoneIpSLACosActionTimeoutErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionTimeoutErrThresh.setStatus("current")


class _ZhoneIpSLACosActionTimeoutClrThresh_Type(Integer32):
    """Custom type zhoneIpSLACosActionTimeoutClrThresh based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ZhoneIpSLACosActionTimeoutClrThresh_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionTimeoutClrThresh_Object = MibTableColumn
zhoneIpSLACosActionTimeoutClrThresh = _ZhoneIpSLACosActionTimeoutClrThresh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 5),
    _ZhoneIpSLACosActionTimeoutClrThresh_Type()
)
zhoneIpSLACosActionTimeoutClrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionTimeoutClrThresh.setStatus("current")


class _ZhoneIpSLACosActionLatencyErrThresh_Type(Integer32):
    """Custom type zhoneIpSLACosActionLatencyErrThresh based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_ZhoneIpSLACosActionLatencyErrThresh_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionLatencyErrThresh_Object = MibTableColumn
zhoneIpSLACosActionLatencyErrThresh = _ZhoneIpSLACosActionLatencyErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 6),
    _ZhoneIpSLACosActionLatencyErrThresh_Type()
)
zhoneIpSLACosActionLatencyErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionLatencyErrThresh.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionLatencyErrThresh.setUnits("milliseconds")


class _ZhoneIpSLACosActionLatencyClrThresh_Type(Integer32):
    """Custom type zhoneIpSLACosActionLatencyClrThresh based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ZhoneIpSLACosActionLatencyClrThresh_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionLatencyClrThresh_Object = MibTableColumn
zhoneIpSLACosActionLatencyClrThresh = _ZhoneIpSLACosActionLatencyClrThresh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 7),
    _ZhoneIpSLACosActionLatencyClrThresh_Type()
)
zhoneIpSLACosActionLatencyClrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionLatencyClrThresh.setStatus("current")


class _ZhoneIpSLACosActionJitterErrThresh_Type(Integer32):
    """Custom type zhoneIpSLACosActionJitterErrThresh based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_ZhoneIpSLACosActionJitterErrThresh_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionJitterErrThresh_Object = MibTableColumn
zhoneIpSLACosActionJitterErrThresh = _ZhoneIpSLACosActionJitterErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 8),
    _ZhoneIpSLACosActionJitterErrThresh_Type()
)
zhoneIpSLACosActionJitterErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionJitterErrThresh.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionJitterErrThresh.setUnits("milliseconds")


class _ZhoneIpSLACosActionJitterClrThresh_Type(Integer32):
    """Custom type zhoneIpSLACosActionJitterClrThresh based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ZhoneIpSLACosActionJitterClrThresh_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionJitterClrThresh_Object = MibTableColumn
zhoneIpSLACosActionJitterClrThresh = _ZhoneIpSLACosActionJitterClrThresh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 9),
    _ZhoneIpSLACosActionJitterClrThresh_Type()
)
zhoneIpSLACosActionJitterClrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionJitterClrThresh.setStatus("current")


class _ZhoneIpSLACosActionMetrics_Type(Integer32):
    """Custom type zhoneIpSLACosActionMetrics based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ZhoneIpSLACosActionMetrics_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionMetrics_Object = MibTableColumn
zhoneIpSLACosActionMetrics = _ZhoneIpSLACosActionMetrics_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 10),
    _ZhoneIpSLACosActionMetrics_Type()
)
zhoneIpSLACosActionMetrics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionMetrics.setStatus("current")


class _ZhoneIpSLACosActionPacketSize_Type(Integer32):
    """Custom type zhoneIpSLACosActionPacketSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2048),
    )


_ZhoneIpSLACosActionPacketSize_Type.__name__ = "Integer32"
_ZhoneIpSLACosActionPacketSize_Object = MibTableColumn
zhoneIpSLACosActionPacketSize = _ZhoneIpSLACosActionPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 3, 1, 11),
    _ZhoneIpSLACosActionPacketSize_Type()
)
zhoneIpSLACosActionPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionPacketSize.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLACosActionPacketSize.setUnits("octets")
_ZhoneIpSLACosMapTable_Object = MibTable
zhoneIpSLACosMapTable = _ZhoneIpSLACosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 4)
)
if mibBuilder.loadTexts:
    zhoneIpSLACosMapTable.setStatus("current")
_ZhoneIpSLACosMapEntry_Object = MibTableRow
zhoneIpSLACosMapEntry = _ZhoneIpSLACosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 4, 1)
)
zhoneIpSLACosMapEntry.setIndexNames(
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosMapDscpIndex"),
)
if mibBuilder.loadTexts:
    zhoneIpSLACosMapEntry.setStatus("current")


class _ZhoneIpSLACosMapDscpIndex_Type(Integer32):
    """Custom type zhoneIpSLACosMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ZhoneIpSLACosMapDscpIndex_Type.__name__ = "Integer32"
_ZhoneIpSLACosMapDscpIndex_Object = MibTableColumn
zhoneIpSLACosMapDscpIndex = _ZhoneIpSLACosMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 4, 1, 1),
    _ZhoneIpSLACosMapDscpIndex_Type()
)
zhoneIpSLACosMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLACosMapDscpIndex.setStatus("current")


class _ZhoneIpSLACosMapCosActionIndex_Type(Integer32):
    """Custom type zhoneIpSLACosMapCosActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZhoneIpSLACosMapCosActionIndex_Type.__name__ = "Integer32"
_ZhoneIpSLACosMapCosActionIndex_Object = MibTableColumn
zhoneIpSLACosMapCosActionIndex = _ZhoneIpSLACosMapCosActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 4, 1, 2),
    _ZhoneIpSLACosMapCosActionIndex_Type()
)
zhoneIpSLACosMapCosActionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLACosMapCosActionIndex.setStatus("current")
_ZhoneIpSLAStaticPathTable_Object = MibTable
zhoneIpSLAStaticPathTable = _ZhoneIpSLAStaticPathTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 5)
)
if mibBuilder.loadTexts:
    zhoneIpSLAStaticPathTable.setStatus("current")
_ZhoneIpSLAStaticPathEntry_Object = MibTableRow
zhoneIpSLAStaticPathEntry = _ZhoneIpSLAStaticPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 5, 1)
)
zhoneIpSLAStaticPathEntry.setIndexNames(
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAStaticPathRdIndex"),
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAStaticPathTargetIP"),
)
if mibBuilder.loadTexts:
    zhoneIpSLAStaticPathEntry.setStatus("current")


class _ZhoneIpSLAStaticPathRdIndex_Type(ZhoneRDIndex):
    """Custom type zhoneIpSLAStaticPathRdIndex based on ZhoneRDIndex"""
    subtypeSpec = ZhoneRDIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZhoneIpSLAStaticPathRdIndex_Type.__name__ = "ZhoneRDIndex"
_ZhoneIpSLAStaticPathRdIndex_Object = MibTableColumn
zhoneIpSLAStaticPathRdIndex = _ZhoneIpSLAStaticPathRdIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 5, 1, 1),
    _ZhoneIpSLAStaticPathRdIndex_Type()
)
zhoneIpSLAStaticPathRdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLAStaticPathRdIndex.setStatus("current")
_ZhoneIpSLAStaticPathTargetIP_Type = IpAddress
_ZhoneIpSLAStaticPathTargetIP_Object = MibTableColumn
zhoneIpSLAStaticPathTargetIP = _ZhoneIpSLAStaticPathTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 5, 1, 2),
    _ZhoneIpSLAStaticPathTargetIP_Type()
)
zhoneIpSLAStaticPathTargetIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLAStaticPathTargetIP.setStatus("current")


class _ZhoneIpSLAStaticPathForwarding_Type(Integer32):
    """Custom type zhoneIpSLAStaticPathForwarding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ZhoneIpSLAStaticPathForwarding_Type.__name__ = "Integer32"
_ZhoneIpSLAStaticPathForwarding_Object = MibTableColumn
zhoneIpSLAStaticPathForwarding = _ZhoneIpSLAStaticPathForwarding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 5, 1, 3),
    _ZhoneIpSLAStaticPathForwarding_Type()
)
zhoneIpSLAStaticPathForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIpSLAStaticPathForwarding.setStatus("current")


class _ZhoneIpSLAStaticPathState_Type(Integer32):
    """Custom type zhoneIpSLAStaticPathState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ZhoneIpSLAStaticPathState_Type.__name__ = "Integer32"
_ZhoneIpSLAStaticPathState_Object = MibTableColumn
zhoneIpSLAStaticPathState = _ZhoneIpSLAStaticPathState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 5, 1, 4),
    _ZhoneIpSLAStaticPathState_Type()
)
zhoneIpSLAStaticPathState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIpSLAStaticPathState.setStatus("current")
_ZhoneIpSLAStaticPathRowstatus_Type = RowStatus
_ZhoneIpSLAStaticPathRowstatus_Object = MibTableColumn
zhoneIpSLAStaticPathRowstatus = _ZhoneIpSLAStaticPathRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 5, 1, 5),
    _ZhoneIpSLAStaticPathRowstatus_Type()
)
zhoneIpSLAStaticPathRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIpSLAStaticPathRowstatus.setStatus("current")
_ZhoneIpSLAPathConnectTable_Object = MibTable
zhoneIpSLAPathConnectTable = _ZhoneIpSLAPathConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6)
)
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectTable.setStatus("current")
_ZhoneIpSLAPathConnectEntry_Object = MibTableRow
zhoneIpSLAPathConnectEntry = _ZhoneIpSLAPathConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1)
)
zhoneIpSLAPathConnectEntry.setIndexNames(
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectEndpointIP"),
)
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectEntry.setStatus("current")
_ZhoneIpSLAPathConnectEndpointIP_Type = IpAddress
_ZhoneIpSLAPathConnectEndpointIP_Object = MibTableColumn
zhoneIpSLAPathConnectEndpointIP = _ZhoneIpSLAPathConnectEndpointIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 1),
    _ZhoneIpSLAPathConnectEndpointIP_Type()
)
zhoneIpSLAPathConnectEndpointIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectEndpointIP.setStatus("current")


class _ZhoneIpSLAPathConnectDevName_Type(OctetString):
    """Custom type zhoneIpSLAPathConnectDevName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZhoneIpSLAPathConnectDevName_Type.__name__ = "OctetString"
_ZhoneIpSLAPathConnectDevName_Object = MibTableColumn
zhoneIpSLAPathConnectDevName = _ZhoneIpSLAPathConnectDevName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 2),
    _ZhoneIpSLAPathConnectDevName_Type()
)
zhoneIpSLAPathConnectDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectDevName.setStatus("current")


class _ZhoneIpSLAPathConnectDevType_Type(OctetString):
    """Custom type zhoneIpSLAPathConnectDevType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ZhoneIpSLAPathConnectDevType_Type.__name__ = "OctetString"
_ZhoneIpSLAPathConnectDevType_Object = MibTableColumn
zhoneIpSLAPathConnectDevType = _ZhoneIpSLAPathConnectDevType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 3),
    _ZhoneIpSLAPathConnectDevType_Type()
)
zhoneIpSLAPathConnectDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectDevType.setStatus("current")


class _ZhoneIpSLAPathConnectStatus_Type(Integer32):
    """Custom type zhoneIpSLAPathConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ZhoneIpSLAPathConnectStatus_Type.__name__ = "Integer32"
_ZhoneIpSLAPathConnectStatus_Object = MibTableColumn
zhoneIpSLAPathConnectStatus = _ZhoneIpSLAPathConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 4),
    _ZhoneIpSLAPathConnectStatus_Type()
)
zhoneIpSLAPathConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectStatus.setStatus("current")
_ZhoneIpSLAPathConnectSrcIP_Type = IpAddress
_ZhoneIpSLAPathConnectSrcIP_Object = MibTableColumn
zhoneIpSLAPathConnectSrcIP = _ZhoneIpSLAPathConnectSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 5),
    _ZhoneIpSLAPathConnectSrcIP_Type()
)
zhoneIpSLAPathConnectSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectSrcIP.setStatus("current")


class _ZhoneIpSLAPathConnectDiscoveryType_Type(Integer32):
    """Custom type zhoneIpSLAPathConnectDiscoveryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_ZhoneIpSLAPathConnectDiscoveryType_Type.__name__ = "Integer32"
_ZhoneIpSLAPathConnectDiscoveryType_Object = MibTableColumn
zhoneIpSLAPathConnectDiscoveryType = _ZhoneIpSLAPathConnectDiscoveryType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 6),
    _ZhoneIpSLAPathConnectDiscoveryType_Type()
)
zhoneIpSLAPathConnectDiscoveryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectDiscoveryType.setStatus("current")
_ZhoneIpSLAPathConnectUpTime_Type = Counter32
_ZhoneIpSLAPathConnectUpTime_Object = MibTableColumn
zhoneIpSLAPathConnectUpTime = _ZhoneIpSLAPathConnectUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 7),
    _ZhoneIpSLAPathConnectUpTime_Type()
)
zhoneIpSLAPathConnectUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectUpTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectUpTime.setUnits("seconds")


class _ZhoneIpSLAPathConnectPollType_Type(Integer32):
    """Custom type zhoneIpSLAPathConnectPollType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("responder", 2))
    )


_ZhoneIpSLAPathConnectPollType_Type.__name__ = "Integer32"
_ZhoneIpSLAPathConnectPollType_Object = MibTableColumn
zhoneIpSLAPathConnectPollType = _ZhoneIpSLAPathConnectPollType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 8),
    _ZhoneIpSLAPathConnectPollType_Type()
)
zhoneIpSLAPathConnectPollType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectPollType.setStatus("current")
_ZhoneIpSLAPathConnectCosMismatch_Type = Counter32
_ZhoneIpSLAPathConnectCosMismatch_Object = MibTableColumn
zhoneIpSLAPathConnectCosMismatch = _ZhoneIpSLAPathConnectCosMismatch_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 9),
    _ZhoneIpSLAPathConnectCosMismatch_Type()
)
zhoneIpSLAPathConnectCosMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectCosMismatch.setStatus("current")


class _ZhoneIpSLAPathConnectLastCosActionIndex_Type(Integer32):
    """Custom type zhoneIpSLAPathConnectLastCosActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZhoneIpSLAPathConnectLastCosActionIndex_Type.__name__ = "Integer32"
_ZhoneIpSLAPathConnectLastCosActionIndex_Object = MibTableColumn
zhoneIpSLAPathConnectLastCosActionIndex = _ZhoneIpSLAPathConnectLastCosActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 6, 1, 10),
    _ZhoneIpSLAPathConnectLastCosActionIndex_Type()
)
zhoneIpSLAPathConnectLastCosActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectLastCosActionIndex.setStatus("current")
_ZhoneIpSLAPathStatByCOSTable_Object = MibTable
zhoneIpSLAPathStatByCOSTable = _ZhoneIpSLAPathStatByCOSTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7)
)
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSTable.setStatus("current")
_ZhoneIpSLAPathStatByCOSEntry_Object = MibTableRow
zhoneIpSLAPathStatByCOSEntry = _ZhoneIpSLAPathStatByCOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7, 1)
)
zhoneIpSLAPathStatByCOSEntry.setIndexNames(
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSCosActIndex"),
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSTargetIP"),
)
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSEntry.setStatus("current")


class _ZhoneIpSLAPathStatByCOSCosActIndex_Type(Integer32):
    """Custom type zhoneIpSLAPathStatByCOSCosActIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZhoneIpSLAPathStatByCOSCosActIndex_Type.__name__ = "Integer32"
_ZhoneIpSLAPathStatByCOSCosActIndex_Object = MibTableColumn
zhoneIpSLAPathStatByCOSCosActIndex = _ZhoneIpSLAPathStatByCOSCosActIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7, 1, 1),
    _ZhoneIpSLAPathStatByCOSCosActIndex_Type()
)
zhoneIpSLAPathStatByCOSCosActIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSCosActIndex.setStatus("current")
_ZhoneIpSLAPathStatByCOSTargetIP_Type = IpAddress
_ZhoneIpSLAPathStatByCOSTargetIP_Object = MibTableColumn
zhoneIpSLAPathStatByCOSTargetIP = _ZhoneIpSLAPathStatByCOSTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7, 1, 2),
    _ZhoneIpSLAPathStatByCOSTargetIP_Type()
)
zhoneIpSLAPathStatByCOSTargetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSTargetIP.setStatus("current")


class _ZhoneIpSLAPathStatByCOSStatus_Type(Integer32):
    """Custom type zhoneIpSLAPathStatByCOSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_ZhoneIpSLAPathStatByCOSStatus_Type.__name__ = "Integer32"
_ZhoneIpSLAPathStatByCOSStatus_Object = MibTableColumn
zhoneIpSLAPathStatByCOSStatus = _ZhoneIpSLAPathStatByCOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7, 1, 3),
    _ZhoneIpSLAPathStatByCOSStatus_Type()
)
zhoneIpSLAPathStatByCOSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSStatus.setStatus("current")
_ZhoneIpSLAPathStatByCOSLastRTT_Type = Counter32
_ZhoneIpSLAPathStatByCOSLastRTT_Object = MibTableColumn
zhoneIpSLAPathStatByCOSLastRTT = _ZhoneIpSLAPathStatByCOSLastRTT_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7, 1, 4),
    _ZhoneIpSLAPathStatByCOSLastRTT_Type()
)
zhoneIpSLAPathStatByCOSLastRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSLastRTT.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSLastRTT.setUnits("milliseconds")
_ZhoneIpSLAPathStatByCOSMinRTT_Type = Counter32
_ZhoneIpSLAPathStatByCOSMinRTT_Object = MibTableColumn
zhoneIpSLAPathStatByCOSMinRTT = _ZhoneIpSLAPathStatByCOSMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7, 1, 5),
    _ZhoneIpSLAPathStatByCOSMinRTT_Type()
)
zhoneIpSLAPathStatByCOSMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSMinRTT.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSMinRTT.setUnits("milliseconds")
_ZhoneIpSLAPathStatByCOSAvgRTT_Type = Counter32
_ZhoneIpSLAPathStatByCOSAvgRTT_Object = MibTableColumn
zhoneIpSLAPathStatByCOSAvgRTT = _ZhoneIpSLAPathStatByCOSAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7, 1, 6),
    _ZhoneIpSLAPathStatByCOSAvgRTT_Type()
)
zhoneIpSLAPathStatByCOSAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSAvgRTT.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSAvgRTT.setUnits("milliseconds")
_ZhoneIpSLAPathStatByCOSMaxRTT_Type = Counter32
_ZhoneIpSLAPathStatByCOSMaxRTT_Object = MibTableColumn
zhoneIpSLAPathStatByCOSMaxRTT = _ZhoneIpSLAPathStatByCOSMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7, 1, 7),
    _ZhoneIpSLAPathStatByCOSMaxRTT_Type()
)
zhoneIpSLAPathStatByCOSMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSMaxRTT.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSMaxRTT.setUnits("milliseconds")
_ZhoneIpSLAPathStatByCOSDroppedResp_Type = Counter32
_ZhoneIpSLAPathStatByCOSDroppedResp_Object = MibTableColumn
zhoneIpSLAPathStatByCOSDroppedResp = _ZhoneIpSLAPathStatByCOSDroppedResp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 7, 1, 8),
    _ZhoneIpSLAPathStatByCOSDroppedResp_Type()
)
zhoneIpSLAPathStatByCOSDroppedResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSDroppedResp.setStatus("current")
_ZhoneIpSLAPathStatByIntervalTable_Object = MibTable
zhoneIpSLAPathStatByIntervalTable = _ZhoneIpSLAPathStatByIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8)
)
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalTable.setStatus("current")
_ZhoneIpSLAPathStatByIntervalEntry_Object = MibTableRow
zhoneIpSLAPathStatByIntervalEntry = _ZhoneIpSLAPathStatByIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1)
)
zhoneIpSLAPathStatByIntervalEntry.setIndexNames(
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalIndex"),
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalCosActIndex"),
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalRdIndex"),
    (0, "ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalTargetIP"),
)
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalEntry.setStatus("current")


class _ZhoneIpSLAPathStatByIntervalIndex_Type(Integer32):
    """Custom type zhoneIpSLAPathStatByIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ZhoneIpSLAPathStatByIntervalIndex_Type.__name__ = "Integer32"
_ZhoneIpSLAPathStatByIntervalIndex_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalIndex = _ZhoneIpSLAPathStatByIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 1),
    _ZhoneIpSLAPathStatByIntervalIndex_Type()
)
zhoneIpSLAPathStatByIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalIndex.setStatus("current")


class _ZhoneIpSLAPathStatByIntervalCosActIndex_Type(Integer32):
    """Custom type zhoneIpSLAPathStatByIntervalCosActIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZhoneIpSLAPathStatByIntervalCosActIndex_Type.__name__ = "Integer32"
_ZhoneIpSLAPathStatByIntervalCosActIndex_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalCosActIndex = _ZhoneIpSLAPathStatByIntervalCosActIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 2),
    _ZhoneIpSLAPathStatByIntervalCosActIndex_Type()
)
zhoneIpSLAPathStatByIntervalCosActIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalCosActIndex.setStatus("current")


class _ZhoneIpSLAPathStatByIntervalRdIndex_Type(ZhoneRDIndex):
    """Custom type zhoneIpSLAPathStatByIntervalRdIndex based on ZhoneRDIndex"""
    subtypeSpec = ZhoneRDIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZhoneIpSLAPathStatByIntervalRdIndex_Type.__name__ = "ZhoneRDIndex"
_ZhoneIpSLAPathStatByIntervalRdIndex_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalRdIndex = _ZhoneIpSLAPathStatByIntervalRdIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 3),
    _ZhoneIpSLAPathStatByIntervalRdIndex_Type()
)
zhoneIpSLAPathStatByIntervalRdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalRdIndex.setStatus("current")
_ZhoneIpSLAPathStatByIntervalTargetIP_Type = IpAddress
_ZhoneIpSLAPathStatByIntervalTargetIP_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalTargetIP = _ZhoneIpSLAPathStatByIntervalTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 4),
    _ZhoneIpSLAPathStatByIntervalTargetIP_Type()
)
zhoneIpSLAPathStatByIntervalTargetIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalTargetIP.setStatus("current")
_ZhoneIpSLAPathStatByIntervalDateTime_Type = DateAndTime
_ZhoneIpSLAPathStatByIntervalDateTime_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalDateTime = _ZhoneIpSLAPathStatByIntervalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 5),
    _ZhoneIpSLAPathStatByIntervalDateTime_Type()
)
zhoneIpSLAPathStatByIntervalDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalDateTime.setStatus("current")


class _ZhoneIpSLAPathStatByIntervalStatus_Type(Integer32):
    """Custom type zhoneIpSLAPathStatByIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_ZhoneIpSLAPathStatByIntervalStatus_Type.__name__ = "Integer32"
_ZhoneIpSLAPathStatByIntervalStatus_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalStatus = _ZhoneIpSLAPathStatByIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 6),
    _ZhoneIpSLAPathStatByIntervalStatus_Type()
)
zhoneIpSLAPathStatByIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalStatus.setStatus("current")
_ZhoneIpSLAPathStatByIntervalMinRTT_Type = Counter32
_ZhoneIpSLAPathStatByIntervalMinRTT_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalMinRTT = _ZhoneIpSLAPathStatByIntervalMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 7),
    _ZhoneIpSLAPathStatByIntervalMinRTT_Type()
)
zhoneIpSLAPathStatByIntervalMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalMinRTT.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalMinRTT.setUnits("milliseconds")
_ZhoneIpSLAPathStatByIntervalAvgRTT_Type = Counter32
_ZhoneIpSLAPathStatByIntervalAvgRTT_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalAvgRTT = _ZhoneIpSLAPathStatByIntervalAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 8),
    _ZhoneIpSLAPathStatByIntervalAvgRTT_Type()
)
zhoneIpSLAPathStatByIntervalAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalAvgRTT.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalAvgRTT.setUnits("milliseconds")
_ZhoneIpSLAPathStatByIntervalMaxRTT_Type = Counter32
_ZhoneIpSLAPathStatByIntervalMaxRTT_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalMaxRTT = _ZhoneIpSLAPathStatByIntervalMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 9),
    _ZhoneIpSLAPathStatByIntervalMaxRTT_Type()
)
zhoneIpSLAPathStatByIntervalMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalMaxRTT.setStatus("current")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalMaxRTT.setUnits("milliseconds")
_ZhoneIpSLAPathStatByIntervalDroppedResp_Type = Counter32
_ZhoneIpSLAPathStatByIntervalDroppedResp_Object = MibTableColumn
zhoneIpSLAPathStatByIntervalDroppedResp = _ZhoneIpSLAPathStatByIntervalDroppedResp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 1, 8, 1, 10),
    _ZhoneIpSLAPathStatByIntervalDroppedResp_Type()
)
zhoneIpSLAPathStatByIntervalDroppedResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalDroppedResp.setStatus("current")
_ZhoneIpSLATraps_ObjectIdentity = ObjectIdentity
zhoneIpSLATraps = _ZhoneIpSLATraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 2)
)
_ZhoneIpSLATrapsPrefix_ObjectIdentity = ObjectIdentity
zhoneIpSLATrapsPrefix = _ZhoneIpSLATrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 2, 0)
)
if mibBuilder.loadTexts:
    zhoneIpSLATrapsPrefix.setStatus("current")
_ZhoneIpSLAConformance_ObjectIdentity = ObjectIdentity
zhoneIpSLAConformance = _ZhoneIpSLAConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3)
)
_ZhoneIpSLAMIBGroups_ObjectIdentity = ObjectIdentity
zhoneIpSLAMIBGroups = _ZhoneIpSLAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 1)
)
_ZhoneIpSLACompliances_ObjectIdentity = ObjectIdentity
zhoneIpSLACompliances = _ZhoneIpSLACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 2)
)

# Managed Objects groups

zhoneIpSLAGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 1, 1)
)
zhoneIpSLAGlobalsGroup.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAGlobalEnable"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAGlobalPollInterval"))
)
if mibBuilder.loadTexts:
    zhoneIpSLAGlobalsGroup.setStatus("current")

zhoneIpSLACosActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 1, 2)
)
zhoneIpSLACosActionGroup.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionName"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionTrapOnError"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionTimeoutErrThresh"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionTimeoutClrThresh"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionLatencyErrThresh"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionLatencyClrThresh"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionJitterErrThresh"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionJitterClrThresh"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionMetrics"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionPacketSize"))
)
if mibBuilder.loadTexts:
    zhoneIpSLACosActionGroup.setStatus("current")

zhoneIpSLACOSMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 1, 3)
)
zhoneIpSLACOSMapGroup.setObjects(
    ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosMapCosActionIndex")
)
if mibBuilder.loadTexts:
    zhoneIpSLACOSMapGroup.setStatus("current")

zhoneIpSLAStaticPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 1, 4)
)
zhoneIpSLAStaticPathGroup.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAStaticPathForwarding"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAStaticPathState"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAStaticPathRowstatus"))
)
if mibBuilder.loadTexts:
    zhoneIpSLAStaticPathGroup.setStatus("current")

zhoneIpSLAPathConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 1, 5)
)
zhoneIpSLAPathConnectGroup.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectDevName"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectDevType"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectStatus"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectSrcIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectDiscoveryType"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectUpTime"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectPollType"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectCosMismatch"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectLastCosActionIndex"))
)
if mibBuilder.loadTexts:
    zhoneIpSLAPathConnectGroup.setStatus("current")

zhoneIpSLAPathStatByCOSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 1, 6)
)
zhoneIpSLAPathStatByCOSGroup.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSTargetIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSStatus"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSLastRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSMinRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSAvgRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSMaxRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSDroppedResp"))
)
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByCOSGroup.setStatus("current")

zhoneIpSLAPathStatByIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 1, 7)
)
zhoneIpSLAPathStatByIntervalGroup.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalDateTime"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalStatus"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalMinRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalAvgRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalMaxRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByIntervalDroppedResp"))
)
if mibBuilder.loadTexts:
    zhoneIpSLAPathStatByIntervalGroup.setStatus("current")


# Notification objects

zhoneIpSLATimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 2, 0, 1)
)
zhoneIpSLATimeoutTrap.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectSrcIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSTargetIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionName"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSDroppedResp"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionTimeoutErrThresh"))
)
if mibBuilder.loadTexts:
    zhoneIpSLATimeoutTrap.setStatus(
        "current"
    )

zhoneIpSLALatencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 2, 0, 2)
)
zhoneIpSLALatencyTrap.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectSrcIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSTargetIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionName"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSAvgRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionLatencyErrThresh"))
)
if mibBuilder.loadTexts:
    zhoneIpSLALatencyTrap.setStatus(
        "current"
    )

zhoneIpSLAJitterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 2, 0, 3)
)
zhoneIpSLAJitterTrap.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectSrcIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSTargetIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionName"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSMinRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSMaxRTT"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionJitterErrThresh"))
)
if mibBuilder.loadTexts:
    zhoneIpSLAJitterTrap.setStatus(
        "current"
    )

zhoneIpSLATimeoutClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 2, 0, 4)
)
zhoneIpSLATimeoutClearTrap.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectSrcIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSTargetIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionName"))
)
if mibBuilder.loadTexts:
    zhoneIpSLATimeoutClearTrap.setStatus(
        "current"
    )

zhoneIpSLALatencyClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 2, 0, 5)
)
zhoneIpSLALatencyClearTrap.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectSrcIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSTargetIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionName"))
)
if mibBuilder.loadTexts:
    zhoneIpSLALatencyClearTrap.setStatus(
        "current"
    )

zhoneIpSLAJitterClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 2, 0, 6)
)
zhoneIpSLAJitterClearTrap.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathConnectSrcIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAPathStatByCOSTargetIP"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLACosActionName"))
)
if mibBuilder.loadTexts:
    zhoneIpSLAJitterClearTrap.setStatus(
        "current"
    )


# Notifications groups

zhoneIpSLANotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 1, 8)
)
zhoneIpSLANotificationGroup.setObjects(
      *(("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLATimeoutTrap"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLALatencyTrap"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAJitterTrap"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLATimeoutClearTrap"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLALatencyClearTrap"),
        ("ZHONE-COM-IP-IPSLA-MIB", "zhoneIpSLAJitterClearTrap"))
)
if mibBuilder.loadTexts:
    zhoneIpSLANotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

zhoneIpSLACompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 21, 3, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneIpSLACompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-IPSLA-MIB",
    **{"zhoneIpSLA": zhoneIpSLA,
       "zhoneIpSLAMibObjects": zhoneIpSLAMibObjects,
       "zhoneIpSLAGlobalEnable": zhoneIpSLAGlobalEnable,
       "zhoneIpSLAGlobalPollInterval": zhoneIpSLAGlobalPollInterval,
       "zhoneIpSLACosActionTable": zhoneIpSLACosActionTable,
       "zhoneIpSLACosActionEntry": zhoneIpSLACosActionEntry,
       "zhoneIpSLACosActionIndex": zhoneIpSLACosActionIndex,
       "zhoneIpSLACosActionName": zhoneIpSLACosActionName,
       "zhoneIpSLACosActionTrapOnError": zhoneIpSLACosActionTrapOnError,
       "zhoneIpSLACosActionTimeoutErrThresh": zhoneIpSLACosActionTimeoutErrThresh,
       "zhoneIpSLACosActionTimeoutClrThresh": zhoneIpSLACosActionTimeoutClrThresh,
       "zhoneIpSLACosActionLatencyErrThresh": zhoneIpSLACosActionLatencyErrThresh,
       "zhoneIpSLACosActionLatencyClrThresh": zhoneIpSLACosActionLatencyClrThresh,
       "zhoneIpSLACosActionJitterErrThresh": zhoneIpSLACosActionJitterErrThresh,
       "zhoneIpSLACosActionJitterClrThresh": zhoneIpSLACosActionJitterClrThresh,
       "zhoneIpSLACosActionMetrics": zhoneIpSLACosActionMetrics,
       "zhoneIpSLACosActionPacketSize": zhoneIpSLACosActionPacketSize,
       "zhoneIpSLACosMapTable": zhoneIpSLACosMapTable,
       "zhoneIpSLACosMapEntry": zhoneIpSLACosMapEntry,
       "zhoneIpSLACosMapDscpIndex": zhoneIpSLACosMapDscpIndex,
       "zhoneIpSLACosMapCosActionIndex": zhoneIpSLACosMapCosActionIndex,
       "zhoneIpSLAStaticPathTable": zhoneIpSLAStaticPathTable,
       "zhoneIpSLAStaticPathEntry": zhoneIpSLAStaticPathEntry,
       "zhoneIpSLAStaticPathRdIndex": zhoneIpSLAStaticPathRdIndex,
       "zhoneIpSLAStaticPathTargetIP": zhoneIpSLAStaticPathTargetIP,
       "zhoneIpSLAStaticPathForwarding": zhoneIpSLAStaticPathForwarding,
       "zhoneIpSLAStaticPathState": zhoneIpSLAStaticPathState,
       "zhoneIpSLAStaticPathRowstatus": zhoneIpSLAStaticPathRowstatus,
       "zhoneIpSLAPathConnectTable": zhoneIpSLAPathConnectTable,
       "zhoneIpSLAPathConnectEntry": zhoneIpSLAPathConnectEntry,
       "zhoneIpSLAPathConnectEndpointIP": zhoneIpSLAPathConnectEndpointIP,
       "zhoneIpSLAPathConnectDevName": zhoneIpSLAPathConnectDevName,
       "zhoneIpSLAPathConnectDevType": zhoneIpSLAPathConnectDevType,
       "zhoneIpSLAPathConnectStatus": zhoneIpSLAPathConnectStatus,
       "zhoneIpSLAPathConnectSrcIP": zhoneIpSLAPathConnectSrcIP,
       "zhoneIpSLAPathConnectDiscoveryType": zhoneIpSLAPathConnectDiscoveryType,
       "zhoneIpSLAPathConnectUpTime": zhoneIpSLAPathConnectUpTime,
       "zhoneIpSLAPathConnectPollType": zhoneIpSLAPathConnectPollType,
       "zhoneIpSLAPathConnectCosMismatch": zhoneIpSLAPathConnectCosMismatch,
       "zhoneIpSLAPathConnectLastCosActionIndex": zhoneIpSLAPathConnectLastCosActionIndex,
       "zhoneIpSLAPathStatByCOSTable": zhoneIpSLAPathStatByCOSTable,
       "zhoneIpSLAPathStatByCOSEntry": zhoneIpSLAPathStatByCOSEntry,
       "zhoneIpSLAPathStatByCOSCosActIndex": zhoneIpSLAPathStatByCOSCosActIndex,
       "zhoneIpSLAPathStatByCOSTargetIP": zhoneIpSLAPathStatByCOSTargetIP,
       "zhoneIpSLAPathStatByCOSStatus": zhoneIpSLAPathStatByCOSStatus,
       "zhoneIpSLAPathStatByCOSLastRTT": zhoneIpSLAPathStatByCOSLastRTT,
       "zhoneIpSLAPathStatByCOSMinRTT": zhoneIpSLAPathStatByCOSMinRTT,
       "zhoneIpSLAPathStatByCOSAvgRTT": zhoneIpSLAPathStatByCOSAvgRTT,
       "zhoneIpSLAPathStatByCOSMaxRTT": zhoneIpSLAPathStatByCOSMaxRTT,
       "zhoneIpSLAPathStatByCOSDroppedResp": zhoneIpSLAPathStatByCOSDroppedResp,
       "zhoneIpSLAPathStatByIntervalTable": zhoneIpSLAPathStatByIntervalTable,
       "zhoneIpSLAPathStatByIntervalEntry": zhoneIpSLAPathStatByIntervalEntry,
       "zhoneIpSLAPathStatByIntervalIndex": zhoneIpSLAPathStatByIntervalIndex,
       "zhoneIpSLAPathStatByIntervalCosActIndex": zhoneIpSLAPathStatByIntervalCosActIndex,
       "zhoneIpSLAPathStatByIntervalRdIndex": zhoneIpSLAPathStatByIntervalRdIndex,
       "zhoneIpSLAPathStatByIntervalTargetIP": zhoneIpSLAPathStatByIntervalTargetIP,
       "zhoneIpSLAPathStatByIntervalDateTime": zhoneIpSLAPathStatByIntervalDateTime,
       "zhoneIpSLAPathStatByIntervalStatus": zhoneIpSLAPathStatByIntervalStatus,
       "zhoneIpSLAPathStatByIntervalMinRTT": zhoneIpSLAPathStatByIntervalMinRTT,
       "zhoneIpSLAPathStatByIntervalAvgRTT": zhoneIpSLAPathStatByIntervalAvgRTT,
       "zhoneIpSLAPathStatByIntervalMaxRTT": zhoneIpSLAPathStatByIntervalMaxRTT,
       "zhoneIpSLAPathStatByIntervalDroppedResp": zhoneIpSLAPathStatByIntervalDroppedResp,
       "zhoneIpSLATraps": zhoneIpSLATraps,
       "zhoneIpSLATrapsPrefix": zhoneIpSLATrapsPrefix,
       "zhoneIpSLATimeoutTrap": zhoneIpSLATimeoutTrap,
       "zhoneIpSLALatencyTrap": zhoneIpSLALatencyTrap,
       "zhoneIpSLAJitterTrap": zhoneIpSLAJitterTrap,
       "zhoneIpSLATimeoutClearTrap": zhoneIpSLATimeoutClearTrap,
       "zhoneIpSLALatencyClearTrap": zhoneIpSLALatencyClearTrap,
       "zhoneIpSLAJitterClearTrap": zhoneIpSLAJitterClearTrap,
       "zhoneIpSLAConformance": zhoneIpSLAConformance,
       "zhoneIpSLAMIBGroups": zhoneIpSLAMIBGroups,
       "zhoneIpSLAGlobalsGroup": zhoneIpSLAGlobalsGroup,
       "zhoneIpSLACosActionGroup": zhoneIpSLACosActionGroup,
       "zhoneIpSLACOSMapGroup": zhoneIpSLACOSMapGroup,
       "zhoneIpSLAStaticPathGroup": zhoneIpSLAStaticPathGroup,
       "zhoneIpSLAPathConnectGroup": zhoneIpSLAPathConnectGroup,
       "zhoneIpSLAPathStatByCOSGroup": zhoneIpSLAPathStatByCOSGroup,
       "zhoneIpSLAPathStatByIntervalGroup": zhoneIpSLAPathStatByIntervalGroup,
       "zhoneIpSLANotificationGroup": zhoneIpSLANotificationGroup,
       "zhoneIpSLACompliances": zhoneIpSLACompliances,
       "zhoneIpSLACompliance": zhoneIpSLACompliance}
)
